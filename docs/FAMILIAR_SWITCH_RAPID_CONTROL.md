# Rapid two-field control retains the quadratic equilibrium precision scale

Faster switching does not amplify the four-state equilibrium requirement
to first order in the fast-hidden regime. One explicit reversible
three-state chain approximates **every finite two-field endpoint-pair
experiment**, with no minimum dwell, pulse-count or horizon restriction,
to error of order $`r^{-2}`$. The existing seven-word lower bound matches
that order. A two-state model has a larger, first-order error when all
these rapid protocols must be reproduced by the same generators.

Thus rapid control changes how many states are needed to retain the
leading memory correction. The equilibrium-specific fourth-state
obstruction remains at the next precision order. This is an analytic
model-reduction result; no simulation, fitted example or new acquisition
certificate is used.

## 1. Task and result

Use the [two-spin heat-bath model](FAMILIAR_SWITCH_FAST_RELAXATION.md),
with fixed $`t=\tanh J\in(0,1)`$, $`u=\tanh H\in(0,1)`$,
$`r=\Gamma_Z/\Gamma_S`$, and time in units of $`1/\Gamma_S`$.
The target starts in $`\pi_0(S,Z)=(1+tSZ)/4`$. Each experiment records
only its true initial and final visible signs. A word is any predetermined
finite sequence of fields $`0,H`$ and nonnegative held durations. Field
changes leave the state unchanged. There are no intermediate records or
feedback.

Let $`E_d^{\rm all}(r)`$ be the infimum maximum endpoint-pair TV error
over ordinary reversible continuous-time Markov models with at most $`d`$
complete persistent states. One fixed generator per field and a fixed
deterministic binary readout are reused throughout. The stationary laws
are normalized and nonnegative, with

```math
\widehat\pi_H(i)=
\frac{\widehat\pi_0(i)(1+v\widehat S(i))}
 {1+v\widehat\pi_0\widehat S},\qquad v\in(-1,1).
```

The tilt is unknown and need not equal $`u`$. Preparation may depend on
the entire scheduled word and previous history. Preparable zero-weight
transients count. No rival rate cap, mass floor or preparation-equilibrium
promise is imposed. The supremum is over all finite words, and the
infimum selects one reusable model, not a new fit for each word.

At fixed $`t,u`$, as $`r\to\infty`$,

**Equation (1).**

```math
\boxed{E_2^{\rm all}(r)=\Theta(r^{-1}),\qquad
E_3^{\rm all}(r)=\Theta(r^{-2}),\qquad E_4^{\rm all}(r)=0.}
```

The two-state lower holds even without a Gibbs relation or detailed
balance. The three-state lower is inherited from the broader stochastic
kernel null of the [quadratic-precision proof](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md).
Continuous-time generators specify how this new all-duration task reuses
one model across different dwells.

| Reusable reversible model | Fixed positive clock, all finite words | Arbitrary two-field dwells, all finite words |
| --- | --- | --- |
| At most two states | $`\Theta(r^{-2})`$ | $`\Theta(r^{-1})`$ |
| At most three states | $`\Theta(r^{-2})`$ | $`\Theta(r^{-2})`$ |
| At most four states | Exact | Exact |

The first column follows from the preceding quadratic-precision theorem.
Neither column locates optimal constants or finite-rate transition points.

## 2. An explicit reversible three-state chain

For the two permitted tilts $`m\in\{0,u\}`$, set

```math
c_m=\frac{1-t^2}{1-t^2m^2},\qquad
\alpha=\frac{1-t^2}{1-t^2u},\qquad
K=\frac{1-t^2u}{t^2u}.
```

Here $`0\lt c_0\lt c_u\lt \alpha\lt 1`$, $`K\gt 0`$, and the essential two-field
identity is

**Equation (2).**

```math
\alpha-c_m=\frac{c_m(1-m)}K,
\qquad m=0,u.
```

Define

**Equation (3).**

```math
R=\frac{r+1+\sqrt{(r+1)^2-4\alpha r}}2,\qquad
\eta=\frac rR.
```

The larger root satisfies $`R\gt \max\{r,1\}`$, so $`0\lt \eta\lt 1`$.
It also satisfies $`R+\alpha\eta=r+1`$.

Take three states with readout and auxiliary observable

**Equation (4).**

```math
\widehat S=(-1,1,1),\qquad G=(0,-2,K),
\qquad
\widehat\pi_0=
\left(\frac12,\frac{K}{2(K+2)},\frac1{K+2}\right).
```

Only neighboring states communicate. The four nonzero off-diagonal
rates are

**Equation (5).**

```math
\begin{aligned}
q_{12}^{(m)}&=\frac{\eta c_m(1+m)}2,&
q_{21}^{(m)}&=\frac{\eta c_m(1-m)(K+2)}{2K},\\
q_{23}^{(m)}&=\frac{2R}{K+2},&
q_{32}^{(m)}&=\frac{KR}{K+2}.
\end{aligned}
```

