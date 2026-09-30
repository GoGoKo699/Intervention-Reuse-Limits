#!/usr/bin/env python3
"""Five-word robust three-versus-four state certificate for two switches.

Physical parameters: tanh(J)=1/3, field tilts L=0 and H=7/9, clock=1.
The menu is L, LL, H, HH, HL. Every menu pair law may vary independently
within TV=1/20000; initial marginals remain common for any genuine rival.
No exact calibration is assumed in this certificate.

Only exact Fraction arithmetic and integer-square-root enclosures enter
verification. Floating-point values, if printed, are display summaries.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import platform

import verify_familiar_chain_accuracy as base

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_chain_cross_rank.json":
        "eee7e6a45c6ee1a823d59f4e0fc79e829090db07932b1c390df43d2e840078cf"
}
PROOFS = {'docs/FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md': '96670d6b5d111dc63627407f5835ab39594a62996079724ff499966d39547428'}
T = F(1, 3)
M = F(7, 9)
DELTA = F(1, 20_000)
WORDS = ((0,), (0, 0), (1,), (1, 1), (1, 0))
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def provenance():
    sources, proofs, reports = {}, {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT / name).read_bytes()
        check("input-hash:" + name, hashlib.sha256(payload).hexdigest() == expected)
        inherited = json.loads(payload)
        check("input-status:" + name, inherited["status"] == "PASS")
        reports[name] = expected
        for source, digest in inherited["source_sha256"].items():
            check("source-hash:" + source,
                  hashlib.sha256((ROOT / "scripts" / source).read_bytes()).hexdigest() == digest)
            sources[source] = digest
        for path, digest in inherited["proof_snapshot_sha256"].items():
            check("inherited-proof-hash:" + path,
                  hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
            proofs[path] = digest
        for path, digest in inherited.get("input_report_sha256", {}).items():
            check("inherited-report-hash:" + path,
                  hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
            reports[path] = digest
    check("inherited-proof-count", len(proofs) == 42)
    check("imported-helper-source-is-bound", Path(base.__file__).name in sources)
    for path, digest in PROOFS.items():
        check("new-proof-hash:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


def point(x):
    return F(x), F(x)


def interval_add(x, y):
    return x[0] + y[0], x[1] + y[1]


def interval_neg(x):
    return -x[1], -x[0]


def interval_sub(x, y):
    return interval_add(x, interval_neg(y))


def interval_mul(x, y):
    values = [a * b for a in x for b in y]
    return min(values), max(values)


def interval_div(x, y):
    check("interval-denominator-positive", y[0] > 0)
    return interval_mul(x, (1 / y[1], 1 / y[0]))


def interval_scale(x, coefficient):
    return interval_mul(x, point(coefficient))


def expand(x, radius):
    return x[0] - radius, x[1] + radius


def interval_square(x):
    lower = F(0) if x[0] <= 0 <= x[1] else min(x[0] ** 2, x[1] ** 2)
    return lower, max(x[0] ** 2, x[1] ** 2)


def interval_sqrt(x):
    check("square-root-nonnegative", 0 <= x[0] <= x[1])
    scale = 10 ** 20
    low_integer = isqrt(x[0].numerator * scale * scale // x[0].denominator)
    high_integer = isqrt(x[1].numerator * scale * scale // x[1].denominator) + 1
    lower, upper = F(low_integer, scale), F(high_integer, scale)
    check("square-root-lower-certificate", lower * lower <= x[0])
    check("square-root-upper-certificate", upper * upper >= x[1])
    return lower, upper


def display_enclosure(x):
    # Short, outward-rounded rational strings; decisions use original intervals.
    scale = 10 ** 12
    lower = F((x[0] * scale).__floor__(), scale)
    upper = F((x[1] * scale).__ceil__(), scale)
    check("outward-report-enclosure", lower <= x[0] <= x[1] <= upper)
    return [str(lower), str(upper)]


def mean_generator(m):
    # Column action Q(1,S,Z)=(1,S,Z)A, so controlled row products have
    # the same left-to-right word ordering as the stochastic kernels.
    a = m * (1 - T * T) / (1 - T * T * m * m)
    b = T * (1 - m * m) / (1 - T * T * m * m)
    return [[F(0), a, F(0)], [F(0), F(-1), T], [F(0), b, F(-1)]]


def target_moments():
    generators = [mean_generator(m) for m in (F(0), M)]
    check("same-Taylor-order-40", base.ORDER == 40)
    check("target-generator-norm-at-most-two",
          all(base.norm_inf(a) <= 2 for a in generators))
    exponentials = [base.exp_taylor(a) for a in generators]
    check("Taylor-factor-norm-below-nine", all(base.norm_inf(e) < 9 for e in exponentials))
    one_factor_error = F(8 * 2 ** 41, factorial(41))
    # exp(2)<8; two factors telescope with error <=2*9*one_factor_error.
    # Initial correlation row (0,1,T) has l1 norm below two.
    moment_error = 4 * 9 * one_factor_error
    check("moment-Taylor-error-below-1e-30", moment_error < F(1, 10 ** 30))
    moments = {}
    for word in WORDS:
        matrix = base.eye(3)
        for field in word:
            matrix = base.matmul(matrix, exponentials[field])
        mean = matrix[0][1]
        correlation = matrix[1][1] + T * matrix[2][1]
        moments[word] = (expand(point(mean), moment_error),
                         expand(point(correlation), moment_error))
    return moments, moment_error


def reversible_three_state_exclusion(moments):
    probability = (F(1, 2) - DELTA, F(1, 2) + DELTA)
    check("both-visible-sign-masses-positive", probability[0] > 0)
    z, variance = {}, {}
    for j, field in enumerate((F(0), M)):
        mean, correlation = moments[(j,)]
        # z_js=E[rho0 1_{S=s} K_j S]. Its test function has range [-1,1].
        z[j] = {sign: expand(interval_scale(interval_add(mean, interval_scale(correlation, sign)),
                                            F(1, 2)), 2 * DELTA)
                for sign in (-1, 1)}
        mean2, correlation2 = moments[(j, j)]
        value = expand(interval_add(correlation2, interval_scale(mean2, field)),
                       2 * (1 + field) * DELTA)
        for sign in (-1, 1):
            value = interval_sub(value, interval_scale(
                interval_div(interval_square(z[j][sign]), probability), 1 + field * sign))
        # Actual conditional variance is nonnegative. This intersection only
        # enlarges the information used from the observation intervals.
        check(f"field {j}:variance-upper-positive", value[1] > 0)
        variance[j] = max(F(0), value[0]), value[1]
    mean_part = point(0)
    for sign in (-1, 1):
        mean_part = interval_add(mean_part, interval_scale(
            interval_div(interval_mul(z[1][sign], z[0][sign]), probability), 1 + M * sign))
    switch_mean, switch_correlation = moments[(1, 0)]
    observed = expand(interval_add(switch_correlation, interval_scale(switch_mean, M)),
                      2 * (1 + M) * DELTA)
    branches = []
    minimum_gap = None
    for sector in (-1, 1):
        radical = interval_sqrt(interval_scale(interval_mul(variance[1], variance[0]),
                                               1 + sector * M))
        for orientation in (-1, 1):
            possible = interval_add(mean_part, interval_scale(radical, orientation))
            below_gap, above_gap = observed[0] - possible[1], possible[0] - observed[1]
            gap = max(below_gap, above_gap)
            check(f"sector {sector},orientation {orientation}:disjoint-switch-intervals", gap > 0)
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
            branches.append({"doubleton_sign": sector, "orientation": orientation,
                             "candidate_W_HL_interval": display_enclosure(possible),
                             "position": "below_target" if below_gap > 0 else "above_target",
                             "strict_interval_gap_lower": str(F((gap * 10 ** 12).__floor__(), 10 ** 12))})
    check("ordinary-three-state-exclusion-margin", minimum_gap > F(47, 100_000))
    print(f"Reversible <=3 excluded at TV={DELTA}; worst interval gap approximately {float(minimum_gap):.12f}")
    return {"status": "PASS", "ordinary_state_lower": 4,
            "target_W_HL_interval_with_TV_error": display_enclosure(observed),
            "conditional_mean_part_interval": display_enclosure(mean_part),
            "conditional_variance_intervals": {"L": display_enclosure(variance[0]),
                                                "H": display_enclosure(variance[1])},
            "branches": branches,
            "strict_minimum_interval_gap_lower": "47/100000",
            "identity": "W_HL=sum_s (1+m*s)*z_Hs*z_Ls/p_s + orientation*sqrt((1+doubleton_sign*m)*V_H*V_L)",
            "scope": "Every reversible rival with at most three persistent states, including imbalanced common preparations and zero-mass states. All five pair laws may have error; exact calibration is not assumed."}


def pair_probability(mean, correlation, initial_sign, final_sign):
    # Target initial sign balance is exact; rival marginals are varied separately.
    return interval_scale(interval_add(point(1), interval_add(
        interval_scale(mean, final_sign),
        interval_scale(correlation, initial_sign * final_sign))), F(1, 4))


def general_two_state_exclusion(moments):
    mean, correlation = moments[(0,)]
    probability = (F(1, 2) - DELTA, F(1, 2) + DELTA)
    observed_one = {(a, b): expand(pair_probability(mean, correlation, a, b), DELTA)
                    for a in (-1, 1) for b in (-1, 1)}
    check("single-tick-cell-bounds-positive", all(value[0] > 0 for value in observed_one.values()))
    predicted = point(0)
    for intermediate in (-1, 1):
        predicted = interval_add(predicted, interval_div(
            interval_mul(observed_one[(1, intermediate)], observed_one[(intermediate, 1)]),
            probability))
    mean2, correlation2 = moments[(0, 0)]
    observed_two = expand(pair_probability(mean2, correlation2, 1, 1), DELTA)
    gap = observed_two[0] - predicted[1]
    check("general-two-state-exclusion-margin", gap > F(328, 100_000))
    print(f"General <=2 excluded at TV={DELTA}; interval gap approximately {float(gap):.12f}")
    return {"status": "PASS", "general_state_lower": 3,
            "two_state_P_LL_plus_plus_interval": display_enclosure(predicted),
            "target_P_LL_plus_plus_interval_with_TV_error": display_enclosure(observed_two),
            "strict_interval_gap_lower": "328/100000",
            "identity": "P_LL(+,+)=sum_u P_L(+,u)*P_L(u,+)/p_u",
            "scope": "Any two-state time-homogeneous Markov rival with deterministic binary readout and common initial law; no reversibility or Gibbs constraint is used."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    moments, moment_error = target_moments()
    ordinary = reversible_three_state_exclusion(moments)
    general = general_two_state_exclusion(moments)
    target_summary = {"".join("L" if j == 0 else "H" for j in word):
                      {"mean": display_enclosure(mean), "correlation": display_enclosure(correlation)}
                      for word, (mean, correlation) in moments.items()}
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "dependencies": "Python standard library only; imported matrix helper is SHA256-bound",
        "arithmetic": "Exact rational Taylor enclosures, rational interval arithmetic, and integer square-root bounds; floating point only for display",
        "fixture": {"physical_switches": 2, "tanh_J": str(T), "field_tilts": ["0", str(M)],
                    "clock": "1", "words": ["L", "LL", "H", "HH", "HL"],
                    "maximum_TV_error_per_word": str(DELTA)},
        "target_moment_enclosures": target_summary,
        "Taylor_order": base.ORDER, "target_moment_error_upper": str(moment_error),
        "ordinary_three_state_exclusion": ordinary,
        "general_two_state_exclusion": general,
        "conclusion": "At maximum-menu TV error <=1/20000 on the five stated words, ordinary reversible rivals require at least four states, and general Markov rivals require at least three. Matching upper constructions are supplied in the companion equivalence note/report.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "The sufficient 50-ppm tolerance is conservative and is not the optimal distance, a sampling budget, or a device-feasibility claim. The analytic dimension identity in the written proof is essential; interval verification alone is not a universal proof. No exact calibration, rate ceiling, stationary-mass floor, stochastic readout, path-law equivalence, or thermodynamic benefit is assumed or established beyond the stated task.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact frozen-bound checks -> {args.output}")


if __name__ == "__main__":
    main()
