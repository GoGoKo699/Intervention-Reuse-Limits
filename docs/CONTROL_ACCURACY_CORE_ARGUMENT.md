# Control resolution and accuracy determine the required model size

**Scientific assessment, 30 September 2026.** The strongest current claim
is an attainable model-size law for a kinetic model reused across
interventions. The exact three-versus-four separation is its fine-precision
limit. This assessment consolidates existing theorems; it adds no fitted
point, numerical certificate or manuscript draft.

## 1. The core argument

Even a pair of equilibrium switches needs different reduced models at
different control speeds and prediction accuracies. Observe only the
initial and final sign of one switch, prepare the target at zero-field
equilibrium, and reuse one model across prescribed words of two fields.
Let the hidden attempt rate be $r$ times the visible attempt rate.
For fixed nonzero coupling and field, the smallest possible worst-word
error has order $r^{-1}$ with two states, $r^{-2}$ with three reversible
states, and zero with four.

These are limits over whole model classes. Positive generators attain
the upper orders; lower bounds exclude every smaller admissible model,
including models with arbitrary word-dependent preparation. A failed
fit is not used as evidence of necessity. At intermediate precision,
three states are therefore necessary and sufficient under unrestricted
two-field timing. At a fixed positive control clock, two reversible
states already achieve the quadratic order. The extra state retains
a leading hidden lag that fast control exposes.

At finer precision, the distinction changes: a general positive
three-state predictor is exact, while preserving ordinary detailed
balance requires four states. This additional equilibrium requirement
appears at second order. Thus leading predictive memory and the cost of
an equilibrium interpretation are separate effects.

The concrete modeling decision is which state budget can meet a stated
accuracy requirement across the allowed controls. It is not enough to
fit relaxation at each held field separately. The result supplies an
explicit benchmark for models intended to transfer between protocols,
with sufficient constructions and necessary limits under one interface.

The boundary results keep that interpretation honest. Strong coupling,
extreme fields or separated rates do not provide a route to a fixed
positive equilibrium-specific penalty at a parameter boundary. A large
interior gap remains unproved. The established outcome is a narrow
controlled-kinetics law; practical memory, heat and device advantages
have not been demonstrated.

## 2. One contract and an explicit model-selection rule

The target is the four-state heat-bath model with energy $-JSZ-hS$,
$t=\tanh J\in(0,1)$, $u=\tanh H\in(0,1)$ and
$r=\Gamma_Z/\Gamma_S$. Keep $t,u$ fixed as $r\to\infty$.
The initial target law is $(1+tSZ)/4$. The task comprises all finite
open-loop words at fields $0,H$, with arbitrary held durations and
true initial/final binary records. There are no intermediate observations
or feedback.

One reduced state space, deterministic binary readout and one
continuous-time generator per field must serve every word. All persistent
states count. Reversible models retain normalized Gibbs-related stationary
laws, with unknown tilt; preparation may vary arbitrarily with the word.
There is no rate cap, stationary-mass floor or preparation-equilibrium
promise. The general class can drop detailed balance and the Gibbs
premise for the conclusions below.

Let $E_d^{\rm rev}$ denote the infimum over at-most-$d$-state reversible
models of their supremum pair-TV error over those words. The
[rapid-control theorem](FAMILIAR_SWITCH_RAPID_CONTROL.md) gives

$$
E_2^{\rm rev}=\Theta(r^{-1}),\qquad
E_3^{\rm rev}=\Theta(r^{-2}),\qquad E_4^{\rm rev}=0.
$$

Its two-state lower holds for general models too. The
[exact positive-realization boundary](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md)
gives a general three-state model for all sufficiently large $r$.
Hence, for tolerance $\epsilon(r)=r^{-p}$, the eventual minimum counts are:

| Required precision | General states | Reversible states |
| --- | ---: | ---: |
| $0<p<1$ | 2 | 2 |
| $1<p<2$ | 3 | 3 |
| $p>2$ | 3 | 4 |

This table is a direct corollary, not a new independent theorem. For
example, $r^{-2}\ll\epsilon\ll r^{-1}$ lies above the three-state
upper and below the two-state lower. A one-state binary-readout model
has error at least $1/2$ from the balanced initial sign, excluding it
in the first row. The cases $p=1,2$ depend on constants and are not
settled by the order notation.

For the separate task with fixed positive low/high ticks, the
[clocked theorem](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) gives quadratic
two-state error uniformly over word length and horizon. Both classes
then need two states for $0<p<2$; for $p>2$, the minima are three
general and four reversible states. Fixed clocks remove the separated-order
three-state window, without excluding a constant-factor advantage at
$\epsilon=\Theta(r^{-2})$. Clocked lower bounds also cover the broader
stochastic-kernel class, and the upper constructions are continuous-time.

## 3. Why the third and fourth states play different roles

Correcting a two-state relaxation rate can absorb the leading hidden
slowing at a held field. Under arbitrarily rapid field mixtures, those
same corrected rates predict a stationary visible response that differs
from the target by order $r^{-1}$. Held-field matching fixes the
two-state parameters, so choosing a different two-state fit cannot
remove both discrepancies. A third reversible state retains the lag
through one field-independent change of coordinates and restores
order $r^{-2}$ uniformly across words.

The remaining fourth-state obstruction uses a different mechanism.
Three states with a binary readout have a sign represented by a single
state. Detailed balance links reversed control orders and forces a
return identity for that sign. The target violates the corresponding
identity in both signs. Two transfers of hidden response make the
preparation-free seven-word violation quadratic in $r^{-1}$.
The positive three-state general predictor shows that this finer
requirement comes from retaining equilibrium structure.

