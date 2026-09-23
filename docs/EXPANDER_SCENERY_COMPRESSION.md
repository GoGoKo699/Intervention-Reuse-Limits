# Polynomial reversible compression for typical scenery on sparse expanders

[Repository overview](../README.md) · [Expander lower bound](EXPANDER_SCENERY_LOWER_BOUND.md) · [Small-flux fragmentation](SPARSE_REVERSIBLE_COMPRESSION.md) · [Bounded-rate prediction](BOUNDED_RATE_FINITE_FIELD.md)

**Research theorem, 22 September 2026.** A typical fixed binary labeling of a logarithmic-girth, four-regular graph has a polynomial-size reversible predictor for the actual controlled mean, simultaneously at every accuracy. A two-state sign layer makes the actuator histogram exactly balanced for every labeling. When the base graphs are expanders, the original sparse local dynamics themselves have a uniform positive gap. The surrogate retains ordinary detailed balance, the original exponential field rule, and the advertised full internal spectral band.

This class can violate both the earlier density-moment condition and the small-stationary-flux fragmentation condition. The construction replaces finite local scenery statistics by those of a small high-girth graph, then selects complete physical components with positive weights. It does not obtain a small surrogate by cutting most strong transitions from the target.

The result concerns a precisely defined, high-probability labeling class. It is not a theorem for arbitrary fixed labels or for a spectral cap alone. The graph construction, concentration, finite convex reduction, and regeneration are established ingredients; their constrained prediction consequence and combination with the [lower bound](EXPANDER_SCENERY_LOWER_BOUND.md) are the research claims assessed here. This expander theorem proves neither an intrinsic asymptotic penalty for reversibility nor an optimal exponent.

## 1. Fixed-label physical model

Fix $k,H,s,a_g>0$ and $0<\eta<1$. Let $G$ be a finite connected simple four-regular undirected graph with $N$ vertices, simple-walk matrix $P_G$, and

$$
\operatorname{girth}(G)\ge a_g\log N.
\tag{1}
$$

Draw independent uniform signs $x_v\in\{-1,+1\}$ once and freeze them. A hidden state is $(v,\sigma)$ with $\sigma\in\{-1,+1\}$. All $2N$ hidden states are counted. Let $F$ flip the sign layer, and define

$$
\mu(v,\sigma)=\frac1{2N},\qquad g_x(v,\sigma)=s\sigma x_v,
$$

$$
L=\frac k4(P_G-I)\otimes I_\sigma
 +\frac k4 I_v\otimes(F-I),\qquad
K=L+\frac{3k}{2}(\Pi_\mu-I).
\tag{2}
$$

The internal generator is independent of $x$; the actuator uses the frozen labels. Every fixed labeling has exactly half its stationary mass at each actuator value $\pm s$. Thus $g$ is centered, its variance is $W=s^2$, and $|g|=s$.

The local support graph is connected and has degree five. Its relaxation rates are at most $k$. If the normalized base-walk Poincaré gap is $\gamma>0$, its local gap is

$$
\kappa_0 k=\min\{\gamma/4,1/2\}k.
\tag{3}
$$

The global refresh gives strictly positive off-diagonal entries and places every nonzero full internal relaxation rate in the fixed band

$$
[3k/2,5k/2].
\tag{4}
$$

Attach the physical state $A$ with the original field rule

$$
q_{A,i}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{i,A}(h)=k e^{(g_i-1)h}.
\tag{5}
$$

Use the fixed readout $S(A)=-1$, $S(B_i)=+1$ and zero-field equilibrium preparation. At constant field, ordinary detailed balance holds under

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(B_i)=\frac{\mu_i e^h}{2\cosh h}.
$$

Every approximation below concerns the actual mean, uniformly over deterministic piecewise-continuous protocols with $|h(t)|\le H$ and all observation times.

## 2. Main theorem and explicit finite budgets

Put

$$
R=e^{(1+s)H},\quad C_R=1+2R^2,\quad A_H=e^{2sH},
\quad \Lambda=5/2,
$$

$$
q=\frac{\Lambda R}{1+\Lambda R},\qquad
\beta=-\log q=\log\left(1+\frac1{\Lambda R}\right),
$$

