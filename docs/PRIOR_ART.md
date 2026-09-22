# Prior-art and novelty audit

[Repository overview](../README.md) · [Exact theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

**Updated 22 September 2026, including full-text comparisons for sampled-response lower bounds.** This is a bounded audit, not a certification of novelty. A derivation obtained independently here may still be known. Access depth and version are recorded below. Earlier failed retrievals remain provenance; a later successful inspection supersedes the associated access limitation, not the need for a complete novelty audit.

## Claims being screened

The exact target combines: equality of the complete passive visible Markov path law; a specified reversible field-dependent rate rule; matching static and dynamic linear mean response; and an all-size sharp separation between passive state count and exact cubic-response state count.

The extension retains nonvanishing total response with bounded coupling, then gives a protocol-uniform cubic approximation certificate and an explicit reversible Markov realization whose size is independent of the original state count. Sampled cubic responses now also provide a lower bound against the broad analytic Markov surrogate class. The coefficient tolerance, known kinetic kernel, and freedom to change microscopic rates are essential assumptions.

The broad claims below are **not** prospective contributions: hidden kinetics affect nonlinear response; one can coarse-grain response; Volterra kernels admit state realizations; positive sums of exponentials can be approximated by shorter sums; Hankel rank and singular values obstruct low-dimensional approximation.

## Established response theory

**Urna Basu, Matthias Krüger, Alexandre Lazarescu, Christian Maes, “Frenetic aspects of second order response” (2015).** Physical Chemistry Chemical Physics 17, 6653–6666. [Primary full text](https://arxiv.org/html/1410.7450v2), [DOI](https://doi.org/10.1039/C4CP04977B).

The paper distinguishes thermodynamic and time-symmetric kinetic rate changes and shows that nonlinear response depends on dynamical information not fixed by equilibrium linear response. The initialization pass retrieved the primary abstract and full-text framework; this follow-up carries that access record forward. Consequence: the kinetic field factor and the general hidden-kinetics message are established, not new here.

**Gregor Diezemann, “Nonlinear response theory for Markov processes: Simple models for glassy relaxation” (2012).** Physical Review E 85, 051502. [Primary record](https://arxiv.org/abs/1203.1785), [DOI](https://doi.org/10.1103/PhysRevE.85.051502).

The primary abstract explicitly states a master-equation perturbation framework through third order and sensitivity of cubic response to kinetic field coupling. The supplied analytical checkpoint recorded full-text inspection; repository initialization reconfirmed the primary record and abstract. This follow-up carries those access records forward. Consequence: cubic response formulas and different nonlinear responses despite matching linear diagnostics are established.

**Fenna Müller, Urna Basu, Peter Sollich, Matthias Krüger, “Coarse-grained second-order response theory” (2020).** Physical Review Research 2, 043123. [Primary record](https://arxiv.org/abs/2005.05169), [DOI](https://doi.org/10.1103/PhysRevResearch.2.043123).

**Access:** the initialization pass reached the abstract only; the follow-up inspected [arXiv v2 full text](https://arxiv.org/html/2005.05169v2) (29 November 2020), especially Sections II–IV, Eq. (30), and Appendix A.4. The paper obtains arbitrary-protocol second-order response from coarse path-weight derivatives measured with step perturbations. Its four-state chain has blocks $\{A,B\}$ and $\{C,D\}$ with only the $B$–$C$ edge crossing blocks. Section IV.1 explicitly identifies the finite-rate passive coarse process as non-Markovian; zero and nonzero cross-block exit rates within a block also show this directly. Appendix A.4 treats a Markov coarse description but does not establish preservation under our hidden-dependent kinetic field rule.

**Comparison:** response reconstruction from reduced observations is established. The displayed example does not give our exactly Markov passive telegraph process or a sharp all-size Markov-surrogate state-count separation. Our equilibrium potential acts on visible states, so the paper's framework is relevant; the order change to cubic is not by itself a novelty argument. Its step measurements include linear response of coarse joint probabilities, which must not be confused with our matching of the single-time mean's linear response.

## Aggregation and realization

**Luca Cardelli, Radu Grosu, Kim Guldstrand Larsen, Mirco Tribastone, Max Tschaikowski, Andrea Vandin, “Lumpability for Uncertain Continuous-Time Markov Chains” (2021).** QEST 2021, 391–409. [Institutional record](https://vbn.aau.dk/en/publications/lumpability-for-uncertain-continuous-time-markov-chains/), [DOI](https://doi.org/10.1007/978-3-030-85172-9_21).

The initialization pass inspected bibliographic information and the abstract. The [author manuscript](https://www.iris.santannapisa.it/retrieve/dd9e0b32-58f9-709e-e053-3705fe0a83fd/qest2021.pdf) was located in the follow-up, but sustained retrieval failed; no new theorem-level claim is based on that file. The abstract concerns preservation of reachable probability sets under time-varying interval uncertainty. The subsequent journal extension provides the accessible theorem-level comparison below.

**The same authors, “Algorithmic Minimization of Uncertain Continuous-Time Markov Chains” (2023).** IEEE Transactions on Automatic Control 68, 6557–6572. [DOI](https://doi.org/10.1109/TAC.2023.3244093), [accepted manuscript, DTU](https://backend.orbit.dtu.dk/ws/files/318778353/HKKR_Algorithmic_Minimization_of_Uncertain_Continuous_Time_Markov_Chains.pdf).

**Access:** accepted full text inspected, notably Introduction, Theorem 2, Definition 4, Theorems 5–6, and Appendix C's control correspondence. Theorem 2 gives pointwise block-rate equalities for time-varying ordinary lumpability. Definition 4 instead requires lumpability of both endpoint generators of an interval-rate family; Theorems 5–6 characterize preservation of extremal value functions for block-constant rewards. The authors explicitly distinguish this from every realized CTMC being lumpable.

**Comparison:** their uncertain reduction can use corresponding, different control functions in the original and reduced systems. It does not assert equality under the same specified scalar actuator $h(t)$, as required here. Replacing our coupled rate family by independent intervals changes the admissible interventions. Ordinary lumpability applied pointwise already proves our block-uniform preservation boundary; that observation is not a new theorem. Neither failure of a partition criterion nor an uncertain-control reduction alone settles our broader lower bound over arbitrary analytic Markov surrogates.

**Arthur E. Frazho, “A Shift Operator Approach to Bilinear System Theory” (1980).** SIAM Journal on Control and Optimization 18(6), 640–658. [Primary publisher record](https://epubs.siam.org/doi/10.1137/0318049).

The publisher abstract describes bilinear realization of Volterra input-output maps, minimality linked to reachability and observability, and finite realizability through rational transforms. Full text was not obtained in either pass; a theorem-level comparison remains open. The pole-location lemma is standard realization reasoning, not an independent innovation.

**Peter Benner and Pawan Goyal, “Balanced Truncation Model Order Reduction For Quadratic-Bilinear Control Systems” (2017 preprint).** [Primary full text](https://arxiv.org/html/1705.00160v1).

**Access:** full-text inspection covers equation (3.1), Volterra kernels (3.2)–(3.5), Theorems 3.1–3.2, Remark 3.3, and Theorem 4.5. The framework supplies Volterra-based reachability/observability Gramians and reduction; setting the quadratic state term to zero gives the bilinear case. It does not impose preservation of a probability simplex, detailed balance, or an exact passive visible path law.

**Our mapping:** write the column generator as $A(h)=\sum_{j\ge0}h^jA_j$, with $A_0p_0=0$. Its coefficient equations are $\dot p_n=A_0p_n+\sum_{j=1}^n A_jp_{n-j}u^j$, $1\le n\le3$. Stacking these states and lifting the input to $(u,u^2,u^3)$ gives a bilinear system; the three lifted inputs are constrained, not independent actuators. Restricting coefficient states to the zero-mass subspace removes the stationary eigenvalue. These signed coefficient states are not Markov probabilities. Thus the formal realization framework is established, while a reduced physical model satisfying our passive-law and reversibility constraints still needs a separate construction.

**Fritz Gesztesy and Barry Simon, “m-Functions and inverse spectral analysis for finite and semi-infinite Jacobi matrices” (1997).** Journal d'Analyse Mathématique 73, 267–297. [Author-hosted primary PDF](https://math.caltech.edu/SimonPapers/261.pdf), [DOI](https://doi.org/10.1007/BF02788147).

**Access:** Theorem 3.5 and the equivalent Appendix Theorem A.6, including the Gram–Schmidt proof, were inspected. Every probability measure supported at $n$ distinct points is the endpoint spectral measure of a unique $n\times n$ Jacobi matrix with positive off-diagonal entries.

**Our corollary:** apply this theorem to $\nu=\tfrac12\delta_0+\sum_j[c_j/(2W)]\delta_{-\lambda_j}$. A similarity using the positive zero eigenvector converts the Jacobi matrix to an irreducible reversible birth–death generator. The zero spectral weight fixes the endpoint stationary probability at $1/2$; the centered endpoint readout then takes only the values $\pm\sqrt W$ and has autocorrelation $C(t)$. This yields $r+1$ hidden states for $r$ distinct active modes, hence $r+2$ total states after adding $A$. [Theory, Section 9](THEORY.md) gives the proof. Inverse spectral realization is established mathematics; this application and its bounded readout do not establish a new general realization theory. Combined with the core pole bound, it settles the generic exact state count when no $\lambda_j=k$.

## Positive exponential approximation

**Yohei M. Koyama, “Exponential sum approximations of finite completely monotonic functions” (2023, version 3).** [Primary full text](https://arxiv.org/html/2301.08931v3).

**Access:** the follow-up inspected Lemma 2.2, Theorems 2.14 and 3.14, and Corollary 3.15. On a finite positive spectral interval $[a,b]$, Lemma 2.2 gives positive quadrature nodes and weights with exact mass preservation. Theorem 2.14 bounds uniform-time error by $(16/\pi)W\widehat\rho^{-2m}$. Theorem 3.14 optimizes the analytic transformation, giving $\widehat\rho=\exp[\pi\mathsf K(a/b)/\mathsf K(\sqrt{1-(a/b)^2})]$, where $\mathsf K$ is the complete elliptic integral.

**Our comparison:** clamp the original rates to $[k\eta,k/\eta]$; this costs at most $W\eta$ in the normalized damped integral norm. Applying the positive mass-preserving quadrature theorem to the clamped measure then gives an $O(\log^2(1/\eta))$ mode count, using the standard elliptic-integral asymptotics. The root-exponential order is therefore a short adaptation of established approximation theory, even without a fixed original spectral interval. Our geometric-bin moment proof provides an elementary explicit certificate, not a new approximation mechanism or optimality theorem. The operational application is its transfer to all bounded protocols and realization under the stated Markov constraints.

## Recent sources: full-text follow-up

**Jiming Zheng and Zhiyue Lu, “The Memory Hidden in Response Fluctuations: Trajectory-Level Fluctuation-Response Theory and Inequalities for Non-Markovian Jump Dynamics” (2026).** [Primary record](https://arxiv.org/abs/2608.20328).

**Access:** initialization reached the primary abstract only; the follow-up inspected [v2 HTML](https://arxiv.org/html/2608.20328v2) (9 September 2026), especially Sections II.4 and VII.1–VII.2, Eqs. (164)–(174). The paper defines response sufficiency relative to an observable, an edge-perturbation family, and a horizon through a response-heterogeneity residual. Its four-state example merges $A_+$ and $A_-$: waiting times, stationary occupations, mean fluxes, and total activity match a state-only Markov surrogate, while exit direction retains previous-state and residence-age information. Consequently that example does **not** have equality of complete passive visible path laws. The physical rate sensitivity is additional information for applying a particular control.

**Comparison:** task-dependent response memory is already an explicit framing. Our target is a stronger passive indistinguishability condition, an equilibrium field rule, and cubic single-time mean state complexity. These distinctions do not establish that the sharp theorem is new. The inspected sections supply no corresponding all-size cubic pole-count theorem.

**Abhishek Chowdhury, “Hidden kinetic correlations control collective phases of entropy-conditioned histories” (2026).** [Primary record](https://arxiv.org/abs/2609.16355).

**Access:** initialization confirmed only the listing; the follow-up inspected the [v1 full text](https://arxiv.org/html/2609.16355v1) (14 September 2026), especially Sections II and X and Appendix K.1, Proposition 2. Its matched comparisons preserve the complete ordinary visible process and specified thermodynamic diagnostics. In its ten-state example, the ordinary visible bit is a telegraph process; entropy selection produces visible memory. Proposition 2 characterizes autonomous selected dynamics by a common positive hidden eigenvector; reversibility at the entropy midpoint additionally connects autonomy to stationary visible Markovianity.

**Comparison:** this is close prior art for exact passive agreement surviving many diagnostics yet failing after changing the dynamical question. Our intervention is an imposed field with reversible rates, not conditioning histories by their full entropy and applying a Doob transform to a driven hidden network. Our cubic single-time mean kernel and sharp analytic-surrogate state count are additional, specific targets absent from the inspected result. A broad claim that exact passive compression need not remain valid under changed dynamics would overlap substantially with this paper.

The two 2026 papers are preprints in the versions inspected. Successful access permits the comparisons above; it does not constitute independent verification of their proofs or an exhaustive citation search.

## Sampled-response lower bounds: source audit

**Clara Lacroce, Borja Balle, Prakash Panangaden, Guillaume Rabusseau, “Optimal approximate minimization of one-letter weighted finite automata” (2024).** [Publisher full text](https://www.cambridge.org/core/journals/mathematical-structures-in-computer-science/article/optimal-approximate-minimization-of-oneletter-weighted-finite-automata/9733CA9F3079F9186103F8515DE86D96), [author manuscript](https://claralacroce.github.io/static/Lacroce_journal.pdf).

**Access:** both full texts inspected, particularly Theorem 2 and Section 3, Theorem 16. They recall the classical rank/state correspondence of Carlyle–Paz and Fliess and the Eckart–Young singular-value obstruction. The paper also explains why a truncated singular-value decomposition need not preserve Hankel structure. **Comparison:** our sampled coefficient lift uses this established reasoning. Transferring a finite matrix obstruction to the bounded-protocol cubic-response norm is a separate step; their optimal Hankel-norm approximation does not assert an admissible Markov realization or our error metric.

**Georgios Kotsalis and Jeff S. Shamma, “Limits of performance for the model reduction problem of hidden Markov models” (2015).** CDC 2015, 4674–4679. [Primary institutional record](https://experts.illinois.edu/en/publications/limits-of-performance-for-the-model-reduction-problem-of-hidden-m/), [DOI](https://doi.org/10.1109/CDC.2015.7402948).

**Access:** the primary abstract and indexed introduction were inspected. The [KAUST manuscript](https://repository.kaust.edu.sa/bitstreams/f7535c55-d4d3-4ebf-a668-0d3017a43749/download) was located, but full-text retrieval failed. The authors already bound approximation by lower-order hidden Markov models using Hankel singular values. **Comparison:** a general stochastic dimension-witness claim would overlap with this work. Its exact assumptions and norm conversion have not been checked at theorem level; neither equivalence to nor exclusion of our cubic-response result is asserted.

**Simon Becker and Carsten Hartmann, “Infinite-dimensional bilinear and stochastic balanced truncation with explicit error bounds” (2019).** Mathematics of Control, Signals, and Systems 31, 1–37. [Primary full text and DOI](https://doi.org/10.1007/s00498-019-0234-8).

**Access:** Definition 3.2, Corollary 3.3, and Theorems 1–2 were inspected. The Volterra-based Hankel operator factors through the state space, and its trace distance bounds output differences under specified stability and input assumptions. **Comparison:** this establishes the relevant realization framework. Their small-gain and bounded-energy conditions do not describe our complete surrogate class or all bounded protocols. Our constant-step coefficient lift and finite-sample error estimate avoid imposing those extra conditions; the underlying factorization is not new.

**David W. Kammler, “$L_1$-Approximation of Completely Monotonic Functions by Sums of Exponentials” (1979).** [Primary publisher record and DOI](https://doi.org/10.1137/0716003).

**Access:** publisher abstract inspected; full text not obtained. The abstract states that a best $L_1$ approximation to a completely monotone function among real exponential sums has positive coefficients and positive decay rates. **Comparison:** this supports the classical status of positive exponential approximation. It does not permit restricting our general Markov surrogates to positive kernels: their cubic coefficients can contain signed residues and exponential-polynomial terms. A kernel approximation lower bound would still require a valid transfer into our response norm.

**Dietrich Braess and Wolfgang Hackbusch, “On the approximation of Stieltjes functions by exponential sums and rational functions with applications to partial differential equations” (2026).** Numerische Mathematik 158, 455–490. [Primary full text and DOI](https://doi.org/10.1007/s00211-025-01523-1) (version of record published 29 December 2025).

**Access:** Sections 4.2.1–4.2.2, Theorem 4.3, and Eq. (4.14) inspected. They establish exponential approximation on finite intervals and root-exponential upper bounds for inverse powers on an infinite interval; the text distinguishes upper bounds from numerical indications about sharp constants. **Comparison:** these are established approximation mechanisms in different norms and target classes. They provide no direct matching lower bound for our analytic Markov response task. The spectral restriction and response-norm transfer must be stated explicitly.

## What this follow-up resolves

The coarse-response example's passive non-Markovianity is now verified from its actual model. The recent response-memory paper matches fewer passive statistics than our target; the recent entropy-selection paper matches the complete passive process and is therefore the closer conceptual comparison. Controlled reduction requires particular care over whether the *same actuator protocol* is retained or controls can be remapped. These findings narrow the possible contribution to the explicit combination of assumptions, cubic kernel characterization, and exact-versus-approximate state complexity. They do not certify that combination as publishably new.

The new lower-bound argument makes a concrete bridge to standard realization theory. A constant-step cubic coefficient of a $D$-state analytic Markov model has a linear lift of dimension at most $1+3(D-1)$. Sampling and applying a fixed finite-difference filter do not increase its Hankel rank. The target's filtered samples form a positive moment matrix; its singular values, together with a bound on the filter's error amplification, obstruct approximation in the actual response norm. This is an application of established rank reasoning, with model-specific target construction and norm conversion. It is not a new general Hankel or minimal-realization theorem.

For fixed positive $WU^3$, the [finite-accuracy results, Sections 8 and 10](FINITE_ACCURACY.md) now bracket the unrestricted-rate minimax state requirement between $\Omega(\log(1/\varepsilon))$ and $O(\log^2(1/\varepsilon))$ as $\varepsilon\downarrow0$. Restricting only the **target's active hidden rates** to $\lambda\le3k$ gives a matching $\Theta(\log(1/\varepsilon))$ order (Section 10.5). The comparison class of analytic Markov surrogates remains unchanged: no rate cap, reversibility, positive-residue assumption, or generator-derivative bound is added to it. The capped-target theorem is a distinct restricted problem and does not close the unrestricted-rate gap.

## Open publication gates

The first gate is a precise comparison of the combined theorem with the closest response, controlled-reduction, and stochastic-realization results. The exact separation, sampled-response lower bound, and capped-target matching tolerance order are specific mathematical statements; their derivation here does not establish publication novelty. The linear lift, Hankel rank obstruction, positive quadrature, and inverse spectral realization are established ingredients. The unavailable HMM full text remains a concrete comparison gap, and further citation tracing could reveal a closer theorem.

The second gate is operational significance: explain what preserving the same actuator, passive path law, and cubic mean response buys a user of the surrogate. The finite-sample witness certifies coefficient-approximation limits; it is not yet a noisy experimental protocol, a statistical reconstruction guarantee, or a finite-amplitude prediction theorem. The active-rate cap needs an explicit physical interpretation if the matching theorem is foregrounded. The third gate is a clear physical account retaining these assumptions without an unsupported turbulence label.

The unrestricted-rate logarithmic-versus-squared-logarithmic tolerance gap remains open. A universal fixed-error lower bound growing with microscopic $N$ remains incompatible with the constructive upper bounds at bounded coupling and protocol amplitude. No conclusion about this project's novelty follows merely because the bounded search did not locate its exact theorem.

No exhaustive citation graph, independent proof review, or journal assessment has been completed. The [current work order](../work_orders/CURRENT.md) turns these limitations into concrete next tasks.
