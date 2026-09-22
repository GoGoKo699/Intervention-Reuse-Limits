# A fixed nonzero field already forces growing predictor size

[Finite-field theorem](FINITE_FIELD.md) · [Cubic lower-bound tools](UNRESTRICTED_RATE_LOWER_BOUND.md)

**Working theorem, 22 September 2026.** This strengthens the finite-field lower bound: one constant step amplitude, chosen independently of target size and requested tolerance, suffices. The proof uses the exact reversible step response, not a Taylor remainder or a derivative of the competing model.

## 1. Statement

Fix $k,W,H>0$, put $s=\sqrt W$, and choose once and for all

$$
h_* = \min\left\{H,\frac1{20(1+s)}\right\}>0,\qquad
\gamma=e^{-h_*}\sinh(s h_*)>0.
$$

For every integer $D\ge2$, set $r=D+3$. There is a target in $\mathcal J(k,W)$ with $r+2=D+5$ states such that every autonomous $D$-state Markov predictor obeys

$$
\boxed{
\sup_{t\ge0}|m_F[h_*](t)-m_{\widehat F}[h_*](t)|
\ge\frac{\tanh(h_*)\gamma^2}{640r^2}
\exp[-2\pi\sqrt{6(r-1)}].
}
$$

The field is switched from zero to the constant value $h_*$ at time zero. Targets start from zero-field equilibrium. Competitors may use any fixed initial probability law and real state readout; only a time-homogeneous Markov generator at this chosen field is needed. No agreement with passive data, analyticity in the field, or bound on rate derivatives is required.

Thus the squared-logarithmic state order in [the finite-field theorem](FINITE_FIELD.md) is already necessary for predicting this single step curve to uniform-in-time accuracy. The target may depend on $D$, but $h_*$ does not. The theorem does not assert the same bound at every arbitrarily large prescribed field, or for noisy finite-sample measurements.

## 2. Exact step response as a positive spectral sum

Use dimensionless time $\tau=kt$. The model's field equilibrium is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(B_i)=\frac{\mu_i e^h}{2\cosh h}.
$$

The density of the initial law $\pi_0$ relative to $\pi_h$ is

$$
\frac{\pi_0}{\pi_h}=\cosh h\,e^{-hS}
=\cosh^2h-\cosh h\sinh h\,S.
$$

Consequently

$$
m_h(t)-\tanh h
=-\cosh h\sinh h\,
\operatorname{Cov}_{\pi_h}(S(0),S(t)).
$$

Reversibility makes the symmetrized negative generator positive semidefinite. The centered readout, normalized to unit variance, is a unit vector $u$ orthogonal to its stationary vector. On that orthogonal complement let the dimensionless symmetrized negative generator be $L_h$. Since $\operatorname{Var}_{\pi_h}S=\operatorname{sech}^2h$,

$$
m_h(\tau/k)=\tanh h\,[1-\langle u,e^{-L_h\tau}u\rangle].
$$

We next identify $L_h$ explicitly for the rank-one sensitivity targets.

## 3. The field generator is a diagonal matrix plus a positive rank-one matrix

Take a kernel with distinct rates and weights

$$
C(t)=\sum_{j=1}^r c_j e^{-\lambda_jt},\qquad c_j>0,\qquad \sum_jc_j=W,
$$

and its $r+2$-state Jacobi realization. The internal symmetric generator has a stationary vector $v_\mu=(\sqrt{\mu_i})_i$. In its orthogonal complement, choose normalized eigenvectors whose overlaps with the centered normalized sensitivity

$$
w=\frac{\operatorname{diag}(\sqrt\mu)g}{s}
=\sqrt2 e_0-v_\mu
$$

are positive. These overlaps are $\sqrt{c_j/W}$.

Use $u$ as the first coordinate and those internal eigenvectors as the remaining coordinates. Direct symmetrization of the $A$--$B$ rates gives

$$
L_h=\operatorname{diag}(d_0,d_1,\ldots,d_r)+\gamma_h vv^T,
$$

where

$$
\kappa_h=e^{-(1+s)h},\qquad
\gamma_h=e^{-h}\sinh(sh),\qquad
 d_0=2e^{-sh}\cosh h,\qquad
 d_j=\frac{\lambda_j}{k}+\kappa_h,
