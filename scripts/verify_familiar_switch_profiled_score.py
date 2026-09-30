#!/usr/bin/env python3
"""Exact 50-million-trial certificate for the unknown-tilt five-word test.

This verifier uses only rational arithmetic. The sampling theorem is for
independent reset trials, with one common preparation under the null.
The local covariance envelope applies uniformly to the null family; no
plug-in variance estimate or Gaussian approximation enters the proof.
"""
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb, factorial
from pathlib import Path
import platform

import verify_familiar_switch_frozen_bound as target

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_frozen_score.json"
INPUT_SHA256 = "2a9b81dec97139d06bb6890319701bdaff9ea07144520fc27dda040352b9860a"
PROOFS = {
    "docs/FAMILIAR_SWITCH_PROFILED_ACQUISITION.md":
        "351b33f58bc3738d44ee418cfa0fb309d1b335f4f964e9ca807e97b2e6dbb184",
}
N = 10_000_000
RADIUS = F(11, 5000)
GATE = F(13, 10000)
CENTER_ERROR = F(1, 10**12)
THRESHOLD = -F(1, 80000)
TARGET_SIGNAL = F(22667, 10**9)
NULL_VARIANCE = F(9, 50000)
TARGET_VARIANCE = F(17, 200000)
INCREMENT = F(1, 20)
REMAINDER_COST = F(65, 4)
QUADRATIC_EXPONENT = F(5)
ZERO_POWER = (0,) * 7
CHECKS = []
CENTER = tuple(map(F, ['0', '1075359480150759/2500000000000000', '19889257581808503/100000000000000000', '39401750008998393/100000000000000000', '3228292094669557/20000000000000000', '9209769650359431/50000000000000000', '4713197221522347/10000000000000000']))
CONTROL_VARIATES = tuple(map(F, ['-1020953/2000000000', '-1020953/2000000000', '-26817373/10000000000', '24855453/5000000000', '-12684003/10000000000']))
Q0 = tuple(tuple(map(F, row)) for row in [['34634049/500000000', '-8511/5000000', '-2828307/125000000', '61050617/500000000', '-47523863/250000000', '50805259/1000000000', '-2420723/250000000'], ['-8511/5000000', '222448921/500000000', '-493678777/1000000000', '2282863/500000000', '945261/40000000', '-4501291/125000000', '3570037/1000000000'], ['-2828307/125000000', '-493678777/1000000000', '154024593/250000000', '157057/6250000', '7630797/500000000', '-87660961/1000000000', '9352113/1000000000'], ['61050617/500000000', '2282863/500000000', '157057/6250000', '102870913/250000000', '-448712073/1000000000', '-79815201/1000000000', '6517681/1000000000'], ['-47523863/250000000', '945261/40000000', '7630797/500000000', '-448712073/1000000000', '125382349/200000000', '-22237137/250000000', '7238911/1000000000'], ['50805259/1000000000', '-4501291/125000000', '-87660961/1000000000', '-79815201/1000000000', '-22237137/250000000', '282445849/1000000000', '-28201741/1000000000'], ['-2420723/250000000', '3570037/1000000000', '9352113/1000000000', '6517681/1000000000', '7238911/1000000000', '-28201741/1000000000', '2552813/250000000']])
PROXY = (F(6, 5), F(6, 5), F(6, 5), F(2), F(6, 5), F(6, 5), F(2))

