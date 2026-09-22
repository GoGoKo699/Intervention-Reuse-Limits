#!/usr/bin/env python3
"""Exact finite checks for reversible compression of the address dictionary.

Address collisions are solved over F2, and scenery is assigned only to visited
address classes. Huge registers and configuration dictionaries are never built.
Small selected physical models verify whole-configuration reweighting exactly.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import sympy as sp


LETTERS = ('J', 'V', 'X')
IDENTITY = (1, 0, ())
CHOICES = (('H', F(5, 8)), ('M', F(1, 8)), ('+', F(1, 8)), ('-', F(1, 8)))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def compose(left, right):
    e, a, lamps = left
    f, b, other = right
    shifted = {e*x+a for x in other}
    return e*f, a+e*b, tuple(sorted(set(lamps) ^ shifted))


def inverse(transform):
    e, a, lamps = transform
    return e, -e*a, tuple(sorted(e*(x-a) for x in lamps))


def generator(letter):
    return {'J': (-1, -1, ()), 'V': (-1, 0, ()), 'X': (1, 0, (0,))}[letter]


def normal_form(word):
    result = IDENTITY
    for letter in word:
        result = compose(generator(letter), result)
    return result


def finite_action(transform, value, width):
    e, a, lamps = transform
    result = 0
    for i in range(width):
        if value & (1 << i):
            result ^= 1 << ((e*i+a) % width)
    for lamp in lamps:
        result ^= 1 << (lamp % width)
    return result


def literal_action(letter, value, width):
    if letter == 'X':
        return value ^ 1
    result = 0
    for i in range(width):
        target = -i-1 if letter == 'J' else -i
        if value & (1 << i):
            result ^= 1 << (target % width)
    return result


def lamp_mask(transform, width):
    mask = 0
    for coordinate in transform[2]:
        mask ^= 1 << (coordinate % width)
    return mask


def equality_rows(first, second, width):
    e, a, _ = first
    f, b, _ = second
    rhs = lamp_mask(first, width) ^ lamp_mask(second, width)
    return tuple((1 << ((e*(i-a)) % width)) ^ (1 << ((f*(i-b)) % width))
                 | (((rhs >> i) & 1) << width) for i in range(width))


def solve_probability(rows, width):
    """Exact uniform-input probability of an affine binary equation system."""
    basis = {}
    variable_mask = (1 << width)-1
    for row in rows:
        while row & variable_mask:
            pivot = (row & variable_mask).bit_length()-1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
        else:
            if row >> width:
                return F(0), len(basis), False
    return F(1, 2**len(basis)), len(basis), True


def affine_checks():
    literal_cases = 0
    words = [word for length in range(5) for word in itertools.product(LETTERS, repeat=length)]
    for word in words:
        transform = normal_form(word)
        require(abs(transform[1]) <= len(word) and all(abs(x) <= len(word) for x in transform[2]),
                'Formal translation and transported-toggle bounds')
        require(compose(transform, inverse(transform)) == IDENTITY
                and compose(inverse(transform), transform) == IDENTITY, 'Exact affine inverse')
        for width in range(1, 7):
            count = 0
            for value in range(1 << width):
                current = value
                for letter in word:
                    current = literal_action(letter, current, width)
                require(current == finite_action(transform, value, width), 'Chronological normal form agrees with literal finite gates')
                count += current == value
                literal_cases += 1
            probability, _, _ = solve_probability(equality_rows(transform, IDENTITY, width), width)
            require(probability == F(count, 1 << width), 'Affine F2 collision probability equals exhaustive small-address counting')
    records = []
    for width in (9, 17, 65, 257):
        maximum_nonidentity = F(0)
        for word in words:
            transform = normal_form(word)
            equations = equality_rows(transform, IDENTITY, width)
            probability, _, consistent = solve_probability(equations, width)
            _, rank, _ = solve_probability(tuple(row & ((1 << width)-1) for row in equations), width)
            if transform == IDENTITY:
                require(probability == 1, 'Formal identities remain exact at every width')
            else:
                require(probability*probability*2**(width-2) <= 1, 'Every nonidentity relative word obeys the advertised collision bound')
                maximum_nonidentity = max(maximum_nonidentity, probability)
                if transform[0] == -1:
                    require(2*rank >= width-2, 'Reflection rank lower bound')
                elif transform[1]:
                    require(2*rank >= width, 'Nonidentity rotation rank lower bound')
                else:
                    require(not consistent, 'A nonzero finite lamp vector cannot fix an address')
        records.append({'register_width': width, 'address_space_enumerated': False,
                        'largest_exact_nonidentity_collision_probability': str(maximum_nonidentity)})
    return {'formal_words_checked': len(words), 'maximum_word_length': 4,
            'literal_small_address_evaluations': literal_cases,
            'small_register_widths': list(range(1, 7)), 'large_width_rank_checks': records,
            'convention': 'J:i->-i-1, V=RJ:i->-i, X toggles bit0; actions compose chronologically.'}


def set_partitions(length):
    def extend(prefix):
        if len(prefix) == length:
            yield tuple(prefix)
        else:
            for value in range(max(prefix, default=-1)+2):
                yield from extend(prefix+[value])
    return list(extend([]))


def formal_partition(transforms):
    known = {}
    result = []
    for transform in transforms:
        if transform not in known:
            known[transform] = len(known)
        result.append(known[transform])
    return tuple(result)


@lru_cache(None)
def equality_partition_law(transforms, width):
    length = len(transforms)
    pairs = list(itertools.combinations(range(length), 2))
    rows = {pair: equality_rows(transforms[pair[0]], transforms[pair[1]], width) for pair in pairs}

    @lru_cache(None)
    def probability(edges):
        return solve_probability(tuple(row for pair in edges for row in rows[pair]), width)[0]

    result = {}
    for partition in set_partitions(length):
        blocks = [[i for i, value in enumerate(partition) if value == block]
                  for block in range(max(partition)+1)]
        required = [(block[0], i) for block in blocks for i in block[1:]]
        forbidden = [(first[0], second[0]) for first, second in itertools.combinations(blocks, 2)]
        value = F(0)
        for bits in itertools.product((0, 1), repeat=len(forbidden)):
            edges = tuple(sorted(required+[pair for pair, bit in zip(forbidden, bits) if bit]))
            value += (-1)**sum(bits)*probability(edges)
        require(value >= 0, 'Equality-partition inclusion-exclusion gives nonnegative exact probabilities')
        if value:
            result[partition] = value
    require(sum(result.values(), F(0)) == 1, 'Address-equivalence partition probabilities sum to one')
    return tuple(result.items())


def add_scenery_law(out, partition, ports, weight):
    blocks = max(partition)+1
    # Uniform initial sigma can be absorbed into independent fair table signs.
    for signs in itertools.product((-1, 1), repeat=blocks):
        word = tuple((port+1)*signs[block] for port, block in zip(ports, partition))
        out[word] = out.get(word, F(0))+weight/F(2**blocks)


@lru_cache(None)
def annealed_local_law(width, updates):
    out = {}
    for initial in range(3):
        for choices in itertools.product(CHOICES, repeat=updates):
            port, transform, weight = initial, IDENTITY, F(1, 3)
            ports, transforms = [port], [transform]
            for choice, probability in choices:
                weight *= probability
                if choice == 'M':
                    transform = compose(generator(LETTERS[port]), transform)
                elif choice == '+':
                    port = (port+1) % 3
                elif choice == '-':
                    port = (port-1) % 3
                ports.append(port)
                transforms.append(transform)
            if width is None:
                partitions = ((formal_partition(transforms), F(1)),)
            else:
                partitions = equality_partition_law(tuple(transforms), width)
            for partition, probability in partitions:
                add_scenery_law(out, partition, ports, weight*probability)
    require(sum(out.values(), F(0)) == 1, 'Annealed six-symbol local prefix law is normalized')
    return out


def tv(first, second):
    return sum((abs(first.get(key, F(0))-second.get(key, F(0)))
                for key in set(first) | set(second)), F(0))/2


def refresh_law(width, updates):
    out = {}
    for flags in itertools.product((0, 1), repeat=updates):
        weight = F(3, 5)**sum(flags)*F(2, 5)**(updates-sum(flags))
        lengths, length = [], 1
        for flag in flags:
            if flag:
                lengths.append(length)
                length = 1
            else:
                length += 1
        lengths.append(length)
        require(sum(size*(size-1)//2 for size in lengths) <= updates*(updates+1)//2,
                'Refresh runs do not add a prefix-length factor to the collision pair budget')
        product_law = {(): weight}
        for size in lengths:
            next_law = {}
            for prefix, mass in product_law.items():
                for suffix, probability in annealed_local_law(width, size-1).items():
                    next_law[prefix+suffix] = mass*probability
            product_law = next_law
        for word, mass in product_law.items():
            out[word] = out.get(word, F(0))+mass
    require(sum(out.values(), F(0)) == 1, 'Full-refresh prefix law is normalized')
    return out


def prefix_checks():
    records = []
    for updates in (1, 2):
        width = 4*updates+1
        universal = annealed_local_law(None, updates)
        first = annealed_local_law(width, updates)
        second = annealed_local_law(width+1, updates)
        bad = updates*(updates+1)//2
        distance = tv(first, universal)
        between = tv(first, second)
        full_distance = tv(refresh_law(width, updates), refresh_law(width+1, updates))
        require(distance**2*2**(width-2) <= bad*bad, 'Exact law satisfies its one-width collision budget')
        require(between**2*2**(width-2) <= (2*bad)**2, 'Exact two-width local prefix bound')
        require(full_distance**2*2**(width-2) <= (2*bad)**2, 'Exact global-refresh prefix bound without an extra length factor')
        records.append({'local_updates': updates, 'compared_widths': [width, width+1],
                        'potential_choice_paths_per_width': 3*4**updates,
                        'large_address_spaces_enumerated': False,
                        'local_TV_to_universal_exact': str(distance),
                        'local_TV_between_widths_exact': str(between),
                        'full_refresh_TV_between_widths_exact': str(full_distance),
                        'between_width_bound': '%d * 2^(-(%d-2)/2)' % (2*bad, width),
                        'six_symbol_word_probabilities_exact': True})
    # Independent small brute force verifies the equality-partition engine.
    checked = 0
    for word in itertools.product(LETTERS, repeat=2):
        transforms = [IDENTITY]
        for letter in word:
            transforms.append(compose(generator(letter), transforms[-1]))
        for width in (2, 3, 4):
            brute = {}
            for value in range(1 << width):
                addresses = [finite_action(t, value, width) for t in transforms]
                groups, partition = {}, []
                for address in addresses:
                    if address not in groups:
                        groups[address] = len(groups)
                    partition.append(groups[address])
                key = tuple(partition)
                brute[key] = brute.get(key, F(0))+F(1, 1 << width)
            require(brute == dict(equality_partition_law(tuple(transforms), width)), 'Equality-partition law matches independent exhaustive address enumeration')
            checked += 1
    return {'records': records, 'independent_small_partition_laws_checked': checked,
            'scenery_handling': 'Assign one fair sign per distinct visited address class, reusing it on every revisit; no full scenery table is enumerated.'}


def component_law(width, table, updates):
    out = {}
    addresses = 1 << width
    for port, sigma, value in itertools.product(range(3), (-1, 1), range(addresses)):
        for choices in itertools.product(CHOICES, repeat=updates):
            current_port, current, weight = port, value, F(1, 6*addresses)
            word = [sigma*(current_port+1)*table[current]]
            for choice, probability in choices:
                weight *= probability
                if choice == 'M':
                    current = literal_action(LETTERS[current_port], current, width)
                elif choice == '+':
                    current_port = (current_port+1) % 3
                elif choice == '-':
                    current_port = (current_port-1) % 3
                word.append(sigma*(current_port+1)*table[current])
            key = tuple(word)
            out[key] = out.get(key, F(0))+weight
    return out


def mixture(laws, weights):
    out = {}
    for law, weight in zip(laws, weights):
        for word, value in law.items():
            out[word] = out.get(word, F(0))+weight*value
    return out


def component_generator(width, table):
    addresses = 1 << width
    states = list(itertools.product(range(3), (-1, 1), range(addresses)))
    index = {state: i for i, state in enumerate(states)}
    size = len(states)
    U, Port = sp.zeros(size), sp.zeros(size)
    for i, (port, sigma, value) in enumerate(states):
        U[i, index[(port, sigma, literal_action(LETTERS[port], value, width))]] = 1
        for other in range(3):
            if other != port:
                Port[i, index[(other, sigma, value)]] = 1
        Port[i, i] = -2
    L = (U-sp.eye(size)+Port)/8
    require(U == U.T and U*U == sp.eye(size), 'Matching gates are ordinary selfadjoint involutions')
    require(L == L.T and L*sp.ones(size, 1) == sp.zeros(size, 1), 'Complete component generator is symmetric and conservative')
    require(2*(sp.eye(size)+U) == (sp.eye(size)+U).T*(sp.eye(size)+U), 'Matching cap certificate is a Gram square')
    port_sum = sp.zeros(2*addresses, size)
    for row, (sigma, value) in enumerate(itertools.product((-1, 1), range(addresses))):
        for port in range(3):
            port_sum[row, index[(port, sigma, value)]] = 1
    require(sp.Rational(5, 8)*sp.eye(size)+L
            == ((sp.eye(size)+U).T*(sp.eye(size)+U)/2+port_sum.T*port_sum)/8,
            'Exact sum-of-squares local spectral-cap certificate at 5/8')
    labels = [sigma*(port+1)*table[value] for port, sigma, value in states]
    return L, labels


def selected_physical(width, tables, weights):
    components = [component_generator(width, table) for table in tables]
    size = 6*(1 << width)
    N = size*len(tables)
    require(N+1 <= 68, 'Selected physical generator stays within the small-matrix budget')
    L = sp.diag(*(item[0] for item in components))
    labels = [label for _, component_labels in components for label in component_labels]
    mu = sp.Matrix([[sp.Rational(weight.numerator, weight.denominator)/size
                     for weight in weights for _ in range(size)]])
    Pi = sp.ones(N, 1)*mu
    K = L+sp.Rational(3, 2)*(Pi-sp.eye(N))
    D = sp.diag(*mu)
    require(D*K == K.T*D and mu*K == sp.zeros(1, N), 'Weighted configuration mixture and refresh obey ordinary detailed balance')
    require(all(K[i, j] > 0 for i in range(N) for j in range(N) if i != j), 'Restored refresh makes every physical internal edge positive')
    require(all(sum(mu[i] for i, value in enumerate(labels) if value == label) == sp.Rational(1, 6)
                for label in (-3, -2, -1, 1, 2, 3)), 'Whole configurations preserve the exact six-level histogram')
    local_prefix = mixture([component_law(width, table, 1) for table in tables], weights)
    full_clock = sp.eye(N)+sp.Rational(2, 5)*K
    for first, second in itertools.product((-3, -2, -1, 1, 2, 3), repeat=2):
        observed = sum(mu[i]*full_clock[i, j] for i in range(N) for j in range(N)
                       if labels[i] == first and labels[j] == second)
        expected = F(2, 5)*local_prefix.get((first, second), F(0))+F(3, 5)*F(1, 36)
        require(observed == sp.Rational(expected.numerator, expected.denominator),
                'The selected physical full clock matches the exact local/refresh prefix decomposition')
    center = sp.eye(N)-Pi
    require(-D*K-sp.Rational(3, 2)*(D-mu.T*mu) == -D*L, 'Exact lower-band Dirichlet identity')
    require(sp.Rational(17, 8)*(D-mu.T*mu)+D*K
            == center.T*D*(sp.Rational(5, 8)*sp.eye(N)+L)*center,
            'Exact upper-band centered Gram identity')
    # Only the selected physical model is built. exp(h/10) is rational.
    z = sp.Rational(65, 64)
    Qh = sp.zeros(N+1)
    Qh[1:, 1:] = K
    for i, label in enumerate(labels):
        Qh[0, i+1] = mu[i]*z**(10+label)
        Qh[i+1, 0] = z**(label-10)
        Qh[i+1, i+1] -= Qh[i+1, 0]
    Qh[0, 0] = -sum(Qh[0, i] for i in range(1, N+1))
    pi = sp.Matrix([[1]+[z**20*value for value in mu]])/(1+z**20)
    require(Qh*sp.ones(N+1, 1) == sp.zeros(N+1, 1), 'Selected original-rule full generator has zero row sums')
    require(sp.diag(*pi)*Qh == Qh.T*sp.diag(*pi), 'Selected full model obeys exact finite-field detailed balance')
    require(pi*Qh == sp.zeros(1, N+1), 'Selected physical preparation/equilibrium identity')
    return {'selected_full_physical_states': N+1, 'exact_histogram_mass_per_level': '1/6',
            'certified_internal_band': ['3/2', '17/8'],
            'local_cap_exact_Gram_certificate': '5/8',
            'weighted_stationary_flux_and_original_field_rule_verified': True,
            'full_clock_two_symbol_probabilities_verified': 36}


def component_selection_checks():
    records = []
    for width in (1, 2):
        addresses = 1 << width
        tables = list(itertools.product((-1, 1), repeat=addresses))
        laws = [component_law(width, table, 1) for table in tables]
        target = mixture(laws, [F(1, len(tables))]*len(tables))
        require(target == annealed_local_law(width, 1), 'Counted small dictionary agrees with the visited-class annealed law')
        if width == 1:
            selected, weights = [0, 1, 2], [F(1, 2), F(1, 4), F(1, 4)]
        else:
            selected = next(list(pair) for pair in itertools.combinations(range(len(tables)), 2)
                            if mixture([laws[i] for i in pair], [F(1, 2)]*2) == target)
            weights = [F(1, 2)]*2
        require(mixture([laws[i] for i in selected], weights) == target, 'Positive whole-configuration selection matches every two-symbol prefix exactly')
        require(all(weight > 0 for weight in weights) and sum(weights) == 1, 'Component weights are positive and normalized')
        longer_updates = 2 if width == 1 else 3
        target_longer = mixture([component_law(width, table, longer_updates) for table in tables], [F(1, len(tables))]*len(tables))
        selected_longer = mixture([component_law(width, tables[i], longer_updates) for i in selected], weights)
        longer_error = tv(target_longer, selected_longer)
        if width == 2:
            require(longer_error > 0, 'Selection check detects that matching the chosen prefix need not match a longer one')
        physical = selected_physical(width, [tables[i] for i in selected], weights)
        records.append({'register_width': width, 'original_fixed_configurations': len(tables),
                        'original_counted_physical_states': 1+6*addresses*len(tables),
                        'original_large_physical_matrix_constructed': False,
                        'selected_configurations': [list(tables[i]) for i in selected],
                        'selected_positive_weights': [str(weight) for weight in weights],
                        'two_symbol_prefix_match_exact': True,
                        'longer_prefix_symbols_checked': longer_updates+1,
                        'longer_prefix_TV_after_selection_exact': str(longer_error), **physical})
    return records


def rational_budgets():
    z = F(65, 64)
    R, AH = z**13, z**6
    CR = 1+2*R*R
    q = F(5, 2)*R/(1+F(5, 2)*R)
    require(q >= F(5, 7), 'beta<=log(7/5) uniformly over the physical parameter class')
    require(F(16) > F(7, 5)**6, 'The address exponent exceeds the other power exponent by more than four')
    require(2*CR > 3, 'The logarithmic offset exceeds one, using exp(1)<3')
    records = []
    for delta in (F(1, 2), F(1, 16), F(1, 256), F(1, 4096)):
        ell = 1
        while CR*q**(ell+1) > delta/2:
            ell += 1
        n0 = 4*ell+1
        ratio = 2*CR*AH*ell*(ell+1)/delta
        while F(2)**(n0-2) < ratio*ratio:
            n0 += 1
        require(n0 >= 4*ell+1, 'Reference width prevents short-word wraparound')
        require((CR*AH*ell*(ell+1))**2 <= (delta/2)**2*2**(n0-2), 'Exact squared collision-error budget')
        require(CR*q**(ell+1) <= delta/2, 'Exact reset-tail error budget')
        require(F(2)**n0 <= max(F(2)**(4*ell+1), 32*(CR*AH)**2*ell**2*(ell+1)**2/delta**2),
                'Ceiling-safe reference-size estimate')
        for original in (1, n0, n0+1, 10*n0):
            reference = min(original, n0)
            require(reference <= n0, 'All original widths share the same reference-size cap')
        records.append({'delta': str(delta), 'prefix_updates_ell': ell, 'reference_width_n0': n0,
                        'reset_tail_mean_error_exact': str(CR*q**(ell+1)),
                        'collision_mean_error_at_most_delta_over_two': True,
                        'counted_total_state_bound': str(1+6**(ell+2)*2**n0),
                        'large_reference_model_constructed': False})
    return {'physical_parameters': {'lambda': '1/8', 'gamma': ['1/10', '1/5', '3/10'],
                                    'exp_H_over_10': '65/64', 'R_exact': str(R), 'A_H_exact': str(AH)},
            'records': records,
            'uniform_polynomial_exponent': 'log(96)/beta, beta=log(1+1/((5/2)R))',
            'all_accuracy_power_margin_certificate': '16>(7/5)^6 implies log(96)/beta > 6+log(6)/beta. The extra fourth power absorbs ell^2(ell+1)^2 for every accuracy, using ell<=log(2C_R/delta)/beta and delta^4 log^4(2C_R/delta)<=log^4(2C_R).',
            'scope': 'Exact rational checks of the all-accuracy formulas and symbolic power margin; enormous reference models are counted but never enumerated.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/register_scenery_compression.json'))
    args = parser.parse_args()
    report = {'status': 'PASS',
              'scope': 'Exact affine address actions and collision equations, visited-address-class annealed prefix laws, positive whole-configuration reduction with small physical models, and rational all-accuracy compression budgets. No simulation or large dictionary matrix.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'affine_dihedral_address_checks': affine_checks(),
              'exact_stationary_prefix_checks': prefix_checks(),
              'positive_whole_configuration_selection': component_selection_checks(),
              'all_accuracy_rational_budgets': rational_budgets(),
              'largest_constructed_physical_generator_dimension': 49,
              'largest_enumerated_address_space': 64,
              'largest_enumerated_scenery_dictionary_configurations': 16,
              'no_large_graph_simulation_or_numerical_rank_tests': True,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
