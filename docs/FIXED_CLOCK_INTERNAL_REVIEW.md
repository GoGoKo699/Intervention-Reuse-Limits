# Internal mathematical review of the fixed-clock route

[Fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) · [Clock Gram transfer](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Tagged target](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) · [Weighted repair](WEIGHTED_WHOLE_WORD_REPAIR.md)

**Internal research review, 23 September 2026.** This record distinguishes mathematical checking of the new proof chain from executable fixtures, live CI, external peer review and a priority assessment. Separate internal reviewers checked the observation interface and the heat/selector reductions. The integration reviewer also recalculated those interfaces and their combined asymptotic budget. These are internal reviews, not external validation.

**Mathematical verdict: PASS for the assembled proof chain.** The review covered the three new proof notes linked above, their use of the existing tagged target and weighted repair, and the two-field finite-horizon quantifiers. Formatting corrections were reported to the proof-note author. No remaining mathematical gap was identified in this internal review. Verifier and CI outcomes are recorded separately in [Verification](VERIFICATION.md).

## 1. Clock means supply the required Gram data

The finite visible-state-row recursion was checked directly from
$\pi_h=(1+\tanh h)\pi_0-\tanh h\,e_A^{\mathsf T}$ and stationarity. The zero-field recursion follows from the invariant telegraph sector. It applies to every finite suffix and requires no long-time preparation limit. Empty words, repeated zero-field factors and the constant term have the stated error bounds.

Rank-one insertions of the visible projector factor into products of actual scalar transition probabilities. Their discrepancy is controlled by telescoping bounded probabilities. It is not necessary to pretend that the projector was physically applied or to assume multitime path observations.

The stationary adjoint identity was checked with the correct metric order:

$$
E_h^{*\pi_0}=W_hE_hW_h^{-1},\qquad
W_h=I+(e^{-2h}-1)A.
$$

The four-term coefficient mass is $2e^{2|h|}-1$. The further density insertion for a $\pi_h$ Gram scalar belongs between the first word's adjoint and the second word. The stated clock-polynomial estimate and its finite tick count follow from these identities. No common coordinates for the target and rival are assumed.

## 2. The resolvent remainder is transferred as a vector norm

The averaged fractional-binomial polynomial was checked on the whole sampled spectral interval $[0,1]$. Its approximation lies in $[0,1]$, its coefficient mass is at most $2^{M+1}$, and the integer-time geometric tail is at most $e^{-az(J+1)}$. Functional calculus therefore gives

$$
\|(R_{h,z}-T_{h,z;M,J})f\|_{\pi_h}
\le e^{-az(J+1)}\|f\|_{\pi_h}
+\|(I-E_h)^{M+1}f\|_{\pi_h}.
$$

The last term is not uniformly small in rival operator norm. Its squared norm on a clock-polynomial suffix is a Gram scalar, so the data transfer the target's exponentially small remainder to that particular rival vector. The word telescope keeps true resolvents in each prefix and polynomial approximants in each suffix. This order avoids assuming a rival rate bound or applying an unproved small remainder to an arbitrary rival vector.

The resulting polynomials are spectral contractions in their own stationary norms. They need not be entrywise nonnegative. Positivity in the entropy argument belongs to the exact physical and hidden operators, not to their observation polynomials.

## 3. Hidden resolvents, binary labels and positivity

The Schur-complement identity was recalculated for the full physical resolvent. Its only scalar denominator, the normalized visible-to-visible resolvent entry, is at least $z/(z+R_H)$. Thus resolvent parameters bounded below by an inverse polynomial incur only polynomial inverse-denominator factors. Products of the Schur identities are evaluated as scalar rational expressions; the true hidden killed resolvents remain positive kernels.

For two fields $0,H$ and binary labels, the resolvent identity and $D_c+D_t=I$ isolate $G_0D_cG_H$ and $G_0D_tG_H$. Their entrywise positivity is an exact fact about the operators on each rival's own states. Raw $s^2G_0D_cG_H$ is generally not selfadjoint. Its symmetrization is entrywise nonnegative, selfadjoint and contractive, but need not be positive semidefinite. A selector $BEB^*$ with positive killed heat $E$ is both entrywise nonnegative and positive semidefinite.

The leading cross-color target term was checked independently. For either the consistently ordered raw features or the symmetrized features,

$$
F_cF_t=\frac2sD_cKD_t+O(s^{-2}).
$$

Diagonal killing terms vanish between different colors. Normalized selector convergence must therefore use this cancellation; an unnormalized $O(s^{-1})$ replacement estimate would not suffice after division by a rare tag weight.

Only the two physical fields $0,H$ are required by this route: they supply the finite row recursion, the two hidden resolvents, binary insertion, natural killed filtering and ordinary hidden heat. The earlier five-field Vandermonde argument is not being used.

## 4. Natural killing and uniform heat approximation

The target scaling was checked exactly. Assign the core sensitivity $+\gamma$ and tags and ballast $-\gamma$. Write $B_H=b_tI+\Delta D_c$, with $\Delta>0$, and set $\eta=\Delta/10^9$. Then

$$
e^{(T_i/\eta)(\eta K_{\rm old}-B_H)}
=e^{-b_tT_i/\eta}e^{T_i(K_{\rm old}-10^9D_c)}.
$$

