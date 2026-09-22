#!/usr/bin/env python3
"""Focused exact checks of shift-register controlled-response lower bounds.

Only registers of one to three bits are built as physical generators.
Larger registers are handled as sparse Walsh polynomials. Exact leaf and
sum-of-squares identities certify the Gram obstruction; derivative-stencil
tests and rational error budgets do not use numerical rank estimates.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def number(value: sp.Expr) -> mp.mpf:
    return mp.mpf(str(sp.N(value, mp.mp.dps+10)))


def matrix(value: sp.Matrix) -> mp.matrix:
    return mp.matrix([[number(value[i, j]) for j in range(value.cols)] for i in range(value.rows)])


def frobenius(value: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(x)**2 for x in value))


def digits(value: mp.mpf) -> str:
    return mp.nstr(value, 50)


def physical_register(bits: int) -> tuple[dict, dict]:
    states = list(itertools.product((-1, 1), repeat=bits))
    index = {state: i for i, state in enumerate(states)}
    N = len(states)
    L = sp.zeros(N)
    for i, state in enumerate(states):
        for fresh in (-1, 1):
            L[i, index[state[1:]+(fresh,)]] += sp.Rational(1, 2)
    K = sp.Rational(3, 2)*(sp.ones(N)/N-sp.eye(N))+(L+L.T-2*sp.eye(N))/4
    g = sp.Matrix([state[0] for state in states])
    W = sp.Matrix([[sp.prod(state[j] for j in range(bits) if mask & (1 << j))
                    for mask in range(N)] for state in states])
    require(W.T*W == N*sp.eye(N), 'Exact Walsh orthogonality')
    require(L*sp.ones(N, 1) == sp.ones(N, 1) and L.T*sp.ones(N, 1) == sp.ones(N, 1),
            'Left shift and its transpose are stochastic')
    require(K == K.T and K*sp.ones(N, 1) == sp.zeros(N, 1), 'Positive reversible shift-register generator')
    require(all(K[i, j] >= sp.Rational(3, 2*N) for i in range(N) for j in range(N) if i != j),
            'Refresh gives a strict physical off-diagonal floor')
    A = sp.zeros(N-1)
    for mask in range(1, N):
        if not mask & (1 << (bits-1)):
            A[(mask << 1)-1, mask-1] += 1
        if not mask & 1:
            A[(mask >> 1)-1, mask-1] += 1
    transformed = W.T*K*W/N
    require(transformed[1:, 1:] == -2*sp.eye(N-1)+A/4, 'Exact Walsh translation adjacency')
    require(A == A.T and max(sum(abs(A[i, j]) for j in range(N-1)) for i in range(N-1)) <= 2,
            'Centered relaxation rates lie in [3/2,5/2]')
    B = sp.zeros(N-1)
    for mask in range(1, N):
        target = mask ^ 1
        if target:
            B[target-1, mask-1] = 1
    require((W.T*sp.diag(*g)*W/N)[1:, 1:] == B, 'Binary actuator toggles bit one after centering')

    z = sp.Rational(65, 64)
    Qs = []
    transform = sp.diag(sp.Integer(1), W)
    inverse = sp.diag(sp.Integer(1), W.T/N)
    for x in (sp.Integer(1), z):
        Q = sp.zeros(N+1)
        Q[1:, 1:] = K
        for j in range(N):
            Q[0, j+1] = x**(1+g[j])/N
            Q[j+1, 0] = x**(g[j]-1)
            Q[j+1, j+1] -= Q[j+1, 0]
        Q[0, 0] = -sum(Q[0, j] for j in range(1, N+1))
        equilibrium = sp.Matrix([[1]+[x*x/N]*N])/(1+x*x)
        require(equilibrium*Q == sp.zeros(1, N+1), 'Exact full-field equilibrium')
        require(sp.diag(*equilibrium)*Q == Q.T*sp.diag(*equilibrium), 'Exact full-field detailed balance')
        Qs.append(inverse*Q*transform)
    Q0, Qh = Qs
    I = sp.eye(N+1)
    F = Q0*(Q0+2*I)/3
    expected = sp.zeros(N+1)
    expected[2:, 2:] = sp.eye(N-1)-A/3+A*A/48
    require(F == expected, 'Exact centered quadratic filter')
    c, u = (z+1/z)/2, (z-1/z)/2
    Z1 = F*(Qh-Q0-(1-c/z)*I)*F/(-u/z)
    require(Z1[2:, 2:] == F[2:, 2:]*B*F[2:, 2:], 'Exact controlled toggle filter')
    p0 = sp.zeros(1, N+1)
    p0[0], p0[1] = sp.Rational(1, 2), sp.Rational(1, 2)
    S, root = sp.zeros(N+1, 1), sp.zeros(N+1, 1)
    S[0], S[1], root[2] = -1, 1, 1
    require(p0*Qh*F == u*u*(F*root).T, 'Mean-response left Gram endpoint')
    require(F*Qh*S == -2*u*F*root/z, 'Mean-response right Gram endpoint')
    report = {'physical_bits': bits, 'hidden_states': N, 'full_Markov_states': N+1,
              'minimum_internal_off_diagonal': str(min(K[i, j] for i in range(N) for j in range(N) if i != j)),
              'Walsh_shift_and_binary_toggle_identities': True,
              'hidden_relaxation_rate_band': ['3/2', '5/2'],
              'G': '1', 'W': '1', 'field_h': 'log(65/64)',
              'full_field_stationarity_reversibility_and_Gram_filters': True}
    return {'Q0': Q0, 'Qh': Qh, 'z': z}, report


def sparse_add(*terms: tuple[sp.Expr, dict[int, sp.Expr]]) -> dict[int, sp.Expr]:
    result: dict[int, sp.Expr] = {}
    for scale, vector in terms:
        for mask, value in vector.items():
            result[mask] = result.get(mask, 0)+scale*value
    return {mask: value for mask, value in result.items() if value}


def sparse_A(vector: dict[int, sp.Expr], bits: int) -> dict[int, sp.Expr]:
    result: dict[int, sp.Expr] = {}
    for mask, value in vector.items():
        if not mask & (1 << (bits-1)):
            result[mask << 1] = result.get(mask << 1, 0)+value
        if not mask & 1:
            result[mask >> 1] = result.get(mask >> 1, 0)+value
    return {mask: value for mask, value in result.items() if value}


def sparse_B(vector: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    return {mask ^ 1: value for mask, value in vector.items() if mask != 1}


def sparse_F(vector: dict[int, sp.Expr], bits: int) -> dict[int, sp.Expr]:
    first = sparse_A(vector, bits)
    second = sparse_A(first, bits)
    return sparse_add((sp.Integer(1), vector), (-sp.Rational(1, 3), first), (sp.Rational(1, 48), second))


def sparse_dot(first: dict[int, sp.Expr], second: dict[int, sp.Expr]) -> sp.Expr:
    return sum(value*second.get(mask, 0) for mask, value in first.items())


def sparse_leaf_check(n: int) -> dict:
    bits = 4*n+3
    coefficient = sp.Rational(1, 48)**(2*n+1)
    words = list(itertools.product((0, 1), repeat=n))
    columns, remainders, expected_masks = [], [], []
    for word in words:
        vector = sparse_F({1: sp.Integer(1)}, bits)
        for toggle in word:
            vector = sparse_F(vector, bits)
            if toggle:
                vector = sparse_B(vector)
            vector = sparse_F(vector, bits)
        mask = 1 << (bits-1)
        for j, toggle in enumerate(word, 1):
            if toggle:
                mask |= 1 << (4*(n-j)+2)
        leaf_part = {key: value for key, value in vector.items() if key & (1 << (bits-1))}
        require(leaf_part == {mask: coefficient}, 'Exact top-leaf coefficient and uniqueness')
        columns.append(vector)
        remainders.append({key: value for key, value in vector.items() if key not in leaf_part})
        expected_masks.append(mask)
    require(len(set(expected_masks)) == 2**n, 'Distinct binary words have distinct top leaves')
    Gram = sp.Matrix([[sparse_dot(v, w) for w in columns] for v in columns])
    remainder_Gram = sp.Matrix([[sparse_dot(v, w) for w in remainders] for v in remainders])
    require(Gram-coefficient**2*sp.eye(2**n) == remainder_Gram, 'Exact sparse Gram sum-of-squares certificate')
    active = set().union(*(set(column) for column in columns))
    return {'word_depth_n': n, 'implicit_register_bits': bits,
            'implicit_physical_target_states': 2**bits+1,
            'physical_state_space_enumerated': False,
            'controlled_Gram_dimension': 2**n, 'active_Walsh_coordinates_evaluated': len(active),
            'largest_sparse_column_support': max(len(column) for column in columns),
            'top_leaf_coefficient_exact': str(coefficient),
            'top_leaf_matrix_is_coefficient_times_identity': True,
            'Gram_remainder_exact_sum_of_squares': True,
            'full_pi0_Gram_eigenvalue_floor': str(coefficient**2/2)}


def exact_stencil_checks() -> list[dict]:
    t = sp.symbols('t')
    records = []
    for a, T, name in ((sp.Integer(0), sp.Integer(1), 'endpoint'),
                       (sp.Rational(1, 8), sp.Integer(2), 'fixed_dwell_extrapolation')):
        for p in (1, 2, 3, 4):
            nodes = [a+(T-a)*(1-sp.cos(j*sp.pi/p))/2 for j in range(p+1)]
            weights = []
            for j in range(p+1):
                basis = sp.prod((t-nodes[k])/(nodes[j]-nodes[k]) for k in range(p+1) if k != j)
                weights.append(sp.simplify(sp.diff(basis, t).subs(t, 0)))
            for power in range(p+1):
                require(sp.simplify(sum(weight*node**power for weight, node in zip(weights, nodes))
                                    -(1 if power == 1 else 0)) == 0,
                        'Exact polynomial derivative reproduction')
            norm = sp.simplify(sum((-1)**(j+1)*weights[j] for j in range(p+1)))
            require(all(sp.simplify((-1)**(j+1)*weights[j]) > 0 for j in range(p+1)),
                    'Exact alternating derivative stencil signs')
            if a == 0:
                bound = 2*p*p/T
                require(norm == bound, 'Exact endpoint stencil l1 norm')
            else:
                # Here (T+a)/(T-a)=17/15, so exp(acosh(...))=5/3.
                bound = 4*p**3/(T-a)*sp.Rational(5, 3)**p
                require(sp.simplify(bound-norm) > 0, 'Fixed-dwell extrapolation l1 bound')
            records.append({'scheme': name, 'polynomial_degree': p,
                            'nodes_exact': [str(node) for node in nodes],
                            'derivative_weights_exact': [str(weight) for weight in weights],
                            'exact_l1_norm': str(norm), 'l1_certificate': str(bound),
                            'polynomial_moments_checked': p+1})
    return records


def rational_filter_error(n: int, delta: sp.Rational) -> sp.Rational:
    z = sp.Rational(65, 64)
    u, c = (z-1/z)/2, (z+1/z)/2
    require(delta < 1, 'Small target generator approximation error')
    # Every lower-bound register has m=4n+3>=3. On singleton Walsh
    # functions, Fr=(49/48) chi_1-(1/3) chi_2+(1/48) chi_3. Hidden
    # functions have half their squared hidden norm in L2(pi_0).
    # Thus ||Fr||_pi0<1 independently of register length. The exact
    # endpoint identities give left norm <=2u^2 and right norm <=2u/z;
    # the right=4u/z bound below is a deliberately looser bound.
    endpoint_squared_norm = (sp.Rational(49, 48)**2+sp.Rational(1, 3)**2
                             +sp.Rational(1, 48)**2)/2
    require(n >= 1 and endpoint_squared_norm < 1,
            'Dimension-independent exact endpoint norm certificate')
    eF = delta*(10+delta)/3
    eZ0 = eF*(4+eF)
    M, b = 9+abs(1-c/z), u/z
    eZ1 = (eF*(M+2*delta)*(2+eF)+4*delta*(2+eF)+2*M*eF)/b
    eZ = max(eZ0, eZ1)
    approximate = 4+eZ
    word_error = n*eZ*approximate**(n-1)
    left, right = 2*u*u, 4*u/z
    require((2*u/z)**2*endpoint_squared_norm <= right**2,
            'Right endpoint norm bound follows from the same exact certificate')
    left_error = delta*(2+eF)+5*eF
    right_error = 2*(eF*(5+delta)+2*delta)
    entry = (left_error*approximate**(2*n)*(right+right_error)
             +left*word_error*approximate**n*(right+right_error)
             +left*4**n*word_error*(right+right_error)
             +left*4**(2*n)*right_error)/(4*u**3/z)
    return 2**n*entry


def scaling_certificates() -> list[dict]:
    records = []
    z = sp.Rational(65, 64)
    c, u = (z+1/z)/2, (z-1/z)/2
    coefficient_letter = (2+abs(1-c/z))/(u/z)
    normalization = 4*u**3/z
    for n in (1, 2, 3):
        Gram_floor = sp.Rational(1, 2*48**(4*n+2))
        for fixed in (False, True):
            if fixed:
                T, a, p = sp.Integer(n+1), sp.Rational(1, 8), 100*(n+1)
                root_floor = math.isqrt(8*(n+1))
                rho_upper = sp.Rational(root_floor+1, root_floor-1)
                J = 4*p**3/(T-a)*rho_upper**p
                scheme = 'fixed_dwell_extrapolation'
            else:
                T, a = sp.Integer(1), sp.Integer(0)
                p = math.ceil(100*(n+1)/math.log(n+2))
                rho_upper = None
                J = 2*p*p/T
                scheme = 'endpoint_shrinking_dwell'
            # e^(5T) < 3^(5T) gives an entirely rational remainder bound.
            delta = J*3**(5*T)*(5*T)**(p+1)/sp.factorial(p+1)
            error = rational_filter_error(n, delta)
            require(error < Gram_floor/2, 'Rational stencil substitution error below half the leaf Gram floor')
            degree = 10*n+6
            coefficient_budget = coefficient_letter**(2*n)*J**degree/normalization
            response_floor = Gram_floor/(2*2**n*coefficient_budget)
            with mp.workdps(100):
                minimum_dwell = number(a) if fixed else (1-mp.cos(mp.pi/p))/2
                records.append({
                    'word_depth_n': n, 'scheme': scheme, 'interpolation_degree': p,
                    'largest_stencil_time_T': str(T), 'minimum_nonzero_dwell': digits(minimum_dwell),
                    'l1_norm_rational_certificate_log10': digits(mp.log10(number(J))),
                    'extrapolation_growth_factor_rational_upper': str(rho_upper) if fixed else None,
                    'generator_Taylor_error_rational_certificate_log10': digits(mp.log10(number(delta))),
                    'controlled_matrix_error_rational_certificate_log10': digits(mp.log10(number(error))),
                    'exact_leaf_Gram_floor': str(Gram_floor),
                    'rational_error_below_half_Gram_floor': True,
                    'certified_finite_experiment_singular_value_floor': str(Gram_floor/2),
                    'generator_word_degree_bound': degree,
                    'maximum_protocol_horizon': str(degree*T),
                    'entry_coefficient_budget_log10': digits(mp.log10(number(coefficient_budget))),
                    'response_error_lower_certificate_log10': digits(mp.log10(number(response_floor))),
                    'scope': 'Exact scalar norm/remainder bookkeeping for the displayed finite choices; constants are sufficient and not optimized.',
                })
    return records


def numerical_weights(a: mp.mpf, T: mp.mpf, p: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    nodes = [a+(T-a)*(1-mp.cos(j*mp.pi/p))/2 for j in range(p+1)]
    barycentric = [(-1)**j*(mp.mpf(1)/2 if j in (0, p) else mp.mpf(1)) for j in range(p+1)]
    if a == 0:
        weights = [mp.mpf(0)]+[-barycentric[j]/(barycentric[0]*nodes[j]) for j in range(1, p+1)]
        weights[0] = -mp.fsum(weights[1:])
    else:
        total = mp.fsum(-barycentric[j]/nodes[j] for j in range(p+1))
        reciprocal_sum = mp.fsum(1/node for node in nodes)
        weights = [(-barycentric[j]/nodes[j]/total)*(-reciprocal_sum+1/nodes[j]) for j in range(p+1)]
    return nodes, weights


def numerical_stencils(data: dict) -> list[dict]:
    records = []
    with mp.workdps(100):
        z = number(data['z'])
        for fixed, p in ((False, 24), (False, 40), (True, 48), (True, 64)):
            a, T = (mp.mpf(1)/8, mp.mpf(2)) if fixed else (mp.mpf(0), mp.mpf(1))
            nodes, weights = numerical_weights(a, T, p)
            J = mp.fsum(abs(weight) for weight in weights)
            bound_J = 4*p**3/(T-a)*mp.exp(p*mp.acosh((T+a)/(T-a))) if fixed else 2*p*p/T
            require(J <= bound_J*(1+mp.mpf('1e-85')), 'High precision stencil l1 consistency')
            for order in (0, 1, 2, p):
                moment = mp.fsum(weight*node**order for weight, node in zip(weights, nodes))
                require(abs(moment-(1 if order == 1 else 0)) < mp.mpf('1e-60'),
                        'Selected high-precision stencil polynomial moments')
            errors = []
            for on, key in ((False, 'Q0'), (True, 'Qh')):
                Q = matrix(data[key])
                D = mp.diag([1/mp.sqrt(z)]+[mp.sqrt(z)]*(Q.rows-1)) if on else mp.eye(Q.rows)
                inverse = D**-1
                symmetric = D*Q*inverse
                values, basis = mp.eigsy((symmetric+symmetric.T)/2)
                approximate_values = [mp.fsum(weight*mp.exp(node*value) for weight, node in zip(weights, nodes))
                                      for value in values]
                approximate = inverse*basis*mp.diag(approximate_values)*basis.T*D
                error = frobenius(approximate-Q)
                certificate = bound_J*mp.exp(5*T)*(5*T)**(p+1)/mp.factorial(p+1)
                require(error <= Q.rows*certificate+mp.mpf('1e-75'),
                        'High-precision derivative stencil agrees with analytic target remainder')
                errors.append(error)
            records.append({'scheme': 'fixed_dwell_extrapolation' if fixed else 'endpoint',
                            'degree': p, 'a': digits(a), 'T': digits(T), 'decimal_precision': 100,
                            'stencil_l1_norm': digits(J), 'stencil_l1_certificate': digits(bound_J),
                            'maximum_generator_Frobenius_error': digits(max(errors)),
                            'operator_Taylor_remainder_certificate': digits(certificate),
                            'full_generator_dimension': data['Q0'].rows,
                            'scope': 'Selected high-precision consistency checks; no numerical rank or optimized lower-bound inference.'})
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/shift_register_lower_bound.json'))
    args = parser.parse_args()
    physical = []
    largest = None
    for bits in (1, 2, 3):
        largest, record = physical_register(bits)
        physical.append(record)
    report = {
        'status': 'PASS',
        'scope': 'Exact small physical shift registers, sparse Walsh leaf/Gram certificates, and endpoint/fixed-dwell derivative-stencil bounds.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
        'physical_register_checks': physical,
        'sparse_Walsh_leaf_checks': [sparse_leaf_check(n) for n in (1, 2, 3)],
        'exact_small_derivative_stencils': exact_stencil_checks(),
        'rational_interpolation_and_coefficient_certificates': scaling_certificates(),
        'selected_high_precision_stencils': numerical_stencils(largest),
        'largest_constructed_physical_generator_dimension': 9,
        'largest_controlled_Gram_dimension': 8,
        'no_large_physical_state_enumeration_or_numerical_rank_tests': True,
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
