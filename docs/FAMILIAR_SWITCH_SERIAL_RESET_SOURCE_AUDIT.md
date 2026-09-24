# Source audit for serial sampling and finite preparation

[Serial sampling](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) · [Finite reset](FAMILIAR_SWITCH_FINITE_RESET.md) · [Internal review](FAMILIAR_SWITCH_SERIAL_RESET_INTERNAL_REVIEW.md) · [Earlier kinetic audit](FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** This is a bounded primary-source comparison for the operational extension. It does not certify priority, device feasibility or journal readiness. Manuscript drafting remains deferred.

## Established concentration tools

David A. Freedman, *On Tail Probabilities for Martingales*, Annals of Probability **3** (1975), 100–118, [DOI](https://doi.org/10.1214/aop/1176996452), is the historical martingale concentration source. Joel A. Tropp, *Freedman's Inequality for Matrix Martingales*, Electronic Communications in Probability **16** (2011), 262–270, [author-hosted full text](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf), supplies an accessible precise statement. Its Theorem 3.1 and conditional moment-generating-function Lemma 3.2 give the scalar Bennett framework underlying this argument. The present proof directly derives a conditional Bernstein moment-generating-function bound and its explicit Chernoff radius; it does not obtain that radius by inverting the weaker quadratic-denominator tail bound.

Martingale concentration already permits dependence on past records. Our contribution at this stage is its careful application to this fixed score and physical error budget: a deterministic case split on one stationary reference pair, enlarged conditional variance boxes, and checked constants that retain the existing trial count. No new concentration inequality is claimed.

## Established mixing and comparison tools

David Aldous and James Allen Fill, *Reversible Markov Chains and Random Walks on Graphs*, unfinished monograph, [Chapter 3, Section 6](https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S6.html), states the continuous-time Dirichlet form, the variational characterization of relaxation time (Theorem 3.25), and the $L^2$ contraction bound (Lemma 3.26). Its direct-comparison argument, including Lemma 3.32, explains why multiplying every equilibrium edge conductance by at least $.99$ retains at least $.99$ of the reference spectral gap.

The new calculation applies these standard tools to the specified four-state kinetic family. Combining its gap and minimum stationary mass gives a uniform finite wait sufficient for the already stated preparation budget. It is a sufficient bound, not an optimal reset protocol or measured relaxation time.

## Physical and statistical boundaries

Jonathan Barrett, Daniel Collins, Lucien Hardy, Adrian Kent and Sandu Popescu, *Quantum nonlocality, Bell inequalities, and the memory loophole*, Physical Review A **66** (2002), 042111, [author preprint](https://arxiv.org/abs/quant-ph/0205016), provides a physics precedent for treating dependence across repetitions explicitly rather than silently assuming independent data. That work concerns Bell tests; it is not a state-count result for our classical controlled model, and no Bell or device-independent conclusion is transferred here.

The reset condition must hold after every possible past history. An unconditional histogram or small visible bias is insufficient. The target's four-state Markov model proves its own reset bound; it does not prove a common finite reset time for all unrestricted reversible rivals. The serial ordinary null therefore carries a separate conditional preparation promise. Arbitrarily slow rivals remain covered by the earlier population obstruction, while a serial finite-sample rejection has only its stated operational scope.

The conditional detector and joint-instrument conditions also remain explicit. A fixed stationary reference pair is essential: this continuation does not allow a new stationary model to be selected after each record. Approximation allowances for single-trial marginals alone do not imply the required conditional allowance. The elapsed-time accounting includes reset and active evolution in attempt units; electronics, switching, readout duration, calibration and the physical conversion from attempt units remain separate resources.
