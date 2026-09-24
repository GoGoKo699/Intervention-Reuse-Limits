# Internal review: two preparations, four endpoints and two pulse orders

[Proof](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) · [Cost analysis](FAMILIAR_SWITCH_PREPARATION_COST.md) · [Source comparison](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** This records internal mathematical and implementation
review. It is not external peer review, a novelty certificate or evidence of
experimental implementation. Manuscript drafting remains deferred.

## 1. Analytic witness and state counts

The root and separate reviewers independently derived the four-response
identity. Low-field reversibility identifies the mixed inner product;
high-field reversibility and the Gibbs change of measure supply the
remaining conditional moment. Their combination gives the exact
conditional covariance in either readout sector. A direct singleton
pointwise identity supplies a second derivation. Both include degenerate
kernels and two-state models without a determinant or rank assumption.

The physical mean closure gives a positive conditional covariance at both
readout signs for every finite positive coupling, high field and pulse
duration. The corresponding all-parameter positive error formula follows
from an explicit linear-plus-quadratic perturbation bound. The existing
three-state positive realization matches both stationary preparations
because their closed mean coordinates agree. Two-state stationary models
are automatically ordinary reversible, so the lower also establishes
unrestricted minimum three. The ordinary upper is the physical four-state
target. The comparison requires two Gibbs-related stationary preparations
and one fixed model across the four cells.

The selected rational certificate uses the same coupling and field as the
previous checkpoint, with tick $3/2$. The lower $9/5000$ and feasible upper
$1/550$ concern the same maximum occupation-error norm and the same four
experiments. Their ratio is $100/99$. A local fit proposed the rational
upper; exact interval propagation, rather than the optimizer, certifies it.
No claim that the necessary quadratic equation characterizes every
realizable three-state response is needed.

## 2. Calibration and preparation

Separate reviewers checked the biased stationary-law identity and the
approximate-tilt residual. The high-field law discrepancy enters through
three stationarity/reversibility defects and replacement of the two
high-preparation responses. The exact six-variable box excludes both
allowed residual bands; this finite arithmetic is an essential numerical
premise of the stated $17/10000$ nominal-reference exclusion.

The physical transfer charges target and rival preparation errors
separately. It also charges field-induced equilibrium shifts, rate changes
over the actual active duration, and timing errors. The combined bound
under the simultaneous $10^{-5}$ tolerances is $0.0000800001<10^{-4}$.
This leaves actual occupation separation greater than $1/625$, while the
three-state predictor approximates the actual target within $10^{-5}$.
The previously proved positive-rate extension covers slightly negative
low fields and both actual stationary preparations.

One fixed preparation law per field is shared across the relevant cells.
Full hidden-state TV is not inferred from visible balance. Fixed
field-specific clocks and the stated independent clock mixtures preserve
the two-kernel argument; arbitrary correlated drift and finite ramps
remain separate. The physical reset waits are target-specific and do not
prepare arbitrary slow rival chains.

## 3. Statistics and the optional observation trade

The root and separate reviewers checked the full cost analysis. The test
fixes its reference and budgets before sampling. Four simultaneous
two-sided confidence events give the factor $8/\alpha$; separate validity
and power events require two sampling radii. Additional observation bias
is charged twice and existing preparation allowances are not charged
again. The sufficient endpoint totals, both reset waits and the exposure
sum were independently recomputed.

The nominal close comparator gives a separate information lower bound,
including adaptive selection among the four cells. Its expected-count
bound is real-valued; only a fixed integer budget is rounded upward to
174,900. The argument assumes independently prepared Bernoulli endpoints
and does not apply to arbitrary trajectory measurements.

The exact-tilt snapshot corollary was checked independently: opposite pulse
orders $0H,H0$, both starting from low-field equilibrium, recover all four
statistics from initial/final binary pairs. Stationarity identifies the
unweighted and Gibbs-weighted expectations. Weighted occupation variables
have range $1+u$, so maximum TV error over the two joint laws transfers to
occupation error with factor $1+u$, giving the $1/1000$ joint-TV gap.
Conditional starting coordinates also prove the three-state predictor's
exact initial/final joint-law match. This requires noninvasive observation;
the calibrated endpoint sample counts are not transferred to this variant.

## 4. Evidence and remaining limits

The exact verifier uses rational arithmetic and imported frozen exponential
enclosures at matrix dimension at most four. The independent numerical
replay retains both singleton fits and the rounded upper, checks full
generators and stationary laws, and runs no optimizer. Source/proof/report
bindings and completed regression are recorded in [Verification](VERIFICATION.md).

The source comparison attributes equilibrium reciprocity, Markov response
operators and preparation-based dimension witnesses. The added preparation
or initial-readout resource is explicit. The proof is substantially simpler
than the earlier seven-word invariant, and its selected deterministic gap
is tightly bracketed. Statistical efficiency, implementable preparation
and the closest-source comparison remain scientific priorities. This
checkpoint alone does not establish PRL readiness.
