# Final sanity audit of the frozen scientific case

**30 September 2026. Verdict: no blocking defect found in the audited
central proof chain; the complete existing verification suite passes.**
The selected theoretical research is complete for the model and prediction
contract in the [scientific guide](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/SCIENTIFIC_CASE.md). The evidence
package is ready for a focused theory manuscript. Manuscript writing
remains on hold as the final phase.

The release-preparation baseline is commit
`4d978a7319fd5ce63f74084b58a9aff43006da52`, tree
`16e1279782ed67e86da6f9b9ffd7aa344e864e25`, with successful
[baseline CI run 36713753639](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/36713753639).
The release pass repeats the complete suite, checks the frozen proof
spine and removes obsolete venue-specific status wording and duplicate
navigation. It adds a collaboration invitation and a retrieval guide.
No theorem, model, optimizer or numerical research result is added.
Proof content, verifier calculations and saved replay models are preserved.

## 1. What was checked analytically

Separate internal review tasks re-derived the central lower bounds,
positive constructions, exact boundary and finite-pulse witness. The
trace-construction algebra was independently checked twice. These are
internal mathematical reviews, not external peer review, formal proof
verification or a guarantee that no error remains.

| Part of the case | Checks and outcome |
| --- | --- |
| [Preparation-free unknown-tilt lower](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md) | Singleton conditioning removes arbitrary rival word preparation. Positive and zero-weight stationary-support cases exhaust the null. Common finite tilt preserves support, and the zero-weight return block has dimension at most two. No missing support or preparation case found. |
| [R92: fixed positive clocks](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) | Unequal-rate determinant factorization, positivity, quadratic asymptotics, global Lipschitz constants and pair-TV denominators were re-derived. The general two-state composition lower and reversible three-state lower have the stated quantifiers. Corrected positive two-state rates and geometric contraction give the quadratic upper uniformly over arbitrarily long clocked words, including the required terminal dwell floor. No gap found. |
| [R93: all-duration words](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_RAPID_CONTROL.md) | Three-state rates, detailed balance, normalized Gibbs family, shared coordinates and uniform error bound check. Held-field matching forces the otherwise uncapped two-state rival rates; product and long-time limits are legitimate within the all-word supremum. Near-minimizers suffice, so existence of an optimal rival is not assumed. |
| [R94: exact general boundary](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md) | Singleton realization transfer, inference of positive stationary weights, both singleton orientations, all coordinate triangles, threshold and equality case were checked. The exact three-state construction and ordinary four-state lower support the current state-count corollaries. |
| [Fast relaxation](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_FAST_RELAXATION.md), [finite-rate window](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md) and [trace reduction](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_TRACE_REDUCTION.md) | Positive generators, invariant regions, pair-TV factors, common switching coordinates, rare-state coupling and same-time trace error all check. Bounds do not hide a horizon or switch-count factor. Parameter-extreme conclusions retain their stated field and feasibility restrictions. |
| [R98: three finite experiments](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md) | Exact two-state contrast multiplication, arbitrary-preparation TV conversion, positive periodic coefficient, $`19/r^2`$ remainder, explicit onset and inherited upper were re-derived. The three-setting menu proves a third-state requirement at intermediate accuracy; it supplies no three-state lower or fourth-state necessity. |
| [Current scientific guide](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/SCIENTIFIC_CASE.md) | Fixed ticks, arbitrary durations and the finite menu are distinct. Target preparation, rival freedom, Gibbs premises, strict-exponent state counts, growing pulse count and physical time are consistent with the proofs. One crossover wording ambiguity was clarified below. |

The fresh line-by-line analytic review focused on the frozen claim and
its dependencies. It did not re-prove every historical ledger row or
independently re-certify the old sampling/martingale budgets. Those older
tasks retain their existing proofs and reproducibility checks; their
sampling guarantees are not imported into R98.

## 2. Full reproducibility check

`make check` completed with exit code zero: all **77 mathematical
verifiers and four deterministic saved-model replays** passed. Optional
optimizers were not run. Fresh suite output remained in `.check-output/`.

The local run used Python **3.12.14** and the exact pinned package
versions: NumPy **2.3.5**, SciPy **1.17.0**, SymPy **1.14.0** and
mpmath **1.3.0**. All 81 fresh reports were structurally compared with
their saved counterparts. Scientific results, checks and source/proof/input
bindings agree; Python-version metadata can differ between the local
3.12 and hosted 3.13 environments.

Before that run, affected saved reports were regenerated by their owning
verifiers in dependency order. Their mathematical payloads were compared
with the release-preparation baseline. Only reviewed path changes,
provenance/version metadata and two neutralized editorial scope sentences
were permitted to differ. No mathematical value or saved model changed.
The original checkpoint verifier and license remain byte-identical.

The repository check also passed local links, math/code-fence balance,
all **82 Python syntax checks**, saved-report provenance and the original
MIT license. The [verification record](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/VERIFICATION.md) records the final
documentation check and preservation boundary. Hosted CI uses Python
3.13 and the same pinned dependencies; its result must be inspected for
the exact published commit, separately from the local run.

