#!/usr/bin/env python3
"""Exact premises for observable preparation and readout calibration boundaries.

This is not a five-type state-count or full sampling certificate. The
hash-bound notes prove the universal statements. All finite checks use
rational arithmetic, polynomial identities, and matrices of dimension three.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
HELPER = 'verify_familiar_switch_margin.py'
HELPER_SHA = 'e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397'
INPUT = 'reports/switch_serial_reset.json'
INPUT_SHA = '9c9f662e63d94d518d3e01bf0aa179dffa6f06d78a2333660e3668582d972fb6'
PROOFS = {
    'docs/FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md': 'deb3e0e892ee790a97f96f3684091c9fccca78ef3db6a135b8237a2b79680ccd',
    'docs/FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md': '751f35f34dc63cfd481694550e09276a7c1115d5464731eacaacd6a7305916c3',
    'docs/FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md': 'be46dd47f5a6d0ef07300c59349ff282f45c185d9aca673731f75bc2d9e55c56',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    payload = (ROOT/INPUT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_SHA,
            'The serial-reset report is the explicitly frozen prerequisite')
    prior = json.loads(payload)
    require(prior['status'] == 'PASS', 'The inherited numerical certificate passed')
    for name, expected in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == expected,
                'Each inherited verifier source matches its frozen expected hash')
    for name, expected in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each inherited mathematical proof matches its frozen expected hash')
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The exact helper has its unconditional expected source hash')
    require(len(PROOFS) == 3 and all(len(value) == 64 for value in PROOFS.values()),
            'All three new mathematical notes have unconditional expected hashes')
    for name, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each new mathematical note matches its reviewed snapshot')
    spec = importlib.util.spec_from_file_location('observable_calibration_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    return h, prior


def total_variation(left, right):
    return sum(abs(a-b) for a, b in zip(left, right))/2


def response_lemma_certificate(h):
    q01, q02, a1, a2, q12, q21, d, hidden, f0, f1, f2 = [h.Poly.variable(11, i) for i in range(11)]
    kernel = [[1-q01-q02, q01, q02], [a1, 1-a1-q12, q12], [a2, q21, 1-a2-q21]]
    delta = [d, -d/2+hidden, -d/2-hidden]
    response, signs = [f0, f1, f2], [-1, 1, 1]
    increment = [[kernel[i][j]-F(i == j) for j in range(3)] for i in range(3)]
    drift = h.mm([delta], increment)[0]
    response_drift = sum(a*b for a, b in zip(drift, response))
    sign_drift = sum(a*b for a, b in zip(drift, signs))
    bias = sum(a*b for a, b in zip(delta, response))
    k = (a1+a2)/2+q12+q21
    beta0 = q01+q02
    tau = (q01-q02)/2+(a1-a2)/4+(q12-q21)/2
    bracket = f0-(f1+f2)/2
    require(response_drift == -k*bias-sign_drift*bracket/2+d*(k*bracket+tau*(f1-f2)),
            'The sharp approximate-balance response identity holds as a formal polynomial')
    require(beta0+k-2*tau == 2*q02+a2+2*q21
            and beta0+k+2*tau == 2*q01+a1+2*q12,
            'Both signs of the mixing coefficient are bounded by explicitly nonnegative transition sums')
    coefficient_row = [k, -k/2+tau, -k/2-tau]
    require(sum(coefficient_row) == 0
            and sum(a*b for a, b in zip(coefficient_row, response)) == k*bracket+tau*(f1-f2),
            'The imbalance remainder has zero mass and the stated response-span coefficient row')
    b, v = [h.Poly.variable(2, i) for i in range(2)]
    require((1-b)*(1+v)+(1+b)*(1-v) == 2*(1-b*v),
            'The stationary singleton-flow bound yields the exact relaxation amplification numerator')
    require((1-v)+(1+v) == 2,
            'The direct imbalance remainder has the unamplified span coefficient two over one minus v')
    alpha, beta, sign, future_a, future_b = [h.Poly.variable(5, i) for i in range(5)]
    first = beta*(F(2, 5)+F(3, 5)*alpha*sign)*future_a-F(3, 10)*alpha*sign
    second = beta*(-F(2, 5)-F(12, 25)*alpha*sign)*future_b+F(3, 10)*alpha*sign
    combined = beta*((F(2, 5)+F(3, 5)*alpha*sign)*future_a-(F(2, 5)+F(12, 25)*alpha*sign)*future_b)
    require(first+second == combined,
            'The two initial-bit score terms cancel pointwise before any preparation assumption')
    extrema = [(F(2, 5)+F(3, 5)*aa*ss)*xa-(F(2, 5)+F(12, 25)*aa*ss)*xb
               for aa, ss, xa, xb in product((F(0), F(1)), (-1, 1), (-1, 1), (-1, 1))]
    require(max(map(abs, extrema)) == F(47, 25),
            'The multilinear score-response corners prove its uniform span bound 94 beta over 25')
    V, guard, low_ceiling = F(1, 10000), F(9, 20), F(3, 20)
    r0, C = 1-low_ceiling/guard, (1+V)/(1-V)
    multiplier = 4*C/r0
    a = multiplier
    bb = F(47, 25)*a
    cc = (bb+F(94, 25)/(1-V))/guard
    floor = F(94, 25)*V/(1-V)
    require(r0 == F(2, 3) and C == F(10001, 9999) and multiplier == F(20002, 3333)
            and floor == F(94, 249975),
            'The conservative observed-correlation guards give the advertised exact relaxation and score-bias constants')
    require(F(2)*V/(1-V) == F(2, 9999),
            'Endpoint and correlation response radii have the stated zero-drift stationary-bias floor')
    # A stationary null outside the local gates can have a larger score.
    identity_score = F(3, 5)-F(12, 25)-F(2, 25)
    require(identity_score == F(1, 25) > F(367, 100000),
            'Identity kernels show why a score-only preparation bound cannot replace the stationary reference gates')
    return {'stationary_bias_absolute_bound_exact': str(V),
            'observed_detector_product_guard_exact': str(guard),
            'observed_low_correlation_upper_exact': str(low_ceiling),
            'latent_relaxation_lower_exact': str(r0),
            'uniform_balance_factor_exact': str(C),
            'response_drift_multiplier_exact': str(multiplier),
            'score_span_over_final_contrast_exact': '94/25',
            'score_correction_coefficients_order': ['abs(score_drift)', 'abs(low_final_mean)', 'abs(initial_mean)'],
            'score_correction_coefficients_exact': list(map(str, (a, bb, cc))),
            'score_stationary_bias_floor_exact': str(floor),
            'endpoint_and_correlation_stationary_bias_floor_exact': '2/9999',
            'scope': 'At most three states and an exactly stationary, readout-preserving, error-independent instrument. The general response lemma does not require reversibility. These observable inequalities do not establish five-type state-count separation or a complete statistical test.'}, (a, bb, cc)


def instrument_certificate(h):
    pi = [F(1, 2), F(1, 4), F(1, 4)]
    high = [F(1, 5), F(2, 5), F(2, 5)]
    signs = [-1, 1, 1]
    p = F(1, 100)
    identity = h.identity(3)
    projection = [[F(1, 3), F(2, 3), F(0)], [F(1, 3), F(2, 3), F(0)], [F(0), F(0), F(1)]]
    low_reset, high_reset = [[x for x in pi] for _ in range(3)], [[x for x in high] for _ in range(3)]
    low_kernel = [[(identity[i][j]+pi[j])/2 for j in range(3)] for i in range(3)]
    high_kernel = [[identity[i][j]/4+projection[i][j]/4+high[j]/2 for j in range(3)] for i in range(3)]
    require(high == [pi[i]*(1+F(3, 5)*signs[i]) for i in range(3)]
            and h.mm(projection, projection) == projection
            and h.mm(projection, high_reset) == h.mm(high_reset, projection) == high_reset,
            'The physical counterexample has the correct stationary tilt and commuting reset projections')
    require(h.mm([[F(identity[i][j]+high_reset[i][j], 2) for j in range(3)] for i in range(3)],
                 [[F(identity[i][j]+projection[i][j], 2) for j in range(3)] for i in range(3)]) == high_kernel,
            'Commuting projection exponentials reproduce the high-field clock exactly')
    for kernel, law in ((low_kernel, pi), (high_kernel, high)):
        require(all(min(row) > 0 and sum(row) == 1 for row in kernel)
                and h.mm([law], kernel) == [law]
                and all(law[i]*kernel[i][j] == law[j]*kernel[j][i] for i, j in product(range(3), repeat=2)),
                'Both fixture clocks are strictly positive, stochastic, stationary, and ordinarily reversible')
    for generator_core, law in (([[low_reset[i][j]-identity[i][j] for j in range(3)] for i in range(3)], pi),
                                ([[high_reset[i][j]+projection[i][j]-2*identity[i][j] for j in range(3)] for i in range(3)], high)):
        require(all(sum(row) == 0 for row in generator_core)
                and min(generator_core[i][j] for i, j in product(range(3), repeat=2) if i != j) > 0
                and h.mm([law], generator_core) == [[F(0)]*3],
                'Each logarithmic generator core is a strict stationary CTMC generator')
    visible_basis = [[F(1), F(s)] for s in signs]
    low_core = [[low_reset[i][j]-identity[i][j] for j in range(3)] for i in range(3)]
    require(h.mm(low_core, visible_basis) == h.mm(visible_basis, [[0, 0], [0, -1]]),
            'The low generator is strongly lumpable for the binary readout at every measurement spacing')
    branches = {}
    for recorded in (-1, 1):
        matrix = []
        for state in range(3):
            if state == 0:
                matrix.append([1-p if recorded == -1 else p, F(0), F(0)])
            else:
                error = recorded == -1
                probability = p if error else 1-p
                zeta = [F(1), F(0)] if error else [(F(1, 2)-p)/(1-p), F(1, 2)/(1-p)]
                matrix.append([F(0), probability*zeta[0], probability*zeta[1]])
        branches[recorded] = matrix
    nonselective = [[sum(branches[y][i][j] for y in (-1, 1)) for j in range(3)] for i in range(3)]
    require(all(sum(row) == 1 and min(row) >= 0 for row in nonselective)
            and h.mm([pi], nonselective) == [pi]
            and all(nonselective[i][j] == 0 for i, j in product(range(3), repeat=2) if signs[i] != signs[j]),
            'The correlated-error instrument preserves the readout and nonselective equilibrium exactly')
    for y, matrix in branches.items():
        for s in (-1, 1):
            sector = [[F(label == s)] for label in signs]
            probability = 1-p if y == s else p
            require(h.mm(matrix, sector) == [[probability*x[0]] for x in sector],
                    'Each readout branch has the sector eigenvector identity proving every finite repeated-readout word has the iid BSC law')
    joint = {y: h.mm([pi], branches[y])[0] for y in (-1, 1)}
    reference = {y: [pi[i]*(1-p if signs[i] == y else p) for i in range(3)] for y in (-1, 1)}
    joint_tv = sum(total_variation(joint[y], reference[y]) for y in (-1, 1))
    require([joint[y] for y in (-1, 1)] == [[F(99, 200), F(1, 200), F(0)], [F(1, 200), F(49, 200), F(1, 4)]]
            and [reference[y] for y in (-1, 1)] == [[F(99, 200), F(1, 400), F(1, 400)], [F(1, 200), F(99, 400), F(99, 400)]]
            and joint_tv == F(1, 200),
            'The equilibrium record/postmeasurement-state joint law nevertheless differs from the independent-error reference')
    def table(rows, kernel):
        return [sum(h.mm([rows[y]], kernel)[0][i] for i in range(3) if signs[i] == final)
                for y, final in product((-1, 1), repeat=2)]
    table_reports = []
    expected_tables = [([1724, 3076, 1036, 3764], [1723, 3077, 1037, 3763]),
                       ([2234, 2566, 1546, 3254], [2233, 2567, 1547, 3253])]
    half_branches = {y: [[(matrix[i][j]+F(i == j)*(1-p if signs[i] == y else p))/2
                          for j in range(3)] for i in range(3)] for y, matrix in branches.items()}
    half_joint = {y: h.mm([pi], matrix)[0] for y, matrix in half_branches.items()}
    half_nonselective = [[sum(half_branches[y][i][j] for y in (-1, 1)) for j in range(3)] for i in range(3)]
    require(h.mm([pi], half_nonselective) == [pi]
            and all(sum(matrix[i]) == (1-p if signs[i] == y else p)
                    for y, matrix in half_branches.items() for i in range(3))
            and sum(total_variation(half_joint[y], reference[y]) for y in (-1, 1)) == F(1, 400),
            'The finite half-reset instrument halves the joint record/state discrepancy')
    for index, (first, second) in enumerate(((low_kernel, high_kernel), (high_kernel, low_kernel))):
        kernel = h.mm(first, second)
        actual, ideal = table(joint, kernel), table(reference, kernel)
        require(actual == [F(x, 9600) for x in expected_tables[index][0]]
                and ideal == [F(x, 9600) for x in expected_tables[index][1]]
                and total_variation(actual, ideal) == F(1, 4800)
                and actual[0]+actual[2] == ideal[0]+ideal[2]
                and actual[1]+actual[3] == ideal[1]+ideal[3],
                'Both physical words reveal a joint-table discrepancy despite exact endpoint agreement')
        require(total_variation(table(half_joint, kernel), ideal) == F(1, 9600) > F(1, 100000),
                'The finite-time conditional kick retains a joint-table error above the old instrument allowance')
        table_reports.append({'actual_joint_table_exact': list(map(str, actual)),
                              'independent_error_reference_table_exact': list(map(str, ideal)),
                              'joint_table_TV_exact': '1/4800'})
    # Positive endpoint-to-joint identity under error-independent backaction.
    d12, d21, n0, n1, err, fzero, fone, ftwo = [h.Poly.variable(8, i) for i in range(8)]
    D = [[1, 0, 0], [0, 1-d12, d12], [0, d21, 1-d21]]
    nu = [n0, n1, 1-n0-n1]
    future = [[1-fzero, fzero], [1-fone, fone], [1-ftwo, ftwo]]
    endpoint_delta = h.mm([[x-y for x, y in zip(h.mm([nu], D)[0], nu)]], future)[0]
    for recorded in (-1, 1):
        before = [nu[i]*(1-err if signs[i] == recorded else err) for i in range(3)]
        after = h.mm([before], D)[0]
        difference = h.mm([[x-y for x, y in zip(after, before)]], future)[0]
        probability = 1-err if recorded == 1 else err
        require(difference == [probability*x for x in endpoint_delta],
                'Every initial-record branch disturbance factors into a nonnegative electronic probability times the endpoint disturbance')
    initial = [F(1, 2), F(1, 8), F(3, 8)]
    positive_before = {y: [initial[i]*(1-p if signs[i] == y else p) for i in range(3)] for y in (-1, 1)}
    positive_after = {y: h.mm([positive_before[y]], nonselective)[0] for y in (-1, 1)}
    before_table, after_table = table(positive_before, high_kernel), table(positive_after, high_kernel)
    positive_joint_tv = total_variation(before_table, after_table)
    positive_endpoint_tv = total_variation([before_table[0]+before_table[2], before_table[1]+before_table[3]],
                                          [after_table[0]+after_table[2], after_table[1]+after_table[3]])
    require(positive_joint_tv == positive_endpoint_tv == F(1, 96),
            'An explicit nonstationary preparation illustrates equality of endpoint and initial/final disturbance under independent electronic errors')
    leaky = [[F(99, 100)*nonselective[i][j]+pi[j]/100 for j in range(3)] for i in range(3)]
    repaired = [row[:] for row in leaky]
    leakage = F(0)
    for i, j in product(range(3), repeat=2):
        if signs[i] != signs[j]:
            leakage += initial[i]*leaky[i][j]
            repaired[i][i] += repaired[i][j]
            repaired[i][j] = F(0)
    leaky_rows = {y: h.mm([positive_before[y]], leaky)[0] for y in (-1, 1)}
    repaired_rows = {y: h.mm([positive_before[y]], repaired)[0] for y in (-1, 1)}
    leaky_table, repaired_table = table(leaky_rows, high_kernel), table(repaired_rows, high_kernel)
    endpoint = lambda values: [values[0]+values[2], values[1]+values[3]]
    require(leakage == F(1, 200)
            and total_variation(leaky_table, repaired_table) <= leakage
            and total_variation(endpoint(leaky_table), endpoint(repaired_table)) <= leakage
            and total_variation(repaired_table, before_table) == total_variation(endpoint(repaired_table), endpoint(before_table))
            and total_variation(leaky_table, before_table) <= total_variation(endpoint(leaky_table), endpoint(before_table))+2*leakage,
            'An explicit sector-repair fixture checks both coupling charges in the endpoint-plus-two-leakage bound')
    return {'stationary_laws_exact': [list(map(str, law)) for law in (pi, high)],
            'low_kernel_exact': [list(map(str, row)) for row in low_kernel],
            'high_kernel_exact': [list(map(str, row)) for row in high_kernel],
            'electronic_error_probability_exact': str(p),
            'nonselective_instrument_exact': [list(map(str, row)) for row in nonselective],
            'joint_record_state_TV_exact': str(joint_tv),
            'finite_half_reset_joint_record_state_TV_exact': '1/400',
            'finite_half_reset_word_joint_table_TV_exact': '1/9600',
            'word_order': ['0H', 'H0'], 'word_joint_table_certificates': table_reports,
            'all_zero_delay_repeat_words_have_iid_BSC_law': True,
            'all_future_endpoint_laws_unchanged_at_equilibrium': True,
            'positive_independent_error_fixture_joint_and_endpoint_TV_exact': str(positive_joint_tv),
            'positive_leakage_repair_fixture_sector_change_probability_exact': str(leakage),
            'scope': 'The negative fixture couples the otherwise fresh electronic error to hidden backaction. It therefore violates error/backaction independence, despite perfect marginal and repeated-readout checks. The positive lemma explicitly assumes this independence and readout-sector preservation.'}


def sampling_cost_certificate(h, constants):
    a, b, c = constants
    widths = [2*(1+a), F(44, 25)*(1+a), 2*a, F(44, 25)*a, 2*(b+c)]
    R = sum(widths)
    probabilities = [width/R for width in widths]
    require(R == F(311165662, 2249775) < 139
            and b == F(940094, 83325) and c == F(15041128, 449955)
            and sum(probabilities) == 1 and min(probabilities) > 0,
            'The fixed type randomization uses positive probabilities and the stated total range bound')
    score_a = [F(2, 5)*y+F(3, 5)*i*y-F(3, 10)*i for i, y in product((-1, 1), repeat=2)]
    score_b = [-F(2, 5)*y-F(12, 25)*i*y+F(3, 10)*i for i, y in product((-1, 1), repeat=2)]
    require((min(score_a)+max(score_a))/2 == -F(3, 10)
            and (min(score_b)+max(score_b))/2 == F(3, 10),
            'The two score midpoints are opposite and cancel in original and prefixed sums')
    for s, t, v in product((-1, 1), repeat=3):
        coefficients = [1+s*a, 1+s*a, -s*a, -s*a]
        possible = [[coefficient*(score-midpoint)/probabilities[index] for score in scores]
                    for index, (coefficient, scores, midpoint) in enumerate(zip(coefficients,
                        (score_a, score_b, score_a, score_b), (-F(3, 10), F(3, 10), -F(3, 10), F(3, 10))))]
        possible.append([(-t*b*y-v*c*i)/probabilities[4] for i, y in product((-1, 1), repeat=2)])
        require(all(abs(value) <= R/2 for values in possible for value in values),
                'Every outcome of every signed inverse-probability score lies in the common centered range')
    N, precision = 60000000000, F(1, 1000)
    require(2*N*precision**2 == 120000 > 6*139**2,
            'The chosen scalar estimation budget yields a two-sided Hoeffding exponent strictly exceeding six')
    term = total = F(1)
    for order in range(1, 41):
        term *= F(6, order)
        total += term
    require(16/total < F(1, 25)
            and N//5000000 == 12000 and 2*N == 120000000000,
            'The union over eight two-sided scalar estimates has failure below four percent at the explicitly counted cost')
    return {'type_order': ['0H', 'H0', 'K then 0H', 'K then H0', 'K'],
            'type_worst_range_widths_exact': list(map(str, widths)),
            'type_assignment_probabilities_exact': list(map(str, probabilities)),
            'total_range_width_exact': str(R), 'total_range_width_upper_exact': '139',
            'signed_linear_functionals': 8, 'paired_trials': N, 'binary_readouts': 2*N,
            'simultaneous_absolute_scalar_precision_exact': str(precision),
            'simultaneous_failure_probability_upper_exact': '1/25',
            'multiple_of_previous_five_million_trial_count': 12000,
            'scope': 'Only precision of eight scalar correction functionals under randomized type selection after preparation is certified. Observable guards, reference gates, target power, systematic errors, and a complete five-type rejection rule are not certified.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_observable_calibration.json'))
    args = parser.parse_args()
    h, prior = load_inputs()
    lemma, constants = response_lemma_certificate(h)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrices, polynomial identities, and finite concentration arithmetic',
              'observable_preparation_certificate': lemma,
              'readout_boundary_certificate': instrument_certificate(h),
              'scalar_sampling_cost_certificate': sampling_cost_certificate(h, constants),
              'new_five_type_state_count_advantage_claimed': False,
              'previous_five_million_trial_guarantee_transferred': False,
              'previous_approximation_allowance_transferred': False,
              'full_five_type_test_size_or_power_claimed': False,
              'largest_dense_matrix_dimension': 3, 'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': {INPUT: INPUT_SHA}, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**prior['proof_snapshot_sha256'], **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 3, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
