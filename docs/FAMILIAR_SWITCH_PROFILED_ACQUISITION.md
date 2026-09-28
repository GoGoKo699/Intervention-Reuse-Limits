# Measuring the five-setting separation without numerical force calibration

[Repository](../README.md) · [Five-setting theorem](FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md) · [Earlier acquisition bounds](FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md) · [Verification](VERIFICATION.md)

The ideal five-setting experiment now admits a test with **50 million
endpoint-pair trials**, valid against every ordinary reversible predictor
with at most three states and an unknown numerical Gibbs tilt. Both error
probabilities are below 5%. A closer explicit reversible three-state rival
proves that any such fixed-budget test needs at least **2,849,458 pairs**,
even when it chooses the next setting adaptively from completed trials.

Thus this fixed design is **within a factor of 18 of the best possible
deterministic trial budget** for the declared five-setting, ideal-readout
problem. This is a certified bracket at one target, not a matching
asymptotic rate or an optimality claim. The sufficient count is twelve
times smaller than the preceding unknown-tilt confidence-box guarantee.
The lower bound replaces a particularly easy statically equivalent rival
by one that trades small errors across all five settings.

The test uses one scalar polynomial and a gate on the observed moments.
The physical experiment, ordinary-reversibility convention and counted
memory are unchanged. Preparation, initial-instrument and independent-trial
assumptions remain substantive; this acquisition bracket does not establish
laboratory feasibility.

## The same experiment and comparison class

Keep the two coupled heat-bath switches with $t=\tanh J=1/3$, low field
zero, high-field tilt $7/9$, equal unit attempt rates and unit dwell times.
The observed settings are $L,L^2,H,H^2,HL$, with chronological order in
$HL$. Every trial records the initial and final signs after a fresh common
preparation. Different complete trials are independent. The protocol is
selected before the current initial sign is observed; the two observations
within a trial are not assumed independent.

The ordinary null has at most three supported states, deterministic latent
binary readout, one common initial law $\rho_0$, and fixed stochastic tick
kernels $K_L,K_H$ reversible under the weights

$$
\omega_L=\rho_0,\qquad \omega_H=\rho_0(1+mS).
$$

The numerical tilt $m$ is now arbitrary in $(-1,1)$. Its Gibbs form remains
assumed. Zero unused masses, initial sign imbalance and arbitrary reversible
stochastic kernels are allowed. No rate cap, CTMC embedding, fixed hidden
architecture or exact match to a calibration setting is required by the
lower-state null. The physical alternative remains the nominal four-state
target. The existing general three-state exact predictor is unchanged.

This test does not infer the preparation or force-interface assumptions
from the observed data. The initial instrument still needs the joint
record/post-readout-state guarantee in the
[measurement note](FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md). A finite reset
bound for the target is not a reset guarantee for every arbitrarily slow
rival. The bounds here concern testing data, separately from acquisition
of instrument calibration, reset time and physical throughput.

## Eliminating the tilt before statistical testing

Write $e=\mathbb E S_0$ and

$$
(x,y,z,v,r)=(C_L,C_{L^2},C_H,C_{H^2},C_{HL}),\qquad
h=M_H,
$$

where $C_w=\mathbb E(S_0S_T\mid w)$ and $M_w=\mathbb E(S_T\mid w)$.
The null identity uses seven observable moments. The test also retains the
already-recorded per-setting initial means for linear zero-mean corrections;
no extra physical measurement is required. Let

$$
\begin{aligned}
g&=1-e^2,& k&=1-z,\\
A&=g(y-e^2)-(x-e^2)^2,\\
C&=g(r-e^2)-(x-e^2)(z-e^2),\\
D&=g(v-z)+k(z-eh).
\end{aligned}
$$

Stationarity under the high-field Gibbs weights gives

$$
h+mz=e+m,\qquad m=\frac{h-e}{1-z}
$$

whenever $k>0$. In the previously derived rank-one identity, put
$w=1+me$, $q=e+m$ and

$$
B=g(wv-eq)-(wz-eq)^2.
$$

Direct substitution and simplification give $B=wD$. Every ordinary null
with both visible signs and at most three supported states satisfies
$(1-sm)wC^2=AB$ for at least one sign $s\in\{-1,+1\}$. Consequently it
satisfies the **tilt-free observable identity**

$$
\boxed{G_s(e,x,y,z,v,r,h)
=[1-z-s(h-e)]C^2-(1-z)AD=0.}
$$

