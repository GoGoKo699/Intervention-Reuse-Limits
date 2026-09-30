# Seven controlled words without rival preparation or numerical tilt calibration

This checkpoint completes the preparation-free unknown-tilt task. On the
chronological menu **L, LL, H, LH, HL, LLH, HLL**, the familiar two-spin
target has attained predictive state counts **three general versus four
ordinary reversible states**, uniformly through **70 ppm maximum per-word
endpoint-pair total-variation error**. The comparison allows arbitrary
word- and history-dependent rival preparation, unknown finite Gibbs tilt,
uncapped reused stochastic kernels, and preparable zero-equilibrium-weight
states. Every persistent predictive state counts.

A separate fixed-budget serial test tolerates one ppm electronic error at
each endpoint and a target-only five-ppm true-boundary pair-law execution
error. Its sufficient budget is **1,176,000,000 complete attempted pairs**,
with false rejection below **0.040389** and target miss below **0.045261**.
This is a conservative cost certificate, not an optimal budget or an
achieved device specification. The 70-ppm population radius and five-ppm
target-power allowance are different statements.

The essential observation is simple: with at most three binary-readout
states and both signs present, one observed sign identifies a single hidden state. Conditioning
on that true word-start sign removes preparation. Two low-field durations
then eliminate the unknown Gibbs reciprocity factor. The target violates
the resulting cubic identity in both sign sectors. Earlier reciprocal
response and path-reversal principles remain the source precedents;
see the [focused source audit](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md).

The population [core report](../reports/familiar_switch_preparation_free_unknown_tilt.json)
and [sampling report](../reports/familiar_switch_preparation_free_unknown_sampling.json)
bind this proof, the source audit and inherited evidence. No earlier
proof, mathematical verifier or report is modified.

## Exact null and measurement boundary

Let `X` be the complete persistent state set, `1 <= |X| <= 3`, with a fixed
deterministic sign `S:X->{-1,+1}`. Let `K_L,K_H` be fixed stochastic kernels
on `X`. There is one normalized nonnegative law `pi_L`, and one unknown
`u in (-1,1)`, such that

```math
 \pi_H(x)=\frac{\pi_L(x)(1+uS(x))}{1+u\pi_LS},
 \qquad \pi_j(x)K_j(x,y)=\pi_j(y)K_j(y,x).
```

The denominator is strictly positive. No irreducibility, mixing rate,
stationary mass floor, CTMC embedding, or preparation equilibrium is
assumed. **All states count**, including zero-stationary-mass states that
can be occupied by preparation. A state can be deleted as unused only if
it is excluded from every preparation and every reachable evolution and
instrument operation. Calling a transient state unsupported does not
remove it from the state budget.

At the active boundary, after any initial instrument action, the initial
record is exactly `A=S(X_0)`. Arbitrary instrument disturbance before this
boundary is absorbed into the preparation. Thus no equilibrium-preserving,
sign-preserving, or fixed initial-instrument channel is required. If a
physical instrument reports a pre-disturbance sign instead, an additional
condition must ensure it equals the active-boundary sign; that is one
possible implementation, not an assumption of the abstract theorem.
The final record is exactly `S(X_T)`. Detector errors are outside this
ideal-boundary theorem unless separately included in a proved observation
model.

Preparation of `X_0` may depend arbitrarily on the previous history and on
the scheduled word. The kernels and readout remain the same throughout.
The words, in chronological order, are

`L, LL, H, LH, HL, LLH, HLL`.

If both signs exist on at most three states, at least one sign `s` is a
singleton `{x_s}`. Conditional on recording that sign, the active state is
known exactly. Its conditional return probabilities are therefore

```math
 r_{w,s}=(K_w)_{x_sx_s},
```

independent of the preparation and history. If a sign never occurs under
the actual preparations, its empirical conditional probabilities are not
available: a quota-based procedure must not reject when that quota is
unfilled. A one-sign model also never completes both sign quotas.

Define for `a=1,2`

```math
 A_a=r_{L^aH,s}-r_{L^a,s}r_{H,s},\qquad
 B_a=r_{HL^a,s}-r_{L^a,s}r_{H,s},\qquad
 F_s=A_1B_2-A_2B_1.
```

The determinant expands to a cubic with six monomials; the apparent
quartic terms cancel. The null assertion is `F_-=0` or `F_+=0`.

