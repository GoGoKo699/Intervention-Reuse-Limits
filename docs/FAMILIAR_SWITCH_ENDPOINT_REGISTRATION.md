# Register the state at the two ends of the active word

A single finite measurement window at each endpoint can replace the
seven-read majorities and disagreement gates in the preparation-free
test. The required detector property is a known uniform conditional
probability of misclassifying the relevant endpoint, at most
$p_*=1/200000=5\times10^{-6}$. The errors may be asymmetric,
history-dependent, and correlated with measurement backaction.

The initial label refers to the hidden state **after** the entire initial
measurement operation, just before the active word begins. The final
label refers to the hidden state **before** the final measurement
operation, just after the active word ends. With these boundaries,
arbitrary initial measurement dynamics become part of the ordinary
rival's arbitrary preparation. Exact sector preservation and stationary
initial measurement are unnecessary for that null.

The same nine-million-trial cap, first-million quotas, and residual
cutoff $.004$ give size below $.015$ for the exact-force null and below
$.04$ for the relative-force class specified below. Target miss remains
below $.014$. There are **18 million integrating measurement windows and
binary decisions**. This is not a count of analog samples or a detector
feasibility demonstration.

[Four-word test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) ·
[Repeated-readout alternative](FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md) ·
[Relative-force bound](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md) ·
[Source audit](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_SOURCE_AUDIT.md) ·
[Exact verifier](../scripts/verify_switch_endpoint_registration.py) ·
[Certificate report](../reports/switch_endpoint_registration.json)

## 1. Define the measured endpoints at the active boundaries

Use the four active words $0,H,0H,H0$, with the same fixed active kernels
as in the preparation-free theorem. In trial $t$, let

$$
 I_t=S(X_t^{\rm in}),\qquad Y_t=S(X_t^{\rm out}),
 \tag{1}
$$

where $X_t^{\rm in}$ is the actual hidden state at the instant the active
word starts and $X_t^{\rm out}$ is its state at the instant that word
finishes. These signs are mathematical reference variables, not extra
readings. The initial acquisition produces a recorded label $\widehat I_t$
for $I_t$; the final acquisition produces $\widehat Y_t$ for $Y_t$.

The initial acquisition boundary includes its barrier release and any
dead time before the word starts. The final acquisition boundary begins
when the active word finishes, before barrier closure or integration.
Any sign changes in these intervening operations matter to endpoint
registration. Taking a label first and then silently allowing the state
to change before its specified active boundary would violate this
definition.

The null has at most three counted states, a deterministic binary map
$S$, and one fixed pair of active reversible kernels. Its preparation and
initial measurement operation may depend arbitrarily on the scheduled
word and the complete past. The initial operation may change $S$ and
need not preserve any stationary law. Conditional on the full joint past
and its actual postmeasurement state, the subsequent active evolution must use
the prescribed fixed kernels. A persistent detector or controller
variable that changes those kernels must be counted in the model state;
it cannot act as unmodeled external memory. There is no feedback from
the recorded label into the active control word.

Let $\mathcal F_{t-1}$ be an analysis filtration containing the complete
joint system/detector past before the present preparation, including
previous true endpoint signs, error indicators, model states, acquired
records, and relevant apparatus information. It does not reveal the
current randomized preparation or current word-start state. The detector
contract is

$$
 \begin{split}
 \Pr(\widehat I_t\ne I_t\mid\mathcal F_{t-1})&\le p_*,\\
 \Pr(\widehat Y_t\ne Y_t\mid\mathcal F_{t-1})&\le p_*.
 \end{split}
 \tag{2}
$$

These inequalities must hold at every trial almost surely. A sufficient
physical specification imposes the same error bounds conditional on all
information and the hidden state at the beginning of each acquisition;
the tower property then gives (2). The initial bound concerns the sign
at the end of that acquisition, so it is not a premise that its error is
independent of the postmeasurement state. The two stage errors may be
correlated with one another and with the active trajectory.

