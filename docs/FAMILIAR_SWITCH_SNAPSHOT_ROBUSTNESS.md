# Two snapshots, two control orders, and a stable state-cost witness

Two opposite-order field protocols suffice for the familiar coupled-switch
target when each trial records the binary conformation initially and
finally. Both protocols start from the same low-field equilibrium. This
uses a richer observation than a single endpoint, while avoiding the
second equilibrium preparation used by the
[four-endpoint witness](FAMILIAR_SWITCH_PREPARATION_WITNESS.md).

The distinction is simple: ordinary reversibility turns the measured
quantities into a conditional covariance of two response propensities.
A readout sector consisting of one state has zero covariance. The
two-switch target has positive covariance in both sectors. Its four
physical states can nevertheless be replaced by three stationary
predictive states when ordinary detailed balance is not required.

**Status:** the analytic proof and exact rational numerical certificate
have passed independent internal review. The certificate supplies the
numerical premises below; the identities and arbitrary-rival implications
are analytic. These are internal checks, not external peer review.
No manuscript is being drafted.

[Underlying preparation witness](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) ·
[Source and scope background](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) ·
[Snapshot statistical test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) ·
[Exact verifier](../scripts/verify_switch_snapshot_design.py) ·
[Certificate report](../reports/switch_snapshot_design.json) ·
[Internal review](FAMILIAR_SWITCH_SNAPSHOT_INTERNAL_REVIEW.md)

## 1. Two joint laws and one shared preparation

The target consists of two time-even conformational variables
$S,Z\in\{-1,1\}$, with energy $-JSZ-hS$ and equal unit-attempt heat-bath
rates. The observed variable is $S$. Write $t=\tanh J$, $u=\tanh H$.
At the selected setting,

$$
 J=H=\log3,\qquad t=u=4/5,\qquad a_0=a_H=3/2.
 \tag{1}
$$

The two chronological protocols are $0,H$ and $H,0$, each with one
initial and one final binary observation. Their active duration is three
attempt-time units. Both use one fixed low-field preparation law.
Under ideal preparation this is $\pi_0$.

Let $E_0,E_H$ be the field-specific transition kernels. Define four moments
of the two joint laws:

$$
 \begin{array}{c|cc}
 \text{Protocol}&\mathbb E[S_{\rm final}]&
                    \mathbb E[S_{\rm initial}S_{\rm final}]\\\hline
 0,H&m&c\\
 H,0&\ell&d
 \end{array}
 \tag{2}
$$

A rival has one finite state space, a deterministic binary readout, and
shared kernels and preparation across the protocols. In the nominal
comparison its stationary laws satisfy

$$
 \pi_0S=0,\qquad \pi_H=\pi_0(1+uS).
 \tag{3}
$$

An ordinary rival obeys detailed balance at both fields. An unrestricted
rival need only have the specified stationary laws. The lower argument
allows arbitrary reversible stochastic kernels, including kernels that
are not continuous-time propagators. It has no rate cap or prescribed
rival graph. The Gibbs relation (3), deterministic readout, and shared
model remain substantive assumptions.

For two $2\times2$ joint tables, define the prediction error

$$
 \delta_{\rm joint}
 =\max_{w\in\{0H,H0\}}\operatorname{TV}(P_w,\widehat P_w),\qquad
 \operatorname{TV}(P,Q)=\frac12\sum_{s,r=\pm1}|P(s,r)-Q(s,r)|.
 \tag{4}
$$

When both models have balanced initial marginals, a table with final
mean $m$ and correlation $c$ has entries $(1+rm+src)/4$. Consequently

$$
 \delta_{\rm joint}
 =\frac12\max\{|\Delta m|,|\Delta c|,|\Delta\ell|,|\Delta d|\}.
 \tag{5}
$$

Without equal initial marginals, the right-hand moment discrepancies
are still bounded by $2\delta_{\rm joint}$, which suffices for the robust
bounds below.

## 2. The direct conditional-covariance identity

Set $F=E_HS$ and $G=E_0S$. Low-field stationarity and detailed balance give
$m=\pi_0F$ and $c=\langle G,F\rangle_0$.
Under exact tilt, the four means from the earlier two-preparation
experiment are recovered as

$$
 b=m+uc,\qquad a=\ell+ud.
 \tag{6}
$$

The second identity uses high-field stationarity; it is not valid without
that assumption. Substitution in the four-response identity gives

$$
 \boxed{\mathcal H_\sigma
 =uc-u(1+\sigma m)d+\sigma(u-m)\ell
 =-\frac{\sigma u^2}{1-\sigma u}
   \operatorname{Cov}_0(G,F\mid S=\sigma),\quad \sigma=\pm1.}
 \tag{7}
