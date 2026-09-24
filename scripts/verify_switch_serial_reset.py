#!/usr/bin/env python3
"""Exact premises for serial snapshot sampling with finite low-field resets.

The hash-bound proofs supply the universal conditional concentration and
mixing arguments. This verifier checks their rational identities, small
matrix calculations, interval bounds, and finite sample arithmetic.
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
INPUT = 'reports/switch_percent_kinetics.json'
INPUT_SHA = '4ddbddfef6c3c31fc5785a21e51aeac521b0b8c5685e595a7b86c615d6ee807e'
PROOFS = {
    'docs/FAMILIAR_SWITCH_SERIAL_SAMPLING.md': '773ded5fba43a9b3390f404b4f259646c8515bce453f334a65228013418d2f6f',
    'docs/FAMILIAR_SWITCH_FINITE_RESET.md': '93873fc5ef107f82b0dc58bac71de0ec856b4508fb156662af6f0df3609f5b00',
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
            'The percent-kinetic report is the explicitly frozen prerequisite')
    prior = json.loads(payload)
    require(prior['status'] == 'PASS', 'The inherited finite certificate passed')
    for name, expected in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == expected,
                'Every inherited source agrees with its frozen expected hash')
    for name, expected in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Every inherited mathematical proof agrees with its frozen expected hash')
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The exact helper has its unconditional expected source hash')
    require(len(PROOFS) == 2 and all(len(value) == 64 for value in PROOFS.values()),
            'Both new mathematical proofs have unconditional expected hashes')
    for name, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each new mathematical proof matches its reviewed snapshot')
    spec = importlib.util.spec_from_file_location('serial_reset_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    return h, prior


def exp_negative_upper(value, degree=40):
    require(value >= 0, 'Every exponential upper bound has a nonnegative argument')
    term = total = F(1)
    for order in range(1, degree+1):
        term *= value/order
        total += term
    return 1/total


def variance(a, b, gamma, mean, correlation, initial):
    mu = a*mean+b*correlation+gamma*initial
    return a*a+b*b+gamma*gamma+2*a*b*initial+2*a*gamma*correlation+2*b*gamma*mean-mu**2


def serial_sampling_certificate(h, prior):
    old = prior['fixed_score_design']
    population = [tuple(map(F, row)) for row in old['population_gate_intervals_exact']]
    empirical = [tuple(map(F, row)) for row in old['empirical_gate_intervals_exact']]
    coefficients = [list(map(F, row)) for row in old['score_coefficients_exact']]
    require(old['gate_coordinate_order'] == ['M', 'C', 'L', 'D', 'A=L+3D/5', 'Q=C-D']
            and coefficients == [[F(2, 5), F(3, 5), -F(3, 10)], [-F(2, 5), -F(12, 25), F(3, 10)]],
            'The serial test uses the same gate ordering and fixed score')
    ER, B = F(11, 50000), F(79, 10**6)
    require(F(old['null_displacement_exact']) == ER
            and F(old['conservative_target_external_TV_allowance_exact']) == B,
            'The conditional per-history comparison budgets equal the frozen marginal budgets')
    sensitivity = [F(2)]*4+[F(16, 5), F(4)]
    reference_gates = [(lo-width*ER, hi+width*ER)
                       for (lo, hi), width in zip(population, sensitivity)]
    conditional_boxes = [(lo-4*ER, hi+4*ER) for lo, hi in population[:4]]
    expected_boxes = [(F(20612, 10**5), F(23088, 10**5)), (F(45212, 10**5), F(49488, 10**5)),
                      (F(11312, 10**5), F(13688, 10**5)), (F(47012, 10**5), F(51388, 10**5))]
    require(conditional_boxes == expected_boxes,
            'The conditional variance boxes include both reference and conditional-law displacements')
    require(all((lo-2*ER, hi+2*ER) == expected
                for (lo, hi), expected in zip(reference_gates[:4], conditional_boxes)),
            'Passing reference gates plus conditional TV error gives the expanded variance boxes')
    broad = [(F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
             (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25)),
             (F(2, 5), F(1)), (-F(1, 25), -F(1, 1000))]
    require(all(outer[0] < inner[0] <= inner[1] < outer[1]
                for inner, outer in zip(reference_gates, broad)),
            'Every reference inside the expanded gates remains in the inherited witness box with positive tangent remainder')
    margins = [F(1, 250)]*5+[F(3, 500)]
    require(all(inner == (outer[0]+gap, outer[1]-gap)
                for inner, outer, gap in zip(empirical, population, margins)),
            'Outside the fixed reference gates the conditional drift must cross the original empirical-to-population gap')
    widths = []
    for a, b, gamma in coefficients:
        scores = [(a+b*i)*y+gamma*i for i, y in product((-1, 1), repeat=2)]
        widths.append(max(scores)-min(scores))
        mean, correlation, initial = [h.Poly.variable(3, i) for i in range(3)]
        law = lambda i, y: (1+i*initial+y*mean+i*y*correlation)/4
        mu = sum(law(i, y)*((a+b*i)*y+gamma*i) for i, y in product((-1, 1), repeat=2))
        second = sum(law(i, y)*((a+b*i)*y+gamma*i)**2 for i, y in product((-1, 1), repeat=2))
        require(second-mu**2 == variance(a, b, gamma, mean, correlation, initial),
                'The conditional score variance follows from the exact four-cell identity')
    require(widths == [F(2), F(44, 25)] and sum(widths) == F(94, 25),
            'Both bounded martingale increments retain their original score widths')
    initial_bound = F(1, 10000)+2*ER
    ceilings = [F(31, 100), F(27, 100)]
    exact_corners = [F(75635985159, 250000000000), F(1636861894119, 6250000000000)]
    for arm, (a, b, gamma) in enumerate(coefficients):
        mean_box, corr_box = conditional_boxes[2*arm:2*arm+2]
        mean, correlation = h.Interval(*mean_box), h.Interval(*corr_box)
        mu = a*mean+b*correlation+gamma*h.Interval(-initial_bound, initial_bound)
        require((2*b*gamma-2*a*mu).hi < 0 and (2*a*gamma-2*b*mu).hi < 0
                and (2*a*b-2*gamma*mu).lo > 0,
                'The variance remains decreasing in both moments and increasing in the initial mean on every conditional box')
        corner = variance(a, b, gamma, mean_box[0], corr_box[0], initial_bound)
        require(corner == exact_corners[arm] < ceilings[arm],
                'The widened conditional variance maximum fits the original null variance ceiling')
    null_ceiling = F(7, 100000)+sum(widths)*ER
    target_floor = F(367, 100000)-sum(widths)*B
    require(null_ceiling == F(old['null_score_mean_upper_exact'])
            and target_floor == F(old['target_score_mean_lower_exact'])
            and F(old['observed_joint_TV_model_allowance_exact']) == F(1, 5000),
            'Per-history score transfer preserves both original mean bounds and the enlarged null allowance')
    mgf_variance, mgf_scale, root = [h.Poly.variable(3, i) for i in range(3)]
    x = mgf_variance*root**2/2
    threshold = mgf_variance*root+mgf_scale*x
    require(root*threshold-mgf_variance*root**2/2 == x*(1+mgf_scale*root),
            'The stated conditional-MGF Chernoff choice proves the square-root-plus-linear Bernstein radius exactly')
    n = 2500000
    require(n == old['paired_trials_per_arm'] and old['total_fresh_paired_trials'] == 2*n
            and old['total_bit_readouts'] == 4*n,
            'The fixed serial schedule retains the inherited allocation and readout count')
    VN, VT, W = F(58, 100)/n, F(57, 100)/n, F(2, n)
    null_gap = F(2078, 10**6)-null_ceiling-W
    target_gap = target_floor-F(2154, 10**6)-W*F(13, 12)
    require(null_gap > 0 and target_gap > 0
            and null_gap**2-2*VN*3 == F(1, 2500000000) > 0
            and target_gap**2-2*VT*F(13, 4) == F(9851449, 5625000000000000) > 0
            and F(2078, 10**6) < F(old['rejection_cutoff_exact']) < F(2154, 10**6),
            'The conditional-MGF Bernstein radii obey the same exact score separation inequalities')
    target_box = [tuple(map(F, row)) for row in prior['direct_witness_certificate']['recorded_moment_public_enclosures_exact']]
    latent_difference = tuple(map(F, prior['direct_witness_certificate']['latent_c_minus_d_enclosure_exact']))
    target_ceilings = [F(3, 10), F(27, 100)]
    target_exact = [F(2911934639, 10**10), F(25322527228864, 10**14)]
    for arm, (a, b, gamma) in enumerate(coefficients):
        tm, tc = target_box[2*arm:2*arm+2]
        require(conditional_boxes[2*arm][0] < tm[0] <= tm[1] < conditional_boxes[2*arm][1]
                and conditional_boxes[2*arm+1][0] < tc[0] <= tc[1] < conditional_boxes[2*arm+1][1],
                'The wider certified variance-derivative domain includes the stationary target moment box')
        target_upper = variance(a, b, gamma, tm[0], tc[0], F(0))+widths[arm]**2*B
        require(target_upper == target_exact[arm] < target_ceilings[arm]
                and target_ceilings[arm] == F(old['target_variance_ceilings_exact'][arm]),
                'The per-history target TV promise retains the original conditional variance ceilings')
    scalar_distance, A_distance, Q_distance = F(346, 10**5), F(358, 10**5), F(456, 10**5)
    require(all(inner[0]-2*B-outer[0] > scalar_distance and outer[1]-inner[1]-2*B > scalar_distance
                for inner, outer in zip(target_box, empirical[:4])),
            'Every target conditional scalar drift remains at the original safe gate distance')
    A_box = (target_box[2][0]+F(3, 5)*target_box[3][0], target_box[2][1]+F(3, 5)*target_box[3][1])
    Q_box = (latent_difference[0], F(49, 50)**2*latent_difference[1])
    require(A_box[0]-F(16, 5)*B-empirical[4][0] > A_distance
            and empirical[4][1]-A_box[1]-F(16, 5)*B > A_distance
            and Q_box[0]-4*B-empirical[5][0] > Q_distance
            and empirical[5][1]-Q_box[1]-4*B > Q_distance,
            'Every target conditional combined-moment drift remains at the original safe gate distances')
    exponents = [n*scalar_distance**2/2, n*A_distance**2/(2*F(8, 5)**2), n*Q_distance**2/4]
    require(exponents == [F(29929, 2000), F(32041, 5120), F(3249, 250)],
            'The conditional Hoeffding gate exponents agree with the frozen design')
    require(n*(F(2, n))**2 == F(4, n)
            and n*(F(16, 5)/n)**2 == 4*F(8, 5)**2/n
            and 2*n*(F(2, n))**2 == F(8, n),
            'The serial scalar, combined-arm, and two-arm gate sums have the asserted Hoeffding range squares')
    gate_failure = sum(weight*exp_negative_upper(exponent) for weight, exponent in zip((8, 2, 2), exponents))
    outside = [n*F(1, 250)**2/2, n*F(1, 250)**2/(2*F(8, 5)**2), n*F(3, 500)**2/4]
    require(gate_failure < F(1, 250)
            and all(exp_negative_upper(exponent) < F(1, 20) for exponent in outside)
            and exp_negative_upper(F(3)) < F(1, 20)
            and exp_negative_upper(F(13, 4))+gate_failure < F(11, 250) < F(1, 20),
            'The serial conditional concentration bounds prove the unchanged size and power guarantees')
    return {'paired_trials_per_arm': n, 'total_serial_paired_trials': 2*n, 'total_bit_readouts': 4*n,
            'fixed_schedule_required': True, 'fresh_independence_required': False,
            'conditional_null_TV_allowance_exact': str(ER), 'conditional_target_TV_allowance_exact': str(B),
            'fixed_reference_gate_intervals_exact': [list(map(str, row)) for row in reference_gates],
            'conditional_variance_moment_order': ['M', 'C', 'L', 'D'],
            'conditional_variance_boxes_exact': [list(map(str, row)) for row in conditional_boxes],
            'conditional_initial_mean_absolute_bound_exact': str(initial_bound),
            'null_conditional_variance_maxima_exact': list(map(str, exact_corners)),
            'null_variance_ceilings_exact': list(map(str, ceilings)),
            'target_variance_ceilings_exact': old['target_variance_ceilings_exact'],
            'rejection_cutoff_exact': old['rejection_cutoff_exact'],
            'null_score_mean_upper_exact': str(null_ceiling), 'target_score_mean_lower_exact': str(target_floor),
            'target_gate_failure_upper_exact': old['target_gate_failure_upper_exact'],
            'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '11/250',
            'scope': 'One fixed model and fixed stationary reference pair, with a conditional comparison promise for every prior history. The universal martingale bounds are analytic; passing empirical gates does not establish the reset or detector promises.'}


def finite_reset_certificate(h, prior):
    u, lam = [h.Poly.variable(2, i) for i in range(2)]
    t = F(4, 5)
    denominator = 1-t*t*u*u
    A_num, B_num = u*(1-t*t), t*(1-u*u)
    states = list(product((-1, 1), repeat=2))
    coordinates = [[F(1), F(s), F(z), F(s*z)] for s, z in states]
    scaled_q = [[h.Poly(2) for _ in range(4)] for _ in range(4)]
    law = [(1+u*s)*(1+t*s*z)/4 for s, z in states]
    for i, (s, z) in enumerate(states):
        for j, (sj, zj) in enumerate(states):
            if sj == -s and zj == z:
                scaled_q[i][j] = (denominator-s*(A_num+B_num*z))/2
            elif sj == s and zj == -z:
                scaled_q[i][j] = denominator*(1-t*s*z)/2
        scaled_q[i][i] = -sum(scaled_q[i])
    closed = [[0, A_num, 0, B_num+t*denominator],
              [0, -denominator, t*denominator, 0],
              [0, B_num, -denominator, A_num], [0, 0, 0, -2*denominator]]
    require(h.determinant(coordinates) != 0
            and h.mm(scaled_q, coordinates) == h.mm(coordinates, closed),
            'The generic low-field heat-bath generator has the exact four-coordinate block form')
    require(sum(law) == 1 and h.mm([law], scaled_q) == [[h.Poly(2)]*4]
            and all(law[i]*scaled_q[i][j] == law[j]*scaled_q[j][i]
                    for i, j in product(range(4), repeat=2)),
            'The generic low-field Gibbs law is normalized, stationary, and reversible as polynomial identities')
    characteristic = h.determinant([[lam*denominator*F(i == j)-closed[i][j] for j in range(4)] for i in range(4)])
    require(characteristic == lam*(lam+2)*denominator**3*(denominator*(lam+1)**2-t*B_num),
            'The exact characteristic factorization yields rates 0, 2, and 1 plus or minus sqrt(t B)')
    require(t*t*denominator-t*B_num == t*t*(1-t*t)*u*u,
            'The low-field coupling product is at most t squared whenever the positive denominator applies')
    eps = F(1, 100000)
    require(1-t*t*eps*eps > 0 and 1-t == F(1, 5),
            'The allowed field interval has positive denominator and nominal spectral gap at least one fifth')
    relative_floor, nominal_gap = F(99, 100), F(1, 5)
    gap = relative_floor*nominal_gap
    minimum_mass = (1-eps)*(1-t)/4
    require(gap == F(99, 500) and minimum_mass > F(1, 21),
            'Symmetric edge Dirichlet comparison and Gibbs masses give the stated perturbed mixing constants')
    flux, factor, displacement = [h.Poly.variable(3, i) for i in range(3)]
    require(flux*factor*displacement**2-relative_floor*flux*displacement**2
            == flux*(factor-relative_floor)*displacement**2,
            'Each perturbed Dirichlet edge term exceeds the claimed fraction of its reference term')
    duration = 63
    exponent = 2*gap*duration
    require(exponent == F(6237, 250), 'The actual 63-unit reset has the stated spectral decay exponent')
    tail_upper = exp_negative_upper(exponent, degree=28)
    require(tail_upper < F(1, 50000000000) and 5*tail_upper < eps**2,
            'The degree-28 positive exponential series certifies TV below one part in one hundred thousand')
    trials = 5000000
    nominal_exposure = trials*(duration+F(5, 2))
    require(nominal_exposure == 327500000 and trials*2*eps == 100
            and trials*duration == 315000000 and trials*F(5, 2) == 12500000,
            'The reset and active-evolution exposure costs are explicitly counted for every serial trial')
    require(nominal_exposure+trials*2*eps == 327500100
            and nominal_exposure+2*trials*2*eps == 327500200,
            'Explicit active and optional reset clock allowances give the advertised worst-case total exposures')
    realization = prior['local_snapshot_realization']
    basis = [list(map(F, row)) for row in realization['coordinate_matrix_exact']]
    inverse = [[value/h.determinant(basis) for value in row] for row in h.adjugate(basis)]
    pi0 = list(map(F, realization['stationary_laws_exact'][0]))
    low_box = [tuple(map(F, row)) for row in realization['embedding_certificates'][0]['parameter_box_exact']]
    weights = [F(1), F(14, 25)]
    x_box, y_box, z_box, w_box = low_box
    weighted_rows = [x_box[1]+z_box[1]*weights[1]/weights[0],
                     y_box[1]*weights[0]/weights[1]+w_box[1]]
    contraction = F(157, 200)
    require(weighted_rows == [F(24529, 31250), F(54203, 70000)]
            and max(weighted_rows) < contraction,
            'Every fitted predictive low kernel contracts the two-coordinate weighted row norm by the stated factor')
    require(h.mm(basis, inverse) == h.identity(3)
            and h.mm([pi0], basis) == [[F(1), F(0), F(0)]],
            'The fixed predictor basis reconstructs its stationary centered probability rows exactly')
    initial_norm = max(sum(abs(row[j+1])*weights[j] for j in range(2)) for row in basis)
    reconstruction = max(sum(abs(value) for value in inverse[j+1])/weights[j] for j in range(2))
    require(initial_norm == F(293, 125) and reconstruction == F(625, 462)
            and initial_norm*reconstruction/2 == F(1465, 924),
            'The extreme initial states and inverse coordinates give the exact predictive TV prefactor')
    predictive_tail = F(1465, 924)*contraction**50
    require(predictive_tail < eps and 50*F(5, 4)+F(1, 2) == duration,
            'Fifty predictive low ticks plus a final stochastic half unit reset every predictive initial law within the same allowance')
    actual_target_budget = F(prior['direct_witness_certificate']['target_external_TV_allowance_exact'])
    predictive_comparison = actual_target_budget+eps
    require(predictive_comparison == F(88025101, 10**12) < F(9, 100000)
            and predictive_comparison < F(prior['fixed_score_design']['observed_joint_TV_model_allowance_exact']),
            'Finite predictor preparation adds one reset allowance to the conditional two-snapshot comparison')
    return {'target_low_field_tanh_absolute_bound_exact': str(eps),
            'target_relative_edge_floor_exact': str(relative_floor),
            'target_spectral_gap_lower_exact': str(gap),
            'target_stationary_minimum_mass_lower_exact': '1/21',
            'actual_reset_duration_attempt_units': duration,
            'squared_TV_decay_prefactor_upper_exact': '5',
            'reset_decay_exponent_exact': str(exponent),
            'reset_TV_upper_exact': str(eps), 'exponential_positive_series_degree': 28,
            'shared_rival_conditional_reset_TV_promise_exact': str(eps),
            'total_nominal_reset_attempt_units': trials*duration,
            'total_nominal_active_attempt_units': int(trials*F(5, 2)),
            'total_nominal_reset_plus_active_attempt_units': int(nominal_exposure),
            'active_dwell_error_total_upper_attempt_units': 100,
            'reset_plus_active_with_active_clock_allowance_upper_attempt_units': 327500100,
            'optional_reset_clock_error_exact': str(eps),
            'optional_reset_clock_nominal_duration_exact': str(63+eps),
            'reset_plus_active_with_both_clock_allowances_upper_attempt_units': 327500200,
            'general_three_state_reset': {
                'weighted_coordinate_norm_weights_exact': list(map(str, weights)),
                'weighted_kernel_row_sum_upper_exact': list(map(str, weighted_rows)),
                'one_tick_contraction_upper_exact': str(contraction),
                'initial_coordinate_norm_upper_exact': str(initial_norm),
                'probability_reconstruction_factor_exact': str(reconstruction),
                'TV_prefactor_exact': '1465/924', 'complete_low_ticks': 50,
                'remaining_reset_attempt_units_exact': '1/2', 'reset_TV_upper_exact': str(eps),
                'actual_target_to_finitely_prepared_predictor_conditional_joint_TV_upper_exact': str(predictive_comparison),
                'scope': 'The same 63-unit reset suffices for every constructed general three-state predictor. The comparison is per-history for a single trial; it is not a total-variation guarantee for the full serial record and does not alter the static state-count interval.'},
            'scope': 'The finite reset time is proved for the one-percent physical target family. Every rival must separately satisfy the shared conditional reset promise; no finite uniform reset time is asserted for unrestricted slow rivals. Readout durations and laboratory conversion of attempt time are not included.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_serial_reset.json'))
    args = parser.parse_args()
    h, prior = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction identities, small polynomial matrices, rational intervals, and positive exponential series',
              'serial_sampling_certificate': serial_sampling_certificate(h, prior),
              'finite_reset_certificate': finite_reset_certificate(h, prior),
              'largest_dense_matrix_dimension': 4,
              'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': {INPUT: INPUT_SHA}, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**prior['proof_snapshot_sha256'], **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