$$

$$
v_0=\sqrt{1+e^{2h}},\qquad v_j=\sqrt{c_j/W}\quad(1\le j\le r).
$$

A check on the entries is useful: the visible diagonal is
$2\cosh(sh)\cosh h=d_0+\gamma_hv_0^2$; the hidden block is
$\operatorname{diag}(\lambda_j/k+\kappa_h)+\gamma_h(v_iv_j)_{i,j\ge1}$; and the visible-to-hidden entries are $\gamma_hv_0v_j$. The stationary eigenvalue has already been removed. The chosen visible coordinate is $u=e_0$ in this basis.

From now on take $h=h_*$. Then

$$
0<\gamma<\frac1{16},\qquad
2\le v_0^2<3,\qquad e^{-1/20}\le\kappa\le1,\qquad 0<d_0<2.01.
$$

## 4. Geometric hidden rates retain separated field eigenvalues

Put

$$
\eta=\pi\sqrt{\frac{2}{3(r-1)}},\qquad
a_j=4e^{(j-1)\eta},\qquad
\lambda_j=k(a_j-3/2),\qquad c_j=W/r.
$$

Thus $v_j^2=1/r$, $d_j=a_j-3/2+\kappa$, and $d_1-d_0>1$. Let $\ell_0,\ldots,\ell_r$ be the eigenvalues of $L_{h_*}$ in increasing order. The secular equation is

$$
f(\ell)=1+\gamma\sum_{i=0}^r\frac{v_i^2}{d_i-\ell}=0.
$$

All $v_i$ are nonzero, so the eigenvalues are simple and strictly interlace the $d_i$: $\ell_i\in(d_i,d_{i+1})$ for $i<r$, and $\ell_r>d_r$. This follows directly because $f$ is strictly increasing between its poles, running from negative to positive infinity on each such interval, and tending to one beyond its last pole.

For every hidden index $j\ge1$, we claim

$$
\ell_j=d_j+\delta_j,\qquad
\frac{\gamma}{2r}\le\delta_j\le\frac{2\gamma}{r}.
$$

To prove this, consider $0<\delta\le2\gamma/r$. Geometric spacing gives
$|d_i-d_j|=|a_i-a_j|\ge4\eta|i-j|$ for hidden indices. Also $\gamma/r<\eta$. Hence, for $i\ne j$,

$$
|d_i-d_j-\delta|\ge2\eta|i-j|.
$$

The two candidate endpoints lie below the next pole. Write

$$
f(d_j+\delta)=1-\frac{\gamma}{r\delta}+\gamma R_j(\delta),
\qquad
R_j(\delta)=\frac{v_0^2}{d_0-d_j-\delta}
+\frac1r\sum_{\substack{i=1\\i\ne j}}^r\frac1{d_i-d_j-\delta}.
$$

With $H_n=\sum_{i=1}^n1/i$ and $H_0=0$,

$$
|R_j(\delta)|
\le3+\frac{H_{j-1}+H_{r-j}}{2r\eta}
\le3+\frac{H_{r-1}}{r\eta}
\le3+\frac{\sqrt6}{\pi}<5.
$$

The last step uses $H_n\le2\sqrt n$. Therefore $|\gamma R_j|<5/16<1/2$. At $\delta=\gamma/(2r)$ the secular function is negative; at $\delta=2\gamma/r$ it is positive. Its monotonicity proves the claimed enclosure. The argument controls the individual shifts by $1/r$; it does not assume that a fixed operator-norm perturbation is smaller than every spectral gap.

## 5. The visible weights of all hidden modes stay positive and quantitative

A normalized eigenvector at $\ell_j$ has components proportional to $v_i/(\ell_j-d_i)$. Its visible squared overlap is therefore

$$
\omega_j=
\frac{v_0^2/(\ell_j-d_0)^2}
{\sum_{i=0}^r v_i^2/(\ell_j-d_i)^2}.
$$

For $j\ge1$, the denominator is at most

$$
\frac{4r}{\gamma^2}+3+
\frac1{4r\eta^2}\sum_{i\ne j}\frac1{(i-j)^2}
\le\frac{4r}{\gamma^2}+3+\frac14
\le\frac{5r}{\gamma^2}.
$$

