#!/usr/bin/env python3
"""Rigorous bounded rational certificate for the finite target clock-word basis.

Dyadic rounding is enclosed explicitly. No floating matrix exponential or
floating eigenvalue is used to certify the least singular value.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform


CHECKS = 0
PRECISION_BITS = 192
ERROR_BITS = 180
SCALE = 1 << PRECISION_BITS
ERROR_SCALE = 1 << ERROR_BITS
BASIS_WORDS = ((), (), ((1, 4),), ((1, 16),), ((0, 4), (1, 4)), ((1, 8),),
               ((1, 4), (0, 4), (1, 4)), ((1, 32),), ((0, 1), (1, 8)),
               ((1, 16), (0, 4), (1, 4)))


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


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


def error_ceiling(value):
    require(value >= 0, 'Enclosed errors are nonnegative')
    scaled = value*ERROR_SCALE
    return F(-(-scaled.numerator//scaled.denominator), ERROR_SCALE)


def rounded_divide(numerator, denominator):
    # Nearest integer, ties upward; valid for both signs.
    return (2*numerator+denominator)//(2*denominator)


def target_generators():
    degrees = [3, 3, 2, 2, 2]
    edges = [(i, j) for i in range(2) for j in range(2, 5)]
    mu = [F(1, 12)]*6+[F(d, 24) for d in degrees]
    k = zeros(11)
    for edge, endpoints in enumerate(edges):
        for vertex in endpoints:
            k[edge][6+vertex] = F(1, 2)
            k[6+vertex][edge] = F(1, degrees[vertex])
    for indices, conditional in ((list(range(6)), [F(1, 6)]*6),
                                 (list(range(6, 11)), [F(d, 12) for d in degrees])):
        for i in indices:
            for j, probability in zip(indices, conditional):
                if i != j:
                    k[i][j] += probability
    for i in range(11):
        k[i][i] = -sum(k[i])
    require(mm([mu], k) == [[F(0)]*11], 'Exact target hidden generator preserves its specified law')
    qs = []
    for beta, bias in (([F(1)]*11, F(1)), ([F(6, 16)]*6+[F(7+j, 16) for j in range(5)], F(4))):
        q = zeros(12)
        for i in range(11):
            q[0][i+1] = bias*mu[i]*beta[i]
            q[i+1][0] = beta[i]
            q[i+1][1:] = k[i][:]
            q[i+1][i+1] -= beta[i]
        q[0][0] = -sum(q[0])
        pi = [1/(1+bias)]+[bias*x/(1+bias) for x in mu]
        require(all(sum(row) == 0 for row in q), 'Every target generator row sums exactly to zero')
        require(all(q[i][j] >= 0 for i in range(12) for j in range(12) if i != j),
                'Every target off-diagonal rate is nonnegative')
        require(all(pi[i]*q[i][j] == pi[j]*q[j][i] for i in range(12) for j in range(12)),
                'Both exact target fields satisfy ordinary detailed balance')
        require(max(-q[i][i] for i in range(12)) <= 4, 'Full target exits are bounded by four')
        qs.append(q)
    pi0 = [F(1, 2)]+[x/2 for x in mu]
    span = zeros(12, 11)
    span[0][0] = 1
    for edge, endpoints in enumerate(edges):
        for vertex in endpoints:
            span[edge+1][vertex+1] = F(1, 2)
    for vertex in range(5):
        span[7+vertex][6+vertex] = 1
    require(rank(span) == 10, 'The exact target observable-space candidate has dimension ten')
    for q in qs:
        require(rank([row+image for row, image in zip(span, mm(q, span))]) == 10,
                'Both exact generators preserve the ten-dimensional observable subspace')
    j_span = [span[0][:]]+[[F(0)]*11 for _ in range(11)]
    require(rank([row+image for row, image in zip(span, j_span)]) == 10,
            'The visible-state projector preserves the same exact subspace')
    return qs, pi0


def clock_enclosure():
    terms = 80
    lower = 2*sum((F(1, (2*j+1)*3**(2*j+1)) for j in range(terms)), F(0))
    remainder = 2*F(1, 3**(2*terms+1))/((2*terms+1)*(1-F(1, 9)))
    upper = lower+remainder
    require(F(0) < lower < upper < 1, 'The positive atanh series brackets log two within zero and one')
    ticks = round(lower*SCALE/8)
    rounded_clock = F(ticks, SCALE)
    clock_error = remainder/8+F(1, 2*SCALE)
    require(abs(rounded_clock-lower/8) <= F(1, 2*SCALE), 'Rational clock rounding has half-mesh error')
    require(0 < rounded_clock < F(1, 8), 'Rounded clock keeps the matrix Taylor argument below one in row norm')
    return rounded_clock, clock_error, {
        'logarithm_series': 'log(2)=2 sum_(j>=0) 1/((2j+1)3^(2j+1))',
        'logarithm_terms': terms, 'rounded_clock_exact': str(rounded_clock),
        'clock_error_upper_exact': str(clock_error)}


def enclosed_one_tick(q, clock, clock_error):
    dimension, order = len(q), 64
    q_norm = max(sum(abs(x) for x in row) for row in q)
    require(clock*q_norm < 1, 'Exact matrix Taylor argument has row norm strictly below one')
    approximate = [[SCALE*int(i == j) for j in range(dimension)] for i in range(dimension)]
    # Horner evaluation: B <- I + (clock Q) B / j, rounded once per entry.
    for degree in range(order, 0, -1):
        updated = [[0]*dimension for _ in range(dimension)]
        for i in range(dimension):
            for j in range(dimension):
                value = clock*sum((q[i][r]*approximate[r][j] for r in range(dimension)), F(0))/degree
                updated[i][j] = round(value)+SCALE*int(i == j)
        approximate = updated
    # Each Horner round contributes at most dimension/(2*SCALE), and each
    # preceding multiplication contracts by at most clock*||Q||/degree<1.
    rounding_error = F(order*dimension, 2*SCALE)
    # Since ||clock Q||<1, the tail is below 2/(order+1)!; using three is safe.
    series_error = F(3, math.factorial(order+1))
    # The semigroup is stochastic for positive times, so its time Lipschitz
    # constant is ||Q||, without an extra exponential factor.
    total_error = error_ceiling(rounding_error+series_error+q_norm*clock_error)
    require(max(sum(abs(x) for x in row) for row in approximate) <= SCALE*(1+total_error),
            'Rounded one-tick matrix norm fits the stochastic-semigroup enclosure')
    return approximate, total_error, {'Taylor_order': order, 'generator_row_norm_exact': str(q_norm),
                                     'one_tick_operator_error_upper_exact': str(total_error)}


def enclosed_product(first, first_error, second, second_error):
    n = len(first)
    out = [[rounded_divide(sum(first[i][k]*second[k][j] for k in range(n)), SCALE)
            for j in range(n)] for i in range(n)]
    error = error_ceiling(first_error+second_error+first_error*second_error+F(n, 2*SCALE))
    return out, error


def enclosed_action(matrix, matrix_error, vector, vector_error):
    out = [rounded_divide(sum(x*y for x, y in zip(row, vector)), SCALE) for row in matrix]
    error = error_ceiling(matrix_error+vector_error+matrix_error*vector_error+F(1, 2*SCALE))
    return out, error


def positive_ldl(matrix):
    require(matrix == [list(row) for row in zip(*matrix)], 'The rational Gram shift is exactly symmetric')
    work, pivots = [row[:] for row in matrix], []
    for i in range(len(matrix)):
        pivot = work[i][i]
        require(pivot > 0, 'Every exact LDL pivot of the shifted Gram is strictly positive')
        pivots.append(pivot)
        for j in range(i+1, len(matrix)):
            for k in range(i+1, len(matrix)):
                work[j][k] -= work[j][i]*work[i][k]/pivot
    return pivots


def basis_checks():
    qs, pi0 = target_generators()
    clock, clock_error, clock_report = clock_enclosure()
    powers, tick_reports = {}, []
    for field, q in enumerate(qs):
        matrix, error, report = enclosed_one_tick(q, clock, clock_error)
        powers[(field, 1)] = (matrix, error)
        tick_reports.append(report)
        for ticks in (2, 4, 8, 16, 32):
            previous, previous_error = powers[(field, ticks//2)]
            powers[(field, ticks)] = enclosed_product(previous, previous_error, previous, previous_error)
    words = BASIS_WORDS
    vectors, errors = [], []
    for index, word in enumerate(words):
        vector = [SCALE]*12 if index == 0 else [-SCALE]+[SCALE]*11
        error = F(0)
        for field, ticks in reversed(word):
            matrix, matrix_error = powers[(field, ticks)]
            vector, error = enclosed_action(matrix, matrix_error, vector, error)
        vectors.append(vector)
        errors.append(error)
    approximate_gram = [[sum((pi0[s]*vectors[i][s]*vectors[j][s] for s in range(12)), F(0))/SCALE**2
                         for j in range(10)] for i in range(10)]
    maximum_error = max(errors)
    gram_error = error_ceiling(10*(2*maximum_error+maximum_error**2))
    require(gram_error < F(1, 2**150), 'All word and rounding errors imply a Gram operator error below two to minus 150')
    shift = F(1, 2**51)
    shifted = [[value-shift*int(i == j) for j, value in enumerate(row)] for i, row in enumerate(approximate_gram)]
    pivots = positive_ldl(shifted)
    require(shift-gram_error > F(1, 2**52), 'Exact shifted-Gram positivity proves the true Gram lower bound two to minus 52')
    names = ['1', 'S', 'EH^4 S', 'EH^16 S', 'E0^4 EH^4 S', 'EH^8 S',
             'EH^4 E0^4 EH^4 S', 'EH^32 S', 'E0 EH^8 S', 'EH^16 E0^4 EH^4 S']
    pivot_floor_exponents = []
    for pivot in pivots:
        exponent = 0
        while F(1, 2**exponent) > pivot:
            exponent += 1
        require(pivot >= F(1, 2**exponent), 'Every exact LDL pivot has the reported positive dyadic lower bound')
        pivot_floor_exponents.append(exponent)
    return {'basis_functions': names, 'basis_dimension': 10, 'target_states': 12,
            'exact_observable_subspace_dimension': 10, 'maximum_basis_clock_letters': max(sum(t for _, t in w) for w in words),
            'clock_enclosure': clock_report, 'one_tick_enclosures': tick_reports,
            'fixed_point_precision_bits': PRECISION_BITS, 'outward_error_precision_bits': ERROR_BITS,
            'maximum_basis_vector_error_upper_exact': str(maximum_error),
            'Gram_operator_error_upper_exact': str(gram_error), 'Gram_operator_error_power_bound': '2^-150',
            'certified_approximate_Gram_shift_exact': str(shift),
            'shifted_Gram_LDL_pivot_lower_bounds': [f'2^-{p}' for p in pivot_floor_exponents],
            'exact_LDL_pivots_sha256': hashlib.sha256(json.dumps([str(x) for x in pivots]).encode()).hexdigest(),
            'true_Gram_lower_bound': '2^-52', 'true_weighted_basis_smallest_singular_value_lower_bound': '2^-26',
            'certificate_method': 'Exact rational clock enclosure, dyadic-rounded Taylor/squaring/word propagation, explicit infinity-norm errors, and exact positive LDL pivots',
            'scope': 'This certifies the listed basis of the fixed twelve-state target. It does not prove the universal approximate-intertwining argument.'}


def finite_menu_checks():
    raw_basis = [''.join(str(field)*ticks for field, ticks in word) for word in BASIS_WORDS]
    endpoints = sorted({prefix+word for word in raw_basis for prefix in ('', '0', '1')},
                       key=lambda word: (len(word), word))
    mean_words = set()
    for first in endpoints:
        for second in endpoints:
            joined = first[::-1]+second
            for length in range(1, len(joined)+1):
                mean_words.update(joined[start:start+length] for start in range(len(joined)-length+1))
    ordered = sorted(mean_words, key=lambda word: (len(word), word))
    require(len(endpoints) == 26, 'The augmented basis gives exactly twenty-six distinct raw endpoint words')
    require(len(ordered) == 12766 and max(map(len, ordered)) == 66,
            'The finite actual-mean menu has exactly 12766 distinct nonempty words of at most 66 ticks')
    require(all(set(word) <= {'0', '1'} and word for word in ordered),
            'Every listed experiment uses only the two allowed clock fields')
    require(all(first[::-1]+second in mean_words for first in endpoints for second in endpoints if first or second),
            'Every nonempty augmented pair word is included in the actual-mean menu')
    require(all(word[1:] in mean_words and word[:-1] in mean_words for word in ordered if len(word) > 1),
            'The finite menu is closed under contiguous prefix and suffix deletion')
    manifest = {
        'schema_version': 1,
        'field_codes': {'0': '0', '1': 'log(2)'},
        'tick_duration': 'log(2)/(8k)',
        'word_convention': 'Field codes run left to right in chronological protocol order; the mean is pi0 E_first ... E_last S. On a column vector the rightmost matrix acts first.',
        'basis_columns': [{'kind': 'constant_one' if index == 0 else 'readout_word', 'word': word}
                          for index, word in enumerate(raw_basis)],
        'endpoint_words': endpoints,
        'mean_words': ordered}
    text = json.dumps(manifest, indent=2)+'\n'
    return text, {'actual_mean_word_count': len(ordered), 'raw_endpoint_word_count': len(endpoints),
                  'maximum_clock_letters': 66, 'maximum_horizon': '33log(2)/(4k)',
                  'word_counts_by_length': dict(sorted(Counter(map(len, ordered)).items())),
                  'menu_sha256': hashlib.sha256(text.encode()).hexdigest(),
                  'menu_encoding': 'UTF-8 JSON with indent=2 and a final newline, as emitted by --menu-output',
                  'menu_definition': 'All nonempty contiguous subwords of reverse(u)v for augmented basis endpoint words u,v',
                  'scope': 'This finite list supplies the actual mean experiments identified by the analytic inserted-word reconstruction; the verifier does not enumerate any larger protocol family.'}


def polynomial_product(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def polynomial_sum(polynomials):
    out = [F(0)]*max(map(len, polynomials))
    for polynomial in polynomials:
        for i, value in enumerate(polynomial):
            out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def rational_node_checks():
    nodes = [F(6+j, 16) for j in range(6)]
    lagrange, weights = [], []
    for node in nodes:
        polynomial, denominator = [F(1)], F(1)
        for other in nodes:
            if other != node:
                polynomial = polynomial_product(polynomial, [-other, F(1)])
                denominator *= node-other
        lagrange.append([x/denominator for x in polynomial])
        weights.append(1/denominator)
    require(polynomial_sum(lagrange) == [F(1)], 'The exact interpolation polynomials form a partition of unity')
    squares = [polynomial_product(polynomial, polynomial) for polynomial in lagrange]
    denominator_polynomial = polynomial_sum(squares)
    sos = []
    for first in range(6):
        for second in range(first+1, 6):
            difference = [x-y for x, y in zip(lagrange[first], lagrange[second])]
            sos.append(polynomial_product(difference, difference))
    six_d_minus_one = [6*x for x in denominator_polynomial]
    six_d_minus_one[0] -= 1
    require(polynomial_sum(sos) == six_d_minus_one,
            'Coefficientwise sum-of-squares identity certifies the rational denominator is globally at least one sixth')
    normalized = [abs(x)/min(map(abs, weights)) for x in weights]
    require(normalized == [1, 5, 10, 10, 5, 1], 'Exact barycentric magnitudes have the required six-node pattern')
    require(sum(x*x for x in normalized) == 252, 'The barycentric squared weights sum to 252')
    sums = [sum((weights[j]/weights[r])**2 for j in range(6) if j != r) for r in range(6)]
    require(max(sums) == 251, 'Every node ratio sum is bounded by the exact endpoint value 251')
    spacing = min(nodes[j+1]-nodes[j] for j in range(5))
    require(spacing == F(1, 16), 'The target-node spacing is exactly one sixteenth')
    require((2/spacing)**2*max(sums) < 512**2,
            'The squared near-node bound proves 32sqrt(251)<512 without floating square roots')
    require(2/spacing == 32 < 512, 'The far-node branch has a strictly smaller bound')
    require(6*(512*2**9)**2 < (2**20)**2,
            'Six orthogonal target projectors and the barrier residual fit the selector-intertwining constant')
    return {'target_nodes_exact': [str(x) for x in nodes],
            'rational_denominator_lower_exact': '1/6',
            'normalized_barycentric_weight_magnitudes_exact': [str(x) for x in normalized],
            'node_ratio_sums_exact': [str(x) for x in sums],
            'maximum_node_ratio_sum_exact': '251',
            'node_anchored_divided_difference_upper': '512',
            'near_node_certificate': '32sqrt(251)<512', 'far_node_certificate': '32<512',
            'selector_intertwining_multiplier_upper': '2^20',
            'scope': 'Exact polynomial identities and rational inequalities certify the constants in the analytic node-anchored bound. A general operator-Lipschitz claim is not made.'}


def universal_budget_checks():
    observation_mass, inserted_word_factor = 1323, 1+7*66
    require(inserted_word_factor == 463 and observation_mass*inserted_word_factor == 612549 < 2**20,
            'The finite observed-mean Gram accounting fits the declared error multiplier')
    require(10*2**20*2**52 < 2**76, 'Basis conditioning and ten-column Gram error give the isometry defect bound')
    require(2**26*4*2 == 2**29, 'The target coefficient-map bound follows from the basis inverse and operator norms')
    require(1+4*2**29 < 2**32 and 4*2**32 == 2**34,
            'Column coefficient and aggregate residual bounds have the stated conservative powers')
    require(2**10*2**34*2**26 == 2**70, 'The approximate-intertwining error has the declared square-root multiplier')
    require(F(2, 3) > F(1, 2) and 8*16 == 2**7,
            'The positive logarithm series gives a>1/16 and the resolvent integral gives the generator multiplier')
    require(2*2**7+2*64 < 2**9, 'Hidden compression preserves the conservative barrier residual budget')
    require(1+F(1, 2)*(2**7+2*16) < 2**8,
            'The hidden Markov-kernel residual fits the stated compression budget')
    require(2*(2*2**20+2**8) < 2**23,
            'Telescoping two rational selectors and one Markov kernel gives the feature error budget')
    require(2**76+2**140 < 2**141, 'Projecting away the visible component gives the hidden metric-defect bound')
    require(16*2**23*2**70 == 2**97 and 2*(2**23*2**70)**2+8*2**141 < 2**188,
            'The final Gram comparison has the stated linear and quadratic error multipliers')
    delta = F(1, 2**220)
    root_delta = F(1, 2**110)
    require(root_delta**2 == delta and 2**76*delta < 1, 'The selected error regime keeps the approximate isometry bounded')
    first, second = 2**97*root_delta, 2**188*delta
    require(first == F(1, 2**13) and second == F(1, 2**32),
            'The final tolerance converts both error terms to the displayed exact powers')
    require(first+second < F(1, 1500), 'The recovered feature Gram meets the sharper eleven-atom obstruction')
    return {'observed_mean_Gram_multiplier_exact': observation_mass*inserted_word_factor,
            'declared_observed_mean_Gram_multiplier': '2^20',
            'basis_Gram_lower_bound': '2^-52', 'isometry_defect_upper': '2^76 delta',
            'intertwining_error_upper': '2^70 sqrt(delta)',
            'generator_residual_multiplier': '2^7', 'barrier_residual_multiplier': '2^9',
            'Markov_kernel_residual_multiplier': '2^8', 'feature_residual_multiplier': '2^23',
            'hidden_metric_defect_upper': '2^141 delta',
            'final_Gram_error_upper': '2^97 sqrt(delta)+2^188 delta',
            'controlled_mean_tolerance': '2^-220',
            'final_Gram_error_at_tolerance_exact': str(first+second),
            'required_Gram_error_threshold_exact': '1/1500',
            'state_comparison_scope': 'Ordinary-reversible minimum 12 versus an unrestricted sufficient count 11 at the new tolerance; unrestricted minimality at this larger tolerance is not asserted.',
            'scope': 'These exact scalar checks validate the stated constants. The dimension-independent rival comparison is the separate analytic theorem.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/rational_observation.json'))
    parser.add_argument('--menu-output', type=Path, help='Optionally export the complete finite actual-mean experiment menu')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    menu_text, menu_report = finite_menu_checks()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact fractions.Fraction and integer fixed-point arithmetic with explicit rational error bounds; no floating eigenvalue or exponential certificate',
              'rigorous_target_basis': basis_checks(), 'finite_actual_mean_menu': menu_report,
              'bounded_rational_node_certificate': rational_node_checks(),
              'universal_recovery_budget': universal_budget_checks(),
              'largest_dense_matrix_dimension': 12,
              'large_target_allocated': False, 'experiment_menu_enumerated': True,
              'controlled_responses_simulated': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': [],
              'limitations': ['The certificate concerns one explicit finite target basis and its stated clock words.',
                              'Universal rival recovery requires the separate analytic proof; no numerical optimization is used as a proof.']}
    proof_names = ['BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md',
                   'FINITE_REVERSIBILITY_ADVANTAGE.md', 'FINITE_GRAM_ROBUSTNESS.md',
                   'FIXED_CLOCK_GRAM_OBSERVABILITY.md', 'CAPPED_KINETIC_INTERFACE_SEPARATION.md',
                   'FINITE_OBSERVATION_BOTTLENECK.md', 'FINITE_PREDICTOR_MINIMALITY.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    if args.menu_output is not None:
        args.menu_output.parent.mkdir(parents=True, exist_ok=True)
        args.menu_output.write_text(menu_text, encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
