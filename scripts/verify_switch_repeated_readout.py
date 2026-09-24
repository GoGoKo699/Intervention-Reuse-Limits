#!/usr/bin/env python3
"""Exact certificates for seven-readout majority with outcome-correlated kicks.

The hash-bound proof carries the universal stochastic-instrument and serial
testing statements. These finite checks use rational arithmetic, a polynomial
identity, and exact three-state instrument enumeration. No hidden-state
independence is inferred from the observed disagreement gate.
"""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from math import comb
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    'reports/switch_serial_reset.json': '9c9f662e63d94d518d3e01bf0aa179dffa6f06d78a2333660e3668582d972fb6',
    'reports/switch_observable_calibration.json': '5883635e5d44264c9cc72ba585f16aa65b2441837ef3cf4d69e54ba3b878ae1c',
}
PROOFS = {
    'docs/FAMILIAR_SWITCH_REPEATED_READOUT.md': '4c9b6a873005f7a0798e99d3edededd7a39607d1c85252221b1e692af13d1182',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    reports, inherited_proofs = {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected,
                'Each prerequisite report matches its unconditional frozen hash')
        report = json.loads(payload)
        require(report['status'] == 'PASS', 'Each frozen prerequisite has status PASS')
        for source, digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Each inherited verifier source matches its frozen report binding')
        for proof, digest in report['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/proof).read_bytes()).hexdigest() == digest,
                    'Each inherited proof matches its frozen report binding')
            require(proof not in inherited_proofs or inherited_proofs[proof] == digest,
                    'Overlapping inherited proof bindings agree')
            inherited_proofs[proof] = digest
        for predecessor, digest in report.get('input_report_sha256', {}).items():
            require(hashlib.sha256((ROOT/predecessor).read_bytes()).hexdigest() == digest,
                    'Each immediate inherited report input retains its frozen binding')
        reports[name] = report
    require(len(PROOFS) == 1 and all(len(value) == 64 for value in PROOFS.values()),
            'The new universal proof has an unconditional reviewed snapshot hash')
    for name, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'The repeated-readout proof matches its reviewed snapshot')
    return reports, inherited_proofs


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def total_variation(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))/2


