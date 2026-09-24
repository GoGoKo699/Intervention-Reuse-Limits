# Seven initial reads remove the need for error–kick independence

Repeat the protected initial measurement seven times and retain its
majority sign. At equilibrium, the joint error between that sign and the
postmeasurement hidden state is exactly the majority classification error,
even when every individual electronic error is correlated with its hidden
kick. A first-pair disagreement gate bounds the relevant raw error rate
without presupposing a one-percent detector for an ordinary rival.

This construction keeps the two active words and the existing five-million
trial score test. It changes the measurement resources: seven initial
physical reads replace one, and their first-pair disagreement is also
processed for calibration. The preparation promise remains necessary.
The result concerns the retained majority/final-bit laws; it does not
establish a three-state predictor or a memory separation for the full
eight-read transcript.

[Protected readout](FAMILIAR_SWITCH_PROTECTED_READOUT.md) ·
[Readout-calibration boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) ·
[Serial score test](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) ·
[Source audit](FAMILIAR_SWITCH_REPEATED_READOUT_SOURCE_AUDIT.md)

## 1. A fresh instrument may correlate its error with its update

Let a finite hidden space have deterministic readout
$S:X\to\{-1,+1\}$ and stationary preparation $\pi$. A single
initial read is a joint stochastic kernel

$$
 R(x;i,y),\qquad i\in\{-1,+1\},\qquad
 D(x,y)=\sum_i R(x;i,y).
 \tag{1}
$$

Use the same kernel for every initial read, in both arms and on every
trial. The exact construction assumes

$$
 \begin{split}
 R(x;i,y)&=0\quad\text{if }S(x)\ne S(y),\\
 \pi D&=\pi,\\
 \sum_y R(x;-S(x),y)&=p\quad\text{for every }x,
 \qquad 0\le p\le\tfrac12.
 \end{split}
 \tag{2}
$$

Successive uses are fresh applications of this kernel: conditional on
the entire preceding history and current hidden state, the next
outcome/update law is $R$. In particular, no unmodeled detector memory
changes that conditional law. The electronic error is permitted to be
arbitrarily correlated with the hidden update **during the same use**.
There is no factorization assumption of the form
$R(x;i,y)=B(i\mid S(x))D(x,y)$.

The first two conditions preserve the observed sector and the
nonselective stationary law. They need not hold conditional on the
electronic outcome. The third condition is a fixed binary symmetric
error rate conditional on the state before the read. Neither stationarity
nor this temporal freshness is certified solely by the disagreement
gate below.

Apply $m$ such reads, with $m$ odd. Write their signs as
$I_1,\ldots,I_m$, their majority as $M$, and their final hidden state as
$X_m$. There is no outcome-dependent choice of the number of reads,
their physical kernels, or the subsequent active word. The accumulation
of votes and disagreement occurs in external apparatus; its memory and
seven measurement durations are physical resources. That apparatus
does not subsequently feed its record or hidden state back into the
active evolution.

## 2. An exact joint-law identity

Define the ideal noiseless-label/state law

$$
 G_\pi(i,y)=\pi(y)\mathbf1\{i=S(y)\},
 \qquad
 b_m(p)=\sum_{k=(m+1)/2}^{m}{m\choose k}p^k(1-p)^{m-k}.
 \tag{3}
$$

**Repeated-readout theorem.** Under (2), at stationary preparation,

$$
 \boxed{\operatorname{TV}
   \bigl(\mathcal L_\pi(M,X_m),G_\pi\bigr)=b_m(p).}
 \tag{4}
$$

For arbitrary preparation with
$\operatorname{TV}(\nu,\pi)\le\epsilon_p$,

$$
 \operatorname{TV}
   \bigl(\mathcal L_\nu(M,X_m),G_\pi\bigr)
 \le\epsilon_p+b_m(p).
 \tag{5}
$$

The result holds for every finite hidden-state dimension; no relaxation
gap, rate cap, or conditional stationarity after a recorded outcome is
required.

### Proof

Sector preservation makes $S(X_j)=S(X_0)$ throughout the block. Set
$E_j=\mathbf1\{I_j\ne S(X_0)\}$. Conditional on the complete history
before read $j$, including its current hidden state, (2) gives
$\Pr(E_j=1\mid\text{history})=p$. Iterating conditional probabilities
shows that the $E_j$ have the product Bernoulli law. They can nevertheless
be correlated with $X_m$: an early error can affect its own hidden kick
and therefore the later trajectory. The majority is incorrect with
probability $b_m(p)$.

At stationary preparation the final hidden marginal is
$\pi D^m=\pi$. For a fixed $y$, let
$a_y=\Pr(M=-S(y),X_m=y)$. The actual joint law has mass $a_y$ in
the incorrect-label cell and $\pi(y)-a_y$ in the correct-label cell.
The ideal law has masses zero and $\pi(y)$ there. Consequently its
total-variation difference is $\sum_y a_y=b_m(p)$, proving (4).