$$

A singleton readout sector forces one of the two expressions to vanish.
Every ordinary rival with at most three states therefore obeys
$\mathcal H_+=0$ or $\mathcal H_-=0$. This argument needs no generator
reconstruction, determinant, or limit of short dwell times.

For the physical target, put

$$
 B=\frac{t(1-u^2)}{1-t^2u^2},\quad \kappa=\sqrt{tB},\quad
 \gamma=e^{-a_H}\frac{B}{\kappa}\sinh(\kappa a_H),\quad
 d_0=e^{-a_0}\sinh(ta_0).
 \tag{8}
$$

The target responses have $F=m+\beta S+\gamma Z$ and
$G=c_0S+d_0Z$, with positive $\gamma,d_0$. Its conditional hidden variance
is $1-t^2$. Therefore

$$
 \mathcal H_-^*=\frac{u^2\gamma d_0(1-t^2)}{1+u}>0,\qquad
 \mathcal H_+^*=-\frac{u^2\gamma d_0(1-t^2)}{1-u}<0.
 \tag{9}
$$

This holds for every finite $J,H,a_0,a_H>0$. The physical obstruction is
the covariance of two conditional response propensities within each
visible conformation, not an additional measured state label.

## 3. A direct joint-TV margin

Let $a=\ell+ud$ at the target. Each of the four moment errors is at most
$r=2\delta_{\rm joint}$. Expanding (7) exactly gives

$$
 |\mathcal H_\sigma-\mathcal H_\sigma^*|
 \le L_\sigma r+(1+u)r^2,\qquad
 L_\sigma=a+3u-m+\sigma um.
 \tag{10}
$$

Here $0<m,a<u$, so $L_\sigma$ is the sum of the absolute first derivatives.
The only quadratic remainder is
$-\sigma\Delta m(\Delta\ell+u\Delta d)$.
The positive root of
$2L_\sigma\delta+4(1+u)\delta^2=|\mathcal H_\sigma^*|$
therefore gives an explicit all-parameter lower radius.

At (1), the approximate moments are

$$
 (m,c,\ell,d)\approx
 (0.4167564946067,\ 0.3454454071627,
  0.2299499923598,\ 0.3860194594377).
 \tag{11}
$$

The exact nominal certificate evaluates (10) on the full moment box
$r=23/6250$, with target-enclosure error included, and proves

$$
 \inf_{\substack{\text{ordinary rivals}\\\text{with at most three states}}}
 \max_w\operatorname{TV}(P_w^*,P_w)
 >\frac{23}{12500}=0.00184.
 \tag{12}
$$

The certificate uses exact rational heat-bath generators at $t=u=4/5$.
For $X=(3/2)Q$, it evaluates the matrix Taylor polynomial through degree
$96$. If $r_X=\|X\|_\infty<98$, the omitted tail is at most

$$
 \frac{r_X^{97}}{97!}\frac{1}{1-r_X/98}<2^{-180}.
$$

Each retained entry is rounded to the nearest $160$-bit dyadic number;
the resulting interval of radius $2^{-160}$ covers rounding and the
entire tail. Exact interval matrix multiplication propagates these
enclosures through both two-tick words and their signed joint moments.
The four reported $128$-bit centers enclose their true moments within
$2^{-120}$. Translating (7) about these centers and summing the absolute
nonconstant coefficients over radius $23/6250+2^{-120}$ leaves more than
$1/30000$ of polynomial slack for both signs. These rational interval
calculations supply the numerical premise of (12).

A fixed rational ordinary three-state comparator gives the accompanying
upper. Set $S=(-1,+1,+1)$ and

$$
 \widehat\pi_0=
 \left(\frac12,\frac{63012}{10^6},\frac{436988}{10^6}\right),
 \qquad
 \widehat\pi_H(i)=\widehat\pi_0(i)(1+\tfrac45 S_i).
$$

Its symmetric stationary fluxes are

| Field | Pair $(1,2)$ | Pair $(1,3)$ | Pair $(2,3)$ |
|---|---:|---:|---:|
| $0$ | $39732/10^6$ | $33330/10^6$ | $21481/10^6$ |
| $H$ | $22758/10^6$ | $23366/10^6$ | $209/10^6$ |

Define $\widehat Q_{ij}$ by dividing the pair flux by
$\widehat\pi_h(i)$, with diagonal entries chosen for zero row sums.
Both generators satisfy detailed balance and have maximum exit rate
below one. The same exact Taylor enclosure gives joint-TV upper bounds
$923961564867/(5\times10^{14})$ for $0H$ and
$924534044621/(5\times10^{14})$ for $H0$, each below
$37/20000=0.00185$. Therefore