def majority_tail(p, reads=7):
    return sum(F(comb(reads, k))*p**k*(1-p)**(reads-k)
               for k in range(reads//2+1, reads+1))


def exp_negative_upper(x, degree=20):
    """Positive Taylor partial sum gives an exact strict upper for exp(-x)."""
    require(x > 0 and degree >= 1, 'The exponential comparison uses a positive exponent')
    term = total = F(1)
    for order in range(1, degree+1):
        term *= x/order
        total += term
    return 1/total


def majority_polynomial_certificate():
    coefficients = [F(0)]*8
    for k in range(4, 8):
        for j in range(8-k):
            coefficients[k+j] += comb(7, k)*comb(7-k, j)*(-1)**j
    require(coefficients == [0, 0, 0, 0, 35, -84, 70, -20],
            'The seven-readout binomial tail has the exact expanded polynomial')
    derivative = [i*coefficients[i] for i in range(1, 8)]
    factored_derivative = [F(0)]*7
    for j in range(4):
        factored_derivative[3+j] = 140*comb(3, j)*(-1)**j
    require(derivative == factored_derivative,
            'The derivative equals 140 p^3 (1-p)^3 and is nonnegative on the probability interval')
    ceiling, target = majority_tail(F(1, 50)), majority_tail(F(1, 100))
    require(ceiling == F(26053, 4882812500) < F(1, 100000)
            and target == F(1708349, 5000000000000) < ceiling,
            'The two-percent and one-percent majority tails fit inside the inherited instrument allowance')
    five_tail, margin = majority_tail(F(1, 100), 5), F(1, 100000)-ceiling
    require(five_tail == F(49253, 5000000000) < F(1, 100000)
            and margin == F(46643456, 10**13) > 0,
            'The five-read comparison and unused whole-block defect margin have the stated exact values')
    require(majority_tail(F(0)) == 0 and majority_tail(F(1, 2)) == F(1, 2),
            'The majority polynomial has the correct noiseless and uninformative endpoints')
    return {'block_length': 7, 'majority_error_threshold': 4,
            'tail_polynomial_coefficients_ascending_exact': list(map(str, coefficients)),
            'derivative_factorization': '140*p^3*(1-p)^3',
            'two_percent_error_tail_exact': str(ceiling),
            'one_percent_error_tail_exact': str(target),
            'five_read_one_percent_error_tail_exact': str(five_tail),
            'remaining_whole_block_defect_margin_exact': str(margin),
            'inherited_joint_instrument_allowance_exact': '1/100000'}


def disagreement_and_sampling_certificate(prior):
    old = prior['serial_sampling_certificate']
    trials, threshold = 5000000, F(3, 100)
    q = lambda p: 2*p*(1-p)
    null_boundary, target_boundary = q(F(1, 50)), q(F(1, 100))
    require(null_boundary == F(49, 1250) and target_boundary == F(99, 5000)
            and target_boundary < threshold < null_boundary,
            'The disagreement gate separates one-percent target noise from the two-percent null boundary')
    # q(v)-q(u)=2(v-u)(1-u-v), nonnegative for 0<=u<=v<=1/2.
    q_coefficients = [F(0), F(2), F(-2)]
    require([q_coefficients[1], 2*q_coefficients[2]] == [2, -4],
            'The disagreement derivative is 2-4p, nonnegative throughout the admissible half interval')
    null_exponent = 2*trials*(null_boundary-threshold)**2
    target_exponent = 2*trials*(threshold-target_boundary)**2
    require(null_exponent == F(4232, 5) and target_exponent == F(5202, 5),
            'Five million first-pair disagreement samples give the claimed exact one-sided exponents')
    null_gate_upper = exp_negative_upper(null_exponent)
    target_gate_upper = exp_negative_upper(target_exponent)
    old_null_upper = exp_negative_upper(F(3))
    require(max(old_null_upper, null_gate_upper) < F(1, 20),
            'The disjoint small-noise and large-noise null cases each have rejection probability below five percent')
    old_miss_upper = F(old['type_II_error_upper_exact'])
    require(old_miss_upper == F(11, 250)
            and old_miss_upper+target_gate_upper < F(1, 20),
            'The inherited target miss bound plus disagreement-gate failure is below five percent without assuming independence')
    slack = F(1, 50000)
    shifted_null_exponent = 2*trials*(null_boundary-threshold-slack)**2
    shifted_target_exponent = 2*trials*(threshold-target_boundary-slack)**2
    require(F(1, 100000)+F(1, 100000)-majority_tail(F(1, 50)) < slack
            and 0 < slack < null_boundary-threshold < threshold-target_boundary,
            'The preparation plus remaining whole-block defect is strictly below the conservative calibration slack')
    require(shifted_null_exponent == F(210681, 250) > 840
            and shifted_target_exponent == F(259081, 250) > 1030,
            'The imperfect-block calibration slack retains the stated strong one-sided exponents')
    require(max(old_null_upper, exp_negative_upper(shifted_null_exponent)) < F(1, 20)
            and old_miss_upper+exp_negative_upper(shifted_target_exponent) < F(1, 20),
            'Both size and power remain valid for the conservatively shifted disagreement gate')
    require(old['total_serial_paired_trials'] == trials
            and old['paired_trials_per_arm'] == trials//2
            and F(old['rejection_cutoff_exact']) == F(21, 10000)
            and F(old['conditional_null_TV_allowance_exact']) == F(11, 50000)
            and F(old['conditional_target_TV_allowance_exact']) == F(79, 1000000),
            'The inherited serial design, score threshold and conditional-TV budgets remain the frozen values')
    require(7*trials == 35000000 and 8*trials == 40000000
            and 8*trials == 4*old['total_bit_readouts'],
            'Seven initial readings plus one final reading cost forty million raw bits, four times the former count')
    return {'total_serial_trials': trials, 'paired_trials_per_arm': trials//2,
            'disagreement_observable': 'First two initial readings differ',
            'disagreement_acceptance_threshold_exact': str(threshold),
            'two_percent_disagreement_exact': str(null_boundary),
            'one_percent_disagreement_exact': str(target_boundary),
            'large_noise_null_gate_exponent_exact': str(null_exponent),
            'target_gate_failure_exponent_exact': str(target_exponent),
            'conservative_imperfect_block_calibration_slack_exact': str(slack),
            'shifted_large_noise_null_gate_exponent_exact': str(shifted_null_exponent),
            'shifted_target_gate_failure_exponent_exact': str(shifted_target_exponent),
            'old_small_noise_null_exponent': 3,
            'null_rejection_upper_rational': str(max(old_null_upper, null_gate_upper)),
            'target_miss_upper_rational': str(old_miss_upper+target_gate_upper),
            'old_score_rejection_cutoff_exact': old['rejection_cutoff_exact'],
            'conditional_null_TV_allowance_exact': old['conditional_null_TV_allowance_exact'],
            'conditional_target_TV_allowance_exact': old['conditional_target_TV_allowance_exact'],
            'initial_raw_bit_readouts': 7*trials, 'total_raw_bit_readouts': 8*trials,
            'scope': 'Fixed instrument with state-independent fresh per-use error p in [0,1/2], sector preservation and nonselective stationarity; fixed-reference conditional preparation and the old independent final detector remain premises. The gate is analyzed jointly with the score by case splitting and a union bound, not by conditioning on gate acceptance.'}


def correlated_instrument_certificate():
    pi, signs, p = [F(1, 2), F(1, 4), F(1, 4)], [-1, 1, 1], F(1, 100)
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    branches = {
        0: [[1-p, 0, 0], [0, F(1, 2)-p, F(1, 2)], [0, F(1, 2)-p, F(1, 2)]],
        1: [[p, 0, 0], [0, p, 0], [0, p, 0]],
    }
    nonselective = [[sum(branches[e][i][j] for e in (0, 1)) for j in range(3)] for i in range(3)]
    require(nonselective == [[1, 0, 0], [0, F(1, 2), F(1, 2)], [0, F(1, 2), F(1, 2)]]
            and mm([pi], nonselective) == [pi],
            'The old outcome-correlated hidden reset is nonselectively stationary')
    require(all(min(row) >= 0 and sum(row) == (p if error else 1-p)
                for error, matrix in branches.items() for row in matrix)
            and all(branches[e][i][j] == 0 for e in (0, 1)
                    for i, j in product(range(3), repeat=2) if signs[i] != signs[j]),
            'Every branch has the state-independent error probability and preserves the visible sector')
    require(branches[1][1][1] != p*nonselective[1][1],
            'The hidden update is explicitly correlated with the electronic error')
    distribution = {(0, state): pi[state] for state in range(3)}
    for step in range(1, 8):
        advanced = {}
        for (errors, state), mass in distribution.items():
            for error, matrix in branches.items():
                for final, probability in enumerate(matrix[state]):
                    key = (errors+error, final)
                    advanced[key] = advanced.get(key, F(0))+mass*probability
        distribution = advanced
        require([sum(mass for (errors, state), mass in distribution.items() if state == j)
                 for j in range(3)] == pi,
                'Each successive nonselective reading preserves the full equilibrium law')
        require(all(sum(mass for (errors, state), mass in distribution.items() if errors == k)
                    == comb(step, k)*p**k*(1-p)**(step-k) for k in range(step+1)),
                'Exact error-count/state enumeration gives the fresh binomial marginal at every block prefix')
    joint = {recorded: [F(0)]*3 for recorded in (-1, 1)}
    for (errors, state), mass in distribution.items():
        recorded = signs[state]*(-1 if errors >= 4 else 1)
        joint[recorded][state] += mass
    perfect = {recorded: [pi[state]*F(signs[state] == recorded) for state in range(3)]
               for recorded in (-1, 1)}
    tail = majority_tail(p)
    independent = {recorded: [pi[state]*(1-tail if signs[state] == recorded else tail) for state in range(3)]
                   for recorded in (-1, 1)}
    joint_tv = sum(total_variation(joint[y], perfect[y]) for y in (-1, 1))
    remaining_dependence = sum(total_variation(joint[y], independent[y]) for y in (-1, 1))
    require(sum(sum(row) for row in joint.values()) == 1
            and [sum(joint[y][state] for y in (-1, 1)) for state in range(3)] == pi
            and joint_tv == tail,
            'The full majority-label/postmeasurement-state TV to perfect nondisturbing readout equals the binomial tail')
    require(0 < remaining_dependence < tail,
            'Majority reduces the joint error without making majority error and hidden backaction independent')
    high = [F(1, 5), F(2, 5), F(2, 5)]
    projection = [[F(1, 3), F(2, 3), F(0)], [F(1, 3), F(2, 3), F(0)], [F(0), F(0), F(1)]]
    low_kernel = [[(identity[i][j]+pi[j])/2 for j in range(3)] for i in range(3)]
    high_kernel = [[identity[i][j]/4+projection[i][j]/4+high[j]/2 for j in range(3)] for i in range(3)]
    require(all(isinstance(value, F) for kernel in (low_kernel, high_kernel) for row in kernel for value in row),
            'Both future fixture clocks contain rational entries exclusively')
    def table(rows, kernel):
        return [sum(mm([rows[y]], kernel)[0][i] for i in range(3) if signs[i] == final)
                for y, final in product((-1, 1), repeat=2)]
    word_reports = []
    for name, first, second in (('0H', low_kernel, high_kernel), ('H0', high_kernel, low_kernel)):
        kernel = mm(first, second)
        actual, ideal = table(joint, kernel), table(perfect, kernel)
        tv = total_variation(actual, ideal)
        require(0 <= tv <= tail < F(1, 100000)
                and actual[0]+actual[2] == ideal[0]+ideal[2]
                and actual[1]+actual[3] == ideal[1]+ideal[3],
                'Each old future word contracts joint majority error and preserves its stationary endpoint marginal')
        word_reports.append({'word': name, 'actual_joint_table_exact': list(map(str, actual)),
                             'perfect_initial_label_table_exact': list(map(str, ideal)),
                             'joint_table_TV_exact': str(tv)})
    return {'per_use_error_exact': str(p), 'instrument_error_branches_exact': {
                str(e): [list(map(str, row)) for row in matrix] for e, matrix in branches.items()},
            'stationary_law_exact': list(map(str, pi)),
            'majority_label_order': [-1, 1],
            'majority_label_poststate_joint_exact': [list(map(str, joint[y])) for y in (-1, 1)],
            'perfect_label_poststate_joint_exact': [list(map(str, perfect[y])) for y in (-1, 1)],
            'joint_majority_state_TV_to_perfect_exact': str(joint_tv),
            'joint_majority_state_TV_to_independent_BSC_exact': str(remaining_dependence),
            'word_certificates': word_reports,
            'scope': 'Exact seven-use enumeration of the previous three-state outcome-correlated instrument. Universal contractivity for arbitrary future channels is proved in the bound note, not established by enumerating these two words.'}


def stationarity_defect_certificate():
    pi, eps = [F(1, 2), F(1, 4), F(1, 4)], F(1, 1000000)
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    first = [[F(1), F(0), F(0)], [F(0), 1-eps, eps], [F(0), F(0), F(1)]]
    second = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), 2*eps, 1-2*eps]]
    kernels = [first, second]+[identity]*5
    law, accumulated = pi, F(0)
    defects = []
    for kernel in kernels:
        defect = total_variation(mm([pi], kernel)[0], pi)
        defects.append(defect)
        accumulated += defect
        law = mm([law], kernel)[0]
        require(total_variation(law, pi) <= accumulated,
                'Each prefix of fixed nonstationary readout operations obeys the telescoping stationary-defect bound')
    require(defects == [eps/4, eps/2]+[F(0)]*5
            and total_variation(law, pi) == eps/4+eps**2/2
            and accumulated == 3*eps/4
            and accumulated+majority_tail(F(1, 50)) < F(1, 100000),
            'The explicit two-kick, seven-read block fits its stationary defect plus majority tail inside the old allowance')
    return {'per_read_stationary_defects_exact': list(map(str, defects)),
            'accumulated_stationary_defect_upper_exact': str(accumulated),
            'actual_final_stationary_defect_exact': str(total_variation(law, pi)),
            'majority_plus_defect_upper_exact': str(accumulated+majority_tail(F(1, 50))),
            'scope': 'Finite fixed-channel illustration of the analytic telescoping bound. The channels are fixed in advance and do not depend on recorded outcomes.'}


