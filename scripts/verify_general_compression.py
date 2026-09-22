#!/usr/bin/env python3
"""Small deterministic checks of the general-family compression construction.

Exact word probabilities verify the canonical finite-memory realization.
Selected matrix calculations check the semigroup and mean-error estimates;
they do not establish their uniform scope, which comes from the proof.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def exact_word_construction() -> dict:
    # P is exp(K) for the product of two reversible two-state chains,
    # with nonzero decay rates log(2) and log(3).
    def bit_transition(r):
        return sp.Matrix([[(1+r)/2, (1-r)/2], [(1-r)/2, (1+r)/2]])

    P = sp.kronecker_product(bit_transition(sp.Rational(1, 2)),
                             bit_transition(sp.Rational(1, 3)))
    mu = sp.ones(1, 4)/4
    original = sp.Matrix([-1, -sp.Rational(1, 4), sp.Rational(1, 4), 1])
    symbols = [-1, 0, 0, 1]
    alphabet = (-1, 0, 1)
    projections = {z: sp.diag(*[int(a == z) for a in symbols]) for z in alphabet}

    def probability(word):
        row = mu*projections[word[0]]
        for z in word[1:]:
            row = row*P*projections[z]
        return (row*sp.ones(4, 1))[0]

    words = list(itertools.product(alphabet, repeat=2))
    index = {word: i for i, word in enumerate(words)}
    nu = sp.Matrix([[probability(w) for w in words]])
    R = sp.zeros(len(words))
    for i, w in enumerate(words):
        for z in alphabet:
            R[i, index[(w[1], z)]] = probability(w+(z,))/nu[i]
    gamma = sp.Matrix([w[-1] for w in words])
    require(R*sp.ones(9, 1) == sp.ones(9, 1), 'Word transition row sums')
    require(nu*R == nu, 'Exact stationary word law')
    require(all(v > 0 for v in nu), 'All stationary word masses are positive')
    require((nu*gamma)[0] == 0, 'Centered word sensitivity')
    require((nu*sp.diag(*gamma)*gamma)[0] == sp.Rational(1, 2), 'Word variance')
    loss = (mu*sp.diag(*original)*original)[0]-sp.Rational(1, 2)
    residual = original-sp.Matrix(symbols)
    require(loss == (mu*sp.diag(*residual)*residual)[0] == sp.Rational(1, 32),
            'Conditional-mean quantization variance identity')
    require(max(abs(v) for v in residual) == sp.Rational(1, 4), 'Quantization error')

    lifted_projections = {z: sp.diag(*[int(v == z) for v in gamma]) for z in alphabet}

    def lifted_probability(word):
        row = nu*lifted_projections[word[0]]
        for z in word[1:]:
            row = row*R*lifted_projections[z]
        return (row*sp.ones(9, 1))[0]

    checked = 0
    for size in (1, 2, 3):
        for word in itertools.product(alphabet, repeat=size):
            require(probability(word) == lifted_probability(word), 'Exact matched symbol block')
            checked += 1
    longer = [(w, probability(w)-lifted_probability(w))
              for w in itertools.product(alphabet, repeat=4)
              if probability(w) != lifted_probability(w)]
    require(bool(longer), 'Example is not accidentally exact at every word length')
    flux = sp.diag(*nu)*R-R.T*sp.diag(*nu)
    require(flux != sp.zeros(9), 'Word dynamics need not preserve reversibility')

    # Exact finite-field equilibrium of the nonreversible physical surrogate.
    z = sp.symbols('z', positive=True)  # z=exp(h)
    Q = sp.zeros(10)
    Q[1:, 1:] = R-sp.eye(9)
    for j, value in enumerate(gamma):
        Q[0, j+1] = nu[j]*z**(1+value)
        Q[j+1, 0] = z**(value-1)
        Q[j+1, j+1] -= Q[j+1, 0]
    Q[0, 0] = -sum(Q[0, j] for j in range(1, 10))
    equilibrium = sp.Matrix([[1]+[z*z*v for v in nu]])/(1+z*z)
    require(all(sp.cancel(x) == 0 for x in equilibrium*Q), 'Exact field equilibrium')
    require(Q*sp.ones(10, 1) == sp.zeros(10, 1), 'Full generator row sums')
    readout = sp.Matrix([-1]+[1]*9)
    require(Q.subs(z, 1)*readout == -2*readout, 'Passive telegraph readout eigenrelation')
    return {
        'hidden_target_states': 4, 'word_length': 2, 'word_states': 9,
        'total_surrogate_states': 10, 'matched_blocks_exact': checked,
        'first_longer_word_witness': list(longer[0][0]),
        'longer_word_probability_difference_exact': str(longer[0][1]),
        'quantization_variance_loss_exact': str(loss),
        'stationarity_and_field_equilibrium_exact': True,
        'surrogate_is_nonreversible': True,
        'scope': 'Exact finite-block and physical-realization identities, not a universal approximation proof.',
    }


def numeric_generator(K, mu, g, h):
    n = len(g)
    Q = np.zeros((n+1, n+1))
    Q[1:, 1:] = K
    Q[0, 1:] = mu*np.exp((1+g)*h)
    Q[1:, 0] = np.exp((g-1)*h)
    Q[0, 0] = -np.sum(Q[0, 1:])
    Q[np.arange(1, n+1), np.arange(1, n+1)] -= Q[1:, 0]
    return Q


def regularization_checks() -> dict:
    bit = np.array([[-.5, .5], [.5, -.5]])
    K = math.log(2)*np.kron(bit, np.eye(2))+math.log(3)*np.kron(np.eye(2), bit)
    mu = np.ones(4)/4
    g = np.array([-1., 0., 0., 1.])
    p0 = np.r_[.5, mu/2]
    S = np.r_[-1., np.ones(4)]
    protocols = [[(.08, .5), (-.04, .4), (.08, .6)],
                 [(-.08, .4), (.08, .6), (0., .5)],
                 [(.04, 1.5)]]
    H, T = .08, 1.5
    R = math.exp(2*H)
    B = 2*(R-1)
    norm_ratios, mean_ratios, mean_errors = [], [], []
    for delta in (.001, .01, .1):
        P = expm(delta*K)
        approximate = (P-np.eye(4))/delta
        require(np.min(P) > 0 and np.max(np.abs(P.sum(axis=1)-1)) < 2e-14,
                'Sampled stochastic internal transition')
        require(np.max(-np.diag(approximate)) <= 1/delta, 'Bounded clock outgoing rate')
        for t in (.0005, .005, .05, .5, 2.):
            error = np.linalg.norm(expm(K*t)-expm(approximate*t), 2)
            certificate = min(1., 2*delta/t)
            require(error <= certificate+2e-14, 'Sampled spectral semigroup bound')
            norm_ratios.append(error/certificate)
        J = 2*delta*(1+math.log(T/(2*delta)))
        certificate = B*math.exp(2*B*T)*J
        for protocol in protocols:
            p, q = p0.copy(), p0.copy()
            for h, duration in protocol:
                p = p@expm(numeric_generator(K, mu, g, h)*duration)
                q = q@expm(numeric_generator(approximate, mu, g, h)*duration)
            error = abs((p-q)@S)
            require(error <= certificate+2e-14, 'Sampled driven-mean certificate')
            mean_errors.append(error)
            mean_ratios.append(error/certificate)
    # Scalar eigenvalue checks also cover many rates far above the clock cap.
    scalar_cases = 0
    for x in (1e-6, .01, .5, 1., 10., 1e6):
        regularized = -math.expm1(-x)
        for t in (1e-4, .1, 1., 10., 1e4):
            gap = math.exp(-regularized*t)-math.exp(-x*t)
            require(-1e-15 <= gap <= min(1., 2/t)+1e-15, 'Scalar all-rate bound sample')
            scalar_cases += 1
    return {
        'normalization': 'k=G=1', 'scalar_spectral_cases': scalar_cases,
        'matrix_semigroup_cases': len(norm_ratios), 'protocol_cases': len(mean_ratios),
        'maximum_semigroup_error_over_certificate': max(norm_ratios),
        'maximum_mean_error_over_certificate': max(mean_ratios),
        'maximum_mean_error': max(mean_errors), 'largest_matrix_dimension': 5,
        'scope': 'Deterministic consistency samples; all-rate and all-protocol guarantees are proved analytically.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/general_compression.json'))
    args = parser.parse_args()
    report = {
        'status': 'PASS',
        'scope': 'Exact canonical word realization and deterministic checks of internal-rate regularization.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'numpy': np.__version__, 'scipy': scipy.__version__},
        'canonical_word_realization': exact_word_construction(),
        'regularization': regularization_checks(),
        'largest_matrix_dimension': 10,
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
