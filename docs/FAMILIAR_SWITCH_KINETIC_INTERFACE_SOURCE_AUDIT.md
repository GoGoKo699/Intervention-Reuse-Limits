# Kinetic tolerance and protected readout: source audit

[Kinetic tolerance](FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) ·
[Protected initial readout](FAMILIAR_SWITCH_PROTECTED_READOUT.md) ·
[Five-million-trial test](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md) ·
[Earlier charge-platform audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)

**Primary-source audit, 24 September 2026.** Published charge devices
provide precedents for reservoir isolation, barrier pulses during readout,
and compensation of gate crosstalk. They motivate a concrete implementation
route for the protected instrument. They do not establish its conditional
stationarity or joint-law accuracy for the present coupled-switch target.
The new kinetic and instrument guarantees are repository deductions under
explicit promises; no inspected experiment establishes the full numerical
specification.

## Inspected primary evidence

The four full texts below were inspected for this checkpoint. The links
identify the publication and the inspected author manuscript; versioned
manuscripts fix the passage locations.

| Primary source | Inspected passage and supported component | Boundary for this project |
|---|---|---|
| **H. G. J. Eenink et al.**, “Tunable Coupling and Isolation of Single Electrons in Silicon Metal-Oxide-Semiconductor Quantum Dots,” *Nano Letters* **19**, 8653–8657 (2019). [DOI](https://doi.org/10.1021/acs.nanolett.9b03254), [author manuscript v2](https://arxiv.org/pdf/1907.08523v2). | Section I, manuscript pp. 3–4, Fig. 3: lowering the reservoir-barrier voltage suppresses electron loading and unloading; the isolated double dot retains interdot transitions. Virtual gates compensate the effect of the interdot barrier on detuning and on-site potential. | Demonstrates useful barrier and compensation controls, not freezing one observed dot while a separately reservoir-coupled spectator retains the required conditional Gibbs law. Its quoted below-1-Hz rate is an **interdot** rate, not a certified residual reservoir-leakage bound for our measurement. |
| **S. Park et al.**, “Single shot latched readout of a quantum dot qubit using barrier gate pulsing,” *npj Quantum Information* **11**, 148 (2025). [Publication](https://doi.org/10.1038/s41534-025-01094-x), [author manuscript v2](https://arxiv.org/pdf/2408.15380v2). | Published Results, Eqs. (1)–(2), Fig. 2 and Methods; manuscript pp. 1–4, Conditions 1–2: barrier pulses control loading, latch lifetime and reset sequentially. Latch escape must be slow compared with measurement bandwidth. The authors explicitly compensate barrier-to-plunger crosstalk. | This hybrid-qubit readout maps to additional metastable charge configurations and includes cotunneling. It is a precedent for the **actuator**, not an implementation of our four-state conditional-equilibrium instrument. Its readout/reset fidelities do not certify independent symmetric electronic errors or our joint-TV bound. |
| **G. Bulnes Cuetara, M. Esposito and P. Gaspard**, “Fluctuation theorems for capacitively coupled electronic currents,” *Physical Review B* **84**, 165114 (2011). [DOI](https://doi.org/10.1103/PhysRevB.84.165114), [full text](https://arxiv.org/pdf/1105.5974). | Eqs. (12)–(19): sequential loading/unloading rates are Fermi factors times bare couplings evaluated at the unshifted or Coulomb-shifted energy. Eq. (20) states the time-scale separation behind the Markov approximation. | Matching those prefactors is an additional heat-bath assumption. Our symmetric edge-prefactor perturbations allow small failures of that equality while preserving the stipulated equilibrium law. The publication supplies no 20-parts-per-million rate guarantee for this target. |
| **D. Taubert et al.**, “Telegraph Noise in Coupled Quantum Dot Circuits Induced by a Quantum Point Contact,” *PRL* **100**, 176805 (2008). [DOI](https://doi.org/10.1103/PhysRevLett.100.176805), [full text](https://arxiv.org/pdf/0801.4002). | Abstract, Figs. 1–3 and concluding discussion: a biased charge detector induces inelastic transitions and modifies charge dynamics in coupled-dot devices. | Accurate charge discrimination alone does not certify a harmless initial instrument. This is evidence for a backaction mechanism, not a universal numerical lower or upper bound on disturbance. |

## What follows from the present mathematics

The invariant-sector identity in the protected-readout note is a direct
finite-state calculation. Holding the observed sign fixed while preserving
each conditional equilibrium law preserves the joint distribution of the
initial sign and the state after readout. Large hidden rearrangements are
compatible with that identity. The leakage coupling and conditional-flux
defect bounds quantify its failures. None of these statements is attributed
to a device paper, and no priority claim for general invariant-kernel or
coupling facts is made.

The charge implementation calls for a barrier-control operation before the
active word, including compensation and barrier release. Its actuator,
accuracy and duration are additional physical resources. It uses the same
two tested field words and two recorded bits, but is not accomplished by
those two field settings alone. Keeping the observed charge fixed does not
by itself preserve the spectator's equilibrium odds; detector heating or
gate-induced energy shifts still need a bound. The property must hold for
every admitted model's own conditional law, not merely for the proposed
four-state target. Constant-sign integration must also have the stipulated
hidden-history-independent electronic channel.

For active dynamics, the new result transfers each full initial–final joint
table using an integrated generator-row TV error. Its four-state ordinary
upper requires fixed generators at each plateau, the same Gibbs laws and
detailed balance. The 20-parts-per-million symmetric-prefactor allowance
is a conservative **sufficient mathematical condition**, not an achieved
device precision. The wider 100-parts-per-million row supplies population
state counts only.

The five-million-trial design separately recomputes the mean, variance and
gate budgets for kinetic error $10^{-4}$ and ordinary-null approximation
allowance $2\times10^{-4}$. It inherits the established concentration tools
documented in the [weaker-field audit](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md).
The new predictor upper is $1.2\times10^{-4}$, within that null allowance.
Neither a finite reset wait nor a published charge fidelity establishes
fresh-trial independence. Preparation and characterization costs remain
unpriced; the older target-only reset bound is not extended to arbitrary
kinetically perturbed targets or arbitrarily slow rivals.

This is a bounded component audit. The unresolved Falk full-text comparison
and novelty limits in the earlier audit remain open. It does not establish
a device demonstration, full visible-path equivalence or PRL readiness.
Manuscript drafting remains deferred.
