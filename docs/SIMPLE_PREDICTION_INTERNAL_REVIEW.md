# Internal review of the simple prediction principles

[Matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) · [Kinetic variance](KINETIC_VARIANCE_COMPRESSION.md) · [Source comparison](SIMPLE_PREDICTION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**Internal mathematical review, 23 September 2026.** The two new notes pass the separate derivation and source-code reviews recorded here. They organize a general state-count theorem and a coarse-accuracy limit around short mechanisms. These are internally reviewed research results, not external peer review or novelty certification. Manuscript drafting remains deferred.

## 1. From a positive matrix to a controlled process

For a normalized completely positive matrix $H$ with positive row sums $v$, any nonnegative factorization normalizes to stochastic memory-to-probe and probe-to-memory kernels $R,T$. Direct multiplication gives $TR=\operatorname{diag}(v)^{-1}H$, $vT=a$, and $aR=v$. Removing zero factors makes every retained stationary mass positive. Conditional block refresh preserves these identities and gives hidden exit cap two. Completely positive factors give exact cross-block detailed balance; the block-constant decomposition then gives the target band $[k,3k]$.

The common map $\operatorname{diag}(1,R,I)$ is stochastic. It intertwines every controlled generator with the canonical endpoint predictor, preserves preparation and binary readout, and commutes with both output-class projectors. Thus all factorizations give identical controlled means and identical finite-dimensional binary-output distributions. The map uses only the present state; it has no access to future fields. The construction also retains the exact passive two-state path law.

This proves sufficient counts for every matrix in the stated class, not merely for the earlier incidence graph. The factorization algorithms or their computational efficiency are not part of the theorem.

## 2. Minimum counts against arbitrary rivals

The exact clock recovery applies to stationary rivals without reversibility. Its full-rate bound follows from the shared hidden cap and bounded endpoint interface. Squared interpolation polynomials are nonnegative on every rival barrier, while the uniformized hidden kernel is positive. Thus matched left/right words give a nonnegative factorization through the rival's own hidden states. Ordinary detailed balance makes the left word the stationary adjoint of the right, giving a nonnegative-feature Gram.

On the target, the matrix is exactly

$$
N_* = \operatorname{diag}(H/2,\operatorname{diag}(v)/2).
$$

The memory factor $1/2$ and the additional probe block were independently checked. Nonnegative and completely positive ranks add across these blocks because positive factors cannot cross a target zero. Consequently the minimum total counts are $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$. Rivals need not have a prescribed memory/probe partition, palette or histogram. The positive-feature argument, not an imposed architecture on rivals, gives the lower bound.

The finite-accuracy existence corollary was checked separately. Fixed-factor-count nonnegative-rank sets are closed after normalizing each left factor; the right factors are bounded by matrix column sums. Fixed-factor-count completely positive sets are closed because the trace bounds every factor norm. The target therefore has positive distance from each class with too few factors. A common finite clock cutoff and a sufficiently small positive mean tolerance transfer this distance to all physical rivals. This proves a matrix-dependent interval; no useful or uniform size is asserted.

The root and two separate mathematical reviewers read the complete canonical note, including the path-law upper and positive-error corollary. All reported no remaining mathematical issue. The source review also checked the necessary scope distinction: generic discrete-time HMM pair data use a different structured factorization. This is a theorem for the specified controlled continuous-time task, not a classification of arbitrary HMM order.

## 3. Hidden deviations must be excited and read out

For the variance theorem, the hidden density relative to its common stationary law splits into its mean and a centered residual $z$. The exact master equation has centered barrier $c=b-\mu b$ in both the source of $z$ and the visible error. Eliminating $z$ produces an exact protocol-dependent kernel $k^2\langle c_t,G(t,s)c_s\rangle_\mu$.

Stationarity gives the Dirichlet identity even for nonreversible hidden generators. Its symmetric gap, together with positive return killing, contracts the centered propagation. The visible error satisfies a damped scalar equation. These two estimates give the uniform barrier-variance bound, without a microscopic state count, minimum stationary mass or hidden rate cap. A common hidden law and the specified initial conditional law are essential. Field-dependent hidden generators are allowed under the stated common-law and gap assumptions.

The inactive-field refinement uses the fact that both forcing terms vanish there, so their norms cannot increase. On the finite target only field $H$ is active. The visible probability remains at most $1/2$, giving source bound $3/2$. With variance $557/49152$, centered damping $11k/8$ and visible damping factor $295/128$, the two-state mean upper is $557/51920$. This is a sufficient estimate, not the optimal two-state error.

For an invariant partition, the same proof uses within-block conditional variance. Commutation of the conditional projector with every hidden generator is required; arbitrary barrier binning is insufficient. The quotient inherits ordinary reversibility and the exit cap when the original hidden generator has them. A field-dependent original generator need not give a field-independent multi-block quotient. The one-block predictor always has zero hidden generator. The earlier nine-state bound $1/2376$ follows from the conditional variance formula with its frozen constants.

The root and an independent mathematical reviewer checked the entire variance proof. The exact kernel is an instance of established projection methodology; the specific uniform controlled bound and constants are its present application. The guarantee concerns endpoint means, not a uniform approximation to whole paths. Averaged exponential curves match a single exponential at the two queried fields, but generally not on an interval.

## 4. Bounded verification and snapshots

The new [combined verifier](../scripts/verify_simple_prediction_principles.py) and [saved report](../reports/simple_prediction_principles.json) contain **200 exact checks**, with maximum dense dimension **12**. All arithmetic uses rational fractions and integers. A positive rank-two example supplies distinct reversible and nonreversible factorizations of the same matrix; the incidence example recovers the established eleven/twelve counts. Checks cover generator normalization, stationarity, caps, reversible band certificates, complete-generator and output-projector intertwining, and the matched feature matrix. Separate reversible and circulating cycle fixtures check the centered master equation and quadratic-form damping. Rational checks validate both variance bounds.

These are bounded algebraic certificates. The program neither solves arbitrary factor-rank problems nor proves the universal state-count and all-protocol statements by enumeration. It performs no trajectory simulation or numerical fitting. Root and separate full code reviews passed; an independent pinned Python 3.13.5 rerun reproduced the saved report byte for byte, and every bound proof snapshot matched.

| Frozen note | SHA-256 |
|---|---|
| `MATRIX_RANK_PREDICTION_PRINCIPLE.md` | `6d13e4f33b8166c1f125eaaf582692dc0523f7e39c23152bf0f82aa105bd8ab2` |
| `KINETIC_VARIANCE_COMPRESSION.md` | `642b2e907dcf37c289af1e2cfc09c98a3b56412fe847d892579c18e09b6646f1` |
| `SIMPLE_PREDICTION_SOURCE_AUDIT.md` | `fbeeb059721f0ec616445c32770b09a0e827c5c98c9f0b4b5b29d66a6a2ab495` |

Full-suite preservation and remote CI are recorded separately in [Verification](VERIFICATION.md). The simple physical interpretation does not remove the specified interface, reversal convention or accuracy limitations. No universal dissipation claim follows.
