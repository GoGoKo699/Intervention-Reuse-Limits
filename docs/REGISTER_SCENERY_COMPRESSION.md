# Uniform polynomial reversible compression of a register scenery dictionary

[Repository overview](../README.md) · [Aggregation lower bound](AGGREGATION_STATE_LOWER_BOUND.md) · [Expander scenery compression](EXPANDER_SCENERY_COMPRESSION.md) · [Bounded-rate prediction](BOUNDED_RATE_FINITE_FIELD.md)

**Research theorem, 22 September 2026.** The entire register-dictionary family used in the aggregation lower bound admits polynomial-size reversible prediction, uniformly over every register width and every accuracy. The construction preserves the original field rule, exact actuator histogram and advertised spectral band. It creates new physical states whose short scenery statistics approximate those of the supplied target.

The actuator has **six fixed values**, not a binary alphabet. The target contains all independent scenery configurations as counted hidden states. A shorter register reproduces their finite-prefix statistics with an explicit collision error; positive selection of complete configuration models then removes almost all of its dictionary. This uniform upper is stronger than a size bound only at a specially chosen sequence of witness accuracies.

The result does not cover arbitrary frozen scenery or resolve the general cap-only problem. Ordinary reversibility is retained throughout. Its comparison with aggregation is a comparison between two reversible model architectures, not a lower bound against every reversible predictor.

## 1. The counted dictionary and physical model

Fix $k,H>0$, $\lambda=1/8$ and

$$
\gamma_j=j/10\quad(j=1,2,3),\qquad G=3/10.
\tag{1}
$$

For an integer $n\ge1$, an address is $v\in\{0,1\}^{\mathbb Z_n}$, and the number of addresses is $r=2^n$. A configuration $x$ assigns a sign $x_v$ to every address. The target includes all $2^r$ configurations, with uniform stationary weight. There are three ports $j\in\{1,2,3\}$ and a sign coordinate $\sigma\in\{-1,+1\}$. Its hidden states are

$$
(x,j,\sigma,v),\qquad
\mu(x,j,\sigma,v)=\frac1{6r2^r},\qquad
 g(x,j,\sigma,v)=\sigma\gamma_jx_v.
\tag{2}
$$

Thus the complete physical target, including $A$, has

$$
\boxed{1+6r2^r=1+6\cdot2^n\cdot2^{2^n}\text{ states}.}
\tag{3}
$$

Each individual fixed-configuration model already has mass $1/6$ at each of the six actuator values $\pm\gamma_j$: the sign coordinate pairs opposite values at every address and port. The entire dictionary and every mixture of complete configurations share this exact histogram. In particular, $\mu g=0$, $|g|\le G$ and $W=7/150$.

Let $R$ rotate coordinate positions by one, $J$ reverse the binary register, $V=RJ$, and $X$ toggle coordinate zero. We fix literal reversal on coordinate indices:

$$
J:i\mapsto-i-1,\qquad R:i\mapsto i+1,
\qquad V=R\circ J:i\mapsto-i.
\tag{4}
$$

The corresponding address map transports the bit at coordinate $i$ to its image. Chronological address-map composition has the ordinary order; backward pullback matrices reverse that order. The proof uses word lengths and relative transformations and does not identify these two conventions. The alternative reflection $J:i\mapsto-i$, $V:i\mapsto1-i$ gives the same estimates when used consistently.

Put $U_1=J$, $U_2=V$, $U_3=X$. All three are involutions. At port $j$, a matching update applies $U_j$ to the address. Other local moves change the port along the complete three-vertex graph. The local generator is

$$
L_n=k\lambda\left[\sum_{j=1}^3D_j(U_j-I)+K_3\right],
\tag{5}
$$

where $D_j$ selects port $j$ and $K_3$ has off-diagonal entries one and diagonal $-2$. The configuration and sign coordinate are unchanged by local moves. A complete fixed-configuration model has $6\cdot2^n$ states; its two sign sectors may be disconnected locally.

The matching part has relaxation cap $2k\lambda$, and the port part has cap $3k\lambda$. Their sum is reversible and has cap at most $5k\lambda=5k/8\le k$. At the common local clock $k$, its update is exactly:

- hold with probability $1-3\lambda$;
- apply the matching involution of the present port with probability $\lambda$;
- move to each of the two other ports with probability $\lambda$.

