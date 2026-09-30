# Intervention Reuse Limits

**Control speed and prediction accuracy determine how many states a reusable kinetic model needs.**

A model that fits relaxation at two held fields can still miss the response
when those fields alternate. For two interacting equilibrium switches,
we prove which state budgets can meet a requested accuracy while one model
is reused across the controls. The results combine explicit positive
models with lower bounds against every admissible smaller model.

## The result

Let $r$ be the hidden-to-visible attempt-rate ratio, with nonzero coupling
and field held fixed as $r$ grows. Observe only the initial and final
visible sign, starting the target at zero-field equilibrium. For all
finite two-field words with arbitrary held durations, the eventual
minimum state counts at error tolerance $\epsilon(r)=r^{-p}$ are:

| Required precision | General model | Reversible model |
| --- | ---: | ---: |
| $0<p<1$ | 2 states | 2 states |
| $1<p<2$ | 3 states | 3 states |
| $p>2$ | 3 states | 4 states |

Reversible rivals retain the stated normalized Gibbs force relation with
unknown tilt. Rival preparations may vary by word; rates are uncapped.
The crossover cases $p=1,2$ depend on constants and are not settled by
these orders. At fixed positive low/high ticks, two states already attain
quadratic error: the separated-order three-state window depends on control
timing. The [scientific guide](docs/SCIENTIFIC_CASE.md) gives the full
contract and theorem dependencies.

The finite-control consequence uses just three experiment settings:
low-field hold, high-field hold, and an alternating train with the same
total residence at each field. Every two-state model has an exact
conditional-contrast multiplication rule. The target violates it at
order $r^{-1}$, while a reversible three-state model has error $O(r^{-2})$
on the same menu. The [finite-pulse proof](docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md)
specifies $2\lceil r/2\rceil$ held segments of duration $1/r$ and a
bounded dimensionless horizon. Three settings therefore contain a growing
pulse count. This restricted menu establishes the third-state requirement;
the fourth-state lower belongs to the separate seven-word/all-word task.

## Read the case

| Reading step | What it answers |
| --- | --- |
| [Scientific guide](docs/SCIENTIFIC_CASE.md) | The core claim, assumptions, evidence map, source distinction and drafting status |
| [Three-experiment proof](docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md) | Why held-field responses cannot be reused by any two-state model at the stated accuracy |
| [All-duration law](docs/FAMILIAR_SWITCH_RAPID_CONTROL.md) and [fixed-clock law](docs/FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) | How the best attainable error changes with control timing |
| [Community model](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md) | Which published kinetic assumptions support the physical target |

The physical model, endpoint observation contract and theorem scope are
frozen. The pre-drafting evidence package is ready for a focused theory
manuscript. **Manuscript writing is on hold.** Broad publication significance
and practical device benefit remain unestablished.

Ideal field jumps and true endpoint records define the task. At fixed
hidden attempt rate, the pulse-train duration grows with $r$. The results
supply no finite-ramp, detector, sampling, hardware-bit or heat-saving
guarantee for that menu. These limitations remain part of the scope.

[Current work](work_orders/CURRENT.md) · [Claim ledger](docs/CLAIM_LEDGER.md) · [Verification](docs/VERIFICATION.md) · [Publication status and history](docs/PUBLICATION_SCOPE.md)

<details>
<summary>Preserved overview and research history before consolidation</summary>

The following overview is historical. Its earlier “current” and “next”
statements record decisions at those checkpoints; the guide and status
above supersede them. The original text and evidence links are retained.

# Intervention Reuse Limits

**What must a model remember when its predictions must survive interventions?**


A small model can predict an equilibrium system exactly for one task and
need more states when the task changes. This project studies the cost of
preserving equilibrium structure while reusing a kinetic model under
control. The main example is a pair of interacting heat-bath switches,
with an explicit connection to a published coupled-charge model.

## The central result: control speed and accuracy select model size

For a pair of interacting switches, a model reused across two controlled
fields has an accuracy-dependent state requirement. With fixed coupling
and field, let $r$ be the hidden-to-visible attempt-rate ratio. As
$r$ grows, the smallest worst-protocol endpoint-pair error is
$\Theta(r^{-1})$ for two states and $\Theta(r^{-2})$ for three
reversible states; four states are exact. These bounds cover arbitrary
held durations, switching counts and horizons under the stated interface.

A fixed positive control clock changes the conclusion: two reversible
states already achieve quadratic error. Thus rapid control exposes the
need for a third state at intermediate precision; only finer precision
exposes the fourth state required by equilibrium structure. The
[core argument and source comparison](docs/CONTROL_ACCURACY_CORE_ARGUMENT.md)
state the exact model-selection rule, assumptions and remaining physical
question. The finite-pulse result below closes its specified timing test;
finite ramps remain outside the theorem.

Three experiments now suffice to expose the leading memory requirement:
hold the low field, hold the high field, and alternate those fields with
the same total residence time at each. Every reusable two-state model
obeys an exact multiplication rule for its conditional contrasts. The
target violates it at order $r^{-1}$; the existing reversible three-state
model has error $O(r^{-2})$ on this same menu. The
[finite-pulse proof](docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md)
specifies $2\lceil r/2\rceil$ segments of duration $1/r$ and a total
dimensionless horizon below $1+2/r$. Three settings do not mean a fixed
short pulse sequence. Ideal field jumps and endpoint-only observations
are retained.

## Exact state counts

For equal attempt rates, finite positive coupling, positive observation
gaps and a finite nonzero controlled field, the four-state target starts
from zero-field equilibrium. Its exact minimum number of predictive
Markov states depends on what the model must reproduce:

| Required observations and controls | General model | Reversible model |
| --- | ---: | ---: |
| Passive initial/final pairs, with one common preparation | 3 | 3 |
| Four controlled pair laws, retaining the physical Gibbs force rule | 3 | 4 |
| One passive three-time law, with an ideal nondisturbing middle observation | 4 | 4 |
| Signed-control pairs, with one common preparation | 3 or 4 across an exact control boundary | 4 |

These are separate prediction contracts. Rivals have a deterministic
binary readout and count all persistent Markov states. The four-pair
comparison allows arbitrary preparation for each word; the signed-control
comparison requires one common preparation and derives the Gibbs relation
for any exact three-state fit. See the [scientific case](docs/SCIENTIFIC_CASE.md)
for the assumptions and physical interpretation.

The mechanism is hidden response variation within each visible sign.
Detailed balance forces a reversible predictor to retain that variation
in both signs. An unrestricted positive predictor can reproduce the
specified endpoint pairs with fewer states, but it cannot thereby predict
an entire observed trajectory or establish physical memory or heat savings.

## What is established, and what matters next

