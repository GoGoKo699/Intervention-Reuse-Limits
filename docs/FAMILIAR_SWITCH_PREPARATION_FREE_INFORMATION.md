# The precision and acquisition cost of the preparation-free seven-word task

The seven-word state-count separation now has a close **ordinary
reversible three-state continuous-time rival**, with fixed reused rates
and one unknown Gibbs tilt. It confines the best three-state maximum
pair-law error to

```math
 \boxed{\frac3{40006}\le E_3\lt \frac{86}{10^6}.}
```

The lower endpoint is approximately **74.98875 ppm**; the upper is
**86 ppm**. Their ratio is below **1.15**. At the lower endpoint the
attained state counts remain three general versus four ordinary
reversible states; at 86 ppm both counts are three.

The same rival proves that **every test with both errors at most 5% needs
at least 109,880,323 complete pairs under a deterministic cap**, even with
adaptive word choice and early stopping at complete-pair boundaries.
Combined with the [existing serial test](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md),
the identical robust statistical task satisfies

```math
 \boxed{109{,}880{,}323\le N_{\rm opt}\le1{,}176{,}000{,}000.}
```

Thus the sufficient design is within a factor **11** of the best possible
fixed budget for this task. A separate expected-count bound permits
integrable random stopping and gives more than **87.66 million** pairs
under the ideal target. Neither bound identifies the optimal test or a
globally closest rival.

The large acquisition cost is therefore partly intrinsic to this fixed
target, menu and observation contract. It cannot all be attributed to
a conservative concentration inequality, detector allowances or reset
overhead. The [focused source audit](FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION_SOURCE_AUDIT.md)
attributes the established information-theoretic tools; the new content
is the admissible controlled realization and its certified consequences.
The [exact report](../reports/familiar_switch_preparation_free_information.json)
binds this proof, the audit and all inherited evidence.

## The experiment and the comparable acquisition problem

The existing seven-word procedure has deterministic cap

```math
 N_{\rm upper}=1{,}176{,}000{,}000
```

complete attempted pairs and errors less than `0.040389` and `0.045261`.
Its null permits one ordinary reversible model on at most three **total**
persistent states, including preparable zero-equilibrium-weight states;
fixed reused field kernels; a common unknown finite Gibbs tilt; and
arbitrary word- and history-dependent preparation. The target power class
permits each conditional true-boundary pair law to differ by at most
`5 ppm TV` from its fixed nominal law. At either endpoint, electronic
registration may disagree with the true active-boundary sign with
conditional probability at most `1 ppm`, as specified in the inherited
contract. The initial true sign is taken after the initial instrument;
the final true sign is taken before final acquisition.

For lower bounds choose the following admissible subclass:

- Under hypothesis `P`, preparation and execution are exactly nominal,
  all complete trials are independent conditional on their chosen word,
  and both endpoint labels are exact.
- Under hypothesis `Q`, use one fixed admissible ordinary at-most-three-
  state model and one fixed preparation `nu_w` for each scheduled word.
  Prepare a fresh independent state from `nu_w` each trial, run that
  word's fixed kernels, and report both true endpoint signs exactly.

The null permits these independent word-specific preparations. The ideal
target has zero execution error, and exact registration has zero error;
zero lies within both nonzero allowances. A test valid for the entire
robust serial contract must therefore distinguish this pair of ideal
subclass experiments. The lower is not weakened by omitting experimental
errors from its hard instance.

The word is selected **before current preparation and before the current
initial sign is observed**. Consequently the null's `nu_w` depends only on
information available at preparation. Conditional on the already chosen
word, its four-outcome pair law is fixed. No current-sign-dependent word
choice, aborted half-trial, intermediate observation, preparation label,
hidden-state record or complete trajectory is included. Exogenous random
coins and public metadata may be used if their law is identical under
both hypotheses. All retained information entering the test consists of
completed endpoint pairs and the scheduled words, plus such common
randomness.

For a deterministic budget define `N_opt` as the smallest cap allowing a
test with at most `N_opt` complete pairs on every history, false rejection
at most `1/20` uniformly over the prescribed null, and target miss at most
`1/20` uniformly over the stated target-execution/registration class.
Words may be selected adaptively from completed past trials; stopping is
between complete pairs. The existing fixed-cycle test is a member of
this class, so `N_opt <= N_upper`.

