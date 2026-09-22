#!/usr/bin/env python3
"""Deterministic checks of exact finite-field kernel closure and its certificate.

The all-protocol/all-horizon bounds and minimax lower bounds are analytic
proofs. These tests compare independent finite-dimensional formulations,
including fields of order one; they do not infer a theorem from sampling.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
import sympy
from scipy.linalg import expm

import verify_checkpoint as core
from verify_minimal_realization import realize_minimal_kernel
from verify_quadrature import compress_tapered, component_certificate


def generator(k, mu, K, g, h):
    """Direct physical column generator at a finite real field."""
    Q = np.zeros((len(mu) + 1, len(mu) + 1))
    Q[0, 1:] = k * mu * np.exp((1 + g) * h)
    Q[1:, 0] = k * np.exp((g - 1) * h)
    Q[1:, 1:] = K
    np.fill_diagonal(Q, 0.)
    np.fill_diagonal(Q, -Q.sum(axis=1))
    return Q.T


def modal_matrix(k, rates, weights, h):
    """Exact kernel closure in coordinates (1, p_A, w_1,...,w_r).

    Hidden relative density at state 0 is
    x_0 = 1-p_A + sum(c_j*w_j)/(2W).
    Each w_j is the convolution of the same normalized source with
    exp[-integral alpha - lambda_j*t]. This is an independent reduction
    of the physical master equation, not a Taylor expansion.
    """
    W = float(sum(weights))
    s = math.sqrt(W)
    alpha = k * math.exp(-(1+s)*h)
    beta = k * math.exp(-h) * (math.exp(s*h)-math.exp(-s*h))
    E = math.exp(2*h)
    b = alpha + beta/2
    matrix = np.zeros((len(rates)+2, len(rates)+2))
    matrix[1, 0] = b
    matrix[1, 1] = -b*(1+E)
    matrix[1, 2:] = beta*weights/(4*W)
    matrix[2:, 0] = -beta
    matrix[2:, 1] = beta*(1+E)
    matrix[2:, 2:] = -np.diag(alpha+rates) - beta*weights[None, :]/(2*W)
    return matrix


def exact_recursion():
    b = [Fraction(1)]
    for j in range(1, 5):
        b.append(2*sum(b[j-l]/math.factorial(l) for l in range(1, j+1)))
    wanted = [Fraction(1), Fraction(2), Fraction(5), Fraction(37,3), Fraction(365,12)]
    core.require(b == wanted, 'Exact uniform coefficient recursion')
    residual = 2*sum(b[j]/math.factorial(4-j) for j in range(4))
    core.require(residual == b[4], 'Exact cubic residual coefficient')
    return {'coefficient_bounds': [str(x) for x in b],
            'cubic_residual_constant': str(residual)}


def fixed_step_checks():
    records = []
    for r in (5, 7):
        W, k, H = .36, 1., .02
        s = math.sqrt(W)
        h = min(H, 1/(20*(1+s)))
        eta = math.pi*math.sqrt(2/(3*(r-1)))
        nodes = 4*np.exp(np.arange(r)*eta)
        rates, weights = nodes-1.5, np.full(r, W/r)
        mu, K, g, _ = realize_minimal_kernel(rates, weights)
        Q = generator(k, mu, K, g, h).T
        pi_h = np.r_[math.exp(-h), mu*math.exp(h)]/(2*math.cosh(h))
        pi0 = np.r_[.5, .5*mu]
        observable = np.r_[-1., np.ones(len(mu))]
        physical = -np.sqrt(pi_h)[:, None]*Q/np.sqrt(pi_h)[None, :]
        physical = (physical+physical.T)/2
        actual = np.linalg.eigvalsh(physical)[1:]
        gamma = math.exp(-h)*math.sinh(s*h)
        kappa = math.exp(-(1+s)*h)
        diagonal = np.r_[2*math.exp(-s*h)*math.cosh(h), rates+kappa]
        v = np.r_[math.sqrt(1+math.exp(2*h)), np.sqrt(weights/W)]
        block = np.diag(diagonal)+gamma*np.outer(v,v)
        eigenvalues, eigenvectors = np.linalg.eigh(block)
        spectral_error = float(max(abs(actual-eigenvalues)))
        core.require(spectral_error < 2e-8, 'Exact rank-one field spectrum')
        shifts = eigenvalues[1:]-diagonal[1:]
        core.require(min(shifts) >= gamma/(2*r) and max(shifts) <= 2*gamma/r,
                     'Secular root enclosures on geometric witnesses')
        spectral_weights = eigenvectors[0, :]**2
        floor = 2*gamma**2/(5*r*nodes[-1]**2)
        core.require(min(spectral_weights[1:]) >= floor, 'Hidden visible-weight floor')
        gram_nodes = eigenvalues[1:]+.5
        core.require(min(np.diff(np.log(gram_nodes))) >= eta/2, 'Logarithmic Gram spacing')
        mean_error = 0.
        for t in (0., .001, .01, .1, 1., 4.):
            mean = pi0@expm(t*Q)@observable
            spectral = math.tanh(h)*(1-spectral_weights@np.exp(-eigenvalues*t))
            mean_error = max(mean_error, abs(float(mean-spectral)))
        core.require(mean_error < 3e-10, 'Exact finite-field positive spectral step formula')
        records.append({'hidden_modes':r,'fixed_step_amplitude':h,
                        'spectrum_discrepancy':spectral_error,
                        'step_mean_discrepancy':mean_error,
                        'min_shift_over_gamma_per_mode':float(min(shifts)*r/gamma),
                        'max_shift_over_gamma_per_mode':float(max(shifts)*r/gamma),
                        'smallest_observable_hidden_weight':float(min(spectral_weights[1:])),
                        'proved_weight_floor':float(floor)})
    return {'cases':records,'scope':'Small numerical consistency of exact spectral identities and analytic enclosures; no numerical rank inference.'}


def checks():
    examples = [
        (1., np.array([.2, 1., 3.]), np.array([.1, .15, .25])),
        (.7, np.array([.03, .4, 2., 6.]), np.array([.01, .04, .17, .42])),
        (1.3, np.array([.05, .2, .6, 1., 2., 4., 9., 14.]), np.full(8, .08)),
    ]
    protocols = [
        [(.25, .8), (.3, -.6), (.5, 0.), (.4, .35)],
        [(.1, -1.2), (.4, 1.2), (.2, -.8), (.5, .9)],
        [(2., .5), (3., -.5), (4., 0.)],
    ]
    maximum_closure = maximum_remainder_ratio = maximum_certificate_ratio = 0.
    largest = comparisons = compression_cases = 0
    records = []
    for k, rates, weights in examples:
        W = float(sum(weights))
        mu, K, g, _ = realize_minimal_kernel(rates, weights)
        N = len(mu)+1
        observable = np.r_[-1., np.ones(len(mu))]
        pi = np.r_[.5, .5*mu]
        largest = max(largest, 4*N)
        local = 0.
        for protocol in protocols:
            full, modal = pi.copy(), np.r_[1., .5, np.zeros(len(rates))]
            for duration, h in protocol:
                Q = generator(k, mu, K, g, h)
                reset_rate = k*math.exp(-(1+math.sqrt(W))*abs(h))
                reset = np.zeros_like(Q)
                reset[0, :] = reset_rate
                reset -= reset_rate*np.eye(N)
                residual = Q-reset
                offdiag = residual.copy()
                np.fill_diagonal(offdiag, 0.)
                core.require(np.min(offdiag) > -1e-12, 'Reset residual is Markov')
                core.require(np.max(abs(residual.sum(axis=0))) < 1e-12,
                             'Reset decomposition conserves mass')
                full = expm(duration*Q) @ full
                modal = expm(duration*modal_matrix(k, rates, weights, h)) @ modal
                error = abs(float(observable@full - (1-2*modal[1])))
                local = max(local, error)
                comparisons += 1
                core.require(error < 3e-11, 'Exact full-field mean matches modal closure')
                core.require(abs(sum(full)-1) < 1e-11 and np.min(full) > -1e-12,
                             'Physical finite-field probability law')
        maximum_closure = max(maximum_closure, local)

        # Taylor hierarchy and finite-field master equation are independent
        # here; compare the proved all-time bound on selected weak protocols.
        coefficients = core.generator_coefficients(k, mu, K, g)
        weak_protocol = [(.2, 1.), (.7, -.6), (.4, .3)]
        for amplitude in (.02, .05):
            full = pi.copy()
            hierarchy = np.zeros(4*N)
            hierarchy[:N] = pi
            bound = float(Fraction(365,12))*math.exp(2*(1+math.sqrt(W))*amplitude) * ((1+math.sqrt(W))*amplitude)**4
            for duration, u in weak_protocol:
                full = expm(duration*generator(k, mu, K, g, amplitude*u)) @ full
                hierarchy = expm(duration*core.block_matrix(coefficients,u)) @ hierarchy
                polynomial = amplitude*(observable@hierarchy[N:2*N]) + amplitude**3*(observable@hierarchy[3*N:])
                ratio = abs(float(observable@full-polynomial))/bound
                maximum_remainder_ratio = max(maximum_remainder_ratio, ratio)
                core.require(ratio <= 1+1e-10, 'Uniform remainder bound at sampled protocols')

        # Select a nontrivial approximation using the theorem's field-dependent
        # damping. The physical k is deliberately left unchanged.
        H = .8
        alpha = k*math.exp(-(1+math.sqrt(W))*H)
        approximation = compress_tapered(alpha, rates, weights, 1)
        if len(approximation.rates) < len(rates):
            mu2, K2, g2, _ = realize_minimal_kernel(approximation.rates, approximation.weights)
            full, reduced = pi.copy(), np.r_[.5, .5*mu2]
            obs2 = np.r_[-1., np.ones(len(mu2))]
            integral_bound = component_certificate(approximation)[0]/alpha
            B = 2*math.sinh(math.sqrt(W)*H)
            certificate = k*k*math.exp(2*H)*B*B/(alpha*W)*integral_bound
            core.require(certificate > 0, 'Nonzero compression certificate')
            for duration, h in protocols[0]:
                full = expm(duration*generator(k, mu, K, g, h)) @ full
                reduced = expm(duration*generator(k, mu2, K2, g2, h)) @ reduced
                ratio = abs(float(observable@full-obs2@reduced))/certificate
                maximum_certificate_ratio = max(maximum_certificate_ratio, ratio)
                core.require(ratio <= 1+1e-10, 'Finite-field compression certificate')
            compression_cases += 1
        records.append({'k':k, 'kernel_mass':W, 'active_modes':len(rates),
                        'states':N, 'max_closure_discrepancy':local,
                        'compressed_modes_at_n1':len(approximation.rates)})
    core.require(compression_cases >= 1, 'A genuinely reduced model was checked')
    return {'models':records, 'finite_field_protocol_comparisons':comparisons,
            'largest_absolute_field':1.2,
            'max_full_master_modal_discrepancy':maximum_closure,
            'max_observed_remainder_over_bound':maximum_remainder_ratio,
            'nontrivial_compression_cases':compression_cases,
            'max_observed_compression_error_over_certificate':maximum_certificate_ratio,
            'largest_matrix_dimension':largest,
            'scope':'Finite deterministic consistency checks; uniformity and lower bounds follow from the proofs.'}


def verify_same_kernel_higher_response_boundary():
    """Exact symbolic check for FINITE_FIELD.md Section 10; no numerical fitting."""
    import sympy as sp

    eta = sp.symbols("eta", real=True)
    x = sp.symbols("x", positive=True)  # x = exp(h)
    g = (-1, 0, 1)
    mu = sp.Matrix([[sp.Rational(1, 3)] * 3])
    p0 = sp.Matrix([[sp.Rational(1, 2)] + [sp.Rational(1, 6)] * 3])
    readout = sp.Matrix([-1, 1, 1, 1])
    gv = sp.Matrix(g)
    w = sp.Matrix([1, -2, 1])
    projector_w = w * w.T / 6
    internal = sp.Matrix([
        [-sp.Rational(1, 2) - eta / 6, eta / 3, sp.Rational(1, 2) - eta / 6],
        [eta / 3, -2 * eta / 3, eta / 3],
        [sp.Rational(1, 2) - eta / 6, eta / 3, -sp.Rational(1, 2) - eta / 6],
    ])
    assert internal * sp.ones(3, 1) == sp.zeros(3, 1)
    assert mu * internal == sp.zeros(1, 3)
    assert internal == internal.T
    assert internal * gv == -gv
    assert internal.diff(eta) == -projector_w
    assert (gv.T * gv)[0] / 3 == sp.Rational(2, 3)
    for value in (1, 2):
        assert all(internal.subs(eta, value)[i, j] > 0
                   for i in range(3) for j in range(3) if i != j)

    internal_full = sp.zeros(4)
    internal_full[1:, 1:] = internal
    star = sp.zeros(4)
    for j, gj in enumerate(g, start=1):
        star[0, j] = x ** (1 + gj) / 3
        star[j, 0] = x ** (gj - 1)
    for i in range(4):
        star[i, i] = -sum(star[i, j] for j in range(4) if j != i)
    generator = star + internal_full
    assert p0 * internal_full == sp.zeros(1, 4)
    assert internal_full * readout == sp.zeros(4, 1)
    assert all(sp.simplify(entry) == 0 for entry in p0 * generator.subs(x, 1))
    for order in (1, 2):
        assert sp.simplify((p0 * generator ** order * readout)[0].diff(eta)) == 0
    third = (p0 * generator ** 3 * readout)[0]
    expected_eta_derivative = (x - 1) ** 5 * (x + 1) / (18 * x ** 4)
    assert sp.factor(sp.diff(third, eta) - expected_eta_derivative) == 0
    assert sp.factor(sp.diff(third, eta, 2)) == 0

    # Independently extract [h^5] Q(h)^3 by coefficient convolution.
    coefficients = []
    for n in range(6):
        coefficient = sp.zeros(4)
        for j, gj in enumerate(g, start=1):
            coefficient[0, j] = sp.Rational((1 + gj) ** n, 3 * sp.factorial(n))
            coefficient[j, 0] = sp.Rational((gj - 1) ** n, sp.factorial(n))
        for i in range(4):
            coefficient[i, i] = -sum(coefficient[i, j] for j in range(4) if j != i)
        if n == 0:
            coefficient += internal_full
        coefficients.append(coefficient)
    cubic_time_fifth_field = sp.factor(sum(
        (p0 * coefficients[i] * coefficients[j] * coefficients[5 - i - j] * readout)[0]
        for i in range(6) for j in range(6 - i)
    ))
    assert sp.simplify(cubic_time_fifth_field - (5 * eta + 1478) / 45) == 0
    for time_order in (1, 2):
        if time_order == 1:
            field_coefficient = (p0 * coefficients[5] * readout)[0]
        else:
            field_coefficient = sum(
                (p0 * coefficients[j] * coefficients[5 - j] * readout)[0]
                for j in range(6)
            )
        assert sp.simplify(sp.diff(field_coefficient, eta)) == 0

    return {
        "kernel": "(2/3)*exp(-t), independent of eta",
        "same_actuator_parameters": "k=1, mu=(1/3,1/3,1/3), g=(-1,0,1)",
        "positive_generator_parameters_checked": [1, 2],
        "d_eta_d3_time_exact_mean": str(sp.factor(expected_eta_derivative)),
        "d3_time_fifth_field_coefficient": str(cubic_time_fifth_field),
        "leading_fifth_response_difference": "(eta2-eta1)*t^3/54 + O(t^4)",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/finite_field.json'))
    args = parser.parse_args()
    report = {'status':'PASS',
              'scope':'Exact finite-field closure and uniform-certificate consistency; no statistical or interval certification.',
              'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},
              'exact_recursion':exact_recursion(), 'finite_field':checks(),
              'fixed_step_lower':fixed_step_checks(),
              'same_kernel_boundary':verify_same_kernel_higher_response_boundary(),
              'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                               for name in ('verify_checkpoint.py','verify_finite_accuracy.py',
                                            'verify_quadrature.py','verify_minimal_realization.py',
                                            'verify_finite_field.py')}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
