# Verification scope and provenance

[Repository overview](../README.md) · [Core theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

## Reproducing the checks

From the repository root, install [the pinned dependencies](../requirements.txt) and run `make check`. The target checks local Markdown links, display-math/code-fence balance, Python syntax, report provenance, and the original MIT license. It then runs all thirty-two mathematical verifiers. Fresh reports are written to `.check-output/`, not over the saved reports.

The workflow uses the same command. A saved local PASS does not establish that a GitHub Actions run completed; inspect the live workflow separately. Neither kind of test constitutes independent mathematical review or novelty certification.

## Original checkpoint

[verify_checkpoint.py](../scripts/verify_checkpoint.py) is byte-for-byte the verifier from the supplied analytical checkpoint; only its repository filename changed. Its SHA-256 is:

```text
ce7a2a981e6a09f7350ad42731afbcafd6c67f2de2bade8d2de16666227e2026
```

All six entries in the supplied checkpoint's checksum manifest were verified before import. The source archive SHA-256 is:

```text
7ee27fc1e6b1c6217c9649374ae01f05edbd1ba61e35e31749925b14b3e99abe
```

The active theory and audit documents reorganize that checkpoint and add the finite-accuracy extension; they are not claimed to be byte-identical originals. The source fiction and conversational material are not repository contents.

The locally rerun [checkpoint report](../reports/checkpoint.json) records exact symbolic checks of generator row sums, detailed balance, stationarity, passive lumpability, three rational-rate Laplace calculations, and the three-state kernel inverse. Independent computational formulations within the script compare a block master equation with spectral and memory formulas.

| Metric | Saved local result |
|---|---:|
| Matrix/spectral comparisons | 56 |
| Largest augmented matrix | 36 by 36 |
| Maximum matrix/spectral discrepancy | about 2.05e-15 |
| Maximum time-dependent protocol discrepancy | about 1.35e-14 |

The original finite-field check is consistent with a fourth-order truncation remainder; that computation alone is not a proof of a uniform remainder. The later finite-field checkpoint below adds the analytic proof and separate checks.

## Finite-accuracy extension

[verify_finite_accuracy.py](../scripts/verify_finite_accuracy.py) checks the bounded-sensitivity path construction against numerical eigendecomposition for 23 models, including both parity cases. It verifies the closed-form positive weights, mass lower bound, and nonvanishing step correction.

For deterministic spectra spanning rates from 0.005k to 40k, it then checks midpoint quantization at four grid sizes, the exact mass-preserving certificate, and the paired-state reversible realization. The complete Markov Taylor equation is compared with the reduced memory equation under a five-segment sign-changing/on-off protocol. Zero mass and invalid inputs are also tested.

The saved [extension report](../reports/finite_accuracy.json) records:

| Metric | Saved local result |
|---|---:|
| Normalized-family models | 23 |
| Maximum spectral-weight discrepancy | about 1.55e-15 |
| Proved cubic-correction lower bound at kt=1/4 | 0.0275894 |
| Smallest sampled correction | 0.0313331 |
| Compression/realization cases | 12 |
| Protocol sample comparisons | 240 |
| Maximum observed error / transport certificate | about 0.0726 |
| Maximum realized-kernel discrepancy | about 3.37e-15 |
| Maximum full-Markov / memory discrepancy | about 1.23e-15 |
| Largest matrix | 68 by 68 |

The protocol samples are consistency tests. The guarantee for every bounded protocol comes from the inequality in the proof, not from extrapolating these samples.

Both runs used Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and, for symbolic checks, SymPy 1.14.0. The extension report records SHA-256 hashes of both calculation scripts. `check_repository.py` detects a mismatch between those source files and the saved report.

## Takeover verification

The takeover started from clean `main` at `80dc6098613b6561428d017b4a41553607fde67b`. Its original `make check` passed again under Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, and SymPy 1.14.0 before the extensions were added. The existing saved baseline reports and both existing mathematical verifiers were retained unchanged.

### Positive-quadrature extension

[verify_quadrature.py](../scripts/verify_quadrature.py) implements tapered Gaussian quadrature in normalized dyadic bins, with a separate high-rate tail atom. It uses fully reorthogonalized discrete Lanczos calculations and positive Gaussian weights. The saved [quadrature report](../reports/quadrature.json) contains 24 bin checks, moments through degree $2d-1$, 192 sampled kernel-sign comparisons, and exact `Fraction` arithmetic checks of the reciprocal-rate integral identity at orders 1–3. The component integral errors are summed as a triangle certificate; they are not mislabeled as the exact absolute error of a mixture whose bin and tail errors can have opposite signs.

The response checks use 162 samples from constant, sign-changing, zero/restart, and larger bounded protocols, including three values of $k$. A selected compressed kernel is also passed through the original paired Markov realization and compared with the full master-equation coefficient hierarchy. Boundary cases cover repeated atoms, exact small support, dyadic endpoints, empty/zero mass, tail-only support, and invalid input.

### Minimal reversible realization

[verify_minimal_realization.py](../scripts/verify_minimal_realization.py) constructs the finite Jacobi matrix from the augmented spectral measure, then uses its positive null vector to form a reversible birth–death generator. The saved [realization report](../reports/minimal_realization.json) checks six spectra, including nonuniform weights, repeated rates, zero-weight atoms, and collisions at $\lambda=k$. It verifies the spectral measure, positive neighboring rates, row sums, detailed balance, endpoint mass $1/2$, and the pointwise sensitivity bound. Twenty-four full-Markov/memory protocol comparisons check the reconstructed response.

| New check | Saved local result |
|---|---:|
| Maximum normalized quadrature moment error | 3.00e-16 |
| Quadrature full-Markov/memory cubic discrepancy | 1.53e-16 |
| Minimal-realization kernel discrepancy | 3.43e-15 |
| Minimal-realization full-Markov/memory discrepancy | 4.02e-16 |
| Largest matrix across all four verifiers | 68 by 68 |

All new saved reports were generated in the same pinned Python 3.13.5 environment and contain calculation-source hashes. These are small floating-point consistency checks plus selected exact rational identities. They do not certify numerical conditioning for arbitrarily clustered spectra or arbitrarily small requested tolerances. The general approximation bounds and generic exact minimality come from the written proofs, not sample extrapolation. In particular, a collision test does not prove the minimal state count at a collision.

The complete extended `make check` passed locally in this environment. All four fresh reports matched their saved JSON reports exactly. The final repository checks also passed; this local record does not assert a GitHub Actions outcome.

## Response lower-bound checkpoint

This continuation starts from `78004603026a8058983e471f0bad73b2310abc12`. All four earlier mathematical verifiers and their saved reports remain unchanged. The new [response lower-bound verifier](../scripts/verify_response_lower_bounds.py) generates [response_lower_bounds.json](../reports/response_lower_bounds.json), using Python 3.13.5, SymPy 1.14.0, and explicitly pinned mpmath 1.3.0.

The two-state checks expand the general analytic rate factor symbolically and independently expand the exact finite-field step solution. Exact algebra verifies the two-sample dual statistic and the equal-and-opposite errors of its minimizer. It does not optimize the all-protocol norm.

For state budgets $D=2,3,4$, the verifier checks rational Vandermonde inverses, Lagrange coefficient identities, the filter-to-positive-moment identity, and the conservative lower bound. The smallest Hankel eigenvalues are computed at 100 and 150 decimal digits; agreement is a numerical consistency check, not interval certification. Those eigenvalues are not substitutes for the general analytic bound. Their small values also illustrate that these conservative witnesses do not make every hidden mode practically observable.

Three surrogate examples check the exact full-to-reduced coefficient-hierarchy intertwining and characteristic-polynomial divisibility. They include a nonreversible four-state model with a defective hidden generator and sensitivity coupled to its Jordan part. High-precision propagation tests the filtered recurrences without inferring rank from a floating-point threshold. A separate complex-contour calculation extracts the cubic coefficient from the exact analytic generator as a cross-check of the hierarchy.

The new verifier's largest matrix is $16\times16$; the largest across the complete suite remains $68\times68$. The theorem covers all allowed models through the proof, not enumeration. The rate-capped upper bound reuses the proved quadrature and realization results; no new approximation algorithm is asserted. Finite-field remainder control and noisy coefficient acquisition remain outside the verification scope.

The complete five-verifier `make check` passed locally in the pinned environment. All five fresh reports matched their saved JSON reports exactly. The original license, four earlier verifiers, and their reports were also checked against the starting commit and remain unchanged. This records the local result; GitHub Actions is checked separately after publication.

## Unrestricted-rate matching-order checkpoint

This continuation starts from `57c0e12bdde4d8a38dc355d6797126debd7a6e76`. All five earlier mathematical verifiers and their saved reports remain unchanged. The new [unrestricted-rate verifier](../scripts/verify_unrestricted_rate_lower_bound.py) generates [unrestricted_rate_lower_bound.json](../reports/unrestricted_rate_lower_bound.json) in the same pinned environment.

Exact rational calculations check four geometric Cauchy matrices, their inverse-diagonal product formulas, and positive principal minors. Symbolic algebra checks the general-rate cubic-step decomposition into three visible exponential-polynomial terms and a negative hidden exponential. It also checks the positive-series identity giving the integral of `log(coth(x/2))` as `pi^2/4`.

For $D=2,3,4$, the verifier constructs the theorem's $r=8,11,14$ mode witnesses at 100 and 150 decimal digits. It checks the inverse-trace estimate, weight floor, optimized bound, and finite-horizon truncation estimate against computed eigenvalues. Precision agreement is a consistency check, not interval certification; the conservative bound is proved analytically for all $D$. These calculations neither optimize the minimax problem nor discretize the operator to infer its rank.

As a separate check of the response-to-Hankel construction, a three-state analytic master equation supplies a $12\times12$ coefficient hierarchy. Thirty-six probability-weighted double-integral moments, evaluated through exact resolvents, agree with the explicit baseline-minus-positive-kernel formula. This connects the operator identities to the Markov response without estimating the continuous operator's spectrum numerically.

The new verifier's largest matrix is $14\times14$; the complete suite's largest matrix remains $68\times68$. The finite-horizon theorem concerns an entire coefficient curve, not a finite sampling protocol, temporal-resolution guarantee, or noisy measurement procedure. The earlier verifier retains the finite-sample and nonreversible Jordan-block checks.

The complete six-verifier `make check` passed locally in the pinned environment. All six fresh reports matched their saved JSON reports exactly. The original license, five earlier verifiers, and their reports were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Publication-scope and structure-cost checkpoint

This continuation starts from `9cf4e64ca27624ee66bb75d93ba7fd215135ac43`. It adds the [publication comparison](PUBLICATION_SCOPE.md) and [structure-cost corollary](STRUCTURE_COST.md). All six mathematical verifiers, their saved reports, and the MIT license remain unchanged.

The corollary uses the existing lower and upper proofs. The unrestricted lower proof already applies to stationary analytic Markov surrogates with a fixed arbitrary readout. In the capped case, filtering preserves the coefficient-lift rank even without passive matching; the mode count becomes $3D-1$, and the same Vandermonde and filter estimates apply. No new approximation algorithm or computed minimax optimum is introduced.

The switch-off formula follows exactly from the zero-field readout eigenrelation, and the two three-state field-on coefficients follow by substitution in the existing step formula. The public note includes their derivation and precise scope. These are analytic corollaries; no additional simulation or statistical test is used to support them. The source comparisons are literature assessments, not mathematical verification by the programs.

The complete six-verifier `make check` passed locally in the pinned environment. All six fresh reports matched their saved JSON reports exactly. The license, all verification scripts and reports, pinned dependencies, build target, and workflow were checked against the starting commit and remain unchanged. Final repository checks passed. GitHub Actions is checked separately after publication.

## Finite-field prediction and path-information checkpoint

This continuation starts from `ef1448235c1fcf70e2c5fdca7d544f87591e9052`. It retains the six earlier mathematical verifiers and saved reports unchanged. The build target and repository checker are extended to include two new verifiers; the MIT license and dependency versions remain unchanged.

[verify_finite_field.py](../scripts/verify_finite_field.py) produces [finite_field.json](../reports/finite_field.json). An exact rational recursion checks the coefficient bounds underlying the uniform fourth-order remainder. Thirty-three deterministic finite-field protocol comparisons, including fields of magnitude 1.2, compare full physical master equations with the independent scalar-kernel modal closure. A genuinely smaller quadrature model is compared with the original under a sign-changing protocol and its weighted-integral certificate. Small weak-field examples check the remainder bound without inferring uniformity from the samples.

Two geometric-spectrum witnesses compare the full symmetrized field generator with the diagonal-plus-rank-one formula, its positive spectral step curve, the secular eigenvalue enclosures, the visible-weight floor, and logarithmic Gram spacing. An exact symbolic four-state calculation holds the actuator and cubic kernel fixed while showing different higher response, checking the stated boundary of the finite-field subclass. The largest new matrix is $40\times40$; the suite maximum remains $68\times68$.

[verify_path_information.py](../scripts/verify_path_information.py) produces [path_information.json](../reports/path_information.json). Exact resolvents check active no-exit coefficients for three examples, including a two-mode hidden kernel. Telegraph pair intensities check normalization of the full quadratic path score. A separate full-generator calculation checks the two-snapshot identity and its signal coefficient. Exact algebra also checks complete and residual waiting densities, normalization and mean duration, the hyperbolic density formula, a censored-relative-entropy identity, and the integral $8/105$ giving the three-state relative-entropy rate coefficient $2/105$. Twelve high-precision deterministic density comparisons provide a further consistency check.

Neither verifier simulates statistical trials or certifies inference performance from sampled data. The testing rates, all-size/all-horizon error bounds, and fixed-field minimax lower bound follow from the written proofs. Spectral consistency tests do not infer rank from numerical thresholds. The calculations and proof audits belong to this investigation and are not independent external validation.

The complete eight-verifier `make check` passed locally in the pinned environment. All eight fresh reports matched their saved JSON reports exactly. The six earlier mathematical scripts and reports, original license, dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## General actuator information and compression checkpoint

This continuation starts from `1f7f747a64442e15eab929c08e19d3958c9f4828`. It retains all eight earlier mathematical verifiers and saved reports unchanged. Two new verifiers cover the broader actuator results; the build target and provenance checker include both.

[verify_actuator_hierarchy.py](../scripts/verify_actuator_hierarchy.py) produces [actuator_hierarchy.json](../reports/actuator_hierarchy.json). Exact rational constructions at $d=2,3,4$ share $G=1$, $W=1/2$ and the full actuator within each pair. It checks positive reversible generators, common stationary laws, orthogonal projectors, and the identical one-mode covariance. Graded reachable spaces closed under the zero-field generator check every response word through the specified orders, without choosing protocol or time samples. Adding the visible observation projector checks finite visible observation words as well. The resulting mean first differences occur at orders $5,7,9$; their leading $t^3$ coefficients are respectively $1/96$, $1/3456$, and $1/1382400$.

Independent full-generator powers verify the exact finite-field third-time-derivative identities for both the mean and no-exit survival. A separate binary-actuator example checks identical complete hidden spectra and two-time kernels, equality of the first four time derivatives of the mean, and the exact fifth derivative difference. Its largest full generator has six states; the largest comparison matrix has dimension twelve. These finite cases support the all-$d$ proof but do not replace it.

[verify_general_compression.py](../scripts/verify_general_compression.py) produces [general_compression.json](../reports/general_compression.json). A four-state product chain gives an exact rational transition matrix and a nine-state order-two symbol-word realization. Thirty-nine symbol blocks of lengths one through three match exactly; a length-four witness differs, so the example does not accidentally reduce to an exact symbol Markov chain. Exact algebra checks the conditional-mean quantization variance loss $1/32$, word stationarity, nonreversibility, the physical surrogate's full finite-field equilibrium, and its passive readout eigenrelation. The largest matrix has dimension ten.

Thirty scalar spectral samples, fifteen semigroup comparisons, and nine deterministic bounded-protocol comparisons check the internal-rate regularization estimates. These are consistency checks, not proofs of the all-rate or all-protocol inequalities. The explicit state-count bound is proved analytically; the script does not attempt to instantiate its potentially enormous worst-case word model. Across the complete suite the largest matrix remains $68\times68$.

The three new theorem documents received reciprocal internal proof audits. These audits, exact identities, and deterministic computations belong to this investigation; they are not external validation, a learning algorithm, or evidence of publication originality. Neither new verifier simulates trajectories or estimates statistical sample complexity. The exact path-equivalence proof uses short-pulse limits analytically and does not claim a numerically stable implementation of those limits.

The complete ten-verifier `make check` passed locally in the pinned environment. All ten fresh reports matched their saved JSON reports exactly. The eight preceding mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## General complexity separation and reversible compression checkpoint

This continuation starts from `1d5928589506cd54440896bb545863f78fa9dd6e`. All ten preceding mathematical verifiers and saved reports are preserved. Two new verifiers check the controlled lower construction and reversible compression; the build target and provenance checker include both.

[verify_general_controlled_lower_bound.py](../scripts/verify_general_controlled_lower_bound.py) generates [general_controlled_lower_bound.json](../reports/general_controlled_lower_bound.json). Exact calculations at tree depths $n=1,2,3$ check the physical Haar change of basis, positive reversible generators, binary sensitivity, fixed internal rate band, and the leaf identity that proves the ideal Gram lower bound. Exact radial invariant subspaces and spectral moments check the stated cubic kernel. Full physical-generator identities independently check the polynomial filters and both mean-response endpoints, including their normalization and formal reversed words.

For these targets, rational norm arithmetic certifies the perturbation after substituting fixed-duration propagator logarithm polynomials. The field is $h=\log(65/64)$, the minimum segment duration is $1/8$, and the polynomial degrees are $280,320,360$. The corresponding certified matrix errors are approximately $5.18\times10^{-69}$, $1.78\times10^{-73}$, and $4.58\times10^{-78}$, each below $1/32$. Separate calculations at 100 and 150 decimal digits evaluate the factorized mean statistics using actual propagators. These are consistency checks, not interval certification or numerical rank tests. The rival rank factorization and the all-$n$ state lower bound are analytic; no search over competitors or statistical trials is performed. The largest new physical generator is $17\times17$, and the largest controlled matrix is $8\times8$.

[verify_reversible_compression.py](../scripts/verify_reversible_compression.py) generates [reversible_compression.json](../reports/reversible_compression.json). An eight-hidden-state reversible product chain gives a nontrivial four-cell predictive partition, with exact projection defect $5/72$ and three-symbol total variation $7/1728$. Rational identities verify the profile error bounds, stationary-flux quotient, detailed balance, and at-most-two-point moment restoration. The resulting six-hidden-state chain preserves $W=15/32$ and $G=1$ exactly. Symbolic full-field checks verify stationarity, detailed balance, passive lumpability, and the exact lifting of the cell model before the restored sensitivities are applied.

Three deterministic protocols with seven checkpoints compare six intermediate and final models. The maximum original-to-final mean discrepancy is about $6.17\times10^{-5}$, and the maximum baseline lifting discrepancy is about $2.22\times10^{-16}$. These selected comparisons do not prove uniform protocol accuracy or instantiate the worst-case partition size. The improved double-exponential upper count follows from the written controlled-expansion argument. The largest matrix across the complete suite remains $68\times68$.

The new proofs received reciprocal internal audits covering physical positivity, error norms, state counts, competitor scope, and the fixed-dwell conversion. Such audits and calculations belong to the same investigation and are not independent external validation or publication novelty certification. The signed statistics in the lower proof may be poorly conditioned for data acquisition, and neither new theorem provides an efficient learning algorithm.

The complete twelve-verifier `make check` passed locally in the pinned environment. All twelve fresh reports matched their saved JSON reports exactly. The ten earlier mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Bounded-rate polynomial upper and shift-register lower checkpoint

This continuation starts from `04666225de07d520555144d26dee342097afb6bd`. All twelve preceding mathematical scripts and saved reports remain regression baselines. Two new verifiers are added to the build and provenance checks.

[verify_bounded_rate_prediction.py](../scripts/verify_bounded_rate_prediction.py) produces [bounded_rate_prediction.json](../reports/bounded_rate_prediction.json). Exact rational examples check a nonlumpable eight-state binary target and a sparse three-state ternary target. They verify the spectral-cap uniformization bound, allowed-word irreducibility and stationarity, exact actuator histograms, and 89 prefix probabilities with their field-entry tilts. A longer-prefix discrepancy confirms that the word approximation is not accidentally exact. Full-field symbolic identities check equilibrium, passive lumpability and the stated reversibility status.

A nontrivial eight-to-four-state predictive quotient checks exact stationary-flux aggregation, inherited lower and upper spectral bounds, and a nonzero three-symbol total-variation discrepancy of `7/1728`. Eight symbolic Poisson/Gamma clock calculations support the regenerative constants. Sixteen rational rounding cases include exact equality boundaries; a separate exact budget checks the reversible prefix approximation. The uniform coupling and all-size polynomial count are proved analytically, not inferred from these cases.

[verify_shift_register_lower_bound.py](../scripts/verify_shift_register_lower_bound.py) produces [shift_register_lower_bound.json](../reports/shift_register_lower_bound.json). Exact one-, two-, and three-bit physical generators check positive rates, Walsh translation and binary toggle actions, full-field equilibrium and detailed balance, and the filtered mean endpoints. For word depths `n=1,2,3`, sparse Walsh polynomials verify the unique maximal-index leaf and an exact sum-of-squares Gram remainder. The largest sparse union has 499 Walsh coordinates; the exponentially larger physical state spaces are not enumerated. The largest physical generator is nine-dimensional and the largest controlled Gram matrix is eight-dimensional.

Exact degree-one through degree-four interpolation formulas reproduce polynomial derivatives and check coefficient bounds for both endpoint and outside-interval stencils. Rational Taylor and filter-perturbation budgets verify that the substituted mean matrix retains at least half the exact Gram floor for the displayed finite choices in both timing regimes. Selected 100-digit calculations check higher-degree stencils against the analytic target remainder. These computations do not use numerical rank, search over competitors, or infer an all-depth exponent from a plot. The written proofs establish the unrestricted-timing and fixed-minimum-dwell lower bounds separately.

Both theorem documents received reciprocal internal mathematical audits, including normalization, physical positivity, competitor scope, regeneration, interpolation and asymptotic inversion. The older tree's all-protocol truncation estimate is an analytic obstruction showing why changing only its measurement filters cannot produce a depth-exponential error floor at the same state threshold. Neither this obstruction nor the new lower theorem claims sample-efficient acquisition of the signed mean statistics. Classical de Bruijn spectra and interpolation are attributed in the [prior-art comparison](PRIOR_ART.md); no external validation or novelty certification follows from these checks.

The complete fourteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All fourteen fresh JSON reports matched their saved reports exactly. The twelve earlier mathematical scripts and reports, original MIT license, pinned dependencies, and workflow were checked against the starting commit and remain unchanged. The suite's largest matrix remains $68\times68$. GitHub Actions is checked separately after publication.

## Polynomial necessity with a fixed switching clock

This continuation starts from `b143adad62c8ec0d8b51733760d5c1c82bcaa213`. The fourteen earlier mathematical verifiers and saved reports are preserved. The new proof reuses the positive shift-register target and exact leaf Gram bound, with total-degree logarithm truncation replacing the earlier per-generator interpolation step.

[verify_polynomial_controlled_lower_bound.py](../scripts/verify_polynomial_controlled_lower_bound.py) produces [polynomial_controlled_lower_bound.json](../reports/polynomial_controlled_lower_bound.json). Small exact noncommutative polynomials check ordering, truncated-series associativity, and the bound on propagator word length. A separate exact counterexample shows that directly cutting the combined matrix entries can increase a rank-one factorization to rank two; the theorem instead truncates its two factors separately.

An exact rational calibration at $s=1$, $e^{h_*}=65/64$ and fixed dwell $a=1/8$ gives a whole-side cutoff $M=200(n+1)$. A base-depth inequality and a decreasing rational ratio verify the matrix-error budget for every $n\ge1$, not just selected depths. The resulting conservative response floor is at least $2^{-871n-849}$, with every positive segment an integer multiple of $1/(8k)$ and maximum horizon $50(n+1)/k$. This explicit calibration is not an optimized polynomial exponent. The written proof covers arbitrary fixed positive dwell times.

The verifier imports the unchanged shift-register verifier for exact small physical-generator and sparse leaf checks, recording both source hashes. A five-state physical example evaluates actual propagator series and the complete left and right factors at cutoffs 12, 24 and 40. Its controlled-matrix discrepancy decreases from about 45.5 to $3.93\times10^{-5}$ and $9.74\times10^{-12}$. These are high-precision consistency checks, not interval certification, numerical rank inference, or the large register used in the lower theorem. No exponentially large protocol menu or physical state space is enumerated; the new verifier's largest physical generator has dimension five, and the suite maximum remains 68.

Internal proof audits checked the target-only logarithm identity, weighted-norm power bounds at any fixed dwell, both coefficient majorants, separate side truncation, competitor rank and strict tolerance inversion. The result establishes the polynomial growth class with unmatched exponents. It does not establish a polynomial reversible upper bound, a statistical sample bound, or publication originality.

The complete fifteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All fifteen fresh JSON reports matched their saved evidence exactly. The fourteen prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow were checked against the starting commit and remain unchanged. GitHub Actions is checked separately after publication.

## Constant-step comparison and bounded-density reversible sampling

This continuation starts from `c2740b58734deda54f30463395362ef7368cb034`. The fifteen earlier mathematical verifiers and saved reports are preserved. Two focused verifiers accompany the new analytic results. Malformed LaTeX commands in Section 7 of the existing finite-field note were also repaired without changing its mathematics.

[verify_constant_step_compression.py](../scripts/verify_constant_step_compression.py) produces [constant_step_compression.json](../reports/constant_step_compression.json). Exact six-state constructions check both field signs, a two-atom positive mixture and one-atom padding, the positive Jacobi generator, detailed balance, irreducibility and the shifted-reset spectral coefficients. Symbolic preparation calculations verify a common full-support sign-balanced law, its stationarity at zero field, and strong lumpability to the exact passive telegraph process. Positive Gaussian nodes and moments are checked algebraically; rational tolerance budgets combine the all-time quadrature bound with the preparation perturbation. These are exact small identities supporting the general written proof, not numerical rank tests or sampled-time inference.

[verify_bounded_density_sampling.py](../scripts/verify_bounded_density_sampling.py) produces [bounded_density_sampling.json](../reports/bounded_density_sampling.json). Exhaustive enumeration of sixteen nonuniform stratified samples checks forty-eight conditional row/function identities, including an actually nonzero self-row bias and its exact conditional variance. Two small sampled graphs, including repeated microscopic vertices, verify positive reversible realization, exact actuator histogram, and the full-field physical identities. Thirty word probabilities check the finite-prefix recursion and tilt estimates. Fifteen concentration and regenerative budgets use rational logarithm enclosures and exact integer ceilings. The new largest matrix is five; no random trajectories or large sampled graph are generated.

Independent internal audits checked the equilibrium-tilt identity, positive quadrature tail, common-state realization and stationary preparation, the shrinking-amplitude capped lower, sampled-row conditioning, union bound, and regenerative all-horizon conversion. The constant-step predictor does not impose the original field rule or field regularity. The reversible switching theorem requires bounded conductance density and does not preserve the original spectral band. These audits do not establish the cap-only reversible theorem or certify originality.

The complete seventeen-verifier `make check` passed locally in the pinned Python 3.13 environment. All seventeen fresh reports matched their saved JSON evidence exactly. The thirty prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow are byte-identical to the starting commit. The largest matrix across the entire suite remains $68\times68$. GitHub Actions is checked separately after publication.

## Analytic constant-step and density-moment checkpoint

This continuation starts from `3f2bb0924a269c9ff4ce7ccb582e334e59c48c58`. The seventeen preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers are included in the build and source-provenance checks.

[verify_analytic_constant_step.py](../scripts/verify_analytic_constant_step.py) produces [analytic_constant_step.json](../reports/analytic_constant_step.json). A symbolic four-state calculation checks the two active reversible blocks, their commuting reset interpolation, fixed stationary preparation and exact passive lumpability. It checks the coefficient equations giving the exact linear and zero quadratic mean responses for arbitrary weak protocols. Two exact six-state constructions cover both field signs and two positive spectral atoms. A spectral measure whose rank collapses at zero field checks the positive reference-measure repair, analytic Jacobi coefficients and Gaussian moments through degree three. Three rational tolerance budgets combine reference regularization, quadrature, preparation and interpolation errors. The new largest generator has dimension six.

[verify_moment_density_sampling.py](../scripts/verify_moment_density_sampling.py) produces [moment_density_sampling.json](../reports/moment_density_sampling.json). Exact matching-graph calculations check symmetric clipping, its spectral cap and the full physical signed-forcing identity. All 64 vertices of a density box check the sharp algebraic forcing constant; an attaining normalized probability law is not claimed reachable. Exhaustive enumeration of 81 stratified configurations checks 84 conditional row/exit identities, including the self-row bias and the variance bound linear in the clipping threshold. A sampled update with a genuinely negative diagonal checks the necessity and effectiveness of the common rate rescaling. The final reset restores strict irreducibility while preserving ordinary detailed balance and exact actuator masses. Thirty prefix probabilities and fourteen exact concentration/error budgets check the fixed-clock recursion, Bernstein bounds and moment-dependent clipping allocation. The new largest matrix has dimension seven. No random samples or trajectories are simulated.

Reciprocal internal proof audits checked analytic moment regularization, the common-state realization, arbitrary-protocol low-order calibration, occupation-density control, conditional concentration, fixed-clock rescaling, the all-horizon bound and the finite-field clipping obstruction. The step theorem permits tolerance-dependent field derivatives and does not impose the original actuator rule. The switching theorem requires uniform density-tail control and does not preserve the original spectral endpoints. These results do not settle the cap-only reversible problem or certify publication originality.

The complete nineteen-verifier `make check` passed locally in the pinned Python 3.13 environment. All nineteen fresh reports matched their saved JSON evidence exactly. The thirty-four prior mathematical scripts and reports, original MIT license, pinned dependencies and workflow are byte-identical to the starting commit. The largest matrix across the suite remains $68\times68$. GitHub Actions is checked separately after publication.

## Sparse reversible compression and local-walk checkpoint

This continuation starts from `2ede88ab4d5cc0be6075e7f881bc66ec07ebb12b`. The nineteen preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers cover the sparse upper construction and the local-walk lower witness; the build and provenance checker include both.

[verify_sparse_reversible_compression.py](../scripts/verify_sparse_reversible_compression.py) generates [sparse_reversible_compression.json](../reports/sparse_reversible_compression.json). Exact positive nullspace elimination reduces six two-state components to three, taking the full physical model from 13 states to 7. The selected component weights are $1/8,27/40,1/5$. All 14 binary words through length three, all 42 refresh-flag conditional laws, and 28 field-entry tilt checks agree. The length-four total-variation difference is exactly $1/2500$, so the smaller model is not accidentally an exact all-word realization. Full-field identities verify the original rate rule, stationary histogram, ordinary reversibility, and the retained internal band $[3/2,5/2]$.

The same verifier enumerates 18 weighted path/grid offsets and 128 vertices of the driven-density box. It checks the sharp signed-forcing constant, a gap-one partition obstruction, a cap-preserving irreducibility repair with no added states, and six exact rational error allocations. It uses integer ceilings and rational powers rather than rounded logarithmic cutoffs. Its largest matrix has dimension 13.

[verify_local_walk_lower_bound.py](../scripts/verify_local_walk_lower_bound.py) generates [local_walk_lower_bound.json](../reports/local_walk_lower_bound.json). Exact 9-state and 25-state physical targets check the binary histogram, finite-field detailed balance, path correlation trace and resolvent, seven correlation moments each, and four actual-mean Gram entries each. At word depths $n=1,2,3$, sparse position/Walsh coordinates check every binary control word, its unique maximal-distance leaf, and an exact sum-of-squares Gram remainder. The largest Gram matrix is eight-dimensional, with 10,298 active sparse coordinates across its columns; the corresponding 491,521-state physical dictionary is not enumerated.

A rational field and dwell calibration includes the path factor $4n+3$ in the whole-side logarithm transfer. A base case and contracting exact ratio certify every depth, with the conservative floor $2^{-874n-849}$ at cutoff $M=200(n+1)$ and dwell $1/8$. This is a state-count obstruction, not a claim of practical statistical resolution. Four small rational Cauchy examples check the generic inverse-diagonal and trace bounds used for the constant-step lower; the cosine spacing and general-rank argument remain analytic. Source hashes record the two unchanged imported verifiers. The arbitrary fixed-clock theorem follows from the proof, not extrapolation from this one calibration. The largest newly constructed physical generator is 25-dimensional; the suite maximum remains 68.

Reciprocal internal proof audits checked stationary-flux normalization, component reweighting, exact refresh-prefix factorization, spectral-band preservation, the cap-preserving repair without an initial refresh, lattice and cycle cuts, and the Poincaré obstruction to cheap fragmentation. The lower audits checked the unique origin of the endpoint Walsh bit, the full stationary norm factor, the positive equal-weight path spectrum, the interior-mode Cauchy bound for constant steps, and the total-degree logarithm transfer at every fixed positive clock. These audits belong to the same investigation; they are not external validation or novelty certification.

The new results classify polynomial growth for the stated local-plus-refresh class with unmatched exponents. They do not settle the general cap-only reversible problem. The constant-step upper retains its freedom to use a different analytic rate rule; the switching upper preserves the original rule. Neither scenery reconstruction nor statistically efficient acquisition of the signed mean statistics is proved.

The full twenty-one-verifier `make check` passed locally in the pinned environment, and all twenty-one fresh reports matched their saved JSON exactly. The nineteen earlier scripts and reports, MIT license, pinned dependencies and workflow were checked byte-for-byte against the starting commit: all 41 protected files are unchanged. Final repository checks passed for 391 local Markdown links and 22 Python files, together with source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Fixed-label connected-expander checkpoint

This continuation starts from `b9553f7fa3498dcc8dd7210de0b1aa0fc24a93e3`. The twenty-one preceding mathematical verifiers and saved reports remain regression baselines. Two new verifiers supplement the [typical-label reversible upper](EXPANDER_SCENERY_COMPRESSION.md) and [fixed-clock lower](EXPANDER_SCENERY_LOWER_BOUND.md). The proof audits checked the evolving sign layer, the all-length good event, the refresh comparison, global-centering leakage, the physical Gram normalization and the fixed-clock transfer. These are independent internal checks, not external mathematical review.

[verify_expander_scenery_compression.py](../scripts/verify_expander_scenery_compression.py) generates [expander_scenery_compression.json](../reports/expander_scenery_compression.json). Exact short paths compare degree-four graph prefixes and longer cycle prefixes, conditioning on holds, moves, sign flips and repeated visits. A low-girth counterexample has total-variation difference $1/64$. Positive elimination reduces eight complete sign-layer coloring components to two, with weights $1/4,3/4$: 48 counted target hidden states become a 13-state physical surrogate. Full-field identities and an exact internal spectrum in $[3/2,19/8]$ check the original field rule, histogram and reversibility.

The same verifier checks 672 single-label word changes, all 14 refresh-flag strings through three updates, the countable failure allocation and exact rational error thresholds. Two length-two runs have total variation $29/576$, exceeding the single-run value $1/24$, so the runwise error factor is substantive. Averaging frozen-label refreshed laws and refreshing the annealed local reference differ by $1/96$; the proof must not interchange those operations. Another 1,456 reduced integer-matrix words through length six check finite cases of the small high-girth graph certificate. The all-length group argument and all-accuracy theorem come from the written proof, not enumeration.

[verify_expander_scenery_lower_bound.py](../scripts/verify_expander_scenery_lower_bound.py) generates [expander_scenery_lower_bound.json](../reports/expander_scenery_lower_bound.json). Physical targets on $K_3,K_4,K_5$ check stationarity, detailed balance, balanced histograms, local spectra, filter identities and twelve actual-mean Gram entries. The largest constructed physical generator has 11 states. Sparse Walsh calculations on cycles with 13 and 21 vertices verify depths one and two, all-terminal maximal-distance leaves, exact sum-of-squares identities and nonzero global-centering leakage. Their largest sparse column has 7,413 coordinates. These cycle checks establish finite geodesic algebra, not a uniformly expanding family.

Exhausting the 16 labelings of $K_4$ checks physical Gram/Parseval identities and 64 label-flip pairs at each depth. Exact induction ratios at a rational field calibration and clock $a=1/8$ certify sufficient base order $N\ge2^{192(n+1)}$, total-degree cutoff $M=300(n+1)$ and response-error floor $2^{-1295n-1279}$, conditional on the graph hypotheses. No graph of that order is constructed. Morgenstern's established graph-existence theorem supplies the family; the verifier does not prove it. An independent audit reran the lower verifier and reproduced its saved JSON exactly.

Both verifiers use exact rational or symbolic calculations without large simulations or numerical rank inference. Their maximum constructed matrices are 13 and 11; the full suite maximum remains $68\times68$. Neither the finite evidence nor the proof claims arbitrary-label reversible compression, a cap-only theorem, a matched exponent, a statistical acquisition guarantee or publication novelty.

The full twenty-three-verifier `make check` passed locally in the pinned environment. All twenty-three fresh reports matched their saved JSON exactly. The twenty-one preceding scripts and reports, MIT license, dependencies and workflow remain byte-identical to the starting commit: all 45 protected files are unchanged. Final repository checks passed for 436 local Markdown links and 24 Python files, with source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Aggregation and register-scenery architecture checkpoint

This continuation starts from `cd8f21a8f8f9d25cd1645ee6a165d1061e0ff3e0`. The twenty-three preceding mathematical verifiers and saved reports remain regression baselines. The new [aggregation lower](AGGREGATION_STATE_LOWER_BOUND.md) and [register-scenery upper](REGISTER_SCENERY_COMPRESSION.md) compare actuator-respecting stationary-flux partition aggregation with newly constructed reversible models. Both use the same fixed six-level histogram, original field rule and advertised band. The new evidence is generated by [verify_aggregation_state_lower_bound.py](../scripts/verify_aggregation_state_lower_bound.py) and [verify_register_scenery_compression.py](../scripts/verify_register_scenery_compression.py), producing [the aggregation report](../reports/aggregation_state_lower_bound.json) and [the register report](../reports/register_scenery_compression.json).

Independent internal proof audits checked the compression-compatible partial isometries, the physical palindrome endpoints, exact projection-loss telescoping, root-cube entropy bound, all-clock actual-mean transfer, affine-dihedral collision probabilities, refresh accounting and uniform register-width replacement. The lower covers every partition in the stated architecture; the upper is uniform over all target widths and all accuracies. These internal audits are distinct from external mathematical review and publication novelty assessment.

The aggregation verifier constructs the full width-one dictionary, with 49 physical states. It checks the six-level histogram and variance, finite-field detailed balance, passive lumpability, and full-state removal of the refresh term. Nine extracted port operators satisfy exact partial-isometry identities. Two nontrivial partitions give eighteen exact agreements between physical gate polynomials and conditional-expectation compressions, including cells that mix root and nonroot addresses. The palindrome norm deficits and telescoping projection losses are checked directly; some tested aggregates lose an entire queried direction.

Width-one and width-two address truth tables verify pure XOR translations and the exact Gram matrices $I_2/6$ and $I_4/6$, without constructing the width-two 385-state physical generator. A $13\times13$ rational Vandermonde inverse checks field extraction exactly; its coefficients have up to 2,880-bit numerators or denominators, making the size of those constants explicit. Small cube partitions and the rational inequality $(16/15)^{15}<4$ check the entropy constant. The transfer checks use representative abstract side bounds $A=2,B=3,\varrho=3/2$ to verify error allocation; they do not calibrate the actual, much larger interpolation-dependent asymptotic constants.

The register-scenery verifier checks 121 formal address words against 15,246 literal actions, and exact binary linear equations for collision probabilities at register widths up to 257. Twenty-seven independently enumerated address-partition laws validate the prefix calculation. Small exact local and refreshed prefix laws test register replacement. Positive selection reduces the width-two dictionary from sixteen configurations to two, or from 385 counted physical states to 49 constructed states, while matching all two-symbol probabilities. A longer four-symbol prefix has nonzero total-variation error $1/3072$, confirming that the selection check distinguishes finite-prefix matching from exact process equivalence.

The selected physical models satisfy the exact histogram, stationary flux and finite-field detailed-balance identities. All thirty-six two-symbol probabilities of the physical uniformized generator agree with the local/refresh decomposition. Exact weighted Gram and Dirichlet identities certify the internal band $[3/2,17/8]$, inside the advertised $[3/2,5/2]$. Rational error budgets check four accuracies down to $1/4096$ and the uniform polynomial exponent; the enormous sufficient reference models are counted, never constructed. Both new verifiers use physical matrices of size at most 49; the preceding suite's maximum remains 68.

The full twenty-five-verifier `make check` passed locally in the pinned environment. All twenty-five fresh JSON reports matched their saved evidence exactly. All 49 protected files—the twenty-three preceding scripts and reports, MIT license, dependencies and workflow—remain byte-identical to the starting commit. Repository checks passed for 478 local Markdown links and 26 Python files, including saved-source provenance and whitespace checks. GitHub Actions is checked separately after publication; this local record does not assert its outcome.

## Intrinsic reversibility, soft aggregation, and exact-prefix checkpoint

This integration starts from the recovered research commit `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`, whose parent is the fully tested twenty-five-verifier main commit `80253e1462d618ccc435f2394aba240e858496b5`. The nine archived proof and recovery files remain unchanged. The disconnected workspace lost the uncommitted verifier sources; the three new programs below are fresh implementations with newly generated reports and their own source hashes. They are not represented as byte-for-byte recovery of the earlier sources.

The [main theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) compares ordinary reversible and stationary nonreversible prediction under a common internal exit budget, original field rule and exact nineteen-level histogram. Independent internal proof audits checked physical endpoint normalization, positive off-diagonal gate extraction, all-clock scalar transfer, balanced-flux repair, the deterministic decoded entropy bound, and the unrestricted whole-side rank lower. Separate audits checked the recovered soft-lift and Ritz arguments. These are internal checks, not external review or novelty certification.

[verify_dynamic_lamp_reversibility_lower_bound.py](../scripts/verify_dynamic_lamp_reversibility_lower_bound.py) produces [dynamic_lamp_reversibility_lower_bound.json](../reports/dynamic_lamp_reversibility_lower_bound.json). The width-one target is represented as 146 physical states and 672 directed sparse internal edges, with no dense 146-dimensional generator. Exact stationary flux checks cover the full nineteen-level histogram, variance, three rational exponential fields and passive telegraph lumpability. All 24 oriented port blocks, 48 first/second physical endpoint moments, and four gate cycles are checked. Width-one and width-two literal tables verify XOR query and lamp-flip relations and Gram matrices I_r/36. The width-two 1154-state physical model is counted but not constructed.

The same program checks all 741 factors of an exact 39-node Vandermonde determinant, factorized star and gate Dirichlet bounds, four rectangular transport repairs and their full path errors, and bit-law entropy inequalities using exact integer powers. An explicit stationary approximate-flip coupling acts on eight actual decoded states. Rational allocations exercise the scalar-transfer and entropy thresholds; they do not calibrate the much larger interpolation-dependent asymptotic constants. Its largest dense matrix is eight-dimensional.

[verify_soft_aggregation_lower_bound.py](../scripts/verify_soft_aggregation_lower_bound.py) produces [soft_aggregation_lower_bound.json](../reports/soft_aggregation_lower_bound.json). A genuinely overlapping four-state binary encoder has eight joint hidden states and nine physical states. Exact checks establish the Bayes reverse, BPA dynamics, full-field physical intertwining, stationary-flux compression, and the extra relaxation modes at 5/2. BKA has negative off-diagonal entries -15/64, so omitting the resampling term is observably a different construction. A two-generator physical feature has nonzero squared projection loss 27/32768. A 27-dimensional auxiliary path matrix verifies the positive Ritz energy identity with a nonzero discarded component. This clock is an algebraic device, not a free model coordinate. The finite binary fixture tests general identities; the asymptotic soft lower still concerns the six-level dictionary.

[verify_exact_reversible_prefix_obstruction.py](../scripts/verify_exact_reversible_prefix_obstruction.py) produces [exact_reversible_prefix_obstruction.json](../reports/exact_reversible_prefix_obstruction.json). Exact rational instances N=3,4,6 have at most twenty states. Detailed balance, five equal color masses, half-laziness and the star comparison certify the target spectral band. Forty-eight distinct prefix probabilities per instance recover the row moments, feature norm 1/10 and zero recurrence norm. The longest prefix has exactly fifteen symbols. The extracted eigenvalue has primitive order N. The all-N state bound follows from the analytic positivity argument, not extrapolation from these cases, and it is a zero-error theorem.

All three fresh verifier sources received independent static review and passed individual runs in Python 3.13.5 with the unchanged pinned dependencies. The full twenty-eight-verifier `make check` passes, and all twenty-eight fresh reports match their saved evidence. The repository checker passes 591 local Markdown links and 29 Python syntax checks, including report provenance. A byte comparison preserves all fifty-three protected files from `80253e1462d618ccc435f2394aba240e858496b5` (twenty-five verifiers, twenty-five reports, license, dependencies and workflow) and all nine recovery files from `ee4e5173ea6a9dd0a54e2d558e83a0ad3a1ad620`. The suite still has maximum dense dimension 68; the new dynamic-lamp check separately constructs 146 physical states as a sparse graph. GitHub Actions is recorded separately from these local checks.

## Binary reversibility checkpoint

This extension starts from local commit `da0073b`, which integrates the recovered nineteen-level theorem and its twenty-eight-verifier gate. The [binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) and [exact verifier](../scripts/verify_binary_reversibility_lower_bound.py) add the balanced two-level construction and the positive-normalization argument. Its [saved report](../reports/binary_reversibility_lower_bound.json) is generated in the unchanged pinned Python 3.13.5 environment using the standard library and records its own source hash.

The verifier constructs the complete width-one weighted hidden graph: 1,795 hidden vertices, plus the counted visible state. Sparse dynamic programming checks every possible marker starting vertex in both directions, leaving exactly the intended root-to-tip map and its reverse. Root-restricted words of lengths 5, 9, 13 and 17 implement the four logical gates; lengths 21 and 25 select the two complementary probes, including the inactive scrambled cycles. Their exact normalization gives root mass `1/18` and query Gram `I/18`.

Degree counts certify the balanced binary histogram and variance `1/100` for sensitivity `±1/10`. Explicit routes certify basin volume 235, maximum route length 28 and maximum load-to-conductance ratio 235, the finite instance of the analytic gap proof. Original-rule edge fluxes satisfy exact detailed balance at three rational exponential fields, and the zero-field rates give exact passive telegraph lumpability. The physical scalar endpoint normalization is checked on the root selector. The theorem's five-field interpolation and all-width inequalities remain analytic statements.

Two-, three- and five-state exact algebraic cases check the new mixed-norm transport repair and normalization identities. One has raw row sum 10 but an L2 operator cap below 2. Another has a positive nonprojector selector with a zero row and a small positive row sum. The five-state case uses `u=(1/1000,1,1,1,0)` and a nonselfadjoint transport: weighted adjoints, both clipping stages, positive deficit filling, bounded path errors and positive outer-selector probe clipping are all checked exactly. These examples do not add any state during normalization or repair, and do not simulate arbitrary physical rivals.

The new verifier's largest dense matrix has dimension five. The suite's earlier maximum dense dimension remains 68; the 1,795-vertex graph is stored sparsely. This is bounded exact verification, not a large simulation or an enumeration proof of the asymptotic lower bound. The complete binary proof and the verifier received separate internal reviews with no outstanding mathematical issue. Its scope is the common exit budget `6580k`, target/reversible-upper band `[k,13160k]`, exact binary histogram and original field rule. The earlier numerical binary band `[k,3k]`, uncapped reversible rivals and matched exponents remain open. Earlier saved reports retain their checkpoint-specific limitations, including statements of questions that this later theorem resolves.

The full twenty-nine-verifier `make check` passes in pinned Python 3.13.5. All twenty-nine fresh reports are byte-identical to their saved evidence. The final repository checker passes 630 local Markdown links, 30 Python syntax checks and saved-source provenance. All fifty-nine protected files from `da0073b` (twenty-eight verifiers, twenty-eight reports, license, dependencies and workflow) and all nine recovery files are byte-identical to their preceding checkpoints. After explicit user authorization, the nineteen-level and binary checkpoints were published on `main` as `9f4a815808e55e4e699a7fae9407c1e0be4a701d` and `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5`. The binary published tree `17cecbfa8461dc139f7e8d0c55cba89dea584adf` matches the locally tested tree exactly. [GitHub Actions run 35811660258](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35811660258) completed successfully for the published binary commit, separately confirming the twenty-nine-verifier gate.

## State–speed and uncapped-boundary checkpoint

This continuation starts from published `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5`. The [research dossier](RESEARCH_DOSSIER.md) and [claim ledger](CLAIM_LEDGER.md) organize the model, assumptions, theorem dependencies, sources and drafting inputs. Manuscript drafting is not part of this checkpoint.

The [state–speed theorem](STATE_SPEED_ACCURACY_TRADEOFF.md), [unbounded-rate boundary](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md), [uniform rate regularization](RATE_REGULARIZATION.md) and [finite-state fast-rate closure](FINITE_STATE_FAST_RATE_CLOSURE.md) have separate written proofs and internal audits. The audits cover the uniform cap dependence and clock quantifiers, whole-word repair without an operator cap, the PSD substitution obstruction, reset-based Volterra estimates, vanishing-mass states and uniform convergence under arbitrary switching. Internal audits are part of this investigation, not external mathematical validation. The [source follow-up](RATE_BOUNDARY_PRIOR_ART.md) explicitly attributes classical spectral compactification and Markov aggregation and records full-text access limits.

[verify_state_speed_boundary.py](../scripts/verify_state_speed_boundary.py) produces [state_speed_boundary.json](../reports/state_speed_boundary.json) using only exact standard-library rational arithmetic. It checks all-width affine exponent inequalities, sufficient coefficient majorants, rigorously enclosed adaptive-clock constants, and finite forward/inverse width crossovers. It does not numerically invert the exponential field-interpolation matrix or estimate its potentially large constants.

A three-state reversible resolvent verifies both palindrome factorizations and the negative-involution obstruction. Five-state positive-kernel examples have exact raw operator norms 16, 1,000 and 1,000,000 while satisfying the measured whole-word hypotheses; they check nontrivial endpoint clipping, stationary flux repair and rounded-bit couplings. Their high norm is carried by a small-mass state, so these cases test the absence of a global norm assumption. They are algebraic kernels, not physical fast rivals.

A separate three-hidden-state, four-physical-state Poisson fixture checks the same-state rate transformation by exact projector functional calculus, preserves the actuator histogram and original external rates, and certifies the extra zero-field decay factor. It does not prove the general all-protocol Volterra bound. The compactness, purity and rare-fast-contamination arguments are analytic; no finite simulation is presented as their proof. The new verifier has maximum dense dimension five, and the unchanged suite-wide maximum remains 68.

The verifier received a separate static review and passed under pinned Python 3.13.5. Its report records its own source hash and separate hashes of the three proof snapshots used by its fixtures. The repository checker validates both kinds of provenance; a changed proof snapshot requires review and regeneration of this new report. Earlier reports retain their existing schemas and checkpoint-specific scope.

The complete thirty-verifier `make check` passed locally in the pinned Python 3.13.5 environment. All thirty fresh reports are byte-identical to their saved evidence. All sixty-one protected baseline files from `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5` (twenty-nine mathematical scripts, twenty-nine reports, license, dependencies and workflow) and all nine recovery files remain byte-identical. Final documentation, syntax and report-provenance checks pass. This checkpoint was published as `7f127f224eb8fe93d360a0d44b56105f8a388ce0`, with tree `325d09618926f12634b45608682b96ea74a5bcb5` matching the locally tested tree. [GitHub Actions run 35818141188](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35818141188) completed successfully for that published commit.

## Uncapped reversibility and Walsh observability checkpoint

This continuation starts from published `7f127f224eb8fe93d360a0d44b56105f8a388ce0`. The preceding thirty mathematical scripts and thirty reports, MIT license, pinned requirements and workflow are protected baselines. The nine recovery files remain preserved. The new [bounded-control resolvent theorem](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md), [uncapped reversibility lower](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) and [Walsh hierarchy](UNCAPPED_WALSH_OBSERVABILITY.md) have separate written proofs and internal reviews. Manuscript drafting is excluded from this checkpoint.

The full proof reviews cover physical convexification for each target/rival pair, one-variable analytic continuation of an entire protocol, ordered resolvent coefficient extraction, interpolation constants, positive gate approximation, whole-word repair, entropy and inversion of the accuracy threshold. They also cover all-port Walsh normalization, target-only fixed-clock transfer, and the exact width-one quotient. The uncapped reversibility lower requires arbitrarily fast switching; the Walsh hierarchy supplies a separate fixed-target rank result at fixed clock. Neither establishes a binary uncapped penalty, a fixed-clock uncapped superpolynomial separation, or the stronger uncapped lower $\exp(c\delta^{-\alpha})$. Internal reviews remain part of this investigation, not external mathematical validation or novelty certification.

[verify_uncapped_observability.py](../scripts/verify_uncapped_observability.py) produces [uncapped_observability.json](../reports/uncapped_observability.json) using exact standard-library rational arithmetic and integer enumeration. Independent coefficient recurrences check ordered sign-polarized resolvent expansions, including signed endpoint features and an internal speed of one million. The fixtures distinguish the required squared-resolvent word from a single-resolvent substitution.

A seven-hidden-state reversible generator checks positive conditional gates, reverse adjoints, a genuinely negative nonpalindromic flip correlation, and the spectral-cap and $216/s$ approximation certificates. Exact Chebyshev coefficients and rational budgets check the constants 1458 and 186624, the interpolation cutoff $M=3m$, and the error allocation leading to $\Delta\le1/(1024r^2)$. No numerical interpolation of the physical field matrix or empirical estimate of its constants is used.

Small Walsh examples check orthogonality, physical preparation/readout endpoints and exact fiber lumpability of the width-one target to 38 states. Sparse enumeration is used for these state spaces; the new maximum dense matrix dimension is seven, and the suite-wide maximum remains 68. These checks support finite algebraic identities; the general analytic continuation, all-width entropy bound and asymptotic state laws come from the written proofs. There is no large simulation, search over rivals, or extrapolation of numerical ranks.

The source and final error budgets received an independent internal static review. The saved report records the verifier source hash and hashes of the three new mathematical proof snapshots. The repository checker validates both kinds of provenance. The [source comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) records verified primary full texts and limits the novelty assessment to the complete constrained theorem.

The complete thirty-one-verifier `make check` passed locally in pinned Python 3.13.5. All thirty-one fresh JSON reports are byte-identical to saved evidence. All sixty-three protected files from the starting commit and all nine recovery files remain byte-identical. Documentation, syntax and source/proof-snapshot provenance checks pass. This checkpoint was published as 63f6be5f05af145948334324681cfaf48fe715b6 with tree 3d0ea4f5771a0647a4449fcccadb7dab5234b6e9 matching the tested tree. [GitHub Actions run 35820205357](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35820205357) completed successfully.

## Binary uncapped checkpoint

This continuation starts from published 63f6be5f05af145948334324681cfaf48fe715b6. The preceding thirty-one mathematical scripts and thirty-one reports, MIT license, pinned requirements and workflow are protected baselines. The nine recovery files are preserved separately. Manuscript drafting is excluded.

The [binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) has a complete proof through the [rare-tag construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md), [mixed observation interface](MIXED_KILLED_WORD_OBSERVABILITY.md) and [weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md). Separate internal reviews checked all four documents and the combined error budget. The reviews covered exact binary balance, every counted state, uniform gap and cap, distance-weighted killed propagation, two-distance suppression of balancing-state corrections, small selector normalizations, positive gates on arbitrary rival states, vanishing central mass, polynomial word budgets and entropy inversion.

The theorem establishes a polynomial unrestricted upper and an uncapped reversible superpolynomial lower on the new tagged family. Its explicit union with the older binary family adds a polynomial unrestricted lower. The new family has rare states and a very large fixed rate-to-gap ratio; the lower uses arbitrarily fast switching. The older numerical rate budget, fixed-clock uncapped result and stronger $\exp(c\delta^{-\alpha})$ uncapped lower are not claimed. The [source comparison](BINARY_OBSERVATION_PRIOR_ART.md) records primary full-text comparisons and access limits without certifying originality.

[verify_binary_uncapped_observability.py](../scripts/verify_binary_uncapped_observability.py) produces [binary_uncapped_observability.json](../reports/binary_uncapped_observability.json) using only exact standard-library rational arithmetic and finite enumeration. It has no imports from earlier repository verifiers. The saved report records its own source and the five new mathematical proof snapshots; the repository checker validates these hashes.

Three-state balanced examples verify positive binary words with negative quadratic forms for both a resolvent and its square, and the failure of a color-only palindrome test with unequal resolvent parameters. The [boundary note](BINARY_UNCAPPED_RESEARCH_BOUNDARY.md) proves the exact scope of those examples and the remaining PSD subclass. Neither a negative scalar nor these examples alone establishes a state-count lower.

Independent ordered coefficient calculations check mixed resolvent polarization with noncommuting rational contraction factors and cross-color leading cancellation. The contraction factors are finite algebraic proxies: the script does not claim to evaluate the general killed semigroup. Weighted examples include zero support, tiny positive marker values, the exact change of measure and scalar identities; finite stationary couplings check the partial-flip entropy mechanism.

An eight-state tag-and-chain toy checks positive rates, detailed balance, exact histogram, the original field rule and a positive fast-sector certificate. Exact rational exponent inequalities cover all eighteen canonical tag types, their discrimination margins, the distant-state error budgets, and the full theorem's word-count and extraction-tail bounds. The enormous canonical chains and bit tables are counted analytically and never allocated.

The new maximum dense dimension is eight; the suite-wide maximum remains 68. The finite verifier received independent internal static review. Its checks support the displayed algebra and error budgets, while the universal propagation estimates, physical analytic continuation and asymptotic state laws remain analytic proofs. Local verification, remote CI and external mathematical review are distinct forms of evidence.

The complete thirty-two-verifier gate passed locally in pinned Python 3.13.5. All thirty-two fresh reports are byte-identical to saved evidence. The final repository checker passes 1,090 local Markdown links, 33 Python syntax checks, saved-source/proof-snapshot provenance and the unchanged license. All sixty-five protected baseline files and all nine recovery files remain byte-identical. Remote CI for this new continuation is checked separately after publication.

## Fixed-clock uncapped checkpoint

This continuation starts from published `33f23b7cacb65b5e17692771022286f1b94c6999`, whose tree `6503c39327c5171dd88ea9f1a03b5f6e2ae86c8e` matched the preceding tested checkpoint. [GitHub Actions run 35837920760](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35837920760) passed its thirty-two-verifier gate. The sixty-seven baseline mathematical scripts, saved reports, license, requirements and workflow are protected, as are all previously hash-bound proof snapshots and the nine recovery files. Manuscript drafting is excluded.

The [fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md), [Gram interface](FIXED_CLOCK_GRAM_OBSERVABILITY.md), and [positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) establish the two-field uncapped penalty with a conservative inner logarithmic exponent $1/12$. The [internal proof review](FIXED_CLOCK_INTERNAL_REVIEW.md) covers finite row recovery, sampled Gram norms, target-sensitive vector remainders, model-dependent Schur denominators, binary insertions, uniform heat approximation, natural-killing scaling, entropy normalization, the polynomial error budget and finite clock horizon. These are internal reviews, distinct from executable checks and external validation.

[verify_fixed_clock_observability.py](../scripts/verify_fixed_clock_observability.py) produces [fixed_clock_observability.json](../reports/fixed_clock_observability.json). It adds 1,543 finite checks, using exact rational arithmetic for algebraic identities and explicitly labeled float64 calculations for actual semigroups, integrated polynomial coefficients and heat residuals. Dense matrices have dimension at most four. It constructs no large tagged graph and imports no earlier repository verifier.

The exact fixtures check visible-row recursion including zero fields, stationary adjoints, inserted-projector and Gram identities, the physical Schur complement, two-field binary insertion, contractive symmetrized label factors and their possible failure of positive semidefiniteness. The leading cross-color coefficient two and sandwich normalization four are verified separately. Fractional-binomial tail identities, coefficient mass, natural-killing scaling and shifted-Chebyshev recurrence checks supplement the written analytic bounds. A separate representative exponent calculation verifies the powers $4,5,6,7,12$; it does not estimate the theorem's potentially enormous physical constants. The actual numerical errors are recorded beside their bounds, not presented as universal estimates.

The report records its verifier source hash and the three new proof snapshot hashes. The repository checker validates these alongside all existing saved evidence. A separate internal reviewer inspected and ran the new verifier. The [primary-source comparison](FIXED_CLOCK_PRIOR_ART.md) distinguishes embedding and matrix-function results, scalar mean recovery, and observable-operator learning; it neither certifies originality nor converts the weaker logarithmic transfer route into an impossibility theorem.

The complete thirty-three-verifier `make check PYTHON=.venv/bin/python` gate passed locally in pinned Python 3.13.5. All thirty-three fresh JSON reports are byte-identical to saved evidence. All sixty-seven protected baseline files and all nine recovery files remain byte-identical; earlier proof snapshots also pass their saved hash checks. The repository checker passes 1,190 local Markdown links and 34 Python syntax checks, with valid source/proof provenance and an unchanged license. Remote CI is separate evidence, associated with the published commit in GitHub Actions.

## PRL exploration checkpoint

This phase starts from published `04d34df8de8643a44515725c1330d55e8c6f53bc`, tree `22e0def6b56d6339de9a720a872e7743270a242f`. [GitHub Actions run 35841494249](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35841494249) passed the preceding thirty-three-verifier gate. The sixty-nine baseline scripts, reports, license, requirements and workflow, earlier proof snapshots and nine recovery files remain protected. PRL is the user's research target; manuscript drafting remains deferred.

The new proofs are [positive label selectors](POSITIVE_LABEL_SELECTORS.md), [the original tight-band fixed-clock separation](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md), [uniform entropy-production reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) and [the state–entropy-production consequence](STATE_ENTROPY_PRODUCTION_TRADEOFF.md). Their [internal review](PRL_EXPLORATION_INTERNAL_REVIEW.md) checks positivity versus positive semidefiniteness, normalized selector powers, the unchanged target band, the fifth-power observation budget, uniform last-reset entropy bounds, entropy-rate conventions and minimax quantifiers. The [source audit](PRL_EXPLORATION_SOURCE_AUDIT.md) attributes the established symmetrization and entropy-comparison ingredients.

[verify_prl_exploration.py](../scripts/verify_prl_exploration.py) produces [prl_exploration.json](../reports/prl_exploration.json). Its bounded fixtures test the positive selector identities, exact positive-semidefinite certificates, off-grid rival labels, conservative power budgets, arithmetic reversibilization, preservation of exits and stationary masses, the sharpened relative-entropy factor, reset-age integration, and finite-entropy-production regularization. It uses exact rational identities, with numerical matrix exponentials, quadrature and logarithms explicitly labeled; the nineteen-level scalar selector check uses 80-digit arithmetic. It allocates no large target graph.

The new report binds its verifier source and all four new proof snapshots. It contains 561 checks, and passed a separate internal code review and independent pinned-environment rerun with a byte-identical report. Dense matrices have dimension at most five; the suite-wide maximum remains 68. Finite checks supplement the universal analytic claims and do not certify them by enumeration. Local regression, remote CI and mathematical review remain separate evidence.

The complete thirty-four-verifier `make check PYTHON=.venv/bin/python` gate passed locally in pinned Python 3.13.5. All thirty-four fresh reports are byte-identical to saved evidence. All sixty-nine protected baseline files and nine recovery files remain byte-identical, and all earlier proof snapshots pass their recorded hash checks. The final repository checker passes 1,317 local Markdown links and 35 Python syntax checks, with valid source/proof provenance and unchanged license. Remote CI is separate evidence tied to the published commit in GitHub Actions.

## Updating evidence after code changes

Do not edit saved metrics by hand. After reviewing and running a changed extension, regenerate the saved evidence with:

```bash
python scripts/verify_finite_accuracy.py --output reports/finite_accuracy.json
python scripts/verify_quadrature.py --output reports/quadrature.json
python scripts/verify_minimal_realization.py --output reports/minimal_realization.json
python scripts/verify_response_lower_bounds.py --output reports/response_lower_bounds.json
python scripts/verify_unrestricted_rate_lower_bound.py --output reports/unrestricted_rate_lower_bound.json
python scripts/verify_finite_field.py --output reports/finite_field.json
python scripts/verify_path_information.py --output reports/path_information.json
python scripts/verify_actuator_hierarchy.py --output reports/actuator_hierarchy.json
python scripts/verify_general_compression.py --output reports/general_compression.json
python scripts/verify_reversible_compression.py --output reports/reversible_compression.json
python scripts/verify_general_controlled_lower_bound.py --output reports/general_controlled_lower_bound.json
python scripts/verify_bounded_rate_prediction.py --output reports/bounded_rate_prediction.json
python scripts/verify_shift_register_lower_bound.py --output reports/shift_register_lower_bound.json
python scripts/verify_polynomial_controlled_lower_bound.py --output reports/polynomial_controlled_lower_bound.json
python scripts/verify_constant_step_compression.py --output reports/constant_step_compression.json
python scripts/verify_bounded_density_sampling.py --output reports/bounded_density_sampling.json
python scripts/verify_analytic_constant_step.py --output reports/analytic_constant_step.json
python scripts/verify_moment_density_sampling.py --output reports/moment_density_sampling.json
python scripts/verify_sparse_reversible_compression.py --output reports/sparse_reversible_compression.json
python scripts/verify_local_walk_lower_bound.py --output reports/local_walk_lower_bound.json
python scripts/verify_expander_scenery_compression.py --output reports/expander_scenery_compression.json
python scripts/verify_expander_scenery_lower_bound.py --output reports/expander_scenery_lower_bound.json
python scripts/verify_aggregation_state_lower_bound.py --output reports/aggregation_state_lower_bound.json
python scripts/verify_register_scenery_compression.py --output reports/register_scenery_compression.json
python scripts/verify_soft_aggregation_lower_bound.py --output reports/soft_aggregation_lower_bound.json
python scripts/verify_exact_reversible_prefix_obstruction.py --output reports/exact_reversible_prefix_obstruction.json
python scripts/verify_dynamic_lamp_reversibility_lower_bound.py --output reports/dynamic_lamp_reversibility_lower_bound.json
python scripts/verify_binary_reversibility_lower_bound.py --output reports/binary_reversibility_lower_bound.json
python scripts/verify_state_speed_boundary.py --output reports/state_speed_boundary.json
python scripts/verify_uncapped_observability.py --output reports/uncapped_observability.json
python scripts/verify_binary_uncapped_observability.py --output reports/binary_uncapped_observability.json
python scripts/verify_fixed_clock_observability.py --output reports/fixed_clock_observability.json
python scripts/verify_prl_exploration.py --output reports/prl_exploration.json
make check
```

The preserved checkpoint verifier remains an unchanged regression baseline. New tests belong in the extension or a new verifier; a deliberate change to that baseline requires revising its provenance explicitly.

## Limits

No large simulations, training, Monte Carlo trajectories, or network requests occur inside the verifiers. A PASS verifies the stated assertions in these programs, not all possible models or protocols by enumeration. Small floating-point errors are expected to differ across platforms. The code and proofs were produced within the same investigation; agreement is not an independent audit. No journal submission, release, physical implementation, or claim of publication-level novelty follows from these checks.
