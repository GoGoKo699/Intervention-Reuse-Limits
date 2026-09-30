# From fast-variable averaging to reusable kinetic models

[Overview](README.md) · [Documentation map](docs/README.md) · [Scientific contract](docs/SCIENTIFIC_CASE.md)

An unobserved variable may relax so quickly that replacing it by its conditional equilibrium gives an accurate small model. This project asks what happens when that same model must predict several control protocols, and when the required accuracy becomes finer. For the target studied here, control timing and precision determine whether two, three or four Markov states are needed.

The selected teaching anchor is Bo and Celani's [*Multiple-scale stochastic processes: decimation, averaging and beyond*](https://arxiv.org/pdf/1612.04999), §§1, 2–2.2 and 2.3.2. Their fast-block construction averages slow transition rates against conditional fast stationary laws, as in Eq. (29). Their Eq. (4) uses column probabilities. We transpose that convention below.

Everything from the specific two-switch target onward is this repository's explanatory bridge to its existing proofs. The review does not establish the project's controlled state-count theorem. The [background guide](docs/MANUSCRIPT_BACKGROUND.md) supplies the broader attribution and closest-result comparisons.

## 1. Probabilities, generators and observations

A finite continuous-time Markov chain describes probabilities flowing between states. We use a row probability vector $`p`$ and generator $`Q`$:

```math
Q_{ij}\ge 0\quad(i\ne j),\qquad
Q\mathbf 1=0,\qquad
\frac{dp}{d\theta}=pQ.
```

The off-diagonal entry is the rate from state $`i`$ to state $`j`$. The diagonal is minus the total exit rate. Over a hold of duration $`a`$, the transition matrix is $`e^{aQ}`$. For a column observable $`f`$, its mean evolves according to

```math
\frac{d}{d\theta}\mathbb E[f(X_\theta)]
=\mathbb E[(Qf)(X_\theta)].
```

The translation from the review is $`Q=L^{\mathsf T}`$. Switching fields changes the generator; an ideal switch leaves the current state unchanged. Consequently, a sequence of holds is represented by the chronological product of their propagators, with the first hold on the left.

A stationary law satisfies $`\pi Q=0`$. Detailed balance additionally requires $`\pi_iQ_{ij}=\pi_jQ_{ji}`$: each stationary flow is balanced by its reverse. These properties concern a held field. Changing fields drives the system.

## 2. The four-state target and its preparation

The target contains a visible sign $`S`$ and a hidden sign $`Z`$, each taking values $`-1,+1`$. Its dimensionless energy is

```math
\mathcal E(S,Z)=-JSZ-hS.
```

The field acts on the visible sign. The [physical derivation](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md) identifies this with a specified equilibrium sequential-tunneling model of two coupled charge occupations. These labels are time-even configurations, not literal magnetic spins.

Write $`t=\tanh J\in(0,1)`$, $`u=\tanh H\in(0,1)`$ and $`r=\Gamma_Z/\Gamma_S`$. Dimensionless time $`\theta`$ is measured in units of $`1/\Gamma_S`$. The allowed fields are $`0,H`$, and the flip rates are

```math
q_h((s,z),(-s,z))=\frac{1-s\tanh(h+Jz)}2,
\qquad
q_h((s,z),(s,-z))=\frac r2(1-tsz).
```

Each held-field generator obeys detailed balance for its Gibbs law. Every target experiment starts from the same zero-field equilibrium:

```math
\pi_0(s,z)=\frac{1+tsz}{4},\qquad
\mathbb P(S_0=s)=\frac12,\qquad
\mathbb E[Z_0\mid S_0=s]=ts.
```

Only the true initial and final signs are recorded. There is no intermediate observation, feedback or resetting during the word. This preparation and observation rule matters: predicting all trajectories or all microscopic initial states would be a stronger task.

## 3. Conditional averaging produces a two-state model

Freeze the visible sign at $`s`$ and consider only the fast hidden flips. Their stationary law is

```math
\rho(z\mid s)=\frac{1+tsz}{2}.
```

It does not depend on the applied field. This is the conditional distribution to average against; the unconditional hidden equilibrium would discard the coupling to the current visible sign.

For $`m=\tanh h`$, averaging the visible flip rate gives

```math
\overline q_h(s,-s)
=\sum_{z=\pm1}\rho(z\mid s)q_h((s,z),(-s,z))
=\frac{c_m}{2}(1-sm),
\qquad
c_m=\frac{1-t^2}{1-t^2m^2}.
```

These are valid positive two-state rates. Their stationary visible law is $`(1+ms)/2`$, exactly the target's visible Gibbs marginal. Thus the approximation already preserves the correct held-field equilibrium.

