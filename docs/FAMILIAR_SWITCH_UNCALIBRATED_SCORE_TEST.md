# A simple score test with unknown detector errors

The detector-unknown witness admits a substantially cheaper fixed test.
Assign an integer score to each recorded bit pair, average separately
over the same two protocols, and compare their sum with a fixed threshold.
The sufficient cost is **32 million paired-snapshot trials**, including
the existing preparation, control and instrument allowances. Enlarging
the null by observed joint-table TV error $`e=10^{-4}`$ costs **90 million
trials**. Both allocations give false rejection below $`5\%`$ and power
above $`95\%`$. These are sufficient costs, not optimized sample complexity
or a laboratory feasibility assessment.

The target electronics may have any fixed independent symmetric error
probabilities in $`[0,0.01]`$; competing models may choose any such
probabilities in $`[0,1/2]`$. Neither probability is estimated or inverted.
The independent symmetric channel form, common preparation and instrument,
stationary force-law promise, and independent freshly prepared trials
remain assumptions. No new measurement or control protocol is introduced.

**Status:** the analytic argument and exact numerical checks have passed
independent internal review. This is not external peer review.
[Underlying witness and physical allowances](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md)
· [Snapshot concentration argument](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md)
· [Frozen target moments](../reports/switch_snapshot_design.json)
· [Exact verifier](../scripts/verify_switch_uncalibrated_score.py)
· [Certificate report](../reports/switch_uncalibrated_score.json)
· [Necessary information cost](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md)
· [Statistical source audit](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md).

## 1. The test is an integer lookup table

Protocol $`A`$ applies the chronological field word $`0,H`$ and records the
initial and final binary values $`(I,Y)`$. Protocol $`B`$ applies $`H,0`$ and
records $`(J,Z)`$. Both use the common low-field preparation. Define

**Equation (1).**

```math
 M=\mathbb EY,\quad C=\mathbb E(IY),\quad
 L=\mathbb EZ,\quad D=\mathbb E(JZ),\quad A=L+\frac45D.
```

Use the following table, fixed before sampling. The first sign in each
column is the initial record and the second is the final record.

| Protocol | $`(+,+)`$ | $`(+,-)`$ | $`(-,+)`$ | $`(-,-)`$ |
|---|---:|---:|---:|---:|
| $`A`$: integer score $`25X_A`$ | 23 | -43 | 3 | 17 |
| $`B`$: integer score $`25X_B`$ | -12 | 32 | -8 | -12 |

Equivalently,

**Equation (2).**

```math
 X_A=\frac{(13+20I)Y-10I}{25},\qquad
 X_B=\frac{-(10+12J)Z+10J}{25},\qquad
 \widehat T=\overline X_A+\overline X_B-\frac{26}{125}.
```

The two arms need not have equal sample counts. Their averages enter
with equal coefficient as written; pooling all integer scores would
define a different statistic. Every trial contains two readouts.

| Null class | $`n_A`$ | $`n_B`$ | Total trials | Reject if $`\widehat T\gt`$ |
|---|---:|---:|---:|---:|
| Admissible ordinary model with at most three states | 18,560,000 | 13,440,000 | 32,000,000 | 0.00079 |
| Observed laws within joint-table TV $`10^{-4}`$ of such a model | 52,200,000 | 37,800,000 | 90,000,000 | 0.001 |

Rejection also requires the empirical gates below. Let $`m_*,c_*,\ell_*,d_*`$
be the fixed dyadic centers of the frozen target certificate, in that
order. Their enclosure radius is $`2^{-120}`$. Set

**Equation (3).**

```math
 M_*=\frac{49}{50}m_*,\quad C_*=\frac{2401}{2500}c_*,\quad
 L_*=\frac{49}{50}\ell_*,\quad D_*=\frac{2401}{2500}d_*,\quad
 A_*=L_*+\frac45D_*,\quad a_*=\ell_*+\frac45d_*.
```

Only these gate endpoints use target-certificate constants. The score
itself is the integer table above.

| Quantity | Empirical gate | Larger population gate |
|---|---|---|
| $`M`$ | $`[M_*-0.0012,\ m_*+0.0012]`$ | $`[M_*-0.002,\ m_*+0.002]`$ |
| $`A`$ | $`[A_*-0.0023,\ a_*+0.0023]`$ | $`[A_*-0.004,\ a_*+0.004]`$ |
| $`C`$ | $`[C_*-0.002,\ c_*+0.002]`$ | $`[C_*-0.004,\ c_*+0.004]`$ |
| $`L`$ | $`[L_*-0.002,\ \ell_*+0.002]`$ | $`[L_*-0.004,\ \ell_*+0.004]`$ |
| $`D`$ | $`[D_*-0.002,\ d_*+0.002]`$ | $`[D_*-0.004,\ d_*+0.004]`$ |
| $`C-D`$ | $`[-0.046,-0.0345]`$ | $`[-0.05,-0.0305]`$ |

