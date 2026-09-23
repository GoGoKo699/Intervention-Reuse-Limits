# A sharper finite nonnegative-atom obstruction

[Finite twelve-versus-eleven theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Capped observation calculus](CAPPED_KINETIC_INTERFACE_SEPARATION.md)

**Analytic refinement, 23 September 2026.** The ten-feature Gram matrix used in the finite state comparison has entrywise distance greater than $1/1500$ from every Gram matrix of at most ten nonnegative atoms. This improves the earlier sufficient tolerance $1/40000$ by a factor of $26\tfrac23$. The earlier theorem and its frozen proof remain unchanged. This note proves a stronger matrix obstruction; it does not assert a new controlled-mean tolerance or an efficient experiment set.

## 1. Matrix and claim

Let $U=\{1,2\}$ and $V=\{3,4,5\}$ be the two parts of $K_{2,3}$, and let $I=\{6,7,8,9,10\}$ be five isolated coordinates. Put

$$
d=(3,3,2,2,2),\qquad
G_* = \operatorname{diag}\left(
\frac1{48}
\begin{pmatrix}3I_2&\mathbf1_{2\times3}\\
\mathbf1_{3\times2}&2I_3\end{pmatrix},
\operatorname{diag}(d_i/24)_{i=1}^5
\right).
\tag{1}
$$

The first block has diagonal $1/16$ on $U$ and $1/24$ on $V$, with entry $1/48$ on every cross edge and zero between distinct vertices in the same part. Each isolated diagonal is at least $1/12$, and every off-diagonal involving an isolated coordinate is zero.

**Proposition.** If

$$
\widehat G=\sum_{s=1}^{r}x_sx_s^{\mathsf T},\qquad
x_s\in\mathbb R_+^{10},\qquad r\le10,
\tag{2}
$$

then

$$
\boxed{\|\widehat G-G_*\|_{\max}>\frac1{1500}.}
\tag{3}
$$

There is no normalization, lower mass bound or upper bound on the number of nonzero coordinates of an atom. In the state-comparison application, $x_s(i)=\sqrt{\widehat\mu_s}\,f_i(s)$; thus $r$ is the number of hidden states.

## 2. Eleven auxiliary witness vectors

Suppose instead that $\|\widehat G-G_*\|_{\max}\le\varepsilon$. For each of the six graph edges $e=\{u,v\}$ with $u\in U,v\in V$, define a vector in $\mathbb R_+^r$ by

$$
y_e(s)=\sqrt{x_s(u)x_s(v)}.
\tag{4}
$$

For each of the five isolated coordinates $i\in I$, define $y_i(s)=x_s(i)$. These eleven vectors all lie in the same $r$-dimensional atom space. Their Gram matrix $W$ has rank at most $r$. Write it in edge and isolated blocks as

$$
W=\begin{pmatrix}E&C\\ C^{\mathsf T}&Z\end{pmatrix}.
\tag{5}
$$

The construction is an argument about a hypothetical nonnegative factorization. It does not introduce new observable features, a hidden readout or an additional preparation. The observable data remain the entries of the original ten-by-ten matrix.

The diagonal bounds are

$$
E_{ee}=\widehat G_{uv}\ge\frac1{48}-\varepsilon,
\qquad Z_{ii}=\widehat G_{ii}\ge\frac1{12}-\varepsilon.
\tag{6}
$$

All overlaps below are nonnegative. Cauchy–Schwarz supplies their upper bounds.

If two distinct edges share $u\in U$, with other endpoints $v,w\in V$, then

$$
\langle y_{uv},y_{uw}\rangle
=\sum_s x_s(u)\sqrt{x_s(v)x_s(w)}
\le\sqrt{\widehat G_{uu}\widehat G_{vw}}
\le\sqrt{(1/16+\varepsilon)\varepsilon}.
\tag{7}
$$

If their shared endpoint lies in $V$, the corresponding bound is
$\sqrt{(1/24+\varepsilon)\varepsilon}$. For disjoint edges $uv$ and $u'v'$, both pairs $u,u'$ and $v,v'$ are target zeros, so

$$
\langle y_{uv},y_{u'v'}\rangle
\le\sqrt{\widehat G_{uu'}\widehat G_{vv'}}\le\varepsilon.
\tag{8}
$$

For an edge $uv$ and an isolated coordinate $i$,

$$
C_{uv,i}=\sum_s\sqrt{x_s(u)x_s(v)}\,x_s(i)
\le\sqrt{\widehat G_{ui}\widehat G_{vi}}\le\varepsilon.
\tag{9}
$$

