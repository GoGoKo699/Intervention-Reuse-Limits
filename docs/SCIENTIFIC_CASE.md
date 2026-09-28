# The scientific case: when a small predictor stops being an equilibrium model

**Current assessment, 28 September 2026.** The strongest established result
is a controlled model-reduction benchmark: the smallest exact Markov predictor
of an equilibrium system can need extra states when it must preserve
equilibrium structure, handle a larger control range, or predict an
additional observation. These requirements are mathematically distinct.
The project gives exact separations and explicit boundaries in a familiar
physical model. Its wider practical importance remains an open research
question; the number of certificates does not answer it.

The immediate modeling decision is concrete. Before interpreting a fitted
kinetic model mechanistically, specify its controls, temporal observations,
preparation and equilibrium requirements. Agreement with the requested
endpoint pairs alone does not justify using it for a richer task. Our
theorems exhibit this failure even when the pair predictions are exact.

## One physical system, different modeling requirements

The target consists of two interacting, time-even binary configurations
$S,Z$, with energy $-JSZ-hS$ and ordinary heat-bath transition rates.
Only $S$ is observed and directly driven. Each held-field generator obeys
detailed balance. The same four-state process is also an equilibrium
specialization of a published sequential-tunneling model for coupled
charge occupations; the [community-model derivation](FAMILIAR_SWITCH_COMMUNITY_MODEL.md)
states its weak-coupling, retained-level and control assumptions.

For equal attempt rates, finite positive coupling and positive observation
gaps, the existing results give the following exact state counts. The target
starts from zero-field equilibrium; $L$ denotes a zero-field pulse and
$H>0$ a positive-field pulse. Time is measured in units of the inverse common
attempt rate. States include all persistent Markov memory and have a
deterministic binary readout.

| Prediction task | General Markov states | Reversible states | Essential conditions |
| --- | ---: | ---: | --- |
| All passive initial/final pairs | 3 | 3 | A shared passive model and preparation |
| Four controlled pairs: $L,H,LH,HL$ | 3 | 4 | Same physical Gibbs force rule; rival preparations may differ by word |
| One passive three-time joint law | 4 | 4 | The middle observation is ideal and nondisturbing; no rival equilibrium premise |
| Signed-control endpoint pairs | 3 or 4, with an exact boundary | 4 | One common preparation and shared continuous-time generators; a 23-word menu suffices |

These are different tasks, not interchangeable experimental guarantees.
The proofs are collected in the [control-scope assessment](FAMILIAR_SWITCH_CONTROL_SCOPE.md).
The three-state upper is a positive Markov model, not merely a fit using
three real coordinates. It does not reproduce the full visible process.
Both three and four abstract states can use two fixed binary register
bits; a physical storage, heat or speed advantage has not been established.

## The mechanism can be explained without a parameter table

Knowing the visible sign need not reveal how the system will respond:
the hidden configuration $Z$ still changes its future response. A binary
readout on three states necessarily has a sign that identifies a single
state. Within that sign, a three-state model has no hidden variation left.

Detailed balance turns suitable opposite-order responses into conditional
covariances. The two-switch target has nonzero response variation within
both signs, so a reversible model must retain at least two states of each
sign. A positive predictor that relaxes detailed balance can nevertheless
reproduce the specified pair statistics on three states. This is a cost
of retaining an equilibrium interpretation of those statistics. A
circulating fitted model does not demonstrate dissipation in the target.

The third observation exposes the same hidden variation more directly.
For passive observations $X=S_0$, $M=S_a$, $Y=S_{a+b}$, put
$t=\tanh J$ and $d_v=e^{-v}\sinh(tv)$. The target obeys

$$
\operatorname{Cov}(X,Y\mid M=s)=(1-t^2)d_a d_b>0,
\qquad s=\pm1.
$$

In a singleton middle-sign sector, a Markov model instead makes past and
future conditionally independent. Thus four states are necessary even
without detailed balance. This short argument explains why an exact pair
predictor is insufficient after an additional observation. The
[three-time proof](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md) supplies the
full state-count and finite-error statements.

The control boundary is equally explicit. For field range $[-H,H]$, let
$u=\tanh H$ and $r=\Gamma_Z/\Gamma_S$. A common three-state positive
continuous-time predictor exists exactly when

$$
(r+2)t^2u^2+(1+t^2)u\le r.
$$

The linear mean dimension stays three on both sides. Positivity under
the enlarged control range causes the extra state requirement. In this
[signed-control theorem](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md), an
exact three-state fit to the richer common-preparation data must inherit
the Gibbs stationary family even though it was not imposed on the rival.
This addresses a substantive assumption concern, at the stated cost of
requiring one common preparation.

## Which assumptions carry the conclusion?

The heat-bath dynamics and charge-model embedding have independent
physical precedents. The small-model comparison additionally specifies
what the reduced model must retain. In the four- and seven-word results,
the field acts through the measured sign: $\pi_h\propto\pi_0e^{hS}$,
or through its unknown-tilt version. A fixed reduction that never mixes
the visible signs inherits this relation by summing equilibrium weights;
see the [equilibrium-reduction derivation](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md).
An arbitrary hidden-state fit with unrelated field-dependent energies
need not satisfy it. The seven-word data remove numerical tilt calibration
and rival preparation promises, but do not remove the force convention.

