# PRL exploration: a short memory test and its calibration boundary

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Observable preparation](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) · [Calibration precision](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) · [Readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) · [Verification](VERIFICATION.md)

## Current result: control range and observation scope — 25 September 2026

The [scope assessment](FAMILIAR_SWITCH_CONTROL_SCOPE.md) now gives a
concrete model-selection result for the same published coupled-dot family.
Passive pairs have a reversible three-state realization; one passive
three-time law requires four states even without equilibrium or stationary
preparation premises on the rival. The [temporal proof](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md)
gives a positive unrestricted TV margin and the exact error when all
pair marginals are retained. A model of endpoint pairs is therefore not
automatically a model after intermediate observations.

The [signed-control theorem](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md)
proves an exact threshold: with $t=\tanh J$, $u=\tanh H$, and attempt
ratio $r=\Gamma_Z/\Gamma_S>0$, three states suffice exactly when
$(r+2)t^2u^2+(1+t^2)u\le r$. Above it, even the general class needs
four. Ordinary reversible models always need four for positive coupling
and field. The linear mean dimension stays three across the threshold.
The criterion is equivalent for all signed-field endpoint protocols and
a fixed 23-word pair menu of at most five ticks. The latter has positive,
unquantified TV margins and permits an arbitrary common preparation.
Any exact three-state fit must inherit positive equilibrium preparation
and the Gibbs stationary family from the data.

The new common-preparation requirement differs from the four-word lower's
arbitrary per-word preparations and declared force rule. The temporal
result separately requires an ideal nondisturbing middle observation.
No detector guarantee, full-path compression, hardware-bit saving or
thermodynamic implementation cost is inferred.

The [source audit](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md) compares
the complete claims with switched realization, common-cone and hidden-state
factorization results, and corrects older Taghavian normalization wording.
These are established methods; the candidate contribution is the explicit
physical-model criterion and state-count map. Broader significance remains
open. The next research task is to test whether the mechanism survives a
small, independently established extension of the kinetic family, beginning
with the already-recorded three-switch chain. Do not equate its linear
closure with a positive Markov upper. Manuscript drafting stays last.

[Exact certificate](../reports/switch_control_scope.json) ·
[Verification](VERIFICATION.md).

## Historical development and conditional extensions

**Owner's physical-model requirement, 24 September 2026.** The next step is to ground the target, controls, measurement and rival comparison in one independently established community model. A favorable accepted idealization is allowed; adding unsupported physical capabilities to rescue a theorem is not. The [assumption ledger](PHYSICAL_ASSUMPTION_ALIGNMENT.md) distinguishes published physics, derived specializations, our numerical design choices and operational premises still needing justification. This model comparison precedes further device feasibility engineering. Existing conditional results remain unchanged; manuscript drafting remains last.

**Research target, 24 September 2026.** The new [endpoint-registration theorem](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md) measures the initial sign after acquisition and the final sign before acquisition. Arbitrary initial measurement dynamics then join the rival's arbitrary preparation. A known conditional endpoint-error bound $5\times10^{-6}$ replaces exact protection, fixed symmetric electronics and repeated-read freshness. A finite integrating detector supplies a sufficient signal/noise/leakage contract, including switching time; its demanding numerical specification is not a device result. The [relative-force theorem](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md) permits residual likelihood-ratio spread $1.001$ without a stationary-mass floor. The same nine-million-trial test has size below $4\%$ and target miss below $1.4\%$, using 18 million integration windows and binary decisions. Ideal four-pair state minima remain three versus four through TV $.0009$. Target postmeasurement marginal preparation, fixed active dynamics and calibrated conditional bounds remain substantive. Manuscript drafting stays last; device feasibility and a complete priority comparison remain open.

## Historical advance: register the actual active boundaries

The initial oracle sign is the sign of the state entering the active word, after the entire acquisition operation; the final oracle sign is taken immediately when the word ends, before the final acquisition. Conditional on a singleton initial sign, any preceding disturbance disappears from the ordinary model's conditional response. The detector only needs to identify these boundaries with a known uniform conditional error bound. This is a calibrated alternative to the previous unknown-fixed-error repetition scheme, not an automatic enlargement of that scheme's detector class.

