#!/usr/bin/env python3
"""Exact checks of the temporal and signed-control scope of three-state prediction.

Universal realization, positivity and compactness arguments are in the
hash-bound proofs. The checks use symbolic identities and exact small matrices,
without optimization, a parameter sweep, or simulated observations.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {'reports/switch_physical_core.json':
          '4b5da0f863c60f09dc656451528c97a1c768089a6d63074e1bfb31e2816c622b'}
PROOFS = {
    'docs/FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md': '126fbcb68b9d552d461134f0f56853592a0cf34e6b16fa06f253ffb110cb9365',
    'docs/FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md': 'b9cefb9caa480b7e60271de6e6093c24766d30c6b1a1832d8c8f1c91cdbdadc3',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zero(value):
    entries = value if isinstance(value, sp.MatrixBase) else [value]
    return all(sp.simplify(sp.cancel(x)) == 0 for x in entries)


def provenance():
    proofs, sources = {}, {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected, 'Frozen input report')
        report = json.loads(payload)
        require(report['status'] == 'PASS', 'Input certificate passed')
        for source, digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Frozen source remains unchanged')
            sources[source] = digest
        for name, digest in report['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                    'Frozen inherited proof')
            proofs[name] = digest
        for name, digest in report.get('input_report_sha256', {}).items():
            require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                    'Frozen inherited prerequisite')
    require(len(PROOFS) >= 2 and all(len(d) == 64 for d in PROOFS.values()),
            'Reviewed scope proofs have unconditional hashes')
    for name, digest in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'New derivation matches reviewed snapshot')
        proofs[name] = digest
    return sources, proofs


def load_core():
    spec = importlib.util.spec_from_file_location('physical_core', ROOT/'scripts/verify_switch_physical_core.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def passive(t, core):
    a, b = (1-t*t)/2, (1+t*t)/2
    c, d = 2*t*t/(1+t*t), (1-t*t)/(1+t*t)
    q = core.generator([[0, a, 0], [b, 0, c], [0, d, 0]])
    pi = sp.Matrix([[sp.Rational(1, 2), (1-t*t)/(2*(1+t*t)), t*t/(1+t*t)]])
    return q, pi, sp.Matrix([-1, 1, 1]), sp.Matrix([-t, -t, 1/t])


def signed(t, u, m, core, ratio=sp.Integer(1)):
    a, b = 2*t, (1-t*t)/(t*(1+u))
    width = a+b
    A = m*(1-t*t)/(1-t*t*m*m)
    B = t*(1-m*m)/(1-t*t*m*m)
    ell, q21 = (1+A-t*B)/2, (1-A+t*B)/2
    q31 = (1-A-B*(t+b))/2
    q = core.generator([[0, ell, 0], [q21, 0, ratio*a/width],
                        [q31, (ratio*b-q31*(2*t+b))/width, 0]])
    s, z = sp.Matrix([-1, 1, 1]), sp.Matrix([-t, -t, t+b])
    pi0 = sp.Matrix([[sp.Rational(1, 2), b/(2*width), a/(2*width)]])
    pi = sp.Matrix([[pi0[i]*(1+m*s[i]) for i in range(3)]])
    return q, pi, s, z


def symbolic_checks(core):
    t, u = sp.symbols('t u', positive=True)
    m = sp.symbols('m', real=True)
    q, pi, s, z = passive(t, core)
    one = sp.ones(3, 1)
    require(zero(q*one) and zero((pi*one)[0]-1), 'Passive generator and normalized law')
    require(zero(pi*q), 'Passive full stationarity')
    flux = sp.diag(*list(pi))*q
    require(zero(flux-flux.T), 'Passive birth-death detailed balance')
    require(zero(q*s-(-s+t*z)) and zero(q*z-(t*s-z)), 'Passive target moment closure')
    x = sp.symbols('x')
    require(zero(q.charpoly(x).as_expr()-x*(x+1-t)*(x+1+t)), 'Two nonzero passive decay rates')
    require(zero((pi*sp.diag(*list(s))*z)[0]-t), 'Passive initial conditional coordinate')
    ca, cb, cab, moment, d = sp.symbols('ca cb cab moment d', real=True)
    for middle in (-1, 1):
        table = sp.Matrix([[(1+ca*left*middle+cb*middle*right+cab*left*right+
                            moment*left*middle*right)/8 for right in (-1, 1)]
                           for left in (-1, 1)])
        require(zero(table.det()-(cab-ca*cb+middle*moment)/16),
                'Middle-sign slice determinant is the conditional covariance divided by sixteen')
        require(zero(table.det().subs({cab: ca*cb+d, moment: -middle*d})),
                'Singleton slice forces the stated triple moment when pairs match')
    aa, bb = sp.symbols('aa bb')
    require(zero(aa*aa+bb*bb+2*t*aa*bb-(aa+t*bb)**2-(1-t*t)*bb*bb),
            'Two passive pair times already exclude a two-state stationary fit')
    radius = (sp.sqrt(1+d/2)-1)/2
    require(zero(radius*(1+radius)/2-d/16), 'Unrestricted triple-TV lower-radius algebra')
    q, pi, s, z = signed(t, u, m, core)
    A, B = m*(1-t*t)/(1-t*t*m*m), t*(1-m*m)/(1-t*t*m*m)
    require(zero(q*one) and zero((pi*one)[0]-1), 'Signed construction normalization')
    require(zero(pi*q), 'Signed construction full stationary Gibbs law')
    require(zero(q*s-(A*one-s+B*z)) and zero(q*z-(t*s-z)),
            'Signed construction matches both target coordinate equations')
    require(zero((pi.subs(m, 0)*sp.diag(*list(s))*z)[0]-t),
            'Signed construction matches initial conditional coordinates')
    phi = 3*t*t*u*u+(1+t*t)*u
    require(zero(q[2, 0].subs(m, u)), 'High-field boundary rate is exactly zero')
    require(zero(q[2, 0].subs(m, -u)-u*(1-t*t)/(1-t*t*u*u)),
            'Negative endpoint gives the largest return rate')
    require(zero(q[2, 1].subs(m, -u)-
                 (1-t*t)*(1-phi)/((1+t*t+2*t*t*u)*(1-t*t*u*u))),
            'Remaining endpoint rate changes sign exactly at the criterion')
    quadratic = 1+t*t*m*m-2*t*z[2]*m
    require(zero(sp.diff(q[2, 0], m)+(1-t*t)*quadratic/(2*(1-t*t*m*m)**2)),
            'Rate derivative reduces to a positive quadratic')
    require(zero(quadratic.subs(m, u)-(1-u)*(1-t*t*u*u)/(1+u)),
            'Derivative quadratic is positive at its interval minimum')
    require(zero(quadratic-quadratic.subs(m, u)-
                 (u-m)*(2*t*z[2]-t*t*(u+m))) and
            zero(z[2]-t*u-(1-t*t*u*u)/(t*(1+u))),
            'The endpoint derivative bound extends over the full signed interval')
    b = sp.symbols('b', positive=True)
    q31_negative = ((1+u)*((1-t*t)-t*b*(1-u)))/(2*(1-t*t*u*u))
    feasibility = b/(2*t+b)-q31_negative
    require(zero(sp.diff(feasibility, b)-(2*t/(2*t+b)**2+
                                               t*(1-u*u)/(2*(1-t*t*u*u)))),
            'Feasibility increases with the triangle height, proving endpoint extremality')
    require(zero(phi.subs({t: sp.Rational(4, 5), u: sp.Rational(3, 5)})-
                 sp.Rational(1047, 625)), 'The previous operating point lies above the signed threshold')
    ratio = sp.symbols('ratio', positive=True)
    q4, pi4, s4, z4 = core.target(t, m)
    for i in range(4):
        for j in range(4):
            if i != j and s4[i] == s4[j]:
                q4[i, j] *= ratio
    q4 = core.generator(q4)
    require(zero(q4*s4-(A*sp.ones(4, 1)-s4+B*z4)) and
            zero(q4*z4-ratio*(t*s4-z4)), 'Independently rescaled physical rates have the unequal closure')
    flux4 = sp.diag(*list(pi4))*q4
    require(zero(pi4*q4) and zero(flux4-flux4.T), 'Physical unequal-rate target retains Gibbs detailed balance')
    qr, pir, sr, zr = signed(t, u, m, core, ratio)
    require(zero(qr*sr-(A*one-sr+B*zr)) and zero(qr*zr-ratio*(t*sr-zr)) and
            zero(pir*qr), 'Arbitrary positive attempt ratio retains closure and full stationary law')
    phi_r = (ratio+2)*t*t*u*u+(1+t*t)*u
    require(zero(qr[2, 1].subs(m, -u)-
                 (1-t*t)*(ratio-phi_r)/((1+t*t+2*t*t*u)*(1-t*t*u*u))),
            'Unequal-rate criterion is the exact endpoint positivity condition')
    M = sp.Matrix([[0, A, 0], [0, -1, ratio*t], [0, B, -ratio]])
    initial, output = sp.Matrix([[1, 0, 0]]), sp.Matrix([0, 1, 0])
    require(zero(sp.Matrix.hstack(output, M*output, M*M*output).det()-ratio*A*B) and
            zero(sp.Matrix.vstack(initial, initial*M, initial*M*M).det()-ratio*t*A*A),
            'Unequal-rate minimality has no exceptional positive ratio')
    require(zero(M.charpoly(x).as_expr()-x*(x*x+(1+ratio)*x+ratio*(1-t*B))),
            'Unequal-rate spectra have the stated positive discriminant')
    require(zero((ratio-phi_r).subs({t: sp.Rational(4, 5), u: sp.Rational(3, 5),
                                   ratio: sp.Rational(903, 481)})),
            'The selected signed task crosses its state boundary at ratio 903/481')
    return {'signed_criterion': '3*t^2*u^2+(1+t^2)*u <= 1',
            'unequal_rate_criterion': '(ratio+2)*t^2*u^2+(1+t^2)*u <= ratio',
            'domain': '0<t<1, 0<u<1, -u<=m<=u; continuous-time models, one common preparation',
            'triple_covariance': '(1-t^2)*exp(-a-b)*sinh(t*a)*sinh(t*b)',
            'triple_TV_lower': '(sqrt(1+D/2)-1)/2',
            'triple_TV_if_pairs_exact': 'D/2',
            'nominal_signed_expression': '1047/625 > 1',
            'scope': 'Universal positivity, transfer to arbitrary rivals, and positive-error existence are proved in the bound notes.'}


def spectral_kernel(q, t):
    # Exact e^(5 log(2) Q) at t=4/5, including the fourth target decay mode.
    values = [(0, sp.Integer(1)), (-1+t, sp.Rational(1, 2)),
              (-1-t, sp.Rational(1, 512))]
    if q.rows == 4:
        values.append((-sp.Integer(2), sp.Rational(1, 1024)))
    identity, result = sp.eye(q.rows), sp.zeros(q.rows)
    for eigenvalue, exponential in values:
        projector = identity
        for other, _ in values:
            if other != eigenvalue:
                projector = projector*(q-other*identity)/(eigenvalue-other)
        result += exponential*projector
    return sp.simplify(result)


def triple(pi, kernel, signs):
    out = {}
    labels = (-1, 1)
    projectors = {s: sp.diag(*[int(x == s) for x in signs]) for s in labels}
    for a in labels:
        for b in labels:
            for c in labels:
                out[(a, b, c)] = (pi*projectors[a]*kernel*projectors[b]*kernel*
                                   projectors[c]*sp.ones(kernel.rows, 1))[0]
    return out


def rational_fixtures(core):
    t = sp.Rational(4, 5)
    physical = core.target(t, sp.Integer(0))
    predictors = {'passive_reversible': passive(t, core),
                  'one_sided_stationary': core.predictor(t, sp.Integer(0))}
    q, pi, s, _ = physical
    k = spectral_kernel(q, t)
    target = triple(pi, k, s)
    D = sp.Rational(23409, 1048576)
    expected_pair = sp.Rational(461, 1024)
    require(sum(target.values()) == 1 and min(target.values()) > 0, 'Exact target triple law')
    require(sum(a*c*p for (a, b, c), p in target.items())-
            expected_pair**2 == D, 'Exact target non-Markov covariance at a=5 log(2)')
    records = []
    for name, (q, pi, s, _) in predictors.items():
        k = spectral_kernel(q, t)
        require(min(k) >= 0 and zero(k*sp.ones(3, 1)-sp.ones(3, 1)), 'Exact predictive kernel')
        law = triple(pi, k, s)
        for first, second in ((0, 1), (1, 2), (0, 2)):
            for a in (-1, 1):
                for b in (-1, 1):
                    target_pair = sum(p for labels, p in target.items() if labels[first] == a and labels[second] == b)
                    model_pair = sum(p for labels, p in law.items() if labels[first] == a and labels[second] == b)
                    require(target_pair == model_pair, 'All three pair marginals agree exactly')
        tv = sum(abs(law[labels]-p) for labels, p in target.items())/2
        require(tv == D/2, 'A pair-perfect three-state model attains the exact triple error')
        records.append({'model': name, 'triple_TV': str(tv)})
    signed_cases = []
    for tv, uv, label in [(sp.Rational(4, 5), sp.Rational(1, 3), 'inside'),
                          (sp.sqrt(sp.Rational(2, 5)), sp.Rational(1, 2), 'boundary'),
                          (sp.Rational(4, 5), sp.Rational(3, 5), 'outside')]:
        phi = sp.simplify(3*tv*tv*uv*uv+(1+tv*tv)*uv)
        for m in (-uv, sp.Integer(0), uv):
            q, pi, _, _ = signed(tv, uv, m, core)
            if label != 'outside':
                require(all(sp.simplify(q[i, j]) >= 0 for i in range(3) for j in range(3) if i != j),
                        'Feasible signed endpoint rates are nonnegative')
                require(all(sp.simplify(p) > 0 for p in pi) and zero(pi*q), 'Positive signed stationary fixture')
                reach = sp.eye(3)+q/10
                require(all(sp.simplify(v) > 0 for v in reach**2), 'Signed fixture remains irreducible at zero rates')
            elif m == -uv:
                require(q[2, 1] < 0, 'The extremal triangle fails beyond the threshold')
        signed_cases.append({'t': str(tv), 'u': str(uv), 'criterion_value': str(phi), 'region': label})
    unequal = []
    for ratio in (sp.Rational(1, 2), sp.Integer(1), sp.Rational(903, 481), sp.Integer(2)):
        uv = sp.Rational(3, 5)
        slack = ratio-((ratio+2)*t*t*uv*uv+(1+t*t)*uv)
        for m in (-uv, sp.Integer(0), uv):
            q, pi, s, z = signed(t, uv, m, core, ratio)
            if slack >= 0:
                require(all(q[i, j] >= 0 for i in range(3) for j in range(3) if i != j) and
                        all(p > 0 for p in pi) and zero(pi*q), 'Unequal-rate feasible construction')
            elif m == -uv:
                require(q[2, 1] < 0, 'Unequal-rate infeasible extremal triangle')
        unequal.append({'ratio': str(ratio), 'criterion_slack': str(slack)})
    return {'clock': 'a=b=5 log(2), t=4/5', 'target_D': str(D),
            'pair_correlation_a': str(expected_pair), 'triple_fits': records,
            'signed_fixtures': signed_cases, 'unequal_rate_fixtures': unequal,
            'outside_scope': 'The negative rate is a construction check; the bound proof, not this fixture, excludes every three-state rival.'}


def finite_menu():
    positive = {('H',)*n for n in range(1, 6)}
    zero = {('H',)*i+('0',)+('H',)*j for i in range(3) for j in range(3)}
    negative = {('H',)*i+('-H',)+('H',)*j for i in range(3) for j in range(3)}
    words = positive | zero | negative
    require(len(words) == 23 and max(map(len, words)) == 5, 'Full shifted-table menu has 23 words of at most five ticks')
    for i in range(3):
        for j in range(3):
            require(i+j == 0 or ('H',)*(i+j) in words, 'Every unshifted Hankel entry is supplied')
            for h in ('0', 'H', '-H'):
                require(('H',)*i+(h,)+('H',)*j in words, 'Every shifted Hankel entry is supplied')
    require(('0',) in words, 'Passive pair supplies the conditional-coordinate moment')
    return {'words': [list(w) for w in sorted(words, key=lambda w: (len(w), w))],
            'count': len(words), 'max_ticks': 5,
            'scope': 'One common arbitrary preparation across words; exact CTMC threshold and parameter-dependent positive-error existence. No per-word preparation freedom or optimized experiment count is claimed.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    require(args.output.resolve() != Path(__file__).resolve(), 'Do not overwrite verifier')
    sources, proofs = provenance()
    core = load_core()
    symbolic = symbolic_checks(core)
    fixtures = rational_fixtures(core)
    menu = finite_menu()
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report = {'status': 'PASS', 'checks': CHECKS, 'largest_matrix_dimension': 4,
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'arithmetic': 'Exact rational and algebraic matrices and symbolic identities; no floating point or search',
              'symbolic_certificate': symbolic, 'exact_fixtures': fixtures, 'finite_signed_menu': menu,
              'source_sha256': sources, 'proof_snapshot_sha256': proofs, 'input_report_sha256': INPUTS,
              'limitations': 'Mathematical checks do not establish sensor nondisturbance, a thermodynamic implementation, literature priority or PRL significance.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(f'PASS: {CHECKS} exact control-scope checks -> {args.output}')


if __name__ == '__main__':
    main()