This is an identity for the whole unknown-tilt null, not the substitution
of a noisy tilt estimate into a known-tilt test. The sign labels the sector
that can contain the one-dimensional hidden residual. Squaring includes
both orientations and zero residuals. Locally around the target, $g,k,w$
and the denominators used in the derivation are positive. Degenerate or
distant null laws must be handled by the statistical gate; they cannot
silently be removed from the comparison class.

At balanced preparation the expression becomes particularly transparent:

$$
G_s=(1-z-sh)(r-xz)^2
-(1-z)(y-x^2)(v-z^2).
$$

The required field information is carried by the final mean $h$ already
available in the $H$ pair data. No extra preparation, control word or
intermediate measurement has been added.

The implementation removes one further exact polynomial factor:

$$
P_s=G_s/(1+se).
$$

Polynomial long division gives a degree-six polynomial with no remainder;
this is the definition of the registered score, evaluated as a polynomial.
Within the population box used below, $1+se>0$, so the true null branch also
satisfies $P_s=0$. No division is performed on empirical data. Degenerate
initial-sign laws outside that box are covered by the gate bound.

## A rigorous sufficient test

Take $N=10\,000\,000$ independent trials at each of the five settings.
Within each setting, compute the sample correlation; use the $H$ group's
final mean for $h$, and pool all $5N$ initial signs for $e$. Write the
seven resulting moments as $\widehat\theta$, in the order
$(e,x,y,z,v,r,h)$. Use the fixed rational center

```
(0,
 0.4301437920603036,
 0.19889257581808503,
 0.39401750008998393,
 0.16141460473347785,
 0.18419539300718862,
 0.4713197221522347)
```

The certificate encloses every exact target coordinate within $10^{-12}$
of this center $\theta_c$. Let $\widehat e_j$ be the initial mean in setting
$j$, ordered as $L,L^2,H,H^2,HL$, and fix

$$
(d_1,d_2,d_3,d_4,d_5)
=\frac{(-5104765,-5104765,-26817373,49710906,-12684003)}{10^{10}}.
$$

These coefficients sum to zero. Therefore $\sum_jd_j\widehat e_j$ has
mean zero for every common-preparation model, including the target. It
uses measurements already collected and reduces variance without fitting
anything to the acquired data.

Define

$$
T=P_+(\widehat\theta)+\sum_{j=1}^5d_j\widehat e_j.
$$

**Reject the entire at-most-three-state ordinary null exactly when both**

$$
\|\widehat\theta-\theta_c\|_\infty\le0.0013,
\qquad T<-0.0000125.
$$

Otherwise return inconclusive. There is no optional stopping or fitted
threshold in this sufficient design. The outcome counts determine the
statistic by exact rational arithmetic; no individual trajectories need
to be retained after counting the four paired outcomes in each setting.

### Why one sign branch is enough

Let $\mathcal B$ be the larger population box
$\|\theta-\theta_c\|_\infty\le R=0.0022$.
Exact shifted-polynomial interval evaluation proves

$$
P_-(\theta)>0.000024\qquad(\theta\in\mathcal B).
$$

Hence any null whose true moments are inside this box must satisfy
$P_+(\theta)=0$. Both hidden-residual orientations remain included in
that identity. Nulls outside the box will be controlled solely by the
empirical gate. This division concerns each fixed null's true moments;
it does not condition a concentration inequality on a selected dataset.

### The linear fluctuation and its actual pair covariance

Put $\xi=\widehat\theta-\theta$ and expand $P_+$ around the **true** moment
vector. Including the linear initial-mean correction, the random linear
term is $N^{-1}\sum_{j,i}(Z_{j,i}-\mathbb E Z_{j,i})$, where for a pair
$(S_0,S_T)$ in setting $j$,

$$
Z_j=a_jS_0+b_jS_0S_T+c_jS_T,
$$

$$
a_j=\partial_eP_+(\theta)/5+d_j,\quad
b_j=\partial_{C_j}P_+(\theta),\quad
c_j=\mathbf1_{j=H}\partial_hP_+(\theta).
$$

The derivatives are evaluated at the true moments for the proof; the
implemented statistic does not estimate or use them. The exact variance is

$$
\operatorname{Var} Z_j
=a_j^2+b_j^2+c_j^2+2a_jb_jM_j+2a_jc_jC_j+2b_jc_je
-(a_je+b_jC_j+c_jM_j)^2.
$$

The final means needed here satisfy

