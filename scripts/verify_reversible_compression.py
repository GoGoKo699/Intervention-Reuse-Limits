#!/usr/bin/env python3
"""Small exact checks of reversible general-actuator compression.

Prediction-profile aggregation and two-point moment restoration are checked
with rational arithmetic. A few deterministic driven master equations check
the realized models; these samples do not establish the theorem's uniform
scope or its asymptotic state count.
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


def scalar_moment(mu: sp.Matrix, g: sp.Matrix, order: int) -> sp.Expr:
    return (mu*g.applyfunc(lambda x: x**order))[0]


def bit_transition(rate: sp.Rational) -> sp.Matrix:
    return sp.Matrix([[(1+rate)/2, (1-rate)/2], [(1-rate)/2, (1+rate)/2]])


def word_probability(P: sp.Matrix, mu: sp.Matrix, labels: list[int], word: tuple[int, ...]) -> sp.Expr:
    row = mu
    for index, symbol in enumerate(word):
        if index:
            row = row*P
        row = row*sp.diag(*[int(value == symbol) for value in labels])
    return (row*sp.ones(P.rows, 1))[0]


def future_prediction(P: sp.Matrix, labels: list[int], word: tuple[int, ...]) -> sp.Matrix:
    prediction = sp.ones(P.rows, 1)
    for symbol in reversed(word):
        prediction = P*sp.diag(*[int(value == symbol) for value in labels])*prediction
    return prediction


def full_generator(K: sp.Matrix, mu: sp.Matrix, g: sp.Matrix, y: sp.Symbol) -> sp.Matrix:
    """Exact field variable y=exp(h/24), suitable for all chosen labels."""
    n = len(g)
    Q = sp.zeros(n+1)
    Q[1:, 1:] = K
    for j in range(n):
        Q[0, j+1] = mu[j]*y**(24*(1+g[j]))
        Q[j+1, 0] = y**(24*(g[j]-1))
        Q[j+1, j+1] -= Q[j+1, 0]
    Q[0, 0] = -sum(Q[0, j] for j in range(1, n+1))
    return Q


def exact_construction() -> tuple[dict, dict]:
    R = sp.Rational
    factors = [bit_transition(R(1, 2)), bit_transition(R(1, 3)), bit_transition(R(1, 4))]
    P = sp.kronecker_product(*factors)
    mu = sp.ones(1, 8)/8
    g = sp.Matrix([-1, -R(3, 4), -R(1, 2), R(1, 4), -R(1, 4), R(1, 2), R(3, 4), 1])
    labels = [-1 if value < 0 else 1 for value in g]
    z = sp.Matrix([R(5, 8)*value for value in labels])
    alphabet = (-1, 1)
    ell, grid_width = 2, R(1, 2)
    words = [word for length in range(1, ell+1) for word in itertools.product(alphabet, repeat=length)]
    predictions = {word: future_prediction(P, labels, word) for word in words}
    require(P == P.T and P*sp.ones(8, 1) == sp.ones(8, 1), 'Original reversible stochastic matrix')
    require(all(value > 0 for value in P), 'Original transition probabilities strictly positive')
    require(scalar_moment(mu, g, 1) == scalar_moment(mu, z, 1) == 0, 'Centered original and quantized actuators')
    W = scalar_moment(mu, g, 2)
    require(W == R(15, 32), 'Original sensitivity variance')
    for symbol in alphabet:
        indices = [i for i, label in enumerate(labels) if label == symbol]
        mean = sum(mu[i]*g[i] for i in indices)/sum(mu[i] for i in indices)
        require(all(z[i] == mean for i in indices), 'Initial quantization is the conditional mean')

    groups: dict[tuple, list[int]] = {}
    for i in range(8):
        signature = (labels[i],)+tuple(sp.floor(predictions[word][i]/grid_width) for word in words)
        groups.setdefault(signature, []).append(i)
    cells = list(groups.values())
    require(cells == [[0], [1, 2, 4], [3, 5, 6], [7]], 'Deterministic nontrivial predictive partition')
    count = len(cells)
    lift = sp.zeros(8, count)
    conditional = sp.zeros(count, 8)
    nu = sp.Matrix([[sum(mu[i] for i in cell) for cell in cells]])
    for c, cell in enumerate(cells):
        for i in cell:
            lift[i, c] = 1
            conditional[c, i] = mu[i]/nu[c]
    E = lift*conditional
    Pbar = conditional*P*lift
    cell_labels = [labels[cell[0]] for cell in cells]
    cell_z = sp.Matrix([z[cell[0]] for cell in cells])
    require(E*E == E and sp.diag(*mu)*E == E.T*sp.diag(*mu), 'Reversible conditional expectation projector')
    require(Pbar*sp.ones(count, 1) == sp.ones(count, 1) and nu*Pbar == nu, 'Cell stochasticity and stationarity')
    require(sp.diag(*nu)*Pbar == Pbar.T*sp.diag(*nu), 'Cell detailed balance')
    require(all(value > 0 for value in Pbar), 'Cell transition probabilities positive')
    require(lift*Pbar*conditional == E*P*E, 'Lifted quotient is E P E')
    for symbol in alphabet:
        D = sp.diag(*[int(value == symbol) for value in labels])
        require(E*D == D*E, 'Prediction partition retains original actuator bins')
    beta = max(abs(value) for prediction in predictions.values() for value in prediction-E*prediction)
    require(beta == R(5, 72) <= grid_width, 'Exact sharper profile projection defect')
    prediction_records = []
    for word in words:
        approximate = lift*future_prediction(Pbar, cell_labels, word)
        error = max(abs(value) for value in predictions[word]-approximate)
        require(error <= len(word)*beta, 'Prediction word telescoping bound')
        prediction_records.append({'word': list(word), 'maximum_prediction_error_exact': str(error),
                                   'certificate_exact': str(len(word)*beta)})
    block_records = []
    nonzero = []
    for length in range(1, ell+2):
        gaps = [(word, word_probability(P, mu, labels, word)-word_probability(Pbar, nu, cell_labels, word))
                for word in itertools.product(alphabet, repeat=length)]
        tv = sum(abs(value) for _, value in gaps)/2
        bound = 0 if length == 1 else R(1, 2)*len(alphabet)**length*(length-1)*beta
        require(tv <= bound, 'Exact stationary word-law total variation bound')
        nonzero.extend((word, value) for word, value in gaps if value != 0)
        block_records.append({'block_length': length, 'total_variation_exact': str(tv),
                              'certificate_exact': str(bound)})
    require(bool(nonzero), 'Predictive quotient is approximate, not accidentally exact')

    # Moment matching uses the original, unquantized actuator within each
    # refined cell, not only the bin average used in the baseline model.
    replicas, moment_records = [], []
    for c, cell in enumerate(cells):
        a, b = (sp.Integer(-1), sp.Integer(0)) if cell_labels[c] == -1 else (sp.Integer(0), sp.Integer(1))
        mean = sum(mu[i]*g[i] for i in cell)/nu[c]
        variance = sum(mu[i]*(g[i]-mean)**2 for i in cell)/nu[c]
        require(variance <= (mean-a)*(b-mean), 'Exact interval conditional variance bound')
        if variance == 0:
            nodes, weights = [mean], [sp.Integer(1)]
        else:
            nodes = [a, mean+variance/(mean-a)]
            denominator = (mean-a)**2+variance
            weights = [variance/denominator, (mean-a)**2/denominator]
        require(sum(weights) == 1 and all(weight > 0 for weight in weights), 'Positive replica weights')
        require(all(a <= node <= b for node in nodes), 'Restored nodes stay in the original bin')
        require(sum(weight*node for weight, node in zip(weights, nodes)) == mean, 'Exact cell mean restoration')
        require(sum(weight*(node-mean)**2 for weight, node in zip(weights, nodes)) == variance,
                'Exact cell variance restoration')
        for node, weight in zip(nodes, weights):
            replicas.append((c, node, weight))
        moment_records.append({'cell_indices': cell, 'bin': [str(a), str(b)],
                               'conditional_mean': str(mean), 'conditional_variance': str(variance),
                               'replica_nodes': [str(node) for node in nodes],
                               'replica_conditional_weights': [str(weight) for weight in weights]})
    nrep = len(replicas)
    replica_mu = sp.Matrix([[nu[c]*weight for c, _, weight in replicas]])
    gamma = sp.Matrix([node for _, node, _ in replicas])
    replica_z = sp.Matrix([cell_z[c] for c, _, _ in replicas])
    Prep = sp.Matrix([[Pbar[c, target]*weight for target, _, weight in replicas]
                     for c, _, _ in replicas])
    cell_projection = sp.Matrix([[int(c == target) for target in range(count)] for c, _, _ in replicas])
    require(Prep*sp.ones(nrep, 1) == sp.ones(nrep, 1), 'Replica transition stochasticity')
    require(replica_mu*Prep == replica_mu, 'Replica stationary law')
    require(sp.diag(*replica_mu)*Prep == Prep.T*sp.diag(*replica_mu), 'Replica detailed balance')
    require(all(value > 0 for value in Prep), 'Replica irreducibility by positive transitions')
    require(Prep*cell_projection == cell_projection*Pbar, 'Replica chain strongly lumps onto cell chain')
    require(replica_mu*cell_projection == nu, 'Replica stationary cell masses')
    require(scalar_moment(replica_mu, gamma, 1) == 0 and scalar_moment(replica_mu, gamma, 2) == W,
            'Restored global mean and variance are exact')
    require(max(abs(value) for value in gamma) == 1, 'Original sensitivity bound attained and preserved')
    require(nrep == 6 < 8, 'Example gives genuine physical state reduction after restoration')

    y = sp.symbols('y', positive=True)
    full_models = {
        'regularized_quantized': (P-sp.eye(8), mu, z),
        'cell_baseline': (Pbar-sp.eye(count), nu, cell_z),
        'replica_baseline': (Prep-sp.eye(nrep), replica_mu, replica_z),
        'replica_restored': (Prep-sp.eye(nrep), replica_mu, gamma),
    }
    exact_generators = {}
    for name, (K, law, actuator) in full_models.items():
        Q = full_generator(K, law, actuator, y)
        equilibrium = sp.Matrix([[1]+[y**48*weight for weight in law]])/(1+y**48)
        require((Q*sp.ones(Q.rows, 1)).applyfunc(sp.expand) == sp.zeros(Q.rows, 1), 'Physical generator row sums')
        require((equilibrium*Q).applyfunc(sp.cancel) == sp.zeros(1, Q.rows), 'Exact full-field stationarity')
        require((sp.diag(*equilibrium)*Q-Q.T*sp.diag(*equilibrium)).applyfunc(sp.cancel) == sp.zeros(Q.rows),
                'Exact full-field detailed balance')
        readout = sp.Matrix([-1]+[1]*(Q.rows-1))
        require(Q.subs(y, 1)*readout == -2*readout, 'Exact passive telegraph readout')
        exact_generators[name] = Q
    full_projection = sp.zeros(nrep+1, count+1)
    full_projection[0, 0] = 1
    full_projection[1:, 1:] = cell_projection
    lumping_residual = exact_generators['replica_baseline']*full_projection-full_projection*exact_generators['cell_baseline']
    require(lumping_residual.applyfunc(sp.cancel) == sp.zeros(nrep+1, count+1), 'Physical replica baseline lumps at every field')

    report = {
        'target_hidden_states': 8, 'cell_states': count, 'replica_hidden_states': nrep,
        'target_total_states': 9, 'final_total_states': 7,
        'P_construction': 'Product of reversible bit kernels with eigenvalues 1/2, 1/3, 1/4; P=exp(K) for the stated product generator.',
        'original_actuator': [str(value) for value in g],
        'bin_actuator_values': ['-5/8', '5/8'], 'original_variance_W': str(W),
        'quantized_variance': str(scalar_moment(mu, z, 2)),
        'predictive_profile_length': ell, 'profile_quantization_width': str(grid_width),
        'partition_cells': cells, 'exact_actual_projection_defect': str(beta),
        'prediction_word_checks': prediction_records, 'stationary_block_checks': block_records,
        'nonzero_word_gap_witness': {'word': list(nonzero[0][0]), 'probability_difference': str(nonzero[0][1])},
        'cell_transition': [[str(Pbar[i, j]) for j in range(count)] for i in range(count)],
        'moment_restoration': moment_records,
        'final_stationary_weights': [str(value) for value in replica_mu],
        'final_actuator': [str(value) for value in gamma],
        'exact_restored_mean': '0', 'exact_restored_variance': str(W), 'exact_preserved_G': '1',
        'quotient_and_replica_reversibility': True,
        'field_stationarity_detailed_balance_and_passive_law': True,
        'all_field_replica_baseline_strong_lumpability': True,
        'scope': 'Exact finite-model identities and finite-word certificates; no assertion that this sample uses the theorem worst-case parameter allocation.',
    }
    data = {'P': P, 'mu': mu, 'g': g, 'z': z, 'Pbar': Pbar, 'nu': nu, 'cell_z': cell_z,
            'Prep': Prep, 'replica_mu': replica_mu, 'replica_z': replica_z, 'gamma': gamma}
    return data, report


def numeric_generator(K: np.ndarray, mu: np.ndarray, g: np.ndarray, field: float) -> np.ndarray:
    Q = np.zeros((len(g)+1, len(g)+1))
    Q[1:, 1:] = K
    Q[0, 1:] = mu*np.exp((1+g)*field)
    Q[1:, 0] = np.exp((g-1)*field)
    Q[0, 0] = -np.sum(Q[0, 1:])
    Q[np.arange(1, len(g)+1), np.arange(1, len(g)+1)] -= Q[1:, 0]
    return Q


def protocol_checks(data: dict) -> dict:
    convert = lambda value: np.asarray(value, dtype=float)
    bit = np.array([[-.5, .5], [.5, -.5]])
    eye = np.eye(2)
    original_K = (math.log(2)*np.kron(np.kron(bit, eye), eye)
                  + math.log(3)*np.kron(np.kron(eye, bit), eye)
                  + math.log(4)*np.kron(np.kron(eye, eye), bit))
    P, mu, g, z = (convert(data[key]) for key in ('P', 'mu', 'g', 'z'))
    mu, g, z = mu.ravel(), g.ravel(), z.ravel()
    require(np.max(np.abs(expm(original_K)-P)) < 2e-14, 'Chosen rational skeleton is the exact product exponential')
    Pbar, Prep = convert(data['Pbar']), convert(data['Prep'])
    nu, cell_z = convert(data['nu']).ravel(), convert(data['cell_z']).ravel()
    replica_mu = convert(data['replica_mu']).ravel()
    replica_z, gamma = convert(data['replica_z']).ravel(), convert(data['gamma']).ravel()
    models = {
        'original': (original_K, mu, g),
        'original_quantized': (original_K, mu, z),
        'regularized_quantized': (P-np.eye(8), mu, z),
        'cell_baseline': (Pbar-np.eye(len(nu)), nu, cell_z),
        'replica_baseline': (Prep-np.eye(len(gamma)), replica_mu, replica_z),
        'replica_restored': (Prep-np.eye(len(gamma)), replica_mu, gamma),
    }
    protocols = [[(.2, .4), (-.15, .5), (.1, .6)],
                 [(-.2, .3), (0., .4), (.2, .8)],
                 [(.12, 1.5)]]
    H, G = .2, 1.
    R = math.exp((1+G)*H)
    quantization_bound = 2*H*R**2*np.max(np.abs(g-z))
    restoration_bound = 2*H*R**2*np.max(np.abs(gamma-replica_z))
    records = []
    maximum_lumping_error = 0.
    maximum_original_final_error = 0.
    for protocol in protocols:
        states = {name: np.r_[.5, law/2] for name, (_, law, _) in models.items()}
        time = 0.
        checkpoints = []
        for field, duration in protocol:
            time += duration
            for name, (K, law, actuator) in models.items():
                states[name] = states[name]@expm(numeric_generator(K, law, actuator, field)*duration)
                require(abs(np.sum(states[name])-1) < 3e-14 and np.min(states[name]) >= -3e-14,
                        'Deterministic master probabilities normalized and nonnegative')
            means = {name: float(1-2*state[0]) for name, state in states.items()}
            lumping_error = abs(means['cell_baseline']-means['replica_baseline'])
            quantization_error = abs(means['original']-means['original_quantized'])
            restoration_error = abs(means['replica_baseline']-means['replica_restored'])
            require(lumping_error < 3e-14, 'Numerical baseline and lifted baseline agree')
            require(quantization_error <= quantization_bound+3e-14, 'Sampled uniform quantization bound')
            require(restoration_error <= restoration_bound+3e-14, 'Sampled uniform restoration bound')
            maximum_lumping_error = max(maximum_lumping_error, lumping_error)
            maximum_original_final_error = max(maximum_original_final_error,
                                               abs(means['original']-means['replica_restored']))
            checkpoints.append({'time': time, 'means': means})
        records.append({'protocol_field_duration': protocol, 'checkpoints': checkpoints})
    return {
        'k': 1, 'G': G, 'maximum_protocol_amplitude_H': H,
        'selected_protocols': records,
        'quantization_uniform_mean_certificate': float(quantization_bound),
        'restoration_uniform_mean_certificate': float(restoration_bound),
        'maximum_baseline_lifting_error': maximum_lumping_error,
        'maximum_original_to_restored_mean_error': maximum_original_final_error,
        'largest_master_matrix_dimension': 9,
        'scope': 'Deterministic selected protocols and checkpoint comparisons. The uniform theorem and its complete approximation budget are analytic, not established by these numerical samples.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/reversible_compression.json'))
    args = parser.parse_args()
    data, exact = exact_construction()
    report = {
        'status': 'PASS',
        'scope': 'Exact reversible prediction-profile quotient, exact cell moment restoration, and small deterministic physical-model comparisons.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'numpy': np.__version__, 'scipy': scipy.__version__},
        'exact_construction': exact, 'selected_driven_means': protocol_checks(data),
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
