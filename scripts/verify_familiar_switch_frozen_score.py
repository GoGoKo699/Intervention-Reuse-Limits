#!/usr/bin/env python3
"""Exact five-word tangent-score sampling certificates.

All proof-bearing arithmetic is rational. The theorem assumes independent
reset trials; no Gaussian approximation or serial-device feasibility is used.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

import verify_familiar_switch_frozen_bound as target

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_frozen_bound.json"
INPUT_SHA256 = "3f807fcf2ed4e68f11831966399389475375bf13b3a801e96434e5fb9adfa625"
# Frozen proof snapshot.
PROOFS = {"docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md": "d8df8dd7b1ce248ff8bdbcd5d1d95f8ef371250c47a8eef4fc8f85f4184097b3"}
M = F(7, 9)
CENTER = tuple(map(F, (
    "0", "0.430143792060304", "0.198892575818085",
    "0.394017500089984", "0.161414604733478", "0.184195393007189",
)))
CENTER_ERROR = F(1, 10**12)
RADIUS = F(1, 625)
GATE = RADIUS / 2
ZERO_POWER = (0,) * 6
CHECKS = []


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
    """Sparse rational polynomial in six variables."""
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


def null_polynomials():
    variables = []
    for index in range(6):
        powers = [0] * 6
        powers[index] = 1
        variables.append(Polynomial({tuple(powers): F(1)}))
    e, x, y, z, v, r = variables
    g, w, q = 1 - e * e, 1 + M * e, e + M
    a = g * (y - e * e) - (x - e * e)**2
    b = g * (w * v - e * q) - (w * z - e * q)**2
    c = g * (r - e * e) - (x - e * e) * (z - e * e)
    return {sign: (1 - sign * M) * w * c * c - a * b for sign in (1, -1)}


def target_center_certificate():
    moments, error = target.target_moments()
    actual = [(F(0), F(0))] + [moments[word][1] for word in target.WORDS]
    check("target-moment-order", target.WORDS == ((0,), (0, 0), (1,), (1, 1), (1, 0)))
    for index, (center, (lower, upper)) in enumerate(zip(CENTER, actual)):
        check(f"center-enclosure-{index}",
              center - CENTER_ERROR <= lower <= upper <= center + CENTER_ERROR)
    return {"status": "PASS", "center": list(map(str, CENTER)),
            "coordinate_order": ["initial_mean", "C_L", "C_LL", "C_H", "C_HH", "C_HL"],
            "coordinate_error_upper": str(CENTER_ERROR),
            "inherited_target_Taylor_error_upper": str(error)}


def score_certificates():
    polynomials = null_polynomials()
    box = [(value - RADIUS, value + RADIUS) for value in CENTER]
    parameters = {
        1: {"direction": -1, "H": F(10), "V": F(41, 100000),
            "b": F(3, 100), "delta": F(374, 10**7)},
        -1: {"direction": 1, "H": F(20), "V": F(351, 100000),
             "b": F(107, 1000), "delta": F(2992, 10**7)},
    }
    scenarios = (
        (20_000_000, F(0), F(1)),
        (25_000_000, F(1, 100000), F(1)),
        (30_000_000, F(1, 100000), F(49, 50)),
    )
    summaries, rational_risks = {}, {}
    for sign, polynomial in polynomials.items():
        params = parameters[sign]
        value = polynomial.evaluate(CENTER)
        gradient = [polynomial.derivative(j).evaluate(CENTER) for j in range(6)]
        hessian_sum = F(0)
        for i in range(6):
            for j in range(6):
                interval = polynomial.derivative(i).derivative(j).interval(box)
                hessian_sum += max(abs(interval[0]), abs(interval[1]))
        check(f"sector-{sign}:Hessian-bound", hessian_sum < params["H"])
        check(f"sector-{sign}:target-score-sign",
              params["direction"] * value > params["delta"])
        variance = sum((abs(x) + abs(gradient[0]) / 5)**2 for x in gradient[1:])
        increment = 2 * max(abs(x) + abs(gradient[0]) / 5 for x in gradient[1:])
        check(f"sector-{sign}:global-variance", variance < params["V"])
        check(f"sector-{sign}:global-increment", increment < params["b"])
        gradient_l1 = sum(map(abs, gradient))
        remainder = params["H"] * RADIUS**2 / 2
        threshold = params["direction"] * (params["delta"] + remainder) / 2
        nominal_margin = (params["delta"] - remainder) / 2
        check(f"sector-{sign}:positive-margin", nominal_margin > 0)
        rows = []
        rational_risks[sign] = []
        for trials, tv_bias, contrast in scenarios:
            channel_l1 = abs(gradient[0]) / contrast + sum(
                abs(x) / contrast**2 for x in gradient[1:])
            channel_variance = sum((abs(x) / contrast**2
                                    + abs(gradient[0]) / (5 * contrast))**2
                                   for x in gradient[1:])
            channel_increment = 2 * max(abs(x) / contrast**2
                                        + abs(gradient[0]) / (5 * contrast)
                                        for x in gradient[1:])
            variance_cap = params["V"] if contrast == 1 else (
                F(1, 2200) if sign == 1 else F(1, 250))
            increment_cap = params["b"] if contrast == 1 else (
                F(4, 125) if sign == 1 else F(3, 25))
            check(f"sector-{sign},N-{trials}:channel-variance",
                  channel_variance < variance_cap)
            check(f"sector-{sign},N-{trials}:channel-increment",
                  channel_increment < increment_cap)
            mean_bias = 2 * tv_bias * channel_l1 + CENTER_ERROR * gradient_l1
            margin = nominal_margin - mean_bias
            check(f"sector-{sign},N-{trials}:biased-margin-positive", margin > 0)
            exponent = trials * margin**2 / (2 * (variance_cap + increment_cap * margin / 3))
            score_tail = exp_negative_upper(exponent)
            gate_distance = GATE - 2 * tv_bias / contrast**2 - CENTER_ERROR
            check(f"sector-{sign},N-{trials}:gate-distance-positive", gate_distance > 0)
            correlation_exponent = trials * gate_distance**2 * contrast**4 / 2
            initial_exponent = 5 * trials * gate_distance**2 * contrast**2 / 2
            correlation_tail = exp_negative_upper(correlation_exponent)
            initial_tail = exp_negative_upper(initial_exponent)
            target_gate = 10 * correlation_tail + 2 * initial_tail
            null_gate = 2 * correlation_tail
            rational_risks[sign].append((score_tail, target_gate, null_gate))
            rows.append({
                "trials_per_word": trials, "recorded_law_TV_budget": str(tv_bias),
                "known_channel_contrast": str(contrast),
                "variance_cap": str(variance_cap), "centered_increment_cap": str(increment_cap),
                "systematic_score_bias_upper": str(rounded_upper(mean_bias)),
                "effective_margin_lower": str(rounded_lower(margin)),
                "Bernstein_exponent_lower": str(rounded_lower(exponent)),
                "one_sided_score_tail_upper": str(rounded_upper(score_tail)),
                "target_gate_failure_upper": str(rounded_upper(target_gate)),
                "outside_null_gate_pass_upper": str(rounded_upper(null_gate)),
            })
        summaries[str(sign)] = {
            "target_score_exact": str(value), "gradient_exact": list(map(str, gradient)),
            "Hessian_absolute_sum_upper": str(rounded_upper(hessian_sum)),
            "Hessian_cap": str(params["H"]), "Taylor_remainder_cap": str(remainder),
            "target_absolute_score_lower": str(params["delta"]),
            "gradient_L1_upper": str(rounded_upper(gradient_l1)),
            "rejection_threshold_exact": str(threshold),
            "rejection_direction": "below" if sign == 1 else "above",
            "scenarios": rows,
        }
    risks = []
    for index, (trials, tv_bias, contrast) in enumerate(scenarios):
        branches = [rational_risks[sign][index] for sign in (1, -1)]
        check(f"N-{trials}:gate-bound-common", branches[0][1:] == branches[1][1:])
        beta = branches[0][1] + sum(row[0] for row in branches)
        # Inside and outside null cases are disjoint; summing is conservative.
        alpha = max(row[0] for row in branches) + max(row[2] for row in branches)
        check(f"N-{trials}:exact-type-I-below-five-percent", alpha < F(1, 20))
        check(f"N-{trials}:exact-type-II-below-five-percent", beta < F(1, 20))
        risks.append({"trials_per_word": trials, "total_reset_trials": 5 * trials,
                      "recorded_law_TV_budget": str(tv_bias),
                      "known_endpoint_flip_probability": str((1 - contrast) / 2),
                      "type_I_upper": str(rounded_upper(alpha)),
                      "type_II_upper": str(rounded_upper(beta)),
                      "status": "PASS"})
    return summaries, risks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    center = target_center_certificate()
    scores, risks = score_certificates()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "arithmetic": "Exact Fraction polynomials, derivatives, interval Hessians, matrix Taylor target enclosures and exponential tail certificates; final probability assertions are rational",
        "target_center": center,
        "test": {"words": ["L", "LL", "H", "HH", "HL"],
                 "field_tilts": ["0", str(M)], "coupling": "1/3", "clock": "1",
                 "population_box_radius": str(RADIUS), "empirical_gate_radius": str(GATE),
                 "score_definition": "W_s=F_s(center)+gradient(F_s)(center) dot (empirical-center)",
                 "null_polynomial": "F_s=(1-s*m)*(1+m*e)*C^2-A*B; A=(1-e^2)*(y-e^2)-(x-e^2)^2; B=(1-e^2)*((1+m*e)*v-e*(e+m))-((1+m*e)*z-e*(e+m))^2; C=(1-e^2)*(r-e^2)-(x-e^2)*(z-e^2)",
                 "rejection_rule": "All six moment gates pass AND W_+ < -251/10000000 AND W_- > 203/1250000",
                 "corrected_lookup": "Y=initial_recorded_sign/contrast; X=product_of_recorded_signs/contrast^2",
                 "initial_mean_estimator": "Pooled over all 5N corrected initial signs; correlations estimated within their N-trial word groups"},
        "score_certificates": scores, "sampling_certificates": risks,
        "sampling_assumptions": "Independent reset trials within and across five word groups. Each actual recorded law is fixed within its group and TV-close to the known tensor endpoint-flip channel applied to one fixed nominal reference family. Under the null that reference is one ordinary reversible <=3-state model with common preparation, deterministic binary readout and prescribed Gibbs tilt; under the alternative it is the stated physical target.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "Sufficient budgets, not sample-complexity optimality or a laboratory throughput claim. No exact calibration is assumed for the null. No serial independence, reset protocol, detector calibration precision, full-path equivalence or device feasibility follows. The written null identity and concentration proof are essential; numerical constants alone are not the statistical theorem.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact frozen-score checks -> {args.output}")


if __name__ == "__main__":
    main()
