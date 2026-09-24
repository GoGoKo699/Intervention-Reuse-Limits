# Calibration tolerances for the seven-experiment state-cost witness

This note quantifies a controlled extension of the
[finite-margin coupled-switch result](FAMILIAR_SWITCH_FINITE_MARGIN.md).
It distinguishes imperfect execution of the target experiment from changes
to the rival assumptions. Fixed field offsets and common clock errors can
be covered. Arbitrary drift or finite switching ramps do not automatically
preserve the witness.

The analytic argument and exact rational certificate have passed
independent internal review. The certified polynomial box is an essential
part of the proof, with the universal rival implication proved below.

[Calibration verifier](../scripts/verify_switch_calibration.py) ·
[Certificate report](../reports/switch_calibration.json) ·
[Source and scope audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md)

## 1. A simultaneous operating regime

The target remains two time-even conformational switches, with energy
$E_h=-Js_0s_1-hs_0$, equal unit attempt rates, observed variable $S=s_0$,
and $J=H=\log3$. Each nominal tick lasts two time units. Use the seven
chronological words

$$
 H,\ H^2,\ H^3,\ H\,0,\ H^2\,0,\ H\,0\,H,\ H^2\,0\,H.
 \tag{1}
$$

The same actual low field $h_0$ and high field $h_H$ are used in every word.
Each occurrence of a field has the same actual tick duration $\tau_0$ or
$\tau_H$; the two durations may differ. Field switches are instantaneous
in this comparison. Each model uses one fixed preparation law across all
seven words. A sufficient simultaneous calibration is

| Quantity | Allowed error |
|---|---:|
| Low field | $\lvert h_0\rvert\le10^{-5}$ |
| High field | $\lvert h_H-\log3\rvert\le10^{-5}$ |
| Each common field-specific tick | $\lvert\tau_h-2\rvert\le10^{-5}$ |
| Target preparation versus its actual low-field equilibrium | TV distance at most $10^{-5}$ |
| Rival preparation versus its own actual low-field stationary law | TV distance at most $10^{-5}$ |

The rival has a deterministic binary readout. Its two generators satisfy
ordinary detailed balance at the actual plateaus, but their rates and graph
are otherwise unrestricted. In addition to the field calibration, allow
its actual high-field stationary law to differ by TV distance at most
$10^{-5}$ from the prescribed Gibbs tilt of its low-field stationary law.
The latter law's readout bias must be within $10^{-4}$ of zero. Section 2
states this distributional assumption precisely.

Under these assumptions, every ordinary rival with at most three states
has maximum occupation-probability error **greater than $3/10000$** against
the actually prepared and driven target on (1). This is 0.03 percentage
points. A stationary unrestricted three-state predictor approximates the
actual target within $10^{-5}$, while the physical four-state target is
itself an ordinary realization. Consequently the minimum counts remain
three versus four for occupation-error tolerances

$$
 10^{-5}\le\delta\le3\times10^{-4}.
 \tag{2}
$$

These tolerances are sufficient, not optimal. Preparation TV and stationary
law TV refer to the full state distributions, not just their binary means.
No hidden-state TV guarantee follows from observing a nearly balanced
readout alone.

## 2. Biased preparation and an approximate equilibrium force law

First consider stationary preparation. Let $\pi$ be a rival's actual
low-field stationary law and write $b=\pi S$. Its high-field stationary
law is $\eta$. Put

$$
 z=1+ub,\qquad
 \lambda(x)=\frac{\pi(x)(1+uS(x))}{z},\qquad
 \operatorname{TV}(\eta,\lambda)\le\theta.
 \tag{3}
$$

Here $u$ is the relative field increment in hyperbolic-tangent coordinates.
For an exact Gibbs force family with a balanced reference law,

$$
 b=\tanh h_0,\qquad u=\tanh(h_H-h_0).
 \tag{4}
$$

The polynomial certificate allows the larger nuisance range

