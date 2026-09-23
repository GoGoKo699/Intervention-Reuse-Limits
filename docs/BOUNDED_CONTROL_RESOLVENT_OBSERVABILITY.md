# Resolvent-word observability without a hidden rate cap

[Original model](THEORY.md) · [Nineteen-level construction](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Algebraic entropy interface](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) · [Bounded-word source audit](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) · [Earlier source audit](PRIOR_ART.md)

**Research derivation, 23 September 2026.** Uniform accuracy of actual controlled means implies quantitative accuracy of bounded hidden resolvent words, without an upper bound on the reversible hidden rates. The proof convexifies a fixed physical field menu, continues one scalar parameter for the entire protocol, integrates over dwell times, and extracts a coefficient by finite Chebyshev interpolation. All constants below are independent of hidden dimension, stationary masses and hidden rates.

This lemma uses the full arbitrary-switching experiment class. The convexification step does not supply a fixed positive minimum dwell time or a rate-independent bound on the number of switches. It does not recover unbounded generator-word derivatives directly. The final implication concerns the explicitly bounded resolvent words specified below.

## 1. Models and explicit constants

Rescale time so that $k=1$. Fix $H>0$ and a finite alphabet $\Gamma\subset(-1,1)$ of size $q\ge1$, and put $G=\max_{\gamma\in\Gamma}|\gamma|$. Both models have the original field rule and same stationary actuator histogram, a positive hidden stationary law $\mu$, reversible hidden generator $K$, preparation $\pi_0=(1/2,\mu/2)$, and readout $S=(-1,1_{\rm hid})$. Their hidden spaces and stationary laws may differ. No lower gap or upper rate bound is assumed.

For each model write $K_b$ for the hidden-only generator extended by zero on $A$, and let $D_\gamma$ be the hidden color projector. For a coefficient vector $c=(a_\gamma,b_\gamma)_{\gamma\in\Gamma}$, define an external operator $V(c)$ by

$$
V(c)_{Ai}=\mu_i a_{g_i},\qquad
V(c)_{iA}=b_{g_i},
$$

with the corresponding negative row sums on the diagonal and all other entries zero. Complex or negative coefficients define an algebraic operator, not necessarily a Markov generator. The physical generators are

$$
Q(h)=K_b+V(c(h)),\qquad
c(h)=\bigl(e^{(1+\gamma)h},e^{(\gamma-1)h}\bigr)_{\gamma\in\Gamma}.
\tag{1}
$$

Set $J=2q+1$ and choose $h_i=iH/(2q)$, $0\le i\le2q$. Let $\mathsf A$ have columns $(1,c(h_i))$. The frequencies $0,1+\gamma,\gamma-1$ are distinct. Thus $\mathsf A$ is an exponential Vandermonde matrix and is invertible. Define

$$
\begin{gathered}
R=e^{(1+G)H},\qquad
L=1+\|\mathsf A^{-1}\|_{\infty\to\infty},\qquad
\eta=\frac1{2JL},\qquad
\chi=\eta^{-1}+\sqrt{\eta^{-2}-1},\qquad \rho=\chi^2,\\
B=2\left[R+\frac{\eta}{2}(\rho+\rho^{-1})(R+1)\right],\qquad
C=\frac{4\sqrt2\chi}{\chi-1},\qquad s_0=\max\{4,B\}.
\end{gathered}
\tag{2}
$$

The matrix norm is the maximum absolute row sum. These are finite explicit constants determined by the fixed alphabet and field menu. In particular, they do not depend on $K$ or the requested word length. Their numerical values need not be small.

Assume the two models' actual means differ by at most $0<\delta<1$ for every bounded deterministic piecewise-continuous physical protocol and every observation time. It suffices to assume this on all switching protocols using the $J$ chosen fields, with arbitrary positive dwell times and arbitrarily many segments.

If the application uses a smaller positive field bound $h_0\le H$, substitute $h_0$ for $H$ throughout the constants and field menu. In particular, the nineteen-level application uses its existing thirty-nine-field menu with that substitution.

## 2. Convexification and a rate-independent holomorphic bound

Work in each model's own $L^2(\pi_0)$ space. In normalized coordinates the external operator has blocks

