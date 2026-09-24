#!/usr/bin/env python3
"""Exact certificates for bounded endpoint registration and relative force error.

Hash-bound proofs carry the conditional measurement, sampling and force-law
arguments. These finite checks use rational arithmetic and small symbolic
fixtures, without a parameter search or simulated experimental records.
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
INPUTS = {
    'reports/switch_preparation_free.json': 'dc10d2baf22899ef663faa4406d720998771e7c40c4de7ef4e8a7b2a3bed3df1',
}
HELPER = 'verify_familiar_switch_margin.py'
HELPER_SHA = 'e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397'
PROOFS = {
    'docs/FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md': '41df45ab86d3a005d9dd32497a7329f711bb433a7fe686ae6ee84b931bf615c9',
    'docs/FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md': '99464fb83b33748c29859f27bbef53b5b8fd7b078b60559978b5bb9d64d087ea',
}
CHECKS = 0
U, B, P_STAR = F(3, 5), F(79, 10**6), F(1, 200000)
SPREAD = F(1001, 1000)
N, M, N_GROUP = 9000000, 2250000, 1000000


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    priors, inherited_proofs = {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected,
                'The preparation-free prerequisite report matches its unconditional frozen hash')
        report = json.loads(payload)
        require(report['status'] == 'PASS', 'The prerequisite report passed')
        for source, digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Each inherited verifier retains its frozen source hash')
        for proof, digest in report['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/proof).read_bytes()).hexdigest() == digest,
                    'Each inherited proof retains its frozen snapshot')
            inherited_proofs[proof] = digest
        for predecessor, digest in report.get('input_report_sha256', {}).items():
            require(hashlib.sha256((ROOT/predecessor).read_bytes()).hexdigest() == digest,
                    'Each immediate inherited report input retains its recorded hash')
        priors[name] = report
    require(len(PROOFS) == 2 and all(len(value) == 64 for value in PROOFS.values()),
            'Both new universal proofs have unconditional reviewed hashes')
    for name, digest in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'Each new proof matches its reviewed snapshot')
    helper_path = ROOT/'scripts'/HELPER
    require(hashlib.sha256(helper_path.read_bytes()).hexdigest() == HELPER_SHA,
            'The exact rational polynomial helper retains its unconditional hash')
    spec = importlib.util.spec_from_file_location('endpoint_registration_exact_helper', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper, priors['reports/switch_preparation_free.json'], inherited_proofs


def tv(first, second):
    return sum((abs(a-b) for a, b in zip(first, second)), F(0))/2


def residual(sign, low, high, low_high, high_low):
    return (1-sign*U)*low_high-(1+sign*U)*high_low+2*sign*U*low*high


def exp_negative_upper(value):
    require(value > 0, 'Every concentration comparison uses a positive rational exponent')
    term = total = F(1)
    for order in range(1, 41):
        term *= value/order
        total += term
    return 1/total


def inherited_contract_certificate(prior):
    ideal = prior['ideal_sampling_certificate']
    noisy = prior['repeated_readout_sampling_certificate']
    gap = prior['conditional_TV_and_memory_gap']
    require(ideal['total_trials'] == N and ideal['trials_per_word'] == M
            and ideal['records_per_word_sign'] == N_GROUP
            and F(ideal['rejection_residual_threshold_exact']) == F(1, 250),
            'The endpoint test retains the frozen four-word cap, quotas and residual threshold')
    require(F(gap['uniform_residual_margin_lower_exact']) == F(9, 1000)
            and F(gap['conservative_target_TV_exact']) == B
            and F(gap['target_conditional_return_error_upper_exact']) == F(79, 499921)
            and F(prior['singleton_and_concentration_identities']['residual_linear_l1_upper_exact']) == F(22, 5)
            and F(prior['singleton_and_concentration_identities']['residual_linear_squared_l2_upper_exact']) == F(28, 5),
            'The full one-percent kinetic margins and conditional-return concentration constants remain frozen')
    require(noisy['per_word_stage_error_cap'] == 50
            and F(noisy['retained_mean_shift_upper_exact']) == F(1, 10000)
            and F(noisy['residual_shift_upper_exact']) == F(11, 25000),
            'The previously proved ordered-list stability estimate uses the same fifty-error caps')
    return {'four_word_order': ['0', 'H', '0H', 'H0'],
            'target_residual_margin_lower_exact': '9/1000',
            'target_conditional_return_error_upper_exact': '79/499921',
            'scope': 'The new registration theorem reuses the true-sign oracle and fixed-quota algebra, not the old fresh-Bernoulli detector model or its disagreement gates.'}


def endpoint_boundary_certificate(h):
    pi, nu = [F(1, 2), F(1, 4), F(1, 4)], [F(1), F(0), F(0)]
    signs = [-1, 1, 1]
    reset = [pi[:] for _ in range(3)]
    post = h.mm([nu], reset)[0]
    post_joint = [post[j]*F(signs[j] == s) for s, j in product((-1, 1), range(3))]
    ideal_joint = [pi[j]*F(signs[j] == s) for s, j in product((-1, 1), range(3))]
    pre_joint = [sum(pi[i]*F(signs[i] == s)*reset[i][j] for i in range(3))
                 for s, j in product((-1, 1), range(3))]
    require(post == pi and h.mm([pi], reset) == [pi]
            and sum(pi[i]*reset[i][j] for i, j in product(range(3), repeat=2)
                    if signs[i] != signs[j]) == F(1, 2),
            'An equilibrium-preserving initial operation may change the sign with probability one half')
    require(tv(post_joint, ideal_joint) == 0 and tv(pre_joint, ideal_joint) == F(1, 2),
            'Post-instrument truth gives the ideal stationary joint law even when pre-instrument labeling would fail')
    for first, second in ((pi, nu), (pi, [F(1, 3)]*3)):
        embedded_first = [first[j]*F(signs[j] == s) for s, j in product((-1, 1), range(3))]
        embedded_second = [second[j]*F(signs[j] == s) for s, j in product((-1, 1), range(3))]
        require(tv(embedded_first, embedded_second) == tv(first, second),
                'Appending the deterministic post-instrument sign preserves the hidden marginal TV distance')
    # A detector with errors only on one hidden state is asymmetric and
    # state-dependent, yet each pre-window conditional error is <= p_star.
    error_rates = [P_STAR, F(0), P_STAR/2]
    recorded = [[pi[j]*((1-error_rates[j]) if s == signs[j] else error_rates[j])
                 for j in range(3)] for s in (-1, 1)]
    require(all(0 <= value <= P_STAR for value in error_rates)
            and sum(sum(row) for row in recorded) == 1
            and error_rates[0] != error_rates[1],
            'Bounded registration admits a hidden-state-dependent asymmetric detector fixture')
    prep, defect = F(1, 100000), F(1, 100000)
    execution = prep+defect+(F(1, 2)+F(101, 100)*(F(5, 4)+prep))*prep+F(101, 25)*prep
    require(execution == F(78025101, 10**12) < B,
            'One preparation charge and one post-instrument stationary defect fit the inherited target execution allowance')
    return {'initial_truth_boundary': 'After the complete initial registration window',
            'final_truth_boundary': 'Before the final registration window',
            'sign_changing_initial_fixture_probability_exact': '1/2',
            'post_truth_fixture_joint_TV_exact': '0', 'pre_truth_fixture_joint_TV_exact': '1/2',
            'asymmetric_fixture_per_state_error_upper_exact': list(map(str, error_rates)),
            'target_postinstrument_stationary_defect_allowance_exact': '1/100000',
            'target_execution_budget_exact': str(execution),
            'scope': 'The universal marginal-TV contraction and post-boundary singleton argument are supplied by the proof. Null initial instruments may move between signs; the active kernels still start from the registered true endpoint state.'}


def registration_sampling_certificate():
    n, cutoff, eta = N_GROUP, F(1, 250), F(1, 100)
    b = B/(F(1, 2)-B)
    mean_count = M*P_STAR
    require(mean_count == F(45, 4) and 3*mean_count == F(135, 4) < 34,
            'Conditional registration errors have per-word-stage count mean at most 11.25')
    # For any adapted Bernoulli errors with conditional mean <= p_star,
    # E[4^K] <= (1+3p_star)^M <= exp(3 M p_star).
    # Markov and e<3 give P(K>=50) < 3^34/4^50.
    count_tail = F(3**34, 4**50)
    count_union = 8*count_tail
    require(count_union < F(2, 10**13),
            'The exact rational eight-count Chernoff union bound is below 2e-13')
    mean_shift, residual_shift = F(100, n), F(22, 5)*F(100, n)
    quadratic = 2*U*eta*eta
    h_null = cutoff-residual_shift-quadratic
    h_target = F(9, 1000)-cutoff-F(22, 5)*b-residual_shift-quadratic
    null_exponent = 2*n*h_null*h_null/F(28, 5)
    target_exponent = 2*n*h_target*h_target/F(28, 5)
    quota_probability = F(1, 2)-B-P_STAR
    quota_exponent = 2*(M*quota_probability-n)**2/M
    require(mean_shift == F(1, 10000) and residual_shift == F(11, 25000)
            and quadratic == F(3, 25000) and h_null == F(43, 12500)
            and h_target == F(46801231, 12498025000) and 50 < n,
            'List stability and the inherited oracle drift give the asserted null and target margins')
    require(null_exponent == F(3698, 875)
            and target_exponent == F(2190355223115361, 437361760921750)
            and quota_probability == F(124979, 250000)
            and quota_exponent == F(15577785721, 1125000) > 13846,
            'The endpoint-registration concentration and observed-quota exponents equal their exact values')
    null_upper = exp_negative_upper(null_exponent)+4*exp_negative_upper(2*n*eta*eta)+count_union
    target_upper = (2*exp_negative_upper(target_exponent)
                    +8*exp_negative_upper(2*n*(eta-b)**2)
                    +count_union+8*exp_negative_upper(quota_exponent))
    require(null_upper < F(3, 200) < F(1, 20)
            and target_upper < F(7, 500) < F(1, 20),
            'The endpoint-registration test has size below .015 and miss probability below .014 without disagreement gates')
    return {'total_trials': N, 'trials_per_word': M, 'records_per_word_sign': n,
            'conditional_endpoint_error_upper_exact': str(P_STAR),
            'per_word_stage_error_cap': 50, 'error_count_mean_upper_exact': str(mean_count),
            'per_count_tail_upper_exact': str(count_tail), 'eight_count_tail_upper_exact': str(count_union),
            'retained_mean_shift_upper_exact': str(mean_shift), 'residual_shift_upper_exact': str(residual_shift),
            'target_conditional_return_error_upper_exact': str(b),
            'null_linear_margin_exact': str(h_null), 'target_linear_margin_exact': str(h_target),
            'null_linear_exponent_exact': str(null_exponent), 'target_linear_exponent_exact': str(target_exponent),
            'target_observed_sign_probability_lower_exact': str(quota_probability),
            'target_observed_quota_exponent_exact': str(quota_exponent),
            'null_rejection_upper_exact': '3/200', 'target_miss_upper_exact': '7/500',
            'disagreement_gates_used': False,
            'scope': 'The known conditional error ceiling is a physical promise, allowing asymmetric, history-dependent and same-window error/backaction correlations. No calibration gate estimates or certifies that ceiling.'}


def stationary_barrier_certificate(h):
    generator, pi, signs = h.physical_generator(F(4, 5), F(0))
    edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
    factors = [h.Poly.variable(4, j) for j in range(4)]
    barrier = F(1, 10**6)
    modified = [[h.Poly(4) for _ in range(4)] for _ in range(4)]
    for factor, (i, j) in zip(factors, edges):
        multiplier = barrier if signs[i] != signs[j] else F(1)
        modified[i][j] = factor*multiplier*generator[i][j]
        modified[j][i] = factor*multiplier*generator[j][i]
        require(pi[i]*modified[i][j] == pi[j]*modified[j][i]
                and min(generator[i][j], generator[j][i])*barrier*F(99, 100) > 0,
                'Symmetric edge and barrier factors preserve equilibrium flux and leave finite positive edge rates')
    for i in range(4):
        modified[i][i] = -sum(modified[i])
    require(all(sum(row) == 0 for row in modified)
            and h.mm([pi], modified) == [[F(0)]*4],
            'The complete nonselective acquisition generator preserves the low equilibrium law as an exact polynomial identity')
    opposite_rates = [sum(generator[i][j] for j in range(4) if signs[i] != signs[j])
                      for i in range(4)]
    require(max(opposite_rates) == F(9, 10) < 1
            and F(101, 100)*barrier*max(opposite_rates) <= F(101, 100)*barrier,
            'The target one-percent edge box admits the conservative sector-change rate bound 1.01*r*Gamma')
    return {'target_stationary_law_exact': list(map(str, pi)),
            'positive_barrier_factor_fixture_exact': str(barrier),
            'nominal_opposite_sector_rates_exact': list(map(str, opposite_rates)),
            'sector_change_rate_upper': '(101/100)*r*Gamma',
            'postinstrument_stationary_defect_exact': '0',
            'scope': 'Exact finite positive-rate target construction with prescribed symmetric edge factors; it neither calibrates a physical sensor nor imposes a rate cap on ordinary rivals.'}


def relative_force_certificate(h):
    a, b, z = [h.Poly.variable(3, j) for j in range(3)]
    for s in (-1, 1):
        # Let z=w_j/w_k; detailed balance gives
        # (1-su)*A=(1+su)*z*B for each off-singleton summand.
        substituted_a = (1+s*U)/(1-s*U)*z*b
        require((1-s*U)*substituted_a-(1+s*U)*b == (1+s*U)*(z-1)*b,
                'The relative-force residual has the outgoing-order representation as a symbolic identity')
        substituted_b = (1-s*U)/(1+s*U)*z*a
        require((1-s*U)*a-(1+s*U)*substituted_b == (1-s*U)*(1-z)*a,
                'The inverse force ratio supplies the complementary order representation')
        require(min(1-s*U, 1+s*U) == 1-U,
                'Both order bounds give a mass-independent prefactor 1-u for either singleton sign')
    ratio_endpoints = [1/SPREAD, SPREAD]
    require(max(abs(ratio-1) for ratio in ratio_endpoints) == SPREAD-1
            and sorted(1/ratio for ratio in ratio_endpoints) == ratio_endpoints,
            'The stipulated total relative spread controls the ratio and its reciprocal by the same defect')
    force_error = (1-U)*(SPREAD-1)
    require(force_error == F(1, 2500),
            'The one-part-in-one-thousand relative force spread gives singleton residual defect .0004')
    fixtures = []
    pi = [F(1, 5), F(3, 10), F(1, 2)]
    weights = [SPREAD, F(1), F(2001, 2000)]
    for s in (-1, 1):
        signs = [s, -s, -s]
        unnormalized = [p*(1+U*t)*weight for p, t, weight in zip(pi, signs, weights)]
        high = [value/sum(unnormalized) for value in unnormalized]
        kernels = [[[(F(i == j)+law[j])/2 for j in range(3)] for i in range(3)]
                   for law in (pi, high)]
        for kernel, law in zip(kernels, (pi, high)):
            require(all(min(row) > 0 and sum(row) == 1 for row in kernel)
                    and h.mm([law], kernel) == [law]
                    and all(law[i]*kernel[i][j] == law[j]*kernel[j][i]
                            for i, j in product(range(3), repeat=2)),
                    'The relative-force fixture has strictly positive reversible kernels and stationary laws')
        low, high_kernel = kernels
        off_a = sum(low[0][j]*high_kernel[j][0] for j in (1, 2))
        off_b = sum(high_kernel[0][j]*low[j][0] for j in (1, 2))
        actual = residual(s, low[0][0], high_kernel[0][0], h.mm(low, high_kernel)[0][0], h.mm(high_kernel, low)[0][0])
        require(0 <= off_a <= 1 and 0 <= off_b <= 1
                and actual == (1-s*U)*off_a-(1+s*U)*off_b
                and 0 < abs(actual) <= force_error,
                'Both fixture orientations obey the nonzero relative-force residual bound')
        fixtures.append({'singleton_sign': s, 'low_stationary_law_exact': list(map(str, pi)),
                         'high_stationary_law_exact': list(map(str, high)),
                         'relative_weight_values_exact': list(map(str, weights)),
                         'return_residual_exact': str(actual)})
    delta = F(9, 10000)
    gap_shift = F(22, 5)*delta/(F(1, 2)-delta)+force_error
    require(gap_shift == F(103991, 12477500) < F(9, 1000),
            'The ideal four-pair memory gap remains at least .0009 under the relative force allowance')
    n, eta = N_GROUP, F(1, 100)
    margin = F(1, 250)-F(11, 25000)-F(3, 25000)-force_error
    exponent = 2*n*margin*margin/F(28, 5)
    count_union = 8*F(3**34, 4**50)
    size_upper = exp_negative_upper(exponent)+4*exp_negative_upper(2*n*eta*eta)+count_union
    require(margin == F(19, 6250) and exponent == F(2888, 875)
            and size_upper < F(1, 25) < F(1, 20),
            'The registered test retains size below .04 with the enlarged relative-force null')
    return {'relative_weight_spread_upper_exact': str(SPREAD),
            'singleton_residual_defect_upper_exact': str(force_error),
            'relative_force_fixtures': fixtures, 'ideal_pair_TV_gap_lower_exact': str(delta),
            'TV_plus_force_residual_displacement_upper_exact': str(gap_shift),
            'registered_null_linear_margin_exact': str(margin),
            'registered_null_linear_exponent_exact': str(exponent), 'registered_null_rejection_upper_exact': '1/25',
            'stationary_mass_lower_bound_required': False,
            'scope': 'The bound concerns the ratio max(w)/min(w), not separate per-state intervals whose ratio would be squared. The target remains the exact-force kinetic family; its inherited power bound is unchanged.'}


def stationary_tv_counterexample(h):
    e = h.Poly.variable(1, 0)
    denom = 1+3*e
    # Subtract normalized tilted masses using common denominator.
    differences = [4*e-e*denom, e*denom-e, (1-2*e)*denom-(1-2*e)]
    require(differences[0] == 3*e*(1-e)
            and differences[1]+differences[2] == differences[0],
            'The normalized stationary-tilt TV numerator is exactly 3 epsilon (1-epsilon)')
    kernel = [[F(3, 4), F(1, 4), F(0)], [F(1, 4), F(3, 4), F(0)], [F(0), F(0), F(1)]]
    projector = [[F(1, 2), -F(1, 2), F(0)], [-F(1, 2), F(1, 2), F(0)], [F(0), F(0), F(0)]]
    identity = h.identity(3)
    signs, preparation = [1, -1, -1], [F(1, 2), F(1, 2), F(0)]
    require(h.mm(projector, projector) == projector
            and kernel == [[identity[i][j]-projector[i][j]/2 for j in range(3)] for i in range(3)]
            and all(sum(row) == 1 for row in kernel),
            'The equal field kernels are exp(-log(2)*A) for an idempotent A, with finite positive pair-transition rate log(2)/2')
    rows = []
    for epsilon in (F(1, 10), F(1, 1000), F(1, 10**9)):
        pi = [epsilon, epsilon, 1-2*epsilon]
        norm = sum(p*(1+U*s) for p, s in zip(pi, signs))
        tilted = [p*(1+U*s)/norm for p, s in zip(pi, signs)]
        distance = tv(pi, tilted)
        require(min(pi) > 0 and h.mm([pi], kernel) == [pi]
                and all(pi[i]*kernel[i][j] == pi[j]*kernel[j][i]
                        for i, j in product(range(3), repeat=2))
                and distance == 3*epsilon*(1-epsilon)/(1+3*epsilon) < 3*epsilon,
                'Strictly positive stationary laws and ordinary reversibility coexist with arbitrarily small absolute tilt TV')
        returns = {}
        for s in (-1, 1):
            mass = sum(p for p, sign in zip(preparation, signs) if sign == s)
            r1, r2 = [sum(preparation[i]*matrix[i][j] for i, j in product(range(3), repeat=2)
                          if signs[i] == s and signs[j] == s)/mass
                      for matrix in (kernel, h.mm(kernel, kernel))]
            require(r1 == F(3, 4) and r2 == F(5, 8)
                    and residual(s, r1, r1, r2, r2) == -s*F(3, 40),
                    'Arbitrary preparation exposes return residuals plus and minus .075 despite vanishing stationary-tilt TV')
            returns[str(s)] = str(residual(s, r1, r1, r2, r2))
        relative_weights = [1/(1+U*s) for s in signs]
        require(max(relative_weights)/min(relative_weights) == 4 > SPREAD,
                'The rare-sector counterexample is excluded by the relative-force spread condition')
        rows.append({'epsilon_exact': str(epsilon), 'stationary_law_exact': list(map(str, pi)),
                     'stationary_tilt_TV_exact': str(distance), 'return_residual_by_sign_exact': returns})
    epsilon, decay = [h.Poly.variable(2, j) for j in range(2)]
    pi_symbolic = [epsilon, epsilon, 1-2*epsilon]
    stationary_reset = [pi_symbolic[:] for _ in range(3)]
    zero = [[F(0)]*3 for _ in range(3)]
    require(h.mm(projector, stationary_reset) == zero and h.mm(stationary_reset, projector) == zero,
            'The reversible mixing generator and stationary reset commute and annihilate one another')
    irreducible_kernel = [[decay*kernel[i][j]+(1-decay)*pi_symbolic[j]
                           for j in range(3)] for i in range(3)]
    require(all(sum(row) == 1 for row in irreducible_kernel)
            and h.mm([pi_symbolic], irreducible_kernel) == [pi_symbolic]
            and all(pi_symbolic[i]*irreducible_kernel[i][j] == pi_symbolic[j]*irreducible_kernel[j][i]
                    for i, j in product(range(3), repeat=2)),
            'The irreducible perturbation propagator has exact symbolic stationarity and detailed balance')
    for s in (-1, 1):
        r1, r2 = [2*sum(preparation[i]*matrix[i][j] for i, j in product(range(3), repeat=2)
                       if signs[i] == s and signs[j] == s)
                  for matrix in (irreducible_kernel, h.mm(irreducible_kernel, irreducible_kernel))]
        value = residual(s, r1, r1, r2, r2)
        require(value.evaluate([F(0), F(1)]) == -s*F(3, 40),
                'The irreducible CTMC residual polynomial retains the same nonzero rare-sector limit')
    return {'stationary_tilt_TV_formula': '3*epsilon*(1-epsilon)/(1+3*epsilon)',
            'common_kernel_exact': [list(map(str, row)) for row in kernel],
            'preparation_exact': list(map(str, preparation)), 'fixtures': rows,
            'relative_weight_spread_exact': '4',
            'finite_pair_generator_rate': 'log(2)/2',
            'irreducible_generator_formula': 'C + epsilon*(Pi_epsilon-I)',
            'irreducible_propagator_formula': 'exp(-epsilon)*P + (1-exp(-epsilon))*Pi_epsilon',
            'limiting_return_residual_by_sign_exact': {'-1': '3/40', '1': '-3/40'},
            'scope': 'This boundary rules out a mass-uniform extension based only on absolute stationary-tilt TV. The displayed kernel is a finite-time finite-rate CTMC propagator, and the optional strictly positive-rate perturbation has the same nonzero residual limit. Every law at positive epsilon has strictly positive masses.'}


def continuous_integrator_certificate():
    normalized_time = F(32)
    noise_exponent = normalized_time/2
    noise_upper = exp_negative_upper(noise_exponent)
    jump_allowance = F(4, 10**6)
    require(noise_exponent == 16 and noise_upper < F(1, 10**6)
            and jump_allowance+noise_upper < P_STAR
            and jump_allowance/normalized_time == F(1, 8000000),
            'A thirty-two-theta continuous-martingale window and bounded jump probability meet the endpoint-error ceiling')
    reads = 2*N
    reset, active = 63*N, F(15, 8)*N
    require(reads == 18000000 and reads*normalized_time == 576000000
            and reset+active == 583875000 and B+2*P_STAR == F(89, 10**6),
            'Two integration windows per trial give eighteen million windows and the stated separated time coefficients')
    return {'noise_model': 'Continuous local martingale in the joint apparatus/system filtration',
            'signal_margin_symbol': 'g>0', 'quadratic_variation_bound_symbol': 'v*T',
            'theta_definition': 'v/g^2', 'window_duration_in_theta_exact': str(normalized_time),
            'noise_tail_exponent_exact': str(noise_exponent), 'noise_tail_upper_exact': '1/1000000',
            'sector_jump_probability_upper_exact': str(jump_allowance),
            'kappa_theta_upper_if_acquisition_equals_integration_exact': '1/8000000',
            'combined_endpoint_error_upper_exact': str(P_STAR),
            'observed_pair_TV_to_ideal_reference_upper_exact': '89/1000000',
            'total_registration_windows': reads,
            'target_reset_plus_active_attempt_units': int(reset+active),
            'total_registration_time_theta_coefficient': int(reads*normalized_time),
            'total_time_formula': '583875000/Gamma + 576000000*theta',
            'scope': 'The bound is conditional and uniform over the joint pre-window history. Leakage is bounded over the full acquisition span tau, including switching and dead time; kappa*T applies only when tau=T. No independence of readout noise, drift and hidden motion is assumed. Continuity or an explicit exponential-supermartingale substitute is necessary; predictable quadratic variation alone does not imply a Gaussian tail for jump martingales. Switching, controller and extra clock durations are additional to the displayed time total.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_endpoint_registration.json'))
    args = parser.parse_args()
    h, prior, inherited_proofs = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction arithmetic, small symbolic polynomials and positive exponential series',
              'inherited_four_word_contract': inherited_contract_certificate(prior),
              'endpoint_boundary_certificate': endpoint_boundary_certificate(h),
              'registration_sampling_certificate': registration_sampling_certificate(),
              'stationary_barrier_certificate': stationary_barrier_certificate(h),
              'relative_force_certificate': relative_force_certificate(h),
              'absolute_stationary_TV_counterexample': stationary_tv_counterexample(h),
              'continuous_integrator_certificate': continuous_integrator_certificate(),
              'rival_preparation_promise_required': False, 'null_initial_sign_preservation_required': False,
              'symmetric_detector_required': False, 'fixed_detector_error_probability_required': False,
              'temporal_detector_independence_required': False, 'known_conditional_registration_bound_required': True,
              'active_model_and_controls_fixed_required': True, 'disagreement_gates_used': False,
              'device_feasibility_claimed': False, 'full_transcript_state_count_claimed': False,
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': INPUTS, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**inherited_proofs, **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
