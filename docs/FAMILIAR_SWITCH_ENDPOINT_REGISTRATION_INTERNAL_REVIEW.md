# Internal review of endpoint registration and relative force tolerance

This is an internal analytic review of
[endpoint registration](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md) and
[relative force robustness](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md).
It is not independent external review, a device-validation report, or a
publication-novelty certification. The earlier preparation-free proof,
fixed-quota sampling argument, and exact four-pair realization were used
as explicit prerequisites.

The reviewed extension replaces the repeated-readout detector contract
with a known uniform conditional endpoint-error bound. It also replaces
exact stationary force coupling by a relative likelihood-ratio spread.
Those changes retain a conditional statistical theorem, with their new
premises stated separately from device performance.

## 1. Moving the oracle signs removes the initial-instrument restriction

The initial true sign is evaluated after the entire initial acquisition,
at the start of the active word. The final true sign is evaluated at the
end of that word, before final acquisition. These placements are essential.
Initial measurement may change the readout sign, because the null permits
an arbitrary actual word-starting state. A singleton postmeasurement
sign still fixes that state exactly.

The four active kernels must remain the same conditional on the joint
past and the actual word-starting state. A detector or controller variable
that changes subsequent active transition laws is part of the counted
model state. It cannot be hidden outside the model by calling it
measurement backaction. Previous records may still influence the next
preparation, as permitted by the null. Current records do not change the
prescribed active word.

Barrier closure, release and dead time are included at the appropriate
acquisition boundaries. An initial label for a state before an unbudgeted
release-induced jump would not identify the specified word-start sign.
Likewise the final label must estimate the state before any final-window
disturbance, rather than only a later detector-held state.

## 2. The conditional error bound uses the full previous joint past

The error-count argument needs a filtration in which previous true
endpoint signs and error indicators are measurable. Review identified
this point in the first draft; the definition now explicitly includes
the previous joint system/detector history, latent endpoint signs,
errors, model states and acquired records. A bound conditional only on
observed records would be insufficient.

For example, a single hidden common error bit can flip every fresh fair
true bit while remaining invisible in the distribution of the recorded
bits. Each observed-history error marginal can remain small, although
all errors occur together. The required full-history conditional bound
excludes that situation after previous true errors enter the analysis
filtration. A physical bound uniform over the acquisition-start history
and current hidden input state supplies the stated pretrial bounds by
the tower property.

Neither a fixed error probability nor independence between endpoint
errors is required. The contract bounds each conditional error
probability by $p_*=5\times10^{-6}$; this is enough for the error-count
moment-generating-function inequality. The contract is an interface
premise, not an inference from the scored data.

## 3. Error counts and fixed-size list stability

For each of four words and two acquisition stages, there are
$M=2{,}250{,}000$ error opportunities. Their mean upper bound is
$Mp_*=11.25$. At exponential parameter $\log4$, the iteration gives

$$
 \Pr(E>50)<\frac{3^{34}}{4^{50}},\qquad
 \epsilon_E=8\frac{3^{34}}{4^{50}}<2\times10^{-13}.
$$

This calculation uses conditional probabilities and a union bound;
it does not assume independence between the eight counts.

Changing $E_i$ initial labels changes at most $E_i$ members of the
ordered first-$n$ selection, with removed and inserted records paired
as replacements. Each replacement changes a binary average by at most
$1/n$. On records selected in common, at most $E_f$ final label errors
change the return values. With $n=10^6$, the good count event therefore
gives mean displacement at most $(50+50)/n=10^{-4}$ and residual
displacement at most $(22/5)10^{-4}=.00044$.

This is a deterministic list comparison and permits error/outcome
correlation. An incomplete true-sign list may be padded after the fixed
cap with reference Bernoulli draws on an enlarged proof probability
space. At most the same number of replacements is required. No extra
acquisition or conditioning on completion is used. If only one true
sign exists, the other recorded group cannot complete on the good count
event; that case has rejection probability at most $\epsilon_E$.

## 4. The oracle concentration filtration remains valid

