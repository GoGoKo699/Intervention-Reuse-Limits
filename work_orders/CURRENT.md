# Current work order: establish the publication contribution

## Completed checkpoint — 22 September 2026

This continuation started from clean `main` at `57c0e12bdde4d8a38dc355d6797126debd7a6e76`. It preserves the MIT license, all five earlier mathematical verifiers, and their saved reports.

**The unrestricted tolerance-order gap is closed.** For `D>=2`, put `r=3D+2`. The original broad minimax problem satisfies

`E_D >= W U^3 exp[-2 pi sqrt(3(r-1))] / (64 r^2)`.

The earlier positive-quadrature and reversible-realization upper bound therefore has the optimal worst-case state-growth order: `Theta(log^2(W U^3/tolerance))` at fixed positive W,U. The separately defined target class with active rates at most `3k` has the already proved `Theta(log(W U^3/tolerance))` order. Both lower bounds retain the full analytic Markov surrogate class, including nonreversible models, Jordan blocks, and unrestricted generator derivatives. Constants in the error exponents are not matched.

The new proof uses geometrically separated target rates, the continuous Hankel operator of the cubic step curve on a probability-weighted function space, and an explicit Cauchy-inverse bound. The target has `3D+4` states, mass W, and pointwise sensitivity magnitude `sqrt(W)`. Its minimum active rate is fixed at `5k/2`; its maximum rate grows with D. A finite-horizon version loses only a factor of two and uses the curve through time `O(sqrt(D)/k)`. It is not a finite-sample or noise-certified measurement theorem.

Proof: `docs/UNRESTRICTED_RATE_LOWER_BOUND.md`. Definitions and quantifiers: `docs/FINITE_ACCURACY.md`, Section 0. Upper bounds and fixed-band lower bounds remain in that note; the exact theorem and minimal reversible realization remain in `docs/THEORY.md`. The new deterministic verifier and generated report check the calculation identities and small high-precision witnesses. `docs/VERIFICATION.md` records the exact computational scope.

## Candidate publication scope

The mathematical story is now complete at the level of worst-case tolerance order:

1. Complete passive binary path equality can coexist with arbitrarily large exact cubic-response state complexity.
2. At fixed coefficient tolerance and bounded sensitivity, a model of size independent of the microscopic target size is sufficient.
3. The worst-case number of states grows as a squared logarithm of inverse tolerance without a target rate cap, and as a single logarithm with a fixed cap.

The same scalar actuator, binary mean readout, stationary preparation, and low-order response constraints must remain explicit. This is a theorem about analytic Markov model reuse and Taylor coefficients. It is not a result about memory bits, learning from data, arbitrary dynamical surrogates, finite-amplitude prediction, or turbulence.

The linear coefficient lift, Hankel-rank obstruction, Cauchy inverse, positive quadrature, and inverse spectral realization are classical ingredients. Their combination into this response-norm theorem does not by itself establish a publishable contribution. Manuscript writing remains on hold.

## Single next priority

**Determine the precise contribution beyond the closest existing response and stochastic-realization theorems, and explain its operational significance.**

Prepare a theorem-by-theorem comparison with explicit assumptions, resource, norm, and conclusion. Prioritize nonlinear/Volterra realization, HMM approximation lower bounds, controlled coarse-graining with the same actuator, and approximation of positive relaxation spectra. The prior-art note distinguishes inspected full text from abstract-only leads; Kotsalis–Shamma and Frazho remain concrete full-text comparison gaps unless that record is updated after successful retrieval.

The comparison must end in a substantive conclusion: an explicit reduction showing that the combined result is already covered, a narrower defensible distinction with clearly identified remaining uncertainty, or a concrete missing theorem needed for that distinction. A larger bibliography or the absence of an exact-title match is not completion. If the theorem is a corollary of established work, record that candidly and reassess publication scope rather than renaming standard ingredients.

Explain what the state-count law tells someone choosing a reusable kinetic model, why the same actuator matters, and what extra information a target rate cap supplies. The hard unrestricted examples require increasingly fast modes; the proof gives no temporal-resolution guarantee for acquiring their coefficient curves. Do not infer a robust experimental cost law from the current idealized norm. Select a physical interpretation only when its assumptions have identifiable precedent; do not add arbitrary surrogate restrictions or new devices merely to force significance.

Do not optimize constants or add more numerical examples unless that resolves a concrete issue in the theorem comparison. Keep finite-field remainder control and noisy coefficient acquisition separate; open either only if a chosen operational claim needs it. A full finite-amplitude or statistical extension is not automatically required for the current theoretical scope.

## Evidence discipline and completion rule

Run `make check` in the pinned Python 3.13 environment. Fresh reports go into `.check-output/`. Regenerate saved reports when calculation sources change; never hand-edit metrics. Preserve the original license, all baseline verifiers, unrelated owner work, and non-forced Git history. Local PASS and GitHub Actions are separate evidence.

Keep the public repository free of source fiction, conversational material, and unrelated projects. Do not claim independent validation from internal checks, experimental implementation, acceptance, or a journal tier. A mathematical result and a publication assessment must remain distinct.

The next checkpoint must deliver the substantive comparison and resulting scope decision, with synchronized repository claims. Another plan, bibliography, simulator, or manuscript draft alone is not completion.
