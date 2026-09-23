#!/usr/bin/env python3
"""Bounded exact certificates for finite predictor minimality and Gram robustness.

Only tiny matrices, support rectangles and rational polynomial identities are
enumerated. The analytic controlled-mean recovery theorem remains separate.
"""
import argparse
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
import math
from pathlib import Path
import platform


CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    work, row = [values[:] for values in a], 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][col]
        work[row] = [x/scale for x in work[row]]
        for i in range(len(a)):
            if i != row:
                scale = work[i][col]
                work[i] = [x-scale*y for x, y in zip(work[i], work[row])]
        row += 1
        if row == len(a):
            break
    return row


def target_gram():
    gram = zeros(10)
    degrees = [3, 3, 2, 2, 2]
    edges = [(i, j) for i in range(2) for j in range(2, 5)]
    for i, degree in enumerate(degrees):
        gram[i][i], gram[5+i][5+i] = F(degree, 48), F(degree, 24)
    for i, j in edges:
        gram[i][j] = gram[j][i] = F(1, 48)
    require(rank(gram) == 9, 'The ordinary rank is nine, below both positive-factorization requirements')
    return gram, edges, degrees


def square_root_witness_checks(gram, edges):
    # Squared rational coordinates make sqrt(x_u*x_v) rational while still
    # exercising all overlap formulas on an arbitrary nonnegative factor.
    roots = [[F(((s+1)*(j+2)) % 7, 7) for j in range(10)] for s in range(3)]
    atoms = [[x*x for x in row] for row in roots]
    auxiliary = [[roots[s][i]*roots[s][j] for i, j in edges]+atoms[s][5:]
                 for s in range(3)]
    example_gram = mm(transpose(atoms), atoms)
    witness_gram = mm(transpose(auxiliary), auxiliary)
    require(rank(witness_gram) <= 3, 'Eleven auxiliary vectors occupy the same three-dimensional atom space')
    pair_types = {'shared_U': 0, 'shared_V': 0, 'disjoint': 0}
    for first, second in combinations(range(6), 2):
        u, v = edges[first]
        a, b = edges[second]
        if u == a:
            upper = example_gram[u][u]*example_gram[v][b]
            pair_types['shared_U'] += 1
        elif v == b:
            upper = example_gram[v][v]*example_gram[u][a]
            pair_types['shared_V'] += 1
        else:
            upper = example_gram[u][a]*example_gram[v][b]
            pair_types['disjoint'] += 1
        require(witness_gram[first][second]**2 <= upper,
                'Exact squared overlap satisfies the appropriate Cauchy-Schwarz pairing')
    require(pair_types == {'shared_U': 6, 'shared_V': 3, 'disjoint': 6},
            'K2,3 has the stated edge-neighbor counts')
    for edge, (u, v) in enumerate(edges):
        require(witness_gram[edge][edge] == example_gram[u][v],
                'Edge-witness squared norm is the original edge entry')
        for isolated in range(5):
            require(witness_gram[edge][6+isolated]**2 <=
                    example_gram[u][5+isolated]*example_gram[v][5+isolated],
                    'Edge-isolated overlap uses two target-zero entries')
    epsilon = F(1, 1500)
    u_square, v_square = (F(1, 16)+epsilon)*epsilon, (F(1, 24)+epsilon)*epsilon
    require(u_square == F(379, 3000**2) and v_square == F(254, 3000**2),
            'Square-root overlap radicands have the stated exact rational values')
    u_upper, v_upper = F(1, 150), F(2, 375)
    require(u_square < u_upper**2 and v_square < v_upper**2,
            'Both rational square-root upper bounds are strictly valid')
    edge_off_diagonal = 2*u_upper+v_upper+2*epsilon
    require(edge_off_diagonal == F(1, 50), 'Strict edge-row overlap sum is bounded by one fiftieth')
    strict_edge_lower = F(1, 48)-epsilon-edge_off_diagonal
    isolated_lower = F(1, 12)-5*epsilon
    correction = 30*epsilon**2/isolated_lower
    require(strict_edge_lower == F(1, 6000) and isolated_lower == F(2, 25),
            'Edge and isolated spectral bounds have the declared rational constants')
    require(correction == strict_edge_lower,
            'Schur correction equals the non-strict endpoint, so strict root inequalities make the complement positive')
    require(F(1, 40000)/epsilon == F(3, 80), 'The new intermediate tolerance improves by exactly eighty thirds')
    return {'entry_tolerance_exact': str(epsilon), 'auxiliary_witness_vectors': 11,
            'excluded_maximum_nonnegative_Gram_atoms': 10, 'toy_factor_atoms': 3,
            'edge_pair_types': pair_types, 'strict_edge_spectral_lower_exact': str(strict_edge_lower),
            'isolated_spectral_lower_exact': str(isolated_lower), 'Schur_correction_upper_exact': str(correction),
            'improvement_factor_exact': '80/3',
            'scope': 'Exact rational constants certify the strict Schur argument. The three-atom overlap fixture is not claimed close to the target Gram, and no measured-mean tolerance of 1/1500 is asserted.'}


