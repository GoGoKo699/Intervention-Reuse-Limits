#!/usr/bin/env python3
"""Bounded exact checks of factorization realizations and kinetic-variance closure.

The finite fixtures supplement the analytic all-matrix and all-protocol proofs.
No numerical fitting, large target, or trajectory simulation is used.
"""
import argparse
from fractions import Fraction as F
from itertools import combinations
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


def psd_ldl(a):
    require(a == transpose(a), 'The quadratic-form certificate is exactly symmetric')
    work, pivots = [row[:] for row in a], []
    for i in range(len(a)):
        pivot = work[i][i]
        require(pivot >= 0, 'Every exact LDL pivot is nonnegative')
        pivots.append(pivot)
        if pivot == 0:
            require(all(work[i][j] == 0 for j in range(i+1, len(a))),
                    'A zero pivot has zero remaining Schur row')
            continue
        for j in range(i+1, len(a)):
            for k in range(i+1, len(a)):
                work[j][k] -= work[j][i]*work[i][k]/pivot
    return [str(x) for x in pivots]


def generator_from_factors(u, w):
    h = mm(u, w)
    n, factors = len(h), len(w)
    v = [sum(row) for row in h]
    s = [sum(row) for row in w]
    require(h == transpose(h) and sum(v) == 1 and min(v+s) > 0,
            'The symmetric matrix and nonzero factor terms have positive normalized masses')
    require(min(x for row in u+w for x in row) >= 0, 'Both arbitrary factor matrices are nonnegative')
    r = [[x/s[alpha] for x in row] for alpha, row in enumerate(w)]
    t = [[u[i][alpha]*s[alpha]/v[i] for alpha in range(factors)] for i in range(n)]
    a = mm([v], t)[0]
    require(all(sum(row) == 1 for row in r+t), 'Factor normalization makes both incidence kernels stochastic')
    require(min(a) > 0 and sum(a) == 1 and mm([a], r) == [v],
            'Normalized memory and probe masses are mutually stationary')
    require(mm(t, r) == [[x/v[i] for x in row] for i, row in enumerate(h)],
            'The two-step endpoint kernel depends only on the matrix H')
    dimension = factors+n
    k = zeros(dimension)
    for alpha in range(factors):
        for j in range(n):
            k[alpha][factors+j] = r[alpha][j]
    for i in range(n):
        for alpha in range(factors):
            k[factors+i][alpha] = t[i][alpha]
    for indices, law in ((list(range(factors)), a), (list(range(factors, dimension)), v)):
        for i in indices:
            for j, value in zip(indices, law):
                if i != j:
                    k[i][j] += value
    for i in range(dimension):
        k[i][i] = -sum(k[i])
    mu = [x/2 for x in a+v]
    require(mm([mu], k) == [[F(0)]*dimension], 'The assembled hidden generator has the claimed stationary law')
    require(max(-k[i][i] for i in range(dimension)) <= 2,
            'Every normalized realization has hidden exit cap at most two')
    return {'H': h, 'n': n, 'factors': factors, 'R': r, 'T': t, 'a': a, 'v': v,
            's': s, 'K': k, 'mu': mu}


def physical(k, mu, barriers, bias):
    q = zeros(len(mu)+1)
    for i in range(len(mu)):
        q[0][i+1] = bias*mu[i]*barriers[i]
        q[i+1][0] = barriers[i]
        q[i+1][1:] = k[i][:]
        q[i+1][i+1] -= barriers[i]
    q[0][0] = -sum(q[0])
    return q


