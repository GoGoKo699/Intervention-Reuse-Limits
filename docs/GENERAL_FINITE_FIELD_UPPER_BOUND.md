# A finite-state upper bound for every bounded-sensitivity target

[Repository overview](../README.md) · [Finite-field theorem for the canonical subclass](FINITE_FIELD.md) · [Original model](THEORY.md)

**Working extension, 22 September 2026.** Every finite target in the original reversible family admits a finite-state approximation of its exact field-on mean, uniformly over all bounded protocols and all horizons, with a state bound independent of microscopic size and internal rates. The construction below gives a large, explicit bound. Its internal surrogate dynamics are generally nonreversible. This is an existence theorem, not an efficient algorithm or a sharp state-complexity result. In particular, it does not extend the canonical subclass's $\Theta(\log^2(1/\varepsilon))$ theorem to the general family.

The construction combines established uniformization and canonical finite-order Markov approximation with the model's common reset and a reversible semigroup estimate. The [prior-art comparison](PRIOR_ART.md) attributes those ingredients; this note does not claim either classical construction as new.

## 1. Statement and an explicit bound

Fix $k>0$, $G>0$, $H>0$, and an error tolerance $0<\varepsilon<1$. The target is any member of the [original model](THEORY.md), with arbitrary finite hidden size, irreducible reversible internal generator $K$, stationary law $\mu$, centered sensitivity $g$, and $|g_j|\le G$. The constructor knows the full target.

There is an autonomous finite-state Markov surrogate with a fixed binary readout, zero-field stationary preparation, analytic instantaneous-field rates, and sensitivity bounded by the **same** $G$, such that

$$
\sup_{T>0}\ \sup_{|h|\le H}\ \sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|\le\varepsilon.
\tag{1}
$$

Protocols are deterministic and piecewise continuous. The surrogate retains the exact passive telegraph law, equilibrium mean $\tanh h$, reference linear mean response, and identically zero quadratic mean response. Its internal generator need not be reversible. Its sensitivity variance need not equal the target's $W$ exactly, but the construction makes its variance differ by at most $\eta^2$, with $\eta$ below.

Rescale time by $k$, so the rest of the proof uses $k=1$. Define

$$
R=e^{(1+G)H},\qquad \alpha=R^{-1},\qquad B=2(R-1),
$$

$$
\eta=\min\left\{1,G,\frac{\varepsilon}{8HR^2}\right\},
\qquad m=\left\lceil\frac{2G}{\eta}\right\rceil,
\qquad T_*=R\log\frac{16}{\varepsilon}.
$$

Choose

$$
\Delta=\min\left\{\frac{T_*}{2},
\frac{\varepsilon^2}{128B^2 e^{4BT_*}T_*}\right\},
\qquad M=\frac{T_*}{\Delta},
$$

and

$$
\ell=\left\lceil
\frac{M+\log[8(1+RT_*)/\varepsilon]}{\log2}
\right\rceil.
$$

An explicit sufficient total state count is

$$
\boxed{D\le1+m^\ell.}
\tag{2}
$$

The very large size of this bound is intentional: no efficiency or asymptotic optimality is claimed. Its role is to show that bounded sensitivity and bounded field prevent an unbounded microscopic state count from forcing an unbounded state requirement at a fixed mean-prediction tolerance. When $H=0$ or $G=0$, the ordinary two-state model suffices and these formulas are unnecessary.

## 2. Quantize the actuator without changing its mean or bound

Partition $[-G,G]$ into $m$ intervals of width at most $\eta$. On each nonempty interval, replace every $g_j$ by the $\mu$-weighted conditional mean in that interval; call the resulting vector $g^\eta$. Empty intervals are discarded. Then

$$
\|g-g^\eta\|_\infty\le\eta,\qquad
\|g^\eta\|_\infty\le G,\qquad
\langle g^\eta,1\rangle_\mu=0.
$$

Conditional expectation also gives

