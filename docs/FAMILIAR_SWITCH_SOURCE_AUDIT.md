# Familiar switch models: source and prediction-scope audit

[Two-switch prediction theorem](FAMILIAR_SWITCH_STRUCTURE.md) · [Protocol and accuracy exploration](FAMILIAR_SWITCH_PROTOCOLS.md) · [Physical realization audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) · [Single-force model](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) · [Matrix prediction principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) · [Simple-principles source audit](SIMPLE_PREDICTION_SOURCE_AUDIT.md)

**Primary-source audit, 23 September 2026.** Four-state force-clamp dynamic disorder and small coupled conformational switches are established model families. The [new repository theorem](FAMILIAR_SWITCH_STRUCTURE.md) proves a three-versus-four exact predictive-state separation for a positively coupled pair under a specified shared Gibbs tilt. Familiarity and classical mean closure alone do not imply that theorem. This note separates the published model ingredients, the new controlled-realization comparison, and the unresolved quantitative accuracy question. It is neither an exhaustive priority search nor a publication assessment.

## 1. What the familiar models do and do not supply

The force-clamp model has two conformations in each of two observed ensembles. A two-unit conformational pair has four configurations; a three-unit chain has eight. Observing one bit and applying a field only there uses conventional Ising interactions and heat-bath switching, but **local control is a stipulated task choice**: the receptor sources below apply a common ligand-dependent field and study total activity.

Conformational labels and occupancies represent configurations, which are even under physical time reversal. Calling these labels “spins” is a mathematical convention; interpreting them as literal magnetic moments would require a different physical reversal analysis. Fixed-field detailed balance does not make a driven experiment an equilibrium process, nor does it determine the admissible predictor class by itself.

Neither family automatically satisfies the repository's single-gateway architecture. The force model has two multistate observed ensembles; the conformational chain has interacting observed and hidden coordinates. The [existing rank theorem](MATRIX_RANK_PREDICTION_PRINCIPLE.md) therefore cannot simply be transferred by renaming states. The two-switch result instead supplies its own realization and conditional-variance obstruction under its stated preparation, readout, control and stationary-law assumptions.

## 2. Primary model sources

### A. Glauber's closed first moments are established

