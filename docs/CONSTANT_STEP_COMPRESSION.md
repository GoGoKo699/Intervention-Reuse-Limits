# Constant steps need logarithmically many states; switching can need polynomially many

[Repository overview](../README.md) · [Polynomial switching lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Earlier finite-field theorem](FINITE_FIELD.md) · [Bounded-rate upper bounds](BOUNDED_RATE_FINITE_FIELD.md)

**Research theorem, 22 September 2026.** For the original reversible targets with bounded internal relaxation rates, one common Markov predictor can approximate every constant-field step with $O(\log(1/\delta))$ states. It has a fixed binary readout and a fixed full-support preparation, is irreducible and reversible at every field, and has a uniform full spectral band. Its preparation is stationary at zero field, its passive visible path is exactly the original telegraph law, and its stationary mean is exactly $\tanh h$.

The same state space and preparation serve all amplitudes. The generator may depend on the field through a general, potentially discontinuous function; the original exponential actuator rate rule is not imposed. A matching lower bound gives logarithmic worst-case state order for the menu of all constant steps. Switching requires a positive power of $1/\delta$ for a binary bounded-rate subclass, even against the broader class of arbitrary Markov predictors. These are internal derivations, not a certification of originality.

## 1. The common-model theorem

Fix $k,G,H,\Lambda>0$ and $0<W\le G^2$. Consider the original reversible target family with $|g|\le G$, $\langle g\rangle_\mu=0$, $\langle g^2\rangle_\mu=W$, and every nonzero internal relaxation rate at most $\Lambda k$. The number of hidden states, the stationary masses, and the number of distinct actuator values are unrestricted. Every experiment starts from the target's zero-field equilibrium.

For a target $F$ and one competing predictor $\widehat F$, define the constant-step error

$$
\mathcal D_H^{\rm step}(F,\widehat F)
=\sup_{|h|\le H}\sup_{t\ge0}
|m_F[h](t)-m_{\widehat F}[h](t)|,
$$

where $h$ is held constant after time zero. Competitors have a fixed initial distribution, a fixed state readout, and a generator depending only on the instantaneous field. The generator at a constant field is time homogeneous. Their rates and field dependence need not follow the original target rule.

Set

$$
R=e^{(1+G)H},\qquad
\alpha=\frac{k}{R},\qquad
B=2k(\Lambda+R),\qquad
q=1-\frac\alpha B\in(0,1).
\tag{1}
$$

For $0<\delta<1$, let

$$
r=\max\left\{1,
\left\lceil\frac{\log(4/\delta)}{-2\log q}\right\rceil
\right\}.
\tag{2}
$$

There is one predictor with

$$
\boxed{
D\le2r+2=O_{G,H,\Lambda}(\log(1/\delta)),\qquad
\mathcal D_H^{\rm step}(F,\widehat F)\le\delta.
}
\tag{3}
$$

It has all of the following properties:

- one common state space, binary readout and full-support initial distribution for every $h\in[-H,H]$;
- an irreducible reversible generator at every field, with every physical off-diagonal rate positive and all nonzero full relaxation rates in $[\alpha/2,B]$;
- initial distribution stationary under its zero-field generator, and exactly the original stationary visible telegraph path law at zero field;
- exact stationary mean $\tanh h$ for every $h$.

The upper construction does not need the fixed-variance assumption; it is included to compare with the same target family as the lower results. The constructor is supplied the kinetic target. The theorem counts physical states, not the complexity or precision of its field-dependent rate functions.

Section 7 proves a matching lower bound for the broad Markov competitor class, including arbitrary rates, real readouts and nonanalytic field dependence. Thus the worst-case common-predictor state count for all constant amplitudes is

$$
\boxed{D_*^{\rm step}(\delta)=\Theta(\log(1/\delta)).}
\tag{4}
$$

The constants may depend on $G,H,W,\Lambda$. The lower proof can choose an amplitude that shrinks with the required accuracy; it does not establish the capped lower at one fixed nonzero amplitude.

## 2. Every exact constant-step curve has a positive spectral measure

At a constant field $h$, let $Q_h$ be the target's full backward generator and $\pi_h$ its equilibrium. Write $S(A)=-1$, $S(B_j)=+1$, and $m=\tanh h$. Detailed balance in the original rate rule gives

