#!/usr/bin/env python3
"""Bounded exact certificates for the finite K2,3 state-advantage construction.

Rational identities and small numerical diagnostics supplement the analytic
controlled-mean transfer theorem; finite examples do not prove that theorem.
"""
import argparse
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm


CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def array(a):
    return np.asarray([[float(x) for x in row] for row in a])


def generator(off):
    out = [row[:] for row in off]
    for i in range(len(out)):
        require(out[i][i] == 0 and all(x >= 0 for x in out[i]),
                'Specified off-diagonal rates are nonnegative')
        out[i][i] = -sum(out[i])
    return out


def weighted_gram(features, mu):
    return mm(transpose(features), [[mu[i]*x for x in row] for i, row in enumerate(features)])


def psd_ldl(a):
    require(a == transpose(a), 'Weighted spectral certificate is symmetric')
    work = [row[:] for row in a]
    pivots = []
    for i in range(len(a)):
        pivot = work[i][i]
        require(pivot >= 0, 'Exact LDL pivot is nonnegative')
        pivots.append(pivot)
        if pivot == 0:
            require(all(work[i][j] == 0 for j in range(i+1, len(a))),
                    'A zero PSD pivot has a zero remaining row')
            continue
        for j in range(i+1, len(a)):
            for k in range(i+1, len(a)):
                work[j][k] -= work[j][i]*work[i][k]/pivot
    return [str(x) for x in pivots]


