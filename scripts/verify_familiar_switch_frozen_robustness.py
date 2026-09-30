#!/usr/bin/env python3
"""Exact common-parameter and residual-error budgets for the two-switch test.

The four common parameters vary independently by one percent. A positive
series certificate preserves their shared response structure, rather than
replacing different target words by independent parameter intervals.
The population family uses the same actual relative Gibbs tilt for target
and rivals. It does not transfer a nominal score's power uniformly to this
box or assert an unknown-tilt profiled certificate for the entire box.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_frozen_bound.json"
INPUT_SHA256 = "9b15c6c9eacf0e19d53e8413442cc8d568aa8e3411eadc552d0547fc01c0d5a8"
PROOF = "docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md"
PROOF_SHA256 = "d8df8dd7b1ce248ff8bdbcd5d1d95f8ef371250c47a8eef4fc8f85f4184097b3"
GENERAL_PROOF = "docs/FAMILIAR_SWITCH_STRUCTURE.md"
ORDER = 40
TLO, THI = F(33, 100), F(101, 300)
MLO, MHI = F(77, 100), F(707, 900)
ALO, AHI = F(99, 100), F(101, 100)
DELTA = F(1, 20_000)
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def exp_interval(x):
    lower = sum((x ** k / factorial(k) for k in range(ORDER + 1)), F(0))
    ratio = x / (ORDER + 2)
    check(f"exponential-tail-ratio:x={x}", 0 <= ratio < 1)
    tail = x ** (ORDER + 1) / factorial(ORDER + 1) / (1 - ratio)
    return lower, lower + tail


def hyperbolic_interval(q, duration, odd):
    """cosh(t*sqrt(q)), or sinh(t*sqrt(q))/sqrt(q), with no radicals."""
    check("hyperbolic-positive-domain", q >= 0 and duration >= 0 and odd in (0, 1))
    terms = [q ** k * duration ** (2 * k + odd) / factorial(2 * k + odd)
             for k in range(ORDER + 1)]
    lower = sum(terms, F(0))
    first = terms[-1] * q * duration ** 2 / ((2 * ORDER + odd + 1) * (2 * ORDER + odd + 2))
    ratio = q * duration ** 2 / ((2 * ORDER + odd + 3) * (2 * ORDER + odd + 4))
    check("hyperbolic-tail-ratio", 0 <= ratio < 1)
    return lower, lower + first / (1 - ratio)


def coupling_coefficient(t, m):
    return t * (1 - m * m) / (1 - t * t * m * m)


def response_box(mlo, mhi):
    # B increases with t and decreases with nonnegative m.
    blo, bhi = coupling_coefficient(TLO, mhi), coupling_coefficient(THI, mlo)
    qlo, qhi = TLO * blo, THI * bhi
    exp_lo, exp_hi = 1 / exp_interval(AHI)[1], 1 / exp_interval(ALO)[0]
    flow = exp_lo * hyperbolic_interval(qlo, ALO, 1)[0]
    fhigh = exp_hi * hyperbolic_interval(qhi, AHI, 1)[1]
    elow = exp_lo * hyperbolic_interval(qlo, ALO, 0)[0]
    ehigh = exp_hi * hyperbolic_interval(qhi, AHI, 0)[1]
    return (blo * flow, bhi * fhigh), (elow + qlo * flow, ehigh + qhi * fhigh)


def sqrt_interval(x):
    check("square-root-domain", x >= 0)
    scale = 10 ** 30
    k = isqrt(x.numerator * scale * scale // x.denominator)
    lower, upper = F(k, scale), F(k + 1, scale)
    check("integer-square-root-enclosure", lower * lower <= x <= upper * upper)
    return lower, upper


def rounded_interval(interval, scale=10 ** 12):
    lo, hi = interval
    return [str(F((lo * scale).__floor__(), scale)),
            str(F((hi * scale).__ceil__(), scale))]


def rounded_lower(x, scale=10 ** 12):
    return str(F((x * scale).__floor__(), scale))


def rounded_upper(x, scale=10 ** 12):
    return str(F((x * scale).__ceil__(), scale))


def common_parameter_box():
    start = len(CHECKS)
    check("one-percent-parameter-domain", 0 < TLO < THI < 1 and 0 <= MLO < MHI < 1
          and TLO == F(1, 3) * F(99, 100) and THI == F(1, 3) * F(101, 100)
          and MLO == F(7, 9) * F(99, 100) and MHI == F(7, 9) * F(101, 100))
    cl, bl = response_box(F(0), F(0))
    ch, bh = response_box(MLO, MHI)
    check("high-field-minus-conditional-moment-positive", MLO - (1 + MLO) * bh[1] > 0)
    check("response-coefficient-range", 0 < bl[0] <= bl[1] < 1 and 0 < bh[0] <= bh[1] < 1
          and 0 < cl[0] <= cl[1] and 0 < ch[0] <= ch[1])
    zl = bl[1] / 2
    zp = (MHI + (1 - MHI) * bh[1]) / 2
    zm = (MHI - (1 + MHI) * bh[0]) / 2
    d, p = DELTA, F(1, 2) - DELTA
    wp, wm = 1 + MHI, 1 - MLO
    # Changes caused by TV perturbations of observed pair laws. Common
    # target-parameter variation is already inside cl,ch,bl,bh and gamma.
    el = 2 * d + 2 * d / p * (4 * zl + 2 * zl * zl + 4 * d)
    eh = 2 * (1 + MHI) * d + d / p * (
        wp * (4 * zp + 2 * zp * zp + 4 * d) + wm * (4 * zm + 2 * zm * zm + 4 * d))
    ea = d / p * (wp * (2 * (zp + zl + zp * zl) + 4 * d)
                  + wm * (2 * (zm + zl + zm * zl) + 4 * d))
    ew = 2 * (1 + MHI) * d
    gamma = 1 - THI * THI
    vl, vh, residual = gamma * cl[0] ** 2, gamma * ch[0] ** 2, gamma * cl[0] * ch[0]
    check("variance-errors-smaller-than-target-variances", eh < vh and el < vl)
    positive_factor = sqrt_interval((1 + MLO) * (1 - eh / vh) * (1 - el / vl))[0] - 1
    negative_sector_factor = 1 - sqrt_interval((1 - MLO) * (1 + eh / vh) * (1 + el / vl))[1]
    check("normalized-branch-factors-positive", positive_factor > 0 and negative_sector_factor > 0)
    gaps = (residual * positive_factor - ea - ew,
            residual * negative_sector_factor - ea - ew,
            residual - ea - ew)
    check("plus-sector-positive-orientation-excluded", gaps[0] > F(228, 10 ** 6))
    check("minus-sector-positive-orientation-excluded", gaps[1] > F(1946, 10 ** 6))
    check("both-negative-orientations-excluded", gaps[2] > 0)
    # The two-state passive Markov defect is gamma*c_L^2/4. Propagate
    # independent cell errors <=d and common initial-marginal error <=d.
    two_state_error = d + d / p * (1 + (1 + bl[1] ** 2) / 4 + 2 * d)
    two_state_gap = vl / 4 - two_state_error
    check("general-two-state-exclusion", two_state_gap > F(3071, 10 ** 6))
    return {"status": "PASS", "exact_checks": len(CHECKS) - start,
            "box": {"t": [str(TLO), str(THI)], "m_H": [str(MLO), str(MHI)],
                    "tau_L": [str(ALO), str(AHI)], "tau_H": [str(ALO), str(AHI)]},
            "fixed_conditions": "Low physical field zero; equal unit attempt rates; common coupling; one reused clock at each field; target and rival share the actual relative Gibbs tilt m",
            "per_word_TV_tolerance": str(DELTA), "general_state_minimum": 3,
            "ordinary_state_minimum": 4,
            "general_upper": "Inherited positive three-state construction, FAMILIAR_SWITCH_STRUCTURE.md Section 3 (G1)-(G7), valid for every 0<t<1 and nonnegative field",
            "ordinary_upper": "The physical four-state heat-bath process",
            "response_intervals": {"c_L": rounded_interval(cl), "b_L": rounded_interval(bl),
                                   "c_H": rounded_interval(ch), "b_H": rounded_interval(bh)},
            "data_perturbation_upper_bounds": {"V_L": rounded_upper(el), "V_H": rounded_upper(eh),
                                              "conditional_mean_part": rounded_upper(ea), "W_HL": rounded_upper(ew)},
            "target_residual_lower": rounded_lower(residual),
            "ordinary_branch_gap_lower": {"plus_sector_positive_orientation": rounded_lower(gaps[0]),
                                           "minus_sector_positive_orientation": rounded_lower(gaps[1]),
                                           "negative_orientations": rounded_lower(gaps[2])},
            "general_two_state_gap_lower": rounded_lower(two_state_gap),
            "method": "Positive scalar series, exact rational tail and radical enclosures, and retained shared identities V_j=gamma*c_j^2 and R=gamma*c_L*c_H; no grid, optimizer or simulation",
            "scope_limits": "Population family result with the same actual m on both sides. No uniform nominal-score power or whole-box unknown-m profiling is certified. No moderate low-field offset or unequal-attempt box is included."}


def reset_certificate():
    start = len(CHECKS)
    # TV^2 <= (5/4)*exp(-28) at nominal reset time 21.
    exp28_lower = sum((F(28) ** k / factorial(k) for k in range(65)), F(0))
    check("nominal-reset-21-below-one-ppm", exp28_lower > F(5, 4) * 10 ** 12)
    # In the common t box: gap>=199/300, pi_min>=199/1200.
    exponent = 2 * (1 - THI) * 22
    exp_box_lower = sum((exponent ** k / factorial(k) for k in range(65)), F(0))
    prefactor_squared = F(1, 4) * (F(4) / (1 - THI) - 1)
    check("common-box-reset-22-below-one-ppm", exp_box_lower > prefactor_squared * 10 ** 12)
    return {"status": "PASS", "exact_checks": len(CHECKS) - start,
            "nominal": {"spectral_gap": "2/3", "minimum_equilibrium_mass": "1/6", "reset_duration": 21,
                        "TV_strict_upper": "1/1000000", "bound": "sqrt(5)/2 * exp(-2*T/3)"},
            "common_box": {"spectral_gap_lower": "199/300", "minimum_equilibrium_mass_lower": "199/1200",
                           "reset_duration": 22, "TV_strict_upper": "1/1000000"},
            "scope": "The stated physical heat-bath targets, from every initial hidden law; not a rate-independent reset guarantee for arbitrary null rivals"}


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def physical_and_detector_budget():
    start = len(CHECKS)
    rate_cap = F(5, 3)
    high_max_exit = (1 + (MHI + THI) / (1 + MHI * THI)) / 2 + (1 + THI) / 2
    check("reference-common-box-exit-cap", high_max_exit < rate_cap and 1 + THI < rate_cap)
    eps_p = F(1, 10 ** 6)
    eps = F(1, 2 * 10 ** 6)
    row_rate_difference = rate_cap * eps + (1 + eps) * (eps + eps / 2)
    target_displacement = eps_p + (eps + eps) / 2 + (2 * AHI + 2 * eps) * row_rate_difference + 2 * rate_cap * eps
    rival_preparation = eps_p
    physical_total = target_displacement + rival_preparation
    check("joint-physical-budget", physical_total < F(7366, 10 ** 9))
    error = F(1, 100)
    contrast = 1 - 2 * error
    channel = [[1 - error, error], [error, 1 - error]]
    inverse = [[(1 - error) / contrast, -error / contrast],
               [-error / contrast, (1 - error) / contrast]]
    check("known-BSC-inverse", matmul(channel, inverse) == [[1, 0], [0, 1]])
    one_norm = max(sum(abs(inverse[i][j]) for i in range(2)) for j in range(2))
    inverse_norm = one_norm * one_norm
    check("two-endpoint-inverse-norm", inverse_norm == F(2500, 2401))
    # Quarter-ppm uncertainty in each endpoint flip probability, on each
    # side of a target/rival comparison. This is distinct from 1% flip noise.
    calibration_error = F(1, 4 * 10 ** 6)
    detector_total = inverse_norm * 4 * calibration_error
    joint = physical_total + detector_total
    check("detector-calibration-budget", detector_total < F(1042, 10 ** 9))
    check("combined-budget-below-ten-ppm", joint < F(8408, 10 ** 9) < F(1, 100_000))
    return {"status": "PASS", "exact_checks": len(CHECKS) - start,
            "reference_exit_cap": str(rate_cap),
            "residual_allowances": {"target_preparation_TV": str(eps_p), "rival_preparation_TV": str(eps_p),
                                    "coupling_J": str(eps), "each_field_h": str(eps),
                                    "each_attempt_rate": str(eps), "each_tick_duration": str(eps)},
            "row_offdiagonal_rate_difference_upper": str(row_rate_difference),
            "target_law_displacement_upper": str(target_displacement),
            "physical_total_strict_upper": "7366/1000000000",
            "BSC_registered_flip_probabilities": [str(error), str(error)],
            "BSC_inverse_l1_norm": str(inverse_norm),
            "each_endpoint_calibration_uncertainty": str(calibration_error),
            "detector_calibration_total_upper": str(detector_total),
            "combined_systematic_strict_upper": "8408/1000000000",
            "coarse_joint_systematic_budget": "1/100000",
            "scope": "A conservative target-law displacement plus separately assumed rival preparation allowance and calibrated-channel comparison using independent BSC errors at the two endpoints. Common parameter uncertainty inside the box is not charged again.",
            "limitations": "No hardware calibration feasibility or universal arbitrary-rate rival drift bound. Shared-kernel and Gibbs-interface validity remain assumptions. Noninvasive readout is assumed; a joint initial-record/poststate disturbance allowance, if needed, adds separately. Known detector inversion also amplifies statistical errors; nominal ideal-detector sample counts do not transfer unchanged."}


def provenance():
    payload = (ROOT / INPUT).read_bytes()
    check("input-report-hash", hashlib.sha256(payload).hexdigest() == INPUT_SHA256)
    inherited = json.loads(payload)
    check("input-report-PASS", inherited["status"] == "PASS")
    sources = dict(inherited["source_sha256"])
    proofs = dict(inherited["proof_snapshot_sha256"])
    reports = dict(inherited["input_report_sha256"])
    reports[INPUT] = INPUT_SHA256
    for name, digest in sources.items():
        check("source-hash:" + name, hashlib.sha256((ROOT / "scripts" / name).read_bytes()).hexdigest() == digest)
    for name, digest in {**proofs, **reports}.items():
        check("inherited-hash:" + name, hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
    check("general-construction-proof-is-bound", GENERAL_PROOF in proofs)
    check("new-proof-hash", hashlib.sha256((ROOT / PROOF).read_bytes()).hexdigest() == PROOF_SHA256)
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    proofs[PROOF] = PROOF_SHA256
    return sources, proofs, reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("Output must not overwrite the source")
    sources, proofs, reports = provenance()
    family, reset, budget = common_parameter_box(), reset_certificate(), physical_and_detector_budget()
    report = {"status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
              "versions": {"python": platform.python_version()},
              "arithmetic": "Exact rational arithmetic, positive scalar series and geometric remainder bounds, integer-square-root enclosures; no grid, optimizer, Monte Carlo or floating-point acceptance",
              "common_parameter_family": family, "target_reset": reset,
              "residual_and_detector_budget": budget,
              "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
              "limitations": "Conditional mathematical tolerances. Population family, nominal statistical power, target drift, null-interface validity, and instrument calibration are distinct. No device feasibility or complete-path prediction claim."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} frozen-measurement robustness checks -> {args.output}")


if __name__ == "__main__":
    main()
