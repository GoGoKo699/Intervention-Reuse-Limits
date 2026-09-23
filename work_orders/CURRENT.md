# Current work order: integrate the reversibility separation and reduce its actuator alphabet

## Recovery and current result — 22 September 2026

The preceding integrated baseline is `80253e1462d618ccc435f2394aba240e858496b5`, with twenty-five mathematical verifiers. After the workspace disconnected, the new proof material was preserved in commit `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`, under [the recovery checkpoint](../research_checkpoints/2026-09-22-reversibility/README.md). This continuation promotes those notes into the main documentation and completes their verification. The expanded twenty-eight-verifier gate passes in pinned Python 3.13.5; all twenty-eight fresh reports match their saved evidence. A byte comparison preserves the fifty-three protected baseline files and all nine recovery files. Local verification and GitHub Actions are separate evidence. Preserve the twenty-five baseline scripts and reports, MIT license, pinned dependencies, workflow and unrelated work.

The main candidate is the [dynamic-lamp reversibility theorem](../docs/DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md). On one common target family, the worst-case minimal state counts satisfy

$$
D_{\rm all}^{(3)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{(3)}(\delta)=\exp(\delta^{-\Theta(1)}).
$$

Both predictor classes retain the original exponential kinetic rule, exact nineteen-level histogram, stationary zero-field preparation, binary readout, and internal outgoing-rate budget $3k$. The histogram is mass $1/2$ at zero and mass $1/36$ at each of $\pm j/100$, $j=1,\ldots,9$, with $G=9/100$ and $W=19/12000$. Only the second class additionally requires ordinary reversibility. Rivals may use arbitrary new states, with no partition, encoder or inherited-coordinate restriction. Targets and the reversible upper retain the internal band $[k,3k]$. The reversible lower at cap $6k$ covers all reversible rivals with internal exits at most $3k$; no lower gap is imposed on those rivals. Do not assign a reversible spectral band to the nonreversible word-chain upper.

Both lower bounds hold already on thirty-nine fixed field values, at every fixed positive clock $a/k$, with witnessing horizons $O_a(\log(1/\delta)/k)$. The uppers serve all bounded protocols and horizons. Constants can depend on the clock, and exponents are unmatched. This is a state-count statement, not a bound on samples, parameter precision or runtime.

For width $n$, the target has $r=2^n$ addresses and $18r2^r+2$ counted physical states. Positive gate blocks query and independently flip table bits. Ordinary reversibility and the fixed cap transfer mean accuracy to reverse-word moments. [Balanced transport repair](../docs/POSITIVE_TRANSPORT_REPAIR.md) builds stationary couplings on the rival's existing states; deterministic rounding then yields an $r$-bit law nearly invariant under each separate bit flip. Entropy forces exponential support. A distinct target-only Gram-rank argument supplies polynomial necessity even for arbitrary Markov rivals. Keep these two lower arguments and their different competitor assumptions separate.

Supporting extensions are the [soft-aggregation lower](../docs/SOFT_AGGREGATION_LOWER_BOUND.md), [observable aggregation rigidity](../docs/OBSERVABLE_AGGREGATION_RIGIDITY.md), [general reversible word observability](../docs/REVERSIBLE_WORD_OBSERVABILITY.md), and [exact fifteen-symbol reversible-prefix obstruction](../docs/EXACT_REVERSIBLE_PREFIX_OBSTRUCTION.md). The soft architecture is the established Bayes-reversed stochastic encoder, and the exact-prefix result is a zero-error statement. Neither substitutes for the positive-error dynamic-lamp proof.

The proof has passed internal audits; the [primary-source comparison](../docs/PRIOR_ART.md) identifies established lamp-growth, entropy, positive-realization and aggregation ingredients. Internal audits and bounded literature search do not certify originality. Binary actuators, unbounded-rate reversible rivals and arbitrary reversible field rules remain outside the separation. Manuscript drafting remains on hold.

The entries below record earlier research states. Their statements of what was then open are historical; the current nineteen-level theorem and the next priority below supersede the old general finite-alphabet question.

## Historical checkpoint: aggregation versus fresh realization — 22 September 2026

This continuation starts from `cd8f21a8f8f9d25cd1645ee6a165d1061e0ff3e0`. All twenty-three preceding mathematical verifiers and saved reports are preserved.

The [aggregation lower](../docs/AGGREGATION_STATE_LOWER_BOUND.md) and [uniform register-scenery upper](../docs/REGISTER_SCENERY_COMPRESSION.md) establish an exponential architectural separation on the same fixed six-level target family. The actuator values are `±1/10,±2/10,±3/10`, each of mass `1/6`, so `G=3/10`, `W=7/150`; the advertised internal band remains `[3k/2,5k/2]`. Every target retains the exact passive two-state law and original exponential field rule.

Every stationary-flux partition aggregate that keeps `A` separate and refines the actuator levels requires at least `exp(c_a δ^-γ_a)` states in the worst case. This allows arbitrary unequal cells and arbitrary mixing of the original coordinates within each actuator level. A fresh-state reversible predictor has the uniform sufficient count `C δ^-p`, with `p=log(96)/log(1+2/[5exp((13/10)H)])`. The exact query-feature Gram matrix is `I_(2^n)/6`, so unrestricted predictors also have a polynomial lower. The general prediction-partition theorem supplies a singly exponential aggregation upper. Both growth classes are therefore determined, with unmatched exponents. The lower bounds hold at any fixed positive control clock. The larger cost is intrinsic to this aggregation architecture, not an intrinsic cost of reversibility.

The lower target contains a binary register, three ports, a sign and a complete independent bit table; every coordinate is counted. Partial-isometry gate words, exact field-generator interpolation and a telescoping projection-loss identity connect actual mean accuracy to reconstructing the table bits. An elementary entropy bound forces exponentially many partition cells. The upper replaces a wide register by a smaller register with nearly identical short affine-dihedral trajectory statistics, then selects complete configurations with positive weights. This gives the same-family upper at all accuracies and all original widths, rather than just at the lower witness sequence.

The qualitative distinction between aggregation and realization is known. The publication candidate is the robust exponential-versus-polynomial state law under these shared physical restrictions. Arbitrary fitted rates on partition cells and a binary-actuator architecture theorem remain outside this lower. The general cap-only reversible question and arbitrary frozen labels on expanders remain open. Manuscript drafting stays on hold.

## Historical checkpoint: fixed-label connected expanders — 22 September 2026

This continuation starts from `b9553f7fa3498dcc8dd7210de0b1aa0fc24a93e3`. All twenty-one preceding mathematical verifiers and saved reports are preserved.

The [new upper theorem](../docs/EXPANDER_SCENERY_COMPRESSION.md) and [new lower theorem](../docs/EXPANDER_SCENERY_LOWER_BOUND.md) put polynomial necessary and reversible sufficient switching growth in the same class of connected uniformly mixing sparse local targets. Each target has one frozen binary labeling on a degree-four logarithmic-girth expander, a dynamic two-state sign layer and stationary refresh. Every coordinate is counted: the full target has `2N+1` states. The sign layer gives an exactly balanced actuator histogram for every labeling. The original field rule and advertised internal band `[3k/2,5k/2]` remain exact.

The upper's event has probability greater than `3/4` for each supplied graph and is independent of accuracy: every labeling in it supports the polynomial reversible bound at all accuracies. High-girth local walk statistics, including sign flips, match an annealed reference on a smaller graph. Positive selection of whole components gives a physical reversible realization. Countable bounded-differences estimates and refresh-run coupling control the frozen-label error. Exact retention of small targets closes the size/accuracy case split.

The lower uses geodesic Walsh leaves, an explicit global-centering leakage bound, an expected Gram estimate averaged over every endpoint, and concentration. Its event intersects the same all-accuracy upper class. Actual-mean error below `exp(-C_a n)` requires at least `2^n` states, even at any fixed clock `a/k` and against arbitrary instantaneous-field Markov predictors. The resulting polynomial exponents are unmatched. The analytic logarithmic constant-step upper applies; a matching step lower in this particular class remains unproved.

These local generators have a uniform positive gap, so bounded-size fragmentation has nonvanishing stationary-flux cost. Every positive conductance-density moment diverges with size. The theorem therefore goes beyond both preceding sufficient hypotheses. It does not cover all deterministic labelings or solve the general cap-only reversible problem. The graph constructions, concentration, convex selection and rank methods are established ingredients; publication novelty is not certified. Manuscript drafting remains on hold.

## Historical checkpoint: local walks and sparse reversible compression — 22 September 2026

This continuation starts from `2ede88ab4d5cc0be6075e7f881bc66ec07ebb12b`. All nineteen preceding mathematical verifiers and saved reports are preserved.

[Sparse reversible compression](../docs/SPARSE_REVERSIBLE_COMPRESSION.md) replaces a density condition by a stationary-flux fragmentation profile. If local edges can be deleted at directed stationary flux at most `εk`, leaving components of at most `S(ε)` vertices, retain a positive convex combination of at most `m^(ell+1)` whole components matching the stationary actuator prefixes. Restoring the same independent global refresh preserves these prefix laws exactly. The state count is `1+S(ε)m^(ell+1)` and actual all-protocol/all-horizon mean error is at most `R³ε+C_R q_Λ^(ell+1)`.

For nearest-neighbor local networks in fixed dimension `d`, random grid offsets give `S(ε)≤max(1,ceil((Λ-c)/ε))^d` when `K=L+ck(Π−I)`. The reversible upper is `C δ^{-(d+p_Λ)}` and retains the original field rule, exact actuator histogram, upper cap `Λk`, and lower gap `ck` when `c>0`. Paths and cycles have exponent `1+p_Λ`. A cap-preserving small-refresh repair handles `c=0`, without retaining a fixed lower gap.

[The local-walk lower](../docs/LOCAL_WALK_LOWER_BOUND.md) uses hidden states `(x,i)`, with an independent binary string `x` of length `4n+3` and a position on its path. The actuator is `sqrt(W) x_i`; local jumps have rate `k/4`, and stationary refresh has rate `3k/2`. All nonzero internal relaxation rates lie in `[3k/2,5k/2]`. A unique maximal-distance Walsh contribution gives a `2^n` Gram witness with floor `48^(-4n-2)/[2(4n+3)]`. The existing total-degree logarithm transfer gives polynomial necessity at every fixed positive control clock, with horizons `O_a(log(1/δ)/k)`.

The same one-dimensional class therefore has passive cost exactly two, constant-step cost `Θ(log(1/δ))`, and switching cost `δ^(-Θ(1))` both with unrestricted and with reversible predictors. The switching upper preserves the original rate rule and band; the analytic constant-step upper still allows different rate functions. Polynomial exponents are not matched, so equality of the optimal reversibility costs is not proved. Along the switching witnesses, the exact cubic minimum is `4n+5`.

The path dictionary can have unbounded density moments, so this is a separate positive route beyond density clipping. Its small-cut assumption does not follow from a spectral cap or bounded degree alone. A local Poincaré gap gives a direct lower bound on the stationary cost of fragmentation; that limits this construction, not every reversible predictor. No manuscript drafting, scenery-learning guarantee or novelty certification is implied.

## Historical checkpoint: analytic step models and density tails — 22 September 2026

This continuation starts from `3f2bb0924a269c9ff4ce7ccb582e334e59c48c58`. All seventeen preceding mathematical verifiers and saved reports are preserved.

[Analytic constant-step compression](../docs/ANALYTIC_CONSTANT_STEP_COMPRESSION.md) removes the earlier discontinuous field dependence without changing the logarithmic state order. One real-analytic reversible predictor retains fixed stationary zero-field preparation, strict positive rates, a full spectral band, exact passive paths and static mean, and the universal linear and zero quadratic mean response for every bounded weak protocol. Regularizing the spectral measure prevents moment-rank changes; two active Jacobi cores and an analytic commuting reset interpolation enforce the preparation and passive calibration. Field derivatives may grow as tolerance decreases, and the original exponential actuator rule is still not imposed.

[Density-moment reversible compression](../docs/MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) allows unbounded individual density values under a global bound `E_(μ⊗μ)[q^(1+a)] ≤ M`, for fixed `a>0`, with `q_ij=K_ij/(kμ_j)` off the diagonal and zero on the diagonal. At fixed internal cap `Λk`, the state bound is `C δ^{-[2(1+p_Λ)+1/a]} log³(2/δ)`, where `p_Λ=log(m)/log(1+1/(ΛR))`. It retains the original actuator rule and exact histogram; the surrogate internal cap is `2Λk`. A more general sufficient count depends on the stationary tail `E(q−B)_+`.

The key sampling change keeps the clock at `Λk`: after clipping, Bernstein concentration uses the fixed row-exit bound, and one common rate rescaling restores stochasticity before adding a small reversible reset. The clipping threshold appears in the sample prefactor rather than the regenerative exponent. The actual clipping error is bounded by `R³ E(q−B)_+`, using the dimension-free driven occupation bound `p(B_i)≤R² μ_i`.

A matching-plus-refresh target proves that a spectral cap alone cannot justify uniform density clipping: it retains a finite driven signal as its density spikes grow, yet is exactly compressible to three physical states. This rules out that shortcut, not a general polynomial reversible predictor. The cap-only question remains open. No manuscript drafting or novelty certification follows from these extensions.

## Historical checkpoint: experiment menus and reversible sampling — 22 September 2026

This continuation starts from `c2740b58734deda54f30463395362ef7368cb034`. All fifteen preceding mathematical verifiers and saved reports are preserved.

The central comparison is now passive observation versus constant-field steps versus switching on the same bounded-spectrum binary target class. The costs are exactly `2`, `Theta(log(1/δ))`, and `δ^{-Theta(1)}` physical states. The last expression has unmatched positive lower and upper exponents and remains necessary at every fixed control clock. Start with [constant-step compression](../docs/CONSTANT_STEP_COMPRESSION.md) and [the polynomial switching lower](../docs/POLYNOMIAL_CONTROLLED_LOWER_BOUND.md).

The step upper works for all original bounded sensitivities with an internal cap, without an alphabet restriction. A positive equilibrium covariance measure has a uniform compact rate interval. Positive quadrature, shifted Jacobi realization, stationary reset, and a small fixed-preparation perturbation give one common reversible, irreducible predictor with stationary zero-field preparation, exact passive telegraph law and static mean, and a full spectral band. Its field-dependent generators need not be continuous or follow the original actuator rule. Field-function complexity is not charged by physical-state count. It has no switching guarantee. The logarithmic lower for the capped step menu may use an amplitude shrinking with state budget.

For switching, [bounded-density reversible sampling](../docs/BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) proves polynomial sufficiency under `K_ij/μ_j ≤ Lk` for every distinct hidden pair, with a fixed finite actuator alphabet. The state bound is `C δ^{-2(1+p_L)} log³(2/δ)`, where `p_L=log(m)/log(1+1/(LR))`. The predictor stays in the original field-rule family, preserves the exact actuator histogram, and has internal spectral cap `2Lk`. The original gap and band are not asserted. A bounded spectrum alone does not imply bounded conductance density; the fixed-band shift registers demonstrate the distinction.

These results improve the conceptual task comparison and resolve a concrete reversible subclass. They do not settle polynomial reversible sufficiency under a spectral cap alone, identify the optimal switching exponent, or certify publication novelty. Manuscript writing remains on hold.

## Historical checkpoint — 22 September 2026

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

The main candidate is now an intrinsic reversibility cost for controlled prediction: exponential versus polynomial state growth under the same field rule, histogram and outgoing-rate budget, using nineteen fixed actuator values. The separation between passive simplicity, cubic-response complexity, and full controlled prediction remains complementary. Binary sensitivity and a fixed rate band already allow polynomial switching necessity, but the exponential reversible lower has not been reduced to two actuator values. The sharp rank-one theorem identifies a tractable structural subclass; it must not be silently extended to all two-level actuators.

All constructors receive a known target. Approximate full path-law error over all horizons, noisy arbitrary-process learning, parameter precision, running time, and a molecular implementation are not established. The model's kinetic field rule is specified; equilibrium detailed balance alone would not determine it.

Response expansions, Hankel rank, positive approximation, reversible conditional-expectation reduction, and matrix-function approximation are established tools. The candidate novelty lies in the combined constrained statements and quantitative physical-state bounds. Internal proofs and source comparisons are not external validation or a certification of originality. Manuscript writing remains on hold.

## Single next research priority

**Reduce the nineteen-value actuator alphabet in the intrinsic reversibility separation, aiming for a binary actuator.**

First finish the recovered checkpoint's exact small-model checks, integrate all new verifier/report pairs, and run the pinned complete suite while preserving the prior evidence. Record local and CI outcomes separately. The mathematical next step then targets the alphabet: separate port sensitivities currently make gate extraction a fixed Vandermonde interpolation. A binary replacement needs another way for actual mean experiments to expose positive gate blocks on every allowed rival. Merely encoding a port label in an auxiliary target coordinate does not supply a corresponding observable port in an arbitrary new-state predictor. All auxiliary coordinates must be counted.

Keep ordinary detailed balance, stationary preparation, exact actuator histogram, the prescribed field rule, fixed binary readout and the all-protocol/all-horizon actual-mean norm. Seek a common outgoing-rate budget for the reversible and nonreversible comparison, and state separately any retained spectral band. The existing binary positive routes through density moments, small-cost fragmentation and typical fixed labels on logarithmic-girth graphs help identify structural boundaries. They do not prove a universal binary upper. Arbitrary fixed expander labels remain a concrete subquestion.

A second major boundary is removal of the competitor rate cap. The current scalar logarithm transfer controls both models and depends on fixed reversible spectral caps. Failure of that transfer without a cap is a limitation of the proof, not a cap-free theorem. Allowing arbitrary reversible field dependence is a further distinct change of competitor class. Sharp exponents and simpler physical constructions remain useful refinements after the main scope is secure.

The exact fifteen-symbol result rules out a dimension bound for exact reversible prefix realization depending only on fixed alphabet and prefix length. It does not by itself give a positive-error lower. The soft-aggregation result extends the prior partition obstruction to a specified stochastic-encoder architecture, while the dynamic-lamp lower already handles arbitrary new-state reversible rivals under the fixed budget. Keep these results distinct.

Maintain the primary-source comparison for the whole theorem. Lamp/Følner growth, entropy, positive realization, stationary transport repair, matrix logarithms, uniformization, word approximation, and finite-word rank have established antecedents. The candidate contribution is the constrained quantitative bridge from actual controlled means to exponentially many reversible predictor states. Do not infer publication originality from a growth-class theorem or the absence of a match in a bounded search.

The analytic constant-step construction's original-rule and uniform-derivative refinements concern a separate task. The all-sensitivity, unrestricted-rate reversible upper also remains broader and quantitatively unresolved. Do not replace the present question with another merely nonzero high-order response coefficient or change the prediction norm. Retain every completed theorem if an attempted improvement fails. Journal selection and manuscript drafting remain separate from research development.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports belong in `.check-output/`. Regenerate saved evidence only from its verifier. Preserve the MIT license, baseline mathematical scripts and reports, unrelated owner work, and non-forced Git history. Build and provenance checks may be extended for new verifiers.

No large simulation is needed. Local checks and GitHub Actions are separate evidence. The hypothesis-testing results assume specified models, ideal recorded data, and stationary preparation; the cost of restoring that preparation is excluded. Do not contact prospective collaborators or send messages without explicit user authorization.