The entire block, including its majority computation, is one stochastic
channel from the prepared state. Its outputs under $\nu$ and $\pi$
are within $\epsilon_p$ by contraction. Combining this with (4) proves
(5). Preparation is charged once, rather than once per read.

Any fixed future stochastic evolution and final observation contract
these bounds. For the existing witness, the final electronics must
still satisfy its fixed independent symmetric-channel premise.
Nothing here removes that final-readout assumption or permits feedback
from the majority into the active word.

## 3. Seven reads fit the existing joint-instrument allowance

The function $b_m(p)$ is increasing in $p$, for example by coupling
Bernoulli trials with common uniforms. Exact values are

| Reads $m$ | Raw error $p$ | Majority error $b_m(p)$ |
| --- | --- | --- |
| 5 | $1/100$ | $49253/5000000000=.0000098506$ |
| 7 | $1/100$ | $1708349/5000000000000=.0000003416698$ |
| 7 | $1/50$ | $26053/4882812500=.0000053356544$ |

Five reads barely fit the existing $10^{-5}$ instrument allowance
at a known one-percent error. Seven reads provide a useful gap between
the target's one-percent raw error and a two-percent null cutoff.
When $p\le1/50$,

$$
 b_7(p)\le .0000053356544<10^{-5},\qquad
 10^{-5}-b_7(1/50)=.0000046643456.
 \tag{6}
$$

The comparison reference uses **identity initial electronics**: all
majority misclassification is included in its joint-instrument TV error.
Identity initial electronics is an allowed member of both the old target
class $p_0\in[0,.01]$ and the old ordinary class
$p_0\in[0,1/2]$. This is a comparison to a noiseless stationary
reference. It is not a claim that the actual majority is an independent
binary symmetric channel acting on the hidden dynamics.

Thus (5) puts the retained majority/final-bit laws within the inherited
preparation plus instrument allowance whenever $p\le.02$. The other
field, timing, kinetic, stationary-tilt and final-detector premises remain
those of the existing test. No numerical threshold or score coefficient
changes.

## 4. A disagreement gate handles arbitrary ordinary raw error rates

One must not silently impose $p\le.02$ on every ordinary rival: the
inherited detector class allowed $p$ up to $1/2$. For each trial retain
or accumulate the diagnostic

$$
 V_t=\mathbf1\{I_{t,1}\ne I_{t,2}\},\qquad
 \widehat q={1\over N}\sum_{t=1}^N V_t.
 \tag{7}
$$

Because the sector is unchanged, $V_t=E_{t,1}\mathbin{\oplus}E_{t,2}$.
The fresh-kernel premise gives

$$
 \mathbb E[V_t\mid\mathcal F_{t-1}]=q(p):=2p(1-p),
 \tag{8}
$$

where $\mathcal F_{t-1}$ is the pre-reset past of the serial test.
Equation (8) holds for every prepared hidden-state distribution; no
preparation-TV correction is needed for this exact construction.
It also holds if previous trials have affected that distribution.

Use the same deterministic arm alternation and
$N=5{,}000{,}000$ trials, with $2{,}500{,}000$ per arm. Reject the
ordinary null only when the existing score threshold $.0021$ and all
its gates pass **and**

$$
 \widehat q\le .03.
 \tag{9}
$$

The bounded martingale Hoeffding inequality gives each one-sided
deviation of $\widehat q$ from $q(p)$ a bound
$\exp(-2Na^2)$ at distance $a>0$.

### Size

Split the null using its one fixed raw error rate $p$.

* If $p\le.02$, (6) embeds its retained pair laws in the old
  serial null class. Its old conditional preparation and stationary
  reference promises are still required. The additional gate can only
  reduce its false-rejection probability.
* If $.02<p\le1/2$, then $q(p)>.0392$. Regardless of its score,
  rejection requires the calibration gate to pass, with probability
  at most

$$
 \exp[-2N(.0392-.03)^2]=e^{-846.4}.
 \tag{10}
$$

These are alternative cases for a fixed model. Their size bounds are
combined by a maximum, not by a sum. The inherited size below $.05$
therefore remains valid. No conditional independence between the gate
and the score is needed.

### Power

For the target $p\le.01$, so $q(p)\le.0198$. Its extra gate fails
with probability at most

$$
 \exp[-2N(.03-.0198)^2]=e^{-1040.4}.
 \tag{11}
$$

The retained pair reference has identity initial electronics and the
same fixed final channel as the target. Its smaller majority error fits
the old instrument allowance. All remaining target execution and
history-conditional preparation promises are unchanged. The inherited
miss bound below $.044$, plus (11), is below $.05$. Power therefore
remains above $.95$.

The ordinary test's additional $.0002$ approximation allowance continues
to concern the retained majority/final-bit pair on each arm. The
calibration law (8) is a separate promise of the enlarged measurement
protocol. The proof does not grant an arbitrary $.0002$ perturbation of
the full raw transcript while still using the exact law (8).

## 5. Imperfect blocks and the remaining error margin

