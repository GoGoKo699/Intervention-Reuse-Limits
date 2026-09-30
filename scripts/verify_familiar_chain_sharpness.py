#!/usr/bin/env python3
"""Exact certificates for the fixed-coupling reversible 2n-state construction.

Finite symbolic and algebraic checks supplement the bound all-length proof.
The certificate uses no floating-point dynamics, optimizer or observations.
"""
import argparse
from functools import lru_cache
import hashlib
from math import isqrt
import json
from pathlib import Path
import platform

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_chain.json":
        "95fddbbdfe22d3d62cb6802e3d5491f3d8826aede5ddbeb3be285c2984265b0e"
}
PROOFS = {
    "docs/FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md":
        "849800074af4cf6e5ba33e1f0ec36286221bb9599d3d8aa444af00c0695469ef",
    "docs/FAMILIAR_CHAIN_FINITE_ACCURACY.md":
        "3d4fc44453ba18b595c8be13350e2fe66fb38da1e8ec0e3413a6ebdbc53d3480"
}
THETA = sp.Rational(1, 6)


class Checks:
    def __init__(self):
        self.labels = []

    def check(self, label, condition):
        if condition is not True and condition is not sp.true:
            raise AssertionError((label, condition))
        self.labels.append(label)

    def zero(self, label, expression):
        value = sp.cancel(expression)
        self.check(label, value == 0)

    def matrix_zero(self, label, matrix):
        if isinstance(matrix, DomainMatrix):
            self.check(label, matrix.is_zero_matrix)
        else:
            self.check(label, all(sp.cancel(v) == 0 for v in matrix))

    def report(self):
        return {"status": "PASS", "exact_checks": len(self.labels),
                "checks": self.labels}


