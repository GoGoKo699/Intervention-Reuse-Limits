# Physical assumptions must come from an established model

[Current work](../work_orders/CURRENT.md) · [Charge realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) · [Charge-platform sources](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) · [Measurement sources](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION_SOURCE_AUDIT.md)

**Research direction, 24 September 2026.** The owner requires the physical
model to be grounded in another community's established assumptions. We may
select a favorable recognized model and a consistent parameter regime. We
must not add unsupported physical capabilities merely because they make
the desired theorem or test work. This criterion governs the next research
step; the existing conditional proofs and certificates remain unchanged.

An accepted idealization can be a legitimate basis for theoretical physics.
Its status comes from its use and justification in an identifiable modeling
tradition, with a stated regime and known exclusions. Community use is not
evidence that every device satisfies it exactly. Conversely, a theory result
does not need an experimental demonstration before its physical model can
be assessed.

## 1. The order of reasoning

Start with a published state space, energy, reservoir model, transition law
and accessible controls. Specify the approximations under which they hold.
Then ask what prediction task and state-cost separation this model supports.
Add a detector only through a compatible published measurement model or an
explicit derivation from established physical premises. Quantitative hardware
feasibility follows after this model choice.

Our pulse sequence, observable comparison, proof and parameter selection can
be new. They need not already appear together in another paper. However,
combining models requires checking that their assumptions can hold together;
independent precedents for a fast sensor, a quiet system and barrier control
do not establish their compatibility in one experiment.

The key distinction is between a physical premise and a calculated
consequence. The requirement of endpoint error at most $5\times10^{-6}$ is
a sufficient condition derived for our current statistical test. It is
neither an established detector convention nor a demonstrated performance.
The numerical value need not have a precedent, but claiming that a physical
model supplies it requires an independently justified model and calculation.

## 2. A provisional model with direct community support

The existing charge realization is a credible starting candidate:
two single-level occupations coupled electrostatically, with weak reservoir
tunneling and no interdot particle transfer. The supporting community is
mesoscopic transport and stochastic thermodynamics of coupled quantum dots.

Five primary full texts establish the model family, including two PRL
papers. They do not all select identical kinetic parameters:

