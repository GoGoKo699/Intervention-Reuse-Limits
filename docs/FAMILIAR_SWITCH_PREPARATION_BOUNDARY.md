# What observable preparation checks can and cannot replace

The [two-snapshot witness](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) needs
preparation and instrument assumptions. Binary balance and even complete
low-field binary trajectory data do not establish the needed preparation
property. Likewise, unchanged endpoint distributions after an initial
measurement do not establish that its recorded bit retains the required
correlation with the subsequent state.

There is nevertheless a useful alternative for preparation: under the
at-most-three-state null and exact balance, one extra low tick can test
the stationarity of each particular future response. Together with an
observed low-field relaxation lower bound, these tests control the
preparation error for the tested joint tables. This adds three protocol
types. It does not remove the instrument premise or replace the shorter
two-protocol result.

**Status:** the elementary arguments and rational fixtures below have
passed independent internal mathematical review. This note establishes a
boundary and an optional change in experimental resources. It makes no
new sampling-cost or calibrated-operating-point claim.

## 1. An equilibrium-looking low-field record can hide preparation bias

Take three states with readout $S=(+1,-1,-1)$ and

$$
 \pi_0=(1/2,1/4,1/4),\qquad
 \nu=(1/2,1/8,3/8),\qquad u=4/5,\qquad
 \pi_H=(9/10,1/20,1/20)=\pi_0(1+uS).
 \tag{1}
$$

The actual preparation $\nu$ is balanced and strictly positive but differs
from $\pi_0$. The two unit-time kernels are

$$
 E_0=\begin{pmatrix}
 3/4&1/8&1/8\\1/4&5/8&1/8\\1/4&1/8&5/8
 \end{pmatrix},\qquad
 E_H=\begin{pmatrix}
 89/95&29/760&1/40\\
 261/380&219/760&1/40\\
 9/20&1/40&21/40
 \end{pmatrix}.
 \tag{2}
$$

These are ordinary reversible continuous-time propagators, not merely
abstract stochastic matrices. Let $\Pi_0,\Pi_H$ denote the row-constant
reset matrices for their respective stationary laws, and put

$$
 R=\begin{pmatrix}
 18/19&1/19&0\\18/19&1/19&0\\0&0&1
 \end{pmatrix},\qquad
 Q_0=(\log2)(\Pi_0-I),\qquad
 Q_H=(\log2)(\Pi_H+R-2I).
 \tag{3}
$$

The off-diagonal rates are positive. The matrix $R$ is $\pi_H$-reversible,
$R^2=R$, and $\Pi_HR=R\Pi_H=\Pi_H$. Consequently

$$
 e^{Q_0}=(I+\Pi_0)/2=E_0,\qquad
 e^{Q_H}=I/4+R/4+\Pi_H/2=E_H.
 \tag{4}
$$

Detailed balance holds at both fields. At low field the readout process
is strongly lumpable: every hidden state of a given readout has the same
total rate into the other readout sector. Its binary generator is

$$
 \frac{\log2}{2}
 \begin{pmatrix}-1&1\\1&-1\end{pmatrix}.
 \tag{5}
$$

Since $\nu$ and $\pi_0$ have the same binary marginal, **all low-only
binary trajectory laws agree**, including observations at arbitrary
times. Such data cannot distinguish the hidden preparation bias. The
high field does distinguish it.

Start both chronological protocols $0,H$ and $H,0$ from $\nu$, and use
ideal noninvasive initial and final observations. Direct matrix
multiplication gives

$$
 (m,c,\ell,d)=
 \left(\frac{723}{1520},\frac{65}{304},
       \frac{339}{1520},\frac{65}{304}\right).
 \tag{6}
$$

For the stationary-preparation witness polynomial

$$
 F_\sigma=uc-u(1+\sigma m)d+\sigma(u-m)\ell,
 \tag{7}
$$

these moments yield

$$
 F_- =\frac{20853}{2310400}>0,\qquad
 F_+ =-\frac{20853}{2310400}<0.
 \tag{8}
$$

Thus an ordinary three-state model can violate both stationary-preparation
branches if its hidden preparation is unvalidated. This example is not a
fit to the selected target tables. It isolates the preparation premise.
For any specified finite wait, slowing $Q_0$ can retain a non-negligible
hidden bias, while all low-only binary records still look exactly like
equilibrium. A finite wait alone supplies no uniform guarantee over
arbitrarily slow rivals.

## 2. Endpoint-only disturbance checks miss a recorded correlation

An even simpler example separates marginal stationarity from an adequate
initial instrument. Use two states $S=\pm1$, balanced $\pi_0$, and
$\pi_H=\pi_0(1+uS)$, with ordinary reversible continuous-time kernels
satisfying

$$
 E_0S=aS,\qquad E_HS=u(1-b)+bS,
 \qquad 0<a,b<1,\quad 0<u<1.
 \tag{9}
$$

For example, reset generators
$Q_0=-(\log a)(\Pi_0-I)$ and
$Q_H=-(\log b)(\Pi_H-I)$ give these unit-time kernels.
Start at $\pi_0$. The initial instrument first records the true bit
$I=S(X_0)$ and then resets the hidden state independently to $\pi_0$.
The nonselective disturbance is $D=\Pi_0$.

This instrument preserves the equilibrium hidden marginal exactly.
Every subsequent endpoint law, for every control protocol, is identical
with and without this nonselective instrument. Initial binary balance
also agrees. Nevertheless the recorded initial bit is now independent
of the subsequent trajectory. The two snapshot tables have moments

$$
 (m,c,\ell,d)=
 \bigl(u(1-b),\ 0,\ au(1-b),\ 0\bigr),
 \qquad F_\sigma=\sigma a u^2b(1-b)\ne0.
 \tag{10}
$$

