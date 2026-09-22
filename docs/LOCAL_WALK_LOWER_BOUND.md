# Three prediction costs for a reversible walk through binary scenery

[Repository overview](../README.md) · [Sparse reversible upper bound](SPARSE_REVERSIBLE_COMPRESSION.md) · [Fixed-clock transfer lemma](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Analytic constant-step upper bound](ANALYTIC_CONSTANT_STEP_COMPRESSION.md)

**Research theorem, 22 September 2026.** The separation between passive observation, constant steps and switching already occurs when the internal dynamics consists of nearest-neighbor motion on disjoint paths and an independent stationary refresh. The path carries a binary scenery, and both the scenery and the walker position are counted as physical hidden states. The passive visible output is exactly two-state. The worst-case constant-step state cost is logarithmic in inverse error, whereas switching costs a positive power of inverse error, even on any fixed positive clock.

For this same target class, whole-component compression supplies a polynomial switching upper bound that preserves ordinary reversibility, the original exponential field rule, the exact binary actuator histogram and the same internal spectral interval. The upper and lower polynomial exponents are not matched. The general spectral-cap-only reversible problem remains open. Random walks in scenery, finite-rank realization, Walsh expansions and positive cubature are established ingredients; these internally audited statements do not certify publication originality. See the [prior-art assessment](PRIOR_ART.md).

## 1. Model, target class and statements

Fix $k>0$, $H>0$, and $0<W\le G^2$, and write $s=\sqrt W$. The original physical states are $A$ and a finite hidden set $\mathcal X$. The visible readout is $S(A)=-1$, $S(x)=+1$ for $x\in\mathcal X$. For a positive hidden stationary law $\mu$ and a centered sensitivity $g$, the rates are

$$
q_{Ax}(h)=k\mu_x e^{(1+g_x)h},\qquad
q_{xA}(h)=k e^{(g_x-1)h}.
\tag{1}
$$

The internal generator $K$ is field independent and reversible under $\mu$. All experiments start from $\pi_0=(1/2,\mu/2)$. The equilibrium at field $h$ is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(x)=\frac{\mu_xe^h}{2\cosh h}.
\tag{2}
$$

Define $\mathcal F_{\rm path}$ to be the targets for which $g$ takes precisely the values $\pm s$, each with stationary mass $1/2$, and

$$
K=L+\frac32k(\Pi_\mu-I),\qquad
\Pi_\mu=\mathbf1\mu^T.
\tag{3}
$$

Here $L$ is a $\mu$-reversible Markov generator whose undirected support is a disjoint union of finite paths and isolated vertices. Its nonzero relaxation rates are at most $k$. Equivalently the full internal cap in (3) is $5k/2$. Every nonzero internal relaxation rate of $K$ lies in $[3k/2,5k/2]$. The arbitrary path lengths, stationary weights, reversible edge rates and scenery assignments are part of the supplied target. The full $K$ includes global refresh and is not itself a nearest-neighbor generator.

Error is the supremum absolute error of the actual visible mean over the specified protocol menu and all observation horizons. A competing model has a fixed preparation, a fixed real readout and a finite physical Markov state space; its generator depends on the instantaneous field. Unless a stronger upper construction is explicitly stated, no reversibility, field analyticity, rate cap, passive agreement or original-family structure is imposed on competitors.

Let $D_*^{\rm path}(\delta)$ be the worst-case minimal such state count for all bounded piecewise-continuous protocols $|h|\le H$. Let $D_{\rm rev}^{\rm path}(\delta)$ require the surrogate also to be ordinarily reversible and use (1), with the exact stationary binary actuator histogram and internal spectral interval $[3k/2,5k/2]$. Its hidden graph need not equal the target graph. Put

$$
R_s=e^{(1+s)H},\qquad
p_{5/2}=\frac{\log2}{\log(1+2/(5R_s))}.
$$

For every fixed $a>0$, there are positive constants $c_a,\gamma_a,C,\delta_a$, depending only on the fixed parameters, such that

$$
\boxed{
c_a\delta^{-\gamma_a}
\le D_*^{\rm path}(\delta)
\le D_{\rm rev}^{\rm path}(\delta)
\le C\delta^{-(1+p_{5/2})},\qquad 0<\delta<\delta_a.
}
\tag{4}
$$

