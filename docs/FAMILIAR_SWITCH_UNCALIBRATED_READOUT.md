# A state-cost witness without calibrated detector contrasts

The two-snapshot experiment has a simple detector-unknown witness.
One scalar inequality and four sign gates exclude every ordinary
reversible model with at most three states, even when the competing
model may choose arbitrary independent symmetric bit-error probabilities
between zero and one half. The detector must be fixed across the two
protocols. Its memoryless, symmetric, independent-bit form remains a
substantive assumption.

The qualitative witness needs no numerical detector calibration. A
prospective guarantee for a specified noisy target is different: the
numerical corollary below assumes that each target bit-error probability
is at most one percent. Rival probabilities remain unrestricted within
$`[0,1/2]`$. Without some restriction on target signal loss, no positive
uniform separation can survive a detector with zero contrast.

**Status:** the analytic derivation, statistical guarantee, and exact
numerical certificate have passed independent internal review. The
certificate supplies the finite numerical premises; the arbitrary-rival
implications are analytic. These checks are not external peer review.
No previous sampling allocation is transferred to this enlarged null
class.

[Snapshot model and instruments](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md) ·
[Exact three-state construction](FAMILIAR_SWITCH_STRUCTURE.md) ·
[Earlier calibrated statistical test](FAMILIAR_SWITCH_SNAPSHOT_SCORE_TEST.md) ·
[Exact interface verifier](../scripts/verify_switch_physical_interface.py) ·
[Certificate report](../reports/switch_physical_interface.json)

## 1. Shared protocols and unknown channels

Both protocols start from the same low-field equilibrium. Protocol
$`A`$ applies $`0,H`$ and records the initial and final readouts $`(I,Y)`$;
protocol $`B`$ applies $`H,0`$ and records $`(J,Z)`$. Define latent moments

**Equation (1).**

```math
 m=\mathbb EY,\quad c=\mathbb E(IY),\quad
 \ell=\mathbb EZ,\quad d=\mathbb E(JZ).
```

An ordinary rival has a deterministic binary kinetic-state readout,
shared field kernels reversible for their stationary laws, and, in
the nominal case,

**Equation (2).**

```math
 \pi_0S=0,\qquad \pi_H=\pi_0(1+uS),\qquad 0\lt u\lt 1.
```

There is no kinetic-rate cap and no prescribed rival graph. Reversible
stochastic kernels are allowed even if they are not continuous-time
propagators. The fixed initial instrument is ideal for now.

The two recorded bits undergo independent binary-symmetric flips,
independent of the hidden evolution. Their contrasts are
$`r_0=1-2p_0`$ and $`r_f=1-2p_f`$, with $`r_0,r_f\in[0,1]`$. They are fixed
across both protocols, but different hypotheses may use different
contrasts. There is no feedback from the noisy initial record.
The recorded moments are

**Equation (3).**

```math
 M=r_fm,\quad C=r_0r_fc,\quad
 L=r_f\ell,\quad D=r_0r_fd.
```

No independence between the initial and final true bits is assumed.
State-dependent emissions, correlated electronic flips, and detectors
that change between protocols are outside this channel model.

## 2. One scalar and four corner checks

The latent singleton-sector identity from the snapshot theorem is

**Equation (4).**

```math
 H_\sigma=u(c-d)+\sigma[(u-m)\ell-umd]=0
 \quad\text{for at least one }\sigma\in\{-1,1\}.
```

Every ordinary model with at most three states has a singleton readout
sector, which supplies its applicable sign. Multiplication, rather than
inversion of the detector, gives

**Equation (5).**

```math
 \begin{split}
 K_\sigma(r_0,r_f)
 &=r_0r_f^2H_\sigma\\
 &=r_fu(C-D)+
 \sigma[r_0r_fuL-uMD-r_0ML].
 \end{split}
```

Thus a necessary condition is $`K_-=0`$ or $`K_+=0`$ for some admissible
contrast pair. Define the observable scalar

**Equation (6).**

```math
 \boxed{R=u(C-D)+uMD-(u-M)L.}
```

Suppose the recorded moments satisfy

**Equation (7).**

```math
 0\lt M\lt u,\qquad L\gt 0,\qquad D\gt 0,\qquad C\lt D,\qquad R\gt 0.
```

For fixed observed moments, (5) is bilinear in the two contrasts.
Consequently its value on the unit square is a convex combination of
its four corner values:

| $`(r_0,r_f)`$ | $`K_-`$ | $`K_+`$ |
|---|---|---|
| $`(0,0)`$ | $`uMD`$ | $`-uMD`$ |
| $`(1,0)`$ | $`uMD+ML`$ | $`-uMD-ML`$ |
| $`(0,1)`$ | $`u(C-D)+uMD`$ | $`u(C-D)-uMD`$ |
| $`(1,1)`$ | $`R`$ | $`2u(C-D)-R`$ |