$$
 \inf_{\substack{\text{ordinary rivals}\\\text{with at most three states}}}
 \max_w\operatorname{TV}(P_w^*,P_w)
 \in\left(\frac{23}{12500},\frac{37}{20000}\right).
$$

This upper is one feasible shared model, not a global optimizer or an
all-protocol approximation. The bracket endpoints differ by a factor
$185/184$.

The positive three-state construction from the
[structural theorem](FAMILIAR_SWITCH_STRUCTURE.md) matches the target's
initial/final joint laws exactly. Conditional on $S_{\rm initial}=\sigma$,
both models begin with coordinate means $(S,Z)=(\sigma,\sigma t)$.
These evolve by the same closed equations, and the initial sector masses
also agree. This proves equality of each two-time joint law, without
claiming equality of complete multitime trajectories.
The ordinary four-state target supplies the other upper, while every
two-state stationary model is ordinarily reversible. The nominal minima
are thus three and four for
$0\le\delta_{\rm joint}\le23/12500$.

## 4. Biased equilibrium and an approximate force law

Let the stationary low-field law be $\pi$, with $v=\pi S$. Write

$$
 z=1+uv,\qquad \lambda=\pi(1+uS)/z,\qquad
 \operatorname{TV}(\eta,\lambda)\le\theta,
 \tag{13}
$$

where the actual high-field kernel is reversible for $\eta$.
All four snapshot moments in this section use stationary low-field
preparation $\pi$. Set $q_\sigma=1+\sigma v$ and define

$$
 \boxed{\mathcal H_\sigma^{\,v}
 =q_\sigma[(1+\sigma u)\ell+uc]
  -(\ell+ud)(1+\sigma m)
  -v[um+\sigma(v+u-m)].}
 \tag{14}
$$

At $v=0$ this is (7). Under exact tilt it satisfies

$$
 u^2q_\sigma^2\operatorname{Cov}_\pi(G,F\mid S=\sigma)
 =-\sigma(1-\sigma u)\mathcal H_\sigma^{\,v}.
 \tag{15}
$$

For an approximate force law, every singleton sector instead obeys

$$
 \boxed{|\mathcal H_\sigma^{\,v}|
 \le\frac{12u q_\sigma z\,\theta+16z^2\theta^2}{1-\sigma u}.}
 \tag{16}
$$

The residual can be derived directly from the snapshot moments, without
introducing a second preparation. Let
$x=\langle SG\rangle_\pi$, $f=\langle SF\rangle_\pi$,
$h=\langle SFG\rangle_\pi$, and define the proxy moments

$$
 x_0=(\ell+ud-v)/u,\qquad
 f_0=(v+u-m)/u,\qquad h_0=(d+u\ell-c)/u.
 \tag{17}
$$

The three high-field defects

$$
 e_1=\lambda F-\lambda S,\quad
 e_2=\lambda E_HG-\lambda G,\quad
 e_3=\langle S,E_HG\rangle_\lambda-\langle F,G\rangle_\lambda
 \tag{18}
$$

have absolute value at most $4\theta$. They vanish under $\eta$ by
stationarity or detailed balance, and replacing $\eta$ by $\lambda$ in
the bounded expectations gives these bounds. Direct substitution yields

$$
 x=x_0-ze_2/u,\qquad f=f_0+ze_1/u,\qquad h=h_0-ze_3/u.
 \tag{19}
$$

The true cleared conditional covariance is
$u^2[q_\sigma(c+\sigma h)-(v+\sigma x)(m+\sigma f)]$.
Its two true conditional factors have absolute value at most $q_\sigma$.
Replacing $x,f$ costs at most
$8u q_\sigma z\theta+16z^2\theta^2$, and replacing $h$ costs at most
$4u q_\sigma z\theta$. The proxy expression is
$-\sigma(1-\sigma u)\mathcal H_\sigma^{\,v}$, proving (16) when
the sector is a singleton.

The robust certificate permits

$$
 |v|\le10^{-4},\quad |u-4/5|\le10^{-4},\quad \theta\le10^{-5}.
 \tag{20}
$$

