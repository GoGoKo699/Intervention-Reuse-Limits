# Current work order: an operational distinction beyond standard realization

## Completed takeover checkpoint — 22 September 2026

The inspected starting point was clean `main` at `80dc6098613b6561428d017b4a41553607fde67b`. The original `make check` was reproduced using Python 3.13.5 and the pinned dependencies. The original MIT license and both original mathematical verifiers remain unchanged.

The audit found no substantive error in the existing passive-law, cubic-kernel, nonvanishing-signal, or midpoint-compression derivations. The new mathematical checkpoint is:

1. **A precise known-kernel approximation task.** `docs/FINITE_ACCURACY.md`, Section 0, fixes preparation, binary readout, coefficient norm, protocol/horizon quantifiers, model and surrogate classes, and information supplied to the constructor. General analytic Markov surrogates remain the broad comparison class.
2. **Stronger compression.** Tapered positive Gaussian quadrature on dyadic damped-rate intervals gives error at most `8 U^3 W 16^(-n)` using at most `2n(n+1)+1` kernel modes. The same surrogate works for every bounded protocol and every finite horizon; there is no original spectral-gap or maximum-rate assumption. Proof: `docs/FINITE_ACCURACY.md`, Section 8. Evidence: `scripts/verify_quadrature.py` and `reports/quadrature.json`.
3. **Sharp generic exact realization.** A positive kernel with `r` distinct modes is realized by a reversible birth–death internal generator with `r+1` hidden states and sensitivity magnitude `sqrt(W)`. Including the visible state A gives `r+2` states, attaining the exact lower bound when no hidden decay rate equals k. Thus the quadrature construction needs at most `2n(n+1)+3` total states. Proof: `docs/THEORY.md`, Section 9. Evidence: `scripts/verify_minimal_realization.py` and `reports/minimal_realization.json`.
4. **Novelty reduced, not certified.** Positive quadrature and Jacobi inverse spectral theory supply the mathematical machinery. The root-exponential order is a short consequence of established approximation results. Both 2026 leads and the coarse second-order paper were inspected at full-text level; Chowdhury already supplies exact ordinary visible-law agreement with altered entropy-selected dynamics. See the source-by-source audit and access depths in `docs/PRIOR_ART.md`.

These are proofs accompanied by internal computational checks, not external proof review. Saved local reports and GitHub Actions are separate evidence. See `docs/VERIFICATION.md` for reproduction and scope.

## Scientific assessment and publication scope

A defensible research note presently concerns finite reversible stochastic models, exact passive binary path compression, cubic mean-response sufficiency, and tolerance-dependent known-kernel Markov realization. It does not establish a new general principle of hidden response, a new exponential approximation method, an optimal tolerance rate, noisy identification, or finite-amplitude observability.

Manuscript writing remains on hold. The combined construction is useful and more tightly characterized, but the audit has not established a distinctive publishable contribution beyond the application of standard tools. Do not turn a successful check or sharper constant into a publication claim.

## Single next priority

**Find a nontrivial lower bound or separating witness in the actual cubic response norm for the broad analytic Markov surrogate class, or document why the strongest plausible statement follows from known realization theory.**

Start with a finite set of step-response samples separating an admissible target from every two-state surrogate that preserves the required passive/static/linear/quadratic behavior. Establish the exact two-state response class before optimizing the witness. Then assess whether the argument scales with tolerance; a two-state witness alone is not the final paper target.

Do not substitute a kernel-approximation lower bound for a response-norm lower bound. Do not impose reversibility, positive residues, topology, rate bounds, or generator-derivative bounds on general surrogates without separating and motivating the new problem. Arbitrarily weak poles do not imply experimentally resolvable degrees of freedom. The constructive `O(log^2(1/tolerance))` upper bound rules out microscopic-size-dependent fixed-accuracy lower bounds at bounded W and U.

Keep the finite-field and noisy-kernel-acquisition tasks separate. Open one only when needed for the selected operational statement, and prove the relevant remainder or statistical bound before claiming it. Frazho's full paper remains an access-limited comparison; the bibliography is not exhaustive.

## Evidence discipline and completion rule

Run `make check` in the pinned environment. Fresh output goes into `.check-output/`. If a verifier changes, regenerate its saved report using the documented command; never hand-edit metrics. Preserve the baseline verifier, license, unrelated owner work, and non-forced Git history.

Keep the public repository free of source fiction, conversational material, and unrelated projects. Do not relabel this model as turbulence, claim independent validation from internal checks, or make acceptance or journal-tier promises.

The next checkpoint must deliver a proof, counterexample, or precise reduction to prior work, plus synchronized claims and appropriate checks. Another plan, bibliography, simulator, or manuscript draft alone does not complete the task.
