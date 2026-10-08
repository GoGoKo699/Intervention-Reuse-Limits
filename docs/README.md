# Documentation map

[Overview](../README.md) · [Tutorial-to-result narrative](../REVIEW.md) ·
[Scientific contract](SCIENTIFIC_CASE.md)

The reading path starts from **Bo–Celani** and follows one
question: how many states must a positive kinetic model retain when it
is reused across controls at a specified accuracy?

## Learn the result

| Read | Purpose |
| --- | --- |
| [Bo–Celani review](https://arxiv.org/pdf/1612.04999), §1, §2 through §2.2, §2.3.2 | The selected single-source multiscale background |
| [Project narrative](../REVIEW.md) | Translate that background into this target, task, mechanism and state-count result |
| [Scientific guide](SCIENTIFIC_CASE.md) | Check the exact comparison classes, control menus and scope |
| [Scientific background](MANUSCRIPT_BACKGROUND.md) | Locate physical precedents and the closest theoretical results |

## Follow the proof spine

The first two notes explain the mechanism. R92–R94 and R98 supply the
current precision laws and finite-control consequence.

| Question | Proof or derivation |
| --- | --- |
| Which physical assumptions define the two switches? | [Community-model derivation](FAMILIAR_SWITCH_COMMUNITY_MODEL.md) |
| What does averaging the fast hidden sign achieve? | [Uniform two-state approximation](FAMILIAR_SWITCH_FAST_RELAXATION.md) |
| What changes when both control ticks stay positive? | [Fixed-clock quadratic law, R92](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) |
| What if the dwell times are unrestricted? | [All-duration law and reversible three-state construction, R93](FAMILIAR_SWITCH_RAPID_CONTROL.md) |
| Can three positive states ever be exact? | [General three-state boundary, R94](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md) |
| Can a specified finite menu force the third state? | [Three-setting pulse witness, R98](FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md) |

The three-setting menu has a two-state lower bound and a three-state
upper bound. Its fourth-state necessity is not proved. The reversible
three-state lower used by the all-word hierarchy comes from the separate
seven-word argument in R92.

## Check assumptions, attribution and evidence

| Record | What it checks |
| --- | --- |
| [Equilibrium-reduction note](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md) | Gibbs inheritance versus dynamical closure |
| [Physical assumption alignment](PHYSICAL_ASSUMPTION_ALIGNMENT.md) | Published model families and the chosen specializations |
| [Bibliography](../references/manuscript.bib) | Citation metadata |
| [Proof review](FINAL_SANITY_AUDIT.md) | Analytic checks, source comparisons and reproducibility |
| [Verification guide](VERIFICATION.md) | Commands, provenance and the limits of computational checks |

## Supporting results

The [finite-rate window](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md) and
[trace reduction](FAMILIAR_SWITCH_TRACE_REDUCTION.md) constrain the size
of the equilibrium-specific effect. The
[control-scope map](FAMILIAR_SWITCH_CONTROL_SCOPE.md) compares other
control and observation tasks.

The [results index](CLAIM_LEDGER.md) maps each claim to its proof,
verification report and source comparison. The
[supplementary results guide](STATE_COST_EXPLORATION.md) groups the
additional models, detector assumptions and acquisition bounds by topic.
[Further reading](TUTORIAL_OPTIONS.md) provides supporting textbook and
positive-realization material.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
