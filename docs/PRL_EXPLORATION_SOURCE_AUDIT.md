# Equilibrium prediction and the cost of detailed balance: PRL exploration audit

[Repository overview](../README.md) · [Fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Uniform reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) · [State–entropy-production tradeoff](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) · [Fixed-clock source comparison](FIXED_CLOCK_PRIOR_ART.md) · [Binary source comparison](BINARY_OBSERVATION_PRIOR_ART.md) · [Earlier source audit](PRIOR_ART.md)

**Research date: 23 September 2026.** This note audits five core primary papers and one foundational entropy-production paper against the proposed physical claim and identifies research advances that would strengthen a Physical Review Letters case. It is an assessment of scientific scope, not a priority certification or a prediction of editorial acceptance. All six papers were opened in full text; inspection depth is stated below. No manuscript or external correspondence is produced.

## 1. The internally reviewed claim

The repository establishes a family-level statement: some finite reversible targets admit much smaller stationary Markov predictors of their controlled means when the predictor is allowed to violate ordinary detailed balance. Both classes retain the same kinetic field rule, zero-field preparation, binary readout and bounded sensitivity range. The lower covers arbitrary new hidden state spaces and arbitrarily fast reversible rivals, not only aggregations of the target.

The [tight-band fixed-clock theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) uses the original targets with nonzero hidden relaxation rates in $[k,3k]$. It needs only two fields, $\{0,H\}$, and any prescribed positive clock. Rivals may choose arbitrary sensitivities in $[-9/100,9/100]$, without matching the target's nineteen-level histogram. It gives a polynomial unrestricted upper and a reversible lower

$$
D_{\mathrm{rev}}(\delta)\ge
\exp\!\left(\exp\!\left(c_{a,H}[\log(1/\delta)]^{1/5}\right)\right).
$$

The target retains nineteen actuator values and an exactly two-state passive visible law; it does not use the earlier binary construction's rare tags or hidden-rate rescaling. The two-field claim supplies an unrestricted upper only; a separate thirty-nine-field menu gives a polynomial unrestricted lower on the same target family. The [earlier binary-actuator theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) remains a distinct result with less favorable target constants. These are worst-case statements over growing families: a single fixed finite target always remains its own exact reversible realization.

The target is an equilibrium model at each constant field. A switching experiment need not keep it in equilibrium. The small rival has a stationary hidden law; stationarity is weaker than ordinary detailed balance. Thus the precise conceptual question is the state cost of **preserving equilibrium structure in one reusable response model**, rather than the existence of stationary predictors or the efficiency of one coarse-graining algorithm.

The separate [entropy-production extension](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) turns this qualitative restriction into a quantitative resource implication. If $R=e^{(1+G)H}$ and $\sigma_0$ is the predictor's full zero-field stationary path entropy-production rate, arithmetic reversibilization on the same states obeys

$$
\sup_{h,T}|m_K[h,T]-m_{(K+K^*)/2}[h,T]|
\le R^{3/2}\sqrt{\sigma_0/k}.
$$

The bound covers every bounded deterministic protocol and every horizon, without a hidden rate cap or minimum stationary mass. It yields

$$
D_{\le\Sigma}(\delta)\ge
D_{\rm rev}\!\left(\delta+R^{3/2}\sqrt{\Sigma/k}\right)
$$

for a common admissible class. [The tradeoff note](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) specifies the distinct capped and uncapped consequences and a same-state finite-entropy-production upper construction. These are internally reviewed research theorems; source comparison is not external validation.

## 2. Five core full-text primary comparisons

### A. Rigorous reversible compression already exists

