# A finite-sample score test from two snapshot protocols

Two initial/final binary tables support a variance-sensitive test of the
ordinary reversible three-state class. The test uses fixed linear scores,
small localization gates, and a bounded-variable Bernstein inequality.
It retains the correlation between the two observations on each trial.
At the selected coupled-switch target, the proposed allocations are
900,000 trials nominally, 1,000,000 with physical calibration allowances,
1,200,000 with uncertain one-percent bit-flip channels, and 1,500,000 when
the last null class is enlarged by an observed-table TV tolerance of
$10^{-4}$. Each trial has two binary readouts.

**Review status:** the analytic proof and exact arithmetic checks have
passed independent internal review.
[Exact verifier](../scripts/verify_switch_snapshot_design.py) ·
[Numerical report](../reports/switch_snapshot_design.json).
The numbers are not a laboratory feasibility claim. This is a test for
the specified model and instrument class, not a device-independent test.

[Snapshot witness and calibration assumptions](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md)
· [Preparation/source boundary](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md)
· [Single-endpoint score comparison](FAMILIAR_SWITCH_ENDPOINT_SCORE_TEST.md)

## 1. Data, model class, and a fixed test

The target has $J=H=\log3$, $u_0=4/5$, and field-specific ticks
$\tau_0=\tau_H=3/2$. Each trial starts from the low-field preparation. Protocol
$A$ applies the chronological order $0,H$ and records $(I,Y)$ initially
and finally. Protocol $B$ applies $H,0$ and records $(J,Z)$.
All four bits take values in $\{-1,1\}$. Trials are independently freshly
prepared, and the law within each protocol is fixed. Independence of the
two bits within a trial is neither assumed nor used.

Write the four true-record moments and one useful combination as

$$
 m=\mathbb EY,\quad c=\mathbb E(IY),\quad
 \ell=\mathbb EZ,\quad d=\mathbb E(JZ),\qquad a=\ell+u_0d.
 \tag{1}
$$

The nominal null is the union of ordinary reversible models with at most
three states, deterministic binary readout, balanced stationary low-field
preparation, and the shared Gibbs tilt
$\pi_H=\pi_0(1+u_0S)$. There is no rate cap or rival graph restriction.
One shared model must explain both protocols. The snapshot identity gives
at least one sign $\sigma\in\{-1,1\}$ for which

$$
 F_\sigma=u_0c-u_0(1+\sigma m)d+\sigma(u_0-m)\ell=0.
 \tag{2}
$$

The robust versions of this null are specified in Section 4. They allow
small bias, approximate tilt, preparation and initial-instrument error,
and specified detector uncertainty. The last row also admits any pair of
data laws within TV $e=10^{-4}$, separately for each observed joint table,
of an admissible ordinary three-state rival.

Choose fixed rational centers $m_0,c_0,\ell_0,d_0$, each within $10^{-12}$
of the nominal target moment, and put $a_0=\ell_0+u_0d_0$. These are
chosen before the experiment. The certificate fixes particular rational
centers. For orientation,

$$
 (m_*,c_*,\ell_*,d_*)\approx
 (0.4167564946067,\ 0.3454454071627,\
  0.2299499923598,\ 0.3860194594377),\qquad
 a_*\approx0.5387655599100.
 \tag{3}
$$

Define $A_\sigma=\sigma(u_0-m_0)$ and
$B_\sigma=-u_0(1+\sigma m_0)$. With ideal electronic records, the
fixed per-trial scores are

$$
 X_{\sigma,A}=(u_0I-\sigma a_0)Y,
 \qquad X_{\sigma,B}=(A_\sigma+B_\sigma J)Z.
 \tag{4}
$$

For noisy records, replace the single final bit by its reference-channel
inverse and the bit product by its product-channel inverse, as in
Section 5. In either case form

$$
 \widehat T_\sigma=\overline X_{\sigma,A}
              +\overline X_{\sigma,B}+\sigma m_0a_0,
 \qquad \widehat S_\sigma=-\sigma\widehat T_\sigma.
 \tag{5}
$$

The test first requires the two tight empirical gates

$$
 |\widehat m-m_0|\le0.006,\qquad
 |\widehat a-a_0|\le0.012.
 \tag{6}
