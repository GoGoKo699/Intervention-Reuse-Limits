# An intrinsic reversible state cost with a binary actuator

[Nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Bounded-rate upper bounds](BOUNDED_RATE_FINITE_FIELD.md) · [Fixed-clock scalar transfer](REVERSIBLE_WORD_OBSERVABILITY.md) · [Positive transport repair](POSITIVE_TRANSPORT_REPAIR.md) · [Verifier](../scripts/verify_binary_reversibility_lower_bound.py) · [Report](../reports/binary_reversibility_lower_bound.json)

**Research theorem, 22 September 2026.** A fixed, balanced binary actuator suffices for an exponential-versus-polynomial state-complexity separation between ordinary reversible and unrestricted Markov prediction. Both predictor classes obey the same internal exit-rate budget and the original field rule. The lower bound applies to arbitrary new reversible state spaces and actual controlled means at every fixed positive control clock.

The binary encoding uses a larger fixed rate-to-gap ratio than the earlier nineteen-level construction. The numerical constants below are convenient explicit bounds, not optimized constants. The binary problem with the earlier target band $[k,3k]$, and the problem without a reversible rival rate cap, remain open.

## 1. The theorem and the comparison

Fix $H,k>0$ and $0<\gamma<1$. Put

$$
\mathcal B=6580,\qquad R_H=e^{(1+\gamma)H},\qquad
p=\frac{\log2}{\log(1+1/(\mathcal B R_H))}.
\tag{1}
$$

There is a family of finite reversible targets indexed by $n\ge1$, with $r=2^n$, having

$$
\begin{gathered}
N_n=224r2^r+4\quad\text{total physical states},\\
\Pr_\mu(g=+\gamma)=\Pr_\mu(g=-\gamma)=\tfrac12,\\
\mu g=0,\qquad \mu g^2=\gamma^2,\\
-K_{ii}=\mathcal B k,\qquad
\operatorname{spec}(-K)\setminus\{0\}\subset[k,2\mathcal B k].
\end{gathered}
\tag{2}
$$

Each target has one visible state $A$, hidden stationary law $\mu$, and the original external rule

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h}.
\tag{3}
$$

The preparation is $\pi_0=(1/2,\mu/2)$ and the readout is $S(A)=-1$, $S(z)=+1$. Its passive visible path law is exactly the rate-$k$ two-state telegraph law. At fixed field the target is reversible with

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h}.
\tag{4}
$$

Let $D_{\rm all}(\delta)$ be the worst-case minimal total predictor state count over this family, with uniform absolute error at most $\delta$ in the actual mean over all bounded deterministic piecewise-continuous protocols and all observation times. Rivals have one visible state, a finite stationary hidden model, the same balanced binary histogram, rule (3), preparation, readout, and hidden exits at most $\mathcal B k$. Their hidden dynamics may be nonreversible. Define $D_{\rm rev}(\delta)$ by additionally requiring ordinary hidden reversibility. All retained states are counted; rivals need not be target partitions or retain any target coordinates.

For sufficiently small $\delta$, fixed positive constants give

$$
\boxed{
\begin{aligned}
c_0\delta^{-\zeta}&\le D_{\rm all}(\delta)\le C_0\delta^{-p},\\
\exp(c_1\delta^{-\alpha})&\le D_{\rm rev}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log\frac2\delta\right).
\end{aligned}}
\tag{5}
$$

The exponents are not matched. Both lower bounds already hold on five fixed field values when every positive segment duration is an integer multiple of any fixed $a/k>0$. Witnessing horizons are $O_a(\log(1/\delta)/k)$. Upper bounds apply to the full protocol class. Neither rival class is required to preserve a lower spectral gap. The reversible upper construction does preserve the target band in (2).

The proof proceeds through positive binary observation words. Their target action identifies logical roots, but their action in a rival need not be a coordinate projector. A positive vector derived from the rival's own word operator supplies the probability law used in the entropy lower bound. This is the distinction that permits a binary alphabet without assuming hidden port labels in the rival.

## 2. A binary graph with uniformly mixing lamp dynamics

Set $k=1$ until the final time rescaling. A logical root is

$$
y=(x,b,\sigma),\quad
b\in\{0,1\}^{\mathbb Z_n},\quad
x\in\{-1,+1\}^{r},\quad \sigma\in\{-1,+1\}.
$$

