#!/usr/bin/env python3
"""Replay retained small Ising-model comparators; optionally repeat bounded fits.

Default execution recomputes saved feasible models without optimization. Use
--refit only to repeat the documented fixed exploratory search. Achieved errors
are numerical upper/falsification diagnostics, never certified lower bounds.
"""
import os
for _thread_variable in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
                         'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_thread_variable] = '1'

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.optimize import least_squares, minimize
from scipy.special import expit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT/'reports/familiar_switch_screen.json'
PROOF_NAMES = ['FAMILIAR_SWITCH_PROTOCOLS.md', 'FAMILIAR_SWITCH_STRUCTURE.md']


def number(value):
    return float(f'{float(value):.12g}')


def ising(couplings, alphas, h):
    n = len(alphas)
    states = np.asarray([[1 if code & (1 << i) else -1 for i in range(n)]
                         for code in range(1 << n)], dtype=float)
    q = np.zeros((1 << n, 1 << n))
    for row, spins in enumerate(states):
        for i, alpha in enumerate(alphas):
            field = h if i == 0 else 0.
            if i:
                field += couplings[i-1]*spins[i-1]
            if i+1 < n:
                field += couplings[i]*spins[i+1]
            q[row, row ^ (1 << i)] = alpha*expit(-2*spins[i]*field)
        q[row, row] = -sum(q[row])
    potential = h*states[:, 0]
    for i, coupling in enumerate(couplings):
        potential += coupling*states[:, i]*states[:, i+1]
    pi = np.exp(potential-np.max(potential))
    pi /= sum(pi)
    return q, pi, (states[:, 0]+1)/2


def affine_mean_generator(couplings, alphas, h):
    n = len(alphas)
    a = np.zeros((n+1, n+1))
    if n == 1:
        a[1, 0], a[1, 1] = alphas[0]*math.tanh(h), -alphas[0]
        return a
    j = couplings[0]
    a[1, 0] = alphas[0]*(math.tanh(h+j)+math.tanh(h-j))/2
    a[1, 1] = -alphas[0]
    a[1, 2] = alphas[0]*(math.tanh(h+j)-math.tanh(h-j))/2
    if n == 2:
        a[2, 1], a[2, 2] = alphas[1]*math.tanh(j), -alphas[1]
    elif n == 3:
        left, right = couplings
        a[2, 1] = alphas[1]*(math.tanh(left+right)+math.tanh(left-right))/2
        a[2, 2] = -alphas[1]
        a[2, 3] = alphas[1]*(math.tanh(left+right)-math.tanh(left-right))/2
        a[3, 2], a[3, 3] = alphas[2]*math.tanh(right), -alphas[2]
    else:
        raise ValueError('At most three spins are included')
    return a


def model(definition, fields):
    kind = definition['kind']
    matrices, laws = [], []
    if kind == 'ising':
        for h in fields:
            q, law, observable = ising(definition['couplings'], definition['alphas'], h)
            matrices.append(q)
            laws.append(law)
    elif kind == 'heatbath_two_state':
        for h, alpha in zip(fields, definition['alphas_by_field']):
            q, law, observable = ising([], [alpha], h)
            matrices.append(q)
            laws.append(law)
    elif kind == 'reversible_three_state':
        pi0 = np.array([.5, definition['split_mass'], .5-definition['split_mass']])
        sign = definition['singleton_sign']
        spins = np.array([sign, -sign, -sign], dtype=float)
        observable = (1+spins)/2
        for h, edges in zip(fields, definition['conductances_by_field']):
            pi = pi0*np.exp(h*spins)
            pi /= sum(pi)
            w01, w02, w12 = edges
            flux = np.array([[0., w01, w02], [w01, 0., w12], [w02, w12, 0.]])
            q = flux/pi[:, None]
            np.fill_diagonal(q, -np.sum(q, axis=1))
            matrices.append(q)
            laws.append(pi)
    elif kind == 'exact_stationary_triangle':
        t = math.tanh(definition['J'])
        spins = np.array([-1., 1., 1.])
        z = np.array([-t, -2*t, (1+t*t)/(2*t)])
        f = np.column_stack((np.ones(3), spins, z))
        pi0 = np.array([.5, (1-t*t)/(2*(1+5*t*t)), 3*t*t/(1+5*t*t)])
        observable = (1+spins)/2
        for h in fields:
            u = math.tanh(h)
            a, b = (1-t*t)*u/(1-t*t*u*u), t*(1-u*u)/(1-t*t*u*u)
            action = np.array([[0., a, 0.], [0., -1., t], [0., b, -1.]])
            q = f @ action @ np.linalg.inv(f)
            pi = pi0*np.exp(h*spins)
            pi /= sum(pi)
            matrices.append(q)
            laws.append(pi)
    else:
        raise ValueError(kind)
    return matrices, laws[0], observable, laws


