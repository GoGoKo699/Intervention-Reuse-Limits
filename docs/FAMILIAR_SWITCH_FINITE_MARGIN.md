# Seven short experiments certify a finite reversible state cost

This note strengthens the [coupled-switch theorem](FAMILIAR_SWITCH_STRUCTURE.md)
without changing its physical model, preparation, or readout. A polynomial
identity in seven endpoint means holds for every ordinarily reversible model
with at most three states and the shared Gibbs force tilt. The four-state
target violates that identity. No generator reconstruction, matrix logarithm,
rate bound, or lower bound on stationary state masses is needed.

An exact rational certificate proves a $1/2000$ lower error bound and checks
one ordinary three-state model with error below $1/1000$, on the same seven
experiments. The bracket is 0.05 to 0.1 percentage points in occupation
probability. The universal obstruction is analytic; the explicit numerical
threshold uses the essential, reproducible certificate in Section 5.

[Certificate script](../scripts/verify_familiar_switch_margin.py) ·
[Certificate report](../reports/familiar_switch_margin.json) ·
[Source comparison](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md)

## 1. Model, experiments, and the quantitative claim

Take two time-even conformational variables $s_0,s_1\in\{-1,1\}$, with
energy $E_h=-Js_0s_1-hs_0$ and equal unit-attempt heat-bath flip rates.
Prepare zero-field equilibrium and observe only $S=s_0$. The parameters in
the numerical certificate are

$$
 J=H=\log3,\qquad t=\tanh J=\frac45,\qquad
 u=\tanh H=\frac45,\qquad a=2.
 \tag{1}
$$

Here $a$ is the duration of one clock tick. Every experiment uses the same
preparation and records only its final occupation probability
$P(S=+1)=(1+\langle S\rangle)/2$. The seven chronological words are

$$
 H,\quad H^2,\quad H^3,\quad H\,0,\quad H^2\,0,
 \quad H\,0\,H,\quad H^2\,0\,H.
 \tag{2}
$$

Thus no experiment has more than three field segments or four ticks. At (1),
the longest experiment lasts eight attempt-rate time units. This menu is a
subset of the previously proved eleven-word menu, so any lower bound here
also applies to that menu.

Rivals have a deterministic binary readout and a zero-field stationary law
$\pi_0$ giving each readout value mass $1/2$. Their equilibrium laws obey

$$
 \pi_H=\pi_0(1+uS),
 \tag{3}
$$

and each field generator satisfies ordinary detailed balance for its own law.
This shared tilt means the force couples only to the measured conformation.
Allowing unrelated equilibrium laws at the two fields is outside the claim.
All other stationary masses, rate choices, and graph structures are free;
in particular, there is no rival rate cap.

The explicit quantitative theorem is that every ordinary rival with at most
three states has maximum occupation-probability error **strictly greater
than $1/2000$** on (2). The exact three-state stationary predictor from the
companion theorem still matches every target mean. Consequently, at every
allowed occupation-error tolerance up to $1/2000$, the minimum counts are
three for unrestricted stationary predictors and four for ordinary ones.
The value $1/2000=0.0005$ is **0.05 percentage points**, not one percent.

In fact, the lower bound covers an even larger class: the two clock
propagators may be arbitrary stochastic matrices reversible for (3).
Continuous-time embeddability and positive propagator spectra are not used.

## 2. A necessary polynomial identity for every small reversible model

Let $E_0,E_H$ denote one-tick propagators, and write the seven measured binary
means in the order

$$
 (m,n,p,\ell_1,\ell_2,k_1,k_2)
 =\bigl(m(H),m(H^2),m(H^3),m(H\,0),m(H^2\,0),m(H\,0\,H),m(H^2\,0\,H)\bigr).
 \tag{4}
$$

Set $F=E_HS$ and $c=1-m/u$. Stationarity under $H$, together with (3), gives

$$
 \langle F\rangle_0=m,\qquad
 \langle SF\rangle_0=c.
 \tag{5}
$$

Detailed balance under $H$ gives
$\langle F^2\rangle_H=\langle S,E_H^2S\rangle_H$. Since
$\pi_0=\pi_H(1-uS)/(1-u^2)$, the second moment is observable directly:

$$
 v_H:=\langle F^2\rangle_H=1-\frac{1-u^2}{u}n.
 \tag{6}
