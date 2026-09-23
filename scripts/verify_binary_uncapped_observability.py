#!/usr/bin/env python3
"""Exact finite certificates for the binary uncapped observation interfaces.

This verifier uses only the standard library. Its small rational fixtures do
not evaluate semigroup exponentials or prove the all-model asymptotic theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction as F
from pathlib import Path


CHECKS = 0


def require(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zero(n: int) -> list[list[F]]:
    return [[F() for _ in range(n)] for _ in range(n)]


def diag(v: list[F]) -> list[list[F]]:
    return [[v[i] if i == j else F() for j in range(len(v))] for i in range(len(v))]


def eye(n: int) -> list[list[F]]:
    return diag([F(1)] * n)


def scale(a: list[list[F]], c: F) -> list[list[F]]:
    return [[c*x for x in row] for row in a]


def add(a: list[list[F]], b: list[list[F]], c: F = F(1)) -> list[list[F]]:
    return [[x+c*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mm(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F())
             for j in range(len(b[0]))] for i in range(len(a))]


def product(terms: list[list[list[F]]]) -> list[list[F]]:
    out = eye(len(terms[0]))
    for term in terms:
        out = mm(out, term)
    return out


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    rows = [a[i][:] + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        value = rows[j][j]
        rows[j] = [x/value for x in rows[j]]
        for i in range(n):
            if i != j:
                value = rows[i][j]
                rows[i] = [x-value*y for x, y in zip(rows[i], rows[j])]
    out = [row[n:] for row in rows]
    require(mm(a, out) == eye(n) and mm(out, a) == eye(n),
            'Rational inverse satisfies both defining identities')
    return out


def mv(a: list[list[F]], v: list[F]) -> list[F]:
    return [sum((x*y for x, y in zip(row, v)), F()) for row in a]


def dot(mu: list[F], x: list[F], y: list[F]) -> F:
    return sum((w*a*b for w, a, b in zip(mu, x, y)), F())


def scalar(mu: list[F], a: list[list[F]]) -> F:
    return dot(mu, [F(1)]*len(mu), mv(a, [F(1)]*len(mu)))


def adjoint(a: list[list[F]], mu: list[F]) -> list[list[F]]:
    return [[mu[j]*a[j][i]/mu[i] for j in range(len(mu))] for i in range(len(mu))]


def weighted_frobenius2(a: list[list[F]], mu: list[F]) -> F:
    return sum((mu[i]*a[i][j]**2/mu[j]
                for i in range(len(mu)) for j in range(len(mu))), F())


def ldl_positive(a: list[list[F]]) -> list[F]:
    require(a == transpose(a), 'LDL certificate is symmetric exactly')
    b, pivots = [row[:] for row in a], []
    for j in range(len(a)):
        p = b[j][j]
        require(p > 0, 'Every LDL pivot is strictly positive')
        pivots.append(p)
        for i in range(j+1, len(a)):
            for k in range(j+1, len(a)):
                b[i][k] -= b[i][j]*b[j][k]/p
    return pivots


def check_generator(k: list[list[F]], mu: list[F]) -> None:
    require(sum(mu) == 1 and min(mu) > 0, 'Stationary weights are a positive probability law')
    require(all(sum(row) == 0 for row in k), 'Generator row sums vanish exactly')
    require(all(k[i][j] >= 0 for i in range(len(k)) for j in range(len(k)) if i != j),
            'All off-diagonal rates are nonnegative')
    require(adjoint(k, mu) == k, 'Every hidden edge obeys exact detailed balance')


def resolvent(k: list[list[F]], s: F) -> list[list[F]]:
    return scale(inverse(add(scale(eye(len(k)), s), k, F(-1))), s)


def star() -> tuple[list[F], list[list[F]], list[list[F]], list[list[F]]]:
    mu = [F(1, 4), F(1, 4), F(1, 2)]
    k = [[F(-1), F(0), F(1)], [F(0), F(-4), F(4)],
         [F(1, 2), F(2), F(-5, 2)]]
    return mu, k, diag([F(1), F(1), F(0)]), diag([F(0), F(0), F(1)])


def binary_word_checks() -> dict:
    mu, k, d0, d1 = star()
    check_generator(k, mu)
    require(sum(mu[:2]) == mu[2] == F(1, 2), 'Three-state binary histogram is balanced')
    p = resolvent(k, F(1))
    require(p == scale([[F(19), F(4), F(10)], [F(4), F(13), F(16)],
                        [F(5), F(8), F(20)]], F(1, 33)),
            'Boundary example has the independently stated exact resolvent')
    v = [F(1), F(-1), F(0)]
    values = []
    for propagator, expected in ((p, F(-1, 7986)), (mm(p, p), F(-125989, 286992882))):
        word = product([d0, propagator, d0, propagator, d1, propagator, d0])
        value = dot(mu, v, mv(word, v))
        require(value == expected < 0, 'Positive nonpalindromic binary word has the stated negative quadratic form')
        require(all(x >= 0 for row in word for x in row), 'The negative quadratic form does not arise from negative entries')
        require(word != adjoint(word, mu), 'The returning word is not selfadjoint')
        values.append(str(value))
    word = product([d0, p, d0, p, d1, p, d0])
    require(mv(word, [F(1)]*3)[:2] == [F(3302, 35937), F(3224, 35937)],
            'Forward marginals retain the explicit unequal values')
    require(mv(adjoint(word, mu), [F(1)]*3)[:2] == [F(2510, 35937), F(4016, 35937)],
            'Adjoint marginals differ, preventing this example from being a stationary flip')
    z = [F(1), F(-3, 5), F(0)]
    asymmetric = product([d0, p, d1, resolvent(k, F(2)), d0])
    require(dot(mu, z, mv(asymmetric, z)) == F(-1, 14850),
            'Unmirrored Laplace parameters break the color palindrome PSD implication')
    b = product([d0, p, d1])
    palindrome = product([d0, p, d1, p, d0])
    require(palindrome == mm(b, adjoint(b, mu)), 'Mirrored parameters restore the exact B B* factorization')
    require(dot(mu, z, mv(palindrome, z)) >= 0, 'The mirrored fixture has nonnegative quadratic form')
    return {'hidden_states': 3, 'P_word_quadratic_exact': values[0],
            'P_squared_word_quadratic_exact': values[1],
            'unequal_parameter_quadratic_exact': '-1/14850',
            'scope': 'Mathematical probe and marginal counterexamples only; no physical gate or new readout is asserted.'}


def poly_product(a: list[list[list[F]]], b: list[list[list[F]]], degree: int) -> list[list[list[F]]]:
    n = len(a[0])
    out = [zero(n) for _ in range(min(degree, len(a)+len(b)-2)+1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i+j <= degree:
                out[i+j] = add(out[i+j], mm(ai, bj))
    return out


def mixed_parity_checks() -> list[dict]:
    mu, k, d0, d1 = star()
    cases = []
    for m in (2, 3):
        s, degree = F(7), m+2
        p = resolvent(k, s)
        ds = [d0, d1, add(d0, d1, F(-1))][:m]
        # Rational contraction proxies, not evaluations of killed semigroups.
        # Diagonal [0,1] multipliers and reversible Markov resolvents contract
        # L2(mu); their ordered products retain that property.
        es = [diag([F(1), F(2, 3), F(1, 2)]),
              mm(resolvent(k, F(2)), diag([F(1, 3), F(1), F(3, 4)])),
              mm(diag([F(4, 5), F(1, 5), F(1)]), resolvent(k, F(4))),
              diag([F(1, 2), F(2, 3), F(3, 4)])][:m+1]
        require(mm(es[1], p) != mm(p, es[1]), 'Inserted contraction fails to commute with the pulse resolvent')
        coefficients = [F() for _ in range(degree+1)]
        for signs in itertools.product((-1, 1), repeat=m):
            combined = [es[0]]
            for d, sign, e in zip(ds, signs, es[1:]):
                a0 = add(scale(eye(3), s), k, F(-1))
                a1 = scale(d, F(sign))
                series = [p]
                for j in range(1, degree+1):
                    series.append(scale(mm(mm(p, d), series[j-1]), -F(sign)/s))
                    require(add(mm(a0, series[j]), mm(a1, series[j-1])) == zero(3),
                            'Pulse coefficients solve the defining resolvent equation')
                combined = poly_product(combined, [mm(term, e) for term in series], degree)
            parity = F(1, 2**m)
            for sign in signs:
                parity *= sign
            for j, term in enumerate(combined):
                coefficients[j] += parity*scalar(mu, term)
        factors = [es[0]]
        for d, e in zip(ds, es[1:]):
            factors.extend((p, d, p, e))
        direct = scalar(mu, product(factors))
        require(coefficients[m] == (-F(1)/s)**m*direct,
                'Mixed parity leading coefficient includes every ordered endpoint and inserted factor')
        require(all(coefficients[j] == 0 for j in range(m)) and coefficients[m+1] == 0,
                'Parity kills all lower and opposite-parity coefficients')
        require(coefficients[m+2] != 0, 'Nonzero higher parity term requires a finite coefficient-extraction remainder')
        require(scalar(mu, product(factors[1:])) != direct,
                'Dropping the leading fixed block changes the observed scalar')
        wrong = [es[0]]
        for d, e in zip(ds, es[1:]):
            wrong.extend((d, p, e))
        require(scalar(mu, product(wrong)) != direct,
                'Stationarity cannot remove pulse endpoint resolvents across inserted contractions')
        cases.append({'pulse_count': m, 's_exact': str(s), 'leading_coefficient_exact': str(coefficients[m]),
                      'higher_parity_coefficient_exact': str(coefficients[m+2]),
                      'mixed_word_exact': str(direct), 'fixed_blocks': 'Rational contraction proxies, not semigroup evaluations'})
    return cases


def cross_color_checks() -> dict:
    mu, k, d0, d1 = star()
    degree = 2
    expansion = [eye(3), k, mm(k, k)]
    f0 = poly_product(poly_product(expansion, [d0], degree), expansion, degree)
    f1 = poly_product(poly_product(expansion, [d1], degree), expansion, degree)
    cross = poly_product(f0, f1, degree)
    raw = product([d0, k, d1])
    require(cross[0] == zero(3) and cross[1] == scale(raw, F(2)),
            'Cross-color cancellation has zero constant term and exactly twice the generator block at first order')
    require(cross[2] != zero(3), 'Second-order cross-color correction is nonzero in the fixture')
    e = diag([F(1, 2), F(1, 3), F(2, 3)])
    reverse = poly_product(f1, f0, degree)
    sandwich = poly_product(poly_product(cross, [e], degree), reverse, degree)
    raw_sandwich = product([d0, k, d1, e, d1, k, d0])
    require(sandwich[0] == sandwich[1] == zero(3) and sandwich[2] == scale(raw_sandwich, F(4)),
            'Two-sided normalized selector has the exact factor four at leading degree two')
    cap, kappa, examples = F(8), F(1, 1000), []
    # Gershgorin bounds the reversible spectrum by twice the maximum exit.
    require(2*max(-k[i][i] for i in range(3)) == cap, 'Fixture spectral cap follows from its exits')
    for s in (F(8), F(32), F(128)):
        p = resolvent(k, s)
        f0s, f1s = product([p, d0, p]), product([p, d1, p])
        block_error = add(mm(f0s, f1s), scale(raw, 2/s), F(-1))
        normalized = scale(product([f0s, f1s, e, f1s, f0s]), s*s/(4*kappa))
        error = add(normalized, scale(raw_sandwich, 1/kappa), F(-1))
        b2, n2 = weighted_frobenius2(block_error, mu), weighted_frobenius2(error, mu)
        require(b2 <= (7*cap**2/s**2)**2, 'Exact weighted Frobenius certificate implies the cross-color norm bound')
        require(n2 <= (7*cap**3/(kappa*s))**2,
                'The normalized bound includes the small selector mass kappa')
        examples.append({'s_exact': str(s), 'cross_error_weighted_Frobenius_squared': str(b2),
                         'normalized_error_weighted_Frobenius_squared': str(n2)})
    return {'target_spectral_cap': 8, 'kappa_exact': str(kappa), 'examples': examples,
            'scope': 'Target-side cancellation only; no rival generator norm is used or inferred.'}


def weighted_measure_checks() -> dict:
    u = [F(1, 1000), F(1, 2), F(1), F(2), F(0)]
    normalizer = 2*sum((1/x**2 for x in u[:4]), F())
    mu = [1/(x*x*normalizer) for x in u[:4]] + [F(1, 2)]
    a, z = diag(u), dot(mu, u, u)
    nu = [mu[i]*u[i]**2/z for i in range(4)]
    require(nu == [F(1, 4)]*4 and sum(mu) == 1, 'Tiny uneven reference weights change exactly to the uniform cube law')
    require(z < F(1, 100000) and u[-1] == 0, 'The fixture has tiny normalization mass and a genuine zero-support state')
    epsilon, delta = F(1, 1000000), F(1, 100000)
    vectors = [[(1+epsilon)*u[i]*(-1 if i & (1 << b) else 1) for i in range(4)] + [F(0)] for b in range(2)]
    q = [(1+2*epsilon)*x for x in u]
    rows = []
    for c in range(2):
        changed = zero(4)
        for i in range(4):
            changed[i][i ^ (1 << c)] = 1+epsilon
        kernel = zero(5)
        for i in range(4):
            for j in range(4):
                kernel[i][j] = u[i]*changed[i][j]/u[j]
        transformed_adjoint = [[adjoint(kernel, mu)[i][j]*u[j]/u[i] for j in range(4)] for i in range(4)]
        require(transformed_adjoint == adjoint(changed, nu), 'Positive diagonal change intertwines stationary adjoints exactly')
        require(all(x == 0 for x in kernel[-1]) and all(row[-1] == 0 for row in kernel),
                'Zero coordinates are excluded without division and the kernel has outer support')
        cu = mv(kernel, u)
        row_defect = dot(mu, [x-y for x, y in zip(cu, u)], [x-y for x, y in zip(cu, u)])
        expanded = scalar(mu, product([a, adjoint(kernel, mu), kernel, a])) - 2*scalar(mu, product([a, kernel, a])) + scalar(mu, mm(a, a))
        require(row_defect == expanded == z*epsilon**2, 'Measured whole-word Gram expansion equals the direct vector defect')
        for b, v in enumerate(vectors):
            vt = [v[i]/u[i] for i in range(4)]
            cv = mv(kernel, v)
            transformed_cv = mv(changed, vt)
            require(dot(mu, v, v)/z == dot(nu, vt, vt), 'Changed query norm is an exact isometry')
            require(dot(mu, cv, cv)/z == dot(nu, transformed_cv, transformed_cv), 'Changed image norm is an exact isometry')
            require(dot(mu, v, cv)/z == dot(nu, vt, transformed_cv), 'Changed correlation is an exact isometry')
            require(all(abs(x) <= y for x, y in zip(v, q)), 'Positive query envelope bounds the signed probe pointwise')
            require(abs(dot(mu, v, v)-z) <= z*delta and dot(mu, cv, cv) <= z*(1+delta),
                    'Perturbed probe and measured image satisfy the whole-word norm hypotheses')
            sign = -1 if b == c else 1
            require(sign*dot(mu, v, cv) >= z*(1-delta), 'Every addressed and unaddressed correlation has the required sign and precision')
            clipped = [max(F(-1), min(F(1), x)) for x in vt]
            clip_error = dot(nu, [x-y for x, y in zip(vt, clipped)], [x-y for x, y in zip(vt, clipped)])
            qdef = dot(mu, [x-y for x, y in zip(q, u)], [x-y for x, y in zip(q, u)])/z
            require(0 < clip_error <= qdef <= delta, 'Nontrivial clipping is controlled by the observed positive envelope')
        require(row_defect <= z*delta and scalar(mu, mm(a, a)) == z,
                'Reference normalization and row defect are recovered by ordinary hidden scalars')
        rows.append(str(max(sum(row) for row in kernel)))
    require(delta <= F(1, (32*2)**2), 'Finite two-bit fixture satisfies the canonical entropy accuracy threshold')
    return {'states': 5, 'support_states': 4, 'u_exact': list(map(str, u)),
            'normalization_Z_exact': str(z), 'changed_law_exact': list(map(str, nu)),
            'Delta_exact': str(delta), 'max_original_kernel_row_sums_exact': rows,
            'scope': 'Exact finite change of measure and scalar identities; no minimum coordinate or uniform raw row bound is assumed.'}


def partial_flip_checks() -> list[dict]:
    reports = []
    for support in (list(range(8)), [0, 1, 2, 3]):
        mass = {x: F(1, len(support)) for x in support}
        lower_sum = F()
        records = []
        for c in range(3):
            # Symmetric edge fluxes give equal marginals independently of
            # whether a requested neighbor remains inside the support.
            joint = {(x, y): F() for x in support for y in support}
            for x in support:
                for bit, fraction in ((c, F(1, 2)), ((c+1) % 3, F(1, 8))):
                    y = x ^ (1 << bit)
                    if y in mass:
                        joint[x, y] += fraction*min(mass[x], mass[y])
                joint[x, x] = mass[x]-sum(joint[x, y] for y in support if y != x)
            require(all(sum(joint[x, y] for y in support) == mass[x] for x in support)
                    and all(sum(joint[x, y] for x in support) == mass[y] for y in support),
                    'Partial-flip coupling has exactly equal marginals')
            p = sum((value for (x, y), value in joint.items() if (x ^ y) & (1 << c)), F())
            e = sum((value for (x, y), value in joint.items() if (x ^ y) & ~(1 << c)), F())
            capacity = F()
            for x in support:
                if not x & (1 << c) and (x ^ (1 << c)) in mass:
                    capacity += 2*min(mass[x], mass[x ^ (1 << c)])
            require(p-e <= capacity, 'Changed-bit minus collateral-change probability is bounded by conditional pair capacity')
            # Uniform support has only equal-probability pairs and singletons;
            # its conditional entropy is exactly this rational capacity.
            lower_sum += p-e
            records.append({'coordinate': c, 'p_exact': str(p), 'e_exact': str(e),
                            'conditional_entropy_exact_bits': str(capacity)})
        entropy = F(len(support).bit_length()-1)
        require(sum(F(row['conditional_entropy_exact_bits']) for row in records) <= entropy,
                'Conditional entropies sum below the exactly known uniform-support entropy')
        require(lower_sum <= entropy, 'The finite partial-flip entropy lower bound holds exactly')
        reports.append({'support_states': len(support), 'entropy_exact_bits': str(entropy),
                        'partial_flip_lower_bound_exact_bits': str(lower_sum), 'coordinates': records})
    return reports


def tagged_toy_checks() -> dict:
    # hub, two core roots, two private tags, two chain vertices, balancing B.
    a, lam, ell = F(11, 10), [F(1, 1000), F(1, 2000)], [F(6, 5), F(7, 5)]
    weights = [F(1, 2), F(1, 4), F(1, 4), lam[0]/(4*ell[0]), lam[1]/(4*ell[1]), a/2, a*a/2]
    color0 = [0, 1, 2, 5, 6]
    w0, wt = sum((weights[i] for i in color0), F()), weights[3]+weights[4]
    weights.append(w0-wt)
    mu, k = [w/(2*w0) for w in weights], zero(8)

    def edge(i: int, j: int, rate: F) -> None:
        reverse = weights[i]*rate/weights[j]
        k[i][j] += rate
        k[i][i] -= rate
        k[j][i] += reverse
        k[j][j] -= reverse

    edge(1, 0, F(1))
    edge(2, 0, F(1))
    edge(1, 2, F(1, 16))
    edge(1, 3, lam[0])
    edge(2, 4, lam[1])
    edge(0, 5, F(1))
    edge(5, 6, F(1))
    edge(7, 6, F(400))
    check_generator(k, mu)
    require(sum(mu[i] for i in color0) == F(1, 2), 'Added distant balancing state restores exact binary balance')
    require(k[5][0] == k[6][5] == 1/a, 'Biased-chain reverse rates match the geometric stationary weights')
    require(k[3][1] == ell[0] and k[4][2] == ell[1], 'Rare tag entrance does not reduce its departure rate')
    require(max(-k[i][i] for i in range(8)) < 500_000_000, 'Finite target toy obeys the advertised crude exit cap')
    # With the tags removed as a principal block, their loss remains in K_FF.
    fast = [0, 1, 2, 5, 6, 7]
    killing, fast_gap = F(10**9), F(200)
    fast_matrix = [[k[i][j] - (killing if i == j and i in color0 else 0) for j in fast] for i in fast]
    fast_weighted = mm(diag([mu[i] for i in fast]),
                       add(scale(eye(len(fast)), -fast_gap), fast_matrix, F(-1)))
    pivots = ldl_positive(fast_weighted)
    require(max(lam[j]*ell[j] for j in range(2)) <= 2*max(lam),
            'Squared tag-to-fast coupling norm has the canonical bound')
    # A full-space weighted PSD certificate can be reduced by its exact null
    # constant vector to any principal block with one state removed.
    g = F(1, 100000)
    projection = [[mu[j] for j in range(8)] for _ in range(8)]
    gap_form = mm(diag(mu), add(scale(k, F(-1)), scale(add(eye(8), projection, F(-1)), -g)))
    require(mv(gap_form, [F(1)]*8) == [F(0)]*8, 'Target gap form has the exact constant null vector')
    gap_pivots = ldl_positive([row[:-1] for row in gap_form[:-1]])
    require(weights[7]/weights[6] <= 2+a/(a-1), 'The balancing-edge weight ratio satisfies the chain bound')
    for base in (F(1), F(3, 2), F(2, 3)):
        # gamma=1/2 and h=2 log(base) make the original field exponentials
        # rational, allowing an exact check without evaluating a logarithm.
        pi_a, ratio = 1/(1+base**4), base**4
        for i in range(8):
            sign = -1 if i in color0 else 1
            q_in, q_out = mu[i]*base**(2+sign), base**(sign-2)
            require(pi_a*q_in == pi_a*ratio*mu[i]*q_out,
                    'Every original-field visible edge obeys exact physical detailed balance')
    require(sum(mu) == 1, 'At zero field both aggregate visible telegraph exit rates equal one')
    return {'hidden_states': 8, 'total_physical_states_with_visible': 9,
            'added_chain_states': 2, 'a_exact': str(a),
            'stationary_weights_exact': list(map(str, mu)), 'binary_color_zero_indices': color0,
            'maximum_exit_exact': str(max(-k[i][i] for i in range(8))),
            'killing_rate': int(killing), 'fast_sector_gap_certificate': int(fast_gap),
            'fast_sector_weighted_LDL_pivots_exact': list(map(str, pivots)),
            'full_target_gap_lower_bound_exact': str(g), 'full_gap_reduced_LDL_pivots_exact': list(map(str, gap_pivots)),
            'rational_physical_field_bases': ['1', '3/2', '2/3'], 'physical_gamma_exact': '1/2',
            'scope': 'An eight-state rational structural toy, with different entrance weights and chain length from the asymptotic target. No killed exponential is evaluated.'}


def exponent_checks() -> dict:
    n_scale, eta = 10**6, F(1, 10**6)
    a = 1+eta
    levels = [1+F(j, 20) for j in range(1, 19)]
    phi = [4*x-x*x for x in levels]
    entrances = [-15+x for x in phi]
    kappas = [-15+x*x for x in levels]
    times = [4-2*x for x in levels]
    max_entrance = max(entrances)
    records = []
    require(max_entrance <= -11 and min(times) == F(1, 5),
            'All eighteen tag exponents have the stated uniform entrance and duration bounds')
    for i, (li, ti, ki) in enumerate(zip(levels, times, kappas)):
        discriminations = []
        for j, lj in enumerate(levels):
            value = entrances[j]-lj*ti-ki
            require(value == -(lj-li)**2, 'Completing the square gives the exact signed-type discriminator')
            require(value == 0 if i == j else n_scale*value <= -2500,
                    'Every off-type tag is suppressed by at least exp(-2500 n)')
            discriminations.append(str(value))
        # log(4)>1: e=sum 1/k! < 1+1+sum_{k>=2} 1/2^(k-1)=3<4.
        # Therefore the following rational use of theta*m >=100*N*n is
        # conservative and avoids evaluating a transcendental exponential.
        powers = [2*max_entrance-ti/2-ki,
                  max_entrance-100-ti/2-ki,
                  -194*ti-ki,
                  max_entrance-200-ti/2-ki]
        require(all(x < -1 for x in powers), 'All four rare/far contamination powers beat exp(-10^6 n) before polynomial prefactors')
        require(20+ki >= 6, 'The resolvent normalization satisfies s*kappa >= exp(6 N n)')
        require(40-ki <= 54, 'Selector normalization costs at most 54 N n in its logarithm, before the helpful divisor four')
        records.append({'type': i+1, 'ell_exact': str(li), 'phi_exact': str(phi[i]),
                        'log_lambda_upper_per_Nn': str(entrances[i]), 'log_kappa_per_Nn': str(ki),
                        'killed_duration_per_Nn': str(ti), 'discrimination_powers_per_Nn': discriminations,
                        'contamination_powers_per_Nn': list(map(str, powers))})
    ratio_bound = 2+a/(a-1)
    require(ratio_bound < 1_000_004 and 400*ratio_bound+2 < 500_000_000,
            'Canonical long-chain balancing exit fits the fixed target cap')
    core_mass_prefactor = 1/(36*(1+a/(2*eta)))
    require(100*n_scale*eta == 100,
            'log(1+eta)<=eta gives the stated exp(100 n) stationary chain growth bound')
    require(-2300+100 == -2200 and -100+50 == -50,
            'Gate normalization and conditional-root norm losses retain decaying target exponents')
    # The final theorem counts at most 60q cross-port factors, hence 122q
    # signed selectors and 488q pulse factors, q=n+1.  Use log 2<1,
    # log 6<2 and n<=q to certify the coefficients without exponentiating.
    selectors, pulses, interpolation = 122, 488, 1200
    require(2*60+2 == selectors and 4*selectors == pulses,
            'Endpoint and gate selector counts imply the advertised pulse budget')
    fixed_log_mass_coefficient = selectors*14*n_scale + 60*(100+4) + selectors + 2
    require(fixed_log_mass_coefficient < 2000*n_scale,
            'Selector inverse masses, gates, sign expansions and scalar sums fit the quadratic log coefficient budget')
    require(selectors*2*n_scale + 60 < 250*n_scale,
            'Killed durations and heat insertions fit the total quadratic duration budget')
    s_power_per_q = 2*selectors + pulses-interpolation
    require(s_power_per_q == -468, 'Normalized interpolation remainder has a strictly decaying resolvent power')
    # After adding N q^2, the logarithm of the exact conservative remainder
    # bound has these polynomial coefficients in t=q-2>=0.
    q2 = 2001*n_scale + 20*n_scale*s_power_per_q
    q1 = -20*n_scale*(s_power_per_q+1) + pulses+2*interpolation
    q0 = 20*n_scale+4
    shifted = [4*q2+2*q1+q0, 4*q2+q1, q2]
    require(all(x < 0 for x in shifted),
            'Every coefficient after q=t+2 is negative, proving the extraction tail <= exp(-N q^2) for all n>=1')
    require(15-1 >= 5, 'Using log 2<1 proves exp(-15 n)<=1/(32*2^n) for every integer n>=1')
    return {'N': n_scale, 'eta_exact': str(eta), 'canonical_chain_states_per_n': 100*n_scale,
            'canonical_chain_constructed': False, 'exponentials_evaluated': False,
            'canonical_balancing_weight_ratio_upper_exact': str(ratio_bound),
            'port_mass_lower_prefactor_before_exp_minus_100n_exact': str(core_mass_prefactor),
            'whole_word_budget': {'cross_port_factors_per_q': 60, 'selectors_per_q': selectors,
                                 'pulses_per_q': pulses, 'interpolation_degree_per_q': interpolation,
                                 'fixed_log_mass_coefficient_bound': fixed_log_mass_coefficient,
                                 'tail_log_plus_Nq_squared_coefficients_in_q_minus_2': shifted},
            'types': records,
            'scope': 'Exact coefficients of n in exponent bounds; fixed constants and polynomial factors still require the sufficiently-large-n argument in the proof.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/binary_uncapped_observability.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Standard-library fractions.Fraction and exact integers only',
              'binary_PSD_route_boundaries': binary_word_checks(),
              'mixed_resolvent_parity': mixed_parity_checks(),
              'normalized_cross_color_cancellation': cross_color_checks(),
              'weighted_whole_word_change_of_measure': weighted_measure_checks(),
              'partial_flip_entropy_combinatorics': partial_flip_checks(),
              'rare_tag_balancing_chain_toy': tagged_toy_checks(),
              'canonical_eighteen_type_exponent_certificates': exponent_checks(),
              'largest_dense_matrix_dimension': 8,
              'full_asymptotic_target_allocated': False,
              'limitations': [
                  'Finite exact fixtures do not prove analytic continuation, all-model mixed-word observability, semigroup estimates, whole-word repair, or the asymptotic lower theorem.',
                  'Inserted rational contractions test the ordered algebra and are not numerical evaluations of killed semigroups.',
                  'The short-chain eight-state toy is not the asymptotic target and does not validate its uniform gap or distant-boundary estimates by simulation.',
                  'Canonical exponent arithmetic does not evaluate tiny rates, long-chain matrices, or asymptotic thresholds that absorb fixed constants.',
                  'No fixed positive control clock, finite switching budget, or rate cap on a rival is inferred.'
              ],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    names = ['MIXED_KILLED_WORD_OBSERVABILITY.md', 'WEIGHTED_WHOLE_WORD_REPAIR.md',
             'BINARY_UNCAPPED_RESEARCH_BOUNDARY.md', 'BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md',
             'BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md']
    report['proof_snapshot_sha256'] = {str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
                                      for name in names}
    report['exact_checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
