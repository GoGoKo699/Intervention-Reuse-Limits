# An uncapped reversibility penalty at every fixed positive clock

[Positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) · [Fixed-clock Gram observability](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Tagged target](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) · [Weighted entropy interface](WEIGHTED_WHOLE_WORD_REPAIR.md) · [Earlier arbitrary-switching theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md)

**Research theorem, 23 September 2026.** A fixed positive control clock still permits a superpolynomial state cost of ordinary reversibility, even when reversible predictors may use arbitrarily fast hidden rates. A balanced binary actuator suffices. The target family has a fixed positive hidden gap and fixed exit cap; the rival class has neither restriction. The lower bound uses actual means, the original field rule, exact histogram, stationary preparation and binary readout.

The bound below has a conservative twelfth-root logarithmic exponent. It does not match the stronger square-root exponent currently proved for arbitrary rapid switching, and the construction has very unfavorable fixed rate-to-gap constants.

## 1. Target family, clock and conclusion

Fix $k,H>0$, $0<\gamma<1$ and a dimensionless clock $a>0$. Use only the two fields $0$ and $H$. Every positive segment duration must be an integer multiple of $a/k$. An observation horizon is also a clock endpoint. Take $h_*=H$ in the natural-killing construction.

Start from the tagged binary family and set

$$
\Delta_b=e^{(\gamma-1)h_*}-e^{(-\gamma-1)h_*}>0,
\qquad \eta=\Delta_b/10^9.
\tag{1}
$$

Assign its core and chain to $+\gamma$, and its private tags and balancing state to $-\gamma$. Multiply its unrescaled hidden generator by $\eta k$. Let $\mathcal F_{\mathrm{clk}}$ be this family for all sufficiently large integer indices $n$. The target count remains

$$
36r2^r+100Nn+3,\qquad r=2^n,\quad N=10^6.
\tag{2}
$$

With $B=5\times10^8$ and the fixed $g_*>0$ of the tagged construction, exits are at most $\eta Bk$ and the nonzero hidden spectrum lies in $[\eta g_*k,2\eta Bk]$. The ratio is fixed independently of $n$. The target gap is not normalized to $k$.

Both rival classes use the original external rule

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
\tag{3}
$$

with exact histogram $\mu(g=\pm\gamma)=1/2$, preparation $(1/2,\mu/2)$ and readout $(-1,1_{\rm hid})$. Rivals may introduce arbitrary new finite state spaces, with every retained state counted. There is no hidden rate cap or prescribed lower gap. The reversible class additionally imposes ordinary hidden detailed balance.

Define worst-case minimal state counts on $\mathcal F_{\mathrm{clk}}$ using uniform mean error at most $\delta$ over the specified two-field clock protocols and all clock horizons. Then fixed positive constants satisfy, for sufficiently small $\delta$,

$$
\boxed{
\begin{aligned}
D_{\rm all}^{\rm clk,unc}(\delta)&\le C_0\delta^{-p},\\
D_{\rm rev}^{\rm clk,unc}(\delta)&\ge
\exp\!\left(\exp\!\left(c_a[\log(1/\delta)]^{1/12}\right)\right),\\
p&=\frac{\log2}{\log(1+1/(\eta B e^{(1+\gamma)H}))}.
\end{aligned}}
\tag{4}
$$

The all-protocol word-chain upper supplies the first line, so it also holds under the smaller clock protocol class. The reversible prediction-partition upper remains available. A polynomial lower for unrestricted prediction on this particular rescaled target family is not asserted.

The lower-bound contradiction uses only finitely many legal clock words for each $n$, with maximum length $O_a((n+1)^{12})$. Their choice and length bounds are independent of rival rates and dimension. This assertion is an existence and observability bound, not a sample-complexity claim.

## 2. Positive kernels and target entropy data

Use the exact natural-killing selectors $A_i$ and transports from the [positive calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md). For a fixed sufficiently large $S_*$, their scales are

$$
s=e^{S_*(n+1)},\qquad
t_i=T_i/\eta=O(n+1),\qquad
\widetilde\kappa_i=\eta^2e^{-b_1t_i}\kappa_i,\qquad
\tau_n=e^{-100n}/\eta.
\tag{5}
$$

In every reversible rival, the selectors and transports are entrywise nonnegative and adjoint-compatible. On the target, selectors differ from signed-port projectors by at most $e^{-2300n}$, and transports differ from the old permutation transports by at most $Ce^{-100n}$.

Let $A=A_{0,+}+A_{0,-}$, $u_0=A1$, $v=(A_{0,+}-A_{0,-})1$ and $Z=\|u_0\|_\mu^2$. Define the same addressed query words $Q_b$, flip words $C_c=Q_cG_FQ_c^*$, vectors $v_b=Q_bv$ and $q_b=Q_bu_0$ as in the arbitrary-switching binary theorem. The central target mass obeys

