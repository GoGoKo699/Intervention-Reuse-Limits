# PRL exploration: equilibrium structure and reusable prediction

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Finite minimum theorem](FINITE_PREDICTOR_MINIMALITY.md) · [Physical model](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) · [Verification](VERIFICATION.md)

**Research target, 23 September 2026.** The user selected *Physical Review Letters*. Exploration remains theorem first, with bounded exact checks; manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about), checked during this phase, emphasize a significant physical advance and impact beyond a narrow technical refinement. This is a research assessment, not an acceptance prediction.

## 1. The current result and its physical question

How many states must a reusable stochastic predictor retain if its reduced dynamics must preserve equilibrium structure?

The project now has a small concrete example alongside the asymptotic theorem. A **twelve-state equilibrium target has an exact eleven-state stationary nonreversible predictor**. Every ordinary-reversible rival with at most eleven total states, within the shared kinetic interface and hidden exit cap $2k$, has controlled-mean error greater than $2^{-1360}$. Its witnesses use only fields $0,\log2$, clock $(\log2)/(8k)$, and at most 520 ticks each. The target has an exact two-state passive visible law and hidden relaxation band $[k,3k]$.

This closes the small finite-instance existence question. The tolerance is extraordinarily small and does not close the useful-accuracy or measurement-cost question. The [new minimality theorem](FINITE_PREDICTOR_MINIMALITY.md) proves that eleven is the unrestricted minimum throughout the same interval $0\le\delta\le2^{-1360}$, while twelve is the ordinary-reversible minimum. No eleven-state generalized-reversible predictor is established. The six-label target is new and generally uncentered, separate from the nineteen-level family.

The [construction](FINITE_REVERSIBILITY_ADVANTAGE.md) remains frozen at its earlier $2^{-3000}$ tolerance. The [minimality and improved clock proof](FINITE_PREDICTOR_MINIMALITY.md), [new internal review](FINITE_PRECISION_INTERNAL_REVIEW.md), [new verifier](../scripts/verify_finite_minimality.py) and [source supplement](FINITE_PRECISION_SOURCE_AUDIT.md) establish the current statement and attribution. The exact $K_{p,q}$ extension gives an ordinary minimum $pq+p+q+1$ and an unrestricted sufficient count $2(p+q)+1$. Its alphabet grows with $p+q$; it is not a fixed-alphabet approximation law.

## 2. Why the small example works

The target has six memory states indexed by the edges of $K_{2,3}$ and five probe states indexed by its vertices. An edge state can next enter either endpoint probe. The smaller predictor instead keeps five memory states, each storing a preselected probe; internal refresh can redraw that selection. Every memory state has the same kinetic control function, so moving this random choice earlier does not require knowledge of future fields. A stochastic intertwiner proves exact response equality for every protocol.

Ordinary detailed balance supplies a different constraint. Ten nonnegative observable features have a Gram matrix whose support requires eleven nonnegative atoms: six for graph edges and five for isolated probe features. Each hidden state supplies one atom. Positive selectors keep this interpretation valid even when a rival chooses off-grid barriers and arbitrary new states. A [square-root witness argument](FINITE_GRAM_ROBUSTNESS.md) now tolerates Gram error $1/1500$. Separately, arbitrary stationary rivals produce a nonnegative left/right factorization: the target support needs ten rectangular factors, hence ten hidden states plus the gateway. A shifted logarithm of each sampled Markov propagator transfers both obstructions without assuming reversible rival spectra. The new $2^{-1360}$ certificate uses 520 ticks and the older sufficient matrix threshold $1/40000$.

The core $5\times5$ matrix itself is a prior example: Fawzi–Parrilo give it explicitly in their Eq. (55), and the source supplement traces an earlier attribution through Korda and collaborators. The matrix-factorization and intertwining mechanisms are established mathematics. The candidate contribution is their concrete controlled-mean realization, same-interface comparison, and certified positive-error state gap. The [primary-source audit](FINITE_ADVANTAGE_SOURCE_AUDIT.md) compares completely positive rank, structured hidden-Markov realization and response reciprocity. It does not certify exhaustive novelty.

## 3. A physical model class with specified parity

The [single-force conformational network](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) assigns one extension to the visible gateway and another to all hidden conformations. State-dependent external transition-state extensions give the heterogeneous escape response. One applied force then produces both the equilibrium block tilt and the kinetic rate factors. Hidden wells and internal saddles share their extension, leaving internal exchange force independent.

This is a stipulated Bell–Arrhenius network with physically even configuration states. The [nine-source audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) provides precedents for its ingredients, including a single-gateway enzyme model and force-dependent conformational exchange. Equal baseline escape rates, coinciding hidden extensions and the chosen graph remain model assumptions. A microscopic landscape or laboratory device realizing the complete network has not been constructed.

