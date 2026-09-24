# PRL exploration: unknown readout noise and a charge-state realization

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Snapshot proof](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) · [Snapshot score test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) · [Endpoint score test](FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md) · [Verification](VERIFICATION.md)

**Research target, 24 September 2026.** The user selected *Physical Review Letters*, prefers a familiar physical candidate, and emphasizes that a strong result should be simple. Manuscript drafting remains the last step. The new lead removes the need to calibrate detector contrasts within a specified symmetric-channel model. A conditional charge-state realization also removes equal-attempt tuning. Preparation and initial-instrument boundaries remain explicit rather than being inferred from apparently equilibrated binary data.

## 1. The short physical mechanism

The target is a pair of time-even conformational switches: energy $-JSZ-hS$, heat-bath flips and equal attempt rates. Observe only $S$. Prepare once at low-field equilibrium, run either $0H$ or $H0$, and record the initial/final binary pair. Define

$$
m=\mathbb E_A Y,\quad c=\mathbb E_A(IY),\quad
\ell=\mathbb E_B Z,\quad d=\mathbb E_B(JZ).
$$

Under the shared Gibbs relation $\pi_H=\pi_0(1+uS)$, with $u=\tanh H$ and balanced $\pi_0$, ordinary detailed balance gives

$$
u c-u(1+\sigma m)d+\sigma(u-m)\ell
=-\frac{\sigma u^2}{1-\sigma u}
\operatorname{Cov}_{\pi_0}(E_HS,E_0S\mid S=\sigma).
$$

A model with at most three states and deterministic binary readout has a singleton sector, whose conditional covariance vanishes. The hidden conformation in the physical pair changes both response propensities within both sectors, so both covariances are positive. Every ordinary rival needs four states. The positive stationary three-state predictor matches the conditional initial coordinates and hence both joint laws exactly.

The lower allows arbitrary rival graphs, masses and rates, including reversible stochastic tick kernels. One fixed preparation, instrument, readout and pair of propagators must explain both protocols. This is a constrained dynamical realization comparison. It does not certify a device-independent dimension, entropy production, or complete controlled path-law equality.

## 2. The detector-unknown result

Let $(M,C,L,D)$ be the recorded versions of the four moments after fixed
independent symmetric errors at the initial and final readouts. The
[new witness](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) uses

$$
 R=u(C-D)+uMD-(u-M)L>0,\qquad
 0<M<u,\quad L,D>0,\quad C<D.
$$

The detector-cleared singleton polynomial is bilinear in the two unknown
contrasts. Its four corner signs rule out every ordinary rival with at
most three states, even when that rival chooses its own two error
probabilities anywhere in $[0,1/2]$. There is no inverse-contrast
singularity or rival rate cap. Symmetry, independence, no readout feedback
and one fixed detector across both protocols remain required.

For the selected equal-rate target with each error probability at most
one percent, the nominal recorded-joint-TV gap exceeds $3/8000$.
Allowing the stated preparation, control and initial-disturbance errors
$10^{-5}$, low stationary bias and relative-tilt uncertainty $10^{-4}$,
and high-law TV defect $10^{-5}$ leaves a gap greater than $1/5000$.
Three general states suffice within $2\times10^{-5}$, so the state
minima are three and four throughout
$2\times10^{-5}\le\delta_{\rm obs}\le2\times10^{-4}$.
The target signal-loss bound differs from numerical calibration of the
rival's detector: its errors are allowed anywhere up to one half.

A first conservative test uses 254 million independent paired trials
per arm, 508 million total, with false rejection below 5% and target
power above 95%. Hoeffding bounds for the four moments and a finite
box/corner calculation certify its size and power. It tests the composite
null with the stated physical allowances, without an additional
model-approximation allowance. This is a finite sufficient design, not
a practical or near-optimal allocation. The calibrated counts below
do not transfer to this larger null class.

## 3. The preserved calibrated gap

At $J=H=\log3$ and tick $3/2$, the best ordinary-three-state maximum TV error over the two joint laws lies in

$$
(23/12500,37/20000)=(0.00184,0.00185).
$$

The lower is a universal response-box exclusion; the upper is a fixed positive rational ordinary model. Their ratio is $185/184$. The numerical fits only supplied candidates for the upper. The longest active sequence lasts three attempt-time units.

The [robustness proof](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) derives a biased/approximate-Gibbs identity directly for the snapshot moments. A stationary joint-TV radius $0.0018$ is excluded with low-field stationary bias and tilt-parameter uncertainty $10^{-4}$, and high-stationary-law discrepancy $10^{-5}$. Simultaneous preparation TV, fixed field/tick errors and initial disturbance bounds $10^{-5}$ retain a positive executed gap.

Independent symmetric detector flips at the two observations are modeled separately. A known 1% channel contracts TV by at most the factor $0.98^2$ in the lower bound. Allowing each flip probability to lie in $0.01\pm10^{-5}$ still leaves recorded joint-law gap $>0.0015$. A constructive three-state upper has error at most $4\times10^{-5}$, so state minima remain three versus four on $[4\times10^{-5},0.0015]$.

The initial disturbance bound controls the hidden state conditional on its premeasurement state. Neither visible balance nor a short readout duration establishes it. The detector model has no free persistent hidden memory, and the channel's flips are independent of the trajectory and one another. The 1% operating point is a mathematical example, not an experimentally validated instrument.

## 4. Preserved calibrated tests and the resource trade

A fixed tangent score concentrates the statistics relevant to the covariance identity. A gate bounds the quadratic remainder; bounded-variable Bernstein inequalities give uniform false rejection below 5% and target power above 95%. All choices are fixed before observations. Calibration bounds and fresh-trial independence are separate premises. These earlier tests retain their calibrated detector classes.

