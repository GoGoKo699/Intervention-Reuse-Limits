# Randomized preparation checks and a conservative precision budget

The [observable preparation bound](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md)
can be combined with random assignment of the five experiment types.
Assignment occurs **after the common preparation** and is independent of
the prepared state. This balances even history-dependent preparation in
the predictable response averages. It does not require a conditional
hidden-state reset estimate.

This note proves that sampling statement and one explicit precision
budget: **60 billion trials** suffice to estimate eight corrected score
functionals simultaneously within $.001$, with probability above $96\%$.
This is a conservative scalar-precision guarantee, not a complete
five-type rejection or power theorem. It is not a lower bound on cost.
The existing five-million-trial test and its narrower preparation
promises remain unchanged.

[Source and scope audit](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md)
· [Readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md)
· [Exact verifier](../scripts/verify_switch_observable_calibration.py)
· [Certificate report](../reports/switch_observable_calibration.json).

## 1. Randomize the type after preparing the system

The five types are the original arms $A=0H$ and $B=H0$, their prefixed
versions $KA,KB$, and a low calibration pair $L$. The calibration low
wait lasts ten attempt-time units. Under the exact protected-instrument
contract, the effective low kernel is $K=D P_0(10)$: $D$ preserves the
readout sectors and the low stationary law, and its electronic error is
independent of its hidden-state action. The $L$ type records the initial
sign, applies $D$ and the low wait, then records the final sign. The
prefixed types apply the same $D$ silently and then the same low wait
before starting the usual initial/final experiment. The protection and
independence requirements are detailed in the observable preparation
note; they are assumptions, not consequences of the calibration data.

Let $\mathcal F_{t-1}$ be the history before trial $t$'s common
preparation, and let $\nu_t$ be its conditional prepared-state law.
The preparation may depend arbitrarily on this history. After that
preparation, choose a type $J_t$ with fixed probabilities $p_j>0$,
independently of the prepared state, history and subsequent experimental
randomness. There is no acceptance, postselection or type choice based
on the prepared state. For each type $j$, the conditional response
channel from that state to the recorded pair is the same fixed channel
$A_j$ on every trial. The hidden model, kernels, instrument and detector
probabilities therefore do not switch with the history. Detector noise
must satisfy the conditional independence contract, rather than merely
have the prescribed unconditional error marginals.

For any fixed bounded recorded-pair functions $f_j$, define

$$
 U_t=\frac{f_{J_t}(O_t)}{p_{J_t}},\qquad
 \bar\nu=\frac1N\sum_{t=1}^N\nu_t.
 \tag{1}
$$

Independent assignment after preparation gives

$$
 \mathbb E[U_t\mid\mathcal F_{t-1}]
   =\sum_j\nu_t A_j f_j,
 \qquad
 \frac1N\sum_t\mathbb E[U_t\mid\mathcal F_{t-1}]
   =\sum_j\bar\nu A_j f_j.
 \tag{2}
$$

Thus **the same averaged preparation** $\bar\nu$ occurs for every
response observable. It is a random probability law, not a claim of
identical trials. Any deterministic response-preparation lemma valid for
every preparation applies to $\bar\nu$ path by path. Concentration is
proved for the martingale differences in (2), without conditioning on
the final random value of $\bar\nu$.

The estimators divide by the known assignment probability and the fixed
total $N$. They do not divide by the random number of trials of a type.
No assertion that the separately selected empirical groups have exactly
the same hidden preparation is needed. Fixing group counts through
history-dependent assignment would require a different argument.

## 2. A response-specific score correction

Use the existing score functions

$$
 X_A=.4Y+.6IY-.3I,\qquad
 X_B=-.4Z-.48JZ+.3J.
 \tag{3}
$$

Let $F(x)$ be the sum of their conditional expectations starting from
prepared state $x$, using the fixed $A$ and $B$ channels. The initial-bit
terms cancel in $F$ pointwise. With detector contrasts $\alpha,\beta$,
its span is at most $3.76\beta$.

All quantities below refer to the same law $\bar\nu$ from (2). Write

$$
 T=\bar\nu F-.08,\qquad
 d=\bar\nu(K-I)F,\qquad
 i=\alpha\bar\nu S,\qquad j=\beta\bar\nu KS.
 \tag{4}
$$

The drift $d$ is the summed prefixed score minus the summed original
score. The low-pair initial and final means give $i$ and $j$. In
particular, the initial bits of $KA,KB$ are recorded after $K$ and do
not have the same preparation as the initial bits of $A,B,L$. Pooling
all five initial bits as an estimator of $i$ would be incorrect.

For the following coefficient choice assume the observable guard
$\max(C,D)\ge g:=.45$, the low-pair correlation is at most $.15$, and
the stationary readout imbalance has magnitude at most $V:=10^{-4}$.
These are statements about the predictable response laws in (2), not
automatically about noisy empirical quantities. The positive original
correlation implies $\alpha\beta\ge g$; hence the latent low relaxation
obeys $r=1-\bar\nu SKS\ge1-.15/.45=2/3$.

The observable preparation lemma then gives

$$
 |\bar\nu F-\pi F|
 \le a|d|+b|j|+c|i|+q,
 \tag{5}
$$

with the exact coefficients

$$
 \begin{split}
 a&=6\frac{1+V}{1-V}=\frac{20002}{3333},\\
 b&=\frac{47}{25}a=\frac{940094}{83325},\\
 c&=\frac{b+(94/25)/(1-V)}{g}
     =\frac{15041128}{449955},\\
 q&=\frac{(94/25)V}{1-V}=\frac{94}{249975}.
 \end{split}
 \tag{6}
$$

Numerically, these are approximately $6.0012$, $11.2823$, $33.4281$
and $.00037604$. The initial-balance coefficient is substantial even
though its recorded statistic is only one binary mean.

