# Two million trials at the weaker field

The weaker-field experiment admits a **two-million-trial** test using a
small table of integer scores and the same two initial--final readouts.
It has false rejection below $5\%$ and power above $95\%$, uniformly over
the stated physical allowances and unknown independent symmetric detector
errors. Allowing the ordinary null an additional observed joint-table TV
error of $10^{-4}$ per protocol is certified with **2.5 million trials**.

The change is physically simple: keep $J=\log3$, set $H=\log2$, and use
the same dwell time $5/4$ at both fields. Both experiments still start
from the common low-field preparation; their chronological words are
$0H$ and $H0$. No extra observation, preparation, field, or protocol is
used. The target detector errors may be any fixed values in $[0,.01]$;
ordinary rivals may choose any values in $[0,1/2]$. These channels may
differ between target and rival hypotheses.

These are sufficient measurement budgets, not optimal sample complexity
or a laboratory feasibility claim. The physical promises, freshly
prepared independent trials, and common instrument remain substantive.
Manuscript drafting remains deferred.

**Status:** the analytic argument has passed independent internal review,
and its numerical premises are certified by exact arithmetic. This is
not external peer review.

[Physical and stationary certificate](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md)
· [Exact verifier](../scripts/verify_switch_weak_field.py)
· [Certificate report](../reports/switch_weak_field.json)
· [Source and comparison audit](FAMILIAR_SWITCH_WEAK_FIELD_SOURCE_AUDIT.md)
· [Statistical source audit](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_SOURCE_AUDIT.md)
· [Old-design necessary cost](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md).

## 1. The fixed test

Write $(I,Y)$ for the initial and final recorded bits in protocol $A=0H$
and $(J,Z)$ for those in protocol $B=H0$. Let

$$
 M=\mathbb EY,\quad C=\mathbb E(IY),\quad
 L=\mathbb EZ,\quad D=\mathbb E(JZ),\quad A=L+\frac35D.
 \tag{1}
$$

Assign these integer scores before collecting data. Columns list the
initial and final recorded signs, in that order.

| Protocol | $(+,+)$ | $(+,-)$ | $(-,+)$ | $(-,-)$ |
|---|---:|---:|---:|---:|
| $A$: $50X_A$ | 35 | -65 | 5 | 25 |
| $B$: $50X_B$ | -29 | 59 | -11 | -19 |

Equivalently,

$$
 X_A=\frac{20Y+30IY-15I}{50},\qquad
 X_B=\frac{-20Z-24JZ+15J}{50},\qquad
 \widehat T=\overline X_A+\overline X_B-\frac2{25}.
 \tag{2}
$$

Average the two arms separately and add their means. The rule rejects
only if every empirical gate below passes and the score exceeds the
specified threshold.

| Null class | Trials per arm | Total trials | Score threshold |
|---|---:|---:|---:|
| Admissible ordinary model with at most three states | 1,000,000 | **2,000,000** | 0.002 |
| Observed laws within joint-table TV $10^{-4}$ per arm of such a model | 1,250,000 | **2,500,000** | 0.00218 |

Every trial uses two binary readouts: the budgets are respectively
**four million** and **five million** binary readouts. The active
two-field evolution lasts $5/2$ time units per trial; preparation time
and calibration acquisition costs are not priced.

Let $m_*,c_*,\ell_*,d_*$ denote the new candidate's exact dyadic target
centers in the [certificate report](../reports/switch_weak_field.json),
each with enclosure radius $2^{-120}$. Define

$$
 M_*={49\over50}m_*,\quad C_*={2401\over2500}c_*,\quad
 L_*={49\over50}\ell_*,\quad D_*={2401\over2500}d_*,\quad
 A_*=L_*+\frac35D_*,\quad a_*=\ell_*+\frac35d_*.
 \tag{3}
$$

Only the gates use these certificate constants; the score table is
entirely rational with small integer entries.

| Quantity | Empirical gate | Larger population gate |
|---|---|---|
| $M$ | $[M_*-.004,m_*+.004]$ | $[M_*-.0065,m_*+.0065]$ |
| $C$ | $[C_*-.004,c_*+.004]$ | $[C_*-.008,c_*+.008]$ |
| $L$ | $[L_*-.004,\ell_*+.004]$ | $[L_*-.008,\ell_*+.008]$ |
| $D$ | $[D_*-.004,d_*+.004]$ | $[D_*-.008,d_*+.008]$ |
| $A$ | $[A_*-.006,a_*+.006]$ | $[A_*-.010,a_*+.010]$ |
| $C-D$ | $[-.03,-.008]$ | $[-.036,-.002]$ |

The population gates are proof devices. Empirical gates use the four
moment estimates in (1); the score also uses the already recorded
initial bits. Passing the gates does not certify equilibrium preparation.

