# Repeated protected readout: focused source comparison

[Protected instrument](FAMILIAR_SWITCH_PROTECTED_READOUT.md) · [Readout counterexample](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) · [Charge realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) · [Earlier calibration audit](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md)

**Bounded primary-source audit, 24 September 2026.** Repeated measurement,
majority decoding, finite-sample concentration and total-variation contraction
are established tools. The purpose of the present construction is narrower:
repair the initial instrument used by this repository's two-word state-cost
witness while permitting correlation between a recorded error and the hidden
transition caused by that same readout. The four full texts below were
inspected at the locations specified. This comparison establishes neither
priority of the complete construction nor device feasibility.

## 1. Repeated QND measurement and majority decoding

Xiao Xue et al., “Repetitive Quantum Nondemolition Measurement and Soft
Decoding of a Silicon Spin Qubit,” *Physical Review X* **10**, 021006
(2020). [DOI](https://doi.org/10.1103/PhysRevX.10.021006),
[author-hosted published PDF](https://qutech.nl/wp-content/uploads/2020/04/2020_04_PhysRevX.10.021006.pdf).
Inspected main text p. 3 and Appendix B, pp. 6–7, especially Eqs. (B8)–(B9).

The experiment repeatedly maps a logical electron spin onto an ancilla,
reads the ancilla and reinitializes it. The text explicitly discusses
majority and weighted-majority decoding. Appendix B uses classical hidden
state trajectories and a factorized observation model conditioned on the
trajectory; the ancilla reset motivates its white-noise assumption.

This is a direct precedent for repeated readout and statistical decoding.
It is not passive repeated measurement of our two charge occupations.
Its fidelity data do not establish a fixed symmetric error probability
conditional on every hidden charge state and prior measurement history.
Our permission for same-use error–kick correlation should be stated
separately from that remaining conditional-probability assumption.

## 2. Barrier pulsing and charge latching

Sanghyeok Park et al., “Single shot latched readout of a quantum dot qubit
using barrier gate pulsing,” *npj Quantum Information* **11**, 148 (2025).
[DOI](https://doi.org/10.1038/s41534-025-01094-x),
[publisher full text](https://www.nature.com/articles/s41534-025-01094-x).
Inspected Results, Eqs. (1)–(2), Fig. 2 and its discussion, and Methods,
“Detailed description of the voltage pulses” and “Measurement.”

The experiment dynamically controls reservoir tunneling to establish a
long-lived charge latch and accelerate subsequent reset. Barrier pulsing
also shifts the adjacent dot's potential; simultaneous plunger pulses
compensate this crosstalk. These observations support treating barrier
control, compensation and switching as real physical resources.

The implementation uses a multi-electron hybrid qubit, an additional
metastable charge configuration and cotunneling. It does not demonstrate
our sector-preserving operation with an unchanged conditional equilibrium
law. Charge latching therefore supplies an actuator precedent, not a
certificate of harmless hidden dynamics or a ready-made realization of
the instrument. Barrier-only backaction remains a specified model
restriction, not an experimental conclusion drawn from this paper.

## 3. A close charge architecture with population backaction

Michael S. Ferguson et al., “Measurement-induced population switching,”
*Physical Review Research* **5**, 023028 (2023).
[DOI](https://doi.org/10.1103/PhysRevResearch.5.023028),
[publisher full PDF](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.5.023028).
Inspected main text pp. 2–3, Appendix A, pp. 5–8, and Appendix B.1,
pp. 8–9, including Eqs. (B1)–(B4).

The two dots are coupled capacitively, each exchanges electrons with its
own lead, and four charge configurations are relevant. An adjacent sensor
dot measures their occupations. This is an unusually close architecture
precedent. It also demonstrates detector-induced changes in preferential
occupation, with negligible interdot tunneling. The microscopic discussion
includes spin degeneracy, and the effective dynamics include
measurement-induced broadening.

The source therefore supports both the candidate architecture and a
concrete limitation: charge discrimination does not imply preservation of
the equilibrium population law. It does not establish the repository's
constant-total-rate kinetics, symmetric independent electronics, or
stationary protected instrument. No numerical backaction tolerance is
transferred from this different device.

## 4. Marginal invariance versus temporal joint distributions

Lucas Clemente and Johannes Kofler, “Necessary and sufficient conditions
for macroscopic realism from quantum mechanics,” *Physical Review A*
**91**, 062103 (2015).
[DOI](https://doi.org/10.1103/PhysRevA.91.062103),
[full HTML manuscript](https://arxiv.org/html/1501.07517v3).
Inspected Sections II B–C (HTML II.2–II.3), Eqs. (6)–(8), (17), and the
paragraph immediately following (17).

The paper distinguishes invariance of a later marginal from invariance
of temporal joint distributions when another measurement is inserted.
Even the collection of all two-time no-signaling-in-time conditions is
insufficient for its three-time criterion. Consequently the broad warning
that nonselective invariance can conceal conditional disturbance is
established. The repository's classical counterexample is a diagnostic
for its instrument premise, not a new general no-signaling principle.
The paper does not supply this repository's finite-state separation or
its particular repeated-readout error budget.

## 5. Remaining assumption and unresolved comparison

The repeated-readout argument retains a fixed conditional error probability
given the entire pre-use hidden state and history. That premise can yield
the binomial majority tail while allowing a same-use hidden kick to depend
on the error. Nonselective conditional stationarity preserves the hidden
marginal; coupling the decoded label to the true sector then bounds the
joint-law defect by the decoding error. This is a witness-specific use of
standard probability arguments. Neither repetition nor a first-two-bit
disagreement check verifies the premise against arbitrary detector memory.
Concentration bounds quantify sampling uncertainty under the stipulated
model; they do not establish that model. The earlier calibration audit
records the concentration references and their inspection limits.

Minsu Kim, Jeongho Bang and Han Seb Moon, “Exact No Signaling in Time
without Temporal Classicality,” [arXiv:2607.14583](https://arxiv.org/abs/2607.14583),
remains an unresolved comparison. This continuation recovered indexed
metadata, but direct abstract, HTML and PDF requests failed. The earlier
audit records an abstract-level lead; its status is not upgraded to
full-text inspection here. No priority or nonoverlap conclusion follows.

The supported advance is a conditional repair of this witness's readout
interface. A complete novelty comparison and physical validation remain
separate tasks. Manuscript drafting remains the last step.