All minus corners are at least $`R\gt 0`$, and all plus corners are at most
$`-R\lt 0`$. For example,
$`u(C-D)+uMD=R+(u-M)L\gt R`$ and
$`uMD=R-u(C-D)+(u-M)L\gt R`$.
This proves the dimension witness:

> If (7) holds, no ordinary reversible model with at most three states
> and any fixed independent symmetric detector contrasts in $`[0,1]`$
> reproduces the two recorded joint laws.

There is no singular inverse at zero contrast. In fact $`D\gt 0`$ already
excludes a zero-contrast detector from matching the observations, but
the polynomial corner proof covers the entire closed square anyway.
This is a population statement; sample estimates require their own
simultaneous statistical error analysis.

## 3. A uniform target margin with at most one-percent bit errors

Use the physical target $`J=H=\log3`$, $`u_0=4/5`$, equal unit attempt
rates, and one clock tick of duration $`3/2`$ at each field. Its latent
moments are supplied by the
[frozen exact snapshot certificate](../reports/switch_snapshot_design.json).
Write target contrasts as $`a,b\in[49/50,1]`$. Equation (6) becomes

**Equation (8).**

```math
 R(a,b)=b\{au_0(c-d+bmd)-u_0\ell+bm\ell\}.
```

It is increasing in both contrasts on this square. This follows from
the positivity of

**Equation (9).**

```math
 \partial_aR=bu_0(c-d+bmd),\qquad
 \partial_bR=au_0(c-d)-u_0\ell+2ab u_0md+2bm\ell,
```

verified with the exact target-moment intervals. The minimum is therefore
at $`a=b=49/50`$: after dividing the first derivative by positive $`b`$,
its remaining factor is affine in $`b`$, while the second derivative is
multiaffine in $`(a,b)`$, so endpoint checks certify both signs. At that
minimum,

```math
 (M,C,L,D)\approx
 (0.4084213647,\ 0.3317657690,\ 0.2253509925,\ 0.3707330888)
```

and $`R\approx0.00171576132`$. In particular,
$`R\gt 343/200000=0.001715`$ uniformly over the target contrast square.

Let the distance between two pairs of recorded joint tables be the
maximum of their two total-variation distances. Distance at most $`g`$
implies that each of the four moments differs by at most $`r=2g`$,
whether or not the two initial marginals agree. On the target square
the absolute gradient mass of $`R`$ is

**Equation (10).**

```math
 u_0D+L+3u_0-(1+u_0)M\le\frac{11}{5}.
```

The exact quadratic remainder is
$`u_0\Delta M\Delta D+\Delta M\Delta L`$, with absolute bound
$`(1+u_0)r^2`$. Thus

**Equation (11).**

```math
 R_{\rm candidate}\gt
 \frac{343}{200000}-\frac{11}{5}r-\frac95r^2.
```

At $`g=3/8000`$, the right-hand side is $`0.0000639875\gt 0`$;
the other sign gates remain strict. Hence the nominal recorded-table
gap against ordinary at-most-three-state models exceeds

**Equation (12).**

```math
 \boxed{\frac3{8000}=0.000375.}
```

The general three-state predictor reproduces both latent joint laws
and may use the same detector as the target. The ordinary four-state
target supplies the other upper. Since every two-state stationary
kinetic model is ordinary, the exact kinetic-state minima are three
and four for all errors between zero and $`3/8000`$.

The weaker margin is the explicit price of allowing the rival to choose
its detector contrasts freely. Equation (12) is a sufficient lower
bound, not the optimized gap.

## 4. Biased equilibrium and an approximate force law

The exact balance assumption in (2) cannot simply be removed. To retain
a quantitative result, allow the stationary low law $`\pi`$ and the
stationary high law $`\eta`$ to satisfy

**Equation (13).**

```math
 |v|=|\pi S|\le10^{-4},\quad |u-u_0|\le10^{-4},\quad
 \mathrm{TV}\!\left(\eta,\frac{\pi(1+uS)}{1+uv}\right)
 \le\theta=10^{-5}.
```

Set $`q_\sigma=1+\sigma v`$ and $`z=1+uv`$. The latent biased polynomial is

**Equation (14).**

```math
 H_\sigma^v=q_\sigma[(1+\sigma u)\ell+uc]
 -(\ell+ud)(1+\sigma m)-v[um+\sigma(v+u-m)].
```

For the singleton sign, the
[approximate-force argument](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md)
gives

**Equation (15).**