Here $\sum_{m\ne0}m^{-2}=\pi^2/3$ and the chosen $\eta$ in fact give the stronger last hidden contribution at most $1/8$. Let $a_{\max}=a_r$. Because $0<\ell_j-d_0<\ell_j<a_{\max}$ and $v_0^2\ge2$,

$$
\boxed{\omega_j\ge\frac{2\gamma^2}{5r a_{\max}^2},\qquad j\ge1.}
$$

The exact mean thus has the form

$$
m_{h_*}(\tau/k)=B(\tau)-\tanh(h_*)\sum_{j=1}^r\omega_j e^{-\ell_j\tau},
$$

where

$$
B(\tau)=\tanh(h_*)[1-\omega_0e^{-\ell_0\tau}]
$$

has Hankel rank at most two.

## 6. A Cauchy lower bound in the actual step-curve norm

Use the probability measure $d\nu(\tau)=e^{-\tau}d\tau$. The Gram matrix of $e^{-\ell_j\tau}$, $j=1,\ldots,r$, is

$$
\mathsf C_{ij}=\frac1{b_i+b_j},\qquad b_j=\ell_j+\frac12=a_j-(1-\kappa)+\delta_j.
$$

These positive nodes satisfy

$$
\log b_{j+1}-\log b_j\ge\frac\eta2,\qquad
b_{\max}\le2a_{\max}.
$$

Indeed, write $t=1-\kappa\ge0$. The eigenvalue enclosure gives

$$
\begin{aligned}
b_{j+1}-e^{\eta/2}b_j
&\ge e^{\eta/2}\left[a_j(e^{\eta/2}-1)-\frac{2\gamma}{r}\right]
+t(e^{\eta/2}-1)\\
&\ge e^{\eta/2}\left[2\eta-\frac{2\gamma}{r}\right]>0.
\end{aligned}
$$

The Cauchy inverse identity and the same decreasing-integral estimate used in [the cubic lower-bound proof](UNRESTRICTED_RATE_LOWER_BOUND.md#4-the-cauchy-gram-matrix) now give

$$
(\mathsf C^{-1})_{ii}
=2b_i\prod_{j\ne i}\left(\frac{b_i+b_j}{b_i-b_j}\right)^2,
\qquad
\operatorname{tr}\mathsf C^{-1}
\le4r a_{\max}e^{2\pi^2/\eta}.
$$

For clarity, logarithmic node gaps of at least $\eta/2$ bound each ratio by
$\coth(|i-j|\eta/4)$. Summing its logarithm, with each positive index distance occurring at most twice, gives the exponent $\pi^2/(\eta/2)=2\pi^2/\eta$.

Let $\mathsf K$ be the positive Hankel operator of
$\tanh(h_*)\sum_{j=1}^r\omega_j e^{-\ell_j\tau}$. Combining the weight and Gram bounds yields

$$
\begin{aligned}
\lambda_{\min}^+(\mathsf K)
&\ge\frac{\tanh(h_*)\gamma^2}{10r^2a_{\max}^3}
 e^{-2\pi^2/\eta}\\
&=\frac{\tanh(h_*)\gamma^2}{640r^2}
 e^{-3(r-1)\eta-2\pi^2/\eta}\\
&=\frac{\tanh(h_*)\gamma^2}{640r^2}
 e^{-2\pi\sqrt{6(r-1)}}.
\end{aligned}
$$

A $D$-state constant-field Markov curve has Hankel rank at most $D$, by factoring its matrix exponential at $\tau+\sigma$. Subtracting it from $B$ gives rank at most $D+2=r-1$. Such an operator cannot approximate the positive rank-$r$ operator $\mathsf K$ to operator error smaller than its least positive eigenvalue. Finally, uniform curve error bounds Hankel operator error by the same number because $\nu$ has mass one. This proves the stated lower bound directly for the exact finite-field curve.

The all-protocol upper theorem gives a predictor of order $O(\log^2(1/\delta))$ for this step as a special case. The matching lower order therefore holds even when the prediction task is reduced to this one fixed-amplitude step, with arbitrary observation times.