$$
p_g=\frac{\log2+\max\{2/a_g,8\log3\}}\beta.
\tag{6}
$$

For each fixed base graph, Section 3 defines a single labeling event $\mathcal E_{G,\eta}$, independent of the requested accuracy, with probability greater than $1-\eta$.

**Theorem.** Every target whose labeling belongs to $\mathcal E_{G,\eta}$ has, simultaneously for every $0<\delta<1$, a surrogate in the original reversible physical family satisfying

$$
\boxed{
\sup_{h,t}|m_F[h](t)-m_{\widehat F}[h](t)|\le\delta,
\qquad
D\le C_{a_g,s,H,\eta}\delta^{-p_g}.
}
\tag{7}
$$

The total physical count $D$ includes every component index, position, sign state, and $A$. The surrogate preserves the exact actuator histogram, original rate rule (5), fixed readout and preparation, ordinary detailed balance, and band (4). It consequently retains the passive telegraph path law, equilibrium curve, reference linear response, and zero quadratic response. A stronger target-specific lower gap, or a connected sparse local decomposition of the surrogate, is not asserted.

Here are explicit parameters before simplifying the polynomial. For $\ell\ge1$ define

$$
B_\ell=(\ell+2)\log2+2\log(\ell+1)+\log(1/\eta).
\tag{8}
$$

For the requested accuracy choose

$$
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_R/\delta)}\beta\right\rceil-1
\right\},
$$

$$
T_\delta=\max\left\{
 e^{(2\ell+1)/a_g},
 \frac{2C_R^2A_H^2\,4^\ell(\ell+1)^4 B_\ell}{\delta^2}
\right\}.
\tag{9}
$$

If $N\le T_\delta$, keep the exact original model, of size $2N+1$. If $N>T_\delta$, the constructed surrogate has

$$
\boxed{
D\le1+2^{\ell+2}(3^{2\ell+1}+2)^4.
}
\tag{10}
$$

This finite case split is essential. It handles small graphs and arbitrarily fine accuracies without demanding a fixed graph have indefinitely increasing girth.

## 3. One high-probability event covers all prefix lengths

Uniformize the local generator at clock $k$:

$$
P_{\rm loc}=I+L/k
=\tfrac12 I+\tfrac14(P_G\otimes I_\sigma)
 +\tfrac14(I_v\otimes F).
\tag{11}
$$

A local update holds, moves to a uniformly selected base neighbor, or flips the sign layer. The base position is uniform at every update under stationary initialization.

For a binary word $w$ of length $\ell+1$, let $f_w(x)$ be its stationary local-prefix probability with the fixed labeling $x$. Define $\mathcal E_{G,\eta}$ by the simultaneous inequalities

$$
\left|f_w(x)-\mathbb E_x f_w(x)\right|
\le(\ell+1)\sqrt{\frac{B_\ell}{2N}}
\tag{12}
$$

for every integer $\ell\ge1$ and every such word. The expectation is over the independent frozen vertex labels. At length one the histogram is already exact for every labeling.

Flip one label $x_v$, and couple the two models using the same stationary base trajectory and sign trajectory. Their observed words can differ only if one of the $\ell+1$ inspected base positions equals $v$. Stationarity and a union bound therefore give

$$
|f_w(x)-f_w(x\text{ with }x_v\text{ flipped})|
\le\frac{\ell+1}{N}.
\tag{13}
$$

McDiarmid's inequality implies that the failure probability of (12) for one word is at most $2e^{-B_\ell}$. Union over its $2^{\ell+1}$ words gives $\eta/(\ell+1)^2$. The countable union over all lengths is valid and yields

$$
\Pr(\mathcal E_{G,\eta}^{\,c})
\le\eta\sum_{\ell=1}^{\infty}\frac1{(\ell+1)^2}
<\eta.
\tag{14}
$$

Thus one event for each fixed graph covers every requested accuracy. No simultaneous random-label guarantee over all possible graphs is claimed.

On this event, the local stationary prefix law differs from its annealed law by total variation at most

$$
\boxed{
\theta_\ell
=2^\ell(\ell+1)\sqrt{\frac{B_\ell}{2N}}.
}
\tag{15}
$$

