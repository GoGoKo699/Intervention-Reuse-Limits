# Two preparations and four endpoints: focused source comparison

[Preparation witness](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) · [Measurement and preparation cost](FAMILIAR_SWITCH_PREPARATION_COST.md) · [Physical-model audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) · [Earlier dimension-witness audit](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) · [Calibration and sampling sources](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md)

**Primary-source audit, 24 September 2026.** The four-endpoint construction uses two equilibrium preparations, two shared field propagators and one binary readout. The second preparation is an additional experimental resource relative to the earlier seven-word task. Correlation reciprocity, conditional covariance and preparation-based dimension witnesses are established ingredients. This bounded comparison does not certify priority of their particular combination, and does not claim a new general fluctuation-response principle.

## 1. The repository calculation being compared

Write $u=\tanh H\in(0,1)$ and assume the baseline stationary law is balanced, with $\pi_H=\pi_0(1+uS)$. Let $E_0,E_H$ be ordinarily reversible for their respective stationary laws. The four measured binary means are

$$
 m=\pi_0E_HS,\qquad a=\pi_HE_0S,\qquad
 b=\pi_HE_0E_HS,\qquad \ell=\pi_0E_HE_0S.
$$

Here the initial equilibrium preparation is part of each experiment. With $F=E_HS$ and $G=E_0S$, direct detailed-balance algebra gives

$$
 b-m-a+\ell+\sigma(u\ell-am)
 =-\frac{\sigma u^2}{1-\sigma u}
   \operatorname{Cov}_{\pi_0}(F,G\mid S=\sigma),
 \qquad \sigma\in\{-1,1\}.
$$

This is an exact finite-field identity, valid for every ordinary model in the stated class. It is not itself a dimension bound. A model with at most three states and deterministic binary readout has a singleton sector, where that conditional covariance vanishes. The positively coupled physical pair has positive covariance in both sectors. The companion proof combines these facts with a stationary three-state realization that also matches both preparations. The issue under study is this controlled realization comparison, not whether covariance or reciprocity is a new mathematical operation.

## 2. Equilibrium reciprocity is a classical antecedent

**Lars Onsager**, “Reciprocal Relations in Irreversible Processes. I,” *Physical Review* **37**, 405–426 (1931), [DOI:10.1103/PhysRev.37.405](https://doi.org/10.1103/PhysRev.37.405). **Inspected:** [original-paper scan](https://users.jyu.fi/~veapaja/Statistical_Physics_B/onsager_reciprocal.relations.PhysRev.37.405.1931.pdf), Section 3, pp. 410–413; Section 4, especially Eq. (4.10), pp. 417–418; and Section 7, pp. 425–426.

The paper relates microscopic reversibility to reciprocal kinetics, and Eq. (4.10) explicitly equates equilibrium correlations with interchanged time order. Section 7 identifies limitations involving magnetic and Coriolis forces. Thus equilibrium time-order reciprocity and the need to specify physical reversal must be credited as established. Our conformational labels are time-even, and ordinary detailed balance is imposed separately at each field. The four-endpoint formula combines two different equilibrium preparations and a finite Gibbs tilt; it is not a claim that an arbitrarily driven two-field protocol is itself an equilibrium process.

## 3. Modern Markov response theory also uses adjoint/time reversal

**Marco Baiesi, Christian Maes and Bram Wynants**, “Fluctuations and Response of Nonequilibrium States,” *Physical Review Letters* **103**, 010602 (2009), [DOI:10.1103/PhysRevLett.103.010602](https://doi.org/10.1103/PhysRevLett.103.010602). **Inspected:** full [arXiv:0902.3955v3](https://arxiv.org/pdf/0902.3955v3), particularly Eqs. (1), (6)–(7) and the equilibrium reduction on pp. 1–2, and Eqs. (11)–(13) on pp. 3–4.

The paper expresses linear response through correlations, explicitly recovers the equilibrium relation using detailed balance and stationarity, and identifies the adjoint generator with time-reversed dynamics. These are relevant operator ingredients. Its response functions differentiate with respect to a perturbation; the present identity instead uses four finite-amplitude endpoint means and a prescribed relation between two stationary laws. The inspected formulas do not provide the singleton-sector state-count argument. Conversely, our identity does not replace the paper's general response theory or establish an entropy-production witness: the four-state target is reversible at both fixed fields.

## 4. Preparation-and-measurement dimension tests are established

**Rodrigo Gallego, Nicolas Brunner, Christopher Hadley and Antonio Acín**, “Device-Independent Tests of Classical and Quantum Dimensions,” *Physical Review Letters* **105**, 230501 (2010), [DOI:10.1103/PhysRevLett.105.230501](https://doi.org/10.1103/PhysRevLett.105.230501). **Inspected:** full [arXiv:1010.5064v1](https://arxiv.org/pdf/1010.5064v1), preparation/measurement definitions and Eqs. (1)–(5), pp. 1–2; the dimension bounds in Eqs. (7) and (10), pp. 3–4.

This source formulates classical dimension witnesses from probabilities indexed by preparation and measurement choices. It also states explicitly on p. 2 that classical dimension at least the number of preparations can reproduce every unconstrained table by encoding the preparation label. With only our two preparation labels, that observation rules out describing the present result as an unconstrained device-independent four-state witness. The shared dynamics, Gibbs-linked preparations and ordinary reversibility are essential additional restrictions. The source also distinguishes correlated mixtures from independent devices; run-to-run mixtures of different small dynamical models cannot silently be treated as one fixed small model here.

## 5. Remaining scope

The second equilibrium preparation must be available with its own preparation guarantee; its cost is not removed by shortening the subsequent protocols. The exact-tilt alternative reweights baseline trials by $1+uS_{\rm initial}$ and therefore needs a noninvasive initial observation; its weighted estimator has a different sampling cost. This elementary change-of-measure identity is not claimed as new. The binary observable alone does not certify either hidden equilibrium law. Fixed common propagators and exact preparation/tilt assumptions define the identity; approximate preparation, field-law error and correlated drift require their own bounds. The earlier physical-source audit, including its unresolved Falk full-text lead, remains applicable. No generic priority claim follows from this three-source comparison.
