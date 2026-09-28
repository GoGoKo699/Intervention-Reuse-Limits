# Measurement cost and physical robustness of the five-setting switching test

[Repository](../README.md) · [Frozen calibration theorem](FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md) · [Verification](VERIFICATION.md)

The five-setting two-spin theorem now has explicit finite-sample tests,
a separate information lower bound, and a uniform physical-parameter
neighborhood. These quantities answer different questions. A fixed ideal
experiment needs at least **136,981 paired trials** to achieve both error
probabilities at most 5% against one explicit rival. A test valid against
the whole ordinary three-state class is certified with **100 million**
ideal paired trials. The wide gap is unresolved; neither number is an
estimate of the optimal acquisition cost.

The population state counts remain exactly three general versus four
ordinary reversible states through 50 ppm throughout a common 1%
parameter box. That family result uses each target's actual Gibbs tilt.
It is not a uniform power guarantee for the nominal statistical test.
A separate **600-million-trial** confidence-set test profiles the tilt
from data and is valid against all unknown tilts in $(-1,1)$; its power
is certified at the nominal target. These are internally reviewed
mathematical guarantees, not evidence of device feasibility or external
validation. Manuscript drafting remains deferred.

All five settings are $L,L^2,H,H^2,HL$, with $HL$ chronological. A pair
trial measures the initial and final signs. The protocol is assigned before
observing the current trial's initial sign. The comparison retains a
single preparation, deterministic latent binary readout, a common Gibbs
force interface and one reused kernel per field. Rates of ordinary rivals
remain uncapped. All persistent predictive states are counted.

## Result and sampling assumption

The physical target is the two-spin heat-bath chain with `t=1/3`, field tilts `m_L=0,m_H=7/9`, tick `tau=1`, common zero-field equilibrium preparation, and binary endpoint readout. Use words `(L,LL,H,HH,HL)`.

Take N **independent reset trials per word**, with all five groups independent. One trial supplies both endpoint signs `(A,B)=(S_0,S_T)`. Every row below controls type-I error against **all** ordinary reversible predictors with at most three states and the specified common-preparation/Gibbs/readout interface; no exact calibration assumption is imposed on that null.

| Observation model | N per word | Total reset trials | Type-I upper bound | Type-II upper bound |
| --- | ---: | ---: | ---: | ---: |
| Ideal recorded pair laws | 20,000,000 | 100,000,000 | <0.028323 | <0.041616 |
| Each recorded law within TV 0.00001 of one fixed nominal family | 25,000,000 | 125,000,000 | <0.019093 | <0.023077 |
| Known independent 1% flips at each endpoint, plus TV 0.00001 residual from that recorded nominal family | 30,000,000 | 150,000,000 | <0.013775 | <0.015575 |

The robust null requires one fixed nominal ordinary model for all five words. The robust alternative requires one fixed nominal physical target. The per-word TV promise applies to the full recorded pair law, and the actual law is fixed within each word group. The final row's nominal recorded law is the known binary symmetric channel applied independently to both endpoints of the nominal pair. The residual TV budget can cover deviations before or after that channel, because it is stated directly on the resulting recorded law.

Repeated observations of one continuously evolving device are not assumed independent. A reset/mixing protocol or a separate conditional-law martingale argument would be needed to apply these counts to a serial device.

## Six moments and an exact null polynomial

Let `e=E A`, common across words under a nominal model, and write

$$
(x,y,z,v,r)=(C_L,C_{LL},C_H,C_{HH},C_{HL}),\qquad C_w=E[AB\mid w].
$$

Put `m=7/9` and

$$
\begin{aligned}
g&=1-e^2,&w&=1+me,&q&=e+m,\\
A_0&=g(y-e^2)-(x-e^2)^2,\\
B_0&=g(wv-eq)-(wz-eq)^2,\\
C_0&=g(r-e^2)-(x-e^2)(z-e^2).
\end{aligned}
$$

For `s=+1,-1`, define

$$
F_s(e,x,y,z,v,r)=(1-sm)wC_0^2-A_0B_0.
$$