One finite integration window per endpoint is sufficient under a signal floor $g>0$, continuous noise martingale with quadratic variation at most $vT$, and whole-acquisition sign-change probability $\Lambda$. The bound is $e^{-g^2T/(2v)}+\Lambda$. Taking $T=32v/g^2$ and $\Lambda\le4\times10^{-6}$ gives endpoint error below $5\times10^{-6}$. Integration duration and total acquisition span must be distinguished: barrier ramps, settling and release consume the same leakage budget. Hidden-charge offsets and asymmetric noise are allowed within the uniform bounds. Average histogram fidelity, small observed jump counts and unspecified colored noise do not establish them.

The initial target operation now needs only the full-channel marginal bound $\operatorname{TV}(\pi D,\pi)\le10^{-5}$. Symmetric barrier changes at fixed energies preserve $\pi$ even with rare visible jumps, giving a concrete mathematical target construction. The actual post-acquisition true pair still has conditional reference budget $79\times10^{-6}$; its recorded pair differs by at most $.000089$. This supplies a per-trial three-state approximation, not a full serial or analog-record state minimum.

Residual stationary reweighting beyond the nominal Gibbs tilt may have maximum/minimum ratio $1.001$. Its singleton residual ceiling is $.0004$, independent of rare stationary weights. A three-state finite-CTMC counterexample shows that arbitrarily small unweighted stationary-law TV error can instead coexist with fixed nonzero return residuals under arbitrary preparation; an irreducible extension preserves the obstruction. This identifies why relative force control is the relevant assumption.

The same nine million cyclic trials and first-million sign quotas retain false rejection below $4\%$ and target miss below $1.4\%$. There are 18 million integrating windows/decisions, not 18 million analog samples. With target attempt frequency $\Gamma$ and common integration time $T$, reset plus active evolution plus integration costs $583875000/\Gamma+18000000T$ seconds, before other overhead. The [eight-source audit](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_SOURCE_AUDIT.md) supports separate component precedents; it does not establish this combined specification. [Internal review](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_INTERNAL_REVIEW.md) and [certificate](../reports/switch_endpoint_registration.json) keep the analytic and finite-check evidence distinct.

## The four-word core: conditioning replaces rival preparation

Write $r_{w,s}=\Pr(S_f=s\mid S_i=s,w)$. An ordinary model with at most three states and both visible signs has a singleton sector $s$. Sign-preserving initial observation leaves its hidden state fixed. For arbitrary per-word and history-dependent preparation,

$$
 (1-su)r_{0H,s}-(1+su)r_{H0,s}+2su r_{0,s}r_{H,s}=0.
$$

No balanced rival equilibrium, rival mixing estimate, stationary-mass lower bound or stationary rival instrument is needed. Strictly positive stationary laws, exact Gibbs tilt and the same two field kernels remain required. At the stationary target, both signed residual magnitudes exceed $.009$ over the independent one-percent edge box. The added single-word correlations are $a=1-m/u$ and $x=(\ell+ud)/u$, precisely the two coordinates already fitted by the general three-state construction. This is a stronger experimental comparison using the same conditional-covariance mechanism.

Nine million trials cycle through the four words. Each word/sign group retains its first million observations. Missing quotas imply nonrejection; completed groups reject only when $\widehat R_->.004$ and $\widehat R_+<-.004$. Stopped martingale bounds handle serial dependence without conditioning on successful completion. The target reference-pair execution budget is $79\times10^{-6}$ after every history. It applies only to target power, never to the rival null.

With seven protected reads per endpoint, a disagreement gate at each stage handles unknown rival error rates in $[0,1/2]$. Under the low-error case, a deterministic comparison of noisy and true-sign retained lists controls selection errors; the null needs no stationary preparation even when measurement errors correlate with hidden kicks. The 126-million-read construction is sufficient, not an optimized or practical budget. Only the four ideal binary pair laws have the exact three-state upper; the extra calibration transcript has no claimed state minimum.

[Proof and certificate](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) · [Readout proof](FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md) · [Source comparison](FAMILIAR_SWITCH_PREPARATION_FREE_SOURCE_AUDIT.md) · [Internal review](FAMILIAR_SWITCH_PREPARATION_FREE_INTERNAL_REVIEW.md).

## 1. The short physical mechanism

The target is a pair of time-even conformational switches: energy $-JSZ-hS$, heat-bath flips and equal attempt rates. Observe only $S$. Prepare once at low-field equilibrium, run either $0H$ or $H0$, and record the initial/final binary pair. Define

$$
m=\mathbb E_A Y,\quad c=\mathbb E_A(IY),\quad
\ell=\mathbb E_B Z,\quad d=\mathbb E_B(JZ).
$$

