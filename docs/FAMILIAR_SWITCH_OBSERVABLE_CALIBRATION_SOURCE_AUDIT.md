# Observable preparation and readout calibration: focused source comparison

[Preparation theorem](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) · [Sampling cost](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) · [Readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) · [Earlier preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)

**Bounded primary-source comparison, 24 September 2026.** The new result is a response-specific preparation inequality for a fixed model with at most three states and a deterministic binary observable. Its experimental use retains a specified measurement instrument and independent symmetric electronic errors. Neither inverse-probability weighting, martingale concentration, nor the distinction between marginal disturbance and conditional disturbance is claimed as new. This comparison does not establish priority of the preparation inequality or experimental feasibility.

## 1. Marginal invariance is an established incomplete disturbance test

Lucas Clemente and Johannes Kofler, “Necessary and sufficient conditions for macroscopic realism from quantum mechanics,” *Physical Review A* **91**, 062103 (2015), [arXiv:1501.07517v3](https://arxiv.org/pdf/1501.07517v3), [DOI](https://doi.org/10.1103/PhysRevA.91.062103). Inspected Sections II B–C, especially Eqs. (6)–(8), (17), and the paragraph following (17).

The paper distinguishes invariance of later marginals under an earlier measurement from invariance of joint distributions when an intermediate measurement is inserted. It explicitly explains why all pairwise no-signaling-in-time conditions need not suffice for its macrorealism criterion. Thus the general warning that endpoint invariance does not establish undisturbed temporal correlations is established. Our example is a classical three-state instrument, with a binary-error coin correlated with a hidden transition. Its exact repeat-readout statistics and original-word table displacement diagnose one assumption in this repository. It is not a new general no-signaling principle, a quantum witness, or a counterexample to the paper's sufficient collection of conditions.

## 2. Known assignment probabilities and sequential estimation

Vitor Hadad, David A. Hirshberg, Ruohan Zhan, Stefan Wager and Susan Athey, “Confidence Intervals for Policy Evaluation in Adaptive Experiments,” *Proceedings of the National Academy of Sciences* **118**, e2014602118 (2021), [arXiv:1911.02768v4](https://arxiv.org/pdf/1911.02768v4), [DOI](https://doi.org/10.1073/pnas.2014602118). Inspected the introduction's inverse-probability estimator, pp. 2–3, and Section 2's definitions of treatment assignment and unbiased scores.

The paper explains inverse-probability weighting, the hazards of small assignment probabilities, and the need for appropriate inference with sequential data. These are established statistical ideas. Here all five probabilities are fixed and positive. Randomization occurs after preparation, independently of the current hidden state, so weighted observations estimate responses of one pathwise averaged preparation even when preparations depend on previous trials. The finite concentration argument is given directly in the companion note; it does not borrow the paper's asymptotic normality theorem or its stationary potential-outcome assumptions. The averaged preparation may be random, and all eight signs must be covered simultaneously.

## 3. Concentration is a standard ingredient

Wassily Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,” *Journal of the American Statistical Association* **58**, 13–30 (1963), [DOI](https://doi.org/10.1080/01621459.1963.10500830). The publisher's abstract was inspected; full text was not retrieved in this continuation. Kazuoki Azuma, “Weighted sums of certain dependent random variables,” *Tohoku Mathematical Journal* **19**, 357–367 (1967), [publisher record](https://projecteuclid.org/journals/tohoku-mathematical-journal/volume-19/issue-3/Weighted-sums-of-certain-dependent-random-variables/10.2748/tmj/1178243286.full). The bibliographic record was retrieved; a full-text fetch failed.

The sampling note supplies its bounded-range conditional moment-generating-function argument, iteration and union bound explicitly. Its large sufficient scalar-resolution count is not a statistical lower bound, a complete rejection test, or a new concentration theorem. The [serial-reset source audit](FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) retains the independently inspected martingale references for the previous five-million-trial test.

## 4. A recent unresolved lead and the remaining comparison

A search also returned Minsu Kim, Jeongho Bang and Han Seb Moon, “Exact No Signaling in Time without Temporal Classicality,” [arXiv:2607.14583](https://arxiv.org/abs/2607.14583), July 2026. The retrieved abstract describes nonselective fixed points concealing outcome-conditioned disturbance. Both attempted full-text endpoints failed. Treat this as an unresolved close comparison, not inspected full-text evidence and not grounds for a priority claim. The older Clemente–Kofler discussion already prevents claiming the broad marginal-versus-joint distinction as new.

The preparation theorem's precise low-dimensional inequality still needs an independent complete-theorem comparison. The readout fixture's role is to delimit the operational claim. The added long-low observation has not been matched by the existing general three-state predictor, and the conservative calibration precision guarantee does not replace the established two-word statistical test. Manuscript drafting remains deferred.