def rectangle_checks(gram):
    support = {(i, j) for i in range(5) for j in range(5) if gram[i][j] > 0}
    maximal = set()
    for row_mask in range(1, 1 << 5):
        rows = {i for i in range(5) if row_mask >> i & 1}
        columns = {j for j in range(5) if all((i, j) in support for i in rows)}
        if columns:
            closure = {i for i in range(5) if all((i, j) in support for j in columns)}
            maximal.add((tuple(sorted(closure)), tuple(sorted(columns))))
    ordered = sorted(maximal)
    cells = [{(i, j) for i in rows for j in columns} for rows, columns in ordered]
    require(len(support) == 17 and len(cells) == 18, 'The five-by-five support has seventeen positive cells and eighteen maximal rectangles')
    all_positive_rectangles = 0
    for row_mask in range(1, 1 << 5):
        for column_mask in range(1, 1 << 5):
            candidate = {(i, j) for i in range(5) for j in range(5)
                         if row_mask >> i & 1 and column_mask >> j & 1}
            if candidate <= support:
                all_positive_rectangles += 1
                require(any(candidate <= rectangle for rectangle in cells),
                        'Every positive rectangle extends to an enumerated maximal rectangle')
    cover_sizes, uncovered_certificate = [], []
    for indices in combinations(range(len(cells)), 4):
        covered = set().union(*(cells[i] for i in indices))
        missing = sorted(support-covered)
        require(bool(missing), 'Four maximal rectangles fail to cover the complete support')
        cover_sizes.append(len(covered))
        uncovered_certificate.append([list(indices), list(missing[0])])
    require(len(cover_sizes) == math.comb(18, 4) == 3060 and max(cover_sizes) == 16,
            'All 3060 four-rectangle candidates miss at least one of seventeen cells')
    row_stars = [{(i, j) for j in range(5) if (i, j) in support} for i in range(5)]
    require(set().union(*row_stars) == support, 'Five positive row-star rectangles attain the support cover bound')
    require(all(gram[i][i] > 0 and all(gram[i][j] == gram[j][i] == 0 for j in range(10) if j != i)
                for i in range(5, 10)), 'Each of the five isolated positive diagonals needs its own rectangle')
    epsilon, minimum, maximum, atoms = F(1, 40000), F(1, 48), F(1, 8), 9
    left, right = atoms**2*epsilon*(maximum+epsilon), (minimum-epsilon)**2
    require(left == F(405081, 1600000000) and right == F(6235009, 14400000000),
            'The robust nonnegative-rank obstruction has the advertised rational products')
    require(right-left == F(16183, 90000000) > 0,
            'A shared atom assigned to incompatible cells contradicts the entry tolerance')
    return {'leading_block_positive_cells': len(support), 'maximal_positive_rectangles':
            [{'rows': list(rows), 'columns': list(columns)} for rows, columns in ordered],
            'all_positive_rectangles_checked': all_positive_rectangles,
            'four_rectangle_combinations_checked': len(cover_sizes),
            'maximum_cells_covered_by_four_rectangles': max(cover_sizes),
            'uncovered_cell_certificate_sha256': hashlib.sha256(json.dumps(uncovered_certificate, separators=(',', ':')).encode()).hexdigest(),
            'leading_block_Boolean_rank': 5, 'full_Boolean_rank': 10,
            'robust_entry_tolerance_exact': str(epsilon), 'excluded_maximum_nonnegative_factor_atoms': atoms,
            'strict_product_inequality_margin_exact': str(right-left),
            'scope': 'A complete bounded support enumeration supplies the five-rectangle lower. The analytic dominant-atom argument converts the positive error tolerance to this support obstruction.'}