The bound may exceed one at large lengths, which does not invalidate it. Its useful range is selected by (9).

## 4. An elementary small graph with prescribed girth

We give a finite quantitative construction. In $\mathrm{SL}_2(\mathbb Z)$ let

$$
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\2&1\end{pmatrix}.
\tag{16}
$$

These matrices freely generate a group. For completeness, use the disjoint sets of nonzero real vectors

$$
X_A=\{(x,y):|x|>|y|\},\qquad
X_B=\{(x,y):|y|>|x|\}.
$$

For every nonzero integer $n$, $A^nX_B\subset X_A$ and $B^nX_A\subset X_B$. A reduced word can be cyclically conjugated to a nonzero power of one generator or to

$$
W=A^{a_1}B^{b_1}\cdots A^{a_r}B^{b_r},
$$

with all exponents nonzero, after interchanging $A,B$ if needed. Powers are visibly nonidentity. If the alternating word were identity, choose an integer $q_0\ne0,b_r$. The reduced word $WB^{-q_0}$ maps $X_A$ into $X_A$ by the displayed inclusions, whereas it would equal $B^{-q_0}$, which maps $X_A$ into $X_B$. This contradiction proves freeness.

Each generator and inverse has absolute row-sum norm at most $3$. Hence any reduced nonempty word of length at most $t$ differs from $I$ in an integer entry whose nonzero absolute value is at most $3^t+1$.

Take the integer modulus

$$
M_t=3^t+2.
$$

Primality is unnecessary: determinant-one matrices remain invertible over $\mathbb Z/M_t\mathbb Z$. Let $\Gamma_t$ be the subgroup generated by their reductions. No reduced relation of length at most $t$ becomes identity modulo $M_t$. Counting all two-by-two matrices gives $|\Gamma_t|\le M_t^4$.

For $t\ge3$, the undirected Cayley graph $H_t$ on $\Gamma_t$ with generators $A,A^{-1},B,B^{-1}$ is connected, simple, and four-regular. A simple cycle of length at most $t$ would give a reduced relation, so

$$
\boxed{
\operatorname{girth}(H_t)>t,\qquad
|H_t|\le(3^t+2)^4.
}
\tag{17}
$$

We use $t=2\ell+1$. This proof supplies an explicit size bound; efficient enumeration is not required by the state-count theorem.

## 5. Match the annealed law with complete physical components

If $\operatorname{girth}(G)>2\ell+1$, every radius-$\ell$ rooted neighborhood has the tree geometry inspected by a walk of at most $\ell$ base moves. The annealed local color-prefix law consequently agrees exactly with the corresponding law on $H_{2\ell+1}$.

To see this, first condition on all hold, base-move, and sign-flip choices in (11), including the initial sign. Couple the paths on their common rooted four-regular tree. Repeated visits identify precisely the same tree vertices. Assign an independent fair frozen label to each distinct visited vertex in both models. Multiplication by the coupled, possibly changing sign $\sigma$ then gives identical output words. This explicitly retains the evolving sign process; it does not replace $\sigma(t)x_{v(t)}$ by independent signs at repeated visits. Finally average over the choices and stationary root.

Let $H=H_{2\ell+1}$. For every fixed labeling $y$ of $H$, form its complete $2|H|$-state sign-layer component with generator (2) before global refresh. Let $v_y$ be its stationary local-prefix vector on the $2^{\ell+1}$ words. The annealed law is their exact convex average. Carathéodory's theorem in the probability simplex gives labelings $y_1,\ldots,y_J$ and positive weights $a_j$ with

$$
J\le2^{\ell+1},\qquad \sum_j a_j=1,
\qquad \sum_j a_jv_{y_j}=\mathbb E_yv_y.
\tag{18}
$$

Copy all positions and both signs of every selected component, keeping its original local rates. Give a copied state stationary mass

$$
\nu(j,v,\sigma)=\frac{a_j}{2|H|}.
$$

Reweighting whole components preserves detailed balance. Each component has exactly balanced actuator histogram, and the mixture does too. Its local spectral cap is $k$. Add the same global refresh,

