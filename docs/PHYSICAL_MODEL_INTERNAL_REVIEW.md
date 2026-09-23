# Internal review: physical model, robustness and reversal closure

[Single-force model](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) · [Robustness theorem](PHYSICAL_INTERFACE_ROBUSTNESS.md) · [Reversal closure](PHYSICAL_REVERSAL_REALIZATION.md) · [Physical source audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**Internal mathematical review, 23 September 2026.** The following analytic notes were checked by separate agents and the coordinating review. This is internal review, not external peer review, microscopic validation or priority certification. The finite state-advantage theorem has its own [review record](FINITE_ADVANTAGE_INTERNAL_REVIEW.md).

| Note | Independent audit | Result and retained boundary |
|---|---|---|
| Single-force conformational model | Mixed-lemma reviewer checked all energy/barrier signs, partition function, conductance construction and common attempt-frequency bound; coordinating reviewer checked the rate derivation and physical interpretation. | PASS. One force gives the exact stipulated Bell rates. Coinciding extensions, calibrated passive returns and force-independent hidden exchange remain assumptions. No molecular landscape or physical odd-parity memory device is supplied. |
| Physical interface robustness | Mixed-lemma reviewer independently checked the one-sided Duhamel orientation, both-reset coupling, weighted occupation bound, rate/log-rate constants, nearby-class quantifiers and finite-ramp convolution. Coordinating reviewer checked the complete note. | PASS. Only the reference needs a reset for the basic bound; weighted refinements require their extra hypotheses. The diagonal is included in the generator-row defect. Fixed defects create an accuracy floor. |
| Physical reversal and Markov closure | Coordinating reviewer checked the path-reversal argument, stationary Markov versus strong-lumping distinction, entrance tilt/killing proof, count and exit preservation, and exact small fixtures. | PASS. Even equilibrium observations that are Markov obey ordinary detailed balance. Stationary flux aggregation alone need not reproduce dynamics. Genuine odd physical variables and non-Markov memory are outside the closure conclusion. |

The frozen snapshots used by the bounded verifier are:

- `SINGLE_FORCE_CONFORMATIONAL_MODEL.md`: `8703852221c67f1b763c38ab8aa90549b70bba65ec20c1f177df7cc320c59c8d`.
- `PHYSICAL_INTERFACE_ROBUSTNESS.md`: `8b003b51e7a98e3752dced5be7d1aad62ca7a08f438bd495003e7bb2cf6f8117`.
- `PHYSICAL_REVERSAL_REALIZATION.md`: `b346f8e550e4f0bac468e38cd89b25e17dc98cf7485084988b87435f339ba727`.

The [bounded verifier](../scripts/verify_physical_robustness.py) and [report](../reports/physical_robustness.json) check small exact identities and separately labeled deterministic numerical diagnostics. They bind these proof snapshots. The analytic uniform-in-time conclusions do not follow from sampling the fixtures. The final pinned-environment gate and published CI are recorded in [Verification](VERIFICATION.md).

The consolidated source received a complete independent static review and pinned rerun: 104 checks passed, maximum dense dimension six, and the regenerated report matched the saved bytes. The coordinating reviewer also inspected the finite fixtures, row-defect convention and Duhamel orientation. No unresolved code or proof correction remained at freeze.

The [source audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) records nine inspected primary papers and exact access limits. It supports individual ingredients, not the entire engineered architecture as a community convention. The simple control-collapse results are elementary special cases: common returns preserve visible lumpability, and a common stationary preparation stays stationary under barrier-only driving. They are not presented as new general no-pumping theorems.
