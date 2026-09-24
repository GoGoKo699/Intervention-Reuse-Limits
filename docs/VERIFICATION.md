# Verification scope and provenance

[Repository overview](../README.md) · [Core theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

## Reproducing the checks

From the repository root, install [the pinned dependencies](../requirements.txt) and run `make check`. The target checks local Markdown links, display-math/code-fence balance, Python syntax, report provenance, and the original MIT license. It then runs all fifty-nine mathematical verifiers and four separate deterministic replays of saved familiar-switch numerical models. Optional optimizers are not run. Fresh reports are written to `.check-output/`, not over the saved reports.

The workflow uses the same command. A saved local PASS does not establish that a GitHub Actions run completed; inspect the live workflow separately. Neither kind of test constitutes independent mathematical review or novelty certification.

## Current checkpoint: temporal records and signed-control feasibility

The published baseline is `2243fbedf8ae1a2ba944d6e33507d2e1613179d8`, tree
`8813fec08175fb15397499edc658ce44ef827f4b`, with successful
[CI run 36035495643](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/36035495643).
The new [scope assessment](FAMILIAR_SWITCH_CONTROL_SCOPE.md) links the
[passive/triple proof](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md),
[signed-control proof](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md), and
[primary-source comparison](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md).
The signed theorem includes every positive hidden/visible attempt-rate
ratio, the equality boundary, a finite 23-pair menu, and positive-margin
existence without a rival rate cap. Common preparation is essential and
differs from the old four-word arbitrary-preparation comparison.

The [new verifier](../scripts/verify_switch_control_scope.py) passes
**166 exact symbolic, rational, algebraic and provenance checks** under
pinned Python 3.13.5 and SymPy 1.14.0. Its largest matrix dimension is four.
The [report](../reports/switch_control_scope.json) binds 34 proof snapshots,
including the two new universal notes and the frozen physical-core input.
It checks the passive birth–death law and detailed balance, conditional
slice determinants and TV algebra, exact pair-preserving triple errors,
the signed triangle and threshold, arbitrary-rate closure independently
for the physical and reduced generators, and all entries of the 23-word
Hankel/shifted-table menu. Feasible, equality and infeasible fixtures use
exact arithmetic. There is no optimization, sampling or parameter sweep.

The two universal derivations and the unequal-rate appendix received
independent internal review. The positive-rate inequalities, transfer to
arbitrary three-state CTMC rivals, simple-spectrum logarithm argument and
compactness proof supply statements that finite fixtures cannot prove.
In particular, no numerical value is claimed for the signed finite-menu
TV margin. The temporal theorem's explicit lower margin is distinct from
its exact optimum under fixed pair marginals.

New verifier SHA-256:
`1343df7a5a3397ed7270f39fcbed2fcd98c6e9d5b79505b4913f7df12aa2e22c`.
New report SHA-256:
`93d74f9c605fbfcc69a70f825b722cc67f1ce39fd3aee4b4d4f460f792f0ac7d`.
All earlier proof snapshots, mathematical scripts, saved reports, license,
dependencies, workflow and claim rows R1–R66 remain unchanged.
These checks do not establish ideal sensor performance, hardware savings,
thermodynamic cost, literature priority or PRL significance.

The complete local `make check` passed: all 59 mathematical verifiers and
four saved-model replays regenerated **63 reports byte for byte**.
The baseline manifest confirmed all 296 files outside the nine intended
navigation/build edits and all 66 historical R rows were unchanged.
This checkpoint adds four notes, one verifier and one report. Remote CI
for the resulting commit is checked separately; the successful run linked
above belongs to the published baseline.

## Historical checkpoint: a source-grounded generic four-word theorem

The published baseline is `8c59beb11b4e4e19915ca31fefa7f5b8b0b37bdd`, tree
`5a450530164e6aa678e884deb327f8721a32c30f`, with successful
[CI run 36031718988](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/36031718988).
The continuation adds the [minimal theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md),
[community model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md),
[equilibrium reduction derivation](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md),
[central comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md), and
[internal scope review](FAMILIAR_SWITCH_PHYSICAL_CORE_REVIEW.md).
Older proof snapshots, mathematical verifiers, saved reports, dependency
pins, workflow and MIT license remain unchanged, as do claim rows R1–R65.

The [new verifier](../scripts/verify_switch_physical_core.py) performs
**95 exact symbolic, rational and provenance checks**, with largest matrix
dimension four. Its [report](../reports/switch_physical_core.json) binds
32 proof snapshots, including the three new model/theory derivations,
and the frozen preparation-free input certificate. It checks target and
predictor stationarity and moment closure independently, initial conditional
means, covariance and radius identities, rate positivity factorizations,
the charge-energy substitution, compensated gate control, equilibrium
force inheritance, and two counterexamples to dropping reduction hypotheses.
The full positivity and semigroup arguments are in the bound proofs;
finite rational fixtures are not a universal parameter sweep.

The proof and verifier received separate internal review. An independent
run reproduced the new report byte for byte using pinned Python 3.13.5
and SymPy 1.14.0. The verifier source SHA-256 is
`0bc9e8be9abf10987ebd1158d2509f938b779fcd861134bfabb38158937952df`;
the saved report SHA-256 is
`4b5da0f863c60f09dc656451528c97a1c768089a6d63074e1bfb31e2816c622b`.
No optimization, stochastic simulation or new detector assumption is used.
Physical acquisition accuracy, literature priority and PRL significance
are outside this certificate.

The complete local `make check` passed: all 58 mathematical verifiers and
four saved-model replays regenerated **62 reports byte for byte**. The
baseline manifest confirmed that all 289 files outside the nine intended
navigation/build-integration edits were unchanged, and all 65 historical
R rows were unchanged. The new checkpoint adds five notes, one verifier
and one report. Remote CI for the resulting commit must be checked
separately; the successful run linked above belongs to the baseline.

## Historical checkpoint: endpoint registration and relative force error

The published baseline is `77efdedb42b2ff18e54344617f6da25c016fe0ad`, tree
`cf2e2dec2b537a28a66bf38cf5a40f81cad0bf73`, with successful
[CI run 35994019903](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35994019903).
Its 56 mathematical verifiers and four saved-model replays were all reproduced
byte for byte in the preceding checkpoint. This continuation preserves 123
baseline source/report/license/dependency/workflow files, 66 proof snapshots
and historical claim rows R1–R63, totaling 189 protected files.

The [endpoint-registration proof](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md)
places oracle signs at the actual active boundaries. Arbitrary initial
measurement dynamics then belong to arbitrary rival preparation. A known
conditional endpoint-error ceiling $5\times10^{-6}$ permits asymmetry,
history dependence and error/backaction correlation. Its one-window detector
alternative has a continuous-martingale signal/noise bound and a separate
whole-acquisition leakage budget; closure, settling and release are included.
The target initial channel needs only a marginal stationary defect, not a
premeasurement-label/poststate joint bound.

The [relative-force proof](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md)
controls the singleton residual by $(1-u)(L-1)$ for residual likelihood spread
$L$. At $L=1001/1000$, the enlarged null retains size below $.04$ and target
miss below $.014$ in nine million trials and 18 million integration windows.
The nominal kinetic family's ideal four-pair state minima are three versus
four through TV $.0009$. A finite-CTMC rare-state counterexample, with an
irreducible extension, shows why an unweighted stationary-law TV allowance
cannot substitute for this relative force condition under arbitrary preparation.

The [new verifier](../scripts/verify_switch_endpoint_registration.py) and
[report](../reports/switch_endpoint_registration.json) bind both new proofs and
the frozen preparation-free certificate. The [internal review](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_INTERNAL_REVIEW.md)
checks the full joint-history filtration, post-instrument marginal argument,
noisy quota comparison, full acquisition span and relative-force inequality.
The [eight-source audit](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_SOURCE_AUDIT.md)
records inspected primary component precedents and their limitations. No
conditional detector envelope or achieved device performance is inferred from
average fidelity data. The full analog or serial transcript has no asserted
three-state realization.

The new verifier passes **104 exact checks** under pinned Python 3.13.5,
with largest dense matrix dimension four. It uses a frozen rational-polynomial
helper, no floating arithmetic and no optimization. It binds 31 proof snapshots,
including the two new universal proofs, and the frozen preparation-free input
report. Source SHA-256:
`9b690e1ac4766de787ed4943f17359a2a13f06476c145f19fde98fdba20a305b`;
canonical report SHA-256:
`bf8f3924d62609cad8235db49743bf6e476ac2873ff644e1976ce0512e989977`.
The coordinator inspected the complete final source and both new proofs.
The Makefile and both explicit checker registries include the new report.
A fresh complete `make check` passed **57 mathematical verifiers and four
saved-model replays**. All **61** generated reports were PASS and byte-identical
to their canonical reports, including an independent production replay of the
104-check endpoint certificate. Final repository checks passed 2675 local Markdown
links, 62 Python syntax checks, report/proof/source provenance and the unchanged
MIT license. All 189 protected baseline files and historical rows R1–R63 remain
byte-identical.

These are local checks of the final source snapshot. The successful CI run
linked above belongs to the named baseline; it is not automatically evidence
for a new commit. Publication uses a non-forced main update, followed by separate
checks of the resulting remote commit and its own workflow.

## Historical checkpoint: preparation-independent four-word test

The published baseline is `6f545598cd86bf8795eca8e58325c15e860a0889`, tree
`4aa478b1a9c5f6c2f3c1b1192b4d336eb4e0bc80`, with successful
[CI run 35991112119](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35991112119).
The baseline has 55 mathematical verifiers and four saved-model replays;
all 59 canonical outputs were reproduced in the preceding checkpoint.
This continuation preserves 121 baseline source/report/license/dependency/
workflow files, 63 bound proof snapshots, and claim rows R1–R61 byte for byte.

The new [four-word proof](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md)
removes rival preparation and mixing promises by conditioning on a singleton
visible sector. The [realization](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md)
fits all four complete ideal pair laws with the existing positive three-state
CTMC, throughout the full one-percent edge-prefactor box. Exact bounds certify
both signed residual magnitudes above $.009$ and state minima three versus
four for maximum pair-table TV error through $.001$. The comparison retains
strictly positive stationary laws, exact Gibbs tilt, fixed field kernels and
sign-preserving initial observation.

Nine million trials give ideal size below $.005$ and target miss below $.004$.
The [readout proof](FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md) uses seven
protected readings at both endpoints and two disagreement gates, retaining
size below $.015$ and miss below $.014$ at 126 million raw readings. It permits
same-use error/kick correlation but requires fixed fresh conditional error
probabilities and exact sector protection. The null needs no equilibrium
preservation by its instrument. Target power still needs its uniform conditional
execution budget and stationary initial block. The exact three-state upper
concerns four ideal pair tables, not the full fourteen-reading transcript.

The [new verifier](../scripts/verify_switch_preparation_free.py) and
[report](../reports/switch_preparation_free.json) bind the three new proofs,
frozen prerequisite reports and exact helper sources. The [internal review](FAMILIAR_SWITCH_PREPARATION_FREE_INTERNAL_REVIEW.md)
covers the universal algebra, completed-quota probability argument and noisy
selection bound. The [source comparison](FAMILIAR_SWITCH_PREPARATION_FREE_SOURCE_AUDIT.md)
distinguishes established conditional-return/reciprocity methods from this
combined preparation-independent state-count comparison.

The new certificate passes **209 exact checks**: 182 direct checks and 27
recomputed inherited perturbation checks, under pinned Python 3.13.5. The
largest dense matrix has dimension four; no floating arithmetic, optimizer
or parameter-grid simulation is used. It binds 29 proof snapshots, both
prerequisite reports and two frozen source imports. Source SHA-256:
`cbd3a0cf4a1617f1c85653e6b5e2bbfd82687a4df202bec925dbcdc7da4da356`;
canonical report SHA-256:
`dc10d2baf22899ef663faa4406d720998771e7c40c4de7ef4e8a7b2a3bed3df1`.
The coordinator inspected the full final source and the three universal
proofs. The Makefile and both checker registries include the new report.
A fresh complete `make check` passed **56 mathematical verifiers and four
saved-model replays**. All **60** generated reports were PASS and byte-identical
to their canonical reports, including an independent production replay of the
209-check new certificate. Final repository checks passed 2626 local Markdown
links, 61 Python syntax checks, report/proof/source provenance and the unchanged
MIT license. All 184 protected baseline files and historical rows R1–R61 remain
byte-identical; no historical proof or report was rewritten.

These are local checks of the final source snapshot. The successful CI run
linked above belongs to the named baseline, not automatically to a new commit.
Publication uses a non-forced main update, and the resulting remote commit and
its own workflow are checked separately after publication.

## Historical checkpoint: repeated protected readout

The published baseline `3f7a368f072f03add7e0fcb6e233556cc31b8a39`, tree
`3747fc54b6b12c7c42f192b220e85667c166fafc`, has successful
[CI run 35986291952](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35986291952).
A fresh baseline `make check PYTHON=.venv/bin/python` passed 54
mathematical verifiers and four saved-model replays in the pinned Python
3.13.5 environment. All 58 outputs were PASS and byte-identical to their
saved reports. This continuation preserves 119 baseline verifier/report/
license/dependency/workflow files, 62 bound proof files and claim rows
R1–R60.

The [repeated-readout proof](FAMILIAR_SWITCH_REPEATED_READOUT.md) gives
an exact equilibrium joint-TV identity, including errors correlated with
the hidden update of the same read. Seven fresh sector-preserving reads
with a stationary nonselective kernel have joint defect equal to their
binomial majority error. At raw error $.02$, the defect is
$.0000053356544$, below the existing $10^{-5}$ instrument allowance.
One first-pair disagreement statistic on the same five million trials
handles unknown rival errors in $[0,1/2]$. The old serial score keeps
size below 5% and power above 95%, with 40 million raw readings.

The [new verifier](../scripts/verify_switch_repeated_readout.py) and
[report](../reports/switch_repeated_readout.json) check exact tail,
calibration and sampling arithmetic and propagate the earlier correlated-
kick instrument through a repeated block. The universal proof supplies
the arbitrary-state, history-conditional statements; finite fixtures do
not enumerate them. The [internal review](FAMILIAR_SWITCH_REPEATED_READOUT_INTERNAL_REVIEW.md)
and [source comparison](FAMILIAR_SWITCH_REPEATED_READOUT_SOURCE_AUDIT.md)
keep standard repetition/concentration tools distinct from this
witness-specific repair.

The new verifier passes **158 exact checks** with largest dense matrix
dimension three, no floating arithmetic, no optimizer and no imported
repository helper. It binds 26 proof snapshots and the two frozen serial-
reset and observable-calibration reports. Source SHA-256:
`cc900a338ef0463206e9c0a2832008ed4a751c47de613850c4b88660a12c028f`;
report SHA-256:
`488a3e39aca64284acc388a91fd38d479b14b727eec0fbf6b21772225391d086`;
new proof SHA-256:
`4c9b6a873005f7a0798e99d3edededd7a39607d1c85252221b1e692af13d1182`.

Fresh errors conditional on the full preceding history, sector protection,
nonselective stationarity and final independent electronics remain
substantive premises. The old approximate-null TV allowance concerns
retained pairs; the diagnostic needs its own conditional-mean guarantee.
The old three-state predictor does not establish a predictor for the full
eight-reading transcript. Preparation and device feasibility remain open
operational questions, and manuscript drafting remains deferred.

**Completed local gate:** `make check PYTHON=.venv/bin/python` exited
successfully under Python 3.13.5 with pinned NumPy 2.3.5, SciPy 1.17.0,
SymPy 1.14.0 and mpmath 1.3.0. All **55 mathematical verifiers and four
saved-model replays** passed. The **59 fresh reports** are PASS and
byte-identical to their canonical reports. Separate review reproduced
the new 158-check report exactly. All 119 protected baseline files,
62 prior proof snapshots and historical rows R1–R60 are unchanged.
The repository checker and `git diff --check` pass. The new calculation
uses at most three states in its matrix fixtures; the historical suite
maximum remains 68. No large simulation was run.

Publication and GitHub Actions are separate evidence. The baseline CI
linked above certifies only the previous commit; the new commit's status
is checked after non-forced publication. Manuscript drafting remains
deferred.

## Historical checkpoint: observable preparation and readout boundaries

The published baseline `f026f67d26b8f5617ff5a27ea1c99648b4a85e69`, tree `0d88522949938e6ccc5b5cbeae4802130dd3ffa5`, had 53 mathematical verifiers, four saved-model replays and successful [CI run 35981239851](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35981239851). This continuation protects all **117** baseline verifier/report/license/dependency/workflow files, earlier proof bindings, nine recovery files and historical claim rows R1–R58.

The [observable preparation theorem](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) controls specified equilibrium response errors from an arbitrary preparation on at most three states. Its proof separates visible imbalance from within-sector imbalance, avoiding inverse-relaxation amplification of the stationary-bias term. A five-type experiment supplies the response drifts and a relaxation guard under an exactly sector-preserving, stationary instrument with independent symmetric electronics. The prefixed types must apply the same instrument silently before the low wait. This does not inherit the previous nonzero joint-instrument allowance.

The [sampling theorem](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) randomizes type after preparation and uses known assignment probabilities. All predictable responses refer to one random pathwise averaged preparation; conditional concentration is applied without conditioning on that final average. An eight-sign, two-tail union gives simultaneous corrected-score precision $.001$ with probability above 96% at **60 billion trials**. This conservative sufficient precision budget is not a necessary cost or a complete rejection/power guarantee. Guard estimation, stationary localization, target error costs and any prediction allowance remain separate.

The [readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) gives a three-state ordinary reversible example whose visible-sector preservation, immediate repeated noisy readings, low-only records and nonselective endpoint checks all agree with independent nondisturbing readout, yet each original joint table differs by TV $1/4800$. The electronic error is correlated with a hidden kick. Conversely, with independent electronics and sector preservation, at most three states imply equality between the joint disturbance and a suitable endpoint-insertion disturbance. Neither statement claims that the example passes the target's score gates or that all calibration is impossible.

The [verifier](../scripts/verify_switch_observable_calibration.py) produces [switch_observable_calibration.json](../reports/switch_observable_calibration.json) with **75 exact checks**, largest dense dimension three, no floating arithmetic and no optimization. Source SHA-256: `6bf14a993246a3770aa829cd65cc9c2dedb9aff516c1072af1ec939392acfdab`; report SHA-256: `5883635e5d44264c9cc72ba585f16aa65b2441837ef3cf4d69e54ba3b878ae1c`. It binds 25 proof snapshots, the frozen serial-reset input report and the inherited rational helper. The three new proof hashes are unconditional: preparation `deb3e0e892ee790a97f96f3684091c9fccca78ef3db6a135b8237a2b79680ccd`, readout `751f35f34dc63cfd481694550e09276a7c1115d5464731eacaacd6a7305916c3`, and sampling `be46dd47f5a6d0ef07300c59349ff282f45c185d9aca673731f75bc2d9e55c56`. The frozen prerequisite's source and proof bindings are checked before the new arithmetic.

The [independent internal review](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_INTERNAL_REVIEW.md) and [focused source comparison](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md) separate finite arithmetic, universal proofs and source attribution. The existing two-word state advantage, five-million-trial theorem and finite reset retain their scopes. No three-state upper for the added calibration data, device demonstration or PRL readiness follows. Manuscript drafting remains deferred.

The separate reviewer inspected the complete final verifier and independently reproduced all **75 checks**, with a canonical report byte-identical to the saved evidence. The coordinator reviewed the proofs, full source and exact fixture changes. These checks support the proofs; they do not enumerate all possible rival models or histories.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **54 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The captured log contains all **59** commands including the repository checker. All **58** fresh reports are PASS and byte-identical to saved evidence. All 117 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R58 remain unchanged. After final documentation integration, the repository checker passes **2,518 local Markdown links**, **59 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension three; the historical suite maximum remains 68.

Published-commit CI is checked separately after non-forced publication; the baseline CI above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: serial trials and finite reset

The published baseline `e80ebbf78f92332e911d35818ae8c6fe659cc77a`, tree `36b901a2782b43885af315055c0f603055f850bb`, had 52 mathematical verifiers, four saved-model replays and successful [CI run 35979212122](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35979212122). This continuation protects all **115** baseline verifier/report/license/dependency/workflow files, earlier proof bindings, nine recovery files and historical claim rows R1–R56.

The [serial sampling theorem](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) retains five million trials, the existing gates and threshold $.0021$, with false rejection below 5% and power above 95%. It replaces fresh-trial independence by a uniform conditional TV promise relative to one fixed stationary reference pair. A fixed-reference case split and widened conditional variance boxes justify the martingale concentration argument. The serial approximate null is conditional on the past; a marginal approximation promise alone is insufficient.

The [finite-reset theorem](FAMILIAR_SWITCH_FINITE_RESET.md) proves that 63 actual low-field attempt units prepare every member of the one-percent four-state family within TV $10^{-5}$, conditional on any pre-reset history. The target gap is at least $99/500$ and minimum stationary mass exceeds $1/21$. The constructive three-state predictor also meets that reset duration through a separate weighted-kernel bound. Its finite-preparation one-trial comparison with the target is below $.00009$, without a full-sequence TV assertion. Arbitrarily slow ordinary rivals require their own conditional preparation guarantee; the broad population lower bound is unchanged.

Reset plus active evolution costs **327.5 million nominal attempt units**, 26.2 times active-only exposure. Active-clock allowance adds at most 100 units; reset-clock allowance, ten million readouts and control overhead are accounted for separately. No laboratory frequency or device capability is assumed.

The [new verifier](../scripts/verify_switch_serial_reset.py) produces [switch_serial_reset.json](../reports/switch_serial_reset.json) with **79 exact checks**, largest dense dimension four, no floating arithmetic and no optimization. Source SHA-256: `b72d58664fed11d9965aea292a938b330118ea8deb491fc13fe11ad40e066526`; report SHA-256: `9c9f662e63d94d518d3e01bf0aa179dffa6f06d78a2333660e3668582d972fb6`. Both new proof hashes are unconditionally bound: sampling `773ded5fba43a9b3390f404b4f259646c8515bce453f334a65228013418d2f6f` and reset `93873fc5ef107f82b0dc58bac71de0ec856b4508fb156662af6f0df3609f5b00`. The report binds 22 proof snapshots, the frozen percent-kinetic input report and the inherited rational helper. The source and proof bindings in that prerequisite are checked against their frozen expected values.

The separate reviewer and coordinator inspected both proofs and the full final source, including the constructive predictor's reset. An independent production replay passed all **79 checks** and reproduced the canonical report byte for byte. The [internal review](FAMILIAR_SWITCH_SERIAL_RESET_INTERNAL_REVIEW.md) separates conditional-law, gate, mixing and resource checks; the [source audit](FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) attributes the standard martingale and Dirichlet-form tools. These finite checks support the analytic arguments; they do not enumerate all possible histories or rival models. Manuscript drafting remains deferred.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **53 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The captured log contains all **58** commands, including the repository checker and final snapshot replay. All **57** fresh reports are PASS and byte-identical to saved evidence. All 115 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R56 remain unchanged. After final documentation integration, the repository checker passes **2,431 local Markdown links**, **58 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is checked separately after non-forced publication; the baseline CI above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: one-percent kinetics and a local three-state realization

The published baseline `24c2cc3185dbff17ce23c366413484fe94e25656`, tree `cce6133f62ead44e27d346491075b92d984884f1`, had 51 mathematical verifiers, four saved-model replays and successful [CI run 35975279317](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35975279317). This continuation protects all **113** baseline verifier/report/license/dependency/workflow files, earlier proof bindings, nine recovery files and historical claim rows R1–R54.

The [direct kinetic theorem](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md) covers eight independent symmetric edge factors in $[.99,1.01]$, four for each fixed plateau generator. A uniform rational coefficient certificate gives $R>.00389$, $T>.00367$ and stationary ordinary-three-state gap $>.001$. The [local realization](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md) constructs a general three-state CTMC reproducing both nominal-field stationary joint tables exactly for each allowed target. It does not assert exact prediction of arbitrary words, clocks or full paths.

With each inherited execution allowance $10^{-5}$, the target external joint-TV budget is $.000078025101$ and the rival budget $.00002$. The actual ordinary-three gap exceeds $.000901974899$; the general-three upper is below $.00008$. Thus the exact minimum counts are three and four on $[.00008,.0009]$, within the inherited stationary uncertainty class. The predictor uses the nominal tilt; actual field and clock deviations are charged externally, and its possible actual-tilt stationary defect is bounded by the inherited $10^{-5}$ allowance.

The [new score test](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md) retains the integer score and five million fresh independent paired trials, but certifies new rational gates and threshold $.0021$. The ordinary-null observed-joint-TV allowance remains $.0002$, above the constructive upper. Null and target concentration boundaries are respectively below $.002078$ and above $.002154$; target gate failure is below $.004$. False rejection is below 5% and power exceeds 95%. The one-percent sufficient edge allowance is 500 times the preceding 20-ppm allowance; neither bound is asserted optimal.

[verify_switch_percent_kinetics.py](../scripts/verify_switch_percent_kinetics.py) produces [switch_percent_kinetics.json](../reports/switch_percent_kinetics.json) with **170 exact checks**, largest dense dimension four, no floating arithmetic and no optimization. Source SHA-256: `6e59c54164d8bef4cca9a45b88a8b70c7dfcbfbd20afbaebc52d7aa7e9358525`; report SHA-256: `4ddbddfef6c3c31fc5785a21e51aeac521b0b8c5685e595a7b86c615d6ee807e`. Three new proof hashes are unconditionally bound: kinetic `0a98d76eb922250ceabc3c72d3801b40f12be67330a32b1dd9ba7e3018d78499`, realization `1e97c8fba182c5c9b320403ceede28b5782d58d6f1c23237a48e272bc51065b4`, and score `32e9962422ea9943d41dfe708e7926a06bd56cadd2a79c4c791033ea2317c8b8`. The report binds 20 proof snapshots, two frozen input reports and the rational helper. Every inherited source and proof is checked against its frozen expected value.

The [internal review](FAMILIAR_SWITCH_PERCENT_KINETIC_INTERNAL_REVIEW.md) records the coefficient and Dyson tails, detector monotonicity, symbolic full-table fit, scalar-log CTMC embedding, execution transfer and finite-sample checks. The [source audit](FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) attributes established realization and logarithm methods while limiting the claim to the specified controlled tables. Preparation, measurement and fresh-trial assumptions still need operational support. Manuscript drafting remains deferred.

The separate reviewer inspected the complete final source, independently reproduced the rational embedding-box bounds and reran the pinned production verifier. All **170 checks** passed and the canonical report was reproduced byte for byte. The coordinator also inspected the full source and reproduced the report in the full regression gate. These checks support the analytic arguments; they do not enumerate all admissible rivals.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **52 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The captured log contains all **57** commands, including the repository checker and final snapshot replay. All **56** fresh reports are PASS and byte-identical to saved evidence. All 113 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R54 remain unchanged. After final documentation integration, the repository checker passes **2,362 local Markdown links**, **57 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence, checked after non-forced publication; the baseline CI above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: kinetic tolerance and protected initial readout

The published baseline `2ffed6de204354e257a344359497fb1e059cc04e`, tree `bcccfafdc14dc8abbc3b5187bf4751f424c297e9`, had 50 mathematical verifiers, four saved-model replays and successful [CI run 35972519604](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35972519604). This continuation protects all **111** baseline verifier/report/license/dependency/workflow files, earlier proof bindings, nine recovery files and historical claim rows R1–R52.

The [kinetic theorem](FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) permits fixed plateau generators with the same stationary Gibbs laws and detailed balance, while abandoning exact heat-bath closure. Integrated full-row generator TV defect at most $10^{-4}$ leaves the general-three-state error at most $0.00012$ and ordinary-three error greater than $0.0009274999$. Thus the exact minimum counts are three and four on $[0.00012,0.0009]$. A sufficient relative symmetric-edge allowance is 20 ppm; the separate 100-ppm row retains only the narrower population interval $[0.0005,0.00055]$.

The [score extension](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md) reuses the frozen integer lookup tables and gates with 2.5 million fresh independent trials per arm, **five million total**. Threshold $0.0022$ gives false rejection below 5% and power above 95%, including ordinary-null observed-TV allowance $0.0002$, which exceeds the constructive general-three upper. This covers a larger target family and is not an improvement on the earlier two-million-trial count.

The [protected-readout theorem](FAMILIAR_SWITCH_PROTECTED_READOUT.md) preserves the initial-label/postmeasurement-state joint law whenever the instrument preserves the observed sector and its conditional equilibrium law. Hidden transitions need no common upper rate bound. Leakage and conditional flux imbalance supply an explicit joint-error budget, with preparation charged once. The operation requires barrier control as an instrument resource. Independent electronics and adequate preparation remain premises; finite waiting does not establish independent trials.

[verify_switch_kinetic_interface.py](../scripts/verify_switch_kinetic_interface.py) produces [switch_kinetic_interface.json](../reports/switch_kinetic_interface.json) with **90 exact checks**, largest dense dimension four, no floating arithmetic and no optimization. Source SHA-256: `1adcc35e8698d7758625c7c38875fde9c3c1686722ab73c1bcbd4437ee381de9`; report SHA-256: `cfb051fbac02d96c5ae3912f80ab42610be426a90127d70173d8e3bbd33e4472`. The three new proof hashes are unconditionally bound: kinetic `fb46d03dc616c78035ced22c62b936f1e3a8c91aac86b0587b3803a0e9e8b5bd`, score `fc5db926ee202f479ccbf5436a2a3ae19ce976a43faea2201f8af89d7f4998f3`, and protected readout `7036d895e2a23dd33105c2ae96ace62904ae86954b0dcfadba18f290be6bd309`. The report binds 17 proof snapshots, the frozen weak-field input report and the rational helper. The inherited source/proof snapshots are checked against the frozen input's expected values.

Separate analytic and source review is recorded in the [internal review](FAMILIAR_SWITCH_KINETIC_INTERFACE_INTERNAL_REVIEW.md). The [primary-source audit](FAMILIAR_SWITCH_KINETIC_INTERFACE_SOURCE_AUDIT.md) distinguishes barrier-control precedents from an achieved device specification. The exact fixtures include nonuniform reversible edge factors that break the original affine closure and a protected instrument with large hidden-state disturbance but zero equilibrium joint disturbance.

The separate reviewer inspected the final source, including its explicit affine-closure failure fixture, and independently reproduced the canonical report byte for byte with all 90 checks passing. The coordinator's additional replay also matched exactly. These finite checks support the analytic arguments and do not enumerate all admissible rivals.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **51 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The captured log contains all **56** commands, including the repository checker and final snapshot replay. All **55** fresh reports are PASS and byte-identical to saved evidence. All 111 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R52 remain unchanged. After final documentation integration, the repository checker passes **2,276 local Markdown links**, **56 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence, checked after non-forced publication. The baseline CI cited above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: a weaker field, a larger gap and fewer trials

The published baseline `7e41d378e87ce5d7524e585c387707638c391ae1`, tree `eafae1855a511389c4d07e8fe730a3f6795ff3dc`, had 49 mathematical verifiers, four saved-model replays and successful [CI run 35969236097](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35969236097). This continuation protects all **109** baseline verifier/report/license/dependency/workflow files, earlier mathematical proof bindings, nine recovery files and historical claim rows R1–R50.

The [weaker-field theorem](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) keeps $J=\log3$, uses $H=\log2$ and equal dwell times $5/4$, with the same two word orders and initial/final binary records. Target bit errors remain at most one percent and rival errors may be any independent symmetric values up to one half. The nominal recorded-table gap exceeds $0.00115$; the stationary robust gap exceeds $0.001125$. Preparation, field, timing and initial-disturbance allowances $10^{-5}$ retain actual gap $>0.001$ and a general-three-state upper $2\times10^{-5}$. Thus the state minima are three and four on $[2\times10^{-5},10^{-3}]$. Increasing those six execution allowances to $5\times10^{-5}$ retains the separate interval $[10^{-4},6\times10^{-4}]$, without a transferred sampling allocation.

The [integer-score test](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) has sufficient totals **2 million** and **2.5 million paired trials**, equally divided between the arms, for the exact ordinary null and its observed-joint-TV $10^{-4}$ enlargement. Both have false rejection below 5% and target power above 95% at the smaller physical tolerances. The new two-million upper lies below the frozen old operating point's necessary expectation $810000\log19$, even for adaptive sampling and stopping there. This is a design-specific comparison, not a transfer of the old lower bound to the new experiment or a global optimum. The exact noise-penalty identity explains why the new setting can have a smaller ideal witness and a larger noisy one.

[verify_switch_weak_field.py](../scripts/verify_switch_weak_field.py) produces [switch_weak_field.json](../reports/switch_weak_field.json) with **172 exact checks**, maximum dense dimension four, no floating arithmetic and no optimizer. Source SHA-256: `b9904605d62f696711fa8bc8664007e186dd5b4e9b2839aa275bcb77d6cd6258`; report SHA-256: `6289576de985afec146faeef47ef504105bc98ca986c6ce8a8bed70dbb2c6a5d`. The robustness proof is pinned at `b878a14a2f56a751808ae3e4b2befd705035f56f8ad58e98282ac707377d00ea` and the score proof at `ddc0f8c16bc8c4289c2b7481d5ff1ef6e920714a141553cfe37bfd028220de6f`. Fourteen proof snapshots, three frozen input reports and the inherited rational helper are bound unconditionally.

The coordinator and separate reviewer inspected the complete source and both proofs. An independent final pinned CLI run passed all 172 checks and reproduced the canonical report byte for byte. The [internal review](FAMILIAR_SWITCH_WEAK_FIELD_INTERNAL_REVIEW.md) records the analytic, variance, gate, physical-transfer and comparison checks, including the aligned charge-predictor coordinates and the distinction between sufficient and necessary counts. The [source audit](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) attributes the established statistical tools and retains the physical and priority boundaries.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **50 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete captured log contains all **55** commands, including the repository checker and final snapshot replay. All **54** fresh reports are PASS and byte-identical to saved evidence. All 109 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R50 remain unchanged. After final document integration, the repository checker passes **2,194 local Markdown links**, **55 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence and is checked after non-forced publication. The baseline CI cited above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: integer scores and the value of detector calibration

The published baseline `9983da2206c0a84e1ce5e111a9d132331afe70f5`, tree `5da1fadc9fe9877e916a5b2a2c775ea6dcfe256d`, had 48 mathematical verifiers, four saved-model replays and successful [CI run 35966287099](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35966287099). This continuation protects all **107** baseline verifier/report/license/dependency/workflow files, earlier mathematical proof bindings, nine recovery files and historical claim rows R1–R48.

The [new score test](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md) keeps the same two pulse orders, target operating point, independent symmetric detector classes and physical allowances. A fixed integer score for each recorded pair, including opposite initial-bit corrections whose expectations cancel, reduces the sufficient count from 508 million to **32 million paired trials**. A second design uses **90 million trials** to reject every pair of observed laws within joint-TV $10^{-4}$ of the ordinary null. This allowance exceeds the general-three constructive error $2\times10^{-5}$. Both designs have false rejection below 5% and target power above 95%; no Gaussian approximation, fitted test coefficient or added observation protocol is used.

The [information-cost proof](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) supplies one fixed positive rational ordinary comparator with a perfect detector, compared with the target's one-percent-noisy recorded law. Exact per-arm Taylor KL bounds are below $1/900000$. Hence any uniformly valid fresh-trial test of the unknown-detector class needs $\mathbb E_*N>810000\log19$, or at least **2,384,996** trials for a fixed count, even allowing adaptive arm choice and the stated stopping rules. The same target is covered by the earlier calibrated 1.2-million sufficient test. This establishes the value of that narrower detector promise, without pricing calibration or claiming optimality.

[verify_switch_uncalibrated_score.py](../scripts/verify_switch_uncalibrated_score.py) produces [switch_uncalibrated_score.json](../reports/switch_uncalibrated_score.json) with **131 exact checks**, maximum dense dimension four and no floating arithmetic or optimizer. Source SHA-256: `32311e7e0050816be3ec00d0a06b1b2f0b566ba0157a38dd29da0e21f9e6fd85`; report SHA-256: `28c432062f3c081c8bf727dcf2299036de35e1c5df13f30e8433b8601a91c182`. It pins both new proofs, twelve proof snapshots in total, two input reports and the inherited rational helper. An independent final pinned run reproduces the canonical report byte for byte.

The [internal review](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_INTERNAL_REVIEW.md) records the analytic and source checks, including the corrected target decimal floor, equality endpoint and empirical-summary wording. The [source audit](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md) attributes the established concentration, control-variate and adaptive-information ingredients. Existing physical assumptions and novelty boundaries remain in force.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **49 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete captured log contains all **54** commands, including the repository checker and final snapshot replay. All **53** fresh reports are PASS and byte-identical to saved evidence. All 107 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R48 remain unchanged. The checker passes **2,113 local Markdown links**, **54 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence and is checked after non-forced publication. The baseline CI cited above certifies only that earlier commit. Manuscript drafting remains deferred.

## Historical checkpoint: unknown detector contrasts and a charge-model bridge

The published baseline `778954f18164c3a228b845be07298ba1a33326eb`, tree `e08a840c71d2474a5ad4866d9daf1c39969e92f6`, had 47 mathematical verifiers, four saved-model replays and successful [CI run 35962664555](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35962664555). This continuation protects all **105** baseline verifier/report/license/dependency/workflow files, all earlier proof bindings, nine recovery files and historical claim rows R1–R45.

The [unknown-detector proof](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) eliminates the two independent symmetric detector contrasts using four corners of a bilinear polynomial. Its numerical guarantee allows target bit errors anywhere in $[0,0.01]$ and rival errors anywhere in $[0,0.5]$, with the specified channel form fixed across protocols. It certifies nominal recorded joint-TV gap $>3/8000$ and, under the existing physical/stationary allowances, actual gap $>1/5000$. The general-three upper is $1/50000$. A new localized confidence-box test has both error probabilities below 5% with 508 million independent paired trials, or 1.016 billion binary readouts. This is a conservative sufficient allocation for the enlarged exact-null class, not a transfer of the old calibrated score budget.

The [charge-model derivation](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) gives an exact sequential-tunneling specialization and a positive three-state predictor for attempt ratios $[2/3,2]$, with common exit cap three in observed-attempt units. The old numerical gap and sample counts remain restricted to equal attempts. The [preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) gives two continuous-time counterexamples to insufficient observable checks and an optional five-protocol response-preparation bound. The [primary-source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) does not claim a demonstrated device meeting all tolerances.

[verify_switch_physical_interface.py](../scripts/verify_switch_physical_interface.py) and [switch_physical_interface.json](../reports/switch_physical_interface.json) bind the three new mathematical notes and the inherited exact snapshot premise. They use rational arithmetic, small formal polynomials and matrices of dimension at most four. The [internal review](FAMILIAR_SWITCH_PHYSICAL_INTERFACE_INTERNAL_REVIEW.md) records the independent proof/source checks and the statistical localization correction. Universal conclusions still depend on the analytic arguments, rather than enumeration of rivals.

The final new source SHA-256 is `d15d2066419b98e6994d31a120d869b6cc2d3820b7f93d7482bda8b6e45af523`; report SHA-256 is `b0ada0ff7f600d974fdffc52ea315a071394eb0d7b487d6b8a1ba3d37e303157`. Its **108 exact checks** include three unconditional expected-proof-hash checks. The report binds all three new proof notes and seven inherited snapshots, imports the frozen snapshot report `b8ee6fb70d37d104ea89fe04e28c8872a8c81f97d108771bd89d14ef2ad9e2cb`, and identifies the frozen rational helper. An independent final pinned replay reproduced the canonical report byte for byte.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **48 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete captured log contains all **53** commands, including the repository checker and final snapshot replay. All **52** fresh reports are PASS and byte-identical to saved evidence. All 105 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R45 remain unchanged. The checker passes **2,036 local Markdown links**, **53 Python syntax checks**, report/source/proof/input provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence and is checked after non-forced publication. The baseline CI cited above certifies only that earlier commit. No manuscript was drafted.

## Historical checkpoint: direct snapshots and fixed-score tests

The published baseline `5ad525792de4e4fe6c681b067d7185e018265082`, tree `cdfa71f58ca37c832f5631e5c21484ae88b25805`, had 45 mathematical verifiers, three saved-model replays and successful [CI run 35958827202](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35958827202). This continuation protects all **99** baseline verifier/report/license/dependency/workflow files, all earlier proof bindings and nine recovery files.

The [direct snapshot proof](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) establishes a conditional-covariance witness on two initial/final joint laws from opposite pulse orders and one low-field preparation. Its nominal joint-TV gap is bracketed by $(23/12500,37/20000)$, ratio $185/184$. The lower covers every ordinary rival with at most three states; the upper is one positive rational feasible comparator. The exact general three-state predictor matches the two joint laws through shared conditional coordinates. Full multitime path-law matching is not asserted.

The new biased/approximate-force residual excludes stationary joint-TV radius $0.0018$ under the stated $10^{-4}$ bias/tilt and $10^{-5}$ high-law discrepancy budgets. Preparation, fixed field/tick errors and initial disturbance $10^{-5}$, plus independently flipped electronic records with probabilities $0.01\pm10^{-5}$, retain recorded separation $>0.0015$. A constructive general upper is $4\times10^{-5}$. The detector noise level, its uncertainty and hidden-state disturbance are distinct assumptions. Arbitrary state-dependent or persistent detector memory is excluded.

[verify_switch_snapshot_design.py](../scripts/verify_switch_snapshot_design.py) produces [switch_snapshot_design.json](../reports/switch_snapshot_design.json) with **168 exact checks**, using rational polynomial arithmetic and frozen-helper matrix-exponential enclosures at dimension at most four. It certifies nominal and robust boxes, the explicit ordinary comparator, detector/physical budgets, and the [snapshot score allocations](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md). It also bounds comparator KL per paired trial by $1/30000$, giving ideal expected count $>27000\log19$ and fixed count at least 79,500 through the analytic information argument.

[verify_switch_endpoint_score.py](../scripts/verify_switch_endpoint_score.py) produces [switch_endpoint_score.json](../reports/switch_endpoint_score.json), with **59 exact checks** for the [endpoint score test](FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md). Its three sufficient totals are 1,450,000, 1,670,000 and 1,890,000 single-readout trials on the original nominal/calibrated/finite-accuracy classes. The snapshot test has totals 900,000, 1,000,000, 1,200,000 and 1,500,000 paired trials, with two binary readouts each and distinct physical/detector premises. The last noisy row excludes observed-joint-TV approximation within $10^{-4}$. All fixed designs have false rejection below 5% and target power above 95%; none is claimed optimal.

The [snapshot numerical replay](../scripts/screen_switch_snapshot_witness.py) and [report](../reports/switch_snapshot_screen.json) preserve two sign-constrained local fits and the rounded exact-feasibility model. They retain full generators, laws and joint tables; check the balanced moment/TV relation and the positive general predictor's conditional-coordinate match; and run no optimization in default or CI mode. Numerical achieved errors are diagnostics, separate from the exact universal lower and rational feasible upper.

The [internal review](FAMILIAR_SWITCH_SNAPSHOT_INTERNAL_REVIEW.md) records independent proof/source checks. The [source comparison](FAMILIAR_SWITCH_SCORE_SOURCE_AUDIT.md) attributes variance-sensitive concentration and union-null testing, while retaining earlier physical-source limits. Preparation and disturbance bounds, fixed shared devices, and fresh-trial independence remain premises. No large simulation or manuscript drafting was performed.

Final snapshot source SHA-256: `a98814e12ddbef4eeed33b827ed0df1d87df1ec6f481f1963441a87541f690f8`; report: `b8ee6fb70d37d104ea89fe04e28c8872a8c81f97d108771bd89d14ef2ad9e2cb`. It unconditionally binds the robustness proof `80480b209ba862e252a7432702d0cd632d64955f2402f17ffeef70c29eff75e4`, score proof `5afeaeffd7adc2fe132b4ea2e53d54000c205207bf8ab0914e1a6c0545000302`, and five inherited proof snapshots. Endpoint source: `130b97e081bafae5e03979db6f4da6987ec6069770701e31ebcc84d1dfce67f0`; report: `3fb6860c9e4868c1f3d6abeabc2ecfeacc4f66216a8dd555c20b5df7df7592d1`. Snapshot replay source: `37b9fcd5d3b3c22c9b27dae6bf8e28e2d58d9c4ffc449aecdfb1e845a3d66552`; report: `ea7aafbc80cc6c9b244440856e61152146519ac81c1512e4fb67f750d89e0328`. Independent pinned reruns reproduce all three final reports byte for byte.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed **47 mathematical verifiers and four saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete captured log contains all 52 commands, including the repository checker and final snapshot replay. All **51** fresh reports are PASS and byte-identical to saved evidence. All 99 protected baseline files, earlier proof bindings, nine recovery files and historical claim rows R1–R43 remain unchanged. The final checker passes **1,943 local Markdown links**, **52 Python syntax checks**, source/proof/input-report provenance and the original MIT license; `git diff --check` passes. New work uses maximum dense dimension four; the historical suite maximum remains 68.

Published-commit CI is separate evidence and is checked after non-forced publication. The baseline CI cited above certifies only that earlier commit. No manuscript was drafted.

## Historical checkpoint: four endpoints from two equilibria

The published baseline `3c56fd45ff5f5988e59c0a4aff833663b53ded53`, tree `6195a00f28c296b9e7b38309e604559e7c1f0068`, had forty-four mathematical verifiers, two saved-model replays and successful [CI run 35944183992](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35944183992). This continuation preserves all **95** protected baseline verifier/report/license/dependency/workflow files, earlier proof bindings and nine recovery files.

The [four-endpoint proof](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) adds a second equilibrium preparation and derives an exact conditional-covariance identity. Every ordinary rival with at most three states has a singleton sector and hence satisfies one of two quadratic equalities. The physical pair violates both for every finite positive coupling, field and pulse duration. The existing three-state stationary predictor matches both preparations. No rival rate cap, determinant or inverse is needed.

At $J=H=\log3$, tick $3/2$, the new certificate brackets the best ordinary-three-state occupation error by $(9/5000,1/550)$ on the same four cells, a ratio $100/99$. It certifies the universal lower by a full response-box exclusion and the upper by one fixed rational feasible generator pair. The six-variable biased/approximate-force box excludes occupation error $17/10000$ with the stated stationary-law uncertainties. Simultaneous preparation, field and timing errors $10^{-5}$ leave actual gap $>1/625$ and state minima three versus four for $10^{-5}\le\delta_P\le1/625$.

The [cost analysis](FAMILIAR_SWITCH_PREPARATION_COST.md) derives four-cell confidence tests, separate validity and power guarantees, low/high target reset waits 62/36 and a distinct adaptive-information lower. At both error probabilities 5%, the sufficient endpoint totals are 12,531,296 nominal, 15,859,920 calibrated and 18,045,064 with calibrated occupation allowance $10^{-4}$. The ideal-case expected lower is $59400\log19$; fixed budgets require at least 174,900. The optional two-order initial/final observation corollary has a separate $1/1000$ joint-TV gap under exact preparation and tilt. The endpoint calibration and sample counts are not transferred to it.

The [new exact verifier](../scripts/verify_switch_preparation_witness.py) and [report](../reports/switch_preparation_witness.json) provide **132 exact checks** at maximum dense dimension **4**, with no optimizer or floating exponential. The complete mathematical source and imported helper were independently reviewed and replayed under pinned Python 3.13.5. Final report binding covers both new proof notes, the frozen calibration extension and both earlier switch proofs. The analytic singleton/covariance proof supplies the all-rival implication; the finite arithmetic is an essential premise of the numerical thresholds.

The [new numerical replay](../scripts/screen_switch_preparation_witness.py) and [saved report](../reports/switch_preparation_screen.json) retain both bounded singleton-sign fits and the rounded rational upper. Full generators, laws and responses are saved. Default and CI execution perform no fitting, use comparison tolerance $2\times10^{-11}$ and separately check positive three-state mean closure from both preparations. Independent full-source review and pinned replay passed. These achieved numerical uppers do not establish a global optimum or an all-protocol approximation.

The [internal review](FAMILIAR_SWITCH_PREPARATION_INTERNAL_REVIEW.md) separates analytic, numerical and statistical evidence. The [source audit](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) records inspected primary reciprocity, response and dimension-witness literature; it does not certify novelty. The added equilibrium preparation or noninvasive initial observation is an explicit experimental resource.

Final exact-source SHA-256: `27be838c09ebca86af5c2f0ec29e6b06a772bd63caaa2d8daa5094097d3f51b6`; exact report: `3c4e563f598c1cbdd9b70a24d2251a052e8577d286a7e0733f061c600bb35b88`; witness proof: `807d2283cc7808df8776b0b22764058fa6169b904ce4b1d845a9bab01fda1961`. Numerical replay source: `e305c5336c5754af64780e230386407fb3aed62ed8f6432af0c6d2976af43524`; replay report: `07fcf24190f6148d2825928e9379c35c9c4a85ce7d5f46e3e7052405946947d5`. Independent final pinned runs reproduced both reports byte for byte and validated every source/proof/input binding.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed all **45 mathematical verifiers and three saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete log contains all 48 commands and the final four-endpoint replay PASS. All **48** regenerated reports match their saved counterparts byte for byte. The 95 protected baseline files, frozen earlier proof bindings and nine recovery files are unchanged. The repository checker passes **1,856 local Markdown links**, **49 Python syntax checks**, source/proof/input-report provenance and the original MIT license; `git diff --check` passes. The new work uses maximum dense dimension four; the full historical suite's maximum remains 68.

The preceding baseline CI certifies only the preceding commit. Published-commit CI is checked separately after non-forced publication and reported with its actual commit. No manuscript was drafted.

## Historical checkpoint: calibration and endpoint measurement cost

The published baseline `c05f2b099e815146646f2c4df8e16f8f0cbe6a04`, tree `2c1f3cdad1f15b9ed3832b09148c8b93448378dd`, had forty-three mathematical verifiers, two saved-model replays and successful [CI run 35941179639](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35941179639). This continuation preserves all **93** protected baseline verifier/report/license/dependency/workflow files, earlier proof bindings and nine recovery files.

The [calibration proof](FAMILIAR_SWITCH_CALIBRATION.md) derives a generalized nine-variable polynomial and an approximate-Gibbs residual bound for all ordinary rivals with at most three states. It retains singular cases and uncapped rates. An exact local box excludes the full allowed residual band at nominal occupation error $1/2500$, baseline/tilt-parameter uncertainty $10^{-4}$ and high-field stationary-law TV error $10^{-5}$. The physical transfer gives actual occupation gap $>3/10000$ under simultaneous preparation, fixed field and common-tick errors $10^{-5}$. Extending the positive three-state predictor to slightly negative low fields gives both minima on $10^{-5}\le\delta_P\le3/10000$.

The [measurement-cost proof](FAMILIAR_SWITCH_MEASUREMENT_COST.md) gives a fixed-sample confidence-box test and separate validity/power guarantees. At both error probabilities 5%, sufficient equal-allocation totals are 315,548,219 ideal endpoints, 876,522,829 calibrated endpoints for exact-null rejection, and 1,972,176,367 to exclude models at occupation-error allowance $10^{-4}$. The separate adaptive lower is $\mathbb E N\ge270000\log19\approx794998.52$ in the ideal seven-endpoint experiment, hence at least 794,999 for fixed integer budgets. The upper and lower are not matched. A 62-unit target reset does not guarantee preparation of every arbitrarily slow rival, and statistical independence is not inferred from waiting.

The [new exact verifier](../scripts/verify_switch_calibration.py) and [report](../reports/switch_calibration.json) provide **112 exact checks**, maximum dense dimension **3**. They validate the frozen helper and target report, check the generalized polynomial, enclose both residual bands, certify positive three-state rates, and verify physical error budgets, reset and sampling constants by rational exponential/logarithm bounds. The local box is an essential computer-assisted premise. The all-rival identity, perturbation and statistical arguments remain analytic. No fitting, floating proof arithmetic or large simulation is used. The inherited target certificate used dimension four; the full historical suite's maximum remains 68.

The final source SHA-256 is `64ed3efabee62971b3ecb4d4a932fb337e1af887ccab2a07bfb5e3e0a7fae9b2`; report: `d9e836b41890dcc0e914dcc344bd00ab27d7cd31643f7bf0f596991140feaba9`. It binds the calibration proof `ac1bf6738eb176b6ac112e5126d417554ebeec4263ab16a34c4da8a7efac537b`, measurement-cost proof `e5ea44b5dfebc74b6071fc1f2faa302dae47ff52fac67745b4022ccab3d02317`, both earlier switch proofs, imported arithmetic helper and frozen target report. The repository checker now validates inherited-report hashes as well as source and proof hashes.

The complete source and proofs received root and separate reviews; an independent pinned Python 3.13.5 final run passed all 112 checks and reproduced the canonical report byte for byte. The [internal review](FAMILIAR_SWITCH_CALIBRATION_INTERNAL_REVIEW.md) distinguishes analytic, numerical and statistical evidence. The [source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md) records inspected primary concentration, adaptive-testing and Markov-perturbation sources without certifying novelty.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed all **44 mathematical verifiers and two saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Completion was checked against all 46 commands and the final replay PASS, not just a shell exit code. All **46** regenerated reports match their saved counterparts byte for byte. The 93 protected baseline files, earlier proof bindings and nine recovery files are unchanged. The repository checker passes **1,795 local Markdown links**, **47 Python syntax checks**, saved source/proof/input-report provenance and the original MIT license; `git diff --check` passes.

The published baseline CI above certifies only the preceding commit. The exact non-forced publication commit receives its own live CI check, reported separately after publication. No manuscript was drafted.

## Historical checkpoint: seven-experiment finite margin

The published baseline `ed66b72eb2e1ddf6a6e9a0397cbdb5304139f335`, tree `ffcc9ba636ac6dc72e9ae03c5ccf558008fe94a1`, had forty-two mathematical verifiers, one saved-model replay and successful [CI run 35887218370](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35887218370). This continuation preserves all **89** protected baseline verifier/report/license/dependency/workflow files, earlier proof bindings and nine recovery files.

The [new proof](FAMILIAR_SWITCH_FINITE_MARGIN.md) derives two quartic polynomials in seven endpoint means. At least one vanishes in every ordinary-reversible rival with at most three states. The necessity includes singular response tables, arbitrarily fast rates, and even reversible discrete-time kernels that do not embed in continuous time. The coupled target violates both; an analytic coefficient bound gives a positive occupation-error lower $\Delta/(2L)$ at every positive coupling, field and clock.

The [new verifier](../scripts/verify_familiar_switch_margin.py) and [canonical report](../reports/familiar_switch_margin.json) provide **103 exact checks**, with maximum dense dimension **4**. At $J=H=\log3$, clock two, rational Taylor enclosures and exact polynomial translation exclude the entire seven-mean error box corresponding to occupation error $1/2000$. This finite arithmetic is an essential premise of the explicit numerical threshold. The same verifier proves a fixed rational ordinary three-state upper below $837/10^6<1/1000$ on the identical seven-word menu. The upper is not an eleven-word or all-protocol guarantee; neither bound is an optimizer result.

The proof and full source received root and separate reviews. A separately coded three-dimensional rational exponential enclosure independently confirms the lower; a final pinned Python 3.13.5 rerun reproduced the canonical report byte for byte. Source SHA-256: `e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397`; report: `dfe9757f74a6fc2d45f239e65292cfc613f913685f895896a9b229cc16067141`; new proof: `77b63640f035c550597df82f70d3912519d643a84f6b39fda315529f14bfdf02`. The report also binds the unchanged structure proof.

The separate [numerical script](../scripts/screen_short_switch_witnesses.py) and [saved diagnostic](../reports/short_switch_witness_screen.json) retain four bounded target panels, eight fitted rivals and one rounded rational model. Full generators, stationary laws, explicit words and endpoint predictions are saved. Default/CI replay performs no fitting. Exact schema and provenance checks are combined with numeric tolerance $2\times10^{-11}$; environment versions are informational. Independent complete source review and pinned replay passed. Source SHA-256: `9f87b7fdbb87e125dc2fb207ded1e19a98b8892400905a568f8f952950bd9e27`; report: `3081d9a2a2c2175a0e9fa5173f810e3bbf15b3af1f2751f160f2faea1895236c`. Both frozen proof notes and the old helper source are bound. Fits are achieved numerical uppers, not global optima or lower certificates.

The [internal review](FAMILIAR_SWITCH_MARGIN_INTERNAL_REVIEW.md) distinguishes analytic proof, essential exact finite certification and numerical diagnostics. The [source audit](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) records primary full-text comparisons and bounded priority scope. The margin is 0.05 percentage points in occupancy, with a same-menu ordinary-three-state upper below 0.1 percentage points; calibration robustness and sample costs remain open. No manuscript was drafted.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed all **43 mathematical verifiers and two saved-model replays** under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. The complete log contains all 45 commands and the final replay PASS; all **45** regenerated reports match their saved counterparts byte for byte. An earlier truncated execution log was not accepted as completion. All 89 protected baseline files and nine recovery files match their preserved hashes/archive. The repository checker passes **1,717 local Markdown links**, **46 Python syntax checks**, source/proof provenance and the unchanged MIT license; `git diff --check` passes. The historical suite's maximum dense dimension remains 68; the new work uses at most four.

The published baseline CI above certifies only the preceding commit. The exact non-forced publication commit receives a separate live CI check, whose result is reported after publication rather than inferred from this local PASS.

## Historical checkpoint: familiar coupled switches

The published baseline `f1a7872fec92353314a06d6f6bd12b79013e79d2`, tree `326d592b4ee47627576a04feb62f3355a3a43c21`, had forty-one verifiers and successful [CI run 35864902730](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35864902730). This continuation preserves all **85** baseline verifier/report/license/dependency/workflow files, all earlier proof bindings, and all nine recovery files.

The [new theorem](FAMILIAR_SWITCH_STRUCTURE.md) analytically proves three stationary predictive states versus four ordinarily reversible states for every finite positive coupling and field in the specified shared-Gibbs-tilt two-switch task. Eleven words of at most five ticks and three segments suffice at every fixed positive clock. A positive, unquantified error margin holds on this same menu without a rival rate cap. The argument uses compact sampled propagators and principal-log continuity, not compactness of unrestricted generators. The exact positive upper works under arbitrary nonnegative field protocols; the scope is means, not complete binary path laws.

The [exact verifier](../scripts/verify_familiar_switches.py) and [report](../reports/familiar_switches.json) add **386 exact checks** at maximum dense dimension **8**. Independently constructed heat-bath rates and mean generators test two- and three-switch closure, stationary Gibbs laws, the explicit rational predictor, sixteen general-family rational fixtures, twelve positive-field derivative-Hankel determinants, conditional-moment arithmetic, passive flip hazards and zero-coupling aggregation. Exact word coverage and a formal polynomial identity check the eleven-experiment Hankel design. These checks supplement the universal proof; they compute no finite-error tolerance.

The source and final additions passed root and separate source reviews. An independent pinned Python 3.13.5 rerun reproduced the canonical report byte for byte. Exact source SHA-256: `aab92b39e8aa15df35277907f427bf2da47f7389dbe93c287dac9ec1847bde7a`; report: `e4f35d54187aa51dd80c602be218356b74e508dd823ae65c0844b833d8d4dfea`; bound proof: `de269cb3264cd972577315497d9d20ac15290ab6bdf3acc1858ce845fbfa5813`.

The [numerical script](../scripts/screen_familiar_switches.py), [protocol note](FAMILIAR_SWITCH_PROTOCOLS.md) and [saved report](../reports/familiar_switch_screen.json) form a separate diagnostic. Nineteen target panels retain 51 comparator models with full generators, stationary laws, menus and endpoint probabilities. Default verification recomputes their feasibility and responses without fitting. Schema, counts and source/proof hashes are exact; numeric replay permits absolute differences $2\times10^{-11}$ and treats environment versions as informational. Root and a separate reviewer read the complete numerical source and protocol note; an independent replay regenerated the report byte for byte. The pinned local report also regenerated byte for byte. The optional optimizer is excluded from the gate. Achieved finite-menu errors are numerical uppers, not certified global lower bounds or all-protocol guarantees.

The numerical source SHA-256 is `13d3abcdbaa0730c18540c56b35c4d0e06c8e14dd110cf856cf0c4459af93b6d`; report: `c1f2d48b379ff67b069ef74016e167300e3978a5f400ec2300d598b3cd10bca0`; protocol note: `ba2847e1e4ae4391044e80f50df80bfda990d083c4dd465fd58d314839f794eb`. The report also binds the theorem. The [internal review](FAMILIAR_SWITCH_INTERNAL_REVIEW.md) separates analytic audits and computation. The [source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) attributes classical ingredients, compares positive-realization tasks and leaves Falk (1983) visibly unresolved at full-text level. Neither audit certifies priority.

**Completed local gate:** `make check PYTHON=.venv/bin/python` passed all **42 mathematical verifiers plus the saved-model replay** under Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. Completion was confirmed by the full command count and the final replay PASS, not only a shell return code. All **43** fresh reports match their saved counterparts byte for byte. The 85 protected baseline files and nine recovery files match their preserved hashes/archive. The repository checker passes all 44 Python syntax checks, local Markdown links, source/proof provenance and the unchanged MIT license; `git diff --check` passes. The historical suite's maximum dense dimension remains 68; the new work uses at most eight.

The baseline CI above certifies the preceding published commit. A new remote run must be checked on the exact non-forced publication commit; its outcome is reported after publication, separately from this local evidence. No manuscript was drafted.

## Historical checkpoint: simple prediction principles

The published baseline `2923ca8c3992726593ee3111342c1e004cd4b53a`, tree `f74bcbf86f5ce25d3d0863822623ea120c0378c0`, had forty verifiers and successful [CI run 35859347383](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35859347383). This continuation adds one combined verifier while preserving all 83 baseline verifiers, saved reports, license, dependency and workflow files, all bound earlier proof snapshots, and all nine recovery files.

The [new verifier](../scripts/verify_simple_prediction_principles.py) and [report](../reports/simple_prediction_principles.json) contain **200 exact checks**, with maximum dense dimension **12**. Rational arithmetic checks a positive rank-two example with reversible and nonreversible factorizations, the general normalization and canonical stochastic maps, full controlled-generator and output-projector intertwining, matched positive features, the established incidence rank counts, centered master equations, reversible/nonreversible energy estimates, and both variance constants. No numerical fitting, trajectory simulation or large target enumeration is used.

The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) analytically proves both minimum counts for arbitrary normalized completely positive matrices with positive row sums, including the positive-error existence corollary and the exact controlled binary path-law upper. The finite verifier does not solve arbitrary matrix ranks or replace the universal proof. The [variance theorem](KINETIC_VARIANCE_COMPRESSION.md) analytically proves uniform mean bounds, including the two-state upper $557/51920$ and a conditional-variance derivation of the previous nine-state upper $1/2376$. Its common-law, preparation, invariant-partition and mean-only limitations are explicit.