There are $M=2r2^r$ roots. Their binary graph color is $0$. The four involutions are the address reflections $J:i\mapsto-i-1$ and $V:i\mapsto-i$, the first-coordinate address flip $X$, and the lamp flip

$$
F(x,b,\sigma)=(x^{(b)},b,\sigma),
\tag{6}
$$

where $x^{(b)}$ flips exactly entry $b$. The first three leave $x,\sigma$ unchanged.

For an odd edge length $\ell\equiv1\pmod4$, define the vertex color word

$$
c(\ell)=(0011)^{(\ell-1)/4}00.
\tag{7}
$$

It has $\ell+1$ vertices, is palindromic, and satisfies $c_{i+2}\ne c_i$ wherever both sides occur. A walk matching this word cannot immediately backtrack.

Assign lengths $5,9,13,17$ to $J,V,X,F$. For every root $y$ and every gate $g$, create a separate corridor of that length from $y$ to $gy$, with colors (7). These are undirected corridors indexed by oriented copies. A nonfixed pair $y,gy$ receives two different corridors; a fixed point receives one odd cycle. In either case each gate contributes exactly two edges incident to every root and $\ell_g-1$ internal vertices per root. All corridor internal vertices are new.

Each root also has two private probe cycles of lengths $21$ and $25$. Their active code is (7). Obtain the inactive code by swapping the pair of positions $2,\ell-2$, both colored $1$, with positions $4,\ell-4$, both colored $0$. Positions are numbered from $0$. This changes the code, preserves its palindrome and color counts, and keeps both neighbors of the root colored $0$. When $\sigma x_b=+1$, the $21$-cycle is active and the $25$-cycle inactive; when $\sigma x_b=-1$, the opposite holds. Both cycles always exist.

Attach to every root a private marker path of $27$ edges with vertex word $(0011)^7$. Its far tip is a leaf. Add a common color-$0$ hub $o$ and a unit-weight edge from every root to $o$. Finally add vertices $u,v$ of color $1$, with edges $o$--$u$ of weight $M$ and $u$--$v$ of weight $7M$. Every other edge has weight one. There are no self-loops in this weighted graph.

Every root has weighted degree $14$: eight gate incidences, four probe incidences, one marker edge, and one hub edge. **Every neighbor of a root has color $0$.** All other private nonleaf vertices have degree $2$, and marker tips have degree $1$. The hub and ballast have degrees $2M,8M,7M$.

Let

$$
P_{ij}=\frac{w_{ij}}{d_i},\qquad
\mu_i=\frac{d_i}{\sum_jd_j},\qquad
K=\mathcal B(P-I).
\tag{8}
$$

Then $P$ is a stochastic reversible matrix with zero diagonal. Thus every hidden exit of $K$ equals $\mathcal B$. Its zero diagonal is a property of the target construction, not a restriction on rivals.

### Counts, histogram and gap

Per root, gate corridors contribute $4+8+12+16=40$ internal vertices, probes contribute $20+24=44$, and the marker contributes $27$. There are $112M+3$ hidden states, including the hub and ballast. Adding $A$ gives $112M+4=224r2^r+4$ physical states.

Every gate and probe has equally many internal vertices of each color, all of degree two. Inactive probes preserve these counts. Marker internal degree volume is $26$ at color $0$ and $27$ at color $1$. Before ballast, roots and the original hub-star therefore produce color-$0$ minus color-$1$ degree volume $14M$. The edge $o$--$u$ is balance-neutral, while $u$--$v$ adds $14M$ color-$1$ degree. Total degree is $252M$, each color has degree $126M$, and the root set $\mathcal R$ has

$$
\mu(\mathcal R)=\frac{14M}{252M}=\frac1{18}=:m.
\tag{9}
$$

Set $g=-\gamma$ on color $0$ and $g=+\gamma$ on color $1$. This proves the fixed balanced histogram and moments in (2), independently of $n$ and of the current table bits.

For the gap, assign every private vertex to a nearest root; the two halves of paired corridors contribute equal volumes. Each root basin has degree volume

$$
14+2(40+44+26)+1=235.
$$

Route every vertex through its assigned root to the hub, and route $u,v$ along their ballast path. Every path has length at most $28$. An ordinary edge carries degree-weighted path load at most $235$. The load-to-conductance ratios on $o$--$u$ and $u$--$v$ are $15$ and $1$. Cauchy--Schwarz along paths gives