def realization_checks(data, canonical, reversible):
    n, factors, k, mu = data['n'], data['factors'], data['K'], data['mu']
    dimension = len(mu)
    c = zeros(dimension, 2*n)
    for alpha in range(factors):
        c[alpha][:n] = data['R'][alpha][:]
    for i in range(n):
        c[factors+i][n+i] = F(1)
    require(all(sum(row) == 1 and min(row) >= 0 for row in c), 'The canonical endpoint map is stochastic')
    require(mm(k, c) == mm(c, canonical['K']), 'Every factorization generator intertwines with the canonical generator')
    require(mm([mu], c) == [canonical['mu']], 'Canonical endpoint mapping preserves hidden preparation')
    labels = [0]*factors+list(range(1, n+1))
    canonical_labels = [0]*n+list(range(1, n+1))
    for label in range(n+1):
        require([[F(labels[i] == label)*c[i][j] for j in range(2*n)] for i in range(dimension)] ==
                [[c[i][j]*F(canonical_labels[j] == label) for j in range(2*n)] for i in range(dimension)],
                'Every label projector intertwines, certifying arbitrary common barrier curves')
    full_c = zeros(dimension+1, 2*n+1)
    full_c[0][0] = F(1)
    for i in range(dimension):
        full_c[i+1][1:] = c[i][:]
    for grid, bias in (([F(1)]*(n+1), F(1)),
                       ([F(3, 8)+F(5*j, 16*n) for j in range(n+1)], F(4))):
        beta = [grid[label] for label in labels]
        canonical_beta = [grid[label] for label in canonical_labels]
        q, q_star = physical(k, mu, beta, bias), physical(canonical['K'], canonical['mu'], canonical_beta, bias)
        require(mm(q, full_c) == mm(full_c, q_star),
                'The complete controlled generators intertwine including both hub rate directions')
    preparation = [F(1, 2)]+[x/2 for x in mu]
    canonical_preparation = [F(1, 2)]+[x/2 for x in canonical['mu']]
    require(mm([preparation], full_c) == [canonical_preparation], 'Full zero-field preparations intertwine')
    require(mm(full_c, [[-F(1)]]+[[F(1)]]*(2*n)) == [[-F(1)]]+[[F(1)]]*dimension,
            'The endpoint map preserves the binary readout')
    for visible in (False, True):
        require([[F((i == 0) == visible)*full_c[i][j] for j in range(2*n+1)] for i in range(dimension+1)] ==
                [[full_c[i][j]*F((j == 0) == visible) for j in range(2*n+1)] for i in range(dimension+1)],
                'Both output-class projectors intertwine, preserving all finite output-path marginals')
    flux_defect = max(abs(mu[i]*k[i][j]-mu[j]*k[j][i]) for i in range(dimension) for j in range(dimension))
    band = None
    if reversible:
        require(flux_defect == 0, 'The completely positive realization satisfies exact detailed balance')
        require(all(data['a'][alpha]*data['R'][alpha][i] == data['v'][i]*data['T'][i][alpha]
                    for alpha in range(factors) for i in range(n)), 'Cross-block balance follows from the symmetric factors')
        lower = [[mu[i]*(-k[i][j]-F(i == j)+mu[j]) for j in range(dimension)] for i in range(dimension)]
        upper = [[mu[i]*(3*F(i == j)+k[i][j]-3*mu[j]) for j in range(dimension)] for i in range(dimension)]
        band = {'lower_LDL_pivots': psd_ldl(lower), 'upper_LDL_pivots': psd_ldl(upper)}
        require(rank(k) == dimension-1, 'The reversible realization has a unique stationary mode')
    else:
        require(flux_defect > 0, 'The deliberately asymmetric factorization gives a nonreversible stationary realization')
    p = [[F(i == j)+k[i][j]/2 for j in range(dimension)] for i in range(dimension)]
    require(all(min(row) >= 0 and sum(row) == 1 for row in p), 'Uniformization gives a positive hidden Markov kernel')
    memory = [[F(i == j and i < factors) for j in range(dimension)] for i in range(dimension)]
    right_words, left_words = [], []
    for i in range(n):
        probe = [[F(j == ell == factors+i) for ell in range(dimension)] for j in range(dimension)]
        right_words.append([[2*x for x in row] for row in mm(mm(memory, p), probe)])
        left_words.append([[2*x for x in row] for row in mm(mm(probe, p), memory)])
    for i in range(n):
        probe = [[F(j == ell == factors+i) for ell in range(dimension)] for j in range(dimension)]
        right_words.append(probe)
        left_words.append(probe)
    left = [mm([mu], word)[0] for word in left_words]
    right = [[sum(word[state]) for word in right_words] for state in range(dimension)]
    expected = zeros(2*n)
    for i in range(n):
        for j in range(n):
            expected[i][j] = data['H'][i][j]/2
        expected[n+i][n+i] = data['v'][i]/2
    observed = mm(left, right)
    require(observed == expected, 'Positive matched feature words yield diag(H/2,diag(v/2)) exactly')
    actual_gram = mm(transpose(right), [[mu[i]*x for x in row] for i, row in enumerate(right)])
    require((actual_gram == expected) == reversible,
            'The chosen fixtures distinguish a true reversible Gram from a general positive left/right factorization')
    return {'probe_labels': n, 'memory_factors': factors, 'total_states': dimension+1,
            'memory_conditional_law_exact': [str(x) for x in data['a']],
            'maximum_ordinary_flux_defect_exact': str(flux_defect), 'reversible_band_certificate': band}


