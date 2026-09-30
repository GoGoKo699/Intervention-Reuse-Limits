# Three experiments expose a finite-pulse memory requirement

**Convergence checkpoint, 30 September 2026.** Two held-field experiments
and one specified alternating pulse train already force a third predictive
state at intermediate accuracy. Every reusable two-state Markov model
obeys an exact multiplication rule for its conditional contrasts. The
two-switch target violates that rule at first order in the inverse
hidden-to-visible rate ratio, while the existing reversible three-state
model has second-order error on the same experiments.

This closes the finite-pulse question in the
[core assessment](CONTROL_ACCURACY_CORE_ARGUMENT.md). It uses the existing
physical model, preparation and endpoint observations. The number of
experiment settings is three; the pulse train contains a growing number
of segments. Finite pulse spacing is established within the ideal-jump
model, without a finite-ramp or device-performance claim.

## 1. A fixed three-experiment recipe

Use the [heat-bath target](FAMILIAR_SWITCH_FAST_RELAXATION.md), with fixed
$`t=\tanh J\in(0,1)`$, $`u=\tanh H\in(0,1)`$ and rate ratio
$`r=\Gamma_Z/\Gamma_S`$. Time is measured in $`1/\Gamma_S`$.
The target starts in $`\pi_0(S,Z)=(1+tSZ)/4`$, and only the true initial
and final signs of $`S`$ are recorded. Put

**Equation (1).**

```math
c_0=1-t^2,\qquad c_1=\frac{1-t^2}{1-t^2u^2},\qquad
\bar c=\frac{c_0+c_1}{2},\qquad
\chi=\frac{(c_1-c_0)^2}{2}\tanh\frac12\gt 0.
```

For $`r\ge2`$, set $`n=\lceil r/2\rceil`$, $`A=n/r`$ and $`T=2A`$.
Let $`L_a,H_a`$ denote a hold at field $`0,H`$ for duration $`a`$.
The entire menu is

**Equation (2).**

```math
\mathcal W_r=\{L_A,\ H_A,\ W_r\},\qquad
W_r=(L_{1/r}H_{1/r})^n.
```

The pulse train has exactly $`2n`$ held segments and $`2n-1`$ field changes.
Its duration satisfies $`1\le T\lt 1+2/r\le2`$. Each calibration hold has
the same duration as the total residence at that field in the pulse train.
There are no intermediate observations or feedback.

For a target word $`w`$, define its visible contrast by

**Equation (3).**

```math
C_w=\frac{\mathbb E[S_{\rm final}\mid S_0=+1]
                 -\mathbb E[S_{\rm final}\mid S_0=-1]}2,
\qquad F_r=C_{W_r}-C_{L_A}C_{H_A}.
```

Let $`E_2(r)`$ be the infimum maximum endpoint-pair TV error on this menu
over all models with at most two persistent Markov states, fixed
deterministic binary readout and one fixed continuous-time generator per
field. Preparation may vary arbitrarily with the whole word. No detailed
balance, Gibbs relation, stationary preparation or rival rate cap is imposed.

**Theorem.** For this finite menu,

**Equation (4).**

```math
E_2(r)\ge\frac{|F_r|}{12},\qquad
F_r=\frac{e^{-\bar c}\chi}{r}+O(r^{-2}),\qquad
E_2(r)=\Theta(r^{-1}).
```

The constants in the asymptotic statement keep $`t,u`$ fixed. The
[existing reversible three-state construction](FAMILIAR_SWITCH_RAPID_CONTROL.md)
on the same menu satisfies

**Equation (5).**

```math
E_3^{\rm rev}(r)\le\frac{2(1-\alpha)}{r^2},\qquad
\alpha=\frac{1-t^2}{1-t^2u}.
```

Consequently three states are necessary and sufficient when the allowed
error obeys $`r^{-2}\ll\epsilon(r)\ll r^{-1}`$. This restricted menu
does not establish a matching three-state lower or fourth-state necessity.
Those remain separate results for the earlier seven-word and all-word tasks.