$$
0\le W-W_\eta
=\langle(g-g^\eta)^2,1\rangle_\mu\le\eta^2.
\tag{3}
$$

Let $F_\eta$ be the target with $g$ replaced by $g^\eta$, leaving $K,\mu$ unchanged. The difference of the two generators has row absolute sum at most $2HR\eta$, uniformly for $|h|\le H$. Every model considered below has a common reset to $A$ of rate at least $\alpha$. Consequently its propagator contracts zero-mass signed measures in total variation norm by $e^{-\alpha(t-s)}$; see [the reset proof](FINITE_FIELD.md#2-a-common-reset-gives-uniform-contraction). Variation of constants therefore gives

$$
\sup_{h,t}|m_F[h](t)-m_{F_\eta}[h](t)|
\le2HR^2\eta\le\frac\varepsilon4.
\tag{4}
$$

This uses genuine stochastic propagators, not a perturbation expansion in the applied field.

## 3. Replace arbitrarily fast internal rates by a bounded clock

Set

$$
P=e^{\Delta K},\qquad K_\Delta=\frac{P-I}{\Delta}.
$$

The matrix $P$ is stochastic and reversible under $\mu$. Thus $K_\Delta$ is a reversible Markov generator with stationary law $\mu$ and total outgoing rates at most $1/\Delta$. It has a uniformized representation: at independent Poisson times of rate $1/\Delta$, update the hidden state by $P$, allowing self-updates.

Reversibility supplies a bound uniform in the original spectrum. On an eigenvector with $K$-eigenvalue $-\lambda$, $\lambda\ge0$, the replacement has decay rate

$$
\lambda_\Delta=\frac{1-e^{-\lambda\Delta}}{\Delta}.
$$

For every $t>0$,

$$
\|e^{Kt}-e^{K_\Delta t}\|_{L^2(\mu)\to L^2(\mu)}
\le d_\Delta(t):=\min\left\{1,\frac{2\Delta}{t}\right\}.
\tag{5}
$$

To verify the nontrivial bound, first take $\lambda\Delta\le1$. Then $\lambda_\Delta\ge\lambda/2$ and $\lambda-\lambda_\Delta\le\lambda^2\Delta/2$, so

$$
0\le e^{-\lambda_\Delta t}-e^{-\lambda t}
\le\frac{\lambda^2\Delta t}{2}e^{-\lambda t/2}
\le\frac{8e^{-2}\Delta}{t}<\frac{2\Delta}{t}.
$$

If $\lambda\Delta>1$, then $\lambda_\Delta\ge(1-e^{-1})/\Delta$, and $e^{-\lambda_\Delta t}\le\Delta/[e(1-e^{-1})t]<\Delta/t$. Both exponentials lie in $[0,1]$, giving the remaining part of (5).

Let $Q_0$ denote the full zero-field generator with the single $A$ state included. In $L^2(\pi_0)$ it has the common constant and visible modes with eigenvalues $0,-2$, and the hidden centered modes with eigenvalues $-(1+\lambda)$. Replacing $K$ by $K_\Delta$ changes only those hidden decay rates. The same bound (5) therefore holds for the full zero-field semigroups.

The field-dependent perturbation $V_h=Q(h)-Q_0$ has

$$
\|V_h\|_{L^2(\pi_0)\to L^2(\pi_0)}\le B=2(R-1).
\tag{6}
$$

For example, separate the $A$ coordinate and the hidden $L^2(\mu)$ space. Each diagonal block and each off-diagonal block has norm at most $R-1$, because $|e^{(1\pm g_j)h}-1|\le R-1$. The block matrix consequently has norm at most twice that value. The forward adjoint has the same norm.

Let $F_{\eta,\Delta}$ denote the model with quantized $g$ and internal generator $K_\Delta$. Both this model and $F_\eta$ start from density $1$ relative to their common $\pi_0$. Their relative densities satisfy the zero-field variation-of-constants equation

$$
\rho(t)=1+\int_0^t e^{Q_0(t-s)}V_{h(s)}^*\rho(s)\,ds.
$$

The adjoint is taken in $L^2(\pi_0)$. Equations (5)--(6), $\|\rho(s)\|_2\le e^{Bs}$, and Gronwall's inequality give, uniformly for $t\le T_*$ and every bounded protocol,

$$
|m_{F_\eta}[h](t)-m_{F_{\eta,\Delta}}[h](t)|
\le B e^{2BT_*}J_\Delta(T_*),
$$

where

$$
J_\Delta(T_*)=\int_0^{T_*}d_\Delta(s)ds
\le2\Delta\left[1+\log\frac{T_*}{2\Delta}\right]
\le2\sqrt{2\Delta T_*}.
$$

The last inequality uses $1+\log x\le2\sqrt x$ for $x\ge1$. The displayed choice of $\Delta$ makes this error at most $\varepsilon/4$. This step controls an integrated semigroup error; it does not claim that rapidly mixing hidden trajectories can be coupled state by state.

## 4. Compress a finite alphabet of hidden words

Observe the stationary discrete chain with transition matrix $P$ only through its quantized symbol $g^\eta$. It is a stationary process on at most $m$ symbols, although it generally is not Markov on those symbols.

Construct its order-$\ell$ Markov approximation. A hidden surrogate state is an allowed word $w=(z_1,\ldots,z_\ell)$ of consecutive symbols. Give it stationary probability

$$
\nu(w)=\Pr(Z_1=z_1,\ldots,Z_\ell=z_\ell).
$$

The transition shifts the word left and appends a new symbol $z$, with probability

$$
\mathsf P(w,(z_2,\ldots,z_\ell,z))
=\Pr(Z_{\ell+1}=z\mid Z_1=z_1,\ldots,Z_\ell=z_\ell).
$$

Its output $\gamma(w)$ is the last symbol of $w$. Stationarity of the original symbol process implies $\nu\mathsf P=\nu$. Starting from $\nu$, the surrogate output process reproduces every original consecutive-symbol distribution of length at most $\ell+1$. To make the future-block claim explicit, consider the stationary two-sided word chain. Deterministic shifts imply that its state is its last $\ell$ output symbols. Its state together with its next output has exactly the original length-$\ell+1$ law by construction. Output stationarity then shifts this block to any chosen future starting time, including time zero. Because $P=e^{\Delta K}$ is strictly positive for an irreducible finite $K$, all words over nonempty symbol classes have positive probability, and the word chain is irreducible. There are at most $m^\ell$ states.

Use the continuous-time internal generator

$$
\widehat K=\frac{\mathsf P-I}{\Delta},
$$

stationary law $\nu$, and sensitivity $\gamma$. Attach the single state $A$ using the original functional field rule. The resulting model has at most $1+m^\ell$ total states, $|\gamma|\le G$, $\langle\gamma,1\rangle_\nu=0$, and sensitivity variance $W_\eta$.

The hidden word chain is generally **not reversible**. Nonetheless its stationarity is sufficient for the full model to have stationary law

$$
\widehat\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\widehat\pi_h(w)=\frac{\nu(w)e^h}{2\cosh h}.
$$

The external edges individually balance under this law, and the internal stationary flux sums to zero. At zero field, strong lumpability gives the exact telegraph path law. Expanding the master equation through order two uses stationarity and centered sensitivity, without requiring reversibility: it gives the reference linear mean and zero quadratic mean. These facts preserve the original passive and low-order comparison constraints, but not the target's microscopic reversibility or its exact $W$.

## 5. Why matching hidden words controls arbitrary field protocols

Compare $F_{\eta,\Delta}$ with the word surrogate on a horizon at most $T_*$. The exit hazard from $A$ depends only on the one-symbol stationary marginal,

$$
e^{h(t)}\langle e^{h(t)g^\eta},1\rangle_\mu,
$$

so it is the same in both models and at most $R$. At a jump into the hidden block, the hidden entry law is tilted by $e^{h(t)g^\eta}$ relative to $\mu$, and by $e^{h(t)\gamma}$ relative to $\nu$, respectively.

The stationary symbol blocks through length $\ell+1$ agree. Tilting both block laws by the same function of their first symbol preserves their equality, with identical normalization. Therefore one can couple the first $\ell+1$ hidden symbols of each newly entered $B$ visit exactly, including this field-dependent entry law. An initial $B$ visit instead uses the common untilted stationary symbol-block law. Poisson internal update times can also be coupled, since their rate is $1/\Delta$ and their clocks are independent of the discrete chain.

Given identical symbols and update times, the external killing rate $e^{(\gamma-1)h(t)}$ agrees at every time, so couple the exits from $B$ using the same clock. This works for arbitrary bounded time-dependent protocols, not just constant steps. The visible paths agree unless some $B$ visit receives more than $\ell$ internal Poisson updates before the observation horizon.

Each visit has at most $T_*$ time available. Its failure probability is bounded by

$$
p_\ell=\Pr\{\operatorname{Pois}(T_*/\Delta)>\ell\}.
$$

There is at most one initial $B$ visit, and the expected number of subsequent entries before $T_*$ is at most $RT_*$. Conditional on a visit's start, its future uniformization clock is a fresh Poisson clock independent of its symbol sequence. A union bound over visits, or equivalently a stopped expected-count argument, consequently bounds path total variation by $(1+RT_*)p_\ell$. No extra factor from the tilted entry distribution is needed: the tilted symbol blocks were coupled exactly, and the Poisson count bound is independent of those symbols.

The binary mean difference is at most twice that probability. Using the elementary exponential-moment bound

$$
p_\ell\le e^{T_*/\Delta}2^{-\ell},
$$

our choice of $\ell$ gives

$$
\sup_{t\le T_*,h}|m_{F_{\eta,\Delta}}[h](t)-m_{\widehat F}[h](t)|
\le2(1+RT_*)p_\ell\le\frac\varepsilon4.
\tag{7}
$$

This is the only step that expands the surrogate state count. It stores a bounded window of hidden symbols as ordinary autonomous Markov states; it does not add an external clock or an uncounted memory register.

## 6. Extend the mean bound to every horizon

Every target, intermediate model, and word surrogate has reset rate at least $\alpha$. For a time $t>T_*$, restart each of $F_\eta$ and the surrogate at its own zero-field equilibrium at time $t-T_*$, then apply the final segment of the original protocol. The change of each final mean is at most $2e^{-\alpha T_*}$, regardless of its previous driven state. Thus restarting both costs at most

$$
4e^{-\alpha T_*}=\frac\varepsilon4.
$$

Over the remaining interval of length $T_*$, Sections 3--5 give error at most $\varepsilon/2$. Adding the quantization error (4) proves (1). For $t\le T_*$, no restart is needed and the bound is smaller.

The reset argument controls the final mean uniformly. It does not give uniform total variation between complete visible histories on arbitrarily long intervals; small per-visit differences can accumulate indefinitely in those histories.

## 7. What is settled and what remains open

This construction rules out a failure of all finite-state, fixed-tolerance mean compression within the bounded-field, bounded-sensitivity general family. Unrestricted hidden size and internal rates alone do not obstruct such compression. It also makes clear why scalar-kernel compression is not automatically enough: the word construction retains higher-order hidden symbol statistics that a two-time correlation kernel can discard.

The upper bound is nonsharp and may be computationally unusable. It applies to known targets and says nothing about obtaining the requisite word probabilities from passive data. It leaves open a small, preferably sharp general-family state bound, and an upper bound that retains reversibility and exactly preserves the target's sensitivity variance. The canonical subclass already has a much stronger result because its actuator permits an exact scalar-kernel closure; no such closure is assumed here.
