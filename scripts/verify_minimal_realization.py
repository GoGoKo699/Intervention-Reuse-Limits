#!/usr/bin/env python3
"""Small deterministic checks of the finite Jacobi kernel realization.

No sampling or network calls. Generic noncollision minimality is proved
by pole locations, not inferred from these numerical examples.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm

import verify_checkpoint as core
from verify_finite_accuracy import memory_matrix


def merge_spectrum(rates: np.ndarray, weights: np.ndarray
                   ) -> tuple[np.ndarray, np.ndarray]:
    """Aggregate repeated positive rates and discard zero-weight atoms."""
    rates = np.asarray(rates, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if (rates.ndim != 1 or rates.shape != weights.shape or not len(rates)
            or not np.all(np.isfinite(rates))
            or not np.all(np.isfinite(weights))
            or np.any(rates <= 0) or np.any(weights < 0)
            or not np.isfinite(weights.sum()) or weights.sum() <= 0):
        raise ValueError('positive finite rates and positive total finite mass required')
    active = weights > 0
    unique, index = np.unique(rates[active], return_inverse=True)
    mass = np.bincount(index, weights=weights[active], minlength=len(unique))
    return unique, mass


def realize_minimal_kernel(rates: np.ndarray, weights: np.ndarray
                          ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return mu, K, g, J for the r+1-hidden-state Jacobi construction.

    Full reorthogonalization stabilizes the small discrete-polynomial
    calculation. This verifier is not a certified numerical algorithm for
    arbitrarily ill-conditioned spectra.
    """
    rates, weights = merge_spectrum(rates, weights)
    W = float(weights.sum())
    scale = float(rates.max())
    support = np.r_[0., -rates / scale]
    spectral_mass = np.r_[.5, weights / (2 * W)]
    size = len(support)
    basis = np.zeros((size, size))
    basis[:, 0] = np.sqrt(spectral_mass)
    diagonal = np.zeros(size)
    adjacent = np.zeros(size - 1)
    for j in range(size):
        vector = support * basis[:, j]
        diagonal[j] = basis[:, j] @ vector
        # Gram--Schmidt on multiplication by x, twice for numerical stability.
        for _ in range(2):
            vector -= basis[:, :j+1] @ (basis[:, :j+1].T @ vector)
        residual = float(np.linalg.norm(vector))
        if j + 1 < size:
            core.require(residual > 1e-13, 'Distinct support gives positive recurrence')
            adjacent[j] = residual
            basis[:, j+1] = vector / residual
        else:
            core.require(residual < 2e-12, 'Terminal polynomial recurrence')
    J = scale * (np.diag(diagonal) + np.diag(adjacent, 1) + np.diag(adjacent, -1))
    eigenvalues, eigenvectors = np.linalg.eigh(J)
    core.require(abs(eigenvalues[-1]) < 2e-12 * max(1., scale), 'Top eigenvalue zero')
    v = eigenvectors[:, -1]
    if v[0] < 0:
        v = -v
    core.require(np.all(v > 0), 'Strictly positive Perron vector')
    mu = v * v
    K = J * v[None, :] / v[:, None]
    g = np.full(size, -np.sqrt(W))
    g[0] = np.sqrt(W)
    return mu, K, g, J