$$
(M_L,M_{L^2},M_H,M_{H^2},M_{HL})
=(e,e,h,e+m(1-v),e+m(x-r)),
\quad m=(h-e)/(1-z).
$$

These stationarity identities hold for every reference null and for the
physical target. Multiplying the sum of variances by $(1-z)^2$ gives an
exact polynomial. Translating it to $\theta=\theta_c+u$ **before** interval
evaluation retains the cancellation between covariance terms. This yields
uniform bounds

$$
\sum_j\operatorname{Var}_{\rm null} Z_j<0.00018,
\qquad
\sum_j\operatorname{Var}_{*} Z_j<0.000085.
$$

The first holds throughout the outer box for realizable null moments;
the second is separately certified at the target. Every centered trial
increment is bounded in absolute value by $b=0.05$. Bernstein therefore
bounds a one-sided linear deviation of size $a>0$ by

$$
\exp\left[-\frac{Na^2}{2(V+ba/3)}\right],
$$

with the appropriate null or target variance bound $V$. Initial signs,
correlations and final means from the same pair are treated jointly.

### A quadratic remainder bound for bounded paired data

A fixed tangent at the target would pay a curvature error proportional to
$R^2$. Expanding around the true moments instead makes the remainder
quadratic in sampling noise. On the event that both $\theta$ and
$\widehat\theta$ belong to $\mathcal B$, a fixed rational positive
semidefinite matrix $Q$ satisfies

$$
-Q\preceq\nabla^2P_+(u)\preceq Q\quad(u\in\mathcal B),
\qquad
|\mathcal R|\le\tfrac12\xi^{\mathsf T}Q\xi.
$$

The whole segment lies in this convex box. The verifier records a rational
matrix $Q_0$ and checks $Q_0\pm\nabla^2P_+(\theta_c)\succeq0$ exactly.
For each Hessian entry it bounds its change throughout $\mathcal B$ by
$E_{ij}$. Adding $\operatorname{diag}(\sum_j E_{ij})$ to $Q_0$ gives $Q$;
symmetric diagonal dominance controls both signs of the Hessian change.
Exact symmetry and rational positive-definiteness checks certify these
matrix statements.

The joint moment noise has the global directional MGF bound

$$
\mathbb E\exp(u^{\mathsf T}\xi)
\le\exp\left(\frac{u^{\mathsf T}D_0u}{2N}\right),
\qquad
D_0=\operatorname{diag}(6/5,6/5,6/5,2,6/5,6/5,2).
$$

Here is a direct justification that does not assume independent moment
coordinates. For one binary pair, half the range of
$aS_0+bS_0S_T+cS_T$ is
$\max(|a|+|b|,|a|+|c|,|b|+|c|)$. Scalar Hoeffding's lemma applies in
every direction. Weighted Cauchy–Schwarz bounds its square by
$6a^2+2b^2+2c^2$ in the $H$ group, and by $6a^2+(6/5)b^2$ in each other
group. Independence of complete trials and the $1/5$ pooling coefficient
on initial means give precisely the displayed $D_0/N$ proxy.

The centered sub-Gaussian quadratic-form inequality then implies, for
$x>0$,

$$
\Pr\!\left\{\xi^{\mathsf T}Q\xi>
\frac{\operatorname{tr}(D_0Q)
+2\sqrt{x\operatorname{tr}((D_0Q)^2)}
+2x\lambda_{\max}(D_0^{1/2}QD_0^{1/2})}{N}\right\}
\le e^{-x}.
$$

This is Hsu–Kakade–Zhang's theorem after a linear change of coordinates;
the source and exact location are given below. The proof uses an auxiliary
Gaussian integration identity. The observations here remain bounded
binary pairs, with no Gaussian sampling approximation.

The exact certificates give

$$
\operatorname{tr}(D_0Q)<\frac92,\qquad
\operatorname{tr}((D_0Q)^2)<\frac{11}2,\qquad
\lambda_{\max}(D_0^{1/2}QD_0^{1/2})<\frac74.
$$

The last bound is checked using the rational matrix
$(7/4)D_0^{-1}-Q\succ0$, without numerical eigenvalue decisions.
Taking $x=5$ and using $\sqrt{55/2}<21/4$ gives the following local remainder guarantee for every true moment
vector in $\mathcal B$:

$$
\Pr\{\text{empirical gate passes and }
|\mathcal R|>65/(4N)\}\le e^{-5}.
$$

