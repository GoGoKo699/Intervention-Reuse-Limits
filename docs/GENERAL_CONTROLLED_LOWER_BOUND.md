# A larger state cost for general finite-field prediction

[Repository overview](../README.md) · [Stronger shift-register lower bounds](SHIFT_REGISTER_LOWER_BOUND.md) · [Reversible general upper bound](REVERSIBLE_GENERAL_COMPRESSION.md) · [Finite-field task](FINITE_FIELD.md) · [Actuator information](ACTUATOR_PROCESS.md)

**Research theorem, 22 September 2026.** Allowing several hidden states at each of just two sensitivity levels changes the finite-field state-complexity problem. This note constructs reversible targets with a bounded internal rate band for which bounded controlled-mean prediction requires more than every fixed power of the logarithm of the inverse error. The proof uses a binary tree in an orthonormal basis, a controlled Hankel matrix, and polynomial approximations of the logarithm of actual propagators. It imposes no field-derivative or rate bound on a competing Markov predictor. These are internal analytic arguments, not an originality certification.

**Historical role.** The [positive shift-register construction](SHIFT_REGISTER_LOWER_BOUND.md) now gives stronger finite-error lower bounds, both with unrestricted timing and with a fixed minimum dwell time. This note retains the earlier proof and its exact cubic-versus-full separation. Section 9 shows that truncating these particular weakly coupled tree targets already attains error $\exp[-\Theta(n^2)]$ below the $2^n$-state threshold, so improving their word filters alone cannot produce the stronger error scale.

## 1. Statement

Fix $k>0$, $H>0$ and $0<W\le G^2$. Let $\mathcal F(k,G,W)$ be the general reversible family in [THEORY.md](THEORY.md), and use the actual-mean error

$$
\mathcal D_H(F,\widehat F)=
\sup_{T>0}\sup_{|h|\le H}\sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|.
$$

Protocols are bounded and piecewise continuous. Competitors have at most $D$ physical Markov states, a fixed initial law and fixed real readout, and a generator depending only on the current field; constant fields give time-homogeneous evolution. They need not be reversible, analytic in the field, or calibrated to the target's passive or lower-order behavior.

Define $D_*^{\mathrm{general}}(\delta)$ as the supremum over targets in $\mathcal F(k,G,W)$ of the smallest competing state count attaining $\mathcal D_H\le\delta$. The competitor may depend on the supplied target. The [reversible upper theorem](REVERSIBLE_GENERAL_COMPRESSION.md) shows that this worst-case count is finite at every positive tolerance.

There are constants $c,C,\delta_0>0$, depending only on the fixed parameters, such that even targets whose nonzero internal relaxation rates lie in $[k,3k]$ satisfy

$$
\boxed{
D_*^{\mathrm{general}}(\delta)
\ge c\exp\!\left(c\sqrt{\log(1/\delta)}\right),
\qquad 0<\delta<\delta_0.
}
\tag{1}
$$

An equivalent useful form is that, for every integer $n\ge1$, a target with $2^{n+1}+1$ total states has

$$
\boxed{
\inf_{\widehat F:\,|\widehat F|<2^n}
\mathcal D_H(F_n,\widehat F)
\ge c e^{-C(n+1)^2}.
}
\tag{2}
$$

Every target uses only $g=\pm\sqrt W$, with each level having stationary mass $1/2$. Its passive visible path remains exactly the same two-state telegraph process. All mean data used by the lower bound come from protocols taking just the two field values $0$ and one fixed $h_*>0$, independent of $n$ and the tolerance.

The lower bound already holds for protocols whose every nonzero segment has duration an integer multiple of $1/(8k)$, with total horizon $O((n+1)^2/k)$. Thus it does not require increasingly rapid switching. The signed combinations used in the proof are not a practical sample-efficient reconstruction experiment.

There is also an exact-response separation within this family: the cubic response needs exactly $n+3$ states, whereas the full finite-field controlled mean needs at least $2^n$ states. Section 7 gives the kernel explicitly.

## 2. A binary tree in hidden function space

Rescale time so that $k=1$; the final result is restored by replacing every time by its value divided by $k$. Put $s=\sqrt W$, and choose $N=2^{n+1}$ hidden physical states with uniform $\mu$. Assign sensitivity $+s$ to half and $-s$ to half.

Work first in the real Hilbert space $L^2(\mu)$. The functions