## Proof, including zero stationary weights

Write `P={x:pi_L(x)>0}` and `Z=X\P`. The high law has the same support.
Detailed balance implies `K_j(P,Z)=0`, so `P` is closed under both fields.

If the singleton `x_s` lies in `P`, all return paths stay in `P`. Reversibility
of `K_L^a` and the common Gibbs weights yield, for each other state `y`,

```math
 (K_L^a)_{x_sy}(K_H)_{yx_s}
 =\frac{1+su}{1-su}(K_H)_{x_sy}(K_L^a)_{yx_s}.
```

States outside `P` contribute zero. Every other state has sign `-s`.
Subtracting the `y=x_s` term gives

```math
 A_a=\frac{1+su}{1-su}B_a.
```

The same factor applies for both `a`, so `F_s=0` without knowing `u`.

If the singleton lies in `Z`, returns reduce to the substochastic blocks
`T=K_L|Z` and `U=K_H|Z`, because a path leaving `Z` cannot return. Since
`P` is nonempty and `|X|<=3`, `|Z|<=2`. With one zero-weight state every
`A_a,B_a` is zero. With two, index the singleton first. Then

```math
 A_1=T_{12}U_{21},\quad B_1=U_{12}T_{21},\quad
 A_2=(T^2)_{12}U_{21},\quad B_2=U_{12}(T^2)_{21}.
```

The off-diagonal entries of `T^2` are `tr(T)` times those of `T`.
Consequently `A_2=tr(T)A_1` and `B_2=tr(T)B_1`, again giving `F_s=0`.
No reversibility relation is imposed on the zero-weight transient block.
Indeed the fixed-Gibbs-ratio identity can fail there; only its eliminated
determinant is asserted.

## Seven exact target returns

The physical target has two heat-bath spins with energy $`-JSZ-hS`$, equal
unit attempt rates, low field zero and high field $`H`$. Write $`t=\tanh J`$
and $`m=\tanh H`$, with `0<t,m<1`,
and low-equilibrium preparation `pi_0(s,z)=(1+t s z)/4`. Thus initial
signs have probability `1/2` and `E[Z|S=s]=ts`. Allow distinct positive
tick dwells `tau_L,tau_H`.

Set

```math
 b=\frac{t(1-m^2)}{1-t^2m^2},\quad \kappa=\sqrt{tb},\quad
 B=e^{-\tau_H}\cosh(\kappa\tau_H),\quad
 C=e^{-\tau_H}\frac b\kappa\sinh(\kappa\tau_H),\quad E=\frac tb C,
```

```math
 a_H=m(1-B-tC),\quad d_H=m(t-E-tB),\quad
 \beta_a=e^{-a\tau_L}\cosh(ta\tau_L),\quad
 \gamma_a=e^{-a\tau_L}\sinh(ta\tau_L).
```

The seven returns are given by the following formulas for `a=1,2`:

```math
 r_{L^a,s}=\frac{1+\beta_a+t\gamma_a}{2},\qquad
 r_{H,s}=\frac{1+s a_H+B+tC}{2},
```

```math
 r_{L^aH,s}=\frac{1+s a_H+B(\beta_a+t\gamma_a)
                              +C(\gamma_a+t\beta_a)}2,
```

```math
 r_{HL^a,s}=\frac{1+s(\beta_a a_H+\gamma_a d_H)
                         +\beta_a(B+tC)+\gamma_a(E+tB)}2.
```

These follow directly from `K_H S=a_H+BS+CZ`,
`K_H Z=d_H+ES+BZ`, and `K_L^a S=beta_a S+gamma_a Z`.

Let `alpha_s=(1+sm)(1-B-tC)/4` and
`alpha'_s=(1-sm)(1-B-tC)/4`. Subtracting the products gives

```math
 A_a=\alpha_s(1-\beta_a)
      +[-t\alpha_s+(1-t^2)C/2]\gamma_a,
```

```math
 B_a=\alpha'_s(1-\beta_a)
      +[-t\alpha'_s+(1-sm)(E-t^2C)/2]\gamma_a.
```

Use `E-t^2C=(1-t^2)C/(1-m^2)` to evaluate their coefficient determinant,
and `beta_2=beta_1^2+gamma_1^2`, `gamma_2=2 beta_1 gamma_1` for the low
duration determinant. The result is

