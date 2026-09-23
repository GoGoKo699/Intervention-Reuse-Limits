# Physical configurations, force control and the realization gap

[Kinetic/parity resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [Generalized-reversal boundary](GENERALIZED_REVERSAL_PREDICTION.md) · [Earlier kinetic source audit](KINETIC_PARITY_SOURCE_AUDIT.md) · [Interface perturbation analysis](PHYSICAL_INTERFACE_ROBUSTNESS.md)

**Primary-source assessment, 23 September 2026.** A recognizable model class is a force-controlled conformational network with one gateway configuration, many unresolved configurations and an occupancy readout. Chemical-number and overdamped configurational states have a specified ordinary physical reversal. A single applied force can produce the repository's equilibrium bias and heterogeneous activation rates simultaneously. This is a meaningful kinetic interpretation, but the inspected sources do not turn the constructed hard target family into an experimentally realized molecule or a microscopic device.

Nine primary papers below support different ingredients. The closest structural precedents are the enzyme model of Berezhkovskii et al. and the force-dependent conformational model of Diezemann et al. Bell's law supplies the simplest force parametrization; Dudko–Hummer–Szabo and Falasco–Esposito supply essential limits on its microscopic interpretation. No source is used to certify the complete architecture, novelty or journal suitability. Manuscript drafting remains deferred.

## 1. A precise single-force interpretation

The following is an explicit model translation, not a physical realization theorem attributed to the papers. Let $f$ be a force conjugate to extension $x$, let $\ell>0$ be a length, and set $h=f\ell/(k_BT)$. Write well and transition-state free energies as

$$
E_x(f)=E_x^0-fx_x,\qquad
W_{xy}(f)=W_{xy}^0-fx_{xy}^{\ddagger},\qquad
q_{xy}(f)=\nu_{xy}\exp\!\left[-\frac{W_{xy}(f)-E_x(f)}{k_BT}\right],
\tag{1}
$$

with symmetric $W_{xy}^0=W_{yx}^0$, $x_{xy}^{\ddagger}=x_{yx}^{\ddagger}$ and $\nu_{xy}=\nu_{yx}$. This assumes fixed effective extensions and force-independent attempt frequencies over the allowed force range. Choose

$$
x_A=-\ell,\qquad x_i=\ell,\qquad x_{Ai}^{\ddagger}=g_i\ell,
\qquad E_A^0=0,\qquad E_i^0=-k_BT\log\mu_i.
\tag{2}
$$

Calibrate the external barriers so $q_{iA}(0)=k$. Detailed balance then gives $q_{Ai}(0)=k\mu_i$, and (1) yields exactly

$$
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{iA}(h)=k e^{(g_i-1)h}.
\tag{3}
$$

Taking $x_{ij}^{\ddagger}=\ell$ on internal edges makes their activation energies independent of force, hence keeps $K$ fixed. A reversible $K$ can be represented at rate level by symmetric internal barriers because $\mu_iK_{ij}=\mu_jK_{ji}$. Edges with zero rates are omitted. The target values $|g_i|\le9/100$ place the external transition states near the midpoint between the two extension levels.

Thus one force suffices: no independent operation of well energies and barriers is required. The force-controlled process can be ordinarily reversible at every fixed force while dissipating during a changing force protocol. The fixed-force stationary weights are proportional to $(e^{-h},\mu_i e^h)$.

This translation makes additional assumptions visible. All unresolved wells must share an extension, all internal saddles must share that extension, passive escape rates must coincide, and a large specified network must be realizable with those properties. Equation (1) assigns graph energies and barriers; it does not construct a smooth molecular landscape with controlled errors, fixed spatial dimension, accessible force range or practical parameter precision. Naming graph states as conformations does not resolve those requirements.

## 2. Exact passive reduction and two limits on simpler controls

These deductions use the row-generator convention and can be checked directly.

At zero force, $q_{Ai}=k\mu_i$ and $q_{iA}=k$. The total rate from $A$ into the hidden block is $k$ and the return rate from every hidden state is $k$. Therefore the visible partition is strongly lumpable, with generator

$$
Q_{\rm vis}=\begin{pmatrix}-k&k\\k&-k\end{pmatrix}.
\tag{4}
$$

This gives the entire two-state path law for every initial microscopic law with the same visible initial law. Equivalently, for any entrance distribution $\rho$, the hidden-visit survival is

$$
\rho e^{t(K-kI)}\mathbf1=e^{-kt},
\tag{5}
$$

because $K\mathbf1=0$. This is stronger than merely having an exponential dwell time from one specially chosen entrance distribution.

Heterogeneous return rates replace scalar killing by $k\operatorname{diag}(b_i(h))$. If the $b_i(h)$ differ, strong lumpability fails; dwell times can then depend on hidden dynamics. A single gateway still makes successive complete excursions independent at a fixed field. **Loss of Markov lumpability does not imply loss of fixed-field renewal.** Under time-dependent control, excursion laws additionally depend on their entry times and the future protocol.

Two tempting physical simplifications remove the mean-prediction effect:

1. **Only ligand concentration changes, with equal constant off-rates.** In a simple binding model $q_{Ai}=k\mu_i c(t)/c_0$, $q_{iA}=k$, the visible process remains exactly two-state under every concentration protocol. Heterogeneous entrance weights alone do not expose $K$ through this readout while all return rates coincide.
2. **Only barriers change while a common equilibrium law remains fixed.** If $\pi Q(u)=0$ for every control $u$ and the preparation is $\pi$, then $p(t)=\pi$ solves the driven master equation. Every endpoint mean stays constant, although trajectory statistics can change. This does not exclude a barrier-only relaxation experiment begun away from that common equilibrium.

The single-force model (1)–(3) avoids both restrictions: it changes the equilibrium block bias and makes the return barriers respond differently. These restrictions concern the specified task and preparation; they are not blanket impossibility claims about ligand sensing or barrier control.

## 3. Primary sources and exact scope

### A. A direct single-gateway enzyme model

**Alexander M. Berezhkovskii, Attila Szabo, T. Rotbart, M. Urbakh and Anatoly B. Kolomeisky, “Dependence of the Enzymatic Velocity on the Substrate Dissociation Rate,” Journal of Physical Chemistry B 121, 3437–3442 (2017; online 2016).** [DOI](https://doi.org/10.1021/acs.jpcb.6b09055) · [author-hosted published PDF](https://bpb-us-e1.wpmucdn.com/blogs.rice.edu/dist/2/12644/files/2022/09/acs.jpcb_.6b09055.pdf).

**Full text inspected:** §2, pp.3438–3439, Eqs.(6)–(15), and Appendix A. One free-enzyme conformation connects to $N$ bound conformations with arbitrary internal Markov kinetics, association rates $k_{\rm on}(i)c$ and dissociation rates $k_{\rm off}(i)$. Equation (13) factors survival as $S_{ES}(t)=e^{-k_{\rm off}t}S_{\rm cat}(t)$ when all off-rates agree. Removing catalytic exits gives (5); that specialization is our inference. The paper also warns that a directed example violates binding/conformational detailed balance.

**Scope:** close physical precedent for the gateway and common-off-rate mechanism. Its turnover results do not establish our force parametrization, equilibrium hard family or controlled-prediction separation. Replacing several free conformations by one requires the additional fast-mixing approximation stated in the paper.

### B. Gateway renewal and passive nonidentifiability

**Ophir Flomenbom, Joseph Klafter and Attila Szabo, “What Can One Learn from Two-State Single-Molecule Trajectories?”, Biophysical Journal 88, 3780–3783 (2005).** [DOI](https://doi.org/10.1529/biophysj.104.055905) · [primary preprint](https://arxiv.org/pdf/q-bio/0502006).

**Full text inspected:** preprint pp.4–6, Eq.(1), gateway characterization and the discussion of Fig.2B–C. Models with one on substate and many off substates generate renewal trajectories; different internal networks with the same two dwell distributions cannot be distinguished by passive trajectory analysis.

**Scope:** the single-gateway renewal mechanism and associated passive ambiguity are established. Renewal dwell distributions need not be exponential, so this result alone does not prove ordinary two-state Markov lumpability. It does not supply a reusable controlled-mean state-count lower.

### C. Force-sensitive barriers with force-independent hidden exchange

**Gregor Diezemann, Thomas Schlesier, Burkhard Geil and Andreas Janshoff, “Statistics of reversible bond dynamics observed in force-clamp spectroscopy,” Physical Review E 82, 051132 (2010).** [DOI](https://doi.org/10.1103/PhysRevE.82.051132) · [primary preprint, v2](https://arxiv.org/pdf/1005.1590v2).

**Full text inspected:** Eqs.(4)–(6) and Appendix C, pp.23–24, Fig.9 and Eqs.(C.1)–(C.4). The general model has conformational substates in two visible ensembles. The worked model assumes a common force-dependent equilibrium ratio across channels and internal exchange rates independent of force. It studies how force-dependent trajectory statistics reveal hidden dynamic disorder.

**Scope:** a particularly close precedent for separating equilibrium bias, heterogeneous crossing kinetics and fixed internal dynamics. The example has two conformations in each ensemble rather than one gateway, and addresses constant-force statistics. It supplies neither our exact passive calibration nor the large-family prediction lower.

### D. Bell's exponential force law is an explicit modeling approximation

**George I. Bell, “Models for the Specific Adhesion of Cells to Cells,” Science 200(4342), 618–627 (1978).** [DOI](https://doi.org/10.1126/science.347575) · [university-hosted publisher reprint](https://faculty.uml.edu/vbarsegov/teaching/bioinformatics/papers/bell.pdf).

**Full text inspected:** journal pp.622–623, Eq.(16), its receptor–ligand interpretation and Fig.6. Bell postulates a bond lifetime proportional to $\exp[(E_0-\gamma f)/(k_BT)]$, equivalently an exponentially force-dependent dissociation rate. The force coefficient represents the response of an activation barrier to load.

**Scope:** supports the force–activation-distance interpretation of the exponents in (3). It does not derive arbitrary network-wide force coefficients, equal passive off-rates or exactly fixed well and saddle positions from molecular mechanics. Equation (3) is exact in the stipulated Bell network, not a consequence that every molecular landscape obeys Bell's law exactly.

### E. Microscopic corrections and the force-rate approximation boundary

**Olga K. Dudko, Gerhard Hummer and Attila Szabo, “Intrinsic Rates and Activation Free Energies from Single-Molecule Pulling Experiments,” Physical Review Letters 96, 108101 (2006).** [DOI](https://doi.org/10.1103/PhysRevLett.96.108101) · [published-paper repository copy](https://zenodo.org/records/1233953) · [PDF](https://zenodo.org/records/1233953/files/article.pdf?download=1).

**Access and inspection:** the four-page published PDF was downloaded and read after the publisher fetch failed. Page 1 uses $U(x)=U_0(x)-Fx$ and identifies Bell kinetics as phenomenological. Equation (1) assumes an instantaneous-rate survival equation and states its failure at extreme pulling speeds or forces. Equation (3) incorporates finite-barrier shape effects and recovers Bell behavior in the stated limiting cases; pp.3–4 demonstrate substantial errors from an apparently adequate Bell fit.

**Scope:** supports single-force energy tilting while preventing a claim of exact general molecular kinetics. It concerns rupture over a barrier, not a proof that the repository's entire reversible graph has a microscopic realization or retains its lower bound under those corrections.

### F. Chemical states have a definite ordinary reversal

**Tim Schmiedl and Udo Seifert, “Stochastic thermodynamics of chemical reaction networks,” Journal of Chemical Physics 126, 044101 (2007).** [DOI](https://doi.org/10.1063/1.2428297) · [primary preprint, v2](https://arxiv.org/pdf/cond-mat/0605080v2).

**Full text inspected:** §II.A, Eqs.(1)–(8), and §V.A, Eqs.(44)–(50). The state is the vector of molecular counts; controlled chemostats are distinguished from retained species. Internal molecular states can be represented as different species. The reversed trajectory in Eq.(46) is $\widetilde n(\tau)=n(t-\tau)$, with the protocol reversed, not a permutation of chemical identities.

**Scope:** supplies a standard even-state thermodynamic interpretation. A one-molecule unimolecular network realizes a finite generator formally, but inventing one species for every engineered table state is not a synthesis or useful chemical implementation. Additional fuel reservoirs are needed for a nonreversible chemical predictor; their affinities and retained intermediates require explicit accounting.

### G. Barrier controls preserve equilibrium ratios but can alter kinetics

**Saar Rahav, Jordan Horowitz and Christopher Jarzynski, “Directed Flow in Nonadiabatic Stochastic Pumps,” Physical Review Letters 101, 140602 (2008).** [DOI](https://doi.org/10.1103/PhysRevLett.101.140602) · [primary full text, v2](https://arxiv.org/pdf/0808.0015v2).

**Full text inspected:** p.1 Arrhenius rates and Eq.(3), and the no-pumping argument surrounding Eq.(11). Well depths determine equilibrium weights; symmetric barriers determine additional kinetic information. In particular, when only barriers vary from an equilibrium preparation, the distribution remains at the same equilibrium. The separate theorem for fixed barriers concerns integrated cyclic currents.

**Scope:** supports the second restriction in §2 and the distinction between bias and kinetic control. It does not require two independent actuators: one physical parameter may move both wells and barriers. Its cyclic-current result does not prohibit nontrivial transient means when both vary, nor establish our state complexity.

### H. A controlled diffusion-to-jump derivation has explicit scale assumptions

**Gianmaria Falasco and Massimiliano Esposito, “Local detailed balance across scales: From diffusions to jump processes and beyond,” Physical Review E 103, 042114 (2021).** [DOI](https://doi.org/10.1103/PhysRevE.103.042114) · [primary full text](https://arxiv.org/pdf/2101.03968).

**Full text inspected:** §II.C, Eqs.(26)–(29), and the time-dependent extension at the end of §IV, preprint p.6. Weak-noise metastable coarse-graining, with weak nonconservative forcing, gives a jump-rate ratio involving basin free energies and work along a transition path. The extension to changing potentials requires preserved minima, high barriers and separation from intrabasin equilibration.

**Scope:** supplies a principled route from even overdamped configurations to thermodynamic jump rates. It does not prove uniform errors for our large graph, exact Bell exponents, or instantaneous force jumps. A physical approximation must be controlled on the witnessing protocol and accuracy scale, not merely at each isolated constant force.

### I. Physical parity is fixed by the retained variables

**Hyun Keun Lee, Chulan Kwon and Hyunggyu Park, “Fluctuation Theorems and Entropy Production with Odd-Parity Variables,” Physical Review Letters 110, 050602 (2013).** [DOI](https://doi.org/10.1103/PhysRevLett.110.050602) · [primary preprint, v1](https://arxiv.org/pdf/1209.0543v1).

**Access and inspection:** preprint under its earlier title, pp.1–3, Eqs.(3)–(11); the journal version was not available in full text. The introduction identifies positions and overdamped Brownian motion as even-variable examples, and momentum as odd. The generalized reversed path includes the state-parity operation; balance and stationary parity symmetry are separate conditions.

**Scope:** chemical identities or positions cannot be made odd merely because an advantageous word representation admits an involution. Conversely, if a proposed device retains actual odd variables, its physical class and entropy functional must include their reversal. The repository's generalized predictor remains a valid mathematical upper and an essential limit on any implementation-independent dissipation claim.

## 4. What would constitute a physical translation of the theorem

The even-state model class is meaningful: retained states are chemical compositions or overdamped conformations, the visible output is membership in one of two configurations or ensembles, and controls alter rates subject to a specified physical free-energy bias. The source record supports that vocabulary and several exact kinetic mechanisms.

For the repository's lower to describe this class, the hard targets must actually belong to it, and the allowed competitors must retain the stated hub interface, preparation and exit budget. A lower against the broader arbitrary-barrier ordinary-reversible class also holds against a physically restricted subclass. This restriction does not automatically establish a useful polynomial **physical** predictor: the existing stationary nonreversible upper still requires an implementation with the chosen even variables, fuel or other nonequilibrium resources, and every persistent state counted.

The next physical result should therefore quantify a model, not add names to its states. Useful concrete deliverables are:

- A force-controlled energy landscape or conformational mechanism that implements a separating target, with its well, saddle, rate and retained-state assumptions explicit.
- A controlled approximation bound from that mechanism to the jump model, including finite ramps and imperfect passive calibration at the relevant clock horizons. The [interface perturbation analysis](PHYSICAL_INTERFACE_ROBUSTNESS.md) addresses the mathematical transfer needed after such errors are supplied.
- A comparison class whose physical reversal is fixed in advance, together with a clear distinction between conformational state count, control complexity, fuel reservoirs and experimental learning cost.

At present, the exact Bell-network translation is a credible mesoscopic interpretation and a route to further work. It is not evidence that a known protein, receptor, chemical network or low-dimensional mechanical device exhibits the proved asymptotic separation. The existing mathematical result should retain that distinction.

## 5. Access and audit limits

All nine selected papers were accessed in full text and the stated passages inspected. Several were read as identified primary preprints; Bell and Berezhkovskii et al. were read as hosted publisher reprints. Dudko–Hummer–Szabo was read from the actual published PDF downloaded from its repository copy, not inferred from the abstract. Attempts to obtain Evans–Ritchie (1997) full text were unsuccessful in this audit, so it is not used as evidence here. Metadata-only and secondary summaries were not substituted for an inspected result.

The search was targeted, not exhaustive. No physical realization, experimental validation, priority certification or editorial assessment follows merely from these precedents.
