# Intervention Reuse Limits

**What must a model remember when its predictions must survive interventions?**

Our current small example is familiar: **two coupled conformational switches**, represented by time-even Ising variables with heat-bath dynamics. Their four equilibrium configurations admit an exact **three-state stationary predictor** for the controlled mean of one switch. Every **ordinary-reversible predictor needs four states**, under the same Gibbs control tilt.

The simplest current experiment uses **one equilibrium preparation and two opposite pulse orders**, with an initial and final binary readout:

| Protocol | Preparation | Active fields | Recorded data |
|---|---|---|---|
| $A$ | Low-field equilibrium | $0,H$ | Initial bit $I$, final bit $Y$ |
| $B$ | Low-field equilibrium | $H,0$ | Initial bit $J$, final bit $Z$ |

The mechanism is a conditional covariance. A hidden conformation changes the response to both pulses, even after fixing the visible conformation. Detailed balance makes that covariance measurable by reversing pulse order. It is nonzero in both visible sectors, so each sector needs at least two states. A stationary predictor with circulation reproduces both initial/final joint laws with three states.

The [direct snapshot theorem](docs/FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) uses four moments $m=\mathbb EY$, $c=\mathbb E(IY)$, $\ell=\mathbb EZ$, $d=\mathbb E(JZ)$. Every ordinary model with at most three states satisfies one of the two identities

$$
u c-u(1+\sigma m)d+\sigma(u-m)\ell=0,\qquad \sigma=\pm1,
$$

where $u=\tanh H$. The coupled pair violates both. This necessity has no rival rate cap and includes arbitrary reversible stochastic tick kernels. One fixed model, preparation, instrument and readout must explain both protocols. Shared Gibbs stationary laws and the specified measurement model are substantive assumptions.

**The detector contrasts need not be calibrated.** Let $(M,C,L,D)$ be the four recorded moments, after independent symmetric bit flips. The [unknown-readout witness](docs/FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) uses

$$
 R=u(C-D)+uMD-(u-M)L>0,
 \qquad 0<M<u,\quad L,D>0,\quad C<D.
$$

These conditions exclude every ordinary model with at most three states even if each rival chooses its own initial and final error probabilities anywhere in $[0,1/2]$. Its detector must still be memoryless, symmetric, independent across the two bits, and fixed across protocols.

**Repeated initial readout can tolerate errors correlated with hidden kicks.** The [seven-readout theorem](docs/FAMILIAR_SWITCH_REPEATED_READOUT.md) replaces each initial bit by the majority of seven protected readings. Each reading must preserve the visible sector and, after discarding its outcome, preserve conditional equilibrium. Its error has one fixed probability conditional on the entire pre-readout state and history; it may be correlated with the hidden update caused by that same reading. At error probability at most 2%, the majority-label/postmeasurement-state joint law is within **0.0000053356544** of ideal initial readout. Hidden kicks need not be small or independent of their electronic errors.

A disagreement gate on the first two readings, using the same five million trials, covers ordinary rivals whose initial error probability is unknown anywhere in $[0,1/2]$. With target errors at most 1%, the existing serial score retains false rejection below 5% and power above 95%, under its preparation and physical promises. The cost becomes **40 million raw binary readings**: seven initial and one final per trial. The two pulse orders, score and threshold remain unchanged. The final detector still obeys the independent symmetric-channel assumption. The gate does not certify fresh errors, sector protection or equilibrium preservation; a shared error across all seven readings can evade it. No three-state realization of the full eight-reading transcript is asserted. [Proof and scope](docs/FAMILIAR_SWITCH_REPEATED_READOUT.md) · [Source comparison](docs/FAMILIAR_SWITCH_REPEATED_READOUT_SOURCE_AUDIT.md).