$$

Each robust row also requires
$|\widehat c-c_0|,|\widehat\ell-\ell_0|,
|\widehat d-d_0|\le0.020$. Reject the null precisely when all applicable
gates pass and both $\widehat S_->t_-$ and
$\widehat S_+>t_+$ hold. The allocations and thresholds are fixed:

| Row | $n_A$ | $n_B$ | Total trials | $t_-$ | $t_+$ |
|---|---:|---:|---:|---:|---:|
| Nominal | 550,000 | 350,000 | 900,000 | 0.0043 | 0.0062 |
| Physical calibration, ideal electronic readout | 600,000 | 400,000 | 1,000,000 | 0.0043 | 0.0065 |
| Physical calibration and uncertain 1% channels | 700,000 | 500,000 | 1,200,000 | 0.00425 | 0.0063 |
| Same, with observed-TV tolerance $e=10^{-4}$ | 850,000 | 650,000 | 1,500,000 | 0.0044 | 0.0064 |

The asserted guarantees are size at most $0.05$ uniformly over the
corresponding null, and power at least $0.95$ uniformly over the specified
target calibration class. The target class is the same in the last two
rows; the fourth row enlarges only the null.

## 2. Why a local linear score is sufficient

At any population moments, the polynomial has the exact expansion

$$
 F_\sigma=T_\sigma-\sigma(m-m_0)(a-a_0).
 \tag{7}
$$

Thus a branch satisfying (2) has
$\mathbb ES_\sigma=-(m-m_0)(a-a_0)$. On the larger population box
$|m-m_0|\le0.010$, $|a-a_0|\le0.020$, its signed-score mean is at most
$0.0002$. For the robust rows the larger population box also has
$|c-c_0|,|\ell-\ell_0|,|d-d_0|\le0.030$.

The proof splits according to this deterministic population box. If a
null lies outside, passing at least one particular empirical gate
requires a one-sided bounded-mean deviation. If it lies inside, a true
null branch has a bounded score mean and rejection requires a Bernstein
deviation. These are alternative cases for a fixed data-generating law,
so their error bounds are maximized, not added. No Bonferroni factor for
the two signs is necessary: the null is a union, whereas rejection
requires rejection of both branches.

The nominal target has
$F_-^*>0.008114$ and $-F_+^*>0.073033$.
The center error changes a target score by only the product of the two
center discrepancies in (7). The difficult statistical direction is
$\sigma=-1$; the other direction has a substantially larger margin.

## 3. A bounded-variable Bernstein bound

Let independent centered variables satisfy $|Z_i|\le M$ and
$\sum_i\mathbb EZ_i^2\le V$. For $0\le\lambda<3/M$, Taylor expansion
and $k!\ge2\,3^{k-2}$ for $k\ge2$ give

$$
 \log\mathbb E\exp\!\left(\lambda\sum_iZ_i\right)
 \le\frac{\lambda^2V}{2(1-\lambda M/3)}.
 \tag{8}
$$

Indeed $|\mathbb EZ_i^k|\le M^{k-2}\mathbb EZ_i^2$; summing the
geometric series and using $\log(1+x)\le x$ proves (8). Put
$s=\sqrt{2x/V}$ and $\lambda=s/(1+Ms/3)$ in Chernoff's bound. Then

$$
 \Pr\!\left\{\sum_iZ_i\ge\sqrt{2Vx}+Mx/3\right\}\le e^{-x}.
 \tag{9}
$$

The same bound holds for the lower tail; the case $V=0$ is immediate.
For two averages of scores with range widths $w_A,w_B$ and variances
bounded by $v_A,v_B$, use

$$
 V=v_A/n_A+v_B/n_B,\qquad
 M=\max\{w_A/n_A,w_B/n_B\},\qquad
 \mathcal B(V,M,x)=\sqrt{2Vx}+Mx/3.
 \tag{10}
$$

A centered variable is bounded in absolute value by its full range
width, so this choice of $M$ is valid. No Gaussian approximation or
estimated standard error is used.