Ideal boundary observations define the prediction task. A physical meter
must separately meet the relevant registration and disturbance conditions.
All persistent memory affecting subsequent predictions belongs in the
state count. The target is reversible while a field is held; switching
the field is a driven protocol. None of these statements establishes the
combined accuracy specification of an actual device.

## A finite-accuracy lesson from fast hidden relaxation

The [new short analytic bound](FAMILIAR_SWITCH_FAST_RELAXATION.md) gives
a useful limit without fitting or simulation. At fixed $0<t<1$, there
is an explicit ordinary reversible two-state model for which

$$
\sup_w\operatorname{TV}(P_w,\widetilde P_w)
\le \min\!\left\{1,\frac{t^2}{r(1-t^2)}\right\}.
$$

Both models start from their low-field equilibrium, and the supremum
covers every predetermined finite signed-field word and every horizon.
The same two-state rates serve all words. The bound concerns endpoint
pairs; it does not claim uniform approximation of full trajectories or
feedback experiments with intermediate observations.

Increasing the hidden attempt rate can enlarge the range allowing exact
three-state prediction. Yet as that rate becomes large, even a reversible
two-state model approximates all the requested pairs. Exact state-count
boundaries and useful finite-accuracy distinctions therefore ask different
questions. Fast equilibration is an established reduction principle;
the displayed uniform bound makes its consequence explicit for this task.
It does not identify an optimal operating point or a sharp error rate.

The longer-chain result supplies a second boundary. Exact counts
$n+1$ versus $2n$ are already attained throughout a fixed weak-coupling
range. But the [chain approximation theorem](FAMILIAR_CHAIN_FINITE_ACCURACY.md)
shows that truncating distant spins approximates every endpoint word
uniformly in time. Thus exact growth with chain length does not establish
a growing state penalty at fixed accuracy. Extending exact counts alone
is no longer the missing scientific step.

## Relation to established theory

The candidate contribution is the explicit combination of attainable
state counts, physical control and observation boundaries. The general
ingredients have substantial precedents. The following focused
comparisons explain the distinction; they do not certify priority.

| Primary result | Established idea and remaining distinction |
| --- | --- |
| Grigoletto, Viola and Ticozzi, [controlled quantum Markov reduction](https://arxiv.org/html/2510.25546v1), Propositions 1–2 and Theorem 1 | Observable subspaces and algebra closure give exact physical reductions under control. This supplies a general framework; it does not state the present binary-readout minima or signed-field threshold. Our preparation-specific pair realization also asks less than preservation for every initial state. |
| Franco, Kepka and Velázquez, [reciprocal-response characterization](https://doi.org/10.1007/s00205-026-02183-7), Eq. (1.2), Propositions 3.8–3.9 | Detailed balance constrains reciprocal responses, and comparing two times removes an unknown constant. These principles precede our witness. Their resolved responses under one generator do not supply the complete shared-control positive-realization separation. |
| Strasberg and Esposito, [equilibrium coarse-graining](https://arxiv.org/pdf/1703.05098), Section II C, Eqs. (25)–(28) | Fast conditional equilibration produces effective rates with detailed balance. The new two-state approximation is an application of that physical principle, with a direct finite-rate, all-word endpoint-error proof for this model. |

The earlier [central-claim comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
and [control-scope audit](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md)
also address positive realization, hidden-Markov inference and spurious
thermodynamic interpretations. Their stated limitations remain, including
an older equilibrium-reduction source whose full text was unavailable.

## What the numerical work does, and the next decision

The universal identities, constructions and impossibility arguments are
analytic. Exact interval calculations certify selected margins and
statistical budgets; saved fits supply admissible comparison models.
Those computations establish their specified inequalities. They do not
establish novelty, physical relevance or a device's performance.

The latest [seven-word information bound](FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md)
shows that one preparation-free design intrinsically needs a budget above
one hundred million complete pairs under its specified observation
contract. This is a limitation of that experiment. It is not the central
reason to study the theorem, and the burden must not be generalized to
other controls, preparations or richer observations.

**The next scientific question is an accuracy-dependent law for the cost
of preserving equilibrium structure:** how does the observable strength
of hidden response variation control the best reversible approximation,
compared with an unrestricted positive predictor? Existing rank and
covariance proofs provide lower bounds; fast relaxation and chain
truncation provide upper bounds. Their physical and quantitative relation
remains unresolved. A useful answer should explain a parameter regime or
give a family-wide obstruction, rather than report a better fitted point.
It should decide whether retaining equilibrium requires an additional
state at a scientifically justified error tolerance under one shared
observation and control contract. Showing that the apparent benefit
disappears under that contract would also answer the question.

The working rule is to state that question, its modeling consequence and
the analytic route before requesting another calculation. A small
calculation is warranted only when it resolves a named obstruction or
checks a delicate step. Further acquisition-constant tuning and manuscript
drafting remain deferred. The present defensible outcome is a precise
structural benchmark; a broader impact claim still needs an argument.
