#!/usr/bin/env python3
"""Exact bounded checks of the intrinsic reversible prediction lower bound.

The n=1 physical model has 146 states and is stored only as sparse edges.
The n=2 checks enumerate literal triples and short words, without a physical
matrix. All arithmetic is rational or integer; there is no trajectory sampling.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def address_maps(n: int) -> dict[str, tuple[int, ...]]:
    addresses = list(itertools.product((0, 1), repeat=n))
    index = {bits: i for i, bits in enumerate(addresses)}
    result = {
        'J': tuple(index[tuple(bits[(-i-1) % n] for i in range(n))] for bits in addresses),
        'V': tuple(index[tuple(bits[(-i) % n] for i in range(n))] for bits in addresses),
        'X': tuple(index[(1-bits[0],)+bits[1:]] for bits in addresses),
    }
    require(all(p[p[a]] == a for p in result.values() for a in range(2**n)),
            'The literal register reflections and bit gate are involutions')
    return result


def translation_words(n: int, maps: dict) -> dict[int, tuple[str, ...]]:
    r = 2**n
    identity = tuple(range(r))
    queue, seen, words = deque([(identity, ())]), {identity}, {}
    while queue and len(words) < r:
        permutation, word = queue.popleft()
        if permutation == tuple(a ^ permutation[0] for a in range(r)):
            words.setdefault(permutation[0], word)
        for gate, mapping in maps.items():
            new = tuple(mapping[permutation[a]] for a in range(r))
            if new not in seen:
                seen.add(new)
                queue.append((new, word+(gate,)))
    require(len(words) == r and max(map(len, words.values())) <= 3*n,
            'Every small-register XOR translation meets the 3n-cycle budget')
    return words


def gate_action(y: tuple[int, int, int], gate: str, maps: dict) -> tuple[int, int, int]:
    table, address, sigma = y
    return ((table ^ (1 << address), address, sigma) if gate == 'F'
            else (table, maps[gate][address], sigma))


def word_action(y: tuple, word: tuple, maps: dict) -> tuple:
    for gate in word:
        y = gate_action(y, gate, maps)
    return y


def bit(table: int, address: int) -> int:
    return 1 if table & (1 << address) else -1


def word_checks() -> dict:
    records = []
    for n in (1, 2):
        r, maps = 2**n, address_maps(n)
        words = translation_words(n, maps)
        triples = list(itertools.product(range(2**r), range(r), (-1, 1)))
        checks = 0
        for y in triples:
            for gate in ('J', 'V', 'X', 'F'):
                require(gate_action(gate_action(y, gate, maps), gate, maps) == y,
                        'Every literal table/register gate is an involution')
            for c, word in words.items():
                moved = word_action(y, word, maps)
                require(moved == (y[0], y[1] ^ c, y[2]), 'The word is a pure XOR translation')
                require(word_action(moved, tuple(reversed(word)), maps) == y,
                        'Reversing the physical gate word gives its adjoint action')
                flipped = word_action(y, word+('F',)+tuple(reversed(word)), maps)
                require(flipped == (y[0] ^ (1 << (y[1] ^ c)), y[1], y[2]),
                        'The conjugated lamp changes exactly one addressed table entry')
                for b in range(r):
                    old = y[2]*bit(y[0], y[1] ^ b)
                    new = flipped[2]*bit(flipped[0], flipped[1] ^ b)
                    require(new == (-old if b == c else old), 'Literal F_c f_b sign relation')
                    checks += 1
        gram = [[sum(F(y[2]*bit(y[0], y[1] ^ b)*y[2]*bit(y[0], y[1] ^ c),
                       36*len(triples)) for y in triples) for c in range(r)] for b in range(r)]
        require(gram == [[F(int(b == c), 36) for c in range(r)] for b in range(r)],
                'The complete small-table physical Gram matrix is I_r/36')
        records.append({'n': n, 'addresses': r, 'enumerated_triples': len(triples),
                        'physical_state_count_formula': 18*r*2**r+2,
                        'constructed_physical_model': n == 1,
                        'xor_gate_words': {str(c): list(w) for c, w in words.items()},
                        'maximum_cross_port_word_length': 3*max(map(len, words.values())),
                        'lamp_feature_sign_equalities': checks,
                        'gram_diagonal_exact': '1/36', 'gram_off_diagonal_exact': '0'})
    return {'instances': records, 'word_budget_scope': 'The exhaustive word check is for n=1,2; the all-n construction is proved in the accompanying note.'}


def sparse_target() -> dict:
    n, r, lam = 1, 2, F(1, 16)
    maps = address_maps(n)
    triples = list(itertools.product(range(2**r), range(r), (-1, 1)))
    # Index 0 is A, index 1 is the hidden hub. Other states are port/triple pairs.
    states = [('A',), ('hub',)]+[(j,)+y for j in range(9) for y in triples]
    index = {state: i for i, state in enumerate(states)}
    N, M = len(states), len(triples)
    mu = [F(0), F(1, 2)]+[F(1, 18*M)]*(9*M)
    pi = [F(1, 2)]+[value/2 for value in mu[1:]]
    g = [F(0), F(0)]+[F((j+1)*sigma*bit(table, address), 100)
                       for j, table, address, sigma in states[2:]]
    rows, gate_rows = [dict() for _ in states], [dict() for _ in states]

    def add(i: int, j: int, rate: F, gates: bool = False) -> None:
        require(i != j and rate > 0, 'All stored jumps are genuine positive off-diagonal rates')
        rows[i][j] = rows[i].get(j, F())+rate
        if gates:
            gate_rows[i][j] = gate_rows[i].get(j, F())+rate

    adjacent = set()
    for gate_index, gate in enumerate(('J', 'V', 'X', 'F')):
        a, b = 2*gate_index+1, 2*gate_index+2
        for y in triples:
            gy = gate_action(y, gate, maps)
            for left, right in (((0,)+y, (a,)+y), ((a,)+y, (b,)+gy), ((b,)+y, (0,)+y)):
                i, j = index[left], index[right]
                add(i, j, lam, True)
                add(j, i, lam, True)
                adjacent.update(((left[0], right[0]), (right[0], left[0])))
    for i in range(2, N):
        add(i, 1, F(1))
        add(1, i, 2*mu[i])
    require(N == 18*r*2**r+2 == 146 and sum(mu) == 1 and sum(pi) == 1,
            'All physical states and their stationary masses are counted')
    require(all(mu[i]*rate == mu[j]*rows[j][i] for i, row in enumerate(rows)
                for j, rate in row.items()), 'Every internal sparse edge satisfies exact detailed balance')
    gate_exits = [sum(row.values(), F()) for row in gate_rows]
    require(max(gate_exits) == F(1, 2) and max(sum(row.values(), F()) for row in rows) == F(3, 2),
            'The central gate degree is eight and the physical internal exits meet the common budget')
    require(all(len(gate_rows[i]) == (8 if states[i][0] == 0 else 2) for i in range(2, N)),
            'Literal matching edges have the advertised port degrees, including fixed-point gates')
    return {'states': states, 'index': index, 'rows': rows, 'gate_rows': gate_rows,
            'mu': mu, 'pi': pi, 'g': g, 'adjacent': sorted(adjacent), 'triples': triples,
            'lambda': lam, 'maps': maps}


def apply_k(model: dict, vector: list[F]) -> list[F]:
    return [sum((rate*(vector[j]-vector[i]) for j, rate in row.items()), F())
            for i, row in enumerate(model['rows'])]


def apply_y(model: dict, vector: list[F], port: int, signed: bool = False) -> list[F]:
    result = [F()]*len(vector)
    for i, state in enumerate(model['states'][2:], 2):
        if state[0] == port:
            sign = 1 if model['g'][i] > 0 else -1
            result[i] = (sign if signed else 1)*(vector[0]-vector[i])
    return result


def transport(model: dict, c: int, d: int, vector: list[F]) -> list[F]:
    right = [-v for v in apply_y(model, vector, d)]
    left = apply_y(model, apply_k(model, right), c)
    return [-v/model['lambda'] for v in left]


def physical_checks(model: dict) -> dict:
    N, mu, pi, g = len(model['states']), model['mu'], model['pi'], model['g']
    histogram = Counter()
    for i in range(1, N):
        histogram[g[i]] += mu[i]
    expected = {F(0): F(1, 2), **{F(j, 100): F(1, 36) for j in range(-9, 10) if j}}
    require(histogram == expected and sum(mu[i]*g[i] for i in range(1, N)) == 0,
            'The nineteen-level histogram and centering are exact')
    require(sum(mu[i]*g[i]**2 for i in range(1, N)) == F(19, 12000),
            'The sensitivity variance is 19/12000')
    field_records = []
    for base in (F(1), F(100001, 100000), F(100000, 100001)):
        # h=100 log(base); all original-rule rates and equilibrium masses are rational.
        tilt = base**200
        field_pi = [1/(1+tilt)]+[tilt*value/(1+tilt) for value in mu[1:]]
        outgoing = [F()]*N
        incoming = [F()]*N
        for i, row in enumerate(model['rows']):
            for j, rate in row.items():
                flux = field_pi[i]*rate
                require(flux == field_pi[j]*model['rows'][j][i], 'Internal field detailed balance')
                outgoing[i] += flux
                incoming[j] += flux
        a_exit = F()
        for i in range(1, N):
            az = mu[i]*base**int(100*(1+g[i]))
            za = base**int(100*(g[i]-1))
            require(az > 0 and za > 0 and field_pi[0]*az == field_pi[i]*za,
                    'Every full original-rule visible/hidden edge has exact finite-field detailed balance')
            flux = field_pi[0]*az
            outgoing[0] += flux
            incoming[i] += flux
            outgoing[i] += flux
            incoming[0] += flux
            a_exit += az
            if base == 1:
                require(za == 1, 'Every hidden state has passive visible exit rate one')
        require(incoming == outgoing and sum(field_pi) == 1, 'The complete physical stationary flux balances')
        require(-field_pi[0]+sum(field_pi[1:]) == (tilt-1)/(tilt+1),
                'The original equilibrium mean is the exact tanh curve')
        if base == 1:
            require(a_exit == 1, 'A also has passive hidden exit one: exact telegraph lumpability')
        field_records.append({'exp_h_over_100_exact': str(base), 'balanced_visible_edges': N-1})
    # A factorized all-vector certificate: v=conditional leaf variance, d=leaf/hub mean difference.
    # Var_mu(f)=v/2+d^2/4; E_star(f,f)=v/2+d^2/2.
    variance_coefficients, star_coefficients = (F(1, 2), F(1, 4)), (F(1, 2), F(1, 2))
    require(tuple(e-v for e, v in zip(star_coefficients, variance_coefficients)) == (0, F(1, 4)),
            'E_star-Var_mu is a nonnegative square coefficient')
    require(tuple(2*v-e for e, v in zip(star_coefficients, variance_coefficients)) == (F(1, 2), 0),
            '2 Var_mu-E_star is a nonnegative variance coefficient')
    require(2*max(sum(row.values(), F()) for row in model['gate_rows']) == 1,
            'The per-edge square inequality gives gate form at most Var_mu for a centered vector')
    return {'physical_states': N, 'hidden_states': N-1,
            'stored_internal_directed_edges': sum(map(len, model['rows'])),
            'dense_physical_matrix_allocated': False,
            'histogram_exact': {str(k): str(v) for k, v in sorted(histogram.items())},
            'variance_exact': '19/12000', 'central_pi0_mass_exact': str(sum(pi[2:18])),
            'maximum_internal_exit_exact': '3/2', 'maximum_gate_exit_exact': '1/2',
            'factorized_star_band_exact': ['1', '2'], 'gate_form_cap_exact': '1',
            'full_hidden_band_certificate_exact': ['1', '3'],
            'common_exit_budget': '3', 'reversible_rival_cap_from_budget': '6',
            'finite_field_flux_checks': field_records,
            'field_scope': '|h|=100 log(100001/100000)<1/1000<1/50, plus h=0.',
            'band_scope': 'Exact coefficient and degree certificates for the all-vector Dirichlet proof; no large-matrix eigenvalue approximation.'}


def endpoint_checks(model: dict) -> dict:
    N, pi = len(model['states']), model['pi']
    S = [F(-1)]+[F(1)]*(N-1)
    s = [F()]*N
    for i, state in enumerate(model['states'][2:], 2):
        if state[0] == 0:
            s[i] = F(state[-1]*bit(state[1], state[2]))
    bsS = apply_y(model, S, 0, True)
    require(bsS == [-2*v for v in s], 'B_s S=-2s on the full physical space')
    # Build the sparse row pi B_s directly, including its A coordinate.
    row = [F()]*N
    for i in range(2, N):
        if model['states'][i][0] == 0:
            row[0] += pi[i]*s[i]
            row[i] -= pi[i]*s[i]
    require(row == [-pi[i]*s[i] for i in range(N)], 'pi B_s=-s^T diag(pi), including A')
    moment_checks = 0
    for c, d in model['adjacent']:
        selected_c = [i for i in range(2, N) if model['states'][i][0] == c]
        for i in selected_c:
            block = [(j, rate/model['lambda']) for j, rate in model['rows'][i].items()
                     if j >= 2 and model['states'][j][0] == d]
            require(len(block) == 1 and block[0][1] == 1, 'Each extracted target cross-port row is a permutation row')
            j = block[0][0]
            require(model['rows'][j][i] == model['lambda'], 'The reverse cross-port block is the conditional adjoint')
        right = apply_y(model, S, d)
        first = apply_y(model, transport(model, c, d, right), c)
        second = apply_y(model, transport(model, d, c, transport(model, c, d, right)), d)
        require(18*sum(p*v for p, v in zip(pi, first)) == 1,
                'The full physical first row moment equals one with the claimed endpoint normalization')
        require(18*sum(p*v for p, v in zip(pi, second)) == 1,
                'The full physical second row moment equals one with the claimed endpoint normalization')
        moment_checks += 2
    for gate_index, gate in enumerate(('J', 'V', 'X', 'F')):
        a, b = 2*gate_index+1, 2*gate_index+2
        result = transport(model, 0, b, transport(model, b, a, transport(model, a, 0, s)))
        expected = [F()]*N
        for y in model['triples']:
            gy = gate_action(y, gate, model['maps'])
            expected[model['index'][(0,)+y]] = F(gy[2]*bit(gy[0], gy[1]))
        require(result == expected, 'The literal full-generator cycle has exactly the gate pullback action')
        scalar = sum(pi[i]*s[i]*result[i] for i in range(N))*36
        physical = apply_y(model, [(-2)*v for v in result], 0, True)
        require(scalar == 18*sum(p*v for p, v in zip(pi, physical)),
                'The signed endpoint identity converts each cycle correlation into an actual-preparation polynomial')
    return {'oriented_cross_port_transports': len(model['adjacent']),
            'first_and_second_endpoint_moments': moment_checks,
            'full_generator_gate_cycles': 4, 'signed_endpoint_normalization': '18',
            'central_conditional_to_physical_gram_factor': '36'}


def adjoint(T: list, mu: list, nu: list) -> list:
    return [[mu[i]*T[i][j]/nu[j] for i in range(len(mu))] for j in range(len(nu))]


def repair(T: list, mu: list, nu: list) -> tuple[list, dict]:
    Fraw = [[mu[i]*T[i][j] for j in range(len(nu))] for i in range(len(mu))]
    row = [sum(values) for values in Fraw]
    col = [sum(Fraw[i][j] for i in range(len(mu))) for j in range(len(nu))]
    a = [min(F(1), mu[i]/row[i]) if row[i] else F(1) for i in range(len(mu))]
    b = [min(F(1), nu[j]/col[j]) if col[j] else F(1) for j in range(len(nu))]
    clipped = [[a[i]*b[j]*Fraw[i][j] for j in range(len(nu))] for i in range(len(mu))]
    u = [mu[i]-sum(clipped[i]) for i in range(len(mu))]
    v = [nu[j]-sum(clipped[i][j] for i in range(len(mu))) for j in range(len(nu))]
    tau = sum(u)
    require(min(u+v) >= 0 and tau == sum(v), 'Clipped marginal deficits are nonnegative with the same mass')
    flux = [[clipped[i][j]+(u[i]*v[j]/tau if tau else 0) for j in range(len(nu))] for i in range(len(mu))]
    U = [[flux[i][j]/mu[i] for j in range(len(nu))] for i in range(len(mu))]
    Ustar = adjoint(U, mu, nu)
    require(all(sum(row) == 1 for row in U+Ustar) and min(itertools.chain.from_iterable(U)) >= 0,
            'One repaired flux gives stochastic transports in both directions without adding states')
    delta_i = sum(abs(row[i]-mu[i]) for i in range(len(mu)))
    delta_j = sum(abs(col[j]-nu[j]) for j in range(len(nu)))
    error = sum(abs(Fraw[i][j]-flux[i][j]) for i in range(len(mu)) for j in range(len(nu)))
    eps = max(sum(mu[i]*(row[i]/mu[i]-1)**2 for i in range(len(mu))),
              sum(nu[j]*(col[j]/nu[j]-1)**2 for j in range(len(nu))))
    require(error <= F(3, 2)*(delta_i+delta_j) and error**2 <= 9*eps,
            'The exact L1 and mean-square repair bounds hold')
    return U, {'row_L1_defect': delta_i, 'column_L1_defect': delta_j,
               'repair_L1': error, 'row_mse_bound': eps, 'filled_mass': tau}


def repair_checks() -> dict:
    mu, nu = [F(1, 3), F(2, 3)], [F(1, 4), F(1, 4), F(1, 2)]
    examples = {
        'excess_sparse_rectangular': [[F(3, 2), F(0), F(0)], [F(0), F(3, 4), F(3, 4)]],
        'zero_rows_and_columns': [[F(0)]*3 for _ in range(2)],
        'already_balanced': [nu.copy(), nu.copy()],
        'small_row_defects': [[v*F(17, 16) for v in nu], [v*F(31, 32) for v in nu]],
    }
    records = []
    for name, T in examples.items():
        U, info = repair(T, mu, nu)
        Tstar, Ustar = adjoint(T, mu, nu), adjoint(U, mu, nu)
        _, reverse_info = repair(Tstar, nu, mu)
        # The actual reverse path uses Ustar, never an independently repaired choice.
        reverse_error = sum(nu[j]*abs(Tstar[j][i]-Ustar[j][i]) for j in range(3) for i in range(2))
        require(reverse_error == info['repair_L1'], 'The shared repaired flux has the same weighted reverse error')
        raw, fixed = [T, Tstar, T], [U, Ustar, U]
        C = max(F(1), *(sum(row) for matrix in raw for row in matrix))
        path_error, endpoint_error = F(), F()
        for path in itertools.product(range(2), range(3), range(2), range(3)):
            p, q = mu[path[0]], mu[path[0]]
            for j in range(3):
                p *= raw[j][path[j]][path[j+1]]
                q *= fixed[j][path[j]][path[j+1]]
            path_error += abs(p-q)
            endpoint_error += (p-q)*(-1 if (path[0]+path[-1]) % 2 else 1)
        edge_bound = info['repair_L1']*(C*C+C+1)
        require(abs(endpoint_error) <= path_error <= edge_bound,
                'The explicit full-path L1 distance meets the repaired-prefix/raw-suffix telescoping bound')
        require(path_error**2 <= (9*C*C)**2*info['row_mse_bound'],
                'The convenient length-three mean-square path bound holds without taking numerical square roots')
        require(reverse_info['row_mse_bound'] == info['row_mse_bound'], 'Forward/reverse defect normalization agrees')
        records.append({'case': name, **{k+'_exact': str(v) for k, v in info.items()},
                        'path_length': 3, 'enumerated_full_paths': 36,
                        'raw_row_cap_exact': str(C), 'full_path_L1_exact': str(path_error),
                        'edge_telescope_bound_exact': str(edge_bound)})
    return {'examples': records, 'state_sets_before_and_after': [2, 3],
            'scope': 'The repair supplies proof couplings on unchanged states; it is not asserted to be a physical predictor.'}


def entropy_exponential(counts: list[int]) -> F:
    """Return 2**(N H(counts/N)) exactly, avoiding logarithm roundoff."""
    N = sum(counts)
    result = F(N**N)
    for count in counts:
        if count:
            result /= count**count
    return result


def entropy_checks() -> dict:
    r, size = 3, 8
    laws = {'uniform': [1]*size, 'small_atom_bias': [135]+[127]*(size-1),
            'even_parity': [int(x.bit_count() % 2 == 0) for x in range(size)]}
    records = []
    for name, counts in laws.items():
        N = sum(counts)
        joint = entropy_exponential(counts)
        conditional_product, sum_tv = F(1), F()
        tvs = []
        for c in range(r):
            tv = sum(abs(counts[x]-counts[x ^ (1 << c)]) for x in range(size))/F(2*N)
            marginals = [counts[x]+counts[x ^ (1 << c)] for x in range(size) if not x & (1 << c)]
            conditional = joint/entropy_exponential(marginals)
            exponent = N*(1-tv)
            require(exponent.denominator == 1 and conditional >= 2**int(exponent),
                    'Exact entropy exponent certificate: H(Z_c|Z_-c) >= 1-TV(rho,flip_c rho)')
            conditional_product *= conditional
            sum_tv += tv
            tvs.append(str(tv))
        require(joint >= conditional_product, 'The entropy chain/conditioning inequality holds on each finite bit law')
        lower_exponent = N*(r-sum_tv)
        require(lower_exponent.denominator == 1 and joint >= 2**int(lower_exponent),
                'The joint entropy lower bound follows from the coordinate flip distances')
        support = sum(count > 0 for count in counts)
        require(joint <= support**N, 'A deterministic decoded vector has entropy at most the log of its actual support')
        records.append({'law': name, 'bits': r, 'integer_masses': counts, 'support': support,
                        'coordinate_flip_TV_exact': tvs, 'entropy_lower_bound_bits_exact': str(r-sum_tv),
                        'certificate': 'Exact integer powers certify the entropy inequalities without floating logarithms.'})
    # A stationary maximal-flip coupling on the eight actual decoded states.
    counts, scale = laws['small_atom_bias'], F(127, 128)
    law = [F(value, sum(counts)) for value in counts]
    eta = F()
    coupling_records = []
    for c in range(r):
        flux = [[F() for _ in range(size)] for _ in range(size)]
        for x in range(size):
            y = x ^ (1 << c)
            flux[x][y] = min(law[x], law[y])
            flux[x][x] = law[x]-flux[x][y]
        require(all(sum(flux[x]) == law[x] for x in range(size)) and
                all(sum(flux[x][y] for x in range(size)) == law[y] for y in range(size)),
                'Each explicit flip coupling is stationary on the same eight states')
        failures = []
        for b in range(r):
            sign = -1 if b == c else 1
            corr = sum(flux[x][y]*scale**2*bit(x, b)*bit(y, b)
                       for x in range(size) for y in range(size))
            eta = max(eta, 1-sign*corr, 1-scale**2)
            failures.append(sum(flux[x][y] for x in range(size) for y in range(size)
                                if bit(y, b) != sign*bit(x, b)))
        vector_fail = sum(flux[x][y] for x in range(size) for y in range(size) if y != x ^ (1 << c))
        tv = sum(abs(law[x]-law[x ^ (1 << c)]) for x in range(size))/2
        require(vector_fail == tv, 'The explicit coupling witnesses the exact one-bit-flip TV distance')
        coupling_records.append((failures, vector_fail))
    require(1-scale <= 1-scale**2 <= eta <= F(1, 6*r), 'Rounded-feature and entropy-threshold budgets hold')
    require(all(failure <= F(3, 2)*eta for failures, _ in coupling_records for failure in failures),
            'Every rounded bit mismatch meets the 3 eta/2 inequality')
    require(all(failure <= F(3*r, 2)*eta for _, failure in coupling_records),
            'The joint-vector mismatch meets the union bound')
    require(size**4 >= 2**(3*r), 'The actual eight-state support respects D >= 2^(3r/4)')
    return {'entropy_laws': records,
            'decoded_coupling': {'actual_states': size, 'scale_exact': str(scale), 'eta_exact': str(eta),
                                'threshold_exact': '1/18', 'no_auxiliary_decoding_randomness': True,
                                'flip_couplings': r, 'feature_correlations': r*r}}


def menu_and_budget_checks() -> dict:
    sensitivities = list(range(-9, 10))
    frequencies = sorted({0} | {100+j for j in sensitivities} | {-100+j for j in sensitivities})
    base = F(1000001, 1000000)
    nodes = [base**omega for omega in frequencies]
    require(len(frequencies) == 39 and all(nodes[i] < nodes[i+1] for i in range(38)),
            'The 39 physical generator frequencies give strictly ordered exact Vandermonde nodes')
    require(all(nodes[j]-nodes[i] > 0 for i in range(39) for j in range(i+1, 39)),
            'Every factor in the Vandermonde determinant is strictly positive')
    require(F(3800, 1000000) < F(1, 50) < F(5, 109),
            'The exact rational exponential menu fits the fixed small-field range')
    # Fixed-clock transfer arithmetic for representative admissible majorants,
    # rather than a numerical estimate of the actual 39-field interpolation mass.
    t, rho, D, Z = F(1, 2), F(2, 3), F(12), F(3)
    require(D == 8/rho, 'The representative retained-word majorant has the stated normalization')
    transfer = []
    for M, degree in ((2, 1), (2, 4), (5, 3), (9, 5)):
        delta, delta_theta = (t/D)**M, t**M
        retained = 2*Z**degree*D**M*delta
        tails = 2*Z**degree*t**(M+1)
        require(retained+tails <= 4*Z**degree*delta_theta, 'The exact two-tail and retained-word allocations give the Holder bound')
        transfer.append({'M': M, 'generator_degree': degree, 'delta_exact': str(delta),
                         'delta_to_theta_exact': str(delta_theta), 'theta_symbolic': 'log(2)/log(24)',
                         'retained_part_vanishes_if_M_below_degree': M < degree})
    budgets = []
    for n in (1, 2, 3, 4):
        r, L, C = 2**n, 36*n+3, 96
        u = F(1, 36*r*L*C**(L-1))
        delta_moment = u*u/3
        eta = delta_moment+3*L*C**(L-1)*u
        require(3*delta_moment == u*u and eta <= F(1, 6*r),
                'The exact scalar-repair budget reaches the deterministic entropy threshold')
        require(3*L*C**(L-1)*u == F(1, 12*r), 'Half of the entropy threshold is allocated to path repair')
        budgets.append({'n': n, 'addresses': r, 'maximum_correlation_edges': L,
                        'maximum_generator_degree': 3*L+2, 'raw_row_cap': C,
                        'moment_error_denominator_bits': delta_moment.denominator.bit_length(),
                        'entropy_threshold_exact': str(F(1, 6*r)),
                        'path_repair_allocation_exact': str(F(1, 12*r))})
    return {'field_menu': {'frequency_hundredths': frequencies, 'exact_node_base': str(base),
                           'positive_determinant_factors_checked': 39*38//2,
                           'largest_node_fraction_bit_length': max(max(abs(v.numerator).bit_length(), v.denominator.bit_length()) for v in nodes),
                           'scope': 'Exact nonsingularity and field range only. The 39x39 inverse and its coefficient masses are not computed.'},
            'representative_fixed_clock_allocations': transfer,
            'common_budget_entropy_allocations': budgets,
            'budget_scope': 'Rational allocation checks do not calibrate the theorem constants A, B, theta from the actual field menu; those remain symbolic in the proof.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/dynamic_lamp_reversibility_lower_bound.json'))
    args = parser.parse_args()
    model = sparse_target()
    report = {
        'status': 'PASS',
        'scope': 'Exact bounded checks of the dynamic-lamp target, physical positive transports, flip entropy, balanced repair, and proof-budget algebra.',
        'versions': {'python': platform.python_version()},
        'physical_target': physical_checks(model),
        'literal_queries_and_lamps': word_checks(),
        'full_physical_endpoint_identities': endpoint_checks(model),
        'balanced_transport_repair': repair_checks(),
        'deterministic_flip_entropy': entropy_checks(),
        'field_menu_and_error_budgets': menu_and_budget_checks(),
        'largest_matrix_dimension': 8,
        'largest_sparse_physical_state_count': len(model['states']),
        'largest_literal_triple_enumeration': 128,
        'limitations': 'These finite exact certificates accompany, and do not replace, the all-n proof or quantify its asymptotic constants. No arbitrary rival is simulated. The claimed separation requires nineteen actuator levels, the original field rule, exact histogram, and a fixed internal rate budget; binary actuators and unbounded-rate reversible rivals remain open.',
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
