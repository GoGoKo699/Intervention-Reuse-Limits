# Finite-state closure under arbitrarily fast reversible rates

[Repository overview](../README.md) · [Uniform rate regularization](RATE_REGULARIZATION.md) · [Original model](THEORY.md)

**Working closure theorem, 23 September 2026.** At a fixed physical state count, the original-rule reversible family has compact closure in the norm of its actual controlled mean, uniformly over every bounded protocol and all horizons. Boundary models have a finite reversible hidden generator and probability distributions of actuator labels on their hidden states. Their external rate factors are averages of exponentials. The total number of constituent actuator atoms, before collapsing those distributions, remains bounded by the original hidden state count.

This theorem supplies a representation of the fast-rate boundary, including sequences with vanishing stationary masses. For $H>0$ and a fixed alphabet contained in $(-1,1)$, exact agreement with a scalar-actuator target forces its boundary clusters to carry single actuator labels. Combined with the nineteen-level entropy argument, this gives a positive uncapped prediction-error floor at each fixed target size and insufficient fixed state budget. The results are qualitative: no modulus of convergence or quantitative inverse-error state lower bound is claimed.

## Model and comparison norm

A row generator acts on column functions. There is one visible state $A$ and a finite hidden space. The hidden generator $K$ is reversible under a positive probability vector $\mu$. Fix $k>0$, an actuator bound $G$, a field bound $H$, and a finite actuator alphabet with a prescribed probability histogram. Every model retains that histogram and the rates

$$
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{iA}(h)=k e^{(g_i-1)h}.
$$

Preparation is $\pi_0=(1/2,\mu/2)$, and the readout $s$ is $-1$ at $A$ and $+1$ on hidden states. Let $m_F[h](t)$ be the actual mean under a deterministic piecewise continuous protocol with $|h|\le H$. The comparison metric on response functions is

$$
d(F,\widehat F)=\sup_{h,t\ge0}
\left|m_F[h](t)-m_{\widehat F}[h](t)\right|.
$$

Distinct physical models can have distance zero. Compactness below refers to their response functions, or equivalently to models modulo this equivalence. Set $R=e^{(1+G)H}$ and $\alpha=k/R$.

## Closure theorem

Consider an arbitrary sequence of reversible original-rule models with at most $D$ hidden states and arbitrary finite internal rates. Passing to a subsequence, assume a fixed number $d\le D$ of states and a fixed label $g_i$ at each index. This uses finiteness of the label alphabet. Extract $\mu_n\to\mu$ in the closed simplex, and let $I=\{i:\mu_i>0\}$ and $Z=\{i:\mu_i=0\}$. The histogram constraint passes to the limit.

**Theorem.** A further subsequence converges in the uniform controlled-mean metric to a finite reversible model whose hidden states are clusters $C$ partitioning $I$. A cluster carries a probability measure $\nu_C$ on actuator values. Its rates are

$$
q_{A C}(h)=k\mu_C e^h\phi_C(h),\qquad
q_{C A}(h)=k e^{-h}\phi_C(h),
$$

$$
\mu_C=\sum_{i\in C}\mu_i,\qquad
\phi_C(h)=\int e^{gh}\,d\nu_C(g)
=\frac1{\mu_C}\sum_{i\in C}\mu_i e^{g_i h}.
\tag{1}
$$

The reduced internal generator is finite and reversible under the cluster masses $\mu_C$. It may be reducible. The full chain remains irreducible because $A$ connects to every positive-mass cluster. The exact actuator histogram survives as the mixture identity

$$
\sum_C\mu_C\nu_C=\sum_i\mu_i\delta_{g_i}.
\tag{2}
$$

There are at most $D$ clusters and at most $D$ constituent atoms before merging identical labels within a cluster. If $D$ denotes total physical states instead, replace $D$ by $D-1$ throughout this statement.

### 1. Spectral subsequence and zero-mass states

Define symmetric positive semidefinite matrices

$$
H_n=-\operatorname{diag}(\sqrt{\mu_n})K_n
\operatorname{diag}(1/\sqrt{\mu_n}).
$$

