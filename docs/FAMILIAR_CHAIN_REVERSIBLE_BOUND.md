# Three boundary fields force two sets of predictive states

A chain of $`n`$ familiar heat-bath switches has an $`(n+1)`$-dimensional
closed space of means. For ordinary reversible predictors, three boundary
field values force **at least $`n`$ Markov states at each visible sign**, hence
at least $`2n`$ states in total. The proof uses a finite menu of endpoint-pair
measurements: $`2(n-1)(n+2)`$ settings, each with at most $`2n-2`$ clock ticks and
two field segments. For three switches, this is twenty settings of at most
four ticks.

The lower bound does not assume that a rival has the target's hidden
coordinates. The observations and the equilibrium field convention force
a common coordinate representation. This closes the gap between a bound
on linear mean dimension and a bound on the number of Markov states.

The equilibrium convention matters: the controlled field couples only to
the measured switch, so the stationary laws at different fields are Gibbs
tilts of one common initial law. The claim does not apply to independently
chosen preparations or unrelated stationary laws at different fields.

## 1. Physical target and finite task

Let $`X_0,\ldots,X_{n-1}\in\{-1,+1\}`$ be time-even conformational switches,
with $`n\ge2`$. The visible switch is $`S=X_0`$. In temperature units, take

**Equation (1).**

```math
E_h(x)=-\sum_{i=0}^{n-2}J_i x_i x_{i+1}-h x_0,
\qquad J_i\gt 0,
```

and ordinary single-switch heat-bath rates

**Equation (2).**

```math
q_i(x,x^{(i)})=
\frac{\alpha_i}{2}
\left[1-x_i\tanh\left(h\mathbf1_{i=0}
 +J_{i-1}x_{i-1}+J_i x_{i+1}\right)\right],
\qquad \alpha_i\gt 0,
```

with absent boundary terms omitted. These assumptions are the open-chain
extension of the model in
[the familiar-switch structure note](FAMILIAR_SWITCH_STRUCTURE.md).
The couplings and attempt rates need not be equal for the lower bound.

Write $`m=\tanh h`$. The strictly positive equilibrium law obeys

**Equation (3).**

```math
\pi_m=\pi_0(1+mS).
```

Choose any three finite boundary fields with

**Equation (4).**

```math
-1\lt m_L\lt m_M\lt m_R\lt 1.
```

They may all be nonnegative. Fix any clock $`\tau\gt 0`$, and let
$`K_j=\exp(\tau Q_j)`$ for $`j\in\{L,M,R\}`$. Prepare $`\pi_0`$ once and
record the joint law of the initial and final visible signs for these words:

**Equation (5).**

```math
\begin{aligned}
&j^q,
&&j\in\{L,M,R\},\quad 1\le q\le2n-2,\\
&L^aM^b,\ R^aM^b,
&&1\le a,b\le n-1.
\end{aligned}
```

Each letter denotes one clock tick at its field, including a zero field
when one is selected. There are

**Equation (6).**

```math
3(2n-2)+2(n-1)^2=2(n-1)(n+2)
```

distinct settings. Word order agrees with row propagation, so the word
$`L^aM^b`$ has kernel $`K_L^aK_M^b`$.

A rival has $`d`$ states, a deterministic binary readout $`\widehat S`$, a
common initial law $`\rho_0`$, and a fixed stochastic kernel $`\widehat K_j`$
for each field. Its ordinary equilibrium convention is

**Equation (7).**

```math
\rho_j=
\frac{\rho_0(1+m_j\widehat S)}
{1+m_j\rho_0\widehat S},
\qquad
\rho_j(x)\widehat K_j(x,y)
 =\rho_j(y)\widehat K_j(y,x).
```

All persistent memory is counted in the rival state. No prescribed hidden
architecture, rate formula, mass floor, rate ceiling, or CTMC embedding is
needed for this lower bound. In particular it applies to reversible CTMC
rivals sampled at the clock. Zero initial masses may be allowed; the proof
then works on their support.

**Finite exact lower bound.** If all laws in (5) agree exactly with the
target, then

**Equation (8).**

```math
d_+\ge n,\qquad d_-\ge n,\qquad d\ge2n,
```

