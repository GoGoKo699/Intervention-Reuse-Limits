# Four endpoint experiments expose the cost of ordinary reversibility

The two coupled conformational switches already studied in this repository
admit a simpler memory witness when both field equilibria can be prepared.
Four occupation probabilities suffice. The obstruction is a conditional
covariance: a readout sector containing only one state cannot retain the
two response propensities whose covariance the experiment measures.

This changes one experimental resource. The earlier
[seven-experiment witness](FAMILIAR_SWITCH_FINITE_MARGIN.md) used only the
low-field equilibrium preparation. This note uses both low- and high-field
equilibrium preparations, with one shared predictor required to explain
all four experiments. The readout, physical target, and two field values
remain the same.

The universal analytic argument and exact rational certificate have passed
independent internal review. The numerical enclosures are essential
premises for the explicit margins below; this is not external peer review
or a claim of certified priority.

[Exact verifier](../scripts/verify_switch_preparation_witness.py) ·
[Certificate report](../reports/switch_preparation_witness.json) ·
[Source and scope audit](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md) ·
[Preparation and sampling costs](FAMILIAR_SWITCH_PREPARATION_COST.md)

## 1. The experiment and the comparison class

The target has two time-even conformational variables $S,Z\in\{-1,1\}$,
energy $-JSZ-hS$, and equal unit-attempt heat-bath dynamics. Write

$$
 t=\tanh J,\qquad u=\tanh H,\qquad J,H>0.
 \tag{1}
$$

Let $E_0$ and $E_H$ denote evolution for fixed positive times $a_0$ and
$a_H$ at the respective fields. The two durations may differ. Let $\pi_0$
and $\pi_H$ be their equilibrium laws. The four measured means are

| Symbol | Preparation | Chronological field sequence |
|---|---|---|
| $m$ | $\pi_0$ | $H$ |
| $a$ | $\pi_H$ | $0$ |
| $b$ | $\pi_H$ | $0,H$ |
| $\ell$ | $\pi_0$ | $H,0$ |

Thus $m=\pi_0E_HS$, $a=\pi_HE_0S$, $b=\pi_HE_0E_HS$, and
$\ell=\pi_0E_HE_0S$. An occupation probability is $(1+\text{mean})/2$.
The maximum active duration is $a_0+a_H$, with at most two field plateaus.
Preparation waits are a separate resource.

Every rival has one finite state space, one deterministic $\pm1$ readout,
and a common equilibrium force law

$$
 \pi_0S=0,\qquad \pi_H(x)=\pi_0(x)(1+uS(x)).
 \tag{2}
$$

Its two preparations are these two stationary laws. In the ordinary class,
its field kernels satisfy detailed balance for the corresponding laws.
There is no restriction on the rival graph or transition rates. Indeed,
the lower bound permits arbitrary reversible stochastic kernels, whether
or not they are continuous-time propagators. In the unrestricted class,
the laws must still be stationary, but detailed balance is not required.

The shared tilt (2) is substantive: the applied field couples only to the
observed conformation. Allowing arbitrary unrelated high-field stationary
laws is a different comparison. No complete trajectory law is required to
match; the task concerns only these four endpoint means.

## 2. A conditional covariance obtained from four means

For an arbitrary ordinary rival, put

$$
 F=E_HS,\qquad G=E_0S.
 \tag{3}
$$

Stationarity, (2), and low-field detailed balance give

$$
\begin{aligned}
 \langle F\rangle_0&=m,&\quad \langle G\rangle_0&=0,\\
 \langle SF\rangle_0&=(u-m)/u,&
 \langle SG\rangle_0&=a/u,\\
 \langle GF\rangle_0&=(b-m)/u.
\end{aligned}
\tag{4}
$$

High-field detailed balance supplies the remaining mixed moment. Using
$\pi_0=\pi_H(1-uS)/(1-u^2)$,

$$
 (1-u^2)\ell
 =a-u\langle GF\rangle_0-u^2\langle SGF\rangle_0,
 \tag{5}
$$

