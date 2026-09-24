# Integrating endpoint registration: physical source audit

[Charge-state model](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) ·
[Preparation-free identity](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) ·
[Earlier platform audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) ·
[Earlier protected instrument](FAMILIAR_SWITCH_PROTECTED_READOUT.md)

**Focused primary-source audit, 24 September 2026.** Integrating a charge-sensor
signal, suppressing tunneling during readout, and compensating gate crosstalk
have established precedents. None of the sources below demonstrates this
repository's full experiment or its uniform conditional error budget.
The eight full texts were inspected at the specified locations. Different
devices' performance numbers are not combined into an achieved specification.

## 1. What the proposed registration model assumes

The proposed alternative to repeated binary readings uses one integration
window at each endpoint. A sufficient conditional model, after subtracting a
fixed threshold baseline, is

$$
 dY_t=(a_tS_t+b_t)\,dt+dM_t,\qquad
 a_t\ge a_{\min},\quad |b_t|\le b_{\max},\quad
 g=a_{\min}-b_{\max}>0,
 \qquad \langle M\rangle_T\le vT.
$$

Here $M_0=0$ and $M$ is a **continuous local martingale in the joint
system-and-detector filtration**, including the prior record. The bounds are
uniform conditional premises, not fitted average noise levels. Hidden charge,
history, gain drift and asymmetric noise can be permitted within these
bounds. No fixed binary symmetric channel, fresh independent bit errors or
hidden-charge-independent spectrum is required.

If the conditional hazard of a true-sign change throughout the window is
at most $\kappa$, thresholding $Y_T$ has the sufficient error bound

$$
 p_{\rm end}\le \exp[-g^2T/(2v)]+\kappa T.
$$

This follows by separating paths with a sign change from the continuous
martingale tail on the remaining paths; it does not condition the noise law
on the absence of a jump. The bound applies to either endpoint of that
window. It is our model calculation, not an experimental result in the
papers below. Writing $\theta=v/g^2$ and $\alpha=g^2/(2v)$, the selected
prescription $T=32\theta$ gives $\alpha T=16$. Together with
$\kappa T\le4\times10^{-6}$ it implies
$p_{\rm end}<5\times10^{-6}$ and requires
$\alpha/\kappa\ge4\times10^6$ when $\kappa>0$.
That ratio is a demanding specification, not a demonstrated device value.
Here the displayed constant-rate ratio assumes the full acquisition span
is the integration time. With closure, settling, release or dead time,
let the full span be $\tau\ge T$ and replace $\kappa T$ by
$\kappa\tau$, or use a separate bound $\Lambda$ on any sign change
throughout that full operation. All such exposure consumes the same
$4\times10^{-6}$ leakage budget.

Quadratic variation alone does not give this Gaussian exponential bound
for a discontinuous compensated Poisson martingale. A counting model needs
its own jump/cumulant bound, or a justified diffusion approximation.
Likewise, arbitrary colored noise does not automatically become a martingale
by integrating it. A bounded predictable part may enter $b_t$; the remaining
innovation must meet the stated conditional requirement.

## 2. Eight component-level comparisons

### Integrated charge-dependent current

