#!/usr/bin/env python3
"""Certify a seven-experiment familiar-switch error margin using exact arithmetic.

Only stdlib rational arithmetic is used. Matrix Taylor remainders enclose the
physical target responses; a translated polynomial bounds an entire error box.
No fitting, floating exponential or eigenvalue is used for the lower bound.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial
import hashlib
import json
from pathlib import Path
import platform


CHECKS = 0
WORDS = ((1,), (1, 1), (1, 1, 1), (1, 0), (1, 1, 0), (1, 0, 1), (1, 1, 0, 1))


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


class Poly:
    """A small sparse multivariate polynomial over the rationals."""

    def __init__(self, n, terms=None):
        self.n = n
        self.terms = {powers: F(value) for powers, value in (terms or {}).items() if value}

    @classmethod
    def variable(cls, n, i):
        return cls(n, {tuple(int(i == j) for j in range(n)): F(1)})

    def coerce(self, value):
        if isinstance(value, Poly):
            assert value.n == self.n
            return value
        return Poly(self.n, {(0,)*self.n: F(value)})

    def __add__(self, other):
        other = self.coerce(other)
        result = self.terms.copy()
        for powers, value in other.terms.items():
            result[powers] = result.get(powers, F(0))+value
        return Poly(self.n, result)

    __radd__ = __add__

    def __neg__(self):
        return Poly(self.n, {powers: -value for powers, value in self.terms.items()})

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        result = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                powers = tuple(x+y for x, y in zip(left, right))
                result[powers] = result.get(powers, F(0))+a*b
        return Poly(self.n, result)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if isinstance(scalar, Poly):
            raise TypeError('Polynomial division is not used in this certificate')
        return Poly(self.n, {powers: value/F(scalar) for powers, value in self.terms.items()})

    def __pow__(self, exponent):
        result = self.coerce(1)
        for _ in range(exponent):
            result = result*self
        return result

    def __eq__(self, other):
        other = self.coerce(other)
        return self.terms == other.terms

    def evaluate(self, values):
        return sum(value*product_value(x**power for x, power in zip(values, powers))
                   for powers, value in self.terms.items())

    def substitute(self, values):
        return sum(value*product_value(x**power for x, power in zip(values, powers))
                   for powers, value in self.terms.items())

    def shifted(self, center):
        result = self.coerce(0)
        for powers, value in self.terms.items():
            term = self.coerce(value)
            for i, power in enumerate(powers):
                if power:
                    expansion = Poly(self.n, {
                        tuple(j if k == i else 0 for k in range(self.n)):
                        F(comb(power, j))*center[i]**(power-j)
                        for j in range(power+1)})
                    term = term*expansion
            result = result+term
        return result


def product_value(values):
    result = 1
    for value in values:
        result *= value
    return result


class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Interval) else Interval(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        corners = [a*b for a, b in product((self.lo, self.hi), (other.lo, other.hi))]
        return Interval(min(corners), max(corners))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if not exponent:
            return Interval(1)
        if exponent % 2:
            return Interval(self.lo**exponent, self.hi**exponent)
        return Interval(0 if self.lo <= 0 <= self.hi else min(self.lo**exponent, self.hi**exponent),
                        max(self.lo**exponent, self.hi**exponent))


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def determinant(a):
    result = 0
    for permutation in permutations(range(len(a))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(a)) for j in range(i+1, len(a)))
        result += (-1)**inversions*product_value(a[i][j] for i, j in enumerate(permutation))
    return result


def adjugate(a):
    return [[(-1)**(i+j)*determinant([[a[row][col] for col in range(len(a)) if col != i]
                                     for row in range(len(a)) if row != j])
             for j in range(len(a))] for i in range(len(a))]


def response_polynomial(sign, u):
    m, n, p, l1, l2, k1, k2 = [Poly.variable(7, i) for i in range(7)]
    c = 1-m/u
    a1, a2 = (p-m)*l1-(n-m)*l2, -n*l1+m*l2
    b1, b2 = (p-m)*(k1-m)-(n-m)*(k2-m), -n*(k1-m)+m*(k2-m)
    variance_numerator = 1-(1-u*u)*n/u-sign*u*(m+sign*c)**2-(1-sign*u)*m*m
    return (1-sign*u)*(b1+c*b2-c*a1)-variance_numerator*a2


def symbolic_checks(u):
    generic = [[Poly.variable(9, 3*i+j) for j in range(3)] for i in range(3)]
    adj, det = adjugate(generic), determinant(generic)
    for actual in (mm(generic, adj), mm(adj, generic)):
        for i, j in product(range(3), repeat=2):
            require(actual[i][j] == (det if i == j else 0),
                    'The generic adjugate identity is an exact polynomial identity without a rank assumption')

    m, n, p, l1, l2, k1, k2, c, raw_second = [Poly.variable(9, i) for i in range(9)]
    v = [[1, 0, m], [1, m, n], [1, n, p]]
    v0 = [[1, 0, m], [1, l1, k1], [1, l2, k2]]
    gram = [[1, 0, m], [0, 1, c], [m, c, raw_second]]
    product_matrix = mm(mm(gram, adjugate(v)), v0)
    skew = product_matrix[1][2]-product_matrix[2][1]
    a1, a2 = (p-m)*l1-(n-m)*l2, -n*l1+m*l2
    b1, b2 = (p-m)*(k1-m)-(n-m)*(k2-m), -n*(k1-m)+m*(k2-m)
    require(skew == b1+c*b2-c*a1-(raw_second-m*m)*a2,
            'The seven-response polynomial equals the exact skew entry of the adjugate Gram product')
    values = [Poly.variable(7, i) for i in range(7)]
    mean, second, third, left1, left2, cross1, cross2 = values
    covariance = 1-mean/u
    polynomials = {}
    for sign in (-1, 1):
        raw = (1-(1-u*u)*second/u-sign*u*(mean+sign*covariance)**2)/(1-sign*u)
        w = response_polynomial(sign, u)
        require((1-sign*u)*skew.substitute(values+[covariance, raw]) == w,
                'The singleton-sector second moment removes the denominator and gives the stated necessary identity')
        length = 1-(1-u*u)*second/u+mean*mean-2*u*mean-sign*u*covariance**2
        aa = (third-mean)*(cross1-mean)-(second-mean)*(cross2-mean)
        bb = mean*(cross2-mean)-second*(cross1-mean)
        tt = mean*left2-second*left1
        uu = (third-mean)*left1-(second-mean)*left2
        alternative = length*tt+(1-sign*u)*covariance*(uu-bb)-(1-sign*u)*aa
        require(w == -alternative, 'Two independently organized scalar identities agree as formal polynomials')
        require(len(w.terms) == 25 and max(map(sum, w.terms)) == 4,
                'The necessary response identity has exactly twenty-five monomials and degree four')
        polynomials[sign] = w
    return polynomials


def words_from_matrices(generators, law, readout):
    responses = []
    for word in WORDS:
        row = [law]
        for field in word:
            row = mm(row, generators[field])
        responses.append(sum(x*y for x, y in zip(row[0], readout)))
    return responses


def reversible_kernel_checks(polynomials, u):
    for sign in (-1, 1):
        readout = [F(sign), -F(sign), -F(sign)]
        law0 = [F(1, 2), F(1, 3), F(1, 6)]
        law_high = [weight*(1+u*s) for weight, s in zip(law0, readout)]
        matrices = []
        for law, fluxes in ((law0, [F(1, 100), F(1, 120), F(1, 150)]),
                            (law_high, [F(1, 400), F(1, 500), F(1, 600)])):
            matrix = identity(3)
            for (i, j), flux in zip(((0, 1), (0, 2), (1, 2)), fluxes):
                matrix[i][j], matrix[j][i] = flux/law[i], flux/law[j]
                matrix[i][i] -= flux/law[i]
                matrix[j][j] -= flux/law[j]
            require(min(value for row in matrix for value in row) > 0
                    and all(sum(row) == 1 for row in matrix),
                    'The independent reversible clock fixture is a positive stochastic matrix')
            require(all(law[i]*matrix[i][j] == law[j]*matrix[j][i]
                        for i, j in product(range(3), repeat=2)),
                    'Both clock fixtures obey detailed balance with the required Gibbs-tilted laws')
            matrices.append(matrix)
        responses = words_from_matrices(matrices, law0, readout)
        require(polynomials[sign].evaluate(responses) == 0,
                'The necessary polynomial vanishes on the independent singleton-sector reversible fixture')
        require(polynomials[-sign].evaluate(responses) != 0,
                'The test fixture distinguishes the two singleton-sector alternatives')
    two_laws = ([F(1, 2)]*2, [(1+u)/2, (1-u)/2])
    two_matrices = []
    for law in two_laws:
        flux = F(1, 100)
        two_matrices.append([[1-flux/law[0], flux/law[0]], [flux/law[1], 1-flux/law[1]]])
    responses = words_from_matrices(two_matrices, two_laws[0], [F(1), -F(1)])
    for sign in (-1, 1):
        require(polynomials[sign].evaluate(responses) == 0,
                'Both identities hold in the singular two-state fixture without an inverse')
        require(polynomials[sign].evaluate([F(0)]*7) == 0,
                'The degenerate identity-clock case is covered without dividing by a response determinant')


def physical_generator(t, u):
    states = list(product((-1, 1), repeat=2))
    index = {state: i for i, state in enumerate(states)}
    r, w = (1+t)/(1-t), (1+u)/(1-u)
    q = [[F(0)]*4 for _ in range(4)]
    weights = []
    for i, state in enumerate(states):
        weights.append(r**int(state[0] == state[1])*w**int(state[0] == 1))
        for site in range(2):
            odds = r**(state[0]*state[1])*(w**state[0] if site == 0 else 1)
            changed = list(state)
            changed[site] *= -1
            q[i][index[tuple(changed)]] = 1/(1+odds)
        q[i][i] = -sum(q[i])
    law = [weight/sum(weights) for weight in weights]
    require(all(sum(row) == 0 for row in q) and max(-q[i][i] for i in range(4)) < 2,
            'The physical target generator has zero row sums and total exit rates below two')
    require(all(law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(4), repeat=2)),
            'The target heat-bath rates satisfy exact ordinary detailed balance')
    require(mm([law], q) == [[F(0)]*4] and min(law) > 0,
            'The exact positive Gibbs preparation is stationary')
    a, b = u*(1-t*t)/(1-t*t*u*u), t*(1-u*u)/(1-t*t*u*u)
    coordinates = [[F(1), F(s), F(z)] for s, z in states]
    reduced = [[0, a, 0], [0, -1, t], [0, b, -1]]
    require(mm(q, coordinates) == mm(coordinates, reduced),
            'The physical generator independently agrees with the closed mean generator')
    return q, law, [F(state[0]) for state in states]


def round_dyadic(value, bits):
    scaled = value*2**bits+F(1, 2)
    return F(scaled.numerator//scaled.denominator, 2**bits)


def exponential_enclosure(q, clock, degree=96, bits=160):
    n = len(q)
    x = [[clock*value for value in row] for row in q]
    norm = max(sum(abs(value) for value in row) for row in x)
    require(norm < degree+2, 'The matrix-exponential tail admits a geometric ratio bound')
    tail = norm**(degree+1)/factorial(degree+1)/(1-norm/F(degree+2))
    require(tail < F(1, 2**180), 'The entire omitted matrix Taylor tail is smaller than 2^-180 in row norm')
    term, total = identity(n), identity(n)
    for order in range(1, degree+1):
        term = [[value/order for value in row] for row in mm(term, x)]
        total = [[a+b for a, b in zip(left, right)] for left, right in zip(total, term)]
    rounded = [[round_dyadic(value, bits) for value in row] for row in total]
    rounding = max(abs(a-b) for left, right in zip(total, rounded) for a, b in zip(left, right))
    require(rounding <= F(1, 2**(bits+1)), 'Every retained Taylor entry has the claimed nearest-dyadic rounding error')
    entry_radius = F(1, 2**bits)
    require(tail+rounding < entry_radius,
            'The dyadic entry radius covers both analytic Taylor remainder and exact rounding')
    enclosure = [[Interval(value-entry_radius, value+entry_radius) for value in row] for row in rounded]
    require(all(sum(row).lo <= 1 <= sum(row).hi for row in enclosure),
            'Each certified exponential row encloses the exact stochastic row sum')
    return enclosure, {'taylor_degree': degree, 'clock_matrix_row_norm_exact': str(norm),
                       'matrix_tail_upper': '2^-180', 'entry_dyadic_bits': bits,
                       'certified_entry_radius': '2^-160'}


def upper_decimal(value, digits=15):
    scaled = value*10**digits
    return F(-((-scaled.numerator)//scaled.denominator), 10**digits)


def target_margin_checks(polynomials, t, u, clock):
    q0, law0, readout = physical_generator(t, F(0))
    qh, law_high, _ = physical_generator(t, u)
    require(law_high == [weight*(1+u*s) for weight, s in zip(law0, readout)],
            'The physical target obeys precisely the rival comparison class Gibbs tilt')
    e0, certificate0 = exponential_enclosure(q0, clock)
    eh, certificate_high = exponential_enclosure(qh, clock)
    responses = words_from_matrices([e0, eh], law0, readout)
    center = [round_dyadic((value.lo+value.hi)/2, 128) for value in responses]
    uncertainty = max(max(abs(value.lo-mid), abs(value.hi-mid)) for value, mid in zip(responses, center))
    require(uncertainty < F(1, 2**120), 'All seven exact target responses lie within 2^-120 of their stated rational centers')
    require(all(-1 < value.lo <= value.hi < 1 for value in responses),
            'Certified response intervals lie in the physical mean range')
    mean_radius = F(1, 1000)
    # Use a convenient outward bound on the target uncertainty in the box radius.
    box_radius = mean_radius+F(1, 2**120)
    reports = {}
    for sign, polynomial in polynomials.items():
        target_value = polynomial.evaluate(responses)
        require(target_value.lo*target_value.hi > 0,
                'The certified target polynomial interval excludes zero for each singleton alternative')
        target_absolute_lower = min(abs(target_value.lo), abs(target_value.hi))
        require(target_absolute_lower > F(1455, 10**7),
                'The true target polynomial magnitude exceeds the public rational lower bound')
        translated = polynomial.shifted(center)
        constant = translated.terms.get((0,)*7, F(0))
        require(constant == polynomial.evaluate(center), 'The translated constant is the exact polynomial value at the certified center')
        require(abs(constant) > F(1455, 10**7),
                'The center polynomial magnitude exceeds the public rational lower bound')
        # Exact re-expansion checks catch a shift-index or coefficient error.
        variables = [Poly.variable(7, i) for i in range(7)]
        require(translated == polynomial.substitute([variable+value for variable, value in zip(variables, center)]),
                'The binomial shift agrees with direct formal substitution as a complete polynomial')
        masses = {degree: sum(abs(coefficient)*box_radius**degree
                             for powers, coefficient in translated.terms.items() if sum(powers) == degree)
                  for degree in range(1, 5)}
        variation = sum(masses.values())
        public_upper = F(1436 if sign == -1 else 425, 10**7)
        require(variation < public_upper < F(1455, 10**7),
                'The full translated polynomial variation on the entire error box is smaller than its nonzero constant')
        require(abs(constant)-variation > F(19, 10**7),
                'Both singleton alternatives retain a strictly positive certified polynomial slack')
        reports[str(sign)] = {
            'target_polynomial_sign': 1 if constant > 0 else -1,
            'target_and_center_absolute_lower_bound_exact': str(F(1455, 10**7)),
            'whole_box_variation_upper_bound_exact': str(public_upper),
            'variation_by_degree_outward_upper_exact': {str(degree): str(upper_decimal(mass)) for degree, mass in masses.items()},
            'polynomial_terms': len(polynomial.terms), 'total_degree': 4}
    require(mean_radius/2 == F(1, 2000), 'Binary occupation error is exactly half the binary mean error')
    report = {'target_parameters': {'tanh_J': str(t), 'tanh_H': str(u), 'J': 'log(3)', 'H': 'log(3)',
                                   'attempt_rates': ['1', '1'], 'clock_tick': str(clock)},
            'zero_field_exponential_certificate': certificate0,
            'high_field_exponential_certificate': certificate_high,
            'target_mean_centers_exact': [str(value) for value in center],
            'target_mean_uniform_enclosure_radius': '2^-120',
            'excluded_uniform_mean_error_exact': str(mean_radius),
            'excluded_uniform_occupation_error_exact': '1/2000',
            'whole_box_radius_exact': str(box_radius),
            'singleton_sign_certificates': reports,
            'strict_polynomial_slack_lower_bound_exact': str(F(19, 10**7)),
            'scope': 'Every response vector within mean error 1/1000 of the physical target makes both necessary singleton-sector polynomials nonzero. The analytic necessary-identity theorem therefore excludes all admissible ordinary models with at most three states, without a rival rate cap. This certificate performs no optimization and asserts no optimal error margin.'}
    return report, responses


def rational_reversible_upper_checks(target_responses, u, clock):
    readout = [-F(1), F(1), F(1)]
    law0 = [F(1, 2), F(61258, 10**6), F(1, 2)-F(61258, 10**6)]
    law_high = [weight*(1+u*s) for weight, s in zip(law0, readout)]
    require(sum(law0) == sum(law_high) == 1 and min(law0+law_high) > 0,
            'The rational three-state comparison model has strictly positive normalized Gibbs-tilted laws')
    flux_numerators = ((110734, 2, 72990), (34039, 15082, 50885))
    generators, exponentials, exponential_certificates = [], [], []
    for law, fluxes in zip((law0, law_high), flux_numerators):
        q = [[F(0)]*3 for _ in range(3)]
        for (i, j), numerator in zip(((0, 1), (0, 2), (1, 2)), fluxes):
            flux = F(numerator, 10**6)
            q[i][j], q[j][i] = flux/law[i], flux/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(all(q[i][j] > 0 for i, j in product(range(3), repeat=2) if i != j)
                and all(sum(row) == 0 for row in q),
                'The rational upper-witness model has positive off-diagonal rates and zero row sums')
        require(all(law[i]*q[i][j] == law[j]*q[j][i] for i, j in product(range(3), repeat=2))
                and mm([law], q) == [[F(0)]*3],
                'The rational upper witness satisfies exact ordinary detailed balance and stationarity')
        require(max(-q[i][i] for i in range(3)) < 3,
                'The upper-witness generators satisfy the optional total exit cap of three')
        enclosure, certificate = exponential_enclosure(q, clock, degree=128)
        generators.append(q)
        exponentials.append(enclosure)
        exponential_certificates.append(certificate)
    require(max(-q[i][i] for q in generators for i in range(3)) == F(91862, 30629),
            'The maximum witness exit rate has the stated exact value')
    responses = words_from_matrices(exponentials, law0, readout)
    error_bounds = []
    for actual, target in zip(responses, target_responses):
        difference = actual-target
        occupation_error_upper = max(abs(difference.lo), abs(difference.hi))/2
        require(occupation_error_upper < F(1, 1000),
                'The exact interval comparison certifies occupation error below one thousandth on each of the seven words')
        error_bounds.append(upper_decimal(occupation_error_upper))
    require(max(error_bounds) < F(837, 10**6),
            'The outward displayed occupation-error upper bound is smaller than 837/1000000')
    return {'total_states': 3, 'readout_exact': [str(value) for value in readout],
            'zero_field_stationary_law_exact': [str(value) for value in law0],
            'high_field_stationary_law_exact': [str(value) for value in law_high],
            'stationary_flux_pair_order': [[0, 1], [0, 2], [1, 2]],
            'stationary_flux_numerators': [list(values) for values in flux_numerators],
            'stationary_flux_denominator': 10**6,
            'generators_exact': [[[str(value) for value in row] for row in q] for q in generators],
            'maximum_exit_rate_exact': '91862/30629',
            'exponential_certificates': exponential_certificates,
            'occupation_error_outward_upper_by_word_exact': [str(value) for value in error_bounds],
            'certified_uniform_occupation_error_upper': '1/1000',
            'scope': 'This one rational shared ordinary three-state model is certified on the same seven-word menu. It was proposed by a separate exploratory fit and then rounded; this verifier only checks its fixed exact rates and certified responses. No eleven-word, all-protocol or optimality upper claim is made.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/familiar_switch_margin.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    t, u, clock = F(4, 5), F(4, 5), F(2)
    polynomials = symbolic_checks(u)
    reversible_kernel_checks(polynomials, u)
    margin_report, target_responses = target_margin_checks(polynomials, t, u, clock)
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact stdlib Fraction sparse polynomials, rational matrix Taylor remainder bounds, outward dyadic intervals and full local polynomial-box bounds',
              'mean_word_order': [list(word) for word in WORDS],
              'field_alphabet': {'0': 'zero field', '1': 'H=log(3)'},
              'distinct_experiments': len(WORDS), 'maximum_ticks': max(map(len, WORDS)),
              'maximum_elapsed_time_exact': str(clock*max(map(len, WORDS))),
              'symbolic_identity': {'degree': 4, 'monomials_per_singleton_sign': 25,
                                    'division_by_response_determinant': False,
                                    'checks': 'Generic adjugate identity, Gram-product skew extraction, singleton moment elimination, independent scalar expression, positive reversible kernel fixtures and singular two-state cases'},
              'certified_target_margin': margin_report,
              'rational_ordinary_three_state_upper_witness': rational_reversible_upper_checks(target_responses, u, clock),
              'largest_dense_matrix_dimension': 4, 'numerical_optimization_used': False,
              'floating_arithmetic_used': False,
              'limitations': ['The necessary-identity proof supplies the universal link from ordinary reversible rivals to one of the two vanishing polynomials. The exact target/error-box and fixed-model exponential certificates are essential premises of the stated numerical lower and upper bounds.',
                              'The independent reversible stochastic-kernel fixtures are algebra tests; they are not asserted to be exponentials of continuous-time generators.',
                              'The explicit margin is sufficient and is not claimed to be optimal.',
                              'The comparison uses deterministic binary readout, stationary preparation and the shared Gibbs tilt; it concerns seven endpoint means, not complete path laws.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'proof_snapshot_sha256': {
                  name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                  for name in ('docs/FAMILIAR_SWITCH_FINITE_MARGIN.md',
                               'docs/FAMILIAR_SWITCH_STRUCTURE.md')
              },
              'imported_repository_verifiers': []}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