A nonreversible fitted predictor does not demonstrate stationary
dissipation in the target at a held field. Switching the field is itself
a driven protocol. Three and four abstract states also require the same
number of fixed binary register bits. Model-size necessity should not be
presented as hardware or heat savings.

## 4. The nearest theory already covers important ingredients

The following is a focused theorem comparison, not a literature-wide
priority certificate. The [earlier comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
covers reciprocal-response and hidden-equilibrium inference; its stated
full-text access gap remains.

| Primary result and inspected passage | What is established and the scope of the present comparison |
| --- | --- |
| Grigoletto and Ticozzi, [*Algebraic Reduction of Hidden Markov Models*](https://arxiv.org/pdf/2208.05968v2), Problems 1–2, Theorems 1–2 and Proposition 4 | Stochastic reductions already exploit selected preparations and distinguish single-time from multitime output preservation; an observable class admits an optimal algebraic reduction. These distinctions themselves are not new here. Their autonomous HMM output may be stochastic. Our claim adds the specified controlled, deterministic-readout equilibrium constraint and matched class-wide error orders. |
| Grigoletto, Viola and Ticozzi, [*Model Reduction for Controlled Quantum Markov Dynamics*](https://arxiv.org/html/2510.25546v1), Proposition 2, Theorem 1 and the following paragraph | One physical reduced generator family preserves expectations for every initial state, control and time. Minimality is explicitly relative to its algebra-projection procedure. Our lower bounds range over all admissible small positive realizations, but our target-preparation task is narrower. A smaller model here is not an improvement on their all-state guarantee. |
| Brandner, [*Dynamics of Microscale and Nanoscale Systems in the Weak-Memory Regime*](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.037101), Eqs. (8)–(14), (21)–(25) | Autonomous effective generators, initial slippage and systematic memory corrections have rigorous precedents. Corrected relaxation rates are not a new method. The present comparison concerns attainable state counts under shared controls, with positive Gibbs constructions and lower bounds over the stated rival classes. |
| Meyer and Brandner, [*Weak-Memory Dynamics in Discrete Time*](https://arxiv.org/html/2510.26325v2), Eqs. (5)–(13), Floquet discussion and Supplement, Sections I–II | Weak-memory reduction already covers periodically driven coarse-graining through the transition matrix of a chosen complete period. A cycle-specific effective matrix with slippage need not factor into one generator for each physical field that also fits held-field data. Our reuse requirement and class-wide lower are distinct. This 2026 result rules out treating driven weak-memory reduction itself as an open subject. |

A short check makes the preparation distinction concrete. At zero field,
$Q_0S=-S+tZ$. Suppose exact visible means were required from all four
target point preparations. A three-state deterministic readout has a
singleton sign $s$. Both initial states $(s,+1)$ and $(s,-1)$ must
then prepare that singleton, because their time-zero means are the
extreme value $s$. Their reduced initial slopes would coincide, while
the target slopes $-s+t$ and $-s-t$ differ. Thus that stronger task
already requires four states passively, without detailed balance.
Likewise, the observable space $\operatorname{span}\{1,S,Z\}$ has
pointwise algebra closure $\operatorname{span}\{1,S,Z,SZ\}$.
Retaining four states in an all-state algebraic reduction is therefore
expected. This explanatory calculation does not alter our fixed target
preparation or the rival's allowed preparation freedom.

The defensible candidate addition is the combined attainable hierarchy
under the declared interface. Shared-control reduction, task dependence,
reciprocity, trace elimination and effective-rate corrections are
established tools. Their presence does not by itself supply these lower
bounds, and their presence also prevents a broad first-discovery claim.

## 5. Decision and the next analytic gate

**Decision:** lead the research with the control/accuracy/model-size law.
The exact equilibrium state separation and the
[uniform trace and interior bounds](FAMILIAR_SWITCH_TRACE_REDUCTION.md)
support and delimit that claim. The current evidence supports a coherent
narrow theory result; it does not yet establish broad physical impact.
Another fourth-state operating-point search or acquisition refinement
would not address the strongest remaining question.

The missing link is a finite-bandwidth consequence. The current
two-state lower takes an arbitrarily rapid product limit and then a
long-time limit inside the all-word supremum. It does not prove that a
specified finite pulse train forces the same first-order error.

The next task is to test one explicit family: held-field calibration
words together with a periodic low/high word whose dwell lengths are
fixed multiples of $1/r$. Seek a constant $c>0$ and an explicit finite
horizon or pulse count for which every reusable two-state model has
pair error at least $c/r$. The existing three-state upper already
supplies order $r^{-2}$ on that restricted family. One failed two-state
fit is insufficient; the lower must allow all the existing rival
preparation and rate freedom. The leading memory requirement would then
have a definite control-time condition. It would remain a third-state
result, separate from the finer equilibrium-specific fourth-state cost.

This timing scale has a physical interpretation within the
[published kinetic model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md): holding
$\Gamma_Z$ admissible and setting $\Gamma_S=\Gamma_Z/r$ converts
a dimensionless dwell $\kappa/r$ to physical duration
$\kappa/\Gamma_Z$. Total duration must also be reported. Finite ramps
and a detector are further requirements, not consequences of this
rescaling.

If the specified family permits an $o(r^{-1})$ two-state fit, record
that limitation and reconsider the control contract; do not infer a
class-wide finite-bandwidth advantage from the ideal supremum. This
single analytic gate is the next justified calculation. No new
simulation, verifier or sampling budget is needed for this assessment.
Manuscript writing remains on hold.
