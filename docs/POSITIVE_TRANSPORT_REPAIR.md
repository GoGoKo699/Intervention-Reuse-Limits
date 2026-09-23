# Balanced repair of positive transports

[Checkpoint](../README.md) · [Dynamic-lamp application](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md)

This note bounds a standard transport repair on the original state sets. Altschuler–Weed–Rigollet, [Algorithm 2, Lemma 7 and Appendix A.4](https://arxiv.org/pdf/1705.09634) (NeurIPS 2017; inspected preprint v2), already clip marginal excesses and fill deficits by an outer product. Their sequential clipping gives an entrywise $L^1$ estimate. Here both factors use the original marginals; the displayed bounds and controlled-word applications are proved directly.

## 1. Statement

Let $\mu$ and $\nu$ be strictly positive probability vectors on finite sets $I$ and $J$. Let $T:I\times J\to[0,\infty)$ be a nonnegative kernel, not necessarily stochastic. Its weighted adjoint is

$$
T^*_{ji}=\frac{\mu_iT_{ij}}{\nu_j}.
$$

Define

$$
\Delta_I=\sum_i\mu_i|(T1)_i-1|,
\qquad
\Delta_J=\sum_j\nu_j|(T^*1)_j-1|.
$$

There is a nonnegative kernel $U$ on the same sets such that

$$
U1=1,\qquad U^*1=1,\qquad
\sum_{i,j}\mu_i|T_{ij}-U_{ij}|
\le\frac32(\Delta_I+\Delta_J).
\tag{1}
$$

Thus $\mu U=\nu$, and $U,U^*$ are forward and reverse stochastic transports. In particular, if the two row-sum mean-square defects are at most $\varepsilon$, then

$$
\sum_{i,j}\mu_i|T_{ij}-U_{ij}|\le3\sqrt\varepsilon.
\tag{2}
$$

No reversibility of a square $T$ is required; the weighted adjoint relation is the hypothesis.

## 2. Explicit construction and proof

Set $F_{ij}=\mu_iT_{ij}$, and let its row and column sums be $r_i$ and $c_j$. Its total mass is $s=\sum F_{ij}$. Define

$$
a_i=\min\{1,\mu_i/r_i\},\qquad
b_j=\min\{1,\nu_j/c_j\},
$$

taking the factor to be one when the denominator is zero. Put $F^0_{ij}=a_i b_jF_{ij}$. Each row of $F^0$ has mass at most $\mu_i$, and each column at most $\nu_j$.

Let $d=\sum(F-F^0)$ be the removed mass. Row clipping costs at most $\sum_i(r_i-\mu_i)_+$ and column clipping at most $\sum_j(c_j-\nu_j)_+$, so

$$
d\le\frac{\Delta_I+s-1}{2}
+\frac{\Delta_J+s-1}{2}
=\frac{\Delta_I+\Delta_J}{2}+s-1.
\tag{3}
$$

Define residual marginals

$$
u_i=\mu_i-\sum_jF^0_{ij},\qquad
v_j=\nu_j-\sum_iF^0_{ij}.
$$

They are nonnegative and have common total mass
$\tau=1-\sum F^0=1-s+d$.
If $\tau>0$, put
$G=F^0+uv^T/\tau$; if $\tau=0$, put $G=F^0$.
Then $G$ has row marginal $\mu$ and column marginal $\nu$ exactly. Set $U_{ij}=G_{ij}/\mu_i$.

Its distance from the original flux satisfies

$$
\sum|F-G|\le d+\tau
=1-s+2d
\le\Delta_I+\Delta_J+s-1.
$$

Since $|s-1|\le\min(\Delta_I,\Delta_J)$, this is at most
$3(\Delta_I+\Delta_J)/2$, proving (1).
Cauchy--Schwarz gives $\Delta_I,\Delta_J\le\sqrt\varepsilon$, proving (2).

Apply the construction once to an unordered pair of state sets. In the reverse direction use the adjoint of the same repaired flux. Repairing each direction independently would not ensure the shared adjoint identity.

## 3. Error accumulated along a path

Consider state sets with prescribed probability measures $\mu_0,\ldots,\mu_L$, raw nonnegative kernels $T_j$ between successive sets, and repaired stochastic transports $U_j$ satisfying
$\mu_{j-1}U_j=\mu_j$. Assume every raw row sum is at most $C\ge1$, and

$$
\sum_{x,y}\mu_{j-1}(x)|T_j(x,y)-U_j(x,y)|\le e_j.
$$

The signed difference between the raw and repaired full path measures, both starting from $\mu_0$, has total $L^1$ norm at most

$$
\sum_{j=1}^Le_jC^{L-j}.
\tag{4}
$$

Indeed, telescope the product with repaired prefixes and raw suffixes. At the changed edge, the repaired prefix has exactly marginal $\mu_{j-1}$. The changed edge costs $e_j$, and a raw suffix of length $L-j$ has total mass at most $C^{L-j}$. Summing proves (4).

If each direction has row-sum mean-square defect at most $\varepsilon$, (2) gives the convenient bound

$$
3LC^{L-1}\sqrt\varepsilon.
\tag{5}
$$

Every path functional bounded in absolute value by one has expectation error at most (4), and in particular endpoint products of bounded features do. This scalar estimate avoids taking an unnecessary further square root.

## 4. A mixed-norm estimate without a row cap

The [binary proof, Section 5](BINARY_REVERSIBILITY_LOWER_BOUND.md#5-repair-under-an-operator-norm-bound), establishes the following variant on one finite probability space $(I,\nu)$. If $T\ge0$, $\|T\|_{2\to2}\le C$ with $C\ge1$, and

$$
\|T1-1\|_2,\ \|T^*1-1\|_2\le\varepsilon,
$$

the same clipping and deficit-fill construction gives stationary $U,U^*$ on the existing states with

$$
|\langle f,(T-U)g\rangle_\nu|
\le(2C+3)\varepsilon\|g\|_2,
\qquad |f|\le1.
\tag{6}
$$

For a product of $L$ kernels satisfying these hypotheses with common constants and bounded endpoint functions, the scalar product error is at most

$$
L(2C+3)C^{L-1}\varepsilon.
\tag{7}
$$

Repaired prefixes preserve the bounded left function under their adjoints; raw suffixes are controlled in $L^2$. Thus no pointwise raw row cap is needed. The full elementary proof is given in the linked section. This mixed-norm estimate is separate from the standard marginal $L^1$ repair guarantee cited above. It is used after positive diagonal normalization in the binary theorem, where a small normalizing vector could make raw row sums large.

## 5. Scope

The repair is algebraic and may create positive edges that were absent. It preserves state sets and stationary marginals. In the dynamic-lamp proof it supplies couplings on the rival's existing states; it is not asserted to be a new physical surrogate obeying the original rates. In Section 3, a row bound controls raw suffix mass; Section 4 instead uses an operator norm. Neither step bounds repaired transition probabilities beyond stochasticity. The rival rate cap in the physical applications is separately needed for the transfer from actual means to word scalars.