$$
\begin{aligned}
\operatorname{Var}_\mu f
&\le\sum_i\mu_i(f_i-f_o)^2\\
&\le28\cdot235\,\mathcal E_P(f,f),\qquad
\mathcal E_P(f,f)=\frac1{252M}\sum_{\{i,j\}}w_{ij}(f_i-f_j)^2.
\end{aligned}
\tag{10}
$$

Thus the gap of $I-P$ is at least $1/6580$. Its cap is at most $2$ since $P$ is a reversible stochastic matrix. Equations (8) and (10) prove the band $[1,13160]$ and the exit budget in (2). The graph is connected through the common hub.

## 3. Positive binary words expose the target gates

Let $D_0,D_1$ be the hidden color projectors. For a color word $c=(c_0,\ldots,c_\ell)$ write

$$
W[c]=D_{c_0}P D_{c_1}P\cdots P D_{c_\ell}.
\tag{11}
$$

Every such word is entrywise nonnegative in any allowed rival, because its uniformization $P=I+K/\mathcal B$ is stochastic under the common exit budget. Reversing the word gives its stationary adjoint. These words need not be positive semidefinite; the proof uses entrywise positivity.

Let $T=W[(0011)^7]$. Every contributing target walk is nonbacktracking. It cannot pass through a root, because the two neighboring colors around an intermediate root would both be $0$, contrary to $c_{i+2}\ne c_i$. All nonmarker corridors have at most $25$ edges. The hub/ballast can only supply the short periodic trail root-$0$, hub-$0$, $u$-$1$, $v$-$1$, which cannot continue. Consequently a matching $27$-edge walk is exactly a root-to-own-marker-tip walk. It cannot start at another location: a marker interior has too little path remaining in either direction, the reverse marker starts at a color-$1$ tip, and all other branches are too short.

The forward marker probability is $14^{-1}2^{-26}$ and the reverse probability is $2^{-26}$. Therefore

$$
TT^*=p_*D_{\mathcal R},\qquad
p_*:=14^{-1}2^{-52},\qquad
A_*:=TT^*/p_*=D_{\mathcal R}\quad\text{in the target}.
\tag{12}
$$

In an arbitrary rival $A_*$ remains entrywise nonnegative and selfadjoint; it need not be a coordinate projector.

Put $W_\ell=W[c(\ell)]$ and

$$
\kappa_\ell=\frac2{14\,2^{\ell-1}},\qquad
T_g=\frac{A_*W_{\ell_g}A_*}{\kappa_{\ell_g}},\qquad
R_+=\frac{A_*W_{21}A_*}{\kappa_{21}},\qquad
R_-=\frac{A_*W_{25}A_*}{\kappa_{25}}.
\tag{13}
$$

A root-to-root walk matching (7) cannot backtrack or meet an intermediate root. Shorter corridors hit a root too early; longer corridors end outside $\mathcal R$ and are killed by the final projector in the target. The hub/ballast trail stops before length five. Thus $T_g$ acts exactly as $g$ on target root functions and is zero off the roots. This includes fixed points: a single cycle has two matching orientations, giving the same factor $\kappa_\ell$ as two parallel corridors.

A probe contributes only when its entire active code matches. Its inactive code cannot match in reverse either, because the accepted code is palindromic. The separate normalizations in (13) give the target identities

$$
(R_++R_-)1=1_{\mathcal R},\qquad
(R_+-R_-)1=\sigma x_b1_{\mathcal R}.
\tag{14}
$$

All operators in (12)--(13) are fixed positive multiples of positive binary words or products of such words. They are positive in every rival. Their degrees and coefficient masses as polynomials in $P,D_0,D_1$ are absolute constants. Their $L^2(\mu)$ operator norms are bounded by an absolute constant $C_*$: each unnormalized word is a contraction, $\|A_*\|\le p_*^{-1}$, and $\|T_g\|,\|R_\pm\|\le p_*^{-2}/\min_{\ell\le25}\kappa_\ell$. No bound here depends on $n$, the rival dimension, or its smallest stationary mass.

## 4. The actual-mean scalar interface

Work in dimensionless time. For sensitivity $\eta\in\{-\gamma,+\gamma\}$, let $X_\eta$ contain the visible-to-hidden edges of that level and their visible diagonal, and let $Y_\eta$ contain hidden-to-visible entries $1$ and hidden diagonals $-1$ on that level. If $K_b$ denotes the hidden-only extension of $K$, then