Under the shared Gibbs relation $\pi_H=\pi_0(1+uS)$, with $u=\tanh H$ and balanced $\pi_0$, ordinary detailed balance gives

$$
u c-u(1+\sigma m)d+\sigma(u-m)\ell
=-\frac{\sigma u^2}{1-\sigma u}
\operatorname{Cov}_{\pi_0}(E_HS,E_0S\mid S=\sigma).
$$

A model with at most three states and deterministic binary readout has a singleton sector, whose conditional covariance vanishes. The hidden conformation in the physical pair changes both response propensities within both sectors, so both covariances are positive. Every ordinary rival needs four states. The positive stationary three-state predictor matches the conditional initial coordinates and hence both joint laws exactly.

The lower allows arbitrary rival graphs, masses and rates, including reversible stochastic tick kernels. One fixed preparation, instrument, readout and pair of propagators must explain both protocols. This is a constrained dynamical realization comparison. It does not certify a device-independent dimension, entropy production, or complete controlled path-law equality.

## 2. The detector-unknown result

Let $(M,C,L,D)$ be the recorded versions of the four moments after fixed
independent symmetric errors at the initial and final readouts. The
[witness](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) uses

$$
 R=u(C-D)+uMD-(u-M)L>0,\qquad
 0<M<u,\quad L,D>0,\quad C<D.
$$

The detector-cleared singleton polynomial is bilinear in the two unknown
contrasts. Its four corner signs rule out every ordinary rival with at
most three states, even when that rival chooses its own two error
probabilities anywhere in $[0,1/2]$. There is no inverse-contrast
singularity or rival rate cap. Symmetry, independence, no readout feedback
and one fixed detector across both protocols remain required.

**Earlier preparation calibration result and its cost.** The
[observable preparation theorem](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md)
extends the earlier exact-balance lemma to arbitrary preparation
$\nu$ and stationary imbalance $|\pi S|\le V<1$ for models with
at most three states. It controls the equilibrium bias of specified
responses through a low-pair relaxation guard and their change after
an extra low preparation step. No rival mixing time, rate cap or
minimum stationary mass is used. The instrument must exactly preserve
the visible sectors and stationary law, with independent fixed symmetric
electronics. Prefixed types include a silent copy of that same instrument
before the calibration low wait; the added operation has a physical cost.

The optional experiment has five types. The
[sampling theorem](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md)
randomizes the type after preparation, independently of its hidden state,
and uses known assignment probabilities. All response estimates then
refer to one pathwise averaged preparation even when the individual
preparations depend on the history. Under the stated population guards,
60 billion trials suffice to estimate eight corrected score functionals
simultaneously within $.001$ with probability above 96%. This is a
conservative precision construction, not a cost lower bound or a full
rejection/power guarantee. Localization, guard confidence, target
acceptance and the larger physical error budget remain to be analyzed.
The original three-state upper, five-million count and approximate-null
allowance do not transfer to the added calibration data.

The [readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md)
gives a three-state counterexample that preserves the visible bit and
passes arbitrary immediate repeat-readout, low-only and stationary
endpoint-insertion checks. Electronic errors correlated with hidden
kicks nevertheless change each original joint table by TV $1/4800$.
This does not fit the selected target or falsify its gated score. Under
the additional independence premise, sector-preserving instruments on
at most three states do admit an endpoint-to-joint TV identity. The
premise itself is not established by the listed calibration records.
The [source audit](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md)
records established disturbance and sampling ideas and an unresolved
recent full-text comparison; no priority claim follows.

**Preserved extension: serial sampling and finite target preparation.** The
[serial theorem](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) retains the
one-percent score test's five million trials, empirical gates and
threshold .0021, with deterministic alternating arms. Conditional on
every previous history, the actual recorded pair must be within TV
$.000079$ of one fixed nominal target reference pair, or $.00022$
of one fixed stationary ordinary reference pair. The latter includes
the $.0002$ approximation allowance. Reference generators and detector
channels remain fixed throughout the experiment. Unconditional or
time-averaged closeness, and changing reference models with the history,
do not satisfy this premise.

Conditional concentration proves size below 5% and power above 95%
without assuming independent trials. The [finite-reset bound](FAMILIAR_SWITCH_FINITE_RESET.md)
gives preparation TV below $10^{-5}$ after an actual low-field wait
of 63 units, from every preceding hidden-state law and history, for
the full one-percent target family with $|h_0|\le10^{-5}$. This
replaces the allocated preparation allowance; it is not an additional
error charge. Five million resets plus the nominal active pulses cost
327.5 million attempt-time units, 26.2 times the active-only exposure,
before readout and switching overhead. No physical attempt rate is
assumed.

