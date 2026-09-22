#!/usr/bin/env python3
"""Small deterministic checks of tapered positive Gaussian compression.

The theorem, rather than these samples, covers all bounded protocols and all
finite horizons.  Gaussian quadrature underestimates each bin's exponential
kernel; moving the high-rate tail to its threshold overestimates that tail.
Thus the sum of component L1 errors is a certificate, not generally the exact
L1 error of the complete kernel.  Nothing here tests finite-field remainders.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
import operator
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm

import verify_checkpoint as core
import verify_finite_accuracy as finite


@dataclass
class BinRule:
    index: int
    order: int
    source_a: np.ndarray
    source_weights: np.ndarray
    nodes: np.ndarray
    weights: np.ndarray


@dataclass
class Compression:
    rates: np.ndarray
    weights: np.ndarray
    bins: list[BinRule]
    tail_a: np.ndarray
    tail_weights: np.ndarray
    tail_threshold: float
    n: int


def gaussian_rule(a: np.ndarray, weights: np.ndarray, order: int,
                  left: float) -> tuple[np.ndarray, np.ndarray]:
    """Discrete Gaussian rule via a fully reorthogonalized Lanczos basis.

    Multiplication acts on x=2*a/left-3 in [-1,1), avoiding raw high powers
    of potentially large rates.  The Jacobi projection is diagonalized only
    after two orthogonalization passes against the complete existing basis.
    Inputs are a nonempty positive measure inside one bin, as supplied below.
    At most `order` distinct atoms are kept exactly.
    """
    atoms, inverse = np.unique(a, return_inverse=True)
    mass = np.bincount(inverse, weights=weights, minlength=len(atoms))
    if len(atoms) <= order:
        return atoms.copy(), mass
    total = float(mass.sum())
    x = 2 * atoms / left - 3
    q = np.sqrt(mass / total)
    basis = [q]
    for _ in range(1, order):
        v = x * basis[-1]
        Q = np.column_stack(basis)
        for _ in range(2):
            v -= Q @ (Q.T @ v)
        norm = float(np.linalg.norm(v))
        if norm <= 32 * np.finfo(float).eps:
            raise ArithmeticError('Floating-point Lanczos breakdown; use higher precision')
        basis.append(v / norm)
    Q = np.column_stack(basis)
    projected = Q.T @ (x[:, None] * Q)
    projected = (projected + projected.T) / 2
    nodes, eigenvectors = np.linalg.eigh(projected)
    quadrature_mass = total * eigenvectors[0] ** 2
    # Enforce zeroth moment against eigensolver roundoff; no signed weights.
    quadrature_mass *= total / float(quadrature_mass.sum())
    return left * (nodes + 3) / 2, quadrature_mass


def compress_tapered(k: float, rates: np.ndarray, weights: np.ndarray,
                     n: int) -> Compression:
    """Compress a known kernel with J=4n and order n-floor(j/4) in bin j.

    Dimensionless damped rates are a=1+lambda/k.  The tail a>=2**J is
    placed at 2**J.  There are at most 2*n*(n+1)+1 active modes.  The
    implementation rejects nonrepresentable floating-point scalings instead
    of emitting zero or infinite kinetic rates.  Zero mass uses no modes.
    """
    if isinstance(n, (bool, np.bool_)):
        raise ValueError('n must be a positive integer, not a Boolean')
    try:
        n = operator.index(n)
    except TypeError as exc:
        raise ValueError('n must be a positive integer') from exc
    if not 1 <= n <= 255:
        raise ValueError('n must lie in 1..255 for float64 bin endpoints')
    rates, weights = np.asarray(rates, dtype=float), np.asarray(weights, dtype=float)
    if (not np.isfinite(k) or k <= 0 or rates.ndim != 1
            or rates.shape != weights.shape or not np.all(np.isfinite(rates))
            or not np.all(np.isfinite(weights)) or np.any(rates <= 0)
            or np.any(weights < 0)):
        raise ValueError('finite positive k/rates and matching nonnegative weights required')
    active = weights > 0
    rates, weights = rates[active], weights[active]
    try:
        total = math.fsum(float(w) for w in weights)
    except OverflowError as exc:
        raise ValueError('total mass must be finite') from exc
    if not math.isfinite(total):
        raise ValueError('total mass must be finite')
    J = 4 * n
    edges = np.ldexp(np.ones(J + 1), np.arange(J + 1))
    with np.errstate(over='ignore', invalid='ignore'):
        a = 1 + rates / k
    if np.any(~np.isfinite(a)) or np.any(a <= 1):
        raise ValueError('dimensionless rates must be finite and distinguishable from 1')
    labels = np.searchsorted(edges, a, side='right') - 1
    bins, nodes, masses = [], [], []
    for j in range(J):
        mask = labels == j
        if not np.any(mask):
            continue
        order = n - j // 4
        aa, ww = gaussian_rule(a[mask], weights[mask], order, edges[j])
        bins.append(BinRule(j, order, a[mask], weights[mask], aa, ww))
        nodes.extend(aa)
        masses.extend(ww)
    tail = labels >= J
    if np.any(tail):
        nodes.append(edges[-1])
        masses.append(float(weights[tail].sum()))
    with np.errstate(over='ignore', invalid='ignore'):
        new_rates = k * (np.asarray(nodes, dtype=float) - 1)
    if np.any(~np.isfinite(new_rates)) or np.any(new_rates <= 0):
        raise ValueError('compressed kinetic rates are not representable as positive float64')
    return Compression(new_rates, np.asarray(masses), bins, a[tail], weights[tail],
                       float(edges[-1]), n)


def inverse_integral(a: np.ndarray, weights: np.ndarray) -> float:
    """Analytic integral of sum w exp(-a*s), with no time discretization."""
    return math.fsum(float(w / rate) for rate, w in zip(a, weights))


def component_certificate(result: Compression) -> tuple[float, float, float]:
    """Return dimensionless component L1 sum, bin bound, and tail error.

    Tiny negative differences can arise when exact quadrature has error below
    roundoff.  They are checked against a roundoff allowance and set to zero;
    this numerical value is not a computer-assisted rigorous proof certificate.
    """
    errors, bounds = [], []
    for rule in result.bins:
        left = 2. ** rule.index
        mass = float(rule.source_weights.sum())
        error = inverse_integral(rule.source_a, rule.source_weights) - inverse_integral(
            rule.nodes, rule.weights)
        tolerance = 4e-14 * mass / left
        bound = 4 * mass * 16. ** (-rule.order) / left
        core.require(-tolerance <= error <= bound + tolerance, 'Bin rational-integral bound')
        errors.append(max(0., error))
        bounds.append(bound)
    tail_mass = float(result.tail_weights.sum())
    tail_error = tail_mass / result.tail_threshold - inverse_integral(
        result.tail_a, result.tail_weights)
    core.require(-1e-14 <= tail_error <= tail_mass / result.tail_threshold + 1e-14,
                 'Tail reciprocal-integral identity and bound')
    return (math.fsum(errors) + max(0., tail_error), math.fsum(bounds), max(0., tail_error))


def solve_fraction(A: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    """Small exact elimination used only for independent rational examples."""
    rows = [row[:] + [rhs] for row, rhs in zip(A, b)]
    for j in range(len(rows)):
        pivot = next(i for i in range(j, len(rows)) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        divisor = rows[j][j]
        rows[j] = [v / divisor for v in rows[j]]
        for i in range(len(rows)):
            if i != j:
                multiplier = rows[i][j]
                rows[i] = [x - multiplier * y for x, y in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def exact_rational_checks() -> dict:
    # Gaussian nodes need not be rational.  If monic p_n vanishes at them,
    # 1/a = -(p_n(a)-p_n(0))/(a*p_n(0)) there.  The right side is a degree
    # n-1 polynomial whose integral is fixed by rational source moments.
    atoms = [Fraction(v, 16) for v in (17, 19, 22, 25, 29, 31)]
    weights = [Fraction(v, 32) for v in (1, 3, 2, 5, 4, 1)]
    cases = []
    largest_error = 0.
    for n in (1, 2, 3):
        moments = [sum((w * a ** r for a, w in zip(atoms, weights)), Fraction(0))
                   for r in range(2*n + 1)]
        coefficients = solve_fraction([[moments[i+j] for j in range(n)] for i in range(n)],
                                      [-moments[i+n] for i in range(n)]) + [Fraction(1)]
        quadrature_inverse = -sum((coefficients[r+1] * moments[r] for r in range(n)),
                                  Fraction(0)) / coefficients[0]
        source_inverse = sum((w / a for a, w in zip(atoms, weights)), Fraction(0))
        error = source_inverse - quadrature_inverse
        bound = 4 * moments[0] / 16 ** n
        core.require(0 < error <= bound, 'Exact rational Gaussian reciprocal bound')
        nodes, masses = gaussian_rule(np.array(atoms, dtype=float),
                                     np.array(weights, dtype=float), n, 1.)
        discrepancy = abs(inverse_integral(nodes, masses) - float(quadrature_inverse))
        largest_error = max(largest_error, discrepancy)
        core.require(discrepancy < 5e-15, 'Float Gaussian reciprocal agrees with exact arithmetic')
        cases.append({'order':n, 'exact_component_l1':str(error),
                      'exact_component_bound':str(bound),
                      'float_inverse_integral_error':discrepancy})
    threshold = Fraction(16)
    tail_atoms, tail_weights = [Fraction(16), Fraction(24), Fraction(64)], [Fraction(1,8)]*3
    tail_error = sum((w * (1/threshold - 1/a) for a, w in zip(tail_atoms, tail_weights)),
                     Fraction(0))
    core.require(tail_error == Fraction(13, 1536), 'Exact rational tail integral identity')
    return {'cases':cases, 'tail_exact_l1':str(tail_error),
            'max_float_inverse_integral_error':largest_error,
            'arithmetic':'fractions.Fraction; no Gaussian node rationality assumed'}


def deterministic_spectrum(n: int, k: float) -> tuple[np.ndarray, np.ndarray]:
    # All bins populated, including every drop in the tapered order.  The
    # modest support size deliberately exceeds each bin's Gaussian order.
    offsets = np.linspace(1.0625, 1.9375, n + 2)
    a = np.concatenate([2.**j * offsets for j in range(4*n)] +
                       [np.array([2.**(4*n), 3*2.**(4*n)])])
    raw = 1 + .25 * (np.arange(len(a)) % 5)
    return k * (a - 1), .64 * raw / raw.sum()


def quadrature_checks() -> tuple[dict, list[tuple[float, np.ndarray, np.ndarray, Compression]]]:
    max_moment_error = 0.
    min_sampled_gap = 0.
    max_mass_error = 0.
    bin_count = sign_samples = 0
    cases, examples = [], []
    for n in (1, 2, 3):
        k = .7
        rates, weights = deterministic_spectrum(n, k)
        result = compress_tapered(k, rates, weights, n)
        W = float(weights.sum())
        core.require(len(result.rates) <= 2*n*(n+1)+1, 'Tapered mode count')
        core.require(np.all(result.weights > 0) and np.all(result.rates > 0), 'Positive surrogate')
        mass_error = abs(float(result.weights.sum()) - W)
        max_mass_error = max(max_mass_error, mass_error)
        core.require(mass_error < 2e-15, 'Total mass preservation')
        for rule in result.bins:
            bin_count += 1
            left = 2.**rule.index
            mass = float(rule.source_weights.sum())
            core.require(np.all(rule.nodes >= left) and np.all(rule.nodes < 2*left),
                         'Gaussian nodes lie in their source bin')
            core.require(len(rule.nodes) <= rule.order, 'Per-bin mode count')
            x, y = 2*rule.source_a/left-3, 2*rule.nodes/left-3
            for degree in range(2*rule.order):
                error = abs(float(rule.source_weights @ x**degree - rule.weights @ y**degree))/mass
                max_moment_error = max(max_moment_error, error)
                core.require(error < 2e-12, 'Gaussian moments through degree 2n_j-1')
            for tau in (0., 1e-4, .03, .3, 1., 3., 10., 30.):
                gap = float(rule.source_weights @ np.exp(-rule.source_a*tau/left)
                            - rule.weights @ np.exp(-rule.nodes*tau/left)) / mass
                min_sampled_gap = min(min_sampled_gap, gap)
                sign_samples += 1
                core.require(gap >= -2e-14, 'Sampled Gaussian exponential underestimate')
        l1, bin_bound, tail_error = component_certificate(result)
        universal = 4*W*16.**(-n)
        component_bound = bin_bound + float(result.tail_weights.sum()) / result.tail_threshold
        core.require(l1 <= component_bound+2e-14 and component_bound <= universal+2e-14,
                     'Tapered universal kernel bound')
        examples.append((k, rates, weights, result))
        cases.append({'order_parameter':n, 'dyadic_bins':4*n,
                      'bin_orders':[rule.order for rule in result.bins],
                      'source_modes':len(rates), 'compressed_modes':len(result.rates),
                      'mode_upper_bound':2*n*(n+1)+1,
                      'component_l1_sum':l1, 'component_bound':component_bound,
                      'universal_dimensionless_l1_bound':universal,
                      'tail_l1':tail_error, 'U1_response_bound':2*universal})
    return ({'cases':cases, 'bins_checked':bin_count,
             'max_mass_error':max_mass_error, 'max_normalized_moment_error':max_moment_error,
             'pointwise_kernel_samples':sign_samples,
             'minimum_normalized_sampled_kernel_gap':min_sampled_gap,
             'scope':'Moment and pointwise sign checks are deterministic samples, not a proof.'}, examples)


PROTOCOLS = {
    'constant':[(.15, 1.), (.65, 1.), (1.3, 1.)],
    'sign_changes':[(.2, 1.), (.35, -1.), (.55, .4), (.4, -1.)],
    'zero_and_restart':[(.2, .8), (.6, 0.), (.15, -.8), (.5, 0.)],
    'larger_amplitude':[(.1, -1.3), (.45, .7), (.7, 1.3)],
}


def run_protocol(k: float, rates: np.ndarray, weights: np.ndarray,
                 result: Compression, protocol: list[tuple[float, float]]) -> tuple[float, int]:
    """Times in PROTOCOLS are dimensionless k*t; each segment is exact expm."""
    original = np.zeros(4+len(rates)); original[0] = 1.
    surrogate = np.zeros(4+len(result.rates)); surrogate[0] = 1.
    largest_error, samples = 0., 0
    for duration, u in protocol:
        A = finite.memory_matrix(k, rates, weights, u)
        B = finite.memory_matrix(k, result.rates, result.weights, u)
        for fraction in (.25, .5, 1.):
            y = expm((duration*fraction/k)*A) @ original
            z = expm((duration*fraction/k)*B) @ surrogate
            largest_error = max(largest_error, float(abs(y[2]+y[3]-z[2]-z[3])))
            samples += 1
        original, surrogate = y, z
    return largest_error, samples


def protocol_checks(examples: list[tuple[float, np.ndarray, np.ndarray, Compression]]) -> dict:
    cases, samples, largest_dimension = [], 0, 0
    max_ratio = 0.
    for k, rates, weights, result in examples:
        l1, _, _ = component_certificate(result)
        for name, protocol in PROTOCOLS.items():
            error, count = run_protocol(k, rates, weights, result, protocol)
            U = max(abs(u) for _, u in protocol)
            certificate = 2 * U**3 * l1
            universal = 8 * U**3 * float(weights.sum()) * 16.**(-result.n)
            core.require(error <= certificate+3e-12 and certificate <= universal+3e-12,
                         'Protocol response coefficient within component and universal bounds')
            max_ratio = max(max_ratio, error/certificate)
            samples += count
            largest_dimension = max(largest_dimension, 4+len(rates), 4+len(result.rates))
            cases.append({'n':result.n, 'protocol':name, 'U':U, 'max_sampled_error':error,
                          'component_response_certificate':certificate,
                          'universal_response_bound':universal})
    scale_cases = []
    reference_rates = reference_weights = None
    reference_error = None
    for k in (.125, .7, 3.):
        rates, weights = deterministic_spectrum(2, k)
        result = compress_tapered(k, rates, weights, 2)
        error, count = run_protocol(k, rates, weights, result, PROTOCOLS['sign_changes'])
        samples += count
        if reference_rates is None:
            reference_rates, reference_weights, reference_error = result.rates/k, result.weights, error
        core.require(np.max(abs(result.rates/k-reference_rates)) < 2e-12
                     and np.max(abs(result.weights-reference_weights)) < 2e-14
                     and abs(error-reference_error) < 3e-12, 'k scaling of nodes, weights, response')
        scale_cases.append({'k':k, 'max_sampled_error':error})
    return {'cases':cases, 'scale_cases':scale_cases, 'protocol_samples':samples,
            'max_observed_error_over_component_certificate':max_ratio,
            'largest_memory_matrix_dimension':largest_dimension,
            'scope':'Selected bounded piecewise constant protocols; all-protocol coverage is analytic.'}


def realization_checks() -> dict:
    # A small three-bin example suffices to check the existing paired-state
    # realization against the new Gaussian kernel without a large generator.
    k = .7
    a = np.concatenate([2.**j*np.array([1.125, 1.375, 1.625, 1.875]) for j in range(3)])
    weights = np.full(len(a), .64/len(a))
    result = compress_tapered(k, k*(a-1), weights, 2)
    mu, H, g = finite.realize_kernel(result.rates, result.weights)
    core.require(np.max(abs(H.sum(axis=1))) < 1e-12, 'Realization row sums')
    core.require(np.max(abs(mu[:,None]*H-H.T*mu[None,:])) < 1e-12, 'Reversible realization')
    mask = ~np.eye(len(mu), dtype=bool)
    core.require(np.all(H[mask] > 0), 'Irreducible realization')
    core.require(abs(mu@g) < 1e-13 and np.max(abs(g)) <= .8+1e-14, 'Centered bounded sensitivity')
    kernel_error = 0.
    for t in (0., .01, .2, 1., 5.):
        actual = float((mu*g) @ expm(t*H) @ g)
        target = float(result.weights @ np.exp(-result.rates*t))
        kernel_error = max(kernel_error, abs(actual-target))
    core.require(kernel_error < 2e-13, 'Paired realization recovers Gaussian kernel')
    B = core.generator_coefficients(k, mu, H, g)
    state_count = len(mu)+1
    full = np.zeros(4*state_count); full[:state_count] = np.r_[.5, .5*mu]
    memory = np.zeros(4+len(result.rates)); memory[0] = 1.
    observable = np.r_[-1., np.ones(len(mu))]
    cubic_error = linear_error = quadratic_error = 0.
    for duration, u in PROTOCOLS['sign_changes']:
        full = expm(duration/k*core.block_matrix(B, u)) @ full
        memory = expm(duration/k*finite.memory_matrix(k, result.rates, result.weights, u)) @ memory
        linear_error = max(linear_error, abs(float(observable @ full[state_count:2*state_count])-memory[1]))
        quadratic_error = max(quadratic_error, abs(float(observable @ full[2*state_count:3*state_count])))
        cubic_error = max(cubic_error, abs(float(observable @ full[3*state_count:])-memory[2]-memory[3]))
    core.require(max(linear_error, quadratic_error, cubic_error) < 3e-12,
                 'Full Markov coefficient hierarchy agrees with memory equations')
    passive = np.zeros((state_count, 2)); passive[0, 0] = 1; passive[1:, 1] = 1
    core.require(np.max(abs(B[0] @ passive - passive @ np.array([[-k,k],[k,-k]]))) < 2e-13,
                 'Realization preserves two-state passive lumpability')
    return {'compressed_modes':len(result.rates), 'surrogate_states':state_count,
            'full_coefficient_matrix_dimension':4*state_count,
            'max_realized_kernel_error':kernel_error, 'max_linear_response_error':linear_error,
            'max_quadratic_response':quadratic_error, 'max_full_markov_memory_cubic_error':cubic_error}


def boundary_checks() -> dict:
    # Exact dyadic endpoints belong to the bin on their right; threshold is tail.
    a = np.array([1.25, 2., 4., 8., 16., 32.])
    weights = np.array([.1, .1, .1, .1, .2, .4])
    result = compress_tapered(1., a-1, weights, 1)
    core.require([rule.index for rule in result.bins] == [0,1,2,3], 'Half-open bin endpoints')
    core.require(np.array_equal(result.tail_a, [16.,32.]), 'Threshold belongs to tail')
    core.require(np.allclose(result.rates, [ .25, 1., 3., 7., 15.]), 'Exact atoms and tail placement')
    l1, _, tail = component_certificate(result)
    core.require(abs(l1-.0125) < 2e-16 and abs(tail-.0125) < 2e-16, 'Tail-only approximation identity')
    duplicate = compress_tapered(1., np.array([.25,.25,.75]), np.array([.1,.2,.3]), 2)
    core.require(np.allclose(duplicate.rates,[.25,.75]) and np.allclose(duplicate.weights,[.3,.3]),
                 'Duplicate atoms aggregated and small support exact')
    empty = compress_tapered(1., np.array([]), np.array([]), 2)
    zero = compress_tapered(1., np.array([.25,10.]), np.zeros(2), 2)
    for item in (empty, zero):
        core.require(len(item.rates) == len(item.weights) == 0
                     and component_certificate(item) == (0.,0.,0.), 'Zero mass requires no modes')
    tail_only = compress_tapered(1., np.array([15.,31.]), np.array([.3,.7]), 1)
    core.require(len(tail_only.bins) == 0 and len(tail_only.rates) == 1,
                 'Tail-only measure has one mode')
    near_zero = compress_tapered(1., np.array([2.**-40]), np.array([1.]), 1)
    core.require(near_zero.rates[0] > 0, 'Representable small positive kinetic rate')
    invalids = [
        (0., [1.], [1.], 1), (float('nan'), [1.], [1.], 1),
        (float('inf'), [1.], [1.], 1), (1., [-1.], [1.], 1),
        (1., [0.], [1.], 1), (1., [float('inf')], [1.], 1),
        (1., [1.], [-1.], 1), (1., [1.], [float('nan')], 1),
        (1., [1.,2.], [1.], 1), (1., [[1.]], [[1.]], 1),
        (1., [1.], [1.], 0), (1., [1.], [1.], 1.5),
        (1., [1.], [1.], 256), (1., [1e-30], [1.], 1),
        (1., [1.], [1.], True), (1., [1.,2.], [1e308,1e308], 1),
    ]
    rejected = 0
    for k, rates, mass, n in invalids:
        try:
            compress_tapered(k, np.array(rates), np.array(mass), n)
        except ValueError:
            rejected += 1
    core.require(rejected == len(invalids), 'Invalid or unrepresentable inputs rejected')
    return {'half_open_endpoints':'PASS', 'exact_small_support_and_duplicates':'PASS',
            'empty_and_zero_mass':'PASS', 'tail_only':'PASS',
            'small_positive_rate':'PASS', 'invalid_inputs_rejected':rejected,
            'float64_limit':'n<=255; unrepresentable dimensionless or compressed rates rejected'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/quadrature.json'))
    args = parser.parse_args()
    quadrature, examples = quadrature_checks()
    report = {
        'status':'PASS',
        'scope':'Deterministic consistency checks, not proof review, optimality, novelty, or finite-field certification.',
        'versions':{'python':platform.python_version(), 'numpy':np.__version__, 'scipy':scipy.__version__},
        'theorem_checked':{'bins':'[2^j,2^(j+1)), j=0,...,4n-1',
                           'bin_order':'n-floor(j/4)', 'tail_threshold':'2^(4n)',
                           'mode_bound':'2n(n+1)+1', 'cubic_coefficient_bound':'8 U^3 W 16^(-n)'},
        'quadrature':quadrature, 'exact_rational_integrals':exact_rational_checks(),
        'protocols':protocol_checks(examples), 'paired_realization':realization_checks(),
        'boundaries':boundary_checks(),
        'source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                         for name in ('verify_checkpoint.py', 'verify_finite_accuracy.py', 'verify_quadrature.py')},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
