# Five million trials with one-percent kinetic variation

The same two-protocol experiment admits a **five-million-trial** test
uniformly over eight independent kinetic prefactors in $`[.99,1.01]`$.
The false-rejection probability is below $`5\%`$ and power is above
$`95\%`$, including the stated preparation, field, timing and initial
instrument allowances. The ordinary null receives an additional
observed joint-table total-variation (TV) allowance $`e=2\cdot10^{-4}`$
per protocol. This exceeds the general three-state predictor's
constructive error bound $`.000079`$ for the same target family.

The experiment retains $`J=\log3`$, $`H=\log2`$, dwell times $`5/4`$, the
two chronological words $`0H,H0`$, and an initial and final binary
readout per trial. Each undirected transition edge has one positive
prefactor at each field, shared by both transition directions and by
both protocols. The four prefactors at either field may vary
independently. Detailed balance and the Gibbs laws are preserved;
the heat-bath moment closure need not be preserved.

This uses the previous integer score with **new empirical gates and a
new threshold**. Its measurement allocation and null allowance equal
those of the [earlier kinetic test](FAMILIAR_SWITCH_KINETIC_SCORE_TEST.md),
while its admitted relative-prefactor tolerance increases from
$`2\cdot10^{-5}`$ to $`.01`$, a factor of $`500`$. The guarantee below is
proved afresh for the larger family. It is a sufficient measurement
budget, not an optimum or a laboratory feasibility claim. Manuscript
drafting remains deferred.

## 1. Promises and the fixed test

Target detector errors are arbitrary fixed values $`p_0,p_f\in[0,.01]`$;
ordinary rivals may choose any fixed values in $`[0,1/2]`$. Both uses
are independent symmetric bit flips, independent of the hidden
dynamics. The preparation, initial instrument and detector channels
are shared across the two protocols within each model. Different
models may use different detector errors. Trials are freshly prepared
and independent; the two observations within a trial are not assumed
independent.

The inherited stationary ordinary class permits at most three states,
arbitrary reversible kernels, low-field imbalance $`|v|\le10^{-4}`$,
tilt parameter $`|u-3/5|\le10^{-4}`$, and stationary tilt TV error at
most $`10^{-5}`$. Execution and approximation allowances are stated
below. These promises are not inferred from passing the test gates.

Write $`(I,Y)`$ for the recorded initial and final signs in arm $`0H`$,
and $`(J,Z)`$ for those in arm $`H0`$. Use the fixed score table:

| Protocol | $`(+,+)`$ | $`(+,-)`$ | $`(-,+)`$ | $`(-,-)`$ |
|---|---:|---:|---:|---:|
| $`0H`$: $`50X_A`$ | 35 | -65 | 5 | 25 |
| $`H0`$: $`50X_B`$ | -29 | 59 | -11 | -19 |

Thus

**Equation (1).**

```math
 X_A=\frac25Y+\frac35IY-\frac3{10}I,\qquad
 X_B=-\frac25Z-\frac{12}{25}JZ+\frac3{10}J,\qquad
 \widehat T=\overline X_A+\overline X_B-\frac2{25}.
```

Collect $`n=2{,}500{,}000`$ trials per arm. Let

**Equation (2).**

```math
 M=\mathbb EY,\quad C=\mathbb E(IY),\quad
 L=\mathbb EZ,\quad D=\mathbb E(JZ),\quad
 A=L+\frac35D,\quad Q=C-D.
```

Use their empirical counterparts for the following gates. Reject the
ordinary null only if every empirical gate passes and
$`\widehat T\gt .0021`$.

| Quantity | Empirical gate | Population gate used only in the proof |
|---|---|---|
| $`M`$ | $`[.211,.226]`$ | $`[.207,.230]`$ |
| $`C`$ | $`[.457,.490]`$ | $`[.453,.494]`$ |
| $`L`$ | $`[.118,.132]`$ | $`[.114,.136]`$ |
| $`D`$ | $`[.475,.509]`$ | $`[.471,.513]`$ |
| $`A`$ | $`[.405,.435]`$ | $`[.401,.439]`$ |
| $`Q`$ | $`[-.025,-.012]`$ | $`[-.031,-.006]`$ |

The allocation is **5,000,000 trials and 10,000,000 binary readouts**.
The nominal active evolution takes $`5/2`$ attempt-time units per trial.
Preparation time and acquisition of the physical promises are not
priced.

## 2. Separate target and null error budgets