The target reset does not give a uniform mixing time for arbitrarily
slow rivals. The serial statistical null explicitly requires the
conditional preparation promise for its own fixed model, separately
from the uncapped stationary population theorem. The latter remains
unchanged. The [verifier](../scripts/verify_switch_serial_reset.py),
[report](../reports/switch_serial_reset.json),
[source audit](FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) and
[internal review](FAMILIAR_SWITCH_SERIAL_RESET_INTERNAL_REVIEW.md)
record this distinction and the finite checks.

**Preserved extension: independent one-percent kinetic departures.** Keep
$J=\log3$, $H=\log2$ and both dwells $5/4$. The
[direct robustness theorem](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md)
allows one independent prefactor in $[.99,1.01]$ on each undirected
transition edge at each plateau: eight factors, with both directions
of an edge scaled together. Fixed plateau generators and the Gibbs
laws are preserved. No new observations, states or protocol types
are introduced. The ordinary rival class still allows arbitrary
reversible kernels without a rate cap.

A degree-two perturbation expansion with a rigorous remainder bounds
the recorded witness directly over the entire box. The
[local realization](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md)
fits four moment coefficients and certifies positive three-state
kernels whose logarithms are genuine Markov generators. This gives
exact nominal-field snapshot prediction without assuming target
mean closure. The fitted model is fixed across the two words;
other words and full trajectories are outside this local theorem.

At nominal fields and times, stationary preparation and ideal initial
instrument, the state minima are three versus four on $[0,.001]$.
With all six preparation, field, timing and initial-instrument
allowances $10^{-5}$, the target table displacement is
$b_T=.000078025101$ and the rival allowance remains $.00002$.
Thus the actual state interval is **$[.00008,.0009]$**.
The stationary bias, tilt and independent symmetric detector
promises remain those of the reference experiment.

The [new score test](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md) uses
2.5 million fresh independent trials per arm, **five million total**
and ten million binary readouts. It retains the integer scores below,
with new gates and threshold .0021, for size below 5% and power
above 95%. Its null joint-TV allowance $.0002$ exceeds the
constructive three-state error. Relative to the preceding kinetic
test, the sufficient relative rate allowance grows 500-fold from
20 ppm to 1%, with unchanged total trial count and null allowance.
This is a new proof for an enlarged family, not an optimal tolerance
or a demonstrated device capability.

**Preserved integrated-error extension.** Keep $J=\log3$,
$H=\log2$ and both dwell times $5/4$. The
[kinetic tolerance theorem](FAMILIAR_SWITCH_KINETIC_TOLERANCE.md)
allows a fixed perturbed generator at each actual plateau, shared
across the words, preserving the Gibbs stationary law and ordinary
detailed balance. The integrated signed generator-row TV defect
$\kappa\le10^{-4}$ transfers both full recorded joint laws. Alongside
the $10^{-5}$ physical allowances below, the general-three-state
error is at most $0.00012$ and the ordinary-three-state error is
greater than $0.0009274999$. Hence the state minima remain three and
four throughout **$[0.00012,0.0009]$**. Exact compression of the
perturbed model is not required or claimed.

Symmetric edge-prefactor changes of at most 20 ppm are one sufficient
condition. They can depend on neighboring charge and break affine
closure while preserving detailed balance. A 100-ppm allowance
separately leaves the population interval $[0.0005,0.00055]$, with
no sampling guarantee. Arbitrary time variation inside an active
plateau is excluded because an ordered product of reversible kernels
need not itself be reversible. The rivals already allow arbitrary
reversible kernels, so they receive no extra kinetic restriction.

The [earlier sampling theorem](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md)
retains the scores and empirical gates below, uses threshold .0022,
and collects 2.5 million fresh independent trials per arm. Its
**five-million total**, or ten million binary readouts, gives false
rejection below 5% and target power above 95%, allowing null joint-TV
prediction error $0.0002$ per word. This exceeds the constructive
general-three-state upper. The enlarged family's budget is separate
from the two-million reference guarantee and the old-design lower
bound; no cheaper-experiment claim follows from this extension.