$$
\frac{\pi_h}{\pi_0}=\frac{e^{hS}}{\cosh h},\qquad
\frac{\pi_0}{\pi_h}
=1-\frac{m}{1-m^2}(S-m).
$$

Since $Q_h$ is reversible under $\pi_h$, the mean from the prescribed initial law is

$$
\boxed{
m_F[h](t)=m\left[
1-\frac{\langle S-m,e^{tQ_h}(S-m)\rangle_{\pi_h}}
{1-m^2}\right].
}
\tag{5}
$$

The normalized covariance in (5) is a positive mixture with total mass one. Its observable is centered, so it has no zero-rate atom. Consequently

$$
m_F[h](t)=\tanh h\,[1-L_h(t)],\qquad
L_h(t)=\int e^{-\lambda t}\,\rho_h(d\lambda),
\tag{6}
$$

for a finite probability measure $\rho_h$ on the positive relaxation spectrum of $-Q_h$. At $h=0$, (5) simply gives the identically zero mean; the normalized covariance remains well defined.

### A spectral interval uniform in field and target size

Every rate from $B_j$ to $A$ is at least $\alpha$. The external-edge Dirichlet form therefore satisfies

$$
\begin{aligned}
\langle f,-Q_hf\rangle_{\pi_h}
&\ge\alpha\sum_j\pi_h(B_j)[f(B_j)-f(A)]^2\\
&\ge\alpha\operatorname{Var}_{\pi_h}(f).
\end{aligned}
$$

The final inequality follows because variance minimizes the squared distance to a constant. Internal edges contribute a nonnegative additional form. Thus every nonzero full relaxation rate is at least $\alpha$.

For the upper bound, the internal spectral cap and reversibility imply $-K_{jj}\le\Lambda k$, by applying the Rayleigh bound to a state indicator. Each external exit rate is at most $kR$, including the summed exit rate from $A$. Every full exit rate is therefore at most $k(\Lambda+R)$. Gershgorin's bound and the real reversible spectrum put every full relaxation rate at most $B$. Hence

$$
\operatorname{supp}\rho_h\subseteq[\alpha,B]
\quad\text{for every }|h|\le H.
\tag{7}
$$

## 3. Positive quadrature controls every observation time

Let $\rho$ be any probability measure on $[\alpha,B]$. Choose its positive $r$-node Gaussian quadrature $\widehat\rho$, exact on polynomials of degree at most $2r-1$. Its weights sum to one and its nodes remain in $[\alpha,B]$. If $\rho$ already has at most $r$ atoms, retain it exactly.

Expand around the upper endpoint:

$$
e^{-\lambda t}
=e^{-Bt}\sum_{j\ge0}\frac{[(B-\lambda)t]^j}{j!}.
$$

The two measures give the same integrals for terms with $j<2r$. For either positive measure, the remaining tail is bounded by

$$
\begin{aligned}
e^{-Bt}\sum_{j\ge2r}\frac{[(B-\alpha)t]^j}{j!}
&\le q^{2r}e^{-Bt}\sum_{j\ge2r}\frac{(Bt)^j}{j!}\\
&\le q^{2r}.
\end{aligned}
$$

Therefore

$$
\boxed{
\sup_{t\ge0}\left|
\int e^{-\lambda t}\rho(d\lambda)
-\int e^{-\lambda t}\widehat\rho(d\lambda)
\right|\le2q^{2r}.
}
\tag{8}
$$

Apply this to $\rho_h$ for every amplitude. With (2), each resulting mixture

$$
\widehat L_h(t)=\sum_{j=1}^{\ell(h)}w_j(h)e^{-\lambda_j(h)t},
\qquad \ell(h)\le r,
\tag{9}
$$

approximates $L_h$ within $\delta/2$ for every time. The weights are positive, sum to one, and the rates lie in $[\alpha,B]$. Zero weights can be removed and equal nodes merged.

Positive Gaussian quadrature and the associated Jacobi realization are standard ingredients, also used in the [earlier positive-kernel approximation](FINITE_ACCURACY.md). A list of mixtures indexed by $h$ is not yet a common predictor. The next two sections realize all of them on the same state labels with a fixed readout and preparation.

