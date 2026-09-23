# Rare binary tags with a distant balancing state

**Construction lemma, 23 September 2026.** This note gives a binary target encoding and positive approximate selectors for the signed ports of the nineteen-level lamp construction. It supplies the target-side ingredient of the [binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md); scalar observability and rival entropy are proved in the linked companion notes.

The construction changes the target family. Its rate-to-gap ratio is a very large fixed constant; no optimization is claimed. All chain, tag, balancing and logical states are physical and counted. The construction uses neither a new physical control nor a third actuator value.

## 1. Parameters and the underlying logical core

Use the nine-port logical graph from [the nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md), with its original unnormalized stationary weights of total one: the hub has weight $1/2$, and each of the nine ports has weight $1/18$. Write $M=2r2^r$, $r=2^n$. Each logical state has weight $1/(18M)$. Matching rates are $1/16$ and logical-state-to-hub rates are one, with the reverse rates fixed by detailed balance. Give **all** these states binary color zero.

There are eighteen signed port types: the nine port indices and the value of the logical sign $\sigma x_b$. Enumerate them by $j=1,\ldots,18$. Set

$$
\begin{gathered}
\eta=10^{-6},\qquad a=1+\eta,\qquad N=10^6,\qquad
m=100Nn,\\
\ell_j=1+j/20,\quad \phi(\ell)=4\ell-\ell^2,\qquad
\lambda_j=\ell_j^{-1}\exp\{Nn[-15+\phi(\ell_j)]\}.
\end{gathered}
\tag{1}
$$

Attach to each nonhub logical state $z$ one private color-one leaf $z'$: the rate $z\to z'$ is $\lambda_{j(z)}$, and the reverse rate is $\ell_{j(z)}$. Give the leaf weight $w_z\lambda_{j(z)}/\ell_{j(z)}$. Tag entrance rates tend to zero; their departure rates are bounded below by one. Their small stationary weight therefore creates no slow escape trap.

Attach to the logical hub $c_0$ a color-zero chain $c_1,\ldots,c_m$, with weights

$$
w(c_j)=a^j/2.
$$

Every forward chain rate is one and every backward rate is $1/a$. Let $W_0$ be the total color-zero weight and $W_t$ the total tag weight. Explicitly,

$$
W_0=1+\frac12\sum_{j=1}^m a^j,\qquad
0<W_t\le\frac12\max_j\frac{\lambda_j}{\ell_j}.
\tag{2}
$$

Add one color-one balancing state $B$ with weight $W_B=W_0-W_t$. Its only neighbor is $c_m$. Set its departure rate to $L=400$ and the reverse rate to $LW_B/w(c_m)$. Normalize all weights by $2W_0$ to obtain $\mu$.

The binary histogram is exactly balanced, since both colors have unnormalized weight $W_0$. Set $g=-\gamma$ on color zero and $g=+\gamma$ on color one, for any fixed $0<\gamma<1$. Attach the visible state, preparation and readout by the original field rule. Detailed balance holds on every hidden edge and hence at each fixed physical field as in the existing model.

The total physical state count is

$$
18M+m+3=36r2^r+100Nn+3.
\tag{3}
$$

There are $9M+1$ logical-core states, $9M$ private tags, $m$ added chain states, $B$, and the visible state. The port mass in the normalized hidden law is

$$
\mu(\text{port }c)=\frac1{36W_0}.
\tag{4}
$$

It is independent of the port and is bounded below by $c_*e^{-100n}$ for a fixed $c_*>0$, because $m\log a\le100n$. The small port mass will cost only $O(n)$ in logarithmic accuracy budgets.

## 2. A uniform gap and a fixed exit cap

The balancing-edge ratio satisfies

$$
\frac{W_B}{w(c_m)}\le\frac{W_0}{w(c_m)}
\le2+\frac{a}{a-1}<1{,}000{,}004.
\tag{5}
$$

Every hidden exit is therefore below $5\times10^8$. This crude bound is independent of $n$, $M$, and all logical table values.

For completeness, a weighted-path estimate gives a uniform positive spectral gap. Put $\beta=\sqrt a$. For a chain path starting at index $i$,