Variance-sensitive bounded-mean concentration is established background.
For example, Maurer and Pontil, *Empirical Bernstein Bounds and Sample
Variance Penalization* (2009), [Theorem 3, printed page 2](https://arxiv.org/pdf/0907.3740v1),
state the corresponding variance-sensitive one-sided bound for iid
variables in $[0,1]$. Equation (8) supplies the needed independent,
non-identically weighted extension directly. No novelty is claimed for
this concentration inequality or for taking a fixed tangent.

## 4. The physical and approximate-null budgets

For every robust rival, let the stationary low law be $\pi$ and the
stationary high law be $\eta$. The assumptions are

$$
 |v|=|\pi S|\le10^{-4},\quad |u-u_0|\le10^{-4},\quad
 \operatorname{TV}\!\left(\eta,\frac{\pi(1+uS)}{1+uv}\right)
 \le\theta=10^{-5}.
 \tag{11}
$$

Detailed balance is required at both fields. On stationary, undisturbed
snapshot moments a singleton sector obeys the residual identity proved
in the [snapshot note, Section 4](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md):

$$
 \begin{split}
 H_\sigma={}&(1+\sigma v)[(1+\sigma u)\ell+uc]
 -(\ell+ud)(1+\sigma m)\\
 &-v[um+\sigma(v+u-m)],\\
 |H_\sigma|\le{}&
 \frac{12u(1+\sigma v)(1+uv)\theta
             +16(1+uv)^2\theta^2}{1-\sigma u}.
 \end{split}
 \tag{12}
$$

Writing $F_{\sigma,u}$ for (2) with $u_0$ replaced by $u$ gives

$$
 H_\sigma=F_{\sigma,u}+vD_{\sigma,u}-\sigma v^2,\qquad
 D_{\sigma,u}=(u+\sigma)\ell+\sigma uc+(\sigma-u)m-\sigma u,
 \quad
 \partial_uF_{\sigma,u}=c-d+\sigma(\ell-md).
 \tag{13}
$$

On the coordinate box of radius $0.03030$ about the nominal target,
and $u\in[0.7999,0.8001]$, elementary corner evaluation yields

| Sign | $|\partial_u F|$ upper | $|D|$ upper | $|F_{\sigma,u_0}|$ upper |
|---|---:|---:|---:|
| $-$ | 0.201 | 0.358 | 0.000110 |
| $+$ | 0.144 | 0.112 | 0.000510 |

The last column follows from (12), the first two columns multiplied by
$10^{-4}$, and the additional $10^{-8}$ term. All corner calculations
are polynomial evaluations on a rectangle; they are not numerical fits.

Target and rival preparation TV errors and initial-instrument joint-TV
errors are each at most $10^{-5}$. A uniform hidden-state disturbance
bound from the snapshot note is sufficient. More generally, an explicit
joint-law bound can include initial misclassification; merely preserving
the visible marginal is insufficient. Common target low/high field
offsets and common per-field tick errors are each at most $10^{-5}$.
The target true-record displacement from its nominal stationary table is
therefore bounded by

$$
 b_T=10^{-5}+(2+10^{-5})10^{-5}+4\cdot10^{-5}+10^{-5}
 =0.0000800001.
 \tag{14}
$$

The rival true-record displacement from its own stationary, undisturbed
table is at most $b_R=2\cdot10^{-5}$. These preparation and instrument
bounds apply to every admissible rival, not just to the target.

For the physical row put $E_T=b_T,E_R=b_R$. For the noisy rows use
reference reliabilities $r_0=r_f=0.98$ and $\kappa=r_0r_f=0.9604$.
Each actual detector probability is within $10^{-5}$ of $0.01$,
so the channel-table TV uncertainty is at most $\chi=2\cdot10^{-5}$.
The reference inverse has induced signed-TV norm $1/\kappa$. Hence put

$$
 E_T=b_T+\chi/\kappa,\qquad
 E_R=b_R+(\chi+e)/\kappa,
 \tag{15}
$$

where $e=0$ in the third row and $e=10^{-4}$ in the fourth.
The quantities obtained by reference inversion need not form a positive
table; (15) only uses a signed-TV norm and linear moments. For the nominal
row set both budgets to zero.

Let $w_A^0,w_{B,\sigma}^0$ denote the ideal-record score range widths.
Within the larger empirical-population box, its stationary rival
counterpart lies within $2E_R$ in each moment and within $3.6E_R$ in
$a$. In particular its coordinate box is contained in radius $0.03030$.
For its singleton sign, the signed population score is at most

$$
 R_\sigma\le
 (0.010+2E_R)(0.020+3.6E_R)
 +f_\sigma+(w_A^0+w_{B,\sigma}^0)E_R,
 \tag{16}
$$

where $f_- =0.000110,f_+=0.000510$ in robust rows, and $f_\sigma=0$
nominally. The last term is the linear score displacement. Similarly
the target signed score is bounded below by

$$
 |F_\sigma^*|-(w_A^0+w_{B,\sigma}^0)E_T-10^{-20}.
 \tag{17}
$$

The small explicit last term covers the fixed rational-center product.
The following rational bounds have ample room for its actual value:

| Row | $R_-$ upper | $R_+$ upper | Target $\mathbb ES_-$ lower | Target $\mathbb ES_+$ lower |
|---|---:|---:|---:|---:|
| Nominal | 0.0002 | 0.0002 | 0.008114 | 0.073033 |
| Physical | 0.0004 | 0.00083 | 0.00776 | 0.07257 |
| Uncertain channels | 0.0005 | 0.00095 | 0.00767 | 0.07245 |
| Same, $e=10^{-4}$ | 0.00096 | 0.00155 | 0.00767 | 0.07245 |

## 5. Corrected records, ranges, and variances

Conditional on the true pair, the initial and final electronic flips are
independent binary-symmetric channels, independent of the dynamics,
instrument disturbance, and other trials. There is no feedback from the
noisy initial record. Their probabilities are fixed within the specified
calibration intervals. The target and the underlying admissible rivals
use this instrument class; they need not share the same unknown
probabilities. The fourth row additionally admits nearby observed laws
that need not themselves have this channel factorization.

For recorded bits $I_o,Y_o$, use
$M=Y_o/r_f$, $C=I_oY_o/(r_0r_f)$; define $L,D$ in the other arm
analogously. The scores are $u_0C-\sigma a_0M$ and
$A_\sigma L+B_\sigma D$. They use reference $r_0,r_f$ throughout,
even when the actual channels differ slightly. Set $r_0=r_f=1$ for the
first two rows. Their range widths are

$$
 w_A=\frac{2(u_0/r_0+|a_0|)}{r_f},\qquad
 w_{B,\sigma}=\frac{2(|A_\sigma|+|B_\sigma|/r_0)}{r_f}.
 \tag{18}
$$

The square of each observed bit is one. Therefore the following second
moments depend on the initial mean, not on independence within a trial:

$$
 \begin{split}
 \mathbb EX_{\sigma,A}^2
 &=\frac{u_0^2/r_0^2+a_0^2
            -2\sigma u_0a_0\,\mathbb EI_o/r_0}{r_f^2},\\
 \mathbb EX_{\sigma,B}^2
 &=\frac{A_\sigma^2+B_\sigma^2/r_0^2
            +2A_\sigma B_\sigma\,\mathbb EJ_o/r_0}{r_f^2}.
 \end{split}
 \tag{19}
$$

For all robust nulls, including the observed-TV enlargement, both
corrected initial means have absolute value below $0.001$. One sufficient
bound, allowing the initial instrument also to affect the initial bit,
is

$$
 \frac{(r_0+2\cdot10^{-5})(10^{-4}+4\cdot10^{-5})+2e}{r_0}
 <0.001.
 \tag{20}
$$

Without noisy channels the same bound holds directly; nominally the
initial means are zero. Dropping the negative squared score means from
(19) bounds each null variance globally. No fitted null variance is used.

For the target nominal table, subtract
$(u_0c_*-\sigma a_0m_*)^2$ and
$(A_\sigma\ell_*+B_\sigma d_*)^2$ from (19), respectively.
If a law changes by TV $b$ and a score has range width $w$, then
$\operatorname{Var}_{\rm new}(X)\le
\operatorname{Var}_{\rm old}(X)+w^2b$: center at the old mean and
use the oscillation bound of $w^2$ for its squared deviation.
Use $b=b_T$ in the physical row and $b=b_T+\chi$ in noisy rows.
The latter bound compares actual observed laws with the nominal observed
channel; no inverse factor is needed for this variance calculation.

The following ceilings suffice. In each triple the entries are for
arm $A$, arm $B$ with sign $-$, and arm $B$ with sign $+$.

| Row | Range-width ceilings $(w_A,w_{B,-},w_{B,+})$ | Null variance ceilings $(v_A,v_{B,-},v_{B,+})$ |
|---|---|---|
| Nominal | $(2.678,1.700,3.034)$ | $(0.931,0.365,1.432)$ |
| Physical | $(2.678,1.700,3.034)$ | $(0.932,0.366,1.434)$ |
| Both noisy rows | $(2.766,1.754,3.143)$ | $(0.998,0.390,1.548)$ |

| Row | Target variance ceilings $(v_{A,-},v_{B,-},v_{A,+},v_{B,+})$ |
|---|---|
| Nominal | $(0.680,0.293,0.928,1.310)$ |
| Physical | $(0.681,0.294,0.929,1.311)$ |
| Both noisy rows | $(0.747,0.318,0.995,1.426)$ |

## 6. Size and power accounting

For gates the individual variables have absolute bounds

$$
 h_m=1/r_f,\qquad h_c=1/(r_0r_f),\qquad
 h_a=(1+u_0/r_0)/r_f.
 \tag{21}
$$

If a population lies outside its larger box, gate passing has probability
at most the maximum of

$$
 e^{-n_A(0.004)^2/(2h_m^2)},\quad
 e^{-n_B(0.008)^2/(2h_a^2)},\quad
 e^{-\min(n_A,n_B)(0.010)^2/(2h_c^2)}.
 \tag{22}
$$

The last term is needed only for robust rows. This follows by applying
the one-sided bounded-mean Hoeffding bound to any violated coordinate.
Inside the box, for at least one branch the population signed-score mean
is at most $R_\sigma$. Its rejection probability is at most $0.05$
whenever

$$
 R_\sigma+\mathcal B(V_{N,\sigma},M_\sigma,\log20)<t_\sigma.
 \tag{23}
$$

Together with (22), this proves uniform size at most $0.05$ by the
alternative-case argument in Section 2.

For target power, the sum of gate-failure bounds is less than $0.001$.
Explicitly, allowing $10^{-12}$ center error in each moment, use

$$
 \begin{split}
 &2\exp\!\left[-\frac{n_A(0.006-2E_T-10^{-12})^2}{2h_m^2}\right]
 +2\exp\!\left[-\frac{n_B(0.012-3.6E_T-1.8\cdot10^{-12})^2}{2h_a^2}\right]\\
 &\quad+2\exp\!\left[-\frac{n_A(0.020-2E_T-10^{-12})^2}{2h_c^2}\right]
 +4\exp\!\left[-\frac{n_B(0.020-2E_T-10^{-12})^2}{2h_c^2}\right].
 \end{split}
 \tag{24}
$$

Omit the second line nominally. Let $s_\sigma$ denote the target
signed-mean lower bounds in Section 4. The two lower-tail checks are

$$
 s_- -\mathcal B(V_{T,-},M_-,\log(125/6))>t_-,\qquad
 s_+ -\mathcal B(V_{T,+},M_+,\log1000)>t_+.
 \tag{25}
$$

Their failure probabilities are at most $0.048$ and $0.001$.
Adding them to the gate failure gives a total below $0.05$.
This is a union bound over power failures, not over the null branches.

For orientation, using the rational ceilings above gives these hard-sign
inequalities; these displayed rounded decimals are not the exact
certificate:

| Row | Null cutoff upper | Chosen cutoff | Target power floor | Gate failure upper |
|---|---:|---:|---:|---:|
| Nominal | 0.004254 | 0.0043 | 0.004560 | 0.000939 |
| Physical | 0.004251 | 0.0043 | 0.004385 | 0.000493 |
| Uncertain channels | 0.004140 | 0.00425 | 0.004449 | 0.000130 |
| Same, $e=10^{-4}$ | 0.004224 | 0.0044 | 0.004784 | 0.000008 |

The larger-sign checks have more slack. The exact verifier checks moment
enclosures, corner bounds, systematic budgets, ranges, variance ceilings,
outside-gate bounds, and both signs of (23) and (25). It uses stronger
rational Bernstein exponents $3$, $3.1$, and $7$ in place of
$\log20$, $\log(125/6)$, and $\log1000$. The comparisons with the score
cutoffs are reduced to positive rational squared inequalities. Positive
degree-96 partial sums for $e^x$ certify the required tail bounds and
the summed gate-failure bound. No floating arithmetic, sampling, or
allocation optimization enters this certificate.

## 7. A necessary information budget

The separately fixed ordinary three-state comparator in the snapshot
certificate supplies a lower bound on statistical cost. For each arm,
let $P$ be the nominal target joint law and $Q$ this comparator's joint
law. All entries are positive, and the exact certificate checks

$$
 D(P\Vert Q)\le\frac12\sum_j
       \frac{(P_j-Q_j)^2}{\min(P_j,Q_j)}<\frac1{30000}.
 \tag{26}
$$

For completeness, Taylor-expand $\sum_jP_j\log(P_j/Q_j)$ about $Q$.
The linear term sums to zero by normalization, and the Hessian entry on
each intervening segment is at most $1/\min(P_j,Q_j)$, proving the first
inequality. The comparator is fixed before this calculation; a numerical
search alone would not certify (26).

Consider any test with false rejection and missed-target probability at
most $0.05$. It may adaptively choose the next arm and use an almost
surely finite stopping rule, provided each chosen observation comes from
a fresh independent trial with that arm's law. Infinite expected trial
cost already satisfies the lower bound. The likelihood chain rule bounds
the accumulated target-to-null
relative entropy by $\mathbb E_PN/30000$. Binary data processing for the
rejection event bounds it below by
$\operatorname{kl}(0.95,0.05)=0.9\log19$. Consequently

$$
 \mathbb E_PN>27000\log19\approx79499.8524.
 \tag{27}
$$

A fixed total must therefore be at least 79,500 trials. The same
per-trial upper in (26) survives a common known binary-symmetric detector
channel by data processing. This is a lower bound from an ideal nominal
subclass, which is enough to constrain any uniformly valid test of the
larger calibrated class. It does not determine the optimal allocation or
close the gap to the sufficient designs above.

The adaptive change-of-measure argument is established: see Kaufmann,
Cappé and Garivier (2016), [Lemma 1, printed page 7, and Appendix A.1](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf),
and the inspected-source discussion in the
[calibration source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md).
Its fresh-trial assumptions are substantive; a continuous trajectory with
memory is a different sampling experiment.

## 8. Resource interpretation and limitations

The totals count independent trials, not individual bit readouts. The
four rows use respectively 1.8, 2.0, 2.4, and 3.0 million binary readouts.
They retain one low-field preparation and two opposite-order protocols;
there is no high-field equilibrium preparation. Their extra observational
resource is the initial snapshot on every trial.

For the calibrated target, the existing 62-unit low-field reset bound
reaches the stipulated preparation TV. With two active ticks, the
target reset-plus-active exposure is at most
$(65+2\cdot10^{-5})N$ attempt-time units for $N$ trials, excluding
measurement and other overhead. Independent reset trials remain an
assumption. A 62-unit target reset does not establish preparation TV or
independence uniformly for arbitrary slow rivals. Exact nominal
equilibrium preparation also does not follow from any finite wait.

The fourth row excludes ordinary three-state approximations within
$10^{-4}$ in the observed joint-table metric. The constructive general
three-state predictor has observed error at most $4\cdot10^{-5}$ under
these target preparation, disturbance, and uncertain-channel allowances,
using the reference channel, as explained in the snapshot note. Thus
this approximation tolerance exceeds that constructive upper; it does
not absorb uncontrolled detector drift or hidden measurement effects.

The model class requires fixed shared kernels, preparation and instrument
laws across protocols. The test does not cover arbitrary correlated or
state-dependent drift, learned score coefficients reused on the same
data, or failure of the stated calibration and sampling assumptions.
The concentration argument establishes a finite mathematical budget; it
does not establish that those physical assumptions can be achieved in a
particular experiment.