Equation (2) is a calibrated uniform upper bound. It requires neither
a fixed error probability, a symmetric binary channel, nor fresh
independent detector errors. An unconditional average error rate would
not supply it. The statistical test below does not estimate this bound
from its scored data.

## 2. The ordinary preparation and initial instrument disappear

If both readout sectors are nonempty, an at-most-three-state model has
a singleton sector $s$. Conditional on $I_t=s$, its actual word-starting
state is necessarily that singleton $x_s$. Thus its four true return
probabilities are

$$
 r_{0,s}=(P_0)_{x_sx_s},\quad
 r_{H,s}=(P_H)_{x_sx_s},\quad
 r_{0H,s}=(P_0P_H)_{x_sx_s},\quad
 r_{H0,s}=(P_HP_0)_{x_sx_s}.
 \tag{3}
$$

No premeasurement sign or initial-instrument property enters (3).
The previous theorem's sign-preserving initial operation was a
sufficient way to identify this same state using a pre-operation sign.
Registering the post-operation sign makes that restriction unnecessary.

For $u=3/5$, form the residual

$$
 R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}
                       +2su\,r_{0,s}r_{H,s}.
 \tag{4}
$$

The exact common Gibbs tilt and detailed balance imply $R_s=0$ by the
existing singleton identity. The
[relative-force lemma](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md)
instead allows a residual likelihood factor with maximum/minimum ratio
at most $1001/1000$. With its strictly positive stationary laws and
fixed reversible kernels, it gives

$$
 |R_s|\le\rho:=\frac1{2500}=.0004.
 \tag{5}
$$

No minimum stationary mass or rival preparation bound is needed for
either conclusion. The size proof below uses only $|R_s|\le\rho$ for
one fixed singleton sign; set $\rho=0$ for the exact-force class.

## 3. The acquisition and test

Cycle deterministically through the four words until

$$
 N=9{,}000{,}000,\qquad M=N/4=2{,}250{,}000
 \tag{6}
$$

trials have been performed, with $M$ trials per word. Each trial has one
initial and one final integrating acquisition. For each of the eight
word/recorded-initial-sign groups, retain its first
$n=1{,}000{,}000$ records. If any group is incomplete at the cap,
do not reject.

For a completed group, let $\widehat r_{w,s}$ be its frequency of
$\widehat Y_t=s$. Compute $\widehat R_s$ using (4). Reject only when
all groups complete and

$$
 \widehat R_->.004,\qquad \widehat R_+<-.004.
 \tag{7}
$$

There are no repeated-read majorities or disagreement gates in this
experiment. It uses the known bound (2) in their place.

## 4. Few endpoint errors imply stable fixed-size groups

For each word and stage, count label errors among that word's $M$
trials. Denote these counts by $E_{w,i}$ and $E_{w,f}$. From (2),
the conditional moment generating function of each increment is at most
$1+p_*(e^t-1)$. At $t=\log4$,

$$
 \Pr(E_{w,j}>50)
 \le4^{-50}(1+3p_*)^M
 \le4^{-50}e^{3Mp_*}
 <\frac{3^{34}}{4^{50}},
 \tag{8}
$$

because $3Mp_*=33.75<34$ and $e<3$. A union over the eight counts
gives

$$
 \epsilon_E:=8\frac{3^{34}}{4^{50}}
 =\frac{16677181699666569}
        {158456325028528675187087900672}
 <2\times10^{-13}.
 \tag{9}
$$

Counts may be correlated; neither their independence nor independence
of their error events from return outcomes is used.

Compare an observed word/sign group to the first $n$ records selected
by its true word-start sign $I_t=s$. If fewer than $n$ true records occur
at the cap, append artificial true records to complete it. For the null
singleton these have its fixed reference return probability. For the
target they have the corresponding fixed reference probability. This
is a proof on an enlarged probability space, not an instruction to
collect additional trials.

Changing $E_{w,i}$ initial labels changes at most that many members of
an ordered first-$n$ selection. Each replacement changes a binary
average by at most $1/n$. On common selected records, $E_{w,f}$
incorrect final labels change at most that many return indicators.
Hence, whenever the observed group completes,