$$
c=\mathbf1,\qquad r=g/s
$$

are orthonormal. The functions supported on the positive-sensitivity states with zero mean form a space $\mathcal H_+$ of dimension $2^n-1$; the corresponding negative-sensitivity space $\mathcal H_-$ has the same dimension. These two spaces are orthogonal to each other and to $c,r$.

Choose orthonormal bases in $\mathcal H_+$ and $\mathcal H_-$. Label them by the nonroot vertices of a complete binary tree of depth $n$: a vertex belongs to the positive or negative basis according to the last sign in its word. Each sign occurs $2^n-1$ times. The root is $r$; the remaining basis vector is $c$.

Let $A$ be the adjacency operator of this tree and set $Ac=0$. It is selfadjoint and $\|A\|\le3$. Let $P=I-|c\rangle\langle c|$ and define

$$
B=P\operatorname{diag}(g/s)P.
$$

On the centered hidden space, $B$ is zero at the root $r$, is $+1$ on each positive-labeled vertex, and is $-1$ on each negative-labeled vertex. Hence $\|B\|\le1$. Put

$$
P_\pm=\frac{I\pm B}{2}
$$

on that centered space.

For every length-$n$ sign word $w=(w_1,\ldots,w_n)$, form

$$
v_w=P_{w_n}A\cdots P_{w_1}A r.
$$

Its projection onto the leaves at depth $n$ is exactly the basis vector indexed by $w$. Indeed, reaching depth $n$ in $n$ adjacency steps requires moving away from the root at every step; the successive $P_{w_j}$ select precisely the prescribed child. Backtracking paths end at smaller depth and do not affect this projection. Consequently, for arbitrary real coefficients $a_w$,

$$
\left\|\sum_w a_wv_w\right\|_\mu^2\ge\sum_w a_w^2.
\tag{3}
$$

This is the source of the $2^n$-dimensional controlled Hankel matrix.

## 3. The operator is a positive reversible Markov generator

Set

$$
K_n=-2P+\varepsilon_n A,
\qquad \varepsilon_n=2^{-20(n+1)}.
$$

Although the tree was specified in a function basis, this is an ordinary generator on the $N$ physical hidden states. Since $\mu$ is uniform, selfadjointness means that its physical matrix is symmetric. It annihilates constants. Each physical entry of $A$ has absolute value at most $\|A\|\le3$, so, for $i\ne j$,

$$
(K_n)_{ij}=\frac2N+\varepsilon_n A_{ij}
\ge\frac2N-3\varepsilon_n\ge\frac1N>0.
$$

Thus $K_n$ is irreducible and reversible under the specified uniform law. Its nonzero relaxation rates lie in

$$
[2-3\varepsilon_n,2+3\varepsilon_n]\subset[1,3].
$$

Adding the state $A$ and the original field-dependent external rates gives a target with $N+1$ states, exactly two sensitivity levels, fixed variance $W$, and the required passive telegraph law. No negative transition rates occur in the physical model. Signed linear combinations below are used only in the proof.

## 4. Recovering the tree operators from finite-field generators

Let $Q_0=Q(0)$ and choose

$$
h_* =\min\{H,1/[20(1+s)]\}>0,\qquad Q_*=Q(h_*).
$$

Use the full equilibrium inner product $L^2(\pi_0)$, with $\pi_0=(1/2,\mu/2)$. Embed centered hidden functions by setting their value at the visible state $A$ to zero. Their full norm is their hidden norm divided by $\sqrt2$.

The full space splits orthogonally into the two-dimensional block-constant space and the centered hidden space. On the first, $Q_0$ has eigenvalues $0,-2$. On the second,

$$
Q_0=-3I+\varepsilon_n A.
$$

Define the polynomial filter

$$
F=\frac{Q_0(Q_0+2I)}3.
$$

It annihilates both block-constant modes, while on centered hidden functions

$$
F=I-\frac43\varepsilon_n A+\frac13\varepsilon_n^2 A^2.
\tag{4}
$$

In particular, $\|F-I\|\le5\varepsilon_n$ on that space.

Write $u_* =\sinh(sh_*)$ and $c_* =\cosh(sh_*)$. The following full-space operators annihilate the block-constant space on both sides:

$$
\mathsf A=\frac{F(Q_0+3I)F}{\varepsilon_n},
$$