$$
Q(h)=K_b+\sum_{\eta=\pm\gamma}e^{(1+\eta)h}X_\eta
                +\sum_{\eta=\pm\gamma}e^{(\eta-1)h}Y_\eta.
\tag{15}
$$

Choose

$$
\bar h=\min\{H,1/[20(1+\gamma)]\},\qquad h_j=j\bar h/4,
\quad j=0,\ldots,4.
\tag{16}
$$

The five frequencies $0,1\pm\gamma,-1\pm\gamma$ are distinct. Their exponential evaluation matrix is a Vandermonde matrix in five distinct positive numbers. Hence $K_b,Y_{+\gamma},Y_{-\gamma}$ are fixed linear combinations of the five physical generators, with coefficients independent of $n$ and identical in every allowed rival.

Write $B_0=Y_{+\gamma}+Y_{-\gamma}$. On the invariant subspace of functions vanishing at the visible state,

$$
I_{\rm hid}=-B_0,\quad D_1=-Y_{+\gamma},\quad D_0=-Y_{-\gamma},
\quad P=-B_0+K_b/\mathcal B.
\tag{17}
$$

These are identities on that subspace; the full matrices $-Y_\eta$ are not asserted to be projectors on arbitrary full functions. We also have

$$
B_0S=-2\,1_{\rm hid},\qquad
\pi_0B_0=(1/2,-\mu/2).
$$

Consequently every hidden word polynomial $V$ satisfies the exact physical identity

$$
\boxed{\mu V1=\pi_0 B_0 V B_0 S.}
\tag{18}
$$

It uses the actual preparation and readout. Inner products of hidden polynomial vectors follow by reversing words: $\langle U1,V1\rangle_\mu=\mu U^*V1$. There is no extra hidden preparation, coordinatewise multiplication operation, or adjoint control.

### Fixed-clock quantitative transfer

A reversible rival with exits at most $\mathcal B$ has hidden spectral cap $2\mathcal B$. Both models' full constant-field spectra in the menu (16) lie in $[-L_*,0]$, where one may take

$$
L_*=2\bigl(2\mathcal B+e^{(1+\gamma)\bar h}\bigr).
$$

At a fixed clock $a>0$, put

$$
\begin{gathered}
\chi=e^{\bar h},\quad q=1-e^{-aL_*},\quad \rho=(1+q)/2,
\quad t=q/\rho,\\
Z_*=(\chi/a)\log\frac1{1-\rho},\quad D_*=8/\rho,
\quad \theta=\frac{\log(1/t)}{\log(D_*/t)}>0.
\end{gathered}
\tag{19}
$$

For $E_h=e^{aQ_h}$ and $U_h=I-E_h$, equilibrium norm equivalence gives
$\|U_h^j\|_{\pi_0}\le\chi q^j$, and

$$
Q_h=-\frac1a\sum_{j\ge1}\frac{U_h^j}{j}.
$$

For a word of $d$ generators, grading this product by total $U$-degree gives a tail above degree $M$ bounded by $Z_*^d t^{M+1}$ in either model. Charge $\chi$ once per logarithm block. A product of $j$ factors $U_h$ expands into legal propagator words with coefficient mass at most $2^j$. Choosing $M=\lfloor\log(1/\delta)/\log(D_*/t)\rfloor$ proves

$$
|\pi_0p(Q)S-\widehat\pi_0p(\widehat Q)\widehat S|
\le4J\max\{1,Z_*\}^{d}\delta^\theta
\tag{20}
$$

for any polynomial of degree at most $d$ and coefficient mass $J$, when all measured means differ by at most $\delta$. Retained experiments have at most $M$ clock steps. This is the direct finite-horizon argument of the [scalar-transfer note](REVERSIBLE_WORD_OBSERVABILITY.md).

Combining (17)--(20), every hidden scalar below with $O(n)$ fixed gadget factors has discrepancy at most

$$
\Delta_n=A_0^{n+1}\delta^\theta
\tag{21}
$$

for a fixed $A_0\ge1$. A finite number of families of scalar expressions is involved; their word lengths and log coefficient masses are all $O(n)$. The number of separately chosen addresses does not multiply (21).

## 5. Repair under an operator norm bound

The following lemma replaces the pointwise row bound used in the nineteen-level proof. It is needed because the positive change of measure below can produce small denominators.

**Lemma.** Let $\nu$ be a probability law and $T$ a nonnegative kernel with

