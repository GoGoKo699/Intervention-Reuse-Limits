#!/usr/bin/env python3
"""Bounded kinetic-interface and generalized-reversal certificates.

Exact rational identities and explicitly labeled small numerical residuals
supplement, rather than prove, the associated all-model theorems.
"""
import argparse
from fractions import Fraction as F
from itertools import product as words
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm


CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def array(a):
    return np.array([[float(x) for x in row] for row in a])


def observable_words(p, mu, label, length):
    active = {}
    for i, value in enumerate(label):
        row = active.setdefault((value,), [F(0)]*len(mu))
        row[i] += mu[i]
    for _ in range(1, length):
        nxt = {}
        for word, row in active.items():
            evolved = mm([row], p)[0]
            for j, mass in enumerate(evolved):
                key = word+(label[j],)
                target = nxt.setdefault(key, [F(0)]*len(mu))
                target[j] += mass
        active = nxt
    return {word: sum(row) for word, row in active.items() if sum(row)}


def entropy_rate(k, mu, theta):
    total = 0.
    for i in range(len(k)):
        for j in range(len(k)):
            if i != j and k[i][j]:
                numerator = mu[i]*k[i][j]
                denominator = mu[theta[j]]*k[theta[j]][theta[i]]
                if denominator == 0:
                    return 'infinity'
                total += float(numerator)*math.log(float(numerator/denominator))
    return total


def full_generator(hidden_k, mu, label, base):
    n = len(mu)
    q = zeros(n+1)
    for i in range(n):
        for j in range(n):
            q[i+1][j+1] = hidden_k[i][j]
        sign = 2*label[i]-1
        q[0][i+1] = mu[i]*base**(2+sign)
        q[i+1][0] = base**(sign-2)
        q[0][0] -= q[0][i+1]
        q[i+1][i+1] -= q[i+1][0]
    pi0 = [F(1, 2)]+[x/2 for x in mu]
    ratio = base**4
    pih = [1/(1+ratio)]+[ratio*x/(1+ratio) for x in mu]
    return q, pi0, pih


