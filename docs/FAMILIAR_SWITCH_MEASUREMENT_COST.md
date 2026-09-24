# Measurement cost of the seven-experiment state witness

The [finite-margin theorem](FAMILIAR_SWITCH_FINITE_MARGIN.md) separates the
four-state coupled-switch target from every admissible ordinary-reversible
model with at most three states using seven endpoint occupation probabilities.
This note translates that deterministic statement into a statistical test.
It gives sufficient sample counts, a separate information-theoretic lower
bound, and the preparation assumptions needed to interpret either result.
No sample count is claimed optimal or experimentally feasible.

The main observation model is one Bernoulli endpoint from each independently
prepared trial. It does not count successive observations along one trajectory
as independent samples. Section 4 gives a conditional-calibration alternative.

## 1. A test with separate calibration, bias, and model-error budgets

Let $q\in[0,1]^7$ be a known reference response vector, such as the nominal
target probabilities in the [exact report](../reports/familiar_switch_margin.json).
Let $\mathcal R$ be the set of response vectors of the ordinary models being
excluded. Suppose a deterministic certificate and its calibration bounds give

$$
 \inf_{r\in\mathcal R}\|q-r\|_\infty>g_0-b_R,
 \qquad \|p_*-q\|_\infty\le b_T.
 \tag{1}
$$

Here $p_*$ is the actual target response vector. The quantities $b_T,b_R$
account for target and rival calibration allowances. Define the remaining
separation budget

$$
 d=g_0-b_R-b_T>0.
 \tag{2}
$$

These are deterministic assumptions, not sampling errors. For the nominal
task, $g_0=1/2000$ and $b_T=b_R=0$. A robust application with
$g_0=1/2500$ and $b_T+b_R\le1/10000$ has $d\ge3/10000$.
The robust rows below use the [calibration theorem](FAMILIAR_SWITCH_CALIBRATION.md);
sampling does not establish its deterministic assumptions.
The reference vector, error budgets, protocol menu and sample sizes are fixed
before collecting these endpoints. Estimating them from data requires
additional simultaneous confidence guarantees and an allocated error budget.

For each protocol $i$, take $n$ independent endpoints
$X_{ij}\sim\operatorname{Bernoulli}(p_i^{\rm obs})$ and set
$\widehat p_i=n^{-1}\sum_jX_{ij}$. Allow an additional, unknown systematic
occupancy bias

$$
 |p_i^{\rm obs}-p_i|\le b.
 \tag{3}
$$

This $b$ must not repeat a preparation or calibration allowance already
included in $b_T$ or $b_R$. Let $e\ge0$ be the model-accuracy allowance:
the null says that the physical responses $p$ lie within $e$ of some
$r\in\mathcal R$. Thus rejection rules out even such approximate models,
not only exact response equality.

For $0<\alpha<1$, put

$$
 r_\alpha(n)=\sqrt{\frac{\log(14/\alpha)}{2n}}.
 \tag{4}
$$

Hoeffding's inequality and a union bound over seven two-sided events give
$\Pr(\|\widehat p-p^{\rm obs}\|_\infty>r_\alpha)\le\alpha$.
Use the following fixed-sample decision rule:

$$
 \boxed{\text{Reject the ordinary-small-model null if }
 \|\widehat p-q\|_\infty+r_\alpha+b+e\le g_0-b_R.}
 \tag{5}
$$

If the inequality fails, report that the test did not reject; this does not
establish the null. On the simultaneous confidence event, a null response
$r$ would satisfy
$\|r-q\|_\infty\le e+b+r_\alpha+\|\widehat p-q\|_\infty$,
contradicting (1). Hence the false-rejection probability is at most $\alpha$
uniformly over the entire stated null class.

Under the target alternative, the event with radius $r_\beta$ gives
$\|\widehat p-q\|_\infty\le b_T+b+r_\beta$. Therefore power is at
least $1-\beta$ whenever

$$
 r_\alpha+r_\beta+2b+e\le d.
 \tag{6}
$$

In particular, if $d>2b+e$, a sufficient common sample count is

$$
 n=\left\lceil
 \frac{\bigl[\sqrt{\log(14/\alpha)}+
              \sqrt{\log(14/\beta)}\bigr]^2}
      {2(d-2b-e)^2}
 \right\rceil.
 \tag{7}
$$

The two confidence radii in (6) matter: one controls validity under the null,
the other guarantees success under the target. Charging only one radius
would not give the stated power. Target calibration costs $b_T$ once in
(6); the unknown observation bias costs $2b$ because validity and power
must hold for its unfavorable values under either hypothesis.

The rational report encloses the reference means within $2^{-120}$, hence
the occupation center within $2^{-121}$. Exact reference probabilities can
be used mathematically; an implementation using their stored centers must
include this enclosure in its deterministic budget, or round the sample
count upward with slack. The table is unchanged if this negligible
enclosure is explicitly included.

