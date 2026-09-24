# What the smaller predictor can and cannot retain

Research assessment, 25 September 2026.

The useful conclusion is now more specific than a three-versus-four
example: **the minimum number of Markov states depends on the required
control range and temporal records, even when the linear mean dynamics
keep the same dimension.** The results below use the same published
coupled-dot model. They introduce no detector capability or new physical
component. They are exact model-selection results for ideal observations.

## One target, several prediction tasks

Let $t=\tanh J$ and $u=\tanh H$, with finite $J,H>0$.
The first four rows below use equal attempt rates. Every rival has a
fixed deterministic binary readout; further conditions differ by task.

| Required data | General Markov states | Ordinary reversible states | Essential comparison condition |
| --- | ---: | ---: | --- |
| Passive pairs at two lags $a,2a$; also all passive pairs | 3 | 3 | One kernel reused at the two times |
| Four controlled pairs $0,H,0H,H0$ | 3 | 4 | Common Gibbs force rule; arbitrary per-word preparation allowed |
| One passive triple $(S_0,S_a,S_{a+b})$ | 4 | 4 | Markov evolution through the counted middle state; arbitrary preparation allowed |
| Signed-control pairs over $\{0,\pm H\}$ | 3 below or at the threshold; 4 above | 4 | One common preparation and the 23-word menu below; force relation need not be assumed |

The [passive and three-time proof](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md)
supplies an explicit reversible three-state birth–death chain matching
all passive pairs. Yet a three-state binary chain has a singleton sign
sector. Given that middle sign, its past and future must be independent.
The target retains a strictly positive conditional covariance for both
signs, so one triple already requires four states. A positive TV margin
holds without a rival stationary-mass floor. If the three pair marginals
must remain exact, the optimal triple error for three states is exactly
half that conditional covariance.

This gives a concrete interpretation of the existing endpoint predictor:
it correctly propagates the requested pair statistics but cannot serve
as a three-state model after an additional ideal observation. The
observable span $\{1,S,Z\}$ closes under propagation, whereas conditioning
on a sign introduces the product $SZ$. Endpoint acquisition guarantees
do not automatically implement the nondisturbing middle observation.

## A sharp control-range boundary

The [signed-control theorem](FAMILIAR_SWITCH_SIGNED_CONTROL_BOUNDARY.md)
proves that a positive three-state predictor exists exactly when

$$
 \boxed{3t^2u^2+(1+t^2)u\le1.}
$$

Below or at that boundary, one generator family matches every endpoint
pair under all field protocols in $[-H,H]$. Above it, every three-state
continuous-time model fails, including nonreversible ones. The minimal
linear realization remains three-dimensional on both sides. Positivity
under the enlarged control range causes the extra state requirement.

The same decision can be established by **23 endpoint-pair experiments**,
each at most five ticks long, at any positive fixed clock:

$$
 \{H^k:1\le k\le5\}
 \cup\{H^i0H^j:0\le i,j\le2\}
 \cup\{H^i(-H)H^j:0\le i,j\le2\}.
$$

All words share one initial preparation. An exact three-state fit is
forced to have a positive low-field equilibrium law and the common
stationary Gibbs tilt, even if neither was assumed. This richer data
requirement differs from the original four-word theorem's freedom to
prepare each word separately. The finite-menu state counts persist on
a positive parameter-dependent TV interval, whose numerical size has
not been calculated. No optimum experiment count is claimed.

The theorem also covers unequal attempt rates. With
$r=\Gamma_Z/\Gamma_S>0$, its criterion becomes

$$
 \boxed{(r+2)t^2u^2+(1+t^2)u\le r.}
$$

At the previous operating point $t=4/5,u=3/5$, equal attempts violate
the signed criterion. The general minimum is four there, although the
nonnegative-field endpoint task admits three. For the same signed field
range, the minimum returns to three when $r\ge903/481$. These are exact
reduced-model thresholds, not measured gate or tunneling tolerances.

## Scientific assessment

The results change a model-selection decision: choose the state budget
after specifying the control range, required temporal records and
equilibrium structure. A compact endpoint simulator can be exact for its
intended task and fail for a modest extension of that task. The failure
has a mathematical certificate, rather than only an unsuccessful fit.

The [source audit](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md) identifies
established shared-realization, invariant-cone and hidden-state
factorization methods. The candidate contribution is the explicit
control-range criterion and the complete task-dependent state comparison
in a familiar physical model. It is not a new general realization method.
The audit also corrects an earlier normalization description of the
Taghavian–Sjölund comparison; the complete-theorem distinction survives.

This is a stronger and more informative theory result than the isolated
state-count example. It still does not establish PRL-level significance,
hardware-bit savings, heat cost or a physical implementation of the
circulating predictor. The next research decision is whether this exact
criterion expresses a useful principle for a broader established kinetic
family. The current model supplies a completed benchmark for that question.
Manuscript drafting and detector tuning remain deferred.

[Exact checks](../reports/switch_control_scope.json) ·
[Verification](VERIFICATION.md) ·
[Community model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md).
