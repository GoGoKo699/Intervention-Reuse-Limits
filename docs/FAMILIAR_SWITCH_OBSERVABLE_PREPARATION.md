# Observable preparation bounds for a small-state null

**Status:** a supporting calibration theorem for an optional five-type
experiment. It extends the exact-balance argument in the
[preparation-boundary note](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) to
approximate balance and unknown fixed symmetric detector errors. It
controls the equilibrium bias of specified responses without a rival
mixing-time assumption. It does not replace the current five-million-trial
test, establish a five-type state-count advantage, or certify the initial
instrument from observed data.

The new experiment retains the two original snapshot types and adds a low
calibration pair and two low-prefixed snapshot types. A sufficiently long
low calibration dwell can make the observable relaxation guard useful;
its duration need not equal the active pulse duration. Every conclusion
below is conditional on measured population quantities or valid confidence
bounds for them. No robust target power or numerical trial count follows
from the deterministic theorem alone.

## 1. A refined approximate-balance lemma

Let $K$ be a stochastic kernel on at most three states, with stationary
law $\pi$, and let $S$ be a deterministic binary readout. For an arbitrary
preparation law $\nu$, put

$$
 v=\pi S,\qquad b=\nu S,\qquad a=\nu KS,\qquad
 r=1-\nu S K S.
 \tag{1}
$$

In the correlation, the first $S$ denotes multiplication by its state
value. Suppose $|v|\le V<1$ and $r>0$. Define

$$
 C_V=\frac{1+V}{1-V}.
$$

For any real response function $f$ with oscillation
$L=\max_xf(x)-\min_xf(x)$,

$$
 \boxed{
 |(\nu-\pi)f|
 \le\frac{4C_V}{r}
       \left[|\nu(K-I)f|+\frac L2|a-b|\right]
       +\frac{L}{1-V}|b-v|.}
 \tag{2}
$$

The stationary imbalance term is not multiplied by $1/r$. This matters
when the null already permits $|v|\le10^{-4}$. No reversibility, rate cap,
minimum stationary mass, or hidden-state mixing estimate is used in (2).

### Proof

Both readout sectors are nonempty because $|v|<1$. With two states,
$|(\nu-\pi)f|\le L|b-v|/2$, so (2) follows immediately. With three
states, one readout sector is a singleton. Relabel states and, if necessary,
reverse the signs of $S$, so $S=(-1,+1,+1)$. All bounds in (2) are
unchanged by this sign reversal.

Write $\delta=\nu-\pi$ and

$$
 \delta=d(1,-1/2,-1/2)+h(0,1,-1),\qquad d=\frac{v-b}{2}.
$$

Define

$$
 \alpha_i=K_{i0}\ (i=1,2),\quad
 a_0=K_{01}+K_{02},\quad
 \beta=K_{12}+K_{21},\quad
 k=\frac{\alpha_1+\alpha_2}{2}+\beta,
$$

$$
 B=f_0-\frac{f_1+f_2}{2},\qquad
 \Delta=f_1-f_2,\qquad
 \tau=\frac{K_{01}-K_{02}}2+
       \frac{\alpha_1-\alpha_2}4+
       \frac{K_{12}-K_{21}}2.
$$

Direct subtraction of the three kernel rows gives

$$
 k\delta f=-\nu(K-I)f-\frac{a-b}{2}B
                  +d[kB+\tau\Delta].
 \tag{3}
$$

Stationarity is used to replace $\delta(K-I)$ by $\nu(K-I)$.
The final bracket is a zero-sum functional with coefficient row
$(k,-k/2+\tau,-k/2-\tau)$. Its $\ell_1$ norm is
$k+\max(k,2|\tau|)$. Since $2|\tau|\le a_0+k$, this norm is at
most $2k+a_0$. Consequently

$$
 |kB+\tau\Delta|\le L(k+a_0/2),\qquad |B|\le L.
 \tag{4}
$$

Stationarity at state zero, whose mass is $(1-v)/2$, implies

$$
 a_0=\frac{\pi_1\alpha_1+\pi_2\alpha_2}{\pi_0}
 \le\frac{1+v}{1-v}\max(\alpha_1,\alpha_2)
 \le2k\frac{1+v}{1-v}.
 \tag{5}
$$

Combining (3)--(5) first yields the sharper orientation-specific bound

$$
 |\delta f|\le
 \frac{|\nu(K-I)f|+(L/2)|a-b|}{k}
       +\frac{L}{1-v}|b-v|.
 \tag{6}
$$

The readout-flip probability under $\nu$ is
$\nu_0a_0+\nu_1\alpha_1+\nu_2\alpha_2$. Using (5) before its
last inequality bounds this probability by
$\max(\alpha_1,\alpha_2)(1-bv)/(1-v)$. Thus