def predictor_factorization_checks(gram, edges, degrees):
    mu = [F(d, 24) for d in degrees]*2
    refresh = [F(d, 12) for d in degrees]
    k = zeros(10)
    for i in range(5):
        k[i][5+i] = F(1)
        k[5+i][i] = F(1, 2)
        for j in range(5):
            if (min(i, j), max(i, j)) in edges:
                k[5+i][j] = F(1, 2*degrees[i])
        for offset in (0, 5):
            for j in range(5):
                if i != j:
                    k[offset+i][offset+j] = refresh[j]
    for i in range(10):
        k[i][i] = -sum(k[i])
    require(all(isinstance(value, F) for row in k for value in row),
            'The reconstructed predictor generator contains only exact rational entries')
    require(mm([mu], k) == [[F(0)]*10], 'The explicit ten-hidden-state predictor remains stationary')
    require(max(-k[i][i] for i in range(10)) <= 2, 'The explicit predictor respects the cap-two interface class')
    p = [[F(i == j)+k[i][j]/2 for j in range(10)] for i in range(10)]
    memory = [[F(i == j and i < 5) for j in range(10)] for i in range(10)]
    features, reversed_features = [], []
    for index in range(5):
        probe = [[F(i == j == 5+index) for j in range(10)] for i in range(10)]
        features.append([[2*x for x in row] for row in mm(mm(memory, p), probe)])
        reversed_features.append([[2*x for x in row] for row in mm(mm(probe, p), memory)])
    for index in range(5):
        probe = [[F(i == j == 5+index) for j in range(10)] for i in range(10)]
        features.append(probe)
        reversed_features.append(probe)
    left = [mm([mu], operator)[0] for operator in reversed_features]
    right = [[sum(operator[state]) for operator in features] for state in range(10)]
    require(min(x for row in left+right for x in row) >= 0, 'Formal reversed positive words give nonnegative left and right factors')
    require(mm(left, right) == gram, 'The explicit nonreversible predictor gives an exact ten-atom nonnegative factorization')
    actual_gram = mm(transpose(right), [[mu[i]*x for x in row] for i, row in enumerate(right)])
    require(actual_gram != gram, 'Without reversibility the observable formal-reverse matrix is not the actual feature Gram')
    require(max(abs(actual_gram[i][j]-gram[i][j]) for i in range(10) for j in range(10)) == F(1, 16),
            'The explicit gap guards against silently equating formal reversal and stationary adjoint')
    return {'predictor_hidden_states': 10, 'predictor_total_states': 11,
            'exact_nonnegative_factor_atoms': 10, 'actual_Gram_difference_max_exact': '1/16',
            'scope': 'The positive factorization is reconstructed from the earlier explicit predictor. Its all-control generator intertwining is covered by the frozen finite-advantage verifier.'}


def polynomial_product(a, b):
    output = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i+j] += x*y
    return output


def polynomial_sum(polynomials):
    output = [F(0)]*max(map(len, polynomials))
    for polynomial in polynomials:
        for i, value in enumerate(polynomial):
            output[i] += value
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return output


def evaluate(polynomial, x):
    return sum((value*x**i for i, value in enumerate(polynomial)), F(0))


