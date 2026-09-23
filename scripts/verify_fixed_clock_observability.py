#!/usr/bin/env python3
"""Small exact and numerical fixtures for fixed-clock observation identities.

The checks are finite certificates of formulas, not an all-model proof or a
simulation of the large binary target family.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.integrate import quad


CHECKS = 0


def require(condition: bool, description: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)


def zero(n: int) -> list[list[F]]:
    return [[F() for _ in range(n)] for _ in range(n)]


def diag(values: list[F]) -> list[list[F]]:
    n = len(values)
    return [[values[i] if i == j else F() for j in range(n)] for i in range(n)]


def eye(n: int) -> list[list[F]]:
    return diag([F(1)]*n)


def scale(a: list[list[F]], c: F) -> list[list[F]]:
    return [[c*x for x in row] for row in a]


def add(a: list[list[F]], b: list[list[F]], c: F = F(1)) -> list[list[F]]:
    return [[x+c*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mm(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F())
             for j in range(len(b[0]))] for i in range(len(a))]


def product(factors: list[list[list[F]]]) -> list[list[F]]:
    out = eye(len(factors[0]))
    for factor in factors:
        out = mm(out, factor)
    return out


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    rows = [a[i][:]+eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        d = rows[j][j]
        rows[j] = [x/d for x in rows[j]]
        for i in range(n):
            if i != j:
                d = rows[i][j]
                rows[i] = [x-d*y for x, y in zip(rows[i], rows[j])]
    result = [row[n:] for row in rows]
    require(mm(a, result) == mm(result, a) == eye(n), 'Exact inverse satisfies both defining identities')
    return result


def adjoint(a: list[list[F]], law: list[F]) -> list[list[F]]:
    return [[law[j]*a[j][i]/law[i] for j in range(len(law))] for i in range(len(law))]


def ldl_positive(a: list[list[F]]) -> list[F]:
    require(a == [list(row) for row in zip(*a)], 'Weighted LDL certificate is exactly symmetric')
    b, pivots = [row[:] for row in a], []
    for j in range(len(a)):
        value = b[j][j]
        require(value > 0, 'All LDL pivots are strictly positive')
        pivots.append(value)
        for i in range(j+1, len(a)):
            for k in range(j+1, len(a)):
                b[i][k] -= b[i][j]*b[j][k]/value
    return pivots


def array(a: list[list[F]]) -> np.ndarray:
    return np.array([[float(x) for x in row] for row in a])


def rounded(value: float) -> float:
    return float(f'{value:.12g}')


def base_model() -> tuple[list[F], list[list[F]], list[list[F]], list[list[F]]]:
    mu = [F(1, 4), F(1, 4), F(1, 2)]
    k = [[F(-1), F(0), F(1)], [F(0), F(-4), F(4)], [F(1, 2), F(2), F(-5, 2)]]
    return mu, k, diag([F(1), F(1), F(0)]), diag([F(0), F(0), F(1)])


def physical_model(base: F) -> tuple[list[F], list[list[F]], list[F]]:
    """gamma=1/2, h=2 log(base), k=1: all physical rates are rational."""
    mu, k, _, _ = base_model()
    q = zero(4)
    for i in range(3):
        for j in range(3):
            q[i+1][j+1] = k[i][j]
        sign = -1 if i < 2 else 1
        q[0][i+1] = mu[i]*base**(2+sign)
        q[i+1][0] = base**(sign-2)
        q[0][0] -= q[0][i+1]
        q[i+1][i+1] -= q[i+1][0]
    pi0 = [F(1, 2)]+[x/2 for x in mu]
    r = base**4
    pih = [1/(1+r)]+[r*x/(1+r) for x in mu]
    require(all(sum(row) == 0 for row in q), 'Original-field generator is conservative')
    require(adjoint(q, pih) == q, 'Original-field generator has the stated stationary law')
    return pi0, q, pih


def a_start_and_adjoint_checks() -> dict:
    bases = [F(1), F(3, 2), F(2), F(4, 3)]
    exact_kernels, numerical_kernels = {}, {}
    pi0 = physical_model(bases[0])[0]
    a_projection = diag([F(1), F(0), F(0), F(0)])
    tick = F(2, 5)
    for base in bases:
        _, q, _ = physical_model(base)
        # A rational Markov resolvent is an exact stationarity fixture for
        # the recursion.  Actual fixed-clock semigroups are tested below.
        e = scale(inverse(add(scale(eye(4), F(5)), q, F(-1))), F(5))
        exact_kernels[base] = e
        numerical_kernels[base] = expm(float(tick)*array(q))
        r = base**4
        d = add(scale(eye(4), r), scale(a_projection, 1-r))
        di = add(scale(eye(4), 1/r), scale(a_projection, 1-1/r))
        require(adjoint(e, pi0) == product([d, e, di]),
                'Exact physical-kernel adjoint is the stationary-law diagonal conjugation')

    def f(word: tuple[F, ...]) -> F:
        p = product([exact_kernels[x] for x in word]) if word else eye(4)
        return sum((pi0[i]*p[i][0] for i in range(4)), F())

    def recursive_a(word: tuple[F, ...]) -> F:
        if not word:
            return F(1)
        if word[0] == 1:
            return F(5, 7)*recursive_a(word[1:])+F(2, 7)*f(word[1:])
        r = word[0]**4
        return recursive_a(word[1:]) + 2*r/(1-r)*(f(word[1:])-f(word))

    cases, max_residual = 0, 0.0
    for length in range(1, 5):
        for word in itertools.product(bases, repeat=length):
            p = product([exact_kernels[x] for x in word])
            require(recursive_a(word) == p[0][0], 'A-start recursion recovers the exact initial-A return probability')
            exact_star = product([adjoint(exact_kernels[x], pi0) for x in reversed(word)])
            require(adjoint(p, pi0) == exact_star, 'Words take stationary adjoints by reversal and generator-wise conjugation')
            matrices = [numerical_kernels[x] for x in word]
            numerical_p = np.eye(4)
            for matrix in matrices:
                numerical_p = numerical_p @ matrix
            recover, tail = 1.0, np.eye(4)
            pi = np.array([float(x) for x in pi0])
            for base in reversed(word):
                longer = numerical_kernels[base] @ tail
                r = float(base**4)
                if base == 1:
                    rho = math.exp(-2*float(tick))
                    recover = rho*recover+(1-rho)*float(pi @ tail[:, 0])
                else:
                    recover += 2*r/(1-r)*float(pi @ (tail-longer)[:, 0])
                tail = longer
            residual = abs(recover-numerical_p[0, 0])
            require(residual < 2e-13, 'Actual fixed-clock exponential words satisfy the A-start recursion numerically')
            max_residual = max(max_residual, residual)
            cases += 1
    s_vector = [F(-1), F(1), F(1), F(1)]

    def inserted_scalar(tokens: tuple) -> F:
        blocks, current = [], []
        for token in tokens:
            if token == 'A':
                blocks.append(tuple(current))
                current = []
            else:
                current.append(token)
        blocks.append(tuple(current))
        if len(blocks) == 1:
            return 1-2*f(blocks[0])
        value = f(blocks[0])
        for block in blocks[1:-1]:
            value *= recursive_a(block)
        return value*(1-2*recursive_a(blocks[-1]))

    def token_matrix(tokens: tuple) -> list[list[F]]:
        return product([a_projection if x == 'A' else exact_kernels[x] for x in tokens]) if tokens else eye(4)

    insertion_cases = [(bases[1], 'A', 'A', bases[2], bases[3], 'A'),
                       ('A', 'A'), ('A', bases[1], 'A', bases[0], 'A', bases[2]), ()]
    for tokens in insertion_cases:
        result = mm([pi0], mm(token_matrix(tokens), [[x] for x in s_vector]))[0][0]
        require(result == inserted_scalar(tokens), 'Rank-one scalar reconstruction handles zero-length blocks and consecutive visible projectors')
    u, v = (bases[1], 'A', bases[2]), ('A', bases[3], bases[0])
    # Expand (I-2A)U*V into inserted legal forward words, then reconstruct
    # each scalar solely from forward means and the A-start recursion.
    terms = [(F(1), ()), (F(-2), ('A',))]
    for token in reversed(u):
        if token == 'A':
            pieces = [(F(1), ('A',))]
        else:
            alpha, beta = token**-4-1, token**4-1
            pieces = [(F(1), (token,)), (alpha, ('A', token)),
                      (beta, (token, 'A')), (alpha*beta, ('A', token, 'A'))]
        terms = [(c*d, left+right) for c, left in terms for d, right in pieces]
    reconstructed = sum((c*inserted_scalar(tokens+v) for c, tokens in terms), F())
    us = mm(token_matrix(u), [[x] for x in s_vector])
    vs = mm(token_matrix(v), [[x] for x in s_vector])
    direct = sum((pi0[i]*us[i][0]*vs[i][0] for i in range(4)), F())
    require(reconstructed == direct, 'Full sampled Gram scalar is recovered by adjoint expansion and rank-one forward-mean formulas')
    return {'total_physical_states': 4, 'word_cases': cases, 'max_word_length': 4,
            'tick_exact': str(tick), 'rational_field_bases': list(map(str, bases)),
            'max_exponential_A_start_residual': rounded(max_residual),
            'inserted_projector_cases': len(insertion_cases), 'reconstructed_Gram_exact': str(direct),
            'Gram_expansion_terms': len(terms), 'max_Gram_forward_ticks': 4,
            'scope': 'Exact rational stationarity fixtures and numerical actual-semigroup words; no arbitrary-width reconstruction claim is inferred.'}


def schur_and_binary_elimination_checks() -> dict:
    mu, k, d0, d1 = base_model()
    bases, examples = (F(1), F(2)), []
    for s in (F(1), F(7), F(31)):
        gs, bs = [], []
        for base in bases:
            _, q, _ = physical_model(base)
            full_r = scale(inverse(add(scale(eye(4), s), q, F(-1))), s)
            schur = [[(full_r[i+1][j+1]-full_r[i+1][0]*full_r[0][j+1]/full_r[0][0])/s
                      for j in range(3)] for i in range(3)]
            b = diag([base**-3, base**-3, base**-1])
            hidden = inverse(add(add(scale(eye(3), s), k, F(-1)), b))
            require(schur == hidden, 'Visible-state Schur elimination yields the exact hidden killed resolvent')
            require(min(x for row in schur for x in row) > 0, 'Exact Schur result is positive despite its signed elimination formula')
            require(adjoint(hidden, mu) == hidden, 'Hidden killed resolvent is selfadjoint in the hidden stationary law')
            gs.append(hidden)
            bs.append(b)
        ga, gb = gs
        delta_b = add(bs[1], bs[0], F(-1))
        difference = add(ga, gb, F(-1))
        require(difference == product([ga, delta_b, gb]), 'Second resolvent identity keeps the binary insertion order')
        gap0, gap1 = delta_b[0][0], delta_b[2][2]
        require(gap0 != gap1, 'Two physical fields give linearly independent binary killing coefficients')
        recovered0 = scale(add(difference, scale(mm(ga, gb), gap1), F(-1)), 1/(gap0-gap1))
        recovered1 = scale(add(scale(mm(ga, gb), gap0), difference, F(-1)), 1/(gap0-gap1))
        require(recovered0 == product([ga, d0, gb]) and recovered1 == product([ga, d1, gb]),
                'Signed observed resolvent formulas eliminate both binary label insertions exactly')
        contractions = []
        for color, d in enumerate((d0, d1)):
            positive = scale(add(product([ga, d, gb]), product([gb, d, ga])), s*s/2)
            require(adjoint(positive, mu) == positive and all(x >= 0 for row in positive for x in row),
                    'Symmetrized binary insertion is entrywise nonnegative and selfadjoint')
            minus = mm(diag(mu), add(eye(3), positive, F(-1)))
            plus = mm(diag(mu), add(eye(3), positive))
            contractions.append({'I_minus_F_weighted_LDL_exact': list(map(str, ldl_positive(minus))),
                                 'I_plus_F_weighted_LDL_exact': list(map(str, ldl_positive(plus)))})
            if color == 0:
                za, zb = scale(ga, s), scale(gb, s)
                normalized_formula = add(scale(add(za, zb, F(-1)), s/(gap0-gap1)),
                    scale(add(mm(za, zb), mm(zb, za)), -gap1/(2*(gap0-gap1))))
                require(normalized_formula == positive,
                        'The normalized two-field selector formula has the exact s and symmetrization factors')
        examples.append({'s_exact': str(s), 'R_AA_exact': str(full_r[0][0]),
                         'binary_coefficient_difference_exact': [str(gap0), str(gap1)],
                         'label_contraction_certificates': contractions})
    return {'hidden_states': 3, 'total_physical_states': 4,
            'physical_field_bases': list(map(str, bases)), 'examples': examples}


def positive_selector_leading_checks() -> dict:
    mu, k, d0, d1 = base_model()
    b0, b1 = eye(3), diag([F(1, 8), F(1, 8), F(1, 2)])
    qa, qb = add(k, b0, F(-1)), add(k, b1, F(-1))
    first_order = []
    for d in (d0, d1):
        first_order.append(scale(add(add(mm(qa, d), mm(d, qb)), add(mm(qb, d), mm(d, qa))), F(1, 2)))
    cross0 = mm(d0, d1)
    cross1 = add(mm(first_order[0], d1), mm(d0, first_order[1]))
    raw = product([d0, k, d1])
    require(cross0 == zero(3) and cross1 == scale(raw, F(2)),
            'Positive physical-resolvent selectors retain the exact cross-color cancellation and factor two')
    e = diag([F(1, 2), F(1, 3), F(2, 3)])
    leading = product([cross1, e, adjoint(cross1, mu)])
    require(leading == scale(product([d0, k, d1, e, d1, k, d0]), F(4)),
            'Normalized two-sided selector has the factor-four target leading term')
    errors = []
    for s in (10., 40., 160.):
        ga = np.linalg.inv(s*np.eye(3)-array(qa))
        gb = np.linalg.inv(s*np.eye(3)-array(qb))
        fs = [s*s/2*(ga @ array(d) @ gb+gb @ array(d) @ ga) for d in (d0, d1)]
        killed = expm(.3*(array(k)-5*array(d0)))
        actual = s*s/4*fs[0] @ fs[1] @ killed @ fs[1] @ fs[0]
        ideal = array(raw) @ killed @ array(adjoint(raw, mu))
        weights = np.sqrt(np.array([float(x) for x in mu]))
        error = np.linalg.norm(weights[:, None]*(actual-ideal)/weights[None, :], 2)
        require(np.min(actual) >= -1e-13, 'Numerical killed selector is entrywise nonnegative')
        errors.append(rounded(float(error)))
    require(errors[2] < errors[1] < errors[0], 'Finite selector residual decreases as the resolvent probe grows')
    # A positive selfadjoint selector need not be PSD. This independently
    # supplied two-state counterexample guards the precise positivity claim.
    ga = scale([[F(3), F(1)], [F(1), F(3)]], F(1, 8))
    gb = scale([[F(18), F(8)], [F(8), F(20)]], F(1, 37))
    toy_k = [[F(-1), F(1)], [F(1), F(-1)]]
    require(ga == inverse(add(scale(eye(2), F(2)), toy_k, F(-1)))
            and gb == inverse(add(add(eye(2), toy_k, F(-1)), diag([F(1, 2), F(1, 4)]))),
            'Non-PSD example resolvents share one generator and physical zero/nonzero binary killing rates')
    dc = diag([F(1), F(0)])
    selector = scale(add(product([ga, dc, gb]), product([gb, dc, ga])), F(1, 2))
    determinant = selector[0][0]*selector[1][1]-selector[0][1]*selector[1][0]
    require(determinant == F(-9, 87616), 'Entrywise positive selfadjoint physical-resolvent selector can have a negative eigenvalue')
    return {'resolvent_scales': [10, 40, 160], 'normalized_selector_operator_residuals': errors,
            'non_PSD_selector_determinant_exact': str(determinant),
            'scope': 'Exact leading-order identities and three numerical residuals on a small fixture; these do not certify an all-model asymptotic error rate.'}


def fractional_and_resolvent_polynomial_checks() -> dict:
    cases = 0
    for theta in (F(0), F(1, 5), F(1, 3), F(1, 2), F(2, 3), F(1)):
        for degree in (1, 2, 5, 12):
            coefficients, coefficient = [], theta
            for l in range(1, degree+1):
                coefficients.append(coefficient)
                coefficient *= (l-theta)/(l+1)
            require(min(coefficients) >= 0 and sum(coefficients) <= 1,
                    'Fractional binomial subtraction weights are nonnegative with total mass at most one')
            remaining = F(1)
            for l in range(1, degree+1):
                remaining *= 1-theta/l
            require(1-sum(coefficients) == remaining,
                    'Finite fractional-binomial tail mass has its independent exact product formula')
            monomials = [F(1)]+[F(0)]*degree
            for l, c in enumerate(coefficients, 1):
                for j in range(l+1):
                    monomials[j] -= c*math.comb(l, j)*(-1)**j
            require(sum(abs(x) for x in monomials) <= 2**(degree+1),
                    'Clock-polynomial monomial coefficient mass fits the stated bound')
            for base in (F(1, 2), F(2, 3), F(3, 4), F(1)):
                x, exact_power = base**theta.denominator, base**theta.numerator
                h = 1-sum((c*(1-x)**l for l, c in enumerate(coefficients, 1)), F())
                expanded = sum((c*x**j for j, c in enumerate(monomials)), F())
                require(expanded == h and exact_power <= h <= 1,
                        'Exact rational powers verify the fractional upper polynomial and its expanded representation')
                require(0 <= h-exact_power <= (1-x)**(degree+1),
                        'Exact finite fractional residual has the high-frequency filter bound')
                cases += 1
    pi0, q, pih = physical_model(F(3, 2))
    tick, s, degree, cutoff = .4, 1.3, 12, 12
    lam = tick*s
    r = math.exp(-lam)
    coefficients, quadrature_errors = [], []
    for l in range(1, degree+1):
        def integrand(theta: float) -> float:
            coefficient = theta
            for j in range(1, l):
                coefficient *= (j-theta)/(j+1)
            return lam*math.exp(-lam*theta)/(1-r)*coefficient
        value, error = quad(integrand, 0., 1., epsabs=1e-13, epsrel=1e-13)
        coefficients.append(value)
        quadrature_errors.append(error)
    e = expm(tick*array(q))
    high_filter = np.eye(4)-e
    h = np.eye(4)
    power = np.eye(4)
    for coefficient in coefficients:
        power = power @ high_filter
        h -= coefficient*power
    geom, power = np.zeros((4, 4)), np.eye(4)
    for j in range(cutoff+1):
        geom += (1-r)*r**j*power
        power = power @ e
    approximation = geom @ h
    exact = s*np.linalg.inv(s*np.eye(4)-array(q))
    weights = np.sqrt(np.array([float(x) for x in pih]))
    symmetric_approximation = weights[:, None]*approximation/weights[None, :]
    require(np.max(np.abs(symmetric_approximation-symmetric_approximation.T)) < 2e-13,
            'Clock resolvent polynomial is stationary selfadjoint numerically')
    eigenvalues = np.linalg.eigvalsh(symmetric_approximation)
    require(min(eigenvalues) >= -2e-13 and max(eigenvalues) <= 1+2e-13,
            'Clock resolvent polynomial is a spectral PSD contraction in the physical stationary norm')
    high_power = np.linalg.matrix_power(high_filter, degree+1)
    residuals = []
    for vector in (np.ones(4), np.array([1., 0., 0., 0.]), np.array([0., 1., -1., .5])):
        residual = np.linalg.norm(weights*((exact-approximation) @ vector))
        bound = r**(cutoff+1)*np.linalg.norm(weights*vector)+np.linalg.norm(weights*(high_power @ vector))
        require(residual <= bound+5e-13, 'Physical clock-resolvent residual obeys the geometric-tail plus vector-filter estimate')
        residuals.append({'residual': rounded(float(residual)), 'bound': rounded(float(bound))})
    eigen_e = np.linalg.eigvalsh(weights[:, None]*e/weights[None, :])
    scalar_residuals = []
    for x in eigen_e:
        exact_h = lam*(1-r*x)/((1-r)*(lam-math.log(x)))
        poly_h = 1-sum(c*(1-x)**l for l, c in enumerate(coefficients, 1))
        require(-2e-13 <= poly_h-exact_h <= (1-x)**(degree+1)+2e-13,
                'Averaged fractional polynomial has the predicted scalar spectral remainder')
        scalar_residuals.append(rounded(float(poly_h-exact_h)))
    return {'exact_fractional_cases': cases, 'max_fractional_degree': 12,
            'physical_resolvent_polynomial': {'tick': tick, 's': s, 'M': degree, 'J': cutoff,
                'clock_degree': degree+cutoff, 'quadrature_tolerance': 1e-13,
                'largest_quadrature_error_estimate': rounded(max(quadrature_errors)),
                'polynomial_spectral_extrema': [rounded(float(min(eigenvalues))), rounded(float(max(eigenvalues)))],
                'vector_residuals': residuals, 'averaged_fractional_spectral_residuals': scalar_residuals},
            'scope': 'Rational fractional identities are exact; averaged physical coefficients and matrix residuals use labeled float64 quadrature. Spectral PSD does not assert entrywise positivity.'}


def natural_heat_and_polynomial_checks() -> dict:
    mu, k, d0, d1 = base_model()
    b0, b1, killing, old_time = F(2, 3), F(8, 27), F(5), F(3, 5)
    eta = (b0-b1)/killing
    time = old_time/eta
    b = add(scale(d0, b0), scale(d1, b1))
    new_exponent = scale(add(scale(k, eta), b, F(-1)), time)
    old_exponent = add(scale(add(k, scale(d0, killing), F(-1)), old_time),
                       scale(eye(3), -b1*time))
    require(new_exponent == old_exponent, 'Natural-killing rescaling is an exact generator identity before exponentiation')
    new_heat = expm(array(new_exponent))
    old_heat = math.exp(-float(b1*time))*expm(float(old_time)*array(add(k, scale(d0, killing), F(-1))))
    residual = float(np.linalg.norm(new_heat-old_heat, 2))
    require(residual < 2e-14, 'Rescaled natural killed heat agrees numerically with the factored old killed heat')
    killed_generator = array(add(k, b, F(-1)))
    z = np.linalg.inv(np.eye(3)-float(time)*killed_generator)
    weights = np.sqrt(np.array([float(x) for x in mu]))
    zs = weights[:, None]*z/weights[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(zs)
    functional = (eigenvectors*np.exp(1-1/eigenvalues)) @ eigenvectors.T
    expected = weights[:, None]*expm(float(time)*killed_generator)/weights[None, :]
    functional_residual = float(np.linalg.norm(functional-expected, 2))
    require(functional_residual < 2e-14, 'The universal f(z)=exp(1-1/z) recovers killed heat from its resolvent spectrum')
    shifted = [[1], [-1, 2]]
    for m in range(1, 64):
        next_poly = [-2*x for x in shifted[-1]]+[0]
        for j, value in enumerate(shifted[-1]):
            next_poly[j+1] += 4*value
        for j, value in enumerate(shifted[-2]):
            next_poly[j] -= value
        shifted.append(next_poly)
    require(shifted[2] == [1, -8, 8], 'Shifted Chebyshev recurrence has the correct initial scaling')
    for m, polynomial in enumerate(shifted):
        require(sum(abs(x) for x in polynomial) <= 7**m,
                'Shifted Chebyshev monomial coefficient mass obeys the heat-polynomial bound')
    stirling = [[1]]
    for k_order in range(1, 17):
        previous = stirling[-1]
        row = [0]*(k_order+1)
        for j in range(1, k_order+1):
            row[j] = previous[j-1]+(j*previous[j] if j < len(previous) else 0)
        stirling.append(row)
        bell_majorant = sum(3**j*math.factorial(j)**2*row[j] for j in range(1, k_order+1))
        middle_majorant = k_order*3**k_order*math.factorial(k_order)*k_order**k_order
        require(bell_majorant <= middle_majorant,
                'Finite Stirling-number coefficients fit the stated composition-derivative majorant')
    samples = 512
    angles = (np.arange(samples)+.5)*math.pi/samples
    nodes = (1+np.cos(angles))/2
    values = np.exp(1-1/nodes)
    coefficients = np.array([2/samples*np.dot(values, np.cos(j*angles)) for j in range(65)])
    coefficients[0] /= 2
    grid = np.linspace(0., 1., 1001)
    exact = np.zeros_like(grid)
    exact[1:] = np.exp(1-1/grid[1:])
    errors = []
    for degree in (8, 16, 32, 64):
        approximate = np.polynomial.chebyshev.chebval(2*grid-1, coefficients[:degree+1])
        errors.append(float(np.max(np.abs(approximate-exact))))
    require(all(later < earlier for earlier, later in zip(errors, errors[1:])),
            'Sampled Chebyshev heat-polynomial residuals decrease across the tested degrees')
    return {'toy_eta_exact': str(eta), 'toy_old_killing_exact': str(killing),
            'natural_heat_factorization_residual': rounded(residual),
            'heat_from_resolvent_spectral_residual': rounded(functional_residual),
            'max_exact_shifted_Chebyshev_degree': 64, 'max_exact_Stirling_order': 16,
            'sampled_heat_polynomial': {'degrees': [8, 16, 32, 64], 'cosine_samples': samples,
                                      'test_grid_points': len(grid), 'maximum_grid_residuals': list(map(rounded, errors))},
            'scope': 'Rational rescaling identity and finite coefficient majorants are exact. Spectral and sampled-grid heat errors are numerical diagnostics, not uniform-error certificates; the toy killing rate is five, not the target constant 10^9.'}


def exponent_budget_checks() -> dict:
    # Representative fixed constants certify the polynomial bookkeeping;
    # they are not values of the physical model's unspecified constants.
    # Use log(q+1)<=q, coefficient log mass<=2q^6, L=3q^5,
    # M=100q^6, J=100q^7, clock a=1/2, z_min=1/q, and
    # target-filter log decay >=1/4 per degree.
    cases = []
    for n in (1, 2, 4, 8, 16):
        q = n+1
        length, m, cutoff = 3*q**5, 100*q**6, 100*q**7
        log_mass_upper = 2*q**6
        filter_tail_log = 2*length+log_mass_upper-F(m, 4)
        integer_tail_log = 2*length+log_mass_upper-F(cutoff+1, 2*q)
        require(filter_tail_log <= -20*q**6 and integer_tail_log <= -20*q**6,
                'Representative deterministic tails beat the expanded coefficient mass')
        noise_log = 2*(length+1)*(m+cutoff+1)+log_mass_upper
        require(noise_log <= 1610*q**12,
                'Full length-times-clock-degree noise cost has twelfth-power growth')
        log_delta_inverse = 4000*q**12
        require(noise_log-F(log_delta_inverse, 2) <= -400*n,
                'Representative inverse-accuracy budget suppresses the square-root observation noise')
        horizon = 2*(length*(m+cutoff)+2+m+1)
        require(horizon <= 1500*q**12,
                'Finite sampled-word horizon fits the same twelfth-power bookkeeping')
        cases.append({'n': n, 'resolvent_word_length': length, 'fractional_degree_M': m,
                      'integer_cutoff_J': cutoff, 'maximum_tick_bound': horizon,
                      'deterministic_filter_log_upper_exact': str(filter_tail_log),
                      'deterministic_integer_log_upper_exact': str(integer_tail_log),
                      'noise_log_upper': noise_log})
    require(1+4 == 5 and 5+7 == 12 and 7-1 == 6,
            'Heat expansion, clock degree and minimum-frequency losses have the canonical exponent accounting')
    return {'representative_cases': cases,
            'scope': 'Exact arithmetic for explicitly stated representative constants only. This checks the degree and normalization accounting, not the theorem constants, asymptotic starting index, or universal proof.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/fixed_clock_observability.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
              'arithmetic': 'Exact fractions.Fraction and integer identities plus explicitly separated float64 matrix exponentials, quadrature and sampled polynomial residuals',
              'A_start_and_stationary_adjoint': a_start_and_adjoint_checks(),
              'physical_Schur_and_binary_elimination': schur_and_binary_elimination_checks(),
              'positive_selector_leading_identity': positive_selector_leading_checks(),
              'fractional_and_physical_resolvent_polynomials': fractional_and_resolvent_polynomial_checks(),
              'natural_heat_and_polynomial_calculus': natural_heat_and_polynomial_checks(),
              'fixed_clock_exponent_bookkeeping': exponent_budget_checks(),
              'largest_dense_matrix_dimension': 4,
              'large_target_allocated': False,
              'limitations': ['Finite fixtures and small numerical residuals do not prove the fixed-clock theorem or uniform reconstruction estimates.',
                              'The exact recursion fixture uses rational stationary kernels; actual fixed-clock semigroups are checked separately in floating-point arithmetic.',
                              'No large logical target, long chain, or extremely small asymptotic rate is simulated.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_names = ['FIXED_CLOCK_GRAM_OBSERVABILITY.md',
                   'FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md',
                   'FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
