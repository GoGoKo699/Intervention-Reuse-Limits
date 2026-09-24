# PRL exploration: four endpoints and two equilibrium preparations

[Research dossier](RESEARCH_DOSSIER.md) · [Claim ledger](CLAIM_LEDGER.md) · [Four-endpoint proof](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) · [Measurement cost](FAMILIAR_SWITCH_PREPARATION_COST.md) · [Verification](VERIFICATION.md)

**Research target, 24 September 2026.** The user selected *Physical Review Letters*, prefers a familiar physical candidate, and emphasizes that a strong result should be simple. Manuscript drafting remains the last step. The [official PRL criteria](https://journals.aps.org/prl/about) are a publication reference, not an acceptance prediction. This checkpoint finds a simpler experimental identity and a larger certified gap by adding a second equilibrium preparation.

## 1. A short physical mechanism and four measurements

The target is the same pair of time-even conformational switches: energy $-JSZ-hS$, heat-bath flips and equal attempt rates. Observe only $S$. Prepare equilibrium at either $0$ or $H$, and measure the four means

$$
m=\pi_0E_HS,\quad a=\pi_HE_0S,\quad
b=\pi_HE_0E_HS,\quad \ell=\pi_0E_HE_0S.
$$

Every ordinary model obeying the shared force relation $\pi_H=\pi_0(1+uS)$, $u=\tanh H$, satisfies the exact conditional-covariance identity

$$
b-m-a+\ell+\sigma(u\ell-am)
=-\frac{\sigma u^2}{1-\sigma u}
\operatorname{Cov}_{\pi_0}(E_HS,E_0S\mid S=\sigma).
$$

A binary-readout model with at most three states has a singleton sector, whose conditional covariance vanishes. In the physical pair, the hidden conformation changes both response propensities within both visible sectors, so both conditional covariances are positive. Every ordinary rival therefore needs four states. The known positive three-state stationary predictor matches the closed mean dynamics from both equilibrium preparations, so it still suffices.

The lower permits arbitrary rival graphs, masses and rates, even reversible stochastic kernels without continuous-time embeddability. It uses no determinant, generator reconstruction or matrix logarithm. One shared model explains all four experiments. The preparation relation and ordinary detailed balance remain essential; this is not a device-independent state witness or an entropy-production test. The physical target is itself reversible at both fixed fields.

## 2. A nearly sharp quantitative example

Retain $J=H=\log3$ and choose a common tick $3/2$. The four active sequences last $3/2,3/2,3,3$ attempt-time units, with at most one field switch. The [exact rational certificate](../reports/switch_preparation_witness.json) proves that the best ordinary-three-state maximum occupation error lies in

$$
\left(\frac9{5000},\frac1{550}\right).
$$

This is 0.18 to 0.181819 percentage points, a bracket of ratio $100/99$. The lower excludes an entire response cube for both possible singleton identities. The upper is a fixed positive rational ordinary model, rigorously enclosed on the identical four cells. No global optimality of a numerical fit is claimed. The unrestricted minimum is three and the ordinary minimum four throughout $0\le\delta_P\le9/5000$.

The [saved-model diagnostic](../reports/switch_preparation_screen.json) retains the two bounded local fits and the rounded comparator; replay runs no optimizer. Exploratory clock tuning on the old seven-word design suggested only modest gains. The useful change is the second preparation and the resulting direct covariance identity. It is an added experimental resource, not a stronger bound for the unchanged single-preparation task.

## 3. Calibration and measurement cost remain visible

The biased-reference polynomial and approximate-tilt residual in the [proof](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) cover stationary low-field bias and relative tilt-parameter uncertainty $10^{-4}$, and high-stationary-law TV discrepancy $10^{-5}$. With simultaneous preparation TV, fixed field-level and fixed tick errors $10^{-5}$, the actual ordinary-small-model separation exceeds $1/625=0.0016$. Each model uses one fixed preparation law per field across its two cells. The calibrated state minima are three versus four for $10^{-5}\le\delta_P\le1/625$.

The [cost analysis](FAMILIAR_SWITCH_PREPARATION_COST.md) gives conservative four-cell designs at 5% false-positive and false-negative probabilities:

| Task | Sufficient endpoints |
|---|---:|
| Nominal exact-null rejection | 12,531,296 |
| Calibrated exact-null rejection | 15,859,920 |
| Calibrated exclusion at occupation allowance $10^{-4}$ | 18,045,064 |

The calibrated exact-null count is more than 55 times smaller than the preceding sufficient seven-cell design, under the changed preparation resource. A separate nominal information lower requires at least 174,900 endpoints for fixed-budget tests; the upper and lower are still far apart. These are physical sampling demands, not computational demands on the user's Ryzen AI Max+ 395 / 128 GB machine.

Target-specific waits of 62 and 36 attempt-time units suffice for the low and high preparation budgets. No uniform wait prepares arbitrary slow rivals, and visible balance cannot certify full hidden-state TV. Fixed field-specific kernels are assumed; arbitrary drift and finite ramps remain separate. A noninvasive initial snapshot can replace the high-field preparation through weighting, but its observation model and sampling cost need a separate analysis. The three-state predictor matches those initial/final joint laws under exact preparation, not arbitrary multitime trajectories.

## 4. Scientific assessment and next priority

The result is now simpler at its core: four probabilities recover a conditional covariance, and a singleton sector cannot support it. The deterministic gap is almost pinned down for the selected experiment. The source comparison and internal reviews remain [explicit](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md); reciprocity, change of measure and dimension witnesses are established ingredients. A bounded search does not certify novelty. The earlier unresolved Falk full-text comparison remains open.

The next focused task should be a statistically sharper test for these four cells, including unequal allocation or direct use of the quadratic identity. A physical implementation also needs credible preparation and force-law calibration. The optional initial-snapshot experiment offers a concrete preparation/readout trade to price separately. Another broad microscopic-model search is less informative until these specific bottlenecks are understood.

This is progress toward a concise physics result, but it does not establish experimental practicality or PRL readiness. Manuscript drafting stays deferred, and no collaborator contact is part of this checkpoint.

## 5. Earlier results retained separately

The [seven-endpoint theorem](FAMILIAR_SWITCH_FINITE_MARGIN.md), [calibration theorem](FAMILIAR_SWITCH_CALIBRATION.md) and [measurement analysis](FAMILIAR_SWITCH_MEASUREMENT_COST.md) retain their single-preparation statements. Their nominal gap exceeds $1/2000$; the calibrated gap exceeds $3/10000$. They are not overwritten by the two-preparation comparison.

The [matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) gives exact counts $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$ for a separate capped hub-interface family. The [variance principle](KINETIC_VARIANCE_COMPRESSION.md) supplies all-protocol compression through kinetic heterogeneity and hidden mixing. The [asymptotic reversal theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) remains a separate polynomial-versus-exponential result with its own interface and reversal convention.

This continuation starts from published commit 3c56fd45ff5f5988e59c0a4aff833663b53ded53, tree 6195a00f28c296b9e7b38309e604559e7c1f0068, with successful [CI run 35944183992](https://github.com/GoGoKo699/Intervention-Reuse-Limits/actions/runs/35944183992). The 95 protected baseline files, earlier proof bindings, nine recovery files and original license remain preserved. [Verification](VERIFICATION.md) distinguishes local completion from publication CI.