$$
\left(\sum_{k=i}^{m-1}d_k\right)^2
\le\frac{\beta}{\beta-1}\sum_{k=i}^{m-1}\beta^{k-i}d_k^2.
\tag{6}
$$

After multiplication by weights proportional to $a^i$ and summation over $i$, the coefficient at edge $k$ is at most

$$
\frac{\beta^2}{(\beta-1)^2}\,w(c_k).
\tag{7}
$$

Here is an explicit bound for the remaining path pieces. Let $R=\sum_{z\text{ logical, nonhub}}w_z(f_z-f_B)^2$. Since each tag weight is at most half its root weight, the tag contribution is at most $2\mathcal E_{\rm tag}+R$. Also $R\le2\mathcal E_{\rm star}+(f_{c_0}-f_B)^2$, because the total logical nonhub weight is $1/2$. These two inequalities bound the complete unnormalized sum to $B$ by $4\mathcal E_{\rm star}+2\mathcal E_{\rm tag}$ plus five times the ordinary weighted chain sum. Splitting the latter at $c_m$ and using (7) costs at most $10\beta^2/(\beta-1)^2$ times the chain energy, plus $10W_0(f_{c_m}-f_B)^2$. The balancing edge has conductance $LW_B$ and $W_B\ge W_0/2$, so its last contribution is at most $(20/L)\mathcal E_B$. Thus $\operatorname{Var}_\mu f\le\sum_x\mu_x(f_x-f_B)^2$ gives the deliberately loose bound

$$
\operatorname{Var}_\mu f
\le C_g\mathcal E_K(f,f),\qquad
C_g=\frac{100\beta^2}{(\beta-1)^2}.
\tag{8}
$$

Thus the hidden gap is at least $g_*=C_g^{-1}>0$. Rescaling every hidden rate by $1/g_*$ gives a family with gap at least one and a fixed exit cap $5\times10^8/g_*$. All subsequent estimates can be rescaled by the same fixed factor. We work below with the unrescaled generator $K$.

This is a uniform-gap construction, but its rate-to-gap ratio is not small. It does not preserve the earlier binary cap $6580$ or the nineteen-level band $[1,3]$.

## 3. Fixed killing makes the non-tag sector uniformly fast

Let $D_0,D_1$ be the binary color projectors and set

$$
A=K-uD_0,\qquad u=10^9.
\tag{9}
$$

The semigroup $e^{tA}$ is entrywise nonnegative and contractive in $L^2(\mu)$. It is an artificial killed semigroup used in the proof; observability must derive it from the actual bounded physical field protocols.

Split hidden space into private tags $T$ and the remaining sector $F$. In stationary orthonormal coordinates,

$$
A=\begin{pmatrix}-\mathcal L&V^*\\V&F\end{pmatrix},
\qquad \mathcal L=\operatorname{diag}(\ell_j),\qquad
\|V\|^2\le2\lambda_{\max}.
\tag{10}
$$

The last bound holds because every core vertex has precisely one private tag. Here $F$ includes the tag departure loss on its diagonal. All states in $F$ except $B$ are killed at rate $u$.

Let $\mathcal E_{\rm bulk}$ denote the edge Dirichlet energy within the non-tag sector, **before** adding killing or tag-departure loss. For a function on $F$,

$$
w_B|f_B|^2
\le\frac2L\mathcal E_{\rm bulk}(f,f)
+2\frac{W_B}{w(c_m)}\sum_{x\ne B}w_x|f_x|^2.
$$

Writing $X=\sum_{x\ne B}w_x|f_x|^2$, this gives $\|f\|_w^2\le(2/L)\mathcal E_{\rm bulk}+(1+2W_B/w(c_m))X$. Meanwhile $-\langle f,Ff\rangle_w\ge\mathcal E_{\rm bulk}+uX$. Hence $F\le-200I$ in quadratic-form order: $L/2=200$ and $u/(1+2W_B/w(c_m))>499$. The edge-energy and killing contributions are allocated separately in this inequality. In particular, $100$ is also a valid bound with substantial slack.

## 4. Distance suppresses the balancing-state contamination

