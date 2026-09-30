#!/usr/bin/env python3
"""Exact rational certificate for the two-field, three-switch accuracy bound.

The fixture uses tanh(J)=1/3, fields tanh(h)=0,1/2, clock=1, and
maximum endpoint-pair TV error delta=1/1_000_000.  It certifies that
all ordinary reversible rivals need three states of each visible sign,
and all general Markov rivals need at least four states.

Only standard-library rational arithmetic enters the checks.  Printed
floats summarize exact rational inequalities; they do not certify them.
See docs/FAMILIAR_CHAIN_TWO_FIELD_ACCURACY.md for the witness proof.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
from itertools import combinations, product
from math import factorial

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_chain_sharpness.json":
        "71bfd5baff344261801b13abc7d0bb629430c1b965ce2e6b31a034cffe81ec56"
}
PROOFS = {
    "docs/FAMILIAR_CHAIN_TWO_FIELD_ACCURACY.md":
        "3cb6df9b691dbd6d9ed2cf4e6880eb54e3583d724c147c666300a3cbc35be65f"
}
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
    check("inherited-proof-count", len(proofs) == 40)
    for path, digest in PROOFS.items():
        check("new-proof-hash:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


DELTA = F(1, 1_000_000)
ORDER = 40
FIELDS = (F(0), F(1, 2))
# Fixed rational function coefficients; no exact-inverse assumption is used.
B_TEXT = (
    (
        "1 0 0 0",
        "0 1 -4.64852569 10.83498686",
        "0 0 16.58061735 -58.90509581",
        "0 0 -10.72257376 72.67126967",
    ),
    (
        "1 0 -0.58197928 -16.32812046",
        "0 1 -6.00405335 14.06958428",
        "0 0 21.45337346 -75.68477372",
        "0 0 -13.95202822 94.38254147",
    ),
)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zeros(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def matmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(ar, bc)), F(0)) for bc in bt] for ar in a]


def norm_inf(a):
    return max(sum(abs(x) for x in row) for row in a)


def congruence(a, left, right=None):
    return matmul(matmul(transpose(left), a), left if right is None else right)


def diagonal_margin(a):
    return min(a[i][i] - sum(abs(x) for j, x in enumerate(a[i]) if j != i)
               for i in range(len(a)))


def generator(m):
    return [
        [F(0), 8 * m / (9 - m * m), F(0), F(0)],
        [F(0), F(-1), F(3, 10), F(0)],
        [F(0), 3 * (1 - m * m) / (9 - m * m), F(-1), F(1, 3)],
        [F(0), F(0), F(3, 10), F(-1)],
    ]


def exp_taylor(a):
    result = eye(len(a))
    term = eye(len(a))
    for k in range(1, ORDER + 1):
        term = scale(F(1, k), matmul(term, a))
        result = add(result, term)
    return result


def insert(coefficients, key, i, j, value=F(1)):
    if key not in coefficients:
        coefficients[key] = zeros(4)
    coefficients[key][i][j] += value


def base_grams(j, reference):
    """Own H_j Gram and mixed <H_j,H_reference> under rho0(1+m_j S).

    H_j=(1,S,K_j S,K_j^2 S).  Reversibility/stationarity give the
    displayed endpoint-moment formulas, even for imbalanced rho0.
    """
    m = FIELDS[j]
    own, cross = {}, {}
    for a in range(4):
        for b in range(4):
            if a == b == 0:
                for target in (own, cross):
                    insert(target, "constant", a, b)
                    insert(target, "eta", a, b, m)
            elif a == 0 or b == 0:
                insert(own, "eta", a, b)
                insert(own, "constant", a, b, m)
                if b == 0 or b == 1:
                    insert(cross, "eta", a, b)
                    insert(cross, "constant", a, b, m)
                else:
                    word = (reference,) * (b - 1)
                    insert(cross, ("mean", word), a, b)
                    insert(cross, ("correlation", word), a, b, m)
            else:
                word = (j,) * (a + b - 2)
                if word:
                    insert(own, ("correlation", word), a, b)
                    insert(own, ("mean", word), a, b, m)
                else:
                    insert(own, "constant", a, b)
                    insert(own, "eta", a, b, m)
                word = (j,) * (a - 1) + (reference,) * (b - 1)
                if word:
                    insert(cross, ("correlation", word), a, b)
                    insert(cross, ("mean", word), a, b, m)
                else:
                    insert(cross, "constant", a, b)
                    insert(cross, "eta", a, b, m)
    return own, cross


def accumulate(target, key, value):
    target[key] = add(target.get(key, zeros(len(value))), value)


def sign_witness(sign, basis):
    reference, j = (0, 1) if sign == 1 else (1, 0)
    r = (1 - sign * FIELDS[j]) / (1 - sign * FIELDS[reference])
    # Conditional orthogonalization makes the ideal target diagonal.
    v = [[F(1), F(-sign, 3), F(0)],
         [F(0), F(1), F(-1, 3)],
         [F(0), F(0), F(1)]]
    transforms = [matmul([[row[k] for k in (0, 2, 3)] for row in b], v)
                  for b in basis]
    tj, tr = transforms[j], transforms[reference]
    own, cross = base_grams(j, reference)
    ref_own, _ = base_grams(reference, reference)
    coefficients = {}
    for key, a in cross.items():
        b = congruence(a, tj, tr)
        accumulate(coefficients, key, add(b, transpose(b)))
    for key, a in own.items():
        accumulate(coefficients, key, scale(-1, congruence(a, tj)))
    for key, a in ref_own.items():
        accumulate(coefficients, key, scale(-r, congruence(a, tr)))
    check(f"sign {sign:+d}:symmetric-witness-coefficients",
          all(a == transpose(a) for a in coefficients.values()))
    return coefficients, reference


def general_data(basis):
    """Observable factorization through d states; assumes no reversibility."""
    coefficients = {}
    for a in range(4):
        for b in range(4):
            if a == b == 0:
                insert(coefficients, "constant", a, b)
            elif b == 0:
                insert(coefficients, "eta", a, b)
            elif a == 0:
                word = (0,) * (b - 1)
                insert(coefficients, ("mean", word) if word else "eta", a, b)
            else:
                word = (0,) * (a + b - 2)
                insert(coefficients, ("correlation", word) if word else "constant", a, b)
    v = [[F(1), F(0), F(0), F(0)],
         [F(0), F(1), F(-1, 3), F(0)],
         [F(0), F(0), F(1), F(-1, 3)],
         [F(0), F(0), F(0), F(1)]]
    transform = matmul(basis[0], v)
    return {key: congruence(a, transform) for key, a in coefficients.items()}, 0


def menu_words():
    pure = {(j,) * q for j in range(2) for q in range(1, 5)}
    mixed = {(j,) * a + (1 - j,) * b
             for j in range(2) for a in (1, 2) for b in (1, 2)}
    return pure | mixed


def evaluate_target(coefficients, exponentials):
    n = len(next(iter(coefficients.values())))
    result = zeros(n)
    for key, coefficient in coefficients.items():
        if key == "constant":
            moment = F(1)
        elif key == "eta":
            moment = F(0)
        else:
            kind, word = key
            matrix = eye(4)
            for j in word:
                matrix = matmul(matrix, exponentials[j])
            if kind == "mean":
                moment = matrix[0][1]
            else:
                moment = matrix[1][1] + matrix[2][1] / 3 + matrix[3][1] / 9
        result = add(result, scale(moment, coefficient))
    return result


def tv_lipschitz(coefficients, reference):
    """TV times summed per-word matrix diameter bounds matrix infinity norm."""
    n = len(next(iter(coefficients.values())))
    z = zeros(n)
    words = {key[1] for key in coefficients if isinstance(key, tuple)}
    words.add((reference,))
    check("witness-uses-only-menu-words", words <= menu_words())
    total = F(0)
    for word in words:
        mean = coefficients.get(("mean", word), z)
        correlation = coefficients.get(("correlation", word), z)
        eta = coefficients.get("eta", z) if word == (reference,) else z
        outcomes = [add(add(scale(a, eta), scale(b, mean)), scale(a * b, correlation))
                    for a, b in product((-1, 1), repeat=2)]
        total += max(norm_inf(add(x, scale(-1, y))) for x, y in combinations(outcomes, 2))
    return total


def certify(name, coefficients, reference, exponentials, moment_error):
    center = evaluate_target(coefficients, exponentials)
    tail = moment_error * sum(norm_inf(a) for key, a in coefficients.items()
                              if isinstance(key, tuple))
    lower_margin = diagonal_margin(center) - tail
    lipschitz = tv_lipschitz(coefficients, reference)
    # Rational outward rounding gives short, independently readable report bounds.
    margin_floor = F((lower_margin * 10 ** 9).__floor__(), 10 ** 9)
    lipschitz_ceiling = F((lipschitz * 10 ** 6).__ceil__(), 10 ** 6)
    remaining = margin_floor - DELTA * lipschitz_ceiling
    check(name + ":outward-margin", margin_floor <= lower_margin)
    check(name + ":outward-TV-coefficient", lipschitz_ceiling >= lipschitz)
    check(name + ":positive-after-TV-error", remaining > 0)
    check(name + ":Taylor-witness-error-below-1e-20", tail < F(1, 10 ** 20))
    coarse_bounds = {
        "sign +1 rank >=3": (F("0.44444443"), F(335557)),
        "sign -1 rank >=3": (F("0.29629628"), F(253748)),
        "general rank >=4": (F("0.88888887"), F(56639)),
    }
    coarse_margin, coarse_lipschitz = coarse_bounds[name]
    check(name + ":document-target-margin", lower_margin > coarse_margin)
    check(name + ":document-TV-coefficient", lipschitz < coarse_lipschitz)
    check(name + ":document-bounds-certify-delta", coarse_margin > DELTA * coarse_lipschitz)
    print(f"{name}: certified margin >= {float(margin_floor):.9f}; "
          f"TV coefficient <= {float(lipschitz_ceiling):.6f}; "
          f"remaining margin approx {float(remaining):.10f}")
    return {
        "status": "PASS", "claim": name,
        "target_diagonal_margin_lower": str(margin_floor),
        "TV_matrix_coefficient_upper": str(lipschitz_ceiling),
        "remaining_margin_lower_at_delta": str(remaining),
        "certified_radius_lower": str(margin_floor / lipschitz_ceiling),
        "Taylor_witness_error_upper": "1/100000000000000000000",
        "document_target_diagonal_margin_strict_lower": str(coarse_margin),
        "document_TV_matrix_coefficient_strict_upper": str(coarse_lipschitz),
        "display_only_decimal_radius": float(margin_floor / lipschitz_ceiling),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, input_reports = provenance()
    basis = [[[F(x) for x in row.split()] for row in table] for table in B_TEXT]
    generators = [generator(m) for m in FIELDS]
    check("generator-infinity-norm-at-most-two", all(norm_inf(a) <= 2 for a in generators))
    exponentials = [exp_taylor(a) for a in generators]
    # Taylor remainder <= exp(2)*2^41/41! < 8*2^41/41!.
    # exp(2)<8 follows, e.g., by summing its first four terms and bounding
    # the remaining tail by (2^4/4!)/(1-2/5), yielding 67/9 < 8.
    exponential_error = F(8 * 2 ** (ORDER + 1), factorial(ORDER + 1))
    check("exponential-tail-below-one", exponential_error < 1)
    check("Taylor-matrix-norm-below-nine", all(norm_inf(e) < 9 for e in exponentials))
    # Every word has <=4 factors; exact factors have norm <8 and Taylor
    # factors <9. Telescoping gives <=4*9^3 times the single-factor error.
    # The initial correlation row (0,1,1/3,1/9) has l1 norm <2.
    moment_error = 2 * 4 * 9 ** 3 * exponential_error
    check("sixteen-distinct-settings", len(menu_words()) == 16)
    certificates = []
    for sign in (1, -1):
        coefficients, reference = sign_witness(sign, basis)
        certificates.append(certify(f"sign {sign:+d} rank >=3", coefficients, reference,
                                    exponentials, moment_error))
    coefficients, reference = general_data(basis)
    certificates.append(certify("general rank >=4", coefficients, reference,
                                exponentials, moment_error))
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "dependencies": "Python standard library only",
        "arithmetic": "Exact Fraction arithmetic, rational Taylor enclosures, and rational outward rounding; floats appear only in display summaries",
        "fixture": {"n": 3, "tanh_J": "1/3", "field_tilts": ["0", "1/2"],
                    "clock": "1", "maximum_TV_error": str(DELTA),
                    "settings": 16, "maximum_clock_ticks": 4,
                    "words": ["".join("L" if j == 0 else "R" for j in word)
                              for word in sorted(menu_words(), key=lambda w: (len(w), w))]},
        "rational_basis_tables": B_TEXT,
        "Taylor_order": ORDER,
        "one_factor_exponential_error_upper": str(exponential_error),
        "endpoint_moment_error_upper": str(moment_error),
        "certificates": certificates,
        "conclusion": "At every maximum-menu TV tolerance 0<=delta<=1/1000000, D_all=4 and D_ord=6, using inherited exact upper constructions and the new two-field lower certificates",
        "shared_interface": "One common preparation, deterministic binary readout; ordinary rivals use Gibbs tilts rho_m proportional to rho_0*(1+m*S) and detailed balance; no stationary mass floor or rate ceiling",
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": input_reports,
        "limitations": "This sufficient tolerance is not the optimum approximation distance or an experimental sampling budget. The exact upper realizations and the universal witness argument are in the written proofs. No device feasibility, useful finite-precision advantage, thermodynamic saving, Shannon-memory saving, or path-law equality is established.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PASS: 16 settings, <=4 ticks, two fields, delta=1/1000000; "
          f"every reversible rival needs >=6 states and every Markov rival >=4 -> {args.output}")


if __name__ == "__main__":
    main()