$$
 |b|\le\frac1{10000},\qquad
 \left|u-\frac45\right|\le\frac1{10000},\qquad
 \theta\le\frac1{100000}.
 \tag{5}
$$

The two transition kernels are reversible for $\pi$ and $\eta$,
respectively. They can even be arbitrary reversible stochastic kernels;
continuous-time embeddability is not needed for this part of the argument.
The stationary-law tolerance in (3) permits a small violation of the exact
force law. It does not permit an arbitrary unrelated high-field equilibrium.

Let $(m,n,p,\ell_1,\ell_2,k_1,k_2)$ be the seven stationary-preparation
binary means in the order (1). Define

$$
\begin{gathered}
 N=b+u-m,\qquad Z=b+u-(1-u^2)n,\qquad
 q_\sigma=1+\sigma b,\qquad
 D_\sigma=u q_\sigma(1-\sigma u),\\
 V=\begin{pmatrix}1&b&m\\1&m&n\\1&n&p\end{pmatrix},\qquad
 V_0=\begin{pmatrix}1&b&m\\1&\ell_1&k_1\\1&\ell_2&k_2\end{pmatrix},
 \qquad A=\operatorname{adj}(V)V_0,
\end{gathered}
\tag{6}
$$

for $\sigma=\pm1$. The scaled candidate Gram matrix is

$$
 G_\sigma=
 \begin{pmatrix}
 D_\sigma&D_\sigma b&D_\sigma m\\
 D_\sigma b&D_\sigma&q_\sigma(1-\sigma u)N\\
 D_\sigma m&q_\sigma(1-\sigma u)N&
 q_\sigma Z-\sigma(um+\sigma N)^2
 \end{pmatrix}.
 \tag{7}
$$

Using one-based matrix indices, form the nine-variable polynomial

$$
 P_\sigma=(G_\sigma A)_{23}-(G_\sigma A)_{32}.
 \tag{8}
$$

At $b=0$ this is $u$ times the polynomial $W_\sigma$ in the preceding
finite-margin note. It has degree four in the response means and total
degree seven when $b,u$ are also variables.

### Exact force law

When $\theta=0$, let $F=E_HS$ and $g=\langle SF\rangle_\pi$.
Stationarity and reversibility at $H$ give

$$
 g=N/u,\qquad z\langle F^2\rangle_\lambda=Z/u.
 \tag{9}
$$

If readout sector $\sigma$ is a singleton, its value of $F$ is
$(m+\sigma g)/q_\sigma$. It follows that $G_\sigma$ equals
$D_\sigma$ times the true baseline Gram matrix of $(1,S,F)$.
The adjugate argument from the preceding note then gives $P_\sigma=0$,
including singular response tables. Every model with at most three states
has at least one such singleton sector; two-state models are covered by
the same algebraic zero-mass padding used there.

### Approximate force law

The same conclusion has a controlled residual when $\theta>0$. Since
$F,E_H^2S,S$ lie in $[-1,1]$, stationarity of $\eta$ implies

$$
 |g-N/u|\le d:=\frac{4z\theta}{u}.
 \tag{10}
$$

For example, $|\lambda F-\lambda S|\le4\theta$, and multiplying this
inequality by $z/u$ gives (10). Detailed balance under $\eta$ further
gives $\langle F^2\rangle_\eta=\langle S,E_H^2S\rangle_\eta$.
Changing the expectation of $F^2\in[0,1]$ costs at most $\theta$;
changing that of $S E_H^2S\in[-1,1]$ costs at most $2\theta$.
Together with the corresponding stationarity defect,

$$
 \left|z\langle F^2\rangle_\lambda-Z/u\right|
 \le z(3+4/u)\theta.
 \tag{11}
$$

The true singleton value also obeys $|m+\sigma g|\le q_\sigma$.
Thus the error in the scaled Gram off-diagonal entry $(2,3)$ is at most
$|D_\sigma|d$, and that in entry $(3,3)$ is at most

