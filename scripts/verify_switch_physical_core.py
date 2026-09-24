#!/usr/bin/env python3
"""Exact algebra checks for the physical model and minimal four-word theorem.

Universal positivity and semigroup arguments live in the reviewed, hash-bound
proofs. Symbolic identities and rational counterexamples check their algebra;
there is no parameter fitting, simulated data, or floating-point arithmetic.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    'reports/switch_preparation_free.json': 'dc10d2baf22899ef663faa4406d720998771e7c40c4de7ef4e8a7b2a3bed3df1',
}
# Reviewed universal derivations; finite fixtures do not replace these proofs.
PROOFS = {
    'docs/FAMILIAR_SWITCH_MINIMAL_THEOREM.md': '4618b2f6882bbc0d4bfe7161b71d14c8c3f16fa0600dc9a3f0324417066b896c',
    'docs/FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md': '63e18ab4e4d059cab98cb687f8e5926452c86a5e3c1cceebe83ea7e9036336a4',
    'docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md': '9573c9a70ac82c319a49f09e7f7d72024c0f6816091a54a2aff6228fee871342',
}
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zero(expression):
    if isinstance(expression, sp.MatrixBase):
        return all(sp.cancel(x) == 0 for x in expression)
    return sp.cancel(expression) == 0


def generator(off_diagonal):
    result = sp.Matrix(off_diagonal)
    for i in range(result.rows):
        result[i, i] = -sum(result[i, j] for j in range(result.cols) if j != i)
    return result


def target(t, m):
    states = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    off = sp.zeros(4)
    for i, (s, z) in enumerate(states):
        off[i, states.index((-s, z))] = (1-s*(m+t*z)/(1+m*t*z))/2
        off[i, states.index((s, -z))] = (1-z*t*s)/2
    pi = sp.Matrix([[(1+t*s*z)*(1+m*s)/4 for s, z in states]])
    return generator(off), pi, sp.Matrix([s for s, z in states]), sp.Matrix([z for s, z in states])


def predictor(t, m):
    d, e = 3*t, (1-t*t)/(2*t)
    width = d+e
    a = m*(1-t*t)/(1-t*t*m*m)
    b = t*(1-m*m)/(1-t*t*m*m)
    ell = (1+a-b*t)/2
    q21, q31 = (1-a+2*b*t)/2, (1-a-b*(t+e))/2
    q = generator([[0, ell*(2*t+e)/width, ell*(d-2*t)/width],
                   [q21, 0, (d+q21*(2*t-d))/width],
                   [q31, (e-q31*(2*t+e))/width, 0]])
    s = sp.Matrix([-1, 1, 1])
    z = sp.Matrix([-t, -2*t, t+e])
    pi0 = sp.Matrix([[sp.Rational(1, 2), e/(2*width), d/(2*width)]])
    pi = sp.Matrix([[pi0[i]*(1+m*s[i]) for i in range(3)]])
    return q, pi, s, z


def inputs():
    inherited = {}
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == expected, 'Frozen prerequisite report')
        report = json.loads(payload)
        require(report['status'] == 'PASS', 'Prerequisite passed')
        for source, digest in report['source_sha256'].items():
            require(hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest,
                    'Frozen prerequisite source')
        for proof, digest in report['proof_snapshot_sha256'].items():
            require(hashlib.sha256((ROOT/proof).read_bytes()).hexdigest() == digest,
                    'Frozen inherited proof')
            inherited[proof] = digest
        for source, digest in report.get('input_report_sha256', {}).items():
            require(hashlib.sha256((ROOT/source).read_bytes()).hexdigest() == digest,
                    'Frozen inherited input report')
    require(len(PROOFS) == 3 and all(len(x) == 64 for x in PROOFS.values()),
            'Three unconditional reviewed proof hashes are present')
    for name, digest in PROOFS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest,
                'New proof matches its reviewed snapshot')
    return {**inherited, **PROOFS}


def symbolic_core():
    t, m = sp.symbols('t m', positive=True)
    q4, pi4, s4, z4 = target(t, m)
    q3, pi3, s3, z3 = predictor(t, m)
    a = m*(1-t*t)/(1-t*t*m*m)
    b = t*(1-m*m)/(1-t*t*m*m)
    for q, pi, s, z in [(q4, pi4, s4, z4), (q3, pi3, s3, z3)]:
        one = sp.ones(q.rows, 1)
        require(zero(q*one), 'Generator rows sum to zero')
        require(zero((pi*one)[0]-1), 'Tilted law is normalized')
        require(zero(pi*q), 'Full tilted stationarity')
        require(zero(q*s-(a*one-s+b*z)), 'Independent first-coordinate closure')
        require(zero(q*z-(t*s-z)), 'Independent second-coordinate closure')
        pi0 = pi.subs(m, 0)
        for sign in (-1, 1):
            conditional = sp.Matrix([[2*pi0[i] if s[i] == sign else 0 for i in range(q.rows)]])
            require(zero((conditional*one)[0]-1), 'Each equilibrium sign has mass one half')
            require(zero((conditional*s)[0]-sign) and zero((conditional*z)[0]-t*sign),
                    'Initial conditional coordinate means agree in both realizations')
    require(zero(sp.diag(*list(pi4))*q4-(sp.diag(*list(pi4))*q4).T),
            'Physical target satisfies detailed balance symbolically')
    require(zero(sp.Matrix.hstack(sp.ones(3, 1), s3, z3).det()-(1+5*t*t)/t),
            'Three predictor coordinates have a strictly positive determinant')
    require(zero(q3[2, 0]-(1-t*t)*(1-m)**2/(4*(1-t*t*m*m))),
            'Delicate positive rate has the stated factorization')
    e = (1-t*t)/(2*t)
    require(zero(e-(1-t*t)*(2*t+e)/4-3*(1-t*t)**2/(8*t)),
            'Positive lower bound for the remaining delicate rate')
    # Independent equilibrium covariance calculation for both visible sectors.
    c, gs, gz, fs, fz = sp.symbols('c gs gz fs fz')
    for sign in (-1, 1):
        prob = lambda z: (1+sign*t*z)/2
        g = lambda z: gs*sign+gz*z
        f = lambda z: c+fs*sign+fz*z
        mean_g = sum(prob(z)*g(z) for z in (-1, 1))
        mean_f = sum(prob(z)*f(z) for z in (-1, 1))
        cov = sum(prob(z)*g(z)*f(z) for z in (-1, 1))-mean_g*mean_f
        require(zero(cov-gz*fz*(1-t*t)), 'Sector covariance has the positive product form')
    u, gap = sp.symbols('u gap', positive=True)
    lip = 2+4*u
    radius = gap/(2*(lip+gap))
    require(zero(lip*radius/(sp.Rational(1, 2)-radius)-gap),
            'Open TV radius meets the residual gap exactly at its excluded endpoint')
    current = sp.factor(pi3[0]*q3[0, 1]-pi3[1]*q3[1, 0])
    require(zero(current.subs(m, 0)-t*t*(1-t*t)/(4*(1+5*t*t))),
            'The predictor already has a strictly positive stationary current at zero field')
    # Check positivity and currents at exact rational points, not a search.
    fixtures = []
    for tv, mv in [(sp.Rational(1, 5), sp.Rational(1, 3)),
                   (sp.Rational(1, 2), sp.Rational(1, 2)),
                   (sp.Rational(4, 5), sp.Rational(3, 5))]:
        q, pi, s, z = predictor(tv, mv)
        require(all(q[i, j] > 0 for i in range(3) for j in range(3) if i != j),
                'Rational predictor fixture has positive rates')
        current = sp.factor(pi[0]*q[0, 1]-pi[1]*q[1, 0])
        qlow, plow, _, _ = predictor(tv, sp.Integer(0))
        current_low = sp.factor(plow[0]*qlow[0, 1]-plow[1]*qlow[1, 0])
        require(current_low > 0, 'Fixture has stationary circulation at zero field')
        fixtures.append({'t': str(tv), 'u': str(mv),
                         'edge_1_2_current_high': str(current),
                         'edge_1_2_current_low': str(current_low)})
    # The Ising representation is a direct substitution in the charge energy.
    j, h, s, z = sp.symbols('j h s z')
    n1, n2 = (1+s)/2, (1-z)/2
    charge_energy = 4*j*n1*n2+(-2*j-2*h)*n1-2*j*n2
    require(zero(charge_energy-(-j*s*z-h*s-j-h)), 'Charge-to-switch energy substitution')
    cap, c1, c2, cg1, cg2, electron = sp.symbols('C c1 c2 Cg1 Cg2 electron', positive=True)
    determinant = c1*c2-cap*cap
    lever = -electron/determinant*sp.Matrix([[c2*cg1, cap*cg2], [cap*cg1, c1*cg2]])
    require(zero(lever.det()-electron**2*cg1*cg2/determinant),
            'Published two-gate capacitance map is invertible in its positive-capacitance domain')
    compensated = lever*sp.Matrix([1, -cap*cg1/(c1*cg2)])
    require(zero(compensated-sp.Matrix([-electron*cg1/c1, 0])),
            'Compensated plunger displacement changes only the selected addition energy')
    return {'symbolic_domain': '0<t<1, 0<=m<1; positive pulse durations in the proof',
            'pair_upper_scope': 'Every finite nonnegative-field word from equilibrium, with one initial and one final label',
            'four_word_lower_scope': 'Every finite J,H,tau0,tauH>0, arbitrary per-word rival preparation',
            'gap_formula': 'g=(u/2)*exp(-tau0)*sinh(t*tau0)*exp(-tauH)*(B/kappa)*sinh(kappa*tauH)*(1-t^2)',
            'TV_radius_open': 'g/[2*(2+4*u+g)]',
            'rational_current_fixtures': fixtures,
            'limitation': 'Symbolic closure and initial moments support the proof of endpoint-pair equality, not multitime path equality. Universal positivity and semigroup arguments are in the bound proof.'}


def reduction_checks():
    t, u = sp.Rational(4, 5), sp.Rational(3, 5)
    q0, p0, s, _ = target(t, sp.Integer(0))
    qh, ph, _, _ = target(t, u)
    signs = sp.Matrix([-1, 1, 1])
    encoders = {
        'partition': sp.Matrix([[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        'stochastic': sp.Matrix([[1, 0, 0], [1, 0, 0],
                                [0, sp.Rational(3, 4), sp.Rational(1, 4)],
                                [0, sp.Rational(1, 3), sp.Rational(2, 3)]])}
    records = []
    for name, enc in encoders.items():
        low, high = p0*enc, ph*enc
        bayes = sp.diag(*[1/x for x in low])*enc.T*sp.diag(*list(p0))
        bayes_h = sp.diag(*[1/x for x in high])*enc.T*sp.diag(*list(ph))
        tilt = sp.Matrix([[low[i]*(1+u*signs[i]) for i in range(3)]])
        require(zero(enc*sp.ones(3, 1)-sp.ones(4, 1)) and zero(enc*signs-s),
                'Encoder is stochastic and exactly retains the measured sign')
        require(zero(high-tilt) and zero(bayes_h-bayes),
                'Coarse Gibbs tilt and conditional equilibrium are inherited')
        for q, law in [(q0, low), (qh, high)]:
            kernel = sp.eye(4)+q/2
            reduced = bayes*kernel*enc
            require(all(x >= 0 for x in reduced) and zero(reduced*sp.ones(3, 1)-sp.ones(3, 1)),
                    'Equilibrium coarse kernel is stochastic')
            require(zero(law*reduced-law) and
                    zero(sp.diag(*list(law))*reduced-(sp.diag(*list(law))*reduced).T),
                    'Equilibrium coarse kernel is stationary and reversible')
        if name == 'partition':
            reduced_q = bayes*q0*enc
            require(zero(bayes*enc-sp.eye(3)) and
                    all(reduced_q[i, j] >= 0 for i in range(3) for j in range(3) if i != j),
                    'Partition flux construction is a valid generator')
            require(not zero(q0*enc-enc*reduced_q),
                    'Equilibrium preservation does not imply exact lumpability of this target')
        weights = sp.Matrix([1, sp.Rational(1001, 1000), 1, sp.Rational(1001, 1000)])
        coarse_weights = bayes*weights
        biased = sp.Matrix([[ph[i]*weights[i] for i in range(4)]])
        biased /= (biased*sp.ones(4, 1))[0]
        predicted = sp.Matrix([[low[i]*(1+u*signs[i])*coarse_weights[i] for i in range(3)]])
        predicted /= (predicted*sp.ones(3, 1))[0]
        require(zero(biased*enc-predicted) and
                min(coarse_weights) >= min(weights) and max(coarse_weights) <= max(weights),
                'Conditional averaging inherits the microscopic relative-force envelope')
        records.append({'encoder': name, 'coarse_low_law': list(map(str, low)),
                        'coarse_residual_weights': list(map(str, coarse_weights))})
    # Necessary hypotheses cannot be dropped from the inheritance statement.
    bad = sp.ones(4, 3)/3
    bad_low, bad_high = p0*bad, ph*bad
    bad_tilt = sp.Matrix([[bad_low[i]*(1+u*signs[i]) for i in range(3)]])
    bad_tilt /= (bad_tilt*sp.ones(3, 1))[0]
    require(not zero(bad*signs-s) and not zero(bad_high-bad_tilt),
            'Losing the measured sign can destroy the shared binary force rule')
    require(not zero(ph*encoders['stochastic']-ph*encoders['partition']),
            'A field-dependent sign-compatible encoder need not preserve the fixed-coordinate tilt')
    uniform = sp.ones(1, 4)/4
    reset = sp.ones(4, 1)*uniform-sp.eye(4)
    soft = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                      [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                      [0, 0, 1], [0, 0, 1]])
    coarse = uniform*soft
    reverse = sp.diag(*[1/x for x in coarse])*soft.T*sp.diag(*list(uniform))
    require(zero(soft*sp.Matrix([-1, -1, 1])-s) and
            (reverse*reset*soft)[0, 1] == -sp.Rational(1, 4),
            'Stochastic readout-compatible encoding can make BQC fail generator positivity')
    return {'fixtures': records,
            'scope': 'Standard equilibrium inheritance and reversible flux projections; projected trajectories need not be Markov. These identities motivate the rival interface but do not make the circulating predictor a physical coarse-graining.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    require(args.output.resolve() != Path(__file__).resolve(), 'Do not overwrite verifier source')
    proofs = inputs()
    core = symbolic_core()
    reductions = reduction_checks()
    report = {'status': 'PASS', 'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'arithmetic': 'Exact symbolic rational functions and rational matrices; no floating point or search',
              'minimal_theorem_certificate': core, 'equilibrium_reduction_certificate': reductions,
              'checks': CHECKS, 'largest_matrix_dimension': 4,
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'input_report_sha256': INPUTS, 'proof_snapshot_sha256': proofs,
              'scope': 'Finite and symbolic checks accompany reviewed universal derivations. They do not establish literature priority, physical detector performance, or PRL significance.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(f'PASS: {CHECKS} physical-core algebra and provenance checks -> {args.output}')


if __name__ == '__main__':
    main()
