# PRL exploration: a familiar model and seven short experiments

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Current proof](FAMILIAR_SWITCH_FINITE_MARGIN.md) · [Verification](VERIFICATION.md)

**Research target, 24 September 2026.** The user selected *Physical Review Letters*, asked for a familiar physical candidate, and emphasized that a strong result should be simple. Manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about) are a publication reference, not an acceptance prediction. The immediate scientific test is whether the simple state-count mechanism has a physically meaningful, robust observable consequence.

## 1. Current result: two coupled conformational switches

Use time-even Ising variables with energy $E_h=-Js_0s_1-hs_0$, heat-bath flips, equal unit attempt rates, and observed conformation $S=s_0$. Prepare zero-field equilibrium. The target has four configurations. The [structure theorem](FAMILIAR_SWITCH_STRUCTURE.md) gives an exact three-state stationary predictor of its controlled mean, whereas ordinary detailed balance requires four states. This holds for every finite $J,H>0$.

Rivals may choose arbitrary new states and rates, but retain a deterministic binary readout, balanced zero-field preparation, and the shared Gibbs tilt $\pi_H=\pi_0(1+uS)$, $u=\tanh H$. Thus control couples only to the observed conformation. Arbitrary independent hidden-state force couplings are outside the theorem. The lower has no rival rate cap. The exact three-state upper works for every nonnegative-field protocol and horizon, with exits below two.

The mechanism is conditional variance: detailed balance at two fields forces a latent coordinate to fluctuate within both observed conformations. Each sector therefore needs at least two states. A stationary nonreversible predictor can instead use three states. These are mean predictions, not complete binary path laws; the target's passive path already reveals hidden memory.

## 2. Seven experiments and a certified error bracket

The [finite-margin theorem](FAMILIAR_SWITCH_FINITE_MARGIN.md) replaces the previous eleven-word reconstruction by a direct quartic identity in seven measured means. In chronological order, the words are

$$
H,\quad H^2,\quad H^3,\quad H0,\quad H^20,\quad H0H,\quad H^20H.
$$

Each letter lasts one clock tick, adjacent equal fields form one segment, and every experiment starts from the same preparation. The longest experiment has four ticks and three segments. Every ordinary rival with at most three states satisfies at least one of two quartic equalities. The target violates both with opposite nonzero signs. An adjugate identity includes singular response tables; no inverse, generator logarithm or rate compactification is required. Necessity even holds for arbitrary reversible stochastic tick kernels with the shared Gibbs tilt, whether or not they embed in continuous time.

The proof gives an analytic positive occupation-error lower bound $\Delta/(2L)$ for every $J,H,a>0$. For the simple choice $J=H=\log3$ and clock $a=2$, a sharper exact rational whole-box certificate proves

$$
D_{\rm all}(\delta_P)=3,\qquad D_{\rm ord}(\delta_P)=4,
\qquad 0\le\delta_P\le1/2000.
$$

Here $\delta_P$ is the maximum absolute error in $P(S=+1)$ across the seven experiments; spin-mean error is twice as large. The tolerance is **0.05 percentage points**, not one percentage point. The maximum horizon is eight attempt-rate units.

The same [exact verifier](../scripts/verify_familiar_switch_margin.py) certifies a fixed rational ordinary three-state model with maximum occupation error below $837/10^6<1/1000$ on these same seven words. Thus the best ordinary-three-state error lies between 0.05 and 0.1 percentage points. This feasible upper is not an optimality claim, an eleven-word bound, or an all-protocol guarantee. Its exits are below three. The numerical thresholds rely on computer-assisted exact arithmetic; the universal polynomial necessity and all-parameter positive bound have analytic proofs.

## 3. Evidence and practical limitations

The [103-check certificate](../reports/familiar_switch_margin.json) uses matrices of dimension at most four, rational matrix-exponential enclosures and exact shifted-polynomial coefficient bounds. Root and separate reviewers inspected the proof and source; an independently coded three-dimensional rational enclosure confirms the lower certificate. The [internal review](FAMILIAR_SWITCH_MARGIN_INTERNAL_REVIEW.md) separates those analytic and arithmetic checks from exploratory fitting.