**The memory advantage survives independent one-percent rate changes.** At $J=\log3$, $H=\log2$ and equal dwell times $5/4$, the [direct kinetic theorem](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md) permits an independent symmetric prefactor in $[.99,1.01]$ on each of the four transition edges at each field. These eight factors preserve Gibbs detailed balance but can break heat-bath moment closure. The same two words retain state minima **three versus four on $[0.00008,0.0009]$**, including the physical allowances below. A [local three-state construction](docs/FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md) fits the two joint snapshot laws exactly at nominal fields and times, using genuine continuous-time Markov generators. It fits those two laws, without asserting agreement for other control words or complete trajectories.

**The five-million-trial test can run serially on one device.** The [conditional sampling theorem](docs/FAMILIAR_SWITCH_SERIAL_SAMPLING.md) retains the [kinetic score test](docs/FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md), its gates and threshold .0021, with 2.5 million trials per protocol and ten million binary readouts. False rejection remains below 5% and power above 95% under deterministic alternation of the two protocols. Trials may be dependent, provided that after every history their conditional recorded joint laws stay within $0.000079$ for the target, or $0.00022$ for the null, of **one fixed stationary reference pair**. The null budget includes observed-joint-TV prediction allowance $0.0002$, exceeding the finitely prepared general-three-state conditional-pair error bound $0.00009$ below. An unconditional average error does not replace this conditional promise; preparation, the initial joint instrument, fixed plateau generators and the stated electronic channels remain substantive.

The [finite-reset theorem](docs/FAMILIAR_SWITCH_FINITE_RESET.md) supplies the target preparation step: an actual low-field wait of **63 attempt-time units** gives hidden-state TV error below $10^{-5}$ from any preceding state, uniformly over the one-percent kinetic family and $|h_0|\le10^{-5}$. Five million resets plus the nominal active pulses cost **327.5 million attempt-time units**, 26.2 times the active-only exposure. Readout, switching and other implementation durations are additional. This target bound does not reset every arbitrarily slow ordinary rival in 63 units. The serial statistical null requires its own conditional preparation guarantee; the broader stationary state-count lower remains unchanged and has no rival rate cap.

The constructive three-state predictor can use **the same 63-unit reset**, giving conditional two-record table error below $.00009$ relative to the actual target. It receives no ideal fresh-preparation advantage. This is a per-trial table guarantee, not a full-record TV bound or a new serial state-count minimum.

The sufficient relative rate allowance increases **500-fold, from 20 ppm to 1%**, with the same total trial count and null approximation allowance. This is a mathematical tolerance improvement, not an optimized threshold or measured device capability. The [earlier integrated-error theorem](docs/FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) and [its score test](docs/FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md) remain valid at their stated scopes. At exact preparation, fields, timing and initial instrument, the new kinetic family has exact three-state prediction and ordinary-three-state gap $>0.001$, giving state minima on $[0,0.001]$.

**The heat-bath reference has a sharper guarantee.** Keep $J=\log3$, use $H=\log2$, and let both dwell times be $5/4$. The [weaker-field robustness theorem](docs/FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) gives a nominal recorded-table gap **greater than 0.00115** for target bit-error probabilities at most 1%. With preparation, field, timing and initial-disturbance allowances $10^{-5}$, stationary bias and tilt uncertainty $10^{-4}$, and stationary-law TV defect $10^{-5}$, the gap remains **greater than 0.001**. Three general states suffice within **0.00002**. The state minima are therefore three and four for $0.00002\le\delta_{\rm obs}\le0.001$, five times the earlier certified upper end of this interval. The two-plateau active duration falls from three to $5/2$ attempt-time units.

The [new integer-score test](docs/FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md) uses only the same initial and final bits. Both allocations have false rejection below 5% and target power above 95% for fresh independent trials, with the physical allowances above:

| Unknown-detector null | Trials per protocol | Total paired trials | Binary readouts |
|---|---:|---:|---:|
| Admissible ordinary model, at most three states | 1,000,000 | **2,000,000** | 4,000,000 |
| Same model class, observed-joint-TV approximation allowance $10^{-4}$ | 1,250,000 | **2,500,000** | 5,000,000 |