where $`d_\pm`$ count the states of each visible sign. Moreover, every exact
Markov rival, without reversibility, needs at least $`n+1`$ states on the same
menu. The $`2n`$ bound is not an assertion that a reversible $`2n`$-state model
always exists; the physical chain supplies the $`2^n`$-state upper bound.

## 2. Mean closure and the affine Gram matrix

At an internal site,

**Equation (9).**

```math
\tanh(J_{i-1}x_{i-1}+J_i x_{i+1})
 =a_i x_{i-1}+b_i x_{i+1},\qquad a_i,b_i\gt 0.
```

At the controlled endpoint, with $`t_0=\tanh J_0`$,

**Equation (10).**

```math
Q_hX_0=\alpha_0(A-X_0+B X_1),
\quad
A=\frac{m(1-t_0^2)}{1-t_0^2m^2},
\quad
B=\frac{t_0(1-m^2)}{1-t_0^2m^2}\gt 0.
```

The remaining spin means form a tridiagonal linear system, with strictly
positive off-diagonal coefficients. Thus

**Equation (11).**

```math
V=\mathrm{span}\{1,X_0,\ldots,X_{n-1}\}
```

is invariant under every field generator and propagator.

For each fixed field, the endpoint is cyclic on this space after including
the constant: the coefficient of $`X_k`$ first appears in $`Q_h^kS`$ as a
nonzero product of the forward tridiagonal coefficients. After centering
by the equilibrium mean, the tridiagonal drift is diagonally similar to a
real symmetric irreducible tridiagonal matrix. It has distinct eigenvalues;
exponentiation preserves their distinctness. Consequently, for every
$`\tau\gt 0`$, the row of functions

**Equation (12).**

```math
H_j=(1,S,K_jS,\ldots,K_j^{n-1}S)
```

is a basis of $`V`$. There is therefore a known invertible matrix $`B_j`$ such
that

**Equation (13).**

```math
H_jB_j=F,
\qquad F=(1,X_0,\ldots,X_{n-1}).
```

These matrices depend only on the specified target and clock. No rival
coordinate choice enters their definition.

Put $`t_i=\tanh J_i`$, $`T_0=1`$, and

**Equation (14).**

```math
T_i=\prod_{r=0}^{i-1}t_r,
\qquad
C_{ij}=\prod_{r=\min(i,j)}^{\max(i,j)-1}t_r.
```

Empty products are one. The equilibrium Gram of the physical coordinates
is

**Equation (15).**

```math
G(m)=\mathbb E_{\pi_m}[F^{\mathsf T}F]
 =\begin{pmatrix}1&mT^{\mathsf T}\\mT&C\end{pmatrix}.
```

It is positive definite for $`|m|\lt 1`$ and affine in $`m`$. The two conditional
Grams are

**Equation (16).**

```math
G_s=G(0)+sG'(0)
 =\mathbb E_{\pi_0}[F^{\mathsf T}F\mid S=s],
\qquad s=\pm1.
```

Each has rank $`n`$: fixing $`S=s`$ removes exactly one linear relation between
$`1`$ and $`S`$, while $`1,X_1,\ldots,X_{n-1}`$ remain independent on the full
conditional support.

## 3. The observations force a common coordinate representation

For the rival, define its row of functions using the same coefficients:

**Equation (17).**

```math
\widehat F_j=
(1,\widehat S,\widehat K_j\widehat S,\ldots,
 \widehat K_j^{n-1}\widehat S)B_j.
```

Use the unnormalized equilibrium weights

**Equation (18).**

```math
\omega_j=\rho_0(1+m_j\widehat S).
```

Multiplying a stationary law by a positive scalar preserves detailed
balance. These weights are exactly affine in $`m_j`$, including when a
rival's initial sign balance is imperfect.

Write $`\langle f,g\rangle_j=\sum_x\omega_j(x)f(x)g(x)`$.
Reversibility gives

**Equation (19).**

```math
\begin{aligned}
\langle\widehat K_j^a\widehat S,
       \widehat K_j^b\widehat S\rangle_j
 &= (\rho_0\widehat S+m_j\rho_0)
       \widehat K_j^{a+b}\widehat S,\\
\langle\widehat K_j^a\widehat S,
       \widehat K_M^b\widehat S\rangle_j
 &= (\rho_0\widehat S+m_j\rho_0)
       \widehat K_j^a\widehat K_M^b\widehat S,
\qquad j=L,R.
\end{aligned}
```

