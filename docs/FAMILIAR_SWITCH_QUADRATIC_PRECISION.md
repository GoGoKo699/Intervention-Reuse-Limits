# Hidden response sets a quadratic precision scale

For the two-switch system, the first correction from a fast hidden degree
of freedom can be absorbed into the rates of a reversible two-state
model. The obstruction requiring four reversible states survives at the
next order. This note proves a matched precision law for the existing
seven-word endpoint-pair task, without simulations or parameter fitting.
The same matched order also holds uniformly over all finite words at the
fixed control clock; seven words already witness its lower bound.

At fixed positive coupling, field and dwell times, let
$`r=\Gamma_Z/\Gamma_S`$ be the hidden-to-visible attempt-rate ratio. The
best maximum pair-law error achievable with at most three ordinary
reversible states satisfies

```math
\boxed{E_{\mathrm{ord},3}(r)=\Theta(r^{-2})\qquad(r\to\infty).}
```

The lower bound allows arbitrary rival preparations and an unknown Gibbs
tilt. The upper is an explicit two-state Gibbs model with corrected
relaxation rates. Thus the order is attained by an admissible model and
cannot be improved by any three-state reversible alternative. The
constants need not agree, and no closest-model claim is made.

## 1. Physical task and comparison

Use the [heat-bath model](FAMILIAR_SWITCH_FAST_RELAXATION.md) with
energy $`-JSZ-hS`$, $`t=\tanh J\in(0,1)`$ and high-field tilt
$`u=\tanh H\in(0,1)`$. Time is in units of $`1/\Gamma_S`$. Fix
$`\tau_L,\tau_H\gt 0`$ and prepare the target in
$`\pi_0(s,z)=(1+tsz)/4`$. Observe its true initial and final signs for

```math
\mathcal W=\{L,LL,H,LH,HL,LLH,HLL\}.
```

Letters denote the fixed low- or high-field dwell. Every word has at most
two held-field segments: $`LL`$ is one uninterrupted low-field segment of
duration $`2\tau_L`$. There are no intermediate observations or feedback.

An ordinary rival has at most three complete persistent states, a fixed
deterministic binary readout, and fixed reused stochastic kernels
$`K_L,K_H`$. They obey detailed balance for normalized nonnegative laws
related by

```math
\widehat\pi_H(x)=
\frac{\widehat\pi_L(x)(1+v\widehat S(x))}
 {1+v\widehat\pi_L\widehat S},\qquad v\in(-1,1).
```

The rival tilt $`v`$ is unknown and need not equal $`u`$. Preparations may
depend arbitrarily on the word and previous history. Preparable zero-weight transient
states count. There is no rate cap, stationary-mass floor, equilibrium
preparation promise or continuous-time embedding requirement on the
null. This is the population class of the
[preparation-free seven-word theorem](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md).
Define $`E_{\mathrm{ord},3}(r)`$ as the infimum, over that class, of the
maximum per-word total-variation error to the target pair laws.

For the general Markov state counts below, retain this interface and
stationarity of the declared Gibbs laws but drop detailed balance. The
two-state lower bound will hold even without stationarity or a Gibbs rule.

This is an ideal population theorem. It neither extends a previous
detector-error budget nor supplies a new acquisition guarantee.

## 2. Two transfers of hidden response give the lower bound

Write $`b_L=t`$, $`b_H=t(1-u^2)/(1-t^2u^2)`$ and $`c_j=1-tb_j`$.
At a field with tilt $`m`$, the centered conditional means evolve under

```math
M_j=\begin{pmatrix}-1&b_j\\rt&-r\end{pmatrix},
\qquad (x_{\rm eq},z_{\rm eq})=(m,tm).
```

Its slow and fast relaxation rates are

```math
\lambda_j=\frac{r+1-\sqrt{(r-1)^2+4rtb_j}}2,
\qquad
\Lambda_j=\frac{r+1+\sqrt{(r-1)^2+4rtb_j}}2.
```