The [fast-relaxation theorem](docs/FAMILIAR_SWITCH_FAST_RELAXATION.md) proves more than convergence at one time: this same two-state model has endpoint-pair error at most $`t^2/[r(1-t^2)]`$ for every allowed word. Correct equilibrium weights, however, do not imply exact transient prediction. The missing quantity is the hidden lag.

## 4. The lag survives averaging

Condition on $`S_0=s`$ and let $`x=\mathbb E[S\mid S_0=s]`$, $`z=\mathbb E[Z\mid S_0=s]`$. Direct application of the target generator closes their equations:

```math
x'=A_m-x+B_mz,\qquad z'=r(tx-z),
\qquad
A_m=mc_m,\quad B_m=\frac{t(1-m^2)}{1-t^2m^2}.
```

Here primes denote dimensionless time derivatives. Define $`e=z-tx`$. The initial conditional equilibrium makes $`e(0)=0`$, but subsequent visible motion generates a lag:

```math
x'=-c_m(x-m)+B_me,\qquad
e'=-re-tx'.
```

The first equation separates averaged relaxation from the lag's feedback. The second says the hidden variable relaxes toward a moving target. Since $`\lvert x'\rvert\le2`$, the existing proof obtains

```math
e(\theta)=-t\int_0^\theta e^{-r(\theta-a)}x'(a)\,da,
\qquad \lvert e(\theta)\rvert\le\frac{2t}{r}.
```

This bound survives every switch: the means remain continuous, and no derivative of the field appears. It explains the uniform first-order approximation.

At a held field, adjusting the two-state relaxation rate absorbs the leading correction. Rapid switching probes whether those adjusted rates remain compatible across protocols. A hidden distribution carrying recent history cannot generally be replaced by a fresh equilibrium distribution at every change of field.

The relevant comparison is between the pulse spacing and the hidden relaxation time. Fixed positive ticks become long on the hidden clock as $`r`$ increases. Pulses of duration $`1/r`$ remain comparable to hidden relaxation. This explains why the two control menus can have different approximation orders even though both use the same two field values. The rate separation alone does not specify the prediction problem; allowed timing must be stated with it.

## 5. Coordinates are not Markov states

The closed observables $`1,S,Z`$ form a three-dimensional linear description. A three-state Markov model requires more: its three probabilities must remain nonnegative, sum to one, and evolve with nonnegative off-diagonal rates. The readout must also assign a definite sign to each state.

Geometrically, a three-state realization uses three vertices in an observable plane. Probability distributions give convex combinations of those vertices. The drift at each vertex must be expressible through nonnegative transition rates toward the others. The same triangle must work at both fields. An arbitrary change of linear coordinates need not preserve this geometry.

The [rapid-control construction, R93](docs/FAMILIAR_SWITCH_RAPID_CONTROL.md), supplies an actual reversible chain with readout $`(-1,+1,+1)`$. Its extra degree of freedom records a scaled lag. One field-independent change of mean coordinates gives a visible correction of size $`O(r^{-1})`$ multiplying a lag already of size $`O(r^{-1})`$. Hence its endpoint-pair error is $`O(r^{-2})`$, uniformly over word length and elapsed time.

This establishes sufficiency. To establish necessity, one must exclude every admissible smaller model, not merely show that a chosen partition or fitting method fails.

## 6. What a reusable rival promises

A rival has one persistent state space, one deterministic binary readout, and one fixed continuous-time generator for each field. Those generators serve all words in the chosen menu. Every preparable persistent state counts, including states with zero stationary weight. Rates are uncapped.

The rival may choose its initial distribution separately for every scheduled word. The lower bounds retain that freedom. The target's balanced preparation is not imposed on the rival.

For a word propagator $`K_w`$ and sign-indicator matrices $`D_s`$, the target pair law is

```math
P_w(s,s')=\pi_0D_sK_wD_{s'}\mathbf1.
```

An intermediate record would insert another indicator into the product, creating a different prediction requirement. Error here means total variation of the complete endpoint-pair tables:

```math
\mathrm{TV}(P,\widehat P)
=\frac12\sum_{s,s'}\lvert P(s,s')-\widehat P(s,s')\rvert.
```

The reversible class additionally requires normalized nonnegative stationary laws, detailed balance, and a shared Gibbs tilt through the readout:

```math
\widehat\pi_H(i)=
\frac{\widehat\pi_0(i)(1+v\widehat S(i))}
     {1+v\sum_j\widehat\pi_0(j)\widehat S(j)},
\qquad -1\lt v\lt1.
```

The tilt $`v`$ is unknown and need not equal the target tilt $`u`$. The general class drops detailed balance and the Gibbs premise. These are declared comparison classes, not properties inferred for arbitrary physical devices from endpoint agreement.

## 7. Three experiments reveal the missing state

The [finite-pulse theorem, R98](docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md), turns reuse into a concrete consistency check. For $`r\ge2`$, put $`n=\lceil r/2\rceil`$ and $`A=n/r`$. Compare two held calibrations with one alternating train:

```math
\mathcal W_r=\{L_A,H_A,W_r\},\qquad
W_r=(L_{1/r}H_{1/r})^n.
```

Each calibration lasts as long as the train's total residence at its field. For any rival with exactly one state per visible sign, its conditional final mean has the affine form $`a_ws+b_w`$. The slope is the product of the held-field relaxation factors. Equal residence times therefore force

```math
a_{W_r}=a_{L_A}a_{H_A}.
```

This identity holds for every pair of two-state generators. It requires no estimated rates, equilibrium assumption or optimal-fit calculation. A rival missing either visible sign already has pair error at least $`1/2`$, so it cannot supply an accurate exception.

Define the target contrast and multiplication residual by

```math
C_w=\frac{\mathbb E[S_{\mathrm{final}}\mid S_0=+1]
             -\mathbb E[S_{\mathrm{final}}\mid S_0=-1]}2,
\qquad F_r=C_{W_r}-C_{L_A}C_{H_A}.
```

Balanced target preparation makes $`C_w=\mathbb E[S_0S_{\mathrm{final}}]`$. If the rival pair error is at most $`\delta`$, its initial mean has magnitude at most $`2\delta`$. Comparing correlations then gives $`\lvert C_w-a_w\rvert\le4\delta`$, even with word-dependent preparation. Applying this at all three settings yields $`\lvert F_r\rvert\le12\delta`$.

The scalar slopes multiply even when the full affine propagators do not commute.

For the target, R98 proves

```math
F_r=\frac{e^{-\bar c}\chi}{r}+O(r^{-2}),\qquad
\bar c=\frac{c_0+c_u}{2},\qquad
\chi=\frac{(c_u-c_0)^2}{2}\tanh\frac12>0,
```

where $`c_0=1-t^2`$ and $`c_u=(1-t^2)/(1-t^2u^2)`$, using the definition of $`c_m`$ above. The positive coefficient comes from the hidden lag across alternating fields; the proof controls the initial transient and remainder. Consequently every two-state rival has error at least $`\lvert F_r\rvert/12`$. The existing three-state upper applies to these same experiments.

The train contains $`2n`$ segments, not a fixed short word. Holding $`\Gamma_Z`$ fixed gives pulse duration $`1/\Gamma_Z`$, calibration duration $`n/\Gamma_Z`$, and train duration $`2n/\Gamma_Z`$. Finite spacing within an ideal-jump model does not establish finite-ramp, detector or sampling performance.

## 8. The state budget depends on the menu and precision

Keep coupling and field fixed as $`r\to\infty`$. Let $`E_d`$ denote the infimum worst-word pair error over the stated class of at-most-$`d`$-state rivals. The infimum chooses a reusable model before taking the supremum over words.

| Control menu | Two states | Three reversible states |
| --- | --- | --- |
| All finite words, arbitrary dwells | $`\Theta(r^{-1})`$ | $`\Theta(r^{-2})`$ |
| All words, fixed positive low/high ticks | $`\Theta(r^{-2})`$ | $`\Theta(r^{-2})`$ |
| The three-setting finite menu | $`\Theta(r^{-1})`$ | $`O(r^{-2})`$ |

The two-state lower bounds also hold in the general class. Four target states give an exact reversible model. [R92](docs/FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) establishes the fixed-clock orders; R93 supplies arbitrary-dwell control. The finite menu establishes no matching three-state lower and no fourth-state necessity.

For arbitrary dwells, a tolerance between the quadratic and linear scales therefore needs exactly three states. At finer precision, the reversible constraint matters: [R94](docs/FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md) constructs an exact general three-state predictor for sufficiently large $`r`$, while reversible three-state error remains quadratic. Detailed balance forces a singleton-sign return identity that the target violates.

The reason a singleton appears is elementary: three states split between two visible signs must leave one sign with only one state. Starting from that sign fixes the hidden state of the rival. The seven-word argument in R92 combines this fact with detailed balance and the shared Gibbs rule; its quantitative violation is second order. This is a separate obstruction from the first-order two-state contrast test above. The approximate reversible chain and the exact general chain are different constructions.

Thus, at tolerance $`\epsilon(r)=r^{-p}`$, the all-duration minima are two states for $`0<p<1`$; three for $`1<p<2`$; and, for $`p>2`$, three general versus four reversible states. At $`p=1`$ and $`p=2`$, the required count depends on the constants. At fixed positive ticks, two states suffice throughout $`0<p<2`$.

These counts describe a prediction task, not the number of physical configurations or hardware bits. A nonreversible compact predictor does not demonstrate dissipation in the held-field target. The complete [scientific guide](docs/SCIENTIFIC_CASE.md) and [sanity audit](docs/FINAL_SANITY_AUDIT.md) record the frozen assumptions, proof boundaries and unresolved implementation limits.