and hence
$\langle SGF\rangle_0=[a-b+m-(1-u^2)\ell]/u^2$.
For example, the crucial step is
$\langle S,E_HG\rangle_H=\langle E_HS,G\rangle_H$;
this uses the same high-field kernel on both sides.

Define two quadratic response expressions

$$
 \boxed{\mathcal F_\sigma
 =b-m-a+\ell+\sigma(u\ell-am),\qquad \sigma=\pm1.}
 \tag{6}
$$

Since the two readout sectors each have baseline mass $1/2$, equations
(4)–(5) give the exact identity

$$
 \boxed{\mathcal F_\sigma
 =-\frac{\sigma u^2}{1-\sigma u}
   \operatorname{Cov}_{\pi_0}(G,F\mid S=\sigma).}
 \tag{7}
$$

No reconstructed generator, determinant, matrix inverse, or limiting
operation appears in (7). A singleton readout sector has zero conditional
covariance. Every model with at most three states and both readout values
present has a singleton sector. Consequently every such ordinary rival
satisfies

$$
 \mathcal F_+=0\quad\text{or}\quad\mathcal F_-=0.
 \tag{8}
$$

This is a universal necessary identity, rather than a test against a
fitted family of small generators.

## 3. The physical target has nonzero covariance in both sectors

The exact mean closure of the target gives

$$
\begin{gathered}
 B=\frac{t(1-u^2)}{1-t^2u^2},\qquad \kappa=\sqrt{tB},\\
 \beta=e^{-a_H}\cosh(\kappa a_H),\qquad
 \gamma=e^{-a_H}\frac{B}{\kappa}\sinh(\kappa a_H),\\
 c_0=e^{-a_0}\cosh(ta_0),\qquad
 d_0=e^{-a_0}\sinh(ta_0),\\
 F=m+\beta S+\gamma Z,\qquad G=c_0S+d_0Z.
\end{gathered}
\tag{9}
$$

At zero field, $\mathbb E[Z\mid S=\sigma]=\sigma t$ and
$\operatorname{Var}(Z\mid S=\sigma)=1-t^2$. Therefore

$$
 \operatorname{Cov}_0(G,F\mid S=\sigma)
 =d_0\gamma(1-t^2)>0
 \tag{10}
$$

for both signs and all finite $J,H,a_0,a_H>0$. In particular,

$$
 \mathcal F_-^*=\frac{u^2d_0\gamma(1-t^2)}{1+u}>0,
 \qquad
 \mathcal F_+^*=-\frac{u^2d_0\gamma(1-t^2)}{1-u}<0.
 \tag{11}
$$

The same unobserved conformation changes both subsequent responses.
Within either observed sector its equilibrium variance remains positive.
Ordinary detailed balance makes that shared dependence accessible through
the reversed two-plateau experiments; a singleton sector cannot supply it.

For reference, all four means have elementary expressions. Put
$D_H=e^{-a_H}\sinh(\kappa a_H)$ and let
$z_H=\pi_0E_HZ$. Then

$$
\begin{aligned}
 m&=u(1-\beta-\kappa D_H),&
 z_H&=tu(1-\beta-D_H/\kappa),\\
 a&=u(c_0+td_0),&
 \ell&=c_0m+d_0z_H,\\
 b&=m+\beta a+\gamma u(d_0+tc_0).
\end{aligned}
\tag{12}
$$

Here $0<m,a<u$. Different low- and high-field durations preserve every
identity above. For fixed $J,H,a_H$, the raw covariance factor $d_0$ is
maximal at $a_0=J/t$; maximizing the final error tolerance also depends on
the response sensitivities.

## 4. A quantitative four-response margin

The quadratic form (6) makes stability elementary. If each rival mean is
within $r$ of the target mean, direct expansion yields

$$
 |\mathcal F_\sigma-\mathcal F_\sigma^*|
 \le L_\sigma r+r^2,
 \qquad L_\sigma=4+\sigma(a+m+u).
 \tag{13}
$$

The four first derivatives at the target are
$(-1-\sigma a,-1-\sigma m,1,1+\sigma u)$; their absolute values sum to
$L_\sigma$. The only quadratic remainder is $-\sigma\,\Delta a\Delta m$.
Thus an explicit positive occupation-error radius is

