"""Exact rational certificates for a four-state reversible approximation.

The same physical two-spin model, with hidden attempt rate 5/6, gives
all-word TV < 1/600 and sixteen-setting TV < 1/3000. No floating point,
optimizer, sampled trajectory, or root finder is used.
"""

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[1]
INPUT = "reports/familiar_chain_sharpness.json"
INPUT_SHA256 = "71bfd5baff344261801b13abc7d0bb629430c1b965ce2e6b31a034cffe81ec56"
PROOF = "docs/FAMILIAR_CHAIN_TWO_FIELD_ACCURACY.md"
PROOF_SHA256 = "3cb6df9b691dbd6d9ed2cf4e6880eb54e3583d724c147c666300a3cbc35be65f"
T = F(1, 3)
R = F(5, 6)
FIELDS = (F(0), F(1, 2))
SERIES_DEGREE = 48


def exp_interval(x, n=32):
    assert x >= 0
    terms = [x**k / factorial(k) for k in range(n + 1)]
    lower = sum(terms, F(0))
    first_omitted = terms[-1] * x / (n + 1)
    later_ratio_bound = x / (n + 2)
    assert later_ratio_bound < 1
    return lower, lower + first_omitted / (1 - later_ratio_bound)


def cosh_interval(x, n=16):
    """cosh(x/sqrt(10)), bounded using only rational arithmetic."""
    assert x >= 0
    terms = [x ** (2 * k) / (10**k * factorial(2 * k)) for k in range(n + 1)]
    lower = sum(terms, F(0))
    first_omitted = terms[-1] * x * x / (10 * (2 * n + 1) * (2 * n + 2))
    later_ratio_bound = x * x / (10 * (2 * n + 3) * (2 * n + 4))
    assert later_ratio_bound < 1
    return lower, lower + first_omitted / (1 - later_ratio_bound)


def scaled_sinh_interval(x, n=16):
    """sinh(x/sqrt(10))/sqrt(10), using rational arithmetic."""
    assert x >= 0
    terms = [
        x ** (2 * k + 1) / (10 ** (k + 1) * factorial(2 * k + 1))
        for k in range(n + 1)
    ]
    lower = sum(terms, F(0))
    first_omitted = terms[-1] * x * x / (10 * (2 * n + 2) * (2 * n + 3))
    later_ratio_bound = x * x / (10 * (2 * n + 4) * (2 * n + 5))
    assert later_ratio_bound < 1
    return lower, lower + first_omitted / (1 - later_ratio_bound)


def reduced_tail_interval(x):
    lower, upper = exp_interval(F(5, 6) * x)
    return 1 / upper, 1 / lower


def target_tail_interval(x):
    exp_lower, exp_upper = exp_interval(x)
    cosh_lower, cosh_upper = cosh_interval(x)
    sinh_lower, sinh_upper = scaled_sinh_interval(x)
    return (
        (cosh_lower + sinh_lower) / exp_upper,
        (cosh_upper + sinh_upper) / exp_lower,
    )


def crossing_sign_interval(x):
    cosh_lower, cosh_upper = cosh_interval(x)
    exp_lower, exp_upper = exp_interval(x / 6)
    return (
        F(9, 10) * cosh_lower - F(5, 6) * exp_upper,
        F(9, 10) * cosh_upper - F(5, 6) * exp_lower,
    )


def uniform_certificate():
    a, b, c, d = (F(x, 10000) for x in (5530, 5531, 33702, 33703))
    assert crossing_sign_interval(a)[0] > 0
    assert crossing_sign_interval(b)[1] < 0
    assert crossing_sign_interval(c)[1] < 0
    assert crossing_sign_interval(d)[0] > 0
    l1_upper = 2 * (
        reduced_tail_interval(a)[1]
        - target_tail_interval(b)[0]
        + target_tail_interval(c)[1]
        - reduced_tail_interval(d)[0]
    )
    assert l1_upper < F(48493102, 10**9)
    assert l1_upper < F(486, 10000)
    tv_upper = l1_upper / 32
    assert tv_upper < F(152, 100000)
    assert tv_upper < F(1, 600)
    return {
        "status": "PASS",
        "crossing_brackets": [[str(a), str(b)], [str(c), str(d)]],
        "normalized_kernel_L1_upper": "243/5000",
        "uniform_TV_upper": "19/12500",
        "simpler_uniform_TV_upper": "1/600",
        "scope": "Every finite nonnegative field word, arbitrary dwell times and total horizons; initial/final pair laws only",
        "method": "Positive rational scalar Taylor series with geometric remainders; exact density-crossing signs and tail enclosures; analytical gain 1/32",
    }


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a, b):
    return [sum((x * y for x, y in zip(row, b)), F(0)) for row in a]