These potential choices are independent of the address. If a matching involution fixes an address, that update is an additional actual hold; the representation remains exact.

Restore stationary refresh,

$$
K_n=L_n+\frac{3k}{2}(\Pi_\mu-I).
\tag{6}
$$

It redraws the configuration, address, port and sign. Every internal off-diagonal rate is positive. Ordinary detailed balance holds, and every nonzero internal relaxation rate lies in the advertised band $[3k/2,5k/2]$; the actual upper cap is at most $17k/8$.

Attach $A$ with the original field rule

$$
q_{A,i}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{i,A}(h)=k e^{(g_i-1)h}.
\tag{7}
$$

Use zero-field equilibrium preparation and the fixed readout $S(A)=-1$, $S(B_i)=+1$. All approximation claims concern the actual mean under deterministic piecewise-continuous protocols with $|h(t)|\le H$, uniformly over all observation times.

## 2. Main theorem and finite budgets

Define

$$
\mathcal R=e^{(1+G)H},\qquad C_{\mathcal R}=1+2\mathcal R^2,
\qquad A_H=e^{2GH},\qquad \Lambda=5/2,
$$

$$
q=\frac{\Lambda\mathcal R}{1+\Lambda\mathcal R},\qquad
\beta=-\log q=\log\left(1+\frac1{\Lambda\mathcal R}\right),
\qquad p_{\rm reg}=\frac{\log96}{\beta}.
\tag{8}
$$

**Theorem.** For every original width $n\ge1$ and every $0<\delta<1$, there is a surrogate with

$$
\boxed{
\sup_{h,t}|m_{F_n}[h](t)-m_{\widehat F}[h](t)|\le\delta,
\qquad D\le C_H\delta^{-p_{\rm reg}}.
}
\tag{9}
$$

Its fixed physical parameters are those in (1); the constant may also be written as depending on those fixed parameters. The surrogate is ordinarily reversible, uses (7), has the exact six-level histogram, fixed readout and stationary preparation, and retains the advertised band $[3k/2,5k/2]$. The passive telegraph path law, equilibrium curve, reference linear mean response and zero quadratic response are consequently preserved.

An explicit choice is

$$
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_{\mathcal R}/\delta)}\beta\right\rceil-1
\right\},
$$

$$
n_0=\max\left\{4\ell+1,
\left\lceil2+2\log_2\left(
\frac{2C_{\mathcal R}A_H\ell(\ell+1)}\delta
\right)\right\rceil\right\}.
\tag{10}
$$

The finite state budget is

$$
\boxed{D\le1+6^{\ell+2}2^{n_0}.}
\tag{11}
$$

If $n\le n_0$, the construction selects configurations of the original width $n$. It does **not** retain the enormous original dictionary. If $n>n_0$, it first replaces the address register by width $n_0$, then selects configurations.

## 3. Formal transformations and the absence of wrapping

Index coordinates temporarily by $\mathbb Z$. A word in $J,V,X$ acts by a coordinate permutation

$$
i\mapsto\varepsilon i+a,\qquad
\varepsilon\in\{-1,+1\},\quad a\in\mathbb Z,
$$

followed by addition modulo two of a finitely supported binary vector $c$. Call $(\varepsilon,a,c)$ its formal affine transformation. A word of length at most $L$ satisfies

$$
|a|\le L,\qquad \operatorname{supp}(c)\subset[-L,L].
\tag{12}
$$

Each reflection has translation offset of absolute value at most one, so composition increases the translation bound by at most one per letter. Each toggle is transported to an image of coordinate zero under a suffix of the word, also lying in this interval. Repeated toggles add modulo two and cannot enlarge the support.

The finite $n$-bit action is obtained by reducing all coordinate indices modulo $n$. Two prefixes of a word with at most $\ell$ address letters have a relative word of length at most $2\ell$, including the inverse of one prefix. Its translation is bounded by $2\ell$ and its toggle support lies in $[-2\ell,2\ell]$.

If $n\ge4\ell+1$, distinct positions in that interval cannot merge modulo $n$. A nonzero pure toggle stays nonzero. A nonzero rotation of absolute displacement at most $2\ell$ cannot become the identity rotation. A reflection cannot become the identity permutation for $n>2$. Thus formal identities agree on every finite address, whereas a formal nonidentity cannot become the identity affine map solely by finite-width wrapping.

A nonidentity affine map can still fix a particular randomly chosen address. That separate event is the only collision error used below.