For the appropriate dwell $`\tau_j`$, put

```math
\mu_j=e^{-\lambda_j\tau_j},\quad
\nu_j=e^{-\Lambda_j\tau_j},\quad
\gamma_j=\frac{b_j(\mu_j-\nu_j)}{\Lambda_j-\lambda_j},\quad
P_H=(e^{\tau_H M_H})_{11}+t\gamma_H.
```

Let $`\rho_{w,s}`$ be the target probability of returning to sign $`s`$
conditional on starting in that sign. Define

```math
A_a=\rho_{L^aH,s}-\rho_{L^a,s}\rho_{H,s},\quad
B_a=\rho_{HL^a,s}-\rho_{L^a,s}\rho_{H,s},\quad
F_s=A_1B_2-A_2B_1.
```

The existing null proof gives $`F_+=0`$ or $`F_-=0`$ for every admissible
rival. A singleton visible sign removes preparation; comparing two low
durations removes the unknown tilt. Its separate transient-block argument
also covers zero stationary weights. Those hypotheses are unchanged here.

For the target, the arbitrary-rate factorization is

**Equation (1).**

```math
\boxed{F_s=-\frac{s u(1-t^2)}8\,
\gamma_H(1-P_H)\gamma_L(1-\mu_L)(1-\nu_L).}
```

Here is a derivation that does not assume equal attempt rates. Set
$`p_a=(e^{a\tau_LM_L})_{11}`$ and
$`g_a=(e^{a\tau_LM_L})_{12}`$. Low-field covariance symmetry implies
that the two evolved conditional coordinates are $`p_a+tg_a`$ and
$`tp_a+g_a`$. For the high propagator $`T=e^{\tau_HM_H}`$,

```math
T_{21}+tT_{22}-t(T_{11}+tT_{12})
=\frac{1-t^2}{1-u^2}\gamma_H.
```

Indeed $`T_{21}=rt\gamma_H/b_H`$ and
$`T_{22}=T_{11}+(1-r)\gamma_H/b_H`$, so the rate ratio cancels.
Put $`\alpha_s=(1+su)(1-P_H)/4`$ and
$`\alpha'_s=(1-su)(1-P_H)/4`$. Direct subtraction of the return products
now gives

```math
A_a=\alpha_s(1-p_a)
 +\left[-t\alpha_s+\frac{1-t^2}{2}\gamma_H\right]g_a,
```

```math
B_a=\alpha'_s(1-p_a)
 +\left[-t\alpha'_s+
 \frac{(1-su)(1-t^2)}{2(1-u^2)}\gamma_H\right]g_a.
```

The determinant of these coefficient rows is
$`s u(1-t^2)\gamma_H(1-P_H)/8`$. Cayley–Hamilton for the low
propagator gives

```math
(1-p_1)g_2-(1-p_2)g_1
=-\gamma_L(1-\mu_L)(1-\nu_L),
```

which proves (1). To check positivity for every $`r\gt 0`$, the quadratic
with roots $`\lambda_j,\Lambda_j`$ has positive roots and is negative at
$`c_j\in(0,1)`$, giving $`0\lt \lambda_j\lt c_j\lt \Lambda_j`$. Also

```math
P_H=\frac{(\Lambda_H-c_H)\mu_H+(c_H-\lambda_H)\nu_H}
          {\Lambda_H-\lambda_H}.
```

This is a convex combination of two numbers strictly between zero and
one. Hence $`0\lt P_H\lt 1`$, and every factor in the magnitude of (1) is
strictly positive.

To convert the witness to pair-law error, its global Lipschitz constant
on the seven-return cube is at most six. In the order
$`(a,b,c,d,e,f,g)=(\rho_L,\rho_{LL},\rho_H,\rho_{LH}, \rho_{HL},\rho_{LLH},\rho_{HLL})`$, the polynomial is