$$
 |\widehat r_{w,s}-\widehat r^{\rm true,padded}_{w,s}|
 \le\frac{E_{w,i}+E_{w,f}}n.
 \tag{10}
$$

Outside the event of probability (9), this is at most $10^{-4}$.
Since the polynomial (4) is Lipschitz on $[0,1]^4$ with constant
$2+4u=22/5$ in the maximum norm, its displacement is at most

$$
 \Delta_R=\frac{22}{5}\,10^{-4}=.00044.
 \tag{11}
$$

This deterministic comparison is why error/backaction independence and
symmetric electronics are unnecessary. If a model has only one true
readout sign, on the same good event its other observed-sign group has
at most 50 records per word and cannot complete; it cannot reject.

## 5. Oracle concentration and null size

The concentration proof uses a filtration that reveals the current
true word-start sign to decide oracle retention. It does not separately
reveal the current initial acquisition transcript or its electronic
label before forming the conditional return mean. Integrate over that
acquisition and the active evolution as appropriate after conditioning
on the true sign. Reveal the current records with the completed trial;
all previous records remain in the past. This avoids conditioning a
hidden update on its correlated current detector error.

For the null singleton, (3) gives the same return mean for every oracle
retained record. For a target, Section 6 supplies a uniform conditional
displacement $b$ from its fixed reference. As in the existing stopped
proof, oracle selection is decided before the true final sign. Padded
records have their reference means. No argument conditions the data
distribution on quota completion.

Write $\Delta_w=\widehat r^{\rm true,padded}_{w,s}-r_{w,s}$ and

$$
 L_s=(1-su)\Delta_{0H}-(1+su)\Delta_{H0}
                 +2su(r_{H,s}\Delta_0+r_{0,s}\Delta_H).
$$

The exact expansion is

$$
 \widehat R_s^{\rm true,padded}-R_s
 =L_s+2su\Delta_0\Delta_H.
 \tag{12}
$$

The sum of squared linear coefficients is at most $28/5$, and the sum
of their absolute values is at most $22/5$. Conditional Hoeffding
therefore bounds either one-sided linear deviation beyond its
predictable drift by
$\exp[-2nh^2/(28/5)]$. With $\eta=.01$, the quadratic term is at
most $.00012$ except with probability $4e^{-2n(\eta-b)^2}$.

For a fixed null, choose its singleton sign before observing data.
Here $b=0$ and $|R_s|\le\rho$. Rejection and (11)--(12) require
a one-sided linear deviation with margin

$$
 h_N=.004-\rho-.00044-.00012.
 \tag{13}
$$

There is no union over possible singleton signs. For the exact-force
class, $h_N=.00344$, and

$$
 \Pr_{\rm null}(\mathrm{reject})
 \le e^{-3698/875}+4e^{-200}+\epsilon_E<.015.
 \tag{14}
$$

For the relative-force class (5), $h_N=.00304$, and

$$
 \Pr_{\rm null}(\mathrm{reject})
 \le e^{-2888/875}+4e^{-200}+\epsilon_E<.04<.05.
 \tag{15}
$$

The single-sign case described after (11) has size at most $\epsilon_E$.
Arbitrary rival preparation or initial measurement can prevent quotas
from completing, which only decreases rejection.

## 6. Target power uses a postmeasurement marginal promise

Fix one reference member of the balanced one-percent kinetic target
family. For each word and every pretrial history in this same analysis
filtration, require its actual
oracle pair $(I_t,Y_t)$ from (1) to be within

$$
 B=\frac{79}{10^6}
 \tag{16}
$$

in TV of that word's fixed reference pair. The reference has both
initial-sign probabilities equal to $1/2$ and residuals
$R_->.009$, $R_+<-.009$. Equation (16) is a target execution
promise, not a rival reset or preparation premise.

Let $D$ denote the actual entire initial acquisition channel after its
record is discarded, including all operations through the word-start
boundary. Here $\pi$ is the target's actual low-field stationary law,
before the separately budgeted comparison to the nominal reference.
If preparation obeys
$\operatorname{TV}(\nu,\pi)\le\epsilon_p$ and

