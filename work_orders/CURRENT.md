# Current work order: close the general prediction-complexity gap

## New completed extension — 22 September 2026

This continuation starts from `b143adad62c8ec0d8b51733760d5c1c82bcaa213`. All fourteen preceding mathematical verifiers and reports are preserved. The polynomial-necessity target is now proved, including fixed control resolution.

For balanced binary sensitivities and a fixed internal spectral band, the worst-case actual-mean prediction cost satisfies `c_a δ^-γ_a ≤ D_* ≤ C δ^-p` for fixed positive exponents. Thus `D_*=δ^{-Θ(1)}` describes the growth class, not a matched optimal exponent. The lower holds for every fixed clock interval `a/k>0`, using only fields `0,h*`, held intervals that are integer multiples of `a/k`, and observation horizons `O_a(log(1/δ))/k`. Competing Markov predictors need only have fixed preparation and readout and rates depending on the instantaneous field; no competitor reversibility, rate bound, field analyticity, or passive matching is required.

Start with [the polynomial controlled lower theorem](../docs/POLYNOMIAL_CONTROLLED_LOWER_BOUND.md). Its positive shift-register target and exact Gram witness are inherited from the preceding checkpoint. The improvement is to truncate the logarithm expansions by **total degree across each whole side** of the response matrix. Each side has generator degree `O(n)` and exponentially bounded coefficient mass. A single total-degree cutoff `M=O_a(n)` controls its complete tail and has only `exp(O_a(n))` actual-propagator coefficient cost. Truncate the left and right sides separately; cutting the combined entry can destroy the rank factorization and is not the proof.

Target reversibility bounds powers of `I-exp(aQ_h)` in field-dependent equilibrium norms even for large fixed `a`. The finite truncated expressions are then evaluated exactly on arbitrary competitors, with no logarithm convergence claim for them. The witness has error floor `exp(-C_a n)` below `2^n` states, fixed minimum dwell `a/k`, and horizon `O_a(n/k)`. It closes the earlier logarithmic loss in the lower exponent. The polynomial upper remains possibly nonreversible, preserving the exact actuator distribution and all specified passive/static/low-order agreements.

The sharp lower and upper **exponents** remain open. So does polynomial reversible sufficiency: the current reversible finite-alphabet capped bound is `exp(C δ^-p log(2/δ))`. A different sufficient construction does not prove an intrinsic reversibility penalty. The wider class with arbitrary bounded sensitivities and unrestricted internal rates retains its double-exponential reversible existence bound.

## Earlier bounded-rate and shift-register checkpoint

This continuation starts from `04666225de07d520555144d26dee342097afb6bd`. All twelve preceding mathematical verifiers and reports remain unchanged. Two stronger lower bounds and a polynomial upper bound now address the same bounded-rate binary target class.

1. **Polynomial sufficiency with exact actuator distribution.** For a fixed alphabet of at most `m` sensitivities and internal relaxation rates at most `Λk`, set `R=exp((1+G)H)` and `p=log(m)/log(1+1/(ΛR))`. A stationary word-chain surrogate has at most `1+max(m,((1+2R²)/δ)^p)` total states. It preserves the entire actuator histogram and the passive/static/low-order constraints, but can lose reversibility. Exact uniformization and regeneration give the all-protocol/all-horizon bound directly.
2. **Stronger positive-rate necessary bounds.** Write `L=log(1/δ)`. Reversible shift-register targets with balanced sensitivity `±sqrt(W)` and internal rates in `[3k/2,5k/2]` force `D≥exp(c L/log L)` under unrestricted timing. Under a fixed minimum dwell `a/k`, the separate bound is `D≥exp(c_a L^(2/3))`. Both allow arbitrary instantaneous-field Markov competitors with fixed preparation and readout. Neither is a polynomial lower bound in `1/δ`.
3. **A sharper reversible sufficient count in the capped finite-alphabet class.** Prediction-function partitions and stationary-flux aggregation give `D_rev≤exp(C δ^-p log(2/δ))`, retaining the exact actuator histogram and both internal spectral-band endpoints when prescribed. No polynomial reversible upper bound or optimal cost of reversibility is established.

Start with [the bounded-rate upper theorem](../docs/BOUNDED_RATE_FINITE_FIELD.md) and [the shift-register lower theorem](../docs/SHIFT_REGISTER_LOWER_BOUND.md). For binary targets in `[k,3k]`, unrestricted predictors now have the interval `exp(c L/log L) ≤ D_* ≤ C δ^-p`. The strongest lower proof uses intervals shrinking like `(log n/n)^2/k` and horizons `O(n/k)`; the fixed-dwell proof has horizons `O_a(n²/k)`. These timing guarantees are different.

