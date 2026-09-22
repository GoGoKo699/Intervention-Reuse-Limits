# Intervention Reuse Limits

**When does a perfect passive model remain useful after an intervention?**

This theory-first project studies finite-state stochastic dynamics. A system can have an exact two-state description when left alone, while hidden kinetic modes become visible in its nonlinear response. The objective is to characterize what a reusable model must retain, and how that requirement changes when exact equality is replaced by a specified accuracy.

**Research status:** the project now has a finite-field prediction theorem, an operational measurement separation, and a quantitative result near imperfect lumpability. The main new bound concerns actual driven means, and one fixed nonzero step already gives the matching lower order. The target actuator subclass and the statistical experiment are specified below. Originality of the combined results remains under assessment; manuscript writing remains on hold.

## Stronger prediction and observation results

**Actual finite-field prediction.** In a specified subclass, exactly one hidden state has sensitivity $+\sqrt W$ and stationary mass $1/2$; all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel has such a reversible realization. For any fixed field bound $H>0$, one reduced Markov model must predict the actual binary mean under every protocol $|h(t)|\le H$, at every time. The sharp worst-case state orders are

| Target spectrum | States for exact-mean error at most $\delta$ |
|---|---|
| Unrestricted active rates | $\Theta(\log^2(1/\delta))$ |
| Active rates at most $3k$ | $\Theta(\log(1/\delta))$ |

The upper construction preserves reversibility, bounded sensitivity, and the entire passive law. The lower bound allows arbitrary finite-state Markov competitors, with no analytic field dependence or passive matching requirement. In the unrestricted case, a **single fixed nonzero step amplitude**, independent of tolerance and state budget, already forces the lower order. See [the finite-field theorem](docs/FINITE_FIELD.md) and [the fixed-step proof](docs/FIXED_FIELD_LOWER_BOUND.md). The guarantee has no Taylor-remainder floor. The actuator restriction is substantive: outside it, identical cubic kernels can give different higher-order responses.

**Two measurements can reveal what the mean misses.** In the broader original family, the complete passive path law and every first-order visible-path response agree with a two-state reference. The second-order path response determines the hidden kernel and can require arbitrarily many states. For a concrete pair of three-state models, retaining the initial and final visible states needs $\Theta(h^{-4})$ independent weak-step trials to distinguish them; retaining only the final state needs $\Theta(h^{-6})$. These are [specified two-hypothesis experiments](docs/ACTIVE_PATH_RESPONSE.md), with no hidden-state access or continuous monitoring required for the stronger exponent.

**Imperfect lumpability has a quantitative information cost.** Small centered changes of the external equilibrium conductances, of relative size $q$, break exact passive lumpability. Nevertheless, the full stationary passive-path relative entropy from the two-state reference is bounded by $q^4(152+241kT)$, independently of hidden dimension and internal rates. A three-state pair attains the quartic information scale while retaining a nonzero finite-field driven signal. The [robustness theorem](docs/NEAR_LUMPABILITY.md) specifies the allowed barrier perturbations and the observation/preparation costs.

## Cubic-response foundations

**Exact separation.** For every $N\ge3$, a reversible $N$-state model has exactly the same complete passive binary path law, static response curve, and dynamic linear mean response as a two-state reference, but its exact cubic step response requires at least $N$ states in an analytic autonomous Markov surrogate. The separation can be maintained with bounded field coupling and a nonvanishing total cubic correction.

**Finite-accuracy reuse.** Within the constructed family, a scalar kinetic kernel determines the cubic mean response to every bounded weak-field protocol. For kernel mass $W$, protocol bound $U$, and any positive integer $n$, a positive-quadrature construction and reversible realization give a surrogate with at most $2n(n+1)+3$ states and cubic-coefficient error

$$
\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|\le8U^3W\,16^{-n}
$$

for every finite horizon and every admissible protocol, independently of the original state count and hidden spectral range. Thus a tolerance $\varepsilon$ needs at most order $\log^2(1/\varepsilon)$ states at fixed $W,U$. The earlier $U^3W/q$ midpoint certificate remains available. Classical quadrature supplies the upper bound; the lower bound below establishes its worst-case state-growth order, without claiming sharp constants or new approximation theory.

**Exact realization of a known kernel.** A kernel with $r$ distinct positive exponential modes has an explicit reversible realization with $r+2$ total states and sensitivity magnitude $\sqrt W$. When no hidden decay rate equals $k$, this meets the exact pole-location lower bound. The construction is a corollary of finite Jacobi inverse spectral theory.

**Finite-accuracy lower bounds.** Two cubic step-response samples of a three-state target force error at least $0.062546\,WU^3$ against every admissible two-state surrogate. For arbitrary state budgets, geometrically separated hidden rates give a matching obstruction through a weighted Hankel operator of the cubic step response. The proof allows nonreversible surrogates and unrestricted field derivatives. Combined with the upper bounds:

| Target information, at fixed positive $W,U$ | Necessary states | Sufficient states |
|---|---|---|
| No common bound on active hidden rates | $\Omega(\log^2(1/\varepsilon))$ | $O(\log^2(1/\varepsilon))$ |
| Active hidden rates at most $3k$ | $\Omega(\log(1/\varepsilon))$ | $O(\log(1/\varepsilon))$ |

The second row adds information about the target; it leaves the broad surrogate class unchanged and assumes no lower bound on the hidden spectral gap. These are asymptotic coefficient-tolerance results, with conservative constants. The unrestricted lower bound already holds for targets whose slowest active rate is $5k/2$: access to increasingly fast hidden modes causes the additional worst-case cost. A finite-horizon version uses the step-response curve only up to time $O(\sqrt D/k)$ for a tested budget of $D$ states; it is not a claim about finitely many noisy measurements.