$$
 \operatorname{TV}(\pi D,\pi)\le\delta_D,
$$

then

$$
 \operatorname{TV}(\nu D,\pi)\le\epsilon_p+\delta_D.
 \tag{17}
$$

The oracle initial sign is the deterministic sign of this actual
postmeasurement state. Thus (17), followed by active evolution, supplies
the preparation/initial-acquisition part of (16). A joint law of a
premeasurement label and postmeasurement state is not needed. Neither
sectorwise stationarity nor error/hidden-state independence is required
for this marginal argument. If $D$ depends on the history, (17) must
hold uniformly for the resulting channel at every history.
Selecting among individually stationary suboperations in response to
current measurement outcomes does not by itself establish this condition
for their complete history-conditional channel.

The inherited physical target budget remains sufficient: use
$\epsilon_p=\delta_D=10^{-5}$ and its existing field and timing
bounds. Its arithmetic is still

$$
 2\epsilon+
 \left[\frac12+\frac{101}{100}\left(\frac54+\epsilon\right)\right]
 \epsilon+\frac{101}{25}\epsilon
 =.000078025101<B,
 \qquad\epsilon=10^{-5}.
 \tag{18}
$$

The first two allowances now refer to preparation and the postmeasurement
marginal defect in (17). The label errors (2) are handled by Section 4
and are not added to the oracle budget (16). A fixed low-field generator
whose barriers are changed by symmetric edge factors while preserving
its stationary law gives $\delta_D=0$, even if rare sign changes occur.
Detector-induced energy changes or nonstationary backaction require
their own bound on $\delta_D$; accurate labels alone do not establish it.

For a concrete member of the finite one-percent kinetic target family,
hold the low-field energies fixed during initial acquisition and multiply
both directions of every $S$-changing edge by a fixed factor
$r\in(0,1]$. Other edge pairs may have their own fixed common factors.
Detailed balance remains valid edge by edge, so the complete
nonselective generator preserves $\pi$ exactly. Thus $\delta_D=0$
despite a positive probability of a sign-changing jump. Prescribed
time-dependent symmetric factors also preserve $\pi$; selection in
response to current outcomes is not inferred to do so.

With target attempt frequency $\Gamma$, the unscaled total
$S$-changing exit rate is at most $1.01\Gamma$. Under a factor $r$
throughout an acquisition of total duration $\tau$, the sufficient
leakage condition is $1.01r\Gamma\tau\le4\times10^{-6}$.
For a prescribed ramp $r(t)$ use
$1.01\Gamma\int_0^\tau r(t)\,dt\le4\times10^{-6}$ instead.
An integrating meter with independent additive Brownian noise and
bounded state-dependent offset is one joint physical realization of
this hidden dynamics and Section 7. The more general theorem permits
noise/backaction correlations. This is a mathematical target
construction with finite positive rates, not a hardware demonstration
or a rate cap derived for arbitrary ordinary rivals.

As in the ideal theorem, (16) bounds the conditional reference return
error of an oracle selected record by

$$
 b=\frac{B}{1/2-B}=\frac{79}{499921}.
 \tag{19}
$$

After accounting for this drift, (11), and the quadratic remainder,
the margin for either target residual is

$$
 h_T=.009-.004-\frac{22}{5}\frac{79}{499921}
                  -.00044-.00012
     =\frac{46801231}{12498025000}>0.
 \tag{20}
$$

The sum of the two signed-score miss bounds and remainder failures is

$$
 2e^{-2nh_T^2/(28/5)}+8e^{-2n(.01-b)^2},\qquad
 \frac{2nh_T^2}{28/5}
 =\frac{2190355223115361}{437361760921750}>5.008.
 \tag{21}
$$

Either actual initial sign has conditional probability at least $1/2-B$.
Misclassification can decrease either recorded-sign probability by at
most $p_*$, without any symmetry assumption. Therefore

$$
 q_T=\frac12-B-p_*=\frac{124979}{250000}=.499916
$$

is a lower bound for each target observed-sign probability. Conditional
Hoeffding and a union over eight groups give quota failure at most

