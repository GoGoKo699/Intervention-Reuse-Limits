#!/usr/bin/env python3
"""Deterministic checks for the finite-accuracy note; no network or sampling."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
from scipy.linalg import expm
import scipy

import verify_checkpoint as core


def compress_spectrum(k: float, rates: np.ndarray, weights: np.ndarray,
                      bins: int) -> tuple[np.ndarray, np.ndarray, float]:
    """Equal-width midpoint quantization of theta=k/(k+lambda).

    Return active rates, their positive masses, and the U=1 response certificate.
    This requires the intervention kernel; passive observations do not supply it.
    """
    if k <= 0 or bins < 1 or int(bins) != bins:
        raise ValueError('k must be positive and bins a positive integer')
    if (rates.ndim != 1 or rates.shape != weights.shape or len(rates) == 0
            or not np.all(np.isfinite(rates)) or not np.all(np.isfinite(weights))
            or np.any(rates <= 0) or np.any(weights < 0)):
        raise ValueError('finite positive rates and nonnegative matching weights required')
    theta = k / (k + rates)
    index = np.minimum((bins * theta).astype(int), bins - 1)
    centers = (np.arange(bins) + .5) / bins
    mass = np.bincount(index, weights=weights, minlength=bins)
    certificate = float(2 * np.dot(weights, abs(theta - centers[index])))
    active = mass > 0
    return k * (1 / centers[active] - 1), mass[active], certificate


def realize_kernel(rates: np.ndarray, weights: np.ndarray
                   ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Irreducible reversible paired-state realization of a positive kernel."""
    if (rates.ndim != 1 or rates.shape != weights.shape or len(rates) == 0
            or not np.all(np.isfinite(rates)) or not np.all(np.isfinite(weights))
            or np.any(rates <= 0) or np.any(weights <= 0)):
        raise ValueError('finite strictly positive rates and weights required')
    W = float(weights.sum())
    mu = np.repeat(weights / (2 * W), 2)
    g = np.tile([np.sqrt(W), -np.sqrt(W)], len(rates))
    beta = float(rates.min() / 2)
    H = beta * (np.ones((len(mu), 1)) @ mu[None, :] - np.eye(len(mu)))
    for j, rate in enumerate(rates):
        a, b = 2 * j, 2 * j + 1
        flip = (rate - beta) / 2
        H[a, b] += flip
        H[b, a] += flip
        H[a, a] -= flip
        H[b, b] -= flip
    return mu, H, g


def memory_matrix(k: float, rates: np.ndarray, weights: np.ndarray,
                  u: float) -> np.ndarray:
    """Generator for [1,m1,b3,delta,memory_modes] on one constant-u segment."""
    A = np.zeros((4 + len(rates), 4 + len(rates)))
    W = float(weights.sum())
    A[1, 0], A[1, 1] = 2*k*u, -2*k
    A[2, 0], A[2, 1], A[2, 2] = k*u**3/3, -k*u*u, -2*k
    A[3, 0], A[3, 1], A[3, 3] = k*W*u**3, -k*W*u*u, -2*k
    A[3, 4:] = -2*k*k*u*weights
    A[4:, 0], A[4:, 1] = u*u, -u
    A[4:, 4:] = -np.diag(k + rates)
    return A


def normalized_path_checks() -> dict:
    examples = []
    max_weight_error = 0.
    minimum_signal = float('inf')
    tau = .25
    signal_bound = float(np.exp(-2*tau)*(3*tau+2-2*np.exp(tau))/4)
    for M in range(2, 25):
        k, mu, H, _ = core.path_model(M)
        alternating = (-1.)**np.arange(M)
        endpoint = np.zeros(M)
        endpoint[0] = 1.
        g = (alternating-alternating.mean()+endpoint-1/M)/2
        ell = np.arange(1, M)
        angle = np.pi*ell/(2*M)
        parity = ((M+ell) % 2 == 1).astype(float)
        weights = (np.cos(angle)+parity/np.cos(angle))**2/(2*M*M)
        rates = 2*.1*(1-np.cos(np.pi*ell/M))
        lam, numeric_weights = core.hidden_spectrum(mu, H, g)
        error = float(np.max(abs(weights-numeric_weights)))
        max_weight_error = max(max_weight_error, error)
        W = float(mu @ (g*g))
        core.require(abs(mu@g) < 1e-13, 'Normalized sensitivity centered')
        core.require(np.max(abs(g)) <= 1, 'Normalized sensitivity bounded')
        core.require(W >= .25 and abs(W-weights.sum()) < 1e-12, 'Nonvanishing mass')
        core.require(np.all(weights > 0) and np.all(rates < k), 'All modes active')
        core.require(error < 2e-12 and np.max(abs(lam-rates)) < 1e-12, 'Mode formula')
        m3 = core.predicted_coefficients(tau/k, k, rates, weights)[3]
        baseline = -(1-np.exp(-2*tau))/3+tau*np.exp(-2*tau)
        signal = float(m3-baseline)
        minimum_signal = min(minimum_signal, signal)
        core.require(signal+1e-12 >= signal_bound, 'Nonvanishing step correction')
        if M in (2, 3, 8, 24):
            examples.append({'microscopic_states':M+1, 'kernel_mass':W,
                             'min_weight':float(weights.min()), 'cubic_correction':signal})
    return {'models_checked':23, 'max_spectral_weight_error':max_weight_error,
            'step_time_in_units_1_over_k':tau, 'proved_signal_lower_bound':signal_bound,
            'min_sampled_signal':minimum_signal, 'examples':examples}


