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
    for name in ('checkpoint','finite_accuracy'):
        report = json.loads((ROOT/f'reports/{name}.json').read_text())
        require(report['status']=='PASS',f'Saved report is not PASS: {name}')
    report = json.loads((ROOT/'reports/finite_accuracy.json').read_text())
    for name,digest in report['source_sha256'].items():
        require(hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()==digest,
                f'Saved extension report is stale for {name}; rerun its verifier into reports/')
    print(f'PASS: {count} local Markdown links, {len(scripts)} Python syntax checks, '
          'saved report provenance, and unchanged MIT license')


if __name__ == '__main__':
    main()