## A fixed rational continuous-time rival

The target is unchanged: two heat-bath spins with energy $`-JSZ-hS`$,
$`t=\tanh J=1/3`$, low field zero, high-field tilt $`m=7/9`$, equal unit
attempt rates and unit ticks. Its low-equilibrium law is
$`\rho^*(s,z)=(1+tsz)/4`$. For definiteness, the target flips have rates

```math
 q^*_h((s,z),(-s,z))=\frac{1-s(m_h+t z)/(1+m_h t z)}2,
 \qquad q^*_h((s,z),(s,-z))=\frac{1-tsz}2,
```

where $`m_L=0`$ and $`m_H=7/9`$; diagonals make each row sum zero.
These are the same frozen physical rates used by the earlier certificates.

The rival has three states with signs $`S=(-1,-1,+1)`$. Every decimal in
the following tables is an **exact terminating rational input**:

| Parameter | Value |
| --- | ---: |
| $`\pi_L(0)`$ | 0.175214276960 |
| $`\pi_L(1)`$ | 0.314270428762 |
| $`\pi_L(2)`$ | 0.510515294278 |
| Unknown high-field tilt $`u`$ | 0.768614727605 |

Set

```math
 \pi_H(i)=\frac{\pi_L(i)(1+uS_i)}{1+u\sum_j\pi_L(j)S_j}.
```

The fixed symmetric conductances are:

| Edge | Low field | High field |
| --- | ---: | ---: |
| $`(0,1)`$ | 0.050001659214 | 0.004181195769 |
| $`(0,2)`$ | 0.048179657002 | 0.024465448649 |
| $`(1,2)`$ | 0.174117179604 | 0.068650610652 |

For either field $`j`$, define

```math
 (Q_j)_{ik}=\frac{c_{j,ik}}{\pi_j(i)}\quad(i\ne k),
 \qquad (Q_j)_{ii}=-\sum_{k\ne i}(Q_j)_{ik},\qquad K_j=e^{Q_j}.
```

All stationary weights and off-diagonal rates are strictly positive.
Detailed balance is immediate from
$`\pi_j(i)(Q_j)_{ik}=c_{j,ik}=c_{j,ki}`$, and stationarity follows from
zero row sums and this identity. The kernels therefore obey the same
ordinary reversible Gibbs interface throughout every word. This is an
actual CTMC construction, with no unproved discrete-kernel embedding.
Its numerical tilt differs from the target's $`7/9`$, which is permitted
because the tested null does not assume independent numerical force
calibration.

For each word choose the preparation
$`\nu_w=(z_w/2,(1-z_w)/2,1/2)`$, using:

| Word | $`z_w`$ |
| --- | ---: |
| $`L`$ | 0.459060621761 |
| $`LL`$ | 0.525924604907 |
| $`H`$ | 0.339345722840 |
| $`LH`$ | 0.376868373461 |
| $`HL`$ | 0.487056483351 |
| $`LLH`$ | 0.420209032611 |
| $`HLL`$ | 0.569073491856 |

Every preparation has initial sign masses exactly $`1/2`$. The word is
announced first, then a fresh state is drawn from its declared law.
No preparation record or extra latent state is observed. Preparation
changes do not change either active generator or its Gibbs law.

The singleton plus row carries the small discrepancy. The two minus
states allow their conditional return to be adjusted by $`z_w`$. Exact
interpolation can match the target minus row whenever it lies strictly
between the two state-specific returns; the appendix proves this and
checks its local scope. The registered $`z_w`$ values are rounded rationals,
so the certificate retains their small residual errors in the **full
four-outcome pair laws**. It does not claim exact matching for the
rounded fixture.

A small deterministic numerical search found the fixture, followed by
rational rounding. No simulated data, optimizer convergence or global
optimality claim enters its acceptance. The verifier reconstructs the
fixed rational generators and preparations directly.

## Exact pair-law and information certificates

For chronological word $`w`$, form the target and rival products of their
respective tick kernels. In outcome order $`(++,+-,-+,--)`$, the rival law is

```math
 Q_w(a,b)=\sum_{i:S_i=a}\nu_w(i)\sum_{k:S_k=b}(K_w)_{ik}.
```