Here $`a,b`$ may be zero. Every right-hand side is an endpoint correlation
plus $`m_j`$ times an endpoint mean. Constant-containing Gram entries are
also determined by the same pair laws and their marginals. The words in
(5) therefore determine the own-field Grams and the two mixed Grams:

**Equation (20).**

```math
\begin{aligned}
\mathbb E_{\omega_j}[\widehat F_j^{\mathsf T}\widehat F_j]
 &=G(m_j),&&j=L,M,R,\\
\mathbb E_{\omega_j}[\widehat F_j^{\mathsf T}\widehat F_M]
 &=G(m_j),&&j=L,R.
\end{aligned}
```

Exact data also give $`\rho_0\widehat S=0`$, so the weights are then
normalized. Set

**Equation (21).**

```math
w_L=\frac{m_R-m_M}{m_R-m_L},\qquad
w_R=\frac{m_M-m_L}{m_R-m_L}.
```

For every real coefficient vector $`v`$, affine dependence of the weights
and (20) imply

**Equation (22).**

```math
\begin{aligned}
&w_L\| (\widehat F_M-\widehat F_L)v\|_L^2
 +w_R\| (\widehat F_M-\widehat F_R)v\|_R^2\\
&\quad=\|\widehat F_Mv\|_M^2
 -\sum_{j=L,R}w_j
  \left[2\langle\widehat F_jv,\widehat F_Mv\rangle_j
                -\|\widehat F_jv\|_j^2\right]\\
&\quad=v^{\mathsf T}
       [G(m_M)-w_LG(m_L)-w_RG(m_R)]v=0.
\end{aligned}
```

Both terms are nonnegative and both weights are positive. Hence all three
coordinate representations agree on the support of $`\rho_0`$. Denote the
common representation by $`\widehat F`$.

Its Grams at two different tilts determine separately

**Equation (23).**

```math
\mathbb E_{\rho_0}[\widehat F^{\mathsf T}\widehat F]=G(0),
\qquad
\mathbb E_{\rho_0}[\widehat S\widehat F^{\mathsf T}\widehat F]
 =G'(0).
```

The conditional Gram in each visible sector is therefore $`G_s`$, of rank
$`n`$. A Gram supported on $`d_s`$ states has rank at most $`d_s`$. This proves
(8), without assuming a hidden-coordinate lift at the start.

## 4. General Markov rivals need at least n+1 states

At one selected field $`j`$, form the data matrix whose columns are

**Equation (24).**

```math
1,\widehat S,\widehat K_j\widehat S,\ldots,
 \widehat K_j^{n-1}\widehat S
```

and whose rows are

**Equation (25).**

```math
\omega_j,\quad \omega_j\widehat S,\quad
\omega_j\widehat S\widehat K_j,\ldots,
\omega_j\widehat S\widehat K_j^{n-1}.
```

All entries are determined by the pure-word pair laws already in (5).
On the target, reversibility makes this matrix the positive-definite Gram
of $`H_j`$, so its rank is $`n+1`$. On any Markov rival the matrix factors
through its $`d`$ states, even if that rival is not reversible and does not
have the equilibrium field convention. Therefore $`d\ge n+1`$.

The two state lower bounds concern the same finite menu. They count total
persistent Markov states, not merely the number of distinct decay rates.