$$
\mathsf B=
\frac{F[Q_*-Q_0-(1-e^{-h_*}c_*)I]F}{-e^{-h_*}u_*}.
$$

On the centered hidden space they are exactly

$$
\mathsf A=FAF,\qquad \mathsf B=FBF.
\tag{5}
$$

For the second identity, the compressed hidden block of $Q_*-Q_0$ is

$$
(1-e^{-h_*}c_*)I-e^{-h_*}u_*B.
$$

Both operators in (5) are selfadjoint. Their differences from $A,B$ are $O(\varepsilon_n)$ with absolute constants; for example one can use $40\varepsilon_n$ and $12\varepsilon_n$, respectively. Their norms are bounded independently of $n$.

Set $\mathsf P_\pm=(I\pm\mathsf B)/2$, and for a sign word define

$$
\mathsf W_w=\mathsf P_{w_n}\mathsf A\cdots\mathsf P_{w_1}\mathsf A.
$$

The full identity in $\mathsf P_\pm$ causes no problem: $\mathsf A$ annihilates the block-constant modes and $Fr$ is centered hidden. A product telescoping bound gives

$$
\|\mathsf W_wFr-v_w\|_\mu
\le C(n+1)6^n\varepsilon_n
$$

with an absolute constant, for example $C=105$. The matrix with these error vectors as columns has norm at most $2^{n/2}$ times this bound, which is less than $1/4$ for the displayed $\varepsilon_n$. By (3), the column matrix $\{\mathsf W_wFr\}_w$ therefore has least singular value at least $3/4$ in the hidden norm.

### The Gram matrix is made from mean responses

With $S(A)=-1$ and $S(B_j)=+1$, direct calculation gives

$$
\pi_0 Q_*F=\ell_*\langle Fr,\,\cdot\,\rangle_{\pi_0},
\qquad FQ_*S=r_*Fr,
$$

where

$$
\ell_*=2\sinh(h_*)\sinh(sh_*),\qquad
r_*=-2e^{-h_*}\sinh(sh_*).
$$

Both constants are nonzero. Thus the $2^n\times2^n$ matrix

$$
\mathsf H_{vw}
=\frac{\pi_0Q_*F\,\mathsf W_v^{\mathrm{rev}}
\mathsf W_wFQ_*S}{\ell_*r_*}
=\langle\mathsf W_vFr,\mathsf W_wFr\rangle_{\pi_0}
\tag{6}
$$

is a positive Gram matrix. Here “rev” reverses the order of the selfadjoint letters in the word. It is the actual adjoint in (6), but its algebraic definition will be retained for arbitrary competitors. Because the full norm is half the squared hidden norm,

$$
\lambda_{\min}(\mathsf H)\ge\frac{9}{32}.
\tag{7}
$$

Equation (6) is still expressed in generators. The next step replaces it by finite linear combinations of actual visible-mean experiments with a fixed minimum segment duration.

## 5. Fixed-duration propagators avoid assumptions on the competitor

Take the fixed dimensionless time $t_0=1/8$ and set

$$
E_a=e^{t_0Q(a)},\qquad a\in\{0,h_*\}.
$$

The target generators can be recovered to exponentially small operator error by the finite logarithm polynomial

$$
L_m(E)=-\frac1{t_0}\sum_{j=1}^m\frac{(I-E)^j}{j}.
\tag{8}
$$

This approximation is used only for the target, not asserted for a competitor.

### Uniform target approximation

In $L^2(\pi_0)$ the zero-field target generator has norm below $4$. The change in the external generator between $0$ and $h_*$ has norm at most

$$
2\left(e^{(1+s)h_*}-1\right)\le2(e^{1/20}-1).
$$

For example, this follows by bounding each of the four blocks in the decomposition $\mathbb R\oplus L^2(\mu)$ by $e^{(1+s)h_*}-1$. Hence $\|Q(h_*)\|_{\pi_0}<5$. Its spectrum is real and nonpositive because it is reversible under $\pi_{h_*}$. Both target spectra therefore lie in $[-5,0]$.

The density ratio of $\pi_{h_*}$ and $\pi_0$ has largest-to-smallest ratio $e^{2h_*}$. Transferring a selfadjoint operator bound from $L^2(\pi_{h_*})$ to $L^2(\pi_0)$ costs at most $e^{h_*}<1.1$. With

$$
\rho=1-e^{-5/8}<\frac12,
$$