Passing these checks supports reproducibility. It does not turn sampled
calculations into universal lower bounds; the analytic proofs supply
those bounds. No new simulation was needed for this audit.

## 3. Minor findings and historical reading map

| Finding | Resolution |
| --- | --- |
| The current guide placed “$`p=1,2`$ depend on constants” immediately after its fixed-clock statement. | Clarified that both exponents are all-duration crossovers; only $`p=2`$ is a fixed-positive-clock crossover. At fixed ticks, $`p=1`$ already lies in the proved two-state regime. No theorem or count changes. |
| R92 originally left the unrestricted-rapid-control three-state order open. | Its outlook now points to R93, which resolves that order. |
| R93 says its own argument does not prove a finite-bandwidth lower and proposes a further finite-rate assessment. | R98 now proves the specified finite-pulse-spacing consequence under ideal jumps; it still does not prove a finite-ramp or bounded-Fourier-bandwidth theorem. The finite-rate and trace notes delimit the finer penalty; a large useful interior gap remains unproved and outside the frozen claim. |
| The finite-rate-window outlook leaves the long-time jointly strong-coupling/strong-field corner open. | The later uniform trace bound closes that parameter-extreme route in the stated nonnegative-field task. It does not establish a large interior gap. |
| Trace-reduction Section 3 defines an auxiliary $`k_0=e/L`$, while evaluating Section 2's indexed $`k_h`$ at $`h=0`$ gives $`e(1-\delta)/(L-\delta)`$. | The local auxiliary definition is explicit and is the quantity actually used in the proof; all inequalities check. This is a notation collision, not a false identity. Use a distinct name such as $`k_{\mathrm{ref}}`$ when incorporating the proof into a manuscript. |

The earlier outlooks now link to the later results that resolve them.
Presentation and status edits change some proof-note bytes; formula and
source-logic comparisons preserve mathematical content and assumptions.
The current guide takes precedence for active status and next-step language.

## 4. Bounded source and physical-assumption check

The closest-source comparison was refreshed at the following passages.
The conclusions in the right column are comparison judgments about the
inspected results, not exhaustive priority claims.

| Source inspected | Relevant distinction |
| --- | --- |
| [Grigoletto–Viola–Ticozzi, v1](https://arxiv.org/html/2510.25546v1), Proposition 2 and Theorem 1 with the following minimality discussion | Shared controlled reduction already exists with all-initial-state guarantees. Its stated minimality is relative to the algebraic procedure; the present task uses a narrower target preparation and lower bounds over all admissible small realizations. |
| [Meyer–Brandner, v2](https://arxiv.org/html/2510.26325v2), Eqs. (5)–(13) and the Floquet construction | Periodically driven weak-memory reduction already exists. Reducing one complete-period map does not impose the pair of field generators shared by the separate calibration holds and the pulse train used here. |
| [Fornace–Lindsey, v3](https://arxiv.org/html/2506.22918v3), Eq. (52), induced-chain properties and error theorem | Reversible positive compression and quantitative error control are established. The inspected theorem does not supply the present shared-field, deterministic-readout all-rival lower bounds. |
| [Franco–Kepka–Velázquez, published 2026](https://link.springer.com/article/10.1007/s00205-026-02183-7), Definition 3.1, Propositions 3.8–3.9, Corollary 3.11 and Example 3.12 | Response reciprocity and a three/four-state distinction already occur for one generator. The present candidate contribution is the combined controlled realization and precision hierarchy, not those ingredients in isolation. |

No inspected passage directly subsumes or contradicts the combined
frozen result. The previously disclosed full-text access gap for
[Falk (1983)](https://doi.org/10.1016/0378-4371(83)90110-3) remains:
the indexed abstract acknowledges equilibrium-preserving stochastic-spin
reduction, but equation-level nonoverlap has not been established. This
is a real limit on a strong priority assertion, not a dependency of the
mathematical proof.

The [community-model mapping](https://github.com/GoGoKo699/Intervention-Reuse-Limits/blob/5b8dbc60d4cff8167f56cec84151e7e28f755535/docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md) was
checked against the cited spinless single-level Fermi-rate models and
the wide-band driven-level model. The energy change, heat-bath rates,
common-temperature equilibrium specialization and compensated gate map
are consistent under the explicit fixed-barrier assumptions. Generic
Coulomb blockade alone does not imply those assumptions. Ideal jumps,
true endpoint records and the growth of physical duration at fixed
hidden rate remain essential scope qualifications. No finite-ramp,
detector, hardware-memory or heat-saving result follows automatically.

## 5. Completion decision

The matched control/accuracy laws, exact general realization and
finite-setting third-state witness form a completed, coherent theoretical
case. No unresolved mathematical prerequisite was identified for drafting
that case. The remaining task is to present the mechanism, central
theorem, assumptions, closest precedents and limitations clearly.

The frozen project does not promise optimal crossover constants,
practical resource savings, a large interior error gap, exhaustive
priority or external endorsement. These are limits of the contribution,
not replacement research gates. Reopen the mathematics only for a
concrete correctness issue. Broad significance and publication acceptance
remain editorial judgments; this audit certifies neither.
