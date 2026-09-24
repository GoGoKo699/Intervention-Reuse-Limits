# What repeatable readout and endpoint checks leave unresolved

A small calibration experiment can address preparation without proving
the initial instrument's required joint property. Even perfect preservation
of the visible state, arbitrarily many immediate repeated readouts, and
unchanged future endpoint distributions do not together establish that
electronic readout errors are independent of a hidden measurement kick.

The example below uses three ordinary reversible states and the same two
field settings and active dwell times as the selected experiment. It is a
boundary for the specified calibration tests. It is not a fit to the
selected target tables, a false rejection by the current gated score, or
an impossibility theorem for every conceivable calibration experiment.

[Preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) ·
[Protected readout](FAMILIAR_SWITCH_PROTECTED_READOUT.md) ·
[Conditional serial sampling](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) ·
[Observable preparation](FAMILIAR_SWITCH_OBSERVABLE_PREPARATION.md) ·
[Calibration precision](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md) ·
[Source audit](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_SOURCE_AUDIT.md) ·
[Internal review](FAMILIAR_SWITCH_OBSERVABLE_CALIBRATION_INTERNAL_REVIEW.md) ·
[Exact verifier](../scripts/verify_switch_observable_calibration.py) ·
[Certificate report](../reports/switch_observable_calibration.json)

## 1. Three ordinary reversible states

Take

$$
 S=(-1,1,1)^T,\qquad
 \pi_0=(1/2,1/4,1/4),\qquad
 u=3/5,\qquad \pi_H=(1/5,2/5,2/5)=\pi_0(1+uS).
 \tag{1}
$$

Thus $H=\log2$ gives the stated Gibbs tilt from a balanced low-field
law. Write $\Pi_0,\Pi_H$ for the row-constant stationary reset matrices,
let $\tau=5/4$, and define

$$
 R=\begin{pmatrix}1/3&2/3&0\\1/3&2/3&0\\0&0&1\end{pmatrix},
 \qquad
 Q_0=\frac{\log2}{\tau}(\Pi_0-I),\qquad
 Q_H=\frac{\log2}{\tau}(\Pi_H+R-2I).
 \tag{2}
$$

Both generators have positive off-diagonal entries and satisfy ordinary
detailed balance for their respective laws. In particular, $R$ is
$\pi_H$-reversible, $R^2=R$, and
$R\Pi_H=\Pi_HR=\Pi_H$. Their dwell-time kernels are

$$
 K_0=\frac{I+\Pi_0}{2}
 =\begin{pmatrix}3/4&1/8&1/8\\1/4&5/8&1/8\\1/4&1/8&5/8\end{pmatrix},
$$

$$
 K_H=\frac I4+\frac R4+\frac{\Pi_H}{2}
 =\begin{pmatrix}
 13/30&11/30&1/5\\11/60&37/60&1/5\\1/10&1/5&7/10
 \end{pmatrix}.
 \tag{3}
$$

All preparations in this example are exactly $\pi_0$. No preparation
error or unknown mixing time is used to produce the obstruction.

## 2. A repeatable instrument with an error-correlated hidden kick

Let the initial electronic error have probability $p=1/100$. Each use
draws a fresh Bernoulli error $E$, independently of earlier draws and
the hidden state before that use, and records $I=S(-1)^E$. The instrument
never changes $S$. In the singleton negative sector it leaves the hidden
state alone. In the positive sector, it resets the two hidden states to

$$
 \zeta_{\rm error}=(1,0),\qquad
 \zeta_{\rm correct}=(49/99,50/99),
 \tag{4}
$$

according to whether $E=1$ or $E=0$. This is a valid classical stochastic
instrument. Its recorded bit has exactly the prescribed binary symmetric
channel conditional on the true input bit. Its hidden kick is correlated
with that electronic error. The two effects can share measurement noise;
the subsequent control word does not depend on the recorded outcome.

The average conditional reset law is

$$
 p\zeta_{\rm error}+(1-p)\zeta_{\rm correct}=(1/2,1/2).
$$

Consequently its nonselective hidden channel is

$$
 D=\begin{pmatrix}1&0&0\\0&1/2&1/2\\0&1/2&1/2\end{pmatrix},
 \qquad \pi_0D=\pi_0.
 \tag{5}
$$

This does not establish the required joint law. In row order $I=-1,+1$
and column order of the three hidden states, the actual label/state law
and the reference law for nondisturbing readout with independent
electronics are

$$
 G=\begin{pmatrix}99/200&1/200&0\\1/200&49/200&1/4\end{pmatrix},
 \qquad
 G_* =\begin{pmatrix}99/200&1/400&1/400\\1/200&99/400&99/400\end{pmatrix}.
 \tag{6}
$$

They have identical visible and hidden marginals, but

$$
 \operatorname{TV}(G,G_*)=\frac1{200}=0.005.
 \tag{7}
$$

The example violates the independent-electronics/current-dynamics
premise of the memory witness. A marginal detector error rate of one
percent does not imply that premise. Nor does nonselective stationarity
imply stationarity conditional on each recorded outcome.

## 3. Which observable checks agree exactly

**Immediate repeated readout.** Since every operation preserves $S$,
any number of zero-delay records has, conditional on that true bit,
exactly the product law of independent binary symmetric errors with
probability $p$. This is precisely the law of repeated nondisturbing
readout with independent electronics. The hidden kicks are invisible
to these records. Perfect preservation of the underlying bit is already
built into the example; uncertainty about visible transitions is not
responsible for the failure.

