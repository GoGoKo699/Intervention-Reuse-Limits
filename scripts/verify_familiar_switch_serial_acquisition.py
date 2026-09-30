#!/usr/bin/env python3
"""Exact constants for the conditional-law serial five-setting acquisition.

The universal martingale and instrument-transfer arguments are in the bound
proof snapshot. This verifier checks their finite rational premises and costs;
it does not certify an apparatus's conditional-law promise.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_profiled_score.json"
INPUT_SHA256 = "27457ae626a6e991f73327436b08c04a8e2c024ff683f4defe34b975b9264f77"
PROOFS = {
    "docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION.md": "7572f23aa9670a745e492dc269317459bc5bee8d6b0b5e2994db402b9870bc6b",
    "docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION_SOURCE_AUDIT.md": "0d3008eb83afb86d77f309aded63e4bfdd05980ec1ec4ae4a06351e79cfb7b05",
}
N = 10_000_000
EPSILON = F(1, 10**6)
ETA = F(1, 50)
RANGE_SUM = F(9, 100)
RANGE_SQUARE_SUM = F(1, 500)
INCREMENT = F(1, 20)
NULL_VARIANCE = F(9, 50000)
TARGET_VARIANCE = F(17, 200000)
THRESHOLD = -F(1, 80000)
TARGET_SIGNAL = F(22667, 10**9)
POPULATION_RADIUS = F(11, 5000)
EMPIRICAL_RADIUS = F(13, 10000)
CENTER_ERROR = F(1, 10**12)
PROXY = (F(6, 5), F(6, 5), F(6, 5), F(2), F(6, 5), F(6, 5), F(2))
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def provenance():
    check("input-report-hash", digest(ROOT / INPUT) == INPUT_SHA256)
    inherited = json.loads((ROOT / INPUT).read_text())
    check("input-report-pass", inherited["status"] == "PASS")
    sources = dict(inherited["source_sha256"])
    proofs = dict(inherited["proof_snapshot_sha256"])
    reports = dict(inherited.get("input_report_sha256", {}))
    reports[INPUT] = INPUT_SHA256
    for name, sha in sources.items():
        check("inherited-source:" + name, digest(ROOT / "scripts" / name) == sha)
    for name, sha in {**proofs, **reports}.items():
        check("inherited-file:" + name, digest(ROOT / name) == sha)
    for name, sha in PROOFS.items():
        check("new-proof-hash-frozen:" + name, len(sha) == 64)
        check("new-proof:" + name, digest(ROOT / name) == sha)
        proofs[name] = sha
    sources[Path(__file__).name] = digest(Path(__file__))
    return inherited, sources, proofs, reports


def positive_exp_sum(x, degree=160):
    """A strict rational lower bound for exp(x), x>0."""
    if x <= 0:
        raise ValueError("Positive exponent required")
    total = term = F(1)
    for order in range(1, degree + 1):
        term *= x / order
        total += term
    return total


def exp_negative_upper(x):
    return 1 / positive_exp_sum(x)


def upper(value, denominator=10**12):
    scaled = value * denominator
    return F(-(-scaled.numerator // scaled.denominator), denominator)


def inherited_constants(inherited):
    test = inherited["test"]
    local = inherited["local_covariance_certificate"]
    quadratic = inherited["quadratic_remainder_certificate"]
    check("fixed-word-menu", test["words"] == ["L", "LL", "H", "HH", "HL"])
    check("registered-trials-per-word", test["independent_reset_trials_per_word"] == N)
    check("registered-population-radius", F(test["population_box_radius"]) == POPULATION_RADIUS)
    check("registered-empirical-radius", F(test["empirical_gate_radius"]) == EMPIRICAL_RADIUS)
    check("registered-null-variance", F(local["uniform_null_variance_cap"]) == NULL_VARIANCE)
    check("registered-target-variance", F(local["target_variance_cap"]) == TARGET_VARIANCE)
    check("registered-increment-cap", F(local["common_centered_increment_cap"]) == INCREMENT)
    check("registered-target-signal", F(local["target_absolute_score_lower"]) == TARGET_SIGNAL)
    check("registered-center-error", F(inherited["target_center"]["coordinate_error_upper"]) == CENTER_ERROR)
    check("registered-rejection-threshold", F(inherited["sampling_certificate"]["rejection_threshold"]) == THRESHOLD)
    check("registered-vector-proxy", tuple(map(F, quadratic["subGaussian_proxy_diagonal_before_dividing_by_N"])) == PROXY)
    check("registered-spectral-cap", F(quadratic["weighted_spectral_norm_cap"]) == F(7, 4))
    check("registered-remainder-cost", F(quadratic["used_remainder_cost_upper"]) == F(65, 4))
    check("registered-quadratic-exponent", F(quadratic["quadratic_tail_exponent"]) == 5)
    check("registered-initial-controls-cancel", sum(map(F, local["common_initial_control_variates"])) == 0)
    ranges = list(map(F, local["arm_centered_increment_upper"]))
    check("five-positive-arm-ranges", len(ranges) == 5 and all(0 < w < INCREMENT for w in ranges))
    # Despite the report key's name, the bound source takes the maximum
    # minus minimum of all four paired-outcome lookup values. It therefore
    # bounds oscillation under every actual conditional outcome law.
    check("sum-of-outcome-ranges", sum(ranges) < RANGE_SUM)
    check("sum-of-squared-outcome-ranges", sum(w*w for w in ranges) < RANGE_SQUARE_SUM)
    return {
        "arm_outcome_range_upper": list(map(str, ranges)),
        "sum_outcome_ranges_upper": str(sum(ranges)),
        "sum_squared_outcome_ranges_upper": str(sum(w*w for w in ranges)),
        "range_sum_cap": str(RANGE_SUM),
        "range_square_sum_cap": str(RANGE_SQUARE_SUM),
        "centered_increment_cap": str(INCREMENT),
        "interpretation": "Frozen source enumerates the four outcome values at coefficient-box vertices and bounds their full maximum-minus-minimum range.",
    }


def serial_risks():
    reciprocal_sum = sum(1 / d for d in PROXY)
    check("proxy-reciprocal-sum", reciprocal_sum == F(31, 6))
    half_drift_quadratic = F(1, 2) * F(7, 4) * 4 * reciprocal_sum
    check("quadratic-drift-coefficient", half_drift_quadratic == F(217, 12))
    remainder = ((1 + ETA) * F(65, 4*N)
                 + (1 + 1/ETA) * half_drift_quadratic * EPSILON**2)
    check("serial-remainder-value", remainder == F(6633689, 4 * 10**12))
    drift = RANGE_SUM * EPSILON
    variance_increment = RANGE_SQUARE_SUM * EPSILON
    null_margin = -THRESHOLD - remainder - drift
    target_margin = TARGET_SIGNAL + THRESHOLD - remainder - drift
    check("null-linear-margin-positive", null_margin > 0)
    check("target-linear-margin-positive", target_margin > 0)
    null_exponent = N * null_margin**2 / (2 * (NULL_VARIANCE + variance_increment + INCREMENT*null_margin/3))
    target_exponent = N * target_margin**2 / (2 * (TARGET_VARIANCE + variance_increment + INCREMENT*target_margin/3))
    null_linear = exp_negative_upper(null_exponent)
    target_linear = exp_negative_upper(target_exponent)
    quadratic = exp_negative_upper(F(5))
    outside_distance = POPULATION_RADIUS - EMPIRICAL_RADIUS - 2*EPSILON
    target_distance = EMPIRICAL_RADIUS - CENTER_ERROR - 2*EPSILON
    check("serial-gate-distances-positive", outside_distance > 0 and target_distance > 0)
    outside = 2 * exp_negative_upper(N * outside_distance**2 / 2)
    gate = (12 * exp_negative_upper(N * target_distance**2 / 2)
            + 2 * exp_negative_upper(5*N * target_distance**2 / 2))
    inside = null_linear + quadratic
    alpha = max(inside, outside)
    beta = target_linear + quadratic + gate
    check("serial-type-I-below-five-percent", alpha < F(1, 20))
    check("serial-type-II-below-five-percent", beta < F(1, 20))
    check("reported-serial-type-I-cap", alpha < F(47185, 10**6))
    check("reported-serial-type-II-cap", beta < F(24949, 10**6))
    check("reported-outside-null-cap", outside < F(35477, 10**6))
    return {
        "trials_per_word": N, "total_trials": 5*N,
        "uniform_history_conditional_pair_TV": str(EPSILON),
        "quadratic_split_eta": str(ETA),
        "predictable_score_drift_absolute": str(drift),
        "conditional_variance_increment": str(variance_increment),
        "coordinate_predictable_drift_absolute": str(2*EPSILON),
        "quadratic_remainder_upper_on_gate": str(remainder),
        "rejection_threshold": str(THRESHOLD),
        "null_linear_margin": str(null_margin), "target_linear_margin": str(target_margin),
        "null_Bernstein_exponent": str(null_exponent), "target_Bernstein_exponent": str(target_exponent),
        "null_linear_tail_upper": str(upper(null_linear)), "target_linear_tail_upper": str(upper(target_linear)),
        "quadratic_tail_upper": str(upper(quadratic)),
        "inside_null_rejection_upper": str(upper(inside)), "outside_null_gate_pass_upper": str(upper(outside)),
        "target_gate_failure_upper": str(upper(gate)),
        "type_I_upper": str(upper(alpha)), "type_II_upper": str(upper(beta)),
        "reported_type_I_cap": "0.047185", "reported_type_II_cap": "0.024949",
        "status": "PASS",
    }


def resource_certificate():
    words = ("L", "LL", "H", "HH", "HL")
    active = N * sum(map(len, words))
    low_ticks = N * sum(word.count("L") for word in words)
    high_ticks = N * sum(word.count("H") for word in words)
    raises = N * sum(word.startswith("H") for word in words)
    internal_falls = N * sum(word.count("HL") for word in words)
    reset_falls = N * sum(word.endswith("H") for word in words)
    check("active-ticks", active == 80_000_000)
    check("balanced-field-exposure", low_ticks == high_ticks == 40_000_000)
    check("field-edge-count", raises == internal_falls + reset_falls == 30_000_000)
    reset_duration = F(24)
    # Independent four-state low-field verification of the reset inputs.
    states = [(s, z) for s in (-1, 1) for z in (-1, 1)]
    pi = [(1 + F(1, 3)*s*z)/4 for s, z in states]
    generator = [[F(0) for _ in states] for _ in states]
    for i, (s, z) in enumerate(states):
        for destination in ((-s, z), (s, -z)):
            generator[i][states.index(destination)] = (1-F(1, 3)*s*z)/2
        generator[i][i] = -sum(generator[i])
    check("nominal-reset-minimum-mass", min(pi) == F(1, 6) and sum(pi) == 1)
    check("nominal-reset-detailed-balance", all(pi[i]*generator[i][j] == pi[j]*generator[j][i]
                                               for i in range(4) for j in range(4)))
    eigenfunctions = [([F(1) for _ in states], F(0)),
                      ([F(s+z) for s, z in states], F(2, 3)),
                      ([F(s-z) for s, z in states], F(4, 3)),
                      ([F(s*z)-F(1, 3) for s, z in states], F(2))]
    for index, (function, rate) in enumerate(eigenfunctions):
        check(f"nominal-reset-eigenfunction-{index}", all(
            sum(generator[i][j]*function[j] for j in range(4)) == -rate*function[i]
            for i in range(4)))
    check("nominal-reset-complete-orthogonal-eigenbasis", all(
        sum(pi[k]*f[k]*f[k] for k in range(4)) > 0 for f, _ in eigenfunctions)
        and all(sum(pi[k]*eigenfunctions[i][0][k]*eigenfunctions[j][0][k] for k in range(4)) == 0
                for i in range(4) for j in range(i)))
    # Nominal target: gap2/3, pi_min1/6. Squaring avoids sqrt5.
    reset_TV_squared = F(5, 4) * exp_negative_upper(F(4, 3)*reset_duration)
    reset_allowance = F(1, 4*10**6)
    check("target-reset24-below-quarter-ppm", reset_TV_squared < reset_allowance**2)
    check("target-reset-square-root-prefactor-below-two", F(5, 4) < F(4))
    check("target-reset-exp16-degree32-comparison", positive_exp_sum(F(16), degree=32) > 8_000_000)
    reset_ticks = 5*N * reset_duration
    check("reset-plus-active-exposure", reset_ticks + active == 1_280_000_000)
    check("example-quarter-ppm-budget", 4*reset_allowance == EPSILON)
    return {
        "deterministic_cycle": list(words), "cycles": N,
        "reset_intervals": 5*N, "endpoint_windows": 10*N,
        "active_ticks": active, "low_active_ticks": low_ticks, "high_active_ticks": high_ticks,
        "L_to_H_edges": raises, "H_to_L_edges": internal_falls+reset_falls,
        "internal_HL_falls": internal_falls, "post_H_or_HH_returns_to_reset": reset_falls,
        "LL_or_HH_internal_seams_without_field_change": 2*N,
        "initial_windows_at_low_field": 5*N,
        "final_windows_at_low_field": 3*N, "final_windows_at_high_field": 2*N,
        "optional_protection_edges_if_each_window_engages_and_releases": 20*N,
        "target_reset_duration_in_attempt_units": str(reset_duration),
        "target_reset_TV_allowance": str(reset_allowance),
        "target_reset_squared_TV_upper": str(upper(reset_TV_squared, 10**30)),
        "reset_attempt_units": int(reset_ticks), "reset_plus_active_attempt_units": int(reset_ticks+active),
        "serial_time_seconds": "1280000000/Gamma + 50000000*(T_initial+T_final) + 30000000*(T_up+T_down) + other_nonoverlapping_overhead",
        "time_convention": "Gamma is the common target attempt frequency per second; endpoint-window and field-edge durations are seconds. All listed stages are nonoverlapping. No extra field edge is charged at an LL/HH clock seam.",
        "example_conditional_TV_allocation": {
            "preparation": str(reset_allowance), "initial_joint_instrument": str(reset_allowance),
            "all_active_control_operations_combined": str(reset_allowance), "final_registration": str(reset_allowance),
        },
        "reset_scope": "The 24-unit wait establishes only the nominal four-state target preparation bound. It is not a uniform reset theorem for uncapped rivals and does not certify the other conditional instrument/control allowances.",
        "resource_exclusions": "Calibration samples, analog sample count, bandwidth, energy, device construction, controller reset and unspecified switching/protection dead time are not priced. If an overhead lies inside a named measurement window, charge it there only once.",
        "status": "PASS",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("Output must not overwrite this source")
    inherited, sources, proofs, reports = provenance()
    ranges = inherited_constants(inherited)
    risks = serial_risks()
    resources = resource_certificate()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()}, "dependencies": "Python standard library only",
        "arithmetic": "Exact Fraction decisions; positive exponential Taylor sums provide rational tail upper bounds. No simulated data, optimization or floating-point proof decisions.",
        "inherited_range_certificate": ranges, "serial_sampling_certificate": risks, "resource_certificate": resources,
        "sampling_contract": "One fixed reference ideal five-arm family per null or target; at every trial, conditional on the full pre-reset history, the actual complete recorded pair law is within1ppm TV of that same reference arm law. The filtration may contain the entering hidden state, but not the current post-reset state. The deterministic cycle has exactly10million trials per word. No independence of complete trials is assumed.",
        "test_contract": "The polynomial, fixed initial-mean controls, empirical gate and rejection threshold remain exactly those of the inherited profiled-score test. The prior ideal necessary pair-count obstruction also constrains tests required to cover this larger serial class, by its ideal iid subclass; no new KL identity for arbitrary dependent processes or physical-time lower bound is asserted here.",
        "proof_scope": "The written conditional-martingale, vector-MGF, drift and joint-instrument proofs establish the universal statements; this finite verifier checks their numerical premises and frozen provenance. It does not prove physical feasibility or validate an apparatus's uniform conditional guarantees.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact serial-acquisition checks -> {args.output}")


if __name__ == "__main__":
    main()