The shift register has constant operator coupling, replacing the earlier tree's exponentially shrinking coupling. A maximal Walsh-index projection gives an exact Gram floor exponential in word depth. Chebyshev derivative stencils convert generator words to actual mean experiments with controlled signed coefficients. Only target generators are approximated; the same finite propagator expressions factor exactly through every competitor's physical state space. The graph spectrum, interpolation, and rank machinery are classical. The constrained quantitative conclusion is the candidate contribution.

The new target has `2^(4n+3)+1` physical states, exact cubic minimum `4n+5` in the analytic-in-field competitor class, and full controlled-mean minimum at least `2^n` even in the broader competitor class. The older tree's cleaner `n+3` versus `2^n` exact separation remains valid. Its truncation analysis also shows why improving only its measurement filters cannot produce a depth-exponential error floor at the same state threshold.

## Earlier complexity and reversible-compression checkpoint

This continuation starts from `1d59285`. The preserved mathematical verifiers and saved reports remain regression baselines. New lower and upper bounds change the general-family assessment.

1. **General prediction costs more than every fixed power of the logarithm.** At fixed `k,G,W,H`, the worst-case physical state requirement for actual controlled-mean error `δ` is at least `c exp(c sqrt(log(1/δ)))`. The targets are reversible, have only the two sensitivity values `±sqrt(W)`, and keep all internal relaxation rates in `[k,3k]`. The lower bound allows arbitrary instantaneous-field Markov competitors with fixed readout and preparation, without field analyticity or passive matching. It uses only fields `0,h*`, with every nonzero held interval an integer multiple of `1/(8k)`. A target of size `2^(n+1)+1` defeats every competitor with fewer than `2^n` states below error `c exp(-C(n+1)^2)`.
2. **Cubic and full controlled prediction can have exponentially different exact state counts.** The same binary-tree family has an `(n+1)`-mode cubic kernel and needs exactly `n+3` states for cubic response in the established analytic-in-field competitor class. Its full finite-field controlled mean needs at least `2^n` states even in the broader competitor class. The target's original `2^(n+1)+1` states provide the exponential upper order.
3. **General compression can preserve reversibility and exact variance.** Every bounded-sensitivity target has an approximant inside the original reversible family, retaining the sensitivity bound, exact variance `W`, passive path law, equilibrium curve, reference linear mean, and zero quadratic mean. The guarantee concerns actual means under every allowed protocol and horizon. Quantization, reversible rate regularization, prediction-function partitions, and a two-replica moment construction prove a sufficient state count `exp(exp(C_G,H log²(16/δ)))`.

Start with `docs/GENERAL_CONTROLLED_LOWER_BOUND.md` and `docs/REVERSIBLE_GENERAL_COMPRESSION.md`. The lower and upper orders are far apart; no sharp general-family minimax law has been proved. Reversibility and exact variance are no longer obstructions to existence, but their additional optimal state cost remains unknown.

The lower proof constructs a binary-tree Gram matrix and replaces generator expressions by logarithm polynomials of fixed-duration propagators. Only the target is approximated in this step; arbitrary competitors are handled by exact rank factorization of the same finite polynomial expressions. Keep this distinction explicit. The signed coefficients can be large: this is a state-count theorem, not a stable experimental reconstruction method.

## Earlier general-family checkpoint

The preceding extension established three complementary results, retained as foundations.

1. **Arbitrary-order obstruction with an unchanged actuator.** For every `d≥2`, two `d+2`-state models share `k,μ,g`, the external field rates, a one-mode kernel, and every bounded-protocol mean coefficient through order `2d`. Complete visible-path coefficients agree through order `2d−1`. The next orders differ; every nonzero step separates the exact means. Only reversible hidden kinetics change, and their rates remain in `[λ,3λ/2]`. The common actuator and state space may change with `d`, and the separating signal may shrink.
2. **Complete general path information.** The stationary law of the hidden sensitivity process `g(X_t)` is equivalent to the collection of all controlled visible path laws. No-exit pulse functionals recover joint Laplace transforms noiselessly. A finite-rank actuator admits a matrix-return closure. A binary-actuator pair with identical two-time level kernels and spectra but different finite-field means rules out a naive two-time replacement.
3. **First general fixed-accuracy construction.** The finite-word Markov construction gave a size-independent upper bound but could lose reversibility and perturb variance. It remains a source of shared estimates and historical evidence. The new reversible exact-variance theorem supersedes those limitations.

