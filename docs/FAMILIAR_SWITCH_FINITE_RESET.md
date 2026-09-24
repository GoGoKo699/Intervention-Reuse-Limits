# A finite reset for the one-percent kinetic family

**Status:** a uniform target preparation bound and an explicit serial-time
budget. An actual low-field wait of **63 attempt-rate time units** prepares
the entire [one-percent kinetic family](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md)
within hidden-state total variation $10^{-5}$ of its actual low-field
stationary law, from every initial law. The bound holds conditional on any
previous measurement history. It does not make consecutive trials exactly
independent, and it does not supply the corresponding mixing guarantee for
an unrestricted ordinary rival.

## 1. Model and the reset operation

The four physical states are $(S,Z)\in\{-1,+1\}^2$, with energy
$-JSZ-hS$, $J=\log3$, and unit attempt rate for each coordinate. The actual
low field satisfies $|h_0|\le10^{-5}$. Every undirected single-coordinate
edge has its own factor $a_e\in[99/100,101/100]$, multiplying both forward
and reverse heat-bath rates. These are the actual fixed low-plateau factors
of the kinetic family. Hold that low generator fixed throughout the reset.

Its stationary law is exactly

$$
 \pi_h(s,z)=\frac{e^{Jsz+hs}}{4\cosh J\cosh h}
 =\frac{(1+\tfrac45sz)(1+s\tanh h)}4.
 \tag{1}
$$

Both the heat-bath reference $Q_h$ and the factor-perturbed generator
$\widetilde Q_h$ are reversible for this same law. The high-field factors
are irrelevant during reset and remain independently free within their
one-percent intervals.

The reset acts on whatever physical state the preceding trial and its
readout leave behind. That state may depend arbitrarily on previous
records, and need not resemble equilibrium. The four-state Markov model
must still describe the subsequent low-field evolution: persistent
environmental memory or unmodelled states are not removed by this bound.

## 2. Uniform spectral gap

Put $t=\tanh J=4/5$ and $u=\tanh h$. For the unperturbed heat-bath
generator, define

$$
 A(h)=\frac{u(1-t^2)}{1-t^2u^2},\qquad
 B(h)=\frac{t(1-u^2)}{1-t^2u^2}.
 \tag{2}
$$

The generator acts on the basis $1,S,Z,SZ$ as

$$
 Q_h1=0,\quad Q_hS=A+B Z-S,\quad Q_hZ=tS-Z,
 \quad Q_h(SZ)=B+t+A Z-2SZ.
 \tag{3}
$$

Consequently its nonzero relaxation rates are
$1-\sqrt{tB}$, $1+\sqrt{tB}$ and $2$. Since
$0\le tB\le t^2$, its spectral gap obeys

$$
 \lambda(Q_h)\ge1-t=\frac15.
 \tag{4}
$$

For every real function $f$, the reversible Dirichlet forms satisfy

$$
 \begin{split}
 \mathcal E_{\widetilde Q_h}(f,f)
 &=\frac12\sum_{x,y}\pi_h(x)a_{\{x,y\}}q_h(x,y)
          [f(y)-f(x)]^2\\
 &\ge\frac{99}{100}\mathcal E_{Q_h}(f,f).
 \end{split}
 \tag{5}
$$

The two forms use the same variance $\operatorname{Var}_{\pi_h}f$.
Taking their variational spectral-gap bounds gives the exact uniform
constant

$$
 \boxed{\lambda(\widetilde Q_h)\ge\frac{99}{500}.}
 \tag{6}
$$

No common rescaling of the four edge factors is assumed. Their upper
bound is not needed for this mixing estimate.

## 3. An actual wait of 63 units

At the allowed low fields, $|\tanh h_0|\le|h_0|\le10^{-5}$, so

$$
 \pi_{h_0,\min}\ge\frac{1-10^{-5}}{20}>\frac1{21}.
 \tag{7}
$$

Reversible $L^2(\pi)$ contraction and Cauchy--Schwarz imply, for any
initial distribution $\mu$,

$$
 \begin{split}
 \operatorname{TV}(\mu e^{L\widetilde Q_{h_0}},\pi_{h_0})
 &\le\frac12
       \sqrt{\frac1{\pi_{h_0,\min}}-1}\,
       e^{-99L/500},\\
 \operatorname{TV}(\mu e^{L\widetilde Q_{h_0}},\pi_{h_0})^2
 &\le5e^{-99L/250}.
 \end{split}
 \tag{8}