Set $`q_{13}=q_{31}=0`$ and the diagonals to minus the exit rates.
Every displayed rate is positive for every $`r\gt 0`$. The chain is
irreducible. Its strictly positive stationary law is

**Equation (6).**

```math
\widehat\pi_m(i)=\widehat\pi_0(i)(1+m\widehat S(i)).
```

It is normalized because the low law has balanced signs. Detailed
balance follows edge by edge: the $`1`$–$`2`$ rate ratio is
$`K(1+m)/[(K+2)(1-m)]`$, and the $`2`$–$`3`$ ratio is $`2/K`$,
exactly the corresponding stationary-weight ratios. Thus this is an
admissible equilibrium model with the actual target tilt.

Prepare it in its one common low-field equilibrium law. Conditional on
either initial sign, its auxiliary mean is zero: on the plus sector,
the weights $`K/(K+2),2/(K+2)`$ average $`-2,K`$ to zero. This choice
constructs the upper bound without restricting the allowed null
preparations.

## 3. One change of mean coordinates controls every word

Condition on the initial sign and write the target means as $`x,z`$.
Put $`v=z/t-x`$. The exact target equations are

**Equation (7).**

```math
x'=-c_m(x-m)+(1-c_m)v,\qquad
v'=c_m(x-m)-(r+1-c_m)v,
\qquad x(0)=\pm1,\quad v(0)=0.
```

The hidden lag also obeys $`v'=-rv-x'`$. Since the visible heat-bath
drift has magnitude at most two, variation of constants gives

**Equation (8).**

```math
|v(\theta)|\le\frac2r
```

at every time, independently of the field word.

Direct application of (5), using (2), gives

```math
\widehat Q_m\widehat S
=-\eta c_m(\widehat S-m)+\eta(\alpha-c_m)G,
```

**Equation (9).**

```math
\widehat Q_m G
=\eta c_m(\widehat S-m)
 -[R+\eta(\alpha-c_m)]G.
```

Substitute

**Equation (10).**

```math
\widehat x=x+(1-\eta)v,\qquad \widehat g=\eta v.
```

Equations (7) and $`R+\alpha\eta=r+1`$ give exactly the mean equations
(9), with the correct conditional initial data. This single coordinate
change is independent of the current field. The means and transformation
remain continuous at every switch, so uniqueness of the linear evolution
proves (10) across any finite word. It is an identity of conditional
means; the model's actual readout remains the deterministic sign in (4).

For each initial sign, the final binary-law TV error is half the mean
error. Both initial signs have mass $`1/2`$, hence

**Equation (11).**

```math
\boxed{\sup_w\mathrm{TV}(P_w,\widehat P_w)
\le\min\left\{1,\frac{1-\eta}{r}\right\}.}
```

The quadratic equation for $`\eta`$ implies

```math
(1-\eta)(r-\eta)=(1-\alpha)\eta^2.
```

Consequently, for $`r\ge2`$,

**Equation (12).**

```math
\frac{1-\eta}{r}
\le\frac{1-\alpha}{r(r-1)}
\le\frac{2(1-\alpha)}{r^2},
\qquad r(1-\eta)\longrightarrow1-\alpha\gt 0.
```

There is no accumulation with pulse count or elapsed time. The residual
error is a small change of the visible mean coordinate multiplied by an
already small hidden lag.
Since $`0\lt 1-\alpha\lt 1`$, the upper is also at most $`2/r^2`$ uniformly
over all $`t,u\in(0,1)`$, including parameters that vary with $`r`$.
The matched lower order below keeps $`t,u`$ fixed; its coefficient need
not stay positive uniformly as they approach the boundary.

Choose any two fixed positive dwells and include the seven words of the
preceding theorem. Its determinant magnitude $`f(r)`$ satisfies
$`r^2f(r)\to C_F\gt 0`$, and every admissible three-state rival has error
at least $`f(r)/(12+2f(r))`$. These words are included in the present
supremum. Together with (11)–(12), this proves the three-state part of
(1), retaining the unknown tilt, arbitrary rival preparations and counted
transients in its lower bound.

## 4. Two states cannot retain first-order accuracy under all rapid words

The [adiabatic two-state construction](FAMILIAR_SWITCH_FAST_RELAXATION.md)
already gives the all-word upper $`t^2/[r(1-t^2)]`$.
For the lower, suppose along a sequence $`r\to\infty`$ that two-state
models achieve uniform pair error $`o(r^{-1})`$. Both visible signs must
occur. Each is then a singleton, so conditioning removes every
word-dependent preparation. Conditional final means differ from the
target by $`o(r^{-1})`$, uniformly over words: a pair error $`\epsilon\lt 1/2`$
gives conditional mean error at most $`2\epsilon/(1/2-\epsilon)`$.

At a held field the target mean is
$`m+(s-m)P_m(a)`$, where, uniformly for $`a\ge0`$,

**Equation (13).**

```math
P_m(a)=e^{-\lambda_m a}+O(r^{-2}),\qquad
\lambda_m=c_m-\frac{c_m(1-c_m)}r+O(r^{-2}).
```