## 4. Accidental address collisions

Let $T$ be a formally nonidentity relative transformation of length at most $2\ell$, with $n\ge4\ell+1$. Its equality $Tv=v$ on a uniform binary address solves

$$
(I-P_T)v=c_T
\tag{13}
$$

over $\mathbb F_2$. The probability is either zero or $2^{-\operatorname{rank}(I-P_T)}$.

If the coordinate permutation is identity, the finite toggle vector is nonzero, so there is no solution. For a nonidentity rotation by $a$ modulo $n$, the permutation has $\gcd(n,a)$ cycles, giving rank $n-\gcd(n,a)\ge n/2$. For a reflection $i\mapsto-i+a$, at most two coordinates are fixed and the others form transpositions. Its rank is at least $(n-2)/2$. Consequently

$$
\Pr_v(Tv=v)\le2^{-(n-2)/2}.
\tag{14}
$$

Condition on any potential local-update choices and the initial port and sign. Let $T_0,\ldots,T_\ell$ be the formal transformations at the inspected symbols. There are at most $\binom{\ell+1}{2}$ pairs. Formally identical prefixes always have identical finite addresses. A union bound over every other pair gives

$$
\boxed{
b_n(\ell)=\binom{\ell+1}{2}2^{-(n-2)/2}
}
\tag{15}
$$

as an upper bound on the probability of any unexpected finite-address coincidence. Port changes and holds use no address letter, so they only reduce the number of relevant transformations. Self-matching addresses are included in this same estimate.

## 5. The universal annealed prefix law

For each distinct formal transformation visited in a local run, assign an independent fair scenery sign. Reuse that sign whenever the same formal transformation recurs. Multiply it by the common initial $\sigma$ and current port value $\gamma_j$. This defines a universal six-symbol prefix law without choosing a finite width.

In the actual dictionary target, the initial address is uniform and its whole configuration is drawn uniformly. Conditional on the address trajectory, scenery signs at distinct addresses are independent fair signs. Outside the collision event in (15), equality of visited addresses is exactly equality of the formal transformations. The target prefix therefore couples exactly to the universal prefix on that event.

One can reveal dictionary bits only when an address is first visited: before a collision, assign the independent sign of its formal class; after a collision, reuse the previously assigned finite-address bit and reveal unused bits independently. This preserves the true dictionary distribution. No conditioning changes the iid scenery law.

Thus the local prefix law at width $n$ has total-variation distance at most $b_n(\ell)$ from the universal law. For $n\ge n_0\ge4\ell+1$, comparison through that law gives

$$
\boxed{
\operatorname{TV}(\mathsf P_n^{\rm loc},\mathsf P_{n_0}^{\rm loc})
\le\ell(\ell+1)2^{-(n_0-2)/2}.
}
\tag{16}
$$

The port and sign histories are included in this comparison. The proof does not draw a fresh scenery sign on an ordinary repeated address visit.

## 6. Refresh preserves the same collision budget

At full internal clock $(5/2)k$, an update is local with probability $2/5$ and an independent stationary draw with probability $3/5$. Refresh redraws the configuration as well: this section concerns the counted dictionary model, not a fixed frozen-label target.

Condition on common refresh flags in a prefix of $\ell+1$ symbols. Each run starts with a fresh independent address, configuration, port and sign. If its run lengths in symbols are $l_1,\ldots,l_q$, then

$$
\sum_j l_j=\ell+1,\qquad
\sum_j\binom{l_j}{2}\le\binom{\ell+1}{2}.
\tag{17}
$$

Apply the coupling from Section 5 in each run. Summing its pair-collision bounds therefore costs no more than one prefix of full length. The full stationary internal prefix law obeys the same estimate,

$$
\boxed{
\operatorname{TV}(\mathsf P_n^{\rm full},\mathsf P_{n_0}^{\rm full})
\le\ell(\ell+1)2^{-(n_0-2)/2}.
}
\tag{18}
$$

The generic approximate-prefix argument would introduce another factor $\ell+1$. It is unnecessary for this particular error, whose collision count adds over independent refresh runs as in (17).

## 7. Select complete configurations of the finite reference

For a reference width $m$, let $v_x$ be the stationary local-prefix vector of a complete fixed-configuration model on its $6\cdot2^m$ states. It has $6^{\ell+1}$ coordinates, one per actuator word. The annealed reference law is their exact convex average.

