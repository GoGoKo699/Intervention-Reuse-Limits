#!/usr/bin/env python3
"""Exact small checks of bounded-rate finite-alphabet mean prediction.

Rational word laws, generator identities, symbolic clock integrals and exact
integer error budgets are checked. No trajectories are simulated. The
uniform protocol/horizon statements and general state bounds remain proved
by the analytic coupling argument in docs/BOUNDED_RATE_FINITE_FIELD.md.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as sp

import verify_reversible_compression as reused


require = reused.require
Rational = sp.Rational


def irreducible(P: sp.Matrix) -> bool:
    def reached(matrix):
        seen, queue = {0}, [0]
        for i in queue:
            for j in range(matrix.rows):
                if matrix[i, j] > 0 and j not in seen:
                    seen.add(j)
                    queue.append(j)
        return len(seen) == matrix.rows

    return reached(P) and reached(P.T)


def histogram(mu: sp.Matrix, labels: list[int]) -> dict[int, sp.Expr]:
    return {a: sum(mu[i] for i, value in enumerate(labels) if value == a)
            for a in sorted(set(labels))}


def models() -> tuple[list[dict], dict]:
    factors = [reused.bit_transition(Rational(1, 2)),
               reused.bit_transition(Rational(1, 3)),
               reused.bit_transition(Rational(1, 4))]
    P = sp.kronecker_product(*factors)
    mu = sp.ones(1, 8)/8
    labels = [-1, -1, -1, 1, -1, 1, 1, 1]
    # Majority-symbol observation of three different bit chains is not lumpable.
    opposite = [i for i, value in enumerate(labels) if value == 1]
    witness = (sum(P[0, j] for j in opposite),
               sum(P[1, j] for j in opposite))
    require(labels[0] == labels[1] and witness[0] != witness[1],
            'The binary target is not lumpable by its sensitivity levels')
    path_K = sp.Matrix([[-1, 1, 0], [1, -2, 1], [0, 1, -1]])
    examples = [
        {'name': 'nonlumpable_binary', 'P': P, 'mu': mu, 'labels': labels,
         'clock': sp.Integer(3), 'word_lengths': (1, 2, 3)},
        {'name': 'sparse_ternary', 'P': sp.eye(3)+path_K/3,
         'mu': sp.ones(1, 3)/3, 'labels': [-1, 0, 1],
         'clock': sp.Integer(3), 'word_lengths': (2,)},
    ]
    records = []
    for model in examples:
        matrix, law, cap = model['P'], model['mu'], model['clock']
        K = cap*(matrix-sp.eye(matrix.rows))
        spectrum = sorted((-K).eigenvals())
        require(K == K.T and law*K == sp.zeros(1, matrix.rows),
                'Exact reversible stationary internal generator')
        require(K*sp.ones(matrix.rows, 1) == sp.zeros(matrix.rows, 1),
                'Exact generator row sums')
        require(all(K[i, j] >= 0 for i in range(K.rows)
                    for j in range(K.cols) if i != j), 'Positive internal rates')
        require(all(0 <= value <= cap for value in spectrum), 'Exact spectral cap')
        require(all(value == 0 or value >= 1 for value in spectrum),
                'Examples also have a lower spectral gap of one')
        require(matrix == sp.eye(K.rows)+K/cap, 'Exact uniformization identity')
        require(matrix*sp.ones(matrix.rows, 1) == sp.ones(matrix.rows, 1),
                'Uniformization matrix is stochastic')
        require(all(matrix[i, i] >= law[i] > 0 for i in range(matrix.rows)),
                'Spectral-cap diagonal bound P_ii >= mu_i')
        require(irreducible(matrix), 'Irreducible update chain')
        require(all(-K[i, i] <= cap*(1-law[i]) for i in range(K.rows)),
                'Stronger exit-rate bound from the centered coordinate vector')
        records.append({'name': model['name'], 'hidden_states': matrix.rows,
                        'relaxation_spectrum_exact': [str(v) for v in spectrum],
                        'clock_rate_exact': str(cap),
                        'minimum_diagonal_margin_Pii_minus_mui_exact':
                            str(min(matrix[i, i]-law[i] for i in range(matrix.rows))),
                        'histogram_exact': {str(a): str(p) for a, p in
                                            histogram(law, model['labels']).items()}})
    return examples, {'models': records,
                      'binary_nonlumpability_exit_probabilities_exact':
                          [str(value) for value in witness]}


def physical_identities(P: sp.Matrix, mu: sp.Matrix,
                        labels: list[int], clock: sp.Expr,
                        reversible: bool) -> int:
    y = sp.symbols('y', positive=True)  # y=exp(h), with k=1.
    n = P.rows
    Q = sp.zeros(n+1)
    Q[1:, 1:] = clock*(P-sp.eye(n))
    for j, value in enumerate(labels):
        Q[0, j+1] = mu[j]*y**(1+value)
        Q[j+1, 0] = y**(value-1)
        Q[j+1, j+1] -= Q[j+1, 0]
    Q[0, 0] = -sum(Q[0, j] for j in range(1, n+1))
    pi = sp.Matrix([[1]+[y*y*value for value in mu]])/(1+y*y)
    require((Q*sp.ones(n+1, 1)).applyfunc(sp.cancel) == sp.zeros(n+1, 1),
            'Exact physical generator row sums')
    require((pi*Q).applyfunc(sp.cancel) == sp.zeros(1, n+1),
            'Exact stationary full-field law even for a nonreversible word chain')
    readout = sp.Matrix([-1]+[1]*n)
    require(sp.cancel((pi*readout)[0]-(y*y-1)/(y*y+1)) == 0,
            'Exact equilibrium mean tanh(h)')
    visible_lift = sp.zeros(n+1, 2)
    visible_lift[0, 0] = 1
    for j in range(1, n+1):
        visible_lift[j, 1] = 1
    telegraph = sp.Matrix([[-1, 1], [1, -1]])
    require(Q.subs(y, 1)*visible_lift == visible_lift*telegraph,
            'Exact passive strong lumpability, not only an autocorrelation check')
    flux = (sp.diag(*pi)*Q-Q.T*sp.diag(*pi)).applyfunc(sp.cancel)
    require((flux == sp.zeros(n+1)) == reversible,
            'Full-field reversibility status agrees with the internal model')
    return n+1


def word_lifts(examples: list[dict]) -> dict:
    records, largest, block_count = [], 0, 0
    for model in examples:
        P, mu, labels = model['P'], model['mu'], model['labels']
        alphabet = tuple(sorted(set(labels)))
        for ell in model['word_lengths']:
            probabilities = {w: reused.word_probability(P, mu, labels, w)
                             for w in itertools.product(alphabet, repeat=ell)}
            words = [w for w, probability in probabilities.items() if probability > 0]
            index = {w: i for i, w in enumerate(words)}
            law = sp.Matrix([[probabilities[w] for w in words]])
            transition = sp.zeros(len(words))
            for i, w in enumerate(words):
                for a in alphabet:
                    joint = reused.word_probability(P, mu, labels, w+(a,))
                    if joint:
                        successor = w[1:]+(a,)
                        require(successor in index, 'Positive transitions lead to allowed words')
                        transition[i, index[successor]] = joint/law[i]
            gamma = [w[-1] for w in words]
            require(transition*sp.ones(len(words), 1) == sp.ones(len(words), 1),
                    'Word transition row sums')
            require(law*transition == law and sum(law) == 1,
                    'Exact stationary word law')
            require(irreducible(transition), 'Allowed-word graph is irreducible')
            require(histogram(law, gamma) == histogram(mu, labels),
                    'Entire stationary actuator histogram is preserved exactly')
            require(reused.scalar_moment(law, sp.Matrix(gamma), 1) == 0,
                    'Exact centered word actuator')
            require(reused.scalar_moment(law, sp.Matrix(gamma), 2)
                    == reused.scalar_moment(mu, sp.Matrix(labels), 2),
                    'Exact original variance W')
            count = 0
            for length in range(1, ell+2):
                for w in itertools.product(alphabet, repeat=length):
                    original = reused.word_probability(P, mu, labels, w)
                    lifted = reused.word_probability(transition, law, gamma, w)
                    require(original == lifted, 'Exact stationary prefix through ell+1 symbols')
                    for tilt in (Rational(2, 3), Rational(3, 2)):
                        normalizer = sum(mu[j]*tilt**labels[j] for j in range(P.rows))
                        lifted_normalizer = sum(law[j]*tilt**gamma[j]
                                                for j in range(transition.rows))
                        require(normalizer == lifted_normalizer,
                                'Entry-tilt normalization is exactly shared')
                        require(original*tilt**w[0]/normalizer
                                == lifted*tilt**w[0]/lifted_normalizer,
                                'Exact first-symbol-tilted entry prefix')
                    count += 1
            block_count += count
            flux = sp.diag(*law)*transition-transition.T*sp.diag(*law)
            is_reversible = flux == sp.zeros(len(words))
            largest = max(largest, physical_identities(transition, law, gamma,
                                                      model['clock'], is_reversible))
            record = {'model': model['name'], 'word_length': ell,
                      'allowed_word_states': len(words),
                      'excluded_zero_probability_words': len(probabilities)-len(words),
                      'matched_prefix_probabilities_exact': count,
                      'word_chain_reversible': is_reversible}
            if model['name'] == 'nonlumpable_binary' and ell == 2:
                gaps = [(w, reused.word_probability(P, mu, labels, w)
                         -reused.word_probability(transition, law, gamma, w))
                        for w in itertools.product(alphabet, repeat=ell+2)]
                witness = next(((w, gap) for w, gap in gaps if gap != 0), None)
                require(witness is not None, 'Finite-prefix agreement is not exact path equivalence')
                require(not is_reversible, 'The word construction can lose reversibility')
                record['first_unmatched_longer_prefix'] = list(witness[0])
                record['longer_prefix_probability_gap_exact'] = str(witness[1])
            if model['name'] == 'sparse_ternary':
                require(len(words) == 7 < 3**ell, 'Zero-probability words really are omitted')
            records.append(record)
    return {'cases': records, 'total_matched_prefix_probabilities_exact': block_count,
            'largest_physical_matrix_dimension': largest}


def reversible_partition(model: dict) -> dict:
    P, mu, labels, cap = (model[key] for key in ('P', 'mu', 'labels', 'clock'))
    alphabet, ell, grid = (-1, 1), 2, Rational(1, 2)
    words = [w for length in range(1, ell+1)
             for w in itertools.product(alphabet, repeat=length)]
    predictions = {w: reused.future_prediction(P, labels, w) for w in words}
    grouped = {}
    for i in range(P.rows):
        key = (labels[i],)+tuple(sp.floor(predictions[w][i]/grid) for w in words)
        grouped.setdefault(key, []).append(i)
    cells = list(grouped.values())
    require(cells == [[0], [1, 2, 4], [3, 5, 6], [7]],
            'Nontrivial fixed prediction partition')
    lift, conditional = sp.zeros(P.rows, len(cells)), sp.zeros(len(cells), P.rows)
    law = sp.Matrix([[sum(mu[i] for i in cell) for cell in cells]])
    for c, cell in enumerate(cells):
        for i in cell:
            lift[i, c], conditional[c, i] = 1, mu[i]/law[c]
    E = lift*conditional
    Pbar = conditional*P*lift
    gamma = [labels[cell[0]] for cell in cells]
    require(E*E == E and sp.diag(*mu)*E == E.T*sp.diag(*mu),
            'Exact stationary conditional-expectation projection')
    require(Pbar*sp.ones(len(cells), 1) == sp.ones(len(cells), 1),
            'Reversible quotient is stochastic')
    require(law*Pbar == law and sp.diag(*law)*Pbar == Pbar.T*sp.diag(*law),
            'Exact quotient stationarity and detailed balance')
    require(irreducible(Pbar), 'Irreducible quotient')
    require(lift*Pbar*conditional == E*P*E, 'Quotient is the actual EPE compression')
    K, Kbar = cap*(P-sp.eye(P.rows)), cap*(Pbar-sp.eye(len(cells)))
    require(lift*Kbar*conditional == E*K*E, 'Actual generator is EKE, not an averaged exponential')
    for a in alphabet:
        indicator = sp.diag(*[int(value == a) for value in labels])
        require(E*indicator == indicator*E, 'Projection commutes with actuator level indicators')
    require(histogram(mu, labels) == histogram(law, gamma), 'Exact quotient actuator histogram')
    target_spectrum, cell_spectrum = sorted((-K).eigenvals()), sorted((-Kbar).eigenvals())
    gap = min(value for value in target_spectrum if value > 0)
    require(all(value == 0 or gap <= value <= cap for value in cell_spectrum),
            'Both lower gap and upper spectral cap are retained exactly')
    defect = max(abs(value) for f in predictions.values() for value in f-E*f)
    require(defect == Rational(5, 72) <= grid, 'Exact profile projection defect')
    for w, prediction in predictions.items():
        error = max(abs(value) for value in prediction
                    -lift*reused.future_prediction(Pbar, gamma, w))
        require(error <= len(w)*defect, 'Prediction suffix-induction bound')
    records = []
    for length in range(1, ell+2):
        gaps = {w: reused.word_probability(P, mu, labels, w)
                -reused.word_probability(Pbar, law, gamma, w)
                for w in itertools.product(alphabet, repeat=length)}
        tv = sum(abs(value) for value in gaps.values())/2
        certificate = sp.Integer(0) if length == 1 else 2**(length-1)*(length-1)*defect
        require(tv <= certificate, 'Stationary prefix TV from prediction defects')
        tilt_records = []
        for tilt in (Rational(2, 3), Rational(3, 2)):
            normalizer = sum(mu[i]*tilt**labels[i] for i in range(P.rows))
            require(normalizer == sum(law[i]*tilt**gamma[i] for i in range(Pbar.rows)),
                    'Approximate prefixes still have identical tilt normalization')
            tilted_tv = sum(abs(value)*tilt**w[0]/normalizer for w, value in gaps.items())/2
            multiplier = max(tilt, 1/tilt)**2
            require(tilted_tv <= multiplier*tv, 'First-symbol tilt TV multiplier')
            tilt_records.append({'exp_h_exact': str(tilt), 'tilted_tv_exact': str(tilted_tv),
                                 'tilt_certificate_exact': str(multiplier*tv)})
        records.append({'length': length, 'tv_exact': str(tv),
                        'profile_certificate_exact': str(certificate), 'tilts': tilt_records})
    require(records[-1]['tv_exact'] != '0', 'The reversible quotient is a genuine approximation')
    physical_identities(Pbar, law, gamma, cap, True)
    return {'target_hidden_states': P.rows, 'cell_hidden_states': Pbar.rows,
            'cells': cells, 'target_spectrum_exact': [str(v) for v in target_spectrum],
            'cell_spectrum_exact': [str(v) for v in cell_spectrum],
            'projection_defect_exact': str(defect), 'prefix_comparisons': records,
            'variance_exact': str(reused.scalar_moment(law, sp.Matrix(gamma), 2)),
            'spectral_cap_and_lower_gap_preserved': True}


def clock_identities() -> dict:
    alpha, nu, t = sp.symbols('alpha nu t', positive=True)
    q = nu/(nu+alpha)
    records = []
    for ell in range(8):
        r = ell+1
        # Integrate the Poisson tail term by term on [0,infinity).
        integral = 1/alpha-sum(nu**j/(alpha+nu)**(j+1) for j in range(r))
        require(sp.cancel(integral-q**r/alpha) == 0, 'Exact Poisson-tail Laplace integral')
        gamma_laplace = sp.factorial(r-1)*nu**r/(sp.factorial(r-1)*(alpha+nu)**r)
        require(sp.cancel(gamma_laplace-q**r) == 0, 'Gamma-clock Laplace transform')
        tail = 1-sp.exp(-nu*t)*sum((nu*t)**j/sp.factorial(j) for j in range(r))
        truncated_laplace = q**r*(1-sp.exp(-(alpha+nu)*t)
                                   *sum(((alpha+nu)*t)**j/sp.factorial(j) for j in range(r)))
        difference = truncated_laplace-sp.exp(-alpha*t)*tail
        require(sp.simplify(sp.diff(difference, t)-alpha*sp.exp(-alpha*t)*tail) == 0,
                'Initial-term inequality has a nonnegative derivative')
        require(sp.simplify(difference.subs(t, 0)) == 0,
                'Initial-term inequality starts at zero')
        records.append({'prefix_updates_retained': ell, 'gamma_shape': r})
    R = sp.symbols('R', positive=True)
    b, reset = R, 1/R
    require(sp.cancel(2*(Rational(1, 2)+b/reset)-(1+2*R**2)) == 0,
            'Regenerative binary-mean constant C_R')
    return {'symbolic_cases': records,
            'integral_identity': 'integral_0^infinity exp(-alpha*u) Pr(Pois(nu*u)>ell) du = q^(ell+1)/alpha',
            'initial_bound_certificate': 'D(0)=0 and D_prime(t)=alpha exp(-alpha*t) Pr(Pois(nu*t)>ell)>=0',
            'scope': 'Symbolic clock identities; entry conditioning and all-protocol coupling are proved in the note.'}


def minimal_word_length(C: sp.Expr, q: sp.Expr, epsilon: sp.Expr) -> int:
    ell = 1
    while C*q**(ell+1) > epsilon:
        ell += 1
    require(C*q**(ell+1) <= epsilon, 'Exact geometric-tail error budget')
    require(ell == 1 or C*q**ell > epsilon, 'Smallest word length allowed by the ceil formula')
    # For ell>1, this is exactly ell <= log(C/epsilon)/(-log q),
    # and hence m^ell <= (C/epsilon)^(log(m)/(-log(q))).
    require(ell == 1 or q**ell >= epsilon/C, 'Polynomial count bound without floating logarithms')
    return ell


def count_and_error_budgets() -> dict:
    # G=1 and H=log(3/2) give exact R=L_H=9/4.
    R = Rational(9, 4)
    C, alpha = 1+2*R**2, 1/R
    cases = []
    for clock in (Rational(1, 100), Rational(1, 2), sp.Integer(3), sp.Integer(7)):
        q = clock/(clock+alpha)
        boundary_power = 2
        while C*q**boundary_power >= 1:
            boundary_power += 1
        tolerances = [Rational(1, 2), Rational(1, 10), Rational(1, 100),
                      C*q**(boundary_power+3)]
        for epsilon in tolerances:
            ell = minimal_word_length(C, q, epsilon)
            certificate = C*q**(ell+1)
            if epsilon == tolerances[-1]:
                require(ell == boundary_power+2, 'Exact integer-boundary ceil case')
            cases.append({'clock_exact': str(clock), 'epsilon_exact': str(epsilon),
                          'word_length': ell, 'binary_total_state_bound': 1+2**ell,
                          'error_certificate_exact': str(certificate)})
    q, epsilon, alphabet = sp.Integer(3)/(3+alpha), Rational(1, 10), 2
    ell = minimal_word_length(2*C, q, epsilon)
    zeta = epsilon/(C*R*ell*alphabet**(ell+1))
    theta = Rational(1, 2)*alphabet**(ell+1)*ell*zeta
    require(C*(R*theta+q**(ell+1)) <= epsilon, 'Reversible corollary combined error budget')
    require(C*R*theta == epsilon/2, 'Exact half-budget for approximate prefixes')
    J = 1+sp.ceiling(1/zeta)
    d = sum(alphabet**r for r in range(1, ell+1))
    # Do not allocate the enormous integer J**d: the theorem counts it symbolically.
    return {'R_exact': str(R), 'C_R_exact': str(C), 'nonreversible_cases': cases,
            'reversible_budget': {'epsilon_exact': str(epsilon), 'word_length': ell,
                                  'prediction_resolution_exact': str(zeta),
                                  'prefix_tv_certificate_exact': str(theta),
                                  'combined_error_certificate_exact': str(C*(R*theta+q**(ell+1))),
                                  'profile_functions': d, 'bins_per_profile': int(J),
                                  'total_state_bound_symbolic': f'1+{alphabet}*({J})^({d})'},
            'rounding_method': 'Exact rational inequalities, including equality boundaries; no floating ceil decisions.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/bounded_rate_prediction.json'))
    args = parser.parse_args()
    examples, spectral = models()
    word_results = word_lifts(examples)
    script = Path(__file__).resolve()
    imported = Path(reused.__file__).resolve()
    report = {
        'status': 'PASS',
        'scope': 'Exact bounded-clock word realization, reversible EPE compression, regenerative clock identities and integer error budgets; no simulations.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'numpy': reused.np.__version__, 'scipy': reused.scipy.__version__},
        'spectral_clock': spectral,
        'stationary_word_models': word_results,
        'reversible_prediction_partition': reversible_partition(examples[0]),
        'regenerative_clock_identities': clock_identities(),
        'error_budgets_and_counts': count_and_error_budgets(),
        'largest_matrix_dimension': word_results['largest_physical_matrix_dimension'],
        'source_sha256': {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                          for path in (script, imported)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