The approximation allowance exceeds the general three-state constructive error. No extra field, preparation, protocol or detector calibration is added. The weaker-field experiment has a smaller ideal witness but loses less signal to the unknown symmetric detector errors; the recorded witness is larger. This is a certified operating point, with no claim of optimal fields, sample complexity or experimental feasibility.

A separate tolerance result allows preparation, field, timing and initial-disturbance errors $5\times10^{-5}$ while preserving state minima three and four on $[10^{-4},6\times10^{-4}]$. The trial budgets above remain proved only for the $10^{-5}$ allowances.

**Changing the physical design beats every test confined to the old design.** At $J=H=\log3$ and dwell $3/2$, the [information bound](docs/FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) requires more than $810000\log19\approx2.385$ million trials in target expectation, even with adaptive sampling, for the nominal target with one-percent errors. The new design needs only two million and covers that detector-error value. The physical and detector classes have the same form at their respective fields; the old lower bound is not a lower bound for the new experiment. Preparation overhead and calibration acquisition are not priced.

**The earlier operating point remains documented.** At $J=H=\log3$ and dwell $3/2$, the unknown-detector nominal and robust gaps remain greater than 0.000375 and 0.0002. Its [fixed-score test](docs/FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md) needs 32 million paired trials, or 90 million with the additional approximation allowance $10^{-4}$. The new design reduces these sufficient budgets by factors of 16 and 36, respectively, while changing the high field and dwell time. The original 508-million confidence-box test also remains valid at its historical scope.

**Detector calibration has a provable statistical value at the earlier operating point.** At $J=H=\log3$ and dwell $3/2$, for the nominal target with one-percent bit errors, the [information lower bound](docs/FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md) requires at least **2,384,996 paired trials** for any fixed-budget test against the unknown-detector class, even though the earlier calibrated test below needs only 1.2 million. Adaptive protocol choices and stopping still require $\mathbb E_*N>810000\log19$. Thus the specified calibration promise reduces the necessary observation budget by more than a factor of 1.98 in this comparison. The cost of obtaining that calibration is separate and unpriced. The smaller calibrated-detector counts do not apply to the unknown-contrast null.

**The earlier calibrated gap is almost pinned down.** At $J=H=\log3$ and tick $3/2$, the best ordinary-three-state maximum joint-law TV error with ideal readout lies strictly between **0.00184 and 0.00185**, a bracket of ratio $185/184$. The lower covers the entire stated rival class; the upper is one certified feasible ordinary model. Three general stationary states are exact for these two joint laws. The longest active experiment lasts three attempt-time units. This does not assert arbitrary multitime path-law equality.

**Preparation, controls and measurement are included.** With simultaneous preparation TV, fixed field/tick errors and initial-readout disturbance budgets $10^{-5}$, stationary low-field bias and relative tilt uncertainty $10^{-4}$, and high-stationary-law discrepancy $10^{-5}$, the witness tolerates independent symmetric readout error probabilities **$0.01\pm10^{-5}$** at both observations. The recorded joint-law gap remains above **0.0015**; the state minima are three versus four for $4\times10^{-5}\le\delta\le0.0015$. Known detector noise, uncertainty in its calibration, and hidden-state disturbance are separate quantities. This 1% detector example is a mathematical operating point, not a device specification.

The earlier [fixed-score tests](docs/FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) improve the measurement budget for their specified detector classes. These counts do not transfer to the detector-unknown result. Each design has false rejection below 5% and target power above 95%, under its stated class:

| Snapshot design | Fresh paired trials | Binary readouts |
|---|---:|---:|
| Exact preparation, controls and readout | 900,000 | 1,800,000 |
| Physical nuisance; ideal readout | 1,000,000 | 2,000,000 |
| Physical nuisance, disturbance and calibrated 1% readout noise | 1,200,000 | 2,400,000 |
| Same noisy class; exclude ordinary approximation within observed TV $10^{-4}$ | 1,500,000 | 3,000,000 |

