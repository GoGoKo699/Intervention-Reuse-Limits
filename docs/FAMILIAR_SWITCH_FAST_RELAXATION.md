# Fast hidden relaxation removes the finite-accuracy state cost

For the two-spin model, making the hidden spin sufficiently fast makes
**one ordinary reversible two-state model approximate every open-loop
endpoint-pair experiment**, uniformly over all finite durations and field
words. The physical system still has four configurations. Its required
predictive state count therefore depends on the observable task and its
accuracy, as well as on the underlying configuration count.

The mechanism is standard adiabatic elimination. The proof controls the
lag of the hidden mean behind its conditionally equilibrated value. Strasberg
and Esposito discuss this principle and the resulting effective local
detailed balance in [*Stochastic thermodynamics in the strong coupling
regime*](https://arxiv.org/abs/1703.05098), Sec. II C, Eqs. (26)–(31).
The explicit bound below is derived here for this two-spin model; it is
not a bound quoted from that source.

## Model and statement

Use dimensionless energy $`-JSZ-hS`$, with $`S,Z`$ in $`\{-1,+1\}`$,
$`t=\tanh J`$ fixed in $`(0,1)`$, and finite signed fields $`h`$. The heat-bath
flip rates are

```math
q_h((s,z),(-s,z))
   =\frac{\Gamma_S}{2}[1-s\tanh(h+Jz)],
```

```math
q_h((s,z),(s,-z))
   =\frac{\Gamma_Z}{2}(1-t s z).
```

Take time in units of $`1/\Gamma_S`$ and put $`r=\Gamma_Z/\Gamma_S\gt 0`$.
Prepare the target once at low-field equilibrium

```math
\pi_0(s,z)=\frac{1+t s z}{4}.
```

An experiment uses any predetermined finite sequence of held fields and
nonnegative durations. Field changes leave the state unchanged. Both
records are the true initial and final signs of $`S`$. There are no
intermediate observations or feedback decisions in this protocol class.

**Theorem.** There is one two-state ordinary reversible controlled CTMC,
specified below, with balanced initial sign, such that every such word
$`w`$ satisfies

```math
\boxed{\mathrm{TV}(P_w^{\mathrm{target}},P_w^{(2)})
 \le \min\!\left\{1,\frac{t^2}{r(1-t^2)}\right\}.}
```

The same model works for all words; it is not fitted separately to each
experiment. The bound is independent of the number, order, strength and
total duration of the field segments.

## A reversible two-state approximation

For each field set $`m=\tanh h`$ and define

```math
A_h=\frac{m(1-t^2)}{1-t^2m^2},\qquad
 B_h=\frac{t(1-m^2)}{1-t^2m^2},\qquad
 c_h=1-tB_h=\frac{1-t^2}{1-t^2m^2}.
```

For every signed finite field,

```math
0\le B_h\le t,\qquad 1-t^2\le c_h\le1,\qquad A_h=m c_h.
```

The approximation has sign states $`s=+1,-1`$ and dimensionless flip rates

```math
\widehat q_h(s,-s)=\frac{c_h}{2}(1-sm).
```

These rates are positive and obey ordinary detailed balance for
$`\widehat\pi_h(s)=(1+ms)/2`$. Summing the target's Gibbs weights over $`Z`$ gives
this same marginal. Thus the approximation retains exactly the target's
visible Gibbs equilibrium family, with the common balanced low-field law.
Physical rates are obtained by multiplying by $`\Gamma_S`$.

## Proof of the uniform bound

Condition on the initial sign $`S_0=s`$ and write
$`x=\mathbb E[S\mid S_0=s]`$, $`z=\mathbb E[Z\mid S_0=s]`$. The target's exact closed mean equations,
with primes denoting dimensionless time derivatives, are

```math
x'=A_h-x+B_hz,\qquad z'=r(tx-z),\qquad
 x(0)=s,\quad z(0)=ts.
```

The mean defect from conditional equilibrium is $`e=z-tx`$. It obeys

```math
e'=-re-tx',\qquad e(0)=0.
```

The visible drift is an average of $`-S+\tanh(h+JZ)`$, so $`|x'|\le2`$.
Variation of constants therefore gives, at every time,

```math
|e(\theta)|
 \le t\int_0^\theta e^{-r(\theta-v)}|x'(v)|\,dv
 \le\frac{2t}{r}.
```

No derivative of the field appears. The means remain continuous at each
field change, so this integral argument holds across every switch without
an accumulated switch-count penalty. Physically, the field acts only on
$`S`$, so the hidden conditional equilibrium mean $`tS`$ is field independent.
Changing the coupling or adding a field on $`Z`$ is outside this model.

The two-state conditional mean $`y`$, started from the same sign, satisfies
$`y'=A_h-c_h y`$, $`y(0)=s`$. Substituting $`z=tx+e`$ into the target equation
and setting $`d=x-y`$ gives

```math
d'=-c_h d+B_h e,\qquad d(0)=0.
```

Using the field-uniform bounds above,

```math
|d(\theta)|
 \le\frac{2t^2}{r}\int_0^\theta
            e^{-(1-t^2)(\theta-v)}\,dv
 \le\frac{2t^2}{r(1-t^2)}.
```

Finally, both models have initial sign probabilities $`1/2`$. A binary
conditional final law is determined by its mean. Consequently their
complete endpoint-pair distance is

```math
\mathrm{TV}(P_w^{\mathrm{target}},P_w^{(2)})
 =\frac14\sum_{s=\pm1}|x_s(\theta)-y_s(\theta)|
 \le\frac{t^2}{r(1-t^2)}.
```

TV is also at most one, completing the proof.

## Scientific consequence and scope

For any fixed $`t\lt 1`$ and desired endpoint-pair error $`\delta\gt 0`$, two ordinary
reversible states suffice uniformly over this entire control family once
$`r\ge t^2/[\delta(1-t^2)]`$. Faster hidden kinetics therefore cannot be treated
as an unconditional advantage for detecting a reversible-state cost:
it also suppresses the effect of hidden variation on endpoint responses. Exact finite-rate realization and finite-accuracy
prediction are different questions.

This is a sufficient bound, not an optimal rate requirement or a claim
about practical parameters. It is not uniform in coupling as $`t`$ tends
to one. It requires the stated target initial law; arbitrary initial
instrument disturbance is not covered. It bounds endpoint pairs, not
full observed trajectories, intermediate-record distributions or protocols
with feedback from intermediate measurements. No thermodynamic
irreversibility of the physical target is asserted: both the four-state
target and this two-state approximation are reversible at each held field.
