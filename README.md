# Intervention Reuse Limits

**What must a model remember when its predictions must survive interventions?**

This project asks how many states one stochastic predictor needs across changing controls. Our current small example is familiar: **two coupled conformational switches**, represented by time-even Ising variables with heat-bath dynamics.

Their four equilibrium configurations admit an exact **three-state stationary predictor** for the controlled mean of one switch. Every **ordinary-reversible predictor needs four states**, under the same Gibbs control tilt. The new experiment uses **four endpoint measurements**, each after at most two pulses, with access to equilibrium preparation at either field.

The mechanism is a conditional covariance. A hidden conformation changes the response to both pulses, even after fixing the visible conformation. Detailed balance makes that covariance measurable by reversing pulse order. It is nonzero in both visible sectors, so each sector needs at least two states. A stationary predictor with circulation can reproduce the same means with three states.

The [four-endpoint theorem](docs/FAMILIAR_SWITCH_PREPARATION_WITNESS.md) gives the direct quadratic identity. Write the four means as $m,a,b,\ell$, with the preparation included in each experiment:

| Mean | Equilibrium preparation | Active field sequence |
|---|---|---|
| $m$ | $0$ | $H$ |
| $a$ | $H$ | $0$ |
| $b$ | $H$ | $0,H$ |
| $\ell$ | $0$ | $H,0$ |

Every ordinary model with at most three states obeys one of
$b-m-a+\ell\pm(u\ell-am)=0$, where $u=\tanh H$. The coupled pair violates both. This necessity has no rival rate cap and also covers arbitrary reversible stochastic tick kernels. One fixed model must explain all four cells; the two preparations have Gibbs-related stationary laws. The result is not an unconstrained preparation-and-measurement dimension test.

**The observable gap is tightly bracketed.** At $J=H=\log3$ and tick $3/2$, the best ordinary three-state maximum occupation error lies strictly between $9/5000$ and $1/550$: **0.18 to 0.181819 percentage points**, a ratio below $100/99$. The lower holds for the whole rival class; the upper comes from one certified feasible model. Three general stationary states remain exact. The longest active experiment lasts three attempt-time units. This is a new two-preparation task; the [seven-word result](docs/FAMILIAR_SWITCH_FINITE_MARGIN.md) retains its single-preparation scope.

**Calibration is included.** Simultaneous full-state preparation TV errors, fixed field errors and fixed per-field tick errors of $10^{-5}$ preserve an actual occupation gap greater than $1/625$: **0.16 percentage points**. The rival class permits stationary low-field bias and relative tilt-parameter uncertainty $10^{-4}$ and a high-field stationary-law TV discrepancy $10^{-5}$. Each model has one fixed preparation law per field, shared across that field's cells. The state minima remain three versus four for $10^{-5}\le\delta_P\le1/625$. These sufficient budgets do not cover arbitrary correlated drift or finite ramps.

The [measurement-cost analysis](docs/FAMILIAR_SWITCH_PREPARATION_COST.md) gives conservative totals at 5% false-positive and false-negative probabilities: **15,859,920 endpoints** for calibrated exact-null rejection, or **18,045,064** to exclude ordinary approximation within $10^{-4}$. A separate ideal-case information bound requires at least **174,900 endpoints** for a fixed-budget test. Sufficient and necessary counts remain far apart. Target-specific preparation waits of 62 and 36 attempt-time units suffice at the low and high fields; they do not prepare every arbitrarily slow rival. Full hidden-state preparation cannot be certified from the visible balance alone.

The [exact verifier](scripts/verify_switch_preparation_witness.py), [report](reports/switch_preparation_witness.json), [source comparison](docs/FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_PREPARATION_INTERNAL_REVIEW.md) separate analytic proof, essential rational certification and statistical assumptions. The [saved-model replay](reports/switch_preparation_screen.json) is diagnostic evidence and runs without optimization. An optional variant needs only the opposite pulse orders $0H,H0$ from low-field equilibrium, with noninvasive initial and final readouts. It certifies a $1/1000$ joint-law TV gap under exact preparation and tilt; its observation model, calibration and sampling cost are separate from the endpoint figures above.