def mean_matrix(n, m):
    den = 1 - T * T * m * m
    a = m * (1 - T * T) / den
    b = T * (1 - m * m) / den
    if n == 3:
        c = T / (1 + T * T)
        return [[F(-1), b, F(0), a],
                [c, F(-1), c, F(0)],
                [F(0), T, F(-1), F(0)],
                [F(0), F(0), F(0), F(0)]]
    assert n == 2
    return [[F(-1), b, a],
            [R * T, -R, F(0)],
            [F(0), F(0), F(0)]]


@lru_cache(None)
def propagator_intervals(n, m, duration):
    """e^(duration*M), with a nonnegative substochastic shifted matrix.

    H=M+I has row sums <=1. Every omitted power H^k has entries <=1,
    so the scalar exponential tail encloses every matrix-series tail.
    """
    mtx = mean_matrix(n, m)
    size = len(mtx)
    unit = identity(size)
    h = [[mtx[i][j] + unit[i][j] for j in range(size)] for i in range(size)]
    assert all(value >= 0 for row in h for value in row)
    assert all(sum(row) <= 1 for row in h)
    term = unit
    partial = [[value for value in row] for row in unit]
    for k in range(1, SERIES_DEGREE + 1):
        term = matmul(term, h)
        term = [[value * duration / k for value in row] for row in term]
        partial = [[partial[i][j] + term[i][j] for j in range(size)]
                   for i in range(size)]
    exp_lower, exp_upper = exp_interval(duration, SERIES_DEGREE)
    scalar_tail = exp_upper - exp_lower
    lower = [[value / exp_upper for value in row] for row in partial]
    upper = [[(value + scalar_tail) / exp_lower for value in row]
             for row in partial]
    return lower, upper


def endpoint_intervals(n, word):
    # Initial U is zero; initial V contains equilibrium conditional means.
    u = [F(0)] * n + [F(1)]
    v = [T**j for j in range(n)] + [F(0)]
    ul, uu, vl, vu = u, u, v, v
    for field, duration in word:
        lower, upper = propagator_intervals(n, FIELDS[field], F(duration))
        ul, uu = matvec(lower, ul), matvec(upper, uu)
        vl, vu = matvec(lower, vl), matvec(upper, vu)
    return (ul[0], uu[0]), (vl[0], vu[0])


def rounded_lower(x, denominator=10**15):
    return F((x * denominator).__floor__(), denominator)


def rounded_upper(x, denominator=10**15):
    return F((x * denominator).__ceil__(), denominator)


def absolute_interval(interval):
    lower, upper = interval
    assert lower <= upper
    min_abs = F(0) if lower <= 0 <= upper else min(abs(lower), abs(upper))
    return min_abs, max(abs(lower), abs(upper))