```math
F=dg-fe+ac(f-g)+bc(e-d).
```

Its gradient norm is bounded by two expressions of the form
$`2|x-y|+|x-z|+|y-z|\le3`$ for $`x,y,z\in[0,1]`$.
Thus $`|F(q)-F(q')|\le6\|q-q'\|_\infty`$.
If a rival pair table is within TV $`\delta\lt 1/2`$ of the balanced target,
each conditional return differs by at most $`\delta/(1/2-\delta)`$.
Both rival initial signs then have positive probability. With
$`f(r)=|F_s|`$, identical for both target signs, the null identity yields

**Equation (2).**

```math
\boxed{E_{\mathrm{ord},3}(r)\ge\frac{f(r)}{12+2f(r)}.}
```

Rivals at distance at least $`1/2`$ already satisfy this bound. Consequently
no assumption about their initial sign balance is needed.

Let $`e_L=e^{-c_L\tau_L}`$ and $`e_H=e^{-c_H\tau_H}`$. The displayed
rates give $`\lambda_j\to c_j`$, $`\Lambda_j/r\to1`$,
$`r\gamma_j\to b_je_j`$ and $`P_H\to e_H`$. Hence

**Equation (3).**

```math
r^2f(r)\longrightarrow
C_F:=\frac{u(1-t^2)t b_H}{8}
e_H(1-e_H)e_L(1-e_L)\gt 0.
```

In particular, $`\liminf_{r\to\infty}r^2E_{\mathrm{ord},3}(r) \ge C_F/12`$. The two response coefficients $`\gamma_L,\gamma_H`$
each contribute one inverse power of the hidden relaxation rate.

## 3. Corrected equilibrium rates attain the same order

For any held field $`m=\tanh h`$, use the corresponding slow rate above
and define a two-state model by

**Equation (4).**

```math
q_h^{(2)}(s,-s)=\frac{\lambda_h}{2}(1-sm).
```

The rates are positive and obey detailed balance for $`(1+ms)/2`$.
Use its common balanced low-field equilibrium preparation. This is an
admissible subclass of the broad ordinary null. The exact identity

```math
c_h-\lambda_h=\frac{\lambda_h(1-\lambda_h)}r
```

shows that (4) corrects the leading adiabatic rate $`c_h`$ by its first
kinetic correction, while retaining the Gibbs equilibrium exactly.

For completeness, an elementary bound controls the error at switches.
Conditional on either initial sign, let $`w=z-tx`$. The target satisfies

```math
x'=-c_h(x-m)+b_hw,\qquad w'=-rw-tx',\qquad w(0)=0.
```

Since $`|x'|\le2`$, variation of constants gives $`|w|\le2t/r`$ at
all times. For $`r\gt 1`$, set

```math
k_h=\frac{t\lambda_h}{r-\lambda_h},\qquad
z_h^{\rm fast}=w-k_h(x-m).
```

Substitution yields the exact triangular equations

```math
(z_h^{\rm fast})'=-\Lambda_h z_h^{\rm fast},\qquad
x'=-\lambda_h(x-m)+b_h z_h^{\rm fast}.
```

The visible displacement contributed by an incoming fast defect $`z_0`$
over one held segment of duration $`a`$ is therefore

```math
\frac{b_hz_0}{\Lambda_h-\lambda_h}
 (e^{-\lambda_h a}-e^{-\Lambda_h a}).
```

Use $`b_h\le t`$, $`k_h\le t/(r-1)`$ and
$`\Lambda_h-\lambda_h\ge r-1`$. On the first segment
$`|z_0|\le2t/(r-1)`$; on a second segment
$`|z_0|\le2t/r+2t/(r-1)`$. The incoming visible error contracts
under the second slow propagator. For either initial sign its final
mean error is at most

```math
\frac{4t^2}{(r-1)^2}+\frac{2t^2}{r(r-1)}.
```