```math
 |H_\sigma^v|
 \le\Gamma_\sigma
 :=\frac{12u q_\sigma z\theta+16z^2\theta^2}{1-\sigma u}.
```

Clearing detector factors again produces a polynomial:

**Equation (16).**

```math
 \begin{split}
 J_\sigma={}&r_0r_f^2H_\sigma^v\\
 ={}&(1+\sigma v)[(1+\sigma u)r_0r_fL+ur_fC]\\
 &-(r_0L+uD)(r_f+\sigma M)\\
 &-vr_0r_f[uM+\sigma(r_f(v+u)-M)].
 \end{split}
```

Therefore $`|J_\sigma|\le\Gamma_\sigma`$; no inverse-contrast amplification
occurs. Compare (16) with $`K_\sigma`$ evaluated at the fixed $`u_0`$.
On the observed-coordinate box

**Equation (17).**

```math
 |M|\le.42,\quad |C|\le.35,\quad |L|\le.24,\quad
 |D|\le.40,\quad |C-D|\le.06,
```

the $`u`$ derivative of $`K_\sigma`$ has absolute value at most $`0.468`$.
Expanding the remaining difference in $`v`$, its linear coefficient has
absolute value at most $`1.884201`$ for sign minus and $`1.596201`$ for sign
plus; the quadratic term is at most $`v^2`$. The inherited exact residual
bounds are $`\Gamma_-\lt 0.000054`$ and $`\Gamma_+\lt 0.000481`$.
The resulting necessary bands for at least one sign are

**Equation (18).**

```math
 \begin{split}
 |K_-|&\lt 0.468\,10^{-4}+1.884201\,10^{-4}
                  +10^{-8}+0.000054\lt 0.0003,\\
 |K_+|&\lt 0.468\,10^{-4}+1.596201\,10^{-4}
                  +10^{-8}+0.000481\lt 0.001.
 \end{split}
```

All bounds hold for every $`r_0,r_f\in[0,1]`$.
For clarity, the minus linear coefficient is bounded by
$`(1-u)|L|+u|C|+(1+u)|M|+u`$; the plus bound uses
$`(1+u)|L|+u|C|+(1-u)|M|+u`$ throughout (13).

Now take a candidate within joint-TV distance
$`g_0=31/100000`$ of any nominal target in the contrast square.
Its moment radius is $`r=0.00062`$. The exact bounds verify (17), the
sign gates, $`C-D\lt -0.03`$, and $`MD\gt 0.06`$. Equation (11) gives

**Equation (19).**

```math
 R_{\rm candidate}\gt 0.00035030808\gt \frac7{20000}.
```

The minus corners therefore all exceed $`0.00035`$. The plus corners
all lie below $`-0.048`$: use $`u_0MD\gt 0.048`$ at the first three corners
and $`2u_0(C-D)-R\lt -0.048`$ at the last. Convex combination extends
both conclusions to the full contrast square. Neither necessary
branch in (18) can hold. The stationary robust recorded-table
separation thus exceeds $`31/100000`$, without a detector-contrast
restriction on the rival.

## 5. Preparation, controls and disturbance

Use the same fixed-instrument assumptions as the snapshot theorem:
initial readout followed by hidden-state disturbance of joint-TV
effect at most $`\xi`$, then independent memoryless electronic flips.
The disturbance and preparation laws are shared across protocols.
For the target take preparation, field, tick and initial-disturbance
allowances all equal to $`10^{-5}`$. Its true-record displacement from
the nominal stationary target is at most

**Equation (20).**

```math
 b_T=10^{-5}+(2+10^{-5})10^{-5}+4\,10^{-5}+10^{-5}
     =0.0000800001.
```

The rival preparation and disturbance allowances give
$`b_R=2\,10^{-5}`$. Applying each model's own fixed detector contracts
its displacement; comparing different hypotheses' channels does not
cost another error term because the stationary lower already allowed
arbitrary rival contrasts. Hence the actual recorded-table gap is
strictly greater than

**Equation (21).**

```math
 \frac{31}{100000}-b_T-b_R
 =0.0002099999\gt \boxed{\frac1{5000}}.
```

The general three-state predictor matches the actual-field, ideal
stationary target joint laws and can use the actual target detector.
Preparation and disturbance give a constructive error at most
$`2\,10^{-5}`$. This is an existence statement; its detector parameters
need not be known to the analyst applying (7). The ordinary target
provides a four-state upper, while the lower excludes all two-state
stationary models as well. Thus the kinetic-state minima are three
and four throughout

**Equation (22).**

```math
 2\,10^{-5}\le\delta_{\rm obs}\le1/5000.
```