The target law $`P_w`$ uses its four-state low-equilibrium preparation.
All four probabilities on each side are strictly positive. The
certificate encloses them with rational matrix-Taylor remainders and
outward rounding, then bounds

```math
 d_w=\sum_{a,b}P_w(a,b)\log\frac{P_w(a,b)}{Q_w(a,b)},\qquad
 A_w=\sum_{a,b}\sqrt{P_w(a,b)Q_w(a,b)},\qquad h_w=1-A_w.
```

The resulting conservative common bounds are

```math
 \max_w d_w\lt \frac{3023}{10^{11}}=3.023\times10^{-8},\qquad
 \max_w h_w\lt \frac{7557}{10^{12}}=7.557\times10^{-9},
```

```math
 \max_w\mathrm{TV}(P_w,Q_w)\lt \frac{86}{10^6}.
```

These are categorical complete-pair quantities, not unweighted
conditional divergences. The numerical maximum TV is about 85.59 ppm;
the rational 86-ppm bound is the proof-bearing upper.

The verifier bounds every generator infinity norm by four and uses
Taylor degree 64. It extends the exponential-product remainder to
three factors, covering $`LLH`$ and $`HLL`$. Rational odd logarithm series
bound the KLs and binary thresholds. For an affinity lower bound and
rational $`x\gt 0`$, the square-root enclosure is obtained from

```math
 \frac{\lfloor D\sqrt{x}\rfloor}{D}
 =\frac{\mathrm{isqrt}(\lfloor D^2x\rfloor)}D\le\sqrt{x},
```

with a fixed integer precision $`D`$. All four downward-enclosed roots
are summed. No floating-point logarithm, square root or near-one
subtraction decides a reported inequality.

## The accuracy threshold is now bracketed

Let $`E_3`$ be the infimum, over all ordinary models with at most three
total persistent states in the declared unknown-tilt/arbitrary-preparation
class, of their maximum TV error on the seven complete pair laws.
The inherited population theorem excludes simultaneous conditional-return
errors at most $`\epsilon=3/20000`$. Target initial signs have mass $`1/2`$,
and the inherited conditioning lemma gives return error at most
$`\delta/(1/2-\delta)`$ from pair-TV error $`\delta`$. Solving this inequality
at equality yields

```math
 \delta_0=\frac{\epsilon}{2(1+\epsilon)}=\frac3{40006},\qquad
 \frac{\delta_0}{1/2-\delta_0}=\frac3{20000}.
```

This re-expresses the existing conditional certificate exactly; it
requires no new target fit or alteration of the frozen 70-ppm checkpoint.
It excludes every such three-state rival through $`\delta_0`$, so
$`E_3\ge\delta_0`$. The explicit CTMC gives $`E_3\lt 86`$ ppm. The ratio of
these two endpoints is

```math
 \frac{86/10^6}{3/40006}=\frac{860129}{750000}\lt 1.15.
```

An exclusion of every individual model at a closed endpoint alone does
not make the infimum strictly greater than that endpoint. The displayed
weak lower inequality is intentional.

The general two-state obstruction also survives at 86 ppm. Its target
composition discrepancy satisfies $`\Delta\gt 69/10000`$, and three relevant
conditional returns under a two-state reused low kernel obey
$`r_{LL,+}=r_{L,+}^2+(1-r_{L,+})(1-r_{L,-})`$. A conditional error bound
$`\varepsilon`$ can change this residual by at most $`4\varepsilon`$.
At $`\delta=86/10^6`$,

```math
 \varepsilon=\frac{\delta}{1/2-\delta}=\frac{43}{249957},\qquad
 \frac{69}{10000}-4\varepsilon\gt 0.
```

The inherited exact general three-state predictor and physical ordinary
four-state target attain the upper counts. At 86 ppm the new ordinary
three-state comparator supplies the smaller upper. Thus

```math
 \begin{aligned}
 D_{\rm general}(\delta)&=3,\quad D_{\rm ordinary}(\delta)=4
       &&(0\le\delta\le3/40006),\\
 D_{\rm general}(86\ {\rm ppm})&=D_{\rm ordinary}(86\ {\rm ppm})=3.
 \end{aligned}
```

No exact transition point inside this narrow interval is asserted.
These population tolerances remain separate from the target's five-ppm
sampling allowance and one-ppm endpoint registration promises.