$$

A three-state binary model has a singleton readout sector, with sign
$\sigma\in\{-1,1\}$. At that state $F$ must equal its conditional mean
$f_\sigma=m+\sigma c$. If $x=\langle F^2\rangle_0$, the tilt implies

$$
 x=x_\sigma:=
 \frac{v_H-\sigma u(m+\sigma c)^2}{1-\sigma u}.
 \tag{7}
$$

The baseline Gram matrix for the three functions $(1,S,F)$ is therefore

$$
 M_\sigma=
 \begin{pmatrix}1&0&m\\0&1&c\\m&c&x_\sigma\end{pmatrix}.
 \tag{8}
$$

The two response tables obtained from the seven measurements are

$$
 V=\begin{pmatrix}1&0&m\\1&m&n\\1&n&p\end{pmatrix},\qquad
 V_0=\begin{pmatrix}1&0&m\\1&\ell_1&k_1\\1&\ell_2&k_2\end{pmatrix}.
 \tag{9}
$$

To include singular response tables, let $C$ have rows $(1,S,F)$ evaluated
at each of the three states, and let $R$ have rows $\pi_0E_H^i$ for
$i=0,1,2$. Then $V=RC$, $V_0=RE_0C$, and
$M_\sigma=C^T\operatorname{diag}(\pi_0)C$. The elementary adjugate identity

$$
 C\,\operatorname{adj}(RC)R=\det(RC)I
 \tag{10}
$$

holds even when $R$ or $C$ is singular. Thus

$$
 M_\sigma\operatorname{adj}(V)V_0
 =\det(V)C^T\operatorname{diag}(\pi_0)E_0C
 \tag{11}
$$

is symmetric by zero-field detailed balance. This is a necessary identity
on the actual measurements, with no matrix inverse or conditioning premise.
Two-state models are included by algebraically adding an isolated zero-mass
state in the opposite readout sector from a chosen singleton. That padding
does not alter their responses, stationarity, tilt, or detailed balance.

For an explicit scalar version, define

$$
\begin{aligned}
 a_1&=(p-m)\ell_1-(n-m)\ell_2,&
 a_2&=-n\ell_1+m\ell_2,\\
 b_1&=(p-m)(k_1-m)-(n-m)(k_2-m),&
 b_2&=-n(k_1-m)+m(k_2-m),\\
 v_\sigma&=1-\frac{1-u^2}{u}n
 -\sigma u(m+\sigma c)^2-(1-\sigma u)m^2.
\end{aligned}
\tag{12}
$$

The antisymmetric $(2,3)$ entry of (11), with its constant denominator
cleared, is the quartic polynomial

$$
 W_\sigma=(1-\sigma u)(b_1+c b_2-c a_1)-v_\sigma a_2.
 \tag{13}
$$

Every ordinary model with at most three states therefore satisfies
$W_+=0$ or $W_-=0$. Both alternatives must be excluded to rule out the
whole rival class. The inference concerns one shared model for all seven
experiments, not a separate fit for each protocol.

## 3. The target violates both alternatives at every positive coupling

For arbitrary $J,H,a>0$, put $t=\tanh J$, $u=\tanh H$, and

$$
 B=\frac{t(1-u^2)}{1-t^2u^2},\quad
 \kappa=\sqrt{tB},\quad
 \gamma=e^{-a}\frac{B}{\kappa}\sinh(a\kappa),\quad
 d=e^{-a}\sinh(at).
 \tag{14}
$$

In the target's closed mean space, $F=E_HS=m+\beta S+\gamma Z$, where
$Z=s_1$ and $\beta=e^{-a}\cosh(a\kappa)$. The zero-field law has
$\langle SZ\rangle_0=t$. Thus the true conditional variance of $F$ at
either readout sign is $\gamma^2(1-t^2)$.

At target data, forcing the singleton formula (7) changes only the last
diagonal entry of the true baseline Gram matrix $M_*$:

$$
 (1-\sigma u)M_\sigma
 =(1-\sigma u)M_*+\sigma u\gamma^2(1-t^2)e_3e_3^T.
 \tag{15}
$$

