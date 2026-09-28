# Where an equilibrium-specific prediction error can remain observable

Comparable hidden and visible rates alone do not guarantee a useful
fourth-state penalty. For the familiar two-spin task, explicit reversible
three-state models show that weak coupling, weak driving, saturating
driving, and several strong-coupling regimes all suppress the error.
These are bounds on the best model over entire protocol families, not
observations from a parameter search.

The resulting design restriction is physical: hidden response must remain
variable within both visible signs and must affect the requested
prediction before the available observation time expires. Increasing a
field or coupling without limit is not an unconditional way to expose
that variation. The remaining interior window is a candidate region;
the bounds do not establish a large or experimentally useful gap there.

## 1. Comparison and analytic screening rule

Retain the [rapid-control task](FAMILIAR_SWITCH_RAPID_CONTROL.md):
$t=\tanh J\in(0,1)$, $u=\tanh H\in(0,1)$, rate ratio
$r=\Gamma_Z/\Gamma_S>0$, target low-equilibrium preparation and true
initial/final sign records. Controls are arbitrary finite words at the
two fields $0,H$. All rates are in visible-attempt units.

Let $E_3^{\rm all}$ be the infimum all-word pair-TV error over ordinary
reversible models with at most three persistent states, fixed reused
continuous-time generators, deterministic binary readout, a common
unknown Gibbs tilt and arbitrary word-dependent preparation. Let
$E_{3,T}$ restrict total active time to at most $T$. No rival rate cap
or mass floor is assumed. Each upper below exhibits an admissible model;
its chosen preparation does not restrict the other rivals.

Before calling a fourth-state requirement an equilibrium-specific cost,
check that the corresponding general three-state prediction is possible.
The [new exact one-sided boundary](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md)
gives this condition, even without a Gibbs or common-preparation premise
on the general rival:

$$
r\ge r_*(t,u)=\frac{u(1+t^2+2t^2u)}{2(1+u)}.
\tag{1}
$$

Below it, the exact general and ordinary minima are both four. Above it,
the general minimum is three and the ordinary minimum is four, but their
finite-accuracy distinction remains a separate question.

Write

$$
c_m=\frac{1-t^2}{1-t^2m^2},\qquad
\alpha=\frac{1-t^2}{1-t^2u},\qquad
R=\frac{r+1+\sqrt{(r+1)^2-4\alpha r}}2,\quad \eta=r/R.
$$

The analytic upper envelope is

$$
\boxed{
E_3^{\rm all}\le U(t,u,r):=
\min\left\{
1,\frac{t^2}{r(1-t^2)},
\frac{t^2u(1-u)}{2(r+1)(1-t^2u^2)^2},
\frac{(1-\eta)c_u}{2(r+1)}
\right\}.}
\tag{2}
$$

For a time budget, a further construction gives

$$
\boxed{E_{3,T}\le
\min\left\{U(t,u,r),
(1-t)\left[\frac14+\frac{T\max\{1,r\}}2\right]\right\}.}
\tag{3}
$$

The minimum may select different models; no single model is claimed to
attain all terms. If this upper is at most a proposed prediction
tolerance $\delta$, a fourth state cannot be necessary at that tolerance
for the stated task. Conversely, if the existing seven-word lower
$f(r)/(12+2f(r))$ exceeds $\delta$, it excludes every ordinary
three-state rival. For (3), those witnessing words must fit within $T$.
Between these sufficient bounds the best error remains undetermined.
No particular scientifically acceptable tolerance is supplied by algebra.

## 2. Reachable hidden lag controls the error

Condition on initial sign $s$ and put $y_s=z_s/t$. The exact target is

$$
x_s'=-x_s+(1-c_m)y_s+c_m m,\qquad
y_s'=r(x_s-y_s),\qquad x_s(0)=y_s(0)=s.
$$

Split mean and initial-sign contrast:
$x_s=\bar x+sC$, $y_s=\bar y+sD$, and
$y_s-x_s=V+sW$. The mean starts at $(0,0)$ and stays in $[0,u]^2$;
the homogeneous contrast starts at $(1,1)$ and stays in $[0,1]^2$.
These squares are invariant because the drift points inward at each
face for either field. Also

$$
W'=c_m C-(r+1-c_m)W
$$

preserves $W\ge0$. Rewriting the two lag equations gives

