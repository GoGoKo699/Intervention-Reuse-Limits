#!/usr/bin/env python3
"""Exact same-seven-word preparation-free information and precision bounds.

A numerical discovery supplied this fixed rational positive reversible
three-state CTMC and seven word-specific preparations. Acceptance uses
only rational matrix-Taylor, logarithm and square-root enclosures. No
optimizer, matrix logarithm, floating-point decision or simulation runs.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import platform

import verify_familiar_switch_frozen_information as base

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_switch_preparation_free_unknown_tilt.json":
        "2facaf21db92bee7cd575eea74d3935f47c8871e6bb78476ab78ab53b12852f0",
    "reports/familiar_switch_preparation_free_unknown_sampling.json":
        "2403a567228859606e3f4655136db4e5ab848ee0f0acec551aa211f9f8e994ea",
    "reports/familiar_switch_frozen_information.json":
        "d7edb41457f765c38f71e431219078782c53413a8ca1ceeb02c0ab9862344651",
}
HELPER_SHA256 = "f3bb879fe189bc305ccfb81b96523aeb36fee44c8727a3ad8bbcf8efce7239f2"
PROOFS = {
    "docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md":
        "dd0ac52d3effebcdeec448944aaedf7fe83797faab53cc28652685e857349542",
    "docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION_SOURCE_AUDIT.md":
        "6bae5bee401d76acf2ae71b40724adddb9a308e93a7e243a223a0025e96eb583",
}
WORDS = ((0,), (0, 0), (1,), (0, 1), (1, 0), (0, 0, 1), (1, 0, 0))
NAMES = ("L", "LL", "H", "LH", "HL", "LLH", "HLL")
EDGES = ((0, 1), (0, 2), (1, 2))
SIGNS = (F(-1), F(-1), F(1))
TARGET_FIELDS = (F(0), F(7, 9))
KL_CAP = F(3023, 10**11)
AFFINITY_DEFECT_CAP = F(7557, 10**12)
TV_CAP = F(86, 10**6)
SQRT_SCALE = 10**30
CHECKS = []
RHO = tuple(map(F, ['0.175214276960', '0.314270428762', '0.510515294278']))
HIGH_TILT = F('0.768614727605')
CONDUCTANCES = tuple(tuple(map(F, row)) for row in [['0.050001659214', '0.048179657002', '0.174117179604'], ['0.004181195769', '0.024465448649', '0.068650610652']])
MIXTURES = tuple(map(F, ['0.459060621761', '0.525924604907', '0.339345722840', '0.376868373461', '0.487056483351', '0.420209032611', '0.569073491856']))


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def provenance():
    check("two-reviewed-new-proof-snapshots-pinned", set(PROOFS) == {
        "docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md",
        "docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION_SOURCE_AUDIT.md",
    } and all(isinstance(digest, str) and len(digest) == 64
              and all(character in "0123456789abcdef" for character in digest)
              for digest in PROOFS.values()))
    sources, proofs, reports, inherited_reports = {}, {}, {}, {}
    for path, expected in INPUTS.items():
        payload = (ROOT / path).read_bytes()
        check("input-report-hash:" + path, hashlib.sha256(payload).hexdigest() == expected)
        report = json.loads(payload)
        check("input-report-pass:" + path, report["status"] == "PASS")
        inherited_reports[path] = report
        reports[path] = expected
        for key, destination in (("source_sha256", sources), ("proof_snapshot_sha256", proofs),
                                 ("input_report_sha256", reports)):
            for name, digest in report.get(key, {}).items():
                check("ancestry-consistent:" + name, name not in destination or destination[name] == digest)
                destination[name] = digest
    for name, digest in sources.items():
        check("inherited-source:" + name,
              hashlib.sha256((ROOT / "scripts" / name).read_bytes()).hexdigest() == digest)
    for name, digest in {**proofs, **reports}.items():
        check("inherited-file:" + name, hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
    check("frozen-interval-helper-bound", sources.get(Path(base.__file__).name) == HELPER_SHA256)
    check("actual-interval-helper-hash", hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest() == HELPER_SHA256)
    for name, digest in PROOFS.items():
        check("new-proof:" + name, hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
        proofs[name] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports, inherited_reports


def outward(box, denominator=10**22):
    return [str(base.lower_round(box[0], denominator)), str(base.upper_round(box[1], denominator))]


def generator(stationary, conductances):
    result = [[F(0)] * 3 for _ in range(3)]
    for conductance, (i, j) in zip(conductances, EDGES):
        result[i][j] = conductance / stationary[i]
        result[j][i] = conductance / stationary[j]
    for i in range(3):
        result[i][i] = -sum(result[i])
    return result


def model_certificate():
    check("low-stationary-law-positive-normalized", min(RHO) > 0 and sum(RHO) == 1)
    check("fixed-singleton-sign-is-positive", SIGNS == (F(-1), F(-1), F(1)))
    check("unknown-tilt-admissible", -1 < HIGH_TILT < 1)
    normalizer = 1 + HIGH_TILT * sum(p * s for p, s in zip(RHO, SIGNS))
    high = tuple(p * (1 + HIGH_TILT * s) / normalizer for p, s in zip(RHO, SIGNS))
    check("high-Gibbs-law-positive-normalized", normalizer > 0 and min(high) > 0 and sum(high) == 1)
    laws = (RHO, high)
    generators = tuple(generator(pi, conductances) for pi, conductances in zip(laws, CONDUCTANCES))
    for field, (pi, q) in enumerate(zip(laws, generators)):
        check(f"field-{field}:conductances-strictly-positive", min(CONDUCTANCES[field]) > 0)
        check(f"field-{field}:generator-row-sums", all(sum(row) == 0 for row in q))
        check(f"field-{field}:positive-off-diagonal-rates",
              all(q[i][j] > 0 for i in range(3) for j in range(3) if i != j))
        check(f"field-{field}:detailed-balance",
              all(pi[i] * q[i][j] == pi[j] * q[j][i] for i in range(3) for j in range(3)))
        check(f"field-{field}:stationarity", all(sum(pi[i] * q[i][j] for i in range(3)) == 0 for j in range(3)))
    preparations = []
    for name, mixture in zip(NAMES, MIXTURES):
        prep = (mixture / 2, (1 - mixture) / 2, F(1, 2))
        check(name + ":positive-balanced-word-preparation",
              0 < mixture < 1 and min(prep) > 0 and sum(prep) == 1
              and sum(p * s for p, s in zip(prep, SIGNS)) == 0)
        preparations.append(prep)
    return generators, preparations, {
        "status": "PASS", "signs": list(map(str, SIGNS)), "singleton_state_index": 2,
        "stationary_low": list(map(str, RHO)), "stationary_high": list(map(str, high)),
        "unknown_high_tilt": str(HIGH_TILT), "Gibbs_normalizer": str(normalizer),
        "edge_order": [list(edge) for edge in EDGES],
        "conductances": [[str(value) for value in row] for row in CONDUCTANCES],
        "generators": [[[str(value) for value in row] for row in q] for q in generators],
        "word_specific_preparations": {name: list(map(str, prep)) for name, prep in zip(NAMES, preparations)},
        "doubleton_first_state_mixtures": dict(zip(NAMES, map(str, MIXTURES))),
        "preparation_scope": "The scheduled word determines a fixed preparation law before the current initial sign is observed. All arms have exactly balanced initial signs. These preparations need not be stationary or common across words; both freedoms are permitted by the registered preparation-free null.",
    }


def interval_difference(a, b):
    return a[0] - b[1], a[1] - b[0]


def absolute_interval(value):
    lower, upper = value
    return (F(0) if lower <= 0 <= upper else min(abs(lower), abs(upper)),
            max(abs(lower), abs(upper)))


def tv_interval(p, q):
    differences = [absolute_interval(interval_difference(a, b)) for a, b in zip(p, q)]
    return sum(lo for lo, hi in differences) / 2, sum(hi for lo, hi in differences) / 2


def sqrt_interval(value):
    lower, upper = value
    check("positive-square-root-argument", 0 <= lower <= upper)
    floor_low = isqrt(lower.numerator * SQRT_SCALE**2 // lower.denominator)
    floor_high = isqrt(upper.numerator * SQRT_SCALE**2 // upper.denominator)
    result = F(floor_low, SQRT_SCALE), F(floor_high + 1, SQRT_SCALE)
    check("exact-integer-square-root-enclosure", result[0]**2 <= lower <= upper <= result[1]**2)
    return result


def affinity_interval(p, q):
    roots = [sqrt_interval((pl * ql, pu * qu)) for (pl, pu), (ql, qu) in zip(p, q)]
    affinity = sum(lo for lo, hi in roots), sum(hi for lo, hi in roots)
    defect = max(F(0), 1 - affinity[1]), 1 - affinity[0]
    check("positive-affinity-defect-enclosure", 0 < defect[0] <= defect[1] < 1)
    return affinity, defect


def local_realization_certificate(kernels, epsilon):
    """Certify the strict scalar regularity condition of the local lemma."""
    low, high = kernels
    v_gap = (low[1][2] - low[0][2] - 2 * epsilon,
             low[1][2] - low[0][2] + 2 * epsilon)
    w1, w2 = RHO[2] / RHO[0], RHO[2] / RHO[1]
    cross_center = w1 * high[2][0] - w2 * high[2][1]
    cross = (cross_center - (w1 + w2) * epsilon,
             cross_center + (w1 + w2) * epsilon)
    jacobian_factor = base.interval_product(v_gap, cross)
    check("local-realization-low-return-coordinates-distinct", v_gap[0] > F(11, 100))
    check("local-realization-J-nonzero-certified",
          -F(217, 100000) < jacobian_factor[0] <= jacobian_factor[1] < -F(216, 100000))
    check("local-realization-positive-tick-kernel-entries",
          all(value - epsilon > 0 for kernel in kernels for row in kernel for value in row))
    return {
        "status": "PASS", "singleton_index": 2,
        "low_return_coordinate_difference_interval": outward(v_gap),
        "J_definition": "(K_L[1,2]-K_L[0,2])*((rho[2]/rho[0])*K_H[2,0]-(rho[2]/rho[1])*K_H[2,1])",
        "J_interval": outward(jacobian_factor),
        "J_simple_strict_bounds": ["-217/100000", "-216/100000"],
        "scope": "A regular interior point for the written local realization lemma; generator positivity, tick positivity and opposite-sector response brackets are also verified. These checks do not establish global completeness of the determinant or a globally nearest rival.",
    }


def pair_certificate(generators, preparations, core_report):
    helper_start = len(base.CHECKS)
    target_q = [base.physical_generator(field) for field in TARGET_FIELDS]
    check("registered-seven-word-menu", list(NAMES) == core_report["word_order"] and max(map(len, WORDS)) == 3)
    check("four-target-and-three-rival-states", len(target_q[0]) == 4 and len(generators[0]) == 3)
    check("generator-infinity-norm-at-most-four",
          all(base.norm_inf(q) <= 4 for q in target_q + list(generators)))
    check("frozen-matrix-Taylor-order64", base.ORDER == 64)
    exp4_partial = sum((F(4)**k / factorial(k) for k in range(33)), F(0))
    exp4_upper = exp4_partial + F(4)**33 / factorial(33) / (1 - F(4, 34))
    check("exp4-below64", exp4_upper < 64)
    epsilon = F(64 * 4**65, factorial(65))
    error = 4 * epsilon
    check("three-stochastic-factor-product-error",
          3 * epsilon + 3 * epsilon**2 + epsilon**3 < error)
    check("pair-Taylor-error-below1e-45", error < F(1, 10**45))
    target_k = [base.exp_taylor(q) for q in target_q]
    rival_k = [base.exp_taylor(q) for q in generators]
    local_realization = local_realization_certificate(rival_k, epsilon)
    reference_returns = core_report["target_certificate"]["conditional_return_enclosures"]
    fixtures, kl_uppers, defect_uppers, tv_uppers = [], [], [], []
    opposite_errors = []
    for index, (name, word, prep) in enumerate(zip(NAMES, WORDS, preparations)):
        target, rival = base.eye(4), base.eye(3)
        for field in word:
            target = base.matmul(target, target_k[field])
            rival = base.matmul(rival, rival_k[field])
        p = base.pair_intervals(target, base.TARGET_RHO, base.TARGET_S, error)
        q = base.pair_intervals(rival, prep, SIGNS, error)
        for sign, diagonal in ((1, 0), (-1, 3)):
            old_lo, old_hi = map(F, reference_returns[str(sign)][index])
            check(f"{name}:independent-target-return-enclosure-{sign}",
                  old_lo <= 2 * p[diagonal][0] <= 2 * p[diagonal][1] <= old_hi)
        kl = base.kl_interval(p, q)
        affinity, defect = affinity_interval(p, q)
        tv = tv_interval(p, q)
        check(name + ":positive-narrow-KL", 0 < kl[0] <= kl[1] and kl[1] - kl[0] < F(1, 10**19))
        check(name + ":KL-below-simple-cap", kl[1] < KL_CAP)
        check(name + ":affinity-defect-below-simple-cap", defect[1] < AFFINITY_DEFECT_CAP)
        check(name + ":TV-below86ppm", tv[1] < TV_CAP)
        # The opposite sector's rounded preparation approximately matches
        # its conditional return. Its small residual is retained in every
        # full-table information and TV calculation; it is not set to zero.
        opposite_error = absolute_interval((2 * (p[3][0] - q[3][1]), 2 * (p[3][1] - q[3][0])))
        check(name + ":rounded-doubleton-row-error-below1e-10", opposite_error[1] < F(1, 10**10))
        # Bracketing shows the exact target doubleton return is interior to
        # the rival's response segment, independently of rounded mixtures.
        endpoints = [(1 - rival[row][2] - error, 1 - rival[row][2] + error) for row in (0, 1)]
        target_return = (2 * p[3][0], 2 * p[3][1])
        check(name + ":strict-opposite-sector-response-bracket",
              (endpoints[0][1] < target_return[0] and target_return[1] < endpoints[1][0])
              or (endpoints[1][1] < target_return[0] and target_return[1] < endpoints[0][0]))
        kl_uppers.append(kl[1]); defect_uppers.append(defect[1]); tv_uppers.append(tv[1]); opposite_errors.append(opposite_error[1])
        fixtures.append({
            "word": name, "target_pair_law": [outward(value) for value in p],
            "rival_pair_law": [outward(value) for value in q],
            "KL_target_to_rival_interval": outward(kl),
            "Hellinger_affinity_interval": outward(affinity),
            "one_minus_affinity_interval": outward(defect), "TV_interval": outward(tv),
            "rounded_doubleton_conditional_return_absolute_error_interval": outward(opposite_error),
            "doubleton_endpoint_return_intervals": [outward(value) for value in endpoints],
        })
    CHECKS.extend("interval-helper:" + label for label in base.CHECKS[helper_start:])
    return {
        "status": "PASS", "pair_outcome_order": ["++", "+-", "-+", "--"],
        "Taylor_order": base.ORDER, "one_tick_matrix_error_upper": str(epsilon),
        "three_tick_pair_error_upper": str(error), "square_root_grid_denominator": str(SQRT_SCALE),
        "fixtures": fixtures, "maximum_arm_KL_upper": str(base.upper_round(max(kl_uppers))),
        "simple_maximum_arm_KL_cap": str(KL_CAP),
        "maximum_arm_affinity_defect_upper": str(base.upper_round(max(defect_uppers))),
        "simple_maximum_arm_affinity_defect_cap": str(AFFINITY_DEFECT_CAP),
        "maximum_arm_TV_upper": str(base.upper_round(max(tv_uppers))), "simple_maximum_arm_TV_cap": str(TV_CAP),
        "maximum_rounded_doubleton_return_error_upper": str(base.upper_round(max(opposite_errors))),
        "local_realization_certificate": local_realization,
        "doubleton_matching_scope": "All seven target opposite-sector returns are strictly inside the rival endpoint response intervals. The listed rational preparation mixtures are rounded, so their residual errors are certified and retained rather than claimed to vanish exactly.",
    }, kl_uppers, defect_uppers


def information_certificate(kl_uppers, defect_uppers, sampling_report):
    helper_start = len(base.CHECKS)
    log2 = base.log_interval(F(2), terms=48)
    log19over16 = base.log_interval(F(19, 16), terms=24)
    log25over19 = base.log_interval(F(25, 19), terms=24)
    kappa = tuple(F(9, 10) * (log19over16[i] + 4 * log2[i]) for i in (0, 1))
    affinity_threshold = tuple((log25over19[i] + 2 * log2[i]) / 2 for i in (0, 1))
    kappa_lower = base.lower_round(kappa[0], 10**14)
    affinity_lower = base.lower_round(affinity_threshold[0], 10**14)
    check("binary-KL-threshold-lower", kappa_lower == F("2.64999508124979"))
    check("binary-affinity-threshold-lower", affinity_lower == F("0.83036560341082"))
    check("affinity-cut-in-unit-interval", 0 < AFFINITY_DEFECT_CAP < 1)
    # -log(1-h)=h+sum_{k>=2}h^k/k <=h+h^2/[2(1-h)].
    affinity_log_upper = AFFINITY_DEFECT_CAP + AFFINITY_DEFECT_CAP**2 / (2 * (1 - AFFINITY_DEFECT_CAP))
    expected_lower = kappa_lower / KL_CAP
    fixed_ratio = affinity_lower / affinity_log_upper
    fixed_count = fixed_ratio.__ceil__()
    check("fixed-count-ratio-not-integer", fixed_ratio.denominator != 1)
    check("fixed-count-ceiling-certificate", fixed_count - 1 < fixed_ratio < fixed_count)
    upper_count = sampling_report["sampling_certificate"]["total_attempt_cap"]
    check("same-task-existing-sufficient-budget", upper_count == 1_176_000_000)
    check("fixed-acquisition-bracket-within-eleven", upper_count < 11 * fixed_count)
    # Optional tighter bounds retain the exact per-arm enclosures rather
    # than the two simple cuts. They are not optimization statements.
    exact_h = max(defect_uppers)
    exact_log_upper = exact_h + exact_h**2 / (2 * (1 - exact_h))
    sum_log_upper = sum(h + h**2 / (2 * (1 - h)) for h in defect_uppers)
    equal_per_word = (affinity_lower / sum_log_upper).__ceil__()
    CHECKS.extend("interval-helper:" + label for label in base.CHECKS[helper_start:])
    return {
        "status": "PASS", "maximum_type_I_and_type_II": "1/20",
        "binary_KL_threshold_exact": "(9/10)*log(19)", "binary_KL_threshold_interval": outward(kappa, 10**14),
        "binary_affinity_upper_squared": "19/100",
        "negative_log_binary_affinity_threshold_exact": "(1/2)*log(100/19)",
        "negative_log_binary_affinity_threshold_interval": outward(affinity_threshold, 10**14),
        "KL_cap": str(KL_CAP), "affinity_defect_cap": str(AFFINITY_DEFECT_CAP),
        "negative_log_minimum_arm_affinity_upper": str(affinity_log_upper),
        "necessary_expected_total_pairs_strict_lower": str(expected_lower),
        "necessary_expected_total_pairs_lower_rounded_down": str(base.lower_round(expected_lower, 10**6)),
        "necessary_fixed_total_pairs": fixed_count, "necessary_fixed_binary_endpoint_records": 2 * fixed_count,
        "fixed_count_unrounded_ratio": str(fixed_ratio), "existing_sufficient_fixed_total_pairs": upper_count,
        "sufficient_to_necessary_fixed_budget_ratio_upper": str(base.upper_round(F(upper_count, fixed_count), 10**9)),
        "optional_tighter_expected_total_pairs_lower": str(base.lower_round(kappa_lower / max(kl_uppers), 10**6)),
        "optional_tighter_fixed_total_pairs": (affinity_lower / exact_log_upper).__ceil__(),
        "optional_equal_allocation_necessary_pairs_per_word": equal_per_word,
        "optional_equal_allocation_necessary_total_pairs": 7 * equal_per_word,
        "expected_budget_scope": "KL chain rule permits adaptive word choices based on completed trials and finite-expected stopping, with word chosen before its current initial sign. It lower-bounds expected complete pairs under the target for the selected independent reference hypotheses. Integer ceilings of expected counts are not asserted.",
        "fixed_budget_scope": "For a deterministic capN, padded transcript affinity is at least(min_w affinity(P_w,Q_w))^N under adaptive word selection. Testing with both errors<=1/20 makes decision affinity at mostsqrt(19/100). The resulting integer cap bound is separate from the expected-stopping KL bound.",
        "robust_task_scope": "The ideal independent target and this ideal independently prepared comparator are members of the registered five-ppm target/one-ppm registration serial task. A test uniformly valid for that larger task must distinguish these two members. Their simple observation laws therefore give a necessary bound for the robust task, without imposing independent resets on every allowed rival.",
    }


def precision_certificate(core_report, pair_report):
    population = core_report["population_robustness_certificate"]
    conditional_radius = F(population["conditional_return_tolerance"])
    check("inherited-conditional-return-radius", conditional_radius == F(3, 20000))
    joint_lower = conditional_radius / (2 * (1 + conditional_radius))
    check("derived-joint-radius-exact", joint_lower == F(3, 40006))
    check("derived-joint-radius-inverts-conditioning",
          joint_lower / (F(1, 2) - joint_lower) == conditional_radius)
    check("derived-joint-radius-exceeds-frozen70ppm", joint_lower > F(70, 10**6))
    check("actual-rival-TV-below86ppm", F(pair_report["maximum_arm_TV_upper"]) < TV_CAP)
    conditional_at_upper = TV_CAP / (F(1, 2) - TV_CAP)
    check("upper-radius-conditional-conversion", conditional_at_upper == F(43, 249957))
    nominal_gap_lower = F(core_report["state_count_certificate"]["target_two_state_composition_gap_enclosure"][0])
    remaining_gap = nominal_gap_lower - 4 * conditional_at_upper
    check("general-two-state-still-excluded-at86ppm", remaining_gap > F(31, 5000))
    check("precision-bracket-ratio-below1point15", TV_CAP / joint_lower < F(23, 20))
    return {
        "status": "PASS", "comparison_class": "Same seven words, unknown Gibbs tilt, arbitrary word-dependent preparations, deterministic binary readout and at most three counted ordinary reversible states",
        "inherited_conditional_return_exclusion_radius": str(conditional_radius),
        "derived_joint_pair_exclusion_radius": str(joint_lower),
        "ordinary_at_most_three_infimum_error_lower": str(joint_lower),
        "ordinary_at_most_three_infimum_error_strict_upper": str(TV_CAP),
        "upper_to_lower_precision_radius_ratio": str(TV_CAP / joint_lower),
        "derivation": "The inherited conditional-return exclusion through150ppm and the balanced-target conditioning bounddelta/(1/2-delta) imply joint exclusion through3/40006. This refines the earlier rounded70ppm statement without altering its frozen certificate.",
        "infimum_scope": "Exclusion of the closed lower-radius ball gives infimum error>=3/40006. A specific rival has error strictly below86ppm. No claim that either endpoint equals the optimal approximation error is made.",
        "general_two_state_remaining_gap_at_upper_radius_lower": str(base.lower_round(remaining_gap)),
        "state_counts_through_lower_radius": {"general": 3, "ordinary_reversible": 4},
        "state_counts_at86ppm": {"general": 3, "ordinary_reversible": 3},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("Output must not overwrite this source")
    sources, proofs, reports, inherited = provenance()
    core_report = inherited["reports/familiar_switch_preparation_free_unknown_tilt.json"]
    sampling_report = inherited["reports/familiar_switch_preparation_free_unknown_sampling.json"]
    generators, preparations, model = model_certificate()
    pair_report, kl_uppers, defect_uppers = pair_certificate(generators, preparations, core_report)
    information = information_certificate(kl_uppers, defect_uppers, sampling_report)
    precision = precision_certificate(core_report, pair_report)
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()}, "dependencies": "Python standard library only",
        "arithmetic": "Exact rational positive CTMC/Gibbs/preparation checks, order64 matrix-Taylor enclosures through three factors, rational logarithm bounds and direct integer-square-root Hellinger affinities. No floating-point decisions, fits, simulations or numerical matrix logarithms.",
        "word_order": list(NAMES), "model_certificate": model, "pair_law_certificate": pair_report,
        "information_certificate": information, "precision_certificate": precision,
        "discovery_and_validation": "A small deterministic numerical fit found an interior reversible tick-kernel candidate. Its numerical principal logarithms suggested positive conductances. Twelve-decimal rational stationary weights, tilt, conductances and word mixtures are frozen here; positivity and all observation/information claims are verified afresh without an optimizer. No global nearest-rival or optimality claim is made.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
        "limitations": "Necessary acquisition bounds apply to complete endpoint pairs from exactly these seven words, with word choice before the current initial sign. Other words, current-sign-conditioned control, intermediate/path/analog observations and additional calibration data require separate information accounting. Approximation and sample-budget brackets are certified bounds, not identified optima or laboratory feasibility claims.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact preparation-free information checks; fixed cap>={information['necessary_fixed_total_pairs']} -> {args.output}")


if __name__ == "__main__":
    main()