## 2. An exact rule excludes every two-state model

A rival that has both visible signs has one state per sign. Its conditional
final mean for any word has the form

**Equation (6).**

```math
\mathbb E[\widehat S_{\rm final}\mid\widehat S_0=s]
=a_ws+b_w,\qquad
a_w=\exp\!\left[-\sum_j\kappa_j\tau_j\right]\in[0,1],
\quad |b_w|\le1,
```

where $`\kappa_j`$ is the sum of its two transition rates at the held field.
Zero generators are included. Since (2) gives identical total residence
times field by field,

**Equation (7).**

```math
a_{W_r}=a_{L_A}a_{H_A}.
```

This identity holds for every choice of rates and stationary means.
It uses reuse of the same two generators, not a fit or rate identification.

Arbitrary word-dependent preparation does not evade the test. Suppose
the rival pair law at a word is within TV distance $`\delta`$ of the target.
The target's initial sign is balanced, so the rival's initial mean
$`\mu_w`$ satisfies $`|\mu_w|\le2\delta`$. Its pair correlation is
$`a_w+\mu_wb_w`$, while the target correlation is $`C_w`$. The correlation
error is at most $`2\delta`$. Hence

**Equation (8).**

```math
|C_w-a_w|\le4\delta.
```

Using (7), $`|C_{L_A}|,|C_{H_A}|\le1`$ and $`a_w\in[0,1]`$ gives
$`|F_r|\le12\delta`$. A model with only one visible sign already has
pair error at least $`1/2`$, so it also satisfies (4). Taking the infimum
proves the exact finite-$`r`$ lower without conditional-probability division,
preparation restrictions or compactness assumptions on the rates.

## 3. Hidden lag produces a nonzero finite-train residual