$$
\|T\|_{2\to2}\le C,\quad C\ge1,\qquad
\|T1-1\|_2\le\varepsilon,\qquad
\|T^*1-1\|_2\le\varepsilon.
\tag{22}
$$

There is a kernel $U$ on the same states such that $U$ and $U^*$ are stochastic, and for every $|f|\le1$ and every $g\in L^2(\nu)$,

$$
|\langle f,(T-U)g\rangle_\nu|
\le(2C+3)\varepsilon\|g\|_2.
\tag{23}
$$

Construct the pair consistently under adjoints. Put $r=T1$, $s=T^*1$, and

$$
a_i=\min\{1,1/r_i\},\quad b_i=\min\{1,1/s_i\},\quad
T_0=\operatorname{diag}(a)T\operatorname{diag}(b),
$$

with the value one at zero denominators. Both $T_01$ and $T_0^*1$ are at most one. Set

$$
d=1-T_01,\qquad e=1-T_0^*1,\qquad
\tau=\nu d=\nu e.
$$

If $\tau>0$, let $Uf=T_0f+d\langle e,f\rangle_\nu/\tau$; otherwise let $U=T_0$. The added term fills both marginal deficits, so $U,U^*$ are stochastic.

To prove the bound, $\|1-a\|_2\le\varepsilon$. For $|f|\le1$, positivity gives $|T^*af|\le s$ and $(1-b)s=(s-1)_+$. Expanding

$$
T-T_0=(I-\operatorname{diag}(a))T
       +\operatorname{diag}(a)T(I-\operatorname{diag}(b))
$$

therefore bounds its scalar contribution by $(C+1)\varepsilon\|g\|_2$. Also

$$
e=(1-s)+(1-b)s+bT^*(1-a),
$$

so $\|e\|_2\le(C+2)\varepsilon$. The fill term is at most $\|e\|_2\|g\|_2$, because $|\langle f,d\rangle|\le\tau$. This proves (23). If $T$ is selfadjoint the construction gives selfadjoint $U$.

For a length-$L$ sequence satisfying (22) with common constants, repaired prefixes and raw suffixes give

$$
\left|\left\langle f,
(T_1\cdots T_L-U_1\cdots U_L)g\right\rangle_\nu\right|
\le L(2C+3)C^{L-1}\varepsilon
\tag{24}
$$

whenever $|f|,|g|\le1$. In each telescoping term the adjoint of the repaired prefix preserves the pointwise bound on $f$, while the raw suffix has $L^2$ norm at most the corresponding power of $C$. No pointwise bound on the raw row sums, no fourth moment, and no new states are needed.

The clip-and-fill construction is an established transport-rounding architecture; compare Altschuler, Weed and Rigollet (2017), Algorithm 2 and Lemma 7, as recorded in the [primary-source audit](PRIOR_ART.md). The estimate proved here is the particular $L^\infty$--$L^2$ scalar bound needed for the subsequent word products.

## 6. A probability law on the rival's own states

In this section $A_*,T_g,R_\pm,\mu$ denote rival objects obtained from the same polynomials. Define

$$
u=A_*1\ge0,\quad v=(R_+-R_-)1,\quad
w=(R_++R_-)1\ge|v|,\quad Z=\|u\|_\mu^2.
\tag{25}
$$

If $u_i=0$, the nonnegative row $i$ of $A_*$ is zero; selfadjointness gives a zero column as well. The outer $A_*$ factors in (13) therefore make every $T_g,R_\pm$ zero on rows and columns outside $\mathcal S=\{u>0\}$. In particular $v$ is supported on $\mathcal S$.

In the target, $u=1_{\mathcal R}$, $Z=m=1/18$, $w=u$, and

$$
T_gu=T_g^*u=u,\qquad \|v\|_\mu^2=Z.
\tag{26}
$$

The squared norms of the differences in (26), and $\|w-u\|^2$, are hidden polynomial scalars with target value zero. Equation (21) therefore controls them in the rival. For all sufficiently small $\delta$, $Z\ge m/2$. Define on $\mathcal S$

$$
\nu_i=\frac{\mu_i u_i^2}{Z},\qquad
B_g(i,j)=\frac{T_g(i,j)u_j}{u_i}.
\tag{27}
$$

This change of measure adds no state. Conjugation by $\operatorname{diag}(u)$ gives the exact identities