$$
 \epsilon_Q\le8\exp\!\left[-\frac{2(Mq_T-n)^2}{M}\right],
 \qquad
 \frac{2(Mq_T-n)^2}{M}
 =\frac{15577785721}{1125000}>13846.
 \tag{22}
$$

Adding (9), (21), and (22) gives target miss below $.014<.05$.
There are no disagreement-gate failures to add. The same target proof
applies to both null force classes: broadening the null does not change
the acquisition or threshold.

## 7. A finite integrating detector that supplies the bound

The following is a sufficient physical noise model, not a certificate
for a particular sensor. Distinguish integration time $T$ from the full
boundary-acquisition span $\tau\ge T$, which also includes relevant
barrier closure, ring-up, release, and dead time. Within its integrating
part, let the centered output start at $Z_0=0$ and obey

$$
 dZ_t=(a_tS_t+b_t)\,dt+dM_t,
 \qquad a_t\ge a_{\min}>b_{\max}\ge|b_t|,
 \qquad g=a_{\min}-b_{\max}>0.
 \tag{23}
$$

Here $a_t,b_t$ may be predictable functions of the hidden state and
history. The residual offset $b_t$ permits asymmetric error rates.
$M_t$ is a continuous martingale in the **joint detector/system
filtration**, with $M_0=0$ and quadratic variation

$$
 \langle M\rangle_T\le vT,\qquad v>0
 \tag{24}
$$

almost surely, conditional on any history entering the integration. It may
be correlated with the system's backaction. Equation (24) is not a
claim of independent electronics or exact Gaussian noise. Continuity
matters: a variance bound for an arbitrary jump process would not by
itself yield the Gaussian exponential bound below.

Report $\operatorname{sign}(Z_T)$, breaking a possible tie in any fixed
way. Let $\Lambda$ uniformly bound, conditional on the full history
entering the acquisition, the probability of any transition that changes
$S$ anywhere in its full relevant span. A constant total sector-changing
rate bound $\kappa$ supplies $\Lambda\le\kappa\tau$ by the compensator
bound. With time-varying rates use their full-span integral. The term is
$\kappa T$ only if $\tau=T$ or if all other exposure has been separately
included in the leakage budget.

Let $s$ be the sign at the beginning of integration, measurable in that
mathematical initial filtration. On the event of no sector-changing
transition anywhere in the acquisition, the sign stays $s$ and agrees
with the sign at both boundaries of the full operation,
so

$$
 sZ_T\ge gT+sM_T.
$$

A label error relative to either full-operation boundary sign is contained
in the union of a sector-changing event and
$\{sM_T\le-gT\}$. The continuous exponential-martingale inequality,
optimized at parameter $g/v$, gives

$$
 \boxed{
 \Pr\{\operatorname{sign}(Z_T)\ne S^{\rm start}\mid\text{acquisition history}\},
 \quad
 \Pr\{\operatorname{sign}(Z_T)\ne S^{\rm end}\mid\text{acquisition history}\}
 \ \le\ \Lambda+\exp\!\left[-\frac{g^2T}{2v}\right].}
 \tag{25}
$$

The two expressions inside the box each obey the stated upper bound;
the conditioning is on history entering the acquisition, not its outcome.
In the tail argument, $s$ is fixed by the initial information and
$\exp[-\lambda sM_t-\lambda^2\langle M\rangle_t/2]$ is a
nonnegative supermartingale. Markov's inequality gives
$\exp[-\lambda gT+\lambda^2vT/2]$, minimized at $\lambda=g/v$.
This uniform bound conditional on the integration-start information also
holds conditional on the earlier acquisition-start history by the tower
property.

Crucially, this argument never conditions the noise distribution on no
sector transition. That conditioning could bias the detector noise when
it is correlated with backaction. The unconditional union bound proves
(25) even with that correlation.

For initial acquisition, use the bound against $S^{\rm end}$; for final
acquisition, use the bound against $S^{\rm start}$. This is precisely the
boundary registration in (1). There is no requirement to manufacture
a symmetric error channel by adding electronic noise.

