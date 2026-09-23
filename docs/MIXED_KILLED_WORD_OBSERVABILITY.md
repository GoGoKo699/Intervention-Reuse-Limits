# Mixed resolvent and killed-semigroup observability

[Original model](THEORY.md) · [Resolvent-word transfer](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) · [Binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Earlier binary construction](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Bounded-word source comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) · [Binary-observation source comparison](BINARY_OBSERVATION_PRIOR_ART.md)

**Research lemma, 23 September 2026.** Actual controlled-mean accuracy implies quantitative accuracy of mixed words containing smoothed actuator projectors and fixed nonnegative label-killing semigroups. The estimate is independent of reversible hidden rates, hidden dimension and minimum stationary mass. It extends the existing resolvent-word lemma by retaining prescribed killed evolution between the extracted factors.

The result supplies the observation interface used by the [tagged binary theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md). The lemma alone does not establish a state lower bound: the target construction and entropy argument are separate steps. It neither identifies exact color-jump events nor assumes that a bounded error in real observations controls derivatives without a separate estimate.

## 1. Models, words and explicit constants

Use dimensionless time, so $k=1$. Fix $H>0$ and a finite alphabet $\Gamma\subset(-1,1)$ of size $q\ge1$. Both finite models have the original field rule, the same stationary actuator histogram, reversible hidden generators, positive hidden stationary laws, preparation $\pi_0=(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. Their hidden spaces and laws may differ. There is no rival rate cap or lower-gap assumption.

Assume their actual means differ by at most $0<\delta<1$ on every switching protocol using the fixed field menu

$$
h_i=iH/(2q),\qquad 0\le i\le2q,
\tag{1}
$$

with arbitrary positive dwell times, arbitrary finite segment counts and all observation times. The full bounded-protocol error hypothesis is sufficient.

Write $G=\max_{\gamma\in\Gamma}|\gamma|$, $J=2q+1$ and $R=e^{(1+G)H}$. As in the [resolvent note](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md), let $\mathsf A$ have columns $(1,c(h_i))$, where

$$
c(h)=\bigl(e^{(1+\gamma)h},e^{(\gamma-1)h}\bigr)_{\gamma\in\Gamma}.
$$

The distinct frequencies $0,1+\gamma,\gamma-1$ make this square exponential Vandermonde matrix invertible. Fix a finite constant $U\ge1$ and set

$$
\begin{gathered}
L_U=1+U\|\mathsf A^{-1}\|_{\infty\to\infty},\qquad
\eta_U=\frac1{2JL_U},\qquad
\chi_U=\eta_U^{-1}+\sqrt{\eta_U^{-2}-1},\qquad
\rho_U=\chi_U^2,\\
B_U=2\left[R+\frac{\eta_U}{2}(\rho_U+\rho_U^{-1})(R+U)\right],\qquad
C_U=\frac{4\sqrt2\chi_U}{\chi_U-1},\qquad
s_U=\max\{4,B_U\}.
\end{gathered}
\tag{2}
$$

All constants in (2) depend only on the fixed alphabet, field menu and $U$.

Choose $m\ge1$ real label functions $d_j:\Gamma\to[-1,1]$ and write $D_j=\operatorname{diag}(d_j(g))$. In each model let

$$
P_s=s(sI-K)^{-1},\qquad A_j=P_sD_jP_s.
\tag{3}
$$

For each $0\le j\le m$, prescribe a finite ordered product

$$
E_j=\prod_{\ell=1}^{a_j}e^{t_{j\ell}(K-V_{j\ell})},\qquad
V_{j\ell}=\operatorname{diag}(v_{j\ell}(g)),\qquad
0\le v_{j\ell}(\gamma)\le U,
\tag{4}
$$

where $t_{j\ell}\ge0$. The same label functions, durations and order are used in both models. The empty product $a_j=0$ is allowed and gives $E_j=I$. Put

$$
T=\sum_{j=0}^m\sum_\ell t_{j\ell},\qquad
W_s=\mu E_0A_1E_1A_2E_2\cdots A_mE_m1.
\tag{5}
$$

**Mixed-word estimate.** For every integer $M\ge m$ and every $s\ge s_U$,

$$
\boxed{
\begin{aligned}
|W_s-\widehat W_s|
&\le C_U e^{B_UT/2}
\left(\frac{s}{s-B_U/2}\right)^m
3^{M+1}s^m\sqrt\delta\\
&\quad+2^{m+2}6^{M+1}s^{m-M-1}.
\end{aligned}}
\tag{6}
$$

Hats denote the second model's scalar expressions, not operators on a common hidden space. Signed $d_j$ are allowed in this scalar assertion; entrywise positivity below uses nonnegative $d_j$.

## 2. One continuation parameter for the entire schedule

Let $K_b$ be $K$ extended by zero on $A$. For an external coefficient vector $c=(a,b)$, let $V(c)$ contain the entries $\mu_i a_{g_i}$ from $A$ to $i$, the entries $b_{g_i}$ from $i$ to $A$, and the negative row sums on the diagonal. In normalized $L^2(\pi_0)$ coordinates its four blocks each have norm at most $\|c\|_\infty$, so

$$
\|V(c)\|\le2\|c\|_\infty,\qquad
\|e^{t(K_b+V(c))}\|\le e^{2\|c\|_\infty t}.
\tag{7}
$$

The second inequality follows from bounded perturbation of the selfadjoint nonpositive $K_b$ and does not use $\|K_b\|$.

Allow artificial coefficient vectors $a=0$, $|b_\gamma|\le U$. Their affine coordinates $\beta(v)=\mathsf A^{-1}(1,v)$ satisfy $\sum_i\beta_i(v)=1$ and

$$
|\beta_i(v)-1/J|\le L_U.
$$

With $c_*=J^{-1}\sum_i c(h_i)$, every $c_*+z(v-c_*)$ lies in the physical coefficient simplex for real $|z|\le\eta_U$. Finite-dimensional product formulas approximate each such convexified segment by the physical menu (1). For each pair of finite models the products converge; uniform mean error therefore passes to these segments. No rate-independent convergence speed or finite switching budget is asserted.

For any finite artificial schedule of total duration $T_{\rm tot}$, deform all its coefficients by this same $z$. The difference $f(z)$ of the two mean expressions is entire. It satisfies $|f(z)|\le\delta$ on $[-\eta_U,\eta_U]$. On the scaled Bernstein ellipse $\eta_UE_{\rho_U}$, (7) and (2) give

$$
|f(z)|\le2e^{B_UT_{\rm tot}}.
$$

Expand $f(\eta_U x)$ in Chebyshev polynomials. The real coefficient integral gives $|a_j|\le2\delta$; the ellipse contour formula gives $|a_j|\le4e^{B_UT_{\rm tot}}\rho_U^{-j}$. Since $|T_j(1/\eta_U)|\le\chi_U^j$ and $\rho_U=\chi_U^2$, splitting the series at

$$
N=\left\lfloor\frac{\log(2e^{B_UT_{\rm tot}}/\delta)}{\log\rho_U}\right\rfloor
$$

gives

$$
|f(1)|\le C_U e^{B_UT_{\rm tot}/2}\sqrt\delta.
\tag{8}
$$

This is the same coefficient-splitting argument as in the preceding resolvent lemma, with the enlarged but fixed artificial bound $U$.

## 3. Random pulse durations and fixed killed evolution

For real parameters $u_j\in[-1,1]$, start with the prescribed fixed block $E_0$, then use an artificial pulse with hidden generator $K-u_jD_j$ before each fixed block $E_j$, $1\le j\le m$. State $A$ is absorbing in every segment of this artificial schedule. Starting from the original preparation, its mean is

$$
\mu E_0\prod_{j=1}^m\left[e^{\tau_j(K-u_jD_j)}E_j\right]1-1.
\tag{9}
$$

The formula also holds for negative pulse killing as an algebraic matrix identity. Negative killing is used only in the analytical argument.

Integrate (9) over independent exponential pulse durations $\tau_j$ with rate $s>B_U/2$. The fixed blocks contribute total duration $T$. The constant minus one cancels between the models, and (8) gives

$$
\begin{aligned}
F_s(u)&=\mu E_0\prod_{j=1}^m\left[s(sI-K+u_jD_j)^{-1}E_j\right]1,\\
|F_s(u)-\widehat F_s(u)|
&\le C_U e^{B_UT/2}
\left(\frac{s}{s-B_U/2}\right)^m\sqrt\delta
\quad(u\in[-1,1]^m).
\end{aligned}
\tag{10}
$$

The integrals converge because the pulse perturbations have norm at most one and $s\ge4$. Fixed killed factors are contractions: each $K-V_{j\ell}$ is selfadjoint nonpositive in its own model's $L^2(\mu)$.

## 4. Polarization and finite coefficient extraction

Define

$$
G_s(z)=2^{-m}\sum_{\epsilon\in\{-1,1\}^m}
\left(\prod_j\epsilon_j\right)F_s(z\epsilon_1,\ldots,z\epsilon_m).
\tag{11}
$$

For $|z|<s$, the pulse resolvent has the norm-convergent expansion

$$
s(sI-K+z\epsilon_jD_j)^{-1}
=\sum_{a\ge0}(-z\epsilon_j/s)^a(P_sD_j)^aP_s.
$$

Polarization retains odd positive $a$ at each pulse. Consequently

$$
[z^m]G_s(z)=(-1/s)^mW_s.
\tag{12}
$$

Because $\|P_s\|\le1$ and every fixed block is a contraction,

$$
|G_s(z)|\le(1-|z|/s)^{-m}\le2^m
\qquad(|z|\le s/2).
\tag{13}
$$

The normalized polarization has total coefficient mass one, so the real node discrepancy of $G_s$ has the same bound as (10).

Interpolate at the $M+1$ roots of $T_{M+1}$ and extract the monomial coefficient of degree $m$ from the degree-$M$ interpolant. The discrete cosine representation of this functional has node-weight mass at most

$$
1+2\sum_{j=1}^M3^j\le3^{M+1}.
\tag{14}
$$

Here $3^j$ bounds the sum of absolute monomial coefficients of $T_j$, by its three-term recurrence. By (13), each Taylor coefficient of $G_s$ has modulus at most $2^m(2/s)^j$. Its Taylor remainder above degree $M$, evaluated at a real node, is at most $2^{m+1}(2/s)^{M+1}$ for $s\ge4$. The interpolation is exact on the retained Taylor polynomial. Apply (14) to the node discrepancy and the two Taylor remainders, then multiply by $s^m$ using (12). This proves (6).

In particular the proof extracts a coefficient using a finite linear functional with a stated error bound. It does not estimate derivatives directly from the observed real error.

## 5. Positive words, adjoints and target approximation

For nonnegative $d_j$, each $A_j=P_sD_jP_s$ is entrywise nonnegative and selfadjoint. Each fixed killed factor in (4) is entrywise nonnegative and selfadjoint, although a product $E_j$ need not be selfadjoint. Reversing all factors gives its stationary adjoint and another permitted mixed word. The leading block $E_0$ permits this closure even when the original final block $E_m$ is nontrivial. Products of these operators are therefore positive kernels on the rival's own states. They need not be stochastic or coordinate projectors.

For example, with binary color projectors $D_0,D_1$ and a fixed $0\le u\le U$, the operator

$$
A_0A_1e^{t(K-uD_0)}A_1A_0
\tag{15}
$$

is positive and selfadjoint in every model. Its scalar, products of such operators and their Gram expressions all have the form (5), by allowing identity fixed blocks. Equation (15) alone supplies no target port-selector identity or lamp-flip operation. In particular positivity and an observed scalar estimate do not replace a separate target construction and entropy argument.

Suppose only the target has $\|-K\|\le\Lambda$. Spectral calculus gives

$$
\|P_s-I\|\le\Lambda/s,\qquad
\|P_sD_jP_s-D_j\|\le2\Lambda/s.
\tag{16}
$$

All factors involved are contractions. Thus replacing the $m$ smoothed factors by their target label multipliers, while retaining the same $E_j$, changes the target operator product by at most $2m\Lambda/s$. Multiplication by any explicit scalar normalization multiplies this bound as well. No corresponding target approximation is presumed for an uncapped rival.

For normalized binary selectors the leading cross-color cancellation gives a sharper useful statement. Put $F_c=P_sD_cP_s$ for disjoint binary color projectors $D_0,D_1$, and let $E$ be any contraction. Then

$$
\begin{aligned}
\left\|F_0F_1-\frac2sD_0KD_1\right\|
&\le\frac{7\Lambda^2}{s^2},\\
\left\|\frac{s^2}{4\kappa}F_0F_1E F_1F_0
-\frac1\kappa D_0KD_1E D_1KD_0\right\|
&\le\frac{7\Lambda^3}{\kappa s}
\qquad(\kappa>0).
\end{aligned}
\tag{17}
$$

These are target-only estimates. To check them, spectral calculus gives
$\|P_s^2-I-2K/s\|\le3\Lambda^2/s^2$ and
$\|P_s^2-I\|\le2\Lambda/s$. Since $D_0D_1=0$,
$F_0F_1=P_s(D_0P_s^2D_1)P_s$. Expanding the two outer factors around the leading $2D_0KD_1/s$ adds at most $4\Lambda^2/s^2$, proving the first bound. Both $F_0F_1$ and $2D_0KD_1/s$ have norm at most $2\Lambda/s$. Telescoping their two-sided sandwich around $E$ gives $28\Lambda^3/s^3$ before multiplication by $s^2/(4\kappa)$, proving the second. Thus a small selector normalization $\kappa$ must be included when choosing $s$; the unnormalized estimate (16) alone does not establish a normalized selector limit.

## 6. Quantitative budgets and scope

For a linear combination of mixed scalars whose total absolute coefficient and normalization mass is $J_n$, multiply (6) by $J_n$. Use the largest pulse count $m_n$ and total fixed duration $T_n$ in that family, with $M$ at least the largest pulse count.

For an explicit conservative scaling, let $p(n)\ge n+1$ be a polynomial satisfying

$$
m_n\le p(n),\qquad T_n\le p(n),\qquad
\log J_n\le p(n).
$$

Choose a fixed $b$ large enough, $s=e^{bp(n)}$ and $M=3\lceil p(n)\rceil$. Then (6), after normalization, has the form

$$
e^{O(p(n)^2)}\sqrt\delta+e^{-\Omega(p(n)^2)}.
\tag{18}
$$

For example $s\ge B_U m_n$ ensures $(s/(s-B_U/2))^{m_n}\le e$. The constants in (18) depend on the fixed model data and $b$. If the target spectral cap $\Lambda$ is uniform in $n$, increase $b$ if needed so that normalized target replacement errors from (16) also decay at any specified exponential rate in $n$. The same conclusion holds for a varying target cap $\Lambda_n$ provided $\log(1+\Lambda_n)\le p(n)$ is included in the budget. Any target-specific approximation involving rare weights or new positive filters still needs its own quantitative proof.

The preceding coefficient budget assumes that $J_n$ is independent of the subsequently chosen $s$. Normalized cross-color words may instead have, for a fixed $a\ge0$,

$$
J_n(s)\le e^{p(n)}s^{a p(n)}.
\tag{19}
$$

With $m_n,T_n\le p(n)$, choose $s=e^{bp(n)}$ and $M=\lceil(a+3)p(n)\rceil$. The noise exponent in (6), including (19), is still $O(p(n)^2)$; the power of $s$ in the tail is at most $-2p(n)-1$. Thus (18) also holds for the **observability error** under this polynomial-in-$s$ normalization budget. This does not make the naive target replacement bound $2m\Lambda J_n(s)/s$ small. Target convergence of normalized kernels must first use their own cancellations, such as (17), and only then compose those normalized estimates.

A sharper separated budget is useful when the number of pulses is linear but their inserted durations sum to a quadratic function. Suppose fixed constants satisfy

$$
m_n\le a_0(n+1),\quad T_n\le a_1(n+1)^2,\quad
\log J_n(s)\le a_2(n+1)^2+a_3(n+1)\log s,
\quad \log s=b(n+1),\ b>0.
\tag{20}
$$

Choose $M=\lceil d(n+1)\rceil$, with $d>a_0+a_3+a_2/b$. The logarithm of the normalized noise coefficient in (6) is $O((n+1)^2)$. The logarithm of its normalized tail is at most

$$
\left[a_2-b(d-a_0-a_3)\right](n+1)^2+O(n+1).
$$

Increasing the fixed $d$ makes this quadratic coefficient as negative as needed. Hence under (20) the observable error has the sharper form
$e^{O((n+1)^2)}\sqrt\delta+e^{-\Omega((n+1)^2)}$.
This remains an observation estimate; the normalized target and entropy hypotheses are separate obligations.

The lemma uses arbitrarily fast physical switching to convexify the field menu and all horizons to integrate pulse durations. It gives no fixed positive control clock, no rate-independent finite switching schedule and no direct recovery of a continuously observed color-jump process. The prescribed nonnegative killing segments are analytical proof operators obtained by continuation; they are not extra physical controls. Their durations may vary with a target index, and their cost is explicitly the factor $e^{B_UT/2}$ in (6).

Restoring units replaces $K$ in dimensionless formulas by $K/k$, the pulse resolvent by $sk(skI-K)^{-1}$, and a dimensionless killed duration $t$ by the physical duration $t/k$ with killing rate $kv(g)$. The parameter $s$ is a probe Laplace frequency, not a restriction on a rival's hidden rate.
