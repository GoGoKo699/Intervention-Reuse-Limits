#!/usr/bin/env python3
"""Exact checks for local binary-scenery response lower bounds.

Only path targets of two and three positions are built physically. Larger
witnesses use sparse position/Walsh coordinates and exact Gram sum-of-squares
identities. The fixed-clock check is an all-depth rational calibration, not
numerical rank inference or a large protocol enumeration.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

import verify_polynomial_controlled_lower_bound as logarithm
import verify_shift_register_lower_bound as reused


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def path_laplacian(m: int) -> sp.Matrix:
    result = sp.zeros(m)
    for i in range(m-1):
        result[i, i+1] = result[i+1, i] = 1
        result[i, i] -= 1
        result[i+1, i+1] -= 1
    return result


def physical_path(m: int) -> dict:
    strings = list(itertools.product((-1, 1), repeat=m))
    labels = [state[i] for state in strings for i in range(m)]
    N = m*2**m
    mu = sp.ones(1, N)/N
    g = sp.Matrix(labels)
    local = sp.kronecker_product(sp.eye(2**m), path_laplacian(m))/4
    K = local+sp.Rational(3, 2)*(sp.ones(N)/N-sp.eye(N))
    require(K == K.T and K*sp.ones(N, 1) == sp.zeros(N, 1),
            'Local walk plus refresh is a reversible generator')
    require(all(K[i, j] >= sp.Rational(3, 2*N)
                for i in range(N) for j in range(N) if i != j),
            'Refresh makes every distinct-state internal rate positive')
    require((mu*g)[0] == 0 and (g.T*g)[0]/N == 1,
            'Exact fair binary histogram, centering and variance')
    rates = [sp.simplify(2-sp.cos(sp.pi*j/m)/2) for j in range(m)]
    local_rates = sorted((-path_laplacian(m)/4).eigenvals())
    require(local_rates == sorted(sp.simplify(rate-sp.Rational(3, 2)) for rate in rates),
            'Exact reflecting-path cosine spectrum')
    require(all(sp.Rational(3, 2) <= rate <= sp.Rational(5, 2) and rate != 1
                for rate in rates) and len(set(rates)) == m,
            'Distinct noncolliding cubic relaxation rates in the shared band')
    value = g
    for degree in range(7):
        require(sp.simplify((g.T*value)[0]/N-sum(rate**degree for rate in rates)/m) == 0,
                'Exact full-state correlation moment equals the path trace')
        value = -K*value
    p = sp.symbols('p', positive=True)
    resolvent_trace = sp.trace(((p+sp.Rational(3, 2))*sp.eye(m)-path_laplacian(m)/4).inv())/m
    require(sp.cancel(resolvent_trace-sum(1/(p+rate) for rate in rates)/m) == 0,
            'Exact cubic correlation Laplace transform, not sampled times')

    z = sp.Rational(65, 64)
    u, cosine = (z-1/z)/2, (z+1/z)/2
    equilibrium0 = sp.Matrix([[sp.Rational(1, 2)]+[sp.Rational(1, 2*N)]*N])
    weight = sp.diag(*equilibrium0)
    output = sp.Matrix([-1]+[1]*N)
    root = sp.Matrix([0]+labels)
    generators = []
    for field in (sp.Integer(1), z):
        Q = sp.zeros(N+1)
        Q[1:, 1:] = K
        for j, label in enumerate(labels):
            Q[0, j+1] = field**(1+label)/N
            Q[j+1, 0] = field**(label-1)
            Q[j+1, j+1] -= Q[j+1, 0]
        Q[0, 0] = -sum(Q[0, j] for j in range(1, N+1))
        equilibrium = sp.Matrix([[1]+[field**2/N]*N])/(1+field**2)
        require(Q*sp.ones(N+1, 1) == sp.zeros(N+1, 1), 'Full physical generator row sums')
        require(equilibrium*Q == sp.zeros(1, N+1), 'Full finite-field stationarity')
        require(sp.diag(*equilibrium)*Q == Q.T*sp.diag(*equilibrium),
                'Full finite-field ordinary detailed balance')
        generators.append(Q)
    Q0, Qh = generators
    I = sp.eye(N+1)
    H = sp.zeros(N+1)
    H[1:, 1:] = sp.eye(N)-sp.ones(N)/N
    F = Q0*(Q0+2*I)/3
    require(F*H == F and H*F == F, 'Quadratic filter kills the entire two-state coarse space')
    B = H*sp.diag(*root)*H
    Z = [F*F, -F*(Qh-Q0-(1-cosine/z)*I)*F/(u/z)]
    require(Z[1] == F*B*F, 'Exact finite-field controlled binary toggle')
    ell, right = 2*u*u, -2*u/z
    require(equilibrium0*Qh*F == ell*(F*root).T*weight, 'Exact actual-mean left endpoint')
    require(F*Qh*output == right*F*root, 'Exact actual-mean right endpoint')
    columns = [letter*F*root for letter in Z]
    sparse_root = {(1 << position, position): sp.Integer(1) for position in range(m)}
    for toggle, column in enumerate(columns):
        sparse_column = sparse_F(sparse_F(sparse_root, m), m)
        if toggle:
            sparse_column = sparse_B(sparse_column, m)
        sparse_column = sparse_F(sparse_column, m)
        expanded = [sp.Integer(0)]
        for state in strings:
            for position in range(m):
                expanded.append(sum(value*sp.prod(state[j] for j in range(m) if mask & (1 << j))
                                    for (mask, site), value in sparse_column.items() if site == position))
        require(column == sp.Matrix(expanded), 'Sparse position-Walsh filter equals the full physical vector')
    for i, j in itertools.product(range(2), repeat=2):
        response = (equilibrium0*Qh*F*Z[i]*Z[j]*F*Qh*output)[0]/(ell*right)
        require(response == (columns[i].T*weight*columns[j])[0],
                'Actual physical mean polynomial equals the controlled Gram entry')
    require(sp.Rational(5, 2)+2*z*z < 5, 'Dimension-independent full-field spectral-cap certificate')
    return {'path_positions': m, 'scenery_strings': 2**m,
            'hidden_states': N, 'full_Markov_states': N+1,
            'exact_internal_rate_band': ['3/2', '5/2'],
            'actuator_histogram': {'-1': '1/2', '1': '1/2'},
            'correlation_relaxation_rates_exact': [str(rate) for rate in rates],
            'correlation_weights_exact': [str(sp.Rational(1, m))]*m,
            'full_state_correlation_moments_checked': 7,
            'exact_correlation_resolvent_trace_identity': True,
            'exact_cubic_minimum_analytic_competitor_class': m+2,
            'finite_field_stationarity_detailed_balance_and_Gram_endpoints': True,
            'sparse_Walsh_filters_match_physical_vectors_exact': True,
            'actual_mean_Gram_entries_checked_exact': 4,
            'field_h': 'log(65/64)',
            'scope': 'Physical identities are exact. The cubic minimum uses the distinct-pole/Jacobi theorem proved in the notes.'}


def sparse_add(*terms):
    result = {}
    for scale, vector in terms:
        for key, value in vector.items():
            result[key] = result.get(key, 0)+scale*value
    return {key: value for key, value in result.items() if value}


def sparse_Q(vector, m):
    # This is Q0 on the hidden-centered subspace. A Walsh-empty vector
    # remains centered over positions, so the refresh still acts as -3/2.
    result = {}
    for (mask, position), value in vector.items():
        neighbors = [j for j in (position-1, position+1) if 0 <= j < m]
        key = (mask, position)
        result[key] = result.get(key, 0)-(sp.Rational(5, 2)+sp.Rational(len(neighbors), 4))*value
        for neighbor in neighbors:
            key = (mask, neighbor)
            result[key] = result.get(key, 0)+value/4
    return {key: value for key, value in result.items() if value}


def sparse_F(vector, m):
    first = sparse_Q(vector, m)
    return sparse_add((sp.Rational(1, 3), sparse_Q(first, m)),
                      (sp.Rational(2, 3), first))


def sparse_B(vector, m):
    result = {(mask ^ (1 << position), position): value
              for (mask, position), value in vector.items()}
    mean = sum(value for (mask, position), value in result.items() if mask == 0)/m
    if mean:
        for position in range(m):
            key = (0, position)
            result[key] = result.get(key, 0)-mean
    return {key: value for key, value in result.items() if value}


def sparse_dot(first, second):
    return sum(value*second.get(key, 0) for key, value in first.items())


def sparse_leaf_check(n):
    m = 4*n+3
    coefficient = sp.Rational(1, 48)**(2*n+1)
    root = {(1 << position, position): sp.Integer(1) for position in range(m)}
    words = list(itertools.product((0, 1), repeat=n))
    columns, remainders, leaves = [], [], []
    for word in words:
        vector = sparse_F(root, m)
        for toggle in word:
            vector = sparse_F(vector, m)
            if toggle:
                vector = sparse_B(vector, m)
            vector = sparse_F(vector, m)
        leaf = (1+sum((1 << (4*j)) for j, toggle in enumerate(word, 1) if toggle), m-1)
        projection = {key: value for key, value in vector.items() if key[0] & 1 and key[1] == m-1}
        require(projection == {leaf: coefficient}, 'Unique maximal-travel leaf and exact coefficient')
        require(sum(value for (mask, position), value in vector.items() if mask == 0) == 0,
                'Empty-Walsh sector remains exactly centered, including global projection terms')
        columns.append(vector)
        remainders.append({key: value for key, value in vector.items() if key not in projection})
        leaves.append(leaf)
    require(len(set(leaves)) == 2**n, 'All binary control words have different leaf characters')
    Gram = sp.Matrix([[sparse_dot(v, w)/(2*m) for w in columns] for v in columns])
    remainder_Gram = sp.Matrix([[sparse_dot(v, w)/(2*m) for w in remainders] for v in remainders])
    floor = coefficient**2/(2*m)
    require(Gram-floor*sp.eye(2**n) == remainder_Gram, 'Exact full-pi0 Gram sum-of-squares identity')
    active = set().union(*(set(column) for column in columns))
    return {'word_depth_n': n, 'path_positions': m,
            'implicit_full_physical_target_states': m*2**m+1,
            'physical_state_space_enumerated': False,
            'controlled_Gram_dimension': 2**n,
            'active_position_Walsh_coordinates_evaluated': len(active),
            'largest_sparse_column_support': max(map(len, columns)),
            'top_leaf_coefficient_exact': str(coefficient),
            'top_leaf_matrix_is_coefficient_times_identity': True,
            'Gram_remainder_exact_sum_of_squares': True,
            'full_pi0_Gram_eigenvalue_floor': str(floor),
            'leaf_coordinates': [[mask, position] for mask, position in leaves]}


def rational_calibration():
    z = sp.Rational(65, 64)
    u, cosine = (z-1/z)/2, (z+1/z)/2
    b, scalar = u/z, 1-cosine/z
    normalization = 4*u**3/z
    require((2+abs(scalar))/b < 256, 'Controlled-letter coefficient sum is below 256')
    require(normalization > sp.Rational(1, 2**17), 'Exact actual-mean normalization floor')
    x = sp.Rational(5, 8)
    exponential_upper = 1+x+x*x/(2*(1-x/3))
    require(exponential_upper < 2, 'Taylor bound gives q=1-exp(-5/8)<1/2')
    require(z*8*2 < 32, 'Analytic log-generator norm below 32 at radius 3/2')
    # The former register calibration acquires the local-path factor 4n+3.
    # Its ratio at depth n+1 versus n is <=2 for every n>=1.
    n = sp.symbols('n', integer=True, positive=True)
    require(sp.expand(2*(4*n+3)-(4*(n+1)+3)) == 4*n-1,
            'Path-length multiplier grows by less than two at every positive depth')
    ratio_step = 2**68*48**4*sp.Rational(2, 3)**200
    require(ratio_step < 1, 'Exact all-depth error/floor ratio contracts')
    require(sp.expand(8*n+5*(5*n+3)-(33*n+15)) == 0, 'Analytic side exponent identity')
    require(sp.expand(8*n+3*(5*n+3)-(23*n+9)) == 0, 'Formal side coefficient exponent identity')
    require(4*1+3 <= 7 and 4*(n+1)+3 <= 7*(4*n+3),
            'Induction certifies 4n+3 <= 7^n < 2^(3n) for every n>=1')
    response_exponent = 24*n+13+3*n+1+n+46*n+35+4*200*(n+1)
    require(sp.expand(response_exponent-(874*n+849)) == 0, 'All-depth response exponent includes path length')
    records = []
    for depth in (1, 2, 3, 10):
        m, cutoff = 4*depth+3, 200*(depth+1)
        side_bound = sp.Integer(2)**(33*depth+15)
        tail = 3*side_bound*sp.Rational(2, 3)**(cutoff+1)
        require(tail < side_bound, 'Side truncation error is below the side norm bound')
        matrix_error = sp.Integer(2)**depth*3*side_bound*tail*2**17
        gram_floor = sp.Rational(1, 2*m*48**(4*depth+2))
        require(matrix_error < gram_floor/2, 'Truncation error is below half the local-walk leaf floor')
        side_budget = sp.Integer(2)**(23*depth+9+2*cutoff)
        entry_budget = side_budget**2*2**17
        response_floor = gram_floor/(2*2**depth*entry_budget)
        require(response_floor >= sp.Rational(1, 2**(874*depth+849)),
                'Exact response floor dominates the stated exponential-in-depth lower bound')
        with mp.workdps(80):
            records.append({'word_depth_n': depth, 'path_positions': m,
                            'whole_side_degree_cutoff': cutoff, 'maximum_horizon': str(sp.Rational(2*cutoff, 8)),
                            'exact_leaf_Gram_floor': str(gram_floor),
                            'matrix_error_log10': reused.digits(mp.log10(reused.number(matrix_error))),
                            'error_below_half_Gram_floor_exact': True,
                            'response_floor_log10': reused.digits(mp.log10(reused.number(response_floor))),
                            'simplified_response_floor': '2^(-%d)' % (874*depth+849)})
    return {'parameters': {'k': 1, 'G': 1, 'W': 1, 'H': 'log(65/64)', 'exp_h': str(z), 'dwell_a': '1/8'},
            'analytic_radius': '3/2', 'formal_majorant_radius': '1/4',
            'exp_5_over_8_rational_upper': str(exponential_upper),
            'actual_mean_normalization_absolute_exact': str(normalization),
            'all_depth_cutoff_formula': 'M=200(n+1)',
            'all_depth_error_to_floor_ratio_upper_multiplier': str(ratio_step),
            'all_depth_certificate': 'The base depth n=1 passes; the ratio decreases by at most the displayed exact multiplier. The factor 4n+3 is included.',
            'all_depth_response_floor': '2^(-874n-849), n>=1',
            'all_depth_protocol_horizon': '50(n+1), with each positive segment a multiple of 1/8',
            'records': records,
            'scope': 'One conservative exact rational field/dwell calibration. The arbitrary fixed-dwell claim is proved analytically in the note.'}


def cauchy_checks():
    records = []
    for r in (2, 3, 5, 6):
        # Rational nodes check the general inverse-Cauchy calculation used
        # after the cosine spacing argument; these are not path eigenvalues.
        nodes = [sp.Rational(13, 4)+sp.Rational(j, 3*r) for j in range(r)]
        C = sp.Matrix([[1/(a+b) for b in nodes] for a in nodes])
        inverse = C.inv()
        for i, node in enumerate(nodes):
            diagonal = 2*node*sp.prod(((node+nodes[j])/(node-nodes[j]))**2
                                     for j in range(r) if j != i)
            require(inverse[i, i] == diagonal, 'Exact inverse-Cauchy diagonal formula')
            require(diagonal <= 8*192**(2*r-2), 'A rational bound stronger than 8(96e)^(2r-2) on these examples')
        weight_floor = sp.Rational(32, 75*r)
        sigma = weight_floor/sp.trace(inverse)
        advertised_smaller_rational_bound = sp.Rational(4, 75*r*r*288**(2*r-2))
        require(sigma >= advertised_smaller_rational_bound,
                'Trace-of-inverse lower bound has the asserted exponential scale')
        records.append({'selected_nodes': r, 'nodes_exact': [str(a) for a in nodes],
                        'inverse_Cauchy_diagonal_formula_exact': True,
                        'weighted_trace_inverse_eigenvalue_floor': str(sigma),
                        'conservative_rational_floor': str(advertised_smaller_rational_bound)})
    return {'records': records,
            'scope': 'Small exact rational-node checks of the generic Cauchy calculation. The cosine spacing and all-rank bound are proved in the note, not inferred from these examples.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/local_walk_lower_bound.json'))
    args = parser.parse_args()
    report = {'status': 'PASS',
              'scope': 'Exact local-scenery physical generators, correlation trace and actual-mean Gram endpoints, sparse Walsh leaf/SOS identities, and all-depth fixed-clock calibration; no simulations or numerical rank tests.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
              'small_physical_targets': [physical_path(m) for m in (2, 3)],
              'sparse_local_walk_leaf_Gram_checks': [sparse_leaf_check(n) for n in (1, 2, 3)],
              'reused_exact_whole_side_noncommutative_checks': logarithm.exact_formal_checks(),
              'exact_fixed_clock_calibration': rational_calibration(),
              'constant_step_Cauchy_calculation_checks': cauchy_checks(),
              'largest_constructed_physical_generator_dimension': 25,
              'largest_constructed_controlled_Gram_dimension': 8,
              'no_large_physical_enumeration_or_numerical_rank_tests': True,
              'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in (Path(__file__), Path(logarithm.__file__), Path(reused.__file__))}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
