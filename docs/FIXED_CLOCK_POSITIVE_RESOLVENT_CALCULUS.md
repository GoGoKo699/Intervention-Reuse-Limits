# Positive hidden kernels from fixed-clock physical observations

[Fixed-clock Gram transfer](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Fixed-clock uncapped theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Tagged binary construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) · [Earlier mixed-word interface](MIXED_KILLED_WORD_OBSERVABILITY.md)

**Research calculus, 23 September 2026.** The operators used by the tagged binary lower bound can be reduced to finite scalar expressions in full physical resolvents and the visible-state projector. This avoids rapid-switching convexification. Exact proof kernels remain entrywise nonnegative on arbitrary reversible rivals. Signed polynomials are used only to recover their scalar values from observations.

The input from [fixed-clock Gram observability](FIXED_CLOCK_GRAM_OBSERVABILITY.md) is quantitative recovery of finite words in normalized full physical resolvents and the visible projector. The present note supplies the operator reduction, the uniform approximation to killed heat, and the target scaling needed for the final theorem.

## 1. Full and hidden resolvents

Work in units $k=1$. Let $J$ be the coordinate projector onto the visible state $A$, and let $H_0=I-J$ denote the hidden projector. This symbol is distinct from the physical field bound $H$. At a fixed field $h$, write

$$
Q_h=\begin{pmatrix}-a_h&\mu\alpha_h\\
\beta_h&K-B_h\end{pmatrix},\qquad
a_h=\mu\alpha_h,\quad
\alpha_h(g)=e^{(1+g)h},\quad
B_h=\operatorname{diag}(\beta_h(g)),\quad
\beta_h(g)=e^{(g-1)h}.
\tag{1}
$$

For $z>0$, let $R_h(z)=(zI-Q_h)^{-1}$ and $Z_h(z)=zR_h(z)$. The normalized physical resolvent is a Markov kernel. The hidden killed resolvent, extended by zero at $A$, is

$$
\begin{aligned}
G_h(z)&=(zI-K+B_h)^{-1},\\
\mathcal Z_h(z):=zG_h(z)
&=H_0 Z_h(z)H_0
-\frac{H_0Z_h(z)JZ_h(z)H_0}{d_h(z)},\qquad
d_h(z)=(Z_h(z))_{AA}.
\end{aligned}
\tag{2}
$$

The right side is a Schur-complement identity, not a positivity argument by subtraction. To verify it, block-invert $zI-Q_h$: the hidden block of its inverse is $G_h+G_h\beta_h(R_h)_{AA}\mu\alpha_hG_h$, while its two off-diagonal blocks are $G_h\beta_h(R_h)_{AA}$ and $(R_h)_{AA}\mu\alpha_hG_h$. The rank-one correction in (2) removes the second term exactly.

The operator $G_h$ is entrywise nonnegative, selfadjoint in $L^2(\mu)$, and has norm at most $1/z$. The scalar denominator obeys

$$
1\ge d_h(z)\ge\frac{z}{z+a_h}\ge\frac{z}{z+R},
\qquad R=e^{(1+\gamma)H}
\tag{3}
$$

for the balanced binary alphabet used below. The lower bound is the contribution of trajectories that stay at $A$ until the independent exponential observation time. Thus (2) is uniformly stable when $z\ge c/(n+1)$ for a fixed $c>0$, up to polynomial factors in $n$.

An insertion of $J$ factorizes a scalar word into visible-start and visible-end scalar expressions. Those expressions are recovered by the finite preparation recursion in the Gram note. There is no hidden preparation or continuous observation of jumps in (2).

For any hidden word $W$ extended by zero on the visible coordinate,
$\mu W1=2\pi_0WS$, where $S=(-1,1_{\rm hid})$. All entropy words below have hidden outer factors and therefore use this identity. Expanding their operators introduces only ordinary physical-word scalars and visible-projector insertions with the actual preparation and readout.