def approximation_checks() -> dict:
    # Wide kinetic range tests the absence of a spectral-bandwidth assumption.
    k = .7
    protocol = [(.3, 1.), (.8, -.6), (1.2, 0.), (2., .4), (1.1, -1.)]
    U = max(abs(u) for _, u in protocol)
    max_ratio = 0.
    max_kernel_error = 0.
    max_full_error = 0.
    largest_matrix = 0
    cases = []
    for count in (5, 13, 31):
        rates = k*np.geomspace(.005, 40., count)
        raw = 1+np.sin(np.arange(count)+.3)**2
        weights = .64*raw/raw.sum()
        for q in (1, 2, 4, 8):
            new_rates, new_weights, certificate = compress_spectrum(k, rates, weights, q)
            W = float(weights.sum())
            core.require(abs(new_weights.sum()-W) < 1e-12, 'Mass preserved')
            core.require(certificate <= W/q+1e-12, 'Universal certificate')
            mu, H, g = realize_kernel(new_rates, new_weights)
            core.require(np.max(abs(H.sum(axis=1))) < 2e-12, 'Realization row sums')
            core.require(np.max(abs(mu[:,None]*H-H.T*mu[None,:])) < 2e-12,
                         'Realization detailed balance')
            offdiag = H.copy(); np.fill_diagonal(offdiag, 0.)
            core.require(np.all(offdiag[~np.eye(len(mu),dtype=bool)] > 0),
                         'Realization irreducibility')
            core.require(abs(mu@g) < 1e-12 and np.max(abs(g)) <= 1,
                         'Realization bounded centered sensitivity')
            for t in (0., .1, 1., 5.):
                recovered = float((mu*g) @ expm(t*H) @ g)
                target = float(new_weights @ np.exp(-new_rates*t))
                max_kernel_error = max(max_kernel_error, abs(recovered-target))
                core.require(abs(recovered-target) < 2e-11, 'Realized kernel')
            y = np.zeros(4+len(rates)); y[0] = 1.
            z = np.zeros(4+len(new_rates)); z[0] = 1.
            B = core.generator_coefficients(k, mu, H, g)
            n = len(mu)+1
            full = np.zeros(4*n); full[:n] = np.r_[.5, .5*mu]
            observable = np.r_[-1., np.ones(len(mu))]
            largest_matrix = max(largest_matrix, 4*n, len(y))
            max_error = 0.
            for duration, u in protocol:
                A, R = memory_matrix(k,rates,weights,u), memory_matrix(k,new_rates,new_weights,u)
                for fraction in (.25, .5, .75, 1.):
                    yy, zz = expm(duration*fraction*A)@y, expm(duration*fraction*R)@z
                    error = float(abs(yy[2]+yy[3]-zz[2]-zz[3]))
                    max_error = max(max_error, error)
                    core.require(error <= U**3*certificate+2e-11, 'Protocol certificate')
                y, z = yy, zz
                full = expm(duration*core.block_matrix(B,u))@full
                full_error = float(abs(observable@full[3*n:4*n]-z[2]-z[3]))
                max_full_error = max(max_full_error, full_error)
                core.require(full_error < 2e-10, 'Full Markov / memory response')
            max_ratio = max(max_ratio, max_error/(U**3*certificate))
            cases.append({'source_modes':count, 'bins':q, 'active_bins':len(new_rates),
                          'surrogate_states':n, 'observed_error':max_error,
                          'transport_certificate':U**3*certificate, 'uniform_bound':U**3*W/q})
    # Zero response mass needs no hidden memory; the grid routine preserves zero.
    rr, ww, cert = compress_spectrum(1., np.array([.1,2.]), np.zeros(2), 2)
    core.require(len(rr)==len(ww)==0 and cert==0, 'Zero-mass boundary')
    # Invalid inputs must fail rather than produce misleading certificates.
    failures = 0
    for k0, r0, w0, q0 in [(0.,[1.],[1.],2), (1.,[-1.],[1.],2),
                            (1.,[1.],[-1.],2), (1.,[1.],[1.],0)]:
        try:
            compress_spectrum(k0,np.array(r0),np.array(w0),q0)
        except ValueError:
            failures += 1
    core.require(failures == 4, 'Input validation')
    return {'cases':cases, 'cases_checked':len(cases), 'protocol_samples':len(cases)*len(protocol)*4,
            'max_observed_error_over_certificate':max_ratio,
            'max_realized_kernel_error':max_kernel_error,
            'max_full_markov_memory_error':max_full_error,
            'largest_matrix_dimension':largest_matrix, 'invalid_inputs_rejected':failures}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/finite_accuracy.json'))
    args = parser.parse_args()
    report = {'status':'PASS', 'scope':'Deterministic consistency checks, not proof review or novelty certification.',
              'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
              'normalized_family':normalized_path_checks(), 'finite_accuracy':approximation_checks(),
              'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                               for name in ('verify_checkpoint.py','verify_finite_accuracy.py')}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
