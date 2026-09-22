# Stronger prediction lower bounds from a reversible shift register

[Repository overview](../README.md) · [Earlier binary-tree lower bound](GENERAL_CONTROLLED_LOWER_BOUND.md) · [Binary bounded-rate upper bounds](BOUNDED_RATE_FINITE_FIELD.md) · [Unrestricted-family reversible upper bound](REVERSIBLE_GENERAL_COMPRESSION.md)

**Research theorem, 22 September 2026.** A positive reversible shift-register generator replaces the small-coupling function-space embedding in the earlier tree construction. Its controlled rank witness has only exponentially small, rather than Gaussian-in-depth, singular values. Polynomial interpolation of actual propagators then gives two stronger state lower bounds. One uses shrinking control dwell times; the other keeps a fixed minimum dwell time. Neither is a polynomial lower bound in the inverse tolerance. For these binary bounded-rate targets, the direct comparison is with the [polynomial nonreversible and singly exponential reversible upper bounds](BOUNDED_RATE_FINITE_FIELD.md); both gaps remain open. The arguments below are internal derivations, not a certification of originality.

## 1. Two finite-error lower bounds

Fix $k>0$, $H>0$, and $0<W\le G^2$. Targets belong to the original reversible family, and error means the supremum actual binary-mean error over all bounded piecewise-continuous protocols and all horizons. Competitors have a fixed initial law, fixed real readout, and at most $D$ Markov states, with a generator depending on the instantaneous field. Constant fields give time-homogeneous evolution. No field analyticity, reversibility, rate bound, or passive-data agreement is required of a competitor.

Put $L_\delta=\log(1/\delta)$. There are positive constants, depending only on the fixed parameters, such that for all sufficiently small $\delta$,

$$
\boxed{
D_*^{\mathrm{general}}(\delta)
\ge \exp\!\left(c\frac{L_\delta}{\log L_\delta}\right).
}
\tag{1}
$$

The witnesses use only $g=\pm\sqrt W$, with mass $1/2$ at each sensitivity level, and all nonzero internal relaxation rates in $[3k/2,5k/2]$. The field takes only the values $0$ and one fixed $h_*>0$.

There is a separate strengthening under a minimum dwell restriction. Fix any $a>0$, and restrict comparison to protocols whose positive-duration constant-field segments all last at least $a/k$. For this smaller protocol class,

$$
\boxed{
D_*^{\mathrm{dwell}\ge a/k}(\delta)
\ge\exp\!\left(c_a L_\delta^{2/3}\right).
}
\tag{2}
$$

The constants in (2) can also depend on $a$. The arbitrary-protocol lower bound (1) is stronger, but its proof uses progressively shorter intervals. The two statements must not be conflated.

More concretely, for every sufficiently large integer $n$ there is a target with $2^{4n+3}+1$ total states such that every predictor with fewer than $2^n$ states has error at least

$$
\begin{cases}
\exp[-C n\log(n+2)], &\text{using the unrestricted protocols in the proof},\\
\exp[-C_a(n+1)^{3/2}], &\text{using only dwell times at least }a/k.
\end{cases}
\tag{3}
$$

In the first case, the witness horizons are $O(n/k)$ and the shortest positive interval is of order $(\log n/n)^2/k$. In the second, horizons are $O_a(n^2/k)$. Signed combinations of many experiments appear in both proofs; these state lower bounds are not sample-efficient testing procedures.

## 2. A positive physical shift-register generator

