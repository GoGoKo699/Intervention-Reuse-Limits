#!/usr/bin/env python3
"""Exact small-matrix checks of fixed-actuator response hierarchies.

Graded reachability checks response words for arbitrary scalar protocols,
not sampled trajectories. Independent full-generator powers check the first
nonzero time and field coefficients. All arithmetic is exact and rational,
except symbolic Laurent polynomials for finite-field identities.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_zero(expression: sp.Expr, message: str) -> None:
    require(sp.cancel(expression) == 0, message)


class ExactSpan:
    """Small rational column span with deterministic echelon reduction."""

    def __init__(self, size: int) -> None:
        self.size = size
        self.columns: list[tuple[int, sp.Matrix]] = []

    def insert(self, candidate: sp.Matrix) -> sp.Matrix | None:
        residual = candidate.copy()
        for pivot, basis in self.columns:
            if residual[pivot]:
                residual -= residual[pivot]*basis
        pivots = [i for i in range(self.size) if residual[i]]
        if not pivots:
            return None
        pivot = pivots[0]
        residual /= residual[pivot]
        self.columns.append((pivot, residual))
        self.columns.sort(key=lambda item: item[0])
        return residual

    def basis(self) -> list[sp.Matrix]:
        return [column for _, column in self.columns]


def close_span(seeds: list[sp.Matrix], operators: list[sp.Matrix], size: int) -> ExactSpan:
    span = ExactSpan(size)
    queue = []
    for seed in seeds:
        added = span.insert(seed)
        if added is not None:
            queue.append(added)
    index = 0
    while index < len(queue):
        column = queue[index]
        index += 1
        for operator in operators:
            added = span.insert(operator*column)
            if added is not None:
                queue.append(added)
    return span


def support(d: int) -> tuple[sp.Matrix, sp.Matrix]:
    R = sp.Rational
    values = {
        2: ([-1, 0, 1], [R(1, 4), R(1, 2), R(1, 4)]),
        3: ([-1, -R(1, 2), R(1, 2), 1], [R(1, 6), R(1, 3), R(1, 3), R(1, 6)]),
        4: ([-1, -R(1, 2), 0, R(1, 2), 1], [R(1, 5)]*5),
    }
    grid, weights = values[d]
    return sp.Matrix(grid), sp.Matrix([weights])


def orthogonal_projector(g: sp.Matrix, mu: sp.Matrix, d: int) -> tuple[sp.Matrix, sp.Expr, sp.Matrix]:
    powers = [g.applyfunc(lambda x: x**j) for j in range(d+1)]
    gram = sp.Matrix([[(mu*sp.diag(*powers[i])*powers[j])[0]
                       for j in range(d)] for i in range(d)])
    rhs = sp.Matrix([(mu*sp.diag(*powers[i])*powers[d])[0] for i in range(d)])
    coefficients = gram.inv()*rhs
    polynomial = powers[d]-sum((coefficients[j]*powers[j] for j in range(d)), sp.zeros(len(g), 1))
    norm = (mu*sp.diag(*polynomial)*polynomial)[0]
    projector = polynomial*mu*sp.diag(*polynomial)/norm
    require(projector**2 == projector, 'Exact orthogonal rank-one projector')
    require(projector.rank() == 1 and norm > 0, 'Positive polynomial norm')
    for j in range(d):
        require(projector*powers[j] == sp.zeros(len(g), 1), 'Projector kills lower actuator powers')
    require((mu*sp.diag(*polynomial)*powers[d])[0] == norm,
            'Monic polynomial leading moment equals its norm')
    return polynomial, norm, projector


def generator_coefficients(K: sp.Matrix, mu: sp.Matrix, g: sp.Matrix, degree: int) -> list[sp.Matrix]:
    """Row-generator Taylor coefficients with k=1; no field differentiation."""
    n = len(g)+1
    coefficients = []
    for order in range(degree+1):
        Q = sp.zeros(n)
        for j in range(len(g)):
            Q[0, j+1] = mu[j]*(1+g[j])**order/sp.factorial(order)
            Q[j+1, 0] = (g[j]-1)**order/sp.factorial(order)
            if order == 0:
                for ell in range(len(g)):
                    if ell != j:
                        Q[j+1, ell+1] = K[j, ell]
        for i in range(n):
            Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
        coefficients.append(Q)
    return coefficients


def finite_generator(K: sp.Matrix, mu: sp.Matrix, g: sp.Matrix, y: sp.Symbol) -> sp.Matrix:
    """Set y=exp(h/2); all actuator levels are half integers."""
    n = len(g)+1
    Q = sp.zeros(n)
    for j in range(len(g)):
        Q[0, j+1] = mu[j]*y**(2*(1+g[j]))
        Q[j+1, 0] = y**(2*(g[j]-1))
        for ell in range(len(g)):
            if ell != j:
                Q[j+1, ell+1] = K[j, ell]
    for i in range(n):
        Q[i, i] = -sum(Q[i, j] for j in range(n) if j != i)
    return Q


def scalar_power(initial: sp.Matrix, matrix: sp.Matrix, output: sp.Matrix, power: int) -> sp.Expr:
    state = initial
    for _ in range(power):
        state = (state*matrix).applyfunc(sp.expand)
    return sp.expand((state*output)[0])


def scalar_power_coefficients(initial: sp.Matrix, matrices: list[sp.Matrix], output: sp.Matrix,
                              power: int, degree: int) -> list[sp.Expr]:
    rows = [initial]+[sp.zeros(1, initial.cols) for _ in range(degree)]
    for _ in range(power):
        rows = [sum((rows[n-j]*matrices[j] for j in range(n+1)), sp.zeros(1, initial.cols))
                for n in range(degree+1)]
    return [(row*output)[0] for row in rows]


def response_word_check(first: list[sp.Matrix], second: list[sp.Matrix], initial: sp.Matrix,
                        output: sp.Matrix, maximum: int, observe_partition: bool) -> dict:
    """All protocol coefficient words lie in the computed graded spaces.

