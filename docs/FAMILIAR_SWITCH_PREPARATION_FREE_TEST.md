# A four-word test with no rival preparation promise

Four short words, $0$, $H$, $0H$, and $H0$, replace a hidden-state reset
assumption by a directly tested return identity. Every ordinary model
with at most three states has a readout sector containing one state.
Conditional on observing that sector, its hidden starting state is known,
regardless of how the apparatus was prepared. Detailed balance then
relates four conditional return probabilities.

This note proves an ideal-readout test with **nine million trials**, at
most two field plateaus per trial, and eighteen million recorded binary
values. Its false-rejection probability is below $5\%$ for arbitrary
history-dependent rival preparation; its power is above $95\%$ on the
entire certified one-percent kinetic target family under the stated
conditional execution budget. No rival mixing time, equilibrium
preparation, balance, or preparation calibration experiment is assumed.
The stationary force relation, fixed dynamics, and initial-instrument
conditions below remain premises.

This is a new four-word experiment. The older two-word score test and its
detector assumptions are unchanged. Electronic readout errors are not
included in this note's ideal-bit theorem. Manuscript drafting remains
deferred.

[Exact verifier](../scripts/verify_switch_preparation_free.py) ·
[Certificate report](../reports/switch_preparation_free.json) ·
[Four-word three-state realization](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md)

## 1. The null and its initial instrument

Let $P_0,P_H$ be one fixed pair of stochastic kernels on at most three
states, with deterministic binary readout $S$. Both kernels obey detailed
balance for strictly positive stationary laws $\pi_0,\pi_H$, related by

$$
 \pi_H(x)=\frac{\pi_0(x)(1+uS(x))}{1+u\pi_0S},
 \qquad u=\frac35.                                      \tag{1}
$$

There is no constraint on $\pi_0S$, no positive lower bound on any
stationary mass, and no restriction on transition rates or the rival
graph. Strict positivity is needed: reversibility against a law assigning
zero mass to a transient state would not supply the transition ratios
used below. The argument also applies to arbitrary reversible stochastic
kernels, without requiring continuous-time embeddability.

The initial instrument records the true pre-instrument sign and then
applies a fixed stochastic channel $D$ that preserves that sign:

$$
 D(x,y)=0\quad\text{when }S(x)\ne S(y).                  \tag{2}
$$

For the null, $D$ need not preserve equilibrium. Motion inside a
multi-state readout sector can be arbitrary. On a singleton sector (2)
forces the state to remain fixed. The final readout records the true
final sign; its subsequent disturbance is irrelevant within the trial.
The model and field kernels are fixed across all words and trials. The
preparation before each initial instrument may depend arbitrarily on
the full past and on the scheduled word. That freedom changes how often
the singleton is encountered, but not its conditional responses.

Both signs must be observed to complete the test. If a model has only
one readout sign, the test never rejects it.

## 2. A conditional return identity

For a sign $s$ whose sector is a singleton state $x_s$, write

$$
 r_{0,s}=(P_0)_{x_sx_s},\qquad
 r_{H,s}=(P_H)_{x_sx_s},\qquad
 r_{0H,s}=(P_0P_H)_{x_sx_s},\qquad
 r_{H0,s}=(P_HP_0)_{x_sx_s}.                            \tag{3}
$$

These are exactly the final return probabilities conditional on the
recorded initial sign being $s$. The preparation and instrument disappear
from (3) because the post-instrument state is necessarily $x_s$.

Every other state has sign $-s$. For any such state $y$, detailed balance
and (1) imply

$$
 (P_0)_{x_sy}(P_H)_{yx_s}
 =\lambda_s(P_H)_{x_sy}(P_0)_{yx_s},\qquad
 \lambda_s=\frac{1+su}{1-su}.                           \tag{4}
$$

The $y=x_s$ term is $r_{0,s}r_{H,s}$ in either order. Summing (4) gives