Zero-field evolution satisfies $E_0S=e^{-a}\cosh(at)S+dZ$. Its coefficient
of $F$ in the $(1,S,F)$ basis is $d/\gamma$. This target mean space is
invariant, so its restricted matrix $A_0$ satisfies $V_0=VA_0$, and
$M_*A_0$ is symmetric. Combining this with (13) and (15) gives

$$
 W_\sigma(\mathbf m_*)=-\sigma\Delta,\qquad
 \Delta=u\gamma(1-t^2)d\det V>0.
 \tag{16}
$$

For completeness, positivity of the determinant is explicit. With
$r=e^{-a(1-\kappa)}$ and $q=e^{-a(1+\kappa)}$,

$$
 m(H^j)=u-\frac{u(1+\kappa)}2r^j
          -\frac{u(1-\kappa)}2q^j,
 \qquad
 \det V=\frac{u^2(1-\kappa^2)}4(1-r)(1-q)(r-q)^2>0.
 \tag{17}
$$

This proves exact discrimination directly at finite times. The obstruction
is the hidden conditional variance at both readout values; the adjugate
calculation expresses it as a scalar constraint on seven measured means.

## 4. An explicit analytic error bound for every parameter choice

Expand (13), at fixed $u$, as
$W_\sigma(\mathbf z)=\sum_\nu w_{\sigma,\nu}\mathbf z^\nu$ and define

$$
 L_\sigma=\sum_\nu |\nu|\,|w_{\sigma,\nu}|,
 \qquad L=\max(L_+,L_-).
 \tag{18}
$$

These are finite, explicitly computable constants from the displayed
quartic; for (1) each polynomial has only 25 nonzero monomials. On the
physical cube $[-1,1]^7$, its gradient has $\ell_1$ norm at most
$L_\sigma$. If every endpoint occupation probability differs from the
target by at most $\delta$, the means differ by at most $2\delta$.
The necessary zero in (13) and the target value (16) imply

$$
 \max_{w\in\mathcal W_7}
 |P_{\rm rival}(S=+1\mid w)-P_*(S=+1\mid w)|
 \ \ge\ \frac{\Delta}{2L}>0.
 \tag{19}
$$

This is an all-parameter quantitative theorem against uncapped ordinary
rivals. It requires no computer-assisted premise, though its coarse
global bound can be improved substantially by bounding the polynomial
only near the specified target data.

## 5. A rational local certificate for occupation error $1/2000$

At (1), the mean drift coefficients are rational:
$A(H)=B(H)=20/41$, while the zero-field coupling is $4/5$. The target
generators are therefore rational, despite the notation $J=H=\log3$.
The clock duration is the rational number two.

For orientation, the seven target means are approximately

| Word | Target mean |
|---|---:|
| $H$ | $0.487382120217$ |
| $H^2$ | $0.654943412382$ |
| $H^3$ | $0.731619808115$ |
| $H\,0$ | $0.251853834636$ |
| $H^2\,0$ | $0.374681009050$ |
| $H\,0\,H$ | $0.593244622764$ |
| $H^2\,0\,H$ | $0.645548833751$ |

The displayed decimals are explanatory, not the numerical certificate.
The certificate uses the following reproducible enclosure, with no floating
exponential or fitting in the verification:

1. Build the physical four-state generators exactly from their heat-bath
   rates. For $X_h=2Q_h$, the maximum absolute row-sum norms are $36/5$ and
   $1548/205$ at the two fields.
2. Evaluate $T_{96}(X_h)=\sum_{j=0}^{96}X_h^j/j!$ in exact rational
   arithmetic. If $r=\|X_h\|_\infty$, bound the full omitted series by
   $r^{97}/[97!(1-r/98)]$. This is below $2^{-180}$ for both matrices.
3. Round each retained entry to the nearest multiple of $2^{-160}$. The
   rounding error is at most $2^{-161}$, so an interval of radius
   $2^{-160}$ around that rounded entry encloses the true exponential.
4. Propagate those rational entry intervals through the at most four ticks
   of each word, with the exact stationary preparation and binary readout.
   Round each final interval midpoint to a multiple of $2^{-128}$. The
   certificate checks that all seven exact means are within
   $\eta=2^{-120}$ of those rational centers. Their exact fractions are
   included in the report.

The geometric tail in step 2 is valid because the ratio of successive
scalar tail terms is at most $r/98<1$. Step 4 uses outward exact interval
arithmetic, so dependence between repeated matrices can only enlarge the
enclosure. No independence assumption is made.