Every ordinary null with at most three states satisfies `F_s=0` for at least one s.

To see this, subtract the conditional sign-sector mean from `K_LS` and `K_HS`. With at most three supported states, both residual functions live in a common space of dimension at most one, supported on one sign sector s. Pure-word reversibility gives their squared norms

$$
V_L=A_0/g,\qquad V_H=(1-m^2)B_0/(gw),
$$

while detailed balance gives the weighted residual cross moment `(1-m²) C_0/g`. The rank-one squared cross-product identity is

$$
(1-m^2)^2(C_0/g)^2=(1+sm)V_LV_H,
$$

which reduces to `F_s=0`.

Stationarity is used to eliminate final-sign means:

$$
M_L=M_{LL}=e,\quad M_H=e+m-mz,\quad M_{HH}=e+m-mv,
$$

and `M_HL=e+mx-mr`. These are consequences of a nominal ordinary model's interface, not assumptions imposed on empirical frequencies. Unequal initial sign masses and arbitrary doubleton masses are allowed. Zero-mass states are unreachable on the common Gibbs support. Degenerate one-sign models lie outside the small target neighborhood used below, so the proof need not divide by g there.

At balanced preparation the polynomial simplifies to

$$
F_s=(1-sm)(r-xz)^2-(y-x^2)(v-z^2).
$$

## A completely fixed statistic

Use this rational center, in order `(e,x,y,z,v,r)`:

```
(0,
 0.430143792060304,
 0.198892575818085,
 0.394017500089984,
 0.161414604733478,
 0.184195393007189)
```

Call it theta_c. Exact rational Taylor bounds enclose every ideal target moment within `10^-12` of its coordinate in theta_c.

For each s, compute the rational gradient `h_s=gradient F_s(theta_c)` and define

$$
W_s=F_s(\theta_c)+h_s\cdot(\widehat\theta-\theta_c).
$$

No data-dependent fitting or tuning is used. Approximate gradient values, included for inspection rather than as the definition, are:

| s | e | x | y | z | v | r |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| +1 | .003932022195 | .002727302257 | -.006164814356 | .008116757752 | -.013868893970 | .006538316169 |
| -1 | .004193863363 | -.015306174685 | -.006164814356 | -.011570155023 | -.013868893970 | .052306529352 |

For ideal readout, estimate each C by averaging AB within its word group. Estimate e by averaging all `5N` initial signs, so the initial-sign observations are reused but their dependence on AB is retained in the analysis.

Reject the entire ordinary-three-state null **only if all three conditions hold**:

1. Every coordinate of `hat_theta` lies within `0.0008` of theta_c.
2. `W_(+1) < -0.0000251`.
3. `W_(-1) > 0.0001624`.

Failure to reject is not evidence that a three-state null fits.

## Rigorous local geometry

On the box `||theta-theta_c||_infinity <= R=0.0016`, exact interval evaluation of the polynomial Hessians gives

$$
\sum_{i,j}|\partial_i\partial_jF_+|<10,
\qquad
\sum_{i,j}|\partial_i\partial_jF_-|<20.
$$

(The directly certified tighter sums are below 9.281 and 17.902.) Taylor's theorem therefore gives remainder bounds

$$
B_+=5R^2=0.0000128,\qquad B_-=10R^2=0.0000256.
$$

Also,

$$
F_+(\theta_c)<-0.0000374,\qquad F_-(\theta_c)>0.0002992.
$$

Under a nominal null inside the population box, one polynomial vanishes, so its corresponding population tangent score has absolute value at most B_s. Thus the rejection threshold is separated from that null score by at least

$$
\eta_+=0.0000123,\qquad\eta_-=0.0001368.
$$

At the ideal target the same margins apply, up to the certified `10^-12` center error times `||h_s||_1`. These L1 gradient norms are below `0.041349` and `0.103411`.

If a nominal null is outside the population box, the empirical gate requires at least one fixed moment coordinate to deviate by `0.0008` or more from that nominal mean. This inside/outside split is essential: a tangent is not used as a globally separating linear witness.