## 4. An exact common reversible realization of the approximating mixtures

First use a preparation supported on two roots. Section 5 replaces it by the full-support stationary preparation needed in the theorem.

### Fixed state labels and binary readout

Allocate two blocks, each of size $r+1$, with states $(-,0),\ldots,(-,r)$ and $(+,0),\ldots,(+,r)$. Define the readout once:

$$
S(-,0)=-1,\quad S(-,j)=+1\ (j\ge1),
$$

$$
S(+,0)=+1,\quad S(+,j)=-1\ (j\ge1).
$$

Let $\rho$ put probability $1/2$ at each root and zero elsewhere. Set $\varepsilon=\alpha/2$.

### A reversible active core at a nonzero field

For $h>0$, put $u=\tanh h\in(0,1)$, $p=1-u$, and $\nu_j=\lambda_j(h)-\varepsilon>0$. The probability measure

$$
p\delta_0+u\sum_{j=1}^{\ell(h)}w_j(h)\delta_{-\nu_j}
\tag{10}
$$

has an irreducible reversible birth-death realization on $\ell(h)+1$ states whose root return probability is

$$
P_{00}(t)=p+u\sum_jw_j(h)e^{-\nu_jt}.
\tag{11}
$$

This is the [positive Jacobi construction](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel), with root mass $p$ in place of $1/2$. For completeness, form the Jacobi matrix of (10), with positive off-diagonals. Its largest eigenvalue is zero; its normalized Perron eigenvector $v$ is strictly positive. Diagonal similarity by $\operatorname{diag}(v)$ gives a Markov generator reversible under $v_i^2$. The root spectral weight at zero is $v_0^2=p$, and its return function is (11).

Place this core in the first block, using its root and $\ell(h)$ nonroot states. Freeze every remaining coordinate, including any padded coordinates in that block. Denote the reducible generator by $Q_h^{\rm base}$. From the fixed preparation $\rho$, its mean is

$$
m_h^{\rm base}(t)
=1-P_{00}(t)
=u\left[1-\sum_jw_j(h)e^{-\nu_jt}\right].
\tag{12}
$$

For $h<0$, activate the mirror core in the second block with $u=|\tanh h|$. Its mean is the negative of (12). Thus in both cases the coefficient in front is $\tanh h$.

### A full-support stationary law with the desired mean

For $h>0$, give the active core total stationary mass $1/4$, distributed according to its positive reversible stationary law. Its conditional stationary readout mean is $2u-1$.

The frozen complement contains both readout signs, including when padding is needed. Give it total mass $3/4$ and conditional readout mean

$$
v_f=\frac{2u+1}{3}\in(-1,1).
$$

For example, assign total fractions $(1+v_f)/2$ and $(1-v_f)/2$ within that complement to its positive and negative states, uniformly within each sign class. This defines a strictly positive stationary law $\widehat\pi_h$ reversible for $Q_h^{\rm base}$, with

$$
\widehat\pi_hS
=\frac14(2u-1)+\frac34\frac{2u+1}{3}=u.
$$

For $h<0$, reverse the signs and use frozen-complement mean $-(2u+1)/3$. In every case $\widehat\pi_hS=\tanh h$. The mass $1/4$ is assigned only to the active core; padded states belong to the frozen complement.

### A stationary reset makes the full generator irreducible

For $h\ne0$, define

$$
\boxed{
\widehat Q_h=Q_h^{\rm base}
+\varepsilon(\mathbf1\widehat\pi_h-I).
}
\tag{13}
$$

Both terms are reversible under $\widehat\pi_h$. Every off-diagonal entry receives the positive reset rate $\varepsilon\widehat\pi_h(j)$, so the full generator is irreducible. Because the stationary projection commutes with $Q_h^{\rm base}$,

$$
e^{t\widehat Q_h}
=e^{-\varepsilon t}e^{tQ_h^{\rm base}}
+(1-e^{-\varepsilon t})\mathbf1\widehat\pi_h.
\tag{14}
$$

Combining (12)--(14) proves the exact common-preparation identity

$$
\boxed{
\rho e^{t\widehat Q_h}S
=\tanh h\,[1-\widehat L_h(t)].
}
\tag{15}
$$

