# Read the visible state while allowing the hidden state to relax

The initial measurement need not freeze the entire system. It suffices to
hold the observed binary state fixed and preserve equilibrium inside each
of its two sectors. Hidden transitions may then be arbitrarily fast and
the measurement may take arbitrarily long: the joint law needed by the
two-protocol witness is unchanged at equilibrium.

This note supplies a structural sufficient condition for the initial
instrument in the [weak-field result](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md).
It replaces a small worst-state disturbance requirement with a condition
on the operation actually needed by the theorem. It introduces no extra
recorded bit or tested control word. It does add a specified measurement
operation before each word. The charge realization requires a barrier
control that suppresses visible tunneling during that operation, in
addition to the two active field settings. This blocking actuator, its
switching accuracy, and the measurement duration are physical resources.
Equilibrium preparation, the detector channel, and the
instrument condition remain model promises, not conclusions of the score.

[Charge-state model](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) ·
[Preparation and instrument counterexamples](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) ·
[Target preparation bound](FAMILIAR_SWITCH_PREPARATION_COST.md)

## 1. The joint instrument is the relevant object

Let a finite hidden state space be partitioned by a deterministic readout
$S:X\to\{-1,+1\}$. Let $\pi$ be the stationary low-field law, with positive
mass in both sectors. Write $w_s=\pi(S=s)$ and
$\pi_s=\pi(\cdot\mid S=s)$. The ideal initial-label/state joint law is

$$
 G_\pi(s,y)=\pi(y)\mathbf1\{S(y)=s\}.
 \tag{1}
$$

An instrument first assigns the true initial label $s=S(x)$ and then
applies a stochastic kernel $K_s$ supported inside that same sector.
Its joint kernel from $x$ to $(s,y)$ is

$$
 D(x;s,y)=\mathbf1\{s=S(x)\}K_s(x,y).
 \tag{2}
$$

**Protected-readout theorem.** If $\pi_sK_s=\pi_s$ for each sector, then

$$
 \pi D=G_\pi.
 \tag{3}
$$

Indeed, for $S(y)=s$,
$\sum_{x:S(x)=s}\pi(x)K_s(x,y)=w_s\pi_s(y)=\pi(y)$;
all other entries vanish. This identity concerns the retained initial
label jointly with the postmeasurement hidden state. It therefore
survives every later control word and final observation by stochastic
contraction. It is stronger than merely preserving the hidden marginal.

There is no restriction on the total change of a particular hidden state.
For example, $K_s=(I+\Pi_s)/2$, where every row of $\Pi_s$ is $\pi_s$,
has worst-row TV disturbance $9/20$ when
$\pi_s=(9/10,1/10)$; nevertheless its equilibrium joint disturbance is
exactly zero. This kernel is produced by the continuous-time reset
generator $L_s=\Pi_s-I$ over duration $\log2$. Even the full conditional
reset $K_s=\Pi_s$ is allowed by (3).

For an arbitrary preparation $\nu$ with
$\operatorname{TV}(\nu,\pi)\le\epsilon_p$, contractivity gives

$$
 \operatorname{TV}(\nu D,G_\pi)\le\epsilon_p.
 \tag{4}
$$

More generally, if an actual joint instrument $\widetilde D$ has
$\operatorname{TV}(\pi\widetilde D,G_\pi)\le\xi$, then

$$
 \operatorname{TV}(\nu\widetilde D,G_\pi)
 \le\epsilon_p+\xi.
 \tag{5}
$$

Preparation is charged once. Comparing the disturbed law at $\nu$ to an
undisturbed law at $\nu$, and only then to equilibrium, would unnecessarily
repeat that charge. Equation (5) is the direct comparison to the stationary
joint law used by the existing robust witness.

## 2. Time-dependent protected dynamics and imperfect protection

Suppose the protected measurement dynamics have a time-dependent Markov
generator $L(t)$, no transitions between the sectors, and

$$
 \pi_sL_s(t)=0 \quad\text{for almost every }t\in[0,T].
 \tag{6}
$$

