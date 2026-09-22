#!/usr/bin/env python3
"""Exact small checks of whole-component reversible compression.

Weighted lattice cuts, positive component selection, stationary refresh flags,
the original physical field rule, spectral-band preservation, irreducibility
repair, and rational error budgets are checked without simulation. The
uniform theorem is proved in docs/SPARSE_REVERSIBLE_COMPRESSION.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as sp

import verify_bounded_rate_prediction as bounded


reused = bounded.reused
require, Q = reused.require, sp.Rational


def components(matrix: sp.Matrix) -> list[list[int]]:
    unseen, result = set(range(matrix.rows)), []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        for i in queue:
            for j in sorted(unseen):
                if matrix[i, j] > 0:
                    unseen.remove(j)
                    queue.append(j)
        result.append(queue)
    return result


def generator(mu: sp.Matrix, edges: list[tuple[int, int, sp.Expr]]) -> sp.Matrix:
    matrix = sp.zeros(len(mu))
    for i, j, conductance in edges:
        matrix[i, j] = conductance/mu[i]
        matrix[j, i] = conductance/mu[j]
    for i in range(matrix.rows):
        matrix[i, i] = -sum(matrix[i, j] for j in range(matrix.rows) if j != i)
    return matrix


def weighted_cuts() -> dict:
    records, offset_checks = [], 0
    forcing_model = None
    for name, vertices in (('weighted_path', [(i,) for i in range(7)]),
                           ('weighted_grid', list(itertools.product(range(3), repeat=2)))):
        count, dimension = len(vertices), len(vertices[0])
        mu = sp.Matrix([[Q(i+1, count*(count+1)//2) for i in range(count)]])
        edges = [(i, j, Q(1+(i+j) % 3, 1000))
                 for i in range(count) for j in range(i+1, count)
                 if sum(abs(x-y) for x, y in zip(vertices[i], vertices[j])) == 1]
        local = generator(mu, edges)
        require(mu*local == sp.zeros(1, count), 'Weighted local stationary law')
        require(sp.diag(*mu)*local == local.T*sp.diag(*mu), 'Weighted local detailed balance')
        # A symmetric diagonally dominant certificate for I+L in L2(mu).
        require(all(mu[i]+mu[i]*local[i, i]
                    >= sum(mu[i]*local[i, j] for j in range(count) if j != i)
                    for i in range(count)), 'Exact local spectral cap one by diagonal dominance')
        mean_exit = sum(mu[i]*(-local[i, i]) for i in range(count))
        for side in (2, 3):
            fluxes, sizes = [], []
            for offset in itertools.product(range(side), repeat=dimension):
                boxes = [tuple((x-o)//side for x, o in zip(vertex, offset)) for vertex in vertices]
                retained = [(i, j, w) for i, j, w in edges if boxes[i] == boxes[j]]
                deleted = generator(mu, retained)
                groups = components(deleted)
                require(max(map(len, groups)) <= side**dimension, 'Each retained component fits in one lattice box')
                require(sp.diag(*mu)*deleted == deleted.T*sp.diag(*mu), 'Symmetric cuts preserve weighted reversibility')
                require(all(deleted[i, i] >= local[i, i] for i in range(count)), 'Deletion decreases every outgoing rate')
                flux = sum(mu[i]*(local[i, j]-deleted[i, j])
                           for i in range(count) for j in range(count) if i != j)
                require(flux == 2*sum(w for i, j, w in edges if boxes[i] != boxes[j]),
                        'Directed cut flux counts both orientations exactly')
                fluxes.append(flux)
                sizes.append(max(map(len, groups)))
                offset_checks += 1
                if name == 'weighted_path' and side == 2 and offset == (0,):
                    forcing_model = (mu, local, deleted, flux)
            require(sum(fluxes)/len(fluxes) == mean_exit/side,
                    'Exact offset average cuts every nearest-neighbor edge with probability 1/a')
            require(min(fluxes) <= mean_exit/side <= Q(1, side), 'An offset attains the uniform cap-based cut budget')
            records.append({'graph': name, 'vertices': count, 'dimension': dimension,
                            'side_length': side, 'offsets': len(fluxes),
                            'stationary_mean_exit_exact': str(mean_exit),
                            'average_directed_cut_flux_exact': str(sum(fluxes)/len(fluxes)),
                            'minimum_directed_cut_flux_exact': str(min(fluxes)),
                            'largest_surviving_component': max(sizes)})
    require(forcing_model is not None, 'A nontrivial weighted deletion was selected')
    mu, local, deleted, flux = forcing_model
    n, radius = len(mu), Q(3, 2)
    x = sp.symbols(f'x0:{n}', nonnegative=True)
    occupation = sp.Matrix([[mu[i]*x[i] for i in range(n)]])
    difference = local-deleted
    forcing = occupation*difference
    formula = sp.Matrix([[sum(mu[i]*difference[i, j]*(x[i]-x[j])
                              for i in range(n) if i != j) for j in range(n)]])
    require((forcing-formula).applyfunc(sp.expand) == sp.zeros(1, n), 'Exact signed forcing identity includes the deleted diagonal')
    require(sp.expand(sum(forcing)) == 0, 'Deleted-edge forcing has zero mass')
    maximum = sp.Integer(0)
    for bits in itertools.product((0, 1), repeat=n):
        value = forcing.subs({x[i]: radius**2*bits[i] for i in range(n)})
        norm = sum(abs(v) for v in value)
        require(norm <= radius**2*flux, 'Signed forcing bound at every density-box vertex')
        maximum = max(maximum, norm)
    require(maximum == radius**2*flux, 'Directed-flux forcing constant is attained')
    # A gap-one complete local graph saturates the partition obstruction.
    uniform = sp.ones(1, 6)/6
    complete = sp.ones(6)/6-sp.eye(6)
    groups = [(0, 1), (2, 3), (4, 5)]
    boundary = sum(uniform[i]*complete[i, j] for group in groups for i in group
                   for j in range(6) if j not in group)
    require(complete.eigenvals() == {0: 1, -1: 5}, 'Exact Poincare gap one')
    require(boundary == 1-sum(sum(uniform[i] for i in group)**2 for group in groups)
            == 1-2*max(uniform) == Q(2, 3), 'Sharp stationary-flux fragmentation obstruction')
    return {'lattice_cases': records, 'offsets_enumerated': offset_checks,
            'forcing_density_box_vertices': 2**n, 'attained_forcing_L1_exact': str(maximum),
            'forcing_radius_exact': str(radius), 'directed_flux_exact': str(flux),
            'Duhamel_mean_bound_exact': str(radius**3*flux),
            'gap_one_partition_obstruction_exact': str(boundary)}


def select_components() -> tuple[dict, dict, dict]:
    rates = [Q(i, 12) for i in range(1, 7)]
    updates = [sp.Matrix([[1-t, t], [t, 1-t]]) for t in rates]
    weights = sp.Matrix([Q(i, 20) for i in (1, 1, 2, 3, 5, 8)])
    words = list(itertools.product((-1, 1), repeat=3))
    vectors = sp.Matrix([[reused.word_probability(P, sp.ones(1, 2)/2, [-1, 1], word)
                          for P in updates] for word in words])
    require(vectors.rank() == 3, 'Length-three component laws span three moment coordinates')
    target_vector = vectors*weights
    selected, mass, steps = list(range(6)), weights.copy(), []
    while True:
        active = vectors[:, selected]
        kernel = active.nullspace()
        if not kernel:
            break
        direction = kernel[0]
        require(sum(direction) == 0 and min(direction) < 0 < max(direction),
                'A nonzero affine dependence has both signs')
        amount = min(mass[i]/direction[j] for j, i in enumerate(selected) if direction[j] > 0)
        before = len(selected)
        for j, i in enumerate(selected):
            mass[i] -= amount*direction[j]
        require(min(mass) >= 0 and sum(mass) == 1 and vectors*mass == target_vector,
                'Exact nullspace elimination preserves positivity, normalization and every prefix coordinate')
        selected = [i for i in selected if mass[i] > 0]
        require(len(selected) < before, 'Each Caratheodory elimination removes a component')
        steps.append({'components_before': before, 'components_after': len(selected),
                      'step_size_exact': str(amount)})
    require(len(selected) == 3 < 6 and len(selected) <= 2**3,
            'A genuine smaller positive mixture meets the simplex bound')

    def assemble(indices: list[int], masses: sp.Matrix) -> dict:
        local_update = sp.diag(*[updates[i] for i in indices])
        mu = sp.Matrix([[masses[i]/2 for i in indices for _ in range(2)]])
        n = len(mu)
        local = local_update-sp.eye(n)
        labels = [-1, 1]*len(indices)
        refresh = sp.ones(n, 1)*mu
        c, cap = Q(3, 2), Q(5, 2)
        K = local+c*(refresh-sp.eye(n))
        P = sp.eye(n)+K/cap
        require(P == local_update/cap+c*refresh/cap, 'Common-clock refresh mixture identity')
        require(min(P) > 0 and P*sp.ones(n, 1) == sp.ones(n, 1), 'Refreshed update is positive and stochastic')
        require(mu*K == sp.zeros(1, n) and sp.diag(*mu)*K == K.T*sp.diag(*mu),
                'Whole-component reweighting and refresh preserve ordinary detailed balance')
        spectrum = (-K).eigenvals()
        require(spectrum.get(0) == 1 and all(value == 0 or c <= value <= cap for value in spectrum),
                'Exact original lower and upper relaxation endpoints are retained')
        require(bounded.histogram(mu, labels) == {-1: Q(1, 2), 1: Q(1, 2)}, 'Exact binary actuator histogram, mean zero and variance one')
        bounded.physical_identities(P, mu, labels, cap, True)
        return {'P_local': local_update, 'L': local, 'mu': mu, 'labels': labels,
                'refresh': refresh, 'K': K, 'P': P,
                'spectrum': {str(v): multiplicity for v, multiplicity in sorted(spectrum.items())}}

    original, reduced = assemble(list(range(6)), weights), assemble(selected, mass)
    record = {'original_components': 6, 'selected_components': len(selected),
              'original_physical_states': len(original['mu'])+1,
              'selected_physical_states': len(reduced['mu'])+1,
              'local_flip_rates_exact': [str(t) for t in rates],
              'original_component_weights_exact': [str(w) for w in weights],
              'selected_original_component_indices': selected,
              'selected_component_weights_exact': [str(mass[i]) for i in selected],
              'prefix_vector_rank': vectors.rank(), 'nullspace_eliminations': steps,
              'original_relaxation_spectrum_exact': original['spectrum'],
              'selected_relaxation_spectrum_exact': reduced['spectrum'],
              'specified_spectral_band_exact': ['3/2', '5/2'],
              'histogram_exact': {'-1': '1/2', '1': '1/2'}}
    return original, reduced, record


def flagged_probability(model: dict, word: tuple[int, ...], flags: tuple[int, ...]) -> sp.Expr:
    row = model['mu']
    for index, symbol in enumerate(word):
        if index:
            row = row*(model['refresh'] if flags[index-1] else model['P_local'])
        row = row*sp.diag(*[int(value == symbol) for value in model['labels']])
    return (row*sp.ones(len(model['mu']), 1))[0]


def prefix_and_refresh(original: dict, reduced: dict) -> dict:
    words_checked, flags_checked, tilt_checks = 0, 0, 0
    for length in range(1, 4):
        for word in itertools.product((-1, 1), repeat=length):
            local = [reused.word_probability(model['P_local'], model['mu'], model['labels'], word)
                     for model in (original, reduced)]
            require(local[0] == local[1], 'All shorter local prefixes follow from selected length-three vector')
            averaged = [sp.Integer(0), sp.Integer(0)]
            for flags in itertools.product((0, 1), repeat=length-1):
                conditional = [flagged_probability(model, word, flags) for model in (original, reduced)]
                require(conditional[0] == conditional[1], 'Every stationary refresh-flag conditional law is shared')
                boundaries = [0]+[j+1 for j, flag in enumerate(flags) if flag]+[length]
                for index, model in enumerate((original, reduced)):
                    product = sp.prod(reused.word_probability(model['P_local'], model['mu'], model['labels'],
                                                               word[start:stop])
                                      for start, stop in zip(boundaries, boundaries[1:]))
                    require(conditional[index] == product, 'Refresh flags factor the law into independent local runs')
                    probability = Q(3, 5)**sum(flags)*Q(2, 5)**(len(flags)-sum(flags))
                    averaged[index] += probability*conditional[index]
                flags_checked += 1
            full = [reused.word_probability(model['P'], model['mu'], model['labels'], word)
                    for model in (original, reduced)]
            require(full[0] == full[1] and averaged == full, 'Averaging all flags recovers the matched full internal prefix')
            for tilt in (Q(2, 3), Q(3, 2)):
                norms = [sum(model['mu'][i]*tilt**label for i, label in enumerate(model['labels']))
                         for model in (original, reduced)]
                require(norms[0] == norms[1] and full[0]*tilt**word[0]/norms[0]
                        == full[1]*tilt**word[0]/norms[1], 'First-symbol field tilt has exactly shared normalization and prefix')
                tilt_checks += 1
            words_checked += 1
    differences = []
    for word in itertools.product((-1, 1), repeat=4):
        gap = reused.word_probability(original['P'], original['mu'], original['labels'], word)
        gap -= reused.word_probability(reduced['P'], reduced['mu'], reduced['labels'], word)
        differences.append((word, gap))
    witness = next(((word, gap) for word, gap in differences if gap != 0), None)
    require(witness is not None, 'Longer prefixes really differ; selection is not accidentally an exact all-word realization')
    return {'matched_words_through_length_three': words_checked,
            'individual_refresh_flag_laws': flags_checked, 'entry_tilt_checks': tilt_checks,
            'length_four_words_checked': len(differences),
            'length_four_total_variation_exact': str(sum(abs(gap) for _, gap in differences)/2),
            'longer_word_witness': list(witness[0]), 'longer_word_probability_gap_exact': str(witness[1])}


def repair_without_refresh(reduced: dict) -> dict:
    local, mu, theta, cap = reduced['L'], reduced['mu'], Q(1, 10), sp.Integer(1)
    n = len(mu)
    require(len(components(local)) == 3, 'Selected local generator is genuinely reducible')
    final = (1-theta)*local+theta*cap*(reduced['refresh']-sp.eye(n))
    require(all(final[i, j] > 0 for i in range(n) for j in range(n) if i != j),
            'The no-refresh repair restores positive off-diagonal rates without states')
    spectrum = (-final).eigenvals()
    require(spectrum.get(0) == 1 and all(v == 0 or theta*cap <= v <= cap for v in spectrum),
            'Repair preserves the original upper cap and supplies its stated lower gap')
    flux = sum(mu[i]*abs(final[i, j]-local[i, j]) for i in range(n) for j in range(n) if i != j)
    require(flux <= 2*theta*cap, 'Exact absolute directed flux is bounded by the remove-and-add budget')
    bounded.physical_identities(sp.eye(n)+final/cap, mu, reduced['labels'], cap, True)
    return {'theta_exact': str(theta), 'physical_states_before_and_after': n+1,
            'absolute_directed_flux_change_exact': str(flux), 'flux_bound_exact': str(2*theta*cap),
            'repaired_relaxation_spectrum_exact': {str(v): multiplicity for v, multiplicity in sorted(spectrum.items())},
            'scope': 'The repair retains the upper cap; no pre-existing larger lower gap is claimed.'}


def error_budgets() -> dict:
    R, cap, local_cap = Fraction(3, 2), Fraction(5, 2), Fraction(1)
    C, q = 1+2*R**2, cap*R/(1+cap*R)
    records = []
    for with_refresh in (True, False):
        parts = 2 if with_refresh else 3
        for delta in (Fraction(1, 4), Fraction(1, 32), Fraction(1, 512)):
            epsilon = delta/(parts*R**3)
            ell = 1
            while C*q**(ell+1) > delta/parts:
                ell += 1
            require(ell == 1 or C*q**ell > delta/parts, 'Exact minimal integer prefix cutoff')
            deletion, prefix = R**3*epsilon, C*q**(ell+1)
            theta = Fraction(0) if with_refresh else min(Fraction(1, 2), delta/(6*R**3*cap))
            repair = 2*R**3*theta*cap
            require(deletion == delta/parts and prefix <= delta/parts and repair <= delta/3,
                    'Exact deletion, finite-prefix and optional repair allocations')
            require(deletion+prefix+repair <= delta, 'Combined all-protocol actual-mean error budget')
            r = local_cap if with_refresh else cap
            side = max(1, -((-r/epsilon).__floor__()))
            require(r/side <= epsilon and (side == 1 or r/(side-1) > epsilon), 'Exact lattice side-length ceiling')
            records.append({'global_refresh_supplied': with_refresh, 'delta_exact': str(delta),
                            'deletion_flux_budget_exact': str(epsilon), 'ell': ell,
                            'deletion_error_exact': str(deletion), 'prefix_error_exact': str(prefix),
                            'repair_theta_exact': str(theta), 'repair_error_exact': str(repair),
                            'lattice_side_length': side,
                            'state_bounds_by_dimension': {str(d): 1+side**d*2**(ell+1) for d in (1, 2)}})
    # Exercise the other branch of theta=min(1/2,delta/(6 R^3 Lambda)).
    small_cap, loose_delta = Fraction(1, 100), Fraction(3, 4)
    clipped_theta = min(Fraction(1, 2), loose_delta/(6*R**3*small_cap))
    require(clipped_theta == Fraction(1, 2) and 2*R**3*clipped_theta*small_cap <= loose_delta/3,
            'The theta half-cap branch also obeys its exact repair budget')
    return {'R_exact': str(R), 'fixed_clock_exact': str(cap), 'regeneration_constant_exact': str(C),
            'continuation_probability_exact': str(q), 'full_error_budgets': records,
            'half_cap_theta_branch_checked': True,
            'method': 'Exact rational powers and integer ceilings; no logarithm rounding or simulation.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/sparse_reversible_compression.json'))
    args = parser.parse_args()
    original, reduced, selection = select_components()
    sources = [Path(__file__).resolve(), Path(bounded.__file__).resolve(), Path(reused.__file__).resolve()]
    report = {'status': 'PASS',
              'scope': 'Exact weighted lattice fragmentation, positive whole-component prefix selection, all refresh flags, original physical field identities, retained spectral band, no-refresh repair and finite error budgets; no simulations.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                           'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
              'weighted_fragmentation_and_forcing': weighted_cuts(),
              'whole_component_selection': selection,
              'prefixes_and_stationary_refresh': prefix_and_refresh(original, reduced),
              'no_refresh_irreducibility_repair': repair_without_refresh(reduced),
              'all_protocol_error_budgets': error_budgets(),
              'largest_matrix_dimension': 13,
              'limitations': 'Finite exact checks support the stated construction; they do not prove a cap-only theorem, cover all bounded-degree graphs, establish an intrinsic reversibility cost, or replace the uniform analytic proof.',
              'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