$$
 r\le4k\frac{1-bv}{1-v}\le4kC_V.
 \tag{7}
$$

In particular $k>0$. Substitution into (6), with
$1/(1-v)\le1/(1-V)$, proves (2). The same uniform constants cover
the opposite singleton orientation.

## 2. The instrument and the five protocol types

The initial instrument first labels the true initial sign $S(x)$ and
then applies a fixed stochastic hidden-state kernel $\mathcal D$. In
this supporting theorem it is **exactly protected**:

$$
 \mathcal D(x,y)=0\ \text{if }S(x)\ne S(y),\qquad
 \pi\mathcal D=\pi.
 \tag{8}
$$

These conditions allow arbitrary hidden motion inside each sector. They
ensure that the stationary initial-label/postmeasurement-state joint law
is the ideal stationary joint law. They are model premises, not observed
consequences of calibration.

Let $P$ be the selected low-field evolution kernel, with $\pi P=\pi$.
Define the effective calibration kernel

$$
 K=\mathcal D P.
 \tag{9}
$$

It is stationary for $\pi$. Let $A_w$ be the fixed channel from the
prepared hidden state to the recorded initial/final pair of original word
$w\in\{0H,H0\}$. It includes that word's usual initial instrument.
The preparation $\nu$, active kernels, instruments and detector channels
must be shared across the following types.

| Type | Operations after the common preparation | Recorded output law |
| --- | --- | --- |
| $0H$ | Usual initial instrument, then $0H$ | $\nu A_{0H}$ |
| $H0$ | Usual initial instrument, then $H0$ | $\nu A_{H0}$ |
| Low pair | Initial label and $\mathcal D$, then $P$, then final readout | Low initial/final pair |
| Prefixed $0H$ | Silent $\mathcal D$, then $P$, then the usual $0H$ experiment | $\nu K A_{0H}$ |
| Prefixed $H0$ | Silent $\mathcal D$, then $P$, then the usual $H0$ experiment | $\nu K A_{H0}$ |

“Silent” means performing the same physical instrument operation without
retaining its label; recording and discarding that label is equivalent.
The usual initial instrument is subsequently performed at the start of
the original word. Thus each prefixed type uses an additional instrument
operation. Its duration and control cost are resources. Omitting that
operation would test a different kernel and would not justify (2) with
the measured low-pair correlation.

The two electronic errors are independent fixed binary symmetric channels,
with contrasts $\alpha,\beta\in[0,1]$. They are independent of the
instrument's hidden-state motion, the dynamics and each other. The same
contrasts are used for all five types. In particular the low-pair moments
are

$$
 i=\alpha b,\qquad j=\beta a,\qquad
 c_K=\alpha\beta\,\nu S K S.
 \tag{10}
$$

An equilibrium-only instrument error allowance does not justify these
identities for an arbitrary unknown preparation and an unmatched prefix.
The current robust score test permits a small nonzero stationary joint
instrument error. That larger instrument class is not silently imported
into the exact theorem here. A fixed arbitrary instrument may be included
inside a response channel $A_w$, but its equilibrium table need not obey
the ideal stationary witness, as the
[instrument counterexample](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md)
shows.

## 3. Observable detector and relaxation guards

Every recorded pair correlation has absolute value at most
$\gamma=\alpha\beta$. Therefore, if either original correlation has
absolute value at least $g>0$, then

$$
 \gamma\ge g,\qquad \alpha\ge g,\qquad\beta\ge g.
 \tag{11}
$$

Let $c_K^+=\max(c_K,0)$. Equation (10) gives

$$
 r\ge r_0:=1-\frac{c_K^+}{g}.
 \tag{12}
$$

When $c_K<0$, the weaker bound $r\ge1$ suffices for (12). A positive
$r_0$ is an observable relaxation condition. No detector calibration value
is presumed known. A low-pair correlation by itself cannot provide this
condition: its attenuation could entirely arise from detector noise.
The useful comparison is a lower contrast-product bound from one pair
and a smaller correlation after the calibration kernel.

A simple sufficient guard is

$$
 g=\frac9{20}=.45,\qquad c_K\le\frac3{20}=.15,
 \qquad r_0=\frac23.
 \tag{13}
$$

These are observed guards, not a claim that every member of the present
target family passes them with a specified measurement budget. Increasing
the calibration low dwell may help the target satisfy the correlation
guard while leaving its stationary response tables invariant. The theorem
does not assert a uniform equilibration time for ordinary rivals.

## 4. A score-specific preparation certificate

Use the fixed per-arm scores of the
[one-percent score test](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md):

$$
 X_A=.4Y+.6IY-.3I,\qquad
 X_B=-.4Z-.48JZ+.3J.
$$

