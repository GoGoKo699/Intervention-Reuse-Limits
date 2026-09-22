# Preserving structure at the same state-growth order

[Repository overview](../README.md) · [Publication scope](PUBLICATION_SCOPE.md) · [Approximation task](FINITE_ACCURACY.md)

**Corollary, 22 September 2026.**

The strongest lower-bound proof does not use the surrogate's passive path
law, equilibrium curve, or linear and quadratic response constraints. Its
state-count obstruction therefore also applies after those requirements
are removed. This gives a precise interpretation of the upper construction:
preserving the specified Markov structure costs no additional asymptotic
order in the number of states required for cubic-coefficient accuracy.
This is a consequence of the existing proofs, not a new approximation
mechanism or a claim that preservation is free at every finite state budget.

## Three nested comparison classes

Keep $k>0$, $U>0$, and $0<W\le G^2$ fixed. Let $\mathcal B_D$ contain all
models with at most $D$ states, a Markov generator analytic in the same
instantaneous scalar field near zero, a fixed zero-field stationary
preparation, and a fixed real-valued state readout. These models need not
match the target's passive law, equilibrium curve, linear response, or
quadratic response. Their readout need not be binary. Only their cubic
coefficient is compared with the target in the norm $\mathcal E_U$ of
[Finite accuracy, Section 0](FINITE_ACCURACY.md#0-the-approximation-task-and-its-quantifiers).
In particular, this relaxed comparison is **not** a claim of approximation
of the full mean, its lower-order coefficients, or finite-field outputs.

Let $\mathcal A_D(k)$ be the original broad comparison class, with the
passive, static, linear, and quadratic requirements stated there. Finally,
let $\mathcal R_D(k,G,W)$ consist of models in the original reversible
rate-rule family with at most $D$ states, the same $k,W$, and
$|\widehat g|\le G$. Then

$$
\mathcal R_D(k,G,W)\subseteq\mathcal A_D(k)\subseteq\mathcal B_D.
$$

For either the unrestricted target class $\mathcal F_\infty=\mathcal F(k,G,W)$
or its subclass $\mathcal F_3$ with all active rates at most $3k$, define

$$
E_{D,\Lambda}^{\mathcal X}
=\sup_{F\in\mathcal F_\Lambda}\;
\inf_{\widehat F\in\mathcal X_D}\mathcal E_U(F,\widehat F),
\qquad \Lambda\in\{\infty,3\},\quad
\mathcal X\in\{\mathcal B,\mathcal A,\mathcal R\}.
$$

The arguments of $\mathcal A_D$ and $\mathcal R_D$ are suppressed in this
notation. The inclusions give

$$
E_{D,\Lambda}^{\mathcal B}
\le E_{D,\Lambda}^{\mathcal A}
\le E_{D,\Lambda}^{\mathcal R}.
$$

An empty restricted class at a very small state budget has infimum
$+\infty$; this does not affect the small-tolerance asymptotics below.
The target cap restricts $\mathcal F_3$, and does not restrict
$\mathcal B_D$ or $\mathcal A_D$.

## The lower bounds survive the relaxation

For any member of $\mathcal B_D$ with $d\le D$ states, the constant-step
cubic coefficient has the same linear lift of dimension $3d-2$ used in
[the unrestricted-rate proof](UNRESTRICTED_RATE_LOWER_BOUND.md).
Stationarity fixes the zeroth-order probability vector; probability
conservation puts each of its first three coefficient vectors in the
$(d-1)$-dimensional zero-sum subspace. The readout is just a fixed linear
functional on the third coefficient. This reasoning does not invoke any
of the constraints removed in $\mathcal B_D$.

The continuous Hankel operator therefore still has rank at most $3D-2$.
The geometric-spectrum target, Cauchy inverse estimate, and conversion
from uniform step error to operator error are unchanged. With $r=3D+2$,

$$
E_{D,\infty}^{\mathcal B}
\ge\frac{WU^3}{64r^2}
\exp\!\left[-2\pi\sqrt{3(r-1)}\right]
\qquad(D\ge2).
$$

The capped-target argument requires only a small change to
[Finite accuracy, Section 10](FINITE_ACCURACY.md#10-a-logarithmic-state-lower-bound-in-the-response-norm).
Sample the lifted cubic curve at spacing $\Delta=\log(2)/k$, and apply
$P(\mathsf E)$ with $P(z)=(z-1)(z-1/4)^2$. Even without a prescribed
passive eigenvalue, filtering cannot increase the lift rank: if
$s_n=\ell^TT^nz_0$, then

$$
(P(\mathsf E)s)_n=\ell^TT^nP(T)z_0,
$$

whose sampled Hankel matrices have rank at most $3d-2$.
One must not use the stronger $3d-5$ rank estimate here; that estimate
used the original passive-law constraint.

Choose $r=3D-1$, take the same equally spaced nodes
$x_j\in[1/16,1/8]$, and set
$\lambda_j=k(-\log_2x_j-1)$ and $c_j=W/r$. This admissible target has
rates in $[2k,3k]$. Its filtered Hankel matrix has rank $r$, while every
relaxed surrogate's matrix has rank at most $r-1$. The positive-weight,
Vandermonde, and filter-error estimates in Section 10 apply to every such
$r$, yielding

$$
E_{D,3}^{\mathcal B}
\ge\frac{7WU^3}{3200r^3(36e)^{2r-2}},
\qquad r=3D-1,\quad D\ge2.
$$

This witness uses raw coefficient samples through
$(2r+1)\Delta=(6D-1)\log(2)/k$. It imposes no passive matching or readout
restriction on the relaxed surrogate.

## The constructive upper bounds retain all the structure

The existing quadrature and Jacobi construction belongs to
$\mathcal R_D(k,G,W)$. For every integer $n\ge1$, it gives

$$
E_{2n(n+1)+3,\infty}^{\mathcal R}
\le8WU^3\,16^{-n},
\qquad
E_{2n+2,3}^{\mathcal R}
\le8WU^3\,16^{-n}.
$$

The second construction even keeps its active surrogate rates within the
target cap, although that additional preservation is not needed for the
class comparison.

For each class, write
$D_{*,\Lambda}^{\mathcal X}(\varepsilon)
=\min\{D\ge2:E_{D,\Lambda}^{\mathcal X}\le\varepsilon\}$.
Sandwiching the relaxed lower bounds and the restricted upper bounds
shows that, at fixed positive $WU^3$ and as $\varepsilon\downarrow0$,

$$
D_{*,\infty}^{\mathcal X}
=\Theta\!\left(\log^2\frac{WU^3}{\varepsilon}\right),
$$

and

$$
D_{*,3}^{\mathcal X}
=\Theta\!\left(\log\frac{WU^3}{\varepsilon}\right).
$$

Both statements hold for every $\mathcal X\in\{\mathcal B,\mathcal A,\mathcal R\}$.

Thus the asymptotic exponent is not a penalty caused by demanding the
correct passive law. It is an approximation obstruction already present
in the relaxed cubic task. The constructive result shows that reversibility,
bounded sensitivity, the exact passive law, and the specified lower-order
response can all be retained at that same state-growth order.
This establishes neither equality of the three minimax errors at fixed
$D$ nor equality of leading constants. It also does not extend the lower
bound to arbitrary nonlinear differential equations, time-dependent
controllers, field-dependent readouts, or non-Markov memory models.