Choose orthonormal eigenbases and ordered eigenvalues. Compactness of the orthogonal group and of the extended interval $[0,\infty]$ gives a subsequence on which each eigenvector $v_{n,j}$ converges to $v_j$ and each eigenvalue $\lambda_{n,j}$ converges in $[0,\infty]$. Therefore, for each $t>0$,

$$
S_n(t)=e^{-tH_n}\longrightarrow
S_\infty(t)=\sum_{\lambda_j<\infty}e^{-t\lambda_j}v_jv_j^T.
\tag{3}
$$

The limit is nonnegative entrywise, symmetric, contractive, and satisfies $S_\infty(t+s)=S_\infty(t)S_\infty(s)$. It fixes $\sqrt\mu$. It can be discontinuous at $t=0$ as an operator on the original space; its right limit there is the orthogonal projection onto the finite-eigenvalue space.

States with vanishing $\mu_i$ must not be discarded before taking this limit. They can mediate finite effective rates. Nevertheless their eventual decoupling from positive-mass coordinates follows directly from detailed balance. If $i\in I$ and $j\in Z$, write $P_n(t)=e^{tK_n}$. Then

$$
0\le(S_n(t))_{ij}
=\sqrt{\frac{\mu_{n,i}}{\mu_{n,j}}}(P_n(t))_{ij}
=\sqrt{\frac{\mu_{n,j}}{\mu_{n,i}}}(P_n(t))_{ji}
\le\sqrt{\frac{\mu_{n,j}}{\mu_{n,i}}}\longrightarrow0,
\tag{4}
$$

uniformly in $t\ge0$. Thus $S_\infty$ is block diagonal between $I$ and $Z$. Any effective influence of $Z$ on $I$ has already been retained in the limiting $I$ block. The $Z$ block carries no limiting preparation or observation weight. We retain it through the full-space semigroup and Dyson convergence below, and remove it only after proving that it decouples from the limiting scalar mean.

### 2. The instantaneous projection is conditional expectation

On $I$ define

$$
P_\infty(t)=\operatorname{diag}(1/\sqrt{\mu_I})
(S_\infty(t))_{II}\operatorname{diag}(\sqrt{\mu_I}).
$$

This is a stochastic reversible semigroup for $t>0$. Its limit $E$ as $t$ decreases to zero is a nonnegative stochastic matrix, reversible under the strictly positive weights $\mu_I$, and $E^2=E$. Equivalently it is an orthogonal projection in $L^2(\mu_I)$.

For completeness, its partition structure follows from elementary finite Markov theory. Reversibility makes positive off-diagonal support symmetric. Thus the connected components $C$ of its support graph are closed, and each restricted stochastic matrix $E_C$ is irreducible. Irreducibility makes its eigenvalue one simple (for example, the maximum principle shows every fixed function is constant on a component). Idempotence forces every eigenvalue to be zero or one, and symmetry gives diagonalizability; hence each $E_C$ has rank one. Its fixed stationary law is the conditional $\mu$ distribution. Consequently

$$
(Ef)_i=\frac1{\mu_C}\sum_{j\in C}\mu_j f_j
\quad(i\in C).
\tag{5}
$$

This proves that $E$ is conditional expectation onto an actual partition, without presupposing a partition architecture for the finite-rate rivals.

The restricted semigroup on $\operatorname{ran}E$ is strongly continuous at zero and acts on a finite-dimensional space. Its cluster-coordinate matrices are stochastic and reversible. Differentiating at zero gives a finite reversible Markov generator $L$ on the clusters; positivity at $t\ge0$ makes every off-diagonal derivative nonnegative. All its eigenvalues are finite by construction.

### 3. Uniform control convergence, including arbitrarily fast switching

Use Euclidean normalized density coordinates $x=\operatorname{diag}(\sqrt{\pi_0})\rho$, where $\rho$ is the probability density relative to $\pi_0$. Thus preparation is $a=\sqrt{\pi_0}$, and the mean readout vector is $b=\operatorname{diag}(\sqrt{\pi_0})s$. Both vectors converge as $n\to\infty$, vanish on $Z$ in the limit, and belong to the normalized cluster-constant subspace.

