#!/usr/bin/env python3
"""Exact finite checks for the fixed-label sparse-expander switching lower bound.

Small physical models check the original field rule and endpoint identities.
Sparse Walsh coordinates check long-geodesic leaves without enumerating scenery.
Only K4's sixteen labelings are enumerated. No large graph or simulation is used.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp

import verify_polynomial_controlled_lower_bound as logarithm
import verify_shift_register_lower_bound as reused


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def local_complete(order):
    degree = order-1
    P = (sp.ones(order)-sp.eye(order))/degree
    J = sp.Matrix([[0, 1], [1, 0]])
    L = (sp.kronecker_product(P, sp.eye(2))-sp.eye(2*order))/4
    L += (sp.kronecker_product(sp.eye(order), J)-sp.eye(2*order))/4
    return L


def physical_check(order):
    N = 2*order
    labels = [sigma*((-1)**v) for v in range(order) for sigma in (-1, 1)]
    r = sp.Matrix([0]+labels)
    L = local_complete(order)
    Pi = sp.ones(N)/N
    K = L+sp.Rational(3, 2)*(Pi-sp.eye(N))
    local_rates = sorted((-L).eigenvals())
    positive = [value for value in local_rates if value]
    require(min(positive) == min(sp.Rational(order, 4*(order-1)), sp.Rational(1, 2)),
            'Exact connected local gap on the product of a complete graph and a sign edge')
    require(max(positive) <= 1, 'Local spectral cap is at most one')
    require(sum(labels) == 0 and sum(x*x for x in labels) == N,
            'Every fixed labeling has exactly balanced unit sensitivities')
    require(all(K[i, j] > 0 for i in range(N) for j in range(N) if i != j),
            'Refresh makes every off-diagonal rate positive')
    require(sorted((-K).eigenvals()) == sorted([sp.Integer(0)]+[x+sp.Rational(3, 2) for x in positive]),
            'Refresh shifts precisely the nonconstant local spectrum')
    z = sp.Rational(65, 64)
    u, cosine = (z-1/z)/2, (z+1/z)/2
    generators = []
    pi0 = sp.Matrix([[sp.Rational(1, 2)]+[sp.Rational(1, 2*N)]*N])
    weight = sp.diag(*pi0)
    output = sp.Matrix([-1]+[1]*N)
    for field in (sp.Integer(1), z):
        generator = sp.zeros(N+1)
        generator[1:, 1:] = K
        for j, label in enumerate(labels):
            generator[0, j+1] = field**(1+label)/N
            generator[j+1, 0] = field**(label-1)
            generator[j+1, j+1] -= generator[j+1, 0]
        generator[0, 0] = -sum(generator[0, j] for j in range(1, N+1))
        pi = sp.Matrix([[1]+[field**2/N]*N])/(1+field**2)
        require(generator*sp.ones(N+1, 1) == sp.zeros(N+1, 1), 'Physical generator row sums')
        require(pi*generator == sp.zeros(1, N+1), 'Exact finite-field equilibrium')
        require(sp.diag(*pi)*generator == generator.T*sp.diag(*pi), 'Ordinary detailed balance')
        generators.append(generator)
    Q0, Qh = generators
    I = sp.eye(N+1)
    F = Q0*(Q0+2*I)/3
    F0 = L*L/3-L+sp.Rational(5, 12)*sp.eye(N)
    require(max(sum(abs(L[i, j]) for j in range(N)) for i in range(N)) == 1,
            'The local counting-l1 and linfinity operator norms equal one')
    require(max(sum(abs(F0[i, j]) for j in range(N)) for i in range(N)) <= sp.Rational(7, 4),
            'Exact all-local filter norm bound')
    require(max(sum(abs(F[i, j]) for j in range(N+1)) for i in range(N+1)) <= sp.Rational(13, 6),
            'Exact physical filter norm bound including global centering')
    require(sp.Rational(7, 2)+2*(z*z-1) < 5,
            'Dimension-independent fixed-field spectral enclosure needed for logarithms')
    require(F[1:, 1:] == F0-sp.Rational(5, 12)*Pi, 'Complete global-centering term in the physical filter')
    require(F[0, :] == sp.zeros(1, N+1) and F[:, 0] == sp.zeros(N+1, 1), 'No A-state filter block')
    H = sp.zeros(N+1)
    H[1:, 1:] = sp.eye(N)-Pi
    require(F*H == H*F == F, 'Filter kills both coarse directions')
    Z = [F*F, -F*(Qh-Q0-(1-cosine/z)*I)*F/(u/z)]
    require(Z[1] == F*sp.diag(*r)*F, 'Controlled binary letter is an exact physical generator polynomial')
    ell, right = 2*u*u, -2*u/z
    require(pi0*Qh*F == ell*(F*r).T*weight, 'Actual-mean left endpoint')
    require(F*Qh*output == right*F*r, 'Actual-mean right endpoint')
    vectors = [letter*F*r for letter in Z]
    for b, c in itertools.product(range(2), repeat=2):
        require((pi0*Qh*F*Z[b]*Z[c]*F*Qh*output)[0]/(ell*right)
                == (vectors[b].T*weight*vectors[c])[0], 'Mean polynomial equals physical Gram entry')
    return {'base_graph': 'K%d' % order, 'base_degree': order-1, 'full_Markov_states': N+1,
            'local_relaxation_rates_exact': [str(x) for x in local_rates],
            'exact_stationarity_detailed_balance_histogram_filter_and_endpoints': True,
            'actual_mean_Gram_entries_checked': 4,
            'scope': 'Small physical identities only; these complete graphs do not satisfy the long-girth lower-bound hypotheses.'}


def clean(vector):
    return {key: value for key, value in vector.items() if value}


def add(*terms):
    out = {}
    for factor, vector in terms:
        for key, value in vector.items():
            out[key] = out.get(key, Q(0))+factor*value
    return clean(out)


def sparse_L(vector, order):
    out = {}
    for (mask, parity, site), value in vector.items():
        for target, factor in (((site-1) % order, Q(1, 8)),
                               ((site+1) % order, Q(1, 8)),
                               (site, -Q(1, 4)-Q(parity, 2))):
            key = (mask, parity, target)
            out[key] = out.get(key, Q(0))+factor*value
    return clean(out)


def sparse_F(vector, order, center):
    first = sparse_L(vector, order)
    result = add((Q(1, 3), sparse_L(first, order)), (-1, first), (Q(5, 12), vector))
    if center:
        averages = {}
        for (mask, parity, _), value in vector.items():
            if parity == 0:
                averages[mask] = averages.get(mask, Q(0))+value/order
        for mask, value in averages.items():
            for site in range(order):
                key = (mask, 0, site)
                result[key] = result.get(key, Q(0))-Q(5, 12)*value
    return clean(result)


def sparse_M(vector):
    return {(mask ^ (1 << site), parity ^ 1, site): value
            for (mask, parity, site), value in vector.items()}


def dot(first, second):
    return sum((value*second.get(key, Q(0)) for key, value in first.items()), Q(0))


def sparse_checks(depth):
    T, order = 2*depth+1, 8*depth+5
    words = list(itertools.product((0, 1), repeat=depth))
    root = {(1 << site, 1, site): Q(1) for site in range(order)}
    local_columns, actual_columns, remainders = [], [], []
    coefficient = Q(1, 192)**T  # d=2, with graph rates 1/(4d).
    B = (depth+1)*T*3**T
    maximum_leakage = Q(0)
    maximum_derivative_l1 = Q(0)
    for word in words:
        columns = []
        for centered in (False, True):
            vector = sparse_F(root, order, centered)
            for bit in word:
                vector = sparse_F(vector, order, centered)
                if bit:
                    vector = sparse_M(vector)
                vector = sparse_F(vector, order, centered)
            columns.append(vector)
        local, actual = columns
        selected = {}
        for terminal in range(order):
            anchor = (terminal-2*T) % order
            mask = (1 << anchor)+sum((1 << ((anchor+4*j) % order))
                                     for j, bit in enumerate(word, 1) if bit)
            leaf = (mask, (1+sum(word)) % 2, terminal)
            projection = {key: value for key, value in local.items()
                          if key[2] == terminal and key[0] & (1 << anchor)}
            require(projection == {leaf: coefficient}, 'Unique maximal-distance all-local Walsh leaf')
            selected[leaf] = coefficient
            difference = add((1, actual), (-1, local))
            derivative_l1 = sum((abs(value) for (mask0, _, site), value in difference.items()
                                 if site == terminal and mask0 & (1 << anchor)), Q(0))
            require(derivative_l1 <= Q(B, order), 'Fourier l1 bound certifies the divided-difference leakage bound')
            maximum_derivative_l1 = max(maximum_derivative_l1, derivative_l1)
            for other in words:
                other_mask = (1 << anchor)+sum((1 << ((anchor+4*j) % order))
                                               for j, bit in enumerate(other, 1) if bit)
                other_key = (other_mask, (1+sum(other)) % 2, terminal)
                leakage = abs(actual.get(other_key, Q(0))-local.get(other_key, Q(0)))
                maximum_leakage = max(maximum_leakage, leakage)
        local_columns.append(local)
        actual_columns.append(actual)
        remainders.append({key: value for key, value in local.items() if key not in selected})
    for i, j in itertools.product(range(len(words)), repeat=2):
        require((dot(local_columns[i], local_columns[j])-dot(remainders[i], remainders[j]))/(2*order)
                == (coefficient**2/2 if i == j else 0), 'Exact annealed Gram sum-of-squares after all-terminal leaf projection')
    require(maximum_leakage > 0, 'The test observes nonzero global-centering leakage; it is not silently omitted')
    return {'word_depth_n': depth, 'base_cycle_vertices': order, 'base_girth': order,
            'physical_states_per_fixed_labeling': 2*order+1,
            'physical_labelings_enumerated': False,
            'controlled_Gram_dimension': len(words),
            'largest_sparse_column_support': max(map(len, local_columns+actual_columns)),
            'local_leaf_coefficient_exact': str(coefficient),
            'all_terminal_all_local_Gram_SOS_floor': str(coefficient**2/2),
            'maximum_selected_Walsh_coefficient_leakage_exact': str(maximum_leakage),
            'maximum_anchor_derivative_Fourier_l1_bound': str(maximum_derivative_l1),
            'advertised_leakage_bound_B_over_N': str(Q(B, order)),
            'scope': 'Exact sparse identities on long cycles. These cycles verify geodesic and centering algebra, not a uniform expander gap.'}


def matvec(matrix, vector):
    return [sum((a*b for a, b in zip(row, vector)), Q(0)) for row in matrix]


def small_ensemble(depth):
    order, hidden = 4, 8
    T = 2*depth+1
    L = local_complete(order)
    F = L*L/3-L+sp.Rational(5, 12)*(sp.eye(hidden)-sp.ones(hidden)/hidden)
    matrix = [[Q(F[i, j]) for j in range(hidden)] for i in range(hidden)]
    words = list(itertools.product((0, 1), repeat=depth))
    bits = list(itertools.product((-1, 1), repeat=order))
    records, grams = {}, {}
    for labeling in bits:
        root = [Q(sigma*labeling[v]) for v in range(order) for sigma in (-1, 1)]
        vectors = []
        for word in words:
            vector = matvec(matrix, root)
            for bit in word:
                vector = matvec(matrix, vector)
                if bit:
                    vector = [x*y for x, y in zip(vector, root)]
                vector = matvec(matrix, vector)
            vectors.append(vector)
        records[labeling] = vectors
        grams[labeling] = [[sum((x*y for x, y in zip(v, w)), Q(0))/(2*hidden)
                            for w in vectors] for v in vectors]
    expected = [[sum((grams[x][i][j] for x in bits), Q(0))/len(bits)
                 for j in range(len(words))] for i in range(len(words))]
    fourier = {}
    for mask in range(1 << order):
        sign = {x: sp.prod(x[v] for v in range(order) if mask & (1 << v)) for x in bits}
        fourier[mask] = [[sum((records[x][b][site]*int(sign[x]) for x in bits), Q(0))/len(bits)
                          for site in range(hidden)] for b in range(len(words))]
    for i, j in itertools.product(range(len(words)), repeat=2):
        parsed = sum((sum((x*y for x, y in zip(vectors[i], vectors[j])), Q(0))
                      for vectors in fourier.values()), Q(0))/(2*hidden)
        require(expected[i][j] == parsed, 'Exact Walsh Parseval/SOS identity for the expected physical Gram')
    maximum_vector_difference = Q(0)
    maximum_gram_difference = Q(0)
    for labeling in bits:
        for vertex in range(order):
            flipped = tuple(-x if v == vertex else x for v, x in enumerate(labeling))
            for b in range(len(words)):
                maximum_vector_difference = max(maximum_vector_difference,
                    sum((abs(x-y) for x, y in zip(records[labeling][b], records[flipped][b])), Q(0)))
            for b, c in itertools.product(range(len(words)), repeat=2):
                maximum_gram_difference = max(maximum_gram_difference,
                    abs(grams[labeling][b][c]-grams[flipped][b][c]))
    require(maximum_vector_difference <= 4*(depth+1)*3**T, 'Every label flip satisfies the proved counting-l1 influence bound')
    A = 2*(depth+1)*3**(2*T)
    require(maximum_gram_difference <= Q(A, order), 'Every label flip satisfies the physical Gram bounded-differences constant')
    return {'base_graph': 'K4', 'word_depth_n': depth, 'fixed_labelings_checked_exactly': len(bits),
            'label_flip_pairs_checked': len(bits)*order, 'controlled_Gram_dimension': len(words),
            'expected_Gram_exact': [[str(x) for x in row] for row in expected],
            'expected_Gram_is_exact_Walsh_sum_of_squares': True,
            'maximum_counting_l1_vector_influence': str(maximum_vector_difference),
            'maximum_physical_Gram_entry_influence': str(maximum_gram_difference),
            'advertised_entry_influence_A_over_N': str(Q(A, order)),
            'scope': 'Exhaustive finite algebra and influence checks only. K4 does not meet the theorem girth hypothesis; no theorem leaf floor is asserted here.'}


def exact_budgets():
    # A conservative calibration for degrees 3 and 4; d=4 is the harder leaf.
    degree, a_leaf, exponent = 4, Q(1, 768), 192
    require(a_leaf > Q(1, 2**10), 'Conservative rational leaf coefficient bound')
    order_ratio = Q(72, 1)*a_leaf**-2/Q(2**exponent)
    concentration_ratio = Q(209952, 1)*a_leaf**-8/Q(2**exponent)
    require(order_ratio < 1 and concentration_ratio < 1, 'Both order requirements contract relative to the proposed exponential size at every depth')
    z = Q(65, 64)
    u, cosine = (z-1/z)/2, (z+1/z)/2
    ell, right, b = 2*u*u, -2*u/z, u/z
    require(max(1, 1/ell, abs(1/right), (2+abs(1-cosine/z))/b) < 2**12,
            'Exact generator-side coefficient base is below 2^12')
    x = Q(5, 8)
    require(1+x+x*x/(2*(1-x/3)) < 2, 'Taylor majorant implies 1-exp(-5/8)<1/2')
    require(z*8*2 < 32, 'Logarithm side-norm base is bounded at radius 3/2')
    tail_ratio = Q(2**75)*a_leaf**-4*Q(2, 3)**300
    require(tail_ratio < 1, 'The fixed-clock truncation error/floor ratio contracts at every depth')
    records = []
    for n in (1, 2, 3, 10):
        T, q = 2*n+1, 2**n
        c = a_leaf**T
        B, A = (n+1)*T*3**T, 2*(n+1)*3**(2*T)
        order = 2**(exponent*(n+1))
        require(order >= 2*q*B/c, 'Chosen order dominates the leakage requirement')
        # log(8 q^2)=(2n+3)log 2 < 2n+3, for eta=1/4.
        require(order >= 128*q*q*A*A*c**-4*(2*n+3), 'Chosen order gives McDiarmid failure probability at most 1/4')
        cutoff = 300*(n+1)
        error = Q(3*q)*2**(74*(n+1))*Q(2, 3)**(cutoff+1)
        require(error <= c*c/32, 'Whole-side truncation costs at most half the fixed-label Gram floor')
        J = 2**(2*cutoff+27*(n+1))
        response = c*c/(32*q*J*J)
        require(response >= Q(1, 2**(1295*n+1279)), 'Exact response lower bound dominates the advertised exponential law')
        records.append({'word_depth_n': n, 'sufficient_order_as_power_of_two': exponent*(n+1),
                        'leakage_and_failure_budgets_exact': True,
                        'whole_side_degree_cutoff': cutoff,
                        'fixed_label_Gram_floor_exact': str(c*c/16),
                        'matrix_error_below_half_Gram_floor': True,
                        'conservative_actual_mean_error_floor': '2^(-%d)' % (1295*n+1279)})
    return {'parameters': {'base_degree': degree, 'G': 1, 'W': 1, 'exp_h': '65/64', 'dwell_a': '1/8'},
            'all_depth_sufficient_base_order': 'N >= 2^[192(n+1)], n>=1',
            'order_budget_ratio_upper_multiplier': str(order_ratio),
            'concentration_budget_ratio_upper_multiplier': str(concentration_ratio),
            'fixed_clock_error_ratio_upper_multiplier': str(tail_ratio),
            'all_depth_cutoff': 'M=300(n+1)',
            'all_depth_actual_mean_error_floor': '2^(-1295n-1279)',
            'all_depth_horizon': '75(n+1), with each positive segment a multiple of 1/8',
            'failure_probability_bound': '1/4',
            'induction_certificate': 'The exact n=1 checks pass. For n>=1 each displayed requirement divided by its proposed bound contracts by the corresponding rational multiplier; (n+2)/(n+1)<=2, (2n+3)/(2n+1)<=2, and (2n+5)/(2n+3)<=2.',
            'records': records,
            'scope': 'Exact all-depth inequality calibration, conditional on a graph with the required order, degree, gap and girth. No graph of the displayed enormous order is constructed or enumerated.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/expander_scenery_lower_bound.json'))
    args = parser.parse_args()
    report = {'status': 'PASS',
              'scope': 'Exact finite physical identities, sparse all-local Walsh leaves and nonzero global-centering leakage, exhaustive K4 influence/Parseval checks, and all-depth rational probability/clock budgets. No large graph simulation or numerical rank inference.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'small_physical_targets': [physical_check(order) for order in (3, 4, 5)],
              'sparse_geodesic_Walsh_checks': [sparse_checks(n) for n in (1, 2)],
              'small_fixed_label_ensemble_checks': [small_ensemble(n) for n in (1, 2)],
              'reused_exact_whole_side_noncommutative_checks': logarithm.exact_formal_checks(),
              'exact_all_depth_probability_and_clock_budgets': exact_budgets(),
              'largest_constructed_physical_generator_dimension': 11,
              'largest_constructed_controlled_Gram_dimension': 4,
              'no_large_graph_simulation_or_numerical_rank_tests': True,
              'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in (Path(__file__), Path(logarithm.__file__), Path(reused.__file__))}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