The lower bound already uses only fields $0,h_*$, where

$$
h_*=\min\{H,1/[20(1+s)]\},
\tag{5}
$$

and every positive-duration segment is an integer multiple of $a/k$. It therefore remains valid for this smaller protocol menu. Witnessing horizons are $O_a(\log(1/\delta)/k)$. The upper bound controls every allowed protocol and every horizon.

For the same target class and the common all-amplitudes constant-step task,

$$
\boxed{D_{*,\rm step}^{\rm path}(\delta)=\Theta(\log(1/\delta)).}
\tag{6}
$$

One fixed model must predict all amplitudes and times. The upper in (6) can use an analytic reversible generator, one fixed stationary zero-field preparation and binary readout, exact passive output, exact static mean, exact linear mean response and zero quadratic response. It does not impose the original field rule (1), the target internal graph, or a field-derivative bound uniform in $\delta$. Thus (6) is not an original-rate-rule constant-step upper theorem. Finally every target's passive visible path law is exactly the common rate-$k$ two-state telegraph law.

## 2. A finite physical scenery target

For any integer $m\ge2$, take

$$
\mathcal X_m=\{-1,+1\}^m\times\{0,1,\ldots,m-1\},\qquad
\mu(x,i)=\frac1{m2^m},\qquad g(x,i)=s x_i.
\tag{7}
$$

Let $\Delta_m$ be the reflecting path generator: its neighboring off-diagonal entries equal one, and its diagonal is minus the vertex degree. Set

$$
L_m=\frac{k}{4}I_{\{-1,+1\}^m}\otimes\Delta_m,
\qquad
K_m=L_m+\frac32k(\Pi_\mu-I).
\tag{8}
$$

Local motion leaves the entire scenery fixed and moves the walker one site. Global refresh independently redraws both the scenery and the position from $\mu$. There are $m2^m$ hidden states and $m2^m+1$ total physical states; no external random scenery or uncounted memory is supplied.

The sensitivity is exactly balanced, with $\mu g=0$, $\mu g^2=W$ and $|g|=s$. The path operator is symmetric and has relaxation spectrum

$$
-\Delta_m:\quad 2\left[1-\cos\left(\frac{\pi j}{m}\right)\right],
\qquad j=0,\ldots,m-1.
$$

Consequently $-L_m$ has cap $k$. On functions centered under $\mu$, refresh shifts each local relaxation rate by $3k/2$. Hence all nonzero internal rates are in $[3k/2,5k/2]$. Every physical internal off-diagonal rate is positive because refresh contributes $3k\mu(y,j)/2$.

At zero field every hidden state exits to $A$ at rate $k$, and $A$ exits to the hidden block at total rate $k$. Strong lumpability proves the exact two-state visible path law. Detailed balance under (2) gives the exact static mean $\tanh h$. The original-family response equations retain the common linear mean and zero quadratic mean response.

## 3. The cubic kernel has exactly $m$ active modes

The cubic kernel is $C_m(t)=\langle g,e^{tK_m}g\rangle_\mu$. Since $g$ is centered, the stationary refresh contributes the scalar factor $e^{-3kt/2}$. Averaging over the independent fair scenery bits gives $\mathbb E[x_ix_j]=\mathbf1_{i=j}$. Thus

$$
\begin{aligned}
C_m(t)
&=\frac Wm e^{-3kt/2}\operatorname{tr}e^{(kt/4)\Delta_m}\\
&=\frac Wm\sum_{j=0}^{m-1}e^{-\lambda_jt},\qquad
\lambda_j=k\left[2-\frac12\cos\left(\frac{\pi j}{m}\right)\right].
\end{aligned}
\tag{9}
$$