def responses(definition, fields, menu):
    generators, pi0, observable, _ = model(definition, fields)
    cache = {(int(field), float(duration)): expm(duration*generators[field])
             for protocol in menu for field, duration in protocol}
    result = []
    for protocol in menu:
        p = pi0.copy()
        for field, duration in protocol:
            p = p @ cache[field, float(duration)]
        result.append(p @ observable)
    return np.asarray(result)


def model_diagnostics(definition, fields):
    qs, pi0, observable, laws = model(definition, fields)
    assert max(len(q) for q in qs) <= 8
    offdiag = [q[i, j] for q in qs for i in range(len(q)) for j in range(len(q)) if i != j]
    exits = [float(np.max(-np.diag(q))) for q in qs]
    stationary = max(float(np.max(np.abs(pi @ q))) for q, pi in zip(qs, laws))
    detailed = max(float(np.max(np.abs(pi[:, None]*q-(pi[:, None]*q).T))) for q, pi in zip(qs, laws))
    assert min(offdiag) >= -2e-14 and max(exits) <= 3+2e-12
    assert stationary < 2e-12
    if definition['kind'] != 'exact_stationary_triangle':
        assert detailed < 2e-12
    result = {'generators': [q.tolist() for q in qs], 'stationary_laws': [pi.tolist() for pi in laws],
              'initial_law': pi0.tolist(), 'occupation_readout': observable.tolist(),
              'maximum_exit': number(max(exits)), 'minimum_off_diagonal': number(min(offdiag)),
              'stationarity_residual': number(stationary), 'detailed_balance_residual': number(detailed)}
    if definition['kind'] == 'ising':
        n = len(definition['alphas'])
        states = np.asarray([[1 if code & (1 << i) else -1 for i in range(n)] for code in range(1 << n)])
        basis = np.column_stack((np.ones(1 << n), states))
        closure = max(float(np.max(np.abs(q @ basis-basis @ affine_mean_generator(
            definition['couplings'], definition['alphas'], h).T))) for q, h in zip(qs, fields))
        assert closure < 2e-13
        result['affine_closure_residual'] = number(closure)
    elif definition['kind'] == 'exact_stationary_triangle':
        t = math.tanh(definition['J'])
        s, z = np.array([-1., 1., 1.]), np.array([-t, -2*t, (1+t*t)/(2*t)])
        closure = 0.
        for q, h in zip(qs, fields):
            u = math.tanh(h)
            a, b = (1-t*t)*u/(1-t*t*u*u), t*(1-u*u)/(1-t*t*u*u)
            closure = max(closure, float(np.max(np.abs(q @ s-(a-s+b*z)))),
                          float(np.max(np.abs(q @ z-(t*s-z)))))
        assert closure < 2e-13 and max(exits) < 2
        result['affine_closure_residual'] = number(closure)
    return result