$$
 r_{0H,s}-\lambda_sr_{H0,s}
   =(1-\lambda_s)r_{0,s}r_{H,s}.                        \tag{5}
$$

Use the bounded-coefficient version

$$
 \boxed{R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}
                  +2su\,r_{0,s}r_{H,s}=0.}             \tag{6}
$$

Every at-most-three-state model with both signs has at least one
singleton, so it satisfies $R_-=0$ or $R_+=0$. This statement permits
different preparations for different words and histories. It is not an
equilibrium inference from binary balance or a low-field relaxation
record. The observed sign identifies the actual singleton state.

## 3. Both target sectors violate the identity

For the four-state target with equilibrium preparation, let the usual
two-word moments be

$$
 m=\mathbb E S_{0H},\quad c=\mathbb E(S_iS_{0H}),\quad
 \ell=\mathbb E S_{H0},\quad d=\mathbb E(S_iS_{H0}).
$$

The initial mean is zero. Stationarity and the exact tilt give the
single-word correlations

$$
 a=1-m/u,\qquad x=(\ell+ud)/u.                         \tag{7}
$$

Consequently the four conditional return probabilities are

$$
 \begin{split}
 r_{0,s}&=(1+x)/2,&
 r_{H,s}&=(1+a+sm)/2,\\
 r_{0H,s}&=(1+c+sm)/2,&
 r_{H0,s}&=(1+d+s\ell)/2.
 \end{split}                                           \tag{8}
$$

Substitution in (6) gives the exact relation to the latent snapshot
witness,

$$
 R_s=\frac{1-su}{2u}\,F_s,\qquad
 F_s=u(c-d)-su\,md+s(u-m)\ell.                         \tag{9}
$$

For equal-attempt heat-bath dynamics at general positive parameters,
write $t=\tanh J$, $u=\tanh H$, and use the closed-mean coefficients
$d_0=e^{-a_0}\sinh(ta_0)$ and
$\gamma=e^{-a_H}(B/\kappa)\sinh(\kappa a_H)$, where
$B=t(1-u^2)/(1-t^2u^2)$ and $\kappa=\sqrt{tB}$. Then

$$
 R_s=-\frac{su}{2}\,d_0\gamma(1-t^2).                  \tag{10}
$$

Thus $R_->0$ and $R_+<0$ for all finite positive $J,H,a_0,a_H$.
At $J=\log3$, $H=\log2$, and $a_0=a_H=5/4$, their common nominal
magnitude is approximately $.0099156766501$.

For robustness, allow the same eight independent field-specific edge
conductance multipliers in $[.99,1.01]$ as in the
[one-percent kinetic theorem](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md).
The new verifier reuses its exact moment polynomials and outward
remainder, sets both detector contrasts to one, and forms (9) before
bounding coefficient magnitudes. It certifies the strict bounds

$$
 \boxed{R_->\frac9{1000},\qquad R_+<-\frac9{1000}.}     \tag{11}
$$

Here is a reproducible description of the additional numerical step.
If $p_m,p_c,p_\ell,p_d$ are the inherited moment polynomials and $\rho$
their shared error radius, substitute them into (9) to obtain a
polynomial $p_{R_s}$. Its constant coefficient, plus or minus the sum
of absolute nonconstant coefficients times the relevant parameter
radii, encloses its entire parameter range. Widen each endpoint by
$4\rho+3\rho^2$. This allowance is conservative: the inherited
containing moment box, expanded by $\rho$, bounds the gradient
$\ell_1$ norm of (9) below four throughout each segment joining the
true and polynomial moments. It gives enclosures lying inside
$[.0090387,.0107927]$ for $R_-$ and
$[-.0107334,-.0090980]$ for $R_+$. Displayed decimals are descriptive;
the strict comparison with (11) uses exact rational arithmetic.

The companion realization note explains why the same general
three-state predictor matches all four ideal equilibrium pair laws.
Adding the two single-word experiments therefore preserves the
three-versus-four state-count comparison.

