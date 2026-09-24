# Detector calibration changes the necessary observation budget

The same two-protocol experiment and the same noisy physical target
support a strict operational comparison. With a detector calibration
promise, the existing test needs **1.2 million paired-snapshot trials**
for at most five-percent false rejection and at least 95-percent power.
When competing models may choose arbitrary independent symmetric
detector errors, every test with those guarantees needs

$$
 \boxed{\mathbb E_*N>810000\log19\approx2.385\text{ million}.}
 \tag{1}
$$

The lower bound holds even for adaptive protocol selection and an
almost-surely finite stopping rule. It therefore exceeds the earlier
fixed sufficient total by more than a factor of 1.98. This is a value of
the specified calibration promise for this experiment, not an optimized
sample-complexity theorem or a new general information inequality.
Obtaining the calibration itself has a separate, unpriced cost.

[Unknown-detector model and witness](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) ·
[Calibrated 1.2-million-trial test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) ·
[Inspected change-of-measure source](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md) ·
[Exact cost verifier](../scripts/verify_switch_uncalibrated_score.py) ·
[Certificate report](../reports/switch_uncalibrated_score.json)

## 1. One target, two competing-model classes

Fix the nominal target with $J=H=\log3$, equal unit attempt rates,
balanced low-field equilibrium preparation, and clock duration $3/2$
at each field. A trial applies $0,H$ or $H,0$ and records the initial
and final binary readouts. Both target readout bits have independent
symmetric error probability exactly $1/100$, fixed across protocols
and independent of the hidden dynamics. Its true joint tables are the
ones in the [frozen snapshot certificate](../reports/switch_snapshot_design.json).
All other execution and instrument errors are zero in this lower-bound
instance.

This target is covered by the earlier robust calibrated test: that test
permits each detector error probability to differ from $0.01$ by at most
$10^{-5}$, alongside its stated physical tolerances. Its corresponding
ordinary at-most-three-state null obeys the same calibration intervals.
The proved sufficient allocation is $700000$ trials of $0,H$ and
$500000$ trials of $H,0$.

The unknown-detector null retains the same shared-model, preparation,
reversibility, force-law, and independent symmetric channel structure.
It permits each rival detector error probability to range over
$[0,1/2]$, with the two probabilities fixed across protocols. In
particular, it contains the perfect-detector ordinary model constructed
below. The target's own one-percent errors remain unchanged. Different
hypotheses may have different detector parameters; requiring an unknown
but numerically identical detector under both hypotheses would be a
different statistical model.

For the information lower bound, the rival is exactly stationary,
ordinarily reversible, and obeys the exact Gibbs tilt. It is therefore
inside the allowed robust null without spending any physical tolerance.
Enlarging that null further by an observed-law approximation allowance
can only preserve this necessary bound.

## 2. A fixed ordinary comparator with a perfect detector

Use three states, readout $S=(-1,+1,+1)$, and stationary laws

$$
 \pi_0=\left(\frac12,\frac{64436}{10^6},
                       \frac{435564}{10^6}\right),\qquad
 \pi_H(i)=\pi_0(i)\left(1+\frac45S_i\right).
 \tag{2}
$$

For edge order $(0,1),(0,2),(1,2)$, choose the symmetric stationary
edge fluxes

| Field | Edge-flux numerators, denominator $10^6$ |
|---|---|
| $0$ | $(41237,38789,22424)$ |
| $H$ | $(20505,24202,651)$ |

At each field put $Q_{ij}=f_{ij}/\pi_i$ for $i\ne j$ and
$Q_{ii}=-\sum_{j\ne i}Q_{ij}$. Every edge flux is positive, so these
are irreducible continuous-time generators. The identities
$\pi_iQ_{ij}=f_{ij}=\pi_jQ_{ji}$ prove ordinary detailed balance.
Both laws are normalized and have the prescribed tilt, and the largest
total exit rate is $63661/64436<1$. Use the propagators
$\exp(3Q_0/2)$ and $\exp(3Q_H/2)$, the same low-field preparation in
both arms, and a perfect detector.

Let $P_A,P_B$ be the target's one-percent-noisy recorded tables and
$Q_A,Q_B$ be this comparator's perfect-detector recorded tables. The
exact matrix-exponential certificate bounds the Taylor majorants by

| Arm | Upper bound for $\frac12\sum_j (P_j-Q_j)^2/\min(P_j,Q_j)$ |
|---|---|
| $0,H$ | $1110332189/10^{15}$ |
| $H,0$ | $276614949/250000000000000$ |

Every table entry is positive and both displayed bounds are strictly
less than $1/900000$. Normalization cancels the linear term in a Taylor
expansion of $D(P\Vert Q)$ about $Q$; the diagonal Hessian along the
line segment is bounded by $1/\min(P_j,Q_j)$. Consequently

$$
 D(P_A\Vert Q_A)<\frac1{900000},\qquad
 D(P_B\Vert Q_B)<\frac1{900000}.
 \tag{3}
$$

The comparator was selected by a small numerical search and then fixed
at the rational parameters above. The certificate uses exact rational
arithmetic and rigorous exponential enclosures for that fixed model.
Neither the search nor this feasible example proves it is the closest
ordinary model.

## 3. Any fresh-trial test pays the information cost

Consider any test using only the two arms. It may randomize, choose the
next arm from the preceding data, and stop at an almost-surely finite
time $N$. Each observation must still be a fresh independent trial with
the law of its selected arm. Assume the probability of rejecting every
admissible ordinary null is at most $0.05$, and that the probability of
rejection at the fixed target above is at least $0.95$.

If $\mathbb E_*N$ is infinite, (1) is immediate. Otherwise, the
likelihood chain rule and (3) bound the accumulated target-to-comparator
relative entropy by $\mathbb E_*N/900000$. Data processing to the
binary rejection event bounds that entropy below by

$$
 \operatorname{kl}(0.95,0.05)=0.9\log19.
 \tag{4}
$$

Combining the two inequalities proves (1). The sequential
change-of-measure statement is established background: Kaufmann,
Cappé and Garivier, *JMLR* **17** (2016), Lemma 1 and Appendix A.1,
as inspected in the linked source audit. It applies here because both
arm tables have full support and the reset-trial conditional laws are
fixed. Waiting for a prescribed time between samples does not itself
establish these assumptions uniformly over arbitrarily slow rivals.

For the same fixed target, the calibrated test's deterministic total is
$1200000$. The ratio of the unknown-detector necessary expectation to
that sufficient total is strictly larger than

$$
 \frac{810000\log19}{1200000}
 =\frac{27}{40}\log19>1.98.
 \tag{5}
$$

The comparison does not assert that 1.2 million is optimal for calibrated
detectors, that 2.385 million is attainable without calibration, or that
these trial counts imply laboratory feasibility. It establishes that
the enlarged detector null cannot be handled within the earlier
calibrated trial budget, even at this shared target. Each paired trial
contains two binary readouts; preparation time and calibration effort
are additional resources.