These $m$ rates are distinct, lie in $[3k/2,5k/2]$ and differ from $k$. Every weight is $W/m>0$. The [cubic pole-location bound and positive Jacobi realization](THEORY.md#8-exact-response-state-count-bound) therefore give the exact minimal cubic-response count

$$
\boxed{D_{\rm cubic}^{\rm exact}(m)=m+2.}
\tag{10}
$$

The lower in (10) is in the established analytic-in-field Markov competitor class: cubic field coefficients have poles only at eigenvalues of the unperturbed competing generator, and the target has at least $m+2$ distinct pole locations. The positive Jacobi realization attains this count using the original field rule. No analyticity assumption on competitors will be needed for the actual finite-field lower bound below.

## 4. A range-two filter and the controlled letters

Set $k=1$ temporarily and choose $m=4n+3$, $n\ge1$. Write $Q_0=Q(0)$ and $Q_*=Q(h_*)$ for the full backward generators. Use $L^2(\pi_0)$ and embed centered hidden functions by giving them value zero at $A$. Let $\mathsf H$ denote the orthogonal projection onto this hidden centered subspace. Its orthogonal complement is the two-dimensional space of functions constant on each visible block. On that complement $Q_0$ has eigenvalues $0,-2$.

Let $\Delta$ mean the path generator acting on the position coordinate separately for every scenery. On hidden centered functions,

$$
Q_0=\frac14\Delta-\frac52I.
$$

The polynomial filter

$$
F=\frac{Q_0(Q_0+2I)}3
\tag{11}
$$

annihilates both block-constant directions. Its centered hidden action is

$$
f(\Delta)=\frac1{48}\Delta^2-\frac14\Delta+\frac5{12}I.
\tag{12}
$$

More explicitly, on arbitrary hidden functions its hidden-to-hidden block is

$$
F_{BB}=f(\Delta)-\frac5{12}\Pi_\mu.
\tag{13}
$$

Indeed $f(0)=5/12$, $\Delta$ commutes with $\Pi_\mu$, and the constant hidden component must be killed. All blocks of $F$ touching $A$ vanish. The local term (12) moves position by at most two, and its coefficient for displacement $+2$, whenever the two forward edges exist, is exactly $1/48$. The extra term in (13) is essential: it accounts for the empty Walsh sector instead of silently treating every sector as purely local.

Let $r(x,i)=x_i=g(x,i)/s$, let $M$ multiply by $r$, and put $B=\mathsf H M\mathsf H$. Define

$$
b_*=e^{-h_*}\sinh(sh_*)>0,\qquad
c_*=1-e^{-h_*}\cosh(sh_*),
$$

$$
Z_0=F^2,\qquad
Z_1=-b_*^{-1}F(Q_*-Q_0-c_*I)F.
\tag{14}
$$

On hidden centered functions the field perturbation sandwiched between the two projections is $c_*I-b_*B$: only the hidden-to-$A$ exit rate changes the hidden diagonal, and $e^{h_*g}=\cosh(sh_*)+r\sinh(sh_*)$. Consequently

$$
Z_0=FIF,\qquad Z_1=FBF=FMF.
\tag{15}
$$

Both letters are selfadjoint in $L^2(\pi_0)$ and kill block-constant functions. Because the nonzero centered relaxation rates of $-Q_0$ are in $[5/2,7/2]$, (11) gives $\|F\|\le7/4$. Thus all filters and letters have norms bounded independently of $n$.

## 5. Exact Walsh leaves and a quantitative Gram bound

For a scenery subset $T\subseteq\{0,\ldots,m-1\}$, let

$$
\chi_T(x)=\prod_{i\in T}x_i.
$$

The Walsh characters are orthonormal in the uniform scenery law. The functions $\mathbf1_{\{i=j\}}\chi_T$ are orthogonal across both $j$ and $T$, with full squared norm $1/(2m)$. Multiplication $M$ at position $i$ toggles membership of the index $i$ in $T$.

For $b=(b_1,\ldots,b_n)\in\{0,1\}^n$, define

$$
W_b=Z_{b_n}\cdots Z_{b_1},\qquad v_b=W_bFr.
$$

Let $P$ project onto functions at the final position $m-1=4n+2$ whose Walsh subsets contain the index $0$. We claim

$$
\boxed{
Pv_b=48^{-(2n+1)}\mathbf1_{\{i=4n+2\}}\chi_{T_b},\qquad
T_b=\{0\}\cup\{4j:b_j=1,\ 1\le j\le n\}.
}
\tag{16}
$$

To prove it, expand each $F$ using (13) and each optional $B$ using $FMF$. Initially

$$
r=\sum_{i=0}^{m-1}\mathbf1_{\{\text{position}=i\}}\chi_{\{i\}}.
$$

A local term of $F$ preserves the Walsh subset and moves position by at most two. A $\Pi_\mu$ term annihilates every nonempty Walsh character and can only leave an empty character. A multiplier can acquire the bit $0$ only while the position is $0$.

Consider the last acquisition of bit $0$ along any nonzero contribution to $Pv_b$. If it occurs at the $j$th multiplier, then $2j$ of the $2n+1$ filters have already acted. No subsequent global projection can contribute without erasing that bit. The remaining local filters can move at most

$$
2(2n+1-2j)=4n+2-4j<4n+2,
$$

so they cannot take position $0$ to the final position. Thus bit $0$ must come from the initial term $\mathbf1_{\{i=0\}}\chi_{\{0\}}$ and survive throughout. Every global projection term vanishes in such a contribution.

There are exactly $2n+1$ filters. To cover distance $4n+2$, every one must make its maximal displacement $+2$, with coefficient $1/48$. There is exactly one such local path through every $\Delta^2$ term: two forward neighboring moves. At the $j$th optional multiplier the position is $4j$, so that multiplier inserts the new bit $4j$ if $b_j=1$. No bit is repeated. This proves (16), including all empty-sector possibilities.

The $2^n$ sets $T_b$ are distinct. Orthogonality and $\|\mathbf1_{\{i=4n+2\}}\chi_{T_b}\|_{\pi_0}^2=1/(2m)$ give

$$
\boxed{
\lambda_{\min}\bigl[\langle v_b,v_c\rangle_{\pi_0}\bigr]
\ge\frac{48^{-(4n+2)}}{2(4n+3)}.
}
\tag{17}
$$

Indeed the full Gram matrix is the projected diagonal Gram matrix plus the positive semidefinite Gram matrix of $(I-P)v_b$. This is an exact sum-of-squares argument, not a numerical rank calculation.

## 6. The Gram entries are accessible through the visible mean

For a centered hidden function $u$, direct evaluation of (1) gives

$$
\pi_0Q_*u=2\sinh(h_*)\sinh(sh_*)\langle r,u\rangle_{\pi_0}.
$$

The hidden centered part of $Q_*S$ is $-2e^{-h_*}\sinh(sh_*)r$. Define the nonzero constants

$$
\ell_*=2\sinh(h_*)\sinh(sh_*),\qquad
r_*=-2e^{-h_*}\sinh(sh_*).
$$

Selfadjointness of $F$ therefore gives the exact endpoint identities

$$
\pi_0Q_*F=\ell_*\langle Fr,\,\cdot\,\rangle_{\pi_0},\qquad
FQ_*S=r_*Fr.
\tag{18}
$$

With formal reversal of the order of the $Z$ letters, set

$$
\mathcal L_b=\ell_*^{-1}Q_*F W_b^{\rm rev},\qquad
\mathcal R_b=r_*^{-1}W_bFQ_*.
$$

In the target, reversal is the adjoint of $W_b$. Hence the matrix

$$
\mathcal G_{bc}=\pi_0\mathcal L_b\mathcal R_cS
=\langle v_b,v_c\rangle_{\pi_0}
\tag{19}
$$

has the singular-value bound (17). Each side polynomial has degree at most $5n+3$ in $Q_0,Q_*$ and coefficient sum at most $C_*^{n+1}$, with the dimension-independent choice

$$
C_*\ge\max\left\{1,|\ell_*|^{-1},|r_*|^{-1},
\frac{2+|c_*|}{b_*}\right\}.
\tag{20}
$$

The coefficient sum of $F$ is one; those of $Z_0$ and $Z_1$ are at most one and $(2+|c_*|)/b_*$, respectively. These statements concern formal generator polynomials. They will be replaced by finite signed combinations of legal experiments before being applied to competitors.

## 7. Transfer to a fixed positive experimental clock

The whole-side logarithm lemma in [POLYNOMIAL_CONTROLLED_LOWER_BOUND.md, Section 3](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md#3-a-general-lemma-for-total-degree-truncation) is dimension independent. Its hypotheses and the altered conditioning budget are recorded here to make the transfer explicit.

The target generators have spectrum in $[-5,0]$. At zero field $\|Q_0\|_{\pi_0}\le7/2$. In the $\pi_0$-weighted coordinates, the external-rate perturbation is the sum of a diagonal matrix of norm at most $e^{(1+s)h_*}-1$ and a star off-diagonal matrix of norm at most the same number. Thus

$$
\|Q_*-Q_0\|_{\pi_0}\le2(e^{(1+s)h_*}-1)<\frac12.
$$

Both generators are reversible under their own equilibria. The density ratio (2) has maximum divided by minimum $e^{2h_*}$, so the Hilbert-norm comparison costs at most $\kappa=e^{h_*}$. For any fixed $a>0$, put

$$
E_i=e^{aQ_i},\quad X_i=I-E_i,\quad q=1-e^{-5a},\quad
\varrho=\frac{1+1/q}{2}>1.
$$

Spectral calculus in the reversible norm, followed by this fixed norm comparison, gives

$$
\|X_i^j\|_{\pi_0}\le\kappa q^j\quad(j\ge1),\qquad
Q_i=-\frac1a\sum_{j\ge1}\frac{X_i^j}{j}.
\tag{21}
$$

The one-step norm of $X_i$ in the common norm need not be below one; the power estimate is enough.

For each complete side polynomial $P=\mathcal L_b$ or $\mathcal R_b$, replace $Q_i$ by the formal series

$$
Q_i(z)=-\frac1a\sum_{j\ge1}\frac{z^jX_i^j}{j}
$$

and retain only terms of total bookkeeping degree at most $M$. Denote the result by $P^{[M]}$. Define

$$
K_a=\frac\kappa a(\log2+5a),\qquad
B_a=C_*\max\{1,K_a\}^5,\qquad
A_a=C_*\max\{1,(\log2)/a\}^5.
$$

The lemma gives

$$
\|P-P^{[M]}\|\le B_a^{n+1}\varrho^{-(M+1)},\qquad
\|P\|\le B_a^{n+1},
\tag{22}
$$

and $P^{[M]}$ is a propagator polynomial of degree at most $M$ and coefficient sum at most

$$
J_n=4^M A_a^{n+1}.
\tag{23}
$$

For completeness, the error majorant at radius $\varrho$ sums each logarithm series to at most $(\kappa/a)\log[1/(1-\varrho q)]=K_a$. Ordered products preserve this coefficient bound without commuting distinct generators. For the propagator coefficients, treat $E_i$ as a formal letter: $\|(I-E_i)^j\|_{\mathrm{coeff},1}\le2^j$. At auxiliary radius $1/4$, the corresponding series sums to $(\log2)/a$. Removing that radius through degree $M$ costs at most $4^M$. These are precisely (22)--(23).

Truncate the two sides separately and define

$$
\mathcal G^{[M]}_{bc}=\pi_0\mathcal L_b^{[M]}\mathcal R_c^{[M]}S.
$$

Its operator error is at most

$$
\|\mathcal G^{[M]}-\mathcal G\|
\le3\,2^n B_a^{2(n+1)}\varrho^{-(M+1)}.
\tag{24}
$$

Here $\|\pi_0\|=\|S\|=1$ in the dual $\pi_0$ pairing; expand the two side errors and bound matrix norm by $2^n$ times the largest entry error. Choose an integer $M=M_n$ such that

$$
\boxed{
\varrho^{M_n+1}\ge
12(4n+3)2^n B_a^{2(n+1)}48^{4n+2}.
}
\tag{25}
$$

The factor $4n+3$ is required by the positional normalization in (17). This choice has $M_n=O_a(n+1)$, since $\log(4n+3)=O(n+1)$. Singular-value perturbation in (17) and (24) yields

$$
\sigma_{\min}(\mathcal G^{[M_n]})
\ge\frac{48^{-(4n+2)}}{4(4n+3)}.
\tag{26}
$$

Every matrix entry is now a finite signed combination of actual visible means, with coefficient sum at most $J_n^2$. Its experiments use at most $2M_n$ propagators, all at fields $0,h_*$ and duration $a$. Zero-degree identity factors are omitted and adjacent equal fields can be merged.

For any $D$-state competitor, evaluate these same finite propagator polynomials at its own actual propagators and use its fixed preparation and readout. The resulting matrix factors through $D$ coordinates, so its rank is at most $D$. The competitor is never Taylor expanded and its generator logarithm is never taken. Accuracy $\delta$ on the experiment menu implies matrix error at most $2^nJ_n^2\delta$. For $D<2^n$, (26) therefore forces

$$
\boxed{
\delta\ge
\frac{48^{-(4n+2)}}{4(4n+3)2^nJ_n^2}
\ge e^{-C_a(n+1)}.
}
\tag{27}
$$

The last constant is finite because $M_n=O_a(n+1)$; for example $4n+3\le7^n$ for $n\ge1$. Inverting (27) with strict error slack proves the first inequality of (4): for sufficiently small $\delta$, take $n=\lfloor\log(1/\delta)/(2C_a)\rfloor-1$, so any model attaining error $\delta$ needs at least $2^n\ge\tfrac14\delta^{-(\log2)/(2C_a)}$ states. Restoring $k$ makes the clock $a/k$ and the horizon at most $2M_na/k$.

This is a physical-state lower bound, not a sample-efficient testing procedure. The finite signed experiment combinations can have large coefficient sums and many terms. Separate truncation of the complete left and right sides is what preserves factorization through the competing state space.

## 8. The same class has a polynomial reversible switching upper bound

Apply the [stationary-flux fragmentation theorem](SPARSE_REVERSIBLE_COMPRESSION.md) to (3), with alphabet size two, $\Lambda=5/2$ and refresh coefficient $c=3/2$. The local spectral cap is $k$.

For an integer $b\ge1$, label the consecutive edges of each path and delete those in a uniformly chosen residue class modulo $b$. Each local edge is cut with probability $1/b$, and every remaining component contains at most $b$ vertices. The expected directed stationary removed flux, in units of $k$, is

$$
\mathbb E\Phi=\frac1{bk}\sum_x\mu_x(-L_{xx})\le\frac1b.
$$

The last inequality follows from the reversible local spectral cap, which bounds every exit rate by $k$. Therefore some choice of cuts has $\Phi\le1/b$. The resulting fragmentation profile is $S(\varepsilon)\le\max\{1,\lceil1/\varepsilon\rceil\}$.

With $C_R=1+2R_s^2$, take

$$
b=\max\{1,\lceil2R_s^3/\delta\rceil\},\qquad
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_R/\delta)}{\log(1+2/(5R_s))}\right\rceil-1\right\}.
$$