The source received root and two separate full code reviews. Independent pinned Python 3.13.5 runs reproduced the saved report byte for byte. The final report binds both new proof notes and three frozen prerequisites. Source SHA-256 is `66408ebc8581fbf23910c945a1aed6cfbb2ca1a72ec55b147dc33c60cb676c02`; report SHA-256 is `e90edaf0ee18045706fb65164fe47a5e09ed4f5e03514e0eac91e0e38869f433`.

The [internal review](SIMPLE_PREDICTION_INTERNAL_REVIEW.md) records independent complete mathematical reviews separately. The [source comparison](SIMPLE_PREDICTION_SOURCE_AUDIT.md) records six primary full texts and distinguishes static factorization, generic discrete-time HMM pair realization, continuous-time Gram identities and the controlled theorem. The README has been shortened to the physical question, current results and navigation; all historical proofs and their scopes remain in the linked ledger and dossier.

The completed `make check PYTHON=.venv/bin/python` gate passed all **41** mathematical verifiers under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. All 41 fresh reports match the saved reports byte for byte. The 83 protected baseline files and all nine recovery files are unchanged. The repository checker passes 42 Python syntax checks, local Markdown links, source/proof provenance and the original MIT license; `git diff --check` passes. The full suite's historical maximum dense dimension remains 68. Remote CI must be checked on the actual published commit; the baseline run above certifies only `2923ca8`. Its new live result is reported after the authorized non-forced publication.