## 2. A positive tangent remainder makes the null bound simple

For $u_0=3/5$ define the recorded-coordinate witness

$$
 R=u_0(C-D-L+MD)+ML.
 \tag{4}
$$

The [weaker-field stationary certificate](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md)
proves the following local
necessary condition. Under $|v|\le10^{-4}$,
$|u-u_0|\le10^{-4}$, and stationary tilt TV error at most $10^{-5}$,
every admissible stationary ordinary model with at most three states
obeys

$$
 R<.00007
 \tag{5}
$$

whenever its recorded moments lie in

$$
 .20\le M\le.24,\quad .45\le C\le.50,\quad
 .11\le L\le.14,\quad .46\le D\le.52,\quad
 -.04\le C-D\le-.001.
 \tag{6}
$$

The condition allows arbitrary initial and final detector contrasts in
$[0,1]$ and does not invert them. Its proof minimizes the cleared
minus-singleton polynomial over the contrast square; the plus-singleton
branch is excluded by its contrast-corner signs. Thus it applies to
the full ordinary class specified here, not only a selected competitor.

For any law with a common initial marginal across the two protocols,
the opposite initial-bit corrections in (2) cancel in expectation.
Direct expansion gives the exact identity

$$
 R=T+\left(M-\frac15\right)\left(A-\frac25\right),
 \qquad T=\mathbb E\widehat T.
 \tag{7}
$$

No independence of the two bits within a trial is assumed. The common
initial marginal follows from the existing common preparation,
initial instrument and detector-channel promises.

Use the newly certified physical table-displacement budgets

$$
 b_T=.0000775001,\qquad b_R=.00002,\qquad E_R=b_R+e.
 \tag{8}
$$

The target budget includes preparation, field, timing and instrument
allowances of $10^{-5}$ each. Its shorter-duration field term is
$(7/4+\epsilon_t)\epsilon_h$; adding $4\epsilon_t+\epsilon_p+\xi$
gives the displayed $b_T$. The rival budget covers preparation and the
initial instrument. All budgets contract through each model's own
channel. The extra $e$ is an observed joint-table TV enlargement of
the null alone.

If an actual null lies inside the population gates, its stationary
reference differs by at most $2E_R$ in each of $M,C,L,D$, by $3.2E_R$
in $A$, and by $4E_R$ in $C-D$. For both allocations, the enlarged
population box lies in (6) and satisfies $M>1/5$, $A>2/5$. The
remainder in (7) is therefore positive, and stationary $T<.00007$.

The exact score widths are $w_A=2$ and $w_B=44/25=1.76$. Transfer
the whole corrected score by TV, including the initial-bit terms:

$$
 \mathbb E\widehat T<.00007+(w_A+w_B)E_R
 =\begin{cases}.0001452,&e=0,\\ .0005212,&e=10^{-4}.
 \end{cases}
 \tag{9}
$$

The nearby observed laws need not have matching initial marginals.
Cancellation is used only for the stationary reference; transferring
the entire score is what makes (9) valid for the enlarged null.

## 3. The target floor and variance bounds

For nominal target contrasts $a,b\in[.98,1]$, the expectation is

$$
 T(a,b)=b\left[\frac25(m_*-\ell_*)
            +a\left(\frac35c_*-\frac{12}{25}d_*\right)\right]
            -\frac2{25},
 \tag{10}
$$

up to the explicitly bounded target-center error. Both contrast
derivatives are positive. The minimum is at $a=b=.98$, where
$T\approx.004183547589$. The exact enclosure gives $T>.0041835$.
Thus every allowed physical target satisfies

$$
 \mathbb E\widehat T>.0041835-3.76b_T>.003892.
 \tag{11}
$$

For variance calculations put $q=2/5$, $u=3/5$, $p=-2/5$,
$k=-12/25$, $\gamma=3/10$, and let $i=\mathbb EI$, $j=\mathbb EJ$.
The exact first and second moments are

$$
 \begin{split}
 \mu_A&=uC+qM-\gamma i,\\
 \mathbb EX_A^2&=u^2+q^2+\gamma^2+2uq i-2u\gamma M-2q\gamma C,\\
 \mu_B&=pL+kD+\gamma j,\\
 \mathbb EX_B^2&=p^2+k^2+\gamma^2+2pk j+2p\gamma D+2k\gamma L.
 \end{split}
 \tag{12}
$$

For actual nulls, $|i|,|j|\le10^{-4}+2E_R\le.00034$. Inside the
population gates, $\mu_A>0$ and $\mu_B<0$. Subtracting the squared
means in (12), the first variance decreases with $M,C$ and increases
with $i$; the second decreases with $L,D$ and increases with $j$.
Their maxima are bounded by substituting the lower moment endpoints
and the upper initial-mean endpoint.

