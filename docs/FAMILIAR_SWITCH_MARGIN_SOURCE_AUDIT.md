# Source audit for the seven-mean reversible state witness

[Finite-margin proof](FAMILIAR_SWITCH_FINITE_MARGIN.md) · [Physical switch model](FAMILIAR_SWITCH_STRUCTURE.md) · [Earlier switch-source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md)

**Focused primary-source check, 24 September 2026.** Three full-text papers were inspected for the algebraic and dimension-witness ingredients of the seven-mean result. Polynomial constraints on observable data, finite Hankel realizations, and robust dimension bounds from expectation values are established methods. The present candidate contribution is the particular ordinary-reversibility constraint under a shared Gibbs tilt, its conditional-variance interpretation, and its explicit finite-error application to the two-switch model. This bounded check is not a novelty certificate.

Page numbers below are one-based PDF pages of the specified versions.

## 1. Finite Hankel reconstruction and polynomial invariants

**Alexander Schönhuth, _Equations for hidden Markov models_, arXiv:0901.3749v2 (2009).** [Primary full text](https://arxiv.org/pdf/0901.3749v2).

Inspected: Theorem 2.5, p. 4; Algorithm 2.8, pp. 7–8, equations (22)–(25); Theorem 3.1, pp. 10–11, equations (35)–(37).

Theorem 2.5 relates finite Hankel dimension to a matrix-product realization of a string function. Algorithm 2.8 chooses a full-rank table and shifted tables, then reconstructs the letter matrices by multiplication with the table inverse. Theorem 3.1 gives determinantal and rank-consistency conditions for the finite-dimensional model under its stated length assumptions.

**Assessment.** The use of an observed table and shifted table to reconstruct a linear realization is prior art. The seven-mean proof's table manipulation should not be presented as a new realization algorithm. Its additional constraint comes from detailed balance, the prescribed equilibrium tilt, and a singleton binary-readout sector. The cited theorem concerns string-function/probability models; its statement is not the controlled two-field reversible-versus-stationary comparison used here.

## 2. Observable polynomial tests beyond bare Hankel rank

**Andrew J. Critch, _Binary Hidden Markov Models and Varieties_, arXiv:1206.0500v3 (2012).** [Primary full text](https://arxiv.org/pdf/1206.0500v3).

Inspected: Definition 2.1, pp. 3–4; Theorem 3.1, p. 7; Proposition 4.7, p. 13; Sections 6.1–6.2, pp. 21–22.

The model has two hidden states, fixed transition and emission matrices, and observed finite joint distributions. Theorem 3.1 supplies 21 quadratic and 29 cubic generators for the four-node model's homogeneous ideal. Proposition 4.7 gives observable-moment parameter formulas with denominators cleared. Sections 6.1–6.2 distinguish polynomial variety membership from stochastic model membership and give a semialgebraic test.

**Assessment.** Polynomial vanishing tests and clearing denominators in hidden-model identification are established. Our witness is a necessary constraint, not a complete membership characterization. Its inputs are seven endpoint means after controlled field words; its rival class imposes reversibility at two equilibria linked by a specified Gibbs tilt. Those restrictions and the two-switch conditional-variance formula are not part of Critch's stated model. The presence of low-degree polynomial equations alone therefore carries no novelty claim.

## 3. Finite noisy expectation values as dimension witnesses

**Michael M. Wolf and David Pérez-García, _Assessing Quantum Dimensionality from Observable Dynamics_, Physical Review Letters 102, 190504 (2009).** [Publisher record](https://doi.org/10.1103/PhysRevLett.102.190504) · [Primary arXiv full text, titled _Assessing dimensions from evolution_, arXiv:0901.2542v2](https://arxiv.org/pdf/0901.2542v2).

Inspected: Proposition 1 and equation (4), p. 2; the classical-evolution comparison, p. 3; “Finite and noisy data,” equations (12)–(13), p. 4. The arXiv version identifier is v2, 3 September 2009; its generated title-page date is not used as the publication date.

The paper bounds dynamical dimension from delayed expectation-value vectors. For finite noisy data, it forms a Hankel table and uses singular-value perturbation bounds to retain a dimension lower bound. It also explains additional restrictions on a classical stochastic realization from its spectrum.

**Assessment.** Inferring dimension from a single observable's evolution, including robustness to bounded measurement error, predates this project. Our seven-mean witness uses two controlled propagators and a reversibility constraint that distinguishes three stationary states from four ordinary reversible states at the same controlled linear-realization dimension. It is not a new general principle of robust dynamical dimension witnessing or a quantum-versus-classical separation.

## 4. Attribution and remaining novelty question

The adjugate identities used to remove divisions are elementary linear algebra. In particular, making an invariant valid at singular observed tables does not by itself constitute a new algebraic method. The inspected sources justify attributing the broader Hankel and observable-invariant framework to prior work; none is being cited as the source of this project's particular quartic formula.

The narrow claim requiring further comparison is the complete combination: a familiar two-switch reversible target; an exact three-state stationary predictor with the same equilibrium force coupling; a seven-endpoint-mean polynomial obstruction for every ordinary rival with at most three states, including singular cases and unbounded rates; and a rigorously quantified positive error margin. The source audit should track that complete task and comparison class, rather than infer originality from different notation or from not finding the same polynomial in these three papers.

This update does not settle the earlier unresolved Falk comparison. No new full text was obtained for that lead, and no nonoverlap conclusion is drawn from its inaccessibility. The scope of this note is limited to the three inspected primary sources above.