The exact construction uses only $b_7(.02)$ of the $10^{-5}$
instrument allowance. The remainder in (6) can cover a quantified
additional defect of the **whole** initial block. It is not a new
allowance on top of the previously budgeted $10^{-5}$.

For example, retain exact sector preservation and the fresh row-error
law, but permit different nonselective channels $D_1,\ldots,D_m$
with
$\delta_j=\operatorname{TV}(\pi D_j,\pi)$.
This sequence is fixed in advance: conditional on every earlier record
and history, the nonselective channel of read $j$ is the same $D_j$.
Contraction and telescoping give

$$
 \operatorname{TV}(\pi D_1\cdots D_m,\pi)
 \le\sum_{j=1}^m\delta_j.
 \tag{12}
$$

Comparison first to the ideal label of this actual final marginal gives

$$
 \operatorname{TV}\bigl(\mathcal L_\nu(M,X_m),G_\pi\bigr)
 \le\epsilon_p+b_m(p)+\sum_j\delta_j.
 \tag{13}
$$

Here (8) remains exact, because no sector changes and the raw errors
remain fresh with the same $p$. The sum in (13) concerns stationary
defects of the nonselective operations, not their worst-state movement.
They may move hidden states substantially while having $\delta_j=0$.

More generally, let the actual full-block instrument, including its
raw transcript and final hidden state, be within TV $\eta$ of the
ideal block when applied to $\pi$. Then the direct comparison is

$$
 \operatorname{TV}\bigl(\mathcal L_\nu(M,X_m),G_\pi\bigr)
 \le\epsilon_p+\eta+b_m(p).
 \tag{14}
$$

A coupling of the physical block to a protected reference can supply
part of $\eta$ through the probability of any sector-changing event;
other stationarity or emission defects must also be included. Repeating
a measurement repeats its opportunities for such failures. One cannot
reuse a single-read leakage budget seven times without accumulation.
Sufficiently small summed per-read comparison defects or a direct
whole-block bound can establish $\eta$.

For every trial, $\eta+b_7(.02)\le10^{-5}$ suffices for the old
retained-pair instrument allowance. It does **not** automatically retain
the exact disagreement law. If only the stationary full-block comparison
and $\operatorname{TV}(\nu,\pi)\le\epsilon_p$ are known, a safe
history-conditional calibration slack is
$\delta_{\rm cal}=\epsilon_p+\eta$:

$$
 \bigl|\mathbb E[V_t\mid\mathcal F_{t-1}]-q(p)\bigr|
 \le\delta_{\rm cal}.
 \tag{15}
$$

A uniform per-input-state full-block comparison by $\eta$ instead
gives $\delta_{\rm cal}=\eta$, since the ideal disagreement law is
preparation independent. With (15), replace (10) and (11) by

$$
 e^{-2N(.0092-\delta_{\rm cal})^2},\qquad
 e^{-2N(.0102-\delta_{\rm cal})^2},
 \tag{16}
$$

respectively, provided both gaps are positive. Under the existing
$\epsilon_p\le10^{-5}$ and the remaining margin in (6),
$\delta_{\rm cal}<.00002$, so these extra tail probabilities remain
negligible for the old size and power bounds. Approximation of the
retained pair alone does not establish (15).

## 6. Scope and a failure mode

The construction replaces independence of an electronic error from its
own hidden kick by a repeated-read requirement that is easier to state
operationally: each read has the same error probability conditional on
all earlier information, and the nonselective protected operation
preserves equilibrium. These remain physical instrument assumptions.
The disagreement gate bounds $p$ **within this model**; it does not
establish the model from data.

For example, a single unobserved error reused on all seven reads gives
zero first-pair disagreement while leaving the majority as unreliable
as one read. That common-mode detector fault violates temporal
freshness and is not covered by the theorem. Likewise, an error rate
depending on the hidden input state need not obey either the binomial
majority law or the calibration relation (8).

The construction directly handles the three-state boundary instrument
whose fresh Bernoulli error selects its hidden kick: its nonselective
channel is stationary, so (4) applies despite its failure of individual
error–kick independence. This is an example within the theorem,
not evidence that a particular charge sensor implements all its
premises.

The experiment now makes **40 million physical binary reads**:
seven initial and one final read per trial. The old score uses ten
million retained majority/final bits, with one disagreement diagnostic
per trial additionally accumulated for (9). The raw votes need not all
be stored, but their acquisition, controller memory, measurement time,
barrier control, and reset remain resources. No additional active
word or five-type preparation-calibration experiment is introduced.

The inherited three-state predictive construction concerns the two
retained pair laws of its stationary references. It does not prove a
three-state realization for all seven raw initial records and their
correlation with the final output. Such a stronger data interface would
require a separate upper construction and comparison. The current
result is an instrument and calibration theorem supporting the same
two-word score test, conditional on the stated preparation and physical
promises. Device feasibility and PRL readiness remain unestablished;
manuscript drafting remains deferred.
