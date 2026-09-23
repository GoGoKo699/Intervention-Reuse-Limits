# Internal review of finite minimality and observation precision

[Minimum-count theorem](FINITE_PREDICTOR_MINIMALITY.md) · [Gram refinement](FINITE_GRAM_ROBUSTNESS.md) · [Observation boundary](FINITE_OBSERVATION_BOTTLENECK.md) · [Source supplement](FINITE_PRECISION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**Internal mathematical audit, 23 September 2026.** The three new notes pass the reviews recorded here. These are separate internal derivation and code reviews, not external peer review or novelty certification. The earlier finite construction, verifiers and proof snapshots remain unchanged.

## 1. Minimum counts and the positive-factor distinction

The minimum-count theorem retains the existing target, two fields, clock, stationary preparation, readout, field-independent hidden generator and hidden exit cap $2k$. It proves $D_{\rm all}=11$ and $D_{\rm ord}=12$ throughout $0\le\delta\le2^{-1360}$ using at most 520 ticks per experiment. It imposes neither inherited rival labels nor a histogram promise.

The reversed positive feature words are legitimate nonnegative kernels in every rival. Without reversibility they are not stationary adjoints. Nevertheless, the matrix $N_{ij}=\mu L_iR_j1$ factors through the rival's hidden states with two independent nonnegative factors. On the target it equals the known Gram matrix. This distinction was checked analytically and, independently, on the explicit nonreversible predictor: its formal-reverse matrix equals the target matrix while its actual feature Gram does not.

The support-cover proof was checked in both cases of its rigid edge-box argument. Four positive rectangles cannot cover the seventeen supported cells of the leading block; five row stars can. Each of the five isolated diagonal cells requires a separate rectangle, giving full nonnegative rank ten. Ordinary rank nine is insufficient for this lower. The prior completely positive rank eleven gives the additional ordinary-reversibility requirement.

The robust nonnegative-rank proof uses the rank-one cross-product identity. Assigning every positive target cell to a sufficiently contributing factor forces each factor's assigned cells into a positive rectangle whenever

$$
81\varepsilon(1/8+\varepsilon)<(1/48-\varepsilon)^2.
$$

At $\varepsilon=1/40000$ the exact margin is $16183/90000000>0$. This step requires no normalization of individual factors or minimum stationary mass. The finite verifier independently enumerates all maximal support rectangles and every four-rectangle candidate; that bounded enumeration supports the written combinatorial proof.

## 2. Centered logarithms and the common finite budget

Every full generator has exit cap four in units $k=1$, even without detailed balance. With $a=(\log2)/8$, the entrywise nonnegative matrix $Q+4I$ gives

$$
\sqrt2 E=\exp[a(Q+4I)]\ge I,
\qquad \|I-\sqrt2 E\|_\infty=\sqrt2-1<5/12.
$$

The logarithm identity follows along the continuous path $\exp[ta(Q+4I)]$, whose centered defect has norm below one. This avoids any assumption of reversible eigenvectors or an ambiguous logarithm branch. The degree-zero logarithm constant is included in both majorants.

At operator bookkeeping radius two and formal coefficient radius one third, each generator majorant is below $\log9/a<32$. Whole-polynomial truncation, preserving factor order, therefore has tail $J32^d2^{-(N+1)}$ and coefficient mass at most $J32^d3^N$. The inserted-visible-projector recursion uses stationarity and the shared interface, so it applies to nonreversible rivals too. Its cost is at most $(1+7N)\delta$ and adds no ticks.

The unchanged feature-polynomial bounds $d\le42$ and $J\le2^{289}$ give $J32^d\le2^{499}$. At $N=520$ and $\delta=2^{-1360}$, the two-model tail is at most $2^{-21}$, while propagated mean error is below $2^{-17}$. Their sum is below $2^{-16}<1/40000$, sufficient for both the nonnegative-rank and older completely-positive-rank obstructions. The horizon is $65\log2/k$.

The finite ordinary-entropy-production corollary substitutes $\eta=\delta/22$ into the previously proved regularization. It retains eleven states and gives error at most $\delta/2$ for $|h|\le\log2$. The entropy bound refers to the full zero-field identity-reversal rate $\sigma_0$, not the hidden rate or driven heat. No same-size generalized-reversible construction is asserted.

The root reviewer, construction-independent route reviewer and verifier author each checked the full minimality proof. A separate matrix reviewer checked the support and positive-factor arguments before the centered-log refinement; that earlier partial review is not counted as an independent review of the final logarithm proof.

## 3. Sharper Gram radius

The eleven auxiliary square-root edge/isolate vectors lie in the hypothetical factorization's atom space. Their overlaps follow from Cauchy–Schwarz and target-zero entries. Each edge has two other edges sharing its size-two-part endpoint, one sharing its size-three-part endpoint, and two disjoint edges.

At $\varepsilon=1/1500$, the six-edge block has smallest eigenvalue strictly greater than $1/6000$. The five-isolate block is bounded below by $2/25$, and the cross-block Schur correction is at most $1/6000$. Strict positivity gives rank eleven, contradicting ten or fewer atoms. The root reviewer, route reviewer and verifier author independently checked these constants and the strict inequality. This improves the intermediate matrix radius by $80/3$; it is not a measured-mean radius and is not needed for the new $2^{-1360}$ certificate.

## 4. Observation-method boundaries and attribution

Nonnegativity on an interval forces even multiplicity at every interior zero. This proves minimum degree ten for exact six-label diagonal polynomial selectors and uniqueness of squared Lagrange interpolation at that degree. The large off-grid coefficient and value are exact rational calculations. They do not lower-bound the best possible observation conditioning or actual rival prediction error.

Normalized squared selectors are bounded and retain the target projectors. The identity $\sum_jL_j=1$ implies $\sum_jL_j^2\ge1/6$; the verifier checks the corresponding coefficientwise sum-of-squares identity. Quantitative observation of inverse denominator insertions remains open.

The separate selective-gate star example has $K=0$ and lies outside the target's hidden band. Its compressed physical propagator retains a constant-selected-mode floor $rm/(1+rm)$, equal to $2/3$ for $r=4,m=1/2$. This rules out identifying one strong fixed-bias pulse with a killed hidden projector. It does not exclude all finite-time certificates. The observation reviewer audited the complete boundary note, and the root reviewer checked the algebra and scope.

The source supplement identifies the exact unscaled core matrix in prior work, including Fawzi–Parrilo Eq. (55), and records the access limits for an earlier attribution. The controlled realization and scalar recovery remain separate obligations. Neither the core matrix, its exact positive-rank gap, nor the general rectangle-cover method is claimed as new.

## 5. Frozen proof snapshots and code review

| Proof note | SHA-256 |
|---|---|
| `FINITE_PREDICTOR_MINIMALITY.md` | `393714abcd79e5c9b7d7c4184c4dd892ebd635265aff3edab5be3c7ed5f527e5` |
| `FINITE_GRAM_ROBUSTNESS.md` | `430735bd478fd76d9ce964bd51cc88b63c2055d988a379052a16e524dd7084b8` |
| `FINITE_OBSERVATION_BOTTLENECK.md` | `360361d398d33270242b835d9705efd798dc60c328c769cb615fafd63748e427` |

The [new verifier](../scripts/verify_finite_minimality.py) and [saved report](../reports/finite_minimality.json) bind these snapshots. The root review covers all source branches, exact arithmetic, enumeration completeness, matrix orientation and report limitations. A separate full source review also passed, with a byte-identical report from an independent pinned Python 3.13.5 rerun. Independent rerun and full-suite evidence belong to [Verification](VERIFICATION.md). Bounded code checks supplement the analytic arbitrary-rival proofs; no large protocol family is enumerated and no practical sample guarantee follows. Manuscript drafting remains deferred.
