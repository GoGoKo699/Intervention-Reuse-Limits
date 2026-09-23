# Source comparison for the matrix principle and kinetic-variance compression

[Matrix prediction principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) · [Kinetic-variance compression](KINETIC_VARIANCE_COMPRESSION.md) · [Earlier finite-realization audit](FINITE_ADVANTAGE_SOURCE_AUDIT.md) · [Earlier matrix-precision audit](FINITE_PRECISION_SOURCE_AUDIT.md)

**Primary-source audit, 23 September 2026.** The matrix principle is a new generalization within this repository: it identifies minimum state counts for a specified controlled continuous-time prediction task. Static positive factorization, stochastic normalization, completely positive mixtures, and projection-based memory equations are established ingredients. The six primary sources below were inspected in full text at the indicated locations. This focused comparison neither certifies priority nor classifies all reversible hidden Markov models. It is separate from the internal mathematical review of the linked proofs.

## 1. The exact claim being compared

For every completely positive matrix $H$ with $v=H1>0$ and $1^{\mathsf T}H1=1$, the [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) constructs a common controlled task satisfying

$$
D_{\rm all}(0)=1+n+\operatorname{rank}_+(H),\qquad
D_{\rm ord}(0)=1+n+\operatorname{cprank}(H).
$$

The $n$ probe labels are distinct; memory states share one label. Both classes use the same hub interface, stationary preparation, binary readout, two fields, positive clock and hidden exit cap. Rivals may choose new hidden states, masses and endpoint barriers. Ordinary reversibility means detailed balance with identity reversal of the hidden states.

The target's nonzero hidden decay rates remain in $[k,3k]$, and its passive zero-field binary path law is exactly two-state Markov. The larger minimum counts therefore concern reuse under interventions. Probe labels specify kinetic rates, not additional observed output symbols.

Three steps distinguish this statement from a static factorization identity:

1. Every nonnegative factorization supplies a stationary continuous-time model whose stochastic intertwiner respects every current field and the binary readout. Completely positive factors supply ordinarily reversible models. The resulting models agree for all protocols and horizons, including their binary-output path laws.
2. Controlled means recover a positive left/right feature matrix. In an arbitrary rival it factors through its actual hidden states; under ordinary detailed balance the two sides become adjoints, giving a nonnegative-feature Gram. On the target this matrix is $\operatorname{diag}(H/2,\operatorname{diag}(v)/2)$.
3. Uniform capped clock recovery and closure of the bounded-factor-count matrix classes give a positive, matrix-dependent accuracy interval and a finite experiment set. This is an existence statement, without a useful general tolerance or menu-size bound.

The simultaneous dynamic upper and lower bounds are the repository contribution under comparison. Neither the familiar rank definitions nor their elementary interpretation as latent factor counts is claimed as new. The growing probe-label count and the prescribed hub geometry remain assumptions.

## 2. Closest factorization and realization sources

### A. Nonnegative rank already has a stochastic membership interpretation