The selector normalization acquires both endpoint factors and the survival factor:
$\kappa_i^{\rm new}=\eta^2e^{-b_tT_i/\eta}\kappa_i^{\rm old}$.
Its inverse still has logarithm $O(n)$, but with a different and potentially enormous fixed constant. The resolvent frequency must exceed that new constant; the old coefficient $20N$ cannot be reused without checking it. The stationary weights, exact binary balance and physical state count are unchanged. Gap and cap are multiplied by $\eta$. A further unit-gap normalization would change this natural-killing relation and is not automatic.

The independent heat review checked the endpoint-flat function
$f(z)=e^{1-1/z}$, $f(0)=0$. Cauchy estimates give
$\|f^{(j)}\|\le e3^j(j!)^2$; composition with $(1+\cos\theta)/2$ and Fourier integration by parts give a uniform polynomial approximation error $Ce^{-c\sqrt d}$ at degree $d$. The shifted Chebyshev recurrence bounds coefficient mass by $e^{O(d)}$. Therefore $e^{tA}=f((I-tA)^{-1})$ is recovered with a uniform estimate for every selfadjoint $A\le0$, including uncapped rivals. No operator logarithm at spectral value zero is used.

## 5. Conservative combined budget

The following deliberately loose allocation was checked so that no claim depends on optimizing exponents. Let $q=n+1$. The normalized logical scalar words contain $O(q)$ heat factors and have logarithmic normalization $O(q^2)$. Uniform replacement in both models may therefore require heat error $e^{-Cq^2}$, giving degree $O(q^4)$. After expansion there are $O(q^5)$ normalized physical-resolvent factors, and scalar coefficient mass has logarithm $O(q^5\log q)$, including Schur denominators. Required resolvent parameters obey $z\ge c/q$.

Choose the fractional-binomial cutoff $M=O(q^6)$ and geometric cutoff $J=O(q^7)$, with sufficiently large fixed constants. These suppress target remainders after the preceding normalization. The conservative clock-Gram bound includes $J$, so its logarithmic data amplification is

$$
O\!\bigl(q^5(M+J)\bigr)=O(q^{12}).
$$

Taking $\delta\le e^{-C_*q^{12}}$ with a sufficiently large fixed constant consequently supplies the exponentially small scalar errors needed by the existing weighted whole-word repair. The tick count is also bounded by a fixed multiple of $q^{12}$. The constants depend on the fixed field, clock and construction; they do not depend on rival dimension, rates or minimum stationary mass.

The assembled theorem includes this budget. Its positive entropy kernels remain exact while signed approximations recover only their scalar values. The required finite mean-word collection is chosen independently of rival dimension, rates and stationary masses. It gives a weaker accuracy exponent than the arbitrary-switching result and makes no optimality claim. Exact tiny fixtures supplement the algebra; they do not enumerate the large tagged target or establish the universal analytic estimates by computation.

The reviewed conclusion is a polynomial unrestricted sufficient count versus a reversible lower of $\exp(\exp(c_a[\log(1/\delta)]^{1/12}))$ on the newly rescaled tagged family. It does not assert a polynomial unrestricted lower on that family, preserve the older numerical gap/budget conventions, or identify an optimal reversible growth law. The new fixed-clock theorem and the earlier arbitrary-switching theorem concern separately specified target scalings and should retain their own quantifiers.

## 6. Five-field union corollary

**Review: PASS.** Section 6 of the fixed-clock theorem explicitly enlarges the family to include the older binary targets and the menu to $\{0,H/4,H/2,3H/4,H\}$. The older target-only rank proof remains valid at this spacing. Its frequencies $0,1\pm\gamma,-1\pm\gamma$ are distinct, so evaluation on that menu is an invertible exponential Vandermonde matrix for every fixed $H>0$. Its inverse changes only fixed coefficients, independent of target width. The older target's full constant-field generators remain uniformly capped over this finite menu. Whole-side logarithm truncation therefore still has degree $O_a(n+1)$ and coefficient mass $e^{O_a(n+1)}$.

No rival logarithm convergence, rate cap or reversible realization is invoked by that rank argument. Its finite clock-word matrix continues to factor through every arbitrary Markov rival's actual state space. It consequently supplies the polynomial unrestricted lower for the explicitly enlarged family and menu. The common word-chain upper supplies polynomial sufficiency, while the new reversible lower already uses the contained two-field menu. This validates the corollary without attributing its unrestricted lower to the tagged family alone.

## 7. A separate assumption-audit lead

The new fixed-clock lower may also permit unequal rival stationary masses on the same fixed binary label set $\{-\gamma,+\gamma\}$. The finite row recursion uses each model's own stationary law; Schur denominators are observed separately; binary label insertion uses the two label values; and weighted repair uses its recovered positive root mass. No explicit equality of the two histogram masses appeared in these reviewed steps.

This is a lead for a separate assumption audit, **not an additional theorem or a change of the current competitor class**. A strengthened statement would need to check the entire reduction and comparison definition and distinguish relaxing label masses from changing the label values or kinetic field rule. The current theorem and union corollary retain their stated exact-histogram assumption.
