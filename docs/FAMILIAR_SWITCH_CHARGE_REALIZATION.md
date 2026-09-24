# A charge-state realization with unequal tunneling rates

Two capacitively coupled charge occupations give the coupled-switch model
without interpreting either binary variable as a magnetic spin. In a
specified sequential-tunneling regime, the charge-state generator is
exactly the heat-bath generator used in the
[structural theorem](FAMILIAR_SWITCH_STRUCTURE.md).
The three-state predictor also survives a substantial asymmetry of the
two tunneling rates: at the selected interaction and field, the explicit
construction below covers every ratio from $2/3$ to $2$.

This is a conditional physical-model realization, not a demonstrated
device or a claim that an arbitrary quantum-dot experiment satisfies the
model. Equal tunneling rates are unnecessary for exact compression.
The previously certified numerical gap and sample counts still refer to
the equal-rate operating point; they are not asserted unchanged throughout
the unequal-rate interval.

**Status:** analytic derivation and independent internal algebra review.
The [interface verifier](../scripts/verify_switch_physical_interface.py)
and [report](../reports/switch_physical_interface.json) supply the finite
algebraic checks. No frozen proof is changed.

## 1. From charge occupations to the two switches

Consider two charge occupations $n_1,n_2\in\{0,1\}$ with grand energy

$$
 {\cal E}=U n_1n_2+\epsilon_1 n_1+\epsilon_2 n_2,\qquad U>0.
 \tag{1}
$$

Each dot exchanges particles only with its own equilibrium reservoir.
The reservoirs have the same temperature $T$. Each $\epsilon_i$ is
measured relative to that reservoir's chemical potential. There is no
interdot particle tunneling. One nondegenerate level per dot is retained;
additional charge, orbital, and spin states are excluded by assumption.

Use the opposite charge conventions

$$
 S=2n_1-1,\qquad Z=1-2n_2,\qquad J=\frac{U}{4k_{\rm B}T},
 \tag{2}
$$

and choose the compensated gate trajectory

$$
 \epsilon_2=-\frac U2,\qquad
 \epsilon_1(h)=-\frac U2-2h k_{\rm B}T.
 \tag{3}
$$

Direct substitution, including the additive constant, gives

$$
 \frac{{\cal E}}{k_{\rm B}T}=-JSZ-hS-J-h.
 \tag{4}
$$

Thus repulsive capacitive coupling becomes positive Ising coupling after
reversing the definition of the second binary variable. The observed
variable is the occupation of dot 1. The control changes its addition
energy while keeping the spectator gate compensated.

For a nondegenerate sequential-tunneling transition, write
$f(x)=(1+e^{x/(k_{\rm B}T)})^{-1}$. The rates are

$$
 q_i(0\longrightarrow1\mid n_j)=\Gamma_i f(\epsilon_i+Un_j),\qquad
 q_i(1\longrightarrow0\mid n_j)=
       \Gamma_i[1-f(\epsilon_i+Un_j)].
 \tag{5}
$$

Here $\Gamma_i$ has units of inverse time, rather than energy. Assume it
does not depend on the neighboring charge or the gate value over the
chosen range. Equation (5) becomes exactly

$$
 q_S(S\longrightarrow-S\mid Z)
  =\frac{\Gamma_1}{1+\exp[2S(h+JZ)]},\qquad
 q_Z(Z\longrightarrow-Z\mid S)
  =\frac{\Gamma_2}{1+\exp(2JSZ)}.
 \tag{6}
$$

The rate ratio on every edge is the Boltzmann factor for its energy
change, so the four-state generator obeys ordinary detailed balance.
Its equilibrium laws satisfy the same measured-coordinate tilt
$\pi_h\propto\pi_0e^{hS}$. Charge occupations are time-even variables.
This is a fixed-parameter statement about the classical occupation
generator; if a magnetic field is used to remove a spin degeneracy, it
does not imply that the full microscopic Hamiltonian is invariant under
reversal without reversing that field.

