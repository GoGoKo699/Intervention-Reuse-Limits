# A weaker field gives a larger detector-unknown memory gap

The same two binary snapshots and opposite control orders give a larger
robust separation at a simpler operating point:

$$
 J=\log3,\qquad H=\log2,\qquad
 t=\frac45,\quad u_0=\frac35,\quad
 \tau_0=\tau_H=\frac54.
 \tag{1}
$$

The total active duration is $5/2$ attempt-time units. No extra field,
preparation, readout, or protocol is introduced. The target is still the
four-state heat-bath model with energy $-JSZ-hS$, deterministic observed
conformation $S$, and equal unit attempt rates.

For independent symmetric detector errors of at most one percent on each
target bit, the nominal recorded-table gap against ordinary models with
at most three states exceeds $0.00115$. With the physical allowances
below, it still exceeds $0.001$. Rival detector errors may range anywhere
from zero to one half and may differ from the target's errors.

**Status:** the analytic derivation and exact numerical premises have
passed independent internal review. The certificate supplies finite
numerical bounds; the arbitrary-rival implications are analytic. These
checks are not external peer review. Sample optimality and experimental
feasibility are not claimed. The former operating point and its frozen
certificates remain valid. No manuscript is being drafted.

[Unknown-detector identity](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) ·
[Snapshot model and instruments](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) ·
[Positive three-state construction](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) ·
[Exploratory origin](FAMILIAR_SWITCH_NEXT_OPERATING_POINT.md) ·
[Source audit](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) ·
[Exact verifier](../scripts/verify_switch_weak_field.py) ·
[Certificate report](../reports/switch_weak_field.json)

## 1. The same observations and comparison class

Both protocols start from one shared low-field preparation. Protocol $A$
applies $0,H$ and records $(I,Y)$; protocol $B$ applies $H,0$ and records
$(J,Z)$. The initial and final readouts undergo independent symmetric
bit flips, independent of the hidden dynamics. Their fixed contrasts are
$r_0,r_f\in[0,1]$ and are shared across protocols. The initial record does
not control the later protocol. The four recorded moments are

$$
 M=\mathbb EY,\quad C=\mathbb E(IY),\quad
 L=\mathbb EZ,\quad D=\mathbb E(JZ).
 \tag{2}
$$

The rival uses one finite state space, deterministic binary readout,
shared preparation, kernels and instrument. Ordinary models obey detailed
balance at both fields. Their kernels need not be continuous-time
propagators; there is no rival graph restriction or kinetic-rate cap.
The comparison distance is the maximum total-variation distance of the
two $2\times2$ recorded joint tables. Distance at most $g$ changes each
moment in (2) by at most $2g$, even if initial marginals differ.

With balanced stationary low preparation and exact measured-coordinate
tilt, a singleton readout sector forces one of the detector-cleared
polynomials

$$
 K_\sigma(r_0,r_f)
 =r_fu_0(C-D)+\sigma[r_0r_fu_0L-u_0MD-r_0ML]
 \tag{3}
$$

to vanish. Every ordinary model with at most three states has such a
sector. The inherited corner argument shows that

$$
 0<M<u_0,\quad L>0,\quad D>0,\quad C<D,\qquad
 R:=u_0(C-D)+u_0MD-(u_0-M)L>0
 \tag{4}
$$

excludes both signs for every contrast pair in the closed square.
No detector inversion or fitted calibration is used.

## 2. Exact target enclosure and nominal margin

At (1), write the four latent moments as $(m,c,\ell,d)$. The exact
matrix-exponential enclosure gives

$$
 (m,c,\ell,d)\approx
 (0.220640327072,\ 0.482884706906,\
  0.125990415957,\ 0.501476600625).
 \tag{5}
$$

The computation uses rational four-state generators and a Taylor
polynomial through degree $96$ at time $5/4$. The induced row-sum norm
tail and dyadic rounding are enclosed exactly, then propagated through
both two-tick words. Each reported dyadic moment center has enclosure
radius $2^{-120}$. Decimal values in this note are explanatory; the
certificate uses the rational enclosures.

For target contrasts $a,b\in[49/50,1]$,

$$
 (M,C,L,D)=(bm,ab c,b\ell,ab d),\qquad
 R(a,b)=b\{a u_0(c-d+bmd)-u_0\ell+bm\ell\}.
 \tag{6}
$$

Both partial derivatives are positive throughout this square. As in the
earlier witness, this follows by checking the affine factor in
$\partial_aR=b u_0(c-d+bmd)$ and the multiaffine expression
$\partial_bR=a u_0(c-d)-u_0\ell+2ab u_0md+2bm\ell$
at their endpoints using the exact moment intervals. Thus the minimum
occurs at $a=b=49/50$, where

$$
 (M,C,L,D)\approx
 (0.216227520531,\ 0.463762472513,\
  0.123470607638,\ 0.481618127240),\qquad
 R>0.0043854.
 \tag{7}
$$

The absolute gradient mass of $R$ at a nominal target is

$$
 u_0D+L+3u_0-(1+u_0)M<1.88.
 \tag{8}
$$

