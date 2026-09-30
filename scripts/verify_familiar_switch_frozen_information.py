#!/usr/bin/env python3
"""Exact acquisition lower bounds for the five-word frozen-field experiment.

The explicit ordinary reversible three-state comparator matches every pure
field law exactly.  Rational matrix and logarithm enclosures bound the only
nonzero arm KL, for HL, with and without a known 1% readout flip channel.
The testing lower bound is a standard change-of-measure consequence; it is
not a sufficient sample budget or a result for arbitrary sampling schemes.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_switch_frozen_equivalence.json"
INPUT_SHA256 = "22d4c933c424c81632dceb3a90a221ed18de3c30cda624fd4a21a6f0d9407a30"
PROOF = "docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md"
PROOF_SHA256 = "d8df8dd7b1ce248ff8bdbcd5d1d95f8ef371250c47a8eef4fc8f85f4184097b3"
ORDER = 64
FIELDS = (F(0), F(7, 9))
WORDS = ("L", "LL", "H", "HH", "HL")
CHECKS = []
TARGET_S = (F(1), F(1), F(-1), F(-1))
TARGET_Z = (F(1), F(-1), F(1), F(-1))
TARGET_RHO = (F(1, 3), F(1, 6), F(1, 6), F(1, 3))
RIVAL_S = (F(1), F(1), F(-1))
RIVAL_RHO = (F(1, 4), F(1, 4), F(1, 2))
RIVAL_Z = ((F(5, 3), F(-1), F(-1, 3)),
           (F(4, 3), F(-2, 3), F(-1, 3)))
RIVAL_Q = (
    ((F(-5, 9), F(1, 3), F(2, 9)),
     (F(1, 3), F(-1), F(2, 3)),
     (F(1, 9), F(1, 3), F(-4, 9))),
    ((F(-43, 85), F(8, 17), F(3, 85)),
     (F(8, 17), F(-11, 17), F(3, 17)),
     (F(12, 85), F(12, 17), F(-72, 85))),
)


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def norm_inf(a):
    return max(sum(abs(x) for x in row) for row in a)


def exp_taylor(a):
    result, term = eye(len(a)), eye(len(a))
    for k in range(1, ORDER + 1):
        term = [[x / k for x in row] for row in matmul(term, a)]
        result = [[x + y for x, y in zip(ar, br)] for ar, br in zip(result, term)]
    return result


def physical_generator(m):
    q = [[F(0)] * 4 for _ in range(4)]
    for i, (s, z) in enumerate(zip(TARGET_S, TARGET_Z)):
        q[i][i ^ 2] = (1 - s * (m + z / 3) / (1 + m * z / 3)) / 2
        q[i][i ^ 1] = (1 - z * s / 3) / 2
        q[i][i] = -sum(q[i])
    return q


def lower_round(x, denominator=10 ** 22):
    return F((x * denominator).__floor__(), denominator)


def upper_round(x, denominator=10 ** 22):
    return F((x * denominator).__ceil__(), denominator)


def pair_intervals(matrix, rho, signs, error):
    result = []
    for a in (F(1), F(-1)):
        for b in (F(1), F(-1)):
            center = sum((rho[i] * matrix[i][j]
                          for i in range(len(signs)) for j in range(len(signs))
                          if signs[i] == a and signs[j] == b), F(0))
            result.append((lower_round(center - error), upper_round(center + error)))
    check("pair-table-positive-and-normalized-enclosure",
          all(0 < lo <= hi < 1 for lo, hi in result)
          and sum(lo for lo, hi in result) <= 1 <= sum(hi for lo, hi in result))
    return result


def log_interval(x, terms=16):
    """log(x)=2*atanh((x-1)/(x+1)); bound its signed odd-series tail."""
    z = (x - 1) / (x + 1)
    check("positive-log-argument-and-convergent-series", x > 0 and abs(z) < 1)
    partial = 2 * sum((z ** (2 * k + 1) / (2 * k + 1)
                       for k in range(terms)), F(0))
    tail = 2 * abs(z) ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    check("log-tail-below-1e-30", tail < F(1, 10 ** 30))
    return partial - tail, partial + tail


def interval_product(a, b):
    corners = [x * y for x in a for y in b]
    return min(corners), max(corners)


def kl_interval(p, q):
    terms = []
    for (pl, pu), (ql, qu) in zip(p, q):
        logs = (log_interval(pl / qu)[0], log_interval(pu / ql)[1])
        terms.append(interval_product((pl, pu), logs))
    return sum(lo for lo, hi in terms), sum(hi for lo, hi in terms)


def readout_channel(table, flip):
    """Independent binary symmetric readout errors on both endpoints."""
    check("valid-known-readout-flip", 0 <= flip < F(1, 2))
    channel = [[(1 - flip) ** (2 - (i ^ j).bit_count())
                * flip ** ((i ^ j).bit_count()) for j in range(4)] for i in range(4)]
    check("readout-channel-stochastic", all(sum(row) == 1 for row in channel))
    return [(sum(channel[i][j] * table[j][0] for j in range(4)),
             sum(channel[i][j] * table[j][1] for j in range(4))) for i in range(4)]


def model_algebra(generators):
    for name, rho, signs, hidden, qs in (
            ("target", TARGET_RHO, TARGET_S, (TARGET_Z, TARGET_Z), generators),
            ("rival", RIVAL_RHO, RIVAL_S, RIVAL_Z, RIVAL_Q)):
        check(name + ":positive-balanced-preparation",
              all(p > 0 for p in rho) and sum(rho) == 1
              and sum(p * s for p, s in zip(rho, signs)) == 0)
        for j, m in enumerate(FIELDS):
            q, z = qs[j], hidden[j]
            pi = [p * (1 + m * s) for p, s in zip(rho, signs)]
            a, b = 8 * m / (9 - m * m), 3 * (1 - m * m) / (9 - m * m)
            check(name + f":m={m}:Markov",
                  all(sum(row) == 0 for row in q)
                  and all(q[k][l] >= 0 for k in range(len(q))
                          for l in range(len(q)) if k != l))
            check(name + f":m={m}:detailed-balance",
                  all(pi[k] * q[k][l] == pi[l] * q[l][k]
                      for k in range(len(q)) for l in range(len(q))))
            check(name + f":m={m}:common-static-closure",
                  matvec(q, signs) == [a - s + b * zz for s, zz in zip(signs, z)]
                  and matvec(q, z) == [s / 3 - zz for s, zz in zip(signs, z)])
            check(name + f":m={m}:same-initial-moments",
                  sum(p * zz for p, zz in zip(rho, z)) == 0
                  and sum(p * s * zz for p, s, zz in zip(rho, signs, z)) == F(1, 3))
    # The closure and initial moments prove identical endpoint-pair laws
    # at every constant field duration, hence exactly zero KL on four arms.


def verify_information():
    target_q = [physical_generator(m) for m in FIELDS]
    model_algebra(target_q)
    check("five-prescribed-words", WORDS == ("L", "LL", "H", "HH", "HL"))
    check("generator-infinity-norm-at-most-four",
          all(norm_inf(q) <= 4 for q in target_q + list(RIVAL_Q)))
    target_e = [exp_taylor(q) for q in target_q]
    rival_e = [exp_taylor(q) for q in RIVAL_Q]
    # exp(2)<8: sum orders 0..3 and a geometric bound starting at order4
    # gives 67/9<8. Thus exp(4)<64 and the matrix Taylor tail is <=epsilon.
    check("scalar-exp2-upper", F(1) + 2 + 2 + F(4, 3)
          + F(2, 3) / (1 - F(2, 5)) == F(67, 9) < 8)
    epsilon = F(64 * 4 ** (ORDER + 1), factorial(ORDER + 1))
    # True CTMC propagators have infinity norm1. A product of two Taylor
    # approximants differs by <=2epsilon+epsilon^2<3epsilon.
    check("single-factor-tail-below-one", epsilon < 1)
    probability_error = 3 * epsilon
    check("pair-probability-error-below-1e-45", probability_error < F(1, 10 ** 45))
    p = pair_intervals(matmul(target_e[1], target_e[0]),
                       TARGET_RHO, TARGET_S, probability_error)
    q = pair_intervals(matmul(rival_e[1], rival_e[0]),
                       RIVAL_RHO, RIVAL_S, probability_error)
    # kl(.95,.05)=.9log19; split log19 so each odd series converges rapidly.
    log_small, log_two = log_interval(F(19, 16)), log_interval(F(2), terms=48)
    binary = (F(9, 10) * (log_small[0] + 4 * log_two[0]),
              F(9, 10) * (log_small[1] + 4 * log_two[1]))
    binary_outward = (lower_round(binary[0], 10 ** 14), upper_round(binary[1], 10 ** 14))
    cases = []
    for name, flip, expected_count in (("ideal_readout", F(0), 136981),
                                        ("known_1pct_BSC_each_endpoint", F(1, 100), 146312)):
        observed_p, observed_q = readout_channel(p, flip), readout_channel(q, flip)
        kl = kl_interval(observed_p, observed_q)
        outward = (lower_round(kl[0], 10 ** 16), upper_round(kl[1], 10 ** 16))
        check(name + ":positive-narrow-KL", 0 < kl[0] <= kl[1]
              and kl[1] - kl[0] < F(1, 10 ** 18))
        ratio_lower = binary_outward[0] / outward[1]
        count = ratio_lower.__ceil__()
        check(name + ":fixed-budget-integer-bound", count == expected_count)
        check(name + ":ratio-bracket", expected_count - 1 < ratio_lower < expected_count)
        cases.append({
            "name": name, "known_independent_flip_per_endpoint": str(flip),
            "KL_HL_target_to_rival_interval": [str(x) for x in outward],
            "pure_word_KL": {word: "0" for word in WORDS[:-1]},
            "necessary_expected_HL_trials_lower": str(ratio_lower),
            "necessary_fixed_total_trials": count,
            "necessary_fixed_total_binary_readouts": 2 * count,
            "observed_target_HL_pair_table": [[str(lower_round(x[0])), str(upper_round(x[1]))]
                                             for x in observed_p],
            "observed_rival_HL_pair_table": [[str(lower_round(x[0])), str(upper_round(x[1]))]
                                            for x in observed_q],
        })
    return {
        "status": "PASS", "menu": list(WORDS), "Taylor_order": ORDER,
        "pair_outcome_order": ["++", "+-", "-+", "--"],
        "target_HL_pair_table": [[str(x) for x in row] for row in p],
        "rival_HL_pair_table": [[str(x) for x in row] for row in q],
        "matrix_probability_error_upper": str(probability_error),
        "binary_error_probability": "1/20", "binary_KL_exact": "(9/10)*log(19)",
        "binary_KL_interval": [str(x) for x in binary_outward],
        "cases": cases,
        "adaptive_lower_formula": "E_target[N_HL] >= kl(19/20,1/20) / D(P_HL || Q_HL)",
        "fixed_budget_interpretation": "If every trial records both endpoints and total trials have deterministic budget N, then N>=ceil(certified expected-HL lower); do not round an expected random count up to that integer",
        "sampling_scope": "Fresh independent reset trials; each word is selected from completed past trials before the current initial sign is observed; choices may otherwise be adaptive. A finite-expectation stopping rule is allowed for the expectation bound. Protocol choice conditioned on the current initial sign, partial-trial selection, trajectories and correlated resets are outside this certificate.",
        "comparison_scope": "A test valid against all ordinary reversible models with at most three states must also distinguish this explicit comparator. The comparator has exact pure-field equivalence; finite calibration slack only enlarges a null class containing it.",
        "detector_scope": "The optional BSC has known independent 1/100 error at each endpoint in both hypotheses. It is not an unknown-detector robustness claim.",
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
    certificate = verify_information()
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "arithmetic": "Python standard-library exact rational matrix Taylor sums, analytic tails, outward interval arithmetic and odd logarithm series; no floats, fitting or simulation",
        "information_certificate": certificate,
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "These necessary acquisition bounds do not give a sufficient sample budget, a matching optimal test, a cost for resetting or a hardware feasibility result. Adaptive sampling scope and expected-versus-fixed counts are stated in the certificate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} frozen-information checks; fixed budgets >=136981 ideal or >=146312 known-BSC trials -> {args.output}")


if __name__ == "__main__":
    main()