The [positive realization](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md) attains
the unrestricted lower bound for equal couplings with
$`0\lt \tanh J\le1/\sqrt5`$ and nonnegative boundary fields. This gives
$`n+1`$ general states versus at least $`2n`$ reversible states for every
$`n\ge3`$. For the three-switch choice $`\tanh J=1/3`$, the
[six-state reversible realization](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
also attains the ordinary lower bound for $`0\le\tanh h\le1/2`$.
Any three distinct fields in that interval therefore give exactly four
general states versus six reversible states on the same finite menu.

## 5. A positive finite-accuracy radius

The state lower bounds persist at a positive total-variation tolerance on
the same menu. An explicit conservative bound follows from the same norm
identity, with no stationary mass floor.

Suppose each rival endpoint-pair law is within total variation $`\delta`$ of
the corresponding target law. A bounded sign or sign product then has
expectation error at most $`2\delta`$. Using the unnormalized weights (18),
every base own-field or mixed Gram entry in (19), including entries with a
constant coordinate, has error at most

**Equation (26).**

```math
\epsilon=2(1+m_*)\delta,
\qquad m_*=\max_j|m_j|.
```

This includes a possible initial sign imbalance of the approximate rival;
normalizing its Gibbs equilibrium is unnecessary for the calculation.
Define any certified upper bound

**Equation (27).**

```math
K\ge\max_j\|B_j\|_{2\to1},
\qquad
w=\min(w_L,w_R),
\qquad
W=\frac{2+|m_L+m_R|}{m_R-m_L}.
```

For example, the largest sum of absolute values of all entries of $`B_j`$ is
a valid choice of $`K`$. Let $`\lambda_*\gt 0`$ be the minimum eigenvalue of the
physical conditional Gram restricted to the $`n`$ coordinates
$`(1,X_1,\ldots,X_{n-1})`$. The two signs have the same eigenvalues: their
Grams are $`C`$ and a diagonal sign conjugate of $`C`$, with $`C`$ from (14).

For every unit coefficient vector $`v`$, the approximate version of (22)
gives

**Equation (28).**

```math
\sum_{j=L,R}w_j
  \| (\widehat F_M-\widehat F_j)v\|_j^2
\le4\epsilon K^2.
```

Indeed, the own middle-field Gram contributes at most $`\epsilon K^2`$;
the weighted mixed and outer own-field Grams contribute at most another
$`3\epsilon K^2`$. Expanding the squared norm around $`\widehat F_j`$ then
yields, for $`j=L,R`$,

**Equation (29).**

```math
\left|\|\widehat F_Mv\|_j^2-v^{\mathsf T}G(m_j)v\right|
\le\epsilon K^2(4/w+3).
```

Extrapolate these two Grams to the weights $`\rho_0(1+s\widehat S)`$,
$`s=\pm1`$. The sum of the absolute extrapolation coefficients is at most
$`W`$. Thus the operator-norm error of each sign-sector mass Gram is at most

**Equation (30).**

```math
W\epsilon K^2(4/w+3).
```

The actual matrix is supported only on the states of that sign. Even when
the rival is imbalanced, its restriction to the $`n`$ selected coordinates
has rank at most $`d_s`$. Its target is positive definite with eigenvalue
bound $`\lambda_*`$. Consequently every ordinary rival with menu error

**Equation (31).**

```math
\delta\lt \delta_{\rm ord}
 :=\frac{\lambda_*}
 {2(1+m_*)WK^2(4/w+3)}
```

still obeys $`d_+,d_-\ge n`$.

For the unrestricted lower bound, transform the data matrix of Section 4
by $`B_j^{\mathsf T}`$ and $`B_j`$. Its target is $`G(m_j)`$, and its
operator-norm error is at most $`\epsilon K^2`$, even though the rival
matrix need not be symmetric. Thus a sufficient unrestricted radius is

**Equation (32).**

```math
\delta_{\rm all}
 :=\frac{\lambda_{\min}(G(m_j))}{2(1+m_*)K^2}
```

for any selected field $`j`$. Below this radius, its rank remains $`n+1`$.
When $`m_L=0`$, $`G(0)=\mathrm{diag}(1,C)`$ has minimum eigenvalue
$`\lambda_*`$, and $`W(4/w+3)\gt 1`$. In that case the single smaller radius
$`\delta_{\rm ord}`$ establishes both lower bounds.

The radius is positive for every fixed target, distinct field triple, and
positive clock. It is not an optimal approximation distance, a uniform
bound over all parameter choices, or a claim of a practical measurement
budget. Conditioning of the finite basis matrices $`B_j`$ remains relevant.

## 6. Meaning and limits

The argument uses three values of one ordinary boundary field. Their role
is to compare three affine equilibrium weights. Detailed balance converts
endpoint correlations into squared norms; equality at the intermediate
field forces the same hidden coordinate representation at the outer
fields. Each visible sign must then carry the full hidden covariance.

The menu is a sufficient certificate, not a proof that twenty settings or
four ticks are optimal for three switches. The lower bound is valid for
any fixed positive clock and any positive physical couplings and attempt
rates. Numerical conditioning and experimental cost may depend strongly
on those choices.

The result concerns controlled endpoint-pair predictions. It does not
assert that a small predictor reproduces the visible path law, implements
a particular detector, or preserves all intermediate observations.
