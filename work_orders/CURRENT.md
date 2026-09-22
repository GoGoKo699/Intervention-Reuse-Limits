# Current work order: sharp general-family state cost

## New completed extension — 22 September 2026

This continuation starts from `1f7f747a64442e15eab929c08e19d3958c9f4828`. All eight preceding mathematical verifiers and reports are preserved. Three broader results have complete internal proofs and proof audits, with two new deterministic verifiers.

1. **Arbitrary-order obstruction with an unchanged actuator.** For every $d\ge2$, two $d+2$-state models share the full tuple $k,\mu,g$, external field rates, a one-mode cubic kernel, and all-protocol mean response through order $2d$. Their complete visible path responses agree through order $2d-1$. The next orders differ; every nonzero constant field separates the exact mean curves. Only the reversible internal generator changes, and its nonzero decay rates stay in $[\lambda,3\lambda/2]$. Fixed $0<W<G^2$ and $G$ are allowed. The tuple may change with $d$, and the separating signal may shrink.
2. **Complete general path information.** The stationary law of the autonomous hidden sensitivity process $g(X_t)$ is equivalent to the collection of all controlled visible path laws. No-exit functionals with short pulses recover joint Laplace transforms noiselessly. A finite-rank actuator admits matrix-return closure. An explicit binary-actuator pair has identical two-time level kernels and internal spectra, but different finite-field means, ruling out a naive two-time matrix replacement.
3. **General-family fixed-accuracy existence.** Every bounded-sensitivity reversible target has a finite Markov mean predictor with a state bound independent of microscopic size and internal rates, uniformly over all bounded protocols and horizons. Quantization, spectral regularization, and canonical finite-word approximation give an explicit, very large bound. The predictor preserves the same sensitivity bound, passive law, equilibrium curve, and linear/quadratic mean agreements. It generally loses internal reversibility and changes sensitivity variance by at most the squared quantization error.

Start with `docs/FIXED_ACTUATOR_HIERARCHY.md`, `docs/ACTUATOR_PROCESS.md`, and `docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md`. The sharp canonical-subclass results below remain the quantitative baseline. No finite response-jet completeness is implied by the general approximation upper bound, and no fixed-error impossibility follows from the hierarchy theorem.

## Earlier finite-field checkpoint — 22 September 2026

This continuation starts from `ef1448235c1fcf70e2c5fdca7d544f87591e9052`. The research direction now extends beyond the previous narrow coefficient-compression assessment. The MIT license, all six earlier mathematical verifiers, and their saved reports are preserved; two new deterministic verifiers cover the extensions.

1. **Actual finite-field prediction.** For the rank-one sensitivity subclass `J(k,W)`, the known scalar kernel determines the exact driven mean, and indeed the complete driven visible path law. A common-reset argument bounds mean error uniformly over every protocol `|h|<=H` and every horizon. Positive quadrature and reversible realization give `Theta(log^2(1/error))` worst-case physical states, or `Theta(log(1/error))` with active rates at most `3k`.
2. **One fixed intervention is enough for the lower order.** For unrestricted rates, choose `h*=min(H,1/[20(1+sqrt(W))])` once, independently of dimension or tolerance. Its exact step mean has a positive spectral expansion. A diagonal-plus-rank-one field generator, quantitative secular estimates, and the Cauchy/Hankel bound establish the root-exponential error obstruction against arbitrary autonomous finite-state Markov competitors. No analytic field dependence or derivative bound is imposed on them.
3. **Visible records reveal hidden kinetics earlier than the mean.** All first-order path responses are universal; the entire quadratic path response is characterized by the kernel. Its exact state requirement is `r+2` without the cubic mean's resonance exception. For a specified three-state pair and fixed-duration weak-step experiment, two visible snapshots need `Theta(h^-4)` independent trials, whereas the final snapshot alone needs `Theta(h^-6)`. Full paths cannot improve the exponent for that task.
4. **A quantitative neighborhood of passive degeneracy.** Small centered external-conductance disorder of relative size `q` gives passive visible-path relative entropy at most `q^4(152+241kT)` from the telegraph process, uniformly over hidden dimension and internal rates. An explicit pair attains the quartic scale, has `Theta(q^-4)` fixed-duration trial complexity, and retains a finite driven mean gap.
5. **A demonstrated closure boundary.** Outside `J`, fixed `k,mu,g` and the same cubic kernel can still give different higher response. The explicit four-state example prevents silently extending the finite-field scalar-kernel theorem to the entire original family.

