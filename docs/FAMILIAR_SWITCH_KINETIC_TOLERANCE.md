# A finite memory advantage without exact heat-bath kinetics

The weaker-field experiment retains its three-versus-four state advantage
under small departures from heat-bath rates. The perturbed four-state
target must still obey detailed balance for the same Gibbs energy at each
field. Its rates may depend on the neighboring charge, so the exact
three-dimensional coordinate closure can fail.

The useful quantity is the accumulated generator-row error during either
two-field protocol. If that error is at most $10^{-4}$, the certified
state-count interval is

$$
 \boxed{0.00012\le\delta_{\rm obs}\le0.0009.}
 \tag{1}
$$

The other physical allowances remain $10^{-5}$ each, and target detector
errors remain unknown independent symmetric flips of at most one percent
per bit. The ordinary rivals retain their unrestricted reversible
kernels and arbitrary symmetric detector errors. Thus a precise
heat-bath rate formula is sufficient for exact compression, but is not
necessary for this finite-accuracy advantage.

This is a conditional model-error guarantee. It does not establish that
a particular device meets the numerical tolerances. Manuscript drafting
remains deferred.

**Status:** the analytic argument has passed independent internal review.
Its finite numerical premises are checked by the exact verifier below.
These are internal checks, not external peer review.

[Weaker-field physical certificate](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md)
· [Charge realization and closure criterion](FAMILIAR_SWITCH_CHARGE_REALIZATION.md)
· [Five-million-trial test](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md)
· [Exact verifier](../scripts/verify_switch_kinetic_interface.py)
· [Certificate report](../reports/switch_kinetic_interface.json)

## 1. The kinetic departure and its counted states

Keep the four physical states $(S,Z)\in\{-1,1\}^2$, energy
$-JSZ-hS$, and $J=\log3$. The nominal fields are $0,\log2$ and
both nominal dwell times are $5/4$. There is one actual low plateau,
one actual high plateau, and one dwell time for each plateau, shared
across the chronological words $0H$ and $H0$.

At an actual field $h$, write $Q_h$ for the equal-unit-attempt
heat-bath generator and $\widetilde Q_h$ for the perturbed target.
Require both to have the same Gibbs stationary law

$$
 \pi_h(S,Z)\ \propto\ \exp(JSZ+hS),
 \tag{2}
$$

and require $\widetilde Q_h$ to obey ordinary detailed balance with
respect to (2). Each plateau uses a fixed generator. Arbitrary time
variation among reversible generators inside a plateau is not included:
their ordered product need not be a reversible kernel. Fixed plateau
generators ensure that the actual target itself remains an admissible
ordinary four-state model.

Define the signed generator-row total-variation defect

$$
 \eta_h=\frac12\max_x\sum_y
       |\widetilde Q_h(x,y)-Q_h(x,y)|,
 \qquad
 \kappa=\widetilde\tau_0\eta_{h_0}
       +\widetilde\tau_H\eta_{h_H}.
 \tag{3}
$$

The diagonal term is included. The same $\kappa$ covers both protocol
orders. It is dimensionless: rates and dwell times use the same units.
No additional hidden states, readout, or control branch are introduced.
Transitions beyond single-coordinate flips can also be covered by (3)
if they remain on these four states and preserve (2) and detailed
balance; the relative-prefactor example below only uses the original
single-coordinate edges.

## 2. A joint-law transfer that retains the initial record

For a signed zero-mass row $v$, use
$\|v\|_{\rm TV}=\frac12\sum_x|v_x|$.
Stochastic kernels contract this norm. Duhamel's identity for a fixed
plateau gives, for every initial distribution $p$,

$$
 \left\|p e^{t\widetilde Q_h}-p e^{tQ_h}\right\|_{\rm TV}
 \le\int_0^t
 \left\|p e^{s\widetilde Q_h}
          (\widetilde Q_h-Q_h)e^{(t-s)Q_h}\right\|_{\rm TV}ds
 \le t\eta_h.
 \tag{4}
$$

Telescoping the two plateau propagators gives a bound $\kappa$ for
either protocol. Apply the same argument separately within every
initial recorded-label sector and then sum its probability weight.
This proves the same bound for the full joint law of the initial
record and final state. Deterministic final readout and each model's
own fixed detector channel contract that bound. Correlations between
the two records within a trial are retained throughout.

Because (2) is unchanged by the kinetic departure, this comparison
requires no new stationary-preparation displacement. Preparation and
initial-instrument errors are charged separately below. No detector
calibration is inferred from this contraction argument.

## 3. Lower and upper state counts charge the departure once each

Use the same six physical allowances as the tighter row of the
[weaker-field proof](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md):

$$
 \epsilon_{p,T}=\epsilon_{p,R}=\epsilon_h=\epsilon_t
 =\xi_T=\xi_R=10^{-5}.
 \tag{5}
$$

Here preparation is measured from each model's stationary low law.
The initial-instrument allowance is a joint-TV bound including its
correlation with the retained initial record. For the target, actual
fields differ from $0,\log2$ by at most $\epsilon_h$, and each actual
dwell time differs from $5/4$ by at most $\epsilon_t$.

The inherited stationary ordinary-three-state separation is greater
than $g_0=9/8000$, allowing low stationary bias $|v|\le10^{-4}$,
tilt-parameter error $|u-3/5|\le10^{-4}$, and stationary tilt TV
residual $\theta\le10^{-5}$. The unchanged Gibbs law (2) ensures the
actual target obeys these promises, with $\theta=0$.

Without the kinetic departure, the target-to-nominal table budget and
rival-to-stationary table budget are