Assume finite, integrable rates on this finite time interval so the
propagator exists. Its sector kernel preserves $\pi_s$, even when the
generators at different times do not commute. Ordinary detailed balance
with $\pi_s$ at every time is sufficient for (6), but is not necessary.
The theorem places no common upper rate bound on competing models: each
model may have arbitrarily large finite within-sector rates.

Now add unwanted sector-changing transitions with total rate at most
$\kappa(t)$ from every state. Couple the actual dynamics to the protected
dynamics until their first such transition, using a dominating Poisson
clock of rate $\kappa(t)$. Consequently their full histories, and hence
their joint label/state laws, differ with probability at most

$$
 \xi_{\rm leak}\le 1-\exp\!\left[-\int_0^T\kappa(t)\,dt\right]
 \le \int_0^T\kappa(t)\,dt.
 \tag{7}
$$

The rate bound in (7) concerns only transitions that change the observed
sector during the measurement. It is not an exit-rate cap on the rival's
hidden dynamics or on its subsequent two control plateaus. The coupling
does not claim that conditioning on no sector-changing jump leaves the
protected law unchanged; such conditioning can bias a path. Only the
unconditional probability that the coupled paths separate is used.

Conditional stationarity may also be imperfect. For sector-preserving
$L_s(t)$ define the signed flux defect

$$
 d_s(t)=\frac12\|\pi_s L_s(t)\|_1.
 \tag{8}
$$

Variation of constants and contraction of zero-mass signed measures give

$$
 \delta_s:=\operatorname{TV}(\pi_sK_s(0,T),\pi_s)
 \le\int_0^T d_s(t)\,dt.
 \tag{9}
$$

For example, the identity behind (9) is
$\pi_sK_s(0,T)-\pi_s=\int_0^T\pi_s L_s(t)K_s(t,T)\,dt$.
Combining the two errors yields the useful sufficient budget

$$
 \boxed{\xi\le
 \sum_s w_s\min\!\left\{1,\int_0^T d_s(t)\,dt\right\}
 +1-e^{-\int_0^T\kappa(t)dt}.}
 \tag{10}
$$

A final cap at one may be applied. Equivalently, a calibrated endpoint
conditional defect $\delta_s$ can replace its integral bound. Hidden
rates need not be small when their stationary fluxes balance exactly.

## 3. Independent electronic errors and finite integration time

Let the initial electronics apply a fixed binary symmetric channel
$B_0(i\mid s)$, with its randomness independent of the hidden dynamics.
Applying this channel to the true label in (1)--(5) contracts TV and
produces the same initial detector model as in the existing proofs.
The final electronic bit flip is independent of the initial one and of
the dynamics, with its own fixed channel $B_f$. Their probabilities may
be unknown; they may differ between the target and a rival. Both remain
shared across the two protocol words within one model.

For an integrating detector, this statement requires that every
constant-$S$ measurement history produce that same channel $B_0$,
independently of the unobserved history and final hidden state. A detector
whose error depends on hidden transitions does not automatically satisfy
this requirement. The duration $T$ may affect its fixed error
probability, which must still lie in the stipulated detector class.

Under imperfect protection, use the same detector randomness on the
coupled paths. If the paths coincide and $S$ stays constant, their
electronic outputs agree. Outputs on paths where protection fails may
be arbitrary; their contribution is already bounded by (7). This is a
joint-instrument perturbation about the independent-channel reference,
not an assertion that arbitrary moving-state integration itself is a
binary symmetric channel. Any additional failure of the constant-state
channel or independence assumptions needs a separate joint-law error
budget.

An outcome-dependent hidden kick is also not automatically harmless.
A sufficient extension is that, for every true sector $s$ and recorded
outcome $i$, its conditional kernel preserve $\pi_s$, and that the
outcome probabilities equal $B_0(i\mid s)$ independently of the initial
hidden state. These conditions preserve the electronic-label/state
joint law directly. No such feedback is needed for the operation above.

## 4. A concrete charge-state operation

For the charge model with energy $-JSZ-h_0S$, block tunneling between the
observed dot and its reservoir during the initial readout, while holding
the energy parameters fixed. The spectator dot may continue relaxing.
Within an observed sector,

