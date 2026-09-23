# PRL exploration: equilibrium structure and reusable prediction

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Rational observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Physical model](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) · [Verification](VERIFICATION.md)

**Research target, 23 September 2026.** The user selected *Physical Review Letters*. Exploration remains theorem first, with bounded exact checks; manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about), checked during this phase, emphasize a significant physical advance and impact beyond a narrow technical refinement. This is a research assessment, not an acceptance prediction.

## 1. The current result and its physical question

How many states must a reusable stochastic predictor retain if its reduced dynamics must preserve equilibrium structure?

The project now has a small concrete example alongside the asymptotic theorem. A **twelve-state equilibrium target has an exact eleven-state stationary nonreversible predictor**. The [new rational observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) proves that every ordinary-reversible rival with at most eleven total states, within the shared kinetic interface and hidden exit cap $2k$, has controlled-mean error greater than $2^{-220}$. The explicit measurement menu has **12,766 protocols**, using only fields $0,\log2$, clock $(\log2)/(8k)$, and at most **66 ticks** each. The target and controls are unchanged. Its passive visible law is exactly two-state and its hidden relaxation band is $[k,3k]$.

The ordinary-reversible minimum is therefore twelve throughout $0\le\delta\le2^{-220}$, while eleven unrestricted states suffice exactly. The [earlier minimality theorem](FINITE_PREDICTOR_MINIMALITY.md) separately proves unrestricted minimum eleven for $\delta\le2^{-1360}$ on the full two-field clock task, already on its 520-tick word family. That unrestricted lower is not claimed for the new smaller menu or throughout the enlarged error interval. No eleven-state generalized-reversible predictor is established. The six-label target is generally uncentered and separate from the nineteen-level family.

The complementary [symmetry-averaged upper](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) gives a **nine-state ordinary-reversible predictor with error at most $1/2376$**, uniformly for every two-field switching protocol and every horizon. It retains the hidden exit cap $2k$ and needs no clock restriction. This limits where a useful-precision exclusion could lie, but does not identify the optimal reversible error. A wide interval remains between the certified lower threshold and this upper guarantee; neither a practical precision nor a useful sample bound has been established.

The [new internal review](RATIONAL_OBSERVATION_INTERNAL_REVIEW.md), [exact certificate](../scripts/verify_rational_observation.py), [report](../reports/rational_observation.json) and [source comparison](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) support the current statement. The [construction](FINITE_REVERSIBILITY_ADVANTAGE.md) remains frozen at $2^{-3000}$, and the [previous precision checkpoint](FINITE_PRECISION_INTERNAL_REVIEW.md) preserves the $2^{-1360}$ minimum-count proof. The frozen construction's exact $K_{p,q}$ extension gives an ordinary minimum $pq+p+q+1$ and unrestricted sufficient count $2(p+q)+1$. The alphabet grows with $p+q$; this is not a fixed-alphabet approximation law.

## 2. Why the small example works

The target has six memory states indexed by the edges of $K_{2,3}$ and five probe states indexed by its vertices. An edge state can next enter either endpoint probe. The smaller predictor instead keeps five memory states, each storing a preselected probe; internal refresh can redraw that selection. Every memory state has the same kinetic control function, so moving this random choice earlier does not require knowledge of future fields. A stochastic intertwiner proves exact response equality for every protocol.

Ordinary detailed balance supplies a different constraint. Ten nonnegative features have a Gram matrix requiring eleven nonnegative atoms: six for graph edges and five for isolated probe features. Each hidden state supplies one atom. A [square-root witness argument](FINITE_GRAM_ROBUSTNESS.md) tolerates Gram error $1/1500$.

Stable observation of bounded rational selectors is now established. An essential exact rational certificate bounds the smallest singular value of ten specified target clock-word functions. Finite means recover their Gram matrices and give an approximate map intertwining the target and rival sampled dynamics. Resolvent calculus transfers that relation to the hidden barrier diagonal; finite-spectrum divided differences then transfer the bounded rational selectors. This avoids the previous large squared-polynomial values on off-grid rival barriers. The proof remains universal over the allowed reversible rivals.