$$
\widehat K=\widehat L+\frac{3k}{2}(\Pi_\nu-I).
\tag{19}
$$

On centered functions, the refresh shifts each local relaxation rate by $3k/2$, proving the full band (4). Off-diagonal rates become strictly positive. The total physical count is $1+2|H|J$, proving (10).

For a good fixed-label target, its local-prefix error from this exact annealed realization is at most $\theta_\ell$ in (15). The chosen mixture index is a counted state coordinate; there is no external label memory.

## 6. Restore refresh and control every horizon

At the common full internal clock $\Lambda k=(5/2)k$,

$$
P_{\rm full}=\tfrac25P_{\rm loc}+\tfrac35\Pi_\mu,
$$

and the surrogate has the same decomposition with its stationary law. Condition on shared independent refresh flags. A prefix of $\ell+1$ symbols splits into at most $\ell+1$ stationary local runs. Conditional on the flags and a fixed target labeling, these runs are independent. Each run has total-variation error at most $\theta_\ell$: its shorter law is a marginal of a matched or approximated length-$\ell+1$ local law. Product total variation is at most the sum of its factor errors. Averaging over flags gives

$$
\theta_{\rm full}\le(\ell+1)\theta_\ell.
\tag{20}
$$

The fixed target retains its labeling when it refreshes, whereas the surrogate may select a different mixture component. Equation (20) compares their deterministic local run laws. It does **not** identify the quenched refreshed law with an average over labelings: an average of products need not be a product of averages.

