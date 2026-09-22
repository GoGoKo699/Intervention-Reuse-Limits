#!/usr/bin/env python3
"""Exact checks of conductance-moment clipping and reversible graph sampling.

Checks full signed forcing, stratified conditional Bernstein ingredients,
global rate rescaling, reset, and exact finite error budgets. Exhaustive small
sample enumeration replaces simulation. Uniform conclusions remain proved in
docs/MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md, not inferred from these cases.
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

import verify_bounded_density_sampling as previous


reused, bounded = previous.reused, previous.bounded
require, Q = reused.require, sp.Rational


def matching_target() -> dict:
    count, cap, threshold = 6, sp.Integer(3), sp.Integer(6)
    mu, labels = sp.ones(1, count)/count, [-1]*3+[1]*3
    flip = sp.zeros(count)
    for i in range(count):
        flip[i, (i+3) % count] = 1
    refresh = sp.ones(count)/count
    K = flip+refresh-2*sp.eye(count)
    density = sp.Matrix(count, count, lambda i, j: K[i, j]/mu[j] if i != j else 0)
    clipped = density.applyfunc(lambda x: min(x, threshold))
    KB = clipped*sp.diag(*mu)
    for i in range(count):
        KB[i, i] = -sum(KB[i, j] for j in range(count) if j != i)
    require(KB == refresh-sp.eye(count)+Q(5, 6)*(flip-sp.eye(count)),
            'Exact clipped matching-graph generator')
    require(K.eigenvals() == {0: 1, -1: 2, -3: 3}, 'Original exact spectral cap')
    require(KB.eigenvals() == {0: 1, -1: 2, -Q(8, 3): 3},
            'Clipping retains the spectral cap by decreasing its Dirichlet form')
    require(all(-K[i, i] <= cap*(1-mu[i]) for i in range(count)),
            'Spectral-cap bound on each exit rate')
    return {'mu': mu, 'labels': labels, 'K': K, 'KB': KB, 'q': density,
            'qB': clipped, 'cap': cap, 'B': threshold, 'b': threshold/cap,
            'PB': sp.eye(count)+KB/cap}


def clipping_forcing(model: dict) -> dict:
    mu, density, clipped = model['mu'], model['q'], model['qB']
    removed = density-clipped
    tail = sum(mu[i]*mu[j]*removed[i, j] for i in range(6) for j in range(6))
    require(tail == Q(1, 6), 'Directed stationary removed-flux normalization')
    moments = {}
    for alpha in (1, 2):
        moment = sum(mu[i]*mu[j]*density[i, j]**(1+alpha)
                     for i in range(6) for j in range(6))
        require(tail <= moment/model['B']**alpha, 'Global moment controls clipping tail')
        moments[str(alpha)] = str(moment)
    x = sp.symbols('x0:6', nonnegative=True)
    hidden = sp.Matrix([[mu[i]*x[i] for i in range(6)]])
    forcing = hidden*(model['K']-model['KB'])
    flux_formula = sp.Matrix([[mu[j]*sum(mu[i]*removed[i, j]*(x[i]-x[j])
                                       for i in range(6)) for j in range(6)]])
    require((forcing-flux_formula).applyfunc(sp.expand) == sp.zeros(1, 6),
            'Exact symmetric signed-forcing identity, including the diagonal')
    require(sum(forcing).expand() == 0, 'Forcing has total mass zero')
    R = Q(4, 3)
    largest = sp.Integer(0)
    for bits in itertools.product((0, 1), repeat=6):
        values = forcing.subs({x[i]: R**2*bits[i] for i in range(6)})
        norm = sum(abs(value) for value in values)
        require(norm <= R**2*tail, 'Exact forcing bound at all density-box vertices')
        largest = max(largest, norm)
    require(largest == R**2*tail, 'The symmetric forcing constant is attained')
    # A normalized full probability law also attains this algebraic bound.
    values = [R**2]*3+[0]*3
    p = sp.Matrix([[1-sum(mu[i]*values[i] for i in range(6))]
                   +[mu[i]*values[i] for i in range(6)]])
    require(min(p) >= 0 and sum(p) == 1, 'Normalized nonnegative witness probability')
    y = sp.symbols('y', positive=True)
    full = reused.full_generator(model['K'], mu, sp.Matrix(model['labels']), y)
    full_B = reused.full_generator(model['KB'], mu, sp.Matrix(model['labels']), y)
    physical_forcing = p*(full-full_B)
    require(physical_forcing[0] == 0 and sum(abs(v) for v in physical_forcing) == R**2*tail,
            'Full physical-generator forcing has the same sharp signed L1 constant')
    t, radius = sp.symbols('t radius', positive=True)
    require(sp.integrate(sp.exp(-t/radius), (t, 0, sp.oo)) == radius,
            'Common-reset resolvent multiplies the forcing bound by R')
    return {'threshold_exact': str(model['B']), 'tail_exact': str(tail),
            'density_moments_exact': moments, 'density_box_vertices_checked': 64,
            'R_exact': str(R), 'attained_signed_forcing_L1_exact': str(largest),
            'all_horizon_Duhamel_bound_exact': str(R**3*tail),
            'scope': 'The normalized witness checks the forcing inequality; it is not asserted to be an actual reachable law.'}


def sampled(model: dict, samples: tuple[int, ...], eta: sp.Expr) -> dict:
    count = len(samples)
    omega = sp.ones(1, count)/count
    gamma = [model['labels'][i] for i in samples]
    require(gamma == [-1]*(count//2)+[1]*(count//2), 'Stratified sample positions')
    Khat = sp.zeros(count)
    for i, x in enumerate(samples):
        for j, y in enumerate(samples):
            if i != j:
                Khat[i, j] = omega[j]*model['qB'][x, y]
        Khat[i, i] = -sum(Khat[i, j] for j in range(count) if j != i)
    Phat = sp.eye(count)+Khat/model['cap']
    Ptilde = sp.eye(count)+Khat/(model['cap']*(1+eta))
    Pstar = (1-eta)*Ptilde+eta*sp.ones(count, 1)*omega
    return {'samples': samples, 'omega': omega, 'gamma': gamma, 'Khat': Khat,
            'Phat': Phat, 'Ptilde': Ptilde, 'Pstar': Pstar,
            'Kstar': model['cap']*(Pstar-sp.eye(count))}


def families(model: dict, ell: int) -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    U, V = [], []
    for length in range(ell+1):
        for word in itertools.product((-1, 1), repeat=length):
            f = reused.future_prediction(model['PB'], model['labels'], word)
            for symbol in (-1, 1):
                u = sp.diag(*[int(label == symbol) for label in model['labels']])*f
                V.append(u)
                if length < ell:
                    U.append(u)
    return U, V


def conditional_bernstein(model: dict) -> dict:
    strata, n, omega = ((0, 1, 2), (3, 4, 5)), 2, sp.ones(1, 4)/4
    U, _ = families(model, 2)
    configurations = [(xs, sampled(model, xs, Q(1, 8)))
                      for xs in itertools.product(strata[0], strata[0], strata[1], strata[1])]
    checks, max_bias, max_variance = 0, sp.Integer(0), sp.Integer(0)
    for i in range(4):
        for x in strata[i//n]:
            for u in U+[None]:
                F = sp.Matrix([model['qB'][x, y]/model['cap']
                               * (1 if u is None else u[y]-u[x]) for y in range(6)])
                require(F[x] == 0 and max(abs(v) for v in F) <= model['b'],
                        'Exit and row tests have zero self term and range at most b')
                moment = (model['mu']*F.applyfunc(lambda v: v*v))[0]
                require(moment <= model['b'], 'Global row cap gives the Bernstein second moment')
                bias = -omega[i]*sum(F[y] for y in strata[i//n])/3
                mean, variance = sp.Integer(0), sp.Integer(0)
                for xs, graph in configurations:
                    if xs[i] != x:
                        continue
                    error = sum(omega[j]*F[xs[j]] for j in range(4))-(model['mu']*F)[0]
                    if u is None:
                        direct = -graph['Khat'][i, i]/model['cap']
                        direct -= -model['KB'][x, x]/model['cap']
                    else:
                        ux = sp.Matrix([u[y] for y in xs])
                        direct = (graph['Phat']*ux)[i]-(model['PB']*u)[x]
                    require(error == direct, 'Exact row/exit empirical identity before rescaling')
                    mean += error/27
                    variance += (error-bias)**2/27
                require(mean == bias and abs(bias) <= model['b']/n,
                        'Exact conditional self-row bias')
                sum_variances = sp.Integer(0)
                proxy = sp.Integer(0)
                for j in range(4):
                    if j == i:
                        continue
                    local = [F[y] for y in strata[j//n]]
                    local_mean = sum(local)/3
                    sum_variances += omega[j]**2*sum((v-local_mean)**2 for v in local)/3
                    proxy += omega[j]**2*sum(v*v for v in local)/3
                require(variance == sum_variances <= proxy <= model['b']/n,
                        'Exact conditional variance and linear-b Bernstein proxy')
                max_bias, max_variance = max(max_bias, abs(bias)), max(max_variance, variance)
                checks += 1
    require(max_bias > 0 and max_variance > 0, 'Nontrivial bias and sampling variation are exercised')
    return {'enumerated_stratified_configurations': len(configurations),
            'conditional_row_and_exit_checks': checks,
            'maximum_self_row_bias_exact': str(max_bias),
            'maximum_conditional_variance_exact': str(max_variance),
            'variance_proxy_exact': str(model['b']/n)}


def rescaling_and_prefixes(model: dict) -> dict:
    bad = sampled(model, (0, 1, 3, 3), Q(1, 8))
    require(min(bad['Phat']) == -Q(1, 12), 'Raw sampled update really has a negative diagonal')
    require(max(-bad['Khat'][i, i] for i in range(4)) == Q(13, 4),
            'Raw sampled exit exceeds the fixed clock Lambda=3')
    require(all(-bad['Khat'][i, i] <= model['cap']*(1+Q(1, 8)) for i in range(4)),
            'The exit-test tolerance permits this raw sample')
    require(max(-value for value in bad['Kstar'].eigenvals()) == Q(293, 72) > model['cap'],
            'The final relaxation cap need not equal the original spectral cap')
    eta, ell = Q(1, 128), 3
    good = sampled(model, tuple(range(6)), eta)
    records = []
    for graph, precision in ((bad, Q(1, 8)), (good, eta)):
        count, omega = len(graph['samples']), graph['omega']
        require(graph['Ptilde'] == (graph['Phat']+precision*sp.eye(count))/(1+precision),
                'Exact common rescaling identity')
        require(min(graph['Ptilde']) >= 0 and min(graph['Pstar']) > 0,
                'Rescaling restores stochasticity and reset restores irreducibility')
        require(graph['Pstar']*sp.ones(count, 1) == sp.ones(count, 1), 'Stochastic final update')
        require(omega*graph['Pstar'] == omega, 'Exact stationary sampled law')
        require(sp.diag(*omega)*graph['Pstar'] == graph['Pstar'].T*sp.diag(*omega),
                'Ordinary detailed balance survives both transformations')
        require(all(-graph['Kstar'][i, i] <= model['cap'] for i in range(count)),
                'The final outgoing cap is the original fixed Lambda')
        for eigenvalue in graph['Kstar'].eigenvals():
            require(bool(-2*model['cap'] <= eigenvalue <= 0), 'Exact final relaxation cap 2 Lambda')
            require(eigenvalue == 0 or bool(eigenvalue <= -precision*model['cap']),
                    'Reset gives a strictly positive gap')
        require(bounded.histogram(omega, graph['gamma'])
                == bounded.histogram(model['mu'], model['labels']), 'Exact actuator histogram and W')
        bounded.physical_identities(graph['Pstar'], omega, graph['gamma'], model['cap'], True)
        records.append({'samples': list(graph['samples']), 'eta_exact': str(precision),
                        'raw_minimum_update_entry_exact': str(min(graph['Phat'])),
                        'final_minimum_update_entry_exact': str(min(graph['Pstar'])),
                        'final_largest_outgoing_rate_exact':
                            str(max(-graph['Kstar'][i, i] for i in range(count))),
                        'final_largest_relaxation_rate_exact':
                            str(max(-value for value in graph['Kstar'].eigenvals()))})
    U, V = families(model, ell)
    require(good['Phat'] == model['PB'], 'The chosen sample has zero raw one-step error')
    for u in U:
        require(max(abs(v) for v in (good['Ptilde']-model['PB'])*u) <= 2*eta,
                'Rescaling error bound of 2 eta')
        require(max(abs(v) for v in (good['Pstar']-good['Ptilde'])*u) <= eta,
                'Reset error bound of eta')
        require(max(abs(v) for v in (good['Pstar']-model['PB'])*u) <= 3*eta,
                'Combined one-step error bound of 3 eta')
    require(all((good['omega']*v)[0] == (model['mu']*v)[0] for v in V),
            'Exact empirical-average good event for the selected sample')
    prefix = []
    for length in range(1, ell+2):
        tv = sp.Integer(0)
        for word in itertools.product((-1, 1), repeat=length):
            original = reused.word_probability(model['PB'], model['mu'], model['labels'], word)
            surrogate = reused.word_probability(good['Pstar'], good['omega'], good['gamma'], word)
            require(abs(original-surrogate) <= (3*(length-1)+1)*eta,
                    'Stationary prefix error with the rescaling coefficient 3')
            tv += abs(original-surrogate)/2
        bound = Q(1, 2)*2**length*(3*(length-1)+1)*eta
        require(tv <= bound, 'Prefix total-variation budget')
        prefix.append({'length': length, 'TV_exact': str(tv), 'bound_exact': str(bound)})
    return {'sampled_graphs': records, 'word_probabilities_checked': 30, 'prefix_TV': prefix}


def sample_budget(m: int, ell: int, b: Fraction, eta: Fraction) -> dict:
    V = sum(m**j for j in range(1, ell+2))
    low, high = previous.log_bounds(Fraction(32*m*(V+1))*b/eta)
    coefficient = 512*b/eta**2
    nlow, nhigh = previous.ceiling(coefficient*low), previous.ceiling(coefficient*high)
    require(nlow == nhigh, 'Rational logarithm enclosures resolve the exact sample ceiling')
    n = nlow
    require(n >= 2*b/eta and n <= 1024*b/eta**2*low, 'Self-bias and sample-size bounds')
    denominator = 8*b+Fraction(8, 3)*b*eta
    require(denominator <= 12*b, 'Bernstein denominator including centered summand range')
    row_exponent = (n*eta**2/(12*b)).__floor__()
    mean_exponent = (2*n*eta**2).__floor__()
    # e^{-x} <= 2^{-floor(x)}; compare integer bit lengths instead of forming
    # an enormous denominator for the large-b empirical-average exponent.
    row_prefactor, mean_prefactor = 2*m*n*(V+1), 2*V
    require(row_prefactor.bit_length()+101 <= row_exponent
            and mean_prefactor.bit_length()+101 <= mean_exponent,
            'Each Bernstein/Hoeffding failure term is strictly below 2^-101')
    return {'m': m, 'ell': ell, 'b_exact': str(b), 'eta_exact': str(eta),
            'samples_per_stratum': n, 'total_states': 1+m*n,
            'union_failure_bound': '< 2^-100'}


def error_budgets() -> dict:
    concentration = [sample_budget(m, ell, b, Fraction(1, 8))
                     for m in (2, 3) for ell in (1, 3) for b in (Fraction(1), Fraction(5))]
    R, A, cap = Fraction(3, 2), Fraction(3, 2), Fraction(3)
    C, q = 1+2*R**2, cap*R/(1+cap*R)
    total = []
    for alpha, M, deltas in ((1, Fraction(53, 6), (Fraction(1, 4), Fraction(1, 32), Fraction(1, 512))),
                              (2, Fraction(256, 3), (Fraction(1, 4), Fraction(1, 16), Fraction(1, 64)))):
        for delta in deltas:
            powered = 2*R**3*M/delta
            if alpha == 1:
                threshold = powered
            else:
                numerator, denominator = sp.integer_nthroot(powered.numerator, 2), sp.integer_nthroot(powered.denominator, 2)
                require(numerator[1] and denominator[1], 'Chosen quadratic threshold is rational exactly')
                threshold = Fraction(numerator[0], denominator[0])
            threshold = max(cap, threshold)
            ell = 1
            while C*q**(ell+1) > delta/4:
                ell += 1
            require(ell == 1 or C*q**ell > delta/4, 'Exact ceiling convention for reset horizon')
            eta = delta/(2*C*A*2**(ell+1)*(3*ell+1))
            theta = Fraction(1, 2)*2**(ell+1)*(3*ell+1)*eta
            clipping, prefix, clock = R**3*M/threshold**alpha, C*A*theta, C*q**(ell+1)
            require(clipping <= delta/2 and prefix == delta/4 and clock <= delta/4,
                    'Exact clipping, prefix and clock allocation')
            require(clipping+prefix+clock <= delta, 'Combined actual-mean certificate')
            item = sample_budget(2, ell, threshold/cap, eta)
            item.update({'alpha': alpha, 'moment_bound_exact': str(M), 'delta_exact': str(delta),
                         'clipping_threshold_exact': str(threshold), 'clipping_error_exact': str(clipping),
                         'prefix_error_exact': str(prefix), 'clock_error_exact': str(clock)})
            total.append(item)
    return {'concentration_cases': concentration, 'full_error_budgets': total,
            'fixed_clock_exact': str(cap), 'R_exact': str(R), 'A_H_exact': str(A),
            'method': 'Exact Fraction arithmetic and rational log enclosures; no floating-point rounding or simulated samples.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/moment_density_sampling.json'))
    args = parser.parse_args()
    model = matching_target()
    sources = [Path(__file__).resolve(), Path(previous.__file__).resolve(),
               Path(bounded.__file__).resolve(), Path(reused.__file__).resolve()]
    report = {'status': 'PASS',
              'scope': 'Exact conductance clipping, signed physical forcing, conditional Bernstein ingredients, fixed-clock reversible rescaling and reset, prefix recursion, and moment-based error budgets; no simulations.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                           'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
              'clipping_and_forcing': clipping_forcing(model),
              'conditional_bernstein': conditional_bernstein(model),
              'rescaling_and_prefixes': rescaling_and_prefixes(model),
              'concentration_and_error_budgets': error_budgets(),
              'largest_matrix_dimension': 7,
              'limitations': 'These finite checks do not remove the global density-tail/moment hypothesis, preserve the original spectral endpoints, or prove the theorem by sample extrapolation.',
              'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