```math
 \boxed{F_s=-\frac{s m(1-t^2)}8 C(1-B-tC)\gamma_1
       [1-e^{-(1-t)\tau_L}][1-e^{-(1+t)\tau_L}].}
```

All factors except `-s` are strictly positive. In particular `0<kappa<1`
and

```math
 B+tC=\frac{1+\kappa}{2}e^{-(1-\kappa)\tau_H}
       +\frac{1-\kappa}{2}e^{-(1+\kappa)\tau_H}\in(0,1).
```

Thus both singleton candidates are excluded for every stated positive
parameter/dwell choice. This target statement uses its specified
equilibrium preparation; removing the null preparation promise does not
remove the target conditions needed for power.

## Exact nominal certificate

At `t=1/3,m=7/9,tau_L=tau_H=1`, the [core verifier](../scripts/verify_familiar_switch_preparation_free_unknown_tilt.py) encloses the returns
using the frozen degree-40 rational matrix-Taylor helper on the invariant
span `(1,S,Z)`. It explicitly extends the product bound to three factors:
one factor error is at most `8*2^41/41!`, each factor norm is below nine,
and the per-return error ceiling is `500*8*2^41/41! < 3e-34`.

The exact outward enclosures are

```math
 0.000122690606768597\le F_-\le0.000122690606768598,
```

```math
 -0.000122690606768598\le F_+\le-0.000122690606768597.
```

The script also checks the generic factorization as a six-variable
rational polynomial after clearing the positive denominator `1-m^2`,
and checks unknown-tilt singleton elimination using seven-variable
symbolic reversible flux fixtures for both orientations. Eight-variable
transient-block fixtures check the zero-mass extension independently.

## Robust population separation and attained state counts

In coordinate order $`(a,b,c,d,e,f,g)=(r_L,r_{LL},r_H,r_{LH},r_{HL},r_{LLH},r_{HLL})`$,

```math
 F=dg-fe+ac(f-g)+bc(e-d).
```

The core report gives fixed rational centers $`c_s`$ enclosing each nominal
return to coordinate error below $`10^{-12}`$. On each radius-$`10^{-3}`$
box about its center, exact interval polynomial arithmetic gives:

| Sign | Gradient one-norm bound | Sum of absolute Hessian entries | Bernoulli score variance sum bound |
| --- | ---: | ---: | ---: |
| $`-`$ | $`67/100`$ | $`14`$ | $`11/500`$ |
| $`+`$ | $`4/5`$ | $`18`$ | $`7/250`$ |

The variance sum bounds $`\sum_w g_{s,w}^2p_w(1-p_w)`$ for fixed center
gradients $`g_s=\nabla F(c_s)`$ and any coordinate means in the box.
The verifier checks the stronger version with interval gradient maxima.
It also certifies each center's signed score above
$`D=12269/10^8=0.00012269`$. These rational constants are reused below.

If all seven conditional returns of each sign are within
$`\epsilon=3/20000=150`$ ppm of the target, the segment joining them to the
target lies inside its certified box. The mean-value theorem gives

```math
 |F_s(r)-F_s(r^*)|\le\frac45\epsilon=0.00012.
```

Both signs therefore retain their nonzero target orientation with margin
strictly above $`269/10^8=2.69`$ ppm, excluding every ordinary model with
at most three counted states. A zero-probability sign stratum provides no
conditional return and is not sufficient data for this conditional claim.

For complete pair laws, use TV in the convention
$`\mathrm{TV}(P,Q)=\tfrac12\sum|P-Q|`$. Each target initial sign has
mass $`1/2`$. If a rival word law is within $`\delta\lt 1/2`$ of the target,
its corresponding sign mass $`q`$ is at least $`1/2-\delta`$. For the target
conditional return $`r`$, the function
$`1\{I=s\}(1\{Y=s\}-r)`$ has oscillation one and target mean zero.
Its expectation under the rival is $`q(\widetilde r-r)`$, so

```math
 |\widetilde r-r|\le\frac{\delta}{1/2-\delta}.
```

At $`\delta=7/100000=70`$ ppm this is $`7/49993\lt 3/20000`$. Both sign
strata necessarily occur, separately for every word; a common rival
preparation is unnecessary. The determinant margin is strictly above

