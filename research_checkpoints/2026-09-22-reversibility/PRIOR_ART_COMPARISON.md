# Primary-source comparison for the recovered checkpoint

[Checkpoint](README.md) · [Main theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md)

This is a bounded literature comparison. It does not certify originality. The source audit was performed before the workspace outage and the central references were opened again during recovery.

## Lamp growth and entropy are established ingredients

Erschler and Zheng, *Isoperimetric inequalities, shapes of Følner sets and groups with Shalom's property HFD*, Annales de l'Institut Fourier 70(4) (2020), 1363--1402: [primary PDF](https://aif.centre-mersenne.org/item/10.5802/aif.3360.pdf).

Theorem 1.1, with constants $1/24$ and $1/4$, turns a small generator-boundary ratio for a finite group subset into a subset with many neighbors under bounded-length words. Combining it with Lemma 2.3 yields exponential cardinality when many independent lamp flips are available. Corollary 1.2 treats direct-product coordinates. Page 1365 explicitly records the already-known exponential-in-base-volume Følner lower for finite-lamp wreath products.

The abstract growth mechanism is therefore not new. Its hypotheses concern subsets of a group carrying prescribed actions. An arbitrary newly constructed reversible predictor is not supplied with those actions or table coordinates. The proposed contribution is a quantitative route from physical mean accuracy to stationary positive couplings and a deterministic decoded law on that predictor's own states.

Verdú and Weissman, *The Information Lost in Erasures*, IEEE Transactions on Information Theory 54(11) (2008), 5030--5059: [author PDF](https://web.stanford.edu/~tsachy/pdf_files/The%20Information%20Lost%20in%20Erasures.pdf).

Theorem 1, Eq. (5), states the standard conditional-entropy sum inequality used here:

$$
\sum_iH(X_i\mid X_{-i})\le H(X).
$$

Together with the elementary binary bound $h_2(u)\ge1-|2u-1|$, it gives

$$
H_{\rm bits}(\rho)
\ge r-\sum_{i=1}^r
\operatorname{TV}(\rho,(\operatorname{flip}_i)_\#\rho).
$$

The main note reproves this special case directly. Neither the entropy inequality nor the elementary coupling estimate is claimed as an independent novelty.

## Single-transfer positive realization is a different guarantee

Grussler and Damm, *A symmetry approach for balanced truncation of positive linear systems*, IEEE CDC (2012): [primary proceedings manuscript](https://lup.lub.lu.se/search/files/3937565/3163112.pdf).

Their Theorem 4 provides a symmetric positive minimal realization for a quasi-symmetric scalar-input scalar-output system. This is an important positive result: symmetry need not enlarge the realization of the specified single scalar transfer function. The present theorem requires one model to realize a common collection of noncommuting actuator words approximately. A theorem matching one transfer function supplies no such simultaneous word-law guarantee. The kinetic field rule, fixed histogram, and ordinary stochastic detailed balance must also be checked separately.

Taghavian and Sjölund, *Minimal positive Markov realizations* (2025), [arXiv v3](https://arxiv.org/html/2502.21102v3), Section III, Eqs. (4)--(6), uses “Markov form” for a canonical companion realization organized by impulse-response parameters. That terminology does not impose stochastic normalization or ordinary detailed balance. It is not a reversible finite-error observation-process theorem.

The bounded search did not locate an established theorem yielding the same exponential-versus-polynomial state comparison with the original kinetic rule, exact nineteen-level histogram, and common internal exit budget. This absence is a search result, not proof of novelty.

## Soft aggregation is an established architecture

Amjad, Blöchl, and Geiger, *A Generalized Framework for Kullback--Leibler Markov Aggregation*, IEEE Transactions on Automatic Control 65(7) (2020), 3068--3075: [primary preprint](https://arxiv.org/pdf/1709.05907).

Section III, Corollary 1, Eq. (6), gives the Bayes-reversed stochastic-encoder architecture

$$
\widehat P=BPA,\qquad
B=D_{\widehat\mu}^{-1}A^TD_\mu,\qquad
\widehat\mu=\mu A.
$$

Its Markov approximation is selected under a relative-entropy-rate criterion for the encoded process. The architecture itself is prior art. The checkpoint's soft-aggregation note instead proves a worst-case state lower from uniform error in actual physical controlled means, under color preservation and the stated fixed update clock. Its claim is the quantitative accuracy-to-state obstruction within this architecture, compared with an existing polynomial fresh-state reversible construction.

## The exact prefix obstruction uses classical peripheral-spectrum theory

Johnson and Paparella, *A matricial view of the Karpelevič theorem*: [primary PDF](https://arxiv.org/pdf/1611.06970), Theorem 2.1, records the unit-circle eigenvalue restrictions for finite stochastic matrices.

Benvenuti and Farina, *A Tutorial on the Positive Realization Problem*: [author PDF](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf), Theorems 4--5 and Example 4, develops the peripheral-spectrum obstruction in positive realization. Full impulse responses can have low real rank while requiring large or no finite positive realization.

The exact-prefix note reproves the elementary root-order bound. Its particular construction forces a stochastic cycle and primitive root from only fifteen observed symbols in an ordinarily reversible, five-color chain. Exact zero-error prefix realization must be distinguished from the main positive-error physical-mean theorem.

Fixed finite data forcing large dimension also have precedents in quantum and tracial moment settings. Musat and Rørdam, [arXiv:1806.10242](https://arxiv.org/pdf/1806.10242), Propositions 2.3--2.4, and Volčič, [arXiv:2306.13498](https://arxiv.org/pdf/2306.13498), Proposition 3.1 and Theorem 5.2, are relevant comparisons. Their noncommuting projections and tracial or quantum realization conditions differ from deterministic color projections and a stationary classical Markov state. The broad idea that finitely many observations can force high dimension is not claimed as new.

## Current assessment

The strongest candidate statement is now the same-family growth-class separation

$$
D_{\rm all}^{(3)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{(3)}(\delta)=\exp(\delta^{-\Theta(1)}),
$$

where the notation records positive upper and lower exponents, not matching exponents. The logarithmic factor in the explicit reversible upper is absorbable into a slightly larger positive power.

Its essential bridge is:

1. Actual controlled means determine the needed generator-word scalars quantitatively at each fixed clock.
2. Detailed balance and positivity turn those scalars into nearly stochastic, adjoint transports.
3. Balanced repair yields exact stationary couplings on the rival's existing states.
4. One deterministic joint lamp decoding has small defect under every bit flip.
5. Established entropy bounds force exponentially many rival states.

Both predictor classes retain the original rule, exact histogram, preparation, readout and exit budget. Binary actuators, unbounded-rate reversible rivals, arbitrary reversible field rules, and optimal exponents remain open. Manuscript drafting and journal choice remain separate from this research checkpoint.