$$
V'=c_m(\bar y-m)-(r+1)V,\qquad
W'=c_m D-(r+1)W.
$$

Variation of constants therefore yields uniformly over all words

$$
|V|\le\frac{u c_u}{r+1},\qquad
0\le W\le\frac{c_u}{r+1}.
\tag{4}
$$

For two models with balanced initial signs, if their conditional final
mean differences are $A+sB$, their complete pair-TV distance is exactly

$$
\frac{|A+B|+|A-B|}{4}
=\frac12\max\{|A|,|B|\}.
\tag{5}
$$

This retains the relation between the two conditional experiments,
rather than treating their errors as unrelated worst cases.

## 3. Both weak and saturating fields permit accurate equilibrium reduction

Set $K_0=(1-t^2)/t^2$. Use three states with

$$
\widehat S=(-1,1,1),\quad G=(0,-2,K_0),\quad
\widehat\pi_0=
\left(\frac12,\frac{K_0}{2(K_0+2)},\frac1{K_0+2}\right).
$$

Choose the positive path rates

$$
q_{12}^{(m)}=\frac{c_m(1+m)}2,\qquad
q_{21}^{(m)}=\frac{c_m(1-m)(K_0+2)}{2K_0},
$$

$$
q_{23}=\frac{2r}{K_0+2},\qquad
q_{32}=\frac{K_0r}{K_0+2},\qquad q_{13}=q_{31}=0.
\tag{6}
$$

The diagonals are minus the exit rates. Edgewise detailed balance holds
for $\widehat\pi_m=\widehat\pi_0(1+m\widehat S)$: the two edge
fluxes are respectively $c_m(1-m^2)/4$ and
$(1+m)K_0r/(K_0+2)^2$. Prepare the chain in its common low law;
the conditional mean of $G$ is zero for both signs.

Define

$$
\alpha_m=c_m\left[1+\frac{1-m}{K_0}\right]
=1-\beta_m,\qquad
\beta_m=\frac{t^2m(1-m)}{1-t^2m^2}.
$$

Direct application of (6), with conditional means
$X=\mathbb E\widehat S$ and $Y=X+\mathbb E G$, gives

$$
X'=-\alpha_m X+(\alpha_m-c_m)Y+c_m m,\qquad
Y'=r(X-Y).
$$

Thus errors $e=X-x$, $g=Y-y$ obey

$$
\binom{e'}{g'}=
\begin{pmatrix}-\alpha_m&\alpha_m-c_m\\r&-r\end{pmatrix}
\binom e g+
\binom{-\beta_m(y-x)}0.
\tag{7}
$$

The off-diagonal entries are nonnegative. For forcing magnitude at most
$F$, the square $[-F/c_0,F/c_0]^2$ is invariant: the first-coordinate
boundary drift is bounded by $-c_mF/c_0+F\le0$, and the second
coordinate points inward. Apply this separately to the mean and contrast
components, with forcing bounds from (4). Since $\beta_0=0$, (5) gives

$$
\sup_w\operatorname{TV}(P_w,\widehat P_w)
\le\frac{\beta_u c_u}{2c_0(r+1)}
=\frac{t^2u(1-u)}{2(r+1)(1-t^2u^2)^2}.
\tag{8}
$$

This proves the field term in (2) for every $r>0$, with no dwell floor
or horizon restriction. At fixed $t,r$, it vanishes linearly as $u\to0$
or $u\to1$. Weak driving supplies little contrast. Saturating driving
makes the high-field visible flip insensitive to the hidden sign.
The formal endpoint $u=1$ is not a finite field; the theorem concerns
strictly $u<1$ and convergence to that limit. The constants are not
uniform at the joint corner $t,u\to1$.

## 4. Strong coupling and the observation-time cost

For the preceding [exact-coordinate three-state model](FAMILIAR_SWITCH_RAPID_CONTROL.md),
the conditional visible error is $(1-\eta)(V+sW)$. Equations (4)–(5)
give the last term in (2). Since $R\le r+1$,
$1-\eta\le1/(r+1)$, and therefore

$$
E_3^{\rm all}\le
\frac{1-t^2}{2(r+1)^2(1-t^2u^2)}.
\tag{9}
$$

At fixed $u<1,r>0$, strong coupling suppresses the error uniformly
over every horizon and switching schedule. Merely waiting longer does
not evade this bound. The weak-coupling term in (2) is the inherited
[adiabatic two-state upper](FAMILIAR_SWITCH_FAST_RELAXATION.md).

