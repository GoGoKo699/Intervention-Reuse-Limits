# Verification scope and provenance

[Repository overview](../README.md) · [Core theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

## Reproducing the checks

From the repository root, install [the pinned dependencies](../requirements.txt) and run `make check`. The target checks local Markdown links, display-math/code-fence balance, Python syntax, report provenance, and the original MIT license. It then runs all twelve mathematical verifiers. Fresh reports are written to `.check-output/`, not over the saved reports.

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
make check
```

The preserved checkpoint verifier remains an unchanged regression baseline. New tests belong in the extension or a new verifier; a deliberate change to that baseline requires revising its provenance explicitly.

## Limits

No large simulations, training, Monte Carlo trajectories, or network requests occur inside the verifiers. A PASS verifies the stated assertions in these programs, not all possible models or protocols by enumeration. Small floating-point errors are expected to differ across platforms. The code and proofs were produced within the same investigation; agreement is not an independent audit. No journal submission, release, physical implementation, or claim of publication-level novelty follows from these checks.
