#!/usr/bin/env python3
"""Small deterministic checks of the root-exponential response obstruction.

The proof uses continuous Hankel rank and a Cauchy inverse identity. This
script checks exact identities and finite examples at high precision; its
computed eigenvalues are not interval certificates or minimax solutions.
All matrices have dimension at most 14. No simulation or network access.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def digits(value: mp.mpf, count: int = 55) -> str:
    return mp.nstr(value, count)


def exact_cauchy_checks() -> list[dict]:
    records = []
    for r, ratio in ((2, sp.Rational(2)), (3, sp.Rational(2)),
                     (4, sp.Rational(3, 2)), (5, sp.Rational(5, 4))):
        nodes = [4*ratio**i for i in range(r)]
        C = sp.Matrix([[1/(a+b) for b in nodes] for a in nodes])
        inverse = C.inv()
        require(C*inverse == sp.eye(r), 'Exact rational Cauchy inverse')
        require(all(C[:i, :i].det() > 0 for i in range(1, r+1)),
                'Exact positive principal minors')
        for i in range(r):
            wanted = 2*nodes[i]*sp.prod(((nodes[i]+nodes[j])/(nodes[i]-nodes[j]))**2
                                      for j in range(r) if j != i)
            require(inverse[i, i] == wanted, 'Exact Cauchy inverse diagonal formula')
        records.append({'dimension': r, 'geometric_ratio_exact': str(ratio),
                        'inverse_identity': True, 'positive_principal_minors': True,
                        'diagonal_product_identities': r,
                        'trace_inverse_exact': str(sp.trace(inverse))})
    return records


def log_coth_integral_check() -> dict:
    m = sp.symbols('m', integer=True, nonnegative=True)
    odd_series = sp.summation(2/(2*m+1)**2, (m, 0, sp.oo))
    require(sp.simplify(odd_series-sp.pi**2/4) == 0,
            'Integrated positive odd-exponential series')
    # log coth(x/2) = 2 sum exp(-(2m+1)x)/(2m+1).
    # Positivity permits termwise integration. No numerical improper
    # quadrature is needed, including at the logarithmic endpoint.
    with mp.workdps(100):
        N = 64
        partial = mp.fsum(mp.mpf(2)/(2*j+1)**2 for j in range(N))
        remainder = mp.pi**2/4-partial
        require(mp.mpf(1)/(2*N+1) <= remainder <= mp.mpf(1)/(2*N-1),
                'Integral-test tail bounds for the odd reciprocal-square series')
        return {'integral': 'integral_0^infinity log(coth(x/2)) dx = pi^2/4',
                'symbolic_positive_series_identity': True,
                'finite_series_terms': N,
                'finite_series_remainder': digits(remainder),
                'remainder_lower_bound': str(sp.Rational(1, 2*N+1)),
                'remainder_upper_bound': str(sp.Rational(1, 2*N-1))}


def symbolic_step_decomposition() -> dict:
    tau, rate, weight = sp.symbols('tau rate weight', real=True)
    e2 = sp.exp(-2*tau)
    source = -(1-e2)/3+tau*e2+e2*(weight*tau-2*weight*(
        sp.exp((1-rate)*tau)-1-(1-rate)*tau)/(1-rate)**2)
    amplitude = 2*weight/(1-rate)**2
    baseline = -sp.Rational(1, 3)+(sp.Rational(1, 3)+amplitude)*e2 + (
        1+weight+2*weight/(1-rate))*tau*e2
    require(sp.simplify(source-baseline+amplitude*sp.exp(-(1+rate)*tau)) == 0,
            'General-rate step curve equals rank-three baseline minus positive exponential')
    t, s = sp.symbols('t s', nonnegative=True)
    b0, b1, b2 = sp.symbols('b0 b1 b2')
    baseline_kernel = b0+b1*sp.exp(-2*(t+s))+b2*(t+s)*sp.exp(-2*(t+s))
    phi_t = sp.Matrix([1, sp.exp(-2*t), t*sp.exp(-2*t)])
    phi_s = sp.Matrix([1, sp.exp(-2*s), s*sp.exp(-2*s)])
    factors = sp.Matrix([[b0, 0, 0], [0, b1, b2], [0, b2, 0]])
    require(sp.expand(baseline_kernel-(phi_t.T*factors*phi_s)[0]) == 0,
            'Explicit three-dimensional baseline Hankel factorization')
    return {'general_rate_identity': True, 'rate_collision_excluded': 'lambda/k = 1',
            'baseline_hankel_factor_dimension': 3,
            'positive_amplitude': '2 c U^3 / (1-lambda/k)^2'}


def theorem_case(D: int, precision: int) -> dict:
    with mp.workdps(precision):
        r = 3*D+2
        delta = mp.pi/mp.sqrt(3*(r-1))
        nodes = [4*mp.exp(j*delta) for j in range(r)]
        maximum = nodes[-1]
        rates = [b-mp.mpf(3)/2 for b in nodes]
        amplitudes = [2/(r*(b-mp.mpf(5)/2)**2) for b in nodes]
        amplitude_floor = 2/(r*maximum**2)
        require(min(rates) > 0 and all(rate != 1 for rate in rates),
                'Strictly positive noncolliding target rates')
        require(min(amplitudes) >= amplitude_floor, 'Positive amplitude lower bound')
        C = mp.matrix([[1/(a+b) for b in nodes] for a in nodes])
        root_weights = mp.diag([mp.sqrt(w) for w in amplitudes])
        K = root_weights*C*root_weights
        inverse = C**-1
        diagonal_relative_error = mp.mpf(0)
        for i, a in enumerate(nodes):
            product = 2*a*mp.fprod(mp.coth(abs(i-j)*delta/2)**2 for j in range(r) if j != i)
            diagonal_relative_error = max(diagonal_relative_error, abs(inverse[i, i]/product-1))
        require(diagonal_relative_error < mp.mpf(10)**(-precision+25),
                'High-precision inverse diagonal agrees with coth product')
        trace_inverse = mp.fsum(inverse[j, j] for j in range(r))
        trace_upper = 2*r*maximum*mp.exp(mp.pi**2/delta)
        require(trace_inverse <= trace_upper, 'Cauchy inverse trace bound')
        c_floor = mp.exp(-mp.pi**2/delta)/(2*r*maximum)
        analytic_bound = mp.exp(-2*mp.pi*mp.sqrt(3*(r-1)))/(64*r*r)
        require(abs(amplitude_floor*c_floor/analytic_bound-1) < mp.mpf(10)**(-precision+8),
                'Optimized root-exponential lower-bound constant')
        lambda_min_C = mp.eigsy(C, eigvals_only=True)[0]
        lambda_min_K = mp.eigsy(K, eigvals_only=True)[0]
        require(lambda_min_C >= c_floor and lambda_min_K >= analytic_bound,
                'Computed Gram eigenvalues respect conservative analytic bounds')

        # Independently check the sum-to-integral bound for log coth,
        # enclosing the uncomputed discrete tail by a geometric series.
        count = 100
        coth_sum = mp.fsum(mp.log(mp.coth(j*delta/2)) for j in range(1, count+1))
        q = mp.exp(-delta)
        coth_tail = 2*q**(count+1)/((1-q)*(1-q**(2*(count+1))))
        require(4*(coth_sum+coth_tail) <= mp.pi**2/delta,
                'Finite sum plus rigorous geometric tail is below integral bound')

        # A finite horizon retains at least half the conservative bound.
        T = (mp.pi**2/delta+(r-1)*delta+mp.log(2*r*r))/8
        tail = mp.matrix([[mp.exp(-(a+b)*T)/(a+b) for b in nodes] for a in nodes])
        finite_C = C-tail
        finite_K = root_weights*finite_C*root_weights
        tail_trace = mp.fsum(tail[j, j] for j in range(r))
        crude_tail = r*mp.exp(-8*T)/8
        require(tail_trace <= crude_tail, 'Truncated Gram positive tail trace bound')
        require(abs(crude_tail/(c_floor/2)-1) < mp.mpf(10)**(-precision+8),
                'Finite horizon chosen to halve the conservative Gram bound')
        finite_lambda_C = mp.eigsy(finite_C, eigvals_only=True)[0]
        finite_lambda_K = mp.eigsy(finite_K, eigvals_only=True)[0]
        require(finite_lambda_C >= c_floor/2 and finite_lambda_K >= analytic_bound/2,
                'Finite-horizon eigenvalues respect half-strength bounds')
        return {
            'state_budget_D': D, 'target_modes_r': r,
            'target_total_states_by_jacobi': r+2,
            'surrogate_stationary_hierarchy_rank_bound': 3*D-2,
            'baseline_plus_surrogate_rank_bound': 3*D+1,
            'working_decimal_digits': precision,
            'geometric_log_spacing': digits(delta),
            'largest_damped_rate_b': digits(maximum),
            'target_lambda_over_k_min': digits(min(rates)),
            'target_lambda_over_k_max': digits(max(rates)),
            'minimum_positive_amplitude': digits(min(amplitudes)),
            'inverse_diagonal_max_relative_error': digits(diagonal_relative_error),
            'computed_inverse_trace': digits(trace_inverse),
            'analytic_inverse_trace_upper': digits(trace_upper),
            'computed_C_smallest_eigenvalue': digits(lambda_min_C, 75),
            'analytic_C_eigenvalue_floor': digits(c_floor, 75),
            'computed_positive_Hankel_smallest_eigenvalue': digits(lambda_min_K, 75),
            'analytic_response_lower_bound': digits(analytic_bound, 75),
            '_eigenvalue_validation_digits': digits(lambda_min_K, precision),
            'coth_series_terms': count,
            'coth_discrete_tail_upper': digits(coth_tail),
            'finite_horizon': {
                'kernel_variable_cutoff_T': digits(T),
                'required_response_horizon_k_t': digits(2*T),
                'weighted_measure_mass': digits(1-mp.exp(-T)),
                'computed_Gram_tail_trace': digits(tail_trace),
                'analytic_Gram_tail_trace_upper': digits(crude_tail),
                'computed_C_T_smallest_eigenvalue': digits(finite_lambda_C, 75),
                'computed_positive_Hankel_smallest_eigenvalue': digits(finite_lambda_K, 75),
                'analytic_response_lower_bound': digits(analytic_bound/2, 75),
            },
        }


def theorem_checks() -> dict:
    cases = []
    for D in (2, 3, 4):
        low = theorem_case(D, 100)
        high = theorem_case(D, 150)
        with mp.workdps(150):
            relative = abs(mp.mpf(low.pop('_eigenvalue_validation_digits')) /
                           mp.mpf(high.pop('_eigenvalue_validation_digits'))-1)
            require(relative < mp.mpf('1e-65'), '100-to-150-digit eigenvalue consistency')
        high['eigenvalue_relative_change_100_to_150_digits'] = digits(relative)
        cases.append(high)
    return {'normalization': 'W=U=k=1; response bounds scale by W U^3, times by 1/k',
            'cases': cases, 'largest_matrix_dimension': max(x['target_modes_r'] for x in cases),
            'eigenvalue_scope': 'High-precision computed consistency; no interval-certified eigenvalues.',
            'bound_scope': 'The conservative bound follows from the analytic rank and inverse-trace proof, not numerical optimization.'}


def exact_master_hankel_moments() -> dict:
    """Check probability-weighted moments against an analytic Markov model.

