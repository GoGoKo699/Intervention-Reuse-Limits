#!/usr/bin/env python3
"""Exact small checks for the five-color, fifteen-symbol obstruction.

Only N=3,4,6 are instantiated, with at most 20 states. These values make
every transition probability rational. The unbounded dimension conclusion
is proved in the companion note, not inferred by finite enumeration.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp

Q = sp.Rational


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def exact_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def check_target(n: int) -> dict:
    size = 3*n+2
    one, pi = sp.ones(size, 1), sp.Matrix([[Q(1, 5*n)]*(3*n)+[Q(1, 5)]*2])
    weight = sp.diag(*pi)
    p, star = sp.zeros(size), sp.zeros(size)
    colors = [j for j in range(3) for _ in range(n)]+['+', '-']
    d = {c: sp.diag(*[int(value == c) for value in colors]) for c in (0, 1, 2, '+', '-')}
    cosine = [sp.expand_trig(sp.cos(2*sp.pi*a/n)) for a in range(n)]
    require(all(value.is_Rational for value in cosine), 'Chosen instances have exact rational transition entries')
    for j in range(3):
        for a in range(n):
            i = j*n+a
            p[i, i] = Q(1, 2)
            for sign, last in ((1, 3*n), (-1, 3*n+1)):
                p[i, last] = (1+sign*cosine[a]/2)/8
                p[last, i] = p[i, last]/n
                star[i, last], star[last, i] = Q(1, 8), Q(1, 8*n)
    for a in range(n):
        for i, j in ((a, n+(-a) % n), (n+a, 2*n+(1-a) % n), (2*n+a, a)):
            p[i, j] = p[j, i] = Q(1, 8)
    p[3*n, 3*n] = p[3*n+1, 3*n+1] = Q(5, 8)
    for i in range(size):
        star[i, i] = -sum(star[i, j] for j in range(size) if j != i)
    require(p*one == one and all(value >= 0 for value in p), 'Exact Markov rows')
    require(pi*p == pi and weight*p == p.T*weight, 'Exact stationary detailed balance')
    require(all((pi*d[c]*one)[0] == Q(1, 5) for c in d), 'All five color masses equal one fifth')
    require(all(p[i, 3*n] >= Q(1, 16) for i in range(3*n)), 'One readout connects every address, proving irreducibility')
    lazy_remainder = 2*p-sp.eye(size)
    require(all(value >= 0 for value in lazy_remainder) and lazy_remainder*one == one,
            'Half-laziness certifies the relaxation cap without floating-point eigenvalues')
    star_spectrum = (-star).eigenvals()
    require(star_spectrum == {sp.Integer(0): 1, Q(1, 4): 3*n-1, Q(3, 8): 1, Q(5, 8): 1},
            'Exact comparison-star relaxation spectrum')
    comparison = p-sp.eye(size)-star/2
    require(comparison*one == sp.zeros(size, 1) and weight*comparison == comparison.T*weight,
            'Dirichlet comparison remainder is reversible with zero row sums')
    require(all(comparison[i, j] >= 0 for i in range(size) for j in range(size) if i != j),
            'Nonnegative comparison conductances certify gap at least one eighth')

    cache = {}

    def probability(word: tuple) -> sp.Expr:
        if word not in cache:
            vector = d[word[-1]]*one
            for c in reversed(word[:-1]):
                vector = d[c]*p*vector
            cache[word] = (pi*vector)[0]
        return cache[word]

    def inner_words(first: tuple, second: tuple) -> sp.Expr:
        return sp.Integer(0) if first[0] != second[0] else probability(first[::-1]+second[1:])

    def prefix_norm(terms: dict[tuple, sp.Expr]) -> sp.Expr:
        return sp.simplify(sum(x*y*inner_words(u, v) for u, x in terms.items() for v, y in terms.items()))

    transports = {}
    row_records = []
    for c in range(3):
        for e in range(3):
            if c == e:
                continue
            transports[c, e] = 8*d[c]*p*d[e]
            row = transports[c, e]*one
            require(row == d[c]*one, 'Each extracted transport has unit rows on its port')
            require(weight*transports[c, e] == (8*d[e]*p*d[c]).T*weight,
                    'Reverse transport is the weighted adjoint')
            require(probability((c, e)) == Q(1, 40) and probability((e, c, e)) == Q(1, 320),
                    'Two- and three-symbol probabilities force zero rival row variance')
            require((5*row.T*weight*row)[0] == 1 and 40*probability((c, e)) == 1,
                    'Conditional first and second moments both equal one')
            row_records.append({'ports': [c, e], 'two_symbol_probability_exact': '1/40',
                                'three_symbol_probability_exact': '1/320'})

    cycle = transports[0, 2]*transports[2, 1]*transports[1, 0]
    expected = sp.zeros(size)
    for a in range(n):
        expected[a, (a-1) % n] = 1
    require(cycle == expected, 'Positive observable cycle is the one-step address rotation')
    feature = 16*d[0]*p*d['+']*one-2*d[0]*one
    require(feature == sp.Matrix(cosine+[0]*(size-n)), 'Physical color-prefix feature is cosine on port zero')
    feature_terms = {(0, '+'): sp.Integer(16), (0,): sp.Integer(-2)}
    norm = (feature.T*weight*feature)[0]
    require(norm == Q(1, 10) and prefix_norm(feature_terms) == norm,
            'Three-symbol data recover the nonzero feature norm')
    recurrence = (cycle*cycle-2*cosine[1]*cycle+d[0])*feature
    require(recurrence == sp.zeros(size, 1), 'Exact second-order observable recurrence')
    terms = {}
    for power, coefficient in ((2, 1), (1, -2*cosine[1]), (0, 1)):
        for word, value in feature_terms.items():
            expanded_word = (0, 2, 1)*power+word
            terms[expanded_word] = terms.get(expanded_word, 0)+coefficient*512**power*value
    require(prefix_norm(terms) == 0, 'Zero recurrence norm is exactly a linear combination of prefix probabilities')
    longest = max(len(u)+len(v)-1 for u in terms for v in terms)
    require(longest == 15 and max(len(word) for word in cache) == 15,
            'No observation beyond fifteen symbols enters the norm witness')

    zeta = sp.expand_complex(sp.exp(2*sp.pi*sp.I/n))
    vector = (cycle-sp.conjugate(zeta)*d[0])*feature
    require(not exact_zero(vector) and exact_zero(cycle*vector-zeta*vector),
            'The nonzero recurrence feature gives a peripheral primitive-root eigenvector')
    orders = [ell for ell in range(1, n+1) if sp.simplify(sp.expand_complex(zeta**ell)-1) == 0]
    require(orders == [n], 'The extracted unit-modulus eigenvalue has exact order N')
    current, visited = 0, []
    while current not in visited:
        visited.append(current)
        successors = [j for j in range(n) if cycle[current, j] > 0]
        require(len(successors) == 1, 'Target cycle has one positive successor per state')
        successor = successors[0]
        require(sp.simplify(vector[successor]-zeta*vector[current]) == 0,
                'Exact peripheral phase advances along each positive target edge')
        current = successor
    require(current == 0 and len(visited) == n, 'The positive cycle visits exactly N actual port states')
    return {'N': n, 'states': size, 'stationary_color_mass_exact': '1/5',
            'comparison_star_spectrum_exact': {str(value): count for value, count in star_spectrum.items()},
            'certified_relaxation_interval_exact': ['1/8', '1'],
            'transport_moments': row_records, 'feature_squared_norm_exact': '1/10',
            'recurrence_squared_norm_exact': '0', 'longest_prefix_symbols': longest,
            'distinct_prefix_probabilities_evaluated': len(cache),
            'primitive_root_order': n, 'positive_cycle_length': len(visited)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/exact_reversible_prefix_obstruction.json'))
    args = parser.parse_args()
    report = {'status': 'PASS',
              'scope': 'Exact rational five-color examples, spectral certificates, reversible prefix-to-norm identities, and the fifteen-symbol primitive-root witness.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'instances': [check_target(n) for n in (3, 4, 6)],
              'largest_matrix_dimension': 20,
              'limitations': 'Finite examples check the construction and witness identities. The theorem for all N and all reversible rivals uses the analytic zero-variance and maximum-modulus arguments. This is exact prefix realization, not a positive-error controlled-mean lower bound.',
              'provenance': 'Fresh verifier reconstructed after workspace recovery; no claim of byte identity with the inaccessible earlier script.',
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