If the high field grows with the coupling, use a different argument.
Delete the physical state $D_*=(-1,+1)$, retain the other three states
and every rate between them, and adjust the diagonals. The retained
path remains reversible for the target Gibbs law conditioned on that
subset. These stationary laws obey the same normalized Gibbs tilt rule.
Map initial mass at $D_*$ to $(-1,-1)$; this preserves the initial
visible sign and gives one balanced preparation. Its stationarity is
not required by the comparison class.

The initial mismatch probability is $(1-t)/4$. At any nonnegative
field, entrances into the deleted state occur from $(-1,-1)$ at rate
$r(1-t)/2$, or from $(+1,+1)$ at rate
$[1-\tanh(J+h)]/2\le(1-t)/2$. No other state enters it.
Coupling the two chains until the first such entrance bounds the mismatch
probability by

$$
\frac{1-t}{4}+\frac{(1-t)T\max\{1,r\}}2,
$$

proving (3). This term applies to arbitrary nonnegative field values,
even if they grow with $J$, and is independent of switch count.

At fixed finite $r$, a nonvanishing separation as $t\to1$ consequently
requires $T=\Omega((1-t)^{-1})$ in the jointly growing-field corner.
This is a necessary observation-time cost, not proof that such long
protocols achieve a separation. The rare-state coupling bound alone
does not give a vanishing all-horizon bound in that joint limit.
The physical active duration is $T/\Gamma_S$; preparation and readout
overhead are not included in this horizon.

For completeness, there is also a parameter-uniform ceiling. Since
$c_u\le\alpha$ and $\alpha\eta^2=(r+1)\eta-r$,

$$
\alpha(1-\eta)=\frac1{4r}
-\frac{[(2r+1)\eta-2r]^2}{4r\eta^2}\le\frac1{4r},
\qquad E_3^{\rm all}\le\frac1{8r(r+1)}.
$$

The equal-rate value $1/16$ is only a ceiling, not an attained error
or an experimentally justified tolerance.

## 5. Scientific consequence and source scope

The relevant use is deciding whether a fitted equilibrium kinetic model
can be reused under intervention at an accepted prediction tolerance.
For this four-state target, adding one state is computationally trivial;
three and four states even fit in the same number of fixed binary bits.
A practical storage or heat advantage has not been established.

The bounds give an analytic way to reject proposed regimes before
simulation. At fixed parameters, neither arbitrarily weak nor saturating
driving helps. Weak coupling removes the response, while strong coupling
either admits a uniform reduction or requires a growing observation
horizon in the remaining joint corner. Slow hidden dynamics can also
cross (1), where general prediction itself requires four states. None
of these restrictions proves a substantial interior gap.

Structure-preserving reduction is established methodology.
Grigoletto, Viola and Ticozzi,
[*Model Reduction for Controlled Quantum Markov Dynamics*](https://arxiv.org/html/2510.25546v1),
Section III-B, Proposition 2 and Theorem 1, construct valid controlled
reductions; the following paragraph limits minimality to that procedure.
Their outlook also discusses restricted preparations. Fornace and Lindsey,
[*An approximation theory for Markov chain compression*](https://arxiv.org/html/2506.22918v3),
Lemma 4.1 and Theorem 3, construct reversible induced chains and quantify
autonomous approximation. These sources do not state the present
all-realization controlled state minima. The explicit bounds here use
standard invariant-region and coupling arguments; the additional result
is their application to this shared physical interface and its exact
positive-realization boundary. This focused comparison is not an
exhaustive novelty audit.

The two-field all-word bounds do not automatically cover finite ramps
or an interval of intermediate fields. The rare-state bound has its
separately stated broader nonnegative-field scope. All statements concern
ideal endpoint pairs from the specified target preparation; detector
errors, intermediate observations, feedback and path laws remain distinct.
No new simulation, optimizer, verifier or sampling certificate is added.

The remaining physical question is whether a robust interior regime,
or the long-time jointly strong-coupling/strong-field regime, produces
a consequential equilibrium-specific prediction error. An approximate
three-state model can also disprove that possibility. Its answer should
come from the mechanism of hidden response and a justified prediction
tolerance, rather than another isolated numerical operating point.
