# Snapshot observation and fixed scores: source comparison

[Snapshot theorem](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) · [Snapshot test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) · [Endpoint test](FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md) · [Earlier physical and reciprocity comparison](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) · [Earlier statistical comparison](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md)

**Focused primary-source audit, 24 September 2026.** This continuation changes the measured data and improves sufficient tests. It does not claim a new concentration inequality, a new general testing principle, or a new method of inverting a binary noise channel. The physical reciprocity, Markov response and preparation-based dimension-witness comparisons in the earlier audit remain applicable.

## 1. Variance-sensitive concentration is established

**Andreas Maurer and Massimiliano Pontil**, “Empirical Bernstein Bounds and Sample Variance Penalization,” COLT 2009, [arXiv:0907.3740](https://arxiv.org/abs/0907.3740), [primary full text](https://arxiv.org/pdf/0907.3740). **Inspected:** Theorems 1 and 3, printed pp. 1–2, and the distinction from empirical variance bounds in Theorem 4.

Theorem 3 supplies a bounded iid variance-sensitive confidence inequality; the paper credits the classical Bennett/Hoeffding lineage. Our tests use fixed population-variance bounds over a response box. They do not estimate variance from the test data or invoke the paper's empirical-variance theorem. The endpoint proof gives the weighted independent-variable exponential-moment derivation used by both designs. For paired observations, each entire initial/final score is one summand; its correlated component moments are not treated as independent samples.

## 2. Rejecting every component of a union null is established

**Roger L. Berger**, “Multiparameter Hypothesis Testing and Acceptance Sampling,” *Technometrics* **24**, 295–300 (1982), [DOI:10.2307/1267823](https://doi.org/10.2307/1267823). **Inspected:** the author's [university research record and abstract](https://asu.elsevierpure.com/en/publications/multiparameter-hypothesis-testing-and-acceptance-sampling/); full text was not inspected in this continuation.

The abstract explicitly describes testing every component and requiring all to pass, with a null formed as a union. Our false-rejection argument is elementary: an ordinary small model satisfies at least one singleton-sign inequality, so rejecting both requires rejecting a true component. No split of the type-I budget between the two signs is needed. This citation establishes an antecedent, not a full theorem-level comparison or a novelty clearance. The separate localization argument partitions fixed population parameters into inside/outside cases; it does not add the two casewise bounds as if they were random events.

## 3. What the new finite certificates contribute

The repository combines its conditional-covariance identity with fixed tangent scores, a bounded quadratic remainder, and localized variance bounds. Exact rational arithmetic certifies the stated allocations, thresholds and nuisance boxes. These are target-specific sufficient designs, not optimal minimax tests or generic learning algorithms.

The direct snapshot theorem bounds the two joint laws in their own TV metric. Its detector calculation explicitly inverts the two independent binary symmetric channels, with lower contraction factor equal to the product of their contrasts. This is elementary finite-channel algebra. Calibration uncertainty and initial hidden-state disturbance are charged separately. The 1% flip probability is a chosen mathematical fixture, without a claimed experimental source.

The necessary sample bound uses the established adaptive change-of-measure principle already compared with Kaufmann, Cappé and Garivier in the earlier statistical audit. The new contribution to that calculation is a certified close ordinary comparator for the paired-data task and an exact per-trial relative-entropy upper bound. It does not prove the sufficient allocations optimal.

## 4. Priority and physical limits remain open

The earlier audits of Onsager reciprocity, finite-field response operators, and classical dimension witnesses remain required reading for the proposed physics contribution. Replacing high-field preparation by an initial observation is an explicit resource change. General three-state matching concerns the two initial/final joint laws; arbitrary multitime trajectory equality is not established.

The closest-source comparison is still bounded, and the previously identified Falk full-text lead remains unresolved. The new statistical work neither resolves that access gap nor establishes PRL readiness. Credible hidden-state preparation and measurement-disturbance calibration in a concrete realization remain scientific work, rather than consequences of this literature check.
