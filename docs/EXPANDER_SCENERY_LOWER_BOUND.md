# Switching hardness with fixed binary labels on a sparse expander

[Repository overview](../README.md) · [Typical-label reversible upper bound](EXPANDER_SCENERY_COMPRESSION.md) · [Local-walk lower bound and physical endpoints](LOCAL_WALK_LOWER_BOUND.md) · [Fixed-clock transfer](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md)

**Research theorem, 22 September 2026.** Polynomial actual-mean switching hardness survives when the local hidden generator is connected, has bounded degree and has a spectral gap independent of its size. The target is a random walk on one fixed binary labeling of a finite expander, augmented by a two-state sign coordinate and the prescribed stationary refresh. Every hidden coordinate is counted. Its passive visible path law remains exactly two-state.

The proof uses a labeling ensemble only to establish that an appropriate fixed labeling exists. The physical target does not redraw its labeling and does not receive external random scenery. A Walsh projection along a long graph geodesic gives exponentially many controlled directions. Explicit bounds on the global-centering terms and on changes under a single label flip turn this ensemble calculation into a lower bound for one fixed target.

The lower bound holds against arbitrary finite Markov competitors, including irreversible ones. It does not establish an intrinsic reversibility cost. Its intersection with the separately proved typical-label upper event places hard targets inside a class with polynomial reversible compression; the polynomial exponents are not matched. The binary question in the tight target band $[k,3k]$ remains open. The separate [binary reversibility theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) gives an intrinsic cost at a larger fixed budget; the [nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) retains budget $3k$. Neither statement changes this expander subclass comparison.

## 1. A connected local generator and a fixed labeling

Use the original physical model with states $A$ and a finite hidden set, readout $S(A)=-1$, $S(B)=+1$, preparation $\pi_0=(1/2,\mu/2)$, and rates

$$
q_{Ay}(h)=k\mu_y e^{(1+g_y)h},\qquad
q_{yA}(h)=k e^{(g_y-1)h}.
\tag{1}
$$

Fix $s=\sqrt W>0$ and $H>0$. Set $k=1$ until the final clock statement. Let $G$ be a finite connected simple $d$-regular graph, $d\ge3$, with $N$ vertices and normalized adjacency matrix $P$. Assume its second largest eigenvalue is at most $\rho<1$. A possible eigenvalue $-1$ is allowed: bipartiteness does not remove the continuous-time spectral gap.

The hidden states and stationary law are

$$
\mathcal X=V(G)\times\{-1,+1\},\qquad
\mu(v,\sigma)=\frac1{2N}.
\tag{2}
$$

Choose labels $x_v\in\{-1,+1\}$ and keep them fixed in the physical target. Let $J$ flip the sign coordinate and put

$$
g_x(v,\sigma)=s\sigma x_v,\qquad
L=\frac14(P-I)+\frac14(J-I),\qquad
K=L+\frac32(\Pi_\mu-I).
\tag{3}
$$

Here $P$ acts on the graph coordinate and $\Pi_\mu=\mathbf1\mu^T$. For every labeling, the stationary actuator histogram is exactly balanced at $\pm s$; in particular $\mu g_x=0$ and $\mu g_x^2=W$.

The local support of $L$ has degree $d+1$ and is connected. The operators $P$ and $J$ commute, so its relaxation rates are

$$
\frac{1-\lambda(P)}4+\frac{1-\lambda(J)}4.
$$

Every nonzero local rate lies in $[\kappa_0,1]$, where

$$
\kappa_0=\min\{(1-\rho)/4,1/2\}>0.
\tag{4}
$$

The nonzero rates of $K$ therefore lie in $[3/2,5/2]$, and refresh makes all full internal off-diagonal rates positive. The advertised interval remains $[3/2,5/2]$; the construction does not ask a surrogate to preserve a larger lower endpoint that a particular target might have.

Strong lumpability at zero field gives the exact rate-$1$ two-state passive telegraph law. The equilibrium is the usual $\pi_h(A)=e^{-h}/(2\cosh h)$, $\pi_h(v,\sigma)=\mu(v,\sigma)e^h/(2\cosh h)$. Thus the static mean and the common linear and zero quadratic responses remain those of the original family. The total physical state count is $2N+1$.

The graph hypotheses have standard explicit examples. In the primary report version of **Morgenstern's Theorem 4.13 and Corollary 4.14**, take field size $3$ and irreducible polynomials of even degree $m$. This gives connected degree-$4$ graphs with

$$
N=\frac{3^{3m}-3^m}{2}\quad\hbox{or}\quad N=3^{3m}-3^m,
\qquad
\rho\le\frac{\sqrt3}{2},\qquad
\operatorname{girth}(G)>\frac23\log_3 N.
\tag{5}
$$