The research target is **Physical Review Letters**; manuscript drafting remains the last step. The [current exploration](docs/PRL_EXPLORATION.md), [research dossier](docs/RESEARCH_DOSSIER.md), and [claim ledger](docs/CLAIM_LEDGER.md) retain the assumptions and unresolved questions. The four-endpoint result concerns means; it does not assert complete controlled path-law equality, an implementation-independent heat cost, or PRL readiness. Earlier constructions below address different target families and interfaces.

## Earlier general principle: one state, two roles

The [matrix prediction principle](docs/MATRIX_RANK_PREDICTION_PRINCIPLE.md) starts with a nonnegative, completely positive matrix $H$ of size $n$, normalized so its entries sum to one and every row has positive sum. Its two relevant ranks count the fewest pieces in

$$
H=\sum_{s=1}^{r_+}u_sw_s^{\mathsf T},\qquad
H=\sum_{s=1}^{r_{\rm cp}}c_sc_s^{\mathsf T},
\qquad u_s,w_s,c_s\ge0.
$$

The first permits different entry and exit profiles. The second uses the same profile on both sides. For the controlled task constructed from $H$, the minimum total state counts are

$$
\boxed{D_{\rm all}(0)=1+n+r_+,\qquad
D_{\rm ord}(0)=1+n+r_{\rm cp}.}
$$

Here the single visible state and all hidden memory and probe states are counted. The target is ordinarily reversible, has hidden relaxation band $[k,3k]$ and hidden exit cap $2k$, and has an exact two-state passive binary path law.

The experiment has one binary readout, one fixed preparation, two field values and a positive control clock. Probe labels specify different kinetic rates; they are not extra observed colors. Rivals may introduce arbitrary new states, stationary masses and endpoint barriers in $[0,1]$, subject to the shared hidden exit cap $2k$. The lower bounds apply to this entire comparison class, beyond the displayed factorization constructions.

The sufficient predictors have a direct interpretation. A memory state chooses a distribution over the next probe. Every factorization maps stochastically to the same endpoint predictor, preserving the complete controlled binary-output path law. Ordinary detailed balance requires matching entry and exit flux profiles. Matched positive tests with reversed operator order then turn that requirement into a nonnegative Gram factorization, which supplies the lower bound.

For each fixed $H$, both counts persist over some positive accuracy interval and can be witnessed by finitely many clock experiments. The theorem does not give a useful uniform size for that interval. The number of kinetic labels grows with $n$.

The [source comparison](docs/SIMPLE_PREDICTION_SOURCE_AUDIT.md) separates established nonnegative factorization, stochastic intertwining and reversible realization ideas from this controlled prediction statement. The [internal review](docs/SIMPLE_PREDICTION_INTERNAL_REVIEW.md) records the proof checks.

## What the twelve-state example establishes

The [small incidence target](docs/FINITE_REVERSIBILITY_ADVANTAGE.md) stores an edge of a five-vertex graph. Its exact eleven-state stationary predictor stores a preselected endpoint. The relevant matrix has nonnegative rank five and completely positive rank six, giving exact minima of eleven and twelve total states through the general principle.

Positive-error results must be read at their stated precision. All entries below concern this same target, binary means, two fields $0,\log2$, shared interface and hidden exit cap $2k$.

| Certified statement | Accuracy and experiment scope |
|---|---|
| **Unrestricted minimum: 11** | $\delta\le2^{-1360}$ on the full clock task; words through 520 ticks already suffice for the lower. |
| **Ordinary-reversible minimum: 12** | $\delta\le2^{-220}$; an explicit list of 12,766 mean experiments, each at most 66 ticks, suffices. |
| **9 ordinary-reversible states suffice** | Error at most $1/2376$, uniformly over every two-field switching protocol and every horizon. |
| **2 ordinary-reversible states suffice** | Error at most $557/51920<0.01073$, with the same uniform protocol and horizon scope. |

The first row is the [minimum-count theorem](docs/FINITE_PREDICTOR_MINIMALITY.md). The second uses [bounded rational observation recovery](docs/BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md): an exact rational, computer-assisted certificate supplies an essential basis-conditioning bound, and the transfer to arbitrary reversible rivals is analytic. The remaining rows follow from [symmetry averaging](docs/SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) and [kinetic variance](docs/KINETIC_VARIANCE_COMPRESSION.md).

