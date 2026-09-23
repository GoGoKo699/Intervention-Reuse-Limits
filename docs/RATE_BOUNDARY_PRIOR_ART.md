# Rate-boundary prior art and assumption audit

[Scope](PUBLICATION_SCOPE.md) · [Binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Full prior-art audit](PRIOR_ART.md)

**Research date: 23 September 2026.** This is a bounded primary-source comparison for the state–speed–accuracy continuation. It does not certify priority, exhaust the literature, or make a publication prediction. The comparison is with the repository's stated research theorem; it is not an independent verification of that theorem's full proof.

## 1. The claim that needs comparison

The binary theorem fixes the target family, $k,H,\gamma$, the balanced $\{\pm\gamma\}$ histogram, stationary preparation, binary readout, and the field rule

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h}.
$$

One predictor must approximate **actual means** uniformly over every admissible protocol and every observation time. The present reversible lower bound also fixes a rival exit budget. At the common budget $6580k$, it separates polynomial unrestricted-predictor state growth from singly exponential reversible-predictor growth. Its lower witnesses already use five fields and any fixed positive clock; its upper guarantees cover all bounded protocols and all horizons. Arbitrary new rival state spaces are allowed.

A rate-sensitive continuation must expose its dependence on the dimensionless rival speed $B=\max_z(-K_{zz})/k$. A theorem proved for each fixed $B$ does not automatically allow $B=B(\delta)\to\infty$: every error exponent, coefficient-amplification constant, clock choice and threshold must be tracked before taking that diagonal limit. Finite state count, finite rates for each individual model, and a **uniform** rate budget are three different conditions.

## 2. Closest inspected comparisons

Each linked source below was opened in primary full text during this pass. “Inspected” refers to the identified statements and their surrounding setup, not every proof in the paper.

