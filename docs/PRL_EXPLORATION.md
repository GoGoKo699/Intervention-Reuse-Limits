# PRL exploration: reusable prediction and time-reversal structure

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Source comparison](KINETIC_PARITY_SOURCE_AUDIT.md) · [Internal review](KINETIC_PARITY_INTERNAL_REVIEW.md) · [Verification](VERIFICATION.md)

**Research target, 23 September 2026.** The user selected *Physical Review Letters*. The present exploration is theory first, with bounded exact checks; manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about), checked on this date, emphasize a significant physical advance and impact beyond a narrow technical refinement. This record sets research priorities, not an acceptance prediction.

## 1. The current physical question

How does a reduced stochastic model's time-reversal structure affect the number of states it needs to predict interventions?

The targets are finite equilibrium systems with an exact two-state passive visible law. Interventions expose hidden structure. The latest comparison permits arbitrary rival barrier functions within a shared equilibrium interface, arbitrary new states and no target histogram promise. It distinguishes ordinary detailed balance, where time reversal fixes each retained configuration, from generalized reversal, which can exchange memory states.

The generalized class changes the conclusion materially. Its polynomial predictor has exactly zero stationary path entropy production under its specified reversal. Thus the preceding identity-reversal resource theorem must not be presented as a universal thermodynamic dissipation requirement. The limitation is a proved construction, not merely a missing proof route.

## 2. Completed advances in this continuation

| Result | What is established | Essential boundary |
|---|---|---|
| [General kinetic interface](GENERAL_KINETIC_INTERFACE.md) | The uncapped ordinary-reversibility lower extends to arbitrary barrier curves with shared equilibrium tilt and bounded queried rates. Two-field unrestricted growth is now polynomially matched. | Curves between the two queried fields are invisible to that task; on the original endpoint interval this is an exact reparameterization. |
| [General endpoint entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) | A common return lower bound and bounded injection density give an all-protocol, all-horizon comparison with hidden additive reversibilization. A general initial-density bound and a qualified distributed-reset extension are included. | Local balance is additionally needed for a fully reversible comparator; entropy uses ordinary reversal. |
| [Capped two-field separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) | At shared hidden exit cap $3k$, ordinary prediction cost is exponential while unrestricted cost is polynomial on the same two-field task. No rival kinetic formula, alphabet or histogram is prescribed. | The hub geometry, field-independent hidden generator, baseline rates, equilibrium tilt and preparation remain fixed. |
| [Generalized-reversal predictor](GENERALIZED_REVERSAL_PREDICTION.md) | Reversing an odd memory word and reading its middle symbol preserves the polynomial predictor's exact controlled response and supplies generalized detailed balance. | The involution is mathematically explicit; a natural physical implementation of that parity is not supplied. |
| [Combined resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | Ordinary and generalized reversal have different state-growth classes; the identity-reversal entropy frontier extends to the broader capped kinetic class. | Zero generalized entropy production coexists with positive identity-reversal entropy production. Neither is automatically driven heat. |

On the original nineteen-level targets, with hidden band $[k,3k]$, any fixed positive clock and the two fields $0,H$, the common-cap comparison is

$$
D_{\rm all}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm inv}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm id}(\delta)=\exp(\delta^{-\Theta(1)}).
$$

The exponents are not matched, and equality of growth classes does not assert equal minimum sizes. Every memory coordinate counts. Witness horizons are logarithmic in inverse error, but their constants and required accuracy can be severe; experiment count and sample complexity are not bounded.

Without a common rival rate cap, the same two-field class has polynomial unrestricted growth and ordinary necessity at least $\exp(\exp(c[\log(1/\delta)]^{1/5}))$. The stronger capped exponent must not be assigned to that uncapped class.

## 3. Why the proofs now differ

The capped lower uses squared Lagrange polynomials of the return-rate diagonal. These are exact selectors on the finite target grid and nonnegative diagonal operators on arbitrary rival values. The common cap makes $I+K/(3k)$ a positive Markov kernel. Their products recover exact target transports, with finite clock observations controlling all repair and entropy tests. The separate rank lower truncates only target-side clock polynomials, so it does not need a rival cap or reversibility.