def deterministic_checks() -> dict:
    examples = [
        ('one_mode_collision', 1., [1.], [.36]),
        ('two_modes_nonuniform', 1., [.25, 2.5], [.08, .42]),
        ('three_modes_collision', 1., [.4, 1., 3.], [.02, .13, .35]),
        ('repeated_rates', .7, [.2, .7, .2, 2., 2.], [.02, .11, .18, .2, .13]),
        ('four_modes_nonuniform', .7, [.03, .4, 2., 6.], [.01, .04, .17, .42]),
        ('zero_weight_discarded', 1., [.2, .4, 1.4], [.2, 0., .4]),
    ]
    protocol = [(.2, 1.), (.6, -.7), (.4, 0.), (.8, .35)]
    max_kernel_error = 0.
    max_spectral_error = 0.
    max_taylor_error = 0.
    max_rowsum = 0.
    max_balance = 0.
    max_half_mass_error = 0.
    largest_matrix = 0
    records = []
    for label, k, raw_rates, raw_weights in examples:
        rates, weights = merge_spectrum(np.array(raw_rates), np.array(raw_weights))
        W = float(weights.sum())
        mu, K, g, J = realize_minimal_kernel(np.array(raw_rates), np.array(raw_weights))
        hidden = len(mu)
        core.require(hidden == len(rates) + 1, 'Realization dimension')
        offdiag = K.copy()
        np.fill_diagonal(offdiag, 0.)
        core.require(np.all(offdiag >= 0), 'Generator offdiagonal positivity')
        core.require(np.all(np.diag(K, 1) > 0) and np.all(np.diag(K, -1) > 0),
                     'Birth-death irreducibility')
        rowsum = float(np.max(abs(K.sum(axis=1))))
        balance = float(np.max(abs(mu[:, None] * K - K.T * mu[None, :])))
        half_error = float(abs(mu[0] - .5))
        max_rowsum = max(max_rowsum, rowsum)
        max_balance = max(max_balance, balance)
        max_half_mass_error = max(max_half_mass_error, half_error)
        core.require(rowsum < 1e-12, 'Generator row sums')
        core.require(balance < 1e-12, 'Detailed balance')
        core.require(abs(mu.sum() - 1.) < 1e-12 and half_error < 1e-12,
                     'Normalized equilibrium and first-state mass')
        core.require(abs(mu @ g) < 1e-12, 'Centered sensitivity')
        core.require(np.max(abs(abs(g) - np.sqrt(W))) < 1e-12,
                     'Pointwise sensitivity magnitude')
        eigenvalues, eigenvectors = np.linalg.eigh(J)
        wanted_values = np.sort(np.r_[-rates, 0.])
        spectral_error = float(np.max(abs(eigenvalues - wanted_values)))
        recovered_weights = eigenvectors[0, :] ** 2
        original_order = np.argsort(np.r_[0., -rates])
        wanted_weights = np.r_[.5, weights / (2 * W)][original_order]
        spectral_error = max(spectral_error, float(np.max(abs(recovered_weights - wanted_weights))))
        max_spectral_error = max(max_spectral_error, spectral_error)
        core.require(spectral_error < 2e-11, 'Prescribed spectral measure')
        local_kernel_error = 0.
        for t in (0., .03, .3, 1., 4.):
            actual = float((mu * g) @ expm(t * K) @ g)
            target = float(weights @ np.exp(-rates * t))
            local_kernel_error = max(local_kernel_error, abs(actual - target))
            core.require(abs(actual - target) < 2e-11, 'Reconstructed kernel')
        max_kernel_error = max(max_kernel_error, local_kernel_error)

        # Compare complete generator Taylor coefficients with the memory system.
        coefficients = core.generator_coefficients(k, mu, K, g)
        total = hidden + 1
        observable = np.r_[-1., np.ones(hidden)]
        full = np.zeros(4 * total)
        full[:total] = np.r_[.5, .5 * mu]
        memory = np.zeros(4 + len(rates))
        memory[0] = 1.
        local_taylor_error = 0.
        largest_matrix = max(largest_matrix, len(full))
        for duration, u in protocol:
            full = expm(duration * core.block_matrix(coefficients, u)) @ full
            memory = expm(duration * memory_matrix(k, rates, weights, u)) @ memory
            actual = np.array([observable @ full[j*total:(j+1)*total] for j in range(4)])
            target = np.array([0., memory[1], 0., memory[2] + memory[3]])
            error = float(np.max(abs(actual - target)))
            local_taylor_error = max(local_taylor_error, error)
            core.require(error < 2e-10, 'Full Markov and memory Taylor response')
        max_taylor_error = max(max_taylor_error, local_taylor_error)
        records.append({'case': label, 'input_atoms': len(raw_rates),
                        'distinct_active_rates': len(rates), 'total_states': total,
                        'contains_visible_rate_collision': bool(np.any(rates == k)),
                        'kernel_mass': W, 'kernel_error': local_kernel_error,
                        'taylor_error': local_taylor_error})

    invalid_rejected = 0
    for rates, weights in [([0.], [1.]), ([1.], [-1.]), ([1.], [0.]),
                           ([1., 2.], [1.]), ([float('inf')], [1.])]:
        try:
            realize_minimal_kernel(np.array(rates), np.array(weights))
        except ValueError:
            invalid_rejected += 1
    core.require(invalid_rejected == 5, 'Invalid inputs rejected')
    return {'cases': records, 'cases_checked': len(records),
            'protocol_comparisons': len(records) * len(protocol),
            'max_kernel_error': max_kernel_error,
            'max_spectral_measure_error': max_spectral_error,
            'max_full_markov_memory_error': max_taylor_error,
            'max_generator_row_sum': max_rowsum,
            'max_detailed_balance_error': max_balance,
            'max_first_state_mass_error': max_half_mass_error,
            'largest_matrix_dimension': largest_matrix,
            'invalid_inputs_rejected': invalid_rejected}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/minimal_realization.json'))
    args = parser.parse_args()
    report = {'status': 'PASS',
              'scope': 'Deterministic consistency checks; minimality requires the noncollision proof.',
              'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                           'scipy': scipy.__version__},
              'minimal_realization': deterministic_checks(),
              'source_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                for name in ('verify_checkpoint.py', 'verify_finite_accuracy.py',
                                             'verify_minimal_realization.py')}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