It tests the joint-TV neighborhood of radius $g_0=9/5000=0.0018$ about
the nominal target through a six-variable polynomial box: the four
snapshot moments, $v$, and $u$. Each moment radius is
$9/2500+2^{-120}$, including the exact target-center enclosure; the
other radii are $10^{-4}$. Polynomial (14) has twelve terms and total
degree three. The exact sum of absolute translated nonconstant
coefficients times the coordinate radii bounds its full variation.
Subtracting both this variation and the worst-case residual (16) from
the target-center magnitude leaves more than $1/10000$ for either sign.
Thus every stationary ordinary rival with at most three states differs
from the nominal target by more than $g_0$ in at least one joint-law TV
distance. The identity is rate independent; observed balance alone does
not establish either the stationary-law defect or hidden-state preparation
in TV.

## 5. Preparation, controls, and the initial measurement

Preparation and measurement assumptions must hold for the target and
every admissible rival. Each model uses one fixed low preparation law
across the two protocols. If its distance from the stationary low law is
at most $\epsilon_p$, the entire initial/final joint law changes by at
most $\epsilon_p$: it is a stochastic image of that initial distribution.

An initial measurement can disturb the state. First define the ideal
initial bit $I=S(X_0)$ and retain it as a fixed label. The measurement
then applies a fixed disturbance kernel $D_x$ to the hidden state. Assume

$$
 \sup_x\operatorname{TV}(D_x,\delta_x)\le\xi.
 \tag{21}
$$

The kernels evolve this postmeasurement state to the final true bit $Y$.
Stochastic contraction bounds the change in the joint law of $(I,Y)$ by
$\xi$, independently of the subsequent dynamics. This is a uniform
disturbance calibration assumption. Electronic record noise is modeled
separately in Section 6 and is not counted twice in $\xi$.
A less structured fault model also gives an additive bound: initial
misclassification probability, disturbance probability, and final
misclassification probability sum to an upper bound by coupling. That
statement needs no independence, but can be wasteful for a calibrated
noisy detector.

The disturbance condition is sufficient and deliberately explicit.
An unchanged visible marginal does not establish it: a measurement may
change the hidden state or its correlation with the initial record.
A short measurement duration alone gives no uniform disturbance bound
for rivals with arbitrarily fast rates.

For target field and timing errors, use the signed row-TV generator norm
$\|\Delta Q\|_{\rm row,TV}=\frac12\max_x\sum_y|\Delta Q_{xy}|$.
Duhamel's identity bounds the joint-law displacement by initial TV plus
the integral of this norm. The initial recorded bit is simply carried
as a fixed label, so there is no extra dimension factor.

Take common actual plateaus within $\epsilon_h$ of $0,\log3$ and common
field-specific ticks within $\epsilon_t$ of $3/2$. The target equilibrium
shift costs at most $\epsilon_h/2$. The changed observed-spin flip rate
costs at most $\epsilon_h/2$ per unit time, and the active duration is
at most $3+2\epsilon_t$. Target exit rates are below two, so the two
duration errors cost at most $4\epsilon_t$. Thus, before detector noise,

$$
 b_T\le\epsilon_{p,T}+(2+\epsilon_t)\epsilon_h+4\epsilon_t,
 \qquad b_R\le\epsilon_{p,R}.
 \tag{22}
$$

Initial-instrument allowances $\xi_T,\xi_R$ are additional. If the
stationary robust witness has radius $g_0$, the true-record comparison
has gap greater than

$$
 g_0-b_T-b_R-\xi_T-\xi_R.
 \tag{23}
$$

The target's preparation wait can be bounded using its known mixing
rate. There is no finite wait that uniformly equilibrates every
arbitrarily slow rival. Waiting also does not establish independence
between trials or remove detector memory.
History-dependent reset errors can be analyzed as statistical bias under
additional conditional bounds, but do not by themselves supply the one
fixed preparation law used in the state-count statements.

The smaller three-state predictor matches the actual-field stationary
target joint laws, including the small negative low-field extension
already certified in the [calibration note](FAMILIAR_SWITCH_CALIBRATION.md).
The conditional initial coordinates remain $(\sigma,\sigma t)$ after
a field tilt. Using equilibrium preparation and the ideal initial
instrument, its error against an imperfectly prepared and disturbed
target is at most $\epsilon_{p,T}+\xi_T$. Arbitrary measurement backaction
does not inherit an exact three-state realization; it receives this
explicit error allowance.

## 6. A calibrated detector can have appreciable bit noise

Suppose the true pair $(I,Y)$ passes through fixed, known binary-symmetric
channels with flip probabilities $p_0,p_f<1/2$. These electronic flips
are independent conditional on the underlying pair, and independent
of its hidden dynamics and initial disturbance. There is no feedback from
the noisy initial bit to the subsequent state or protocol. The same two channels
are applied to the target and every competing model.
These are detector assumptions, not consequences of an equilibrium wait.