$$
 g_*=
 \min_{\sigma=\pm1}
 \frac{|\mathcal F_\sigma^*|}
 {\sqrt{L_\sigma^2+4|\mathcal F_\sigma^*|}+L_\sigma}.
 \tag{14}
$$

Every occupation error strictly below $g_*$ is excluded for ordinary
models with at most three states. This is an all-parameter positive
finite-accuracy statement with an explicit formula.

For a simple concrete setting, retain $J=H=\log3$, so $t=u=4/5$, and
take $a_0=a_H=3/2$. The active durations are $3/2,3/2,3,3$.
The approximate target values are

| Quantity | Approximate value |
|---|---:|
| $m$ | $0.4167564946067$ |
| $a$ | $0.5387655599100$ |
| $b$ | $0.6931128203369$ |
| $\ell$ | $0.2299499923598$ |
| $\mathcal F_-^*$ | $0.0081148104550$ |
| $\mathcal F_+^*$ | $-0.0730332940951$ |

The exact nominal certificate establishes

$$
 |\mathcal F_\sigma^*|>
 L_\sigma\frac9{2500}+\left(\frac9{2500}\right)^2
 \quad(\sigma=\pm1).
 \tag{15}
$$

(15) proves a maximum occupation-error lower bound
strictly greater than $9/5000=0.0018$, or 0.18 percentage points, for every
ordinary rival with at most three states. The displayed decimals are only
orientation. The numerical implication uses exact rational enclosures:
the verifier evaluates the two physical $4\times4$ matrix exponentials by
a degree-96 Taylor polynomial with outward remainder
$r^{97}/[97!(1-r/98)]$, where $r=\|(3/2)Q_h\|_\infty<6$.
It rounds matrix entries to 160-bit dyadics with explicit error intervals,
propagates the four response intervals, and certifies each mean within
$2^{-120}$ of its recorded 128-bit rational center. Translating (6) about
these centers and using mean radius $9/2500+2^{-120}$ leaves a polynomial
slack greater than $217/10^7$ for both signs. All these operations use exact
integer and rational arithmetic. This numerical enclosure is a premise of
the explicit constant; the all-rival implication is the analytic identity
(7), not an enumeration of candidate predictors.

### A nearby ordinary model bounds the remaining improvement

A fixed rational ordinary three-state model nearly attains this bound on
the same four experiments. Use readout $(-1,1,1)$, low stationary law

$$
 \pi_0=\left(\frac12,\frac{67251}{10^6},\frac{432749}{10^6}\right),
 \qquad \pi_H=\pi_0(1+uS),\quad u=4/5.
$$

Its symmetric stationary fluxes, in pair order $(1,2),(1,3),(2,3)$, are

| Field | Flux numerators, with denominator $10^6$ |
|---|---|
| $0$ | $36246,35559,19500$ |
| $H$ | $31102,18523,702$ |

Set $Q_{ij}=c_{ij}/\pi_i$ off the diagonal and choose row sums zero.
These are positive irreducible generators, exactly reversible for the
stated laws. Their maximum total exit rate is $18582/22417<1$.
The exact exponential enclosure certifies maximum occupation error less
than $1/550$ on the four protocols. Combined with (14)–(15), this yields

$$
 \frac9{5000}<
 \inf_{\substack{\text{ordinary models}\\\text{with at most three states}}}
 \max_i|p_i-p_i^*|
 <\frac1{550}.
 \tag{15a}
$$

The bracket endpoints differ by a factor $100/99$. The rational candidate
originated from a separate numerical search, but its validity and error
are verified without optimization. This is not an exact optimum or an
all-protocol approximation claim. It also shows that further optimization
of the proof alone cannot make this particular four-experiment gap large.

## 5. The exact three-state predictor still works

The positive three-state construction in
[the structural theorem](FAMILIAR_SWITCH_STRUCTURE.md) matches the two
closed target means for all positive-field control sequences. Its
equilibrium law at field $h$ has the same closed coordinates
$(\mathbb E S,\mathbb E Z)=(\tanh h,t\tanh h)$ as the physical target.
Therefore it matches all four experiments exactly from the corresponding
low- and high-field equilibrium preparations. The added preparation does
not require an extra predictor state.