**Preserved heat-bath reference.** At $J=\log3$, $H=\log2$ and equal dwell
$5/4$, the [new robustness proof](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md)
certifies nominal recorded joint-TV separation $>0.00115$ when each
target detector error is at most one percent. Preparation, field,
timing and initial-disturbance budgets $10^{-5}$, stationary bias and
relative-tilt uncertainty $10^{-4}$, and high-law TV defect $10^{-5}$
leave an actual separation $>0.001$. Three general states suffice
within $2\times10^{-5}$, giving state minima three and four throughout
$2\times10^{-5}\le\delta_{\rm obs}\le10^{-3}$.

The [new score test](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) assigns
small integer scores to the already recorded pairs. It uses
$X_A=(20Y+30IY-15I)/50$,
$X_B=(-20Z-24JZ+15J)/50$, and
$\widehat T=\overline X_A+\overline X_B-2/25$, together with the
proof's fixed empirical gates. The initial-bit corrections cancel
under the common preparation and channel, and reduce variance without
adding an observation. Both designs have false rejection below 5%
and target power above 95% for fresh independent trials:

| Unknown-detector null | Trials per arm | Total paired trials | Binary readouts | Threshold |
|---|---:|---:|---:|---:|
| Admissible ordinary model, at most three states | 1,000,000 | **2,000,000** | 4,000,000 | .002 |
| Same model class, observed-joint-TV allowance $10^{-4}$ | 1,250,000 | **2,500,000** | 5,000,000 | .00218 |

The second allowance exceeds the constructive general-three-state
error. Relative to the old design's sufficient budgets below, these
totals improve by factors of 16 and 36 while reducing active duration
from three to $5/2$ attempt-time units. The old information lower
also gives a stronger comparison: at its nominal target with one-percent
errors, any valid test confined to the old two protocols needs
$\mathbb E_*N>810000\log19>2{,}384{,}995$. The new sufficient
two-million total falls below this old necessary count. The nulls have
the same form at their respective fields, rather than being identical
sets of fixed-field laws. The comparison does not lower-bound the new
experiment, optimize over designs, or price preparation overhead.

The simpler physical explanation is reduced detector loss. For equal
contrast $r$, the witness obeys
$R(r,r)=r^2R(1,1)-r(1-r)u(\ell+rmd)$.
The new point has a smaller ideal witness but a smaller noise penalty,
leaving a larger recorded signal. No monotonic field-strength rule or
optimal operating point is claimed.

A separate population-level tolerance corollary raises all preparation,
field, timing and disturbance allowances to $5\times10^{-5}$ while
retaining state minima three and four on
$10^{-4}\le\delta_{\rm obs}\le6\times10^{-4}$. The two sampling
allocations above remain proved only for the $10^{-5}$ allowances.

**Preserved earlier operating point: $J=H=\log3$, dwell $3/2$.**
For this equal-rate target with each error probability at most
one percent, the nominal recorded-joint-TV gap exceeds $3/8000$.
Allowing the stated preparation, control and initial-disturbance errors
$10^{-5}$, low stationary bias and relative-tilt uncertainty $10^{-4}$,
and high-law TV defect $10^{-5}$ leaves a gap greater than $1/5000$.
Three general states suffice within $2\times10^{-5}$, so the state
minima are three and four throughout
$2\times10^{-5}\le\delta_{\rm obs}\le2\times10^{-4}$.
The target signal-loss bound differs from numerical calibration of the
rival's detector: its errors are allowed anywhere up to one half.

The [earlier fixed-score test](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md)
uses only the already recorded bits:

$$
 X_A=\frac{(13+20I)Y-10I}{25},\qquad
 X_B=\frac{-(10+12J)Z+10J}{25}.
$$

Its statistic is $\overline X_A+\overline X_B-26/125$, with the
empirical localization gates and fixed threshold given in the proof.
The initial-bit corrections have cancelling expectations because the
same preparation and initial channel serve both protocols. Their
within-trial correlation lowers variance without adding a measurement
or assuming exact observed balance. Integer lookup scores, a fixed
allocation and bounded-variable concentration suffice.

| Unknown-detector null | $0H$ trials | $H0$ trials | Total paired trials | Binary readouts |
|---|---:|---:|---:|---:|
| Physical allowances, no additional approximation error | 18,560,000 | 13,440,000 | **32,000,000** | 64,000,000 |
| Same class, observed-joint-TV approximation allowance $10^{-4}$ | 52,200,000 | 37,800,000 | **90,000,000** | 180,000,000 |

Both designs have false rejection below 5% and target power above 95%
for independent fresh trials. The finite-accuracy allowance exceeds the
constructive general three-state error $2\times10^{-5}$. The first
508-million-trial confidence-box design remains valid, but the new
score improves its sufficient total by a factor of 15.875 on the same
class. These totals are not necessary or optimal. The calibrated counts
below do not transfer to this enlarged null.

