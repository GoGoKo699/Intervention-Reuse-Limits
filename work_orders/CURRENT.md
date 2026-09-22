# Current work order: close the general prediction-complexity gap

## New completed extension — 22 September 2026

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

**Narrow the remaining general-family complexity gap, especially the upper bound.**

The current interval runs from `exp(c sqrt(log(1/δ)))` necessary states to `exp(exp(C log²(16/δ)))` sufficient reversible states. Preserve the actual all-protocol/all-horizon mean norm and count every physical state. An improved construction must establish positive rates and its claimed structural properties; a stronger lower bound must transfer to actual finite errors against the stated competitor class.

The new lower bound already handles binary sensitivities, bounded internal rates, and a fixed minimum dwell time. Those features cannot by themselves recover the rank-one complexity law. Whether the optimum is different for unrestricted and reversible competitors is unresolved: existence of a reversible approximation does not answer that comparison.

Do not replace this quantitative question with more examples of a merely nonzero high-order coefficient, duplicate the weaker varying-moment construction, or silently change the prediction norm. Retain every completed theorem if a proposed improvement fails. Journal selection and manuscript drafting remain separate from the research task.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports belong in `.check-output/`. Regenerate saved evidence only from its verifier. Preserve the MIT license, baseline mathematical scripts and reports, unrelated owner work, and non-forced Git history. Build and provenance checks may be extended for new verifiers.

No large simulation is needed. Local checks and GitHub Actions are separate evidence. The hypothesis-testing results assume specified models, ideal recorded data, and stationary preparation; the cost of restoring that preparation is excluded. Do not contact prospective collaborators or send messages without explicit user authorization.