## Expected acquisition: the complete-pair information bound

Let `T` be the stopping time, and `N_w` the number of completed trials
using word `w`. Assume almost-sure termination under both hard
hypotheses; if `E_P T` is infinite the expected-cost lower is automatic.
The same randomized arm-selection rule is used under either hypothesis.
Conditional on any completed history and chosen next word, the next
pair laws are `P_w,Q_w`. The action-selection probabilities therefore
cancel from the likelihood ratio. The stopped chain rule gives

```math
 D(P_{\rm transcript}\Vert Q_{\rm transcript})
    =\sum_w\mathbb E_P[N_w]d_w.
```

For a deterministic cap this is a finite chain rule. For integrable
stopping, finite alphabets, finitely many words and full-support pair
laws make the likelihood increments bounded, giving the same identity
by the stopped likelihood/chain-rule argument.

Let `R` denote rejection of the ordinary null. Required errors imply
`P(R)>=19/20` and `Q(R)<=1/20`. Data processing to this binary decision
and monotonicity of binary KL give

```math
 \sum_w\mathbb E_P[N_w]d_w
 \ge\mathrm{kl}(19/20,1/20)
 =\frac9{10}\log19=:\kappa.
```

Thus for `dbar_max=max_w dbar_w`,

```math
 \boxed{\mathbb E_P[T]\ge\frac\kappa{\overline d_{\max}}.}
```

A fixed total cap must satisfy the corresponding integer lower bound.
An expected random count must **not** be rounded to an integer. The
expectation is under the exact target `P`; no worst-history stopping-time
or acquisition-time lower is silently substituted for it.

The existing rational logarithm series supplies

```math
 2.64999508124979\lt \kappa\lt 2.64999508124980.
```

Using the lower endpoint and any certified upper bound on `dbar_max`
is conservative. Since all seven arm divergences can now be nonzero,
the relevant count is total acquisition, not just one switched arm.

For deterministic per-arm caps `M_w`, stopping and adaptive ordering
still give

```math
 \kappa\le\sum_w\mathbb E_P[N_w]d_w
           \le\sum_w M_w\overline d_w.
```

In particular, equal caps `M` on the seven words require

```math
 M\ge\left\lceil\frac{\kappa_{\rm lower}}
                              {\sum_w\overline d_w}\right\rceil,
 \qquad N_{\rm allocated}=7M.
```

This allocation-specific bound may improve on the max-arm bound. It is
not a lower for arbitrary allocations with the same total cap.

## Fixed acquisition caps: a stronger affinity bound

The Hellinger affinity increases under a common observation channel.
For a binary decision this is the direct Cauchy–Schwarz inequality
applied separately to rejection and non-rejection. Therefore

```math
 A(P_{\rm transcript},Q_{\rm transcript})
 \le\sqrt{P(R)Q(R)}+\sqrt{(1-P(R))(1-Q(R))}
 \le2\sqrt{\frac{19}{20}\frac1{20}}
 =\sqrt{\frac{19}{100}}.
```

The last bound is maximized at the two allowed error boundaries.

Let `a=min_w A_w`. At any completed history, the common randomized
choice of word has conditional affinity

```math
 \sum_w\psi(w\mid\text{history})A_w\ge a.
```

Consequently the full prefix affinity obeys `A_{t+1}>=a A_t`.
If the test has already stopped, pad to the deterministic cap with a
common absorbing record, whose conditional affinity is one and hence
at least `a`. Starting from affinity one, every test using at most `N`
complete pairs satisfies

```math
 A(P_{\rm transcript},Q_{\rm transcript})\ge a^N.
```

Combining the inequalities yields

```math
 \boxed{N\ge\frac{-\tfrac12\log(19/100)}{-\log a}.}
```

This proof covers randomized adaptive word choices and early stopping
under a deterministic cap. It does not assert that the transcript
affinity equals the product of observed arm affinities under adaptive
choice, and it does not replace `N` by `E_P T`.

For certified `hbar_max=max_w hbar_w`, use `a>=1-hbar_max` and

```math
 c(h):=h+\frac{h^2}{2(1-h)}\ge-\log(1-h),\qquad 0\le h\lt 1.
```