The full zero-field semigroups $T_{0,n}$, conjugated into these coordinates, have a pointwise limit for $t>0$ by (3). The external zero-field operator preserves the span of $A$ and $\sqrt{\mu_n}$, where the internal operator vanishes, and acts as $-kI$ on hidden centered vectors. On that orthogonal hidden subspace the full zero-field semigroup is $e^{-kt}S_n(t)$. The visible two-dimensional block has fixed eigenvalues $0$ and $-2k$. Thus $T_{0,n}(t)\to T_{0,\infty}(t)$ on the full space, including the limiting $Z$ block. On $A\cup I$, its instantaneous projection $\mathcal E$ keeps $A$ separate and is the Euclidean conjugate of $E$ on $I$. The $Z$ block is decoupled but is retained in the operator convergence.

Let $\mathcal V_{n,h}$ denote the normalized forward external perturbation corresponding to $Q_n(h)-Q_{0,n}$. These matrices converge uniformly for $|h|\le H$ to a bounded family $\mathcal V_{\infty,h}$. Indeed their hidden diagonal entries are continuous functions of the fixed labels and $h$, their $A$-hidden entries contain $\sqrt{\mu_{n,i}}$, and their $A$ diagonal contains $\sum_i\mu_{n,i}e^{(1+g_i)h}$. They are uniformly bounded by $B=2k(R-1)$. All entries coupling $A$ or $I$ to $Z$ tend to zero. The surviving $I$-diagonal entries need not preserve $\operatorname{ran}\mathcal E$; their compression $\mathcal E\mathcal V_{\infty,h}\mathcal E$ is therefore essential.

For each finite $T$, dominated convergence gives

$$
\int_0^T\|T_{0,n}(u)-T_{0,\infty}(u)\|\,du\longrightarrow0.
\tag{6}
$$

The possible discrepancy at $u=0$ has measure zero. Expand the finite-horizon evolution in its Dyson series around $T_{0,n}$. The norm of its $r$th term is at most $(BT)^r/r!$, uniformly in the protocol. Write

$$
e_n(T)=\int_0^T\|T_{0,n}(u)-T_{0,\infty}(u)\|\,du,
\qquad
v_n=\sup_{|h|\le H}\|\mathcal V_{n,h}-\mathcal V_{\infty,h}\|.
$$

For $r\ge1$, telescoping the $r+1$ semigroup factors and $r$ perturbation factors bounds the difference of the corresponding operator terms, uniformly for $t\le T$, by

$$
(r+1)B^r\frac{T^{r-1}}{(r-1)!}e_n(T)
+rB^{r-1}\frac{T^r}{r!}v_n.
$$

For each semigroup gap, the remaining simplex volume is at most $T^{r-1}/(r-1)!$, including the two endpoint gaps. This proves the bound using only integrated semigroup convergence, without regularity of the protocol. The $r=0$ term fixes preparation exactly and has no boundary layer. Since preparation and readout vectors have norm one, summing the series gives

$$
\begin{aligned}
\sup_{h,\,t\le T}|m_n[h](t)-m_\infty[h](t)|
\le e^{BT}\bigl[&\|a_n-a_\infty\|+\|b_n-b_\infty\|\\
&+B(BT+2)e_n(T)+Tv_n\bigr].
\end{aligned}
$$

Every term on the right tends to zero. This proves uniform convergence of means on $[0,T]$, including protocols depending on $n$ or switching arbitrarily rapidly.

In the full limiting Dyson products, both the semigroup and the perturbations are block diagonal between $A\cup I$ and $Z$. Since the limiting preparation and readout vanish on $Z$, that block contributes zero to the mean and may now be discarded. On $A\cup I$, every positive-time semigroup factor projects onto $\operatorname{ran}\mathcal E$. Therefore the surviving normalized dynamics consists of the reduced zero-field generator plus $\mathcal E\mathcal V_{\infty,h}\mathcal E$. Transforming to cluster coordinates and applying (5) gives exactly (1), with the internal generator $L$ described above. Preparation and readout become the ordinary zero-field preparation and binary readout of this reduced model.

Finally every original model and the reduced mixture model has hidden-to-$A$ rate at least $\alpha$. For $t>T$, restart each model at its own zero-field preparation at time $t-T$ and reuse the final protocol segment. Each restart changes its final mean by at most $2e^{-\alpha T}$, by the common-reset contraction. Consequently