```math
 \frac{12269}{10^8}-\frac45\frac7{49993}
 =\frac{53364117}{4999300000000}\gt 0.
```

To obtain exact state counts, a general two-state model with both signs
has one state of each sign. Regardless of word-specific preparation,
reuse of its low-field kernel forces

```math
 r_{LL,+}=r_{L,+}^2+(1-r_{L,+})(1-r_{L,-}).
```

The target has $`r_{L^a,s}=(1+c(a))/2`$, where
$`c(\tau)=\tfrac23e^{-2\tau/3}+\tfrac13e^{-4\tau/3}`$. Its composition
residual is

```math
 \Delta=\frac{c(2)-c(1)^2}{2}
       =\frac19(e^{-2/3}-e^{-4/3})^2\gt \frac{69}{10000}.
```

On the unit square the two derivative magnitudes of the right-hand side
are bounded by two and one. Conditional errors at most $`\epsilon`$
therefore change this residual by at most $`4\epsilon`$. At the certified
$`\epsilon=3/20000`$, it stays above $`63/10000`$. This excludes general
models with at most two states even without Gibbs or reversibility
assumptions.

The [inherited three-state construction](FAMILIAR_SWITCH_FROZEN_EQUIVALENCE.md)
uses sign $`S=(-1,1,1)`$, auxiliary function $`Z=(-1/3,-2/3,5/3)`$ and one
preparation $`\rho=(1/2,2/7,3/14)`$. Its positive rational generators are

```math
 Q_L=\begin{pmatrix}-4/9&8/21&4/63\\11/18&-20/21&43/126\\2/9&8/21&-38/63\end{pmatrix},\quad
 Q_H=\begin{pmatrix}-72/85&432/595&72/595\\3/17&-69/119&48/119\\1/85&334/595&-341/595\end{pmatrix}.
```

They have the prescribed Gibbs stationary laws and close on the same
functions $`(1,S,Z)`$ as the physical target:
$`Q_LS=-S+Z/3`$, $`Q_HS=63/85-S+12Z/85`$, and $`Q_jZ=S/3-Z`$.
Their initial sign masses are $`1/2`$ and $`\mathbb E_\rho[Z\mid S=s]=s/3`$.
Thus every finite-word endpoint-pair law agrees with the target, including
the seven current words. This is an endpoint-pair claim, not full visible
trajectory equality. The general upper chooses a common preparation,
which is permitted in the larger arbitrary-preparation class. The physical
four-state target supplies the ordinary upper. Consequently

```math
 \boxed{D_{\rm general}(\delta)=3,\qquad
        D_{\rm ordinary}(\delta)=4\quad(0\le\delta\le70\ {\rm ppm}).}
```

The general comparison retains the common Gibbs force and deterministic
readout interface while dropping detailed balance. The ordinary comparison
uses time-even states and ordinary detailed balance. The target itself is
reversible at each held field; this is a constrained state-realization
separation, not evidence that the target violates detailed balance.

## Measurement boundary and what remains assumed

The true initial sign is the sign **after the initial instrument and
before active evolution**. An instrument may kick the hidden state,
change its sign, or vary with history and word before that boundary.
Those operations only choose the rival's preparation. No null
low-equilibrium reset or fixed, sign-preserving initial channel is needed.
A device that reports only the pre-kick sign must separately establish
its relation to the post-instrument sign used here. The theorem does
not infer that relation from an average detector fidelity.

The reused active kernels must hold conditional on the full relevant
previous history and current predictive state. A detector or controller
record that changes subsequent kinetics cannot be hidden from the state
budget. Merely matching unconditional Markov marginals is insufficient.
The final true sign is taken at active-word completion, before final
acquisition. The next sections allow electronic disagreement with these
two true boundary signs.

Target power still needs the stated target preparation and execution
accuracy at these boundaries. Arbitrary initial backaction is harmless
for null validity but can destroy the target signal. The target-only
five-ppm conditional pair-law promise below includes this effect.

## Data contract and exact test

For a trial, I and Y denote the true signs at the beginning and end of the
active word. The initial boundary is **after** the initial instrument;
its preceding disturbance can be arbitrary. The recorded labels are
Ihat and Yhat. The scheduled word is chosen before current preparation
and initial observation. For each word perform M=168,000,000 trials,
interleaved in a fixed cycle. Total trials are7M=1,176,000,000.