The [detector information bound](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md)
shows that some of the increased cost is unavoidable. For the fixed
nominal target with one-percent errors at both readouts, a rational
ordinary three-state comparator with a perfect detector has per-arm
relative entropy below $1/900000$. Any test with the same 5%/95%
guarantees therefore needs $\mathbb E_*N>810000\log19$, even with
adaptive arm choices and an almost-surely finite stopping rule; a fixed
budget must be at least **2,384,996 paired trials**. The earlier
calibrated 1.2-million-trial test covers this same target. Consequently
the calibration promise has a strict observation-budget value exceeding
a factor of 1.98. This comparison does not price obtaining calibration,
match the necessary and sufficient bounds, or extend to richer data.

## 3. The preserved calibrated gap

At $J=H=\log3$ and tick $3/2$, the best ordinary-three-state maximum TV error over the two joint laws lies in

$$
(23/12500,37/20000)=(0.00184,0.00185).
$$

The lower is a universal response-box exclusion; the upper is a fixed positive rational ordinary model. Their ratio is $185/184$. The numerical fits only supplied candidates for the upper. The longest active sequence lasts three attempt-time units.

The [robustness proof](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) derives a biased/approximate-Gibbs identity directly for the snapshot moments. A stationary joint-TV radius $0.0018$ is excluded with low-field stationary bias and tilt-parameter uncertainty $10^{-4}$, and high-stationary-law discrepancy $10^{-5}$. Simultaneous preparation TV, fixed field/tick errors and initial disturbance bounds $10^{-5}$ retain a positive executed gap.

Independent symmetric detector flips at the two observations are modeled separately. A known 1% channel contracts TV by at most the factor $0.98^2$ in the lower bound. Allowing each flip probability to lie in $0.01\pm10^{-5}$ still leaves recorded joint-law gap $>0.0015$. A constructive three-state upper has error at most $4\times10^{-5}$, so state minima remain three versus four on $[4\times10^{-5},0.0015]$.

The initial disturbance bound controls the hidden state conditional on its premeasurement state. Neither visible balance nor a short readout duration establishes it. The detector model has no free persistent hidden memory, and the channel's flips are independent of the trajectory and one another. The 1% operating point is a mathematical example, not an experimentally validated instrument.

## 4. Preserved calibrated tests and the resource trade

A fixed tangent score concentrates the statistics relevant to the covariance identity. A gate bounds the quadratic remainder; bounded-variable Bernstein inequalities give uniform false rejection below 5% and target power above 95%. All choices are fixed before observations. Calibration bounds and fresh-trial independence are separate premises. These earlier tests retain their calibrated detector classes.

| Design | Fresh trials | Readouts per trial | Equilibrium preparations |
|---|---:|---:|---|
| Nominal four-endpoint score | 1,450,000 | 1 | Low and high |
| Calibrated four-endpoint score | 1,670,000 | 1 | Low and high |
| Calibrated endpoint score, occupation allowance $10^{-4}$ | 1,890,000 | 1 | Low and high |
| Nominal two-snapshot score | 900,000 | 2 | Low only |
| Physical nuisance, ideal snapshot readout | 1,000,000 | 2 | Low only |
| Fully calibrated noisy snapshot score | 1,200,000 | 2 | Low only |
| Same noisy class, observed-joint-TV allowance $10^{-4}$ | 1,500,000 | 2 | Low only |

The endpoint allocations improve the earlier sufficient confidence-box counts by roughly a factor of nine on the same classes. Snapshot trials require fewer resets and no high-field preparation, but more binary readouts than the comparable endpoint designs. The noisy snapshot row also covers detector assumptions absent from the endpoint rows. These are sufficient choices, not optimal sample budgets.

A separate nominal information lower requires fixed budgets of at least 174,900 endpoints or 79,500 paired trials for their respective observation tasks. The necessary and sufficient counts are not matched. The paired lower also survives a common known detector channel by data processing.

Low-field target reset time 62 suffices at the stated preparation tolerance; high-field time 36 is used only by the endpoint designs. For noisy snapshots, serial target exposure is at most $(65+2\times10^{-5})N$ attempt-time units. These waits neither equilibrate every arbitrarily slow rival nor establish trial independence. Computation remains tiny-matrix CPU work suitable for the user's hardware.

## 5. Conditional physical realization and preparation limits

