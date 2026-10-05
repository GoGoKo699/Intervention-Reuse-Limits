# Scientific background for the frozen manuscript

**Background consolidation, 30 September 2026.** This guide supplies the
concepts, physical precedents and closest-result comparisons needed to
present the [frozen scientific case](SCIENTIFIC_CASE.md). It adds no
theorem or experiment. **Bo–Celani is the selected tutorial anchor.**
The [project narrative](../REVIEW.md) supplies the bridge to the proofs;
the [selection record](TUTORIAL_OPTIONS.md) retains the alternatives
considered.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [BibTeX file](../references/manuscript.bib) collects the twenty
sources used here or in the shortlist. Keys shown below match that file.
This is a focused working bibliography, not a requirement that a reader
master twenty papers or that the manuscript cite every historical audit.

## 1. The question the background must prepare the reader to ask

Eliminating a hidden variable can produce a useful small kinetic model.
The harder question is whether one such model remains accurate when
the controls change, and how many persistent states are necessary at
the requested accuracy. The present work answers that question for one
specified equilibrium target and endpoint observation task.

Three distinctions organize the background:

| Distinction | Why it matters here |
| --- | --- |
| Observed sign, linear coordinate and Markov state | A binary output can conceal memory. Three closed mean coordinates do not by themselves define three nonnegative state probabilities. |
| A particular coarse-graining and every admissible predictor | Failure of one partition or fitting procedure cannot establish a minimum over all smaller positive models. |
| A held-field or cycle-specific model and a reused field-generator family | The same generators must fit the calibration holds and their compositions. A separate model for each experiment is a different task. |

These distinctions are established background. The candidate contribution
is the matched control/accuracy/state-count law and its finite-setting
consequence under the declared interface. The source comparisons below
identify the additional conditions and conclusions precisely.

## 2. Minimal mathematical language and the bridge to the proofs

Use row probability vectors throughout the manuscript. A finite
continuous-time generator satisfies $`Q_{ij}\ge0`$ for $`i\ne j`$ and
$`Q\mathbf1=0`$. Probabilities obey $`\dot p=pQ`$, whereas a column
observable $`f`$ obeys

```math
\frac{d}{dt}\mathbb E[f(X_t)]=\mathbb E[(Qf)(X_t)].
```

A hold at field $`h`$ lasts $`a`$ and has propagator $`e^{aQ_h}`$. Write $`K_w`$
for a word's chronological product. With $`D_s`$ the diagonal indicator
of visible sign $`s`$, its endpoint-pair law is

```math
P_w(s,s')=\nu D_s K_w D_{s'}\mathbf1.
```

An intermediate observation inserts another indicator matrix into the
product. Matching endpoint pairs therefore does not establish matching
of full output trajectories. The target uses the fixed law
$`\nu(S,Z)=(1+tSZ)/4`$; rivals may choose a different initial law for
each word. Pair-TV error includes the initial marginal, so arbitrary
rival preparation cannot be silently replaced by balanced preparation.
These are the repository's task definitions, not an extra claim about
the cited models.

For a partition with indicator matrix $`C`$, equal total exit rates into
each block give $`Q_hC=C\overline Q_h`$. If the same partition satisfies
this at both fields, exponentiation and multiplication preserve the
quotient under every word. Without such closure, the conditional hidden
distribution can retain history. This explains *lumpability*; it does
not exhaust the possible smaller surrogate models.

The [mean equations](FAMILIAR_SWITCH_FAST_RELAXATION.md) close on
$`1,S,Z`$. Writing $`x=\mathbb E S`$, $`z=\mathbb E Z`$ gives

```math
\dot x=A_h-x+B_hz,\qquad \dot z=r(tx-z).
```

The lag $`z-tx`$ is the fast coordinate. Its elimination motivates an
effective two-state model; the proof notes determine its actual error
under each control menu. Keep the expansion parameter $`1/r`$ distinct
from the requested prediction tolerance $`\epsilon`$. An asymptotic
reduction at a fixed field supplies neither uniform accuracy over
unrestricted words nor a lower bound against all smaller realizations.

