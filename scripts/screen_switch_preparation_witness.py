#!/usr/bin/env python3
"""Replay retained models for four endpoints from two equilibrium preparations.

No optimization runs in this script. Retained local fits give achievable
numerical upper diagnostics, not lower bounds or global-optimality claims.
The exact verifier separately encloses the rounded candidate's response error.
"""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

# The frozen helper sets BLAS thread counts before importing numerical libraries.
import screen_familiar_switches as core
import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT/'reports/switch_preparation_screen.json'
PROOFS = ['FAMILIAR_SWITCH_STRUCTURE.md', 'FAMILIAR_SWITCH_PREPARATION_WITNESS.md']
EXPERIMENTS = [('m', 0, [1]), ('a', 1, [0]), ('b', 1, [0, 1]), ('l', 0, [1, 0])]


def responses(definition, fields, clock):
    matrices, _, observable, laws = core.model(definition, fields)
    kernels = [expm(clock*q) for q in matrices]
    result = []
    for _, preparation, word in EXPERIMENTS:
        p = laws[preparation].copy()
        for field in word:
            p = p @ kernels[field]
        result.append(p @ observable)
    return np.array(result)


def witness(probabilities, sign):
    m, a, b, ell = 2*probabilities-1
    return float(b-m-a+ell+sign*(.8*ell-a*m))


def exact_rounded_feasibility(comparator):
    values = comparator['rational_parameters']
    denominator = values['denominator']
    p = F(values['split_numerator'], denominator)
    fluxes = [[F(x, denominator) for x in row] for row in values['flux_numerators_by_field']]
    model = comparator['model']
    assert model['singleton_sign'] == -1 and model['split_mass'] == float(p)
    assert model['conductances_by_field'] == [[float(x) for x in row] for row in fluxes]
    laws = [[F(1, 2), p, F(1, 2)-p], [F(1, 10), F(9, 5)*p, F(9, 5)*(F(1, 2)-p)]]
    matrices = []
    for law, edges in zip(laws, fluxes):
        q = [[F(0) for _ in range(3)] for _ in range(3)]
        for (i, j), flux in zip([(0, 1), (0, 2), (1, 2)], edges):
            q[i][j], q[j][i] = flux/law[i], flux/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        assert sum(law) == 1 and min(law) > 0
        assert all(q[i][j] > 0 for i in range(3) for j in range(3) if i != j)
        assert all(law[i]*q[i][j] == law[j]*q[j][i] for i in range(3) for j in range(3))
        assert all(sum(law[i]*q[i][j] for i in range(3)) == 0 for j in range(3))
        assert all(-q[i][i] < 1 for i in range(3))
        matrices.append(q)
    return {'stationary_laws': [[str(x) for x in law] for law in laws],
            'generators': [[[str(x) for x in row] for row in q] for q in matrices],
            'maximum_exit': str(max(-q[i][i] for q in matrices for i in range(3))),
            'scope': 'Exact positivity, Gibbs tilt, detailed balance, stationarity and exit feasibility; response replay below is floating arithmetic.'}


def response_record(definition, fields, clock, target):
    predicted = responses(definition, fields, clock)
    assert np.min(predicted) >= -1e-12 and np.max(predicted) <= 1+1e-12
    return {'occupations': [core.number(x) for x in predicted],
            'occupation_errors': [core.number(x) for x in predicted-target],
            'maximum_occupation_error': core.number(np.max(np.abs(predicted-target)))}


def replay(saved):
    result = copy.deepcopy(saved)
    fields, clock = result['fields'], result['clock']
    assert fields == [0., math.log(3)] and clock == 1.5
    assert result['target'] == {'kind': 'ising', 'couplings': [math.log(3)], 'alphas': [1., 1.]}
    assert result['experiments'] == [{'name': name, 'preparation_field': prep, 'word': word}
                                     for name, prep, word in EXPERIMENTS]
    target = responses(result['target'], fields, clock)
    result['target_diagnostics'] = core.model_diagnostics(result['target'], fields)
    result['target_occupations'] = [core.number(x) for x in target]
    result['target_witness_values'] = {str(sign): core.number(witness(target, sign)) for sign in (1, -1)}
    fitted_signs, rounded_count, errors = [], 0, []
    for comparator in result['comparators']:
        model = comparator['model']
        assert model['kind'] == 'reversible_three_state'
        comparator['diagnostics'] = core.model_diagnostics(model, fields)
        comparator['responses'] = response_record(model, fields, clock, target)
        residual = witness(responses(model, fields, clock), model['singleton_sign'])
        assert abs(residual) < 3e-12
        comparator['witness_residual'] = core.number(residual)
        if comparator['role'] == 'bounded_local_fit':
            fitted_signs.append(model['singleton_sign'])
            errors.append(comparator['responses']['maximum_occupation_error'])
        else:
            assert comparator['role'] == 'rounded_rational_upper'
            comparator['exact_feasibility'] = exact_rounded_feasibility(comparator)
            rounded_count += 1
    assert sorted(fitted_signs) == [-1, 1] and rounded_count == 1
    triangle = {'kind': 'exact_stationary_triangle', 'J': math.log(3)}
    result['exact_stationary_triangle'] = {
        'model': triangle, 'diagnostics': core.model_diagnostics(triangle, fields),
        'responses': response_record(triangle, fields, clock, target)}
    assert result['exact_stationary_triangle']['diagnostics']['minimum_off_diagonal'] > 0
    assert result['exact_stationary_triangle']['responses']['maximum_occupation_error'] < 3e-12
    result['summary'] = {'endpoint_experiments': 4, 'equilibrium_preparations': 2,
                         'retained_fitted_models': 2, 'rounded_rational_models': 1,
                         'maximum_dense_dimension': 4, 'best_achieved_fit_occupation_error': min(errors),
                         'scope': 'Achieved numerical errors on four specified endpoints only; no fitted lower bound, global optimum, or all-protocol upper.'}
    result['versions'] = {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}
    result['source_sha256'] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in (Path(__file__), Path(core.__file__))}
    result['proof_snapshot_sha256'] = {str(Path('docs')/name): hashlib.sha256((ROOT/'docs'/name).read_bytes()).hexdigest()
                                       for name in PROOFS}
    result['status'] = 'PASS'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--models', type=Path, default=DEFAULT_REPORT)
    parser.add_argument('--verify-saved', nargs='?', const=DEFAULT_REPORT, type=Path,
                        help='Replay without fitting; numerical tolerance2e-11, versions informational')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    saved = json.loads((args.verify_saved or args.models).read_text())
    result = replay(saved)
    if args.verify_saved is not None:
        core.compare_saved(saved, result)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': result['status'], 'mode': 'saved_model_replay', **result['summary']}, sort_keys=True))


if __name__ == '__main__':
    main()