Hence unchanged endpoint laws, even if checked exhaustively, do not
justify the snapshot covariance identity. This counterexample concerns
that identity; it is not asserted to pass the fixed target's score gates.

The relevant instrument object is the **joint law of the recorded initial
bit and the postmeasurement hidden state**, rather than just the latter's
marginal. A sufficient weaker condition than a worst-state disturbance
bound is that this joint law equal, or be close in TV to,
$\pi_0(x)\mathbf1\{i=S(x)\}$. Subsequent evolution and final readout
are a stochastic channel on this joint law, so its TV error bounds every
resulting snapshot-table error. Large hidden changes can be harmless:
an instrument that preserves $S$ and each conditional equilibrium law
$\pi_0(\cdot\mid S)$ leaves that joint law unchanged at equilibrium.
These are instrument properties, not consequences of an unchanged visible
marginal or of short measurement duration.

## 3. A response-specific preparation bound for small rivals

Here is a positive result that uses the state-count restriction. Let $K$
be a stochastic kernel on at most three states, with stationary law
$\pi$. Let $S$ be a deterministic binary readout and $\nu$ the actual
preparation. Assume

$$
 \pi S=\nu S=0,\qquad
 r=1-\nu S K S>0.
 \tag{11}
$$

The product notation means $\nu S K S=\mathbb E_\nu[S_0S_1]$.
No reversibility, rate bound, stationary minimum-mass bound, or mixing-time
estimate is required for the following lemma. For every $|f|\le1$,

$$
 \boxed{\displaystyle
 |(\nu-\pi)f|\le
 \frac{4}{r}\bigl(|\nu(K-I)f|+|\nu KS|\bigr).}
 \tag{12}
$$

With two states, balance determines the entire law, so $\nu=\pi$.
With three states, one readout sector is a singleton. Relabel it as state
$0$ with $S_0=-1$, with states $1,2$ having readout $+1$. Balance implies
$\nu_0=\pi_0=1/2$ and
$\delta=\nu-\pi=(0,h,-h)$. Put

$$
 \alpha_i=K_{i0}\ (i=1,2),\quad
 \beta=K_{12}+K_{21},\quad
 k_*=(\alpha_1+\alpha_2)/2+\beta.
 \tag{13}
$$

Stationarity and direct subtraction of rows give

$$
 \begin{split}
 \nu(K-I)f
 &=-k_*\delta f+h(\alpha_1-\alpha_2)
       \left(f_0-\frac{f_1+f_2}{2}\right),\\
 \nu KS&=-2h(\alpha_1-\alpha_2).
 \end{split}
 \tag{14}
$$

The bracket in the first line has absolute value at most two. Thus
$k_*|\delta f|\le|\nu(K-I)f|+|\nu KS|$.
Stationarity at the singleton gives
$K_{01}+K_{02}=2\pi_1\alpha_1+2\pi_2\alpha_2$.
The probability of a readout flip under $\nu$ is consequently at most
$\max(\alpha_1,\alpha_2)\le2k_*$. Since $r$ is twice that flip
probability, $r\le4k_*$. This proves (12), including positivity of the
denominator $k_*$ under (11).

The inequality controls the bias of the particular probed response $f$.
It does not claim that a finite set of such probes controls hidden-state
TV. Weak relaxation makes the bound weak: a positive observed lower bound
on $r$ is essential, so the lemma does not supply a uniform finite wait.

## 4. How to measure its premises for the two tables

Let $A_w$ be a fixed stochastic observation channel from the prepared
hidden state to the outcome of a future experiment $w$. It may return a
whole initial/final binary pair. Apply (12) to $f=A_wg$, for arbitrary
output functions $|g|\le1$, and use TV duality. This gives

$$
 \boxed{\displaystyle
 \operatorname{TV}(\nu A_w,\pi A_w)
 \le\frac{4\operatorname{TV}(\nu K A_w,\nu A_w)
                  +2|\nu KS|}{r}.}
 \tag{15}
$$

Every quantity on the right has an observable interpretation if the
preparation, low kernel and observation channel are shared across the
experiments. For the original two protocols, add these three types:

| Added type | Observation timing | Purpose |
|---|---|---|
| One low tick | Record immediately after preparation and after $K$ | Measure $r$ and the final mean $\nu KS$ |
| Extra low tick, then $0,H$ | Apply $K$ without a record; then use the original protocol's initial/final observations | Compare $\nu K A_{0H}$ with $\nu A_{0H}$ |
| Extra low tick, then $H,0$ | Apply $K$ without a record; then use the original protocol's initial/final observations | Compare $\nu K A_{H0}$ with $\nu A_{H0}$ |

The two original table types are retained. Exact equality in these
stationarity comparisons, together with $\nu KS=0$ and $r>0$, establishes
the needed equilibrium response tables for every at-most-three-state
rival, even if the hidden preparation law itself is unknown. Nonzero
population discrepancies receive exactly the deterministic allowance
in (15). This does not contradict Section 1: the new comparisons include
high-field responses, not solely low-field binary records.

This is an optional five-type experiment, not the original two-type
experiment with its assumptions silently weakened. Exact balance in
(11) remains a premise here. A finite-sample use would need simultaneous
confidence bounds for balance, the table discrepancies, the final mean,
and a strictly positive lower bound on $r$, followed by a fresh error
budget. No previous trial count is asserted to transfer.

Finally, measuring $r$ as $1-\nu SKS$ requires a noninvasive or
quantitatively calibrated joint instrument. A fixed arbitrary instrument
can be absorbed into $A_w$ for the response-preparation bound itself, but
then $\pi A_w$ is that instrument's equilibrium table; it need not satisfy
the ideal covariance identity. Section 2 shows precisely why the
preparation checks cannot resolve this separate obstacle.
