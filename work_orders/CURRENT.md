# Current work order: broaden finite-field intervention reuse

## Completed checkpoint — 22 September 2026

This continuation starts from `ef1448235c1fcf70e2c5fdca7d544f87591e9052`. The research direction now extends beyond the previous narrow coefficient-compression assessment. The MIT license, all six earlier mathematical verifiers, and their saved reports are preserved; two new deterministic verifiers cover the extensions.

1. **Actual finite-field prediction.** For the rank-one sensitivity subclass `J(k,W)`, the known scalar kernel determines the exact driven mean, and indeed the complete driven visible path law. A common-reset argument bounds mean error uniformly over every protocol `|h|<=H` and every horizon. Positive quadrature and reversible realization give `Theta(log^2(1/error))` worst-case physical states, or `Theta(log(1/error))` with active rates at most `3k`.
2. **One fixed intervention is enough for the lower order.** For unrestricted rates, choose `h*=min(H,1/[20(1+sqrt(W))])` once, independently of dimension or tolerance. Its exact step mean has a positive spectral expansion. A diagonal-plus-rank-one field generator, quantitative secular estimates, and the Cauchy/Hankel bound establish the root-exponential error obstruction against arbitrary autonomous finite-state Markov competitors. No analytic field dependence or derivative bound is imposed on them.
3. **Visible records reveal hidden kinetics earlier than the mean.** All first-order path responses are universal; the entire quadratic path response is characterized by the kernel. Its exact state requirement is `r+2` without the cubic mean's resonance exception. For a specified three-state pair and fixed-duration weak-step experiment, two visible snapshots need `Theta(h^-4)` independent trials, whereas the final snapshot alone needs `Theta(h^-6)`. Full paths cannot improve the exponent for that task.
4. **A quantitative neighborhood of passive degeneracy.** Small centered external-conductance disorder of relative size `q` gives passive visible-path relative entropy at most `q^4(152+241kT)` from the telegraph process, uniformly over hidden dimension and internal rates. An explicit pair attains the quartic scale, has `Theta(q^-4)` fixed-duration trial complexity, and retains a finite driven mean gap.
5. **A demonstrated closure boundary.** Outside `J`, fixed `k,mu,g` and the same cubic kernel can still give different higher response. The explicit four-state example prevents silently extending the finite-field scalar-kernel theorem to the entire original family.

Start with `docs/FINITE_FIELD.md` and `docs/FIXED_FIELD_LOWER_BOUND.md`. Observation and robustness results are in `docs/ACTIVE_PATH_RESPONSE.md` and `docs/NEAR_LUMPABILITY.md`. `docs/PUBLICATION_SCOPE.md` now centers the stronger theorem; `docs/PRIOR_ART.md` records classical precedents and actual source-access depth.

## Scientific position

The main candidate is a sharp finite-field prediction theorem behind exact passive compression, with an operational explanation of what observations reveal and how passive information vanishes near lumpability. This is more ambitious than a coefficient-only compatibility statement. It remains a theorem about a specified stochastic model and physical Markov state count.

The finite-field upper theorem assumes one distinguished sensitivity state with stationary mass one half. It accepts every finite positive kernel, but restricts its field realization. The fixed-step lower theorem needs no corresponding restrictions on competing Markov predictors. The known-kernel constructor is not a learning algorithm. Approximate full path-law error, noisy arbitrary-kernel recovery, finite precision, runtime, and a molecular implementation are not established.

Canonical aggregated Markov models, waiting-time inference, poor identifiability near equal dwell times, nonlinear response expansions, positive quadrature, and Hankel rank are established. The new observation exponents follow from their leading signal orders and ordinary hypothesis-testing bounds. Do not present those mechanisms as discoveries or infer publication originality from an unsuccessful exact-title search.

## Single next research priority

**Determine what intervention information replaces the scalar kernel outside the rank-one sensitivity subclass, and whether a broader finite-field complexity theorem is possible.**

A concrete first question is whether any finite response jet can be sufficient in the original bounded-sensitivity family. A possible analytic route uses a reversible refresh generator and finite sensitivity distributions with matching moments. This is an exploration lead, not a proved public result. Establish the exact all-protocol coefficient dependence before making a hierarchy claim; moment matching alone is not a new mechanism.

Then identify the smallest additional kernel or response data that closes a larger actuator class. A proposed upper theorem must control actual means for a fixed field interval and all horizons, while counting physical Markov states. A proposed obstruction must keep the actuator and observation task explicit. State exactly which result would settle this question; do not open an unrestricted list of new projects.

Retain the completed finite-field theorem even if the broader extension fails. A rigorous boundary can be scientifically useful. Do not weaken or obscure the current assumptions to obtain a more dramatic framing, and do not replace substantive research with a journal-ranking exercise. Manuscript writing remains on hold.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports belong in `.check-output/`. Regenerate saved evidence only from its verifier. Preserve baseline mathematical scripts, reports, the MIT license, unrelated owner work, and non-forced Git history. The build target and provenance checker may be extended for new verifiers.

No large simulation is needed. Proof audits and calculations within this investigation are not independent external validation. Local PASS and GitHub Actions are separate evidence. The hypothesis-testing results assume specified models, ideal recorded data, and stationary preparation; they do not charge the cost of restoring that preparation. Do not contact prospective collaborators or send messages without explicit user authorization.