Finally $0\le Z_{ij}=\widehat G_{ij}\le\varepsilon$ for distinct isolated coordinates.

Each edge has two other edges sharing its $U$ endpoint, one sharing its $V$ endpoint and two disjoint edges. Consequently

$$
\begin{aligned}
\lambda_{\min}(E)&\ge
\frac1{48}-3\varepsilon
-2\sqrt{(1/16+\varepsilon)\varepsilon}
-\sqrt{(1/24+\varepsilon)\varepsilon},\\
\lambda_{\min}(Z)&\ge\frac1{12}-5\varepsilon,\\
\|C\|_2^2&\le\|C\|_{\mathrm F}^2\le30\varepsilon^2.
\end{aligned}
\tag{10}
$$

The first two inequalities are symmetric diagonal-dominance bounds; the last uses the thirty entries of the six-by-five cross block.

## 3. Exact certificate at $\varepsilon=1/1500$

At this value,

$$
\sqrt{(1/16+\varepsilon)\varepsilon}
=\frac{\sqrt{379}}{3000}<\frac1{150},\qquad
\sqrt{(1/24+\varepsilon)\varepsilon}
=\frac{\sqrt{254}}{3000}<\frac2{375}.
\tag{11}
$$

Thus the sum of the off-diagonal entries in an edge row is strictly less than

$$
\frac2{150}+\frac2{375}+\frac2{1500}=\frac1{50}.
$$

Equations (6) and (10) give

$$
\lambda_{\min}(E)>
\frac1{48}-\frac1{1500}-\frac1{50}
=\frac1{6000},\qquad
\lambda_{\min}(Z)\ge\frac1{12}-\frac5{1500}=\frac2{25}.
\tag{12}
$$

In particular $Z$ is positive definite. The Schur-complement correction is bounded by

$$
\|CZ^{-1}C^{\mathsf T}\|_2
\le\frac{30(1/1500)^2}{2/25}=\frac1{6000}.
\tag{13}
$$

Therefore $E-CZ^{-1}C^{\mathsf T}$ is positive definite, and so is $W$. It follows that $\operatorname{rank}W=11$, contradicting $\operatorname{rank}W\le r\le10$. This proves (3), including its strict inequality. Smaller entrywise errors are covered by the same upper bounds.

More generally, (10) gives a sufficient obstruction whenever $0<\varepsilon<1/60$ and

$$
\frac1{48}-3\varepsilon
-2\sqrt{(1/16+\varepsilon)\varepsilon}
-\sqrt{(1/24+\varepsilon)\varepsilon}
>
\frac{30\varepsilon^2}{1/12-5\varepsilon}.
\tag{14}
$$

The rational certificate above avoids relying on a numerical root or an optimized constant. No optimal-distance claim is made.

## 4. Consequence and remaining quantitative bottleneck

The [finite state theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) constructs nonnegative features on every allowed rival and identifies their Gram with controlled-mean generator-polynomial scalars whenever the rival is ordinarily reversible. The present proposition can replace its earlier matrix obstruction without changing that construction, the target, the rate cap, the rival quantifier or the two-field interface. Any independent observation estimate placing every Gram entry within $1/1500$ is now sufficient to exclude ten hidden rival states.

This is a stronger tolerance for an intermediate Gram matrix, not a tolerance of $1/1500$ for the measured means. The earlier observation estimate contains large interpolation coefficients and a whole-word logarithm truncation. Those factors still have to be paid. Merely substituting the new matrix tolerance cannot justify a practical experimental precision, a short list of experiments or a microscopic implementation.

The square-root witnesses collect information from all six edge entries before counting dimensions. They avoid the loss from first assigning one of ten atoms to each witness. The resulting proof uses established nonnegative Gram, Cauchy–Schwarz and Schur-complement arguments.

The first five-by-five block in (1), multiplied by $48$, already appears in [Fawzi and Parrilo, *Self-scaled bounds for atomic cone ranks: applications to nonnegative rank and cp-rank*, arXiv:1404.3240](https://arxiv.org/pdf/1404.3240), Section 4.5, equation (55), at parameters $a=b=0$. That source proves its completely positive rank is six and discusses graph-based and semidefinite lower bounds. Neither this matrix nor its exact rank gap is claimed as new here. This note supplies the explicit entrywise perturbation estimate for the ten-coordinate block matrix needed by the controlled comparison, without a priority claim for the witness method or an optimal-distance claim.

Improving the observable reconstruction, or finding a certificate directly in finite-time response data, remains the larger quantitative task. Manuscript drafting remains deferred.