$$
\begin{pmatrix}
-\sum_i\mu_i a_{g_i} & (\sqrt{\mu_i}a_{g_i})_i^T\\
(\sqrt{\mu_i}b_{g_i})_i & -\operatorname{diag}(b_{g_i})
\end{pmatrix}.
$$

Each block norm is at most $\|c\|_\infty$, hence

$$
\|V(c)\|_{2\to2}\le2\|c\|_\infty.
\tag{3}
$$

The operator $K_b$ is selfadjoint and nonpositive. Bounded-perturbation variation of constants therefore gives

$$
\|e^{t(K_b+V(c))}\|_{2\to2}\le e^{2\|c\|_\infty t},\qquad t\ge0.
\tag{4}
$$

This does not use a bound on $\|K_b\|$. The preparation functional and readout both have norm one.

Let $c_*=J^{-1}\sum_i c(h_i)$. We will use artificial coefficient vectors from

$$
\mathcal V=\{(a,b):a_\gamma=0,\ |b_\gamma|\le1\text{ for all }\gamma\}.
$$

For $v\in\mathcal V$, its affine coordinates $\beta(v)=\mathsf A^{-1}(1,v)$ satisfy $\sum_i\beta_i(v)=1$ and
$|\beta_i(v)-1/J|\le L$. Consequently

$$
c_*+z(v-c_*)\in\operatorname{conv}\{c(h_i):0\le i<J\}
\quad\text{for every real }|z|\le\eta:
$$

its barycentric weights are $1/J+z(\beta_i(v)-1/J)\ge1/(2J)$.

For a convex combination $Q_c=\sum_i w_iQ(h_i)$, the finite-dimensional product formula gives

$$
e^{tQ_c}=\lim_{N\to\infty}
\left(\prod_i e^{(tw_i/N)Q(h_i)}\right)^N.
\tag{5}
$$

Apply this separately in both finite models and in every segment. Every approximating product is an allowed physical switching protocol. Uniform mean error $\delta$ therefore passes to the convexified protocol. No uniform convergence speed in (5) is needed; in particular, no rate cap is inferred from it.

Fix any finite artificial schedule $v_1,\ldots,v_m\in\mathcal V$ with durations $t_1,\ldots,t_m\ge0$, and put $T=\sum_i t_i$. Deform the entire schedule using the same scalar $z$:

$$
c_j(z)=c_*+z(v_j-c_*).
$$

Let $f(z)$ be the difference of the two scalar mean expressions for this schedule. It is entire in $z$, and $|f(z)|\le\delta$ on the real interval $[-\eta,\eta]$. Let $E_\rho$ be the filled Bernstein ellipse with boundary $x=(w+w^{-1})/2$, $|w|=\rho$. On $z\in\eta E_\rho$,

$$
\|c_j(z)\|_\infty\le
R+\frac\eta2(\rho+\rho^{-1})(R+1),
\qquad |f(z)|\le M_T:=2e^{BT}.
\tag{6}
$$

The bound is independent of the number of segments except through total duration. Continuing each segment separately would lose this property.

## 3. Explicit continuation from a real interval

Expand $f(\eta x)=\sum_{\ell\ge0}a_\ell T_\ell(x)$ in Chebyshev polynomials. The real integral formula gives $|a_\ell|\le2\delta$. Independently, the contour formula on the ellipse gives $|a_\ell|\le2M_T\rho^{-\ell}$. For clarity, the latter follows by applying the Laurent coefficient formula to $f(\eta(w+w^{-1})/2)$ on $|w|=\rho$; it uses the a priori complex bound (6), not an inference that small real error is automatically small in the complex plane.

At $x=1/\eta$, $|T_\ell(x)|\le\chi^\ell$. With

$$
N=\left\lfloor\frac{\log(M_T/\delta)}{\log\rho}\right\rfloor\ge0,
$$

split the series at $N$. Since $\rho=\chi^2$,

$$
\begin{aligned}
|f(1)|
&\le \frac{2\delta\chi^{N+1}}{\chi-1}
 +\frac{2M_T\chi^{-N}}{\chi-1}\\