The spinless four-state Hamiltonian and charging/discharging Fermi rates
are standard. Bulnes Cuetara, Esposito, and Gaspard give them in
[arXiv:1105.5974](https://arxiv.org/abs/1105.5974), equations (1) and
(12)–(19). Their derivation uses weak reservoir coupling and Markov and
secular approximations; it also distinguishes tunneling prefactors at
$\epsilon_i$ and $\epsilon_i+U$. Setting those prefactors equal is an
additional model assumption here.

At the selected operating point,

$$
 U=4k_{\rm B}T\log3,\quad
 \epsilon_{1,\rm low}=\epsilon_2=-2k_{\rm B}T\log3,\quad
 \epsilon_{1,\rm high}=-4k_{\rm B}T\log3.
 \tag{7}
$$

If $\Gamma_1=\Gamma_2=\Gamma$, the two ticks of the
[snapshot witness](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) each last
$3/(2\Gamma)$ in physical time. No value of $\Gamma$ or laboratory clock
resolution is inferred from this mathematical conversion.

## 2. An exact three-state predictor with unequal attempts

Keep $J=\log3$, hence $t=\tanh J=4/5$. Normalize time by $\Gamma_1$ and
put $r=\Gamma_2/\Gamma_1$. For $m=\tanh h$, define

$$
 A(m)=\frac{m(1-t^2)}{1-t^2m^2},\qquad
 B(m)=\frac{t(1-m^2)}{1-t^2m^2}.
 \tag{8}
$$

The physical coordinate equations close exactly:

$$
 QS=A-S+BZ,\qquad QZ=r(tS-Z).
 \tag{9}
$$

Use the following three predictive states:

$$
 \widehat S=(-1,1,1)^T,\qquad
 \widehat Z=(-4/5,-8/5,26/25)^T,\qquad
 \widehat\pi_0=(1/2,1/22,5/11).
 \tag{10}
$$

The auxiliary coordinate $\widehat Z$ is not a measured charge and need
not lie in $[-1,1]$. The actual readout remains the deterministic binary
coordinate $\widehat S$.

Let

$$
 \begin{aligned}
 L&=\frac{9(1+m)}{2(25-16m^2)},\\
 q_{21}&=\frac{(1-m)(57+48m)}{2(25-16m^2)},\\
 q_{31}&=\frac{(1-m)(21-24m)}{2(125-80m^2)}.
 \end{aligned}
 \tag{11}
$$

The other four rates are

$$
 q_{12}=\frac{23L}{33},\quad q_{13}=\frac{10L}{33},\quad
 q_{23}=\frac{10(3r-q_{21})}{33},\quad
 q_{32}=\frac{3r-23q_{31}}{33}.
 \tag{12}
$$

Set diagonal entries for zero row sums. All rates in (11)–(12) are in
units of $\Gamma_1$.

**Positive-rate interval.** For

$$
 -10^{-4}\le m\le81/100,\qquad r\ge2/3,
 \tag{13}
$$

every off-diagonal rate is strictly greater than $1/1000$. In particular,
the same fixed predictor covers the two fields $0,\log3$ and their small
calibration neighborhoods.

Here is a direct bound, avoiding sampled positivity tests. On (13),

$$
 \frac{19}{200}\le q_{21}<\frac{22801}{20000},\qquad
 \frac{741}{625000}\le q_{31}<\frac{17}{200}.
 \tag{14}
$$

The $q_{21}$ bounds follow from
$q_{21}=(1-A+2tB)/2$, $|A|\le|m|$, and $0<B\le t$.
For the lower $q_{31}$ bound use
$1-m\ge19/100$, $21-24m\ge39/25$, and
$2(125-80m^2)\le250$.
For $m\ge0$, multiplication by the positive denominator shows that
$q_{31}\le21/250$ is equivalent to
$(9/25)m(104m-125)\le0$.
For $-10^{-4}\le m<0$, its numerator is less than $21.005$ and its
denominator exceeds $249$, giving the upper bound in (14).

Also $L\ge9(1-10^{-4})/50$. Equations (12) and (14) give

$$
 q_{23}>\frac{10}{33}\left(2-\frac{22801}{20000}\right)>10^{-3},
 \qquad q_{32}>\frac{2-23(17/200)}{33}
             =\frac3{2200}>10^{-3}.
 \tag{15}
$$

The $L$ bound gives the same conclusion for $q_{12},q_{13}$.
If in addition $r\le2$, all predictor exit rates are below three:
the row sums are $L$, $(23q_{21}+30r)/33$, and
$(10q_{31}+3r)/33$. The physical target also has exit rates below
$1+r\le3$. Restoring units multiplies these bounds by $\Gamma_1$.

Direct substitution proves (9) for the predictive coordinates in (10).
For example, the two rates from state 1 have ratio $23:10$, so their
contributions to $Q\widehat Z$ cancel there; (12) then gives the desired
$r(t\widehat S-\widehat Z)$ at the other two states.
The vectors $\mathbf1,\widehat S,\widehat Z$ are a basis.
The tilted law

$$
 \widehat\pi_h=\widehat\pi_0(1+m\widehat S)
 \tag{16}
$$

is positive, normalized, and has coordinate means $(m,tm)$.
The identity $A=(1-tB)m$ makes their time derivatives zero.
Together with $Q\mathbf1=0$ and the coordinate basis, this proves full
stationarity of (16), not just stationarity of the observed mean.

Both physical and predictive equilibrium preparations satisfy
$\mathbb E[Z\mid S=\sigma]=t\sigma$. Their conditional initial
coordinate means therefore agree. Equation (9) propagates that equality
through every field protocol in (13), proving equality of the initial
and final binary joint law. This is not a claim of complete visible
trajectory equivalence.

## 3. What remains true about the state cost

The conditional-covariance lower bound does not require equal attempts.
For arbitrary positive attempts $\alpha_0,\alpha_1$, write

$$
 c_*=\frac{\alpha_0+\alpha_1}{2},\qquad
 \omega_h^2=\frac{(\alpha_0-\alpha_1)^2}{4}
                  +\alpha_0\alpha_1tB(h).
 \tag{17}
$$

The coefficient of $Z$ in $e^{aQ_h}S$ is

$$
 \gamma_h(a)=\alpha_0 B(h)e^{-c_*a}
                    \frac{\sinh(\omega_h a)}{\omega_h}>0.
 \tag{18}
$$

At zero field replace $B(h)$ by $t$. Consequently the conditional
covariance used by the two-snapshot witness is

$$
 \gamma_H(a_H)\gamma_0(a_0)(1-t^2)>0
 \tag{19}
$$

for all positive attempt rates and dwell times. The same singleton-sector
identity therefore excludes every ordinary model with at most three
states from exact agreement, with no rival rate cap.

Combining (10)–(16) with this lower bound gives exact minima of three
unrestricted predictive states and four ordinary states for the two joint
snapshot laws at $J=H=\log3$ and $2/3\le r\le2$.
The four-state physical target and the three-state predictor both fit
the common exit cap $3\Gamma_1$. The lower statement itself allows
uncapped rivals. Every stationary two-state kinetic model is ordinary,
so it is excluded as well.

For each fixed positive rate ratio in this interval, the nonzero
polynomial defects also imply a positive finite-error interval by the
explicit polynomial continuity bound in the snapshot proof. Its numerical
size depends on the actual responses.
The certified $0.00184$ joint-TV gap and the existing sample counts
remain assertions about $r=1$. Substantial positivity margins in (15)
do not by themselves certify an unchanged observation gap.

## 4. Which rate deformations preserve exact compression?

For a generator containing only single-coordinate flips, let
$a_Z=q(S=-1\to+1\mid Z)$ and $b_Z=q(S=+1\to-1\mid Z)$.
Then

$$
 QS=(a_Z-b_Z)-(a_Z+b_Z)S.
 \tag{20}
$$

Since every function of binary $Z$ is affine in $Z$, the only term
outside $\operatorname{span}\{\mathbf1,S,Z\}$ is the $SZ$ term arising
from a neighbor-dependent sum $a_Z+b_Z$.
Thus this coordinate space is invariant if and only if each coordinate's
forward-plus-reverse rate is independent of its neighbor.
Under the stated Gibbs detailed balance, this is precisely heat-bath
form with an attempt factor that may depend on the applied field, but
not on the neighboring charge.

The construction above consequently also permits field-dependent attempts
whose ratio stays in its positivity domain. It does not automatically
cover arbitrary energy-dependent tunnel couplings, cotunneling channels,
or extra microscopic states. A small change preserving detailed balance
can still destroy the exact affine closure.

Approximate compression has a simple separate bound. On a common physical
state space, if $\widetilde Q$ is a perturbed generator, define

$$
 \eta(t)=\frac12\max_x\sum_y
                |\widetilde Q_t(x,y)-Q_t(x,y)|.
 \tag{21}
$$

Stochastic contraction and Duhamel's identity bound each initial/final
joint-law displacement by

$$
 b\le\operatorname{TV}(\widetilde\pi,\pi)
                 +\int_0^T\eta(t)\,dt.
 \tag{22}
$$

The initial recorded bit is carried as a fixed label in this argument.
There is no hidden-state dimension factor. For the nominal two-tick
experiment, $T=3$ in attempt-time units.
If a deformation keeps the comparison class's stationary Gibbs relation,
the original three-state model approximates the deformed target with
error at most $b$, while its ordinary-three gap is greater than
$0.00184-b$. A nonempty interval follows when $2b<0.00184$.
If the force law is also deformed, its separate residual must be included;
(22) alone does not verify that interface assumption.

For example, relative changes of at most $\varepsilon_\Gamma$ in each
of the two nominal unit attempt prefactors give the safe bound
$\eta\le2\varepsilon_\Gamma$. Symmetric edge prefactors preserve the
Gibbs law, even when they break affine closure. With unchanged
preparation, (22) then gives $b\le6\varepsilon_\Gamma$.
This is a sufficient model-error bound, not a claim that experimental
tunneling prefactors have been calibrated to that accuracy.

## 5. Spectator-gate leakage and physical assumptions

A residual spectator-energy offset
$\delta\epsilon_2(h)$ contributes an additional field $-g(h)Z$, where

$$
 g(h)=\frac{\delta\epsilon_2(h)}{2k_{\rm B}T}.
 \tag{23}
$$

The intended relation between two stationary laws tilts only $S$.
If the actual spectator field changes by $\Delta g$, the remaining
reweighting is $e^{\Delta g Z}$. For any initial law its TV effect is at
most

$$
 \operatorname{TV}(\pi_{\rm actual,high},\pi_{\rm intended,high})
 \le\tanh(|\Delta g|/2)\le|\Delta g|/2.
 \tag{24}
$$

One way to verify the first bound is to maximize the binary marginal
change under a likelihood ratio $e^{2\Delta g}$; conditional laws
within each $Z$ sector are unchanged.
Thus the earlier $\theta=10^{-5}$ force-law allowance is guaranteed by
$|\Delta g|\le2\times10^{-5}$, or by
$|\delta\epsilon_{2,H}-\delta\epsilon_{2,0}|
 \le4\times10^{-5}k_{\rm B}T$.
If residual leakage is $\Delta g=-\kappa H$ at $H=\log3$, the sufficient
condition is $|\kappa|\le2\times10^{-5}/\log3$.
These are residual errors after gate compensation, not bounds on the
bare physical cross-capacitance.

The target dynamics change too. A hidden-field error costs at most
$(\alpha_1/2)|g(h)|$ in the generator row-TV norm. More generally,
small changes of the dimensionless fields and coupling give the safe
bound

$$
 \eta\le|\Delta\alpha_0|+|\Delta\alpha_1|
 +\frac{\alpha_0}{2}(|\Delta h|+|\Delta J|)
 +\frac{\alpha_1}{2}(|\Delta g|+|\Delta J|).
 \tag{25}
$$

Here the unperturbed attempts appear in the field-error terms; the
prefactor errors cover the remaining difference. Preparation changes
and the force-law defect (24) are separate contributions.

The physical reduction requires the sequential, incoherent charge-state
description, sufficiently weak reservoir coupling, negligible interdot
particle transfer, and no relevant additional levels. Reservoir-induced
broadening, higher-order tunneling, and detector-induced transitions
must be excluded or entered as model error, rather than inferred absent
from a four-state fit.

Spin degeneracy is a concrete caveat. With one empty state and $g$ equally
coupled occupied states, simple charge aggregation gives
$q_{\rm in}=g\Gamma f$ and $q_{\rm out}=\Gamma(1-f)$.
The equilibrium odds acquire the factor $g$, while the total rate
$\Gamma[1+(g-1)f]$ becomes energy dependent. An entropy shift in the
level energy does not alone restore (6).
Hofmann et al.,
[arXiv:1610.00928](https://arxiv.org/abs/1610.00928), equations (1)–(2),
experimentally distinguish degeneracy factors in the in/out rates and
show their removal for resolved nondegenerate transitions.
The stipulated single nondegenerate transition therefore needs physical
justification; it is not implied by naming a device a quantum dot.

## 6. Readout duration does not calibrate arbitrary rivals

If an initial readout's only disturbance is evolution for duration
$\tau_{\rm m}$ under a generator with exit cap $R$, its disturbance
kernel satisfies

$$
 \sup_x\operatorname{TV}(e^{\tau_{\rm m}Q}(x,\cdot),\delta_x)
 \le1-e^{-R\tau_{\rm m}}\le R\tau_{\rm m}.
 \tag{26}
$$

This follows by coupling to the event of no jump.
For the target one may use its known rate bound, such as
$R<3\Gamma_1$ on the unequal-rate interval.
It does not establish an initial-disturbance bound for the full
uncapped rival class. Such a rival can move an order-one probability
during an arbitrarily short measurement. A common rate cap would be a
new restriction on that class.

The per-state disturbance condition in the snapshot proof is sufficient,
not necessary. A weaker valid condition bounds the TV distance between
the entire joint law of initial record and postmeasurement hidden state
and its ideal nondisturbing law. For example, a disturbance that preserves
$S$ and the stationary conditional law $\pi_0(\cdot\mid S)$ leaves that
joint law unchanged under stationary preparation, despite possibly large
hidden jumps. Preserving only the visible marginal, or only the hidden
marginal without its record correlation, does not suffice.
Any such weakening requires its own calibration or observable argument.

The charge detector is external apparatus in this embedding. The two
coupled dots themselves are the target's two state variables; treating
one as an independently driven detector would change its dynamics and
the theorem's assumptions.
