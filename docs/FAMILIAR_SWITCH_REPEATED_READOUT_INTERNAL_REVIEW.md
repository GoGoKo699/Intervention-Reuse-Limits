# Internal review of the repeated protected-readout construction

[Proof](FAMILIAR_SWITCH_REPEATED_READOUT.md) ·
[Readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) ·
[Serial score](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) ·
[Source audit](FAMILIAR_SWITCH_REPEATED_READOUT_SOURCE_AUDIT.md) ·
[Verifier](../scripts/verify_switch_repeated_readout.py) ·
[Report](../reports/switch_repeated_readout.json) ·
[Verification](VERIFICATION.md)

**24 September 2026.** A separate internal reviewer examined the complete
proof and final verifier, re-derived the central probability argument,
and independently replayed the certificate. The coordinator also reviewed
the proof and source. These are internal checks, not external peer review,
priority certification, a demonstrated instrument implementation, or a
publication-readiness assessment.

## The joint law is controlled without error–kick independence

The proof uses a fixed joint outcome/update kernel on each read,
conditional on all preceding information and the current hidden input.
This is stronger than a fixed marginal detector error rate. It ensures
that the successive error indicators have the product Bernoulli law even
when an error changes the hidden state during its own read. Sector
preservation makes all seven votes refer to the same true sign.

Nonselective stationarity then gives the postblock hidden marginal
$\pi D^7=\pi$. At each final hidden state, every incorrectly labeled
probability mass is matched by an equal deficit in its correctly labeled
cell relative to the ideal joint law. The resulting TV distance is
exactly the majority-error probability, not merely an upper bound.
This argument neither factorizes the majority from the hidden state nor
requires outcome-conditioned stationarity.

Preparation is charged once by applying stochastic contraction to the
entire initial block. Subsequent contraction requires a fixed future
channel depending on the included hidden state. The proof excludes
record-dependent active controls and retained detector/controller memory
that later feeds back into the system. It also retains the existing
independent final-electronics premise.

The boundary example with an outcome-correlated hidden reset satisfies
the new assumptions. Exact enumeration verifies that seven reads reduce
its joint error to the binomial tail while leaving a nonzero correlation
between majority error and hidden backaction. Thus the new statement
controls the relevant joint error without asserting that repeated
measurement has made the electronics independent.

## The calibration gate and score are combined unconditionally

Review checked the exact tails
$b_7(.02)=.0000053356544$ and
$b_7(.01)=.0000003416698$. The two-percent tail fits the old
$10^{-5}$ initial-instrument allowance, leaving
$.0000046643456$ for a quantified whole-block defect. The comparison
reference has identity initial electronics, which belongs to both
inherited detector classes. The majority is not itself assumed to be
an independent electronic channel.

First-pair disagreement has conditional mean $2p(1-p)$ for every
preparation, including preparation that depends on the preceding
trial history. At five million trials the $.03$ gate has null and
target Hoeffding exponents $846.4$ and $1040.4$. No independence
between trials or between the gate and score is used.

The null is split by its one fixed raw error rate. For $p\le.02$,
the retained pair lies in the inherited serial null class, and adding
a gate can only reduce rejection. For $p>.02$, the disagreement
gate alone bounds rejection. These alternative null cases are combined
by a maximum. Target miss probabilities are combined by a union bound.
The proof never conditions the score theorem on passing calibration.
The existing threshold, moment gates, five-million trial allocation,
and conditional preparation promises remain in force.

## The approximation allowance has a specified data interface

A central scope concern was resolved explicitly: the old $.0002$
null approximation allowance controls the retained majority/final-bit
pair only. It does not constrain disagreement of the first two raw
reads. The exact conditional disagreement law is a separate promise
of the enlarged protocol. Allowing arbitrary perturbations of the
raw transcript while controlling only the retained pair would invalidate
the high-error null argument; that enlargement is not admitted.

The imperfect-block extension supplies a different, explicit route.
A full-block comparison, including the raw transcript and final hidden
state, bounds calibration drift as well as the retained-pair error.
A stationary comparison gives calibration slack
$\epsilon_p+\eta$; a comparison uniform over input states gives
$\eta$. The reduced Hoeffding gaps are stated separately.
Under the remaining instrument margin, the conservative slack
$.00002$ retains exponents above $840$ and $1030$.

The stationary-defect extension was also checked. Its channels
$D_1,\ldots,D_m$ are explicitly fixed in advance, with the same
conditional nonselective kernel at each use given every prior history.
This qualification prevents substituting history-selected stationary
kernels into the telescoping argument. Their stationary defects add,
and sector leakage must be accumulated over the whole block. No extra
allowance is added after spending the existing instrument budget.

## Verification and remaining boundaries

The final verifier passed **158 exact checks** under pinned Python
3.13.5. A separate execution wrote a temporary report and reproduced
the canonical report byte for byte. The code uses exact rational
arithmetic, with no optimization and dense matrices of dimension at
most three. A review correction made every fixture-clock entry a
`Fraction` before division and added an explicit arithmetic-type check.

Checks cover the majority polynomial and its monotonicity, five- and
seven-read tails, the instrument margin, exact and slack-adjusted
calibration exponents, inherited serial budgets, the correlated-kick
fixture, two future-word contractions, a stationary-defect example,
and a common-mode error counterexample. The hash-bound written proof
carries the universal claims; finite fixtures do not prove them by
exhausting all instruments or rivals.

Reviewed snapshot hashes are:

| Artifact | SHA-256 |
| --- | --- |
| Proof | `4c9b6a873005f7a0798e99d3edededd7a39607d1c85252221b1e692af13d1182` |
| Verifier | `cc900a338ef0463206e9c0a2832008ed4a751c47de613850c4b88660a12c028f` |
| Canonical report | `488a3e39aca64284acc388a91fd38d479b14b727eec0fbf6b21772225391d086` |

A common-mode error reused across all votes produces zero disagreement
without reducing majority error. The gate therefore does not establish
temporal freshness, state-independent error rates, stationary protection,
or preparation. Their physical justification remains necessary.

The new acquisition costs **40 million physical binary reads**, plus
the associated controller memory, measurement time, barrier operation
and reset. The inherited general three-state construction concerns the
two retained pair laws. No general three-state upper or state-count
separation is asserted for the full eight-read transcript. This is a
conditional instrument and calibration result supporting the existing
score test. Device feasibility and PRL readiness remain open, and
manuscript drafting remains deferred.
