# Physical core: scope decision and internal review

24 September 2026. This is an internal research assessment, not external
validation or a manuscript. The owner's requirement is to inherit physical
assumptions from an established community model and derive the prediction
result within it.

## Decision

Lead with the [minimal four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md)
in the [published coupled-dot model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md).
For every finite positive coupling, field and pair of dwell times in its
equal-attempt specialization, four initial/final occupation-pair laws have
minimum stationary predictive state count three and minimum ordinary
reversible state count four. Both classes retain the same deterministic
binary readout and Gibbs force coupling. The rivals may prepare each word
arbitrarily. There is a positive, parameter-dependent TV interval with the
same minima; no uniform numerical radius over all parameters is claimed.

The [equilibrium reduction derivation](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md)
grounds the shared force interface: fixed readout-compatible reductions
inherit the microscopic Gibbs tilt. This is established equilibrium
algebra, not a new physical law. A free hidden-state fit with unrelated
field-dependent stationary laws is outside this comparison. The return
tables alone do not certify the common force relation.

The useful conclusion is a state-count cost of preserving equilibrium
structure in controlled prediction. Every minimal three-state fit in the
shared-force class must violate ordinary detailed balance at some held
field, although the four-state target satisfies it at each held field.
That does not assign dissipation to the target or implementation cost to
the predictor. Three versus four abstract states does not automatically
save a physical bit; both can use two fixed binary register bits.

## Checks and corrections

Separate internal reviews checked the explicit positive generator, full
stationarity, conditional initial moments, covariance gap and TV radius.
The three-state upper matches every initial/final pair law from low
equilibrium under finite nonnegative-field words. Intermediate observations
are not covered. The lower requires only reversible stochastic kernels,
so it also applies to continuous-time rivals.

The [exact verifier](../scripts/verify_switch_physical_core.py) checks
symbolic closure and stationarity independently in both dimensions, the
delicate rate factorizations, the covariance and radius algebra, charge
energy and compensated-gate identities, and rational reduction fixtures.
It binds reviewed proofs and the unchanged preparation-free certificate.
Finite fixtures supplement the universal proofs; they do not prove the
literature comparison or device performance. Its largest matrix is four
by four, without optimization, simulated data or floating arithmetic.

Two tempting overstatements were explicitly ruled out. A stochastic
encoder gives a reversible coarse kernel, but naive compression of a
generator can have a negative off-diagonal rate. Also, the explicit
predictor's high-field current vanishes at $\tanh H=1/3$; its zero-field
current is always positive. The theorem says at least one field must
violate ordinary detailed balance, not both. Both cases have exact checks.

The community model supplies ideal state-process observables and a
published pulse-limit convention. It supplies no experimental accuracy
for classification, gate compensation, finite ramps or measurement
disturbance. Previous kinetic, sampling and detector certificates remain
valid only within their original interfaces and parameter scopes.

## Novelty and the next research decision

The [primary-source comparison](FAMILIAR_SWITCH_CENTRAL_CLAIM_COMPARISON.md)
finds strong precedents for reciprocity, singleton inference, positive
realization, reversible reduction and artificial-irreversibility warnings.
The complete shared-control three-versus-four positive-realization theorem
is the candidate contribution. No priority claim follows from a bounded
source audit; the Falk full text remains an explicit access gap.

**PRL readiness remains unestablished.** The next substantive question is
whether the complete theorem expresses a useful general constraint on
equilibrium model reduction, beyond this exact benchmark. A concrete next
analysis should test whether an existing simultaneous reversible-realization
theorem already explains the state-count cost and identify a concrete
model-reduction decision that this obstruction changes. The existing
unequal-rate extension is supporting evidence to inspect, not an open
problem to rederive. A larger parameter table alone would not establish
significance. Complete the claim-to-theorem comparison and articulate the
modeling consequence before choosing a broader theorem or a narrower
publication scope. Further detector tuning and manuscript drafting remain
deferred.
