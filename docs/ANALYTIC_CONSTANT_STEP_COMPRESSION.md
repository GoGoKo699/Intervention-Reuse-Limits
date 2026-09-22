# Analytic constant-step compression with exact passive and low-order calibration

[Repository overview](../README.md) · [Constant-step theorem and matching lower bound](CONSTANT_STEP_COMPRESSION.md) · [Polynomial switching lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md)

**Research theorem, 22 September 2026.** The logarithmic constant-step upper bound can be attained by a predictor whose generator is real analytic in the field. It retains one fixed binary readout and one fixed full-support stationary zero-field preparation, positive physical rates, reversibility, a uniform full spectral band, the exact passive visible path law, and the exact stationary mean. Its linear mean response and zero quadratic mean response also agree with the original family for every bounded weak protocol.

The construction uses regularized spectral moments, two continuously active Jacobi cores, and an analytic stationary-reset interpolation near zero field. The state order remains $O(\log(1/\delta))$. The field derivatives are not bounded uniformly as $\delta\downarrow0$, and the original exponential actuator rate rule is not imposed. These are internal derivations, not a certification of originality.

## 1. Statement and parameters

Use the target family and constant-step norm in [CONSTANT_STEP_COMPRESSION.md](CONSTANT_STEP_COMPRESSION.md): fix $k,G,H,\Lambda>0$, with original reversible targets satisfying $|g|\le G$ and internal relaxation rates at most $\Lambda k$. One model must predict every constant amplitude $|h|\le H$ and every observation time from the prescribed preparation. A fixed positive variance $0<W\le G^2$ may also be imposed; the upper proof does not need it.

Write

$$
R=e^{(1+G)H},\qquad
\alpha=k/R,\qquad B=2k(\Lambda+R),\qquad
q=1-\alpha/B,\qquad \varepsilon=\alpha/2.
\tag{1}
$$

For $0<\delta<1$, choose

$$
\xi=\delta/4,\qquad
r=\max\left\{1,
\left\lceil\frac{\log(8/\delta)}{-2\log q}\right\rceil
\right\},
\tag{2}
$$

$$
\tau=\frac{\delta(1-\tanh H)}4,
\qquad
\eta=\frac{\alpha\delta}{2B},
\qquad
\chi(h)=\frac{h^2}{h^2+\eta^2}.
\tag{3}
$$

There is a predictor on $2r+2$ states with

$$
\boxed{
\sup_{|h|\le H}\sup_{t\ge0}
|m_F[h](t)-m_{\widehat F}[h](t)|\le\delta,
\qquad D=O_{G,H,\Lambda}(\log(1/\delta)).
}
\tag{4}
$$

Its generator is real analytic on an open real neighborhood of $[-H,H]$. For every allowed field it is irreducible and reversible, every physical off-diagonal entry is positive, and every nonzero full relaxation rate lies in $[\alpha/2,B]$. It has a fixed binary readout $S$ and a fixed full-support initial distribution $\sigma$ which is stationary at zero field. At zero field its complete stationary visible path is exactly the rate-$k$ telegraph law. Its stationary mean is exactly $\tanh h$.

For any bounded piecewise-continuous protocol $u(t)$, expand the mean under the weak field $h(t)=z u(t)$ as $z m_1[u]+z^2m_2[u]+\cdots$. The same predictor satisfies

$$
\boxed{
m_1[u](t)=2k\int_0^t e^{-2k(t-s)}u(s)\,ds,
\qquad m_2[u](t)=0.
}
\tag{5}
$$

No accuracy assertion is made for general finite-amplitude switching. The rate functions need not have the original actuator form, and their derivatives can depend on the requested tolerance.

## 2. Analytic positive quadrature without rank changes

