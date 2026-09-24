# Internal review of the four-word preparation-free construction

[Return test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) ·
[Four-word realization](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md) ·
[Repeated-readout extension](FAMILIAR_SWITCH_PREPARATION_FREE_READOUT.md) ·
[Verifier](../scripts/verify_switch_preparation_free.py) ·
[Report](../reports/switch_preparation_free.json) ·
[Verification](VERIFICATION.md)

**24 September 2026.** A separate internal reviewer read the three proof
notes, independently derived the singleton identity and conditional
covariance formula, checked the four-table realization argument, and
audited the stopped sampling and noisy-selection proofs. The coordinator
also read all three notes. A second internal reviewer independently
confirmed the noisy first-$n$ selection comparison and oracle completion
argument. These are internal mathematical checks, not external peer
review, a priority determination, or evidence of an implemented device.

## The singleton removes the rival preparation premise

For a singleton sign $s$, a faithful initial sign fixes the actual
starting state. Any sign-preserving initial kick acts trivially on that
state. This remains true if preparation depends on the scheduled word,
every previous observation, or the hidden-state history. No stationary
preparation, common preparation, balance, or lower bound on a relaxation
rate is used.

Review derived the return identity by separating the self-transition
term in the two opposite-order matrix products. Every path through the
other visible sector has the same detailed-balance ratio
$(1+su)/(1-su)$. The self-transition term is the product of the two
single-word return probabilities. Clearing the denominator gives

$$
 (1-su)r_{0H,s}-(1+su)r_{H0,s}+2su r_{0,s}r_{H,s}=0.
$$

With at most three states and two nonempty visible sectors, at least
one sector is a singleton. A model that never produces one sign cannot
complete the sampling quotas and is not rejected. This addresses rare
or absent initial signs without a rival preparation assumption.

Strictly positive stationary laws must remain explicit. Detailed balance
against a law with zero mass on transient states can impose no useful
constraint inside their transient block. Removing the stationary balance
promise does not permit dropping stationary support. No quantitative
lower stationary-mass bound is needed for the exact force relation used
here.

The claimed improvement bypasses certification of rival preparation; it
does not show that an arbitrary rival has equilibrated. The target still
has its stated preparation and execution contract.

## Target covariance and the full four-table upper

The reviewer independently recovered

$$
 R_s=-\frac{su}{2}\operatorname{Cov}_{\pi}
       (K_0S,K_HS\mid S=s).
$$

Thus the four-word construction uses the existing within-sector
covariance mechanism. Its new strength is a necessary singleton identity
that does not require equilibrium preparation of the competing model.
For the equal-attempt target the two residuals have opposite signs and
equal magnitude, as stated in the return-test note. The stronger uniform
$9/1000$ kinetic margins require the new exact polynomial certificate;
the covariance identity alone is not their numerical verification.

The four-table upper does not assume that the one-percent kinetic
perturbations preserve the original heat-bath moment closure. Low and
high stationarity with the common tilt imply

$$
 a=1-m/u,\qquad x=(\ell+ud)/u.
$$

These determine the complete single-$H$ and single-$0$ pair laws from
the original four moments. The existing positive three-state
continuous-time realization fits those moments and has the required
stationary laws, so it fits both added pair laws as well. This is one
shared realization per target model, not a new model for each word.
The argument introduces no additional generator or positivity domain.

For the target, a sign-preserving initial channel that also preserves
$\pi$ preserves each stationary sign-conditioned sublaw. Consequently
its true initial-label/postmeasurement joint law is unchanged. The
ordinary singleton lower only requires sign preservation; the
stationarity requirement belongs to the target upper.

Review checked the conditional-TV conversion
$|\widehat r-r|\le\delta/(1/2-\delta)$ by using the centered event
function $\mathbf1_A-r\mathbf1_B$. Its oscillation is at most one.
The return polynomial is $22/5$-Lipschitz on the probability cube.
At $\delta=1/1000$ the possible residual displacement is
$22/2495<9/1000$. These facts justify the four-table state-count
interval once the certified kinetic residual margins are supplied.
They do not establish a trajectory-level state minimum.

## Fixed quotas do not assume conditional independence after selection

The acquisition has a deterministic word schedule and a fixed trial
cap. Each word/sign group retains at most its first $n$ outcomes, with
retention decided from the initial sign and previous counts before the
current final outcome. Failure to fill a group causes nonrejection.

For a null singleton, every accepted endpoint has the same conditional
Bernoulli return mean, regardless of previous preparation. The linear
part of the polynomial error is a sum of conditionally centered
increments. Each retained increment has width equal to its fixed
coefficient divided by $n$; the quota caps bound the total squared
widths by $(28/5)/n$. The conditional exponential bound therefore
controls the event of completion and a large deviation. It never
conditions the law on having completed the quotas.

