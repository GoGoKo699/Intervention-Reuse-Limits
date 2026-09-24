# Internal review: a simpler score and the price of detector uncertainty

[Score proof](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md) · [Information lower bound](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) · [Source comparison](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md) · [Exact verifier](../scripts/verify_switch_uncalibrated_score.py) · [Report](../reports/switch_uncalibrated_score.json) · [Verification](VERIFICATION.md)

**24 September 2026.** The score author, separate statistical and adversarial reviewers, and the coordinator checked the new analytic arguments. The coordinator and statistical reviewer also inspected the complete relevant verifier source; the information comparator was independently reproduced with the frozen rational helper. These are separate internal checks within the same investigation, not external peer review or novelty certification.

## Scope and the simple statistic

The experiment keeps the same two chronological words, low-field preparation and initial/final records. The new statistic assigns one of four integer weights to each recorded pair, averages within each arm and combines the two averages. Its coefficients are fixed before data collection. The initial-bit correction has zero mean because the initial law is shared across arms. It reduces variance using data already collected; no independent-bit assumption within a trajectory is introduced.

The gates use four final-mean/correlation estimates. The corrected score also uses the two initial-bit means from those same records. Review corrected a sentence that had described the entire test as using only four empirical moments. This distinction changes no measurement resource.

The target detector probabilities remain arbitrary in $[0,0.01]$ and rival probabilities in $[0,1/2]$, under fixed independent symmetric channels. No detector inversion or fitted calibration value occurs. The stationary force-law, preparation, disturbance and independent fresh-trial assumptions are unchanged.

## All-rival and statistical checks

The reviewers checked the full detector square, including zero contrasts. On the local recorded-coordinate box the biased minus polynomial is affine in the initial contrast; both endpoint curves decrease with the final contrast, and their endpoint comparison places the global minimum at the perfect-detector corner. The resulting local necessary bound is $R<10^{-4}$. The plus branch is excluded whenever $R\ge10^{-4}$, so the equality case is covered.

The fixed tangent has a one-sided quadratic remainder on the enlarged population gates. Its null bound includes all preparation/instrument errors and the optional observed-law allowance. For arbitrary approximate observed laws, initial marginals can differ. The proof therefore transfers the entire corrected score by its range width rather than assuming its control-variate cancellation persists in those laws.

The variance identities were independently expanded over all four binary outcomes. Monotonicity in the recorded coordinates and initial means identifies valid worst corners. Target variances use the worst detector contrasts and a separate squared-width TV displacement bound. The variance ceilings are deterministic, not empirical standard errors.

For false rejection, a fixed null outside the population gates must cross one empirical gate; a null inside the gates must cross the score threshold. These alternative cases are maximized, not added. For power, gate failures and the score lower tail are union-bounded. The different arm allocations and the cross-arm $C-D$ gate retain their correct concentration denominators.

The resulting sufficient totals are 32 million paired trials for the exact admissible class and 90 million with observed-joint-TV allowance $10^{-4}$. Both error probabilities are below five percent. The latter allowance exceeds the constructive general-three error $2\times10^{-5}$. It is charged to the null only; the target class is unchanged.

## Necessary cost and the calibration comparison

The fixed rational ordinary comparator is irreducible, obeys detailed balance at both fields and has maximum exit rate below one. It uses a perfect detector while the target uses one-percent errors. The unknown-detector class permits those distinct hypotheses. Exact exponential enclosures give per-arm target-to-comparator KL less than $1/900000$.

The adaptive likelihood argument yields $\mathbb E_*N>810000\log19$; fixed counts require at least 2,384,996 trials. This applies to fresh selections of the same two arms, including adaptive choice and the stated stopping rules. It is not a lower bound for richer control or observation tasks.

The same noisy target belongs to the earlier calibrated class with its 1.2-million-trial sufficient test. Its narrow detector promise excludes the new perfect-detector rival. Hence the comparison establishes a greater-than-1.98 factor in the value of that promise for this task. It does not prove either count optimal or include the cost of obtaining calibration.

## Numerical corrections and evidence

Review corrected a LaTeX form-feed, made the $R=10^{-4}$ endpoint explicit, and fixed the four-versus-six empirical-summary wording. A decimal rounding issue was also corrected: the coarse nominal floor $0.001699$ alone is slightly insufficient to imply the displayed physical floor after charging $4.4b_T$. The exact nominal interval exceeds $0.0016994$, which suffices. The verifier explicitly checks this stronger floor, the printed safe difference-gate margin and the integer lookup values.

The final verifier has 131 exact checks at maximum dense dimension four. It pins two input reports, the rational helper, both new mathematical notes and all inherited proof snapshots. Final hashes, independent replay and the complete repository gate are recorded in [Verification](VERIFICATION.md). No earlier proof, verifier or saved numerical report is revised.

The remaining gap between sufficient and necessary counts is substantial. The separate next-operating-point exploration is a numerical research lead, with no transferred robust gap or trial allocation. Preparation and initial-instrument support remain physical questions. Manuscript drafting is deferred.
