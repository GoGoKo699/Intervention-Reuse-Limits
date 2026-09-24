# Weaker-field design: sources and comparison boundaries

[Robustness proof](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) · [Score test](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) · [Earlier statistical audit](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md) · [Physical-source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)

**24 September 2026.** This checkpoint changes the high field and the two dwell times of the existing coupled-switch experiment. The two pulse orders, one preparation, two binary readouts per trial and independent symmetric detector classes remain the same. The covariance identity and the positive three-state construction are inherited repository results. The new work certifies a different operating point and its finite-sample design; it does not introduce a new general concentration or information inequality.

## Established statistical ingredients

The primary full texts below were reopened for this checkpoint. Their relevant passages were already compared with the preceding test in the linked audit.

| Source | Relevant passage | Use here |
|---|---|---|
| A. Maurer and M. Pontil, “Empirical Bernstein Bounds and Sample Variance Penalization,” COLT 2009, [author preprint](https://arxiv.org/pdf/0907.3740v1). | Theorem 3, printed page 2. | Bounded-variable concentration with population variance is established. The repository supplies fixed variance ceilings for each complete bit-pair score and uses the weighted-summand derivation in its earlier snapshot score proof. No empirical standard-error estimate is substituted for these ceilings. |
| E. Kaufmann, O. Cappé and A. Garivier, “On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models,” *JMLR* **17** (2016), [primary full text](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf). | Lemma 1, printed page 7, and Appendix A.1. | Adaptive change of measure underlies the already frozen necessary-count theorem at the previous operating point. Comparing that lower bound with a newly certified upper bound is a design comparison; no new sequential-information theorem is claimed. |

The fixed initial-bit corrections are control variates whose expectations cancel across the shared preparation and initial channel. The earlier audit gives the author-hosted Owen textbook passage for this standard variance-reduction idea. Neither initial/final independence within a trial nor known detector probabilities are assumed. Fresh-trial independence remains necessary for the sampling guarantee.

## What the comparison establishes

A sufficient count at the new field and clock can lie below a necessary count for every valid test restricted to the two old arms. The former is uniform over its stated physical target allowances; the latter already holds for one nominal old target with one-percent detector errors. Both use the same coupling, observation types and detector assumptions, but their applied field and dwell times differ.

This establishes a statistical benefit of this particular operating-design change. It does not transfer the old lower bound to the new experiment, establish optimality of either design, or prove that weaker fields always supply more information. In particular, a larger value of a nonlinear witness alone would not establish the comparison; the separate size, power and information bounds are essential.

The microscopic charge mapping, constant-rate-prefactor assumptions, preparation and joint-instrument requirements, and unresolved full-text Falk comparison retain the scope of the earlier physical audit. Shorter active duration does not price resetting or establish independent repetitions. The improved numerical certificate is not a device demonstration, complete novelty assessment or PRL-readiness decision. Manuscript drafting remains deferred.