## Historical checkpoint: rational observation and symmetry compression

The published baseline `a60dee50b8728fb15717d9f06f3876fdf9f67b4a`, tree `41ce1198905603e5d9061060510d5066fe102a6b`, had thirty-eight verifiers and successful [CI run 35856173987](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35856173987). This continuation adds two verifiers while preserving all 79 baseline verifiers, saved reports, license, dependency and workflow files, all earlier bound proof snapshots, and all nine recovery files.

| New verifier and saved report | Evidence | Checks | Maximum dense dimension |
|---|---|---:|---:|
| [Rational observation](../scripts/verify_rational_observation.py), [report](../reports/rational_observation.json) | Essential exact certificate for the ten-function target basis, complete 12,766-word menu enumeration, rational selector identities and universal-transfer constants. | 98 | 12 |
| [Symmetry compression](../scripts/verify_symmetric_compression.py), [report](../reports/symmetric_compression.json) | Exact target/quotient and detailed-balance identities, cap/band, all 66 contraction pairs per field, odd-sector/source constants, plus bounded switched-propagator implementation diagnostics. | 283 | 12 |

The rational basis premise is computer-assisted with rigorous integer/fraction arithmetic. A dyadic matrix enclosure with explicit logarithm, Taylor and rounding errors establishes a weighted Gram lower bound $2^{-52}I$. No floating eigensolver or exponential is used as proof. The rest of the [new observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) analytically transfers finite mean agreement to positive features in every admissible reversible rival. The report binds that proof and six frozen prerequisites. Its arithmetic establishes ordinary minimum twelve at mean error $2^{-220}$, with an unrestricted sufficient count eleven. It does not extend the older unrestricted minimum to this larger tolerance.