The exact histogram gives a common entry-tilt normalization under (5). Tilting a prefix by its first symbol increases total variation by at most $A_H$. The [bounded-rate regenerative estimate](BOUNDED_RATE_FINITE_FIELD.md#72-regeneration-with-approximate-prefixes), using the common external reset to $A$ at rate $k/R$, now gives

$$
\begin{aligned}
\sup_{h,t}|m_F[h](t)-m_{\widehat F}[h](t)|
&\le C_R\left[A_H(\ell+1)\theta_\ell+q^{\ell+1}\right]\\
&=C_R\left[
 A_H2^\ell(\ell+1)^2\sqrt{\frac{B_\ell}{2N}}
 +q^{\ell+1}\right].
\end{aligned}
\tag{21}
$$

The same argument covers stationary initial hidden visits and field-tilted later entries. It bounds the actual mean at every observation time, rather than entire-history total variation over unbounded horizons.

If $N>T_\delta$, (1) and (9) imply $\operatorname{girth}(G)>2\ell+1$, and the two terms in (21) are each at most $\delta/2$. If $N\le T_\delta$, the exact model has zero error. This proves the explicit finite theorem.

## 7. Simplifying the count to a polynomial

At fixed $a_g,s,H,\eta$, the chosen $\ell$ is $O(\log(2/\delta))$. The exact-model threshold satisfies

$$
T_\delta\le C\left[
\delta^{-2/(a_g\beta)}
+\delta^{-[2+2\log2/\beta]}\log^5(2/\delta)
\right].
\tag{22}
$$

The replacement size has

$$
(3^{2\ell+1}+2)^4\le1296e^{8\ell\log3},
$$

so (10) is at most $1+5184e^{(\log2+8\log3)\ell}$. Its exponent is $(\log2+8\log3)/\beta$.

Both terms in (22) are bounded by a constant times $\delta^{-p_g}$. The first has a strictly smaller exponent. For the second, use $R\ge1$, so $\beta\le\log(7/5)$, and

$$
\frac{\log2+8\log3}{\beta}
-\left(2+\frac{2\log2}{\beta}\right)
=\frac{8\log3-\log2-2\beta}{\beta}>0.
\tag{23}
$$

This strict power margin absorbs the fifth power of the logarithm. Equations (22)–(23) prove (7) with the stated sufficient exponent. The large constants and conservative exponent do not claim efficient construction, learning from samples, bounded parameter precision, or a practical state budget.

## 8. Why neither previous sufficient condition applies uniformly

Suppose now that the base graphs form a logarithmic-girth expander family with normalized gap at least $\gamma_0>0$. Then (3) gives a fixed positive local gap $\kappa_0k$ on the connected sign-layer graph. Such base families are supplied by established expander constructions; see [the primary-source discussion](PRIOR_ART.md). The lower-bound note fixes an explicit family and its quantitative constants.

The local base edge rate is $k/16$. Since each hidden stationary mass is $1/(2N)$, its full conductance density is at least $N/8$. There are $8N$ directed base edges, so for every $\alpha>0$,

$$
\sum_{i,j}\mu_i\mu_j q(i,j)^{1+\alpha}
\ge\frac{2}{N}\left(\frac N8\right)^{1+\alpha}
=2\cdot8^{-(1+\alpha)}N^\alpha.
\tag{24}
$$

Thus no uniform positive density moment holds, regardless of the fixed labeling.

The [Poincaré fragmentation obstruction](SPARSE_REVERSIBLE_COMPRESSION.md#10-a-precise-limitation-of-stationary-flux-fragmentation), applied to the local sign-layer generator with uniform law on $2N$ states, gives

$$
\Phi\ge\kappa_0\left(1-\frac{S}{2N}\right)
\tag{25}
$$

for any symmetric edge deletion leaving components of at most $S$ states. A target-size-independent component bound therefore cannot have vanishing removed stationary flux. In this connected expander application the new predictor applies where both preceding sufficient hypotheses fail.

The target's local gap is used here to separate the hypotheses, not to prove the prediction upper. The upper only uses logarithmic girth and the labeling event. The surrogate may use several local components and is asserted to retain the full advertised band (4) through its supplied refresh. No inference from a failed approximation method to an intrinsic reversible memory lower bound is made.

## 9. An unconditional annealed subtheorem

An auxiliary deterministic version makes the finite-statistics construction explicit. Replace the frozen target labeling by a counted hidden coordinate ranging over all $2^N$ labelings, with uniform stationary weight, while keeping local base and sign dynamics as in (2). A global refresh redraws the labeling as well. This target has $2N2^N$ hidden states and exactly the same advertised physical constraints.

For any $\ell$, if $\operatorname{girth}(G)>2\ell+1$, replace its base by $H_{2\ell+1}$; otherwise (1) gives $N\le e^{(2\ell+1)/a_g}$ and retain $G$. Select at most $2^{\ell+1}$ entire fixed-label sign-layer components by (18). The local prefix match is now exact. Conditioning on refresh flags keeps the full prefix match exact as well. Hence

$$
D\le1+2^{\ell+2}
\max\left\{e^{(2\ell+1)/a_g},(3^{2\ell+1}+2)^4\right\},
$$

$$
\sup_{h,t}|m_F[h](t)-m_{\widehat F}[h](t)|
\le C_Rq^{\ell+1}.
\tag{26}
$$

Choosing $\ell=\max\{1,\lceil\log(C_R/\delta)/\beta\rceil-1\}$ gives the same polynomial exponent $p_g$, without a good-label event. The full original dictionary and every retained component are counted. This annealed model is separate from the single fixed-label connected target in Sections 1–8.

## 10. Verification and remaining scope

[The exact verifier](../scripts/verify_expander_scenery_compression.py) and [saved report](../reports/expander_scenery_compression.json) check the finite algebra behind the construction. The uniform theorem is the proof above; finite checks do not certify all graph sizes or all controls. See [verification notes](VERIFICATION.md) for the audited scope.

The good event is target-specific but defined uniformly over all lengths. At $\eta=1/4$ it has probability greater than $3/4$ for each supplied base graph. It can therefore be intersected with a separately proved lower-bound event of probability at least $3/4$, producing fixed labels that satisfy both conclusions. The [expander lower-bound theorem](EXPANDER_SCENERY_LOWER_BOUND.md) carries out that intersection.

Arbitrary deterministic binary scenery in this expander class, the binary question in the tight band $[k,3k]$, and matching polynomial exponents remain open. A separate [binary family](BINARY_REVERSIBILITY_LOWER_BOUND.md) proves an intrinsic reversibility cost at a larger fixed budget, with the prescribed rule and exact histogram; it does not resolve those tighter questions. All constructors receive the supplied target. Manuscript drafting and claims of established publication novelty do not follow from this theorem.