Conditional binary TV is half the mean error, and both initial signs
have probability $`1/2`$. Thus the same model satisfies

**Equation (5).**

```math
\boxed{\max_{w\in\mathcal W}\mathrm{TV}(P_w,P_w^{(2)})
\le\min\!\left\{1,\frac{10t^2}{r^2}\right\},\qquad r\ge2.}
```

This conservative constant is not optimized. The upper is uniform in
the two nonnegative dwell times and total elapsed time. Together with
(2)–(3), it proves the matched order at fixed positive dwells. The limits
in (3) are uniform on compact subsets of
$`(t,u,\tau_L,\tau_H)\in(0,1)^2\times(0,\infty)^2`$, so the order
also holds uniformly on each such parameter region.

### A fixed minimum dwell permits arbitrarily many segments

Let every held-field segment, including the terminal observed segment,
last at least $`a\gt 0`$, independently of $`r`$. Since
$`\lambda_h\Lambda_h=rc_h`$ and $`\Lambda_h\le r+1`$,

```math
\lambda_h\ge\frac{r(1-t^2)}{r+1}
\ge\frac23(1-t^2),\qquad r\ge2.
```

The preceding fast-defect bounds give a conditional-mean error injection
of at most $`12t^2/r^2`$ on any segment, including the first. If $`D_k`$
is the maximum error over the two initial signs after segment $`k`$, then

```math
D_k\le q_a D_{k-1}+\frac{12t^2}{r^2},\qquad
q_a=e^{-2(1-t^2)a/3}\lt 1,\qquad D_0=0.
```

Summing the geometric series and converting to pair TV yields

**Equation (6).**

```math
\sup_w\mathrm{TV}(P_w,P_w^{(2)})
\le\min\!\left\{1,\frac{6t^2}{r^2(1-q_a)}\right\}.
```

There is no dependence on the number of segments or total horizon.
Contraction during each minimum dwell prevents switch errors from
accumulating without bound.

To keep the comparison interface unchanged, define
$`E_{\mathrm{ord},3}^{\rm clock}(r)`$ using the same rival class as in
Section 1, but replace the seven-word maximum by the supremum over all
finite words in $`\{L,H\}^*`$. The fixed tick durations are still
$`\tau_L,\tau_H`$, and arbitrary word-dependent preparations remain allowed.
Each merged held-field segment lasts at least
$`a=\min\{\tau_L,\tau_H\}\gt 0`$. The seven words are a subset, while (6)
uses one admissible two-state model for the whole task. Therefore

```math
\frac{f(r)}{12+2f(r)}
\le E_{\mathrm{ord},3}(r)
\le E_{\mathrm{ord},3}^{\rm clock}(r)
\le\frac{6t^2}{r^2(1-q_a)},\qquad r\ge2,
```

and $`E_{\mathrm{ord},3}^{\rm clock}(r)=\Theta(r^{-2})`$ as well.
This statement requires neither an upper bound on word length nor a
common rival preparation. Its constants are also uniform on the compact
parameter regions specified above.

## 4. What happens to the state-count distinction?

An arbitrary general two-state model also has a second-order obstruction.
For the low field, define

```math
\beta=\frac{c_L-\lambda_L}{\Lambda_L-\lambda_L},\qquad
C_j=(1-\beta)\mu_L^j+\beta\nu_L^j.
```

The target passive correlation at $`j`$ low ticks is $`C_j`$, and

```math
\Delta(r)=C_2-C_1^2
=\beta(1-\beta)(\mu_L-\nu_L)^2\gt 0,
\quad r^2\Delta(r)\to t^2(1-t^2)e_L^2\gt 0.
```

For any two-state kernel, its $`L,LL`$ conditional returns obey
$`\rho_{LL,+}=\rho_{L,+}^2+(1-\rho_{L,+})(1-\rho_{L,-})`$,
independently of preparation. This identity has Lipschitz constant at
most three on its return cube; the target violates it by $`\Delta/2`$.
The same conditioning argument gives a general two-state error lower
bound $`\Delta/(12+2\Delta)`$.

