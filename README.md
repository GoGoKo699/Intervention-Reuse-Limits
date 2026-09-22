# Intervention Reuse Limits

**When does a perfect passive model remain useful after an intervention?**

This theory-first project studies finite-state stochastic dynamics. A system can have an exact two-state description when left alone, while hidden kinetic modes become visible in its nonlinear response. The objective is to characterize what a reusable model must retain, and how that requirement changes when exact equality is replaced by a specified accuracy.

**Research status:** the general-family state cost is now proved to exceed every fixed power of the logarithm of the inverse error. This already happens with two sensitivity values, a bounded internal rate band, and a fixed minimum control dwell time. A complementary upper theorem supplies reversible approximants preserving the exact sensitivity variance, but the quantitative gap remains large. Originality of the combined results remains under assessment; manuscript writing remains on hold.

## Main result: driven predictions can require many more states

An exact two-state passive model does not bound the cost of predicting the same binary mean under an applied field. At fixed $k,G,W,H$, the [general controlled lower bound](docs/GENERAL_CONTROLLED_LOWER_BOUND.md) proves that worst-case mean error $\delta$ requires at least

$$
D_*(\delta)\ge c\exp\!\left(c\sqrt{\log(1/\delta)}\right)
$$

physical Markov states for sufficiently small $\delta$. This grows faster than every fixed power of $\log(1/\delta)$. The targets are reversible, use only $g=\pm\sqrt W$, and have all internal relaxation rates in $[k,3k]$. The lower bound allows arbitrary Markov competitors with fixed readout and preparation. Its controls use only $0$ and one fixed nonzero field, with every nonzero held interval at least $1/(8k)$.

The same construction gives an exact comparison:

$$
D_{\mathrm{cubic}}=n+3,
\qquad 2^n\le D_{\mathrm{full\ controlled}}\le2^{n+1}+1.
$$

Here the cubic minimum uses the established analytic-in-field competitor class; the full controlled lower bound permits broader Markov competitors. Thus a small model that reproduces every cubic response can still require exponentially more states to reproduce actual controlled means. The finite-error theorem separately quantifies this obstruction; it does not follow merely from exact rank.

Compression nevertheless remains possible throughout the bounded-sensitivity family. The [reversible general upper bound](docs/REVERSIBLE_GENERAL_COMPRESSION.md) constructs one predictor for all allowed protocols and horizons, within the original model family: reversibility, the sensitivity bound, variance $W$, passive law, equilibrium curve, and linear/quadratic mean agreements are retained exactly. Its sufficient count is

$$
D(\delta)\le\exp\!\left\{\exp\!\left[C_{G,H}\log^2(16/\delta)\right]\right\}.
$$

This double-exponential upper bound and the lower bound are far apart. The optimal general-family state order, and any additional optimal cost of preserving reversibility, remain open. Both results concern a supplied microscopic model; neither is a learning algorithm or an experimental sample bound.

## A sharp subclass and operational results

**Actual finite-field prediction.** In a specified subclass, exactly one hidden state has sensitivity $+\sqrt W$ and stationary mass $1/2$; all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel has such a reversible realization. For any fixed field bound $H>0$, one reduced Markov model must predict the actual binary mean under every protocol $|h(t)|\le H$, at every time. The sharp worst-case state orders are

| Target spectrum | States for exact-mean error at most $\delta$ |
|---|---|
| Unrestricted active rates | $\Theta(\log^2(1/\delta))$ |
| Active rates at most $3k$ | $\Theta(\log(1/\delta))$ |

The upper construction preserves reversibility, bounded sensitivity, and the entire passive law. The lower bound allows arbitrary finite-state Markov competitors, with no analytic field dependence or passive matching requirement. In the unrestricted case, a **single fixed nonzero step amplitude**, independent of tolerance and state budget, already forces the lower order. See [the finite-field theorem](docs/FINITE_FIELD.md) and [the fixed-step proof](docs/FIXED_FIELD_LOWER_BOUND.md). The guarantee has no Taylor-remainder floor. The actuator restriction is substantive: outside it, identical cubic kernels can give different higher-order responses.

**Two measurements can reveal what the mean misses.** In the broader original family, the complete passive path law and every first-order visible-path response agree with a two-state reference. The second-order path response determines the hidden kernel and can require arbitrarily many states. For a concrete pair of three-state models, retaining the initial and final visible states needs $\Theta(h^{-4})$ independent weak-step trials to distinguish them; retaining only the final state needs $\Theta(h^{-6})$. These are [specified two-hypothesis experiments](docs/ACTIVE_PATH_RESPONSE.md), with no hidden-state access or continuous monitoring required for the stronger exponent.

**Imperfect lumpability has a quantitative information cost.** Small centered changes of the external equilibrium conductances, of relative size $q$, break exact passive lumpability. Nevertheless, the full stationary passive-path relative entropy from the two-state reference is bounded by $q^4(152+241kT)$, independently of hidden dimension and internal rates. A three-state pair attains the quartic information scale while retaining a nonzero finite-field driven signal. The [robustness theorem](docs/NEAR_LUMPABILITY.md) specifies the allowed barrier perturbations and the observation/preparation costs.

## Beyond the scalar-kernel subclass