Indeed the fast exponential has weight
$`(c_m-\lambda_m)/(\Lambda_m-\lambda_m)=O(r^{-2})`$,
with the slow and fast rates defined in the preceding proof.

A nonconstant two-state generator has a relaxation rate $`\kappa_m\gt 0`$
and stationary mean $`\widetilde m_m`$. A zero generator cannot match
the two target held-field conditional rows. Taking long held times
therefore forces $`\widetilde m_m=m+o(r^{-1})`$. Comparing the difference
of the two initial-sign rows at any fixed positive time then gives
$`\kappa_m=\lambda_m+o(r^{-1})`$.

Now fix a high-field duty fraction $`p\in(0,1)`$ and alternate the two
fields increasingly rapidly. For each fixed $`r`$, finite-matrix product
convergence gives the evolution under the weighted average generator.
Taking its long-time limit gives target stationary visible mean

**Equation (14).**

```math
M_p=\frac{pu c_u}{\bar c},\qquad
\bar c=(1-p)c_0+pc_u.
```

This follows directly by averaging (7): stationarity sets $`v=0`$.
For the two-state model the corresponding mean is

```math
\widetilde M_p=
\frac{(1-p)\kappa_0\widetilde m_0+
 p\kappa_u\widetilde m_u}
 {(1-p)\kappa_0+p\kappa_u}.
```

Inserting (13) and the forced parameter estimates yields

**Equation (15).**

```math
\widetilde M_p-M_p
=\frac{pu(1-p)c_0c_u(c_u-c_0)}{r\bar c^2}
 +o(r^{-1}).
```

The coefficient is strictly positive. This contradicts the assumed
uniform $`o(r^{-1})`$ error. Both limiting operations here are taken for
each fixed $`r`$ through finite protocols already included in the
supremum; no uniform-in-$`r`$ product-limit estimate is needed. If the
infimum were not $`\Omega(r^{-1})`$, near-minimizing models along a
subsequence would give precisely the contradicted assumption. This
proves the two-state claim in (1) without a regularity assumption on
the rival rates.

## 5. Physical consequence and boundaries

The proposed rapid-control remedy is now resolved for this two-field
endpoint task. Switching arbitrarily often can expose a first-order
memory correction that no reusable two-state generator reproduces.
A reversible three-state chain retains that correction uniformly.
The fourth equilibrium state is still only forced at second-order
precision. For sufficiently large $`r`$, the existing general three-state
construction remains exact, but this exact compression advantage does
not imply a large finite-accuracy benefit.

The special identity (2) holds at the two selected fields. This proof
does not extend the quadratic all-word upper to a continuum of fields,
a third arbitrary field or a finite ramp passing through intermediate
values. It also retains low-equilibrium target preparation and the
endpoint-only observation task. No path-law, feedback, detector-budget,
sample-count, heat-saving or hardware-memory claim follows.
The first-order two-state lower concerns the ideal all-duration supremum;
the later [finite-pulse witness](FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md)
establishes that order on three specified settings with a growing train
of finitely spaced ideal jumps. Neither result establishes a lower bound
for finite ramps or a bounded Fourier bandwidth.

Rapid control itself is physically meaningful within the
[community model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md). Keeping
$`\Gamma_Z`$ admissible and taking $`\Gamma_S=\Gamma_Z/r`$ makes a
dimensionless dwell $`a=\kappa/r`$ correspond to fixed physical duration
$`\kappa/\Gamma_Z`$. The theorem does not require increasing an absolute
tunneling rate without bound. Actual pulse ramps must nevertheless
respect the microscopic timescales. Esposito et al.,
[*EPL* **89**, 20003 (2010)](https://arxiv.org/pdf/0909.3618), concluding
discussion on p. 6, interpret ideal jumps as ramps fast relative to
tunneling but slow relative to omitted-level and reservoir dynamics.
That precedent supplies a modeling hierarchy, not an implementation
error certificate for this device.

Corrected reduction and linear changes of coordinates are established
tools. Brandner's [weak-memory result](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.037101)
constructs autonomous effective local dynamics and slippage corrections;
its outlook concerns the state of that 2025 work. The
[current background comparison](MANUSCRIPT_BACKGROUND.md) also records
Meyer–Brandner's 2026 complete-period Floquet result for driven weak-memory
reduction. The specific result here is the positive common-Gibbs
three-state realization of (9), the exact shared transformation (10), and
the matched approximation orders over the stated controlled model classes.
This is a bounded source comparison, not an exhaustive priority claim.

The subsequent [finite-rate bounds](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md)
and [trace reduction](FAMILIAR_SWITCH_TRACE_REDUCTION.md) delimit the
finite-accuracy interpretation: parameter extremes do not provide a
fixed positive equilibrium-specific penalty in the exact general-three-state
regime. A substantial interior gap remains unproved and lies outside the
[frozen scientific claim](SCIENTIFIC_CASE.md). It is not an active
pre-drafting requirement.