For every nominal-field, nominal-time target in the one-percent
prefactor family, the
[direct kinetic certificate](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md)
gives the following
recorded-moment enclosures, uniformly over both target detector errors:

**Equation (3).**

```math
 \begin{split}
 .21465&\le M\le.22225,& .46075&\le C\le.48602,\\
 .12167&\le L\le.12783,& .47862&\le D\le.50460.
 \end{split}
```

It also certifies the score bound $`T\gt .00367`$ and the latent correlation
difference $`-.019608\le c-d\le-.017576`$. Since the detector contrast
product lies in $`[.9604,1]`$,

**Equation (4).**

```math
 -.019608\le Q\le-.017576\cdot.9604=-.0168799904.
```

Unlike a displacement from one fixed ideal heat-bath law, (3)--(4)
and the score floor cover the kinetic family directly. Only the
additional physical execution errors are charged by TV. With target
preparation, field, timing and initial-instrument allowances each
$`10^{-5}`$, their joint-table displacement is bounded by

**Equation (5).**

```math
 b_T=.000078025101\lt  B:=.000079.
```

This includes comparison to the nominal low-field preparation and
holds for the full initial--final joint law. It uses the same actual
edge multipliers when replacing an actual plateau field by its nominal
value; no field smoothness of unknown multipliers is assumed. Each
target's detector channel contracts the bound.

Ordinary rivals already permit arbitrary reversible kinetics. Their
execution budget remains $`b_R=.00002`$, from preparation and the
initial instrument. The additional observed-law prediction allowance
$`e=.0002`$ therefore gives

**Equation (6).**

```math
 E_R=b_R+e=.00022.
```

This allowance enlarges the ordinary null alone. It is not charged
again to the target.

The exact score widths are $`w_A=2`$, $`w_B=44/25`$, with sum $`94/25`$.
Transferring the entire score by (5), including its initial-bit terms,
gives the physical target floor

**Equation (7).**

```math
 \mathbb E\widehat T\gt .00367-\frac{94}{25}B
 =.00337296=:R_T.
```

## 3. Uniform null ceiling

The [frozen weaker-field proof](FAMILIAR_SWITCH_WEAK_FIELD_SCORE_TEST.md)
establishes the local stationary ordinary condition

**Equation (8).**

```math
 R\lt .00007,\qquad
 R=\frac35(C-D-L+MD)+ML,
```

on the box

**Equation (9).**

```math
 [.20,.24]\times[.45,.50]\times[.11,.14]\times[.46,.52],
 \qquad -.04\le Q\le-.001.
```

It holds for the full unknown-detector ordinary class above. At any
stationary reference, common initial marginals cancel the two opposite
initial-bit terms, and direct expansion gives

**Equation (10).**

```math
 R=T+\left(M-\frac15\right)\left(A-\frac25\right).
```

If an actual approximate null lies inside every population gate, its
stationary reference is within $`2E_R`$ in each scalar moment, $`3.2E_R`$
in $`A`$, and $`4E_R`$ in $`Q`$. Enlarging the population gates by those
amounts keeps them in (9). The enlarged lower endpoints are
$`M\ge.20656\gt 1/5`$ and $`A\ge.400296\gt 2/5`$, so the remainder in
(10) is positive. Its stationary score is therefore below $`.00007`$.
Transfer the whole score to obtain

**Equation (11).**

```math
 \mathbb E\widehat T\lt .00007+\frac{94}{25}E_R
 =.0008972=:R_N.
```

An approximate null need not retain equal initial marginals. Equality
is used only for the stationary reference; whole-score transfer makes
(11) valid for all laws in the stated TV enlargement.

## 4. Deterministic variance ceilings

For $`X=aY+bIY+gI`$, with $`m=\mathbb EY`$, $`c=\mathbb E(IY)`$ and
$`i=\mathbb EI`$, its exact variance is

**Equation (12).**

```math
 V(a,b,g;m,c,i)=a^2+b^2+g^2+2ab i+2ag c+2bg m
 -(am+bc+gi)^2.
```

The two arms use $`(a,b,g)=(2/5,3/5,-3/10)`$ and
$`(-2/5,-12/25,3/10)`$ respectively. For an actual null inside the
population gates,

**Equation (13).**

```math
 |\mathbb EI|,|\mathbb EJ|\le10^{-4}+2E_R=.00054.
```

On those boxes the first score mean is positive and the second
negative. Differentiating (12) shows that each variance decreases
with its two moments and increases with the initial mean. Substitution
of the lower population endpoints and $`i=.00054`$ consequently bounds
the null variances by