$$
 \pi_s(z)=\frac{1+tsz}{2},\qquad t=\tanh J,
 \qquad
 q_z(t_{\rm m};z\to-z\mid s)
 =\frac{\gamma_s(t_{\rm m})}{2}(1-tsz).
 \tag{11}
$$

Here $t_{\rm m}$ is measurement time and $\gamma_s$ is any nonnegative
integrable attempt rate. The low field $h_0$ affects sector masses but
not these conditional laws. The two stationary edge fluxes are both
$\gamma_s(1-t^2)/4$, so (6) holds for arbitrary measurement duration,
including large hidden rearrangement. At $J=\log3$, the conditional
probabilities are $9/10$ and $1/10$.

If the observed tunneling is only suppressed, its actual maximum
sector-changing rate supplies $\kappa$. A uniform bound
$\kappa T\le10^{-5}$ fits the earlier $\xi=10^{-5}$ allowance,
provided conditional stationarity is exact. With residual spectator
rates $q_-: -1\to+1$ and $q_+: +1\to-1$, the exact defect is

$$
 d_s=\left|\pi_s(-1)q_- -\pi_s(+1)q_+\right|.
 \tag{12}
$$

This identifies which backaction matters. Changing the common spectator
attempt rate is harmless; changing its conditional stationary odds must
be bounded or compensated. Changing the barrier may also shift dot
energies, and a charge detector may cause transitions. Those effects are
not excluded by the word "block"; they enter (7), (8), or the electronic
channel premise. Releasing the barrier must likewise be included in
the measurement operation until the stipulated active plateau begins.

For an ordinary rival, deleting all between-sector edges of any generator
reversible with respect to its own $\pi$ leaves each conditional law
stationary. Thus the same mathematical operation is meaningful without
knowing the rival's hidden graph or limiting its internal rates. Whether
a physical barrier realizes that operation for every admissible rival is
an instrument premise. Target-specific control of one dot does not
establish this structural property for an arbitrary alternative model.

## 5. What this does and does not settle about preparation

Protected readout preserves a correct conditional equilibrium law. It
does not establish that the starting law had that property. Conditional
relaxation can move an arbitrary law toward
$\nu(S=s)\pi_s$, but it preserves the original sector weights; a
balanced readout alone therefore does not certify full preparation.
Nor does observing unchanged endpoint probabilities certify the joint
instrument. The explicit counterexamples in the
[preparation-boundary note](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)
remain applicable.

For the specified equal-attempt heat-bath target only, a low-field wait
of 62 attempt-time units still supplies the existing preparation bound
$\epsilon_p<10^{-5}$ from any starting law. The proof uses spectral gap
at least $1/5$ and minimum equilibrium mass greater than $1/21$ for the
allowed low fields:

$$
 \operatorname{TV}(\mu e^{62Q_0},\pi_0)^2
 \le 5e^{-124/5}<10^{-10}.
 \tag{13}
$$

This previously established bound is recalled, not extended to a new
kinetic family. An arbitrarily slow rival has no uniform finite reset
time. Also, a finite mixing wait in one reused device does not make
successive trials exactly independent. The existing two-million and
2.5-million trial certificates continue to require their stated fresh
independent trials; a conditional mixing or martingale replacement
requires a separate sampling argument.

In the existing weak-field physical budgets, (10) may be used for each
model's $\xi$. Exact protected readout has $\xi_T=\xi_R=0$ at stationary
preparation, whatever the within-sector measurement duration. Using the
older nonnegative $10^{-5}$ allowances remains conservative, so no
existing separation or sample certificate is weakened. Any reduction
of a numerical certificate's printed budget should be separately
computed rather than inferred here.

The resulting physical requirement is precise: prepare the low-field
law, protect the observed sector during initial measurement, preserve
its conditional stationary law, and use the promised detector channel.
Only the specified two control words and their initial/final bits enter
the witness. Preparation and readout duration remain unpriced overhead;
this is not a device demonstration or a claim of PRL readiness.
