#!/usr/bin/env python3
"""Exact small-matrix premises for percent-scale kinetic robustness.

The universal perturbation and realization arguments are in hash-bound notes.
This verifier uses rational matrix-polynomial arithmetic and outward bounds;
it performs neither a parameter grid search nor numerical optimization.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from math import factorial
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
HELPER = 'verify_familiar_switch_margin.py'
HELPER_SHA = 'e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397'
INPUTS = {
    'reports/switch_weak_field.json': '6289576de985afec146faeef47ef504105bc98ca986c6ce8a8bed70dbb2c6a5d',
    'reports/switch_kinetic_interface.json': 'cfb051fbac02d96c5ae3912f80ab42610be426a90127d70173d8e3bbd33e4472',
}
PROOFS = {
    'docs/FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md': '0a98d76eb922250ceabc3c72d3801b40f12be67330a32b1dd9ba7e3018d78499',
    'docs/FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md': '1e97c8fba182c5c9b320403ceede28b5782d58d6f1c23237a48e272bc51065b4',
    'docs/FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md': '32e9962422ea9943d41dfe708e7926a06bd56cadd2a79c4c791033ea2317c8b8',
}
CHECKS = 0
EDGES = ((0, 1), (0, 2), (1, 3), (2, 3))
ZERO = (0,)*8
EPSILON = F(1, 100)
U = F(3, 5)
CLOCK = F(5, 4)


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def up(value, digits=15):
    scale = 10**digits
    scaled = value*scale
    return F(-((-scaled.numerator)//scaled.denominator), scale)


def down(value, digits=15):
    return -up(-value, digits)


def display_interval(interval):
    return [str(down(interval.lo)), str(up(interval.hi))]


def load_inputs():
    priors = {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected,
                'Each prerequisite report is the explicitly frozen snapshot')
        prior = json.loads(payload)
        require(prior['status'] == 'PASS', 'Each inherited numerical certificate passed')
        for source, digest in prior['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Every inherited source matches its frozen expected hash')
        for proof, digest in prior['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/proof).read_bytes()).hexdigest() == digest,
                    'Every inherited proof matches its frozen expected hash')
        priors[name] = prior
    require(hashlib.sha256((ROOT/'scripts'/HELPER).read_bytes()).hexdigest() == HELPER_SHA,
            'The rational helper has its unconditional expected source hash')
    require(len(PROOFS) == 3 and all(len(value) == 64 for value in PROOFS.values()),
            'All new mathematical proofs have unconditional expected hashes')
    for name, expected in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected,
                'Each new mathematical proof matches its reviewed snapshot')
    spec = importlib.util.spec_from_file_location('percent_kinetics_exact', ROOT/'scripts'/HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper, priors


def zero_matrix():
    return [[F(0)]*4 for _ in range(4)]


def matrix_add_scaled(target, source, scale=F(1)):
    for i, j in product(range(4), repeat=2):
        target[i][j] += scale*source[i][j]


def matrix_polynomial_product(h, left, right, degree=2):
    result = {}
    for alpha, a in left.items():
        for beta, b in right.items():
            powers = tuple(x+y for x, y in zip(alpha, beta))
            if sum(powers) <= degree:
                matrix_add_scaled(result.setdefault(powers, zero_matrix()), h.mm(a, b))
    return result


def coefficient_row_norm(polynomial):
    """Submultiplicative max-row sum over columns AND all coefficients."""
    return max(sum(abs(matrix[i][j]) for matrix in polynomial.values() for j in range(4))
               for i in range(4))


def exponential_polynomial(h, q):
    zero = (0,)*4
    generator = {zero: [[CLOCK*x for x in row] for row in q]}
    for k, (i, j) in enumerate(EDGES):
        edge = zero_matrix()
        edge[i][j], edge[j][i] = q[i][j], q[j][i]
        edge[i][i], edge[j][j] = -q[i][j], -q[j][i]
        powers = tuple(int(k == index) for index in range(4))
        generator[powers] = [[CLOCK*x for x in row] for row in edge]
        require(all(sum(row) == 0 for row in edge),
                'Each independent undirected edge perturbation retains zero row sums')
    require(coefficient_row_norm(generator) <= F(19, 2),
            'The complete coefficient-row norm is bounded by the stated Taylor norm')
    term, total = {zero: h.identity(4)}, {zero: h.identity(4)}
    for order in range(1, 97):
        term = matrix_polynomial_product(h, term, generator)
        for powers, matrix in term.items():
            for i, j in product(range(4), repeat=2):
                matrix[i][j] /= order
            matrix_add_scaled(total.setdefault(powers, zero_matrix()), matrix)
    require(len(total) == 15 and max(map(sum, total)) == 2,
            'Every plateau retains exactly the fifteen coefficients through perturbation degree two')
    return total


def polynomial_width(polynomial, radius=EPSILON):
    return sum(abs(value)*radius**sum(powers)
               for powers, value in polynomial.terms.items() if sum(powers))


def polynomial_interval(h, polynomial, remainder=F(0)):
    center = polynomial.terms.get(ZERO, F(0))
    radius = polynomial_width(polynomial)+remainder
    return h.Interval(center-radius, center+radius)


def polynomial_summary(polynomial):
    encoded = json.dumps([[list(powers), str(value)] for powers, value in sorted(polynomial.terms.items())],
                         separators=(',', ':')).encode()
    return {'coefficient_sha256': hashlib.sha256(encoded).hexdigest(),
            'nonzero_coefficients': len(polynomial.terms),
            'constant_enclosure_exact': [str(down(polynomial.terms.get(ZERO, F(0)))),
                                         str(up(polynomial.terms.get(ZERO, F(0))))],
            'coefficient_l1_by_degree_upper_exact': {
                str(degree): str(up(sum(abs(value) for powers, value in polynomial.terms.items()
                                        if sum(powers) == degree)))
                for degree in range(1, 1+max(map(sum, polynomial.terms)))}}


def perturbation_certificate(h, prior):
    nominal = prior['nominal_certificate']
    generators = [[[F(x) for x in row] for row in q]
                  for q in nominal['physical_generators_exact']]
    laws = [list(map(F, law)) for law in nominal['physical_stationary_laws_exact']]
    readout = [F(-1), F(-1), F(1), F(1)]
    for index, q in enumerate(generators):
        independent_q, law, signs = h.physical_generator(F(4, 5), index*U)
        require(q == independent_q and laws[index] == law and signs == readout,
                'The imported nominal matrices equal the independently reconstructed physical generators')
        require(max(-q[i][i] for i in range(4)) < F(19, 10)
                and laws[1] == [p*(1+U*s) for p, s in zip(laws[0], readout)],
                'The exit-rate norm and fixed Gibbs force law hold at both plateaus')
        for i, j in EDGES:
            require(law[i]*q[i][j] == law[j]*q[j][i],
                    'Every separately scaled undirected edge preserves its equilibrium flux equality')
    plateaus = [exponential_polynomial(h, q) for q in generators]
    embedded = [{(powers+(0,)*4 if index == 0 else (0,)*4+powers): matrix
                 for powers, matrix in plateau.items()} for index, plateau in enumerate(plateaus)]
    moments = []
    for first, second in ((0, 1), (1, 0)):
        kernel = matrix_polynomial_product(h, embedded[first], embedded[second])
        for correlation in (False, True):
            moments.append(h.Poly(8, {powers: sum(laws[0][i]*(readout[i] if correlation else 1)
                                                  *matrix[i][j]*readout[j]
                                                  for i, j in product(range(4), repeat=2))
                                      for powers, matrix in kernel.items()}))
    one_plateau = []
    for index, correlation in ((0, True), (1, False)):
        one_plateau.append(h.Poly(8, {powers: sum(laws[0][i]*(readout[i] if correlation else 1)
                                                       *matrix[i][j]*readout[j]
                                                       for i, j in product(range(4), repeat=2))
                                          for powers, matrix in embedded[index].items()}))
    taylor_tail = F(19, 2)**97/factorial(97)/(1-F(19, 2)/98)
    low_degree_norm = 1+F(19, 4)+F(19, 4)**2/2
    coefficient_error = 2*taylor_tail*low_degree_norm+taylor_tail*taylor_tail
    dyson_argument = F(19, 2)*EPSILON
    remainder = dyson_argument**3/(6*(1-dyson_argument/4))+coefficient_error
    one_argument = dyson_argument/2
    one_remainder = one_argument**3/(6*(1-one_argument/4))+taylor_tail
    require(taylor_tail < F(1, 10**55) and coefficient_error < F(1, 10**53),
            'The exact Taylor coefficient errors satisfy the asserted negligible bounds')
    require(remainder < F(146373, 10**9) and one_remainder < F(181, 10**7),
            'The two-plateau and one-plateau Dyson remainders fit their public rational ceilings')
    centers = list(map(F, nominal['moment_centers_exact']))
    require(all(abs(poly.terms[ZERO]-center) < coefficient_error+F(1, 2**120)
                for poly, center in zip(moments, centers)),
            'The new polynomial constants agree with the frozen nominal moment enclosures')
    intervals = [polynomial_interval(h, poly, remainder) for poly in moments]
    return {'independent_edge_count': 8, 'relative_edge_interval_exact': ['99/100', '101/100'],
            'edge_order_per_plateau': [list(edge) for edge in EDGES],
            'perturbation_polynomial_degree': 2, 'matrix_taylor_degree': 96,
            'plateau_coefficient_count': 15,
            'coefficient_norm': 'max_i sum_j sum_alpha abs(A_alpha[i,j])',
            'two_plateau_Dyson_argument_exact': str(dyson_argument),
            'two_plateau_moment_remainder_upper_exact': str(up(remainder)),
            'one_plateau_moment_remainder_upper_exact': str(up(one_remainder)),
            'Taylor_coefficient_error_upper_exact': str(F(1, 10**53)),
            'moment_order': ['m', 'c', 'l', 'd'],
            'latent_moment_enclosures_exact': [display_interval(interval) for interval in intervals],
            'moment_polynomial_certificates': [polynomial_summary(poly) for poly in moments]}, moments, one_plateau, remainder, one_remainder


def divide_interval(h, numerator, denominator):
    require(denominator.lo > 0 or denominator.hi < 0,
            'Every interval division excludes a zero denominator')
    return numerator*h.Interval(1/denominator.hi, 1/denominator.lo)


def logarithm_interval(h, value):
    require(value > 0, 'Each scalar logarithm has a positive rational argument')
    z = (value-1)/(value+1)
    total = 2*sum(z**(2*k+1)/F(2*k+1) for k in range(256))
    radius = 2*abs(z)**513/(513*(1-z*z))
    require(radius < F(1, 10**40), 'The scalar logarithm series has its asserted exact tail bound')
    return h.Interval(total-radius, total+radius)


def realization_certificate(h, prior, moments, single, remainder, one_remainder):
    coordinates = [[F(1), F(-1), F(0)], [F(1), F(1), -F(12, 5)],
                   [F(1), F(1), F(6, 25)]]
    inverse = [[x/h.determinant(coordinates) for x in row] for row in h.adjugate(coordinates)]
    pi0 = [F(1, 2), F(1, 22), F(5, 11)]
    signs = [F(-1), F(1), F(1)]
    pih = [p*(1+U*s) for p, s in zip(pi0, signs)]
    require(h.mm(coordinates, inverse) == h.identity(3)
            and h.mm([pi0], coordinates) == [[F(1), F(0), F(0)]]
            and h.mm([pih], coordinates) == [[F(1), U, F(0)]],
            'The fixed predictive basis has the asserted inverse and both stationary coordinates')
    nominal_q = prior['nominal_certificate']['exact_three_state_predictor']['generators_exact']
    nominal_b = []
    for q in nominal_q:
        kernel, _ = h.exponential_enclosure([[F(x) for x in row] for row in q], CLOCK)
        nominal_b.append(h.mm(h.mm(inverse, kernel), coordinates))
    xstar, z, y, w = nominal_b[0][1][1], nominal_b[0][1][2], nominal_b[0][2][1], nominal_b[0][2][2]
    astar, cstar, bstar, d = nominal_b[1][1][1], nominal_b[1][1][2], nominal_b[1][2][1], nominal_b[1][2][2]
    xpoly, high_mean = single
    m, c, ell, corr_d = moments
    require(m == high_mean and (ell+U*corr_d)/U == xpoly,
            'Stationarity identities reduce the fitted x and a to single-plateau polynomials exactly')
    apoly = 1-high_mean/U
    axpoly = apoly*xpoly
    bnum, cnum = c-axpoly, corr_d-axpoly
    xmax = abs(xpoly.terms[ZERO])+polynomial_width(xpoly)
    amax = abs(apoly.terms[ZERO])+polynomial_width(apoly)
    numerator_error = remainder+one_remainder*(amax+xmax/U)+one_remainder**2/U
    xbound = polynomial_interval(h, xpoly, one_remainder)
    abound = polynomial_interval(h, apoly, one_remainder/U)
    bbound = divide_interval(h, polynomial_interval(h, bnum, numerator_error), z)
    cbound = divide_interval(h, polynomial_interval(h, cnum, numerator_error), y)
    fit_radii = [F(2021, 10**6), F(2468, 10**6), F(7022, 10**6), F(3647, 10**6)]
    fitted = [xbound, abound, bbound, cbound]
    nominal_fitted = [xstar, astar, bstar, cstar]
    for actual, nominal, radius in zip(fitted, nominal_fitted, fit_radii):
        require(max(abs(actual.lo-nominal.hi), abs(actual.hi-nominal.lo)) < radius,
                'Each fitted parameter remains inside its certified neighborhood of the nominal kernel')
    low_boxes = [(F(706, 1000), F(717, 1000)), (F(3366, 10000), F(3368, 10000)),
                 (F(1211, 10000), F(1213, 10000)), (F(1726, 10000), F(1729, 10000))]
    high_boxes = [(F(627, 1000), F(638, 1000)), (F(260, 1000), F(285, 1000)),
                  (F(146, 1000), F(161, 1000)), (F(1959, 10000), F(1961, 10000))]
    require(all(lo < actual.lo <= actual.hi < hi for actual, (lo, hi)
                in zip([xbound, y, z, w], low_boxes))
            and all(lo < actual.lo <= actual.hi < hi for actual, (lo, hi)
                    in zip([abound, bbound, cbound, d], high_boxes)),
            'The entire physical percent-kinetic family maps inside the CTMC embedding boxes')
    variables = [h.Poly.variable(8, i) for i in range(8)]
    xs, ys, zs, ws, aa, bb, cc, dd = variables
    low_symbolic = [[1, 0, 0], [0, xs, zs], [0, ys, ws]]
    high_symbolic = [[1, U*(1-aa), -U*cc], [0, aa, cc], [0, bb, dd]]
    symbolic_kernels = [h.mm(h.mm(coordinates, matrix), inverse)
                        for matrix in (low_symbolic, high_symbolic)]
    for matrix, law in zip(symbolic_kernels, (pi0, pih)):
        require(all(sum(row) == 1 for row in matrix) and h.mm([law], matrix) == [law],
                'The complete affine kernel families are stochastic-row and stationary-law identities')
    moments_symbolic = []
    for first, second in ((0, 1), (1, 0)):
        kernel = h.mm(symbolic_kernels[first], symbolic_kernels[second])
        for correlation in (False, True):
            moments_symbolic.append(sum(pi0[i]*(signs[i] if correlation else 1)*kernel[i][j]*signs[j]
                                        for i, j in product(range(3), repeat=2)))
    expected_moments = [U*(1-aa), aa*xs+bb*zs,
                        U*(xs-aa*xs-cc*ys), aa*xs+cc*ys]
    require(moments_symbolic == expected_moments,
            'Direct three-state summation proves the four fitted moment identities as exact polynomials')
    embedding = []
    for index, (boxes, law, lower_l, lower_h, kappa_floor, ratio_floor) in enumerate((
            (low_boxes, pi0, F(1, 10), F(77, 100), F(855, 1000), F(181, 1000)),
            (high_boxes, pih, F(107, 1000), F(7, 10), F(812, 1000), F(191, 1000)))):
        av, bv, cv, dv = [h.Interval(*box) for box in boxes]
        # Both nonconstant blocks have trace a+d and off-diagonal product b*c.
        determinant_low = (av-lower_l)*(dv-lower_l)-bv*cv
        determinant_high = (lower_h-av)*(lower_h-dv)-bv*cv
        determinant_one = (1-av)*(1-dv)-bv*cv
        require(bv.lo > 0 and cv.lo > 0 and (av+dv).lo > 2*lower_l
                and determinant_low.lo > 0 and determinant_high.hi < 0
                and (av+dv).hi < 2 and determinant_one.lo > 0,
                'The exact determinant signs put both distinct nonconstant eigenvalues strictly between zero and one')
        log_l, log_h = logarithm_interval(h, lower_l), logarithm_interval(h, lower_h)
        kappa = divide_interval(h, lower_h*log_l-lower_l*log_h, log_l-log_h)
        require(kappa.lo > kappa_floor,
                'The scalar logarithm certificate gives the asserted monotone kappa lower bound')
        corner_ratios, corner_diagonals = [], []
        for corner in product(*boxes):
            a, b, cvalue, dvalue = corner
            matrix = ([[1, 0, 0], [0, a, cvalue], [0, b, dvalue]] if index == 0 else
                      [[1, U*(1-a), -U*cvalue], [0, a, cvalue], [0, b, dvalue]])
            kernel = h.mm(h.mm(coordinates, matrix), inverse)
            require(all(sum(row) == 1 for row in kernel) and h.mm([law], kernel) == [law],
                    'Every affine corner independently has unit row sums and its designated invariant law')
            corner_diagonals.extend(kernel[i][i] for i in range(3))
            corner_ratios.extend(kernel[i][j]/law[j] for i, j in product(range(3), repeat=2) if i != j)
        require(min(corner_diagonals) > 0 and min(corner_ratios) >= ratio_floor
                and ratio_floor > 1-kappa_floor,
                'All kernel entries and every off-diagonal logarithm entry are strictly positive throughout the box')
        embedding.append({'parameter_box_exact': [list(map(str, box)) for box in boxes],
                          'nonconstant_eigenvalue_lower_bounds_exact': [str(lower_l), str(lower_h)],
                          'kappa_lower_exact': str(kappa_floor),
                          'off_diagonal_stationary_ratio_lower_exact': str(ratio_floor),
                          'minimum_corner_ratio_exact': str(min(corner_ratios)),
                          'minimum_corner_diagonal_exact': str(min(corner_diagonals)),
                          'affine_corner_count': 16})
    return {'coordinate_matrix_exact': [list(map(str, row)) for row in coordinates],
            'stationary_laws_exact': [list(map(str, law)) for law in (pi0, pih)],
            'fitted_parameter_order': ['x', 'a', 'b', 'c'],
            'fitted_parameter_enclosures_exact': [display_interval(interval) for interval in fitted],
            'fitted_parameter_variation_upper_exact': list(map(str, fit_radii)),
            'low_kernel_box_order': ['x', 'y', 'z', 'w'],
            'high_kernel_box_order': ['a', 'b', 'c', 'd'],
            'embedding_certificates': embedding,
            'scope': 'One fixed three-state CTMC pair exactly reproduces both ideal stationary initial/final joint laws for every allowed physical edge tuple. The constructed generators depend on that tuple, not on the selected word. No full path-law or arbitrary-field-word reproduction is asserted.'}


def witness_certificate(h, moments, remainder):
    low = F(49, 50)
    latent = [polynomial_interval(h, polynomial, remainder) for polynomial in moments]
    coarse = [(F(219, 1000), F(223, 1000)), (F(479, 1000), F(487, 1000)),
              (F(124, 1000), F(128, 1000)), (F(498, 1000), F(505, 1000))]
    require(all(lo < actual.lo <= actual.hi < hi for actual, (lo, hi) in zip(latent, coarse)),
            'The complete latent kinetic family lies in the coarse detector-monotonicity box')
    mi, ci, li, di = [h.Interval(*box) for box in coarse]
    contrast = h.Interval(low, 1)
    derivative_initial = contrast*U*(ci-di+contrast*mi*di)
    derivative_final = contrast*U*(ci-di)+2*contrast*contrast*U*mi*di-U*li+2*contrast*mi*li
    require(derivative_initial.lo > 0 and derivative_final.lo > 0
            and (U*ci-F(12, 25)*di).lo > 0 and (F(2, 5)*(mi-li)).lo > 0,
            'Both witness and score strictly increase with each independent detector contrast throughout the kinetic box')
    recorded = [h.Interval(factor*actual.lo, actual.hi)
                for factor, actual in zip((low, low*low, low, low*low), latent)]
    public = [(F(21465, 100000), F(22225, 100000)), (F(46075, 100000), F(48602, 100000)),
              (F(12167, 100000), F(12783, 100000)), (F(47862, 100000), F(50460, 100000))]
    require(all(lo < actual.lo <= actual.hi < hi for actual, (lo, hi) in zip(recorded, public)),
            'All recorded moments obey the advertised strict outward enclosures')
    difference = polynomial_interval(h, moments[1]-moments[3], 2*remainder)
    qbox = (F(-19608, 10**6), F(-17576, 10**6))
    require(qbox[0] < difference.lo <= difference.hi < qbox[1],
            'The correlated difference polynomial certifies the stated latent correlation-difference interval')
    observed = [factor*polynomial for factor, polynomial in zip((low, low*low, low, low*low), moments)]
    m, c, ell, d = observed
    witness = U*(c-d)+U*m*d-(U-m)*ell
    score = F(2, 5)*m+U*c-F(2, 5)*ell-F(12, 25)*d-F(2, 25)
    gradient = U*recorded[3].hi+recorded[2].hi+3*U-(1+U)*recorded[0].lo
    witness_floor = witness.terms[ZERO]-polynomial_width(witness)-gradient*remainder-F(8, 5)*remainder**2
    score_floor = score.terms[ZERO]-polynomial_width(score)-F(47, 25)*remainder
    require(gradient < F(19, 10) and witness_floor > F(389, 100000)
            and score_floor > F(367, 100000),
            'Direct polynomial cancellation yields the uniform witness and fixed-score lower bounds')
    for polynomial, first_bound, second_bound in ((witness, F(21507, 10**6), F(31412, 10**6)),
                                                 (score, F(23330, 10**6), F(42791, 10**6))):
        require(sum(abs(value) for powers, value in polynomial.terms.items() if sum(powers) == 1) < first_bound
                and sum(abs(value) for powers, value in polynomial.terms.items() if sum(powers) == 2) < second_bound,
                'The stated first- and second-degree coefficient masses bound the exact polynomials')
    g = F(1, 1000)
    inherited_box = [(F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
                     (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25))]
    require(all(outer[0] < inner[0]-2*g and inner[1]+2*g < outer[1]
                for inner, outer in zip(public, inherited_box))
            and qbox[0]-4*g > -F(1, 25) and low*low*qbox[1]+4*g < -F(1, 1000),
            'Every joint-TV ball of the stated radius remains inside the inherited stationary singleton box')
    local_floor = F(389, 100000)-F(19, 10)*2*g-F(8, 5)*(2*g)**2
    require(local_floor == F(209, 2500000) > F(7, 100000),
            'The entire joint-TV ball violates the inherited ordinary-three-state witness ceiling')
    eps = F(1, 100000)
    target_budget = 2*eps+(F(1, 2)+F(101, 100)*(F(5, 4)+eps))*eps+F(101, 25)*eps
    rival_budget = 2*eps
    require(target_budget == F(78025101, 10**12) < F(79, 10**6)
            and g-target_budget-rival_budget == F(901974899, 10**12) > F(9, 10000)
            and target_budget < F(1, 12500),
            'The physical interface transfer proves the advertised actual memory interval')
    return {'target_detector_contrast_interval_exact': ['49/50', '1'],
            'recorded_moment_public_enclosures_exact': [list(map(str, box)) for box in public],
            'latent_c_minus_d_enclosure_exact': list(map(str, qbox)),
            'witness_polynomial_certificate': polynomial_summary(witness),
            'score_polynomial_certificate': polynomial_summary(score),
            'witness_lower_exact': '389/100000', 'score_lower_exact': '367/100000',
            'witness_gradient_l1_upper_exact': '19/10',
            'stationary_ordinary_three_state_gap_lower_exact': '1/1000',
            'stationary_general_three_state_error_exact': '0',
            'stationary_state_count_interval_exact': ['0', '1/1000'],
            'target_external_TV_allowance_exact': str(target_budget),
            'rival_external_TV_allowance_exact': str(rival_budget),
            'actual_ordinary_gap_lower_exact': '9/10000',
            'actual_general_three_state_error_upper_exact': '1/12500',
            'actual_state_count_interval_exact': ['1/12500', '9/10000']}, public, qbox


def exp_negative_upper(value):
    require(value >= 0, 'Each concentration exponent is nonnegative')
    term = total = F(1)
    for order in range(1, 41):
        term *= value/order
        total += term
    return 1/total


def variance(a, b, gamma, mean, correlation, initial):
    mu = a*mean+b*correlation+gamma*initial
    return a*a+b*b+gamma*gamma+2*a*b*initial+2*a*gamma*correlation+2*b*gamma*mean-mu**2


def score_certificate(h, prior, recorded_box, difference_box):
    coefficients = [[F(2, 5), F(3, 5), -F(3, 10)], [-F(2, 5), -F(12, 25), F(3, 10)]]
    inherited = prior['fixed_score_designs']
    require(coefficients == [list(map(F, row)) for row in inherited['score_coefficients_exact']]
            and F(inherited['constant_subtracted_exact']) == F(2, 25),
            'The new test retains exactly the frozen integer score coefficients')
    widths, lookup = [], []
    for a, b, gamma in coefficients:
        values = [(a+b*i)*y+gamma*i for i, y in ((1, 1), (1, -1), (-1, 1), (-1, -1))]
        widths.append(max(values)-min(values))
        lookup.append([int(50*value) for value in values])
        mean, correlation, initial = [h.Poly.variable(3, i) for i in range(3)]
        law = lambda i, y: (1+i*initial+y*mean+i*y*correlation)/4
        exact_mean = sum(law(i, y)*((a+b*i)*y+gamma*i) for i, y in product((-1, 1), repeat=2))
        exact_second = sum(law(i, y)*((a+b*i)*y+gamma*i)**2 for i, y in product((-1, 1), repeat=2))
        require(exact_mean == a*mean+b*correlation+gamma*initial
                and exact_second-exact_mean**2 == variance(a, b, gamma, mean, correlation, initial),
                'Direct four-cell summation proves the score variance formula without distributional approximations')
    require(widths == [F(2), F(44, 25)] and sum(widths) == F(94, 25)
            and lookup == [[35, -65, 5, 25], [-29, 59, -11, -19]],
            'The exact score widths and public integer lookup tables agree')
    M, C, L, D = [h.Poly.variable(4, i) for i in range(4)]
    R = U*(C-D)+U*M*D-(U-M)*L
    T = F(2, 5)*M+U*C-F(2, 5)*L-F(12, 25)*D-F(2, 25)
    require(R-T == (M-F(1, 5))*(L+U*D-F(2, 5)) and coefficients[0][2]+coefficients[1][2] == 0,
            'The stationary tangent identity and common-initial-law cancellation hold exactly')
    population = [(F(207, 1000), F(230, 1000)), (F(453, 1000), F(494, 1000)),
                  (F(114, 1000), F(136, 1000)), (F(471, 1000), F(513, 1000)),
                  (F(401, 1000), F(439, 1000)), (F(-31, 1000), F(-6, 1000))]
    empirical = [(F(211, 1000), F(226, 1000)), (F(457, 1000), F(490, 1000)),
                 (F(118, 1000), F(132, 1000)), (F(475, 1000), F(509, 1000)),
                 (F(405, 1000), F(435, 1000)), (F(-25, 1000), F(-12, 1000))]
    margins = [F(1, 250)]*5+[F(3, 500)]
    require(all(inner == (outer[0]+gap, outer[1]-gap)
                for inner, outer, gap in zip(empirical, population, margins)),
            'Every empirical gate has the stated margin from its population gate')
    B, bR, allowance = F(79, 10**6), F(1, 50000), F(1, 5000)
    ER = bR+allowance
    require(allowance > F(1, 12500),
            'The tested ordinary approximation allowance exceeds the constructive general-three-state error')
    reference = [(lo-2*ER, hi+2*ER) for lo, hi in population[:4]]
    broad = [(F(1, 5), F(6, 25)), (F(9, 20), F(1, 2)),
             (F(11, 100), F(7, 50)), (F(23, 50), F(13, 25))]
    require(all(outer[0] < inner[0] <= inner[1] < outer[1] for inner, outer in zip(reference, broad))
            and population[5][0]-4*ER > -F(1, 25) and population[5][1]+4*ER < -F(1, 1000)
            and reference[0][0] > F(1, 5) and population[4][0]-F(16, 5)*ER > F(2, 5),
            'Every passing null population box has a stationary reference in the inherited witness box with positive tangent remainder')
    initial_bound = F(1, 10000)+2*ER
    null_ceiling = F(7, 100000)+sum(widths)*ER
    target_floor = F(367, 100000)-sum(widths)*B
    require(initial_bound == F(27, 50000) and null_ceiling == F(2243, 2500000)
            and target_floor == F(21081, 6250000),
            'The complete-score transfer gives the stated null ceiling, target floor, and initial-mean bound')
    null_variances, target_variances = [F(31, 100), F(27, 100)], [F(3, 10), F(27, 100)]
    null_exact = [F(75348226039, 250000000000), F(65253333919, 250000000000)]
    target_exact = [F(2911934639, 10**10), F(25322527228864, 10**14)]
    for arm, (a, b, gamma) in enumerate(coefficients):
        mean_box, correlation_box = population[2*arm:2*arm+2]
        mean, correlation = h.Interval(*mean_box), h.Interval(*correlation_box)
        mu = a*mean+b*correlation+gamma*h.Interval(-initial_bound, initial_bound)
        require((2*b*gamma-2*a*mu).hi < 0 and (2*a*gamma-2*b*mu).hi < 0
                and (2*a*b-2*gamma*mu).lo > 0,
                'Each score variance decreases with its two moments and increases with its initial mean on the full null box')
        null_corner = variance(a, b, gamma, mean_box[0], correlation_box[0], initial_bound)
        tm, tc = recorded_box[2*arm:2*arm+2]
        require(mean_box[0] < tm[0] <= tm[1] < mean_box[1]
                and correlation_box[0] < tc[0] <= tc[1] < correlation_box[1],
                'The same variance derivative signs cover every stationary kinetic target')
        target_upper = variance(a, b, gamma, tm[0], tc[0], F(0))+widths[arm]**2*B
        require(null_corner == null_exact[arm] < null_variances[arm]
                and target_upper == target_exact[arm] < target_variances[arm],
                'Exact corner substitution and target execution charge prove all stated variance bounds')
    n = 2500000
    cutoff = F(21, 10000)
    VN, VT, W = sum(null_variances)/n, sum(target_variances)/n, F(2, n)
    null_gap = F(2078, 10**6)-null_ceiling-W
    target_gap = target_floor-F(2154, 10**6)-W*F(13, 12)
    require(null_gap > 0 and target_gap > 0
            and null_gap**2-2*VN*3 == F(1, 2500000000) > 0
            and target_gap**2-2*VT*F(13, 4) == F(9851449, 5625000000000000) > 0
            and F(2078, 10**6) < cutoff < F(2154, 10**6),
            'Squared rational Bernstein inequalities separate both population scores from the rejection threshold')
    scalar_distance, A_distance, Q_distance = F(346, 100000), F(358, 100000), F(456, 100000)
    require(all(inner[0]-2*B-outer[0] > scalar_distance and outer[1]-inner[1]-2*B > scalar_distance
                for inner, outer in zip(recorded_box, empirical[:4])),
            'Every physical target has the stated safe distance from all four scalar empirical gates')
    A_box = (recorded_box[2][0]+U*recorded_box[3][0], recorded_box[2][1]+U*recorded_box[3][1])
    Q_box = (difference_box[0], F(49, 50)**2*difference_box[1])
    require(A_box[0]-F(16, 5)*B-empirical[4][0] > A_distance
            and empirical[4][1]-A_box[1]-F(16, 5)*B > A_distance
            and Q_box[0]-4*B-empirical[5][0] > Q_distance
            and empirical[5][1]-Q_box[1]-4*B > Q_distance,
            'Every physical target has the stated safe distances from the combined-moment empirical gates')
    exponents = [n*scalar_distance**2/2, n*A_distance**2/(2*F(8, 5)**2), n*Q_distance**2/4]
    require(exponents == [F(29929, 2000), F(32041, 5120), F(3249, 250)],
            'The target gate exponents equal the public rational values')
    gate_failure = sum(weight*exp_negative_upper(exponent) for weight, exponent in zip((8, 2, 2), exponents))
    outside_exponents = [n*F(1, 250)**2/2, n*F(1, 250)**2/(2*F(8, 5)**2), n*F(3, 500)**2/4]
    require(gate_failure < F(1, 250)
            and all(exp_negative_upper(exponent) < F(1, 20) for exponent in outside_exponents)
            and exp_negative_upper(F(3)) < F(1, 20)
            and exp_negative_upper(F(13, 4)) < F(1, 25)
            and gate_failure+exp_negative_upper(F(13, 4)) < F(11, 250) < F(1, 20),
            'Exact exponential upper bounds prove five-percent size and greater-than-95-percent power')
    return {'score_coefficients_exact': [list(map(str, row)) for row in coefficients],
            'integer_score_lookup_divisor': 50, 'integer_score_lookup': lookup,
            'outcome_order': [[1, 1], [1, -1], [-1, 1], [-1, -1]],
            'constant_subtracted_exact': '2/25', 'paired_trials_per_arm': n,
            'total_fresh_paired_trials': 2*n, 'total_bit_readouts': 4*n,
            'observed_joint_TV_model_allowance_exact': str(allowance),
            'conservative_target_external_TV_allowance_exact': str(B),
            'null_displacement_exact': str(ER), 'null_score_mean_upper_exact': str(null_ceiling),
            'target_score_mean_lower_exact': str(target_floor), 'rejection_cutoff_exact': str(cutoff),
            'null_variance_ceilings_exact': list(map(str, null_variances)),
            'target_variance_ceilings_exact': list(map(str, target_variances)),
            'gate_coordinate_order': ['M', 'C', 'L', 'D', 'A=L+3D/5', 'Q=C-D'],
            'population_gate_intervals_exact': [list(map(str, row)) for row in population],
            'empirical_gate_intervals_exact': [list(map(str, row)) for row in empirical],
            'target_gate_failure_upper_exact': str(up(gate_failure)),
            'type_I_error_upper_exact': '1/20', 'type_II_error_upper_exact': '11/250',
            'scope': 'Fresh independent trials; no independence assumption within a paired trial. Physical promises are supplied assumptions, not consequences of the empirical gates. The approximation allowance enlarges only the ordinary null.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/switch_percent_kinetics.json'))
    args = parser.parse_args()
    h, priors = load_inputs()
    weak = priors['reports/switch_weak_field.json']
    perturbation, moments, one_plateau, remainder, one_remainder = perturbation_certificate(h, weak)
    realization = realization_certificate(h, weak, moments, one_plateau, remainder, one_remainder)
    witness, recorded_box, difference_box = witness_certificate(h, moments, remainder)
    score = score_certificate(h, weak, recorded_box, difference_box)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction matrix polynomials and outward rational intervals',
              'perturbation_certificate': perturbation,
              'local_snapshot_realization': realization,
              'direct_witness_certificate': witness,
              'fixed_score_design': score,
              'largest_dense_matrix_dimension': 4,
              'floating_arithmetic_used': False, 'optimization_used': False,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), HELPER: HELPER_SHA},
              'input_report_sha256': INPUTS, 'imported_repository_verifiers': [HELPER],
              'proof_snapshot_sha256': {**priors['reports/switch_kinetic_interface.json']['proof_snapshot_sha256'], **PROOFS}}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': CHECKS,
                      'largest_dense_matrix_dimension': 4, 'report': str(args.output)}))


if __name__ == '__main__':
    main()