**Nonselective endpoint insertion.** Starting from $\pi_0$, inserting
the instrument and discarding its record leaves every later endpoint
law unchanged, for every fixed future stochastic observation channel
$A$, because $\pi_0DA=\pi_0A$. Repeating such insertions before the
future channel has the same property. This statement does not cover
arbitrary insertions during a nonstationary high-field trajectory.

**Low-only records.** The low-field process is strongly lumpable by
$S$: its total transition rate into the opposite sector is
$(\log2)/(2\tau)$ from every state. Its complete binary path law is
therefore independent of the hidden distribution inside a sector. The
instrument preserves that sector and uses fresh errors. All low-only
recorded processes, including arbitrary measurement spacings and
repetitions, agree with the reference instrument.

**Response-preparation checks.** The preparation is already stationary.
An extra low tick before either original word leaves it unchanged, as
does an unrecorded application of (5) followed by that tick. Thus the
usual equal-response preparation checks pass exactly. They establish
no independence between the retained initial electronic bit and its
subsequent hidden kick.

## 4. The two original joint tables nevertheless differ

Use a noiseless final readout, and compare the instrument above with
nondisturbing initial readout having the same $p=1/100$. The two tables
have rows given by the initial recorded sign and columns by the final
sign, both ordered $-1,+1$.

$$
 P_{0H}=\frac1{9600}
 \begin{pmatrix}1724&3076\\1036&3764\end{pmatrix},
 \qquad
 P_{0H}^*=\frac1{9600}
 \begin{pmatrix}1723&3077\\1037&3763\end{pmatrix},
$$

$$
 P_{H0}=\frac1{9600}
 \begin{pmatrix}2234&2566\\1546&3254\end{pmatrix},
 \qquad
 P_{H0}^*=\frac1{9600}
 \begin{pmatrix}2233&2567\\1547&3253\end{pmatrix}.
 \tag{8}
$$

Both initial and final marginals agree. Each initial--final correlation
changes by $1/2400=p/24$, and

$$
 \operatorname{TV}(P_{0H},P_{0H}^*)
 =\operatorname{TV}(P_{H0},P_{H0}^*)
 =\frac1{4800}>10^{-5}.
 \tag{9}
$$

Thus the calibration checks above do not certify the existing
$10^{-5}$ joint-instrument allowance. This is a comparison of two
instruments on one ordinary model, not a claim that either table pair
passes the selected target's empirical gates.

The phenomenon does not require a singular instantaneous reset. Replace
each conditional reset in (4) by
$(I+\Pi_{\zeta})/2$ inside the positive sector. This is the finite-time
kernel of $\Pi_{\zeta}-I$ over duration $\log2$. Nonselective
stationarity, visible preservation and all listed calibration agreements
persist, while the differences in (6) and (8) are halved.
The resulting joint-table TV is still $1/9600>10^{-5}$. The conditional
measurement dynamics remain correlated with the electronic outcome.

## 5. A positive endpoint lemma under the missing structural premise

There is a useful converse for at most three hidden states. Let $S$
have two nonempty sectors, let $\nu$ be any preparation, and let $D$
preserve $S$ exactly. The instrument records the input true bit and then
applies $D$. Its optional electronic channel $B(i\mid S)$ must be
independent of the hidden update and future evolution. Let $A$ be any
fixed future stochastic channel, including the active word and final
electronics, without feedback from the initial record.

Write $J_D,J_I$ for the full recorded-initial-bit/future-output laws with
and without $D$. Then

$$
 \boxed{\operatorname{TV}(J_D,J_I)
       =\operatorname{TV}(\nu DA,\nu A).}
 \tag{10}
$$

With two states, both sectors are singletons and $D=I$. With three
states, only one sector can contain more than one state; call its sign
$s_*$. The singleton sector is unchanged, so the signed endpoint
displacement $\delta=(\nu D-\nu)A$ comes entirely from the $s_*$
sector. The joint displacement is exactly
$B(i\mid s_*)\delta(o)$. Summing its absolute values over $i,o$
gives (10). No stationarity, reversibility, mixing bound or knowledge
of the hidden conditional distribution is needed for this identity.

If the probability of changing sectors during $D$ is at most
$\epsilon$ under $\nu$, the same assumptions give the weaker bound

$$
 \operatorname{TV}(J_D,J_I)
 \le\operatorname{TV}(\nu DA,\nu A)+2\epsilon.
 \tag{11}
$$

To prove it, redirect every sector-changing transition of $D$ back to
its input state, producing a sector-preserving channel. This repair
changes both the joint law and its endpoint marginal by at most
$\epsilon$; apply (10) and the triangle inequality.

Equations (10)--(11) can support a calibration comparing future endpoints
with and without an unrecorded initial measurement, but only under the
stated structural premises. The unrecorded insertion must realize the
same nonselective operation as the recorded measurement. At unknown preparation $\nu$,
the endpoint test controls disturbance at that same $\nu$; transferring
it to an equilibrium reference requires the separate preparation
argument. In particular, it does not automatically certify the
instrument at $\pi$ from its behavior at a different hidden law.

The counterexample in Sections 1--4 satisfies exact sector preservation
but fails the electronic-independence premise, so it does not contradict
(10). A defensible physical realization can place electronic errors
downstream of a protected measurement interaction, or establish that
each outcome-conditioned hidden operation preserves the relevant
conditional equilibrium law. These are explicit properties of the
instrument. The listed binary calibration records do not prove them.