The finite menu is completely reproducible without storing a large word list. From the repository root:

```sh
python scripts/verify_rational_observation.py --output .check-output/rational_observation.json --menu-output .check-output/rational_observation_menu.json
```

The export has 12,766 words, maximum length 66, and SHA-256 `03b25dbba22ad0f560ea023464921b71d011843bea5fce354c056d341e64a079`. Independent enumeration from the raw word grammar reproduced the entire menu and checksum. This is an explicit experiment specification, not a practical precision or sample guarantee.

The [symmetry proof](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) gives a nine-state ordinary-reversible approximation at uniform two-field error $1/2376$. Its all-protocol bound is analytic. The verifier's seven deterministic protocol samples, at most 64 segments, and three amplitude comparisons check the implementation only; they neither optimize over rivals nor establish the uniform theorem. The separate all-field bound permits arithmetic averages of barrier curves and is distinguished from the exponential endpoint implementation.

Both programs received independent full source reviews and pinned Python 3.13.5 reruns with byte-identical reports. The symmetry report schema was aligned with the repository's `source_sha256` and `proof_snapshot_sha256` provenance fields before the full gate; the mathematical assertions were unchanged. Final source and report digests are:

| Verifier | Source SHA-256 | Report SHA-256 |
|---|---|---|
| Rational observation | `ce9e33d7bba0c863b809cde813db91f3f968a1702e2e6952d3e9c2010c26ad0c` | `e708e1b6fd53ef3995fd9f1089f0ec635833234b6f6c08b57c172a246f7c2d43` |
| Symmetry compression | `e91d00de4654e6ca89e05de29dfb5593cb7f214dc93515ee7ecdd05abd8aecad` | `40cab5d956e15ba3f4ae5592262757b40bafd5c75065c9c4f0d6b555255c03ad` |

The [internal review](RATIONAL_OBSERVATION_INTERNAL_REVIEW.md) records independent mathematical review separately from code checks. The [source comparison](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) records six inspected primary full texts and one passage-level source, with explicit access and novelty limits. The fixed matrix and general realization, functional-calculus and response ingredients remain attributed to prior work.

The completed `make check PYTHON=.venv/bin/python` gate passed all **40** mathematical verifiers under pinned Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. All forty fresh reports match the saved reports byte for byte. The 79 protected baseline files and all nine recovery files are unchanged. The repository checker passes 41 Python syntax checks, local Markdown links, source/proof provenance and the original MIT license; `git diff --check` passes. The full suite's historical maximum dense dimension remains 68. Remote CI belongs to the published commit and must be checked separately. The baseline run above certifies only `a60dee5`; the new live result is reported after non-forced publication.

## Historical checkpoint: finite minimality and improved precision

The published baseline `720962175fc76e2062e7f2aa4deb1938ba111c77`, tree `e9e51a49936be496f39a3384a8053ee26280eb4c`, had thirty-seven verifiers and successful [CI run 35853478678](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35853478678). This continuation adds one verifier while preserving all 77 baseline verifiers, saved reports, license, dependency and workflow files.

The [finite-minimality verifier](../scripts/verify_finite_minimality.py) and [saved report](../reports/finite_minimality.json) contain **3272 exact checks**, with maximum dense dimension **11**. They enumerate the 18 maximal positive rectangles of the five-by-five support and all 3060 four-rectangle candidates, reconstruct the explicit predictor's positive left/right factorization, distinguish formal reversal from its actual Gram, check the stronger Schur obstruction and centered-log budget, and verify selector and reinjection identities. All arithmetic uses rational fractions and integers; no optimizer, large target or controlled protocol enumeration is used. The source received both root and separate full code reviews. An independent pinned Python 3.13.5 run reproduced the canonical report byte for byte. Source SHA-256 is `f68d0d6e8d944b389ded95015f963bbef39e3bf188ac339c19d2a1e6c58843c7`; report SHA-256 is `c6f2c58959eb8546f5d07670ea57286ec89868cffd39828cf1593b556c7f1b28`.

The report binds the [minimum-count theorem](FINITE_PREDICTOR_MINIMALITY.md), [Gram refinement](FINITE_GRAM_ROBUSTNESS.md) and [observation boundary](FINITE_OBSERVATION_BOTTLENECK.md). The [internal review](FINITE_PRECISION_INTERNAL_REVIEW.md) records analytic audits separately from these finite checks. The [source supplement](FINITE_PRECISION_SOURCE_AUDIT.md) attributes the exact core matrix to prior work. The finite ordinary-EPR corollary is an analytic parameter substitution into the preserved earlier bound, not a new numerical fixture.

The controlled-mean certificate is $2^{-1360}$ with at most 520 ticks. The matrix tolerance $1/1500$ concerns an intermediate Gram only. Bounded rational selectors have no observation-recovery bound in this checkpoint, and the selective-gate example is not a new target satisfying the hard hidden band. These limitations are explicit in the notes and report.

The completed `make check PYTHON=.venv/bin/python` gate passed all **38** mathematical verifiers under the pinned Python 3.13.5 environment (NumPy 2.3.5 and SciPy 1.17.0 for earlier numerical verifiers). All 38 regenerated reports are byte-identical to the saved reports. The 77 protected baseline files and all nine recovery files are unchanged. Local documentation links, 39 Python syntax checks, saved source/proof hashes and the MIT license pass the repository checker; `git diff --check` passes. The full suite's historical maximum dense dimension remains 68.

Remote CI belongs to the published commit and must be checked separately. The baseline run above certifies only `7209621`; publication and the new run's live result are reported after the non-forced branch update.

## Historical checkpoint: finite advantage and physical robustness

The published baseline `c6b81946e6e16145a52862b7c96a3986d1d23a69` had thirty-five verifiers and successful [CI run 35847878583](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35847878583). This continuation adds two mathematical verifiers without modifying any earlier verifier or saved report.

