# Prediction states and stationary entropy production

[Uniform reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) · [Tight-band fixed-clock lower](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Fixed-budget lower](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [PRL exploration](PRL_EXPLORATION.md)

**Research consequence, 23 September 2026.** The reversible state lower bounds imply quantitative constraints on predictors with small stationary entropy production. The bridge uses additive reversibilization on exactly the same states. It does not identify state count with Shannon entropy or assume that the weighted law in the lamp argument is the predictor's physical stationary law.

Entropy production here is the standard continuous-time Markov path entropy-production rate under ordinary, identity time reversal. Interpreting it thermodynamically presumes this reversal convention for the counted states. No statement about generalized reversals of odd variables, Landauer erasure heat, or a specified device's energy consumption is made.

## 1. A common resource definition

Let a predictor have stationary hidden generator $K$, positive stationary law $\mu$, original external rates, zero-field preparation $(1/2,\mu/2)$ and binary readout. Put $K^*_{ij}=\mu_jK_{ji}/\mu_i$ for $i\ne j$. Its hidden stationary entropy-production rate is

$$
\sigma_{\rm hid}(K)=\sum_{i\ne j}\mu_iK_{ij}
\log\frac{\mu_iK_{ij}}{\mu_jK_{ji}},
\qquad \sigma_0(K)=\frac12\sigma_{\rm hid}(K).
\tag{1}
$$

The conventions are $0\log(0/b)=0$ and a positive forward flux with zero reverse flux gives $+\infty$. Rates are measured in nats per unit time. The second quantity is the full physical model's stationary entropy-production rate at zero field: the hidden block has mass $1/2$, and all external edges individually obey detailed balance. At a constant field $h$, its stationary rate is $[e^h/(2\cosh h)]\sigma_{\rm hid}$. Under a changing field the total entropy balance has additional terms and is not asserted to equal (1).

Fix the target family, physical sensitivity bound $G$, field bound $H$, an observation norm, and one common competitor class whose only additional reversible constraint is ordinary detailed balance. Define

$$
D_{\le\Sigma}(\delta)=\sup_F\inf\bigl\{|\widehat F|:
\widehat F\text{ is admissible},\ 
\mathcal D(F,\widehat F)\le\delta,\ 
\sigma_0(\widehat F)\le\Sigma\bigr\}.
\tag{2}
$$

All states, including the visible state, count. The worst-case target may depend on both tolerances. The relevant class may impose a common exit cap or exact histogram, provided it is preserved by additive reversibilization. Neither is needed for the general comparison below.

## 2. Same-state comparison with a reversible predictor

Set $R=e^{(1+G)H}$. The [uniform reversibilization theorem](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) uses

$$
K_{\rm sym}=\tfrac12(K+K^*)
\tag{3}
$$

on the same states. It preserves $\mu$, every actuator label, the histogram and each hidden exit rate, and obeys detailed balance. With the same original external rule and preparation, its actual means satisfy

$$
\mathcal D_H(\widehat F,\widehat F_{\rm sym})
\le R^{3/2}\sqrt{\sigma_0(\widehat F)/k}.
\tag{4}
$$

The estimate holds uniformly over all bounded protocols and all horizons; hence it holds on every fixed-clock subfamily. Its constant does not depend on the hidden rate cap, state count or minimum stationary mass. It compares endpoint means; it does not claim that complete path distributions remain uniformly close at indefinitely long observation times.

The triangle inequality and preservation of the admissible constraints give the general resource implication

$$
\boxed{
D_{\le\Sigma}(\delta)\ge
D_{\rm rev}\!\left(\delta+R^{3/2}\sqrt{\Sigma/k}\right).}
\tag{5}
$$

This holds first for each individual target, by mapping every admitted predictor to (3), and then after taking the supremum. No interchange of target-dependent optimizers is required. Write

$$
\varepsilon=\delta+R^{3/2}\sqrt{\Sigma/k}.
\tag{6}
$$

Only values of $\varepsilon$ in the small-error range of an invoked state lower bound are used below.

## 3. A frontier without a rival rate cap or histogram constraint

Use the original nineteen-level target family with hidden relaxation band $[k,3k]$, and the broad rivals of the [new tight-band theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md). Both classes allow any finite hidden state space, any stationary mass distribution, arbitrary finite hidden rates and any sensitivity values in $[-9/100,9/100]$. The original field rule, preparation and readout remain fixed. Only the target has the nineteen-level histogram.

For the two fields $0,H$ and any fixed positive clock $a/k$, equations (5)–(6) imply

$$
\boxed{
D_{\le\Sigma}^{(2,a)}(\delta)\ge
\exp\!\left(\exp\!\left(
c_{a,H}[\log(1/\varepsilon)]^{1/5}\right)\right).}
\tag{7}
$$

Here $\varepsilon$ must be sufficiently small. The statement is uniform over arbitrarily fast rival dynamics. At zero entropy production it reduces to the ordinary reversible lower. A growing rate budget cannot evade the comparison (4).

A concrete target-index version is useful. If target $n$ requires at least $2^{3\cdot2^n/4}$ reversible states below $\delta_n=e^{-C_*(n+1)^5}$, then any predictor of that target with fewer states and error $\delta<\delta_n$ must satisfy

$$
\sigma_0>\frac{k}{R^3}(\delta_n-\delta)^2.
\tag{8}
$$

Otherwise its symmetrization would contradict the reversible lower at error at most $\delta_n$. For $\delta\le\delta_n/2$, the necessary rate is at least $k\delta_n^2/(4R^3)$, with a strict inequality when using the stated non-strict accuracy threshold. This is a positive but potentially extremely small finite-accuracy requirement, not an order-one dissipation floor.

## 4. A stronger frontier under the original common exit budget

For this section retain the older comparison's exact nineteen-level histogram, original field rule and common exit cap $3k$ in both classes. The targets are the same original family. Use fixed-clock protocols with bounded fields; the old lower already uses a fixed thirty-nine-field sub-menu. Additive reversibilization preserves every one of these rival constraints.

The [fixed-budget theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) supplies fixed $c,\alpha>0$ such that $D_{\rm rev}^{(3,a)}(\varepsilon)\ge\exp(c\varepsilon^{-\alpha})$ at small $\varepsilon$. Therefore

$$
\boxed{
D_{\le\Sigma}^{(3,a)}(\delta)
\ge\exp\!\left[c\left(
\delta+R^{3/2}\sqrt{\Sigma/k}\right)^{-\alpha}\right].}
\tag{9}
$$

This stronger law has the older cap and histogram assumptions. It must not be substituted into (7)'s broader rival class.

If a uniform predictor budget $D\ge2$ serves every target at error $\delta$ with entropy-production budget $\Sigma$, then, in the range where (9) applies,

$$
\Sigma\ge\frac{k}{R^3}
\left[\left(\frac{c}{\log D}\right)^{1/\alpha}-\delta\right]_+^2,
\qquad [x]_+=\max\{x,0\}.
\tag{10}
$$

In particular, for any fixed constants $C_D,p_D>0$, a budget $D(\delta)\le C_D\delta^{-p_D}$ uniformly over the targets requires

$$
\Sigma(\delta)\ge c'k[\log(1/\delta)]^{-2/\alpha}
\tag{11}
$$

for sufficiently small $\delta$. To see the quantifiers carefully, if $\Sigma$ stays above a fixed positive threshold the claim is automatic. Otherwise (6) enters the small-error range of (9), and $\log D=O(\log(1/\delta))$ while $\delta=o([\log(1/\delta)]^{-1/\alpha})$. The theorem guarantees a hard target for the uniform budget; it does not require every target to dissipate at this rate.

## 5. Polynomial prediction with finite entropy production

The directed word-chain upper need not be left with infinite entropy production. Start from its stationary predictor $K$ at accuracy $\delta/2$ and exit bound $Bk$, with $B=3$ here. For $0<\theta<1/2$, set

$$
K_\theta=(1-\theta)K+\theta K^*.
\tag{12}
$$

This changes no state, label, stationary mass, histogram or exit rate. Every positive stationary edge flux now has a positive reverse flux, and the flux ratio lies between $\theta/(1-\theta)$ and its reciprocal. Consequently

$$
\sigma_0(K_\theta)\le\frac{Bk}{2}
\log\frac{1-\theta}{\theta}.
\tag{13}
$$

The common-reset coupling in the reversibilization note bounds the resulting all-protocol mean change by $2BR\theta$. For sufficiently small $\delta$, choose $\theta=\delta/(4BR)$. The total prediction error is at most $\delta$, the state count remains $C\delta^{-p}$, and

$$
\sigma_0(K_\theta)\le\frac{Bk}{2}\log\frac{4BR}{\delta}.
\tag{14}
$$

Thus finite, logarithmically bounded stationary entropy production suffices for the polynomial-state upper. This construction is admissible both in the capped exact-histogram class and in the broader class of Section 3. Bounds (11) and (14) do not match; they establish a quantitative tradeoff and a finite upper construction, not its optimal curve.

## 6. Physical meaning and limits

Every target is an equilibrium reversible Markov system with an exactly two-state passive visible law. Under the stated kinetic actuator, a predictor with fewer states may require stationary irreversible probability currents even at zero applied field. Equations (7)–(11) quantify that statement. The conclusion concerns the predictor's dynamics, not entropy production of the reversible target itself.

The microscopic realization of a predictor remains a separate issue. Multiplication of the path entropy-production rate by Boltzmann's constant gives entropy units when ordinary Markov time reversal describes the physical states. Identifying a heat rate additionally requires a thermodynamic realization and its reservoirs. No such identification is needed for the mathematical lower.

The theorem concerns counted Markov states and stationary path irreversibility. It does not lower-bound the predictor's physical stationary Shannon entropy, experimental sample cost, fitting time or robustness to arbitrary changes of field rule. The field rule and bounded sensitivity range remain explicit assumptions. Primary-source precedents and the PRL significance assessment are recorded separately; manuscript drafting remains deferred.