$$
z_n\ge c_*e^{-100n}.
\tag{6}
$$

The normalized target defects in the [weighted repair hypotheses](WEIGHTED_WHOLE_WORD_REPAIR.md#1-hypotheses-on-one-finite-probability-space) are at most $e^{-40n}$ for sufficiently large $n$. This follows from the same target telescoping argument as before: unnormalized vector errors are $C(n+1)e^{-100n}$, ideal endpoint vectors have norm $\sqrt{z_n}$, and division by $\sqrt{z_n}$ costs at most $Ce^{50n}$. In particular this includes the target difference between $Z$ and $z_n$.

Only the observation interface changes. The exact rival kernels in this section are not replaced by signed polynomial kernels when applying entropy repair.

## 3. Finite reduction of every required scalar

The largest entropy scalar still has at most $54n+6$ cross-port factors and two endpoint selectors. Every scalar is a linear combination of hidden words containing $O(n+1)$ exact heat blocks and scalar normalizations with product $e^{O((n+1)^2)}$.

Use the uniform killed-heat approximation in the calculus note at accuracy $e^{-C(n+1)^2}$. A degree $d=O((n+1)^4)$ polynomial in a normalized natural resolvent suffices. Choose its fixed constant large enough that every complete entropy scalar changes by at most $e^{-600(n+1)}$ in **each** model. This approximation is uniform even when the rival generator is unbounded.

After expansion of the symmetrized label factors and these heat polynomials, and then the visible Schur complements, all scalar expressions have the following bounds. Write $q=n+1$.

| Quantity | Bound |
|---|---:|
| Normalized physical resolvent/projector factors in a word | $L\le C_Lq^5$ |
| Smallest Laplace parameter | $z\ge c_z/q$ |
| Logarithm of total scalar coefficient and denominator-Lipschitz mass | $C_Jq^5\log(q+1)$ |
| Uniform error from the heat-polynomial replacements | $e^{-600q}$ |

The constants are fixed by the construction, field bound and alphabet. In particular, expanding a Schur complement adds a fixed number of factors and a denominator inverse bounded by $Cq$, rather than an unknown rival-dependent exponential cost. Differences of these denominator factors are controlled by their separately observed visible-return scalars.

## 4. Clock-Gram transfer and an explicit twelfth-power budget

Let $E_h=e^{aQ_h}$ for the allowed menu. The [clock-Gram lemma](FIXED_CLOCK_GRAM_OBSERVABILITY.md) uses detailed balance and the rank-one visible metric change to recover Gram norms of finite clock words. A target cap bounds each target sampled spectrum away from zero. This controls the target high-frequency filter $(I-E_h)^{M+1}$ and, through the observed Gram scalar, the same filter acting on the rival's required polynomial vectors.

For a normalized physical resolvent, its clock polynomial uses a fractional-power truncation degree $M$ and an integer-time cutoff $J_{\mathrm{cut}}$. It has coefficient mass at most $2^{M+1}$. Its unresolved integer tail is $e^{-az(J_{\mathrm{cut}}+1)}$. The resulting scalar transfer for words of length $L$ has a deterministic tail bounded by

$$
e^{CL}\left(e^{-az_{min}(J_{\mathrm{cut}}+1)}+\rho_*^M\right),
\qquad 0<\rho_*<1,
\tag{7}
$$

and a measurement term bounded by

$$
\exp\!\left(C(L+1)(M+J_{\mathrm{cut}}+1)\right)\sqrt\delta.
\tag{8}
$$

The constants depend on the fixed target cap, physical fields and clock, not on rival rates. The bounded visible-projector endpoints introduce only fixed coefficient factors; the displayed bound may be enlarged to absorb their finite preparation recursion.

Choose fixed sufficiently large constants $C_M,C_T$ and take

$$
M=\lceil C_Mq^6\rceil,\qquad
J_{\mathrm{cut}}=\lceil C_Tq^7\rceil.
\tag{9}
$$

Since $z_{min}\ge c_z/q$, both deterministic tails in (7) decay as $e^{-cq^6}$. They beat the coefficient and denominator-Lipschitz factor $\exp(C_Jq^5\log(q+1))$ from Section 3. The exponent in (8) is at most $C_aq^{12}$ because $L=O(q^5)$ and $M+J_{\mathrm{cut}}=O(q^7)$. The same coefficient factor can be absorbed in this exponent. Thus every exact entropy scalar differs between target and rival by at most

$$
e^{C_aq^{12}}\sqrt\delta+e^{-c q^6}+2e^{-600q}.
\tag{10}
$$

All sampled words used in these estimates have at most $O_a(q^{12})$ ticks: a resolvent polynomial has degree at most $M+J_{\mathrm{cut}}$, at most $O(q^5)$ such factors occur, and Gram reversal only changes a fixed multiplier. The finite visible-preparation recursion does not require a limit or a longer asymptotic time scale.

Choose a fixed $C_*>0$ large enough and assume

$$
\delta\le e^{-C_*(n+1)^{12}}.
\tag{11}
$$

Then (10) is at most $e^{-400n}$ for sufficiently large $n$. Together with (6), the normalization scalar $Z$ is at least $z_n/2$, and every rival hypothesis of weighted repair holds with $\Delta\le e^{-30n}$, after adding the target defects from Section 2.

## 5. Entropy and inversion

The exact rival kernels are positive and have the support required by weighted repair: the central selector is an outer factor in nonempty central words and every flip word. Empty query words cause no difficulty because $u_0$ and $v$ already have that support. Positivity gives $|v_b|\le q_b$.

On the rival's actual states, set $\nu_i=\mu_i u_0(i)^2/Z$ where $u_0(i)>0$. The weighted whole-word lemma, applied to the exact kernels, yields

$$
\sqrt\Delta\le\frac1{32\,2^n},\qquad
D\ge2^{3\cdot2^n/4}
\tag{12}
$$

for sufficiently large $n$. No hidden coordinates or new states are supplied to the rival in this argument.

For a given small $\delta$, choose the largest integer $n$ for which $C_*(n+1)^{12}\le\log(1/\delta)$. Then $n=\Theta((\log(1/\delta))^{1/12})$, proving the reversible lower in (4). The exponent $1/12$ is a conservative consequence of the explicit polynomial recovery budgets; no optimality is claimed.

## 6. A five-field common-family growth-class corollary

For this corollary explicitly enlarge both the target family and the permitted menu. Let

$$
\mathcal F_{\rm union}=\mathcal F_{\mathrm{clk}}\cup\mathcal F_{\rm old,bin},
\qquad \mathcal H_5=\{0,H/4,H/2,3H/4,H\},
\tag{13}
$$

where $\mathcal F_{\rm old,bin}$ is the earlier budget-$6580$ binary family. Both subsets use the same $k,H,\gamma$, exact histogram, preparation and readout. They share the fixed exit bound $B_{\rm union}k$, with $B_{\rm union}=\max\{\eta B,6580\}$, and lower hidden gap $\min\{\eta g_*,1\}k$.

The old family's [target-only rank argument](BINARY_REVERSIBILITY_LOWER_BOUND.md#9-a-polynomial-lower-for-unrestricted-prediction) supplies a polynomial unrestricted lower with unbounded rival rates. To use the menu in (13), replace the older convenient small field spacing by $H/4$: the exponential Vandermonde matrix remains invertible for every $H>0$, target constant-field spectra remain in a fixed bounded interval, and the same whole-side logarithm truncation has degree $O_a(n)$ and coefficient mass $e^{O_a(n)}$. Thus the rank proof and its polynomial lower retain their form, with changed fixed constants.

The common word-chain upper and the new lower, which already needs only $\{0,H\}\subset\mathcal H_5$, give

$$
D_{\rm all}^{\rm union,clk,unc}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{\rm union,clk,unc}(\delta)
\ge\exp\!\left(\exp\!\left(c_a[\log(1/\delta)]^{1/12}\right)\right).
\tag{14}
$$

The enlarged family and five-field menu are part of this corollary. The two-field main theorem (4) makes only a polynomial sufficient-count assertion for unrestricted prediction on its rescaled tagged family.

## 7. Scope

The theorem uses a fixed two-field binary interface and every prescribed positive clock. It therefore also gives a reversible lower bound when the admissible protocol class contains a larger fixed menu including these fields, such as the five-field menu in Section 6. It removes the rival rate cap without requiring arbitrarily fast control switching. A fixed finite set of clock words at each accuracy suffices for the lower-bound implication, but the result does not specify an experimentally practical sample count or numerical conditioning.

The target differs from both the earlier budget-$6580$ binary family and the tight-band nineteen-level family. It uses rare tags, a distant balancing state, a small but fixed positive hidden gap, and large fixed constants. The same fixed-clock uncapped penalty on either earlier target family remains open, as do stronger error exponents and the uncapped law $\exp(c\delta^{-\alpha})$. The arbitrary-switching square-root-log theorem and the present fixed-clock twelfth-root-log theorem have different protocol guarantees and should be stated separately. Manuscript drafting remains the last step.
