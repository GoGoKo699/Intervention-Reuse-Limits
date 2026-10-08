# The scientific case: control, accuracy and reusable model size

The research establishes an attainable state-count law for a familiar equilibrium kinetic model
reused under control. A third state retains the leading hidden lag exposed
by rapid switching; a fourth is needed to preserve equilibrium structure
at finer precision. A specified three-experiment menu already witnesses
the leading third-state requirement.

The scientific decision is which state budget can satisfy a stated
prediction tolerance across allowed controls. Separate fits at held fields
do not settle whether one model transfers between protocols. The proofs
supply both sufficient constructions and class-wide necessary limits.

## 1. The prediction contract

The target has two time-even binary configurations $`S,Z`$ with energy
$`-JSZ-hS`$ and heat-bath rates. Write $`t=\tanh J\in(0,1)`$,
$`u=\tanh H\in(0,1)`$ and $`r=\Gamma_Z/\Gamma_S`$. The precision laws
keep $`t,u`$ fixed as $`r\to\infty`$; time is in units of $`1/\Gamma_S`$.
The [community-model derivation](FAMILIAR_SWITCH_COMMUNITY_MODEL.md)
connects this target to a selected equilibrium, wide-band, spinless
sequential-tunneling model and records its physical approximations.

| Part of the contract | Requirement |
| --- | --- |
| Target preparation | Zero-field equilibrium, $`\pi_0(S,Z)=(1+tSZ)/4`$ |
| Observations | True initial/final signs of $`S`$; no intermediate observation or feedback |
| Control | Prescribed holds at fields $`0,H`$; ideal changes leave the state unchanged |
| Reusable rival | One persistent state space, deterministic binary readout and one fixed continuous-time generator per field |
| Preparation freedom | Rival preparation may depend arbitrarily on the entire word; no equilibrium-preparation promise or rate cap |
| Equilibrium class | Ordinary detailed balance for normalized nonnegative stationary laws with a shared Gibbs tilt through the visible sign; the tilt is unknown |
| General class | Positive Markov generators without the detailed-balance or Gibbs premise for the general minima stated below |

All persistent states count, including preparable zero-weight transients.
The endpoint-pair task is narrower than preserving every initial state
or every observed trajectory. Switching is a driven protocol even though
each held-field target generator is reversible.

## 2. What the theorems establish

Let $`E_d`$ be the infimum, over at-most-$`d`$-state reusable rivals, of the
maximum endpoint-pair total-variation error over the specified menu.
The menu is part of the theorem; lower bounds do not automatically
transfer to a smaller set of experiments.

| Control menu | Established error statement | Evidence |
| --- | --- | --- |
| All finite two-field words, arbitrary held durations | Two states have $`\Theta(r^{-1})`$ error, even in the general class; three reversible states have $`\Theta(r^{-2})`$ error; four are exact | [R93](FAMILIAR_SWITCH_RAPID_CONTROL.md), with the three-state lower from R92 |
| All words at fixed positive low/high ticks | Two reversible states attain $`O(r^{-2})`$; the two-state general lower and three-state reversible lower have the same order | [R92](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md); its lower also covers the stated broader stochastic-kernel null |
| Two held calibrations and one specified finite train | Two-state error is $`\Theta(r^{-1})`$; an existing reversible three-state model attains $`O(r^{-2})`$ | [R98](FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md), inheriting the upper from R93; no three-state lower or fourth-state claim on this restricted menu |
| All two-field words, exact general prediction | A positive three-state model exists for all sufficiently large $`r`$ without a Gibbs premise on the rival | [R94](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md), which supplies the exact rate threshold |

For the all-duration menu, these results imply the eventual minimum
counts at tolerance $`\epsilon(r)=r^{-p}`$:

| Precision exponent | General states | Reversible states |
| --- | ---: | ---: |
| $`0\lt p\lt 1`$ | 2 | 2 |
| $`1\lt p\lt 2`$ | 3 | 3 |
| $`p\gt 2`$ | 3 | 4 |

A one-state deterministic readout already misses the balanced initial
sign by TV at least $`1/2`$. At fixed positive ticks, both classes instead
need two states for $`0\lt p\lt 2`$; for $`p\gt 2`$ their minima are three and four.
For the all-duration menu, $`p=1,2`$ depend on constants; at fixed positive
ticks only $`p=2`$ is a crossover. A possible constant-factor three-state
advantage at the quadratic crossover remains outside the order-level
statements.

## 3. The mechanism and its finite witness

