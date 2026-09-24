# Measurement and preparation cost of the four-endpoint witness

The [four-endpoint theorem](FAMILIAR_SWITCH_PREPARATION_WITNESS.md) increases
the certified occupation gap and shortens the active experiments by adding
high-field equilibrium as a second preparation. This note prices that
resource explicitly. It uses independent Bernoulli endpoints from fresh
preparations, and the same separate validity and power guarantees as the
[earlier measurement analysis](FAMILIAR_SWITCH_MEASUREMENT_COST.md).

The [exact verifier](../scripts/verify_switch_preparation_witness.py) and
[report](../reports/switch_preparation_witness.json) certify the numerical
constants below. The analytic concentration and adaptive-testing arguments
are inherited from the earlier note and its inspected primary sources;
see also the [new source comparison](FAMILIAR_SWITCH_PREPARATION_SOURCE_AUDIT.md).

## 1. Four cells, with preparation included in the cell label

In the order $(m,a,b,\ell)$, the preparation/word pairs are

$$
 (0;H),\quad(H;0),\quad(H;0H),\quad(0;H0).
 \tag{1}
$$

The semicolon separates the equilibrium preparation from the active
chronological word. Each trial produces one Bernoulli endpoint, with
probability $(1+\text{mean})/2$. At $J=H=\log3$ and tick $3/2$, the
active durations are $3/2,3/2,3,3$, summing to nine attempt-time units.

Let $q$ be the known nominal target probability vector. For the ordinary
comparison class $\mathcal R$, suppose

$$
 \inf_{r\in\mathcal R}\|q-r\|_\infty>g_0-b_R,
 \qquad \|p_*-q\|_\infty\le b_T,
 \qquad d=g_0-b_R-b_T>0.
 \tag{2}
$$

The nominal certificate uses $g_0=9/5000$ and $b_T=b_R=0$. The calibrated
certificate uses $g_0=17/10000$, $b_T+b_R<1/10000$, hence $d>1/625$.
Preparation and physical calibration are already included in these budgets.
In the calibrated class, low-field stationary bias, relative tilt uncertainty
and high-field stationary-law discrepancy obey the theorem's stated bounds.
The two stationary laws and field kernels are shared across all cells.

Take $n$ independent endpoints in each cell, and let $\widehat p$ be the
four empirical frequencies. An additional unknown observation bias $c$
satisfies $\|p^{\rm obs}-p\|_\infty\le c$; it must not repeat a preparation
allowance already charged in (2). The model-accuracy allowance $e\ge0$
means the null includes physical responses within $e$ of some
$r\in\mathcal R$. Fix the menu, reference, budgets and sample sizes before
collecting the test data. Define

$$
 r_\alpha(n)=\sqrt{\frac{\log(8/\alpha)}{2n}}.
 \tag{3}
$$

Hoeffding's inequality and four two-sided confidence events give a test:

$$
 \text{Reject if}\quad
 \|\widehat p-q\|_\infty+r_\alpha+c+e\le g_0-b_R.
 \tag{4}
$$

Under the null, the simultaneous confidence event makes (4) contradict
(2), so its rejection probability is at most $\alpha$. Under the target,
the event with confidence radius $r_\beta$ guarantees rejection whenever

$$
 r_\alpha+r_\beta+2c+e\le d.
 \tag{5}
$$

Thus the sufficient equal allocation is

$$
 n=\left\lceil
 \frac{\bigl(\sqrt{\log(8/\alpha)}+
                  \sqrt{\log(8/\beta)}\bigr)^2}
      {2(d-2c-e)^2}
 \right\rceil,
 \qquad d>2c+e.
 \tag{6}
$$

Two sampling radii are essential. Target calibration costs $b_T$ once;
additional unknown observation bias costs $2c$. A failure to reject does
not establish the small-model null. These are sufficient designs, not
optimal tests or experimentally measured sample requirements.

## 2. Endpoint counts and the changed resource budget

At $\alpha=\beta=1/20$ and $c=0$, equation (6) becomes
$n=\lceil2\log160/(d-e)^2\rceil$:

| Comparison | Guaranteed budget $d$ | Model allowance $e$ | Endpoints per cell | Total endpoints |
|---|---:|---:|---:|---:|
| Nominal | $9/5000$ | 0 | 3,132,824 | 12,531,296 |
| Calibrated | $1/625$ | 0 | 3,964,980 | 15,859,920 |
| Calibrated, finite accuracy | $1/625$ | $1/10000$ | 4,511,266 | 18,045,064 |

The earlier seven-cell designs required 315,548,219, 876,522,829 and
1,972,176,367 endpoints in these respective roles. Those comparisons use
different deterministic certificates and experimental resources: the new
design requires both field equilibria, rather than only the low-field one.
The conservative calibrated exact-null budget falls by a factor greater
than 55. This does not establish a 55-fold improvement in the optimal test.

The stored reference means have enclosure radius $2^{-120}$, hence each
occupation center has radius $2^{-121}$. Accounting for that numerical
reference uncertainty in both validity and power leaves all displayed
integer sample counts unchanged. The reference uncertainty is separate
from data-driven calibration uncertainty, which would need its own
simultaneous confidence allocation.

