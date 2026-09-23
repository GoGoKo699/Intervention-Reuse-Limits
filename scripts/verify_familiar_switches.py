#!/usr/bin/env python3
"""Exact finite certificates for familiar heat-bath switches and prediction order.

Rational generators, observable closure, derivative-Hankel identities and a
formal clock-menu certificate are checked without fitting trajectories or
computing a finite-accuracy threshold.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations, product
import hashlib
import json
from pathlib import Path
import platform


CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    work, row = [values[:] for values in a], 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][col]
        work[row] = [x/scale for x in work[row]]
        for i in range(len(a)):
            if i != row:
                scale = work[i][col]
                work[i] = [x-scale*y for x, y in zip(work[i], work[row])]
        row += 1
        if row == len(a):
            break
    return row


def determinant(a):
    work, value = [row[:] for row in a], F(1)
    for col in range(len(a)):
        pivot = next((i for i in range(col, len(a)) if work[i][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            value = -value
        scale = work[col][col]
        value *= scale
        for j in range(col+1, len(a)):
            factor = work[j][col]/scale
            for k in range(col+1, len(a)):
                work[j][k] -= factor*work[col][k]
    return value


def inverse(a):
    n = len(a)
    work = [a[i][:]+[F(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if work[i][col])
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [value/scale for value in work[col]]
        for row in range(n):
            if row != col:
                scale = work[row][col]
                work[row] = [x-scale*y for x, y in zip(work[row], work[col])]
    return [row[n:] for row in work]


def universal_predictor_checks():
    """Check physical rates and the proposed realization by independent formulas."""
    cases = []
    for t, m in product((F(1, 3), F(3, 5), F(4, 5), F(9, 10)),
                        (F(0), F(1, 3), F(3, 5), F(9, 10))):
        denominator = 1-t*t*m*m
        a, b = m*(1-t*t)/denominator, t*(1-m*m)/denominator
        require(denominator > 0 and 0 < t*b < 1 and a == (1-t*b)*m,
                'The rational hyperbolic parameters satisfy the stationary mean identity')
        readout = [-F(1), F(1), F(1)]
        auxiliary = [-t, -2*t, (1+t*t)/(2*t)]
        coordinates = [[F(1), s, z] for s, z in zip(readout, auxiliary)]
        reduced = [[F(0), a, F(0)], [F(0), -F(1), t], [F(0), b, -F(1)]]
        d, e = 3*t, (1-t*t)/(2*t)
        width, first_exit = d+e, (1+a-b*t)/2
        q21, q31 = (1-a+2*b*t)/2, (1-a-b*(t+e))/2
        rates = {(0, 1): first_exit*(2*t+e)/width,
                 (0, 2): first_exit*(d-2*t)/width,
                 (1, 0): q21, (1, 2): (d+q21*(2*t-d))/width,
                 (2, 0): q31, (2, 1): (e-q31*(2*t+e))/width}
        q = zeros(3)
        for (i, j), rate in rates.items():
            q[i][j] = rate
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(q == mm(mm(coordinates, reduced), inverse(coordinates)),
                'Explicit universal rates equal the independently conjugated mean generator')
        require(min(rates.values()) > 0 and all(sum(row) == 0 for row in q),
                'Every universal-family fixture is an irreducible generator with positive reverse rates')
        require(q31 == (1-t*t)*(1-m)**2/(4*denominator) and 0 < q31 <= (1-t*t)/4,
                'The potentially small return rate has the stated positive factorization')
        require(e-q31*(2*t+e) >= 3*(1-t*t)**2/(8*t) > 0,
                'The last internal rate satisfies its strict positivity margin')
        require(0 < q21 <= (1+2*t*t)/2 < F(3, 2) and t*(3-q21) > 0,
                'The other internal rate has a positive numerator')
        require(2*width-d-q21*(2*t+e) >= e/2 > 0,
                'The second-row cap is certified by the stated rational margin')
        exits = [-q[i][i] for i in range(3)]
        require(exits == [first_exit, (d+q21*(2*t+e))/width, (e+t*q31)/width]
                and exits[0] < 1 and exits[1] < 2 and exits[2] < 1,
                'All predictor exit rates satisfy the analytic cap bounds')
        law0 = [F(1, 2), e/(2*width), d/(2*width)]
        law = [weight*(1+m*s) for weight, s in zip(law0, readout)]
        require(sum(law) == 1 and min(law) > 0 and mm([law], q) == [[F(0)]*3],
                'The exact Gibbs-tilted law is normalized, positive and stationary')
        require(mm([law0], coordinates) == [[F(1), F(0), F(0)]]
                and mm([law], coordinates) == [[F(1), m, t*m]],
                'The universal predictor has the required initial and stationary coordinates')
        flux_defect = law[0]*q[0][1]-law[1]*q[1][0]
        require(m != 0 or flux_defect != 0,
                'The universal predictor violates ordinary detailed balance at zero field')

        # Build the physical four-state heat-bath chain from exp(2J), exp(2h),
        # independently of the reduced drift and predictor rate formulas.
        states = list(product((-1, 1), repeat=2))
        index = {state: i for i, state in enumerate(states)}
        coupling_bias, field_bias = (1+t)/(1-t), (1+m)/(1-m)
        target, weights = zeros(4), []
        for i, state in enumerate(states):
            weights.append(coupling_bias**int(state[0] == state[1])
                           *field_bias**int(state[0] == 1))
            for site in range(2):
                odds = coupling_bias**(state[site]*state[1-site])
                if site == 0:
                    odds *= field_bias**state[0]
                flipped = list(state)
                flipped[site] *= -1
                target[i][index[tuple(flipped)]] = 1/(1+odds)
            target[i][i] = -sum(target[i])
        target_law = [weight/sum(weights) for weight in weights]
        target_coordinates = [[F(1), F(s), F(z)] for s, z in states]
        require(mm(target, target_coordinates) == mm(target_coordinates, reduced),
                'The independently built physical heat-bath model has exactly the same mean closure')
        require(all(target_law[i]*target[i][j] == target_law[j]*target[j][i]
                    for i in range(4) for j in range(4)) and max(-target[i][i] for i in range(4)) < 2,
                'The physical target has ordinary detailed balance and the same exit cap')
        require(mm([target_law], target_coordinates) == [[F(1), m, t*m]],
                'The physical target stationary readout and hidden-spin means agree')

        initial_weights = [coupling_bias**int(s == z) for s, z in states]
        target_initial = [weight/sum(initial_weights) for weight in initial_weights]
        row, derivatives = target_initial, []
        for _ in range(5):
            derivatives.append(sum(row[i]*states[i][0] for i in range(4)))
            row = mm([row], target)[0]
        require(derivatives == [F(0), a, -a, a*(1+b*t), -a*(1+3*b*t)],
                'The single-high-field output derivatives have the claimed order-three form')
        hankel = [[derivatives[i+j] for j in range(3)] for i in range(3)]
        require(determinant(hankel) == a**3*b*t and (m == 0 or determinant(hankel) > 0),
                'Every nonzero-field fixture has a nonzero exact single-field Hankel determinant')
        require(t*(1-a*m) == b,
                'Detailed-balance moment arithmetic forces the auxiliary second moment to one')
        if m:
            require((t-a*t*m)/b == 1 and t*m/m == t and 1-t*t > 0,
                    'Both visible sectors in an ordinary rival require positive conditional variance')
        cases.append({'coupling_tanh_exact': str(t), 'field_tanh_exact': str(m),
                      'drift_coefficients_exact': [str(a), str(b)],
                      'predictor_stationary_law_exact': [str(x) for x in law],
                      'predictor_exit_rates_exact': [str(x) for x in exits],
                      'ordinary_stationary_flux_defect_exact': str(flux_defect),
                      'single_field_derivative_Hankel_determinant_exact': str(determinant(hankel)),
                      'required_ordinary_conditional_variance_exact': str(1-t*t)})
    return {'rational_parameter_fixtures': cases,
            'coupling_fixtures': 4, 'field_fixtures_per_coupling': 4,
            'positive_field_Hankel_certificates': 12,
            'nonreversibility_scope': 'The shared family is not reversible at zero field; some individual positive-field generators are reversible.',
            'scope': 'These 16 exact instances test the universal formulas and their positivity margins. The proof supplies positivity for every finite J>0, h>=0, fixed-clock rank, and the arbitrary-rival lower bound; a finite set of parameter checks does not prove those universal statements.'}


def spin_generator(n, alpha, field, coupled=True):
    states = list(product((-1, 1), repeat=n))
    index = {state: i for i, state in enumerate(states)}
    q = zeros(len(states))
    weights = []
    for i, state in enumerate(states):
        aligned = sum(state[j] == state[j+1] for j in range(n-1)) if coupled else 0
        weights.append(F(2)**(aligned+field*int(state[0] == 1)))
        for site in range(n):
            neighbor_sum = ((state[site-1] if site else 0)+(state[site+1] if site+1 < n else 0)) if coupled else 0
            exponent = state[site]*(neighbor_sum+(field if site == 0 else 0))
            rate = alpha[site]/(1+F(2)**exponent)
            changed = list(state)
            changed[site] *= -1
            q[i][index[tuple(changed)]] = rate
        q[i][i] = -sum(q[i])
    pi = [weight/sum(weights) for weight in weights]
    require(min(pi) > 0 and sum(pi) == 1, 'Every spin conformation has a positive stationary preparation weight')
    require(all(sum(row) == 0 for row in q), 'Heat-bath rows sum exactly to zero')
    require(all(q[i][j] >= 0 for i in range(len(q)) for j in range(len(q)) if i != j),
            'Every heat-bath transition rate is nonnegative')
    require(all(pi[i]*q[i][j] == pi[j]*q[j][i] for i in range(len(q)) for j in range(len(q))),
            'Heat-bath rates obey detailed balance with the exact Ising weights')
    require(mm([pi], q) == [[F(0)]*len(q)], 'The exact Gibbs preparation is stationary')
    require(max(-q[i][i] for i in range(len(q))) <= sum(alpha) <= n,
            'The total heat-bath exit rate is bounded by the sum of attempt rates')
    return states, q, pi


def closure_matrix(n, alpha, field):
    z_plus, z_minus = F(2)**(field+1), F(2)**(field-1)
    tanh_plus, tanh_minus = (z_plus-1)/(z_plus+1), (z_minus-1)/(z_minus+1)
    a, b = (tanh_plus+tanh_minus)/2, (tanh_plus-tanh_minus)/2
    reduced = zeros(n+1)
    reduced[0][1], reduced[1][1], reduced[2][1] = alpha[0]*a, -alpha[0], alpha[0]*b
    for site in range(1, n):
        reduced[site+1][site+1] = -alpha[site]
        if site == n-1:
            reduced[site][site+1] = alpha[site]/3
        else:
            reduced[site][site+1] = F(3, 10)*alpha[site]
            reduced[site+2][site+1] = F(3, 10)*alpha[site]
    return reduced


def controlled_spaces(qs, pi0, readout):
    reachable, prefixes, pointer = [pi0[:]], [()], 0
    while pointer < len(reachable):
        for field, q in enumerate(qs):
            candidate = mm([reachable[pointer]], q)[0]
            if rank(reachable+[candidate]) > len(reachable):
                reachable.append(candidate)
                prefixes.append(prefixes[pointer]+(field,))
        pointer += 1
    observable, suffixes, pointer = [readout[:]], [()], 0
    while pointer < len(observable):
        for field, q in enumerate(qs):
            candidate = [row[0] for row in mm(q, [[x] for x in observable[pointer]])]
            if rank(observable+[candidate]) > len(observable):
                observable.append(candidate)
                suffixes.append((field,)+suffixes[pointer])
        pointer += 1
    hankel = mm(reachable, transpose(observable))
    return reachable, observable, prefixes, suffixes, hankel


def familiar_chain_checks():
    cases = []
    two_spin_data = None
    for n, alpha in ((2, [F(1), F(1)]), (3, [F(1), F(2, 3), F(1, 2)])):
        qs, laws, closures = [], [], []
        for field in (0, 1):
            states, q, pi = spin_generator(n, alpha, field)
            coordinates = [[F(1)]+[F(x) for x in state] for state in states]
            reduced = closure_matrix(n, alpha, field)
            require(mm(q, coordinates) == mm(coordinates, reduced),
                    'Single-spin means and the constant form an exact invariant observable subspace')
            qs.append(q)
            laws.append(pi)
            closures.append(reduced)
        readout = [F(state[0]) for state in states]
        require(sum(x*y for x, y in zip(laws[0], readout)) == 0,
                'Neutral-field stationary preparation has zero mean output')
        reachable, observable, prefixes, suffixes, hankel = controlled_spaces(qs, laws[0], readout)
        require(len(observable) == n+1 and rank(hankel) == n+1,
                'The controlled mean series has exact linear order n+1')
        first = states.index(tuple([-1]*n))
        second_state = [-1]*n
        second_state[1] = 1
        second = states.index(tuple(second_state))
        opposite = [i for i, state in enumerate(states) if state[0] == 1]
        first_hazard, second_hazard = sum(qs[0][first][j] for j in opposite), sum(qs[0][second][j] for j in opposite)
        require(first_hazard == F(1, 3) and second_hazard == F(2, 3),
                'Equal visible spins can have different visible-flip hazards, so the visible partition is not strongly lumpable')
        cases.append({'spins': n, 'physical_states': 2**n, 'attempt_rates_exact': [str(x) for x in alpha],
                      'stationary_probabilities_exact': [[str(x) for x in law] for law in laws],
                      'closed_mean_coordinates': ['1']+[f's{i}' for i in range(n)],
                      'full_probability_reachable_rank': len(reachable), 'controlled_observable_rank': len(observable),
                      'generator_Hankel_rank': rank(hankel),
                      'independent_reachable_prefixes': [list(word) for word in prefixes],
                      'independent_observable_suffixes': [list(word) for word in suffixes],
                      'same_output_distinct_hazards_exact': [str(first_hazard), str(second_hazard)]})
        if n == 2:
            two_spin_data = states, qs, laws, closures
    return two_spin_data, {'cases': cases,
                          'scope': 'These are exact mean-closure and generator-word rank certificates. They do not identify a lower-dimensional Markov aggregation or prove any finite-accuracy state lower bound.'}


def three_state_predictor_checks(two_spin_data):
    states, target_qs, target_laws, reduced = two_spin_data
    rates = ((F(10, 27), F(2, 27), F(11, 18), F(43, 108), F(5, 18), F(29, 108)),
             (F(1, 4), F(1, 20), F(3, 4), F(3, 8), F(9, 20), F(1, 8)))
    readout, auxiliary = [F(1), -F(1), -F(1)], [F(1, 3), F(2, 3), -F(4, 3)]
    laws = [[F(1, 2), F(1, 4), F(1, 4)], [F(2, 3), F(1, 6), F(1, 6)]]
    coordinates = [[F(1), s, z] for s, z in zip(readout, auxiliary)]
    require(determinant(coordinates) != 0, 'The three predictor coordinates span its full state space')
    qs, flux_defects = [], []
    for field, off in enumerate(rates):
        q = zeros(3)
        for (i, j), value in zip(((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)), off):
            q[i][j] = value
        for i in range(3):
            q[i][i] = -sum(q[i])
        require(all(q[i][j] > 0 for i in range(3) for j in range(3) if i != j),
                'The smaller predictor has bidirectional positive support and hence finite ordinary stationary entropy production')
        require(max(-q[i][i] for i in range(3)) <= 2, 'The smaller predictor satisfies the target total-rate cap')
        require(mm([laws[field]], q) == [[F(0)]*3], 'The stated field-dependent predictor law is stationary')
        require(mm(q, coordinates) == mm(coordinates, reduced[field]),
                'Target and smaller predictor have identical closed mean generators at both fields')
        defect = laws[field][0]*q[0][1]-laws[field][1]*q[1][0]
        require(defect != 0, 'The smaller stationary predictor is not ordinarily reversible')
        flux_defects.append(str(defect))
        qs.append(q)
    require(laws[1] == [laws[0][i]*(1+readout[i]/3) for i in range(3)],
            'The predictor stationary laws have exactly the common readout Gibbs tilt')
    target_coordinates = [[F(1), F(state[0]), F(state[1])] for state in states]
    require(mm([target_laws[0]], target_coordinates) == mm([laws[0]], coordinates) == [[F(1), F(0), F(0)]],
            'The target and predictor have identical initial mean coordinates')
    prefixes = [(), (1,), (1, 0)]
    suffixes = [(), (0,), (1,)]
    def derivative_hankel(generators, law, output):
        rows = []
        for word in prefixes:
            row = law[:]
            for field in word:
                row = mm([row], generators[field])[0]
            rows.append(row)
        columns = []
        for word in suffixes:
            column = [[x] for x in output]
            for field in reversed(word):
                column = mm(generators[field], column)
            columns.append([row[0] for row in column])
        return mm(rows, transpose(columns))
    target_hankel = derivative_hankel(target_qs, target_laws[0], [F(state[0]) for state in states])
    predictor_hankel = derivative_hankel(qs, laws[0], readout)
    expected = [[F(0), F(0), F(3, 10)], [F(3, 10), -F(3, 10), -F(3, 10)],
                [-F(3, 10), F(1, 3), F(33, 100)]]
    require(target_hankel == predictor_hankel == expected, 'Both models have the same explicit derivative-Hankel witness')
    require(determinant(target_hankel) == F(3, 1000), 'A nonzero exact Hankel determinant proves minimal linear order three')
    return {'target_total_states': 4, 'predictor_total_states': 3,
            'predictor_readout_exact': [str(x) for x in readout],
            'predictor_auxiliary_coordinate_exact': [str(x) for x in auxiliary],
            'ordinary_stationary_flux_defects_exact': flux_defects,
            'derivative_Hankel_prefixes': [list(w) for w in prefixes],
            'derivative_Hankel_suffixes': [list(w) for w in suffixes],
            'derivative_Hankel_exact': [[str(x) for x in row] for row in expected],
            'derivative_Hankel_determinant_exact': '3/1000',
            'scope': 'Exact closure and matching initial coordinates certify all switched endpoint means in the stated two-field task. Binary-output path-law agreement is not asserted, and no numerical finite-accuracy threshold is computed.'}


def conditional_moment_obstruction_checks():
    coupling, a_high, b_high = F(1, 3), F(3, 10), F(3, 10)
    high_s = a_high/(1-coupling*b_high)
    high_z = coupling*high_s
    require(high_s == F(1, 3) and high_z == F(1, 9),
            'Stationarity of the recovered closed equations fixes the high-field first moments')
    second_zero = coupling/coupling
    second_high = (coupling-a_high*high_z)/b_high
    require(second_zero == second_high == 1,
            'Ordinary adjoint symmetry at both fields forces both auxiliary second moments to one')
    mixed_first = high_z/F(1, 3)
    mixed_second = (second_high-second_zero)/F(1, 3)
    require(mixed_first == F(1, 3) and mixed_second == 0,
            'The common readout Gibbs tilt fixes the zero-field mixed first and second moments')
    conditional_means = [mixed_first, -mixed_first]
    conditional_seconds = [second_zero+mixed_second, second_zero-mixed_second]
    variances = [second-mean*mean for second, mean in zip(conditional_seconds, conditional_means)]
    require(variances == [F(8, 9)]*2,
            'Both visible sectors would require strictly positive conditional auxiliary variance')
    require(all(variance > 0 for variance in variances) and 3 < 2+2,
            'Three physical states cannot provide two non-singleton visible sectors')
    return {'required_conditional_auxiliary_means_exact': [str(x) for x in conditional_means],
            'required_conditional_auxiliary_second_moments_exact': [str(x) for x in conditional_seconds],
            'required_conditional_auxiliary_variances_exact': [str(x) for x in variances],
            'ordinary_reversible_minimum_total_states': 4,
            'scope': 'This checks the rational moment contradiction conditional on the analytic minimal-realization argument recovering the closed coordinates in every exact three-state rival.'}


def aggregation_boundary_checks(two_spin_data):
    states, qs, laws, _ = two_spin_data
    minus = [i for i, state in enumerate(states) if state[0] == -1]
    plus = [i for i, state in enumerate(states) if state[0] == 1]
    pi, q = laws[0], qs[0]
    hazards = [sum(q[i][j] for j in plus) for i in minus]
    stationary_hazard = sum(pi[i]*hazard for i, hazard in zip(minus, hazards))/sum(pi[i] for i in minus)
    incoming = [sum(pi[j]*q[j][i] for j in plus) for i in minus]
    entry_hazard = sum(value*hazard for value, hazard in zip(incoming, hazards))/sum(incoming)
    require(stationary_hazard == F(4, 9) and entry_hazard == F(1, 2),
            'The coupled passive output has different stationary-conditioned and entry-conditioned hazards')
    projection = [[F(state[0] == -1), F(state[0] == 1)] for state in states]
    for field in (0, 1):
        _, neutral, neutral_pi = spin_generator(2, [F(1), F(1)], field, coupled=False)
        bias = F(2)**field
        reduced = [[-bias/(1+bias), bias/(1+bias)], [1/(1+bias), -1/(1+bias)]]
        require(mm(neutral, projection) == mm(projection, reduced),
                'Removing coupling gives a genuine exact two-state Markov projection at both fields')
        require(mm([neutral_pi], projection) == [[1/(1+bias), bias/(1+bias)]],
                'The uncoupled reduced equilibrium law has the correct controlled bias')
    return {'coupled_stationary_conditional_flip_hazard_exact': str(stationary_hazard),
            'coupled_entry_conditional_flip_hazard_exact': str(entry_hazard),
            'uncoupled_exact_Markov_quotient_states': 2,
            'scope': 'Neutral equilibrium gives a constant mean even when the coupled visible path is non-Markov. The exact two-state path reduction checked here uses zero coupling.'}


def finite_clock_menu_checks():
    # Field 1 denotes H, and field 0 denotes zero. The empty response is known
    # to be zero from the prescribed neutral preparation; it is not an experiment.
    menu = {(1,)*n for n in range(1, 6)}
    menu.update((1,)*i+(0,)+(1,)*j for i in (1, 2) for j in (0, 1, 2))
    require(len(menu) == 11, 'The proposed exact observation menu has eleven distinct words')
    require(max(map(len, menu)) == 5,
            'No word in the exact observation menu uses more than five ticks')
    runs = lambda word: 1+sum(a != b for a, b in zip(word, word[1:]))
    require(max(map(runs, menu)) == 3,
            'The finite observation menu needs at most three constant-field runs')
    known = menu | {()}
    for i, j in product(range(3), repeat=2):
        require((1,)*(i+j) in known,
                'Every base Hankel entry is measured or is the known initial response')
        require((1,)*(i+j+1) in known,
                'Every high-field shifted Hankel entry occurs in the menu')
        zero_shift_word = (1,)*i+(0,)+(1,)*j if i else (1,)*j
        require(zero_shift_word in known,
                'Every zero-field shifted entry is covered after neutral-preparation stationarity')

    # A tiny exact polynomial ring checks an identity, rather than sampling
    # putative clock exponentials. Variables are c0,c1,c2,x,y; m_n=c0+c1*x^n+c2*y^n.
    def add(left, right):
        result = left.copy()
        for power, coefficient in right.items():
            result[power] = result.get(power, F(0))+coefficient
            if not result[power]:
                del result[power]
        return result

    def multiply(left, right):
        result = {}
        for a, x in left.items():
            for b, y in right.items():
                power = tuple(i+j for i, j in zip(a, b))
                result[power] = result.get(power, F(0))+x*y
        return {power: coefficient for power, coefficient in result.items() if coefficient}

    one = {(0,)*5: F(1)}
    variables = [{tuple(int(i == j) for i in range(5)): F(1)} for j in range(5)]
    c0, c1, c2, x, y = variables

    def power(polynomial, exponent):
        result = one
        for _ in range(exponent):
            result = multiply(result, polynomial)
        return result

    def subtract(left, right):
        return add(left, {powers: -coefficient for powers, coefficient in right.items()})

    moments = [add(add(c0, multiply(c1, power(x, n))), multiply(c2, power(y, n)))
               for n in range(5)]
    formal_determinant = {}
    for permutation in permutations(range(3)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(3) for j in range(i+1, 3))
        term = {(0,)*5: F((-1)**inversions)}
        for i, j in enumerate(permutation):
            term = multiply(term, moments[i+j])
        formal_determinant = add(formal_determinant, term)
    factored = multiply(multiply(c0, c1), c2)
    for difference in (subtract(x, one), subtract(y, one), subtract(y, x)):
        factored = multiply(factored, power(difference, 2))
    require(formal_determinant == factored and bool(factored),
            'The three-exponential Hankel determinant equals the exact Vandermonde-square polynomial')
    return {'field_alphabet': {'0': 'zero field', '1': 'positive field H'},
            'mean_word_menu': [list(word) for word in sorted(menu, key=lambda word: (len(word), word))],
            'distinct_measured_words': 11, 'maximum_ticks': 5, 'maximum_constant_field_runs': 3,
            'reconstructed_matrices': ['G[i,j]=m(H^(i+j))',
                                       'G_H[i,j]=m(H^(i+j+1))',
                                       'G_0[i,j]=m(H^i 0 H^j)'],
            'formal_Hankel_determinant_identity': 'c0*c1*c2*(x-1)^2*(y-1)^2*(y-x)^2',
            'formal_polynomial_nonzero_terms': len(factored),
            'scope': 'Word coverage and the determinant identity are exact. Nonzero physical mode weights, distinct clock bases for every tick a>0, realization recovery and a positive but unquantified tolerance without a rival rate cap are established analytically in the proof; no exponential response values or error margin are computed here.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/familiar_switches.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    two_spin_data, chain_report = familiar_chain_checks()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact fractions.Fraction generator, moment, closure, Hankel and formal polynomial identities; no numerical optimization or floating dynamics',
              'heat_bath_chain_fixtures': chain_report,
              'universal_positive_three_state_family': universal_predictor_checks(),
              'exact_three_state_predictor': three_state_predictor_checks(two_spin_data),
              'ordinary_reversible_conditional_moment_obstruction': conditional_moment_obstruction_checks(),
              'mean_closure_and_Markov_aggregation_boundary': aggregation_boundary_checks(two_spin_data),
              'finite_clock_observation_menu': finite_clock_menu_checks(),
              'largest_dense_matrix_dimension': 8, 'large_target_allocated': False,
              'controlled_responses_simulated': False, 'experiment_menu_enumerated': True,
              'limitations': ['Finite exact checks supplement the analytic arbitrary-rival realization and reversibility arguments.',
                              'A closed system for single-spin means does not imply a smaller Markov state process.',
                              'Generator-Hankel entries are derivatives of mean responses; no finite measured-error threshold is inferred.',
                              'The exact three-state predictor preserves the specified controlled means, not the complete visible path law.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'proof_snapshot_sha256': {
                  name: hashlib.sha256((root/name).read_bytes()).hexdigest()
                  for name in ('docs/FAMILIAR_SWITCH_STRUCTURE.md',)
              },
              'imported_repository_verifiers': []}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
