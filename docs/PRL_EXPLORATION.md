# PRL exploration: equilibrium structure and reusable prediction

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Rational observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Physical model](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) · [Verification](VERIFICATION.md)

**Research target, 23 September 2026.** The user selected *Physical Review Letters*. Exploration remains theorem first, with bounded exact checks; manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about), checked during this phase, emphasize a significant physical advance and impact beyond a narrow technical refinement. This is a research assessment, not an acceptance prediction.

## 1. The current result and its physical question

How many states must a reusable stochastic predictor retain if its reduced dynamics must preserve equilibrium structure?

The user emphasizes that a strong result should have a simple mechanism. The new [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) supplies one: a stationary predictor may use distinct incoming and outgoing memory profiles; ordinary detailed balance identifies the two sides of matched reversed tests. For a normalized completely positive $n\times n$ matrix $H$ with positive row sums, the controlled task has exact minima

$$
D_{\rm all}(0)=1+n+\operatorname{rank}_+(H),\qquad
D_{\rm ord}(0)=1+n+\operatorname{cprank}(H).
$$

Every target retains an exact two-state passive path law, hidden band $[k,3k]$, two fields and a common hidden exit cap $2k$. Rivals may create arbitrary new states and endpoint barriers. Both minima persist on a positive matrix-dependent accuracy interval and finite menu, without a useful general tolerance being asserted. The growing target label count and the specified physical interface remain part of the theorem. The algebraic ingredients have established precedents; the [source comparison](SIMPLE_PREDICTION_SOURCE_AUDIT.md) isolates the controlled realization statement.

The project also retains the small concrete example alongside the asymptotic theorem. A **twelve-state equilibrium target has an exact eleven-state stationary nonreversible predictor**. The [new rational observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) proves that every ordinary-reversible rival with at most eleven total states, within the shared kinetic interface and hidden exit cap $2k$, has controlled-mean error greater than $2^{-220}$. The explicit measurement menu has **12,766 protocols**, using only fields $0,\log2$, clock $(\log2)/(8k)$, and at most **66 ticks** each. The target and controls are unchanged. Its passive visible law is exactly two-state and its hidden relaxation band is $[k,3k]$.

The ordinary-reversible minimum is therefore twelve throughout $0\le\delta\le2^{-220}$, while eleven unrestricted states suffice exactly. The [earlier minimality theorem](FINITE_PREDICTOR_MINIMALITY.md) separately proves unrestricted minimum eleven for $\delta\le2^{-1360}$ on the full two-field clock task, already on its 520-tick word family. That unrestricted lower is not claimed for the new smaller menu or throughout the enlarged error interval. No eleven-state generalized-reversible predictor is established. The six-label target is generally uncentered and separate from the nineteen-level family.

The complementary [symmetry-averaged upper](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) gives a **nine-state ordinary-reversible predictor with error at most $1/2376$**, uniformly for every two-field switching protocol and every horizon. It retains the hidden exit cap $2k$ and needs no clock restriction. This limits where a useful-precision exclusion could lie, but does not identify the optimal reversible error. A wide interval remains between the certified lower threshold and this upper guarantee; neither a practical precision nor a useful sample bound has been established.

The [new internal review](RATIONAL_OBSERVATION_INTERNAL_REVIEW.md), [exact certificate](../scripts/verify_rational_observation.py), [report](../reports/rational_observation.json) and [source comparison](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) support the current statement. The [construction](FINITE_REVERSIBILITY_ADVANTAGE.md) remains frozen at $2^{-3000}$, and the [previous precision checkpoint](FINITE_PRECISION_INTERNAL_REVIEW.md) preserves the $2^{-1360}$ minimum-count proof. The frozen construction's exact $K_{p,q}$ extension gives an ordinary minimum $pq+p+q+1$ and unrestricted sufficient count $2(p+q)+1$. The alphabet grows with $p+q$; this is not a fixed-alphabet approximation law.

The [kinetic-variance theorem](KINETIC_VARIANCE_COMPRESSION.md) gives the other half of the story. Hidden deviations affect the mean only after heterogeneous barriers excite them and then read them out. An exact memory-kernel identity yields a uniform variance/mixing bound. The unchanged target therefore also admits a **two-state ordinary-reversible predictor at error at most $557/51920<0.01073$**, for every two-field protocol and horizon. Its best error is not determined. This bound and the nine-state upper should accompany claims about the small target's significance.

## 2. Why the small example works

The matrix principle proves the mechanism for any normalized completely positive matrix with positive row sums: every factorization stochastically maps to the same endpoint predictor, while matched positive tests impose the corresponding lower factor count. It also preserves the complete controlled binary-output path law. The earlier target is the case with nonnegative rank five and completely positive rank six. Concretely, it has six memory states indexed by the edges of $K_{2,3}$ and five probe states indexed by its vertices. An edge state can next enter either endpoint probe. The smaller predictor instead keeps five memory states, each storing a preselected probe; internal refresh can redraw that selection. Every memory state has the same kinetic control function, so moving this random choice earlier does not require knowledge of future fields. A stochastic intertwiner proves exact response equality for every protocol.

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

1. **Keep the mechanism simple and test its physical scale.** The general rank formula organizes exact and sufficiently fine prediction, while the variance theorem explains coarse-accuracy collapse. On the current target, nine reversible states suffice at $1/2376$ and two at $557/51920$; the state-gap certificate remains $2^{-220}$. Seek a direct, useful-precision witness or a better-conditioned target with a short physical explanation.
2. **Broaden a substantive assumption with a clean proof.** A natural next question is whether exact continuous-dwell data force the target barrier palette and remove the rival rate cap from the matrix characterization. This is a research direction, not part of the frozen theorem. Its fixed-clock positive-error version would require separate control.
3. **A conventional microscopic model.** Test whether a force-controlled conformational system justifies the equal-extension and barrier assumptions over a finite range, using the perturbation budget to quantify deviations. A graph-level Arrhenius assignment alone is insufficient.
4. **Complete-theorem significance and novelty.** Compare the controlled classification with the closest positive realization results, while retaining the variance bound as a check on finite-precision relevance. Arbitrary interfaces and hidden control dependence remain open for the state-count classification; the variance theorem already permits field-dependent hidden generators with a common stationary law. Sharper identity-reversal entropy frontiers remain a separate problem.

The research story is clearer: the matrix theorem identifies what ordinary reversal changes in the required memory, and the variance theorem identifies when that memory barely changes the measured response. Useful precision, microscopic justification and the broader significance/priority assessment still require work. This is progress toward the PRL target, not an acceptance prediction. Manuscript drafting stays deferred.

## 6. Evidence and checkpoint history

The preceding published checkpoint is `2923ca8c3992726593ee3111342c1e004cd4b53a`, tree `f74bcbf86f5ce25d3d0863822623ea120c0378c0`, with successful [CI run 35859347383](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35859347383). It supplied forty verifiers, the rational observation certificate and the nine-state symmetry upper.

This continuation adds two analytic principles and one combined verifier, bringing the verified suite to forty-one. Its 200 exact checks cover factor normalization, stochastic intertwining, matched feature matrices, centered density equations and variance constants, at dense dimension at most twelve. The general matrix and all-protocol theorems have separate internal reviews. The README now presents the short physical story and points to the complete ledger for historical scopes. Earlier proof snapshots, verifiers, reports, recovery files and license remain preserved. [Verification](VERIFICATION.md) records the completed local gate and separate remote CI.