**Mark Fornace and Michael Lindsey, “An approximation theory for Markov chain compression,” arXiv:2506.22918v3, 29 August 2025.** [Primary full text](https://arxiv.org/html/2506.22918v3), [version record](https://arxiv.org/abs/2506.22918v3).

**Inspected:** introduction, Proposition 4.1, Eq. (52), and Theorems 3/3*. Their induced generator is an irreducible reversible Markov generator over selected states. Theorem 3 bounds the lifted autonomous semigroup's nuclear-norm error by

$$
\left(\frac{3\sqrt3}{2\pi}+\frac{2|I|}{\pi}\right)
\frac{\varepsilon_*(I)}{t},\qquad t>0,
$$

where $\varepsilon_*(I)$ is an instance-dependent Nyström error; Theorem 3* refines the estimate using obliqueness quantities. The introduction explicitly discusses the uncontrolled short-time regime.

**Comparison:** preserving positivity and reversibility with quantitative dynamical error control is established. This is one autonomous generator, with a specified compression/lifting architecture. It is not a minimax comparison against arbitrary new-state models, nor a single reduced kinetic family for all fields and switching histories. Our lower does not invalidate their upper: their spectral error parameter need not be small on the required controlled witnesses.

### B. A scalar symmetric response can have a minimal positive symmetric realization

**Christian Grussler and Tobias Damm, “A Symmetry Approach for Balanced Truncation of Positive Linear Systems,” IEEE CDC (2012), 4308–4313.** [Institutional full manuscript](https://lup.lub.lu.se/search/files/3937565/3163112.pdf).

**Inspected:** §§3–5, especially Theorem 4 and its Arnoldi/Lanczos proof. For a quasi-symmetric SISO realization, $A=A^T$ and $C=cB^T$ with $c>0$, Theorem 4 gives a symmetric internally positive minimal realization of the same scalar transfer function. The construction reduces to a symmetric tridiagonal Metzler state matrix with compatible positive input/output vectors.

**Comparison:** symmetry need not enlarge the minimal realization for this scalar linear task. Internal positivity alone does not impose conservative stochastic normalization, the prescribed stationary preparation or the original field rule. Most importantly, equality of one transfer function is not simultaneous realization of a noncommuting family of controlled operator words. The prospective physical principle therefore has to concern reuse across interventions; a broad assertion that equilibrium responses generally require larger symmetric realizations would be false in this inspected setting.

### C. Large causal-state asymmetries are established, with a different restriction

**Christopher J. Ellison, John R. Mahoney, Ryan G. James, James P. Crutchfield and Jörg Reichardt, “Information Symmetries in Irreversible Processes,” Chaos 21 (2011), 037107.** [Primary full text, arXiv:1107.2168v1](https://arxiv.org/html/1107.2168v1), [author publication record](https://csc.ucdavis.edu/~cmg/compmech/pubs/pratisp2.htm).

**Inspected:** §§IV–V, §VI.2.3, footnote 11 and Appendix B. Their explicit explosive example has two recurrent forward causal states and countably many reverse causal states. These canonical representations are minimal within the unifilar class. Footnote 11 expressly retains a finite reverse generator once nonunifilarity is allowed. They distinguish properties of a process from properties of its hidden presentations.

**Comparison:** large representational asymmetries and causal-state memory costs are not new themes. Their separation compares prediction with retrodiction for an irreversible output process. Ours compares ordinary detailed balance with unrestricted stationary hidden dynamics for the same controlled prediction task, and imposes no unifilarity restriction. The state lower must continue to cover general positive hidden realizations; otherwise it could collapse to this already established representational distinction.

### D. Entropy-controlled comparison with additive reversibilization is established

**Artemy Kolchinsky, Naruo Ohga and Sosuke Ito, “Thermodynamic bound on spectral perturbations, with applications to oscillations and relaxation dynamics,” Physical Review Research 6 (2024), 013082.** [DOI](https://doi.org/10.1103/PhysRevResearch.6.013082), [primary full text, arXiv:2304.01714v4](https://arxiv.org/html/2304.01714v4).

**Inspected:** §§II–III, Eqs. (3)–(7), and Appendix C.1. For an irreducible finite generator with bidirectional edges, they use arithmetic reversibilization, preserving the stationary law, every escape rate and each edge's dynamical activity. Equation (7) implies

$$
\|\boldsymbol\lambda^W-\boldsymbol\lambda^{\bar W}\|^2
\le \kappa\sigma/2,\qquad
\kappa=\max_{i\ne j}\frac{\pi_iW_{ji}+\pi_jW_{ij}}{2\pi_i\pi_j}.
$$

The eigenvalues are sorted by real part. Their stronger bound also uses a weighted activity parameter. The proof controls the stationary-weighted antisymmetric matrix part and applies a spectral perturbation theorem.

**Comparison:** neither additive reversibilization nor the broad idea that entropy production controls departure from an equilibrium analogue is new. This is a spectral estimate for an autonomous generator; its constants involve normalized hidden activity. It does not bound all controlled endpoint means uniformly in horizon using only the external-interface constants, or connect that bound to a state-realization lower. Those are the specific distinctions to test in the repository's entropy extension.

### E. Thermodynamic memory efficiency is not state-count efficiency

**Susanne Still, David A. Sivak, Anthony J. Bell and Gavin E. Crooks, “Thermodynamics of Prediction,” Physical Review Letters 109 (2012), 120604.** [DOI](https://doi.org/10.1103/PhysRevLett.109.120604), [full arXiv:1203.3271v3 PDF](https://arxiv.org/pdf/1203.3271v3).

**Inspected:** the stochastic-drive setup and Eqs. (11)–(18). A thermally coupled Markov system is driven without feedback through alternating work and relaxation steps. Their Eq. (14) identifies average work-step dissipation, in thermal units, with $I(s_t;x_t)-I(s_t;x_{t+1})$; Eq. (18) bounds total average dissipation by the summed information difference, with the stated free-energy accounting.

**Comparison:** the connection between prediction, information retained in a physical state and dissipation is already explicit. The variables are mutual information and energetic costs under a driving distribution, not the number of available Markov states. The repository's state-count theorem alone does not imply this information difference or an entropy-production lower. Its separate reversibilization argument is needed to reach a state–fidelity–path-irreversibility tradeoff; it does not identify that tradeoff with work or heat in this paper's physical model.

### F. Foundational addition: path entropy production and its physical convention

**Udo Seifert, “Entropy Production along a Stochastic Trajectory and an Integral Fluctuation Theorem,” Physical Review Letters 95 (2005), 040602.** [DOI](https://doi.org/10.1103/PhysRevLett.95.040602), [publisher full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.95.040602/fulltext), [primary arXiv PDF](https://arxiv.org/pdf/cond-mat/0503686).

**Inspected:** the discrete-state generalization on pp. 3–4, Eqs. (22)–(30), in both the primary preprint and published article. Equation (28) gives the instantaneous total entropy-production rate $\sum_{n,k}p_nw_{nk}\log[p_nw_{nk}/(p_kw_{kn})]$. Equation (30) expresses the forward/reversed path likelihood ratio through the medium contribution and initial/final probability term. The discrete-state development does not require an a priori heat definition.

**Comparison:** stationary Markov path irreversibility and its entropy interpretation are established foundations. Specializing Eq. (28) to $p=\mu$ gives the repository's $\sigma_{\rm hid}$. This source does not provide the arithmetic-reversibilization approximation, reset-density estimate, uniform controlled-mean bound or state-budget consequence. Its reversed path leaves the discrete configuration label unchanged; interpreting that convention physically requires appropriate even states and thermodynamic assumptions. The repository does not obtain a Landauer erasure or device-heat theorem from this reference.

## 3. What survives this comparison

The inspected results do not supply the repository's combined conclusion: an equilibrium target family, one shared finite kinetic interface, finite-error prediction of actual controlled means, a much smaller stationary positive realization, and a lower against every ordinary-reversible realization despite unbounded rival rates. This is a bounded comparison, not evidence that no matching result exists elsewhere.

The most defensible distinction is the conflict between **simultaneous response reuse and detailed balance**. Autonomous compression, one-transfer realization and minimal causal-state construction solve materially different problems. Binary readout, two applied fields and a positive clock make the distinction operationally sharper than an unrestricted formal-series separation.

The entropy extension adds a distinct comparison with the closest spectral precedent. It uses relative entropy of finite path segments, a density estimate relative to $\mu$, and the last common return to the visible state. This controls endpoint response despite arbitrarily fast hidden dynamics; it is not obtained by replacing the normalized activity constant in the spectral bound. The reset is a decomposition of the existing interface, not a new physical operation or an uncounted memory state. Neither that decomposition alone nor arithmetic symmetrization should be presented as a new principle.

The remaining physical limitation is clear: the target still implements an engineered lamp/address system, and the prescribed kinetic rule does substantial work. The tight-band result removes the earlier rare-tag and large target rate-to-gap limitations for the nineteen-level family. It does not establish prevalence in a conventional local material or biochemical class, or a universal cost for every thermodynamically admissible actuator.

## 4. Resource statements that need separate proofs

| Quantity | What the current results support | Additional requirement for a physical claim |
|---|---|---|
| Retained state count $D$ | A lower on every counted finite reversible Markov realization | Already the proved resource; say explicitly that the model is Markov and uses the retained field rule |
| Worst-case storage capacity $\log D$ | Follows from counting distinguishable state labels | Does not identify how often those labels are occupied |
| Stationary information $H(\mu)$ or driven mutual information | No general lower follows from $D$ alone | Control the actual stationary/driven law, not only the law tilted by a recovered witness |
| Stationary path entropy production $\sigma_0$ | The separate reversibilization theorem gives a quantitative state–fidelity–irreversibility constraint | Respect the original interface and ordinary reversal; the lower can be very small and does not give the optimal tradeoff curve |
| Chemical work or heat | No device energy budget is identified | Specify reservoirs, local detailed balance and a physical realization |
| Experimental sample complexity | Finite clock witnesses exist | Control their number, signal sizes, estimation error and numerical conditioning |

The third row is a real logical distinction. For
$\mu=(1-\epsilon,\epsilon/(D-1),\ldots,\epsilon/(D-1))$,

$$
H(\mu)=h_2(\epsilon)+\epsilon\log(D-1),
$$

which can be small while $D$ is arbitrarily large. The repository's [weighted entropy proof](WEIGHTED_WHOLE_WORD_REPAIR.md) uses a witness-dependent law $\nu\propto\mu u_0^2$; high entropy under $\nu$ does not automatically lower-bound $H(\mu)$. This observation does not weaken the state-count theorem, but prevents identifying it directly with a Landauer or steady-dissipation bound.

Ordinary detailed balance uses identity reversal on every counted state. A thermodynamic interpretation therefore takes the retained states to be even configurations. An extension to generalized equilibrium with a nontrivial time-reversal involution is not supplied. The entropy theorem uses $\sigma_{\rm hid}=\sum_{i\ne j}\mu_iK_{ij}\log[(\mu_iK_{ij})/(\mu_jK_{ji})]$ and $\sigma_0=\sigma_{\rm hid}/2$; neither is the total entropy generated during arbitrary time-dependent driving. Its finite-entropy regularization gives every used hidden edge a positive reverse flux without adding states. This removes the one-way-edge obstruction to finite path entropy production; it does not specify a molecular implementation or local detailed balance with particular reservoirs.

## 5. What changed the assessment, and what would strengthen it further

Two priorities identified during this audit have now produced internally reviewed theorems: an entropy-production tradeoff, and a fixed-clock separation on the original tight-band target without a rival histogram constraint. Their contribution is more substantial than an improved logarithmic exponent alone. The remaining proposals below are not completed results.

**Strengthen the now-proved quantitative tradeoff.** The current lower forces stationary path irreversibility below an appropriate reversible state budget, while a polynomial-state upper has finite $\sigma_0=O(k\log(1/\delta))$ at fixed exit budget. These curves are unmatched. The uncapped target-index lower can be extremely small, of order $k\delta_n^2$ at error $\delta_n/2$; it is not an order-one dissipation floor. A sharp regime, a stronger lower in an explicit physical realization, or a directly observable finite-precision consequence would clarify how consequential the cost is. A thermodynamic device interpretation must add its actual reservoirs and time-reversal convention.

**High payoff: broaden the physical class while retaining a proved separation.** Extract a reusable criterion in terms of controlled positive transport and a state-information witness, then verify it in a second recognizable model class with local interactions or conventional kinetic transitions. A result stable under a specified, physically meaningful perturbation class would answer whether the advantage survives beyond exactly encoded logical operations. Merely restating the existing entropy lemma more abstractly, or plotting additional instances of the same construction, would not establish this broader relevance.

**Direct generality test: relax the kinetic rule itself.** The new theorem already lets rivals choose any bounded sensitivities without histogram matching. It still fixes the exponential entry/exit rate rule. Determine which part of the lower survives for a wider, explicitly bounded class of thermodynamically admissible field couplings. Preserving a thermodynamic rate ratio does not automatically preserve this kinetic family. A positive result for a broader class, or a precise counterexample locating the necessary structure, would clarify the physical content considerably.

**Make the effect visible at controlled finite precision.** A modest model with a rigorous reversible lower at a stated tolerance, together with an explicit smaller stationary predictor, would supply an interpretable instance of the mechanism. The relevant advance is a certified gap with realistic signal and protocol budgets, not a large simulation. Such an example complements the asymptotic theorem but does not replace the arbitrary-rival lower.

The present evidence supports a stronger PRL case than the state-count result alone: a controlled prediction resource tradeoff with an explicit equilibrium reference and finite-irreversibility upper realization. The main unresolved significance question is its reach beyond the particular kinetic interface and engineered target, together with the scale of the unavoidable cost. This assessment does not certify novelty or journal fit, and manuscript drafting remains deferred.

## 6. Audit boundary

The five core papers were selected from targeted searches and the existing repository audits; the entropy-production development added one foundational source. Both search systems were used. Two selected papers are PRL articles, one is in Physical Review Research, two are mathematical/control comparisons and one is a statistical-physics causal-state comparison. The closer spectral-perturbation paper took precedence over a general coarse-graining example. Full text means the primary manuscript or article was opened and the listed statements and surrounding assumptions were read; it does not mean every proof or supplement was independently checked. Earlier broader searches remain documented in the linked source notes. No exhaustive priority claim or external validation follows from this audit.
