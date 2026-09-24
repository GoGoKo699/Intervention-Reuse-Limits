#!/usr/bin/env python3
"""Exact charge, preparation-boundary and unknown-detector certificates.

Only rational arithmetic and small formal polynomials are used. Imported
moment enclosures and arithmetic are identified by their frozen hashes.
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
INPUT_REPORT = 'reports/switch_snapshot_design.json'
INPUT_SHA = 'b8ee6fb70d37d104ea89fe04e28c8872a8c81f97d108771bd89d14ef2ad9e2cb'
NEW_PROOF_SHA256 = {
    'docs/FAMILIAR_SWITCH_CHARGE_REALIZATION.md': '7d2e175b512a044ee6f99cfbd92ba131a64dc4e929aadf3de3721726a12ac2f7',
    'docs/FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md': '00c4b1c04092f5b929dec5f921cb64e21ad221e7cd8f9144474d1922139b847d',
    'docs/FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md': '032eea67448cece0eafadb5ce98ccdf67194be50170c60fb734e2843f419a99e',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def load_inputs():
    payload = (ROOT/INPUT_REPORT).read_bytes()
    require(hashlib.sha256(payload).hexdigest() == INPUT_SHA, 'The numerical premise is the frozen exact snapshot report')
    prior = json.loads(payload)
    for name, digest in prior['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest() == digest, 'Imported certificate source hashes agree')
    for name, digest in prior['proof_snapshot_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'Imported proof hashes agree')
    for name, digest in NEW_PROOF_SHA256.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'Each new proof matches its explicitly frozen expected snapshot')
    spec = importlib.util.spec_from_file_location('physical_interface_exact', ROOT/'scripts'/HELPER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)
    centers = list(map(F, prior['nominal_certificate']['moment_centers_exact']))
    eta = F(1, 2**120)
    return h, prior, [h.Interval(c-eta, c+eta) for c in centers]


def matrix_add(a, b):
    return [[x+y for x, y in zip(row, other)] for row, other in zip(a, b)]


def matrix_scale(a, scalar):
    return [[scalar*x for x in row] for row in a]


def snapshots(h, kernels, law, readout, instrument=None):
    values = []
    for left, right in ((0, 1), (1, 0)):
        kernel = h.mm(kernels[left], kernels[right])
        if instrument is not None:
            kernel = h.mm(instrument, kernel)
        values.extend((sum(law[i]*kernel[i][j]*readout[j] for i in range(len(law)) for j in range(len(law))),
                       sum(law[i]*kernel[i][j]*readout[i]*readout[j] for i in range(len(law)) for j in range(len(law)))))
    return values


def witness(values, sign, u=F(4, 5)):
    m, c, l, d = values
    return u*c-u*(1+sign*m)*d+sign*(u-m)*l


def charge_checks(h):
    J, field = [h.Poly.variable(2, i) for i in range(2)]
    for s, z in product((-1, 1), repeat=2):
        n1, n2 = F(1+s, 2), F(1-z, 2)
        energy = 4*J*n1*n2+(-2*J-2*field)*n1-2*J*n2
        require(energy == -J*s*z-field*s-J-field, 'The charge-to-conformation energy identity includes its additive constant')
    t = F(4, 5)
    states = list(product((-1, 1), repeat=2))
    for m, ratio in product((F(0), F(4, 5)), (F(2, 3), F(1), F(2))):
        physical, law, _ = h.physical_generator(t, m)
        charge = [[F(0)]*4 for _ in range(4)]
        for i, (s, z) in enumerate(states):
            n1, n2 = (1+s)//2, (1-z)//2
            for coordinate in (0, 1):
                destination = (-s, z) if coordinate == 0 else (s, -z)
                j = states.index(destination)
                if coordinate == 0:
                    addition_factor, occupation, attempt = F(81)**n2/(9*((1+m)/(1-m))), n1, F(1)
                else:
                    addition_factor, occupation, attempt = F(81)**n1/9, n2, ratio
                    physical[i][j] *= ratio
                charge[i][j] = attempt*(addition_factor if occupation else 1)/(1+addition_factor)
            charge[i][i] = -sum(charge[i])
            physical[i][i] = -sum(physical[i][j] for j in range(4) if j != i)
        require(charge == physical, 'Independent Fermi addition/removal rates reproduce the rational heat-bath generator')
        require(h.mm([law], charge) == [[F(0)]*4]
                and all(law[i]*charge[i][j] == law[j]*charge[j][i] for i, j in product(range(4), repeat=2)),
                'The unequal-attempt physical generator has the shared Gibbs equilibrium and ordinary detailed balance')
    m, r = [h.Poly.variable(2, i) for i in range(2)]
    denominator = 2*(125-80*m*m)
    L, q21, q31 = 45*(1+m), 5*(1-m)*(57+48*m), (1-m)*(21-24*m)
    q = [[0, F(23, 33)*L, F(10, 33)*L],
         [q21, 0, F(10, 33)*(3*r*denominator-q21)],
         [q31, (3*r*denominator-23*q31)/33, 0]]
    for i in range(3):
        q[i][i] = -sum(q[i])
    coordinates = [[1, -1, -t], [1, 1, -2*t], [1, 1, F(26, 25)]]
    reduced = [[0, 90*m, 0], [0, -denominator, r*t*denominator], [0, 200*(1-m*m), -r*denominator]]
    require(h.mm(q, coordinates) == h.mm(coordinates, reduced), 'Cleared polynomial identities establish both controlled mean equations for every field and attempt ratio')
    law0 = [F(1, 2), F(1, 22), F(5, 11)]
    tilted = [p*(1+m*row[1]) for p, row in zip(law0, coordinates)]
    require(h.mm([tilted], q) == [[h.Poly(2)]*3], 'The same formal polynomial calculation proves full stationarity of the tilted three-state law')
    require(h.determinant(coordinates) != 0 and h.mm([tilted], coordinates) == [[1, m, t*m]], 'The closed coordinates form a basis and match the physical equilibrium means')
    for sign in (-1, 1):
        mass = sum(p for p, row in zip(law0, coordinates) if row[1] == sign)
        require(mass == F(1, 2) and sum(p*row[2] for p, row in zip(law0, coordinates) if row[1] == sign)/mass == sign*t,
                'Both readout sectors have the physical conditional initial coordinate mean')
    require(q31-F(21, 250)*denominator == F(9, 25)*m*(104*m-125), 'The nonnegative-field q31 upper bound has the stated exact polynomial certificate')
    lo, hi = -F(1, 10000), F(81, 100)
    require(2*(125-80*hi*hi) > 0 and 104*hi < 125, 'The common denominator and q31 sign factors are valid on the full field interval')
    q21lo, q21hi, q31lo, q31hi = F(19, 200), F(22801, 20000), F(741, 625000), F(17, 200)
    require((1-hi)/2 == q21lo and (1-lo+2*t*t)/2 == q21hi
            and (1-hi)*(21-24*hi)/250 == q31lo, 'The direct interval rate bounds have the asserted exact constants')
    require((1-lo)*(21-24*lo) < F(4201, 200) and 2*(125-80*lo*lo) > 249
            and F(4201, 200)/249 < q31hi, 'The small negative-field portion obeys the q31 upper bound')
    lower_L = 9*(1+lo)/50
    lower_rates = [F(23, 33)*lower_L, F(10, 33)*lower_L, q21lo,
                   F(10, 33)*(2-q21hi), q31lo, (2-23*q31hi)/33]
    require(min(lower_rates) > F(1, 1000), 'All six predictive rates are uniformly strictly above one per thousand for every ratio at least two thirds')
    upper_L = 9*(1+hi)/(2*(25-16*hi*hi))
    require(max(upper_L, (23*q21hi+60)/33, (10*q31hi+6)/33) < 3,
            'Every predictive exit rate is below three when the attempt ratio is at most two')
    p, odds = [h.Poly.variable(2, i) for i in range(2)]
    denominator = (odds+1)*(1+(odds*odds-1)*p)
    numerator = (odds-1)*(1+(odds*odds-1)*p)-(odds+1)*(odds*odds-1)*p*(1-p)
    require(numerator == (odds-1)*((odds+1)*p-1)**2,
            'The sharp binary spectator-tilt TV bound reduces to a nonnegative square after clearing its positive denominator')
    require(F(1, 2)*F(2, 100000) == F(1, 100000) and 2*F(2, 100000) == F(4, 100000),
            'The spectator field and charge-energy tolerances imply the advertised force-law budget')
    return {'time_unit': 'inverse observed-dot attempt rate', 'attempt_ratio_interval_exact': ['2/3', '2'],
            'field_tanh_interval_exact': ['-1/10000', '81/100'], 'all_predictive_offdiagonal_lower_exact': '1/1000',
            'predictive_exit_upper_exact': '3', 'predictive_auxiliary_coordinates_exact': ['-4/5', '-8/5', '26/25'],
            'predictive_zero_law_exact': list(map(str, law0)),
            'scope': 'The exact energy, Fermi-rate, closure and positivity statements are mathematical checks under the physical-model assumptions in the note. No device realization, unchanged unequal-rate numerical gap or new sampling allocation is claimed.'}


def preparation_checks(h):
    pi0, nu, piH = [F(1, 2), F(1, 4), F(1, 4)], [F(1, 2), F(1, 8), F(3, 8)], [F(9, 10), F(1, 20), F(1, 20)]
    readout, identity = [1, -1, -1], h.identity(3)
    P0, PH = [pi0[:] for _ in range(3)], [piH[:] for _ in range(3)]
    reset = [[F(18, 19), F(1, 19), 0], [F(18, 19), F(1, 19), 0], [0, 0, 1]]
    require(h.mm(reset, reset) == reset and h.mm(reset, PH) == h.mm(PH, reset) == PH,
            'The high-field reset projections commute and are exactly idempotent')
    e0 = matrix_scale(matrix_add(identity, P0), F(1, 2))
    eh = matrix_add(matrix_scale(matrix_add(identity, reset), F(1, 4)), matrix_scale(PH, F(1, 2)))
    q0 = matrix_add(P0, matrix_scale(identity, -1))
    qh = matrix_add(matrix_add(PH, reset), matrix_scale(identity, -2))
    projectors = [PH, matrix_add(reset, matrix_scale(PH, -1)), matrix_add(identity, matrix_scale(reset, -1))]
    for index, projector in enumerate(projectors):
        require(h.mm(qh, projector) == matrix_scale(projector, -index), 'The exact projection decomposition certifies the logarithmic-time continuous-time propagator')
    for law, q, kernel in ((pi0, q0, e0), (piH, qh, eh)):
        require(all(q[i][j] > 0 and law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(3), repeat=2) if i != j)
                and h.mm([law], kernel) == [law], 'Both counterexample kernels are stationary reversible propagators of positive-rate generators scaled by log two')
    require(sum(pi0[i]*readout[i] for i in range(3)) == sum(nu[i]*readout[i] for i in range(3)) == 0
            and nu != pi0 and q0[1][0] == q0[2][0] == F(1, 2) == q0[0][1]+q0[0][2],
            'The nonstationary balanced preparation has exactly the same strongly lumped low-only binary process')
    values = snapshots(h, [e0, eh], nu, readout)
    require(values == [F(723, 1520), F(65, 304), F(339, 1520), F(65, 304)], 'Independent matrix multiplication reproduces the preparation counterexample moments')
    require(witness(values, -1) == F(20853, 2310400) and witness(values, 1) == -F(20853, 2310400),
            'An ordinary three-state nonstationary preparation violates both stationary witness branches')
    law, high_law, s = [F(1, 2)]*2, [F(9, 10), F(1, 10)], [1, -1]
    reset0, resetH = [law[:] for _ in range(2)], [high_law[:] for _ in range(2)]
    kernels = [matrix_scale(matrix_add(h.identity(2), P), F(1, 2)) for P in (reset0, resetH)]
    require(h.mm([law], reset0) == [law] and h.mm(reset0, reset0) == reset0, 'The disturbing instrument preserves the entire equilibrium hidden marginal')
    disturbed = snapshots(h, kernels, law, s, reset0)
    require(disturbed == [F(2, 5), 0, F(1, 5), 0] and witness(disturbed, 1) == F(2, 25)
            and witness(disturbed, -1) == -F(2, 25), 'An independent hidden reset destroys recorded correlations while leaving both endpoint means unchanged')
    undisturbed = snapshots(h, kernels, law, s)
    require(disturbed[::2] == undisturbed[::2] and disturbed[1::2] != undisturbed[1::2], 'The example separates endpoint agreement from initial/final joint-law agreement')
    a1, a2, x12, x21, bias, f0, f1, f2 = [h.Poly.variable(8, i) for i in range(8)]
    delta_KminusI = bias*((a1-a2)*f0+(-a1-x12-x21)*f1+(a2+x12+x21)*f2)
    kstar, delta_f = (a1+a2)/2+x12+x21, bias*(f1-f2)
    require(delta_KminusI == -kstar*delta_f+bias*(a1-a2)*(f0-(f1+f2)/2), 'The contrast lemma row identity holds formally for arbitrary stochastic-row parameters and response values')
    require(bias*((a1-a2)*(-1)+(-a1-x12-x21)+(a2+x12+x21)) == -2*bias*(a1-a2),
            'The observed contrast drift has the exact coefficient used by the preparation lemma')
    pi, actual = [F(1, 2), F(3, 10), F(1, 5)], [F(1, 2), F(1, 10), F(2, 5)]
    kernel = h.identity(3)
    for i, j in ((0, 1), (1, 2), (2, 0)):
        kernel[i][j] += F(1, 100)/pi[i]
        kernel[i][i] -= F(1, 100)/pi[i]
    require(h.mm([pi], kernel) == [pi] and pi[0]*kernel[0][1] != pi[1]*kernel[1][0], 'The response-specific preparation fixture is stationary but nonreversible')
    signs = [-1, 1, 1]
    relaxation = 1-sum(actual[i]*signs[i]*kernel[i][j]*signs[j] for i, j in product(range(3), repeat=2))
    contrast = sum(actual[i]*kernel[i][j]*signs[j] for i, j in product(range(3), repeat=2))
    ks = (kernel[1][0]+kernel[2][0])/2+kernel[1][2]+kernel[2][1]
    require(0 < relaxation <= 4*ks, 'The observable relaxation denominator is controlled by the hidden row contrast')
    for f in product((-1, 1), repeat=3):
        error = abs(sum((actual[i]-pi[i])*f[i] for i in range(3)))
        drift = sum(actual[i]*(sum(kernel[i][j]*f[j] for j in range(3))-f[i]) for i in range(3))
        require(error <= 4*(abs(drift)+abs(contrast))/relaxation, 'The response-specific preparation bound holds on the bounded nonreversible fixture')
    return {'nonstationary_counterexample_moments_exact': list(map(str, values)),
            'nonstationary_witness_minus_exact': '20853/2310400', 'disturbance_counterexample_moments_exact': list(map(str, disturbed)),
            'contrast_lemma_formal_identity_checked': True,
            'scope': 'The commuting projection identities certify genuine continuous-time examples without floating logarithms. The universal preparation lemma is analytic; a formal row identity and a nonreversible fixture test its mechanism. No observable calibration or new sampling claim follows.'}


def unknown_detector_checks(h, moments):
    u0, low = F(4, 5), F(49, 50)
    m, c, l, d = moments
    for a, b in product((low, F(1)), repeat=2):
        da = b*u0*(c-d+b*m*d)
        db = a*u0*(c-d)-u0*l+2*a*b*u0*m*d+2*b*m*l
        gradient = 3*u0+b*(u0*a*d+l-(1+u0)*m)
        require(da.lo > 0 and db.lo > 0,
                'Positive b times an affine factor and a multiaffine derivative certify target monotonicity')
        require(gradient.hi < F(11, 5), 'Dependency-preserving target corner bounds certify the observed witness gradient mass')
    minimum_R = low*(low*u0*(c-d+low*m*d)-u0*l+low*m*l)
    require(minimum_R.lo > F(343, 200000), 'The worst target contrasts retain the advertised exact witness floor')
    nominal_radius, robust_radius = F(3, 4000), F(31, 50000)
    nominal_floor = F(343, 200000)-F(11, 5)*nominal_radius-F(9, 5)*nominal_radius**2
    robust_floor = F(343, 200000)-F(11, 5)*robust_radius-F(9, 5)*robust_radius**2
    require(nominal_floor == F(5119, 80000000) > 0 and robust_floor > F(7, 20000), 'Both entire observed-moment boxes retain the required positive witness slack')
    # Each interval below includes the whole target contrast square and the
    # allowed candidate moment radius; C-D keeps its shared product factor.
    M = h.Interval(low*m.lo-robust_radius, m.hi+robust_radius)
    C = h.Interval(low*low*c.lo-robust_radius, c.hi+robust_radius)
    L = h.Interval(low*l.lo-robust_radius, l.hi+robust_radius)
    D = h.Interval(low*low*d.lo-robust_radius, d.hi+robust_radius)
    CD = h.Interval((c-d).lo-2*robust_radius, low*low*(c-d).hi+2*robust_radius)
    require(0 < M.lo < M.hi < u0 and L.lo > 0 and D.lo > 0 and CD.hi < -F(3, 100)
            and M.lo*D.lo > F(3, 50), 'The robust candidate box preserves all sign and quantitative corner gates')
    require(max(abs(M.lo), abs(M.hi)) < F(42, 100) and max(abs(C.lo), abs(C.hi)) < F(35, 100)
            and max(abs(L.lo), abs(L.hi)) < F(24, 100) and max(abs(D.lo), abs(D.hi)) < F(40, 100)
            and max(abs(CD.lo), abs(CD.hi)) < F(6, 100), 'The whole detector family and candidate box fit the nuisance-coordinate bounds')
    require(F(11, 5)*nominal_radius+F(9, 5)*nominal_radius**2 < minimum_R.lo,
            'The nominal full moment box excludes every unknown-contrast singleton alternative')
    # Nominal gates use a slightly larger box than the robust case.
    require(low*m.lo-nominal_radius > 0 and m.hi+nominal_radius < u0
            and low*l.lo-nominal_radius > 0 and low*low*d.lo-nominal_radius > 0
            and low*low*(c-d).hi+2*nominal_radius < 0, 'The nominal joint-TV neighborhood also preserves every required sign gate')
    variables = [h.Poly.variable(8, i) for i in range(8)]
    M, C, L, D, v, u, r0, rf = variables
    rpoly = u*(C-D)+u*M*D-(u-M)*L
    sign_reports = {}
    for sign in (-1, 1):
        K = rf*u*(C-D)+sign*(r0*rf*u*L-u*M*D-r0*M*L)
        require(all(all(powers[i] <= 1 for i in (0, 1, 2, 3, 6, 7)) for powers in K.terms),
                'Observed-coordinate and detector-contrast boxes admit exact vertex certification of each witness branch')
        corners = [K.substitute([M, C, L, D, v, u, a, b]) for a, b in ((0, 0), (1, 0), (0, 1), (1, 1))]
        mixture = (1-r0)*(1-rf)*corners[0]+r0*(1-rf)*corners[1]+(1-r0)*rf*corners[2]+r0*rf*corners[3]
        require(K == mixture, 'Bilinear contrast interpolation reduces the whole closed detector square to four corners')
        expected = ([u*M*D, u*M*D+M*L, rpoly+(u-M)*L, rpoly] if sign == -1
                    else [-u*M*D, -u*M*D-M*L, u*(C-D)-u*M*D, 2*u*(C-D)-rpoly])
        require(corners == expected, 'The universal detector-corner identities have the stated sign certificates')
        J = (1+sign*v)*((1+sign*u)*r0*rf*L+u*rf*C)-(r0*L+u*D)*(rf+sign*M)-v*r0*rf*(u*M+sign*(rf*(v+u)-M))
        latent = (1+sign*v)*((1+sign*u)*L+u*C)-(L+u*D)*(1+sign*M)-v*(u*M+sign*(v+u-M))
        require(J.substitute([rf*M, r0*rf*C, rf*L, r0*rf*D, v, u, r0, rf]) == r0*rf*rf*latent,
                'The biased detector numerator equals the latent singleton polynomial times nonnegative contrast factors')
        linear_v = r0*rf*((sign+u)*L+(sign-u)*M-sign*rf*u)+sign*u*rf*C
        require(J == K+v*linear_v-sign*v*v*r0*rf*rf, 'The exact bias expansion supplies the global nuisance bounds without inverse contrasts')
        umax, umin = F(8001, 10000), F(7999, 10000)
        du = F(6, 100)+F(24, 100)+F(42, 100)*F(40, 100)
        dv = ((1-umin)*F(24, 100)+(1+umax)*F(42, 100) if sign == -1
              else (1+umax)*F(24, 100)+(1-umin)*F(42, 100))+umax*F(135, 100)
        require(du == F(468, 1000) and dv == F(1884201 if sign == -1 else 1596201, 10**6), 'The stated global drift constants follow from the bounded observed coordinates')
        qmax, zmax, theta = F(10001, 10000), 1+umax/F(10000), F(1, 100000)
        residual = (12*umax*qmax*zmax*theta+16*zmax*zmax*theta*theta)/(1-umax if sign == 1 else 1+umin)
        residual_bound = F(54 if sign == -1 else 481, 10**6)
        total = (du+dv)/10000+F(1, 10**8)+residual_bound
        band = F(3, 10000) if sign == -1 else F(1, 1000)
        require(residual < residual_bound and total < band, 'Both global biased approximate-force bands are smaller than their observed corner exclusions')
        require((robust_floor if sign == -1 else F(48, 1000)) > band, 'Every unknown rival contrast pair is excluded throughout the robust observed box')
        sign_reports[str(sign)] = {'field_derivative_upper_exact': str(du), 'bias_coefficient_upper_exact': str(dv),
                                  'residual_upper_exact': str(residual_bound), 'necessary_band_upper_exact': str(band)}
    bT, bR = F(800001, 10**10), F(1, 50000)
    require(F(31, 100000)-bT-bR == F(2099999, 10**10) > F(1, 5000), 'Actual preparation, field, timing and backaction costs preserve the final detector-unknown separation')
    return {'target_each_contrast_interval_exact': ['49/50', '1'], 'rival_each_contrast_interval_exact': ['0', '1'],
            'uniform_target_R_lower_exact': '343/200000', 'gradient_mass_upper_exact': '11/5', 'quadratic_mass_exact': '9/5',
            'nominal_recorded_joint_TV_separation_exact': '3/8000', 'stationary_robust_joint_TV_separation_exact': '31/100000',
            'robust_candidate_R_lower_exact': '7/20000', 'nuisance_sign_certificates': sign_reports,
            'actual_recorded_joint_TV_separation_exact': '1/5000', 'constructive_three_state_upper_exact': '1/50000',
            'scope': 'The target may have unknown symmetric bit errors up to one percent; rivals may choose any fixed independent symmetric contrasts in the full unit square. This does not cover asymmetric, state-dependent, correlated or protocol-changing detectors. No old sample-count allocation transfers.'}


def biased_detector_counterexample(h):
    readout, u = [-1, 1, 1], F(4, 5)
    results = []
    for v in (F(0), F(1, 1000)):
        low = [(1-v)/2, (1+v)/4, (1+v)/4]
        high = [p*(1+u*s)/(1+u*v) for p, s in zip(low, readout)]
        kernels, eigenvalues = [], []
        for law, flux in ((low, F(1, 10)), (high, F(1, 20))):
            kernel = h.identity(3)
            kernel[0][1], kernel[1][0] = flux/law[0], flux/law[1]
            kernel[0][0] -= kernel[0][1]
            kernel[1][1] -= kernel[1][0]
            eigenvalue = 1-kernel[0][1]-kernel[1][0]
            require(0 < eigenvalue < 1 and h.mm([law], kernel) == [law]
                    and all(law[i]*kernel[i][j] == law[j]*kernel[j][i] for i, j in product(range(3), repeat=2)),
                    'The biased example has reversible stochastic kernels with positive active-block eigenvalues and hence continuous-time embeddings')
            kernels.append(kernel)
            eigenvalues.append(eigenvalue)
        values = snapshots(h, kernels, low, readout)
        M, C, L, D = values
        R = u*(C-D)+u*M*D-(u-M)*L
        require(0 < M < u and L > 0 and D > 0 and C < D, 'All observed sign gates persist in the biased ordinary example')
        if not v:
            require(values == [F(4, 9), F(13, 45), F(8, 45), F(17, 45)] and R == 0,
                    'The balanced version lies exactly on the ordinary detector-witness boundary')
        else:
            require(R == F(1340051, 4995000000) > 0, 'The small uncharged baseline bias yields the claimed false-positive population witness')
        results.append({'baseline_bias_exact': str(v), 'R_exact': str(R), 'active_kernel_eigenvalues_exact': list(map(str, eigenvalues))})
    return results


def unknown_detector_sampling():
    trials, epsilon = 254000000, F(1, 5000)
    exponent = F(trials)*epsilon*epsilon/2
    term = total = F(1)
    for degree in range(1, 33):
        term *= exponent/degree
        total += term
    require(exponent == F(127, 25) and total > 160 and 8/total < F(1, 20),
            'A positive rational exponential sum certifies the simultaneous four-moment Hoeffding error bound')
    bT, bR = F(800001, 10**10), F(1, 50000)
    null_radius, target_radius = epsilon+2*bR, 2*(bT+bR)+2*epsilon
    require(null_radius == F(3, 12500) and target_radius == F(3000001, 5000000000) < F(31, 50000),
            'The enlarged null confidence box stays inside the independently certified robust target box on the target concentration event')
    require(2*trials == 508000000 and 4*trials == 1016000000,
            'The design counts fresh paired trials separately from their two binary readouts')
    return {'trials_per_protocol': trials, 'total_fresh_paired_trials': 2*trials, 'total_bit_readouts': 4*trials,
            'empirical_moment_error_radius_exact': str(epsilon), 'null_confidence_box_radius_exact': str(null_radius),
            'target_total_moment_radius_exact': str(target_radius), 'type_I_error_upper_exact': '1/20',
            'type_II_error_upper_exact': '1/20', 'observed_box_vertices': 16, 'contrast_corners_per_vertex': 4,
            'required_rejection_gates': ['Every observed-box vertex lies within |M|<=.42, |C|<=.35, |L|<=.24, |D|<=.40 and |C-D|<=.06.',
                                         'Every observed-box vertex satisfies the stated sign gates.',
                                         'At each observed-box vertex and detector corner, K_minus>.0003 and K_plus<-.001.'],
            'scope': 'This new conservative design uses independent fresh trials, an exact composite null, and no model-accuracy allowance. Rejection requires the whole confidence box to satisfy the localization, sign and contrast-corner gates. Analytic Hoeffding and the multiaffine vertex test supply validity and power; only their numerical budgets are certified here. It is not a reuse of the calibrated-detector allocations or an optimality claim.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_physical_interface.json'))
    args = parser.parse_args()
    helper, prior, moments = load_inputs()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrices, sparse formal polynomials and inherited rational moment intervals',
              'charge_realization': charge_checks(helper), 'preparation_boundary': preparation_checks(helper),
              'unknown_detector': unknown_detector_checks(helper, moments),
              'biased_detector_boundary_fixture': biased_detector_counterexample(helper),
              'unknown_detector_sampling': unknown_detector_sampling(),
              'largest_dense_matrix_dimension': 4, 'floating_arithmetic_used': False, 'optimization_used': False,
              'limitations': ['Universal physical-model and all-rival statements remain analytic; numerical intervals and exact algebra certify specified premises.',
                              'Unequal-attempt positivity and mean closure do not establish the previous numerical gap or sample counts at unequal attempts.',
                              'The preparation counterexamples isolate assumptions; they are not fits to the selected target.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                HELPER: hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest()},
              'input_report_sha256': {INPUT_REPORT: INPUT_SHA}, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**prior['proof_snapshot_sha256'], **NEW_PROOF_SHA256}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS, 'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