Closure under drift includes every unperturbed semigroup. In the visible
law check closure also includes the A observation projector; B is I-A.
This allows arbitrary observation times without choosing time samples.
"""
    size = first[0].rows
    combined = [sp.diag(first[j].T, second[j].T) for j in range(maximum+1)]
    initial_pair = initial.T.col_join(initial.T)
    readout = (-output.T).row_join(output.T)
    free_operators = [combined[0]]
    if observe_partition:
        A = sp.zeros(size)
        A[0, 0] = 1
        free_operators.append(sp.diag(A, A))
    spaces = []
    records = []
    for order in range(maximum+1):
        if order == 0:
            seeds = [initial_pair]
        else:
            seeds = [combined[j]*column for j in range(1, order+1)
                     for column in spaces[order-j].basis()]
        span = close_span(seeds, free_operators, 2*size)
        spaces.append(span)
        values = [(readout*column)[0] for column in span.basis()]
        records.append({'field_order': order, 'reachable_span_dimension': len(span.columns),
                        'difference_readout_annihilates_span': all(value == 0 for value in values)})
    return {'pair_state_dimension': 2*size, 'orders': records,
            'free_operators': 'unperturbed generator and A observation projector' if observe_partition else 'unperturbed generator',
            'scope': 'Exact sufficient equality certificate for every response word and every bounded scalar protocol; no numerical time grid.'}


def hierarchy_case(d: int) -> dict:
    g, mu = support(d)
    hidden = len(g)
    one = sp.ones(hidden, 1)
    polynomial, norm, projector = orthogonal_projector(g, mu, d)
    eta = norm/(2*max(abs(x) for x in polynomial)**2)
    K0 = one*mu-sp.eye(hidden)
    K1 = K0-eta*projector
    require((mu*g)[0] == 0 and (mu*sp.diag(*g)*g)[0] == sp.Rational(1, 2),
            'Shared G=1 and W=1/2 support')
    for K in (K0, K1):
        require(K*one == sp.zeros(hidden, 1) and mu*K == sp.zeros(1, hidden),
                'Hidden generator conserves probability and has fixed stationary law')
        require(sp.diag(*mu)*K == K.T*sp.diag(*mu), 'Exact detailed balance')
        require(all(K[i, j] >= mu[j]/2 > 0 for i in range(hidden) for j in range(hidden) if i != j),
                'Strictly positive off-diagonal generator entries with common floor')
        require(K*g == -g, 'Same single exponential actuator covariance')
    initial = sp.Matrix([[sp.Rational(1, 2)]+[x/2 for x in mu]])
    readout = sp.Matrix([-1]+[1]*hidden)
    degree = 2*d+1
    first = generator_coefficients(K0, mu, g, degree)
    second = generator_coefficients(K1, mu, g, degree)
    require(initial*first[0] == sp.zeros(1, hidden+1), 'Zero-field stationary preparation')
    mean_words = response_word_check(first, second, initial, readout, degree, False)
    require(all(item['difference_readout_annihilates_span'] for item in mean_words['orders'][:-1]),
            'Every protocol mean coefficient agrees through order 2d')
    require(not mean_words['orders'][-1]['difference_readout_annihilates_span'],
            'Response-word space can distinguish at order 2d+1')
    path_words = response_word_check(first, second, initial, sp.ones(hidden+1, 1), 2*d, True)
    require(all(item['difference_readout_annihilates_span'] for item in path_words['orders'][:-1]),
            'Every finite visible observation word agrees through order 2d-1')
    require(not path_words['orders'][-1]['difference_readout_annihilates_span'],
            'Visible observation words can distinguish at order 2d')

    y = sp.symbols('y', positive=True)
    full0, full1 = (finite_generator(K, mu, g, y) for K in (K0, K1))
    field_overlap = sum(mu[i]*polynomial[i]*y**(2*g[i]) for i in range(hidden))
    actual = scalar_power(initial, full1, readout, 3)-scalar_power(initial, full0, readout, 3)
    expected = eta*(1-y**(-4))*field_overlap**2/norm
    require_zero(actual-expected, 'Exact finite-field third time derivative of mean')
    coefficients0 = scalar_power_coefficients(initial, first, readout, 3, degree)
    coefficients1 = scalar_power_coefficients(initial, second, readout, 3, degree)
    difference = [b-a for a, b in zip(coefficients0, coefficients1)]
    leading = 2*eta*norm/sp.factorial(d)**2
    require(all(value == 0 for value in difference[:-1]), 'Direct full-generator time derivative lower field orders vanish')
    require(difference[-1] == leading > 0, 'Direct full-generator leading mean coefficient')

    killed0 = K0-sp.diag(*[y**(2*(value-1)) for value in g])
    killed1 = K1-sp.diag(*[y**(2*(value-1)) for value in g])
    no_exit_gap = scalar_power(mu, killed1, one, 3)-scalar_power(mu, killed0, one, 3)
    require_zero(no_exit_gap+eta*y**(-4)*field_overlap**2/norm,
                 'Exact finite-field third time derivative of B no-exit probability')
    return {
        'polynomial_degree_d': d, 'hidden_states': hidden, 'full_Markov_states': hidden+1,
        'actuator_values': [str(x) for x in g], 'stationary_weights': [str(x) for x in mu],
        'G': '1', 'W': '1/2', 'k': '1', 'lambda': '1',
        'monic_orthogonal_polynomial_values': [str(x) for x in polynomial],
        'polynomial_squared_norm': str(norm), 'eta_first': '0', 'eta_second': str(eta),
        'minimum_off_diagonal_K0': str(min(K0[i, j] for i in range(hidden) for j in range(hidden) if i != j)),
        'minimum_off_diagonal_K1': str(min(K1[i, j] for i in range(hidden) for j in range(hidden) if i != j)),
        'common_actuator_covariance': '(1/2) exp(-t)',
        'stationarity_reversibility_and_positive_generator': True,
        'mean_protocol_response_words': mean_words,
        'visible_path_response_words': path_words,
        'exact_finite_field_mean_third_time_derivative_identity': True,
        'first_differing_mean_field_order': degree,
        'difference_mean_field_coefficient_leading_t3': str(leading/6),
        'exact_finite_field_no_exit_third_time_derivative_identity': True,
        'first_differing_no_exit_field_order': 2*d,
        'difference_no_exit_field_coefficient_leading_t3': str(-eta*norm/(6*sp.factorial(d)**2)),
    }


def binary_actuator_case() -> dict:
    R = sp.Rational
    Kplus = sp.Matrix([[-R(1, 2), R(1, 4), R(1, 8), R(1, 8)],
                       [R(1, 4), -1, R(3, 8), R(3, 8)],
                       [R(1, 8), R(3, 8), -R(3, 4), R(1, 4)],
                       [R(1, 8), R(3, 8), R(1, 4), -R(3, 4)]])
    Kminus = sp.Matrix([[-R(3, 4), R(1, 4), R(3, 8), R(1, 8)],
                        [R(1, 4), -R(3, 4), R(3, 8), R(1, 8)],
                        [R(3, 8), R(3, 8), -1, R(1, 4)],
                        [R(1, 8), R(1, 8), R(1, 4), -R(1, 2)]])
    g, mu, one = sp.Matrix([1, 1, -1, -1]), sp.ones(1, 4)/4, sp.ones(4, 1)
    z = sp.symbols('z', positive=True)
    covariance_transform = (z+1)/((z+1)**2-sp.Rational(1, 8))
    require(Kplus.charpoly(z).as_expr() == Kminus.charpoly(z).as_expr(),
            'Binary actuator examples also have the same complete hidden spectrum')
    triple_values = []
    for K in (Kplus, Kminus):
        require(K == K.T and K*one == sp.zeros(4, 1), 'Binary actuator reversible generator')
        require(all(K[i, j] > 0 for i in range(4) for j in range(4) if i != j),
                'Binary actuator generator strictly positive off diagonal')
        direct = (mu*sp.diag(*g)*(z*sp.eye(4)-K).inv()*g)[0]
        require_zero(direct-covariance_transform, 'Same complete two-time actuator covariance')
        triple_values.append((mu*sp.diag(*(K*g))*sp.diag(*g)*(K*g))[0])
    require(triple_values == [R(1, 8), -R(1, 8)], 'Different mixed higher actuator moment')

    x = sp.symbols('x', positive=True)
    initial = sp.Matrix([[R(1, 2), R(1, 8), R(1, 8), R(1, 8), R(1, 8)]])
    output = sp.Matrix([-1, 1, 1, 1, 1])
    y = sp.symbols('y', positive=True)
    full = [finite_generator(K, mu, g, y).subs(y, x**R(1, 4)) for K in (Kplus, Kminus)]
    # Here x=exp(2h), distinct from y=exp(h/2) in the helper.
    derivatives = []
    for n in range(1, 6):
        gap = scalar_power(initial, full[0], output, n)-scalar_power(initial, full[1], output, n)
        gap = sp.factor(gap)
        derivatives.append(gap)
    require(all(value == 0 for value in derivatives[:4]), 'Binary mean time derivatives one through four agree')
    require_zero(derivatives[4]-(x-1)**4/(32*x**3), 'Exact fifth time derivative counterexample')
    return {
        'hidden_states': 4, 'full_Markov_states': 5,
        'stationary_weights': ['1/4']*4, 'actuator_values': ['1', '1', '-1', '-1'],
        'K_plus': [[str(Kplus[i, j]) for j in range(4)] for i in range(4)],
        'K_minus': [[str(Kminus[i, j]) for j in range(4)] for i in range(4)],
        'common_covariance': 'exp(-t) cosh(t/(2 sqrt(2)))',
        'common_covariance_Laplace_transform': str(covariance_transform),
        'common_hidden_characteristic_polynomial': str(sp.factor(Kplus.charpoly(z).as_expr())),
        'all_binary_actuator_two_time_laws_equal': True,
        'higher_actuator_moments_plus_minus': [str(value) for value in triple_values],
        'time_derivatives_1_through_4_equal_at_every_field': True,
        'fifth_time_derivative_difference': str(derivatives[4]),
        'field_variable': 'x=exp(2h)', 'gap_orientation': 'plus minus minus',
        'first_nonzero_field_power_in_fifth_time_derivative': 4,
        'scope': 'A deterministic finite-state counterexample: matching all two-time actuator laws does not match finite-field mean response.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/actuator_hierarchy.json'))
    args = parser.parse_args()
    report = {
        'status': 'PASS',
        'scope': 'Exact finite-state consistency checks of fixed-actuator delayed response and a binary-actuator two-time counterexample; no simulations or statistical inference.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
        'fixed_actuator_hierarchies': [hierarchy_case(d) for d in (2, 3, 4)],
        'binary_actuator_two_time_counterexample': binary_actuator_case(),
        'largest_full_generator_dimension': 6,
        'largest_pair_response_word_dimension': 12,
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