def generalized_reversal_checks():
    # Three-state reversible hidden target with two output colors. Its
    # unequal color-zero exits make the observed binary process non-Markov.
    target_mu = [F(1, 4), F(1, 4), F(1, 2)]
    target_k = [[F(-1), F(0), F(1)], [F(0), F(-4), F(4)],
                [F(1, 2), F(2), F(-5, 2)]]
    rate = F(8)
    target_p = [[F(int(i == j))+target_k[i][j]/rate for j in range(3)] for i in range(3)]
    target_labels = [0, 0, 1]
    require(all(sum(row) == 1 for row in target_p), 'Target uniformization is stochastic')
    require(all(target_mu[i]*target_p[i][j] == target_mu[j]*target_p[j][i]
                for i in range(3) for j in range(3)), 'Target uniformization is reversible exactly')
    prefixes = {length: observable_words(target_p, target_mu, target_labels, length) for length in range(1, 7)}
    states = sorted(prefixes[3])
    require(len(states) == 8, 'All eight binary three-letter states are allowed')
    index = {word: i for i, word in enumerate(states)}
    mu = [prefixes[3][word] for word in states]
    p = zeros(len(states))
    for i, word in enumerate(states):
        for symbol in (0, 1):
            extended = word+(symbol,)
            p[i][index[extended[1:]]] = prefixes[4].get(extended, F(0))/mu[i]
    theta = [index[tuple(reversed(word))] for word in states]
    middle = [word[1] for word in states]
    endpoint = [word[-1] for word in states]
    require(all(sum(row) == 1 for row in p), 'The finite-word predictor is stochastic')
    require(all(sum(mu[i]*p[i][j] for i in range(8)) == mu[j] for j in range(8)),
            'Finite-word stationary weights have the correct incoming flux')
    require(all(theta[theta[i]] == i and mu[theta[i]] == mu[i] and middle[theta[i]] == middle[i]
                for i in range(8)), 'Word reversal is an invariant-law involution preserving the middle actuator')
    require(any(endpoint[theta[i]] != endpoint[i] for i in range(8)),
            'Endpoint labeling would not preserve the actuator under the same involution')
    require(all(mu[i]*p[i][j] == mu[theta[j]]*p[theta[j]][theta[i]]
                for i in range(8) for j in range(8)), 'Every finite-word transition obeys generalized detailed balance')
    require(any(mu[i]*p[i][j] != mu[j]*p[j][i] for i in range(8) for j in range(8)),
            'The generalized reversible word chain is not ordinarily reversible')
    prefix_checks = []
    for length in range(1, 7):
        mid = observable_words(p, mu, middle, length)
        end = observable_words(p, mu, endpoint, length)
        require(mid == end, 'Middle and endpoint labels have exactly the same stationary finite output law')
        require(all(mid[word] == mid[tuple(reversed(word))] for word in mid),
                'Middle-labeled output law is time-reversal invariant')
        if length <= 4:
            require(mid == prefixes[length], 'Target prefix matching survives the change to the middle symbol')
        tv = sum(abs(mid.get(word, F(0))-prefixes[length].get(word, F(0)))
                 for word in set(mid)|set(prefixes[length]))/2
        prefix_checks.append({'length': length, 'target_prefix_TV_exact': str(tv)})
    require(F(prefix_checks[-1]['target_prefix_TV_exact']) > 0,
            'The fixture is a genuinely finite-history approximation, not an accidentally exact Markov output')
    hidden_k = [[rate*(p[i][j]-F(int(i == j))) for j in range(8)] for i in range(8)]
    require(entropy_rate(hidden_k, mu, theta) == 0., 'Generalized stationary hidden entropy production vanishes')
    ordinary_epr = entropy_rate(hidden_k, mu, list(range(8)))
    require(ordinary_epr == 'infinity', 'Directed finite-window shifts have infinite ordinary EPR in this fixture')
    reverse_k = [[mu[j]*hidden_k[j][i]/mu[i] for j in range(8)] for i in range(8)]
    epsilon = F(1, 10)
    regularized = [[(1-epsilon)*hidden_k[i][j]+epsilon*reverse_k[i][j] for j in range(8)] for i in range(8)]
    require(all(regularized[i][i] == hidden_k[i][i] for i in range(8)),
            'Adding a small ordinary reverse component preserves every exit')
    require(all(mu[i]*regularized[i][j] == mu[theta[j]]*regularized[theta[j]][theta[i]]
                for i in range(8) for j in range(8)), 'Bidirectional regularization preserves generalized detailed balance')
    finite_ordinary = entropy_rate(regularized, mu, list(range(8)))
    require(isinstance(finite_ordinary, float) and finite_ordinary > 0
            and entropy_rate(regularized, mu, theta) == 0.,
            'Positive finite ordinary EPR coexists with zero generalized EPR')
    full_theta = [0]+[i+1 for i in theta]
    full_cases = []
    qs_mid, qs_end = {}, {}
    for base in (F(1), F(3, 2), F(2, 3)):
        qmid, pi0, pih = full_generator(hidden_k, mu, middle, base)
        qend, _, _ = full_generator(hidden_k, mu, endpoint, base)
        qs_mid[base], qs_end[base] = qmid, qend
        require(all(sum(row) == 0 for row in qmid), 'Original-rule middle-labeled full generator is conservative')
        require(all(sum(pih[i]*qmid[i][j] for i in range(9)) == 0 for j in range(9)),
                'Original-rule full generator has the stated stationary field law')
        require(all(pih[i]*qmid[i][j] == pih[full_theta[j]]*qmid[full_theta[j]][full_theta[i]]
                    for i in range(9) for j in range(9)),
                'Original external rates preserve generalized detailed balance at every tested field')
        if base != 1:
            require(any(pih[i]*qend[i][j] != pih[full_theta[j]]*qend[full_theta[j]][full_theta[i]]
                        for i in range(9) for j in range(9)),
                    'Endpoint labeling fails this specified word-reversal identity')
        full_cases.append({'field_base_exact': str(base), 'generalized_full_EPR': entropy_rate(qmid, pih, full_theta)})
    readout = [[F(-1)]]+[[F(1)] for _ in range(8)]
    generator_words = 0
    bases = (F(3, 2), F(2, 3))
    for length in range(1, 5):
        for word in words(bases, repeat=length):
            left, right = [pi0], [pi0]
            for base in word:
                left, right = mm(left, qs_mid[base]), mm(right, qs_end[base])
            require(mm(left, readout) == mm(right, readout),
                    'Exact original-rule generator-word mean agrees between middle and endpoint realizations')
            generator_words += 1
    protocols = [[(F(3, 2), .2)], [(F(3, 2), .3), (F(2, 3), .7)],
                 [(F(2, 3), .2), (F(3, 2), .4), (F(1), .5)]]
    protocol_residuals = []
    for protocol in protocols:
        mid = np.array([float(x) for x in pi0])
        end = mid.copy()
        for base, duration in protocol:
            mid = mid @ expm(duration*array(qs_mid[base]))
            end = end @ expm(duration*array(qs_end[base]))
        residual = 2*abs(float(mid[0]-end[0]))
        require(residual < 2e-13, 'Finite switched means agree in independent numerical exponential calculations')
        protocol_residuals.append(float(f'{residual:.12g}'))
    report = {'target_hidden_states': 3,
              'predictor_hidden_states': 8, 'total_predictor_states': 9,
              'word_length': 3, 'word_stationary_weights_exact': {str(word): str(mu[index[word]]) for word in states},
              'prefix_comparisons': prefix_checks, 'ordinary_hidden_EPR': ordinary_epr,
              'generalized_hidden_EPR': 0, 'regularization_epsilon_exact': str(epsilon),
              'regularized_ordinary_hidden_EPR': float(f'{finite_ordinary:.12g}'),
              'regularized_generalized_hidden_EPR': 0, 'full_field_cases': full_cases,
              'exact_generator_word_cases': generator_words,
              'numerical_controlled_mean_residuals': protocol_residuals,
              'limitations': ['This small fixture validates identities and scope; it is not a state-count advantage example.',
                              'Finite checks do not prove the all-word stationary index-shift identity or all-protocol response equivalence.',
                              'Generalized stationary EPR is different from the ordinary reversal used by the existing state/EPR lower bounds.',
                              'No thermodynamic device realization or zero total entropy production under time-dependent driving is asserted.']}
    return report