&\le\frac{4\chi}{\chi-1}\sqrt{M_T\delta}
= C e^{BT/2}\sqrt\delta.
\end{aligned}
\tag{7}
$$

The exponent $1/2$ is fixed independently of hidden rates, dimension, segment count and word length. The finite constants can be large because the physical coefficient simplex can be narrow.

## 4. Exponentially distributed dwell times expose resolvents

Choose real label functions $d_j:\Gamma\to[-1,1]$ and let $D_j=\operatorname{diag}(d_j(g))$ on each model's hidden space, for $1\le j\le m$. A color projector is the special case $d_j(\gamma)=\mathbf1_{\gamma=c_j}$; port indicators and signed actuator endpoints are also permitted. For real $u_j\in[-1,1]$, the artificial schedule has $a=0$ and $b_\gamma=u_jd_j(\gamma)$ in segment $j$. State $A$ is absorbing in this algebraic schedule, and the hidden generator is $K-u_jD_j$. Its mean equals

$$
\mu\prod_{j=1}^m e^{t_j(K-u_jD_j)}1-1.
\tag{8}
$$

Negative $u_j$ are used only in analytic continuation, not as physical transition rates. Because their magnitude is at most one, the artificial coefficient set and all constants (2) remain independent of the Laplace parameter $s$ below.

Integrating over independent exponential dwell times of rate $s>B/2$ gives

$$
F_s(u_1,\ldots,u_m)
=\mu\prod_{j=1}^m\left[s(sI-K+u_jD_j)^{-1}\right]1.
\tag{9}
$$

The integrals converge for $s>1$, which is automatic when $s\ge s_0$. Integrating (7) and canceling the constant in (8) yields

$$
|F_s-\widehat F_s|
\le C\left(\frac{s}{s-B/2}\right)^m\sqrt\delta
\le C2^m\sqrt\delta,\qquad s\ge s_0.
\tag{10}
$$

The last inequality is uniform on the real cube $[-1,1]^m$. This is a Laplace integral of scalar mean differences, not a claim that the two hidden operators act on the same space.

## 5. Polarization and a finite coefficient functional

Let $P=s(sI-K)^{-1}$ and define

$$
G_s(z)=2^{-m}\sum_{\epsilon\in\{-1,1\}^m}
\left(\prod_j\epsilon_j\right)F_s(z\epsilon_1,\ldots,z\epsilon_m).
\tag{11}
$$

Since $K$ is selfadjoint nonpositive, $\|P\|\le1$. Neumann expansion gives, for $|z|<s$,

$$
s(sI-K+z\epsilon_jD_j)^{-1}
=\sum_{r\ge0}(-z\epsilon_j/s)^r(PD_j)^rP.
$$

Polarization retains terms with an odd positive power from every segment. Hence its coefficient of degree $m$ is exactly

$$
[z^m]G_s(z)=(-1/s)^m W_s,
\qquad
W_s=\mu\prod_{j=1}^m(PD_jP)1.
\tag{12}
$$

Furthermore,

$$
|G_s(z)|\le(1-|z|/s)^{-m}\le2^m
\quad(|z|\le s/2),
\tag{13}
$$

and (10) implies $|G_s-\widehat G_s|\le C2^m\sqrt\delta$ on $[-1,1]$. The normalized polarization has total absolute coefficient mass one, so its $2^m$ summands cause no additional error multiplier at this step.

Fix an integer $M\ge m$ and put $N=M+1$. Interpolate a scalar function at the Chebyshev roots

$$
x_j=\cos\theta_j,\qquad \theta_j=\frac{(2j+1)\pi}{2N},\quad 0\le j<N.
$$

For its degree-$M$ interpolant $I_M f$, define $\mathcal L_{M,m}(f)=[z^m]I_Mf$. The exact discrete cosine formulas give

$$
I_Mf=\sum_{\ell=0}^M a_\ell T_\ell,
\quad a_0=N^{-1}\sum_jf(x_j),\quad
a_\ell=2N^{-1}\sum_jf(x_j)\cos(\ell\theta_j)\ (\ell\ge1).
$$

