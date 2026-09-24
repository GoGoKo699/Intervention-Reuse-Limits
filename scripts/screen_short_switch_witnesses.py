#!/usr/bin/env python3
"""Replay four bounded short-witness screens; optional fixed-budget refitting.

Default and --verify-saved execution never optimize. These saved ordinary
three-state models give achievable numerical errors on their stated menus,
not lower bounds or global optima. The rational candidate's feasibility is
checked exactly; rigorous exponential enclosures belong to the exact verifier.
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

# This frozen helper sets numerical-library thread counts before importing them.
import screen_familiar_switches as core
import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT/'reports/short_switch_witness_screen.json'
PROOF_NAMES = ['FAMILIAR_SWITCH_STRUCTURE.md', 'FAMILIAR_SWITCH_FINITE_MARGIN.md']
ELEVEN = ['1', '11', '111', '1111', '11111', '10', '101', '1011', '110', '1101', '11011']
SEVEN = ['1', '11', '111', '10', '101', '110', '1101']


def protocol_menu(words, clock):
    return [[[int(letter), clock] for letter in word] for word in words]


def rational_feasibility(comparator, panel):
    """Exact checks for the denominator-million, log(3), clock-two candidate."""
    certificate = comparator['rational_parameters']
    denominator = certificate['denominator']
    split = Fraction(certificate['split_numerator'], denominator)
    fluxes = [[Fraction(x, denominator) for x in row]
              for row in certificate['flux_numerators_by_field']]
    assert abs(panel['fields'][1]-math.log(3)) < 1e-14
    assert panel['clock'] == 2 and panel['words'] == SEVEN
    assert comparator['model']['singleton_sign'] == -1
    assert comparator['model']['split_mass'] == float(split)
    assert comparator['model']['conductances_by_field'] == [[float(x) for x in row] for row in fluxes]
    laws = [[Fraction(1, 2), split, Fraction(1, 2)-split],
            [Fraction(1, 10), Fraction(9, 5)*split, Fraction(9, 5)*(Fraction(1, 2)-split)]]
    matrices = []
    for law, edges in zip(laws, fluxes):
        q = [[Fraction(0) for _ in range(3)] for _ in range(3)]
        for (i, j), flux in zip([(0, 1), (0, 2), (1, 2)], edges):
            q[i][j], q[j][i] = flux/law[i], flux/law[j]
        for i in range(3):
            q[i][i] = -sum(q[i])
        assert min(law) > 0 and sum(law) == 1
        assert all(q[i][j] > 0 for i in range(3) for j in range(3) if i != j)
        assert all(-q[i][i] < 3 for i in range(3))
        assert all(sum(law[i]*q[i][j] for i in range(3)) == 0 for j in range(3))
        assert all(law[i]*q[i][j] == law[j]*q[j][i] for i in range(3) for j in range(3))
        matrices.append(q)
    return {'stationary_laws': [[str(x) for x in law] for law in laws],
            'generators': [[[str(x) for x in row] for row in q] for q in matrices],
            'maximum_exit': str(max(-q[i][i] for q in matrices for i in range(3))),
            'scope': 'Exact feasibility only; floating response replay is not an interval certificate.'}


def response_record(predicted, target):
    error = predicted-target
    assert np.min(predicted) >= -1e-12 and np.max(predicted) <= 1+1e-12
    return {'occupations': [core.number(x) for x in predicted],
            'occupation_errors': [core.number(x) for x in error],
            'maximum_occupation_error': core.number(np.max(np.abs(error)))}


def replay(saved):
    result = copy.deepcopy(saved)
    fitted_count = rounded_count = 0
    best = {}
    for panel in result['panels']:
        assert panel['words'] in (SEVEN, ELEVEN)
        assert panel['clock'] > 0 and panel['fields'][0] == 0 and panel['fields'][1] > 0
        assert panel['target']['kind'] == 'ising' and panel['target']['alphas'] == [1., 1.]
        assert len(panel['target']['couplings']) == 1
        menu = protocol_menu(panel['words'], panel['clock'])
        eleven = protocol_menu(ELEVEN, panel['clock'])
        assert panel['menu'] == menu
        fields = panel['fields']
        target = core.responses(panel['target'], fields, menu)
        target_eleven = core.responses(panel['target'], fields, eleven)
        panel['target_diagnostics'] = core.model_diagnostics(panel['target'], fields)
        panel['target_occupations'] = [core.number(x) for x in target]
        panel['eleven_target_occupations'] = [core.number(x) for x in target_eleven]
        fitted_errors = []
        for comparator in panel['comparators']:
            definition = comparator['model']
            assert definition['kind'] == 'reversible_three_state'
            comparator['diagnostics'] = core.model_diagnostics(definition, fields)
            comparator['fit_menu_replay'] = response_record(core.responses(definition, fields, menu), target)
            comparator['eleven_menu_replay_without_refit'] = response_record(
                core.responses(definition, fields, eleven), target_eleven)
            if comparator['role'] == 'rounded_rational_upper':
                comparator['exact_feasibility'] = rational_feasibility(comparator, panel)
                rounded_count += 1
            else:
                assert comparator['role'] == 'bounded_local_fit'
                fitted_count += 1
                fitted_errors.append(comparator['fit_menu_replay']['maximum_occupation_error'])
        assert len(fitted_errors) == 2
        best[panel['name']] = min(fitted_errors)
        panel['best_achieved_fit_menu_occupation_error'] = min(fitted_errors)
        triangle = {'kind': 'exact_stationary_triangle', 'J': panel['target']['couplings'][0]}
        triangle_values = core.responses(triangle, fields, eleven)
        panel['exact_general_triangle_diagnostic'] = {
            'model': triangle, 'diagnostics': core.model_diagnostics(triangle, fields),
            'eleven_menu_replay': response_record(triangle_values, target_eleven)}
        assert np.max(np.abs(triangle_values-target_eleven)) < 3e-12
    assert len(result['panels']) == 4 and fitted_count == 8 and rounded_count == 1
    result['summary'] = {'target_panels': 4, 'retained_fitted_models': fitted_count,
                         'rounded_rational_models': rounded_count, 'maximum_dense_dimension': 4,
                         'best_achieved_fit_menu_occupation_errors': best,
                         'scope': 'Finite-menu achieved numerical upper diagnostics only; no optimization lower bound, all-protocol upper, or global optimum is claimed.'}
    result['versions'] = {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}
    result['source_sha256'] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in (Path(__file__), Path(core.__file__))}
    result['proof_snapshot_sha256'] = {str(Path('docs')/name): hashlib.sha256((ROOT/'docs'/name).read_bytes()).hexdigest()
                                        for name in PROOF_NAMES}
    result['status'] = 'PASS'
    return result


def refit(saved):
    """Optional fixed budget; retained rounded model is never optimized."""
    import resource
    consumed = resource.getrusage(resource.RUSAGE_SELF)
    cpu_limit = math.ceil(consumed.ru_utime+consumed.ru_stime)+120
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit))
    result = copy.deepcopy(saved)
    started = time.perf_counter()
    for panel in result['panels']:
        for comparator in panel['comparators']:
            if comparator['role'] != 'bounded_local_fit':
                continue
            if time.perf_counter()-started > 120:
                raise RuntimeError('Fixed refit budget reached; no report written')
            definition, diagnostic = core.refit_three(panel, comparator['model']['singleton_sign'])
            comparator['model'], comparator['fit_diagnostics'] = definition, diagnostic
            comparator['fit_versions'] = {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}
    result['optional_refit_runtime_seconds'] = core.number(time.perf_counter()-started)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--models', type=Path, default=DEFAULT_REPORT)
    parser.add_argument('--verify-saved', nargs='?', const=DEFAULT_REPORT, type=Path,
                        help='Replay saved feasible models; no optimization; absolute numeric comparison tolerance2e-11')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--refit', action='store_true', help='Optional eight fixed-budget fits; never required for verification')
    args = parser.parse_args()
    if args.refit and args.verify_saved is not None:
        parser.error('--refit and --verify-saved are mutually exclusive')
    saved = json.loads((args.verify_saved or args.models).read_text())
    result = replay(refit(saved) if args.refit else saved)
    if args.verify_saved is not None:
        core.compare_saved(saved, result)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': 'PASS', 'mode': 'bounded_refit' if args.refit else 'saved_model_replay',
                      **result['summary']}, sort_keys=True))


if __name__ == '__main__':
    main()