The population gates are proof devices, not additional observations.
The gates use the sample averages of the four moments in (1); the scores
also use the already recorded initial bits. Passing these gates is not
an equilibrium-preparation certification.

## 2. A sharper necessary bound for the unknown-channel null

Retain the stationary bias, force and approximate-tilt allowances

**Equation (4).**

```math
 |v|\le10^{-4},\qquad |u-4/5|\le10^{-4},\qquad
 \mathrm{TV}\!\left(\eta,\frac{\pi(1+uS)}{1+uv}\right)\le10^{-5}.
```

Every ordinary model with at most three states has a singleton readout
sector. The underlying witness proves that its detector-cleared biased
polynomial $`J_\sigma`$ satisfies $`|J_\sigma|\le\Gamma_\sigma`$ for its
singleton sign, with $`\Gamma_-\lt 0.000054`$ and $`\Gamma_+\lt 0.000481`$.
The contrasts $`r_0,r_f`$ remain unrestricted in $`[0,1]`$.

We use the following local recorded-coordinate box:

**Equation (5).**

```math
 .4\le M\le.42,\quad .32\le C\le.35,\quad
 .21\le L\le.24,\quad .36\le D\le.4,\quad
 -.06\le C-D\le-.03.
```

On this box the minus polynomial attains its minimum over the entire
contrast square at $`(r_0,r_f)=(1,1)`$. Here is the direct argument.
It is affine in $`r_0`$, and its two endpoint polynomials are

**Equation (6).**

```math
 \begin{split}
 J_-(0,r_f)&=uMD+ur_f(C-D-vC),\\
 J_-(1,r_f)&=uMD+ML+r_f\{u(C-D-L)\\
 &\hspace{28mm}-v[(1-u)L+uC+(1+u)M]\}
                  +r_f^2(vu+v^2).
 \end{split}
```

Both decrease strictly with $`r_f`$ throughout (4)--(5), as follows by
bounding their derivatives at $`r_f=0,1`$. Moreover,

**Equation (7).**

```math
 J_-(0,1)-J_-(1,1)
 =(u-M)L-v[(u-1)L-(1+u)M+u]-v^2\gt 0.
```

Thus $`J_-(r_0,r_f)\ge J_-(1,1)`$, without dividing by any contrast.
Write $`R_u=u(C-D-L+MD)+ML`$ and define

**Equation (8).**

```math
 B_u=(u-1)L-uC-(1+u)M+u.
```

Then $`J_-(1,1)=R_u+vB_u+v^2`$. On (4)--(5),
$`|\partial_uR_u|\lt 0.157`$ and $`|B_u|\lt 0.285`$. Consequently a minus
singleton branch implies, at the fixed analysis value $`u_0=4/5`$,

**Equation (9).**

```math
 R:=R_{u_0}
 \lt 0.000054+0.157\cdot10^{-4}+0.285\cdot10^{-4}+10^{-8}
 \lt 0.0001.
```

For a plus singleton branch, the earlier local bound gives
$`|K_+|\lt 0.001`$ for some contrasts. If $`R\ge0.0001`$ on (5), all four
contrast corners instead satisfy $`K_+\lt -0.048`$: the first three use
$`u_0MD\gt 0.048`$ and $`C\lt D`$, and the last is
$`2u_0(C-D)-R\lt -0.048`$. Bilinear interpolation rules out this branch
as well. Therefore **every admissible stationary ordinary model with
at most three states lying in (5) obeys $`R\lt 0.0001`$**, regardless of
its independent symmetric detector error probabilities.

This argument sharpens a necessary local bound; it does not identify
the globally closest ordinary model or the optimized separation.

## 3. The tangent and the free variance reduction

Let $`T`$ denote the expectation of (2) under a law whose initial marginal
is shared across protocols. Direct expansion gives

**Equation (10).**

```math
 R=T+\left(M-\frac25\right)\left(A-\frac{13}{25}\right).
```

