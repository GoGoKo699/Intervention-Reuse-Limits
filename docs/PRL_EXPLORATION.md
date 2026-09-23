# PRL exploration: a familiar model and a short memory mechanism

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Current proof](FAMILIAR_SWITCH_STRUCTURE.md) · [Verification](VERIFICATION.md)

**Research target, 23 September 2026.** The user selected *Physical Review Letters*, asked for a familiar physical candidate, and emphasized that a strong result should be simple. Manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about) motivate a significant physical advance beyond a narrow technical refinement; this record makes no acceptance prediction.

## 1. Current candidate: two coupled conformational switches

Use time-even Ising variables with energy $E_h=-Js_0s_1-hs_0$, heat-bath flips, equal attempt rates, and observed conformation $S=s_0$. Prepare equilibrium at zero field. The target has four configurations. The [new theorem](FAMILIAR_SWITCH_STRUCTURE.md) gives, for every finite $J,H>0$ and every fixed clock $a>0$,

$$
D_{\rm all}(0)=3,\qquad D_{\rm ord}(0)=4.
$$

The comparison allows arbitrary new predictor states and rates, but keeps a deterministic binary readout and the Gibbs tilt $\pi_h=\pi_0e^{hS}/\cosh h$. The two zero-field readout masses are one half. This means the applied control couples only to the observed conformation. Arbitrary independent hidden-state force couplings are outside the theorem. Exact lower bounds need no rival rate cap; both explicit upper models have exits below two in attempt-rate units.

The mechanism uses only two mean equations. Their three-dimensional linear realization identifies an internal coordinate $Z$. Ordinary detailed balance, together with the common control tilt at zero and positive field, forces

$$
\operatorname{Var}(Z\mid S=+1)=\operatorname{Var}(Z\mid S=-1)=1-\tanh^2J>0.
$$

Both observed conformations need at least two underlying states. A three-state stationary predictor avoids that equilibrium constraint; explicit positive rates reproduce the same closed mean equations under every nonnegative field protocol and every horizon.

Eleven endpoint measurements suffice: $H^n$ for $n=1,\ldots,5$, and $H^i0H^j$ for $i=1,2$, $j=0,1,2$. Each experiment starts from the same preparation and uses at most three segments and five ticks. The constant-field Hankel matrix and two shifted response tables identify both propagators. This gives a finite exact witness and a positive, presently unquantified accuracy interval on the same menu, even without a rival rate cap. Compactness of sampled propagators and continuity of their principal logarithms exclude arbitrarily fast zero-error limiting sequences.

These are mean predictions, not complete path laws. Passive paths in the coupled pair already reveal hidden memory. At zero coupling the observed switch is autonomous and exactly two-state. The main three-versus-four theorem uses equal attempt rates; a three-spin linear closure alone does not establish a positive Markov realization with four states.

## 2. What the bounded numerical screen says

The [protocol record](FAMILIAR_SWITCH_PROTOCOLS.md) saves feasible equilibrium rivals, their full generators, and every tested endpoint. It distinguishes occupancy error $|\Delta P(S=+1)|$ from spin-mean error, which is twice as large.

At the rational fixture $J=H=\log2/2$, a shared three-state ordinary-reversible model closely approximates the tested responses. Across twelve stronger-coupling fixtures with $J\in\{0.5,1,1.5,2\}$ and $H\in\{0.5,1,2\}$, all 33-protocol fitting menus admit saved feasible rivals below 0.14% occupancy error. For the retained comparator at $(J,H)=(1.5,2)$, 32 held-out pulses give at most 0.2707% occupancy error, and the eleven-word menu at clock one gives 0.4711%, without refitting. These remain finite samples and achievable uppers. No tested fitting menu establishes a one-percent advantage.

These calculations provide upper bounds on the best finite-menu error. Local optimization cannot certify exclusion of every equilibrium rival. The exact theorem and positive-error existence remain valid, but a useful experimental tolerance, sample budget, and optimal clock remain unresolved. The optional search is small enough for the user's Ryzen AI Max+ 395, 128 GB machine; deterministic replay uses only tiny matrices and does not rerun fitting in CI.

## 3. Evidence and literature boundary

The [internal review](FAMILIAR_SWITCH_INTERNAL_REVIEW.md) separates independent analytic audits from the [exact finite verifier](../scripts/verify_familiar_switches.py) and [saved report](../reports/familiar_switches.json). The verifier checks rational two- and three-switch fixtures, positive three-state generators, Gibbs stationarity, closure, rank identities, and the finite menu. It supplements the universal proof.

The [source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) attributes Glauber mean closure, heat-bath receptor models, finite-state dynamic disorder, and positive realization theory. It compares their tasks with the controlled Gibbs-family state-count theorem. Falk's 1983 reduced spin-chain paper remains an abstract-only lead requiring full-text comparison. The search is bounded and does not certify novelty. All configurations here are time-even; no universal dissipation or heat requirement follows from an ordinary-reversibility state penalty.

## 4. Next scientific work

1. **Quantify the eleven-experiment margin.** Use the small realization and conditional-variance contradiction to derive stable inequalities in the measured means. Compare any certified lower with the saved feasible ordinary rivals at the same $J,H,a$ and in the same error units.
2. **Choose a useful clock and physical regime.** Evaluate conditioning and response contrast using bounded calculations. Keep one shared rival across all protocols; avoid interpreting a fitted residual as a universal lower bound. Stop a candidate if a certified simple upper makes its observable advantage negligible.
3. **Test the substantive interface restriction.** Determine whether the shared Gibbs tilt can be independently calibrated in a familiar conformational or receptor setting. Broader hidden force coupling is a new problem, not an automatic extension.
4. **Complete the closest-source comparison.** Obtain the unresolved reduced-spin-model full text and compare whole assumptions and claims. External scientific review would improve evidence; it is not a new permission gate for continued research.

The immediate objective is a useful precision certificate for the familiar two-switch mechanism. A manuscript remains deferred until the physical scope, accuracy, and contribution are sufficiently clear.

## 5. Earlier results retained as reference

The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) gives exact state counts $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$ for a separate capped hub-interface family with exact two-state passive paths. The [variance principle](KINETIC_VARIANCE_COMPRESSION.md) bounds all-protocol mean compression through kinetic heterogeneity and hidden mixing. Neither theorem's interface is silently transferred to the coupled-switch model.

The twelve-state incidence target retains its exact eleven-state stationary upper and [ordinary minimum twelve](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) at error $2^{-220}$ on 12,766 experiments of at most 66 ticks. Unrestricted minimum eleven was proved on the narrower $2^{-1360}$ interval and a different witness family. Nine reversible states suffice at $1/2376$, and two at $557/51920$, uniformly over all two-field protocols. Those upper bounds explain why useful precision remained a concern.

The [asymptotic reversal theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) remains a separate result: unrestricted and generalized-reversible growth are polynomial, ordinary-reversible growth exponential, under its common cap and interface. Generalized reversal can have zero stationary entropy production, so ordinary reversal cannot be equated with a universal heat requirement.

This continuation starts from published `f1a7872fec92353314a06d6f6bd12b79013e79d2`, tree `326d592b4ee47627576a04feb62f3355a3a43c21`, with successful [CI run 35864902730](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35864902730). The 41 earlier verifiers, saved reports, frozen proofs, nine recovery files and original license remain preserved. [Verification](VERIFICATION.md) records local checks and distinguishes publication CI.