The physical target supplies an ordinary four-state realization. Every
two-state stationary Markov model satisfies ordinary detailed balance, so
the same lower bound excludes unrestricted two-state models as well.
For the selected certificate, this gives

$$
 D_{\rm all}(\delta)=3,\qquad D_{\rm ord}(\delta)=4,
 \qquad 0\le\delta\le9/5000.
 \tag{16}
$$

For general positive parameters, the same formulas hold whenever
$0\le\delta<g_*$. The lower argument has no rival rate cap, and even
covers discrete-time reversible kernels. The continuous-time target and
three-state upper both have total exit rates below two in unit-attempt
time. Neither statement identifies ordinary reversibility with every
possible notion of physical time reversal.

## 6. Preparation errors and a biased reference law

Two equilibrium preparations must be justified, rather than inferred from
the two binary stationary means alone. Suppose each model uses one fixed
preparation law per field across all applicable experiments. Let the
target preparations be within TV distance $\epsilon_T$ of their respective
equilibria, and the rival preparations within $\epsilon_R$ of their own.
Stochastic contraction changes each occupation probability by at most its
corresponding preparation TV error. Thus a stationary-preparation margin
$g$ transfers to

$$
 \max_i|p_{T,i}^{\rm actual}-p_{R,i}^{\rm actual}|
 >g-\epsilon_T-\epsilon_R.
 \tag{17}
$$

The equilibrium-prepared three-state predictor approximates the actual
target within $\epsilon_T$. The physical four-state model with its
equilibrium preparations also meets that error and has zero preparation
error of its own. If $\epsilon_T\le\epsilon_R$, it may instead use the
target's actual preparations and match exactly. Consequently (16) persists for

$$
 \epsilon_T\le\delta\le g-\epsilon_T-\epsilon_R
 \tag{18}
$$

when the interval is nonempty. For example, $g=9/5000$ and
$\epsilon_T=\epsilon_R=10^{-4}$ leave a lower separation greater than
$0.0016$, with a three-state upper error at most $10^{-4}$. There is no
uniform finite preparation wait for arbitrarily slow rival dynamics.

An exact biased-reference version of the covariance identity is also
available. It supplies the algebra for field calibration; Section 7 adds
the separate numerical allowance. Write
$v=\pi_0S$, $z=1+uv$, and
$\pi_H=\pi_0(1+uS)/z$. Keep the four definitions of $m,a,b,\ell$.
Set

$$
\begin{gathered}
 c_F=(v+u-m)/u,\qquad c_G=(za-v)/u,\\
 T=(zb-m)/u,\qquad
 U=[za-zb+m-(1-u^2)\ell]/u^2,\qquad
 q_\sigma=1+\sigma v.
\end{gathered}
\tag{19}
$$

The same reversibility argument gives

$$
 \operatorname{Cov}_0(G,F\mid S=\sigma)
 =\frac{T+\sigma U}{q_\sigma}
  -\frac{(v+\sigma c_G)(m+\sigma c_F)}{q_\sigma^2}.
 \tag{20}
$$

Its cleared numerator must vanish for a singleton sector. This permits
biased low-field equilibrium once $v$ and the relative tilt are included
as calibrated inputs. The next section supplies a residual bound and a
separate calibration certificate for this four-experiment witness.

## 7. Stationary-law and execution tolerances

Let $\pi$ be the actual low stationary law, with $v=\pi S$, and $\eta$
the actual high stationary law. Allow an approximate force relation

$$
 z=1+uv,\qquad \lambda=\pi(1+uS)/z,\qquad
 \operatorname{TV}(\eta,\lambda)\le\theta.
 \tag{21}
$$

The low and high kernels are reversible for $\pi$ and $\eta$. The high
preparation in $a,b$ is now $\eta$. Define

$$
\begin{aligned}
 q_\sigma&=1+\sigma v,\qquad
 T_\sigma=um+\sigma(v+u-m),\\
 \mathcal G_\sigma
 &=q_\sigma[(1+\sigma u)\ell+zb-m]
       -za(1+\sigma m)-vT_\sigma.
