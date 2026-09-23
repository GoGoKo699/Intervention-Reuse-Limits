# Prediction states, kinetic freedom and the reversal convention

[Capped interface separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [Generalized-reversal upper](GENERALIZED_REVERSAL_PREDICTION.md) · [General interface entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) · [Uncapped interface comparison](GENERAL_KINETIC_INTERFACE.md)

**Research consequence, 23 September 2026.** The state cost of preserving ordinary detailed balance differs from the cost of preserving a specified generalized time reversal. On the original tight-band targets, polynomial prediction is possible with a hidden reversal involution and an even actuator. Ordinary detailed balance requires exponentially more states under the same exit budget, even when rival barrier functions and actuator histograms are unrestricted within a fixed bounded interface.

The entropy-production implication uses identity reversal. The generalized construction can have exactly zero entropy production under its own reversal convention. Consequently these theorems do not establish an implementation-independent thermodynamic dissipation requirement.

## 1. Three classes under one interface

Fix $k,H,a>0$. The targets are the original nineteen-level lamp family with hidden band $[k,3k]$. Their actuator sensitivities satisfy $|g|\le G=9/100$, and their original external rates remain unchanged. Put $R=e^{(1+G)H}$.

For definiteness choose fixed constants $b_-,b_+,c_+$ with

$$
0<b_-\le R^{-1},\qquad b_+\ge R,\qquad c_+\ge R.
\tag{1}
$$

A competitor has one visible state $A$, any finite hidden set, a positive stationary law $\mu$, and a field-independent stationary generator $K$ with each hidden exit at most $3k$. It may choose arbitrary Borel barrier functions $b_i(h)$ satisfying, for $|h|\le H$,

$$
b_i(0)=1,\qquad b_-\le b_i(h)\le b_+,\qquad
e^{2h}b_i(h)\le c_+.
\tag{2}
$$

The external rates are

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h).
\tag{3}
$$

Thus $q_{Ai}/q_{iA}=\mu_i e^{2h}$, fixing the equilibrium block tilt while leaving kinetic barriers free. At zero field the preparation is $(1/2,\mu/2)$ and the readout is $(-1,+1_{\rm hid})$. No target actuator alphabet, histogram, moments, state topology or lower gap is imposed on a rival. The target and the existing upper constructions belong to this class by (1).

The three competitor classes differ only by their reversal requirement:

| Class | Hidden requirement |
|---|---|
| $\mathcal C_{\rm all}$ | Stationarity $\mu K=0$ |
| $\mathcal C_{\rm inv}$ | An involution $\theta$ with $\mu_{\theta i}=\mu_i$, $b_{\theta i}(h)=b_i(h)$ and $K^*=\Theta K\Theta$ |
| $\mathcal C_{\rm id}$ | Ordinary detailed balance $K^*=K$ |

Here $K^*_{ij}=\mu_jK_{ji}/\mu_i$ off the diagonal, $(\Theta f)(i)=f(\theta i)$, and $\theta(A)=A$. The involution is a property of the counted state space, not an available control or an uncounted memory register. These classes obey $\mathcal C_{\rm id}\subset\mathcal C_{\rm inv}\subset\mathcal C_{\rm all}$.

Use the two fields $0,H$, segment durations in $(a/k)\mathbb N$ and clock-endpoint observations. Let $D_{\rm all},D_{\rm inv},D_{\rm id}$ be the corresponding worst-case minimum total state counts over the same targets for uniform absolute mean error $\delta$. A predictor is selected before the protocol and must serve every legal word and horizon.

## 2. Different growth classes for the same prediction task

The [capped interface theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md) and the [centered-word construction](GENERALIZED_REVERSAL_PREDICTION.md) give fixed positive constants and exponents such that

$$
\boxed{
\begin{aligned}
c_0\delta^{-\gamma}
&\le D_{\rm all}(\delta)
\le D_{\rm inv}(\delta)
\le C_0\delta^{-p},\\
\exp(c_1\delta^{-\alpha})
&\le D_{\rm id}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log\frac2\delta\right),\\
p&=\frac{\log19}{\log(1+1/(3R))}.
\end{aligned}}
\tag{4}
$$

All quantities use the same two-field clock task, target family and common exit cap. In growth-class notation, $D_{\rm all}=D_{\rm inv}=\delta^{-\Theta(1)}$ and $D_{\rm id}=\exp(\delta^{-\Theta(1)})$; this does not assert equality of the exponents or pointwise equality of the first two state counts.

The lower rank argument only truncates target-side clock polynomials and consequently does not require a rival rate cap. The ordinary lower uses the common cap to make $I+K/(3k)$ a positive hidden Markov update, allowing exact nonnegative squared-Lagrange selectors and positive transports. Its witnessing horizons are $O_{a,H}(\log(1/\delta)/k)$ in physical time, with constants also depending on the fixed interface bounds.

The generalized upper uses odd-length words of the reversible target's stationary actuator process. Word reversal supplies $\theta$, and the middle symbol is an even actuator. The middle-symbol process has exactly the same stationary path law as the usual endpoint-symbol word predictor. It therefore has exactly the same original-rule controlled response and retains its all-protocol, all-horizon approximation guarantee. Rounding the word length to an odd integer costs at most one symbol, a fixed factor of nineteen in the sufficient state count.

The ordinary reversible upper is the existing prediction-partition construction. It preserves the original rule and exact histogram, and its exits remain at most $3k$, so it also belongs to the broader class (2)–(3). No new upper algorithm is assumed in (4).

