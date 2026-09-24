#!/usr/bin/env python3
"""Exact snapshot-law, calibration and fixed-score design certificates.

Small rational matrices and polynomial boxes certify numerical premises of the
analytic ordinary-reversibility witness. No floating arithmetic, optimization,
sample simulation or universal-rival enumeration is used.
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
INPUT_REPORT = 'reports/switch_preparation_witness.json'
INPUT_SHA = '3c4e563f598c1cbdd9b70a24d2251a052e8577d286a7e0733f061c600bb35b88'
CHECKS = 0
WORDS = ((0, 1), (1, 0))


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_helper():
    payload = (ROOT/INPUT_REPORT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_SHA, 'The prerequisite report is the frozen reviewed version')
    prior = json.loads(payload)
    for name, digest in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == digest, 'The inherited source snapshots are intact')
    for name, digest in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'The inherited proof snapshots are intact')
    spec = importlib.util.spec_from_file_location('frozen_snapshot_arithmetic', ROOT/'scripts'/HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper, prior


def snapshot_laws(h, exponentials, law, readout):
    tables, moments = [], []
    for left, right in WORDS:
        kernel = h.mm(exponentials[left], exponentials[right])
        table = [[sum(law[i]*kernel[i][j] for i in range(len(law)) for j in range(len(law))
                      if readout[i] == si and readout[j] == sj) for sj in (-1, 1)] for si in (-1, 1)]
        mean = sum(law[i]*kernel[i][j]*readout[j] for i in range(len(law)) for j in range(len(law)))
        correlation = sum(law[i]*kernel[i][j]*readout[i]*readout[j] for i in range(len(law)) for j in range(len(law)))
        tables.append(table)
        moments.extend((mean, correlation))
    return tables, moments


def interval_distance(value, center):
    return max(abs(value.lo-center), abs(value.hi-center))


def nominal_certificate(h, prior):
    t = u = F(4, 5)
    generators, laws, exponentials, certificates = [], [], [], []
    for field in (F(0), u):
        q, law, readout = h.physical_generator(t, field)
        exponential, certificate = h.exponential_enclosure(q, F(3, 2))
        generators.append(q)
        laws.append(law)
        exponentials.append(exponential)
        certificates.append(certificate)
    tables, moments = snapshot_laws(h, exponentials, laws[0], readout)
    centers = [h.round_dyadic((x.lo+x.hi)/2, 128) for x in moments]
    eta = F(1, 2**120)
    require(all(interval_distance(x, c) < eta for x, c in zip(moments, centers)), 'All four exact joint moments have the stated dyadic enclosures')
    for table, mean, correlation in zip(tables, moments[::2], moments[1::2]):
        for i, si in enumerate((-1, 1)):
            for j, sj in enumerate((-1, 1)):
                recovered = F(1, 4)*(1+sj*mean+si*sj*correlation)
                cell = table[i][j]
                require(cell.lo > 0 and cell.hi < 1 and max(cell.lo, recovered.lo) <= min(cell.hi, recovered.hi),
                        'Physical joint-law cells are positive and agree with the balanced binary moment representation')
    m, c, l, d = [h.Poly.variable(4, i) for i in range(4)]
    signs = {}
    for sign in (-1, 1):
        polynomial = u*c-u*(1+sign*m)*d+sign*(u-m)*l
        require(polynomial == (m+u*c)-m-(l+u*d)+l+sign*(u*l-(l+u*d)*m), 'Direct snapshot and four-preparation witnesses are exactly the same polynomial')
        shifted = polynomial.shifted(centers)
        constant = shifted.terms[(0,)*4]
        linear = sum(abs(v) for powers, v in shifted.terms.items() if sum(powers) == 1)
        quadratic = sum(abs(v) for powers, v in shifted.terms.items() if sum(powers) == 2)
        require(linear == centers[2]+u*centers[3]+3*u-centers[0]+sign*u*centers[0] and quadratic == 1+u,
                'The complete translated witness has the independently stated linear and quadratic masses')
        radius = F(23, 6250)+eta
        variation = linear*radius+quadratic*radius*radius
        require(abs(constant)-variation > F(1, 30000), 'The entire nominal joint-TV box leaves strictly positive witness slack')
        signs[str(sign)] = {'constant_exact': str(constant), 'linear_mass_exact': str(linear),
                            'quadratic_mass_exact': str(quadratic), 'variation_outward_upper_exact': str(h.upper_decimal(variation)),
                            'remaining_slack_lower_exact': '1/30000'}
    for dm, dc in ((F(2, 7), F(1, 9)), (-F(1, 4), F(3, 5)), (F(1, 3), -F(1, 3)), (F(0), F(1, 8))):
        require((abs(dm+dc)+abs(dm-dc))/4 == max(abs(dm), abs(dc))/2, 'The balanced binary joint-TV identity holds in each sign-order fixture')
    upper = prior['target_certificate']['exact_three_state_upper']
    nu0 = list(map(F, upper['stationary_preparations_exact'][0]))
    labels = list(map(F, upper['readout_exact']))
    auxiliary = [-t, -2*t, (1+t*t)/(2*t)]
    coordinates = [[F(1), s, z] for s, z in zip(labels, auxiliary)]
    target_coordinates = [[F(1), F(s), F(z)] for s, z in product((-1, 1), repeat=2)]
    for index, field in enumerate((F(0), u)):
        q = [list(map(F, row)) for row in upper['generators_exact'][index]]
        denominator = 1-t*t*field*field
        reduced = [[F(0), field*(1-t*t)/denominator, F(0)], [F(0), -F(1), t], [F(0), t*(1-field*field)/denominator, -F(1)]]
        require(h.mm(q, coordinates) == h.mm(coordinates, reduced) and h.mm(generators[index], target_coordinates) == h.mm(target_coordinates, reduced),
                'The archived positive predictor and physical target share the exact controlled mean equations')
    for sign in (-1, 1):
        mass = sum(p for p, s in zip(nu0, labels) if s == sign)
        conditional = sum(p*z for p, s, z in zip(nu0, labels, auxiliary) if s == sign)/mass
        require(mass == F(1, 2) and conditional == t*sign, 'Both initial sectors match the physical conditional closed coordinates')
    report = {'tanh_J_exact': '4/5', 'tanh_H_exact': '4/5', 'clock_exact': '3/2',
              'moment_order': ['m', 'c', 'l', 'd'], 'moment_centers_exact': list(map(str, centers)), 'moment_enclosure_radius': '2^-120',
              'joint_cell_order': 'rows initial -,+; columns final -,+',
              'joint_law_intervals_exact': [[[[str(x.lo), str(x.hi)] for x in row] for row in table] for table in tables],
              'physical_exponential_certificates': certificates, 'joint_TV_separation_lower_exact': '23/12500',
              'sign_certificates': signs, 'exact_three_state_conditional_mean_match': True}
    return report, tables, moments, centers


def comparator_certificate(h, targets):
    u, nu0, readout = F(4, 5), [F(1, 2), F(63012, 10**6), F(436988, 10**6)], [-1, 1, 1]
    laws = [nu0, [p*(1+u*s) for p, s in zip(nu0, readout)]]
    fluxes = ((39732, 33330, 21481), (22758, 23366, 209))
    generators, exponentials, certificates = [], [], []
    for law, numerators in zip(laws, fluxes):
        q = [[F(0)]*3 for _ in range(3)]
        for (i, j), numerator in zip(((0, 1), (0, 2), (1, 2)), numerators):
            q[i][j], q[j][i] = F(numerator, 10**6)/law[i], F(numerator, 10**6)/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(sum(law) == 1 and min(law) > 0 and h.mm([law], q) == [[F(0)]*3], 'The fixed comparator preparations are positive, normalized and stationary')
        require(all(q[i][j] > 0 and law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(3), repeat=2) if i != j),
                'The fixed comparator is strictly positive and ordinarily reversible at both fields')
        exponential, certificate = h.exponential_enclosure(q, F(3, 2))
        generators.append(q)
        exponentials.append(exponential)
        certificates.append(certificate)
    require(max(-q[i][i] for q in generators for i in range(3)) == F(61213, 63012) < 1, 'The comparator has the advertised total exit-rate cap')
    tables, _ = snapshot_laws(h, exponentials, nu0, readout)
    tvs, kls = [], []
    for target, table in zip(targets, tables):
        tv = kl = F(0)
        for tr, qr in zip(target, table):
            for p, q in zip(tr, qr):
                require(min(p.lo, q.lo) > 0, 'The information comparison uses strictly interior joint probabilities')
                difference = p-q
                error = max(abs(difference.lo), abs(difference.hi))
                tv += error/2
                kl += error*error/(2*min(p.lo, q.lo))
        require(tv < F(37, 20000), 'Exact cell intervals certify the nearby ordinary joint-law upper')
        require(kl < F(1, 30000), 'The exact Taylor KL majorant is below one over thirty thousand')
        tvs.append(str(h.upper_decimal(tv)))
        kls.append(str(h.upper_decimal(kl)))
    require(F(37, 20000)/F(23, 12500) == F(185, 184), 'The upper/lower bracket has the stated relative width')
    return {'readout': readout, 'preparation_laws_exact': [list(map(str, law)) for law in laws],
            'flux_pair_order': [[0, 1], [0, 2], [1, 2]], 'flux_numerators': [list(row) for row in fluxes], 'flux_denominator': 10**6,
            'generators_exact': [[[str(x) for x in row] for row in q] for q in generators],
            'exponential_certificates': certificates, 'maximum_exit_exact': '61213/63012',
            'joint_TV_outward_uppers_exact': tvs, 'uniform_joint_TV_upper_exact': '37/20000',
            'KL_Taylor_outward_uppers_exact': kls, 'uniform_KL_upper_exact': '1/30000',
            'scope': 'This fixed rational model was selected separately; no fit or optimum is computed here. The KL Taylor majorant uses exact normalization analytically and interval cell differences numerically.'}


def robust_certificate(h, centers):
    m, c, l, d, v, u = [h.Poly.variable(6, i) for i in range(6)]
    center = centers+[F(0), F(4, 5)]
    radii = [F(9, 2500)+F(1, 2**120)]*4+[F(1, 10000)]*2
    umax, umin, qmax = F(8001, 10000), F(7999, 10000), F(10001, 10000)
    zmax, theta = 1+umax/F(10000), F(1, 100000)
    signs = {}
    for sign in (-1, 1):
        direct = (1+sign*v)*((1+sign*u)*l+u*c)-(l+u*d)*(1+sign*m)-v*(u*m+sign*(v+u-m))
        expanded = u*c-u*d-sign*u*m*d+sign*u*l-sign*m*l+v*((sign+u)*l+sign*u*c-u*m-sign*u+sign*m)-sign*v*v
        require(direct == expanded and len(direct.terms) == 12 and max(map(sum, direct.terms)) == 3,
                'The direct and expanded biased singleton identities agree as formal polynomials')
        shifted = direct.shifted(center)
        require(len(shifted.terms) == 22, 'The complete shifted calibration polynomial has the expected support')
        constant = abs(shifted.terms[(0,)*6])
        variation = sum(abs(coefficient)*h.product_value(radius**power for radius, power in zip(radii, powers))
                        for powers, coefficient in shifted.terms.items() if sum(powers))
        denominator = 1-umax if sign == 1 else 1+umin
        residual = (12*umax*qmax*zmax*theta+16*zmax*zmax*theta*theta)/denominator
        public = (F(8114 if sign == -1 else 73033, 10**6), F(7943 if sign == -1 else 10311, 10**6), F(54 if sign == -1 else 481, 10**6))
        require(constant > public[0] and variation < public[1] and residual < public[2]
                and constant-variation-residual > F(1, 10000), 'The full biased approximate-force box remains outside both singleton residual bands')
        signs[str(sign)] = {'center_absolute_lower_exact': str(public[0]), 'variation_upper_exact': str(public[1]),
                            'residual_upper_exact': str(public[2]), 'remaining_slack_lower_exact': '1/10000'}
    return {'stationary_joint_TV_exclusion_exact': '9/5000', 'baseline_bias_bound_exact': '1/10000',
            'tanh_increment_center_exact': '4/5', 'tanh_increment_radius_exact': '1/10000',
            'high_stationary_TV_mismatch_bound_exact': '1/100000', 'target_center_charge': '2^-120', 'sign_certificates': signs}


def detector_execution_certificate(h):
    eps, p, r = F(1, 100000), F(1, 100), F(49, 50)
    channel = [[1-p, p], [p, 1-p]]
    inverse = [[(1-p)/r, -p/r], [-p/r, (1-p)/r]]
    require(h.mm(channel, inverse) == h.identity(2) and max(sum(abs(x) for x in row) for row in inverse) == 1/r,
            'The binary symmetric detector has an exact inverse with the stated l1 norm')
    joint_inverse = [[inverse[i][k]*inverse[j][l] for k, l in product(range(2), repeat=2)] for i, j in product(range(2), repeat=2)]
    conorm = r*r
    require(max(sum(abs(x) for x in row) for row in joint_inverse) == 1/conorm == F(2500, 2401),
            'The product detector has the exact two-bit TV conorm certificate')
    target_budget = 2*eps+eps/2+(F(3, 2)+eps)*eps+4*eps
    rival_budget = 2*eps
    require(target_budget == F(800001, 10**10) and target_budget+rival_budget < F(101, 10**6),
            'Preparation, field, tick and noninvasive-readout deviations have the stated conservative joint-TV budget')
    known_gap = conorm*(F(9, 5000)-target_budget-rival_budget)
    unknown_gap = known_gap-4*eps
    require(known_gap > F(1, 625) and unknown_gap > F(3, 2000),
            'The calibrated joint-law separation survives the known and uncertain detector allowances')
    require(4*eps == F(1, 25000), 'The stated general three-state upper allows two preparation/backaction and two channel-calibration charges')
    return {'target_joint_TV_displacement_exact': str(target_budget), 'rival_joint_TV_displacement_exact': str(rival_budget),
            'each_preparation_field_tick_backaction_tolerance_exact': str(eps), 'nominal_each_detector_error_exact': str(p),
            'known_product_detector_conorm_exact': str(conorm), 'each_detector_calibration_tolerance_exact': str(eps),
            'known_detector_separation_lower_exact': '1/625', 'uncertain_detector_separation_lower_exact': '3/2000',
            'general_three_state_uncertain_detector_upper_exact': '1/25000',
            'scope': 'The analytic coupling and perturbation arguments supply the component bounds. The matrix norm calculation and arithmetic certify their numerical consequences; no arbitrary state-dependent detector or arbitrary disturbance is covered.'}


def exp_negative_upper(x):
    """Positive Taylor partial sums bound exp(x) from below for x >= 0."""
    require(x >= 0, 'Only nonnegative arguments enter the one-sided exponential certificate')
    term = total = F(1)
    for j in range(1, 97):
        term *= x/j
        total += term
    return 1/total


def score_certificate(h, moments, centers):
    u0 = F(4, 5)
    m0, c0, l0, d0 = centers
    a0, eta = l0+u0*d0, F(1, 10**12)
    eps, btarget, conorm = F(1, 100000), F(800001, 10**10), F(2401, 2500)
    latent_ranges = {}
    fband = {-1: F(110, 10**6), 1: F(510, 10**6)}
    for sign in (-1, 1):
        derivative_max = nuisance_max = F(0)
        for bits in product((-1, 1), repeat=5):
            m, c, l, d = [value+bit*F(303, 10000) for value, bit in zip(centers, bits)]
            u = u0+bits[4]/F(10000)
            derivative_max = max(derivative_max, abs(c-(1+sign*m)*d+sign*l))
            nuisance_max = max(nuisance_max, abs((u+sign)*l+sign*u*c+(sign-u)*m-sign*u))
        require(derivative_max < F(201 if sign == -1 else 144, 1000)
                and nuisance_max < F(358 if sign == -1 else 112, 1000),
                'Multi-affine corner bounds certify field and baseline sensitivities throughout the enlarged gate box')
        umax, umin, qmax = F(8001, 10000), F(7999, 10000), F(10001, 10000)
        zmax = 1+umax/F(10000)
        residual = (12*umax*qmax*zmax*eps+16*zmax*zmax*eps*eps)/(1-umax if sign == 1 else 1+umin)
        require(residual+(derivative_max+nuisance_max)/10000+F(1, 10**8) < fband[sign],
                'The calibrated singleton score band includes force, bias and quadratic baseline errors')
        A, B = sign*(u0-m0), -u0*(1+sign*m0)
        latent_ranges[sign] = (2*(u0+abs(a0)), 2*(abs(A)+abs(B)))
    rows = [
        ('nominal', 550000, 350000, False, False, F(0),
         ('0.931', '0.365', '1.432'), ('0.680', '0.293', '0.928', '1.310'),
         ('2.678', '1.700', '3.034'), ('0.0002', '0.0002'), ('0.008114', '0.073033'), ('0.0043', '0.0062')),
        ('physical', 600000, 400000, True, False, F(0),
         ('0.932', '0.366', '1.434'), ('0.681', '0.294', '0.929', '1.311'),
         ('2.678', '1.700', '3.034'), ('0.0004', '0.00083'), ('0.00776', '0.07257'), ('0.0043', '0.0065')),
        ('uncertain_detector', 700000, 500000, True, True, F(0),
         ('0.998', '0.390', '1.548'), ('0.747', '0.318', '0.995', '1.426'),
         ('2.766', '1.754', '3.143'), ('0.0005', '0.00095'), ('0.00767', '0.07245'), ('0.00425', '0.0063')),
        ('uncertain_detector_with_model_allowance', 850000, 650000, True, True, F(1, 10000),
         ('0.998', '0.390', '1.548'), ('0.747', '0.318', '0.995', '1.426'),
         ('2.766', '1.754', '3.143'), ('0.00096', '0.00155'), ('0.00767', '0.07245'), ('0.0044', '0.0064'))]
    reports = []
    for label, nA, nB, calibrated, noisy, allowance, nulls, targets, widths, bands, means, cuts in rows:
        nulls, targets, widths, bands, means, cuts = [tuple(map(F, values)) for values in (nulls, targets, widths, bands, means, cuts)]
        r0 = rf = F(49, 50) if noisy else F(1)
        channel_budget = 2*eps if noisy else F(0)
        ET = (btarget if calibrated else F(0))+channel_budget/conorm
        ER = (2*eps if calibrated else F(0))+(channel_budget+allowance)/conorm
        observed_displacement = (btarget if calibrated else F(0))+channel_budget
        bias = F(1, 1000) if calibrated else F(0)
        if calibrated:
            require(((r0+2*eps)*(F(1, 10000)+4*eps)+2*allowance)/r0 < bias,
                    'The enlarged null class has the corrected initial-bias bound used by the variance certificate')
            require(F(3, 100)+2*ER+eta < F(303, 10000), 'The true gate box and systematic error remain within the certified nuisance-corner box')
        sign_reports = {}
        for index, sign in enumerate((-1, 1)):
            A, B = sign*(u0-m0), -u0*(1+sign*m0)
            widthA, widthB = 2*(u0/r0+abs(a0))/rf, 2*(abs(A)+abs(B)/r0)/rf
            require(widthA < widths[0] and widthB < widths[index+1], 'Each fixed score range is bounded on all four possible binary outcomes')
            secondA = (u0*u0/(r0*r0)+a0*a0+2*u0*abs(a0)*bias)/(rf*rf)
            secondB = (A*A+B*B/(r0*r0)+2*abs(A*B)*bias)/(rf*rf)
            require(secondA < nulls[0] and secondB < nulls[index+1], 'Null score second moments are bounded uniformly under the gate assumptions')
            scoreA = u0*moments[1]-sign*a0*moments[0]
            scoreB = A*moments[2]+B*moments[3]
            varianceA = (u0*u0/(r0*r0)+a0*a0)/(rf*rf)-scoreA**2
            varianceB = (A*A+B*B/(r0*r0))/(rf*rf)-scoreB**2
            require(varianceA.hi+widths[0]**2*observed_displacement < targets[2*index]
                    and varianceB.hi+widths[index+1]**2*observed_displacement < targets[2*index+1],
                    'Exact target-law variances plus the TV perturbation allowance fit the advertised ceilings')
            systematic = (F(1, 100)+2*ER)*(F(1, 50)+F(18, 5)*ER)
            if calibrated:
                systematic += fband[sign]+sum(latent_ranges[sign])*ER
            require(systematic <= bands[index], 'The fixed-tangent remainder and all null systematic costs fit the stated band')
            signed_target = -sign*(scoreA+scoreB+sign*m0*a0)
            require(signed_target.lo-sum(latent_ranges[sign])*ET-F(1, 10**20) > means[index],
                    'The target signed score keeps the required mean after all admitted displacements')
            size_gap, power_gap = cuts[index]-bands[index], means[index]-cuts[index]
            null_variance = nulls[0]/nA+nulls[index+1]/nB
            target_variance = targets[2*index]/nA+targets[2*index+1]/nB
            maximum_step = max(widths[0]/nA, widths[index+1]/nB)
            for gap, variance, exponent in ((size_gap, null_variance, F(3)),
                                            (power_gap, target_variance, F(31, 10) if sign == -1 else F(7))):
                adjusted = gap-maximum_step*exponent/3
                require(adjusted > 0 and adjusted*adjusted > 2*variance*exponent,
                        'Exact squared inequalities certify the Bernstein score size or power bound')
            sign_reports[str(sign)] = {'null_variance_ceilings_exact': [str(nulls[0]), str(nulls[index+1])],
                                       'target_variance_ceilings_exact': [str(targets[2*index]), str(targets[2*index+1])],
                                       'score_range_ceilings_exact': [str(widths[0]), str(widths[index+1])],
                                       'null_band_exact': str(bands[index]), 'target_mean_lower_exact': str(means[index]),
                                       'rejection_cutoff_exact': str(cuts[index])}
        hm, hc, ha = 1/rf, 1/(r0*rf), (1+u0/r0)/rf
        outside = [F(nA)*F(4, 1000)**2/(2*hm*hm), F(nB)*F(8, 1000)**2/(2*ha*ha)]
        if calibrated:
            outside.append(F(min(nA, nB))*F(1, 100)**2/(2*hc*hc))
        require(all(exp_negative_upper(x) < F(1, 20) for x in outside), 'If a true gate condition fails, the corresponding empirical pass has probability below the size allowance')
        gate_m_gap = F(6, 1000)-2*ET-eta
        gate_a_gap = F(12, 1000)-F(18, 5)*ET-F(9, 5)*eta
        gate_extra_gap = F(1, 50)-2*ET-eta
        require(gate_m_gap > 0 and gate_a_gap > 0 and (not calibrated or gate_extra_gap > 0),
                'All target gate margins are strictly positive before their concentration inequalities are squared')
        gate_failure = 2*exp_negative_upper(F(nA)*gate_m_gap**2/(2*hm*hm))
        gate_failure += 2*exp_negative_upper(F(nB)*gate_a_gap**2/(2*ha*ha))
        if calibrated:
            gate_failure += 2*exp_negative_upper(F(nA)*gate_extra_gap**2/(2*hc*hc))
            gate_failure += 4*exp_negative_upper(F(nB)*gate_extra_gap**2/(2*hc*hc))
        require(gate_failure < F(1, 1000), 'The target satisfies all empirical gates with the allocated joint failure probability')
        reports.append({'case': label, 'paired_trials_0H': nA, 'paired_trials_H0': nB, 'total_fresh_paired_trials': nA+nB,
                        'total_bit_readouts': 2*(nA+nB), 'observed_joint_TV_model_allowance_exact': str(allowance),
                        'target_decoded_TV_allowance_exact': str(ET), 'rival_decoded_TV_allowance_exact': str(ER),
                        'sign_certificates': sign_reports, 'target_gate_failure_upper_exact': str(h.upper_decimal(gate_failure))})
    require(exp_negative_upper(F(3)) < F(1, 20) and exp_negative_upper(F(31, 10)) < F(6, 125)
            and exp_negative_upper(F(7)) < F(1, 1000) and F(6, 125)+F(1, 1000)+F(1, 1000) == F(1, 20),
            'The separate score and gate budgets give five-percent size and power errors')
    return {'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '1/20',
            'target_center_error_charge_exact': str(eta), 'score_center_a_exact': str(a0),
            'gate_empirical_m_radius_exact': '3/500', 'gate_empirical_a_radius_exact': '3/250',
            'robust_additional_gate_c_l_d_radius_exact': '1/50', 'designs': reports,
            'scope': 'Fixed scores, independent fresh paired trials and gates are chosen before data collection. The analytic Bernstein/Hoeffding arguments justify the test; these exact calculations certify all numerical premises. No allocation optimality is claimed.'}


def information_certificate(h):
    def log_ratio(ratio):
        x = (ratio-1)/(ratio+1)
        lower = 2*sum(x**(2*j+1)/F(2*j+1) for j in range(32))
        return h.Interval(lower, lower+2*x**65/(65*(1-x*x)))
    log19 = 4*log_ratio(F(2))+log_ratio(F(19, 16))
    bound = 27000*log19
    ceil = lambda x: -((-x.numerator)//x.denominator)
    require(F(2)**4*F(19, 16) == 19 and ceil(bound.lo) == ceil(bound.hi) == 79500,
            'The exact information lower count is determined by positive atanh logarithm enclosures')
    return {'adaptive_expected_paired_trials_lower_exact': '27000*log(19)', 'fixed_integer_paired_trials_lower': 79500,
            'scope': 'This lower bound uses only the two joint-law protocols and the fixed nearby ordinary comparator. It persists under a common known detector by data processing; expectation is not rounded to an integer.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_snapshot_design.json'))
    args = parser.parse_args()
    helper, prior = load_helper()
    nominal, tables, moments, centers = nominal_certificate(helper, prior)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction polynomial identities, rational matrix Taylor enclosures and concentration-bound arithmetic',
              'protocols': [list(word) for word in WORDS], 'stationary_preparation_field': 0,
              'nominal_certificate': nominal, 'ordinary_comparator': comparator_certificate(helper, tables),
              'robust_stationary_certificate': robust_certificate(helper, centers),
              'detector_and_execution': detector_execution_certificate(helper),
              'fixed_score_designs': score_certificate(helper, moments, centers),
              'necessary_information_cost': information_certificate(helper),
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'limitations': ['The all-rival implication, perturbation assumptions and statistical theorems are analytic. Exact target and response-box calculations are essential numerical premises.',
                              'Two initial/final joint laws are certified; complete trajectory matching is not asserted.',
                              'The fixed ordinary comparator is a feasible upper, not a certified global minimizer.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                HELPER: hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest()},
              'input_report_sha256': {INPUT_REPORT: INPUT_SHA}, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                                        for name in ('docs/FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md',
                                                     'docs/FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md',
                                                     'docs/FAMILIAR_SWITCH_PREPARATION_WITNESS.md',
                                                     'docs/FAMILIAR_SWITCH_PREPARATION_COST.md',
                                                     'docs/FAMILIAR_SWITCH_CALIBRATION.md',
                                                     'docs/FAMILIAR_SWITCH_FINITE_MARGIN.md',
                                                     'docs/FAMILIAR_SWITCH_STRUCTURE.md')}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