$$
\begin{aligned}
\|B_g\|_{L^2(\nu)\to L^2(\nu)}&\le C_*,\\
\|B_g1-1\|_{L^2(\nu)}
&=\frac{\|T_gu-u\|_{L^2(\mu)}}{\sqrt Z},\\
\|B_g^*1-1\|_{L^2(\nu)}
&=\frac{\|T_g^*u-u\|_{L^2(\mu)}}{\sqrt Z}.
\end{aligned}
\tag{28}
$$

There is no loss involving $\min u_i$: the square in the probability (27) cancels the denominator. Zero coordinates were already removed by the outer factors. In particular all defects in (28) are at most $C_2\delta^{\theta/2}$ for a fixed $C_2$, by constant-degree instances of (21).

The positive conjugation and the squared stationary weight are the familiar reversible $h$-transform mechanism; compare Chetrite and Touchette (2015) in the [primary-source audit](PRIOR_ART.md). Here approximate eigenvector identities inferred from actual means are followed by the explicit repair of Section 5.

Apply Section 5 to obtain stationary Markov kernels $U_g$ on $(\mathcal S,\nu)$, consistently under adjoints. These are proof operators on the rival's own states, not additional physical controls or a claimed surrogate generator.

Put

$$
h=\operatorname{clip}(v/u,-1,1).
\tag{29}
$$

Since $|v|\le w$,

$$
\|h-v/u\|_{L^2(\nu)}
\le\frac{\|w-u\|_{L^2(\mu)}}{\sqrt Z}
\le C_3\delta^{\theta/2}.
\tag{30}
$$

Also $\|v/u\|_\nu^2=\|v\|_\mu^2/Z=1+O(\delta^\theta)$, so $\|h\|_\nu^2\ge1-O(\delta^{\theta/2})$. Both constants are independent of dimension and minimum stationary mass.

Every product of raw $B_g$ is exactly conjugate to the corresponding product of $T_g$, with no omitted excursions. For example, writing $h^{\rm raw}=v/u$,

$$
\langle h^{\rm raw},B_{g_1}\cdots B_{g_L}h^{\rm raw}\rangle_\nu
=Z^{-1}\langle v,T_{g_1}\cdots T_{g_L}v\rangle_\mu.
\tag{31}
$$

Thus all raw query moments remain physical scalars through (18). Replacing $h^{\rm raw}$ by $h$ costs at most $C_4 C_*^L\delta^{\theta/2}$: use (30), the operator bound, and the bounded $L^2$ norm of $h^{\rm raw}$. Replacing raw gates by repaired ones then costs at most (24), with endpoints bounded by one. These two replacements are kept separate; (24) is not applied to an unbounded endpoint.

## 7. All addressed lamp flips force high entropy

The address reflections generate cyclic rotation. For any $c\in\{0,1\}^{\mathbb Z_n}$, a word of at most $n$ rotations and $n$ first-bit flips implements pure XOR translation. Hence there is a product $W_c$ of at most $3n$ target gates such that

$$
(W_cf)(x,b,\sigma)=f(x,b\oplus c,\sigma).
\tag{32}
$$

Its reversed word is its adjoint, with the same target action. On target roots let

$$
f_c=W_cv=\sigma x_{b\oplus c},\qquad
C_c=W_cT_FW_c^*.
$$

Then $C_cf_b=(-1)^{\mathbf1_{b=c}}f_b$, and

$$
\|W_bv\|_\mu^2=m,\qquad
\langle W_bv,W_cT_FW_c^*W_bv\rangle_\mu
=(-1)^{\mathbf1_{b=c}}m.
\tag{33}
$$

These words have $O(n)$ gadget factors. Define $\widehat W_c$ using the repaired rival gates, set $h_c=\widehat W_ch$, and put $\widehat C_c=\widehat W_cU_F\widehat W_c^*$. They are stationary Markov operators on $\nu$, and $|h_c|\le1$.

Equations (21), (24), and (30)--(33) yield fixed $A_1\ge1$ such that

$$
\begin{gathered}
\mathbb E_\nu h_b^2\ge1-\eta_n,\\
(-1)^{\mathbf1_{b=c}}\langle h_b,\widehat C_ch_b\rangle_\nu
\ge1-\eta_n,\\
\eta_n\le A_1^{n+1}\delta^{\theta/2}.
\end{gathered}
\tag{34}
$$