**Equation (14).**

```math
 \frac{75348226039}{250000000000}\lt .302,\qquad
 \frac{65253333919}{250000000000}\lt .262.
```

The nominal-field kinetic targets have zero initial means, since the
low-field Gibbs law remains balanced and the detector is symmetric.
The same derivative signs hold on (3). Substituting the lower
endpoints of (3) and $`i=0`$ bounds their nominal variances. A TV
displacement $`B`$ increases the variance of a score of width $`w`$ by
at most $`w^2B`$: center the new second moment at the old mean, use
the bounded expectation difference, then minimize over centering.
Adding $`4B`$ and $`(44/25)^2B`$ gives respectively

**Equation (15).**

```math
 .2911934639\lt .292,\qquad .25322527228864\lt .254.
```

Use the following looser ceilings to keep the concentration check
simple:

| Law | $`\mathrm{Var}(X_A)`$ upper | $`\mathrm{Var}(X_B)`$ upper |
|---|---:|---:|
| Actual null inside every population gate | .31 | .27 |
| Every allowed physical target | .30 | .27 |

These are analytic population bounds, not estimated sample variances.

## 5. Size and power

For independent arm averages define

**Equation (16).**

```math
 V_N=\frac{.58}{n},\quad V_T=\frac{.57}{n},\quad W=\frac2n,
 \qquad
 \mathcal B(V,W,x)=\sqrt{2Vx}+\frac{Wx}{3}.
```

The bounded-variable Bernstein argument in the
[inherited score proof](FAMILIAR_SWITCH_UNCALIBRATED_SCORE_TEST.md)
gives a one-sided tail probability at most $`e^{-x}`$ at this radius.
Squared rational inequalities certify

**Equation (17).**

```math
 R_N+\mathcal B(V_N,W,3)\lt .002078\lt .0021
 \lt .002154\lt R_T-\mathcal B(V_T,W,13/4).
```

For example, after subtracting the linear Bernstein terms, the two
positive squared margins are $`1/2500000000`$ and
$`9851449/5625000000000000`$.

For a fixed null inside all population gates, (17) gives size at most
$`e^{-3}\lt .05`$. If it lies outside a population gate, passing that
empirical gate requires crossing a gap $`.004`$ for a scalar moment or
$`A`$, or $`.006`$ for $`Q`$. Hoeffding's inequality gives one of

**Equation (18).**

```math
 e^{-n(.004)^2/2},\qquad
 e^{-n(.004)^2/(2\cdot1.6^2)},\qquad
 e^{-n(.006)^2/4},
```

each below $`.05`$. The middle bound uses the range $`[-1.6,1.6]`$ of
$`Z+(3/5)JZ`$; the last uses two independent arm averages. Selecting
one violated population gate for a fixed null requires no union over
the gates. The inside and outside cases are alternatives, so their
size bounds are combined by a maximum.

For the target, (3)--(5) imply safe distances from the empirical gate
edges of

**Equation (19).**

```math
 d_S=.00346\quad\text{for each of }M,C,L,D,\qquad
 d_A=.00358,\qquad d_Q=.00456.
```

For instance, the nominal lower $`A`$ endpoint is
$`.12167+.6(.47862)=.408842`$; its distance from $`.405`$, less
$`3.2B`$, is $`.0035892\gt d_A`$. The smallest scalar distance after
subtracting $`2B`$ is $`.003462\gt d_S`$. The upper $`Q`$ endpoint in
(4), after allowing $`4B`$, remains $`.0045639904\gt d_Q`$ below
the upper empirical gate.

A union bound gives total gate-failure probability

**Equation (20).**

```math
 \begin{split}
 G&\le8e^{-nd_S^2/2}
       +2e^{-nd_A^2/(2\cdot1.6^2)}
       +2e^{-nd_Q^2/4}\\
  &=8e^{-29929/2000}+2e^{-32041/5120}+2e^{-3249/250}\lt .004.
 \end{split}
```

This last inequality is certified using rational bounds
$`e^{-x}\le[\sum_{k=0}^{40}x^k/k!]^{-1}`$ for $`x\gt 0`$. Together
with (17), the miss probability is less than
$`e^{-13/4}+.004\lt .044\lt .05`$. This proves the stated size and power
uniformly, without a normal approximation or detector inversion.

The conclusion concerns the two joint snapshot laws and the stated
ordinary model class. It neither establishes full path-law equivalence
nor certifies preparation, readout, rate or stationary promises from
these records alone.
