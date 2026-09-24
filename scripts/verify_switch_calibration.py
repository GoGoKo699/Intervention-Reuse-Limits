#!/usr/bin/env python3
"""Exact calibration, preparation, timing and sampling certificates for switches.

The frozen finite-margin verifier supplies reviewed polynomial arithmetic and
certified target centers. This verifier adds a nine-variable error box, an
approximate-Gibbs residual band, physical error budgets and exact log bounds.
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
FROZEN_REPORT = 'reports/familiar_switch_margin.json'
FROZEN_REPORT_SHA256 = 'dfe9757f74a6fc2d45f239e65292cfc613f913685f895896a9b229cc16067141'
HELPER = 'verify_familiar_switch_margin.py'
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_frozen_inputs():
    payload = (ROOT/FROZEN_REPORT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == FROZEN_REPORT_SHA256,
            'The inherited target certificate is exactly the independently reviewed frozen report')
    report = json.loads(payload)
    require(report['status'] == 'PASS', 'The inherited exact certificate passed')
    helper_path = ROOT/'scripts'/HELPER
    require(hashlib.sha256(helper_path.read_bytes()).hexdigest() == report['source_sha256'][HELPER],
            'The imported polynomial helper matches the frozen source snapshot')
    for name, digest in report['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'Each inherited proof still matches its frozen certificate snapshot')
    spec = importlib.util.spec_from_file_location('frozen_switch_margin', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    centers = list(map(F, report['certified_target_margin']['target_mean_centers_exact']))
    require(len(centers) == 7 and report['certified_target_margin']['target_mean_uniform_enclosure_radius'] == '2^-120',
            'The inherited seven rational centers have the specified certified mean enclosure')
    return helper, report, centers


def calibrated_polynomials(helper):
    variables = [helper.Poly.variable(9, i) for i in range(9)]
    m, n, p, l1, l2, k1, k2, b, u = variables
    numerator = b+u-m
    second = b+u-(1-u*u)*n
    table = [[1, b, m], [1, m, n], [1, n, p]]
    shifted_table = [[1, b, m], [1, l1, k1], [1, l2, k2]]
    adjugate_product = helper.mm(helper.adjugate(table), shifted_table)
    polynomials = {}
    for sign in (-1, 1):
        denominator = u*(1+sign*b)*(1-sign*u)
        covariance = (1+sign*b)*(1-sign*u)*numerator
        raw_second = (1+sign*b)*second-sign*(u*m+sign*numerator)**2
        gram = [[denominator, denominator*b, denominator*m],
                [denominator*b, denominator, covariance],
                [denominator*m, covariance, raw_second]]
        matrix = helper.mm(gram, adjugate_product)
        polynomial = matrix[1][2]-matrix[2][1]
        require(len(polynomial.terms) == 182 and max(map(sum, polynomial.terms)) == 7,
                'The cleared nine-variable necessary identity has 182 monomials and total degree seven')
        require(max(sum(powers[:7]) for powers in polynomial.terms) == 4,
                'The calibrated identity remains quartic in its seven response variables')
        # Check the unbiased reduction with a symbolic, rather than sampled, u.
        x = [helper.Poly.variable(8, i) for i in range(8)]
        mm, nn, pp, ll1, ll2, kk1, kk2, uu = x
        a1, a2 = (pp-mm)*ll1-(nn-mm)*ll2, -nn*ll1+mm*ll2
        b1, b2 = (pp-mm)*(kk1-mm)-(nn-mm)*(kk2-mm), -nn*(kk1-mm)+mm*(kk2-mm)
        scaled_variance = uu-(1-uu*uu)*nn-sign*(uu*mm+sign*(uu-mm))**2-uu*(1-sign*uu)*mm*mm
        unbiased = (1-sign*uu)*(uu*b1+(uu-mm)*b2-(uu-mm)*a1)-scaled_variance*a2
        require(polynomial.substitute(x[:7]+[F(0), uu]) == unbiased,
                'Setting baseline bias to zero gives u times the former witness as a formal polynomial')
        y = [helper.Poly.variable(7, i) for i in range(7)]
        require(polynomial.substitute(y+[F(0), F(4, 5)]) == F(4, 5)*helper.response_polynomial(sign, F(4, 5)),
                'The calibrated polynomial specializes exactly to the frozen numerical witness')
        polynomials[sign] = polynomial
    return polynomials, adjugate_product


def reversible_matrix(helper, law, fluxes):
    n = len(law)
    matrix = helper.identity(n)
    for (i, j), flux in zip(((0, 1), (0, 2), (1, 2)) if n == 3 else ((0, 1),), fluxes):
        matrix[i][j], matrix[j][i] = flux/law[i], flux/law[j]
        matrix[i][i] -= flux/law[i]
        matrix[j][j] -= flux/law[j]
    require(all(sum(row) == 1 for row in matrix) and min(value for row in matrix for value in row) > 0,
            'The independent fixture is a positive stochastic matrix')
    require(all(law[i]*matrix[i][j] == law[j]*matrix[j][i] for i, j in product(range(n), repeat=2)),
            'The fixture satisfies exact detailed balance for its stated stationary law')
    return matrix


def approximate_tilt_band(sign, b, u, tau, diagonal_bound, lower_bound):
    q, z = 1+sign*b, 1+u*b
    denominator = u*q*(1-sign*u)
    d = 4*z*tau/u
    return abs(denominator)*diagonal_bound*d+lower_bound*(
        u*q*z*(3+4/u)*tau+u*u*(2*q+d)*d)


def biased_kernel_fixtures(helper, polynomials, adjugate_product):
    b, u, tau = F(1, 7), F(2, 3), F(1, 100000)
    for sign in (-1, 1):
        readout = [F(sign), -F(sign), -F(sign)]
        singleton_mass = (1+sign*b)/2
        law0 = [singleton_mass, (1-singleton_mass)*F(2, 3), (1-singleton_mass)/3]
        tilted = [weight*(1+u*s)/(1+u*b) for weight, s in zip(law0, readout)]
        require(sum(tilted) == 1 and sum(x*s for x, s in zip(law0, readout)) == b,
                'The biased baseline and normalized Gibbs tilt have the claimed interpretation')
        zero = reversible_matrix(helper, law0, [F(1, 100), F(1, 120), F(1, 150)])
        for defect in (F(0), tau):
            high_law = tilted[:]
            high_law[1] += defect
            high_law[2] -= defect
            require(sum(abs(a-c) for a, c in zip(high_law, tilted))/2 == defect,
                    'The high-field stationary-law perturbation has exactly the requested total variation')
            high = reversible_matrix(helper, high_law, [F(1, 400), F(1, 500), F(1, 600)])
            responses = helper.words_from_matrices([zero, high], law0, readout)
            values = responses+[b, u]
            actual = polynomials[sign].evaluate(values)
            diagonal = abs((adjugate_product[2][2]-adjugate_product[1][1]).evaluate(values))
            lower = abs(adjugate_product[2][1].evaluate(values))
            band = approximate_tilt_band(sign, b, u, defect, diagonal, lower)
            require(abs(actual) <= band,
                    'The exact biased reversible fixture satisfies the approximate-tilt residual inequality')
            if not defect:
                require(actual == 0, 'The necessary identity vanishes exactly when the Gibbs tilt is exact')
        # An independent mixture of clock kernels preserves the same laws and identity.
        high = reversible_matrix(helper, tilted, [F(1, 400), F(1, 500), F(1, 600)])
        mixed = []
        for matrix in (zero, high):
            squared = helper.mm(matrix, matrix)
            mixed.append([[F(2, 5)*x+F(3, 5)*y for x, y in zip(a, c)] for a, c in zip(matrix, squared)])
        values = helper.words_from_matrices(mixed, law0, readout)+[b, u]
        require(polynomials[sign].evaluate(values) == 0,
                'An independently sampled clock mixture preserves the reversible necessary identity')
    law0 = [(1+b)/2, (1-b)/2]
    tilted = [law0[0]*(1+u)/(1+u*b), law0[1]*(1-u)/(1+u*b)]
    matrices = [reversible_matrix(helper, law, [F(1, 100)]) for law in (law0, tilted)]
    values = helper.words_from_matrices(matrices, law0, [F(1), -F(1)])+[b, u]
    require(all(polynomial.evaluate(values) == 0 for polynomial in polynomials.values()),
            'Both necessary identities include the singular biased two-state case')


def box_certificate(helper, centers, polynomials, adjugate_product):
    center = centers+[F(0), F(4, 5)]
    radii = [F(1, 1250)+F(1, 2**120)]*7+[F(1, 10000)]*2

    def shifted_mass(polynomial, omit_constant=False):
        shifted = polynomial.shifted(center)
        return sum(abs(coefficient)*helper.product_value(radius**power for radius, power in zip(radii, powers))
                   for powers, coefficient in shifted.terms.items() if not omit_constant or sum(powers))

    diagonal_bound = shifted_mass(adjugate_product[2][2]-adjugate_product[1][1])
    lower_bound = shifted_mass(adjugate_product[2][1])
    require(diagonal_bound < F(10854, 10**6) and lower_bound < F(19084, 10**6),
            'Exact local polynomial boxes bound the two adjugate-product entries used by the tilt residual')
    umin, umax, qmax = F(7999, 10000), F(8001, 10000), F(10001, 10000)
    zmax, tau = 1+umax/F(10000), F(1, 100000)
    dmax = 4*zmax*tau/umin
    reports = {}
    for sign, polynomial in polynomials.items():
        shifted = polynomial.shifted(center)
        require(len(shifted.terms) == 289, 'The exact translated calibration polynomial has the expected support')
        constant = shifted.terms[(0,)*9]
        require(constant == polynomial.evaluate(center) and abs(constant) > F(1164, 10**7),
                'The certified center has the stated nonzero polynomial magnitude')
        variation = shifted_mass(polynomial, omit_constant=True)
        public_variation = F(914 if sign == -1 else 272, 10**7)
        require(variation < public_variation and abs(constant)-variation > F(1, 40000),
                'Every point in the nine-variable box has the stated exact-tilt nonzero margin')
        denominator_max = umax*qmax*(1+umax if sign == -1 else 1-umin)
        band = denominator_max*diagonal_bound*dmax+lower_bound*(
            umax*qmax*zmax*(3+4/umin)*tau+umax**2*(2*qmax+dmax)*dmax)
        require(band < F(1, 300000),
                'The entire allowed approximate-Gibbs residual band is below the public rational bound')
        require(abs(constant)-variation-band > F(13, 600000),
                'The necessary approximate identity remains impossible everywhere in the full calibrated box')
        reports[str(sign)] = {'center_absolute_lower_exact': str(F(1164, 10**7)),
                              'whole_box_variation_upper_exact': str(public_variation),
                              'exact_tilt_slack_lower_exact': '1/40000',
                              'approximate_tilt_residual_upper_exact': '1/300000',
                              'remaining_polynomial_slack_lower_exact': '13/600000'}
    return {'variable_order': ['mH', 'mHH', 'mHHH', 'mH0', 'mHH0', 'mH0H', 'mHH0H', 'stationary_baseline_mean', 'tanh_field_increment'],
            'mean_radius_about_nominal_target_exact': '1/1250',
            'inherited_target_center_mean_radius': '2^-120',
            'baseline_mean_absolute_bound_exact': '1/10000',
            'tanh_field_increment_center_exact': '4/5',
            'tanh_field_increment_radius_exact': '1/10000',
            'approximate_Gibbs_stationary_TV_bound_exact': '1/100000',
            'nominal_occupation_error_exclusion_exact': '1/2500',
            'adjugate_diagonal_difference_absolute_upper_exact': str(F(10854, 10**6)),
            'adjugate_lower_entry_absolute_upper_exact': str(F(19084, 10**6)),
            'sign_certificates': reports,
            'scope': 'This exact local box excludes both necessary approximate-Gibbs residual bands. The analytic stationary-law and reversibility argument supplies the universal connection to arbitrary ordinary rivals; baseline bias is not a substitute for controlling nonstationary preparation.'}


def positive_three_state_extension(helper):
    t, low, high = F(4, 5), -F(1, 10000), F(9, 10)
    m = helper.Poly.variable(1, 0)
    denominator = 1-t*t*m*m
    a_bar, b_bar = (1-t*t)*m, t*(1-m*m)
    l_bar = (1-t*t)*(1+m)/2
    q21_bar = (denominator-a_bar+2*t*b_bar)/2
    q31_bar = (1-t*t)*(1-m)**2/4
    require(q21_bar == (1-m)*(57+48*m)/50,
            'The potentially delicate return rate has an exact positive numerator factorization')
    q = [[0, F(73, 105)*l_bar, F(32, 105)*l_bar],
         [q21_bar, 0, F(32, 105)*(3*denominator-q21_bar)],
         [q31_bar, (9*denominator-73*q31_bar)/105, 0]]
    for i in range(3):
        q[i][i] = -sum(q[i])
    readout = [-F(1), F(1), F(1)]
    auxiliary = [-t, -2*t, (1+t*t)/(2*t)]
    coordinates = [[F(1), s, z] for s, z in zip(readout, auxiliary)]
    reduced = [[0, a_bar, 0], [0, -denominator, t*denominator], [0, b_bar, -denominator]]
    require(helper.mm(q, coordinates) == helper.mm(coordinates, reduced),
            'Clearing the common positive denominator gives exact three-state mean closure for a symbolic field')
    d, e = 3*t, (1-t*t)/(2*t)
    law0 = [F(1, 2), e/(2*(d+e)), d/(2*(d+e))]
    law = [weight*(1+m*s) for weight, s in zip(law0, readout)]
    require(sum(law) == 1 and all(value == 0 for value in helper.mm([law], q)[0]),
            'The Gibbs-tilted three-state law is exactly stationary for the symbolic field family')
    require(helper.mm([law], coordinates) == [[1, m, t*m]],
            'The predictor and physical equilibrium preparation share both closed mean coordinates')
    require(1-t*t*high*high > 0 and 1+low > 0 and 1-high > 0 and 57+48*low > 0,
            'All denominator and factored-rate sign conditions hold on the complete field interval')
    q21_upper = (1-low+2*t*t)/2
    require(q21_upper < F(3, 2), 'The first return rate is uniformly below three halves on the field interval')
    q31_upper = F(9, 100)*(1-low)**2/(1-t*t*low*low)
    require((1+t*t)*high < 2 and q31_upper < F(91, 1000),
            'Positive and negative fields give a common uniform upper bound for the second return rate')
    require(9-73*q31_upper > 0 and 3-q21_upper > 0,
            'The two internal transition rates have positive numerators on the full interval')
    l_upper = (1-t*t)*(1+high)/(2*(1-t*t*high*high))
    require(l_upper < 1 and F(96, 105)+F(73, 105)*q21_upper < 2
            and F(9, 105)+F(32, 105)*q31_upper < 1,
            'The extended positive predictor retains total exit rates below two')
    eps = F(1, 100000)
    require(low < -eps and t+eps < high and 2*eps < F(1, 10000),
            'Both perturbed physical fields and their force increment lie within the certified domains')
    return {'tanh_field_interval_exact': [str(low), str(high)], 'total_states': 3,
            'strict_total_exit_cap': 2,
            'scope': 'The positive generator family matches the physical target exactly from corresponding stationary preparations, including the slightly negative low field. For target preparation within TV epsilon_p of equilibrium, only an occupation-error upper bound epsilon_p is inferred.'}


def physical_budget_and_reset(helper):
    eps_p = eps_h = eps_t = F(1, 100000)
    low_rate_lipschitz = F(9, 50)/(1-F(4, 5)*F(1, 8))
    require(low_rate_lipschitz == F(1, 5),
            'The low-field finite-difference bound, rather than a pointwise derivative bound, has constant one fifth')
    require(eps_h < F(1, 8) and F(1, 5)+3*F(1, 2) == F(17, 10),
            'The seven-word menu has the stated combined low/high field-defect coefficient')
    require(max(sum(word) for word in helper.WORDS) == 3
            and max(len(word)-sum(word) for word in helper.WORDS) == 1,
            'The actual fixed menu contains at most three high-field ticks and one zero-field tick')
    require(F(9, 10)+3*F(81, 82) == F(792, 205),
            'The nominal per-spin timing constants sum to the stated four-tick coefficient')
    t, high_b = F(4, 5), F(20, 41)
    require(0 < high_b <= t < 1,
            'The cooperative mean systems have nonnegative off-diagonals and nonincreasing coefficient mass')
    displacement = 2*eps_p+eps_h/2+(2+eps_t)*F(17, 10)*eps_h+F(792, 205)*eps_t
    require(displacement < F(1, 10000), 'The exact combined target and rival preparation/calibration/timing budget is below one ten-thousandth')
    require(F(1, 2500)-displacement > F(3, 10000),
            'The actual calibrated occupation separation exceeds three ten-thousandths')
    require(eps_p < F(3, 10000), 'The prepared three-state upper and four-state lower leave a nonempty tolerance interval')

    pi_min = (1-eps_h)/20
    exponential_argument = F(124, 5)
    term = total = F(1)
    for j in range(1, 65):
        term *= exponential_argument/j
        total += term
    require(1/pi_min-1 < 4*eps_p*eps_p*total,
            'A positive rational exponential partial sum certifies the squared 62-unit reset TV bound')
    require(1-t == F(1, 5) and 20*pi_min == 1-eps_h,
            'The reset constants use the physical gap and stationary-mass lower bound')
    term = nominal_exponential_lower = F(1)
    for j in range(1, 33):
        term *= F(11, j)
        nominal_exponential_lower += term
    require(nominal_exponential_lower > 55000,
            'The nominal 55-unit preparation bound (11/20) exp(-11) is below one hundred-thousandth')
    return {'preparation_TV_tolerance_exact': str(eps_p), 'field_error_tolerance_exact': str(eps_h),
            'per_tick_time_error_tolerance_exact': str(eps_t),
            'combined_occupation_displacement_exact': str(displacement),
            'combined_displacement_upper_exact': '1/10000',
            'actual_occupation_separation_lower_exact': '3/10000',
            'minimum_state_count_tolerance_interval_exact': ['1/100000', '3/10000'],
            'reset_actual_wait_lower_exact': '62', 'reset_stationary_mass_lower_exact': str(pi_min),
            'reset_spectral_gap_lower_exact': '1/5', 'reset_exponential_lower_bound_degree': 64,
            'nominal_reset_actual_wait_lower_exact': '55', 'nominal_reset_exponential_lower_bound_degree': 32,
            'scope': 'These are exact arithmetic checks of the analytic perturbation and mixing bounds, not an exhaustive verification of all time-dependent physical protocols. The reset bound concerns the physical target; no finite universal reset wait is inferred for uncapped rivals.'}


def ceil_fraction(value):
    return -((-value.numerator)//value.denominator)


def log_enclosure(helper, ratio, terms=32):
    x = (ratio-1)/(ratio+1)
    require(0 <= x < 1, 'The logarithm range reduction has a convergent positive atanh series')
    lower = 2*sum(x**(2*j+1)/F(2*j+1) for j in range(terms))
    tail = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return helper.Interval(lower, lower+tail)


def sampling_checks(helper, frozen, centers):
    require(F(2)**8*F(35, 32) == 280 and F(2)**4*F(19, 16) == 19,
            'The rational logarithm range reductions are exact')
    log_two = log_enclosure(helper, F(2))
    log_280 = 8*log_two+log_enclosure(helper, F(35, 32))
    log_19 = 4*log_two+log_enclosure(helper, F(19, 16))
    require(log_280.hi-log_280.lo < F(1, 10**30) and log_19.hi-log_19.lo < F(1, 10**30),
            'The logarithm intervals are narrow enough to determine all stated sample ceilings')
    cases = []
    for label, separation, readout_bias, model_error, expected in (
            ('nominal', F(1, 2000), F(0), F(0), 45078317),
            ('calibrated', F(3, 10000), F(0), F(0), 125217547),
            ('calibrated_with_model_error', F(3, 10000), F(0), F(1, 10000), 281739481),
            ('nominal_with_additional_bias', F(1, 2000), F(1, 100000), F(0), 48913105)):
        gap = separation-2*readout_bias-model_error-F(1, 2**120)
        require(gap > 0, 'The statistical separation remains positive after both reference-center errors and specified tolerances')
        lower = 2*log_280.lo/(gap*gap)
        upper = 2*log_280.hi/(gap*gap)
        require(ceil_fraction(lower) == ceil_fraction(upper) == expected,
                'Exact log intervals determine the published sufficient per-word sample ceiling')
        require(F(expected)*gap*gap/2 >= log_280.hi
                and F(expected-1)*gap*gap/2 < log_280.lo,
                'The reported integer is precisely the ceiling of the conservative Hoeffding formula')
        cases.append({'case': label, 'occupation_separation_exact': str(separation),
                      'additional_occupation_bias_bound_exact': str(readout_bias), 'model_error_allowance_exact': str(model_error),
                      'sufficient_trials_per_word': expected, 'sufficient_trials_total_seven_words': 7*expected})

    require(frozen['rational_ordinary_three_state_upper_witness']['certified_uniform_occupation_error_upper'] == '1/1000',
            'The information lower bound uses the frozen same-menu ordinary witness')
    upper_errors = list(map(F, frozen['rational_ordinary_three_state_upper_witness']['occupation_error_outward_upper_by_word_exact']))
    require(max(upper_errors) < F(837, 10**6), 'Every frozen witness discrepancy is smaller than the certified KL input bound')
    probability_error = F(1, 2**121)
    for center, error in zip(centers, upper_errors):
        p = (1+center)/2
        require(F(1, 8) < p-probability_error-error and p+probability_error+error < F(7, 8),
                'Both target and explicit witness Bernoulli probabilities lie in the certified interior interval')
    kl_upper = F(32, 7)*F(837, 10**6)**2
    require(kl_upper < F(1, 300000), 'The Bernoulli divergence upper bound is below one over three hundred thousand')
    expected_lower = 270000*log_19
    require(ceil_fraction(expected_lower.lo) == ceil_fraction(expected_lower.hi) == 794999,
            'The information bound implies the stated integer lower count for a fixed total sample size')
    require(expected_lower.lo > F(794998524, 1000),
            'The adaptive expected-sample lower bound has the stated outward rational lower endpoint')
    durations = [2*len(word) for word in helper.WORDS]
    require(sum(durations) == 36 and sum(len(word) for word in helper.WORDS) == 18 and max(durations) == 8,
            'The seven experiments have the stated nominal duration and tick totals')
    nominal_exposure = (36+7*55)*48913105
    robust_exposure = (F(36)+F(18, 100000)+7*62)*125217547
    require(nominal_exposure == 20592417205 and robust_exposure < 58852270000,
            'The stated serial preparation-plus-protocol exposures include all seven waits and actual tick uncertainty')
    return {'type_I_error_bound_exact': '1/20', 'type_II_error_bound_exact': '1/20',
            'target_probability_center_error': '2^-121',
            'sufficient_count_gap_correction': '2^-120',
            'logarithm_certificate': {'method': 'Positive atanh series with rational range reduction and geometric tail',
                                      'terms_per_reduced_log': 32, 'uniform_interval_width_upper': '1/10^30'},
            'sufficient_sample_counts': cases,
            'per_observation_KL_upper_exact': str(kl_upper),
            'fixed_integer_total_trials_lower': 794999,
            'adaptive_expected_total_trials_strict_lower_exact': '270000*log(19)',
            'adaptive_expected_total_trials_outward_lower_exact': str(F(794998524, 1000)),
            'nominal_sum_word_durations_exact': '36',
            'calibrated_sum_word_durations_upper_exact': str(F(36)+F(18, 100000)),
            'nominal_55_wait_example_serial_exposure_exact': str(nominal_exposure),
            'calibrated_62_wait_example_serial_exposure_upper_exact': str(robust_exposure),
            'scope': 'The analytic testing argument supplies the concentration and adaptive-information inequalities. These exact checks certify their numerical constants and distinguish integer trial counts from a real-valued expected stopping time. The lower bound uses the nominal target and frozen explicit ordinary witness on this seven-word menu; it is not a lower bound for every possible experiment design.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_calibration.json'))
    args = parser.parse_args()
    helper, frozen, centers = load_frozen_inputs()
    polynomials, adjugate_product = calibrated_polynomials(helper)
    biased_kernel_fixtures(helper, polynomials, adjugate_product)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction polynomial algebra, certified coefficient boxes, rational exponential lower sums and rational logarithm enclosures',
              'calibration_box': box_certificate(helper, centers, polynomials, adjugate_product),
              'positive_three_state_extension': positive_three_state_extension(helper),
              'physical_transfer_and_reset': physical_budget_and_reset(helper),
              'sampling': sampling_checks(helper, frozen, centers),
              'largest_dense_matrix_dimension': 3, 'floating_arithmetic_used': False,
              'numerical_optimization_used': False,
              'limitations': ['The exact box computation is an essential computer-assisted premise; the all-rival residual identity, perturbation and statistical arguments are analytic.',
                              'Baseline bias refers to a stationary law. Preparation errors are separate total-variation assumptions.',
                              'A fixed propagator per field or independent identically distributed timing mixtures are covered; correlated occurrence-dependent drift is not automatically covered.',
                              'The rational stochastic-kernel fixtures test algebra and are not claimed to be continuous-time exponential realizations.',
                              'The finite physical reset wait supplies a target preparation guarantee, not a universal preparation procedure for arbitrary uncapped rivals.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                HELPER: hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest()},
              'input_report_sha256': {FROZEN_REPORT: FROZEN_REPORT_SHA256},
              'proof_snapshot_sha256': {
                  name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                  for name in ('docs/FAMILIAR_SWITCH_CALIBRATION.md',
                               'docs/FAMILIAR_SWITCH_MEASUREMENT_COST.md',
                               'docs/FAMILIAR_SWITCH_FINITE_MARGIN.md',
                               'docs/FAMILIAR_SWITCH_STRUCTURE.md')
              },
              'imported_repository_verifiers': [HELPER]}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