On the orthogonal complement of constants, the reset shifts each relaxation rate upward by $\varepsilon$. The active rates $\nu_j$ become $\lambda_j(h)$; the remaining component-constant zero modes become $\varepsilon$. Thus the nonzero full spectrum lies in $[\alpha/2,B]$. No states or approximation error were added by the reset.

## 5. Fixed stationary preparation and exact passive calibration

Let $U$ be uniform on the $2r+2$ state labels. It is sign balanced because the fixed readout has $r+1$ states of each sign. Put

$$
\zeta=\frac\delta4,\qquad
\boxed{\sigma=(1-\zeta)\rho+\zeta U.}
\tag{16}
$$

This full-support probability law is fixed independently of $h$ and has mean zero. For every nonzero constant field, retain the generator (13) and start it from $\sigma$. Since a Markov propagator contracts the supremum norm of the fixed binary readout,

$$
|\sigma e^{t\widehat Q_h}S-\rho e^{t\widehat Q_h}S|
\le\|\sigma-\rho\|_1\le2\zeta=\delta/2
\tag{17}
$$

uniformly in $h,t$. The quadrature error in (8) contributes at most another $\delta/2$. This proves (3) for $h\ne0$. Irreducibility still gives exact limiting mean $\widehat\pi_hS=\tanh h$ from this preparation.

At zero field define separately

$$
\boxed{\widehat Q_0=2k(\mathbf1\sigma-I).}
\tag{18}
$$

This generator is irreducible and reversible under $\sigma$, so the fixed preparation is stationary at zero field. From every microscopic state, the total rate to the opposite readout sign is $2k\cdot\tfrac12=k$. Strong lumpability therefore gives exactly the rate-$k$ visible telegraph process. Its initial signs are equiprobable, so its complete visible path law is the original stationary passive law. Its mean and stationary mean are zero.

All nonzero eigenvalues of $-\widehat Q_0$ equal $2k$, which lies in $[\alpha/2,B]$. Thus all spectral, positivity, reversibility and preparation assertions hold also at zero field.

## 6. This is one model for every field, with an explicit scope

The state labels, readout and preparation in (16) are fixed before the field is chosen. The construction supplies a single function $h\mapsto\widehat Q_h$ on $[-H,H]$. Varying quadrature nodes and weights become entries of this field-dependent generator; they do not change the state space or reprepare the model.

The finite quadrature and Jacobi rules can be selected in Borel fashion by ordering nodes and using rank-based padding when moment matrices degenerate. All exit rates are uniformly bounded by $B$, as follows from the full spectral cap and reversibility. Hence this generator function defines Markov evolution for bounded piecewise-continuous protocols. The theorem guarantees accuracy for constant steps only; it makes no accuracy assertion after subsequent switching.

Field continuity or analyticity is not imposed. In particular the separate zero-field definition can be discontinuous. The predictor need not follow the original exponential external rate rule or carry the original stationary actuator distribution. Its stationary measure at nonzero field need not be the exponential tilt of $\sigma$. These restrictions matter: the construction is a reversible predictor in the broad Markov comparison class, not an upper theorem within the original actuator family.

It nevertheless preserves zero-field hidden stationarity, the entire passive visible path law, binary readout, irreducibility, a uniform full spectral band and the exact stationary response curve. It does not settle whether a polynomial-size reversible predictor in the original rate-rule family suffices for arbitrary switching. No statistical sample bound or bound on field-function complexity is proved here.

## 7. A matching logarithmic lower bound for every positive internal cap

