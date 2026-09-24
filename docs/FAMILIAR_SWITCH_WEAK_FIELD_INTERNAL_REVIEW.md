# Internal review of the weaker-field experiment

[Robustness proof](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) · [Score proof](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) · [Exact verifier](../scripts/verify_switch_weak_field.py) · [Report](../reports/switch_weak_field.json) · [Source audit](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** Separate proof authors, an adversarial reviewer and the coordinator checked the new analytic arguments. The coordinator and reviewer also inspected the verifier source. These are internal checks within the same investigation, not external peer review or a complete novelty assessment.

## Physical and all-rival reasoning

The experiment changes only the high field to $H=\log2$ and both dwell times to $5/4$, keeping $J=\log3$, equal unit attempt rates, the same preparation, two word orders and initial/final bits. Each target electronic error remains at most one percent; ordinary rivals may choose independent symmetric errors anywhere up to one half, fixed across protocols. Different hypotheses may use different detectors.

The review checked the inherited singleton covariance identity, the entire closed detector-contrast square, and the new local biased/approximate-force bound $R<0.00007$. The derivative and endpoint inequalities minimize the minus branch without dividing by a detector contrast. The plus branch is excluded at and above that threshold, including its equality endpoint. The exact target neighborhoods retain every sign and localization condition.

The shortened-duration perturbation formula is $b_T=\epsilon_p+(7/4+\epsilon_t)\epsilon_h+4\epsilon_t+\xi$. The initial record is retained when charging disturbance; its correlation with the postmeasurement hidden state cannot be discarded. Preparation and instrument errors are charged to both hypotheses, and each model's own electronics contract its displacement.

The positive three-state construction covers small negative low-field errors. Review aligned the new verifier's displayed coordinate triangle with the charge construction used in the robustness proof; both the earlier nominal triangle and the selected charge triangle are valid at the ideal point, but the latter makes the actual-field provenance explicit. The three-state upper concerns the two joint snapshot laws. It does not assert equality of arbitrary multitime observations.

The optional fivefold-tolerance row follows from the same stationary separation and perturbation formula. It retains a state-count interval $[10^{-4},6\times10^{-4}]$ with all preparation, field, timing and disturbance allowances $5\times10^{-5}$. The two-million and 2.5-million sampling designs retain the smaller $10^{-5}$ allowances; no sampling count is transferred to the relaxed row.

## Statistical reasoning

The integer lookup scores were checked directly on all four bit pairs. Their initial-bit corrections have cancelling expectations under the common initial law and reduce variance using already recorded data. Both arms have equal trial counts, and the statistic adds their separate means. Dependence within each recorded pair is retained.

The tangent remainder is positive throughout the enlarged stationary population gates. Thus the stationary null score is bounded by the local witness ceiling without a quadratic remainder cost. Arbitrary approximate observed laws can have different initial marginals; the proof transfers the entire corrected score by total variation rather than assuming cancellation for those laws.

The exact four-cell variance polynomials decrease in the recorded mean and correlation and increase in the initial mean on the required boxes. Target contrast monotonicity and the squared-width perturbation bound give separate target ceilings. These are fixed population bounds, not standard errors fitted from the observations.

For nulls outside a population gate, the chance of passing one violated empirical gate bounds rejection. For nulls inside all gates, the score tail bounds rejection. These are alternative cases for each fixed law. For target power, gate failures and the score lower tail are union-bounded. The independent review also checked the cross-arm difference denominator and all center-enclosure charges.

The two-million design has relatively small positive threshold slacks. Its validity rests on rational squared inequalities and rational exponential bounds, not decimal rounding or a normal approximation. The separate 2.5-million design enlarges the ordinary null by observed joint-table TV $10^{-4}$ per protocol. Review replaced wording that could have mistaken this sufficient count for a necessary one.

## The comparison with the earlier operating point

The new sufficient two-million count is below the frozen old necessary expectation $810000\log19$. The old lower already applies to the target with exactly one-percent detector errors, while the new uniform target class includes that error level. Both use the same coupling, observation types and form of physical promises, with their respective applied fields and dwell times.

This comparison is stronger than comparing two sufficient tests. It certifies an observation-budget advantage of this particular operating-design change, including against adaptive sampling and stopping at the old design. The fixed-field null sets differ, the old lower does not become a lower at the new point, and neither global optimality nor a general ordering of experiments follows. Resetting, calibration acquisition and laboratory overhead remain unpriced.

The exact certificate, final source/proof hashes, independent replay and complete repository gate are recorded in [Verification](VERIFICATION.md). Earlier proofs, verifiers and saved numerical reports remain intact. Preparation, an adequate initial joint instrument and kinetic-model support remain substantive physical requirements; manuscript drafting is deferred.