Put $\theta=v/g^2$, with units of time. A simple sufficient choice is

$$
 T=32\theta,\qquad \Lambda\le4\times10^{-6}.
 \tag{26}
$$

Then (25) is at most
$4\times10^{-6}+e^{-16}<5\times10^{-6}=p_*$.
If $\tau=T$, the sufficient constant-rate condition is equivalently
$\kappa\theta\le1/8000000$. Longer acquisition spans must instead
satisfy $\kappa\tau\le4\times10^{-6}$. This is a demanding, explicit
leakage/signal-to-noise requirement, not evidence that a device meets it.
Longer integration reduces the noise term but increases the leakage
term; unlimited averaging is not a free remedy.

The familiar Gaussian model
$dZ_t=aS\,dt+\sigma\,dW_t$ under exact sector protection is a
special case. Its exact classification error is
$\Phi(-a\sqrt T/\sigma)$, with $v=\sigma^2$, while (25) supplies
a conservative bound. The theorem uses the broader conditional
martingale specification, so fixed error probabilities and temporal
independence of binary outcomes are unnecessary.

All control changes between an active boundary and the relevant
integration endpoint must be included in $\Lambda$. Barrier switching
and dead time outside the interval on which (23)--(24) apply consume
that same total leakage budget in (26).
Likewise, an unremoved initial integrator offset requires a reduced
signal margin or a separate error bound. Neither switching errors nor
integrator reset errors disappear by naming the window protected.

## 8. Resources and the comparison class

The known endpoint-error envelope (2) is a different detector premise
from the earlier unknown-fixed-error experiment. The earlier scheme
allowed raw error rates up to $1/2$ for rivals and used disagreement
gates within a freshness model. The present scheme permits asymmetry
and adaptive conditional errors but requires a trusted uniform small
error bound. Neither result automatically covers the other's entire
instrument class. The physical model (23)--(26) is one way to justify
the new envelope; the test's own scored data do not establish its
signal, noise, offset, or leakage bounds.

Nine million trials require 18 million integration windows and endpoint
binary decisions, including trials whose selected group is already
full. This is not a claim that the electronics acquire only 18 million
analog samples. For equal window duration $T$ seconds and target attempt
frequency $\Gamma$ per second, the inherited reset and active-word
exposure plus integration is

$$
 \frac{583875000}{\Gamma}+18{,}000{,}000\,T
 \quad\text{seconds},
 \tag{27}
$$

before other overhead. The first term includes nine million 63-unit
target resets and average active duration $15/8$ units per trial.
With (26), the readout contribution is $576{,}000{,}000\,\theta$.
Barrier switching, controller reset, dead time not included in $T$,
storage, and bandwidth remain additional resources; their endpoint
registration errors must already have been budgeted as specified above.
No finite reset-time premise is imposed on the ordinary null.

For the fixed ideal four-word population laws, the relative-force note
establishes state minima three versus four through maximum pair-table
TV tolerance $.0009$. Those population statements concern the specified
binary endpoint interface, not the analog current record. For a target
execution obeying (2) and (16), a coupling to the oracle pair gives

$$
 \operatorname{TV}\bigl(
   \mathcal L(\widehat I_t,\widehat Y_t\mid\mathcal F_{t-1}),
   P^*_{w_t}\bigr)
 \le B+2p_*=.000089.
 \tag{28}
$$

Thus the existing three-state general predictor of the ideal reference
also provides this per-trial pair approximation. This does not assert
an exact fit to arbitrary asymmetric detector errors or a three-state
realization of the full analog/transcript process, and it does not
identify state minima for the complete history-dependent serial law.

The new result makes the physical readout task precise: register the
state at the active boundaries with a uniform conditional error bound.
Ordinary preparation and arbitrary initial measurement dynamics are
absorbed into the state that actually starts the word. Target preparation,
its postmeasurement marginal control, fixed active dynamics, the stated
force relation, and the calibrated detector envelope remain substantive
premises. Device feasibility and PRL readiness remain unestablished;
manuscript drafting remains deferred.