For all sufficiently large $`r`$, the
[existing positive three-state construction](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md)
is exact, since its sufficient and necessary signed-control condition is

```math
r\ge\frac{u(1+t^2+2t^2u)}{1-t^2u^2}.
```

The four-state target is the ordinary upper. Consequently, on the
seven-word task, at error

```math
0\le\delta\lt \min\!\left\{
\frac{f(r)}{12+2f(r)},\frac{\Delta(r)}{12+2\Delta(r)}\right\},
```

the attained minima are **three general versus four ordinary states**.
Both displayed thresholds have order $`r^{-2}`$. Conversely, when
$`10t^2/r^2\le\delta\lt 1/2`$, both classes need exactly **two states**:
(5) supplies them, while a one-sign state is at least TV $`1/2`$ from
the balanced initial target. The intervening transitions are not located.
For all clocked words, the same lower state-count interval applies; the
two-state upper threshold uses (6) instead of (5).

## 5. Physical meaning, control scope and prior work

The result identifies where the equilibrium state penalty resides in
this fast-hidden regime. First-order slowing changes relaxation rates;
it can be represented without adding states or breaking detailed balance.
Second-order response variation obstructs every three-state reversible
fit to the seven words. A fixed accuracy eventually cannot resolve that
penalty, even though it remains present in the exact finite-rate model.

Here $`r\to\infty`$ is a relative-timescale limit of the reduced kinetic
model, not permission to increase an absolute tunneling rate beyond the
[community model's validity regime](FAMILIAR_SWITCH_COMMUNITY_MODEL.md).
The ratio can instead grow by decreasing $`\Gamma_S`$ while keeping
$`\Gamma_Z`$ admissible; the fixed dimensionless dwells then correspond to
longer physical durations $`\tau_j/\Gamma_S`$.

Two qualifications carry physical content. Low-equilibrium target
preparation makes the initial hidden lag vanish; arbitrary target
disturbance can restore a first-order error. Repeated switches create new
fast transients, but a fixed minimum dwell controls their accumulation
even over arbitrarily long words. The constant in (6) deteriorates as
that dwell tends to zero; the proof does not provide a second-order bound
under unrestricted switching cadence. The preceding
[all-word first-order bound](FAMILIAR_SWITCH_FAST_RELAXATION.md) retains
its broader control scope. The subsequent
[all-duration theorem](FAMILIAR_SWITCH_RAPID_CONTROL.md) resolves the
rapid-control question: two-state error becomes first order, while the
optimal reversible three-state error remains second order. Its positive
three-state upper and class-wide lower are separate arguments; failure
of the present two-state approximation alone would not establish them.
Full trajectories, intermediate measurements and feedback remain
different prediction tasks.

The approximation method has close precedents. Strasberg and Esposito,
[*Phys. Rev. E* **95**, 062101 (2017)](https://arxiv.org/pdf/1703.05098),
Section II C, Eqs. (25)–(28), describe conditional equilibration and
effective detailed balance. Brandner,
[*Phys. Rev. Lett.* **134**, 037101 (2025)](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.037101),
Eqs. (8)–(14) and (21)–(25), develops autonomous effective local
generators, initial slippage and systematic corrections in a weak-memory
regime. Correcting a slow relaxation rate is not a new general method.

The model-specific assertion here is the matched approximation order
against **every** admissible ordinary three-state rival for a controlled
task, including arbitrary rival preparation and unknown tilt, together
with a positive Gibbs upper and the resulting state-count regimes.
The reciprocal-return method and its source precedents remain those of
the [seven-word source audit](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md).
This comparison does not establish exhaustive priority or broad practical
importance. The law explains a regime where the penalty becomes small;
it does not yet identify an experimentally useful regime with a large one.