Here $65/(4N)=0.000001625$. The quadratic-form tail is global, while its
application to the Taylor remainder is restricted to this gate event.
This is an unconditional probability of an intersection, not concentration
for a conditionally selected noise distribution.

### Error probabilities for the complete composite null

For an inside-box null, $P_+(\theta)=0$. Set $u=0.0000125$ and
$q=65/(4N)$. The false-rejection bound is

$$
\alpha_{\rm in}\le e^{-5}
+\exp\left[-\frac{N(u-q)^2}{2(0.00018+0.05(u-q)/3)}\right]
<0.044297.
$$

For any fixed null outside the box, some fixed coordinate is at least
$R$ from the registered center. The empirical gate requires a fluctuation
of at least $R-0.0013=0.0009$. Hence

$$
\alpha_{\rm out}\le2\exp[-N(0.0009)^2/2]<0.034845.
$$

The pooled initial mean has an even stronger bound. Since the inside and
outside cases are alternatives for each fixed null, the uniform type-I
bound is their **maximum**, not their sum. No union over the continuously
many null models or possible tilts is needed.

At the target, the exact polynomial enclosure gives
$P_+(\theta_*)<-0.000022667$. Use
$\Delta=0.000022667$ in the probability calculation. The target gate-failure
bound, allowing the $10^{-12}$ center enclosure, is

$$
\gamma_*\le12e^{-N(0.0013-10^{-12})^2/2}
+2e^{-5N(0.0013-10^{-12})^2/2}.
$$

There are six unpooled sign moments and one pooled initial mean. With
$a_*=\Delta-u-q>0$, the complete missed-target bound is

$$
\beta\le\gamma_*+e^{-5}
+\exp\left[-\frac{Na_*^2}{2(0.000085+0.05a_*/3)}\right]
<0.023080.
$$

Every final comparison uses rational upper bounds on these tails obtained
from positive exponential series. Gate, score and remainder events need
not be independent. The complete test therefore has false rejection below
4.430% and nominal-target power above 97.692%, using 50 million paired
trials or 100 million endpoint bit readouts.

## A closer physical rival and a necessary acquisition cost

The earlier information bound used a rival that agreed perfectly with all
four pure-field laws. That is a useful calibration example, but a difficult
testing rival can trade small calibration errors for a much smaller switched
error. The following fixed three-state CTMC does so while keeping the
registered tilt exactly $7/9$.

Take $S=(+1,+1,-1)$, $\rho_0=(1/4,1/4,1/2)$ and
$\rho_H=(4/9,4/9,1/9)$. Specify symmetric equilibrium conductances on
the three edges; each displayed decimal is an exact rational number:

| Field | $c_{01}$ | $c_{02}$ | $c_{12}$ |
| --- | ---: | ---: | ---: |
| $L$ | $0.09006333$ | $0.05831059$ | $0.16147905$ |
| $H$ | $0.24140656$ | $0.01830492$ | $0.07508300$ |

Set $(Q_j)_{ab}=c^{(j)}_{ab}/(\rho_j)_a$ for $a\ne b$, and set each
diagonal to minus its row sum. All off-diagonal rates are positive and
$\rho_{j,a}(Q_j)_{ab}=c^{(j)}_{ab}=\rho_{j,b}(Q_j)_{ba}$, so both generators
are ordinary reversible and have the required Gibbs laws. Both fields use
the same initial law $\rho_0$. The tick kernels are $\exp Q_j$ and repeated
letters compose the same kernels. This model belongs to both the fixed-tilt
and unknown-tilt null classes.

Let $P_w$ be the physical target pair law and $Q_w$ this rival's pair law.
The exact certificate proves, for every one of the five settings,

$$
0<D(P_w\Vert Q_w)<\frac{93}{10^8}=9.3\times10^{-7}.
$$

The largest certified upper bound is below $9.29036\times10^{-7}$; the
coarser rational cap is sufficient for the statement below. These are
categorical relative entropies of complete paired observations. Every arm
now carries nonzero information, so the previous argument involving only
$N_{HL}$ is not applicable.

For a test with both error probabilities at most $0.05$, the adaptive
change-of-measure inequality gives

$$
\sum_w\mathbb E_P[N_w]D(P_w\Vert Q_w)
\ge\operatorname{kl}(0.95,0.05)=0.9\log19.
$$

The maximum arm divergence therefore yields

$$
\mathbb E_P[N_{\rm total}]
>\frac{0.9\log19}{9.3\times10^{-7}}
>2\,849\,457.0766.
$$