In each word/recorded-initial-sign group retain its first n=80,000,000
records and average1{Yhat=s}. Retention is decided from Ihat and previous
counts before seeing Yhat. If any of the14 groups is incomplete at the
fixed cap, do not reject.

Use the exact rational centers c_s and fixed gradients g_s from the
[core report](../reports/familiar_switch_preparation_free_unknown_tilt.json). Define the **tangent**, not the
empirical determinant,

    W_s = F(c_s)+g_s dot (rhat_s-c_s).

Reject only if all14 coordinate gates |rhat_ws-c_ws|<=1/2000 pass and

    W_- >55/10^6,       W_+ <-62/10^6.

No fitted parameter, optional stopping, adaptive threshold, or direct
division by an empirical sign frequency is used. Failure to reject is
not an assertion that the null fits.

The null consists of one fixed ordinary reversible at-most-three-state
model with the specified unknown-tilt Gibbs interface and reused active
kernels. Conditional on the full relevant past and actual current model
state, active evolution follows those same fixed kernels. Initial
preparation and initial-instrument kicks may depend arbitrarily on the
past and scheduled word. Apparatus memory changing the active kernels
must be included in the predictive state; unconditional Markov marginals
alone are not sufficient. Boundary-registration errors may correlate
with kicks and final outcomes, subject to the next paragraph.

Let H_t be the complete joint past before current preparation, including
previous true boundary signs, error events and relevant apparatus
information. For each endpoint j=i,f assume, almost surely,

    Pr(recorded endpoint != true active-boundary sign | H_t, word)
       <= eta =1/10^6.                                   (1)

No symmetry, constant flip probability, endpoint-error independence or
independence of different trials is assumed.

## Corruption counts without selected-row error calibration

For each of the7 words and2 endpoints count all its label errors, E_wj,
among the M attempts. The conditional Bernoulli MGF bound at t=log2
gives

    Pr(E_wj>280) <=2^-280 (1+eta)^M
                 <=2^-280 exp(M eta)
                 <2^-280(11/4)^168.

The last strict comparison uses e<11/4 and M eta=168. Therefore the
global bad-count probability is at most

    gamma_E =14(11/4)^168 /2^280 <4.64e-10.              (2)

Let G_E be the complementary event. This is not a conditioning step in
the concentration proof: all final risk bounds add gamma_E separately.

For each word/sign, form an oracle list of the first n trials whose
**true postinstrument boundary sign** is s. If fewer occur, append
independent artificial Bernoulli records of that row's fixed reference
return probability to fill it. For the null, only one singleton row
needs this probabilistic interpretation; for the target both rows do.
These artificial records are a proof device, not additional acquisition.

Relabeling E_wi initial labels changes at most E_wi members of a first-n
selection, including the padded comparison. Pair removals with insertions;
each replacement changes a binary average by at most1/n. The E_wf final
errors change at most that many retained return indicators. Hence on
observed completion and G_E,

    |rhat_observed_ws-rhat_oracle,padded_ws|
       <=(E_wi+E_wf)/n <=560/n=7/10^6=:d_E.             (3)

This deterministic inequality needs no detector-error independence and
no bound on error probability conditional on a rare observed sign. If a
null has only one true sign, its opposite observed quota cannot complete
on G_E because280<n. Such models can reject only on the same bad-count
event already charged in (2).

## Oracle conditional means and the correct filtration

Fix one singleton sign of a two-sign null **before** observing the data.
Its true boundary state is the singleton, so each retained oracle return
has one fixed mean r_ws, independently of preparation. The analytic
theorem gives F(r_s)=0. No union over possible singleton signs is needed
for type I error; the other sign's response can vary with history.

For power, assume one fixed nominal balanced target such that every
word's true-boundary pair law, conditional on H_t before current
preparation, is within

    B=5/10^6

of that target's ideal pair law. This is a target-only execution promise;
it is not imposed on rival preparation. The target reference sign mass
is1/2. For a reference return r, the bounded function
1{I=s}(1{Y=s}-r) has oscillation one and reference mean zero. Consequently
the oracle conditional return probability differs from r by at most

    b_T=B/(1/2-B)=1/99999.                              (4)

