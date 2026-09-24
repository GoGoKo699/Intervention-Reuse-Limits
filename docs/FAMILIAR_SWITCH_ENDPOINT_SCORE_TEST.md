# A direct endpoint-score test with fewer fresh preparations

The [four-endpoint witness](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) can be
tested directly instead of estimating all four probabilities to the same
accuracy. A fixed linear score, with a bounded quadratic remainder and a
localization gate, gives the following sufficient designs. Both the
false-rejection probability and the missed-target probability are below
5%, uniformly over their stated classes.

| Design | Endpoints in cells $(m,a,b,\ell)$ | Total | Allowed model error |
|---|---|---:|---:|
| Nominal | $(350000,400000,550000,150000)$ | 1,450,000 | 0 |
| Calibrated | $(400000,460000,630000,180000)$ | 1,670,000 | 0 |
| Calibrated, finite accuracy | $(450000,520000,720000,200000)$ | 1,890,000 | $10^{-4}$ |

The corresponding confidence-box designs required 12,531,296, 15,859,920,
and 18,045,064 endpoints. These are comparisons between sufficient designs,
not an optimality statement. All designs here use the same four independent
Bernoulli endpoint experiments, including the two equilibrium preparations.
They do not use initial/final snapshot data.
In the last row the calibrated unrestricted three-state predictor has
error at most $10^{-5}$, so it attains the $10^{-4}$ accuracy level
being tested against ordinary models.

**Review status:** proof and numerical certificate passed independent
internal review. [Exact verifier](../scripts/verify_switch_endpoint_score.py) ·
[Report](../reports/switch_endpoint_score.json) ·
[Earlier preparation and sampling costs](FAMILIAR_SWITCH_PREPARATION_COST.md).

## 1. Fixed reference and the decision rule

Use the cell order
$(0;H),(H;0),(H;0H),(0;H0)$, where the first entry denotes preparation.
The target has $J=H=\log3$ and clock $3/2$. Let $q$ be the exact rational
occupation center recorded in the frozen four-endpoint certificate.
Its coordinate error relative to the nominal target is at most
$\zeta=2^{-121}$. Write its corresponding mean vector as
$x^0=2q-\mathbf1=(m_0,a_0,b_0,\ell_0)$.

At $u_0=4/5$, define

$$
 F_\sigma(x)=b-m-a+\ell+\sigma(u_0\ell-am),\qquad \sigma=\pm1.
 \tag{1}
$$

The target has $F_- >0$ and $F_+<0$. Define oriented tangent scores

$$
 T_\sigma(p)=-\sigma\left[
 F_\sigma(x^0)+
 \nabla_pF_\sigma(2q-\mathbf1)\mathbin{\cdot}(p-q)\right],
 \tag{2}
$$

where the occupation-coordinate gradient is

$$
 g_\sigma=(-2(1+\sigma a_0),-2(1+\sigma m_0),2,2(1+\sigma u_0)).
 \tag{3}
$$

Thus the score coefficients are $h_\sigma=-\sigma g_\sigma$.
They and all sampling choices are fixed before collecting observations.
No parameters are fitted to the test data.
Calibration bounds are deterministic premises. Estimating them from data
requires a separate simultaneous confidence allocation.

Let $\widehat p_i$ be the average of $n_i$ fresh independent Bernoulli
endpoints. Reject the ordinary-at-most-three-state null **only if**:

1. Each coordinate satisfies $|\widehat p_i-q_i|\le\rho_i$, where
   $\rho=(0.004,0.004,0.006,0.006)$.
2. Both $T_-(\widehat p)>c_-$ and $T_+(\widehat p)>3/200$ hold.

The minus cutoffs are $c_-=41/10000$, $1/250$, and $17/4000$ in the
three table rows, respectively. Failure to reject is inconclusive.
This is a target-specific composite-null test; it is not a test that
must detect every possible four-state alternative.

## 2. A local null bound, including calibration

Put $R=2\rho$, and write $\mathcal B=\{p:|p_i-q_i|\le R_i\}$.
The quadratic remainder in (1) is exact:

$$
 F_\sigma(2p-\mathbf1)
 =F_\sigma(x^0)+g_\sigma\cdot(p-q)
       -4\sigma(p_m-q_m)(p_a-q_a).
 \tag{4}
$$

In the nominal class every ordinary small model has
$F_+=0$ or $F_-=0$. In the calibrated class use precisely the stationary
bias, relative-tilt, high-stationary-law TV, field, clock and preparation
assumptions of the four-endpoint theorem. There is no added rate cap.

For reference, its generalized stationary identity is

$$
 \begin{aligned}
 z&=1+uv,\quad q_\sigma=1+\sigma v,\quad
 U_\sigma=um+\sigma(v+u-m),\\
 G_\sigma&=q_\sigma[(1+\sigma u)\ell+zb-m]
              -za(1+\sigma m)-vU_\sigma .
 \end{aligned}
 \tag{5}
$$

For at least one singleton sign, the approximate force law gives

$$
 |G_\sigma|\le
 \left[\frac{4q_\sigma z(1+2u)}{1-\sigma u}
       +2z(q_\sigma+|1+\sigma m|)\right]\theta .
 \tag{6}
$$

Throughout the local stationary-response box
$|p_i-q_i|\le R_i+11/100000$, with
$|v|\le10^{-4}$, $|u-u_0|\le10^{-4}$, and $\theta\le10^{-5}$,
exact coefficient bounds on $G_\sigma-F_\sigma$ and (6) imply

$$
 |F_-|\le B_-=\frac1{8000}\quad\hbox{or}\quad
 |F_+|\le B_+=\frac1{1600},
 \tag{7}
$$

for the applicable singleton sign. The verifier shifts the sixteen-term
polynomial (5) about the rational reference and bounds each nuisance term
by its absolute coefficient times its coordinate radii. The numerical
local-band checks are an essential premise, while (6) is the analytic
all-rival implication. No fitted comparator is used for the test.

Let $\epsilon_p$ be the rival preparation allowance, and let $e$ be the
requested model accuracy. In the calibrated rows $\epsilon_p=10^{-5}$;
in the nominal row it is zero. If the physical response vector $p$ lies
within $e$ of an admissible rival's actually prepared responses, it lies
within

$$
 s=\epsilon_p+e
 \tag{8}
$$

of that rival's stationary-preparation vector. Thus, for $p\in\mathcal B$,
at least one score satisfies

$$
 T_\sigma(p)\le C_\sigma
 :=B_\sigma+4(R_m+s)(R_a+s)+L_\sigma s,\qquad
 L_\sigma=\sum_i|h_{\sigma i}|.
 \tag{9}
$$

Here $B_\sigma=0$ for the nominal row. Equations (4) and (7) prove (9);
the final term transfers the fixed linear score from stationary rival
responses to the physical responses. Preparation error is not charged
again as observation noise.

## 3. Bernstein bounds and a valid gate partition

For independent centered variables with $|Y_j|\le M$ and total variance
at most $V$, the usual bounded-variable Bernstein inequality gives

$$
 \Pr\!\left(\sum_jY_j\ge t\right)
 \le\exp\!\left[-\frac{t^2}{2(V+Mt/3)}\right],\qquad t>0.
 \tag{10}
$$