The inequality follows from the positive logarithm series, bounding
`1/k<=1/2` for every `k>=2`. Thus a purely rational sufficient
calculation is

```math
 N\ge\left\lceil\frac{C_{\rm lower}}{c(\overline h_{\max})}\right\rceil,
 \qquad C=-\tfrac12\log(19/100),
```

with the exact enclosure

```math
 0.83036560341082\lt C\lt 0.83036560341083.
```

The [information verifier](../scripts/verify_familiar_switch_preparation_free_information.py)
checks both scalar enclosures using exact rational logarithm series and
geometric tails. For nearby
laws, `h_w` is approximately `d_w/4`; this explains the expected gain
from the affinity bound, but that approximation is not used to certify
any integer count.

For optional fixed per-word caps $`M_w`$, pre-generate independent arrays
of $`M_w`$ pairs from each word under the two selected hypotheses. Any
adaptive ordering and early stopping within those caps is a common
channel from those arrays and common random coins. Hence transcript
affinity is at least $`\prod_w A_w^{M_w}`$. With certified per-word deficit
bounds $`\overline h_w`$, a necessary condition is

```math
 \sum_w M_w c(\overline h_w)\ge C_{\rm lower}.
```

The report also records this optional bound for equal per-word caps.
It does not substitute average arm information for the maximum-arm
bound when allocations are unrestricted.

## Certified counts and what they settle

With the stated KL upper, the exact scalar enclosure gives

```math
 \mathbb E_P[T]\gt
 \frac{2.64999508124979}{3023/10^{11}}
 \gt 87{,}661{,}100.934495.
```

This is an expectation under the exact nominal target, not an integer
minimum for every realized stopped experiment.

For a deterministic cap, insert $`h=7557/10^{12}`$ into the rational
$`c(h)`$ above. The exact lower ratio lies strictly between 109,880,322
and 109,880,323, so

```math
 N\ge109{,}880{,}323.
```

The ideal target and comparator used in this proof are admissible
subcases of the entire serial error contract. Therefore the same
necessary cap applies to its minimax $`N_{\rm opt}`$, while the existing
1,176,000,000-pair procedure provides its upper. Exact integer arithmetic
checks $`1{,}176{,}000{,}000\lt 11\times109{,}880{,}323`$.

All attempted complete pairs count, including observations later
discarded by quotas. Extra calibration data, continuous readout traces,
intermediate observations, selected-sign preparation controls, or
choosing a word after seeing its initial sign would change the
information available and require a new bound. Known interface and error
promises may be assumed; data used to establish them are not free extra
observations in this seven-word transcript. Pair counts do not by
themselves price reset time, calibration acquisition or laboratory
throughput, and are not a state bound on the whole apparatus.

The near-100-million necessary count shows a genuine distinguishability
obstacle at this fixed operating point. The upper can still improve by
up to the certified gap; neither the rival nor the test is proven optimal.
The finite-error frontier and acquisition bracket now quantify the
limitations of this specific task rather than leaving a billion-pair
upper without a scale comparison.

The next scientific priority is to derive a physical design principle
for increasing separation across the same familiar heat-bath family.
Use the analytic witness factorization to study its dependence on
coupling, field and dwell time, including signal versus duration. Seek
a structural improvement or a family-wide obstruction; an isolated
retuned numerical example or further minor tail-constant tuning is
insufficient. The accepted preparation, memory and observation boundaries
must remain explicit. Manuscript drafting remains deferred.

## Appendix: why the cubic is locally the complete obstruction

Relabel the singleton as state `0`, with sign `s`, and the other two
states as `1,2`, both with sign `-s`. Write the seven proposed returns as

```math
 (d,e,h,f,g,p,q)
 =(r_L,r_{LL},r_H,r_{LH},r_{HL},r_{LLH},r_{HLL}).
```

Define

```math
 \ell=1-d,\quad k=1-h,\quad R=e-d^2,\quad
 A=f-dh,\quad B=g-dh,\quad B_2=q-eh.
```

Assume `A,B>0` and the determinant identity

```math
 F=A B_2-(p-eh)B=0.
```

Then `lambda=A/B>0`, and a Gibbs tilt realizing this reciprocal factor is

```math
 u=s\frac{\lambda-1}{\lambda+1}\in(-1,1).
```

Choose two distinct numbers `v_1,v_2` in `(0,1)` and set