The eleven-state predictor is sufficient at every accuracy because its controlled predictions are exact. Its unrestricted minimality is not proved throughout the larger $2^{-220}$ interval or on the smaller experiment list. The numerical lower tolerance remains impractical, and these bounds leave a wide unresolved accuracy range. Neither upper bound is claimed optimal. An eleven-state generalized-reversible realization is not established.

## Heterogeneity both excites and reads hidden memory

The [variance theorem](docs/KINETIC_VARIANCE_COMPRESSION.md) gives the complementary physical explanation. Write $b_i(h)$ for hidden return rates in units of $k$, and let $c_i(h)=b_i(h)-\sum_j\mu_jb_j(h)$. This centered heterogeneity appears twice: it creates deviations from the stationary hidden distribution, and it couples those deviations back into the visible signal.

Eliminating the hidden density gives an exact memory kernel with one factor of $c$ at each end. Consequently the error of a two-state predictor using the averaged return rate is bounded by a constant times $\sup_h\operatorname{Var}_\mu b(h)$. Faster hidden mixing reduces that bound. If the return rates are identical at each field, the two-state reduction is exact.

This is a finite-amplitude, all-horizon statement. It allows stationary nonreversible hidden dynamics and needs no microscopic state-count or minimum-mass factor. A conditional-variance version also explains the nine-state symmetry quotient. Averaged barrier curves belong to the broad kinetic interface class; on two queried fields they can be implemented by one exponential curve with matching endpoints. Interval-wide exponential matching is a separate requirement.

## The larger separation and the reversal convention

On a different, nineteen-level target family, the [resource theorem](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) gives the following worst-case state growth at accuracy $\delta$:

| Predictor class | Total state growth |
|---|---|
| Stationary | $\delta^{-\Theta(1)}$ |
| Generalized reversible under a specified state involution | $\delta^{-\Theta(1)}$ |
| Ordinarily reversible | $\exp(\delta^{-\Theta(1)})$ |

These comparisons use the same target family, two physical fields, any fixed positive clock, common hidden exit cap $3k$, preparation and binary readout. Targets retain hidden band $[k,3k]$. Rivals may choose arbitrary bounded kinetic barriers without matching a histogram or a finite label alphabet. The exponents are unmatched; state count does not charge parameter precision, construction time or sampling cost.

The [generalized-reversal predictor](docs/GENERALIZED_REVERSAL_PREDICTION.md) reverses a retained memory word while preserving its actuator value. Its entropy production is zero under that reversal, even when identity-reversal entropy production is positive. Thus an ordinary-reversal state penalty is **not a universal thermodynamic dissipation or heat requirement**. The physical reversal of retained variables must be specified. The [entropy comparison](docs/GENERAL_INTERFACE_ENTROPY_BOUND.md) and [resource frontier](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) retain their explicit identity-reversal meaning.

## Scope, evidence and next questions

The [single-force conformational model](docs/SINGLE_FORCE_CONFORMATIONAL_MODEL.md) interprets the earlier hub network through force-dependent equilibrium bias and transition-state barriers. It is not the coupled-switch model or a demonstrated molecular implementation. [Interface robustness](docs/PHYSICAL_INTERFACE_ROBUSTNESS.md) treats small rate and ramp errors within that earlier setting. The new switch result has certified fixed-calibration tolerances and sampling bounds, but no device implementation or claim of experimental practicality. A natural implementation of generalized-reversal memory is a separate question.

The repository contains older binary, uncapped-rate, response-order and compression theorems with different assumptions. Their proofs remain unchanged and are indexed in the [claim ledger](docs/CLAIM_LEDGER.md) and [dossier](docs/RESEARCH_DOSSIER.md). Internal mathematical reviews, source comparisons and finite certificates are different kinds of evidence; none constitutes external peer review or a complete priority determination.

For reproducibility, use the pinned environment and the [Makefile](Makefile):

```sh
make check PYTHON=.venv/bin/python
```

[Verification](docs/VERIFICATION.md) records the full suite and its limits. The certificates bound entire error boxes and fixed comparison models; they do not optimize over rival generators. The next scientific priority is a larger observable separation or a more informative short measurement, alongside better statistical tests and a closer source comparison. The present endpoint-only sample burden is a concrete obstacle to physical significance. Manuscript drafting remains deferred.