$$
\sup_{h,t\ge0}|m_n[h](t)-m_\infty[h](t)|
\le4e^{-\alpha T}
+\sup_{h,0\le t\le T}|m_n[h](t)-m_\infty[h](t)|.
\tag{7}
$$

Choose $T$ large, then $n$ large. This proves convergence in the full all-horizon controlled-mean metric.

### 4. Why the boundary is larger than the original scalar rule

For a cluster with mixed actuator values, $\phi_C(h)$ is a sum of exponentials. If $\phi_C(h)=e^{g_Ch}$ on any interval around zero, its first two derivatives imply

$$
\mathbb E_{\nu_C}g=g_C,\qquad
\mathbb E_{\nu_C}g^2=g_C^2,
$$

so $\operatorname{Var}_{\nu_C}(g)=0$. Thus a mixed cluster generally lies outside the original scalar-actuator rate rule, even though it remains reversible at every fixed field and preserves the histogram as (2). Binary labels also allow mixed clusters: $\phi_C(h)=p_Ce^{\gamma h}+(1-p_C)e^{-\gamma h}$.

Conversely, a finite cluster model of this form with at most $D$ constituent atoms is a limit of original-rule models with at most $D$ hidden states. Disaggregate each cluster according to its atom masses. Lift every intercluster transition $C\to C'$ by choosing the destination atom according to $\nu_{C'}$, and add independent within-cluster refresh at rate $M$. The cross-cluster detailed-balance flux is $\mu_C\nu_C(i)L_{CC'}\nu_{C'}(j)$, which is symmetric under exchanging endpoints. The resulting internal generator is reversible under the stationary atom weights. As $M\to\infty$, its fast limit is the prescribed cluster model. If necessary, add independent global $\mu$ refresh at a rate tending to zero to make the hidden generator irreducible. The same semigroup, Dyson and reset argument proves controlled-mean convergence. Hence these mixture-cluster systems describe precisely the finite-$D$ closure, with the constituent-atom budget retained.

## Exact agreement forces pure actuator clusters

Assume $H>0$, the fixed actuator alphabet $\Gamma$ lies in $(-1,1)$, as in both separation constructions, and let $f_\gamma$ be its prescribed histogram. Suppose a finite mixture-cluster model agrees exactly with a scalar-actuator target on every actual-mean experiment. Write

$$
p_{C\gamma}=\nu_C(\{\gamma\}),\qquad
\sum_C\mu_Cp_{C\gamma}=f_\gamma.
\tag{8}
$$

**Purity proposition.** Every positive-mass cluster has one actuator label: all $p_{C\gamma}$ are zero or one. This also follows from exact agreement on a fixed identifiable finite field menu at any fixed positive clock, with no bound on the finite internal rates of the two models.

**Proof.** The mixture generator has the same frequency decomposition as a scalar-actuator generator,

$$
Q(h)=K_b+\sum_{\gamma\in\Gamma}e^{(1+\gamma)h}X_\gamma
       +\sum_{\gamma\in\Gamma}e^{(\gamma-1)h}Y_\gamma.
\tag{9}
$$

Here $X_\gamma$ has visible-to-cluster entries $\mu_Cp_{C\gamma}$, together with the corresponding visible diagonal, while $Y_\gamma$ has hidden row $p_{C\gamma}(e_A^T-e_C^T)$. Units may be fixed by $k=1$. The frequencies $0,1+\gamma,\gamma-1$ are distinct because $\Gamma\subset(-1,1)$. The exponential Vandermonde argument therefore recovers every $Y_\gamma$ as the same linear combination of finitely many physical generators in both models. For example, take $2|\Gamma|+1$ equally spaced fields in a nontrivial interval inside $[-H,H]$.

Exact full-protocol agreement implies equality of all generator-word scalars by differentiating finite-dimensional semigroup products in their segment durations at zero. For the stated fixed-clock version, use the separate convergent logarithm series for $e^{aQ(h)}$ in each finite model. Each model has finite spectra on the finite menu, so its series converges in operator norm. Every truncated expression is a finite linear combination of legal fixed-clock propagator words. Exact mean agreement gives equality for every truncation, then for its generator-word limit. This argument uses no uniform rate bound across the model class.