```math
 a_1=\frac{R-\ell v_2}{v_1-v_2},\qquad a_2=\ell-a_1,
```

```math
 b_1=\frac{B-kv_2}{v_1-v_2},\qquad b_2=k-b_1,
 \qquad w_i=\frac{v_i}{a_i}.
```

Require `a_i,b_i>0`. Define

```math
 J=(v_2-v_1)(b_1w_1-b_2w_2),\qquad
 B_{20}=\sum_{i=1}^2 b_i v_i(d+1-v_i),
```

```math
 \theta=\frac{B_2-B_{20}}{J},\qquad J\ne0.
```

For any chosen `zeta>0`, construct

```math
 K_L=\begin{pmatrix}
 d&a_1&a_2\\
 v_1&1-v_1-\theta w_1&\theta w_1\\
 v_2&\theta w_2&1-v_2-\theta w_2
 \end{pmatrix},
```

```math
 K_H=\begin{pmatrix}
 h&b_1&b_2\\
 \lambda w_1b_1&1-\lambda w_1(b_1+\zeta)&\lambda w_1\zeta\\
 \lambda w_2b_2&\lambda w_2\zeta&1-\lambda w_2(b_2+\zeta)
 \end{pmatrix}.
```

The explicit strict feasibility conditions are

```math
 0\lt d,h\lt 1,\quad a_i,b_i\gt 0,\quad 0\lt v_i\lt 1,\quad
 \theta\gt 0,\quad v_i+\theta w_i\lt 1,
```

```math
 \zeta\gt 0,\qquad \lambda w_i(b_i+\zeta)\lt 1\quad(i=1,2).
```

Under these conditions both matrices are strictly positive stochastic
kernels. Their reversible laws are

```math
 \pi_L\propto(1,1/w_1,1/w_2),\qquad
 \pi_H\propto(1,1/(\lambda w_1),1/(\lambda w_2)).
```

For signs `(s,-s,-s)` these laws have exactly the common Gibbs relation
with the displayed `u`. Detailed balance follows entry by entry, including
the hidden `1 <-> 2` exchange.

To verify the row, the first definitions give

```math
 (K_L^2)_{00}=d^2+\sum_i a_i v_i=e,
 \quad (K_HK_L)_{00}=dh+\sum_i b_i v_i=g.
```

The reversed cross return is `dh+lambda B=f`. Further,

```math
 (K_L^2)_{10}=v_1(d+1-v_1)+\theta w_1(v_2-v_1),
```

```math
 (K_L^2)_{20}=v_2(d+1-v_2)+\theta w_2(v_1-v_2).
```

Hence `(K_HK_L^2)_{00}=eh+B20+theta J=q`. Reversibility and the Gibbs
relation give `(K_L^2K_H)_{00}=eh+lambda B2=p`, where the final equality
uses `F=0`. All seven returns are therefore realized exactly.

### Local completeness and its limits

At an existing strict-interior realization, fix its values `v_1,v_2` and
its high exchange parameter `zeta`. If `v_1!=v_2` and `J!=0`, the inverse
above is a smooth rational function of the six independent row
coordinates `(d,e,h,f,g,q)` near that point. The remaining coordinate is
`p=eh+(A/B)(q-eh)`. Because `B>0`, the determinant surface is regular
there; equivalently `partial F/partial p=-B!=0`.

All strict positivity inequalities persist in some neighborhood.
Consequently **every sufficiently nearby row on `F=0` is realizable by
ordinary reversible three-state kernels with a common unknown Gibbs
tilt**. The return map has rank six at such a point. This conclusion is
provided by the explicit right inverse, not by a parameter-count argument.

If each desired opposite-sign return lies strictly between the two
doubleton endpoint responses at the base point, those inequalities also
persist locally. Word-specific preparation can then keep the entire
opposite-sign row equal to its desired value while the singleton row
moves along `F=0`.

This is not global sufficiency. For example the probability vector
`(d,e,h,f,g,p,q)=(1/2,1/10,1/2,1/4,1/4,1/20,1/20)` satisfies `F=0`,
but violates the necessary Markov inequality `(K_L^2)00 >= (K_L)00^2`.
At boundaries or `J=0`, the inverse is not asserted to work.

