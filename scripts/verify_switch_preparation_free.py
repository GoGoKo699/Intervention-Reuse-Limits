#!/usr/bin/env python3
"""Exact certificates for the four-word preparation-free singleton test.

The universal return identity and adapted sampling proofs live in hash-bound
notes. Finite checks here use exact polynomial, rational and matrix arithmetic.
They neither enumerate all rivals nor certify laboratory instrument promises.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from math import comb
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    'reports/switch_percent_kinetics.json': '4ddbddfef6c3c31fc5785a21e51aeac521b0b8c5685e595a7b86c615d6ee807e',
    'reports/switch_repeated_readout.json': '488a3e39aca64284acc388a91fd38d479b14b727eec0fbf6b21772225391d086',
}
IMPORTS = {
    'verify_switch_percent_kinetics.py': '6e59c54164d8bef4cca9a45b88a8b70c7dfcbfbd20afbaebc52d7aa7e9358525',
    'verify_familiar_switch_margin.py': 'e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397',
}
PROOFS = {
    'docs/FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md': '42530472f40412d9e1f93d868a4df1dd2d833ba34ee89f8531df1cb1679dec0a',
    'docs/FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md': '311ddad97cfec6ab09a733565e5655532a4449f2b1ff4c33a37516565ed592fa',
    'docs/FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md': 'eb35e4b689e6a06573eea0fa12e91e19a41c08c23ec14bf0d5262c0b1846a5b9',
}
CHECKS = 0
U = F(3, 5)
B = F(79, 10**6)
N, M, N_GROUP = 9000000, 2250000, 1000000


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def import_source(name):
    path = ROOT/'scripts'/name
    require(hashlib.sha256(path.read_bytes()).hexdigest() == IMPORTS[name],
            'The imported exact-arithmetic source matches its frozen hash')
    spec = importlib.util.spec_from_file_location('preparation_free_'+path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_inputs():
    priors, inherited_proofs = {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected,
                'Each prerequisite report has its unconditional frozen hash')
        report = json.loads(payload)
        require(report['status'] == 'PASS', 'Each prerequisite report passed')
        for source, digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Every inherited verifier retains its recorded source hash')
        for proof, digest in report['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/proof).read_bytes()).hexdigest() == digest,
                    'Every inherited proof retains its frozen snapshot')
            require(proof not in inherited_proofs or inherited_proofs[proof] == digest,
                    'Overlapping inherited proof bindings agree')
            inherited_proofs[proof] = digest
        for predecessor, digest in report.get('input_report_sha256', {}).items():
            require(hashlib.sha256((ROOT/predecessor).read_bytes()).hexdigest() == digest,
                    'Immediate inherited report inputs retain their recorded hashes')
        priors[name] = report
    require(len(PROOFS) == 3 and all(len(value) == 64 for value in PROOFS.values()),
            'All three new universal proofs have unconditional reviewed hashes')
    for name, digest in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'Each new proof matches its reviewed snapshot')
    h, v = import_source('verify_familiar_switch_margin.py'), import_source('verify_switch_percent_kinetics.py')
    return h, v, priors, inherited_proofs


def exp_negative_upper(value):
    require(value > 0, 'Every exponential comparison has positive rational exponent')
    term = total = F(1)
    for order in range(1, 41):
        term *= value/order
        total += term
    return 1/total


def residual(s, r0, rh, r0h, rh0):
    return (1-s*U)*r0h-(1+s*U)*rh0+2*s*U*r0*rh


def majority_tail(p):
    return sum(F(comb(7, k))*p**k*(1-p)**(7-k) for k in range(4, 8))


def singleton_and_sampling_identities(h):
    pi = [F(1, 5), F(3, 10), F(1, 2)]
    edges = [(0, 1), (0, 2), (1, 2)]
    fluxes = [h.Poly.variable(6, j) for j in range(6)]
    fixtures = []
    for s in (-1, 1):
        signs = [s, -s, -s]
        imbalance = sum(p*t for p, t in zip(pi, signs))
        high = [p*(1+U*t)/(1+U*imbalance) for p, t in zip(pi, signs)]
        require(sum(high) == 1 and min(high) > 0 and imbalance != 0,
                'The singleton fixture admits an unbalanced low law and positive normalized Gibbs tilt')
        kernels = []
        for arm, law in enumerate((pi, high)):
            kernel = [[h.Poly(6) for _ in range(3)] for _ in range(3)]
            for j, (a, b) in enumerate(edges):
                kernel[a][b] = fluxes[3*arm+j]/law[a]
                kernel[b][a] = fluxes[3*arm+j]/law[b]
            for j in range(3):
                kernel[j][j] = 1-sum(kernel[j])
            require(all(sum(row) == 1 for row in kernel)
                    and h.mm([law], kernel) == [law]
                    and all(law[i]*kernel[i][j] == law[j]*kernel[j][i]
                            for i, j in product(range(3), repeat=2)),
                    'The symbolic flux family has row sums one, stationarity and ordinary detailed balance')
            concrete = [[entry.evaluate([F(1, 100)]*6) for entry in row] for row in kernel]
            require(all(min(row) > 0 and sum(row) == 1 for row in concrete),
                    'A strictly positive stochastic point exists in each symbolic reversible fixture')
            kernels.append(kernel)
        low, high_kernel = kernels
        for j in (1, 2):
            require((1-s*U)*low[0][j]*high_kernel[j][0]
                    == (1+s*U)*high_kernel[0][j]*low[j][0],
                    'Each off-singleton return contribution obeys the Gibbs-tilted detailed-balance identity')
        r0h, rh0 = h.mm(low, high_kernel)[0][0], h.mm(high_kernel, low)[0][0]
        require(residual(s, low[0][0], high_kernel[0][0], r0h, rh0) == 0,
                'The complete singleton residual vanishes as an exact six-variable polynomial')
        fixtures.append({'singleton_sign': s, 'low_law_exact': list(map(str, pi)),
                         'high_law_exact': list(map(str, high)), 'low_imbalance_exact': str(imbalance)})
    m, c, ell, d = [h.Poly.variable(4, j) for j in range(4)]
    x, a = (ell+U*d)/U, 1-m/U
    for s in (-1, 1):
        rs = residual(s, (1+x)/2, (1+a+s*m)/2, (1+c+s*m)/2, (1+d+s*ell)/2)
        fs = U*(c-d)-s*U*m*d+s*(U-m)*ell
        require(rs == (1-s*U)/(2*U)*fs,
                'Direct symbolic substitution proves the return-residual versus latent-witness identity')
    r0, rh, r0h, rh0, e0, eh, e0h, eh0 = [h.Poly.variable(8, j) for j in range(8)]
    for s in (-1, 1):
        linear = (1-s*U)*e0h-(1+s*U)*eh0+2*s*U*(rh*e0+r0*eh)
        require(residual(s, r0+e0, rh+eh, r0h+e0h, rh0+eh0)
                -residual(s, r0, rh, r0h, rh0) == linear+2*s*U*e0*eh,
                'The retained-record residual has exactly the stated linear part and quadratic remainder')
        for r0_value, rh_value in product((F(0), F(1)), repeat=2):
            coefficients = [1-s*U, -(1+s*U), 2*s*U*rh_value, 2*s*U*r0_value]
            require(sum(map(abs, coefficients)) <= F(22, 5)
                    and sum(value*value for value in coefficients) <= F(28, 5),
                    'All extremal probability corners satisfy the linear width and squared-width ceilings')
    return {'unbalanced_reversible_symbolic_fixtures': fixtures,
            'symbolic_flux_variable_count': 6, 'residual_linear_l1_upper_exact': '22/5',
            'residual_linear_squared_l2_upper_exact': '28/5',
            'scope': 'Universal singleton and stopped-sampling arguments are in the bound proofs; the symbolic flux fixtures demonstrate both singleton orientations without a balanced stationary law.'}


def four_word_upper_identity(h, prior):
    realization = prior['local_snapshot_realization']
    coordinates = [list(map(F, row)) for row in realization['coordinate_matrix_exact']]
    inverse = [[entry/h.determinant(coordinates) for entry in row] for row in h.adjugate(coordinates)]
    low, high = [list(map(F, row)) for row in realization['stationary_laws_exact']]
    signs = [F(-1), F(1), F(1)]
    require(sum(p*s for p, s in zip(low, signs)) == 0
            and high == [p*(1+U*s) for p, s in zip(low, signs)],
            'The inherited general three-state basis has the balanced law and required Gibbs tilt')
    x, y, z, w, a, b, c, d = [h.Poly.variable(8, j) for j in range(8)]
    matrices = [[[1, 0, 0], [0, x, z], [0, y, w]],
                [[1, U*(1-a), -U*c], [0, a, c], [0, b, d]]]
    kernels = [h.mm(h.mm(coordinates, matrix), inverse) for matrix in matrices]
    for kernel, law in zip(kernels, (low, high)):
        require(all(sum(row) == 1 for row in kernel) and h.mm([law], kernel) == [law],
                'The whole predictive affine family preserves its two specified stationary laws')
    def moments(kernel):
        return [sum(low[i]*(signs[i] if correlation else 1)*kernel[i][j]*signs[j]
                    for i, j in product(range(3), repeat=2)) for correlation in (False, True)]
    low_one, high_one = [moments(kernel) for kernel in kernels]
    m, cc = moments(h.mm(kernels[0], kernels[1]))
    ell, dd = moments(h.mm(kernels[1], kernels[0]))
    require(low_one == [0, x] and high_one == [m, a]
            and m+U*a == U and ell+U*dd == U*x,
            'Both added single-word moments are exactly determined by the original two-word moments')
    require(len(realization['embedding_certificates']) == 2
            and all(item['affine_corner_count'] == 16 for item in realization['embedding_certificates']),
            'The frozen predecessor certifies both fixed kernel families as positive continuous-time propagators')
    return {'additional_word_order': ['0', 'H'],
            'single_word_mean_identities': ['0', 'm'],
            'single_word_correlation_identities': ['(l+u*d)/u', '1-m/u'],
            'general_three_state_four_pair_error_exact': '0',
            'scope': 'The same inherited general three-state CTMC pair matches all four stationary ideal-bit pair laws. No intermediate-record or full repeated-readout transcript upper is claimed.'}


def percent_margin_certificate(h, v, prior):
    weak = json.loads((ROOT/'reports/switch_weak_field.json').read_text())
    require(hashlib.sha256((ROOT/'reports/switch_weak_field.json').read_bytes()).hexdigest()
            == v.INPUTS['reports/switch_weak_field.json'],
            'The rerun perturbation calculation uses the frozen weak-field input')
    inherited, moments, single, raw_remainder, one_remainder = v.perturbation_certificate(h, weak)
    rho = F(146372172429, 10**15)
    require(raw_remainder < rho
            and inherited == prior['perturbation_certificate'],
            'Independent recalculation reproduces the frozen moment-polynomial certificate and outward remainder')
    coarse = [(F(219, 1000), F(223, 1000)), (F(479, 1000), F(487, 1000)),
              (F(124, 1000), F(128, 1000)), (F(498, 1000), F(505, 1000))]
    for polynomial, (lo, hi) in zip(moments, coarse):
        interval = v.polynomial_interval(h, polynomial, rho)
        require(lo < interval.lo <= interval.hi < hi,
                'Both true and polynomial moments lie within the inherited coarse interval')
    expanded = [h.Interval(lo-rho, hi+rho) for lo, hi in coarse]
    mi, ci, li, di = expanded
    m, c, ell, d = moments
    results = []
    for s in (-1, 1):
        factor = (1-s*U)/(2*U)
        gradients = [factor*(-s*U*di-s*li), h.Interval(factor*U),
                     factor*s*(U-mi), factor*(-U-s*U*mi)]
        gradient_l1 = sum(max(abs(value.lo), abs(value.hi)) for value in gradients)
        require(gradient_l1 < 4,
                'The residual gradient l1 norm is below four on every expanded containing-box segment')
        polynomial = factor*(U*(c-d)-s*U*m*d+s*(U-m)*ell)
        center, width = polynomial.terms[v.ZERO], v.polynomial_width(polynomial)
        remainder = 4*rho+3*rho*rho
        lo, hi = center-width-remainder, center+width+remainder
        require((lo > F(9, 1000) if s == -1 else hi < -F(9, 1000)),
                'The directly combined kinetic polynomial uniformly separates its return residual from zero by .009')
        results.append({'sign': s, 'polynomial_certificate': v.polynomial_summary(polynomial),
                        'gradient_l1_upper_exact': str(gradient_l1),
                        'range_enclosure_exact': [str(v.down(lo)), str(v.up(hi))]})
    require(m == single[1] and (ell+U*d)/U == single[0],
            'The recalculated target polynomials obey the two single-plateau stationary identities exactly')
    return {'independent_edge_count': 8, 'relative_kinetic_interval_exact': ['99/100', '101/100'],
            'moment_remainder_upper_exact': str(rho), 'propagated_residual_remainder_upper_exact': str(4*rho+3*rho*rho),
            'expanded_containing_moment_box_exact': [[str(box.lo), str(box.hi)] for box in expanded],
            'signed_residual_certificates': results, 'signed_uniform_margin_lower_exact': '9/1000',
            'imported_perturbation_checks': v.CHECKS,
            'scope': 'Exact coefficient bounds over the full eight-dimensional kinetic box, not a parameter grid or floating-point optimization.'}


def conditional_tv_certificate(h):
    r, mass, delta_r = [h.Poly.variable(3, j) for j in range(3)]
    require(mass*(r+delta_r)-r*mass == mass*delta_r,
            'The centered within-sector return numerator is exactly sector mass times conditional error')
    for value in (F(0), F(1, 3), F(1)):
        values = [-value, 1-value, F(0)]
        require(max(values)-min(values) == 1,
                'The centered return indicator has oscillation one, including deterministic-return endpoints')
    delta = F(1, 1000)
    conditional = delta/(F(1, 2)-delta)
    drift = F(22, 5)*conditional
    require(conditional == F(1, 499) and drift == F(22, 2495) < F(9, 1000),
            'A joint-table TV ball of radius .001 cannot bring either target residual to the ordinary singleton zero')
    eps = F(1, 100000)
    execution = 2*eps+(F(1, 2)+F(101, 100)*(F(5, 4)+eps))*eps+F(101, 25)*eps
    require(execution == F(78025101, 10**12) < B and B/(F(1, 2)-B) == F(79, 499921),
            'The inherited target execution budget yields the stated conditional return radius for all four words')
    return {'pair_TV_gap_lower_exact': str(delta), 'conditional_error_at_gap_exact': str(conditional),
            'residual_displacement_at_gap_upper_exact': str(drift),
            'uniform_residual_margin_lower_exact': '9/1000',
            'target_execution_TV_exact': str(execution), 'conservative_target_TV_exact': str(B),
            'target_conditional_return_error_upper_exact': '79/499921',
            'general_state_minimum': 3, 'ordinary_state_minimum': 4,
            'scope': 'Four ideal initial/final pair laws with arbitrary per-word rival preparation, shared exact tilt and fixed dynamics; the general and ordinary upper models use stationary target preparation.'}


def ideal_sampling_certificate():
    n, cutoff, eta, b = N_GROUP, F(1, 250), F(1, 100), B/(F(1, 2)-B)
    quadratic = 2*U*eta*eta
    h_null = cutoff-quadratic
    h_target = F(9, 1000)-cutoff-F(22, 5)*b-quadratic
    null_exp = 2*n*h_null*h_null/F(28, 5)
    target_exp = 2*n*h_target*h_target/F(28, 5)
    quota_exp = 2*(M*(F(1, 2)-B)-n)**2/M
    require(N == 4*M and 0 < n < M*(F(1, 2)-B)
            and quadratic == F(3, 25000) and h_target > 0,
            'The fixed cap, quotas and residual margins satisfy the ideal acquisition design')
    require(null_exp == F(9409, 1750)
            and target_exp == F(1367663932665522, 218680880460875) > F(25, 4)
            and quota_exp == F(249289505521, 18000000),
            'The ideal singleton-null, target and eight-group quota exponents equal their stated exact values')
    null_upper = exp_negative_upper(null_exp)+4*exp_negative_upper(2*n*eta*eta)
    target_upper = (2*exp_negative_upper(target_exp)+8*exp_negative_upper(2*n*(eta-b)**2)
                    +8*exp_negative_upper(quota_exp))
    require(null_upper < F(1, 200) < F(1, 20)
            and target_upper < F(1, 250) < F(1, 20),
            'The unconditional ideal test has size below .005 and target miss below .004')
    return {'total_trials': N, 'trials_per_word': M, 'records_per_word_sign': n,
            'binary_readouts': 2*N, 'rejection_residual_threshold_exact': str(cutoff),
            'quadratic_control_radius_exact': str(eta), 'quadratic_residual_bound_exact': str(quadratic),
            'null_linear_exponent_exact': str(null_exp), 'target_linear_exponent_exact': str(target_exp),
            'target_quota_exponent_exact': str(quota_exp),
            'null_rejection_upper_exact': '1/200', 'target_miss_upper_exact': '1/250',
            'scope': 'Retain the first fixed quota in each observed true-sign group at a fixed horizon; incomplete groups cause nonrejection. Conditional Hoeffding is applied before conditioning on quota completion.'}


def noisy_sampling_certificate():
    n, cutoff, eta, b = N_GROUP, F(1, 250), F(1, 100), B/(F(1, 2)-B)
    ceiling, target_tail = majority_tail(F(1, 50)), majority_tail(F(1, 100))
    require(ceiling == F(26053, 4882812500) and target_tail == F(1708349, 5000000000000),
            'Both seven-read stages use the same certified majority-error tails')
    mean_bound = M*ceiling
    require(3*mean_bound < 37,
            'The exponential-moment bound at base four is below exp(37) for each stage and word')
    # E[4^K] <= exp(3 M p). Since e<3 and 3 M p<37,
    # P(K>=50) < 3^37/4^50. This also bounds P(K>50).
    count_tail = F(3**37, 4**50)
    require(count_tail < F(1, 10**12) and 8*count_tail < F(3, 10**12),
            'The exact Chernoff count tails have the stated per-event and eight-event union upper bounds')
    mean_shift = F(2*50, n)
    residual_shift = F(22, 5)*mean_shift
    quadratic = 2*U*eta*eta
    h_null = cutoff-residual_shift-quadratic
    h_target = F(9, 1000)-cutoff-F(22, 5)*b-residual_shift-quadratic
    require(mean_shift == F(1, 10000) and residual_shift == F(11, 25000)
            and h_null > 0 and h_target > 0,
            'At most fifty errors per stage change each retained mean by .0001 and each residual by .00044')
    null_exp = 2*n*h_null*h_null/F(28, 5)
    target_exp = 2*n*h_target*h_target/F(28, 5)
    null_gate_exp, target_gate_exp = 2*N*F(23, 2500)**2, 2*N*F(51, 5000)**2
    quota_probability = F(1, 2)-B-target_tail
    quota_exp = 2*(M*quota_probability-n)**2/M
    require(0 < quota_probability < F(1, 2) and M*quota_probability > n
            and null_gate_exp == F(38088, 25) and target_gate_exp == F(46818, 25)
            and quota_exp > 13849,
            'Observed-majority quotas have a positive target margin and the two stage gates have the stated pooled exponents')
    require(null_exp == F(3698, 875)
            and target_exp == F(2190355223115361, 437361760921750)
            and h_target == F(46801231, 12498025000),
            'The noisy residual margins and concentration exponents equal the displayed rational values')
    small_noise_null = (exp_negative_upper(null_exp)+4*exp_negative_upper(2*n*eta*eta)
                        +8*count_tail)
    null_upper = max(small_noise_null, exp_negative_upper(null_gate_exp))
    target_upper = (2*exp_negative_upper(target_exp)+8*exp_negative_upper(2*n*(eta-b)**2)
                    +8*count_tail+2*exp_negative_upper(target_gate_exp)+8*exp_negative_upper(quota_exp))
    require(null_upper < F(3, 200) < F(1, 20)
            and target_upper < F(7, 500) < F(1, 20),
            'Eight count tails, two target gates and eight quota failures preserve size below five percent and power above 95 percent')
    reset, active = 63*N, F(15, 8)*N
    require(reset == 567000000 and active == 16875000
            and reset+active == 583875000 and 14*N == 126000000,
            'The inherited sixty-three-unit target reset and four-word active duration give the stated physical resource totals')
    return {'total_trials': N, 'trials_per_word': M, 'records_per_word_sign': n,
            'initial_reads_per_trial': 7, 'final_reads_per_trial': 7, 'total_physical_binary_reads': 14*N,
            'per_word_stage_error_cap': 50, 'number_of_count_tail_events': 8,
            'error_count_mean_upper_exact': str(mean_bound), 'per_count_tail_upper_exact': str(count_tail),
            'retained_mean_shift_upper_exact': str(mean_shift), 'residual_shift_upper_exact': str(residual_shift),
            'null_linear_margin_exact': str(h_null), 'target_linear_margin_exact': str(h_target),
            'null_linear_exponent_exact': str(null_exp), 'target_linear_exponent_exact': str(target_exp),
            'per_stage_disagreement_gate_threshold_exact': '3/100',
            'large_noise_null_gate_exponent_exact': str(null_gate_exp),
            'target_gate_exponent_exact': str(target_gate_exp), 'target_observed_quota_exponent_exact': str(quota_exp),
            'null_rejection_upper_exact': '3/200', 'target_miss_upper_exact': '7/500',
            'target_nominal_reset_attempt_units': reset,
            'target_nominal_active_attempt_units': int(active),
            'target_nominal_reset_plus_active_attempt_units': int(reset+active),
            'resource_cost_excludes_readout_and_barrier_durations': True,
            'scope': 'Two protected seven-read blocks with fixed fresh stage-specific errors, exact sector preservation, fixed hidden dynamics and a target true-bit pair budget. The true-sign comparison arrays are padded after the horizon if needed; the proof does not condition an oracle sampling law on observed completion. The raw transcript is not covered by the three-state upper.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_preparation_free.json'))
    args = parser.parse_args()
    h, v, priors, inherited_proofs = load_inputs()
    prior = priors['reports/switch_percent_kinetics.json']
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction sparse polynomials, finite matrices and positive exponential series',
              'singleton_and_concentration_identities': singleton_and_sampling_identities(h),
              'four_word_general_realization': four_word_upper_identity(h, prior),
              'percent_kinetic_residual_margin': percent_margin_certificate(h, v, prior),
              'conditional_TV_and_memory_gap': conditional_tv_certificate(h),
              'ideal_sampling_certificate': ideal_sampling_certificate(),
              'repeated_readout_sampling_certificate': noisy_sampling_certificate(),
              'rival_preparation_promise_required': False,
              'target_execution_promise_required': True, 'strictly_positive_stationary_laws_required': True,
              'shared_exact_stationary_tilt_required': True, 'readout_conditional_freshness_required_for_noisy_test': True,
              'full_raw_transcript_state_count_claimed': False, 'device_feasibility_claimed': False,
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), **IMPORTS},
              'input_report_sha256': INPUTS, 'imported_repository_verifiers': list(IMPORTS),
              'proof_snapshot_sha256': {**inherited_proofs, **PROOFS}}
    report['direct_checks'] = CHECKS
    report['imported_perturbation_checks'] = v.CHECKS
    report['checks'] = CHECKS+v.CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'checks': report['checks'],
                      'direct_checks': CHECKS, 'imported_perturbation_checks': v.CHECKS,
                      'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