The older unrestricted lower uses a different positive left/right factorization: the target support needs ten rectangular factors, hence ten hidden states plus the gateway. Its centered-logarithm transfer works without reversible rival spectra and remains valid at its stated $2^{-1360}$ threshold. The new rational argument uses reversibility and does not automatically strengthen that unrestricted lower.

The core $5\times5$ matrix itself is a prior example: Fawzi–Parrilo give it explicitly in their Eq. (55), and the [source supplement](FINITE_PRECISION_SOURCE_AUDIT.md) traces an earlier attribution through Korda and collaborators. The matrix-factorization and intertwining mechanisms are established mathematics. The candidate contribution is their concrete controlled-mean realization, same-interface comparison, and certified positive-error state gap. The [primary-source audit](FINITE_ADVANTAGE_SOURCE_AUDIT.md) compares completely positive rank, structured hidden-Markov realization and response reciprocity. It does not certify exhaustive novelty.

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

The generalized-reversal polynomial predictor can have zero stationary entropy production under its own reversal. Hence the ordinary-reversal lower is not a universal heat or dissipation requirement. The small eleven-state predictor in Section 1 is a separate stationary nonreversible construction. Its one-way edges give infinite ordinary entropy production at exact agreement, but reverse-rate regularization retains eleven states and finite ordinary entropy production at any prescribed positive error, including $2^{-221}$ for the new reversible separation.

The [even-observation closure result](PHYSICAL_REVERSAL_REALIZATION.md) further specifies the boundary: a reversal-even equilibrium observation that is itself Markov must obey ordinary detailed balance. Stationary flux aggregation alone need not supply that Markov closure. An ordinary-equilibrium hidden phase cannot generate an exactly nonreversible Markov lump without changing these assumptions. A natural physical implementation of the centered word reversal remains open.

## 5. What to pursue next

1. **A useful finite tolerance.** Bounded rational recovery is solved for the fixed target, but its certified basis remains poorly conditioned and the $2^{-220}$ threshold is impractical. Improve the basis, the observation certificate or the target itself, or certify a direct finite-time separation. The nine-state reversible upper $1/2376$ supplies a concrete constraint: the best smaller-rival error is at most that value, and the wide remaining range is unresolved. Exact positive polynomial selectors still require degree at least ten on the six-label grid; that earlier obstruction has not become a general conditioning lower bound.
2. **A stronger small comparison.** Explore other incidence graphs or positive realizations for a larger state saving at modest precision. The exact $K_{p,q}$ family provides an analytic starting point; its growing actuator alphabet must be counted as a changed resource.
3. **A conventional microscopic model.** Test whether a force-controlled conformational system justifies the equal-extension and barrier assumptions over a finite range, using the perturbation budget to quantify deviations. A graph-level Arrhenius assignment alone is insufficient.
4. **Substantive generality.** Arbitrary field-dependent hidden generators, more general interfaces and sharper identity-reversal entropy frontiers remain open. Small-neighborhood stability is a partial result with a stated floor.

The PRL case now includes a small explicit mechanism, stable rational recovery with a certified observable basis, and an all-protocol reversible approximation that bounds the possible finite advantage from above. Useful accuracy, microscopic justification and the broader significance/novelty assessment still require work. Manuscript drafting stays deferred.

## 6. Evidence and checkpoint history

The preceding published checkpoint is `a60dee50b8728fb15717d9f06f3876fdf9f67b4a`, tree `41ce1198905603e5d9061060510d5066fe102a6b`, with successful [CI run 35856173987](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35856173987). It supplied thirty-eight verifiers, the exact finite minimum counts at $2^{-1360}$, and the selector/reinjection boundaries.

This continuation adds two verifiers, bringing the verified suite to forty: an exact rational certificate for the essential ten-dimensional target-basis premise, and bounded checks of the symmetry-averaged reversible upper. The new ordinary lower is $2^{-220}$ on the explicit 12,766-word menu, while the nine-state upper is $1/2376$ over all two-field protocols. Universal rival transfer and all-horizon comparison remain analytic; the basis inequality is explicitly computer-assisted. Earlier proof snapshots, reports, recovery files and license remain preserved. [Verification](VERIFICATION.md) records the final local gate and distinguishes it from remote CI; internal mathematical audits are not external peer review.
