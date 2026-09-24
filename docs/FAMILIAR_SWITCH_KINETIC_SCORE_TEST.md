# Five million trials with a bounded kinetic departure

The weaker-field test remains effective when the target's transition rates
depart from the nominal heat-bath rates. If the kinetic departure adds at
most $\kappa=10^{-4}$ to each recorded joint-table total-variation (TV)
error budget, **five million fresh trials** suffice for false rejection
below $5\%$ and power above $95\%$. The ordinary null also receives an
additional observed-table prediction allowance $e=2\cdot10^{-4}$ per
protocol. This allowance exceeds the general three-state predictor's
constructive error upper bound $1.2\cdot10^{-4}$ at the same kinetic
budget.

The test keeps the existing integer scores and empirical gates. It uses
the same physical setting $J=\log3$, $H=\log2$, dwell times $5/4$, two
chronological words $0H,H0$, and initial--final binary readouts. The
target detector errors are arbitrary fixed values in $[0,.01]$; ordinary
rivals may use arbitrary fixed values in $[0,1/2]$. Both uses are
independent symmetric flips, independent of the hidden dynamics, and
the instrument and channels are shared across the protocols within
each model. No detector calibration or additional observation is used.

This is a sufficient budget under explicit physical and preparation
promises. It is not a sample optimum, a laboratory feasibility claim,
or permission to transfer the earlier two-million-trial bound to the
larger target family. Manuscript drafting remains deferred.

The [frozen weaker-field score proof](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md)
supplies the score identities, stationary singleton inequality, nominal
moment enclosures and concentration arguments. The present note checks
the enlarged error budgets separately. The
[kinetic tolerance theorem](FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) gives
the generator condition used here and the corresponding state-count
comparison.

## 1. One fixed design

Let $(I,Y)$ be the recorded initial--final signs in the $0H$ arm and
$(J,Z)$ those in the $H0$ arm. Use the following lookup table, with the
initial sign listed first:

| Protocol | $(+,+)$ | $(+,-)$ | $(-,+)$ | $(-,-)$ |
|---|---:|---:|---:|---:|
| $0H$: $50X_A$ | 35 | -65 | 5 | 25 |
| $H0$: $50X_B$ | -29 | 59 | -11 | -19 |

Thus

$$
 X_A=\frac{20Y+30IY-15I}{50},\qquad
 X_B=\frac{-20Z-24JZ+15J}{50},\qquad
 \widehat T=\overline X_A+\overline X_B-\frac2{25}.
 \tag{1}
$$

Collect $n=2{,}500{,}000$ independent fresh trials in each arm and
average each arm separately. Reject the ordinary null precisely when
all the empirical gates in Section 1 of the frozen score proof pass
and

$$
 \widehat T>\frac{11}{5000}=.0022.
 \tag{2}
$$

The total is **5,000,000 trials and 10,000,000 binary readouts**. Each
trial's two observations remain statistically dependent; independence
is required between fresh trials. The nominal active duration per trial
is $5/2$ attempt-time units. Preparation and acquisition of the physical
promises are not priced.

The frozen gates and their exact dyadic centers are unchanged. In the
notation $M=\mathbb EY$, $C=\mathbb E(IY)$, $L=\mathbb EZ$,
$D=\mathbb E(JZ)$ and $A=L+(3/5)D$, their empirical-to-population
padding is $.0025$ for $M$, $.004$ for $C,L,D,A$, and $.006$ for
$C-D$. Passing these gates does not establish equilibrium preparation.

## 2. Error budgets and means

Write

$$
 b_0=.0000775001,\qquad \kappa=\frac1{10000},\qquad
 B=b_0+\kappa=.0001775001,
 \tag{3}
$$

where $b_0$ is the frozen target budget for preparation, field, timing
and initial-instrument disturbance at their original $10^{-5}$
allowances. The kinetic term is the integrated generator row-TV bound
on each two-tick protocol, including the admitted timing errors. The
kinetic perturbation theorem supplies a sufficient physical condition
for (3): one fixed perturbed generator at each actual plateau, shared
across both protocols, with the same Gibbs stationary law and detailed
balance. Its full signed generator-row half-$\ell_1$ difference is
integrated over both dwell times. Alternatively, the statistical argument applies directly
whenever each actual target joint law is within $B$ of the corresponding
nominal noisy target law. Each model's detector channel contracts these
TV bounds.

The ordinary model already allows arbitrary detailed-balance kernels;
it has no heat-bath-rate restriction to relax. Its execution displacement
remains $b_R=.00002$. For the additional observed-law allowance
$e=.0002$, its total displacement from a stationary ordinary reference
is

$$
 E_R=b_R+e=.00022.
 \tag{4}
$$

The target kinetic charge and null prediction allowance have different
roles. The allowance $e$ enlarges the null and is not charged again to
the target. A target kinetic perturbation need not itself belong to
the ordinary null class.

The frozen local stationary inequality and tangent identity are

$$
 R<.00007,\qquad
 R=T+\left(M-\frac15\right)\left(A-\frac25\right).
 \tag{5}
$$

Here $R=(3/5)(C-D-L+MD)+ML$, and the stationary identity uses a
common initial marginal across protocols. It holds for all ordinary
models with at most three states under the inherited stationary
imbalance, field-tilt and tilt-error promises. The identity uses
cancellation of the two opposite initial-bit corrections in (1).

For an actual null inside the population gates, enlarge the four moment
intervals by $2E_R$, the $A$ interval by $3.2E_R$, and the $C-D$
interval by $4E_R$. These enlarged intervals remain in the frozen
stationary box