| New verifier and saved report | Bounded evidence | Maximum dense dimension |
|---|---|---:|
| [Finite advantage](../scripts/verify_finite_advantage.py), [report](../reports/finite_advantage.json) | 259 checks: exact target/predictor generators, stationary preparation/readout, all-control intertwining identities, rational spectral-band certificates, positive feature Gram and eleven-atom obstruction, explicit total-degree clock budget, and finite-EPR regularization. | 12 |
| [Physical robustness](../scripts/verify_physical_robustness.py), [report](../reports/physical_robustness.json) | 104 checks: Bell–Arrhenius reconstruction, common-return lumpability, barrier-only stationarity, row-defect normalization, switched Duhamel identity, reset/weighted/ramp bounds, and even Markov-projection fixtures. | 6 |

The finite verifier binds the frozen [finite theorem](FINITE_REVERSIBILITY_ADVANTAGE.md). Its $2^{-3000}$ arithmetic is rational/symbolic; the program does not enumerate the enormous finite protocol menu or represent that tolerance in ordinary floating point. The physical verifier binds the [robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md), [single-force](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) and [reversal-closure](PHYSICAL_REVERSAL_REALIZATION.md) snapshots. Both source programs received separate full code reviews and independent pinned reruns with byte-identical reports. The [finite proof review](FINITE_ADVANTAGE_INTERNAL_REVIEW.md) and [physical proof review](PHYSICAL_MODEL_INTERNAL_REVIEW.md) record analytic review separately.

The completed local `make check PYTHON=.venv/bin/python` gate passed all **37** mathematical verifiers under Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. All 37 fresh reports match their saved bytes. The 73 protected baseline files (35 verifiers, 35 reports, license, requirements and workflow) are unchanged, as are all nine recovery files relative to archive commit `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`. The repository checker passes 38 Python syntax checks, local documentation links and saved source/proof hashes; `git diff --check` passes. The full suite's earlier maximum dense dimension remains 68.

Remote CI belongs to the actual published commit and must be checked separately from this local result. The preceding run linked above certifies the baseline only. The new checkpoint's workflow is triggered by its non-forced publication; its live result and exact commit are reported after that publication.

## Original checkpoint

[verify_checkpoint.py](../scripts/verify_checkpoint.py) is byte-for-byte the verifier from the supplied analytical checkpoint; only its repository filename changed. Its SHA-256 is:

```text
ce7a2a981e6a09f7350ad42731afbcafd6c67f2de2bade8d2de16666227e2026
```

All six entries in the supplied checkpoint's checksum manifest were verified before import. The source archive SHA-256 is:

```text
7ee27fc1e6b1c6217c9649374ae01f05edbd1ba61e35e31749925b14b3e99abe
```

The active theory and audit documents reorganize that checkpoint and add the finite-accuracy extension; they are not claimed to be byte-identical originals. The source fiction and conversational material are not repository contents.

The locally rerun [checkpoint report](../reports/checkpoint.json) records exact symbolic checks of generator row sums, detailed balance, stationarity, passive lumpability, three rational-rate Laplace calculations, and the three-state kernel inverse. Independent computational formulations within the script compare a block master equation with spectral and memory formulas.

| Metric | Saved local result |
|---|---:|
| Matrix/spectral comparisons | 56 |
| Largest augmented matrix | 36 by 36 |
| Maximum matrix/spectral discrepancy | about 2.05e-15 |
| Maximum time-dependent protocol discrepancy | about 1.35e-14 |

The original finite-field check is consistent with a fourth-order truncation remainder; that computation alone is not a proof of a uniform remainder. The later finite-field checkpoint below adds the analytic proof and separate checks.

## Finite-accuracy extension

[verify_finite_accuracy.py](../scripts/verify_finite_accuracy.py) checks the bounded-sensitivity path construction against numerical eigendecomposition for 23 models, including both parity cases. It verifies the closed-form positive weights, mass lower bound, and nonvanishing step correction.

For deterministic spectra spanning rates from 0.005k to 40k, it then checks midpoint quantization at four grid sizes, the exact mass-preserving certificate, and the paired-state reversible realization. The complete Markov Taylor equation is compared with the reduced memory equation under a five-segment sign-changing/on-off protocol. Zero mass and invalid inputs are also tested.

The saved [extension report](../reports/finite_accuracy.json) records:

| Metric | Saved local result |
|---|---:|
| Normalized-family models | 23 |
| Maximum spectral-weight discrepancy | about 1.55e-15 |
| Proved cubic-correction lower bound at kt=1/4 | 0.0275894 |
| Smallest sampled correction | 0.0313331 |
| Compression/realization cases | 12 |
| Protocol sample comparisons | 240 |
| Maximum observed error / transport certificate | about 0.0726 |
| Maximum realized-kernel discrepancy | about 3.37e-15 |
| Maximum full-Markov / memory discrepancy | about 1.23e-15 |
| Largest matrix | 68 by 68 |

The protocol samples are consistency tests. The guarantee for every bounded protocol comes from the inequality in the proof, not from extrapolating these samples.

Both runs used Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and, for symbolic checks, SymPy 1.14.0. The extension report records SHA-256 hashes of both calculation scripts. `check_repository.py` detects a mismatch between those source files and the saved report.

## Takeover verification

The takeover started from clean `main` at `80dc6098613b6561428d017b4a41553607fde67b`. Its original `make check` passed again under Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and SymPy 1.14.0 before the extensions were added. The existing saved baseline reports and both existing mathematical verifiers were retained unchanged.

### Positive-quadrature extension

[verify_quadrature.py](../scripts/verify_quadrature.py) implements tapered Gaussian quadrature in normalized dyadic bins, with a separate high-rate tail atom. It uses fully reorthogonalized discrete Lanczos calculations and positive Gaussian weights. The saved [quadrature report](../reports/quadrature.json) contains 24 bin checks, moments through degree $2d-1$, 192 sampled kernel-sign comparisons, and exact `Fraction` arithmetic checks of the reciprocal-rate integral identity at orders 1–3. The component integral errors are summed as a triangle certificate; they are not mislabeled as the exact absolute error of a mixture whose bin and tail errors can have opposite signs.

The response checks use 162 samples from constant, sign-changing, zero/restart, and larger bounded protocols, including three values of $k$. A selected compressed kernel is also passed through the original paired Markov realization and compared with the full master-equation coefficient hierarchy. Boundary cases cover repeated atoms, exact small support, dyadic endpoints, empty/zero mass, tail-only support, and invalid input.

### Minimal reversible realization

[verify_minimal_realization.py](../scripts/verify_minimal_realization.py) constructs the finite Jacobi matrix from the augmented spectral measure, then uses its positive null vector to form a reversible birth–death generator. The saved [realization report](../reports/minimal_realization.json) checks six spectra, including nonuniform weights, repeated rates, zero-weight atoms, and collisions at $\lambda=k$. It verifies the spectral measure, positive neighboring rates, row sums, detailed balance, endpoint mass $1/2$, and the pointwise sensitivity bound. Twenty-four full-Markov/memory protocol comparisons check the reconstructed response.

| New check | Saved local result |
|---|---:|
| Maximum normalized quadrature moment error | 3.00e-16 |
| Quadrature full-Markov/memory cubic discrepancy | 1.53e-16 |
| Minimal-realization kernel discrepancy | 3.43e-15 |
| Minimal-realization full-Markov/memory discrepancy | 4.02e-16 |
| Largest matrix across all four verifiers | 68 by 68 |

All new saved reports were generated in the same pinned Python 3.13.5 environment and contain calculation-source hashes. These are small floating-point consistency checks plus selected exact rational identities. They do not certify numerical conditioning for arbitrarily clustered spectra or arbitrarily small requested tolerances. The general approximation bounds and generic exact minimality come from the written proofs, not sample extrapolation. In particular, a collision test does not prove the minimal state count at a collision.

The complete extended `make check` passed locally in this environment. All four fresh reports matched their saved JSON reports exactly. The final repository checks also passed; this local record does not assert a GitHub Actions outcome.

## Response lower-bound checkpoint

This continuation starts from `78004603026a8058983e471f0bad73b2310abc12`. All four earlier mathematical verifiers and their saved reports remain unchanged. The new [response lower-bound verifier](../scripts/verify_response_lower_bounds.py) generates [response_lower_bounds.json](../reports/response_lower_bounds.json), using Python 3.13.5, SymPy 1.14.0, and explicitly pinned mpmath 1.3.0.

The two-state checks expand the general analytic rate factor symbolically and independently expand the exact finite-field step solution. Exact algebra verifies the two-sample dual statistic and the equal-and-opposite errors of its minimizer. It does not optimize the all-protocol norm.

For state budgets $D=2,3,4$, the verifier checks rational Vandermonde inverses, Lagrange coefficient identities, the filter-to-positive-moment identity, and the conservative lower bound. The smallest Hankel eigenvalues are computed at 100 and 150 decimal digits; agreement is a numerical consistency check, not interval certification. Those eigenvalues are not substitutes for the general analytic bound. Their small values also illustrate that these conservative witnesses do not make every hidden mode practically observable.

Three surrogate examples check the exact full-to-reduced coefficient-hierarchy intertwining and characteristic-polynomial divisibility. They include a nonreversible four-state model with a defective hidden generator and sensitivity coupled to its Jordan part. High-precision propagation tests the filtered recurrences without inferring rank from a floating-point threshold. A separate complex-contour calculation extracts the cubic coefficient from the exact analytic generator as a cross-check of the hierarchy.

The new verifier's largest matrix is $16\times16$; the largest across the complete suite remains $68\times68$. The theorem covers all allowed models through the proof, not enumeration. The rate-capped upper bound reuses the proved quadrature and realization results; no new approximation algorithm is asserted. Finite-field remainder control and noisy coefficient acquisition remain outside the verification scope.

The complete five-verifier `make check` passed locally in the pinned environment. All five fresh reports matched their saved JSON reports exactly. The original license, four earlier verifiers, and their reports were also checked against the starting commit and remain unchanged. This records the local result; GitHub Actions is checked separately after publication.

## Unrestricted-rate matching-order checkpoint

This continuation starts from `57c0e12bdde4d8a38dc355d6797126debd7a6e76`. All five earlier mathematical verifiers and their saved reports remain unchanged. The new [unrestricted-rate verifier](../scripts/verify_unrestricted_rate_lower_bound.py) generates [unrestricted_rate_lower_bound.json](../reports/unrestricted_rate_lower_bound.json) in the same pinned environment.

Exact rational calculations check four geometric Cauchy matrices, their inverse-diagonal product formulas, and positive principal minors. Symbolic algebra checks the general-rate cubic-step decomposition into three visible exponential-polynomial terms and a negative hidden exponential. It also checks the positive-series identity giving the integral of `log(coth(x/2))` as `pi^2/4`.

For $D=2,3,4$, the verifier constructs the theorem's $r=8,11,14$ mode witnesses at 100 and 150 decimal digits. It checks the inverse-trace estimate, weight floor, optimized bound, and finite-horizon truncation estimate against computed eigenvalues. Precision agreement is a consistency check, not interval certification; the conservative bound is proved analytically for all $D$. These calculations neither optimize the minimax problem nor discretize the operator to infer its rank.

As a separate check of the response-to-Hankel construction, a three-state analytic master equation supplies a $12\times12$ coefficient hierarchy. Thirty-six probability-weighted double-integral moments, evaluated through exact resolvents, agree with the explicit baseline-minus-positive-kernel formula. This connects the operator identities to the Markov response without estimating the continuous operator's spectrum numerically.

The new verifier's largest matrix is $14\times14$; the complete suite's largest matrix remains $68\times68$. The finite-horizon theorem concerns an entire coefficient curve, not a finite sampling protocol, temporal-resolution guarantee, or noisy measurement procedure. The earlier verifier retains the finite-sample and nonreversible Jordan-block checks.

The complete six-verifier `make check` passed locally in the pinned environment. All six fresh reports matched their saved JSON reports exactly. The original license, five earlier verifiers, and their reports were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Publication-scope and structure-cost checkpoint

This continuation starts from `9cf4e64ca27624ee66bb75d93ba7fd215135ac43`. It adds the [publication comparison](PUBLICATION_SCOPE.md) and [structure-cost corollary](STRUCTURE_COST.md). All six mathematical verifiers, their saved reports, and the MIT license remain unchanged.

The corollary uses the existing lower and upper proofs. The unrestricted lower proof already applies to stationary analytic Markov surrogates with a fixed arbitrary readout. In the capped case, filtering preserves the coefficient-lift rank even without passive matching; the mode count becomes $3D-1$, and the same Vandermonde and filter estimates apply. No new approximation algorithm or computed minimax optimum is introduced.

The switch-off formula follows exactly from the zero-field readout eigenrelation, and the two three-state field-on coefficients follow by substitution in the existing step formula. The public note includes their derivation and precise scope. These are analytic corollaries; no additional simulation or statistical test is used to support them. The source comparisons are literature assessments, not mathematical verification by the programs.

The complete six-verifier `make check` passed locally in the pinned environment. All six fresh reports matched their saved JSON reports exactly. The license, all verification scripts and reports, pinned dependencies, build target, and workflow were checked against the starting commit and remain unchanged. Final repository checks passed. GitHub Actions is checked separately after publication.

## Finite-field prediction and path-information checkpoint

This continuation starts from `ef1448235c1fcf70e2c5fdca7d544f87591e9052`. It retains the six earlier mathematical verifiers and saved reports unchanged. The build target and repository checker are extended to include two new verifiers; the MIT license and dependency versions remain unchanged.

[verify_finite_field.py](../scripts/verify_finite_field.py) produces [finite_field.json](../reports/finite_field.json). An exact rational recursion checks the coefficient bounds underlying the uniform fourth-order remainder. Thirty-three deterministic finite-field protocol comparisons, including fields of magnitude 1.2, compare full physical master equations with the independent scalar-kernel modal closure. A genuinely smaller quadrature model is compared with the original under a sign-changing protocol and its weighted-integral certificate. Small weak-field examples check the remainder bound without inferring uniformity from the samples.

Two geometric-spectrum witnesses compare the full symmetrized field generator with the diagonal-plus-rank-one formula, its positive spectral step curve, the secular eigenvalue enclosures, the visible-weight floor, and logarithmic Gram spacing. An exact symbolic four-state calculation holds the actuator and cubic kernel fixed while showing different higher response, checking the stated boundary of the finite-field subclass. The largest new matrix is $40\times40$; the suite maximum remains $68\times68$.

[verify_path_information.py](../scripts/verify_path_information.py) produces [path_information.json](../reports/path_information.json). Exact resolvents check active no-exit coefficients for three examples, including a two-mode hidden kernel. Telegraph pair intensities check normalization of the full quadratic path score. A separate full-generator calculation checks the two-snapshot identity and its signal coefficient. Exact algebra also checks complete and residual waiting densities, normalization and mean duration, the hyperbolic density formula, a censored-relative-entropy identity, and the integral $8/105$ giving the three-state relative-entropy rate coefficient $2/105$. Twelve high-precision deterministic density comparisons provide a further consistency check.

Neither verifier simulates statistical trials or certifies inference performance from sampled data. The testing rates, all-size/all-horizon error bounds, and fixed-field minimax lower bound follow from the written proofs. Spectral consistency tests do not infer rank from numerical thresholds. The calculations and proof audits belong to this investigation and are not independent external validation.

The complete eight-verifier `make check` passed locally in the pinned environment. All eight fresh reports matched their saved JSON reports exactly. The six earlier mathematical scripts and reports, original license, dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## General actuator information and compression checkpoint

This continuation starts from `1f7f747a64442e15eab929c08e19d3958c9f4828`. It retains all eight earlier mathematical verifiers and saved reports unchanged. Two new verifiers cover the broader actuator results; the build target and provenance checker include both.

[verify_actuator_hierarchy.py](../scripts/verify_actuator_hierarchy.py) produces [actuator_hierarchy.json](../reports/actuator_hierarchy.json). Exact rational constructions at $d=2,3,4$ share $G=1$, $W=1/2$ and the full actuator within each pair. It checks positive reversible generators, common stationary laws, orthogonal projectors, and the identical one-mode covariance. Graded reachable spaces closed under the zero-field generator check every response word through the specified orders, without choosing protocol or time samples. Adding the visible observation projector checks finite visible observation words as well. The resulting mean first differences occur at orders $5,7,9$; their leading $t^3$ coefficients are respectively $1/96$, $1/3456$, and $1/1382400$.

Independent full-generator powers verify the exact finite-field third-time-derivative identities for both the mean and no-exit survival. A separate binary-actuator example checks identical complete hidden spectra and two-time kernels, equality of the first four time derivatives of the mean, and the exact fifth derivative difference. Its largest full generator has six states; the largest comparison matrix has dimension twelve. These finite cases support the all-$d$ proof but do not replace it.

[verify_general_compression.py](../scripts/verify_general_compression.py) produces [general_compression.json](../reports/general_compression.json). A four-state product chain gives an exact rational transition matrix and a nine-state order-two symbol-word realization. Thirty-nine symbol blocks of lengths one through three match exactly; a length-four witness differs, so the example does not accidentally reduce to an exact symbol Markov chain. Exact algebra checks the conditional-mean quantization variance loss $1/32$, word stationarity, nonreversibility, the physical surrogate's full finite-field equilibrium, and its passive readout eigenrelation. The largest matrix has dimension ten.

Thirty scalar spectral samples, fifteen semigroup comparisons, and nine deterministic bounded-protocol comparisons check the internal-rate regularization estimates. These are consistency checks, not proofs of the all-rate or all-protocol inequalities. The explicit state-count bound is proved analytically; the script does not attempt to instantiate its potentially enormous worst-case word model. Across the complete suite the largest matrix remains $68\times68$.

The three new theorem documents received reciprocal internal proof audits. These audits, exact identities, and deterministic computations belong to this investigation; they are not external validation, a learning algorithm, or evidence of publication originality. Neither new verifier simulates trajectories or estimates statistical sample complexity. The exact path-equivalence proof uses short-pulse limits analytically and does not claim a numerically stable implementation of those limits.

The complete ten-verifier `make check` passed locally in the pinned environment. All ten fresh reports matched their saved JSON reports exactly. The eight preceding mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## General complexity separation and reversible compression checkpoint