## 2. Sufficient endpoint counts and elapsed protocol time

At $\alpha=\beta=0.05$ and with no additional observation bias $b$, (7) gives:

| Deterministic remaining budget $d$ | Model allowance $e$ | Endpoints per word $n$ | Total endpoints $7n$ | Nominal active exposure $36n$ |
|---|---:|---:|---:|---:|
| Nominal $1/2000$ | 0 | 45,078,317 | 315,548,219 | 1,622,819,412 |
| Robust calibration budget $3/10000$ | 0 | 125,217,547 | 876,522,829 | 4,507,831,692 |
| Robust calibration budget $3/10000$ | $1/10000$ | 281,739,481 | 1,972,176,367 | 10,142,621,316 |

The second row excludes exact ordinary response models. The third also
excludes ordinary models whose seven probabilities approximate the physical
responses within $10^{-4}$; it gives a statistical version of the approximate
memory comparison. The calibration theorem supplies an unrestricted
three-state predictor with occupation error at most $10^{-5}$ under the
same assumptions. Thus the third row tests an accuracy level that this
smaller predictor attains. Neither row is a statistical guarantee on
protocols outside this menu.

All times are in the target's unit attempt-rate time. The chronological
words are $H,H^2,H^3,H0,H^20,H0H,H^20H$. At clock two, their durations are
$2,4,6,4,6,6,8$, totaling 36; the average is $36/7$, and the maximum is 8.
The exposure column assumes serial trials and excludes preparation and
readout overhead. Parallel samples reduce wall-clock duration, not the
number of independently prepared endpoints.

For actual word durations $T_i$, the serial active exposure is
$n\sum_iT_i$. Let the actual tick lengths $\tau_0,\tau_H$ be fixed across
all occurrences, with $|\tau_h-2|\le\varepsilon_t$. Thus $H^2$ lasts
$2\tau_H$. The menu contains 18 ticks, giving

$$
 \sum_iT_i\le36+18\varepsilon_t,\qquad
 \max_iT_i\le8+4\varepsilon_t.
 \tag{8}
$$

With a preparation wait of duration $T_{\rm prep}$ before every endpoint,
the serial exposure becomes $n(\sum_iT_i+7T_{\rm prep})$.

For the nominal system, charging a 55-unit wait's preparation error as
an additional $b=10^{-5}$ increases the required $n$ to 48,913,105.
The total exposure is then $421n=20,592,417,205$ units. A finite wait's
preparation error cannot be omitted while retaining the first row's ideal
sample count.

For the robust $e=0$ row, a 62-unit preparation wait and
$\varepsilon_t=10^{-5}$ give exposure at most
$n(470+18\times10^{-5})<58,852,270,000$ units. This row assumes that its
preparation allowance was already included in the deterministic calibration
budget. No physical conversion to seconds is claimed without an attempt
rate and preparation mechanism.

## 3. A necessary sample burden from the nearby reversible model

The [finite-margin certificate](../reports/familiar_switch_margin.json)
also gives a particular ordinary three-state model with response vector $r$
satisfying $\|p_*-r\|_\infty<837/10^6$ for the nominal target.
The certified target probabilities and this error bound place every $p_{*,i}$
and $r_i$ in $[1/8,7/8]$.

Write
$\operatorname{kl}(p,q)=p\log(p/q)+(1-p)\log[(1-p)/(1-q)]$.
As a function of its first argument, its second derivative is
$1/[p(1-p)]$. Taylor's theorem along the interval between $p_{*,i}$ and
$r_i$ therefore gives

$$
 \operatorname{kl}(p_{*,i},r_i)
 \le\frac{32}{7}(p_{*,i}-r_i)^2
 <\frac{32}{7}\left(\frac{837}{10^6}\right)^2
 <\frac1{300000}.
 \tag{9}
$$

Consider any test using only these seven endpoint experiments, with a fresh
independent Bernoulli draw at each trial. It may select the next word
adaptively and may stop at an almost-surely finite stopping time. Suppose
it rejects with probability at most $\alpha$ under every ordinary null,
and with probability at least $1-\beta$ under the nominal target, where
$\alpha+\beta<1$. The change-of-measure inequality gives

$$
 \sum_i\mathbb E_*N_i\,
   \operatorname{kl}(p_{*,i},r_i)
 \ge\operatorname{kl}(1-\beta,\alpha).
$$

Combining this with (9) yields

$$
 \boxed{\mathbb E_*N\ge
 300000\,\operatorname{kl}(1-\beta,\alpha).}
 \tag{10}
$$

For $\alpha=\beta=0.05$, the right side is
$270000\log19\approx794,998.52$. A deterministic sample budget therefore
needs at least 794,999 endpoints. A random stopping rule has the stated
expected-count lower bound, rather than an integer-rounded expectation.
Since every allowed word lasts at least two units, its expected active
exposure is at least twice this bound, before preparation overhead.