**Preserving structure at the optimal order.** The same two state-growth orders hold even for stationary analytic Markov competitors that are judged only on the cubic coefficient and may abandon passive, static, linear, and quadratic matching. Our reversible construction retains all those agreements and the sensitivity bound at that same asymptotic order. The [comparison proof](docs/STRUCTURE_COST.md) does not claim equal errors at a fixed state budget or equal leading constants.

**The distinction matters:** exact response complexity can grow without bound even at nonvanishing signal strength; that does not imply an equally large state requirement at fixed accuracy. The approximation requires intervention-relevant information that cannot be obtained from the passive binary process alone.

The [switch-off example](docs/PUBLICATION_SCOPE.md#3-a-diagnostic-boundary-switching-the-field-off-versus-keeping-it-on) gives a separate diagnostic boundary: all targets have the same relaxation after a stationary field is switched off, even at finite field strength, yet their field-on response can differ. The intended compression task starts from a supplied kinetic model; the measurement results separately ask what visible data can distinguish.

## Read and inspect

| Question | Document |
|---|---|
| What is proved for actual finite-field predictions? | [Uniform finite-field theorem](docs/FINITE_FIELD.md) |
| Does one fixed intervention already require growing model size? | [Fixed nonzero step lower bound](docs/FIXED_FIELD_LOWER_BOUND.md) |
| What can two visible measurements reveal? | [Path response and statistical separation](docs/ACTIVE_PATH_RESPONSE.md) |
| Does the distinction survive imperfect passive lumpability? | [Quartic passive information and robustness](docs/NEAR_LUMPABILITY.md) |
| What is the candidate contribution, and how does it compare with prior theorems? | [Publication scope and operational interpretation](docs/PUBLICATION_SCOPE.md) |
| What is the model, and where is the exact proof? | [Core theory and three-state example](docs/THEORY.md) |
| What survives at nonzero error tolerance? | [Nonvanishing signal, approximation bound, and Markov realization](docs/FINITE_ACCURACY.md) |
| Why is the squared-logarithmic state count necessary? | [Unrestricted-rate lower bound](docs/UNRESTRICTED_RATE_LOWER_BOUND.md) |
| Does preserving the physical structure increase the asymptotic state cost? | [Relaxed and structure-preserving comparison](docs/STRUCTURE_COST.md) |
| What is already known, and what remains to be checked? | [Prior-art and novelty audit](docs/PRIOR_ART.md) |
| What was actually tested? | [Verification scope and provenance](docs/VERIFICATION.md) |
| What is the next research task? | [Current work order](work_orders/CURRENT.md) |

The preserved [checkpoint verifier](scripts/verify_checkpoint.py) and [finite-accuracy verifier](scripts/verify_finite_accuracy.py) remain regression baselines. Extensions check [positive quadrature](scripts/verify_quadrature.py), [minimal reversible realization](scripts/verify_minimal_realization.py), [finite-sample response lower bounds](scripts/verify_response_lower_bounds.py), [unrestricted-rate lower bounds](scripts/verify_unrestricted_rate_lower_bound.py), [finite-field identities](scripts/verify_finite_field.py), and [path information](scripts/verify_path_information.py). Their generated evidence is in [reports](reports).

## Reproduce

Use Python 3.13; the saved local run used 3.13.5. Dependencies are pinned to the tested environment in [requirements.txt](requirements.txt).

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make check
```

Without Make:

```bash
python scripts/check_repository.py
mkdir -p .check-output
python scripts/verify_checkpoint.py --output .check-output/checkpoint.json
python scripts/verify_finite_accuracy.py --output .check-output/finite_accuracy.json
python scripts/verify_quadrature.py --output .check-output/quadrature.json
python scripts/verify_minimal_realization.py --output .check-output/minimal_realization.json
python scripts/verify_response_lower_bounds.py --output .check-output/response_lower_bounds.json
python scripts/verify_unrestricted_rate_lower_bound.py --output .check-output/unrestricted_rate_lower_bound.json
python scripts/verify_finite_field.py --output .check-output/finite_field.json
python scripts/verify_path_information.py --output .check-output/path_information.json
```

A failed assertion exits unsuccessfully. Fresh reports go into the ignored `.check-output` directory; the saved reports are not overwritten. Numerical roundoff can differ across platforms. Dependency installation and GitHub Actions setup require network access; the verification calculations themselves do not.

The checks use symbolic algebra, exact rational calculations, and small deterministic matrices. There are no sampled trajectories, trained models, large fluid simulations, or external datasets. The [workflow](.github/workflows/verify.yml) runs the same checks on pushes and pull requests; its live status is separate from the saved local reports.

## Scope and attribution

The coefficient theorems cover the original centered-sensitivity family; the finite-field upper theorem covers the explicitly defined rank-one sensitivity subclass. The finite-field norm measures single-time means, not approximate full path distributions. The statistical results concern specified hypotheses and records, not recovery of an arbitrary unknown generator. State counts do not measure bits, parameter precision, runtime, or experimental resolution. No turbulence or generic molecular implementation claim is made.

Nonlinear response, aggregated Markov inference from dwell times, minimal realization, positive model reduction, and Hankel dimension witnesses are established subjects. The [audit](docs/PRIOR_ART.md) and [publication scope](docs/PUBLICATION_SCOPE.md) distinguish those ingredients from the new combined claims. Demanding the correct passive law does not cause the approximation lower bound: it already applies to competitors without that requirement.

Manuscript writing is on hold while the novelty and significance questions are resolved. Research contact: **Ruge Lin**, [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's existing license is unchanged. Linked third-party papers retain their own copyrights and licenses; their text and figures are not redistributed here.