this gives $\|(I-E_a)^j\|_{\pi_0}\le e^{h_*}\rho^j$. The logarithm series converges, including on the stationary eigenvector, and its tail obeys

$$
\|L_m(E_a)-Q(a)\|_{\pi_0}
\le\frac{e^{h_*}\rho^{m+1}}{t_0(m+1)(1-\rho)}
\le32\,2^{-m}.
\tag{9}
$$

No hidden dimension or internal rate enters this estimate.

### Substitution in the controlled matrix

Replace every occurrence of $Q_0,Q_*$ in $F$, $\mathsf A$, $\mathsf B$, the word expressions, and both endpoints of (6) by $L_m(E_0),L_m(E_{h_*})$. Call the resulting matrix $\mathsf H^{[m]}$.

If $\eta_m=32\,2^{-m}$, substitution in the fixed-degree polynomials gives endpoint errors $O(\eta_m)$ and letter errors at most $C_0\eta_m/\varepsilon_n$. Constants may depend on $s,h_*$ and the nonzero endpoint normalization factors, but not on $n$. The exact letter norms are bounded by fixed constants. Once $\eta_m/\varepsilon_n$ is small enough, the substituted norms are also bounded by fixed constants. Product telescoping over $O(n)$ factors and conversion from entrywise error to matrix norm then give

$$
\|\mathsf H^{[m]}-\mathsf H\|
\le C_1(n+1)2^n L^n\frac{\eta_m}{\varepsilon_n},
\tag{10}
$$

where $C_1,L$ are independent of $n$. One may use $L=100$: each composite letter $\mathsf P_\pm\mathsf A$ has norm at most $6$, substituted composite norms can be kept below $7$, and the two length-$n$ words contribute at most $7^{2n}$. Fixed endpoint factors are absorbed into $C_1$.

Choose

$$
m_n=40(n+1)+m_*,
$$

where the fixed integer offset $m_*$ is sufficiently large for the chosen $s,h_*$. Then $\eta_{m_n}\le c_{\log}\varepsilon_n^2$ with an arbitrarily small fixed $c_{\log}>0$. Since $\varepsilon_n=2^{-20(n+1)}$, the right side of (10) is at most $1/32$ for every $n\ge1$ after increasing $m_*$. Combining this with (7) yields

$$
\sigma_{\min}(\mathsf H^{[m_n]})\ge\frac14.
\tag{11}
$$

The substituted matrix need not be symmetric or an exact Gram matrix: the polynomial logarithm does not make the filter annihilate the $-2$ mode exactly. Only the perturbation estimate (10) and singular-value bound (11) are used.

### What its entries measure

The polynomial $L_m(E_a)$ is a signed linear combination of $I,E_a,\ldots,E_a^m$. Each $E_a^j$ is an actual segment at field $a$ of duration $jt_0$. Its sum of absolute polynomial coefficients satisfies

$$
\|L_m\|_{\mathrm{coeff},1}
\le\frac1{t_0}\sum_{j=1}^m\frac{2^j}{j}
\le16\,2^m.
$$

Expanding an entry of $\mathsf H^{[m_n]}$ therefore gives a finite signed linear combination of visible means under legal protocols taking values $0,h_*$. Zero powers are identities and can be omitted. Every nonzero segment is an integer multiple of $t_0$, so no interval shorter than $t_0$ is required. All experiments use the original fixed preparation and visible readout.

Let $J_n$ bound the sum of absolute coefficients in any expanded entry, including normalization. The two endpoints together have generator-polynomial degree at most six; each of the at most $4n$ letters has degree at most five and a coefficient factor bounded by $C_2/\varepsilon_n$. Writing $R_m=16\,2^m$ gives

$$
J_n\le C_3 R_{m_n}^{6}
\left(C_3\varepsilon_n^{-1}R_{m_n}^{5}\right)^{4n}
\le e^{C_4(n+1)^2}.
\tag{12}
$$

Increasing the fixed constants covers identity terms and both signs. Every expanded experiment lasts at most

$$
(20n+6)m_n t_0=O((n+1)^2).
$$

The number of signed experiments and the magnitudes of their coefficients can be large; the claim concerns the supremum prediction norm, not the sample complexity of estimating this matrix.

## 6. Rank forces the state count

