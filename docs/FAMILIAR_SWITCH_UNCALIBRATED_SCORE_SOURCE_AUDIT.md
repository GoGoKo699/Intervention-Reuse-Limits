# Unknown-detector testing: concentration, control variates and information cost

[Score test](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md) · [Information cost](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) · [Earlier score audit](FAMILIAR_SWITCH_SCORE_SOURCE_AUDIT.md) · [Physical-source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)

**Primary-source comparison, 24 September 2026.** The new work improves sufficient and necessary measurement budgets for the repository's specified two-protocol experiment. Fixed tangent scores, control variates, bounded-variable concentration and adaptive change of measure are established tools. The contribution assessed here is their explicit application to the unknown symmetric detector class, with certified nuisance and approximation allowances. This is not a new general statistical method or a complete physics-priority determination.

## Inspected sources

| Primary source | Inspected passage | Role and boundary |
|---|---|---|
| Andreas Maurer and Massimiliano Pontil, “Empirical Bernstein Bounds and Sample Variance Penalization,” COLT 2009, [author preprint](https://arxiv.org/pdf/0907.3740v1). | Theorem 3, printed page 2, and its distinction from empirical-variance bounds. | Bounded population-variance concentration is established. Our weighted independent-summand inequality is derived in the earlier score note; we do not estimate a standard error from the testing data or claim the empirical-variance theorem. |
| Art B. Owen, *Monte Carlo theory, methods and examples*, [Chapter 8, “Variance reduction”](https://artowen.su.domains/mc/Ch-var-basic.pdf), author-hosted version bearing 2009–2013, 2018 copyright. | Section 8.9, printed pages 28–31, especially fixed-coefficient control variates and equations (8.30)–(8.32). | Subtracting a known-mean correlated quantity preserves expectation and can reduce variance. Here the two initial-record means agree by the shared-preparation/instrument premise, so their difference has known mean zero even though neither mean is known. The coefficient is fixed before sampling. This is an application of control variates, not a new variance-reduction principle. |
| Emilie Kaufmann, Olivier Cappé and Aurélien Garivier, “On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models,” *JMLR* **17** (2016), [primary full text](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf). | Lemma 1, printed page 7, and Appendix A's likelihood-ratio argument. | Relative entropy accumulated under adaptive arm selection bounds the binary decision information. The repository's two arms are the two pulse orders. The new input is one explicit rational reversible comparator with a different detector, whose per-trial divergences are certified. Fresh independent trials and the stated stopping conditions are essential. |

## What changes in the experiment

No observation type is added. The initial and final bits were already recorded. Their within-trial dependence is retained in each complete score, while independent fresh trials supply the concentration argument. The initial-record correction exploits a shared law across arms; it cannot be transferred to arm-dependent preparation or detector drift without a new bound.

The unknown-detector lower bound compares the same noisy target with a reversible rival using a perfect detector. That rival is admitted when detector probabilities are unknown but excluded by the earlier narrow calibration interval. Comparing this lower bound with the earlier calibrated sufficient design therefore quantifies the value of a calibration promise for this task. It does not prove either test optimal, price the experiment needed to establish that promise, or transfer the count to richer protocols.

The physical candidate, preparation and disturbance requirements, time-reversal convention and unresolved full-text Falk comparison retain their previous scope. Better concentration does not validate those assumptions or establish PRL readiness. Manuscript drafting remains deferred.