The certificate then translates the two exact polynomials:

$$
 W_\sigma(\mathbf z_c+\mathbf y)
 =\sum_\nu c_{\sigma,\nu}\mathbf y^\nu.
 \tag{20}
$$

If the center error is at most $\eta$ in each mean, a rival with occupation
error at most $1/2000$ lies in the box $|y_i|\le\rho=1/1000+\eta$.
All coefficients in (20), including the constant, are rational. The exact
test is

$$
 |c_{\sigma,0}|>
 \sum_{\nu\ne0}|c_{\sigma,\nu}|\rho^{|\nu|}
 \quad\text{for both }\sigma=\pm1.
 \tag{21}
$$

It excludes a zero anywhere in either box. The verified conservative
rational bounds are

$$
\begin{aligned}
 |c_{\sigma,0}|&>\frac{1455}{10^7},\\
 \sum_{\nu\ne0}|c_{-,\nu}|\rho^{|\nu|}
 &<\frac{1436}{10^7},\\
 \sum_{\nu\ne0}|c_{+,\nu}|\rho^{|\nu|}
 &<\frac{425}{10^7}.
\end{aligned}
\tag{22}
$$

This bounded rational computation supplies an essential numerical premise
for the stated $1/2000$ threshold. It is not a simulation or a fit over a
restricted rival family. The universal lower bound follows analytically
from the necessary polynomial identity and (21).

### A certified ordinary three-state upper on the same menu

For comparison, take readout $(-1,1,1)$ and the rational baseline law

$$
 \pi_0=\left(\frac12,\frac{61258}{10^6},\frac{438742}{10^6}\right),
 \qquad \pi_H=\pi_0(1+\tfrac45S).
 \tag{23}
$$

Specify symmetric stationary fluxes for pairs $(1,2),(1,3),(2,3)$ by

| Field | $10^6\pi_h(1)Q_h(1,2)$ | $10^6\pi_h(1)Q_h(1,3)$ | $10^6\pi_h(2)Q_h(2,3)$ |
|---|---:|---:|---:|
| $0$ | $110734$ | $2$ | $72990$ |
| $H$ | $34039$ | $15082$ | $50885$ |

For each pair, define both directed rates by dividing its displayed flux
by the source stationary mass; diagonals are minus row sums. This defines
one shared model, with exact detailed balance and strictly positive rates.
Its maximum exit rate is $91862/30629<3$.

The certificate encloses these two propagators by the same procedure, using
Taylor degree 128. Their row norms are $367448/30629$ and $94360/30629$;
the respective tail bounds are again below $2^{-180}$. Exact interval
comparison on all seven words proves that its maximum occupation error is
less than $1/1000$ (indeed less than $837/10^6$).

These rational parameters originated from a separate bounded fit. Their
validity and the upper error bound depend only on the explicit rates and
the exact certificate, not on the optimizer. This upper bound is restricted
to the seven specified experiments. No eleven-word or all-protocol upper
approximation is asserted.

The verification can be reproduced with

```bash
python scripts/verify_familiar_switch_margin.py --output /tmp/familiar_switch_margin.json
```

It uses only exact standard-library rational arithmetic. The report records
the response ordering, exact centers, coefficient-box bounds, explicit
ordinary model, and proof/source hashes.

## 6. Meaning and limits

The result concerns a familiar four-configuration target and short field
pulses. It makes the ordinary-reversibility cost quantitative with seven
means and an explicitly checkable tolerance. The exact three-state upper
is the same stationary, generally nonreversible predictor already proved
for this target family; the four-state physical target is an ordinary
upper. Every stationary two-state chain is ordinarily reversible, so the
same exclusion proves that two unrestricted states do not suffice at the
claimed tolerance.

The certified quantity is an error in endpoint occupation probabilities.
It is not a statement about individual trajectories, a measurement-noise
model, or a practical sample count. The lower tolerance is 0.05 percentage
points, and an explicit ordinary three-state model fits these same
experiments within 0.1 percentage points. The theorem therefore does not
establish a one-percentage-point advantage and does not identify the
optimal approximation error.

No proof of irreversibility of a physical molecule is inferred. The target
itself obeys ordinary detailed balance; the result compares state counts
of predictive models under the specified shared force-response constraint.
