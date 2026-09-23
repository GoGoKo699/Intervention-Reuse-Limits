#!/usr/bin/env python3
"""Bounded exact certificates for the nine-state symmetry compression.

Exact finite generators and contraction coefficients support the separate
all-protocol proof. The small propagator checks are not an optimal-error search.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.linalg import expm

CHECKS = 0
MAX_DENSE = 0
PROOFS = {
    'SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md': '38bc3447bbe6578eb37a6917d5e6ef700696077a3c98c499be47ed1dbff357cf',
    'FINITE_REVERSIBILITY_ADVANTAGE.md': 'f112054e19a2ed86f4998481d6b130df2001eea32c92bf3876d86c9ee676e1fe',
}


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def mm(a, b):
    return [[sum((a[i][t]*b[t][j] for t in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b, scale=F(1)):
    return [[x+scale*y for x, y in zip(row, other)] for row, other in zip(a, b)]


def generator(off):
    q = [row[:] for row in off]
    for i in range(len(q)):
        require(q[i][i] == 0 and min(q[i]) >= 0, 'Off-diagonal generator specification is nonnegative')
        q[i][i] = -sum(q[i])
    return q


def array(a):
    global MAX_DENSE
    MAX_DENSE = max(MAX_DENSE, len(a), len(a[0]))
    require(MAX_DENSE <= 12, 'No dense calculation exceeds the twelve-state target')
    return np.asarray([[float(x) for x in row] for row in a])


def tv(v):
    return sum(abs(x) for x in v)/2


def physical(k, mu, barriers, ratio):
    q = zeros(len(mu)+1)
    for i in range(len(mu)):
        q[0][i+1] = ratio*mu[i]*barriers[i]
        q[i+1][0] = barriers[i]
        q[i+1][1:] = k[i][:]
        q[i+1][i+1] -= barriers[i]
    q[0][0] = -sum(q[0])
    return q


def detailed_balance(q, pi):
    return all(pi[i]*q[i][j] == pi[j]*q[j][i]
               for i in range(len(q)) for j in range(len(q)))


def psd_ldl(matrix):
    work = [row[:] for row in matrix]
    require(work == [list(row) for row in zip(*work)], 'Weighted spectral certificate is symmetric')
    pivots = []
    for i in range(len(work)):
        pivot = work[i][i]
        require(pivot >= 0, 'Exact spectral LDL pivot is nonnegative')
        pivots.append(str(pivot))
        if pivot == 0:
            require(all(work[i][j] == 0 for j in range(i+1, len(work))), 'Zero LDL pivot has zero residual row')
            continue
        for j in range(i+1, len(work)):
            for t in range(i+1, len(work)):
                work[j][t] -= work[j][i]*work[i][t]/pivot
    return pivots


def target_and_quotient():
    edges = [(left, right) for left in (1, 2) for right in (3, 4, 5)]
    degrees = [3, 3, 2, 2, 2]
    mu = [F(1, 12)]*6+[F(d, 24) for d in degrees]
    incidence_off = zeros(11)
    for e, vertices in enumerate(edges):
        for vertex in vertices:
            incidence_off[e][5+vertex] = F(1, 2)
            incidence_off[5+vertex][e] = F(1, degrees[vertex-1])
    k0 = generator(incidence_off)
    refresh = zeros(11)
    for i in range(11):
        for j in range(11):
            if (i < 6) == (j < 6):
                refresh[i][j] = 2*mu[j]
    k = add(k0, refresh)
    for i in range(11):
        k[i][i] -= 1
    swap = {1: 1, 2: 2, 3: 4, 4: 3, 5: 5}
    theta = [edges.index((a, swap[b])) for a, b in edges]+[5+swap[i] for i in range(1, 6)]
    require(all(theta[theta[i]] == i for i in range(11)), 'Hidden label exchange is an involution')
    require(all(mu[i] == mu[theta[i]] for i in range(11)), 'The involution preserves the hidden law')
    require(all(k[i][j] == k[theta[i]][theta[j]] for i in range(11) for j in range(11)), 'The hidden generator commutes with the involution')
    require(sum(mu) == 1 and mm([mu], k) == [[F(0)]*11], 'The hidden target law is normalized and stationary')
    require(detailed_balance(k, mu), 'The target hidden generator has ordinary detailed balance')
    orbits = []
    for i in range(11):
        if all(i not in orbit for orbit in orbits):
            orbits.append(sorted({i, theta[i]}))
    require(len(orbits) == 8 and sum(len(o) == 2 for o in orbits) == 3, 'Three paired orbits give eight hidden quotient states')
    quotient_mu = [sum(mu[i] for i in orbit) for orbit in orbits]
    quotient_k = [[sum(k[orbit[0]][j] for j in other) for other in orbits] for orbit in orbits]
    hidden_projection = [[F(i in orbit) for orbit in orbits] for i in range(11)]
    require(mm(k, hidden_projection) == mm(hidden_projection, quotient_k), 'Exact hidden generator strong lumpability')
    require(detailed_balance(quotient_k, quotient_mu), 'The quotient has ordinary hidden detailed balance')
    require(all(sum(row) == 0 for row in quotient_k), 'The quotient hidden generator is conservative')
    require(max(-k[i][i] for i in range(11)) <= 2 and max(-quotient_k[i][i] for i in range(8)) <= 2, 'Both hidden exit caps are at most two')
    # Weighted PSD: -K >= I-Pi and -K <= 3(I-Pi).
    lower, upper = zeros(8), zeros(8)
    for i in range(8):
        for j in range(8):
            variance = quotient_mu[i]*F(i == j)-quotient_mu[i]*quotient_mu[j]
            dirichlet = -quotient_mu[i]*quotient_k[i][j]
            lower[i][j] = dirichlet-variance
            upper[i][j] = 3*variance-dirichlet
    lower_pivots, upper_pivots = psd_ldl(lower), psd_ldl(upper)
    projection = [[F(1)]+[F(0)]*8]+[[F(0)]+row for row in hidden_projection]
    physical_theta = [0]+[i+1 for i in theta]
    pi = [F(1, 2)]+[x/2 for x in mu]
    quotient_pi = [F(1, 2)]+[x/2 for x in quotient_mu]
    require(mm([pi], projection) == [quotient_pi], 'The preparation pushes exactly to the quotient preparation')
    require(mm(projection, [[-F(1)]]+[[F(1)]]*8) == [[-F(1)]]+[[F(1)]]*11, 'The binary readout is preserved by the quotient')
    target_q, averaged_q, quotient_q, defects, table = [], [], [], [], {}
    beta = [F(6, 16)]*6+[F(j+6, 16) for j in range(1, 6)]
    expected_table = {
        'A-memory': (6, F(41, 24), F(37, 24)),
        'A-probe': (5, F(5, 3), F(57, 32)),
        'memory-memory': (15, F(2), F(11, 8)),
        'memory-probe incident': (12, F(7, 3), F(41, 24)),
        'memory-probe nonincident': (18, F(7, 4), F(9, 8)),
        'probe-probe': (10, F(2), F(23, 16)),
    }
    for field, ratio in enumerate((F(1), F(4))):
        b = [F(1)]*11 if field == 0 else beta[:]
        averaged_b = b[:]
        averaged_b[8] = averaged_b[9] = (b[8]+b[9])/2
        q = physical(k, mu, b, ratio)
        averaged = physical(k, mu, averaged_b, ratio)
        reduced = physical(quotient_k, quotient_mu, [averaged_b[o[0]] for o in orbits], ratio)
        defect = add(q, averaged, F(-1))
        require(mm(averaged, projection) == mm(projection, reduced), 'The full averaged physical generator intertwines the nine-state quotient')
        for full_q, law in ((q, mu), (averaged, mu), (reduced, quotient_mu)):
            stationary = [1/(1+ratio)]+[ratio*x/(1+ratio) for x in law]
            require(detailed_balance(full_q, stationary), 'Every full physical model has ordinary fixed-field detailed balance')
        require(all(averaged[i][j] == averaged[physical_theta[i]][physical_theta[j]] for i in range(12) for j in range(12)), 'The averaged full generator is even')
        require(all(defect[i][j] == -defect[physical_theta[i]][physical_theta[j]] for i in range(12) for j in range(12)), 'The perturbation is odd')
        eta = max(tv(row) for row in defect)
        require(eta == (F(0) if field == 0 else F(1, 32)), 'Exact diagonal-included row defect equals the claimed eta')
        # Verify the odd-source formula on a basis of all even row vectors.
        d = (b[8]-b[9])/2
        for orbit in [[0]]+[[i+1 for i in o] for o in orbits]:
            v = [F(i in orbit, len(orbit)) for i in range(12)]
            expected = [F(0)]*12
            expected[9] = d*(ratio*mu[8]*v[0]-v[9])
            expected[10] = -expected[9]
            require(mm([v], defect) == [expected], 'Every even basis row has the exact two-probe odd source')
        # On each odd basis vector the hub is absent and refresh is -I.
        for orbit in orbits:
            if len(orbit) != 2:
                continue
            v = [F(0)]*11
            v[orbit[0]], v[orbit[1]] = F(1), F(-1)
            require(mm([v], refresh) == [[F(0)]*11], 'Odd rows have zero conditional-refresh image')
            residual = mm([v], k0)[0]
            expected = [F(0)]+[residual[i]-v[i]*(1+averaged_b[i]) for i in range(11)]
            require(mm([[F(0)]+v], averaged) == [expected], 'Odd propagation is incidence plus killing at least one plus b_min')
        buckets = {name: [] for name in expected_table}
        for i in range(12):
            for j in range(i+1, 12):
                if i == 0:
                    name = 'A-memory' if j <= 6 else 'A-probe'
                elif j <= 6:
                    name = 'memory-memory'
                elif i >= 7:
                    name = 'probe-probe'
                else:
                    name = 'memory-probe incident' if j-6 in edges[i-1] else 'memory-probe nonincident'
                coefficient = averaged[i][j]+averaged[j][i]+sum(min(averaged[i][z], averaged[j][z]) for z in range(12) if z not in (i, j))
                buckets[name].append(coefficient)
                require(coefficient >= (F(5, 3) if field == 0 else F(9, 8)), 'Each rational row pair meets the claimed Dobrushin contraction')
        for name, values in buckets.items():
            count, zero_min, high_min = expected_table[name]
            require(len(values) == count and min(values) == (zero_min if field == 0 else high_min), 'Exact row-pair class minimum agrees with the analytic table')
            table.setdefault(name, {'pairs': count})['zero' if field == 0 else 'high'] = str(min(values))
        require(min(averaged_b) >= F(3, 8), 'The common hub reset and odd killing lower bound hold')
        target_q.append(q)
        averaged_q.append(averaged)
        quotient_q.append(reduced)
        defects.append(defect)
    return {
        'q': target_q, 'averaged': averaged_q, 'quotient': quotient_q, 'defects': defects,
        'pi': pi, 'quotient_pi': quotient_pi, 'projection': projection,
        'report': {'target_total_states': 12, 'quotient_total_states': 9,
                   'quotient_hidden_masses_exact': [str(x) for x in quotient_mu],
                   'target_hidden_exit_max_exact': str(max(-k[i][i] for i in range(11))),
                   'quotient_hidden_exit_max_exact': str(max(-quotient_k[i][i] for i in range(8))),
                   'quotient_band_lower_LDL_pivots': lower_pivots,
                   'quotient_band_upper_LDL_pivots': upper_pivots,
                   'Dobrushin_exact_table': table}}


def constant_checks():
    eta, gamma, odd_rate, reset = F(1, 32), F(9, 8), F(11, 8), F(3, 8)
    source_density, probe_mass = F(2), F(1, 12)
    require(source_density*probe_mass == F(1, 6), 'Two-field invariant-box source coefficient is one sixth')
    require(F(4)*F(1, 2) <= source_density, 'Both allowed fields point inward at the hidden density ceiling')
    require(F(2)-F(4)*F(1, 2) == 0, 'The high-field hub boundary estimate points inward')
    require(F(1)-2*F(1, 2) == 0, 'The zero-field hub boundary derivative vanishes')
    bound = 2*eta**2/(3*gamma*odd_rate)
    require(bound == F(1, 2376), 'The final two-field binary-mean bound has the correct factors')
    beta3, beta4 = F(9, 16), F(10, 16)
    negative_half_difference = (1/beta3-1/beta4)/2
    positive_MVT_bound = (beta4-beta3)/(2*beta3)
    require(negative_half_difference == F(4, 45) and positive_MVT_bound == F(1, 18), 'Full-interval negative endpoint and positive mean-value constants are exact')
    require(positive_MVT_bound <= negative_half_difference, 'The negative-field half-difference dominates the positive bound')
    full_bound = 4*negative_half_difference**2/(3*reset*odd_rate)
    require(full_bound == F(4096, 200475), 'Full-interval bound uses its weaker occupation and reset constants')
    require((beta3+beta4)/2 == F(19, 32), 'The averaged high-field barrier is admissible and exact')
    require(beta3*beta4 < ((beta3+beta4)/2)**2, 'The arithmetic average of unequal exponential curves cannot itself be the endpoint exponential')
    return {'two_field_mean_upper_exact': str(bound), 'two_field_mean_upper_decimal': float(f'{float(bound):.12g}'),
            'all_field_mean_upper_exact': str(full_bound), 'eta_over_k_exact': str(eta),
            'odd_decay_over_k_exact': str(odd_rate), 'full_law_decay_over_k_exact': str(gamma),
            'all_field_scope': 'Arithmetic-average barrier curves, not one exponential sensitivity over the full interval.'}


def numerical_checks(data):
    q = [array(x) for x in data['q']]
    avg = [array(x) for x in data['averaged']]
    quotient = [array(x) for x in data['quotient']]
    projection = array(data['projection'])
    pi = np.asarray([float(x) for x in data['pi']])
    quotient_pi = np.asarray([float(x) for x in data['quotient_pi']])
    s, sq = np.array([-1.]+[1.]*11), np.array([-1.]+[1.]*8)
    clock = math.log(2)/8
    schedules = [[], [(1, .2)], [(1, 2.)], [(1, .3), (0, .2), (1, 1.2)],
                 [(i % 2, clock) for i in range(64)],
                 [(1-i % 2, .35) for i in range(32)], [(1, 30.), (0, .5), (1, 4.)]]
    errors, closure_residuals, box_excess = [], [], []
    mu = np.asarray([float(x*2) for x in data['pi'][1:]])
    for schedule in schedules:
        p, reference, reduced = pi.copy(), pi.copy(), quotient_pi.copy()
        for field, duration in schedule:
            p = p @ expm(duration*q[field])
            reference = reference @ expm(duration*avg[field])
            reduced = reduced @ expm(duration*quotient[field])
            box_excess.append(max(p[0]-.5, float(np.max(p[1:]/mu))-2, 0.))
        error = abs(float((p-reference) @ s))
        residual = float(np.max(np.abs(reference @ projection-reduced)))
        require(error <= 1/2376+2e-13, 'Each bounded switched experiment satisfies the uniform analytic bound')
        require(residual <= 4e-13 and abs(float(reference@s-reduced@sq)) <= 4e-13, 'Full averaged and nine-state quotient predictions coincide')
        errors.append(float(f'{error:.12g}'))
        closure_residuals.append(float(f'{residual:.12g}'))
    require(max(box_excess) <= 4e-13, 'Sampled exact propagators preserve the two-field occupation box')
    # A nonzero response with +/- perturbations and three amplitudes checks
    # the cancellation structure independently of merely tiny full errors.
    schedule = [(1, .3), (0, .2), (1, 1.2)]
    amplitudes, scaled_errors = [], []
    for amplitude in (1., .5, .25):
        plus, minus, base = pi.copy(), pi.copy(), pi.copy()
        for field, duration in schedule:
            v = array(data['defects'][field])
            plus = plus @ expm(duration*(avg[field]+amplitude*v))
            minus = minus @ expm(duration*(avg[field]-amplitude*v))
            base = base @ expm(duration*avg[field])
        err = abs(float((plus-base)@s))
        require(abs(float((plus-minus)@s)) <= 3e-14, 'Opposite symmetry perturbations have exactly even observed response up to rounding')
        require(0 < err <= amplitude**2/2376, 'Nonzero finite-amplitude response obeys the quadratic bound')
        amplitudes.append({'amplitude': amplitude, 'mean_error': float(f'{err:.12g}')})
        scaled_errors.append(err/amplitude**2)
    require(max(scaled_errors)/min(scaled_errors) < 1.01, 'Small finite-amplitude responses exhibit the expected quadratic scaling')
    return {'deterministic_protocol_count': len(schedules), 'maximum_segments': max(map(len, schedules)),
            'sample_mean_errors': errors, 'quotient_closure_residuals': closure_residuals,
            'symmetry_amplitude_diagnostics': amplitudes,
            'scope': 'Bounded deterministic implementation checks; neither an exhaustive protocol search nor an estimate of optimal rival error.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/symmetric_compression.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    bindings = {}
    for name, expected in PROOFS.items():
        actual = hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        require(actual == expected, 'Frozen proof hash matches: '+name)
        bindings[str(Path('docs')/name)] = actual
    data = target_and_quotient()
    constants = constant_checks()
    numerical = numerical_checks(data)
    report = {'status': 'PASS', 'checks': CHECKS, 'maximum_dense_dimension': MAX_DENSE,
              'python_version': platform.python_version(), 'numpy_version': np.__version__,
              'scipy_version': scipy.__version__,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'proof_snapshot_sha256': bindings, 'construction': data['report'],
              'analytic_constants': constants, 'bounded_propagator_diagnostics': numerical,
              'limitations': ['The all-protocol guarantee is proved in the companion note, not by finite trajectories.',
                              'This sufficient nine-state approximation does not identify an optimal state count or optimal error.',
                              'The all-field upper uses averaged barrier curves; exponential endpoint matching supports only the two-field claim.']}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': 'PASS', 'checks': CHECKS, 'maximum_dense_dimension': MAX_DENSE,
                      'two_field_mean_upper': constants['two_field_mean_upper_exact'], 'output': str(args.output)}, sort_keys=True))


if __name__ == '__main__':
    main()