The opposite initial-bit terms in (2) cancel in expectation because
$`\mathbb EI=\mathbb EJ`$. This is already implied by the common
preparation, initial instrument and electronic channel assumptions.
Their inclusion reduces the variance by using the correlation of the
initial record with the uncorrected score. It adds no assumption that
the two records within a trial are independent.

For nearby observed laws in the second row, the initial marginals need
not agree. We therefore transfer the **entire corrected score** by TV,
including the initial-bit terms; no cancellation is assumed for such
arbitrary nearby laws. The exact score range widths are

**Equation (11).**

```math
 w_A=\frac{66}{25}=2.64,\qquad w_B=\frac{44}{25}=1.76,
 \qquad w_A+w_B=\frac{22}{5}=4.4.
```

Use the inherited physical displacement bounds

**Equation (12).**

```math
 b_T=0.0000800001,\qquad b_R=0.00002,\qquad E_R=b_R+e.
```

The target budget includes preparation, field, timing and initial
instrument allowances; the rival budget includes preparation and
instrument allowances. Each is contracted by the model's own channel.
The extra $`e`$ is observed joint-table TV distance per arm and is added
only to the null. No detector inverse occurs.

If an actual null lies inside the population gates, its stationary
reference moments differ by at most $`2E_R`$ individually and by
$`3.6E_R`$ in $`A`$. For both rows their enlarged gate box lies inside (5).
Throughout that enlarged box $`M\gt 2/5`$, and hence

**Equation (13).**

```math
 -\left(M-\frac25\right)\left(A-\frac{13}{25}\right)
 \le q(E_R):=
 \left(m_*+0.002+2E_R-\frac25\right)
 \left(\frac{13}{25}-A_*+0.004+3.6E_R\right).
```

The right-hand side is positive for the two stated rows. Equations
(9)--(13) imply the following uniform actual-score mean bounds:

**Equation (14).**

```math
 \mathbb E\widehat T\lt 0.0001+q(E_R)+4.4E_R
 \lt \begin{cases}0.000229,&e=0,\\0.000676,&e=10^{-4}.\end{cases}
```

For the nominal target with initial and final contrasts $`a,b\in[.98,1]`$,
the score mean is

**Equation (15).**

```math
 T(a,b)=b\left[\frac{13}{25}m_*-\frac25\ell_*
       +\frac45a\left(c_*-\frac35d_*\right)\right]-\frac{26}{125},
```

up to the explicitly bounded target-center enclosure error. Both its
$`a`$ and $`b`$ derivatives are positive. Its minimum occurs at
$`a=b=.98`$, where $`T\approx0.00169944523`$. Exact interval evaluation gives
$`T\gt 0.0016994`$, so every physically allowed target obeys

**Equation (16).**

```math
 \mathbb E\widehat T\gt 0.0016994-4.4b_T\gt 0.001347.
```

## 4. Range and variance bounds

Put $`u=4/5`$, $`q=13/25`$, $`p=-2/5`$, $`k=-12/25`$, $`\gamma=2/5`$,
and denote the two initial means by $`i,j`$. The exact score means and
second moments are

**Equation (17).**

```math
 \begin{split}
 \mu_A&=uC+qM-\gamma i,\\
 \mathbb EX_A^2&=u^2+q^2+\gamma^2+2uq i-2u\gamma M-2q\gamma C,\\
 \mu_B&=pL+kD+\gamma j,\\
 \mathbb EX_B^2&=p^2+k^2+\gamma^2+2pk j+2p\gamma D+2k\gamma L.
 \end{split}
```

Subtract $`\mu_A^2`$ and $`\mu_B^2`$ for the variances. Every actual null
has $`|i|,|j|\le10^{-4}+2E_R\le0.00034`$. This includes the arbitrary
observed-law enlargement in the second row. On the population gates,
$`\mu_A\gt 0`$ and $`\mu_B\lt 0`$. The first variance decreases in $`M,C`$ and
increases in $`i`$; the second decreases in $`L,D`$ and increases in $`j`$.
Their maxima therefore occur at the respective lower coordinate
endpoints and the upper initial-mean endpoint. Exact substitution gives
the common null ceilings below.

For the nominal targets $`i=j=0`$; each variance decreases with both
contrasts, so its maximum is at $`a=b=.98`$. Under a further table
displacement $`b_T`$, a score of width $`w`$ has variance at most its old
variance plus $`w^2b_T`$: center at the old mean and bound the oscillation
of the squared deviation by $`w^2`$. This yields

