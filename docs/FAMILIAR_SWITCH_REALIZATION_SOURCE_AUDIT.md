# Familiar switches: charge realization and measurement source audit

[Charge-model derivation](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) · [Unknown symmetric readout noise](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) · [Two-snapshot robustness](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) · [Earlier familiar-model audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) · [Earlier physical audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md)

**Primary-source audit, 24 September 2026.** Two capacitively coupled quantum dots are a concrete candidate for the four-state target. Nondegenerate single-level dots give the required logistic rates in the sequential-tunneling model with constant bare couplings. Published experiments establish relevant components, including coupled charge fluctuations and rapid charge discrimination. The inspected papers do **not** demonstrate the complete target with the preparation, control and disturbance tolerances used in the repository's calibrated certificate. Metallic boxes and several colloidal precedents require different kinetic models. This is a focused evidence audit, not a device demonstration, exhaustive priority search or publication-readiness assessment.

## 1. Seven primary charge-platform sources

All seven main texts were inspected; the Koski supplement was also inspected. Equations and experimental settings below identify what each source supports. Results from distinct devices are not combined into a claimed achieved specification.

| Source and full-text access | Inspected evidence and actual conditions | Limit of the evidence for this task |
|---|---|---|
| **G. Bulnes Cuetara, M. Esposito and P. Gaspard**, “Fluctuation theorems for capacitively coupled electronic currents,” *Physical Review B* **84**, 165114 (2011). [DOI](https://doi.org/10.1103/PhysRevB.84.165114), [full text](https://arxiv.org/pdf/1105.5974), Eqs. (1), (12)–(20). | Spinless single-level dots with capacitive interaction and no interchannel particle exchange. Weak-coupling Markov/secular dynamics have Fermi loading/unloading rates; the paper allows distinct bare couplings at Coulomb-shifted energies. | The equilibrium specialization and equality of those prefactors are explicit assumptions in our embedding. Neither the general Hamiltonian nor detailed balance alone establishes the required constant-total-rate kinetics. |
| **P. Strasberg, G. Schaller, T. Brandes and M. Esposito**, “Thermodynamics of a Physical Model Implementing a Maxwell Demon,” *PRL* **110**, 040601 (2013). [DOI](https://doi.org/10.1103/PhysRevLett.110.040601), [full text](https://arxiv.org/pdf/1210.5661), pp. 1–2, Eqs. (1)–(5). | Two single-level dots interact through Coulomb repulsion without interdot particle transfer. Four charge populations obey a weak-coupling master equation. Rates are bare coupling times a Fermi function or its complement; the text distinguishes energy-dependent couplings from the wide-band limit. | A theoretical architecture and rate law. Its demon operating regime is not our common-equilibrium protocol; that is a specialization of the model. |
| **A. Hofmann et al.**, “Measuring the Degeneracy of Discrete Energy Levels Using a GaAs/AlGaAs Quantum Dot,” *PRL* **117**, 206803 (2016). [DOI](https://doi.org/10.1103/PhysRevLett.117.206803), [full text](https://arxiv.org/html/1610.00928v1), Eqs. (1)–(2), Figs. 2–3. | One reservoir, about 50 mK, charging energy about 1 meV, fewer than nine electrons; QPC charge sensing. Fermi-dependent rates have weakly energy-dependent prefactors. The first eight resonances show alternating 2:1 and 1:2 prefactor ratios; Zeeman-resolved ground transitions give 1:1. | Direct evidence that degeneracy and energy dependence matter. Resolving a ground transition does not establish the required precision across both Coulomb-shifted energies and both controls. |
| **J. V. Koski et al.**, “On-Chip Maxwell's Demon as an Information-Powered Refrigerator,” *PRL* **115**, 260602 (2015). [DOI](https://doi.org/10.1103/PhysRevLett.115.260602), [full text and supplement](https://arxiv.org/pdf/1507.00530), main Fig. 2 and supplement Eqs. (6)–(9). | A normal-metal SET and single-electron-box demon are capacitively coupled. Example settings include a 40 mK bath, electron base temperatures 77/55 mK and bias 20 microvolts. The supplement gives orthodox metal-junction rates, including their equal-temperature reduction. | A working coupled charge device, with different kinetics and a driven, unequal-temperature operating point. It does not supply the target's heat-bath law or a nondemolition bit-error certificate. |
| **K. Chida, A. Andrieux and K. Nishiguchi**, “Coulomb-mediated single-electron heat transfer statistics across capacitively coupled silicon nanodots,” *Communications Physics* **9**, 8 (2026), published 4 December 2025. [DOI and full text](https://doi.org/10.1038/s42005-025-02439-w), [author manuscript](https://arxiv.org/abs/2507.12799), Results and Figs. 1–3. | Two 100-nm silicon dots, electrically separated by about 20 nm, exchange electrons with a common reservoir. A three-terminal detector resolves both charge fluctuations at equilibrium. At 300 K, charging energies are about 7/9 meV and coupling about 2 meV; reported relaxation times are 5.4/9.8 s. | The architecture is close, but multiple charge states participate: charging energies are below the roughly 26 meV thermal energy. This is not the four-state, strongly interacting target. |
| **E. J. Connors, J. J. Nelson and J. M. Nichol**, “Rapid High-Fidelity Spin-State Readout in Si/SiGe Quantum Dots via rf Reflectometry,” *Physical Review Applied* **13**, 024019 (2020). [DOI](https://doi.org/10.1103/PhysRevApplied.13.024019), [full text](https://arxiv.org/pdf/1910.08755), Sec. III, Eq. (3), Fig. 3. | The separate charge-readout experiment uses a roughly 50 mK device, 224 MHz reflectometry and a charge transition tuned to about 10 Hz. Fitted voltage-histogram discrimination gives 98.8% charge fidelity at 100 ns and above 99.9% at 300 ns integration. | These are charge-discrimination results, not the spin figures in the title. Average classification fidelity is not a bound on channel asymmetry, temporal independence, hidden-state disturbance or calibration uncertainty. |
| **D. Taubert et al.**, “Telegraph Noise in Coupled Quantum Dot Circuits Induced by a Quantum Point Contact,” *PRL* **100**, 176805 (2008). [DOI](https://doi.org/10.1103/PhysRevLett.100.176805), [full text](https://arxiv.org/pdf/0801.4002), Figs. 1–3 and concluding discussion. | GaAs/AlGaAs coupled-dot devices at 30–100 mK exhibit QPC-induced charge transitions. Detector biases include 0.1 mV in one stability diagram and 0.6–2.0 mV in the bias comparison. The detector supplies energy for inelastic transitions and changes occupation dynamics. | Charge sensing can disturb populations and rates, not merely phase coherence. This is a mechanism warning from a different device, not a universal numerical backaction bound. |

## 2. Why nondegenerate dots match the target

This section is our algebraic specialization of the published sequential-tunneling model; the complete repository derivation is in [the charge note](FAMILIAR_SWITCH_CHARGE_REALIZATION.md). Absorb common reservoir chemical potentials into the single-dot energies and write

$$
\mathcal E(n_1,n_2)=\epsilon_1n_1+\epsilon_2n_2+Un_1n_2,
\qquad n_i\in\{0,1\},\quad U>0.
$$

Set $S=2n_1-1$, $Z=1-2n_2$, $\epsilon_2=-U/2$ and $\epsilon_1(h)=-U/2-2k_BT h$. Then

$$
\mathcal E/(k_BT)=\text{constant}-JSZ-hS,
\qquad J=U/(4k_BT).
$$

Reversing the unobserved occupation label accounts for the sign of the repulsive electrostatic interaction. With $f(\Delta)=(1+e^{\Delta/(k_BT)})^{-1}$, a nondegenerate level has loading and unloading rates $\Gamma f(\Delta)$ and $\Gamma[1-f(\Delta)]$. Their sum is $\Gamma$. Equal, energy-independent bare couplings on the two dots therefore give the target's equal-attempt heat-bath rates. The microscopic input is the Fermi rate law in Strasberg et al.; the mapping and parameter choices are our calculation.

For the certified fixture $J=H=\log3$, the requirements are $U=4k_BT\log3$ and an observed-dot energy shift $-U/2$. Its conditional addition energies run from $-U$ to $U/2$, including zero. Constancy of the bare couplings must cover these energies and gate settings. Agreement at one charge degeneracy point is insufficient. As an illustrative conversion only, at 50 mK the required $U$ is about 18.9 microelectronvolts; this is not a measured setting in the cited devices.

The Markov approximation also requires weak reservoir broadening, $\hbar\Gamma\ll k_BT$, isolated relevant levels and negligible unwanted transitions. There must be no appreciable direct interdot tunneling or coherent charge hybridization. Additional orbitals, spin/valley channels, cotunneling and gate-dependent barriers require explicit modeling or error bounds. Local gate control includes compensation of cross-capacitances; it does not follow merely from having a plunger gate. The required pulse must also be compatible with reservoir relaxation and the desired clock accuracy.

### Degeneracy cannot simply be absorbed into the energy

For an empty dot and a spin-degenerate singly occupied level, the ideal loading/unloading rates are $2\Gamma f(\Delta)$ and $\Gamma[1-f(\Delta)]$. Their ratio can be represented by shifting the free energy by $-k_BT\log2$, but their sum is $\Gamma[1+f(\Delta)]$, which varies with energy. The equilibrium correction alone does not restore heat-bath kinetics. This is the concrete issue illustrated by Hofmann et al.'s degeneracy measurements.

Charge occupations are even under time reversal. If a magnetic field is used to isolate a spin channel, the microscopic reversal also changes that field and spin. A fixed-field charge-population model can obey ordinary detailed balance under its stated sequential-tunneling assumptions, but it should not be advertised as proof that every discarded microscopic degree of freedom is even. Resolving spin is an additional physical choice, not a silent removal of degeneracy.

### Metallic boxes preserve detailed balance, but change the kinetics

At equal electrode temperatures, the orthodox rate in the Koski supplement is

$$
\Gamma_{\rm metal}(\Delta)=
\frac{\Delta}{e^2R\,[e^{\Delta/(k_BT)}-1]}.
$$

Directly summing opposite directions gives

$$
\Gamma_{\rm metal}(\Delta)+\Gamma_{\rm metal}(-\Delta)
=\frac{\Delta}{e^2R}\coth\!\left(\frac{\Delta}{2k_BT}\right).
$$

This energy-dependent activity approaches $2k_BT/(e^2R)$ only near zero. The rate ratio has the Gibbs form, but the exact mean closure and the current numerical margin cannot be transferred merely by matching the equilibrium energy. Extending the theorem to measured box rates would be a new model calculation.

## 3. What readout and preparation still require

The distinction is between **misclassification of a bit** and **changing the process that generates it**. A fitted charge-discrimination fidelity can support a detector model. It does not show that the two conditional error probabilities are equal, that initial/final errors are independent, or that the errors are independent of the hidden charge and protocol. Likewise, an accurate first readout may heat the device or alter its conditional hidden law. Taubert et al. demonstrate one physical mechanism for such changes. Detector integration can also include a real charge transition, which is different from static classification error.

The [companion readout analysis](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) eliminates the unknown contrasts algebraically when detector errors satisfy an independent symmetric-channel model. Removing the need to know its error probability precisely does not establish that channel model experimentally, and does not remove preparation or backaction assumptions. In particular, neither a balanced observed bit nor a good single-bit fidelity bounds total variation of the full four-state preparation law. Its conservative finite-sample guarantee is separate from the earlier calibrated-detector score test; it is not a laboratory-efficiency claim.

A device comparison would need independently supported full-state equilibration or mixing bounds, compensated local fields, rate characterization over the relevant energy range, and a disturbance bound for the initial observation. Temporarily reading both charges could help validate a proposed target model; it would be an additional characterization resource, not part of the claimed one-bit prediction task. Turning the detector off between snapshots is a candidate implementation choice, not a proven bound on the disturbance caused by either pulse. None of the inspected papers supplies all these bounds at $10^{-5}$.

## 4. Colloidal alternatives: useful components, different dynamics

Three additional primary full texts were inspected in the parallel platform audit and checked here. They keep the physical alternatives concrete without implying that the electronic route is the only possibility.

| Primary source | Demonstrated component | Mismatch with the present target |
|---|---|---|
| **A. Curran et al.**, “Partial Synchronization of Stochastic Oscillators through Hydrodynamic Coupling,” *PRL* **108**, 240601 (2012), [DOI](https://doi.org/10.1103/PhysRevLett.108.240601), [published PDF](https://www.gla.ac.uk/media/Media_236326_smxx.pdf). | Two 800-nm colloids in bistable optical traps; 1.55 kHz imaging, order-one-second hops and 2–3-hour traces. | Coupling is through hydrodynamic mobility while the landscapes remain substantially unchanged. This does not demonstrate an energetic $-JSZ$ interaction. |
| **D. Babič, C. Schmitt, I. Poberaj and C. Bechinger**, “Stochastic resonance in colloidal systems,” *Europhysics Letters* **67**, 158–164 (2004), [DOI](https://doi.org/10.1209/epl/i2004-10055-3), [full PDF](https://d-nb.info/1136571035/34). | Independent tilt/barrier control for one colloid; intrawell relaxation below 0.1 s and a measured Kramers time $7.3\pm0.4$ s. | It is a single bistable element; Kramers kinetics do not guarantee constant-total-rate heat-bath switching. |
| **A. Ortiz-Ambriz and P. Tierno**, “Engineering of frustration in colloidal artificial ices realized on microfeatured grooved lattices,” *Nature Communications* **7**, 10575 (2016), [DOI](https://doi.org/10.1038/ncomms10575), [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4740443/). | Interacting dipolar colloids in bistable grooves with individual imaging/manipulation; the Methods include an isolated-pair check. | The reported barrier is about $540k_BT$ and suppresses spontaneous thermal switching. The field changes interactions; it is not our prescribed local bias. |

These papers support bistability, coupling or control separately. None supplies the exact target kinetics or the current precision assumptions. A deliberately feedback-synthesized classical switch network would also have to count its controller and measurement assumptions explicitly.

## 5. Bounded prior-art and claim boundary

The older reduction lead remains unresolved at full-text level: **H. Falk**, “Reduced Markov chains at stochastic spin models,” *Physica A* **119**(3), 580–590 (1983), [DOI](https://doi.org/10.1016/0378-4371(83)90110-3), [publisher record](https://www.sciencedirect.com/science/article/pii/0378437183901103). A bounded follow-up recovered the publisher abstract, which describes reduced discrete-time Glauber models preserving cluster equilibrium marginals while generally changing dynamics. Publisher/Elsevier full-text attempts and a focused repository search did not produce the paper. Its technical special cases have not been cleared; the abstract cannot establish novelty or nonoverlap.

The supported physical statement is an exact mapping **within an explicit sequential-tunneling model**, with experimental precedents for several ingredients. The supported mathematical statement comes from the linked repository proofs under their own preparation, control, readout and predictor-class assumptions. Neither establishes that an existing device has demonstrated the predictive-state advantage. No heat-cost, generalized-reversal, unrestricted path-law, or publication-readiness claim follows from this audit.
