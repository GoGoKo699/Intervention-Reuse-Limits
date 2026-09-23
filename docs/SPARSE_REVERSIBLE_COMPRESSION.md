# Polynomial reversible compression from small stationary-flux cuts

[Repository overview](../README.md) · [Local-walk lower bound](LOCAL_WALK_LOWER_BOUND.md) · [Conductance-tail and moment bounds](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) · [Bounded-rate finite-field prediction](BOUNDED_RATE_FINITE_FIELD.md)

**Research theorem, 22 September 2026.** If the local part of a reversible hidden generator can be cut into small components at low stationary jump cost, then a small weighted selection of whole components gives a reversible predictor for the actual controlled mean. Strong transitions inside the selected components are retained exactly. For nearest-neighbor graphs in fixed dimension, the resulting state count is polynomial in inverse error, without a conductance-density or density-moment bound.

The surrogate uses the original exponential field rule and preserves the exact actuator histogram and original upper spectral cap. A supplied positive global refresh also preserves its corresponding lower spectral endpoint. In particular, the binary path-and-refresh class in the [local-walk theorem](LOCAL_WALK_LOWER_BOUND.md) has polynomial reversible switching complexity within its original spectral band. The exponent need not match the lower-bound exponent.

Graph fragmentation, positive finite cubature, and regeneration are established ideas; see [the prior-art discussion](PRIOR_ART.md). The contribution assessed here is their combination with the physical constraints and the uniform controlled-mean guarantee. A spectral cap alone does not imply the fragmentation hypothesis. The binary problem in the tight band $[k,3k]$ remains open. A separate [binary family](BINARY_REVERSIBILITY_LOWER_BOUND.md) has exponential reversible cost at a larger fixed rate budget, under the prescribed rule and exact histogram; the [nineteen-level family](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) retains budget $3k$.

## 1. Model and fragmentation hypothesis

Fix $k,\Lambda,G,H>0$ and a finite actuator alphabet of $m\ge2$ positive-mass values in $[-G,G]$. The target has hidden stationary law $\mu$, centered actuator $g$, and internal generator

$$
K=L+ck(\Pi_\mu-I),\qquad 0\le c\le\Lambda,
\tag{1}
$$

where $L$ is a $\mu$-reversible Markov generator, possibly reducible, and $\Pi_\mu=\mathbf1\mu^T$. Assume every nonzero eigenvalue of $-K$ is at most $\Lambda k$. All stationary masses are positive. An existing lower spectral bound by itself does **not** assert the nonnegative Markov decomposition (1).

The physical states are $A$ and the hidden states $B_i$, with fixed readout $S(A)=-1$, $S(B_i)=+1$, external rates

$$
q_{A B_i}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{B_i A}(h)=k e^{(g_i-1)h},
\tag{2}
$$

and field-independent internal generator $K$. At each constant field the full model is ordinarily reversible with stationary law

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(B_i)=\frac{\mu_i e^h}{2\cosh h}.
\tag{3}
$$

Every experiment starts from $\pi_0$, and $m_F[h](t)$ denotes its actual mean readout under a deterministic piecewise-continuous protocol with $|h(t)|\le H$. The approximation norm below is uniform over all such protocols and all observation times.

Put $r=\Lambda-c$. On $\mu$-centered functions, $-K=-L+ckI$, so $-L$ has spectral cap $rk$. This remains true if $L$ is reducible. Applying the cap to the centered indicator of a state gives

$$
-L_{ii}\le rk(1-\mu_i)\le rk.
\tag{4}
$$

For $\varepsilon>0$, suppose symmetric deletion of some local edges gives a generator $L^{\rm del}$ whose connected components have at most $S(\varepsilon)$ vertices and whose dimensionless directed stationary removed flux is

$$
\Phi:=\frac1k\sum_i\mu_i\sum_{j\ne i}
       (L_{ij}-L^{\rm del}_{ij})\le\varepsilon.
\tag{5}
$$

Deletion removes both directions of an edge and resets the diagonal to the negative remaining row sum. In particular, $L^{\rm del}$ remains reversible, and its Dirichlet form is bounded by that of $L$; its spectral cap is still $rk$. The function $S$ may be a uniform class bound or a certificate for a supplied target. Bounded degree alone is insufficient to give a target-size-independent profile; Section 10 proves a precise obstruction.

