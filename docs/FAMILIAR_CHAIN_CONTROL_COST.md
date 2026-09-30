# Equilibrium consistency costs predictive states

An equilibrium chain can have a smaller predictive Markov model whose
stationary dynamics circulate. Requiring the predictive model itself to
obey detailed balance makes that compression more expensive once the model
must respond to a local field. This is now a theorem for chains of arbitrary
length, with a sharp three-switch example.

The physical system is the familiar open heat-bath Ising chain. Only its
first switch is observed and controlled. Each experiment records that switch
at the beginning and end; all experiments share the same zero-field
equilibrium preparation. The model being tested must reuse one set of
states and one generator per field.

## The state-count comparison

For equal attempt rates, equal coupling $`t=\tanh J`$ with
$`0\lt t\le1/\sqrt5`$, and any chain length $`n\ge3`$:

| Required ideal endpoint-pair data | General Markov model | Ordinary reversible model |
| --- | ---: | ---: |
| All passive pairs | $`n+1`$ | $`n+1`$ |
| The three-field controlled menu below | $`n+1`$ | At least $`2n`$, at most $`2^n`$ |
| Three switches, $`t=1/3`$, three field tilts in $`[0,1/2]`$ | **4** | **6** |

The reversible comparison imposes the inherited equilibrium convention:
the field couples only to the measured binary switch, and the stationary
laws are Gibbs tilts of the common initial law. The general construction
obeys the same tilt and preparation; it relaxes detailed balance. Its
$`n+1`$ lower bound actually covers rivals without the equilibrium promises.

The [positive construction](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md) works
for **every finite nonnegative field protocol**, and all its exit rates
are at most $`13/12`$ in attempted-update time units, independently of chain
length. The coupling bound is sufficient for this construction, not an
optimal boundary. The [reversible lower bound](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md)
holds more broadly, for arbitrary positive couplings and attempt rates.
The [six-state construction](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
makes the three-switch comparison exact.

## A finite and robust test of reuse

Choose field tilts $`m_L=0\lt m_M\lt m_R\lt 1`$, where $`m=\tanh h`$, and any positive
clock $`\tau`$. Measure the endpoint pair for

```math
j^q\quad(j=L,M,R;\ 1\le q\le2n-2),
\qquad L^aM^b,\ R^aM^b\quad(1\le a,b\le n-1).
```

There are $`2(n-1)(n+2)`$ settings. Each uses at most two constant-field
segments and $`2n-2`$ ticks. For three switches, **20 settings of at most
four ticks** already determine the four-versus-six distinction when all
three tilts lie in $`[0,1/2]`$. No intermediate observation is requested.

The [proof gives an explicit positive TV radius](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md)
in terms of known finite basis coefficients and a target Gram eigenvalue.
Below that radius the same state-count bounds hold. There is no rival rate
cap or minimum equilibrium weight. The radius is conservative and has no
claim of being uniform in chain length, coupling, field spacing, or clock.
No useful experimental trial budget is inferred from its positivity.

## Why equilibrium adds states

The $`n`$ spin means close, so their evolution with the constant function
has dimension $`n+1`$. The positive model realizes those equations on an
explicit simplex of $`n+1`$ states. Its initial conditional means agree with
the physical chain, so every required binary endpoint-pair law agrees.

Detailed balance supplies more information. At each field, endpoint-pair
data determine inner products of reconstructed response coordinates.
Gibbs reweighting makes these inner products affine in $`m`$. Consistency
at three fields forces the reconstructed coordinates to be the same
functions on the rival state space. After conditioning on either visible
sign, their Gram matrix has rank $`n`$. Each sign therefore needs at least
$`n`$ hidden states. The argument covers larger, nonminimal rivals; it does
not assume that they already carry the physical spin coordinates.

The [passive birth–death construction](FAMILIAR_CHAIN_PASSIVE_REALIZATION.md)
shows why the control requirement matters. A reversible model with $`n+1`$
states already reproduces every passive pair. It cannot retain that state
count while reproducing the prescribed controlled pairs.

## Physical assumptions and contribution

The [source audit](FAMILIAR_CHAIN_SOURCE_AUDIT.md) separates the standard
heat-bath model, common Gibbs force coupling, chosen weak-coupling family,
and ideal endpoint observation task. The [equilibrium reduction derivation](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md)
explains when a fixed reduction inherits that force interface. An arbitrary
alternative actuator that couples to hidden states is outside this class.

Linear closure, positive-realization geometry, inverse Jacobi construction,
conditional rank bounds, and the quadratic-norm identity have established
precedents. The candidate contribution is their exact combination here:
an all-length controlled positive construction with bounded rates, a finite
and robust $`2n`$ reversible obstruction, and sharpness at three switches.
The focused comparison has not established literature priority conclusively.

State count is the number of distinct complete Markov states, including
persisting hidden memory. The proved ratio $`2n/(n+1)`$ approaches two; it
does not establish an extensive bit-memory saving, a Shannon-entropy gap,
an energetic advantage, or a hardware implementation. Full-path equivalence
and noisy-device feasibility remain separate questions.

## Remaining scientific decision

The mechanism now extends beyond the original coupled pair. The next
structural question is whether the reversible bound $`2n`$ is attainable
for general chain length, or whether a stronger obstruction appears.
A simple answer would clarify the physical scope more than another
parameter table. Manuscript drafting remains deferred.

[Exact verification](../reports/familiar_chain.json) ·
[Source comparison](FAMILIAR_CHAIN_SOURCE_AUDIT.md) ·
[Verification record](VERIFICATION.md)