Start with `docs/FINITE_FIELD.md` and `docs/FIXED_FIELD_LOWER_BOUND.md`. Observation and robustness results are in `docs/ACTIVE_PATH_RESPONSE.md` and `docs/NEAR_LUMPABILITY.md`. `docs/PUBLICATION_SCOPE.md` now centers the stronger theorem; `docs/PRIOR_ART.md` records classical precedents and actual source-access depth.

## Scientific position

The main candidate is a sharp finite-field prediction theorem behind exact passive compression, with an operational explanation of what observations reveal and how passive information vanishes near lumpability. This is more ambitious than a coefficient-only compatibility statement. It remains a theorem about a specified stochastic model and physical Markov state count.

The sharp finite-field upper theorem assumes one distinguished sensitivity state with stationary mass one half. It accepts every finite positive kernel, but restricts its field realization. The general upper theorem removes that geometry at the cost of a much larger state bound and potentially nonreversible surrogate. The fixed-step lower theorem needs no corresponding restrictions on competing Markov predictors. Neither constructor is a learning algorithm. Approximate full path-law error over all horizons, noisy arbitrary-kernel recovery, finite precision, runtime, and a molecular implementation are not established.

Canonical aggregated Markov models, waiting-time inference, poor identifiability near equal dwell times, nonlinear response expansions, positive quadrature, and Hankel rank are established. The new observation exponents follow from their leading signal orders and ordinary hypothesis-testing bounds. Do not present those mechanisms as discoveries or infer publication originality from an unsuccessful exact-title search.

## Single next research priority

**Determine the optimal general-family state cost, including whether preserving reversibility changes it.**

The completed extension answers the earlier information and existence questions. The fixed-actuator construction is stronger than the deferred varying-moment construction, so the latter need not become a duplicate theorem. The exact actuator-process invariant and nonsharp general upper bound are now available tools.

At fixed $k,G,W,H$ with $0<W<G^2$, the canonical targets embed into the general family and supply the squared-logarithmic lower order against arbitrary Markov predictors. The general upper bound is far larger and permits nonreversibility and small variance error. The task is to narrow that gap or prove a larger state order, while keeping the same controlled-mean norm and counting all physical memory states.

A concrete first restricted class is two sensitivity levels with more than one hidden state at each level. Its two-time kernel already fails exact closure. Alternatively, a rank-two actuator gives a matrix-return equation, but positive-semidefinite matrix quadrature alone does not establish nonnegative Markov rates. Any proposed constructive realization must prove positivity; any lower bound must control a fixed nonzero accuracy rather than only a formally nonzero response coefficient. Avoid assuming that the new hierarchy theorem supplies such a lower bound.

Retain the completed finite-field theorem even if the broader extension fails. A rigorous boundary can be scientifically useful. Do not weaken or obscure the current assumptions to obtain a more dramatic framing, and do not replace substantive research with a journal-ranking exercise. Manuscript writing remains on hold.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports belong in `.check-output/`. Regenerate saved evidence only from its verifier. Preserve baseline mathematical scripts, reports, the MIT license, unrelated owner work, and non-forced Git history. The build target and provenance checker may be extended for new verifiers.

No large simulation is needed. Proof audits and calculations within this investigation are not independent external validation. Local PASS and GitHub Actions are separate evidence. The hypothesis-testing results assume specified models, ideal recorded data, and stationary preparation; they do not charge the cost of restoring that preparation. Do not contact prospective collaborators or send messages without explicit user authorization.