Edge deletion costs at most $R_s^3/b\le\delta/2$ in all-protocol mean error. Whole-component positive selection exactly matches stationary local actuator prefixes of length $\ell+1$ using at most $2^{\ell+1}$ retained components. Restoring the same refresh rate preserves those prefixes at the full internal clock. The regeneration estimate costs at most $C_R[5R_s/(2+5R_s)]^{\ell+1}\le\delta/2$. Thus

$$
D\le1+b2^{\ell+1}
\le1+2b\max\{2,(2C_R/\delta)^{p_{5/2}}\}
\le C\delta^{-(1+p_{5/2})}.
\tag{28}
$$

The selection copies complete physical components and reweights their stationary masses. It preserves their internal transition rates and detailed balance, and adding the original stationary refresh retains the band $[3k/2,5k/2]$. The one-symbol marginal preserves the exact actuator histogram. Using (1) then preserves the passive and static identities and the original low-order response calibration. These are genuine Markov states, with no uncounted component register.

This argument does not assume uniformly bounded conductance densities or their moments. In fact the targets (7)--(8) violate every fixed positive density-moment bound as $m\to\infty$. For $N=m2^m$ and off-diagonal density $q_{uv}=K_{uv}/(k\mu_v)$, each directed local edge has $q_{uv}=3/2+N/4$. There are $2(m-1)2^m$ such edges. For every fixed $\alpha>0$,

