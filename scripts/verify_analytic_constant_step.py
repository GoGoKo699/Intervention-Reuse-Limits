#!/usr/bin/env python3
"""Focused exact checks of analytic common constant-step compression.

Symbolic both-core calculations certify stationarity, the commuting blend,
and the first two arbitrary-protocol response equations. Exact small
two-node examples and regularized Gaussian moments check the remaining
construction. No simulation or numerical rank test is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp

import verify_constant_step_compression as constant


require = constant.require
zero = constant.zero


def symbolic_both_core_check():
    m, d, x = sp.symbols('m d x', real=True)
    tau, eta = sp.symbols('tau eta', positive=True)
    epsilon, rate = sp.Rational(1, 2), sp.Integer(3)
    nu = rate-epsilon
    pminus, pplus = 1-(d+m)/2, 1-(d-m)/2
    core = lambda p: sp.Matrix([[-nu*(1-p), nu*(1-p)], [nu*p, -nu*p]])
    base = sp.diag(core(pminus), core(pplus))
    pi = sp.Matrix([[pminus/2, (1-pminus)/2, pplus/2, (1-pplus)/2]])
    rho, S = sp.Matrix([[sp.Rational(1, 2), 0, sp.Rational(1, 2), 0]]), sp.Matrix([-1, 1, 1, -1])
    I, one = sp.eye(4), sp.ones(4, 1)
    projection = one*pi
    raw = base+epsilon*(projection-I)
    reset = 2*(projection-I)
    final = x*raw+(1-x)*reset
    require(sum(pi) == 1 and sp.expand((pi*S)[0]-m) == 0,
            'Both-core stationary readout mean is exactly m')
    require(zero(pi*base) and zero(pi*raw) and zero(pi*final), 'Common stationary law through the blend')
    require(zero(sp.diag(*pi)*final-final.T*sp.diag(*pi)), 'Symbolic reversibility of the blended generator')
    require(zero(raw*reset-reset*raw), 'Raw generator commutes with its stationary reset')
    visible_rate = x*rate+(1-x)*2
    residual_rate = x*epsilon+(1-x)*2
    annihilator = final*(final+visible_rate*I)*(final+residual_rate*I)
    require(zero(annihilator), 'Symbolic affine transformation of the raw relaxation spectrum')
    for j in range(1, 4):
        require(sp.expand((rho*final**j*S)[0]+m*(-visible_rate)**j) == 0,
                'Exact half-root mean coefficients after the commuting blend')

    # Analytic field substitution has m=tanh(h)=h+O(h^3),
    # d=sqrt(m^2+tau^2)=tau+h^2/(2tau)+O(h^4), and
    # chi=h^2/(h^2+eta^2)=h^2/eta^2+O(h^4).
    at_zero = {m: 0, d: tau}
    sigma = pi.subs(at_zero)
    pi1 = pi.diff(m)
    pi2 = pi.diff(d)/(2*tau)
    Q0 = reset.subs(at_zero)
    D0 = (raw-reset).subs(at_zero)
    Q1 = 2*one*pi1
    Q2 = 2*one*pi2+D0/eta**2
    require(zero(sigma*D0), 'Stationary preparation annihilates the order-two splice forcing')
    require(zero(sigma*Q1-2*pi1) and zero(sigma*Q2-2*pi2),
            'First two generator forcing rows equal the reset-family rows')
    require((pi1*S)[0] == 1 and (pi2*S)[0] == 0 and zero(Q0*S+2*S),
            'Universal linear forcing and zero quadratic mean forcing')
    a, b, c = sp.symbols('a b c')
    mass_zero = sp.Matrix([[a, b, c, -a-b-c]])
    require(zero(mass_zero*Q1), 'Every mass-zero first-order state correction annihilates Q1')
    exact_l1 = sp.simplify(sum(abs(v) for v in sigma-rho))
    require(exact_l1 == tau, 'Fixed stationary preparation is exactly tau from half roots in row l1')
    lump = sp.Matrix([[int(sign == value) for value in (-1, 1)] for sign in S])
    telegraph = sp.Matrix([[-1, 1], [1, -1]])
    require(zero(Q0*lump-lump*telegraph) and zero(sigma*Q0),
            'Analytic blend gives exact stationary passive telegraph law at zero')
    return {'symbolic_generator_dimension': 4,
            'analytic_field_substitution': 'm=tanh(h), d=sqrt(m^2+tau^2), chi=h^2/(h^2+eta^2)',
            'shared_stationarity_reversibility_and_commutation': True,
            'raw_active_rate': str(rate), 'raw_reset_rate': str(epsilon),
            'blended_visible_rate': str(visible_rate), 'blended_residual_rate': str(residual_rate),
            'fixed_preparation_l1_distance_to_half_roots': 'tau',
            'exact_passive_lumpability_and_hidden_stationarity': True,
            'arbitrary_protocol_response_identities': {
                'sigma_D0_zero': True, 'mass_zero_p1_Q1_zero': True,
                'pi1_S': '1', 'pi2_S': '0',
                'linear_mean_equation': "m1'=-2m1+2u(t)",
                'quadratic_mean_equation': "m2'=-2m2, m2(0)=0",
                'scope': 'Exact coefficient equations for every bounded weak protocol, not a constant-step-only derivative check.'}}


def exact_two_node_case(sign):
    tau, m = sp.Rational(1, 12), sign*sp.Rational(1, 9)
    d = sp.sqrt(m*m+tau*tau)
    require(d == sp.Rational(5, 36), 'Rational nonzero-field calibration')
    rates, weights = [sp.Integer(2), sp.Integer(3)], [sp.Rational(1, 4), sp.Rational(3, 4)]
    epsilon, chi = sp.Rational(1, 2), sp.Rational(2, 3)
    shifted = [rate-epsilon for rate in rates]
    pminus, pplus = 1-(d+m)/2, 1-(d-m)/2
    left, left_pi = constant.birth_death_from_root_measure(shifted, weights, pminus)
    right, right_pi = constant.birth_death_from_root_measure(shifted, weights, pplus)
    _, zero_pi = constant.birth_death_from_root_measure(shifted, weights, 1-tau/2)
    pi = sp.Matrix.hstack(left_pi/2, right_pi/2)
    sigma = sp.Matrix.hstack(zero_pi/2, zero_pi/2)
    base = sp.diag(left, right)
    S = sp.Matrix([-1, 1, 1, 1, -1, -1])
    rho = sp.Matrix([[sp.Rational(1, 2), 0, 0, sp.Rational(1, 2), 0, 0]])
    projection = sp.ones(6, 1)*pi
    raw = base+epsilon*(projection-sp.eye(6))
    reset = 2*(projection-sp.eye(6))
    final = chi*raw+(1-chi)*reset
    require(all(v > 0 for v in pi) and all(v > 0 for v in sigma), 'Both stationary laws have full support')
    require((pi*S)[0] == m and (sigma*S)[0] == 0, 'Exact stationary curve and fixed sign-balanced preparation')
    require(sum(abs(v) for v in sigma-rho) == tau, 'Exact full-support preparation budget in the two-node case')
    require(zero(pi*final) and sp.diag(*pi)*final == final.T*sp.diag(*pi),
            'Exact two-core stationarity and detailed balance')
    require(all(final[i, j] > 0 for i in range(6) for j in range(6) if i != j),
            'Analytic blend retains strict positivity of every off-diagonal rate')
    blended = [chi*rate+(1-chi)*2 for rate in rates]
    residual = chi*epsilon+(1-chi)*2
    spectral = constant.projectors(final, [sp.Integer(0), residual]+blended)
    coefficients = [sp.simplify((rho*P*S)[0]) for P in spectral]
    require(coefficients == [m, 0]+[-m*w for w in weights],
            'Exact two-node half-root mixture under the blend')
    return {'sign': sign, 'm_exact': str(m), 'tau': str(tau), 'chi': str(chi),
            'full_generator_dimension': 6, 'both_active_root_masses': [str(pminus), str(pplus)],
            'fixed_stationary_zero_field_preparation': [str(v) for v in sigma],
            'nonzero_full_rates': [str(residual)]+[str(rate) for rate in blended],
            'exact_half_root_mean_coefficients': [str(v) for v in coefficients],
            'stationarity_irreducibility_reversibility': True,
            'preparation_mean_error_bound_all_times': str(tau)}


def regularized_moment_check():
    m, xi = sp.symbols('m xi', real=True)
    # A two-atom analytic family collapses to one atom at m=0. The fixed
    # uniform reference prevents Gaussian moment rank loss there.
    reference = lambda j: sp.Rational(4**(j+1)-1, 3*(j+1))
    moments = [(1-xi)*((1-m*m)*2**j+m*m*3**j)+xi*reference(j) for j in range(4)]
    H = sp.Matrix([[moments[0], moments[1]], [moments[1], moments[2]]])
    uniform_gram = sp.Matrix([[reference(0), reference(1)], [reference(1), reference(2)]])
    v2, v3 = sp.Matrix([1, 2]), sp.Matrix([1, 3])
    positive_decomposition = (1-xi)*((1-m*m)*v2*v2.T+m*m*v3*v3.T)+xi*uniform_gram
    require(zero(H-positive_decomposition), 'Exact positive moment-Gram decomposition')
    require(uniform_gram[0, 0] > 0 and uniform_gram.det() > 0,
            'The uniform reference has a strictly positive moment Gram matrix')
    require(sp.simplify(H.det().subs({m: 0, xi: 0})) == 0,
            'The unregularized example loses Gaussian moment rank at zero field')
    chosen = sp.Rational(1, 8)
    mu = [sp.expand(value.subs(xi, chosen)) for value in moments]
    beta = sp.simplify(mu[2]-mu[1]**2)
    a0 = mu[1]
    a1 = sp.simplify((mu[3]-2*a0*mu[2]+a0*a0*mu[1])/beta)
    J = sp.Matrix([[a0, sp.sqrt(beta)], [sp.sqrt(beta), a1]])
    for value in (sp.Rational(-1, 3), sp.Integer(0), sp.Rational(1, 3)):
        require(beta.subs(m, value) > 0, 'Regularized Jacobi off-diagonal remains strictly positive')
        require(all(sp.diff(entry, m).subs(m, value).is_finite for entry in J),
                'Analytic Jacobi coefficient derivatives remain finite through the old rank collapse')
        for degree in range(4):
            require(sp.simplify((J**degree)[0, 0].subs(m, value)-mu[degree].subs(m, value)) == 0,
                    'Regularized Gaussian Jacobi moments are exact through degree three')
    require(sp.simplify(beta.subs(m, 0)) > 0, 'Reference regularization repairs the zero-field rank collapse')
    return {'reference_interval': ['1', '4'], 'reference_weight': str(chosen),
            'uniform_reference_Gram_exact': str(uniform_gram),
            'uniform_reference_Gram_determinant': str(uniform_gram.det()),
            'analytic_moment_family': '(1-xi)[(1-m^2)delta_2+m^2 delta_3]+xi Uniform[1,4], |m|<1, 0<xi<1',
            'positive_Gram_decomposition_verified': True,
            'zero_field_regularized_offdiagonal_squared': str(sp.simplify(beta.subs(m, 0))),
            'rank_collapse_without_reference': True, 'analytic_derivatives_checked': ['-1/3', '0', '1/3'],
            'Gaussian_moment_degrees_checked': [0, 1, 2, 3],
            'scope': 'Exact small moment/Jacobi example; arbitrary fixed rank follows from the positive reference moment-Gram argument in the proof.'}


def error_budgets():
    alpha, upper, mmax = sp.Integer(1), sp.Integer(4), sp.Rational(1, 2)
    q = 1-alpha/upper
    records = []
    for delta in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        xi, tau, eta = delta/4, (1-mmax)*delta/4, alpha*delta/(2*upper)
        r = 1
        while 2*q**(2*r) > delta/4:
            r += 1
        require(mmax+tau/2 < 1, 'Both analytic active-core root masses stay strictly positive')
        splice = upper*eta/(2*alpha)
        total = xi+2*q**(2*r)+tau+splice
        require(splice == delta/4 and total <= delta,
                'Reference, quadrature, preparation, and analytic splice budgets sum to tolerance')
        records.append({'tolerance': str(delta), 'reference_weight_xi': str(xi),
                        'preparation_distance_tau': str(tau), 'splice_scale_eta': str(eta),
                        'quadrature_atoms': r, 'state_count': 2*r+2,
                        'combined_error_bound_exact': str(total)})
    h, eta = sp.symbols('h eta', real=True, positive=True)
    # For h>=0, h*eta^2/(h^2+eta^2)<=eta/2 is equivalent
    # to the explicitly nonnegative square (h-eta)^2>=0.
    require(sp.factor(eta*(h*h+eta*eta)-2*h*eta*eta) == eta*(h-eta)**2,
            'Exact analytic-splice uniform field inequality')
    return {'calibration_interval': ['1', '4'], 'maximum_abs_tanh_H': str(mmax),
            'splice_inequality': '|h| eta^2/(h^2+eta^2) <= eta/2',
            'records': records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/analytic_constant_step.json'))
    args = parser.parse_args()
    point_cases = [exact_two_node_case(sign) for sign in (1, -1)]
    require(point_cases[0]['fixed_stationary_zero_field_preparation'] == point_cases[1]['fixed_stationary_zero_field_preparation'],
            'Positive and negative fields use the same full-support preparation')
    report = {'status': 'PASS',
              'scope': 'Exact analytic both-core/reset identities, passive and first-two-response calibration, positive Gaussian regularization, and rational error budgets.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'symbolic_both_core_and_weak_response': symbolic_both_core_check(),
              'exact_two_node_both_core_cases': point_cases,
              'analytic_regularized_quadrature': regularized_moment_check(),
              'rational_uniform_error_budgets': error_budgets(),
              'largest_generator_dimension': 6,
              'no_simulation_or_numerical_rank_tests': True,
              'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in (Path(__file__), Path(constant.__file__))}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, default=str)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2, default=str))


if __name__ == '__main__':
    main()