Define

$$
R=e^{(1+G)H},\qquad C_R=1+2R^2,\qquad
q_\Lambda=\frac{\Lambda R}{1+\Lambda R},
$$

$$
\beta=\log\left(1+\frac1{\Lambda R}\right),\qquad
p_\Lambda=\frac{\log m}{\beta}.
\tag{6}
$$

## 2. Reversible upper bound with a positive supplied refresh

**Theorem.** Suppose $c>0$. For any integer $\ell\ge1$ and deletion satisfying (5), there is a surrogate in the original reversible physical family with at most

$$
\boxed{D\le1+S(\varepsilon)m^{\ell+1}}
\tag{7}
$$

total physical states and

$$
\boxed{
\sup_{T>0}\sup_{|h|\le H}\sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|
\le R^3\varepsilon+C_Rq_\Lambda^{\ell+1}.
}
\tag{8}
$$

The surrogate uses (2), the preparation (3) at zero field, and the fixed binary readout. It preserves every actuator value and its exact stationary mass. Hence it preserves centering, variance $W$, the sensitivity bound, the passive telegraph path law, equilibrium curve, reference linear mean response, and zero quadratic mean response. Its nonzero internal relaxation rates lie in

$$
[ck,\Lambda k].
\tag{9}
$$

It is ordinarily reversible at each constant field, and its internal off-diagonal rates are strictly positive. A target lower spectral endpoint larger than $ck$ is not asserted to survive.

For a prescribed $0<\delta<1$, set

$$
\varepsilon=\frac{\delta}{2R^3},\qquad
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_R/\delta)}\beta\right\rceil-1
\right\}.
\tag{10}
$$

Then the error is at most $\delta$, and

$$
\boxed{
D\le1+S\left(\frac{\delta}{2R^3}\right)
m\max\left\{m,\left(\frac{2C_R}{\delta}\right)^{p_\Lambda}\right\}.
}
\tag{11}
$$

No conductance-density bound, density-moment bound, stationary-mass lower bound, or restriction on individual local edge weights is assumed beyond (1), the spectral cap, and (5). If $r=0$, the internal chain is pure stationary refresh and an exact model with $m+1$ total states suffices.

## 3. Edge deletion is charged in the actual driven-mean norm

Let $K^{\rm del}=L^{\rm del}+ck(\Pi_\mu-I)$ and keep the external rates unchanged. The target's driven hidden density satisfies

$$
0\le x_i(t):=\frac{p_{B,i}(t)}{\mu_i}\le R^2
\tag{12}
$$

uniformly in protocols and time. Its hidden forward equation has stationary internal dynamics, killing rates at least $k/R$, and entry-source coordinates at most $kR\mu_i$. Since its initial hidden density is $1/2$, the constant density $R^2$ is a supersolution, and the finite-dimensional positive-system comparison principle gives (12).

Write $\Delta L=L-L^{\rm del}$ and, for $i\ne j$, let

$$
d_{ij}=\frac{\Delta L_{ij}}{k\mu_j},\qquad d_{ii}=0.
$$

Detailed balance gives $d_{ij}=d_{ji}$, and the diagonal row-sum identity yields

$$
(p_B\Delta L)_j
=k\mu_j\sum_i\mu_i d_{ij}(x_i-x_j).
\tag{13}
$$

Therefore

$$
\|p_B\Delta L\|_1
\le k\sum_{i,j}\mu_i\mu_jd_{ij}|x_i-x_j|
\le kR^2\Phi.
\tag{14}
$$

The signed forcing has total mass zero. The full deleted generator at every field contains a common reset to $A$ at rate $\alpha=k/R$:

$$
Q^{\rm del}(h)=\alpha(\mathbf1 e_A^T-I)+Q^{\rm res}(h),
\tag{15}
$$

where the residual is a Markov generator. On zero-mass rows, the rank-one reset term vanishes; its propagator thus contracts signed $L^1$ norm by $e^{-\alpha(t-s)}$, also under time-dependent fields. Duhamel's formula, with the original occupation in the forcing and the deleted propagator afterwards, gives

$$
\|p_F(t)-p_{F^{\rm del}}(t)\|_1
\le kR^2\Phi\int_0^t e^{-k(t-s)/R}\,ds
\le R^3\Phi.
$$