This is a lower bound for the ideal nominal, unbiased endpoint-only task.
It is not a minimax-optimal count, a lower bound for richer trajectory
observations, or a separately quantified bound for each calibrated target.
Any test that covers the nominal setting among its allowed calibrations
must still satisfy this limitation there. Neither this argument nor the
sufficient count establishes that uniform allocation is optimal.

Unknown bias can also destroy identifiability. If each hypothesis may
have arbitrary per-word observation bias of size
$b\ge837/(2\times10^6)$, the target and the explicit ordinary comparator
can both produce Bernoulli probabilities $(p_*+r)/2$. No number of samples
then distinguishes them uniformly over those bias choices.

## 4. Preparation: a target wait is not a universal reset

For the nominal target at zero field, direct decomposition of its four-state
generator gives the following total-variation distances from stationarity
after a wait $T$:

$$
 \begin{aligned}
 D_{\rm aligned}(T)&=\tfrac12e^{-T/5}+\tfrac1{20}e^{-2T},\\
 D_{\rm anti}(T)&=\tfrac12e^{-9T/5}+\tfrac9{20}e^{-2T}.
 \end{aligned}
 \tag{11}
$$

These cover the two aligned and two anti-aligned pure starting states;
convexity covers any starting distribution. For $T\ge1$, the aligned
bound dominates, since
$D_{\rm anti}(T)\le(19/20)e^{-9T/5}<(1/2)e^{-T/5}$.
Thus $T=55$ gives uniform target preparation error below $10^{-5}$.
Subsequent controlled Markov evolution cannot increase this total-variation
error, and any endpoint occupation error is bounded by it.

If the preparation field obeys $|h_0|\le10^{-5}$, the target's zero-field
reference law is replaced by its actual low-field stationary law.
For this fixed coupling, the nonzero relaxation rates are
$1\pm\sqrt{tB(h_0)}$ and $2$, where
$B(h)=t[1-\tanh^2h]/[1-t^2\tanh^2h]$. Hence its gap is at least $1/5$.
Also $\pi_{h_0,\min}\ge(1-10^{-5})/20$. Reversible $L^2$ contraction
and Cauchy--Schwarz give

$$
 \sup_x\|P_{h_0}^T(x,\cdot)-\pi_{h_0}\|_{\rm TV}
 \le\frac12\sqrt{\frac{20}{1-10^{-5}}-1}\,e^{-T/5}.
 \tag{12}
$$

An **actual wait of at least 62 units** makes this less than $10^{-5}$.
The change from the actual stationary law to the nominal law is a separate
calibration allowance. A nominal wait with timing uncertainty must be
chosen to guarantee the stated actual lower duration.

These preparation times are target-specific. There is no finite uniform
equilibration wait for all uncapped ordinary rivals: their entire generators
can be slowed while preserving their stationary laws and detailed balance.
Uniform null validity therefore requires an independent preparation
guarantee, not merely waiting for the target's mixing time.

Exact independence is sufficient, but not necessary for (4)--(7). Suppose,
conditional on every past history, the next endpoint's mean differs by at
most $b$ from the same fixed protocol probability. Conditional Hoeffding's
lemma for a variable of range width one gives
$\mathbb E[e^{\lambda(X-\mathbb E[X\mid\mathcal F])}\mid\mathcal F]
\le e^{\lambda^2/8}$. Iteration gives the same concentration radius for
a fixed number of trials per protocol. The conditional mean discrepancies
are charged to $b$. This remains a calibration assumption under both null
and alternative; a long wait does not prove it for every possible rival.
The adaptive KL lower in Section 3 uses the stated fresh-independent-draw
model, not this more general dependent-data extension.

## 5. Sources and limits

Hoeffding's original [paper](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf),
*JASA* 58 (1963), 13--30, Theorem 2 on page 16, supplies the bounded-sum
concentration inequality; [publisher DOI](https://doi.org/10.1080/01621459.1963.10500830).
The conditional extension above follows directly by iterating the conditional
exponential-moment bound, so it does not assume iid data after waiting.

Kaufmann, Cappe and Garivier,
[On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf),
*JMLR* 17 (2016), 1--42, Lemma 1 on page 7 and Appendix A.1, give the
adaptive change-of-measure inequality used in (10). Here the seven protocols
are the seven sampling choices. The Bernoulli KL upper (9) is derived above.

The [source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md) records these
attributions and the calibration conventions. The
[exact verifier](../scripts/verify_switch_calibration.py) and its
[report](../reports/switch_calibration.json) check the bounded numerical
certificates used here.

The statistical tools are established results. This note applies them to
the certified response margin and its explicit close ordinary comparator.
The sufficient and necessary costs remain far apart. Preparation, field,
timing and observation calibration consume real error budgets; endpoint
sample counts do not price a device, a reset mechanism or parallel capacity.
No fitted residual, Gaussian approximation, optimizer, or large simulation
enters these conclusions.
