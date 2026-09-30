#!/usr/bin/env python3
"""Exact five-protocol acquisition lower from a closer reversible CTMC rival.

A small numerical fit located the six conductances. This verifier treats the
listed rational numbers as fixed inputs: no optimizer, fit convergence,
simulation, or floating-point calculation enters acceptance. It certifies a
constructive comparator, not a closest model or a minimax optimum.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

import verify_familiar_switch_frozen_information as base

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_frozen_information.json"
INPUT_SHA256 = "766adef9a912231a30e8c4675cec5353bdbd11e31767d8151292006f9c223d71"
PROOF = "docs/FAMILIAR_SWITCH_PROFILED_ACQUISITION.md"
PROOF_SHA256 = "351b33f58bc3738d44ee418cfa0fb309d1b335f4f964e9ca807e97b2e6dbb184"
HELPER_SHA256 = "9587614ec13e0d436825f389b32223fe3f73cba2c88951ef24c65cb383c8c12e"
RHO = (F(1, 4), F(1, 4), F(1, 2))
SIGNS = (F(1), F(1), F(-1))
FIELDS = (F(0), F(7, 9))
EDGES = ((0, 1), (0, 2), (1, 2))
CONDUCTANCES = (
    (F("0.09006333"), F("0.05831059"), F("0.16147905")),
    (F("0.24140656"), F("0.01830492"), F("0.07508300")),
)
WORDS = ((0,), (0, 0), (1,), (1, 1), (1, 0))
NAMES = ("L", "LL", "H", "HH", "HL")
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def rival_generator(m, conductances):
    pi = [p * (1 + m * s) for p, s in zip(RHO, SIGNS)]
    q = [[F(0)] * 3 for _ in range(3)]
    for conductance, (i, j) in zip(conductances, EDGES):
        q[i][j] = conductance / pi[i]
        q[j][i] = conductance / pi[j]
    for i in range(3):
        q[i][i] = -sum(q[i])
    check(f"m={m}:positive-normalized-Gibbs-law", min(pi) > 0 and sum(pi) == 1)
    check(f"m={m}:strictly-positive-off-diagonal-rates",
          all(q[i][j] > 0 for i in range(3) for j in range(3) if i != j))
    check(f"m={m}:zero-row-sums", all(sum(row) == 0 for row in q))
    check(f"m={m}:detailed-balance",
          all(pi[i] * q[i][j] == pi[j] * q[j][i] for i in range(3) for j in range(3)))
    check(f"m={m}:stationarity",
          all(sum(pi[i] * q[i][j] for i in range(3)) == 0 for j in range(3)))
    return q


def table_text(table):
    return [[str(base.lower_round(lo)), str(base.upper_round(hi))] for lo, hi in table]


def tv_interval(p, q):
    differences = [(pl - qu, pu - ql) for (pl, pu), (ql, qu) in zip(p, q)]
    lower = sum(F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi)) for lo, hi in differences) / 2
    upper = sum(max(abs(lo), abs(hi)) for lo, hi in differences) / 2
    return [str(base.lower_round(lower, 10 ** 14)), str(base.upper_round(upper, 10 ** 14))]


def verify_profiled_information():
    inherited_check_start = len(base.CHECKS)
    check("common-balanced-rational-preparation", sum(RHO) == 1 and min(RHO) > 0
          and sum(p * s for p, s in zip(RHO, SIGNS)) == 0)
    check("five-word-menu", WORDS == ((0,), (0, 0), (1,), (1, 1), (1, 0)))
    target_q = [base.physical_generator(m) for m in FIELDS]
    rival_q = [rival_generator(m, c) for m, c in zip(FIELDS, CONDUCTANCES)]
    check("generator-infinity-norm-at-most-four",
          all(base.norm_inf(q) <= 4 for q in target_q + rival_q))
    check("fixed-Taylor-order-64", base.ORDER == 64)
    target_e = [base.exp_taylor(q) for q in target_q]
    rival_e = [base.exp_taylor(q) for q in rival_q]
    # The bound is the inherited e^4<64 matrix Taylor remainder. True
    # CTMC factors have norm 1; products of at most two factors have error
    # <=2epsilon+epsilon^2<3epsilon. A pair event cannot increase that bound.
    epsilon = F(64 * 4 ** 65, factorial(65))
    error = 3 * epsilon
    check("matrix-tail-small", epsilon < 1 and error < F(1, 10 ** 45))
    log_small = base.log_interval(F(19, 16))
    log_two = base.log_interval(F(2), terms=48)
    binary_lower = base.lower_round(F(9, 10) * (log_small[0] + 4 * log_two[0]), 10 ** 14)
    binary_upper = base.upper_round(F(9, 10) * (log_small[1] + 4 * log_two[1]), 10 ** 14)
    tables = []
    for name, word in zip(NAMES, WORDS):
        target, rival = base.eye(4), base.eye(3)
        for j in word:
            target = base.matmul(target, target_e[j])
            rival = base.matmul(rival, rival_e[j])
        p = base.pair_intervals(target, base.TARGET_RHO, base.TARGET_S, error)
        q = base.pair_intervals(rival, RHO, SIGNS, error)
        tables.append((name, p, q))
    cases = []
    for name, flip, coarse, expected_count in (
            ("ideal_readout", F(0), F(93, 10 ** 8), 2849458),
            ("known_1pct_BSC_each_endpoint", F(1, 100), F(86, 10 ** 8), 3081390)):
        fixtures, maximum_upper = [], F(0)
        for word, p, q in tables:
            observed_p = base.readout_channel(p, flip)
            observed_q = base.readout_channel(q, flip)
            lo, hi = base.kl_interval(observed_p, observed_q)
            outward = (base.lower_round(lo, 10 ** 17), base.upper_round(hi, 10 ** 17))
            check(name + f":{word}:positive-narrow-KL", 0 < lo <= hi and hi - lo < F(1, 10 ** 18))
            check(name + f":{word}:KL-below-coarse-upper", outward[1] < coarse)
            maximum_upper = max(maximum_upper, outward[1])
            fixtures.append({"word": word, "KL_target_to_rival_interval": [str(x) for x in outward],
                             "TV_interval": tv_interval(observed_p, observed_q),
                             "target_pair_table": table_text(observed_p),
                             "rival_pair_table": table_text(observed_q)})
        ratio = binary_lower / coarse
        tight_ratio = binary_lower / maximum_upper
        fixed_count = ratio.__ceil__()
        check(name + ":fixed-total-budget-lower", fixed_count == expected_count)
        check(name + ":expected-count-bracket", expected_count - 1 < ratio < expected_count)
        cases.append({
            "name": name, "known_independent_flip_per_endpoint": str(flip),
            "fixtures": fixtures, "maximum_arm_KL_upper": str(maximum_upper),
            "simple_maximum_arm_KL_upper": str(coarse),
            "necessary_expected_total_trials_strict_lower": str(ratio),
            "necessary_fixed_total_trials": fixed_count,
            "necessary_fixed_total_binary_readouts": 2 * fixed_count,
            "optional_tighter_necessary_fixed_total_trials": tight_ratio.__ceil__(),
        })
    CHECKS.extend("helper:" + label for label in base.CHECKS[inherited_check_start:])
    return {
        "status": "PASS", "menu": list(NAMES), "clock": "1", "tanh_J": "1/3",
        "fields": [str(m) for m in FIELDS], "rho0": [str(x) for x in RHO],
        "signs": [str(x) for x in SIGNS], "edge_order": [list(edge) for edge in EDGES],
        "conductances": [[str(x) for x in row] for row in CONDUCTANCES],
        "generators": [[[str(x) for x in row] for row in q] for q in rival_q],
        "Taylor_order": 64, "pair_outcome_order": ["++", "+-", "-+", "--"],
        "pair_probability_error_upper": str(error),
        "binary_error_probability": "1/20", "binary_KL_exact": "(9/10)*log(19)",
        "binary_KL_interval": [str(binary_lower), str(binary_upper)], "cases": cases,
        "adaptive_change_of_measure": "sum_w E_target[N_w]*D(P_w||Q_w) >= kl(19/20,1/20); bounding every arm KL by c gives E_target[N_total] > certified_binary_KL_lower/c",
        "sampling_scope": "Independent complete reset-pair trials; arm chosen using completed past trials before seeing the current initial sign. Adaptive choice and finite-expectation stopping are allowed. Current-sign-conditioned arm choice, partial-trial selection, correlated resets, other words and trajectory observations are outside this bound.",
        "fixed_budget_interpretation": "Integer ceiling applies to a deterministic cap on total pair trials, not to an expected random count. Each complete pair trial contains two binary endpoint readouts.",
        "null_scope": "The explicit comparator is a genuine ordinary reversible CTMC with the exact nominal tilt 7/9 and common balanced preparation. It is a member of both the fixed-tilt null and any larger unknown-tilt null containing 7/9. Pure-field laws are approximately, not exactly, matched.",
        "discovery_and_validation": "A small deterministic numerical fit suggested six conductances; the fixed eight-decimal rational table is certified here without invoking an optimizer or its convergence. No closest-comparator or minimax-optimality claim is made.",
        "detector_scope": "Optional known 1/100 independent BSC errors at each endpoint are identical under both hypotheses; no unknown-detector robustness is asserted.",
    }


def provenance():
    payload = (ROOT / INPUT).read_bytes()
    check("input-report-hash", hashlib.sha256(payload).hexdigest() == INPUT_SHA256)
    inherited = json.loads(payload)
    check("input-report-PASS", inherited["status"] == "PASS")
    sources = dict(inherited["source_sha256"])
    proofs = dict(inherited["proof_snapshot_sha256"])
    reports = dict(inherited["input_report_sha256"])
    reports[INPUT] = INPUT_SHA256
    check("imported-helper-hash", hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest() == HELPER_SHA256)
    check("helper-in-inherited-source-chain", sources.get(Path(base.__file__).name) == HELPER_SHA256)
    for name, digest in sources.items():
        check("source-hash:" + name,
              hashlib.sha256((ROOT / "scripts" / name).read_bytes()).hexdigest() == digest)
    for name, digest in {**proofs, **reports}.items():
        check("inherited-hash:" + name,
              hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest)
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
    certificate = verify_profiled_information()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "arithmetic": "Exact standard-library Fraction arithmetic; fixed rational CTMC rates, SHA-bound matrix Taylor/logarithm interval helpers and outward rounding; no floating-point computations or optimizer",
        "profiled_information_certificate": certificate,
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "Necessary acquisition counts on this five-word menu only; no sufficient testing budget, optimal null, complete-path comparison, detector-uncertainty certificate or hardware-feasibility conclusion.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} profiled-information checks; fixed budgets >=2849458 ideal or >=3081390 known-BSC trials -> {args.output}")


if __name__ == "__main__":
    main()