**Roy J. Glauber**, “Time-Dependent Statistics of the Ising Model,” *Journal of Mathematical Physics* **4**, 294–307 (1963), [DOI:10.1063/1.1703954](https://doi.org/10.1063/1.1703954). **Access:** the [publisher PDF](https://pubs.aip.org/aip/jmp/article-pdf/4/2/294/19156949/294_1_online.pdf) failed to open. The publicly exposed [primary-paper transcription](https://www.scribd.com/document/455589659/glauber1963-pdf) was inspected at printed pp. 296–299, especially Eqs. (9), (17), (28) and (30); its OCR is imperfect. This is not claimed as inspection of a publisher-hosted scan.

Equation (30) closes the single-spin means for the selected zero-field nearest-neighbor rate. The text immediately distinguishes other detailed-balanced kinetic choices that can couple different moment orders. The fixed-spin boundary example on p. 299 is also explicit. Thus neither first-moment closure nor boundary forcing should be advertised as a newly discovered mechanism. An arbitrary finite field at a dynamically switching endpoint is a separate specialization; it is not the fixed-spin example.

### B. A full primary account verifies the closure and its kinetic limits

**Claude Godrèche**, “Dynamics of the directed Ising chain,” *Journal of Statistical Mechanics* **2011**, P04005, [DOI:10.1088/1742-5468/2011/04/P04005](https://doi.org/10.1088/1742-5468/2011/04/P04005). **Access:** full [arXiv:1102.0141v2](https://arxiv.org/pdf/1102.0141v2), with Sections 1–3 and 6.2 inspected.

Equation (3.2) gives the closed magnetization equation for the directed zero-field chain; its symmetric case is Glauber's equation. Section 2 distinguishes the multiplicative-field rate from the heat-bath rate and notes that a spatially varying field preserves detailed balance for the symmetric dynamics. Section 6.2 treats an infinitesimal field: Eq. (6.4) displays the correlation term that precedes the linear-response approximation. This makes the boundary of the closure claim concrete. The paper does not identify minimum positive realizations of a finite controlled binary-mean task; its directed chain retains the original configuration space.

### C. Coupled receptor conformations have a direct PRL precedent

**Monica Skoge, Yigal Meir and Ned S. Wingreen**, “Dynamics of Cooperativity in Chemical Sensing among Cell-Surface Receptors,” *Physical Review Letters* **107**, 178101 (2011), [DOI:10.1103/PhysRevLett.107.178101](https://doi.org/10.1103/PhysRevLett.107.178101). **Access:** full [arXiv:1109.4160v1](https://arxiv.org/pdf/1109.4160v1), especially Eqs. (1)–(6), inspected.

The model uses active/inactive conformations, nearest-neighbor Ising interactions, and a common ligand-dependent bias. Eliminating explicit binding assumes binding/unbinding is faster than conformational switching. The authors assume local detailed balance and select a simple kinetic rule; they explicitly say its detailed dependence had not been experimentally measured. Their Eq. (4) is a **multiplicative-field Glauber rule**, not the constant-total-rate heat-bath rule at arbitrary field. The question is small-signal sensing through time-averaged total activity. This supports the conformational vocabulary and physical assumptions, not an experimental implementation of our local-control task or a predictor state-count advantage.

### D. The later receptor paper uses heat-bath rates explicitly

**Monica Skoge, Sahin Naqvi, Yigal Meir and Ned S. Wingreen**, “Chemical Sensing by Nonequilibrium Cooperative Receptors,” *Physical Review Letters* **110**, 248102 (2013), [DOI:10.1103/PhysRevLett.110.248102](https://doi.org/10.1103/PhysRevLett.110.248102). **Access:** full [arXiv:1307.2930v1 HTML](https://arxiv.org/html/1307.2930v1) inspected, including Fig. 1, Eq. (3) and Table 1.

Figure 1 distinguishes four activity/binding states of one receptor from its two-conformation fast-binding limit. Equation (3) imposes constant-total-rate heat-bath kinetics; the equilibrium specialization is an Ising model. Nonequilibrium cycle parameters are varied to optimize sensing, with a common concentration signal and total-activity response. These four states are **not** the four configurations of two binary receptors. The paper compares sensing performance of different physical dynamics, not smaller predictors of the same controlled target. Its nonequilibrium results cannot be cited as a memory-count separation.

### E. Four-state force-clamp dynamic disorder is explicit, but is not a hub model

**Gregor Diezemann, Thomas Schlesier, Burkhard Geil and Andreas Janshoff**, “Statistics of reversible bond dynamics observed in force-clamp spectroscopy,” *Physical Review E* **82**, 051132 (2010), [DOI:10.1103/PhysRevE.82.051132](https://doi.org/10.1103/PhysRevE.82.051132). **Access:** full [arXiv:1005.1590v2](https://arxiv.org/pdf/1005.1590v2), especially Appendix C, Fig. 9 and Eq. (C.1), inspected.

The illustrative network contains two configurations in each observed ensemble. Inter-ensemble rates depend on force; intra-ensemble exchange rates are assumed force independent. A common force-dependent equilibrium ratio across channels specializes it to fluctuating barriers. The paper analyzes waiting-time and counting statistics, including departures from a two-state Markov description. These assumptions are a concrete source-backed benchmark, not proof of a particular molecular realization. Non-Markovian visible trajectories do not imply that a smaller stationary nonreversible predictor outperforms every reversible predictor. That stronger comparison still requires a new certificate for the specified controls and accuracy.

## 3. The endpoint closure: an elementary specialization, not a new mechanism

For clarity, take the dimensionless energy

$$
E_h(\sigma)=-J_{01}\sigma_0\sigma_1-J_{12}\sigma_1\sigma_2-h\sigma_0
$$

and single-bit flip rates

$$
w_i(\sigma;h)=\frac{\alpha_i}{2}
\left[1-\sigma_i\tanh\left(h\,1_{i=0}+\sum_{j\sim i}J_{ij}\sigma_j\right)\right].
$$

This paragraph is our direct calculation for the stipulated open chain. It is not attributed as a theorem of the receptor papers. With $m_i=\mathbb E\sigma_i$, define

$$
a(h)=\frac{\tanh(h+J_{01})+\tanh(h-J_{01})}{2},\qquad
b(h)=\frac{\tanh(h+J_{01})-\tanh(h-J_{01})}{2},
$$

$$
c_0=\frac{\tanh(J_{01}+J_{12})+\tanh(J_{01}-J_{12})}{2},\qquad
c_2=\frac{\tanh(J_{01}+J_{12})-\tanh(J_{01}-J_{12})}{2}.
$$

The exact equations are

$$
\begin{aligned}
\dot m_0&=\alpha_0[-m_0+a(h)+b(h)m_1],\\
\dot m_1&=\alpha_1[-m_1+c_0m_0+c_2m_2],\\
\dot m_2&=\alpha_2[-m_2+\tanh(J_{12})m_1].
\end{aligned}
$$

They hold for arbitrary initial laws and every piecewise-constant endpoint protocol, without a small-field approximation. The closure follows because a function of the endpoint's single binary neighbor is affine, while the zero-field middle-site response is odd in its two binary neighbors. A field at the middle, degree-two hidden site generally introduces an even neighbor-product term; a field at a degree-two observed site can do so as well. A field at the other endpoint still gives an affine neighbor response. These modifications must be checked against the actual topology.

The invariant observable space is contained in $\operatorname{span}\{1,\sigma_0,\sigma_1,\sigma_2\}$. This bounds the dimension of a real linear representation of controlled endpoint means. It does **not** establish a four-state stochastic realization: nonnegative probabilities, a common preparation, an allowed readout and forward control dependence remain additional requirements. It also does not identify the dimension of an entire output path-law realization.

## 4. Positive duality is established; forward reuse remains a separate requirement

**J. Theodore Cox, Yuval Peres and Jeffrey E. Steif**, “Cutoff for the noisy voter model,” *Annals of Applied Probability* **26**(2), 917–932 (2016), [DOI:10.1214/15-AAP1108](https://doi.org/10.1214/15-AAP1108). **Access:** full published reprint [arXiv:1408.5122v2](https://arxiv.org/pdf/1408.5122v2), Section 1, Eq. (1.5), and Section 3.2, Eq. (3.5), inspected.

The paper identifies zero-field heat-bath Ising dynamics on a cycle with noisy-voter dynamics after time rescaling. Its graphical construction traces an observed site's ancestry backward through copying events, stopping at rerandomization; multiple ancestral paths coalesce. This supplies an exact positive representation, not merely a formal signed moment expansion. The source treats autonomous rates and does not establish a forward predictor for arbitrary boundary-control words.

Assume both bonds are ferromagnetic, $J_{01},J_{12}\ge0$. Our endpoint algebra gives $b(h)\ge0$ and $|a(h)|+b(h)\le1$. A heat-bath update can therefore copy its neighbor with probability $b(h)$, reset to $+1$ with probability $(1-b(h)+a(h))/2$, or reset to $-1$ with probability $(1-b(h)-a(h))/2$. Analogous site-dependent copying and reset probabilities apply to the zero-field hidden sites. Open endpoints require these recalculated probabilities; the uniform cycle construction cannot simply be reused unchanged.

This extension yields a positive **backward** ancestral representation. Under time-dependent driving, a lineage from time $t$ encounters rates at $t-s$: it traverses the original protocol in reverse chronological order. A simulator allowed that reversed sequence is not automatically a causal forward predictor driven by the original sequence. Establishing an admissible smaller model requires an explicit positive forward realization or intertwiner respecting every control, preparation and readout. The new two-switch theorem supplies that additional construction directly; no no-go theorem, or reversibility advantage, follows from duality alone.

## 5. Two recent memory results: relevant boundaries, different theorems

**Hugues Meyer and Kay Brandner**, “Weak-Memory Dynamics in Discrete Time,” *Physical Review Letters* **136**, 220401 (2026), [DOI:10.1103/kdhy-66b6](https://doi.org/10.1103/kdhy-66b6). **Access:** full [published seven-page PDF](https://journals.aps.org/prl/pdf/10.1103/kdhy-66b6), Eqs. (2)–(13), inspected; supplemental proof not inspected. Their recurrence has a time-independent free propagator and memory kernel. Under explicit weak-memory conditions, they construct a unique effective first-order generator, an initial-slippage matrix and an exponentially decaying approximation bound. Periodic driving is handled stroboscopically. This does not itself compare finite-state positive realizations under arbitrary switching words, the same preparation, and shared kinetic constraints. It is a useful precedent for rigorous memory reduction, not a direct solution to the present task.

**Pep Español**, “Embedding memory in coarse-grained Hamiltonian systems,” *Physical Review Research* **8**, 033133 (2026), [DOI:10.1103/dlzj-gtx3](https://doi.org/10.1103/dlzj-gtx3). **Access:** full [published 21-page PDF](https://journals.aps.org/prresearch/pdf/10.1103/dlzj-gtx3), especially Eq. (84) and Appendix B, inspected; supplemental material not inspected. The work constrains extended Fokker–Planck models by equilibrium structure and microscopic reversal. Equation (B1) distinguishes even configuration variables from odd momenta; Eqs. (B17)–(B18) constrain auxiliary parities and couplings. This directly supports keeping physical reversal explicit. Continuous auxiliary embeddings and finite-state predictor minima are different problems; auxiliary coordinates cannot silently be counted as a fixed number of discrete states.

## 6. The new two-switch result and its closest realization comparisons

For every finite $J>0$ and $H>0$, the [two-switch theorem](FAMILIAR_SWITCH_STRUCTURE.md) uses equal attempt rates, energy $-Js_0s_1-hs_0$, readout $S=s_0$ and zero-field equilibrium preparation. A rival must have a deterministic binary readout and stationary laws

$$
\widehat\pi_h(x)=\frac{\widehat\pi_0(x)e^{h\widehat S(x)}}{\cosh h},
\qquad \widehat\pi_0(\widehat S=\pm1)=\frac12.
$$

Within this class, the exact minimum counts are three stationary states and four ordinarily reversible states. An explicit positive three-state generator family reproduces all controlled means for arbitrary finite nonnegative fields; its exits are below two in unit-attempt-rate time. Two queried fields, $0,H$, already force the four-state ordinary minimum, even without a rival rate cap and at any prescribed positive clock. The explicit distinguishing menu consists of eleven words: $H^1,\ldots,H^5$ and $H^i0H^j$ for $i\in\{1,2\}$, $j\in\{0,1,2\}$, with at most five ticks and three constant-field segments. A positive error interval on this menu also holds without a rival rate cap: compact endpoint propagators and principal-log continuity exclude a zero-error limiting sequence. The argument does not quantify a useful margin.

The lower bound is not a new static rank identity. Minimal linear realization transfers a hidden coordinate $Z$ to any putative three-state rival. The common Gibbs tilt and detailed balance at both fields then force

$$
\mathbb E_0[Z\mid S=\pm1]=\pm\tanh J,\qquad
\mathbb E_0[Z^2\mid S=\pm1]=1.
$$

Both readout sectors have positive conditional variance. Each requires two states. The complementary upper realizes the familiar closed means with a single positive family obeying the required stationary tilt. Mean closure, linear realization theory and elementary variance support are established ingredients; their controlled positive-versus-reversible realization consequence is the repository result under comparison.

**Luca Benvenuti, Lorenzo Farina, Brian D. O. Anderson and Franky De Bruyne**, “Minimal Positive Realizations of Transfer Functions with Positive Real Poles,” *IEEE Transactions on Circuits and Systems I* **47**(9), 1370–1377 (2000), [DOI:10.1109/81.883332](https://doi.org/10.1109/81.883332). **Access:** full [author-uploaded published PDF](https://www.researchgate.net/profile/Lorenzo-Farina/publication/2367933_Minimal_positive_realizations_of_transfer_functions_with_positive_real_poles/links/0912f50c856539cc5b000000/Minimal-positive-realizations-of-transfer-functions-with-positive-real-poles.pdf), Sections I–III and Theorems 2–3, inspected. Theorem 2 recalls the invariant-polyhedral-cone characterization of positive realization; Theorem 3 constructs and characterizes third-order positive realizations with distinct positive real poles. The object is one autonomous discrete-time SISO transfer function. Matching each fixed-field response separately does not establish one shared controlled realization, the Gibbs tilt, or detailed balance across fields. This is a close positive-realization precedent, not a complete statement of the two-switch comparison.

The [earlier source audit](SIMPLE_PREDICTION_SOURCE_AUDIT.md) records the full-text comparison with Vanluyten–Willems–De Moor's structured HMM factorization and other static latent-state ranks. Those methods establish important realization ingredients. The present lower bound additionally uses a shared field-dependent stationary law and two-field self-adjointness; a generic pair-distribution factorization does not encode these conditions.

**Unresolved full-text lead:** H. Falk, “Reduced Markov chains at stochastic spin models,” *Physica A* **119**(3), 580–590 (1983), [DOI:10.1016/0378-4371(83)90110-3](https://doi.org/10.1016/0378-4371(83)90110-3). **Access:** [publisher abstract](https://www.sciencedirect.com/science/article/pii/0378437183901103) only; article/PDF access failed, and no primary full text was obtained in this focused search. The abstract describes reduced discrete-time Glauber cluster chains with exact marginal equilibrium distributions but generally altered time dependence. It is a relevant equilibrium-preserving reduction precedent. Without the paper, its formulas and special cases have not been excluded from a closer comparison; the abstract alone cannot certify nonoverlap or novelty.

## 7. What remains unresolved

The result is a comparison within the **shared Gibbs-tilt class**. It does not allow arbitrary independent field coupling to hidden rival coordinates; removing that assumption requires another theorem. It concerns endpoint means, not equality of output path laws, and makes no generalized-reversal or unavoidable-dissipation claim. The target's passive visible path already has hidden memory; its zero equilibrium mean alone is trivial to reproduce.

The exact separation is established in the repository, while practical robustness remains unresolved. The eleven-word design is explicit, but a positive tolerance supplied by compactness is not a percent-level advantage or a sample-complexity estimate. The [protocol exploration](FAMILIAR_SWITCH_PROTOCOLS.md) records reversible three-state fits below $0.14\%$ occupancy error on the current screening menus and below $1\%$ on sampled held-out protocols. Those are finite numerical comparisons, not all-protocol guarantees or certified global optima. They do not invalidate the exact separation, and they do not demonstrate a practical one-percent advantage. The three-switch closure and four-state force-clamp family remain useful follow-up models; this audit does not assign them an advantage.

The focused sources support the physical vocabulary and identify established mathematical ingredients. They do not settle priority of the full controlled theorem. The unresolved Falk full-text lead should remain visible, and the twelve-state construction remains a separate mathematical benchmark rather than a demonstrated molecular implementation.