def adjoint(a, mu):
    return [[mu[j]*a[j][i]/mu[i] for j in range(len(mu))] for i in range(len(mu))]


def kinetic_generator(k, mu, beta, equilibrium_ratio):
    """q_Ai=mu_i*r*beta_i, q_iA=beta_i, where r=e^(2h)."""
    n = len(mu)
    q = zeros(n+1)
    for i in range(n):
        for j in range(n):
            q[i+1][j+1] = k[i][j]
        q[0][i+1] = mu[i]*equilibrium_ratio*beta[i]
        q[i+1][0] = beta[i]
        q[0][0] -= q[0][i+1]
        q[i+1][i+1] -= beta[i]
    pi = [1/(1+equilibrium_ratio)]+[equilibrium_ratio*x/(1+equilibrium_ratio) for x in mu]
    return q, pi


def soft_lagrange_checks():
    grid = [F(1, 5), F(2, 5), F(3, 5), F(4, 5), F(1)]
    target_mu = [F(1, 5)]*5
    target_k = [[F(1, 16) if i != j else F(-1, 4) for j in range(5)] for i in range(5)]
    rival_mu = [F(1, 6), F(1, 3), F(1, 2)]
    rival_k = [[F(1, 12)/rival_mu[i] if i != j else -F(1, 6)/rival_mu[i]
                for j in range(3)] for i in range(3)]
    rival_beta = [F(1, 3), F(2, 3), F(5, 6)]

    def lagrange(index, value):
        out = F(1)
        for j, node in enumerate(grid):
            if index != j:
                out *= (value-node)/(grid[index]-node)
        return out

    cases = []
    for name, k, mu, beta in (('target', target_k, target_mu, grid),
                              ('off_grid_rival', rival_k, rival_mu, rival_beta)):
        n = len(mu)
        q0, pi0 = kinetic_generator(k, mu, [F(1)]*n, F(1))
        qh, pih = kinetic_generator(k, mu, beta, F(4))
        require(all(sum(row) == 0 for row in q0) and all(sum(row) == 0 for row in qh),
                'Generic kinetic full generators conserve probability')
        require(adjoint(q0, pi0) == q0 and adjoint(qh, pih) == qh,
                'Arbitrary positive barriers preserve the exact two-field equilibrium bias and detailed balance')
        require(pih[0] == F(1, 5) and pih[1:] == [F(4, 5)*x for x in mu],
                'The nonzero field stationary law depends on the bias, not on the barrier values')
        hidden = [[F(int(i == j and i != 0)) for j in range(n+1)] for i in range(n+1)]
        difference = [[q0[i][j]-qh[i][j] for j in range(n+1)] for i in range(n+1)]
        recovered_beta = mm(mm(hidden, difference), hidden)
        recovered_k = mm(mm(hidden, q0), hidden)
        for i in range(n+1):
            for j in range(n+1):
                recovered_beta[i][j] += hidden[i][j]
                recovered_k[i][j] += hidden[i][j]
        require(recovered_beta == [[beta[i-1] if i == j and i else F(0) for j in range(n+1)] for i in range(n+1)],
                'Two physical generators recover the actual rival barrier multiplier exactly')
        require([row[1:] for row in recovered_k[1:]] == k and all(x == 0 for x in recovered_k[0]),
                'The zero-field physical generator recovers the hidden generator without a hidden inverse')
        readout = [[F(-1)]]+[[F(1)] for _ in range(n)]
        require(mm(q0, readout) == [[-2*x[0]] for x in readout],
                'The zero-field visible readout has the exact rate-one telegraph generator action')
        p = [[F(int(i == j))+k[i][j]/3 for j in range(n)] for i in range(n)]
        require(all(sum(row) == 1 for row in p) and min(x for row in p for x in row) >= 0,
                'A common exit cap makes uniformization entrywise nonnegative and stochastic')
        selectors = []
        for index in range(len(grid)):
            values = [lagrange(index, value)**2 for value in beta]
            selector = [[values[i] if i == j else F(0) for j in range(n)] for i in range(n)]
            require(all(value >= 0 for value in values), 'Squared Lagrange soft selector is nonnegative at every actual rival barrier')
            require(adjoint(selector, mu) == selector, 'Soft selector is stationary selfadjoint')
            if name == 'target':
                require(values == [F(int(i == index)) for i in range(n)],
                        'Squared Lagrange selector is the exact target projector on the finite barrier grid')
            selectors.append(selector)
        if name == 'off_grid_rival':
            require(any(mm(a, a) != a for a in selectors),
                    'Off-grid rival selectors are positive soft weights, not coordinate projectors')
        forward = [[48*x for x in row] for row in mm(mm(selectors[0], p), selectors[1])]
        backward = [[48*x for x in row] for row in mm(mm(selectors[1], p), selectors[0])]
        require(min(x for row in forward for x in row) >= 0 and backward == adjoint(forward, mu),
                'Uniformized soft-port transport is positive and reverses to its stationary adjoint')
        if name == 'target':
            require(forward[0][1] == 1 and sum(sum(row) for row in forward) == 1,
                    'The rational target transport is exactly the one-state matching map')
        cases.append({'fixture': name, 'hidden_states': n, 'full_states': n+1,
                      'stationary_hidden_law_exact': list(map(str, mu)), 'barriers_exact': list(map(str, beta)),
                      'hidden_exit_cap_exact': str(max(-k[i][i] for i in range(n))),
                      'selector_diagonals_exact': [[str(a[i][i]) for i in range(n)] for a in selectors]})
    return {'target_barrier_grid_exact': list(map(str, grid)), 'field_equilibrium_ratio_exact': '4',
            'cases': cases,
            'scope': 'Exact finite two-field barrier algebra and bounded-rate positive selectors; no unlimited-rate soft-Lagrange or all-model separation is asserted by these fixtures.'}


