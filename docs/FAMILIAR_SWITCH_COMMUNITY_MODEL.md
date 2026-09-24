# A published coupled-dot model for the ideal prediction theorem

[Physical-assumption policy](PHYSICAL_ASSUMPTION_ALIGNMENT.md) · [Charge mapping](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) · [Minimal four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md)

**Model decision, 24 September 2026.** Use the spinless, single-level,
capacitively coupled quantum-dot master equation, in its equilibrium,
constant-interaction and wide-band specialization. This established
mesoscopic model supplies a physical basis for the four-state target and
its controlled occupation probabilities. The main retained result is a
comparison of predictive state counts for ideal endpoint laws. It does
not require inventing a detector. A laboratory test of those laws needs
an additional, compatible measurement model.

The selection below reconstructs one consistent model. Published premises,
our parameter choices, and our deductions are distinguished explicitly.
Exact statements concern the reduced master equation, not an exact
microscopic description of every quantum-dot device. Existing proofs and
certificates are unchanged.

## 1. Equation-level source map

All listed model passages were inspected in full text. The five-paper
family ledger is in the [alignment note](PHYSICAL_ASSUMPTION_ALIGNMENT.md);
one additional source addresses the previously unresolved drive idealization.

| Ref. | Primary source and inspected location | What is inherited; boundary |
| --- | --- | --- |
| C1 | Bulnes Cuetara, Esposito and Gaspard, *PRB* **84**, 165114 (2011), [author text](https://arxiv.org/pdf/1105.5974), Sec. II, Eq. (1), Eqs. (12)–(20), pp. 2–4 | Spinless four-occupation Hamiltonian and weak-coupling Fermi rates. Reservoir memory is shorter than the coarse-graining time, itself shorter than population relaxation. Couplings at the two addition energies may differ. |
| C2 | Strasberg et al., *PRL* **110**, 040601 (2013), [author text](https://arxiv.org/pdf/1210.5661), pp. 1–2, Eqs. (1)–(5) and adjacent definitions | Same capacitive population model; equality of shifted and unshifted bare couplings is identified with the common wide-band approximation. Its demon regime is not our equilibrium operating point. |
| C3 | Ruokola and Ojanen, *PRB* **83**, 241404(R) (2011), [author text](https://arxiv.org/pdf/1102.4187), pp. 1–2, rates following Eq. (2); p. 4, Eq. (8) | One reservoir per dot, explicitly energy-independent tunneling strengths, discrete-level Fermi-rate branch, and two separate electrostatic gates. The metallic-island branch has different rates. |
| C4 | Sánchez and Büttiker, *PRB* **83**, 085428 (2011), [author text](https://arxiv.org/pdf/1008.3528), Sec. II A, Eq. (2), p. 3; Appendix A, p. 6 | Four-state sequential model and capacitance-derived addition energies. Its conversion mechanism retains energy-dependent transmissions. Appendix A controls reservoir voltages, not two independent plunger gates at fixed reservoir potentials. |
| C5 | Sánchez, López, Sánchez and Büttiker, *PRL* **104**, 076801 (2010), [published text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.104.076801/fulltext), p. 076801-2, Eq. (4) | Same four-state Fermi generator family; its Coulomb-drag mechanism uses occupation-dependent bare couplings and bias. It is not a constant-prefactor operating example. |
| C6 | Esposito, Kawai, Lindenberg and Van den Broeck, *EPL* **89**, 20003 (2010), [author text](https://arxiv.org/pdf/0909.3618), p. 2, Eqs. (1)–(3); p. 6, concluding discussion | A driven single-level dot has time-dependent level energy and constant wide-band coupling. Ideal jumps represent ramps short versus tunneling but long versus inverse level spacing and reservoir relaxation. This supplies a drive convention and its limit, not a coupled-device pulse certificate. |

These sources share compatible ingredients of a master-equation modeling
tradition. They do not all analyze our protocol, and their different
nonequilibrium operating regimes are not imported together.

## 2. State, reservoirs and transition law

Retain one fermionic occupation per dot, $n_i\in\{0,1\}$. In the spinless
model, there is one retained state for each occupation pair. Write

$$
 H_S(t)=e_1(t)n_1+e_2(t)n_2+Un_1n_2,\qquad U>0.
 \tag{1}
$$

Each dot exchanges particles with its own equilibrium reservoir through
a weak tunneling Hamiltonian. Reservoirs have fixed chemical potentials
$\mu_i$ and a common temperature $T>0$. There is no direct interdot
particle transfer. This is C3's one-reservoir architecture with C1's
explicit spinless Hamiltonian. Multiple leads per dot, as in C1/C2,
reduce to the same occupation generator when their Fermi functions agree;
their bare rates then add. We select the simpler single-reservoir case.

Define $\epsilon_i=e_i-\mu_i$, $\beta=(k_BT)^{-1}$ and the grand energy

$$
 \mathcal E_t(n)=\epsilon_1(t)n_1+\epsilon_2(t)n_2+Un_1n_2.
 \tag{2}
$$

To sequential order, only one occupation changes at a time. With $j\ne i$,

$$
 \begin{aligned}
 q_i(0\to1\mid n_j;t)&=\gamma_i(n_j,t)f(\epsilon_i(t)+Un_j),\\
 q_i(1\to0\mid n_j;t)&=\gamma_i(n_j,t)[1-f(\epsilon_i(t)+Un_j)],\\
 f(E)&=(1+e^{\beta E})^{-1}.
 \end{aligned}
 \tag{3}
$$

Rates here have units of inverse time. The same positive bare factor on
the two directions of an edge is part of the sequential model. The
selected wide-band subfamily sets $\gamma_i(n_j,t)=\Gamma_i>0$.
This does not make each directional rate constant: its Fermi factor
changes with energy. It makes their sum $\Gamma_i$.

The inherited regime excludes unresolved spin/orbital/valley multiplicity,
additional accessible charge states, appreciable coherent interdot
hybridization, and higher-order tunneling corrections. It requires
$\hbar\Gamma_i\ll k_BT$, sufficiently isolated retained levels, and
short reservoir memory. Spinless is a declared theoretical branch;
Coulomb blockade by itself does not remove degeneracy. The published
diode's particular cotunneling estimates are not quantitative error bounds
for our operating point.

**Three distinct choices:** flat coupling versus transition energy is the
wide-band specialization; $\Gamma_1=\Gamma_2$ is an additional parameter
choice; leaving both couplings unchanged under a gate drive is a control
idealization. C6 explicitly makes the last choice for an energy-driven
level. In our Hamiltonian contract the gate changes diagonal level energies
while the tunneling Hamiltonian remains fixed. Electrostatic compensation
alone does not prove that a fabricated barrier behaves this way.

## 3. Equilibrium and the switch mapping are deductions

At each held field, (3) gives

$$
 \frac{q_i(0\to1\mid n_j)}{q_i(1\to0\mid n_j)}
 =e^{-\beta(\epsilon_i+Un_j)}.
 \tag{4}
$$

Consequently $\pi(n)\propto e^{-\beta\mathcal E(n)}$ satisfies ordinary
detailed balance. This is our equilibrium specialization, not a claim
that the five coupled-dot papers study equilibrium. The two $\mu_i$ need
not be equal: each dot plus its own reservoir conserves its separate
particle number, so no inter-reservoir particle-transfer affinity exists.
In a multiple-lead version, leads attached to the same dot must have equal
chemical potential and temperature for this reduction.

Set

$$
 S=2n_1-1,\quad Z=1-2n_2,\quad
 \epsilon_2=-U/2,\quad \epsilon_1(h)=-U/2-2k_BT h,
 \quad J=\beta U/4.
 \tag{5}
$$

Then $\beta\mathcal E_h=-JSZ-hS-J-h$. The additive term does not affect
populations, and

$$
 q_S=\frac{\Gamma_1}{1+e^{2S(h+JZ)}},\qquad
 q_Z=\frac{\Gamma_2}{1+e^{2JSZ}},\qquad
 \pi_h=\frac{\pi_0e^{hS}}{\pi_0(e^{hS})}.
 \tag{6}
$$

This recovers the repository's heat-bath generator exactly within the
selected model. The opposite convention for $Z$ converts repulsive charge
coupling into positive $J$. Charge occupations are time-even labels;
detailed balance here describes the occupation process, not a claim about
time reversal of every omitted microscopic variable.

For the current four-word fixture choose $J=\log3$, $H=\log2$,
$\Gamma_1=\Gamma_2=\Gamma$, and plateau durations $5/(4\Gamma)$.
Thus $U=4k_BT\log3$ and the controlled energy change is
$\Delta\epsilon_1=-2k_BT\log2$. These are our dimensionless parameter
choices. They specify no fabricated temperature, tunneling frequency or
precision. The older $H=\log3$ fixture remains a different operating point.

## 4. Compensated control follows from the capacitance model

Here is an explicit derivation from C3, Eq. (8), rather than an assertion
that a local gate has no cross-coupling. Use its mutual capacitance $C$,
reservoir capacitances $C_1,C_2$, gate capacitances $C_{G1},C_{G2}$, and put

$$
 c_i=C+C_i+C_{Gi},\qquad \Delta_C=c_1c_2-C^2>0.
$$

Keep reservoir voltages, capacitances, bare orbital offsets and the
electron-occupation branch fixed. Differentiating the published charging
energy gives

$$
 \begin{pmatrix}\delta\epsilon_1\\\delta\epsilon_2\end{pmatrix}
 =-\frac e{\Delta_C}
 \begin{pmatrix}c_2C_{G1}&CC_{G2}\\CC_{G1}&c_1C_{G2}\end{pmatrix}
 \begin{pmatrix}\delta V_{G1}\\\delta V_{G2}\end{pmatrix},
 \qquad U=\frac{e^2C}{\Delta_C}.
 \tag{7}
$$

The lever-arm determinant is $e^2C_{G1}C_{G2}/\Delta_C>0$ when both
gates couple. In particular,

$$
 \delta V_{G2}=-\frac{CC_{G1}}{c_1C_{G2}}\delta V_{G1}
 \quad\Longrightarrow\quad
 \delta\epsilon_2=0,\qquad
 \delta\epsilon_1=-\frac{eC_{G1}}{c_1}\delta V_{G1}.
 \tag{8}
$$

With fixed coefficients this is also a finite linear displacement. It
implements (5) while leaving $U$ fixed. Its domain is the constant-
capacitance, fixed-level model over the selected voltage interval, with
the same four retained occupations. It supplies no measured compensation
accuracy or barrier invariance.

C4's Appendix A is not a substitute for this argument. Its reservoir
voltage changes also move chemical potentials; when the conducting leads
are unbiased, only their voltage difference from the other reservoir
controls the two relative addition energies. An invertible map for
absolute electrostatic energies alone would not establish our control.

For the mathematical pulse protocol, change $h$ at a boundary without
changing the occupation label, then use $e^{tQ_h}$ on each plateau.
C6 supplies a published interpretation of this convention: a ramp must
be long compared with omitted level/reservoir dynamics and short compared
with tunneling. Together with C1's Markov hierarchy, a compatible regime
is schematically

$$
 \max(\tau_{\rm reservoir},\hbar/\Delta_{\rm omitted})
 \ll\tau_{\rm ramp}\ll(\Gamma_1+\Gamma_2)^{-1}.
 \tag{9}
$$

This is a timescale interpretation, not a numerical ramp guarantee.
The exact step protocol is the reduced-model limit. Finite ramp dynamics
need an explicit bound before inheriting a finite-accuracy certificate;
a plateau timing tolerance alone does not bound arbitrary slew effects.

## 5. Observation and the target/rival boundary

The basic observables are state probabilities. With
$M_s=\operatorname{diag}\mathbf1_{S=s}$, initial law $\nu$, and plateau
product $P_w$, the ideal pair law is

$$
 P_w(s,t)=\nu M_sP_wM_t\mathbf1.
 \tag{10}
$$

It specifies the distribution of two occupation labels in the modeled
process. It does not postulate a physical meter that obtains them without
disturbance. Population means and these correlations can be the subject
of a theoretical prediction task before an instrument is supplied.
Identifying (10) with experimental recorded bits is a separate step.

The target has the four states and rates above. An ordinary rival is
broader: arbitrary finite states, deterministic binary label, fixed
reversible field kernels and strictly positive stationary laws with the
same force relation $\widehat\pi_h\propto\widehat\pi_0e^{h\widehat S}$.
It is not restricted to two dots, heat-bath kinetics, the target graph,
equal rates, or the target's hidden preparation. The four-word lower
bound permits a different arbitrary starting distribution for every word.

The force relation expresses retention of the same energetic control,
not a universal fact about fitted hidden-state models. For a fixed
equilibrium partition that never mixes different observed labels,
summing microscopic Boltzmann weights immediately gives this same tilt
for each coarse state. Such a partition need not have autonomous Markov
dynamics; the [equilibrium-reduction note](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md)
separates force inheritance from dynamical closure. Arbitrary predictors with unrelated field-dependent stationary
laws are outside this comparison. The source-backed target does not
establish the interface for every conceivable rival by observation alone.

General stationary predictors retain that interface but may circulate
probability. Their three-state construction is a predictive model, not
an asserted three-state single-bath quantum-dot device. A physical
implementation and its nonequilibrium resources would need separate work.
Persistent detector/controller memory that changes active kernels cannot
be omitted from a physical Markov state count.

## 6. Definitive scope of the inherited results

| Existing result | Decision under this model contract |
| --- | --- |
| [Minimal four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md) | Lead with the equal-attempt model for every finite positive coupling, field and pair of dwell times. Its exact state minima are three and four, with a positive parameter-dependent TV interval. This is an ideal population-law result; the following numerical neighborhoods are separate extensions. |
| [Exact controlled-mean theorem](FAMILIAR_SWITCH_STRUCTURE.md) and [charge mapping](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) | Retain as physical-model prediction results. The equal-rate model supplies the original theorem; the charge note separately gives its stated unequal-rate extension. These are not complete trajectory-law realizations. |
| [Four-word endpoint state minimum](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md) | Retain as the principal finite-task result: the ideal laws for $0,H,0H,H0$ have general minimum three and ordinary minimum four through pair-law TV error $.001$. The nominal sourced target is inside the certified family. Target equilibrium is still used; arbitrary rival preparations are allowed. |
| Independent one-percent edge-prefactor box | Retain as a mathematical robustness neighborhood inside the broader reversible Fermi-rate form (3). The percentages are our certified tolerance, not a measured material property. Exact constant prefactors are sufficient for the core claim. |
| [Nine-million-trial ideal-bit test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) | Retain as a statistical consequence if its ideal records and conditional execution premises are available. The model contract alone does not build their acquisition or certify a laboratory trial count. |
| Target relaxation/reset calculations | Retain as consequences of the stipulated generator. They do not give arbitrary rivals a mixing bound, establish independent trials, or account for acquisition disturbance. |
| Protected/repeated readout, [endpoint registration](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md), and relative-force tolerances | Retain as conditional extensions. The community generator does not supply their instrument contracts, uniform classification bounds, leakage budgets, preparation preservation, or numerical force error. |

The resulting claim is physically grounded at the model level: a standard
equilibrium coupled-dot process has a smaller stationary predictive model
than any ordinary reversible model preserving the specified control and
endpoint task. The remaining experimental question is whether a compatible
instrument and finite control implementation deliver the requisite records.
It is not answered by appending unrelated best-performance detector
examples. This contract does not settle novelty, hardware feasibility,
thermodynamic implementation cost, or publication readiness.
