#!/usr/bin/env python3
"""Small certificates for positive label selection and state/EPR comparisons.

Exact rational algebra, finite high-precision scalar checks, and labeled
small-matrix numerical diagnostics supplement the proofs; they do not prove
the asymptotic all-model theorems.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm


CHECKS = 0


def require(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zero(n: int) -> list[list[F]]:
    return [[F() for _ in range(n)] for _ in range(n)]


def diag(values: list[F]) -> list[list[F]]:
    return [[values[i] if i == j else F() for j in range(len(values))] for i in range(len(values))]


def eye(n: int) -> list[list[F]]:
    return diag([F(1)]*n)


def scale(a: list[list[F]], value: F) -> list[list[F]]:
    return [[value*x for x in row] for row in a]


def add(a: list[list[F]], b: list[list[F]], value: F = F(1)) -> list[list[F]]:
    return [[x+value*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mm(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F())
             for j in range(len(b[0]))] for i in range(len(a))]


def product(factors: list[list[list[F]]]) -> list[list[F]]:
    out = eye(len(factors[0]))
    for factor in factors:
        out = mm(out, factor)
    return out


def power(a: list[list[F]], exponent: int) -> list[list[F]]:
    out = eye(len(a))
    for _ in range(exponent):
        out = mm(out, a)
    return out


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    rows = [a[i][:]+eye(n)[i] for i in range(n)]
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
    require(mm(a, out) == mm(out, a) == eye(n), 'Exact inverse solves both defining equations')
    return out


def adjoint(a: list[list[F]], mu: list[F]) -> list[list[F]]:
    return [[mu[j]*a[j][i]/mu[i] for j in range(len(mu))] for i in range(len(mu))]


def check_generator(k: list[list[F]], mu: list[F]) -> None:
    require(sum(mu) == 1 and min(mu) > 0, 'Hidden stationary law is a positive probability vector')
    require(all(sum(row) == 0 for row in k), 'Generator rows sum to zero')
    require(all(k[i][j] >= 0 for i in range(len(k)) for j in range(len(k)) if i != j),
            'Off-diagonal generator rates are nonnegative')
    require(all(sum(mu[i]*k[i][j] for i in range(len(k))) == 0 for j in range(len(k))),
            'Stationary incoming and outgoing fluxes agree exactly')


def array(a: list[list[F]]) -> np.ndarray:
    return np.array([[float(x) for x in row] for row in a])


def rounded(value: float) -> float:
    return float(f'{value:.12g}')


def certify_operator_bound(a: list[list[F]], mu: list[F], bound: F) -> None:
    form = mm(diag(mu), add(scale(eye(len(mu)), bound*bound), mm(adjoint(a, mu), a), F(-1)))
    require(form == [list(row) for row in zip(*form)], 'Squared operator-bound form is symmetric exactly')
    for j in range(len(mu)):
        pivot = form[j][j]
        require(pivot > 0, 'Positive rational LDL pivots certify the operator-norm upper bound')
        for i in range(j+1, len(mu)):
            for k in range(j+1, len(mu)):
                form[i][k] -= form[i][j]*form[j][k]/pivot


def biased_cycle(mu: list[F], bias: F) -> list[list[F]]:
    k = zero(3)
    for i in range(3):
        k[i][(i+1) % 3] = (1+bias)/(3*mu[i])
        k[i][(i-1) % 3] = (1-bias)/(3*mu[i])
        k[i][i] = -sum(k[i])
    return k


def entropy_production(k: list[list[F]], mu: list[F]) -> float:
    reverse = adjoint(k, mu)
    value = 0.
    for i in range(len(k)):
        for j in range(len(k)):
            if i != j and k[i][j]:
                if not reverse[i][j]:
                    return math.inf
                value += float(mu[i]*k[i][j])*math.log(float(k[i][j]/reverse[i][j]))
    return value


def row_kl_rates(k: list[list[F]], other: list[list[F]]) -> list[float]:
    out = []
    for i in range(len(k)):
        value = 0.
        for j in range(len(k)):
            if i != j:
                a, b = float(k[i][j]), float(other[i][j])
                value += (a*math.log(a/b) if a else 0.)-a+b
        require(value >= -1e-14, 'Each continuous-time row KL rate is nonnegative')
        out.append(value)
    return out


def reversibilization_checks() -> dict:
    cases = []
    for mu in ([F(1, 3)]*3, [F(1, 4), F(1, 4), F(1, 2)]):
        for bias in (F(0), F(1, 100), F(1, 5), F(1, 2), F(9, 10), F(1)):
            k = biased_cycle(mu, bias)
            check_generator(k, mu)
            reverse = adjoint(k, mu)
            sym = scale(add(k, reverse), F(1, 2))
            check_generator(reverse, mu)
            check_generator(sym, mu)
            require(adjoint(sym, mu) == sym, 'Arithmetic reversibilization has exact detailed balance')
            require(all(k[i][i] == reverse[i][i] == sym[i][i] for i in range(3)),
                    'Time reversal and arithmetic reversibilization preserve every individual exit rate')
            sigma = entropy_production(k, mu)
            d = sum(float(w)*x for w, x in zip(mu, row_kl_rates(k, sym)))
            if math.isfinite(sigma):
                expected = 2*float(bias)*math.log(float((1+bias)/(1-bias))) if bias else 0.
                require(abs(sigma-expected) < 2e-13, 'Biased-cycle entropy production matches the independent flux formula')
                require(d <= sigma/4+2e-14, 'Stationary path KL rate fits the sharpened quarter-EPR bound')
            else:
                require(d <= 2*math.log(2)+1e-13, 'One-way cycle has infinite EPR but finite KL to its symmetrization')
            # Full zero-field model: external flux pairs balance exactly and
            # every hidden flux is half its hidden-only stationary value.
            q, pi0 = physical_generator(k, mu, F(1))
            sigma_full = entropy_production(q, pi0)
            require((math.isinf(sigma) and math.isinf(sigma_full)) or abs(sigma_full-sigma/2) < 2e-13,
                    'Full zero-field entropy production is exactly one half of the hidden EPR')
            cases.append({'hidden_law_exact': list(map(str, mu)), 'bias_exact': str(bias),
                          'hidden_EPR': rounded(sigma) if math.isfinite(sigma) else 'infinity',
                          'stationary_KL_rate_to_arithmetic_reverse': rounded(d),
                          'full_zero_field_EPR': rounded(sigma_full) if math.isfinite(sigma_full) else 'infinity'})
    derivative_cases = []
    for t in (F(0), F(1, 10), F(1, 3), F(1, 2), F(9, 10)):
        second = 2*(1+t*t)/(1-t*t)**2-2/(1-t*t)
        require(second == 4*t*t/(1-t*t)**2 >= 0,
                'The pairwise quarter-EPR comparison has the exact nonnegative second derivative')
        x = float(t)
        f_value = x*math.log((1+x)/(1-x))-2*((1+x)*math.log1p(x)+(1-x)*math.log1p(-x))
        require(f_value >= -2e-15, 'Finite Jensen-Shannon versus Jeffreys flux examples have the asserted sign')
        derivative_cases.append({'t_exact': str(t), 'F_second_derivative_exact': str(second), 'F_numeric': rounded(f_value)})
    return {'biased_cycle_cases': cases, 'quarter_EPR_pairwise_function': derivative_cases,
            'scope': 'Exact generator, stationarity and exit identities plus finite logarithmic evaluations; the all-pair inequality is proved analytically in the companion note.'}


def physical_generator(k: list[list[F]], mu: list[F], base: F) -> tuple[list[list[F]], list[F]]:
    # gamma=1/2, hidden colors (-,-,+), h=2 log(base), external k=1.
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
    return q, pi0


def reset_age_and_controlled_mean_checks() -> dict:
    mu, bias = [F(1, 4), F(1, 4), F(1, 2)], F(1, 5)
    k = biased_cycle(mu, bias)
    sym = scale(add(k, adjoint(k, mu)), F(1, 2))
    drows = row_kl_rates(k, sym)
    d = sum(float(w)*x for w, x in zip(mu, drows))
    sigma = entropy_production(k, mu)
    base, external_k = F(11, 10), F(1)
    r_bound = base**3
    alpha = external_k/r_bound
    reset = zero(4)
    for i in range(1, 4):
        reset[i][0], reset[i][i] = alpha, -alpha
    density_residuals = []
    for field_base in (1/base, F(1), base):
        q, pi0 = physical_generator(k, mu, field_base)
        residual = add(q, reset, F(-1))
        require(all(residual[i][j] >= 0 for i in range(4) for j in range(4) if i != j)
                and all(sum(row) == 0 for row in residual),
                'Uniform reset subtraction leaves a valid residual physical generator')
        for start, c0 in ((np.array([1., 0., 0., 0.]), 0.), (np.array([float(x) for x in pi0]), .5)):
            for duration in (.05, .5, 2., 7.):
                law = start @ expm(duration*array(residual))
                ratios = law[1:]/np.array([float(x) for x in mu])
                bound = c0+float(external_k*r_bound)*duration
                require(max(ratios) <= bound+2e-13,
                        'Finite residual hidden densities obey the stationary-law domination bound')
                density_residuals.append(rounded(float(bound-max(ratios))))
    age_cases = []
    for r in (F(1), r_bound, F(3)):
        a = 1/float(r)
        for horizon in (.1, 1., 10.):
            integral, error = quad(lambda age: a*math.exp(-a*age)*float(r)*age*age/2,
                                   0., horizon, epsabs=1e-13, epsrel=1e-13)
            direct = integral+math.exp(-a*horizon)*(horizon/2+float(r)*horizon*horizon/2)
            x = a*horizon
            closed = float(r)**3*(1-(1+x)*math.exp(-x))+(horizon/2)*math.exp(-x)
            deficit = math.exp(-x)/a*(float(r)**2+(float(r)**2-.5)*x)
            require(abs(direct-closed) <= 2e-12*max(1., abs(closed)),
                    'Independent quadrature reproduces the exact reset-age expression')
            require(abs(float(r)**3-closed-deficit) <= 2e-12*max(1., float(r)**3)
                    and deficit >= 0 and closed <= float(r)**3+1e-13,
                    'Initial-preparation contribution is absorbed in the sharp uniform age bound')
            age_cases.append({'R_exact': str(r), 'horizon': horizon, 'age_factor': rounded(closed),
                              'uniform_factor_R_cubed': rounded(float(r)**3), 'quadrature_error_estimate': rounded(error)})
    protocols = [[(base, .1)], [(base, 1.)], [(base, .3), (1/base, .7), (base, 1.1)],
                 [(1/base, .2), (base, .4), (F(1), 3.)]]
    protocol_cases = []
    for protocol in protocols:
        p = np.array([.5]+[float(x)/2 for x in mu])
        qlaw = p.copy()
        for field_base, duration in protocol:
            qk, _ = physical_generator(k, mu, field_base)
            qs, _ = physical_generator(sym, mu, field_base)
            p = p @ expm(duration*array(qk))
            qlaw = qlaw @ expm(duration*array(qs))
        endpoint_kl = float(np.sum(p*np.log(p/qlaw)))
        mean_difference = 2*abs(float(p[0]-qlaw[0]))
        kl_bound = d*float(r_bound)**3
        mean_bound = math.sqrt(float(r_bound)**3*sigma/2)
        require(endpoint_kl <= kl_bound+2e-13 and mean_difference <= mean_bound+2e-13,
                'Finite switched physical means and endpoint laws obey the uniform reversibilization estimates')
        protocol_cases.append({'protocol': [[str(x), t] for x, t in protocol],
                               'endpoint_KL': rounded(endpoint_kl), 'KL_bound': rounded(kl_bound),
                               'absolute_mean_difference': rounded(mean_difference), 'mean_bound': rounded(mean_bound)})
    return {'R_exact': str(r_bound), 'reset_rate_exact': str(alpha),
            'minimum_density_domination_slack': min(density_residuals), 'age_cases': age_cases,
            'finite_protocol_cases': protocol_cases,
            'scope': 'Residual generators and reset rates are exact; density, quadrature and endpoint diagnostics use finite float64 examples. They do not verify all protocols or the path relative-entropy theorem by simulation.'}


def finite_EPR_regularization_checks() -> dict:
    mu = [F(1, 4), F(1, 4), F(1, 2)]
    k = biased_cycle(mu, F(1))
    reverse = adjoint(k, mu)
    cap, cases = max(-k[i][i] for i in range(3)), []
    for epsilon in (F(1, 1000), F(1, 20), F(1, 4)):
        regularized = add(scale(k, 1-epsilon), scale(reverse, epsilon))
        check_generator(regularized, mu)
        require(all(regularized[i][i] == k[i][i] for i in range(3)),
                'Finite-EPR regularization preserves each original hidden exit')
        ratio_bound = (1-epsilon)/epsilon
        reverse_regularized = adjoint(regularized, mu)
        for i in range(3):
            for j in range(3):
                if i != j:
                    ratio = regularized[i][j]/reverse_regularized[i][j]
                    require(1/ratio_bound <= ratio <= ratio_bound,
                            'Regularized forward/backward flux ratios have the exact epsilon envelope')
            mismatch = sum(abs(regularized[i][j]-k[i][j]) for j in range(3) if i != j)/2
            require(mismatch <= epsilon*cap, 'Equal-exit coupling mismatch has the sharp epsilon-times-cap bound')
        sigma = entropy_production(regularized, mu)
        bound = float(cap)*math.log(float(ratio_bound))
        require(math.isfinite(sigma) and sigma <= bound+2e-13,
                'Regularized one-way cycle has finite EPR within the shared-exit logarithmic bound')
        cases.append({'epsilon_exact': str(epsilon), 'exit_cap_exact': str(cap),
                      'hidden_EPR': rounded(sigma), 'hidden_EPR_upper': rounded(bound)})
    return {'cases': cases, 'original_hidden_EPR': 'infinity',
            'scope': 'Finite flux/rate certificates for regularization. The all-horizon mean perturbation bound is proved through common-reset coupling in the accompanying note.'}


def soft_features(k: list[list[F]], x_values: list[F], s: F) -> tuple[list[list[F]], list[list[F]]]:
    n, lower, upper = len(k), F(1, 4), F(3, 4)
    x, y = diag(x_values), diag([1-v for v in x_values])
    b = diag([lower+(upper-lower)*v for v in x_values])
    g0 = inverse(add(scale(eye(n), s+1), k, F(-1)))
    gh = inverse(add(add(scale(eye(n), s), k, F(-1)), b))
    fplus = scale(add(product([g0, x, gh]), product([gh, x, g0])), s*s/2)
    fminus = scale(add(product([g0, y, gh]), product([gh, y, g0])), s*s/2)
    z0, zh = scale(g0, s), scale(gh, s)
    recovered_plus = add(scale(add(z0, zh, F(-1)), s/(upper-lower)),
        scale(add(mm(z0, zh), mm(zh, z0)), -(lower-1)/(2*(upper-lower))))
    recovered_minus = add(scale(add(mm(z0, zh), mm(zh, z0)), F(1, 2)), recovered_plus, F(-1))
    require(recovered_plus == fplus and recovered_minus == fminus,
            'Two natural resolvents recover both soft label features with their exact normalization')
    return fplus, fminus


def positive_selector_checks() -> dict:
    target_mu = [F(1, 5)]*5
    target_k = [[(F(1, 10) if i != j else F(-2, 5)) for j in range(5)] for i in range(5)]
    target_grid = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    rival_mu = [F(1, 10), F(1, 5), F(1, 4), F(3, 20), F(3, 10)]
    rival_k = [[1000*(rival_mu[j]-(1 if i == j else 0)) for j in range(5)] for i in range(5)]
    rival_grid = [F(0), F(1, 7), F(2, 5), F(7, 9), F(1)]
    scalar_cases = []
    for index, (a, b) in enumerate(((0, 1), (1, 3), (1, 1), (3, 1), (1, 0))):
        phi = [x**(2*a)*(1-x)**(2*b) for x in target_grid]
        w = phi[index]
        rho = max(value/w for j, value in enumerate(phi) if j != index)
        require(w > 0 and rho < 1, 'Every rational beta selector has a unique maximum on the target label list')
        for m in (1, 2, 5):
            require(max((value/w)**m for j, value in enumerate(phi) if j != index) == rho**m,
                    'Diagonal beta-selector suppression is exactly the power of the finite-label ratio')
        scalar_cases.append({'target_feature_exact': str(target_grid[index]), 'a': a, 'b': b,
                             'w_exact': str(w), 'rho_exact': str(rho)})
    examples = []
    for name, mu, k, grid, s in (('bounded_target', target_mu, target_k, target_grid, F(4096)),
                                ('fast_off_grid_rival', rival_mu, rival_k, rival_grid, F(4))):
        check_generator(k, mu)
        require(adjoint(k, mu) == k, 'Selector fixture generator is reversible')
        fp, fm = soft_features(k, grid, s)
        require(mm(fp, fm) != mm(fm, fp), 'Soft label features in the fixture do not commute')
        for feature in (fp, fm):
            require(adjoint(feature, mu) == feature and all(x >= 0 for row in feature for x in row),
                    'Exact soft feature is entrywise nonnegative and selfadjoint on off-grid as well as target labels')
        # Central target label: a=b=1, phi=x^2(1-x)^2, w=1/16.
        t = product([fp, fm, fm, fp])
        bfactor = mm(fp, fm)
        require(t == mm(bfactor, adjoint(bfactor, mu)), 'Noncommuting selector has an exact B B* PSD certificate')
        normalized = scale(t, F(16))
        selected = power(normalized, 3)
        selected_factor = mm(normalized, scale(bfactor, F(4)))
        require(selected == mm(selected_factor, adjoint(selected_factor, mu)),
                'Odd selector power retains an exact PSD factorization after normalization')
        require(adjoint(selected, mu) == selected and all(x >= 0 for row in selected for x in row),
                'Powered rival selector remains entrywise nonnegative and selfadjoint')
        if name == 'bounded_target':
            c_f = F(11, 4)  # target Lambda=1/2 and b_+=3/4
            certify_operator_bound(add(fp, diag(grid), F(-1)), mu, c_f/s)
            polynomial = diag([x*x*(1-x)**2 for x in grid])
            certify_operator_bound(add(t, polynomial, F(-1)), mu, 4*c_f/s)
            c_i, m_i, rho_i = 4*c_f*16, 3, F(9, 16)
            selector_bound = rho_i**m_i+(m_i*c_i/s)*(1+c_i/s)**(m_i-1)
            require(selector_bound < F(1, 2), 'The finite target selector error certificate is nontrivial')
            certify_operator_bound(add(selected, diag([F(0), F(0), F(1), F(0), F(0)]), F(-1)),
                                   mu, selector_bound)
        examples.append({'fixture': name, 'hidden_states': 5, 'feature_values_exact': list(map(str, grid)),
                         's_exact': str(s), 'largest_hidden_exit_exact': str(max(-k[i][i] for i in range(5))),
                         'selector_entrywise_nonnegative': True, 'selector_exact_Gram_factorization': True})
    off_grid_gain = F(1, 16)/(F(2, 5)**2*F(3, 5)**2)
    require(off_grid_gain == F(625, 576) > 1,
            'A valid off-grid rival feature can exceed the target-normalized beta peak, so selectors are not assumed contractive')
    return {'exact_beta_cases': scalar_cases, 'matrix_examples': examples,
            'off_grid_normalized_scalar_gain_exact': str(off_grid_gain),
            'scope': 'Five-state rational feature fixtures and a fast off-grid reversible rival; the canonical nineteen-level target is checked only through scalar label/exponent calculations below.'}


def canonical_label_and_budget_checks() -> dict:
    mp.mp.dps = 80
    bound = mp.mpf(9)/100
    labels = [mp.mpf(j)/100 for j in range(-9, 10)]
    b_lower, b_upper = mp.exp(-1-bound), mp.exp(-1+bound)
    xs = [(mp.exp(g-1)-b_lower)/(b_upper-b_lower) for g in labels]
    cases = []
    for index, x in enumerate(xs):
        a, b = ((0, 1) if index == 0 else (1, 0) if index == 18 else (index, 18-index))
        def log_phi(value: mp.mpf) -> mp.mpf:
            if (a and value == 0) or (b and value == 1):
                return mp.ninf
            return (2*a*mp.log(value) if a else 0)+(2*b*mp.log1p(-value) if b else 0)
        log_w = log_phi(x)
        log_rho = max(log_phi(y)-log_w for j, y in enumerate(xs) if j != index)
        require(log_rho < 0, 'All nineteen canonical label selectors have a strict finite-grid maximum at H=1')
        beta = min(mp.mpf(1), -log_rho)
        c_f = 7+b_upper
        degree = 2*a+2*b
        log_c = mp.log(degree*c_f)-log_w
        examples = []
        for q in (2, 3, 5):
            m = int(mp.ceil(120*q/beta))
            require(m*log_rho <= -120*q, 'Canonical beta power meets the intended off-label suppression')
            log_perturbation = mp.log(m)+log_c-200*q+(m-1)*mp.log1p(mp.exp(log_c-200*q))
            log_total = mp.log(mp.exp(-120*q)+mp.exp(log_perturbation))
            require(log_total <= -110*q, 'Explicit finite canonical constants satisfy the target selector error allocation')
            examples.append({'q': q, 'power_m': m, 'log_target_error_upper': mp.nstr(log_total, 14)})
        cases.append({'gamma': str(F(index-9, 100)), 'a': a, 'b': b,
                      'log_w': mp.nstr(log_w, 14), 'log_rho': mp.nstr(log_rho, 14), 'allocations': examples})
    budget_cases = []
    for n in (1, 2, 4, 8, 16):
        q = n+1
        length, m, log_mass = 3*q*q, 100*q**3, 2*q**3
        # Illustrative constants only: filter log decay>=1/4, clock=1/2.
        filter_log = 2*length+log_mass-F(m, 4)
        # exp(20q)-1 >= (20q)^4/24 avoids enormous exponentials.
        integer_log = 2*length+log_mass-F((20*q)**4, 48)
        require(filter_log <= -20*q**3 and integer_log <= -20*q**3,
                'Representative fifth-power-route tails beat coefficient mass with integer cutoff zero')
        noise_log = 2*(length+1)*(m+1)+log_mass
        require(noise_log <= 810*q**5 and noise_log-1000*q**5 <= -400*n,
                'Representative length-times-degree recovery cost has a safe fifth-power accuracy budget')
        ticks = 2*(length*m+m+1)
        require(ticks <= 900*q**5, 'Representative finite observing horizon has fifth-power growth')
        budget_cases.append({'n': n, 'word_length': length, 'fractional_degree': m, 'integer_cutoff': 0,
                             'noise_log_upper': noise_log, 'maximum_ticks': ticks})
    return {'canonical_field_H': 1, 'scalar_precision_decimal_digits': 80,
            'nineteen_label_cases': cases, 'representative_fifth_power_budgets': budget_cases,
            'scope': 'Canonical label allocations are finite high-precision scalar checks at H=1. Degree budgets use explicitly representative constants and do not determine the theorem constants or starting index for arbitrary H and clock.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/prl_exploration.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                                           'scipy': scipy.__version__, 'mpmath': mp.__version__},
              'arithmetic': 'Exact fractions/integer identities; separately labeled float64 matrix exponentials/quadrature/logarithms and 80-digit scalar label checks',
              'arithmetic_reversibilization_and_EPR': reversibilization_checks(),
              'reset_age_and_controlled_means': reset_age_and_controlled_mean_checks(),
              'finite_EPR_regularization': finite_EPR_regularization_checks(),
              'positive_soft_label_selectors': positive_selector_checks(),
              'canonical_label_and_fifth_power_budgets': canonical_label_and_budget_checks(),
              'largest_dense_matrix_dimension': 5,
              'large_target_allocated': False,
              'limitations': ['Finite fixtures do not prove the all-model path-KL comparison, fixed-clock transfer, selector asymptotics, or state/EPR frontier.',
                              'The fast off-grid rival checks positivity without an inherited target label set; it is not a fitted small predictor.',
                              'All numerical protocol comparisons concern the listed small matrices and finite protocols only.',
                              'The fifth-power bookkeeping uses representative constants; no practical experimental accuracy or horizon is claimed.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_names = ['POSITIVE_LABEL_SELECTORS.md', 'TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md',
                   'ENTROPY_PRODUCTION_REVERSIBILIZATION.md', 'STATE_ENTROPY_PRODUCTION_TRADEOFF.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