- **G. Bulnes Cuetara, M. Esposito and P. Gaspard**, *Physical Review B*
  **84**, 165114 (2011), [full text](https://arxiv.org/pdf/1105.5974).
  Section II, Eqs. (1), (12)–(20), gives the four-occupation model and
  derives Fermi charging/discharging rates in the weak-coupling,
  Born–Markov–secular regime. The bare couplings can differ between
  Coulomb-shifted transition energies. This supports the generator family,
  not automatic energy independence.
- **P. Strasberg et al.**, *Physical Review Letters* **110**, 040601
  (2013), [full text](https://arxiv.org/pdf/1210.5661).
  Pages 1–2 and Eqs. (1)–(5) give the capacitive two-dot architecture,
  four populations and rates proportional to $f$ and $1-f$. The text
  immediately following these equations identifies equal prefactors at
  the two transition energies with the common wide-band approximation.
  Its driven demon operating regime is not our equilibrium protocol.
- **T. Ruokola and T. Ojanen**, “Single-electron heat diode,”
  *Physical Review B* **83**, 241404(R) (2011),
  [full text](https://arxiv.org/pdf/1102.4187).
  Pages 1–2, Fig. 1, Eq. (1) and the rates following Eq. (2) give
  a particularly close template: one reservoir per dot, four retained
  charge states, no interdot particle transfer, and explicitly
  energy-independent tunneling strengths. The single-discrete-level
  branch uses Fermi functions; Eq. (3) also selects equal couplings.
  The paper separately treats metallic islands with different rates.
  Its temperature-biased diode regime and level labeling are not our
  gate-pulse operating point; their validity conditions must be checked
  anew for our specialization.
- **R. Sánchez and M. Büttiker**, “Optimal energy quanta to current
  conversion,” *Physical Review B* **83**, 085428 (2011),
  [full text](https://arxiv.org/pdf/1008.3528).
  Section II A, Eq. (2) and the following rates give the four-state
  sequential-tunneling generator with Fermi loading/unloading factors
  and $k_BT\gg\hbar\Gamma$. Section II retains energy-dependent
  transmissions for the conversion effect. This supports the family
  and identifies a boundary; it is not an example of the constant-rate
  specialization used in our target.
- **R. Sánchez, R. López, D. Sánchez and M. Büttiker**, “Mesoscopic
  Coulomb Drag, Broken Detailed Balance, and Fluctuation Relations,”
  *Physical Review Letters* **104**, 076801 (2010),
  [published full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.104.076801/fulltext).
  Page 076801-2, Eq. (4) and adjacent definitions give the four-charge-state
  generator, Fermi rates and occupation-dependent addition energies.
  Its drag mechanism uses energy-dependent tunneling prefactors and
  applied bias. Its discussion of three versus four retained charge
  states concerns that charge-transition topology and drag observable;
  it belongs in the close prior-art comparison, not in a claim that our
  arbitrary-predictor state minimum is already established or novel.

All five full texts were inspected at these locations for this alignment
note (four arXiv PDFs and the published 2010 PRL). These are direct
equation-level anchors, not a complete audit of every operational premise.
The broader [platform audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)
also contains experimental examples and incompatible alternatives; those
papers must not all be counted as endorsements of the same model.

Taking reservoirs at common equilibrium conditions is an explicit
specialization of the generator. Its equilibrium stationary law and
detailed balance then follow from the Fermi rate ratios. In the wide-band
subfamily, the forward and backward rates on an edge sum to its bare
coupling. These are our deductions within the published model, not new
physical assumptions attributed to the papers.

Equal attempt rates on the two dots are a further parameter choice;
wide-band behavior alone does not impose that equality. Keeping couplings
fixed under a gate pulse also needs its own control justification. The
[charge mapping](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) supplies the
algebraic correspondence to the switch model, but does not certify a
device's level isolation, compensation or detector disturbance.

## 3. Present assumption ledger

“Supported” below means supported as a model in the specified regime.
It does not mean experimentally certified for our proposed implementation.

| Item used in the project | Present status | Required treatment |
|---|---|---|
| Four charge occupations, capacitive interaction, sequential Fermi tunneling | Direct published model support, with restricted levels and weak coupling | Inherit the approximation regime; do not silently discard spin, orbital or coherent channels in a device |
| Energy-independent bare couplings | Named wide-band specialization with direct precedent | Distinguish constancy across energy from constancy under applied gates; equal couplings between dots are a further choice |
| Equilibrium reservoirs and ordinary detailed balance for charge populations | Consistent equilibrium specialization; charge labels describe even configurations | State the physical reversal and retained variables; do not extend to arbitrary odd auxiliary variables |
| Field coupled only to the observed occupation | Explicit controlled energy and comparison-interface premise | Justify the permitted control and compensation; it is not implied by detailed balance or by calling the signal a local field |
| The same stationary force rule for every rival | Essential restriction defining the state-cost comparison | Explain why this is the physical property a reusable reduced model must retain; no device-independent dimension claim |
| Fixed active dynamics conditional on the counted state | Markov model and control premise | Any retained detector/controller variable affecting future dynamics belongs in the model; model closure needs justification |
| Ideal endpoint pair laws | Well-defined observables of the mathematical state process | Keep the population-law theorem distinct from a physical readout construction |
| Uniform conditional endpoint errors and joint signal/noise/leakage bounds | Sufficient instrument premises; existing sources support components only | Derive from one compatible published detector/control model, or leave the operational extension conditional |
| Target initial acquisition preserves or nearly preserves its equilibrium marginal | Proved for the stipulated symmetric-rate construction | Establish that the full physical acquisition realizes this construction; barrier control alone does not establish it |
| One-percent kinetic box, force spread $1.001$, error budgets and nine-million-trial allocation | Our mathematical tolerances and design choices | Retain as conditional results; assess whether an inherited model supplies them rather than calling them community assumptions |
| Three-state stationary predictor with circulation | Constructive mathematical upper bound for the specified prediction task | A corresponding three-state physical device and its thermodynamic resources have not been established |

The null and target must be audited separately. A detector bound verified
only inside our chosen four-state target does not automatically justify
the same bound over the entire rival class. Likewise, finite target
equilibration does not imply that every slow rival equilibrates in that
time. The preparation-free lower avoids the latter promise; the detector
and shared-force premises remain substantive.

## 4. The next deliverable

Produce one assumption-by-assumption model comparison before adding more
tolerance extensions. The five primary examples above supply an initial
community basis for the generator family. Extend this set only where an
unresolved assumption requires further evidence, especially controls and
measurement. Identify the equations and approximation regimes actually
shared. Citation count is a breadth check, not a vote that establishes an
unsupported condition. The same set need not endorse our new pulse sequence
or computed constants.

For the selected model, the comparison must record:

1. Its published state space, energies, reservoirs, rates, controls and
   observation model, with exact source locations and exclusions.
2. Every specialization we make, why it is physically consistent, and
   which quantities are parameter choices rather than extra capabilities.
3. Which parts of our three-versus-four theorem and finite test survive
   without changing the inherited physical premises.
4. Any missing assumption, the claim that depends on it, and the available
   response: derive it, change the protocol/model, weaken the claim, or
   keep that operational extension explicitly conditional.

The assessment must permit an unfavorable answer. Do not progressively
add perfect protection, noise independence, invisible controller memory,
exact compensation or arbitrarily fast reset to rescue the current test.
Do not combine the best numerical performance from different devices.

An idealized state-process theorem can remain the principal contribution
if its model and task have independent physical standing. An experimental
proposal requires a compatible measurement and control description on top
of that foundation. Quantitative feasibility, scientific novelty and
publication significance are separate assessments. Manuscript drafting
remains deferred while this model comparison and close prior-art analysis
are resolved.