def replay(report):
    out = copy.deepcopy(report)
    for panel in out['panels']:
        fields = panel['fields']
        panel['target_diagnostics'] = model_diagnostics(panel['target'], fields)
        panel['target_occupations'] = [number(x) for x in responses(panel['target'], fields, panel['menu'])]
        target = responses(panel['target'], fields, panel['menu'])
        for comparator in panel['comparators']:
            definition = comparator['model']
            values = responses(definition, fields, panel['menu'])
            comparator['diagnostics'] = model_diagnostics(definition, fields)
            comparator['occupations'] = [number(x) for x in values]
            comparator['maximum_occupation_error'] = number(np.max(np.abs(values-target)))
            comparator['rms_occupation_error'] = number(np.sqrt(np.mean((values-target)**2)))
            for heldout in comparator.get('heldout', []):
                true = responses(panel['target'], fields, heldout['menu'])
                predicted = responses(definition, fields, heldout['menu'])
                heldout['target_occupations'] = [number(x) for x in true]
                heldout['comparator_occupations'] = [number(x) for x in predicted]
                heldout['maximum_occupation_error'] = number(np.max(np.abs(predicted-true)))
        if panel['family'] == 'two_spin_grid':
            ordinary = [c['maximum_occupation_error'] for c in panel['comparators'] if c['role'] == 'ordinary_reversible']
            panel['best_retained_ordinary_error'] = min(ordinary)
    grid = [p for p in out['panels'] if p['family'] == 'two_spin_grid']
    out['summary'] = {
        'largest_grid_best_retained_occupation_error': max(p['best_retained_ordinary_error'] for p in grid),
        'grid_case_count': len(grid), 'all_grid_retained_menu_errors_below_one_percent':
            all(p['best_retained_ordinary_error'] < .01 for p in grid),
        'maximum_dense_dimension': 8,
        'scope': 'Achievable numerical errors of retained shared models on the stated finite menus; no minimax lower bound or all-protocol approximation follows.'}
    out['versions'] = {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}
    out['source_sha256'] = {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out['proof_snapshot_sha256'] = {str(Path('docs')/name): hashlib.sha256((ROOT/'docs'/name).read_bytes()).hexdigest()
                                     for name in PROOF_NAMES}
    return out


def compare_saved(expected, actual, path='report'):
    """Exact structure/provenance/counts; absolute2e-11 numerical tolerance.

    Environment versions are retained as information. Model positivity,
    stationarity, detailed balance and cap checks run independently above.
    """
    if path == 'report.versions':
        return
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or expected.keys() != actual.keys():
            raise AssertionError('Saved structure differs at '+path)
        for key in expected:
            compare_saved(expected[key], actual[key], path+'.'+key)
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(expected) != len(actual):
            raise AssertionError('Saved list length differs at '+path)
        for index, (old, new) in enumerate(zip(expected, actual)):
            compare_saved(old, new, path+f'[{index}]')
    elif isinstance(expected, bool):
        if type(actual) is not bool or expected != actual:
            raise AssertionError('Saved boolean differs at '+path)
    elif isinstance(expected, int):
        if type(actual) is not int or expected != actual:
            raise AssertionError('Saved integer differs at '+path)
    elif isinstance(expected, float):
        if not isinstance(actual, (int, float)) or not math.isfinite(actual) or abs(expected-actual) > 2e-11:
            raise AssertionError('Saved numeric value differs at '+path)
    elif expected != actual:
        raise AssertionError('Saved value or provenance differs at '+path)


def theta_model(theta, singleton_sign, fields):
    split = .5*expit(theta[0])
    pi0 = np.array([.5, split, .5-split])
    s = np.array([singleton_sign, -singleton_sign, -singleton_sign])
    edges_by_field = []
    for index, h in enumerate(fields):
        pi = pi0*np.exp(h*s)
        pi /= sum(pi)
        raw = np.exp(theta[1+3*index:4+3*index])
        flux = np.array([[0., raw[0], raw[1]], [raw[0], 0., raw[2]], [raw[1], raw[2], 0.]])
        scale = 1+float(np.max(np.sum(flux/pi[:, None], axis=1)))/3
        edges_by_field.append((raw/scale).tolist())
    return {'kind': 'reversible_three_state', 'split_mass': float(split), 'singleton_sign': singleton_sign,
            'conductances_by_field': edges_by_field}


def refit_three(panel, singleton_sign):
    target = responses(panel['target'], panel['fields'], panel['menu'])
    lower, upper = np.array([-12.]+[-16.]*6), np.array([12.]+[6.]*6)
    starts = [np.array([0., *np.log([.15, .10, .05]), *np.log([.12, .08, .04])]),
              np.array([1., *np.log([.25, .03, .10]), *np.log([.20, .05, .12])]),
              np.array([-1., *np.log([.08, .22, .02]), *np.log([.05, .18, .03])])]
    def error(theta):
        return responses(theta_model(theta, singleton_sign, panel['fields']), panel['fields'], panel['menu'])-target
    runs = []
    for start in starts:
        fit = least_squares(error, start, bounds=(lower, upper), max_nfev=300,
                            xtol=3e-12, ftol=3e-12, gtol=3e-12)
        runs.append((float(np.max(np.abs(error(fit.x)))), fit))
    _, best = min(runs, key=lambda item: item[0])
    initial = np.r_[best.x, np.max(np.abs(error(best.x)))*1.01]
    def constraints(x):
        e = error(x[:-1])
        return np.r_[x[-1]-e, x[-1]+e]
    fit = minimize(lambda x: x[-1], initial, method='SLSQP', bounds=list(zip(lower, upper))+[(0., .1)],
                   constraints={'type': 'ineq', 'fun': constraints}, options={'maxiter': 150, 'ftol': 2e-13})
    chosen = fit.x[:-1] if np.max(np.abs(error(fit.x[:-1]))) < np.max(np.abs(error(best.x))) else best.x
    return theta_model(chosen, singleton_sign, panel['fields']), {
        'least_squares_nfev': [int(r.nfev) for _, r in runs],
        'least_squares_success': [bool(r.success) for _, r in runs],
        'epigraph_success': bool(fit.success), 'epigraph_iterations': int(fit.nit)}


def refit_small_ising(panel, kind):
    target = responses(panel['target'], panel['fields'], panel['menu'])
    if kind == 'heatbath_two_state':
        starts, lower, upper = ([1., 1.], [.2, .2], [.05, .5]), np.log([1e-4]*2), np.log([3.]*2)
        constructor = lambda x: {'kind': kind, 'alphas_by_field': np.exp(x).tolist()}
    else:
        starts, lower, upper = ([.4, .9, .9], [1., .8, .3], [2., .4, .1]), np.log([.001]*3), np.log([3., 1., 1.])
        constructor = lambda x: {'kind': 'ising', 'couplings': [float(np.exp(x[0]))], 'alphas': np.exp(x[1:]).tolist()}
    def error(x):
        return responses(constructor(x), panel['fields'], panel['menu'])-target
    fits = [least_squares(error, np.log(start), bounds=(lower, upper), max_nfev=120,
                          xtol=3e-9, ftol=3e-9, gtol=3e-9) for start in starts]
    best = min(fits, key=lambda fit: np.max(np.abs(error(fit.x))))
    return constructor(best.x), {'least_squares_nfev': [int(fit.nfev) for fit in fits],
                                'least_squares_success': [bool(fit.success) for fit in fits]}


def refit(report):
    result = copy.deepcopy(report)
    started = time.perf_counter()
    for panel in result['panels']:
        for comparator in panel['comparators']:
            if time.perf_counter()-started > 180:
                raise RuntimeError('Fixed refit runtime budget reached; no output report written')
            kind = comparator['model']['kind']
            if kind == 'exact_stationary_triangle':
                continue
            if kind == 'reversible_three_state':
                definition, diagnostic = refit_three(panel, comparator['model']['singleton_sign'])
            else:
                definition, diagnostic = refit_small_ising(panel, kind)
            comparator['model'], comparator['fit_diagnostics'] = definition, diagnostic
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--models', type=Path, default=DEFAULT_REPORT, help='Saved definitions and protocol menus')
    parser.add_argument('--verify-saved', nargs='?', const=DEFAULT_REPORT, type=Path,
                        help='Check deterministic replay of the supplied saved report without refitting')
    parser.add_argument('--output', type=Path, help='Optional regenerated report path; default only summarizes')
    parser.add_argument('--refit', action='store_true', help='Repeat the fixed local optimization budget; unnecessary for ordinary verification')
    args = parser.parse_args()
    if args.verify_saved is not None and args.refit:
        parser.error('--verify-saved and --refit are mutually exclusive')
    report = json.loads((args.verify_saved or args.models).read_text())
    if args.refit:
        report = refit(report)
    result = replay(report)
    if args.verify_saved is not None:
        compare_saved(report, result)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': 'PASS', 'mode': 'refit' if args.refit else 'saved_model_replay',
                      **result['summary']}, sort_keys=True))


if __name__ == '__main__':
    main()