This continuation starts from `1d5928589506cd54440896bb545863f78fa9dd6e`. All ten preceding mathematical verifiers and saved reports are preserved. Two new verifiers check the controlled lower construction and reversible compression; the build target and provenance checker include both.

[verify_general_controlled_lower_bound.py](../scripts/verify_general_controlled_lower_bound.py) generates [general_controlled_lower_bound.json](../reports/general_controlled_lower_bound.json). Exact calculations at tree depths $n=1,2,3$ check the physical Haar change of basis, positive reversible generators, binary sensitivity, fixed internal rate band, and the leaf identity that proves the ideal Gram lower bound. Exact radial invariant subspaces and spectral moments check the stated cubic kernel. Full physical-generator identities independently check the polynomial filters and both mean-response endpoints, including their normalization and formal reversed words.

For these targets, rational norm arithmetic certifies the perturbation after substituting fixed-duration propagator logarithm polynomials. The field is $h=\log(65/64)$, the minimum segment duration is $1/8$, and the polynomial degrees are $280,320,360$. The corresponding certified matrix errors are approximately $5.18\times10^{-69}$, $1.78\times10^{-73}$, and $4.58\times10^{-78}$, each below $1/32$. Separate calculations at 100 and 150 decimal digits evaluate the factorized mean statistics using actual propagators. These are consistency checks, not interval certification or numerical rank tests. The rival rank factorization and the all-$n$ state lower bound are analytic; no search over competitors or statistical trials is performed. The largest new physical generator is $17\times17$, and the largest controlled matrix is $8\times8$.

[verify_reversible_compression.py](../scripts/verify_reversible_compression.py) generates [reversible_compression.json](../reports/reversible_compression.json). An eight-hidden-state reversible product chain gives a nontrivial four-cell predictive partition, with exact projection defect $5/72$ and three-symbol total variation $7/1728$. Rational identities verify the profile error bounds, stationary-flux quotient, detailed balance, and at-most-two-point moment restoration. The resulting six-hidden-state chain preserves $W=15/32$ and $G=1$ exactly. Symbolic full-field checks verify stationarity, detailed balance, passive lumpability, and the exact lifting of the cell model before the restored sensitivities are applied.

Three deterministic protocols with seven checkpoints compare six intermediate and final models. The maximum original-to-final mean discrepancy is about $6.17\times10^{-5}$, and the maximum baseline lifting discrepancy is about $2.22\times10^{-16}$. These selected comparisons do not prove uniform protocol accuracy or instantiate the worst-case partition size. The improved double-exponential upper count follows from the written controlled-expansion argument. The largest matrix across the complete suite remains $68\times68$.

The new proofs received reciprocal internal audits covering physical positivity, error norms, state counts, competitor scope, and the fixed-dwell conversion. Such audits and calculations belong to the same investigation and are not independent external validation or publication novelty certification. The signed statistics in the lower proof may be poorly conditioned for data acquisition, and neither new theorem provides an efficient learning algorithm.

The complete twelve-verifier `make check` passed locally in the pinned environment. All twelve fresh reports matched their saved JSON reports exactly. The ten earlier mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Bounded-rate polynomial upper and shift-register lower checkpoint

This continuation starts from `04666225de07d520555144d26dee342097afb6bd`. All twelve preceding mathematical scripts and saved reports remain regression baselines. Two new verifiers are added to the build and provenance checks.

[verify_bounded_rate_prediction.py](../scripts/verify_bounded_rate_prediction.py) produces [bounded_rate_prediction.json](../reports/bounded_rate_prediction.json). Exact rational examples check a nonlumpable eight-state binary target and a sparse three-state ternary target. They verify the spectral-cap uniformization bound, allowed-word irreducibility and stationarity, exact actuator histograms, and 89 prefix probabilities with their field-entry tilts. A longer-prefix discrepancy confirms that the word approximation is not accidentally exact. Full-field symbolic identities check equilibrium, passive lumpability and the stated reversibility status.

A nontrivial eight-to-four-state predictive quotient checks exact stationary-flux aggregation, inherited lower and upper spectral bounds, and a nonzero three-symbol total-variation discrepancy of `7/1728`. Eight symbolic Poisson/Gamma clock calculations support the regenerative constants. Sixteen rational rounding cases include exact equality boundaries; a separate exact budget checks the reversible prefix approximation. The uniform coupling and all-size polynomial count are proved analytically, not inferred from these cases.

[verify_shift_register_lower_bound.py](../scripts/verify_shift_register_lower_bound.py) produces [shift_register_lower_bound.json](../reports/shift_register_lower_bound.json). Exact one-, two-, and three-bit physical generators check positive rates, Walsh translation and binary toggle actions, full-field equilibrium and detailed balance, and the filtered mean endpoints. For word depths `n=1,2,3`, sparse Walsh polynomials verify the unique maximal-index leaf and an exact sum-of-squares Gram remainder. The largest sparse union has 499 Walsh coordinates; the exponentially larger physical state spaces are not enumerated. The largest physical generator is nine-dimensional and the largest controlled Gram matrix is eight-dimensional.

Exact degree-one through degree-four interpolation formulas reproduce polynomial derivatives and check coefficient bounds for both endpoint and outside-interval stencils. Rational Taylor and filter-perturbation budgets verify that the substituted mean matrix retains at least half the exact Gram floor for the displayed finite choices in both timing regimes. Selected 100-digit calculations check higher-degree stencils against the analytic target remainder. These computations do not use numerical rank, search over competitors, or infer an all-depth exponent from a plot. The written proofs establish the unrestricted-timing and fixed-minimum-dwell lower bounds separately.

Both theorem documents received reciprocal internal mathematical audits, including normalization, physical positivity, competitor scope, regeneration, interpolation and asymptotic inversion. The older tree's all-protocol truncation estimate is an analytic obstruction showing why changing only its measurement filters cannot produce a depth-exponential error floor at the same state threshold. Neither this obstruction nor the new lower theorem claims sample-efficient acquisition of the signed mean statistics. Classical de Bruijn spectra and interpolation are attributed in the [prior-art comparison](PRIOR_ART.md); no external validation or novelty certification follows from these checks.

The complete fourteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All fourteen fresh JSON reports matched their saved reports exactly. The twelve earlier mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. The suite's largest matrix remains $68\times68$. GitHub Actions is checked separately after publication.

## Polynomial necessity with a fixed switching clock

This continuation starts from `b143adad62c8ec0d8b51733760d5c1c82bcaa213`. The fourteen earlier mathematical verifiers and saved reports are preserved. The new proof reuses the positive shift-register target and exact leaf Gram bound, with total-degree logarithm truncation replacing the earlier per-generator interpolation step.

[verify_polynomial_controlled_lower_bound.py](../scripts/verify_polynomial_controlled_lower_bound.py) produces [polynomial_controlled_lower_bound.json](../reports/polynomial_controlled_lower_bound.json). Small exact noncommutative polynomials check ordering, truncated-series associativity, and the bound on propagator word length. A separate exact counterexample shows that directly cutting the combined matrix entries can increase a rank-one factorization to rank two; the theorem instead truncates its two factors separately.

An exact rational calibration at $s=1$, $e^{h_*}=65/64$ and fixed dwell $a=1/8$ gives a whole-side cutoff $M=200(n+1)$. A base-depth inequality and a decreasing rational ratio verify the matrix-error budget for every $n\ge1$, not just selected depths. The resulting conservative response floor is at least $2^{-871n-849}$, with every positive segment an integer multiple of $1/(8k)$ and maximum horizon $50(n+1)/k$. This explicit calibration is not an optimized polynomial exponent. The written proof covers arbitrary fixed positive dwell times.

The verifier imports the unchanged shift-register verifier for exact small physical-generator and sparse leaf checks, recording both source hashes. A five-state physical example evaluates actual propagator series and the complete left and right factors at cutoffs 12, 24 and 40. Its controlled-matrix discrepancy decreases from about 45.5 to $3.93\times10^{-5}$ and $9.74\times10^{-12}$. These are high-precision consistency checks, not interval certification, numerical rank inference, or the large register used in the lower theorem. No exponentially large protocol menu or physical state space is enumerated; the new verifier's largest physical generator has dimension five, and the suite maximum remains 68.

Internal proof audits checked the target-only logarithm identity, weighted-norm power bounds at any fixed dwell, both coefficient majorants, separate side truncation, competitor rank and strict tolerance inversion. The result establishes the polynomial growth class with unmatched exponents. It does not establish a polynomial reversible upper bound, a statistical sample bound, or publication originality.

The complete fifteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All fifteen fresh JSON reports matched their saved evidence exactly. The fourteen prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Constant-step comparison and bounded-density reversible sampling

This continuation starts from `c2740b58734deda54f30463395362ef7368cb034`. The fifteen earlier mathematical verifiers and saved reports are preserved. Two focused verifiers accompany the new analytic results. Malformed LaTeX commands in Section 7 of the existing finite-field note were also repaired without changing its mathematics.

[verify_constant_step_compression.py](../scripts/verify_constant_step_compression.py) produces [constant_step_compression.json](../reports/constant_step_compression.json). Exact six-state constructions check both field signs, a two-atom positive mixture and one-atom padding, the positive Jacobi generator, detailed balance, irreducibility and the shifted-reset spectral coefficients. Symbolic preparation calculations verify a common full-support sign-balanced law, its stationarity at zero field, and strong lumpability to the exact passive telegraph process. Positive Gaussian nodes and moments are checked algebraically; rational tolerance budgets combine the all-time quadrature bound with the preparation perturbation. These are exact small identities supporting the general written proof, not numerical rank tests or sampled-time inference.

[verify_bounded_density_sampling.py](../scripts/verify_bounded_density_sampling.py) produces [bounded_density_sampling.json](../reports/bounded_density_sampling.json). Exhaustive enumeration of sixteen nonuniform stratified samples checks forty-eight conditional row/function identities, including an actually nonzero self-row bias and its exact conditional variance. Two small sampled graphs, including repeated microscopic vertices, verify positive reversible realization, exact actuator histogram, and the full-field physical identities. Thirty word probabilities check the finite-prefix recursion and tilt estimates. Fifteen concentration and regenerative budgets use rational logarithm enclosures and exact integer ceilings. The new largest matrix is five; no random trajectories or large sampled graph are generated.

Independent internal audits checked the equilibrium-tilt identity, positive quadrature tail, common-state realization and stationary preparation, the shrinking-amplitude capped lower, sampled-row conditioning, union bound, and regenerative all-horizon conversion. The constant-step predictor does not impose the original field rule or field regularity. The reversible switching theorem requires bounded conductance density and does not preserve the original spectral band. These audits do not establish the cap-only reversible theorem or certify originality.

The complete seventeen-verifier `make check` passed locally in the pinned Python 3.13 environment. All seventeen fresh reports matched their saved JSON evidence exactly. The thirty prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow are byte-identical to the starting commit. The largest matrix across the entire suite remains $68\times68$. GitHub Actions is checked separately after publication.

## Analytic constant-step and density-moment checkpoint

This continuation starts from `3f2bb0924a269c9ff4ce7ccb582e334e59c48c58`. The seventeen preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers are included in the build and source-provenance checks.

[verify_analytic_constant_step.py](../scripts/verify_analytic_constant_step.py) produces [analytic_constant_step.json](../reports/analytic_constant_step.json). A symbolic four-state calculation checks the two active reversible blocks, their commuting reset interpolation, fixed stationary preparation and exact passive lumpability. It checks the coefficient equations giving the exact linear and zero quadratic mean responses for arbitrary weak protocols. Two exact six-state constructions cover both field signs and two positive spectral atoms. A spectral measure whose rank collapses at zero field checks the positive reference-measure repair, analytic Jacobi coefficients and Gaussian moments through degree three. Three rational tolerance budgets combine reference regularization, quadrature, preparation and interpolation errors. The new largest generator has dimension six.

[verify_moment_density_sampling.py](../scripts/verify_moment_density_sampling.py) produces [moment_density_sampling.json](../reports/moment_density_sampling.json). Exact matching-graph calculations check symmetric clipping, its spectral cap and the full physical signed-forcing identity. All 64 vertices of a density box check the sharp algebraic forcing constant; an attaining normalized probability law is not claimed reachable. Exhaustive enumeration of 81 stratified configurations checks 84 conditional row/exit identities, including the self-row bias and the variance bound linear in the clipping threshold. A sampled update with a genuinely negative diagonal checks the necessity and effectiveness of the common rate rescaling. The final reset restores strict irreducibility while preserving ordinary detailed balance and exact actuator masses. Thirty prefix probabilities and fourteen exact concentration/error budgets check the fixed-clock recursion, Bernstein bounds and moment-dependent clipping allocation. The new largest matrix has dimension seven. No random samples or trajectories are simulated.

Reciprocal internal proof audits checked analytic moment regularization, the common-state realization, arbitrary-protocol low-order calibration, occupation-density control, conditional concentration, fixed-clock rescaling, the all-horizon bound and the finite-field clipping obstruction. The step theorem permits tolerance-dependent field derivatives and does not impose the original actuator rule. The switching theorem requires uniform density-tail control and does not preserve the original spectral endpoints. These results do not settle the cap-only reversible problem or certify publication originality.

The complete nineteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All nineteen fresh reports matched their saved JSON evidence exactly. The thirty-four prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow are byte-identical to the starting commit. The largest matrix across the suite remains $68\times68$. GitHub Actions is checked separately after publication.

## Sparse reversible compression and local-walk checkpoint

This continuation starts from `2ede88ab4d5cc0be6075e7f881bc66ec07ebb12b`. The nineteen preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers cover the sparse upper construction and the local-walk lower witness; the build and provenance checker include both.

[verify_sparse_reversible_compression.py](../scripts/verify_sparse_reversible_compression.py) generates [sparse_reversible_compression.json](../reports/sparse_reversible_compression.json). Exact positive nullspace elimination reduces six two-state components to three, taking the full physical model from 13 states to 7. The selected component weights are $1/8,27/40,1/5$. All 14 binary words through length three, all 42 refresh-flag conditional laws, and 28 field-entry tilt checks agree. The length-four total-variation difference is exactly $1/2500$, so the smaller model is not accidentally an exact all-word realization. Full-field identities verify the original rate rule, stationary histogram, ordinary reversibility, and the retained internal band $[3/2,5/2]$.

The same verifier enumerates 18 weighted path/grid offsets and 128 vertices of the driven-density box. It checks the sharp signed-forcing constant, a gap-one partition obstruction, a cap-preserving irreducibility repair with no added states, and six exact rational error allocations. It uses integer ceilings and rational powers rather than rounded logarithmic cutoffs. Its largest matrix has dimension 13.

[verify_local_walk_lower_bound.py](../scripts/verify_local_walk_lower_bound.py) generates [local_walk_lower_bound.json](../reports/local_walk_lower_bound.json). Exact 9-state and 25-state physical targets check the binary histogram, finite-field detailed balance, path correlation trace and resolvent, seven correlation moments each, and four actual-mean Gram entries each. At word depths $n=1,2,3$, sparse position/Walsh coordinates check every binary control word, its unique maximal-distance leaf, and an exact sum-of-squares Gram remainder. The largest Gram matrix is eight-dimensional, with 10,298 active sparse coordinates across its columns; the corresponding 491,521-state physical dictionary is not enumerated.

A rational field and dwell calibration includes the path factor $4n+3$ in the whole-side logarithm transfer. A base case and contracting exact ratio certify every depth, with the conservative floor $2^{-874n-849}$ at cutoff $M=200(n+1)$ and dwell $1/8$. This is a state-count obstruction, not a claim of practical statistical resolution. Four small rational Cauchy examples check the generic inverse-diagonal and trace bounds used for the constant-step lower; the cosine spacing and general-rank argument remain analytic. Source hashes record the two unchanged imported verifiers. The arbitrary fixed-clock theorem follows from the proof, not extrapolation from this one calibration. The largest newly constructed physical generator is 25-dimensional; the suite maximum remains 68.

Reciprocal internal proof audits checked stationary-flux normalization, component reweighting, exact refresh-prefix factorization, spectral-band preservation, the cap-preserving repair without an initial refresh, lattice and cycle cuts, and the Poincaré obstruction to cheap fragmentation. The lower audits checked the unique origin of the endpoint Walsh bit, the full stationary norm factor, the positive equal-weight path spectrum, the interior-mode Cauchy bound for constant steps, and the total-degree logarithm transfer at every fixed positive clock. These audits belong to the same investigation; they are not external validation or novelty certification.

The new results classify polynomial growth for the stated local-plus-refresh class with unmatched exponents. They do not settle the general cap-only reversible problem. The constant-step upper retains its freedom to use a different analytic rate rule; the switching upper preserves the original rule. Neither scenery reconstruction nor statistically efficient acquisition of the signed mean statistics is proved.

The full twenty-one-verifier `make check` passed locally in the pinned environment, and all twenty-one fresh reports matched their saved JSON exactly. The nineteen earlier scripts and reports, MIT license, pinned dependencies and workflow were checked byte-for-byte against the starting commit: all 41 protected files are unchanged. Final repository checks passed for 391 local Markdown links and 22 Python files, together with source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Fixed-label connected-expander checkpoint

This continuation starts from `b9553f7fa3498dcc8dd7210de0b1aa0fc24a93e3`. The twenty-one preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers supplement the [typical-label reversible upper](EXPANDER_SCENERY_COMPRESSION.md) and [fixed-clock lower](EXPANDER_SCENERY_LOWER_BOUND.md). The proof audits checked the evolving sign layer, the all-length good event, the refresh comparison, global-centering leakage, the physical Gram normalization and the fixed-clock transfer. These are independent internal checks, not external mathematical review.

[verify_expander_scenery_compression.py](../scripts/verify_expander_scenery_compression.py) generates [expander_scenery_compression.json](../reports/expander_scenery_compression.json). Exact short paths compare degree-four graph prefixes and longer cycle prefixes, conditioning on holds, moves, sign flips and repeated visits. A low-girth counterexample has total-variation difference $1/64$. Positive elimination reduces eight complete sign-layer coloring components to two, with weights $1/4,3/4$: 48 counted target hidden states become a 13-state physical surrogate. Full-field identities and an exact internal spectrum in $[3/2,19/8]$ check the original field rule, histogram and reversibility.