def rank(a):
    work = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(a[0])):
        candidate = next((i for i in range(pivot_row, len(a)) if work[i][col]), None)
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        factor = work[pivot_row][col]
        work[pivot_row] = [x/factor for x in work[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row:
                factor = work[i][col]
                work[i] = [x-factor*y for x, y in zip(work[i], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def physical_generator(k, mu, beta, bias):
    n = len(mu)
    q = zeros(n+1)
    for i in range(n):
        q[0][i+1] = bias*mu[i]*beta[i]
        q[i+1][0] = beta[i]
        for j in range(n):
            q[i+1][j+1] = k[i][j]
        q[i+1][i+1] -= beta[i]
    q[0][0] = -sum(q[0])
    pi = [1/(1+bias)]+[bias*x/(1+bias) for x in mu]
    return q, pi


def construction_checks():
    edges = [(left, right) for left in range(2) for right in range(2, 5)]
    degrees = [3, 3, 2, 2, 2]
    vertex_law = [F(d, 12) for d in degrees]
    target_mu = [F(1, 12)]*6+[F(d, 24) for d in degrees]
    rival_mu = [F(d, 24) for d in degrees]*2
    target_off, rival_off = zeros(11), zeros(10)
    for e, endpoints in enumerate(edges):
        for vertex in endpoints:
            target_off[e][6+vertex] = F(1, 2)
            target_off[6+vertex][e] = F(1, degrees[vertex])
    for vertex in range(5):
        rival_off[vertex][5+vertex] = 1
        rival_off[5+vertex][vertex] = F(1, 2)
        for neighbor in range(5):
            if (min(vertex, neighbor), max(vertex, neighbor)) in edges:
                rival_off[5+vertex][neighbor] = F(1, 2*degrees[vertex])
    # Independent rate-one refresh inside each of the two hidden blocks.
    for off, split, memory_law in ((target_off, 6, [F(1, 6)]*6),
                                    (rival_off, 5, vertex_law)):
        for block, law in ((list(range(split)), memory_law),
                           (list(range(split, len(off))), vertex_law)):
            for i in block:
                for j, weight in zip(block, law):
                    if i != j:
                        off[i][j] += weight
    target_k, rival_k = generator(target_off), generator(rival_off)
    for k, mu in ((target_k, target_mu), (rival_k, rival_mu)):
        require(sum(mu) == 1 and min(mu) > 0, 'Hidden stationary law is a positive probability')
        require(mm([mu], k) == [[F(0)]*len(mu)], 'Hidden stationary law balances every column')
        require(max(-k[i][i] for i in range(len(k))) <= 2, 'Both hidden exit caps are at most two')
    require(all(target_mu[i]*target_k[i][j] == target_mu[j]*target_k[j][i]
                for i in range(11) for j in range(11)), 'Target hidden generator satisfies ordinary detailed balance')
    flux_defects = [(i, j, rival_mu[i]*rival_k[i][j]-rival_mu[j]*rival_k[j][i])
                    for i in range(10) for j in range(i+1, 10)
                    if rival_mu[i]*rival_k[i][j] != rival_mu[j]*rival_k[j][i]]
    require(bool(flux_defects), 'The exact smaller rival fails ordinary detailed balance')
    c = zeros(11, 10)
    for e, endpoints in enumerate(edges):
        for vertex in endpoints:
            c[e][vertex] = F(1, 2)
    for vertex in range(5):
        c[6+vertex][5+vertex] = 1
    require(all(sum(row) == 1 and min(row) >= 0 for row in c), 'Intertwiner is stochastic')
    require(mm(target_k, c) == mm(c, rival_k), 'Exact hidden generator intertwining holds')
    require(mm([target_mu], c) == [rival_mu], 'Intertwiner preserves the stationary preparation')
    lower = [[target_mu[i]*(-target_k[i][j]-F(i == j)+target_mu[j])
              for j in range(11)] for i in range(11)]
    upper = [[target_mu[i]*(3*F(i == j)+target_k[i][j]-3*target_mu[j])
              for j in range(11)] for i in range(11)]
    lower_pivots, upper_pivots = psd_ldl(lower), psd_ldl(upper)
    require(rank(target_k) == 10, 'The target has a unique stationary mode')
    full_c = zeros(12, 11)
    full_c[0][0] = 1
    for i in range(11):
        full_c[i+1][1:] = c[i][:]
    endpoint = [F(6, 16)]+[F(7+j, 16) for j in range(5)]
    # Arbitrary positive blockwise barriers are allowed, not just the two
    # commanded endpoints. This checks more than one numerical field pair.
    menu = [([F(1)]*6, F(1)), (endpoint, F(4)),
            ([F(2, 3), F(1, 2), F(3, 4), F(4, 5), F(5, 6), F(6, 7)], F(9, 4))]
    field_cases, target_qs, rival_qs = [], [], []
    for label_barriers, bias in menu:
        target_beta = [label_barriers[0]]*6+label_barriers[1:]
        rival_beta = [label_barriers[0]]*5+label_barriers[1:]
        target_q, target_pi = physical_generator(target_k, target_mu, target_beta, bias)
        rival_q, rival_pi = physical_generator(rival_k, rival_mu, rival_beta, bias)
        require(mm(target_q, full_c) == mm(full_c, rival_q),
                'Full physical generators intertwine including entrance, returns and diagonals')
        require(mm([target_pi], full_c) == [rival_pi], 'Every field-dependent stationary preparation is preserved')
        require(mm([target_pi], target_q) == [[F(0)]*12] and
                mm([rival_pi], rival_q) == [[F(0)]*11], 'Both full controlled generators are stationary')
        require(all(target_pi[i]*target_q[i][j] == target_pi[j]*target_q[j][i]
                    for i in range(12) for j in range(12)), 'Full target obeys detailed balance at every fixture field')
        target_qs.append(target_q)
        rival_qs.append(rival_q)
        field_cases.append({'equilibrium_bias_exact': str(bias),
                            'six_label_barriers_exact': [str(x) for x in label_barriers]})
    target_readout, rival_readout = [[-F(1)]]+[[F(1)]]*11, [[-F(1)]]+[[F(1)]]*10
    require(mm(full_c, rival_readout) == target_readout, 'Intertwiner preserves the visible readout')
    target_initial = [F(1, 2)]+[x/2 for x in target_mu]
    rival_initial = [F(1, 2)]+[x/2 for x in rival_mu]
    require(mm([target_initial], full_c) == [rival_initial], 'Zero-field initial laws intertwine')
    residuals = []
    for protocol in (((0, F(1, 3)),), ((1, F(1, 5)), (0, F(2, 3))),
                     ((2, F(1, 4)), (1, F(1, 2)), (0, F(3, 4)))):
        p, q = np.asarray([float(x) for x in target_initial]), np.asarray([float(x) for x in rival_initial])
        for index, duration in protocol:
            p = p @ expm(float(duration)*array(target_qs[index]))
            q = q @ expm(float(duration)*array(rival_qs[index]))
        residual = max(float(np.max(np.abs(p @ array(full_c)-q))),
                       abs(float(p @ array(target_readout)[:, 0]-q @ array(rival_readout)[:, 0])))
        require(residual < 2e-13, 'Small switched-semigroup comparison agrees with exact intertwining')
        residuals.append(float(f'{residual:.12g}'))
    return target_k, target_mu, rival_k, rival_mu, edges, degrees, {
        'target_hidden_states': 11, 'target_total_states': 12,
        'rival_hidden_states': 10, 'rival_total_states': 11,
        'hidden_exit_cap_exact': '2', 'target_nonzero_decay_band_exact': ['1', '3'],
        'target_band_lower_LDL_pivots': lower_pivots, 'target_band_upper_LDL_pivots': upper_pivots,
        'rival_nonzero_ordinary_flux_defects': len(flux_defects),
        'one_ordinary_flux_defect_exact': {'states': list(flux_defects[0][:2]), 'value': str(flux_defects[0][2])},
        'field_cases': field_cases, 'numerical_switched_mean_law_residuals': residuals,
        'scope': 'Exact intertwining is certified on the constructed generators; the analytic proof extends it to every admissible blockwise barrier and protocol.'}


def gram_checks(k, mu, edges, degrees):
    p = [[F(i == j)+k[i][j]/2 for j in range(11)] for i in range(11)]
    require(all(min(row) >= 0 and sum(row) == 1 for row in p), 'Uniformization P=I+K/2 is stochastic')
    features = zeros(11, 10)
    for i in range(6):
        for j in range(5):
            features[i][j] = 2*p[i][6+j]
    for j in range(5):
        features[6+j][5+j] = 1
    require(all(min(row) >= 0 for row in features), 'Ten features are nonnegative')
    gram = weighted_gram(features, mu)
    expected = zeros(10)
    for j, d in enumerate(degrees):
        expected[j][j] = F(d, 48)
        expected[5+j][5+j] = F(d, 24)
    for i, j in edges:
        expected[i][j] = expected[j][i] = F(1, 48)
    require(gram == expected, 'Operator-defined features reproduce the complete ten-feature target Gram')
    require(rank(gram) == 9, 'Ordinary matrix rank is nine and cannot replace the CP atom obstruction')
    witnesses = [frozenset(edge) for edge in edges]+[frozenset([j]) for j in range(5, 10)]
    require(len(witnesses) == 11, 'Six positive cross edges plus five isolated positive diagonals give eleven requirements')
    forbidden = {frozenset([i, j]) for i in range(10) for j in range(i+1, 10) if gram[i][j] == 0}
    for first, second in combinations(witnesses, 2):
        require(any(pair <= first | second for pair in forbidden),
                'Each pair of distinct atom requirements has an identically zero cross entry')
    atom_supports = [frozenset(j for j, x in enumerate(row) if x) for row in features]
    require(sorted(map(sorted, atom_supports)) == sorted(map(sorted, witnesses)),
            'The eleven target atoms meet the support lower bound exactly')
    dimension, epsilon, minimum, diagonal = 10, F(1, 40000), F(1, 48), F(1, 8)
    require(min(gram[next(iter(w))][next(iter(w))] if len(w) == 1 else gram[min(w)][max(w)]
                for w in witnesses) == minimum, 'Smallest positive witness entry is exactly 1/48')
    require(max(gram[i][i] for i in range(10)) == diagonal, 'Largest diagonal is exactly 1/8')
    left = epsilon*dimension**2*(diagonal+epsilon)
    right = (minimum-epsilon)**2
    require(left < right, 'Strict rational robust-CP inequality excludes ten atoms at the stated entry tolerance')
    dominant_atom_threshold = (minimum-epsilon)/dimension
    forbidden_lower = dominant_atom_threshold**2/(diagonal+epsilon)
    require(forbidden_lower > epsilon, 'A shared dominant atom forces a forbidden entry larger than tolerance')
    return {'features': 10, 'ordinary_matrix_rank': 9, 'exact_CP_atom_count': 11,
            'positive_support_requirements': [sorted(w) for w in witnesses],
            'target_Gram_exact': [[str(x) for x in row] for row in gram],
            'robust_entry_tolerance_exact': str(epsilon), 'excluded_maximum_atoms': dimension,
            'strict_inequality_left_exact': str(left), 'strict_inequality_right_exact': str(right),
            'forced_forbidden_entry_lower_exact': str(forbidden_lower),
            'scope': 'The positive entry tolerance is a Gram-matrix certificate. Converting controlled-mean error to this tolerance requires the separately proved finite-clock transfer estimate.'}


def polynomial_product(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def soft_selector_checks():
    grid = [F(6+j, 16) for j in range(6)]
    off_grid = [F(0), F(1, 4), F(1, 2), F(7, 8), F(1)]
    coefficient_masses = []
    for index, location in enumerate(grid):
        lagrange = [F(1)]
        for other in grid:
            if other != location:
                lagrange = polynomial_product(lagrange, [-other/(location-other), 1/(location-other)])
        selector = polynomial_product(lagrange, lagrange)
        evaluate = lambda x: sum((value*x**power for power, value in enumerate(selector)), F(0))
        require(len(selector)-1 == 10, 'Squared six-level Lagrange selector has degree ten')
        require(all(evaluate(x) == F(j == index) for j, x in enumerate(grid)),
                'Squared Lagrange selector is the exact target label projector')
        require(all(evaluate(x) >= 0 for x in off_grid),
                'Off-grid selectors remain nonnegative, including barrier-domain endpoints')
        mass = sum(abs(x) for x in selector)
        require(mass <= 2**70, 'Exact selector coefficient mass fits the declared conservative bound')
        coefficient_masses.append(str(mass))
    return {'grid_exact': [str(x) for x in grid], 'off_grid_checks_exact': [str(x) for x in off_grid],
            'selector_degree': 10, 'selector_coefficient_l1_exact': coefficient_masses,
            'declared_selector_coefficient_l1_bound': '2^70',
            'scope': 'These finite polynomial checks certify the six target values and sample off-grid values; global positivity follows analytically because each selector is a square.'}


def recovery_budget_checks():
    grid = [F(6+j, 16) for j in range(6)]
    require(all(F(1, 8) < x*x < F(1, 2) for x in grid),
            'Rational squared barriers certify all Bell sensitivities strictly between minus and plus one half')
    products = [math.prod(abs(x-y) for y in grid if y != x) for x in grid]
    denominator = min(products)
    require(denominator == F(12, 16**5), 'The minimum five-factor interpolation denominator is exact')
    b_mass, h_mass = 10, 2
    factor_mass = b_mass+h_mass
    lagrange_mass = F(factor_mass**5)/denominator
    require(lagrange_mass == 81*2**28 and lagrange_mass < 2**35,
            'Expanded generator/projector Lagrange mass obeys the analytic bound')
    selector_degree, selector_mass = 10, 2**70
    feature_degree = 2*selector_degree+1
    feature_mass = 2*selector_mass**2*5
    require(feature_degree == 21 and feature_mass < 2**144,
            'Positive feature degree and expanded coefficient mass fit the declared bounds')
    gram_degree, gram_mass = 2*feature_degree, 2*(2**144)**2
    require(gram_degree == 42 and gram_mass == 2**289,
            'The complete Gram polynomial has degree at most42 and coefficient mass at most2^289')
    rho, varrho, chi = F(1, 2), F(3, 2), F(2)
    require(1/(1-varrho*rho) == 4 and chi*8*2 == 32,
            'With a=log(2)/8 the logarithm majorant constant is exactly32')
    coth_h = F(5, 3)
    recursion_constant = 1+2*(1+coth_h)
    require(recursion_constant == F(19, 3) and recursion_constant < 7,
            'The two-field inserted-projection recursion constant is below seven')
    ca, cutoff, accuracy_exponent = 32, 1200, 3000
    majorant = gram_mass*ca**gram_degree
    require(majorant == 2**499, 'Whole-polynomial majorant equals the declared power2^499')
    tail = majorant*2*F(2, 3)**(cutoff+1)
    propagated = majorant*4**cutoff*(1+7*cutoff)*F(1, 2**accuracy_exponent)
    require(F(2, 3)**2 < F(1, 2) and 1+7*cutoff == 8401 < 2**14,
            'Elementary strict inequalities justify the conservative recovery exponents')
    require(tail < F(1, 2**100) and propagated < F(1, 2**87),
            'Exact rational total-degree truncation errors satisfy the two declared powers')
    require(tail+propagated < F(1, 2**100)+F(1, 2**87) < F(1, 40000),
            'Recovered Gram error is strictly below the robust eleven-atom threshold')
    require(F(cutoff, 8) == 150, 'All witness protocols fit the stated150log(2)/k horizon')
    return {'clock_duration': 'log(2)/(8k)', 'maximum_clock_letters': cutoff,
            'maximum_horizon': '150log(2)/k', 'controlled_mean_tolerance': '2^-3000',
            'barrier_squared_lower_bound_exact': '1/8', 'barrier_squared_upper_bound_exact': '1/2',
            'sensitivity_interval': '(-1/2,1/2)', 'minimum_interpolation_denominator_exact': str(denominator),
            'expanded_Lagrange_coefficient_mass_bound_exact': str(lagrange_mass),
            'Gram_generator_degree_bound': gram_degree, 'Gram_coefficient_mass_bound': '2^289',
            'log_majorant_constant_exact': str(ca), 'projection_recursion_constant_exact': str(recursion_constant),
            'whole_polynomial_majorant_bound': '2^499',
            'analytic_tail_upper_bound': '2^-100', 'propagated_mean_error_upper_bound': '2^-87',
            'Gram_entry_threshold_exact': '1/40000',
            'scope': 'Exact rational arithmetic checks the stated constants for total bookkeeping-degree truncation of the entire Gram polynomial. The analytic word-recovery theorem, not this arithmetic, supplies the arbitrary-rival implication.'}


def finite_entropy_checks(k, mu):
    n = len(k)
    reverse = [[mu[j]*k[j][i]/mu[i] for j in range(n)] for i in range(n)]
    epsilon = F(1, 10)
    regularized = [[(1-epsilon)*k[i][j]+epsilon*reverse[i][j]
                    for j in range(n)] for i in range(n)]
    require(mm([mu], reverse) == [[F(0)]*n] and mm([mu], regularized) == [[F(0)]*n],
            'Time reversal and reverse-mixture preserve hidden stationarity')
    require(all(regularized[i][i] == k[i][i] for i in range(n)),
            'Reverse-mixture preserves every hidden exit and the cap')
    require(all((regularized[i][j] > 0) == (regularized[j][i] > 0)
                for i in range(n) for j in range(n) if i != j),
            'Regularization makes the positive transition support bidirectional')
    hidden_epr = 0.
    for i in range(n):
        for j in range(n):
            if i != j and regularized[i][j]:
                flux, back = mu[i]*regularized[i][j], mu[j]*regularized[j][i]
                require(epsilon/(1-epsilon) <= flux/back <= (1-epsilon)/epsilon,
                        'Every regularized stationary flux ratio satisfies the exact mixture bound')
                hidden_epr += float(flux)*math.log(float(flux/back))
    require(0 < hidden_epr <= 2*math.log(float((1-epsilon)/epsilon)),
            'Finite positive hidden EPR obeys the cap-two logarithmic bound')
    q, pi = physical_generator(regularized, mu, [F(1)]*n, F(1))
    full_epr = sum(float(pi[i]*q[i][j])*math.log(float(pi[i]*q[i][j]/(pi[j]*q[j][i])))
                   for i in range(n+1) for j in range(n+1) if i != j and q[i][j])
    require(abs(full_epr-hidden_epr/2) < 2e-14, 'Zero-field full EPR is one half of hidden EPR')
    # Keep the theorem-scale accuracy symbolic: no float underflow or huge
    # target allocation is needed for its exact constant comparison.
    mean_cost_over_delta = 2*F(2)/F(3, 8)/22
    require(mean_cost_over_delta == F(16, 33) and mean_cost_over_delta < F(1, 2),
            'Epsilon=delta0/22 gives a regularized mean error strictly below delta0/2')
    original_rule_R = F(11, 4)
    require(F(3, 8) >= 1/original_rule_R and original_rule_R == 4*F(11, 16),
            'R=11/4 bounds both directions of the original-rule interface')
    theorem_mean_cost = 2*2*original_rule_R/22
    require(theorem_mean_cost == F(1, 2), 'The theorem original-rule bound is exactly11epsilon=delta0/2')
    return {'fixture_epsilon_exact': str(epsilon),
            'fixture_hidden_EPR': float(f'{hidden_epr:.12g}'),
            'fixture_zero_field_full_EPR': float(f'{full_epr:.12g}'),
            'theorem_regularization': 'epsilon = delta0/22',
            'theorem_original_rule_R_exact': str(original_rule_R),
            'theorem_mean_error_bound_over_delta0_exact': str(theorem_mean_cost),
            'sharper_generic_interface_mean_error_bound_over_delta0_exact': str(mean_cost_over_delta),
            'zero_field_full_EPR_upper_bound': 'log(22/delta0), in units k=1',
            'scope': 'The finite rational mixture verifies stationarity, support and EPR conventions. The theorem-scale tolerance is retained symbolically.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/finite_advantage.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    k, mu, rival_k, rival_mu, edges, degrees, construction = construction_checks()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                                           'scipy': scipy.__version__},
              'arithmetic': 'Exact fractions.Fraction identities, rational LDL and support combinatorics; separately labeled float64 matrix-exponential diagnostics',
              'finite_construction': construction, 'completely_positive_Gram': gram_checks(k, mu, edges, degrees),
              'positive_soft_selectors': soft_selector_checks(),
              'finite_clock_recovery_budget': recovery_budget_checks(),
              'finite_entropy_regularization': finite_entropy_checks(rival_k, rival_mu),
              'largest_dense_matrix_dimension': 12, 'large_target_allocated': False,
              'limitations': ['The verifier does not independently prove the all-rival controlled-mean transfer theorem.',
                              'The ten-atom obstruction concerns nonnegative Gram representations and is stronger than ordinary matrix rank.',
                              'Numerical protocol comparisons are finite diagnostics; exact generator intertwining is the structural certificate.',
                              'The target has six original-rule Bell sensitivities in (-1/2,1/2); the comparison permits rival endpoint barriers anywhere in[0,1] and is not the earlier fixed nineteen-level target family.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_name = Path('docs/FINITE_REVERSIBILITY_ADVANTAGE.md')
    report['proof_snapshot_sha256'] = {
        str(proof_name): hashlib.sha256((root/proof_name).read_bytes()).hexdigest()}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