**A. N. Korotkov**, “Continuous quantum measurement of a double dot,”
*Physical Review B* **60**, 5737 (1999).
[DOI](https://doi.org/10.1103/PhysRevB.60.5737),
[full extended author version](https://arxiv.org/pdf/cond-mat/9909039).
Inspected pp. 1–3, Eqs. (1)–(5), (9)–(10).

For a weakly responding tunnel-point-contact detector, sufficiently low
frequencies and zero interdot tunneling, the charge-conditioned averaged
current is Gaussian with variance $S_I/(2T)$. Centering the two current
levels gives the frozen-charge special case with
$a=|I_2-I_1|/2$ and $v=S_I/2$. The underlying shot noise and the
low-frequency approximation are explicit. This supports a standard model
for the integrated record; it does not certify uniform $g,v,\kappa$ for
another device, arbitrary hidden variables or every past history.

### Finite bandwidth can conceal actual charge transitions

**O. Naaman and J. Aumentado**, “Poisson Transition Rates from Time-Domain
Measurements with a Finite Bandwidth,” *Physical Review Letters* **96**,
100201 (2006).
[DOI](https://doi.org/10.1103/PhysRevLett.96.100201),
[full preprint](https://arxiv.org/pdf/cond-mat/0511026).
Inspected all four pages, especially Fig. 2 and Eqs. (1)–(3).

The authors include the detector's recorded state in a transition model
and compare it with quasiparticle-tunneling measurements. Missed short
excursions change the observed dwell-time distribution and bias inferred
transition rates downward. The detector and underlying system need not
change state simultaneously. Consequently, a small observed switching rate
alone cannot certify our upper hazard bound $\kappa$. A measurement-chain
model and uncertainty allowance would be needed. The paper does not give
a universal correction for arbitrary detector memory.

### Asymmetric noise and correlations introduced by filtering

**D. Keith et al.**, “Benchmarking high fidelity single-shot readout of
semiconductor qubits,” *New Journal of Physics* **21**, 063011 (2019).
[DOI](https://doi.org/10.1088/1367-2630/ab242c),
[full preprint](https://arxiv.org/pdf/1811.03630).
Inspected pp. 9–10, Eqs. (50)–(58), and Supplement II, p. 16,
Eqs. (S5)–(S6). The publisher full text was not retrieved.

The Gaussian example permits different variances for the two detector
levels. Its filter analysis explicitly explains that filtered samples are
correlated, so independent-sample distribution products no longer apply.
The paper treats peak detection after spin-to-charge conversion, not our
integrated-sign classifier. Its relevance is the need to model bandwidth,
sampling and noise spectrum together. A histogram fit or an effective
sample-count correction does not establish the joint-filtration martingale
bound used above.

### Fast charge discrimination by rf reflectometry

**E. J. Connors, J. J. Nelson and J. M. Nichol**, “Rapid High-Fidelity
Spin-State Readout in Si/SiGe Quantum Dots via rf Reflectometry,”
*Physical Review Applied* **13**, 024019 (2020).
[DOI](https://doi.org/10.1103/PhysRevApplied.13.024019),
[full preprint](https://arxiv.org/pdf/1910.08755).
Inspected Section III, pp. 3–4, Eqs. (1)–(3), Fig. 3, and the
ring-up discussion on p. 5.

The separate charge-discrimination experiment tunes reservoir tunneling
to about 10 Hz and fits two voltage distributions with separate variances.
It reports charge fidelity above 99.9% at 300 ns integration. The latching
experiment separately discards an initial interval for resonator ring-up
and charge mapping. These are useful integration and settling precedents.
They do not supply a $5\times10^{-6}$ conditional error bound or a
uniform hazard estimate for our two interacting occupations.

### Closing a barrier before charge readout

**T. Struck et al.**, “Spin-EPR-pair separation by conveyor-mode single
electron shuttling in Si/SiGe,” *Nature Communications* **15**, 1325 (2024).
[DOI and publisher full text](https://doi.org/10.1038/s41467-024-45583-7).
Inspected Results, “Device Layout and Method” and “Pulse sequence,”
especially Fig. 1 stages P and F.

The experiment decouples the loading reservoir, performs spin-to-charge
conversion and then closes the interdot barrier to hold the resulting
charge configuration while reading the SET current. This is a direct
precedent for a barrier-held readout interval. The device contains more
electrons and different dynamical operations than our target. The paper's
use of charge freezing does not establish zero leakage or the proposed
uniform $\kappa T$ bound. That bound must include unwanted reservoir,
interdot and detector-induced transitions in the specified device.

### Dynamic latching and gate compensation

**S. Park et al.**, “Single shot latched readout of a quantum dot qubit
using barrier gate pulsing,” *npj Quantum Information* **11**, 148 (2025).
[DOI and publisher full text](https://doi.org/10.1038/s41534-025-01094-x).
Inspected Results, Eqs. (1)–(4), Fig. 2, and Methods,
“Detailed description of the voltage pulses” and “Measurement.”

Barrier pulses separately control loading, latch lifetime and reset.
Synchronized plunger pulses compensate the barrier gate's electrostatic
crosstalk. The paper also treats finite bandwidth, unequal fitted signal
variances and the lifetime/reset tradeoff. This supports counting the
barrier actuator, compensation pulses and measurement time as resources.
The latch uses an extra charge configuration and cotunneling, so it
cannot be inserted silently into our four-state target. Compensating one
observed transition does not establish preservation of every conditional
hidden equilibrium law or the exact stationary force relation.

### A detector can change occupation dynamics

**D. Taubert et al.**, “Telegraph Noise in Coupled Quantum Dot Circuits
Induced by a Quantum Point Contact,” *Physical Review Letters* **100**,
176805 (2008).
[DOI](https://doi.org/10.1103/PhysRevLett.100.176805),
[full preprint](https://arxiv.org/pdf/0801.4002).
Inspected all four pages, especially Figs. 1–3 and the conclusion.

A biased QPC induces inelastic transitions and charge exchange that would
otherwise be suppressed in the coupled-dot circuit. This is population
backaction, not merely a wrong electronic label. It motivates including
detector-on transitions in $\kappa$ and separately analyzing the target's
nonselective initial disturbance. Absence of visible telegraph noise in
one operating region is not evidence of absent backaction elsewhere.
No universal rate or disturbance bound transfers from this device.

### Hidden-charge response and population backaction in a close geometry

**M. S. Ferguson et al.**, “Measurement-induced population switching,”
*Physical Review Research* **5**, 023028 (2023).
[DOI](https://doi.org/10.1103/PhysRevResearch.5.023028),
[publisher full PDF](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.5.023028).
Inspected pp. 2–4, Appendix A.1 and A.4, Fig. 9, and Appendix B.1–B.2.

Two capacitively coupled dots exchange charge with their respective leads;
a third dot senses their occupations. Four distinct sensor-conductance
levels resolve all four target configurations, and detector bias changes
the occupation statistics. Gate compensation maintains sensor sensitivity
but does not eliminate backaction. For our relaxed model, hidden-charge
response may enter $b_t$: the necessary requirement is that both hidden
configurations of each visible sign stay on its correct side of a common
threshold with a uniform margin. Neither this geometry nor its fitted
backaction model certifies that margin, noise bound or equilibrium
preservation for the proposed operating point.

## 3. Boundary between a physical model and a demonstrated experiment

The oracle signs for the proposed extension are taken **after** the initial
window and **before** the final window. Initial measurement disturbance
can then be absorbed into the rival's arbitrary preparation. Exact sign
protection of every rival is unnecessary; the conditional registration
error bound remains an interface premise for the comparison class.
Characterizing one target device alone does not establish that premise
for all rival descriptions.

For target power, the relevant initial condition is preservation, or a
budgeted displacement, of the nonselective hidden marginal $\pi D$.
Scaling both directional rates on each edge preserves detailed balance
and hence $\pi$; this is an algebraic sufficient condition, not a property
inferred from barrier pulsing. Gate-energy shifts, asymmetric rate changes
and detector heating need their own bounds. Detector or controller memory
that changes the subsequent field kernels must also be represented or
excluded by the stated model. The published components support investigating
this conditional implementation; they establish neither the complete
performance specification nor a demonstrated predictive-state advantage.
