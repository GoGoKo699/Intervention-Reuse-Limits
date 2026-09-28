#!/usr/bin/env python3
"""Exact two-field cross-rank certificate at endpoint-pair TV error 2e-6.

Uses the unchanged sixteen-setting task. A twelve-setting subset already
certifies both state minima. Opposite control orders determine conditional
cross-Gram matrices directly; their ranks bound states of each visible sign.
All decisions use exact rational arithmetic and explicit Taylor remainders.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from itertools import combinations, product
from math import factorial
from pathlib import Path
import platform

import verify_familiar_chain_accuracy as base

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_chain_accuracy.json":
        "4648f09eb6a900486a1b66cfa8b64568a24299e7fbb473faf80a3d59f0197aec"
}
PROOFS = {'docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md': '04be8e949df054d51e17c3450174807c201a7715bd24fd7f8e9fb40caf1838ef'}
DELTA = F(1, 500_000)
FIVE_STATE_TOLERANCE = F(19, 5_000_000)
FOUR_STATE_TOLERANCE = F(1, 50_000)
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
    check("inherited-proof-count", len(proofs) == 41)
    check("imported-helper-source-is-provenance-bound",
          Path(base.__file__).name in sources)
    for path, digest in PROOFS.items():
        check("new-proof-hash:" + path,
              hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


def subset_words():
    pure = {(j,) * q for j in (0, 1) for q in (1, 2)}
    mixed = {(j,) * a + (1 - j,) * b
             for j in (0, 1) for a in (1, 2) for b in (1, 2)}
    return pure | mixed


def sign_cross_coefficients(sign, basis):
    # At a fixed visible sign, orthogonalized target coordinates are
    # (1, X1-sign/3, X2-X1/3), with Gram diag(1,8/9,8/9).
    v = [[F(1), F(-sign, 3), F(0)],
         [F(0), F(1), F(-1, 3)],
         [F(0), F(0), F(1)]]
    transforms = [base.matmul([[row[k] for k in (0, 2, 3)] for row in b], v)
                  for b in basis]
    left = base.base_grams(0, 1)[1]
    right = base.base_grams(1, 0)[1]
    alpha = (base.FIELDS[1] - sign) / (base.FIELDS[1] - base.FIELDS[0])
    beta = (sign - base.FIELDS[0]) / (base.FIELDS[1] - base.FIELDS[0])
    check(f"sign {sign:+d}:affine-constant-weight", alpha + beta == 1)
    check(f"sign {sign:+d}:affine-sign-weight",
          alpha * base.FIELDS[0] + beta * base.FIELDS[1] == sign)
    coefficients = {}
    for key, matrix in left.items():
        value = base.congruence(matrix, transforms[0], transforms[1])
        base.accumulate(coefficients, key, base.scale(alpha, value))
    for key, matrix in right.items():
        value = base.congruence(base.transpose(matrix), transforms[0], transforms[1])
        base.accumulate(coefficients, key, base.scale(beta, value))
    return coefficients


def general_cross_coefficients(basis):
    # With m_L=0, the raw left cross-data matrix has rows
    # rho0, rho0*S, rho0*S*K_L, rho0*S*K_L^2, and columns
    # 1, S, K_R*S, K_R^2*S. This factorization needs no reversibility.
    check("general-data-low-field-is-zero", base.FIELDS[0] == 0)
    v = [[F(1), F(0), F(0), F(0)],
         [F(0), F(1), F(-1, 3), F(0)],
         [F(0), F(0), F(1), F(-1, 3)],
         [F(0), F(0), F(0), F(1)]]
    transforms = [base.matmul(b, v) for b in basis]
    raw = base.base_grams(0, 1)[1]
    return {key: base.congruence(matrix, transforms[0], transforms[1])
            for key, matrix in raw.items()}


def certify(name, coefficients, exponentials, moment_error, coarse_lipschitz):
    used = {key[1] for key in coefficients if isinstance(key, tuple)}
    check(name + ":uses-only-twelve-setting-subset", used <= subset_words())
    center = base.evaluate_target(coefficients, exponentials)
    tail = moment_error * sum(base.norm_inf(a) for key, a in coefficients.items()
                              if isinstance(key, tuple))
    margin = base.diagonal_margin(center) - tail
    lipschitz = base.tv_lipschitz(coefficients, 0)
    coarse_margin = F("0.88888887")
    check(name + ":target-diagonal-margin", margin > coarse_margin)
    check(name + ":TV-coefficient", lipschitz < coarse_lipschitz)
    check(name + ":positive-at-delta", coarse_margin > DELTA * coarse_lipschitz)
    check(name + ":Taylor-witness-error-below-1e-20", tail < F(1, 10 ** 20))
    # Outward rounding keeps report comparisons short and fully rational.
    lower = F((margin * 10 ** 9).__floor__(), 10 ** 9)
    upper = F((lipschitz * 10 ** 6).__ceil__(), 10 ** 6)
    check(name + ":outward-margin", lower <= margin)
    check(name + ":outward-TV-coefficient", upper >= lipschitz)
    check(name + ":positive-outward-margin", lower > DELTA * upper)
    print(f"{name}: margin >= {float(lower):.9f}, TV coefficient <= "
          f"{float(upper):.6f}, remaining approximately {float(lower-DELTA*upper):.9f}")
    return {
        "status": "PASS", "claim": name,
        "target_diagonal_margin_lower": str(lower),
        "TV_matrix_coefficient_upper": str(upper),
        "remaining_margin_lower_at_delta": str(lower - DELTA * upper),
        "certified_radius_lower": str(lower / upper),
        "document_target_margin_strict_lower": str(coarse_margin),
        "document_TV_coefficient_strict_upper": str(coarse_lipschitz),
        "Taylor_witness_error_upper": "1/100000000000000000000",
        "display_only_decimal_radius": float(lower / upper),
        "settings_used": len(used),
    }


def spectral_safe_bound(matrix):
    # ||M||_2 <= sqrt(||M||_1 ||M||_infinity) <= max of these two norms.
    return max(base.norm_inf(matrix), base.norm_inf(base.transpose(matrix)))


def positive_leading_minors(matrix):
    """Sylvester criterion, exact, for symmetric matrices of order <=3."""
    if matrix[0][0] <= 0:
        return False
    if len(matrix) == 1:
        return True
    if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] <= 0:
        return False
    if len(matrix) == 2:
        return True
    a = matrix
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])) > 0


def spectral_norm_upper(matrix):
    """Rational q with q^2 I-M^T M positive definite, certified exactly."""
    dimension = len(matrix)
    check("spectral-norm-matrix-order-at-most-three", 1 <= dimension <= 3)
    square = base.matmul(base.transpose(matrix), matrix)

    def good(q):
        test = base.add(base.scale(q * q, base.eye(dimension)), base.scale(-1, square))
        return positive_leading_minors(test)

    lower, upper = F(0), spectral_safe_bound(matrix) + 1
    check("spectral-norm-initial-upper", good(upper))
    while upper - lower > F(1, 1000):
        middle = (lower + upper) / 2
        if good(middle):
            upper = middle
        else:
            lower = middle
    check("spectral-norm-final-upper", good(upper))
    return upper


def spectral_tv_coefficient(coefficients):
    dimension = len(next(iter(coefficients.values())))
    zero = base.zeros(dimension)
    words = {key[1] for key in coefficients if isinstance(key, tuple)}
    words.add((0,))
    check("spectral-witness-uses-twelve-setting-subset", words <= subset_words())
    total = F(0)
    for word in sorted(words):
        mean = coefficients.get(("mean", word), zero)
        correlation = coefficients.get(("correlation", word), zero)
        eta = coefficients.get("eta", zero) if word == (0,) else zero
        outcomes = [base.add(base.add(base.scale(a, eta), base.scale(b, mean)),
                             base.scale(a * b, correlation))
                    for a, b in product((-1, 1), repeat=2)]
        total += max(spectral_norm_upper(base.add(x, base.scale(-1, y)))
                     for x, y in combinations(outcomes, 2))
    return total


def phase_rank_certificate(sign, dimension, basis, exponentials, moment_error,
                           tolerance=FIVE_STATE_TOLERANCE):
    coefficients = sign_cross_coefficients(sign, basis)
    transform = base.eye(dimension)
    for i in range(1, dimension):
        transform[i][i] = F(17, 16)
    coefficients = {key: base.congruence([row[:dimension] for row in matrix[:dimension]],
                                         transform)
                    for key, matrix in coefficients.items()}
    center = base.evaluate_target(coefficients, exponentials)
    nominal = base.eye(dimension)
    for i in range(1, dimension):
        nominal[i][i] = F(289, 288)
    residual = base.add(center, base.scale(-1, nominal))
    tail = moment_error * sum(spectral_safe_bound(matrix) for key, matrix in coefficients.items()
                              if isinstance(key, tuple))
    # The smallest singular value of nominal is one. No symmetry of the
    # actual cross matrix, center residual, or perturbation is presumed.
    singular_lower = 1 - spectral_safe_bound(residual) - tail
    coefficient_upper = spectral_tv_coefficient(coefficients)
    coarse_margin = F("0.99999998")
    coarse_coefficient = F({(1, 3): 258772, (1, 2): 10377, (-1, 2): 14707}[(sign, dimension)])
    label = f"tolerance {tolerance}:sign {sign:+d}:rank>={dimension}"
    check(label + ":target-smallest-singular-value", singular_lower > coarse_margin)
    check(label + ":spectral-TV-coefficient", coefficient_upper < coarse_coefficient)
    check(label + ":positive-at-phase-tolerance",
          coarse_margin > tolerance * coarse_coefficient)
    print(f"{label}: singular margin > {coarse_margin}, TV coefficient < "
          f"{coarse_coefficient}, rank survives TV={tolerance}")
    return {"status": "PASS", "sign": sign, "rank_lower": dimension,
            "target_smallest_singular_value_strict_lower": str(coarse_margin),
            "spectral_TV_coefficient_strict_upper": str(coarse_coefficient),
            "remaining_singular_margin_strict_lower":
                str(coarse_margin - tolerance * coarse_coefficient),
            "spectral_norm_certification": "Rational bisection to width 1/1000; positivity of q^2*I-M^T*M checked by exact leading principal minors",
            "diagonal_preconditioner": ["1"] + ["17/16"] * (dimension - 1)}


def word_names(words):
    return ["".join("L" if j == 0 else "R" for j in word)
            for word in sorted(words, key=lambda word: (len(word), word))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    check("twelve-settings", len(subset_words()) == 12)
    check("subset-of-unchanged-sixteen-setting-task", subset_words() < base.menu_words())
    check("same-two-fields", base.FIELDS == (F(0), F(1, 2)))
    check("same-Taylor-order", base.ORDER == 40)
    basis = [[[F(x) for x in row.split()] for row in table] for table in base.B_TEXT]
    generators = [base.generator(m) for m in base.FIELDS]
    check("generator-norm-at-most-two", all(base.norm_inf(a) <= 2 for a in generators))
    exponentials = [base.exp_taylor(a) for a in generators]
    exponential_error = F(8 * 2 ** 41, factorial(41))
    check("exponential-error-below-one", exponential_error < 1)
    check("Taylor-matrix-norm-below-nine", all(base.norm_inf(e) < 9 for e in exponentials))
    # exp(2)<8. A four-factor product error is <=4*9^3 times the
    # one-factor remainder, and both initial moment rows have l1 norm <2.
    moment_error = 2 * 4 * 9 ** 3 * exponential_error
    certificates = [
        certify("sign +1 rank >=3", sign_cross_coefficients(1, basis),
                exponentials, moment_error, F(264859)),
        certify("sign -1 rank >=3", sign_cross_coefficients(-1, basis),
                exponentials, moment_error, F(392686)),
        certify("general rank >=4", general_cross_coefficients(basis),
                exponentials, moment_error, F(73901)),
    ]
    phase_certificates = [
        phase_rank_certificate(1, 3, basis, exponentials, moment_error),
        phase_rank_certificate(-1, 2, basis, exponentials, moment_error),
    ]
    check("phase-general-rank-at-least-four",
          F("0.88888887") > FIVE_STATE_TOLERANCE * F(73901))
    four_state_certificates = [
        phase_rank_certificate(1, 2, basis, exponentials, moment_error,
                               FOUR_STATE_TOLERANCE),
        phase_rank_certificate(-1, 2, basis, exponentials, moment_error,
                               FOUR_STATE_TOLERANCE),
    ]
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "dependencies": "Python standard library only; imported helper is SHA256-bound",
        "arithmetic": "Exact Fraction arithmetic, explicit rational Taylor remainders, and rational outward rounding; floats only for display summaries",
        "fixture": {"n": 3, "tanh_J": "1/3", "field_tilts": ["0", "1/2"],
                    "clock": "1", "maximum_TV_error": str(DELTA),
                    "original_menu_words": word_names(base.menu_words()),
                    "sufficient_subset_words": word_names(subset_words()),
                    "maximum_clock_ticks": 4},
        "rational_basis_tables": base.B_TEXT,
        "Taylor_order": base.ORDER,
        "one_factor_exponential_error_upper": str(exponential_error),
        "endpoint_moment_error_upper": str(moment_error),
        "certificates": certificates,
        "five_state_phase_lower_certificate": {
            "maximum_TV_error": str(FIVE_STATE_TOLERANCE),
            "ordinary_state_lower": 5, "general_state_lower": 4,
            "interval_supported_with_companion_upper": ["9/2500000", "19/5000000"],
            "sector_certificates": phase_certificates,
            "scope": "On both original sixteen settings and the twelve-setting subset. This is a lower certificate; the separate five-state construction supplies the matching ordinary upper bound. The inherited four-state general model supplies the matching general upper bound.",
        },
        "four_state_phase_lower_certificate": {
            "maximum_TV_error": str(FOUR_STATE_TOLERANCE),
            "ordinary_state_lower": 4,
            "sector_certificates": four_state_certificates,
            "scope": "On both original sixteen settings and the twelve-setting subset. The separate four-state ordinary construction supplies the matching upper bound. No matching general-state lower bound is claimed at this tolerance.",
        },
        "conclusion": "For every maximum-menu TV tolerance 0<=delta<=1/500000, D_all=4 and D_ord=6 on the original sixteen settings and on the displayed twelve-setting subset; exact upper constructions are inherited",
        "shared_interface": "One common preparation and deterministic binary readout; ordinary rivals obey Gibbs tilts rho_m proportional to rho_0*(1+m*S) and detailed balance, with no rate ceiling or stationary mass floor",
        "source_sha256": sources, "proof_snapshot_sha256": proofs,
        "input_report_sha256": reports,
        "limitations": "The lower certificate alone does not determine the optimum approximation error. This report certifies finite matrix enclosures and rank margins; the universal rank factorization is proved in the text. It establishes no useful device precision, practical sample count, dissipation saving, Shannon-memory saving, or full-path equality.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {len(CHECKS)} exact cross-rank checks -> {args.output}")


if __name__ == "__main__":
    main()