**Anru Zhang and Mengdi Wang**, “Spectral State Compression of Markov Processes,” *IEEE Transactions on Information Theory* **66**(5), 3202–3231 (2020), [DOI:10.1109/TIT.2019.2956737](https://doi.org/10.1109/TIT.2019.2956737). **Access:** full [arXiv:1802.02920v3](https://arxiv.org/pdf/1802.02920v3), including the supplementary proof, inspected.

Section 3, Definition 2 and Proposition 2 identify nonnegative rank with the least size of a latent membership representation of a homogeneous Markov transition kernel. The factors can be normalized to probability distributions; the proposition is proved in Supplement A.2. This directly precedes the stochastic normalization of incoming and outgoing factors used here.

Their object is a discrete-time transition kernel and its state-compression representation. These results do not identify the minimum stationary continuous-time predictors of every controlled binary mean, impose the repository's hub interface, or pair that minimum with a completely positive rank minimum under ordinary detailed balance. A stochastic factorization is an established ingredient, not by itself the present controlled realization theorem.

### B. Length-two HMM realization uses a different structured rank

**Bart Vanluyten, Jan C. Willems and Bart De Moor**, “Structured nonnegative matrix factorization with applications to hidden Markov realization and clustering,” *Linear Algebra and its Applications* **429**(7), 1409–1424 (2008), [DOI:10.1016/j.laa.2008.03.010](https://doi.org/10.1016/j.laa.2008.03.010). **Access:** full [author-hosted published PDF](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2008.1.pdf) inspected.

Section 5, Eq. (16), writes the length-two output probability matrix as

$$
P=B^{\mathsf T}\operatorname{diag}(\pi)\Pi B.
$$

Minimizing its HMM state dimension is a structured nonnegative factorization problem $P=VAV^{\mathsf T}$. Their normalization reconstructs emissions, transition matrix and initial law; the application explicitly matches strings of length two. It does not establish compatibility with every longer string or a controlled family of generators. Sections 3–4 separately treat structured and completely positive factorizations. This is a close realization precedent, but it does not equate a generic HMM minimum with either rank in the repository theorem.

### C. Symmetry of a middle factor is weaker than complete positivity

**Damjana Kokol Bukovšek and Helena Šmigoc**, “Symmetric Nonnegative Matrix Trifactorization,” *Linear Algebra and its Applications* **665** (2023), [DOI:10.1016/j.laa.2023.01.027](https://doi.org/10.1016/j.laa.2023.01.027). **Access:** full [arXiv:2106.14437v2](https://arxiv.org/html/2106.14437v2), dated 12 May 2022, inspected; the publisher DOI page did not open in this audit, so theorem numbering refers to that preprint.

Definition 1.1 minimizes the inner dimension of $A=BCB^{\mathsf T}$ with $B,C\ge0$ and $C=C^{\mathsf T}$. Proposition 2.1 proves

$$
\operatorname{rank}_+(A)\le\operatorname{st}_+(A)\le\operatorname{cprank}(A).
$$

The paper explicitly connects symmetric trifactorization to HMM identification. For generic stationary reversible discrete-time HMM one-step pair data, the flux $\operatorname{diag}(\pi)\Pi$ is symmetric and nonnegative; this alone does not make it a nonnegative Gram factor. The repository uses adjoint-paired positive tests to identify its particular completely positive matrix. These are distinct ranks and distinct observations; the continuous-time qualification below matters.

### D. Completely positive factors already count static mixture components

**Drew Fudenberg and Giacomo Lanzani**, “Conditionally I.I.D. Models,” working paper dated 13 January 2026. **Access:** full [author-hosted PDF](https://economics.mit.edu/sites/default/files/inline-files/psd_decisiontheory_drew_giacomo-46.pdf) inspected. No journal publication is asserted here.

Theorem 2 and Claim 1, pp. 9–10, characterize two-period conditional-i.i.d. representations by complete positivity of a normalized joint matrix. Their simplex normalization writes it as $\sum_s\gamma_s p_sp_s^{\mathsf T}$ with probability vectors $p_s$. Section 5.2 and Appendix A.10 bound support size below by completely positive rank. Combining that bound with their factor normalization identifies the minimum static support count; this last equality is an immediate inference from those ingredients.

This provides a direct probabilistic interpretation of the same nonnegative Gram factors. It is a static Bayesian mixture representation, with no controlled continuous-time evolution or detailed-balance predictor minimum. The repository's dynamic integration of these factors is the separate issue.

## 3. A five-state reversible HMM is an essential counterpoint

Consider the normalized incidence matrix already used in the repository,

$$
H=\frac1{24}
\begin{pmatrix}
3I_2&\mathbf1_{2\times3}\\
\mathbf1_{3\times2}&2I_3
\end{pmatrix},\qquad v=H1.
$$

Its nonnegative rank is five and its completely positive rank is six; the established matrix sources and repository support proofs are recorded in the [finite-precision source audit](FINITE_PRECISION_SOURCE_AUDIT.md) and [finite minimum-count proof](FINITE_PREDICTOR_MINIMALITY.md).

Nevertheless, a **five-state stationary reversible discrete-time HMM** realizes $H$ as its length-two output law. Take deterministic emissions $B=I_5$, stationary law $v$, and transition matrix

$$
M=\operatorname{diag}(v)^{-1}H.
$$

Then $M1=1$, $v^{\mathsf T}M=v^{\mathsf T}$ when $v$ is written as a column, and $v_iM_{ij}=H_{ij}=H_{ji}=v_jM_{ji}$. Its output pair matrix is exactly $H$. Equivalently, $\operatorname{st}_+(H)=5$, since it lies between $\operatorname{rank}_+(H)=5$ and the matrix size five.

This calculation is our elementary application of the factorization framework, not a claim that the cited papers studied this particular dynamical example. It shows why completely positive rank is not a generic lower bound on reversible HMM order for pair data. No continuous-time embedding of $M$ is asserted. This HMM is not the shared-hub controlled predictor of the matrix principle: it observes five symbols and is only being asked to reproduce a pair distribution. In the repository task, the stronger positive Gram is recovered using controlled binary means and adjoint-paired words. The total minima there are eleven and twelve, including the hub and five probes.

For an ordinarily reversible **continuous-time** chain, identical-output stationary pair data at lag $t$ do have a completely positive factorization. If $E_t=e^{tQ}$ and $B\ge0$ is the emission matrix, detailed balance and the semigroup law give

$$
B^{\mathsf T}\operatorname{diag}(\pi)E_tB
=(E_{t/2}B)^{\mathsf T}\operatorname{diag}(\pi)(E_{t/2}B).
$$

All factors are nonnegative. This elementary half-time identity is consistent with the repository's Gram mechanism. The five-state counterpoint concerns generic discrete-time pair realization; it does not invalidate this continuous-time fact. The controlled theorem additionally identifies the specific rank-bearing matrix from its prescribed binary-mean task and supplies matching models under the same interface.

## 4. Two close precedents for the variance theorem

### E. Uniform-in-time Markov coarse-graining is already established

**Bastian Hilder and Upanshu Sharma**, “Quantitative Coarse-Graining of Markov Chains,” *SIAM Journal on Mathematical Analysis* **56**(1), 913–954 (2024), [DOI:10.1137/22M1473996](https://doi.org/10.1137/22M1473996). **Access:** full [arXiv:2201.10256v2](https://arxiv.org/pdf/2201.10256v2) inspected.

Equation (18) averages the microscopic rates against conditional stationary measures. Theorem 3.1, Eq. (20), gives a relative-entropy approximation bound uniform in time under a uniform conditional logarithmic Sobolev inequality, without explicit scale separation. Its constant depends on the original/effective generators and stationary law. Remark 3.2 distinguishes a stronger finite-horizon estimate; Corollary 3.6 gives a decaying long-time bound.

The microscopic generator is autonomous. Its projected marginal generator can depend on time through evolving conditional laws; that is not arbitrary external switching. The [repository variance theorem](KINETIC_VARIANCE_COMPRESSION.md) instead exploits its special hub geometry to obtain an explicit stationary-barrier-variance bound for every allowed protocol and horizon, using a symmetric gap and common hidden law, without a state-count or minimum-mass factor. Averaging and uniform-time error control themselves are not new claims.

### F. Entering and leaving the discarded subspace is classical memory-kernel structure

**Hazime Mori**, “Transport, Collective Motion, and Brownian Motion,” *Progress of Theoretical Physics* **33**(3), 423–455 (1965), [DOI:10.1143/PTP.33.423](https://doi.org/10.1143/PTP.33.423). **Access:** full published scan [hosted by UC San Diego](https://courses.physics.ucsd.edu/2020/Fall/physics210b/Mori-1965.pdf) inspected, especially Section 3, Eqs. (3.7)–(3.12), printed pp. 430–431.

Mori derives an exact projected equation with a memory kernel expressed through the orthogonal force autocorrelation. The resulting two-sided coupling through discarded variables is the classical structural precedent for exciting hidden deviations and reading them back. The source treats microscopic Liouville dynamics and its projection; it does not provide the present finite Markov hub constants or an all-protocol barrier-variance bound. The repository's exact kernel and energy estimate specialize that established projection mechanism. Calling the quadratic mechanism itself a newly discovered principle would overstate the comparison.

## 5. Bounded assessment and remaining limits

The inspected sources establish the constituent rank interpretations and projection mechanisms. Their stated results do not supply the paired controlled-predictor minima of the matrix principle. The defensible description is therefore a **general realization principle for this specified controlled architecture**, new to this repository, with established algebraic ingredients. This is neither an exhaustive literature conclusion nor a journal-fit judgment.

The variance result supplies the complementary coarse-accuracy statement: a two-state reversible predictor can hide extensive internal structure when barrier variance is small relative to mixing and visible damping. Its claim concerns binary means, not the entire output path law. The conditional-variance extension requires an invariant conditional-averaging subspace; arbitrary grouping of kinetic labels does not suffice. On a continuous field interval an arithmetic average of exponential barriers need not belong to the original single-exponential family; matching the two queried endpoints avoids that separate issue.

The exact matrix classification and the variance upper bound concern different accuracy regimes. Neither removes the fixed physical-parity assumption, proves an unavoidable thermodynamic dissipation cost, supplies a generic HMM minimum, or establishes a practical measurement precision for every matrix. Earlier sources on static positive realization, individual matrix rank gaps and stochastic intertwining remain documented in the linked frozen audits.
