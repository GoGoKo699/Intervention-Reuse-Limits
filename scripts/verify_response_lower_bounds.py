#!/usr/bin/env python3
"""Deterministic checks for finite-error response lower bounds.

Exact algebra and small high-precision matrices check the identities used
in the proofs. Computed eigenvalue witnesses are not minimax optimizers or
interval-certified eigenvalue bounds. No random sampling or network calls.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp


FILTER = (sp.Rational(-1, 16), sp.Rational(9, 16), sp.Rational(-3, 2), sp.Integer(1))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def number(value: sp.Expr | int) -> mp.mpf:
    return mp.mpf(str(sp.N(value, mp.mp.dps + 10)))


def matrix(value: sp.Matrix) -> mp.matrix:
    return mp.matrix([[number(value[i, j]) for j in range(value.cols)]
                      for i in range(value.rows)])


def digits(value: mp.mpf, count: int = 45) -> str:
    return mp.nstr(value, count)


def maxabs(value: mp.matrix) -> mp.mpf:
    return max(abs(x) for x in value)


def symbolic_two_state() -> dict:
    epsilon, u, k, t = sp.symbols('epsilon u k t', real=True)
    m1, m2, m3, r1, alpha, beta = sp.symbols('m1 m2 m3 r1 alpha beta', real=True)
    field = epsilon * u
    mean = epsilon*m1 + epsilon**2*m2 + epsilon**3*m3
    speed = 1 + r1*field + alpha*field**2 + beta*field**3
    rhs = sp.series(2*k*speed*(sp.sinh(field)-mean*sp.cosh(field)), epsilon, 0, 4).removeO()
    expected = (
        2*k*(u-m1),
        -2*k*m2 + 2*k*r1*u*(u-m1),
        -2*k*m3 - 2*k*r1*u*m2 + 2*k*alpha*u**2*(u-m1)
        + 2*k*(u**3/sp.Integer(6)-m1*u**2/sp.Integer(2)),
    )
    for order, wanted in enumerate(expected, 1):
        require(sp.expand(rhs.coeff(epsilon, order)-wanted) == 0,
                f'Two-state symbolic coefficient {order}')

    # Independently expand the exact finite-field step solution.
    h = sp.symbols('h', real=True)
    exact_mean = sp.tanh(h)*(1-sp.exp(-2*k*t*sp.exp(alpha*h*h)*sp.cosh(h)))
    exact_cubic = sp.series(exact_mean, h, 0, 4).removeO().expand().coeff(h, 3)
    reference = -(1-sp.exp(-2*k*t))/3 + k*t*sp.exp(-2*k*t)
    require(sp.simplify(exact_cubic-reference-2*k*alpha*t*sp.exp(-2*k*t)) == 0,
            'Exact analytic two-state step solution')

    tau1, tau2 = sp.Rational(1, 4), sp.Rational(3, 2)
    f1, f2 = tau1*sp.exp(-2*tau1), tau2*sp.exp(-2*tau2)
    twice_alpha = (f1*(1-tau1)+f2*(1-tau2))/(f1+f2)
    error1 = f1*(1-tau1-twice_alpha)
    error2 = f2*(1-tau2-twice_alpha)
    bound = sp.Rational(15, 8)/(sp.exp(3)+6*sp.exp(sp.Rational(1, 2)))
    require(sp.simplify(error1-bound) == 0 and sp.simplify(error2+bound) == 0,
            'Exact two-sample equal and opposite errors')
    arbitrary_alpha = sp.symbols('arbitrary_alpha', real=True)
    e1 = f1*(1-tau1-2*arbitrary_alpha)
    e2 = f2*(1-tau2-2*arbitrary_alpha)
    require(sp.simplify(f2*e1-f1*e2-f1*f2*(tau2-tau1)) == 0,
            'All-alpha dual witness identity')
    return {
        'normalization': 'W=U=k=1; general bound scales as W U^3 and times as 1/k',
        'symbolic_coefficient_equations': 3,
        'exact_finite_field_step_expansion': True,
        'sampling_tau': ['1/4', '3/2'],
        'normalized_two_sample_minimax_exact': str(bound),
        'normalized_two_sample_minimax_decimal': str(sp.N(bound, 55)),
        'optimal_alpha_decimal': str(sp.N(twice_alpha/2, 55)),
        'all_alpha_dual_identity': True,
        'scope': 'Exact minimax for the two specified samples, not the all-protocol optimum.',
    }


def rational_vandermonde(D: int) -> tuple[list[sp.Rational], dict]:
    r = 3*D-4
    n = r-1
    nodes = [sp.Rational(1, 16)+sp.Rational(j, 16*n) for j in range(r)]
    vandermonde = sp.Matrix([[x**i for x in nodes] for i in range(r)])
    inverse = vandermonde.inv()
    require(vandermonde*inverse == sp.eye(r), 'Exact rational Vandermonde inverse')
    rows = [sum(abs(inverse[j, i]) for i in range(r)) for j in range(r)]
    spacing = sp.Rational(1, 16*n)
    for j in range(r):
        product_row = sp.prod(1+nodes[m] for m in range(r) if m != j) / (
            spacing**n*math.factorial(j)*math.factorial(n-j))
        require(rows[j] == product_row, 'Exact Lagrange coefficient l1 norm')
        endpoint_bound = sp.Rational(9, 8)**n / (
            spacing**n*math.factorial(j)*math.factorial(n-j))
        require(rows[j] <= endpoint_bound, 'Exact endpoint product bound')
    factorial_bound = sp.Rational(36**n*n**n, math.factorial(n))
    require(max(rows) <= factorial_bound, 'Exact combinatorial row bound')
    # The finite positive series is strictly below e, giving a rational
    # certificate for each tested comparison with (36 e)^(r-1).
    e_lower = sum(sp.Rational(1, math.factorial(j)) for j in range(19))
    require(max(rows) < (36*e_lower)**n, 'Rational certificate below exponential bound')
    return nodes, {
        'exact_inverse_checked': True,
        'exact_lagrange_row_identities': r,
        'maximum_inverse_row_l1_rational': str(max(rows)),
        'combinatorial_row_bound_rational': str(factorial_bound),
        'e_lower_series_terms': 19,
        'rational_certificate_below_36e_power': True,
    }


def target_step(tau: mp.mpf, rates: list[mp.mpf]) -> mp.mpf:
    r = len(rates)
    e2 = mp.exp(-2*tau)
    baseline = -(1-e2)/3 + tau*e2
    integral = mp.fsum((mp.expm1((1-rate)*tau)-(1-rate)*tau)/(1-rate)**2
                       for rate in rates)/r
    return baseline + e2*(tau-2*integral)


def target_hankel(D: int, precision: int) -> dict:
    with mp.workdps(precision):
        nodes_exact, exact_checks = rational_vandermonde(D)
        nodes = [number(x) for x in nodes_exact]
        r = len(nodes)
        rates = [-mp.log(x, 2)-1 for x in nodes]
        weights = [2*(1-x)*(x-mp.mpf(1)/4)**2/(r*(1-rate)**2)
                   for x, rate in zip(nodes, rates)]
        d_floor = mp.mpf(7)/(1024*r)
        require(all(w >= d_floor for w in weights), 'Positive filtered weight lower bound')
        dt = mp.log(2)
        raw = [target_step(i*dt, rates) for i in range(2*r+2)]
        filtered = [mp.fsum(number(FILTER[j])*raw[i+j] for j in range(4))
                    for i in range(2*r-1)]
        moments = [mp.fsum(w*x**i for w, x in zip(weights, nodes))
                   for i in range(2*r-1)]
        residual = max(abs(a-b) for a, b in zip(filtered, moments))
        require(residual < mp.mpf(10)**(-precision+12), 'Target filter-to-positive-moments identity')
        H = mp.matrix([[moments[i+j] for j in range(r)] for i in range(r)])
        V = mp.matrix([[x**i for x in nodes] for i in range(r)])
        decomposition_error = maxabs(H - V*mp.diag(weights)*V.T)
        eigenvalues = mp.eigsy(H, eigvals_only=True)
        lambda_min = eigenvalues[0]
        require(lambda_min > 0, 'High precision target Hankel eigenvalue positive')
        conservative = mp.mpf(7)/(3200*r**3*(36*mp.e)**(2*r-2))
        eigen_witness = 8*lambda_min/(25*r)
        require(eigen_witness >= conservative, 'Computed witness above proved conservative bound')
        return {
            'state_budget_D': D, 'target_modes_r': r,
            'target_total_states_by_jacobi': r+2,
            'hankel_dimension': r,
            'maximum_raw_sample_index': 2*r+1,
            'sample_time_spacing_k_t': 'log(2)',
            'normalized_rates_interval': [2, 3],
            'working_decimal_digits': precision,
            'minimum_filtered_weight': digits(min(weights)),
            'proved_filtered_weight_floor': digits(d_floor),
            'filter_identity_max_abs_error': digits(residual),
            'vandermonde_factorization_max_abs_error': digits(decomposition_error),
            'computed_hankel_smallest_eigenvalue': digits(lambda_min, 70),
            '_eigenvalue_validation_digits': digits(lambda_min, precision),
            'computed_response_witness_8_lambda_min_over_25r': digits(eigen_witness, 70),
            'proved_conservative_response_lower_bound': digits(conservative, 70),
            'exact_rational_vandermonde': exact_checks,
        }


def target_checks() -> dict:
    results = []
    for D in (2, 3, 4):
        low = target_hankel(D, 100)
        high = target_hankel(D, 150)
        with mp.workdps(150):
            relative = abs(mp.mpf(low.pop('_eigenvalue_validation_digits'))/
                           mp.mpf(high.pop('_eigenvalue_validation_digits'))-1)
            require(relative < mp.mpf('1e-55'), 'Eigenvalue precision-doubling consistency')
        high['eigenvalue_relative_change_100_to_150_digits'] = digits(relative)
        results.append(high)
    return {
        'normalization': 'W=U=k=1; bounds and filtered weights scale by W U^3',
        'filter_coefficients_lag_0_to_3': [str(x) for x in FILTER],
        'filter_l1_norm_exact': str(sum(abs(x) for x in FILTER)),
        'cases': results,
        'eigenvalue_scope': 'High-precision numerical consistency, not interval-certified minima.',
        'lower_bound_scope': 'The conservative analytic bound is proved in the note; sample eigenvalues do not establish minimax optimality.',
    }


def surrogate_cases() -> list[dict]:
    R = sp.Rational
    one = sp.ones(3, 1)
    a, eta = R(3, 5), R(1, 25)
    u, v = sp.Matrix([1, -1, 0]), sp.Matrix([1, 1, -2])
    defective = -a*(sp.eye(3)-one*one.T/3) + eta*u*v.T
    require((u*v.T)**2 == sp.zeros(3), 'Defective perturbation is nilpotent')
    require((u*v.T).rank() == 1, 'Defective perturbation is nonzero rank one')
    return [
        {'name': 'two_state_arbitrary_alpha', 'mu': sp.Matrix([1]),
         'K': sp.zeros(1), 'g': sp.Matrix([0]), 'alpha': R(2, 7)},
        {'name': 'three_state_reversible', 'mu': sp.Matrix([R(1, 2), R(1, 2)]),
         'K': sp.Matrix([[-R(2, 5), R(2, 5)], [R(2, 5), -R(2, 5)]]),
         'g': sp.Matrix([R(1, 2), -R(1, 2)]), 'alpha': sp.Integer(0)},
        {'name': 'four_state_nonreversible_defective', 'mu': sp.ones(3, 1)/3,
         'K': defective, 'g': sp.Matrix([R(1, 5), 0, -R(1, 5)]),
         'alpha': sp.Integer(0)},
    ]


def coefficients(case: dict) -> list[sp.Matrix]:
    h = sp.symbols('h')
    mu, K, g, alpha = (case[x] for x in ('mu', 'K', 'g', 'alpha'))
    D = len(mu)+1
    Q = sp.zeros(D)
    for i in range(D-1):
        Q[0, i+1] = mu[i]*sp.exp((1+g[i])*h+alpha*h*h)
        Q[i+1, 0] = sp.exp((g[i]-1)*h+alpha*h*h)
        for j in range(D-1):
            if i != j:
                Q[i+1, j+1] = K[i, j]
    for i in range(D):
        Q[i, i] = -sum(Q[i, j] for j in range(D) if j != i)
    return [Q.diff(h, n).subs(h, 0).T/sp.factorial(n) for n in range(4)]


def generator_numeric(case: dict, h: mp.mpc | mp.mpf) -> mp.matrix:
    mu, K, g, alpha = (case[x] for x in ('mu', 'K', 'g', 'alpha'))
    D = len(mu)+1
    Q = mp.matrix(D)
    for i in range(D-1):
        Q[0, i+1] = number(mu[i])*mp.exp((1+number(g[i]))*h+number(alpha)*h*h)
        Q[i+1, 0] = mp.exp((number(g[i])-1)*h+number(alpha)*h*h)
        for j in range(D-1):
            if i != j:
                Q[i+1, j+1] = number(K[i, j])
    for i in range(D):
        Q[i, i] = -mp.fsum(Q[i, j] for j in range(D) if j != i)
    return Q.T


def hierarchy(case: dict) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    A = coefficients(case)
    D = A[0].rows
    n = D-1
    p0 = sp.Matrix([sp.Rational(1, 2)]+[x/2 for x in case['mu']])
    readout = sp.Matrix([-1]+[1]*n)
    require(A[0]*p0 == sp.zeros(D, 1), 'Exact stationary preparation')
    require(A[0].T*readout == -2*readout, 'Exact passive readout eigenmode')
    require(all(sum(A[j][:, i]) == 0 for j in range(4) for i in range(D)),
            'Every generator coefficient conserves total mass')
    T = sp.eye(D)[:, :n]
    for i in range(n):
        T[D-1, i] = -1
    L = sp.eye(D)[:n, :]
    reduced = sp.zeros(1+3*n)
    full = sp.zeros(4*D)
    for row in range(4):
        for col in range(row+1):
            full[row*D:(row+1)*D, col*D:(col+1)*D] = A[row-col]
    for order in range(1, 4):
        start = 1+(order-1)*n
        reduced[start:start+n, 0] = L*A[order]*p0
        for earlier in range(1, order+1):
            col = 1+(earlier-1)*n
            reduced[start:start+n, col:col+n] = L*A[order-earlier]*T
    # Exact intertwining checks the complete state representation, not just
    # the observed scalar trajectory used by the finite sample checks.
    embed = sp.zeros(4*D, 1+3*n)
    embed[:D, 0] = p0
    for order in range(1, 4):
        embed[order*D:(order+1)*D, 1+(order-1)*n:1+order*n] = T
    require(full*embed == embed*reduced, 'Exact full/reduced hierarchy intertwining')
    return full, reduced, embed, readout, L*A[0]*T


def recurrence_residual(samples: list[mp.mpf], coefficients_: list[mp.mpf]) -> mp.mpf:
    degree = len(coefficients_)-1
    return max(abs(mp.fsum(c*samples[start+j] for j, c in enumerate(coefficients_)))
               for start in range(len(samples)-degree))


def hierarchy_checks() -> dict:
    results = []
    with mp.workdps(100):
        dt = mp.log(2)
        for case in surrogate_cases():
            full, reduced, embed, observable, A = hierarchy(case)
            D = A.rows+1
            eigenvalues = A.eigenvals()
            require(-2 in eigenvalues, 'Passive eigenvalue appears on zero-mass subspace')
            z = sp.symbols('z')
            characteristic = sp.Poly((z-1)*sp.prod((z-2**eigenvalue)**(3*multiplicity)
                                      for eigenvalue, multiplicity in eigenvalues.items()), z)
            filter_poly = sp.Poly(sum(FILTER[j]*z**j for j in range(4)), z)
            quotient, remainder = sp.div(characteristic, filter_poly)
            require(sp.simplify(remainder.as_expr()) == 0, 'Exact sampled characteristic divisibility')
            require(quotient.degree() == 3*D-5, 'Filtered recurrence degree')
            full_mp, reduced_mp, embed_mp = matrix(full), matrix(reduced), matrix(embed)
            full_step = mp.expm(dt*full_mp)
            reduced_step = mp.expm(dt*reduced_mp)
            reduced_state = mp.matrix(reduced.rows, 1)
            reduced_state[0] = 1
            full_state = embed_mp*reduced_state
            obs = matrix(observable)
            max_hierarchy_error = mp.mpf(0)
            max_linear_error = mp.mpf(0)
            max_quadratic_error = mp.mpf(0)
            raw = []
            for i in range(2*(3*D-5)+8):
                max_hierarchy_error = max(max_hierarchy_error,
                                          maxabs(full_state-embed_mp*reduced_state))
                means = [(obs.T*full_state[j*D:(j+1)*D, :])[0] for j in range(4)]
                max_linear_error = max(max_linear_error, abs(means[1]-(1-mp.mpf(4)**(-i))))
                max_quadratic_error = max(max_quadratic_error, abs(means[2]))
                raw.append(means[3])
                full_state = full_step*full_state
                reduced_state = reduced_step*reduced_state
            filtered = [mp.fsum(number(FILTER[j])*raw[i+j] for j in range(4))
                        for i in range(len(raw)-3)]
            raw_coeffs = [number(characteristic.nth(j)) for j in range(characteristic.degree()+1)]
            filt_coeffs = [number(quotient.nth(j)) for j in range(quotient.degree()+1)]
            raw_residual = recurrence_residual(raw, raw_coeffs)
            filt_residual = recurrence_residual(filtered, filt_coeffs)
            require(max(max_hierarchy_error, max_linear_error, max_quadratic_error,
                        raw_residual, filt_residual) < mp.mpf('1e-85'),
                    'High-precision hierarchy and recurrence consistency')
            defect = []
            jordan_observable_coupling = None
            for eigenvalue, multiplicity in eigenvalues.items():
                nullity = A.rows-(A-eigenvalue*sp.eye(A.rows)).rank()
                if multiplicity > nullity:
                    defect.append({'eigenvalue': str(eigenvalue),
                                   'algebraic_multiplicity': multiplicity,
                                   'geometric_multiplicity': nullity})
            if 'defective' in case['name']:
                require(len(defect) == 1 and defect[0]['algebraic_multiplicity'] == 2,
                        'Nonreversible defective test actually contains a Jordan block')
                require(case['K'] != case['K'].T, 'Defective uniform chain is nonreversible')
                require(all(case['K'][i, j] > 0 for i in range(3) for j in range(3) if i != j),
                        'Defective internal chain is irreducible')
                nilpotent = case['K'] + sp.Rational(3, 5)*(sp.eye(3)-sp.ones(3)/3)
                jordan_observable_coupling = (case['g'].T*nilpotent*case['g'])[0]/3
                require(jordan_observable_coupling != 0,
                        'Sensitivity actually couples to the nontrivial Jordan part')
            results.append({
                'case': case['name'], 'states_D': D,
                'full_coefficient_hierarchy_dimension': full.rows,
                'stationary_reduced_hierarchy_dimension': reduced.rows,
                'exact_hierarchy_intertwining': True,
                'zero_mass_generator_eigenvalues': {str(x): m for x, m in eigenvalues.items()},
                'defective_eigenvalues': defect,
                'stationary_jordan_observable_coupling_exact': (
                    str(jordan_observable_coupling) if jordan_observable_coupling is not None else None),
                'unfiltered_recurrence_degree': characteristic.degree(),
                'filtered_recurrence_degree': quotient.degree(),
                'exact_filter_divisibility': True,
                'raw_samples_checked': len(raw),
                'max_full_reduced_state_error': digits(max_hierarchy_error),
                'max_linear_reference_error': digits(max_linear_error),
                'max_quadratic_mean_abs': digits(max_quadratic_error),
                'max_raw_recurrence_error': digits(raw_residual),
                'max_filtered_recurrence_error': digits(filt_residual),
            })
    return {'working_decimal_digits': 100, 'cases': results,
            'largest_matrix_dimension': max(row['full_coefficient_hierarchy_dimension'] for row in results),
            'scope': 'Exact intertwining/divisibility plus high-precision trajectory checks; not a numerical rank test.'}


def analytic_master_coefficient_check() -> dict:
    case = surrogate_cases()[-1]
    full, reduced, embed, observable, _ = hierarchy(case)
    D = observable.rows
    with mp.workdps(100):
        tau = mp.mpf(7)/10
        p0 = matrix(embed[:D, 0])
        obs = matrix(observable)
        initial = mp.matrix(full.rows, 1)
        initial[:D, 0] = p0
        exact_hierarchy = mp.expm(tau*matrix(full))*initial
        cubic = (obs.T*exact_hierarchy[3*D:4*D, :])[0]
        records = []
        for nodes, radius in ((24, mp.mpf('0.005')), (32, mp.mpf('0.01'))):
            terms = []
            for j in range(nodes):
                angle = 2*mp.pi*j/nodes
                h = radius*mp.exp(1j*angle)
                mean = (obs.T*mp.expm(tau*generator_numeric(case, h))*p0)[0]
                terms.append(mean*mp.exp(-3j*angle))
            cauchy = mp.fsum(terms)/(nodes*radius**3)
            error = abs(cauchy-cubic)
            require(error < mp.mpf('1e-45'), 'Independent exact-generator contour coefficient')
            records.append({'complex_contour_nodes': nodes, 'radius': digits(radius),
                            'absolute_error_against_hierarchy': digits(error)})
        stationary_errors = []
        for h in (mp.mpf('-0.2'), mp.mpf('0.1')):
            equilibrium = mp.matrix([mp.exp(-h)/(2*mp.cosh(h))] +
                                    [number(mu)*mp.exp(h)/(2*mp.cosh(h)) for mu in case['mu']])
            stationary_errors.append(maxabs(generator_numeric(case, h)*equilibrium))
        require(max(stationary_errors) < mp.mpf('1e-90'), 'Nonreversible example preserves stated equilibrium')
        return {'case': case['name'], 'time_k_t': '7/10',
                'matrix_dimension': D, 'working_decimal_digits': 100,
                'cubic_coefficient_from_hierarchy': digits(cubic),
                'contour_convergence_checks': records,
                'max_finite_field_stationarity_residual': digits(max(stationary_errors)),
                'scope': 'Converging complex-contour consistency check; no finite-field approximation bound claimed.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/response_lower_bounds.json'))
    args = parser.parse_args()
    report = {
        'status': 'PASS',
        'scope': 'Small deterministic proof-identity checks; no minimax optimization or interval certification.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'mpmath': mp.__version__},
        'two_state': symbolic_two_state(),
        'target_hankel_witnesses': target_checks(),
        'surrogate_recurrences': hierarchy_checks(),
        'independent_analytic_master_equation': analytic_master_coefficient_check(),
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