The same verifier checks 672 single-label word changes, all 14 refresh-flag strings through three updates, the countable failure allocation and exact rational error thresholds. Two length-two runs have total variation $29/576$, exceeding the single-run value $1/24$, so the runwise error factor is substantive. Averaging frozen-label refreshed laws and refreshing the annealed local reference differ by $1/96$; the proof must not interchange those operations. Another 1,456 reduced integer-matrix words through length six check finite cases of the small high-girth graph certificate. The all-length group argument and all-accuracy theorem come from the written proof, not enumeration.

[verify_expander_scenery_lower_bound.py](../scripts/verify_expander_scenery_lower_bound.py) generates [expander_scenery_lower_bound.json](../reports/expander_scenery_lower_bound.json). Physical targets on $K_3,K_4,K_5$ check stationarity, detailed balance, balanced histograms, local spectra, filter identities and twelve actual-mean Gram entries. The largest constructed physical generator has 11 states. Sparse Walsh calculations on cycles with 13 and 21 vertices verify depths one and two, all-terminal maximal-distance leaves, exact sum-of-squares identities and nonzero global-centering leakage. Their largest sparse column has 7,413 coordinates. These cycle checks establish finite geodesic algebra, not a uniformly expanding family.

Exhausting the 16 labelings of $K_4$ checks physical Gram/Parseval identities and 64 label-flip pairs at each depth. Exact induction ratios at a rational field calibration and clock $a=1/8$ certify sufficient base order $N\ge2^{192(n+1)}$, total-degree cutoff $M=300(n+1)$ and response-error floor $2^{-1295n-1279}$, conditional on the graph hypotheses. No graph of that order is constructed. Morgenstern's established graph-existence theorem supplies the family; the verifier does not prove it. An independent audit reran the lower verifier and reproduced its saved JSON exactly.

Both verifiers use exact rational or symbolic calculations without large simulations or numerical rank inference. Their maximum constructed matrices are 13 and 11; the full suite maximum remains $68\times68$. Neither the finite evidence nor the proof claims arbitrary-label reversible compression, a cap-only theorem, a matched exponent, a statistical acquisition guarantee or publication novelty.

The full twenty-three-verifier `make check` passed locally in the pinned environment. All twenty-three fresh reports matched their saved JSON exactly. The twenty-one preceding scripts and reports, MIT license, dependencies and workflow remain byte-identical to the starting commit: all 45 protected files are unchanged. Final repository checks passed for 436 local Markdown links and 24 Python files, with source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Aggregation and register-scenery architecture checkpoint

This continuation starts from `cd8f21a8f8f9d25cd1645ee6a165d1061e0ff3e0`. The twenty-three preceding mathematical verifiers and saved reports remain regression baselines. The new [aggregation lower](AGGREGATION_STATE_LOWER_BOUND.md) and [register-scenery upper](REGISTER_SCENERY_COMPRESSION.md) compare actuator-respecting stationary-flux partition aggregation with newly constructed reversible models. Both use the same fixed six-level histogram, original field rule and advertised band. The new evidence is generated by [verify_aggregation_state_lower_bound.py](../scripts/verify_aggregation_state_lower_bound.py) and [verify_register_scenery_compression.py](../scripts/verify_register_scenery_compression.py), producing [the aggregation report](../reports/aggregation_state_lower_bound.json) and [the register report](../reports/register_scenery_compression.json).

Independent internal proof audits checked the compression-compatible partial isometries, the physical palindrome endpoints, exact projection-loss telescoping, root-cube entropy bound, all-clock actual-mean transfer, affine-dihedral collision probabilities, refresh accounting and uniform register-width replacement. The lower covers every partition in the stated architecture; the upper is uniform over all target widths and all accuracies. These internal audits are distinct from external mathematical review and publication novelty assessment.

The aggregation verifier constructs the full width-one dictionary, with 49 physical states. It checks the six-level histogram and variance, finite-field detailed balance, passive lumpability, and full-state removal of the refresh term. Nine extracted port operators satisfy exact partial-isometry identities. Two nontrivial partitions give eighteen exact agreements between physical gate polynomials and conditional-expectation compressions, including cells that mix root and nonroot addresses. The palindrome norm deficits and telescoping projection losses are checked directly; some tested aggregates lose an entire queried direction.

Width-one and width-two address truth tables verify pure XOR translations and the exact Gram matrices $I_2/6$ and $I_4/6$, without constructing the width-two 385-state physical generator. A $13\times13$ rational Vandermonde inverse checks field extraction exactly; its coefficients have up to 2,880-bit numerators or denominators, making the size of those constants explicit. Small cube partitions and the rational inequality $(16/15)^{15}<4$ check the entropy constant. The transfer checks use representative abstract side bounds $A=2,B=3,\varrho=3/2$ to verify error allocation; they do not calibrate the actual, much larger interpolation-dependent asymptotic constants.

The register-scenery verifier checks 121 formal address words against 15,246 literal actions, and exact binary linear equations for collision probabilities at register widths up to 257. Twenty-seven independently enumerated address-partition laws validate the prefix calculation. Small exact local and refreshed prefix laws test register replacement. Positive selection reduces the width-two dictionary from sixteen configurations to two, or from 385 counted physical states to 49 constructed states, while matching all two-symbol probabilities. A longer four-symbol prefix has nonzero total-variation error $1/3072$, confirming that the selection check distinguishes finite-prefix matching from exact process equivalence.

The selected physical models satisfy the exact histogram, stationary flux and finite-field detailed-balance identities. All thirty-six two-symbol probabilities of the physical uniformized generator agree with the local/refresh decomposition. Exact weighted Gram and Dirichlet identities certify the internal band $[3/2,17/8]$, inside the advertised $[3/2,5/2]$. Rational error budgets check four accuracies down to $1/4096$ and the uniform polynomial exponent; the enormous sufficient reference models are counted, never constructed. Both new verifiers use physical matrices of size at most 49; the preceding suite's maximum remains 68.

The full twenty-five-verifier `make check` passed locally in the pinned environment. All twenty-five fresh JSON reports matched their saved evidence exactly. All 49 protected files—the twenty-three preceding scripts and reports, MIT license, dependencies and workflow—remain byte-identical to the starting commit. Repository checks passed for 478 local Markdown links and 26 Python files, including saved-source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Intrinsic reversibility, soft aggregation, and exact-prefix checkpoint

This integration starts from the recovered research commit `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`, whose parent is the fully tested twenty-five-verifier main commit `80253e1462d618ccc435f2394aba240e858496b5`. The nine archived proof and recovery files remain unchanged. The disconnected workspace lost the uncommitted verifier sources; the three new programs below are fresh implementations with newly generated reports and their own source hashes. They are not represented as byte-for-byte recovery of the earlier sources.

The [main theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) compares ordinary reversible and stationary nonreversible prediction under a common internal exit budget, original field rule and exact nineteen-level histogram. Independent internal proof audits checked physical endpoint normalization, positive off-diagonal gate extraction, all-clock scalar transfer, balanced-flux repair, the deterministic decoded entropy bound, and the unrestricted whole-side rank lower. Separate audits checked the recovered soft-lift and Ritz arguments. These are internal checks, not external review or novelty certification.

[verify_dynamic_lamp_reversibility_lower_bound.py](../scripts/verify_dynamic_lamp_reversibility_lower_bound.py) produces [dynamic_lamp_reversibility_lower_bound.json](../reports/dynamic_lamp_reversibility_lower_bound.json). The width-one target is represented as 146 physical states and 672 directed sparse internal edges, with no dense 146-dimensional generator. Exact stationary flux checks cover the full nineteen-level histogram, variance, three rational exponential fields and passive telegraph lumpability. All 24 oriented port blocks, 48 first/second physical endpoint moments, and four gate cycles are checked. Width-one and width-two literal tables verify XOR query and lamp-flip relations and Gram matrices I_r/36. The width-two 1154-state physical model is counted but not constructed.

The same program checks all 741 factors of an exact 39-node Vandermonde determinant, factorized star and gate Dirichlet bounds, four rectangular transport repairs and their full path errors, and bit-law entropy inequalities using exact integer powers. An explicit stationary approximate-flip coupling acts on eight actual decoded states. Rational allocations exercise the scalar-transfer and entropy thresholds; they do not calibrate the much larger interpolation-dependent asymptotic constants. Its largest dense matrix is eight-dimensional.

[verify_soft_aggregation_lower_bound.py](../scripts/verify_soft_aggregation_lower_bound.py) produces [soft_aggregation_lower_bound.json](../reports/soft_aggregation_lower_bound.json). A genuinely overlapping four-state binary encoder has eight joint hidden states and nine physical states. Exact checks establish the Bayes reverse, BPA dynamics, full-field physical intertwining, stationary-flux compression, and the extra relaxation modes at 5/2. BKA has negative off-diagonal entries -15/64, so omitting the resampling term is observably a different construction. A two-generator physical feature has nonzero squared projection loss 27/32768. A 27-dimensional auxiliary path matrix verifies the positive Ritz energy identity with a nonzero discarded component. This clock is an algebraic device, not a free model coordinate. The finite binary fixture tests general identities; the asymptotic soft lower still concerns the six-level dictionary.

[verify_exact_reversible_prefix_obstruction.py](../scripts/verify_exact_reversible_prefix_obstruction.py) produces [exact_reversible_prefix_obstruction.json](../reports/exact_reversible_prefix_obstruction.json). Exact rational instances N=3,4,6 have at most twenty states. Detailed balance, five equal color masses, half-laziness and the star comparison certify the target spectral band. Forty-eight distinct prefix probabilities per instance recover the row moments, feature norm 1/10 and zero recurrence norm. The longest prefix has exactly fifteen symbols. The extracted eigenvalue has primitive order N. The all-N state bound follows from the analytic positivity argument, not extrapolation from these cases, and it is a zero-error theorem.

All three fresh verifier sources received independent static review and passed individual runs in Python 3.13.5 with the unchanged pinned dependencies. The full twenty-eight-verifier `make check` passes, and all twenty-eight fresh reports match their saved evidence. The repository checker passes 591 local Markdown links and 29 Python syntax checks, including report provenance. A byte comparison preserves all fifty-three protected files from `80253e1462d618ccc435f2394aba240e858496b5` (twenty-five verifiers, twenty-five reports, license, dependencies and workflow) and all nine recovery files from `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`. The suite still has maximum dense dimension 68; the new dynamic-lamp check separately constructs 146 physical states as a sparse graph. GitHub Actions is recorded separately from these local checks.

## Binary reversibility checkpoint

This extension starts from local commit `da0073b`, which integrates the recovered nineteen-level theorem and its twenty-eight-verifier gate. The [binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) and [exact verifier](../scripts/verify_binary_reversibility_lower_bound.py) add the balanced two-level construction and the positive-normalization argument. Its [saved report](../reports/binary_reversibility_lower_bound.json) is generated in the unchanged pinned Python 3.13.5 environment using the standard library and records its own source hash.

The verifier constructs the complete width-one weighted hidden graph: 1,795 hidden vertices, plus the counted visible state. Sparse dynamic programming checks every possible marker starting vertex in both directions, leaving exactly the intended root-to-tip map and its reverse. Root-restricted words of lengths 5, 9, 13 and 17 implement the four logical gates; lengths 21 and 25 select the two complementary probes, including the inactive scrambled cycles. Their exact normalization gives root mass `1/18` and query Gram `I/18`.

Degree counts certify the balanced binary histogram and variance `1/100` for sensitivity `±1/10`. Explicit routes certify basin volume 235, maximum route length 28 and maximum load-to-conductance ratio 235, the finite instance of the analytic gap proof. Original-rule edge fluxes satisfy exact detailed balance at three rational exponential fields, and the zero-field rates give exact passive telegraph lumpability. The physical scalar endpoint normalization is checked on the root selector. The theorem's five-field interpolation and all-width inequalities remain analytic statements.

Two-, three- and five-state exact algebraic cases check the new mixed-norm transport repair and normalization identities. One has raw row sum 10 but an L2 operator cap below 2. Another has a positive nonprojector selector with a zero row and a small positive row sum. The five-state case uses `u=(1/1000,1,1,1,0)` and a nonselfadjoint transport: weighted adjoints, both clipping stages, positive deficit filling, bounded path errors and positive outer-selector probe clipping are all checked exactly. These examples do not add any state during normalization or repair, and do not simulate arbitrary physical rivals.

The new verifier's largest dense matrix has dimension five. The suite's earlier maximum dense dimension remains 68; the 1,795-vertex graph is stored sparsely. This is bounded exact verification, not a large simulation or an enumeration proof of the asymptotic lower bound. The complete binary proof and the verifier received separate internal reviews with no outstanding mathematical issue. Its scope is the common exit budget `6580k`, target/reversible-upper band `[k,13160k]`, exact binary histogram and original field rule. The earlier numerical binary band `[k,3k]`, uncapped reversible rivals and matched exponents remain open. Earlier saved reports retain their checkpoint-specific limitations, including statements of questions that this later theorem resolves.

The full twenty-nine-verifier `make check` passes in pinned Python 3.13.5. All twenty-nine fresh reports are byte-identical to their saved evidence. The final repository checker passes 630 local Markdown links, 30 Python syntax checks and saved-source provenance. All fifty-nine protected files from `da0073b` (twenty-eight verifiers, twenty-eight reports, license, dependencies and workflow) and all nine recovery files are byte-identical to their preceding checkpoints. After explicit user authorization, the nineteen-level and binary checkpoints were published on `main` as `9f4a815808e55e4e699a7fae9407c1e0be4a701d` and `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5`. The binary published tree `17cecbfa8461dc139f7e8d0c55cba89dea584adf` matches the locally tested tree exactly. [GitHub Actions run 35811660258](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35811660258) completed successfully for the published binary commit, separately confirming the twenty-nine-verifier gate.

## State–speed and uncapped-boundary checkpoint

This continuation starts from published `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5`. The [research dossier](RESEARCH_DOSSIER.md) and [claim ledger](CLAIM_LEDGER.md) organize the model, assumptions, theorem dependencies, sources and drafting inputs. Manuscript drafting is not part of this checkpoint.

The [state–speed theorem](STATE_SPEED_ACCURACY_TRADEOFF.md), [unbounded-rate boundary](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md), [uniform rate regularization](RATE_REGULARIZATION.md) and [finite-state fast-rate closure](FINITE_STATE_FAST_RATE_CLOSURE.md) have separate written proofs and internal audits. The audits cover the uniform cap dependence and clock quantifiers, whole-word repair without an operator cap, the PSD substitution obstruction, reset-based Volterra estimates, vanishing-mass states and uniform convergence under arbitrary switching. Internal audits are part of this investigation, not external mathematical validation. The [source follow-up](RATE_BOUNDARY_PRIOR_ART.md) explicitly attributes classical spectral compactification and Markov aggregation and records full-text access limits.

[verify_state_speed_boundary.py](../scripts/verify_state_speed_boundary.py) produces [state_speed_boundary.json](../reports/state_speed_boundary.json) using only exact standard-library rational arithmetic. It checks all-width affine exponent inequalities, sufficient coefficient majorants, rigorously enclosed adaptive-clock constants, and finite forward/inverse width crossovers. It does not numerically invert the exponential field-interpolation matrix or estimate its potentially large constants.

A three-state reversible resolvent verifies both palindrome factorizations and the negative-involution obstruction. Five-state positive-kernel examples have exact raw operator norms 16, 1,000 and 1,000,000 while satisfying the measured whole-word hypotheses; they check nontrivial endpoint clipping, stationary flux repair and rounded-bit couplings. Their high norm is carried by a small-mass state, so these cases test the absence of a global norm assumption. They are algebraic kernels, not physical fast rivals.

A separate three-hidden-state, four-physical-state Poisson fixture checks the same-state rate transformation by exact projector functional calculus, preserves the actuator histogram and original external rates, and certifies the extra zero-field decay factor. It does not prove the general all-protocol Volterra bound. The compactness, purity and rare-fast-contamination arguments are analytic; no finite simulation is presented as their proof. The new verifier has maximum dense dimension five, and the unchanged suite-wide maximum remains 68.

The verifier received a separate static review and passed under pinned Python 3.13.5. Its report records its own source hash and separate hashes of the three proof snapshots used by its fixtures. The repository checker validates both kinds of provenance; a changed proof snapshot requires review and regeneration of this new report. Earlier reports retain their existing schemas and checkpoint-specific scope.

The complete thirty-verifier `make check` passed locally in the pinned Python 3.13.5 environment. All thirty fresh reports are byte-identical to their saved evidence. All sixty-one protected baseline files from `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5` (twenty-nine mathematical scripts, twenty-nine reports, license, dependencies and workflow) and all nine recovery files remain byte-identical. Final documentation, syntax and report-provenance checks pass. This checkpoint was published as `7f127f224eb8fe93d360a0d44b56105f8a388ce0`, with tree `325d09618926f12634b45608682b96ea74a5bcb5` matching the locally tested tree. [GitHub Actions run 35818141188](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35818141188) completed successfully for that published commit.

## Uncapped reversibility and Walsh observability checkpoint

This continuation starts from published `7f127f224eb8fe93d360a0d44b56105f8a388ce0`. The preceding thirty mathematical scripts and thirty reports, MIT license, pinned requirements and workflow are protected baselines. The nine recovery files remain preserved. The new [bounded-control resolvent theorem](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md), [uncapped reversibility lower](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) and [Walsh hierarchy](UNCAPPED_WALSH_OBSERVABILITY.md) have separate written proofs and internal reviews. Manuscript drafting is excluded from this checkpoint.

The full proof reviews cover physical convexification for each target/rival pair, one-variable analytic continuation of an entire protocol, ordered resolvent coefficient extraction, interpolation constants, positive gate approximation, whole-word repair, entropy and inversion of the accuracy threshold. They also cover all-port Walsh normalization, target-only fixed-clock transfer, and the exact width-one quotient. The uncapped reversibility lower requires arbitrarily fast switching; the Walsh hierarchy supplies a separate fixed-target rank result at fixed clock. Neither establishes a binary uncapped penalty, a fixed-clock uncapped superpolynomial separation, or the stronger uncapped lower $\exp(c\delta^{-\alpha})$. Internal reviews remain part of this investigation, not external mathematical validation or novelty certification.