$$
 E_\sigma=u q_\sigma z(3+4/u)\theta
           +u^2(2q_\sigma+d)d.
 \tag{12}
$$

All its other entries are exact. The true Gram-adjugate product remains
symmetric by low-field detailed balance, so every such small ordinary
rival satisfies, for at least one singleton sign,

$$
 |P_\sigma|\le
 |D_\sigma|\,|A_{33}-A_{22}|d+|A_{32}|E_\sigma.
 \tag{13}
$$

There is no division by $\det V$, no lower stationary-mass assumption,
and no rival rate constant in this estimate.

## 3. The enlarged exact certificate

The new certificate reuses the rigorously enclosed nominal target means
from the frozen [finite-margin report](../reports/familiar_switch_margin.json).
Each lies within $2^{-120}$ of its recorded rational center. Translate the
polynomials (8) about those seven centers together with $b=0,u=4/5$.
The coordinate radii are

$$
 \rho_{\mathrm{mean}}=\frac1{1250}+2^{-120},\qquad
 \rho_b=\rho_u=\frac1{10000}.
 \tag{14}
$$

The first radius corresponds to occupation error $g_0=1/2500$. The verifier
constructs each polynomial exactly, expands it about the center, and bounds
its entire variation by the sum of absolute nonconstant coefficients times
the appropriate powers of the nine radii. It certifies

$$
\begin{aligned}
 |P_\sigma(\text{center})|&>1164/10^7,\\
 \text{variation}(P_-)&<914/10^7,\\
 \text{variation}(P_+)&<272/10^7.
\end{aligned}
\tag{15}
$$

Hence $|P_\sigma|>1/40000$ throughout this box. On the same box it verifies

$$
 |A_{33}-A_{22}|<10854/10^6,\qquad |A_{32}|<19084/10^6.
 \tag{16}
$$

Inserting (5) and (16) in the analytic residual bound (13) gives a value
strictly below $1/300000$, for either sign. Thus the polynomial separation
from every allowed residual is greater than

$$
 \frac1{40000}-\frac1{300000}=\frac{13}{600000}>0.
 \tag{17}
$$

This proves that every allowed stationary-preparation ordinary rival with
at most three states differs from the nominal target by more than
$g_0=1/2500$ in at least one occupation probability. The rational computation
is an essential numerical premise; the universal implication comes from
(13), not from testing a set of fitted rivals.

## 4. Target displacement under calibrated fields, clocks, and preparation

For two finite-state generators, use the signed row total-variation norm

$$
 \|\widetilde Q-Q\|_{\rm row,TV}
 =\frac12\max_x\sum_y|\widetilde Q_{xy}-Q_{xy}|.
 \tag{18}
$$

Duhamel's identity and stochastic contraction show that any endpoint
occupation probability changes by at most initial TV error plus the
integral of (18). This bound has no dimension factor: the backward
propagated occupation observable remains in $[0,1]$.

A field change affects only the observed-spin flip rate and its opposite
diagonal entry. Its row-TV cost is exactly the maximum change of that flip
rate. At the high plateau it is at most $|\Delta h|/2$. At the low plateau,
with $t=4/5$ and $|h|\le1/8$, the sharper finite-difference estimate is

$$
 \max_s|q_0(s;h)-q_0(s;0)|
 \le\frac{(1-t^2)\tanh|h|}{2(1-t\tanh|h|)}
 \le\frac{|h|}{5}.
 \tag{19}
$$

The last inequality uses $\tanh|h|\le|h|$ and $t|h|\le1/10$.
It is a finite-difference bound, not a claim that the derivative remains
below $1/5$ over that whole interval.

Timing admits a similarly simple target-specific bound. After any future
sequence of ferromagnetic field plateaus, a backward occupation observable
has the form $A+bS+cZ$ with $b,c\ge0$ and $b+c\le1/2$.
The two-spin mean closure preserves these properties. Applying $Q_0$ to
such an observable has sup norm at most $9/10$; applying $Q_H$ has norm at
most $81/82$. Therefore a low-field tick error costs at most
$(9/10)|\Delta\tau_0|$, and each high-field tick error at most
$(81/82)|\Delta\tau_H|$. The longest menu word has three high ticks and
one low tick, so common errors bounded by $\epsilon_t$ contribute at most