Let $Q_h$ and $\pi_h$ be the original target generator and equilibrium, and put $m(h)=\tanh h$. The [equilibrium-tilt identity](CONSTANT_STEP_COMPRESSION.md#2-every-exact-constant-step-curve-has-a-positive-spectral-measure) gives

$$
m_F[h](t)=m(h)[1-L_h(t)],\qquad
L_h(t)=\int_{\alpha}^{B}e^{-\lambda t}\,\rho_h(d\lambda),
\tag{6}
$$

where $\rho_h$ is a probability measure. Its support can change with $h$, which prevents direct use of a fixed-rank quadrature construction. Its moments, however, are real analytic:

$$
\mu_j(h)=
\frac{\langle S-m(h),(-Q_h)^j(S-m(h))\rangle_{\pi_h}}
{1-m(h)^2},\qquad j\ge0.
\tag{7}
$$

The target rate rule, equilibrium and denominator in (7) are analytic, with $1-m(h)^2>0$ on the real field interval.

Let $V$ be the uniform probability measure on $[\alpha,B]$ and set

$$
\rho_h^{\xi}=(1-\xi)\rho_h+\xi V.
\tag{8}
$$

Every finite polynomial Gram matrix of this measure is strictly positive definite: the fixed uniform component gives a positive integral for the square of every nonzero polynomial. All its moments are analytic in $h$. Finite Gram--Schmidt, using positive norm square roots, therefore gives an analytic $r\times r$ Jacobi matrix $J_h$ for the $r$-node Gaussian quadrature. Its off-diagonals are strictly positive. Its eigenvalues $\lambda_j(h)$ are simple and lie inside $[\alpha,B]$, and its root spectral weights $w_j(h)$ are positive and sum to one.

The ordered nodes and their spectral projections are analytic because the Jacobi eigenvalues are simple. Alternatively, the later construction can use the analytic matrix moments $e_0^TJ_h^j e_0$ directly. There is no support-rank switch and no padding.

Let

$$
L_h^\xi(t)=\int e^{-\lambda t}\rho_h^\xi(d\lambda),
\qquad
\widetilde L_h(t)=\sum_{j=1}^r w_j(h)e^{-\lambda_j(h)t}.
$$

Both unregularized and reference Laplace transforms lie in $[0,1]$, so

$$
\sup_{h,t}|L_h(t)-L_h^\xi(t)|\le\xi.
$$

The [positive whole-interval quadrature bound](CONSTANT_STEP_COMPRESSION.md#3-positive-quadrature-controls-every-observation-time) gives

$$
\sup_{h,t}|L_h^\xi(t)-\widetilde L_h(t)|
\le2q^{2r}\le\delta/4.
\tag{9}
$$

That bound expands $e^{-\lambda t}$ around $B$ and uses polynomial exactness through degree $2r-1$; each positive tail is at most $q^{2r}$ uniformly in time.

## 3. Two analytic Jacobi cores on fixed state labels

Use two blocks of $r+1$ states. In the minus block, the root has readout $-1$ and all nonroot states have readout $+1$. In the plus block, the root has readout $+1$ and all nonroot states have readout $-1$. Let $\rho$ put mass $1/2$ at each root.

Define

$$
d(h)=\sqrt{m(h)^2+\tau^2},\qquad
u_-(h)=\frac{d(h)+m(h)}2,\qquad
u_+(h)=\frac{d(h)-m(h)}2,
$$

$$
p_-(h)=1-u_-(h),\qquad p_+(h)=1-u_+(h).
\tag{10}
$$

These functions are real analytic and strictly between zero and one. Indeed $u_\pm>0$, and

$$
u_\pm(h)\le |m(h)|+\tau/2
\le\tanh H+\frac{1-\tanh H}{8}<1.
$$

They obey

$$
u_-(h)-u_+(h)=m(h),\qquad
p_+(h)-p_-(h)=m(h).
\tag{11}
$$

Put $\nu_j(h)=\lambda_j(h)-\varepsilon>0$. In each block take the positive Jacobi realization of the root spectral measure

$$
\omega_{\pm,h}
=p_\pm(h)\delta_0
+u_\pm(h)\sum_{j=1}^r w_j(h)\delta_{-\nu_j(h)}.
\tag{12}
$$

Each measure has exactly $r+1$ distinct support points and positive weights. Its finite moment matrices are strictly positive definite up to the required degree. Its moments can be written without selecting quadrature eigenvectors:

$$
\int x^j\omega_{\pm,h}(dx)
=p_\pm(h)\mathbf1_{\{j=0\}}
+u_\pm(h)e_0^T(\varepsilon I-J_h)^j e_0.
$$

They are analytic. The second finite Jacobi construction therefore gives analytic symmetric tridiagonal matrices, with positive off-diagonals and largest eigenvalue zero. Their normalized zero eigenvectors can be chosen strictly positive and analytic. Diagonal similarity by these eigenvectors gives analytic irreducible reversible block generators $A_h^-,A_h^+$ and analytic stationary laws $\pi_h^-,\pi_h^+$. Their stationary root masses are $p_-(h),p_+(h)$.

This is the [positive Jacobi realization](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel). Analyticity of its Markov similarity follows also by taking the analytic spectral projection at the isolated zero eigenvalue and fixing its positive root coordinate to $\sqrt{p_\pm(h)}$. All strict inequalities hold on the compact field interval, so the construction is analytic on an open neighborhood of it.

Let

$$
A_h=A_h^-\oplus A_h^+,\qquad
\pi_h=\tfrac12\pi_h^-\oplus\tfrac12\pi_h^+,
\qquad \Pi_h=\mathbf1\pi_h.
\tag{13}
$$

Here $\pi_h$ denotes the predictor's stationary law; from this point it is distinct from the target equilibrium used in (7). The block stationary readout means are $2u_--1$ and $1-2u_+$, so

$$
\pi_hS=u_-(h)-u_+(h)=\tanh h.
\tag{14}
$$

The two root return functions are

$$
P_{\pm,00}(t)
=p_\pm(h)+u_\pm(h)\sum_jw_j(h)e^{-\nu_j(h)t}.
$$

Their difference gives the exact mean from the fixed half-root law:

$$
\rho e^{tA_h}S
=P_{+,00}(t)-P_{-,00}(t)
=m(h)\left[1-\sum_jw_j(h)e^{-\nu_j(h)t}\right].
\tag{15}
$$

## 4. Analytic reset and exact passive calibration

First add the stationary reset

$$
Q_h^{\rm raw}=A_h+\varepsilon(\Pi_h-I).
\tag{16}
$$

It is analytic, irreducible and reversible under $\pi_h$. Every off-diagonal rate is positive. The nonzero spectrum of $-Q_h^{\rm raw}$ consists of the quadrature rates $\lambda_j(h)$, each twice, and one rate $\varepsilon$. The stationary-reset semigroup identity and (15) give

$$
\rho e^{tQ_h^{\rm raw}}S
=m(h)[1-\widetilde L_h(t)].
\tag{17}
$$

To calibrate the passive law without a separate field definition, set

$$
\boxed{
\widehat Q_h
=\chi(h)Q_h^{\rm raw}
+2k[1-\chi(h)](\Pi_h-I).
}
\tag{18}
$$

Both summands share the analytic stationary law $\pi_h$. Thus (18) is analytic and reversible. Its reset contribution has rate $\chi(h)\varepsilon+[1-\chi(h)]2k\ge\varepsilon$, so every physical off-diagonal entry is positive. Since the stationary projection commutes with the raw generator, each nonzero raw relaxation rate $\lambda$ is replaced by

$$
\lambda^\chi=\chi(h)\lambda+[1-\chi(h)]2k.
\tag{19}
$$

This preserves the full interval $[\alpha/2,B]$, because $2k$ lies in that interval. The half-root mean becomes exactly

$$
\rho e^{t\widehat Q_h}S
=m(h)\left[1-
\sum_{j=1}^r w_j(h)e^{-\lambda_j^\chi(h)t}\right].
\tag{20}
$$

At $h=0$, both cores are identical up to readout reversal and their root mass is $1-\tau/2$. Define the actual preparation by

$$
\boxed{\sigma=\pi_0.}
\tag{21}
$$

It is fixed independently of the applied field and has full support. Its total nonroot mass is $\tau/2$, and

$$
\|\sigma-\rho\|_1=\tau.
\tag{22}
$$

Since $\chi(0)=0$, the zero-field generator is exactly

$$
\widehat Q_0=2k(\mathbf1\sigma-I).
\tag{23}
$$

Thus $\sigma$ is its stationary law. Equation (14) makes it sign balanced. From every microscopic state, the total rate to the opposite readout sign is $k$, so strong lumpability gives the exact stationary rate-$k$ visible telegraph path law. For every field, the unique stationary mean remains $\pi_hS=\tanh h$.

## 5. Uniform constant-step error

The preparation change costs at most $\tau$ in every mean, uniformly in field and time, by Markov contraction and (22).

It remains to bound the spectral interpolation in (19). For a quadrature rate $\lambda_j\in[\alpha,B]$, both $\lambda_j$ and $\lambda_j^\chi$ are at least $\alpha$. Therefore

$$
\begin{aligned}
|e^{-\lambda_jt}-e^{-\lambda_j^\chi t}|
&\le t|\lambda_j-\lambda_j^\chi|e^{-\alpha t}\\
&\le\frac B\alpha[1-\chi(h)].
\end{aligned}
$$

Here $|\lambda_j-2k|\le B$ and $t e^{-\alpha t}\le1/\alpha$. Multiplying by $|m(h)|\le|h|$ and summing the probability weights gives

$$
\sup_t\left|
m(h)\sum_jw_j(h)
[e^{-\lambda_jt}-e^{-\lambda_j^\chi t}]
\right|
\le\frac B\alpha
\frac{|h|\eta^2}{h^2+\eta^2}
\le\frac{B\eta}{2\alpha}=\delta/4.
\tag{24}
$$

Combining regularization, Gaussian quadrature, the stationary preparation change, and (24),

$$
\boxed{
\mathcal D_H^{\rm step}(F,\widehat F)
\le \xi+2q^{2r}+\tau+\frac{B\eta}{2\alpha}
\le\delta.
}
\tag{25}
$$

No additional states were required for regularization, the analytic two-core construction, or the reset interpolation.

## 6. Exact linear response and zero quadratic response for weak protocols

The construction also matches the universal first two mean-response coefficients, although no general finite-amplitude switching approximation has been proved.

Write the predictor stationary law as

$$
\pi_h=\sigma+h\pi_1+h^2\pi_2+O(h^3),
$$

with Taylor coefficients divided by factorials. From (14),

$$
\pi_1S=1,\qquad \pi_2S=0.
$$

Set $D_h=Q_h^{\rm raw}-2k(\Pi_h-I)$. Then

$$
\widehat Q_h=2k(\Pi_h-I)+\chi(h)D_h,
\qquad \sigma D_0=0,
$$

because $\sigma=\pi_0$ is stationary for both terms in $D_0$. Also $\chi(0)=\chi'(0)=0$. For the generator Taylor coefficients this implies

$$
\widehat Q^{(0)}=2k(\mathbf1\sigma-I),\qquad
\widehat Q^{(1)}=2k\mathbf1\pi_1,
\qquad
\sigma\widehat Q^{(2)}=2k\pi_2.
\tag{26}
$$

For $h(t)=zu(t)$, let $p_1(t),p_2(t)$ be the first two probability-law coefficients from initial law $\sigma$. Both have total mass zero. The coefficient equations are

$$
\begin{aligned}
\dot p_1&=p_1\widehat Q^{(0)}
+u(t)\sigma\widehat Q^{(1)},\\
\dot p_2&=p_2\widehat Q^{(0)}
+u(t)p_1\widehat Q^{(1)}
+u(t)^2\sigma\widehat Q^{(2)}.
\end{aligned}
$$

For zero-mass rows, $p_j\widehat Q^{(0)}=-2kp_j$ and $p_1\widehat Q^{(1)}=0$. Multiplying by $S$ gives

$$
\dot m_1=-2km_1+2ku(t),\qquad
\dot m_2=-2km_2,
\qquad m_1(0)=m_2(0)=0.
$$

This proves (5) on every finite horizon for every bounded piecewise-continuous weak protocol. The generator is analytic for each fixed requested tolerance, so the coefficient equations are valid. No uniform bound on higher field derivatives as $\delta$ decreases is inferred.

## 7. Consequences and limits

The [constant-step lower bound](CONSTANT_STEP_COMPRESSION.md#7-a-matching-logarithmic-lower-bound-for-every-positive-internal-cap) permits arbitrary Markov competitors and proves $\Omega(\log(1/\delta))$ for every fixed positive internal cap and positive actuator variance. The upper theorem here therefore gives matching logarithmic state order even when competitors must have analytic field dependence, reversibility, strict physical positivity, stationary zero-field preparation, exact passive visible paths, exact static mean, and the mean calibrations (5).

For the binary shift-register targets with internal cap $5k/2$, adding switching experiments still forces a positive power of $1/\delta$, by the [polynomial controlled lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md). That lower allows a broader competitor class, so the analytic and calibrated structure of the present constant-step predictor does not weaken the comparison. Both tasks use one common model for all amplitudes, with fixed preparation and readout.

The rate functions produced here are real analytic, but their derivatives can grow with the requested accuracy. The smoothing widths, small reference mass and polynomial moment conditioning depend on $\delta$. This result does not impose the original exponential actuator rate rule, a fixed bound on its field derivatives, or an exponential-tilt relation between $\sigma$ and $\pi_h$. It does not establish a sharp constant-step upper bound under those additional requirements or a polynomial reversible upper for general switching in the original family.

The theorem concerns physical-state count. No statistical sample bound, numerical-conditioning guarantee or bound on the description length of the field-dependent rates is proved here.