## Bernstein bounds with the initial signs reused

Let h_0 be the initial-mean coefficient and h_j the correlation coefficient for word j. For each trial of word j define

$$
Z_{j,i}=h_j A_{j,i}B_{j,i}+(h_0/5)A_{j,i}.
$$

The random part of W_s is `(1/N) sum_(j,i) Z_(j,i)`. Therefore valid global bounds, with no moment or covariance approximation, are

$$
V_s=\sum_{j=1}^5(|h_j|+|h_0|/5)^2,
\qquad b_s=2\max_j(|h_j|+|h_0|/5).
$$

The total variance is at most `N V_s`, and each centered summand is bounded by b_s. The certificate uses the simple envelopes

| s | V upper | b upper |
| --- | ---: | ---: |
| +1 | 0.00041 | 0.03 |
| -1 | 0.00351 | 0.107 |

Bernstein gives, for either one-sided deviation a,

$$
\Pr(W_s-EW_s\ge a)\le
\exp\left[-\frac{Na^2}{2(V_s+b_sa/3)}\right],
$$

with the analogous lower-tail statement. The same formula applies to independent but differently distributed word groups.

Hoeffding gives the target gate-failure bound

$$
G_N(d)\le10e^{-Nd^2/2}+2e^{-5Nd^2/2},
$$

where `d=0.0008-10^-12` in the ideal row. For a nominal null outside the population box, one fixed coordinate suffices, giving the smaller bound `2exp(-N d^2/2)`.

For the ideal row, N=20,000,000 yields score tails at most `0.024999654` and `7.54e-24`; target gate failure is at most `0.016615573`. Their union is below `0.041616`. Adding the outside-null gate bound to the larger score tail, conservatively, gives type-I error below `0.028323`. The two null cases are mutually exclusive, so this last sum is deliberately conservative.

## Systematic TV allowance

Suppose each recorded pair law is within TV b of its designated nominal law. Every bounded sign moment changes by at most `2b`. The score mean changes by at most

$$
2b\|h_s\|_1.
$$

Use effective Bernstein margins

$$
a_s=\eta_s-2b\|h_s\|_1-10^{-12}\|h_s\|_1,
$$

and gate distance `d=0.0008-2b-10^-12`. Applying the same concentration bounds with `b=10^-5,N=25,000,000` produces the second row. This allowance is stated against one fixed nominal family; choosing a new reference separately after observing each trial is not covered.

## Known independent endpoint-flip channel

Let each endpoint be flipped independently with known probability p=0.01 and let `kappa=1-2p=49/50`. For observed signs `(A',B')`, replace the two per-trial values by

$$
Y=A'/\kappa,\qquad X=A'B'/\kappa^2.
$$

These are unbiased estimators of the latent initial sign and endpoint product under the known channel. The test's center, polynomials, gradients, gates, and score thresholds are unchanged. The lookup values now have larger bounded ranges; this is explicitly included, rather than approximating readout noise by a TV budget.

The safe score constants become

$$
V_s^{(\kappa)}=\sum_j\left(|h_j|/\kappa^2+|h_0|/(5\kappa)\right)^2,
$$

$$
b_s^{(\kappa)}=2\max_j\left(|h_j|/\kappa^2+|h_0|/(5\kappa)\right).
$$

The certificate uses envelopes `V_+<1/2200`, `V_-<1/250`, `b_+<0.032`, `b_-<0.12`.

If the final recorded pair law also has TV residual b relative to the known-channel nominal law, the score bias is bounded by

$$
2b\left(|h_0|/\kappa+\sum_j|h_j|/\kappa^2\right).
$$

Every corrected moment bias is at most `2b/kappa^2`. Set `d=0.0008-2b/kappa^2-10^-12`. The target gate bound is

$$
10e^{-Nd^2\kappa^4/2}+2e^{-5Nd^2\kappa^2/2}.
$$

Use the analogous outside-null bound `2exp(-N d^2 kappa^4/2)`. With N=30,000,000 and b=10^-5, the positive score tail is below `0.013325104`, the negative score tail below `3.26e-30`, and the target gate tail below `0.002249253`. This proves the final table row.