\end{aligned}
\tag{22}
$$

At $v=0$, this is $\mathcal F_\sigma$. For exact tilt, the biased
conditional-covariance calculation gives

$$
 u^2q_\sigma^2\operatorname{Cov}_\pi(G,F\mid S=\sigma)
 =-\sigma(1-\sigma u)\mathcal G_\sigma.
 \tag{23}
$$

For approximate tilt, a singleton sector instead implies

$$
 |\mathcal G_\sigma|
 \le \left[
 \frac{4q_\sigma z(1+2u)}{1-\sigma u}
 +2z\bigl(q_\sigma+|1+\sigma m|\bigr)
 \right]\theta.
 \tag{24}
$$

Here is a direct accounting of this bound. First replace the two high-prep
responses by $a_\lambda=\lambda G$ and
$b_\lambda=\lambda E_0F$. Each replacement costs at most $2\theta$.
The high-kernel defects

$$
 d_1=\lambda F-\lambda S,\qquad
 d_2=\lambda E_HG-\lambda G,\qquad
 d_3=\langle S,E_HG\rangle_\lambda-\langle F,G\rangle_\lambda
 \tag{25}
$$

each have absolute value at most $4\theta$, by stationarity or detailed
balance under $\eta$. Relative to the exact-tilt moment formulas,
$\langle SF\rangle_\pi$ changes by $zd_1/u$, and
$\langle SGF\rangle_\pi$ by $z(d_2-ud_3)/u^2$.
In the cleared conditional covariance, these changes cost at most
$4q_\sigma z(1+2u)\theta$, using
$|v+\sigma\langle SG\rangle_\pi|\le q_\sigma$.
Division by $1-\sigma u$ gives the first term in (24). Replacing
$a_\lambda,b_\lambda$ by the actual responses gives the second term,
since their coefficients in (22) are $-z(1+\sigma m)$ and
$q_\sigma z$. No small-state rate constant appears.

The exact calibration certificate evaluates (22) and (24) on the
box

$$
 |v|\le10^{-4},\qquad |u-4/5|\le10^{-4},\qquad
 \theta\le10^{-5},\qquad
 \|\mathbf m-\mathbf m_*\|_\infty\le\frac{17}{5000}.
 \tag{26}
$$

The verifier translates each sixteen-term polynomial (22) about the four
certified target centers, $v=0$, and $u=4/5$. It adds $2^{-120}$ to each
response radius to account for the target enclosure. Summing the absolute
nonconstant coefficients times the appropriate coordinate radii bounds
the entire variation. The resulting public rational bounds are

| Sign | Center magnitude greater than | Variation less than | Allowed residual less than |
|---|---:|---:|---:|
| $-$ | $8114/10^6$ | $7670/10^6$ | $90/10^6$ |
| $+$ | $73033/10^6$ | $19614/10^6$ | $569/10^6$ |

Both signs retain slack greater than $177/500000$. Thus neither allowed
singleton residual can occur in (26). This excludes stationary-preparation
ordinary rivals within occupation error $g_0=17/10000=0.0017$ of the nominal
target.

For physical execution, suppose both fields are fixed across experiments,
$|h_0|\le\epsilon_h$ and $|h_H-\log3|\le\epsilon_h$, with fixed
field-specific tick durations within $\epsilon_t$ of $3/2$. The target's
two preparation laws are within $\epsilon_p$ of their respective actual
equilibria. Each equilibrium field shift costs at most $\epsilon_h/2$ in
TV. Field-rate changes cost at most $\epsilon_h/2$ per unit active time,
and the total duration is at most $3+2\epsilon_t$. A simple timing bound
uses target exit rates below two and at most two ticks. Thus

$$
 b_T\le\epsilon_p+(2+\epsilon_t)\epsilon_h+4\epsilon_t,
 \qquad b_R\le\epsilon_p,
 \tag{27}
$$

