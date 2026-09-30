# When nonnegative control permits exact three-state prediction

Slowing the hidden switch does not necessarily strengthen an
equilibrium-specific state advantage. Below an exact rate threshold,
even a general positive predictor needs all four states. This note
locates that threshold for the existing nonnegative two-field task,
including arbitrary word-dependent rival preparation.

Use the low-equilibrium heat-bath target with
$`t=\tanh J\in(0,1)`$, $`u=\tanh H\in(0,1)`$ and
$`r=\Gamma_Z/\Gamma_S\gt 0`$. Observe the true initial/final visible signs
for every predetermined finite word using fields $`0,H`$ and arbitrary
positive dwells. A general rival has one deterministic binary readout
and fixed reused continuous-time generators on its complete persistent
state space. Its preparation may change with the word. No Gibbs rule,
stationary preparation, detailed balance, rate cap or positive-mass
promise is imposed on this general class.

The exact minima are

**Equation (1).**

```math
\boxed{
D_{\rm general}(0)=
\begin{cases}
3,&r\ge r_*(t,u),\\
4,&r\lt r_*(t,u),
\end{cases}
\qquad
r_*(t,u)=\frac{u(1+t^2+2t^2u)}{2(1+u)}.}
```

The ordinary reversible minimum is four throughout. When available,
the three-state construction works on the whole interval $`[0,H]`$,
with one common equilibrium preparation and the target Gibbs force.
This is an exact all-word theorem, not a new quantitative error margin.

The proof adapts the exhaustive realization argument of the
[signed-control boundary](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md).
The one-sided threshold is different, and the singleton argument below
removes that theorem's common-preparation premise for the present task.

## 1. A singleton response determines the common realization

Both target initial signs have probability $`1/2`$. A three-state binary
readout has a singleton sign $`s`$. Conditional on that sign, the rival
starts from the same point mass for every word, regardless of its
preparation choices. Its response must equal the corresponding target
conditional response.

At held high field, the latter is

```math
x_s(a)=u+(s-u)
 \left[Ae^{-\lambda_H a}+Be^{-\Lambda_H a}\right],
\qquad A,B\gt 0,\quad A+B=1,
```

where $`0\lt \lambda_H\lt \Lambda_H`$ are the two target relaxation rates.
All three coefficients are nonzero. Consequently this scalar response
has minimal linear dimension three, excluding any two-state exact fit.
Its high-field row and column Krylov matrices are invertible.

Minimal-realization similarity therefore transfers the high generator,
output and fixed conditional initial row to a hypothetical three-state
rival. Mixed high–low–high words transfer the low generator under the
same similarity: their derivatives give every matrix element
$`\delta_s Q_H^i Q_0 Q_H^j S`$ for $`0\le i,j\le2`$, and the two
invertible high-field Krylov matrices determine $`Q_0`$ from this table.
Thus the common observable closure is

**Equation (2).**

```math
Q_mS=A_m-S+B_mZ,\qquad Q_mZ=r(tS-Z),
```

```math
A_m=\frac{m(1-t^2)}{1-t^2m^2},\qquad
B_m=\frac{t(1-m^2)}{1-t^2m^2}.
```

The constant coordinate is preserved: its simple zero mode is normalized
by the conditional initial row. That row is $`(1,s,ts)`$, so the singleton
has $`Z=ts`$. The auxiliary observable need not have binary values.

Any low-field stationary law has $`\mathbb E S=\mathbb E Z=0`$ by
(2). Hence it puts mass $`1/2`$ on the singleton and satisfies
$`\mathbb E SZ=t`$. It must have full support. Otherwise its two-state
closed support would have $`Z=tS`$, giving both
$`Q_0Z=tQ_0S=-t(1-t^2)S`$ and $`Q_0Z=r(tS-Z)=0`$, a contradiction.

Write this positive law as $`\pi_0`$. The normalized positive laws
$`\pi_m=\pi_0(1+mS)`$ have moments $`(1,m,tm)`$, which annihilate
the closure matrix. Because $`(1,S,Z)`$ is a basis, they are stationary.
Thus the common Gibbs family follows from the conditional data; it was
not a premise imposed on the general rival.

## 2. Positivity gives the rate boundary

First take the singleton to be negative. The exhaustive parameterization
and corresponding low stationary law are

