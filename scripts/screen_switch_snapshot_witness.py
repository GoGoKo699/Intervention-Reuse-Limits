#!/usr/bin/env python3
"""Replay retained three-state models for two initial/final joint laws.

No optimizer is run. The retained fits are achievable numerical upper
diagnostics, not lower bounds or global-optimality claims. Exact response
enclosures for the rounded candidate belong to the separate verifier.
"""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform

# The frozen helper sets numerical-library thread counts before their import.
import screen_familiar_switches as core
import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT/'reports/switch_snapshot_screen.json'
PROOFS = ['FAMILIAR_SWITCH_PREPARATION_WITNESS.md', 'FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md']
WORDS = [[0, 1], [1, 0]]
SIGNS = np.array([-1., 1.])


def joint_laws(definition, fields, clock):
    matrices, pi0, observable, _ = core.model(definition, fields)
    kernels = [expm(clock*q) for q in matrices]
    masks = [1-observable, observable]
    tables = []
    for word in WORDS:
        transition = kernels[word[0]] @ kernels[word[1]]
        tables.append([[(pi0*masks[i]) @ transition @ masks[j]
                        for j in range(2)] for i in range(2)])
    tables = np.array(tables)
    assert np.min(tables) >= -2e-14
    assert np.max(np.abs(np.sum(tables, axis=(1, 2))-1)) < 2e-13
    # The feature/TV identity below requires equal initial marginals. This
    # fixture uses balanced initial marginals for every compared model.
    assert np.max(np.abs(np.sum(tables, axis=2)-.5)) < 2e-13
    return tables


def features(tables):
    return np.array([value for table in tables for value in
                     [np.sum(table*SIGNS[None, :]), np.sum(table*np.outer(SIGNS, SIGNS))]])


def witness(values, sign):
    m, c, ell, d = values
    return float(.8*(c-d)+sign*((.8-m)*ell-.8*m*d))


def response_record(definition, fields, clock, target):
    predicted = joint_laws(definition, fields, clock)
    values, target_values = features(predicted), features(target)
    distances = .5*np.sum(np.abs(predicted-target), axis=(1, 2))
    feature_distances = .5*np.max(np.abs(values-target_values).reshape(2, 2), axis=1)
    assert np.max(np.abs(distances-feature_distances)) < 2e-13
    return {'joint_laws': predicted.tolist(),
            'features': [core.number(x) for x in values],
            'feature_errors': [core.number(x) for x in values-target_values],
            'TV_by_word': [core.number(x) for x in distances],
            'maximum_TV': core.number(np.max(distances)),
            'balanced_feature_TV_identity_residual': core.number(np.max(np.abs(distances-feature_distances)))}


def exact_rounded_feasibility(comparator):
    values = comparator['rational_parameters']
    denominator = values['denominator']
    p = F(values['split_numerator'], denominator)
    fluxes = [[F(x, denominator) for x in row] for row in values['flux_numerators_by_field']]
    model = comparator['model']
    assert model['singleton_sign'] == -1 and model['split_mass'] == float(p)
    assert model['conductances_by_field'] == [[float(x) for x in row] for row in fluxes]
    law0 = [F(1, 2), p, F(1, 2)-p]
    laws = [law0, [mass*(1+F(4, 5)*spin) for mass, spin in zip(law0, [-1, 1, 1])]]
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
            'scope': 'Exact positivity, Gibbs tilt, detailed balance, stationarity and exit feasibility; joint-response replay is floating arithmetic.'}


def triangle_check(target_definition, fields, clock, target):
    triangle = {'kind': 'exact_stationary_triangle', 'J': math.log(3)}
    t = math.tanh(math.log(3))
    coordinates = [np.array([-1., -1., 1., 1.]), np.array([-t, -2*t, (1+t*t)/(2*t)])]
    conditional = []
    for model, z in zip([target_definition, triangle], coordinates):
        _, pi0, observable, _ = core.model(model, fields)
        means = []
        for sign, mask in zip(SIGNS, [1-observable, observable]):
            mass = pi0 @ mask
            mean_z = (pi0*mask) @ z/mass
            assert abs(mass-.5) < 2e-14 and abs(mean_z-sign*t) < 2e-14
            means.append(core.number(mean_z))
        conditional.append(means)
    diagnostics = core.model_diagnostics(triangle, fields)
    predicted = response_record(triangle, fields, clock, target)
    assert diagnostics['minimum_off_diagonal'] > 0
    assert predicted['maximum_TV'] < 3e-13
    return {'model': triangle, 'diagnostics': diagnostics, 'responses': predicted,
            'conditional_coordinate_means_target_triangle': conditional,
            'scope': 'Shared closed coordinate equations and matching conditional initial coordinates reproduce both joint laws; no full-path-law assertion.'}


def replay(saved):
    result = copy.deepcopy(saved)
    fields, clock = result['fields'], result['clock']
    assert fields == [0., math.log(3)] and clock == 1.5
    assert result['target'] == {'kind': 'ising', 'couplings': [math.log(3)], 'alphas': [1., 1.]}
    assert result['words'] == WORDS
    assert result['joint_table_labels'] == {'rows_initial': [-1, 1], 'columns_final': [-1, 1]}
    assert result['feature_order'] == ['m_0H', 'c_0H', 'm_H0', 'c_H0']
    target = joint_laws(result['target'], fields, clock)
    result['target_diagnostics'] = core.model_diagnostics(result['target'], fields)
    result['target_joint_laws'] = target.tolist()
    result['target_features'] = [core.number(x) for x in features(target)]
    result['target_witness_values'] = {str(sign): core.number(witness(features(target), sign)) for sign in (1, -1)}
    fitted_signs, rounded_count, errors = [], 0, []
    for comparator in result['comparators']:
        model = comparator['model']
        assert model['kind'] == 'reversible_three_state'
        comparator['diagnostics'] = core.model_diagnostics(model, fields)
        comparator['responses'] = response_record(model, fields, clock, target)
        residual = witness(features(joint_laws(model, fields, clock)), model['singleton_sign'])
        assert abs(residual) < 3e-12
        comparator['ordinary_witness_residual'] = core.number(residual)
        if comparator['role'] == 'bounded_local_fit':
            fitted_signs.append(model['singleton_sign'])
            errors.append(comparator['responses']['maximum_TV'])
        else:
            assert comparator['role'] == 'rounded_rational_upper'
            comparator['exact_feasibility'] = exact_rounded_feasibility(comparator)
            rounded_count += 1
    assert sorted(fitted_signs) == [-1, 1] and rounded_count == 1
    result['exact_stationary_triangle'] = triangle_check(result['target'], fields, clock, target)
    result['summary'] = {'joint_experiments': 2, 'equilibrium_preparations': 1,
                         'readouts_per_trial': 2, 'control_segments_per_trial': 2,
                         'retained_fitted_models': 2, 'rounded_rational_models': 1,
                         'maximum_dense_dimension': 4, 'best_achieved_fit_joint_TV': min(errors),
                         'scope': 'Achieved numerical errors on two specified joint laws only; no fitted lower bound, global optimum, all-protocol upper or noisy-detector experiment.'}
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
                        help='Replay without fitting; numerical tolerance 2e-11, versions informational')
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