$$
 [.20,.24]\times[.45,.50]\times[.11,.14]\times[.46,.52],
 \qquad -.04<C-D<-.001.
 \tag{6}
$$

They also retain $M>1/5$ and $A>2/5$. In particular the enlarged
upper endpoint for $C-D$ is $-.002+4E_R=-.00112$. The remainder
in (5) is positive, so the stationary reference score is below $.00007$.

The exact score widths are $w_A=2$, $w_B=44/25$, with sum $94/25$.
Transfer the entire corrected score, including the initial-bit terms:

$$
 \mathbb E\widehat T<.00007+\frac{94}{25}E_R
 =\frac{2243}{2500000}=.0008972=:R_N.
 \tag{7}
$$

Nearby observed laws need not have equal initial marginals. Cancellation
is used only at the stationary reference; transferring the whole score
makes (7) valid without imposing equality on an approximate null law.

The nominal target score is uniformly above $.0041835$ over both
detector-error intervals. Hence the enlarged target family satisfies

$$
 \mathbb E\widehat T>.0041835-\frac{94}{25}B
 =.003516099624>.003516=:R_T.
 \tag{8}
$$

This uses the same whole-score transfer. It therefore does not require
the perturbed law to preserve nominal moment relations or zero initial
means exactly.

## 3. Variance bounds remain small

Inside the population gates, the approximate null's initial recorded
means obey

$$
 |\mathbb EI|,|\mathbb EJ|\le10^{-4}+2E_R
 =.00054.
 \tag{9}
$$

This follows by transferring the stationary low-field imbalance promise
through the detector and the full joint-table displacement. For a score
$X=aY+bIY+gI$, its exact variance is

$$
 V(a,b,g;M,C,i)=a^2+b^2+g^2+2ab i+2ag C+2bg M
 -(aM+bC+gi)^2.
 \tag{10}
$$

Use $(a,b,g)=(2/5,3/5,-3/10)$ in the first arm and
$(-2/5,-12/25,3/10)$ in the second. On the unchanged population
gates with (9), the first score mean is positive and the second negative.
Differentiating (10) consequently shows, in each arm, that the variance
decreases in both recorded moments and increases in the initial mean.
The maximum is therefore at the two lower moment endpoints and
$i=.00054$. Exact substitution gives respectively values below
$.297793$ and $.258957$, so the frozen null ceilings $.299,.260$
still apply.

If two score laws differ by TV $b$ and the score width is $w$, their
variances differ in the direction needed here by at most $w^2b$.
Indeed, center the second moment at the old mean, use the TV expectation
bound for that squared deviation, and then minimize over the new
centering. The frozen proof already bounds the nominal worst-contrast
variances plus $w^2b_0$ by $.289,.252$. Replacing $b_0$ by $B$ gives
the following convenient deterministic ceilings:

| Law | $\operatorname{Var}(X_A)$ upper | $\operatorname{Var}(X_B)$ upper |
|---|---:|---:|
| Actual null inside the population gates | .299 | .260 |
| Every enlarged physical target | .290 | .253 |

For the target the increases are at most $4\kappa=.0004$ and
$(44/25)^2\kappa=.00030976$, both covered by the displayed rounding.
These are population bounds, not estimated sample variances.

## 4. Size and power at the fixed allocation

For $n=2{,}500{,}000$ trials per arm, define

$$
 V_N=\frac{.299+.260}{n},\quad
 V_T=\frac{.290+.253}{n},\quad W=\frac2n,\qquad
 \mathcal B(V,W,x)=\sqrt{2Vx}+\frac{Wx}{3}.
 \tag{11}
$$

The inherited bounded-variable Bernstein inequality bounds the
appropriate one-sided score deviation at this radius by $e^{-x}$.
Exact squared rational inequalities certify

$$
 R_N+\mathcal B(V_N,W,3)<.002057<.0022
 <.002326<R_T-\mathcal B(V_T,W,13/4).
 \tag{12}
$$

The first inequality establishes size below $e^{-3}<.05$ whenever
the fixed null lies inside all population gates. If it lies outside one,
passing that empirical gate alone has probability bounded by one of

$$
 e^{-n(.0025)^2/2},\quad
 e^{-n(.004)^2/2},\quad
 e^{-n(.004)^2/(2\cdot1.6^2)},\quad
 e^{-n(.006)^2/4},
 \tag{13}
$$

all below $.05$. The two cases are alternatives for a fixed law; their
probabilities are not added.

For the target, use the positive gate distances

$$
 d_M=.004-2B-10^{-20},\qquad
 d_A=.006-3.2B-10^{-20},\qquad
 d_Q=.009-4B-10^{-20}.
 \tag{14}
$$

The first applies to all four scalar moments. The last uses the inherited
nominal interval $-.019<C-D<-.017$; the small buffers cover exact
center-enclosure errors. The joint gate-failure probability obeys

$$
 G\le8e^{-nd_M^2/2}
 +2e^{-nd_A^2/(2\cdot1.6^2)}
 +2e^{-nd_Q^2/4}<2\cdot10^{-6}.
 \tag{15}
$$

Combining (12) and (15), the miss probability is below
$e^{-13/4}+2\cdot10^{-6}<.040002<.05$. Thus both asserted error
guarantees hold uniformly over the enlarged physical target and null
families, with no normal approximation or detector inversion.

The comparison remains one of two joint snapshot laws under the
stated state-count, stationary, preparation and detector promises.
It does not establish full path-law equivalence or certify those
promises from the score data themselves.
