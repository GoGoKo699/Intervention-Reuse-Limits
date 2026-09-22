#!/usr/bin/env python3
"""Exact bounded checks of the partition-aggregation state lower bound.

The only complete dictionary matrix uses n=1 and 49 physical states.
Larger n=2 checks enumerate only address permutations and individual table
values. No growing Markov dictionary or trajectory simulation is used.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction as F
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as sp

import verify_bounded_rate_prediction as bounded

reused = bounded.reused
require = reused.require
Q = sp.Rational


def address_gates(n: int) -> list[tuple[int, ...]]:
    addresses = list(itertools.product((0, 1), repeat=n))
    index = {a: i for i, a in enumerate(addresses)}
    reversal = lambda a: a[::-1]
    rotation = lambda a: a[-1:]+a[:-1]
    maps = [reversal, lambda a: rotation(reversal(a)), lambda a: (1-a[0],)+a[1:]]
    result = [tuple(index[fn(a)] for a in addresses) for fn in maps]
    require(all(all(p[p[a]] == a for a in range(2**n)) for p in result),
            'All three address gates are involutions, including small-n fixed points')
    return result


def address_words(n: int) -> dict[int, list[tuple[int, int]]]:
    gates, count = address_gates(n), 2**n
    identity = tuple(range(count))
    queue, seen, found = deque([(identity, [])]), {identity}, {}
    while queue and len(found) < count:
        permutation, sequence = queue.popleft()
        if permutation == tuple(b ^ permutation[0] for b in range(count)):
            found.setdefault(permutation[0], sequence)
        for j, gate in enumerate(gates):
            new = tuple(permutation[gate[a]] for a in range(count))
            if new not in seen:
                seen.add(new)
                queue.append((new, sequence+[j]))
    require(len(found) == count and max(map(len, found.values())) <= 3*n,
            'Every small address is reached within the claimed involution budget')
    words = {}
    for a, sequence in found.items():
        letters = []
        for j in sequence:
            letters.extend([(0, 0)] if j == 0 else [(j, 0), (j, j), (0, j)])
        require(len(letters) <= 9*n, 'Expanded port itinerary meets the partial-isometry budget')
        words[a] = letters
    return words


def build_model(n: int, configurations: list[tuple[int, ...]] | None = None) -> dict:
    require(n <= 2, 'Verifier only constructs bounded model instances')
    r, gates = 2**n, address_gates(n)
    if configurations is None:
        require(n == 1, 'Only n=1 may enumerate the complete configuration dictionary')
        configurations = list(itertools.product((-1, 1), repeat=r))
    states = [(x, a, j, sigma) for x in configurations for a in range(r)
              for j in range(3) for sigma in (-1, 1)]
    index, N = {z: i for i, z in enumerate(states)}, len(states)
    lam, c = Q(1, 8), Q(3, 2)
    matching, port_average = sp.zeros(N), sp.zeros(N)
    for i, (x, a, j, sigma) in enumerate(states):
        matching[i, index[(x, gates[j][a], j, sigma)]] = 1
        for port in range(3):
            port_average[i, index[(x, a, port, sigma)]] = Q(1, 3)
    require(matching == matching.T and matching*matching == sp.eye(N), 'Exact matching involution')
    require(port_average == port_average.T and port_average*port_average == port_average,
            'Port averaging is an orthogonal projection')
    L = lam*(matching-sp.eye(N))+3*lam*(port_average-sp.eye(N))
    mu = sp.ones(1, N)/N
    K = L+c*(sp.ones(N, 1)*mu-sp.eye(N))
    g = [Q(sigma*(j+1)*x[a], 10) for x, a, j, sigma in states]
    levels = sorted(set(g))
    X, Y = {}, {}
    for gamma in levels:
        xmat, ymat = sp.zeros(N+1), sp.zeros(N+1)
        for i, value in enumerate(g):
            if value == gamma:
                xmat[0, i+1] = mu[i]
                xmat[0, 0] -= mu[i]
                ymat[i+1, 0], ymat[i+1, i+1] = 1, -1
        X[gamma], Y[gamma] = xmat, ymat
    Kb = sp.zeros(N+1)
    Kb[1:, 1:] = K
    return {'n': n, 'r': r, 'states': states, 'index': index, 'mu': mu,
            'L': L, 'K': K, 'g': g, 'X_levels': X, 'Y_levels': Y, 'Kb': Kb,
            'lambda': lam, 'c': c, 'matching': matching, 'port_average': port_average}


def physical_checks(model: dict) -> tuple[dict, dict]:
    N, mu, g = len(model['states']), model['mu'], model['g']
    require(N == 48, 'The complete dictionary has exactly 48 hidden states')
    histogram = bounded.histogram(mu, g)
    require(set(histogram.values()) == {Q(1, 6)} and sum(mu[i]*g[i] for i in range(N)) == 0,
            'Exact fixed six-level histogram and centering')
    require(sum(mu[i]*g[i]**2 for i in range(N)) == Q(7, 150), 'Fixed sensitivity variance')
    require(model['K'] == model['K'].T and mu*model['K'] == sp.zeros(1, N),
            'Uniform reversibility and stationarity')
    require(all(model['K'][i, j] > 0 for i in range(N) for j in range(N) if i != j),
            'Global refresh makes all off-diagonal rates positive')
    require(5*model['lambda'] == Q(5, 8) and model['c']+5*model['lambda'] == Q(17, 8),
            'Matching and port projection certificates give the advertised spectral cap')
    X = sum(model['X_levels'].values(), sp.zeros(N+1))
    Y = sum(model['Y_levels'].values(), sp.zeros(N+1))
    Lb = model['Kb']-model['c']*Y*X-model['c']*Y
    expected = sp.zeros(N+1)
    expected[1:, 1:] = model['L']
    require(Lb == expected, 'Full-state local extraction cancels every A-coordinate term')
    S, pi0 = sp.Matrix([-1]+[1]*N), sp.Matrix([[Q(1, 2)]+[value/2 for value in mu]])
    lift = sp.zeros(N+1, 2)
    lift[0, 0] = 1
    for i in range(N):
        lift[i+1, 1] = 1
    records = []
    for base in (Q(1), Q(10001, 10000)):
        # h=10 log(base), so all sensitivity exponentials are rational.
        full = model['Kb'].copy()
        for gamma in model['X_levels']:
            full += base**int(10*(1+gamma))*model['X_levels'][gamma]
            full += base**int(10*(gamma-1))*model['Y_levels'][gamma]
        pi = sp.Matrix([[1]+[base**20*value for value in mu]])/(1+base**20)
        require(full*sp.ones(N+1, 1) == sp.zeros(N+1, 1), 'Physical generator row sums')
        require(pi*full == sp.zeros(1, N+1), 'Physical finite-field stationary law')
        require(sp.diag(*pi)*full == full.T*sp.diag(*pi), 'Physical finite-field detailed balance')
        require((pi*S)[0] == (base**20-1)/(base**20+1), 'Exact equilibrium tanh curve')
        if base == 1:
            require(full*lift == lift*sp.Matrix([[-1, 1], [1, -1]]), 'Exact passive telegraph lumpability')
        records.append({'exp_h_over_ten_exact': str(base), 'physical_states': N+1})
    D = {j: -model['Y_levels'][Q(j+1, 10)]-model['Y_levels'][-Q(j+1, 10)] for j in range(3)}
    Tfull = {}
    for c in range(3):
        for d in range(3):
            Tfull[c, d] = D[c]*Lb*D[d]/model['lambda']+(3*D[c] if c == d else sp.zeros(N+1))
    Yd = model['Y_levels'][Q(1, 10)]-model['Y_levels'][-Q(1, 10)]
    f0 = sp.Matrix([sigma*x[a] if j == 0 else 0 for x, a, j, sigma in model['states']])
    require((-Yd*S/2)[1:, :] == f0 and (-Yd*S/2)[0] == 0, 'Physical initial-feature extraction')
    expected_row = sp.Matrix([[0]+[mu[i]*f0[i]/2 for i in range(N)]])
    require(-pi0*Yd == expected_row, 'Full row endpoint identity, including zero A entry')
    return ({'hidden_states': N, 'physical_states': N+1,
            'histogram_exact': {str(x): str(v) for x, v in histogram.items()},
            'variance_exact': '7/150', 'local_spectral_cap_exact': '5/8',
            'full_nonzero_spectral_interval_exact': ['3/2', '17/8'], 'field_checks': records},
            {'D': D, 'Tfull': Tfull, 'Yd': Yd, 'S': S, 'pi0': pi0, 'f0': f0, 'Lb': Lb})


def gate_truth(model: dict, operators: dict) -> dict:
    N, states = len(model['states']), model['states']
    T = {key: value[1:, 1:] for key, value in operators['Tfull'].items()}
    checks = 0
    for (c, d), matrix in T.items():
        require(matrix.T == T[d, c], 'Partial isometry adjoints exchange the ports')
        projector = sp.diag(*[int(j == d) for _, _, j, _ in states])
        require(matrix.T*matrix == projector, 'Each letter is an isometry on its input port')
        require(all(value in (0, 1) for value in matrix), 'Extracted gate has only permutation incidences')
        checks += 1
    truths, lengths, grams = 0, {}, []
    for n in (1, 2):
        gates, words, r = address_gates(n), address_words(n), 2**n
        lengths[str(n)] = {str(a): len(word) for a, word in words.items()}
        for a, word in words.items():
            # Pullback composition is checked as an address map, without a dictionary matrix.
            mapping, current_port = tuple(range(r)), 0
            for c, d in word:
                require(current_port == d, 'The port itinerary always lies in the isometric domain')
                if c == d:
                    mapping = tuple(mapping[gates[c][b]] for b in range(r))
                current_port = c
            require(current_port == 0 and mapping == tuple(b ^ a for b in range(r)),
                    'Address word is a pure xor translation on every address')
            for x in itertools.product((-1, 1), repeat=r):
                for sigma in (-1, 1):
                    require(sigma*x[mapping[0]] == sigma*x[a], 'Exact table-bit root feature')
                    truths += 1
        gram = sp.zeros(r)
        for x in itertools.product((-1, 1), repeat=r):
            for sigma in (-1, 1):
                for b in range(r):
                    features = sp.Matrix([sigma*x[b ^ a] for a in range(r)])
                    gram += features*features.T/Q(12*r*2**r)
        require(gram == sp.eye(r)/6, 'All-address translated table features have exact Gram I_r/6')
        grams.append({'n': n, 'features': r, 'exact_Gram': 'I_r/6',
                      'configuration_sign_address_samples': 2**r*2*r})
    return {'partial_isometries_checked': checks, 'n_one_two_root_bit_truths': truths,
            'partial_isometry_word_lengths': lengths, 'translated_feature_Gram_checks': grams,
            'scope': 'n=2 uses only four-address maps and individual four-bit truth tables; no 385-state physical matrix.'}


def partition_matrices(model: dict, extra_bit: bool) -> tuple[sp.Matrix, sp.Matrix]:
    keys = [(g, z[0][0]) if extra_bit else (g,) for g, z in zip(model['g'], model['states'])]
    unique = sorted(set(keys))
    B = sp.Matrix([[int(key == cell) for cell in unique] for key in keys])
    counts = [keys.count(cell) for cell in unique]
    C = sp.diag(*[1/sp.Integer(count) for count in counts])*B.T
    require(C*B == sp.eye(len(unique)), 'Conditional averaging and cell lift are reciprocal')
    require(B*C == (B*C).T and B*C*B*C == B*C, 'Uniform conditional expectation is orthogonal')
    return B, C


def aggregation_checks(model: dict, operators: dict) -> dict:
    records, compressions = [], 0
    N, mu, f0 = len(model['states']), model['mu'], operators['f0']
    full_T = operators['Tfull']
    for extra in (False, True):
        B, C = partition_matrices(model, extra)
        d = B.cols
        BF, CF = sp.diag(sp.ones(1), B), sp.diag(sp.ones(1), C)
        nu = mu*B
        pi = sp.Matrix([[Q(1, 2)]+[v/2 for v in nu]])
        S = sp.Matrix([-1]+[1]*d)
        Kb = CF*model['Kb']*BF
        X = sum((CF*m*BF for m in model['X_levels'].values()), sp.zeros(d+1))
        Y = sum((CF*m*BF for m in model['Y_levels'].values()), sp.zeros(d+1))
        Lb = Kb-model['c']*Y*X-model['c']*Y
        require(Lb == CF*operators['Lb']*BF, 'Full local extraction commutes exactly with aggregation')
        Tbar = {}
        for (c, dd), T in full_T.items():
            Dc, Dd = CF*operators['D'][c]*BF, CF*operators['D'][dd]*BF
            polynomial = Dc*Lb*Dd/model['lambda']+(3*Dc if c == dd else sp.zeros(d+1))
            require(polynomial == CF*T*BF, 'Physical gate polynomial evaluates to exact E T E compression')
            Tbar[c, dd] = polynomial
            compressions += 1
        Yd = CF*operators['Yd']*BF
        require(B*C*f0 == f0, 'Initial port-one bit feature is cell measurable')
        for address, word in address_words(1).items():
            f, z = f0.copy(), C*f0
            loss_sum = sp.Integer(0)
            for c, dd in word:
                gate = full_T[c, dd][1:, 1:]
                lifted_before = B*z
                transported = gate*lifted_before
                z_new = C*transported
                residual = transported-B*z_new
                loss = (residual.T*residual)[0]/(2*N)
                before_norm = (z.T*sp.diag(*nu)*z)[0]/2
                after_norm = (z_new.T*sp.diag(*nu)*z_new)[0]/2
                require(loss == before_norm-after_norm, 'Each compressed gate has exact projection norm loss')
                loss_sum += loss
                z, f = z_new, gate*f
            target_norm = (f.T*f)[0]/(2*N)
            aggregate_norm = (z.T*sp.diag(*nu)*z)[0]/2
            require(target_norm == Q(1, 6) and loss_sum == Q(1, 6)-aggregate_norm,
                    'Exact nonnegative palindrome deficit telescopes')
            defect = f-B*C*f
            defect_squared = (defect.T*defect)[0]/(2*N)
            require(defect_squared <= len(word)*loss_sum, 'Transport inequality controls true feature conditional variance')
            value = Yd*S
            for letter in word:
                value = Tbar[letter]*value
            for c, dd in reversed(word):
                value = Tbar[dd, c]*value
            palindrome = (pi*Yd*value)[0]/2
            require(palindrome == aggregate_norm, 'Physical visible-mean palindrome equals aggregate feature norm')
            records.append({'extra_configuration_bit_in_cells': extra, 'hidden_cells': d,
                            'root_address': address, 'letters': len(word),
                            'aggregate_norm_squared_exact': str(aggregate_norm),
                            'palindrome_deficit_exact': str(loss_sum),
                            'feature_projection_loss_exact': str(defect_squared)})
    require(any(Q(r['palindrome_deficit_exact']) > 0 for r in records),
            'A genuinely information-losing partition is exercised')
    return {'cases': records, 'compression_compatible_gate_polynomials_checked': compressions,
            'partitions_allow_root_and_nonroot_states_in_one_cell': True}


def vandermonde_checks() -> dict:
    frequencies = [-13, -12, -11, -9, -8, -7, 0, 7, 8, 9, 11, 12, 13]
    base = F(10001, 10000)
    nodes = [base**omega for omega in frequencies]
    require(len(set(nodes)) == 13, 'Thirteen distinct generator frequencies give distinct rational nodes')
    rows = []
    largest_bits = 0
    for j, node in enumerate(nodes):
        coefficients = [F(1)]
        denominator = F(1)
        for t, other in enumerate(nodes):
            if t == j:
                continue
            updated = [F()]*(len(coefficients)+1)
            for i, value in enumerate(coefficients):
                updated[i] -= other*value
                updated[i+1] += value
            coefficients = updated
            denominator *= node-other
        coefficients = [value/denominator for value in coefficients]
        for k, other in enumerate(nodes):
            value = F()
            for coefficient in reversed(coefficients):
                value = value*other+coefficient
            require(value == int(k == j), 'Exact inverse Vandermonde via Lagrange polynomials')
        largest_bits = max(largest_bits, *(max(abs(v.numerator).bit_length(), v.denominator.bit_length())
                                           for v in coefficients))
        rows.append(sum(abs(value) for value in coefficients))
    # h_i=10i log(base), h_12<120/10000<1/50 and <1/26=1/[20(1+G)].
    require(F(120, 10000) < F(1, 50) < F(1, 26), 'Rational field menu lies inside a fixed small field range')
    return {'frequency_tenths': frequencies, 'exp_h_step_over_ten_exact': str(base),
            'exact_inverse_entries_checked': 13**2,
            'largest_inverse_coefficient_bit_length': largest_bits,
            'maximum_row_mass_numerator_bits': max(abs(v.numerator).bit_length() for v in rows),
            'scope': 'The inverse is exactly verified, not numerically fitted. Large interpolation coefficients are counted in proof constants.'}


def cube_and_budget_checks() -> dict:
    r = 4
    tables = list(itertools.product((-1, 1), repeat=r))
    cases = []
    for known in range(r+1):
        groups = {}
        for x in tables:
            groups.setdefault(x[:known], []).append(x)
        error = F()
        mistakes = F()
        for values in groups.values():
            means = [sum(x[j] for x in values)/F(len(values)) for j in range(r)]
            for x in values:
                error += sum((F(x[j])-means[j])**2 for j in range(r))/len(tables)
                mistakes += sum((1 if means[j] >= 0 else -1) != x[j] for j in range(r))/F(len(tables))
        require(error == r-known and mistakes <= error, 'Conditional-mean cube distortion and thresholding inequality')
        if error <= F(r, 16):
            require(len(groups)**8 >= 2**(5*r), 'Exact small-cube count respects the claimed entropy lower bound')
        cases.append({'revealed_bits': known, 'cells': len(groups), 'summed_squared_error_exact': str(error),
                      'summed_threshold_errors_exact': str(mistakes)})
    # h2(1/16)=1/4+(15/16)log2(16/15)<3/8 iff (16/15)^15<4.
    require(F(16, 15)**15 < 4, 'Exact rational certificate for the binary entropy constant')
    budgets = []
    # This checks bookkeeping for representative admissible side bounds. It
    # does not calibrate the much larger field-interpolation constant above.
    rho, A, B = F(3, 2), 2, 3
    for n in (1, 2, 3, 4):
        epsilon = F(1, 864*n*2**n)
        M = 0
        while rho**(M+1) < 12*B**(2*n+2)/epsilon:
            M += 1
        J = 4**M*A**(n+1)
        delta = epsilon/(2*J**2)
        tail = 6*B**(2*n+2)/rho**(M+1)
        require(tail <= epsilon/2 and delta*J**2 == epsilon/2,
                'Both-model truncation and actual-mean allocations sum to epsilon')
        require(9*n*2**n*epsilon == F(1, 96), 'Total projected feature loss meets the root distortion threshold')
        budgets.append({'n': n, 'epsilon_exact': str(epsilon), 'M': M,
                        'delta_denominator_bit_length': delta.denominator.bit_length(),
                        'propagator_side_mass_bit_length': J.bit_length(),
                        'root_feature_error_budget_exact': '1/96'})
    return {'small_cube_partitions': cases, 'entropy_constant_certificate': '(16/15)^15<4',
            'representative_two_model_transfer_budgets': budgets,
            'transfer_budget_scope': 'Exact allocation algebra for representative A=2,B=3,rho=3/2; the theorem retains the actual menu-dependent constants symbolically.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/aggregation_state_lower_bound.json'))
    args = parser.parse_args()
    model = build_model(1)
    physical, operators = physical_checks(model)
    sources = [Path(__file__).resolve(), Path(bounded.__file__).resolve(), Path(reused.__file__).resolve()]
    report = {'status': 'PASS',
              'scope': 'Exact six-level register gadget, full physical extraction, compression-compatible port partial isometries, visible palindrome norms, conditional-variance transport, small cube distortion, and fixed-clock budget algebra.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                           'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
              'physical_dictionary': physical, 'partial_isometries_and_addresses': gate_truth(model, operators),
              'all_partition_architecture_checks': aggregation_checks(model, operators),
              'physical_field_menu': vandermonde_checks(), 'cube_and_transfer': cube_and_budget_checks(),
              'largest_matrix_dimension': 49,
              'limitations': 'Finite exact checks support the uniform proof; they do not enumerate all partitions or prove asymptotic information inequalities by experiment. The lower bound concerns stationary-flux partitions refining the exact actuator, not every reversible model.',
              'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
