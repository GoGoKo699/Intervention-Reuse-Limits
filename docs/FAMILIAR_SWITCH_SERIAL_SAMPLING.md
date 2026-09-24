# Five million serial trials with conditional reset control

The [one-percent kinetic score test](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md)
keeps its **five-million-trial allocation, empirical gates and threshold
$.0021$** when fresh-trial independence is replaced by a uniform
conditional preparation promise. The false-rejection probability remains
below $5\%$ and power remains above $95\%$. Dependence between trials is
allowed. The required control is conditional on the full past, rather
than an unconditional or time-averaged preparation error.

This is a sampling theorem for the two joint snapshot laws. It does not
prove that an arbitrary apparatus resets sufficiently quickly. The
[finite-reset bound](FAMILIAR_SWITCH_FINITE_RESET.md) supplies that physical
step for the specified four-state target. The stationary ordinary-model
and measurement promises remain substantive assumptions. Manuscript
drafting remains deferred.

## 1. One fixed reference pair and an adapted experiment

Fix the deterministic schedule $A,B,A,B,\ldots,A,B$, with
$n=2{,}500{,}000$ trials of each arm. Here $A$ is the chronological word
$0H$, and $B$ is $H0$, with the same fields, nominal dwell times and
binary initial/final observations as the percent-kinetic checkpoint.
Let $\mathcal F_{t-1}$ contain the complete past immediately **before
trial $t$'s reset**, including previous outcomes and any retained
apparatus information. Let $\mathcal F_t$ be the corresponding history
after trial $t$'s final readout and before the next reset.
Let $a_t\in\{A,B\}$ be its scheduled arm, and write
$P_t(\cdot\mid\mathcal F_{t-1})$ for the conditional law of its two
recorded signs. The filtration may include the hidden state entering
the reset because the physical reset estimate is uniform over that
state. It must not condition on the hidden state emerging from the
current reset: doing so would remove the randomized preparation whose
conditional law is being bounded.

The target promise is that there is **one fixed pair**
$(P_A^*,P_B^*)$ from the nominal-field, nominal-time one-percent kinetic
target family such that, almost surely at every trial,

$$
 \operatorname{TV}\!\left(P_t(\cdot\mid\mathcal F_{t-1}),
                         P_{a_t}^*\right)\le B,
 \qquad B=.000079.                                      \tag{1}
$$

The conditional preparation, instrument, field and timing errors must
fit the existing target budget
$b_T=.000078025101<B$. Finite reset replaces the preparation allowance;
it is not an additional error to append after spending that allowance.
The reference's eight edge multipliers and two detector error
probabilities are fixed for the entire experiment.

A sufficient physical implementation uses the same symmetric detector
channels on every trial, with their electronic flips independent of the
past, the hidden dynamics and each other. Equivalently, conditional on
the pre-reset past their probabilities are the fixed channel values,
and the current flips are independent of the current hidden evolution
and one another. The conditional bounds here
apply to the complete recorded joint law, after preparation, the initial
instrument and both channels. Unconditional detector-error marginals
alone do not supply them.

The null promise is that there is **one fixed pair** $(P_A^0,P_B^0)$
from the inherited stationary ordinary class with at most three states,
such that, almost surely at every trial,

$$
 \operatorname{TV}\!\left(P_t(\cdot\mid\mathcal F_{t-1}),
                         P_{a_t}^0\right)\le E_R,
 \qquad E_R=.00022=.00002+.0002.                         \tag{2}
$$

The stationary class is the same as in the percent score proof:
reversible kernels, low-field imbalance $|v|\le10^{-4}$, tilt
$|u-3/5|\le10^{-4}$, stationary tilt TV error at most $10^{-5}$, and
fixed independent symmetric detector errors in $[0,1/2]$. The $.00002$
part of (2) allows conditional preparation and initial-instrument error;
the $.0002$ part is the additional observed-law approximation allowance.
Neither part is charged to the target again.

Equations (1)--(2) allow the actual conditional laws to depend on the
past. They do not allow selecting a different stationary physical model
for each history. In particular, unconditional closeness of a time
average to some ordinary model is insufficient for (2). A finite reset
time for the four-state target does not certify a mixing time for every
ordinary rival; the rival's conditional preparation promise must be
supplied separately.

## 2. The test is unchanged

Write $(I,Y)$ for an $A$ outcome and $(J,Z)$ for a $B$ outcome. Use

$$
 X_A=.4Y+.6IY-.3I,\qquad
 X_B=-.4Z-.48JZ+.3J,\qquad
 \widehat T=\overline X_A+\overline X_B-.08.              \tag{3}
$$

Equivalently, the lookup table is:

| Protocol | $(+,+)$ | $(+,-)$ | $(-,+)$ | $(-,-)$ |
|---|---:|---:|---:|---:|
| $50X_A$ | 35 | -65 | 5 | 25 |
| $50X_B$ | -29 | 59 | -11 | -19 |