A separate ideal information lower requires at least **79,500 paired trials** for fixed-budget testing. The sufficient and necessary budgets are not matched. A target-specific low-field wait of 62 attempt-time units supports the preparation tolerance; it does not prepare every arbitrarily slow rival or establish fresh-trial independence. Visible balance alone cannot certify full hidden-state preparation or measurement disturbance.

The earlier **two-preparation, four-endpoint experiment** remains useful when initial observation is costly. Its [new score test](docs/FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md) needs **1,450,000**, **1,670,000**, or **1,890,000** single-readout trials for nominal, calibrated and calibrated finite-accuracy testing. These replace earlier sufficient confidence-box counts of 12,531,296, 15,859,920 and 18,045,064 on those same classes. Its [deterministic theorem](docs/FAMILIAR_SWITCH_PREPARATION_WITNESS.md) and [preparation costs](docs/FAMILIAR_SWITCH_PREPARATION_COST.md) remain unchanged. Preparation types, readouts and calibration premises differ between the designs; neither dominates every resource.

The [exact snapshot certificate](reports/switch_snapshot_design.json), [endpoint certificate](reports/switch_endpoint_score.json), [saved-model replay](reports/switch_snapshot_screen.json), [source comparison](docs/FAMILIAR_SWITCH_SCORE_SOURCE_AUDIT.md), and [internal review](docs/FAMILIAR_SWITCH_SNAPSHOT_INTERNAL_REVIEW.md) separate analytic proof, essential rational bounds and statistical assumptions. No large simulation is needed.

**A conditional charge-state realization removes equal-rate tuning.** Two capacitively coupled nondegenerate dots, each exchanging electrons with an equilibrium reservoir, map exactly to the switches under the specified sequential Fermi-tunneling model. The [charge derivation](docs/FAMILIAR_SWITCH_CHARGE_REALIZATION.md) gives an exact three-state predictor for hidden-to-observed tunneling-rate ratios at least $2/3$ over the selected field range. Ratios from $2/3$ to $2$ also retain a common exit cap of three observed-attempt units. The numerical gaps and sample counts above remain tied to equal attempts. The [primary-source audit](docs/FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) distinguishes demonstrated device components from the unestablished complete experimental specification.

**Preparation and the initial instrument remain real assumptions.** The [preparation boundary](docs/FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) constructs a biased ordinary model whose entire low-field binary record looks equilibrated, and a disturbance that preserves every endpoint distribution while corrupting the initial/final correlation. It also gives an optional response-specific preparation check for at-most-three-state rivals, adding three protocol types under exact balance. This does not remove the instrument premise or inherit a previous trial count.

The [new observable preparation bound](docs/FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) allows arbitrary hidden preparation and approximate stationary balance in that five-type design. It bounds the equilibrium bias of selected responses using low-pair means, relaxation and original-to-prefixed response differences, without a rival mixing-time estimate. It requires an exactly protected initial instrument and independent symmetric electronics. Each prefixed type must include a silent copy of the same instrument before its low wait; this is an extra physical operation.

The [randomized calibration analysis](docs/FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) handles history-dependent preparation by choosing the type only after preparation. Its conservative allocation of **60 billion trials** estimates eight corrected scalar functionals within $.001$ simultaneously with probability above 96%. This is a precision guarantee, not a full five-type rejection/power theorem or a lower bound on calibration cost. The added data have no established three-state predictor or inherited five-million-trial guarantee. We retain the two-word core as the practical research design and seek sharper joint calibration.

The [readout calibration boundary](docs/FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md) strengthens the instrument warning: a three-state classical model can pass arbitrary immediate repeat-readout checks, all low-only records and unchanged-endpoint checks, while a correlation between the electronic error and a hidden measurement kick changes the two snapshot tables. The example does not fit the selected target or show false rejection by its gated score. Physical independence of the electronic errors from the hidden update remains a separate requirement.