The known p is part of the row's assumptions. Uncertainty or dependence in the detector channel must be included in a proved residual-law bound or handled by a separate calibration analysis.


## Inferring the Gibbs tilt rather than fixing its numerical value

The score rows above register exactly $m=7/9$ in the reference null. A
physical target field-error bound does not make those rows valid against
every ordinary rival with a different tilt. Stationarity instead supplies
an observable way to profile that nuisance parameter:

$$
M_H+mC_H=e+m,\qquad m=\frac{M_H-e}{1-C_H}.
$$

For an unknown relative tilt, also record the final-sign mean $M_H$ in the
$H$ group. Construct simultaneous confidence intervals for the six previous
statistics and this seventh statistic. Use radius $1/3200$ for each of the
five correlations and $M_H$, and $1/7000$ for the pooled initial mean.
Clip expectation intervals to $[-1,1]$. When $1-C_H$ has a strictly positive
interval lower bound, enclose the ratio above. The implemented test requires
that interval to lie strictly inside $(-1,1)$; otherwise it conservatively
returns inconclusive. It also returns inconclusive if the initial-mean
interval touches either endpoint $-1$ or $1$. No numerical external field
calibration is used.

With this tilt interval, evaluate $g,w,q,A_0,B_0,C_0$ from the preceding
polynomial definitions by outward rational interval arithmetic. Intersect
$A_0,B_0$ with $[0,\infty)$. If all required denominators are positive,
compare the interval for $C_0$ with the four intervals

$$
\eta\sqrt{\frac{A_0B_0}{(1-sm)w}},\qquad s,\eta\in\{-1,+1\}.
$$

Reject only if all four intervals are disjoint from the $C_0$ interval.
Infeasible nonnegative variances also exclude the null. Cases without a
certified positive denominator remain inconclusive. The method encloses
all feasible parameters rather than substituting an estimated tilt into
a point equality. Dependence of statistics from the same trial is allowed.

For **120 million independent trials per setting, 600 million total**,
Hoeffding and a seven-statistic union bound give failure below
$0.039943$. For a null, simultaneous coverage retains its true tilt and
its true polynomial branch, proving type-I control uniformly over all
$m\in(-1,1)$. For the nominal target, simultaneous coverage places every
confidence interval inside the target-centered box with twice the stated
radii. Exact interval evaluation over that larger box gives a profiled
tilt contained in $[0.775475,0.780086]$ and minimum branch separation
above $0.000180$. Thus type-II error is also below $0.039943$.

A simpler known-$m$ confidence-set version uses only six statistics and
**115 million per setting, 575 million total**. Its failure probability
is below $0.043704$ and its doubled-box branch margin exceeds $0.000265$.
The tangent-score test is substantially cheaper when its numerical-tilt
contract is appropriate. Neither confidence-set row includes unknown
instrument bias, a serial-reset theorem, or power uniformly over the 1%
physical family. The shared Gibbs form remains a physical assumption even
when its numerical tilt is inferred.

For a bounded sign statistic, the inequality used here is
$\Pr(|\widehat\mu-\mu|>h)\le2\exp(-nh^2/2)$. The certificates bound
these exponentials by positive rational Taylor sums. No Gaussian
approximation or independence between statistics from one pair is used.

## A necessary acquisition budget

Take the explicit reversible three-state comparator in
[the frozen theorem, Section 2](FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md).
It matches the four pure-setting pair laws exactly, so

$$
D(P_w\Vert Q_w)=0\quad (w=L,L^2,H,H^2).
$$

Rational matrix Taylor bounds and a rational logarithm series enclose
the remaining categorical relative entropy as

$$
D(P_{HL}\Vert Q_{HL})\in
[0.0000193457427238,0.0000193457427239].
$$

Let $E$ be the decision to reject the ordinary three-state null. Any test
with target power at least $0.95$ and false rejection at most $0.05$
satisfies the adaptive change-of-measure bound