Nominal targets have $i=j=0$. Each variance decreases with both
contrasts, hence is largest at $a=b=.98$. A table displacement of TV
$b_T$ increases the variance of a score of width $w$ by at most
$w^2b_T$: center at its old mean, use the TV expectation bound for
the squared deviation, and then minimize over the new centering.
Exact substitution yields common deterministic ceilings:

| Distribution class | $\operatorname{Var}(X_A)$ upper | $\operatorname{Var}(X_B)$ upper |
|---|---:|---:|
| Either actual null, inside the population gates | .299 | .260 |
| Every allowed physical target | .289 | .252 |

These are population bounds, not estimated sample variances.

## 4. Uniform size and power

For independent arm averages with $n$ trials each, set

$$
 V=\frac{v_A+v_B}{n},\qquad W=\frac2n,\qquad
 \mathcal B(V,W,x)=\sqrt{2Vx}+\frac{Wx}{3}.
 \tag{13}
$$

The bounded-variable Bernstein argument in the
[earlier score proof](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md)
gives a one-sided deviation probability at most $e^{-x}$ at this
radius. The two records within a trial remain dependent throughout.

For size, if a fixed actual null lies outside a population gate,
passing the corresponding empirical gate has probability at most one
of

$$
 e^{-n(.0025)^2/2},\qquad
 e^{-n(.004)^2/2},\qquad
 e^{-n(.004)^2/(2\cdot1.6^2)},\qquad
 e^{-n(.006)^2/4}.
 \tag{14}
$$

These respectively cover $M$, the other three scalar moments, $A$,
and the cross-arm difference $C-D$. All are below $.05$ already
at $n=10^6$. Choosing one violated population gate for a fixed law
requires no union over the possible violations.

If the null instead lies inside every population gate, (9) and the
variance ceilings give size below $e^{-3}<.05$, because

$$
 R_N+\mathcal B(V_N,W,3)<t
 \tag{15}
$$

for the corresponding mean bound $R_N$ and threshold $t$. The
inside and outside cases are alternatives, so the size bound is their
maximum, not their sum.

For power, safe distances of the physical target from the empirical
gate edges are

$$
 d_M=.004-2b_T-10^{-20},\qquad
 d_A=.006-3.2b_T-10^{-20},\qquad
 d_Q=.009-4b_T-10^{-20}.
 \tag{16}
$$

The first distance applies to all four scalar moments. The last uses
the certified nominal interval $-.019<C-D<-.017$. The small buffers
cover the dyadic-center errors. A union bound gives

$$
 G=8e^{-nd_M^2/2}
   +2e^{-nd_A^2/(2\cdot1.6^2)}
   +2e^{-nd_Q^2/4}<.01.
 \tag{17}
$$

Numerically $G<.0081$ at one million trials per arm and $G<.0014$
at 1.25 million per arm; these displayed comparisons are certified
with exact exponential bounds. Finally,

$$
 t<.003892-\mathcal B(V_T,W,13/4)
 \tag{18}
$$

gives score failure probability below $e^{-13/4}<.04$. Combining
it with (17) proves power above $.95$ for both rows. No normal
approximation or fitted variance is used.

## 5. A design advantage beyond improving the old statistic

The frozen [detector information-cost proof](FAMILIAR_SWITCH_DETECTOR_INFORMATION_COST.md)
concerns the old operating point $u=4/5$, with dwell times $3/2$.
At its target with exactly one-percent error in both detector uses,
every test restricted to its two protocols with both errors at most
$5\%$ needs

$$
 \mathbb E_*N>810000\log19>2{,}384{,}995,
 \tag{19}
$$

even with adaptive arm selection and stopping. In contrast, the new
operating point has a fixed two-million-trial test that covers that
same detector-error value, indeed every target error in $[0,.01]$.
Both designs use the same physical four-state model with $J=\log3$,
the same two word orders, and the same form of physical and readout
resource promises at their respective field values. The nulls are
defined at the respective nominal fields; they are not literally
the same fixed-field set of laws.

Thus the simpler field and timing change gives a sufficient trial
count smaller than a necessary count for every test using the old
two protocols. It demonstrates an experimental-design advantage
beyond merely improving the statistic at the old design. It is not
a global design optimum, a Blackwell ordering of the experiments,
or a bound on total laboratory time. Active dwell time also decreases
from $3$ to $5/2$ per trial, while preparation overhead remains outside
the comparison.

The 2.5-million row also allows prediction error $10^{-4}$, larger
than the general three-state predictor's constructive physical
allowance $2\cdot10^{-5}$. The result concerns the two joint snapshot
laws and their stated model class. It does not establish full
multitime-law equivalence, an unpromised instrument model, or PRL
readiness.
