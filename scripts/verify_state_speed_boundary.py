#!/usr/bin/env python3
"""Exact small certificates for the state-speed and unbounded-rate boundary notes.

Uses only the Python standard library and rational arithmetic.  No physical
target graph, floating-point rank, or exponential Vandermonde inverse is built.
These checks support specific algebraic steps, not the full analytic theorems.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def eye(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def mm(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F())
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a: list[list[F]], x: list[F]) -> list[F]:
    return [sum((v*w for v, w in zip(row, x)), F()) for row in a]


def add(a: list[list[F]], b: list[list[F]], scale: F = F(1)) -> list[list[F]]:
    return [[x+scale*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def times(a: list[list[F]], scalar: F) -> list[list[F]]:
    return [[scalar*x for x in row] for row in a]


def inner(x: list[F], y: list[F], mu: list[F]) -> F:
    return sum((p*a*b for p, a, b in zip(mu, x, y)), F())


def norm2(x: list[F], mu: list[F]) -> F:
    return inner(x, x, mu)


def adjoint(a: list[list[F]], mu: list[F]) -> list[list[F]]:
    return [[mu[j]*a[j][i]/mu[i] for j in range(len(mu))] for i in range(len(mu))]


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    aug = [row.copy()+unit for row, unit in zip(a, eye(n))]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        divisor = aug[col][col]
        aug[col] = [value/divisor for value in aug[col]]
        for row in range(n):
            if row != col:
                multiplier = aug[row][col]
                aug[row] = [x-multiplier*y for x, y in zip(aug[row], aug[col])]
    result = [row[n:] for row in aug]
    require(mm(a, result) == eye(n), 'Exact inverse must multiply back to the identity')
    return result


def determinant(a: list[list[F]]) -> F:
    if len(a) == 1:
        return a[0][0]
    return sum(((-1)**j*a[0][j]*determinant(
        [[a[i][k] for k in range(len(a)) if k != j] for i in range(1, len(a))])
        for j in range(len(a))), F())


def psd_principal_minors(a: list[list[F]]) -> list[F]:
    require(a == transpose(a), 'A PSD certificate applies to a symmetric matrix')
    n, minors = len(a), []
    for length in range(1, n+1):
        for subset in itertools.combinations(range(n), length):
            minor = determinant([[a[i][j] for j in subset] for i in subset])
            require(minor >= 0, 'Every principal minor in the exact PSD certificate is nonnegative')
            minors.append(minor)
    return minors


def flux_repair(a: list[list[F]], mu: list[F]) -> list[list[F]]:
    """The simultaneous original-marginal clipping and rank-one fill in the note."""
    n, one = len(mu), [F(1)]*len(mu)
    row, col = mv(a, one), mv(adjoint(a, mu), one)
    left = [min(F(1), 1/x) if x else F(1) for x in row]
    right = [min(F(1), 1/x) if x else F(1) for x in col]
    clipped = [[left[i]*a[i][j]*right[j] for j in range(n)] for i in range(n)]
    row_deficit = [1-x for x in mv(clipped, one)]
    col_deficit = [1-x for x in mv(adjoint(clipped, mu), one)]
    total = sum((mu[i]*row_deficit[i] for i in range(n)), F())
    require(min(row_deficit+col_deficit) >= 0 and
            total == sum((mu[i]*col_deficit[i] for i in range(n)), F()),
            'Clipping leaves nonnegative deficits of equal total stationary mass')
    result = [[clipped[i][j]+(row_deficit[i]*mu[j]*col_deficit[j]/total if total else 0)
               for j in range(n)] for i in range(n)]
    require(mv(result, one) == one and mv(adjoint(result, mu), one) == one,
            'The repaired kernel and its consistently defined adjoint are stochastic')
    return result


def exp_one_interval(terms: int = 18) -> tuple[F, F]:
    term, lower = F(1), F(1)
    for j in range(1, terms+1):
        term /= j
        lower += term
    first_omitted = term/(terms+1)
    upper = lower+first_omitted/(1-F(1, terms+2))
    return lower, upper


def log_interval(value: F, terms: int = 36) -> tuple[F, F]:
    """Enclose log(value) with 2*atanh series, using only exact rationals."""
    require(value > 0, 'Logarithm interval has a positive argument')
    if value < 1:
        lo, hi = log_interval(1/value, terms)
        return -hi, -lo
    power = 0
    while value > 2:
        value /= 2
        power += 1

    def local(x: F) -> tuple[F, F]:
        z = (x-1)/(x+1)
        lower = 2*sum((z**(2*j+1)/(2*j+1) for j in range(terms)), F())
        tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
        return lower, lower+tail

    lo, hi = local(value)
    lo2, hi2 = local(F(2))
    return lo+power*lo2, hi+power*hi2


def short_interval(interval: tuple[F, F], places: int = 10) -> dict:
    denominator = 10**places
    lo, hi = interval
    lo_scaled, hi_scaled = lo*denominator, hi*denominator
    left = lo_scaled.numerator//lo_scaled.denominator
    right = -((-hi_scaled.numerator)//hi_scaled.denominator)
    require(F(left, denominator) <= lo <= hi <= F(right, denominator),
            'Reported rational interval is rounded outward')
    return {'lower_exact': str(F(left, denominator)), 'upper_exact': str(F(right, denominator))}


def uniform_bookkeeping_checks() -> dict:
    # An affine expression is the pair (coefficient of n, constant).
    def affine_le(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
        difference = tuple(b-a for a, b in zip(left, right))
        require(difference[0] >= 0 and sum(difference) >= 0,
                'An affine exponent difference is nonnegative for every integer n >= 1')
        return difference

    gaps = {
        '36n+5 <= 36(n+1)': affine_le((36, 5), (36, 36)),
        '108n+11 <= 108(n+1)': affine_le((108, 11), (108, 108)),
        '91n+57 <= 91(n+1)': affine_le((91, 57), (91, 91)),
    }
    require((1+36+54, 1+2+54) == (91, 57), 'The repair exponent expands exactly')
    require(3*36 == 108 and 3*3+2 == 11, 'Scalar degree is three per edge plus two endpoints')
    require(3*54 == 162 and 3*6+2 == 20, 'Whole-word Gram degree is 162n+20')
    require(64**2 >= 72, 'V >= 1 implies 72 V^2 <= (64 V^3)^2')
    coefficient_examples = []
    for v in (F(1), F(3, 2), F(7)):
        p = 64*v**3
        require(16*(2*v)*v*(2*v) == p and 72*v*v <= p*p,
                'Transport and scalar coefficient masses agree with the prescribed formulas')
        coefficient_examples.append({'V_exact': str(v), 'P_exact': str(p)})
    # Replace 3 sqrt(3) by 6; check the induction base and linear step exactly.
    require(27 <= 36 and 6*(36+3) <= 256**2,
            'The square-root majorant and n=1 induction base are exact')
    induction_difference = (6*(256*36-36), 6*(256*3-39))
    require(min(induction_difference) > 0,
            '256*6*(36n+3)-6*(36(n+1)+3) has positive coefficients')
    require(109-220//2 == -1 and 220 % 2 == 0,
            'At the sufficient accuracy threshold the repair exponent is exactly -N')
    require(2*2**108 <= 2**109, 'Two summands can be absorbed by one extra exponent for Y >= 2')
    require(6*2 <= 256**2 and 2 <= 256,
            'The n=1 threshold and induction ratio give 256^-(n+1) <= 1/(6*2^n)')
    return {
        'affine_exponent_gaps': {k: {'slope': v[0], 'constant': v[1]} for k, v in gaps.items()},
        'coefficient_mass_rational_examples': coefficient_examples,
        'square_root_majorant_squared': {'27': 27, '36': 36},
        'induction_step_difference_coefficients': list(induction_difference),
        'C_star_times_theta_exact': 220,
        'threshold_exponent_after_substitution': '-(n+1)',
        'whole_word_largest_degree': '162n+20',
        'scope': 'Exact exponent identities and rational sufficient majorants only. V_H is symbolic; no exponential Vandermonde inverse or actual enormous interpolation constant is evaluated.'}


def clock_constant_checks() -> dict:
    elo, ehi = exp_one_interval()
    require(F(8, 3) < elo < ehi < F(11, 4), 'The Taylor enclosure certifies elementary bounds on e')
    slo, shi = 1/ehi, 1/elo
    numerator_lo = log_interval((1-slo/2)/(1-slo))[0]
    numerator_hi = log_interval((1-shi/2)/(1-shi))[1]
    denominator_lo = log_interval(8/(1-slo))[0]
    denominator_hi = log_interval(8/(1-shi))[1]
    theta = numerator_lo/denominator_hi, numerator_hi/denominator_lo
    require(0 < theta[0] <= theta[1] < 1, 'The adaptive-clock theta is strictly positive and below one')
    cstar = 220/theta[1], 220/theta[0]
    fixed_examples = []
    for s in (F(1, 4), F(1, 8), F(1, 64), F(1, 1024)):
        require(s <= slo, 'Each chosen epsilon equals e^-u for some u >= 1')
        v = s/(2*(1-s))
        loglo, loghi = log_interval(1+v)
        require(v/(1+v) <= loglo <= loghi <= v,
                'The rational logarithm enclosure verifies both standard log(1+v) bounds')
        require(v/(1+v) >= s/2 and v <= s/(2*(1-shi)),
                'The fixed-clock numerator majorants have the prescribed epsilon dependence')
        dlow, dhigh = log_interval(8/(1-s))
        fixed_examples.append({'epsilon_exact': str(s),
                               'theta_certified_interval': short_interval((loglo/dhigh, loghi/dlow))})
    return {'method': 'Exact factorial tail for e and exact atanh-series geometric tails for logarithms; outward rational reporting, no binary floating point.',
            'e_certified_interval': short_interval((elo, ehi)),
            'theta_star_certified_interval': short_interval(theta),
            'C_star_certified_interval': short_interval(cstar),
            'fixed_clock_examples': fixed_examples,
            'scope': 'The constant enclosures and listed epsilon cases are certified. The universal fixed-clock asymptotic claim and all protocol quantifiers remain analytic statements in the note.'}


def width_checks() -> dict:
    forward = []
    for x in (F(0), F(1, 2), F(199, 100), F(2), F(201, 100), F(3), F(17, 4), F(10)):
        if x >= 2:
            n = x.numerator//x.denominator-1
            require(n >= 1 and n+1 <= x and n >= x-2,
                    'The selected width is admissible and both floor bounds hold')
            forward.append({'x_exact': str(x), 'branch': 'selected target width', 'n': n})
        else:
            require(0 <= x < 2 and 2**3 < 20**4,
                    'The small-x branch uses the histogram, with 2^(3/4) < 20 exactly')
            forward.append({'x_exact': str(x), 'branch': 'twenty-state histogram'})
    inverse_examples = []
    for d in (2, 3, 19, 20, 64, 1000, 2**24, 2**48, 2**96):
        n = 1
        while 2**(3*2**n) <= d**4:
            n += 1
        require(2**(3*2**n) > d**4 and (n == 1 or 2**(3*2**(n-1)) <= d**4),
                'Integer powers certify the strict inverse-width threshold and its previous-width boundary')
        inverse_examples.append({'state_budget': d, 'n_D': n,
                                 'strict_threshold_check': '2^(3*2^n_D) > D^4',
                                 'histogram_excludes_rival': d < 20})
    return {'forward_crossover_cases': forward, 'inverse_width_cases': inverse_examples,
            'inverse_method': 'Find the least n>=1 with 2^(3*2^n)>D^4. By monotonicity of logarithms this equals floor(log2((4/3)*log2(D)))+1, including equality boundaries.',
            'scope': 'Finite exact floor/crossover examples and an integer-power reformulation; no enormous target state space is allocated.'}


def palindrome_resolvent_checks() -> dict:
    n, ident = 3, eye(3)
    refresh = [[F(1, 3)]*3 for _ in range(3)]
    generator = add(refresh, ident, F(-1))
    resolvent = inverse(add(ident, generator, F(-1)))
    require(resolvent == add(times(ident, F(1, 2)), times(refresh, F(1, 2))),
            'The exact reversible resolvent is one half identity plus one half stationary refresh')
    require(all(x >= 0 for row in resolvent for x in row) and all(sum(row) == 1 for row in resolvent),
            'The resolvent is an entrywise nonnegative stochastic matrix')
    resolvent_minors = psd_principal_minors(resolvent)
    d0 = [[F(i == j and i < 2) for j in range(n)] for i in range(n)]
    d1 = [[F(i == j and i > 0) for j in range(n)] for i in range(n)]
    b = mm(d0, resolvent)
    even = mm(mm(mm(mm(d0, resolvent), d1), resolvent), d0)
    odd = mm(mm(mm(mm(mm(mm(d0, resolvent), d1), resolvent), d1), resolvent), d0)
    require(even == mm(mm(b, d1), transpose(b)), 'The even palindrome is exactly B D B*')
    central = mm(mm(d1, resolvent), d1)
    require(odd == mm(mm(b, central), transpose(b)), 'The odd palindrome is exactly B (D S D) B*')
    psd_principal_minors(even)
    psd_principal_minors(central)
    psd_principal_minors(odd)
    a = [[F(1), F(1, 2), F(0)], [F(1, 2), F(1), F(0)], [F(0), F(0), F(1)]]
    sandwich = times(mm(mm(a, odd), a), F(7, 3))
    psd_principal_minors(sandwich)
    flip = [[F(0), F(1), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(1)]]
    v, mu = [F(1), F(-1), F(0)], [F(1, 3)]*3
    require(mv(flip, v) == [-x for x in v], 'The literal involution has a negative eigenvector')
    flip_scalar = inner(v, mv(flip, v), mu)
    candidate_scalar = inner(v, mv(sandwich, v), mu)
    require(flip_scalar == -norm2(v, mu) and candidate_scalar >= 0 and
            candidate_scalar-flip_scalar >= norm2(v, mu),
            'A positively normalized palindromic resolvent sandwich cannot match the negative involution scalar')
    return {'matrix_dimension': n, 'resolvent_exact': [[str(x) for x in row] for row in resolvent],
            'resolvent_principal_minors_exact': list(map(str, resolvent_minors)),
            'palindrome_edge_counts': [2, 3],
            'even_factorization': 'B D B*', 'odd_factorization': 'B (D S D) B*',
            'positive_sandwich_scale_exact': '7/3',
            'probe_norm_squared_exact': str(norm2(v, mu)),
            'involution_probe_scalar_exact': str(flip_scalar),
            'replacement_probe_scalar_exact': str(candidate_scalar),
            'scope': 'Exact 3x3 examples certify both parity factorizations, a positive resolvent and the negative-involution obstruction. They concern the literal PSD replacement route, not all possible uncapped constructions.'}


def whole_word_repair_checks() -> dict:
    labels = list(itertools.product((-1, 1), repeat=2))
    r, n = 2, 5
    epsilon, delta = F(1, 128), F(1, 128**2)
    tau = delta/8
    s = [F(bits[0]) for bits in labels]+[F(0)]
    records = []
    for amplitude in (16, 1000, 1000000):
        # Shrinking the fifth state's mass leaves all measured defects small
        # while the exact L2 operator norm grows with amplitude.
        weight = delta/(4*(amplitude-1)**2)
        mu = [(1-weight)/4]*4+[weight]
        one = [F(1)]*n
        queries, flips = [], []
        for bit in range(r):
            query, flip = [[F(0)]*n for _ in range(n)], [[F(0)]*n for _ in range(n)]
            for i, bits in enumerate(labels):
                query_bits = bits if bit == 0 else tuple(reversed(bits))
                flipped_bits = tuple(-x if j == bit else x for j, x in enumerate(bits))
                query[i][labels.index(query_bits)] = 1+tau
                flip[i][labels.index(flipped_bits)] = 1
            query[4][4] = flip[4][4] = F(amplitude)
            queries.append(query)
            flips.append(flip)
        vectors = [mv(q, s) for q in queries]
        clipped = [[max(F(-1), min(F(1), x)) for x in v] for v in vectors]
        require(any(v != h for v, h in zip(vectors, clipped)), 'Endpoint clipping is nontrivial')
        require(epsilon <= F(1, 32*r) and epsilon**2 == delta,
                'The whole-word entropy small-defect threshold is met exactly')
        for q, v in zip(queries, vectors):
            require(norm2([x-1 for x in mv(q, one)], mu) <= delta and abs(norm2(v, mu)-1) <= delta,
                    'Query row defects and signed-vector norms meet the exact lemma hypotheses')
        repaired_kernels, largest_flux_error, largest_corner_norm = [], F(), F()
        for c, raw in enumerate(flips):
            star = adjoint(raw, mu)
            require(raw == star, 'The example whole flip kernel has its exact stationary adjoint')
            require(norm2([x-1 for x in mv(raw, one)], mu) == delta/4 and
                    norm2([x-1 for x in mv(star, one)], mu) == delta/4,
                    'Both whole-kernel row defects remain small with no norm cap assumption')
            fixed = flux_repair(raw, mu)
            repaired_kernels.append(fixed)
            for b, (v, h) in enumerate(zip(vectors, clipped)):
                sign = F(-1 if b == c else 1)
                require(norm2(mv(raw, v), mu) <= 1+delta and sign*inner(v, mv(raw, v), mu) >= 1-delta,
                        'All additional measured image norms and signed lamp correlations are certified')
                require(norm2(h, mu) >= 1-4*epsilon and sign*inner(h, mv(fixed, h), mu) >= 1-8*epsilon,
                        'The clipped and whole-word repaired kernels meet both lemma conclusions')
            difference = add(raw, fixed, F(-1))
            flux_error = sum((mu[i]*abs(difference[i][j]) for i in range(n) for j in range(n)), F())
            require(flux_error <= 3*epsilon, 'Whole-kernel stationary flux repair obeys the L1 estimate')
            corners = itertools.product((F(-1), F(1)), repeat=n)
            max_corner_norm = max(norm2(mv(difference, list(f)), mu) for f in corners)
            require(max_corner_norm == delta/4,
                    'All 32 corners give the exact infinity-to-L2 norm squared of the repair difference')
            x = epsilon/2
            require(x*x == max_corner_norm and x*x <= 6*epsilon+epsilon*x,
                    'The general cap-free repair quadratic inequality holds with an exact rational norm')
            # This is an exact norm certificate, not a hypothesis of the repair test.
            gram = [[sum((mu[k]*raw[k][i]*raw[k][j] for k in range(n)), F()) for j in range(n)] for i in range(n)]
            cap_certificate = [[(amplitude**2*mu[i] if i == j else 0)-gram[i][j] for j in range(n)] for i in range(n)]
            require(all(cap_certificate[i][j] == 0 for i in range(n) for j in range(n) if i != j)
                    and all(cap_certificate[i][i] >= 0 for i in range(n)),
                    'A diagonal quadratic-form certificate bounds the actual raw L2 norm by the amplitude')
            spike = [F(0)]*4+[F(1)]
            require(norm2(mv(raw, spike), mu) == amplitude**2*norm2(spike, mu),
                    'The small-mass fifth state attains that growing norm exactly')
            largest_flux_error = max(largest_flux_error, flux_error)
            largest_corner_norm = max(largest_corner_norm, max_corner_norm)
        rounded = [[F(1) if x >= 0 else F(-1) for x in h] for h in clipped]
        largest_bit_failure = F()
        for c, fixed in enumerate(repaired_kernels):
            for b in range(r):
                sign = -1 if b == c else 1
                failure = sum((mu[i]*fixed[i][j] for i in range(n) for j in range(n)
                               if rounded[b][j] != sign*rounded[b][i]), F())
                require(failure <= 8*epsilon, 'Rounded-bit mismatch obeys the stated coupling bound')
                largest_bit_failure = max(largest_bit_failure, failure)
        require(n**4 >= 2**(3*r), 'The finite example has enough states for the concluded entropy bound')
        records.append({'raw_L2_operator_norm_exact': str(amplitude),
                        'small_stationary_mass_exact': str(weight),
                        'query_main_block_scale_exact': str(1+tau),
                        'largest_stationary_flux_repair_error_exact': str(largest_flux_error),
                        'repair_infinity_to_L2_norm_squared_exact': str(largest_corner_norm),
                        'largest_rounded_bit_failure_exact': str(largest_bit_failure)})
    return {'states': n, 'bits': r, 'epsilon_exact': str(epsilon), 'Delta_exact': str(delta),
            'bounded_feature_corners_per_kernel': 2**n, 'examples': records,
            'scope': 'Five-state algebraic examples satisfy every whole-word lemma hypothesis with nontrivial clipping and arbitrarily scalable raw norms through a small-mass state. They are proof-kernel examples, not physical rivals or a cap-free observable-transfer theorem.'}


def same_state_poisson_capping_checks() -> dict:
    mu, gamma = [F(1, 4), F(1, 4), F(1, 2)], F(1, 10)
    labels = [-gamma, -gamma, gamma]
    refresh = [mu.copy() for _ in mu]
    ident = eye(3)
    require(mm(refresh, refresh) == refresh and adjoint(refresh, mu) == refresh,
            'The hidden refresh is an exact stationary orthogonal projection')
    # K=(log 2)(Pi-I), Delta=1.  Projection functional calculus gives
    # exp(K)=Pi+(I-Pi)/2.  Only its exact rational value is represented here.
    exp_k = times(add(ident, refresh), F(1, 2))
    capped = add(exp_k, ident, F(-1))
    require(capped == times(add(refresh, ident, F(-1)), F(1, 2)),
            'The projection formula gives the exact Poisson-capped generator')
    require(mv(capped, [F(1)]*3) == [F(0)]*3 and adjoint(capped, mu) == capped,
            'Same-state capping preserves conservation and exact detailed balance')
    require(all(capped[i][j] > 0 for i in range(3) for j in range(3) if i != j)
            and max(-capped[i][i] for i in range(3)) <= 1,
            'The capped chain is irreducible and respects the 1/Delta exit bound')
    require(sum((p*g for p, g in zip(mu, labels)), F()) == 0 and
            sum((p for p, g in zip(mu, labels) if g == gamma), F()) == F(1, 2),
            'The same three states retain the balanced binary histogram exactly')
    log2_lower, _ = log_interval(F(2))
    require(log2_lower > F(1, 2), 'Capping strictly reduces this nonzero internal gap')
    pi = [F(1, 2)]+[p/2 for p in mu]
    visible = [F(-1), F(1), F(1), F(1)]
    stationary_projector = [pi.copy() for _ in pi]
    visible_projector = [[visible[i]*pi[j]*visible[j] for j in range(4)] for i in range(4)]
    hidden_projector = [[F(0)]*4 for _ in range(4)]
    for i in range(3):
        for j in range(3):
            hidden_projector[i+1][j+1] = F(i == j)-mu[j]
    projectors = [stationary_projector, visible_projector, hidden_projector]
    require(add(add(projectors[0], projectors[1]), projectors[2]) == eye(4),
            'Stationary, visible and hidden-centered projections span the full physical state space')
    for i, left in enumerate(projectors):
        require(adjoint(left, pi) == left, 'Every projection is selfadjoint in the correct stationary geometry')
        for j, right in enumerate(projectors):
            require(mm(left, right) == (left if i == j else [[F(0)]*4 for _ in range(4)]),
                    'The three physical subspaces are exact mutually orthogonal projection ranges')
    q_constant, q_slope = [[F(0)]*4 for _ in range(4)], [[F(0)]*4 for _ in range(4)]
    q_constant[0] = [F(-1)]+mu
    for i in range(3):
        q_constant[i+1][0] = 1
        q_constant[i+1][i+1] = -1
        for j in range(3):
            q_slope[i+1][j+1] = mu[j]-F(i == j)
    require(q_constant == add(times(visible_projector, F(-2)), times(hidden_projector, F(-1)))
            and q_slope == times(hidden_projector, F(-1)),
            'Q(lambda)=-2 P_visible-(1+lambda) P_hidden holds coefficient by coefficient')
    full_capped = add(q_constant, q_slope, F(1, 2))
    require(adjoint(full_capped, pi) == full_capped and mv(full_capped, [F(1)]*4) == [F(0)]*4,
            'The four-state capped physical zero-field generator is reversible and conservative')
    field_examples = []
    for base in (F(1), F(11, 10), F(10, 11)):
        # h=10 log(base), so every external field factor is exactly rational.
        tilt = base**20
        pih = [1/(1+tilt)]+[tilt*p/(1+tilt) for p in mu]
        external_az = [p*base**int(10*(1+g)) for p, g in zip(mu, labels)]
        external_za = [base**int(10*(g-1)) for g in labels]
        require(all(pih[0]*external_az[i] == pih[i+1]*external_za[i] for i in range(3)),
                'The unchanged original field rule has exact external detailed balance after capping')
        require(all(pih[i+1]*capped[i][j] == pih[j+1]*capped[j][i]
                    for i in range(3) for j in range(3)),
                'Capped internal detailed balance holds at the same field stationary law')
        field_examples.append({'exp_h_over_10_exact': str(base),
                               'A_to_hidden_rates_exact': list(map(str, external_az)),
                               'hidden_to_A_rates_exact': list(map(str, external_za))})
    return {'hidden_states_before_and_after': 3, 'total_physical_states_before_and_after': 4,
            'mu_exact': list(map(str, mu)), 'actuator_labels_exact': list(map(str, labels)),
            'Delta_exact': '1', 'original_internal_rate_symbol': 'log(2)', 'capped_internal_rate_exact': '1/2',
            'capped_hidden_generator_exact': [[str(x) for x in row] for row in capped],
            'zero_field_spectral_identity': 'Q(lambda) = -2 P_visible - (1+lambda) P_hidden',
            'semigroup_difference_identity': 'T_capped(u)-T_original(u) = exp(-u) [exp(-u/2)-exp(-u log(2))] P_hidden',
            'field_examples': field_examples,
            'scope': 'Projection functional calculus and exact rational 3x3/4x4 identities certify this same-state Poisson transformation, preserved histogram/rule, and the extra zero-field exp(-u) factor. They do not verify the general driven all-horizon Volterra estimate or its asymptotic cap law.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/state_speed_boundary.json'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    proof_sources = [root/'docs/STATE_SPEED_ACCURACY_TRADEOFF.md',
                     root/'docs/UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md',
                     root/'docs/RATE_REGULARIZATION.md']
    report = {
        'status': 'PASS', 'versions': {'python': platform.python_version()},
        'arithmetic': 'Python standard-library fractions.Fraction; no numerical rank or floating-point matrix operations',
        'uniform_cap_bookkeeping': uniform_bookkeeping_checks(),
        'clock_constants': clock_constant_checks(), 'width_selection_and_crossover': width_checks(),
        'PSD_palindromes_and_resolvent_obstruction': palindrome_resolvent_checks(),
        'whole_word_repair_without_norm_cap': whole_word_repair_checks(),
        'same_state_poisson_capping': same_state_poisson_capping_checks(),
        'largest_matrix_dimension': 5, 'physical_target_matrix_allocated': False,
        'limitations': ['Finite examples and symbolic exponent identities do not prove the complete all-n, all-model, all-protocol analytic theorems.',
                       'No actual exponential interpolation inverse or numerical value of V_H is computed.',
                       'No cap-free recovery of raw generator-word scalars from mean accuracy is established.',
                       'The Poisson fixture certifies only the displayed small projection example, not the general controlled all-horizon regularization theorem.'],
        'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        'proof_snapshot_sha256': {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in proof_sources},
        'imported_repository_verifiers': [],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
