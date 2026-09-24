#!/usr/bin/env python3
"""Exact unknown-detector score and necessary-information certificates.

The universal statistical and kinetic implications are analytic. This script
checks their numerical premises with rational intervals and small matrices;
it performs no fitting, floating computation, or sample simulation.
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
    'reports/switch_physical_interface.json': 'b0ada0ff7f600d974fdffc52ea315a071394eb0d7b487d6b8a1ba3d37e303157',
    'reports/switch_snapshot_design.json': 'b8ee6fb70d37d104ea89fe04e28c8872a8c81f97d108771bd89d14ef2ad9e2cb',
}
NEW_PROOF = 'docs/FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md'
NEW_PROOF_SHA = 'b16a3f4fd0e693c46bf281360d54527f190d12be626d4cb8c608bd93acaaf084'
INFORMATION_PROOF = 'docs/FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md'
INFORMATION_PROOF_SHA = 'e0eb4e0de15e2a8be733d34b2900124e8fe8226713babc6bee96d4f644d6428c'
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
        require(hashlib.sha256(payload).hexdigest() == digest, 'The prerequisite report is the frozen reviewed version')
        prior = json.loads(payload)
        require(prior['status'] == 'PASS', 'Every imported numerical certificate passed')
        for name, source_digest in prior['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == source_digest,
                    'The imported certificate source snapshots are intact')
        for name, proof_digest in prior['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == proof_digest,
                    'The imported mathematical proof snapshots are intact')
        priors[path] = prior
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The rational matrix and polynomial helper matches its explicitly pinned source')
    require(hashlib.sha256((ROOT/NEW_PROOF).read_bytes()).hexdigest() == NEW_PROOF_SHA,
            'The new statistical derivation matches its explicitly frozen reviewed snapshot')
    require(hashlib.sha256((ROOT/INFORMATION_PROOF).read_bytes()).hexdigest() == INFORMATION_PROOF_SHA,
            'The new information lower-bound derivation matches its frozen reviewed snapshot')
    spec = importlib.util.spec_from_file_location('uncalibrated_score_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    snapshot = priors['reports/switch_snapshot_design.json']['nominal_certificate']
    centers = list(map(F, snapshot['moment_centers_exact']))
    radius = F(1, 2**120)
    moments = [h.Interval(x-radius, x+radius) for x in centers]
    tables = [[[h.Interval(F(x[0]), F(x[1])) for x in row] for row in table]
              for table in snapshot['joint_law_intervals_exact']]
    return h, priors, moments, centers, tables


def exp_negative_upper(x):
    require(x >= 0, 'The exponential tail argument is nonnegative')
    term = total = F(1)
    for j in range(1, 97):
        term *= x/j
        total += term
    return 1/total


def snapshot_laws(h, exponentials, law, readout):
    tables = []
    for left, right in ((0, 1), (1, 0)):
        kernel = h.mm(exponentials[left], exponentials[right])
        tables.append([[sum(law[i]*kernel[i][j] for i in range(len(law)) for j in range(len(law))
                            if readout[i] == si and readout[j] == sj)
                        for sj in (-1, 1)] for si in (-1, 1)])
    return tables


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
            'The two detector-edge derivatives have the asserted exact polynomial forms')
    difference = L*(u-M)-v*((u-1)*L-(1+u)*M+u)-v*v
    require(branch0.substitute(variables[:7]+[1])-branch1.substitute(variables[:7]+[1]) == difference,
            'The two decreasing detector edges have the asserted endpoint difference')
    R = u*(C-D)+u*M*D-(u-M)*L
    bias = (u-1)*L-u*C-(1+u)*M+u
    require(branch1.substitute(variables[:7]+[1]) == R+v*bias+v*v,
            'The minimum detector corner is the raw witness plus the exact balance correction')
    require(differentiate(R, 5) == C-D-L+M*D,
            'The raw witness field sensitivity has its stated exact form')

    mi, ci, li, di = [h.Interval(*bounds) for bounds in
                       ((F(2, 5), F(21, 50)), (F(8, 25), F(7, 20)),
                        (F(21, 100), F(6, 25)), (F(9, 25), F(2, 5)))]
    vi, ui, fi = h.Interval(-F(1, 10000), F(1, 10000)), h.Interval(F(7999, 10000), F(8001, 10000)), h.Interval(0, 1)
    cd = h.Interval(-F(3, 50), -F(3, 100))
    edge0 = ui*(cd-vi*ci)
    edge1 = ui*(cd-li)+vi*((ui-1)*li-(1+ui)*mi+2*fi*ui-ui*ci)+2*vi**2*fi
    endpoint_difference = li*(ui-mi)-vi*((ui-1)*li-(1+ui)*mi+ui)-vi**2
    require(edge0.hi < 0 and edge1.hi < 0 and endpoint_difference.lo > F(79, 1000),
            'Both detector edges decrease and the final corner r0=rf=1 is the global minimum on the full contrast square')
    du, dv = cd-li+mi*di, (ui-1)*li-ui*ci-(1+ui)*mi+ui
    require(max(abs(du.lo), abs(du.hi)) < F(157, 1000)
            and max(abs(dv.lo), abs(dv.hi)) < F(285, 1000),
            'The local observed box sharply bounds field and stationary-balance drift')
    umax, umin, theta = F(8001, 10000), F(7999, 10000), F(1, 100000)
    qmax, zmax = F(10001, 10000), 1+umax/F(10000)
    residual = (12*umax*qmax*zmax*theta+16*zmax*zmax*theta*theta)/(1+umin)
    require(residual < F(54, 10**6)
            and F(54, 10**6)+(F(157, 1000)+F(285, 1000))/10000+F(1, 10**8) < F(1, 10000),
            'Every minus singleton gives R below one ten-thousandth throughout the local box')
    require(F(4, 5)*mi.lo*di.lo > F(48, 1000)
            and 2*F(4, 5)*cd.hi-F(1, 10000) < -F(48, 1000)
            and F(48, 1000) > F(1, 1000),
            'If R exceeds the local band, all plus corners contradict the inherited plus necessary band')
    return {'observed_coordinate_box_exact': [['2/5', '21/50'], ['8/25', '7/20'], ['21/100', '6/25'], ['9/25', '2/5']],
            'C_minus_D_box_exact': ['-3/50', '-3/100'], 'detector_minimum_corner': [1, 1],
            'field_derivative_absolute_upper_exact': '157/1000', 'balance_coefficient_absolute_upper_exact': '57/200',
            'minus_residual_upper_exact': '27/500000', 'stationary_null_R_upper_exact': '1/10000',
            'scope': 'Derivative and endpoint inequalities certify the full closed detector square, using the analytic singleton residual. They do not impose an interior contrast bound or an inverse detector.'}


def variance(a, b, gamma, mean, correlation, initial):
    score_mean = a*mean+b*correlation+gamma*initial
    second = a*a+b*b+gamma*gamma+2*a*b*initial+2*a*gamma*correlation+2*b*gamma*mean
    return second-score_mean**2


def score_certificate(h, moments, centers):
    u, pivot_m, pivot_a, gamma, low = F(4, 5), F(2, 5), F(13, 25), F(2, 5), F(49, 50)
    m, c, l, d = moments
    mc, cc, lc, dc = centers
    Ms, Cs, Ls, Ds = low*mc, low*low*cc, low*lc, low*low*dc
    As, amax = Ls+u*Ds, lc+u*dc
    bT, bR, tiny = F(800001, 10**10), F(1, 50000), F(1, 10**20)
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
                'All four binary outcomes independently reproduce the fixed score mean and variance formulas')
    require(ranges == [F(66, 25), F(44, 25)] and sum(ranges) == F(22, 5),
            'The two simple rational scores have the stated exact ranges and joint TV sensitivity')
    outcome_order = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    integer_lookup = [[25*((a+b*i)*y+g*i) for i, y in outcome_order] for a, b, g in weights]
    require(integer_lookup == [[23, -43, 3, 17], [-12, 32, -8, -12]],
            'The exact four-outcome integer lookup tables implement the stated scores')
    M, C, L, D, i = [h.Poly.variable(5, j) for j in range(5)]
    T = pivot_a*M+u*C+(pivot_m-u)*L+u*(pivot_m-1)*D-pivot_m*pivot_a
    R = u*(C-D)+u*M*D-(u-M)*L
    require(R-T == (M-pivot_m)*(L+u*D-pivot_a),
            'The exact fixed-score tangent remainder factors into two observable deviations')
    require(weights[0][2]+weights[1][2] == 0 and pivot_m*pivot_a == F(26, 125),
            'The initial-mean control variates cancel under the common initial instrument and preparation')
    target_min = u*low*low*c+pivot_a*low*m+(pivot_m-u)*low*l+u*(pivot_m-1)*low*low*d-pivot_m*pivot_a
    da = u*(c+(pivot_m-1)*d)
    db_min = low*da+pivot_a*m+(pivot_m-u)*l
    require(da.lo > 0 and db_min.lo > 0 and target_min.lo > F(8497, 5000000),
            'The target fixed-score mean increases in both detector contrasts and has the advertised worst-corner floor')
    target_floor = F(1347, 10**6)
    require(F(8497, 5000000)-sum(ranges)*bT > target_floor,
            'All target preparation, field, timing and initial-disturbance errors retain the stated fixed-score mean')

    population = [(Ms-F(1, 500), mc+F(1, 500)), (As-F(1, 250), amax+F(1, 250)),
                  (Cs-F(1, 250), cc+F(1, 250)), (Ls-F(1, 250), lc+F(1, 250)),
                  (Ds-F(1, 250), dc+F(1, 250)), (-F(1, 20), -F(61, 2000))]
    margins = [F(1, 1250), F(17, 10000), F(1, 500), F(1, 500), F(1, 500), F(1, 250)]
    empirical = [(lo+gap, hi-gap) for (lo, hi), gap in zip(population, margins)]
    target_boxes = [(low*m.lo, m.hi), (low*l.lo+u*low*low*d.lo, l.hi+u*d.hi),
                    (low*low*c.lo, c.hi), (low*l.lo, l.hi), (low*low*d.lo, d.hi),
                    ((c-d).lo, low*low*(c-d).hi)]
    require(all(outer[0] < inner[0] <= inner[1] < outer[1] for inner, outer in zip(target_boxes, population)),
            'Every nominal target detector contrast pair lies in the population box used for score-variance monotonicity')
    rows = [('physical', 18560000, 13440000, F(0), F(229, 10**6), F(79, 100000)),
            ('physical_with_model_allowance', 52200000, 37800000, F(1, 10000), F(676, 10**6), F(1, 1000))]
    designs = []
    for label, nA, nB, allowance, null_band, cutoff in rows:
        ER, initial_bound = bR+allowance, F(1, 10000)+2*(bR+allowance)
        mstat = (population[0][0]-2*ER, population[0][1]+2*ER)
        cstat = (population[2][0]-2*ER, population[2][1]+2*ER)
        lstat = (population[3][0]-2*ER, population[3][1]+2*ER)
        dstat = (population[4][0]-2*ER, population[4][1]+2*ER)
        cdstat = (population[5][0]-4*ER, population[5][1]+4*ER)
        for endpoints, broad in zip((mstat, cstat, lstat, dstat, cdstat),
                                    ((F(2, 5), F(21, 50)), (F(8, 25), F(7, 20)),
                                     (F(21, 100), F(6, 25)), (F(9, 25), F(2, 5)),
                                     (-F(3, 50), -F(3, 100)))):
            require(broad[0] < endpoints[0] <= endpoints[1] < broad[1],
                    'Population gates and every admitted null displacement fit the certified stationary box')
        remainder = (mc+F(1, 500)+2*ER-pivot_m)*(pivot_a-As+F(1, 250)+F(18, 5)*ER)
        require(mstat[0] > pivot_m and pivot_a-As+F(1, 250)+F(18, 5)*ER > 0,
                'The stationary tangent remainder has the one-sided sign control used by the null bound')
        systematic = F(1, 10000)+remainder+sum(ranges)*ER
        require(systematic < null_band, 'The local singleton band, one-sided remainder and actual null displacement fit the score ceiling')
        null_variances, target_variances = [F(452, 1000), F(280, 1000)], [F(444, 1000), F(275, 1000)]
        for arm, (a, b, g) in enumerate(weights):
            mean_box, corr_box = ((population[0], population[2]) if arm == 0 else (population[3], population[4]))
            mean_i, corr_i, initial_i = h.Interval(*mean_box), h.Interval(*corr_box), h.Interval(-initial_bound, initial_bound)
            mu = a*mean_i+b*corr_i+g*initial_i
            dm, dcorr, dinitial = 2*b*g-2*a*mu, 2*a*g-2*b*mu, 2*a*b-2*g*mu
            require(dm.hi < 0 and dcorr.hi < 0 and dinitial.lo > 0,
                    'Each score variance decreases in its two recorded moments and increases in the initial mean on the entire population box')
            max_null = variance(a, b, g, mean_box[0], corr_box[0], initial_bound)
            require(max_null < null_variances[arm], 'The exact null variance corner fits its stated uniform ceiling')
            tm, tc = (low*m, low*low*c) if arm == 0 else (low*l, low*low*d)
            nominal_var = variance(a, b, g, tm, tc, F(0))
            require(nominal_var.hi+ranges[arm]**2*bT < target_variances[arm],
                    'The target worst-contrast variance and physical TV displacement fit the target variance ceiling')
        max_step = max(ranges[0]/nA, ranges[1]/nB)
        null_v = null_variances[0]/nA+null_variances[1]/nB
        target_v = target_variances[0]/nA+target_variances[1]/nB
        for gap, var, exponent in ((cutoff-null_band, null_v, F(3)), (target_floor-cutoff, target_v, F(13, 4))):
            adjusted = gap-max_step*exponent/3
            require(adjusted > 0 and adjusted**2 > 2*var*exponent,
                    'Exact rational squared inequalities certify the Bernstein size and power deviations')
        outside_exponents = [F(nA)*margins[0]**2/2,
                             F(nB)*margins[1]**2/(2*(1+u)**2),
                             F(nA)*margins[2]**2/2,
                             F(nB)*margins[3]**2/2,
                             F(nB)*margins[4]**2/2,
                             margins[5]**2/(2*(F(1, nA)+F(1, nB)))]
        require(all(exp_negative_upper(x) < F(1, 20) for x in outside_exponents),
                'If any population gate fails, its empirical pass alone has probability below the allowed false rejection rate')
        target_gate_gaps = [F(3, 2500)-2*bT-tiny, F(23, 10000)-F(18, 5)*bT-tiny,
                            F(1, 500)-2*bT-tiny, F(1, 500)-2*bT-tiny, F(1, 500)-2*bT-tiny]
        require((c-d).lo > -F(203, 5000) and low*low*(c-d).hi < -F(389, 10000)
                and min(-F(203, 5000)-empirical[5][0], empirical[5][1]+F(389, 10000)) >= F(11, 2500),
                'The nominal target contrast family has at least the public difference-gate margin')
        cdgap = F(11, 2500)-4*bT-tiny
        require(min(target_gate_gaps+[cdgap]) > 0,
                'Every target gate has strictly positive margin after physical errors and exact center enclosure')
        gate_exponents = [F(nA)*target_gate_gaps[0]**2/2,
                          F(nB)*target_gate_gaps[1]**2/(2*(1+u)**2),
                          F(nA)*target_gate_gaps[2]**2/2,
                          F(nB)*target_gate_gaps[3]**2/2,
                          F(nB)*target_gate_gaps[4]**2/2,
                          cdgap**2/(2*(F(1, nA)+F(1, nB)))]
        gate_failure = 2*sum(exp_negative_upper(x) for x in gate_exponents)
        require(gate_failure < F(1, 1000), 'A joint Hoeffding union bound certifies all target gates with the stated failure budget')
        designs.append({'case': label, 'paired_trials_0H': nA, 'paired_trials_H0': nB,
                        'total_fresh_paired_trials': nA+nB, 'total_bit_readouts': 2*(nA+nB),
                        'observed_joint_TV_model_allowance_exact': str(allowance), 'null_displacement_exact': str(ER),
                        'initial_mean_absolute_bound_exact': str(initial_bound), 'null_score_mean_upper_exact': str(null_band),
                        'target_score_mean_lower_exact': str(target_floor), 'rejection_cutoff_exact': str(cutoff),
                        'null_variance_ceilings_exact': list(map(str, null_variances)),
                        'target_variance_ceilings_exact': list(map(str, target_variances)),
                        'target_joint_gate_failure_upper_exact': str(h.upper_decimal(gate_failure))})
    require(exp_negative_upper(F(3)) < F(1, 20) and exp_negative_upper(F(13, 4)) < F(1, 25)
            and F(1, 25)+F(1, 1000) < F(1, 20),
            'The separate gate and Bernstein budgets guarantee at most five-percent errors')
    require(F(1, 2**120)*(1+u) < tiny,
            'The fixed tiny center charge exceeds every inherited nominal moment and combined-moment interval radius')
    require(F(508000000, 32000000) == F(127, 8) and F(1, 50000) < F(1, 10000) < F(1, 5000),
            'The stated cost improvement and constructive-versus-ordinary approximation interval follow exactly')
    return {'score_coefficients_exact': [list(map(str, row)) for row in weights],
            'coefficient_order': ['final_bit', 'initial_times_final', 'initial_bit'], 'constant_subtracted_exact': '26/125',
            'outcome_order': [list(row) for row in outcome_order], 'integer_score_lookup_divisor': 25,
            'integer_score_lookup': [[int(x) for x in row] for row in integer_lookup],
            'score_range_widths_exact': list(map(str, ranges)), 'target_nominal_mean_lower_exact': '8497/5000000',
            'target_execution_TV_allowance_exact': str(bT), 'rival_execution_TV_allowance_exact': str(bR),
            'gate_coordinate_order': ['M', 'L+(4/5)D', 'C', 'L', 'D', 'C-D'],
            'population_gate_intervals_exact': [list(map(str, row)) for row in population],
            'empirical_gate_intervals_exact': [list(map(str, row)) for row in empirical],
            'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '1/20',
            'designs': designs,
            'scope': 'The simple scores and all gates are chosen before data collection. Null detector contrasts are arbitrary in the full unit square; target bit errors are each at most one percent. The model allowance enlarges the null joint-law class and is not charged a second time to the target. Independent fresh paired trials remain required.'}


def information_certificate(h, true_targets):
    detector = [[F(99, 100), F(1, 100)], [F(1, 100), F(99, 100)]]
    targets = [h.mm(h.mm(detector, table), detector) for table in true_targets]
    u, law0, readout = F(4, 5), [F(1, 2), F(64436, 10**6), F(435564, 10**6)], [-1, 1, 1]
    laws = [law0, [p*(1+u*s) for p, s in zip(law0, readout)]]
    fluxes = ((41237, 38789, 22424), (20505, 24202, 651))
    generators, exponentials, certificates = [], [], []
    for law, numerators in zip(laws, fluxes):
        q = [[F(0)]*3 for _ in range(3)]
        for (i, j), numerator in zip(((0, 1), (0, 2), (1, 2)), numerators):
            q[i][j], q[j][i] = F(numerator, 10**6)/law[i], F(numerator, 10**6)/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(sum(law) == 1 and min(law) > 0 and h.mm([law], q) == [[F(0)]*3],
                'The fixed ordinary comparator has positive normalized stationary laws')
        require(all(q[i][j] > 0 and law[i]*q[i][j] == law[j]*q[j][i]
                    for i, j in product(range(3), repeat=2) if i != j),
                'The fixed ordinary comparator is irreducible and satisfies detailed balance at both fields')
        exponential, certificate = h.exponential_enclosure(q, F(3, 2))
        generators.append(q)
        exponentials.append(exponential)
        certificates.append(certificate)
    require(max(-q[i][i] for q in generators for i in range(3)) == F(63661, 64436) < 1,
            'The rational comparator has the stated maximum exit rate')
    rivals = snapshot_laws(h, exponentials, law0, readout)
    kls, tvs = [], []
    for target, rival in zip(targets, rivals):
        kl = tv = F(0)
        for target_row, rival_row in zip(target, rival):
            for p, q in zip(target_row, rival_row):
                require(min(p.lo, q.lo) > 0, 'All target and comparator joint cells are strictly interior')
                difference = p-q
                error = max(abs(difference.lo), abs(difference.hi))
                tv += error/2
                kl += error*error/(2*min(p.lo, q.lo))
        require(kl < F(1, 900000), 'Each exact normalized-law Taylor KL majorant is below one over nine hundred thousand')
        kls.append(str(h.upper_decimal(kl)))
        tvs.append(str(h.upper_decimal(tv)))

    def log_ratio(ratio):
        x = (ratio-1)/(ratio+1)
        lower = 2*sum(x**(2*j+1)/F(2*j+1) for j in range(32))
        return h.Interval(lower, lower+2*x**65/(65*(1-x*x)))

    log19 = 4*log_ratio(F(2))+log_ratio(F(19, 16))
    bound = 810000*log19
    ceiling = lambda x: -((-x.numerator)//x.denominator)
    count = ceiling(bound.hi)
    require(F(2)**4*F(19, 16) == 19 and ceiling(bound.lo) == count,
            'Positive atanh logarithm enclosures determine the exact integer information lower count')
    require(F(9, 10)*900000 == 810000,
            'The binary ninety-five-percent testing divergence gives the stated adaptive expected count')
    require(log19.lo > F(44, 15) and F(27, 40)*F(44, 15) == F(99, 50),
            'The unknown-detector information lower bound exceeds the earlier known-detector upper by more than 1.98 on the same noisy target')
    return {'target_each_bit_error_exact': '1/100', 'rival_each_bit_error_exact': '0',
            'readout': readout, 'stationary_laws_exact': [list(map(str, law)) for law in laws],
            'flux_pair_order': [[0, 1], [0, 2], [1, 2]], 'flux_numerators': [list(row) for row in fluxes],
            'flux_denominator': 10**6, 'clock_exact': '3/2',
            'generators_exact': [[[str(x) for x in row] for row in q] for q in generators],
            'maximum_exit_exact': '63661/64436', 'exponential_certificates': certificates,
            'joint_TV_outward_uppers_exact': tvs, 'KL_Taylor_outward_uppers_exact': kls,
            'uniform_KL_upper_exact': '1/900000', 'type_I_and_II_error_upper_exact': '1/20',
            'adaptive_expected_paired_trials_lower_exact': '810000*log(19)',
            'fixed_integer_paired_trials_lower': count,
            'scope': 'This fixed rational ordinary comparator uses a perfect detector while the target has one-percent independent bit errors. The enlarged null permits distinct detector contrasts under different hypotheses. The information bound holds for fresh adaptive selections of the same two protocols; no optimized comparator or universal lower under other controls is claimed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_uncalibrated_score.json'))
    args = parser.parse_args()
    h, priors, moments, centers, tables = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrices, polynomial identities, outward rational intervals and concentration arithmetic',
              'protocols': [[0, 1], [1, 0]], 'stationary_preparation_field': 0,
              'local_null_certificate': local_null_certificate(h),
              'fixed_score_designs': score_certificate(h, moments, centers),
              'necessary_information_cost': information_certificate(h, tables),
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'limitations': ['The kinetic null implication and universal statistical guarantees are analytic; the exact calculations certify their specified numerical premises.',
                              'Independent fresh paired trials are assumed. Waiting or binary balance alone does not certify fresh equilibrium preparation.',
                              'No fixed design or ordinary comparator is asserted globally optimal.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': INPUTS, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**priors['reports/switch_physical_interface.json']['proof_snapshot_sha256'],
                                        NEW_PROOF: NEW_PROOF_SHA, INFORMATION_PROOF: INFORMATION_PROOF_SHA}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS, 'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