Assign distance zero to the complete logical core and its tags, distance $j$ to $c_j$, and distance $m$ to $B$. Conjugate by the diagonal weight $e^{\theta d}$, with $\theta=\log4$. Only the ordinary chain edges change. The large balancing edge has endpoints of equal distance and is unchanged. In stationary coordinates each chain off-diagonal is $1/\sqrt a<1$, so the operator norm of the conjugation perturbation is at most

$$
2(e^\theta-1)=6.
\tag{11}
$$

The conjugated fast operator therefore generates a semigroup of norm at most $e^{-194t}$. The same statement holds for the negative weight. Consequently propagation between the core and $B$ gains a factor $e^{-\theta m}$ in addition to the fast time decay.

One can make the needed tag estimates explicit by expanding in the off-diagonal block $V$ in (10). Every tag-to-tag correction has at least two factors $V$; every tag-to-$B$ term has at least one $V$ and one core-to-$B$ fast propagation; every correction to the $B$--$B$ block has two such traversals. Since $\ell_j\ge1.05$ and $\|V\|$ is exponentially small, the time-ordered integrals, bounded by the contraction of the diagonal blocks, give fixed constants $C,c>0$ and, for all $t\ge0$,

$$
\begin{aligned}
\|(e^{tA})_{TT}-e^{-t\mathcal L}\|
&\le C\lambda_{\max}(1+t)^2e^{-t/2},\\
\|(e^{tA})_{TB}\|
&\le C\sqrt{\lambda_{\max}}e^{-\theta m}(1+t)^2e^{-t/2},\\
|(e^{tA})_{BB}|
&\le e^{-194t}
+C\lambda_{\max}e^{-2\theta m}(1+t)^2e^{-t/2}.
\end{aligned}
\tag{12}
$$

For example, the first inequality follows by summing the even-order perturbation series and using $e^{\|V\|t}e^{-t}\le e^{-t/2}$. For the second and third, place the exponentially weighted fast semigroup at each end adjoining $B$ before integrating. The constants do not depend on the number of logical states or the chain length.

The distance factor is essential. Without the long color-zero chain, a fixed-killing slow tag mode can have a balancing-state tail which remains significant after division by the tiny tag entrance rate.

## 5. Positive diagonal selectors on the target

For signed type $i$, put

$$
T_i=Nn(4-2\ell_i),\qquad
\kappa_i=\exp\{Nn(-15+\ell_i^2)\}.
\tag{13}
$$

Consider first the target expression

$$
J_i=\kappa_i^{-1}D_0KD_1e^{T_iA}D_1KD_0.
\tag{14}
$$

Each cross-color block of $K$ is entrywise nonnegative. Thus $J_i$ is nonnegative and selfadjoint. It is not yet an admissible uncapped observable expression because it contains unbounded generator blocks on a rival.

Ignoring the perturbations in (12), its private-tag contribution is diagonal on logical roots, with value

$$
\frac{\lambda_j\ell_j e^{-\ell_jT_i}}{\kappa_i}
=\exp\{-Nn(\ell_j-\ell_i)^2\}
\tag{15}
$$

at roots of type $j$. The value is one for $j=i$, and at most $e^{-2500n}$ otherwise. Let $D_i$ denote the target coordinate projector onto signed type $i$.

The perturbations in (12), after multiplication by the endpoint blocks, are bounded by a fixed constant times

$$
\kappa_i^{-1}(1+T_i)^2\left[
\lambda_{\max}^2e^{-T_i/2}
+\lambda_{\max}e^{-\theta m}e^{-T_i/2}
+e^{-194T_i}
+\lambda_{\max}e^{-2\theta m}e^{-T_i/2}\right].
\tag{16}
$$

The endpoint block to $B$ has a fixed norm, bounded by the fixed target exit cap, and is absorbed in the constant. All exponents in (16) are more negative than $-10^6n$: $T_i\ge0.2Nn$, $\lambda_{\max}\le e^{-11Nn}$, $\kappa_i^{-1}\le e^{14Nn}$, and $\theta m=100(\log4)Nn$. Therefore, for all sufficiently large $n$,