The [new saved-model screen](../reports/short_switch_witness_screen.json) contains four bounded panels, eight fitted rivals and the rounded rational upper. It replays without optimization. Direct refitting on the old eleven-word menu at $(J,H,a)=(1.5,2,1)$ reaches occupation error about $0.00017745$, substantially below the older retained model's $0.00471093$ without refitting. Neither number is a universal lower bound. Earlier 33-word screens and held-out evaluations remain preserved in the [original protocol record](FAMILIAR_SWITCH_PROTOCOLS.md).

The tiny matrices and bounded CPU searches fit the user's Ryzen AI Max+ 395 / 128 GB hardware. Large simulation, cloud compute and a GPU are unnecessary for this checkpoint. A practical sample budget, imperfect preparation, clock and field calibration, and violations of the shared tilt have not yet been certified. These limits matter more now than another exact state-count example.

The [new source comparison](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) examines primary full texts on finite realization, observable polynomial invariants and robust dimension witnesses. Those ingredients are attributed, not claimed as new. The [kinetic source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) covers familiar closure and dynamic-disorder models; Falk's 1983 reduced spin-chain paper remains an unresolved full-text comparison. The searches are bounded and do not certify priority. Time-even conformation and ordinary reversal are explicit: no universal heat requirement or generalized-reversal separation follows.

## 4. Next scientific decision

1. **Stress-test physical tolerances.** Quantify how preparation bias, field and timing errors consume the $1/2000$ error budget. Use the same seven means and polynomial certificate where possible; distinguish target perturbation from relaxing the rival's shared Gibbs law.
2. **Test the interface assumption.** Determine what can independently calibrate control coupling only to the observed conformation. Small hidden force dependence is a new robustness problem, not covered by arbitrary endpoint rates at an exact shared tilt.
3. **Assess measurement cost and significance.** Translate simultaneous endpoint precision into a stated statistical experiment and sample budget. Retain the ordinary-three-state upper beside the lower. Do not call a sub-tenth-percentage-point distinction an experimentally robust advantage without this work.
4. **Complete the closest-source comparison.** Resolve the outstanding full text and compare whole assumptions and claims. External scientific scrutiny would strengthen evidence; no collaborator contact is part of this checkpoint.

The result is now simple enough to explain and quantitatively falsifiable. Whether its precision and interface restrictions support a compelling PRL contribution remains open. Manuscript drafting stays deferred.

## 5. Earlier results retained separately

The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) gives exact state counts $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$ for a separate capped hub-interface family with exact two-state passive paths. The [variance principle](KINETIC_VARIANCE_COMPRESSION.md) bounds all-protocol compression through kinetic heterogeneity and hidden mixing. Neither interface is silently transferred to the coupled pair.

The twelve-state target retains an exact eleven-state stationary upper and [ordinary minimum twelve](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) at mean error $2^{-220}$ on 12,766 experiments of at most 66 ticks. Unrestricted minimum eleven is established on the narrower $2^{-1360}$ interval and a different menu. Nine reversible states suffice at $1/2376$, and two at $557/51920$, uniformly over its two-field protocols.

The [asymptotic reversal theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) remains a separate result: unrestricted and generalized-reversible growth are polynomial, ordinary-reversible growth exponential, under its common cap and interface. Generalized reversal can have zero stationary entropy production.

This continuation starts from published commit ed66b72eb2e1ddf6a6e9a0397cbdb5304139f335, tree ffcc9ba636ac6dc72e9ae03c5ccf558008fe94a1, with successful [CI run 35887218370](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35887218370). The 89 protected baseline files, earlier proof bindings, nine recovery files and original license remain preserved. [Verification](VERIFICATION.md) distinguishes local completion from publication CI.
