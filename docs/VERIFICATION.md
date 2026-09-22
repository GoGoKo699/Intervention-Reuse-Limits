# Verification scope and provenance

[Repository overview](../README.md) · [Core theory](THEORY.md) · [Finite accuracy](FINITE_ACCURACY.md)

## Reproducing the checks

From the repository root, install [the pinned dependencies](../requirements.txt) and run `make check`. The target checks local Markdown links, display-math/code-fence balance, Python syntax, report provenance, and the original MIT license. It then runs all four mathematical verifiers. Fresh reports are written to `.check-output/`, not over the saved reports.

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

## Updating evidence after code changes

Do not edit saved metrics by hand. After reviewing and running a changed extension, regenerate the saved evidence with:

```bash
python scripts/verify_finite_accuracy.py --output reports/finite_accuracy.json
python scripts/verify_quadrature.py --output reports/quadrature.json
python scripts/verify_minimal_realization.py --output reports/minimal_realization.json
make check
```

The preserved checkpoint verifier remains an unchanged regression baseline. New tests belong in the extension or a new verifier; a deliberate change to that baseline requires revising its provenance explicitly.

## Limits

No large simulations, training, Monte Carlo trajectories, or network requests occur inside the verifiers. A PASS verifies the stated assertions in these programs, not all possible models or protocols by enumeration. Small floating-point errors are expected to differ across platforms. The code and proofs were produced within the same investigation; agreement is not an independent audit. No journal submission, release, physical implementation, or claim of publication-level novelty follows from these checks.
