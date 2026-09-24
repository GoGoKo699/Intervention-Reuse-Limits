# Internal review of percent-scale kinetic robustness

[Kinetic theorem](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md) · [Three-state realization](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md) · [Score proof](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md) · [Verifier](../scripts/verify_switch_percent_kinetics.py) · [Report](../reports/switch_percent_kinetics.json) · [Source audit](FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** Separate proof authors, an adversarial reviewer and the coordinator inspected the three analytic notes and the complete verifier. These are internal checks within this investigation, not external peer review or novelty certification.

## Direct kinetic certificate

The family has eight independent edge factors, four for each fixed plateau generator, in $[.99,1.01]$. A factor multiplies both directions of its edge, preserving detailed balance and the designated Gibbs law. The same two generators serve both word orders. This permits failure of the original affine mean closure; no correlation or compensating adjustment between the eight factors is imposed.

Review checked that the coefficient norm takes the maximum row after summing over columns and all monomials. Its submultiplicativity bounds the degree-96 exponential-series tail. Truncation in perturbation degree is charged separately by the ordered Dyson series and contraction of the reference Markov propagators. These are uniform bounds on the full parameter box, not an inference from sampled rate tuples.

The witness is formed from the moment polynomials before absolute coefficient bounds are taken. The correlation difference is likewise bounded as one polynomial. Independent detector contrasts are minimized at their common lower endpoint by positive partial derivatives on a certified containing box. The resulting strict floors are $R>.00389$ and $T>.00367$. The gradient bound $1.9$, the quadratic remainder and containment of every joint-TV $.001$ neighborhood in the inherited singleton box give the stationary ordinary-three-state gap $>.001$.

## Constructive three-state upper

The fixed three-state basis and stationary laws leave four parameters to fit four moments. The fit reproduces both complete balanced initial/final joint tables, using one shared pair of generators for each physical target. It is not a claim that the entire kinetic family has one universal predictor, nor that this predictor reproduces arbitrary words, times or path laws.

The verifier derives the four moment identities symbolically. Correlated numerator bounds and single-plateau reductions enclose the fitted parameters. Review raised a small exactness issue about comparing a truncated constant coefficient with the exact nominal coefficient; the final proof and implementation include both errors through interval comparison with an independently enclosed nominal kernel.

Kernel positivity alone does not prove continuous-time realizability. Review independently reproduced the affine-corner entry ratios and characteristic-polynomial signs, and checked the monotonic scalar logarithm bound. They establish strictly positive off-diagonal entries of the real matrix logarithm throughout each containing box. Thus the fitted kernels have valid three-state continuous-time generators with the required stationary laws.

## Execution errors and scope

Each of the six inherited preparation, field, timing and initial-disturbance allowances is $10^{-5}$. The target external joint-TV budget is $.000078025101$ and the rival budget $.00002$. They give actual ordinary-three error $>.000901974899$ and a general-three upper below $.00008$, hence the state minima three and four on $[.00008,.0009]$ under the inherited stationary promises.

The predictor is constructed at nominal fields and clocks. Actual field and timing errors are charged in the external joint-TV comparison. It is not claimed to have the exact actual-field Gibbs law: if indexed by the actual relative tilt, its stationary-tilt defect is at most $10^{-5}$, within the inherited uncertainty class. In the field comparison, the actual edge-factor values are held fixed; no continuity of an edge factor as a function of field is assumed.

## Five-million-trial test

The test retains the integer score coefficients and a $.0002$ enlargement of the ordinary null, but uses newly certified rational gates and threshold $.0021$. Review checked complete-score TV transfer, including the initial-bit corrections for displaced laws, the enlarged stationary reference box, variance monotonicity and corner values, every gate distance, and rational Bernstein and Hoeffding bounds.

The null concentration boundary is below $.002078$ and the target boundary above $.002154$. Target gate failure is below $.004$. With 2.5 million fresh independent trials per arm, false rejection is below 5% and target power exceeds 95%. The null inside/outside population-gate cases are alternatives; target gate and score failures are union-bounded. No within-pair independence or Gaussian approximation is used.

This preserves the earlier five-million sufficient count while expanding the certified edge tolerance from 20 ppm to one percent, a factor of 500. It neither lowers the earlier ideal-family trial count nor establishes an optimal kinetic tolerance or sampling cost. Finite waiting alone does not prove independent repetitions or uniform preparation of arbitrarily slow rivals.

## Evidence and next question

The new verifier uses exact rational arithmetic, matrices of dimension at most four, three unconditionally pinned new proof snapshots, two frozen input reports and the inherited rational helper. Its 170 checks establish finite premises of the analytic proofs; they do not enumerate the universal rival class. Independent replay, hashes and the complete regression gate are recorded in [Verification](VERIFICATION.md).

The next operational task is to derive a conditional finite-reset sampling guarantee and price preparation under explicit mixing assumptions. The source audit does not certify a device meeting the complete preparation, measurement and detector promises. Manuscript drafting remains deferred.