In particular, any deterministic acquisition budget needs at least
**2,849,458 endpoint-pair trials**, or **5,698,916 endpoint bit readouts**.
This necessary bound applies even with adaptive protocol selection based
on completed past trials and admissible stopping. An expected random count
is not rounded upward to that integer. Current-initial-sign-conditioned
protocol selection, partial-trial selection and richer trajectory data are
outside the five-arm sampling contract.

The fixture was discovered by a small numerical search and then rounded
to the exact table above. Verification does not run an optimizer. Rational
matrix Taylor series through degree 64, norm remainder bounds, positive
pair-probability enclosures and rational logarithm series certify all five
divergences. No claim that this is the closest rival, an optimal experiment
allocation or the exact minimax acquisition cost is needed.

## Scope, sources and reproducibility

Define $N_*^{\rm ideal}$ as the smallest deterministic total-trial budget
that achieves false rejection at most $0.05$ against every unknown-tilt
ordinary at-most-three-state null and power at least $0.95$ at the nominal
physical target. Setting choices may depend on completed past trials but
must precede each current initial observation. The two certified results
apply to exactly this class and give

$$
2\,849\,458\le N_*^{\rm ideal}\le50\,000\,000,
\qquad \frac{50\,000\,000}{N_*^{\rm ideal}}<18.
$$

The upper uses a fixed equal allocation; the lower permits adaptive
allocation. A single explicit rival suffices for the latter. Neither
certificate identifies an optimal design, a closest rival or an exact
minimax budget. At this fixed target, a factor bracket is the appropriate
claim; there is no new asymptotic sample-complexity order.

The sufficient test here assumes ideal recorded pairs. The earlier 10 ppm
systematic-error and known-channel sufficient tests keep their own scope.
They do not automatically transfer to the new statistic. For completeness,
the new comparator also certifies a separate necessary budget of
**3,081,390 pairs** when known independent 1% bit-flip channels act at both
endpoints. This follows from a maximum recorded-arm KL below
$8.6\times10^{-7}$; it is not a noisy-readout sufficient guarantee.

Eliminating $m$ broadens the statistical null. It does not extend the
previous 50 ppm population or common-1% parameter-box theorem to rivals
with independently fitted different tilts. The acquisition bracket does
not price detector calibration, finite resets, switching ramps or
physical acquisition time. Those require the complete measurement contract
in the [preceding note](FAMILIAR_SWITCH_FROZEN_MEASUREMENT.md).

The statistical tools are established. The linear bounded-observation
bounds and adaptive change-of-measure inequality retain the attribution
in the preceding note. The quadratic remainder uses Hsu, Kakade and Zhang,
[*A tail inequality for quadratic forms of subgaussian random vectors*](https://www.cs.columbia.edu/~djhsu/papers/quadratic-ecp.pdf),
Electronic Communications in Probability 17(52), 1–6 (2012),
Theorem 2.1, equation (2.1) and centered Remark 2.2 on page 3. Their
all-direction MGF premise is established explicitly above; a covariance
bound alone would not suffice. This result needs neither independent
moment coordinates nor Gaussian observations. The additional work here
is the observable elimination, the one-branch local certificate and the
certified acquisition bracket for this physical prediction task.

The [score verifier](../scripts/verify_familiar_switch_profiled_score.py)
and [score report](../reports/familiar_switch_profiled_score.json) contain
the exact polynomial, center, linear corrections, rational Hessian matrix
certificate, variance polynomials and risk bounds. The
[information verifier](../scripts/verify_familiar_switch_profiled_information.py)
and [information report](../reports/familiar_switch_profiled_information.json)
contain the explicit CTMC and all five KL enclosures. Both reports bind
this proof and inherited frozen evidence. No optimizer or simulation is
needed to rerun either certificate. Dynamics matrices have dimension at
most four; the statistical Hessian certificate has dimension seven.

Independent internal review covers nuisance elimination, zero-variance
and outside-box cases, joint moment concentration, the covariance
polynomial, the Hessian majorant and the adaptive lower-bound scope.
Internal review and regression are distinct from external validation or
priority certification. Earlier proof and evidence snapshots remain
unchanged.

The next question is the full physical acquisition contract: whether a
community-standard preparation, switching and readout procedure can
support this prediction task at its now bounded testing cost. That question
has priority over smaller changes to the concentration constants. A
statistical rejection under a declared interface is not by itself an exact
state count for an entire imperfect apparatus. Manuscript drafting remains
deferred.
