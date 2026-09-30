#!/usr/bin/env python3
"""Exact confidence-set sampling certificate for the five-word switch test.

The primary test profiles an unknown high-field Gibbs tilt from observations.
It uses 120,000,000 independent reset trials per word (600,000,000 total).
A fixed-tilt alternative uses 115,000,000 per word (575,000,000 total).
Both have type-I error and nominal-target type-II error below 1/20.
These are conservative sufficient budgets, not sample-complexity lower bounds.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import verify_familiar_switch_frozen_bound as bound

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_switch_frozen_bound.json":
        "9b15c6c9eacf0e19d53e8413442cc8d568aa8e3411eadc552d0547fc01c0d5a8"
}
# Frozen proof snapshot.
PROOFS = {"docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md": "d8df8dd7b1ce248ff8bdbcd5d1d95f8ef371250c47a8eef4fc8f85f4184097b3"}
WORDS = ("L", "LL", "H", "HH", "HL")
WORD_IDS = ((0,), (0, 0), (1,), (1, 1), (1, 0))
CORRELATION_RADIUS = F(1, 3200)
INITIAL_RADIUS = F(1, 7000)
TILT = F(7, 9)
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
    check("inherited-proof-count", len(proofs) == 43)
    check("imported-helper-source-is-bound", Path(bound.__file__).name in sources)
    for path, digest in PROOFS.items():
        check("new-proof-hash:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


add = bound.interval_add
sub = bound.interval_sub
mul = bound.interval_mul
scale = bound.interval_scale
square = bound.interval_square
divide = bound.interval_div
sqrt = bound.interval_sqrt
point = bound.point
expand = bound.expand


def clip_expectation(interval):
    return max(F(-1), interval[0]), min(F(1), interval[1])


def outward(interval, denominator=10 ** 12):
    lower = F((interval[0] * denominator).__floor__(), denominator)
    upper = F((interval[1] * denominator).__ceil__(), denominator)
    check("outward-report-interval", lower <= interval[0] <= interval[1] <= upper)
    return [str(lower), str(upper)]


def identity_box_decision(box, profile_tilt=True):
    """Conservative confidence-set exclusion; no estimated equality plug-in.

    Box keys: initial_mean, C_L, C_LL, C_H, C_HH, C_HL, and M_H when profiling.
    Every value is an exact closed interval. Degenerate denominators return
    inconclusive. Returned interval gaps are diagnostic, not p-values.
    """
    e = box["initial_mean"]
    if not -1 < e[0] <= e[1] < 1:
        return {"reject": False, "reason": "initial-sign mass not bounded away from zero"}
    x, y, z, v, r = (box["C_" + word] for word in WORDS)
    if profile_tilt:
        denominator = sub(point(1), z)
        if denominator[0] <= 0:
            return {"reject": False, "reason": "tilt-inference denominator not positive"}
        tilt = divide(sub(box["M_H"], e), denominator)
        if not -1 < tilt[0] <= tilt[1] < 1:
            return {"reject": False, "reason": "inferred tilt not confined inside (-1,1)"}
    else:
        tilt = point(TILT)
    e2 = square(e)
    g = sub(point(1), e2)
    w = add(point(1), mul(tilt, e))
    q = add(e, tilt)
    eq = mul(e, q)
    X, Z = sub(x, e2), sub(z, e2)
    A = sub(mul(g, sub(y, e2)), square(X))
    B = sub(mul(g, sub(mul(w, v), eq)), square(sub(mul(w, z), eq)))
    C = sub(mul(g, sub(r, e2)), mul(X, Z))
    if A[1] < 0 or B[1] < 0:
        return {"reject": True, "reason": "nonnegative null variance impossible", "tilt": tilt}
    A, B = (max(F(0), A[0]), A[1]), (max(F(0), B[0]), B[1])
    branches = []
    for sector in (-1, 1):
        denominator = mul(sub(point(1), scale(tilt, sector)), w)
        if denominator[0] <= 0:
            return {"reject": False, "reason": "rank-identity denominator not positive"}
        radical = sqrt(divide(mul(A, B), denominator))
        for orientation in (-1, 1):
            possible = scale(radical, orientation)
            gap = max(C[0] - possible[1], possible[0] - C[1])
            branches.append({"doubleton_sign": sector, "orientation": orientation,
                             "possible_C": possible, "gap": gap})
    return {"reject": all(branch["gap"] > 0 for branch in branches),
            "reason": "four rank-one branches evaluated", "tilt": tilt,
            "C": C, "A": A, "B": B, "branches": branches}


def confidence_decision(statistics, profile_tilt=True):
    """Apply the stated test to exact empirical means from the fixed protocol."""
    names = ["initial_mean"] + ["C_" + word for word in WORDS]
    if profile_tilt:
        names.append("M_H")
    box = {}
    for name in names:
        value = F(statistics[name])
        if not -1 <= value <= 1:
            raise ValueError("An empirical sign statistic lies outside [-1,1]")
        radius = INITIAL_RADIUS if name == "initial_mean" else CORRELATION_RADIUS
        box[name] = clip_expectation(expand(point(value), radius))
    return identity_box_decision(box, profile_tilt)


def statistics_from_counts(counts, profile_tilt=True):
    """Exact statistics for a fixed five-arm design.

    counts[word] maps the four integer outcome pairs (S0,ST) to counts.
    The prescribed equal per-arm count is enforced; no optional stopping.
    """
    per_word = 120_000_000 if profile_tilt else 115_000_000
    total_initial = 0
    statistics = {}
    outcomes = {(a, b) for a in (-1, 1) for b in (-1, 1)}
    for word in WORDS:
        table = counts[word]
        if set(table) != outcomes or any(type(n) is not int or n < 0 for n in table.values()):
            raise ValueError("Each arm must contain four nonnegative integer outcome counts")
        if sum(table.values()) != per_word:
            raise ValueError("Each arm must have the prescribed fixed number of trials")
        statistics["C_" + word] = F(sum(a * b * n for (a, b), n in table.items()), per_word)
        total_initial += sum(a * n for (a, _), n in table.items())
        if word == "H" and profile_tilt:
            statistics["M_H"] = F(sum(b * n for (_, b), n in table.items()), per_word)
    statistics["initial_mean"] = F(total_initial, 5 * per_word)
    return statistics


def hoeffding_certificate(per_word, statistic_count):
    # For X in [-1,1], two-sided Hoeffding is 2*exp(-N*r^2/2).
    exponent = min(F(per_word, 2) * CORRELATION_RADIUS ** 2,
                   F(5 * per_word, 2) * INITIAL_RADIUS ** 2)
    term = F(1)
    exponential_lower = term
    for k in range(1, 31):
        term *= exponent / k
        exponential_lower += term
    # Positive-term truncation bounds exp(exponent) from below. Thus no
    # floating-point log or exp enters the certified probability comparison.
    failure_upper = F(2 * statistic_count, 1) / exponential_lower
    check("simultaneous-Hoeffding-failure-below-one-twentieth", failure_upper < F(1, 20))
    rounded_upper = F((failure_upper * 10 ** 12).__ceil__(), 10 ** 12)
    check("outward-failure-bound", failure_upper <= rounded_upper < F(1, 20))
    return {"statistics": statistic_count, "minimum_Hoeffding_exponent": str(exponent),
            "positive_exponential_series_terms": 31,
            "simultaneous_failure_probability_upper": str(rounded_upper)}


def certify_protocol(profile_tilt, moments):
    per_word, statistic_count = (120_000_000, 7) if profile_tilt else (115_000_000, 6)
    tail = hoeffding_certificate(per_word, statistic_count)
    # On the target concentration event, each empirical confidence interval
    # is contained in this twice-radius deterministic box, including the
    # inherited exact target-moment Taylor enclosure.
    box = {"initial_mean": expand(point(0), 2 * INITIAL_RADIUS)}
    for word, word_id in zip(WORDS, WORD_IDS):
        box["C_" + word] = expand(moments[word_id][1], 2 * CORRELATION_RADIUS)
    if profile_tilt:
        box["M_H"] = expand(moments[(1,)][0], 2 * CORRELATION_RADIUS)
    decision = identity_box_decision(box, profile_tilt)
    check("nominal-doubled-confidence-box-rejects-null", decision["reject"] is True)
    check("nominal-proof-uses-all-four-branches", len(decision["branches"]) == 4)
    minimum_gap = min(branch["gap"] for branch in decision["branches"])
    coarse_gap = F(180 if profile_tilt else 265, 1_000_000)
    check("nominal-power-strict-branch-gap", minimum_gap > coarse_gap)
    if profile_tilt:
        check("inferred-tilt-document-lower", decision["tilt"][0] > F("0.775475"))
        check("inferred-tilt-document-upper", decision["tilt"][1] < F("0.780086"))
    report_branches = []
    for branch in decision["branches"]:
        gap_floor = F((branch["gap"] * 10 ** 12).__floor__(), 10 ** 12)
        report_branches.append({"doubleton_sign": branch["doubleton_sign"],
                                "orientation": branch["orientation"],
                                "possible_C_interval": outward(branch["possible_C"]),
                                "strict_separation_lower": str(gap_floor)})
    name = "profiled_tilt" if profile_tilt else "fixed_tilt"
    print(f"{name}: {5*per_word} trials; each error probability <= "
          f"{tail['simultaneous_failure_probability_upper']}; nominal gap approximately {float(minimum_gap):.12f}")
    return {"status": "PASS", "protocol": name, "trials_per_word": per_word,
            "total_trials": 5 * per_word,
            "statistic_names": ["initial_mean"] + ["C_" + word for word in WORDS]
                               + (["M_H"] if profile_tilt else []),
            "initial_mean_confidence_half_width": str(INITIAL_RADIUS),
            "other_confidence_half_width": str(CORRELATION_RADIUS),
            "confidence_coverage": tail,
            "type_I_error_upper": tail["simultaneous_failure_probability_upper"],
            "nominal_type_II_error_upper": tail["simultaneous_failure_probability_upper"],
            "nominal_target_power_lower": str(1 - F(tail["simultaneous_failure_probability_upper"])),
            "nominal_doubled_box_tilt_interval": outward(decision["tilt"]),
            "nominal_doubled_box_C_interval": outward(decision["C"]),
            "nominal_strict_branch_gap_lower": str(coarse_gap),
            "nominal_branches": report_branches}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    moments, error = bound.target_moments()
    check("target-moment-error-below-1e-30", error < F(1, 10 ** 30))
    fixed = certify_protocol(False, moments)
    profiled = certify_protocol(True, moments)
    # A zero-mass sign sector cannot cause an automatic positive conclusion.
    degenerate = {"initial_mean": F(1), "M_H": F(1)}
    degenerate.update({"C_" + word: F(1) for word in WORDS})
    check("degenerate-sign-data-return-inconclusive",
          confidence_decision(degenerate, True)["reject"] is False)
    # This exact expectation vector comes from reversible complete-reset
    # kernels at both fields and is compatible with a two-state null.
    reset_null = {"initial_mean": F(0), "M_H": TILT}
    reset_null.update({"C_" + word: F(0) for word in WORDS})
    check("reset-null-confidence-box-not-rejected",
          confidence_decision(reset_null, True)["reject"] is False)
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "dependencies": "Python standard library only; imported moment/interval helpers are SHA256-bound",
        "arithmetic": "Exact rational intervals, integer square-root bounds, and positive-term exponential lower bounds. No floating-point probability decisions or Monte Carlo.",
        "fixture": {"tanh_J": "1/3", "nominal_high_tilt": "7/9", "clock": "1",
                    "words": list(WORDS)},
        "sampling_contract": "Fixed arm allocations, chosen before each initial readout; independent trials from one fixed common preparation and fixed kernels. Independence of statistics extracted from the same trial is not assumed.",
        "null": "Every at-most-three-state ordinary reversible Markov predictor with common preparation, deterministic binary readout, and Gibbs tilt; numerical high tilt is arbitrary in (-1,1) for the profiled protocol",
        "null_identity": "(1-s*m)*(1+m*e)*C^2=A*B for one s in {-1,+1}; A,B nonnegative",
        "identity_coordinates": {"g": "1-e^2", "w": "1+m*e", "q": "e+m",
                                 "A": "g*(y-e^2)-(x-e^2)^2",
                                 "B": "g*(w*v-e*q)-(w*z-e*q)^2",
                                 "C": "g*(r-e^2)-(x-e^2)*(z-e^2)",
                                 "x,y,z,v,r": "C_L,C_LL,C_H,C_HH,C_HL"},
        "tilt_profile": "m=(M_H-e)/(1-C_H); return inconclusive if the denominator or strict physical interval cannot be certified",
        "profiled_tilt_protocol": profiled,
        "fixed_tilt_alternative": fixed,
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "These are conservative sufficient acquisition budgets, not optimal sample complexities or device feasibility claims. Power is guaranteed at the specified nominal target, separately from uniform null validity. The fresh independent reset sampling contract is not supplied by a target-only reset-time calculation and does not hold automatically for arbitrarily slow rivals. Unknown detector effects, preparation drift, or correlations require an additional validated model; no serial or optional-stopping guarantee is claimed.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact frozen-sampling checks -> {args.output}")


if __name__ == "__main__":
    main()