$$
\sum_w\mathbb E_P N_w D(P_w\Vert Q_w)
\ge \operatorname{kl}(P(E),Q(E))
\ge 0.9\log19.
$$

Consequently $\mathbb E_P N_{HL}>136980.7879$. A deterministic total budget
therefore needs at least **136,981 pair trials**, or **273,962 endpoint
bit readouts**. This includes adaptive protocol selection based on
completed past trials and almost-surely finite stopping under fixed
independent-reset arm laws. The current protocol must be chosen before
seeing its initial sign. Initial-sign-conditioned protocol selection,
richer trajectories and different menus are outside this bound.

The lower bound uses one comparator, so it does not establish the
minimax acquisition cost of the composite-null problem. The four pure
settings have zero information against this particular rival even with
unlimited data. Exact calibration in this lower-bound construction is
not an assumption imposed on the null of the sufficient tests.

With a known independent 1% binary symmetric channel at both endpoints,
the same calculation gives a necessary fixed budget of **146,312 pairs**.
This concerns testing data under the known channel; acquiring the
calibration that justifies treating that channel as known is additional.

## Uniform common four-parameter box (actual relative tilt known)

Let

$$
t\in[33/100,101/300],\quad m\in[77/100,707/900],\quad
\tau_L,\tau_H\in[99/100,101/100].
$$

Both attempt rates remain one, the low physical field is zero, and each
field-specific clock is reused across the five settings. Each rival is
compared using the **same actual relative Gibbs tilt m** as its target.
This is a population family result, not a uniform power guarantee for an
unmodified nominal score or a certificate allowing a different fitted m.

Write `gamma=1-t²` and, at each field,

$$
B=t(1-m^2)/(1-t^2m^2),\quad q=tB,\quad
b=e^{-\tau}[\cosh(\tau\sqrt q)+\sqrt q\sinh(\tau\sqrt q)],
\qquad c=B e^{-\tau}\frac{\sinh(\tau\sqrt q)}{\sqrt q}.
$$

The target first-tick function is `g=a+b S+c U`, with
`a=m(1-b)`, `U=Z-tS`, zero conditional means of U, and its weighted
variance `gamma`. Thus

$$
V_L^*=\gamma c_L^2,\quad V_H^*=\gamma c_H^2,\quad
W^*-A^*=R=\gamma c_Lc_H,
$$

where `W=C_HL+m M_HL`,
`A=sum_s(1+ms) z_Hs z_Ls/p_s`, and nominal `p_s=1/2`.
These linked expressions retain the common-parameter dependence.

Suppose every rival pair law is within TV `d=1/20000` of its target.
Then `p_s>=p=1/2-d`, `|delta z_js|<=2d`, and
`|delta(C_jj+m_j M_jj)|<=2(1+m_j)d`.
Let `zL` bound both `|z_Ls^*|`, and `zp,zm` bound the positive target
values `z_H+^*,z_H-^*`; the certificate verifies positivity of the latter.
Put `wp=1+m_max`, `wm=1-m_min`. Algebraic expansion gives

$$
\begin{aligned}
e_L&=2d+\frac{2d}{p}(4z_L+2z_L^2+4d),\\
e_H&=2(1+m_{\max})d+\frac d p
\sum_{s=\pm}w_s(4z_s+2z_s^2+4d),\\
e_A&=\frac d p\sum_{s=\pm}w_s[2(z_s+z_L+z_sz_L)+4d],\\
e_W&=2(1+m_{\max})d.
\end{aligned}
$$

These bound changes of `V_L,V_H,A,W` respectively. For example the
conditional-product bound follows by expanding
`(z_H+dz_H)(z_L+dz_L)/(1/2+dp)-2z_Hz_L` before taking absolute values.

Let `vL,vH,Rlo` be uniform positive lower bounds for
`gamma c_L²,gamma c_H²,gamma c_Lc_H`. The closest positive-orientation
branches are excluded if

$$
R_{\rm lo}\left[\sqrt{(1+m_{\min})(1-e_H/v_H)(1-e_L/v_L)}-1\right]
>e_A+e_W,
$$

and

