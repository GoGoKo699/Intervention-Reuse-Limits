# Familiar two-switch theorem: internal review

[Proof](FAMILIAR_SWITCH_STRUCTURE.md) · [Source comparison](FAMILIAR_SWITCH_SOURCE_AUDIT.md) · [Protocol diagnostics](FAMILIAR_SWITCH_PROTOCOLS.md) · [Verification](VERIFICATION.md)

**Internal mathematical review, 23 September 2026.** The root reviewer and three separate analytic reviewers checked the universal construction, arbitrary-rival obstruction, and eleven-experiment refinement. The statements below passed those checks. This records internal work, not external peer review or a novelty certificate.

## 1. Reviewed theorem and assumptions

For two time-even conformational Ising variables with finite $J>0$, locally applied field $h\in\{0,H\}$ with $H>0$, and equal unit heat-bath attempt rates, the exact controlled-mean minima are three stationary states and four ordinary-reversible states. Preparation is zero-field equilibrium; the readout is deterministic and binary with balanced zero-field masses. Every rival obeys the same Gibbs tilt $\pi_h=\pi_0e^{hS}/\cosh h$. Its other microscopic states and generators are free. Independent hidden-state field coupling is outside this class.

The three-state upper is positive for every finite nonnegative field and reproduces every switched endpoint mean. All exits are below two, as are the target's. The lower and positive-error existence need no rival rate cap. The two control fields suffice at every prescribed positive clock.

## 2. Checks of the mechanism

- **Exact closure and rank.** Direct generator action closes $1,S,Z$. A constant positive field produces one nonzero constant coefficient and two nonzero decaying coefficients with distinct exponents. The sampled Hankel rank is three at every positive clock. This supplies necessity beyond the informal observation that two means close.
- **Positive upper.** Independent derivations checked the explicit six rates against conjugation of the closed mean generator. The potentially small rates have strictly positive factorizations and margins for every $0<\tanh J<1$, $0\le\tanh h<1$. The Gibbs-tilted law is stationary because the three closure coordinates form a basis. The internal coordinate may exceed the range of a physical spin; it is not an additional readout. Strictly positive reverse rates also make ordinary stationary entropy production finite at each finite field. The family is nonreversible at zero field; particular positive-field members can be reversible.
- **Ordinary lower.** A shared minimal realization transfers both sampled propagators. Ordinary detailed balance supplies positive propagator spectra and identifies each generator with its principal logarithm divided by the clock. The Gibbs tilt and adjoint symmetry force conditional means $\pm\tanh J$ and conditional second moments one. Both readout sectors therefore require variance $1-\tanh^2J>0$, excluding a singleton sector and hence three states.
- **Eleven measurements.** Five constant-field words provide the $3\times3$ Hankel and its high-field shift; six additional words provide the zero-field shifted table. Its first row is already known from zero-field stationarity. Invertibility identifies both propagators in common coordinates. The longest word has five ticks and three constant-field segments. Experiments restart from the common preparation.
- **Uncapped positive margin.** If ordinary rivals with at most three states approached the eleven means arbitrarily closely, a fixed-size/readout subsequence would have convergent stationary laws and stochastic endpoint propagators. Zero-mass states would be inaccessible from the common positive support, contradicting the limiting rank-three Hankel. The eleven tables then fix both limiting propagator spectra to the strictly positive target spectra. Principal-log continuity forces finite limiting Markov generators, retaining detailed balance and the Gibbs tilt, contradicting the exact lower. This compactness argument concerns propagators, not an assumed compact set of unbounded generators. Two-state stationary models are reversible, so the same margin excludes every unrestricted two-state rival.

The last argument proves existence of $\varepsilon(J,H,a)>0$ on the specified menu. It computes no numerical value and gives no uniform bound over parameters, clocks, or sampling budgets.

## 3. Exact finite evidence and numerical evidence

The [exact verifier](../scripts/verify_familiar_switches.py) and [report](../reports/familiar_switches.json) contain **386 rational/formal checks**, maximum dense dimension eight. They use independently built physical rates and reduced generators, sixteen rational coupling/field fixtures, twelve nonzero-field derivative-Hankel determinants, a second rational predictor, passive flip hazards, uncoupled aggregation, two- and three-switch mean ranks, exact eleven-word coverage, and a formal Vandermonde-square polynomial identity. Root and a separate source reviewer read the implementation; pinned regeneration is recorded in the verification log. Finite fixtures supplement the analytic universal proof.

The [screen script](../scripts/screen_familiar_switches.py) and [saved models](../reports/familiar_switch_screen.json) are a separate numerical diagnostic. Small-matrix exponential propagation checks feasible ordinary rivals on listed protocols; the optional bounded fitting routine is excluded from CI. Root and a separate reviewer read the complete script and protocol note; independent replay regenerated the saved report byte for byte. A fitted residual is an achievable upper error, never a universal lower. In the twelve-case two-switch grid, each 33-word menu has a retained ordinary three-state fit below 0.14% occupancy error. The retained comparator at $(J,H)=(1.5,2)$ has 0.4711% occupancy error on the separate eleven-word clock-one menu, without refitting. Spin-mean errors are twice occupancy errors.

The numerical results leave practical accuracy unresolved. They do not contradict the positive-margin theorem and do not establish a percent-scale separation.

## 4. Boundaries retained after review

The passive coupled output is not two-state Markov: in the rational fixture its stationary-conditioned flip hazard is $4/9$, while its immediate post-flip hazard is $1/2$. The theorem preserves means, not complete output trajectories. The three-switch mean closure alone does not supply a four-state positive Markov predictor. The main positive construction assumes equal attempt rates. The theorem is about ordinary time reversal for configurations; no generalized-reversal minimum, device implementation, or universal heat claim follows.

The [source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) attributes classical Glauber closure, receptor heat-bath kinetics, dynamic disorder and positive realization. Its closest unresolved full-text lead is Falk (1983); the focused search does not establish priority. The earlier hub, matrix-rank and asymptotic results keep their original comparison classes.

## 5. Frozen proof provenance

The final proof SHA-256 is `de269cb3264cd972577315497d9d20ac15290ab6bdf3acc1858ce845fbfa5813`. The exact report binds that file and its verifier source. Numerical diagnostics separately bind their script, the proof, and the protocol note. [Verification](VERIFICATION.md) records the completed local gate and preserves the distinction between local checks and CI on the published commit.
