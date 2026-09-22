# Verification scope and provenance

[Repository overview](../README.md) · [Core theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

## Reproducing the checks

From the repository root, install [the pinned dependencies](../requirements.txt) and run `make check`. The target checks local Markdown links, display-math/code-fence balance, Python syntax, report provenance, and the original MIT license. It then runs all six mathematical verifiers. Fresh reports are written to `.check-output/`, not over the saved reports.

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

The finite-field check is consistent with a fourth-order truncation remainder; it is not a proved uniform remainder bound.

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

## Updating evidence after code changes

Do not edit saved metrics by hand. After reviewing and running a changed extension, regenerate the saved evidence with:

```bash
python scripts/verify_finite_accuracy.py --output reports/finite_accuracy.json
python scripts/verify_quadrature.py --output reports/quadrature.json
python scripts/verify_minimal_realization.py --output reports/minimal_realization.json
python scripts/verify_response_lower_bounds.py --output reports/response_lower_bounds.json
python scripts/verify_unrestricted_rate_lower_bound.py --output reports/unrestricted_rate_lower_bound.json
make check
```

The preserved checkpoint verifier remains an unchanged regression baseline. New tests belong in the extension or a new verifier; a deliberate change to that baseline requires revising its provenance explicitly.

## Limits

No large simulations, training, Monte Carlo trajectories, or network requests occur inside the verifiers. A PASS verifies the stated assertions in these programs, not all possible models or protocols by enumeration. Small floating-point errors are expected to differ across platforms. The code and proofs were produced within the same investigation; agreement is not an independent audit. No journal submission, release, physical implementation, or claim of publication-level novelty follows from these checks.
