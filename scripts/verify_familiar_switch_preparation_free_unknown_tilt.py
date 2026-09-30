#!/usr/bin/env python3
"""Exact population certificate for seven preparation-free unknown-tilt words.

The universal singleton argument is a written theorem. These checks verify
its polynomial elimination and the target formulas with rational arithmetic.
Finite-sample acquisition has a separate verifier and report.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

import verify_familiar_switch_frozen_bound as target
import verify_familiar_switch_frozen_equivalence as equivalence
import verify_familiar_switch_margin as algebra


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "reports/familiar_switch_frozen_bound.json":
        "3f807fcf2ed4e68f11831966399389475375bf13b3a801e96434e5fb9adfa625",
    "reports/familiar_switch_frozen_equivalence.json":
        "22d4c933c424c81632dceb3a90a221ed18de3c30cda624fd4a21a6f0d9407a30",
}
EXTRA_SOURCES = {
    "verify_familiar_switch_margin.py":
        "e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397",
}
PROOFS = {
    "docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md":
        "a25ea1b3620c80208646c6c2bca11a5f2c4541815261a8378495e165b25a950f",
    "docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md":
        "164619060bf7f5805f77b2da5d2f81387d9defa5e9064f30677ef8ec6d91252b",
}
WORDS = ((0,), (0, 0), (1,), (0, 1), (1, 0), (0, 0, 1), (1, 0, 0))
WORD_NAMES = ("L", "LL", "H", "LH", "HL", "LLH", "HLL")
T, M = F(1, 3), F(7, 9)
CHECKS = []


def check(label, condition):
    if condition is not True:
        raise AssertionError(label)
    CHECKS.append(label)


def provenance():
    sources, proofs, reports = {}, {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        check("input-report-hash:"+name, hashlib.sha256(payload).hexdigest() == expected)
        inherited = json.loads(payload)
        check("input-report-pass:"+name, inherited["status"] == "PASS")
        reports[name] = expected
        for source, digest in inherited["source_sha256"].items():
            check("inherited-source:"+source,
                  hashlib.sha256((ROOT/"scripts"/source).read_bytes()).hexdigest() == digest)
            check("inherited-source-agreement:"+source, source not in sources or sources[source] == digest)
            sources[source] = digest
        for path, digest in inherited["proof_snapshot_sha256"].items():
            check("inherited-proof:"+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
            check("inherited-proof-agreement:"+path, path not in proofs or proofs[path] == digest)
            proofs[path] = digest
        for path, digest in inherited.get("input_report_sha256", {}).items():
            check("inherited-report:"+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
            check("inherited-report-agreement:"+path, path not in reports or reports[path] == digest)
            reports[path] = digest
    for name, expected in EXTRA_SOURCES.items():
        check("extra-source:"+name, hashlib.sha256((ROOT/"scripts"/name).read_bytes()).hexdigest() == expected)
        sources[name] = expected
    for helper in (target, equivalence, algebra):
        check("imported-source-is-bound:"+Path(helper.__file__).name, Path(helper.__file__).name in sources)
    check("both-new-proofs-have-reviewed-hashes", len(PROOFS) == 2 and all(len(v) == 64 for v in PROOFS.values()))
    for path, digest in PROOFS.items():
        check("new-proof:"+path, hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest)
        proofs[path] = digest
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, reports


def witness(returns):
    """F=A1*B2-A2*B1, in WORD_NAMES order; works on exact scalars/polys."""
    low, low2, high, low_high, high_low, low2_high, high_low2 = returns
    a1, b1 = low_high-low*high, high_low-low*high
    a2, b2 = low2_high-low2*high, high_low2-low2*high
    return a1*b2-a2*b1


def witness_polynomial():
    variables = [algebra.Poly.variable(7, index) for index in range(7)]
    result = witness(variables)
    check("witness-is-degree-three-after-quartic-cancellation",
          max(map(sum, result.terms)) == 3)
    check("witness-has-six-nonzero-monomials", len(result.terms) == 6)
    return result


def rounded_interval(value, denominator=10**18):
    lower, upper = value
    lo = F((lower*denominator).__floor__(), denominator)
    hi = F((upper*denominator).__ceil__(), denominator)
    check("outward-rational-enclosure", lo <= lower <= upper <= hi)
    return [str(lo), str(hi)]


def interval_witness(box):
    value = witness([algebra.Interval(lo, hi) for lo, hi in box])
    return value.lo, value.hi


def singleton_polynomial_certificate():
    """Unknown-tilt polynomial fixtures for both singleton orientations.

    This complements, and does not replace, the universal detailed-balance
    proof for arbitrary positive stationary weights in the bound note.
    """
    pi = [F(1, 5), F(3, 10), F(1, 2)]
    variables = [algebra.Poly.variable(7, j) for j in range(7)]
    u, flows = variables[0], variables[1:]
    denominator = 1-u*u
    fixtures = []
    for sign in (-1, 1):
        signs = [sign, -sign, -sign]
        low = [[algebra.Poly(7) for _ in range(3)] for _ in range(3)]
        high_scaled = [[algebra.Poly(7) for _ in range(3)] for _ in range(3)]
        for k, (i, j) in enumerate(((0, 1), (0, 2), (1, 2))):
            low[i][j], low[j][i] = flows[k]/pi[i], flows[k]/pi[j]
            high_scaled[i][j] = flows[3+k]*(1-u*signs[i])/pi[i]
            high_scaled[j][i] = flows[3+k]*(1-u*signs[j])/pi[j]
        for i in range(3):
            low[i][i] = 1-sum(low[i])
            high_scaled[i][i] = denominator-sum(high_scaled[i])
        high_weights = [pi[i]*(1+u*signs[i]) for i in range(3)]
        check(f"singleton-{sign}:low-reversible",
              all(pi[i]*low[i][j] == pi[j]*low[j][i]
                  for i in range(3) for j in range(3)))
        check(f"singleton-{sign}:high-reversible-after-common-clearing",
              all(high_weights[i]*high_scaled[i][j] == high_weights[j]*high_scaled[j][i]
                  for i in range(3) for j in range(3)))
        check(f"singleton-{sign}:stochastic-row-identities",
              all(sum(row) == 1 for row in low)
              and all(sum(row) == denominator for row in high_scaled))
        residuals = []
        for length in (1, 2):
            low_power = low if length == 1 else algebra.mm(low, low)
            check(f"singleton-{sign}:power-{length}-reversible",
                  all(pi[i]*low_power[i][j] == pi[j]*low_power[j][i]
                      for i in range(3) for j in range(3)))
            cross_forward = algebra.mm(low_power, high_scaled)[0][0]
            cross_reverse = algebra.mm(high_scaled, low_power)[0][0]
            product = low_power[0][0]*high_scaled[0][0]
            a, b = cross_forward-product, cross_reverse-product
            check(f"singleton-{sign}:unknown-tilt-duration-{length}-identity",
                  (1-sign*u)*a == (1+sign*u)*b)
            residuals.append((a, b))
        check(f"singleton-{sign}:eliminated-flux-identity",
              residuals[0][0]*residuals[1][1]-residuals[1][0]*residuals[0][1] == 0)
        concrete = [F(2, 5)] + [F(1, 100)]*6
        positive_low = [[entry.evaluate(concrete) for entry in row] for row in low]
        positive_high = [[entry.evaluate(concrete)/(1-concrete[0]**2)
                          for entry in row] for row in high_scaled]
        check(f"singleton-{sign}:strictly-positive-stochastic-fixture",
              all(min(row) > 0 and sum(row) == 1 for row in positive_low+positive_high))
        fixtures.append({"singleton_sign": sign, "low_weights": list(map(str, pi)),
                         "low_imbalance": str(sum(p*s for p, s in zip(pi, signs)))})
    return {"status": "PASS", "symbolic_variable_count": 7,
            "variables": ["unknown tilt", "three low fluxes", "three high fluxes"],
            "high_kernel_common_denominator": "1-u^2",
            "identity": "A_a=((1+s*u)/(1-s*u))*B_a for a=1,2; A_1*B_2-A_2*B_1=0",
            "fixtures": fixtures,
            "scope": "Exact unknown-tilt polynomial fixtures with unbalanced positive stationary weights and both singleton signs. The written universal proof covers all positive stationary laws and all supported state counts at most three."}


def zero_mass_certificate():
    """The eliminated identity also holds at transient zero-weight states."""
    a, b, c, d, e, f, g, hh = [algebra.Poly.variable(8, j) for j in range(8)]
    low = [[1, 0, 0], [1-a-b, a, b], [1-c-d, c, d]]
    high = [[1, 0, 0], [1-e-f, e, f], [1-g-hh, g, hh]]
    zero = algebra.Poly(8)
    pi = [F(1), F(0), F(0)]
    check("zero-mass:positive-support-is-absorbing", low[0] == high[0] == [1, 0, 0])
    check("zero-mass:both-kernels-reversible-for-pi",
          all(pi[i]*low[i][j] == pi[j]*low[j][i]
              and pi[i]*high[i][j] == pi[j]*high[j][i]
              for i in range(3) for j in range(3)))
    returns = []
    for word in WORDS:
        matrix = algebra.identity(3)
        for field in word:
            matrix = algebra.mm(matrix, (low, high)[field])
        returns.append(matrix[1][1])
    a1 = returns[3]-returns[0]*returns[2]
    b1 = returns[4]-returns[0]*returns[2]
    a2 = returns[5]-returns[1]*returns[2]
    b2 = returns[6]-returns[1]*returns[2]
    check("zero-mass:offdiagonal-return-products", a1 == b*g and b1 == f*c)
    check("zero-mass:two-dimensional-transient-Cayley-Hamilton",
          a2 == (a+d)*a1 and b2 == (a+d)*b1)
    check("zero-mass:eliminated-identity-without-transient-DB", witness(returns) == zero)
    # A concrete example deliberately violates the positive-weight Gibbs
    # ratio, so accidentally applying that stronger assertion is caught.
    fixture = [F(1, 2), F(3, 10), F(2, 7), F(4, 7),
               F(1, 3), F(1, 3), F(1, 10), F(1, 2)]
    values = [value.evaluate(fixture) for value in (a1, b1, a2, b2)]
    check("zero-mass:fixture-nonzero-residual-products",
          values == [F(3, 100), F(2, 21), F(9, 280), F(5, 49)])
    check("zero-mass:fixture-not-a-Gibbs-ratio-at-u-zero", values[0] != values[1])
    check("zero-mass:fixture-determinant-zero", values[0]*values[3]-values[2]*values[1] == 0)
    # With only one zero-weight state its transient blocks are scalars.
    single_low = [[1, 0], [1-a, a]]
    single_high = [[1, 0], [1-e, e]]
    single_returns = []
    for word in WORDS:
        matrix = algebra.identity(2)
        for field in word:
            matrix = algebra.mm(matrix, (single_low, single_high)[field])
        single_returns.append(matrix[1][1])
    check("zero-mass:one-transient-state-all-residuals-zero",
          single_returns[3]-single_returns[0]*single_returns[2] == 0
          and single_returns[4]-single_returns[0]*single_returns[2] == 0
          and single_returns[5]-single_returns[1]*single_returns[2] == 0
          and single_returns[6]-single_returns[1]*single_returns[2] == 0)
    return {"status": "PASS", "symbolic_variable_count": 8,
            "stationary_law": ["1", "0", "0"],
            "two_transient_state_identity": "A_2=tr(T_L)*A_1 and B_2=tr(T_L)*B_1",
            "fixture_A1_B1_A2_B2": list(map(str, values)),
            "scope": "All persistent states, including zero-stationary-mass states occupied by preparation, count toward the at-most-three-state null. The usual Gibbs-ratio identity is used only for a positive-weight singleton. The eliminated determinant also vanishes for a zero-weight singleton by the dimension-at-most-two transient-block argument."}


def target_factorization_certificate():
    """Check the generic target factorization after clearing 1-m^2."""
    t, m, high_b, high_c, beta, gamma = [algebra.Poly.variable(6, j) for j in range(6)]
    denominator = 1-m*m
    high_e_numerator = (1-t*t*m*m)*high_c
    high_a = m*(1-high_b-t*high_c)
    high_d_numerator = m*(t*denominator-high_e_numerator-t*high_b*denominator)
    for sign in (-1, 1):
        high_return = (1+sign*high_a+high_b+t*high_c)/2
        residuals = []
        for low_b, low_c in ((beta, gamma), (beta*beta+gamma*gamma, 2*beta*gamma)):
            low_return = (1+low_b+t*low_c)/2
            forward = (1+sign*high_a+high_b*(low_b+t*low_c)
                       +high_c*(low_c+t*low_b))/2
            reverse_scaled = (denominator+sign*(low_b*high_a*denominator+low_c*high_d_numerator)
                              +low_b*denominator*(high_b+t*high_c)
                              +low_c*(high_e_numerator+t*high_b*denominator))/2
            residuals.append((forward-low_return*high_return,
                              reverse_scaled-denominator*low_return*high_return))
        determinant_scaled = residuals[0][0]*residuals[1][1]-residuals[1][0]*residuals[0][1]
        expected = (-sign*m*(1-t*t)*high_c*(1-high_b-t*high_c)*gamma
                    *((1-beta)**2-gamma**2)*denominator/8)
        check(f"target-sign-{sign}:generic-factorization", determinant_scaled == expected)
    return {"status": "PASS", "symbolic_variable_count": 6,
            "cleared_positive_denominator": "1-m^2",
            "generic_domain": "0<t<1, 0<m<1, tau_L>0, tau_H>0",
            "factorization": "F_s=-s*m*(1-t^2)*C*(1-B-t*C)*gamma_1*(1-exp(-(1-t)*tau_L))*(1-exp(-(1+t)*tau_L))/8",
            "high_coefficients": "b=t*(1-m^2)/(1-t^2*m^2), kappa=sqrt(t*b), B=exp(-tau_H)*cosh(kappa*tau_H), C=exp(-tau_H)*b*sinh(kappa*tau_H)/kappa",
            "low_coefficient": "gamma_1=exp(-tau_L)*sinh(t*tau_L)",
            "sign": "F_+<0 and F_->0 throughout the stated open domain"}


def target_certificate():
    """Return (JSON-ready certificate, {sign: seven exact interval tuples})."""
    check("target-helper-parameters", target.T == T and target.M == M)
    check("target-helper-Taylor-order", target.base.ORDER == 40)
    generators = [target.mean_generator(field) for field in (F(0), M)]
    check("target-generator-norm-at-most-two",
          all(target.base.norm_inf(q) <= 2 for q in generators))
    exponentials = [target.base.exp_taylor(q) for q in generators]
    check("target-Taylor-factor-norm-below-nine",
          all(target.base.norm_inf(k) < 9 for k in exponentials))
    check("scalar-exp-two-below-eight",
          1+2+2+F(2**3, factorial(3))/(1-F(2, 4)) < 8)
    # ||exp(Q)-Taylor_40(Q)|| <= exp(2)*2^41/41! < 8*2^41/41!.
    one_factor_error = F(8*2**41, factorial(41))
    # At most three factors: telescoping <=3*9^2*one_factor_error.
    # The conditional initial row (1,s,t*s), followed by division by two,
    # has l1 norm (2+t)/2=7/6. The ceiling 500 exceeds (7/6)*3*81.
    error = 500*one_factor_error
    check("target-three-factor-error-ceiling", F(2+T, 2)*3*9**2 < 500)
    check("target-return-error-below-1e-30", error < F(1, 10**30))
    returns = {-1: [], 1: []}
    word_matrices = {}
    for name, word in zip(WORD_NAMES, WORDS):
        matrix = target.base.eye(3)
        for field in word:
            matrix = target.base.matmul(matrix, exponentials[field])
        word_matrices[name] = matrix
        for sign in (-1, 1):
            value = (1+sign*matrix[0][1]+matrix[1][1]+T*matrix[2][1])/2
            enclosed = value-error, value+error
            check(f"return-{name}-{sign}:strictly-between-zero-and-one", 0 < enclosed[0] < enclosed[1] < 1)
            returns[sign].append(enclosed)
    # Independent enclosure of the displayed product factor using the same
    # certified one-tick matrix entries and the semigroup double-angle law.
    b = target.expand(target.point(exponentials[1][1][1]), one_factor_error)
    c = target.expand(target.point(exponentials[1][2][1]), one_factor_error)
    beta = target.expand(target.point(exponentials[0][1][1]), one_factor_error)
    gamma = target.expand(target.point(exponentials[0][2][1]), one_factor_error)
    high_decay = target.interval_sub(target.point(1), target.interval_add(b, target.interval_scale(c, T)))
    low_decay = target.interval_sub(target.interval_square(target.interval_sub(target.point(1), beta)),
                                    target.interval_square(gamma))
    check("target-factor-positive-intervals", min(c[0], gamma[0], high_decay[0], low_decay[0]) > 0)
    factor = target.point(M*(1-T*T)/8)
    for value in (c, high_decay, gamma, low_decay):
        factor = target.interval_mul(factor, value)
    witnesses = {sign: interval_witness(returns[sign]) for sign in (-1, 1)}
    for sign in (-1, 1):
        expected = target.interval_scale(factor, -sign)
        observed = witnesses[sign]
        check(f"target-sign-{sign}:direct-and-factor-enclosures-overlap",
              max(expected[0], observed[0]) <= min(expected[1], observed[1]))
        check(f"target-sign-{sign}:margin-exceeds-0.0001226906067685",
              (-observed[1] if sign == 1 else observed[0]) > F(1226906067685, 10**16))
    result = {"status": "PASS", "t": str(T), "m": str(M), "tau_L": "1", "tau_H": "1",
              "word_order": list(WORD_NAMES), "initial_sign_probabilities": {"-1": "1/2", "1": "1/2"},
              "Taylor_degree": 40, "per_return_error_upper": str(error),
              "conditional_return_enclosures": {str(sign): [rounded_interval(value) for value in returns[sign]] for sign in (-1, 1)},
              "witness_enclosures": {str(sign): rounded_interval(witnesses[sign]) for sign in (-1, 1)},
              "factor_magnitude_enclosure": rounded_interval(factor),
              "strict_magnitude_lower": "1226906067685/10000000000000000",
              "target_preparation": "Exact low-field equilibrium pi_0(s,z)=(1+t*s*z)/4, so E[Z|S=s]=t*s",
              "scope": "Exact rational matrix-Taylor enclosures, including three-tick words. Generic factorization separately verified as a polynomial identity. No preparation-free target power or sampling count is asserted by this core."}
    return result, returns


CENTERS = {
 -1:tuple(map(F, ['.7150718960301519','.5994462879090425','.4613488889688746','.3519881480346514','.49645109687182737','.3057816566261857','.5024733107309787'])),
 1:tuple(map(F, ['.7150718960301519','.5994462879090425','.9326686111211093','.8233078701868861','.6877442961353613','.7771013787784204','.5873246657617845'])),
}


def derivative(poly, index):
    terms = {}
    for powers, coefficient in poly.terms.items():
        if powers[index]:
            new = list(powers)
            new[index] -= 1
            terms[tuple(new)] = coefficient*powers[index]
    return type(poly)(poly.n, terms)


def rounded_up(value, denominator=10**12):
    return F((value*denominator).__ceil__(), denominator)


def population_robustness_certificate(target_return_boxes):
    polynomial = witness_polynomial()
    radius, center_error = F(1, 1000), F(1, 10**12)
    signal = F(12269, 10**8)
    response_radius, joint_radius = F(3, 20000), F(7, 100000)
    local = {}
    for sign in (-1, 1):
        center = CENTERS[sign]
        for j, ((lo, hi), c) in enumerate(zip(target_return_boxes[sign], center)):
            check(f"local-sign-{sign}:center-enclosure-{j}", c-center_error < lo <= hi < c+center_error)
            check(f"local-sign-{sign}:probability-box-{j}", 0 < c-radius < c+radius < 1)
        center_score = polynomial.evaluate(center)
        check(f"local-sign-{sign}:center-witness-margin",
              center_score > signal if sign == -1 else center_score < -signal)
        shifted = polynomial.shifted(center)
        target_box = shifted.evaluate([algebra.Interval(-center_error, center_error)]*7)
        check(f"local-sign-{sign}:target-witness-margin", target_box.lo > signal if sign == -1 else target_box.hi < -signal)
        shifted_box = [algebra.Interval(-radius, radius)]*7
        derivatives = [derivative(shifted, j) for j in range(7)]
        gradient = [g.evaluate([F(0)]*7) for g in derivatives]
        gradient_boxes = [g.evaluate(shifted_box) for g in derivatives]
        gradient_caps = [max(abs(a.lo), abs(a.hi)) for a in gradient_boxes]
        hessian_sum = F(0)
        for i in range(7):
            for j in range(7):
                value = derivative(derivatives[i], j).evaluate(shifted_box)
                # Identically zero Poly.evaluate returns integer zero.
                lo, hi = (value.lo, value.hi) if hasattr(value, 'lo') else (F(value), F(value))
                hessian_sum += max(abs(lo), abs(hi))
        bernoulli_caps = []
        for c in center:
            lo, hi = c-radius, c+radius
            bernoulli_caps.append(lo*(1-lo) if lo >= F(1, 2) else hi*(1-hi) if hi <= F(1, 2) else F(1, 4))
        variance = sum(g*g*b for g, b in zip(gradient_caps, bernoulli_caps))
        l1_cap = F(67, 100) if sign == -1 else F(4, 5)
        hessian_cap = F(14) if sign == -1 else F(18)
        variance_cap = F(11, 500) if sign == -1 else F(7, 250)
        check(f"local-sign-{sign}:gradient-l1-cap", sum(gradient_caps) < l1_cap)
        check(f"local-sign-{sign}:absolute-Hessian-entry-sum-cap", hessian_sum < hessian_cap)
        check(f"local-sign-{sign}:Bernoulli-score-variance-cap", variance < variance_cap)
        check(f"local-sign-{sign}:scalar-increment-cap", max(gradient_caps) < F(23, 100))
        local[str(sign)] = {
            "center": list(map(str, center)), "center_score": str(polynomial.evaluate(center)),
            "gradient_at_center": list(map(str, gradient)),
            "gradient_absolute_component_upper": [str(rounded_up(x)) for x in gradient_caps],
            "gradient_l1_upper": str(rounded_up(sum(gradient_caps))), "gradient_l1_cap": str(l1_cap),
            "Hessian_absolute_entry_sum_upper": str(rounded_up(hessian_sum)), "Hessian_absolute_entry_sum_cap": str(hessian_cap),
            "Bernoulli_linear_variance_sum_upper": str(rounded_up(variance)), "Bernoulli_linear_variance_sum_cap": str(variance_cap),
            "centered_single_return_increment_cap": "23/100",
        }
    check("conditional-return-ball-inside-local-box", response_radius+center_error < radius)
    score_margin = signal-F(4, 5)*response_radius
    check("positive-score-margin-through-return-tolerance", score_margin > 0)
    conditional_from_joint = joint_radius/(F(1, 2)-joint_radius)
    check("joint-law-ball-preserves-both-initial-signs", joint_radius < F(1, 2))
    check("joint-law-tolerance-implies-certified-return-tolerance", conditional_from_joint < response_radius)
    return {
        "status": "PASS", "word_order": list(WORD_NAMES),
        "local_coordinate_radius": str(radius), "target_center_error": str(center_error),
        "target_witness_magnitude_lower": str(signal), "sign_certificates": local,
        "conditional_return_tolerance": str(response_radius),
        "determinant_margin_at_return_tolerance": str(score_margin),
        "per_word_joint_pair_TV_tolerance": str(joint_radius),
        "joint_TV_implied_conditional_return_radius": str(conditional_from_joint),
        "joint_TV_determinant_margin": str(signal-F(4, 5)*conditional_from_joint),
        "population_scope": "Every ordinary at-most-three-state model with both visible signs, the declared fixed reused kernels, unknown common Gibbs tilt and arbitrary per-word preparations has one singleton-sign determinant zero. A one-sign model cannot approximate the balanced target's pair laws within TV less than1/2 or fill both sign quotas. Neither simultaneous conditional-return approximation through3/20000 nor simultaneous full paired-law approximation through7/100000 to the balanced target is possible. No null stationary-preparation premise is introduced.",
        "conditioning_lemma": "For target initial sign mass1/2 and pair-TV error delta, the rival sign mass is at least1/2-delta. The return-probability error is at mostdelta/(1/2-delta), using the bounded function1{A=s,B=s}-r_target*1{A=s}, whose oscillation is one.",
        "statistical_constant_scope": "Local derivative, Hessian and Bernoulli variance constants support a separate quota/martingale proof. A pair-TV population approximation is not an assumed null preparation or serial-execution promise. Boundary misregistration and rare-sign group selection require their own error-count argument.",
    }


def state_count_certificate(target_returns):
    inherited = equivalence.verify_algebra()
    check("inherited-general-three-state-algebra-rerun", inherited["exact_checks"] == 66)
    check("general-three-state-common-initial-sign-law",
          sum(p*s for p, s in zip(equivalence.GEN_RHO, equivalence.GEN_S)) == 0)
    # A two-state deterministic binary readout exposes the complete state.
    # Therefore the LL conditional return is the corresponding K_L^2 entry,
    # regardless of distinct or history-dependent word preparations.
    low_plus = algebra.Interval(*target_returns[1][0])
    low_minus = algebra.Interval(*target_returns[-1][0])
    low2_plus = algebra.Interval(*target_returns[1][1])
    gap = low2_plus-low_plus**2-(1-low_plus)*(1-low_minus)
    check("general-two-state-nominal-composition-gap", gap.lo > F(69, 10000))
    response_radius, joint_radius = F(3, 20000), F(7, 100000)
    # For f(x,y)=x^2+(1-x)(1-y), |f_x|<=2 and |f_y|<=1
    # on the unit square. The LL coordinate contributes one more error.
    for x in (F(0), F(1)):
        for y in (F(0), F(1)):
            check("general-two-state-composition-gradient-corner",
                  abs(2*x+y-1) <= 2 and abs(x-1) <= 1)
    check("general-two-state-conditional-return-robust-gap",
          gap.lo-4*response_radius > F(63, 10000))
    check("general-two-state-joint-TV-to-conditional-radius",
          joint_radius/(F(1, 2)-joint_radius) < response_radius)
    return {"status": "PASS", "inherited_algebra": inherited,
            "general_two_state_identity": "r_LL,+ = r_L,+^2+(1-r_L,+)*(1-r_L,-)",
            "target_two_state_composition_gap_enclosure": rounded_interval((gap.lo, gap.hi)),
            "target_two_state_gap_formula": "(exp(-2/3)-exp(-4/3))^2/9",
            "conditional_return_error_tolerance": str(response_radius),
            "remaining_two_state_gap_strict_lower": "63/10000",
            "per_word_joint_pair_TV_tolerance": str(joint_radius),
            "general_state_minimum": 3, "ordinary_reversible_state_minimum": 4,
            "general_upper": "The inherited fixed three-state positive CTMC generators, common Gibbs laws, deterministic signs and invariant response coordinates reproduce every finite word's endpoint pairs from the one common preparation; this includes all seven registered words and their sign-conditional returns exactly.",
            "ordinary_upper": "The physical target itself is an ordinary reversible four-state realization.",
            "scope": "The minima apply to the seven endpoint-pair laws, including approximation with maximum per-word TV tolerance7/100000. The two-state lower permits arbitrary word preparations. No complete observed-path or intermediate-record equivalence is asserted."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        raise ValueError("The output must not overwrite this source")
    sources, proofs, reports = provenance()
    polynomial = witness_polynomial()
    singleton = singleton_polynomial_certificate()
    zero_mass = zero_mass_certificate()
    factorization = target_factorization_certificate()
    target_report, returns = target_certificate()
    population = population_robustness_certificate(returns)
    counts = state_count_certificate(returns)
    report = {
        "status": "PASS", "checks": len(CHECKS), "check_labels": CHECKS,
        "versions": {"python": platform.python_version()},
        "dependencies": "Python standard library only",
        "arithmetic": "Exact Fraction sparse polynomials, frozen matrix-Taylor enclosures through three factors, and rational local derivative bounds. No floating-point proof decisions.",
        "word_order": list(WORD_NAMES),
        "witness": {"definition": "F_s=(r_LH-r_L*r_H)*(r_HLL-r_LL*r_H)-(r_LLH-r_LL*r_H)*(r_HL-r_L*r_H)",
                    "degree": max(map(sum, polynomial.terms)), "nonzero_monomials": len(polynomial.terms)},
        "positive_weight_singleton_certificate": singleton,
        "zero_stationary_mass_certificate": zero_mass,
        "generic_target_factorization": factorization,
        "target_certificate": target_report,
        "population_robustness_certificate": population,
        "state_count_certificate": counts,
        "null_scope": "At most three total persistent states, including transient states with zero stationary mass; fixed stochastic kernels reversible for nonnegative Gibbs-related stationary laws with one unknown tilt in(-1,1); arbitrary history-dependent and word-dependent active-boundary preparations; initial and final records equal the actual boundary-state signs. No equilibrium reset, irreducibility, gap, fixed initial instrument, sign-preserving disturbance or numerical tilt calibration is assumed.",
        "source_sha256": sources, "proof_snapshot_sha256": proofs, "input_report_sha256": reports,
        "limitations": "This report certifies population identities, exact target response and local constants; finite-sample acquisition is certified separately. The target uses its stated equilibrium preparation. No laboratory throughput, detector robustness beyond a separately proved observation model, arbitrary target preparation or full-path equivalence is asserted.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(f"PASS: {len(CHECKS)} exact seven-word checks -> {args.output}")


if __name__ == "__main__":
    main()