$$
R_{\rm lo}\left[1-\sqrt{(1-m_{\min})(1+e_H/v_H)(1+e_L/v_L)}\right]
>e_A+e_W.
$$

Negative orientations are excluded by `Rlo>e_A+e_W`. The exact
rational certificate establishes margins above `.000228`, `.001946`,
and zero, respectively, over the entire box. No grid is used.

For the general two-state lower, the target passive Markov defect in
the `++` cell is `gamma*c_L²/4`. A two-state predictor's propagation
error is at most

$$
e_2=d+\frac d p\left[1+\frac{1+b_{L,\max}^2}{4}+2d\right].
$$

The uniform remaining gap exceeds `.003071`. The inherited positive
three-state all-word construction applies throughout `0<t<1,m>=0`,
and the physical four-state process is reversible. Hence the common box
has the same population state counts three and four through 50 ppm.

## Null validity and common clocks

The two dwell times may differ and may each differ from one by a common
calibrated offset. What is needed is a single reused `K_L` and `K_H`:
`LL` must use `K_L²`, `HH` must use `K_H²`, and `HL` must use `K_H K_L`.
Independent identically distributed timing fluctuations on each tick also
give a reused averaged kernel, reversible under the same equilibrium.
Trial-level shared jitter does not generally have this property:
`E[K_tau²]` need not equal `(E[K_tau])²`. Bounded timing error alone
does not uniformly repair this issue for arbitrary-rate rivals.

One common J may differ from its design value. A field-dependent J would
introduce an SZ contribution in the Gibbs ratio and change the force
interface. Fixed per-spin attempt-rate changes preserve Gibbs equilibrium,
but unequal attempts are not included in the four-parameter family above.

With a nonzero low-field offset hL, the correct relative tilt is
`u=tanh(hH-hL)`, and the base law is the low-field equilibrium. The rival
identity remains valid with imbalanced initial mean mu0. In fact

$$
M_H+uC_H=\mu_0+u,\qquad
u=(M_H-\mu_0)/(1-C_H).
$$

Thus an observed confidence interval can profile u. If its denominator
interval includes zero the inference is inconclusive. A moderate low-field
offset is not part of the certified target box above; it can be included
only by evaluating an expanded target family. Small residual offsets can
instead be charged to the target-TV budget below. Approximate preparation
must likewise be charged: the displayed stationarity identity need not
hold for an arbitrary nonstationary initial distribution.

## Conservative target-law displacement

For a two-spin heat-bath generator with attempted updates alphaS,alphaZ,

$$
q_S=\frac{\alpha_S}2[1-S\tanh(JZ+h)],\qquad
q_Z=\frac{\alpha_Z}2[1-Z\tanh(JS)].
$$

Let the reference be any common-box target. Bound residual deviations by
`|dJ|<=epsJ`, `|dh|<=epsh`, `|dalpha_i|<=epsa`. Its nominal maximum
exit rate is below `lambda=5/3`. Since tanh is 1-Lipschitz,

$$
D:=\sup_x\sum_{y\ne x}|\widetilde q(x,y)-q(x,y)|
\le\frac53\epsilon_a+(1+\epsilon_a)(\epsilon_J+\epsilon_h/2).
$$

A maximal-jump coupling or Duhamel contraction gives transition-TV
displacement at most `integral D dt`. With at most two ticks, each
duration within epst of its registered value, the endpoint-pair distance
is bounded by

$$
b_T\le \epsilon_{p,T}+\frac{\epsilon_J+\epsilon_{hL}}2
+(101/50+2\epsilon_t)D+\frac{10}3\epsilon_t.
$$

Here preparation is within epspT of the actual low equilibrium; the extra
half-sum bounds its displacement from the registered low equilibrium.
If preparation error is defined directly relative to the registered law,
omit that extra half-sum. Retaining the initial sign does not double the
preparation bound. A joint initial-record/post-measurement disturbance
allowance xi, if needed, adds once.

The corresponding rival preparation allowance contributes
`b_R=epspR` by contraction, independently of rival rates. This does not
justify unregistered rival clock or field drift. Those would alter the
shared-kernel/Gibbs assumptions and need separate operational promises.