The local statement also holds **within reversible CTMCs** at a base
point whose two tick kernels have positive spectrum and principal
logarithms with strictly positive off-diagonal entries. The matrix
logarithm is continuous there. Nearby reversible kernels have real
positive spectrum; their logarithms have row sums zero, inherit detailed
balance, and retain positive off-diagonal rates. Thus they remain valid
unit-tick CTMC propagators. This does not say that every reversible
stochastic kernel is embeddable.

### Exact doubleton preparation lemma

For a word `w`, let

```math
 t_{w,i}=1-(K_w)_{i0},\qquad i=1,2,
```

be the doubleton return probabilities. If the desired return `r^*_{w,-s}`
lies strictly between them, the mixture

```math
 z_w=\frac{r^*_{w,-s}-t_{w,2}}{t_{w,1}-t_{w,2}}\in(0,1)
```

matches that conditional row exactly. With desired balanced initial
signs, choose the preparation

```math
 \mu_w=(1/2,z_w/2,(1-z_w)/2).
```

It is selected after the word is announced and before the current initial
sign is observed. It changes neither generator nor the common Gibbs
interface. Independent draws of these preparations form an admissible
reference subclass of the larger history-dependent null.

For target-to-rival KL, the chain rule shows that a different rival
singleton mass `q_w` would give

```math
 D(P_w^*\|Q_w)=\mathrm{kl}(1/2\|q_w)
   +\tfrac12\mathrm{kl}(r^*_{w,s}\|r_{w,s}),
```

when the opposite conditional row is matched. Thus `q_w=1/2` is exactly
optimal for this divergence, and

```math
 D(P_w^*\|Q_w)=\tfrac12\mathrm{kl}(r^*_{w,s}\|r_{w,s}).
```

Balanced preparation is not optimal for every divergence. If
`a_w=sqrt(r^* r)+sqrt((1-r^*)(1-r))` is the singleton Bernoulli affinity,
the full pair affinity is

```math
 \mathcal A(P_w^*,Q_w)
  =\frac{a_w\sqrt{q_w}+\sqrt{1-q_w}}{\sqrt2}.
```

Its maximum is `sqrt((1+a_w^2)/2)`, attained at
`q_w=a_w^2/(1+a_w^2)`. The balanced reference has affinity `(1+a_w)/2`.
The registered fixture uses its explicitly declared preparations; no
divergence-optimality assertion is needed for a valid lower bound.

### Regularity of the certified fixture

In the registered state order $`(-,-,+)`$, the singleton is index two.
Take $`v_1=(K_L)_{02}`$, $`v_2=(K_L)_{12}`$,
$`a_1=(K_L)_{20}`$, $`a_2=(K_L)_{21}`$,
$`b_1=(K_H)_{20}`$ and $`b_2=(K_H)_{21}`$.
Detailed balance gives the exact rational substitutions
$`w_1=\pi_L(2)/\pi_L(0)`$ and $`w_2=\pi_L(2)/\pi_L(1)`$.
The same interval certificate checks distinct $`v_i`$, strict opposite-row
bracketing, and

```math
 -\frac{217}{100000}\lt J\lt -\frac{216}{100000}.
```

The registered generators have strictly positive off-diagonal rates;
reversibility makes their spectra real, so their exponential kernels
have positive spectra and principal logarithms equal to those generators.
The local CTMC statement therefore applies at this comparator. It does
not prove that the nearby target itself is on the cubic surface, nor
that the found comparator minimizes any divergence or distance.

## Verification and attribution

The [verifier](../scripts/verify_familiar_switch_preparation_free_information.py)
uses fixed rational model inputs and inherited SHA-bound helpers. It
certifies generator admissibility, preparation, full pair-law intervals,
KL, affinity, TV, scalar thresholds, the approximation frontier and
local regularity. Independent internal review checks the written adaptive
likelihood, affinity recursion and realization arguments; finite checks
support their algebraic and numerical premises.

Adaptive change of measure and affinity data processing are established
methods, attributed with inspected primary locations in the
[source audit](FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION_SOURCE_AUDIT.md).
The adaptive affinity lower is proved directly here; it is not an
assertion of exact product structure under adaptive sampling. The
explicit local inverse is a limited realization statement, not a global
classification. Physical feasibility, complete priority and broader
publication significance remain separate questions.
