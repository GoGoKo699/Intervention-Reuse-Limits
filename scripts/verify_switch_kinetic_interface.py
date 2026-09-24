#!/usr/bin/env python3
"""Exact numerical premises for kinetic tolerance and protected readout.

All computations use rational arithmetic, intervals, or small polynomial
identities. Universal comparison and concentration statements are proved
in the hash-bound notes; no optimization or sample simulation is used.
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
INPUT_REPORT = 'reports/switch_weak_field.json'
INPUT_SHA = '6289576de985afec146faeef47ef504105bc98ca986c6ce8a8bed70dbb2c6a5d'
PROOFS = {
    'docs/FAMILIAR_SWITCH_KINETIC_TOLERANCE.md': 'fb46d03dc616c78035ced22c62b936f1e3a8c91aac86b0587b3803a0e9e8b5bd',
    'docs/FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md': 'fc5db926ee202f479ccbf5436a2a3ae19ce976a43faea2201f8af89d7f4998f3',
    'docs/FAMILIAR_SWITCH_PROTECTED_READOUT.md': '7036d895e2a23dd33105c2ae96ace62904ae86954b0dcfadba18f290be6bd309',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    payload = (ROOT/INPUT_REPORT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_SHA,
            'The inherited weak-field report is the explicitly frozen snapshot')
    prior = json.loads(payload)
    require(prior['status'] == 'PASS', 'The inherited numerical certificate passed')
    for name, expected in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == expected,
                'Each inherited verifier source snapshot remains intact')
    for name, expected in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each inherited mathematical proof snapshot remains intact')
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The rational helper has its unconditional expected source hash')
    require(len(PROOFS) == 3 and all(len(value) == 64 for value in PROOFS.values()),
            'All three new mathematical proofs have unconditional expected hashes')
    for name, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each new mathematical proof matches its reviewed snapshot')
    spec = importlib.util.spec_from_file_location('kinetic_interface_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    centers = list(map(F, prior['nominal_certificate']['moment_centers_exact']))
    eta = F(1, 2**120)
    return h, prior, [h.Interval(c-eta, c+eta) for c in centers], centers


def exp_negative_upper(x):
    require(x >= 0, 'Each exponential tail argument is nonnegative')
    term = total = F(1)
    for index in range(1, 97):
        term *= x/index
        total += term
    return 1/total


def kinetic_certificate(h, prior):
    eps, kappa = F(1, 100000), F(1, 10000)
    bT, bR, gap0 = F(775001, 10**10), F(1, 50000), F(9, 8000)
    inherited = prior['robust_certificate']
    require(F(inherited['target_joint_TV_displacement_exact']) == bT
            and F(inherited['rival_joint_TV_displacement_exact']) == bR
            and F(inherited['separation_certificates'][1]['joint_TV_separation_lower_exact']) == gap0,
            'The kinetic transfer starts from the frozen target, rival, and stationary-gap premises')
    actual_target = bT+kappa
    predictor_upper = 2*eps+kappa
    require(actual_target == F(1775001, 10**10)
            and gap0-actual_target-bR == F(9274999, 10**10) > F(9, 10000)
            and predictor_upper == F(3, 25000) < F(9, 10000),
            'One kinetic charge leaves the advertised population gap and constructive memory interval')
    require((gap0-bT-bR-2*eps)/2 == F(10074999, 20000000000),
            'The exact positive-width condition for the two-sided kinetic error charge is as stated')
    t = F(4, 5)
    maximum_conditional_polarization = (t+t)/(1+t*t)
    exit_bound = (1+t)/2+(1+maximum_conditional_polarization)/2
    require(maximum_conditional_polarization == F(40, 41)
            and exit_bound == F(387, 205) < F(19, 10),
            'The heat-bath rate bound holds at the largest allowed field magnitude')
    duration = F(5, 2)+2*eps
    relative_tolerance = F(1, 50000)
    rate_charge = F(19, 10)*duration*relative_tolerance
    require(rate_charge == F(2375019, 25000000000) < kappa,
            'The stated relative edge-prefactor tolerance fits the integrated kinetic allowance')
    relaxed_tolerance = F(1, 10000)
    relaxed_charge = F(19, 10)*duration*relaxed_tolerance
    require(relaxed_charge == F(2375019, 5000000000)
            and 2*eps+relaxed_charge < F(1, 2000)
            and gap0-bT-bR-relaxed_charge > F(11, 20000),
            'The larger kinetic tolerance retains its stated population-only memory interval')
    flux, factor = [h.Poly.variable(2, i) for i in range(2)]
    require(factor*flux-flux*factor == h.Poly(2),
            'Applying the same edge factor to forward and reverse equilibrium flux preserves detailed balance')
    states = list(product((-1, 1), repeat=2))
    for field in (F(0), F(3, 5)):
        q, law, _ = h.physical_generator(t, field)
        perturbed = [row[:] for row in q]
        for i, j in product(range(4), repeat=2):
            if i != j:
                factor = 1+relative_tolerance*F((min(i, j)+max(i, j)) % 3-1)
                perturbed[i][j] *= factor
        for i in range(4):
            perturbed[i][i] = -sum(perturbed[i][j] for j in range(4) if i != j)
        require(h.mm([law], perturbed) == [[F(0)]*4]
                and all(law[i]*perturbed[i][j] == law[j]*perturbed[j][i] for i, j in product(range(4), repeat=2)),
                'A nonuniform edge-prefactor example retains the exact Gibbs law and detailed balance')
        require(max(sum(abs(perturbed[i][j]-q[i][j]) for j in range(4) if i != j) for i in range(4))
                <= relative_tolerance*exit_bound,
                'The explicit edge-prefactor example obeys the off-diagonal discrepancy bound')
        missing_coordinate = sum(s*z*sum(perturbed[i][j]*states[j][0] for j in range(4))
                                 for i, (s, z) in enumerate(states))/4
        require(missing_coordinate == F(1, 100000),
                'The nonuniform edge example gives Q applied to S a nonzero S-times-Z component, breaking the original affine closure')
    return {'integrated_generator_row_TV_allowance_exact': str(kappa),
            'inherited_target_joint_TV_allowance_exact': str(bT),
            'target_joint_TV_allowance_with_kinetics_exact': str(actual_target),
            'rival_joint_TV_allowance_exact': str(bR),
            'ordinary_joint_TV_separation_lower_exact': '9/10000',
            'general_three_state_joint_TV_upper_exact': str(predictor_upper),
            'state_count_interval_exact': [str(predictor_upper), '9/10000'],
            'relative_symmetric_edge_tolerance_exact': str(relative_tolerance),
            'heat_bath_exit_upper_exact': str(exit_bound),
            'duration_upper_exact': str(duration),
            'relative_edge_integrated_charge_upper_exact': str(rate_charge),
            'nonuniform_edge_example_QS_SZ_coefficient_exact': '1/100000',
            'larger_kinetic_population_only': {
                'relative_symmetric_edge_tolerance_exact': str(relaxed_tolerance),
                'integrated_charge_upper_exact': str(relaxed_charge),
                'state_count_interval_exact': ['1/2000', '11/20000'],
                'sampling_budget_transferred': False},
            'scope': 'The law-transfer and predictor-existence implications are analytic. The kinetic allowance is half the full signed generator-row l1 discrepancy, including its diagonal. The four-state ordinary upper uses a fixed time-homogeneous generator on each field plateau. Symmetric edge factors preserve the Gibbs law; arbitrary rate changes need a separate stationary-law promise.'}


def variance(a, b, gamma, mean, correlation, initial):
    score_mean = a*mean+b*correlation+gamma*initial
    second = a*a+b*b+gamma*gamma+2*a*b*initial+2*a*gamma*correlation+2*b*gamma*mean
    return second-score_mean**2


def score_certificate(h, prior, moments):
    old = prior['fixed_score_designs']
    u, bT, bR, allowance = F(3, 5), F(1775001, 10**10), F(1, 50000), F(1, 5000)
    ER, n, cutoff = bR+allowance, 2500000, F(11, 5000)
    require(allowance >= F(3, 25000),
            'The enlarged ordinary null allowance covers the constructive three-state prediction error')
    weights = [list(map(F, row)) for row in old['score_coefficients_exact']]
    require(weights == [[F(2, 5), F(3, 5), -F(3, 10)], [-F(2, 5), -F(12, 25), F(3, 10)]]
            and F(old['constant_subtracted_exact']) == F(2, 25),
            'The kinetic design retains the fixed weak-field score without refitting')
    ranges = []
    for a, b, g in weights:
        values = [(a+b*i)*y+g*i for i, y in product((-1, 1), repeat=2)]
        ranges.append(max(values)-min(values))
        vm, vc, vi = [h.Poly.variable(3, i) for i in range(3)]
        law = lambda i, y: (1+i*vi+y*vm+i*y*vc)/4
        actual_mean = sum(law(i, y)*((a+b*i)*y+g*i) for i, y in product((-1, 1), repeat=2))
        actual_second = sum(law(i, y)*((a+b*i)*y+g*i)**2 for i, y in product((-1, 1), repeat=2))
        require(actual_mean == a*vm+b*vc+g*vi
                and actual_second-actual_mean**2 == variance(a, b, g, vm, vc, vi),
                'Direct four-cell summation reproduces each score mean and variance polynomial')
    require(ranges == [F(2), F(44, 25)] and sum(ranges) == F(94, 25),
            'The full corrected score retains the asserted range and TV sensitivity')
    lookup = [[50*((a+b*i)*y+g*i) for i, y in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
              for a, b, g in weights]
    require(lookup == [[35, -65, 5, 25], [-29, 59, -11, -19]],
            'The public integer score tables agree with the certified coefficients')
    M, C, L, D = [h.Poly.variable(4, index) for index in range(4)]
    T = F(2, 5)*M+u*C-F(2, 5)*L-F(12, 25)*D-F(2, 25)
    R = u*(C-D)+u*M*D-(u-M)*L
    require(R-T == (M-F(1, 5))*(L+u*D-F(2, 5))
            and weights[0][2]+weights[1][2] == 0,
            'The tangent identity and common-initial-law cancellation remain exact')
    m, c, l, d = moments
    low = F(49, 50)
    nominal_floor = F(8367, 2000000)
    target_min = F(2, 5)*low*m+u*low*low*c-F(2, 5)*low*l-F(12, 25)*low*low*d-F(2, 25)
    initial_derivative = u*(c-F(4, 5)*d)
    final_derivative = low*initial_derivative+F(2, 5)*(m-l)
    require(initial_derivative.lo > 0 and final_derivative.lo > 0 and target_min.lo > nominal_floor,
            'The nominal target score is minimized at the two smallest target detector contrasts')
    target_floor = F(879, 250000)
    require(nominal_floor-sum(ranges)*bT > target_floor,
            'The complete target kinetic and interface allowance leaves the stated score floor')
    population = [tuple(map(F, row)) for row in old['population_gate_intervals_exact']]
    empirical = [tuple(map(F, row)) for row in old['empirical_gate_intervals_exact']]
    margins = [F(1, 400), F(1, 250), F(1, 250), F(1, 250), F(1, 250), F(3, 500)]
    require(all(inner == (outer[0]+gap, outer[1]-gap)
                for outer, inner, gap in zip(population, empirical, margins)),
            'The inherited empirical and population gates have their asserted exact margins')
    target_boxes = [(low*m.lo, m.hi), (low*l.lo+u*low*low*d.lo, l.hi+u*d.hi),
                    (low*low*c.lo, c.hi), (low*l.lo, l.hi), (low*low*d.lo, d.hi),
                    ((c-d).lo, low*low*(c-d).hi)]
    require(all(outer[0] < inner[0] <= inner[1] < outer[1] for inner, outer in zip(target_boxes, population)),
            'The full nominal detector family lies inside the population variance box')
    stationary = [(population[index][0]-2*ER, population[index][1]+2*ER) for index in (0, 2, 3, 4)]
    difference_box = (population[5][0]-4*ER, population[5][1]+4*ER)
    broad = ((F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
             (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25)), (-F(1, 25), -F(1, 1000)))
    require(all(outer[0] < inner[0] <= inner[1] < outer[1]
                for inner, outer in zip(stationary+[difference_box], broad)),
            'All stationary null laws behind passing population gates remain in the certified singleton box')
    require(stationary[0][0] > F(1, 5) and population[1][0]-2*(1+u)*ER > F(2, 5),
            'The stationary tangent remainder is positive throughout the enlarged null population box')
    null_band, initial_bound = F(2243, 2500000), F(27, 50000)
    require(F(7, 100000)+sum(ranges)*ER == null_band
            and F(1, 10000)+2*ER == initial_bound,
            'The stationary ceiling and complete-score TV transfer give the null score and initial-mean bounds')
    null_variances, target_variances = [F(299, 1000), F(13, 50)], [F(29, 100), F(253, 1000)]
    null_corners, target_uppers = [], []
    for arm, (a, b, g) in enumerate(weights):
        mean_box, corr_box = (population[0], population[2]) if arm == 0 else (population[3], population[4])
        mean_i, corr_i = h.Interval(*mean_box), h.Interval(*corr_box)
        mu = a*mean_i+b*corr_i+g*h.Interval(-initial_bound, initial_bound)
        dm, dcorr, dinitial = 2*b*g-2*a*mu, 2*a*g-2*b*mu, 2*a*b-2*g*mu
        require(dm.hi < 0 and dcorr.hi < 0 and dinitial.lo > 0,
                'Each exact variance decreases in its two recorded moments and increases in its initial mean')
        null_corner = variance(a, b, g, mean_box[0], corr_box[0], initial_bound)
        require(null_corner < [F(297793, 10**6), F(258957, 10**6)][arm] < null_variances[arm],
                'The worst null variance corner satisfies its asserted ceiling')
        tm, tc = (low*m, low*low*c) if arm == 0 else (low*l, low*low*d)
        target_upper = variance(a, b, g, tm, tc, F(0)).hi+ranges[arm]**2*bT
        require(target_upper < target_variances[arm],
                'The nominal target variance plus its complete TV charge satisfies its asserted ceiling')
        null_corners.append(str(null_corner))
        target_uppers.append(str(target_upper))
    max_step = max(ranges)/n
    for gap, variance_bound, exponent in ((cutoff-null_band, sum(null_variances)/n, F(3)),
                                           (target_floor-cutoff, sum(target_variances)/n, F(13, 4))):
        adjusted = gap-max_step*exponent/3
        require(adjusted > 0 and adjusted**2 > 2*variance_bound*exponent,
                'Rational squared Bernstein inequalities certify the null and target score tails')
    for gap, variance_bound, exponent in ((F(2057, 10**6)-null_band, sum(null_variances)/n, F(3)),
                                           (target_floor-F(2326, 10**6), sum(target_variances)/n, F(13, 4))):
        adjusted = gap-max_step*exponent/3
        require(adjusted > 0 and adjusted**2 > 2*variance_bound*exponent,
                'The additional printed rounded Bernstein intermediates retain strict certified slack')
    require(F(2057, 10**6) < cutoff < F(2326, 10**6),
            'The prescribed cutoff lies strictly between the displayed concentration bounds')
    outside_exponents = [F(n)*margins[0]**2/2, F(n)*margins[1]**2/(2*(1+u)**2),
                         F(n)*margins[2]**2/2, F(n)*margins[3]**2/2,
                         F(n)*margins[4]**2/2, F(n)*margins[5]**2/4]
    require(all(exp_negative_upper(x) < F(1, 20) for x in outside_exponents),
            'Failure of any one population gate makes its empirical pass alone rarer than five percent')
    tiny = F(1, 10**20)
    require(F(1, 2**120)*(1+u) < tiny,
            'The center charge exceeds both individual and combined moment enclosure radii')
    target_gate_gaps = [F(1, 250)-2*bT-tiny, F(3, 500)-2*(1+u)*bT-tiny,
                        F(1, 250)-2*bT-tiny, F(1, 250)-2*bT-tiny, F(1, 250)-2*bT-tiny]
    require((c-d).lo > -F(19, 1000) and low*low*(c-d).hi < -F(17, 1000)
            and min(-F(19, 1000)-empirical[5][0], empirical[5][1]+F(17, 1000)) == F(9, 1000),
            'The full target detector family retains the asserted nominal difference-gate clearance')
    difference_gap = F(9, 1000)-4*bT-tiny
    require(min(target_gate_gaps+[difference_gap]) > 0,
            'Every target gate has positive clearance after physical and kinetic errors')
    gate_exponents = [F(n)*target_gate_gaps[0]**2/2, F(n)*target_gate_gaps[1]**2/(2*(1+u)**2),
                      F(n)*target_gate_gaps[2]**2/2, F(n)*target_gate_gaps[3]**2/2,
                      F(n)*target_gate_gaps[4]**2/2, F(n)*difference_gap**2/4]
    gate_failure = 2*sum(exp_negative_upper(x) for x in gate_exponents)
    require(gate_failure < F(1, 500000)
            and exp_negative_upper(F(3)) < F(1, 20)
            and exp_negative_upper(F(13, 4))+F(1, 500000) < F(1, 20),
            'The gate and score bounds give both advertised five-percent error guarantees')
    return {'score_coefficients_exact': [list(map(str, row)) for row in weights],
            'integer_score_lookup_divisor': 50, 'integer_score_lookup': [[int(x) for x in row] for row in lookup],
            'outcome_order': [[1, 1], [1, -1], [-1, 1], [-1, -1]],
            'constant_subtracted_exact': '2/25', 'score_range_widths_exact': list(map(str, ranges)),
            'paired_trials_0H': n, 'paired_trials_H0': n, 'total_fresh_paired_trials': 2*n,
            'total_bit_readouts': 4*n, 'observed_joint_TV_model_allowance_exact': str(allowance),
            'target_execution_TV_allowance_exact': str(bT), 'null_displacement_exact': str(ER),
            'initial_mean_absolute_bound_exact': str(initial_bound),
            'null_score_mean_upper_exact': str(null_band), 'target_score_mean_lower_exact': str(target_floor),
            'rejection_cutoff_exact': str(cutoff),
            'null_variance_ceilings_exact': list(map(str, null_variances)),
            'target_variance_ceilings_exact': list(map(str, target_variances)),
            'null_variance_corners_exact': null_corners, 'target_variance_upper_bounds_exact': target_uppers,
            'gate_coordinate_order': old['gate_coordinate_order'],
            'population_gate_intervals_exact': [list(map(str, row)) for row in population],
            'empirical_gate_intervals_exact': [list(map(str, row)) for row in empirical],
            'target_joint_gate_failure_upper_exact': str(h.upper_decimal(gate_failure)),
            'target_joint_gate_failure_public_upper_exact': '1/500000',
            'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '1/20',
            'scope': 'Fresh independent paired trials are required. The model allowance enlarges the ordinary null and is not charged to the target. The kinetic charge belongs to the target; the ordinary kinetic class was already arbitrary.'}


def protected_readout_certificate(h):
    t, gamma = [h.Poly.variable(2, index) for index in range(2)]
    for s in (-1, 1):
        fluxes = [F(1, 2)*(1+t*s*z)*F(1, 2)*gamma*(1-t*s*z) for z in (-1, 1)]
        require(fluxes[0] == fluxes[1] == gamma*(1-t*t)*F(1, 4),
                'Every sector heat-bath edge has equal stationary flux for arbitrary common attempt rate')
    states = list(product((-1, 1), repeat=2))
    t = F(4, 5)
    law = [(1+t*s*z)/4 for s, z in states]
    kernel = [[F(0)]*4 for _ in range(4)]
    for i, (s, z) in enumerate(states):
        for j, (sj, zj) in enumerate(states):
            if sj == s:
                kernel[i][j] = F(i == j, 2)+(1+t*s*zj)/4
    require(all(sum(row) == 1 and min(row) >= 0 for row in kernel)
            and h.mm([law], kernel) == [law],
            'The protected hidden-reset example is stochastic and preserves full equilibrium')
    initial_joint = [[p if s == label else F(0) for p, (s, _) in zip(law, states)] for label in (-1, 1)]
    require(h.mm(initial_joint, kernel) == initial_joint,
            'The protected kernel preserves the initial-label and postmeasurement-state joint law exactly')
    worst_disturbance = max(sum(abs(kernel[i][j]-F(i == j)) for j in range(4))/2 for i in range(4))
    require(worst_disturbance == F(9, 20),
            'Joint equilibrium preservation coexists with the stated large worst-state disturbance')
    projection = [[(1+t*s*zj)/2 if sj == s else F(0) for sj, zj in states] for s, _ in states]
    require(h.mm(projection, projection) == projection
            and h.mm(initial_joint, projection) == initial_joint,
            'Even full within-sector reset preserves the required joint law')
    p, qminus, qplus = [h.Poly.variable(3, index) for index in range(3)]
    flux = p*qminus-(1-p)*qplus
    signed_stationarity_defect = h.mm([[p, 1-p]], [[-qminus, qminus], [qplus, -qplus]])
    require(signed_stationarity_defect == [[-flux, flux]],
            'The binary-sector half-l1 stationarity defect equals the absolute stationary flux imbalance')
    require(F(1, 2)*F(1, 10**6)+F(1, 2)*F(3, 10**6)+F(8, 10**6) == F(1, 100000),
            'An explicit weighted conditional-defect and leakage allocation fits the common instrument allowance')
    require(5*exp_negative_upper(F(124, 5)) < F(1, 10**10),
            'The recalled equal-attempt target reset-time numerical tail has its asserted squared-TV bound')
    return {'conditional_polarization_exact': '4/5',
            'conditional_law_example_exact': ['9/10', '1/10'],
            'example_initial_state_joint_exact': [list(map(str, row)) for row in initial_joint],
            'example_protected_kernel_exact': [list(map(str, row)) for row in kernel],
            'example_worst_row_TV_disturbance_exact': str(worst_disturbance),
            'example_equilibrium_joint_disturbance_exact': '0',
            'conditional_heat_bath_flux_identity': 'gamma*(1-t*t)/4',
            'binary_conditional_stationarity_defect': 'abs(pi_minus*q_minus-pi_plus*q_plus)',
            'instrument_allowance_exact': '1/100000',
            'recalled_equal_attempt_target_reset_time': 62,
            'recalled_target_reset_squared_TV_upper_exact': '1/10000000000',
            'scope': 'The general joint-instrument invariance, contraction, leakage, and flux-defect statements are analytic. The reset bound is target-specific and is not transferred to perturbed kinetics or arbitrary rivals. Protected readout does not establish preparation, independent trials, or an independent electronic channel.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_kinetic_interface.json'))
    args = parser.parse_args()
    h, prior, moments, centers = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrices, polynomial identities, outward rational intervals and concentration arithmetic',
              'kinetic_tolerance': kinetic_certificate(h, prior),
              'fixed_score_design': score_certificate(h, prior, moments),
              'protected_readout': protected_readout_certificate(h),
              'largest_dense_matrix_dimension': 4,
              'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': {INPUT_REPORT: INPUT_SHA},
              'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**prior['proof_snapshot_sha256'], **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS, 'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