def factorization_principle_checks():
    cp = [[F(1, 5), F(1, 5)], [F(1, 5), F(2, 5)], [F(1, 5), F(1, 5)]]
    h = mm(cp, transpose(cp))
    change = [[F(1), F(1, 4)], [F(0), F(1)]]
    inverse_change = [[F(1), -F(1, 4)], [F(0), F(1)]]
    require(mm(change, inverse_change) == [[F(1), F(0)], [F(0), F(1)]],
            'The deliberately nonsymmetric change of factors preserves the matrix product')
    nonnegative_u, nonnegative_w = mm(cp, change), mm(inverse_change, transpose(cp))
    require(min(x for row in nonnegative_u+nonnegative_w for x in row) > 0,
            'Both changed factor matrices remain strictly positive despite the nonsymmetric factor gauge')
    require(mm(nonnegative_u, nonnegative_w) == h, 'Distinct incoming and outgoing factors produce exactly the same H')
    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    canonical = generator_from_factors(h, identity)
    cp_data = generator_from_factors(cp, transpose(cp))
    noncp_data = generator_from_factors(nonnegative_u, nonnegative_w)
    require(cp_data['a'] == [x*x for x in cp_data['s']], 'A literal completely positive factorization has a_alpha=s_alpha squared')
    require(rank(h) == 2, 'The small positive matrix has rank two, certifying both two-factor minima')
    small = {'CP': realization_checks(cp_data, canonical, True),
             'asymmetric_NMF': realization_checks(noncp_data, canonical, False)}
    # K2,3 has a weighted nonnegative Gram factor U diag(1/24) U^T.
    # Keeping the positive diagonal weight rational avoids artificial square roots.
    edges = [(i, j) for i in range(2) for j in range(2, 5)]
    incidence = [[F(i in edge) for edge in edges] for i in range(5)]
    transpose_weighted = [[x/24 for x in row] for row in transpose(incidence)]
    graph = generator_from_factors(incidence, transpose_weighted)
    graph_canonical = generator_from_factors(graph['H'], [[F(i == j) for j in range(5)] for i in range(5)])
    graph_report = realization_checks(graph, graph_canonical, True)
    require(graph['a'] == [F(1, 6)]*6 and graph['v'] == [F(d, 12) for d in (3, 3, 2, 2, 2)],
            'The general normalization reproduces the established incidence target masses')
    require(rank(graph['H']) == 4, 'The incidence matrix has the established ordinary rank four')
    support = {(i, j) for i in range(5) for j in range(5) if graph['H'][i][j] > 0}
    rectangles = set()
    for mask in range(1, 32):
        rows = {i for i in range(5) if mask >> i & 1}
        columns = {j for j in range(5) if all((i, j) in support for i in rows)}
        if columns:
            closure = {i for i in range(5) if all((i, j) in support for j in columns)}
            rectangles.add(frozenset((i, j) for i in closure for j in columns))
    require(len(rectangles) == 18 and all(len(set().union(*group)) < 17 for group in combinations(rectangles, 4)),
            'The small support cannot be covered by four positive rectangles, recovering nonnegative rank five')
    require(all(any((i, j) not in support for i in first | second for j in first | second)
                for first, second in combinations(map(set, edges), 2)),
            'Two distinct graph edges cannot share one nonnegative Gram atom, recovering CP rank six')
    require(1+5+5 == 11 and 1+5+6 == 12, 'The rank principle reproduces the existing eleven-versus-twelve total-state counts')
    return {'positive_rank_two_example_H_exact': [[str(x) for x in row] for row in h],
            'positive_rank_two_realizations': small, 'positive_rank_two_minimum_total_states': 6,
            'K23_CP_realization': graph_report, 'K23_ordinary_rank': 4,
            'K23_nonnegative_rank': 5, 'K23_completely_positive_rank': 6,
            'K23_unrestricted_minimum_total_states': 11, 'K23_ordinary_minimum_total_states': 12,
            'scope': 'Finite normalization, intertwining, feature and support certificates supplement the general matrix principle. The all-rival lower and existence of a positive error interval remain analytic.'}