Let $\widehat M,\widehat C$ be the $A$ averages of $Y,IY$ and
$\widehat L,\widehat D$ the $B$ averages of $Z,JZ$; put
$\widehat A=\widehat L+.6\widehat D$ and
$\widehat Q=\widehat C-\widehat D$. Reject only if
$\widehat T>.0021$ and every empirical gate below passes.

| Quantity | Empirical gate $G$ | Auxiliary interval $H$ |
|---|---|---|
| $M$ | $[.211,.226]$ | $[.207,.230]$ |
| $C$ | $[.457,.490]$ | $[.453,.494]$ |
| $L$ | $[.118,.132]$ | $[.114,.136]$ |
| $D$ | $[.475,.509]$ | $[.471,.513]$ |
| $A$ | $[.405,.435]$ | $[.401,.439]$ |
| $Q$ | $[-.025,-.012]$ | $[-.031,-.006]$ |

There need not be one population law for the actual serial process, so
the second column of intervals from the independent-trial proof is
called $H$ here. It is a deterministic proof device. The data still
contain ten million binary readouts.

## 3. A fixed-reference split establishes the null ceiling

For a sign-valued observable, TV error $E_R$ moves its expectation by at
most $2E_R$. The corresponding displacements are $3.2E_R$ for $A$ and
$4E_R$ for $Q$. Denote these three amounts by $\Delta_S,\Delta_A,
\Delta_Q$.

First suppose the stationary reference lies inside every interval $H$
expanded by its $\Delta$. These enlarged intervals lie in the frozen
ordinary witness box

$$
 [.20,.24]\times[.45,.50]\times[.11,.14]\times[.46,.52],
 \qquad -.04\le Q\le-.001.                             \tag{4}
$$

Their lower endpoints satisfy $M^0\ge.20656>.2$ and
$A^0\ge.400296>.4$. The inherited necessary bound and identity are

$$
 R^0<.00007,\qquad
 R^0=T^0+(M^0-.2)(A^0-.4),                              \tag{5}
$$

so $T^0<.00007$. The initial-bit terms cancel at this stationary
reference, whose initial marginals are shared across arms. No
cancellation is asserted for the history-dependent actual laws.

The score widths are $w_A=2$ and $w_B=44/25$, and their sum is
$94/25$. Transfer the entire score, including its initial-bit terms.
For every possible history, the predictable total score satisfies

$$
 D_T:=\frac1n\sum_{t=1}^{2n}
       \mathbb E[X_{a_t,t}\mid\mathcal F_{t-1}]-.08
 <.00007+\frac{94}{25}E_R
 =.0008972=:R_N.                                       \tag{6}
$$

Although $D_T$ is generally random, the upper bound is deterministic.

If the stationary reference instead lies outside one expanded interval,
choose any such coordinate before observing the experiment. Every
possible predictable empirical drift for that coordinate lies outside
the unexpanded $H$ on the same side. For $Q$, this follows by adding the
two separately bounded arm drifts, even though their conditional means
depend on different histories. Passing the corresponding empirical gate
therefore requires a martingale displacement of at least $.004$ for a
scalar moment or $A$, or $.006$ for $Q$. These inside and outside cases
are determined by the fixed reference, not by the observed data.

## 4. Conditional variance bounds

Inside the reference case of Section 3, a conditional actual scalar
moment can be $2E_R$ away from the reference, and the reference can be
$2E_R$ beyond $H$. Thus the necessary conditional boxes expand $H$ by
**$4E_R$**, not $2E_R$:

$$
 \begin{split}
 M&\in[.20612,.23088],& C&\in[.45212,.49488],\\
 L&\in[.11312,.13688],& D&\in[.47012,.51388].
 \end{split}                                           \tag{7}
$$

Every conditional initial mean has absolute value at most
$10^{-4}+2E_R=.00054$. For
$X=aY+bIY+gI$, write $m=\mathbb EY,c=\mathbb E(IY),i=\mathbb EI$.
Its variance is

$$
 V=a^2+b^2+g^2+2ab i+2ag c+2bg m-(am+bc+gi)^2.           \tag{8}
$$

On (7), the $A$ score mean is positive and the $B$ score mean is
negative. Substitution into the affine derivatives of (8) proves
$\partial_m V<0$, $\partial_c V<0$ and $\partial_i V>0$ for both
scores. Their maxima are consequently bounded at the lower moment
endpoints and $i=.00054$ by

$$
 V_A\le\frac{75635985159}{250000000000}
       =.302543940636<.31,\qquad
 V_B\le\frac{1636861894119}{6250000000000}
       =.26189790305904<.27.                            \tag{9}
$$

For a target, each conditional law is within $B$ of its fixed nominal
reference. The percent certificate bounds the nominal variances and
the general inequality
$\operatorname{Var}_{P}X\le\operatorname{Var}_{P^*}X+w^2B$
applies separately at every history. It gives the inherited ceilings
$.2911934639<.30$ and $.25322527228864<.27$.

Hence the sum of conditional variances of the $2n$ centered score
increments, each divided by $n$, is at most

$$
 V_N=.58/n\quad\hbox{or}\quad V_T=.57/n,
 \qquad W=2/n                                         \tag{10}
$$