$$
 b_T=\epsilon_{p,T}
      +\left(\frac74+\epsilon_t\right)\epsilon_h
      +4\epsilon_t+\xi_T=0.0000775001,
 \qquad b_R=\epsilon_{p,R}+\xi_R=0.00002.
 \tag{6}
$$

Equation (4) adds $\kappa$ to the target budget. It adds nothing to the
rival budget: the stationary lower already covers arbitrary reversible
rival kernels. Therefore every admissible ordinary rival with at most
three states has observed error strictly greater than

$$
 g_0-b_T-b_R-\kappa=0.0010274999-\kappa.
 \tag{7}
$$

For the constructive general three-state upper, use the positive
predictor in the [charge-realization proof](FAMILIAR_SWITCH_CHARGE_REALIZATION.md),
at the actual two fields and actual two dwell times. Those fields remain
within its proven positivity domain. Its stationary ideal-instrument
joint laws agree exactly with the heat-bath reference at those actual
values. It therefore needs no field or timing transfer term. Use the
target's own detector on this predictor. Its error for the kinetically
perturbed target is at most

$$
 b_G+\kappa:=\epsilon_{p,T}+\xi_T+\kappa
            =0.00002+\kappa.
 \tag{8}
$$

The two appearances of $\kappa$ in (7) and (8) concern different
comparisons: the ordinary lower and the constructive general upper.
It is counted once in each. Exact three-state agreement with the
perturbed target is not asserted.

The actual four-state target supplies an exact ordinary upper.
Every stationary two-state kinetic model is ordinary, so (7) also
excludes general predictors with at most two states. Consequently the
minimum state counts are exactly three for the general stationary
class and four for the ordinary class throughout

$$
 0.00002+\kappa\ \le\ \delta_{\rm obs}\ \le\
 0.0010274999-\kappa.
 \tag{9}
$$

Here any advertised upper bound on the actual $\kappa$ may be used
on both sides. The interval has positive width if

$$
 \kappa<0.00050374995.
 \tag{10}
$$

At $\kappa\le10^{-4}$, (8) is at most $0.00012$ and (7) is
greater than $0.0009274999>0.0009$, proving (1). The target's full
table budget for any new sampling analysis is then

$$
 b_T^{\rm kin}=b_T+10^{-4}=0.0001775001.
 \tag{11}
$$

The former two-million and 2.5-million trial guarantees used the
smaller budget (6); those counts are not automatically transferred
to (11). Also, an approximate-null test intended to cover the new
constructive error should allow at least $0.00012$, rather than
retaining the earlier $0.0001$ allowance.
The [new five-million-trial test](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md)
uses (11) and allows $0.0002$ observed prediction error for the ordinary
null, with false rejection below $5\%$ and power above $95\%$.

## 4. A symmetric-edge prefactor example

For every undirected original flip edge $\{x,y\}$, choose one positive
factor $a_{xy}(h)=a_{yx}(h)$ and set

$$
 \widetilde q_h(x,y)=a_{xy}(h)q_h(x,y),\qquad
 |a_{xy}(h)-1|\le\varepsilon_\Gamma.
 \tag{12}
$$

Set the diagonal entries by zero row sums. The factor may depend on
the field and on the unchanged neighboring coordinate. Its symmetry
preserves the equilibrium edge flux equality, hence (2) and detailed
balance. Neighbor dependence can make the forward-plus-reverse rate
depend on that neighbor and destroy the exact affine closure. It is
therefore a genuine departure from the heat-bath closure assumption.

For each row, the absolute diagonal perturbation is at most the sum
of the absolute off-diagonal perturbations. Thus

$$
 \eta_h\le\max_x\sum_{y\ne x}
       |\widetilde q_h(x,y)-q_h(x,y)|
 \le\varepsilon_\Gamma\max_x\sum_{y\ne x}q_h(x,y).
 \tag{13}
$$

All actual fields in (5) obey $|h|\le\log3$: in particular,
$\log(3/2)\ge1/3>10^{-5}$. Since $J=\log3$, the spectator flip
rate is at most $9/10$ and the observed-coordinate flip rate is at
most $81/82$. Therefore the reference exit rate is bounded by

$$
 \frac9{10}+\frac{81}{82}=\frac{387}{205}<\frac{19}{10}.
 \tag{14}
$$

The actual total duration is at most $5/2+2\times10^{-5}$. Combining
(3), (13), and (14) gives the simple sufficient conversion

$$
 \kappa\le\frac{19}{10}
       \left(\frac52+2\times10^{-5}\right)\varepsilon_\Gamma
       =4.750038\,\varepsilon_\Gamma.
 \tag{15}
$$

In particular, a relative prefactor tolerance of $2\times10^{-5}$
(20 parts per million, or $0.002\%$) gives
$\kappa\le0.00009500076<10^{-4}$ and hence (1).
A larger $10^{-4}$ relative tolerance still leaves a narrower certified
population interval:

| Relative edge-prefactor allowance | Sufficient integrated budget | General three-state upper | Certified three-versus-four interval |
|---|---:|---:|---|
| $2\times10^{-5}$ | $10^{-4}$ | $0.00012$ | $[0.00012,0.0009]$ |
| $10^{-4}$ | $0.0004750038$ | $0.0004950038$ | $[0.0005,0.00055]$ |

For the second row, the ordinary-three error is greater than
$0.0005524961>0.00055$. This row supplies population state counts,
not a sampling guarantee. Both relative tolerances are sufficient and
conservative; no rate-uncertainty calibration procedure is priced.

The bound does not cover extra microscopic states, arbitrary driven
nonreversible transitions, or an unaccounted change of stationary
energy. Those change the model being certified and need their own
assumptions or error terms. The result concerns the two prescribed
initial--final joint tables, not equality of full visible trajectories.
