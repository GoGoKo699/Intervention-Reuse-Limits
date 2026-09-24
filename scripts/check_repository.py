#!/usr/bin/env python3
"""Offline checks of local documentation links, report provenance, and license."""
from pathlib import Path
import ast
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LICENSE_SHA = 'a92600540b1ab7a18301e2632a29334b3df227ad836e88df9967d69e3c86db66'
CHECKPOINT_SHA = 'ce7a2a981e6a09f7350ad42731afbcafd6c67f2de2bade8d2de16666227e2026'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256((ROOT/'LICENSE').read_bytes()).hexdigest() == LICENSE_SHA,
            'The owner-provided MIT license changed')
    require(hashlib.sha256((ROOT/'scripts/verify_checkpoint.py').read_bytes()).hexdigest() == CHECKPOINT_SHA,
            'The preserved checkpoint verifier changed; review provenance before updating this check')
    count = 0
    for path in ROOT.rglob('*.md'):
        if any(part in {'.venv','.git','.check-output'} for part in path.parts):
            continue
        text = path.read_text(encoding='utf-8')
        require(sum(line.strip().startswith('```') for line in text.splitlines()) % 2 == 0,
                f'Unbalanced code fences: {path.relative_to(ROOT)}')
        require(sum(line.strip() == '$$' for line in text.splitlines()) % 2 == 0,
                f'Unbalanced display math: {path.relative_to(ROOT)}')
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        prose = re.sub(r'\$\$.*?\$\$', '', prose, flags=re.S)
        prose = re.sub(r'(?<!\\)\$(?!\$).*?(?<!\\)\$', '', prose, flags=re.S)
        prose = re.sub(r'`[^`]*`', '', prose)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose):
            target = target.split()[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent/unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(ROOT),f'Link escapes repository: {target}')
            require(resolved.exists(),f'Broken local link in {path.name}: {target}')
            count += 1
    scripts = list((ROOT/'scripts').glob('*.py'))
    for script in scripts:
        ast.parse(script.read_text(encoding='utf-8'),filename=str(script))
    for name in ('checkpoint','finite_accuracy','quadrature','minimal_realization','response_lower_bounds','unrestricted_rate_lower_bound','finite_field','path_information','actuator_hierarchy','general_compression','reversible_compression','general_controlled_lower_bound','bounded_rate_prediction','shift_register_lower_bound','polynomial_controlled_lower_bound','constant_step_compression','bounded_density_sampling','analytic_constant_step','moment_density_sampling','sparse_reversible_compression','local_walk_lower_bound','expander_scenery_compression','expander_scenery_lower_bound','aggregation_state_lower_bound','register_scenery_compression','soft_aggregation_lower_bound','exact_reversible_prefix_obstruction','dynamic_lamp_reversibility_lower_bound','binary_reversibility_lower_bound','state_speed_boundary','uncapped_observability','binary_uncapped_observability','fixed_clock_observability','prl_exploration','kinetic_parity','finite_advantage','physical_robustness','finite_minimality','rational_observation','symmetric_compression','simple_prediction_principles','familiar_switches','familiar_switch_screen','familiar_switch_margin','short_switch_witness_screen','switch_calibration','switch_preparation_witness','switch_preparation_screen'):
        report = json.loads((ROOT/f'reports/{name}.json').read_text())
        require(report['status']=='PASS',f'Saved report is not PASS: {name}')
    for report_name in ('finite_accuracy','quadrature','minimal_realization','response_lower_bounds','unrestricted_rate_lower_bound','finite_field','path_information','actuator_hierarchy','general_compression','reversible_compression','general_controlled_lower_bound','bounded_rate_prediction','shift_register_lower_bound','polynomial_controlled_lower_bound','constant_step_compression','bounded_density_sampling','analytic_constant_step','moment_density_sampling','sparse_reversible_compression','local_walk_lower_bound','expander_scenery_compression','expander_scenery_lower_bound','aggregation_state_lower_bound','register_scenery_compression','soft_aggregation_lower_bound','exact_reversible_prefix_obstruction','dynamic_lamp_reversibility_lower_bound','binary_reversibility_lower_bound','state_speed_boundary','uncapped_observability','binary_uncapped_observability','fixed_clock_observability','prl_exploration','kinetic_parity','finite_advantage','physical_robustness','finite_minimality','rational_observation','symmetric_compression','simple_prediction_principles','familiar_switches','familiar_switch_screen','familiar_switch_margin','short_switch_witness_screen','switch_calibration','switch_preparation_witness','switch_preparation_screen'):
        report = json.loads((ROOT/f'reports/{report_name}.json').read_text())
        for name,digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()==digest,
                    f'Saved {report_name} report is stale for {name}; rerun its verifier into reports/')
        for name,digest in report.get('proof_snapshot_sha256',{}).items():
            path = (ROOT/name).resolve()
            require(path.is_relative_to(ROOT),f'Proof snapshot escapes repository: {name}')
            require(hashlib.sha256(path.read_bytes()).hexdigest()==digest,
                    f'Saved {report_name} proof snapshot is stale for {name}; review and rerun its verifier')
        for name,digest in report.get('input_report_sha256',{}).items():
            path = (ROOT/name).resolve()
            require(path.is_relative_to(ROOT),f'Input report escapes repository: {name}')
            require(hashlib.sha256(path.read_bytes()).hexdigest()==digest,
                    f'Saved {report_name} input report is stale for {name}; review and rerun its verifier')
    print(f'PASS: {count} local Markdown links, {len(scripts)} Python syntax checks, '
          'saved report provenance, and unchanged MIT license')


if __name__ == '__main__':
    main()