It equals $3u_0+b[a u_0d+\ell-(1+u_0)m]$; the bracket is positive
and both contrasts increase this expression, so its maximum is at
$a=b=1$. The exact quadratic remainder under moment perturbations of
absolute size at most $r$ is bounded by $(1+u_0)r^2=(8/5)r^2$.
Consequently every point within joint-table TV $g$ of this target family
satisfies

$$
 R>0.0043854-1.88(2g)-\frac85(2g)^2.
 \tag{9}
$$

At $g=23/20000=0.00115$, the right-hand side is
$6617/125000000=0.000052936>0$. The four sign gates in (4) remain
strict. Hence the nominal ordinary-three-state gap exceeds $0.00115$.
This is a sufficient lower bound, not the optimized distance.

## 3. A local necessary inequality with imperfect stationary laws

Retain the same stationary promises as the earlier robust witness,
centered at the new high-field difference:

$$
 |v|=|\pi S|\le10^{-4},\qquad |u-u_0|\le10^{-4},\qquad
 \operatorname{TV}\!\left(\eta,\frac{\pi(1+uS)}{1+uv}\right)
 \le\theta=10^{-5}.
 \tag{10}
$$

Here $\pi,\eta$ are the stationary low and high laws. The stationary
recorded moments in this section use preparation $\pi$. Use the local
box

$$
 \begin{gathered}
 .20\le M\le.24,\quad .45\le C\le.50,\quad
 .11\le L\le.14,\quad .46\le D\le.52,\\
 -.04\le C-D\le-.001.
 \end{gathered}
 \tag{11}
$$

The biased detector-cleared polynomial is

$$
 \begin{split}
 J_\sigma={}&(1+\sigma v)[(1+\sigma u)r_0r_fL+ur_fC]\\
 &-(r_0L+uD)(r_f+\sigma M)
 -vr_0r_f[uM+\sigma(r_f(v+u)-M)].
 \end{split}
 \tag{12}
$$

The inherited singleton-sector argument gives

$$
 |J_\sigma|\le\Gamma_\sigma
 :=\frac{12u(1+\sigma v)(1+uv)\theta+
                 16(1+uv)^2\theta^2}{1-\sigma u}.
 \tag{13}
$$

Throughout (10), $\Gamma_-<0.000046$ and
$\Gamma_+<0.000181$. These bounds permit arbitrary detector contrasts.

The minus branch admits a much sharper bound than taking the absolute
value of every coefficient. It is affine in $r_0$, with endpoints

$$
 \begin{split}
 J_-(0,r_f)&=uMD+ur_f(C-D-vC),\\
 J_-(1,r_f)&=uMD+ML+r_f\{u(C-D-L)\\
 &\hspace{24mm}-v[(1-u)L+uC+(1+u)M]\}
 +r_f^2(vu+v^2).
 \end{split}
 \tag{14}
$$

Both decrease in $r_f$ on (10)--(11): their derivative upper bounds
are $-0.000569905$ and $-0.0665148712$. At $r_f=1$ their difference is

$$
 J_-(0,1)-J_-(1,1)
 =(u-M)L-v[(u-1)L-(1+u)M+u]-v^2
 \ge0.0395653769>0.0395.
 \tag{15}
$$

Thus the global minimum over the full contrast square is

$$
 J_-(1,1)=R_u+vB_u+v^2,\quad
 R_u=u(C-D-L+MD)+ML,\quad
 B_u=(u-1)L-uC-(1+u)M+u.
 \tag{16}
$$

The exact local bounds are $|\partial_uR_u|\le.088$ and
$|B_u|<.141$. A minus singleton therefore implies

$$
 R<.000046+.088\,10^{-4}+.141\,10^{-4}+10^{-8}
 =.00006891<.00007.
 \tag{17}
$$

For the plus branch, compare (12) with $K_+$ at fixed $u_0$.
The absolute $u$ derivative is below $.305$; the linear coefficient
of $v$ has absolute value at most $1.220188$ and its quadratic term
is at most $v^2$. Therefore the necessary bound is

$$
 |K_+|<.305\,10^{-4}+1.220188\,10^{-4}+10^{-8}+.000181
 <.0004.
 \tag{18}
$$

If $R\ge.00007$, the first three contrast corners of $K_+$ are at
most $-u_0MD\le-.0552$, while the last is
$2u_0(C-D)-R\le-.00127$. Bilinear interpolation contradicts (18).
Combining the two branches proves the local necessary condition

$$
 \boxed{R<0.00007}
 \tag{19}
$$

for every stationary ordinary model with at most three states in (11).
The wider $C-D$ gate in (11) also allows economical statistical gates;
it does not add a new observable.

At $g_0=9/8000=0.001125$, (9) gives $R>0.0001473$.
Every point in that target neighborhood lies in (11). Equation (19)
therefore proves a stationary ordinary-three-state separation greater
than $g_0$, uniformly over (10) and the entire rival contrast square.

## 4. Physical tolerances and the actual memory interval

Use the same fixed preparation and initial-instrument assumptions as the
snapshot proof. Let each preparation be within $\epsilon_p$ of its
stationary low law, and let the joint-TV effect of the initial hidden
disturbance be at most $\xi$. A uniform per-state disturbance bound is
sufficient; the bound must include its correlation with the retained
initial label. Electronics are already counted in the symmetric channels.