where the rival's two preparations are likewise within $\epsilon_p$ of
their own actual stationary laws. For all three tolerances equal to
$10^{-5}$, the combined bound is $0.0000800001<10^{-4}$. Exact balanced
reference Gibbs families have $v=\tanh h_0$ and
$u=\tanh(h_H-h_0)$, inside (26); more generally the bounds and (21)
are distributional assumptions.

These simultaneous tolerances leave
an actual target-versus-ordinary-small-model gap greater than $0.0016$.
The three-state upper extends to these slightly negative low fields by
the [previously certified positive-rate extension](FAMILIAR_SWITCH_CALIBRATION.md),
and matches both actual stationary preparations. Hence the calibrated
minimum counts remain three versus four for
$10^{-5}\le\delta\le0.0016$.

Fixed common field-specific clocks preserve the argument. Independent
per-occurrence clock mixtures also preserve the two reversible averaged
kernels when their laws are fixed by field and independent of state and
other ticks. Arbitrary drift and finite ramps are not automatically
covered. The full-distribution preparation and stationary-law tolerances
cannot be inferred solely from the binary stationary means.

## 8. An initial-snapshot alternative to the second preparation

Under exact tilt, baseline trials with a noninvasive initial binary
observation can replace the high-equilibrium preparation. Only the two
opposite-order protocols $0,H$ and $H,0$ are then needed. Stationarity
and (2) give

$$
\begin{array}{c|cc}
 \text{Protocol}&\mathbb E[S_{\rm final}]&
 \mathbb E[(1+uS_{\rm initial})S_{\rm final}]\\\hline
 0,H&m&b\\
 H,0&\ell&a
\end{array}
 \tag{28}
$$

Both trials start from $\pi_0$. The first row uses $\pi_0E_0=\pi_0$;
the second weighted mean uses $\pi_HE_H=\pi_H$.
This is a different observation resource, with weights in $[1-u,1+u]$;
the four estimates obtained from the two initial/final joint laws are
correlated and do not have the same variance as independent Bernoulli
endpoints from two equilibria. In particular, the unbiased
weighted occupation variable
$(1+uS_{\rm initial})\mathbf 1_{\{S_{\rm final}=1\}}$ lies in $[0,1+u]$.

There is a direct finite-accuracy consequence. Give each protocol its
$2\times2$ initial/final probability table, and measure prediction error
by the maximum TV distance over the two tables, where TV is half the sum
of the four absolute entry differences. If that error is $\delta_{\rm joint}$,
the unweighted and weighted occupation expectations in (28) differ by
at most $\delta_{\rm joint}$ and $(1+u)\delta_{\rm joint}$, respectively.
Thus the nominal endpoint margin at $u=4/5$ implies

$$
 \max_{w\in\{0H,H0\}}
 \operatorname{TV}(P_w^{\rm target},P_w^{\rm ordinary})
 >\frac{9/5000}{1+4/5}=\frac1{1000}
 \tag{29}
$$

for every ordinary rival with at most three states.

The three-state predictor also matches each initial/final joint law:
conditional on initial $S=\sigma$,
target and predictor share initial coordinate means $(\sigma,\sigma t)$,
which evolve by the same closed equations. This is not a claim of matching
complete multitime path laws. Together with the ordinary four-state target
and the two-state lower implication, it gives minimum counts three versus
four for joint-TV tolerances $0\le\delta_{\rm joint}\le1/1000$ on these
two protocols. This corollary assumes exact equilibrium preparation and
tilt. Readout disturbances, weighting error, and approximate-tilt
calibration need separate treatment; the endpoint-only sample counts do
not apply unchanged.

## 9. What this improvement uses

The gain comes from a covariance identity and a second controlled
preparation, or the initial-snapshot alternative. The readout remains
binary and the lower bound covers arbitrary ordinary small models. All
four endpoint responses must be explained by the same model with its
two Gibbs-related equilibrium laws.

In the endpoint-only version, high-field preparation is needed repeatedly.
Its preparation time and statistical cost belong in the comparison. The
active protocol is short, but the proven probability gap remains small;
no one-percent separation or laboratory feasibility claim follows from
this result. Manuscript drafting remains deferred.