Within a current trial the oracle first reveals the true post-acquisition
initial sign and uses it for retention. It delays revelation of the
current acquisition transcript and label until the trial is complete.
All previous joint information remains in the past. This is compatible
with the chronological physical process: it is a coarser analysis
filtration, not conditioning away physical backaction.

For a singleton null, the true sign fixes the active starting state and
therefore its fixed conditional return mean. For the target, the
history-conditional oracle pair-law promise gives return displacement
$b=B/(1/2-B)=79/499921$. Conditioning separately on a current meter
record correlated with its hidden update could invalidate this target
bound; the proof does not do so.

Padded records have the reference return means. The fixed-quota
concentration argument therefore retains squared linear coefficient
sum at most $28/5$, target predictable drift at most $(22/5)b$, and
quadratic remainder $.00012$ outside its stated concentration event.
The analysis does not condition on error-count success or quota
completion. Those failure events are paid separately.

The resulting linear margins are $.00344$ for an exact-force singleton,
$.00304$ for a singleton with residual ceiling $.0004$, and
$46801231/12498025000$ for the target. These give the stated size bounds
below $.015$ and $.04$, and target miss below $.014$. The target observed
sign-probability floor is $1/2-B-p_*=.499916$, which supplies the quota
bound without symmetry of the detector errors.

## 5. Target power needs only the postmeasurement marginal promise

Let $\pi$ be the actual low-field target equilibrium and $D$ the whole
initial acquisition channel with its record discarded. The contraction
bound

$$
 \operatorname{TV}(\nu D,\pi)
 \le\operatorname{TV}(\nu,\pi)
       +\operatorname{TV}(\pi D,\pi)
$$

is sufficient because the oracle label is the deterministic sign of the
postmeasurement state itself. No joint law of a premeasurement label
and the postmeasurement state is being substituted into that argument.
The prior $79\times10^{-6}$ oracle pair allowance is retained by
paying preparation and marginal instrument defect separately, with the
actual-to-reference field and timing changes charged once.

If the acquisition channel depends on history, the marginal promise
must hold for the entire resulting channel at each history. Adaptive
selection among suboperations that individually preserve equilibrium
does not establish preservation by their complete feedback operation.
The revised proof states this boundary explicitly.

Symmetric changes to both directional rates on each target edge give
a concrete nonselective stationary acquisition model. A prescribed
time-dependent family of such generators also preserves the same law.
Positive, sufficiently suppressed sign-changing rates permit finite
leakage rather than demanding exact sign protection. This construction
shows consistency of the conditional model; it does not establish a
physical device's barrier, energy or detector specifications.

## 6. The integrating-meter tail does not condition on no jumps

The continuous meter noise must be a martingale in the joint
system/detector filtration. The predictable drift has signed margin
$g>0$, the conditional quadratic variation is bounded by $vT$ with
$v>0$, and the full acquisition has sign-change probability at most
$\Lambda$. The reference sign at integration start is known in the
mathematical initial filtration.

On a path with no sign change, a misclassification requires a signed
martingale excursion of at least $gT$. Its exponential bound is
$e^{-g^2T/(2v)}$. The error event is contained in the union of this
excursion and a sign-changing event; hence each endpoint error is at
most $\Lambda+e^{-g^2T/(2v)}$. No noise law is conditioned on absence
of a jump. This is the step that allows noise/backaction correlation.

The integration duration $T$ and full acquisition duration $\tau$ are
distinct. A constant sector-changing hazard gives $\Lambda\le\kappa\tau$,
including switching and dead time; using $\kappa T$ alone requires
$\tau=T$ or a separate accounting of other exposure. With
$T=32v/g^2$ and $\Lambda\le4\times10^{-6}$, the sufficient endpoint
error is $4\times10^{-6}+e^{-16}<5\times10^{-6}$.

Continuity of the martingale matters. A variance bound for unrestricted
jump noise does not give the same Gaussian exponential tail. Neither
colored noise, a fitted histogram nor accurate observed labels alone
establish the required joint-filtration, leakage or marginal-stationarity
promises.