For $\sigma=(\sigma_d,\sigma_j,\sigma_i)\in\{-1,+1\}^3$, put

$$
 H_\sigma=T-a\sigma_d d-b\sigma_j j-c\sigma_i i.
 \tag{7}
$$

Their minimum is $T-a|d|-b|j|-c|i|$. Equation (5) implies
$\min_\sigma H_\sigma\le T_\pi+q$, where $T_\pi=\pi F-.08$.
If additional localization establishes the inherited ordinary stationary
score ceiling $T_\pi<.00007$, this becomes
$\min_\sigma H_\sigma<.00007+q$. That localization is a separate
requirement; (5) alone is not a global ordinary score ceiling.

## 3. A fixed assignment and a bounded estimator

The midpoints of the score ranges are $-.3$ and $+.3$. Define
$\widetilde X_A=X_A+.3$ and $\widetilde X_B=X_B-.3$, with ranges
$[-1,1]$ and $[-.88,.88]$. Their midpoint shifts cancel in each summed
original or prefixed response. For each sign triple, use these five
outcome functions:

| Type | Function $f_{j,\sigma}$ | Uniform range-width bound $w_j$ |
|---|---|---:|
| $A$ | $(1+a\sigma_d)\widetilde X_A$ | $2(1+a)$ |
| $B$ | $(1+a\sigma_d)\widetilde X_B$ | $(44/25)(1+a)$ |
| $KA$ | $-a\sigma_d\widetilde X_A$ | $2a$ |
| $KB$ | $-a\sigma_d\widetilde X_B$ | $(44/25)a$ |
| $L$ | $-b\sigma_j Y_L-c\sigma_i I_L$ | $2(b+c)$ |

Each function has absolute value at most $w_j/2$. Choose the same
assignment probabilities for all eight statistics,

$$
 p_j=\frac{w_j}{R},\qquad
 R=\sum_jw_j
   =\frac{311165662}{2249775}<139.
 \tag{8}
$$

The resulting single-trial variable
$U_{t,\sigma}=f_{J_t,\sigma}(O_t)/p_{J_t}$ always lies in
$[-R/2,R/2]$. By (2),

$$
 \widehat H_\sigma:=\frac1N\sum_t U_{t,\sigma}-.08,
 \qquad
 \frac1N\sum_t\mathbb E[U_{t,\sigma}\mid\mathcal F_{t-1}]-.08
 =H_\sigma(\bar\nu).
 \tag{9}
$$

The same realized trials estimate all eight statistics. There is no
eightfold multiplier in the number of acquired records.

## 4. An exact precision statement

For completeness, fix a history and let $\psi(\lambda)$ be the logarithm
of the conditional MGF of a centered variable in an interval of width
$R$. Its value and slope vanish at zero. Its second derivative is the
variance under exponential tilting of that conditional law. Tilting
does not change the interval, so this variance is at most $R^2/4$:
center at the interval midpoint and then minimize the second moment
over centers. Integrating twice gives
$\psi(\lambda)\le\lambda^2R^2/8$ for either sign of $\lambda$.
Iteration of this conditional MGF bound over the history and Chernoff
optimization therefore give, for either tail,

$$
 \Pr\{\widehat H_\sigma-H_\sigma(\bar\nu)\ge\delta\}
 \le\exp\!\left(-\frac{2N\delta^2}{R^2}\right),
 \tag{10}
$$

and the same inequality with the difference negated. A union over both
tails and all eight fixed sign triples proves

$$
 \Pr\left\{\max_\sigma
   |\widehat H_\sigma-H_\sigma(\bar\nu)|>\delta\right\}
 \le16\exp\!\left(-\frac{2N\delta^2}{R^2}\right).
 \tag{11}
$$

This union also handles the fact that the minimizing sign triple in
(7) can depend on the random averaged preparation. Selecting a fixed
worst sign in advance would be unjustified for arbitrary adaptive
preparation.

Take

$$
 N=60{,}000{,}000{,}000,\qquad \delta=\frac1{1000}.
 \tag{12}
$$

Then

$$
 2N\delta^2=120000>6\cdot139^2=115926>6R^2,
 \tag{13}
$$

so the failure probability in (11) is below $16e^{-6}<.04$.
The last inequality can be certified with the rational bound
$e^{-6}\le[\sum_{k=0}^{40}6^k/k!]^{-1}$. Thus all eight corrected
functionals have absolute error at most $.001$ with probability above
$96\%$, uniformly over the history-dependent preparations allowed in
Section 1. There is no Gaussian approximation or independent-trial
assumption in this statement.

This allocation contains 120 billion recorded binary values, two per
trial. Its number of trials is 12,000 times the earlier five-million
allocation. That ratio describes this sufficient precision construction;
it is not a necessary price of removing the preparation promise.
Improved variance bounds, pooling compatible records or different
allocations may reduce it.

## 5. What this does not yet certify

Equations (11)--(13) estimate the corrected scalar functionals. A full
five-type rejection and power theorem would additionally need:

- simultaneous confidence for the contrast and low-correlation guards;
- response calibration sufficient to place the stationary reference in
  the local witness box and control its tangent remainder;
- a target budget for the extra low waits and calibration comparisons,
  including all preparation and control errors;
- an explicit treatment of any approximate instrument and observed-law
  prediction allowance, with amplification through (5) charged afresh.

Those tasks have not been completed by this precision calculation. In
particular, neither the earlier five-million-trial guarantee nor its
additional ordinary approximation allowance $e=.0002$ transfers to this
changed experiment. The existing three-state construction fits the two
original snapshot tables; it is not asserted to fit the three added
types. This note makes no five-type three-versus-four state-count claim.
Manuscript drafting remains deferred.