def finite_menu_certificate():
    menu = [((j, q),) for j in range(2) for q in range(1, 5)]
    menu += [((j, a), (1 - j, b)) for j in range(2)
             for a in (1, 2) for b in (1, 2)]
    assert len(menu) == len(set(menu)) == 16
    fixtures = []
    global_lower, global_upper = F(0), F(0)
    for word in menu:
        target = endpoint_intervals(3, word)
        reduced = endpoint_intervals(2, word)
        diffs = [absolute_interval((x[0] - y[1], x[1] - y[0]))
                 for x, y in zip(target, reduced)]
        tv_lower = max(x[0] for x in diffs) / 2
        tv_upper = max(x[1] for x in diffs) / 2
        assert tv_upper - tv_lower < F(1, 10**25)
        assert tv_upper < F(1, 3000)
        global_lower = max(global_lower, tv_lower)
        global_upper = max(global_upper, tv_upper)
        fixtures.append({
            "word": [[str(FIELDS[j]), q] for j, q in word],
            "TV_lower": str(rounded_lower(tv_lower)),
            "TV_upper": str(rounded_upper(tv_upper)),
            "target_U": [str(rounded_lower(target[0][0])), str(rounded_upper(target[0][1]))],
            "target_V": [str(rounded_lower(target[1][0])), str(rounded_upper(target[1][1]))],
        })
    assert global_upper < F(273, 10**6)
    return {
        "status": "PASS", "settings": len(menu), "clock": "1",
        "fields": [str(m) for m in FIELDS], "series_degree": SERIES_DEGREE,
        "largest_matrix_dimension": 4,
        "maximum_TV_interval": [str(rounded_lower(global_lower)), str(rounded_upper(global_upper))],
        "uniform_menu_TV_upper": "1/3000", "fixtures": fixtures,
        "method": "Exact nonnegative shifted-matrix Taylor sums, scalar exponential and geometric tail enclosures; balanced-pair TV=max(|dU|,|dV|)/2",
    }


def physical_model_checks():
    states = [(s, z) for s in (1, -1) for z in (1, -1)]
    for m in (F(0), F(1, 4), F(1, 2)):
        rho = [(1 + T * s * z) * (1 + m * s) / 4 for s, z in states]
        assert sum(rho) == 1 and all(p > 0 for p in rho)
        q = [[F(0) for _ in states] for _ in states]
        for i, (s, z) in enumerate(states):
            q[i][states.index((-s, z))] = (1 - s * (m + T * z) / (1 + m * T * z)) / 2
            q[i][states.index((s, -z))] = R * (1 - z * T * s) / 2
            q[i][i] = -sum(q[i])
        assert all(q[i][j] >= 0 for i in range(4) for j in range(4) if i != j)
        assert all(rho[i] * q[i][j] == rho[j] * q[j][i]
                   for i in range(4) for j in range(4))
        qs = matvec(q, [F(s) for s, z in states])
        qz = matvec(q, [F(z) for s, z in states])
        matrix = mean_matrix(2, m)
        assert all(qs[i] == matrix[0][0] * s + matrix[0][1] * z + matrix[0][2]
                   for i, (s, z) in enumerate(states))
        assert all(qz[i] == R * (T * s - z) for i, (s, z) in enumerate(states))
    return {"status": "PASS", "states": 4, "t": str(T),
            "boundary_attempt_rate": "1", "hidden_attempt_rate": str(R),
            "fields_checked": ["0", "1/4", "1/2"],
            "scope": "Physical two-spin heat-bath CTMC with deterministic sign; zero-field equilibrium preparation; standard Gibbs tilt and detailed balance"}


def provenance():
    payload = (ROOT / INPUT).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == INPUT_SHA256
    inherited = json.loads(payload)
    assert inherited["status"] == "PASS"
    sources = dict(inherited["source_sha256"])
    proofs = dict(inherited["proof_snapshot_sha256"])
    reports = dict(inherited.get("input_report_sha256", {}))
    reports[INPUT] = INPUT_SHA256
    for name, digest in sources.items():
        assert hashlib.sha256((ROOT / "scripts" / name).read_bytes()).hexdigest() == digest
    for name, digest in {**proofs, **reports}.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert hashlib.sha256((ROOT / PROOF).read_bytes()).hexdigest() == PROOF_SHA256
    proofs[PROOF] = PROOF_SHA256
    return sources, proofs, reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    report = {
        "status": "PASS", "versions": {"python": platform.python_version()},
        "arithmetic": "Exact Python Fraction rational arithmetic; no floats, optimizer, root finder, numerical integral, or simulated data",
        "physical_model": physical_model_checks(),
        "uniform_endpoint_bound": uniform_certificate(),
        "finite_menu_bound": finite_menu_certificate(),
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "These are constructive upper bounds on approximation error. They do not prove optimality, full-path approximation, a measurement budget or hardware feasibility. The all-word analytical argument is supplied in the bound proof; finite fixtures supplement it.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: exact four-state approximation certificates, 16 settings and all-word bound -> {args.output}")


if __name__ == "__main__":
    main()
