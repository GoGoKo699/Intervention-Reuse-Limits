#!/usr/bin/env python3
"""Exact finite checks of reversible sampling with bounded conductance density.

Enumerated stratified samples verify the self-row conditioning identity;
small rational graphs verify positive realization and prefix recursion. Exact
logarithm enclosures check the concentration and regenerative error budgets.
No trajectories or random samples are simulated. The all-size existence and
all-protocol guarantees remain statements of the accompanying proof.
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
import verify_reversible_compression as reused


require = reused.require
Q = sp.Rational


def target() -> dict:
    mu = sp.Matrix([[Q(1, 6), Q(1, 3), Q(1, 4), Q(1, 4)]])
    labels = [-1, -1, 1, 1]
    density = sp.Matrix([[0, Q(1, 2), 1, Q(3, 2)],
                         [Q(1, 2), 0, Q(3, 2), Q(1, 4)],
                         [1, Q(3, 2), 0, 2],
                         [Q(3, 2), Q(1, 4), 2, 0]])
    L = sp.Integer(2)
    K = density*sp.diag(*mu)
    for i in range(K.rows):
        K[i, i] = -sum(K[i, j] for j in range(K.cols) if j != i)
    P = sp.eye(K.rows)+K/L
    require(all(0 <= value <= L for value in density), 'Bounded density')
    require(density == density.T, 'Symmetric conductance density')
    require(mu*K == sp.zeros(1, 4), 'Exact target stationarity')
    require(sp.diag(*mu)*K == K.T*sp.diag(*mu), 'Target detailed balance')
    witness = [sum(P[i, j] for j in (2, 3)) for i in (0, 1)]
    require(witness[0] != witness[1], 'Binary target is not actuator-lumpable')
    return {'mu': mu, 'labels': labels, 'q': density, 'L': L, 'K': K, 'P': P,
            'nonlumpability_witness': witness}


def sample_graph(model: dict, samples: tuple[int, ...], eta: sp.Expr) -> dict:
    n = len(samples)//2
    require(all(model['labels'][x] == (-1 if i < n else 1)
                for i, x in enumerate(samples)), 'Stratified sample positions')
    omega = sp.ones(1, 2*n)/(2*n)
    gamma = [model['labels'][x] for x in samples]
    Kbar = sp.zeros(2*n)
    for i, x in enumerate(samples):
        for j, y in enumerate(samples):
            if i != j:
                Kbar[i, j] = omega[j]*model['q'][x, y]
        Kbar[i, i] = -sum(Kbar[i, j] for j in range(2*n) if j != i)
    Pbar = sp.eye(2*n)+Kbar/model['L']
    Pstar = (1-eta)*Pbar+eta*sp.ones(2*n, 1)*omega
    return {'Pbar': Pbar, 'Pstar': Pstar, 'omega': omega, 'gamma': gamma,
            'samples': samples, 'Kstar': model['L']*(Pstar-sp.eye(2*n))}


def function_family(model: dict, ell: int) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    U, V = [], []
    for length in range(ell+1):
        for word in itertools.product((-1, 1), repeat=length):
            prediction = reused.future_prediction(model['P'], model['labels'], word)
            for symbol in (-1, 1):
                value = sp.diag(*[int(g == symbol) for g in model['labels']])*prediction
                V.append(value)
                if length < ell:
                    U.append(value)
    return U, V


def enumerate_conditioning(model: dict) -> dict:
    """All 16 size-two stratified samples, with their exact nonuniform weights."""
    n, omega = 2, sp.ones(1, 4)/4
    strata, conditional = ((0, 1), (2, 3)), {0: Q(1, 3), 1: Q(2, 3),
                                            2: Q(1, 2), 3: Q(1, 2)}
    U, V = function_family(model, 2)
    configurations = []
    for xs in itertools.product(strata[0], strata[0], strata[1], strata[1]):
        weight = sp.prod(conditional[x] for x in xs)
        configurations.append((xs, weight, sample_graph(model, xs, Q(1, 16))))
    require(sum(weight for _, weight, _ in configurations) == 1,
            'Enumerated sample law is normalized')
    checks, max_bias = 0, sp.Integer(0)
    for i in range(4):
        stratum = strata[i//n]
        for x in stratum:
            for u in U:
                F = sp.Matrix([model['q'][x, y]*(u[y]-u[x])/model['L']
                               for y in range(4)])
                require(F[x] == 0 and all(-1 <= value <= 1 for value in F),
                        'Diagonal kernel convention and Hoeffding range')
                expectation = sp.Integer(0)
                centered_second_moment = sp.Integer(0)
                stratum_mean = sum(conditional[y]*F[y] for y in stratum)
                bias = -omega[i]*stratum_mean
                for xs, probability, graph in configurations:
                    if xs[i] != x:
                        continue
                    ux = sp.Matrix([u[y] for y in xs])
                    row_error = (graph['Pbar']*ux)[i]-(model['P']*u)[x]
                    empirical_identity = sum(omega[j]*F[xs[j]] for j in range(4))
                    empirical_identity -= (model['mu']*F)[0]
                    require(row_error == empirical_identity,
                            'Exact sampled-row identity, including repeated samples')
                    conditional_probability = probability/conditional[x]
                    expectation += conditional_probability*row_error
                    centered_second_moment += conditional_probability*(row_error-bias)**2
                require(expectation == bias, 'Only the conditioned self-row causes bias')
                require(abs(bias) <= omega[i] <= Q(1, n), 'Exact conditional bias bound')
                variance = sp.Integer(0)
                for j in range(4):
                    if j == i:
                        continue
                    options = strata[j//n]
                    mean = sum(conditional[y]*F[y] for y in options)
                    variance += omega[j]**2*sum(conditional[y]*(F[y]-mean)**2
                                                for y in options)
                require(centered_second_moment == variance,
                        'Conditional independence gives the exact sum of variances')
                require(variance <= sum(omega[j]**2 for j in range(4) if j != i)
                        <= Q(1, n), 'Weighted-Hoeffding variance proxy')
                max_bias = max(max_bias, abs(bias))
                checks += 1
    for v in V:
        empirical_expectation = sum(probability*sum(omega[i]*v[xs[i]] for i in range(4))
                                    for xs, probability, _ in configurations)
        require(empirical_expectation == (model['mu']*v)[0],
                'Stratified empirical averages are unbiased')
    require(max_bias > 0, 'A nonzero self-row bias is actually exercised')
    return {'enumerated_configurations': len(configurations),
            'conditional_row_function_checks': checks,
            'empirical_average_checks': len(V),
            'largest_absolute_conditional_bias_exact': str(max_bias),
            'sample_law': 'Complete finite enumeration, not Monte Carlo.'}


def realizations_and_prefixes(model: dict) -> dict:
    eta, ell = Q(1, 16), 3
    U, V = function_family(model, ell)
    records = []
    for samples in ((0, 1, 2, 3), (0, 0, 2, 2)):
        graph = sample_graph(model, samples, eta)
        Pbar, Pstar, omega, gamma, Kstar = (graph[key] for key in
                                         ('Pbar', 'Pstar', 'omega', 'gamma', 'Kstar'))
        require(Pstar*sp.ones(4, 1) == sp.ones(4, 1), 'Stochastic sampled update')
        require(omega*Pstar == omega, 'Exact sampled stationarity')
        require(sp.diag(*omega)*Pstar == Pstar.T*sp.diag(*omega),
                'Ordinary sampled reversibility')
        require(all(value > 0 for value in Pstar), 'Positive reset ensures irreducibility')
        require(all(-Kstar[i, i] <= model['L'] for i in range(4)), 'Outgoing-rate cap')
        for size in range(1, 5):
            for indices in itertools.combinations(range(4), size):
                cap_form = 2*model['L']*sp.diag(*omega)+sp.diag(*omega)*Kstar
                require(cap_form.extract(indices, indices).det() >= 0,
                        'Exact principal-minor certificate for relaxation cap 2L')
        require(bounded.histogram(omega, gamma)
                == bounded.histogram(model['mu'], model['labels']), 'Exact full histogram')
        for order in range(1, 7):
            require(reused.scalar_moment(omega, sp.Matrix(gamma), order)
                    == reused.scalar_moment(model['mu'], sp.Matrix(model['labels']), order),
                    'Exact actuator moments, including mean zero and W=1')
        bounded.physical_identities(Pstar, omega, gamma, model['L'], True)
        for u in U:
            ux = sp.Matrix([u[x] for x in samples])
            require(max(abs(v) for v in (Pstar-Pbar)*ux) <= eta,
                    'Reset changes every tested [0,1] function by at most eta')
        records.append({'microscopic_samples': list(samples),
                        'distinct_microscopic_states': len(set(samples)),
                        'physical_replica_states': 4,
                        'minimum_update_entry_exact': str(min(Pstar)),
                        'largest_outgoing_rate_exact': str(max(-Kstar[i, i] for i in range(4)))})
    graph = sample_graph(model, (0, 1, 2, 3), eta)
    Pstar, omega, gamma = graph['Pstar'], graph['omega'], graph['gamma']
    row_defect = max(abs(value) for u in U for value in (graph['Pbar']-model['P'])*u)
    average_defect = max(abs((omega*v)[0]-(model['mu']*v)[0]) for v in V)
    require(row_defect <= eta and average_defect <= eta, 'Concrete simultaneous good event')
    words_checked, tv_records = 0, []
    for length in range(1, ell+2):
        variation = sp.Integer(0)
        for word in itertools.product((-1, 1), repeat=length):
            original = reused.word_probability(model['P'], model['mu'], model['labels'], word)
            sampled = reused.word_probability(Pstar, omega, gamma, word)
            require(abs(original-sampled) <= (2*(length-1)+1)*eta,
                    'Word error from one-step recursion plus empirical average')
            if length <= ell:
                f = reused.future_prediction(model['P'], model['labels'], word)
                fs = reused.future_prediction(Pstar, gamma, word)
                require(max(abs(value) for value in fs-f) <= 2*length*eta,
                        'Exact future-prediction induction bound')
            variation += abs(original-sampled)/2
            words_checked += 1
        theta = Q(1, 2)*2**length*(2*(length-1)+1)*eta
        require(variation <= theta, 'Stationary prefix total-variation certificate')
        for tilt in (Q(2, 3), Q(3, 2)):
            normalizer = sum(model['mu'][i]*tilt**model['labels'][i] for i in range(4))
            require(normalizer == sum(omega[i]*tilt**gamma[i] for i in range(4)),
                    'Exact entry-tilt normalization')
            tilted_variation = sum(abs(reused.word_probability(model['P'], model['mu'],
                                                               model['labels'], word)
                                       -reused.word_probability(Pstar, omega, gamma, word))
                                   *tilt**word[0]/(2*normalizer)
                                   for word in itertools.product((-1, 1), repeat=length))
            require(tilted_variation <= max(tilt**2, tilt**-2)*variation,
                    'First-symbol tilt amplifies TV by at most exp(2GH)')
        tv_records.append({'prefix_length': length, 'actual_TV_exact': str(variation),
                           'certificate_exact': str(theta)})
    return {'sampled_graphs': records, 'reset_precision_exact': str(eta),
            'good_sample_one_step_defect_exact': str(row_defect),
            'good_sample_average_defect_exact': str(average_defect),
            'word_probabilities_checked': words_checked, 'prefix_TV': tv_records}


def log_bounds(value: Fraction, terms: int = 100) -> tuple[Fraction, Fraction]:
    """Rational enclosures using log x = 2 atanh((x-1)/(x+1))."""
    require(value >= 1, 'Log enclosure domain')
    power = 0
    while value >= 2:
        value /= 2
        power += 1

    def near_one(x):
        z = (x-1)/(x+1)
        lower = 2*sum((z**(2*j+1)/Fraction(2*j+1) for j in range(terms)), Fraction(0))
        tail = 2*z**(2*terms+1)/(Fraction(2*terms+1)*(1-z*z))
        return lower, lower+tail

    lo, hi = near_one(value)
    lo2, hi2 = near_one(Fraction(2))
    return lo+power*lo2, hi+power*hi2


def ceiling(x: Fraction) -> int:
    return -(-x.numerator//x.denominator)


def concentration_budget(m: int, ell: int, eta: Fraction) -> dict:
    count = sum(m**r for r in range(1, ell+2))
    lo, hi = log_bounds(Fraction(16*m*count)/eta)
    factor = 256/eta**2
    nlo, nhi = ceiling(factor*lo), ceiling(factor*hi)
    require(nlo == nhi, 'Exact theorem ceiling resolved by rational logarithm enclosure')
    n = nlo
    require(n >= 2/eta, 'Self-row bias is at most eta/2')
    first_exponent = (n*eta**2/8).__floor__()
    second_exponent = (2*n*eta**2).__floor__()
    # e > 2 implies e^{-x} <= 2^{-floor(x)} for x >= 0.
    bound = Fraction(2*m*n*count, 2**first_exponent)
    bound += Fraction(2*count, 2**second_exponent)
    require(bound < 1, 'Simultaneous weighted-Hoeffding failure probability is below one')
    require(bound < Fraction(1, 2**100), 'Quantitative margin, using only rational arithmetic')
    return {'alphabet_size': m, 'prefix_updates': ell, 'eta_exact': str(eta),
            'functions_bound': count, 'samples_per_stratum': n,
            'total_physical_states': 1+m*n,
            'union_failure_bound': '< 2^-100',
            'logarithm_enclosure_terms': 100}


def budgets() -> dict:
    concentration = [concentration_budget(m, ell, eta)
                     for m in (2, 3) for ell in (1, 3)
                     for eta in (Fraction(1, 2), Fraction(1, 8), Fraction(1, 128))]
    # G=1, H=log(3/2)/2 gives R=A_H=3/2; L=2 gives q=3/4.
    R, A, L = Fraction(3, 2), Fraction(3, 2), Fraction(2)
    C, q = 1+2*R**2, L*R/(1+L*R)
    regenerative = []
    for delta in (Fraction(1, 4), Fraction(1, 32), Fraction(1, 512)):
        ell = 1
        while C*q**(ell+1) > delta/2:
            ell += 1
        require(ell == 1 or C*q**ell > delta/2, 'Exact minimal cutoff and ceil convention')
        eta = delta/(C*A*2**(ell+1)*(2*ell+1))
        theta = Fraction(1, 2)*2**(ell+1)*(2*ell+1)*eta
        prefix_error, clock_error = C*A*theta, C*q**(ell+1)
        require(prefix_error == delta/2 and clock_error <= delta/2,
                'Exact regenerative error allocation')
        require(prefix_error+clock_error <= delta, 'All-horizon certificate budget')
        item = concentration_budget(2, ell, eta)
        item.update({'requested_error_exact': str(delta),
                     'prefix_error_exact': str(prefix_error),
                     'clock_error_exact': str(clock_error)})
        regenerative.append(item)
    return {'concentration_cases': concentration, 'regenerative_cases': regenerative,
            'fixed_parameters_exact': {'L': str(L), 'R': str(R), 'A_H': str(A),
                                       'C_R': str(C), 'q': str(q)},
            'method': 'Exact rational logarithm enclosures and integer inequalities; no floating-point ceilings.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/bounded_density_sampling.json'))
    args = parser.parse_args()
    model = target()
    sources = [Path(__file__).resolve(), Path(bounded.__file__).resolve(),
               Path(reused.__file__).resolve()]
    report = {
        'status': 'PASS',
        'scope': 'Exact sampled-row conditioning, reversible graph realization, finite prefix recursion, and concentration/regenerative budgets under an additional bounded conductance density; no simulations.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
        'target': {'stationary_law_exact': [str(x) for x in model['mu']],
                   'sensitivity': model['labels'], 'W_exact': '1',
                   'conductance_density_cap_exact': str(model['L']),
                   'nonlumpability_exit_probabilities_exact':
                       [str(x) for x in model['nonlumpability_witness']]},
        'conditional_sampling': enumerate_conditioning(model),
        'realizations_and_prefixes': realizations_and_prefixes(model),
        'concentration_and_regeneration': budgets(),
        'largest_matrix_dimension': 5,
        'limitations': 'Finite exact checks do not prove the all-size theorem or remove its bounded-density assumption; the predicted spectral cap is 2L, not preservation of a target band.',
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