Put $B_0=\sum_\gamma Y_\gamma$. On functions vanishing at $A$, $D_\gamma=-Y_\gamma$ is multiplication by $p_{C\gamma}$; it is not yet asserted to be a projector. The actual preparation and readout satisfy

$$
B_0s=-2\,1_{\rm hid},\qquad
\pi_0B_0=(1/2,-\mu/2).
$$

Consequently the observable physical polynomial scalar is

$$
\pi_0B_0D_\gamma^2B_0s
=\sum_C\mu_Cp_{C\gamma}^2.
\tag{10}
$$

In the scalar-actuator target, its value is $f_\gamma$. Equality of the physical generator-word scalars and the histogram identity (8) give

$$
\sum_C\mu_Cp_{C\gamma}(1-p_{C\gamma})=0.
\tag{11}
$$

Every summand is nonnegative and every retained $\mu_C$ is positive. Hence each $p_{C\gamma}$ is zero or one; their sum over $\gamma$ is one. The boundary model therefore satisfies the original scalar-actuator rule after all. $\square$

The identities above use the original preparation, readout and physical fields. They introduce no cluster-specific preparation or additional actuator.

## A qualitative uncapped error floor for the nineteen-level targets

Fix target $n$ from the [nineteen-level construction](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md), let $r=2^n$, and fix an integer hidden-state budget $D<2^r$. Then

$$
\inf_{\substack{F\text{ reversible original-rule rival}\\
\#\text{hidden states}(F)\le D}}
\sup_{h,t\ge0}|m_F[h](t)-m_n[h](t)|>0,
\tag{12}
$$

without an internal rate cap. The rival has the prescribed exact histogram, preparation and readout. The statement also holds when the supremum is restricted to the nineteen-level theorem's thirty-nine-field menu and segment lengths that are integer multiples of any fixed positive clock.

To prove this, suppose the infimum were zero. Compactness supplies a limiting mixture-cluster model with at most $D$ clusters, retaining the constituent-atom budget, whose means agree exactly with the target. The purity proposition makes this an original-rule scalar-actuator model. Its cross-port kernels $16D_cK_bD_d$ are nonnegative because the ports are disjoint, irrespective of the size of its finite rates. Exact generator-word agreement supplies every scalar hypothesis of the [whole-word entropy lemma](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) with $\Delta=0$. That lemma gives $H(Z)\ge r$ on its own central stationary state space. Thus it has at least $2^r$ central states, contradicting its total hidden budget $D<2^r$.

For the fixed-clock version, restriction of response functions to those experiments is continuous because its supremum distance is no larger than the full distance. The restricted image of the compact closure is therefore compact. Exact agreement in that image is excluded by the fixed-clock purity argument and the same zero-defect entropy argument. Its distance from the target is consequently positive as well.

The positive number in (12) can depend on $n,D,H,k$ and the chosen clock; this proof supplies no useful bound on that dependence. In particular, (12) does not establish a growth law of the form $\exp(c\delta^{-\alpha})$ for uncapped reversible prediction. It establishes robustness at each fixed target and state budget, beyond excluding exact finite-rate realizations. If states are counted physically including $A$, the condition is $D_{\rm total}-1<2^r$.

## Scope

The closure description includes reducible hidden generators, because irreducibility need not survive a limit; the full chain remains connected through $A$. It includes instantaneous equilibration inside clusters, represented by their actuator distributions. It does not retain a lower internal spectral gap.

A target outside this compact closure has strictly positive distance from all original-rule rivals with the prescribed state budget. The purity proposition supplies the missing reduction from mixture boundary models to scalar-actuator models for exact agreement, and the nineteen-level application supplies one such exclusion. Compactness gives no quantitative relation between that positive distance and the state budget. The [uniform rate-regularization bound](RATE_REGULARIZATION.md) is a separate quantitative approximation statement; its cap grows with inverse accuracy.

This corollary does not establish a separation between reversible and unrestricted rivals; no matching smaller unrestricted realization at its unknown tolerance is established.