## 3. Both equilibrium preparations can be bounded for the physical target

The common preparation budget is total-variation distance $10^{-5}$ from
the actual equilibrium law at the preparation field. For the physical
two-switch heat-bath generator, the spectrum is

$$
 0,\quad -2,\quad -1\pm\sqrt{tB(h)},\qquad
 B(h)=\frac{t(1-\tanh^2h)}{1-t^2\tanh^2h}.
 \tag{7}
$$

This follows from the invariant mean space $(1,S,Z)$ and the additional
correlation coordinate $SZ$, whose diagonal decay is $-2$. For a reversible
chain, spectral contraction and Cauchy--Schwarz give the uniform bound

$$
 \|\mu e^{TQ}-\pi\|_{\rm TV}
 \le\frac12\sqrt{\pi_{\min}^{-1}-1}\,e^{-\lambda T}.
 \tag{8}
$$

The supremum over initial distributions is attained at a point mass before
applying this bound. At the allowed low fields, $\lambda\ge1-t=1/5$ and
$\pi_{\min}>1/21$. At the allowed high fields,
$\tanh h\ge4/5-10^{-5}$ gives $tB(h)<25/64$, hence
$\lambda>3/8$, and $\pi_{\min}>1/101$.
For the mass bounds, the nominal minima are $1/20$ and $1/100$;
a field shift of magnitude $\epsilon_h$ changes each Gibbs mass by a
factor at least $e^{-2\epsilon_h}\ge1-2\epsilon_h$.

The following actual waits therefore suffice from any target starting law:

| Preparation field | Actual wait | Squared TV upper used |
|---|---:|---|
| Low | 62 | $5e^{-124/5}<10^{-10}$ |
| High | 36 | $25e^{-27}<10^{-10}$ |

These are target-specific preparation guarantees. No finite wait prepares
every arbitrary rival, whose rates remain uncapped and may be arbitrarily
slow. The rival preparation condition must be justified separately. Waiting
does not, by itself, turn successive observations into independent samples.
For the deterministic state-count theorem, each preparation field has one
fixed starting law shared by its two cells.

With equal allocation, two cells use each preparation. Serial preparation
exposure is $196n$; nominal active exposure is $9n$. If each tick differs
from $3/2$ by at most $\epsilon_t$, the six active ticks give total exposure

$$
 n(205+6\epsilon_t).
 \tag{9}
$$

For the calibrated exact-null row and $\epsilon_t=10^{-5}$ this is below
$812{,}821{,}138$ attempt-time units. It excludes readout, hardware switching
and other overhead. Converting to seconds requires a physical attempt rate.

## 4. A separate necessary information bound

The exact report supplies a fixed ordinary three-state comparator whose
four occupation probabilities differ from the nominal target by less
than $1/550$. Both vectors lie in $[1/8,7/8]^4$. Taylor's theorem for the
Bernoulli relative entropy gives, for each cell,

$$
 D_{\rm KL}(\operatorname{Ber}(p_i^*)\Vert
             \operatorname{Ber}(q_i))
 \le\frac{32}{7}(p_i^*-q_i)^2
 <\frac{32}{7\cdot550^2}<\frac1{66000}.
 \tag{10}
$$

Allow adaptive choice among these four preparation/word pairs, independent
fresh endpoints conditional on each choice, and an almost surely finite
stopping rule, with $\alpha+\beta<1$. The standard change-of-measure inequality, applied to the
test decision, then yields

$$
 \mathbb E_*N\ge66000\,\operatorname{kl}(1-\beta,\alpha).
 \tag{11}
$$

At $\alpha=\beta=1/20$ this is
$59400\log19\approx174899.67536$. A fixed integer budget must consequently
be at least **174,900**. An expected stopping time is not rounded to an
integer. The lower applies to the ideal nominal endpoint task and hence
to uniform tests covering that case. It does not apply to richer trajectory
observations, different menus, or the initial-snapshot variant below.
The sufficient and necessary sample bounds remain far apart.

## 5. An alternative preparation resource

The theorem's optional initial-snapshot corollary uses just the opposite
orders $0H$ and $H0$, both prepared at low-field equilibrium and observed
at the initial and final times. The unweighted final means give $m,\ell$;
weighting by $1+uS_{\rm initial}$ gives $b,a$, respectively. Stationarity
of the two field laws makes these identifications exact.

This requires a noninvasive initial readout and bounded weighted
observations. The three-state predictor matches both initial/final joint
laws. Their maximum TV error is greater than $1/1000$ for every ordinary
model with at most three states, under exact preparation and tilt. That
TV norm differs from the endpoint-occupation norm in the table above.
The endpoint counts and calibrated bounds in this note cannot be reused
for the snapshot observation model. Pricing its correlated statistics,
readout disturbance and weighting uncertainty is a concrete next task
when high-field preparation is difficult.

This checkpoint makes the mechanism and short experiment simpler and gives
a much tighter deterministic gap bracket. The remaining endpoint burden,
the preparation promises and the common force law still matter for physical
significance. Manuscript drafting remains deferred.