```math
S=(-1,1,1),\quad Z=(-t,t-a,t+b),\quad
\pi_0=\left(\frac12,\frac{b}{2(a+b)},\frac{a}{2(a+b)}\right),
\quad a,b\gt 0.
```

The closure fixes all six rates, as in the unequal-rate appendix of the
signed-control proof. In particular, $`q_{13}\ge0`$ forces $`a\ge2t`$,
while $`q_{31}(H)\ge0`$ forces

```math
b\le b_*:=\frac{1-t^2}{t(1+u)}.
```

At zero field, $`q_{31}=(1-t^2-tb)/2`$, and $`q_{32}\ge0`$ requires

**Equation (3).**

```math
\frac{1-t^2-tb}{2}\le\frac{rb}{2t+b}.
```

The left side minus the right decreases strictly with $`b`$. Substitution
of its largest allowed value $`b_*`$ into (3) gives exactly $`r\ge r_*`$.

For a positive singleton, reflect signs and fields. The available tilts
become $`-u,0`$. Now $`b\le(1-t^2)/t`$, and testing the other endpoint
at that largest value gives the necessary condition

```math
r\ge r_+(t,u):=
\frac{u(1+u)(1+t^2)}{2(1-t^2u^2)}\gt r_*(t,u).
```

The strict comparison follows from

```math
(1+u)^2(1+t^2)
 -(1-t^2u^2)(1+t^2+2t^2u)
=2u+(1+t^2)^2u^2+2t^4u^3\gt 0.
```

Allowing either singleton sign therefore does not weaken (1).

## 3. A matching positive construction

Set $`a=2t`$, $`b=b_*`$, and

```math
\chi=\frac{1-t^2}{1+t^2+2t^2u},\qquad \rho=1-\chi.
```

Use $`S=(-1,1,1)`$, $`Z=(-t,-t,t+b_*)`$ and the common preparation
$`\pi_0=(1/2,\chi/2,\rho/2)`$. For every $`0\le m\le u`$, put

```math
L(m)=\frac{(1-t^2)(1+m)}{2(1-t^2m^2)},\qquad
k(m)=\frac{(1-t^2)(1-m)(u-m)}{2(1+u)(1-t^2m^2)},
```

**Equation (4).**

```math
Q_m=\begin{pmatrix}
-L&L&0\\
1-L&-(1-L+r\rho)&r\rho\\
k&r\chi-k&-r\chi
\end{pmatrix}.
```

Here $`0\lt L\lt 1`$ and $`k`$ decreases from
$`k(0)=(1-t^2)u/[2(1+u)]`$ to zero. For example,
$`2t^2m/(1-t^2m^2)\le1/(1-m)`$ makes the logarithmic derivative of
$`(1-m)(u-m)/(1-t^2m^2)`$ negative on $`(0,u)`$.
The only nontrivial positivity condition is $`k(0)\le r\chi`$, exactly
(1). The chain remains irreducible at equality: both directions between
states 1 and 2 and the rate from 2 to 3 are positive, and state 3 has
positive total exit $`r\chi`$.

Direct substitution verifies (2), the Gibbs stationary laws and the
conditional initial means $`\mathbb E[Z\mid S=s]=ts`$. Hence this
single model matches all endpoint-pair laws for every allowed word.

For an exact ordinary three-state model, the conditional-data argument
has already forced a positive Gibbs family. The existing singleton
reciprocity identity then applies and is violated by the target for
every $`t,u,r\gt 0`$. Thus ordinary three-state matching is impossible.
The physical four-state model supplies the remaining uppers.

## 4. What the boundary means

Since $`r_*\lt u\lt 1`$, equal or faster hidden attempts permit exact general
three-state compression throughout the nonnegative control range.
But $`r_*\to1`$ as $`t,u\to1`$. At fixed $`r\lt 1`$, sufficiently strong
coupling and field eventually require four general states as well.
That exact failure of compression is not specifically an equilibrium
cost. Above the boundary, a positive exact three-state predictor is
available, so its comparison with reversible approximation is meaningful.

The [finite-rate bounds](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md) separately
show why existence of this exact difference does not guarantee a large
observable error. This note supplies no new sample count, detector
tolerance, finite-clock margin or physical memory saving.
