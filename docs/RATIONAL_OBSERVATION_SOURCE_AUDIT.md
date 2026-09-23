# Observable realization, rational transfer and symmetry compression: source audit

[Rational observation certificate](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Symmetry compression](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) · [Earlier finite precision audit](FINITE_PRECISION_SOURCE_AUDIT.md) · [Fixed-clock source audit](FIXED_CLOCK_PRIOR_ART.md)

**Focused primary-source comparison, 23 September 2026.** Stable realization from finite observable matrices, divided-difference operator calculus and second-order response are established subjects. This note identifies the closest inspected results and separates them from the repository's specific controlled-prediction claims. It does not certify external priority. Manuscript drafting remains deferred.

**Local status:** both linked research theorems have passed independent internal analytic reviews. The explicit ten-function target basis also has an independently checked rational certificate. Their constants below describe the repository's proved statements, not conclusions supplied or externally validated by the cited papers.

## 1. Robust realization from a finite matrix

**Samet Oymak and Necmiye Ozay, “Non-asymptotic Identification of LTI Systems from a Single Trajectory.”** [Inspected full primary preprint, arXiv:1806.05722v2](https://arxiv.org/pdf/1806.05722). The expanded journal article is **“Revisiting Ho–Kalman-Based System Identification: Robustness and Finite-Sample Analysis,” IEEE Transactions on Automatic Control 67(4), 1914–1928 (2022)**, [DOI](https://doi.org/10.1109/TAC.2021.3083651).

**Inspected result:** preprint §5, Theorem 5.3 and Corollary 5.4, with proofs in Appendix B. A small perturbation of finite Hankel data yields nearby balanced realization factors, after unitary alignment. The hypothesis and estimates depend on the least nonzero singular value of the relevant Hankel block. The bounds make explicit the instability of weakly observable directions.

**Comparison:** this is direct precedent for conditioning an observable coordinate construction and aligning realization factors. It does not assert a nonnegative Markov realization, detailed balance or recovery of positive features inside every larger competing realization. Its LTI input-output setting also differs from a finite set of switched-generator endpoint means. The inspected full text is the preprint; the journal download was unavailable, so theorem numbering here refers only to the preprint.

## 2. Controlled observable operators and the positivity distinction

**Byron Boots, Sajid M. Siddiqi and Geoffrey J. Gordon, “Closing the Learning-Planning Loop with Predictive State Representations,” Robotics: Science and Systems VI (2010).** [Conference record](https://www.roboticsproceedings.org/rss06/p36.html) · [inspected full author PDF](https://homes.cs.washington.edu/~bboots/files/RSSclosingtheloop.pdf). The journal version appeared in **The International Journal of Robotics Research 30(7), 954–966 (2011)**, [DOI](https://doi.org/10.1177/0278364911404092).

**Inspected result:** §II defines controlled tests through future action-observation sequences. Section III, Eq.(4a–c), constructs transformed predictive-state operators from test/history probability matrices and their rank subspace. The section establishes statistical consistency up to a linear change of coordinates. It also explicitly recognizes that finite-data estimates can produce negative probabilities.

**Comparison:** controlled finite-matrix realization is therefore an established ingredient, not a new interpretation of ordinary hidden-state reconstruction. The input is richer than the repository's stationary-preparation endpoint means. The inspected consistency statement is not a uniform finite-error theorem over arbitrary positive reversible rivals. A signed predictive-state representation is insufficient for the repository's positive Gram obstruction. The full conference paper was inspected; the journal full text was not.

The [fixed-clock audit](FIXED_CLOCK_PRIOR_ART.md) separately compares Hsu–Kakade–Zhang's spectral HMM realization and its rank/positivity hypotheses. That comparison remains applicable; it should not be replaced by an assertion that spectral realization was previously unavailable.

## 3. Divided differences already transfer approximate intertwiners

**A. B. Aleksandrov and V. V. Peller, “Operator and commutator moduli of continuity for normal operators,” Proceedings of the London Mathematical Society 105(4), 821–851 (2012).** [DOI](https://doi.org/10.1112/plms/pds012) · [inspected full primary preprint, arXiv:1108.4637v1](https://arxiv.org/pdf/1108.4637).

**Inspected result:** §2, Eq.(2.7), expresses $f(A)R-Rf(B)$ as the double operator integral of $AR-RB$ against the divided difference of $f$, for selfadjoint operators under the stated multiplier hypotheses. Section 3 develops operator/commutator Lipschitz estimates. The paper attributes the underlying integral identity to Birman–Solomyak; that older original was not inspected here.

The elementary finite-target specialization used locally is transparent. If $B=\sum_{r=1}^m\beta_rD_r$ is selfadjoint and $E=AV-VB$, then

$$
f(A)V-Vf(B)=\sum_{r=1}^m
\frac{f(A)-f(\beta_r)I}{A-\beta_r I}\,E D_r.
$$

For differentiable $f$, the quotient takes its continuous value at a coinciding eigenvalue. A scalar Lipschitz bound $L$ on the spectra gives

$$
\|f(A)V-Vf(B)\|\le \sqrt m\,L\,\|AV-VB\|,
$$

by Cauchy–Schwarz over the orthogonal $D_r$. This is a finite-spectrum consequence, not a claim that scalar Lipschitz continuity implies a dimension-free operator-Lipschitz bound. The local contribution must lie in obtaining the observable intertwiner and preserving the required positive features, not in the divided-difference identity itself.

## 4. Second-order response and coarse-grained protocols

**Urna Basu, Matthias Krüger, Alexandre Lazarescu and Christian Maes, “Frenetic aspects of second order response,” Physical Chemistry Chemical Physics 17, 6653–6666 (2015).** [DOI](https://doi.org/10.1039/C4CP04977B) · [inspected full primary preprint, arXiv:1410.7450](https://arxiv.org/pdf/1410.7450).

**Inspected result:** §III, Eq.(5), gives the second-order endpoint response around equilibrium in terms of the entropy-flux and time-symmetric dynamical-activity derivatives. Appendix A treats time-dependent perturbation protocols; Appendix B provides the generator perturbation formulation. Kinetic information beyond the equilibrium potential already enters the second-order coefficient.

**Comparison:** expansions and symmetry cancellation of response orders are established tools. The cited result is not the repository's explicit finite-amplitude comparison between an actual generator and its symmetry average, with a common reset providing an error bound independent of the protocol horizon. It does not construct the particular smaller reversible quotient.

**Fenna Müller, Urna Basu, Peter Sollich and Matthias Krüger, “Coarse-grained second-order response theory,” Physical Review Research 2, 043123 (2020).** [DOI](https://doi.org/10.1103/PhysRevResearch.2.043123) · [inspected full primary preprint, arXiv:2005.05169v2](https://arxiv.org/pdf/2005.05169).

**Inspected result:** §II B, Eq.(10), gives coarse-grained second-order response without requiring the coarse process to be Markovian. The perturbation potential must be measurable at the coarse level. Section III C, Eq.(26), handles general time protocols through second-order susceptibility; the paper develops a procedure using step-perturbation probabilities.

**Comparison:** neither coarse observables nor arbitrary time-dependent forcing distinguishes the local work from this source. The relevant distinction is a finite-amplitude, all-horizon error certificate for a specified autonomous Markov quotient. A second derivative or an $O(\varepsilon^3)$ expansion remainder alone supplies no uniform bound as the horizon grows. Conversely, the local result does not replace this more general nonlinear-response framework.

## 5. Uniform perturbation bounds from contraction

**A. Yu. Mitrophanov, “Ergodicity coefficient and perturbation bounds for continuous-time Markov chains,” Mathematical Inequalities & Applications 8(1), 159–168 (2005).** [Publisher record](https://mia.ele-math.com/08-15/Ergodicity-coefficient-and-perturbation-bounds-for-continuous-time-Markov-chains) · [inspected full primary PDF](https://files.ele-math.com/articles/mia-08-15.pdf).

**Inspected result:** §2, Theorem 2.1, Eqs.(2.2)–(2.4), and its variation-of-constants proof. For two finite homogeneous chains with generator difference $E$, law difference $z(t)$, and reference contraction coefficient $\beta_t$, Eq.(2.6) gives

$$
\|z(t)\|_1\le\beta_t\|z(0)\|_1+
\|E\|_{\infty}\int_0^t\beta_u\,du.
$$

Here the matrix norm is the maximum absolute row sum. The theorem derives explicit uniform-time estimates from this integral; the paper attributes Eq.(2.6) itself to its reference [9]. Thus Duhamel propagation of a perturbation, followed by integrable contraction, is a direct prior ingredient.

**Comparison:** this is a finite-amplitude bound, not only a response derivative. Its inspected setting is homogeneous and its generic dependence is first order in the generator perturbation. The local theorem adds a symmetry-even observable, exact odd/even coupling and a second contraction estimate for a specified switched family. Uniform saturation alone is not the distinguishing claim.

**A. Yu. Mitrophanov, “Stability Estimates for Finite Homogeneous Continuous-time Markov Chains,” Theory of Probability and its Applications 50(2), 319–326 (2006).** [English DOI](https://doi.org/10.1137/S0040585X97981718) · [primary record and Russian original](https://www.mathnet.ru/eng/tvp114), **Teoriya Veroyatnostei i ee Primeneniya 50(2), 371–379 (2005)**, [Russian DOI](https://doi.org/10.4213/tvp114).

**Access:** the primary record and indexed passages of the publisher PDF were inspected, including §3, printed p.322. Download/open attempts for the complete PDF failed; the Russian full-text link redirected to the record. This is passage-level primary evidence, not a claim to have inspected the complete paper.

The inspected Theorem 3, Eq.(14), bounds the semigroup difference uniformly by $\delta^{-1}\|\widetilde Q-Q\|_{\infty}$, where $\delta=\sum_j\min_{i\ne j}q_{ij}>0$ when the reference chain has a strongly accessible state. It is a close predecessor of the common-return mechanism. It concerns homogeneous chains and does not state the symmetry-cancelled quadratic estimate used locally. No priority claim is based on the missing remainder of the paper.

## 6. What the local statements add, and what remains separate

The [rational observation certificate](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) uses ten target clock-word functions spanning an invariant observable space. An exact dyadic calculation encloses their Gram matrix: the rounded Gram minus $2^{-51}I$ has ten positive rational LDL pivots, while the operator-norm enclosure error is at most $1281/2^{180}<2^{-150}$. Thus the true weighted basis has smallest singular value greater than $2^{-26}$. The calculation is a certificate for this target, not a general realization theorem.

The analytic argument then has distinct obligations: reconstruct inner products from the permitted means; embed the target space approximately into each reversible rival; transfer clock operators and capped generators; apply bounded rational selectors; and retain nonnegative rival features so that the CP Gram obstruction applies. The literature above supplies close tools and comparisons but does not discharge this chain automatically. Rational selectors are useful here because their denominator remains bounded below on the entire admissible rival spectrum, rather than only at the target interpolation nodes.

The current lower statement uses at most **66 clock ticks** and a menu of **12,766 controlled endpoint means**, with tolerance **$2^{-220}$**, under the specified finite-field capped interface. It forces at least **12 total states for ordinary-reversible predictors**; the earlier exact stationary construction still supplies **11 total states without reversibility**. This improvement does **not** extend the previously proved unrestricted minimum of 11 to the whole enlarged tolerance interval. That separate lower bound remains on its earlier interval, as recorded in [predictor minimality](FINITE_PREDICTOR_MINIMALITY.md).

The [symmetry-compression note](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) instead gives a nine-state ordinary-reversible model with mean error at most **$1/2376$** for every horizon and every protocol over the two permitted fields. Its symmetry is a permutation of equivalent target sectors, not a reassignment of physical time-reversal parity. Averaging the relevant barriers cancels the first perturbative term exactly; contraction from the common reset controls the full remaining difference. The claim is the stated finite-amplitude bound and explicit quotient, not merely the formal absence of a linear Taylor coefficient. The small-error lower and this larger-error upper concern different accuracy regimes and leave an intervening gap.

Six primary full texts support the detailed comparisons above; a seventh close source is recorded with its passage-level access limit. This focused search does not exhaust robust positive realization, quasi-commutator estimates or symmetry-aware Markov perturbation theory. No absence-of-prior-art or journal-fit conclusion follows from it.