| Distribution class | $`\mathrm{Var}(X_A)`$ upper | $`\mathrm{Var}(X_B)`$ upper |
|---|---:|---:|
| Either actual null, inside the population gates | 0.452 | 0.280 |
| Any allowed physical target | 0.444 | 0.275 |

These are deterministic ceilings, not fitted sample variances.

## 5. Uniform size and power

For two independent arm averages with variance ceilings $`v_A,v_B`$,
define

**Equation (18).**

```math
 V=\frac{v_A}{n_A}+\frac{v_B}{n_B},\qquad
 W=\max\left\{\frac{w_A}{n_A},\frac{w_B}{n_B}\right\},\qquad
 \mathcal B(V,W,x)=\sqrt{2Vx}+\frac{Wx}{3}.
```

The bounded-variable Bernstein derivation in the earlier snapshot score
note gives each one-sided deviation probability at most $`e^{-x}`$ at
this radius. It accommodates the two different sample counts and
retains dependence of the two bits within each trial.

For size, first suppose an actual null lies outside the larger population
gates. Passing its corresponding empirical gate has probability at most
one of

**Equation (19).**

```math
 e^{-n_A(0.0008)^2/2},\quad
 e^{-n_B(0.0017)^2/(2\cdot1.8^2)},\quad
 e^{-\min(n_A,n_B)(0.002)^2/2},\quad
 e^{-(0.004)^2/[2(1/n_A+1/n_B)]}.
```

Every bound is below $`0.05`$ already at the smaller allocation. For a
fixed distribution, choose any violated population gate; no union
over all possible violated gates is needed. If the actual null instead
lies inside all population gates, (14) and the null variance ceilings
give rejection probability below $`e^{-3}\lt 0.05`$, because

**Equation (20).**

```math
 R_N+\mathcal B(V_N,W,3)\lt t
```

for both rows. Here $`R_N`$ is the corresponding bound in (14), and $`t`$
is its fixed threshold. These outside and inside cases are alternatives,
so their error probabilities are maximized, not added.

For power, each physically perturbed target remains a positive distance
inside every empirical gate. Safe lower distances are

**Equation (21).**

```math
 d_M=0.0012-2b_T-10^{-20},\quad
 d_A=0.0023-3.6b_T-10^{-20},\quad
 d_C=0.002-2b_T-10^{-20},\quad
 d_Q=0.0044-4b_T-10^{-20}.
```

The last uses the certified nominal interval
$`-.0406\lt C-D\lt -.0389`$; either edge of the empirical difference gate is
at least $`0.0044`$ away. The sum of gate-failure probabilities is bounded by

**Equation (22).**

```math
 \begin{split}
 G={}&2e^{-n_Ad_M^2/2}
 +2e^{-n_Bd_A^2/(2\cdot1.8^2)}
 +2e^{-n_Ad_C^2/2}+4e^{-n_Bd_C^2/2}\\
 &+2e^{-d_Q^2/[2(1/n_A+1/n_B)]}\lt 0.001.
 \end{split}
```

The target score itself fails its threshold with probability at most
$`e^{-13/4}\lt 0.04`$, since

**Equation (23).**

```math
 t\lt 0.001347-\mathcal B(V_T,W,13/4).
```

A union bound gives failure probability less than $`0.041`$, hence power
above $`95\%`$. The concentration comparisons, gate containments,
variance bounds and finite target intervals are certified by exact
arithmetic; a Gaussian approximation is not used.

## 6. What has and has not improved

The 32-million allocation replaces the previous sufficient
508-million-trial detector-unknown test, a reduction by a factor of
$`15.875`$. The 90-million allocation additionally rejects every pair of
observed laws within TV $`10^{-4}`$ per table of the ordinary class. That
allowance exceeds the constructive general three-state approximation
error $`2\cdot10^{-5}`$, while remaining below the previously certified
ordinary recorded-table gap $`1/5000`$.

The first row uses 64 million binary readouts and the second 180 million.
Preparation waiting and any independent calibration work are additional.
The two protocols and short control sequence are unchanged. The earlier
1.2-million calibrated-detector cost describes a narrower null and is
not a valid comparison at fixed assumptions. Neither the new integer
score nor Bernstein concentration is a novelty claim; the contribution
here is the explicit uniform test for the enlarged physical model class.

Stationary preparation and a sufficiently gentle initial instrument are
still substantive premises. Passing the gates does not prove them, and
successive snapshots along one unreset trajectory do not supply the
independent trials used above. The exact three-state predictor concerns
these two joint laws, not complete multitime trajectory equivalence.
