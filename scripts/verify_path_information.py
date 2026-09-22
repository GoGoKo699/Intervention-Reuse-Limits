#!/usr/bin/env python3
"""Exact and small deterministic checks of visible path information.

Killed-generator resolvents independently check the second-order no-exit
and waiting-density formulas. Exact integrations check the illustrative
quartic entropy-rate coefficient. These are algebraic consistency checks,
not statistical simulations, inference guarantees, or theorem proofs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def equal(actual: sp.Expr, expected: sp.Expr, message: str) -> None:
    require(sp.cancel(actual-expected) == 0, message)


def cases() -> list[dict]:
    half = sp.Rational(1, 2)
    return [
        {'name': 'two_hidden_rate_one', 'K': sp.Matrix([[-half, half], [half, -half]]),
         'mu': sp.Matrix([[half, half]]), 'b': sp.Matrix([1, -1]),
         'rates': [sp.Integer(1)], 'weights': [sp.Integer(1)]},
        {'name': 'two_hidden_rate_three', 'K': sp.Matrix([[-3*half, 3*half], [3*half, -3*half]]),
         'mu': sp.Matrix([[half, half]]), 'b': sp.Matrix([1, -1]),
         'rates': [sp.Integer(3)], 'weights': [sp.Integer(1)]},
        {'name': 'three_hidden_two_modes',
         'K': sp.Matrix([[-1, 1, 0], [1, -2, 1], [0, 1, -1]]),
         'mu': sp.Matrix([[sp.Rational(1, 3)]*3]), 'b': sp.Matrix([1, -1, 0]),
         'rates': [sp.Integer(1), sp.Integer(3)],
         'weights': [sp.Rational(1, 6), sp.Rational(1, 2)]},
    ]


def killed_resolvent_checks() -> list[dict]:
    """Expand matrix resolvents, without using the proposed time formulas."""
    z = sp.symbols('z', positive=True)
    results = []
    for case in cases():
        K, mu, b = (case[key] for key in ('K', 'mu', 'b'))
        n = K.rows
        k = sp.Rational(3, 2) if n == 3 else sp.Integer(1)
        I, one, B = sp.eye(n), sp.ones(n, 1), sp.diag(*b)
        require(K*one == sp.zeros(n, 1) and mu*K == sp.zeros(1, n),
                'Internal generator and stationary law')
        equal((mu*b)[0], 0, 'Centered sensitivity')
        W = (mu*B*b)[0]
        R = ((z+k)*I-K).inv()
        C_laplace = sp.cancel((mu*B*R*b)[0])
        spectral = sum(weight/(z+k+rate) for weight, rate in
                       zip(case['weights'], case['rates']))
        equal(C_laplace, spectral, 'Exact finite spectral measure')

        # Active experiment: killed matrix K-k diag(exp((b-1)h)).
        # Taylor coefficients are derivatives divided by factorials.
        M1 = k*(I-B)
        M2 = -k*(B-I)**2/2
        active0 = (mu*R*one)[0]
        active1 = (mu*R*M1*R*one)[0]
        active2 = (mu*(R*M2*R+R*M1*R*M1*R)*one)[0]
        equal(active0, 1/(z+k), 'No-exit zeroth coefficient')
        equal(active1, k/(z+k)**2, 'No-exit first coefficient')
        wanted = k**2/(z+k)**3-k*(1+W)/(2*(z+k)**2)
        wanted += k**2*C_laplace/(z+k)**2
        equal(active2, wanted, 'No-exit second coefficient vs spectral kernel')

        # Near-lumpability experiment: a=1+delta b, initial B entry mu*a,
        # exit vector k*a, and killed generator K-k diag(a).
        N1 = -k*B
        full1 = k*(mu*(B*R+R*B+R*N1*R)*one)[0]
        full2 = k*(mu*(B*R*B+B*R*N1*R+R*N1*R*B
                       +R*N1*R*N1*R)*one)[0]
        residual1 = k*(mu*(R*B+R*N1*R)*one)[0]
        residual2 = k*(mu*(R*N1*R*B+R*N1*R*N1*R)*one)[0]
        equal(full1, 0, 'Complete B wait has no first-order perturbation')
        equal(full2, k*z**2*C_laplace/(z+k)**2,
              'Complete B wait second coefficient')
        equal(residual1, 0, 'Stationary B residual has no first-order perturbation')
        equal(residual2, -k**2*z*C_laplace/(z+k)**2,
              'Stationary B residual second coefficient')
        equal(sp.cancel(full2).subs(z, 0), 0, 'Full wait second coefficient integrates to zero')
        equal(sp.diff(sp.cancel(full2), z).subs(z, 0), 0,
              'Full wait mean has zero second-order perturbation')
        equal(sp.cancel(residual2).subs(z, 0), 0,
              'Residual second coefficient integrates to zero')
        results.append({
            'name': case['name'], 'hidden_states': n,
            'internal_generator': [[str(K[i, j]) for j in range(n)] for i in range(n)],
            'centered_sensitivity': [str(x) for x in b],
            'kernel_mass': str(W),
            'kernel_rates': [str(x) for x in case['rates']],
            'kernel_weights': [str(x) for x in case['weights']],
            'visible_switch_rate_k': str(k),
            'active_no_exit_coefficients_orders_0_1_2': True,
            'complete_wait_first_and_second_coefficients': True,
            'stationary_residual_first_and_second_coefficients': True,
            'complete_wait_second_coefficient_mass_and_mean_zero': True,
        })
    return results


def active_event_checks() -> dict:
    t, s = sp.symbols('t s', nonnegative=True)
    no_exit2 = []
    for rate in (1, 3):
        integral = sp.integrate((t-s)*sp.exp(-rate*s), (s, 0, t))
        no_exit2.append(sp.exp(-t)*((t*t-2*t)/2+integral))
    gap = sp.simplify((no_exit2[1]-no_exit2[0]).subs(t, 1))
    wanted = sp.exp(-1)*(2+sp.exp(-3)-9*sp.exp(-1))/9
    require(sp.simplify(gap-wanted) == 0, 'Specified no-exit event gap')
    require(gap.is_negative is True, 'The specified no-exit coefficient gap is nonzero')

    # Under the stationary telegraph law, for ordered times s<t, the
    # four same-B-segment pair intensities share exp(-k(t-s)):
    # entry/exit, entry/occupation, occupation/exit, occupation/occupation.
    # Endpoint signs are +1; the continuous signed measure is -k dt.
    k, time, W = sp.symbols('k time W', positive=True)
    pair_terms = [k*k/2, -k*k/2, -k*k/2, k*k/2]
    equal(sum(pair_terms), 0, 'All off-diagonal path-score expectation terms cancel')
    equal(k*W*time/2-k*W*time/2, 0,
          'Expected atomic diagonal cancels path-score compensator')
    return {
        'normalization': 'k=W=1; no-exit coefficient gap scales by W at t=1/k',
        'gap_orientation': 'lambda=3k minus lambda=k',
        'conditional_B_no_exit_gap_exact': str(gap),
        'conditional_B_no_exit_gap_decimal': str(sp.N(gap, 50)),
        'joint_stationary_initial_B_event_gap_exact': str(gap/2),
        'gap_order': 'Second Taylor coefficient in active field h',
        'path_score_normalization': {
            'ordered_pair_terms_after_common_exponential': [str(x) for x in pair_terms],
            'off_diagonal_sum_zero': True,
            'expected_atomic_diagonal': 'k W integral_0^T u(t)^2 dt',
            'one_half_diagonal_cancels_compensator': True,
            'scope': 'Exact telegraph pair-intensity cancellation for the stated score, not simulation of path samples.',
        },
    }


def two_snapshot_checks() -> dict:
    """Independent full-generator response coefficients for endpoint data."""
    z, h, t = sp.symbols('z h t', positive=True)
    initial = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)]])
    readout = sp.Matrix([-1, 1, 1])
    correlations = []
    for rate in (1, 3):
        Q = sp.Matrix([[0, sp.exp(2*h)/2, sp.Rational(1, 2)],
                       [1, 0, sp.Rational(rate, 2)],
                       [sp.exp(-2*h), sp.Rational(rate, 2), 0]])
        for i in range(3):
            Q[i, i] = -sum(Q[i, j] for j in range(3) if j != i)
        pi = sp.diag(1/(1+sp.exp(2*h)), sp.exp(2*h)/(2*(1+sp.exp(2*h))),
                     sp.exp(2*h)/(2*(1+sp.exp(2*h))))
        require((pi*Q-Q.T*pi).applyfunc(sp.simplify) == sp.zeros(3),
                'Finite-field detailed balance for two-snapshot identity')
        coefficients = [Q.diff(h, j).subs(h, 0)/sp.factorial(j) for j in range(4)]
        R0 = (z*sp.eye(3)-coefficients[0]).inv()
        resolvents = [R0]
        for order in range(1, 4):
            source = sum((coefficients[j]*resolvents[order-j] for j in range(1, order+1)), sp.zeros(3))
            resolvents.append((R0*source).applyfunc(sp.cancel))
        mean3 = sp.cancel((initial*resolvents[3]*readout)[0])
        corr2 = sp.cancel((initial*sp.diag(*readout)*resolvents[2]*readout)[0])
        equal(mean3+corr2, -(1/z-1/(z+2))/3,
              'Two-snapshot second coefficient fixed by cubic mean and tanh expansion')
        correlations.append(sp.inverse_laplace_transform(corr2, z, t))
    gap = sp.simplify((correlations[1]-correlations[0]).subs(t, 1))
    wanted = -(sp.exp(-2)-sp.exp(-4))/2
    require(sp.simplify(gap-wanted) == 0, 'Explicit two-snapshot coefficient gap')
    return {
        'normalization': 'k=W=1; hidden rates lambda=1 and 3',
        'gap_orientation': 'lambda=3k minus lambda=k',
        'full_markov_states': 3,
        'exact_finite_field_detailed_balance': True,
        'resolvent_expansion_through_order': 3,
        'correlation_second_coefficient_and_mean_third_identity': True,
        'correlation_second_coefficient_gap_at_t_one': str(gap),
        'same_endpoint_sign_event_coefficient_gap': str(gap/2),
        'scope': 'Checks the two-snapshot signal coefficient; does not establish sample complexity.',
    }


def exact_waiting_and_kl_checks() -> dict:
    z, rate, q = sp.symbols('z rate q', positive=True)
    a = sp.Matrix([1+q, 1-q])
    mu = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
    K = sp.Matrix([[-rate/2, rate/2], [rate/2, -rate/2]])
    killed = K-sp.diag(*a)
    resolvent = (z*sp.eye(2)-killed).inv()
    density_laplace = sp.cancel((mu*sp.diag(*a)*resolvent*a)[0])
    denominator = (z+1)*(z+1+rate)-q*q
    density_wanted = ((1+q*q)*z+1+rate-q*q)/denominator
    equal(density_laplace, density_wanted, 'Exact symmetric full B density transform')
    equal(density_laplace.subs(z, 0), 1, 'Exact full B density normalized')
    equal(-sp.diff(density_laplace, z).subs(z, 0), 1, 'Exact mean B waiting time')
    residual_laplace = sp.cancel((mu*resolvent*a)[0])
    equal(residual_laplace, (1-density_laplace)/z,
          'Stationary B residual density equals complete B survival when k=1')

    # Direct Laplace transform of the proposed hyperbolic closed form.
    center = 1+rate/2
    omega2 = (rate/2)**2+q*q
    hyperbolic_laplace = ((1+q*q)*(z+center)+rate*(1-q*q)/2-2*q*q)/(
        (z+center)**2-omega2)
    equal(density_laplace, hyperbolic_laplace, 'Hyperbolic density vs killed resolvent')

    x, s = sp.symbols('x s', nonnegative=True)
    responses = []
    for lam in (1, 3):
        C = sp.exp(-lam*x)
        R = C-2*sp.integrate(sp.exp(-lam*s), (s, 0, x))
        R += sp.integrate((x-s)*sp.exp(-lam*s), (s, 0, x))
        require(sp.integrate(sp.exp(-x)*R, (x, 0, sp.oo)) == 0,
                'Waiting-density quadratic coefficient normalization')
        responses.append(sp.simplify(R))
    difference = sp.simplify(responses[0]-responses[1])
    expected_difference = 4*sp.exp(-x)-sp.Rational(16, 9)*sp.exp(-3*x)
    expected_difference += 2*x/3-sp.Rational(20, 9)
    require(sp.simplify(difference-expected_difference) == 0, 'Waiting coefficient difference')
    squared_integral = sp.integrate(sp.expand(sp.exp(-x)*difference**2), (x, 0, sp.oo))
    require(squared_integral == sp.Rational(8, 105), 'Exact quartic information coefficient integral')

    # Check the KL Taylor algebra before using normalization to remove
    # the unknown fourth-order coefficients of the two densities.
    epsilon = sp.symbols('epsilon')
    A, B, C, D = sp.symbols('A B C D')
    first = 1+epsilon**2*A+epsilon**4*C
    second = 1+epsilon**2*B+epsilon**4*D
    expansion = sp.series(first*sp.log(first/second), epsilon, 0, 6).removeO().expand()
    equal(expansion.coeff(epsilon, 2), A-B, 'KL quadratic algebra')
    equal(expansion.coeff(epsilon, 4), C-D+(A-B)**2/2, 'KL quartic algebra')
    rate_coefficient = squared_integral/4
    require(rate_coefficient == sp.Rational(2, 105), 'Renewal entropy-rate coefficient')

    # The censored KL identity follows by differentiating its density
    # integral plus terminal survival atom, using S_i'=-f_i.
    f1, f2, S1, S2 = sp.symbols('f1 f2 S1 S2', positive=True)
    derivative = f1*sp.log(f1/f2)-f1*sp.log(S1/S2)-f1+S1*f2/S2
    hazard_integrand = S1*((f1/S1)*sp.log((f1/S1)/(f2/S2))-f1/S1+f2/S2)
    require(sp.expand_log(derivative-hazard_integrand, force=True).expand() == 0,
            'Censored KL derivative equals survival-weighted hazard divergence')
    return {
        'normalization': 'k=1; q=delta sqrt(W), hidden rates lambda=k and 3k',
        'complete_wait_laplace_exact': str(density_laplace),
        'full_wait_mass_exact': '1', 'full_wait_mean_exact': '1/k',
        'residual_density_equals_k_times_complete_survival': True,
        'hyperbolic_density_transform_identity': True,
        'quadratic_coefficient_difference': str(difference),
        'squared_difference_weighted_integral_exact': str(squared_integral),
        'waiting_KL_q4_coefficient_exact': str(squared_integral/2),
        'renewal_cycle_rate': 'k/2',
        'entropy_rate_q4_coefficient_divided_by_k_exact': str(rate_coefficient),
        'KL_series_algebra_checked_through_order': 4,
        'censored_KL_hazard_identity_symbolic': True,
        'scope': 'Checks the analytic quartic coefficient and exact identities; does not prove asymptotic remainder bounds or statistical sample complexity.',
    }


def finite_perturbation_checks() -> dict:
    with mp.workdps(90):
        errors = []
        minimum = mp.inf
        count = 0
        for lam in (mp.mpf(1), mp.mpf(3)):
            for q in (mp.mpf(1)/8, mp.mpf(1)/4):
                a = mp.matrix([1+q, 1-q])
                entry = mp.matrix([[a[0]/2, a[1]/2]])
                killed = mp.matrix([[-lam/2-a[0], lam/2], [lam/2, -lam/2-a[1]]])
                omega = mp.sqrt((lam/2)**2+q*q)
                for t in (mp.mpf(1)/4, mp.mpf(1), mp.mpf(3)):
                    direct = (entry*mp.expm(killed*t)*a)[0]
                    explicit = mp.exp(-(1+lam/2)*t)*(
                        (1+q*q)*mp.cosh(omega*t)
                        +(lam*(1-q*q)/2-2*q*q)*mp.sinh(omega*t)/omega)
                    errors.append(abs(direct-explicit))
                    minimum = min(minimum, direct)
                    count += 1
        require(max(errors) < mp.mpf('1e-85'), 'Finite-perturbation density agrees with matrix exponential')
        require(minimum > 0, 'Selected full B densities strictly positive')
        return {
            'normalization': 'k=W=1', 'decimal_precision': 90,
            'hidden_decay_rates': [1, 3], 'q_values': ['1/8', '1/4'],
            'time_values': ['1/4', '1', '3'], 'density_cases': count,
            'largest_killed_matrix_dimension': 2,
            'maximum_matrix_exponential_formula_error': mp.nstr(max(errors), 45),
            'minimum_selected_density': mp.nstr(minimum, 45),
            'scope': 'Deterministic pointwise agreement of two exact representations; no tail, KL, or statistical claim follows from these samples.',
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/path_information.json'))
    args = parser.parse_args()
    report = {
        'status': 'PASS',
        'scope': 'Exact symbolic killed-generator, visible-path score, and waiting-time information identities, plus small deterministic matrix-exponential checks.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
        'killed_resolvent_coefficients': killed_resolvent_checks(),
        'active_visible_path': active_event_checks(),
        'two_snapshot_information': two_snapshot_checks(),
        'near_lumpability_waiting_and_information': exact_waiting_and_kl_checks(),
        'finite_perturbation_density': finite_perturbation_checks(),
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