def common_mode_counterexample():
    p = F(1, 4)
    histories = [((0,)*7, 1-p), ((1,)*7, p)]
    disagreement = sum(mass for word, mass in histories if word[0] != word[1])
    majority_error = sum(mass for word, mass in histories if sum(word) >= 4)
    require(sum(mass for word, mass in histories) == 1
            and all(sum(mass for word, mass in histories if word[i]) == p for i in range(7))
            and disagreement == 0 and majority_error == p > F(1, 50),
            'A common-mode error has the same per-use marginal but zero disagreement and an unreduced majority error')
    require(sum(mass for word, mass in histories if word[0] == 1 and word[1] == 1) == p != p*p,
            'The common-mode fixture violates the explicitly required conditional freshness premise')
    return {'marginal_per_read_error_exact': str(p),
            'first_pair_disagreement_exact': str(disagreement),
            'majority_error_exact': str(majority_error),
            'scope': 'The disagreement gate alone cannot establish temporal freshness. All seven readings may share a latent common-mode error even with an identity hidden-state instrument.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_repeated_readout.json'))
    args = parser.parse_args()
    prerequisites, inherited_proofs = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction arithmetic, polynomial coefficients, three-state instrument enumeration and positive exponential series',
              'majority_certificate': majority_polynomial_certificate(),
              'disagreement_and_sampling_certificate': disagreement_and_sampling_certificate(prerequisites['reports/switch_serial_reset.json']),
              'correlated_backaction_fixture': correlated_instrument_certificate(),
              'stationarity_defect_fixture': stationarity_defect_certificate(),
              'freshness_counterexample': common_mode_counterexample(),
              'outcome_hidden_update_independence_required': False,
              'per_use_conditional_freshness_required': True,
              'nonselective_stationarity_and_sector_preservation_required': True,
              'rival_preparation_certified_by_disagreement_gate': False,
              'full_raw_record_state_count_minimum_claimed': False,
              'new_device_implementation_claimed': False,
              'largest_dense_matrix_dimension': 3, 'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'input_report_sha256': INPUTS,
              'imported_repository_verifiers': [],
              'proof_snapshot_sha256': {**inherited_proofs, **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 3, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
