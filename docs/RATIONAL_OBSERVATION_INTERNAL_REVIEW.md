# Internal review of rational observation and symmetry compression

[Rational observation theorem](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Symmetry compression](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) · [Source comparison](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**Internal mathematical audit, 23 September 2026.** Both new proof notes pass the independent internal reviews recorded here. This is neither external peer review nor priority certification. Earlier proof snapshots and verifiers are unchanged. Manuscript drafting remains deferred.

## 1. Target basis and exact certificate

The full stochastic intertwiner of the twelve-state target has a ten-dimensional invariant column space: four incidence directions, five probes and the visible state. It contains the constant, binary readout and visible projector range. The ten finite clock-word functions in the new theorem span this space once their weighted Gram is positive definite.

The basis inequality is an essential computer-assisted premise, not merely a diagnostic fixture. Exact rational arithmetic encloses the transcendental clock and propagators: an 80-term logarithm series, 192-bit dyadic rounding, a degree-64 Taylor polynomial, and explicit outward matrix/vector errors give a Gram error at most $1281/2^{180}<2^{-150}$. Exact rational LDL elimination shows the rounded Gram minus $2^{-51}I$ has ten positive pivots. Hence the true Gram is greater than $2^{-52}I$, giving smallest singular value at least $2^{-26}$. Floating eigenvalues and exponentials do not enter this premise.

Separate full source reviews checked the logarithm tail, Horner recurrence, stochastic time-perturbation bound, rounded-product errors, vector orientation, weighted Gram enclosure and pivot positivity. The small numerical singular-value diagnostic is not used as proof. Invariance and closure are exact algebraic facts; the certificate is specific to this target and basis.

## 2. Actual means to positive rational features

The Gram reconstruction retains the original stationary preparation and binary endpoint readout. In the common zero-field metric, adjoints at field $H$ are recovered through the known visible/hidden weight operator. Visible-projector insertions are recovered by the existing scalar recursion; they are not extra experimental preparations or path measurements.

An independent implementation reconstructed the complete menu from the nine raw words, their left extensions, and every contiguous subword of a reversed word followed by another word. It reproduced all **12,766** words, maximum length **66**, and the canonical export checksum. This verifies that all segments needed by the insertion recursion belong to the permitted physical experiment menu. The Gram-entry error multiplier $612549$ is below $2^{20}$.

The basis defines a map into every ordinarily reversible rival. Finite Gram agreement gives its near-isometry defect and bounds its residual for the two clock propagators and visible projector. Closure on the target space is essential: the rival need not have the same dimension or invariant subspace. The proof does not assume a rival stationary mass floor or inherited kinetic labels.

The full exit cap bounds the sampled spectra away from zero. The exact logarithm quasi-commutator integral then transfers approximate intertwining from the clock propagators to generators. Its resolvent norm comparison accounts for the two reversible metrics. Compression to the hidden block preserves the hidden constant exactly; both the barrier operator and positive uniformized kernel have controlled residuals.

For each target node, the normalized squared Lagrange selector has divided-difference bound 512. This follows from the exact barycentric weights, node spacing and a near/far split. The denominator is at least $1/6$ throughout the rival interval. The functional-calculus estimate uses the target's six orthogonal spectral projectors; it does not invoke a false general implication from scalar Lipschitz to operator Lipschitz continuity. The selector acts on the hidden space and is extended by zero on the visible state: its scalar value at zero must not be applied to the visible coordinate.

Nonnegative rival features then have Gram-entry error bounded by

$$
2^{97}\sqrt\delta+2^{188}\delta.
$$

At $\delta=2^{-220}$ this is $2^{-13}+2^{-32}<1/1500$. The frozen completely positive Gram obstruction therefore requires at least eleven hidden atoms, hence twelve total states. The target itself supplies the matching ordinary-reversible upper. The root reviewer and a separate mathematical reviewer read the complete canonical proof; source/menu reviewers independently audited the exact certificate and enumeration. No unresolved proof issue remained at freeze.

## 3. Symmetry compression and the quadratic error

Exchanging two right-side probes and their incident edge pairs preserves the target's hidden generator, stationary preparation and readout. Averaging the two probe barriers makes the full generator commute with this involution. Its orbit partition is strongly lumpable and has eight hidden states plus the visible state. Summing detailed balance over orbit pairs gives ordinary reversibility, with no increase in the hidden exit cap. At the two queried fields the averaged barriers can be implemented by effective exponential sensitivities; arithmetic curves over an entire interval have a different scope.

The generator perturbation is odd under the symmetry. Decomposing the actual law into even and odd parts gives exact coupled evolution equations; the readout sees only the even part. Thus an odd perturbation must act twice to change the measured response. The proof bounds the complete finite-amplitude remainder, not just the quadratic Taylor coefficient.

For the two fields, the invariant box $p_A\le1/2$ and $p_i/\mu_i\le2$ bounds the odd source by $\eta/6$, where $\eta=k/32$. Conditional block refresh and return killing give odd-sector decay $11k/8$. Exact evaluation of all 66 unordered state pairs at each field gives full-law contraction at least $9k/8$. Variation of constants twice then bounds the binary-mean error by

$$
\frac{2\eta^2}{3(9k/8)(11k/8)}=\frac1{2376},
$$

uniformly over all two-field switching protocols and horizons. The nine-state predictor is fixed across protocols. The proof also gives a separate all-field upper $4096/200475$ using arithmetic averages of barrier curves; the sharper occupation box and endpoint exponential implementation are not extended to that claim.

Root and two separate reviewers checked the canonical analytic proof. A further full code review checked quotient construction, detailed balance, cap/band, odd-sector identities and the complete rational contraction table. The verifier's few switched trajectories and amplitude comparisons are implementation diagnostics, not a search over protocols or rival models. They do not certify the all-protocol bound or estimate optimal approximation error.

## 4. Accuracy and interpretation boundaries

For the full two-field clock task, the earlier unrestricted minimum of eleven persists on $\delta\le2^{-1360}$. The new theorem proves ordinary-reversible minimum twelve up to $2^{-220}$ and retains an exact unrestricted sufficient count of eleven. It does not extend unrestricted minimality to the enlarged interval or prove it from the smaller new experiment menu.

The nine-state reversible upper at $1/2376$ leaves a broad unresolved interval above the state-gap lower. Neither nine-state minimality nor the best error achievable with eleven reversible states is known. The explicit finite menu does not make the required precision practical and gives no sample-complexity guarantee. Better-conditioned bases, direct positive finite-time features or a stronger target remain research directions. Simply normalizing a large polynomial does not by itself provide a stable observation bound; proposed stronger pulses must count any changed control, rate and timing resources.

Ordinary reversal continues to mean the physical reversal of even configurations in the stipulated model. The symmetry permutation used for quotienting is not a reassignment of physical parity. No universal heat requirement or new generalized-reversible eleven-state realization follows. The microscopic realization question remains separate.

The [source audit](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) attributes finite observable realization, divided-difference calculus, second-order response and contraction-controlled perturbation bounds to inspected prior work. The candidate contribution is the complete constrained connection and its explicit certificates, not those general mechanisms or the previously known core matrix.

## 5. Frozen snapshots and reproducible checks

| Artifact | SHA-256 |
|---|---|
| `BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md` | `3082b801ed5a621bc7c5ee609e5d6682b40d6986af955a493d8652aaedfc15a9` |
| `SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md` | `38bc3447bbe6578eb37a6917d5e6ef700696077a3c98c499be47ed1dbff357cf` |
| `RATIONAL_OBSERVATION_SOURCE_AUDIT.md` | `5d0d45344de9e35bd17306670d0541c6a3cb4fbc388335114a188b29f2a1d1f4` |

The [rational verifier](../scripts/verify_rational_observation.py) passes **98 exact checks**, binds seven proof snapshots and uses dense dimension at most twelve. The [symmetry verifier](../scripts/verify_symmetric_compression.py) passes **283 checks**, binds its theorem and target proof, and also uses dense dimension at most twelve. Both finalized reports were independently regenerated under pinned Python 3.13.5 and matched the saved reports byte for byte. Full-suite preservation and live publication checks are recorded separately in [Verification](VERIFICATION.md).
