# Internal review: calibration and measurement cost

[Calibration proof](FAMILIAR_SWITCH_CALIBRATION.md) · [Measurement-cost proof](FAMILIAR_SWITCH_MEASUREMENT_COST.md) · [Source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** This is an internal mathematical and implementation review. It does not constitute external peer review, a novelty certificate or a demonstration of experimental feasibility. Manuscript drafting remains deferred.

## 1. Universal calibrated obstruction

The root and a separate analytic reviewer independently checked the generalized stationary-bias and Gibbs-increment formulas, including normalization by $1+ub$. Scaling the candidate Gram matrix by $u(1+\sigma b)(1-\sigma u)$ clears denominators. Its adjugate-product skew entry is a polynomial in nine variables, still quartic in the seven response means. The reduction at $b=0$ equals $u$ times the frozen witness. The same identity includes singular tables and two-state padding; no inverse, minimum stationary mass or rate cap is introduced.

The approximate high-field law was reviewed separately from target execution error. If its stationary law is within TV $\theta$ of the prescribed tilt, stationarity bounds the mixed first moment by $4(1+ub)\theta/u$. The second-moment defect uses one TV unit for $F^2\in[0,1]$, two for $SE_H^2S\in[-1,1]$, and the stationarity defect. These give the explicit polynomial residual band. Low-field detailed balance and the exact baseline Gram matrix remain essential. This argument covers an entire rival class, not just fixtures in the verifier.

The exact certificate uses a box in seven response means, stationary baseline bias and relative Gibbs parameter. For occupation radius $1/2500$, bias/parameter radii $10^{-4}$ and stationary-law TV discrepancy $10^{-5}$, both polynomial magnitudes exceed their allowed residual bands. The verified residual gap is greater than $13/600000$. The numerical threshold is computer-assisted exact arithmetic; the universal transfer to arbitrary rivals is analytic.

## 2. Physical error budget and state counts

The proof's full simultaneous budget was independently checked. It charges target and rival nonequilibrium preparation separately, includes the shift of the target's actual low-field equilibrium, and uses actual plateau durations for the field-error integral. The low-field estimate is a finite rate difference; a derivative bound over the whole auxiliary interval would be false and is not claimed. The timing constants follow from the cooperative two-mean closure and bounded backward occupation observables.

At preparation, field and common-tick tolerances $10^{-5}$, the combined occupation displacement is exactly $400300697/4100000000000<10^{-4}$. Thus the actual ordinary-three-state error exceeds $3/10000$. The existing three-state generator remains strictly positive on the enlarged hyperbolic-tangent field interval $[-10^{-4},9/10]$, including slightly negative low fields. Starting it in its actual low-field stationary law matches the stationary target means; target preparation error then costs at most $10^{-5}$. Both minima therefore hold for $10^{-5}\le\delta_P\le3/10000$. No exact three-state upper is asserted for every perturbed nonequilibrium preparation.

The state-count statement uses one fixed preparation law per model across the words. Independent timing draws preserve averaged reversible kernels when their law is fixed per field and draws are independent of states and other ticks. Correlated timing drift, per-occurrence field changes and uncapped finite ramps are not silently included. The optional ramp estimate explicitly adds a rate cap and uses the actual plateau difference.

## 3. Preparation and statistical validity

The target's gap and stationary-mass bounds certify an actual preparation wait of at least 62 attempt-rate time units at the allowed low fields. The nominal zero-field eigenmode formula also certifies a 55-unit wait. Neither is a uniform equilibration guarantee for arbitrary rivals, whose rates may be arbitrarily slow. Full hidden-distribution TV cannot be inferred from initial visible balance.

The root reviewed the complete measurement-cost proof, and separate statistical/source reviewers checked its concentration and change-of-measure assumptions. The test fixes its reference and budgets before sampling. Type-I validity and target power require two concentration radii; systematic target calibration enters once, while an additional unknown readout bias enters twice. Existing preparation allowances are not charged again. The conditional-moment extension permits a uniform conditional error guarantee; waiting alone does not establish independence or that guarantee under every null model.

At 5% false-positive and false-negative probabilities, the sufficient endpoint totals are 315,548,219 for the nominal exact null, 876,522,829 for the calibrated exact null, and 1,972,176,367 for the calibrated null with occupation-error allowance $10^{-4}$. These are conservative designs, not universal necessary counts. The explicit close ordinary comparator gives an independent adaptive expected-count lower bound $270000\log19\approx794998.52$ in the ideal endpoint-only task. A deterministic budget must be at least 794,999; an expectation is not rounded to an integer. Richer observations and other protocol menus are outside that lower bound.

## 4. Code, provenance and scientific limits

The root and a separate reviewer read the complete new verifier and its imported arithmetic helpers; another reviewer checked the physical, logarithm and sampling sections. Independent pinned Python 3.13.5 runs reproduced the development report byte for byte. The new verifier validates the frozen helper, target report and earlier proof hashes before using inherited centers. Exact rational polynomial boxes, logarithm tails and exponential partial sums establish the numerical constants; no optimizer, floating exponential or large simulation is used. Final source/report/proof binding and full regression are recorded in [Verification](VERIFICATION.md).

The [source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md) attributes concentration, adaptive information inequalities and Markov perturbation/mixing methods to primary literature. No claim of novelty attaches to those general methods. The contribution assessed here is their explicit application to this calibrated reversible-realization comparison.

The main unresolved physical issue is now the small observable separation and the resulting endpoint sample burden, alongside support for the preparation and force-law promises. Better statistical tests may narrow the wide upper/lower sample interval; a larger gap or more informative short measurement could change the scientific significance. This checkpoint alone does not establish PRL readiness.
