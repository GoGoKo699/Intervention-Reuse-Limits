# Internal review of serial sampling and finite reset

[Serial theorem](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) · [Reset theorem](FAMILIAR_SWITCH_FINITE_RESET.md) · [Verifier](../scripts/verify_switch_serial_reset.py) · [Report](../reports/switch_serial_reset.json) · [Source audit](FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** Separate proof authors, a reviewer and the coordinator examined this continuation. These are internal checks within the investigation, not external peer review, novelty certification or an achieved device specification.

## Conditional laws and the ordinary null

Review required one fixed stationary reference pair for the entire run. Actual conditional laws may depend on the past within the stated TV allowance, but a different stationary model cannot be selected after each record. The serial null's approximation promise is conditional on history. The earlier single-trial marginal approximation promise alone does not imply it.

The filtration is taken immediately before the current reset. It may include the hidden state entering that reset and every earlier record; it does not condition on the hidden state emerging from the current reset. This distinction is necessary because knowing the emerging state would destroy the claimed conditional preparation bound. Fixed conditional symmetric detector channels, independent of the past and hidden dynamics, are a sufficient implementation; unconditional electronic error frequencies are insufficient.

The reset fills the already allocated preparation allowance. It is not added again to the observation error. The actual-to-nominal field comparison and the current initial instrument still have their separate existing terms. Arbitrary disturbance by the preceding final measurement is allowed because the next reset starts from an arbitrary conditional hidden law.

## Gates, variance and concentration

The null case split is made on its fixed stationary reference, using the auxiliary intervals expanded by the TV moment allowance. It is not made on a random average of conditional means. Outside an expanded reference interval, every predictable drift is outside the unexpanded auxiliary interval on the same side, so passing the empirical gate forces a martingale deviation.

Inside the reference intervals, each conditional scalar law requires a second TV enlargement. Review checked the resulting $4E_R$ expansion of the original variance boxes. Exact conditional maxima are $.302543940636$ and $.26189790305904$, still below the original $.31$ and $.27$ ceilings. Whole-score transfer includes the initial-bit corrections; their cancellation is invoked only at the common stationary reference.

The score proof derives its conditional exponential bound and explicit Chernoff parameter. This justifies the square-root-plus-linear radius directly, without incorrectly inverting the weaker quadratic-denominator tail inequality. Gate concentration sums conditional range squares across the deterministic arm schedule; it does not require independent arm averages. The selected violated null gate is fixed by the reference, so no union over null gates is needed. Target gate failures and the score miss event are union-bounded.

The score coefficients, gates, threshold $.0021$ and five-million allocation remain unchanged. The null boundary stays below $.002078$, the target boundary above $.002154$, and target gate failure below $.004$. False rejection is below 5% and power exceeds 95% under the uniform conditional promises. No per-trial coupling failures are union-bounded over five million trials, and no independence claim follows from waiting a finite time.

## Target reset and resource accounting

The generic four-state heat-bath generator closes on $1,S,Z,SZ$ and has gap at least $1/5$. The actual low-field Gibbs law remains invariant when each edge's two directions receive the same factor. Dirichlet comparison therefore gives gap at least $99/500$ throughout the independent one-percent box. The minimum stationary mass exceeds $1/21$ for the allowed low fields. A positive degree-28 exponential series certifies that 63 actual attempt units give hidden-law TV error below $10^{-5}$ from every starting law.

This is a target-specific mixing proof. A reversible rival can be slowed arbitrarily without changing its equilibrium law, so no common finite wait prepares the entire unrestricted rival class. Serial rejection requires each rival to meet the stated conditional preparation promise. The earlier broad population obstruction remains unchanged. No target gap or minimum stationary mass is silently imposed on all rivals.

The constructive three-state predictor also admits the same reset duration. A weighted norm on its frozen two-dimensional low-kernel block bounds contraction over 50 ticks of length $5/4$; the remaining half-unit contracts TV. This requires no reversible predictor assumption. Its stationary law is the nominal law, with the previously stated actual-tilt uncertainty. Finite preparation of this predictor adds at most $10^{-5}$ to the target-to-predictor conditional table comparison, leaving it below $.00009$. That is a per-history, one-trial comparison, not a full-sequence TV bound or a new state-count theorem for complete records.

Five million resets cost 315 million attempt units and active evolution costs 12.5 million, totaling 327.5 million nominal units, or 26.2 times active-only exposure. Active timing error contributes at most another 100 units. A separately specified reset-clock tolerance has its own stated cost. Ten million binary readouts, switching and other control overhead remain additional; no device attempt frequency is inferred.

## Evidence and remaining boundary

The exact verifier checks the symbolic generator identities, finite reset inequalities, widened conditional variance boxes, martingale arithmetic and sampling constants, with largest dense dimension four. The linked proofs supply the universal probability and mixing arguments. Final proof bindings, independent replay and the full regression gate are recorded in [Verification](VERIFICATION.md).

The operational question now concerns support for the rival preparation promise, the joint instrument and the detector model in a concrete implementation. Passing the current gates does not establish those premises. The optional preparation protocols retain their separate unresolved finite-sample cost. Manuscript drafting remains deferred.