$$

For completeness, the initial $\chi^2$ divergence is
$\sum_x\mu(x)^2/\pi(x)-1\le1/\pi_{\min}-1$. The reversible
semigroup contracts its square root by $e^{-\lambda L}$; total variation
is at most half this square root. Thus (8) includes pure starting states
and all mixtures without a further preparation assumption.

At $L=63$, $99L/250=6237/250$. The finite rational inequality

$$
 \sum_{k=0}^{28}\frac{(6237/250)^k}{k!}
 >50\,000\,000\,000
 \tag{9}
$$

and the positive exponential series certify

$$
 \boxed{\sup_\mu\operatorname{TV}
   (\mu e^{63\widetilde Q_{h_0}},\pi_{h_0})<10^{-5}.}
 \tag{10}
$$

The square root of the coarse squared bound in (8) is approximately
$8.553\times10^{-6}$; this decimal is illustrative, whereas (9) is the exact
certificate. The integer wait is sufficient, not claimed optimal. The
earlier [62-unit heat-bath bound](FAMILIAR_SWITCH_PROTECTED_READOUT.md)
was restricted to equal attempt prefactors; (10) covers the full independent
one-percent box.

Condition on any previous history $\mathcal F$ before starting the reset.
Its conditional state law is some $\mu_{\mathcal F}$. The same fixed
semigroup applies and (10) is uniform in that law. Therefore

$$
 \operatorname{TV}\!\left(
  \mathcal L(X_{\rm after\ reset}\mid\mathcal F),\pi_{h_0}\right)
 <10^{-5}
 \tag{11}
$$

almost surely, even if the preceding final measurement disturbed the
hidden state arbitrarily. The **current** initial measurement still needs
its stated joint record/postmeasurement-state instrument guarantee.

Equation (11) supplies the already allocated target preparation term
$\epsilon_{p,T}=10^{-5}$. It is charged **once** in the per-trial observation
budget. The actual-to-nominal stationary-law displacement remains in the
existing field term; neither term is added a second time. A conditional
concentration argument is needed to turn this preparation statement into
a sampling theorem for a reused device.

## 4. The three-state predictor can use the same reset

The [constructive general three-state predictor](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md)
also prepares within $10^{-5}$ after 63 units, uniformly over its certified
parameter domain. This avoids granting it an ideal fresh preparation while
charging the physical target for a finite wait.

In that construction's coordinates $1,S,W$, the low-field kernel at
$\tau=5/4$ has its nonconstant block

$$
 D=\begin{pmatrix}x&z\\y&w\end{pmatrix},\qquad
 x\le.717,\ z\le.1213,\ y\le.3368,\ w\le.1729.
$$

All four entries are positive. For row vectors, use the weighted norm
$\|(p,q)\|_v=|p|+(14/25)|q|$. Its induced contraction factor is at most

$$
 \max\left\{x+\frac{14}{25}z,
                 \frac{25}{14}y+w\right\}
 \le\max\left\{\frac{24529}{31250},\frac{54203}{70000}\right\}
 <\frac{157}{200}.
$$

For any starting law $\mu$, its deviation from the predictor's stationary
law $\pi=(1/2,1/22,5/11)$ has coordinate row $(0,p,q)$ with
$p=\mu S$, $q=\mu W$. Since $|S|\le1$ and $|W|\le12/5$,
$\|(p,q)\|_v\le293/125$. The two nonconstant rows of $F^{-1}$
have ordinary $\ell_1$ norms $1$ and $25/33$, respectively. Hence
reconstruction to a signed probability row has norm at most
$(625/462)\|(p,q)\|_v$. After 50 low kernels, corresponding to
62.5 time units, direct rational arithmetic gives

$$
 \operatorname{TV}(\mu K_0^{50},\pi)
 \le\frac{1465}{924}\left(\frac{157}{200}\right)^{50}
 <\frac1{100000}.
 \tag{12}
$$

The already proved continuous-time embedding makes the remaining
half-unit a stochastic stationary semigroup, so it can only contract
total variation. The same 63-unit wait therefore suffices, conditional
on every starting history. No reversibility of this predictor is used.