$$
\|J_i-D_i\|_{L^2(\mu)\to L^2(\mu)}\le e^{-2400n}.
\tag{17}
$$

The statement is uniform over the eighteen signed types. The lower restriction on $n$ only absorbs fixed constants; the asymptotic family may begin at that index.

## 6. Replace every generator block by a bounded positive word

For any reversible model, including an uncapped rival, set

$$
P_s=s(sI-K)^{-1},\qquad F_c=P_sD_cP_s,
\qquad s=e^{20Nn}.
\tag{18}
$$

These are positive selfadjoint operators. Define the common observable word

$$
E_i=\frac{s^2}{4\kappa_i}
F_0F_1e^{T_i(K-uD_0)}F_1F_0.
\tag{19}
$$

It is positive and selfadjoint on every rival. No rival generator norm or minimum stationary weight is assumed. On the target only, its fixed generator cap and $D_0D_1=0$ give

$$
F_0F_1=\frac2sD_0KD_1+O(s^{-2}),
\tag{20}
$$

in operator norm. The adjoint expansion holds for $F_1F_0$. Hence

$$
\|E_i-J_i\|\le\frac{C}{s\kappa_i},
\tag{21}
$$

with a fixed target-dependent constant. Since $s\kappa_i\ge e^{6Nn}$, equations (17)--(21) prove

$$
\boxed{\|E_i-D_i\|\le e^{-2300n}}
\tag{22}
$$

for sufficiently large $n$. The word has a fixed number of resolvent and killed-semigroup factors, total killed duration $O(n)$, and logarithmic normalization $O(n)$. Its resolvent scale is exponentially large in $n$, but it is a proof probe, not a physical target or rival rate restriction.

## 7. Positive logical transports and signed probes

For a port $c$, let $E_c$ be the sum of its two signed selectors. For the central signed probe use $E_{0,+}-E_{0,-}$. These approximate the old port projectors and signed central multiplication with operator error at most $2e^{-2300n}$.

For distinct adjacent logical ports define, on every model,

$$
\mathsf T_{cd}=\frac{1}{\lambda\tau}E_c e^{\tau K}E_d,
\qquad \lambda=1/16,\qquad \tau=e^{-100n}.
\tag{23}
$$

It is entrywise nonnegative and $\mathsf T_{dc}=\mathsf T_{cd}^*$. On the target, a first-order expansion gives

$$
\left\|\mathsf T_{cd}-\lambda^{-1}D_cKD_d\right\|
\le C\tau+C e^{-2300n}/\tau
\le C e^{-100n}.
\tag{24}
$$

The leading target block is exactly the original permutation transport. Triangular gate products are nonpalindromic and implement the old logical gates up to exponentially small error. Positive signed selectors supply the central probe in the same way as in the bounded-rate binary construction. The tiny central mass in (4) costs at most $e^{50n}$ when passing from global vector norms to conditional core norms, leaving exponentially small target defects.

The resolvent scale in (18) and the heat time in (23) must be independent. Reusing one small parameter can cancel the target approximation gain when a gate is normalized.

## 8. Proven observation and entropy interfaces

The [mixed killed-word observation theorem](MIXED_KILLED_WORD_OBSERVABILITY.md) recovers the required words from actual means with the original binary field rule, without a rival rate cap. The application has $O(n)$ primitive factors, total killed duration $O(n^2)$ and logarithmic normalization $O(n^2)$.

The [weighted whole-word repair lemma](WEIGHTED_WHOLE_WORD_REPAIR.md) supplies a positive change of measure and stationary repair on each rival's own states. It accounts for approximate projectors and the exponentially small target root mass; no global rival operator-norm bound is needed.

The [full binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) combines these interfaces with this construction. Its explicit error allocation requires $\delta\le e^{-C(n+1)^2}$ and then gives $D\ge2^{3\cdot2^n/4}$ for reversible rivals. The tagged family itself has a polynomial unrestricted sufficient count. A separate, explicitly stated union with the older binary family also has a polynomial unrestricted lower. Both conclusions retain the arbitrary-switching limitation and leave the exact uncapped reversible growth class unmatched.