The [protected-readout theorem](docs/FAMILIAR_SWITCH_PROTECTED_READOUT.md) gives a simple sufficient instrument: hold the observed state fixed and preserve the equilibrium law inside each observed sector. Hidden motion may then be arbitrarily large without changing the retained initial-label/postmeasurement-state joint law at equilibrium. Preparation error is charged once; visible leakage and conditional-stationarity defects supply explicit extra bounds. In the charge model, blocking observed-dot tunneling requires a barrier actuator and controlled switching during the readout stage. It adds no recorded bit or tested word, but is a physical control resource. Independent symmetric electronics and the joint-instrument promise remain requirements. The existing 62-unit reset is target-only for the reference heat-bath model and does not establish independent repeated trials.

The [serial-reset verifier](scripts/verify_switch_serial_reset.py), [report](reports/switch_serial_reset.json), [source comparison](docs/FAMILIAR_SWITCH_SERIAL_RESET_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_SERIAL_RESET_INTERNAL_REVIEW.md) accompany the conditional sampling and finite-reset results. The [percent-kinetic verifier](scripts/verify_switch_percent_kinetics.py), [report](reports/switch_percent_kinetics.json), [source comparison](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_PERCENT_KINETIC_INTERNAL_REVIEW.md) retain the direct robustness and local realization. The earlier [kinetic-interface verifier](scripts/verify_switch_kinetic_interface.py), [report](reports/switch_kinetic_interface.json), [source comparison](docs/FAMILIAR_SWITCH_KINETIC_INTERFACE_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_KINETIC_INTERFACE_INTERNAL_REVIEW.md) retain the protected-readout and integrated-error results. These records distinguish mathematical guarantees from experimental calibration.

The [observable-calibration verifier](scripts/verify_switch_observable_calibration.py), [report](reports/switch_observable_calibration.json), [source comparison](docs/FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_INTERNAL_REVIEW.md) record the new preparation inequality, scalar precision calculation and instrument boundary. The marginal-versus-joint disturbance distinction is established; a close recent full-text comparison remains unresolved.

The [weaker-field verifier](scripts/verify_switch_weak_field.py) and [report](reports/switch_weak_field.json) certify the new margin and trial counts. Its [source comparison](docs/FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md) and [internal review](docs/FAMILIAR_SWITCH_WEAK_FIELD_INTERNAL_REVIEW.md) record the inherited tools and new operating-point argument. The [physical-interface verifier](scripts/verify_switch_physical_interface.py) and [report](reports/switch_physical_interface.json) retain their 108 checks, and the [earlier cost verifier](scripts/verify_switch_uncalibrated_score.py) and [report](reports/switch_uncalibrated_score.json) retain the old score and information bounds. The [verification record](docs/VERIFICATION.md) distinguishes analytic review, finite checks and the complete repository gate.

The research target is **Physical Review Letters**; manuscript drafting remains the last step. The [current exploration](docs/PRL_EXPLORATION.md), [research dossier](docs/RESEARCH_DOSSIER.md), and [claim ledger](docs/CLAIM_LEDGER.md) retain the assumptions and unresolved questions. This is a controlled realization comparison, not an implementation-independent heat-cost result or a PRL-readiness claim.

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

[Verification](docs/VERIFICATION.md) records the full suite and its limits. The certificates cover entire error boxes and explicit local realizations; they do not optimize the allowed rate error. Serial sampling and finite target preparation have their own conditional guarantees and exposure budget. The optional observable calibration now makes part of the assumption-versus-measurement tradeoff explicit, but its present scalar precision construction is expensive. The next priority is sharper joint calibration and physically justified independence of the readout electronics from the hidden measurement update. Keep the short two-word core and its explicit preparation and instrument promises while pursuing those questions. Further field or score-constant tuning is secondary. Manuscript drafting remains deferred.
