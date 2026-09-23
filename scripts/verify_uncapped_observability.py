#!/usr/bin/env python3
"""Exact finite certificates for ordered resolvents and uncapped observability.

Only standard-library rational arithmetic is used.  The largest dense matrix
is 7 by 7.  No earlier repository verifier is imported or modified.  These
fixtures check algebra and explicit finite examples, not analytic continuation
for all models or the all-accuracy lower-bound theorem.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def eye(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def zeros(n: int) -> list[list[F]]:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def mm(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F())
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a: list[list[F]], x: list[F]) -> list[F]:
    return [sum((v*w for v, w in zip(row, x)), F()) for row in a]


def add(a: list[list[F]], b: list[list[F]], scale: F = F(1)) -> list[list[F]]:
    return [[x+scale*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def times(a: list[list[F]], scalar: F) -> list[list[F]]:
    return [[scalar*x for x in row] for row in a]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    aug = [row.copy()+unit for row, unit in zip(a, eye(n))]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divisor = aug[col][col]
        aug[col] = [value/divisor for value in aug[col]]
        for row in range(n):
            if row != col:
                multiplier = aug[row][col]
                aug[row] = [x-multiplier*y for x, y in zip(aug[row], aug[col])]
    result = [row[n:] for row in aug]
    require(mm(a, result) == eye(n), 'Rational inverse multiplies back to the identity')
    return result


def diagonal(x: list[F]) -> list[list[F]]:
    return [[value if i == j else F() for j in range(len(x))]
            for i, value in enumerate(x)]


def scalar(a: list[list[F]], mu: list[F]) -> F:
    return sum((p*sum(row) for p, row in zip(mu, a)), F())


def product(items: list[list[list[F]]]) -> list[list[F]]:
    answer = eye(len(items[0]))
    for item in items:
        answer = mm(answer, item)
    return answer


def check_markov_reversible(p: list[list[F]], mu: list[F]) -> None:
    require(all(value >= 0 for row in p for value in row), 'Resolvent entries are nonnegative')
    require(all(sum(row) == 1 for row in p), 'Resolvent rows sum to one')
    require(all(mu[i]*p[i][j] == mu[j]*p[j][i]
                for i in range(len(mu)) for j in range(len(mu))),
            'Resolvent obeys exact detailed balance')


def polynomial_product(a: list[list[list[F]]], b: list[list[list[F]]],
                       degree: int) -> list[list[list[F]]]:
    n = len(a[0])
    result = [zeros(n) for _ in range(degree+1)]
    for i in range(min(len(a), degree+1)):
        for j in range(min(len(b), degree+1-i)):
            result[i+j] = add(result[i+j], mm(a[i], b[j]))
    return result


def resolvent_parity_checks() -> list[dict]:
    """Compare a sign average of full series with the ordered P^2 word."""
    k0 = [[F(-1), F(1), F(0)],
          [F(1), F(-3), F(2)],
          [F(0), F(2), F(-2)]]
    mu, s = [F(1, 3)]*3, F(8)
    features = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    cases = []
    for speed in (1, 10**6):
        k = times(k0, F(speed))
        p = times(inverse(add(times(eye(3), s), k, F(-1))), s)
        check_markov_reversible(p, mu)
        p2 = mm(p, p)
        for signed in (False, True):
            labels = [row.copy() for row in features]
            if signed:
                labels[1] = [F(1), F(-1), F(0)]
            ds = [diagonal(row) for row in labels]
            m, degree = len(ds), len(ds)+2
            coefficients = [F() for _ in range(degree+1)]
            for signs in itertools.product((-1, 1), repeat=m):
                polys = []
                for d, sign in zip(ds, signs):
                    series = [p]
                    multiplier = times(mm(p, d), F(-sign)/s)
                    for _ in range(degree):
                        series.append(mm(multiplier, series[-1]))
                    # This series solves (sI-K+z sign D) R(z)=sI coefficientwise.
                    a0, a1 = add(times(eye(3), s), k, F(-1)), times(d, F(sign))
                    require(mm(a0, series[0]) == times(eye(3), s),
                            'Constant resolvent coefficient solves the defining equation')
                    for j in range(1, degree+1):
                        require(add(mm(a0, series[j]), mm(a1, series[j-1])) == zeros(3),
                                'Every higher resolvent coefficient solves the defining equation')
                    polys.append(series)
                series_product = [eye(3)]
                for poly in polys:
                    series_product = polynomial_product(series_product, poly, degree)
                parity = F(1, 2**m)
                for sign in signs:
                    parity *= sign
                for j, coefficient in enumerate(series_product):
                    coefficients[j] += parity*scalar(coefficient, mu)
            word_factors = [ds[0]]
            for d in ds[1:]:
                word_factors.extend((p2, d))
            direct_word = scalar(product(word_factors), mu)
            expected = (-F(1)/s)**m*direct_word
            require(coefficients[m] == expected,
                    'Parity degree m equals (-1/s)^m times the ordered P^2 color word')
            require(all(coefficients[j] == 0 for j in range(m)) and coefficients[m+1] == 0,
                    'All lower degrees and the next opposite-parity degree vanish')
            require(coefficients[m+2] != 0,
                    'A nonzero higher parity term makes the interpolation tail necessary')
            pdp_word = scalar(product([mm(mm(p, d), p) for d in ds]), mu)
            require(pdp_word == direct_word, 'Stationarity removes exactly the two endpoint resolvents')
            wrong_factors = [ds[0]]
            for d in ds[1:]:
                wrong_factors.extend((p, d))
            require(scalar(product(wrong_factors), mu) != direct_word,
                    'The fixture distinguishes the required P^2 gaps from an incorrect single P')
            cases.append({'internal_speed': speed, 'signed_feature': signed,
                          's_exact': str(s), 'feature_count': m,
                          'leading_parity_coefficient_exact': str(coefficients[m]),
                          'higher_parity_coefficient_exact': str(coefficients[m+2]),
                          'ordered_color_word_exact': str(direct_word)})
    return cases


def positive_definite_pivots(a: list[list[F]]) -> list[F]:
    require(a == transpose(a), 'Exact LDL test receives a symmetric matrix')
    b, pivots = [row.copy() for row in a], []
    for j in range(len(a)):
        pivot = b[j][j]
        require(pivot > 0, 'Each exact LDL pivot is positive')
        pivots.append(pivot)
        for i in range(j+1, len(a)):
            for k in range(j+1, len(a)):
                b[i][k] -= b[i][j]*b[j][k]/pivot
    return pivots


def smoothed_flip_checks() -> dict:
    """Three two-bit ports and a hub retain a negative flip mode after smoothing."""
    mu, k = [F(1, 12)]*6+[F(1, 2)], zeros(7)

    def rate(i: int, j: int, value: F) -> None:
        k[i][j] += value
        k[i][i] -= value

    for bit in range(2):
        for i, j in ((bit, 2+bit), (2+bit, 4+(1-bit)), (4+bit, bit)):
            rate(i, j, F(1, 16))
            rate(j, i, F(1, 16))
    for leaf in range(6):
        rate(leaf, 6, F(1))
        rate(6, leaf, F(1, 6))
    require(all(sum(row) == 0 for row in k), 'Miniature hidden generator is conservative')
    require(all(mu[i]*k[i][j] == mu[j]*k[j][i] for i in range(7) for j in range(7)),
            'Hub and matching gates obey exact detailed balance')
    weighted_cap = mm(diagonal(mu), add(times(eye(7), F(3)), k))
    cap_pivots = positive_definite_pivots(weighted_cap)
    ports = [list(range(2*j, 2*j+2)) for j in range(3)]

    def block(a: list[list[F]], c: int, d: int) -> list[list[F]]:
        return [[a[i][j] for j in ports[d]] for i in ports[c]]

    edges = ((0, 2), (2, 1), (1, 0))
    raw = {edge: times(block(k, *edge), F(16)) for edge in edges}
    flip = [[F(0), F(1)], [F(1), F(0)]]
    require(product([raw[edge] for edge in edges]) == flip,
            'The exact raw three-edge gate is a bit flip')
    results = []
    for s in (F(8), F(64), F(1024)):
        p = times(inverse(add(times(eye(7), s), k, F(-1))), s)
        check_markov_reversible(p, mu)
        p2 = mm(p, p)
        smoothed = {edge: times(block(p2, *edge), 8*s) for edge in edges}
        bounds = []
        for edge in edges:
            c, d = edge
            require(all(value >= 0 for row in smoothed[edge] for value in row),
                    'Every smoothed off-port kernel is positive')
            require(times(block(p2, d, c), 8*s) == transpose(smoothed[edge]),
                    'Reverse smoothed edge is the conditional stationary adjoint')
            error = add(smoothed[edge], raw[edge], F(-1))
            frobenius2 = sum((v*v for row in error for v in row), F())
            require(frobenius2 <= (F(216)/s)**2,
                    'Exact block Frobenius certificate implies the advertised 216/s operator bound')
            bounds.append(str(frobenius2))
        cycle = product([smoothed[edge] for edge in edges])
        require(cycle[0][0] == cycle[1][1] and cycle[0][1] == cycle[1][0],
                'Simultaneous bit flip symmetry diagonalizes the smoothed cycle')
        signed_eigenvalue = cycle[0][0]-cycle[0][1]
        require(signed_eigenvalue < 0,
                'The ordered positive cross-port cycle retains a negative bit-flip mode')
        results.append({'s_exact': str(s), 'signed_cycle_eigenvalue_exact': str(signed_eigenvalue),
                        'cycle_row_sum_exact': str(sum(cycle[0])),
                        'edge_error_frobenius_squared_exact': bounds})
    return {'hidden_states': 7, 'full_states_with_A': 8,
            'mu_exact': list(map(str, mu)), 'spectral_cap': 3,
            'positive_weighted_cap_LDL_pivots_exact': list(map(str, cap_pivots)),
            'raw_cycle_exact': [[str(x) for x in row] for row in flip], 'cases': results,
            'scope': 'A three-port miniature checks ordered smoothing and the surviving negative flip eigenvalue. It is not the complete nineteen-level target.'}


def chebyshev_and_budget_checks() -> dict:
    polynomials = [[1], [0, 1]]
    for degree in range(1, 64):
        nxt = [0]+[2*x for x in polynomials[-1]]
        for j, value in enumerate(polynomials[-2]):
            nxt[j] -= value
        polynomials.append(nxt)
    for degree, polynomial in enumerate(polynomials):
        require(sum(map(abs, polynomial)) <= 3**degree,
                'Chebyshev coefficient l1 norm is bounded by 3^degree')
    checks = 0
    for degree in (1, 2, 4, 8, 16, 32, 64):
        for coefficient in range(degree+1):
            majorant = int(coefficient == 0)+2*sum(
                abs(polynomials[j][coefficient]) if coefficient < len(polynomials[j]) else 0
                for j in range(1, degree+1))
            require(majorant <= 3**(degree+1),
                    'Discrete Chebyshev coefficient-functional majorant has the claimed l1 bound')
            checks += 1
    budgets = []
    for n in (1, 2, 4, 8):
        r, length = 2**n, 54*n+6
        m = length+1
        # Representative b_an values check the symbolic formula, not its
        # physical-menu numerical value.  No value of C_an is assumed.
        b_an = (0, 1, 10**6, 10**12)[(1, 2, 4, 8).index(n)]
        c_h = 4_000_000+2*b_an
        s = c_h*m*r*r
        degree = 3*m
        smoothing = (1+F(216, s))**length-1
        tail = 18*(8*s)**length*s**m*2**(m+2)*F(6, s)**(degree+1)
        require(tail == F(186624, s**3)*F(3456, s)**length,
                'M=3m gives exactly the canonical 186624 s^-3 (3456/s)^L tail')
        require(smoothing <= F(432*length, s),
                'The exact word smoothing error satisfies the canonical linear bound')
        require(F(s, s-b_an)**m <= F(8, 3),
                'The finite Laplace amplification is below 8/3, itself a strict lower bound on e')
        allocation = F(1, 9216*r*r)
        require(smoothing <= allocation and tail <= allocation,
                'An explicit finite parameter choice fits smoothing and extraction-tail allocations')
        amplification = 18*(8*s)**length*s**m*3**(degree+1)
        require(amplification == 1458*s*(216*s*s)**length,
                'M=3m gives exactly the canonical 1458 s (216 s^2)^L noise amplification')
        # A normalized observation error, without assigning a value to C_an.
        observed_error = F(1, amplification*9216*r*r)
        require(amplification*observed_error <= allocation,
                'The remaining scalar observation-noise allocation is exact')
        basic_error = smoothing+tail+amplification*observed_error
        require(basic_error <= F(1, 3072*r*r) and 3*basic_error <= F(1, 1024*r*r),
                'The three budgets imply the canonical whole-word entropy hypothesis')
        budgets.append({'n': n, 'r': r, 'max_edges': length, 'm': m,
                        'representative_b_an': b_an, 'C_H': c_h,
                        's': s, 'interpolation_degree': degree,
                        'smoothing_below_allocation': smoothing <= allocation,
                        'tail_below_allocation': tail <= allocation,
                        'allocation_exact': str(allocation),
                        'noise_amplification_bit_length': amplification.bit_length(),
                        'scope': 'Canonical equations (18)-(21) bookkeeping at representative b_an values; no physical-menu analytic-continuation constant is numerically asserted.'})
    return {'max_Chebyshev_degree': 64, 'coefficient_majorant_checks': checks,
            'parameter_examples': budgets}


def central_states(n: int) -> list[tuple[tuple[int, ...], int, int]]:
    r = 2**n
    return [(table, address, sign) for table in itertools.product((-1, 1), repeat=r)
            for address in range(r) for sign in (-1, 1)]


def walsh_checks() -> list[dict]:
    reports = []
    for n in (1, 2):
        r, states = 2**n, central_states(n)

        def character(state: tuple[tuple[int, ...], int, int], mask: int) -> int:
            table, address, sign = state
            value = 1
            for bit in range(r):
                if mask & (1 << bit):
                    value *= sign*table[address ^ bit]
            return value

        for left in range(2**r):
            require(sum(character(state, left) for state in states) == (len(states) if left == 0 else 0),
                    'Every nonempty relative Walsh character has zero mean')
            # Apply physical multiplication blocks as sparse row operations.
            # M_f has hidden diagonal f and A-column -f; its A row is zero.
            # This avoids allocating a matrix on the central configuration set.
            row_a = F(1, 36)
            row_hidden = [F(-1, 36*len(states)) for _ in states]
            for bit in reversed(range(r)):
                if left & (1 << bit):
                    values = [character(state, 1 << bit) for state in states]
                    row_a = -sum((weight*value for weight, value in zip(row_hidden, values)), F())
                    row_hidden = [weight*value for weight, value in zip(row_hidden, values)]
            require(-36*row_a+int(left == 0) == 0,
                    'The physical left endpoint correction cancels its visible A component')
            require([-36*weight for weight in row_hidden] ==
                    [F(character(state, left), len(states)) for state in states],
                    'The corrected physical left row is the normalized relative Walsh density')
            for right in range(2**r):
                cross = sum(character(state, left)*character(state, right) for state in states)
                require(cross == (len(states) if left == right else 0),
                        'Relative Walsh characters are exactly orthonormal')
        for state in states:
            table, address, sign = state
            for bit in range(r):
                shifted = (table, address ^ bit, sign)
                require(sign*shifted[0][shifted[1]] == character(state, 1 << bit),
                        'Conjugated central multiplication returns the relative table bit')
                require(character(state, 1 << bit)**2 == 1, 'Each relative bit squares to one')
        reports.append({'n': n, 'addresses': r, 'central_triples_enumerated': len(states),
                        'Walsh_features': 2**r, 'scalar_Gram_pairs_checked': 4**r,
                        'physical_left_endpoint_cancellations_checked': 2**r,
                        'independent_port_hub_A_feature_count': 9*2**r+2,
                        'dense_feature_Gram_allocated': False})
    # Aggregate only the visible state, hub, and all nonhub hidden states.
    # This checks the two remaining physical endpoint identities exactly.
    pi = [F(1, 2), F(1, 4), F(1, 4)]
    y_hub = [[F(0)]*3, [F(1), F(-1), F(0)], [F(0)]*3]
    y_ports = [[F(0)]*3, [F(0)]*3, [F(1), F(0), F(-1)]]
    l_a = add(add(eye(3), y_hub), y_ports)
    left_a = mm([pi], l_a)[0]
    require(left_a == [F(1), F(0), F(0)], 'The physical reset polynomial supplies the A row')
    left_hub = [-4*x+y for x, y in zip(mm([pi], y_hub)[0], left_a)]
    require(left_hub == [F(0), F(1), F(0)], 'The hub endpoint removes its visible component')
    return reports


def one_bit_quotient_checks() -> dict:
    states = central_states(1)

    def quotient(state: tuple[tuple[int, ...], int, int]) -> tuple[int, int]:
        table, address, sign = state
        return sign*table[address], sign*table[address ^ 1]

    fibres = Counter(quotient(state) for state in states)
    require(len(fibres) == 4 and set(fibres.values()) == {4},
            'The one-address-bit target has four equal relative-table fibres')
    gate_maps: dict[str, dict[tuple[int, int], tuple[int, int]]] = {}
    for gate in ('J', 'V', 'X', 'F'):
        mapping = {}
        for state in states:
            table, address, sign = state
            if gate in ('J', 'V'):
                target = state  # Both reflections fix the sole register coordinate.
            elif gate == 'X':
                target = table, address ^ 1, sign
            else:
                changed = list(table)
                changed[address] *= -1
                target = tuple(changed), address, sign
            source, destination = quotient(state), quotient(target)
            if source in mapping:
                require(mapping[source] == destination, 'Every gate is constant on quotient fibres')
            mapping[source] = destination
        gate_maps[gate] = mapping
    require(all(gate_maps['X'][z] == (z[1], z[0]) and
                gate_maps['F'][z] == (-z[0], z[1]) for z in fibres),
            'The quotient retains address swap and independent current-bit flip')
    microscopic_mu, quotient_mu = F(1, 288), F(1, 72)
    require(4*microscopic_mu == quotient_mu, 'Four stationary microstates give each quotient weight')
    histogram: dict[F, F] = {F(0): F(1, 2)}
    for port in range(9):
        for relative in fibres:
            label = F(port+1, 100)*relative[0]
            histogram[label] = histogram.get(label, F())+quotient_mu
    require(sum(histogram.values()) == 1 and histogram[F(0)] == F(1, 2)
            and all(weight == F(1, 36) for label, weight in histogram.items() if label),
            'All nineteen actuator weights survive the exact quotient')
    for base in (F(1), F(11, 10), F(10, 11)):
        ratio = base**200
        pi_a = 1/(1+ratio)
        for port in range(9):
            for relative in fibres:
                exponent = (port+1)*relative[0]
                q_a = quotient_mu*base**(100+exponent)
                q_back = base**(exponent-100)
                pi_leaf = ratio*quotient_mu/(1+ratio)
                require(pi_a*q_a == pi_leaf*q_back,
                        'Quotient external rates keep the exact original exponential detailed balance')
                require(4*microscopic_mu*base**(100+exponent) == q_a,
                        'Four equal-label entrance rates sum to the prescribed quotient entrance rate')
        require(F(1, 2)*F(1, 36) == quotient_mu,
                'Hub-to-quotient rate is the sum of the four microscopic rates')
    return {'original_total_states_n1': 146, 'quotient_total_states_n1': 38,
            'relative_table_fibres': {str(z): count for z, count in sorted(fibres.items())},
            'quotient_leaf_mu_exact': str(quotient_mu), 'hub_mu_exact': '1/2',
            'hub_to_quotient_rate_exact': '1/36', 'gate_rate_exact': '1/16',
            'histogram_exact': {str(label): str(weight) for label, weight in sorted(histogram.items())},
            'scope': 'Gate equivariance, equal labels and exact fluxes verify this finite lumping. No dense 38-state generator or numerical rank is used.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/uncapped_observability.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    proof_sources = [root/'docs/BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md',
                     root/'docs/UNCAPPED_REVERSIBILITY_LOWER_BOUND.md',
                     root/'docs/UNCAPPED_WALSH_OBSERVABILITY.md']
    report = {
        'status': 'PASS', 'versions': {'python': platform.python_version()},
        'arithmetic': 'Python standard-library fractions.Fraction; exact integer enumeration; no floating-point matrices',
        'ordered_resolvent_parity': resolvent_parity_checks(),
        'positive_smoothed_flip': smoothed_flip_checks(),
        'Chebyshev_and_error_budget': chebyshev_and_budget_checks(),
        'relative_Walsh_orthogonality': walsh_checks(),
        'one_bit_exact_38_state_quotient': one_bit_quotient_checks(),
        'largest_dense_matrix_dimension': 7,
        'full_target_matrix_allocated': False,
        'limitations': [
            'Finite certificates do not prove the complete all-model analytic continuation, convexification, resolvent transfer or asymptotic lower theorem.',
            'The fixtures do not justify a fixed positive control clock: the new physical convexification argument uses arbitrarily short dwell times.',
            'The miniature smoothing example is not the complete nineteen-level target.',
            'The exact finite Walsh feature identities are checked, not a large numerical rank.'
        ],
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        'proof_snapshot_sha256': {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                                  for path in proof_sources},
        'imported_repository_verifiers': [],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