$$
 \left(\frac9{10}+\frac{243}{82}\right)\epsilon_t
 =\frac{792}{205}\epsilon_t.
 \tag{20}
$$

Let both plateau offsets be bounded by $\epsilon_h\le1/8$, and target
preparation be within $\epsilon_p$ of its actual low-field equilibrium.
The shift of that equilibrium from the nominal zero-field law has TV
distance $|\tanh h_0|/2\le\epsilon_h/2$. Applying (19) for the actual
plateau durations and then (20) gives the uniform target displacement

$$
 b_T=\epsilon_p+\frac{\epsilon_h}{2}
 +(2+\epsilon_t)\frac{17}{10}\epsilon_h
 +\frac{792}{205}\epsilon_t.
 \tag{21}
$$

The $17/10$ coefficient is three high ticks at rate sensitivity $1/2$
plus one low tick at sensitivity $1/5$. A rival preparation within
$\epsilon_p$ of its own low-field stationary law changes each of its
occupation responses by at most $b_R=\epsilon_p$, regardless of its rates.

The field bounds in Section 1 imply $|b|\le10^{-5}$ in an exact reference
Gibbs family and $|u-4/5|\le2\times10^{-5}$, inside (5). More generally,
the stated low-bias bound and approximate high-field law may be checked
as assumptions directly. Combining (21) with Section 3 yields the general
tradeoff

$$
 \|\mathbf p_{\rm target,actual}-\mathbf p_{\rm ordinary,actual}\|_\infty
 >g_0-b_T-b_R.
 \tag{22}
$$

For $\epsilon_h=\epsilon_t=\epsilon_p=10^{-5}$,

$$
 b_T+b_R=0.00009763431634146\ldots<\frac1{10000}.
 \tag{23}
$$

Thus the actual comparison has gap greater than $3/10000$, as claimed.
Preparation error is charged on both sides. Merely bounding the target's
execution error would not establish this same-experiment statement.

## 5. The three-state upper survives the same calibration

The exact three-state predictor from the structural note extends to the
small negative low fields allowed here. At $t=4/5$, use its readout
$(-1,1,1)$ and internal coordinate $(-4/5,-8/5,41/40)$.
For $v=\tanh h$, its rates reduce to

$$
\begin{gathered}
 L=\frac{9(1+v)}{2(25-16v^2)},\qquad
 q_{21}=\frac{(1-v)(57+48v)}{2(25-16v^2)},\qquad
 q_{31}=\frac{9(1-v)^2}{4(25-16v^2)},\\
 q_{12}=\frac{73}{105}L,\quad q_{13}=\frac{32}{105}L,\quad
 q_{23}=\frac{32}{105}(3-q_{21}),\quad
 q_{32}=\frac{9-73q_{31}}{105}.
\end{gathered}
\tag{24}
$$

On $-10^{-4}\le v\le9/10$, all rates are strictly positive:
$q_{21}\le1.14005<3/2$, $q_{31}<91/1000$, and the remaining numerators
are then positive. Its exit rates stay below two. This interval covers
both actual plateaus. The closure and Gibbs-stationarity identities are
algebraic and remain valid throughout it.

Start this predictor in its actual low-field stationary law. Its controlled
means agree exactly with those of the physical target started in its
actual low-field equilibrium. An arbitrary allowed target preparation
error changes the latter occupation probabilities by at most
$\epsilon_p=10^{-5}$. Thus this three-state predictor meets that error
budget while itself having zero preparation error and exact equilibrium
tilt. The physical four-state target supplies the ordinary upper. Every
two-state stationary chain is ordinarily reversible, so (22) excludes
unrestricted two-state competitors as well. These facts prove (2).

## 6. What preserves the repeated-kernel experiment