See `docs/FIXED_ACTUATOR_HIERARCHY.md`, `docs/ACTUATOR_PROCESS.md`, and `docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md`. The hierarchy theorem is an exact identifiability obstruction; do not substitute it for the separate finite-error controlled lower bound.

## Earlier sharp and operational results

The rank-one sensitivity subclass remains quantitatively resolved. A scalar kernel determines the complete driven visible law, and actual controlled-mean approximation needs `Theta(log²(1/δ))` states, or `Theta(log(1/δ))` with active rates at most `3k`. Reversible constructions retain the model's prescribed structure. For unrestricted target rates, one fixed nonzero step already gives the lower order against arbitrary Markov competitors. See `docs/FINITE_FIELD.md` and `docs/FIXED_FIELD_LOWER_BOUND.md`.

The observation theorem proves universal first-order path response, complete second-order characterization by the kernel, and a sharp `r+2` second-order path state count. In a specified weak-step two-model test, two snapshots require `Theta(h^-4)` independent trials while the final snapshot alone requires `Theta(h^-6)`. The near-lumpability theorem bounds full passive-path relative entropy by `q^4(152+241kT)` under specified barrier disorder and gives a matching quartic information example with a finite active signal. See `docs/ACTIVE_PATH_RESPONSE.md` and `docs/NEAR_LUMPABILITY.md`.

The original exact and finite-accuracy cubic results, their two-state witnesses, and the structure-cost comparison remain valid and reproducible. Preserve their proofs, baseline scripts, saved reports, and provenance.

## Scientific position

The main candidate is the separation between passive simplicity, cubic-response complexity, and full controlled prediction, with general lower and structure-preserving upper bounds. Binary sensitivity and a fixed rate band already allow the stronger general obstruction. The sharp rank-one theorem identifies a tractable structural subclass; it must not be silently extended to all two-level actuators.

All constructors receive a known target. Approximate full path-law error over all horizons, noisy arbitrary-process learning, parameter precision, running time, and a molecular implementation are not established. The model's kinetic field rule is specified; equilibrium detailed balance alone would not determine it.

Response expansions, Hankel rank, positive approximation, reversible conditional-expectation reduction, and matrix-function approximation are established tools. The candidate novelty lies in the combined constrained statements and quantitative physical-state bounds. Internal proofs and source comparisons are not external validation or a certification of originality. Manuscript writing remains on hold.

## Single next research priority

**Determine the optimal cost of retaining reversible dynamics in the bounded-rate binary class.**

Polynomial necessary growth is established. Focus on a reversible predictor of polynomial size, or a rigorous lower bound that separates reversible from unrestricted predictors. Retain ordinary detailed balance, the exact actuator histogram, fixed binary readout, and the all-protocol/all-horizon mean guarantee; specify separately whether the spectral band is also retained. The current sufficient bounds alone imply no structural penalty. Improving the unmatched polynomial exponents is a secondary quantitative direction.

Two exploratory routes did not settle that question. Exact reversible three-symbol matching has a small realization, but its extension needs consistent transition relations between conditional prediction profiles. Matching only their Gram and projected one-step moments is insufficient: dynamics outside the retained profile space can return and change later correlations. These are limitations of proposed certificates, not impossibility results for polynomial reversible compression. Do not substitute finite-prefix success or moment matching alone for a controlled-mean approximation proof.

Maintain the primary-source comparison for the complete physical theorem. Matrix logarithms, formal power series, finite-word rank, the de Bruijn/Walsh spectrum, uniformization and canonical word approximation are classical. The candidate contribution is their constrained quantitative consequence: a fixed-resolution intervention task with polynomial physical state cost behind an exact two-state passive law. A growth-class theorem does not certify publication originality. The all-sensitivity, unrestricted-rate upper theorem concerns a broader class and remains a separate question.

Do not replace this quantitative question with more examples of a merely nonzero high-order coefficient, duplicate the weaker varying-moment construction, or silently change the prediction norm. Retain every completed theorem if a proposed improvement fails. Journal selection and manuscript drafting remain separate from the research task.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports belong in `.check-output/`. Regenerate saved evidence only from its verifier. Preserve the MIT license, baseline mathematical scripts and reports, unrelated owner work, and non-forced Git history. Build and provenance checks may be extended for new verifiers.

No large simulation is needed. Local checks and GitHub Actions are separate evidence. The hypothesis-testing results assume specified models, ideal recorded data, and stationary preparation; the cost of restoring that preparation is excluded. Do not contact prospective collaborators or send messages without explicit user authorization.