The [charge realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) starts
with two capacitively coupled nondegenerate dot occupations, each
exchanging particles with its own equal-temperature equilibrium reservoir.
With compensated spectator energy and sequential Fermi tunneling, the
charge energy maps exactly to $-JSZ-hS$; both charge variables are
time-even. A positive three-state triangle covers attempt ratios
$r=\Gamma_{\rm hidden}/\Gamma_{\rm observed}\ge2/3$ over the selected
field range. Restricting $r\le2$ gives the common exit cap
$3\Gamma_{\rm observed}$. Exact compression therefore does not require
equal tunneling rates. The finite numerical gaps and sample allocations
remain certified only at $r=1$.

This model requires isolated relevant levels, the specified Fermi rates,
and controlled unwanted transitions and gate leakage. The
[primary-source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)
identifies relevant demonstrated components without combining them into
a claimed achieved device specification. Spin degeneracy, energy-dependent
prefactors and metallic-box kinetics cannot be removed by relabeling
their equilibrium energy.

The [preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)
shows two distinct failures: every low-only binary trajectory can look
stationary while hidden preparation bias remains, and an instrument can
preserve every endpoint distribution while destroying the initial/final
correlation. A response-specific bound for at-most-three-state rivals
can replace a preparation premise after adding three protocol types
and assuming exact balance. It leaves the instrument premise in place
and has no inherited sampling allocation.

The [protected-readout theorem](FAMILIAR_SWITCH_PROTECTED_READOUT.md)
now supplies a structural sufficient condition for that instrument.
Hold the observed sector fixed and preserve its conditional equilibrium
law. The joint law of the retained initial label and postmeasurement
hidden state is then exactly the ideal one at equilibrium, even with
arbitrarily large hidden rearrangement. Preparation TV is charged once.
With imperfect protection, the integrated visible-jump hazard and
conditional stationary-flux defects bound the joint error. This
condition concerns correlations, not only the postmeasurement marginal.

For the charge model, the proposed operation blocks observed-dot
tunneling while the spectator relaxes at unchanged conditional odds.
It adds a barrier actuator, switching accuracy and readout time to the
instrument resources, although it adds no recorded bit or tested word.
Whether it protects every admitted rival is still a premise; target
control alone does not establish that. Constant-state detector errors
must remain independent symmetric channels. The old 62-unit reset
bound applies only to the specified reference heat-bath target, not
the new kinetic family or arbitrary slow rivals, and does not turn
serial measurements into independent trials.

## 6. Scientific assessment and next priority

The mechanism is concise: reversed pulse order measures a conditional covariance, and a singleton sector cannot support it. Direct treatment of the paired data strengthens the previous $0.001$ snapshot corollary and gives its own nuisance and sampling guarantees. The endpoint task retains its original deterministic theorem and gains a more efficient test.

The weaker-field point now supplies a larger certified observed
separation and a smaller sufficient count than the old experiment's
necessary count. Its [original exploration note](FAMILIAR_SWITCH_NEXT_OPERATING_POINT.md)
is retained as a historical numerical lead; the new proofs and exact
certificate supply the robustness and statistical conclusions.
The earlier calibration-value theorem remains tied to its original
field and dwell. No lower bound or calibrated trial count is transferred
to the new point merely by changing parameters.

The endpoint-registration result now supplies a concrete conditional measurement specification and permits small leakage, asymmetric errors and history dependence. Relative force control handles rare stationary states without restoring a preparation or mass-floor premise. The next priority is to assess a physical operating regime against the combined signal, noise, leakage, marginal-disturbance and force requirements, while comparing the complete state-cost theorem with close prior work. The eight-source audit establishes component precedents, not achieved performance. Further minor score tuning is secondary. Manuscript drafting remains deferred.

The [percent-kinetic source comparison](FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md)
and [internal review](FAMILIAR_SWITCH_PERCENT_KINETIC_INTERNAL_REVIEW.md)
separate standard perturbation and embedding tools from the local
snapshot construction and certified physical error box.

The [kinetic-interface source comparison](FAMILIAR_SWITCH_KINETIC_INTERFACE_SOURCE_AUDIT.md) and [internal review](FAMILIAR_SWITCH_KINETIC_INTERFACE_INTERNAL_REVIEW.md) distinguish structural conditions and conservative perturbation estimates from demonstrated device capabilities. The [weaker-field comparison](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) and [review](FAMILIAR_SWITCH_WEAK_FIELD_INTERNAL_REVIEW.md) preserve the operating-point argument and established statistical tools. The [earlier statistical comparison](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md) retains the calibration-information attribution. The unresolved Falk full-text comparison remains open. Internal review and finite certificates are not external validation, a complete priority determination, or PRL readiness. Manuscript drafting stays deferred.