| Background needed | Source passage and manuscript use | Project-specific next step |
| --- | --- | --- |
| CTMCs, stationary laws and reversal | `Seifert2012`, [author text](https://arxiv.org/pdf/1205.4176), §§6.1.1–6.1.3, Eqs. (110)–(114), for master equations, currents, detailed balance and trajectory probabilities. | State the row convention and exact endpoint contract before the theorem. |
| Lumpability | `Cardelli2023`, [accepted manuscript](https://backend.orbit.dtu.dk/ws/files/318778353/HKKR_Algorithmic_Minimization_of_Uncertain_Continuous_Time_Markov_Chains.pdf), §II, Theorem 2, for the classical pointwise exit-sum criterion and all-initial-law quotient. | Distinguish a partition criterion from an all-realization lower. The paper's uncertainty/value-function optimization is not being imported. |
| Fast-variable averaging | `BoCelani2017`, [author review](https://arxiv.org/pdf/1612.04999), §2, especially §2.2, Eq. (29), for averaging slow transition rates against conditional fast stationary laws. | R92–R93 prove the menu-dependent orders; R98 supplies the finite witness. |
| Positive realization | `BenvenutiFarina2004`, [tutorial PDF](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf), §II, Theorem 2 and Eq. (2), §§VI–VII, for invariant cones and positive order versus linear order. | Establish an actual common CTMC, its readout and equilibrium properties; a three-coordinate closure alone is insufficient. |

Only elementary finite probability, matrix algebra, matrix exponentials,
linear ODEs and asymptotic estimates are needed to follow the central
proofs. A full stochastic-calculus course, fluctuation-theorem machinery
and large-scale simulation methods are not prerequisites. The broader
textbook option is available for readers who want those foundations.

## 3. Physical model: what is inherited and what is chosen

The [community-model note](FAMILIAR_SWITCH_COMMUNITY_MODEL.md) supplies
the complete derivation. Its existing
[assumption-family ledger](PHYSICAL_ASSUMPTION_ALIGNMENT.md) remains
the corroborating record. The essential citation chain for the frozen
model is compact:

| Source and inspected passage | What it supports | Qualification to retain |
| --- | --- | --- |
| `BulnesCuetara2011`, [author text](https://arxiv.org/pdf/1105.5974), §II A, Eq. (1), Eqs. (12)–(20) | Spinless four-occupation Hamiltonian, capacitive interaction, sequential Fermi rates and Markov timescale ordering. | Its bare couplings may depend on addition energy. It does not establish unchanged barriers during our protocol. |
| `Strasberg2013`, [author text](https://arxiv.org/pdf/1210.5661), Eqs. (1)–(5) and adjacent rate definitions | The same population-rate family; shifted/unshifted bare-coupling equality is the wide-band specialization. | The paper's demon operating regime is not the equilibrium operating point chosen here. |
| `Ruokola2011`, [author text](https://arxiv.org/pdf/1102.4187), rates after Eq. (2), Eq. (8) | One reservoir per dot, energy-independent bare rates for discrete levels, and two-gate capacitance energy. | Its metallic-island branch has different kinetics. Compensated control is our deduction from its electrostatics. |
| `Esposito2010`, [author text](https://arxiv.org/pdf/0909.3618), Eqs. (1)–(4), closing discussion | A driven level with constant coupling and the microscopic interpretation of ideal jumps. | The stated timescale window motivates a limit; it does not bound ramp errors in our growing pulse train. |

Selecting a common temperature, fixed chemical potentials and no
interdot particle transfer gives an equilibrium specialization. From the
Fermi-rate ratio, detailed balance follows for the grand energy
$`\mathcal E=\epsilon_1n_1+\epsilon_2n_2+Un_1n_2`$. The repository's
substitution

```math
S=2n_1-1,\quad Z=1-2n_2,\quad J=\frac{U}{4k_BT},\quad
\epsilon_2=-\frac U2,\quad \epsilon_1=-\frac U2-2k_BT h
```

gives $`\mathcal E/(k_BT)=-JSZ-hS-J-h`$. This algebraic identification
and the selected operating point are deductions, not an experiment
reported in those papers. Occupation labels are time-even; literal
magnetic-spin reversal should not be substituted for this convention.

Keep three kinetic choices separate: flat coupling versus transition
energy, equal attempts on the two dots, and unchanged tunneling barriers
during control. Equal attempts are not assumed in the present
$`r=\Gamma_Z/\Gamma_S`$ theorem. Spinlessness, isolated levels, weak
tunneling and short reservoir memory define the selected physical
branch. The sources do not provide a microscopic error certificate at
arbitrarily fine theorem tolerances.

## 4. Equilibrium structure is an additional model requirement

Ordinary detailed balance is $`\pi_iQ_{ij}=\pi_jQ_{ji}`$. It does not
alone determine how a control changes stationary weights. The separate
energy coupling through the measured sign gives
$`\pi_h\propto\pi_0e^{hS}`$. A fixed readout-compatible equilibrium
aggregation inherits this relation by summing weights. For a freely
fitted rival the corresponding unknown-tilt Gibbs rule is a declared
interface requirement; it is not inferred from endpoint agreement.

| Source | Background supplied and boundary |
| --- | --- |
| `Esposito2012`, [author text](https://arxiv.org/pdf/1112.5410), §III, Eqs. (31)–(32), (34), (37), (39) | Coarse rates depend on conditional microscopic populations; the equilibrium specialization needs its stated conditions. Matching stationary weights or fluxes does not alone establish exact finite-time closure. |
| `StrasbergEsposito2017`, [author text](https://arxiv.org/pdf/1703.05098), §II C, Eqs. (25)–(28) | Conditional equilibration and log-sum free energy supply the established equilibrium-reduction background. Our Gibbs-inheritance calculation uses the equilibrium sum; exact switched closure is a separate issue. |
| `Maes2021`, [author review](https://arxiv.org/pdf/2011.09200), §§I–III and V in the preprint | Local detailed balance relates rate ratios to reservoir exchanges and leaves kinetic prefactors undetermined. Multiple reservoirs/channels require care; an abstract fitted generator alone is not a measured heat or entropy-production result. |

The [equilibrium-reduction note](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md)
proves the needed inheritance statements and separates them from closure.
A stationary deterministic projection of a reversible process retains
reversal symmetry, although it may have memory. Thus the smaller general
predictor's nonreversibility must not be described as dissipation generated
by simply hiding part of an equilibrium system.

## 5. Closest results and the precise remaining contribution

The table records what the inspected results supply. The last column is
our comparison of their hypotheses and conclusions with this project;
it is not a literature-wide absence theorem.

| Source and exact passage | Established result | Additional requirement or conclusion here |
| --- | --- | --- |
| `GrigolettoTicozzi2023`, [v2](https://arxiv.org/pdf/2208.05968), Problems 1–2, Theorems 1–2, Proposition 4 | Stochastic HMM reduction with selected initial laws and distinct single-time/multitime preservation tasks. | The specified controlled deterministic-readout/Gibbs interface and class-wide finite-error hierarchy. Preparation specificity itself is established. |
| `PetreczkyBakoVanSchuppen2012`, [v2](https://arxiv.org/pdf/1103.1343), Theorems 3 and 5, Remark 12 | Shared switched linear realization, reachability/observability and generalized Hankel-rank minimality, with a continuous-time correspondence. | Probability normalization, positive generators, deterministic readout and equilibrium constraints on the common realization. |
| `GrigolettoViolaTicozzi2025`, [v1](https://arxiv.org/html/2510.25546v1), Proposition 2, Theorem 1 and following discussion | A physical controlled reduction preserving expectations for all initial states and controls; minimality relative to its algebraic procedure. | Our preparation task is narrower; our lower bounds range over all admissible small rivals. Our smaller model does not improve its stronger all-state guarantee. |
| `FornaceLindsey2025`, [v3](https://arxiv.org/html/2506.22918v3), §4.1, Eq. (52), Lemma 4.1, Corollary 4.6, Theorem 3 | Positive reversible compression and quantitative error bounds for one autonomous chain. | One family shared across controls, with necessary state-budget bounds in addition to sufficient constructions. |
| `Brandner2025`, [published text](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.037101), Eqs. (8)–(14), (21)–(25) | Effective autonomous generators, slippage and systematic weak-memory corrections. | Matched approximation orders under the specified shared controls and positive/Gibbs state budgets. Correcting an effective rate is an established method. |
| `MeyerBrandner2026`, [v2](https://arxiv.org/html/2510.26325v2), Eqs. (5)–(13), Floquet passage, Supplement I | Periodically driven weak-memory reduction via a complete-period map. | The same two field generators must also fit the separate calibration holds. A cycle-specific reduced matrix need not meet this factorization requirement. |
| `FrancoKepkaVelazquez2026`, [published text](https://link.springer.com/article/10.1007/s00205-026-02183-7), Definition 3.1, Propositions 3.8–3.9, Corollary 3.11, Example 3.12 | One-generator reciprocal-response tests and an existing three/four-state distinction. | Two linked controlled kernels, constructive positive realizations, and quantitative state minima for the same endpoint task. Reciprocity alone is not the novelty claim. |

The [earlier focused comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
also documents autonomous hidden-equilibrium inference and cautions about
thermodynamic inference from coarse paths. Those references remain
available if the manuscript discusses those subjects; they need not all
become introductory prerequisites.

`Falk1983`, [publisher record](https://doi.org/10.1016/0378-4371(83)90110-3),
remains abstract-only in this audit. The indexed description supplies an
early equilibrium-preserving stochastic-spin reduction precedent. A
renewed bounded search did not obtain full text. Its formulas and special
cases have not been cleared, so retain this explicit priority limitation.

## 6. Citation placement and evidence boundaries

| Manuscript purpose | Smallest useful source cluster or repository evidence |
| --- | --- |
| Introduce reduced kinetic models and hidden fast variables | `BoCelani2017`; definitions from `Seifert2012` if needed |
| Specify the physical target | `BulnesCuetara2011`, `Strasberg2013`, `Ruokola2011`, `Esposito2010`; community-model derivation |
| Explain the equilibrium rival class | `Esposito2012`, `StrasbergEsposito2017`; equilibrium-reduction note; `Maes2021` for rate-ratio versus kinetics distinctions |
| Explain why linear order is insufficient | `BenvenutiFarina2004`; `PetreczkyBakoVanSchuppen2012` if using switched-realization language |
| Position the actual reduction claim | HMM, controlled reduction, reversible compression and the two weak-memory papers in Section 5 |
| Present the accuracy hierarchy | [R92](FAMILIAR_SWITCH_QUADRATIC_PRECISION.md), [R93](FAMILIAR_SWITCH_RAPID_CONTROL.md), [R94](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md) |
| Present the finite operational witness | [R98](FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md); compare its shared-generator requirement with `MeyerBrandner2026` |
| Discuss the finer equilibrium obstruction | Unknown-tilt lower proof and `FrancoKepkaVelazquez2026`; retain the Falk qualification |

No source here certifies the theorem's growing pulse train in a device.
The alternating setting contains $`2\lceil r/2\rceil`$ held segments;
the other two settings are single calibration holds. At fixed
$`\Gamma_Z`$, each alternating segment lasts $`1/\Gamma_Z`$, and the
alternating protocol's total duration grows as $`r/\Gamma_Z`$.
Ideal jumps, true endpoint records and the absence of
a demonstrated hardware/heat saving must remain explicit. Old sampling,
detector and numerical certificates belong to their original tasks.

## 7. Access record and completion

This consolidation freshly checked the pedagogical sources, CTMC
lumpability statement, HMM and switched-linear passages, physical-model
passages, equilibrium-reduction background and rate-ratio review.
The controlled, reversible-compression, reciprocal-response and
weak-memory comparisons combine reopened passages and metadata with
the same-day [sanity audit](FINAL_SANITY_AUDIT.md) and its earlier
equation-level checks. They are not represented as wholly new full-paper
audits. Gardiner's recommended chapter coverage is contents-based;
the preface and probability sample were inspected, not the entire book.
Falk remains the explicit full-text gap. Section references follow the
linked versions, whose pagination can differ from the journal editions.

The scientific background needed for the frozen claim is now organized
for drafting. No new theorem, model family, simulation or replacement
research gate follows from this pass. The selected **Bo–Celani** route
now leads through a [compact project narrative](../REVIEW.md) to the
existing proofs. Other bibliography entries support attribution rather
than adding to the single-source teaching prerequisite. The manuscript
itself remains the final phase.