Either alternative suffices. Consecutive even degrees change the order by a bounded factor. The resulting local sign-layer graph has degree $5$ and gap at least $(2-\sqrt3)/8$. The [primary report](https://www.cs.ubc.ca/sites/default/files/tr/1991/TR-91-11.pdf), printed pages 13–15, contains the theorem, girth proof and infinite-family corollary; the paper was published in *Journal of Combinatorial Theory, Series B* **62** (1994), 44–62. This external graph-existence ingredient is established prior work.

## 2. Controlled vectors and their physical filter

Let $Q_0=Q(0)$ and $Q_*=Q(h_*)$, with

$$
h_* =\min\{H,1/[20(1+s)]\}.
$$

In $L^2(\pi_0)$ define

$$
F=\frac{Q_0(Q_0+2I)}3.
\tag{6}
$$

It annihilates the two-dimensional space of functions constant on each visible block. All blocks touching $A$ vanish. Its hidden block is exactly

$$
F=F_0-\frac5{12}\Pi_\mu,
\qquad
F_0=\frac13L^2-L+\frac5{12}I.
\tag{7}
$$

Indeed, on centered hidden functions $Q_0=L-(5/2)I$; applying (6) gives $F_0$, whose constant eigenvalue is $5/12$. Subtracting the last term in (7) is essential. Averaging a **fixed** labeling over spatial positions does not annihilate all nonempty Walsh characters of the labeling ensemble.

Use unnormalized counting $\ell^1$ and $\ell^\infty$ norms on the $2N$ hidden states. The local exit rate is $1/2$, and $L$ is symmetric. Its two induced norms equal $1$, so

$$
\|F_0\|_{1\to1},\|F_0\|_{\infty\to\infty}\le\frac74,
\qquad
\|F\|_{1\to1},\|F\|_{\infty\to\infty}\le\frac{13}6<3.
\tag{8}
$$

Multiplication $M_x$ by $r_x(v,\sigma)=\sigma x_v$ has both induced norms one. Also

$$
\|\Pi_\mu\|_{1\to\infty}=\frac1{2N}.
\tag{9}
$$

Set $b_*=e^{-h_*}\sinh(sh_*)>0$ and $c_*=1-e^{-h_*}\cosh(sh_*)$. The physical generator letters are

$$
Z_0=F^2,\qquad
Z_1=-b_*^{-1}F(Q_*-Q_0-c_*I)F=FM_xF.
\tag{10}
$$

For $b=(b_1,\ldots,b_n)\in\{0,1\}^n$, write

$$
W_b=Z_{b_n}\cdots Z_{b_1},\qquad v_b=W_bFr_x.
\tag{11}
$$

There are $T=2n+1$ filters and at most $n$ multipliers in each vector. Define $\widetilde v_b$ by replacing every $F$ with $F_0$. Both vectors have $\ell^\infty$ norm at most $3^T$.

## 3. Exact geodesic Walsh coefficients before centering

Assume

$$
\operatorname{girth}(G)>4T=8n+4.
\tag{12}
$$

For every terminal vertex $v$, choose a vertex $u_v$ at distance $2T$ and its unique geodesic

$$
z_0=u_v,z_1,\ldots,z_{2T}=v.
$$

To justify this choice, extend any nonbacktracking path for $2T$ steps. A repeated vertex or a shorter alternative route would give a cycle of length at most $4T$, and two distinct geodesics would do the same. This argument requires unique geodesic routes, not that all edges between boundary vertices of the ball be absent.

Temporarily regard the labels $x_w$ as independent fair bits and expand each coordinate of $\widetilde v_b$ in Walsh characters $\chi_U(x)=\prod_{w\in U}x_w$. Each local filter moves at most two base-graph edges. A multiplier can acquire the bit $x_{u_v}$ only at base vertex $u_v$.

If the last acquisition of that bit is at the $j$th multiplier, $2j$ filters have already acted. The remaining $T-2j$ filters cannot reach the terminal vertex at distance $2T$. Thus a surviving term containing $x_{u_v}$ must obtain it from the initial $r_x$ at $u_v$ and retain it throughout.

To cover distance $2T$ in $T$ filters, every filter must use $L^2/3$ and take two forward base moves along the unique geodesic. Sign flips and diagonal terms cannot contribute to maximal base displacement. Each filter contributes

$$
a_d=\frac1{48d^2}.
$$

At the $j$th multiplier the base position is $z_{4j}$. All these vertices are distinct. Consequently the entire Walsh part of $\widetilde v_b(v,\sigma)$ containing $u_v$ is exactly

$$
c_n\sigma^{1+|b|}\chi_{U_b(v)},\qquad
c_n=a_d^{2n+1},\qquad
U_b(v)=\{z_0\}\cup\{z_{4j}:b_j=1\}.
\tag{13}
$$

The $q_n=2^n$ sets $U_b(v)$ are distinct.

## 4. Every global-centering contribution is controlled

For a function of the labeling, define the divided difference

$$
D_uf(x)=\frac{f(x)-f(x^{(u)})}{2},
$$

where $x^{(u)}$ flips only $x_u$. If $u\in U$, the Walsh coefficient of $f$ indexed by $U$ equals that of $D_uf$, and is bounded in magnitude by $\sup_x|D_uf(x)|$.

Differentiate a word by telescoping over its at most $n$ multiplication letters and its initial $r_x$. At a multiplier, $(M_x-M_{x^{(u)}})/2$ is supported on the two states over $u$ and has entries of absolute value one there. The differentiated $r_x$ is likewise supported on those states and has counting $\ell^1$ norm $2$.

For the initial insertion, telescope the difference between the actual suffix and its all-local version over the $T$ filter sites. Each summand has one explicit factor $-(5/12)\Pi_\mu$. All other filters have either induced norm at most $3$. Apply the counting $\ell^1$ bound before that projection, (9) at the projection, and the $\ell^\infty$ bound afterward. Each summand contributes at most

$$
\frac5{12N}3^{T-1}
\tag{14}
$$

at any terminal coordinate. There are at most $T$ summands.

For differentiation at the $j$th multiplier, the prefix supplies a vector supported on the two states over $u_v$, of counting $\ell^1$ norm at most $2\cdot3^{2j}$. Its all-local suffix contributes zero at $v$, since only $T-2j$ filters remain. Replace the actual suffix by its difference from the all-local suffix and telescope over its filter sites. Each term again has an explicit projection and obeys (14), including the prefix factor; there are at most $T-2j$ such terms. The corresponding all-local differentiated full word is zero for the same range reason, regardless of its prefix.

Adding all insertion sites gives the conservative bound

$$
\left|D_{u_v}(v_b-\widetilde v_b)(v,\sigma)\right|
\le\frac{B_n}{N},\qquad
B_n=(n+1)(2n+1)3^{2n+1}.
\tag{15}
$$

Every selected Walsh coefficient therefore differs from (13) by at most $B_n/N$. This includes coefficients indexed by another word's selected leaf. Equation (15) handles all terms with global centering without treating spatial averaging as averaging over the labeling ensemble.

## 5. A quantitative expected Gram bound

At each terminal $v$ and sign $\sigma$, project the $q_n$ word coordinates onto the $q_n$ characters $U_b(v)$. Their coefficient matrix has the form

$$
c_n\operatorname{diag}(\sigma^{1+|b|})+E(v,\sigma),
\qquad |E_{bc}(v,\sigma)|\le\frac{B_n}{N}.
$$

If

$$
N\ge\frac{2q_nB_n}{c_n},
\tag{16}
$$

its smallest singular value is at least $c_n/2$. Define the physical Gram matrix

$$
\mathcal G_{bc}(x)=\langle v_b(x),v_c(x)\rangle_{\pi_0}
=\frac1{4N}\sum_{v,\sigma}v_b(v,\sigma)v_c(v,\sigma).
$$

Parseval's inequality, followed by averaging over terminal vertices and signs, yields

$$
\boxed{\mathbb E_x\mathcal G(x)\succeq\frac{c_n^2}{8}I.}
\tag{17}
$$

The factor $1/2$ for the total hidden probability under $\pi_0$ is included.

## 6. Concentration selects one fixed labeling

The same insertion telescoping and counting $\ell^1$ bounds give

$$
\|v_b(x)-v_b(x^{(u)})\|_1\le4(n+1)3^{2n+1}.
$$

There are at most $n+1$ insertions; each divided-difference insertion has counting $\ell^1$ norm at most $2\cdot3^{2n+1}$, and undoing the divided difference gives the other factor two. Combining this with the uniform vector bound gives

$$
|\mathcal G_{bc}(x)-\mathcal G_{bc}(x^{(u)})|
\le\frac{A_n}{N},\qquad
A_n=2(n+1)3^{4n+2}.
\tag{18}
$$

The bounded-differences inequality for independent bits and a union bound over $q_n^2$ entries imply

$$
\Pr\!\left(\max_{b,c}|\mathcal G_{bc}-\mathbb E\mathcal G_{bc}|\ge t\right)
\le2q_n^2\exp\!\left(-\frac{2Nt^2}{A_n^2}\right).
$$

Set $t=c_n^2/(16q_n)$. The matrix operator norm is at most $q_n$ times its largest entry magnitude. From (17), with probability at least

$$
1-2q_n^2\exp\!\left(-\frac{Nc_n^4}{128q_n^2A_n^2}\right),
\tag{19}
$$

one fixed labeling obeys

$$
\boxed{\mathcal G(x)\succeq\frac{c_n^2}{16}I.}
\tag{20}
$$

For any requested failure probability $\eta\in(0,1)$, it is enough to combine (16) with

$$
N\ge128q_n^2A_n^2c_n^{-4}\log\frac{2q_n^2}{\eta}.
\tag{21}
$$

For fixed degree, these budgets are exponential in $n$ up to polynomial factors, which can be absorbed into an exponential. Taking (5) sufficiently large also enforces (12), and the bounded ratio between successive graph orders allows $N=e^{O(n)}$. The construction is an existence theorem proved by exact estimates; it does not require large simulations or a computational search for labels.

## 7. Transfer to actual means on any fixed positive clock

The physical endpoint identities in [the local-walk proof, Section 6](LOCAL_WALK_LOWER_BOUND.md#6-the-gram-entries-are-accessible-through-the-visible-mean) use only the original field rule, balanced binary sensitivity and the filter (6). They apply unchanged. With

$$
\ell_*=2\sinh(h_*)\sinh(sh_*),\qquad
r_*=-2e^{-h_*}\sinh(sh_*),
$$

the side polynomials

$$
\mathcal L_b=\ell_*^{-1}Q_*FW_b^{\rm rev},\qquad
\mathcal R_b=r_*^{-1}W_bFQ_*
$$

satisfy $\pi_0\mathcal L_b\mathcal R_cS=\mathcal G_{bc}$. Here reversal gives the adjoint in the target. Each side has generator degree at most $5n+3$ and coefficient sum at most $C_*^{n+1}$, with the same dimension-independent $C_*$ as that proof.

Fix a clock $a>0$. The target spectra and norm comparisons obey the same bounds used in [Section 7 of the local-walk proof](LOCAL_WALK_LOWER_BOUND.md#7-transfer-to-a-fixed-positive-experimental-clock). In particular the common spectral interval is contained in $[-5,0]$. Use its constants $\varrho>1$, $B_a,A_a$ and truncate each complete side logarithm series at total degree $M$. The resulting matrix error is at most

$$
3q_nB_a^{2n+2}\varrho^{-(M+1)}.
$$

Choose

$$
\varrho^{M+1}\ge96q_nB_a^{2n+2}c_n^{-2}.
\tag{22}
$$

Then $M=O_{a,d}(n+1)$ and the truncated matrix has smallest singular value at least $c_n^2/32$. Each side is a finite propagator polynomial with coefficient sum at most $J_n=4^MA_a^{n+1}$.

For a competitor with $D$ physical states, evaluating these same finite propagator polynomials using its own actual propagators produces a matrix of rank at most $D$. No competitor generator is expanded or logarithmically transformed. If its actual-mean error on the legal experiment menu is at most $\delta$ and $D<q_n$, rank and singular-value perturbation force

$$
\boxed{
\delta\ge\frac{c_n^2}{32q_nJ_n^2}
\ge e^{-C_{a,d}(n+1)}.
}
\tag{23}
$$

Only fields $0,h_*$ occur. Restoring $k$, every positive-duration segment is an integer multiple of $a/k$ and the witnessing horizons are $O_{a,d}(n/k)$. Competitors need only a fixed preparation, fixed real readout and finite Markov state space; they need not be reversible, analytic in the field, rate bounded, passively exact or members of (1).

Therefore the worst-case state cost in this connected-expander subclass satisfies

$$
D_*(\delta)\ge c_a\delta^{-\gamma_a}
\tag{24}
$$

for positive constants depending only on the fixed parameters and sufficiently small $\delta$.

## 8. Intersection with an all-accuracy upper event

Fix each base graph before selecting labels. The [companion upper theorem](EXPANDER_SCENERY_COMPRESSION.md) defines an event $\mathcal E_G=\mathcal E_{G,1/4}$ using stationary local color-prefix probabilities $f_w(x)$ at the local uniformization clock, $P_{\rm loc}=I+L=\tfrac12I+\tfrac14P+\tfrac14J$. With $\eta=1/4$, it requires simultaneously for every $\ell\ge1$ and every binary word $w$ of length $\ell+1$ that

$$
|f_w(x)-\mathbb E_xf_w(x)|
\le(\ell+1)\sqrt{\frac{B_\ell}{2N}},\qquad
B_\ell=(\ell+2)\log2+2\log(\ell+1)+\log4.
\tag{25}
$$

That theorem proves $\Pr(\mathcal E_G)>3/4$ by summing the depth-dependent failure budgets. This is one event independent of the requested accuracy, and it guarantees polynomial reversible prediction at all accuracies for each selected target on the specified logarithmic-girth graph class.

Choose $\eta=1/4$ in (21). The lower event has probability at least $3/4$, so its intersection with $\mathcal E_G$ has probability greater than $1/2$. For each depth $n$, select a sufficiently large graph from (5) and one labeling in this intersection. These targets belong to the same all-accuracy upper class and satisfy (23).

Let $\mathcal F_{\rm good}$ consist of the targets (3) on the fixed family (5), with labels restricted to $\mathcal E_G$. Its unrestricted and original-field-rule reversible switching costs satisfy

$$
c_a\delta^{-\gamma_a}
\le D_*^{\rm good}(\delta)
\le D_{\rm rev}^{\rm good}(\delta)
\le C\delta^{-p}
\tag{26}
$$

for positive fixed constants and sufficiently small $\delta$. For the family (5), the companion theorem supplies the explicit sufficient exponent

$$
p=\frac{\log2+8\log3}{\log(1+2/(5R_s))},\qquad R_s=e^{(1+s)H}.
$$

The upper preserves the exact binary actuator histogram and the advertised interval $[3k/2,5k/2]$; it need not preserve the target's graph or its larger actual gap. The polynomial exponents are unmatched. Equation (26) concerns the stated typical-label class, not every possible fixed labeling of an expander.

The common analytic constant-step upper theorem gives $O(\log(1/\delta))$ on this class. A matching logarithmic step lower has not been established here, and an original-field-rule logarithmic step upper is not asserted.

## 9. Why the earlier sufficient conditions fail

The local spectral gap gives a direct obstruction to bounded-size low-cost fragmentation. For any edge-deletion partition with component sizes at most $S$, the [Poincare estimate](SPARSE_REVERSIBLE_COMPRESSION.md#10-a-precise-limitation-of-stationary-flux-fragmentation) yields directed stationary removed flux at least

$$
\Phi\ge\kappa_0\left(1-\frac{S}{2N}\right).
\tag{27}
$$

Thus a fixed flux error below $\kappa_0$ requires component sizes proportional to the target size.

The density-moment hypothesis also fails uniformly. With stationary weights $1/(2N)$ and a fixed positive local neighbor rate, the transition density $K_{ij}/\mu_j$ on those neighbors is proportional to $N$. There are $\Theta(N)$ such directed pairs, each of stationary pair mass $1/(4N^2)$. For every $\alpha>0$, their contribution to the global $(1+\alpha)$-moment is $\Theta(N^\alpha)$.

These calculations show that two earlier upper-bound hypotheses do not explain this class. They are not additional actual-mean lower bounds, and do not rule out another reversible compression construction.

## 10. Scope and evidence

The proof was independently checked internally for the global-centering coefficient bound, expected physical Gram normalization, single-label sensitivity, concentration constants, physical endpoint identities and fixed-clock transfer. The [exact verifier](../scripts/verify_expander_scenery_lower_bound.py) and [saved report](../reports/expander_scenery_lower_bound.json) supplement those arguments. They check physical generators with at most 11 states; sparse Walsh coefficients on cycles of 13 and 21 vertices, including nonzero centering leakage; exhaustive label-flip and Parseval identities for the 16 labelings of $K_4$; and exact all-depth probability and fixed-clock budgets. The cycle calculations verify geodesic algebra and do not represent a uniformly expanding graph family.

At the rational calibration $s=1$, $H=h=\log(65/64)$ and clock $a=1/8$, the verifier certifies the sufficient size budget $N\ge2^{192(n+1)}$, cutoff $M=300(n+1)$ and actual-mean error floor $2^{-1295n-1279}$ for rivals with fewer than $2^n$ states, conditional on the stated graph hypotheses. These deliberately loose bounds are checked by exact induction ratios; no graph of that enormous order is constructed. A separate graph-existence theorem supplies appropriate graphs. Finite checks do not prove that theorem or validate publication novelty.

High-girth expanders, random labels, Walsh expansions, bounded differences and finite-rank realization are established ingredients. The candidate contribution is their combination in a physical prediction problem with a fixed binary actuator, exactly two-state passive output, finite-clock actual-mean hardness, and connected uniformly mixing sparse local dynamics. The [prior-art assessment](PRIOR_ART.md) records the external ingredients and limits of the novelty assessment.