| Design | Fresh trials | Readouts per trial | Equilibrium preparations |
|---|---:|---:|---|
| Nominal four-endpoint score | 1,450,000 | 1 | Low and high |
| Calibrated four-endpoint score | 1,670,000 | 1 | Low and high |
| Calibrated endpoint score, occupation allowance $10^{-4}$ | 1,890,000 | 1 | Low and high |
| Nominal two-snapshot score | 900,000 | 2 | Low only |
| Physical nuisance, ideal snapshot readout | 1,000,000 | 2 | Low only |
| Fully calibrated noisy snapshot score | 1,200,000 | 2 | Low only |
| Same noisy class, observed-joint-TV allowance $10^{-4}$ | 1,500,000 | 2 | Low only |

The endpoint allocations improve the earlier sufficient confidence-box counts by roughly a factor of nine on the same classes. Snapshot trials require fewer resets and no high-field preparation, but more binary readouts than the comparable endpoint designs. The noisy snapshot row also covers detector assumptions absent from the endpoint rows. These are sufficient choices, not optimal sample budgets.

A separate nominal information lower requires fixed budgets of at least 174,900 endpoints or 79,500 paired trials for their respective observation tasks. The necessary and sufficient counts are not matched. The paired lower also survives a common known detector channel by data processing.

Low-field target reset time 62 suffices at the stated preparation tolerance; high-field time 36 is used only by the endpoint designs. For noisy snapshots, serial target exposure is at most $(65+2\times10^{-5})N$ attempt-time units. These waits neither equilibrate every arbitrarily slow rival nor establish trial independence. Computation remains tiny-matrix CPU work suitable for the user's hardware.

## 5. Conditional physical realization and preparation limits

The [charge realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) starts
with two capacitively coupled nondegenerate dot occupations, each
exchanging particles with its own equal-temperature equilibrium reservoir.
With compensated spectator energy and sequential Fermi tunneling, the
charge energy maps exactly to $-JSZ-hS$; both charge variables are
time-even. A positive three-state triangle covers attempt ratios
$r=\Gamma_{\rm hidden}/\Gamma_{\rm observed}\ge2/3$ over the selected
field range. Restricting $r\le2$ gives the common exit cap
$3\Gamma_{\rm observed}$. Exact compression therefore does not require
equal tunneling rates. The finite numerical gaps and sample allocations
remain certified only at $r=1$.

This model requires isolated relevant levels, the specified Fermi rates,
and controlled unwanted transitions and gate leakage. The
[primary-source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md)
identifies relevant demonstrated components without combining them into
a claimed achieved device specification. Spin degeneracy, energy-dependent
prefactors and metallic-box kinetics cannot be removed by relabeling
their equilibrium energy.

The [preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)
shows two distinct failures: every low-only binary trajectory can look
stationary while hidden preparation bias remains, and an instrument can
preserve every endpoint distribution while destroying the initial/final
correlation. A response-specific bound for at-most-three-state rivals
can replace a preparation premise after adding three protocol types
and assuming exact balance. It leaves the instrument premise in place
and has no inherited sampling allocation.

## 6. Scientific assessment and next priority

The mechanism is concise: reversed pulse order measures a conditional covariance, and a singleton sector cannot support it. Direct treatment of the paired data strengthens the previous $0.001$ snapshot corollary and gives its own nuisance and sampling guarantees. The endpoint task retains its original deterministic theorem and gains a more efficient test.

The equal-rate calibrated gap is already tightly bracketed. The new
result instead removes detector-contrast calibration under explicit
channel assumptions, and the charge bridge supplies a conditional
physical candidate. The next useful work is a less conservative test
for the enlarged null and independently supported preparation,
force-law and initial-instrument conditions. The sampling burden
remains substantial. A larger gap would still help, but changed
resources and observation tasks must be charged explicitly.

The [source comparison](FAMILIAR_SWITCH_SCORE_SOURCE_AUDIT.md) attributes the established concentration and union-null testing tools and links the earlier physical and dimension-witness audits. The earlier unresolved Falk full-text comparison remains open. Internal review and finite certificates are not external validation, a complete priority determination, or PRL readiness. Manuscript drafting stays deferred.

## 7. Preserved results and provenance

The [four-endpoint theorem](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) retains its two-preparation occupation-gap bracket $(9/5000,1/550)$ and calibrated gap $>1/625$. The [seven-endpoint theorem](FAMILIAR_SWITCH_FINITE_MARGIN.md) and [calibration theorem](FAMILIAR_SWITCH_CALIBRATION.md) retain their single-preparation statements. The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md), [variance principle](KINETIC_VARIANCE_COMPRESSION.md), and [asymptotic reversal theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) concern separate families and interfaces.

The preceding snapshot checkpoint started from published commit
5ad525792de4e4fe6c681b067d7185e018265082, tree
cdfa71f58ca37c832f5631e5c21484ae88b25805, with successful
[CI run 35958827202](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35958827202).
This continuation starts from published commit
778954f18164c3a228b845be07298ba1a33326eb, tree
e08a840c71d2474a5ad4866d9daf1c39969e92f6. Earlier protected proofs,
certificate bindings, recovery files and the original license remain
preserved. The new
[physical-interface verifier](../scripts/verify_switch_physical_interface.py)
and [report](../reports/switch_physical_interface.json) pass 108 exact
checks at maximum dense dimension four. The
[internal review](FAMILIAR_SWITCH_PHYSICAL_INTERFACE_INTERNAL_REVIEW.md)
records the proof and source audits.
[Verification](VERIFICATION.md) distinguishes local completion from
publication CI.