Let $F(x)$ be the sum of their conditional expectations given prepared
hidden state $x$. The two initial-only terms cancel pointwise because
the initial instrument and detector are shared. If $H_A,H_B$ denote the
conditional latent final means after the corresponding initial instrument
and word, then

$$
 F(x)=\beta\{[.4+.6\alpha S(x)]H_A(x)
              -[.4+.48\alpha S(x)]H_B(x)\}.
$$

Since $|H_A|,|H_B|\le1$, $|F|\le1.88\beta$ and
$\operatorname{osc}(F)\le3.76\beta$. Define the observable signed
score drift

$$
 d_F=\nu(K-I)F
 =\mathbb E X_A^{\rm prefix}+\mathbb E X_B^{\rm prefix}
  -\mathbb E X_A-\mathbb E X_B.
 \tag{14}
$$

The signed sum is taken before its absolute value. From (10)--(11),

$$
 \beta|a-b|\le|j|+\frac{|i|}{g},\qquad
 \beta|b-v|\le\frac{|i|}{g}+V.
$$

Thus (2) gives the entirely observable bound

$$
 \boxed{
 |(\nu-\pi)F|\le B_F:={4C_V\over r_0}
 \left[|d_F|+{47\over25}\left(|j|+{|i|\over g}\right)\right]
 +{94\over25(1-V)}\left({|i|\over g}+V\right).}
 \tag{15}
$$

The constant $-.08$ in the complete score has no preparation drift and
needs no further term. With $V=10^{-4}$ and (13),

$$
 {4C_V\over r_0}={20002\over3333},\qquad
 B_F\big|_{d_F=i=j=0}={94\over249975}
 \simeq .000376038.
 \tag{16}
$$

This conservative nonzero floor reflects the admitted stationary
imbalance and the unknown detector contrasts. It is smaller than the
nominal target score floor but does not by itself prove a rejection test:
confidence errors, localization and target acceptance must also be paid.
It must not be substituted into an old threshold without a new analysis.

## 5. Moment bounds needed for localization

The ordinary stationary score ceiling is local in the four moments, so
a score-only drift bound cannot by itself invoke it. The same five types
also measure each moment's original-to-prefix difference.

For a recorded final mean $m_w$, let $d_{m_w}$ be that difference.
Its response function has oscillation at most $2\beta$. Hence

$$
 |m_w(\nu)-m_w(\pi)|\le B_{m_w}:=
 {4C_V\over r_0}\left[|d_{m_w}|+|j|+{|i|\over g}\right]
 +{2\over1-V}\left({|i|\over g}+V\right).
 \tag{17}
$$

For a recorded pair correlation $c_w$, its response has oscillation at
most $2\alpha\beta$. The additional factor $\alpha$ improves the
detector conversion:
$\alpha\beta|a-b|\le|j|+|i|$ and
$\alpha\beta|b-v|\le|i|+V$. Consequently

$$
 |c_w(\nu)-c_w(\pi)|\le B_{c_w}:=
 {4C_V\over r_0}\left[|d_{c_w}|+|j|+|i|\right]
 +{2\over1-V}(|i|+V).
 \tag{18}
$$

Apply (17) to $M,L$ and (18) to $C,D$. The stationary quantities
$A=L+.6D$ and $Q=C-D$ then have error radii at most
$B_L+.6B_D$ and $B_C+B_D$, respectively. A sufficient localization
check is that the entire resulting stationary enclosure lie inside the
inherited ordinary local box, including its $Q$ condition, and satisfy
$M>1/5$, $A>2/5$ throughout. Under all of the inherited stationary
force-law promises, its score is then below $.00007$. Equation (15)
provides the additional preparation contribution to an observable null
ceiling. This is a deterministic implication, not a completed statistical
test or a new memory-separation claim.

## 6. Sampling and scope

The deterministic statements use one shared preparation law $\nu$.
Sequential data need not have independent hidden preparations, but a
sampling argument must recover genuinely shared response averages. One
possible design randomly assigns a type only after the common preparation,
independently of its hidden state and the past. With fixed kernels and
channels, suitable martingale estimates can then refer to one pathwise
average preparation. The [calibration sampling-cost note](FAMILIAR_SWITCH_CALIBRATION_SAMPLING_COST.md)
proves that statistical reduction and gives a conservative precision
certificate, rather than a complete test or power claim. Merely
interleaving the five types is insufficient.

The [readout-calibration boundary](FAMILIAR_SWITCH_CALIBRATION_READOUT_BOUNDARY.md)
explains why independent electronic errors and the joint instrument
condition remain substantive premises.

These observable checks concern the probed responses. They do not certify
hidden-state total variation, an arbitrary instrument, or a full visible
trajectory model. They also change experimental resources: five types,
longer calibration evolution and extra silent instrument operations are
used. No prior two-type sample count or three-state construction is
asserted to transfer. Manuscript drafting remains deferred.