Two simpler controls remove the intended effect. Changing only association rates while all off-rates remain equal leaves an exact two-state visible process. Changing only barriers at a fixed common equilibrium, starting from that equilibrium, leaves every endpoint mean constant. A force with heterogeneous transition-state positions avoids both restrictions.

The [uniform perturbation theorem](PHYSICAL_INTERFACE_ROBUSTNESS.md) supplies a quantitative neighborhood: a reference return reset at rate $\alpha$ and maximum generator-row TV defect $\eta$ give endpoint TV at most

$$
e^{-\alpha T}d_0+(\eta/\alpha)(1-e^{-\alpha T}).
$$

Small control-dependent hidden-rate errors and finite clocked ramps are therefore allowed with explicit response bounds. Nearby-rival lower bounds require a same-state nearby core model. At fixed defects there is an accuracy floor; the theorem does not establish arbitrary-accuracy asymptotics with fixed experimental errors.

## 4. The asymptotic reversal boundary remains central

On the original nineteen-level equilibrium targets, the [shared-cap theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) retains

$$
D_{\rm all}(\delta)=D_{\rm inv}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm id}(\delta)=\exp(\delta^{-\Theta(1)}).
$$

These are growth classes with unmatched exponents. The same two fields and every fixed positive clock suffice under hidden exit cap $3k$, arbitrary bounded rival barrier functions, and the common equilibrium interface. No rival target alphabet or histogram is required. Without a rival cap, the [uncapped comparison](GENERAL_KINETIC_INTERFACE.md) retains polynomial unrestricted growth and a weaker ordinary-reversible lower.

The generalized-reversal polynomial predictor can have zero stationary entropy production under its own reversal. Hence the ordinary-reversal lower is not a universal heat or dissipation requirement. The small eleven-state predictor in Section 1 is a separate stationary nonreversible construction. Its one-way edges give infinite ordinary entropy production at exact agreement, but reverse-rate regularization retains eleven states and finite ordinary entropy production at error at most $2^{-1361}$.

The [even-observation closure result](PHYSICAL_REVERSAL_REALIZATION.md) further specifies the boundary: a reversal-even equilibrium observation that is itself Markov must obey ordinary detailed balance. Stationary flux aggregation alone need not supply that Markov closure. An ordinary-equilibrium hidden phase cannot generate an exactly nonreversible Markov lump without changing these assumptions. A natural physical implementation of the centered word reversal remains open.

## 5. What to pursue next

1. **A useful finite tolerance.** Develop stable recovery of the bounded rational selectors in the [observation diagnosis](FINITE_OBSERVATION_BOTTLENECK.md), or directly certify finite-time observables. Exact nonnegative polynomial selectors on this six-label grid require degree at least ten; merely lowering their degree cannot retain the same guarantees. The improved $2^{-1360}$ remains an existence threshold, not an estimate of the actual best eleven-state reversible error.
2. **A stronger small comparison.** Explore other incidence graphs or positive realizations for a larger state saving at modest precision. The exact $K_{p,q}$ family provides an analytic starting point; its growing actuator alphabet must be counted as a changed resource.
3. **A conventional microscopic model.** Test whether a force-controlled conformational system justifies the equal-extension and barrier assumptions over a finite range, using the perturbation budget to quantify deviations. A graph-level Arrhenius assignment alone is insufficient.
4. **Substantive generality.** Arbitrary field-dependent hidden generators, more general interfaces and sharper identity-reversal entropy frontiers remain open. Small-neighborhood stability is a partial result with a stated floor.

The PRL case has improved: the state advantage is now visible in a small explicit mechanism, and a single-force model fixes a relevant physical parity. Useful accuracy, microscopic justification and the broader significance/novelty assessment still require work. Manuscript drafting stays deferred.

## 6. Evidence and checkpoint history

The preceding published checkpoint is `720962175fc76e2062e7f2aa4deb1938ba111c77`, tree `e9e51a49936be496f39a3384a8053ee26280eb4c`, with successful [CI run 35853478678](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35853478678). It supplied thirty-seven verifiers, the finite advantage and physical model/robustness results.

This continuation determines both finite minimum counts, improves the same-task observation budget, strengthens the intermediate Gram obstruction and records the remaining selector and reinjection limitations. One new bounded verifier checks the supporting finite identities and constants. Universal rival statements remain analytic. Earlier reports, verifiers, proof snapshots, recovery files and license remain preserved. [Verification](VERIFICATION.md) records the final local gate and distinguishes it from remote CI; internal mathematical audits are not external peer review.