def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def provenance():
    payload = (ROOT / INPUT).read_bytes()
    check("input-report-hash", hashlib.sha256(payload).hexdigest() == INPUT_SHA256)
    inherited = json.loads(payload)
    check("input-report-pass", inherited["status"] == "PASS")
    sources = dict(inherited["source_sha256"])
    proofs = dict(inherited["proof_snapshot_sha256"])
    reports = dict(inherited.get("input_report_sha256", {}))
    reports[INPUT] = INPUT_SHA256
    for path, digest in sources.items():
        check("inherited-source:" + path,
              hashlib.sha256((ROOT / "scripts" / path).read_bytes()).hexdigest() == digest)
    for path, digest in {**proofs, **reports}.items():
        check("inherited-file:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
    check("imported-target-helper-bound", Path(target.__file__).name in sources)
    for path, digest in PROOFS.items():
        check("new-proof:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


def product(values):
    answer = F(1)
    for value in values:
        answer *= value
    return answer


def interval_add(x, y):
    return x[0] + y[0], x[1] + y[1]


def interval_multiply(x, y):
    values = [a * b for a in x for b in y]
    return min(values), max(values)


class Polynomial:
    """Sparse rational polynomial in seven variables."""
    def __init__(self, value=0):
        self.terms = value if isinstance(value, dict) else {ZERO_POWER: F(value)}

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        result = dict(self.terms)
        for powers, coefficient in other.terms.items():
            result[powers] = result.get(powers, F(0)) + coefficient
        return Polynomial({k: v for k, v in result.items() if v})

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        return self + (-other)

    def __rsub__(self, other):
        return Polynomial(other) + (-self)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        result = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                powers = tuple(x + y for x, y in zip(left, right))
                result[powers] = result.get(powers, F(0)) + a * b
        return Polynomial({k: v for k, v in result.items() if v})

    __rmul__ = __mul__

    def __pow__(self, power):
        answer = Polynomial(1)
        for _ in range(power):
            answer *= self
        return answer

    def derivative(self, variable):
        result = {}
        for powers, coefficient in self.terms.items():
            if powers[variable]:
                new_powers = list(powers)
                new_powers[variable] -= 1
                result[tuple(new_powers)] = powers[variable] * coefficient
        return Polynomial(result)

    def evaluate(self, point):
        return sum((coefficient * product(x**p for x, p in zip(point, powers))
                    for powers, coefficient in self.terms.items()), F(0))

    def interval(self, box):
        answer = F(0), F(0)
        for powers, coefficient in self.terms.items():
            term = coefficient, coefficient
            for (lower, upper), power in zip(box, powers):
                if power == 0:
                    factor = F(1), F(1)
                elif power % 2:
                    factor = lower**power, upper**power
                else:
                    factor = (F(0) if lower <= 0 <= upper
                              else min(lower**power, upper**power),
                              max(lower**power, upper**power))
                term = interval_multiply(term, factor)
            answer = interval_add(answer, term)
        return answer


def exponential_interval(x, degree=120):
    check("exponential-argument-nonnegative", x >= 0)
    lower = sum((x**k / factorial(k) for k in range(degree + 1)), F(0))
    first_omitted = x**(degree + 1) / factorial(degree + 1)
    ratio = x / (degree + 2)
    check("exponential-tail-ratio-below-one", ratio < 1)
    return lower, lower + first_omitted / (1 - ratio)


def exp_negative_upper(x):
    lower, _ = exponential_interval(x)
    return 1 / lower


def rounded_upper(x, denominator=10**12):
    return F((x * denominator).__ceil__(), denominator)


def rounded_lower(x, denominator=10**12):
    return F((x * denominator).__floor__(), denominator)


def variables():
    result = []
    for index in range(7):
        powers = [0] * 7
        powers[index] = 1
        result.append(Polynomial({tuple(powers): F(1)}))
    return result


def divide_by_initial_factor(polynomial, sign):
    """Exact division by 1+sign*e, with a checked zero remainder."""
    groups = {}
    for powers, coefficient in polynomial.terms.items():
        groups.setdefault(powers[1:], {})[powers[0]] = coefficient
    result = {}
    for other_powers, coefficients in groups.items():
        degree, previous = max(coefficients), F(0)
        for power in range(degree):
            value = coefficients.get(power, F(0)) - sign * previous
            if value:
                result[(power,) + other_powers] = value
            previous = value
        check(f"sector-{sign}:exact-polynomial-division-{other_powers}",
              coefficients.get(degree, F(0)) == sign * previous)
    return Polynomial(result)


def null_polynomials():
    e, x, y, z, v, r, h = variables()
    d, g = 1 - z, 1 - e * e
    a = g * (y - e * e) - (x - e * e)**2
    c = g * (r - e * e) - (x - e * e) * (z - e * e)
    dd = g * (v - z) + d * (z - e * h)
    result = {}
    for sign in (1, -1):
        numerator = (d - sign * (h - e)) * c * c - d * a * dd
        quotient = divide_by_initial_factor(numerator, sign)
        check(f"sector-{sign}:degree-six", max(map(sum, quotient.terms)) == 6)
        check(f"sector-{sign}:factorization",
              not (quotient * (1 + sign * e) - numerator).terms)
        result[sign] = quotient
    return result


def shifted(polynomial, center):
    """Translate exactly before interval evaluation to preserve cancellations."""
    terms = dict(polynomial.terms)
    for index, center_value in enumerate(center):
        if not center_value:
            continue
        result = {}
        for powers, coefficient in terms.items():
            for power in range(powers[index] + 1):
                new_powers = list(powers)
                new_powers[index] = power
                key = tuple(new_powers)
                result[key] = result.get(key, F(0)) + (
                    coefficient * comb(powers[index], power)
                    * center_value**(powers[index] - power))
        terms = {powers: coefficient for powers, coefficient in result.items()
                 if coefficient}
    return Polynomial(terms)


def target_center_certificate():
    moments, error = target.target_moments()
    check("target-moment-order", target.WORDS == ((0,), (0, 0), (1,), (1, 1), (1, 0)))
    actual = ([(F(0), F(0))] + [moments[word][1] for word in target.WORDS]
              + [moments[(1,)][0]])
    for index, (center, (lower, upper)) in enumerate(zip(CENTER, actual)):
        check(f"center-enclosure-{index}",
              center - CENTER_ERROR <= lower <= upper <= center + CENTER_ERROR)
    check("common-initial-control-variates-sum-zero", sum(CONTROL_VARIATES) == 0)
    check("initial-factor-positive-on-local-box", abs(CENTER[0]) + RADIUS < 1)
    check("profile-denominator-positive-on-local-box", 1 - CENTER[3] - RADIUS > 0)
    return {"status": "PASS", "center": list(map(str, CENTER)),
            "coordinate_order": ["initial_mean", "C_L", "C_LL", "C_H", "C_HH", "C_HL", "M_H"],
            "coordinate_error_upper": str(CENTER_ERROR),
            "inherited_target_Taylor_error_upper": str(error)}


def variance_numerator(shifted_plus):
    """Build d^2 times the sum of the five complete paired-score variances.

    For Z=a*S0+b*S0*ST+c*ST, retain all within-pair covariances.
    The five final means follow from common Gibbs stationarity, with the
    unknown tilt profiled as (h-e)/(1-z). The resulting expression is a
    polynomial, so a single centered interval retains exact cancellations.
    """
    derivatives = [shifted_plus.derivative(index) for index in range(7)]
    theta = [variable + value for variable, value in zip(variables(), CENTER)]
    e, x, y, z, v, r, h = theta
    d = 1 - z
    mean_numerators = [e * d, e * d, h * d,
                       e * d + (h - e) * (1 - v),
                       e * d + (h - e) * (x - r)]
    result = Polynomial(0)
    for arm in range(5):
        a = derivatives[0] * F(1, 5) + CONTROL_VARIATES[arm]
        b = derivatives[arm + 1]
        c = derivatives[6] if arm == 2 else Polynomial(0)
        correlation, mean_numerator = theta[arm + 1], mean_numerators[arm]
        result += (
            d * d * (a * a + b * b + c * c
                     + 2 * a * c * correlation + 2 * b * c * e)
            + 2 * a * b * mean_numerator * d
            - (d * (a * e + b * correlation) + c * mean_numerator)**2)
    return result


def variance_and_branch_certificates(polynomials):
    shifted_plus = shifted(polynomials[1], CENTER)
    shifted_minus = shifted(polynomials[-1], CENTER)
    box = [(-RADIUS, RADIUS)] * 7
    target_box = [(-CENTER_ERROR, CENTER_ERROR)] * 7
    minus_interval = shifted_minus.interval(box)
    check("minus-branch-excluded-throughout-population-box",
          minus_interval[0] > F(24, 10**6))
    plus_target = shifted_plus.interval(target_box)
    check("target-plus-score-negative-with-certified-margin",
          plus_target[1] < -TARGET_SIGNAL)
    numerator = variance_numerator(shifted_plus)
    local_variance = numerator.interval(box)[1] / (1 - CENTER[3] - RADIUS)**2
    nominal_variance = numerator.interval(target_box)[1] / (
        1 - CENTER[3] - CENTER_ERROR)**2
    check("uniform-null-local-variance-cap", local_variance < NULL_VARIANCE)
    check("nominal-target-variance-cap", nominal_variance < TARGET_VARIANCE)
    ranges = []
    for arm in range(5):
        coefficients = [
            (shifted_plus.derivative(0) * F(1, 5) + CONTROL_VARIATES[arm]).interval(box),
            shifted_plus.derivative(arm + 1).interval(box),
            shifted_plus.derivative(6).interval(box) if arm == 2 else (F(0), F(0)),
        ]
        range_upper = F(0)
        # The outcome range is convex in these three coefficients, so its
        # maximum on their interval box occurs at a coefficient-box vertex.
        for a, b, c in itertools.product(*coefficients):
            values = [a * initial + b * initial * final + c * final
                      for initial, final in itertools.product((-1, 1), repeat=2)]
            range_upper = max(range_upper, max(values) - min(values))
        check(f"arm-{arm}:centered-increment-cap", range_upper < INCREMENT)
        ranges.append(range_upper)
    summary = {
        "minus_score_lower_over_full_population_box": str(rounded_lower(minus_interval[0])),
        "minus_score_positive_cap": str(F(24, 10**6)),
        "target_plus_score_upper": str(rounded_upper(plus_target[1])),
        "target_absolute_score_lower": str(TARGET_SIGNAL),
        "common_initial_control_variates": list(map(str, CONTROL_VARIATES)),
        "variance_numerator_term_count": len(numerator.terms),
        "uniform_null_variance_upper": str(rounded_upper(local_variance)),
        "uniform_null_variance_cap": str(NULL_VARIANCE),
        "target_variance_upper": str(rounded_upper(nominal_variance)),
        "target_variance_cap": str(TARGET_VARIANCE),
        "arm_centered_increment_upper": [str(rounded_upper(value)) for value in ranges],
        "common_centered_increment_cap": str(INCREMENT),
    }
    return shifted_plus, summary


def positive_definite(matrix, label):
    """Exact symmetric LDL elimination; all pivots must be positive."""
    size = len(matrix)
    check(label + ":symmetric", all(matrix[i][j] == matrix[j][i]
                                    for i in range(size) for j in range(size)))
    work = [list(row) for row in matrix]
    pivots = []
    for index in range(size):
        pivot = work[index][index]
        check(f"{label}:positive-pivot-{index}", pivot > 0)
        pivots.append(pivot)
        for row in range(index + 1, size):
            for column in range(row, size):
                work[row][column] -= work[row][index] * work[column][index] / pivot
                work[column][row] = work[row][column]
    return min(pivots)


def quadratic_certificate(shifted_plus):
    box = [(-RADIUS, RADIUS)] * 7
    zero = (F(0),) * 7
    hessian_polynomials = [[shifted_plus.derivative(i).derivative(j)
                           for j in range(7)] for i in range(7)]
    hessian_center = [[entry.evaluate(zero) for entry in row]
                      for row in hessian_polynomials]
    check("Q0-exact-symmetry", all(Q0[i][j] == Q0[j][i]
                                  for i in range(7) for j in range(7)))
    check("Hessian-exact-symmetry", all(hessian_polynomials[i][j].terms
                                      == hessian_polynomials[j][i].terms
                                      for i in range(7) for j in range(7)))
    pivot_lowers = {}
    for sign in (-1, 1):
        pivot_lowers[str(sign)] = positive_definite(
            [[Q0[i][j] + sign * hessian_center[i][j] for j in range(7)]
             for i in range(7)], f"Q0-plus-{sign}-Hcenter")
    deviations = []
    for i in range(7):
        row = []
        for j in range(7):
            lower, upper = hessian_polynomials[i][j].interval(box)
            row.append(max(abs(lower - hessian_center[i][j]),
                           abs(upper - hessian_center[i][j])))
        deviations.append(row)
    check("Hessian-deviation-exact-symmetry", all(deviations[i][j] == deviations[j][i]
                                                for i in range(7) for j in range(7)))
    # Row-sum diagonal padding dominates both signs of every symmetric
    # Hessian perturbation whose entries obey the interval deviations.
    q = [[Q0[i][j] + (sum(deviations[i]) if i == j else 0)
          for j in range(7)] for i in range(7)]
    trace = sum(PROXY[i] * q[i][i] for i in range(7))
    trace_square = sum(PROXY[i] * PROXY[j] * q[i][j]**2
                       for i in range(7) for j in range(7))
    trace_cap, trace_square_cap, spectral_cap = F(9, 2), F(11, 2), F(7, 4)
    check("quadratic-trace-cap", trace < trace_cap)
    check("quadratic-trace-square-cap", trace_square < trace_square_cap)
    positive_definite([[(spectral_cap / PROXY[i] if i == j else 0) - q[i][j]
                       for j in range(7)] for i in range(7)], "quadratic-spectral-cap")
    square_root_cap = F(21, 4)
    check("quadratic-square-root-cap",
          QUADRATIC_EXPONENT * trace_square_cap < square_root_cap**2)
    cost = (trace_cap + 2 * square_root_cap
            + 2 * spectral_cap * QUADRATIC_EXPONENT) / 2
    check("quadratic-remainder-cost-cap", cost == F(65, 4) == REMAINDER_COST)
    # Proxy validity: per-arm diagonal weights are (6,6/5) off H and
    # (6,2,2) on H. Every pair of reciprocal weights sums to at most one.
    check("non-H-pair-proxy", F(1, 6) + F(5, 6) <= 1)
    check("H-pair-proxy-initial-final", F(1, 6) + F(1, 2) <= 1)
    check("H-pair-proxy-correlation-final", F(1, 2) + F(1, 2) <= 1)
    return {
        "Q0_exact": [[str(value) for value in row] for row in Q0],
        "Hessian_deviation_row_sum_upper": [str(rounded_upper(sum(row))) for row in deviations],
        "Q0_signed_Hessian_minimum_LDL_pivot_lower": {
            sign: str(rounded_lower(value)) for sign, value in pivot_lowers.items()},
        "subGaussian_proxy_diagonal_before_dividing_by_N": list(map(str, PROXY)),
        "weighted_trace_upper": str(rounded_upper(trace)), "weighted_trace_cap": str(trace_cap),
        "weighted_trace_square_upper": str(rounded_upper(trace_square)),
        "weighted_trace_square_cap": str(trace_square_cap),
        "weighted_spectral_norm_cap": str(spectral_cap),
        "quadratic_tail_exponent": str(QUADRATIC_EXPONENT),
        "derived_remainder_cost_upper": str(cost),
        "used_remainder_cost_upper": str(REMAINDER_COST),
        "remainder_upper": str(REMAINDER_COST / N),
        "remainder_event_scope": "For a population vector in the outer box, probability(empirical gate passes AND absolute Taylor remainder>65/(4N))<=exp(-5); no global Hessian bound outside the box is asserted",
    }


def probability_certificate():
    remainder = REMAINDER_COST / N
    null_margin = -THRESHOLD - remainder
    target_margin = TARGET_SIGNAL + THRESHOLD - remainder
    check("null-linear-margin-positive", null_margin > 0)
    check("target-linear-margin-positive", target_margin > 0)
    null_exponent = N * null_margin**2 / (2 * (NULL_VARIANCE + INCREMENT * null_margin / 3))
    target_exponent = N * target_margin**2 / (2 * (TARGET_VARIANCE + INCREMENT * target_margin / 3))
    null_linear, target_linear = map(exp_negative_upper, (null_exponent, target_exponent))
    quadratic = exp_negative_upper(QUADRATIC_EXPONENT)
    outside_distance = RADIUS - GATE
    target_distance = GATE - CENTER_ERROR
    check("gate-distances-positive", outside_distance > 0 and target_distance > 0)
    outside_null = 2 * exp_negative_upper(N * outside_distance**2 / 2)
    target_gate = (12 * exp_negative_upper(N * target_distance**2 / 2)
                   + 2 * exp_negative_upper(5 * N * target_distance**2 / 2))
    # On the empirical gate and with true theta in the population box,
    # the connecting segment is in that box. Only this event needs the
    # local Hessian majorant and its Taylor-remainder tail certificate.
    inside_null = null_linear + quadratic
    # A fixed null population lies either inside or outside the box.
    alpha = max(inside_null, outside_null)
    beta = target_linear + quadratic + target_gate
    check("exact-type-I-below-five-percent", alpha < F(1, 20))
    check("exact-type-II-below-five-percent", beta < F(1, 20))
    check("reported-type-I-cap", alpha < F(44297, 10**6))
    check("reported-type-II-cap", beta < F(23080, 10**6))
    return {
        "trials_per_word": N, "total_reset_trials": 5 * N,
        "target_absolute_score_lower": str(TARGET_SIGNAL),
        "rejection_threshold": str(THRESHOLD),
        "null_linear_margin": str(null_margin), "target_linear_margin": str(target_margin),
        "null_Bernstein_exponent_lower": str(rounded_lower(null_exponent)),
        "target_Bernstein_exponent_lower": str(rounded_lower(target_exponent)),
        "null_linear_tail_upper": str(rounded_upper(null_linear)),
        "target_linear_tail_upper": str(rounded_upper(target_linear)),
        "quadratic_remainder_tail_upper": str(rounded_upper(quadratic)),
        "inside_null_rejection_upper": str(rounded_upper(inside_null)),
        "outside_null_gate_pass_upper": str(rounded_upper(outside_null)),
        "target_gate_failure_upper": str(rounded_upper(target_gate)),
        "type_I_upper": str(rounded_upper(alpha)), "type_II_upper": str(rounded_upper(beta)),
        "status": "PASS",
    }


def evaluate_test(initial_sums, correlation_sums, final_high_sum):
    """The fixed test on integer sufficient statistics from N trials/word.

    Word order is L,LL,H,HH,HL. Return True exactly on rejection of the
    ordinary reversible at-most-three-state null. This is not a data loader.
    """
    if len(initial_sums) != 5 or len(correlation_sums) != 5:
        raise ValueError("Exactly five initial and five correlation sums are required")
    entries = list(initial_sums) + list(correlation_sums) + [final_high_sum]
    if any(type(value) is not int or abs(value) > N or (value + N) % 2 for value in entries):
        raise ValueError("Each sum must be a feasible sum of N binary signs")
    initial_means = [F(value, N) for value in initial_sums]
    point = [sum(initial_means) / 5] + [F(value, N) for value in correlation_sums]
    point.append(F(final_high_sum, N))
    if any(abs(value - center) > GATE for value, center in zip(point, CENTER)):
        return False
    score = null_polynomials()[1].evaluate(point) + sum(
        coefficient * mean for coefficient, mean in zip(CONTROL_VARIATES, initial_means))
    return score < THRESHOLD


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    center = target_center_certificate()
    polynomials = null_polynomials()
    shifted_plus, covariance = variance_and_branch_certificates(polynomials)
    quadratic = quadratic_certificate(shifted_plus)
    risks = probability_certificate()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()}, "dependencies": "Python standard library only",
        "arithmetic": "Exact Fraction sparse polynomials, exact center translation and interval bounds, symmetric rational LDL positivity, matrix-Taylor target enclosures, and rational exponential-tail comparisons. No floating-point proof decisions.",
        "target_center": center,
        "test": {
            "words": ["L", "LL", "H", "HH", "HL"], "target_field_tilts": ["0", "7/9"],
            "target_coupling": "1/3", "target_clock": "1", "null_high_tilt": "unknown",
            "population_box_radius": str(RADIUS), "empirical_gate_radius": str(GATE),
            "coordinate_order": ["e", "x=C_L", "y=C_LL", "z=C_H", "v=C_HH", "r=C_HL", "h=M_H"],
            "null_polynomial": "P_s=([d-s*(h-e)]*C^2-d*A*D)/(1+s*e), an exact degree-six polynomial; d=1-z; g=1-e^2; A=g*(y-e^2)-(x-e^2)^2; C=g*(r-e^2)-(x-e^2)*(z-e^2); D=g*(v-z)+d*(z-e*h)",
            "score_definition": "P_+(empirical seven-moment vector)+sum_j control_variate_j*empirical_initial_mean_j",
            "rejection_rule": "All seven coordinate gates of radius13/10000 about the fixed center pass AND score< -1/80000; otherwise do not reject",
            "initial_mean_estimator": "Mean of all 5N initial signs; all five correlation means and the H final-sign mean use their N-trial arm",
            "independent_reset_trials_per_word": N, "total_independent_reset_trials": 5 * N,
        },
        "local_covariance_certificate": covariance, "quadratic_remainder_certificate": quadratic,
        "sampling_certificate": risks,
        "sampling_assumptions": "Independent trials within and across the five fixed word groups. Under the null, their paired laws come from one ordinary reversible model with at most three states, one common preparation, deterministic binary readout, coherent reused tick kernels and Gibbs weights rho_H=rho_0*(1+m*S) for an unknown admissible m. The null is not assumed exactly calibrated to any target moments. Nominal power is for the stated four-state physical target with its exact reset preparation.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
        "limitations": "A sufficient independent-reset sampling budget for this fixed test, not an optimality, laboratory throughput, finite-reset equilibration, serial sampling, detector-noise, physical calibration robustness or full-path-equivalence claim. The written null-identity and concentration proofs are required in addition to these exact constant checks.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact profiled-score checks -> {args.output}")


if __name__ == "__main__":
    main()
