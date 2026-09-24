#!/usr/bin/env python3
"""Exact constants for a localized endpoint-score test; no fitting or sampling."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[1]
INPUT = 'reports/switch_preparation_witness.json'
INPUT_SHA = '3c4e563f598c1cbdd9b70a24d2251a052e8577d286a7e0733f061c600bb35b88'
HELPER = 'verify_familiar_switch_margin.py'
PROOF = 'docs/FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md'
CHECKS = 0
GATES = (F(1, 250), F(1, 250), F(3, 500), F(3, 500))
OUTER = tuple(2*x for x in GATES)
U = F(4, 5)
EPS = F(1, 100000)
CENTER_RADIUS = F(1, 2**121)
CASES = (
    ('nominal', (350000, 400000, 550000, 150000), F(0), F(0), F(0), F(41, 10000)),
    ('calibrated', (400000, 460000, 630000, 180000), EPS, F(0),
     F(700001, 10**10), F(1, 250)),
    ('calibrated_model_error', (450000, 520000, 720000, 200000), EPS,
     F(1, 10000), F(700001, 10**10), F(17, 4000)),
)


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    payload = (ROOT/INPUT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_SHA,
            'The target and calibration premises are the frozen exact four-endpoint certificate')
    prior = json.loads(payload)
    require(prior['status'] == 'PASS', 'The inherited exact certificate passed')
    for name, digest in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == digest,
                'Each inherited source matches the frozen report')
    for name, digest in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'Each inherited proof matches its frozen report')
    spec = importlib.util.spec_from_file_location('frozen_endpoint_score_arithmetic',
                                                 ROOT/'scripts'/HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    certificate = prior['target_certificate']
    require(certificate['target_mean_uniform_enclosure_radius'] == '2^-120',
            'The target enclosure has the stated mean radius')
    centers = list(map(F, certificate['target_mean_centers_exact']))
    require(len(centers) == 4 and prior['mean_order'] == ['m', 'a', 'b', 'l'],
            'The four centers use the intended preparation/word order')
    return helper, prior, centers


def upper(value, digits):
    scale = 10**digits
    return F(-((-value.numerator*scale)//value.denominator), scale)


def lower(value, digits):
    scale = 10**digits
    return F((value.numerator*scale)//value.denominator, scale)


def positive_exponential_sum(argument, degree=32):
    term = total = F(1)
    for j in range(1, degree+1):
        term *= argument/j
        total += term
    return total


def probability_budgets():
    for argument, target in ((F(3), F(20)), (F(31, 10), F(1000, 49)),
                             (F(8), F(2000)), (F(10), F(16000))):
        require(positive_exponential_sum(argument) > target,
                'A positive rational exponential sum certifies the required tail-probability comparison')
    require(F(49, 1000)+F(1, 2000)+F(1, 2000) == F(1, 20),
            'The two score failures and gate failures sum to the allowed type-II error')
    return {'inside_null_exponent_lower': '3',
            'target_minus_exponent_lower': '31/10',
            'target_plus_exponent_lower': '8',
            'gate_exponent_lower': '10',
            'exponential_lower_sum_degree': 32,
            'type_I_error_strict_upper': '1/20',
            'type_II_components_strict_upper': ['49/1000', '1/2000', '1/2000'],
            'type_II_error_strict_upper': '1/20'}


def local_calibrated_bands(helper, centers):
    m, a, b, ell, r, u = [helper.Poly.variable(6, i) for i in range(6)]
    z = 1+u*r
    max_transfer = EPS+F(1, 10000)
    radii = [2*(x+max_transfer) for x in OUTER]+[F(1, 10000)]*2
    point = centers+[F(0), U]
    umin, umax = U-F(1, 10000), U+F(1, 10000)
    qmax, zmax = 1+F(1, 10000), 1+umax/F(10000)
    result = {}
    for sign in (-1, 1):
        q = 1+sign*r
        numerator = u*m+sign*(r+u-m)
        generalized = q*((1+sign*u)*ell+z*b-m)-z*a*(1+sign*m)-r*numerator
        nominal = b-m-a+ell+sign*(U*ell-a*m)
        require(len(generalized.terms) == 16,
                'The calibrated polynomial is the stated sixteen-term identity')
        difference = (generalized-nominal).shifted(point)
        require(difference.terms.get((0,)*6, F(0)) == 0,
                'Only calibration nuisance terms separate the generalized and nominal identities')
        drift = sum(abs(coefficient)*helper.product_value(rad**power for rad, power in zip(radii, powers))
                    for powers, coefficient in difference.terms.items())
        denominator = 1-umax if sign == 1 else 1+umin
        factor = max(abs(1+sign*x) for x in (centers[0]-radii[0], centers[0]+radii[0]))
        residual = (4*qmax*zmax*(1+2*umax)/denominator
                    +2*zmax*(qmax+factor))*EPS
        band = F(1, 8000) if sign == -1 else F(1, 1600)
        require(drift+residual < band,
                'The calibrated necessary residual and nuisance drift fit the public local nominal-witness band')
        result[sign] = band
        result[str(sign)] = {'nominal_witness_band_exact': str(band),
                            'nuisance_drift_outward_upper': str(upper(drift, 15)),
                            'approximate_tilt_residual_outward_upper': str(upper(residual, 15))}
    return result, {'stationary_response_mean_radii': [str(x) for x in radii[:4]],
                    'baseline_bias_radius': '1/10000', 'tanh_increment_radius': '1/10000',
                    'stationary_high_law_TV_radius': '1/100000',
                    'maximum_preparation_plus_model_transfer': str(max_transfer),
                    'sign_bounds': {str(sign): result[str(sign)] for sign in (-1, 1)}}


def score_rows(helper, centers, bands):
    probabilities = [(1+x)/2 for x in centers]
    m, a, b, ell = centers
    occupation_variables = [helper.Poly.variable(4, i) for i in range(4)]
    mean_variables = [2*x-1 for x in occupation_variables]
    require(all(F(1, 2) < p-r < p+r < 1 for p, r in zip(probabilities, OUTER)),
            'Bernoulli variance is maximized at the lower endpoint of each localization interval')
    rows = []
    for label, allocation, prep, model_error, target_displacement, minus_cutoff in CASES:
        transfer = prep+model_error
        target_radius = target_displacement+CENTER_RADIUS
        require(target_radius < min(GATES),
                'Every allowed target response remains strictly inside the empirical gate')
        require(all(2*n*(r-g)**2 > 10 for n, r, g in zip(allocation, OUTER, GATES)),
                'Every possible outside-box coordinate makes passing its gate have exponent greater than ten')
        require(all(2*n*(g-target_radius)**2 > 10 for n, g in zip(allocation, GATES)),
                'Each target gate tail has exponent greater than ten, including calibration and center error')
        scores = {}
        for sign in (-1, 1):
            raw = b-m-a+ell+sign*(U*ell-a*m)
            raw_coefficients = [-2*(1+sign*a), -2*(1+sign*m), F(2), 2*(1+sign*U)]
            coefficients = [-sign*x for x in raw_coefficients]
            intercept = -sign*raw
            require(intercept > 0, 'Both oriented target scores have positive reference values')
            if label == 'nominal':
                mv, av, bv, lv = mean_variables
                witness = bv-mv-av+lv+sign*(U*lv-av*mv)
                score = intercept+sum(c*(p-q) for c, p, q in
                                      zip(coefficients, occupation_variables, probabilities))
                remainder = 4*(occupation_variables[0]-probabilities[0])*(occupation_variables[1]-probabilities[1])
                require(-sign*witness == score+remainder,
                        'The oriented occupation-score identity has exactly the stated bilinear remainder and sign')
            mass = sum(abs(x) for x in coefficients)
            band = bands[sign] if prep else F(0)
            curvature = 4*(OUTER[0]+transfer)*(OUTER[1]+transfer)
            null_upper = upper(band+curvature+mass*transfer, 12)
            target_lower = lower(intercept-mass*target_radius, 12)
            null_variance = upper(sum(c*c*(p-r)*(1-p+r)/n
                                      for c, p, r, n in zip(coefficients, probabilities, OUTER, allocation)), 18)
            target_variance = upper(sum(c*c*(p-target_radius)*(1-p+target_radius)/n
                                        for c, p, n in zip(coefficients, probabilities, allocation)), 18)
            step = upper(max(abs(c)/n for c, n in zip(coefficients, allocation)), 15)
            cutoff = minus_cutoff if sign == -1 else F(3, 200)
            null_deviation, target_deviation = cutoff-null_upper, target_lower-cutoff
            require(null_deviation > 0 and target_deviation > 0,
                    'Each public cutoff lies strictly between the worst null and target score centers')
            null_exponent = null_deviation**2/(2*(null_variance+step*null_deviation/3))
            target_exponent = target_deviation**2/(2*(target_variance+step*target_deviation/3))
            require(null_exponent > 3, 'The exact Bernstein null exponent exceeds three')
            required_power = F(31, 10) if sign == -1 else F(8)
            require(target_exponent > required_power,
                    'The exact Bernstein target exponent covers its assigned failure probability')
            scores[str(sign)] = {'reference_intercept_exact': str(intercept),
                                  'occupation_coefficients_exact': [str(x) for x in coefficients],
                                  'coefficient_absolute_sum_exact': str(mass),
                                  'cutoff_exact': str(cutoff),
                                  'stationary_null_band_exact': str(band),
                                  'curvature_bound_exact': str(curvature),
                                  'null_center_outward_upper': str(null_upper),
                                  'target_center_outward_lower': str(target_lower),
                                  'null_variance_outward_upper': str(null_variance),
                                  'target_variance_outward_upper': str(target_variance),
                                  'summand_absolute_bound_outward_upper': str(step),
                                  'null_exponent_lower': '3',
                                  'target_exponent_lower': str(required_power)}
        ticks = allocation[0]+allocation[1]+2*allocation[2]+2*allocation[3]
        active = F(3, 2)*ticks
        calibrated_time = (active+62*(allocation[0]+allocation[3])
                           +36*(allocation[1]+allocation[2])+EPS*ticks)
        rows.append({'case': label, 'allocation_m_a_b_l': list(allocation),
                     'total_fresh_endpoints': sum(allocation),
                     'preparation_TV_bound': str(prep),
                     'model_accuracy_allowance': str(model_error),
                     'additional_observation_bias': '0',
                     'target_physical_displacement_bound': str(target_displacement),
                     'target_radius_including_center_error': str(target_radius),
                     'nominal_active_exposure_exact': str(active),
                     'calibrated_serial_exposure_upper_exact': str(calibrated_time) if prep else None,
                     'scores': scores})
    require([row['total_fresh_endpoints'] for row in rows] == [1450000, 1670000, 1890000],
            'The three prescribed allocations have the advertised total endpoint counts')
    return probabilities, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_endpoint_score.json'))
    args = parser.parse_args()
    helper, prior, centers = load_inputs()
    failure_budgets = probability_budgets()
    bands, band_report = local_calibrated_bands(helper, centers)
    probabilities, rows = score_rows(helper, centers, bands)
    snapshots = dict(prior['proof_snapshot_sha256'])
    snapshots[PROOF] = hashlib.sha256((ROOT/PROOF).read_bytes()).hexdigest()
    report = {'status': 'PASS', 'checks': CHECKS, 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction polynomial boxes, variance and Bernstein exponent bounds, positive exponential sums',
              'cell_order': ['m', 'a', 'b', 'l'],
              'reference_occupation_centers_exact': [str(x) for x in probabilities],
              'reference_occupation_enclosure_radius': '2^-121',
              'empirical_gate_halfwidths_exact': [str(x) for x in GATES],
              'population_localization_halfwidths_exact': [str(x) for x in OUTER],
              'calibrated_local_bands': band_report, 'failure_budgets': failure_budgets,
              'designs': rows, 'floating_arithmetic_used': False,
              'numerical_optimization_used': False, 'samples_simulated': 0,
              'limitations': ['The universal identity and statistical gate partition are analytic premises, not inferred from fitted models.',
                              'Fresh independent Bernoulli endpoints and fixed reference/design choices are assumed.',
                              'The additional readout-bias budget is zero in the certified rows; preparation allowances are charged explicitly.',
                              'The nominal design assumes exact stationary preparation. Finite target reset waits support only the calibrated rows.',
                              'These sufficient target-specific tests are not asserted optimal and do not apply unchanged to initial/final snapshot data.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                HELPER: hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest()},
              'input_report_sha256': {INPUT: INPUT_SHA},
              'proof_snapshot_sha256': snapshots,
              'imported_repository_verifiers': [HELPER]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'total_endpoints': [x['total_fresh_endpoints'] for x in rows]}))


if __name__ == '__main__':
    main()