## 4. A fixed acquisition rule

Cycle deterministically through $0,H,0H,H0$ for

$$
 N=9{,}000{,}000\quad\text{trials},\qquad
 M=N/4=2{,}250{,}000\quad\text{trials per word}.          \tag{12}
$$

Within each of the eight word/initial-sign groups retain the first
$n=1{,}000{,}000$ final signs. Their return indicators have averages
$\widehat r_{w,s}$. Group membership and retention are decided by the
initial sign and previous counts, before seeing the current final sign.
Extra outcomes in a full group are ignored for these averages.

If any group remains incomplete at the fixed cap $N$, do not reject.
Otherwise compute (6) from the eight averages and reject only when

$$
 \boxed{\widehat R_->.004\quad\text{and}\quad
        \widehat R_+<-.004.}                           \tag{13}
$$

No initial-sign postselection occurs before preparation, and no hidden
state is selected. Retaining a fixed number of observed-sign records is
part of the statistic. Incomplete groups cause nonrejection, rather than
an unbounded experiment.

## 5. Concentration for the retained records

Fix one sign and fixed reference return probabilities $r_w$.
Suppose that, whenever a record is retained in word $w$, its conditional
return probability differs from $r_w$ by at most $b$. The null singleton
has $b=0$. Put $\Delta_w=\widehat r_w-r_w$ and

$$
 L_s=(1-su)\Delta_{0H}-(1+su)\Delta_{H0}
       +2su(r_H\Delta_0+r_0\Delta_H).
$$

The exact polynomial expansion is

$$
 \widehat R_s-R_s=L_s+2su\Delta_0\Delta_H.              \tag{14}
$$

The sum of absolute linear coefficients is at most $22/5$, and their
squared sum is at most

$$
 (1-su)^2+(1+su)^2+4u^2(r_0^2+r_H^2)
 \le2+10u^2=\frac{28}{5}.                             \tag{15}
$$

For any positive $h$, the conditional Hoeffding lemma applied to the
retained, centered Bernoulli increments gives either one-sided bound

$$
 \Pr\{\text{groups complete},\ \pm L_s>(22/5)b+h\}
 \le\exp\!\left(-\frac{2nh^2}{28/5}\right).            \tag{16}
$$

This does not condition the distribution on completion. In the original
fixed-horizon trial filtration, set an increment to zero whenever the
trial is in another group or its quota is already full. Otherwise give
its centered return indicator the corresponding coefficient divided by
$n$. The decision to include it is known before its final readout.
At most $n$ increments occur in each group, so their total squared
range widths are at most the right side of (15) divided by $n$.
Iterated conditional moment-generating-function bounds, or equivalently
the stopped exponential supermartingale, prove (16) on the event of
completion. The predictable reference displacement contributes at most
$(22/5)b$. No independence after conditioning on completion is asserted.

For $\eta>b$, the same argument for the low and high single-word
averages gives

$$
 \Pr\{\text{groups complete},\
          \max(|\Delta_0|,|\Delta_H|)>\eta\}
 \le4e^{-2n(\eta-b)^2}.                               \tag{17}
$$

Take $\eta=1/100$. Outside (17), the quadratic term in (14) is at
most $2u\eta^2=3/25000=.00012$ in absolute value.

## 6. Uniform size and conditional target power

For a null, choose any singleton sign before observing the data. Its
reference probabilities obey $R_s=0$ and $b=0$. Rejection requires the
one-sided deviation in (13) for that sign, so (16)--(17) give

$$
 \Pr_{\rm null}(\text{reject})
 \le \exp\!\left[-\frac{2n(.004-.00012)^2}{28/5}\right]
       +4e^{-2n(.01)^2}
 =e^{-9409/1750}+4e^{-200}<.005<.05.                  \tag{18}
$$

There is no union over possible singleton signs: for each fixed model,
one valid sign is fixed before the experiment. Arbitrarily unbalanced
preparation can prevent completion, which only decreases rejection.