Without a common rival exit cap, the [broader interface corollary](GENERAL_KINETIC_INTERFACE.md) still supplies the weaker fifth-root-log ordinary lower. The capped exponential law in (4) must not be transferred to that uncapped class.

## 3. The identity-reversal entropy-production frontier

Define the full zero-field stationary entropy-production rate under identity reversal by

$$
\sigma_0^{\rm id}(K)=\frac12\sum_{i\ne j}\mu_iK_{ij}
\log\frac{\mu_iK_{ij}}{\mu_jK_{ji}}.
\tag{5}
$$

A positive forward flux with zero reverse flux gives $+\infty$. The factor $1/2$ is the hidden block's stationary mass; every external edge balances individually. Entropy is measured in nats.

Additive reversibilization $K_{\rm sym}=(K+K^*)/2$ preserves the state space, stationary law, every barrier function and each hidden exit. The [general interface bound](GENERAL_INTERFACE_ENTROPY_BOUND.md), with return lower bound $kb_-$ and entry-density upper bound $kc_+$, gives

$$
\mathcal D_H(F,F_{\rm sym})
\le\sqrt{\frac{c_+}{b_-^2}\frac{\sigma_0^{\rm id}}k}.
\tag{6}
$$

Its constant has no hidden dimension, rate or minimum-mass factor. It bounds endpoint means uniformly in horizon, not complete long-time path distributions. It also applies to the two-field clock norm.

Let $D_{\le\Sigma}^{\rm id}(\delta)$ restrict $\mathcal C_{\rm all}$ by the budget $\sigma_0^{\rm id}\le\Sigma$. Mapping each admissible predictor to its symmetrization first for each target, and then taking the family supremum, gives

$$
\boxed{
D_{\le\Sigma}^{\rm id}(\delta)
\ge D_{\rm id}(\varepsilon)
\ge\exp(c_1\varepsilon^{-\alpha}),\qquad
\varepsilon=\delta+\sqrt{\frac{c_+}{b_-^2}\frac\Sigma k}.}
\tag{7}
$$

The last inequality uses the small-$\varepsilon$ range of (4). In particular a uniform state budget $D\ge2$ at accuracy $\delta$ and entropy-production budget $\Sigma$ requires, in that range,

$$
\Sigma\ge \frac{k b_-^2}{c_+}
\left[\left(\frac{c_1}{\log D}\right)^{1/\alpha}-\delta\right]_+^2.
\tag{8}
$$

For a fixed polynomial budget $D(\delta)\le C_D\delta^{-p_D}$, this implies a necessary worst-case budget $\Sigma(\delta)\ge c'k[\log(1/\delta)]^{-2/\alpha}$ for sufficiently small $\delta$. If $\Sigma$ lies outside the small-error range by staying above a fixed positive threshold, that asymptotic inequality is automatic. Otherwise apply (8). The hard target may depend on the budgets; not every target is required to have this cost.

Unlike the preceding capped resource theorem, (7) does not require exact rival histogram matching or the exponential barrier rule. It still requires the common hub geometry, bounded interface, field-independent hidden dynamics, fixed block tilt, preparation and ordinary reversal convention.

## 4. Zero generalized entropy production is compatible with polynomial prediction

The centered-word predictor obeys $\widehat K^*=\Theta\widehat K\Theta$ and has a $\theta$-invariant stationary law and actuator. Its full stationary path law at each constant field is invariant under path reversal combined with $\theta$. The relative-entropy rate against that reversed path law is therefore

$$
\sigma_0^{\theta}=0.
\tag{9}
$$

This is not in conflict with (7), which uses a different reference reversal. For sufficiently accurate predictors below the ordinary reversible state threshold, the same model can have $\sigma_0^{\rm id}>0$ while (9) holds.

The construction need not retain infinite identity-reversal entropy production. Start from its accuracy-$\delta/2$ version and use $K_\eta=(1-\eta)K+\eta K^*$ with $\eta=\delta/(12R)$ for sufficiently small $\delta$. This preserves generalized balance, states, stationary masses, actuator labels and each exit. The original-interface perturbation bound gives mean cost at most $6R\eta=\delta/2$, while

$$
\sigma_0^{\rm id}(K_\eta)\le\frac{3k}{2}\log\frac{12R}{\delta},
\qquad \sigma_0^{\theta}(K_\eta)=0.
\tag{10}
$$

Thus polynomial prediction with zero generalized stationary entropy production survives a finite-affinity regularization. The ordinary lower and upper entropy-production curves remain unmatched.

## 5. Physical conclusion and remaining work

The rigorous distinction is between ordinary detailed balance on retained configurations and generalized reversal on a memory representation. If the retained variables are physically even configurations, identity reversal is the relevant convention and the ordinary state/entropy constraints apply. If a nontrivial involution is allowed, the generalized construction prevents interpreting those constraints as a universal thermodynamic dissipation cost of prediction.

The involution in this theorem is mathematically explicit. A natural mechanical, chemical or other device realization with that parity has not been supplied. Neither zero stationary generalized entropy production nor ordinary stationarity implies zero total entropy production during a changing protocol. No heat, work, sample-complexity or stationary Shannon-entropy lower bound follows here.

The target still contains a constructed address-and-table system. The two-field horizon bound does not supply a small certified example at a useful tolerance. Establishing such an example, or verifying the separation in a recognizable physical model class, remains important to the PRL exploration. Manuscript drafting stays deferred.
