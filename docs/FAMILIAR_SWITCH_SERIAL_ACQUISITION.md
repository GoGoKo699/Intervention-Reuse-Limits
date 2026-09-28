# A physical contract for serial five-setting measurements

[Repository](../README.md) · [Registered test](FAMILIAR_SWITCH_PROFILED_ACQUISITION.md) · [Physical source audit](FAMILIAR_SWITCH_SERIAL_ACQUISITION_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

The same **50-million-pair, unknown-tilt test** remains valid for serial
measurements when each trial's recorded-pair distribution, conditional on
the preceding history, stays within **one part per million in total
variation** of one fixed reference model. Trials need not be independent.
The certified false-rejection probability is below **0.047185** and the
nominal-target miss probability is below **0.024949**.

This is a sufficient operational contract, not a claim that visible
calibration certifies it or that a device has achieved it. The new result
transfers the already registered test to bounded history dependence and
implementation error. The statistical ingredients and the general use of
conditional error budgets are established; the new certificate concerns
this five-setting unknown-tilt score.

For the nominal target, a low-field wait of $24/\Gamma$ gives the stated
preparation allowance from every entering state, where $\Gamma$ is the
common attempt rate. Fifty million such waits plus the active evolution
cost $1.28\times10^9/\Gamma$, before readout, ramps, recovery and calibration.
No finite waiting time prepares every arbitrarily slow competing model.
The null's preparation and instrument promises remain explicit.

## One reference model throughout the acquisition

Use the same five words $L,L^2,H,H^2,HL$, with chronological word order.
Take exactly $N=10^7$ pairs per word; for the concrete resource count below,
repeat this five-word cycle $N$ times. The setting is fixed before its
current initial observation. Use the unchanged empirical gate, polynomial
score, initial-mean corrections and rejection threshold of the
[registered test](FAMILIAR_SWITCH_PROFILED_ACQUISITION.md).

Fix one reference family of pair laws $P_j$. Under the null this family
comes from a single ordinary reversible model with at most three
supported states, a common low-field stationary preparation, fixed
reused kernels, deterministic binary latent readout and one Gibbs tilt
$m\in(-1,1)$. Under the power statement it is the nominal four-state
target with $\tanh J=1/3$, high tilt $7/9$ and unit dwell times.
No numerical tilt calibration is added to the null.

Let $\mathcal F_{t-1}$ contain the past before the reset of trial $t$,
including relevant entering-state, detector and controller information.
It does not expose the current post-reset state or condition away the
fresh randomness of the current preparation. For its
scheduled word $j_t$, assume almost surely

$$
\operatorname{TV}\!\left(
 \mathcal L(A_t,B_t\mid\mathcal F_{t-1}),P_{j_t}
 \right)\le\epsilon,\qquad \epsilon=10^{-6}.
\tag{1}
$$

The reference is fixed for the entire experiment. It cannot be selected
afresh for each history, word or observed result. Conditional deviations
may vary and be correlated across trials. Bounds on unconditional
single-trial marginals or an average calibration error do not imply (1).
The theorem has a fixed final sample count; it does not license optional
stopping or selection using the current initial sign.

There is no transfer here of the older known-1%-flip-channel test.
Equation (1) is a small deviation from the ideal pair law used by the
registered score. Raw 1% endpoint errors do not satisfy a one-ppm
allowance merely because a channel has been calibrated.

## Serial concentration for the unchanged score

Let $\theta=(e,x,y,z,v,r,h)$ be the moments of the fixed reference family.
Retain the registered population box radius $R=0.0022$, empirical gate
radius $g=0.0013$, rational center accuracy $c=10^{-12}$ and rejection
threshold $u=1/80000$. All population identities, polynomial coefficients,
variance bounds and Hessian bounds below are inherited from the frozen
[score certificate](../reports/familiar_switch_profiled_score.json).

### Linear term: conditional bias and variance

Expand the polynomial $P_+$ at the fixed reference $\theta$, not at a
history-dependent conditional mean. With the registered initial-mean
corrections, the linear increment in arm $j$ is

$$
 Z_j=a_j A+b_jAB+c_jB,\qquad
 a_j=\partial_eP_+(\theta)/5+d_j,\quad
 b_j=\partial_{C_j}P_+(\theta),\quad
 c_j=\mathbf1_{\{j=H\}}\partial_hP_+(\theta).
$$

Let $w_j$ be its range over all four binary pairs. The inherited
coefficient-box certificate bounds the full outcome ranges, not merely
their centered values under a selected reference distribution. It gives

$$
\sum_jw_j<0.09,\qquad \sum_jw_j^2<0.002,\qquad
\max_jw_j<0.05.
\tag{2}
$$

For any two laws at TV distance at most $\epsilon$,

$$
|\mathbb E_{\rm actual}Z_j-\mathbb E_{\rm ref}Z_j|
 \le\epsilon w_j,
$$

and, centering the square at the reference mean,

$$
\operatorname{Var}_{\rm actual}Z_j
\le\mathbb E_{\rm actual}(Z_j-\mathbb E_{\rm ref}Z_j)^2
\le\operatorname{Var}_{\rm ref}Z_j+\epsilon w_j^2.
\tag{3}
$$

The oscillation of that squared variable is at most $w_j^2$.
Consequently $1/N$ times the sum of $5N$ increments has predictable drift
at most $d=0.09\epsilon$ in absolute value. Its martingale part has
predictable variance at most $(V+0.002\epsilon)/N$ and increments bounded
by $0.05/N$. The inherited values are

$$
V_0=0.00018,\qquad V_*=0.000085.
$$

Scalar Freedman concentration gives, for a one-sided deviation $a>0$,

$$
F(a,V)=
\exp\!\left[-\frac{Na^2}
 {2(V+0.002\epsilon+0.05a/3)}\right].
\tag{4}
$$

Within-pair covariance is already included in the inherited variance.
There is no assumption of independent initial and final signs.

### Quadratic term: the same directional proxy

Write the seven empirical moment errors as

$$
\widehat\theta-\theta=M+b,\qquad \|b\|_\infty\le2\epsilon.
$$

Here $M$ is the sum of conditionally centered moment increments and $b$
is their accumulated predictable drift; $b$ may be random. Conditional
Hoeffding bounds hold for each binary pair in every direction. Iterating
them gives

$$
\mathbb E e^{v^{\mathsf T}M}
 \le\exp\!\left(\frac{v^{\mathsf T}D_0v}{2N}\right),\qquad
D_0=\operatorname{diag}(6/5,6/5,6/5,2,6/5,6/5,2).
\tag{5}
$$

Indeed, the half-range of $aA+bAB+cB$ is
$\max(|a|+|b|,|a|+|c|,|b|+|c|)$. The same weighted
Cauchy--Schwarz bounds used by the independent-trial proof apply
conditionally; exactly $N$ observations per word give the same final
proxy. Independence between trials is unnecessary.

Let $Q$ be the certified positive-semidefinite Hessian majorant on the
population box. The inherited quadratic-form bound gives

$$
\Pr\!\left\{\tfrac12M^{\mathsf T}QM>\frac{65}{4N}\right\}\le e^{-5}.
\tag{6}
$$

This uses a global directional MGF hypothesis, not independent moment
coordinates or Gaussian observations. Also
$Q\preceq(7/4)D_0^{-1}$ and $\operatorname{tr}D_0^{-1}=31/6$, so

$$
\tfrac12b^{\mathsf T}Qb\le\frac{217}{12}\epsilon^2.
$$

Young's inequality with $\eta=1/50$ yields

$$
\tfrac12(M+b)^{\mathsf T}Q(M+b)
\le\frac{51}{50}\,\tfrac12M^{\mathsf T}QM
  +51\,\tfrac12b^{\mathsf T}Qb.
$$

For a reference $\theta$ in the population box, the empirical gate
puts the entire Taylor segment inside that box. Therefore

$$
\Pr\{\text{gate passes and }|\mathcal R|>q\}\le e^{-5},
\quad
q=\frac{51}{50}\frac{65}{4N}
  +51\frac{217}{12}\epsilon^2
 =0.00000165842225.
\tag{7}
$$

The gate intersection is essential. The quadratic tail is global, but
its identification with the Taylor remainder uses the local Hessian
certificate.

### Both error probabilities

Every null reference in the population box has the $P_+$ branch equal
to zero; the other branch is strictly positive there. The inside-null
bound is

$$
\alpha_{\rm in}\le e^{-5}+F(u-q-d,V_0).
$$

For a null reference outside that box, rejection requires one empirical
coordinate to deviate by at least $R-g$. Its predictable bias is at most
$2\epsilon$, so a conservative conditional Hoeffding bound gives

$$
\alpha_{\rm out}\le
2\exp[-N(R-g-2\epsilon)^2/2].
$$

These are deterministic cases for the one fixed reference. Their maximum,
not their sum, bounds the uniform type-I error.

The target signal has magnitude at least
$\Delta=22667/10^9$. The gate-failure bound is

$$
G_*=12\exp[-N(g-c-2\epsilon)^2/2]
  +2\exp[-5N(g-c-2\epsilon)^2/2].
$$

There are six separately sampled noninitial coordinates and one initial
mean pooled over $5N$ records. Dependence among their errors is permitted
by the union bound. Thus

$$
\beta\le G_*+e^{-5}
 +F(\Delta-u-q-d,V_*).
$$

Exact rational exponential enclosures certify

$$
\alpha_{\rm in}<0.047185,\qquad
\alpha_{\rm out}<0.035477,\qquad
\boxed{\alpha<0.047185,\quad\beta<0.024949.}
\tag{8}
$$

No optimization, floating-point acceptance decision or simulation is
used by the new verifier. The earlier ideal necessary count of
2,849,458 pairs remains a necessary bound for a test required to work
uniformly over this enlarged class, since that class contains the ideal
independent target and comparator. This inclusion argument is not a
new KL theorem for arbitrary dependent data and does not bound elapsed
physical time.

## Sufficient preparation, instrument and control conditions

For one reference model write
$G_\rho(a,x)=\rho(x)\mathbf1_{\{a=S(x)\}}$.
Conditional on the pretrial history, let $\nu$ be the actual preparation
and let $D$ map an entering state to the retained initial record and
word-start state. Sufficient initial conditions are

$$
\operatorname{TV}(\nu,\rho)\le\delta_p,\qquad
\operatorname{TV}(\rho D,G_\rho)\le\delta_i.
\tag{9}
$$

The instrument condition is averaged at $\rho$ but concerns the **joint**
record and hidden state. Contractivity gives

$$
\operatorname{TV}(\nu D,G_\rho)\le\delta_p+\delta_i.
$$

Preparation is charged once. For each subsequent active block, require
its actual conditional next-state law, given the entire within-trial
history and current state, to be within row-TV $\kappa_k$ of the fixed
reference kernel. If final registration differs from the true sign at
the declared active endpoint with probability at most $\delta_f$,
conditional on the pretrial history and word, sequential coupling gives

$$
\operatorname{TV}(\mathcal L(A,B\mid\mathcal F),P_j)
 \le\delta_p+\delta_i+\sum_k\kappa_k+\delta_f.
\tag{10}
$$

Couple the initial joint laws, then the active transitions until the
first mismatch, then the final record. The right side bounds the
probability of any mismatch. It does not require independent detector
errors or independent trials. A proved defect for the complete active
word can replace the sum of individual block bounds.

Every ramp, barrier operation, settling interval and detector influence
must belong to a specified block. The active allowance is per complete
word; it cannot be spent once per tick. A boundary move cannot remove
unaccounted physical evolution between the retained record and the active
start. Memory that changes future transition laws must satisfy these
conditional bounds or be included among the predictive states.

An alternative instrument characterization follows from the exact identity

$$
\operatorname{TV}(J,G_\mu)=\Pr_J\{A\ne S(X)\},
$$

where $\mu$ is the hidden marginal of a joint record/state law $J$.
For each state, the off-label mass equals the deficit of the on-label
mass. Therefore hidden-law error plus misregistration at the actual
word-start boundary bounds $\operatorname{TV}(J,G_\rho)$.
If the nonselective instrument preserves $\rho$ up to $\delta_{\rm ns}$
and its actual boundary registration error is at most $\delta_r$, the
initial contribution is at most $\delta_p+\delta_{\rm ns}+\delta_r$.
This is an alternative to $\delta_p+\delta_i$, not another charge.

A transparent sufficient allocation is:

| Component | Conditional allowance per complete trial |
| --- | ---: |
| Preparation before the initial instrument | 0.25 ppm |
| Joint initial-record/word-start-state instrument | 0.25 ppm |
| Complete active word and assigned ramps | 0.25 ppm |
| Final registration | 0.25 ppm |
| Total recorded-pair TV | 1 ppm |

These are mathematical requirements, not achieved device specifications.
The initial allowance includes correlated recording errors and hidden
kicks. The final endpoint is taken before any subsequent disturbance;
that disturbance still affects the state entering the next reset.

For a separate calibration stage completed before testing, any
probability of an invalid calibration certificate must be included in
the final risk. If the conditional contract holds for every valid
calibration record and certificate failure probability is at most
$\delta_{\rm cal}$, the corresponding unconditional risk is at most
the bound in (8) plus $\delta_{\rm cal}$. Postselecting on calibration
computed from the scored data does not justify this argument.

## What a finite reset proves

For the nominal target, the zero-field equilibrium has minimum mass
$1/6$ and gap $2\Gamma/3$. Standard reversible $L^2$ contraction gives

$$
\operatorname{TV}(\nu e^{TQ_L},\rho)
 \le\frac{\sqrt5}{2}e^{-2\Gamma T/3}.
$$

At $T=24/\Gamma$, this is about $0.126$ ppm and strictly below
$0.25$ ppm. A rational proof uses $\sqrt5/2<2$ and
$\sum_{k=0}^{32}16^k/k!>8{,}000{,}000$.
The bound is uniform over entering distributions, hence over the target's
past histories, provided the reset generator itself has the stated
dynamics. It establishes only the preparation row of the allocation.

There is no common finite passive wait over the unrestricted null.
Multiplying every generator of an admissible reversible Gibbs family by
$\lambda>0$ preserves that family and its state count. At any finite
waiting time its propagator tends to the identity as $\lambda\downarrow0$.
Starting at state $x$, the preparation error tends to $1-\rho(x)$.
Thus unrestricted slowing defeats any proposed small uniform reset
tolerance. A separately justified relaxation bound or preparation
mechanism changes this premise; the target's bound cannot supply it.

Visible equilibrium-looking data do not establish hidden equilibrium.
The existing [preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)
gives a reversible three-state example with identical complete low-field
binary trajectory laws but biased hidden preparation and altered switched
responses. The [readout boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md)
likewise separates visible classification calibration from the joint
instrument condition. These are earlier results, not new false-rejection
examples for the present gated test.

## Complete serial resource count

Use a low-field reset before each trial. After the initial readout,
execute the selected word and the final readout at its ending field,
then return to low field. A readout hold is separate from its active tick.

| Resource | Count for $N=10^7$ five-word cycles |
| --- | ---: |
| Complete pair trials and resets | 50,000,000 |
| Initial plus final endpoint windows | 100,000,000 |
| Low-field active ticks | 40,000,000 |
| High-field active ticks | 40,000,000 |
| Low-to-high field transitions | 30,000,000 |
| High-to-low field transitions | 30,000,000 |
| Same-field internal tick seams in $L^2,H^2$ | 20,000,000 |

Each $H,H^2,HL$ trial has one upward and one downward field transition.
Ten million downward transitions occur inside $HL$; the other twenty
million return $H,H^2$ trials to reset. The seam inside $L^2$ or $H^2$
is not an additional field transition.

With reset duration $T_r/\Gamma$, endpoint durations $T_i,T_f$,
up/down ramp durations $t_\uparrow,t_\downarrow$ and other nonoverlapping
overhead $T_{\rm other}$, the serial elapsed time is

$$
T_{\rm total}
=\frac{80\,000\,000+50\,000\,000T_r}{\Gamma}
 +50\,000\,000(T_i+T_f)
 +30\,000\,000(t_\uparrow+t_\downarrow)+T_{\rm other}.
\tag{11}
$$

At $T_r=24$, the first term is $1.28\times10^9/\Gamma$.
Calibration and initialization overhead belongs in $T_{\rm other}$.
If a separate protective barrier is engaged and released for every
endpoint window, there are 200 million such barrier edges; these are
distinct from field transitions. Their durations and errors must be
assigned without double counting. Parallel devices would have a
different wall-clock cost and require their own common-reference and
calibration justification.

Fast detector discrimination alone does not determine $\Gamma$ or the
reset throughput. The [source audit](FAMILIAR_SWITCH_SERIAL_ACQUISITION_SOURCE_AUDIT.md)
compares actual device regimes instead of combining their best numbers.

## Physical meaning and next question

The supported physical anchor is a sequential-tunneling population model
of capacitively coupled single-level dots, with common-equilibrium
reservoirs, compensated energy control and fixed wide-band couplings.
Its binary variables are charge occupations, not coherent electron spins.
The source audit records ten primary comparisons, including equilibrium
cycle experiments and detector-induced population backaction. These
establish component conventions, not the full one-ppm implementation.

The theorem is an operational extension of a controlled model-selection
benchmark. Rejection excludes the stated ordinary three-state reference
class under its implementation promises. It does not establish an exact
four-state upper for an entire imperfect apparatus, a heat saving, or a
hardware-memory saving. The earlier nine-million-trial preparation-free
result has a different known-tilt statistic and target/interface scope;
the present result is not the first serial or preparation-free test.

The principal unresolved issue is how to reduce or justify the competing
models' preparation and instrument assumptions using an established
physical interface. The existing preparation-free return identity
suggests looking for a short unknown-tilt version. That structural
question is more useful now than further small improvements in
concentration constants. Manuscript drafting remains deferred.

## Certification and attribution

The [new verifier](../scripts/verify_familiar_switch_serial_acquisition.py)
and [report](../reports/familiar_switch_serial_acquisition.json) bind this
note, the source audit and the inherited exact score evidence. They check
the range aggregates, variance inflation, drift and quadratic-remainder
arithmetic, rational probability bounds, target reset inequality and
resource counts. Finite checks supplement the analytic conditional-MGF,
coupling and no-uniform-reset arguments; they do not enumerate all
histories or validate a device.

Freedman's scalar martingale inequality is stated as Theorem 1.1 in
[Tropp's author text](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf),
following Freedman (1975). The centered directional sub-Gaussian
quadratic bound is Theorem 2.1 and Remark 2.2 of
[Hsu--Kakade--Zhang](https://www.cs.columbia.edu/~djhsu/papers/quadratic-ecp.pdf).
Its MGF hypothesis permits the dependent vector in (5). Reversible mixing,
TV contraction and sequential coupling are standard tools. No new
general concentration, mixing or coupling theorem is claimed.
