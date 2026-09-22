#!/usr/bin/env python3
"""Check whole-side logarithm truncation and its polynomial state witness.

Exact checks cover noncommutative coefficient bookkeeping, factorization,
and an all-depth rational error calibration. Small actual propagators check
whole-word numerical consistency. No large protocol expansion or numerical
rank inference is used; the physical register construction is imported from
the existing shift-register verifier and its source hash is recorded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

import verify_shift_register_lower_bound as shift


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def nc_add(*terms):
    result = {}
    for scale, poly in terms:
        for word, value in poly.items():
            result[word] = result.get(word, 0) + scale * value
    return {word: value for word, value in result.items() if value}


def nc_mul(left, right):
    result = {}
    for a, av in left.items():
        for b, bv in right.items():
            word = a + b
            result[word] = result.get(word, 0) + av * bv
    return {word: value for word, value in result.items() if value}


def nc_series_mul(left, right, cutoff):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            if i+j <= cutoff:
                result[i+j] = nc_add((1, result.get(i+j, {})), (1, nc_mul(a, b)))
    return result


def nc_series_add(*terms):
    result = {}
    for scale, series in terms:
        for degree, poly in series.items():
            result[degree] = nc_add((1, result.get(degree, {})), (scale, poly))
    return {degree: poly for degree, poly in result.items() if poly}


def exact_formal_checks():
    cutoff, a = 5, sp.Rational(1, 8)
    Q = []
    for letter in (0, 1):
        Q.append({j: {(letter,)*ell: -sp.binomial(j, ell)*(-1)**ell/(a*j)
                      for ell in range(j+1)} for j in range(1, cutoff+1)})
    product = lambda x, y: nc_series_mul(x, y, cutoff)
    # A fixed three-factor example checks order without enumerating the
    # exponentially many protocols in the actual large-cutoff witness.
    P = nc_series_add((1, product(product(Q[0], Q[1]), Q[0])),
                      (2, product(Q[1], Q[0])), (-3, product(Q[0], Q[1])))
    E = [sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 3)], [0, sp.Rational(2, 3)]]),
         sp.Matrix([[sp.Rational(3, 4), 0], [sp.Rational(1, 5), sp.Rational(1, 4)]])]
    require(E[0]*E[1] != E[1]*E[0], 'Formal test matrices do not commute')

    def evaluate(poly):
        out = sp.zeros(2)
        for word, coefficient in poly.items():
            term = sp.eye(2)
            for letter in word:
                term = term*E[letter]
            out += coefficient*term
        return out

    qmat = [{j: -(sp.eye(2)-e)**j/(a*j) for j in range(1, cutoff+1)} for e in E]
    pm = series_add((1, series_mul(series_mul(qmat[0], qmat[1], cutoff), qmat[0], cutoff)),
                    (2, series_mul(qmat[1], qmat[0], cutoff)),
                    (-3, series_mul(qmat[0], qmat[1], cutoff)))
    require(all(evaluate(P[j]) == pm[j] for j in P), 'Exact ordered coefficient evaluation')
    require(all(len(word) <= j for j, poly in P.items() for word in poly),
            'Every propagator word length is at most total logarithm degree')
    require(product(product(Q[0], Q[1]), Q[0]) == product(Q[0], product(Q[1], Q[0])),
            'Truncated series multiplication is associative')
    # Whole-side truncation matters. A total-degree cut on matrix entries
    # can turn a rank-one factorization into rank two.
    z = sp.symbols('z')
    left, right = sp.Matrix([1, z]), sp.Matrix([[1, z]])
    separate = (left*right).subs(z, 1)
    entry_cut = (left*right).applyfunc(lambda p: sp.series(p, z, 0, 2).removeO()).subs(z, 1)
    require(separate.det() == 0 and entry_cut.det() == -1,
            'Separate side truncation preserves rank; direct entry truncation need not')
    return {'maximum_checked_total_degree': cutoff,
            'exact_noncommutative_order_and_associativity': True,
            'propagator_word_length_bounded_by_total_degree': True,
            'separate_factor_matrix_exact': str(separate),
            'incorrect_entry_cut_matrix_exact': str(entry_cut),
            'incorrect_entry_cut_has_rank_two_from_rank_one_factors': True,
            'scope': 'Small exact coefficient check only; no large protocol expansion.'}


def rational_calibration():
    z = sp.Rational(65, 64)
    u, c = (z-1/z)/2, (z+1/z)/2
    b, scalar = u/z, 1-c/z
    normalization = 4*u**3/z
    require((2+abs(scalar))/b < 256, 'Generator coefficient sum of each controlled letter <256')
    require(normalization > sp.Rational(1, 2**17), 'Exact mean normalization floor')
    # e^(5/8) is bounded by its first two terms and a geometric Taylor tail.
    x = sp.Rational(5, 8)
    exponential_upper = 1+x+x*x/(2*(1-x/3))
    require(exponential_upper < 2, 'Exact Taylor bound gives q=1-exp(-5/8)<1/2')
    # At analytic radius 3/2: ||Q(z)|| <= (65/64)*8*log(4)<32.
    require(z*8*2 < 32, 'Dimension-independent analytic generator bound')
    # The geometric ratio below certifies the error inequality at every
    # depth n>=1, not merely at the displayed finite sample depths.
    ratio_step = 2**67 * 48**4 * sp.Rational(2, 3)**200
    require(ratio_step < 1, 'All-depth error/floor ratio decreases geometrically')
    depth = sp.symbols('n', integer=True, positive=True)
    # These exponent identities establish the displayed bounds at every
    # depth, independently of the finite sample checks below:
    # 256^n * 32^(5n+3) = 2^(33n+15), and the formal weighted
    # coefficient sum is 256^n * 8^(5n+3) = 2^(23n+9).
    require(sp.expand(8*depth+5*(5*depth+3)-(33*depth+15)) == 0,
            'All-depth analytic side exponent identity')
    require(sp.expand(8*depth+3*(5*depth+3)-(23*depth+9)) == 0,
            'All-depth formal side exponent identity')
    # Since 48<64, the leaf floor is at least 2^(-24n-13).
    # Divide it by 2*2^n and by the entry coefficient bound
    # 2^(46n+35+4M), then substitute M=200(n+1).
    require(48 < 64, 'Power-of-two lower bound for the exact leaf floor')
    response_exponent = 24*depth+13 + 1+depth + 46*depth+35 + 4*200*(depth+1)
    require(sp.expand(response_exponent-(871*depth+849)) == 0,
            'All-depth simplified response exponent identity')
    records = []
    for n in (1, 2, 3, 10):
        cutoff = 200*(n+1)
        side_bound = sp.Integer(2)**(33*n+15)
        tail = 3*side_bound*sp.Rational(2, 3)**(cutoff+1)
        require(tail < side_bound, 'Truncated side error is below side norm bound')
        matrix_error = sp.Integer(2)**n * 3*side_bound*tail * 2**17
        gram_floor = sp.Rational(1, 2*48**(4*n+2))
        require(matrix_error < gram_floor/2, 'Exact rational error below half the leaf Gram floor')
        side_budget = sp.Integer(2)**(23*n+9+2*cutoff)
        entry_budget = side_budget**2 * 2**17
        response_floor = gram_floor/(2*2**n*entry_budget)
        explicit_floor = sp.Rational(1, 2**(871*n+849))
        require(response_floor >= explicit_floor, 'Explicit exponential-in-depth response floor')
        with mp.workdps(80):
            records.append({'word_depth_n': n, 'whole_side_degree_cutoff': cutoff,
                            'minimum_dwell': '1/8', 'maximum_horizon': str(sp.Rational(2*cutoff, 8)),
                            'side_analytic_bound_log2': 33*n+15,
                            'side_formal_coefficient_bound_log2': 23*n+9+2*cutoff,
                            'matrix_error_log10': shift.digits(mp.log10(shift.number(matrix_error))),
                            'exact_leaf_Gram_floor': str(gram_floor),
                            'error_below_half_Gram_floor_exact': True,
                            'response_floor_log10': shift.digits(mp.log10(shift.number(response_floor))),
                            'simplified_response_floor': '2^(-%d)' % (871*n+849)})
    return {'parameters': {'k': 1, 'G': 1, 'W': 1, 'exp_h': str(z), 'dwell_a': '1/8'},
            'analytic_radius': '3/2', 'formal_majorant_radius': '1/4',
            'exp_5_over_8_rational_upper': str(exponential_upper),
            'normalization_exact': str(normalization),
            'all_depth_cutoff_formula': 'M=200(n+1)',
            'all_depth_error_to_floor_ratio_multiplier': str(ratio_step),
            'all_depth_certificate': 'Base depth n=1 passes and the ratio decreases by the displayed exact factor at each depth.',
            'all_depth_response_floor': '2^(-871n-849), n>=1',
            'all_depth_protocol_horizon': '50(n+1), with each positive segment a multiple of 1/8',
            'records': records,
            'scope': 'A conservative exact rational calibration at one fixed field/dwell; arbitrary fixed dwell is covered analytically in the theorem.'}


def series_add(*terms):
    out = {}
    for scale, series in terms:
        for j, value in series.items():
            out[j] = scale*value if j not in out else out[j]+scale*value
    return out


def series_mul(left, right, cutoff):
    out = {}
    for i, a in left.items():
        for j, b in right.items():
            if i+j <= cutoff:
                term = a*b
                out[i+j] = term if i+j not in out else out[i+j]+term
    return out


def numerical_whole_side(data):
    records = []
    with mp.workdps(70):
        Q0, Qh = shift.matrix(data['Q0']), shift.matrix(data['Qh'])
        size, z = Q0.rows, shift.number(data['z'])
        a, cutoff = mp.mpf(1)/8, 40
        identity = mp.eye(size)
        u, c = (z-1/z)/2, (z+1/z)/2
        scalar, b = 1-c/z, u/z
        normalization = -4*u**3/z
        E = [mp.expm(a*Q) for Q in (Q0, Qh)]
        series_Q = []
        for e in E:
            X, power, coefficients = identity-e, identity, {}
            for j in range(1, cutoff+1):
                power = power*X
                coefficients[j] = -power/(a*j)
            series_Q.append(coefficients)
        sq0, sqh = series_Q
        mul = lambda first, second: series_mul(first, second, cutoff)
        F = series_add((mp.mpf(1)/3, mul(sq0, sq0)), (mp.mpf(2)/3, sq0))
        V = series_add((1, sqh), (-1, sq0), (-scalar, {0: identity}))
        letters = [mul(F, F), series_add((-1/b, mul(mul(F, V), F)))]
        left_series = [mul(mul(sqh, F), letter) for letter in letters]
        right_series = [mul(mul(letter, F), sqh) for letter in letters]
        exact_F = Q0*(Q0+2*identity)/3
        exact_Z = [exact_F*exact_F,
                   -exact_F*(Qh-Q0-scalar*identity)*exact_F/b]
        p0, S = mp.matrix([[mp.mpf(1)/2, mp.mpf(1)/2]+[0]*(size-2)]), mp.matrix([-1, 1]+[0]*(size-2))
        exact_left = [p0*Qh*exact_F*letter for letter in exact_Z]
        exact_right = [letter*exact_F*Qh*S for letter in exact_Z]
        exact_H = mp.matrix([[(row*column)[0]/normalization for column in exact_right]
                             for row in exact_left])
        previous = None
        for M in (12, 24, 40):
            def evaluate(series):
                total = mp.zeros(size)
                for j, value in series.items():
                    if j <= M:
                        total += value
                return total
            left = [p0*evaluate(series) for series in left_series]
            right = [evaluate(series)*S for series in right_series]
            H = mp.matrix([[(row*column)[0]/normalization for column in right] for row in left])
            error = shift.frobenius(H-exact_H)
            require(previous is None or error < previous, 'Whole-side truncation converges in selected physical example')
            previous = error
            records.append({'whole_side_cutoff': M, 'maximum_propagator_factors_per_entry': 2*M,
                            'maximum_protocol_horizon': str(2*M*a),
                            'controlled_matrix_Frobenius_error': shift.digits(error),
                            'full_generator_dimension': size, 'decimal_precision': 70})
        require(previous < mp.mpf('1e-10'), 'High-precision whole-word evaluation agrees with exact target statistic')
    return {'records': records,
            'scope': 'Small actual-propagator consistency only, not a numerical rank proof or interval certificate. The small register is not the n=1 leaf witness.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/polynomial_controlled_lower_bound.json'))
    args = parser.parse_args()
    data, physical = shift.physical_register(2)
    report = {'status': 'PASS',
              'scope': 'Whole-side noncommutative logarithm truncation, exact all-depth calibration, and small actual-propagator consistency.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__, 'mpmath': mp.__version__},
              'exact_formal_checks': exact_formal_checks(),
              'exact_rational_calibration': rational_calibration(),
              'reused_small_physical_register_check': physical,
              'reused_sparse_leaf_Gram_checks': [shift.sparse_leaf_check(n) for n in (1, 2)],
              'actual_propagator_whole_side_checks': numerical_whole_side(data),
              'largest_constructed_physical_generator_dimension': 5,
              'largest_constructed_controlled_Gram_dimension': 4,
              'no_large_physical_enumeration_or_numerical_rank_tests': True,
              'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in (Path(__file__), Path(shift.__file__))}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
