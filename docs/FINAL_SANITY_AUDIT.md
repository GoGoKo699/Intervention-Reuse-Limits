# Proof and verification checks

[Scientific guide](SCIENTIFIC_CASE.md) · [Results index](CLAIM_LEDGER.md) · [Reproduction instructions](VERIFICATION.md)

The analytic review found no blocking defect in the central proof chain.
The checks below identify the arguments inspected, the computational
evidence and the source-comparison limits.

## 1. What was checked analytically

Separate internal review tasks re-derived the central lower bounds,
positive constructions, exact boundary and finite-pulse witness. The
trace-construction algebra was independently checked twice. These are
internal mathematical reviews, not external peer review, formal proof
verification or a guarantee that no error remains.

| Part of the case | Checks and outcome |
| --- | --- |
| [Preparation-free unknown-tilt lower](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md) | Singleton conditioning removes arbitrary rival word preparation. Positive and zero-weight stationary-support cases exhaust the null. Common finite tilt preserves support, and the zero-weight return block has dimension at most two. No missing support or preparation case found. |
| [R92: fixed positive clocks](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) | Unequal-rate determinant factorization, positivity, quadratic asymptotics, global Lipschitz constants and pair-TV denominators were re-derived. The general two-state composition lower and reversible three-state lower have the stated quantifiers. Corrected positive two-state rates and geometric contraction give the quadratic upper uniformly over arbitrarily long clocked words, including the required terminal dwell floor. No gap found. |
| [R93: all-duration words](FAMILIAR_SWITCH_RAPID_CONTROL.md) | Three-state rates, detailed balance, normalized Gibbs family, shared coordinates and uniform error bound check. Held-field matching forces the otherwise uncapped two-state rival rates; product and long-time limits are legitimate within the all-word supremum. Near-minimizers suffice, so existence of an optimal rival is not assumed. |
| [R94: exact general boundary](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md) | Singleton realization transfer, inference of positive stationary weights, both singleton orientations, all coordinate triangles, threshold and equality case were checked. The exact three-state construction and ordinary four-state lower support the current state-count corollaries. |
| [Fast relaxation](FAMILIAR_SWITCH_FAST_RELAXATION.md), [finite-rate window](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md) and [trace reduction](FAMILIAR_SWITCH_TRACE_REDUCTION.md) | Positive generators, invariant regions, pair-TV factors, common switching coordinates, rare-state coupling and same-time trace error all check. Bounds do not hide a horizon or switch-count factor. Parameter-extreme conclusions retain their stated field and feasibility restrictions. |
| [R98: three finite experiments](FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md) | Exact two-state contrast multiplication, arbitrary-preparation TV conversion, positive periodic coefficient, $`19/r^2`$ remainder, explicit onset and inherited upper were re-derived. The three-setting menu proves a third-state requirement at intermediate accuracy; it supplies no three-state lower or fourth-state necessity. |
| [Scientific guide](SCIENTIFIC_CASE.md) | Fixed ticks, arbitrary durations and the finite menu are distinct. Target preparation, rival freedom, Gibbs premises, strict-exponent state counts, growing pulse count and physical time are consistent with the proofs. Both exponents are all-duration crossovers; only the quadratic exponent is a fixed-clock crossover. |

The line-by-line analytic review focused on the state-count hierarchy and
its dependencies. It did not re-prove every supporting result or
independently re-certify the old sampling/martingale budgets. Those older
tasks retain their existing proofs and reproducibility checks; their
sampling guarantees are not imported into R98.

## 2. Reproducibility and interpretation

The complete suite comprises the repository integrity check, 77
mathematical verifiers and four deterministic saved-model replays.
The recorded full run passed with the pinned versions in
[requirements.txt](../requirements.txt); all 81 reproduced reports agreed
with their saved scientific payloads and source/proof/input bindings.
Python-version metadata may differ between local and hosted environments.

The repository check covers local links, fence balance, all 82 Python
syntax checks, saved-report provenance and the original MIT license.
[GitHub Actions](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions)
provides verification for each published commit. The
[verification guide](VERIFICATION.md) gives the reproduction commands.

Passing a finite calculation supports its stated certificate or
consistency check; the analytic arguments supply the universal bounds.
Sampling guarantees remain attached to their original observation tasks.

The trace-reduction proof uses a locally defined auxiliary rate whose
symbol also appears in a field-indexed family. The local definition is
explicit and the reviewed inequalities use that definition.

## 3. Bounded source and physical-assumption check

The source comparison covers the following passages.
The conclusions in the right column are comparison judgments about the
inspected results, not exhaustive priority claims.

| Source inspected | Relevant distinction |
| --- | --- |
| [Grigoletto–Viola–Ticozzi, v1](https://arxiv.org/html/2510.25546v1), Proposition 2 and Theorem 1 with the following minimality discussion | Shared controlled reduction already exists with all-initial-state guarantees. Its stated minimality is relative to the algebraic procedure; the present task uses a narrower target preparation and lower bounds over all admissible small realizations. |
| [Meyer–Brandner, v2](https://arxiv.org/html/2510.26325v2), Eqs. (5)–(13) and the Floquet construction | Periodically driven weak-memory reduction already exists. Reducing one complete-period map does not impose the pair of field generators shared by the separate calibration holds and the pulse train used here. |
| [Fornace–Lindsey, v3](https://arxiv.org/html/2506.22918v3), Eq. (52), induced-chain properties and error theorem | Reversible positive compression and quantitative error control are established. The inspected theorem does not supply the present shared-field, deterministic-readout all-rival lower bounds. |
| [Franco–Kepka–Velázquez, published 2026](https://link.springer.com/article/10.1007/s00205-026-02183-7), Definition 3.1, Propositions 3.8–3.9, Corollary 3.11 and Example 3.12 | Response reciprocity and a three/four-state distinction already occur for one generator. The present candidate contribution is the combined controlled realization and precision hierarchy, not those ingredients in isolation. |

No inspected passage directly subsumes or contradicts the combined
result. The previously disclosed full-text access gap for
[Falk (1983)](https://doi.org/10.1016/0378-4371(83)90110-3) remains:
the indexed abstract acknowledges equilibrium-preserving stochastic-spin
reduction, but equation-level nonoverlap has not been established. This
is a real limit on a strong priority assertion, not a dependency of the
mathematical proof.

The [community-model mapping](FAMILIAR_SWITCH_COMMUNITY_MODEL.md) was
checked against the cited spinless single-level Fermi-rate models and
the wide-band driven-level model. The energy change, heat-bath rates,
common-temperature equilibrium specialization and compensated gate map
are consistent under the explicit fixed-barrier assumptions. Generic
Coulomb blockade alone does not imply those assumptions. Ideal jumps,
true endpoint records and the growth of physical duration at fixed
hidden rate remain essential scope qualifications. No finite-ramp,
detector, hardware-memory or heat-saving result follows automatically.
