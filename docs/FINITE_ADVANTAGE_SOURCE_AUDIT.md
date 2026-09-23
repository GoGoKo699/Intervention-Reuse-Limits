# Finite state advantage: CP-rank, positive realization and controlled observations

[Finite theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Earlier realization comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) · [Kinetic/parity scope](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [Physical source audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md)

**Focused primary-source audit, 23 September 2026.** The proposed small example uses established completely positive matrix theory inside a controlled Markov realization problem. Neither a gap between nonnegative rank and CP-rank nor the use of positive matrix factorizations for hidden Markov realization is new. The question requiring a separate theorem is whether one concrete ordinary-reversible target needs more states in every ordinary-reversible predictor of its controlled means than an explicit stationary nonreversible predictor needs, with the same kinetic interface.

The [internally reviewed finite theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) gives twelve total target states, an exact eleven-total-state nonreversible predictor, and an ordinary-reversible lower at error $2^{-3000}$ using two fields and words of at most 1200 clock steps. The [independent internal review record](FINITE_ADVANTAGE_INTERNAL_REVIEW.md) is separate from this source audit. The source comparison below certifies neither the proof nor external priority. Manuscript drafting remains deferred.

## 1. The algebraic gap and its limited implication

For a symmetric matrix $M$, define

$$
\operatorname{cpr}(M)=\min\{r:M=BB^\top,\ B\in\mathbb R_+^{d\times r}\}.
$$

This is entrywise nonnegative Gram factorization, not complete positivity of a quantum map. The candidate uses the unsigned incidence matrix $C$ of $K_{2,3}$, with one column $e_u+e_v$ for each of its six edges. Thus

$$
H=CC^\top=
\begin{pmatrix}3I_2&J_{2\times3}\\J_{3\times2}&2I_3\end{pmatrix}.
\tag{1}
$$

The elementary support argument is worth retaining with its classical attribution. In any nonnegative Gram factorization, every column's support is a clique of the nonzero off-diagonal graph. A triangle-free graph permits at most one edge per column, and all six positive edges must be covered. Therefore $\operatorname{cpr}(H)\ge6$; the incidence factor attains six. This is a special case of the prior graph theorem in source A. In contrast, $\operatorname{rank}_+(H)\le5$ by the trivial factorization $H=HI_5$. No new rank-gap theorem is claimed.

For $a>0$ and any positive diagonal $5\times5$ matrix $D$, disjoint supports give

$$
\operatorname{cpr}(aH\oplus D)=6+5=11.
\tag{2}
$$

Indeed, a Gram column cannot meet two blocks because their cross entries vanish. Ordinary rank gives only nine: $C$ has rank four, since $C^\top x=0$ forces a constant value on each bipartition class with opposite signs. The five singleton features add five. The proposed obstruction therefore uses positivity beyond a spectral or ordinary-rank count.

Equations (1)–(2) alone do **not** construct a Markov predictor. A low-rank factor must extend to nonnegative conservative dynamics, preserve stationary preparation and readout, and remain compatible with every allowed field. The explicit generator intertwining is needed for that upper. Similarly, a CP-rank obstruction applies to a rival only after the observable experiments force that rival to possess the relevant positive Gram representation.

## 2. Five primary comparisons

### A. Triangle-free graph CP-rank is established

**Naomi Shaked-Monderer, “Bounding the CP-rank by graph parameters,” Electronic Journal of Linear Algebra 28, 99–116 (2015).** [DOI](https://doi.org/10.13001/1081-3810.3009) · [publisher full text](https://journals.uwyo.edu/index.php/ela/article/download/1465/1465/1465).

**Inspected:** definition of graph CP-rank on p.100; Proposition 2.4 on p.103; Lemma 3.2 and its proof on p.105. Proposition 2.4(b) states that every CP matrix whose graph is connected, triangle-free and not a tree has CP-rank equal to the number of edges. It attributes this result to Drew–Johnson–Loewy. The direct-sum additivity of matrix CP-rank is also stated in the proof of Lemma 3.2.

**Comparison:** exactly covers the matrix ingredient for $K_{2,3}$. Distinguish the maximum $\operatorname{cpr}(G)$ over matrices with graph $G$ from the stronger matrix-specific statement in Proposition 2.4. No controlled dynamics or observation theorem is supplied.

**Original attribution:** John H. Drew, Charles R. Johnson and Raphael Loewy, “Completely positive matrices associated with $M$-matrices,” Linear and Multilinear Algebra 37, 303–310 (1994), [DOI](https://doi.org/10.1080/03081089408818334). Its full text was not obtained in this audit; the precise result is verified through the inspected 2015 primary research paper, not presented as an inspection of the original proof.

### B. Structured and symmetric factorizations already meet HMM realization

**Bart Vanluyten, Jan C. Willems and Bart De Moor, “Structured nonnegative matrix factorization with applications to hidden Markov realization and clustering,” Linear Algebra and its Applications 429(7), 1409–1424 (2008).** [DOI](https://doi.org/10.1016/j.laa.2008.03.010) · [author-hosted published PDF](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2008.1.pdf).

**Inspected:** §§3–5, especially pp.1416–1419 and Eq.(16). The paper distinguishes $VAV^\top$ with nonnegative $A,V$ from $VV^\top$, compares their minimum dimensions, and gives approximation algorithms. For symmetric data it permits symmetric $A$. Its HMM application factors the two-symbol probability matrix as $B^\top\operatorname{diag}(\pi)\Pi B$ and reconstructs a model matching or approximating these length-two statistics.

**Comparison:** a close precedent, so the broad claim that structured positivity creates realization costs would overstate the contribution. Symmetric stationary flux $A$ is not the same constraint as a nonnegative Gram factor $VV^\top$. The inspected result does not give the present all-protocol continuous-time state separation or recover its Gram from controlled endpoint means. Matching two-symbol statistics is a weaker requirement than matching the entire controlled behavior.

The publisher fetch was blocked; the actual sixteen-page published paper was read at the linked author archive. Vanluyten's [2008 primary thesis](https://www.bartdemoor.be/wp-content/uploads/2025/07/doc_080623_14.39.pdf), §§2.3–2.4 and §5.3.1, was also inspected as a cross-check.

### C. Static positive rank does not solve dynamic realization

**Lorenzo Finesso and Peter Spreij, “Approximate realization of hidden Markov chains,” Proceedings of the 2002 IEEE Information Theory Workshop, 90–93 (2002).** [DOI](https://doi.org/10.1109/ITW.2002.1115424) · [author-hosted full text](https://staff.fnwi.uva.nl/p.j.c.spreij/itw.2002.1115424.pdf).

**Inspected:** §III's unnumbered static-realization theorem and rank lemma, and §IV. Conditional independence of past and future through a finite latent variable is equivalent to a nonnegative factorization of their joint probability matrix. Minimum inner dimension governs this static problem. Compound sequence matrices factor through hidden states; the approximation objective uses informational divergence.

**Comparison:** supplies the correct positive-realization background and the reason ordinary rank alone is insufficient. A static nonnegative factorization need not extend to a common time-homogeneous generator and all fields. The current explicit intertwiner must establish that compatibility. The inspected paper does not impose ordinary detailed balance or derive finite-error bounds from the repository's binary controlled means.

### D. Stochastic intertwining and compatible initialization are classical

**Thomas G. Kurtz, “Martingale problems for conditional distributions of Markov processes,” Electronic Journal of Probability 3, paper 9, 1–29 (1998).** [DOI](https://doi.org/10.1214/EJP.v3-31) · [primary full text](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/31/31-61-1-PB.pdf).

**Inspected:** Corollary 3.5, Remark 3.6 and the proof, pp.14–15. A kernel supported on observation fibers, a compatible initial law and the generator/martingale conditions yield a Markov observation and its conditional hidden-state law. Remark 3.6 explicitly identifies the semigroup-intertwining predecessor: Rogers–Pitman, Theorem 2.

**Comparison:** the intertwining method and its preparation conditions are established. A rectangular stochastic link between two different controlled realizations need not be a deterministic projection satisfying the fiber hypothesis. For the finite construction, one should prove its matrix identities directly and not cite this theorem as automatically covering every such link. Reusing one link for every field then supplies the elementary product-of-semigroups argument for arbitrary switching.

**Earlier source:** L. C. G. Rogers and J. W. Pitman, “Markov Functions,” Annals of Probability 9(4), 573–582 (1981), [DOI](https://doi.org/10.1214/aop/1176994363). The original full text was not obtained; its role and theorem conditions above were checked through Kurtz's inspected extension.

### E. Response tests of detailed balance are a distinct nearby problem

**Eugenia Franco, Bernhard Kepka and Juan J. L. Velázquez, “Characterizing the Detailed Balance Property by Means of Measurements,” Archive for Rational Mechanics and Analysis 250, article 25 (2026).** [DOI and publisher full text](https://doi.org/10.1007/s00205-026-02183-7).

**Inspected:** Theorem 1.1, Proposition 3.8, Definition 4.1 and Theorems 4.8/5.5 with their arguments. Detailed balance implies reciprocal impulse responses proportional by a constant. If this relation survives all sufficiently small admissible rate perturbations of a network without cut vertices, detailed balance follows. The admissible perturbations preserve architecture and specified balanced edges. Cut vertices and fine tuning create exceptions.

**Comparison:** this is a response-based identification theorem for linear biochemical networks, with species injection and concentration measurements. Our candidate compares the smallest realizations of a single equilibrium target's controlled occupancy response. Its nonreversible predictor may produce the same data as that target; we are not diagnosing the target as nonequilibrium. Their perturbation stability is not a finite-measurement-error state-count bound, and their accessible perturbations are not the same fixed kinetic field rule. The published full HTML and theorem passages were inspected.

## 3. What the controlled positive Gram must add

The following elementary implications clarify the remaining proof obligation; they are not a new general realization theory.

If a reversible rival has $D$ hidden states with law $\mu$ and its positive features are $f_a(i)\ge0$, then

$$
G_{ab}=\langle f_a,f_b\rangle_\mu
=\sum_{i=1}^D\bigl(\sqrt{\mu_i}f_a(i)\bigr)
                 \bigl(\sqrt{\mu_i}f_b(i)\bigr)
\tag{3}
$$

is CP with CP-rank at most $D$. Reversibility is used before (3), when experimental words and their reversed adjoints are shown to recover these inner products on the rival's own state space. Merely observing a symmetric two-time matrix does not establish (3). For example, a reversible discrete-time transition matrix may have negative eigenvalues, so its symmetric flux matrix need not be positive semidefinite. Continuous-time semigroups and specifically constructed reflected word Grams provide additional structure that must be retained in the argument.

The set $\{BB^\top:B\ge0,\ B\in\mathbb R^{d\times r}\}$ is closed for each fixed $r$. To see this, if $B_nB_n^\top$ converges, then $\|B_n\|_F^2=\operatorname{tr}(B_nB_n^\top)$ is bounded. A subsequence converges to a nonnegative $B$, giving the limiting factorization. Thus a fixed Gram of CP-rank eleven has some positive distance from CP-rank-at-most-ten matrices. This compactness observation alone supplies neither a numerical distance nor a controlled-mean tolerance.

A reviewable finite certificate needs both a quantitative matrix obstruction and a uniform transfer from measured means to that matrix, valid for every rival in the stated comparison class. Positive soft selectors must be valid on arbitrary rival sensitivities; target-only projection identities are insufficient. Every use of a rival exit cap, field menu, switching resolution or preparation restriction should appear in that transfer. A finite example with these ingredients would establish a concrete state advantage; a numerical fit against selected rival topologies would not.

For the upper, a shared stochastic link $L$ with

$$
Q_{\rm target}(h)L=LQ_{\rm pred}(h),\qquad
\pi_{\rm target}L=\pi_{\rm pred},\qquad
b_{\rm target}=Lb_{\rm pred}
\tag{4}
$$

implies equality of all endpoint means under piecewise constant protocols: expand the exponential to obtain $e^{tQ_{\rm target}(h)}L=Le^{tQ_{\rm pred}(h)}$ and telescope along the protocol. The actual link may be written in the reverse orientation; the corresponding identities must be adjusted consistently. Conservativity, positivity, stationarity and common-field compatibility are separate checks, not consequences of $\operatorname{rank}_+(H)\le5$.

## 4. Bounded assessment

The matrix obstruction, positive realization framework and intertwining method have close primary precedents. The finite contribution to assess is their integration into a single fixed-rate-rule, physically interpretable controlled prediction example, with an explicit smaller stationary predictor and a quantitative lower against arbitrary ordinary-reversible competitors under the common hidden exit cap. This is narrower than claiming a new CP-rank gap or a general cost of thermodynamic reversibility.

The exact $K_{p,q}$ extension also inherits its edge-count obstruction from classical triangle-free support arguments. Its additional claim is an explicit common-interface dynamic realization with $pq+p+q+1$ ordinary-reversible states versus at most $2(p+q)+1$ unrestricted states. The growing actuator alphabet and exact-agreement restriction must accompany that comparison. It does not improve the practical tolerance of the twelve-versus-eleven example, whose $2^{-3000}$ budget is a mathematical separation rather than an experimentally accessible signal.

The exact target and exact upper must be distinguished from a finite-entropy regularization of one-way predictor transitions. An approximate regularization is a separate upper at a stated positive tolerance; it is not automatically another exact eleven-state realization. Physical reversal remains fixed by the chosen variables, as discussed in the [physical audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md).

All five main comparisons above use inspected primary full text, with the exact alternate access routes stated. The original 1994 graph proof and 1981 Markov-functions proof were not read directly. Searches for reversible hidden Markov realization did not identify an inspected theorem settling this complete controlled comparison; that limited search outcome is not a priority certificate. The mathematical theorem and its error budget require independent review regardless of the literature comparison.