Target bit errors are at most one percent for this numerical guarantee;
rivals may choose any errors up to one half. The channel form and its
constancy across protocols, the preparation bounds, and the stationary
force-law promise are not inferred from the four observed moments.

## 6. A conservative finite-sample test

Removing detector calibration enlarges the null class. A simple test
prices that enlargement without reusing the earlier calibrated score
allocation. Assume independent fresh-preparation trials within each arm,
with the physical allowances of Section 5 fixed before data collection.
Each trial supplies one final bit and one initial/final bit product,
both in $`\{-1,1\}`$. They may be dependent within the trial.

Use $`n=254000000`$ trials in each arm and estimate the four recorded
moments by their sample averages. For $`\varepsilon=1/5000`$, Hoeffding's
inequality and a union bound give

**Equation (23).**

```math
 \Pr\!\left(\max_j|\widehat x_j-x_j|\gt \varepsilon\right)
 \le8\exp(-n\varepsilon^2/2)
 =8\exp(-127/25)\lt 0.05.
```

The exact certificate checks the last comparison using a rational
partial sum for $`\exp(127/25)\gt 160`$; the
[concentration source audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md)
records the statistical conventions.

Form the observed-moment box centered at the four estimates with radius
$`\varepsilon+2b_R=0.00024`$. Reject the ordinary at-most-three-state null
if every point in this box satisfies the sign gates (7) and every
point also lies in the localization box (17), while every contrast pair
satisfies $`K_-\gt 0.0003`$ and $`K_+\lt -0.001`$.
This is a finite calculation: check the sign gates and both polynomials
at all sixteen moment-box vertices and all four contrast corners,
and check the affine localization inequalities at the same moment
vertices.
Each corner polynomial is multiaffine in the four moments, so these
checks imply the required inequalities throughout both boxes.

Under any admissible null, actual moments differ from its stationary
moments by at most $`2b_R`$. On the simultaneous event in (23), that
stationary point lies in the tested box. At least one necessary band
(18) holds there, so rejection is impossible. The type-I error is thus
less than $`0.05`$, uniformly over the unknown rival contrasts.

Under the allowed target, every point in the tested box differs from
one nominal target in the contrast square by at most

**Equation (24).**

```math
 2(b_T+b_R)+2\varepsilon=0.0006000002\lt 0.00062
```

on the same event. The robust stationary proof therefore guarantees
rejection, giving power greater than $`0.95`$ uniformly over the target
contrast square and the stated physical allowances.

The sufficient cost is **508 million independent paired-snapshot trials**,
or **1.016 billion binary readouts**. Preparation waiting is additional.
This test concerns the exact composite null with its stated physical
allowances; it does not add a separate model-approximation allowance.
It is deliberately conservative, with no claim of optimal allocation,
near-optimal sample complexity, or experimental feasibility. Successive
snapshots along one unreset trajectory are not independent trials.

## 7. Why balance still needs a promise or an error budget

There is an elementary biased ordinary counterexample to dropping (2).
Use three states with $`S=(-1,1,1)`$ and

**Equation (25).**

```math
 \pi_0=((1-v)/2,(1+v)/4,(1+v)/4),\qquad
 \pi_H=\pi_0(1+uS)/(1+uv),\qquad u=4/5.
```

Let each field kernel be the identity except for its $`1\leftrightarrow2`$
edge. Set the symmetric stationary edge flux to $`1/10`$ at low field
and $`1/20`$ at high field: $`E_{12}=f/\pi_1`$,
$`E_{21}=f/\pi_2`$, with the corresponding diagonal row sums.
These kernels obey ordinary detailed balance. At $`v=0`$ their moments are
$`(4/9,13/45,8/45,17/45)`$; all the sign gates except $`R\gt 0`$ are strict,
and $`R=0`$. At $`v=1/1000`$ direct rational evaluation gives

**Equation (26).**

```math
 R=\frac{1340051}{4995000000}\gt 0.
```

All other gates remain strict, even with perfect detectors. The active
two-state blocks have positive nontrivial eigenvalues, so both kernels
are continuous-time embeddable. Adding sufficiently small positive
reversible conductances to the third state in their generators
$`\log E_h`$ also makes the resulting continuous-time kernels irreducible
without destroying the strict inequalities, by continuity.
Thus the detector-unknown criterion does not remove the equilibrium
balance or preparation requirements. Section 4 retains a separation by
charging bounded departures quantitatively.

The earlier 1.2-million or 1.5-million snapshot sampling allocations
were proved for calibrated detector intervals. They do not establish
size or power for this enlarged class. A statistical test of (7) and
(18) is a separate task. Complete trajectory equivalence and laboratory
feasibility are not claimed.
