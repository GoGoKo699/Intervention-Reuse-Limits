# Controlled realization: source comparison and observation scope

Focused audit, 25 September 2026. This continues the
[central claim comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
for the [four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md).
It concerns simultaneous positive realization, reversible reduction,
and the distinction between endpoint prediction and an entire observed
process. No priority claim follows from this bounded selection.

**Assessment:** shared switched realizations and common invariant cones
are established methods. The inspected theorems do not directly give
the present positive-CTMC three-state upper together with the universal
ordinary four-state lower. The contribution remains a concrete controlled
realization separation, rather than a general realization method. Its
meaning depends on the control and observation task; enlarging that task
can remove the separation.

## 1. Primary-source comparisons

| Source and inspected result | What it explains; what still needs proof here |
| --- | --- |
| Petreczky, Bako and van Schuppen, *Realization theory of discrete-time linear switched systems*, [primary preprint, version 2](https://arxiv.org/pdf/1103.1343), Theorems 3 and 5, Procedures 2–5, Remark 12 | Shared state spaces, noncommuting word products, simultaneous reduction, and minimal dimension from generalized Hankel rank are explicit. Theorem 3 gives minimality through span-reachability and observability; Theorem 5 constructs a minimal linear realization. Thus sharing two controlled operators is not itself new. Their real-coordinate transformations do not require a stochastic simplex, a deterministic readout, continuous-time positive rates, or reversible stationary laws with a common Gibbs tilt. Rank three alone does not prove our positive three-state upper or the ordinary minimum of four. |
| Benvenuti and Farina, *A Tutorial on the Positive Realization Problem*, *IEEE TAC* **49** (2004), 651–664, [primary author text](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf), Theorem 2 and Eq. (2) | For a minimal linear realization, a suitable invariant polyhedral cone gives a positive realization. Cone generators determine the lift and its dimension through the intertwining equations. This is the standard geometric explanation of our positive realization. The stated theorem treats a single autonomous operator; applying its algebra simultaneously requires one cone invariant under every selected operator. It does not find the model-specific triangle, enforce our binary readout and force rule, or exclude reversible alternatives. |
| Fanizza, Lumbreras and Winter, *Commun. Math. Phys.* **405**, 50 (2024), [publisher full text](https://link.springer.com/article/10.1007/s00220-023-04913-4), Section 2.1, Propositions 1–2; Section 2.2 | Their multiletter quasi-realizations use a common cone invariant under all word operators; Section 2.2 recalls the classical polyhedral-cone criterion attributed to Dharmadhikari (1963). Their own realization-class separations demonstrate that common-cone obstructions and dimension comparisons are established tools. These are stationary output-word models, with symbol operators whose sum preserves normalization. Control kernels individually preserve normalization, and our endpoint task does not specify intermediate output-word probabilities. The cited criterion supplies a framework, not the present reversible-class obstruction or its particular three-state realization. |
| Huang, Ge, Kakade and Dahleh, *Minimal Realization Problems for Hidden Markov Models*, [primary preprint, version 2](https://arxiv.org/html/1411.3698v2), Definitions 1–3, Lemma 1, Theorems 1, 3 and 4 | They distinguish quasi-HMM and stochastic HMM realization, characterize rank-based reconstruction, and establish generic finite-string recovery results for the entire stationary autonomous output process. This is strong prior art for reconstructing small stochastic models from finite observations. Their generic parameter class allows stochastic emissions; deterministic emission matrices lie in a lower-dimensional subset, so generic guarantees cannot simply be imported. There is no shared controlled Gibbs family or additional reversible minimum. Conversely, our endpoint realization does not establish a smaller HMM for their whole-process task. |
| Noé, Wu, Prinz and Plattner, *Projected and Hidden Markov Models for calculating kinetics and metastable states of complex molecules*, [primary preprint](https://arxiv.org/pdf/1309.3220), Section II, Appendix A, Eqs. (18)–(20) and (30) | They construct equilibrium hidden models for projected metastable dynamics. The exact Appendix A argument assumes zero propagator eigenvalues for discarded fast modes, nonoverlapping metastable densities, and constant weighted eigenfunctions on those sets. It yields a reversible reduced transition matrix. Our finite-time finite-rate CTMC has no zero propagator eigenvalues, so that exact hypothesis fails. The practical approximation remains relevant but does not yield exact endpoint agreement for the shared field family. The stochastic emission interface is also broader than a deterministic binary state label. |
| Ullah, Bruno and Pearson, *J. Theor. Biol.* **311** (2012), 117–129, [primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3930476/), Sections 2.2–2.3 and 3.2, Eqs. (23) and (31) | An equilibrium-flux construction eliminates low-occupancy fast states. Their four-state acyclic example becomes a three-state cycle while retaining detailed balance. Thus neither a three-state cycle nor an equilibrium-preserving four-to-three reduction is new. Their approximation discards dynamics in a low-occupancy singular limit; the full and reduced first-passage laws converge as the eliminated occupancy vanishes. It is not an exact finite-parameter four-table fit or a theorem excluding every reversible model at a given state budget. |

These readings extend, rather than replace, the earlier comparisons to
Amann–Schmiedl–Seifert, Wu–Jia, Franco–Kepka–Velázquez and
Fornace–Lindsey. The [matrix-rank note](MATRIX_RANK_PREDICTION_PRINCIPLE.md)
already treats rank-based state-count comparisons. No new attribution
is claimed for that general idea.

## 2. Correction concerning “positive Markov realizations”

Taghavian and Sjölund, [*Minimal positive Markov realizations*, version 3](https://arxiv.org/html/2502.21102v3)
(2025), Sections II–III, Eq. (4), study one discrete-time SISO transfer
function using a canonical companion form built from its Markov
parameters. This terminology alone does not impose detailed balance or
continuous-time realizability.

However, the statement in the older [prior-art note](PRIOR_ART.md) that
the form does not impose stochastic normalization needs qualification.
Under their normalization that the dominant pole is one, a *positive*
matrix in Eq. (4) is column-stochastic. Its first columns each contain
one unit entry. If the monic denominator is
$z^N+c_1z^{N-1}+\cdots+c_N$, its root at one gives
$-\sum_{k=1}^N c_k=1$, which is the sum of the final column.
This is a direct deduction from their displayed matrix.

The output row remains an arbitrary nonnegative reward, rather than
our deterministic binary readout. For dimension greater than one that
companion matrix has zero diagonal entries, whereas a finite-rate CTMC
propagator has positive diagonal entries at finite time. Their result
therefore does not directly furnish our continuous-time construction,
shared control family, or reversible-class lower bound. The correction
changes the normalization wording, not the comparison's conclusion.

## 3. How the existing upper fits the established methods

The target's mean equations close on $1,S,Z$. In the affine $(S,Z)$
plane, the three-state construction uses vertices

$$
 (-1,-t),\qquad (1,-2t),\qquad (1,t+e),
 \qquad t=\tanh J,\quad e=\frac{1-t^2}{2t}.
$$

The positive rates express each vertex's drift as a nonnegative sum of
directions towards the other vertices. This gives one invariant triangle
for the selected nonnegative fields. Adding the normalization coordinate
turns it into a common polyhedral cone. Thus the upper is a concrete
application of established invariant-cone/intertwining reasoning.
The explicit triangle, its valid field range, and its compatible stationary
weights are the model-specific content.

General switched linear realization cannot replace those positivity
checks. General cone realizability does not replace finding a cone with
the required number of generators and output values. Neither gives the
four-table reciprocal-return identity that excludes all ordinary
three-state alternatives with arbitrary per-word preparations. The
complete separation is consequently not obtained by merely substituting
parameters into the inspected theorems. Its ingredients nevertheless
make it a modest explicit application, not a new universal technique.

## 4. Observation and control scope

The follow-up results are in the separately reviewed
[passive/triple proof](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md) and
[signed-control proof](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md).
They are scope statements about the same target, not conclusions established
by the cited literature.

| Prediction task | Scope conclusion and boundary |
| --- | --- |
| Passive low-field endpoint pair law for every time | A reversible three-state birth–death realization matches these laws. Thus passive pair data alone need not incur the extra ordinary state. It does not provide the same model under a second field. |
| One passive three-time law with two positive gaps | The derived lower bound is four even without detailed balance: conditional on a singleton middle sign, any three-state hidden chain makes past and future independent, whereas the target retains conditional dependence for either sign. A pair-law realization therefore need not reproduce an observed trajectory. |
| Four controlled pair tables $0,H,0H,H0$ | The established theorem gives three general states versus four ordinary states. Its lower bound allows arbitrary per-word preparations. |
| Signed-control endpoint protocols over $\{0,\pm H\}$ or $[-H,H]$, one common preparation | The exact equal-rate criterion is $3t^2u^2+(1+t^2)u\le1$. A 23-pair menu of at most five ticks per word determines the same state minimum, with a positive parameter-dependent TV margin. It uses minimal shared linear realization and an invariant triangle. Its common-preparation requirement differs from the four-word arbitrary-preparation class. |

At the existing fixture $t=4/5$, $u=3/5$, the equal-rate expression is
$1.6752>1$. Allowing both field signs requires four states even in the
general class for the richer endpoint task. Equality permits zero rates
while the constructed chain remains irreducible. Strict interior parameters
permit a small triangle perturbation with all six rates positive.

For arbitrary hidden/visible attempt ratio $r>0$, the signed proof gives
$(r+2)t^2u^2+(1+t^2)u\le r$. This extends the exact criterion within
the same published kinetic family; it is distinct from the previously
constructed one-sided unequal-rate interval. The finite menu uses one
common preparation and does not establish the same threshold for arbitrary
unrelated per-word preparations. It also does not assert that every smaller
subset of the 23 experiments has the same minimum.

The threshold is an exact application of existing realization and cone
methods. For a three-state exact fit, the richer pair data themselves
force the positive equilibrium preparation and common Gibbs stationary
family. That deduction is conditional on a fixed shared Markov model and
initialization; it is not an observation-only certification of arbitrary
physical control devices.

## 5. Scientific use and readiness

The defensible use is a model-selection benchmark for an ensemble
simulator of endpoint occupation under prescribed open-loop pulses.
It identifies when a compact predictor can retain both the selected
responses and an equilibrium interpretation at held fields. An exact
lower bound distinguishes a structural failure from an optimizer's
failure to find parameters. The scope map also tells the modeler which
extra observations or controls invalidate a proposed compression.

This is not a certified filtering model after intermediate observations,
an exact reduced microscopic mechanism, or a demonstrated hardware,
runtime or heat-cost saving. Artificial thermodynamic conclusions from
coarse models already have the precedents discussed in the central
comparison. The current evidence supports developing a precise theorem
about controlled model size and observation scope. It does not yet
establish a broad practical impact or a PRL-level significance case.

The bounded audit found no inspected theorem that directly supplies the
complete separation. That is a statement about compared hypotheses and
conclusions, not about missing keywords or exhaustive literature absence.
The older Falk full-text access gap remains as recorded in the central
comparison; no broader nonoverlap claim is made here.
