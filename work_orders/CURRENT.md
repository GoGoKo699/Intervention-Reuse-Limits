# Current work order: the remaining unrestricted tolerance gap

## Completed checkpoint — 22 September 2026

This continuation started from clean `main` at `78004603026a8058983e471f0bad73b2310abc12`. It preserves the existing MIT license, all four earlier mathematical verifiers, and their saved reports.

The earlier checkpoint established exact passive two-state compression versus arbitrarily large exact cubic-response state count; positive-quadrature compression with `O(log^2(1/tolerance))` states; and an `r+2`-state reversible realization of an `r`-mode kernel. This checkpoint adds actual response-norm lower bounds:

1. **Complete two-state characterization and witness.** Every admissible two-state model has rates `k r(h) exp(±h)` with `r(0)=1`, `r'(0)=0`. Its cubic freedom is one unrestricted real coefficient. Two step samples of a three-state target force error at least `15 W U^3 / [8(exp(3)+6 exp(1/2))]`, approximately `0.06254614958 W U^3`. This is exact for the two-sample minimax problem, not asserted optimal for the all-protocol norm.
2. **A lower bound for every state budget.** For `D>=2`, set `r=3D-4`. The broad minimax error obeys `E_D >= 7 W U^3 / [3200 r^3 (36e)^(2r-2)]`. The proof uses a finite difference filter and a positive sampled Hankel matrix of one target with `3D-2` states. It allows all analytic Markov surrogates in the original comparison class, including nonreversible models, Jordan blocks, and unrestricted generator derivatives. The sample horizon is `(6D-7) log(2)/k`.
3. **Matching order with a target rate cap.** Restricting only target active rates to `lambda<=3k` gives necessary and sufficient `Theta(log(W U^3/tolerance))` states at fixed positive W,U. No hidden spectral-gap lower bound is imposed. The broad surrogate class is unchanged. The unrestricted target problem still has logarithmic necessary versus squared-logarithmic sufficient state growth.

Proofs: `docs/FINITE_ACCURACY.md`, Sections 9–10. Evidence: `scripts/verify_response_lower_bounds.py` and its generated report. Definitions and quantifiers remain in Section 0; earlier proofs are retained. Verification procedures and precise computational scope are in `docs/VERIFICATION.md`.

The prior-art audit now compares sampled Hankel and stochastic realization bounds. The linear lift, rank obstruction, singular-value bound, positive quadrature, and inverse spectral construction are established ingredients. The new application-specific claims are the bridge to this constrained cubic-response norm, the explicit target witnesses, and the tolerance state laws. Their originality is not certified by deriving them here.

## Publication scope

The narrow candidate story is exact passive compression, exact nonlinear-response complexity, and tolerance-controlled Markov reuse under a specified actuator and readout. The capped-target theorem is complete at the level of state-growth order. It is not a theorem about finite-amplitude signals, learning from data, memory bits, arbitrary dynamical surrogates, or turbulence.

Manuscript writing remains on hold for a precise closest-theorem comparison and a clear operational explanation. Kotsalis–Shamma's HMM reduction paper and Frazho's bilinear realization paper remain full-text access gaps. The active-rate cap must be explained as additional information about target relaxation times if it is foregrounded. Do not treat the absence of an exact theorem in a bounded search as a novelty certificate.

Closing the unrestricted-rate gap is not automatically a prerequisite to a paper if the completed capped-target result supports a distinctive, meaningful scope. Conversely, matching asymptotic order alone does not establish that scope.

## Single next mathematical priority

**Determine whether unrestricted target rates genuinely require squared-logarithmic state growth, or whether a logarithmic-state construction exists in the allowed surrogate class.**

Start by assessing whether multiscale target spectra strengthen the response-sample lower bound beyond the present fixed-band witnesses. If using nonuniform sample times, preserve the finite-dimensional factorization for arbitrary analytic Markov surrogates; the convenient uniform-grid recurrence cannot simply be assumed. Any new lower bound must be in the actual response norm, with sample horizon and weight dependence explicit.

In parallel with the mathematical comparison, check the closest Hankel/HMM and exponential-approximation results for a direct reduction. A documented reduction to known work is a valid checkpoint. Do not restrict general surrogates to positive kernels, reversible dynamics, bounded derivatives, or a chosen topology merely to force a bound. The present lower theorem already avoids those restrictions.

Keep finite-field remainder control and noisy coefficient acquisition separate. Open one only when needed for a selected physical claim, and prove the required quantitative bound before adding that interpretation. Coefficient samples in these witnesses are not directly finite-field or noise-certified measurements.

## Evidence discipline and completion rule

Run `make check` in the pinned Python 3.13 environment. Fresh reports go into `.check-output/`. Regenerate saved reports when calculation sources change; never hand-edit metrics. Preserve the original license, baseline verifiers, unrelated owner work, and non-forced Git history. A local PASS and a GitHub Actions result are separate evidence.

Keep the public repository free of source fiction, conversational material, and unrelated projects. Do not claim independent validation from internal checks, experimental implementation, acceptance, or a journal tier.

The next checkpoint must deliver a proof, counterexample, or precise reduction to prior work, together with synchronized claims and appropriate checks. Another plan, bibliography, simulator, or manuscript draft alone is not completion.