The predictor is the existing nominal-field construction. Its fixed
stationary laws and the allowed residual under an actual-field tilt
retain the scope of the [kinetic proof](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md).
For either prescribed word, use a nondisturbing initial binary readout
and the same fixed independent symmetric electronic errors as the
reference target. Let the initial law be produced by this finite reset. Markov
contraction bounds its entire recorded pair's displacement from the
stationary predictor table by $10^{-5}$. Combining this with the actual
target allowance $b_T=.000078025101$ gives the per-history table bound

$$
 \operatorname{TV}(q_{T,\mathrm{word}},q_{3,\mathrm{word}})
 \le b_T+10^{-5}=.000088025101<.00009.
 \tag{13}
$$

This is a conditional two-record table guarantee for either word. It is
not a bound on the joint law of the entire serial data sequence or on
full visible paths. The previously stated static state-count interval is
unchanged; no new serial state-complexity minimum is asserted here.

## 5. The separate promise for ordinary rivals

The static ordinary-three-state lower bound needs no universal rate cap.
It continues to apply to arbitrarily slow generators. However, if every
rate of any irreducible reversible rival is multiplied by $c>0$, detailed
balance and its stationary law are unchanged, while its equilibration
time diverges as $c\downarrow0$. A target reset duration cannot establish
a uniform rival preparation bound over that class.

For serial testing, state the shared preparation promise directly: for
each candidate model, conditional on every previous history, its
post-reset hidden law is within $\epsilon_p=10^{-5}$ of that model's
**fixed** low-field stationary law. A sufficient model-level condition is

$$
 \sup_x\operatorname{TV}
   (e^{L\widehat Q_0}(x,\cdot),\widehat\pi_0)\le10^{-5}.
 \tag{14}
$$

The target satisfies (14) at $L=63$. Rivals require their own justification
of (14), or of the direct conditional preparation promise. For a
reversible rival, known constants $\widehat\lambda>0$ and
$\widehat\pi_{\min}>0$ suffice whenever
$\tfrac12\sqrt{\widehat\pi_{\min}^{-1}-1}
 e^{-\widehat\lambda L}\le10^{-5}$. This is a lower mixing guarantee,
not an upper rate cap. No minimum stationary mass or target spectral gap
is silently imposed on all rivals.

Conditional preparation restricts the serial statistical null; it does
not strengthen the previously proved static state-count lower bound.
Initial visible balance alone does not certify hidden-state preparation.

## 6. Serial exposure and readout cost

Use one reset before every trial, including the first trial. The two words
each contain two active dwells of $5/4$. For five million trials on one
device, a fixed actual reset of 63 units gives

$$
 \begin{array}{lr}
 \text{reset exposure}&315\,000\,000,\\
 \text{nominal active exposure}&12\,500\,000,\\
 \text{total reset plus active exposure}&327\,500\,000.
 \end{array}
 \tag{15}
$$

Allowing both active dwells to exceed their nominal duration by
$\epsilon_t=10^{-5}$ raises the last upper bound by at most 100 units,
to $327\,500\,100$. These are dimensionless attempt-rate time units,
not seconds. If the common physical attempt rate is $\alpha$ per second,
divide these exposures by $\alpha$ to obtain seconds. No numerical
physical rate is assumed or inferred.

There are ten million binary readouts. Their durations, switching and
other implementation overhead must be added separately. For readout
durations $t_{\rm i}$ and $t_{\rm f}$ in seconds, their contribution is
$5\times10^6(t_{\rm i}+t_{\rm f})$. The protected-readout assumption
can allow a long measurement without increasing its ideal disturbance;
it does not make the measurement duration zero.

The reset lower bound concerns **actual** elapsed low-field time. If the
reset clock itself has error at most $\epsilon_{\rm r}$, scheduling a
nominal duration $63+\epsilon_{\rm r}$ guarantees (10), with actual
reset at most $63+2\epsilon_{\rm r}$. Thus its additional worst-case
serial cost is $10^7\epsilon_{\rm r}$ attempt units. For example,
$\epsilon_{\rm r}=10^{-5}$ adds another 100 units. This is an explicit
clock allowance, not an assumption inherited automatically from the
active-dwell tolerance.

The finite reset removes a target preparation idealization under the
specified four-state Markov dynamics. Physical calibration, the rival
preparation promise, the initial instrument, detector conditions and the
conditional sampling theorem remain separate obligations. Manuscript
drafting remains deferred.