The generalized upper changes the interpretation of retained memory. Stationary word probabilities of a reversible target obey word-reversal symmetry. An odd word's middle symbol is unchanged by reversal. Its stationary output process is an index shift of the usual endpoint-labeled word process, so their complete stationary actuator-path laws agree. That equality preserves the original controlled response, including the entry tilts and repeated hidden visits. No controller knows future applied fields, and no uncounted clock is introduced.

The broader entropy comparison instead uses the last common return to the visible state. This limits the duration over which different internal dynamics affect an endpoint. It needs neither the exponential barrier formula nor a hidden rate cap. Its state-budget consequences still depend on the separate ordinary-reversibility lower.

## 4. Prior work and physical interpretation

The [new source audit](KINETIC_PARITY_SOURCE_AUDIT.md) gives precise primary-source comparisons. Reversible higher-order processes and word-reversal fluxes are established in Bacallado; non-selfadjoint trajectory-reversible lifts appear in Diaconis–Miclo; odd-parity entropy accounting is addressed by Lee–Kwon–Park. These prevent claiming word reversal or the distinction between ordinary and generalized reversibility as new principles.

The claim under investigation is the combined quantitative controlled-prediction comparison: the same target, two-field observation task, counted state space, finite accuracy and common kinetic budget. The audit also separates standard local detailed balance and barrier freedom from this project's deliberately chosen hub geometry, unchanged hidden dynamics and preparation. Ten relevant papers do not make the entire chosen architecture a community convention.

For physically even retained configurations, ordinary detailed balance is the relevant reversal constraint and the identity-reversal state/entropy bounds apply. If a nontrivial physical reversal is available, the generalized construction prevents a universal heat-cost conclusion. A device-level interpretation would have to justify the actual parity and reservoirs. State count is not the stationary Shannon entropy, and stationary entropy production is not total entropy generated during an arbitrary driving protocol.

## 5. What to pursue next

1. **A recognizable physical model class or realization.** Seek conventional local dynamics or a concrete memory realization for which the relevant reversal parity is physically fixed. Show which part of the state advantage survives there.
2. **A small, certified finite-accuracy advantage.** Produce a stated tolerance and an explicit smaller predictor with a rigorous lower against all ordinary-reversible rivals. The present small checks illustrate identities; they do not establish that finite example. The smallest earlier lamp target has equal 38-state exact minima in the compared broad classes.
3. **Relax a substantive remaining interface assumption.** Field-dependent hidden generators, nonuniform baseline return rates or more general equilibrium weights require new arguments. Freedom at unqueried field values is not, by itself, operational generality.
4. **Sharpen the resource frontier where identity reversal is physically justified.** Its necessary inverse-polylogarithmic and sufficient logarithmic entropy-production budgets remain unmatched. Improving that gap is more consequential than only sharpening the uncapped fifth-root bookkeeping exponent.

These are research priorities, not permission gates. The current assessment is to continue the PRL-directed exploration with the parity boundary central. The mathematics is stronger and the thermodynamic claim is more sharply delimited; broad physical significance still needs a convincing model class or finite-accuracy instance.

## 6. Evidence and checkpoint history

All five new proof notes received separate internal mathematical audits. The [bounded verifier](../scripts/verify_kinetic_parity.py) and [saved report](../reports/kinetic_parity.json) cover finite word-reversal, kinetic-selector and entropy-bound identities; universal conclusions remain analytic. [Verification](VERIFICATION.md) records the completed local gate and separately identified remote CI. Internal audits and bounded source comparisons are not external peer review or priority certification.

The preceding published checkpoint is e38dde1171995892e8a34abc7100b6489ab393bd, with thirty-four verifiers. It established the original tight-band two-field lower and the identity-reversal entropy-production bridge. Its four proof snapshots, all earlier verifiers/reports and the license remain preserved. The present notes extend those results and supply the generalized-reversal boundary that the preceding assessment explicitly left open.

Manuscript drafting remains deferred.