The oracle filtration reveals the current true initial sign to decide
retention, but does not also reveal the current hidden target state or
current electronic error transcript before taking the conditional return
mean. Integrate over those current variables. All previous histories are
retained in the filtration. A conditional pair-TV bound averaged over
the hidden current state would not imply (4) after revealing that state.
For a singleton null the full-state and sign distinction disappears.

Padding records have their reference means and introduce zero drift.
For a fixed score, retain its appropriate coefficient times a centered
Bernoulli increment when an oracle record is selected and zero otherwise.
After padding, each of the7 groups has exactly n terms. Apply the stopped
exponential supermartingale over the original finite trial horizon and
the artificial completion. This proves concentration jointly with the
observed-completion event; no law is conditioned on completing quotas.

## Exact local constants and linear concentration

For each sign let R=1/1000 and use the box ||r-c_s||_infinity<=R. The
analytic certificate proves the following rational bounds over the box:

| sign | gradient l1 bound L_s | absolute Hessian-entry sum H_s | Bernoulli score variance sum V_s |
| --- | ---: | ---: | ---: |
| - |67/100 |14 |11/500 |
| + |4/5 |18 |7/250 |

The variance bound includes all7 Bernoulli coordinates with their fixed
center-gradient coefficients. In fact the certificate proves the
stronger bound using componentwise gradient maxima throughout the box.
The centered single-return increment is less than.23, and use the safe
b_inc=1/4. Every target coordinate is within CE=10^-12 of its rational
center, and each rational **center itself** has signed F magnitude
greater than D=12269/10^8=0.00012269.

For a null reference inside this box, the oracle Bernoulli means are its
fixed return coordinates, so V_s applies. For the target, the actual
conditional oracle means are within b_T+CE<R of the center, so V_s also
applies to their conditional variances. No global-variance claim outside
the local box is used.

The stopped martingale Bernstein inequality yields either one-sided
score deviation beyond its predictable drift with bound

    exp[-n a^2/(2(V_s+b_inc*a/3))].                    (5)

The target drift is at most L_s b_T. Its center mismatch contributes
at most L_s CE. The observed/oracle replacement contributes at most
L_s d_E. These enter through separate deterministic comparisons, not
by assuming unbiased electronic errors.

## Null size

If the singleton reference lies inside its R-box, F(r_s)=0 and Taylor's
theorem give |W_s(r_s)|<=H_s R^2/2. Consequently on G_E rejection forces
a one-sided oracle fluctuation of at least

    a_N,s=T_s-H_s R^2/2-L_s d_E,
    T_-=55/10^6, T_+=62/10^6.

These margins are43.31ppm and47.4ppm, respectively. Formula (5) gives
tails less than.033044298765 and.040388733132.

If the fixed singleton reference is outside its R-box, some fixed
coordinate differs from its center by more than R. On G_E the observed
gate can pass only if the padded oracle coordinate deviates from its
reference by at least R-1/2000-d_E. Conditional Hoeffding gives the
single-coordinate bound

    gamma_Ngate=2 exp[-2n(R-1/2000-d_E)^2].              (6)

The inside and outside cases partition fixed null models, so take their
maximum rather than summing them. The complete type I bound is

    alpha <= gamma_E+max(gamma_Ngate, tail_N,-,tail_N,+)
           <0.040389.

## Target power and completion

Each target score has sufficient separation after center, drift and
registration replacement errors:

    a_T,s=D-T_s-L_s(d_E+b_T+CE).

These are greater than56.2999ppm for sign- and47.0899ppm for sign+.
Their Bernstein tails are less than.003145349958 and.042114768683.
Only the **center** score lower bound is used here, so the linear CE
charge occurs once; there is no R^2 curvature penalty at the target.

On G_E and observed completion, target gate failure requires at least
one of14 padded oracle coordinates to deviate from its fixed target
reference by at least1/2000-d_E-CE. Removing predictable bias b_T and
using two-sided conditional Hoeffding gives

    gamma_Tgate=28 exp[-2n(1/2000-d_E-b_T-CE)^2].        (7)

At each target attempt the observed initial-sign probability is at
least q_T=1/2-B-eta. This follows from the target true-pair contract
and the endpoint-error bound (1), conditional only on $`H_t`$ and the scheduled
word, without
conditioning on the current error. Conditional Hoeffding and a union
over14 quotas give

    gamma_quota=14 exp[-2(M q_T-n)^2/M].                (8)

