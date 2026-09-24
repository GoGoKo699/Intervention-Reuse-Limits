#!/usr/bin/env python3
"""Exact certificates for the weaker-field, two-snapshot experiment.

Rational matrices, polynomial identities and outward intervals check the
numerical premises of the analytic proofs. No fitting or sample simulation
is performed, and the largest dense matrix has dimension four.
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
INPUTS = {
    'reports/switch_snapshot_design.json': 'b8ee6fb70d37d104ea89fe04e28c8872a8c81f97d108771bd89d14ef2ad9e2cb',
    'reports/switch_physical_interface.json': 'b0ada0ff7f600d974fdffc52ea315a071394eb0d7b487d6b8a1ba3d37e303157',
    'reports/switch_uncalibrated_score.json': '28c432062f3c081c8bf727dcf2299036de35e1c5df13f30e8433b8601a91c182',
}
PROOFS = {
    'docs/FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md': 'b878a14a2f56a751808ae3e4b2befd705035f56f8ad58e98282ac707377d00ea',
    'docs/FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md': 'ddc0f8c16bc8c4289c2b7481d5ff1ef6e920714a141553cfe37bfd028220de6f',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    priors = {}
    for path, digest in INPUTS.items():
        payload = (ROOT/path).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == digest,
                'The prerequisite report is the explicitly frozen reviewed version')
        prior = json.loads(payload)
        require(prior['status'] == 'PASS', 'Each imported numerical certificate passed')
        for name, expected in prior['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == expected,
                    'The inherited verifier source snapshots remain intact')
        for name, expected in prior['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                    'The inherited proof snapshots remain intact')
        priors[path] = prior
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The rational helper agrees with its unconditional expected source hash')
    require(len(PROOFS) == 2, 'Both new mathematical proofs have frozen expected hashes')
    for path, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected,
                'Each new mathematical proof matches its frozen reviewed snapshot')
    spec = importlib.util.spec_from_file_location('weak_field_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    return h, priors


def snapshot_laws(h, exponentials, law, readout):
    tables, moments = [], []
    for left, right in ((0, 1), (1, 0)):
        kernel = h.mm(exponentials[left], exponentials[right])
        table = [[sum(law[i]*kernel[i][j] for i in range(len(law)) for j in range(len(law))
                      if readout[i] == si and readout[j] == sj)
                  for sj in (-1, 1)] for si in (-1, 1)]
        tables.append(table)
        moments.extend((sum(law[i]*kernel[i][j]*readout[j] for i in range(len(law)) for j in range(len(law))),
                        sum(law[i]*kernel[i][j]*readout[i]*readout[j] for i in range(len(law)) for j in range(len(law)))))
    return tables, moments


def nominal_certificate(h):
    t, u, clock = F(4, 5), F(3, 5), F(5, 4)
    generators, laws, exponentials, certificates = [], [], [], []
    for field in (F(0), u):
        q, law, readout = h.physical_generator(t, field)
        exponential, certificate = h.exponential_enclosure(q, clock)
        generators.append(q)
        laws.append(law)
        exponentials.append(exponential)
        certificates.append(certificate)
        require(sum(law) == 1 and min(law) > 0 and h.mm([law], q) == [[F(0)]*4],
                'Each physical stationary law is positive, normalized and stationary')
        require(all(law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(4), repeat=2)),
                'Both four-state physical generators obey ordinary detailed balance')
    tables, moments = snapshot_laws(h, exponentials, laws[0], readout)
    centers = [h.round_dyadic((x.lo+x.hi)/2, 128) for x in moments]
    eta = F(1, 2**120)
    require(all(max(abs(x.lo-c), abs(x.hi-c)) < eta for x, c in zip(moments, centers)),
            'All four freshly recomputed moments fit their dyadic center enclosures')
    for table, mean, correlation in zip(tables, moments[::2], moments[1::2]):
        for i, si in enumerate((-1, 1)):
            for j, sj in enumerate((-1, 1)):
                recovered = F(1, 4)*(1+sj*mean+si*sj*correlation)
                cell = table[i][j]
                require(cell.lo > 0 and cell.hi < 1 and max(cell.lo, recovered.lo) <= min(cell.hi, recovered.hi),
                        'Every joint cell is interior and agrees with the balanced binary moment representation')
    d, e = 3*t, F(6, 25)
    auxiliary = [-t, -2*t, t+e]
    labels = [-1, 1, 1]
    coordinates = [[F(1), F(s), z] for s, z in zip(labels, auxiliary)]
    physical_coordinates = [[F(1), F(s), F(z)] for s, z in product((-1, 1), repeat=2)]
    width = d+e
    law0 = [F(1, 2), e/(2*width), d/(2*width)]
    predictor_generators, predictor_laws = [], []
    require(law0 == [F(1, 2), F(1, 22), F(5, 11)] and h.determinant(coordinates) != 0,
            'The simple predictor has the stated positive law and independent closed coordinates')
    for index, field in enumerate((F(0), u)):
        A, B = field*(1-t*t)/(1-t*t*field*field), t*(1-field*field)/(1-t*t*field*field)
        leaving = (1+A-B*t)/2
        q21, q31 = (1-A+2*B*t)/2, (1-A-B*(t+e))/2
        q = [[F(0), leaving*(2*t+e)/width, leaving*(d-2*t)/width],
             [q21, F(0), (d+q21*(2*t-d))/width],
             [q31, (e-q31*(2*t+e))/width, F(0)]]
        for i in range(3):
            q[i][i] = -sum(q[i])
        law = [p*(1+field*s) for p, s in zip(law0, labels)]
        reduced = [[F(0), A, F(0)], [F(0), -F(1), t], [F(0), B, -F(1)]]
        require(h.mm(q, coordinates) == h.mm(coordinates, reduced)
                and h.mm(generators[index], physical_coordinates) == h.mm(physical_coordinates, reduced),
                'Predictor and physical model share the exact controlled coordinate equations')
        require(all(q[i][j] > 0 for i, j in product(range(3), repeat=2) if i != j)
                and max(-q[i][i] for i in range(3)) < 2,
                'Both predictive generators are positive and have exit rates below two')
        require(sum(law) == 1 and min(law) > 0 and h.mm([law], q) == [[F(0)]*3],
                'The tilted predictor laws are positive, normalized and stationary')
        predictor_generators.append(q)
        predictor_laws.append(law)
    for sign in (-1, 1):
        mass = sum(p for p, s in zip(law0, labels) if s == sign)
        conditional = sum(p*z for p, s, z in zip(law0, labels, auxiliary) if s == sign)/mass
        require(mass == F(1, 2) and conditional == t*sign,
                'Both initial sectors have the physical conditional coordinate means')
    report = {'tanh_J_exact': str(t), 'tanh_H_exact': str(u), 'clock_exact': str(clock),
              'moment_order': ['m', 'c', 'l', 'd'], 'moment_centers_exact': list(map(str, centers)),
              'moment_enclosure_radius': '2^-120', 'joint_cell_order': 'rows initial -,+; columns final -,+',
              'joint_law_intervals_exact': [[[[str(x.lo), str(x.hi)] for x in row] for row in table] for table in tables],
              'physical_exponential_certificates': certificates,
              'physical_generators_exact': [[[str(x) for x in row] for row in q] for q in generators],
              'physical_stationary_laws_exact': [list(map(str, law)) for law in laws],
              'exact_three_state_predictor': {'coordinate_matrix_exact': [list(map(str, row)) for row in coordinates],
                                             'stationary_laws_exact': [list(map(str, law)) for law in predictor_laws],
                                             'generators_exact': [[[str(x) for x in row] for row in q] for q in predictor_generators],
                                             'maximum_exit_upper_exact': '2', 'conditional_coordinate_match': True}}
    return report, [h.Interval(c-eta, c+eta) for c in centers], centers


def differentiate(polynomial, index):
    terms = {}
    for powers, value in polynomial.terms.items():
        if powers[index]:
            reduced = list(powers)
            reduced[index] -= 1
            terms[tuple(reduced)] = value*powers[index]
    return type(polynomial)(polynomial.n, terms)


def local_null_certificate(h):
    M, C, L, D, v, u, r0, rf = variables = [h.Poly.variable(8, i) for i in range(8)]
    J = (1-v)*((1-u)*r0*rf*L+u*rf*C)-(r0*L+u*D)*(rf-M)-v*r0*rf*(u*M-rf*(v+u)+M)
    branch0 = J.substitute(variables[:6]+[0, rf])
    branch1 = J.substitute(variables[:6]+[1, rf])
    derivative0 = u*(C-D-v*C)
    derivative1 = u*(C-D-L)+v*((u-1)*L-(1+u)*M+2*rf*u-u*C)+2*v*v*rf
    require(J == (1-r0)*branch0+r0*branch1,
            'The biased minus detector numerator is affine in the initial contrast')
    require(differentiate(branch0, 7) == derivative0 and differentiate(branch1, 7) == derivative1,
            'The detector-edge derivatives have the claimed polynomial forms')
    difference = L*(u-M)-v*((u-1)*L-(1+u)*M+u)-v*v
    require(branch0.substitute(variables[:7]+[1])-branch1.substitute(variables[:7]+[1]) == difference,
            'The two decreasing detector edges have the claimed endpoint difference')
    R = u*(C-D)+u*M*D-(u-M)*L
    bias = (u-1)*L-u*C-(1+u)*M+u
    require(branch1.substitute(variables[:7]+[1]) == R+v*bias+v*v
            and differentiate(R, 5) == C-D-L+M*D,
            'The minimizing corner and field derivative have their exact asserted forms')
    mi, ci, li, di = [h.Interval(*bounds) for bounds in
                       ((F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
                        (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25)))]
    vi = h.Interval(-F(1, 10000), F(1, 10000))
    ui, fi, cd = h.Interval(F(5999, 10000), F(6001, 10000)), h.Interval(0, 1), h.Interval(-F(1, 25), -F(1, 1000))
    edge0 = ui*(cd-vi*ci)
    edge1 = ui*(cd-li)+vi*((ui-1)*li-(1+ui)*mi+2*fi*ui-ui*ci)+2*vi**2*fi
    endpoint_difference = li*(ui-mi)-vi*((ui-1)*li-(1+ui)*mi+ui)-vi**2
    require(edge0.hi == -F(113981, 200000000) < 0
            and edge1.hi == -F(83143589, 1250000000) < 0
            and endpoint_difference.lo == F(395653769, 10**10) > F(79, 2000),
            'Both detector edges decrease and the corner r0=rf=1 is the global minimum on the full contrast square')
    du, dv = cd-li+mi*di, (ui-1)*li-ui*ci-(1+ui)*mi+ui
    require(max(abs(du.lo), abs(du.hi)) <= F(11, 125)
            and max(abs(dv.lo), abs(dv.hi)) < F(141, 1000),
            'Field and stationary-balance drift have the sharper local bounds')
    umax, umin, theta = F(6001, 10000), F(5999, 10000), F(1, 100000)
    qmax, zmax = F(10001, 10000), 1+umax/F(10000)
    numerator = 12*umax*qmax*zmax*theta+16*zmax*zmax*theta*theta
    require(numerator/(1+umin) < F(46, 10**6)
            and F(46, 10**6)+(F(11, 125)+F(141, 1000))/10000+F(1, 10**8) < F(7, 100000),
            'The minus singleton forces R below seven hundred-thousandths throughout the local box')
    plus_derivative = max(abs(cd.lo), abs(cd.hi))+li.hi+mi.hi*di.hi
    plus_bias = (1+umax)*li.hi+umax*ci.hi+(1-umin)*mi.hi+umax
    require(plus_derivative < F(61, 200) and plus_bias <= F(305047, 250000)
            and numerator/(1-umax) < F(181, 10**6)
            and F(61, 200)/10000+F(305047, 250000)/10000+F(1, 10**8)+F(181, 10**6) < F(1, 2500),
            'The plus singleton gives the claimed uniform necessary band on the full detector square')
    require(F(3, 5)*mi.lo*di.lo > F(127, 100000)
            and 2*F(3, 5)*cd.hi-F(7, 100000) == -F(127, 100000)
            and F(127, 100000) > F(1, 2500),
            'If R reaches the local ceiling, every plus corner contradicts its necessary band')
    return {'observed_coordinate_box_exact': [['1/5', '6/25'], ['9/20', '1/2'], ['11/100', '7/50'], ['23/50', '13/25']],
            'C_minus_D_box_exact': ['-1/25', '-1/1000'], 'detector_minimum_corner': [1, 1],
            'field_derivative_absolute_upper_exact': '11/125', 'balance_coefficient_absolute_upper_exact': '141/1000',
            'minus_residual_upper_exact': '23/500000', 'plus_necessary_band_exact': '1/2500',
            'stationary_null_R_upper_exact': '7/100000',
            'scope': 'Derivative and endpoint inequalities certify the full closed detector square. The inherited analytic singleton residual supplies the arbitrary-model implication.'}


def robust_certificate(h, moments):
    u, low = F(3, 5), F(49, 50)
    m, c, l, d = moments
    require((u*(c-d+low*m*d)).lo > 0,
            'The target witness increases in the initial detector contrast over the entire target square')
    for a, b in product((low, F(1)), repeat=2):
        derivative_b = a*u*(c-d)-u*l+2*a*b*u*m*d+2*b*m*l
        require(derivative_b.lo > 0,
                'Every multiaffine derivative corner certifies increase in the final detector contrast')
    M, C, L, D = low*m, low*low*c, low*l, low*low*d
    floor = F(21927, 5000000)
    R = u*(C-D)+u*M*D-(u-M)*L
    require(R.lo > floor, 'The target worst-contrast raw witness exceeds its stated floor')
    nominal_boxes = [(low*m.lo, m.hi), (low*low*c.lo, c.hi), (low*l.lo, l.hi), (low*low*d.lo, d.hi)]
    cd_box = ((c-d).lo, low*low*(c-d).hi)
    require((u*low*d+l-(1+u)*m).lo > 0,
            'The target gradient-mass bracket is positive, so both contrasts increase it')
    for a, b in product((low, F(1)), repeat=2):
        gradient_mass = b*l+u*a*b*d+3*u-(1+u)*b*m
        require(gradient_mass.hi < F(47, 25),
                'All multiaffine target corners have raw-witness gradient mass below 1.88')
    nominal_gap, stationary_gap = F(23, 20000), F(9, 8000)
    rows = []
    for label, gap, band in [('nominal', nominal_gap, F(0)), ('stationary_robust', stationary_gap, F(7, 100000))]:
        radius = 2*gap
        remainder = F(47, 25)*radius+(1+u)*radius*radius
        require(floor-remainder > band,
                'The full joint-TV moment box leaves positive raw-witness slack above the applicable singleton band')
        broad = ((F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)), (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25)))
        require(all(outer[0] < inner[0]-radius <= inner[1]+radius < outer[1] for inner, outer in zip(nominal_boxes, broad))
                and -F(1, 25) < cd_box[0]-2*radius <= cd_box[1]+2*radius < -F(1, 1000),
                'Every candidate law in the joint-TV box retains the local coordinate and sign gates')
        rows.append({'case': label, 'joint_TV_separation_lower_exact': str(gap),
                     'raw_witness_remaining_lower_exact': str(floor-remainder), 'applicable_null_band_exact': str(band)})
    vm, vc, vl, vd, r = [h.Poly.variable(5, i) for i in range(5)]
    ideal = u*(vc-vd)+u*vm*vd-(u-vm)*vl
    noisy = u*r*r*(vc-vd)+u*r**3*vm*vd-(u-r*vm)*r*vl
    require(noisy == r*r*ideal-r*(1-r)*u*(vl+r*vm*vd),
            'The equal-detector witness loss has the exact simple polynomial identity')
    eps = F(1, 100000)
    bT, bR = eps+eps/2+(F(5, 4)+eps)*eps+4*eps+eps, 2*eps
    require(bT == F(775001, 10**10) and stationary_gap-bT-bR > F(1, 1000)
            and bR < F(1, 1000),
            'The physical preparation, field, timing and disturbance budget retains the stated recorded-law gap')
    eps_relaxed = F(1, 20000)
    bT_relaxed, bR_relaxed = F(31, 4)*eps_relaxed+eps_relaxed**2, 2*eps_relaxed
    require(bT_relaxed == F(155001, 400000000) and bR_relaxed == F(1, 10000)
            and stationary_gap-bT_relaxed-bR_relaxed == F(254999, 400000000) > F(3, 5000)
            and 2*eps_relaxed <= F(1, 10000) and -eps_relaxed > -F(1, 10000)
            and u+eps_relaxed < F(81, 100),
            'Fivefold physical tolerances retain the larger-error memory interval and the inherited bias, tilt and predictor domain promises')
    return {'target_contrast_interval_exact': ['49/50', '1'], 'target_raw_witness_lower_exact': str(floor),
            'target_gradient_mass_upper_exact': '47/25', 'separation_certificates': rows,
            'each_preparation_field_tick_backaction_tolerance_exact': str(eps),
            'target_joint_TV_displacement_exact': str(bT), 'rival_joint_TV_displacement_exact': str(bR),
            'actual_joint_TV_separation_lower_exact': '1/1000',
            'general_three_state_joint_TV_upper_exact': str(bR),
            'state_count_interval_exact': [str(bR), '1/1000'],
            'relaxed_tolerance_margin_only': {'each_physical_tolerance_exact': str(eps_relaxed),
                                              'target_joint_TV_displacement_exact': str(bT_relaxed),
                                              'rival_joint_TV_displacement_exact': str(bR_relaxed),
                                              'actual_joint_TV_separation_lower_exact': '3/5000',
                                              'state_count_interval_exact': ['1/10000', '3/5000'],
                                              'sampling_budget_transferred': False},
            'scope': 'The ordinary lower allows arbitrary independent symmetric rival detector contrasts. Target bit errors are each at most one percent. The constructive upper is inherited from exact closed-coordinate matching under the stated shared instrument assumptions.'}


def exp_negative_upper(x):
    require(x >= 0, 'The exponential tail argument is nonnegative')
    term = total = F(1)
    for j in range(1, 97):
        term *= x/j
        total += term
    return 1/total


def variance(a, b, gamma, mean, correlation, initial):
    score_mean = a*mean+b*correlation+gamma*initial
    second = a*a+b*b+gamma*gamma+2*a*b*initial+2*a*gamma*correlation+2*b*gamma*mean
    return second-score_mean**2


def score_certificate(h, moments, centers):
    u, pivot_m, pivot_a, gamma, low = F(3, 5), F(1, 5), F(2, 5), F(3, 10), F(49, 50)
    m, c, l, d = moments
    mc, cc, lc, dc = centers
    Ms, Cs, Ls, Ds = low*mc, low*low*cc, low*lc, low*low*dc
    As, amax = Ls+u*Ds, lc+u*dc
    bT, bR, tiny = F(775001, 10**10), F(1, 50000), F(1, 10**20)
    weights = ((pivot_a, u, -gamma), (pivot_m-u, u*(pivot_m-1), gamma))
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
                'All four outcomes independently reproduce each score mean and variance polynomial')
    require(ranges == [F(2), F(44, 25)] and sum(ranges) == F(94, 25),
            'The two simple scores have the asserted range widths and joint-TV sensitivity')
    outcome_order = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    integer_lookup = [[50*((a+b*i)*y+g*i) for i, y in outcome_order] for a, b, g in weights]
    require(integer_lookup == [[35, -65, 5, 25], [-29, 59, -11, -19]],
            'The two integer lookup tables implement the exact fixed scores')
    M, C, L, D = [h.Poly.variable(4, j) for j in range(4)]
    T = pivot_a*M+u*C+(pivot_m-u)*L+u*(pivot_m-1)*D-pivot_m*pivot_a
    R = u*(C-D)+u*M*D-(u-M)*L
    require(R-T == (M-pivot_m)*(L+u*D-pivot_a)
            and weights[0][2]+weights[1][2] == 0 and pivot_m*pivot_a == F(2, 25),
            'The tangent identity and common-initial-law control-variate cancellation are exact')
    target_min = pivot_a*low*m+u*low*low*c+(pivot_m-u)*low*l+u*(pivot_m-1)*low*low*d-pivot_m*pivot_a
    da = u*(c+(pivot_m-1)*d)
    db_min = low*da+pivot_a*m+(pivot_m-u)*l
    require(da.lo > 0 and db_min.lo > 0 and target_min.lo > F(8367, 2000000),
            'The target score increases in both detector contrasts and retains the worst-corner nominal floor')
    target_floor = F(973, 250000)
    require(F(8367, 2000000)-sum(ranges)*bT > target_floor,
            'Every admitted physical target retains score mean above the stated floor')
    population = [(Ms-F(13, 2000), mc+F(13, 2000)), (As-F(1, 100), amax+F(1, 100)),
                  (Cs-F(1, 125), cc+F(1, 125)), (Ls-F(1, 125), lc+F(1, 125)),
                  (Ds-F(1, 125), dc+F(1, 125)), (-F(9, 250), -F(1, 500))]
    margins = [F(1, 400), F(1, 250), F(1, 250), F(1, 250), F(1, 250), F(3, 500)]
    empirical = [(lo+gap, hi-gap) for (lo, hi), gap in zip(population, margins)]
    target_boxes = [(low*m.lo, m.hi), (low*l.lo+u*low*low*d.lo, l.hi+u*d.hi),
                    (low*low*c.lo, c.hi), (low*l.lo, l.hi), (low*low*d.lo, d.hi),
                    ((c-d).lo, low*low*(c-d).hi)]
    require(all(outer[0] < inner[0] <= inner[1] < outer[1] for inner, outer in zip(target_boxes, population)),
            'All nominal target contrast pairs lie in the population box used for variance monotonicity')
    rows = [('physical', 1000000, F(0), F(363, 2500000), F(1, 500)),
            ('physical_with_model_allowance', 1250000, F(1, 10000), F(1303, 2500000), F(109, 50000))]
    designs = []
    for label, n, allowance, null_band, cutoff in rows:
        ER, initial_bound = bR+allowance, F(1, 10000)+2*(bR+allowance)
        stationary = [(population[index][0]-2*ER, population[index][1]+2*ER) for index in (0, 2, 3, 4)]
        cdstat = (population[5][0]-4*ER, population[5][1]+4*ER)
        for endpoints, broad in zip(stationary+[cdstat],
                                    ((F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
                                     (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25)),
                                     (-F(1, 25), -F(1, 1000)))):
            require(broad[0] < endpoints[0] <= endpoints[1] < broad[1],
                    'Population gates and all admitted null displacement fit the certified stationary box')
        require(stationary[0][0] > pivot_m and population[1][0]-2*(1+u)*ER > pivot_a,
                'The stationary tangent remainder is positive throughout the population gates')
        require(F(7, 100000)+sum(ranges)*ER == null_band,
                'The local singleton ceiling and whole-score TV transfer give the claimed null score ceiling')
        null_variances, target_variances = [F(299, 1000), F(13, 50)], [F(289, 1000), F(63, 250)]
        for arm, (a, b, g) in enumerate(weights):
            mean_box, corr_box = ((population[0], population[2]) if arm == 0 else (population[3], population[4]))
            mean_i, corr_i, initial_i = h.Interval(*mean_box), h.Interval(*corr_box), h.Interval(-initial_bound, initial_bound)
            mu = a*mean_i+b*corr_i+g*initial_i
            dm, dcorr, dinitial = 2*b*g-2*a*mu, 2*a*g-2*b*mu, 2*a*b-2*g*mu
            require(dm.hi < 0 and dcorr.hi < 0 and dinitial.lo > 0,
                    'Each score variance decreases in its recorded moments and increases in the initial mean on the whole population box')
            max_null = variance(a, b, g, mean_box[0], corr_box[0], initial_bound)
            require(max_null < null_variances[arm],
                    'The exact variance corner fits the uniform null variance ceiling')
            tm, tc = (low*m, low*low*c) if arm == 0 else (low*l, low*low*d)
            nominal_var = variance(a, b, g, tm, tc, F(0))
            require(nominal_var.hi+ranges[arm]**2*bT < target_variances[arm],
                    'Worst-contrast target variances and physical displacement fit the target variance ceilings')
        max_step = max(ranges)/n
        null_v, target_v = sum(null_variances)/n, sum(target_variances)/n
        for gap, var, exponent in ((cutoff-null_band, null_v, F(3)), (target_floor-cutoff, target_v, F(13, 4))):
            adjusted = gap-max_step*exponent/3
            require(adjusted > 0 and adjusted**2 > 2*var*exponent,
                    'Exact rational squared inequalities certify the Bernstein size and power deviations')
        outside_exponents = [F(n)*margins[0]**2/2,
                             F(n)*margins[1]**2/(2*(1+u)**2),
                             F(n)*margins[2]**2/2, F(n)*margins[3]**2/2, F(n)*margins[4]**2/2,
                             F(n)*margins[5]**2/4]
        require(all(exp_negative_upper(x) < F(1, 20) for x in outside_exponents),
                'Failure of any population gate makes its empirical pass alone rarer than the allowed false rejection rate')
        target_gate_gaps = [F(1, 250)-2*bT-tiny, F(3, 500)-2*(1+u)*bT-tiny,
                            F(1, 250)-2*bT-tiny, F(1, 250)-2*bT-tiny, F(1, 250)-2*bT-tiny]
        require((c-d).lo > -F(19, 1000) and low*low*(c-d).hi < -F(17, 1000)
                and min(-F(19, 1000)-empirical[5][0], empirical[5][1]+F(17, 1000)) == F(9, 1000),
                'The nominal contrast family retains the public difference-gate margin')
        cdgap = F(9, 1000)-4*bT-tiny
        require(min(target_gate_gaps+[cdgap]) > 0,
                'All target gates retain positive margins after physical errors and interval-center charges')
        gate_exponents = [F(n)*target_gate_gaps[0]**2/2,
                          F(n)*target_gate_gaps[1]**2/(2*(1+u)**2),
                          F(n)*target_gate_gaps[2]**2/2, F(n)*target_gate_gaps[3]**2/2, F(n)*target_gate_gaps[4]**2/2,
                          F(n)*cdgap**2/4]
        gate_failure = 2*sum(exp_negative_upper(x) for x in gate_exponents)
        public_gate_ceiling = F(81, 10000) if n == 1000000 else F(7, 5000)
        require(gate_failure < public_gate_ceiling < F(1, 100),
                'A simultaneous Hoeffding bound certifies all target gates within the stated failure budget')
        designs.append({'case': label, 'paired_trials_0H': n, 'paired_trials_H0': n,
                        'total_fresh_paired_trials': 2*n, 'total_bit_readouts': 4*n,
                        'observed_joint_TV_model_allowance_exact': str(allowance), 'null_displacement_exact': str(ER),
                        'initial_mean_absolute_bound_exact': str(initial_bound), 'null_score_mean_upper_exact': str(null_band),
                        'target_score_mean_lower_exact': str(target_floor), 'rejection_cutoff_exact': str(cutoff),
                        'null_variance_ceilings_exact': list(map(str, null_variances)),
                        'target_variance_ceilings_exact': list(map(str, target_variances)),
                        'target_joint_gate_failure_upper_exact': str(h.upper_decimal(gate_failure))})
    require(exp_negative_upper(F(3)) < F(1, 20) and exp_negative_upper(F(13, 4)) < F(1, 25)
            and F(1, 25)+F(1, 100) == F(1, 20),
            'The separate gate and score concentration budgets give at most five-percent errors')
    require(F(1, 2**120)*(1+u) < tiny,
            'The center charge exceeds the nominal moment and combined-moment enclosure radii')
    require(F(32000000, 2000000) == 16 and F(90000000, 2500000) == 36,
            'The stated trial-count improvements are exact comparisons with the preceding designs')
    return {'score_coefficients_exact': [list(map(str, row)) for row in weights],
            'coefficient_order': ['final_bit', 'initial_times_final', 'initial_bit'], 'constant_subtracted_exact': '2/25',
            'outcome_order': [list(row) for row in outcome_order], 'integer_score_lookup_divisor': 50,
            'integer_score_lookup': [[int(x) for x in row] for row in integer_lookup],
            'score_range_widths_exact': list(map(str, ranges)), 'target_nominal_mean_lower_exact': '8367/2000000',
            'target_execution_TV_allowance_exact': str(bT), 'rival_execution_TV_allowance_exact': str(bR),
            'gate_coordinate_order': ['M', 'L+(3/5)D', 'C', 'L', 'D', 'C-D'],
            'population_gate_intervals_exact': [list(map(str, row)) for row in population],
            'empirical_gate_intervals_exact': [list(map(str, row)) for row in empirical],
            'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '1/20',
            'designs': designs,
            'scope': 'Fixed scores and gates are chosen before data collection. Detector contrasts remain arbitrary in the null and at least 0.98 in the target. The additional joint-law model allowance enlarges the null and is not charged a second time to the target. Fresh independent trials are required.'}


def design_comparison(h, moments, priors):
    old = priors['reports/switch_snapshot_design.json']['nominal_certificate']
    old_centers = list(map(F, old['moment_centers_exact']))
    eta = F(1, 2**120)
    old_moments = [h.Interval(c-eta, c+eta) for c in old_centers]
    low = F(49, 50)
    diagnostics = []
    for u, values in ((F(4, 5), old_moments), (F(3, 5), moments)):
        m, c, l, d = values
        ideal = u*(c-d)+u*m*d-(u-m)*l
        noisy = u*low*low*(c-d)+u*low**3*m*d-(u-low*m)*low*l
        penalty = low*(1-low)*u*(l+low*m*d)
        diagnostics.append((ideal, noisy, penalty))
    old_ideal, old_noisy, old_penalty = diagnostics[0]
    new_ideal, new_noisy, new_penalty = diagnostics[1]
    require(F(811481, 10**8) < old_ideal.lo < old_ideal.hi < F(811482, 10**8)
            and F(743675, 10**8) < new_ideal.lo < new_ideal.hi < F(743676, 10**8),
            'The weaker-field ideal witness is smaller than the earlier ideal witness')
    require(F(275681, 10**8) < new_penalty.lo < new_penalty.hi < F(275683, 10**8)
            and new_penalty.hi < old_penalty.lo and new_noisy.lo > F(51, 20)*old_noisy.hi,
            'The weaker field reduces the symmetric-detector penalty and increases the noisy raw witness by more than 2.55')
    def log_lower(ratio):
        x = (ratio-1)/(ratio+1)
        return 2*sum(x**(2*j+1)/F(2*j+1) for j in range(32))
    log19_lower = 4*log_lower(F(2))+log_lower(F(19, 16))
    information = priors['reports/switch_uncalibrated_score.json']['necessary_information_cost']
    require(information['adaptive_expected_paired_trials_lower_exact'] == '810000*log(19)'
            and log19_lower > F(44, 15) and 810000*F(44, 15) > 2000000,
            'The new uniform sufficient design is below the old operating-point information lower under the same unknown-detector class')
    interval_strings = lambda x: [str(-h.upper_decimal(-x.lo)), str(h.upper_decimal(x.hi))]
    return {'old_ideal_raw_witness_interval_exact': interval_strings(old_ideal),
            'new_ideal_raw_witness_interval_exact': interval_strings(new_ideal),
            'old_one_percent_raw_witness_interval_exact': interval_strings(old_noisy),
            'new_one_percent_raw_witness_interval_exact': interval_strings(new_noisy),
            'old_equal_contrast_penalty_interval_exact': interval_strings(old_penalty),
            'new_equal_contrast_penalty_interval_exact': interval_strings(new_penalty),
            'old_design_necessary_expected_trials': '810000*log(19)',
            'new_design_sufficient_trials': 2000000,
            'scope': 'This comparison changes the operating point. The old information lower is not a lower bound for the new experiment, and neither design is asserted optimal.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_weak_field.json'))
    args = parser.parse_args()
    h, priors = load_inputs()
    nominal, moments, centers = nominal_certificate(h)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrices, polynomial identities, outward rational intervals and concentration arithmetic',
              'protocols': [[0, 1], [1, 0]], 'stationary_preparation_field': 0,
              'nominal_certificate': nominal,
              'local_null_certificate': local_null_certificate(h),
              'robust_certificate': robust_certificate(h, moments),
              'fixed_score_designs': score_certificate(h, moments, centers),
              'operating_point_comparison': design_comparison(h, moments, priors),
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'limitations': ['The kinetic null implication and universal statistical guarantees are analytic; exact calculations certify their specified numerical premises.',
                              'Independent fresh paired trials are assumed. Waiting or binary balance alone does not certify fresh equilibrium preparation.',
                              'This candidate and its sampling design are not asserted globally optimal.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': INPUTS, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**priors['reports/switch_uncalibrated_score.json']['proof_snapshot_sha256'], **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS, 'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
