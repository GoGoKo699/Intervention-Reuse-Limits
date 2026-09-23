# Kinetic freedom, word memory and the time-reversal boundary

[Resource and parity comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [General kinetic interface](GENERAL_KINETIC_INTERFACE.md) · [General interface entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) · [Generalized-reversal theorem](GENERALIZED_REVERSAL_PREDICTION.md) · [Earlier PRL source audit](PRL_EXPLORATION_SOURCE_AUDIT.md)

**Primary-source audit, 23 September 2026.** The most consequential comparison is with reversible higher-order Markov models. Their word-state representations need not obey ordinary detailed balance, although the represented sequence is time reversible. Consequently, a lower against ordinary reversible predictors does not automatically extend to predictors with a nontrivial state-reversal involution, or imply a convention-independent physical dissipation cost.

This note compares the broader barrier interface and the internally reviewed [centered-word theorem](GENERALIZED_REVERSAL_PREDICTION.md) with ten primary sources. Full-text access and exact inspected statements are identified below; no inference relies on an abstract alone. The audit supplies bounded comparisons, not a priority certification. Manuscript drafting and external contact remain deferred.

## 1. Closest precedents: reversible memory is not a selfadjoint word process

### A. Bacallado: the precise reversed-word flux identity

**Sergio Bacallado, “Bayesian analysis of variable-order, reversible Markov chains,” Annals of Statistics 39(2), 838–864 (2011).** [DOI](https://doi.org/10.1214/10-AOS857) · [primary electronic reprint](https://arxiv.org/pdf/1105.2640).

**Full text inspected:** Definition 1.1, Proposition 1.2, the subsequent first-order-representation warning, and Definition 2.2/Proposition 2.3 with proof. For an order-$r$ process, reversal symmetry of stationary $(r+1)$-blocks suffices for full sequence reversibility. On de Bruijn word states, the paper imposes edge weights $k_{uv}=k_{v^*u^*}$ and masses $k_u=k_{u^*}$, where $u^*$ reverses the word. With $P(u,v)=k_{uv}/k_u$, its proof gives

$$
\pi(u)P(u,v)=\pi(v^*)P(v^*,u^*).
$$

**Comparison:** this is a direct precedent for generalized-reversible word realizations. The paper expressly distinguishes them from ordinary reversibility of the lifted first-order chain. It does not prove the repository's centered-actuator continuous-time controlled-response equivalence or quantitative polynomial approximation bound. Those additional steps must be proved separately; reversed-word balance itself should not be claimed as new.

### B. Diaconis–Miclo: trajectorial reversibility does not restore operator symmetry

**Persi Diaconis and Laurent Miclo, “On the spectral analysis of second-order Markov chains,” Annales de la Faculté des sciences de Toulouse: Mathématiques, series 6, 22(3), 573–621 (2013).** [DOI](https://doi.org/10.5802/afst.1383) · [publisher full text](https://www.numdam.org/article/AFST_2013_6_22_3_573_0.pdf).

**Full text inspected:** §1, Eqs. (1.1)–(1.5), and Theorem 1.1 with its construction. They distinguish reversal of $(X_0,\ldots,X_n)$ from ordinary reversibility of the pair chain $(X_n,X_{n+1})$. The lifted operator need not be selfadjoint or even diagonalizable. For an irreducible, aperiodic reversible kernel other than independent resampling, Theorem 1.1 constructs a trajectorially reversible second-order perturbation whose spectral gap initially increases.

**Comparison:** performance advantages compatible with sequence reversal and a nonsymmetric lifted operator are established. Their resource is mixing speed for a fixed sampling task, not state count for reusable controlled means. This is nevertheless a direct warning against identifying the repository's selfadjoint competitor restriction with all equilibrium dynamics involving memory or velocity-like variables.

### C. Lee–Kwon–Park: the entropy functional must use the physical reversal

**Hyun Keun Lee, Chulan Kwon and Hyunggyu Park, “Fluctuation Theorems and Entropy Production with Odd-Parity Variables,” Physical Review Letters 110, 050602 (2013).** [DOI](https://doi.org/10.1103/PhysRevLett.110.050602) · [primary preprint](https://arxiv.org/pdf/1209.0543v1).

**Access and inspection:** the full preprint, under its earlier title “Fluctuation theorems in general stochastic processes with odd-parity variables,” was read at pp. 2–3, Eqs. (3)–(11); journal metadata was checked, but the publisher full-text request failed. Equation numbers here refer to the preprint. Reversal maps $x(t)$ to $\theta x(T-t)$. The generalized balance condition uses $\omega_{xy}p_y^s=\omega_{\theta y,\theta x}p_{\theta x}^s$; parity symmetry of the stationary law is a separate condition. Holding-time factors need not cancel as in the all-even case.

**Comparison:** substituting ordinary edge-flux entropy for entropy under an arbitrary reversal is invalid. A word-reversal construction with invariant stationary mass, compatible rates and an even actuator addresses this distinction mathematically. This source does not assign a microscopic parity to an arbitrary information-processing device.

## 2. What broader barrier kinetics does and does not assume

Consider the external rates in the [general kinetic interface](GENERAL_KINETIC_INTERFACE.md),

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),\qquad b_i(0)=1,
\qquad 0<b_-\le b_i(h)\le b_+<\infty.
\tag{1}
$$

Here $K$ remains field independent and stationary under $\mu$. The following is direct algebra for (1), not a theorem attributed to the sources. At fixed $h$,

$$
\pi_h(A)=\frac1{1+e^{2h}},\qquad
\pi_h(i)=\frac{\mu_i e^{2h}}{1+e^{2h}},\qquad
\pi_h(A)q_{Ai}(h)=\pi_h(i)q_{iA}(h).
\tag{2}
$$

Thus $\pi_h$ is stationary, and the external edge conductance is
$k\mu_i e^{2h}b_i(h)/(1+e^{2h})$. Ordinary reversibility of the full chain additionally requires ordinary reversibility of $K$. Changing $b_i$ changes kinetics without changing this stationary law or the external forward/backward rate ratio.

In thermal units, energies $E_A=h$ and $E_i=-h-\log\mu_i$ reproduce the ratio $q_{Ai}/q_{iA}=e^{E_A-E_i}$. With an attempt frequency $\nu$, a symmetric transition-state energy $B_{Ai}=B_{iA}=E_i-\log[kb_i(h)/\nu]$ represents the two external rates in Arrhenius form. This rate-level representation is not a derivation from a specific microscopic landscape or an accounting of the work required to operate its barriers.

### D. Rahav–Horowitz–Jarzynski: well energies and barrier energies are distinct controls

**Saar Rahav, Jordan Horowitz and Christopher Jarzynski, “Directed Flow in Nonadiabatic Stochastic Pumps,” Physical Review Letters 101, 140602 (2008).** [DOI](https://doi.org/10.1103/PhysRevLett.101.140602) · [primary full text](https://arxiv.org/pdf/0808.0015v2).

**Full text inspected:** p. 1 Arrhenius rates and Eq. (3), Eqs. (4)–(5), and the no-pumping proof around Eq. (11). Their model separates well energies, which set equilibrium weights, from symmetric barrier energies, which set branching fractions. The no-pumping theorem makes a dynamical distinction: varying only well depths with fixed barriers, or only barriers with fixed wells, cannot produce a net integrated current over the specified cycle.

**Comparison:** independent kinetic freedom at a fixed equilibrium rate ratio is established and physically motivated. The source does not make our single-hub topology, field-independent hidden block, bounded return-rate assumption or common preparation a universal model of thermodynamic actuation. Its cyclic-current theorem is not a controlled-mean state-realization theorem.

### E. Baiesi–Maes–Wynants: entropy flux alone does not determine response

**Marco Baiesi, Christian Maes and Bram Wynants, “Fluctuations and Response of Nonequilibrium States,” Physical Review Letters 103, 010602 (2009).** [DOI](https://doi.org/10.1103/PhysRevLett.103.010602) · [author-hosted published full text](https://fys.kuleuven.be/english/staff/christ/files/pdf/pub/physrevlett-103-010602.pdf).

**Full text inspected:** pp. 1–2, Eqs. (3)–(7). Their path-action decomposition separates excess entropy flux from excess time-symmetric dynamical activity. The general response formula contains correlations with both contributions; for the stated jump-rate perturbation, activity is expressed through the generator acting on the perturbed potential.

**Comparison:** specifying the thermodynamic bias does not exhaust the dynamical response problem. This supports treating barrier functions as substantive kinetic freedom. The theorem is a linear-response identity with specified perturbations, not a finite-amplitude comparison of two hidden realizations uniformly over protocols and all times.

### F. Falasco–Esposito: deriving thermodynamic rates requires more than naming them

**Gianmaria Falasco and Massimiliano Esposito, “Local detailed balance across scales: From diffusions to jump processes and beyond,” Physical Review E 103, 042114 (2021).** [DOI](https://doi.org/10.1103/PhysRevE.103.042114) · [primary full text](https://arxiv.org/pdf/2101.03968).

**Full text inspected:** §II.C, Eqs. (26)–(29), and §IV, including the time-dependent extension. Under weak-noise and weak-nonconservative-force assumptions, the coarse-grained log rate ratio is a free-energy difference plus work along a typical transition path. The time-dependent extension also assumes separation from intrabasin equilibration and preserved metastable structure.

**Comparison:** a microscopic justification of local detailed balance is a separate, assumption-dependent result. The algebraic consistency of (1) does not prove that every bounded measurable barrier function is implementable by that coarse-graining procedure, especially under arbitrarily rapid driving. Our finite-state control model can be well defined without asserting this stronger physical derivation.

The community-supported ingredients in D–F are rate-ratio thermodynamics and independent kinetic information. The special assumptions of the repository remain the star-shaped visible interface, a common hidden equilibrium law, a field-independent $K$, preparation $(1/2,\mu/2)$, bounded barrier rates, and an endpoint-mean prediction task. Source counts cannot establish that entire architecture as conventional or general.

## 3. Closest bounds and the precise remaining distinction

### G. Kolchinsky–Ohga–Ito: entropy-controlled additive reversibilization, spectrally

**Artemy Kolchinsky, Naruo Ohga and Sosuke Ito, “Thermodynamic bound on spectral perturbations, with applications to oscillations and relaxation dynamics,” Physical Review Research 6, 013082 (2024).** [DOI](https://doi.org/10.1103/PhysRevResearch.6.013082) · [primary full text](https://arxiv.org/html/2304.01714v4).

**Full text inspected:** §§II–III and Appendix C.1. Arithmetic reversibilization preserves the stationary law, escape rates and edge activity. Their Eq. (7) implies $\|\boldsymbol\lambda^W-\boldsymbol\lambda^{\bar W}\|^2\le\kappa\sigma/2$, where $\kappa=\max_{i\ne j}(\pi_iW_{ji}+\pi_jW_{ij})/(2\pi_i\pi_j)$ is a normalized activity rate. They assume irreducibility and bidirectional edges.

**Comparison:** the general idea of an entropy-controlled difference from an equilibrium analogue is already explicit. Their bound controls autonomous spectra with hidden kinetic constants. It does not supply a bound on every controlled endpoint mean with only interface constants, or a minimax state-budget consequence. Its ordinary reversal convention cannot be replaced by word reversal without changing the problem.

### H. Dechant–Sasa: exact observable-response inequalities from relative entropy

**Andreas Dechant and Shin-ichi Sasa, “Fluctuation–response inequality out of equilibrium,” Proceedings of the National Academy of Sciences 117, 6430–6436 (2020).** [DOI](https://doi.org/10.1073/pnas.1918386117) · [full published article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7104339/).

**Full text inspected:** Eqs. (3)–(12), the Markov-jump interpretation around Eqs. (13)–(16), and the time-reversal specialization, Eqs. (25)–(27). Their exact inequality bounds an observable's mean difference using relative entropy and its cumulant-generating function. It allows path observables, endpoint observables and finite changes; the simpler variance formula generally requires linear response or Gaussian fluctuations. Time-dependent reference and perturbed dynamics are allowed.

**Comparison:** entropy-to-observable control is established well beyond stationary linear response. Applying the generic inequality to a whole path ordinarily retains the time dependence of path relative entropy. The repository's extra work is an interface-specific uniform bound on endpoint relative entropy using the final reset interval, then its connection to an ordinary-reversible realization lower. The source alone does not supply that step.

### I. Evans–Majumdar: the last-reset-age mechanism is established

**Martin R. Evans and Satya N. Majumdar, “Diffusion with Stochastic Resetting,” Physical Review Letters 106, 160601 (2011).** [DOI](https://doi.org/10.1103/PhysRevLett.106.160601) · [primary full text](https://arxiv.org/pdf/1102.2704).

**Full text inspected:** the resetting equation and renewal interpretation, Eqs. (1)–(3). A Poisson reset to a fixed position gives an exponentially distributed last-reset age in stationarity; integrating the ordinary diffusion propagator against that age law gives the reset stationary density.

**Comparison:** forgetting through a last-reset decomposition is established. Their result concerns diffusion with an explicitly added reset, including stationary and search properties. It does not compare arbitrary controlled CTMC realizations in terms of hidden entropy production. In the repository the reset clock is a representation of existing return rates; attributing a separate reset work cost to this proof representation would change the model.

### J. Dupuis–Katsoulakis–Pantazis–Plecháč: information bounds can remain useful at long times

**Paul Dupuis, Markos A. Katsoulakis, Yannis Pantazis and Petr Plecháč, “Path-Space Information Bounds for Uncertainty Quantification and Sensitivity Analysis of Stochastic Dynamics,” SIAM/ASA Journal on Uncertainty Quantification 4(1), 80–111 (2016).** [DOI](https://doi.org/10.1137/15M1025645) · [primary preprint](https://arxiv.org/pdf/1503.05136v2).

**Access and inspection:** full preprint, §§3.2–3.6, Theorems 3.3–3.9 and Eqs. (3.38)–(3.39); numbering refers to this version, with journal metadata checked separately. Theorem 3.3 bounds finite-time observable bias by an optimized cumulant-generating expression and path relative entropy. Theorem 3.4 supplies its long-time limit under a limiting cumulant assumption. The sensitivity estimates yield uniform control when $T\operatorname{Var}(F)$ stays bounded, including suitable time averages with summable stationary correlations.

**Comparison:** it would be incorrect to suggest information inequalities inherently fail at long times. An instantaneous endpoint observable generally does not satisfy that variance-scaling condition. The repository instead bounds endpoint relative entropy through the last reset, uniformly over arbitrary legal controls, without a hidden mixing constant. This particular step and its same-state reversibilization application are not supplied by the inspected statements.

### What the inspected sources do not combine

The closest comparisons are complementary: G compares a generator with its additive reversibilization, H and J turn relative entropy into observable error, and I supplies reset renewal. None of these inspected statements directly supplies the repository's combination of an interface-only, all-horizon, all-bounded-protocol endpoint estimate and a same-state ordinary-reversible comparator. This is a precise comparison of inspected statements, not evidence of exhaustive priority. The ordinary path-entropy foundation from Seifert (2005) is documented in the [earlier audit](PRL_EXPLORATION_SOURCE_AUDIT.md).

The [general interface entropy theorem](GENERAL_INTERFACE_ENTROPY_BOUND.md) proves the extension from exponential sensitivities to (1): the return rate remains at least $kb_-$ and the injection density is bounded by $k e^{2H}b_+$. More generally, its endpoint bound needs only a positive return lower bound, a stationary-law-dominated injection upper bound and a controlled initial hidden density. The common equilibrium ratio is needed separately to make the full comparison model reversible. A whole-path relative-entropy bound uniform over arbitrarily long times is not claimed.

## 4. Required claim boundary after allowing word reversal

For a stationary hidden law invariant under an involution $\theta$, let $\Theta f=f\circ\theta$. Ordinary detailed balance is $K^*=K$; generalized balance is

$$
K^*=\Theta K\Theta.
\tag{3}
$$

The latter does not make $K$ selfadjoint. If additionally $\theta A=A$ and $b_{\theta i}(h)=b_i(h)$, the external rule is compatible with the same reversal. A centered odd-length word has a reversal-invariant middle-symbol actuator, unlike an endpoint-symbol actuator viewed on the same word state. The repository's [generalized-reversal theorem](GENERALIZED_REVERSAL_PREDICTION.md) proves equality of the coordinate-shifted stationary actuator-path laws and transfers that equality to the controlled continuous-time interface. That last step is a repository argument, not a consequence of the cited statistics papers alone.

The centered-word result is an internally reviewed research theorem: it retains the polynomial prediction bound, target histogram and hidden exit cap while satisfying (3), with exactly zero generalized stationary entropy production. It therefore disproves a superpolynomial state requirement for the enlarged generalized-reversible class on these targets. The stronger conclusion of unavoidable thermodynamic dissipation across all reversal conventions is explicitly false for that mathematical class. Zero stationary entropy under $\theta$ still does not mean zero entropy generated during arbitrary driving or establish a particular physical device.

Arithmetic reversibilization $(K+K^*)/2$ remains a valid same-state ordinary-reversible comparator. Its entropy bound uses ordinary path reversal. Replacing $K^*$ with $\Theta K^*\Theta$ would instead aim at generalized balance; for a predictor already satisfying (3), this operation leaves $K$ unchanged and supplies no ordinary-reversible competitor. It therefore cannot extend the ordinary state lower by a change of notation.

The defensible physical statement is conditional: in implementations whose counted retained states are even under the physical reversal, the ordinary path-irreversibility frontier applies. For a class admitting compatible reversal of hidden memory states, one must analyze that broader class directly. The distinction should be foregrounded in the research assessment, not relegated to a final caveat.

The [capped kinetic-interface separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) broadens the ordinary rival class beyond the prescribed exponential barrier curves and histogram. Its common exit cap still supports positive hidden transition operators. This strengthening does not remove the hub geometry, field-independent hidden dynamics, common preparation, equilibrium block tilt or ordinary reversal requirement. The [resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) states the resulting growth classes and entropy-budget implication under those assumptions; source precedent cannot substitute for its proof and internal review.

## 5. Access and audit limits

All ten selected sources were opened in full text and the listed sections were inspected. The Bacallado file is a primary electronic reprint with pagination differing from the journal; Lee–Kwon–Park was inspected as its explicitly identified preprint, not as the inaccessible publisher PDF. The other links identify the primary article/manuscript versions used. No review, search snippet, lecture note or secondary summary substitutes for a key statement.

The search covered kinetic barriers, local detailed balance, observable-response information inequalities, reset renewal, generalized reversal and higher-order Markov representations. It was targeted rather than exhaustive. Neither the number of papers nor the absence of a matching theorem among them certifies novelty, broad physical applicability or PRL suitability.