The state counts and control boundaries follow from analytic constructions
and impossibility proofs. The [control-scope map](docs/FAMILIAR_SWITCH_CONTROL_SCOPE.md)
is the compact theorem guide. The [physical model](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md)
and [source comparison](docs/FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
explain the inherited assumptions and closest precedents.

Finite accuracy can change the conclusion. A [short new analytic bound](docs/FAMILIAR_SWITCH_FAST_RELAXATION.md)
shows that fast hidden relaxation makes a reversible two-state model
approximate every prescribed endpoint-pair protocol uniformly in time.
The [chain approximation theorem](docs/FAMILIAR_CHAIN_FINITE_ACCURACY.md)
similarly limits the meaning of exact state-count growth. The latest
seven-word acquisition analysis identifies a costly experimental design;
it is supporting scope evidence, rather than the lead scientific claim.

The [rapid-control theorem](docs/FAMILIAR_SWITCH_RAPID_CONTROL.md)
now resolves the fast-hidden regime even when pulse durations shrink.
At fixed coupling and two field values, with hidden/visible rate ratio
$r$, the best all-protocol error is of order $r^{-1}$ for two states
and $r^{-2}$ for three reversible states under the stated Gibbs and
readout requirements; four states are exact. One explicit equilibrium
three-state chain works at every switching speed and horizon. It retains
a fast internal mode, and its error does not accumulate at switches.
Rapid control can expose the need for a third state, while the fourth
equilibrium state remains a second-order precision requirement. These
are analytic bounds for endpoint pairs, not a device-performance claim.

The [finite-rate bounds](docs/FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md)
now rule out several simple routes to a larger signal. At fixed coupling,
both weak and nearly saturating fields admit accurate equilibrium
three-state models. Strong coupling also suppresses the distinction,
either uniformly in time at a fixed field or over bounded horizons when
the field grows with it. A separate [exact rate boundary](docs/FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md)
shows when slow hidden dynamics require four states even without
reversibility. A large observable equilibrium-specific gap in the
remaining parameter region has not been established.

The [trace-reduction theorem](docs/FAMILIAR_SWITCH_TRACE_REDUCTION.md)
closes that long-time corner. Retaining the transition route through one
rare configuration gives a reversible three-state model with endpoint-pair
error at most $3(1-\tanh J)/2$, uniformly over every positive rate ratio,
nonnegative field sequence, switching speed and observation time.
Together with the earlier bounds, any fixed positive equilibrium-specific
penalty must lie in an interior parameter region. The theorem does not
establish a large gap there. Its physical lesson is that rare occupation
can be removed while its transition flux must be retained.

The selected finite-pulse test is complete. The project is now in
convergence: freeze the physical model, observation contract and theorem
scope, and consolidate the established core argument and evidence.
The three-setting result concerns the third predictive state; it does
not establish fourth-state necessity on that restricted menu. Pulse count
and physical observation time grow with the rate ratio when the hidden
rate is fixed. Broad practical significance and device feasibility remain
unresolved. These are stated limitations, not automatic new research
branches. Manuscript writing is on hold.

[Core argument](docs/CONTROL_ACCURACY_CORE_ARGUMENT.md) · [Model scope](docs/SCIENTIFIC_CASE.md) · [Current work](work_orders/CURRENT.md) · [Claim ledger](docs/CLAIM_LEDGER.md) · [Verification](docs/VERIFICATION.md)

<details>
<summary>Preserved research history and technical checkpoints</summary>

The entries below retain their original wording, dates and assumptions.
The core argument and current work order above give the current
assessment; older next-step statements record the work at those times.

### Previous fixed-clock precision checkpoint

The [matched precision law](docs/FAMILIAR_SWITCH_QUADRATIC_PRECISION.md)
now explains the fast-hidden regime at fixed coupling and field. With
hidden/visible attempt ratio $r$, the smallest attainable error among
reversible models with at most three states under the stated Gibbs and
readout requirements is of order $r^{-2}$. A two-state equilibrium model absorbs the first-order
slowing into corrected rates; the extra-state obstruction occurs at
second order. The law holds for every finite clocked pulse word at fixed
positive dwell times. Allowing the control timescale itself to shrink
remains a different question. This is an analytic regime statement.


## Current milestone: a narrow precision window and necessary acquisition cost — 28 September 2026

**Mathematical review and full local verification passed.**
The [new information analysis](docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md)
constructs a positive ordinary reversible three-state continuous-time
rival for the same seven settings $L,L^2,H,LH,HL,L^2H,HL^2$.
Its fixed reused rates, unknown Gibbs tilt $u=0.768614727605$ and
word-specific preparations with balanced initial signs are admissible
under the existing arbitrary-preparation null.

The best ordinary at-most-three-state maximum pair-law TV error obeys
**$3/40006\le E_3<86/10^6$**, where $3/40006$ is approximately
**74.98875 ppm**. The upper/lower ratio is below **1.15**. The attained
state counts remain **three general versus four ordinary reversible
states through $3/40006$**; at **86 ppm both counts are three**.
The lower endpoint follows from the existing 150 ppm conditional-return
certificate. The new fixed rival supplies the upper; no closest-rival
optimality is asserted.

For the same robust statistical contract, every test with both errors
at most 5% needs a deterministic cap of at least **109,880,323 complete
pairs**. Together with the existing **1.176-billion-pair** sufficient
design, this places the optimal fixed budget within a factor **11**.
Adaptive word choice uses completed past trials, before current
preparation and the initial sign; stopping is between complete pairs.
A separate bound for expected stopping requires more than
**87,661,100.934495 pairs under the ideal target**. Ideal independent
target/rival trials form a hard subclass of the broader conditional
serial contract, including its target-only 5 ppm execution allowance
and 1 ppm registration allowance per endpoint. The lower does not
assume that arbitrary serial errors have independent-trial information.

The high acquisition cost is partly intrinsic to this fixed target,
menu and observation contract. The next priority is a physical design
principle from analytic factorization across the same familiar heat-bath
family: vary coupling, field and dwell times to understand signal versus
duration, and seek a structural improvement or a family-wide obstruction.
An isolated retuned example or further constant tuning is secondary.
Device feasibility remains open; manuscript drafting remains deferred.

[Proof and scope](docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md) · [Exact verifier](scripts/verify_familiar_switch_preparation_free_information.py) · [Certificate](reports/familiar_switch_preparation_free_information.json) · [Source comparison](docs/FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION_SOURCE_AUDIT.md) · [Verification](docs/VERIFICATION.md)

**Preserved preceding checkpoints follow.** Their original prose and
claim scopes remain intact; this precision-and-acquisition update supplies
the current assessment and next step.


## Current milestone: seven settings without a rival preparation promise — 28 September 2026

**Mathematical review and full local verification passed.**
The [new seven-setting theorem](docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md)
removes the rival equilibrium-preparation requirement while retaining an
unknown Gibbs tilt. It uses
$L,L^2,H,LH,HL,L^2H,HL^2$ at the same two-switch target. Rivals may
prepare arbitrary hidden-state distributions for each word and each
trial history. Their field kernels, deterministic sign readout and
shared Gibbs interface remain fixed; zero-equilibrium-weight transient
states count toward the state budget.

The attained population comparison is **three general states versus
four ordinary reversible states through 70 ppm per-word pair-law TV**.
The underlying conditional-return exclusion tolerates 150 ppm error.
The initial true sign is defined after the initial instrument, at the
start of active evolution; the final true sign is taken at its end.
Removing the rival preparation promise does not remove these observation
and control requirements.

The finite test allows **168 million attempted pairs per setting**, or
**1.176 billion total**, retaining 80 million observations of each
initial sign for each setting. Incomplete quotas do not certify
rejection. Under the stated conditional registration bound of 1 ppm
per endpoint, false rejection is below $0.040389$ without a null
preparation-closeness promise. Target miss is below $0.045261$ when,
conditional on the past, the target's true-boundary pair law is within
5 ppm TV of its nominal reference for each setting. These sampling and
registration allowances are separate from the 70 ppm population radius.

The earlier 50-million-pair design remains a different experiment with a
stronger preparation contract. The new count is sufficient, without a
cost-optimality or device-feasibility claim. The next priority is to
determine whether its high acquisition cost is intrinsic: construct
admissible nearby rivals and a seven-setting information lower bound
before further tuning constants. Manuscript drafting remains deferred.

[Proof and scope](docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md) · [Population certificate](reports/familiar_switch_preparation_free_unknown_tilt.json) · [Sampling certificate](reports/familiar_switch_preparation_free_unknown_sampling.json) · [Source comparison](docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md) · [Verification](docs/VERIFICATION.md)

**Preserved preceding checkpoints follow.** Their original prose and
claim scopes remain intact; the seven-setting update above supplies the
current assessment and next step.


## Current serial-acquisition milestone — 28 September 2026

**Mathematical review and full local verification passed.**
The [serial acquisition analysis](docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION.md)
retains the **50 million paired trials** and the same unknown-tilt test,
while allowing dependence between trials. It requires every recorded
pair law, conditional on the complete past history, to lie within
**1 ppm in total variation** of one fixed ideal reference family across
all five settings and all trials. A marginal or average error bound is
insufficient. Under this contract, false rejection is below $0.047185$
for the ordinary at-most-three-state null with $m\in(-1,1)$, and the
nominal-target miss probability is below $0.024949$.

For the nominal target with attempt scale $\Gamma$, a reset of
$24/\Gamma$ leaves full-state TV error at most
$\tfrac{\sqrt5}{2}e^{-16}<0.25$ ppm. A serial cycle through
$L,L^2,H,H^2,HL$, repeated 10 million times, accounts for

$$
T_{\mathrm{serial}}=
\frac{1.28\times10^9}{\Gamma}
+50\times10^6(T_{\mathrm{initial}}+T_{\mathrm{final}})
+30\times10^6(t_{\uparrow}+t_{\downarrow})
+T_{\mathrm{other,nonoverlap}}.
$$

This includes 50 million resets, 80 million active ticks, 100 million
endpoint windows and 60 million field edges. It is target-only schedule
accounting. Arbitrarily slow rivals still need a separate preparation
promise; the target reset estimate cannot establish their conditional-law
contract. The retained-state comparison concerns the predictive model
under the stated interface, not the full apparatus.

The [physical source audit](docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION_SOURCE_AUDIT.md)
anchors the components in mesoscopic single-electron stochastic
thermodynamics. Published components do not yet establish the combined
precision, instrument and control specification. The next scientific
priority is to seek an unknown-tilt witness that removes the rival
equilibrium-preparation promise, then certify its error budget. Trial counts alone do not demonstrate a device; manuscript
drafting remains deferred.

[Serial proof and scope](docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION.md) · [Serial certificate](reports/familiar_switch_serial_acquisition.json) · [Physical sources](docs/FAMILIAR_SWITCH_SERIAL_ACQUISITION_SOURCE_AUDIT.md) · [Verification](docs/VERIFICATION.md)

**Preserved preceding checkpoints follow.** Their original prose and
claim scopes remain intact; the serial-acquisition assessment above
supplies the current status and next step.


## Current acquisition milestone — 28 September 2026

**Mathematical review and full local repository verification passed.** The
[new acquisition analysis](docs/FAMILIAR_SWITCH_PROFILED_ACQUISITION.md)
reduces the sufficient ideal-data design to **50 million paired trials**:
10 million for each of $L,L^2,H,H^2,HL$. A fixed empirical gate and one
scalar degree-six polynomial test the whole ordinary at-most-three-state
null with unknown Gibbs tilt $m\in(-1,1)$. The certificate bounds
false rejection by $0.044297$ and nominal-target miss by $0.023080$.
This is twelve times fewer trials than the earlier unknown-tilt design.

A closer ordinary reversible three-state CTMC gives a stronger necessary
count of **2,849,458 paired trials**. The same ideal experiment therefore
has the deterministic-budget bracket

$$
2{,}849{,}458\le N_{\mathrm{optimal}}\le50{,}000{,}000.
$$

The sufficient count is within a factor of 18 of the optimal deterministic
budget. The lower
allows adaptive choice among the five settings using completed past
trials, with the next setting chosen before its initial sign is observed.
This is a fixed-target finite-budget comparison, not an asymptotic
optimality result.

Independent fresh resets, the full initial-instrument contract and the
shared Gibbs/reused-kernel interface remain required. The prior noisy
readout designs retain their separate scopes. The earlier 50 ppm and
common 1% population results do not extend to arbitrary different fitted
tilts through this sampling statement. No device feasibility follows.

The next priority is to assess full acquisition time and the preparation,
readout and control requirements needed for a useful implementation;
further minor statistical tuning is secondary.

[Acquisition proof and scope](docs/FAMILIAR_SWITCH_PROFILED_ACQUISITION.md) · [Score certificate](reports/familiar_switch_profiled_score.json) · [Information certificate](reports/familiar_switch_profiled_information.json) · [Verification](docs/VERIFICATION.md)

**Preserved preceding checkpoints follow.** Their original content is
retained; the new acquisition status supersedes their current priorities
and ideal sufficient/necessary counts under the scopes stated above.


## Current measurement milestone — 28 September 2026

The [five-setting measurement analysis](docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md)
adds finite-sample tests to the two-switch theorem below. Each trial
records one initial/final sign pair for $L,L^2,H,H^2$ or $HL$.

| Measurement contract for the numerical $m=7/9$ score | Sufficient paired trials |
| --- | ---: |
| Ideal observations | 100 million |
| Per-word recorded-law TV allowance of 10 ppm on each side | 125 million |
| Known independent 1% binary-symmetric errors at both endpoints, plus the same residual allowance | 150 million |

Both false-rejection and target-miss probabilities are below $0.05$.
Each allowance is relative to one fixed nominal model across all words,
separately for the target and rival; the known detector belongs to the
reference law. A separate unknown-$m$ profile test uses 600 million ideal
trials, with nominal-target power and null validity for $-1<m<1$.
The numerical $m=7/9$ score does not itself cover an unknown field tilt.
A fixed-budget KL comparison gives a necessary total of at least
136,981 trials for the ideal experiment. The substantial gap between
necessary and sufficient counts remains unresolved.

The guarantees require independent fresh resets and the complete
preparation, initial-instrument, detector and repeated-control contract.
Target mixing does not certify a finite reset time for arbitrary slow
rivals. A separate population certificate gives exactly three general
versus four ordinary reversible states through 50 ppm throughout a
common 1% parameter box. It does not automatically transfer the nominal
score's power to the whole box.

The frozen theorem is unchanged. Sampling uncertainty, physical error
allowances and its 50 ppm population tolerance are different quantities.
The next priority is to narrow the acquisition-cost gap and assess the
instrument assumptions needed for a useful test. Device
feasibility and publication significance remain open; manuscript drafting
stays deferred.

[Measurement proof and scope](docs/FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md) · [Score certificate](reports/familiar_switch_frozen_score.json) · [Sampling certificate](reports/familiar_switch_frozen_sampling.json) · [Information certificate](reports/familiar_switch_frozen_information.json) · [Robustness certificate](reports/familiar_switch_frozen_robustness.json) · [Verification](docs/VERIFICATION.md)

## Preserved theorem checkpoint

The following theorem summary and preceding checkpoints retain their
original content. Their next-step assessments are historical and are
superseded by the measurement status above.


**Perfect fixed-field calibration can still require another state after
one switch.** Two coupled heat-bath switches give a small example: one
reversible three-state predictor matches every initial/final sign law at
either constant field, for every duration. It uses one common preparation,
one binary readout and the prescribed Gibbs force. Yet every such
three-state predictor must make an error when the field changes.

The [calibration-and-switching theorem](docs/FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md)
uses coupling $\tanh J=1/3$, high field $H=3J$ and equal attempt rates.
Only the first switch is controlled and observed. Starting from zero-field
equilibrium, record its initial and final signs. Write $L$ for one time
unit at zero field and $H$ for one time unit at the high field; $HL$
applies the high field first.

| Endpoint prediction task | General Markov states | Ordinary reversible states |
| --- | ---: | ---: |
| Every duration at both constant fields, exactly | $3$ | $3$ |
| Five settings $L,L^2,H,H^2,HL$, through TV error $1/20000$ | $3$ | $4$ |
| Every finite protocol at the two fields, exactly | $3$ | $4$ |

**Four exact calibration laws force a sharp switched error.** Matching
$L,L^2,H,H^2$ exactly makes the smallest possible three-state reversible
error on $HL$ equal to $0.002451868563\ldots$, about **$0.245\%$** in
total variation. An explicit model with rational rates attains this
minimum and also matches every constant-field duration. Its construction
extends to all nonnegative constant fields. The obstruction comes from
the field-dependent normalization of the one hidden contrast available
in three states.

**Imperfect calibration has a separate guarantee.** If every one of the
five pair laws may have TV error at most $1/20000=50$ ppm, the exact
minimum counts remain three general states versus four ordinary
reversible states. The lower permits arbitrary reversible stochastic
tick kernels, imbalanced initial signs and unused zero-mass states,
without a rate cap. One common preparation, deterministic readout and the
shared Gibbs tilt remain required. The $0.245\%$ conditional minimum is
not a uniform tolerance for errors in all five settings.

An existing general three-state predictor keeps the same hidden coordinate
across fields and matches every finite protocol. It obeys the prescribed
Gibbs stationary laws while allowing stationary circulation. The physical
four-state process supplies the reversible upper.

Constant-field equivalence without switching equivalence is known in
control theory. The [source comparison](docs/FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md#6-established-mechanism-and-additional-content)
attributes that mechanism and coarse-grained response theory. The additional
result is the attained minimum over the calibrated three-state reversible
class and its finite-error counterpart under the stated physical interface.
These endpoint theorems do not establish full-path equivalence, hardware
savings or a dissipation benefit.

The next priority is to quantify the usefulness, acquisition cost and
physical robustness of this five-setting test. Device feasibility and
publication significance remain open. Manuscript drafting remains deferred.

[Proof and scope](docs/FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md) · [Construction certificate](reports/familiar_switch_frozen_equivalence.json) · [Finite-error certificate](reports/familiar_switch_frozen_bound.json) · [Verification](docs/VERIFICATION.md) · [Current work](work_orders/CURRENT.md)

## Complementary chain results — preceding checkpoint

The chain results below retain their stated scopes. Their earlier
next-step assessment is superseded by the five-setting priority above.

The [two-field chain theorem](docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md) shows that
**requiring a predictive model to obey equilibrium detailed balance can
increase the number of states it needs under control**.

A familiar heat-bath Ising chain has $n$ interacting switches. We control
and observe only the first one, recording its initial and final signs.
For every $n\ge3$, at one fixed coupling $0<\tanh J\le1/64$ and
nonnegative field tilts $0\le\tanh h\le1/2$:

| Required endpoint-pair data | General Markov states | Ordinary reversible states |
| --- | ---: | ---: |
| Passive pairs | $n+1$ | $n+1$ |
| Two-field controlled menu, exactly | $n+1$ | $2n$ |
| All controlled endpoint pairs, exactly | $n+1$ | $2n$ |

The [explicit positive model](docs/FAMILIAR_CHAIN_POSITIVE_REALIZATION.md)
works under every finite nonnegative-field protocol, with exit rates at
most $13/12$ independently of chain length. The
[reversible lower bound](docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md) needs only
two field values and $2n(n-1)$ endpoint-pair settings, each with at
most two field segments. The new
[reversible realization](docs/FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md)
attains $2n$ at every length, with strictly positive rates and total exit
rates at most $33/32$. The coupling interval is independent of length.
The older [four-versus-six example](docs/FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
remains valid at the stronger three-switch coupling $t=1/3$.

All experiments reuse one preparation and one model. The reversible class
retains the physical force convention: its stationary laws are Gibbs tilts
in the measured sign. The general construction obeys that same convention
but permits stationary circulation. The lower bound has an explicit
positive error radius for each fixed instance, without a rival rate cap
or minimum stationary weight.

**Exact state cost and finite-accuracy cost differ.** The new
[truncation bound](docs/FAMILIAR_CHAIN_FINITE_ACCURACY.md) shows that
retaining only the first $\ell$ switches changes any endpoint-pair law by
at most $t^{2\ell}/(1-t^4)$ in total variation, uniformly over all protocols
and horizons. In the new weak-coupling interval, four reversible states
already approximate every length within $6\times10^{-8}$. Any error
threshold certifying the exact $2n$ count must decrease at least
exponentially with length. The exact separation is a constraint on lossless
equilibrium reduction, not an extensive fixed-precision advantage.

**The three-switch minimum now changes at certified precisions.** At
$t=1/3$, field tilts $0,1/2$ and a unit clock, twelve endpoint-pair settings
suffice. Each has at most four ticks and two field segments. Opposite pulse
orders expose the rank within each visible-sign sector without an
intermediate observation. For maximum pair-law total-variation error
$\delta$:

| Allowed error | General Markov states | Ordinary reversible states |
| --- | ---: | ---: |
| $0\le\delta\le2\times10^{-6}$ | Exactly $4$ | Exactly $6$ |
| $3.6\times10^{-6}\le\delta\le3.8\times10^{-6}$ | Exactly $4$ | Exactly $5$ |
| $\delta=2\times10^{-5}$ | At most $4$ | Exactly $4$ |

These counts hold for both the twelve-setting menu and the preceding
sixteen-setting menu. The intervals between the rows and exact transition
locations remain undetermined. The last row asserts no general four-state
lower bound at that larger tolerance.

The best menu error $E_{\le5}$ with at most five ordinary reversible states
now satisfies

$$
2\times10^{-6}\le E_{\le5}<3.6\times10^{-6}.
$$

The [explicit five-state model](docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md#4-two-explicit-reversible-approximations)
is therefore within a factor of $1.8$ of the best possible error. The lower
allows arbitrary reversible stochastic tick kernels, initial sign
imbalance and zero masses; the upper is a continuous-time Markov model.
Exact rational certificates support both bounds. Their parts-per-million
scale leaves practical acquisition cost and physical usefulness open.

These results complement the two-switch calibration theorem by quantifying
precision dependence for a longer chain.

The [precision-dependent result and scope](docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md)
provides the derivation and exact certificates. Its [source comparison](docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md#5-established-tools-contribution-and-remaining-significance), together with the
[construction audit](docs/FAMILIAR_CHAIN_SHARPNESS_SOURCE_AUDIT.md), separates
the established kinetic model and mathematical tools from the combined
state-count result. These are ideal prediction theorems, without a hardware,
heat-cost, or full-path claim. Manuscript drafting remains deferred.

[Rank certificate](reports/familiar_chain_cross_rank.json) · [Small-model certificates](reports/familiar_chain_small_models.json) · [Verification](docs/VERIFICATION.md) · [Current work](work_orders/CURRENT.md)

## Preserved two-switch boundaries

The preceding [published coupled-dot model](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md) gives a precise example of **how control range and temporal observations change the minimum number of predictive Markov states**. Its four configurations have three-dimensional closed mean dynamics, but a positive three-state model cannot serve every prediction task.

| Required ideal data | General Markov states | Ordinary reversible states |
| --- | ---: | ---: |
| Passive endpoint pairs at two lags; also all passive pairs | 3 | 3 |
| Four controlled pairs $0,H,0H,H0$ | 3 | 4 |
| One passive three-time law | 4 | 4 |
| Signed-control endpoint pairs | 3 or 4, with an exact threshold | 4 |

The [passive/triple theorem](docs/FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md) supplies an explicit reversible three-state model for passive pairs. Adding one ideal intermediate observation forces four states even without detailed balance: a singleton middle-sign sector would make past and future independent, while the target retains dependence in both sectors. This gives a positive TV margin and an exact triple error when all pair marginals must remain correct.

The [signed-control theorem](docs/FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md) supplies the other boundary. Write $t=\tanh J$, $u=\tanh H$, and let $r=\Gamma_Z/\Gamma_S>0$ be the hidden/visible attempt-rate ratio. One positive three-state model matches every endpoint pair under all protocols in $[-H,H]$ **if and only if**

$$
 (r+2)t^2u^2+(1+t^2)u\le r.
$$

Otherwise the general minimum is four. The linear mean dimension stays three across this boundary; nonnegative rates under the enlarged control range cause the additional state requirement. At the previous equal-rate operating point, allowing both field signs removes the three-state advantage. Faster hidden relaxation can restore it.

The same boundary is determined by **23 endpoint-pair experiments**, each at most five ticks long, from one common arbitrary initial preparation. The data force equilibrium preparation and the stationary Gibbs tilt for any exact three-state fit; those laws need not be assumed separately. Positive finite-menu TV margins exist, but their numerical sizes are not yet calculated. This reuse condition differs from the [four-word theorem](docs/FAMILIAR_SWITCH_MINIMAL_THEOREM.md), which permits arbitrary per-word preparation while imposing the common force interface. The passive/triple rows likewise retain their own kernel and observation conditions.

The [scope assessment](docs/FAMILIAR_SWITCH_CONTROL_SCOPE.md) explains which smaller model is valid for which task. The [primary-source comparison](docs/FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md) attributes the established realization, cone and conditional-independence tools. The candidate contribution is this explicit control-range criterion and complete state-count comparison in a familiar physical model. The open-chain theorem above supplies the broader kinetic-family extension. These two-switch boundaries retain their own preparation and observation assumptions. Detector engineering and manuscript drafting remain deferred.

These are ideal state-process theorems, with no claim of hardware-bit savings, predictor heat cost or complete-path equivalence. The shared physical model, control assumptions and limits are stated in the [community model contract](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md).

[Exact certificate](reports/switch_control_scope.json) · [Verification](docs/VERIFICATION.md) · [Current work](work_orders/CURRENT.md)

## Preserved finite-accuracy and detector extensions

The following results retain their original operating points and observation contracts. Numerical margins and acquisition counts below are separate from the generic ideal-model theorem above.

**The current four-experiment test removes the rival preparation promise.** Add the single pulses $0$ and $H$ to the opposite orders $0H,H0$. Any binary model with at most three states has a visible sector containing only one hidden state. Conditioning on its initial sign therefore fixes its starting state, however it was prepared. Detailed balance and the common Gibbs tilt imply

$$
 R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}+2su\,r_{0,s}r_{H,s}=0
$$

for at least one sign $s$, where $r_{w,s}$ is the conditional return probability and $u=3/5$. The target violates both identities throughout the independent one-percent kinetic box: $R_->.009$ and $R_+<-.009$. Its existing three-state predictor matches **all four complete ideal pair laws exactly**. Thus the [four-word realization theorem](docs/FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md) gives **three general states versus four ordinary-reversible states for pair-table TV error up to .001**, even with different arbitrary preparations for every rival word.

The [finite test](docs/FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) uses **nine million trials**, cycling through the four words and retaining the first million records of each initial sign in each word. Reject only if both residuals cross their signed $.004$ thresholds; incomplete groups cause nonrejection. Ideal readout gives false rejection below .5% and target miss probability below .4%. Rival preparations may depend on the entire history. Target power still needs its stated conditional execution bound; the fixed kernels, exact stationary Gibbs tilt and sign-preserving initial instrument remain premises.

The [noisy-readout extension](docs/FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md) uses seven protected readings at **each** endpoint, with two disagreement gates. It retains size below 1.5% and target miss probability below 1.4%, at **126 million raw readings**. Errors may correlate with same-use hidden kicks, but their fixed per-use probabilities must hold conditional on every preceding state and history. Sector protection is exact. The target initial block preserves equilibrium; the null needs no such stationarity. Calibration does not certify these structural conditions. The state-count theorem concerns the four ideal pair laws, not the full fourteen-reading transcript, and the old approximate-null allowance is not transferred to this new test. [Certificate](reports/switch_preparation_free.json) · [Source comparison](docs/FAMILIAR_SWITCH_PREPARATION_FREE_SOURCE_AUDIT.md) · [Internal review](docs/FAMILIAR_SWITCH_PREPARATION_FREE_INTERNAL_REVIEW.md).

**A calibrated integrating detector can tolerate imperfect protection.** The new [endpoint-registration theorem](docs/FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md) takes the initial true sign **after** the initial acquisition and the final true sign **before** the final acquisition. Initial measurement disturbance then belongs to the rival's arbitrary preparation. A uniform conditional endpoint-misclassification bound of $5\times10^{-6}$ suffices, even with unequal, history-dependent error rates and errors correlated with hidden kicks. Exact sector protection, a fixed symmetric bit-flip channel and seven repeated readings are unnecessary for this alternative. The accuracy bound is a calibration/model premise; the earlier unknown-detector disagreement scheme does not establish it.

One integrating window at each endpoint gives **18 million windows and binary decisions** in the same nine-million-trial experiment. A signal margin $g$, continuous-martingale noise with quadratic variation at most $vT$, and whole-acquisition sign-change probability at most $\Lambda$ imply endpoint error at most $e^{-g^2T/(2v)}+\Lambda$. The sufficient choice $T=32v/g^2$, $\Lambda\le4\times10^{-6}$ meets the required accuracy. Switching and settling belong in that leakage budget. This is a demanding physical specification, not a demonstrated device performance or a count of analog samples. The [eight-source audit](docs/FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_SOURCE_AUDIT.md) separates established detector/control components from the unverified combined specification.

The [relative-force theorem](docs/FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md) also permits a factor **1.001** spread in the residual stationary reweighting beyond the nominal Gibbs tilt, without a minimum stationary mass. The enlarged null has false rejection below **4%** and target miss below **1.4%** with the same trial cap. The four ideal boundary-pair state minima remain **three versus four through TV error .0009**. A counterexample shows why a small unweighted stationary-law TV error cannot replace this relative force condition when rivals may start in rare states. Target power requires its post-acquisition marginal preparation/execution budget; the full analog transcript has no claimed three-state realization. [Exact certificate](reports/switch_endpoint_registration.json) · [Internal review](docs/FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_INTERNAL_REVIEW.md).

The earlier two-word experiment uses **one equilibrium preparation and two opposite pulse orders**, with an initial and final binary readout:

| Protocol | Preparation | Active fields | Recorded data |
|---|---|---|---|
| $A$ | Low-field equilibrium | $0,H$ | Initial bit $I$, final bit $Y$ |
| $B$ | Low-field equilibrium | $H,0$ | Initial bit $J$, final bit $Z$ |

The mechanism is a conditional covariance. A hidden conformation changes the response to both pulses, even after fixing the visible conformation. Detailed balance makes that covariance measurable by reversing pulse order. It is nonzero in both visible sectors, so each sector needs at least two states. A stationary predictor with circulation reproduces both initial/final joint laws with three states.

The [direct snapshot theorem](docs/FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) uses four moments $m=\mathbb EY$, $c=\mathbb E(IY)$, $\ell=\mathbb EZ$, $d=\mathbb E(JZ)$. Every ordinary model with at most three states satisfies one of the two identities

$$
u c-u(1+\sigma m)d+\sigma(u-m)\ell=0,\qquad \sigma=\pm1,
$$

where $u=\tanh H$. The coupled pair violates both. This necessity has no rival rate cap and includes arbitrary reversible stochastic tick kernels. One fixed model, preparation, instrument and readout must explain both protocols. Shared Gibbs stationary laws and the specified measurement model are substantive assumptions.

**The detector contrasts need not be calibrated.** Let $(M,C,L,D)$ be the four recorded moments, after independent symmetric bit flips. The [unknown-readout witness](docs/FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) uses

$$
 R=u(C-D)+uMD-(u-M)L>0,
 \qquad 0<M<u,\quad L,D>0,\quad C<D.
$$

These conditions exclude every ordinary model with at most three states even if each rival chooses its own initial and final error probabilities anywhere in $[0,1/2]$. Its detector must still be memoryless, symmetric, independent across the two bits, and fixed across protocols.

**Repeated initial readout can tolerate errors correlated with hidden kicks.** The [seven-readout theorem](docs/FAMILIAR_SWITCH_REPEATED_READOUT.md) replaces each initial bit by the majority of seven protected readings. Each reading must preserve the visible sector and, after discarding its outcome, preserve conditional equilibrium. Its error has one fixed probability conditional on the entire pre-readout state and history; it may be correlated with the hidden update caused by that same reading. At error probability at most 2%, the majority-label/postmeasurement-state joint law is within **0.0000053356544** of ideal initial readout. Hidden kicks need not be small or independent of their electronic errors.

A disagreement gate on the first two readings, using the same five million trials, covers ordinary rivals whose initial error probability is unknown anywhere in $[0,1/2]$. With target errors at most 1%, the existing serial score retains false rejection below 5% and power above 95%, under its preparation and physical promises. The cost becomes **40 million raw binary readings**: seven initial and one final per trial. The two pulse orders, score and threshold remain unchanged. The final detector still obeys the independent symmetric-channel assumption. The gate does not certify fresh errors, sector protection or equilibrium preservation; a shared error across all seven readings can evade it. No three-state realization of the full eight-reading transcript is asserted. [Proof and scope](docs/FAMILIAR_SWITCH_REPEATED_READOUT.md) · [Source comparison](docs/FAMILIAR_SWITCH_REPEATED_READOUT_SOURCE_AUDIT.md).

**The memory advantage survives independent one-percent rate changes.** At $J=\log3$, $H=\log2$ and equal dwell times $5/4$, the [direct kinetic theorem](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md) permits an independent symmetric prefactor in $[.99,1.01]$ on each of the four transition edges at each field. These eight factors preserve Gibbs detailed balance but can break heat-bath moment closure. The same two words retain state minima **three versus four on $[0.00008,0.0009]$**, including the physical allowances below. A [local three-state construction](docs/FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md) fits the two joint snapshot laws exactly at nominal fields and times, using genuine continuous-time Markov generators. It fits those two laws, without asserting agreement for other control words or complete trajectories.

**The five-million-trial test can run serially on one device.** The [conditional sampling theorem](docs/FAMILIAR_SWITCH_SERIAL_SAMPLING.md) retains the [kinetic score test](docs/FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md), its gates and threshold .0021, with 2.5 million trials per protocol and ten million binary readouts. False rejection remains below 5% and power above 95% under deterministic alternation of the two protocols. Trials may be dependent, provided that after every history their conditional recorded joint laws stay within $0.000079$ for the target, or $0.00022$ for the null, of **one fixed stationary reference pair**. The null budget includes observed-joint-TV prediction allowance $0.0002$, exceeding the finitely prepared general-three-state conditional-pair error bound $0.00009$ below. An unconditional average error does not replace this conditional promise; preparation, the initial joint instrument, fixed plateau generators and the stated electronic channels remain substantive.

The [finite-reset theorem](docs/FAMILIAR_SWITCH_FINITE_RESET.md) supplies the target preparation step: an actual low-field wait of **63 attempt-time units** gives hidden-state TV error below $10^{-5}$ from any preceding state, uniformly over the one-percent kinetic family and $|h_0|\le10^{-5}$. Five million resets plus the nominal active pulses cost **327.5 million attempt-time units**, 26.2 times the active-only exposure. Readout, switching and other implementation durations are additional. This target bound does not reset every arbitrarily slow ordinary rival in 63 units. The serial statistical null requires its own conditional preparation guarantee; the broader stationary state-count lower remains unchanged and has no rival rate cap.

The constructive three-state predictor can use **the same 63-unit reset**, giving conditional two-record table error below $.00009$ relative to the actual target. It receives no ideal fresh-preparation advantage. This is a per-trial table guarantee, not a full-record TV bound or a new serial state-count minimum.

The sufficient relative rate allowance increases **500-fold, from 20 ppm to 1%**, with the same total trial count and null approximation allowance. This is a mathematical tolerance improvement, not an optimized threshold or measured device capability. The [earlier integrated-error theorem](docs/FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) and [its score test](docs/FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md) remain valid at their stated scopes. At exact preparation, fields, timing and initial instrument, the new kinetic family has exact three-state prediction and ordinary-three-state gap $>0.001$, giving state minima on $[0,0.001]$.

**The heat-bath reference has a sharper guarantee.** Keep $J=\log3$, use $H=\log2$, and let both dwell times be $5/4$. The [weaker-field robustness theorem](docs/FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) gives a nominal recorded-table gap **greater than 0.00115** for target bit-error probabilities at most 1%. With preparation, field, timing and initial-disturbance allowances $10^{-5}$, stationary bias and tilt uncertainty $10^{-4}$, and stationary-law TV defect $10^{-5}$, the gap remains **greater than 0.001**. Three general states suffice within **0.00002**. The state minima are therefore three and four for $0.00002\le\delta_{\rm obs}\le0.001$, five times the earlier certified upper end of this interval. The two-plateau active duration falls from three to $5/2$ attempt-time units.

The [new integer-score test](docs/FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) uses only the same initial and final bits. Both allocations have false rejection below 5% and target power above 95% for fresh independent trials, with the physical allowances above:

| Unknown-detector null | Trials per protocol | Total paired trials | Binary readouts |
|---|---:|---:|---:|
| Admissible ordinary model, at most three states | 1,000,000 | **2,000,000** | 4,000,000 |
| Same model class, observed-joint-TV approximation allowance $10^{-4}$ | 1,250,000 | **2,500,000** | 5,000,000 |

The approximation allowance exceeds the general three-state constructive error. No extra field, preparation, protocol or detector calibration is added. The weaker-field experiment has a smaller ideal witness but loses less signal to the unknown symmetric detector errors; the recorded witness is larger. This is a certified operating point, with no claim of optimal fields, sample complexity or experimental feasibility.

A separate tolerance result allows preparation, field, timing and initial-disturbance errors $5\times10^{-5}$ while preserving state minima three and four on $[10^{-4},6\times10^{-4}]$. The trial budgets above remain proved only for the $10^{-5}$ allowances.

**Changing the physical design beats every test confined to the old design.** At $J=H=\log3$ and dwell $3/2$, the [information bound](docs/FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) requires more than $810000\log19\approx2.385$ million trials in target expectation, even with adaptive sampling, for the nominal target with one-percent errors. The new design needs only two million and covers that detector-error value. The physical and detector classes have the same form at their respective fields; the old lower bound is not a lower bound for the new experiment. Preparation overhead and calibration acquisition are not priced.

**The earlier operating point remains documented.** At $J=H=\log3$ and dwell $3/2$, the unknown-detector nominal and robust gaps remain greater than 0.000375 and 0.0002. Its [fixed-score test](docs/FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md) needs 32 million paired trials, or 90 million with the additional approximation allowance $10^{-4}$. The new design reduces these sufficient budgets by factors of 16 and 36, respectively, while changing the high field and dwell time. The original 508-million confidence-box test also remains valid at its historical scope.

**Detector calibration has a provable statistical value at the earlier operating point.** At $J=H=\log3$ and dwell $3/2$, for the nominal target with one-percent bit errors, the [information lower bound](docs/FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) requires at least **2,384,996 paired trials** for any fixed-budget test against the unknown-detector class, even though the earlier calibrated test below needs only 1.2 million. Adaptive protocol choices and stopping still require $\mathbb E_*N>810000\log19$. Thus the specified calibration promise reduces the necessary observation budget by more than a factor of 1.98 in this comparison. The cost of obtaining that calibration is separate and unpriced. The smaller calibrated-detector counts do not apply to the unknown-contrast null.

**The earlier calibrated gap is almost pinned down.** At $J=H=\log3$ and tick $3/2$, the best ordinary-three-state maximum joint-law TV error with ideal readout lies strictly between **0.00184 and 0.00185**, a bracket of ratio $185/184$. The lower covers the entire stated rival class; the upper is one certified feasible ordinary model. Three general stationary states are exact for these two joint laws. The longest active experiment lasts three attempt-time units. This does not assert arbitrary multitime path-law equality.

**Preparation, controls and measurement are included.** With simultaneous preparation TV, fixed field/tick errors and initial-readout disturbance budgets $10^{-5}$, stationary low-field bias and relative tilt uncertainty $10^{-4}$, and high-stationary-law discrepancy $10^{-5}$, the witness tolerates independent symmetric readout error probabilities **$0.01\pm10^{-5}$** at both observations. The recorded joint-law gap remains above **0.0015**; the state minima are three versus four for $4\times10^{-5}\le\delta\le0.0015$. Known detector noise, uncertainty in its calibration, and hidden-state disturbance are separate quantities. This 1% detector example is a mathematical operating point, not a device specification.

The earlier [fixed-score tests](docs/FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) improve the measurement budget for their specified detector classes. These counts do not transfer to the detector-unknown result. Each design has false rejection below 5% and target power above 95%, under its stated class:

| Snapshot design | Fresh paired trials | Binary readouts |
|---|---:|---:|
| Exact preparation, controls and readout | 900,000 | 1,800,000 |
| Physical nuisance; ideal readout | 1,000,000 | 2,000,000 |
| Physical nuisance, disturbance and calibrated 1% readout noise | 1,200,000 | 2,400,000 |
| Same noisy class; exclude ordinary approximation within observed TV $10^{-4}$ | 1,500,000 | 3,000,000 |

A separate ideal information lower requires at least **79,500 paired trials** for fixed-budget testing. The sufficient and necessary budgets are not matched. A target-specific low-field wait of 62 attempt-time units supports the preparation tolerance; it does not prepare every arbitrarily slow rival or establish fresh-trial independence. Visible balance alone cannot certify full hidden-state preparation or measurement disturbance.

The earlier **two-preparation, four-endpoint experiment** remains useful when initial observation is costly. Its [new score test](docs/FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md) needs **1,450,000**, **1,670,000**, or **1,890,000** single-readout trials for nominal, calibrated and calibrated finite-accuracy testing. These replace earlier sufficient confidence-box counts of 12,531,296, 15,859,920 and 18,045,064 on those same classes. Its [deterministic theorem](docs/FAMILIAR_SWITCH_PREPARATION_WITNESS.md) and [preparation costs](docs/FAMILIAR_SWITCH_PREPARATION_COST.md) remain unchanged. Preparation types, readouts and calibration premises differ between the designs; neither dominates every resource.

The [exact snapshot certificate](reports/switch_snapshot_design.json), [endpoint certificate](reports/switch_endpoint_score.json), [saved-model replay](reports/switch_snapshot_screen.json), [source comparison](docs/FAMILIAR_SWITCH_SCORE_SOURCE_AUDIT.md), and [internal review](docs/FAMILIAR_SWITCH_SNAPSHOT_INTERNAL_REVIEW.md) separate analytic proof, essential rational bounds and statistical assumptions. No large simulation is needed.

**A conditional charge-state realization removes equal-rate tuning.** Two capacitively coupled nondegenerate dots, each exchanging electrons with an equilibrium reservoir, map exactly to the switches under the specified sequential Fermi-tunneling model. The [charge derivation](docs/FAMILIAR_SWITCH_CHARGE_REALIZATION.md) gives an exact three-state predictor for hidden-to-observed tunneling-rate ratios at least $2/3$ over the selected field range. Ratios from $2/3$ to $2$ also retain a common exit cap of three observed-attempt units. The numerical gaps and sample counts above remain tied to equal attempts. The [primary-source audit](docs/FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) distinguishes demonstrated device components from the unestablished complete experimental specification.

**Preparation and the initial instrument remain real assumptions.** The [preparation boundary](docs/FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) constructs a biased ordinary model whose entire low-field binary record looks equilibrated, and a disturbance that preserves every endpoint distribution while corrupting the initial/final correlation. It also gives an optional response-specific preparation check for at-most-three-state rivals, adding three protocol types under exact balance. This does not remove the instrument premise or inherit a previous trial count.

The [new observable preparation bound](docs/FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) allows arbitrary hidden preparation and approximate stationary balance in that five-type design. It bounds the equilibrium bias of selected responses using low-pair means, relaxation and original-to-prefixed response differences, without a rival mixing-time estimate. It requires an exactly protected initial instrument and independent symmetric electronics. Each prefixed type must include a silent copy of the same instrument before its low wait; this is an extra physical operation.

The [randomized calibration analysis](docs/FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) handles history-dependent preparation by choosing the type only after preparation. Its conservative allocation of **60 billion trials** estimates eight corrected scalar functionals within $.001$ simultaneously with probability above 96%. This is a precision guarantee, not a full five-type rejection/power theorem or a lower bound on calibration cost. The added data have no established three-state predictor or inherited five-million-trial guarantee. The current four-word singleton test supplies a separate completed route; this historical five-type precision calculation remains unchanged.

The [readout calibration boundary](docs/FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) strengthens the instrument warning: a three-state classical model can pass arbitrary immediate repeat-readout checks, all low-only records and unchanged-endpoint checks, while a correlation between the electronic error and a hidden measurement kick changes the two snapshot tables. The example does not fit the selected target or show false rejection by its gated score. Physical independence of the electronic errors from the hidden update remains a separate requirement.

The [protected-readout theorem](docs/FAMILIAR_SWITCH_PROTECTED_READOUT.md) gives a simple sufficient instrument: hold the observed state fixed and preserve the equilibrium law inside each observed sector. Hidden motion may then be arbitrarily large without changing the retained initial-label/postmeasurement-state joint law at equilibrium. Preparation error is charged once; visible leakage and conditional-stationarity defects supply explicit extra bounds. In the charge model, blocking observed-dot tunneling requires a barrier actuator and controlled switching during the readout stage. It adds no recorded bit or tested word, but is a physical control resource. Independent symmetric electronics and the joint-instrument promise remain requirements. The existing 62-unit reset is target-only for the reference heat-bath model and does not establish independent repeated trials.

The [serial-reset verifier](scripts/verify_switch_serial_reset.py), [report](reports/switch_serial_reset.json), [source comparison](docs/FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_SERIAL_RESET_INTERNAL_REVIEW.md) accompany the conditional sampling and finite-reset results. The [percent-kinetic verifier](scripts/verify_switch_percent_kinetics.py), [report](reports/switch_percent_kinetics.json), [source comparison](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_INTERNAL_REVIEW.md) retain the direct robustness and local realization. The earlier [kinetic-interface verifier](scripts/verify_switch_kinetic_interface.py), [report](reports/switch_kinetic_interface.json), [source comparison](docs/FAMILIAR_SWITCH_KINETIC_INTERFACE_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_KINETIC_INTERFACE_INTERNAL_REVIEW.md) retain the protected-readout and integrated-error results. These records distinguish mathematical guarantees from experimental calibration.

The [observable-calibration verifier](scripts/verify_switch_observable_calibration.py), [report](reports/switch_observable_calibration.json), [source comparison](docs/FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_INTERNAL_REVIEW.md) record the new preparation inequality, scalar precision calculation and instrument boundary. The marginal-versus-joint disturbance distinction is established; a close recent full-text comparison remains unresolved.

The [weaker-field verifier](scripts/verify_switch_weak_field.py) and [report](reports/switch_weak_field.json) certify the new margin and trial counts. Its [source comparison](docs/FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_WEAK_FIELD_INTERNAL_REVIEW.md) record the inherited tools and new operating-point argument. The [physical-interface verifier](scripts/verify_switch_physical_interface.py) and [report](reports/switch_physical_interface.json) retain their 108 checks, and the [earlier cost verifier](scripts/verify_switch_uncalibrated_score.py) and [report](reports/switch_uncalibrated_score.json) retain the old score and information bounds. The [verification record](docs/VERIFICATION.md) distinguishes analytic review, finite checks and the complete repository gate.

The research target is **Physical Review Letters**; manuscript drafting remains the last step. The [current exploration](docs/PRL_EXPLORATION.md), [research dossier](docs/RESEARCH_DOSSIER.md), and [claim ledger](docs/CLAIM_LEDGER.md) retain the assumptions and unresolved questions. This is a controlled realization comparison, not an implementation-independent heat-cost result or a PRL-readiness claim.

## Earlier general principle: one state, two roles

The [matrix prediction principle](docs/MATRIX_RANK_PREDICTION_PRINCIPLE.md) starts with a nonnegative, completely positive matrix $H$ of size $n$, normalized so its entries sum to one and every row has positive sum. Its two relevant ranks count the fewest pieces in

$$
H=\sum_{s=1}^{r_+}u_sw_s^{\mathsf T},\qquad
H=\sum_{s=1}^{r_{\rm cp}}c_sc_s^{\mathsf T},
\qquad u_s,w_s,c_s\ge0.
$$

The first permits different entry and exit profiles. The second uses the same profile on both sides. For the controlled task constructed from $H$, the minimum total state counts are

$$
\boxed{D_{\rm all}(0)=1+n+r_+,\qquad
D_{\rm ord}(0)=1+n+r_{\rm cp}.}
$$

Here the single visible state and all hidden memory and probe states are counted. The target is ordinarily reversible, has hidden relaxation band $[k,3k]$ and hidden exit cap $2k$, and has an exact two-state passive binary path law.

The experiment has one binary readout, one fixed preparation, two field values and a positive control clock. Probe labels specify different kinetic rates; they are not extra observed colors. Rivals may introduce arbitrary new states, stationary masses and endpoint barriers in $[0,1]$, subject to the shared hidden exit cap $2k$. The lower bounds apply to this entire comparison class, beyond the displayed factorization constructions.

The sufficient predictors have a direct interpretation. A memory state chooses a distribution over the next probe. Every factorization maps stochastically to the same endpoint predictor, preserving the complete controlled binary-output path law. Ordinary detailed balance requires matching entry and exit flux profiles. Matched positive tests with reversed operator order then turn that requirement into a nonnegative Gram factorization, which supplies the lower bound.

For each fixed $H$, both counts persist over some positive accuracy interval and can be witnessed by finitely many clock experiments. The theorem does not give a useful uniform size for that interval. The number of kinetic labels grows with $n$.

The [source comparison](docs/SIMPLE_PREDICTION_SOURCE_AUDIT.md) separates established nonnegative factorization, stochastic intertwining and reversible realization ideas from this controlled prediction statement. The [internal review](docs/SIMPLE_PREDICTION_INTERNAL_REVIEW.md) records the proof checks.

## What the twelve-state example establishes

The [small incidence target](docs/FINITE_REVERSIBILITY_ADVANTAGE.md) stores an edge of a five-vertex graph. Its exact eleven-state stationary predictor stores a preselected endpoint. The relevant matrix has nonnegative rank five and completely positive rank six, giving exact minima of eleven and twelve total states through the general principle.

Positive-error results must be read at their stated precision. All entries below concern this same target, binary means, two fields $0,\log2$, shared interface and hidden exit cap $2k$.

| Certified statement | Accuracy and experiment scope |
|---|---|
| **Unrestricted minimum: 11** | $\delta\le2^{-1360}$ on the full clock task; words through 520 ticks already suffice for the lower. |
| **Ordinary-reversible minimum: 12** | $\delta\le2^{-220}$; an explicit list of 12,766 mean experiments, each at most 66 ticks, suffices. |
| **9 ordinary-reversible states suffice** | Error at most $1/2376$, uniformly over every two-field switching protocol and every horizon. |
| **2 ordinary-reversible states suffice** | Error at most $557/51920<0.01073$, with the same uniform protocol and horizon scope. |

The first row is the [minimum-count theorem](docs/FINITE_PREDICTOR_MINIMALITY.md). The second uses [bounded rational observation recovery](docs/BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md): an exact rational, computer-assisted certificate supplies an essential basis-conditioning bound, and the transfer to arbitrary reversible rivals is analytic. The remaining rows follow from [symmetry averaging](docs/SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) and [kinetic variance](docs/KINETIC_VARIANCE_COMPRESSION.md).

The eleven-state predictor is sufficient at every accuracy because its controlled predictions are exact. Its unrestricted minimality is not proved throughout the larger $2^{-220}$ interval or on the smaller experiment list. The numerical lower tolerance remains impractical, and these bounds leave a wide unresolved accuracy range. Neither upper bound is claimed optimal. An eleven-state generalized-reversible realization is not established.

## Heterogeneity both excites and reads hidden memory

The [variance theorem](docs/KINETIC_VARIANCE_COMPRESSION.md) gives the complementary physical explanation. Write $b_i(h)$ for hidden return rates in units of $k$, and let $c_i(h)=b_i(h)-\sum_j\mu_jb_j(h)$. This centered heterogeneity appears twice: it creates deviations from the stationary hidden distribution, and it couples those deviations back into the visible signal.

Eliminating the hidden density gives an exact memory kernel with one factor of $c$ at each end. Consequently the error of a two-state predictor using the averaged return rate is bounded by a constant times $\sup_h\operatorname{Var}_\mu b(h)$. Faster hidden mixing reduces that bound. If the return rates are identical at each field, the two-state reduction is exact.

This is a finite-amplitude, all-horizon statement. It allows stationary nonreversible hidden dynamics and needs no microscopic state-count or minimum-mass factor. A conditional-variance version also explains the nine-state symmetry quotient. Averaged barrier curves belong to the broad kinetic interface class; on two queried fields they can be implemented by one exponential curve with matching endpoints. Interval-wide exponential matching is a separate requirement.

## The larger separation and the reversal convention

On a different, nineteen-level target family, the [resource theorem](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) gives the following worst-case state growth at accuracy $\delta$:

| Predictor class | Total state growth |
|---|---|
| Stationary | $\delta^{-\Theta(1)}$ |
| Generalized reversible under a specified state involution | $\delta^{-\Theta(1)}$ |
| Ordinarily reversible | $\exp(\delta^{-\Theta(1)})$ |

These comparisons use the same target family, two physical fields, any fixed positive clock, common hidden exit cap $3k$, preparation and binary readout. Targets retain hidden band $[k,3k]$. Rivals may choose arbitrary bounded kinetic barriers without matching a histogram or a finite label alphabet. The exponents are unmatched; state count does not charge parameter precision, construction time or sampling cost.

The [generalized-reversal predictor](docs/GENERALIZED_REVERSAL_PREDICTION.md) reverses a retained memory word while preserving its actuator value. Its entropy production is zero under that reversal, even when identity-reversal entropy production is positive. Thus an ordinary-reversal state penalty is **not a universal thermodynamic dissipation or heat requirement**. The physical reversal of retained variables must be specified. The [entropy comparison](docs/GENERAL_INTERFACE_ENTROPY_BOUND.md) and [resource frontier](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) retain their explicit identity-reversal meaning.

## Scope, evidence and next questions

The [single-force conformational model](docs/SINGLE_FORCE_CONFORMATIONAL_MODEL.md) interprets the earlier hub network through force-dependent equilibrium bias and transition-state barriers. It is not the coupled-switch model or a demonstrated molecular implementation. [Interface robustness](docs/PHYSICAL_INTERFACE_ROBUSTNESS.md) treats small rate and ramp errors within that earlier setting. The new switch result has certified fixed-calibration tolerances and sampling bounds, but no device implementation or claim of experimental practicality. A natural implementation of generalized-reversal memory is a separate question.

The repository contains older binary, uncapped-rate, response-order and compression theorems with different assumptions. Their proofs remain unchanged and are indexed in the [claim ledger](docs/CLAIM_LEDGER.md) and [dossier](docs/RESEARCH_DOSSIER.md). Internal mathematical reviews, source comparisons and finite certificates are different kinds of evidence; none constitutes external peer review or a complete priority determination.

For reproducibility, use the pinned environment and the [Makefile](Makefile):

```sh
make check PYTHON=.venv/bin/python
```

[Verification](docs/VERIFICATION.md) records the full suite and its limits. The four-word experiment removes rival preparation, and its new endpoint-registration formulation replaces exact protection and fixed symmetric errors by quantitative measurement conditions. The relative-force bound controls rare-state errors that unweighted stationary-law TV cannot control. The current priority is the [two-field approximation gap](docs/FAMILIAR_CHAIN_TWO_FIELD_ACCURACY.md): determine how much error is unavoidable for reversible models below six states. The [community-model comparison](docs/PHYSICAL_ASSUMPTION_ALIGNMENT.md) remains the physical-assumption reference. Quantitative device feasibility and the close prior-art comparison remain open. Current counts are sufficient bounds, not optimal costs or demonstrated feasibility. Manuscript drafting remains deferred.

</details>

</details>