## 7. Relative force spread and the rare-state boundary

For the stationary likelihood factor $w$, the condition is the spread
$\max w/\min w\le L$, not a separate per-state error bound silently
reinterpreted as the same cross-state ratio. Detailed balance gives
nonnegative weighted cross-return sums $U,V$ with
$V/L\le U\le LV$. Therefore

$$
 |U-V|\le(L-1)\min(U,V)
 \le(1-u)(L-1).
$$

At $u=3/5$ and $L=1001/1000$, this is the ceiling $.0004$.
The argument requires positive stationary support but no mass floor,
mixing rate, balanced law or equilibrium preparation. The exact target
and its three-state predictor remain inside the enlarged force class.

For population pair error $\delta=.0009$, conditional return error is
at most $9/4991$. Adding the force ceiling and the residual Lipschitz
charge gives
$1/2500+198/24955<.009$. The ideal four-pair state minima therefore
remain three and four on the stated interval.

Review suggested and checked the finite-rate version of the rare-state
counterexample. Its reversible two-state block has diagonal $3/4$
and off-diagonal $1/4$, generated in unit time by equal rates
$(\log2)/2$. Single-word returns are $3/4$, two-word returns are
$5/8$, and the residuals are $-3/40,+3/40$, while the unweighted
stationary force-law TV error tends to zero.

Adding $\varepsilon(\Pi_\varepsilon-I)$ to that generator makes every
off-diagonal rate positive while preserving detailed balance. Since
$C\Pi_\varepsilon=\Pi_\varepsilon C=0$, the unit-time kernel is
$e^{-\varepsilon}P+(1-e^{-\varepsilon})\Pi_\varepsilon$ and approaches
the same counterexample. The failure of absolute stationary TV thus
persists for irreducible finite continuous-time models; it is not an
artifact of a nonembeddable projection kernel.

## 8. Scope, source comparison and remaining verification record

The endpoint theorem uses 18 million measurement windows and binary
decisions. It does not count only 18 million analog samples. Integration,
barrier transitions, meter reset and dead time remain resources, with
their errors included in the stated acquisition budgets.

The per-trial coupling bound $B+2p_*=.000089$ supplies an approximation
by the existing fixed three-state predictor of the ideal reference
pair laws. It does not prove state minima for the complete recorded
history-dependent process, nor a three-state realization of an analog
trace or arbitrary detector-memory correlations. The state-count theorem
continues to concern the four specified ideal pair laws.

The accompanying source audit distinguishes component precedents from
the complete proposed experiment. It does not combine performance
numbers from separate devices into an achieved specification. This
review checked that scope boundary; it does not independently certify
every literature attribution or resolve complete-theorem novelty.

The coordinator inspected the complete final verifier source and both proof
snapshots. The canonical verifier passes **104 exact checks** under pinned
Python 3.13.5, with largest dense matrix dimension four, no floating arithmetic
and no optimization. It binds 31 written proof snapshots. The written proofs
carry the universal conditional statements; finite fixtures do not exhaust
all detectors, model histories or rival generators.

| Artifact | SHA-256 |
| --- | --- |
| Endpoint-registration proof | `41df45ab86d3a005d9dd32497a7329f711bb433a7fe686ae6ee84b931bf615c9` |
| Relative-force proof | `99464fb83b33748c29859f27bbef53b5b8fd7b078b60559978b5bb9d64d087ea` |
| Verifier | `9b690e1ac4766de787ed4943f17359a2a13f06476c145f19fde98fdba20a305b` |
| Canonical report | `bf8f3924d62609cad8235db49743bf6e476ac2873ff644e1976ce0512e989977` |

The independent production replay, complete regression and publication status
are recorded in [Verification](VERIFICATION.md). These are internal execution
checks, not external peer review or a priority determination. No unresolved
analytic blocker remains after the filtration and acquisition-boundary
clarifications above. Manuscript drafting remains deferred.
