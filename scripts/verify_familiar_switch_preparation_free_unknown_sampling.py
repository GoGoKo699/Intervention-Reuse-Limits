#!/usr/bin/env python3
"""Exact serial quota certificate for the seven-word unknown-tilt test.

The fixed statistic uses two local tangent scores and fourteen return
gates. Endpoint-registration errors are bounded conditional on the full
pre-preparation history, without conditioning on a selected sign. A
deterministic first-n comparison controls the resulting selection errors.
No rival preparation promise, independent-trial assumption, selected-row
detector calibration, Gaussian approximation or floating-point decision
is used. The accompanying written proof is part of the certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

import verify_familiar_switch_preparation_free_unknown_tilt as core

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_preparation_free_unknown_tilt.json"
# Frozen reviewed analytic core and its proof snapshots.
INPUT_SHA256 = "2facaf21db92bee7cd575eea74d3935f47c8871e6bb78476ab78ab53b12852f0"
N = 80_000_000
M = 168_000_000
RADIUS = F(1, 1000)
GATE = F(1, 2000)
CENTER_ERROR = F(1, 10**12)
SIGNAL = F(12269, 10**8)
ENDPOINT_ERROR = F(1, 10**6)
TARGET_PAIR_TV = F(5, 10**6)
ERROR_COUNT_CAP = 280
INCREMENT_CAP = F(1, 4)
THRESHOLDS = {-1: F(55, 10**6), 1: -F(62, 10**6)}
CAPS = {
    -1: {"L": F(67, 100), "H": F(14), "V": F(11, 500)},
    1: {"L": F(4, 5), "H": F(18), "V": F(7, 250)},
}
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def provenance():
    payload = (ROOT / INPUT).read_bytes()
    check("input-core-report-hash", hashlib.sha256(payload).hexdigest() == INPUT_SHA256)
    inherited = json.loads(payload)
    check("input-core-report-pass", inherited["status"] == "PASS")
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
    check("imported-analytic-core-bound", Path(core.__file__).name in sources)
    check("unified-proof-bound", "docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md" in proofs)
    check("focused-source-audit-bound", "docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md" in proofs)
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


def rounded_up(value, denominator=10**12):
    return F((value * denominator).__ceil__(), denominator)


def rounded_down(value, denominator=10**12):
    return F((value * denominator).__floor__(), denominator)


def exp_negative_upper(value, degree=120):
    """Positive Taylor terms bound exp(value) from below for every value>=0."""
    check("exponential-tail-argument-nonnegative", value >= 0)
    lower = sum((value**power / factorial(power) for power in range(degree + 1)), F(0))
    return 1 / lower


def fixed_coefficients():
    polynomial = core.witness_polynomial()
    result = {}
    for sign in (-1, 1):
        center = core.CENTERS[sign]
        result[sign] = {
            "center": center,
            "score": polynomial.evaluate(center),
            "gradient": tuple(core.derivative(polynomial, j).evaluate(center) for j in range(7)),
        }
    return result


def local_geometry_certificate():
    target_certificate, returns = core.target_certificate()
    geometry = core.population_robustness_certificate(returns)
    coefficients = fixed_coefficients()
    check("registered-seven-word-order",
          core.WORD_NAMES == ("L", "LL", "H", "LH", "HL", "LLH", "HLL"))
    check("core-local-box-matches-sampling-box", F(geometry["local_coordinate_radius"]) == RADIUS)
    check("core-center-error-matches-sampling", F(geometry["target_center_error"]) == CENTER_ERROR)
    check("core-signal-matches-sampling", F(geometry["target_witness_magnitude_lower"]) == SIGNAL)
    for sign in (-1, 1):
        row = geometry["sign_certificates"][str(sign)]
        fixed = coefficients[sign]
        check(f"sign-{sign}:same-rational-center", tuple(map(F, row["center"])) == fixed["center"])
        check(f"sign-{sign}:same-fixed-score", F(row["center_score"]) == fixed["score"])
        check(f"sign-{sign}:same-fixed-gradient",
              tuple(map(F, row["gradient_at_center"])) == fixed["gradient"])
        check(f"sign-{sign}:center-itself-has-signed-margin", -sign * fixed["score"] > SIGNAL)
        check(f"sign-{sign}:registered-gradient-cap", F(row["gradient_l1_cap"]) == CAPS[sign]["L"])
        check(f"sign-{sign}:registered-Hessian-cap",
              F(row["Hessian_absolute_entry_sum_cap"]) == CAPS[sign]["H"])
        check(f"sign-{sign}:registered-local-variance-cap",
              F(row["Bernoulli_linear_variance_sum_cap"]) == CAPS[sign]["V"])
        check(f"sign-{sign}:fixed-gradient-l1-bound",
              sum(map(abs, fixed["gradient"])) < CAPS[sign]["L"])
        check(f"sign-{sign}:fixed-gradient-increment-bound",
              max(map(abs, fixed["gradient"])) < F(row["centered_single_return_increment_cap"]) < INCREMENT_CAP)
    return {
        "status": "PASS", "target_parameters": {"t": target_certificate["t"], "m": target_certificate["m"],
                                                       "tau_L": "1", "tau_H": "1"},
        "target_center_error": str(CENTER_ERROR), "population_box_radius": str(RADIUS),
        "target_signed_center_score_lower": str(SIGNAL),
        "sign_certificates": geometry["sign_certificates"],
        "variance_scope": "Within the local box, the inherited bound controls sum_j g_j(center)^2*q_j*(1-q_j). Null singleton q equals its fixed reference row. Target oracle conditional q is within center_error+B/(1/2-B) of the center. No global variance bound outside the box is used.",
    }, coefficients


def registration_certificate():
    check("error-count-cap-below-quota", ERROR_COUNT_CAP < N)
    check("conditional-error-mean-cap", M * ENDPOINT_ERROR == 168)
    degree = 20
    e_lower = sum((F(1, factorial(power)) for power in range(degree + 1)), F(0))
    first_omitted = F(1, factorial(degree + 1))
    e_upper = e_lower + first_omitted / (1 - F(1, degree + 2))
    check("exact-e-upper-below-eleven-quarters", e_upper < F(11, 4))
    # For each of14 word/endpoint counts, conditional MGF at log2 gives
    # P(E>280)<=2^-280(1+eta)^M<=2^-280 exp(M eta).
    bad_counts = 14 * F(11, 4)**168 / F(2)**ERROR_COUNT_CAP
    replacement = F(2 * ERROR_COUNT_CAP, N)
    check("registered-coordinate-replacement-budget", replacement == F(7, 10**6))
    check("error-count-failure-cap", bad_counts < F(464, 10**12))
    return {
        "status": "PASS", "conditional_boundary_error_per_endpoint": str(ENDPOINT_ERROR),
        "word_endpoint_count_number": 14, "error_cap_per_word_endpoint": ERROR_COUNT_CAP,
        "conditional_error_count_MGF_argument": "log(2)",
        "bad_count_probability_exact_rational_upper": str(bad_counts),
        "bad_count_probability_upper": str(rounded_up(bad_counts)),
        "observed_vs_padded_oracle_return_error": str(replacement),
        "selection_comparison": "On observed completion, each first-n observed-sign return mean differs from its padded first-n true-boundary-sign mean by at most(E_initial+E_final)/n. Errors may correlate with kicks and final outcomes.",
        "one_sign_null": "On the good error-count event, the opposite observed-sign quota cannot complete because280<n. A one-sign model can reject only on the same globally budgeted bad-count event.",
    }, bad_counts, replacement


def sampling_certificate(bad_counts, replacement):
    target_bias = TARGET_PAIR_TV / (F(1, 2) - TARGET_PAIR_TV)
    target_observed_sign_lower = F(1, 2) - TARGET_PAIR_TV - ENDPOINT_ERROR
    check("target-return-bias-exact", target_bias == F(1, 99999))
    check("target-conditional-means-inside-local-variance-box", target_bias + CENTER_ERROR < RADIUS)
    null_distance = RADIUS - GATE - replacement
    target_distance = GATE - replacement - target_bias - CENTER_ERROR
    check("null-gate-distance-positive", null_distance > 0)
    check("target-gate-distance-positive", target_distance > 0)
    rows, null_tails, target_tails = {}, [], []
    for sign in (-1, 1):
        limits = CAPS[sign]
        curvature = limits["H"] * RADIUS**2 / 2
        threshold = abs(THRESHOLDS[sign])
        null_margin = threshold - curvature - limits["L"] * replacement
        target_margin = SIGNAL - threshold - limits["L"] * (replacement + target_bias + CENTER_ERROR)
        check(f"sign-{sign}:null-score-margin-positive", null_margin > 0)
        check(f"sign-{sign}:target-score-margin-positive", target_margin > 0)
        null_exponent = N * null_margin**2 / (2 * (limits["V"] + INCREMENT_CAP * null_margin / 3))
        target_exponent = N * target_margin**2 / (2 * (limits["V"] + INCREMENT_CAP * target_margin / 3))
        null_tail, target_tail = map(exp_negative_upper, (null_exponent, target_exponent))
        null_tails.append(null_tail)
        target_tails.append(target_tail)
        rows[str(sign)] = {
            "threshold": str(THRESHOLDS[sign]),
            "rejection_direction": "above" if sign == -1 else "below",
            "null_Taylor_remainder_upper": str(curvature),
            "registration_score_displacement_upper": str(limits["L"] * replacement),
            "target_oracle_drift_upper": str(rounded_up(limits["L"] * target_bias)),
            "null_score_margin": str(null_margin), "target_score_margin_lower": str(rounded_down(target_margin)),
            "local_variance_cap": str(limits["V"]), "centered_increment_cap": str(INCREMENT_CAP),
            "null_Bernstein_exponent_lower": str(rounded_down(null_exponent)),
            "target_Bernstein_exponent_lower": str(rounded_down(target_exponent)),
            "null_score_tail_upper": str(rounded_up(null_tail)),
            "target_score_tail_upper": str(rounded_up(target_tail)),
        }
    null_gate = 2 * exp_negative_upper(2 * N * null_distance**2)
    target_gate = 28 * exp_negative_upper(2 * N * target_distance**2)
    quota_margin = M * target_observed_sign_lower - N
    check("target-quota-mean-margin-positive", quota_margin > 0)
    quota_exponent = 2 * quota_margin**2 / M
    check("target-quota-exponent-exceeds-one-hundred", quota_exponent > 100)
    quota_failure = 14 * exp_negative_upper(F(100))
    # For each fixed null choose one singleton before looking at data.
    # Inside/outside its population box are disjoint model cases. No
    # union over singleton signs and no conditioning on quota completion.
    alpha = bad_counts + max(null_gate, *null_tails)
    beta = bad_counts + sum(target_tails) + target_gate + quota_failure
    check("type-I-exactly-below-five-percent", alpha < F(1, 20))
    check("type-II-exactly-below-five-percent", beta < F(1, 20))
    check("reported-type-I-cap", alpha < F(40389, 10**6))
    check("reported-type-II-cap", beta < F(45261, 10**6))
    check("proof-type-I-outward-rounding", alpha < F(403887335941, 10**13))
    check("proof-type-II-outward-rounding", beta < F(452601191033, 10**13))
    return {
        "status": "PASS", "quota_per_word_sign": N, "attempts_per_word": M,
        "total_attempt_cap": 7 * M, "total_retained_pairs_on_completion": 14 * N,
        "empirical_gate_radius": str(GATE), "population_box_radius": str(RADIUS),
        "target_true_boundary_pair_TV_budget": str(TARGET_PAIR_TV),
        "target_oracle_return_bias": str(target_bias),
        "target_observed_sign_probability_lower": str(target_observed_sign_lower),
        "sign_score_certificates": rows,
        "outside_null_gate_pass_upper": str(rounded_up(null_gate)),
        "target_gate_failure_upper": str(rounded_up(target_gate)),
        "target_quota_exponent_lower": str(rounded_down(quota_exponent)),
        "used_quota_exponent_lower": "100",
        "target_quota_failure_upper": str(rounded_up(quota_failure, 10**45)),
        "type_I_upper": str(rounded_up(alpha, 10**13)), "type_II_upper": str(rounded_up(beta, 10**13)),
        "type_I_formula": "bad_counts+max(outside_null_gate,null_score_minus,null_score_plus)",
        "type_II_formula": "bad_counts+target_score_minus+target_score_plus+target_gate+quota_failure",
    }


def decide(retained_counts, return_counts):
    """Evaluate the registered test from first-n count summaries.

    Each argument maps signs -1,+1 to seven integer counts in WORD_NAMES
    order. return_counts are successes among the retained records. The
    caller must have retained the first n records and stopped at the fixed
    attempt cap; this function cannot infer that acquisition history.
    """
    for sign in (-1, 1):
        if sign not in retained_counts or sign not in return_counts:
            raise ValueError("Both initial signs are required")
        if len(retained_counts[sign]) != 7 or len(return_counts[sign]) != 7:
            raise ValueError("Exactly seven word counts are required per sign")
        for kept, success in zip(retained_counts[sign], return_counts[sign]):
            if type(kept) is not int or type(success) is not int or not 0 <= success <= kept <= N:
                raise ValueError("Counts must be integers satisfying0<=returns<=retained<=quota")
    if any(count != N for sign in (-1, 1) for count in retained_counts[sign]):
        return False
    coefficients = fixed_coefficients()
    scores = {}
    for sign in (-1, 1):
        row = tuple(F(count, N) for count in return_counts[sign])
        fixed = coefficients[sign]
        if any(abs(value - center) > GATE for value, center in zip(row, fixed["center"])):
            return False
        scores[sign] = fixed["score"] + sum(g * (value - center)
            for g, value, center in zip(fixed["gradient"], row, fixed["center"]))
    return scores[-1] > THRESHOLDS[-1] and scores[1] < THRESHOLDS[1]


def resource_certificate():
    lengths = [len(word) for word in core.WORDS]
    low = sum(word.count(0) for word in core.WORDS)
    high = sum(word.count(1) for word in core.WORDS)
    # Begin and end at the low field. The last return to low precedes
    # the next reset and is counted even for a word ending at high field.
    up = down = seams = 0
    for word in core.WORDS:
        path = (0,) + word + (0,)
        up += sum(left == 0 and right == 1 for left, right in zip(path, path[1:]))
        down += sum(left == 1 and right == 0 for left, right in zip(path, path[1:]))
        seams += sum(left == right == 0 for left, right in zip(word, word[1:]))
    check("resource-word-lengths", lengths == [1, 2, 1, 2, 2, 3, 3])
    check("resource-low-high-ticks-per-cycle", low == 9 and high == 5)
    check("resource-ramp-count-per-cycle", up == down == 5)
    check("resource-same-low-seams-per-cycle", seams == 3)
    pairs, endpoints, active = 7 * M, 14 * M, sum(lengths) * M
    check("resource-total-pairs", pairs == 1_176_000_000)
    check("resource-total-endpoints-and-active-ticks", endpoints == active == 2_352_000_000)
    reset_units = 24 * pairs
    reset_plus_active = reset_units + active
    check("resource-target-reset-time-units", reset_units == 28_224_000_000)
    check("resource-target-reset-plus-active-time-units", reset_plus_active == 30_576_000_000)
    check("nominal-target-reset-minimum-mass", (1 - core.T) / 4 == F(1, 6))
    check("nominal-target-reset-gap-coefficient", 1 - core.T == F(2, 3))
    positive_series = sum((F(16)**power / factorial(power) for power in range(33)), F(0))
    check("target-reset-exp16-lower", positive_series > 8_000_000)
    check("target-reset-error-quarter-ppm", 2 / positive_series < F(1, 4_000_000))
    return {
        "status": "PASS", "word_lengths": lengths, "complete_seven_word_cycles": M,
        "pairs_and_target_resets": pairs, "recorded_binary_endpoints": endpoints,
        "total_active_ticks": active, "low_active_ticks": low * M, "high_active_ticks": high * M,
        "up_ramps": up * M, "down_ramps": down * M, "total_up_down_ramps": (up + down) * M,
        "same_low_tick_seams": seams * M,
        "nominal_target_reset_duration_in_inverse_Gamma": 24,
        "nominal_target_reset_TV_upper": "1/4000000",
        "total_target_reset_time_in_inverse_Gamma": reset_units,
        "total_reset_plus_active_time_in_inverse_Gamma": reset_plus_active,
        "additional_sequential_time": "1176000000*(T_initial+T_final)+840000000*(T_up+T_down), plus other overhead",
        "reset_scope": "Target-only nominal heat-bath reset with minimum mass1/6 and gap2Gamma/3; L2 contraction gives TV<2exp(-16)<quarterppm at24/Gamma from any starting state. No finite reset duration or preparation guarantee is imposed on rivals.",
        "budget_scope": "The target reset error, postinitial hidden-law disturbance and active-control errors must jointly fit the separate5ppm true-boundary pair budget. The1ppm boundary-registration premise is additional and is not proved by this clock accounting. Ramps/readout intervals must be assigned to their declared operational boundaries without double counting. Same-low seams do not authorize an intervening hidden kick.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    geometry, _ = local_geometry_certificate()
    registration, bad_counts, replacement = registration_certificate()
    sampling = sampling_certificate(bad_counts, replacement)
    resources = resource_certificate()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()}, "dependencies": "Python standard library only",
        "arithmetic": "Exact rational target enclosures, cubic polynomial derivatives, local Hessian/Bernoulli variance bounds, error-count MGF and exponential-tail certificates. All probability assertions use Fraction arithmetic; no floating-point proof decisions.",
        "test": {
            "words": list(core.WORD_NAMES), "unknown_null_tilt": "one fixed m in(-1,1)",
            "quota_per_word_recorded_sign": N, "attempts_per_word": M, "total_attempt_cap": 7 * M,
            "oracle_endpoints": "True signs at the start and end of the active word; the initial boundary is after the initial instrument",
            "selection": "Retain the first n records in each word/recorded-initial-sign group; incomplete groups at the fixed cap imply nonrejection",
            "score": "W_s=F(c_s)+gradient(F)(c_s) dot(empirical_return_row_s-c_s), a fixed tangent rather than F(empirical_row)",
            "rejection": "All14 coordinate gates of radius1/2000 pass AND W_minus>55/1000000 AND W_plus< -62/1000000",
            "determinant": "F=r_LH*r_HLL-r_LLH*r_HL+r_L*r_H*(r_LLH-r_HLL)+r_LL*r_H*(r_HL-r_LH)",
        },
        "local_geometry_certificate": geometry, "registration_certificate": registration,
        "sampling_certificate": sampling, "resource_certificate": resources,
        "null_contract": "One fixed ordinary reversible at-most-three-state model with deterministic binary readout, reused kernels and common Gibbs tilt relation for an unknown fixed tilt. Preparation and initial kicks may depend arbitrarily on history and word. Conditional on all relevant past and current model state, active transitions use the fixed kernels; uncounted predictive controller memory is excluded. No null reset or stationary-preparation promise is imposed. Each recorded endpoint has conditional error at most1ppm relative to its true active-boundary sign, before the current preparation; errors may be correlated with one another and hidden kicks.",
        "target_power_contract": "For one fixed nominal target, every true-boundary paired law is conditionally within5ppm TV before current preparation, for every word and full past. The same1ppm boundary-registration envelope applies. This execution/preparation requirement is target-only and is separate from the broader70ppm population-separation result.",
        "sampling_scope": "A fixed attempt cap with stopped/padded oracle martingale concentration; no independent-trial assumption. Current true initial sign is revealed to oracle selection, while current hidden target state and noisy electronic transcript are integrated out until the completed trial. All prior transcripts remain in the history. The probability law is never conditioned on quota completion or passing a gate.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
        "limitations": "A sufficient budget for this fixed seven-word design, not a sample-complexity optimum or device demonstration. Removing rival preparation and numerical-tilt premises does not remove the fixed-kernel/Gibbs/readout contract. Endpoint registration is a conditional calibration premise, not a conclusion from these binary counts. Target throughput, calibration acquisition, apparatus memory, and reset/readout time require separate accounting.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact preparation-free sampling checks -> {args.output}")


if __name__ == "__main__":
    main()
