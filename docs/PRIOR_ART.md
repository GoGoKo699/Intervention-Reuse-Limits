# Prior-art and novelty audit

[Repository overview](../README.md) · [Exact theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

**Updated 22 September 2026, including the publication-scope comparison.** This is a bounded audit, not a certification of novelty. A derivation obtained independently here may still be known. Access depth and version are recorded below. Earlier failed retrievals remain provenance; a later successful inspection supersedes the associated access limitation, not the need for a complete novelty audit. The [scope assessment](PUBLICATION_SCOPE.md) identifies the candidate combined theorem and its operational interpretation.

## Claims being screened

The exact target combines: equality of the complete passive visible Markov path law; a specified reversible field-dependent rate rule; matching static and dynamic linear mean response; and an all-size sharp separation between passive state count and exact cubic-response state count.

The extension retains nonvanishing total response with bounded coupling, then gives a protocol-uniform cubic approximation certificate and an explicit reversible Markov realization whose size is independent of the original state count. Sampled and continuous Hankel witnesses give lower bounds against the broad analytic Markov surrogate class, completing the worst-case tolerance order. The coefficient tolerance, known kinetic kernel, and freedom to change microscopic rates are essential assumptions.

The broad claims below are **not** prospective contributions: hidden kinetics affect nonlinear response; the same unperturbed process can respond differently under different kinetic implementations of a thermodynamically identical perturbation; one can coarse-grain response; Volterra kernels admit state realizations; positive sums of exponentials can be approximated by shorter sums; Hankel rank and singular values obstruct low-dimensional approximation.

## Established response theory

**Urna Basu, Matthias Krüger, Alexandre Lazarescu, Christian Maes, “Frenetic aspects of second order response” (2015).** Physical Chemistry Chemical Physics 17, 6653–6666. [Primary full text](https://arxiv.org/html/1410.7450v2), [DOI](https://doi.org/10.1039/C4CP04977B).

**Access:** initialization inspected the response framework; the publication-scope follow-up inspected v2 (3 March 2015), especially Section III.1 and Section IV.1, Eqs. (20)–(27) and Figure 3. The zero-range example keeps the unperturbed process fixed and implements the same chemical-potential change through two different entry/exit rate rules. Linear response agrees; second-order response differs. Thus even equality of the complete passive law, together with a common thermodynamic field change, is insufficient as a novelty distinction.

**Comparison:** in our within-family comparisons at fixed state labels, $k,\mu,g$ and their displayed field dependence can remain fixed while the reversible internal generator $K$ varies. The complete microscopic generator is not held fixed. This isolates hidden kinetics without changing the prescribed actuator rule. The state-complexity question, rather than the general kinetic origin of nonlinear response, is the candidate contribution.

**Gregor Diezemann, “Nonlinear response theory for Markov processes: Simple models for glassy relaxation” (2012).** Physical Review E 85, 051502. [Primary record](https://arxiv.org/abs/1203.1785), [DOI](https://doi.org/10.1103/PhysRevE.85.051502).

**Access:** the supplied checkpoint recorded full-text inspection and initialization reconfirmed the abstract. The publication-scope follow-up inspected [v1 full text](https://arxiv.org/html/1203.1785v1), particularly Eqs. (4)–(5), (25), Figure 6, and Appendix A. The general master-equation expansion allows analytic field dependence and gives response through third order. In the trap-model comparison, changing kinetic field-coupling parameters while holding their thermodynamic sum fixed leaves the zero-field generator and linear susceptibility unchanged, but changes cubic response.

**Comparison:** cubic response and passive agreement with different nonlinear behavior are already present when the kinetic actuator implementation changes. Our comparison instead retains the specified rate-rule parameters while varying $K$, and asks for exact and approximate Markov state requirements. The response formulas themselves are not a contribution. The inspected results do not provide the repository's state-budget minimax theorem or its protocol-uniform coefficient norm.

**Fenna Müller, Urna Basu, Peter Sollich, Matthias Krüger, “Coarse-grained second-order response theory” (2020).** Physical Review Research 2, 043123. [Primary record](https://arxiv.org/abs/2005.05169), [DOI](https://doi.org/10.1103/PhysRevResearch.2.043123).

**Access:** the initialization pass reached the abstract only; the follow-up inspected [arXiv v2 full text](https://arxiv.org/html/2005.05169v2) (29 November 2020), especially Sections II–IV, Eq. (30), and Appendix A.4. The paper obtains arbitrary-protocol second-order response from coarse path-weight derivatives measured with step perturbations. Its four-state chain has blocks $\{A,B\}$ and $\{C,D\}$ with only the $B$–$C$ edge crossing blocks. Section IV.1 explicitly identifies the finite-rate passive coarse process as non-Markovian; zero and nonzero cross-block exit rates within a block also show this directly. Appendix A.4 treats a Markov coarse description but does not establish preservation under our hidden-dependent kinetic field rule.

**Comparison:** response reconstruction from reduced observations is established. The displayed example does not give our exactly Markov passive telegraph process or a sharp all-size Markov-surrogate state-count separation. Our equilibrium potential acts on visible states, so the paper's framework is relevant; the order change to cubic is not by itself a novelty argument. Its step measurements include linear response of coarse joint probabilities, which must not be confused with our matching of the single-time mean's linear response.

**Kirsten Engbring, Dima Boriskovsky, Yael Roichman, Benjamin Lindner, “A Nonlinear Fluctuation-Dissipation Test for Markovian Systems” (2023).** Physical Review X 13, 021034. [Author-hosted full text](https://people.physik.hu-berlin.de/~lindner/PDF/Engbring_PhysRevX_2023.pdf), [DOI](https://doi.org/10.1103/PhysRevX.13.021034).

**Access:** published full text inspected, especially Section II.A, Eqs. (3)–(8). Its nonlinear relation compares passive correlations with relaxation after a stationary perturbation is switched off. The conjugate observable is the ratio of perturbed to unperturbed stationary densities minus one. This is a perturbation-arrest diagnostic, not a finite-state approximation theorem for a field that remains on.

**Our comparison, derived from strong lumpability:** prepare our model at any constant field $h_0$, then set $h=0$. For every $K$,

$$
m_{\mathrm{arrest}}(t)=\tanh(h_0)e^{-2kt}.
$$

The visible stationary-density ratio gives $z(S)=\tanh(h_0)S$, so

$$
C_{zz}(t)=\tanh^2(h_0)e^{-2kt}
=\mathbb E_{\mathrm{arrest}}z(t).
$$

Thus the family satisfies this diagnostic at every finite $h_0$, while its field-on cubic response can vary with $K$. This distinction follows from our model; it neither contradicts the cited relation nor establishes a new Markovianity test.

## Aggregation and realization

**Luca Cardelli, Radu Grosu, Kim Guldstrand Larsen, Mirco Tribastone, Max Tschaikowski, Andrea Vandin, “Lumpability for Uncertain Continuous-Time Markov Chains” (2021).** QEST 2021, 391–409. [Institutional record](https://vbn.aau.dk/en/publications/lumpability-for-uncertain-continuous-time-markov-chains/), [DOI](https://doi.org/10.1007/978-3-030-85172-9_21).

The initialization pass inspected bibliographic information and the abstract. The [author manuscript](https://www.iris.santannapisa.it/retrieve/dd9e0b32-58f9-709e-e053-3705fe0a83fd/qest2021.pdf) was located in the follow-up, but sustained retrieval failed; no new theorem-level claim is based on that file. The abstract concerns preservation of reachable probability sets under time-varying interval uncertainty. The subsequent journal extension provides the accessible theorem-level comparison below.

**The same authors, “Algorithmic Minimization of Uncertain Continuous-Time Markov Chains” (2023).** IEEE Transactions on Automatic Control 68, 6557–6572. [DOI](https://doi.org/10.1109/TAC.2023.3244093), [accepted manuscript, DTU](https://backend.orbit.dtu.dk/ws/files/318778353/HKKR_Algorithmic_Minimization_of_Uncertain_Continuous_Time_Markov_Chains.pdf).

**Access:** accepted full text inspected, notably Introduction, Theorem 2, Definition 4, Theorems 5–6, and Appendix C's control correspondence. Theorem 2 gives pointwise block-rate equalities for time-varying ordinary lumpability. Definition 4 instead requires lumpability of both endpoint generators of an interval-rate family; Theorems 5–6 characterize preservation of extremal value functions for block-constant rewards. The authors explicitly distinguish this from every realized CTMC being lumpable.

**Comparison:** their uncertain reduction can use corresponding, different control functions in the original and reduced systems. It does not assert equality under the same specified scalar actuator $h(t)$, as required here. Replacing our coupled rate family by independent intervals changes the admissible interventions. Ordinary lumpability applied pointwise already proves our block-uniform preservation boundary; that observation is not a new theorem. Neither failure of a partition criterion nor an uncertain-control reduction alone settles our broader lower bound over arbitrary analytic Markov surrogates.

**Arthur E. Frazho, “A Shift Operator Approach to Bilinear System Theory” (1980).** SIAM Journal on Control and Optimization 18(6), 640–658. [Primary publisher record](https://epubs.siam.org/doi/10.1137/0318049).

The publisher abstract describes bilinear realization of Volterra input-output maps, minimality linked to reachability and observability, and finite realizability through rational transforms. Full text was not obtained; its precise theorem statements remain unaudited. The accessible full-text successor below establishes the classical framework comparison without requiring that historical access gap to be closed. The pole-location lemma is standard realization reasoning, not an independent innovation.

**Mihály Petreczky, “Realization theory for linear and bilinear switched systems: A formal power series approach. Part II: Bilinear switched systems” (2011).** ESAIM: COCV 17, 446–471. [Primary full text](https://www.numdam.org/item/10.1051/cocv/2010015.pdf).

**Access/comparison:** Section 2.1 and Theorem 2.3 were inspected. For arbitrary switching, minimal bilinear realization dimension equals Hankel rank, equivalently semi-reachability and observability; minimal realizations are isomorphic. A single mode recovers the ordinary bilinear framework. This is exact realization in unrestricted real coordinates, without an approximation norm or Markov constraints. Our signed coefficient lift fits that framework, but its input channels $(u,u^2,u^3)$ are constrained; unrestricted bilinear minimality cannot simply be identified with physical Markov state count.

**Peter Benner and Pawan Goyal, “Balanced Truncation Model Order Reduction For Quadratic-Bilinear Control Systems” (2017 preprint).** [Primary full text](https://arxiv.org/html/1705.00160v1).

**Access:** full-text inspection covers equation (3.1), Volterra kernels (3.2)–(3.5), Theorems 3.1–3.2, Remark 3.3, and Theorem 4.5. The framework supplies Volterra-based reachability/observability Gramians and reduction; setting the quadratic state term to zero gives the bilinear case. It does not impose preservation of a probability simplex, detailed balance, or an exact passive visible path law.

**Our mapping:** write the column generator as $A(h)=\sum_{j\ge0}h^jA_j$, with $A_0p_0=0$. Its coefficient equations are $\dot p_n=A_0p_n+\sum_{j=1}^n A_jp_{n-j}u^j$, $1\le n\le3$. Stacking these states and lifting the input to $(u,u^2,u^3)$ gives a bilinear system; the three lifted inputs are constrained, not independent actuators. For an irreducible reference generator, restricting coefficient states to the zero-mass subspace removes the stationary eigenvalue. These signed coefficient states are not Markov probabilities. Thus the formal realization framework is established, while a reduced physical model satisfying our passive-law and reversibility constraints still needs a separate construction.

**Timo Reis and Elena Virnik, “Positivity Preserving Balanced Truncation for Descriptor Systems” (2009).** SIAM Journal on Control and Optimization 48(4), 2600–2619. [DOI](https://doi.org/10.1137/080734200), [full author manuscript](https://www.researchgate.net/profile/Elena_Virnik/publication/220259131_Positivity_Preserving_Balanced_Truncation_for_Descriptor_Systems/links/00b7d5174f1aa6ed84000000.pdf).

**Access/comparison:** Theorems 3.1–3.2 give diagonal Lyapunov-inequality balancing for stable positive LTI systems and positive, stable truncations with $H_\infty$ error bounded by twice the discarded balancing values. These instance-specific values supply no uniform tolerance-to-state bound. Generally $H_\infty$ error does not control absolute damped $L_1$ error; when the impulse error is nonnegative, its $L_1$ norm equals its DC gain and the bound can transfer. The remaining requirements are a uniform state bound and a conservative reversible Markov embedding preserving the prescribed passive law.

**Luca Benvenuti and Lorenzo Farina, “A Tutorial on the Positive Realization Problem” (2004).** IEEE Transactions on Automatic Control 49(5), 651–664. [Full manuscript](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf).

**Access/comparison:** Theorem 2 characterizes exact positive realization through an invariant proper polyhedral cone; its extreme rays determine positive realization dimension. Our positive exponential kernel already has a diagonal positive LTI realization with one coordinate per mode. Converting it to an irreducible reversible stationary autocorrelation with bounded readout is a different requirement, addressed by the Jacobi corollary below.

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

**Access:** complete PDF retrieval failed. The publication-scope pass inspected indexed primary-manuscript excerpts containing Definitions 2.1–2.3, Lemma 2.1, Section IV.B, and Theorems 4.1–4.2 from the [KAUST manuscript](https://repository.kaust.edu.sa/bitstreams/f7535c55-d4d3-4ebf-a668-0d3017a43749/download). This is theorem-level partial access, not a claim to have read the entire paper. The stationary finite-alphabet process is specified by word probabilities. In the stable controllable/observable tree-system setting, Theorem 4.2 lower-bounds order-$k$ Hankel approximation error by the $(k+1)$st Hankel singular value.

**Comparison:** the stochastic Hankel dimension obstruction is established. Directly applying it to our passive visible word law gives no intervention bound: that law already has an exact two-state realization for every target. A response application first needs the coefficient lift, its norm estimate, and a physical Markov realization. The inspected theorem supplies the rank mechanism, not those additional conclusions. The remaining full-paper access limitation is not evidence for novelty.

**Simon Becker and Carsten Hartmann, “Infinite-dimensional bilinear and stochastic balanced truncation with explicit error bounds” (2019).** Mathematics of Control, Signals, and Systems 31, 1–37. [Primary full text and DOI](https://doi.org/10.1007/s00498-019-0234-8).

**Access:** Definition 3.2, Corollary 3.3, and Theorems 1–2 were inspected. The Volterra-based Hankel operator factors through the state space, and its trace distance bounds output differences under specified stability and input assumptions. **Comparison:** this establishes the relevant realization framework. Their small-gain and bounded-energy conditions do not describe our complete surrogate class or all bounded protocols. Our constant-step coefficient lift and finite-sample error estimate avoid imposing those extra conditions; the underlying factorization is not new.

**David W. Kammler, “$L_1$-Approximation of Completely Monotonic Functions by Sums of Exponentials” (1979).** [Primary publisher record and DOI](https://doi.org/10.1137/0716003).

**Access:** publisher abstract inspected; full text not obtained. The abstract states that a best $L_1$ approximation to a completely monotone function among real exponential sums has positive coefficients and positive decay rates. **Comparison:** this supports the classical status of positive exponential approximation. It does not permit restricting our general Markov surrogates to positive kernels: their cubic coefficients can contain signed residues and exponential-polynomial terms. A kernel approximation lower bound would still require a valid transfer into our response norm.

**Dietrich Braess and Wolfgang Hackbusch, “On the approximation of Stieltjes functions by exponential sums and rational functions with applications to partial differential equations” (2026).** Numerische Mathematik 158, 455–490. [Primary full text and DOI](https://doi.org/10.1007/s00211-025-01523-1) (version of record published 29 December 2025).

**Access:** Sections 4.2.1–4.2.2, Theorem 4.3, and Eq. (4.14) inspected. They establish exponential approximation on finite intervals and root-exponential upper bounds for inverse powers on an infinite interval; the text distinguishes upper bounds from numerical indications about sharp constants. **Comparison:** these are established approximation mechanisms in different norms and target classes. They provide no direct matching lower bound for our analytic Markov response task. The spectral restriction and response-norm transfer must be stated explicitly.

## Cauchy matrices and root-exponential lower bounds

**Dario Fasino, “Orthogonal Cauchy-like matrices” (2023).** Numerical Algorithms 92, 619–637; published online 5 September 2022. [Primary full text and DOI](https://doi.org/10.1007/s11075-022-01391-y).

**Access:** Section 2.1, Eqs. (5)–(8), including the inverse formula and its derivation, inspected in full. Fasino attributes these classical formulas to Samuel Schechter, “On the inversion of certain matrices” (1959), and Rod Gow (1992); Schechter's original article was located but not obtained. **Comparison:** specializing the displayed Cauchy inverse to $C_{ij}=1/(b_i+b_j)$ gives exactly $(C^{-1})_{ii}=2b_i\prod_{j\ne i}[(b_i+b_j)/(b_i-b_j)]^2$. Our geometric-rate lower bound uses this established identity. Its conversion into a response error floor depends separately on the coefficient lift, probability-weighted Hankel operator, and admissible target realization.

**Bernhard Beckermann and Alex Townsend, “On the singular values of matrices with displacement structure” (2016 preprint, version 1).** [Primary full text](https://arxiv.org/pdf/1609.09494v1).

**Access:** Theorem 2.1, Corollaries 3.2 and 4.2, and the Hilbert-matrix example Eq. (4.8) inspected. A low-rank Sylvester displacement with normal coefficient matrices gives singular-value upper bounds through Zolotarev numbers. For Cauchy matrices whose node sets lie in disjoint real intervals, the decay depends on the intervals' cross-ratio; the Hilbert example has exponent proportional to minus rank divided by logarithmic matrix size. **Comparison:** these are upper bounds, not the smallest-eigenvalue lower estimate needed here. The authors explicitly caution that sharp Zolotarev estimates need not yield sharp singular-value bounds. Our proof instead bounds the exact inverse directly.

**Herbert Stahl, “Best uniform rational approximation of $x^\alpha$ on $[0,1]$” (1993).** Bulletin of the American Mathematical Society 28, 116–122. [Primary full text, including proof sketch](https://arxiv.org/html/math/9301217v1).

**Access:** the rational approximation class, Theorem 1, and the proof outline inspected; this short article does not contain the complete proof. For fixed noninteger $\alpha>0$, its theorem gives $E_{nn}(x^\alpha,[0,1])\sim4^{1+\alpha}|\sin(\pi\alpha)|e^{-2\pi\sqrt{\alpha n}}$ for rational functions with numerator and denominator degrees at most $n$. **Comparison:** sharp root-exponential approximation barriers are established. This theorem concerns uniform rational approximation, not our damped kernel or protocol response norm. Transferring it would require a proved norm and degree reduction. Our finite Cauchy-matrix argument does not invoke that transfer.

## What this follow-up resolves

The coarse-response example's passive non-Markovianity is now verified from its actual model. The recent response-memory paper matches fewer passive statistics than our target; the recent entropy-selection paper matches the complete passive process and is therefore the closer conceptual comparison. Controlled reduction requires particular care over whether the *same actuator protocol* is retained or controls can be remapped. These findings narrow the possible contribution to the explicit combination of assumptions, cubic kernel characterization, and exact-versus-approximate state complexity. They do not certify that combination as publishably new.

The new lower-bound argument makes a concrete bridge to standard realization theory. A constant-step cubic coefficient of a $D$-state analytic Markov model has a linear lift of dimension at most $1+3(D-1)$. Sampling and applying a fixed finite-difference filter do not increase its Hankel rank. The target's filtered samples form a positive moment matrix; its singular values, together with a bound on the filter's error amplification, obstruct approximation in the actual response norm. This is an application of established rank reasoning, with model-specific target construction and norm conversion. It is not a new general Hankel or minimal-realization theorem.

The [unrestricted-rate proof](UNRESTRICTED_RATE_LOWER_BOUND.md) adds a continuous Hankel witness with probability weight $e^{-t}\,dt$ in dimensionless time, so its operator error is bounded by uniform constant-step response error. The surrogate lift has rank at most $3D-2$; subtracting the target's three-dimensional visible exponential-polynomial part leaves rank at most $3D+1$. A target with $r=3D+2$ positive modes at geometrically spaced rates has a Cauchy Gram matrix. The classical inverse formula gives the error floor $WU^3(64r^2)^{-1}e^{-2\pi\sqrt{3(r-1)}}$. This is a model-specific lower-bound construction using standard rank and matrix tools, not a new general Hankel theorem.

For fixed positive $WU^3$, the [finite-accuracy results, Sections 8 and 11](FINITE_ACCURACY.md) now give the matching unrestricted-rate minimax state requirement $\Theta(\log^2(1/\varepsilon))$ as $\varepsilon\downarrow0$. Restricting only the **target's active hidden rates** to $\lambda\le3k$ gives $\Theta(\log(1/\varepsilon))$ instead (Section 10.5). In both results the comparison class of analytic Markov surrogates is unchanged: no rate cap, reversibility, positive-residue assumption, or generator-derivative bound is imposed on it. The fixed-band sampled witness remains a separate finite coefficient-sample certificate; the stronger unrestricted-rate proof uses a continuous operator and targets whose spectral range grows with the state budget.

## Open publication gates

The [publication comparison](PUBLICATION_SCOPE.md) now identifies the candidate contribution more narrowly: optimal-order cubic approximation can retain reversibility, bounded sensitivity, and the prescribed passive and low-order response agreements, even when compared with stationary analytic Markov fits that abandon those agreements. The [class comparison](STRUCTURE_COST.md) makes this a proved corollary. The linear lift, Hankel obstruction, Cauchy inverse, positive quadrature, and inverse spectral realization remain established ingredients. The inspected HMM definitions and lower-bound theorem now permit a concrete comparison despite incomplete full-paper access; further work could still reveal a result covering the combined statement.

The scope note also specifies the operational use: compress a supplied kinetic model for reuse across weak protocols, with an active-rate cap describing extra information about hidden relaxation times. Its exact switch-off versus cubic field-on comparison explains which calibration records miss the hidden dynamics. This does not establish a molecular implementation, finite-amplitude prediction theorem, or noisy inference method. The remaining significance question concerns the usefulness and originality of that complete modeling statement, rather than another generic demonstration that nonlinear response detects kinetics.

The unrestricted-rate logarithmic-versus-squared-logarithmic tolerance gap is now closed within the stated model and error norm; sharp constants and an operational interpretation beyond coefficient approximation are not settled by that result. A universal fixed-error lower bound growing with microscopic $N$ remains incompatible with the constructive upper bounds at bounded coupling and protocol amplitude. No conclusion about this project's novelty follows merely because the bounded search did not locate its exact theorem.

No exhaustive citation graph, independent proof review, or journal assessment has been completed. The [current work order](../work_orders/CURRENT.md) turns these limitations into concrete next tasks.