## 7. Preserved results and provenance

The [four-endpoint theorem](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) retains its two-preparation occupation-gap bracket $(9/5000,1/550)$ and calibrated gap $>1/625$. The [seven-endpoint theorem](FAMILIAR_SWITCH_FINITE_MARGIN.md) and [calibration theorem](FAMILIAR_SWITCH_CALIBRATION.md) retain their single-preparation statements. The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md), [variance principle](KINETIC_VARIANCE_COMPRESSION.md), and [asymptotic reversal theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) concern separate families and interfaces.

The preceding snapshot checkpoint started from published commit
5ad525792de4e4fe6c681b067d7185e018265082, tree
cdfa71f58ca37c832f5631e5c21484ae88b25805, with successful
[CI run 35958827202](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35958827202).
The physical-interface continuation started from published commit
778954f18164c3a228b845be07298ba1a33326eb, tree
e08a840c71d2474a5ad4866d9daf1c39969e92f6. The score/information continuation started from
published commit 9983da2206c0a84e1ce5e111a9d132331afe70f5, tree
5da1fadc9fe9877e916a5b2a2c775ea6dcfe256d, with successful
[CI run 35966287099](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35966287099).
The weaker-field continuation started from published commit
7e41d378e87ce5d7524e585c387707638c391ae1, tree
eafae1855a511389c4d07e8fe730a3f6795ff3dc, with successful
[CI run 35969236097](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35969236097).
The kinetic-interface continuation started from published commit
2ffed6de204354e257a344359497fb1e059cc04e, tree
bcccfafdc14dc8abbc3b5187bf4751f424c297e9, with successful
[CI run 35972519604](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35972519604).
The percent-kinetic continuation starts from published commit
24c2cc3185dbff17ce23c366413484fe94e25656, tree
cce6133f62ead44e27d346491075b92d984884f1, with successful
[CI run 35975279317](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35975279317).
The serial-reset continuation starts from published commit
e80ebbf78f92332e911d35818ae8c6fe659cc77a, tree
36b901a2782b43885af315055c0f603055f850bb, with successful
[CI run 35979212122](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35979212122).
The observable-calibration continuation starts from published commit
f026f67d26b8f5617ff5a27ea1c99648b4a85e69, tree
0d88522949938e6ccc5b5cbeae4802130dd3ffa5, with successful
[CI run 35981239851](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35981239851).
Earlier protected proofs, certificate bindings, recovery files and the
original license remain preserved. The
[physical-interface verifier](../scripts/verify_switch_physical_interface.py)
and [report](../reports/switch_physical_interface.json) pass 108 exact
checks at maximum dense dimension four. The
[internal review](FAMILIAR_SWITCH_PHYSICAL_INTERFACE_INTERNAL_REVIEW.md)
records the proof and source audits.
The preserved [score/information verifier](../scripts/verify_switch_uncalibrated_score.py)
and [report](../reports/switch_uncalibrated_score.json) certify the fixed
test and the rational ordinary comparator.
The preserved [weaker-field verifier](../scripts/verify_switch_weak_field.py)
and [report](../reports/switch_weak_field.json) certify the target
enclosures, robust gap and both trial allocations.
The [kinetic-interface verifier](../scripts/verify_switch_kinetic_interface.py)
and [report](../reports/switch_kinetic_interface.json) check the new
kinetic budgets, five-million-trial allocation and protected-readout
finite identities; the linked proofs carry the universal arguments.
The [percent-kinetic verifier](../scripts/verify_switch_percent_kinetics.py)
and [report](../reports/switch_percent_kinetics.json) cover the entire
one-percent parameter box, local CTMC realization and revised score.
The [serial-reset verifier](../scripts/verify_switch_serial_reset.py)
and [report](../reports/switch_serial_reset.json) check the enlarged
conditional variance boxes, unchanged sampling margins, uniform reset
bound and exposure arithmetic.
The [observable-calibration verifier](../scripts/verify_switch_observable_calibration.py)
and [report](../reports/switch_observable_calibration.json) check the
new finite preparation, precision and instrument fixtures; the analytic
proofs carry their universal and sequential claims.
[Verification](VERIFICATION.md) distinguishes local completion from
publication CI.
