#!/usr/bin/env python3
"""Exact frozen-field equivalence and switching error for two Ising spins.

Checks two fixed rational three-state constructions directly. The reversible
construction is exact at each fixed field, but changes its hidden coordinate
when the field changes. The general construction is exact for all words.
Only standard-library rational arithmetic enters the certificates.
"""
import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from math import factorial
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_chain_cross_rank.json"
INPUT_SHA256 = "2f23889fbe560df9201e9885769bbe83dd28e7373adebb86c3bb31c422e1e39c"
PROOF = "docs/FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md"
PROOF_SHA256 = "96670d6b5d111dc63627407f5835ab39594a62996079724ff499966d39547428"
FIELDS = (F(0), F(7, 9))
T = F(1, 3)
ORDER = 48
CHECKS = []
REV_RHO = (F(1, 4), F(1, 4), F(1, 2))
REV_S = (F(1), F(1), F(-1))
REV_Z = ((F(5, 3), F(-1), F(-1, 3)),
         (F(4, 3), F(-2, 3), F(-1, 3)))
REV_Q = (
    ((F(-5, 9), F(1, 3), F(2, 9)),
     (F(1, 3), F(-1), F(2, 3)),
     (F(1, 9), F(1, 3), F(-4, 9))),
    ((F(-43, 85), F(8, 17), F(3, 85)),
     (F(8, 17), F(-11, 17), F(3, 17)),
     (F(12, 85), F(12, 17), F(-72, 85))),
)
GEN_RHO = (F(1, 2), F(2, 7), F(3, 14))
GEN_S = (F(-1), F(1), F(1))
GEN_Z = (F(-1, 3), F(-2, 3), F(5, 3))
GEN_Q = (
    ((F(-4, 9), F(8, 21), F(4, 63)),
     (F(11, 18), F(-20, 21), F(43, 126)),
     (F(2, 9), F(8, 21), F(-38, 63))),
    ((F(-72, 85), F(432, 595), F(72, 595)),
     (F(3, 17), F(-69, 119), F(48, 119)),
     (F(1, 85), F(334, 595), F(-341, 595))),
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


def rowmat(v, a):
    return [sum((v[i] * a[i][j] for i in range(len(v))), F(0)) for j in range(len(a[0]))]


def coefficients(m):
    return 8 * m / (9 - m * m), 3 * (1 - m * m) / (9 - m * m)


def target_mean_matrix(m):
    a, b = coefficients(m)
    return [[F(-1), b, a], [T, F(-1), F(0)], [F(0), F(0), F(0)]]


def target_centered_matrix(m):
    _, b = coefficients(m)
    return [[F(-1), b], [T, F(-1)]]


def scalar_exp_interval(x):
    lower = sum((x ** k / factorial(k) for k in range(ORDER + 1)), F(0))
    first = x ** (ORDER + 1) / factorial(ORDER + 1)
    check(f"scalar-tail:x={x}", 0 <= x < ORDER + 2)
    return lower, lower + first / (1 - x / (ORDER + 2))


def exp_interval(q, time=F(1), rate=F(1)):
    """Positive uniformization, for a substochastic shifted matrix."""
    n = len(q)
    unit = eye(n)
    h = [[unit[i][j] + q[i][j] / rate for j in range(n)] for i in range(n)]
    check(f"dimension={n}:shift-positive-substochastic",
          all(x >= 0 for row in h for x in row) and all(sum(row) <= 1 for row in h))
    x = time * rate
    term, partial = unit, [row[:] for row in unit]
    for k in range(1, ORDER + 1):
        term = [[value * x / k for value in row] for row in matmul(term, h)]
        partial = [[partial[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    exp_lower, exp_upper = scalar_exp_interval(x)
    tail = exp_upper - exp_lower
    return ([[value / exp_upper for value in row] for row in partial],
            [[(value + tail) / exp_lower for value in row] for row in partial])


def closure(label, q, signs, hidden, m):
    a, b = coefficients(m)
    check(label + ":visible", matvec(q, signs) == [a - s + b * z for s, z in zip(signs, hidden)])
    check(label + ":hidden", matvec(q, hidden) == [T * s - z for s, z in zip(signs, hidden)])


def model_checks(label, rho, signs, zs, generators, reversible):
    check(label + ":positive-balanced-preparation", all(x > 0 for x in rho)
          and sum(rho) == 1 and sum(p * s for p, s in zip(rho, signs)) == 0)
    for j, m in enumerate(FIELDS):
        q, hidden = generators[j], zs[j]
        field_rho = [p * (1 + m * s) for p, s in zip(rho, signs)]
        prefix = label + f":m={m}"
        check(prefix + ":positive-normalized-field-law", all(x > 0 for x in field_rho) and sum(field_rho) == 1)
        check(prefix + ":Markov", all(sum(row) == 0 for row in q)
              and all(q[i][k] >= 0 for i in range(len(q)) for k in range(len(q)) if i != k))
        check(prefix + ":unit-exit-budget", all(-q[i][i] <= 1 for i in range(len(q))))
        check(prefix + ":stationarity", rowmat(field_rho, q) == [F(0)] * len(q))
        residual = field_rho[0] * q[0][1] - field_rho[1] * q[1][0]
        if reversible:
            check(prefix + ":detailed-balance", all(field_rho[i] * q[i][k] == field_rho[k] * q[k][i]
                                                     for i in range(len(q)) for k in range(len(q))))
        else:
            check(prefix + ":nonreversible-flux", residual == (F(1, 63), F(-16, 1785))[j])
        check(prefix + ":irreducible", all(q[i][k] > 0 for i in range(len(q)) for k in range(len(q)) if i != k))
        closure(prefix + ":pointwise-closure", q, signs, hidden, m)
        for sign in (1, -1):
            prep = [2 * p if s == sign else F(0) for p, s in zip(rho, signs)]
            check(prefix + f":conditional-preparation-{sign}", sum(prep) == 1
                  and sum(p * z for p, z in zip(prep, hidden)) == T * sign)


def physical_generator(m):
    states = tuple(product((1, -1), repeat=2))
    q = [[F(0) for _ in states] for _ in states]
    for i, (s, z) in enumerate(states):
        q[i][states.index((-s, z))] = (1 - s * (m + T * z) / (1 + m * T * z)) / 2
        q[i][states.index((s, -z))] = (1 - z * T * s) / 2
        q[i][i] = -sum(q[i])
    return states, q


def verify_algebra():
    start = len(CHECKS)
    check("field-H-coefficients", coefficients(FIELDS[1]) == (F(63, 85), F(12, 85)))
    model_checks("reversible-three-state", REV_RHO, REV_S, REV_Z, REV_Q, True)
    model_checks("general-three-state", GEN_RHO, GEN_S, (GEN_Z, GEN_Z), GEN_Q, False)
    u0 = [z - T * s for z, s in zip(REV_Z[0], REV_S)]
    uh = [z - T * s for z, s in zip(REV_Z[1], REV_S)]
    check("field-dependent-hidden-coordinate-ratio", uh == [F(3, 4) * u for u in u0])
    check("singleton-hidden-coordinate-zero", u0[2] == uh[2] == 0)
    for j, m in enumerate(FIELDS):
        field_rho = [p * (1 + m * s) for p, s in zip(REV_RHO, REV_S)]
        centered = [z - T * s for z, s in zip(REV_Z[j], REV_S)]
        check(f"m={m}:hidden-zero-mean-and-covariance",
              sum(p * u for p, u in zip(field_rho, centered)) == 0
              and sum(p * s * u for p, s, u in zip(field_rho, REV_S, centered)) == 0)
        check(f"m={m}:hidden-Gram", sum(p * u * u for p, u in zip(field_rho, centered)) == F(8, 9))
        states, q = physical_generator(m)
        signs = [F(s) for s, z in states]
        hidden = [F(z) for s, z in states]
        rho0 = [(1 + T * s * z) / 4 for s, z in states]
        pm = [p * (1 + m * s) for p, s in zip(rho0, signs)]
        check(f"m={m}:physical-normalization", sum(pm) == 1 and all(p > 0 for p in pm))
        check(f"m={m}:physical-detailed-balance", all(pm[i] * q[i][k] == pm[k] * q[k][i]
                                                     for i in range(4) for k in range(4)))
        closure(f"m={m}:physical-four-state", q, signs, hidden, m)
        for sign in (1, -1):
            check(f"m={m}:physical-conditional-preparation-{sign}",
                  sum(2 * p * z for p, s, z in zip(rho0, signs, hidden) if s == sign) == T * sign)
        _, b = coefficients(m)
        # For e^A, J_m=(b/t) H_m and the hidden residual response is (1-t*b)H_m.
        a = target_centered_matrix(m)
        check(f"m={m}:centered-offdiagonal-ratio", a[0][1] / a[1][0] == b / T)
    check("LH-switch-coefficient", F(1, 2) * F(1, 4) * F(8, 9) * F(36, 85) == F(4, 85))
    check("HL-switch-coefficient", F(1, 2) * F(1, 3) * F(81, 85) == F(27, 170))
    check("opposite-order-factor-ratio", F(27, 170) / F(4, 85) == F(27, 8))
    return {"status": "PASS", "exact_checks": len(CHECKS) - start,
            "reversible_model": "Three states; one Gibbs preparation; exact fixed-field endpoint-pair laws for every duration at both fields; field-dependent hidden coordinate",
            "general_model": "Three states; same Gibbs equilibrium family but not detailed balanced; one common hidden coordinate closes under both generators, hence exact endpoint pairs for all finite words over the two selected fields",
            "fixed_field_scope": "Common initial preparation and deterministic readout; no control-dependent preparation",
            "exit_budget": "Every rate sum in either three-state construction is at most one"}


def target_moments(word, kernels):
    u, v = [F(0), F(0), F(1)], [F(1), T, F(0)]
    ul, uu, vl, vu = u, u, v, v
    for j in word:
        lo, hi = kernels[j]
        ul, uu, vl, vu = matvec(lo, ul), matvec(hi, uu), matvec(lo, vl), matvec(hi, vu)
    return (ul[0], uu[0]), (vl[0], vu[0])


def rival_moments(word, kernels):
    conditional = []
    for sign in (1, -1):
        initial = [2 * p if s == sign else F(0) for p, s in zip(REV_RHO, REV_S)]
        lo, hi = initial, initial
        for j in word:
            kl, ku = kernels[j]
            lo, hi = rowmat(lo, kl), rowmat(hi, ku)
        conditional.append((lo[0] + lo[1] - hi[2], hi[0] + hi[1] - lo[2]))
    plus, minus = conditional
    return ((plus[0] + minus[0]) / 2, (plus[1] + minus[1]) / 2), \
           ((plus[0] - minus[1]) / 2, (plus[1] - minus[0]) / 2)


def absolute_interval(interval):
    lo, hi = interval
    return (F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))), max(abs(lo), abs(hi))


def tv_interval(target, rival):
    differences = [absolute_interval((x[0] - y[1], x[1] - y[0])) for x, y in zip(target, rival)]
    return max(d[0] for d in differences) / 2, max(d[1] for d in differences) / 2


def rounded_interval(interval, denominator=10 ** 16):
    lo, hi = interval
    return [str(F((lo * denominator).__floor__(), denominator)),
            str(F((hi * denominator).__ceil__(), denominator))]


def verify_switching():
    start = len(CHECKS)
    target = [exp_interval(target_mean_matrix(m)) for m in FIELDS]
    rival = [exp_interval(q) for q in REV_Q]
    hs, responses, pure, mixed = {}, [], [], []
    for j, m in enumerate(FIELDS):
        for time in (1, 2):
            lo, hi = exp_interval(target_centered_matrix(m), F(time))
            h = hs[j, time] = (lo[1][0], hi[1][0])
            check(f"m={m},time={time}:positive-response", h[0] > 0)
            check(f"m={m},time={time}:response-width", h[1] - h[0] < F(1, 10 ** 40))
            responses.append({"m": str(m), "time": time, "H_ZS_interval": rounded_interval(h)})
        check(f"m={m}:response-at-one-exceeds-two", hs[j, 1][0] > hs[j, 2][1])
        for q in (1, 2, 3, 4):
            word = (j,) * q
            actual, predicted = target_moments(word, target), rival_moments(word, rival)
            check(f"pure-{j}^{q}:independent-moment-enclosures",
                  all(max(x[0], y[0]) <= min(x[1], y[1]) for x, y in zip(actual, predicted)))
            pure.append({"field": str(m), "duration": q, "exact_TV": "0",
                         "target_mean_interval": rounded_interval(actual[0]),
                         "target_correlation_interval": rounded_interval(actual[1])})
    errors = {}
    factors = (F(4, 85), F(27, 170))
    for first in (0, 1):
        for a, b in product((1, 2), repeat=2):
            second = 1 - first
            x, y = hs[first, a], hs[second, b]
            formula = (factors[first] * x[0] * y[0], factors[first] * x[1] * y[1])
            word = (first,) * a + (second,) * b
            direct = tv_interval(target_moments(word, target), rival_moments(word, rival))
            check(f"mixed-{first}^{a}{second}^{b}:direct-formula-agreement",
                  max(formula[0], direct[0]) <= min(formula[1], direct[1]))
            check(f"mixed-{first}^{a}{second}^{b}:positive-and-narrow",
                  formula[0] > 0 and formula[1] - formula[0] < F(1, 10 ** 40))
            errors[first, a, b] = formula
            mixed.append({"first_field": str(FIELDS[first]), "first_duration": a,
                          "second_field": str(FIELDS[second]), "second_duration": b,
                          "TV_interval": rounded_interval(formula)})
    maximum = errors[1, 1, 1]
    check("unique-sixteen-setting-maximum-HL",
          all(maximum[0] > interval[1] for key, interval in errors.items() if key != (1, 1, 1)))
    check("unit-switch-error-between-decimal-bounds",
          F(24518685633, 10 ** 13) < maximum[0] <= maximum[1] < F(24518685635, 10 ** 13))
    return {"status": "PASS", "exact_checks": len(CHECKS) - start,
            "Taylor_order": ORDER, "largest_exponential_dimension": 3,
            "response_values": responses, "pure_settings": pure, "mixed_settings": mixed,
            "maximum_word": "H L", "maximum_TV_interval": rounded_interval(maximum),
            "formula_scope": "The single-switch formula holds between the two selected fields for every positive pair of segment durations; the rational numerical enclosures use durations one and two",
            "limitations": "This fixture comparison alone does not establish an optimum over all three-state rivals; any universal bound must state its calibration assumptions separately"}


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
    algebra, switching = verify_algebra(), verify_switching()
    report = {"status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
              "versions": {"python": platform.python_version()},
              "arithmetic": "Exact rational standard-library arithmetic, fixed generator tables, positive uniformization Taylor sums, and geometric tail bounds; no optimizer or floating-point arithmetic",
              "algebraic_certificate": algebra, "switching_certificate": switching,
              "reversible_fixture": {"rho0": [str(x) for x in REV_RHO], "S": [int(x) for x in REV_S],
                                     "Z": [[str(x) for x in z] for z in REV_Z],
                                     "Q": [[[str(x) for x in row] for row in q] for q in REV_Q]},
              "general_fixture": {"rho0": [str(x) for x in GEN_RHO], "S": [int(x) for x in GEN_S],
                                   "Z": [str(x) for x in GEN_Z],
                                   "Q": [[[str(x) for x in row] for row in q] for q in GEN_Q]},
              "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
              "limitations": "Endpoint-pair statements with one preparation. No complete visible-path equivalence, device realization, practical measurement budget, or global optimization claim."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} frozen-equivalence checks -> {args.output}")


if __name__ == "__main__":
    main()