def selector_boundary_checks():
    grid = [F(6+j, 16) for j in range(6)]
    lagrange, selectors, denominators = [], [], []
    for j, location in enumerate(grid):
        polynomial, denominator = [F(1)], F(1)
        for other in grid:
            if other != location:
                polynomial = polynomial_product(polynomial, [-other, F(1)])
                denominator *= location-other
        polynomial = [x/denominator for x in polynomial]
        lagrange.append(polynomial)
        selectors.append(polynomial_product(polynomial, polynomial))
        denominators.append(denominator)
        require(all(evaluate(selectors[j], x) == F(i == j) for i, x in enumerate(grid)),
                'Exact degree-ten squared selectors interpolate all six labels')
        derivative = [i*x for i, x in enumerate(selectors[j])][1:]
        second = [i*x for i, x in enumerate(derivative)][1:]
        require(len(selectors[j])-1 == 10 and all(evaluate(derivative, x) == 0 and evaluate(second, x) != 0
                                                for i, x in enumerate(grid) if i != j),
                'Every excluded interior label is a root of exactly multiplicity two')
    require(denominators[2] == -F(3, 262144), 'The selected interpolation denominator has its exact sign and magnitude')
    require(selectors[2][-1] == F(68719476736, 9), 'The leading selector coefficient has the stated large value')
    require(selectors[2][0] == 12006225, 'The permitted zero-barrier endpoint has the stated selector amplification')
    require(polynomial_sum(lagrange) == [F(1)], 'The Lagrange partition of unity is a polynomial identity')
    denominator_polynomial = polynomial_sum(selectors)
    difference_squares = []
    for first, second in combinations(lagrange, 2):
        difference = [x-y for x, y in zip(first, second)]
        difference_squares.append(polynomial_product(difference, difference))
    six_d_minus_one = [6*x for x in denominator_polynomial]
    six_d_minus_one[0] -= 1
    require(polynomial_sum(difference_squares) == six_d_minus_one,
            'The coefficientwise sum-of-squares identity proves the rational-selector denominator is at least one sixth')
    return {'target_labels_exact': [str(x) for x in grid], 'minimum_positive_polynomial_selector_degree': 10,
            'selector_2_denominator_exact': str(denominators[2]),
            'selector_2_leading_coefficient_exact': str(selectors[2][-1]),
            'selector_2_at_zero_exact': str(selectors[2][0]),
            'rational_selector_denominator_lower_exact': '1/6',
            'polynomial_identity': '6 sum_j L_j(x)^2 - 1 = sum_(i<j) (L_i(x)-L_j(x))^2',
            'scope': 'Exact coefficient identities support the selector boundary and rational normalization. No controlled-mean recovery inequality for inverse denominator insertions is asserted.'}


def nonreversible_recovery_checks():
    # Full exit cap four gives Q+4I >=0 entrywise. For a=log(2)/8,
    # sqrt(2) E=exp[a(Q+4I)] >=I and the centered defect has row norm sqrt(2)-1.
    require(F(17, 12)**2 > 2, 'The exact square comparison gives sqrt(2)-1<5/12')
    require(F(5, 3)**2 > 2 and 2 < 4,
            'The operator-radius ratio 4+3sqrt(2) and coefficient-radius ratio 3+3sqrt(2) are both below nine')
    require(9 < 16, 'Both centered-log majorants are below 8 log_2(16)=32')
    d, j_exponent, cutoff, tolerance_exponent = 42, 289, 520, 1360
    majorant = 2**j_exponent*32**d
    require(majorant == 2**499, 'The nonreversible whole-polynomial majorant keeps the same exponent 499')
    require(F(19, 3) < 7 and 1+7*cutoff == 3641 < 2**12,
            'The inserted-word preparation constant gives the stated finite clock coefficient')
    tail = majorant*2*F(1, 2**(cutoff+1))
    propagated = majorant*3**cutoff*(1+7*cutoff)*F(1, 2**tolerance_exponent)
    require(3**5 < 2**8 and cutoff == 5*104,
            'An exact small integer inequality bounds the centered-log coefficient amplification')
    require(tail == F(1, 2**21) and propagated < F(1, 2**17),
            'Exact centered total-degree errors obey the conservative tail and mean-error powers')
    require(tail+propagated < F(1, 2**16), 'The recovered entry error is strictly below two to minus sixteen')
    require(tail+propagated < F(1, 40000) < F(1, 1500),
            'The same controlled-mean tolerance is sufficient for both positive-factor obstructions')
    return {'clock_duration': 'log(2)/(8k)', 'full_exit_cap_in_k_units': 4,
            'centered_infinity_norm_clock_defect': 'sqrt(2)-1<5/12',
            'operator_majorant_ratio': '4+3sqrt(2)<9',
            'coefficient_majorant_ratio': '3+3sqrt(2)<9',
            'logarithm_majorant_upper': '8log_2(9)<32',
            'whole_polynomial_majorant': '2^499', 'maximum_clock_letters': cutoff,
            'controlled_mean_tolerance': '2^-1360', 'recovered_entry_error_upper': '2^-21+2^-17<2^-16<1/40000',
            'scope': 'This exact arithmetic checks the nonreversible norm and total-degree constants; uniform word recovery and the all-rival quantifier are supplied by the analytic proof.'}