For a concrete conservative example, take
`epspT=epspR=10^-6` and
`epsJ=epsh=epshL=epsa=epst=0.5*10^-6`. Then
`b_T+b_R<7.366*10^-6`, leaving more than 42.6 ppm of the population
50 ppm gap. These are sufficient mathematical allowances, not a claim
that hardware achieves them. Common parameter uncertainty inside the
one-percent box is not included in this residual budget.

## Reset and detector channels

For the nominal physical target, pi_min=1/6 and the zero-field spectral
gap is 2/3. From every initial hidden state,

$$
\operatorname{TV}(\mu e^{TQ_0},\pi_0)
\le\frac{\sqrt5}2e^{-2T/3}.
$$

At T=21 this is below one ppm. This is a physical-target reset guarantee;
it is not a rate-independent reset guarantee for arbitrary rivals.
Uniformly over the common t box, T=22 suffices below one ppm using gap
`>=199/300` and `pi_min>=199/1200`. These reset times concern unit attempts
and zero low field. The residual-error example above assumes its stated
preparation accuracy separately; these reset bounds do not automatically
certify that accuracy with unequal attempts or a low-field offset.

For two known independent symmetric bit-flip channels with probabilities
p0,pf<1/2, the product inverse has induced l1 norm

$$
\kappa=[(1-2p_0)(1-2p_f)]^{-1}.
$$

Consequently a common channel converts a latent TV separation G into
a recorded separation at least G/kappa. One-percent flips at both ends
give kappa=2500/2401. Statistical errors after inversion are amplified by
this factor; nominal ideal-detector sample counts do not transfer unchanged.
For an asymmetric binary channel with false-positive/negative rates a,b,
the corresponding factor is `(1+|a-b|)/|1-a-b|`, and the two endpoint
factors multiply.

If endpoint bit-error probabilities are only bounded, a coupling gives
TV(recorded,latent)<=e0+ef, without requiring independent errors. Target
and rival allowances must both be charged if both channels are unknown.
Arbitrary unbounded rival detector errors are not covered by this new test.

If a known BSC calibration has residual probability uncertainties eta0,etaf,
inversion under the registered channel incurs at most
`kappa*(eta0+etaf)` latent-TV error per table. Charge both sides when
target and rival detector calibrations may differ. At registered one-percent
channels, eta0=etaf=0.25 ppm on each side adds at most 1.042 ppm.
Together with the physical example above, the total is below 8.408 ppm,
hence below a joint 10 ppm systematic budget.

## What the physical allowances establish

The common 1% parameter box changes a single coherent reference model;
it does not permit each word to choose new physics. Its $t$ and $m$ widths
are relative widths in $\tanh J$ and $\tanh H$, not relative widths in
$J$ and $H$ themselves. The target family fixes low field zero and equal
attempt rates. Its proof yields a population minimum of four ordinary
states, with an exact four-state upper, for each target in the box.

In contrast, proximity of actual recorded laws to an ideal target proves
statistical power under the specified instrument model. It does not by
itself prove an exact four-state upper for a whole imperfect apparatus.
A rejection means that the data are incompatible, at the stated error
level, with the ordinary at-most-three-state prediction class under the
reference and instrument promises. Persistent detector or controller
memory must be counted or explicitly modeled as part of the external
observation interface.

An initial readout requires control of the **joint law of its record and
the post-readout hidden state**. Preserving the visible bit or its marginal,
repeatability, and high classification fidelity do not establish this.
See the [existing readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md).
The known-channel score row assumes a fixed memoryless channel independent
of the latent trajectory; its 1% flips are already part of the reference.
Only calibration error, departure from that channel or instrument mismatch
uses the additional 10 ppm recorded-law allowance.

A finite field ramp inserts an additional propagator between plateaus.
It need not preserve either endpoint reversible law. With arbitrarily
large rival rates, a short ramp time alone cannot bound its error uniformly.
Use an explicitly registered switching interface or an independent bound
on its full pair-law effect. The target coupling/Duhamel estimate above
cannot certify this promise for the null class.