The same bound applies to the lower tail. One direct proof expands the
exponential moment, uses
$\mathbb E|Y_j|^k\le M^{k-2}\mathbb EY_j^2$ and
$k!\ge2\,3^{k-2}$ for $k\ge2$, and multiplies the independent
moment-generating bounds. This gives
$\log\mathbb E e^{\lambda\sum Y_j}
\le\lambda^2V/[2(1-\lambda M/3)]$.
Choosing $\lambda=t/(V+Mt/3)$ gives (10).
This is an established concentration tool; see Maurer and Pontil's
[primary paper](https://arxiv.org/pdf/0907.3740v1), Theorem 3, printed
page 2, for the bounded iid variance-sensitive form. The weighted,
independent version used here follows from the displayed argument.

For the fixed score, set

$$
 M_\sigma=\max_i\frac{|h_{\sigma i}|}{n_i},\qquad
 V_{\sigma,N}=\sum_i
 \frac{h_{\sigma i}^2(q_i-R_i)(1-q_i+R_i)}{n_i}.
 \tag{11}
$$

Every $q_i-R_i>1/2$, so (11) bounds the variance for all
$p\in\mathcal B$. These are population variance bounds from a fixed
box, not empirical variance estimates.

There are two cases for any fixed null response vector.
If $p\notin\mathcal B$, fix a coordinate outside its interval.
Passing the gate requires a one-sided sample displacement of at least
$R_i-\rho_i=\rho_i$. Hoeffding bounds that probability by
$\exp(-2n_i\rho_i^2)<e^{-10}<1/20$.
There is no union over coordinates: any one fixed violating coordinate
suffices.

If $p\in\mathcal B$, choose its applicable singleton sign. Rejecting
requires that score to exceed its cutoff. By (9)--(11), the verifier
certifies a Bernstein exponent greater than three. Thus false rejection
has probability less than $e^{-3}<1/20$. Requiring both scores to pass
does not require an additional union bound: at least one null inequality
is true. The outside and inside cases partition fixed population vectors,
not random events that must have their error probabilities added.
This proves uniform type-I error below 5%.

## 4. Uniform power at the intended target

The nominal target lies within $\zeta$ of $q$. In the calibrated rows,
the physical target displacement bound is
$b_T=700001/10^{10}$, so put $d_T=b_T+\zeta$; in the nominal row
put $d_T=\zeta$. The score's population mean is at least

$$
 D_\sigma=-\sigma F_\sigma(x^0)-L_\sigma d_T.
 \tag{12}
$$

Use the target variance bound

$$
 V_{\sigma,T}=\sum_i
 \frac{h_{\sigma i}^2(q_i-d_T)(1-q_i+d_T)}{n_i}.
 \tag{13}
$$

The exact checker verifies (10) at deviation $D_\sigma-c_\sigma$:
the exponent is greater than $31/10$ for the minus score and greater
than eight for the plus score. Every target gate tail has exponent
$2n_i(\rho_i-d_T)^2>10$. Consequently the probability of failing
either score or any gate is strictly less than

$$
 e^{-31/10}+e^{-8}+8e^{-10}
 <\frac{49}{1000}+\frac1{2000}+\frac1{2000}
 =\frac1{20}.
 \tag{14}
$$

The factor eight counts two tails in four cells. This proves at least
95% power uniformly over the allowed calibrated targets, including
the finite-accuracy null in the last table row.

The checker uses exact rational variance and step bounds, rounded outward
before computing the Bernstein exponents. Positive degree-32 partial sums
of the exponential certify $e^3>20$, $e^{31/10}>1000/49$,
$e^8>2000$, and $e^{10}>16000$. It draws no samples, performs no
optimization, and uses no floating arithmetic.

## 5. Resources and limits

The allocations are fixed choices, not claimed optimal. Each cell remains
an independent Bernoulli endpoint experiment from a fresh preparation.
The shared null may have arbitrary rates and topology; its stationarity,
Gibbs-law and preparation assumptions are substantive.
There is no additional observation-bias allowance in the certified rows.
With such an allowance $c$, one would replace $s$ by
$\epsilon_p+e+c$ and $d_T$ by $b_T+\zeta+c$, and recertify the gate,
bands and concentration inequalities.

The nominal active exposure is 3,225,000, 3,720,000, and 4,215,000
attempt-time units in the three rows. For the calibrated rows, the
previously certified actual waits of 62 units at low field and 36 at
high field, plus tick error at most $10^{-5}$, give serial exposure
at most 78,920,024.8 and 89,155,028.1 units. These waits guarantee
the target's preparation error, not a uniform reset for arbitrarily slow
rivals. The nominal design assumes exact equilibrium preparation; a
finite wait's error cannot be omitted from that row.

The observed gains concern a sufficient statistical scheme for this
specific target. They do not change the deterministic separation or its
nearby ordinary comparator, prove an optimal testing cost, or certify
laboratory feasibility. The initial/final snapshot experiment has different
joint data and requires its own analysis.