def selective_gate_return_checks():
    q = [[F(-6), F(3), F(3), F(0)], [F(3), F(-3), F(0), F(0)],
         [F(3), F(0), F(-3), F(0)], [F(0)]*4]
    pi = [F(1, 5), F(1, 5), F(1, 5), F(2, 5)]
    require(mm([pi], q) == [[F(0)]*4] and all(pi[i]*q[i][j] == pi[j]*q[j][i]
                                                            for i in range(4) for j in range(4)),
            'The selective-gate fixture preserves the full local-balance ratio')
    q_squared = mm(q, q)
    propagator = [[F(i == j)+F(29, 144)*q[i][j]+F(5, 432)*q_squared[i][j]
                   for j in range(4)] for i in range(4)]
    modes = [[F(1), F(1), F(1), F(0)], [F(0), F(0), F(0), F(1)],
             [F(0), F(1), F(-1), F(0)], [F(-2), F(1), F(1), F(0)]]
    require(rank(modes) == 4, 'Four explicit rational eigenmodes span the full state space')
    for mode, rate, factor in zip(modes, (0, 0, -3, -9), (F(1), F(1), F(1, 2), F(1, 8))):
        column = [[x] for x in mode]
        require(mm(q, column) == [[rate*x] for x in mode], 'Exact generator eigenmode has the declared decay rate')
        require(mm(propagator, column) == [[factor*x] for x in mode],
                'The rational propagator interpolates exp(tQ) exactly at t=log(2)/3')
    require(all(sum(row) == 1 and min(row) >= 0 for row in propagator), 'The exact full propagator is stochastic')
    compressed = [[propagator[i][j] for j in range(1, 4)] for i in range(1, 4)]
    killed = [[F(i == j)*(F(1, 2) if i < 2 else F(1)) for j in range(3)] for i in range(3)]
    require([row[:2] for row in compressed[:2]] == [[F(29, 48), F(5, 48)], [F(5, 48), F(29, 48)]],
            'Selective-gate compression has the stated reinjection cross terms')
    require(compressed != killed and compressed[0][1] == F(5, 48) > 0,
            'Hub reinjection prevents identifying physical compression with the killed hidden semigroup')
    require(sum(compressed[0]) == F(17, 24) == F(2, 3)+F(1, 24),
            'The selected constant mode retains its positive equilibrium component')
    return {'states': 4, 'gate_equilibrium_bias_exact': '4', 'active_return_rate_exact': '3',
            'observation_time': 'log(2)/3', 'selected_block_exact': [['29/48', '5/48'], ['5/48', '29/48']],
            'selected_block_row_sum_exact': '17/24', 'killed_selected_row_sum_exact': '1/2',
            'scope': 'This small selective-gate example isolates hub reinjection. It is not an additional controlled-mean certificate for the fixed two-field target.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/finite_minimality.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    gram, edges, degrees = target_gram()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact fractions.Fraction, integer support enumeration, rational matrix products and coefficientwise polynomial identities; no numerical optimization',
              'sharper_nonnegative_Gram_obstruction': square_root_witness_checks(gram, edges),
              'robust_nonnegative_factorization_obstruction': rectangle_checks(gram),
              'explicit_predictor_factorization': predictor_factorization_checks(gram, edges, degrees),
              'selector_observation_boundary': selector_boundary_checks(),
              'selective_gate_reinjection_boundary': selective_gate_return_checks(),
              'nonreversible_clock_recovery': nonreversible_recovery_checks(),
              'finite_EPR_corollary': {
                  'regularization_parameter': 'eta = delta/22 for 0<delta<=2^-1360',
                  'controlled_mean_error_upper': 'delta/2',
                  'full_zero_field_identity_EPR_upper': 'k log(22/delta)',
                  'verification_scope': 'Analytic parameter substitution into the previously verified finite-advantage regularization; no new EPR fixture is claimed here.'},
              'largest_dense_matrix_dimension': 11, 'large_target_allocated': False,
              'controlled_protocols_enumerated': False,
              'limitations': ['Finite certificates do not replace the analytic arbitrary-rival controlled-mean transfer proof.',
                              'The stronger 1/1500 bound concerns an intermediate Gram matrix, not measured means.',
                              'The rational selectors have no proved observation-recovery budget here.',
                              'The explicit state advantage remains at a rigorously positive but impractical tolerance 2^-1360.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_names = ['FINITE_GRAM_ROBUSTNESS.md', 'FINITE_PREDICTOR_MINIMALITY.md',
                   'FINITE_OBSERVATION_BOTTLENECK.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