**No finite response hierarchy is universally complete, even with the actuator fixed.** For every $d\ge2$, two $d+2$-state models can share the same state labels, $k,\mu,g$, field-dependent external rates, and one-mode kernel $C(t)=We^{-\lambda t}$. Changing only reversible hidden kinetics leaves every bounded-protocol mean coefficient through order $2d$ identical, and every visible-path coefficient through order $2d-1$ identical. The next orders differ, and their actual mean curves differ under every nonzero constant field. All hidden relaxation rates stay in $[\lambda,3\lambda/2]$. The [fixed-actuator hierarchy theorem](docs/FIXED_ACTUATOR_HIERARCHY.md) holds for any fixed $0<W<G^2$; the common actuator and state space may change with $d$. This is exact incompleteness, not a noise-robust separation or a finite-error state lower bound.

**The complete path information has an exact description.** For the general family, equality of all controlled visible path laws is equivalent to equality in law of the stationary hidden sensitivity process $Y_t=g(X_t)$. Short-pulse no-exit functionals recover its joint Laplace transforms in principle. The [actuator-process theorem](docs/ACTUATOR_PROCESS.md) also gives a matrix-return closure for finitely many distinguished actuator states. Two sensitivity levels alone are insufficient for two-time closure: an explicit pair has identical two-time level kernels but different finite-field means. Necessity from mean data alone is not established.

**Reversibility and exact variance can be retained.** The [general reversible construction](docs/REVERSIBLE_GENERAL_COMPRESSION.md) partitions the target using finitely many prediction functions, averages reversible transitions, and uses at most two sensitivity replicas per cell to restore the original variance. A truncated controlled expansion improves its sufficient count to the double-exponential bound above. The [earlier finite-word construction](docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md) remains as a preliminary existence proof and source of shared estimates; its nonreversibility and variance error are no longer limitations of the best available upper theorem.

These results separate three questions: which intervention data are complete, whether fixed-accuracy compression exists, and how many physical states it optimally costs. A finite response hierarchy can fail the first question without making the second impossible.

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
| Why does the general state cost exceed every power of the logarithm? | [Binary-tree controlled lower bound](docs/GENERAL_CONTROLLED_LOWER_BOUND.md) |
| Can approximation preserve reversibility and exact variance? | [General reversible compression](docs/REVERSIBLE_GENERAL_COMPRESSION.md) |
| Where is the finite-field state order sharp? | [Uniform finite-field theorem for the rank-one subclass](docs/FINITE_FIELD.md) |
| Does one fixed intervention already require growing model size? | [Fixed nonzero step lower bound](docs/FIXED_FIELD_LOWER_BOUND.md) |
| Can arbitrarily many response orders agree with the actuator fixed? | [Fixed-actuator response hierarchy](docs/FIXED_ACTUATOR_HIERARCHY.md) |
| What replaces the scalar kernel for complete driven path laws? | [Stationary actuator process and matrix-return closure](docs/ACTUATOR_PROCESS.md) |
| What was the first general existence construction? | [Finite-word bounded-sensitivity upper bound](docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md) |
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

The preserved [checkpoint verifier](scripts/verify_checkpoint.py) and [finite-accuracy verifier](scripts/verify_finite_accuracy.py) remain regression baselines. Extensions check [positive quadrature](scripts/verify_quadrature.py), [minimal reversible realization](scripts/verify_minimal_realization.py), [finite-sample response lower bounds](scripts/verify_response_lower_bounds.py), [unrestricted-rate lower bounds](scripts/verify_unrestricted_rate_lower_bound.py), [finite-field identities](scripts/verify_finite_field.py), [path information](scripts/verify_path_information.py), [the actuator hierarchy](scripts/verify_actuator_hierarchy.py), [general compression identities](scripts/verify_general_compression.py), [reversible compression](scripts/verify_reversible_compression.py), and [the controlled general lower bound](scripts/verify_general_controlled_lower_bound.py). Their generated evidence is in [reports](reports).

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
python scripts/verify_actuator_hierarchy.py --output .check-output/actuator_hierarchy.json
python scripts/verify_general_compression.py --output .check-output/general_compression.json
python scripts/verify_reversible_compression.py --output .check-output/reversible_compression.json
python scripts/verify_general_controlled_lower_bound.py --output .check-output/general_controlled_lower_bound.json
```

A failed assertion exits unsuccessfully. Fresh reports go into the ignored `.check-output` directory; the saved reports are not overwritten. Numerical roundoff can differ across platforms. Dependency installation and GitHub Actions setup require network access; the verification calculations themselves do not.

The checks use symbolic algebra, exact rational calculations, and small deterministic matrices. There are no sampled trajectories, trained models, large fluid simulations, or external datasets. The [workflow](.github/workflows/verify.yml) runs the same checks on pushes and pull requests; its live status is separate from the saved local reports.

## Scope and attribution

The coefficient theorems cover the original centered-sensitivity family. The sharp finite-field state order applies to the specified rank-one subclass. For general actuators, the new lower bound exceeds every fixed power of the logarithm, while the much larger upper bound preserves the original reversible family and exact variance; their orders do not match. The finite-field approximation norm measures single-time means, while exact path equivalence is a separate theorem. The statistical results concern specified hypotheses and records, not recovery of an arbitrary unknown generator. State counts do not measure bits, parameter precision, runtime, or experimental resolution. No turbulence or generic molecular implementation claim is made.

Nonlinear response, aggregated Markov inference from dwell times, minimal realization, positive model reduction, and Hankel dimension witnesses are established subjects. The [audit](docs/PRIOR_ART.md) and [publication scope](docs/PUBLICATION_SCOPE.md) distinguish those ingredients from the new combined claims. Demanding the correct passive law does not cause the approximation lower bound: it already applies to competitors without that requirement.

Manuscript writing is on hold while the novelty and significance questions are resolved. Research contact: **Ruge Lin**, [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's existing license is unchanged. Linked third-party papers retain their own copyrights and licenses; their text and figures are not redistributed here.