For a target, assume one fixed reference member of the nominal-field,
nominal-time one-percent kinetic family such that, conditional on every
preparation history, the actual ideal-bit pair law of each of the four
words differs from its reference by TV at most

$$
 B=\frac{79}{10^6}.                                   \tag{19}
$$

This is a target execution promise, not a rival preparation promise.
The conditional finite-reset and execution accounting used in the
[serial-sampling theorem](FAMILIAR_SWITCH_SERIAL_SAMPLING.md) supplies
(19) for the two-word protocols. Its same physical bound supplies the
single-word protocols: there is the same preparation and initial
instrument, with fewer field plateaus and no longer active duration.
Specifically, for $\epsilon=10^{-5}$ the common upper bound remains

$$
 2\epsilon+
 \left[\frac12+\frac{101}{100}\left(\frac54+\epsilon\right)\right]
 \epsilon+\frac{101}{25}\epsilon
 =.000078025101<B.                                    \tag{20}
$$

The terms respectively cover preparation plus initial instrument,
equilibrium-field and active-rate changes, and timing. Ideal electronic
readout is used here. The finite-reset argument remains needed for the
specified physical target. It is never imposed on its rivals.

The reference initial sign has probability $1/2$. If $r$ is its
conditional return probability, the function
$f=\mathbf1_{\{S_i=s\}}(\mathbf1_{\{S_f=s\}}-r)$ has range width
one and reference mean zero. Thus (19) bounds its actual mean by $B$,
while the actual initial-sign probability is at least $1/2-B$.
Every selected target record therefore has conditional return error

$$
 b\le\frac{B}{1/2-B}=\frac{79}{499921}.                 \tag{21}
$$

For each arm, failure to obtain $n$ records of either sign requires a
downward deviation from an initial-sign count with conditional success
probability at least $1/2-B$. Conditional Hoeffding and a union over
the eight groups bound quota failure by

$$
 8\exp\!\left[-\frac{2(M(1/2-B)-n)^2}{M}\right]
 =8e^{-249289505521/18000000}.                          \tag{22}
$$

On completed groups, use (11), (14)--(17), and (21). Each signed target
residual can fail its threshold only through a linear deviation with
margin

$$
 h_T=.009-.004-\frac{22}{5}\frac{79}{499921}-.00012>0.
$$

The total target miss probability is at most

$$
 \begin{split}
 2\exp\!\left[-\frac{2nh_T^2}{28/5}\right]
  +8e^{-2n(.01-79/499921)^2}
  +8e^{-249289505521/18000000}
 &<.004<.05,\\
 \frac{2nh_T^2}{28/5}
 &=\frac{1367663932665522}{218680880460875}>6.25.
 \end{split}                                          \tag{23}
$$

The verifier checks the displayed exponential comparisons using
$e^{-x}\le[\sum_{k=0}^{40}x^k/k!]^{-1}$ and exact fractions.
This proves the stated $5\%$ size and $95\%$ power guarantees with
considerable margin, uniformly over the allowed adaptive target
preparations.

## 7. Scope of the simplification

The statistic uses a finite-state structural fact: a binary readout on
at most three states has a singleton. The initial readout turns that
fact into a known conditional starting state. It removes the need to
certify hidden preparation for the ordinary small-state null and avoids
the large coefficients in the optional five-type observable-preparation
correction. Its two added single-word experiments are also matched by
the existing three-state general realization.

The price is four word types and faithful ideal initial/final signs in
the theorem above. Exact sign preservation by the null's initial
instrument is essential. An initial electronic mislabel can select a
multi-state sector under the apparent singleton label, and a
sign-changing instrument can leave the singleton after recording it.
Such errors require a separate analysis; the previous two-word detector
allowances cannot be substituted here. The argument concerns the four
initial/final pair laws and does not establish matching full trajectory
laws or remove the shared stationary force relation.
