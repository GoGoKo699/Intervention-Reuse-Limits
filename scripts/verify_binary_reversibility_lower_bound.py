#!/usr/bin/env python3
"""Exact sparse checks of the balanced binary reversible prediction gadget.

Only n=1 is built: 1795 hidden vertices and one counted visible state. All
accepted color walks are evaluated by sparse dynamic programming, including
accidental walks from every possible marker starting vertex. Dense matrices
have dimension at most five. No random trajectories or asymptotic fitting.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def code(length: int) -> list[int]:
    return [int('0011'[i % 4]) for i in range(length+1)]


def gate(y: tuple, name: str, n: int) -> tuple:
    table, address, sigma = y
    bits = tuple((address >> (n-1-i)) & 1 for i in range(n))
    if name == 'F':
        return table ^ (1 << address), address, sigma
    if name == 'J':
        new = tuple(bits[(-i-1) % n] for i in range(n))
    elif name == 'V':
        new = tuple(bits[(-i) % n] for i in range(n))
    else:
        require(name == 'X', 'Only the four prescribed logical gates are used')
        new = (1-bits[0],)+bits[1:]
    return table, sum(value << (n-1-i) for i, value in enumerate(new)), sigma


def feature(y: tuple) -> int:
    table, address, sigma = y
    return sigma*(1 if table & (1 << address) else -1)


def build_graph() -> dict:
    n, r = 1, 2
    triples = list(itertools.product(range(2**r), range(r), (-1, 1)))
    M = len(triples)
    labels, colors, adjacency, parent = [], [], [], []

    def vertex(label: tuple, color: int) -> int:
        index = len(labels)
        labels.append(label)
        colors.append(color)
        adjacency.append({})
        parent.append(None)
        return index

    def edge(i: int, j: int, weight: int = 1) -> None:
        require(i != j and weight > 0, 'The graph has no loops and every edge weight is positive')
        require(j not in adjacency[i], 'Private corridor vertices prevent accidental duplicate edges')
        adjacency[i][j] = weight
        adjacency[j][i] = weight

    roots = {y: vertex(('root',)+y, 0) for y in triples}
    hub, u, v = vertex(('hub',), 0), vertex(('ballast_u',), 1), vertex(('ballast_v',), 1)
    for root in roots.values():
        edge(root, hub)
        parent[root] = hub
    edge(hub, u, M)
    edge(u, v, 7*M)
    parent[u], parent[v] = hub, u
    corridors, markers = [], {}

    def corridor(y: tuple, endpoint: tuple, length: int, colors_word: list, kind: str) -> None:
        inside = [vertex((kind,)+y+(i,), colors_word[i]) for i in range(1, length)]
        path = [roots[y]]+inside+[roots[endpoint]]
        for left, right in zip(path, path[1:]):
            edge(left, right)
        for i in range(1, length):
            parent[path[i]] = path[i-1] if i <= length//2 else path[i+1]
        corridors.append({'kind': kind, 'source': y, 'endpoint': endpoint, 'length': length,
                          'path': path, 'active': colors_word == code(length)})

    for y in triples:
        for name, length in (('J', 5), ('V', 9), ('X', 13), ('F', 17)):
            gy = gate(y, name, n)
            require(gate(gy, name, n) == y, 'All literal logical gates are involutions')
            corridor(y, gy, length, code(length), name)
        for length, selected in ((21, feature(y) == 1), (25, feature(y) == -1)):
            accepted = code(length)
            actual = accepted.copy()
            if not selected:
                for left, right in ((2, 4), (length-2, length-4)):
                    actual[left], actual[right] = actual[right], actual[left]
                require(actual != accepted and actual == list(reversed(actual)) and sum(actual) == sum(accepted),
                        'Inactive probe scrambling changes both directions and preserves palindrome and color volume')
            corridor(y, y, length, actual, 'probe_'+str(length))
        marker_path = [roots[y]]+[vertex(('marker',)+y+(i,), code(27)[i]) for i in range(1, 28)]
        for left, right in zip(marker_path, marker_path[1:]):
            edge(left, right)
            parent[right] = left
        markers[y] = marker_path
    degrees = [sum(row.values()) for row in adjacency]
    total = sum(degrees)
    require(len(labels) == 112*M+3 == 1795 and total == 252*M,
            'Every physical decoration is counted and total degree is exactly 252M')
    require(all(degrees[root] == 14 and all(colors[j] == 0 for j in adjacency[root]) for root in roots.values()),
            'Each root has fourteen incidences and every neighbor is color zero')
    require(all(degrees[path[-1]] == 1 for path in markers.values()), 'Each private marker has a degree-one tip')
    require(sum(d for d, c in zip(degrees, colors) if c == 0) == total//2,
            'The weighted binary actuator histogram is exactly balanced')
    require(sum(degrees[root] for root in roots.values()) == F(total, 18), 'The stationary root mass is exactly 1/18')
    mu = [F(d, total) for d in degrees]
    P = [{j: F(weight, degrees[i]) for j, weight in row.items()} for i, row in enumerate(adjacency)]
    require(all(sum(row.values()) == 1 for row in P), 'The sparse transition is stochastic and nonlazy')
    require(all(mu[i]*value == mu[j]*P[j][i] for i, row in enumerate(P) for j, value in row.items()),
            'Every weighted graph edge obeys exact stationary detailed balance')
    return {'n': n, 'r': r, 'M': M, 'triples': triples, 'roots': roots, 'hub': hub, 'ballast': (u, v),
            'labels': labels, 'colors': colors, 'adjacency': adjacency, 'parent': parent,
            'markers': markers, 'corridors': corridors, 'degrees': degrees, 'total_degree': total,
            'mu': mu, 'P': P}


def walk(graph: dict, start: int, colors_word: list[int]) -> dict[int, F]:
    if graph['colors'][start] != colors_word[0]:
        return {}
    distribution = {start: F(1)}
    for color in colors_word[1:]:
        updated = {}
        for i, mass in distribution.items():
            for j, probability in graph['P'][i].items():
                if graph['colors'][j] == color:
                    updated[j] = updated.get(j, F())+mass*probability
        distribution = updated
        if not distribution:
            break
    return distribution


def word_checks(graph: dict) -> dict:
    marker_word, N = code(27), len(graph['labels'])
    require(marker_word == [int(value) for value in '0011'*7], 'The marker is the prescribed 28-symbol word')
    require(all(marker_word[i] != marker_word[i+2] for i in range(26)), 'The marker word excludes every immediate backtrack')
    forward = {i: row for i in range(N) if (row := walk(graph, i, marker_word))}
    backward = {i: row for i in range(N) if (row := walk(graph, i, list(reversed(marker_word))))}
    expected_forward, expected_backward = {}, {}
    for y, root in graph['roots'].items():
        tip = graph['markers'][y][-1]
        expected_forward[root] = {tip: F(1, 14*2**26)}
        expected_backward[tip] = {root: F(1, 2**26)}
    require(forward == expected_forward and backward == expected_backward,
            'All-start sparse walk enumeration leaves exactly the root-to-private-tip marker and its reverse')
    p = F(1, 14*2**52)
    for i, row in forward.items():
        product = {}
        for j, value in row.items():
            for k, other in backward[j].items():
                product[k] = product.get(k, F())+value*other
            require(graph['mu'][i]*value == graph['mu'][j]*backward[j][i],
                    'The reversed marker word is the stationary adjoint')
        require(product == {i: p}, 'Tmark Tmark* equals p times the exact target root projector')
    records = []
    root_set = set(graph['roots'].values())
    for name, length in (('J', 5), ('V', 9), ('X', 13), ('F', 17), ('plus_probe', 21), ('minus_probe', 25)):
        accepted, kappa = code(length), F(2, 14*2**(length-1))
        require(accepted == list(reversed(accepted)) and all(accepted[i] != accepted[i+2] for i in range(length-1)),
                'Each gate/probe accepted word is palindromic and disallows immediate backtracking')
        nonzero = 0
        for y, root in graph['roots'].items():
            result = {j: value for j, value in walk(graph, root, accepted).items() if j in root_set}
            if name in ('J', 'V', 'X', 'F'):
                expected = {graph['roots'][gate(y, name, graph['n'])]: kappa}
            else:
                selected = feature(y) == (1 if name == 'plus_probe' else -1)
                expected = {root: kappa} if selected else {}
            require(result == expected, 'Root-restricted sparse walks contain exactly the intended normalized gate or active probe')
            nonzero += bool(result)
        records.append({'name': name, 'edges': length, 'normalization_kappa_exact': str(kappa),
                        'positive_polynomial_scale_exact': str(1/kappa), 'nonzero_root_rows': nonzero})
    # The normalized query Gram can be evaluated on roots without allocating a physical matrix.
    r = graph['r']
    gram = [[sum(graph['mu'][root]*y[2]**2*
                 (1 if y[0] & (1 << (y[1] ^ b)) else -1)*
                 (1 if y[0] & (1 << (y[1] ^ c)) else -1)
                 for y, root in graph['roots'].items()) for c in range(r)] for b in range(r)]
    require(gram == [[F(int(b == c), 18) for c in range(r)] for b in range(r)],
            'The hidden stationary query Gram is I_r/18 with all root and table coordinates counted')
    return {'marker': {'all_start_vertices_checked_each_direction': N, 'nonzero_forward_rows': len(forward),
                       'nonzero_reverse_rows': len(backward), 'forward_probability_exact': str(F(1, 14*2**26)),
                       'reverse_probability_exact': str(F(1, 2**26)), 'TT_adjoint_root_factor_exact': str(p),
                       'positive_projector_polynomial_scale_exact': str(1/p)},
            'gate_and_probe_words': records, 'hidden_query_gram_diagonal_exact': '1/18',
            'word_check_scope': 'Every possible starting vertex is checked for the marker. Gates and probes are checked on both target root endpoints, as prescribed by their outer marker projectors.'}


def graph_and_field_checks(graph: dict) -> dict:
    degrees, parent, hub = graph['degrees'], graph['parent'], graph['hub']
    loads, depths, basins = {}, {}, {root: 0 for root in graph['roots'].values()}
    root_set = set(basins)
    for start in range(len(degrees)):
        current, path, owner = start, [], None
        while current != hub:
            require(current not in path and parent[current] is not None, 'The canonical route reaches the hub without a cycle')
            path.append(current)
            if current in root_set:
                owner = current
            nxt = parent[current]
            require(nxt in graph['adjacency'][current], 'Every routing step is an actual graph edge')
            edge = tuple(sorted((current, nxt)))
            loads[edge] = loads.get(edge, 0)+degrees[start]
            current = nxt
        depths[start] = len(path)
        if owner is not None:
            basins[owner] += degrees[start]
    require(set(basins.values()) == {235} and max(depths.values()) == 28,
            'All nearest-root basins have degree volume 235 and all routes have length at most 28')
    ratios = {edge: F(load, graph['adjacency'][edge[0]][edge[1]]) for edge, load in loads.items()}
    u, v = graph['ballast']
    require(ratios[tuple(sorted((hub, u)))] == 15 and ratios[tuple(sorted((u, v)))] == 1,
            'Weighted ballast route loads have the claimed conductance ratios')
    require(max(ratios.values()) == 235 and 28*235 == 6580,
            'The exact finite graph satisfies the claimed Poincare path-load certificate')
    mu, B, gamma = graph['mu'], 6580, F(1, 10)
    g = [gamma if color else -gamma for color in graph['colors']]
    require(sum(p*value for p, value in zip(mu, g)) == 0 and
            sum(p*value**2 for p, value in zip(mu, g)) == gamma**2,
            'The actual degree-weighted binary sensitivities have exact mean zero and variance gamma squared')
    field_records = []
    for base in (F(1), F(10001, 10000), F(10000, 10001)):
        tilt = base**20
        pi_A = 1/(1+tilt)
        pi_hidden = [tilt*p/(1+tilt) for p in mu]
        a_exit = F()
        for i, p in enumerate(mu):
            az, za = p*base**int(10*(1+g[i])), base**int(10*(g[i]-1))
            require(pi_A*az == pi_hidden[i]*za, 'Every original-rule visible edge has exact finite-field detailed balance')
            a_exit += az
            require(sum(B*value for value in graph['P'][i].values()) == B,
                    'Every target hidden state has the same internal exit Bk at k=1')
            if base == 1:
                require(za == 1, 'The hidden-to-visible passive exit equals one')
        require(all(pi_hidden[i]*B*prob == pi_hidden[j]*B*graph['P'][j][i]
                    for i, row in enumerate(graph['P']) for j, prob in row.items()),
                'All internal edges remain reversible under the physical field equilibrium')
        if base == 1:
            require(a_exit == 1, 'The full passive model has exact two-state telegraph lumpability')
        field_records.append({'exp_h_over_ten_exact': str(base), 'visible_edges_checked': len(mu)})
    # Bfield=Y_plus+Y_minus gives mu V1=pi0 Bfield V Bfield S.
    # V acts only on hidden vectors and is chosen here to be the target root projector.
    V1 = [F(int(i in root_set)) for i in range(len(mu))]
    right = [-2*value for value in V1]
    left_after_B = [-value for value in right]
    physical_scalar = sum(mu[i]*left_after_B[i]/2 for i in range(len(mu)))
    require(physical_scalar == sum(mu[i]*V1[i] for i in range(len(mu))) == F(1, 18),
            'The physical preparation/readout scalar exposes a hidden word with the exact claimed normalization')
    return {'logical_triples': graph['M'], 'hidden_states': len(degrees), 'physical_states': len(degrees)+1,
            'stored_directed_edges': sum(map(len, graph['P'])), 'total_degree': graph['total_degree'],
            'root_degree': 14, 'root_stationary_mass_exact': '1/18',
            'binary_stationary_histogram_exact': {'-1/10': '1/2', '1/10': '1/2'},
            'variance_exact': '1/100', 'maximum_route_edges': 28,
            'root_basin_degree_volume': 235, 'maximum_load_over_conductance': 235,
            'gap_lower_certificate_exact': '1/6580', 'P_relaxation_cap': 2,
            'physical_internal_exit_budget_k_units': B, 'physical_gap_lower_k_units': 1,
            'physical_spectral_cap_k_units': 2*B, 'physical_field_checks': field_records,
            'scope': 'Exact n=1 graph, path-load, and original-field checks. The dimension-independent construction and Poincare inequality are proved separately.'}


def matmul(A: list, B: list) -> list:
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def mv(A: list, v: list) -> list:
    return [sum(a*b for a, b in zip(row, v)) for row in A]


def adjoint(A: list, mu: list) -> list:
    return [[mu[j]*A[j][i]/mu[i] for j in range(len(mu))] for i in range(len(mu))]


def norm_squared(v: list, mu: list) -> F:
    return sum(p*x*x for p, x in zip(mu, v))


def repaired(T: list, mu: list) -> tuple[list, list, F]:
    n = len(mu)
    row, col = mv(T, [F(1)]*n), mv(adjoint(T, mu), [F(1)]*n)
    a = [min(F(1), 1/r) if r else F(1) for r in row]
    b = [min(F(1), 1/s) if s else F(1) for s in col]
    T0 = [[a[i]*T[i][j]*b[j] for j in range(n)] for i in range(n)]
    d = [1-r for r in mv(T0, [F(1)]*n)]
    e = [1-s for s in mv(adjoint(T0, mu), [F(1)]*n)]
    mass = sum(p*x for p, x in zip(mu, d))
    require(min(d+e) >= 0 and mass == sum(p*x for p, x in zip(mu, e)),
            'L2 repair clips both marginals to matching nonnegative deficits')
    U = [[T0[i][j]+(d[i]*mu[j]*e[j]/mass if mass else 0) for j in range(n)] for i in range(n)]
    require(all(sum(values) == 1 for values in U+adjoint(U, mu)),
            'The filled kernel and its shared-flux adjoint are stochastic')
    eps2 = max(norm_squared([r-1 for r in row], mu), norm_squared([s-1 for s in col], mu))
    return U, e, eps2


def l2_repair_checks() -> dict:
    mu = [F(1, 10000), F(9999, 10000)]
    T = [[F(0), F(10)], [F(1, 1000), F(999, 1000)]]
    C = F(2)
    # Exact PSD criterion for C^2 diag(mu)-T^T diag(mu)T certifies the operator cap.
    certificate = [[(C*C*mu[i] if i == j else 0)-sum(mu[k]*T[k][i]*T[k][j] for k in range(2))
                    for j in range(2)] for i in range(2)]
    require(certificate[0][0] > 0 and certificate[1][1] > 0 and
            certificate[0][0]*certificate[1][1] > certificate[0][1]*certificate[1][0],
            'An exact two-dimensional positive-definiteness certificate gives L2 operator norm below two')
    require(max(map(sum, T)) == 10 > C, 'This example has a row sum larger than the L2 cap')
    U, e, eps2 = repaired(T, mu)
    require(norm_squared(e, mu) <= (C+2)**2*eps2, 'The fill-vector L2 estimate holds')
    difference = [[T[i][j]-U[i][j] for j in range(2)] for i in range(2)]
    signs = list(itertools.product((F(-1), F(1)), repeat=2))
    maximum_dual_norm2 = max(norm_squared(mv(adjoint(difference, mu), list(f)), mu) for f in signs)
    require(maximum_dual_norm2 <= (2*C+3)**2*eps2,
            'All box corners certify the mixed infinity/L2 repair bound for every bounded f and every L2 g')
    raw = matmul(matmul(T, adjoint(T, mu)), T)
    fixed = matmul(matmul(U, adjoint(U, mu)), U)
    path_diff = [[raw[i][j]-fixed[i][j] for j in range(2)] for i in range(2)]
    max_scalar = max(abs(sum(mu[i]*f[i]*mv(path_diff, list(g))[i] for i in range(2))) for f in signs for g in signs)
    require(max_scalar**2 <= (3*(2*C+3)*C**2)**2*eps2,
            'All endpoint box corners meet the length-three L2 path-repair bound')
    return {'states_before_and_after': 2, 'L2_cap_exact': str(C), 'maximum_raw_row_sum_exact': '10',
            'maximum_row_mse_exact': str(eps2), 'maximum_repair_dual_norm_squared_exact': str(maximum_dual_norm2),
            'bounded_left_corners_checked': len(signs), 'path_endpoint_corner_pairs_checked': len(signs)**2,
            'maximum_path_scalar_error_exact': str(max_scalar), 'path_length': 3,
            'scope': 'The exact 2x2 positive-definiteness certificate and box-corner checks establish the stated inequalities for this example; the general L2 repair lemma is a separate proof.'}


def doob_checks() -> dict:
    mu, u = [F(1, 3)]*3, [F(1, 1000), F(2), F(0)]
    mean, Z = sum(p*x for p, x in zip(mu, u)), norm_squared(u, mu)
    A = [[u[i]*u[j]*mu[j]/mean for j in range(3)] for i in range(3)]
    require(A == adjoint(A, mu) and mv(A, [F(1)]*3) == u,
            'The rival selector is positive and selfadjoint, with a nonconstant positive row-sum vector on its support')
    require(matmul(A, A) != A, 'The rival selector is genuinely non-idempotent')
    require(A[2] == [0]*3 and all(A[i][2] == 0 for i in range(3)),
            'A zero selector row sum kills both its row and its column')
    support = [i for i, value in enumerate(u) if value > 0]
    nu = [mu[i]*u[i]**2/Z for i in support]
    records = []
    for scale in (F(1), F(17, 16)):
        # T=positive_constant*A*A, hence the outer selector support is literal.
        constant = scale*mean**2/Z**2
        T = [[constant*value for value in row] for row in matmul(A, A)]
        B = [[T[i][j]*u[j]/u[i] for j in support] for i in support]
        require(B == [[scale*p for p in nu] for _ in support], 'The Doob kernel is a scaled stationary rank-one kernel')
        require(B == adjoint(B, nu), 'The Doob kernel has the exact conditional stationary adjoint')
        require(matmul(T, T) == [[scale*v for v in row] for row in T] and
                matmul(B, B) == [[scale*v for v in row] for row in B],
                'Both selfadjoint positive rank-one operators have exact L2 norm equal to the scale')
        defect_mu = norm_squared([value-u[i] for i, value in enumerate(mv(T, u))], mu)/Z
        defect_nu = norm_squared([value-1 for value in mv(B, [F(1)]*2)], nu)
        require(defect_mu == defect_nu == (scale-1)**2,
                'The Doob stochastic-defect identity holds exactly without a pointwise inverse-u bound')
        require(mv(T, [F(1)]*3) != [F(1)]*3, 'The untransformed positive operator is not mistaken for a stochastic kernel')
        U, _, _ = repaired(B, nu)
        require(all(sum(row) == 1 for row in U+adjoint(U, nu)), 'Repair preserves the two actual positive-support states')
        records.append({'scale_exact': str(scale), 'positive_outer_A_coefficient_exact': str(constant),
                        'both_normalized_defects_squared_exact': str(defect_mu),
                        'exact_L2_operator_norm': str(scale)})
    v, w = [4*u[0], -u[1]/2, F(0)], [4*u[0], u[1]/2, F(0)]
    raw = [v[i]/u[i] for i in support]
    clipped = [max(F(-1), min(F(1), value)) for value in raw]
    clip_error = norm_squared([a-b for a, b in zip(raw, clipped)], nu)
    envelope_error = norm_squared([w[i]-u[i] for i in range(3)], mu)/Z
    require(all(abs(v[i]) <= w[i] for i in range(3)) and clip_error <= envelope_error,
            'Clipping the signed observable meets the positive-envelope L2 inequality')
    return {'actual_selector_states': 3, 'retained_positive_support_states': len(support),
            'selector_row_sum_u_exact': list(map(str, u)), 'normalization_Z_exact': str(Z),
            'Doob_stationary_law_exact': list(map(str, nu)), 'selector_is_projection': False,
            'scaled_kernel_examples': records, 'clipping_error_squared_exact': str(clip_error),
            'envelope_error_bound_squared_exact': str(envelope_error),
            'scope': 'A tiny non-idempotent selector with one zero row and a small positive u entry checks support, conjugation, adjoints, normalization and clipping. It is an algebraic illustration, not a constructed physical rival.'}


def nonsymmetric_doob_repair_checks() -> dict:
    t, mu = F(1, 1000), [F(1, 5)]*5
    A = [[t/2, t/2, F(0), F(0), F(0)],
         [t/2, F(3, 4)-t/2, F(1, 8), F(1, 8), F(0)],
         [F(0), F(1, 8), F(3, 4), F(1, 8), F(0)],
         [F(0), F(1, 8), F(1, 8), F(3, 4), F(0)],
         [F(0)]*5]
    require(A == adjoint(A, mu) and all(A[i][i] >= sum(A[i][j] for j in range(5) if j != i) for i in range(5)),
            'The selector is symmetric diagonally dominant, giving an exact PSD certificate')
    u = mv(A, [F(1)]*5)
    require(u == [t, 1, 1, 1, 0] and matmul(A, A) != A and max(u) == 1,
            'The positive selector is a non-idempotent L2 contraction with small and zero row sums')
    Wmap = [0, 2, 3, 1, 4]
    W = [[F(int(j == Wmap[i])) for j in range(5)] for i in range(5)]
    require(matmul(adjoint(W, mu), W) == [[F(int(i == j)) for j in range(5)] for i in range(5)],
            'The middle permutation is an L2 isometry with a genuine three-cycle')
    C = 1+t
    T = [[C*value for value in row] for row in matmul(matmul(A, W), A)]
    require(T != adjoint(T, mu) and T[4] == [0]*5 and all(T[i][4] == 0 for i in range(5)),
            'The positive outer-selector operator is non-selfadjoint and has no support excursions')
    Z = norm_squared(u, mu)
    support = [0, 1, 2, 3]
    nu = [mu[i]*u[i]**2/Z for i in support]
    B = [[T[i][j]*u[j]/u[i] for j in support] for i in support]
    Bstar = adjoint(B, nu)
    Tstar = adjoint(T, mu)
    require(B != Bstar and Bstar == [[Tstar[i][j]*u[j]/u[i] for j in support] for i in support],
            'The Doob transform preserves the weighted adjoint relation even for non-selfadjoint transports')
    raw_defects = []
    for raw, transformed in ((T, B), (Tstar, Bstar)):
        original = norm_squared([value-u[i] for i, value in enumerate(mv(raw, u))], mu)/Z
        changed = norm_squared([value-1 for value in mv(transformed, [F(1)]*4)], nu)
        require(original == changed <= t*t, 'Both Doob row-defect identities hold with epsilon=t')
        raw_defects.append(changed)
    U, fill_vector, eps2 = repaired(B, nu)
    require(max(mv(B, [F(1)]*4)) > 1 and max(mv(Bstar, [F(1)]*4)) > 1 and
            sum(p*e for p, e in zip(nu, fill_vector)) > 0,
            'Both clipping operations and the positive fill are genuinely used in this example')
    difference = [[B[i][j]-U[i][j] for j in support] for i in support]
    corners = list(itertools.product((F(-1), F(1)), repeat=4))
    max_norm2 = max(norm_squared(mv(adjoint(difference, nu), list(f)), nu) for f in corners)
    require(max_norm2 <= (2*C+3)**2*t*t, 'All sixteen left corners certify the mixed L2 repair inequality')
    raw_product = matmul(matmul(B, Bstar), B)
    fixed_product = matmul(matmul(U, adjoint(U, nu)), U)
    product_difference = [[raw_product[i][j]-fixed_product[i][j] for j in support] for i in support]
    max_path_error = max(sum(nu[i]*abs(value) for i, value in enumerate(mv(product_difference, list(g)))) for g in corners)
    path_bound = 3*(2*C+3)*C*C*t
    require(max_path_error <= path_bound, 'Sixteen terminal corners certify the path bound for all bounded endpoint pairs')
    A2 = matmul(A, A)
    Rplus = [[(1+2*t)*value for value in row] for row in A2]
    Rminus = [[t*A[i][0]*A[0][j] for j in range(5)] for i in range(5)]
    plus, minus = mv(Rplus, [F(1)]*5), mv(Rminus, [F(1)]*5)
    v, w = [a-b for a, b in zip(plus, minus)], [a+b for a, b in zip(plus, minus)]
    raw_feature = [v[i]/u[i] for i in support]
    h = [max(F(-1), min(F(1), value)) for value in raw_feature]
    clipping_error = norm_squared([a-b for a, b in zip(raw_feature, h)], nu)
    envelope_bound = norm_squared([w[i]-u[i] for i in range(5)], mu)/Z
    require(any(raw_feature[i] != h[i] for i in support) and 0 < clipping_error <= envelope_bound,
            'Two positive outer-selector probes produce a nontrivial clipping test with the claimed envelope bound')
    return {'actual_states': 5, 'positive_support_states': 4, 't_exact': str(t),
            'selector_row_sums_exact': list(map(str, u)), 'normalization_Z_exact': str(Z),
            'Doob_stationary_law_exact': list(map(str, nu)), 'L2_cap_exact': str(C),
            'transport_differs_from_its_adjoint': True, 'both_row_defects_squared_exact': list(map(str, raw_defects)),
            'row_defect_bound_epsilon_exact': str(t), 'mixed_repair_left_corners': len(corners),
            'maximum_mixed_repair_dual_norm_squared_exact': str(max_norm2),
            'mixed_repair_bound_squared_exact': str((2*C+3)**2*t*t),
            'path_length': 3, 'path_terminal_corners': len(corners),
            'maximum_bounded_path_error_exact': str(max_path_error), 'path_error_bound_exact': str(path_bound),
            'clipped_feature_exact': list(map(str, h)), 'clipping_error_squared_exact': str(clipping_error),
            'positive_envelope_bound_squared_exact': str(envelope_bound),
            'scope': 'An exact five-state algebraic example tests distinct adjoints, both clipping stages, positive fill, and outer-selector probes. Operator caps follow from the certified selector contraction and permutation isometry, with no inverse-small-u factor.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/binary_reversibility_lower_bound.json'))
    args = parser.parse_args()
    graph = build_graph()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'scope': 'Exact bounded certificates for the balanced binary temporal-marker construction and the positive-selector L2 repair bridge.',
              'weighted_graph_and_physical_model': graph_and_field_checks(graph),
              'positive_marker_gate_and_probe_words': word_checks(graph),
              'L2_transport_repair': l2_repair_checks(), 'positive_selector_Doob_transform': doob_checks(),
              'non_selfadjoint_Doob_and_repair': nonsymmetric_doob_repair_checks(),
              'largest_matrix_dimension': 5, 'largest_sparse_hidden_state_count': len(graph['labels']),
              'largest_counted_physical_state_count': len(graph['labels'])+1,
              'dense_physical_matrix_allocated': False,
              'limitations': 'The verifier builds only n=1 and does not establish an all-n theorem by enumeration. It does not calibrate the asymptotic fixed-clock constants or simulate arbitrary reversible rivals. The intended theorem keeps a fixed common rate budget and the original binary field rule; it does not remove that budget or retain the earlier numerical [k,3k] band.',
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