The sum of absolute monomial coefficients of $T_\ell$ is at most $3^\ell$: use $T_{\ell+1}=2zT_\ell-T_{\ell-1}$ and induction from $T_0=1,T_1=z$. Therefore the node-weight sum of $\mathcal L_{M,m}$ obeys

$$
\|\mathcal L_{M,m}\|_{\text{node }\ell^\infty\to\mathbb C}
\le1+2\sum_{\ell=1}^M3^\ell
\le3^{M+1}.
\tag{14}
$$

This is an explicit finite coefficient extraction rule. No derivatives are estimated by assuming that bounded real error controls derivatives.

By (13), the Taylor coefficients of either $G_s$ have modulus at most $2^m(2/s)^j$. For $s\ge4$, its Taylor remainder after degree $M$, evaluated at the real interpolation nodes, is at most

$$
2^{m+1}(2/s)^{M+1}.
$$

Interpolation is exact on the retained Taylor polynomial. Apply (14) to the remainder for each of the two models and to their observed node discrepancy. Equations (10)–(14) give the uniform bound

$$
\boxed{
|W_s-\widehat W_s|
\le C2^m3^{M+1}s^m\sqrt\delta
 +2^{m+2}6^{M+1}s^{m-M-1},
\qquad s\ge s_0,\quad M\ge m.
}
\tag{15}
$$

## 6. Color words, gate normalization and the quadratic logarithmic scale

Because $\mu P=\mu$ and $P1=1$, with $S_s=P^2$ the scalar in (12) is the stationary color-word scalar

$$
W_s=\mu D_1S_sD_2\cdots S_sD_m1.
\tag{16}
$$

For color indicators this is a stationary color-word probability of a reversible stochastic matrix. General $d_j$ give its bounded label-word expectation; every preceding estimate used only $\|D_j\|\le1$. For a fixed normalization constant $a>0$ and an integer $L\ge0$, multiplying such a scalar by $(s/a)^L$ changes (15) to

$$
\boxed{
\left|(s/a)^L(W_s-\widehat W_s)\right|
\le a^{-L}\left[
C2^m3^{M+1}s^{m+L}\sqrt\delta
 +2^{m+2}6^{M+1}s^{m+L-M-1}\right].
}
\tag{17}
$$

The cross-port application uses $a=2\lambda$, where $\lambda$ is the fixed target gate-edge rate in units of $k$. Linear combinations of words multiply the right side by their absolute coefficient mass. This includes signed endpoints; a separate algebraic argument must specify their coefficients and prove the required target gate identities or approximation errors.

For word families with $m+L=O(n)$, choose $M=O(n)$ larger than $m+L$ by a positive multiple of $n$, and $s=e^{b(n+1)}$ with fixed $b$ large enough that $s\ge s_0$. Then the first term of (17) is $e^{O(n^2)}\sqrt\delta$, and the second is $e^{-\Omega(n^2)}$ after enlarging $b$ if necessary. Additional word coefficients of mass $e^{O(n)}$ preserve these orders. Thus accuracies $\delta_n=e^{-C_1(n+1)^2}$ can make the scalar discrepancy exponentially small in $n$, with $C_1$ chosen from the displayed constants and the word budget. Any target approximation error must still be added separately; (17) alone is not an entropy or state-count lower bound.

Restoring units replaces $P$ by $sk(skI-K)^{-1}$, artificial killing by $ku_jD_{c_j}$ and exponential dwell rate by $sk$. The dimensionless constants and error estimates are unchanged. The parameter $s$ is a probe's Laplace frequency, not a bound imposed on the rival's internal rate.

## 7. Scope of the transfer

The rate-independent conclusion comes from bounded external perturbations of a reversible contraction generator, with one common continuation parameter for the full protocol. The finite-field affine span, zero-field equilibrium preparation and fixed binary readout are used explicitly. No minimum stationary mass, hidden dimension bound, rival rate bound or common hidden state space is used.

The argument is compatible with arbitrary fast physical switching because the data norm already includes that class. It supplies neither the previous fixed-clock conclusion nor a rate-independent finite Trotter schedule. Laplace integration also uses the all-horizon error hypothesis. A finite-horizon or limited-switching version would require separate estimates. The proof controls bounded resolvent color words and must not be cited as uniform recovery of the unbounded raw generator moments.
