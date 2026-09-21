# Prior-art and novelty audit

[Repository overview](../README.md) · [Exact theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

**Updated 22 September 2026.** This is a bounded audit, not a certification of novelty. A derivation obtained independently here may still be known. Sources were revisited during repository initialization; the depth of verification is recorded below rather than inferred from a citation's presence.

## Claims being screened

The exact target combines: equality of the complete passive visible Markov path law; a specified reversible field-dependent rate rule; matching static and dynamic linear mean response; and an all-size sharp separation between passive state count and exact cubic-response state count.

The extension retains nonvanishing total response with bounded coupling, then gives a protocol-uniform cubic approximation certificate and an explicit reversible Markov realization whose size is independent of the original state count. The coefficient tolerance, known kinetic kernel, and freedom to change microscopic rates are essential assumptions.

The broad claims below are **not** prospective contributions: hidden kinetics affect nonlinear response; one can coarse-grain response; Volterra kernels admit state realizations; positive sums of exponentials can be approximated by shorter sums.

## Established response theory

**Urna Basu, Matthias Krüger, Alexandre Lazarescu, Christian Maes, “Frenetic aspects of second order response” (2015).** Physical Chemistry Chemical Physics 17, 6653–6666. [Primary full text](https://arxiv.org/html/1410.7450v2), [DOI](https://doi.org/10.1039/C4CP04977B).

The paper distinguishes thermodynamic and time-symmetric kinetic rate changes and shows that nonlinear response depends on dynamical information not fixed by equilibrium linear response. The primary abstract and full-text framework were retrieved again in this pass. Consequence: the kinetic field factor and the general hidden-kinetics message are established, not new here.

**Gregor Diezemann, “Nonlinear response theory for Markov processes: Simple models for glassy relaxation” (2012).** Physical Review E 85, 051502. [Primary record](https://arxiv.org/abs/1203.1785), [DOI](https://doi.org/10.1103/PhysRevE.85.051502).

The primary abstract explicitly states a master-equation perturbation framework through third order and sensitivity of cubic response to kinetic field coupling. The initial checkpoint recorded full-text inspection; this pass reconfirmed the primary record and abstract. Consequence: cubic response formulas and different nonlinear responses despite matching linear diagnostics are established.

**Fenna Müller, Urna Basu, Peter Sollich, Matthias Krüger, “Coarse-grained second-order response theory” (2020).** Physical Review Research 2, 043123. [Primary record](https://arxiv.org/abs/2005.05169), [DOI](https://doi.org/10.1103/PhysRevResearch.2.043123).

The primary abstract describes exact second-order coarse response under time-dependent perturbations, an extrapolation from single-step response measurements, and an exactly solvable four-state example. The initial checkpoint reported that example's passive coarse process as non-Markovian. The HTML full text was not retrievable during this pass, so theorem-level comparison must be revisited; the abstract alone does not settle the relation to our exact passive Markov property.

## Aggregation and realization

**Luca Cardelli, Radu Grosu, Kim Guldstrand Larsen, Mirco Tribastone, Max Tschaikowski, Andrea Vandin, “Lumpability for Uncertain Continuous-Time Markov Chains” (2021).** QEST 2021, 391–409. [Institutional record](https://vbn.aau.dk/en/publications/lumpability-for-uncertain-continuous-time-markov-chains/), [DOI](https://doi.org/10.1007/978-3-030-85172-9_21).

Bibliographic and abstract-level inspection identifies robust lumpability under time-varying uncertain rates. Full theorem-level comparison is pending. The block-uniform preservation observation in our note is a baseline consequence of ordinary lumpability, not a new theorem.

**A. E. Frazho, “A Shift Operator Approach to Bilinear System Theory” (1980).** [Primary publisher record](https://epubs.siam.org/doi/10.1137/0318049).

The publisher abstract describes bilinear realization of Volterra input-output maps and minimality linked to reachability and observability. Only the publisher abstract was inspected in this pass. A theorem-level comparison remains required. The pole-location lemma must be treated as standard realization reasoning, not an independent innovation.

**Peter Benner and Pawan Goyal, “Balanced Truncation Model Order Reduction For Quadratic-Bilinear Control Systems” (2017 preprint).** [Primary full text](https://arxiv.org/html/1705.00160v1).

The primary record and framework describe Volterra-based Gramians and reduced models for quadratic-bilinear systems. This establishes an adjacent reduction framework; it does not by itself settle positive Markov realization or the specific passive/response separation. Detailed mapping of our coefficient system into this framework remains pending.

## Positive exponential approximation

**Yohei M. Koyama, “Exponential sum approximations of finite completely monotonic functions” (2023, version 3).** [Primary full text](https://arxiv.org/html/2301.08931v3).

Sections 1–2 discuss positive exponential approximation of Laplace transforms with finite positive spectral intervals, previous approximation theorems, Gaussian quadrature, and geometric error bounds under specified conditions. These sections were retrieved in this pass. Our elementary midpoint quantization uses a damped integral norm, compactified rates, and no uniform original spectral interval; this difference is a comparison task, not proof of novelty. A claimed new exponential approximation algorithm would be unjustified.

The explicit paired-state reversible realization must also be checked against positive realization, hyperexponential/phase-type representations, and reversible network synthesis. The current construction proves existence for our use; it does not establish novelty or minimality of that construction.

## Recent sources carried forward, with access limitations

**Jiming Zheng and Zhiyue Lu, “The Memory Hidden in Response Fluctuations: Trajectory-Level Fluctuation-Response Theory and Inequalities for Non-Markovian Jump Dynamics” (2026).** [Primary record](https://arxiv.org/abs/2608.20328).

Existence and the primary abstract were reconfirmed through search. The abstract explicitly discusses a response-heterogeneity gap and response-sufficient memory coordinates. Direct full-text retrieval failed in this pass. Specific statements about its hidden-state example from the initial checkpoint are therefore not used here as newly verified theorem-level comparisons. Response sufficiency is not a new general framing of this repository.

**Abhishek Chowdhury, “Hidden kinetic correlations control collective phases of entropy-conditioned histories” (2026).** [Primary record](https://arxiv.org/abs/2609.16355).

The title and author were reconfirmed in primary arXiv listings, but direct abstract/full-text retrieval failed in this pass. The initial checkpoint described identical ordinary visible path laws with different entropy-conditioned dynamics. That substantive comparison remains a carried-forward lead requiring full-text reinspection, not evidence freshly verified here. Do not claim either precedence or distinction on the basis of the title alone.

The failed retrievals are access limitations, not evidence that these papers do not exist. No novelty conclusion depends on their absence.

## Open publication gates

The first gate is whether the exact sharp separation, bounded-signal variant, and cubic kernel characterization are already immediate instances of established realization or response results. The second is whether the finite-accuracy statement adds a useful operational distinction beyond generic positive exponential approximation. The third is a physical interpretation with the same actuator and observation assumptions, not an unsupported turbulence label.

The current $1/q$ certificate is not asserted optimal. A universal fixed-error lower bound growing with microscopic $N$ is incompatible with our constructive upper bound at bounded coupling and protocol amplitude. The next mathematical target is the dependence on tolerance and meaningful restrictions, not an attempt to rescue an invalid $N$-dependent claim.

No exhaustive citation graph, independent proof review, or journal assessment has been completed. The [current work order](../work_orders/CURRENT.md) turns these limitations into concrete next tasks.
