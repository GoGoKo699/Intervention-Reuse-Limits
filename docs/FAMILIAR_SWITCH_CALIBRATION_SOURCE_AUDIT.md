# Calibration and sampling: focused source audit

[Calibration theorem](FAMILIAR_SWITCH_CALIBRATION.md) · [Measurement cost](FAMILIAR_SWITCH_MEASUREMENT_COST.md) · [Seven-mean margin](FAMILIAR_SWITCH_FINITE_MARGIN.md) · [Polynomial-witness sources](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) · [Physical-model sources](FAMILIAR_SWITCH_SOURCE_AUDIT.md)

**Primary-source audit, 24 September 2026.** This note records established concentration, testing and Markov-perturbation ingredients used around the seven-mean certificate. It is not an exhaustive priority search or a novelty certificate. Generic concentration, exponential mixing, perturbation bounds and robust polynomial tests are not claimed as new. The model-specific calculation is the calibrated reversible-realization identity and its explicit error budget.

## 1. Independent endpoint sampling

**Wassily Hoeffding**, “Probability Inequalities for Sums of Bounded Random Variables,” *Journal of the American Statistical Association* **58**(301), 13–30 (1963), [DOI:10.1080/01621459.1963.10500830](https://doi.org/10.1080/01621459.1963.10500830). **Inspected:** [original-paper scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf), Theorem 2, printed p. 16 (PDF page 4), independently checked in this project's source review.

The theorem bounds the upper tail of an average of independent bounded variables with exponent $-2n^2t^2/\sum_i(b_i-a_i)^2$. Applying both tails to $N$ freshly prepared Bernoulli occupation measurements per word, followed by a union bound over seven words, gives

$$
\Pr\!\left(\max_{1\le j\le7}|\widehat p_j-p_j|>r\right)
\le 14e^{-2Nr^2}.
$$

This is a sampling statement about occupation probabilities, not binary means, whose errors are twice as large. A deterministic calibration displacement must be budgeted separately. Independent resets with fixed per-word response laws justify this application. A conditional version with uniformly bounded preparation errors requires a conditional moment-generating-function argument; independent-sample Hoeffding alone does not certify arbitrary correlated laboratory drift.

## 2. Adaptive protocol selection and testing lower bounds

**Emilie Kaufmann, Olivier Cappé and Aurélien Garivier**, “On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models,” *Journal of Machine Learning Research* **17**(1), 1–42 (2016), [full published paper](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf). **Inspected:** Lemma 1, printed p. 7, and Appendix A.1, printed pp. 25–26, including Lemma 19 and the likelihood-ratio proof.

Lemma 1 bounds the binary relative entropy of any decision event by the sum of expected arm counts times the corresponding one-observation Kullback–Leibler divergences, for mutually absolutely continuous arm laws and an almost-surely finite stopping time. Thus each reset protocol can be regarded as an arm: adaptive choices and stopping are allowed when the conditional observation law remains the chosen fixed Bernoulli law. Applying the lemma to one target/rival pair supplies a necessary testing sample count; it does not by itself identify the hardest composite rival or an optimal seven-protocol allocation.

Neither a deterministic response gap nor this information inequality proves independent preparation, specifies instrument noise, or resolves persistent drift. Changing those assumptions changes the statistical experiment and its likelihood ratio.

## 3. Total variation, preparation and Markov perturbations

**A. Yu. Mitrophanov**, “Sensitivity and convergence of uniformly ergodic Markov chains,” *Journal of Applied Probability* **42**(4), 1003–1014 (2005), [DOI:10.1239/jap/1134587812](https://doi.org/10.1239/jap/1134587812), [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/26A9854BCB8D103B3A63A9B272616EC0/S0021900200001066a.pdf/sensitivity_and_convergence_of_uniformly_ergodic_markov_chains.pdf). **Inspected:** Section 2, pp. 1004–1005; Theorem 3.1 and Eqs. (3.2)–(3.8), pp. 1005–1006; Theorem 4.2 and Remark 4.1, p. 1010.

The source treats initial-distribution and transition-kernel perturbations separately, using a telescoping identity and Markov contraction. Its signed-measure norm is the full variation norm; for differences of probabilities this is twice our $\operatorname{TV}=\tfrac12\|\cdot\|_1$. Its uniform long-time bounds require quantitative convergence information. The spectral estimate also depends on the stationary distribution and a convergence parameter. These established results support the conventions and explain why target mixing constants cannot be transferred to unrestricted rivals. Our continuous-time finite-horizon estimates follow directly from the corresponding semigroup integral and are proved in the calibration note; they are not attributed as verbatim statements of this discrete-time paper.

## 4. Assumptions that calibration does not remove

The physical and algebraic audits linked above remain in force. Local control of one time-even conformation, the chosen heat-bath kinetics, deterministic binary readout and a shared Gibbs tilt define the comparison class; the receptor literature does not experimentally validate that full task. A small allowed discrepancy between stationary laws relaxes the tilt quantitatively, but measured equilibrium occupancy alone cannot bound hidden-state total variation. The unresolved Falk full-text lead in the original audit remains unresolved here.

In the calibrated polynomial, $b=\pi_0S$ denotes **stationary baseline bias**. It is not a substitute for a bound on nonequilibrium preparation. A full-law preparation error at most $\varepsilon$ changes any subsequent endpoint occupation probability by at most $\varepsilon$, regardless of dimension, rates or protocol duration. Equal initial visible occupancy alone gives no such guarantee. The target's explicit waiting-time bound validates its own reset; arbitrarily slow rivals still require their stipulated preparation bound.

Two fixed actual fields and one fixed propagator per field preserve the repeated-word algebra, including fixed unknown tick lengths. Independent timing draws with the same field-specific distribution on every occurrence also produce fixed averaged reversible propagators. Correlated run-wide timing variation, history-dependent preparation and per-occurrence field changes do not automatically preserve those identities. They require an additional uniform error bound or a different null class. These are mathematical scope conditions, not conclusions supplied by a concentration inequality.