The remaining product error is exactly $2su\Delta_0\Delta_H$.
Bounding the two single-word errors by $.01$ makes its magnitude at
most $.00012$. A fixed model needs only one chosen singleton sign for
the size proof; there is no union over possible singleton orientations.

The target TV allowance $B=79/10^6$ must be converted after conditioning:
its conditional-return allowance is $B/(1/2-B)=79/499921$, rather than
$B$. The test pays this predictable drift, both signed score failures,
and incomplete target quotas. The target's history-dependent execution
contract is used for power; it is not imposed on its rivals.

## Noisy labels are controlled by list stability

Seven protected readings refer to one true sign throughout each block.
Conditional freshness gives the binomial majority-error probability
even when an error is correlated with its own hidden kick. The error
probability must be fixed conditional on every pre-use hidden state and
history. Unconditional error marginals and a passed disagreement gate
do not establish this condition.

For a fixed word/sign group, changing $E_i$ initial labels changes at
most $E_i$ members of its ordered first-$n$ selection. The two lists
may have symmetric difference as large as $2E_i$, but those entries
pair into at most $E_i$ replacements, each changing the sum by at most
one. Final majority errors cost at most another $E_f$. Thus the mean
difference is bounded by $(E_i+E_f)/n$, with no independence from the
outcomes being estimated.

If the true-sign list is incomplete while the observed list completes,
append independent reference Bernoulli values to the true list after
the cap. At most $E_i$ such positions are needed, and the same
replacement bound remains valid. These artificial values are used only
on an enlarged proof probability space. They neither extend acquisition
nor condition its distribution on completion.

The padded true lists have the same fixed-quota concentration bound.
For the target, its oracle filtration first reveals the true initial
sign for retention and then integrates over the current readout block
and field evolution. The current error transcript is revealed with the
completed trial. All earlier raw transcripts remain in the past. This
ordering is necessary: conditioning the target response on the current
error transcript could bias its hidden kick and invalidate the target's
nonselective response bound.

The instrument is therefore a fixed joint error/update operation with
no current-record feedback into subsequent readout operations or active
control. Merely selecting adaptively among equilibrium-preserving
nonselective kernels would not justify equilibrium preservation of the
whole block. The null needs sign protection; the target initial block
also needs the stated nonselective equilibrium preservation. Final-block
equilibrium preservation is unnecessary because its true sign is fixed
and its disturbance follows the scored field evolution.

With at most 50 majority errors per word/stage, the four conditional
means each move by at most $10^{-4}$ and their residual moves by at
most $.00044$. Review checked this displacement and the remaining null
and target concentration margins. The count-failure event is union
bounded separately. Large-error and small-error null cases are
alternatives combined by a maximum; target score, quota, error-count,
and disagreement-gate failures are combined by a union bound. No gate
is used to condition a score distribution.

## Boundaries and verification status

All three notes retain one fixed pair of field kernels and an exact
shared Gibbs tilt with $u=3/5$. They do not import an earlier approximate
force-law allowance, an approximate ordinary-null prediction allowance,
or a sign-changing instrument allowance. An explicit additional analysis
would be needed for each such enlargement. The repeated-readout theorem
has 126 million raw readings, with their durations and other apparatus
costs kept separate from the target's stated attempt-time budget.

The three-state upper concerns the four specified initial/final pair
laws. An exact three-state realization of the fourteen-reading
transcript, its calibration records, or intertrial correlations has not
been proved. The new sufficient trial allocation is not claimed to be
optimal. Source priority and the physical precedent comparison are
separate work; this review does not certify either.

The final verifier passes **209 exact checks** under pinned Python 3.13.5:
182 direct checks and 27 recomputed perturbation checks from the frozen
percent-kinetics helper. The coordinator read the complete final source.
The largest dense matrix has dimension four, with exact rational and sparse
polynomial arithmetic; no optimizer, floating arithmetic or large simulation
is used. All three new proofs and 26 inherited proof snapshots are bound.
The finite checks support the written universal arguments, rather than
enumerating all rivals, preparations or measurement histories.

| Artifact | SHA-256 |
| --- | --- |
| Return-test proof | `42530472f40412d9e1f93d868a4df1dd2d833ba34ee89f8531df1cb1679dec0a` |
| Four-table realization proof | `311ddad97cfec6ab09a733565e5655532a4449f2b1ff4c33a37516565ed592fa` |
| Repeated-readout proof | `eb35e4b689e6a06573eea0fa12e91e19a41c08c23ec14bf0d5262c0b1846a5b9` |
| Verifier | `cbd3a0cf4a1617f1c85653e6b5e2bbfd82687a4df202bec925dbcdc7da4da356` |
| Canonical report | `dc10d2baf22899ef663faa4406d720998771e7c40c4de7ef4e8a7b2a3bed3df1` |

The independent production replay and full regression status are recorded in
[Verification](VERIFICATION.md). Manuscript drafting remains deferred.