$$
\sum_{u\ne v}\mu_u\mu_v q_{uv}^{1+\alpha}
\ge\frac{m-1}{2m}\left(\frac N4\right)^\alpha\longrightarrow\infty.
\tag{29}
$$

The local-walk theorem therefore covers a family outside the earlier uniform density-moment condition. It closes a polynomial growth-class comparison for this path-plus-refresh target class, not the unrestricted cap-only reversible problem.

## 9. A logarithmic constant-step lower bound inside the same class

The [analytic constant-step theorem](ANALYTIC_CONSTANT_STEP_COMPRESSION.md) gives $O(\log(1/\delta))$ states uniformly over all capped original-family targets, hence over $\mathcal F_{\rm path}$. To show that the lower bound also holds inside this class, fix a competitor size $D\ge2$, let $r_0=D+4$, and use the target (7)--(8) with $m=3r_0$.

Use dimensionless time $\tau=kt$ and let $\lambda_j/k=2-\tfrac12\cos(\pi j/m)$. The cubic step formula from [THEORY.md](THEORY.md#8-exact-response-state-count-bound) has the positive decomposition

$$
m_3(\tau)=B_0(\tau)-\sum_{j=0}^{m-1}w_j e^{-\beta_j\tau},
\qquad B_0\in\operatorname{span}\{1,e^{-2\tau},\tau e^{-2\tau}\},
$$

$$
\beta_j=1+\lambda_j/k,\qquad
w_j=\frac{2W}{m(1-\lambda_j/k)^2}>0.
\tag{30}
$$

Select the $r_0$ indices $j=r_0,\ldots,2r_0-1$. On this central portion of the cosine spectrum,

$$
\frac74\le\frac{\lambda_j}{k}\le\frac94,\qquad
\left|\frac{\lambda_i-\lambda_j}{k}\right|
\ge\frac{|i-j|}{3r_0},\qquad
w_j\ge\frac{32W}{75r_0}.
\tag{31}
$$

For the spacing estimate, apply the mean value theorem to the cosine on $[\pi/3,2\pi/3]$, where sine is at least $\sqrt3/2$; the resulting derivative $\pi\sqrt3/(12r_0)$ is at least $1/(3r_0)$.

Define the Hankel operator of the positive sum in (30) on $L^2(e^{-\tau}d\tau)$. A selected exponential has Gram parameters

$$
a_j=\beta_j+\frac12=\frac32+\frac{\lambda_j}{k}\in[13/4,15/4],
\qquad \mathcal C_{ij}=\frac1{a_i+a_j}.
$$

For the selected $r_0\times r_0$ Cauchy matrix, the exact inverse diagonal identity is

$$
(\mathcal C^{-1})_{ii}
=2a_i\prod_{j\ne i}\left(\frac{a_i+a_j}{a_i-a_j}\right)^2.
$$

Relabel the selected indices as $i=0,\ldots,r_0-1$. Since $a_i+a_j\le8$ and the spacing is at least $|i-j|/(3r_0)$,

$$
\prod_{j\ne i}\frac{a_i+a_j}{|a_i-a_j|}
\le\frac{(24r_0)^{r_0-1}}{i!(r_0-1-i)!}
\le(96e)^{r_0-1}.
\tag{32}
$$

The last step uses $\binom{r_0-1}{i}\le2^{r_0-1}$, $(r_0-1)!\ge[(r_0-1)/e]^{r_0-1}$ and $r_0/(r_0-1)\le2$. Bounding the norm of the positive inverse by its trace gives

$$
\lambda_{\min}(\mathcal C)
\ge\frac1{8r_0(96e)^{2r_0-2}}.
$$

The positive Hankel operator of the selected sum therefore has its $r_0$th eigenvalue at least

$$
\boxed{
\sigma_{r_0}=\frac{4W}{75r_0^2(96e)^{2r_0-2}}.
}
\tag{33}
$$

The full sum in (30) adds a positive operator, so its $r_0$th eigenvalue is at least the same number. This statement concerns the $r_0$th eigenvalue, not the least eigenvalue of the full rank-$m$ sum; the remaining positive modes cannot weaken the rank-$r_0$ obstruction.

Only the target is Taylor expanded in the field. The [uniform target remainder](FINITE_FIELD.md#6-a-taylor-remainder-uniform-in-size-and-horizon) gives, for a constant step $0<z\le H$,

$$
\sup_{\tau\ge0}|m(z,\tau)-z m_1(\tau)-z^3m_3(\tau)|\le R_H z^4,
\qquad
R_H=\frac{365}{12}e^{2(1+s)H}(1+s)^4.
\tag{34}
$$

A $D$-state competitor's exact curve at field $z$ has Hankel rank at most $D$, by factoring $e^{(\tau+\sigma)\widehat Q(z)/k}$. Subtracting that curve from the baseline $z m_1+z^3B_0$ yields rank at most $D+3=r_0-1$, since $m_1=1-e^{-2\tau}$ lies in the same three-dimensional baseline span. Uniform curve error bounds Hankel operator error by the same number because $e^{-\tau}d\tau$ has mass one. Equations (30), (33) and (34) therefore force any uniform mean error $e_D$ to satisfy

$$
e_D+R_Hz^4\ge z^3\sigma_{r_0}.
$$

Take $z_D=\min\{H,\sigma_{r_0}/(2R_H)\}$. Then

$$
\boxed{
e_D\ge\frac12\sigma_{r_0}z_D^3\ge c e^{-CD}
}
\tag{35}
$$

for fixed positive $c,C$ and sufficiently large $D$. The polynomial factors in (33) are absorbed by increasing $C$. Inversion proves the logarithmic lower in (6), including against arbitrary nonanalytic or nonreversible competitors. The witness amplitude shrinks with $D$; the theorem concerns one predictor for all constant amplitudes and does not claim the same lower at every prescribed nonzero amplitude.

## 10. What the combined comparison establishes

All three tasks concern the same class $\mathcal F_{\rm path}$, with fixed $k,H,W$, binary sensitivities, stationary preparation and internal band $[3k/2,5k/2]$:

| Prediction task | Worst-case physical-state cost | Scope of the sufficient predictor |
|---|---:|---|
| Exact passive visible path law | $2$ | Exact two-state telegraph process |
| Actual mean for every constant amplitude and time | $\Theta(\log(1/\delta))$ | One analytic reversible calibrated Markov model; original exponential rate rule not imposed |
| Actual mean under arbitrary bounded switching | Between $c_a\delta^{-\gamma_a}$ and $C\delta^{-(1+p_{5/2})}$ | Original exponential rate rule, exact actuator histogram, ordinary reversibility and the same internal band |

The switching lower already holds on a fixed clock and therefore applies to both the broad and the structured predictor classes. The notation polynomial growth class means fixed positive lower and upper exponents; it does not assert equality of those exponents or equality of the optimal unrestricted and reversible state counts.

Along the explicit switching witnesses, $m=4n+3$, so the exact cubic minimum is $4n+5$, while precision $\delta_n=\tfrac12e^{-C_a(n+1)}$ requires at least $2^n$ states for full controlled means. This strengthens the task separation using local path motion plus refresh. It does not identify a necessary extra cost of reversibility: both unrestricted and reversible switching costs are polynomial for this class.

The full kinetic target is supplied to the constructor. No learning guarantee from passive data, experiment count, statistical sample bound, parameter-precision bound or computational efficiency claim is proved. Sparse fragmentation need not be available on general capped graphs; that remaining problem is separate from the one-dimensional result here.

The [dedicated exact verifier](../scripts/verify_local_walk_lower_bound.py) and [saved report](../reports/local_walk_lower_bound.json) check physical targets with 9 and 25 total states, the resolvent version of the trace kernel, detailed balance and both visible endpoints, and sparse Walsh leaf identities at depths one through three. They also check a conservative all-depth fixed-clock coefficient calibration. The cosine-spacing argument and all-size theorems above are proofs; finite examples support their algebra and do not replace those proofs. See [VERIFICATION.md](VERIFICATION.md) for the full checkpoint evidence and limits.