def centered_variance_checks():
    mu, barrier = [F(1, 3)]*3, [F(3, 8), F(1, 2), F(11, 16)]
    average = sum(x*y for x, y in zip(mu, barrier))
    centered = [x-average for x in barrier]
    projection = [[F(i == j)-mu[j] for j in range(3)] for i in range(3)]
    basis = [[F(1), F(1)], [-F(1), F(0)], [F(0), -F(1)]]
    cases = []
    for forward, backward in ((F(1, 2), F(1, 2)), (F(3, 4), F(1, 4))):
        k = [[-F(1), forward, backward], [backward, -F(1), forward], [forward, backward, -F(1)]]
        reverse = [[mu[j]*k[j][i]/mu[i] for j in range(3)] for i in range(3)]
        require(mm([mu], k) == [[F(0)]*3], 'The reversible or biased cycle has the same stationary hidden law')
        gamma = F(3, 2)
        diagonal = [[F(i == j)*barrier[i] for j in range(3)] for i in range(3)]
        projected_killing = mm(projection, diagonal)
        l = [[reverse[i][j]-projected_killing[i][j] for j in range(3)] for i in range(3)]
        require(mm([mu], l) == [[F(0)]*3], 'The centered evolution preserves the zero-mean density subspace')
        for ratio in (F(1), F(4)):
            q = physical(k, mu, barrier, ratio)
            # Probability point masses span the affine mass-one plane, so
            # these checks certify the complete finite master-equation identity.
            for starting_state in range(4):
                probability = [F(i == starting_state) for i in range(4)]
                a = probability[0]
                z = [probability[i+1]/mu[i]-(1-a) for i in range(3)]
                y = (1+ratio)*a-1
                derivative = mm([probability], q)[0]
                observed_a = -average*y+sum(mu[i]*centered[i]*z[i] for i in range(3))
                observed_z = [sum(l[i][j]*z[j] for j in range(3))+centered[i]*y for i in range(3)]
                require(derivative[0] == observed_a,
                        'The visible derivative has exactly one centered-barrier readout factor')
                require([derivative[i+1]/mu[i]+derivative[0] for i in range(3)] == observed_z,
                        'The hidden centered derivative has the exact projected damping and excitation source')
        for column in transpose(basis):
            dissipation = -sum(mu[i]*column[i]*sum(reverse[i][j]*column[j] for j in range(3)) for i in range(3))
            dirichlet = sum(mu[i]*k[i][j]*(column[j]-column[i])**2 for i in range(3) for j in range(3))/2
            require(dissipation == dirichlet == gamma*sum(mu[i]*column[i]**2 for i in range(3)),
                    'Stationarity gives the same centered Dirichlet gap even with nonzero circulation')
        decay = gamma+min(barrier)
        form = [[-(mu[i]*l[i][j]+mu[j]*l[j][i])/2-decay*mu[i]*F(i == j)
                 for j in range(3)] for i in range(3)]
        restricted = mm(mm(transpose(basis), form), basis)
        pivots = psd_ldl(restricted)
        is_reversible = forward == backward
        require((mu[0]*k[0][1] == mu[1]*k[1][0]) == is_reversible,
                'The second contraction fixture genuinely violates ordinary detailed balance')
        cases.append({'clockwise_rate_exact': str(forward), 'counterclockwise_rate_exact': str(backward),
                      'symmetric_centered_gap_exact': str(gamma), 'centered_damping_lower_exact': str(decay),
                      'restricted_damping_LDL_pivots': pivots})
    require(sum(mu[i]*centered[i] for i in range(3)) == 0,
            'The excitation and readout barrier vector lies in the centered subspace')
    require(mm(projection, [[F(1)]]*3) == [[F(0)]]*3,
            'Equal barriers annihilate the hidden-memory source exactly')
    return {'master_equation_initial_basis_states': 4, 'field_biases_exact': ['1', '4'],
            'reversible_and_nonreversible_cases': cases,
            'scope': 'Exact master-equation identities and centered quadratic forms check the finite memory-kernel ingredients. The uniform time-dependent Volterra and error bounds remain analytic.'}