for the null inside the reference gates or for a target, respectively.
The quantities in (10) are deterministic upper bounds on predictable
variance; no empirical variance estimate is used.

## 5. Conditional concentration without independent trials

Here is the concentration argument used for the serial experiment.
Suppose $Z_t$ is a martingale difference, $|Z_t|\le W$, and its
conditional variance is at most a deterministic $v_t$. For
$0\le\lambda<3/W$, expanding the conditional exponential and using
$k!\ge2\cdot3^{k-2}$ for $k\ge2$ gives

$$
 \mathbb E[e^{\lambda Z_t}\mid\mathcal F_{t-1}]
 \le\exp\!\left(\frac{\lambda^2v_t}
                         {2(1-\lambda W/3)}\right).    \tag{11}
$$

Indeed, $|\mathbb E[Z_t^k\mid\mathcal F_{t-1}]|
\le W^{k-2}\mathbb E[Z_t^2\mid\mathcal F_{t-1}]$ bounds every
term of order at least two, and $1+x\le e^x$ completes the estimate.
Iterated conditional expectation multiplies these deterministic
factors. With $V=\sum_t v_t$, Chernoff's inequality and

$$
 \lambda=\frac{\sqrt{2x/V}}{1+(W/3)\sqrt{2x/V}}
$$

yield

$$
 \Pr\!\left\{\sum_tZ_t\ge
       \sqrt{2Vx}+\frac{Wx}{3}\right\}\le e^{-x}.        \tag{12}
$$

The same bound holds for the lower tail by replacing $Z_t$ with
$-Z_t$. For the score, take
$Z_t=(X_{a_t,t}-\mathbb E[X_{a_t,t}\mid\mathcal F_{t-1}])/n$.
Its absolute value is at most the score width divided by $n$, so (10)
supplies (12). The random predictable drift in (6) is bounded
pathwise; it does not have to equal an unconditional expectation.

For gates, the conditional Hoeffding lemma for an increment of range
width $w_t$ gives a conditional MGF bounded by
$\exp(\lambda^2w_t^2/8)$. Iteration therefore gives the one-sided
tail $\exp[-2d^2/\sum_t w_t^2]$. It applies to the deviation from the
predictable empirical drift. A scalar gate uses $n$ nonzero
increments of width $2/n$; $A$ uses $n$ increments of width $3.2/n$;
$Q$ uses $2n$ increments of width $2/n$, with a negative coefficient
on the $B$ arm. No independence of the two arm averages is required.

## 6. The same numerical margins prove size and power

For a target, whole-score transfer of the nominal floor $.00367$
gives the pathwise predictable lower bound

$$
 D_T>.00367-\frac{94}{25}B=.00337296=:R_T.               \tag{13}
$$

Let $\mathcal B(V,W,x)=\sqrt{2Vx}+Wx/3$. The unchanged rational
comparisons from the percent certificate give

$$
 R_N+\mathcal B(V_N,W,3)<.002078<.0021
 <.002154<R_T-\mathcal B(V_T,W,13/4).                    \tag{14}
$$

After subtracting the linear terms, the squared positive margins for
the two outside comparisons are $1/2500000000$ and
$9851449/5625000000000000$.

For a fixed null reference inside the expanded gates, (12) and (14)
bound rejection by $e^{-3}<.05$. Outside them, Section 3 and the
conditional Hoeffding bounds give, for the selected violated gate,
one of

$$
 e^{-n(.004)^2/2},\qquad
 e^{-n(.004)^2/(2\cdot1.6^2)},\qquad
 e^{-n(.006)^2/4},                                    \tag{15}
$$

all below $.05$. The cases are alternatives and their bounds are
combined by a maximum, not by addition. The violated coordinate is
fixed by the reference, so no union over null gates is necessary.

For a target, the nominal moment boxes in the percent certificate and
(1) bound every predictable drift inside each empirical gate. The same
safe distances remain

$$
 d_S=.00346,\qquad d_A=.00358,\qquad d_Q=.00456.          \tag{16}
$$

Consequently the probability of failing any target gate is at most

$$
 \begin{split}
 G&\le8e^{-nd_S^2/2}
       +2e^{-nd_A^2/(2\cdot1.6^2)}+2e^{-nd_Q^2/4}\\
  &=8e^{-29929/2000}+2e^{-32041/5120}+2e^{-3249/250}<.004.
 \end{split}                                           \tag{17}
$$

Together with the lower score tail from (12)--(14), target miss
probability is less than $e^{-13/4}+.004<.044<.05$. These exponential
comparisons admit the same rational certificate
$e^{-x}\le[\sum_{k=0}^{40}x^k/k!]^{-1}$ for $x>0$.

Thus serial dependence costs no additional trials under the stated
uniform conditional budgets. Resetting must establish those budgets
after every history, including histories selected by past readouts.
Neither a small stationary average error nor a nominal mixing time
alone establishes that promise. The test still concerns a fixed pair
of two-time laws and a fixed ordinary reference model; it does not
establish a full multitime compression or allow history-dependent
switching among unrelated ordinary models.