The [exact mean closure](FAMILIAR_SWITCH_RAPID_CONTROL.md#3-one-change-of-mean-coordinates-controls-every-word)
uses $`x=\mathbb E[S]`$ and $`v=\mathbb E[Z]/t-x`$. Taking half the
difference between the two initial-sign solutions cancels the affine
field forcing. Write these contrast coordinates as $`C,V`$. During a hold,

**Equation (9).**

```math
C'=-cC+(1-c)V,\qquad
V'=cC-(r+1-c)V,\qquad C(0)=1,\quad V(0)=0,
```

with $`c=c_0`$ or $`c_1`$. The cooperative equations give $`C\gt 0,V\ge0`$.
Set $`\varepsilon=1/r`$, use fast time $`\sigma=r\theta`$, and put
$`w=rV/C`$. Direct differentiation gives

**Equation (10).**

```math
\frac{dw}{d\sigma}
=c-w+\varepsilon(2c-1)w-\varepsilon^2(1-c)w^2,
\qquad
\frac{d\log C}{d\sigma}
=-\varepsilon c+\varepsilon^2(1-c)w.
```

For $`\varepsilon\le1/2`$, the interval $`0\le w\le2`$ is invariant:
the drift is positive at zero and at most $`-1+2\varepsilon`$ at two.
Let $`y'=c-y`$, $`y(0)=0`$, with primes now in fast time. Variation of
constants and (10) imply

**Equation (11).**

```math
|w-y|\le2\varepsilon+4\varepsilon^2\le4\varepsilon.
```

For the unit-low/unit-high square wave in fast time, let $`z`$ be the
unique period-two solution of $`z'=c-z`$. It lies between $`c_0,c_1`$,
and $`y-z=-z(0)e^{-\sigma}`$. Therefore

**Equation (12).**

```math
|w-z|\le4\varepsilon+e^{-\sigma}.
```

The period solution is explicit. With $`q=e^{-1}`$ and $`d=c_1-c_0`$,
its low-interval initial value is $`c_0+d/(1+q)`$; its high-interval
initial value is $`c_1-d/(1+q)`$. Integrating each exponential yields

**Equation (13).**

```math
\int_0^2(1-c)z\,d\sigma
=c_0(1-c_0)+c_1(1-c_1)+2\chi.
```

The extra $`2\chi=d^2(1-q)/(1+q)`$ is strictly positive. Equivalently
it is $`\int_0^2(z')^2\,d\sigma`$: periodicity gives
$`\int z'=\int zz'=0`$ and $`c=z+z'`$. The lag across field changes
is the source of the residual.

Integrating (10) over the $`n`$ complete periods, and using (12), gives

**Equation (14).**

```math
\log C_{W_r}
=-(c_0+c_1)A
 +\varepsilon A[c_0(1-c_0)+c_1(1-c_1)+2\chi]+R_W,
\quad |R_W|\le\varepsilon^2(4T+1).
```

For a calibration hold the same calculation uses the constant solution
$`z=c_j`$ and gives

**Equation (15).**

```math
\log C_{j,A}=-c_jA+\varepsilon A c_j(1-c_j)+R_j,
\quad |R_j|\le\varepsilon^2(4A+1).
```

Thus there is no uncontrolled first-order initial transient. Subtracting,

**Equation (16).**

```math
\log\frac{C_{W_r}}{C_{L_A}C_{H_A}}
=\frac{T\chi}{r}+R,\qquad
|R|\le\frac{8T+3}{r^2}\le\frac{19}{r^2}.
```

Since $`T=1+O(r^{-1})`$ and $`C_{L_A}C_{H_A}=e^{-\bar c}+O(r^{-1})`$,
exponentiation proves the expansion in (4). The
[adiabatic two-state upper](FAMILIAR_SWITCH_FAST_RELAXATION.md)
$`t^2/[r(1-t^2)]`$ applies to every word and completes $`E_2=\Theta(r^{-1})`$.

For completeness, a conservative fully explicit version follows from
(16): if $`r\ge\max\{2,38/\chi\}`$, then

**Equation (17).**

```math
E_2(r)\ge\frac{e^{-2}\chi}{24r}.
```

Indeed the log ratio is at least $`\chi/(2r)`$, and (10) with $`w\ge0`$
gives $`C_{L_A}C_{H_A}\ge e^{-(c_0+c_1)A}\ge e^{-2}`$.
This sufficient onset is deliberately loose; it is not a proposed
operating point or an optimized experimental threshold.

## 4. What this closes, and where the project stops

The previous lower used arbitrarily rapid product and long-time limits.
Here the dwell, segment count and observation horizon are specified for
every $`r`$. The scientific statement is simple: two-state held-field
responses cannot be reused to reproduce the finite pulse response to
first-order accuracy. A third reversible state retains the missing lag.
The three calibration/drive settings constitute a concrete consistency
test, not a numerical search over candidate fits.

Timing costs remain explicit. If $`\Gamma_Z`$ is held admissible and
$`\Gamma_S=\Gamma_Z/r`$, each pulse lasts $`1/\Gamma_Z`$ physically,
each calibration lasts $`n/\Gamma_Z`$, and the pulse train lasts
$`2n/\Gamma_Z\sim r/\Gamma_Z`$. The number of switches grows with $`r`$.
Thus this is finite switching rate with ideal field jumps, not a claim
of bounded Fourier bandwidth or a fixed short sequence. Finite ramps,
detectors and sampling costs have not been added to the theorem.

This result strengthens the finite-control interpretation of the
existing accuracy hierarchy. It neither enlarges the fourth-state
equilibrium penalty nor establishes hardware memory, heat savings,
device feasibility or a large practical error gap. The cited earlier
assessment retains the primary-source comparison; this proof introduces
no broader priority claim.

**Convergence decision:** the selected analytic gate is closed. Freeze
the physical model, observation contract and theorem scope. The next
work is a bounded consistency and presentation pass over the established
core argument and evidence, using the existing source comparison.
Open implementation questions remain stated limitations; they do not
automatically become new research branches. No simulation, optimizer,
new numerical verifier or acquisition refinement is needed here.
Manuscript drafting remains last.