def provenance():
    checks = Checks()
    sources, proofs, reports = {}, {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT / name).read_bytes()
        checks.check("input-hash:" + name,
                     hashlib.sha256(payload).hexdigest() == expected)
        inherited = json.loads(payload)
        checks.check("input-status:" + name, inherited["status"] == "PASS")
        reports[name] = expected
        for source, digest in inherited["source_sha256"].items():
            checks.check("source-hash:" + source,
                         hashlib.sha256((ROOT / "scripts" / source).read_bytes()).hexdigest()
                         == digest)
            sources[source] = digest
        for path, digest in inherited["proof_snapshot_sha256"].items():
            checks.check("inherited-proof-hash:" + path,
                         hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
            proofs[path] = digest
        for path, digest in inherited.get("input_report_sha256", {}).items():
            checks.check("inherited-report-hash:" + path,
                         hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
            reports[path] = digest
    checks.check("inherited-proof-count", len(proofs) == 38)
    for path, digest in PROOFS.items():
        checks.check("new-proof-hash:" + path,
                     hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    checks.check("total-proof-count", len(proofs) == 40)
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports, checks.report()


def physical_matrices(n, t, m):
    den = 1 - t*t*m*m
    A = m*(1-t*t)/den
    B = t*(1-m*m)/den
    c = t/(1+t*t)
    K = sp.zeros(n)
    K[0, 1] = B
    K[n-1, n-2] = t
    for j in range(1, n-1):
        K[j, j-1] = K[j, j+1] = c
    T = sp.Matrix([t**j for j in range(n)])
    C = sp.Matrix(n, n, lambda i, j: t**abs(i-j))
    L = sp.Matrix(n, n, lambda i, j:
                  t**i if j == 0 else
                  (sp.sqrt(1-t*t)*t**(i-j) if j <= i else 0))
    return A, B, K, T, C, L


def whitened_checks():
    checks = Checks()
    t, m = sp.symbols("t m", real=True)
    d = 1-t*t
    den = 1-t*t*m*m
    c = t/(1+t*t)
    for n in range(3, 9):
        A, B, K, T, C, L = physical_matrices(n, t, m)
        # Independently use the bidiagonal inverse, not a symbolic dense inverse.
        Linv = sp.zeros(n)
        Linv[0, 0] = 1
        for j in range(1, n):
            Linv[j, j] = 1/sp.sqrt(d)
            Linv[j, j-1] = -t/sp.sqrt(d)
        D = sp.diag(1-m*m, *([1]*(n-1)))
        R = C-m*m*T*T.T
        checks.matrix_zero(f"n={n}:cholesky", L*L.T-C)
        checks.matrix_zero(f"n={n}:bidiagonal-inverse", Linv*L-sp.eye(n))
        checks.matrix_zero(f"n={n}:centered-covariance", L*D*L.T-R)
        checks.matrix_zero(f"n={n}:stationary-means",
                           sp.Matrix([A]+[0]*(n-1))+(-sp.eye(n)+K)*(m*T))
        checks.matrix_zero(f"n={n}:covariance-self-adjoint", K*R-R*K.T)
        H = (Linv*K*L).T*sp.diag(1/(1-m*m), *([1]*(n-1)))
        expected = sp.zeros(n)
        expected[0, 0] = t*t/den
        expected[0, 1] = expected[1, 0] = t*sp.sqrt(d)/den
        expected[1, 1] = -t**4/(1+t*t)+t*t*d*m*m/den
        expected[n-1, n-1] = -t*c
        for j in range(1, n-1):
            expected[j, j+1] = expected[j+1, j] = c
        checks.matrix_zero(f"n={n}:whitened-drift", H-expected)
        checks.matrix_zero(f"n={n}:whitened-symmetry", H-H.T)
        J = sp.zeros(n)
        J[0, 1] = J[1, 0] = 1/sp.sqrt(2)
        for j in range(1, n-1):
            J[j, j+1] = J[j+1, j] = sp.Rational(1, 2)
        E = expected-2*c*J
        allowed = {(0, 0), (0, 1), (1, 0), (1, 1), (n-1, n-1)}
        checks.check(f"n={n}:boundary-perturbation-support",
                     all(sp.cancel(E[i, j]) == 0
                         for i in range(n) for j in range(n) if (i, j) not in allowed))
        checks.zero(f"n={n}:first-offdiagonal-remainder",
                    E[0, 1]-(t*sp.sqrt(d)/den-sp.sqrt(2)*c))
    result = checks.report()
    result.update({"symbolic_lengths": list(range(3, 9)),
                   "free_parameters": ["t", "m"],
                   "scope": "Free-symbol covariance, whitening and boundary-support identities."})
    return result


def positivity_constants():
    checks = Checks()
    q = sp.Rational
    t, m, n = sp.symbols("t m n", real=True)
    den = 1-t*t*m*m
    B = t*(1-m*m)/den
    checks.zero("endpoint-row-sum-bound-factor", t-B-t*m*m*(1-t*t)/den)
    checks.zero("interior-row-sum-bound-factor",
                2*t-2*t/(1+t*t)-2*t**3/(1+t*t))
    checks.zero("denominator-bound-value", 1-q(1, 4)**2*q(1, 2)**2-q(63, 64))
    checks.check("H00-coefficient", q(16, 63) < q(1, 3))
    checks.check("H01-coefficient", q(64, 63) < q(4, 3))
    checks.check("H11-coefficient", q(1, 64)+q(4, 63) < q(1, 12))
    checks.check("sqrt-two-bound", q(3, 2)**2 > 2)
    checks.zero("boundary-entry-sum",
                q(1, 3)+2*(q(4, 3)+q(3, 2))+q(1, 12)+q(1, 4)-q(19, 3))
    checks.zero("first-column-sum", q(1, 3)+q(4, 3)-q(5, 3))
    checks.zero("epsilon-coefficient",
                2*q(19, 3)+2*q(1, 2)*q(3, 2)*q(5, 3)+q(1, 2)**2*q(1, 3)-q(61, 4))
    checks.check("epsilon-less-than-16t", q(61, 4) < 16)
    checks.zero("same-sign-baseline-minimum", 1-THETA*3-q(1, 2))
    checks.zero("opposite-sign-different-node-baseline", 1-THETA-q(5, 6))
    checks.zero("opposite-sign-same-node-baseline", 1-THETA+THETA*n-(n+5)/6)
    checks.zero("different-node-positive-bracket", q(1, 2)-16*q(1, 64)-q(1, 4))
    checks.zero("same-node-positive-bracket-decomposition",
                n*(THETA-2*q(1, 64))+q(5, 6)-16*q(1, 64)
                -(q(13, 96)*(n-3)+q(95, 96)))
    checks.check("same-node-bound-exceeds-quarter", q(95, 96) > q(1, 4))
    checks.zero("rate-floor", q(1, 4)*q(1, 4)-q(1, 16))
    checks.zero("physical-spectral-lower-bound", 1-2*q(1, 64)-q(31, 32))
    checks.zero("exit-rate-cap", 1+2*q(1, 64)-q(33, 32))
    checks.check("complement-spectrum-in-cap", 0 < 1-THETA < 1)
    result = checks.report()
    result.update({"intermediate_domain": "0<t<=1/4, |m|<=1/2",
                   "final_domain": "n>=3, 0<t<=1/64, |m|<=1/2",
                   "epsilon_coefficient": "61/4 < 16",
                   "offdiagonal_rate_floor": "1/(16*n)",
                   "exit_rate_cap": "1+2*t <= 33/32",
                   "scope": "Exact factor identities and rational constants used by the analytical inequalities; no grid sampling."})
    return result


def truncation_checks():
    checks = Checks()
    t, m, xleft, xnext = sp.symbols("t m xleft xnext", real=True)
    c = t/(1+t*t)
    checks.zero("hidden-box-interior-recurrence", c*(1+t*t)-t)
    checks.zero("terminal-drift-forcing",
                c*(xleft+xnext)-t*xleft-c*(xnext-t*t*xleft))
    B = t*(1-m*m)/(1-t*t*m*m)
    checks.zero("passive-drift-comparison-factor",
                t-B-t*m*m*(1-t*t)/(1-t*t*m*m))
    checks.zero("interior-stability-factor", 1-2*c-(1-t)**2/(1+t*t))
    for ell in range(2, 9):
        _, _, K, _, _, _ = physical_matrices(ell, t, sp.Integer(0))
        negative_drift = sp.eye(ell)-K
        endpoint_source = sp.zeros(ell, 1)
        endpoint_source[ell-1] = 1
        green_column = sp.Matrix([t**(ell-1-j)/(1-t*t) for j in range(ell)])
        checks.matrix_zero(f"ell={ell}:full-Green-column",
                           negative_drift*green_column-endpoint_source)
        checks.zero(f"ell={ell}:inverse-endpoint-entry",
                    negative_drift.inv()[0, ell-1]-t**(ell-1)/(1-t*t))
        checks.zero(f"ell={ell}:terminal-hidden-box", t*t**(ell-2)-t**(ell-1))
        checks.zero(f"ell={ell}:pair-TV-bound",
                    (2*c*t**ell)*(t**(ell-1)/(1-t*t))/2
                    -t**(2*ell)/(1-t**4))
    nominal = sp.Rational(1, 64**4-1)
    checks.zero("four-state-accuracy-value",
                sp.Rational(1, 64)**4/(1-sp.Rational(1, 64)**4)-nominal)
    checks.check("four-state-accuracy-less-than-6e-8", nominal < sp.Rational(6, 10**8))
    checks.zero("stronger-coupling-two-spin-bound",
                sp.Rational(1, 3)**4/(1-sp.Rational(1, 3)**4)-sp.Rational(1, 80))
    result = checks.report()
    result.update({"truncation_lengths": list(range(2, 9)),
                   "theorem_domain": "0<t<1, 2<=ell<n, arbitrary finite signed fields and horizons",
                   "uniform_endpoint_pair_TV_bound": "t**(2*ell)/(1-t**4)",
                   "four_state_bound_at_t_le_1_over_64": "1/16777215 < 6/100000000",
                   "upper_bound_on_certifiable_2n_state_tolerance": "t**(2*n-2)/(1-t**4)",
                   "scope": "Exact hidden-box, discrepancy forcing, and Green-function identities supporting the analytical uniform-in-word comparison."})
    return result


@lru_cache(maxsize=None)
def radical_interval(expression, bits):
    """Enclose a real radical expression using rational arithmetic only."""
    expression = sp.sympify(expression)
    if expression.is_Rational:
        return expression, expression
    if expression.is_Add:
        pieces = [radical_interval(v, bits) for v in expression.args]
        return sum(v[0] for v in pieces), sum(v[1] for v in pieces)
    if expression.is_Mul:
        lower = upper = sp.Integer(1)
        for value in expression.args:
            lo, hi = radical_interval(value, bits)
            products = [lower*lo, lower*hi, upper*lo, upper*hi]
            lower, upper = min(products), max(products)
        return lower, upper
    if expression.is_Pow:
        base, power = expression.args
        lo, hi = radical_interval(base, bits)
        if power == sp.Rational(1, 2):
            if lo < 0:
                raise AssertionError(("negative square-root interval", expression))
            scale = 1 << bits

            def lower_root(value):
                return sp.Rational(isqrt((int(value.p)*scale*scale)//int(value.q)), scale)

            lower, upper = lower_root(lo), lower_root(hi)
            if upper*upper != hi:
                upper += sp.Rational(1, scale)
            return lower, upper
        if power.is_Integer:
            k = int(power)
            if k < 0:
                if lo <= 0 <= hi:
                    raise AssertionError(("interval includes inverse singularity", expression))
                lo, hi = 1/hi, 1/lo
                k = -k
            lower = upper = sp.Integer(1)
            for _ in range(k):
                products = [lower*lo, lower*hi, upper*lo, upper*hi]
                lower, upper = min(products), max(products)
            return lower, upper
    raise AssertionError(("unsupported exact interval expression", expression))


def positive_radical(expression):
    for bits in (32, 64, 128, 256, 512):
        lo, _ = radical_interval(expression, bits)
        if lo > 0:
            return bits
    raise AssertionError(("positive radical not certified", expression))


def dct_fixture(n, t, fields):
    checks = Checks()
    if n == 3:
        domain = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(3), sp.sqrt(455))
    elif n == 4:
        domain = sp.QQ.algebraic_field(sp.sqrt(2), sp.sqrt(2+sp.sqrt(2)))
    else:
        raise ValueError("Only the explicitly bounded n=3,4 algebraic fixtures are used")

    def dm(matrix):
        return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(domain)

    def scale(matrix, value):
        return matrix.scalarmul(domain.convert(value))

    def eq(label, left, right):
        checks.matrix_zero(label, left-right)

    W_expr = sp.Matrix(n, n, lambda i, k:
                       1 if k == 0 else
                       sp.sqrt(2)*sp.cos(sp.pi*(2*i+1)*k/(2*n)))
    W = dm(W_expr)
    A, B, K, T_expr, C_expr, L_expr = physical_matrices(n, t, sp.Integer(0))
    L, C, T = dm(L_expr), dm(C_expr), dm(T_expr)
    identity_n = DomainMatrix.eye(n, domain)
    V = W*L.transpose()
    X_expr = V.to_Matrix().col_join(-V.to_Matrix())
    X = dm(X_expr)
    dimension = 2*n
    identity = DomainMatrix.eye(dimension, domain)
    one = dm(sp.ones(dimension, 1))
    zero = dm(sp.zeros(dimension, 1))
    rho0 = dm(sp.ones(1, dimension)/(2*n))
    J_expr = sp.zeros(n)
    J_expr[0, 1] = J_expr[1, 0] = 1/sp.sqrt(2)
    for j in range(1, n-1):
        J_expr[j, j+1] = J_expr[j+1, j] = sp.Rational(1, 2)
    cosines = dm(sp.diag(*[sp.cos(sp.pi*(2*i+1)/(2*n)) for i in range(n)]))
    eq("DCT-column-orthogonality", W.transpose()*W, scale(identity_n, n))
    eq("DCT-row-orthogonality", W*W.transpose(), scale(identity_n, n))
    eq("DCT-Jacobi-diagonalization", W*dm(J_expr)*W.transpose(), scale(cosines, n))
    eq("simplex-conditional-mean", scale(dm(sp.ones(1, n))*V, sp.Rational(1, n)), T.transpose())
    eq("simplex-second-moment", scale(V.transpose()*V, sp.Rational(1, n)), C)
    eq("simplex-inverse-Gram", V*C.inv()*V.transpose(), scale(identity_n, n))
    eq("common-initial-means", rho0*X, dm(sp.zeros(1, n)))
    eq("initial-sign-cross-moments", rho0*dm(sp.diag(*X_expr[:, 0]))*X, T.transpose())
    for sign, block in [(1, V), (-1, scale(V, -1))]:
        eq(f"conditional-initial-means:{sign}",
           scale(dm(sp.ones(1, n))*block, sp.Rational(1, n)), scale(T.transpose(), sign))

    fixture_fields = []
    for m in fields:
        label = f"m={m}:"
        A, B, K_expr, _, _, _ = physical_matrices(n, t, m)
        K = dm(K_expr)
        a = dm(sp.Matrix([[A]+[0]*(n-1)]))
        rho_expr = sp.Matrix([[(1+m*s)/(2*n) for s in (1, -1) for _ in range(n)]])
        rho = dm(rho_expr)
        Drho = dm(sp.diag(*rho_expr))
        Y = X-scale(one*T.transpose(), m)
        R = C-scale(T*T.transpose(), m*m)
        Rinv = R.inv()
        Pi = one*rho
        P = Y*Rinv*Y.transpose()*Drho
        Pperp = identity-Pi-P
        Q = -identity+Pi+Y*K.transpose()*Rinv*Y.transpose()*Drho+scale(Pperp, THETA)
        eq(label+"normalization", rho*one, dm([[1]]))
        eq(label+"tilted-means", rho*X, scale(T.transpose(), m))
        eq(label+"raw-covariance", X.transpose()*Drho*X, C)
        eq(label+"centered-covariance", Y.transpose()*Drho*Y, R)
        eq(label+"mean-centering", rho*Y, dm(sp.zeros(1, n)))
        eq(label+"constant-projector", Pi*Pi, Pi)
        eq(label+"mean-projector", P*P, P)
        eq(label+"complement-projector", Pperp*Pperp, Pperp)
        eq(label+"constant-mean-orthogonality", Pi*P, dm(sp.zeros(dimension)))
        eq(label+"mean-complement-orthogonality", P*Pperp, dm(sp.zeros(dimension)))
        eq(label+"complement-annihilates-constants", Pperp*one, zero)
        eq(label+"complement-annihilates-coordinates", Pperp*Y, dm(sp.zeros(dimension, n)))
        eq(label+"mean-projector-self-adjoint", Drho*P, P.transpose()*Drho)
        eq(label+"complement-self-adjoint", Drho*Pperp, Pperp.transpose()*Drho)
        eq(label+"row-sums", Q*one, zero)
        eq(label+"stationarity", rho*Q, dm(sp.zeros(1, dimension)))
        eq(label+"detailed-balance", Drho*Q, Q.transpose()*Drho)
        eq(label+"full-affine-closure", Q*X, one*a+X*(-identity_n+K).transpose())
        eq(label+"complement-eigenvalue", Q*Pperp, scale(Pperp, -1+THETA))
        ell_expr = sp.Matrix(dimension, dimension, lambda i, j:
                             (1 if i < n else -1)*(1 if j < n else -1)
                             *(n*int(i % n == j % n)-1)
                             +((1 if i < n else -1)-m)*((1 if j < n else -1)-m)/(1-m*m))
        eq(label+"simplex-centered-inner-products", Y*Rinv*Y.transpose(), dm(ell_expr))
        q_expr = Q.to_Matrix()
        maximum_bits = 0
        rates = 0
        for i in range(dimension):
            for j in range(dimension):
                if i != j:
                    maximum_bits = max(maximum_bits,
                                       positive_radical(q_expr[i, j]-sp.Rational(1, 16*n)))
                    rates += 1
            maximum_bits = max(maximum_bits,
                               positive_radical(1+2*t+q_expr[i, i]))
        checks.check(label+"all-offdiagonals-exceed-proved-floor", rates == dimension*(dimension-1))
        checks.check(label+"all-exits-below-spectral-cap", maximum_bits <= 512)
        fixture_fields.append({"m": str(m), "offdiagonal_rates_checked": rates,
                               "exit_rates_checked": dimension,
                               "rational_interval_precision_bits": maximum_bits})
    result = checks.report()
    result.update({"n": n, "states": dimension, "t": str(t),
                   "algebraic_field_degree": int(domain.mod.degree()),
                   "fields": fixture_fields,
                   "rate_floor": f"1/{16*n}", "exit_cap": str(1+2*t),
                   "scope": "Actual discrete-cosine nodes and full exact generator; positivity uses rational radical enclosures."})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, input_reports, provenance_report = provenance()
    whitened = whitened_checks()
    constants = positivity_constants()
    truncation = truncation_checks()
    fixtures = [dct_fixture(3, sp.Rational(1, 64), [sp.Rational(-1, 2), sp.Rational(1, 2)]),
                dct_fixture(4, sp.Rational(256, 16385), [sp.Rational(-1, 2), sp.Rational(1, 2)])]
    count = (provenance_report["exact_checks"]+whitened["exact_checks"]
             +constants["exact_checks"]+truncation["exact_checks"]
             +sum(f["exact_checks"] for f in fixtures))
    report = {
        "status": "PASS", "checks": count,
        "versions": {"python": platform.python_version(), "sympy": sp.__version__},
        "arithmetic": "Exact symbolic, rational, and algebraic arithmetic, including rational radical enclosures; no floats, optimizer, or simulated observations",
        "theorem_domain": "n>=3, 0<t<=1/64, |m|<=1/2",
        "construction_state_count": "2*n",
        "shared_interface": "One deterministic binary readout and common preparation; rho_m=rho_0*(1+m*S)",
        "matching_scope": "All controlled initial/final pair laws for arbitrary finite field words and positive dwell times",
        "sharpness_scope": "On the inherited finite menu with three distinct nonnegative tilts <=1/2: D_all=n+1 and D_ord=2*n. Choosing the lowest tilt zero gives the inherited common explicit positive TV radius.",
        "new_largest_matrix_dimension": 8,
        "largest_matrix_dimension_including_inherited": 9,
        "whitened_drift": whitened,
        "uniform_positivity_constants": constants,
        "finite_accuracy_truncation": truncation,
        "discrete_cosine_fixtures": fixtures,
        "provenance": provenance_report,
        "source_sha256": sources,
        "proof_snapshot_sha256": proofs,
        "input_report_sha256": input_reports,
        "limitations": "Finite fixtures supplement the analytical all-length proofs. The sufficient coupling constant is not optimal. At t<=1/64, four reversible states approximate every length's endpoint data within 1/16777215; certifying the exact 2*n reversible count requires a tolerance no larger than t**(2*n-2)/(1-t**4). No uniform-in-length accuracy separation, practical sample count, hardware realization, dissipation saving, Shannon-entropy saving, physical-bit saving, or full-path equality is established."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(f"PASS: {count} exact familiar-chain sharpness checks -> {args.output}")


if __name__ == "__main__":
    main()
