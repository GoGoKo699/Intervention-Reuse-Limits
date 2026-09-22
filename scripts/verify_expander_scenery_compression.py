#!/usr/bin/env python3
"""Exact small checks of high-girth scenery compression and one-event bounds.

No graph family or label dictionary of growing size is enumerated. Path
equalities, positive whole-coloring selection, physical identities, bounded
differences, refresh amplification and rational error budgets are verified.
The uniform proof is in docs/EXPANDER_SCENERY_COMPRESSION.md.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
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


def cycle(n: int) -> list[list[int]]:
    return [[(v-1) % n, (v+1) % n] for v in range(n)]


def update(graph: list[list[int]], sign_flip: bool) -> list[dict[int, F]]:
    n = len(graph)
    rows = []
    for sigma in range(2 if sign_flip else 1):
        for v, neighbors in enumerate(graph):
            row = defaultdict(F)
            row[sigma*n+v] += F(1, 2)
            for u in neighbors:
                row[sigma*n+u] += F(1, (4 if sign_flip else 2)*len(neighbors))
            if sign_flip:
                row[(1-sigma)*n+v] += F(1, 4)
            require(sum(row.values()) == 1, 'Exact local update row normalization')
            rows.append(dict(row))
    require(all(rows[i].get(j, 0) == rows[j].get(i, 0)
                for i in range(len(rows)) for j in range(len(rows))),
            'Uniform local update is symmetric')
    return rows


def paths(rows: list[dict[int, F]], ell: int) -> list[tuple[tuple[int, ...], F]]:
    result = [((i,), F(1, len(rows))) for i in range(len(rows))]
    for _ in range(ell):
        result = [(path+(j,), mass*prob) for path, mass in result
                  for j, prob in rows[path[-1]].items()]
    require(sum(mass for _, mass in result) == 1, 'Stationary path mass is normalized')
    return result


def path_law(graph: list[list[int]], ell: int, sign_flip: bool,
             labels: tuple[int, ...] | None = None) -> dict[tuple[int, ...], F]:
    n = len(graph)
    law = defaultdict(F)
    for path, mass in paths(update(graph, sign_flip), ell):
        visited = sorted({state % n for state in path})
        assignments = [dict(zip(range(n), labels))] if labels is not None else [
            dict(zip(visited, bits)) for bits in itertools.product((-1, 1), repeat=len(visited))]
        for assignment in assignments:
            word = tuple((1 if state < n else -1)*assignment[state % n] for state in path)
            law[word] += mass/len(assignments)
    require(sum(law.values()) == 1, 'Actuator word law is normalized')
    return dict(law)


def tv(left: dict, right: dict) -> F:
    return sum((abs(left.get(w, 0)-right.get(w, 0)) for w in left.keys() | right.keys()), F())/2


def universal_prefixes() -> dict:
    bipartite = [list(range(4, 8)) for _ in range(4)]+[list(range(4)) for _ in range(4)]
    cube = [[v ^ (1 << j) for j in range(4)] for v in range(16)]
    records = []
    for name, left, right, ell in [('degree_four', bipartite, cube, 1),
                                   ('cycles_length_three', cycle(7), cycle(9), 2),
                                   ('cycles_length_four', cycle(9), cycle(11), 3)]:
        for sign in (False, True):
            a, b = path_law(left, ell, sign), path_law(right, ell, sign)
            require(a == b, 'High-girth universal local prefix equality, including sign paths')
            records.append({'case': name, 'base_vertices': [len(left), len(right)],
                            'ell': ell, 'sign_flips': sign, 'matched_word_count': len(a),
                            'total_variation_exact': str(tv(a, b))})
    triangle, square = path_law(cycle(3), 3, False), path_law(cycle(4), 3, False)
    gap = tv(triangle, square)
    require(gap > 0, 'Removing the girth condition really changes longer word laws')
    return {'universal_cases': records, 'low_girth_counterexample_total_variation_exact': str(gap),
            'method': 'Enumerate short walk paths and labels only on visited base vertices.'}


def matrix_law(P: sp.Matrix, mu: sp.Matrix, labels: list[int], ell: int) -> dict:
    return {w: F(reused.word_probability(P, mu, labels, w))
            for w in itertools.product((-1, 1), repeat=ell+1)}


def coloring_selection() -> tuple[dict, dict, dict]:
    graph, n, ell = cycle(3), 3, 2
    colors = list(itertools.product((-1, 1), repeat=n))
    words = list(itertools.product((-1, 1), repeat=ell+1))
    laws = [path_law(graph, ell, True, x) for x in colors]
    V = sp.Matrix([[sp.Rational(law.get(w, 0)) for law in laws] for w in words])
    mass = sp.ones(len(colors), 1)/len(colors)
    target = V*mass
    active, steps = list(range(len(colors))), []
    while V[:, active].nullspace():
        direction = V[:, active].nullspace()[0]
        require(sum(direction) == 0 and min(direction) < 0 < max(direction),
                'Prefix affine dependence has both signs')
        amount = min(mass[i]/direction[j] for j, i in enumerate(active) if direction[j] > 0)
        before = len(active)
        for j, i in enumerate(active):
            mass[i] -= amount*direction[j]
        active = [i for i in active if mass[i] > 0]
        require(min(mass) >= 0 and sum(mass) == 1 and V*mass == target and len(active) < before,
                'Whole-coloring elimination retains exact prefix law and positive weights')
        steps.append([before, len(active)])
    require(len(active) < len(colors) and len(active) <= 2**(ell+1),
            'A genuine smaller complete-component model meets the Caratheodory count')
    local_rows = update(graph, True)
    local_P = sp.Matrix([[sp.Rational(local_rows[i].get(j, 0)) for j in range(2*n)]
                         for i in range(2*n)])

    def assemble(indices: list[int], weights: list[sp.Expr]) -> dict:
        P_loc = sp.diag(*[local_P for _ in indices])
        mu = sp.Matrix([[weight/(2*n) for weight in weights for _ in range(2*n)]])
        labels = [sigma*colors[i][v] for i in indices for sigma in (1, -1) for v in range(n)]
        count = len(mu)
        refresh = sp.ones(count, 1)*mu
        K = P_loc-sp.eye(count)+sp.Rational(3, 2)*(refresh-sp.eye(count))
        P = sp.eye(count)+K/sp.Rational(5, 2)
        require(P == sp.Rational(2, 5)*P_loc+sp.Rational(3, 5)*refresh,
                'Full-clock mixture has exact local/refresh weights')
        require(mu*K == sp.zeros(1, count) and sp.diag(*mu)*K == K.T*sp.diag(*mu),
                'Selected whole components and refresh preserve ordinary detailed balance')
        require(bounded.histogram(mu, labels) == {-1: sp.Rational(1, 2), 1: sp.Rational(1, 2)},
                'Sign-layer histogram is exact for every selected coloring mixture')
        spectrum = (-K).eigenvals()
        require(spectrum.get(0) == 1 and all(x == 0 or sp.Rational(3, 2) <= x <= sp.Rational(5, 2)
                                            for x in spectrum), 'Original supplied spectral band')
        largest = bounded.physical_identities(P, mu, labels, sp.Rational(5, 2), True)
        return {'P_loc': P_loc, 'P': P, 'mu': mu, 'labels': labels,
                'refresh': refresh, 'physical_states': largest,
                'spectrum': {str(x): v for x, v in sorted(spectrum.items())}}

    selected = assemble(active, [mass[i] for i in active])
    fixed = assemble([1], [sp.Integer(1)])
    require(matrix_law(selected['P_loc'], selected['mu'], selected['labels'], ell)
            == path_law(graph, ell, True), 'Assembled physical model matches annealed prefix')
    return selected, fixed, {'initial_whole_colorings': len(colors), 'selected_whole_colorings': len(active),
                            'selected_indices': active, 'weights_exact': [str(mass[i]) for i in active],
                            'elimination_steps': steps, 'preserved_prefix_length': ell+1,
                            'original_dictionary_hidden_states_counted': len(colors)*2*n,
                            'selected_physical_states': selected['physical_states'],
                            'relaxation_spectrum_exact': selected['spectrum']}


def bounded_differences() -> dict:
    graph, records, comparisons = cycle(3), [], 0
    colors = list(itertools.product((-1, 1), repeat=3))
    for ell in (1, 2, 3):
        laws = {x: path_law(graph, ell, True, x) for x in colors}
        average = {w: sum(laws[x].get(w, 0) for x in colors)/len(colors)
                   for w in itertools.product((-1, 1), repeat=ell+1)}
        require(average == path_law(graph, ell, True),
                'Annealed reference retains the same evolving sign process')
        largest = F()
        for x in colors:
            for v in range(3):
                y = tuple(-bit if j == v else bit for j, bit in enumerate(x))
                for w in average:
                    gap = abs(laws[x].get(w, 0)-laws[y].get(w, 0))
                    require(gap <= F(ell+1, 3), 'Exhaustive one-bit bounded-difference inequality')
                    largest = max(largest, gap)
                    comparisons += 1
        walk_paths = paths(update(graph, True), ell)
        visits = [sum(mass for path, mass in walk_paths if any(state % 3 == v for state in path))
                  for v in range(3)]
        require(all(p <= F(ell+1, 3) for p in visits), 'Stationary visited-vertex probability bound')
        records.append({'ell': ell, 'largest_single_word_change_exact': str(largest),
                        'theoretical_per_bit_bound_exact': str(F(ell+1, 3)),
                        'visited_vertex_probability_exact': str(visits[0])})
    j = sp.symbols('j', integer=True, positive=True)
    require(sp.cancel(1/(j*(j+1))-1/(j+1)**2-1/(j*(j+1)**2)) == 0,
            'Exact summable allocation comparison')
    require(sp.summation(1/(j*(j+1)), (j, 2, sp.oo)) == sp.Rational(1, 2),
            'Telescoping tail bounds all prefix lengths at once')
    # First term 1/4 plus this tail gives <=3/4, strictly below one.
    allocation = sp.Rational(1, 4)+sp.Rational(1, 2)
    require(allocation < 1, 'All-ell union bound costs less than eta')
    return {'cases': records, 'individual_bit_word_comparisons': comparisons,
            'all_ell_failure_bound_as_fraction_of_eta': str(allocation),
            'B_ell': '(ell+2)log(2)+2log(ell+1)+log(1/eta)',
            'local_TV_bound': '2^ell*(ell+1)*sqrt(B_ell/(2N))',
            'scope': 'One labeling event per fixed supplied graph, simultaneously for all integer ell and all accuracies.'}


def flag_law(model: dict, flags: tuple[int, ...]) -> dict:
    law = {}
    for word in itertools.product((-1, 1), repeat=len(flags)+1):
        row = model['mu'].copy()
        for j, symbol in enumerate(word):
            row = sp.Matrix([[row[i] if model['labels'][i] == symbol else 0 for i in range(len(row))]])
            if j < len(flags):
                row = row*(model['refresh'] if flags[j] else model['P_loc'])
        law[word] = F(sum(row))
    return law


def refresh_comparison(selected: dict, fixed: dict) -> dict:
    records, flag_checks = [], 0
    for ell in (1, 2, 3):
        a = matrix_law(fixed['P_loc'], fixed['mu'], fixed['labels'], ell)
        b = matrix_law(selected['P_loc'], selected['mu'], selected['labels'], ell)
        theta = tv(a, b)
        require(theta > 0, 'Fixed scenery and its annealed reference really differ')
        mixtures = [defaultdict(F), defaultdict(F)]
        maximum_ratio = F()
        for flags in itertools.product((0, 1), repeat=ell):
            laws = [flag_law(model, flags) for model in (fixed, selected)]
            runs = 1+sum(flags)
            gap = tv(*laws)
            require(gap <= runs*theta <= (ell+1)*theta,
                    'Each stationary refresh run costs at most one local-prefix discrepancy')
            maximum_ratio = max(maximum_ratio, gap/theta)
            probability = F(3, 5)**sum(flags)*F(2, 5)**(ell-sum(flags))
            for mixture, law in zip(mixtures, laws):
                for word, mass in law.items():
                    mixture[word] += probability*mass
            flag_checks += 1
        direct = [matrix_law(model['P'], model['mu'], model['labels'], ell) for model in (fixed, selected)]
        require(all(dict(mix) == law for mix, law in zip(mixtures, direct)),
                'Conditioning on all flags reproduces full refreshed prefix laws exactly')
        require(tv(*direct) <= (ell+1)*theta, 'Full-prefix amplification bound')
        records.append({'ell': ell, 'local_TV_exact': str(theta), 'full_TV_exact': str(tv(*direct)),
                        'largest_flag_TV_over_local_TV_exact': str(maximum_ratio),
                        'allowed_run_factor': ell+1})
    short_theta = tv(matrix_law(fixed['P_loc'], fixed['mu'], fixed['labels'], 1),
                     matrix_law(selected['P_loc'], selected['mu'], selected['labels'], 1))
    two_run_gap = tv(flag_law(fixed, (0, 1, 0)), flag_law(selected, (0, 1, 0)))
    require(short_theta < two_run_gap <= 2*short_theta,
            'Two independent local runs can cost strictly more than one run')
    frozen_average = defaultdict(F)
    for colors in itertools.product((-1, 1), repeat=3):
        model = dict(fixed, labels=[sigma*colors[v] for sigma in (1, -1) for v in range(3)])
        for word, probability in flag_law(model, (0, 1, 0)).items():
            frozen_average[word] += probability/8
    noncommutation = tv(dict(frozen_average), flag_law(selected, (0, 1, 0)))
    require(noncommutation > 0,
            'Averaging frozen-label refreshed laws is not the refreshed annealed-reference law')
    return {'cases': records, 'individual_flag_words_checked': flag_checks,
            'two_length_two_runs_TV_exact': str(two_run_gap),
            'one_length_two_run_TV_exact': str(short_theta),
            'frozen_average_versus_annealed_refresh_TV_exact': str(noncommutation),
            'warning': 'Averaging a frozen labeling does not commute with multiplying refreshed local-run probabilities.'}


def free_word_certificates() -> dict:
    generators = [(1, 2, 0, 1), (1, -2, 0, 1), (1, 0, 2, 1), (1, 0, -2, 1)]
    identity = (1, 0, 0, 1)

    def multiply(a: tuple, b: tuple) -> tuple:
        return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])

    level, records, total = [((), identity)], [], 0
    for depth in range(1, 7):
        level = [(word+(j,), multiply(matrix, generator)) for word, matrix in level
                 for j, generator in enumerate(generators) if not word or j != (word[-1] ^ 1)]
        modulus = 3**depth+2
        for _, matrix in level:
            require(matrix != identity and matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1,
                    'Every sampled reduced word is a nonidentity determinant-one integer matrix')
            difference = [x-y for x, y in zip(matrix, identity)]
            require(max(map(abs, matrix)) <= 3**depth and max(map(abs, difference)) < modulus,
                    'Integer row-norm bound keeps a nonzero difference below the composite modulus')
            require(any(x % modulus for x in difference), 'No sampled reduced word vanishes modulo M')
        total += len(level)
        records.append({'reduced_word_length': depth, 'words_checked': len(level),
                        'integer_modulus': modulus, 'group_size_upper_bound': modulus**4})
    return {'cases': records, 'total_reduced_words_checked': total,
            'scope': 'Finite exact certificates support, but do not replace, the all-length ping-pong proof.'}


def error_budgets() -> dict:
    R, cap, A = F(3, 2), F(5, 2), F(9, 4)
    C, q = 1+2*R**2, cap*R/(1+cap*R)
    records = []
    for delta in (F(1, 4), F(1, 16), F(1, 64)):
        ell = 1
        while C*q**(ell+1) > delta/2:
            ell += 1
        require(ell == 1 or C*q**ell > delta/2, 'Exact minimal cutoff with half the error allocated to exhaustion')
        # eta=1/16: log2<1, log(ell+1)<=ell and log16<4 give B_ell<=3ell+6.
        B_upper = 3*ell+6
        threshold = 2*C**2*A**2*4**ell*(ell+1)**4*B_upper/delta**2
        N = -((-threshold).__floor__())
        theta_squared = F(4**ell*(ell+1)**2*B_upper, 2*N)
        require(C**2*A**2*(ell+1)**2*theta_squared <= delta**2/4,
                'Concentration threshold gives at most half the actual-mean error')
        require(C*q**(ell+1) <= delta/2, 'Exact prefix exhaustion budget')
        # a=1/(8 log3) is the explicit Cayley-family girth constant.
        N_girth = 3**(8*(2*ell+1))
        H_size = (3**(2*ell+1)+2)**4
        sign_surrogate_states = 1+2**(ell+2)*H_size
        exact_retention_bound = 1+2*max(N, N_girth)
        records.append({'delta_exact': str(delta), 'ell': ell, 'B_ell_rational_upper': B_upper,
                        'concentration_threshold_ceiling': N, 'girth_threshold_exact': N_girth,
                        'prefix_error_exact': str(C*q**(ell+1)),
                        'concentration_mean_error_squared_exact': str(C**2*A**2*(ell+1)**2*theta_squared),
                        'selected_sign_layer_state_bound': sign_surrogate_states,
                        'exact_retention_state_bound': exact_retention_bound})
    return {'R_exact': str(R), 'entry_tilt_amplification_upper_exact': str(A),
            'eta_exact': '1/16', 'continuation_probability_exact': str(q), 'cases': records,
            'method': 'Rational powers, squared concentration inequalities and integer ceilings; no simulated trajectories.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/expander_scenery_compression.json'))
    args = parser.parse_args()
    selected, fixed, selection = coloring_selection()
    sources = [Path(__file__).resolve(), Path(bounded.__file__).resolve(), Path(reused.__file__).resolve()]
    report = {'status': 'PASS',
              'scope': 'Exact high-girth prefix comparison, complete-coloring convex reduction, evolving sign-layer physical model, all-ell bounded-difference allocation, refresh amplification and finite error budgets.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                           'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
              'universal_tree_prefixes': universal_prefixes(), 'whole_coloring_selection': selection,
              'quenched_one_event_for_all_accuracies': bounded_differences(),
              'approximate_prefix_refresh': refresh_comparison(selected, fixed),
              'integer_high_girth_graph_certificates': free_word_certificates(),
              'all_protocol_error_budgets': error_budgets(),
              'largest_matrix_dimension': max(selected['physical_states'], fixed['physical_states']),
              'limitations': 'The finite checks do not prove the all-size graph theorem, a cap-only result, an all-labeling upper, or a new expander construction. The graph is fixed before the random labeling. The full proof and prior-art qualifications are in the accompanying research note.',
              'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