The shift mechanism is a weighted undirected de Bruijn walk, supplemented by independent refresh. Its Fourier/Walsh deletion-and-shift representation and decomposition into tridiagonal chains are established: see [Philippakis, Mallinar, Pandit and Belkin (2024), Sections 2.2–2.3 and Theorem 3.1](https://arxiv.org/html/2410.07622v1), and the earlier spectral work discussed there. Those graph and spectral mechanisms are not claimed as discoveries here. The subsequent controlled-word witness and transfer to the specified physical prediction norm are the candidate additional results.

Rescale time to set $k=1$. Let $m=4n+3$, and take the $2^m$ bit strings $x=(x_1,\ldots,x_m)\in\{-1,+1\}^m$ as hidden physical states, with uniform stationary law $\mu$. Set

$$
g(x)=s x_1,\qquad s=\sqrt W.
$$

The centering, sensitivity bound and variance constraints hold exactly.

Let $L$ be the stochastic matrix that deletes $x_1$, shifts the remaining bits left and appends a fresh fair bit. Its transpose under the uniform law is the stochastic matrix $R=L^T$ that shifts right and prepends a fresh fair bit. Indeed, either directed operation has probability $1/2$ precisely when the corresponding overlap of $m-1$ bits agrees. Let $\Pi=\mathbf1\mu^T$ be independent uniform refresh. Define

$$
\boxed{
K=\frac32(\Pi-I)+\frac14(L+R-2I).
}
\tag{4}
$$

This is a sum of Markov generators. It is symmetric in physical coordinates and is irreducible because refresh supplies every off-diagonal entry with rate at least $3/(2\cdot2^m)$. There are no negative physical transition rates and no coupling parameter that shrinks with $n$.

### Walsh representation

The functions

$$
\chi_S(x)=\prod_{j\in S}x_j,\qquad S\subseteq\{1,\ldots,m\},
$$

form an orthonormal basis of $L^2(\mu)$. The empty subset represents the constant function. For a nonempty subset,

$$
L\chi_S=
\begin{cases}
\chi_{S+1},&m\notin S,\\
0,&m\in S,
\end{cases}
\qquad
R\chi_S=
\begin{cases}
\chi_{S-1},&1\notin S,\\
0,&1\in S.
\end{cases}
$$

Here $S\pm1$ shifts every index by one. Write $A$ for this sum of shifts on nonempty subsets and set $A\chi_\varnothing=0$. It is selfadjoint, with norm at most $2$. On centered functions,

$$
K=-2I+\frac14A.
$$

Consequently every nonzero internal relaxation rate lies in $[3/2,5/2]$, independently of register length.

Let $r=\chi_{\{1\}}=g/s$. Multiplication by $g/s$ toggles membership of the index $1$ in a Walsh subset. Its compression to centered functions is denoted by $B$; the transition from $\{1\}$ to the empty subset is removed. Thus $B$ is selfadjoint and $\|B\|\le1$.

Adding the state $A$ and the original external field rates gives the required target. Its zero-field visible path is still exactly the two-state telegraph law, and its equilibrium mean remains $\tanh h$.

## 3. A controlled Gram matrix with exponentially small singular values

Choose

$$
h_* =\min\{H,1/[20(1+s)]\}>0,
\qquad Q_0=Q(0),\quad Q_*=Q(h_*).
$$

Use the full inner product weighted by $\pi_0=(1/2,\mu/2)$. Centered hidden functions are extended by zero on the state $A$; their squared full norm is half their squared hidden norm.

On block-constant functions, $Q_0$ has eigenvalues $0,-2$. On centered hidden functions, it equals $-3I+A/4$. Therefore

$$
F=\frac{Q_0(Q_0+2I)}3
$$

annihilates the block-constant space and has centered hidden action

$$
\boxed{F=I-\frac13A+\frac1{48}A^2.}
\tag{5}
$$

In particular, $\|F\|\le7/4$. With $b_*=e^{-h_*}\sinh(sh_*)>0$, define

$$
Z_0=F^2,
$$

$$
Z_1=-\frac1{b_*}
F\left[Q_*-Q_0-(1-e^{-h_*}\cosh(sh_*))I\right]F.
$$

Their centered hidden actions are exactly

$$
Z_0=FIF,\qquad Z_1=FBF.
\tag{6}
$$

Both annihilate block-constant functions on either side and are selfadjoint in $L^2(\pi_0)$. Their norms are at most $(7/4)^2$, uniformly in $n$. Their expressions have generator-polynomial degree at most five, with coefficient sums bounded by a fixed constant depending on $s,h_*$.

### An exact leaf projection

For a bit word $b=(b_1,\ldots,b_n)\in\{0,1\}^n$, set

$$
v_b=Z_{b_n}\cdots Z_{b_1}Fr.
$$

Put $q=1/48$. Consider its projection onto Walsh subsets with maximum index $m=4n+3$. Each occurrence of $F$ can increase the maximum index by at most two. There are $2n+1$ such occurrences. Starting at $\{1\}$, reaching index $4n+3$ requires every $F$ to use its $qA^2$ term and both shifts in every $A^2$ to move right. No identity, single-shift, or backtracking term can reach that index. Toggling index $1$ cannot increase the maximum index of a nonempty subset; any erased constant component is annihilated by the next filter.

Under this unique maximal advance, each optional $B$ inserts a new index $1$, since the preceding right shifts have moved all existing indices above it. Its eventual location is $4(n-j)+3$ if it was inserted by $b_j$. Thus the selected leaf is

$$
S_b=\{4n+3\}\cup
\{4(n-j)+3: b_j=1,\ 1\le j\le n\},
$$

and the projection of $v_b$ onto these $2^n$ selected leaves is exactly

$$
q^{2n+1}\chi_{S_b}.
\tag{7}
$$

All selected subsets are distinct. It follows that their full Gram matrix satisfies

$$
\lambda_{\min}\bigl[\langle v_b,v_c\rangle_{\pi_0}\bigr]
\ge\frac12q^{4n+2}.
\tag{8}
$$

This conclusion uses an exact projection identity; it is not a numerical rank observation.

### Access through the visible mean

As in the earlier controlled lower bound, the endpoint identities are

$$
\pi_0Q_*F=\ell_*\langle Fr,\,\cdot\,\rangle_{\pi_0},
\qquad FQ_*S=r_*Fr,
$$

where

$$
\ell_*=2\sinh(h_*)\sinh(sh_*),\qquad
r_*=-2e^{-h_*}\sinh(sh_*).
$$

Here $S$ is the fixed visible readout. For $W_b=Z_{b_n}\cdots Z_{b_1}$, define

$$
\mathsf H_{bc}
=\frac{\pi_0Q_*F W_b^{\mathrm{rev}}W_cFQ_*S}{\ell_*r_*}
=\langle v_b,v_c\rangle_{\pi_0}.
\tag{9}
$$

Reversal means reversing the order of the $Z$ letters. In (9) it is their actual adjoint; for competitors it will remain a purely algebraic operation.

Every entry is a noncommutative polynomial in $Q_0,Q_*$ of total degree at most $10n+6$. Its generator-polynomial coefficient sum is at most $C^{n+1}$ for a fixed $C$. No inverse coupling that grows with $n$ is present.

## 4. Replace generator words by actual mean experiments

Suppose that each target generator $Q_a$, $a\in\{0,h_*\}$, is approximated by a finite signed propagator sum

$$
\mathcal Q_a=\sum_{j=0}^p d_j e^{t_jQ_a},
\qquad t_j\ge0,
$$

with common coefficient sum $J=\sum_j|d_j|$ and target operator error at most $\eta$. Substitute these sums throughout (9), preserving the same word reversal, and call the result $\mathsf H_{\eta}$.

The target generators, filters, and letters have norms bounded independently of register length. Fixed-degree polynomial perturbation and product telescoping therefore give constants $C_0,C_1$ such that, when $\eta$ is sufficiently small,

$$
\|\mathsf H_\eta-\mathsf H\|
\le 2^n C_0(n+1)C_1^n\eta.
\tag{10}
$$

All constants may depend on $s,h_*$ but not on $n$. Consequently there is a constant $A_0>0$ such that $\eta\le e^{-A_0(n+1)}$ ensures

$$
\sigma_{\min}(\mathsf H_\eta)\ge\frac14q^{4n+2}
\tag{11}
$$

for all sufficiently large $n$. The substituted matrix need not remain a Gram matrix or be symmetric; (10) transfers the singular-value bound.

Every expanded entry of $\mathsf H_\eta$ is a signed combination of actual visible means under protocols taking the two values $0,h_*$. A factor $e^{t_jQ_a}$ is a segment of duration $t_j$; zero-duration factors are omitted. The total coefficient sum per entry is at most

$$
C^{n+1}\max\{1,J\}^{10n+6}.
\tag{12}
$$

For any $D$-state competitor, apply exactly the same propagator sums and polynomial expressions to its generators, preparation and readout. The resulting matrix factors through $D$ coordinates, so its rank is at most $D$. No approximation statement about the competitor's generators is needed.

If this competitor has mean error at most $\delta$ on all the expanded protocols, then the entrywise error is bounded by (12) times $\delta$. For $D<2^n$, the rank and (11) force

$$
\boxed{
\delta\ge
\frac{q^{4n+2}}
{4\,2^n C^{n+1}\max\{1,J\}^{10n+6}}.
}
\tag{13}
$$

It remains to supply two propagator formulas with sufficiently small $\eta$ and controlled $J$.

## 5. A general interpolation estimate

The target generators satisfy $\|Q_a\|_{\pi_0}<5$. Indeed $\|Q_0\|\le7/2$, and the external field perturbation has norm at most $2(e^{(1+s)h_*}-1)<1/2$. Use $\Lambda=5$ below.

Let $I_p f$ be the polynomial of degree at most $p$ interpolating $f(t)$ at $p+1$ distinct nonnegative times in $[0,T]$. Write its derivative at zero as

$$
(I_pf)'(0)=\sum_{j=0}^p d_j f(t_j),\qquad
J=\sum_{j=0}^p|d_j|.
$$

This definition is valid even when zero lies outside the node interval. Applied to $f(t)=e^{tQ}$, it gives a signed sum of legal propagators. Compare with the Taylor polynomial

$$
P_p(t)=\sum_{\ell=0}^p\frac{t^\ell Q^\ell}{\ell!}.
$$

Interpolation is exact on $P_p$, and $P_p'(0)=Q$. The operator Taylor tail at every node has norm at most $e^{\Lambda T}(\Lambda T)^{p+1}/(p+1)!$. Hence

$$
\boxed{
\left\|\sum_jd_je^{t_jQ}-Q\right\|
\le J e^{\Lambda T}\frac{(\Lambda T)^{p+1}}{(p+1)!}.
}
\tag{14}
$$

This elementary argument avoids inferring derivatives of a competitor from a small observed error. Only the bounded target generator is approximated.

## 6. Arbitrary protocols: a polynomial coefficient budget

Chebyshev--Lobatto interpolation and endpoint differentiation are standard ingredients. The differentiation weights used here are an affine rescaling of the classical Chebyshev differentiation matrix implemented in [Trefethen's author-hosted `cheb.m`](https://people.maths.ox.ac.uk/trefethen/cheb.m), accompanying *Spectral Methods in MATLAB*. No interpolation or differentiation formula is claimed as new; its role here is to control the coefficient cost of replacing generator words by actual mean experiments.

Take $T=1$ and the Chebyshev--Lobatto nodes

$$
t_j=\frac12\left(1-\cos\frac{j\pi}{p}\right),
\qquad 0\le j\le p.
$$

The derivative weights at zero are

$$
d_0=-\frac{2p^2+1}{3},\qquad
 d_j=\frac{2(-1)^{j+1}}{t_j}\ (1\le j<p),\qquad
 d_p=(-1)^{p+1}.
$$

Their absolute sum is exactly

$$
J=2p^2.
\tag{15}
$$

These identities follow by differentiating the Lagrange basis at the endpoint. For example, the off-diagonal weights use the Chebyshev barycentric weights, and the sum follows from the elementary cosecant-square identity. They also hold for $p=1$.

Choose

$$
p_n=\left\lceil C_2\frac{n+1}{\log(n+2)}\right\rceil
$$

with a sufficiently large fixed $C_2$. Stirling's bound in (14) gives error at most $e^{-A_0(n+1)}$ for all sufficiently large $n$: $p_n\log p_n=C_2n(1+o(1))$, while the remaining logarithms in (14) are lower order. Meanwhile $\log J=O(\log(n+2))$.

Substituting in (13) yields

$$
\delta\ge e^{-C_3 n\log(n+2)}
$$

against every competitor with fewer than $2^n$ states. This is the first line of (3); inversion proves (1).

Every segment lasts at most one rescaled time unit, so the expanded experiments have total horizon at most $10n+6$. The smallest positive node is

$$
t_1=\frac12(1-\cos(\pi/p_n))\asymp p_n^{-2}.
$$

Restoring $k$ gives the stated shrinking dwell times and $O(n/k)$ horizon. This proof does not establish (1) under a fixed positive minimum dwell restriction.

## 7. Fixed minimum dwell: extrapolation with subexponential coefficients

Fix $a>0$, and now place every node in

$$
[a,T_n],\qquad T_n=(a+1)(n+1).
$$

Take the Chebyshev--Lobatto nodes of this interval, with degree $p_n=\lceil C_4(n+1)\rceil$. The derivative is still evaluated at zero, outside the interpolation interval.

Map the interval to $[-1,1]$. The evaluation point becomes

$$
x_0=-\frac{T_n+a}{T_n-a}=-\cosh\zeta_n,
\qquad
\zeta_n=\operatorname{arcosh}\left(1+\frac{2a}{T_n-a}\right)
\le2\sqrt{\frac{a}{T_n-a}}.
$$

For arbitrary node data bounded in absolute value by one, every Chebyshev coefficient of the interpolant has absolute value at most two, as follows from its discrete cosine formula. Moreover,

$$
|T_\ell'(x_0)|
=\ell\frac{\sinh(\ell\zeta_n)}{\sinh\zeta_n}
\le\ell^2e^{\ell\zeta_n}.
$$

Taking the supremum over these node data bounds the derivative-stencil coefficient sum:

$$
\boxed{
J\le\frac4{T_n-a}\sum_{\ell=1}^{p_n}\ell^2e^{\ell\zeta_n}
\le\frac{4p_n^3}{T_n-a}e^{p_n\zeta_n}
\le\operatorname{poly}(n)e^{C_a\sqrt n}.
}
\tag{16}
$$

Thus $\log J=O_a(\sqrt{n+1})$ despite the extrapolation.

The Taylor bound (14) still applies because all nodes are at most $T_n$. With $p_n=C_4(n+1)+O(1)$ and sufficiently large fixed $C_4$, Stirling's bound makes

$$
e^{\Lambda T_n}\frac{(\Lambda T_n)^{p_n+1}}{(p_n+1)!}
\le e^{-(A_0+1)(n+1)}
$$

after increasing $C_4$ further if necessary. The subexponential factor in (16) is then absorbed into the exponential accuracy budget for all sufficiently large $n$. Therefore (11)--(13) hold and give

$$
\delta\ge e^{-C_a'(n+1)^{3/2}}.
$$

This proves the second line of (3), and inversion proves (2).

Every positive segment is at least $a$, and every expanded experiment has horizon at most $(10n+6)T_n=O_a(n^2)$. Restoring $k$ gives a fixed minimum dwell $a/k$ and horizon $O_a(n^2/k)$. No analytic field dependence or rate bound on the competitor was used.

## 8. The cubic kernel remains small

The root $r=\chi_{\{1\}}$ evolves under $A$ only among the singleton subsets. On that $m$-dimensional subspace, $A$ is the ordinary path adjacency with off-diagonal entries one. Thus the cubic kernel has exactly $m$ modes,

$$
C(t)=\sum_{j=1}^{m}c_j e^{-\lambda_jt},
$$

$$
\lambda_j=k\left[2-\frac12\cos\left(\frac{j\pi}{m+1}\right)\right],
\qquad
c_j=\frac{2W}{m+1}\sin^2\left(\frac{j\pi}{m+1}\right).
$$

All weights are positive and all rates differ from $k$. The established analytic-in-field Markov cubic competitor class therefore has exact minimal state count $m+2=4n+5$, by the pole bound and Jacobi realization. The full controlled-mean task requires at least $2^n$ states even for the broader competitor class, by (13). The new construction preserves the exponential exact task separation while strengthening the finite-error bounds.

## 9. What remains open

The arbitrary-protocol lower bound in (1) exceeds every fixed power of the logarithm and is stronger than the previous $\exp(c\sqrt{L_\delta})$ result. It is still subpolynomial in $1/\delta$; a lower bound $(1/\delta)^c$ has not been proved. The fixed-minimum-dwell lower bound improves to (2), with a smaller exponent than the unrestricted timing result.

For the targets constructed here, the sharper upper comparison comes from [the finite-alphabet bounded-rate theorem](BOUNDED_RATE_FINITE_FIELD.md). Set $R_s=e^{(1+s)H}$, use the cap $\Lambda=5/2$, and write

$$
p=\frac{\log2}{\log(1+2/(5R_s))}.
$$

Let $D_{*,\mathrm{bin},5/2}(\delta)$ denote the worst-case unrestricted-predictor state count over all centered targets with actuator values $\pm s$ and internal rates at most $5k/2$. This class contains the shift-register targets. The present lower bound and the polynomial upper theorem give

$$
\exp\!\left(c\frac{L_\delta}{\log L_\delta}\right)
\le D_{*,\mathrm{bin},5/2}(\delta)
\le 1+\max\left\{2,
\left(\frac{1+2R_s^2}{\delta}\right)^p\right\}.
$$

The sufficient surrogate on the right can be nonreversible and preserves the stationary binary actuator distribution exactly. If the surrogate must remain reversible and retain the spectral cap, the same bounded-rate note supplies the stronger applicable sufficient bound

$$
D_{\rm rev}(\delta)
\le\exp\!\left[C\delta^{-p}\log(2/\delta)\right].
$$

That construction also preserves the exact actuator distribution, including $G$ and $W$. These sufficient bounds hold on all protocols and horizons, so they also apply to the smaller fixed-dwell comparison class. They do not prove an optimal-state separation between reversible and unrestricted predictors. A polynomial reversible bound remains open.

For the general family without a fixed actuator alphabet or spectral cap, the [reversible exact-variance upper bound](REVERSIBLE_GENERAL_COMPRESSION.md) remains double exponential in $L_\delta^2$. It is valid for the present targets too, but is not their sharpest available sufficient bound. The optimal general state order and the corresponding binary bounded-rate order both remain open. All statements count physical Markov states, not bit memory, parameter precision, computation time, or the sample cost of evaluating the signed interpolation formulas. The same binary passive path law, fixed actuator rule, and stationary preparation are retained throughout.