## 2. Binary label factors from two natural resolvents

Use only the two physical fields $0$ and $h_*=H>0$. Assign binary color $0$ to $g=+\gamma$ and color $1$ to $g=-\gamma$, and write

$$
B_{h_*}=b_0D_0+b_1D_1,\qquad
b_0=e^{(\gamma-1)h_*}>b_1=e^{(-\gamma-1)h_*},\qquad
\Delta_b=b_0-b_1>0.
\tag{4}
$$

Here $D_0,D_1$ are the rival's actual binary label projectors; their coordinate realizations need not agree with the target's. At zero field $B_0=I$. For a common parameter $s>0$, abbreviate $G_0=G_0(s)$ and $G_*=G_{h_*}(s)$. The resolvent identity gives

$$
G_0D_0G_*=
\frac{G_0-G_*-(b_1-1)G_0G_*}{\Delta_b},\qquad
G_0D_1G_*=G_0G_*-G_0D_0G_*.
\tag{5}
$$

Define the symmetrized factors

$$
F_c=\frac{s^2}{2}(G_0D_cG_*+G_*D_cG_0),\qquad c=0,1.
\tag{6}
$$

Each $F_c$ is entrywise nonnegative, selfadjoint and an $L^2(\mu)$ contraction in every reversible rival. Selfadjointness here is not a claim of positive semidefiniteness. In normalized natural resolvents, (5) becomes the finite observable formula

$$
\begin{aligned}
F_0&=\frac{s}{\Delta_b}(\mathcal Z_0-\mathcal Z_*)
-\frac{b_1-1}{2\Delta_b}
(\mathcal Z_0\mathcal Z_*+\mathcal Z_*\mathcal Z_0),\\
F_1&=\tfrac12(\mathcal Z_0\mathcal Z_*+\mathcal Z_*\mathcal Z_0)-F_0.
\end{aligned}
\tag{7}
$$

For a fixed bounded target generator, set $A_{\mathrm{av}}=K-(I+B_{h_*})/2$. Expansion of the two resolvents gives

$$
F_c=D_c+\frac{A_{\mathrm{av}}D_c+D_cA_{\mathrm{av}}}s+O(s^{-2}),
\qquad
F_0F_1=\frac2sD_0KD_1+O(s^{-2}).
\tag{8}
$$

The constants depend only on the fixed target cap and the chosen fields. The diagonal parts of $A_{\mathrm{av}}$ vanish between distinct colors. Consequently, for any contraction $E$ and any $\kappa>0$,

$$
\left\|\frac{s^2}{4\kappa}F_0F_1E F_1F_0
-\frac1\kappa D_0KD_1E D_1KD_0\right\|
\le\frac{C}{s\kappa}
\tag{9}
$$

on the target, for sufficiently large $s$. In a rival the exact left-hand sandwich remains entrywise nonnegative whenever $E$ is. If $E$ is selfadjoint, so is the sandwich. No target expansion such as (8) is assumed for a rival.

## 3. Natural killing implements the rare-tag filter

Let $K^{\rm old}_n$ be the unrescaled family in the [tagged construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md), including all its rare tags, color-zero chain and distant balancing state. Its filter uses killing $u_*=10^9$ on color zero. Keep the graph, weights and binary partition but assign its color-zero states to $+\gamma$, as in (4). Define the new target hidden generator

$$
\eta=\frac{\Delta_b}{u_*}>0,\qquad K_n=\eta K^{\rm old}_n.
\tag{10}
$$

This is a fixed scaling independent of $n$. If the old exits are at most $B=5\times10^8$ and its gap is at least $g_*>0$, the new exits are at most $\eta B$ and the new gap is at least $\eta g_*$. The exact balanced histogram is unchanged. An additional normalization of the hidden gap to one is not part of this construction: it would change the relationship between hidden dynamics and natural killing.

For each signed type $i$, retain the old $T_i$ and $\kappa_i$, and put