Since $|S|=1$,

$$
\sup_{h,t}|m_F[h](t)-m_{F^{\rm del}}[h](t)|
\le R^3\Phi\le R^3\varepsilon.
\tag{16}
$$

The flux in (5) is directed. There is no extra factor two after combining the two reversible contributions into $x_i-x_j$. The same calculation applies to a signed symmetric rate change if $\Phi$ is replaced by its absolute directed stationary off-diagonal flux; that version will be used in Section 6. This is the forcing argument from [the moment-density theorem](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md#3-symmetric-clipping-costs-only-a-stationary-weighted-flux).

## 4. Preserve finite prefixes by selecting whole components

Suppose $r>0$. For every connected component $C$ of $L^{\rm del}$, let $\mu(C)>0$ be its stationary mass and $\mu_C$ its conditional stationary law. The restriction $L_C$ is reversible and irreducible, or a singleton, and its spectral cap is at most $rk$. Thus

$$
P_C=I+\frac{L_C}{rk}
\tag{17}
$$

is a stochastic reversible matrix. Let $v_C(w)$ be the stationary probability of actuator word $w$ of length $\ell+1$ under $P_C$, starting from $\mu_C$. Each $v_C$ belongs to the probability simplex of affine dimension $m^{\ell+1}-1$. The stationary prefix vector for the deleted local chain is

$$
v=\sum_C\mu(C)v_C.
$$

Carathéodory's theorem in that affine simplex supplies components $C_1,\ldots,C_J$ and positive weights $a_1,\ldots,a_J$ such that

$$
J\le m^{\ell+1},\qquad
\sum_{j=1}^Ja_j=1,\qquad
v=\sum_{j=1}^Ja_jv_{C_j}.
\tag{18}
$$

Zero weights are omitted. Copy every microscopic state and rate within each selected component. Define the new stationary law and block generator by

$$
\nu(j,x)=a_j\mu_{C_j}(x),\qquad
L^{\rm sel}|_{C_j}=L_{C_j},
\tag{19}
$$

with no local transitions between copied components. Reweighting an entire component leaves detailed balance intact. The spectrum is the union of its component spectra, so $-L^{\rm sel}$ still has cap $rk$. Its total hidden state count is at most $S(\varepsilon)m^{\ell+1}$.

Equation (18) exactly matches stationary local actuator prefixes of length $\ell+1$. Marginalizing matches every shorter prefix, including the one-symbol marginal. Consequently the entire actuator histogram is exact, with no subsequent centering, variance, or moment correction.

Restore the same global refresh rate:

$$
K^{\rm sel}=L^{\rm sel}+ck(\Pi_\nu-I).
\tag{20}
$$

For $c>0$, this has strictly positive off-diagonal entries and is ordinarily reversible under $\nu$. On centered functions, each relaxation eigenvalue is $ck$ plus an eigenvalue of $-L^{\rm sel}$, establishing (9).

If $r=0$, the cap forces $L=0$. Its exact actuator partition has stationary masses $\rho_a=\mu(g=z_a)$, sensitivities $z_a$, and generator $ck(\Pi_\rho-I)$. This is a lumping of both the internal and external dynamics, so the $m+1$-state physical model is exact for all protocols.

## 5. Restore global refresh and bound all horizons

At the common internal update clock $\Lambda k$, the deleted target and selected surrogate have matrices

$$
P^{\rm del}=\frac r\Lambda P^{\rm loc}+\frac c\Lambda\Pi_\mu,
\qquad
P^{\rm sel}=\frac r\Lambda P^{\rm loc}_{\rm sel}
             +\frac c\Lambda\Pi_\nu,
\tag{21}
$$

where $P^{\rm loc}=I+L^{\rm del}/(rk)$ and similarly for the selected chain. At each update, use the same independent Bernoulli flag in both models: perform a local update with probability $r/\Lambda$, or draw independently from the stationary law with probability $c/\Lambda$.

Condition on all flags in any block of at most $\ell+1$ actuator symbols. Every refresh splits the block into independent local runs. The first run starts in stationarity, and every later run starts with the stationary refresh draw. Each run therefore has a stationary local prefix distribution of length at most $\ell+1$. All these distributions agree by (18). Thus the full stationary actuator prefix laws agree exactly through length $\ell+1$ after restoring refresh. Reducibility of the local chain causes no difficulty.

Both physical models have the same escape hazard from $A$,

$$
k e^{h(t)}\sum_i\mu_i e^{h(t)g_i}\le kR=:b.
$$

At a hidden entry, its first actuator is tilted by $e^{h g}$ from its stationary law, with the same normalization in both models. This tilt preserves exact equality of the finite-prefix distributions. Initial hidden visits start from the untilted stationary law. Therefore the first $\ell+1$ actuator symbols of every visit can be coupled exactly, together with their rate-$\nu_0$ update clock, where $\nu_0=\Lambda k$. Until the $(\ell+1)$st update in the visit, their field-dependent killing rates agree.

For completeness, the all-horizon estimate from [the bounded-rate theorem](BOUNDED_RATE_FINITE_FIELD.md#5-a-regenerative-estimate-without-a-horizon-cutoff) can be applied directly. Couple the common reset clock (15), of rate $\alpha=k/R$, independently of the update clock. Declare the coupling bad if a hidden visit exhausts its prefix, and retain that declaration until the next common reset. Let

$$
p_\ell(u)=\Pr\{N_{\nu_0}(u)>\ell\}.
$$

At an observation time $t$, a bad coupling must originate from the initial hidden visit, of probability $1/2$, or a later hidden entry, whose intensity is at most $b$. Counting all potential updates after each such start only enlarges the event. Independence of future clock increments, conditioning at entry times, gives

$$
\Pr\{\text{bad at }t\}
\le\tfrac12 e^{-\alpha t}p_\ell(t)
 +b\int_0^t e^{-\alpha u}p_\ell(u)\,du.
\tag{22}
$$

If $\tau_{\ell+1}$ is the $(\ell+1)$st update time, then

$$
\mathbb E e^{-\alpha\tau_{\ell+1}}
=\left(\frac{\nu_0}{\nu_0+\alpha}\right)^{\ell+1}
=q_\Lambda^{\ell+1}.
$$

Hence $e^{-\alpha t}p_\ell(t)\le q_\Lambda^{\ell+1}$ and

$$
\int_0^\infty e^{-\alpha u}p_\ell(u)\,du
=\frac{q_\Lambda^{\ell+1}}\alpha.
$$

Multiplying (22) by two for the binary readout and using $b/\alpha=R^2$ proves

$$
\sup_{h,t}|m_{F^{\rm del}}[h](t)-m_{\widehat F}[h](t)|
\le(1+2R^2)q_\Lambda^{\ell+1}.
\tag{23}
$$

Together with (16), this proves (8). Since the prefix match is exact, no field-tilting amplification factor is needed. The clock is the full $\Lambda k$, including refresh. This estimate concerns the actual mean at each observation time; it is not a total-variation bound on entire visible histories over unbounded horizons.

All retained memory consists of the copied component vertices. The component index is part of the physical state count (7); there is no additional uncounted register.

## 6. Irreducibility repair when no global refresh is supplied

When $c=0$, the same selection and error proofs apply, but $L^{\rm sel}$ may be reducible internally. The full physical model, including $A$, is still irreducible. If irreducible internal dynamics or strictly positive internal off-diagonal rates are required, repair them without adding states.

For $0<\delta<1$, choose

$$
\varepsilon=\frac{\delta}{3R^3},\qquad
\ell=\max\left\{1,
\left\lceil\frac{\log(3C_R/\delta)}\beta\right\rceil-1
\right\},\qquad
\theta=\min\left\{\frac12,\frac{\delta}{6R^3\Lambda}\right\}.
\tag{24}
$$

Construct $L^{\rm sel}$ as above and set

$$
K^{\rm final}=(1-\theta)L^{\rm sel}
             +\theta\Lambda k(\Pi_\nu-I).
\tag{25}
$$

This is irreducible and reversible, has positive off-diagonal rates, and preserves the exact actuator histogram and external rule. Each centered relaxation eigenvalue $\lambda\in[0,\Lambda k]$ becomes $(1-\theta)\lambda+\theta\Lambda k$, so the final internal spectral interval is

$$
[\theta\Lambda k,\Lambda k].
\tag{26}
$$

The absolute directed stationary off-diagonal flux change obeys

$$
\frac1k\sum_i\nu_i\sum_{j\ne i}
|K^{\rm final}_{ij}-L^{\rm sel}_{ij}|
\le\theta\left[\frac1k\sum_i\nu_i(-L^{\rm sel}_{ii})
                 +\Lambda\left(1-\sum_i\nu_i^2\right)\right]
\le2\theta\Lambda.
\tag{27}
$$

The signed symmetric version of (13)–(16) therefore charges the repair at most $2R^3\theta\Lambda\le\delta/3$ in actual-mean error. Deletion and prefix truncation each cost at most $\delta/3$ under (24), proving total error at most $\delta$ with

$$
D\le1+S\left(\frac{\delta}{3R^3}\right)
m\max\left\{m,\left(\frac{3C_R}{\delta}\right)^{p_\Lambda}\right\}.
\tag{28}
$$

Thus the original upper cap and the same state-growth order survive without a pre-existing refresh. A larger original lower gap is not guaranteed by this repair.

## 7. Nearest-neighbor lattice graphs give a polynomial

Suppose the hidden vertices are distinct sites of any finite $V\subset\mathbb Z^d$, for fixed $d\ge1$, and every off-diagonal edge of $L$ joins lattice nearest neighbors. The stationary masses, reversible edge weights, actuator labels, and shape of $V$ are arbitrary. The full generator (1) may also include dense global refresh; the locality assumption applies to $L$.

Choose an integer $a\ge1$ and an offset $O$ uniformly from $\{0,\ldots,a-1\}^d$. Partition by the box coordinates

$$
\left(\left\lfloor\frac{x_j-O_j}{a}\right\rfloor\right)_{j=1}^d,
$$

and delete local edges crossing between boxes. Each nearest-neighbor edge crosses a box boundary with probability exactly $1/a$. Every remaining component lies inside a box and has at most $a^d$ vertices. Linearity of expectation and (4) give

$$
\mathbb E\Phi
=\frac1{ak}\sum_i\mu_i(-L_{ii})\le\frac ra.
\tag{29}
$$

Some offset therefore has $\Phi\le r/a$. No regularity or lower bound on the edge weights or stationary masses is used. A uniform fragmentation profile is

$$
S(\varepsilon)\le\max\{1,\lceil r/\varepsilon\rceil\}^{d}.
\tag{30}
$$

For $c>0$ and $r>0$, take $a=\max\{1,\lceil2R^3r/\delta\rceil\}$ in (11). Then

$$
\boxed{
D\le1+a^d m\max\left\{m,
\left(\frac{2C_R}{\delta}\right)^{p_\Lambda}\right\}
\le C_{d,m,\Lambda,c,G,H}\delta^{-(d+p_\Lambda)}.
}
\tag{31}
$$

For $c=0$, use $a=\max\{1,\lceil3R^3\Lambda/\delta\rceil\}$, (24), and the repair. The same exponent $d+p_\Lambda$ results. If $r=0$, the exact $m+1$-state model applies. If the supplied decomposition has $c\ge\kappa>0$, the construction preserves the specified internal band $[\kappa k,\Lambda k]$.

This condition can hold outside every fixed global $L^{1+\alpha}$ conductance-density class. For example, on increasingly long paths with uniform stationary law, each local edge of fixed positive jump rate has density proportional to the number of vertices, while the spectral cap stays bounded. A positive proportion of vertices have such an edge, so their contribution to $\sum_{i,j}\mu_i\mu_j q_{ij}^{1+\alpha}$ grows proportionally to a positive power of the path size. Adding a fixed global refresh does not remove that divergence. The cut profile (30) remains uniform.

## 8. Degree-two local graphs, including cycles

Every finite undirected support graph of maximum degree two is a disjoint union of paths, cycles, and isolated vertices. The preceding argument handles paths, and a direct cut construction handles all these graphs with the same one-dimensional exponent.

On each path, number its edges consecutively and delete edges in one uniformly chosen residue class modulo $a$. Every edge is cut with probability $1/a$, and each resulting component contains at most $a$ vertices.

For a cycle of $N<2a$ vertices, retain it whole. For $N\ge2a$, let $q=\lfloor N/a\rfloor\ge2$. Place $q$ cuts around the cycle with successive spacings differing by at most one, then rotate the pattern uniformly over its $N$ edges. Each edge is cut with probability $q/N\le1/a$. Every surviving arc contains at most $\lceil N/q\rceil\le2a$ vertices. Thus all components, including retained small cycles, have at most $2a$ vertices.

The expected directed stationary removed flux is at most $r/a$, by summing the cut probabilities against the edge fluxes. Some joint choice of cuts therefore has that bound. This proves

$$
S(\varepsilon)\le2\max\{1,\lceil r/\varepsilon\rceil\},
\qquad
D=O\bigl(\delta^{-(1+p_\Lambda)}\bigr),
\tag{32}
$$

with the same histogram, external-rule, spectral, and all-protocol guarantees as above. Multiple transition mechanisms between a pair of vertices are combined into their single generator entry; the degree refers to that ordinary undirected support graph.

For binary sensitivities $g=\pm\sqrt W$, use $m=2$ and $G=\sqrt W$ in (6). With refresh $c=3/2$ and cap $\Lambda=5/2$, this upper bound applies to the class in the [local-walk lower-bound theorem](LOCAL_WALK_LOWER_BOUND.md). It preserves its band $[3k/2,5k/2]$ and original field rule while achieving polynomial switching state count. The lower bound is also polynomial for unrestricted competitors; this establishes the same polynomial growth class without identifying an optimal common exponent.

## 9. Interpretation and verification

The construction keeps strong transitions inside complete physical component models. Positive weights in (18) then combine their stationary prefix laws. Carathéodory's theorem is being applied to an existing convex mixture of valid component models; arbitrary Gram matching or feature cubature is not being claimed to produce a positive Markov realization.

The constructor receives the full target, chooses an admissible cut, and selects components from their finite-prefix vectors. This is a state-count existence theorem, without a polynomial runtime, parameter-precision, or sample-efficient learning guarantee. The number of retained vertices is explicit, and the original target size does not enter when the fragmentation profile is uniform.

[The exact verifier](../scripts/verify_sparse_reversible_compression.py) and its [saved report](../reports/sparse_reversible_compression.json) check finite examples of the cut and component-selection identities, the physical constraints, and the explicit error allocations. These checks support the algebra; the uniform theorem follows from Sections 3–8. See [verification notes](VERIFICATION.md) for the checked scope and internal proof audits.

## 10. A precise limitation of stationary-flux fragmentation

Suppose the local generator $L$ itself has Poincaré gap $\kappa_0k>0$. For any partition into the surviving connected components $C$ after edge deletion, apply Poincaré to each indicator $\mathbf1_C$:

$$
\frac1k\sum_{i\in C,\ j\notin C}\mu_iL_{ij}
\ge\kappa_0\mu(C)[1-\mu(C)].
\tag{33}
$$

Every edge between different surviving components was removed. The sum of the component boundaries is therefore at most the total directed removed flux; equality is unnecessary, since some removed edges might have both ends in a surviving component. Summing (33) gives

$$
\Phi\ge\kappa_0\left[1-\sum_C\mu(C)^2\right]
\ge\kappa_0[1-S\mu_{\max}],\qquad
\mu_{\max}=\max_i\mu_i,
\tag{34}
$$

when every component has at most $S$ vertices. The last inequality uses $\mu(C)\le S\mu_{\max}$ and $\sum_C\mu(C)=1$. In particular, for uniform stationary law on $N$ vertices, a fragmentation with $\Phi\le\varepsilon<\kappa_0$ requires

$$
\boxed{S\ge N\left(1-\frac{\varepsilon}{\kappa_0}\right).}
\tag{35}
$$

Uniformly mixing local graphs with small individual stationary masses therefore cannot be fragmented into target-size-independent small components at vanishing stationary-flux cost. Bounded-degree expander families are one obstruction to inferring this property from sparsity and a cap alone.

This is a limitation of the fragmentation method, not a lower bound on optimal controlled-mean predictor size. A different reversible reduction could retain or reorganize transitions without such cuts. The tight-band binary problem and optimal exponents remain open. The separate [binary reversibility theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) proves an intrinsic asymptotic cost at a larger fixed competitor budget; the fragmentation obstruction is not that lower bound.