For the target let actual common plateaus lie within $\epsilon_h$ of
$0,\log2$, and actual common field-specific dwell times lie within
$\epsilon_t$ of $5/4$. The equilibrium displacement costs at most
$\epsilon_h/2$. The observed-spin generator perturbation costs at most
$\epsilon_h/2$ per unit active time, whose total is at most
$5/2+2\epsilon_t$. The two timing errors cost at most $4\epsilon_t$
because the target exit rate is below two. Including preparation and
disturbance gives

$$
 b_T\le\epsilon_{p,T}
       +\left(\frac74+\epsilon_t\right)\epsilon_h
       +4\epsilon_t+\xi_T,\qquad
 b_R\le\epsilon_{p,R}+\xi_R.
 \tag{20}
$$

Here $b_R$ compares an actual rival to its own stationary reference;
the rate-independent stationary lower already permits arbitrary
reversible field kernels. Choose

$$
 \epsilon_{p,T}=\epsilon_{p,R}=\epsilon_h=\epsilon_t
 =\xi_T=\xi_R=10^{-5}.
 \tag{21}
$$

Then $b_T=0.0000775001$ and $b_R=0.00002$ suffice.
The actual target has low bias $|\tanh h_0|\le10^{-5}$ and exact
stationary tilt parameter $u=\tanh(h_H-h_0)$, so
$|u-3/5|\le2\times10^{-5}$; it lies within (10) with $\theta=0$.
Each model's own fixed channel contracts its displacement. Since the
stationary argument already allows rival and target channels to differ,
no extra channel-comparison term is needed. The actual observed gap is
strictly greater than

$$
 \frac9{8000}-b_T-b_R=0.0010274999>\boxed{0.001}.
 \tag{22}
$$

The positive three-state construction in the charge-realization proof,
with rate ratio one, applies at every field with
$-10^{-4}\le\tanh h\le.81$. Both actual plateaus in (21) lie inside
this interval, including negative low-field errors. Its readout and
auxiliary coordinates are

$$
 \widehat S=(-1,1,1),\qquad
 \widehat Z=(-4/5,-8/5,26/25),\qquad
 \widehat\pi_0=(1/2,1/22,5/11).
 \tag{23}
$$

The tilted stationary law has the same initial sector masses and
conditional coordinate means $(\sigma,(4/5)\sigma)$ as the physical
model. The shared closed evolution therefore reproduces both actual-field,
stationary, ideal-instrument joint laws, at their actual dwell times.
Use the target's detector on this predictor. The preparation and
disturbance allowance then gives constructive error at most
$\epsilon_{p,T}+\xi_T=2\times10^{-5}$.

The actual four-state target is itself an admissible ordinary upper.
Every stationary two-state kinetic model is ordinary, so the same lower
also excludes general two-state competitors. Consequently the exact
kinetic-state minima are three for general stationary predictors and
four for ordinary models throughout

$$
 \boxed{2\times10^{-5}\le\delta_{\rm obs}\le10^{-3}.}
 \tag{24}
$$

At the ideal operating point the corresponding interval begins at zero
and extends through $0.00115$. These state counts concern only the two
specified joint tables. The preparation, channel form, fixed instrument,
and stationary force-law promises are not inferred from the four moments.

There is also a simple tolerance tradeoff. Increase all six allowances in
(21) to $5\times10^{-5}$, keeping the stationary promises (10) and the
same detector classes. Equation (20) gives $b_T=0.0003875025$ and
$b_R=0.0001$, so the actual gap exceeds $0.0006374975>0.0006$.
The actual target still has $|v|\le5\times10^{-5}$ and
$|u-u_0|\le10^{-4}$; both fields remain in the positive predictor's
domain. Its constructive error is now at most $10^{-4}$.

| Common value of all six allowances in (21) | General three-state upper | Certified three-versus-four error interval |
|---|---:|---|
| $10^{-5}$ | $2\times10^{-5}$ | $[2\times10^{-5},10^{-3}]$ |
| $5\times10^{-5}$ | $10^{-4}$ | $[10^{-4},6\times10^{-4}]$ |

The [two-million and 2.5-million-trial tests](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md)
use the tighter first row. Their sample guarantees are not transferred
to the relaxed row; that row certifies a population state-cost interval.

## 5. Why this operating point improves the noisy signal

For equal detector contrasts $r$, the witness has the exact decomposition

$$
 R(r,r)=r^2R(1,1)-r(1-r)u_0(\ell+rmd).
 \tag{25}
$$

The second term is the noise penalty. At the new point the ideal witness
is approximately $0.00743676$, smaller than the earlier point's
$0.00811481$. At one-percent errors, however, the penalty is approximately
$0.00275682$, and the remaining witness is $0.00438544$ instead of
$0.00171576$. The weaker-field, shorter-dwell choice improves the balance
between signal and this detector penalty. Maximizing the ideal witness
alone would miss that advantage. This comparison does not assert an
optimal field or dwell time, or extend the target detector allowance
beyond one percent.
