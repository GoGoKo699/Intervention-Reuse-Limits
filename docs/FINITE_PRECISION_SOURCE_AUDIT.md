# Direct matrix precedents and quantitative positive-rank comparisons

[Earlier finite source audit](FINITE_ADVANTAGE_SOURCE_AUDIT.md) · [Finite controlled theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Predictor minimality](FINITE_PREDICTOR_MINIMALITY.md) · [Sharper Gram obstruction](FINITE_GRAM_ROBUSTNESS.md) · [Observation bottleneck](FINITE_OBSERVATION_BOTTLENECK.md)

**Supplemental primary-source audit, 23 September 2026.** This note adds a closer precedent to the earlier, frozen audit: the particular five-by-five matrix used in the finite construction already occurs explicitly in the positive-rank literature. The comparison must credit that matrix, its CP-rank and the established lower-bound methods. The repository's controlled realization, observable reconstruction and numerical perturbation certificate are separate mathematical obligations. This source audit does not certify their external priority. Manuscript drafting remains deferred.

## 1. Three inspected primary sources

### A. The same matrix and a semidefinite CP-rank certificate

**Hamza Fawzi and Pablo A. Parrilo, “Self-scaled bounds for atomic cone ranks: applications to nonnegative rank and cp-rank,” Mathematical Programming 158(1–2), 417–465 (2016).** [DOI](https://doi.org/10.1007/s10107-015-0937-7) · [inspected primary preprint](https://arxiv.org/pdf/1404.3240) · [MIT manuscript record](https://hdl.handle.net/1721.1/103632).

**Inspected:** arXiv:1404.3240v1, §§4.1–4.5, especially Eq.(55) and Figure 9, printed pp.30–31. The paper considers

$$
A(a,b)=\begin{pmatrix}(3+a)I_2&J_{2\times3}\\J_{3\times2}&(2+b)I_3\end{pmatrix},\qquad a,b\ge0.
$$

Its $A(0,0)$ is exactly $48H$ in the finite theorem. It establishes CP-rank six for this family; Figure 9 reports the self-scaled semidefinite lower bound attaining six at $(0,0)$. Sections 4.1–4.2 bound CP atoms both entrywise and in the positive-semidefinite order before forming a convex relaxation. Section 4.4 compares rank and fractional edge-clique bounds.

**Limit:** the diagonal-parameter computation is not an explicit max-norm neighborhood certificate allowing formerly zero entries to become positive. The matrix, its exact CP-rank and quantitative optimization approaches are prior ingredients.

**Access:** full preprint inspected. MIT identifies its separate file as the author's final manuscript, but that download failed; section/equation numbers here refer to the inspected preprint.

### B. An older attributed occurrence and exact support-based moment bounds

**Milan Korda, Monique Laurent, Victor Magron and Andries Steenkamp, “Exploiting ideal-sparsity in the generalized moment problem with application to matrix factorization ranks,” Mathematical Programming 205, 703–744 (2024), published online 8 July 2023.** [DOI and inspected publisher full text](https://doi.org/10.1007/s10107-023-01993-x).

**Inspected:** §4.2, Lemma 13 and Example 14; §4.3.2, Eq.(55), example `ex2`. The latter is exactly $48H$ after swapping the bipartition order. The paper obtains a first-level ideal-sparse bound equal to its CP-rank six. Lemma 13 compares that bound to fractional edge-clique covering; exact zero products permit the sparse decomposition.

**Limit:** a dense positive perturbation changes the support graph and removes these exact zero constraints. Applying this particular support argument unchanged therefore does not prove the repository's uniform perturbation estimate. This does not preclude a suitable dense moment or robust optimization certificate.

**Earlier attribution, not directly inspected:** the paper attributes `ex2` to Shuhuang Xiang and Shuwen Xiang, “Notes on completely positive matrices,” Linear Algebra and its Applications 271(1–3), 273–282 (1998), [DOI](https://doi.org/10.1016/S0024-3795(97)00278-4). The original publisher page and PDF were inaccessible in this audit. Its matrix attribution is checked through the inspected 2024 primary paper, not through the 1998 proof.

### C. Rectangle covering is an established nonnegative-rank lower bound

**Samuel Fiorini, Volker Kaibel, Kanstantsin Pashkovich and Dirk Oliver Theis, “Combinatorial bounds on nonnegative rank and extended formulations,” Discrete Mathematics 313(1), 67–83 (2013).** [DOI](https://doi.org/10.1016/j.disc.2012.09.015) · [inspected primary preprint](https://arxiv.org/pdf/1111.0444).

**Inspected:** arXiv:1111.0444v2, §2.4, Eq.(2), printed p.9; the following Boolean-factorization discussion and §5's rectangle-graph methods. For every nonnegative matrix, the minimum number of positive-entry rectangles covering its support is at most its nonnegative rank. Each nonnegative rank-one term has rectangular support. Rectangle covering is equivalently Boolean rank. The statement does not require the matrix to be a polytope slack matrix.

**Comparison:** a five-rectangle lower for the support of $H$, combined with the trivial five-column upper, proves $\operatorname{rank}_+(H)=5$ by this established method. This paper supplies the method; no inspected passage specifically calculates the repository's $H$. An exact support argument alone gives no numerical distance to lower nonnegative rank, because arbitrarily small positive entries can change the support.

## 2. What the new local calculations establish

Write

$$
G_* = H\oplus\operatorname{diag}(d_i/24),\qquad
H=\frac1{48}\begin{pmatrix}3I_2&J_{2\times3}\\J_{3\times2}&2I_3\end{pmatrix},\qquad
d=(3,3,2,2,2).
$$

The [Gram refinement](FINITE_GRAM_ROBUSTNESS.md) proves that every nonnegative Gram sum with at most ten atoms has max-norm distance strictly greater than $1/1500$ from $G_*$. Its six auxiliary edge vectors are $y_{uv}(s)=\sqrt{x_s(u)x_s(v)}$; five more vectors are the isolated-coordinate columns. Cauchy–Schwarz bounds their overlaps using small entries at target zeros. Diagonal dominance and a Schur-complement estimate then make the eleven-vector Gram positive definite, contradicting the assumed ten-dimensional atom space.

These auxiliary vectors are constructed inside a hypothetical factorization. They are not additional measured observables. The tolerance applies to the ten-feature Gram, not directly to controlled endpoint means. The [observation estimate](FINITE_OBSERVATION_BOTTLENECK.md) remains a separate task, and a better matrix radius alone does not remove its interpolation and generator-reconstruction costs. No optimal-distance or new-method claim follows from this audit.

The [minimality refinement](FINITE_PREDICTOR_MINIMALITY.md) concerns a different factorization constraint: $UV$ with independent nonnegative factors, rather than $BB^{\mathsf T}$. It calculates Boolean rank five for $H$, strengthening the static lower from ordinary rank four to nonnegative rank five. Adding five positive singleton blocks raises the nonnegative rank to ten: a positive rank-one term cannot meet two blocks without creating a forbidden cross entry. Its separate assignment-of-cells argument gives a $1/40000$ neighborhood exclusion for nine-factor nonnegative matrices. These are elementary applications of support and rank-one cross-product identities, without a claim of a new general nonnegative-rank method.

The minimality note turns that static count into an unrestricted hidden-state lower by recovering positive left/right words through each rival's own hidden states. The factors need not be adjoints; the clock-reconstruction estimate must therefore work without reversibility. Conversely, the exact eleven-total-state upper still requires the shared generator intertwiner, preparation and readout checks in the [finite theorem](FINITE_REVERSIBILITY_ADVANTAGE.md). A static factorization does not automatically supply compatible Markov dynamics for all fields. The source comparisons above neither prove nor independently validate this observation transfer.

## 3. Bounded assessment and useful next comparison

The closest matrix predecessor is explicit, not merely a graph theorem with similar keywords. The earlier source audit remains useful for positive realization and Markov intertwining, while this supplement sharpens its attribution of the finite matrix ingredient. Neither the CP-rank-six example nor the general rectangle-cover method should be presented as a discovery of this project.

The square-root witness argument supplies a transparent numerical neighborhood estimate for the particular block matrix. A useful further comparison would formulate the same neighborhood exclusion using a rationally certified self-scaled or moment-relaxation dual. It might improve the constant or reveal a simpler certificate; the inspected results do not establish either outcome. Such an optimization should be judged against the full observable error transfer, since improving an intermediate matrix tolerance can leave the dominant measurement cost intact.

This focused search inspected three primary full texts and recorded the older matrix attribution with its access limit. It did not exhaust the literature on robust CP-rank, approximate nonnegative rank or nonlinear witness constructions. Absence of a matching inspected theorem is not evidence of priority.
