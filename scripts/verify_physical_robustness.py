#!/usr/bin/env python3
"""Small exact and numerical checks of physical interface and reversal scope.

Finite fixtures supplement, rather than prove, the uniform perturbation and
stationary Markov-projection theorems. No microscopic implementation is modeled.
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
from scipy.integrate import quad, quad_vec
from scipy.linalg import expm


CHECKS = 0
MAX_DENSE = 0
PROOFS = {
    'PHYSICAL_INTERFACE_ROBUSTNESS.md': '8b003b51e7a98e3752dced5be7d1aad62ca7a08f438bd495003e7bb2cf6f8117',
    'SINGLE_FORCE_CONFORMATIONAL_MODEL.md': '8703852221c67f1b763c38ab8aa90549b70bba65ec20c1f177df7cc320c59c8d',
    'PHYSICAL_REVERSAL_REALIZATION.md': 'b346f8e550e4f0bac468e38cd89b25e17dc98cf7485084988b87435f339ba727',
}


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def array(a):
    global MAX_DENSE
    MAX_DENSE = max(MAX_DENSE, len(a), len(a[0]))
    if MAX_DENSE > 6:
        raise AssertionError('Dense fixture exceeds six states')
    return np.asarray([[float(x) for x in row] for row in a])


def physical(k, mu, beta, bias):
    n = len(mu)
    q = zeros(n+1)
    for i in range(n):
        q[0][i+1] = bias*mu[i]*beta[i]
        q[i+1][0] = beta[i]
        q[i+1][1:] = k[i][:]
        q[i+1][i+1] -= beta[i]
    q[0][0] = -sum(q[0])
    return q


def conductance_generator(mu, conductances):
    k = zeros(len(mu))
    for (i, j), value in conductances.items():
        k[i][j], k[j][i] = value/mu[i], value/mu[j]
    for i in range(len(mu)):
        k[i][i] = -sum(k[i])
    return k


def bell_and_erasure_checks():
    mu, g = [F(1, 2), F(1, 3), F(1, 6)], [F(-1, 2), F(0), F(1, 2)]
    conductances = {(0, 1): F(1, 12), (0, 2): F(1, 24), (1, 2): F(1, 18)}
    k = conductance_generator(mu, conductances)
    attempt = 16.
    energy_residuals, cases = [], []
    for base in (F(2, 3), F(1), F(3, 2)):
        h = 2*math.log(float(base))
        beta = [base**int(2*x-2) for x in g]
        q = physical(k, mu, beta, base**4)
        weights = [1/base**2]+[x*base**2 for x in mu]
        pi = [x/sum(weights) for x in weights]
        saddle_weights = zeros(4)
        for i in range(3):
            saddle_weights[0][i+1] = saddle_weights[i+1][0] = mu[i]*base**int(2*g[i])/16
        for (i, j), value in conductances.items():
            saddle_weights[i+1][j+1] = saddle_weights[j+1][i+1] = value*base**2/16
        require(all(16*saddle_weights[i][j]/weights[i] == q[i][j]
                    for i in range(4) for j in range(4) if i != j),
                'Exact rational Boltzmann and saddle weights reconstruct every Arrhenius rate')
        require(all(sum(row) == 0 for row in q)
                and all(q[i][j] >= 0 for i in range(4) for j in range(4) if i != j),
                'The independently assembled force rates form a conservative positive generator')
        require(mm([pi], q) == [[F(0)]*4], 'Bell equilibrium law balances the full physical generator')
        require(all(pi[i]*q[i][j] == pi[j]*q[j][i] for i in range(4) for j in range(4)),
                'Single-force rates satisfy ordinary detailed balance')
        energies = [h]+[-math.log(float(x))-h for x in mu]
        residual = 0.
        for i in range(3):
            barrier = -math.log(float(mu[i]))+math.log(attempt)-float(g[i])*h
            require(barrier >= max(energies[0], energies[i+1]), 'External saddle is above both well energies')
            for a, b in ((0, i+1), (i+1, 0)):
                residual = max(residual, abs(attempt*math.exp(energies[a]-barrier)-float(q[a][b])))
        for (i, j), value in conductances.items():
            barrier = math.log(attempt/float(value))-h
            require(barrier >= max(energies[i+1], energies[j+1]), 'Internal saddle is above both hidden wells')
            for a, b in ((i, j), (j, i)):
                residual = max(residual, abs(attempt*math.exp(energies[a+1]-barrier)-float(k[a][b])))
        require(residual < 4e-15, 'Arrhenius reconstruction agrees with independently assembled rational rates')
        readout = [-F(1)]+[F(1)]*3
        mean = sum(x*y for x, y in zip(pi, readout))
        require(mean == (base**4-1)/(base**4+1), 'The equilibrium binary mean has the correct bias sign')
        energy_residuals.append(float(f'{residual:.12g}'))
        cases.append({'exp_half_field_exact': str(base), 'equilibrium_mean_exact': str(mean)})
    partition = [[F(1), F(0)]]+[[F(0), F(1)]]*3
    lumped_residuals = []
    full = np.array([.2, .5, .1, .2])
    reduced = full @ array(partition)
    for bias, returned, duration in ((F(4), F(3, 4), F(1, 5)), (F(1, 2), F(2), F(2, 3))):
        q = physical(k, mu, [returned]*3, bias)
        two = [[-bias*returned, bias*returned], [returned, -returned]]
        require(mm(q, partition) == mm(partition, two), 'Common hidden return rates make the visible partition strongly lumpable')
        full = full @ expm(float(duration)*array(q))
        reduced = reduced @ expm(float(duration)*array(two))
        residual = float(np.max(np.abs(full @ array(partition)-reduced)))
        require(residual < 2e-14, 'Common-return controlled visible law equals its two-state reduction')
        lumped_residuals.append(float(f'{residual:.12g}'))
    stationary = [F(1, 2)]+[x/2 for x in mu]
    barrier_matrices = []
    for multiplier in (F(1), F(3, 2)):
        rates = {(0, 1): F(1, 10)*multiplier, (0, 2): F(1, 12)/multiplier,
                 (0, 3): F(1, 15), (1, 2): F(1, 20)*multiplier, (2, 3): F(1, 30)}
        q = conductance_generator(stationary, rates)
        require(mm([stationary], q) == [[F(0)]*4], 'Barrier-only controls share one exact stationary distribution')
        barrier_matrices.append(q)
    require(mm(barrier_matrices[0], barrier_matrices[1]) != mm(barrier_matrices[1], barrier_matrices[0]),
            'Barrier-only switching changes noncommuting kinetics, not just a common clock speed')
    law = np.asarray([float(x) for x in stationary])
    for q in barrier_matrices:
        law = law @ expm(.7*array(q))
    stationary_residual = float(np.max(np.abs(law-np.asarray([float(x) for x in stationary]))))
    require(stationary_residual < 2e-14, 'Equilibrium preparation remains constant under barrier-only switching')
    return {'hidden_states': 3, 'field_cases': cases, 'Arrhenius_rate_residuals': energy_residuals,
            'common_return_projection_residuals': lumped_residuals,
            'barrier_only_stationary_residual': float(f'{stationary_residual:.12g}'),
            'scope': 'Exact finite-graph Bell rates and two erasure mechanisms; no molecular geometry or instantaneous-rate approximation is derived.'}


def reversal_projection_checks():
    cycle = [[-F(1), F(3, 4), F(1, 4)], [F(1, 4), -F(1), F(3, 4)],
             [F(3, 4), F(1, 4), -F(1)]]
    mu, theta = [F(1, 3)]*3, [0, 2, 1]
    require(all(mu[i]*cycle[i][j] == mu[theta[j]]*cycle[theta[j]][theta[i]]
                for i in range(3) for j in range(3)), 'Biased cycle obeys generalized detailed balance')
    require(cycle[0][1] != cycle[1][0], 'The same cycle fails ordinary detailed balance')
    partition = [0, 1, 1]
    require(all(partition[i] == partition[theta[i]] for i in range(3)), 'The informative projection is reversal-even')
    require(cycle[1][0] != cycle[2][0], 'The informative even partition is not strongly lumpable')
    # Stationary entry into the hidden block comes from state zero.
    entry = [cycle[0][1]/(-cycle[0][0]), cycle[0][2]/(-cycle[0][0])]
    entry_hazard = entry[0]*cycle[1][0]+entry[1]*cycle[2][0]
    stationary_hazard = (mu[1]*cycle[1][0]+mu[2]*cycle[2][0])/(mu[1]+mu[2])
    require(entry_hazard == F(3, 8) and stationary_hazard == F(1, 2),
            'Entry-history and stationary conditional hazards differ, giving a stationary non-Markov certificate')
    ordinary_epr = sum(float(mu[i]*cycle[i][j])*math.log(float(cycle[i][j]/cycle[j][i]))
                       for i in range(3) for j in range(3) if i != j)
    require(abs(ordinary_epr-math.log(3)/2) < 1e-15, 'Cycle ordinary EPR uses the ordered-flux convention')
    two, nu = [[-F(1), F(1)], [F(2), -F(2)]], [F(2, 3), F(1, 3)]
    product = zeros(6)
    law = [mu[c]*nu[x] for c in range(3) for x in range(2)]
    involution = [2*theta[c]+x for c in range(3) for x in range(2)]
    projection = [[F(x == 0), F(x == 1)] for c in range(3) for x in range(2)]
    for c in range(3):
        for x in range(2):
            for d in range(3):
                product[2*c+x][2*d+x] += cycle[c][d]
            for y in range(2):
                product[2*c+x][2*c+y] += two[x][y]
    require(all(law[i]*product[i][j] == law[involution[j]]*product[involution[j]][involution[i]]
                for i in range(6) for j in range(6)), 'Six-state product has exact generalized equilibrium reversal')
    require(mm([law], product) == [[F(0)]*6] and all(sum(row) == 0 for row in product),
            'Six-state product has the exact stationary law and conservative generator')
    require(mm(product, projection) == mm(projection, two), 'Even two-state projection is exactly Markov by strong lumpability')
    require(all(nu[i]*two[i][j] == nu[j]*two[j][i] for i in range(2) for j in range(2)),
            'The even Markov projection obeys ordinary detailed balance')
    initial = np.array([1., 0., 0., 0., 0., 0.])
    closure_residuals = []
    for duration in (.1, .7, 2.):
        residual = float(np.max(np.abs(initial @ expm(duration*array(product)) @ array(projection)
                                       -np.array([1., 0.]) @ expm(duration*array(two)))))
        require(residual < 3e-15, 'Actual six-state propagator has the stated even Markov closure from a nonstationary start')
        closure_residuals.append(float(f'{residual:.12g}'))
    return {'non_Markov_even_fixture_states': 3, 'Markov_even_fixture_states': 6,
            'entry_conditioned_exit_hazard_exact': str(entry_hazard),
            'stationary_conditioned_exit_hazard_exact': str(stationary_hazard),
            'ordinary_cycle_EPR': float(f'{ordinary_epr:.12g}'), 'generalized_cycle_EPR': 0,
            'six_state_projection_propagator_residuals': closure_residuals,
            'scope': 'The exact fixtures illustrate both sides; stationary Markov projection implies ordinary reversibility by the separate analytic path-law theorem.'}


def row_defect(q, perturbed):
    differences = [[y-x for x, y in zip(row, other)] for row, other in zip(q, perturbed)]
    defects = []
    for i, row in enumerate(differences):
        half = sum(abs(x) for x in row)/2
        positive = sum(max(F(0), x) for j, x in enumerate(row) if j != i)
        negative = sum(max(F(0), -x) for j, x in enumerate(row) if j != i)
        require(sum(row) == 0 and half == max(positive, negative), 'Half full-row L1 defect equals the maximum positive/negative off-diagonal mass')
        defects.append(half)
    return max(defects), defects, differences


def robustness_checks():
    mu, hidden = [F(2, 3), F(1, 3)], [[-F(1), F(1)], [F(2), -F(2)]]
    reference, perturbations = [], []
    for scale, beta, bias in ((F(1, 2), [F(3, 4), F(1)], F(4)),
                              (F(3, 2), [F(1), F(1, 2)], F(1))):
        k = [[scale*x for x in row] for row in hidden]
        reference.append(physical(k, mu, beta, bias))
    for index, q in enumerate(reference):
        altered = [row[:] for row in q]
        if index == 0:
            altered[1][2] += F(1, 20)
            altered[1][1] -= F(1, 20)
        else:
            altered[2][2] += altered[2][0]-F(1, 8)
            altered[2][0] = F(0)
            altered[2][1] += F(1, 8)
        perturbations.append(altered)
    alpha = F(1, 2)
    eta = max(row_defect(q, altered)[0] for q, altered in zip(reference, perturbations))
    require(eta == F(1, 2), 'One-sided fixture has exact global generator defect one half')
    require(all(q[i][0] >= alpha for q in reference for i in (1, 2)), 'Only reference reset rate is required')
    require(perturbations[1][2][0] == 0, 'Perturbed fixture genuinely lacks a positive common reset to the hub')
    initial, perturbed_initial = np.array([1., 0., 0.]), np.array([.9, .1, 0.])
    d0 = F(1, 10)
    diagnostics = []
    for protocol in (((1, .1),), ((0, .2), (1, .4)), ((1, .3), (0, .2), (1, .4))):
        p, changed = initial.copy(), perturbed_initial.copy()
        ref_product, prefixes = np.eye(3), []
        for field, duration in protocol:
            prefixes.append(changed.copy())
            p = p @ expm(duration*array(reference[field]))
            changed = changed @ expm(duration*array(perturbations[field]))
            ref_product = ref_product @ expm(duration*array(reference[field]))
        horizon = sum(t for _, t in protocol)
        integral = np.zeros(3)
        for index, (field, duration) in enumerate(protocol):
            suffix = np.eye(3)
            for other_field, other_duration in protocol[index+1:]:
                suffix = suffix @ expm(other_duration*array(reference[other_field]))
            delta = array(perturbations[field])-array(reference[field])
            value, _ = quad_vec(lambda age: prefixes[index] @ expm(age*array(perturbations[field])) @ delta @
                               expm((duration-age)*array(reference[field])) @ suffix, 0., duration,
                               epsabs=1e-12, epsrel=1e-12)
            integral += value
        duhamel_residual = float(np.max(np.abs(changed-p-(perturbed_initial-initial) @ ref_product-integral)))
        require(duhamel_residual < 2e-13, 'One-sided Duhamel orientation reproduces the actual switched endpoint difference')
        tv = float(np.sum(np.abs(changed-p))/2)
        bound = math.exp(-float(alpha)*horizon)*float(d0)+float(eta/alpha)*(1-math.exp(-float(alpha)*horizon))
        require(tv <= bound+2e-14, 'Nonstationary, nonreversible, field-dependent perturbation obeys the one-sided bound')
        contraction = max(np.sum(np.abs(ref_product[i]-ref_product[j]))/2 for i in range(3) for j in range(3))
        require(contraction <= math.exp(-float(alpha)*horizon)+2e-14, 'Reference propagator has the predicted reset contraction')
        diagnostics.append({'horizon': horizon, 'endpoint_TV': float(f'{tv:.12g}'),
                            'one_sided_bound': float(f'{bound:.12g}'), 'Duhamel_residual': float(f'{duhamel_residual:.12g}')})
    # Both-reset and stationary-weighted refinements use a different fixture.
    q = physical(hidden, mu, [F(1), F(1)], F(1))
    altered = [row[:] for row in q]
    altered[2][1] += F(1, 10)
    altered[2][2] -= F(1, 10)
    defect, row_errors, _ = row_defect(q, altered)
    weighted = sum(mu[i]*row_errors[i+1] for i in range(2))
    require(defect == F(1, 10) and weighted == F(1, 30), 'Rare-row perturbation has a smaller exact stationary-weighted defect')
    refinements = []
    for horizon in (.1, 1., 4.):
        p, changed = initial @ expm(horizon*array(q)), initial @ expm(horizon*array(altered))
        tv = float(np.sum(np.abs(changed-p))/2)
        both_bound = float(defect/(1+defect))*(1-math.exp(-float(1+defect)*horizon))
        weighted_bound = float(weighted)*(1-math.exp(-horizon))
        require(tv <= min(both_bound, weighted_bound)+2e-14, 'Both-reset and weighted occupation refinements hold in the finite fixture')
        require(max(p[1:]/np.asarray([float(x) for x in mu])) <= 1-math.exp(-horizon)+2e-14,
                'Nonstationary reference hidden density obeys its reset occupation bound')
        refinements.append({'horizon': horizon, 'endpoint_TV': float(f'{tv:.12g}'),
                            'both_reset_bound': float(f'{both_bound:.12g}'),
                            'weighted_bound': float(f'{weighted_bound:.12g}')})
    # Omitting the diagonal halves this one-edge rate defect and fails even
    # at a small positive time. This guards the normalization in the theorem.
    small_q = [[-F(1), F(1)], [F(1), -F(1)]]
    small_changed = [[-F(5, 4), F(5, 4)], [F(1), -F(1)]]
    exact_eta, _, _ = row_defect(small_q, small_changed)
    t = .01
    difference = np.array([1., 0.]) @ (expm(t*array(small_changed))-expm(t*array(small_q)))
    actual = float(np.sum(np.abs(difference))/2)
    require(exact_eta == F(1, 4) and actual > float(exact_eta/2)*(1-math.exp(-t)),
            'Counterexample detects the invalid omission of the diagonal contribution')
    epsilon = F(1, 20)
    relative = [row[:] for row in q]
    for i in range(len(q)):
        for j in range(len(q)):
            if i != j:
                relative[i][j] = q[i][j]*(1+epsilon*(-1 if (i+j) % 2 else 1))
        relative[i][i] = -sum(relative[i][j] for j in range(len(q)) if j != i)
    relative_eta, _, _ = row_defect(q, relative)
    full_exit_cap = max(-q[i][i] for i in range(len(q)))
    require(relative_eta <= epsilon*full_exit_cap,
            'Relative rate errors have the exact epsilon-times-full-exit row-defect bound')
    zeta = -math.log1p(-float(epsilon))
    require(all(abs(math.log(float(relative[i][j]/q[i][j]))) <= zeta+1e-15
                for i in range(len(q)) for j in range(len(q)) if i != j and q[i][j]),
            'All perturbed rates obey the declared logarithmic tolerance')
    require(float(relative_eta) <= math.expm1(zeta)*float(full_exit_cap)+1e-15,
            'Logarithmic tolerance implies the stated full-row rate bound')
    ramp_cases = []
    alpha_float, spacing, width = .5, .5, .1
    ramp_bound = (1-math.exp(-alpha_float*width))/(alpha_float*(1-math.exp(-alpha_float*spacing)))
    for count in (1, 4, 12):
        endpoint = (count-1)*spacing+width
        integrated = sum(quad(lambda s: math.exp(-alpha_float*(endpoint-s)),
                              j*spacing, j*spacing+width, epsabs=1e-13)[0] for j in range(count))
        finite = ramp_bound*(1-math.exp(-alpha_float*spacing*count))
        require(abs(integrated-finite) < 2e-14 and finite <= ramp_bound,
                'Finite ramp defect integrals match the geometric fixed-clock bound')
        ramp_cases.append({'ramps': count, 'integrated_contraction_kernel': float(f'{integrated:.12g}')})
    rational_ramps = []
    # At alpha=log(4), spacing=1 and width=1/2 the exponential factors
    # are exactly 1/4 and 1/2; alpha times the limiting envelope is 2/3.
    for count in (1, 3, 8):
        scaled_integral = F(1, 2)*sum((F(1, 4)**j for j in range(count)), F(0))
        require(scaled_integral == F(2, 3)*(1-F(1, 4)**count) and scaled_integral < F(2, 3),
                'Exact rational geometric ramp certificate has the correct limiting envelope')
        rational_ramps.append({'ramps': count, 'alpha_times_integral_exact': str(scaled_integral)})
    return {'one_sided_reset_rate_exact': str(alpha), 'one_sided_row_defect_exact': str(eta),
            'initial_TV_exact': str(d0), 'one_sided_cases': diagnostics,
            'both_reset_and_weighted_cases': refinements, 'diagonal_omission_counterexample_TV': float(f'{actual:.12g}'),
            'relative_rate_certificate': {'epsilon_exact': str(epsilon), 'eta_exact': str(relative_eta),
                                          'epsilon_exit_bound_exact': str(epsilon*full_exit_cap),
                                          'logarithmic_tolerance': float(f'{zeta:.12g}')},
            'finite_ramp_cases': ramp_cases, 'uniform_ramp_kernel_bound': float(f'{ramp_bound:.12g}'),
            'rational_ramp_certificate': rational_ramps,
            'scope': 'Small finite-time diagnostics check exact defect conventions and theorem branches; they do not replace the uniform analytic proof.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/physical_robustness.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    snapshots = {}
    for name, expected in PROOFS.items():
        actual = hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        require(actual == expected, f'Frozen proof remains unchanged: {name}')
        snapshots[str(Path('docs')/name)] = actual
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                                           'scipy': scipy.__version__},
              'arithmetic': 'Exact fractions.Fraction identities with separately labeled float64 Arrhenius, matrix-exponential and quadrature diagnostics',
              'single_force_and_erasure': bell_and_erasure_checks(),
              'physical_reversal_and_Markov_projection': reversal_projection_checks(),
              'interface_robustness': robustness_checks(),
              'large_target_allocated': False,
              'limitations': ['Finite fixtures do not prove the uniform perturbation or stationary projection theorems.',
                              'Arrhenius identities specify mesoscopic rates and do not construct a microscopic molecular device.',
                              'The perturbed one-sided fixture lacks its own common reset; both-reset refinements are tested separately.',
                              'Endpoint robustness does not imply long-time path-law closeness or zero driven entropy production.',
                              'The parity fixtures do not certify a state-count advantage or physical odd-memory realization.',
                              'Fixed rate defects and ramp durations impose accuracy floors rather than all-accuracy robustness.',
                              'Float64 exponentials and quadrature are consistency diagnostics, not interval certificates.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'proof_snapshot_sha256': snapshots, 'imported_repository_verifiers': []}
    require(MAX_DENSE == 6, 'Measured dense fixture maximum is exactly six states')
    report['largest_dense_matrix_dimension'] = MAX_DENSE
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