$$
t_i=T_i/\eta,\qquad
\widetilde\kappa_i=\eta^2e^{-b_1t_i}\kappa_i.
\tag{11}
$$

Then the exact identity

$$
e^{t_i(K_n-B_{h_*})}
=e^{-b_1t_i}e^{T_i(K^{\rm old}_n-u_*D_0)}
\tag{12}
$$

shows that the natural filter

$$
A_i=\frac{s^2}{4\widetilde\kappa_i}
F_0F_1e^{t_i(K-B_{h_*})}F_1F_0
\tag{13}
$$

has exactly the old ideal selector limit on the new target as $s\to\infty$. The two cross-color generator blocks supply the factor $\eta^2$ canceled in (11).

There is a fixed constant $K_\kappa$ with
$\widetilde\kappa_i^{-1}\le e^{K_\kappa(n+1)}$. For example one may use

$$
K_\kappa=14N+2Nb_1/\eta+2|\log\eta|+1,\qquad N=10^6.
$$

Choose a fixed $S_*>K_\kappa+6000$ and $s=e^{S_*(n+1)}$. Equations (9), (12) and the old construction's raw tag-selector estimate (its equation (17), with error $e^{-2400n}$) give

$$
\|A_i-D_i\|\le e^{-2300n}
\tag{14}
$$

for sufficiently large $n$, after harmlessly enlarging $S_*$ or the starting index. Here $D_i$ is the target signed-port projector. The frequency constant must account for $e^{b_1t_i}$; the older numerical choice $20N$ is not automatically sufficient after (10).

For gate heat, put $\tau_n=e^{-100n}/\eta$. Then
$e^{\tau_nK_n}=e^{e^{-100n}K^{\rm old}_n}$, and

$$
\mathsf T_{cd}=16e^{100n}A_c e^{\tau_nK}A_d,
\qquad A_c=A_{c,+}+A_{c,-},
\tag{15}
$$

has the old target transport limit with error $Ce^{-100n}$. Every factor is positive in every rival, and reversing a word gives its stationary adjoint. Ordinary hidden heat can also be written using natural zero-field killing:
$e^{tK}=e^t e^{t(K-I)}$.

## 4. Uniform polynomial recovery of killed heat

Let $A\le0$ be selfadjoint and $t>0$. With $Z=(I-tA)^{-1}$,

$$
e^{tA}=f(Z),\qquad
f(z)=e^{1-1/z}\ (z>0),\qquad f(0)=0.
\tag{16}
$$

There are universal constants $C,c>0$ and degree-$d$ polynomials $p_d$ such that

$$
\sup_{0\le z\le1}|f(z)-p_d(z)|\le Ce^{-c\sqrt d},\qquad
\|p_d\|_{\rm coefficient\ \ell^1}\le Ce^{Cd}.
\tag{17}
$$

Here is a direct proof. On the disk $|w-z|\le z/2$, with real $z>0$, one has $\operatorname{Re}(1/w)\ge2/(3z)$. Cauchy's estimate gives

$$
|f^{(k)}(z)|\le e\,k!(2/z)^ke^{-2/(3z)}
\le e\,3^k(k!)^2.
\tag{18}
$$

The function and all derivatives extend by zero at $z=0$. For the smooth periodic function $g(\theta)=f((1+\cos\theta)/2)$, Faà di Bruno's formula and $\left\{{k\atop j}\right\}\le j^k/j!$ for Stirling numbers give

$$
\|g^{(k)}\|_\infty
\le\sum_{j=1}^k e3^j(j!)^2\left\{{k\atop j}\right\}
\le e\,k3^kk!k^k
\le e(6e)^k(k!)^2.
\tag{19}
$$

