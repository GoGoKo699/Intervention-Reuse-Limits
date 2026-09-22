#!/usr/bin/env python3
"""Exact tree/filter identities and fixed-dwell controlled-response checks.

The state obstruction is analytic: an exact leaf identity bounds a Gram
matrix from below, while explicit polynomial perturbation bounds control
the replacement by legal fixed-duration propagators. Numerical matrix
calculations check consistency at two precisions; they are not rank tests,
interval certificates, or searches over competing predictors.
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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def number(value: sp.Expr) -> mp.mpf:
    return mp.mpf(str(sp.N(value, mp.mp.dps+10)))


def numeric_matrix(value: sp.Matrix) -> mp.matrix:
    return mp.matrix([[number(value[i, j]) for j in range(value.cols)] for i in range(value.rows)])


def frobenius(value: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(x)**2 for x in value))


def digits(value: mp.mpf, count: int = 50) -> str:
    return mp.nstr(value, count)


def tree_basis(n: int) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, list[tuple[int, ...]]]:
    half, N = 2**n, 2**(n+1)
    vertices = [word for depth in range(n+1) for word in itertools.product((-1, 1), repeat=depth)]
    index = {word: j for j, word in enumerate(vertices)}
    A = sp.zeros(len(vertices))
    for word in vertices[1:]:
        i, j = index[word], index[word[:-1]]
        A[i, j] = A[j, i] = 1
    B = sp.diag(*[0 if not word else word[-1] for word in vertices])

    # Euclidean-normalized Haar functions within each physical half.
    waves = []
    size = half
    while size >= 2:
        for start in range(0, half, size):
            wave = sp.zeros(half, 1)
            for j in range(size):
                wave[start+j] = (1 if j < size//2 else -1)/sp.sqrt(size)
            waves.append(wave)
        size //= 2
    columns = [sp.ones(N, 1)/sp.sqrt(N), sp.Matrix([1]*half+[-1]*half)/sp.sqrt(N)]
    counts = {-1: 0, 1: 0}
    for word in vertices[1:]:
        sign = word[-1]
        column = sp.zeros(N, 1)
        start = 0 if sign == 1 else half
        column[start:start+half, 0] = waves[counts[sign]]
        counts[sign] += 1
        columns.append(column)
    U = sp.Matrix.hstack(*columns)
    require((U.T*U).applyfunc(sp.simplify) == sp.eye(N), 'Physical Haar basis is exactly orthonormal')
    g = sp.Matrix([1]*half+[-1]*half)
    expected = sp.zeros(N)
    expected[0, 1] = expected[1, 0] = 1
    expected[1:, 1:] = B
    require((U.T*sp.diag(*g)*U).applyfunc(sp.simplify) == expected,
            'Binary actuator becomes root swap and sign-labeled diagonal')
    return U, A, B, vertices


def full_basis_generator(A: sp.Matrix, B: sp.Matrix, epsilon: sp.Rational, z: sp.Rational) -> sp.Matrix:
    hidden = A.rows+1
    K = sp.zeros(hidden)
    K[1:, 1:] = -2*sp.eye(A.rows)+epsilon*A
    J = sp.zeros(hidden)
    J[0, 1] = J[1, 0] = 1
    J[1:, 1:] = B
    c, u = (z+1/z)/2, (z-1/z)/2
    Q = sp.zeros(hidden+1)
    Q[0, 0] = -z*c
    Q[0, 1], Q[0, 2] = z*c, z*u
    Q[1, 0], Q[2, 0] = c/z, u/z
    Q[1:, 1:] = K-(c*sp.eye(hidden)+u*J)/z
    return Q


def matrix_letters(Q0, Qh, epsilon, z, identity):
    F = Q0*(Q0+2*identity)/3
    c, u = (z+1/z)/2, (z-1/z)/2
    A = F*(Q0+3*identity)*F/epsilon
    B = F*(Qh-Q0-(1-c/z)*identity)*F/(-u/z)
    return F, A, {-1: (identity-B)/2, 1: (identity+B)/2}


def exact_case(n: int) -> tuple[dict, dict]:
    epsilon = sp.Rational(1, 2**(20*(n+1)))
    z = sp.Rational(65, 64)  # h=log(z)<1/64<1/40.
    U, A, B, vertices = tree_basis(n)
    N, R = U.rows, 2**n
    Ahidden = sp.zeros(N)
    Ahidden[1:, 1:] = A
    physical_A = (U*Ahidden*U.T).applyfunc(sp.simplify)
    physical_K = -2*(sp.eye(N)-sp.ones(N)/N)+epsilon*physical_A
    require(physical_K == physical_K.T and physical_K*sp.ones(N, 1) == sp.zeros(N, 1),
            'Physical internal generator symmetric and conservative')
    require(max(sum(abs(A[i, j]) for j in range(A.cols)) for i in range(A.rows)) <= 3,
            'Tree operator norm certified by maximum absolute row sum')
    positivity_floor = sp.Rational(2, N)-3*epsilon
    require(positivity_floor >= sp.Rational(1, N) > 0,
            'Strict physical off-diagonal positivity certificate')
    require(2-3*epsilon >= 1 and 2+3*epsilon <= 3, 'Fixed hidden relaxation-rate band')

    root = sp.zeros(A.rows, 1)
    root[0] = 1
    leaves = [i for i, word in enumerate(vertices) if len(word) == n]
    words = list(itertools.product((-1, 1), repeat=n))
    ideal_columns = []
    for word in words:
        column = root
        for sign in word:
            column = (sp.eye(A.rows)+sign*B)*A*column/2
        ideal_columns.append(column)
    V = sp.Matrix.hstack(*ideal_columns)
    require(V.extract(leaves, range(R)) == sp.eye(R), 'Exact ideal-word leaf matrix identity')
    nonleaves = [i for i in range(A.rows) if i not in leaves]
    remainder = V.extract(nonleaves, range(R))
    require(V.T*V-sp.eye(R) == remainder.T*remainder, 'Exact Gram lower bound by sum of squares')

    # Radial invariance proves the full root spectral measure without
    # relying on a numerical eigendecomposition of near-colliding rates.
    radial = sp.zeros(A.rows, n+1)
    for depth in range(n+1):
        for i, word in enumerate(vertices):
            if len(word) == depth:
                radial[i, depth] = 1/sp.sqrt(2**depth)
    J = sp.zeros(n+1)
    for i in range(n):
        J[i, i+1] = J[i+1, i] = sp.sqrt(2)
    require((radial.T*radial).applyfunc(sp.simplify) == sp.eye(n+1), 'Normalized radial basis')
    require((A*radial-radial*J).applyfunc(sp.simplify) == sp.zeros(A.rows, n+1), 'Exact radial tridiagonal restriction')
    weights = [2*sp.sin(j*sp.pi/(n+2))**2/(n+2) for j in range(1, n+2)]
    eigenvalues = [2*sp.sqrt(2)*sp.cos(j*sp.pi/(n+2)) for j in range(1, n+2)]
    for power in range(2*n+2):
        spectral = sum(weight*value**power for weight, value in zip(weights, eigenvalues))
        require(sp.simplify(spectral-(J**power)[0, 0]) == 0, 'Exact radial spectral weights and moments')

    Q0 = full_basis_generator(A, B, epsilon, sp.Integer(1))
    Qh = full_basis_generator(A, B, epsilon, z)
    size = N+1
    I = sp.eye(size)
    p0 = sp.zeros(1, size)
    p0[0], p0[1] = sp.Rational(1, 2), sp.Rational(1, 2)
    S = sp.zeros(size, 1)
    S[0], S[1] = -1, 1
    embedded_root = sp.zeros(size, 1)
    embedded_root[2] = 1
    require(Q0 == Q0.T and p0*Q0 == sp.zeros(1, size), 'Zero-field reversible basis and stationary preparation')
    physical_Qh = sp.zeros(size)
    physical_Qh[1:, 1:] = physical_K
    for j in range(N):
        sign = 1 if j < N//2 else -1
        physical_Qh[0, j+1] = z**(1+sign)/N
        physical_Qh[j+1, 0] = z**(sign-1)
        physical_Qh[j+1, j+1] -= physical_Qh[j+1, 0]
    physical_Qh[0, 0] = -sum(physical_Qh[0, j] for j in range(1, size))
    transform = sp.diag(sp.Integer(1), sp.sqrt(N)*U)
    require((physical_Qh*transform-transform*Qh).applyfunc(sp.simplify) == sp.zeros(size),
            'Full field matrix is exactly the original physical rate rule')

    F, filtered_A, projectors = matrix_letters(Q0, Qh, epsilon, z, I)
    Fhidden = sp.eye(A.rows)-sp.Rational(4, 3)*epsilon*A+epsilon**2*A**2/3
    expected_F = sp.zeros(size)
    expected_F[2:, 2:] = Fhidden
    require(F == expected_F, 'Exact quadratic filter kills both block-constant modes')
    require(filtered_A[2:, 2:] == Fhidden*A*Fhidden, 'Exact adjacency filter')
    require((projectors[1]-projectors[-1])[2:, 2:] == Fhidden*B*Fhidden, 'Exact actuator sign filter')
    require(filtered_A == filtered_A.T and all(P == P.T for P in projectors.values()),
            'Exact filtered letters selfadjoint')
    u = (z-1/z)/2
    ell, endpoint_r = 2*u*u, -2*u/z
    normalization = ell*endpoint_r
    require(p0*Qh*F == ell*(F*embedded_root).T/2, 'Exact left mean-response endpoint')
    require(F*Qh*S == endpoint_r*F*embedded_root, 'Exact right mean-response endpoint')
    actual_columns = []
    for word in words:
        column = F*embedded_root
        left = p0*Qh*F
        for sign in word:
            column = projectors[sign]*filtered_A*column
            left = left*filtered_A*projectors[sign]
        require(left == ell*column.T/2, 'Formal reversed word equals Gram left factor')
        actual_columns.append(column)
    actual_V = sp.Matrix.hstack(*actual_columns)
    gram = actual_V.T*actual_V/2
    # The error certificate is analytic, not computed from a singular value.
    column_bound = 105*(n+1)*6**n*epsilon
    matrix_bound_squared = R*column_bound**2
    require(matrix_bound_squared < sp.Rational(1, 16), 'Analytic column perturbation bound below one quarter')
    require(all(sum(value**2 for value in (actual_V[2:, j]-V[:, j])) <= column_bound**2 for j in range(R)),
            'Exact selected columns satisfy analytic tree-filter perturbation bound')

    report = {
        'depth_n': n, 'hidden_states': N, 'full_Markov_states': size,
        'controlled_matrix_dimension': R, 'epsilon_exact': str(epsilon),
        'G': '1', 'W': '1', 'field_h': 'log(65/64)', 'exp_h_exact': str(z),
        'physical_Haar_orthonormality': True, 'physical_generator_positivity_floor': str(positivity_floor),
        'hidden_relaxation_rate_band': [1, 3], 'ideal_leaf_matrix_exact_identity': True,
        'ideal_Gram_minus_identity_exact_sum_of_squares': True,
        'radial_modes': n+1, 'radial_weights_exact': [str(sp.simplify(w)) for w in weights],
        'radial_moments_checked': 2*n+2, 'exact_minimal_cubic_response_states': n+3,
        'physical_rate_rule_and_generator_filter_identities': True,
        'left_and_right_mean_Gram_endpoints': True,
        'endpoint_normalization_exact': str(normalization),
        'tree_filter_column_error_certificate': str(column_bound),
        'certified_exact_filtered_Gram_eigenvalue_floor': '9/32',
    }
    data = {'n': n, 'epsilon': epsilon, 'z': z, 'Q0': Q0, 'Qh': Qh, 'p0': p0, 'S': S,
            'F': F, 'gram': gram, 'words': words, 'normalization': normalization}
    return data, report


def replacement_certificate(data: dict, degree: int) -> dict:
    """Explicit rational norm arithmetic for this fixed target family."""
    n, eps, z = data['n'], data['epsilon'], data['z']
    delta = sp.Rational(32, 2**degree)
    u, c = (z-1/z)/2, (z+1/z)/2
    f = 1+5*eps
    eF = delta*(10+delta)/3
    a = 3*f*f
    eA = (eF*(7+delta)*(f+eF)+f*delta*(f+eF)+7*f*eF)/eps
    b = u/z
    M = 9+abs(1-c/z)
    eB = (eF*(M+2*delta)*(f+eF)+2*f*delta*(f+eF)+f*M*eF)/b
    p = (1+f*f)/2
    eP = eB/2
    composite, error_composite = p*a, eP*(a+eA)+p*eA
    approximate = composite+error_composite
    word_error = n*error_composite*approximate**(n-1)
    left, right = u*u*f, 2*u*f/z
    # ||pi0||<=1 and ||S||<=2 in the chosen orthogonal basis.
    left_error = delta*(f+eF)+5*eF
    right_error = 2*(eF*(5+delta)+f*delta)
    entry_error = (
        left_error*approximate**(2*n)*(right+right_error)
        +left*word_error*approximate**n*(right+right_error)
        +left*composite**n*word_error*(right+right_error)
        +left*composite**(2*n)*right_error)/abs(data['normalization'])
    matrix_error = 2**n*entry_error
    require(matrix_error < sp.Rational(1, 32), 'Exact rational substitution error certificate')

    # Univariate polynomial coefficients only; no protocol-stencil expansion.
    harmonic = sum(sp.Rational(1, j) for j in range(1, degree+1))
    coefficient_norm = 8*harmonic+8*sum(sp.binomial(degree, j)/j for j in range(1, degree+1))
    Rm = 16*2**degree
    require(coefficient_norm <= Rm, 'Exact logarithm-polynomial coefficient l1 bound')
    B_coefficient = (2+abs(1-c/z))/b
    P_coefficient = (1+B_coefficient)/2
    # F has generator-polynomial coefficient l1 norm <=1; A <=4/eps.
    base_coefficient = (4*P_coefficient/eps)**(2*n)/abs(data['normalization'])
    total_degree = 20*n+6
    J = base_coefficient*Rm**total_degree
    response_floor = 1/(4*2**n*J)
    with mp.workdps(150):
        output = {
            'logarithm_polynomial_degree': degree, 'fixed_dwell_time': '1/8',
            'target_generator_error_bound': digits(number(delta)),
            'controlled_matrix_error_bound': digits(number(matrix_error)),
            'rational_bound_below_one_over_32': True,
            'certified_propagator_matrix_singular_value_floor': '1/4',
            'log2_exact_logarithm_polynomial_coefficient_l1': digits(mp.log(number(coefficient_norm), 2)),
            'log2_logarithm_polynomial_coefficient_bound': degree+4,
            'generator_word_degree_bound': total_degree,
            'maximum_experiment_horizon': str(sp.Rational(total_degree*degree, 8)),
            'log2_entry_coefficient_budget_bound': digits(mp.log(number(J), 2)),
            'log10_finite_example_response_lower_bound': digits(mp.log10(number(response_floor))),
            'coefficient_budget_formula': '(4 P_coeff / epsilon)^(2n) * (16 * 2^m)^(20n+6) / abs(ell*r)',
            'scope': 'Exact scalar norm and coefficient bookkeeping for the checked depths and fixed offset 200; not an optimized or numerically estimated state lower bound.',
        }
    return {'report': output, 'matrix_error_exact': matrix_error, 'delta_exact': delta}


def logarithm_from_propagator(Q: mp.matrix, z: mp.mpf, degree: int, field_on: bool) -> tuple[mp.matrix, mp.mpf]:
    size = Q.rows
    diagonal = [1/mp.sqrt(z)]+[mp.sqrt(z)]*(size-1) if field_on else [mp.mpf(1)]*size
    D = mp.diag(diagonal)
    inverse = mp.diag([1/x for x in diagonal])
    symmetric = D*Q*inverse
    require(frobenius(symmetric-symmetric.T) < mp.mpf(10)**(-mp.mp.dps+8), 'Reversible target similarity')
    eigenvalues, basis = mp.eigsy((symmetric+symmetric.T)/2)
    propagator_values, logarithm_values = [], []
    for eigenvalue in eigenvalues:
        propagator_values.append(mp.exp(eigenvalue/8))
        q = -mp.expm1(eigenvalue/8)
        power, total = q, mp.mpf(0)
        for j in range(1, degree+1):
            total += power/j
            power *= q
        logarithm_values.append(-8*total)
    propagator = inverse*basis*mp.diag(propagator_values)*basis.T*D
    approximation = inverse*basis*mp.diag(logarithm_values)*basis.T*D
    # This independently checks that the spectral polynomial was evaluated
    # on actual fixed-dwell propagators, not a different transition family.
    propagator_error = frobenius(propagator-mp.expm(Q/8))
    require(propagator_error < mp.mpf(10)**(-mp.mp.dps+8), 'Fixed-dwell propagator consistency')
    return approximation, propagator_error


def numerical_case(data: dict, degree: int, certificate: dict, precision: int) -> tuple[dict, mp.matrix]:
    with mp.workdps(precision):
        Q0, Qh = numeric_matrix(data['Q0']), numeric_matrix(data['Qh'])
        z, eps = number(data['z']), number(data['epsilon'])
        p0, S = numeric_matrix(data['p0']), numeric_matrix(data['S'])
        approx0, prop_error0 = logarithm_from_propagator(Q0, z, degree, False)
        approxh, prop_errorh = logarithm_from_propagator(Qh, z, degree, True)
        generator_error = max(frobenius(approx0-Q0), frobenius(approxh-Qh))
        rounding_allowance = mp.mpf(10)**(-precision+15)
        require(generator_error <= Q0.rows*number(certificate['delta_exact'])+rounding_allowance,
                'Computed polynomial error consistent with analytic tail and precision floor')
        F, A, projectors = matrix_letters(approx0, approxh, eps, z, mp.eye(Q0.rows))
        left_rows, right_columns = [], []
        for word in data['words']:
            left, right = p0*approxh*F, F*approxh*S
            for sign in word:
                left = left*A*projectors[sign]
                right = projectors[sign]*A*right
            left_rows.append(left)
            right_columns.append(right)
        H = mp.matrix([[(left*right)[0]/number(data['normalization']) for right in right_columns]
                       for left in left_rows])
        gram_error = frobenius(H-numeric_matrix(data['gram']))
        if precision == 150:
            require(gram_error < number(certificate['matrix_error_exact']),
                    'High-precision propagator statistic respects conservative analytic error bound')
        require(gram_error < mp.mpf(1)/32, 'Computed finite experiment statistic near the exact Gram matrix')
        return {
            'working_decimal_digits': precision,
            'generator_polynomial_Frobenius_error': digits(generator_error),
            'propagator_exponential_consistency_error': digits(max(prop_error0, prop_errorh)),
            'controlled_matrix_Frobenius_error_vs_exact_Gram': digits(gram_error),
            'precision_floor_allowance': digits(rounding_allowance),
            'scope': 'High-precision consistency, not interval certification; the rank obstruction uses the separate exact inequalities.',
        }, H


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/general_controlled_lower_bound.json'))
    args = parser.parse_args()
    records = []
    for n in (1, 2, 3):
        data, exact = exact_case(n)
        degree = 40*(n+1)+200
        certificate = replacement_certificate(data, degree)
        low, low_matrix = numerical_case(data, degree, certificate, 100)
        high, high_matrix = numerical_case(data, degree, certificate, 150)
        with mp.workdps(150):
            change = frobenius(low_matrix-high_matrix)
            require(change < mp.mpf('1e-55'), '100-to-150 digit controlled-matrix consistency')
        records.append({'exact_tree_and_filters': exact, 'fixed_dwell_certificate': certificate['report'],
                        'numerical_checks': [low, high],
                        'controlled_matrix_change_100_to_150_digits': digits(change)})
    report = {
        'status': 'PASS',
        'scope': 'Exact small reversible tree targets, ideal leaf/Gram identities, rational polynomial-error certificates, and high-precision fixed-dwell experiment consistency.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
        'depth_cases': records,
        'largest_physical_generator_dimension': 17, 'largest_controlled_matrix_dimension': 8,
        'no_numerical_rank_tests': True,
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