The finite master-coefficient hierarchy and explicit response formula are
independent representations of the same three-state reversible example.
Their weighted double integrals are computed by exact resolvents.
"""
    h = sp.symbols('h', real=True)
    Q = sp.Matrix([
        [0, sp.exp(sp.Rational(3, 2)*h)/2, sp.exp(h/2)/2],
        [sp.exp(-h/2), 0, sp.Rational(2, 5)],
        [sp.exp(-sp.Rational(3, 2)*h), sp.Rational(2, 5), 0],
    ])
    for i in range(3):
        Q[i, i] = -sum(Q[i, j] for j in range(3) if j != i)
    A = [Q.diff(h, n).subs(h, 0).T/sp.factorial(n) for n in range(4)]
    L = sp.zeros(12)
    for row in range(4):
        for col in range(row+1):
            L[3*row:3*row+3, 3*col:3*col+3] = A[row-col]
    initial = sp.zeros(12, 1)
    initial[:3, 0] = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)])
    output = sp.zeros(1, 12)
    output[0, 9:12] = sp.Matrix([[-1, 1, 1]])
    require(A[0]*initial[:3, 0] == sp.zeros(3, 1), 'Exact master preparation stationary')

    test_rates = [sp.Rational(j, 3) for j in range(6)]
    # The probability weight exp(-t) adds one to each test rate.
    resolvents = [((1+s)*sp.eye(12)-L).inv() for s in test_rates]
    direct = sp.Matrix([[(output*left*right*initial)[0] for right in resolvents]
                        for left in resolvents])
    rate, W = sp.Rational(4, 5), sp.Rational(1, 4)
    beta = 1+rate
    amplitude = 2*W/(1-rate)**2
    constant = -sp.Rational(1, 3)
    e_coefficient = sp.Rational(1, 3)+amplitude
    t_coefficient = 1+W+2*W/(1-rate)
    baseline = sp.Matrix([[
        constant/((1+s)*(1+t)) + e_coefficient/((3+s)*(3+t))
        + t_coefficient*(1/((3+s)**2*(3+t))+1/((3+s)*(3+t)**2))
        for t in test_rates] for s in test_rates])
    positive = sp.Matrix([[amplitude/((1+beta+s)*(1+beta+t))
                           for t in test_rates] for s in test_rates])
    require(direct == baseline-positive, 'Exact probability-Hankel moments from master resolvents')
    require(baseline.rank() == 3, 'Exact compressed baseline rank three')
    require(positive.rank() == 1, 'Exact positive one-mode compressed rank one')
    # These are finite moments of the continuous kernel, not a discretized
    # approximation of the operator spectrum used for the lower bound.
    return {'target_states': 3, 'master_coefficient_matrix_dimension': 12,
            'test_functions': ['exp(-s t), s='+str(x) for x in test_rates],
            'probability_weight': 'exp(-t) dt on [0,infinity)',
            'exact_double_resolvent_moments_checked': len(test_rates)**2,
            'exact_baseline_compressed_rank': baseline.rank(),
            'exact_positive_component_rank': positive.rank(),
            'master_response_decomposition_exact': True,
            'scope': 'Exact integrated kernel identities; no discretized operator-rank inference.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/unrestricted_rate_lower_bound.json'))
    args = parser.parse_args()
    report = {
        'status': 'PASS',
        'scope': 'Exact algebra and small deterministic high-precision checks of the continuous-Hankel proof.',
        'versions': {'python': platform.python_version(), 'sympy': sp.__version__,
                     'mpmath': mp.__version__},
        'exact_cauchy_inverse': exact_cauchy_checks(),
        'log_coth_integral': log_coth_integral_check(),
        'step_decomposition': symbolic_step_decomposition(),
        'root_exponential_witnesses': theorem_checks(),
        'independent_master_hankel_moments': exact_master_hankel_moments(),
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