Carathéodory's theorem in the probability simplex supplies at most

$$
J\le6^{\ell+1}
\tag{19}
$$

complete configurations and positive weights summing to one that reproduce this local-prefix vector exactly. Keep all their local states and rates, giving every state of a selected configuration its uniform conditional weight times the component weight. This preserves ordinary detailed balance, the local spectral cap and the exact six-level histogram.

Add the same $(3k/2)$ stationary refresh. Conditioning on its flags shows that exact local-prefix matching gives exact full-prefix matching with the reference dictionary. Its internal off-diagonal rates are positive, and its nonzero relaxation rates retain the advertised band. Attach $A$ by (7). The full physical count is

$$
D\le1+6\cdot2^mJ\le1+6^{\ell+2}2^m.
\tag{20}
$$

Every configuration index, port, sign and address is counted. The selected configurations need not be a partition of the original target, particularly when the reference width differs from its width.

## 8. All protocols, all horizons and the polynomial

Use (10). For $n\le n_0$, take reference width $m=n$ and select its configurations; full prefixes match exactly. For $n>n_0$, take $m=n_0$ and use (18). Either choice has the count (11), and the latter has prefix error at most $\delta/(2C_{\mathcal R}A_H)$.

Exact histogram supplies the common entry-tilt normalization. The [bounded-rate approximate-prefix regeneration theorem](BOUNDED_RATE_FINITE_FIELD.md#72-regeneration-with-approximate-prefixes) gives

$$
\sup_{h,t}|m_{F_n}[h](t)-m_{\widehat F}[h](t)|
\le C_{\mathcal R}\left[A_H\operatorname{TV}(\text{prefixes})
 +q^{\ell+1}\right]\le\delta.
\tag{21}
$$

This uses the original physical field rule and a common external reset to $A$ at rate $k/\mathcal R$. It covers the actual mean at every horizon, with no derivative approximation or finite observation cutoff.

For the count, rounding in (10) gives

$$
2^{n_0}\le\max\left\{2^{4\ell+1},
32(C_{\mathcal R}A_H)^2\ell^2(\ell+1)^2\delta^{-2}\right\}.
\tag{22}
$$

The first contribution to (11) is $O(96^\ell)$. The second is

$$
O\!\left(6^\ell\delta^{-2}\log^4(2/\delta)\right).
$$

Their accuracy exponents before absorbing logarithms are $\log96/\beta$ and $2+\log6/\beta$. Since $\mathcal R\ge1$ implies $\beta\le\log(7/5)$,

$$
\frac{\log96}{\beta}-\left(2+\frac{\log6}{\beta}\right)
=\frac{4\log2}{\beta}-2>0.
\tag{23}
$$

This fixed power margin absorbs the fourth power of the logarithm, proving (9). The exponent and constant are sufficient bounds; no optimal exponent, efficient construction algorithm, parameter-precision bound or practical state budget is asserted.

## 9. What the theorem adds to the architecture comparison

Selecting complete configurations of the original register alone gives a factor $2^n$ and would not prove a uniform bound across all widths. The additional step is replacing a wide register by width $n_0=O(\log(1/\delta))$ before selecting configurations. Short affine-dihedral transformations almost never coincide accidentally on a long uniform binary register, so that replacement controls the needed scenery statistics.

Consequently the entire target family has the uniform upper (9). The [aggregation lower bound](AGGREGATION_STATE_LOWER_BOUND.md) addresses the more restrictive architecture obtained by partitioning the original hidden states and using its conditional-expectation generator. Its actual-mean lower bound must be established separately; failure of a stronger reconstruction certificate would not suffice.

The original and replacement models both remain reversible and obey the same physical rate rule and histogram constraints. This theorem does not establish a reversible-versus-irreversible separation. It also does not remove the independent full-dictionary assumption or cover arbitrary frozen scenery. The general cap-only polynomial reversible question remains open.

## 10. Verification and evidence

[The exact verifier](../scripts/verify_register_scenery_compression.py) and [saved report](../reports/register_scenery_compression.json) check finite affine-action identities, collision ranks, short annealed scenery laws, positive whole-configuration selection and the explicit error budgets. These finite algebra checks support the proof above; they do not prove a statement about every width by enumeration or certify publication novelty. See [verification notes](VERIFICATION.md) for the final checked scope and internal audits.