The derivatives of $(1+\cos\theta)/2$ have absolute value at most one, which justifies the Bell-polynomial bound in this calculation. Integrating the Fourier coefficient of order $m$ by parts $k=\lfloor\sqrt{m/(24e)}\rfloor$ times gives
$|a_m|\le2e[(6e)k^2/m]^k\le2e4^{-k}$ for sufficiently large $m$. Truncating the cosine series proves the first estimate in (17), after summing its tail. This is a shifted Chebyshev polynomial in $z$. The recurrence bounds the monomial coefficient mass of $T_m(2z-1)$ by $7^m$; summing finitely many coefficients gives the second estimate.

For a natural killed generator $A=K-B_h$,

$$
Z=(I-t(K-B_h))^{-1}=\mathcal Z_h(1/t).
\tag{20}
$$

These polynomials act on the hidden Hilbert space. After embedding into the full physical space, a constant term multiplies $H_0$, rather than the full identity; expanding $H_0=I-J$ adds only visible-projector factors. Thus (17) approximates killed heat uniformly in **both** uncapped reversible models, with no generator cap, dimension bound or Trotter subdivision. The exact heat and exact proof kernels remain positive; the approximating polynomial is not assumed positive. Precision $e^{-C(n+1)^2}$ needs degree $O((n+1)^4)$ and logarithmic coefficient mass $O((n+1)^4)$.

## 5. Quantitative finite algebraic reduction

The entropy interface uses $O(n+1)$ signed selectors, cross-port factors and heat blocks. The exact factors $F_c$ are contractions, every exact killed or ordinary heat is a contraction, and all scalar normalizations in a complete entropy word have product at most $e^{C_0(n+1)^2}$. These estimates hold on every rival, since the only large factors are known scalar normalizations.

Replace each killed heat by (17), and each ordinary heat by $e^t p_d(\mathcal Z_0(1/t))$. Its duration $t=\tau_n$ is bounded for sufficiently large $n$. Choose degree $d\le C_1(n+1)^4$, with $C_1$ large enough that the total word error in either model is at most $e^{-600(n+1)}$. A telescoping expansion justifies this uniformly: polynomial approximants have operator norm at most $1+\varepsilon$, and the exact heat approximation error can be chosen $\varepsilon\le e^{-C_2(n+1)^2}$, beating all word normalizations.

Expand (7) and these heat polynomials. Every resulting scalar has at most

$$
L_n\le C_3(n+1)^5
\tag{21}
$$

normalized natural resolvent factors and logarithmic total coefficient mass at most $C_4(n+1)^5$. All their Laplace parameters satisfy

$$
z\ge c_0/(n+1)
\tag{22}
$$

for a fixed $c_0>0$: long tag durations are $O(n+1)$, short gate durations give large parameters, and $s$ is exponentially large.

Apply (2) to every natural resolvent and expand $H_0=I-J$. Each factor produces a fixed number of full physical resolvents and visible projectors, with scalar denominator inverse at most $C(n+1)$ by (3). The resulting rational scalar expressions have full physical word lengths $O((n+1)^5)$ and total coefficient bounds

$$
\exp\!\bigl(C(n+1)^5\log(n+2)\bigr).
\tag{23}
$$

Their dependence on the denominators has a Lipschitz bound of the same form. Indeed for $d,\widehat d\ge c/(n+1)$,
$|d^{-1}-\widehat d^{-1}|\le C(n+1)^2|d-\widehat d|$; telescope the products of at most $O((n+1)^5)$ such factors. Equation (23) also absorbs the fixed number of terms from expanding each $I-J$. Physical scalars in these expressions have absolute value at most one when endpoints are bounded by one, because normalized physical resolvents and $J$ are sub-Markov kernels.

Equations (21)–(23) are a finite reduction with polynomial logarithmic cost. Coupling them to the Gram-transfer estimate with polynomial degrees $M=O((n+1)^6)$ and integer-time cutoff $J_{\mathrm{cut}}=O((n+1)^7)$ gives the twelfth-power accuracy budget in the [fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md). Neither a rival rate cap nor an infinite switching limit is used.
