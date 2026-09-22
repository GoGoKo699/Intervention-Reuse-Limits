# Current work order: assess the focused modeling contribution

## Completed checkpoint — 22 September 2026

This continuation started from clean `main` at `9cf4e64ca27624ee66bb75d93ba7fd215135ac43`. It preserves the MIT license, all six mathematical verifiers, and all saved reports.

The mathematical tolerance laws remain unchanged: at fixed positive W,U, unrestricted target rates require and admit `Theta(log^2(W U^3/tolerance))` states; active target rates at most `3k` require and admit `Theta(log(W U^3/tolerance))` states. This checkpoint makes their contribution and comparison classes explicit.

1. **A proved structure-cost corollary.** The unrestricted lower bound already applies to stationary analytic Markov surrogates with fixed arbitrary real readouts, without passive, static, linear, or quadratic matching requirements. For capped targets, filtering preserves the full coefficient-lift rank and the same witness estimates apply with `r=3D-1`. The reversible bounded-sensitivity constructions retain every prescribed agreement at the same asymptotic state-growth order. This does not assert equal finite-budget errors or leading constants.
2. **An exact diagnostic boundary.** Preparing equilibrium at field h and switching it off gives `m(t)=tanh(h) exp(-2kt)` for every internal K, at any finite h. The corresponding nonlinear perturbation-arrest relation is satisfied. Yet two three-state targets with fixed actuator parameters and different K have unequal cubic field-on responses. Passing passive and switch-off diagnostics does not certify driven reuse.
3. **A theorem-level publication comparison.** The individual response, realization, positive-reduction, Hankel, quadrature, and inverse-spectral mechanisms are established. The candidate contribution is their compatibility in a constrained Markov state-complexity theorem. The broad hidden-kinetics message is not a novelty claim.

Read `docs/PUBLICATION_SCOPE.md` first. The formal relaxed/original/reversible comparison is in `docs/STRUCTURE_COST.md`; detailed source access and attribution are in `docs/PRIOR_ART.md`. The existing proofs remain the source of the exact separation, upper bounds, and lower bounds.

The HMM comparison now goes beyond an abstract: indexed primary-manuscript excerpts supplied Kotsalis–Shamma's probability-law definitions and Theorems 4.1–4.2. Full PDF access remains unavailable and is not claimed. Direct passive-word-law approximation is vacuous for distinguishing our targets, because every one already has the same exact two-state passive realization. The historical Frazho full-text gap no longer blocks the classical-realization comparison: Petreczky's inspected theorem supplies a precise accessible counterpart.

## Scope decision

**Conditional go for a narrowly framed theoretical model-reduction contribution.** The result to assess is that optimal-order cubic response compression can retain reversibility, bounded sensitivity, and exact passive and prescribed low-order response behavior, even compared with Markov fits that abandon those requirements.

This is not a broad new physical law, a general claim that positivity is free, or a new approximation mechanism. The problem supplies the intervention kernel exactly and charges latent Markov states. Parameter precision, data acquisition, runtime, finite-amplitude error, and experimental resolution are not quantified. Exact lumpability and centered sensitivity are deliberate model choices, not generic molecular assumptions.

The intended user already has a microscopic kinetic model and needs a smaller Markov model reusable across bounded weak protocols. A target rate cap is information about active hidden relaxation times. A particular experimental platform is neither established nor necessary for the present mathematical statement.

The inspected results do not directly imply the whole combined theorem. That bounded comparison supports a focused candidate claim; it does not certify originality across the literature or establish a journal's significance threshold. Manuscript writing remains on hold.

## Single next priority

**Decide whether the focused theorem warrants a standalone theoretical paper, and define the smallest defensible publication claim.**

Use the completed comparison rather than reopening a general bibliography search. The exact remaining question is whether an existing result supplies the entire arbitrary-positive-kernel embedding behind the prescribed passive law, its reversible bounded-sensitivity field family, and the matching broad-surrogate state law in this response norm. A source covering only one ingredient does not resolve that question; an explicit reduction covering all of them would.

Assess significance for the identified model-reduction audience. Explain why the compatibility and fixed-actuator guarantees are useful relative to unconstrained fits, despite the standard approximation exponents. Distinguish a rigorous theorem note from a broad physics claim. Do not force a molecular interpretation or add new restrictions to make the result look more consequential.

End with a concrete recommendation: proceed on that bounded claim with an explicit working originality statement and appropriate audience, narrow it further with a stated reason, or record that the remaining distinction is too routine for a standalone project. Do not replace that decision with more examples, a longer bibliography, or an unsupported journal ranking. Expert assessment may improve confidence, but do not send messages or contact anyone without the user's explicit authorization.

No new numerical work or constant optimization is needed by default. Open finite-field, noisy-inference, robustness, or application extensions only if the selected publication claim requires a specific quantitative result; such an extension must have its own clear completion criterion. Do not turn every limitation into a new research branch.

## Evidence discipline

Run `make check` in the pinned Python 3.13 environment. Fresh reports go into `.check-output/`. Regenerate saved reports only when calculation sources change; never hand-edit metrics. Preserve the license, baseline verifiers, unrelated owner work, and non-forced Git history. Local PASS and GitHub Actions are separate evidence.

Keep source fiction, conversational material, and unrelated projects out of the public repository. Internal proof checks are not independent validation. A source excerpt is not a full-paper audit, and a mathematical result is not a novelty certificate. Do not draft the manuscript until the contribution assessment supports its specific claim.
