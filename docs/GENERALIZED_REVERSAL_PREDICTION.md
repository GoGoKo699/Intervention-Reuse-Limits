# Polynomial prediction under generalized time reversal

[Kinetic and parity resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [Original word-chain upper](BOUNDED_RATE_FINITE_FIELD.md) · [Ordinary-reversibility lower](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Entropy-production scope](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) · [PRL exploration](PRL_EXPLORATION.md)

**Research theorem and physical boundary, 23 September 2026.** Allowing a hidden-state time-reversal involution changes the state-complexity conclusion. The polynomial word predictor can obey generalized detailed balance, with an even actuator, the exact target histogram and the original rate cap. Its controlled response is exactly the same as that of the existing word predictor. Thus the superpolynomial lower for ordinary detailed balance does not extend to this broader notion of equilibrium.

This result does not contradict the ordinary-reversibility or identity-reversal entropy-production theorems. It limits their physical interpretation: they constrain predictors whose retained configurations are all even under the specified physical reversal. They do not establish a generic thermodynamic dissipation necessity when nontrivial reversal parities are allowed.

Word reversal in higher-order Markov representations is established; see Sergio Bacallado, “Bayesian analysis of variable-order, reversible Markov chains,” *Annals of Statistics* **39** (2011), 838–864, [DOI](https://doi.org/10.1214/10-AOS857), [primary text](https://arxiv.org/pdf/1105.2640), Definition 2.2 and Proposition 2.3. Those results characterize the relevant reversal-symmetric word-edge fluxes. The argument here additionally centers the actuator, proves exact response equivalence for the original continuous-time controlled interface, and retains the quantitative approximation bound. No novelty claim is made for word reversal itself.

## 1. Model and statement

Use the row-generator convention. A target has a finite irreducible hidden generator $K$, reversible stationary law $\mu$, sensitivities $g$ in an alphabet of at most $m\ge2$ values, and hidden exit rates at most $\Lambda k$. Assume $0<G<1$, $|g|\le G$, $|h|\le H$, and retain the original rates

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
\tag{1}
$$

preparation $(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. The target may also retain any specified centered actuator histogram.

For a predictor, let $\theta$ be an involution of its hidden states and let $(\Theta f)(w)=f(\theta w)$. Generalized reversibility with an even actuator means

$$
\widehat\mu(\theta w)=\widehat\mu(w),\qquad
\gamma(\theta w)=\gamma(w),\qquad
\widehat K^*=\Theta\widehat K\Theta,
\tag{2}
$$

where the adjoint uses $L^2(\widehat\mu)$. This permits $\widehat K^*\ne\widehat K$.

Put

$$
R=e^{(1+G)H},\qquad
q=\frac{\Lambda R}{1+\Lambda R},\qquad
C_R=1+2R^2,\qquad
p=\frac{\log m}{\log(1+1/(\Lambda R))}.
\tag{3}
$$

**Theorem.** For every odd integer $\ell\ge1$, there is a predictor satisfying (1)–(2), with at most $1+m^\ell$ total physical states, hidden exits at most $\Lambda k$, and exactly the target actuator histogram, such that

$$
\sup_{h,T}|m_F[h,T]-m_{\widehat F_\ell}[h,T]|
\le C_Rq^{\ell+1}.
\tag{4}
$$

The supremum includes every bounded deterministic piecewise-continuous protocol and every horizon. Consequently, for sufficiently small $\delta$, generalized-reversible prediction has the polynomial sufficient count

$$
\boxed{
D_{\rm gen}(\delta)
\le1+m\max\left\{m,(C_R/\delta)^p\right\}.}
\tag{5}
$$

The factor $m$ comes only from rounding the existing sufficient word length upward to an odd integer. It is independent of accuracy and target size. A reversible relaxation cap $\Lambda k$ supplies the needed exit bound, as proved in the original upper theorem.

## 2. The word-reversal involution

Set $\nu=\Lambda k$ and $P=I+K/\nu$. Let $(Z_j)_{j\in\mathbb Z}$ be the actuator process of the stationary target chain with transition $P$. Target reversibility gives

$$
p(z_1,\ldots,z_L)=p(z_L,\ldots,z_1)
\tag{6}
$$

for every finite block. Use the allowed words $w=(z_1,\ldots,z_\ell)$ as states, with

$$
\widehat\mu(w)=p(w),\qquad
\widehat P(w,(z_2,\ldots,z_\ell,a))
=\frac{p(z_1,\ldots,z_\ell,a)}{p(w)}.
\tag{7}
$$

Zero-probability words are omitted. Stationarity gives $\widehat\mu\widehat P=\widehat\mu$, and the existing microscopic-bridge argument proves irreducibility. Define

$$
\theta(z_1,\ldots,z_\ell)=(z_\ell,\ldots,z_1).
$$

The allowed set is closed under $\theta$, and (6) gives $\widehat\mu\theta=\widehat\mu$. For an allowed edge $w\to v=(z_2,\ldots,z_\ell,a)$,

$$
\begin{aligned}
\widehat\mu(w)\widehat P(w,v)
&=p(z_1,\ldots,z_\ell,a)\\
&=p(a,z_\ell,\ldots,z_1)\\
&=\widehat\mu(\theta v)\widehat P(\theta v,\theta w).
\end{aligned}
\tag{8}
$$

A pair is shift-compatible exactly when its reversed, word-reversed pair is compatible. Thus (8) also covers zero edges, and includes self-transitions. It proves

$$
\widehat P^*=\Theta\widehat P\Theta,\qquad
\widehat K=\nu(\widehat P-I),\qquad
\widehat K^*=\Theta\widehat K\Theta.
\tag{9}
$$

For $\ell=2d+1$, assign the middle actuator

$$
\gamma(w)=z_{d+1}.
\tag{10}
$$

It is $\theta$-even. Every stationary coordinate of a word has the target one-symbol law, so the entire histogram is unchanged. No extra orientation states are introduced.

## 3. Exact equality of controlled responses

The equality of responses is stronger than a time-reversed average. Consider a stationary two-sided realization $(W_j)$ of the same word chain. Write $E_j=(W_j)_\ell$ for the usual last-coordinate actuator. Deterministic shifts imply almost surely

$$
W_j=(E_{j-\ell+1},\ldots,E_j),\qquad
\gamma(W_j)=E_{j-d}.
\tag{11}
$$

Stationarity therefore makes the entire middle-coordinate output sequence equal in law to the last-coordinate output sequence. Equation (11) shifts the discrete update index, not physical time. Embedding either stationary output sequence with an independent rate-$\nu$ Poisson clock gives exactly the same stationary continuous-time actuator-path law, including self-updates.

That path law determines the original-rule controlled response. At an entry time $s$ into the hidden block, the entry law is the stationary law tilted by $e^{h(s)\gamma}$. The exit hazard from $A$ is

$$
k e^{h(s)}\mathbb E e^{h(s)\gamma}.
$$

Conditional on the resulting hidden actuator path, survival to $t$ is

$$
\exp\!\left[-\int_s^t k e^{(\gamma_u-1)h(u)}\,du\right],
\tag{12}
$$

and the final hidden-to-visible hazard is $k e^{(\gamma_t-1)h(t)}$. The initial hidden visit uses the untilted stationary path. Equality of stationary actuator-path laws gives equality after the same initial-symbol tilt, the same hidden-visit survival/exit laws and the same rates out of $A$. The alternating visible/hidden visit construction consequently gives identical visible path laws for each prescribed deterministic protocol.

Thus the centered predictor has **exactly the same actual controlled means** as the original last-coordinate word predictor. Its finite-prefix and common-reset proof gives (4) unchanged. Let $\ell_0$ be the sufficient length in the original upper. The least odd $\ell\ge\ell_0$ obeys $\ell\le\ell_0+1$, so $m^\ell\le m m^{\ell_0}$, proving (5). No inference from approximate forward means to approximate reversed means is needed.

## 4. Generalized equilibrium and finite ordinary entropy production

Extend $\theta$ by $\theta(A)=A$. Its even actuator and invariant stationary mass make the full fixed-field law $\widehat\pi_h$ invariant under $\theta$. External edges obey ordinary detailed balance and are $\theta$-invariant. Together with (8), this gives

$$
\widehat\pi_h(x)\widehat Q_h(x,y)
=\widehat\pi_h(\theta y)\widehat Q_h(\theta y,\theta x),
\qquad
\widehat Q_h^{*\widehat\pi_h}=\Theta\widehat Q_h\Theta.
\tag{13}
$$

The stationary path law is invariant under time reversal combined with $\theta$. Its generalized stationary entropy-production rate is zero at every constant field. Its ordinary identity-reversal entropy production need not vanish and may be infinite.

The latter infinity is not essential to the upper. Starting with accuracy $\delta/2$, put

$$
\widehat K_\epsilon=(1-\epsilon)\widehat K+\epsilon\widehat K^*,
\qquad 0<\epsilon<1/2.
$$

Then $\widehat K_\epsilon^*=\Theta\widehat K_\epsilon\Theta$, and its states, labels, stationary law and exit rates are unchanged. The [finite-EPR perturbation bound](ENTROPY_PRODUCTION_REVERSIBILIZATION.md#5-finite-entropy-production-for-a-bounded-rate-predictor) gives mean cost at most $2\Lambda R\epsilon$ and ordinary hidden entropy production at most

$$
\Lambda k\log\frac{1-\epsilon}{\epsilon}.
\tag{14}
$$

Choosing $\epsilon=\delta/(4\Lambda R)$ for sufficiently small $\delta$ retains polynomial size and error at most $\delta$, with finite ordinary full zero-field entropy production $O(k\log(1/\delta))$ and exactly zero generalized stationary entropy production.

These are properties of a specified mathematical reversal. They do not demonstrate that the word-memory states have a natural mechanical implementation with that physical parity, nor that an arbitrary driven protocol has zero total entropy production.

## 5. Consequences for the state comparison

For the original nineteen-level targets take $m=19$, $\Lambda=3$ and $G=9/100$. The generalized predictor retains hidden exits at most $3k$ and the exact target histogram. Equation (5) holds for all bounded protocols, hence also at every fixed positive clock and on the two-field menu $\{0,H\}$.

The [new two-field rank lower](CAPPED_KINETIC_INTERFACE_SEPARATION.md#6-a-polynomial-unrestricted-lower-on-the-same-two-fields) applies to every stationary rival with the shared equilibrium interface and prescribed preparation/readout. Its logarithm truncation is target-only; a rival needs neither a cap nor ordinary reversibility. In particular it applies to (2). Together with (5), it gives, on the same target family and the same two-field clock menu,

$$
D_{\rm gen}^{(2,a)}(\delta)=\delta^{-\Theta(1)}.
\tag{15}
$$

This remains true with the common hidden exit cap $3k$ imposed, since the sufficient predictor already satisfies it. The [combined resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) states the three-class comparison within a wider, shared bounded kinetic interface. The earlier thirty-nine-field rank lower remains valid, but those additional fields are no longer needed for this polynomial necessity.

The lower and upper powers need not match. This excludes a superpolynomial generalized-reversibility penalty for this family, even under the original histogram and cap. The ordinary detailed-balance lower and the identity-reversal EPR frontier retain their stated content.

The involution is a fixed permutation of counted states. It is neither a supplied control nor a hidden external clock. The Poisson uniformization clock is the standard representation of the autonomous generator $\widehat K$; the word itself is an ordinary counted Markov state. The construction does not read future observations or receive an uncounted memory register.

## 6. Why the ordinary proof and a naive doubling argument differ

Generalized reversibility gives $e^{t\widehat K^*}=\Theta e^{t\widehat K}\Theta$, rather than ordinary selfadjointness. The permutation commutes with actuator multiplication but need not commute with $\widehat K$, and it is not an allowed physical operation. Reversing the available word does not supply its ordinary stationary adjoint. Likewise the old symmetrized resolvent feature is generally only $\Theta$-selfadjoint, so the selfadjoint/PSD and observed Gram arguments cannot be reused unchanged. The explicit polynomial upper shows that the corresponding universal superpolynomial extension is false, rather than merely unproved by that route.

For an arbitrary stationary predictor, the doubled chain $\operatorname{diag}(K,K^*)$ with equal orientation masses and identical paired labels is generalized reversible under orientation exchange. This does not by itself preserve its controlled response: each hidden visit uses the average of the two stationary actuator-path laws. Repeated visits also mean that the complete visible response is not generally the arithmetic average of the two complete responses. Exact preservation follows if the original stationary actuator process is itself reversal-invariant. The centered-word proof establishes the required path-law identity directly and uses no generic doubling claim.