The 100m, 125m and 150m sufficient pair counts correspond to 200m, 250m
and 300m endpoint readouts. Reset, ramp and detector acquisition times,
channel-calibration samples and physical throughput are additional costs.
The reset bounds price only the target. They do not imply that every
admissible rival equilibrates in the same waiting time. The finite-sample
theorems in this note assume independent complete trials; a serial
application needs a separately justified conditional-law argument.

## Sources, certification and remaining question

The physical source audits remain in force. Bulnes Cuetara, Esposito and
Gaspard, [*Fluctuation theorems for capacitively coupled electronic currents*](https://arxiv.org/pdf/1105.5974),
Section II.A–B, equations (1), (12)–(20), derive a four-occupation weak-coupling
Markov model. A common equilibrium reservoir and energy-independent bare
coupling specialize it to the heat-bath setting; those specializations
and the measurement contract are additional assumptions here.
Connors, Nelson and Nichol, [*Rapid high-fidelity spin state readout in
Si/SiGe quantum dots via radio-frequency reflectometry*](https://arxiv.org/pdf/1910.08755),
Section III and equations (1)–(3), illustrate charge discrimination using
occupation-conditioned distributions. Detector fidelity alone supplies
no joint hidden-state-disturbance guarantee. Park et al.,
[npj Quantum Information (2025)](https://doi.org/10.1038/s41534-025-01094-x),
Methods on voltage pulses and supplementary lever-arm calibration,
illustrate crosstalk, timing and energy calibration. Their qubit reset is
not the common thermal four-state preparation required here. These sources
support components and conventions, not the full 50 ppm device contract.

The statistical tools are classical. Hoeffding,
[*Probability inequalities for sums of bounded random variables*](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)
(1963), Theorems 1–2, supplies the independent bounded-observation bounds.
The Bernstein inequality follows from the centered bounded-variable
exponential-moment bound
$\log\mathbb E e^{\lambda X}\le
\lambda^2\mathbb E X^2/[2(1-\lambda b/3)]$ for $\lambda b<3$.
Kaufmann, Cappé and Garivier,
[*On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models*](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf)
(2016), Lemma 1 and Appendix A.1, gives the adaptive change-of-measure
inequality used for the lower bound. No novelty is claimed for these tools.

Four new exact-arithmetic verifiers accompany this note:

- [Score test](../scripts/verify_familiar_switch_frozen_score.py) and [report](../reports/familiar_switch_frozen_score.json): fixed rational polynomials, target moment enclosures, gradients, Hessian boxes, global range/variance bounds and all three error-probability rows.
- [Tilt profiling](../scripts/verify_familiar_switch_frozen_sampling.py) and [report](../reports/familiar_switch_frozen_sampling.json): doubled confidence boxes, square-root branches and rational Hoeffding tails.
- [Information lower bound](../scripts/verify_familiar_switch_frozen_information.py) and [report](../reports/familiar_switch_frozen_information.json): pure-law equivalence, switched pair-law KL enclosures and necessary counts with ideal and known noisy readout.
- [Physical robustness](../scripts/verify_familiar_switch_frozen_robustness.py) and [report](../reports/familiar_switch_frozen_robustness.json): the continuous 1% box, population state lower bounds, control budgets, reset and detector inverse bounds.

All proof-bearing decisions use rational arithmetic and certified series
remainders; floating point is only for readable summaries. The new reports
bind this note and inherited frozen evidence. Largest propagated dynamics
matrix dimension is four. Independent internal review checks the analytic
identities and statistical/physical scope separately from running the
certificates. Existing proof and report snapshots remain unchanged.

The next scientific question is whether the same five-setting experiment
admits a substantially cheaper rigorous composite-null test, preferably
with tilt profiling, or whether a closer admissible rival raises the
information lower bound. This should narrow the acquisition gap before
any claim of a practical device test or broad publication significance.
The attained sharp calibrated switching error remains the structural
result; it is distinct from the 50 ppm uniform state certificate and from
finite-sample detection cost.