The hidden configuration changes the visible response even when the
visible sign is known. At a held field its leading effect can be absorbed
into a corrected two-state relaxation rate. Rapid switching exposes the
remaining lag. A third reversible state retains that lag through one
field-independent change of mean coordinates, giving quadratic accuracy
uniformly over words and horizons.

The finite witness makes the reuse failure concrete. Put
$`n=\lceil r/2\rceil`$, $`A=n/r`$ and use the holds $`L_A,H_A`$ together
with $`W=(L_{1/r}H_{1/r})^n`$. For a two-state model containing both
visible signs, let $`a_w`$ be half the difference of its conditional final
means from the two initial signs.
The same generators force $`a_W=a_{L_A}a_{H_A}`$. The target contrasts
$`C_w`$ instead satisfy

```math
C_W-C_{L_A}C_{H_A}
=\frac{e^{-\bar c}\chi}{r}+O(r^{-2}),\qquad \chi\gt 0.
```

R98 gives $`\bar c,\chi`$ explicitly and converts the absolute residual
to a universal pair-TV lower by dividing by twelve, while retaining
arbitrary rival preparations. This proves the intermediate-accuracy
third-state window on just three settings. The train has
$`2\lceil r/2\rceil`$ segments, so its length is not fixed as $`r`$ grows.

The fourth-state obstruction is separate. With three states and binary
readout, one sign identifies a singleton state. Detailed balance with the
shared Gibbs rule then
forces a reverse-order return identity that the target violates in both
signs. Two transfers of hidden response make the seven-word violation
quadratic in $`r^{-1}`$. A general positive three-state predictor is exact
in the fast-hidden regime; retaining equilibrium structure is therefore
the additional fine-precision requirement.

## 4. Relation to existing work and the role of supporting evidence

The [scientific background guide](MANUSCRIPT_BACKGROUND.md) consolidates
the mathematical language, physical citation chain and closest-result
comparisons, with a [focused bibliography](../references/manuscript.bib).
The selected teaching anchor is Bo–Celani. The
[tutorial-to-result narrative](../REVIEW.md) connects its fast-variable
averaging framework to this prediction task and the existing proofs.
[Further reading](TUTORIAL_OPTIONS.md) provides additional mathematical
and stochastic-process background.

The [bounded primary-source comparison](CONTROL_ACCURACY_CORE_ARGUMENT.md#4-the-nearest-theory-already-covers-important-ingredients)
already records preparation-specific HMM reduction, shared controlled
Markov reduction, effective rates and slippage, and periodically driven
weak-memory approximation. These ingredients are established. In
particular, Meyer–Brandner's 2026 result covers a complete-period Floquet
map; driven reduction itself is not an open subject.

The candidate contribution is the combined attainable state hierarchy
under the declared interface, with lower bounds over all admissible small
positive realizations. One pair of field generators must serve both
calibration and driven words. The comparison is narrower than an all-state
controlled-reduction guarantee and does not establish broad priority.
The source audit records a full-text access gap; the comparison is bounded
by the inspected sources.

The [finite-rate bounds](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md) and
[uniform trace reduction](FAMILIAR_SWITCH_TRACE_REDUCTION.md) delimit the
fourth-state effect: parameter extremes do not produce a fixed positive
equilibrium-specific penalty in the exact general-three-state regime.
A large interior gap is unproved. The chain, signed-control and
additional-observation results remain supporting task-boundary examples;
they do not enlarge the present core claim.

The current hierarchy and finite-pulse witness are analytic. Saved fits,
interval certificates and acquisition calculations support their own
specified tasks. Their margins or sample counts do not transfer to R98.

## 5. Physical interpretation and evidence

The [proof review](FINAL_SANITY_AUDIT.md) records the analytic checks of
the central arguments and the scope of the reproducibility evidence.

| Scope question | Interpretation |
| --- | --- |
| Finite ramps, detector behavior and sampling costs | Unproved implementation requirements for this menu; guarantees for other observation contracts do not transfer automatically |
| Pulse count and physical time | At fixed $`\Gamma_Z`$, each pulse lasts $`1/\Gamma_Z`$ and the train lasts $`2\lceil r/2\rceil/\Gamma_Z`$ |
| Hardware bits, heat savings and a large useful error gap | No such benefit is established; three and four abstract states both fit in two fixed register bits |
| Broad significance and complete priority | The source comparison is bounded by the inspected works and does not certify exhaustive priority or broad impact |
| External review | Internal analytic reviews and reproducibility checks are recorded; external endorsement is not claimed |

The [theorem-scope page](PUBLICATION_SCOPE.md) collects the comparison
classes and boundaries. The [verification guide](VERIFICATION.md)
provides the reproduction commands and explains the evidence types.