The capped lower argument in [FINITE_FIELD.md, Sections 7--8](FINITE_FIELD.md#8-the-capped-lower-bound) already uses only constant steps and permits the broad competitor class. Its displayed example has internal rates in $[2k,3k]$. The following change of interval extends the logarithmic lower to every fixed $\Lambda>0$.

Fix $D\ge2$, put $r_0=D+4$ and $s=\sqrt W$, and define

$$
\eta=\min\{\Lambda/2,1/2\},\qquad
\frac{\lambda_j}{k}
=\frac\eta2+\frac{\eta(j-1)}{2(r_0-1)},\qquad
c_j=\frac W{r_0},\quad 1\le j\le r_0.
$$

These distinct internal rates lie in $(0,\Lambda k]$ and are separated from $k$. The positive Jacobi target realization has precisely these nonzero internal rates and has $g=\pm s$ with mass $1/2$ at each level. It is therefore in the target class of Section 1.

In dimensionless time $\tau=kt$, its cubic step response has the established decomposition

$$
m_3(\tau)=B_0(\tau)-\sum_{j=1}^{r_0}w_je^{-\beta_j\tau},
\quad
B_0(\tau)=b_0+(b_1+b_2\tau)e^{-2\tau},
$$

$$
\beta_j=1+\lambda_j/k,\qquad
w_j=\frac{2W}{r_0(1-\lambda_j/k)^2}\ge\frac{2W}{r_0}.
$$

For the positive Hankel operator of the exponential sum on $L^2(e^{-\tau}d\tau)$, set $a_j=\beta_j+1/2\le2$. Its Cauchy Gram matrix is $C_{ij}=1/(a_i+a_j)$. The inverse diagonal identity and the equally spaced nodes give

$$
(C^{-1})_{ii}
=2a_i\prod_{j\ne i}\left(\frac{a_i+a_j}{a_i-a_j}\right)^2,
$$

$$
\prod_{j\ne i}\frac{a_i+a_j}{|a_i-a_j|}
\le\frac{[8(r_0-1)/\eta]^{r_0-1}}{(i-1)!(r_0-i)!}
\le(16e/\eta)^{r_0-1}.
$$

Consequently the least positive Hankel eigenvalue is at least

$$
\boxed{
\sigma_{r_0}
=\frac{W}{2r_0^2(16e/\eta)^{2r_0-2}}.
}
\tag{19}
$$

Only the target is Taylor expanded. The [uniform target remainder](FINITE_FIELD.md#6-a-taylor-remainder-uniform-in-size-and-horizon) is at most $R_H z^4$ at amplitude $0<z\le H$, where

$$
R_H=\frac{365}{12}e^{2(1+s)H}(1+s)^4.
$$

A $D$-state competitor's exact constant-field mean has Hankel rank at most $D$. Subtracting the baseline $z m_1+z^3B_0$ increases this by at most three, since that baseline lies in the span of $1,e^{-2\tau},\tau e^{-2\tau}$. The positive target sum has rank $r_0=D+4$. Therefore any uniform mean error $e_D$ must obey

$$
e_D+R_Hz^4\ge z^3\sigma_{r_0}.
$$

Choose

$$
z_D=\min\{H,\sigma_{r_0}/(2R_H)\}.
$$

Then

$$
\boxed{e_D\ge\tfrac12\sigma_{r_0}z_D^3.}
\tag{20}
$$

For large $D$ the right-hand side is exponential in $-D$ up to polynomial factors, and hence is bounded below by $c e^{-CD}$ for fixed positive constants. This proves $D_*^{\rm step}(\delta)=\Omega(\log(1/\delta))$ and, with (3), the matching order (4). The lower remains valid for the more structured reversible predictor class supplied by the upper theorem, because it already permits arbitrary Markov competitors.

The witness amplitude $z_D$ shrinks. This is sufficient for the common all-amplitudes step task, and makes no inference about derivatives of a competitor from its finite-field accuracy.

## 8. What switching adds

For this comparison, take $\Lambda=5/2$ and apply the upper theorem to the binary shift-register targets. All their constant steps admit one common predictor with $O(\log(1/\delta))$ states and all the structural properties above. In contrast, the [polynomial controlled lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) requires at least $c_a\delta^{-\gamma_a}$ states when switching is included, for every fixed minimum dwell $a/k$. That lower allows arbitrary competing rates, nonreversibility and nonanalytic field dependence.

Thus the logarithmic-versus-polynomial difference is caused by the enlarged experiment menu. It does not compare a separate predictor at each constant amplitude against one common switching predictor. Both tasks use a single field-dependent Markov model with fixed preparation and readout. The upper controls every observation time for constant steps; the switching lower already has witnesses of horizon $O_a(\log(1/\delta)/k)$.

This comparison does not assert that every individual target is difficult under switching or that the switching exponent is optimal. It also leaves open corresponding sharp bounds under additional field regularity or the original actuator rate rule.