To detail the dependence: (33) contributes $A_0^{n+1}\delta^\theta$; normalizing by $Z\ge m/2$ costs only a fixed constant; endpoint clipping contributes a constant to power $O(n)$ times $\delta^{\theta/2}$; each repaired concatenated word has length $O(n)$ and costs at most its length times $C_*^{O(n)}\delta^{\theta/2}$. A fixed enlargement of $A_1$ absorbs all these terms. No factor depending on the number of queried addresses is included until the explicit union bound below.

For an explicit bound, enlarge $\Delta_n$ to cover every scalar used and suppose $\Delta_n\le m/2$, as holds on the inverse-error scale below. Then $\|v/u\|_\nu\le\sqrt3$, and every row defect and clipping error is at most $\sqrt{2\Delta_n/m}$. The longest concatenated scalar word has at most $L=12n+1$ gates. One may take

$$
\eta_n\le\frac{4\Delta_n}{m}
+\left[\sqrt3+1+L(2C_*+3)\right]C_*^L
\sqrt{\frac{2\Delta_n}{m}}.
\tag{34a}
$$

Since $L=O(n)$ and $\Delta_n=A_0^{n+1}\delta^\theta$, this implies the last line of (34). Choosing the inverse-error constant large enough also ensures $\Delta_n\le m/2$.

Decode a deterministic vector on the rival's states by $Z_b=\operatorname{sign}(h_b)$, with sign zero chosen as $+1$. Since $|h_b|\le1$,

$$
\mathbb E_\nu|Z_b-h_b|\le1-\mathbb E_\nu h_b^2\le\eta_n.
$$

Under a stationary coupling $(I,J)$ with transition kernel $\widehat C_c$, (34) gives

$$
\Pr\{Z_b(J)\ne(-1)^{\mathbf1_{b=c}}Z_b(I)\}\le\tfrac32\eta_n.
$$

Let $\rho$ be the law of the entire decoded vector $Z=(Z_b)_b$. A union bound over its $r$ coordinates gives

$$
\|\rho-\operatorname{flip}_c\rho\|_{\rm TV}\le\tfrac32 r\eta_n
\quad\text{for every }c.
\tag{35}
$$

For a binary distribution, $h_2(p)\ge1-|2p-1|$. Conditioning on all coordinates except $c$ therefore gives

$$
H(Z_c\mid Z_{-c})\ge1-\|\rho-\operatorname{flip}_c\rho\|_{\rm TV}.
$$

The entropy chain rule now implies

$$
H(Z)\ge\sum_cH(Z_c\mid Z_{-c})
\ge r(1-3r\eta_n/2).
\tag{36}
$$

The decoded vector is a deterministic function of one of the actual rival states in $\mathcal S$. Consequently

$$
\eta_n\le\frac1{6r}\quad\Longrightarrow\quad
\log_2 D_{\rm rival}\ge H(Z)\ge\frac34r.
\tag{37}
$$

Choose a fixed $C_5$ sufficiently large that $\delta_n=e^{-C_5(n+1)}$ makes (34) at most $1/(6\cdot2^n)$ for every $n\ge1$. At every $\delta\le\delta_n$, target $n$ therefore needs at least $2^{3\cdot2^n/4}$ reversible rival states. Taking the largest admissible $n$ proves

$$
D_{\rm rev}(\delta)\ge\exp(c\delta^{-\alpha}),\qquad
\alpha=(\log2)/C_5>0.
\tag{38}
$$

All scalar witnesses used at this $n$ have retained fixed-clock horizons $O_a(\log(1/\delta))$ by Section 4.

## 8. Upper bounds under the same exit budget

The [bounded-rate finite-word upper bound](BOUNDED_RATE_FINITE_FIELD.md) starts from a stochastic uniformization. Its spectral-cap assumption is used there to obtain such a matrix and bound the update rate. Here the target already has the explicit stochastic $P=I+K/\mathcal B$, so the proof applies directly with update rate $\mathcal B$, even though the target spectral cap is $2\mathcal B$. It does not require $P$ to have nonnegative spectrum or positive diagonal.

The stationary word chain over the two output symbols has at most $2^\ell$ hidden states, preserves the exact histogram and original field rule, and has exits at most $\mathcal B$. Its all-horizon controlled-mean error is at most

$$
(1+2R_H^2)\left(\frac{\mathcal B R_H}{1+\mathcal B R_H}\right)^{\ell+1}.
$$

Thus it gives the explicit upper

$$
D_{\rm all}(\delta)\le
1+\max\left\{2,\left(\frac{1+2R_H^2}{\delta}\right)^p\right\}.
\tag{39}
$$