def generic_reset_checks():
    # These menu bounds include beta_0=1 and the rational target grid above.
    # They are fixture constants, not universal values of an interface.
    birth_upper, return_lower = F(4), F(1, 5)
    alpha = return_lower  # external k=1
    uniform_age = birth_upper/return_lower**2
    require(birth_upper >= 1 and return_lower <= 1 and birth_upper/return_lower >= 1,
            'Zero-field normalization makes the sharp initial-age cancellation admissible')
    mu = [F(1, 6), F(1, 3), F(1, 2)]
    k = zeros(3)
    for i in range(3):
        k[i][(i+1) % 3] = F(1, 4)/mu[i]
        k[i][(i-1) % 3] = F(1, 12)/mu[i]
        k[i][i] = -sum(k[i])
    require(all(sum(mu[i]*k[i][j] for i in range(3)) == 0 for j in range(3)),
            'Generic reset fixture allows stationary irreversible hidden dynamics')
    reset = zeros(4)
    for i in range(1, 4):
        reset[i][0], reset[i][i] = alpha, -alpha
    density_cases = []
    for ratio, beta in ((F(1), [F(1)]*3), (F(4), [F(1, 3), F(2, 3), F(5, 6)])):
        q, _ = kinetic_generator(k, mu, beta, ratio)
        require(min(beta) >= return_lower and max(ratio*x for x in beta) <= birth_upper,
                'Rational physical rates fit the generic return and birth envelope')
        residual = [[q[i][j]-reset[i][j] for j in range(4)] for i in range(4)]
        require(all(sum(row) == 0 for row in residual)
                and all(residual[i][j] >= 0 for i in range(4) for j in range(4) if i != j),
                'The common generic reset leaves nonnegative residual jump rates')
        for duration in (.1, .7, 3.):
            initial = np.array([.5]+[float(x)/2 for x in mu])
            law = initial @ expm(duration*array(residual))
            max_density = max(law[1:]/np.array([float(x) for x in mu]))
            density_bound = .5+float(birth_upper)*duration
            require(max_density <= density_bound+2e-13,
                    'Nonexponential barriers obey the same residual hidden-density bound')
            density_cases.append({'equilibrium_ratio_exact': str(ratio), 'duration': duration,
                                  'maximum_hidden_density': float(f'{max_density:.12g}'),
                                  'density_upper_bound': float(f'{density_bound:.12g}')})
    age_cases = []
    for horizon in (.2, 1., 8.):
        a, source = float(alpha), float(birth_upper)
        integral, _ = quad(lambda age: a*math.exp(-a*age)*source*age*age/2,
                           0., horizon, epsabs=1e-13, epsrel=1e-13)
        direct = integral+math.exp(-a*horizon)*(horizon/2+source*horizon*horizon/2)
        x = a*horizon
        closed = float(uniform_age)*(1-(1+x)*math.exp(-x))+horizon*math.exp(-x)/2
        deficit = math.exp(-x)/a*(source/a+(source/a-.5)*x)
        require(abs(direct-closed) < 2e-12 and abs(float(uniform_age)-closed-deficit) < 2e-12,
                'Generic reset-age quadrature agrees with both exact closed formulas')
        require(deficit >= 0 and closed <= float(uniform_age),
                'Generic barrier constants give a horizon-independent endpoint-KL multiplier')
        age_cases.append({'horizon': horizon, 'age_factor': float(f'{closed:.12g}'),
                          'uniform_age_factor': str(uniform_age)})
    general_initial_cases = []
    for initial_density, a_ratio in ((F(0), F(1)), (F(1, 2), F(1)),
                                     (F(2), F(1, 4)), (F(3), F(1))):
        if initial_density <= a_ratio:
            psi = float(a_ratio)
            maximizer = None
            require(initial_density >= 0 and a_ratio-initial_density >= 0,
                    'Low-density branch has an everywhere nonnegative derivative coefficient')
        else:
            critical = initial_density/(initial_density-a_ratio)
            require(initial_density-(initial_density-a_ratio)*critical == 0,
                    'High-density branch has the exact finite maximizing age')
            maximizer = float(critical)
            psi = float(a_ratio)+float(initial_density-a_ratio)*math.exp(-maximizer)
            at_max = float(a_ratio)+(float(initial_density-a_ratio)*maximizer-float(a_ratio))*math.exp(-maximizer)
            require(abs(at_max-psi) < 2e-15, 'The finite maximum equals the closed Psi expression')
        for x in (0., .2, 1., 2., 5., 20.):
            value = float(a_ratio)+(float(initial_density-a_ratio)*x-float(a_ratio))*math.exp(-x)
            require(-2e-15 <= value <= psi+2e-15,
                    'Finite general-initialization age factors lie below the correct branch of Psi')
        general_initial_cases.append({'initial_density_bound_exact': str(initial_density),
                                      'beta_over_alpha_exact': str(a_ratio), 'maximizing_scaled_age': maximizer,
                                      'Psi': float(f'{psi:.12g}')})
    return {'birth_upper_exact': str(birth_upper), 'return_lower_exact': str(return_lower),
            'reset_rate_exact': str(alpha), 'endpoint_KL_multiplier_exact': str(uniform_age),
            'density_cases': density_cases, 'age_cases': age_cases,
            'general_initialization_Psi_cases': general_initial_cases,
            'scope': 'Exact rate-envelope checks and finite numerical density/age diagnostics; proof constants for a general kinetic interface remain symbolic.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/kinetic_parity.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                                           'scipy': scipy.__version__},
              'arithmetic': 'Exact fractions.Fraction and finite symbol enumeration, with separately labeled float64 matrix-exponential/quadrature residuals',
              'generalized_word_reversal': generalized_reversal_checks(),
              'generic_barrier_soft_Lagrange': soft_lagrange_checks(),
              'generic_interface_reset_constants': generic_reset_checks(),
              'largest_dense_matrix_dimension': 9,
              'large_target_allocated': False,
              'limitations': ['Finite fixtures do not prove uniform prediction or all-model state-complexity theorems.',
                              'The parity fixture is not a small state-count advantage; it checks the generalized-reversal construction and its exact physical interface.',
                              'Generalized stationary entropy production depends on the specified physical reversal and is not ordinary identity-reversal entropy production.',
                              'No thermodynamic implementation or zero entropy under arbitrary time-dependent driving is asserted.'],
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'imported_repository_verifiers': []}
    proof_names = ['GENERAL_KINETIC_INTERFACE.md', 'GENERAL_INTERFACE_ENTROPY_BOUND.md',
                   'CAPPED_KINETIC_INTERFACE_SEPARATION.md', 'GENERALIZED_REVERSAL_PREDICTION.md',
                   'KINETIC_PARITY_RESOURCE_TRADEOFF.md']
    report['proof_snapshot_sha256'] = {
        str(Path('docs')/name): hashlib.sha256((root/'docs'/name).read_bytes()).hexdigest()
        for name in proof_names}
    report['checks'] = CHECKS
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