Take any $D$-state Markov competitor from the stated class. Build a matrix $\widehat{\mathsf H}^{[m_n]}$ using exactly the same propagator-polynomial formulas and scalar coefficients as above, with its generators at $0,h_*$, initial law, and fixed readout. The reversed left words are defined by formal reversal, without assuming selfadjointness.

The matrix factors into a matrix of row vectors of length $D$ times a matrix of column vectors of length $D$. Hence

$$
\operatorname{rank}\widehat{\mathsf H}^{[m_n]}\le D.
$$

If the competitor's controlled-mean error is at most $\delta$, every individual experiment in an expanded entry differs by at most $\delta$. Equations (11)--(12) therefore imply

$$
\|\mathsf H^{[m_n]}-\widehat{\mathsf H}^{[m_n]}\|
\le2^nJ_n\delta.
$$

For $D<2^n$, a rank-deficient matrix is at operator-norm distance at least $\sigma_{\min}(\mathsf H^{[m_n]})\ge1/4$. Consequently,

$$
\delta\ge\frac1{4\,2^nJ_n}\ge c e^{-C(n+1)^2}.
$$

This proves (2), and inversion gives (1). Restoring $k$ changes the fixed minimum segment duration to $1/(8k)$ and all hidden relaxation rates to $[k,3k]$; it does not change the state count.

Only the target generators were approximated by logarithm polynomials in the proof. The competitor matrix was built exactly from its actual propagators. Its generators may have arbitrarily large rates, it may be nonreversible, and its field dependence need not be differentiable. No hidden derivative bound is inferred from a small mean error.

## 7. Exponentially more states than the cubic response needs

The root $r$ is invariant under automorphisms permuting the two children of every vertex. Its cyclic subspace under $A$ is therefore the radial subspace spanned by the normalized sums at depths $0,1,\ldots,n$. In this basis $A$ is the $(n+1)$-vertex path adjacency with every off-diagonal entry equal to $\sqrt2$.

Its eigenvalues and root spectral weights are explicit. Restoring $k$, the cubic kernel of the constructed target is

$$
C_n(t)=\sum_{j=1}^{n+1}c_j e^{-\lambda_jt},
$$

$$
\lambda_j=k\left[2-2\sqrt2\,\varepsilon_n
\cos\left(\frac{j\pi}{n+2}\right)\right],\qquad
c_j=\frac{2W}{n+2}\sin^2\left(\frac{j\pi}{n+2}\right).
$$

All $n+1$ weights are positive, the rates are distinct and differ from $k$, and their total mass is $W$. The [exact cubic pole bound and Jacobi realization](THEORY.md) therefore give an exact minimal cubic-response state count of $n+3$ in the established analytic-in-field Markov competitor class. The full finite-field lower bound permits the broader, potentially nonanalytic competitor class stated in Section 1.

By contrast, Section 6 proves that the exact full finite-field controlled mean needs at least $2^n$ states; the original $2^{n+1}+1$-state model supplies the matching exponential upper order. Thus, in one family with binary sensitivity and bounded internal rates,

$$
\boxed{
D_{\mathrm{cubic}}=n+3,
\qquad 2^n\le D_{\mathrm{full\ controlled}}\le2^{n+1}+1.
}
$$

This is a difference between prediction tasks. It does not say that every high-order response problem is hard, nor that a small cubic approximation error automatically produces the particular finite-field error in (2).

## 8. Interpretation and limits

The general bounded-sensitivity family has a strictly larger worst-case finite-field state order than the distinguished rank-one sensitivity subclass: the lower bound in (1) exceeds every fixed power of $\log(1/\delta)$. The distinction persists with two sensitivity values and a fixed internal rate band. It is produced by noncommuting controlled evolution, rather than a proliferation of scalar relaxation rates in the cubic kernel.

The upper bound for the general family remains much larger; the optimal order and the extra cost, if any, of requiring reversible approximants remain open. This result counts physical states, not parameter bits or run time. The signed polynomial combinations can have very large coefficients, so the proof is not a stable reconstruction algorithm or a practical statistical protocol. The lower bound already allows a fixed minimum switching interval $1/(8k)$; a shorter fixed horizon, a more restricted protocol menu, or statistical observation noise would require separate analysis.

## 9. Truncation limits this particular target sequence

The quadratic exponent in (2) is sharp in order for these targets at the threshold of fewer than $2^n$ states. This is an actual all-protocol, all-horizon approximation statement. It explains why the stronger [shift-register result](SHIFT_REGISTER_LOWER_BOUND.md) changes the target construction.