Unknown but fixed field-specific durations preserve the experiment:
$E_0=e^{\tau_0Q_0}$ and $E_H=e^{\tau_HQ_H}$ remain two shared reversible
kernels. The polynomial does not require $\tau_0=\tau_H$ or knowledge of
their numerical values. The bounds on them in Section 1 are used to bound
the target's displacement from the certified nominal response.

Independent per-occurrence duration jitter is also compatible if each
field always uses the same duration distribution, independent of the
hidden state and other ticks. Its averaged kernel is a mixture of
same-field reversible kernels, hence reversible and stationary for the
same law. Products of these averaged kernels describe the mean responses.
To use the concrete target bound above, the jitter must obey the stated
duration-error bound almost surely; expected absolute errors can instead
be inserted in the timing term. A random duration shared across several
ticks in one trial is not covered by this independence argument.

Protocol-dependent durations, field drift, or correlations between ticks
can destroy the repeated-kernel identities. Finite switching ramps are
also different: a time-ordered product of instantaneous generators with
different equilibrium laws need not be reversible for either endpoint law.
Even reproducible ramps therefore do not automatically fit the two-kernel
comparison. With unbounded arbitrary rival kinetics, a short ramp has no
uniformly small effect. No finite-ramp tolerance is claimed by the main
theorem.

There is an optional rate-capped extension for ramp errors. If both the
actual and nominal rival generators have exit rates at most $R$ throughout
a ramp, their row-TV difference is at most $R$. Total ramp duration
$T_r$ then costs at most $RT_r$ on the rival side. On the target side,
the cost is at most $\tfrac12\int|h_{\rm ramp}-h_{\rm step}|dt$.
For three one-sided linear ramps, each of duration $\rho$ replacing part
of a plateau, the joint additional allowance is at most
$(3R+3|h_H-h_0|/4)\rho$, or conservatively
$(3R+3(H+2\epsilon_h)/4)\rho$. This requires an additional rate cap and is
separate from the uncapped result above.

## 7. Preparation and measurement costs

The target's zero-field single-spin relaxation eigenvalues are
$-1\pm t$, and the remaining nonconstant eigenvalue is $-2$.
At an actual low field, $tB(h_0)\le t^2$, so its spectral gap remains at
least $1/5$. Its smallest stationary mass is at least
$(1-10^{-5})/20$. Standard reversible contraction therefore gives, from
any initial target law,

$$
 \operatorname{TV}(\rho e^{TQ_{h_0}},\pi_{h_0})
 \le\frac12\sqrt{\frac{20}{1-10^{-5}}-1}\,e^{-T/5}.
 \tag{25}
$$

A reset wait of 62 time units makes the right side smaller than $10^{-5}$.
This is a target-specific guarantee. No finite uniform wait prepares every
arbitrarily slow rival near its own equilibrium. The rival preparation
assumption must be justified separately, and stationary readout bias is
not a substitute for hidden-state TV control.

Conditional reset guarantees that allow the preparation error to depend
on earlier trials can support statistical bias bounds. They do not by
themselves give the single fixed preparation law used in the state-count
statement (2).

For a statistical confidence-box comparison, systematic target displacement,
rival preparation, requested prediction tolerance $r$, and a simultaneous
sampling radius $e$ must satisfy

$$
 b_T+b_R+r+2e\le g_0.
 \tag{26}
$$

The two sampling radii account for the fluctuation of the data and the
confidence region around those data. Under the concrete calibration above,
$r=e=10^{-4}$ is sufficient. A conservative independent-endpoint
Hoeffding calculation gives 1,972,176,367 total trials at 95% simultaneous
confidence, with type-I error at most 5% and power at least 95% for this
example. This is a sufficient scheme, not a necessary sample complexity.
The statistical decision rule, sufficient counts, and information lower
bound are developed in the separate
[measurement-cost note](FAMILIAR_SWITCH_MEASUREMENT_COST.md) rather than
duplicated here.