| Primary source and inspected location | Assumptions and conclusion | What does not follow for this repository |
|---|---|---|
| Grussler–Damm, *A Symmetry Approach for Balanced Truncation of Positive Linear Systems* (CDC 2012), [institutional manuscript](https://lup.lub.lu.se/search/files/3937565/3163112.pdf), §§3–5, Theorems 3–5, especially Theorem 4 | A quasi-symmetric SISO realization has $A=A^T$, $C=cB^T$, $c>0$. Theorem 4 supplies a symmetric positive minimal realization via Arnoldi/Lanczos. The surrounding reduction discussion concerns stable linear systems and one scalar transfer function. | Symmetry need not cost extra states for this particular scalar task. This is no simultaneous realization theorem for noncommuting field words, stochastic normalization, the exact histogram or the prescribed kinetic rule. Its internal positivity is not by itself a conservative reversible CTMC. |
| Huang–Ge–Kakade–Dahleh, *Minimal Realization Problems for Hidden Markov Models* (2014), [v1 full text](https://arxiv.org/html/1411.3698v1), Theorems 1–3 and §III.D | Stationary discrete-time HMMs in general position, excluding a measure-zero parameter set: exact finite-word probabilities identify minimal quasi-HMM/HMM realizations using logarithmic word length. Theorem 2's statistical parameter-error bound depends on the smallest retained Hankel singular value. | Generic identification is not worst-case approximation, and the exceptional set cannot be discarded for a deliberately constructed hard family. No ordinary-reversibility or continuous-time rate constraint is imposed. Parameter/sample accuracy is not a state-versus-rate-precision theorem. Passive words alone already admit the target's two-state telegraph realization. |
| Ellison–Mahoney–James–Crutchfield–Reichardt, *Information Symmetries in Irreversible Processes* (2011), [v1 full text](https://arxiv.org/html/1107.2168v1), §§IV–V, §VI.2.3 and footnote 11 | Canonical **unifilar** forward and reverse generators of a stationary output process can differ greatly: the explosive example has two recurrent forward causal states and countably many reverse causal states. Footnote 11 explicitly retains a finite reverse generator once nonunifilarity is allowed. | This is a prediction/retrodiction representation asymmetry. It is not an exponential lower bound for arbitrary ordinary-reversible hidden CTMC realizations of the same controlled mean map. The unifilar restriction is substantive. |
| Rosas et al., *AI in a vat: Fundamental limits of efficient worldmodelling for agent sandboxing and interpretability* (2025), [full text](https://arxiv.org/html/2504.04608), §6.1, Definition 8 and Theorem 4 | A transducer is called reversible when an additional reverse kernel generates the same interface with the required action dependence. Theorem 4 gives a conditional-independence criterion. The paper explicitly distinguishes its definition from thermodynamic reversibility. | Existence of a reverse kernel does not impose equality with the forward kernel or ordinary detailed balance. Its terminology cannot be used to assert or refute the present reversible-state separation. The rest of its world-model complexity results were not audited here. |
| Fornace–Lindsey, *An approximation theory for Markov chain compression* (2025), [v3 full text](https://arxiv.org/html/2506.22918v3), introduction, Proposition 4.1, Eq. (52), Theorems 3/3* | Given an autonomous irreducible reversible chain and selected states, the induced generator is again irreducible and reversible. Theorem 3 gives nuclear-norm semigroup error bounded by $[(3\sqrt3)/(2\pi)+2\lvert I\rvert/\pi]\varepsilon_*(I)/t$; Theorem 3* uses instance-dependent obliqueness quantities. | This preserves positive Markov structure but does not deliver one model for all controlled fields or preserve the actuator rule/histogram. An estimate valid for each $t>0$ need not tend uniformly to zero over all $t\ge0$. The introduction explicitly explains the short-time limitation. |
| Bielecki–Stettner, *Ergodic Control of a Singularly Perturbed Markov Process in Discrete Time with General State and Compact Action Spaces* (1998), [author PDF](https://math.iit.edu/~bielecki/publication/Ergodic_BL_98.pdf), §3 assumptions (A1)–(A5), Corollary 3.1 | The control class consists of stationary measurable state-feedback policies. Assumptions include a common ergodic decomposition, uniform within-class mixing, communication between classes, and unique perturbed invariant measures. Corollary 3.1 gives uniform-in-policy convergence of long-run average costs to the aggregated problem. | This is a genuine uniform control result, but for stationary policies and an ergodic cost. It is not uniform transient prediction for arbitrary externally prescribed switching, nor preservation of a scalar exponential field family. The ergodic assumptions are substantive, not cosmetic regularity. |
| Apers–Ticozzi–Sarlette, *Lifting Markov Chains To Mix Faster: Limits and Opportunities* (2017), [v1 full text](https://arxiv.org/html/1705.08253v1), Theorems 1–5 and Lemma 3 | Discrete-time lifted chains trade auxiliary states and initialization/invariance constraints against mixing time. Theorem 2 supplies diameter-time mixing in specified scenarios using order $D_{\mathcal G}N^2$ lifted nodes. Conductance limits depend on the retained constraints. | Auxiliary memory can accelerate sampling, but matching a stationary target and approaching it quickly do not preserve a target's time-dependent response. The resource is mixing steps on a graph, not CTMC exit speed at fixed visible clock $k$. |

The last two comparisons are useful warnings against broad phrases such as “uniform control reduction” or “states versus speed”: both are established subjects, with quantifiers different from the present task.

## 3. A structural obstruction to automatic fast-mode elimination

The following calculation is a direct consequence of the repository's rate rule, not a theorem attributed to the sources above. It checks the proposed limiting generator; it does not assert a general uniform convergence theorem for singular perturbations.

Suppose a fast irreducible hidden block $C$ equilibrates with conditional law $\mu(\cdot\mid C)$, while its external transitions remain of order $k$. Collapsing that block to one macrostate gives the usual averaged external rates

$$
\bar q_{AC}(h)=k\mu(C)e^h M_C(h),\qquad
\bar q_{CA}(h)=ke^{-h}M_C(h),\qquad
M_C(h)=\mathbb E_{\mu(\cdot\mid C)}e^{gh}.
$$

To represent this macrostate by the original rule with a single field-independent label $g_C$, one needs $M_C(h)=e^{g_Ch}$ on the allowed field interval. Differentiation at zero then gives

$$
g_C=\mathbb E_Cg,\qquad
g_C^2=\mathbb E_Cg^2,
$$

so $\operatorname{Var}_C(g)=0$. Conversely, a monochromatic block satisfies the identity. For a balanced block carrying $\pm\gamma$, $M_C(h)=\cosh(\gamma h)$, which is not a single exponential on any interval containing zero.

Thus ordinary averaging can preserve reversibility and the thermodynamic ratio $\bar q_{AC}/\bar q_{CA}=\mu(C)e^{2h}$ while leaving the **kinetic** family used in the theorem. Preserving ordinary detailed balance is insufficient. Retaining additional ports, replacing the field rule, or proving a special monochromatic elimination theorem changes the argument and must be counted explicitly.

This exposes an essential closure condition for that proposed route. It does **not** prove that the rival rate cap is intrinsically necessary, that every cap-free reduction fails, or that fast reversible rivals can beat the existing lower bound.

The Fornace–Lindsey short-time limitation likewise needs care. Failure of a full-state semigroup operator estimate near zero does not imply failure for one prescribed preparation and one binary readout. Invisible fast modes may have little integrated effect on that observable. Conversely, repeatedly switching fields can recouple retained and discarded directions. An autonomous error bound can neither rule out nor establish the required all-protocol observable estimate without an additional transfer argument.

## 4. State count, speed and numerical precision

The existing theorem grants arbitrary real transition parameters within its stated rate budget. Its lower bound therefore already tolerates uncharged parameter precision in that class. No precision assumption is needed to state that lower bound.

For a constructive tradeoff, however, three separate quantities must remain visible:

| Resource | Required statement |
|---|---|
| State count $D$ | Count every retained physical state, including ports, clocks and auxiliary registers. |
| Speed $B$ | Bound actual internal exits relative to fixed $k$; do not infer speed from matrix rank, parameter count or a change of time units. |
| Parameter precision | Specify a representation and perturbation norm, then prove stability of the same all-protocol/all-time observable error under rounding. The conditioning of a Hankel reconstruction is a different question. |

A large finite rate may have a short symbolic description, and an innocuous-looking bounded rate may require many bits under a chosen representation. No numerical-precision conclusion follows from a rate cap alone. No primary result inspected here supplies the missing conversion for this field family. This is a limit of the audit, not an impossibility claim.

## 5. Inherited ingredients and audit conclusion

The [existing primary-source audit](PRIOR_ART.md) already identifies the classical ingredients: [Altschuler–Weed–Rigollet (2017)](https://arxiv.org/abs/1705.09634), Algorithm 2/Lemma 7, for transport rounding; [Chetrite–Touchette (2015)](https://arxiv.org/abs/1405.5157), for generalized Doob transforms; and [Erschler–Zheng (2020)](https://aif.centre-mersenne.org/item/10.5802/aif.3360.pdf), Theorem 1.1/Lemma 2.3/Corollary 1.2, for lamp-growth ingredients. Those full-text audits were not repeated here. None should be presented as a new general mechanism.

**Finding:** this pass found no inspected result that establishes the same combined state-growth separation or eliminates the competitor rate cap while retaining every listed constraint. The positive-realization and HMM comparisons do not identify an omitted assumption in the existing capped theorem. They do identify substantive conditions that a continuation cannot silently discard: ordinary detailed balance rather than reverse-kernel existence; arbitrary positive rivals rather than unifilar representations; the same kinetic field rule after elimination; and explicit uniformity when a rate budget grows with inverse error.

The newly explicit fast-block closure failure is stronger than saying that the current logarithm-transfer proof loses constants. It blocks a specific naive reduction route. The intrinsic necessity of the rate cap remains unresolved by this audit.

**Search/access boundary.** Searches used both web search systems, including primary-domain coverage for reversible HMM realization, controlled fast reduction and lifting. Search engines sometimes broadened queries, so unrelated hits were discarded. The primary publisher record for Yin–Zhang–Badowski, [*Singularly Perturbed Markov Chains: Convergence and Aggregation* (2000)](https://www.sciencedirect.com/science/article/pii/S0047259X99918559), was located, but its full theorem text was not obtained in this pass; it is not used for a theorem-level conclusion. Likewise, the earlier Kotsalis–Shamma full-paper access limits in `PRIOR_ART.md` remain. No exhaustive priority claim is supported.

## 6. Finite-state fast limits: a focused source addendum

The subsequent [finite-state closure note](FINITE_STATE_FAST_RATE_CLOSURE.md) proves a qualitative controlled-mean compactification. Its general spectral and partition mechanisms have substantial prior art; they should not be presented as new general facts.

| Primary source and inspection | Relation to the closure argument | Scope still needing the repository's argument |
| --- | --- | --- |
| Colin de Verdière–Pan–Ycart, *Singular limits of Schrödinger operators and Markov processes* (1999), [journal full text](https://jot.theta.ro/jot/archive/1999-041-001/1999-041-001-009.pdf), §2.1, Theorem 2.15 and §3.1 | The finite-dimensional symmetric-operator compactification allows finite limiting dynamics on a proper subspace. Theorem 2.15 identifies a graph Schrödinger limit through disjoint supported one-dimensional subspaces and an explicitly constructed reduced graph. Section 3.1 conjugates reversible generators by square roots of stationary weights. This directly precedes the closure note's spectral subsequence and cluster interpretation. | The inspected statements concern autonomous operators and spectral/graph reduction. They do not state convergence of this prescribed mean response uniformly over every bounded externally switched field and all horizons, or the exact mixture-valued actuator identity with a constituent-atom budget. The present elementary spectral proof is a specialization and adaptation, not a new compactification principle. |
| Coderch–Willsky–Sastry–Castanon, *Hierarchical Aggregation of Singularly Perturbed Finite State Markov Processes* (1983), [author-hosted scan](https://willsky.lids.mit.edu/publ_pdfs/41_pub_STOC.pdf), introduction and §3.1 remarks, printed pp. 271–272 | The scan discusses finite Markov semigroups discontinuous at time zero, an initial stochastic projection, its ergodic partition, instantaneous within-class equilibration and transient states. The introduction also states an autonomous approximation assembled from several time scales and valid on the infinite time interval. Initial projections and class aggregation are established mechanisms. | Autonomous all-time approximation is not the same quantifier as one approximation uniform over arbitrary switching protocols. The retrieved scan omits some printed pages; the comparison uses the displayed introduction and remarks, not an uninspected full theorem or its proof. |
| Kurtz, *A limit theorem for perturbed operator semigroups with applications to random evolutions* (1973), [publisher record](https://www.sciencedirect.com/science/article/pii/002212367390089X), abstract only | The primary abstract studies generators $A+\alpha B$ as $\alpha\to\infty$, a limiting projection $P$ for the fast semigroup, and effective dynamics generated by the closure of $PA$ on its range. Projection and compression are classical singular-perturbation ideas. | The full paper was not obtained in this pass. Its hypotheses or theorem-level coverage of the repository's nonautonomous setting are therefore not asserted. |

The stochastic-idempotent step in the closure note is also elementary: with a strictly positive reversible stationary law, support components are closed; irreducibility makes the fixed space on a component one-dimensional; idempotence leaves only eigenvalues zero and one. The projection is consequently conditional expectation onto those components. The note supplies this proof directly rather than assigning it a new general result. The older stochastic-projection discussion above is a concrete attribution anchor.

The specific statement to retain is narrower: arbitrary reversible rivals of bounded state count, with possible vanishing stationary masses and no uniform rate cap, have subsequential limits in the **all-protocol, all-horizon scalar response metric**; those limits have finite reversible cluster dynamics, averaged exponential actuator factors and the retained constituent-atom budget. The Dyson argument supplies uniformity under arbitrary switching, and the common visible reset extends finite-time convergence to all horizons. These are the points to compare in any further novelty search. This pass establishes neither priority for that combination nor a quantitative uncapped state lower bound.