Work in rescaled time $k=1$. For $0\le d<n$, truncate the depth-$n$ tree at depth $d$ and realize it on its own $N_d=2^{d+1}$ hidden physical states. Retain the original coupling $\varepsilon_n=2^{-20(n+1)}$, rather than replacing it by $\varepsilon_d$. The truncated model has uniform stationary law, the same two actuator values $\pm s$ with equal masses, and baseline internal generator $-2P$. It is an admissible reversible physical surrogate: its off-diagonal internal rates are at least

$$
\frac2{N_d}-3\varepsilon_n\ge\frac1{N_d}>0,
$$

and all nonzero internal relaxation rates remain in $[1,3]$. Attach the same visible state and the original field rule.

### Finite-horizon comparison

In the full function-coordinate space, write

$$
Q_n(h)=Q_{\rm base}(h)+\varepsilon_n A_n.
$$

The base operator preserves the three-dimensional space spanned by the visible-state indicator, hidden constant and actuator root $r$. On this space it is the three-state model with symmetric hidden flip rate one. Every other tree coordinate, whose last sign is $\sigma\in\{-1,1\}$, evolves by scalar multiplication by $-2-e^{(\sigma s-1)h}$. Embed the truncated adjacency $A_d$ by removing every edge outside depths $0,\ldots,d$, while keeping $Q_{\rm base}$ unchanged. Unused coordinates are inaccessible from both scalar-response endpoints, so the embedded response equals that of the smaller physical surrogate.

Every controlled base propagator has $L^2(\pi_0)$ norm at most two, uniformly in its duration and the protocol. Indeed, the three-state block is a Markov propagator with reference weights $(1/2,1/4,1/4)$, so its supremum-norm contraction bounds its $L^2$ norm by two; the other coordinates are scalar contractions. Also $\|A_n\|,\|A_d\|\le3$.

Expand by Duhamel in $\varepsilon_n$, leaving the entire time-dependent base evolution unexpanded. A scalar term can detect a removed edge only by leaving the root, reaching that edge and returning. It therefore needs at least $M=2(d+1)$ adjacency insertions. All lower-order terms agree for every protocol. Each order-$j$ term has norm at most $2(6\varepsilon_n T)^j/j!$. Bounding both tails gives

$$
\sup_{0\le t\le T}|m_n[h](t)-m_d[h](t)|
\le4e^{6\varepsilon_n T}
\frac{(6\varepsilon_n T)^{2(d+1)}}{[2(d+1)]!}.
\tag{13}
$$

### Extending the estimate to every horizon

Both models have a common reset to the visible state $A$ at rate at least $\alpha=e^{-(1+s)H}$. Subtracting this reset leaves a Markov generator. Hence changing a model's initial distribution changes its final binary mean by at most $2e^{-\alpha T}$ after a duration $T$, for every bounded protocol. For observations later than $T$, restart both models from their own zero-field equilibria $T$ before the observation and apply (13) to the last $T$ units. For earlier observations use (13) directly. Thus, for every $T>0$,

$$
\mathcal D_H(F_n,F_d)
\le4e^{-\alpha T}
+4e^{6\varepsilon_n T}
\frac{(6\varepsilon_n T)^{2(d+1)}}{[2(d+1)]!}.
\tag{14}
$$

Take $d=n-2$ for $n\ge2$. The surrogate has $2^{n-1}+1<2^n$ total states. With $T=(n+1)^2/\alpha$, the first term in (14) is $4e^{-(n+1)^2}$, and the logarithm of the second term is

$$
-40(\log2)n^2+O_{s,H}(n\log(n+1)).
$$

Consequently, for fixed positive constants $c_H,C_H$,

$$
\inf_{\widehat F:\,|\widehat F|<2^n}
\mathcal D_H(F_n,\widehat F)
\le C_H e^{-c_H n^2}.
\tag{15}
$$

Together with (2), this sandwiches the best error for this sequence between two bounds with quadratic exponents in $n$. Changing polynomial filters or conditioning the word matrix cannot make this same sequence prove an error lower bound $e^{-O(n)}$ at this state threshold. This obstruction does not apply to the positive constant-coupling shift-register targets. The constants and cutoff time in (14) are not asserted to be optimal.
