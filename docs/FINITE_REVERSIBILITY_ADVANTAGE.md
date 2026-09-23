# A finite twelve-versus-eleven state advantage

[Capped interface observation calculus](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [Whole-side logarithm truncation](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Finite-EPR perturbation](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) · [Generalized-reversal distinction](GENERALIZED_REVERSAL_PREDICTION.md)

**Finite model theorem, 23 September 2026.** A twelve-state ordinarily reversible target has an exact eleven-state stationary nonreversible predictor for every controlled mean. Nevertheless, every ordinarily reversible predictor with at most eleven total states has error greater than $2^{-3000}$ on a specified finite set of two-field clock experiments. The comparison allows rivals their own states and endpoint kinetic barriers; it imposes no target histogram or inherited coordinates.

This is an ordinary-reversible versus unrestricted state advantage. No eleven-state generalized-reversible realization is asserted. The explicit error tolerance is a rigorous positive separation, not a useful experimental precision. The target is a new six-level model, not a member of the earlier nineteen-level lamp family; its actuator need not be centered.

## 1. Task and statement

Fix the external rate $k>0$. Take

$$
H=\log2,\qquad a=\frac{\log2}{8},\qquad
\beta_j=\frac{6+j}{16}\quad(0\le j\le5),\qquad
\delta_0=2^{-3000}.
\tag{1}
$$

The target constructed below has eleven hidden states plus one visible state $A$. Its hidden generator is ordinarily reversible, all hidden exits are at most $2k$, and its nonzero relaxation rates lie in $[k,3k]$. A hidden state of label $j$ uses

$$
b_j(h)=\beta_j^{h/H},\qquad
q_{iA}(h)=kb_j(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_j(h).
\tag{2}
$$

Thus it retains the original exponential rate form with sensitivity
$g_j=1+\log\beta_j/\log2$. All six sensitivities lie in $(-1/2,1/2)$; no centering condition is imposed. Preparation is $\pi_0=(1/2,\mu/2)$ and readout is $S=(-1,1_{\rm hid})$. The passive visible law is exactly the rate-$k$ telegraph law.

A rival has the same visible/hidden structure, preparation convention and binary readout, any finite positive stationary hidden law $\widehat\mu$, and a field-independent hidden generator with exits at most $2k$. At the observed fields it may choose any barriers satisfying

$$
\widehat b_i(0)=1,\qquad 0\le\widehat b_i(H)\le1,
\qquad
\widehat q_{iA}(h)=k\widehat b_i(h),\quad
\widehat q_{Ai}(h)=k\widehat\mu_i e^{2h}\widehat b_i(h).
\tag{3}
$$

One may restrict the endpoint barriers to be strictly positive; the lower also permits zero. Their values between the two fields are irrelevant to the lower. Ordinary reversibility means detailed balance of the hidden generator under its own stationary law. The unrestricted class requires only stationarity.

Let $\mathcal W_{1200}$ be all words in the two propagators for fields $0,H$, each held for $a/k$, containing at most $1200$ letters. Consecutive equal fields may be merged. Their horizons are at most

$$
\frac{1200a}{k}=\frac{150\log2}{k}.
\tag{4}
$$

**Theorem.** The target admits an eleven-total-state stationary predictor with exactly the same controlled means for all bounded protocols and all horizons. Every ordinarily reversible rival obeying (3) with at most eleven total states satisfies

$$
\boxed{
\max_{w\in\mathcal W_{1200}}|m_F(w)-m_{\widehat F}(w)|>\delta_0.}
\tag{5}
$$

Consequently the ordinary reversible minimum at every tolerance $0\le\delta\le\delta_0$ is exactly twelve states, while unrestricted prediction needs at most eleven. The latter is a sufficient count, not a minimality claim. A finite-entropy-production eleven-state predictor at error at most $\delta_0/2$ is also given in Section 8.

## 2. A reversible incidence-graph target

Work in units $k=1$ until physical times are restored. Let $\mathcal V=\{1,\ldots,5\}$ be the vertices of the complete bipartite graph $K_{2,3}$, with parts $\{1,2\}$ and $\{3,4,5\}$. Its six edges form $\mathcal E$. Write

$$
d=(3,3,2,2,2),\qquad w_i=d_i/12.
\tag{6}
$$

The target hidden states are six memory states $e\in\mathcal E$ and five probe states $p_i$, with stationary masses

$$
\mu_T(e)=1/12,\qquad \mu_T(p_i)=d_i/24=w_i/2.
\tag{7}
$$

Every memory state has label $0$; probe $p_i$ has label $i$. Define a rate-one incidence walk by

$$
K_T^0(e,p_i)=1/2\quad(i\in e),\qquad
K_T^0(p_i,e)=1/d_i\quad(i\in e),
\tag{8}
$$

with no other off-diagonal rates and row-sum-zero diagonals. Add rate-one refresh separately within the memory block and within the probe block, to their conditional stationary laws: uniform on the six memory states, and $w$ on the probes. Denote this block refresh generator by $J_T-I$, where $J_T$ redraws from the current block. The target hidden generator is

$$
K_T=K_T^0+J_T-I.
\tag{9}
$$

Detailed balance holds on each incidence edge because both stationary fluxes equal $1/24$, and holds for each conditional refresh. Every exit is at most two. The incidence graph is connected, so the hidden generator is irreducible.

For the relaxation band, the rate-one incidence walk has spectrum of $-K_T^0$ in $[0,2]$. The two-dimensional subspace of functions constant on each block is invariant: its relaxation rates are $0,2$, and the refresh vanishes there. The orthogonal complement is invariant by selfadjointness, and $J_T-I=-I$ on it. Its relaxation rates therefore lie in $[1,3]$. This proves the advertised target band. A global refresh is not used: it would fill the cross-block zeros needed below.

## 3. An exact eleven-state nonreversible predictor

The predictor has five memory states $m_i$ and the same five probes $p_i$, with

$$
\mu_R(m_i)=\mu_R(p_i)=d_i/24.
\tag{10}
$$

All memories have label $0$, and probe $p_i$ has label $i$. Its incidence part is

$$
\begin{aligned}
K_R^0(m_i,p_i)&=1,\\
K_R^0(p_j,m_j)&=1/2,\\
K_R^0(p_j,m_i)&=1/(2d_j)\quad\text{if }\{i,j\}\in\mathcal E,
\end{aligned}
\tag{11}
$$

with the other off-diagonal rates zero. Add rate-one conditional refresh within each of its two five-state blocks, both using $w$. Call the resulting generator $K_R$; it also has exits at most two.

Define an $11\times10$ stochastic matrix $C$ from target hidden states to predictor hidden states by

$$
C(e,m_i)=1/2\quad(i\in e),\qquad C(p_i,p_i)=1,
\tag{12}
$$

with all other entries zero. Direct multiplication gives

$$
C1=1,\qquad \mu_TC=\mu_R,\qquad K_TC=CK_R.
\tag{13}
$$

For an edge row, (13) just averages its endpoint-memory rows. For a probe row, the two-step incidence weights are $1/2$ at its own memory vertex and $1/(2d_j)$ at each neighboring memory vertex, exactly (11). Conditional refreshes also intertwine because $C$ pushes each target conditional law to the corresponding predictor law. Stationarity of $\mu_R$ follows from (13).

The predictor is not ordinarily reversible: for adjacent distinct vertices $i,j$, the rate $p_j\to m_i$ is positive while $m_i\to p_j$ is zero. Conditional block refresh adds no such cross-block reverse edge.

The smaller memory has a direct interpretation. When the target enters an edge-memory state, its next incidence jump chooses one of the two endpoint probes uniformly. The predictor stores that endpoint in advance. From probe $p_j$, first choosing an incident edge and then its endpoint gives probability $1/2$ of returning to $p_j$ and $1/(2d_j)$ of reaching each neighbor, exactly (11). A memory-block refresh redraws this stored endpoint with law $w$. All memory states have the same kinetic barrier, so a field-dependent return to $A$ can interrupt this plan without distinguishing its hidden alternatives. The endpoint is sampled using present transition probabilities; no future field, future observation or uncounted memory is supplied.

Let $B_T(h)$ and $B_R(h)$ be the diagonal barrier matrices. Each mixed row of $C$ stays within label $0$, so

$$
B_T(h)C=CB_R(h)
\tag{14}
$$

for every field, not just the two queried values. Extend $C$ by fixing the visible state, writing $\widetilde C=\operatorname{diag}(1,C)$. Equations (13)–(14) imply for the full physical generators, preparations and readouts

$$
Q_T(h)\widetilde C=\widetilde C Q_R(h),\qquad
\pi_T\widetilde C=\pi_R,\qquad
S_T=\widetilde C S_R.
\tag{15}
$$

The outgoing visible rate agrees because the barrier histograms agree. Passing $\widetilde C$ successively through any product of propagators proves exact equality of every controlled mean. Bounded time-dependent protocols follow by the usual piecewise-constant approximation. No target coordinate is supplied to an external predictor; all ten hidden predictor coordinates are counted.

## 4. Ten positive observable features

For a target or rival, let $J=e_Ae_A^{\mathsf T}$ and $H_0=I-J$. Extend hidden operators by zero at $A$. In units $k=1$, the two full generators recover the hidden barrier multiplication and hidden generator by

$$
B=H_0+H_0(Q_0-Q_H)H_0,\qquad
K=H_0Q_0H_0+H_0.
\tag{16}
$$

For the six grid points (1), put

$$
L_j(x)=\prod_{r\ne j}\frac{x-\beta_r}{\beta_j-\beta_r},\qquad
A_j=L_j(B)^2\quad(0\le j\le5),
\tag{17}
$$

using $H_0$ for the polynomial constant term. Each $A_j$ is a nonnegative diagonal kernel on every rival, including off-grid barriers. On the target it is exactly the corresponding label projector. The common cap makes

$$
P=H_0+K/2
\tag{18}
$$

a positive Markov kernel on the hidden block. It is selfadjoint in an ordinary reversible rival.

Define ten feature operators and their vectors by

$$
F_i=2A_0PA_i,\quad F_{5+i}=A_i\quad(1\le i\le5),
\qquad f_j=F_j1\quad(1\le j\le10).
\tag{19}
$$

Every feature is pointwise nonnegative in every rival. On the target, $f_i(e)=1/2$ when $i\in e$ and zero elsewhere, while $f_{5+i}$ is the indicator of probe $p_i$. The block refresh in (9) creates no additional memory-to-probe transitions.

Their hidden stationary Gram matrix is

$$
G_T=\bigl[\langle f_i,f_j\rangle_{\mu_T}\bigr]_{i,j=1}^{10}
=\operatorname{diag}\left(H,\operatorname{diag}(d_i/24)\right),
$$
$$
H=\frac1{48}
\begin{pmatrix}3I_2&\mathbf1_{2\times3}\\
\mathbf1_{3\times2}&2I_3\end{pmatrix}.
\tag{20}
$$

In an ordinary reversible rival, every Gram entry is an observable generator/projector polynomial scalar:

$$
\langle F_i1,F_j1\rangle_{\widehat\mu}
=2\widehat\pi_0 F_i^*F_j\widehat S.
\tag{21}
$$

The adjoint reverses the selfadjoint hidden factors $A_j,P$. Thus its polynomial expression is specified in the same way in both models. No new initial law, hidden readout or physical adjoint operation is introduced.

## 5. A robust eleven-atom obstruction

A Gram matrix of ten nonnegative functions on $D_h$ hidden states has the form

$$
\widehat G=\sum_{s=1}^{D_h}x_sx_s^{\mathsf T},\qquad x_s\ge0,
\tag{22}
$$

where $x_s(i)=\sqrt{\widehat\mu_s}\,f_i(s)$. Such a factorization is called completely positive. Only its elementary nonnegative-atom form is needed here.

The support graph of (20) has six edges forming $K_{2,3}$ on the first five coordinates, and five isolated coordinates with positive diagonal. Select these six edge entries and five isolated diagonal entries as eleven witnesses. Every selected target entry is at least $c=1/48$, and every target diagonal is at most $M_0=1/8$.

**Finite Gram lemma.** If $D_h\le10$, then

$$
\boxed{\|\widehat G-G_T\|_{\max}>\varepsilon_0,
\qquad \varepsilon_0=1/40000.}
\tag{23}
$$

To prove this, suppose the entrywise error is at most $\varepsilon_0$. Each witness is a sum of at most ten nonnegative atom contributions, so assign to it an atom contributing at least $(c-\varepsilon_0)/10$. Every coordinate of every atom is at most $\sqrt{M_0+\varepsilon_0}$. For an edge witness, each of its two endpoint coordinates in the assigned atom is therefore at least

$$
L=\frac{c-\varepsilon_0}{10\sqrt{M_0+\varepsilon_0}}.
$$

For an isolated diagonal witness, its assigned coordinate is at least $\sqrt{(c-\varepsilon_0)/10}\ge L$. Two of the eleven witnesses must be assigned to the same atom. The union of any two distinct witness supports contains a target off-diagonal zero: $K_{2,3}$ is triangle-free, and the last five coordinates are isolated. That atom then contributes at least $L^2$ to a target-zero entry. But

$$
\varepsilon_0\,100(M_0+\varepsilon_0)
=\frac{5001}{16000000}
<\frac{6235009}{14400000000}
=(c-\varepsilon_0)^2,
\tag{24}
$$

so $L^2>\varepsilon_0$, a contradiction. No lower bound on rival stationary masses or feature values is assumed. At exact agreement the same support argument says that (20) needs at least eleven nonnegative atoms.

## 6. Explicit controlled-mean recovery budget

This section applies to the target and every ordinary reversible rival under (3). At zero the full exit cap is three; at $H=\log2$ the hidden exits are at most three and the visible exit is $4\sum_i\mu_i b_i(H)\le4$. Full reversibility therefore gives spectral cap eight at both fields. With the clock in (1),

$$
\rho=1-e^{-8a}=1/2,\qquad \varrho=3/2,\qquad
\chi=e^H=2.
\tag{25}
$$

The [whole-side capped transfer](CAPPED_KINETIC_INTERFACE_SEPARATION.md#4-uniform-capped-clock-transfer-with-projector-insertions) applies with

$$
C_a=\max\left\{1,\frac\chi a\log\frac1{1-\varrho\rho},
\frac{\log2}{a}\right\}=32,
\qquad C_H=1+2(1+\coth H)=19/3<7.
\tag{26}
$$

For clarity, it substitutes the logarithm series into the **entire generator polynomial**, attaches a bookkeeping degree to each series term, and truncates at total degree $N$. It does not truncate each generator letter independently at degree $N$. Consequently a polynomial of generator degree $d$ and coefficient mass $J_{\mathcal P}$ obeys

$$
|\pi_0\mathcal P S-\widehat\pi_0\widehat{\mathcal P}\widehat S|
\le J_{\mathcal P}32^d
\left[2(2/3)^{N+1}+4^N(1+7N)\delta\right]
\tag{27}
$$

when all clock means through $N$ ticks agree within $\delta$. The finite visible-state preparation recursion reconstructs all inserted $J$ factors. Their number introduces no additional horizon: each observed word has at most $N$ propagator letters. This is precisely the total-degree majorant and inserted-word estimate proved in the linked note.

Here are sufficient coefficient bounds after expanding $H_0=I-J$. Equation (16) gives mass at most ten for $B$ and mass two for $H_0$. Each factor $B-\beta_rH_0$ has mass at most twelve. The minimum denominator product in (17) is

$$
\min_j\prod_{r\ne j}|\beta_j-\beta_r|=12/16^5.
$$

Thus

$$
\|L_j(B)\|_{\mathrm{coeff},1}
\le12^4 16^5=81\,2^{28}<2^{35},\qquad
\|A_j\|_{\mathrm{coeff},1}<2^{70},\quad \deg A_j\le10.
\tag{28}
$$

Also $P=(3/2)H_0+(1/2)H_0Q_0H_0$ has mass at most five and degree one. The feature operators in (19) therefore have degree at most $21$ and mass at most $2^{144}$. The full Gram polynomial $\mathcal P_{ij}=2F_i^*F_j$ has

$$
d\le42,\qquad J_{\mathcal P}\le2^{289},\qquad
J_{\mathcal P}32^d\le2^{499}.
\tag{29}
$$

Take $N=1200$ and $\delta=\delta_0=2^{-3000}$. Since $(2/3)^2<1/2$ and $1+7N=8401<2^{14}$, (27)–(29) give

$$
\max_{i,j}|(G_T)_{ij}-(\widehat G)_{ij}|
\le2^{499}\left[2(2/3)^{1201}
+2^{2400}\,8401\,2^{-3000}\right]
<2^{-100}+2^{-87}<\frac1{40000}.
\tag{30}
$$

## 7. Completion of the finite separation

An eleven-total-state rival has at most ten hidden states. Its positive features have at most ten Gram atoms by (22). If it were ordinarily reversible and matched all means in $\mathcal W_{1200}$ to error at most $\delta_0$, (30) would contradict (23). This proves (5). The target itself is a twelve-state admissible ordinary reversible model, so its ordinary minimum at this tolerance is exactly twelve. Section 3 supplies the exact eleven-state unrestricted predictor.

The lower covers arbitrary new rival states, stationary masses and endpoint barriers throughout $[0,1]$. It is not an aggregation lower, a fit against a selected list of candidates, or an inference from a rank threshold alone. The finite Gram lemma is where ordinary reversibility produces an additional positive-factorization constraint beyond the unrestricted realization.

## 8. A finite-entropy-production eleven-state predictor

The exact predictor in Section 3 has one-way edges and infinite ordinary stationary entropy production. This infinity is unnecessary for a finite-error advantage. Its original-rule sensitivity bound may be taken as

$$
G=\log_2(11/8),\qquad R=e^{(1+G)H}=11/4.
$$

Let $K_R^*$ be its stationary reverse and define

$$
K_{R,\eta}=(1-\eta)K_R+\eta K_R^*,\qquad
\eta=\delta_0/22.
\tag{31}
$$

It preserves the ten hidden states, stationary law, labels and every exit rate. The [common-reset perturbation bound](ENTROPY_PRODUCTION_REVERSIBILIZATION.md#5-finite-entropy-production-for-a-bounded-rate-predictor), with hidden exit cap $B=2$, gives mean change uniformly over protocols with $|h(t)|\le H=\log2$ and all horizons at most

$$
2BR\eta=11\eta=\delta_0/2.
\tag{32}
$$

Its full zero-field identity-reversal entropy-production rate is finite and obeys

$$
\sigma_0\le\frac{Bk}{2}\log\frac{1-\eta}{\eta}
\le k\log\frac{22}{\delta_0}.
\tag{33}
$$

Thus the same eleven-state budget attains error at most $\delta_0/2$ with finite ordinary entropy production, while every ordinary reversible eleven-state rival has error greater than $\delta_0$. No generalized-reversal or device-level heat assertion is needed for this conclusion.

## 9. Exact extension to complete bipartite incidence graphs

The same construction gives an exact family of comparisons without a fixed alphabet-size claim. For positive integers $p,q$, use $K_{p,q}$ and put $E=pq$, $V=p+q$. Use $E$ memory edges of mass $1/(2E)$, $V$ probe vertices of mass $d_i/(4E)$, the same incidence rates $1/2$ and $1/d_i$, and the same rate-one conditional block refreshes. Endpoint barriers may be chosen as

$$
\beta_j=\frac38+\frac{5j}{16V}\quad(0\le j\le V),
$$

with common memory label $0$ and distinct probe labels $1,\ldots,V$. Their original-rule sensitivities remain in $(-1/2,1/2)$. The endpoint-mixture intertwiner gives a stationary exact predictor with $2V$ hidden states. The target has $E+V$ hidden states, exits at most two and hidden band $[1,3]$ by the same block decomposition.

The $2V$ positive features have a target Gram with $E$ nonzero triangle-free edge witnesses and $V$ isolated positive diagonal witnesses. Exact agreement therefore forces at least $E+V$ nonnegative atoms in an ordinary reversible rival. Exact controlled means determine these Gram scalars by the capped clock calculus: for each fixed $p,q$, let its total-degree cutoff tend to infinity at zero mean discrepancy. Hence

$$
D_{\rm id}(0)=pq+p+q+1,\qquad
D_{\rm all}(0)\le2(p+q)+1.
\tag{34}
$$

For $p=q=m\ge3$, these counts are quadratic versus linear in $m$. The target alphabet has $2m+1$ values, and the predictor's displayed count is only an upper bound. This is an exact realization corollary; no alphabet-independent law or practical uniform positive-error tolerance is asserted. The explicit finite-error statement of this note remains the $K_{2,3}$ theorem (5).

## 10. Interpretation and limits

The finite example establishes a genuine one-state advantage with explicit analytic witnesses. Its target is a small reversible incidence-and-refresh network with six kinetic labels, and its hidden relaxation band remains $[k,3k]$. Its eleven-state predictor preserves the target's complete kinetic histogram even though the lower does not require rivals to do so.

The tolerance $2^{-3000}$ is deliberately conservative and far beyond practical resolution. The collection of witnessing protocols is finite but potentially enormous; neither its sample cost nor an efficient experiment-selection scheme is supplied. A useful-tolerance certificate remains an open improvement. The ordinary-versus-unrestricted distinction must also be kept separate from the existing generalized-reversal upper theorem.

Nonnegative Gram factorizations, triangle-free support bounds and Markov intertwinings are established mathematical tools. The new claim is their concrete controlled-mean realization and explicit finite state comparison under the stated common interface and rate budget. Small exact checks can validate its matrices and inequalities; the arbitrary-rival quantifier is supplied by the analytic positivity, clock-recovery and atom-count proof. Manuscript drafting remains deferred.