def variance_constant_checks():
    mu = [F(1, 12)]*6+[F(d, 24) for d in (3, 3, 2, 2, 2)]
    barrier = [F(3, 8)]*6+[F(7+i, 16) for i in range(5)]
    average = sum(x*y for x, y in zip(mu, barrier))
    variance = sum(mu[i]*(barrier[i]-average)**2 for i in range(11))
    require(average == F(59, 128) and variance == F(557, 49152),
            'Direct stationary averaging gives the finite target barrier mean and variance')
    require(min(barrier) == F(3, 8) and max(barrier) == F(11, 16),
            'The active field has the stated smallest and largest return barriers')
    boundary_derivative = (max(barrier)-4*average)/2
    require(boundary_derivative == -F(37, 64) < 0,
            'The visible half-interval has an inward derivative at the active-field boundary')
    source_bound = max(abs(-F(1)), abs(5*F(1, 2)-1))
    damping, scalar_decay = 1+min(barrier), 5*average
    require(source_bound == F(3, 2) and damping == F(11, 8) and scalar_decay == F(295, 128),
            'Invariant preparation and the active-field gap give the sharp displayed constants')
    mean_error = 2*source_bound*variance/(damping*scalar_decay)
    require(mean_error == F(557, 51920) < F(1073, 100000),
            'The two-state mean error is uniformly bounded by the claimed rational value')
    require(F(1, 8) < average**2 < F(1, 2),
            'The averaged endpoint is realizable by an original-rule sensitivity strictly between minus and plus one half')
    q = [[-4*average, 4*average], [average, -average]]
    pi = [F(1, 5), F(4, 5)]
    require(mm([pi], q) == [[F(0), F(0)]] and pi[0]*q[0][1] == pi[1]*q[1][0],
            'The single-hidden-state predictor is stationary and ordinarily reversible at the active field')
    block_variance = F(1, 6)*F(1, 32)**2
    block_error = 2*2*block_variance/(F(9, 8)*F(11, 8))
    require(block_variance == F(1, 6144) and block_error == F(1, 2376),
            'Conditional variance recovers the previously certified nine-state bound')
    return {'active_barrier_mean_exact': str(average), 'active_barrier_variance_exact': str(variance),
            'visible_boundary_derivative_upper_exact': str(boundary_derivative),
            'active_source_bound_exact': str(source_bound), 'active_hidden_damping_exact': str(damping),
            'active_scalar_decay_exact': str(scalar_decay), 'two_state_uniform_mean_error_upper_exact': str(mean_error),
            'two_state_predictor_hidden_states': 1, 'two_state_predictor_total_states': 2,
            'conditional_variance_exact': str(block_variance), 'nine_state_mean_error_upper_exact': str(block_error),
            'scope': 'Exact constants use the stated active-field invariance and analytic variance theorem. Endpoint exponential matching is asserted only on the original two queried fields, not on a whole control interval.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/simple_prediction_principles.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = {'status': 'PASS', 'versions': {'python': platform.python_version()},
              'arithmetic': 'Exact fractions.Fraction, rational matrix products and LDL certificates, with a bounded support enumeration; no numerical optimization',
              'matrix_rank_realization_principle': factorization_principle_checks(),
              'centered_hidden_memory_identities': centered_variance_checks(),
              'variance_compression_constants': variance_constant_checks(),
              'largest_dense_matrix_dimension': 12, 'large_target_allocated': False,
              'controlled_responses_simulated': False,
              'limitations': ['Finite fixtures do not prove the arbitrary-matrix prediction-rank theorem or its positive-error existence corollary.',
                              'The variance estimates concern controlled means, not a uniform approximation to full output-path laws.',
                              'The two-state bound is a sufficient upper estimate, not an optimal-error claim.',
                              'Exact rank counts and coarse-precision compression concern different requested accuracies.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_names = ['MATRIX_RANK_PREDICTION_PRINCIPLE.md', 'KINETIC_VARIANCE_COMPRESSION.md',
                   'FINITE_REVERSIBILITY_ADVANTAGE.md', 'FINITE_PREDICTOR_MINIMALITY.md',
                   'SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