[verify_uncapped_observability.py](../scripts/verify_uncapped_observability.py) produces [uncapped_observability.json](../reports/uncapped_observability.json) using exact standard-library rational arithmetic and integer enumeration. Independent coefficient recurrences check ordered sign-polarized resolvent expansions, including signed endpoint features and an internal speed of one million. The fixtures distinguish the required squared-resolvent word from a single-resolvent substitution.

A seven-hidden-state reversible generator checks positive conditional gates, reverse adjoints, a genuinely negative nonpalindromic flip correlation, and the spectral-cap and $216/s$ approximation certificates. Exact Chebyshev coefficients and rational budgets check the constants 1458 and 186624, the interpolation cutoff $M=3m$, and the error allocation leading to $\Delta\le1/(1024r^2)$. No numerical interpolation of the physical field matrix or empirical estimate of its constants is used.

Small Walsh examples check orthogonality, physical preparation/readout endpoints and exact fiber lumpability of the width-one target to 38 states. Sparse enumeration is used for these state spaces; the new maximum dense matrix dimension is seven, and the suite-wide maximum remains 68. These checks support finite algebraic identities; the general analytic continuation, all-width entropy bound and asymptotic state laws come from the written proofs. There is no large simulation, search over rivals, or extrapolation of numerical ranks.

The source and final error budgets received an independent internal static review. The saved report records the verifier source hash and hashes of the three new mathematical proof snapshots. The repository checker validates both kinds of provenance. The [source comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) records verified primary full texts and limits the novelty assessment to the complete constrained theorem.

The complete thirty-one-verifier `make check` passed locally in pinned Python 3.13.5. All thirty-one fresh JSON reports are byte-identical to saved evidence. All sixty-three protected files from the starting commit and all nine recovery files remain byte-identical. Documentation, syntax and source/proof-snapshot provenance checks pass. This checkpoint was published as 63f6be5f05af145948334324681cfaf48fe715b6 with tree 3d0ea4f5771a0647a4449fcccadb7dab5234b6e9 matching the tested tree. [GitHub Actions run 35820205357](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35820205357) completed successfully.

## Binary uncapped checkpoint

This continuation starts from published 63f6be5f05af145948334324681cfaf48fe715b6. The preceding thirty-one mathematical scripts and thirty-one reports, MIT license, pinned requirements and workflow are protected baselines. The nine recovery files are preserved separately. Manuscript drafting is excluded.

The [binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) has a complete proof through the [rare-tag construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md), [mixed observation interface](MIXED_KILLED_WORD_OBSERVABILITY.md) and [weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md). Separate internal reviews checked all four documents and the combined error budget. The reviews covered exact binary balance, every counted state, uniform gap and cap, distance-weighted killed propagation, two-distance suppression of balancing-state corrections, small selector normalizations, positive gates on arbitrary rival states, vanishing central mass, polynomial word budgets and entropy inversion.

The theorem establishes a polynomial unrestricted upper and an uncapped reversible superpolynomial lower on the new tagged family. Its explicit union with the older binary family adds a polynomial unrestricted lower. The new family has rare states and a very large fixed rate-to-gap ratio; the lower uses arbitrarily fast switching. The older numerical rate budget, fixed-clock uncapped result and stronger $\exp(c\delta^{-\alpha})$ uncapped lower are not claimed. The [source comparison](BINARY_OBSERVATION_PRIOR_ART.md) records primary full-text comparisons and access limits without certifying originality.

[verify_binary_uncapped_observability.py](../scripts/verify_binary_uncapped_observability.py) produces [binary_uncapped_observability.json](../reports/binary_uncapped_observability.json) using only exact standard-library rational arithmetic and finite enumeration. It has no imports from earlier repository verifiers. The saved report records its own source and the five new mathematical proof snapshots; the repository checker validates these hashes.

Three-state balanced examples verify positive binary words with negative quadratic forms for both a resolvent and its square, and the failure of a color-only palindrome test with unequal resolvent parameters. The [boundary note](BINARY_UNCAPPED_RESEARCH_BOUNDARY.md) proves the exact scope of those examples and the remaining PSD subclass. Neither a negative scalar nor these examples alone establishes a state-count lower.

Independent ordered coefficient calculations check mixed resolvent polarization with noncommuting rational contraction factors and cross-color leading cancellation. The contraction factors are finite algebraic proxies: the script does not claim to evaluate the general killed semigroup. Weighted examples include zero support, tiny positive marker values, the exact change of measure and scalar identities; finite stationary couplings check the partial-flip entropy mechanism.

An eight-state tag-and-chain toy checks positive rates, detailed balance, exact histogram, the original field rule and a positive fast-sector certificate. Exact rational exponent inequalities cover all eighteen canonical tag types, their discrimination margins, the distant-state error budgets, and the full theorem's word-count and extraction-tail bounds. The enormous canonical chains and bit tables are counted analytically and never allocated.

The new maximum dense dimension is eight; the suite-wide maximum remains 68. The finite verifier received independent internal static review. Its checks support the displayed algebra and error budgets, while the universal propagation estimates, physical analytic continuation and asymptotic state laws remain analytic proofs. Local verification, remote CI and external mathematical review are distinct forms of evidence.

The complete thirty-two-verifier gate passed locally in pinned Python 3.13.5. All thirty-two fresh reports are byte-identical to saved evidence. The final repository checker passes 1,090 local Markdown links, 33 Python syntax checks, saved-source/proof-snapshot provenance and the unchanged license. All sixty-five protected baseline files and all nine recovery files remain byte-identical. Remote CI for this new continuation is checked separately after publication.

## Fixed-clock uncapped checkpoint

This continuation starts from published `33f23b7cacb65b5e17692771022286f1b94c6999`, whose tree `6503c39327c5171dd88ea9f1a03b5f6e2ae86c8e` matched the preceding tested checkpoint. [GitHub Actions run 35837920760](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35837920760) passed its thirty-two-verifier gate. The sixty-seven baseline mathematical scripts, saved reports, license, requirements and workflow are protected, as are all previously hash-bound proof snapshots and the nine recovery files. Manuscript drafting is excluded.

The [fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md), [Gram interface](FIXED_CLOCK_GRAM_OBSERVABILITY.md), and [positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) establish the two-field uncapped penalty with a conservative inner logarithmic exponent $1/12$. The [internal proof review](FIXED_CLOCK_INTERNAL_REVIEW.md) covers finite row recovery, sampled Gram norms, target-sensitive vector remainders, model-dependent Schur denominators, binary insertions, uniform heat approximation, natural-killing scaling, entropy normalization, the polynomial error budget and finite clock horizon. These are internal reviews, distinct from executable checks and external validation.

[verify_fixed_clock_observability.py](../scripts/verify_fixed_clock_observability.py) produces [fixed_clock_observability.json](../reports/fixed_clock_observability.json). It adds 1,543 finite checks, using exact rational arithmetic for algebraic identities and explicitly labeled float64 calculations for actual semigroups, integrated polynomial coefficients and heat residuals. Dense matrices have dimension at most four. It constructs no large tagged graph and imports no earlier repository verifier.

The exact fixtures check visible-row recursion including zero fields, stationary adjoints, inserted-projector and Gram identities, the physical Schur complement, two-field binary insertion, contractive symmetrized label factors and their possible failure of positive semidefiniteness. The leading cross-color coefficient two and sandwich normalization four are verified separately. Fractional-binomial tail identities, coefficient mass, natural-killing scaling and shifted-Chebyshev recurrence checks supplement the written analytic bounds. A separate representative exponent calculation verifies the powers $4,5,6,7,12$; it does not estimate the theorem's potentially enormous physical constants. The actual numerical errors are recorded beside their bounds, not presented as universal estimates.

The report records its verifier source hash and the three new proof snapshot hashes. The repository checker validates these alongside all existing saved evidence. A separate internal reviewer inspected and ran the new verifier. The [primary-source comparison](FIXED_CLOCK_PRIOR_ART.md) distinguishes embedding and matrix-function results, scalar mean recovery, and observable-operator learning; it neither certifies originality nor converts the weaker logarithmic transfer route into an impossibility theorem.

The complete thirty-three-verifier `make check PYTHON=.venv/bin/python` gate passed locally in pinned Python 3.13.5. All thirty-three fresh JSON reports are byte-identical to saved evidence. All sixty-seven protected baseline files and all nine recovery files remain byte-identical; earlier proof snapshots also pass their saved hash checks. The repository checker passes 1,190 local Markdown links and 34 Python syntax checks, with valid source/proof provenance and an unchanged license. Remote CI is separate evidence, associated with the published commit in GitHub Actions.

## PRL exploration checkpoint

This phase starts from published `04d34df8de8643a44515725c1330d55e8c6f53bc`, tree `22e0def6b56d6339de9a720a872e7743270a242f`. [GitHub Actions run 35841494249](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35841494249) passed the preceding thirty-three-verifier gate. The sixty-nine baseline scripts, reports, license, requirements and workflow, earlier proof snapshots and nine recovery files remain protected. PRL is the user's research target; manuscript drafting remains deferred.

The new proofs are [positive label selectors](POSITIVE_LABEL_SELECTORS.md), [the original tight-band fixed-clock separation](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md), [uniform entropy-production reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) and [the state–entropy-production consequence](STATE_ENTROPY_PRODUCTION_TRADEOFF.md). Their [internal review](PRL_EXPLORATION_INTERNAL_REVIEW.md) checks positivity versus positive semidefiniteness, normalized selector powers, the unchanged target band, the fifth-power observation budget, uniform last-reset entropy bounds, entropy-rate conventions and minimax quantifiers. The [source audit](PRL_EXPLORATION_SOURCE_AUDIT.md) attributes the established symmetrization and entropy-comparison ingredients.

[verify_prl_exploration.py](../scripts/verify_prl_exploration.py) produces [prl_exploration.json](../reports/prl_exploration.json). Its bounded fixtures test the positive selector identities, exact positive-semidefinite certificates, off-grid rival labels, conservative power budgets, arithmetic reversibilization, preservation of exits and stationary masses, the sharpened relative-entropy factor, reset-age integration, and finite-entropy-production regularization. It uses exact rational identities, with numerical matrix exponentials, quadrature and logarithms explicitly labeled; the nineteen-level scalar selector check uses 80-digit arithmetic. It allocates no large target graph.

The new report binds its verifier source and all four new proof snapshots. It contains 561 checks, and passed a separate internal code review and independent pinned-environment rerun with a byte-identical report. Dense matrices have dimension at most five; the suite-wide maximum remains 68. Finite checks supplement the universal analytic claims and do not certify them by enumeration. Local regression, remote CI and mathematical review remain separate evidence.

The complete thirty-four-verifier `make check PYTHON=.venv/bin/python` gate passed locally in pinned Python 3.13.5. All thirty-four fresh reports are byte-identical to saved evidence. All sixty-nine protected baseline files and nine recovery files remain byte-identical, and all earlier proof snapshots pass their recorded hash checks. The final repository checker passes 1,317 local Markdown links and 35 Python syntax checks, with valid source/proof provenance and unchanged license. Remote CI is separate evidence tied to the published commit in GitHub Actions.

## Kinetic-interface and generalized-reversal checkpoint

This continuation starts from published `e38dde1171995892e8a34abc7100b6489ab393bd`, tree `0238889a245e1e8f4b94e8edbd814cd0f3e256f5`. [GitHub Actions run 35845007667](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35845007667) passed the preceding thirty-four-verifier gate. The seventy-one baseline mathematical scripts, reports, license, requirements and workflow, all prior proof snapshots and the nine recovery files remain protected. PRL remains the research target, and manuscript drafting remains deferred.

Five new proof notes cover [general kinetics](GENERAL_KINETIC_INTERFACE.md), the [general endpoint entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md), the [capped two-field separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md), [generalized-reversal prediction](GENERALIZED_REVERSAL_PREDICTION.md), and the [combined resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md). The [internal review](KINETIC_PARITY_INTERNAL_REVIEW.md) records separate checks of exact nonnegative selectors, capped uniformization, inserted-projector clock recovery, target-only rank factorization, reset-age constants and initial-density dependence, the centered-word path-law identity, and ordinary versus generalized entropy-production quantifiers. The [source audit](KINETIC_PARITY_SOURCE_AUDIT.md) attributes established higher-order word reversal and physical parity conventions rather than presenting them as new mechanisms.

[verify_kinetic_parity.py](../scripts/verify_kinetic_parity.py) produces [kinetic_parity.json](../reports/kinetic_parity.json), with 166 bounded checks. A three-hidden-state reversible target has a non-Markov binary actuator process. Its eight-hidden-state length-three word predictor checks exact generalized flux balance, the even middle actuator, equality of center/endpoint stationary output laws through six symbols, target-prefix agreement through four symbols and genuine mismatch at longer prefixes. Exact generator-word calculations and labeled numerical switched propagators supplement the analytic all-protocol response identity. The full fixture has nine states and is not a state-count advantage example.

A reverse-mixture fixture verifies finite positive ordinary entropy production alongside zero generalized entropy production. Separate rational barrier fixtures recover the hidden diagonal and generator from two physical generators, check squared-Lagrange positivity on off-grid rival values, and verify positive adjoint-paired transports under a common cap. General reset fixtures check rate envelopes, residual positivity, finite occupation bounds and both branches of the initial-density-dependent age constant. Numerical exponentials and quadrature are explicitly distinguished from rational certificates.

The new report binds the verifier source and all five frozen proof snapshots. A separate internal reviewer inspected the complete program and its final binding changes, ran pinned Python 3.13.5, and reproduced the report byte-for-byte. The largest new dense matrix has dimension nine; the suite-wide maximum remains 68. No large target is allocated. Finite checks do not enumerate the universal state-complexity or entropy theorems, and no physical device realization is claimed.

The complete thirty-five-verifier `make check PYTHON=.venv/bin/python` gate passed locally in pinned Python 3.13.5. All thirty-five fresh reports are byte-identical to saved evidence. All seventy-one protected baseline files and nine recovery files remain byte-identical, and earlier proof snapshots pass their recorded hashes. The repository checker passes all local Markdown links and 36 Python syntax checks, with valid source/proof provenance and unchanged license. Remote CI remains separate evidence associated with the published commit.

## Updating evidence after code changes

Do not edit saved metrics by hand. After reviewing and running a changed extension, regenerate the saved evidence with:

```bash
python scripts/verify_finite_accuracy.py --output reports/finite_accuracy.json
python scripts/verify_quadrature.py --output reports/quadrature.json
python scripts/verify_minimal_realization.py --output reports/minimal_realization.json
python scripts/verify_response_lower_bounds.py --output reports/response_lower_bounds.json
python scripts/verify_unrestricted_rate_lower_bound.py --output reports/unrestricted_rate_lower_bound.json
python scripts/verify_finite_field.py --output reports/finite_field.json
python scripts/verify_path_information.py --output reports/path_information.json
python scripts/verify_actuator_hierarchy.py --output reports/actuator_hierarchy.json
python scripts/verify_general_compression.py --output reports/general_compression.json
python scripts/verify_reversible_compression.py --output reports/reversible_compression.json
python scripts/verify_general_controlled_lower_bound.py --output reports/general_controlled_lower_bound.json
python scripts/verify_bounded_rate_prediction.py --output reports/bounded_rate_prediction.json
python scripts/verify_shift_register_lower_bound.py --output reports/shift_register_lower_bound.json
python scripts/verify_polynomial_controlled_lower_bound.py --output reports/polynomial_controlled_lower_bound.json
python scripts/verify_constant_step_compression.py --output reports/constant_step_compression.json
python scripts/verify_bounded_density_sampling.py --output reports/bounded_density_sampling.json
python scripts/verify_analytic_constant_step.py --output reports/analytic_constant_step.json
python scripts/verify_moment_density_sampling.py --output reports/moment_density_sampling.json
python scripts/verify_sparse_reversible_compression.py --output reports/sparse_reversible_compression.json
python scripts/verify_local_walk_lower_bound.py --output reports/local_walk_lower_bound.json
python scripts/verify_expander_scenery_compression.py --output reports/expander_scenery_compression.json
python scripts/verify_expander_scenery_lower_bound.py --output reports/expander_scenery_lower_bound.json
python scripts/verify_aggregation_state_lower_bound.py --output reports/aggregation_state_lower_bound.json
python scripts/verify_register_scenery_compression.py --output reports/register_scenery_compression.json
python scripts/verify_soft_aggregation_lower_bound.py --output reports/soft_aggregation_lower_bound.json
python scripts/verify_exact_reversible_prefix_obstruction.py --output reports/exact_reversible_prefix_obstruction.json
python scripts/verify_dynamic_lamp_reversibility_lower_bound.py --output reports/dynamic_lamp_reversibility_lower_bound.json
python scripts/verify_binary_reversibility_lower_bound.py --output reports/binary_reversibility_lower_bound.json
python scripts/verify_state_speed_boundary.py --output reports/state_speed_boundary.json
python scripts/verify_uncapped_observability.py --output reports/uncapped_observability.json
python scripts/verify_binary_uncapped_observability.py --output reports/binary_uncapped_observability.json
python scripts/verify_fixed_clock_observability.py --output reports/fixed_clock_observability.json
python scripts/verify_prl_exploration.py --output reports/prl_exploration.json
python scripts/verify_kinetic_parity.py --output reports/kinetic_parity.json
python scripts/verify_finite_advantage.py --output reports/finite_advantage.json
python scripts/verify_physical_robustness.py --output reports/physical_robustness.json
python scripts/verify_switch_kinetic_interface.py --output reports/switch_kinetic_interface.json
make check
```

The preserved checkpoint verifier remains an unchanged regression baseline. New tests belong in the extension or a new verifier; a deliberate change to that baseline requires revising its provenance explicitly.

## Limits

No large simulations, training, Monte Carlo trajectories, or network requests occur inside the verifiers. A PASS verifies the stated assertions in these programs, not all possible models or protocols by enumeration. Small floating-point errors are expected to differ across platforms. The code and proofs were produced within the same investigation; agreement is not an independent audit. No journal submission, release, physical implementation, or claim of publication-level novelty follows from these checks.