For reversible prediction, the finite-word prediction partition from Section 7 of the same upper-bound note gives

$$
D_{\rm rev}(\delta)\le
\exp\!\left(C\delta^{-p}\log(2/\delta)\right).
\tag{40}
$$

Again use the target's actual uniformization rate $\mathcal B$ in its proof. The partition refines exact binary levels and uses the compressed generator $EKE$. Its nonzero Rayleigh quotients retain the band $[1,2\mathcal B]$. More directly, a cell's exit is a conditional average of the original rates leaving that cell, hence at most $\mathcal B$; this proves the common exit budget without confusing it with the spectral cap. The target is connected, so the positive-mass quotient is irreducible.

## 9. A polynomial lower for unrestricted prediction

Uniform root weights and the independent table bits give

$$
\langle f_b,f_c\rangle_\mu=m\,\mathbf1_{b=c},\qquad m=1/18.
\tag{41}
$$

Let $Q_s=R_+-R_-$. Since $v=Q_s1$, the physical scalar factorization is

$$
L_b=\pi_0 B_0 Q_s^*W_b^*,\qquad
R_c=W_cQ_s B_0S,\qquad
L_bR_c=m\,\mathbf1_{b=c}.
\tag{42}
$$

Equation (18) verifies the normalization. Each complete side has physical generator degree $O(n)$ and coefficient mass $\exp(O(n))$.

Apply the target-only whole-side fixed-clock rank argument from the [polynomial controlled lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md). Expand the target generators as logarithms and truncate each whole side separately at total degree $M_0=C_a(n+1)$. The target operator tails decay geometrically in $M_0$ with prefactors exponential in $n$. Choose $C_a$ large enough that each resulting matrix entry changes by at most $m/(4r)$. The resulting $r\times r$ target matrix has smallest singular value at least $3m/4$, since its perturbation from $mI_r$ has operator norm at most $m/4$.

Each retained side is a finite linear combination of legal propagator words, with coefficient mass $\exp(O_a(n))$. On any $D$-state Markov rival the same scalar matrix factors through $D$ coordinates, so its rank is at most $D$. This step uses only finite physical experiments on the rival; no rival generator is expanded as a logarithm. If $D<r$, target-to-rival matrix error in operator norm is at least $3m/4$. Uniform actual-mean error bounds it above by $r\exp(O_a(n))\delta$. Thus some actual mean differs by at least $e^{-C_6(n+1)}$.

Selecting $n$ on this inverse-error scale gives $D_{\rm all}(\delta)\ge c_0\delta^{-\zeta}$ for a fixed $\zeta>0$. In fact this rank lower permits arbitrary rival field dependence, fixed preparation and readout, and unbounded rates; it therefore applies in particular to the narrower common-budget class of Section 1. The reversible entropy lower is logically separate and does require the prescribed binary field rule and rate budget.

Restoring $k$ multiplies all rates by $k$ and divides witnessing times by $k$. Equations (38)--(42) complete (5).

## 10. Scope and contribution

The binary alphabet is fixed and exactly balanced. The target is uniformly mixing, every retained gadget coordinate is counted, and the two predictor classes have the same exit budget $6580k$. The only difference between those classes is ordinary reversibility. The proof assigns no target labels to new rival states: its measure (27), repaired kernels and decoded bits are constructed on those states themselves.

The lower already uses five field values and any fixed positive clock. It concerns finite-error prediction of actual means, not only formal derivatives, hidden prefix laws, or exact realization. The upper bounds hold over all bounded protocols and horizons. Matching exponents, improving the fixed rate-to-gap ratio to the earlier band $[k,3k]$, and removing the rival rate cap are open.

Binary marker coding, positive changes of measure, stationary transport repair, and the lamp-flip entropy argument are mathematical ingredients of the proof. The candidate research contribution is their combination into the quantitative common-budget prediction separation (5). This theorem and its internal checks do not themselves certify publication novelty; the [prior-art audit](PRIOR_ART.md) records that separate question.

The accompanying [exact verifier](../scripts/verify_binary_reversibility_lower_bound.py) checks the literal $n=1$ sparse graph, marker support from every hidden state, root-restricted gate and probe words, weighted histogram and path-load identities, and small repair/change-of-measure examples. Its [saved report](../reports/binary_reversibility_lower_bound.json) records that executable evidence. These finite checks support the all-$n$ arguments above; they do not numerically establish the asymptotic lower bound or the novelty assessment.
