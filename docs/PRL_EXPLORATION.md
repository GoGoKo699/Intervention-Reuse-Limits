# PRL exploration: prediction states and stationary irreversibility

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Source comparison](PRL_EXPLORATION_SOURCE_AUDIT.md) · [Internal review](PRL_EXPLORATION_INTERNAL_REVIEW.md) · [Verification](VERIFICATION.md)

**Target decision, 23 September 2026.** The user selected *Physical Review Letters* as the target for a new exploration phase. Manuscript drafting remains the last step. This record sets the research direction and documents the first completed advances; it is not a manuscript, submission decision or prediction of acceptance.

The [official PRL criteria](https://journals.aps.org/prl/about), checked on this date, call for a significant physical advance through a new avenue, a critical problem, an impactful method or unusual broad interest. Our working test is whether the results expose a useful physical limitation on reusable stochastic models, beyond a technically stronger state-count construction.

## 1. Physical question

Can an equilibrium stochastic system require an irreversible reduced model if the reduced model must remain small and predict interventions accurately?

The targets are reversible finite-state systems. Their complete passive visible law has an exact two-state realization. Intervention exposes hidden information. The new results connect the cost of retaining that information to ordinary detailed balance and to the stationary entropy production of a predictor. The target itself remains at equilibrium at zero field; it is the reduced predictor whose irreversible currents are at issue.

All comparisons use one predictor for every allowed protocol and horizon, the original exponential field rule, stationary zero-field preparation and binary readout. State count includes every retained memory coordinate. The results concern a specified model class, not every possible physical implementation of prediction.

## 2. What this phase established

| Result | Advance | Scope that must remain visible |
|---|---|---|
| [Positive label selectors](POSITIVE_LABEL_SELECTORS.md) | Two physical fields recover positive approximate selectors for the target's nineteen actuator levels. | Rival labels may vary anywhere in the same bounded interval. Exact rival histogram matching is unnecessary. |
| [Tight-band fixed-clock separation](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) | The original target band remains $[k,3k]$, with no new target states or rate rescaling. Ordinary reversible prediction is superpolynomial while unrestricted prediction has a polynomial sufficient count. | Two fields and any fixed positive clock suffice; arbitrary finite rival rates and new states are permitted. The original kinetic field rule remains essential. |
| [Uniform entropy-production reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) | Replacing $K$ by $(K+K^*)/2$ preserves every state, label, stationary mass and exit rate, with an all-protocol, all-horizon mean-error bound. | The constant depends only on the external interface, with no hidden rate, dimension or minimum-mass factor. The result concerns endpoint responses, not entire long path distributions. |
| [State–entropy-production tradeoff](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) | Reversible state lower bounds extend to predictors with a bounded stationary entropy-production rate. Polynomial predictors can also be regularized to have finite entropy production. | The stronger quantitative frontier keeps the older common cap and exact histogram; it is separate from the broader uncapped frontier. Bounds are not matched. |

The two-field state comparison is

$$
D_{\rm all}^{(2,a)}(\delta)\le C\delta^{-p},\qquad
D_{\rm rev}^{(2,a)}(\delta)\ge
\exp\!\left(\exp\!\left(c_{a,H}[\log(1/\delta)]^{1/5}\right)\right).
$$

At target index $n$, accuracy $e^{-C(n+1)^5}$ forces at least $2^{3\cdot2^n/4}$ reversible states, witnessed by finite clock experiments of at most $C(n+1)^5$ ticks. No bound on experiment count, sample size or parameter precision follows. A separate thirty-nine-field corollary supplies polynomial unrestricted necessity on the same target family. A two-field matching unrestricted lower is not claimed.

For any original-rule stationary predictor with $|g|\le G$, let $R=e^{(1+G)H}$ and let $\sigma_0$ be its full zero-field stationary entropy-production rate in nats per unit time. The new bridge is

$$
\mathcal D_H(F,F_{\rm sym})\le
R^{3/2}\sqrt{\sigma_0/k},\qquad
D_{\le\Sigma}(\delta)\ge
D_{\rm rev}\!\left(\delta+R^{3/2}\sqrt{\Sigma/k}\right).
$$

Under the common exit cap $3k$ and exact nineteen-level histogram, this gives

$$
D_{\le\Sigma}(\delta)\ge
\exp\!\left(c[\delta+R^{3/2}\sqrt{\Sigma/k}]^{-\alpha}\right).
$$

A uniform polynomial state budget then requires a worst-case stationary entropy-production budget at least $c'k[\log(1/\delta)]^{-2/\alpha}$. Conversely a polynomial predictor with $\sigma_0\le(3k/2)\log(12R/\delta)$ exists. This gap is explicit. Neither a nonzero asymptotic floor nor an optimal tradeoff is asserted.

## 3. Contribution and prior work

The [source audit](PRL_EXPLORATION_SOURCE_AUDIT.md) compares complete theorem scopes. Additive reversibilization and its entropy-controlled proximity to an equilibrium analogue are established ideas. In particular, Kolchinsky–Ohga–Ito bound spectral differences using entropy production and a normalized edge-activity factor. The candidate addition here is a uniform controlled endpoint-response estimate with constants supplied by the visible interface, followed by a state-budget obstruction. The source record also distinguishes autonomous positive realization and compression, causal asymmetry, and thermodynamic prediction-information bounds.

The reset representation supplies the physical mechanism behind uniformity in time. Every hidden state returns to the visible state at a rate bounded below by the fixed external interface. This limits how long differences in internal irreversible dynamics can influence an endpoint response. The written proof conditions on the most recent common reset and bounds path relative entropy only over that interval.

Four proof notes have passed separate internal mathematical audits. A bounded exact verifier supplements operator identities and error bookkeeping; it does not prove universal theorems by finite enumeration. See the verification record for the current regression and publication evidence. The novelty comparison and internal audits do not constitute independent peer review.

## 4. Priorities before drafting

1. **Broaden or sharply delimit the physical interface.** Determine which kinetic field rules and preparation mechanisms retain the uniform entropy bridge and state obstruction. Test generalized reversal conventions separately; the present results use ordinary identity reversal.
2. **Find a transparent finite-accuracy example.** Seek a small, certified controlled-mean state advantage with a useful tolerance. A drawing of the lamp mechanism is insufficient: the smallest existing target has a 38-state exact realization and matching general rank threshold, so it does not establish a tiny reversible-versus-irreversible gap.
3. **Narrow the entropy-production frontier.** Improve the inverse-polylogarithmic lower or logarithmic upper under the common cap, or identify the correct additional parameter. Merely sharpening the fifth-root bookkeeping exponent is a secondary priority.
4. **Stress-test the claimed distinction from the closest theorems.** Compare the full controlled-response and minimax resource statements, including state parity, protocol class and activity dependence. Update claims if a closer result subsumes an ingredient.

These are research priorities, not new permission gates. Continue with bounded analytic work and small exact checks; large simulations and manuscript prose remain deferred.

## 5. Physical interpretation limits

The entropy-production rate uses ordinary time reversal of the counted configurations. A thermodynamic reading presumes those variables have that reversal convention. Generalized detailed balance with odd variables has not been analyzed. Stationary zero-field entropy production is distinct from total entropy production during a driven protocol and is not automatically a heat or power estimate for a specified device.

The entropy in the state lower proof belongs to an auxiliary decoded law on the rival's states. It is not the predictor's stationary Shannon entropy. Thus the result does not identify $\log D$ with stored thermodynamic information or invoke a Landauer bound. The targets are constructed worst-case examples, and the necessary entropy production at a fixed accuracy can be extremely small.

The current assessment is to **continue the PRL-directed exploration**: the physical resource question is materially stronger than at the preceding checkpoint, while generality, a transparent finite-accuracy example and the quantitative frontier remain the most consequential open work.