Putting these separate error events into a union bound,

    beta <=gamma_E+tail_T,-+tail_T,++gamma_Tgate+gamma_quota
          <0.045261.

The [sampling verifier](../scripts/verify_familiar_switch_preparation_free_unknown_sampling.py)
checks all margins and exponential bounds using exact rational arithmetic,
including the fixed cap, registration-error counts and the inherited local
geometry. It binds the finalized core report. The certified risk bounds
are $`\alpha\le0.0403887335941`$ and $`\beta\le0.0452601191033`$.
The broader 70-ppm population ball is not the test's five-ppm target-power
contract. No null preparation-closeness condition is introduced by the
sampling proof.

## Acquisition resources and comparison with the previous task

Repeat the ordered seven-word cycle $`M=168,000,000`$ times. Each attempt
starts at low field and returns to low field after its final observation.
Counting a same-low-field tick boundary as a seam rather than a field
transition gives the following exact upper accounting:

| Resource | Per cycle | Complete fixed budget |
| --- | ---: | ---: |
| Complete pairs and initial reset opportunities | 7 | 1,176,000,000 |
| Endpoint observation windows | 14 | 2,352,000,000 |
| Active unit ticks | 14 | 2,352,000,000 |
| Low-field active ticks | 9 | 1,512,000,000 |
| High-field active ticks | 5 | 840,000,000 |
| Upward field transitions | 5 | 840,000,000 |
| Downward field transitions | 5 | 840,000,000 |
| Same-low-field seams | 3 | 504,000,000 |

The [earlier target mixing certificate](FAMILIAR_SWITCH_SERIAL_ACQUISITION.md)
puts a $`24/\Gamma`$ low-field reset below quarter-ppm preparation TV for
the nominal four-state target. If used before every pair, reset exposure
is $`28.224`$ billion$`/\Gamma`$, and reset plus active exposure is
$`30.576`$ billion$`/\Gamma`$. With nonoverlapping initial/final observation
windows $`T_i,T_f`$ and transition times $`t_\uparrow,t_\downarrow`$, add

```math
 1.176\times10^9(T_i+T_f)
 +0.840\times10^9(t_\uparrow+t_\downarrow)
```

and any other acquisition/calibration overhead. This is conditional
resource accounting; no device speed or achieved combined accuracy is
asserted. The target reset alone does not certify the post-instrument
state. Preparation error, initial disturbance and active-control error
must jointly meet the five-ppm true-boundary pair-law promise; electronic
endpoint misregistration has its separate one-ppm allowance. None of this
requires equilibration of arbitrary rivals.

The preceding five-word serial test used 50 million pairs and a one-ppm
conditional recorded-law distance to a fixed reference family on both
sides, including rival preparation. The present seven-word test removes
that null preparation burden while retaining unknown tilt, at a much larger
certified budget. It retains L, LL, H and HL, drops HH, and adds LH, LLH
and HLL. Seven rather than five settings is a net increase of two; it is
not the old menu with two settings appended. Each word has at most three
ticks and two field plateaus. Counts from distinct task contracts should
not be described as an efficiency improvement or a same-task optimum.

The old five-word information lower bound does not automatically become
a lower bound for this larger preparation-free seven-word task. The next
scientific priority is to determine whether the high sufficient cost is
intrinsic: construct admissible close rivals and derive an information
lower bound for this exact menu and observation contract before further
minor tuning of constants. A shorter or statistically stronger witness
would also require a new theorem, not a change to the accepted physics.

## Scope of completion

The analytic null identity, its zero-stationary-mass extension, the target
factorization, robust attained state counts, and the finite-budget serial
sampling guarantee are complete under their stated assumptions. Exact
finite checks verify their numerical and algebraic premises; they do not
enumerate all possible histories or establish experimental feasibility.
Independent internal review checked the population and martingale proofs,
including the delayed electronic transcript and proof-only padding.

The [source audit](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md)
separates established reciprocity and detector principles from this
specific controlled state-count result. Full novelty, physical usefulness
at the certified budget, and publication significance remain open.
Manuscript drafting remains deferred until those questions are clearer.