Let $C=B(p_0)\otimes B(p_f)$ act on the four-entry joint table, where
$B(p)$ is the binary-symmetric confusion matrix. Its inverse has induced
$\ell^1$ norm $[(1-2p_0)(1-2p_f)]^{-1}$. Therefore every pair of laws obeys

$$
 (1-2p_0)(1-2p_f)\operatorname{TV}(P,Q)
 \le\operatorname{TV}(PC,QC)
 \le\operatorname{TV}(P,Q).
 \tag{24}
$$

For $p_0=p_f=1/100$, the lower factor is $2401/2500=0.9604$.
Thus one-percent known bit-error rates need not be smaller than the
state-cost gap. They modestly attenuate it; they are different from
uncontrolled detector uncertainty or state disturbance.
Exact equality of the target and three-state predictor's joint laws
survives the common channel.

Combining (23)–(24), the observed gap exceeds

$$
 \frac{2401}{2500}
 (g_0-b_T-b_R-\xi_T-\xi_R).
 \tag{25}
$$

If the detector channels are only known within an error budget, their
uncertainty must also be included. For product binary-flip channels whose
two probabilities differ from the reference by at most
$\Delta_0,\Delta_f$, coupling gives a uniform channel-TV discrepancy at
most $\chi=\Delta_0+\Delta_f$. If different admissible hypotheses may
use different uncertain channels, subtract $\chi_T+\chi_R$ from (25).
Fixing the predictor to the nominal reference channel gives the
constructive three-state upper
$\epsilon_{p,T}+\xi_T+\chi_T$. This conservative choice avoids requiring
the predictor to know the target's exact detector probabilities.
The multiplicative bound alone does not justify freely refitting a
different detector under each hypothesis.

For a concrete simultaneous operating point, take the stationary-law
box (20), preparation TV errors $\epsilon_{p,T}=\epsilon_{p,R}=10^{-5}$,
field and tick errors $\epsilon_h=\epsilon_t=10^{-5}$, and disturbance
bounds $\xi_T=\xi_R=10^{-5}$. Then

$$
 b_T+b_R=\frac{800001}{10^{10}}=0.0000800001,\qquad
 g_0-b_T-b_R-\xi_T-\xi_R=0.0016999999.
 \tag{26}
$$

With the common known one-percent detector channels, (25) gives an
observed gap greater than $0.00163267990396$, hence greater than $0.0016$.
The smaller predictor has observed joint-TV error at most
$\epsilon_{p,T}+\xi_T=2\times10^{-5}$.

If each initial/final flip probability is instead permitted to differ
from $1/100$ by at most $10^{-5}$ under each hypothesis, the channel
allowance is $\chi_T+\chi_R\le4\times10^{-5}$. The observed gap remains
greater than $0.00159267990396$, hence greater than $0.0015$.
Fixing the smaller predictor to the reference detector channels gives
the conservative upper $4\times10^{-5}$.

These statements concern the recorded joint tables. Let $\delta_{\rm obs}$
be the maximum TV error of those two tables, after detector noise; it is
distinct from the underlying true-record metric (4). The kinetic state
counts are three versus four throughout

| Detector assumption | Range of recorded-table error $\delta_{\rm obs}$ |
|---|---|
| Common known $p_0=p_f=1/100$ | $2\times10^{-5}\le\delta_{\rm obs}\le0.0016$ |
| Each flip probability within $10^{-5}$ of $1/100$ | $4\times10^{-5}\le\delta_{\rm obs}\le0.0015$ |

The ordinary four-state physical model with stationary preparation,
no initial disturbance and the reference detector meets the same stated
upper allowance. Every two-state stationary kinetic model is ordinary,
so the lower also excludes unrestricted two-state competitors. The
memoryless detector is a specified shared resource; its parameters cannot
be replaced by unrestricted state-dependent emissions.

The deterministic budgets do not supply sample independence or empirical
estimates of their own calibration parameters. Their statistical use is
treated separately in the
[snapshot test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md).

## 7. Scope of the improvement

The main resource is two-time binary observation, not additional hidden
state labels. The two measured joint laws contain endpoint means and
initial/final correlations from opposite control orders. Ordinary
detailed balance links those quantities to a within-sector covariance;
the general three-state predictor reproduces the joint laws through
its closed mean coordinates.

One fixed preparation, two shared field kernels, and one fixed initial
instrument are required across the protocol family. State-dependent or
correlated occurrence-to-occurrence drift is not automatically covered.
The detector channel in Section 6 is a specified, shared postprocessing
mechanism. Complete trajectory equivalence, device-independent dimension
certification, and laboratory feasibility are not claimed.
