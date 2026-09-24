# Internal review of observable preparation and readout calibration

[Preparation theorem](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) ·
[Sampling precision](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) ·
[Readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) ·
[Source audit](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md) ·
[Verifier](../scripts/verify_switch_observable_calibration.py) ·
[Report](../reports/switch_observable_calibration.json) ·
[Verification](VERIFICATION.md)

**24 September 2026.** Separate authors, a critic, an independent exact
implementation and the coordinator examined this supporting checkpoint.
The preparation and sampling proofs received independent mathematical
review. The readout example was implemented independently of its original
scratch calculation, and the coordinator reviewed its positive endpoint
lemma. These are internal research checks, not external peer review,
priority certification or an achieved experimental specification.

## Preparation without a rival mixing-time bound

Review re-derived the three-state decomposition into visible imbalance
and a hidden difference within the doubleton sector. The exact kernel-row
identity and its zero-sum oscillation bound give the sharper imbalance
term $L|b-v|/(1-v)$ before taking a uniform orientation bound. The
stationary imbalance is not multiplied by the inverse observed
relaxation. The flip-probability estimate gives
$r\le4k(1+V)/(1-V)$, with $k>0$ when the observed relaxation guard is
positive. No reversibility, minimum stationary mass or mixing-time
bound enters this argument.

The detector conversion was checked separately. A sufficiently large
original recorded correlation lower-bounds the common detector contrast
product. A smaller low-pair correlation can then certify relaxation;
the low-pair correlation alone cannot separate relaxation from electronic
attenuation. The positive-part convention also covers a negative
low-pair correlation.

The stated guards $g=.45$ and $c_K\le.15$ give $r\ge2/3$. For
$V=10^{-4}$ the score preparation correction has a nonzero
conservative floor $94/249975\simeq.000376038$ even when the three
recorded correction statistics vanish. This is an upper bound from the
chosen assumptions, not a physical noise floor or a statistical lower
bound.

## The effective calibration operation must match

An initial protected measurement can change an unknown preparation
inside a visible sector even when it preserves the equilibrium joint
law exactly. Therefore the low-pair correlation probes $K=DP$, not $P$
alone. Each prefixed protocol must apply the same nonselective instrument
$D$ before the low evolution. Recording and discarding its label is a
valid silent implementation; omitting the physical operation is not.

This matching requirement adds an instrument operation to each prefixed
type. Its duration and control are resources, even though its label is
not an additional retained data value. The supporting theorem assumes
exact sector preservation, exact stationary preservation and electronic
errors independent of the hidden instrument action. The earlier small
nonzero stationary instrument allowance is not automatically admitted by
this new theorem.

The score's opposite initial-bit terms cancel pointwise only because the
two original response channels share the preparation, instrument and
detector. The recorded means and correlations receive separate
preparation radii. Those radii are needed to localize the stationary
reference before invoking its ordinary score ceiling. A score-only bound
is insufficient: stationary identity kernels can give score $.04$ while
lying outside the witness's localization gates.

## Random assignment and the large precision budget

Random assignment occurs after the common preparation and is independent
of the prepared state. Fixed response channels then make every weighted
observable refer to the same pathwise averaged preparation. That
preparation may be random and history-dependent. The concentration proof
uses its predictable averages without conditioning on its final value.

Review checked the inverse-probability estimator's fixed total-trial
normalization. Dividing by random type counts would not give the stated
argument. Likewise, the initial records of the prefixed types occur
after $K$ and cannot be pooled with the original initial records as if
they measured the same preparation.

Opposite score midpoint shifts cancel in the summed original and prefixed
responses. The fixed assignment probabilities bound all eight signed
estimators by a common range
$R=311165662/2249775<139$. Both tails of all eight statistics must be
covered because their minimizing sign can depend on the random averaged
preparation. The conditional bounded-range moment-generating-function
proof and the resulting 16-tail union bound are valid without independent
trials.

The exact arithmetic certifies that 60 billion trials estimate those
eight scalar correction functionals simultaneously within $.001$ with
probability above 96%. This is 120 billion recorded binary values and
12,000 times the earlier five-million allocation. It is deliberately a
sufficient precision construction, not a lower bound and not a completed
five-type rejection or target-power guarantee. Statistical confidence for
the guards and localization, target acceptance, and systematic-error
amplification remain separate work.

## The instrument cannot be inferred from the listed checks

The new three-state ordinary example preserves the visible state and the
equilibrium hidden marginal. Its immediate repeated records have exactly
the law of independent binary symmetric errors, and all low-only visible
processes and stationary future endpoint-insertion checks agree with a
nondisturbing reference. A fresh electronic error nevertheless shares
randomness with a hidden kick.

Independent exact implementation reproduced joint label/state TV
$1/200$ and original-word joint-table TV $1/4800$ for both words. The
finite-time conditional half-reset variant retains all calibration
agreements and gives table TV $1/9600$. Neither fixture is asserted to
pass the selected target's score gates. Their role is to demonstrate
that these calibration records do not establish electronic-error
independence from hidden backaction.

The positive endpoint lemma was also checked: under actual sector
preservation and electronic independence, disturbance of any fixed
future endpoint law equals disturbance of the full initial-record/future
joint law for at most three states. All signed changes reside in the
single doubleton sector. Repairing sector-changing transitions gives the
stated endpoint-plus-$2\epsilon$ bound. This lemma is conditional on the
structural instrument assumptions and concerns the same preparation at
which the endpoint comparison is made.

## Verification and claim boundary

The final verifier passed **75 exact checks**, with largest dense matrix
dimension three, no floating arithmetic and no optimization. A separate
execution produced a report byte-identical to the canonical report.
The checks include the sharp polynomial identity, detector and score
constants, the ordinary reversible fixture, repeated-readout and
low-lumpability identities, both joint-table discrepancies, the positive
endpoint factorization, and the scalar sampling arithmetic. The
hash-bound proofs supply the universal arguments.

This checkpoint does not transfer the old five-million guarantee, its
observed-law approximation allowance, or its nonzero instrument-error
class to the new experiment. The existing general three-state model
matches the two original tables; no fit to the three added calibration
types has been proved here. The two-word state-count result remains
unchanged. Manuscript drafting remains deferred.
