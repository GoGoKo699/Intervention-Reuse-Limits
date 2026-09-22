#!/usr/bin/env python3
"""Exact small checks of the common reversible constant-step predictor.

This verifies positive Jacobi realization, fixed binary preparation/readout,
padding, stationary reset, exact spectral mean coefficients, and passive
lumpability. Gaussian quadrature moments and rational uniform-error budgets
are checked separately. No large simulation or numerical rank test is used.
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


def zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


def recurrence(nodes, weights, count):
    """Monic orthogonal polynomials, with exact positive norms."""
    x = sp.symbols('x')
    inner = lambda f, g: sp.simplify(sum(w*f.subs(x, v)*g.subs(x, v)
                                       for v, w in zip(nodes, weights)))
    polynomials, norms, diagonals, ratios = [sp.Integer(1)], [], [], []
    for j in range(count):
        p = polynomials[j]
        norm = inner(p, p)
        require(norm > 0, 'Positive orthogonal-polynomial norm')
        diagonal = sp.simplify(inner(x*p, p)/norm)
        ratio = sp.Integer(0) if j == 0 else sp.simplify(norm/norms[-1])
        next_p = sp.expand((x-diagonal)*p-(ratio*polynomials[j-1] if j else 0))
        norms.append(norm)
        diagonals.append(diagonal)
        ratios.append(ratio)
        polynomials.append(next_p)
    return x, polynomials, norms, diagonals, ratios


def birth_death_from_root_measure(rates, weights, root_mass):
    nodes = [sp.Integer(0)]+[-rate for rate in rates]
    masses = [root_mass]+[(1-root_mass)*weight for weight in weights]
    count = len(nodes)
    x, polynomials, norms, diagonals, ratios = recurrence(nodes, masses, count)
    values = [sp.simplify(p.subs(x, 0)) for p in polynomials]
    require(all(v > 0 for v in values[:-1]) and values[-1] == 0,
            'Positive Jacobi harmonic vector at the zero spectral endpoint')
    Q = sp.zeros(count)
    for j in range(count):
        Q[j, j] = diagonals[j]
        if j+1 < count:
            Q[j, j+1] = sp.simplify(values[j+1]/values[j])
        if j:
            Q[j, j-1] = sp.simplify(ratios[j]*values[j-1]/values[j])
    stationary = sp.Matrix([[sp.simplify(root_mass*values[j]**2/norms[j]) for j in range(count)]])
    require(sum(stationary) == 1 and stationary[0] == root_mass,
            'Root atom equals root stationary mass')
    require(zero(Q*sp.ones(count, 1)) and zero(stationary*Q), 'Birth-death generator conservation and stationarity')
    require(sp.diag(*stationary)*Q == Q.T*sp.diag(*stationary), 'Exact Jacobi detailed balance')
    require(all(Q[j, j+1] > 0 and Q[j+1, j] > 0 for j in range(count-1)),
            'Strictly positive nearest-neighbor birth-death rates')
    spectral = projectors(Q, [sp.Integer(0)]+list(rates))
    require(all(sp.simplify(P[0, 0]-mass) == 0 for P, mass in zip(spectral, masses)),
            'Exact root spectral weights, hence exact return mixture for all times')
    return Q, stationary


def projectors(Q, relaxation_rates):
    I = sp.eye(Q.rows)
    out = []
    annihilator = I
    for rate in relaxation_rates:
        annihilator = annihilator*(Q+rate*I)
    require(zero(annihilator), 'Displayed distinct rates annihilate the exact generator')
    for rate in relaxation_rates:
        P = I
        for other in relaxation_rates:
            if other != rate:
                P = P*(Q+other*I)/(other-rate)
        out.append(P.applyfunc(sp.simplify))
    require(zero(sum(out, sp.zeros(Q.rows))-I), 'Exact spectral projector resolution of identity')
    return out


def constant_step_case(sign, rates, weights, allocated_atoms=2):
    alpha, upper, epsilon = sp.Integer(1), sp.Integer(4), sp.Rational(1, 2)
    u, target_mean = sp.Rational(1, 3), sign*sp.Rational(1, 3)
    width, size = allocated_atoms+1, 2*(allocated_atoms+1)
    S = sp.Matrix([-1]+[1]*allocated_atoms+[1]+[-1]*allocated_atoms)
    initial = sp.zeros(1, size)
    initial[0], initial[width] = sp.Rational(1, 2), sp.Rational(1, 2)
    require((initial*S)[0] == 0, 'Fixed half-root preparation has zero binary mean')
    shifted = [rate-epsilon for rate in rates]
    block, block_pi = birth_death_from_root_measure(shifted, weights, 1-u)
    start = 0 if sign > 0 else width
    active = list(range(start, start+block.rows))
    frozen = [j for j in range(size) if j not in active]
    Qbase, pi = sp.zeros(size), sp.zeros(1, size)
    for i, global_i in enumerate(active):
        pi[global_i] = block_pi[i]/4
        for j, global_j in enumerate(active):
            Qbase[global_i, global_j] = block[i, j]
    frozen_mean = sign*(2*u+1)/3
    for readout in (-1, 1):
        group = [j for j in frozen if S[j] == readout]
        require(len(group) > 0, 'Both readout signs occur among frozen coordinates, including padding')
        mass = sp.Rational(3, 4)*(1+readout*frozen_mean)/2
        for j in group:
            pi[j] = mass/len(group)
    require(sum(pi) == 1 and all(value > 0 for value in pi), 'Strictly positive full stationary law')
    require((pi*S)[0] == target_mean and zero(pi*Qbase), 'Stationary reset law has the desired equilibrium mean')
    require(sp.diag(*pi)*Qbase == Qbase.T*sp.diag(*pi), 'Reducible base is reversible under the selected full law')
    projection = sp.ones(size, 1)*pi
    require(zero(Qbase*projection) and zero(projection*Qbase), 'Stationary reset commutes with base evolution')
    Q = Qbase+epsilon*(projection-sp.eye(size))
    require(zero(Q*sp.ones(size, 1)) and zero(pi*Q), 'Reset generator conservation and stationarity')
    require(all(Q[i, j] > 0 for i in range(size) for j in range(size) if i != j),
            'Reset makes the full generator irreducible by strictly positive off-diagonal rates')
    require(sp.diag(*pi)*Q == Q.T*sp.diag(*pi), 'Full predictor remains exactly reversible')
    relaxation_rates = [sp.Integer(0), epsilon]+list(rates)
    spectral = projectors(Q, relaxation_rates)
    coefficients = [sp.simplify((initial*P*S)[0]) for P in spectral]
    expected = [target_mean, sp.Integer(0)]+[-target_mean*w for w in weights]
    require(coefficients == expected, 'Exact constant-step mean has only the intended exponential mixture')
    require(spectral[0] == projection, 'Unique stationary projector equals the selected strictly positive law')
    x = sp.symbols('x')
    expected_characteristic = x*(x+epsilon)**(size-block.rows)*sp.prod(x+rate for rate in rates)
    require(sp.expand(Q.charpoly(x).as_expr()-expected_characteristic) == 0,
            'Exact spectral shift including formerly disconnected component modes')
    require(all(alpha/2 <= rate <= upper for rate in relaxation_rates[1:]),
            'Predictor retains the uniform full spectral band [alpha/2,B]')
    require(max(-Q[j, j] for j in range(size)) <= upper, 'Bounded full generator exit rates')
    return {'sign_of_field': sign, 'tanh_h_exact': str(target_mean),
            'allocated_mixture_atoms': allocated_atoms, 'actual_mixture_atoms': len(rates),
            'total_predictor_states': size, 'active_coordinates': active, 'frozen_coordinates': frozen,
            'fixed_initial_law_exact': [str(v) for v in initial],
            'fixed_binary_readout': list(S), 'active_Jacobi_generator_exact': str(block),
            'full_stationary_law_exact': [str(v) for v in pi],
            'strict_irreducibility_and_detailed_balance': True,
            'relaxation_rates_exact': [str(v) for v in relaxation_rates],
            'mean_spectral_coefficients_exact': [str(v) for v in coefficients],
            'reset_mode_readout_coefficient_exact': '0',
            'preparation_role': 'Intermediate exact half-root realization; the final full-support preparation and its error budget are checked separately.',
            'fixed_initial_law_is_hidden_stationary': zero(initial*Q),
            'exact_characteristic_polynomial': str(sp.factor(expected_characteristic)),
            'exact_mixture_mean_for_every_time': True}


def zero_field_case(allocated_atoms=2):
    width, size = allocated_atoms+1, 2*(allocated_atoms+1)
    S = [-1]+[1]*allocated_atoms+[1]+[-1]*allocated_atoms
    initial = sp.zeros(1, size)
    initial[0], initial[width] = sp.Rational(1, 2), sp.Rational(1, 2)
    zeta = sp.symbols('zeta', positive=True)
    pi = (1-zeta)*initial+zeta*sp.ones(1, size)/size
    Q = 2*(sp.ones(size, 1)*pi-sp.eye(size))
    lump = sp.Matrix([[int(sign == value) for value in (-1, 1)] for sign in S])
    telegraph = sp.Matrix([[-1, 1], [1, -1]])
    require(zero(Q*lump-lump*telegraph), 'Exact symbolic strong lumpability to the rate-one telegraph process')
    require(zero(pi*lump-sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])),
            'Full-support preparation is exactly sign-balanced')
    require(zero(pi*Q) and zero(sp.diag(*pi)*Q-Q.T*sp.diag(*pi)),
            'The final fixed preparation is stationary and reversible at zero field')
    require(zero(Q*Q+2*Q), 'Zero-field nonzero relaxation rate is exactly two')
    exact_l1 = sp.simplify(sum(abs(value) for value in pi-initial))
    require(sp.simplify(exact_l1-2*zeta*(1-sp.Rational(2, size))) == 0,
            'Exact total-variation perturbation from the intermediate half-root law')
    calibrations = []
    for tolerance in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        chosen = tolerance/4
        stationary = pi.subs(zeta, chosen)
        generator = Q.subs(zeta, chosen)
        require(all(value > 0 for value in stationary), 'Calibrated preparation has full support')
        require(all(generator[i, j] > 0 for i in range(size) for j in range(size) if i != j),
                'Calibrated zero-field generator is irreducible')
        require(exact_l1.subs(zeta, chosen) <= 2*chosen == tolerance/2,
                'Preparation changes every bounded binary mean by at most half the tolerance')
        calibrations.append({'tolerance': str(tolerance), 'zeta': str(chosen),
                             'full_support_fixed_preparation': [str(v) for v in stationary],
                             'exact_l1_preparation_change': str(exact_l1.subs(zeta, chosen)),
                             'all_fields_all_times_mean_error_budget': str(tolerance/2)})
    return {'total_predictor_states': size, 'stationary_law': '(1-zeta) half-roots + zeta uniform, 0<zeta<1',
            'exact_lumping_generator': str(telegraph), 'full_nonzero_relaxation_rate': '2',
            'entire_passive_visible_telegraph_law_preserved': True,
            'fixed_preparation_hidden_stationary': True,
            'symbolic_stationarity_detailed_balance_and_sign_balance': True,
            'all_time_preparation_bound_argument': 'A Markov semigroup contracts row l1 distance; the binary readout has sup norm one. Thus the exact initial l1 change bounds every mean change.',
            'preparation_calibrations': calibrations}


def covariance_identity():
    m, w = sp.symbols('m w', real=True)
    pi_h = sp.Matrix([[(1-m)/2, (1+m)*w/2, (1+m)*(1-w)/2]])
    pi0 = sp.Matrix([[sp.Rational(1, 2), w/2, (1-w)/2]])
    S = sp.Matrix([-1, 1, 1])
    centered = S-m*sp.ones(3, 1)
    require(zero(pi0-pi_h+m*(centered.T*sp.diag(*pi_h))/(1-m*m)),
            'Exact equilibrium-tilt identity behind the positive covariance mixture')
    require(sp.simplify((centered.T*sp.diag(*pi_h)*centered)[0]-(1-m*m)) == 0,
            'Binary stationary covariance normalization')
    return {'symbolic_equilibrium_tilt_identity': True, 'normalized_covariance_variance': '1-m^2'}


def quadrature_checks():
    lower, upper = sp.Integer(1), sp.Integer(4)
    nodes = [sp.Integer(1), sp.Rational(3, 2), sp.Integer(2), sp.Integer(3), sp.Integer(4)]
    weights = [sp.Rational(v, 9) for v in (1, 2, 3, 2, 1)]
    x, polys, norms, diagonals, ratios = recurrence(nodes, weights, 2)
    gaussian_nodes = sorted(sp.solve(polys[2], x), key=lambda v: float(v))
    mean = sum(v*w for v, w in zip(nodes, weights))
    lo, hi = gaussian_nodes
    gaussian_weights = [sp.simplify((hi-mean)/(hi-lo)), sp.simplify((mean-lo)/(hi-lo))]
    require(all(sp.simplify(v-lower) > 0 and sp.simplify(upper-v) > 0 for v in gaussian_nodes),
            'Gaussian nodes remain inside the common relaxation interval')
    require(all(w > 0 for w in gaussian_weights) and sp.simplify(sum(gaussian_weights)-1) == 0,
            'Gaussian quadrature weights are positive and normalized')
    for degree in range(4):
        discrepancy = sum(w*v**degree for v, w in zip(nodes, weights))-sum(w*v**degree for v, w in zip(gaussian_nodes, gaussian_weights))
        require(sp.simplify(discrepancy) == 0, 'Two-node Gaussian quadrature has exact moments through degree three')
    q, records = 1-lower/upper, []
    for tolerance in (sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 1000)):
        r = 1
        while 2*q**(2*r) > tolerance/2:
            r += 1
        bound = 2*q**(2*r)
        require(bound <= tolerance/2 and (r == 1 or 2*q**(2*(r-1)) > tolerance/2),
                'Exact rational calibration of the uniform positive quadrature tail')
        require(bound+2*(tolerance/4) <= tolerance,
                'Quadrature and full-support preparation budgets sum to at most the requested tolerance')
        records.append({'tolerance': str(tolerance), 'atoms_sufficient': r,
                        'uniform_quadrature_error_bound_exact': str(bound),
                        'preparation_error_budget': str(tolerance/2),
                        'combined_error_bound_exact': str(bound+tolerance/2),
                        'predictor_state_bound': 2*r+2})
    return {'interval': [str(lower), str(upper)], 'q_exact': str(q),
            'positive_gaussian_nodes_exact': [str(v) for v in gaussian_nodes],
            'positive_gaussian_weights_exact': [str(v) for v in gaussian_weights],
            'exact_polynomial_degrees_checked': [0, 1, 2, 3],
            'uniform_error_bound': '2(1-alpha/B)^(2r)',
            'analytic_tail_argument': 'For j>=2r, ((B-lambda)/B)^j <= q^(2r); the remaining exp(-Bt) Poisson series is at most one. Both positive measures have total mass one.',
            'rational_tolerance_calibrations': records,
            'scope': 'Exact quadrature moments and analytic all-time tail bookkeeping, not a sampled-time error guarantee.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/constant_step_compression.json'))
    args = parser.parse_args()
    cases = []
    for sign in (1, -1):
        cases.append(constant_step_case(sign, [sp.Integer(2), sp.Integer(3)],
                                        [sp.Rational(1, 4), sp.Rational(3, 4)]))
        cases.append(constant_step_case(sign, [sp.Rational(5, 2)], [sp.Integer(1)]))
    require(all(case['fixed_initial_law_exact'] == cases[0]['fixed_initial_law_exact']
                and case['fixed_binary_readout'] == cases[0]['fixed_binary_readout'] for case in cases),
            'All field signs and atom counts share exactly the same state labels, preparation, and readout')
    report = {'status': 'PASS',
              'scope': 'Exact small common reversible/irreducible constant-step predictors and analytic positive quadrature calibration.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
              'equilibrium_covariance_identity': covariance_identity(),
              'signed_and_padded_realization_cases': cases,
              'zero_field_passive_lumpability': zero_field_case(),
              'positive_quadrature_checks': quadrature_checks(),
              'largest_generator_dimension': 6,
              'no_simulation_or_numerical_rank_tests': True,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, default=str)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2, default=str))


if __name__ == '__main__':
    main()
