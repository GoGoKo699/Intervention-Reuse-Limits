# Matching tolerance order without a rate cap

[Repository overview](../README.md) · [Approximation task](FINITE_ACCURACY.md#0-the-approximation-task-and-its-quantifiers) · [Core model](THEORY.md) · [Prior art](PRIOR_ART.md)

**Working theorem, 22 September 2026.** The proof below closes the
logarithmic versus squared-logarithmic state-count gap for the minimax
problem in [Finite accuracy, Section 0](FINITE_ACCURACY.md). Its lower
bound uses the actual cubic response error and applies to the full
analytic Markov surrogate class. The Hankel-rank and Cauchy-matrix tools
are established mathematics; publication-level originality of their
application here remains a separate question.

## 1. Statement and quantifiers

Keep $k>0$, $U>0$, and $0<W\le G^2$ fixed. The target class
$\mathcal F(k,G,W)$ and broad surrogate class $\mathcal A_D(k)$ are exactly
those in the finite-accuracy note. In particular the target spectral range
is unrestricted, whereas a surrogate need not be reversible, possess a
positive memory kernel, or satisfy a rate-derivative bound.

**Theorem.** For each integer $D\ge2$, set $r=3D+2$. Then

$$
\boxed{
E_D(k,G,W,U)\ge
\frac{U^3W}{64r^2}
\exp\!\left[-2\pi\sqrt{3(r-1)}\right].
}
$$

A witnessing target has $r+2=3D+4$ states, $|g_i|=\sqrt W$, and a finite
positive kernel of mass $W$. Only its response to the constant protocol
$u=U$ is used. The target depends on $D$; the theorem is a worst-case
compression statement, not a claim that one fixed finite target requires
an unbounded number of states.

Combining this lower bound with the constructive upper bound in
[Finite accuracy, Section 8](FINITE_ACCURACY.md#8-a-stronger-bound-by-positive-gaussian-quadrature)
gives the order

$$
\boxed{
D_*(\varepsilon)=
\Theta\!\left(\left[\log\frac{U^3W}{\varepsilon}\right]^2\right)
\quad(\varepsilon\downarrow0),
}
$$

where $D_*(\varepsilon)=\min\{D\ge2:E_D\le\varepsilon\}$.
The constants in the exponential error rates are not matched. The cases
$W=0$ or $U=0$ have no cubic correction to approximate and are excluded
from this small-tolerance statement.

## 2. A continuous Hankel operator measured in the response norm

Use dimensionless time $\tau=kt$ and the probability measure

$$
d\mu(\tau)=e^{-\tau}\,d\tau,\qquad \tau\ge0.
$$

For a cubic step curve $s(\tau)=m_3[U](\tau/k)$, define the integral
operator on $L^2(\mu)$ by

$$
(\mathsf H_s f)(\tau)
=\int_0^\infty s(\tau+\sigma)f(\sigma)\,d\mu(\sigma).
$$

If two curves differ by at most $\varepsilon$ at every nonnegative time,
then

$$
\|\mathsf H_s-\mathsf H_{\widehat s}\|_{2\to2}
\le\varepsilon.
$$

Indeed, the absolute value of their bilinear form is at most
$\varepsilon\|f\|_{L^1(\mu)}\|g\|_{L^1(\mu)}$, and each $L^1$ norm is at
most the corresponding $L^2$ norm because $\mu$ has mass one. Thus this
operator error is controlled directly by the specified response norm.
No derivative of an approximate curve and no assumption about the
surrogate's response kernel enters this step.

### Finite rank for every admissible surrogate

For a surrogate with $d\le D$ states, stationarity of its fixed preparation
and conservation of probability give the cubic coefficient hierarchy on
$\mathbb R\oplus V\oplus V\oplus V$, where
$V=\{v:\mathbf1^Tv=0\}$ has dimension $d-1$. Explicitly, if $L_j$ are the
coefficients of its step generator and $p_0$ is the stationary
preparation, then

$$
\begin{aligned}
\dot p_1&=L_0p_1+L_1p_0,\\
\dot p_2&=L_0p_2+L_1p_1+L_2p_0,\\
\dot p_3&=L_0p_3+L_1p_2+L_2p_1+L_3p_0.
\end{aligned}
$$

Adjoining a constant coordinate yields a matrix $\mathcal L$ of dimension
$3d-2$. After rescaling time, the scalar cubic curve has the form
$\widehat s(\tau)=\ell^Te^{\mathcal L\tau}z_0$. Therefore

$$
\widehat s(\tau+\sigma)
=\ell^Te^{\mathcal L\tau}e^{\mathcal L\sigma}z_0
$$

is a sum of at most $3d-2$ separable terms, so

$$
\operatorname{rank}\mathsf H_{\widehat s}\le3d-2\le3D-2.
$$

These terms define bounded finite-rank operators on $L^2(\mu)$.
The eigenvalues of $L_0$ have nonpositive real parts because it is a
Markov generator. The augmented hierarchy repeats those eigenvalues and
adds a zero eigenvalue. Its matrix exponential therefore grows at most
polynomially, including in reducible or defective cases. Every resulting
coordinate function lies in $L^2(e^{-\tau}d\tau)$.
Neither irreducibility nor diagonalizability of the surrogate is needed.

## 3. A target with a geometrically spaced spectrum

For the moment let $\eta>0$ be arbitrary. For $1\le j\le r$, put

$$
a_j=4e^{(j-1)\eta},\qquad
\beta_j=a_j-\frac12,\qquad
\lambda_j=k\left(a_j-\frac32\right),\qquad
c_j=\frac Wr.
$$

Then $\beta_j=1+\lambda_j/k$, the rates $\lambda_j$ are distinct and
strictly positive, and their minimum is $5k/2$. The kernel

$$
C(t)=\sum_{j=1}^rc_je^{-\lambda_jt}
$$

has mass $W$. The Jacobi construction in
[Theory, Section 9](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel)
realizes it as a target with $r+2$ states, $|g_i|=\sqrt W\le G$, and all the
required passive and low-order response properties.

The exact cubic step formula gives

$$
s(\tau)=B(\tau)-\sum_{j=1}^rw_je^{-\beta_j\tau},\qquad
B(\tau)=b_0+(b_1+b_2\tau)e^{-2\tau},
$$

for real constants $b_0,b_1,b_2$, where

$$
w_j=\frac{2U^3c_j}{(1-\lambda_j/k)^2}
=\frac{2U^3W}{r(a_j-5/2)^2}>0.
$$

The factor $U^3$ follows from homogeneity of a third-order coefficient
under a constant protocol. The baseline has Hankel rank at most three:
the constant contributes rank one, and
$(b_1+b_2(\tau+\sigma))e^{-2(\tau+\sigma)}$ contributes at most two.

Write

$$
\mathsf K=\sum_{j=1}^rw_j\,\phi_j\otimes\phi_j,
\qquad \phi_j(\tau)=e^{-\beta_j\tau}.
$$

Then $\mathsf H_s=\mathsf H_B-\mathsf K$. For any admissible surrogate,

$$
\operatorname{rank}(\mathsf H_B-\mathsf H_{\widehat s})
\le3+(3D-2)=3D+1=r-1.
$$

Because $\mathsf K$ is positive with rank $r$, its smallest nonzero
eigenvalue bounds its distance in operator norm to every operator of rank
at most $r-1$. For a direct proof, restrict the latter operator to the
$r$-dimensional range of $\mathsf K$ and choose a unit vector in its
nullspace; $\mathsf K$ has norm at least its smallest positive eigenvalue
on that vector. Consequently,

$$
\mathcal E_U(F,\widehat F)
\ge\|\mathsf H_s-\mathsf H_{\widehat s}\|_{2\to2}
\ge\lambda_{\min}^{+}(\mathsf K).
$$

## 4. The Cauchy Gram matrix

The Gram matrix of the functions $\phi_j$ is

$$
\mathsf C_{ij}
=\int_0^\infty e^{-(\beta_i+\beta_j)\tau}e^{-\tau}\,d\tau
=\frac1{a_i+a_j}.
$$

Distinct exponentials are linearly independent, so $\mathsf C$ is positive
definite. The positive eigenvalues of $\mathsf K$ are those of
$\operatorname{diag}(\sqrt w)\mathsf C\operatorname{diag}(\sqrt w)$.
Let $a_{\max}=4e^{(r-1)\eta}$. Since
$(a_j-5/2)^2\le a_{\max}^2$,

$$
\lambda_{\min}^{+}(\mathsf K)
\ge\frac{2U^3W}{r a_{\max}^2}\lambda_{\min}(\mathsf C).
$$

The diagonal entries of the inverse of this Cauchy matrix are

$$
(\mathsf C^{-1})_{ii}
=2a_i\prod_{j\ne i}\left(\frac{a_i+a_j}{a_i-a_j}\right)^2.
$$

One way to verify the formula is to solve $\mathsf Cx=e_i$ using the
rational function $R(z)=\sum_jx_j/(z+a_j)$. Its values at $a_\ell$ are
$\delta_{i\ell}$. Its numerator is therefore proportional to
$\prod_{\ell\ne i}(z-a_\ell)$. Normalizing $R(a_i)=1$ and taking its
residue at $z=-a_i$ gives the displayed diagonal entry.

Geometric spacing gives

$$
\left|\frac{a_i+a_j}{a_i-a_j}\right|
=\coth\!\left(\frac{|i-j|\eta}{2}\right).
$$

Each positive integer distance occurs at most twice. The function
$f(x)=\log\coth(x/2)$ is positive and decreasing for $x>0$, so

$$
\begin{aligned}
\log\prod_{j\ne i}\left(\frac{a_i+a_j}{a_i-a_j}\right)^2
&\le4\sum_{m=1}^\infty f(m\eta)\\
&\le\frac4\eta\int_0^\infty f(x)\,dx
=\frac{\pi^2}{\eta}.
\end{aligned}
$$

For completeness, the integral follows from the positive series

$$
f(x)=\log\frac{1+e^{-x}}{1-e^{-x}}
=2\sum_{\substack{n\ge1\\n\ {\rm odd}}}\frac{e^{-nx}}n,
\qquad
\int_0^\infty f(x)\,dx
=2\sum_{n\ {\rm odd}}\frac1{n^2}=\frac{\pi^2}{4}.
$$

Termwise integration is justified by nonnegativity. Comparing the
decreasing function with its left-hand integrals justifies the preceding
sum bound even though $f$ is unbounded at zero.

Since the inverse is positive definite,

$$
\|\mathsf C^{-1}\|_2
\le\operatorname{tr}(\mathsf C^{-1})
\le2r a_{\max}e^{\pi^2/\eta}.
$$

It follows that

$$
\lambda_{\min}^{+}(\mathsf K)
\ge\frac{U^3W}{r^2a_{\max}^3}e^{-\pi^2/\eta}
=\frac{U^3W}{64r^2}
\exp\!\left[-3(r-1)\eta-\frac{\pi^2}{\eta}\right].
$$

Choose

$$
\eta=\frac{\pi}{\sqrt{3(r-1)}}.
$$

The two terms in the exponent are then equal, proving the theorem.
The bound holds for every admissible surrogate for this target; taking
the infimum over surrogates and then the supremum over targets proves the
claimed minimax inequality.

## 5. A finite observation horizon suffices

The all-horizon norm makes the probability-measure argument natural, but
the obstruction can also be placed on an explicit finite horizon.
For the same target and optimized $\eta$, define the dimensionless cutoff

$$
T_r=\frac18\left[
\frac{\pi^2}{\eta}+(r-1)\eta+\log(2r^2)
\right].
$$

Use the subprobability measure $e^{-\tau}\mathbf1_{[0,T_r]}d\tau$.
Its mass is at most one, so the response-to-operator error bound is
unchanged. Its exponential Gram matrix is

$$
(\mathsf C_{T_r})_{ij}
=\frac{1-e^{-(a_i+a_j)T_r}}{a_i+a_j}.
$$

The omitted tail is positive semidefinite, with

$$
\|\mathsf C-\mathsf C_{T_r}\|_2
\le\operatorname{tr}(\mathsf C-\mathsf C_{T_r})
=\sum_j\frac{e^{-2a_jT_r}}{2a_j}
\le\frac r8e^{-8T_r}
=\frac{e^{-\pi^2/\eta}}{4r a_{\max}}.
$$

The last expression is half the lower bound on
$\lambda_{\min}(\mathsf C)$ established above. Thus truncation loses at
most a factor of two in the final bound. Every admissible surrogate
satisfies

$$
\boxed{
\sup_{0\le t\le2T_r/k}
|m_{3,F}[U](t)-m_{3,\widehat F}[U](t)|
\ge\frac{U^3W}{128r^2}
e^{-2\pi\sqrt{3(r-1)}}.
}
$$

Only a constant protocol and response times up to
$2T_r/k=O(\sqrt D/k)$ are needed. This is a finite-horizon statement, not
a claim about a finite number of measurements, prescribed temporal
resolution, or stable statistical reconstruction.

## 6. Consequences and limits

If $E_D\le\varepsilon$, the main theorem implies

$$
\log\frac{U^3W}{\varepsilon}
\le\log64+2\log(3D+2)+2\pi\sqrt{3(3D+1)}.
$$

Hence $D_*(\varepsilon)=\Omega(\log^2(U^3W/\varepsilon))$.
The existing positive-quadrature construction supplies the matching
$O(\log^2(U^3W/\varepsilon))$ upper bound with a reversible surrogate.
This proves the optimal asymptotic **order** for the original broad
minimax problem, while leaving the optimal constants open.

The hard targets have

$$
\frac{\lambda_{\max}}k
=4\exp\!\left[\pi\sqrt{\frac{r-1}{3}}\right]-\frac32.
$$

Their active spectral range increases with the state budget. This is
consistent with the logarithmic state-count order already established
for targets with a fixed upper bound on active rates. No lower bound on
the hidden gap is needed in that capped problem; here the hard targets
actually have a fixed positive gap.

The theorem concerns a known-model compression task and Taylor
coefficients, with state count as the resource. It imposes no surrogate
bit-precision cost and provides no uniform finite-field remainder,
kernel-learning guarantee, or noise-robust experimental procedure.
Exact passive path equality and low-order response constraints remain
those of the original model and comparison class. No turbulence or
molecular-system claim is inferred.
