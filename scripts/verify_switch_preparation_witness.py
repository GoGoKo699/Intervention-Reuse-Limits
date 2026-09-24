#!/usr/bin/env python3
"""Exact four-mean witness with two stationary preparations for coupled switches.

The certificate uses rational physical generators, reviewed exact exponential
enclosures, and a bilinear response identity. It contains no floating arithmetic
or optimization and does not modify any preceding certificate.
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
INPUT_REPORT = 'reports/familiar_switch_margin.json'
INPUT_REPORT_SHA256 = 'dfe9757f74a6fc2d45f239e65292cfc613f913685f895896a9b229cc16067141'
CHECKS = 0
PROTOCOLS = ((0, (1,)), (1, (0,)), (1, (0, 1)), (0, (1, 0)))


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_helper():
    payload = (ROOT/INPUT_REPORT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_REPORT_SHA256,
            'The imported exponential arithmetic is identified by the frozen reviewed certificate')
    frozen = json.loads(payload)
    source = ROOT/'scripts'/HELPER
    require(hashlib.sha256(source.read_bytes()).hexdigest() == frozen['source_sha256'][HELPER],
            'The imported helper source agrees with its frozen snapshot')
    for name, digest in frozen['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'The inherited proof snapshot remains unchanged')
    spec = importlib.util.spec_from_file_location('frozen_four_mean_arithmetic', source)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper


def response_polynomial(helper, sign, u):
    m, a, b, l = [helper.Poly.variable(4, i) for i in range(4)]
    return b-m-a+l+sign*(u*l-a*m)


def symbolic_checks(helper):
    m, a, b, l, u = [helper.Poly.variable(5, i) for i in range(5)]
    for sign in (-1, 1):
        u_singleton_value = u*m+sign*(u-m)
        require(1-u_singleton_value == (1-sign*u)*(1+sign*m),
                'The singleton conditional value gives the exact force-dependent factor')
        inner_product_identity = (1-u*u)*l-(1-u_singleton_value)*a+(1-sign*u)*(b-m)
        witness = b-m-a+l+sign*(u*l-a*m)
        require(inner_product_identity == (1-sign*u)*witness,
                'The cleared inner-product identity factors into the claimed four-mean polynomial')
        f = [helper.Poly.variable(3, i) for i in range(3)]
        for readout, value in zip((sign, -sign, -sign), f):
            require(readout*value == -sign*value+sign*f[0]*(1+sign*readout),
                    'The singleton-sector pointwise product identity holds for arbitrary function values')


def four_responses(helper, matrices, laws, readout):
    responses = []
    for preparation, word in PROTOCOLS:
        row = [laws[preparation]]
        for field in word:
            row = helper.mm(row, matrices[field])
        responses.append(sum(x*s for x, s in zip(row[0], readout)))
    return responses


def reversible_clock(helper, law, fluxes):
    matrix = helper.identity(len(law))
    pairs = ((0, 1), (0, 2), (1, 2)) if len(law) == 3 else ((0, 1),)
    for (i, j), flux in zip(pairs, fluxes):
        matrix[i][j], matrix[j][i] = flux/law[i], flux/law[j]
        matrix[i][i] -= flux/law[i]
        matrix[j][j] -= flux/law[j]
    require(all(sum(row) == 1 for row in matrix) and min(value for row in matrix for value in row) > 0,
            'The algebra fixture is a strictly positive stochastic matrix')
    require(all(law[i]*matrix[i][j] == law[j]*matrix[j][i]
                for i, j in product(range(len(law)), repeat=2)),
            'The algebra fixture is reversible for its own preparation law')
    return matrix


def reversible_fixture_checks(helper, u, polynomials):
    for sign in (-1, 1):
        readout = [F(sign), -F(sign), -F(sign)]
        low_law = [F(1, 2), F(1, 3), F(1, 6)]
        high_law = [weight*(1+u*s) for weight, s in zip(low_law, readout)]
        zero = reversible_clock(helper, low_law, [F(1, 100), F(1, 120), F(1, 150)])
        high = reversible_clock(helper, high_law, [F(1, 400), F(1, 500), F(1, 600)])
        values = four_responses(helper, [zero, high], [low_law, high_law], readout)
        require(polynomials[sign].evaluate(values) == 0,
                'The necessary identity vanishes on an independently constructed reversible singleton fixture')
        require(polynomials[-sign].evaluate(values) != 0,
                'The fixture distinguishes the two possible singleton readout signs')
        f = [row[0] for row in helper.mm(high, [[s] for s in readout])]
        m = sum(weight*value for weight, value in zip(low_law, f))
        covariance = sum(weight*s*value for weight, s, value in zip(low_law, readout, f))
        require(covariance == 1-m/u and f[0] == m+sign*covariance,
                'Stationarity and the singleton sector give the conditional function value used in the proof')
        adjoint_one = [sum(low_law[j]*high[j][i] for j in range(3))/low_law[i] for i in range(3)]
        require(adjoint_one == [(1+u*s)*(1-u*value)/(1-u*u) for s, value in zip(readout, f)],
                'The high-field adjoint acting on the constant obeys the exact change-of-measure identity')
    laws = [[F(1, 2), F(1, 2)], [(1+u)/2, (1-u)/2]]
    matrices = [reversible_clock(helper, law, [F(1, 100)]) for law in laws]
    values = four_responses(helper, matrices, laws, [F(1), -F(1)])
    require(all(polynomial.evaluate(values) == 0 for polynomial in polynomials.values()),
            'Both singleton identities include the two-state degeneracy')


def exact_three_state_upper(helper, t, u, target_generators, target_laws):
    readout = [-F(1), F(1), F(1)]
    auxiliary = [-t, -2*t, (1+t*t)/(2*t)]
    coordinates = [[F(1), s, z] for s, z in zip(readout, auxiliary)]
    target_coordinates = [[F(1), F(s), F(z)] for s, z in product((-1, 1), repeat=2)]
    d, e = 3*t, (1-t*t)/(2*t)
    width = d+e
    law0 = [F(1, 2), e/(2*width), d/(2*width)]
    generators, laws = [], []
    for field, tanh_field in enumerate((F(0), u)):
        denominator = 1-t*t*tanh_field*tanh_field
        a, b = tanh_field*(1-t*t)/denominator, t*(1-tanh_field*tanh_field)/denominator
        first_exit = (1+a-b*t)/2
        q21, q31 = (1-a+2*b*t)/2, (1-a-b*(t+e))/2
        q = [[F(0), first_exit*(2*t+e)/width, first_exit*(d-2*t)/width],
             [q21, F(0), (d+q21*(2*t-d))/width],
             [q31, (e-q31*(2*t+e))/width, F(0)]]
        for i in range(3):
            q[i][i] = -sum(q[i])
        law = [weight*(1+tanh_field*s) for weight, s in zip(law0, readout)]
        reduced = [[F(0), a, F(0)], [F(0), -F(1), t], [F(0), b, -F(1)]]
        require(all(q[i][j] > 0 for i, j in product(range(3), repeat=2) if i != j)
                and max(-q[i][i] for i in range(3)) < 2,
                'The exact smaller predictor has strictly positive rates and total exit rates below two')
        require(helper.mm([law], q) == [[F(0)]*3] and sum(law) == 1 and min(law) > 0,
                'Each stated predictor preparation is exactly stationary')
        require(helper.mm(q, coordinates) == helper.mm(coordinates, reduced)
                and helper.mm(target_generators[field], target_coordinates) == helper.mm(target_coordinates, reduced),
                'Physical target and predictor have the same exact mean generators at both fields')
        require(helper.mm([law], coordinates) == helper.mm([target_laws[field]], target_coordinates),
                'Both stationary preparations give the same complete set of closed mean coordinates')
        generators.append(q)
        laws.append(law)
    require(any(laws[0][i]*generators[0][i][j] != laws[0][j]*generators[0][j][i]
                for i, j in product(range(3), repeat=2)),
            'The exact smaller predictor does not satisfy ordinary detailed balance at zero field')
    for sign in (-1, 1):
        predictor_mass = sum(weight for weight, s in zip(law0, readout) if s == sign)
        target_mass = sum(weight for weight, row in zip(target_laws[0], target_coordinates) if row[1] == sign)
        predictor_conditional = [sum(weight*row[j] for weight, row in zip(law0, coordinates)
                                     if row[1] == sign)/predictor_mass for j in range(3)]
        target_conditional = [sum(weight*row[j] for weight, row in zip(target_laws[0], target_coordinates)
                                  if row[1] == sign)/target_mass for j in range(3)]
        require(predictor_mass == target_mass == F(1, 2)
                and predictor_conditional == target_conditional == [F(1), F(sign), t*sign],
                'Conditioning on either initial readout gives the same closed mean coordinates in target and predictor')
    return {'total_states': 3, 'readout_exact': [str(x) for x in readout],
            'stationary_preparations_exact': [[str(x) for x in law] for law in laws],
            'generators_exact': [[[str(x) for x in row] for row in q] for q in generators],
            'scope': 'The exact common mean closure and matching initial coordinates at both equilibria imply identical controlled means for either preparation. This does not claim equality of observed path laws.'}


def snapshot_corollary_checks(helper, u):
    readout = [-F(1), F(1), F(1)]
    laws = [[F(1, 2), F(1, 3), F(1, 6)]]
    laws.append([weight*(1+u*s) for weight, s in zip(laws[0], readout)])
    matrices = [reversible_clock(helper, laws[0], [F(1, 100), F(1, 120), F(1, 150)]),
                reversible_clock(helper, laws[1], [F(1, 400), F(1, 500), F(1, 600)])]
    m, a, b, l = four_responses(helper, matrices, laws, readout)
    for word, plain, weighted in (((0, 1), m, b), ((1, 0), l, a)):
        kernel = helper.mm(matrices[word[0]], matrices[word[1]])
        final_means = [sum(row[j]*readout[j] for j in range(3)) for row in kernel]
        require(sum(weight*value for weight, value in zip(laws[0], final_means)) == plain
                and sum(weight*(1+u*s)*value for weight, s, value in zip(laws[0], readout, final_means)) == weighted,
                'Each pair of four-mean measurements is recovered by unweighted or Gibbs-weighted initial/final snapshots')
    require(F(9, 5000)/(1+u) == F(1, 1000),
            'The four-mean occupation separation gives the claimed two-snapshot joint-law TV separation')
    return {'stationary_preparation_field': 0, 'chronological_words': [[0, 1], [1, 0]],
            'observations_per_run': 'initial and final binary readouts',
            'joint_law_TV_separation_lower_exact': '1/1000',
            'scope': 'This corollary assumes exact stationary preparation and exact Gibbs tilt. The three-state construction matches these two-time joint laws by the separately checked conditional initial coordinates. No full trajectory, calibrated snapshot or snapshot sample-count claim is made.'}


def target_certificate(helper, t, u, clock, polynomials):
    q0, law0, readout = helper.physical_generator(t, F(0))
    qh, law_high, _ = helper.physical_generator(t, u)
    e0, certificate0 = helper.exponential_enclosure(q0, clock)
    eh, certificate_high = helper.exponential_enclosure(qh, clock)
    values = four_responses(helper, [e0, eh], [law0, law_high], readout)
    centers = [helper.round_dyadic((value.lo+value.hi)/2, 128) for value in values]
    require(all(max(abs(value.lo-center), abs(value.hi-center)) < F(1, 2**120)
                for value, center in zip(values, centers)),
            'The four physical target means lie within 2^-120 of the stated rational centers')
    require(all(0 < value.lo < value.hi < 1 for value in values),
            'All target means lie strictly between zero and one')
    occupation_radius = F(9, 5000)
    radius = 2*occupation_radius+F(1, 2**120)
    reports = {}
    for sign, polynomial in polynomials.items():
        shifted = polynomial.shifted(centers)
        constant = shifted.terms[(0,)*4]
        value = polynomial.evaluate(values)
        require(value.lo*value.hi > 0,
                'Exact interval target propagation excludes zero in both witness alternatives')
        linear = sum(abs(coefficient) for powers, coefficient in shifted.terms.items() if sum(powers) == 1)
        quadratic = sum(abs(coefficient) for powers, coefficient in shifted.terms.items() if sum(powers) == 2)
        require(linear == 4+sign*(centers[0]+centers[1]+u) and quadratic == 1,
                'The complete translated bilinear witness has the claimed exact linear and quadratic coefficient masses')
        variation = linear*radius+radius*radius
        require(abs(constant) > variation,
                'The entire occupation-error box of radius 9/5000 avoids the necessary zero set')
        require(abs(constant)-variation > F(217, 10**7),
                'Both singleton alternatives retain the stated strictly positive rational slack')
        reports[str(sign)] = {'constant_exact': str(constant), 'linear_coefficient_mass_exact': str(linear),
                              'quadratic_coefficient_mass_exact': '1',
                              'whole_box_variation_outward_upper_exact': str(helper.upper_decimal(variation)),
                              'polynomial_slack_lower_exact': '217/10000000'}
    upper = exact_three_state_upper(helper, t, u, [q0, qh], [law0, law_high])
    report = {'target_parameters': {'tanh_J': str(t), 'tanh_H': str(u), 'J': 'log(3)', 'H': 'log(3)',
                                   'attempt_rates': ['1', '1'], 'common_clock_tick': str(clock)},
            'stationary_preparations_exact': [[str(x) for x in law] for law in (law0, law_high)],
            'zero_field_exponential_certificate': certificate0,
            'high_field_exponential_certificate': certificate_high,
            'target_mean_centers_exact': [str(x) for x in centers],
            'target_mean_uniform_enclosure_radius': '2^-120',
            'excluded_uniform_occupation_error_exact': str(occupation_radius),
            'mean_box_radius_exact': str(radius), 'singleton_sign_certificates': reports,
            'exact_three_state_upper': upper}
    return report, values, centers


def ordinary_upper_certificate(helper, u, clock, target_values):
    readout = [-F(1), F(1), F(1)]
    law0 = [F(1, 2), F(67251, 10**6), F(432749, 10**6)]
    law_high = [weight*(1+u*s) for weight, s in zip(law0, readout)]
    require(sum(law0) == sum(law_high) == 1 and min(law0+law_high) > 0,
            'The rounded ordinary upper witness has two positive normalized Gibbs-tilted preparations')
    fluxes = ((36246, 35559, 19500), (31102, 18523, 702))
    generators, exponentials, exponential_certificates = [], [], []
    for law, numerators in zip((law0, law_high), fluxes):
        q = [[F(0)]*3 for _ in range(3)]
        for (i, j), numerator in zip(((0, 1), (0, 2), (1, 2)), numerators):
            flux = F(numerator, 10**6)
            q[i][j], q[j][i] = flux/law[i], flux/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(all(q[i][j] > 0 for i, j in product(range(3), repeat=2) if i != j)
                and all(sum(row) == 0 for row in q),
                'The ordinary upper witness is a genuine irreducible generator')
        require(all(law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(3), repeat=2))
                and helper.mm([law], q) == [[F(0)]*3],
                'The ordinary upper witness is exactly reversible and stationary at each preparation field')
        exponential, certificate = helper.exponential_enclosure(q, clock)
        generators.append(q)
        exponentials.append(exponential)
        exponential_certificates.append(certificate)
    require(max(-q[i][i] for q in generators for i in range(3)) == F(18582, 22417) < 1,
            'The ordinary witness has the stated exact maximum exit rate below one')
    values = four_responses(helper, exponentials, [law0, law_high], readout)
    errors = []
    for value, target in zip(values, target_values):
        difference = value-target
        error = max(abs(difference.lo), abs(difference.hi))/2
        require(error < F(1, 550),
                'Exact intervals certify occupation error below one over 550 in each of the same four experiments')
        errors.append(helper.upper_decimal(error))
    necessary_value = response_polynomial(helper, -1, u).evaluate(values)
    require(necessary_value.lo <= 0 <= necessary_value.hi,
            'The ordinary witness interval responses are consistent with their exact necessary zero')
    require(F(1, 550)/F(9, 5000) == F(100, 99),
            'The certified upper and universal lower bracket differ by the stated factor')
    return {'total_states': 3, 'readout_exact': [str(x) for x in readout],
            'stationary_preparations_exact': [[str(x) for x in law] for law in (law0, law_high)],
            'stationary_flux_pair_order': [[0, 1], [0, 2], [1, 2]],
            'stationary_flux_numerators': [list(row) for row in fluxes], 'stationary_flux_denominator': 10**6,
            'generators_exact': [[[str(x) for x in row] for row in q] for q in generators],
            'exponential_certificates': exponential_certificates, 'maximum_exit_rate_exact': '18582/22417',
            'occupation_error_outward_upper_by_protocol_exact': [str(x) for x in errors],
            'certified_uniform_occupation_error_upper_exact': '1/550',
            'upper_to_lower_bracket_ratio_exact': '100/99',
            'scope': 'These fixed rational parameters originated from a separate exploratory fit. Their validity and four-experiment upper error are certified without fitting here; no all-protocol approximation or exact optimum is claimed.'}, values


def biased_polynomials(helper):
    variables = [helper.Poly.variable(6, i) for i in range(6)]
    m, a, b, l, r, u = variables
    z = 1+u*r
    polynomials = {}
    for sign in (-1, 1):
        q = 1+sign*r
        singleton_numerator = u*m+sign*(r+u-m)
        polynomial = q*((1+sign*u)*l+z*b-m)-z*a*(1+sign*m)-r*singleton_numerator
        require(len(polynomial.terms) == 16 and max(map(sum, polynomial.terms)) == 4,
                'The biased four-mean identity has sixteen monomials and total degree four')
        m0, a0, b0, l0, u0 = [helper.Poly.variable(5, i) for i in range(5)]
        require(polynomial.substitute([m0, a0, b0, l0, F(0), u0]) == b0-m0-a0+l0+sign*(u0*l0-a0*m0),
                'The biased identity reduces to the original witness with a symbolic field increment')
        polynomials[sign] = polynomial
    return polynomials


def biased_fixture_checks(helper, polynomials):
    r, u, tau = F(1, 7), F(2, 3), F(1, 100000)
    for sign in (-1, 1):
        readout = [F(sign), -F(sign), -F(sign)]
        singleton = (1+sign*r)/2
        low_law = [singleton, (1-singleton)*F(2, 3), (1-singleton)/3]
        tilted = [weight*(1+u*s)/(1+u*r) for weight, s in zip(low_law, readout)]
        require(sum(tilted) == 1 and sum(weight*s for weight, s in zip(low_law, readout)) == r,
                'The independent biased fixture has the required normalized relative Gibbs tilt')
        low = reversible_clock(helper, low_law, [F(1, 100), F(1, 120), F(1, 150)])
        for defect in (F(0), tau):
            high_law = tilted[:]
            high_law[1] += defect
            high_law[2] -= defect
            require(sum(abs(x-y) for x, y in zip(high_law, tilted))/2 == defect,
                    'The high-field equilibrium mismatch has exactly the stated total variation')
            high = reversible_clock(helper, high_law, [F(1, 400), F(1, 500), F(1, 600)])
            values = four_responses(helper, [low, high], [low_law, high_law], readout)
            actual = polynomials[sign].evaluate(values+[r, u])
            q, z = 1+sign*r, 1+u*r
            band = (4*q*z*(1+2*u)/(1-sign*u)+2*z*(q+abs(1+sign*values[0])))*defect
            require(abs(actual) <= band,
                    'Independent reversible fixtures obey the exact or approximate Gibbs residual inequality')
            if not defect:
                require(actual == 0, 'The biased necessary witness vanishes exactly under the exact force law')


def robust_box_certificate(helper, centers):
    polynomials = biased_polynomials(helper)
    biased_fixture_checks(helper, polynomials)
    center = centers+[F(0), F(4, 5)]
    radii = [F(17, 5000)+F(1, 2**120)]*4+[F(1, 10000)]*2
    umin, umax, qmax = F(7999, 10000), F(8001, 10000), F(10001, 10000)
    zmax, tau = 1+umax/F(10000), F(1, 100000)
    signs = {}
    for sign, polynomial in polynomials.items():
        shifted = polynomial.shifted(center)
        require(len(shifted.terms) == 24, 'The exact local biased witness has the expected translated support')
        constant = shifted.terms[(0,)*6]
        variation = sum(abs(coefficient)*helper.product_value(radius**power for radius, power in zip(radii, powers))
                        for powers, coefficient in shifted.terms.items() if sum(powers))
        minimum_denominator = 1-umax if sign == 1 else 1+umin
        local_m = (centers[0]-radii[0], centers[0]+radii[0])
        absolute_factor = max(abs(1+sign*m) for m in local_m)
        residual = (4*qmax*zmax*(1+2*umax)/minimum_denominator+2*zmax*(qmax+absolute_factor))*tau
        public_constant = F(8114 if sign == -1 else 73033, 10**6)
        public_variation = F(7670 if sign == -1 else 19614, 10**6)
        public_residual = F(90 if sign == -1 else 569, 10**6)
        require(abs(constant) > public_constant and variation < public_variation and residual < public_residual,
                'The exact biased box satisfies all stated center, variation and approximate-force bounds')
        require(abs(constant)-variation-residual > F(354, 10**6),
                'Every allowed biased response vector stays strictly outside its necessary residual band')
        signs[str(sign)] = {'center_absolute_lower_exact': str(public_constant),
                             'whole_box_variation_upper_exact': str(public_variation),
                             'approximate_force_residual_upper_exact': str(public_residual),
                             'remaining_slack_lower_exact': '177/500000'}
    return {'mean_radius_about_nominal_target_exact': '17/5000',
            'inherited_target_mean_center_radius': '2^-120',
            'stationary_baseline_bias_absolute_bound_exact': '1/10000',
            'tanh_increment_center_exact': '4/5', 'tanh_increment_radius_exact': '1/10000',
            'high_field_stationary_TV_mismatch_bound_exact': '1/100000',
            'stationary_preparation_occupation_error_exclusion_exact': '17/10000',
            'sign_certificates': signs,
            'scope': 'The exact box is an essential premise of the analytic biased/approximate-force exclusion. Each experiment uses the stationary law of its designated preparation field before separate preparation-error allowances.'}


def execution_and_resets(helper):
    eps = F(1, 100000)
    displacement = 2*eps+eps/2+(F(3, 2)+eps)*eps+4*eps
    require(displacement == F(800001, 10**10) < F(1, 10000),
            'The two-preparation target/rival displacement budget has the stated exact value')
    require(F(17, 10000)-displacement > F(1, 625),
            'Actual preparation, field and clock errors leave occupation separation greater than one over 625')
    require((1-eps)/20 > F(1, 21) and (1-2*eps)/100 > F(1, 101),
            'Both physical preparation laws have the conservative minimum masses used in the reset bounds')
    t, high_min = F(4, 5), F(4, 5)-eps
    maximum_high_kappa_squared = t*t*(1-high_min*high_min)/(1-t*t*high_min*high_min)
    require(maximum_high_kappa_squared < F(25, 64) and 1-F(5, 8) == F(3, 8),
            'The actual high-field target has the stated spectral-gap lower bound')
    reset_reports = []
    for label, wait, gap, coefficient in (('low', F(62), F(1, 5), F(5)),
                                          ('high', F(36), F(3, 8), F(25))):
        argument = 2*wait*gap
        term = lower_exponential = F(1)
        for j in range(1, 65):
            term *= argument/j
            lower_exponential += term
        require(coefficient < eps*eps*lower_exponential,
                'A positive rational exponential lower sum certifies the squared preparation TV bound')
        reset_reports.append({'field': label, 'actual_wait_lower_exact': str(wait),
                              'spectral_gap_lower_exact': str(gap), 'squared_TV_prefactor_upper_exact': str(coefficient),
                              'exponential_lower_sum_degree': 64})
    require(sum(1 for preparation, _ in PROTOCOLS if preparation == 0) == 2
            and sum(1 for preparation, _ in PROTOCOLS if preparation == 1) == 2,
            'The experiment menu uses two low-field and two high-field preparations')
    require(sum(len(word) for _, word in PROTOCOLS) == 6 and F(3, 2)*6 == 9
            and 2*62+2*36 == 196,
            'The four protocols have the stated active tick count and two-preparation wait budget')
    return {'preparation_TV_tolerance_exact': str(eps), 'field_tolerance_exact': str(eps),
            'per_tick_duration_tolerance_exact': str(eps), 'combined_occupation_displacement_exact': str(displacement),
            'actual_occupation_separation_lower_exact': '1/625',
            'target_preparation_reset_certificates': reset_reports,
            'nominal_active_duration_sum_exact': '9', 'preparation_duration_sum_exact': '196',
            'calibrated_serial_exposure_per_common_replicate_upper_exact': str(F(205)+6*eps),
            'scope': 'The universal perturbation and target spectral arguments are analytic. These checks certify their numerical budget and reset inequalities. No finite reset time is inferred for arbitrary uncapped rivals, and the positive three-state upper for imperfect target preparations has error at most the preparation TV tolerance.'}


def sampling_checks(helper, target_values, upper_values):
    def log_ratio(ratio):
        x = (ratio-1)/(ratio+1)
        require(0 <= x < 1, 'The exact logarithm range reduction admits the positive atanh expansion')
        lower = 2*sum(x**(2*j+1)/F(2*j+1) for j in range(32))
        tail = 2*x**65/(65*(1-x*x))
        return helper.Interval(lower, lower+tail)

    def ceiling(value):
        return -((-value.numerator)//value.denominator)

    require(F(2)**7*F(5, 4) == 160 and F(2)**4*F(19, 16) == 19,
            'Both log range-reduction products are exact')
    log_two = log_ratio(F(2))
    log_160 = 7*log_two+log_ratio(F(5, 4))
    log_19 = 4*log_two+log_ratio(F(19, 16))
    require(log_160.hi-log_160.lo < F(1, 10**30) and log_19.hi-log_19.lo < F(1, 10**30),
            'The rational log intervals determine the sample-count ceilings without floating logarithms')
    counts = []
    for label, separation, model_error in (('nominal', F(9, 5000), F(0)),
                                            ('calibrated', F(1, 625), F(0)),
                                            ('calibrated_with_model_allowance', F(1, 625), F(1, 10000))):
        gap = separation-model_error-F(1, 2**120)
        lower, upper = 2*log_160.lo/(gap*gap), 2*log_160.hi/(gap*gap)
        count = ceiling(upper)
        require(ceiling(lower) == count and F(count)*gap*gap/2 >= log_160.hi
                and F(count-1)*gap*gap/2 < log_160.lo,
                'The sufficient four-cell confidence and power sample ceiling is fixed by exact inequalities')
        counts.append({'case': label, 'occupation_separation_exact': str(separation),
                       'model_allowance_exact': str(model_error), 'trials_per_experiment': count,
                       'total_trials_four_experiments': 4*count,
                       'serial_exposure_with_two_resets_upper_exact': str(count*(F(205)+F(6, 100000)))})
    for target, upper in zip(target_values, upper_values):
        require(F(1, 8) < (1+target.lo)/2 <= (1+target.hi)/2 < F(7, 8)
                and F(1, 8) < (1+upper.lo)/2 <= (1+upper.hi)/2 < F(7, 8),
                'Both certified Bernoulli responses lie in the interval used by the information bound')
    kl_bound = F(32, 7*550**2)
    require(kl_bound < F(1, 66000), 'The nearby ordinary witness gives the stated per-observation KL upper bound')
    information_lower = 59400*log_19
    integer_lower = ceiling(information_lower.lo)
    require(integer_lower == ceiling(information_lower.hi),
            'The deterministic integer sample lower count is fixed by exact logarithm bounds')
    return {'type_I_error_bound_exact': '1/20', 'type_II_error_bound_exact': '1/20',
            'target_center_gap_charge': '2^-120',
            'logarithm_method': '32-term positive atanh series with exact range reduction and geometric remainder',
            'sufficient_counts': counts, 'per_observation_KL_upper_exact': str(kl_bound),
            'adaptive_expected_total_trials_strict_lower_exact': '59400*log(19)',
            'fixed_integer_total_trials_lower': integer_lower,
            'scope': 'These numbers certify the analytic four-cell Hoeffding and information bounds under the stated preparation/readout assumptions. The sufficient allocation is not claimed optimal; the information lower bound uses only this four-experiment menu and the explicit nearby reversible witness.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_preparation_witness.json'))
    args = parser.parse_args()
    helper = load_helper()
    t, u, clock = F(4, 5), F(4, 5), F(3, 2)
    symbolic_checks(helper)
    polynomials = {sign: response_polynomial(helper, sign, u) for sign in (-1, 1)}
    reversible_fixture_checks(helper, u, polynomials)
    target, target_values, centers = target_certificate(helper, t, u, clock, polynomials)
    ordinary_upper, upper_values = ordinary_upper_certificate(helper, u, clock, target_values)
    require(len(PROTOCOLS) == 4 and max(len(word) for _, word in PROTOCOLS) == 2,
            'The witness uses four endpoint experiments with at most two ticks and one switch')
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction polynomial identities, physical generators, rational Taylor enclosures and bilinear whole-box bounds',
              'protocol_order': [{'stationary_preparation_field': prep, 'chronological_fields': list(word)} for prep, word in PROTOCOLS],
              'mean_order': ['m', 'a', 'b', 'l'], 'target_certificate': target,
              'ordinary_three_state_upper': ordinary_upper,
              'two_snapshot_corollary': snapshot_corollary_checks(helper, u),
              'calibrated_witness': robust_box_certificate(helper, centers),
              'execution_and_two_preparation_resets': execution_and_resets(helper),
              'sampling': sampling_checks(helper, target_values, upper_values),
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False,
              'numerical_optimization_used': False,
              'limitations': ['The universal ordinary-rival implication is an analytic singleton-sector identity; the exact target and local-box calculations are essential numerical premises.',
                              'The comparison requires both corresponding stationary preparations and the shared Gibbs force tilt.',
                              'The rational reversible-kernel fixtures test the necessary algebra; continuous-time embeddability of those fixtures is not asserted.',
                              'The positive three-state realization preserves controlled means, not entire output trajectories.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                HELPER: hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest()},
              'input_report_sha256': {INPUT_REPORT: INPUT_REPORT_SHA256},
              'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                                        for name in ('docs/FAMILIAR_SWITCH_PREPARATION_WITNESS.md',
                                                     'docs/FAMILIAR_SWITCH_PREPARATION_COST.md',
                                                     'docs/FAMILIAR_SWITCH_CALIBRATION.md',
                                                     'docs/FAMILIAR_SWITCH_FINITE_MARGIN.md',
                                                     'docs/FAMILIAR_SWITCH_STRUCTURE.md')}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
