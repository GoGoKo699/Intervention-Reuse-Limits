# Perfect fixed-field calibration can still require another state after one switch

[Repository](../README.md) · [Physical model](FAMILIAR_SWITCH_STRUCTURE.md) · [Earlier precision frontier](FAMILIAR_CHAIN_PRECISION_FRONTIER.md)

Two coupled heat-bath switches give a small, explicit distinction between
calibration and reuse. One reversible three-state predictor reproduces
every initial/final sign law at either registered constant field, for every
duration, using one common preparation and the prescribed Gibbs force.
Nevertheless, every such three-state predictor must make an error after
one field switch. The smallest possible error is known exactly and is
attained by a model with rational rates.

This is a sharper statement than exhibiting a badly chosen predictor.
Four fixed-field endpoint experiments already force the same lower bound.
The physical four-state process predicts the switched experiment exactly;
an existing three-state predictor also does so when stationary circulation
is allowed. All persistent states are counted.

At the operating point below, the resulting state counts are:

| Endpoint prediction task | General states | Ordinary reversible states |
| --- | ---: | ---: |
| Every duration at both constant fields, exactly | $`3`$ | $`3`$ |
| Five specified settings, through TV error $`1/20000`$ | $`3`$ | $`4`$ |
| Every finite protocol at the two fields, exactly | $`3`$ | $`4`$ |

The $`0.245\%`$ sharp switched error requires exact calibration. The
$`1/20000=50`$ ppm guarantee is a separate uniform approximation theorem
that permits errors in all five settings.

## 1. Physical experiment and comparison class

Use the [established two-switch heat-bath model](FAMILIAR_SWITCH_STRUCTURE.md)
with energy, in temperature units,

```math
E_h(S,Z)=-JSZ-hS,
\qquad S,Z\in\{-1,+1\},
```

and equal unit attempt rates. The configurations are time-even, so ordinary
detailed balance uses identity time reversal. The control acts only on
the observed sign $`S`$. Prepare zero-field equilibrium once and measure
the initial and final signs. No intermediate observation is needed.

Write $`t=\tanh J`$, $`m=\tanh h`$, and

```math
A_m=\frac{m(1-t^2)}{1-t^2m^2},\qquad
B_m=\frac{t(1-m^2)}{1-t^2m^2},\qquad
\kappa_m=\sqrt{tB_m}.
```

The physical mean equations close exactly:

```math
Q_mS=A_m-S+B_mZ,\qquad Q_mZ=tS-Z.
```

The concrete operating point is

```math
t=\frac13,\quad m_H=\frac79,
\qquad J=\frac12\log2,\quad H=3J.
```

A letter $`L`$ means one unit of time at zero field and $`H`$ means one unit
at field $`H`$. Protocol order is chronological: $`HL`$ applies the high
field first. The five settings are

```math
L,\quad L^2,\quad H,\quad H^2,\quad HL.
```

A rival has fixed states, deterministic readout $`S`$, common initial law
$`\rho_0`$, and one stochastic tick kernel $`K_j`$ per field. Ordinary rivals
are reversible under
$`\rho_j\propto\rho_0(1+m_jS)`$. The lower arguments allow initial sign
imbalance, zero unused masses and arbitrary reversible stochastic kernels;
no rate cap or continuous-time embedding is required. Exact calibration
forces the observed initial sign law to be balanced. The explicit upper
models are continuous-time Markov chains with positive stationary masses.

At nonzero field these are relaxation experiments from zero-field
equilibrium. They are not all stationary experiments at the applied field.
The physical model and force convention retain the
[existing source and assumption audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md).

## 2. Three reversible states pass every constant-field test

Use states with readout $`(+,+,-)`$ and one preparation

```math
\rho_0=(1/4,1/4,1/2),\qquad
\rho_H=(4/9,4/9,1/9).
```

The two generators are

```math
Q_L=\begin{pmatrix}
-5/9&1/3&2/9\\
1/3&-1&2/3\\
1/9&1/3&-4/9
\end{pmatrix},\qquad
Q_H=\begin{pmatrix}
-43/85&8/17&3/85\\
8/17&-11/17&3/17\\
12/85&12/17&-72/85
\end{pmatrix}.
```

Every off-diagonal rate is positive, rows sum to zero, exit rates are at
most one, and detailed balance holds under the displayed Gibbs laws.
Introduce the auxiliary functions

```math
Z_L=(5/3,-1,-1/3),\qquad Z_H=(4/3,-2/3,-1/3).
```

Direct substitution gives
$`Q_jS=A_j-S+B_jZ_j`$ and $`Q_jZ_j=tS-Z_j`$.
Both have initial conditional means
$`\mathbb E_{\rho_0}[Z_j\mid S=s]=ts`$.
Thus the two conditional final sign means obey exactly the physical
equations from exactly the physical initial means. Every constant-field
endpoint-pair law agrees for every nonnegative duration at either field.
The same statement holds from each model's corresponding field equilibrium,
because the Gibbs tilt leaves the conditional law given $`S`$ unchanged.

Only $`S`$ is measured. The field-dependent $`Z_j`$ are functions used in the
proof; neither the readout nor the state labels change at a switch. Their
difference is precisely the obstacle to reusing the reduced dynamics:

```math
Z_L-tS=\frac43(Z_H-tS).
```

The construction belongs to a simple family. For $`0\lt t\lt 1`$ and $`0\le m\lt 1`$,
put $`r_m=\sqrt{2(1-t^2)/(1+m)}`$, $`Z_m=(t+r_m,t-r_m,-t)`$ and
$`d_m=(1-m)(1-tB_m)/2`$. With the same readout and preparation, take

```math
\begin{aligned}
q_{02}&=d_m-B_mr_m/2,&q_{12}&=d_m+B_mr_m/2,\\
q_{01}=q_{10}&=\frac{1+m+(3-m)tB_m}{4},\\
q_{20}&=\frac{1+m}{2(1-m)}q_{02},&
q_{21}&=\frac{1+m}{2(1-m)}q_{12}.
\end{aligned}
```

Diagonals are minus row sums. These are nonnegative exactly when
$`t^2(3+2m)\le1`$; strict inequality makes every off-diagonal rate positive.
The identity $`B_mr_m^2=4td_m`$ verifies the two closure equations.
At $`t=1/3`$, the condition holds for every $`0\le m\lt 1`$. Thus even exact
constant-field calibration over this entire nonnegative field range is
possible with three reversible states. The switching lower below still
uses only the two registered fields.

## 3. Four calibration settings force a sharp switching error

Let $`U=Z-tS`$ and $`\gamma=1-t^2`$. On the physical target,

```math
K_jS=a_j+b_jS+c_jU,
\quad b_j=e^{-1}\bigl(\cosh\kappa_j+\kappa_j\sinh\kappa_j\bigr),
\quad a_j=m_j(1-b_j),
\quad c_j=\frac{B_j}{\kappa_j}e^{-1}\sinh\kappa_j\gt 0.
```

The physical $`U`$ has zero conditional mean given either initial sign,
and $`\mathbb E_{\pi_j}U^2=\gamma`$ at both fields.

Suppose an ordinary rival with at most three supported states matches
only the four pair laws $`L,L^2,H,H^2`$ exactly. Define its functions

```math
U_j=\frac{K_jS-a_j-b_jS}{c_j}.
```

The first-lag means and correlations force
$`\mathbb E_{\rho_0}U_j=\mathbb E_{\rho_0}SU_j=0`$.
Reversibility gives

```math
\langle K_jS,K_jS\rangle_{\omega_j}
=\langle S,K_j^2S\rangle_{\omega_j},
\qquad \omega_j=\rho_0(1+m_jS).
```

Hence the second-lag data force
$`\|U_j\|_{\omega_j}^2=\gamma`$ and
$`\langle1,U_j\rangle_{\omega_j} =\langle S,U_j\rangle_{\omega_j}=0`$.
No assumption about matching longer pure words is used.

Both sign sectors have positive mass. A nonzero function with zero mean
in each sector needs at least three supported states. With exactly three,
one sector is a singleton and the other has two states. Each $`U_j`$ is zero
on the singleton, and the centered functions on the other sector form
one line. If $`s`$ is the sign of the two-state sector, the two norms force

```math
U_L=\eta\sqrt{1+sm_H}\,U_H,\qquad \eta\in\{-1,+1\}.
```

This statement allows unequal hidden masses and unrelated field kinetics.
It follows from the prescribed change of equilibrium weights, not a
chosen hidden architecture.

Stationarity and detailed balance at the high field give

```math
\mathbb E_{\rho_0}K_HU_H=-m_H\mathbb E_{\rho_0}SK_HU_H,
\qquad
\mathbb E_{\rho_0}SK_HU_H=\frac{c_H\gamma}{1-m_H^2}.
```

Expand $`K_LS`$ and apply $`K_H`$. Writing $`M`$ for the final mean and $`C`$ for
the initial/final correlation, the switched discrepancies are

```math
\Delta C=\frac{\gamma c_Lc_H}{1-m_H^2}
       \bigl(\eta\sqrt{1+sm_H}-1\bigr),
\qquad \Delta M=-m_H\Delta C.
```

For balanced initial signs, pair-law TV equals
$`\max(|\Delta M|,|\Delta C|)/2`$. Among the four possible multipliers,
the smallest distance from one is $`\sqrt{1+m_H}-1`$. Therefore

```math
\boxed{\mathrm{TV}(HL)\ge
\frac{\gamma c_Lc_H}{2(1-m_H^2)}
\bigl(\sqrt{1+m_H}-1\bigr).}
```

The model in Section 2 attains equality. At the rational operating point,

```math
\boxed{\min\mathrm{TV}(HL)=
\frac9{4\sqrt{85}}e^{-2}
\sinh\!\left(\frac2{\sqrt{85}}\right)
\sinh\!\left(\frac13\right)
=0.002451868563\ldots.}
```

This is about $`0.245\%`$ in total variation. It is the sharp switched error
**subject to exact agreement on the four calibration settings**. It is
not the best uniform error when a rival may trade calibration error for
switched accuracy. Arbitrary reversible tick kernels are covered by the
lower; the matching upper is a reversible CTMC. If calibration at every
duration is required, the same construction attains the same minimum.

More generally, with a high-field dwell $`u\gt 0`$ followed by a zero-field
dwell $`v\gt 0`$, exact constant-field calibration gives the sharp minimum

```math
\frac9{4\sqrt{85}}e^{-(u+v)}
\sinh\!\left(\frac{2u}{\sqrt{85}}\right)
\sinh\!\left(\frac v3\right).
```

It is positive for all positive dwells and vanishes for zero dwell or
after complete relaxation. This is a transient switching effect.

## 4. An observable identity for imperfect calibration

The exact-calibration result has a direct finite-error counterpart.
For an ordinary rival with positive mass in both visible-sign sectors,
define $`g_j=K_jS`$ and the quantities available from the four pure pair laws:

```math
p_s=\Pr(S_0=s),\qquad
z_{j,s}=\mathbb E[\mathbf1_{S_0=s}S_1]_j,
\qquad
V_j=C_{j^2}+m_jM_{j^2}
-\sum_{s=\pm1}(1+m_js)\frac{z_{j,s}^2}{p_s}.
```

Here $`V_j\ge0`$ is the squared norm of $`g_j`$ after subtracting its
conditional mean in each sign sector, weighted by $`\omega_j`$.
For at most three supported states, those residuals occupy at most one
one-dimensional sector. Consequently, for some
$`s\in\{-1,+1\}`$ and $`\eta\in\{-1,+1\}`$,

```math
\boxed{C_{HL}+m_HM_{HL}
=\sum_{r=\pm1}(1+m_Hr)\frac{z_{H,r}z_{L,r}}{p_r}
 +\eta\sqrt{(1+sm_H)V_HV_L}.}
```

If a residual variance vanishes the square-root term is zero. This
identity remains valid for imbalanced initial signs and unused zero-mass
states; it imposes no CTMC or rate assumption. It also supplies a
calibration-versus-switching tradeoff using only observed quantities.
Both sign masses are positive automatically in the error neighborhood
used below, since $`\delta\lt 1/2`$.

Per-word TV error at most $`\delta`$ gives
$`p_s\in[1/2-\delta,1/2+\delta]`$,
$`|z_{j,s}-z_{j,s}^*|\le2\delta`$, and

```math
|(C_w+m_jM_w)-(C_w^*+m_jM_w^*)|
\le2(1+m_j)\delta.
```

Positive denominators and nonnegative variances allow exact rational
interval evaluation of all four possible branches. The
[bound verifier](../scripts/verify_familiar_switch_frozen_bound.py)
certifies their separation at $`\delta=1/20000`$. Even the closest branch
remains separated from the allowed switched-data interval by more than
$`0.0004717`$ in the weighted moment $`C_{HL}+m_HM_{HL}`$. Thus **no ordinary
rival with at most three states fits all five pair laws within 50 ppm**.
This certificate permits calibration errors and imposes no positive mass
floor beyond what the observed initial marginal implies.

For completeness, at most two general states are also excluded at this
tolerance using only $`L,L^2`$. With deterministic binary readout and both
signs present, two hidden states are fully observed. Their pair tables
must satisfy

```math
P_{L^2}(s,t)=\sum_{r=\pm1}\frac{P_L(s,r)P_L(r,t)}{p_r}.
```

Exact interval propagation from the allowed $`P_L,p`$ boxes leaves its
$`(+,+)`$ prediction more than $`0.00328`$ below the allowed target interval.
This argument does not assume reversibility or stationary preparation.
The general three-state upper below and physical four-state reversible
upper therefore give the exact state counts in the opening table for
every $`0\le\delta\le1/20000`$ on this same five-setting task.

## 5. The general three-state model keeps one common hidden coordinate

The existing [general construction](FAMILIAR_SWITCH_STRUCTURE.md) uses

```math
S=(-1,1,1),\quad Z=(-1/3,-2/3,5/3),\quad
\rho_0=(1/2,2/7,3/14).
```

At the present fields its generators are

```math
Q_L=\begin{pmatrix}
-4/9&8/21&4/63\\
11/18&-20/21&43/126\\
2/9&8/21&-38/63
\end{pmatrix},\qquad
Q_H=\begin{pmatrix}
-72/85&432/595&72/595\\
3/17&-69/119&48/119\\
1/85&334/595&-341/595
\end{pmatrix}.
```

They obey the same physical closure with the **same** function $`Z`$ at
both fields. Their initial conditional means agree with the target,
and their stationary laws have the prescribed Gibbs tilt. Thus endpoint
pair laws agree under every finite protocol using these fields and
arbitrary nonnegative durations. The inherited construction extends over
all nonnegative fields. Stationary circulation prevents ordinary detailed
balance: the $`01`$ flux differences are $`1/63`$ and $`-16/1785`$ respectively.
The four-state physical target supplies the reversible upper.

The [construction verifier](../scripts/verify_familiar_switch_frozen_equivalence.py)
checks both rational three-state tables and the physical four-state
generator directly, including closure, preparation, positivity and
stationarity. Rational exponential enclosures independently compare
switched pair laws and enclose the attained sharp error in
$`[0.0024518685633936,0.0024518685633937]`$.
The [construction report](../reports/familiar_switch_frozen_equivalence.json)
and [bound report](../reports/familiar_switch_frozen_bound.json)
bind this proof and their inherited sources. Numerical fitting, simulation
and floating-point acceptance decisions are unnecessary.

## 6. Established mechanism and additional content

Constant-control equivalence without switching equivalence is established
in control theory. Alkhoury, Petreczky and Mercère,
[*Comparing global input-output behavior of frozen-equivalent LPV
state-space models*](https://arxiv.org/pdf/1703.03679), Definition 6,
Remark 2, equations (8), (12) and Theorem 1, describe and bound the mismatch
caused by control-dependent coordinate transformations. Bencherki,
Türkay and Akçay, [*Basis transform in linear switched system models from
input-output data*](https://arxiv.org/pdf/2106.10888), equation (4) and
Sections 2–3, study how to align individually identified modes.

There is also a direct physical precedent for coarse-grained response:
Müller, Basu, Sollich and Krüger,
[*Coarse-grained second-order response theory*](https://arxiv.org/abs/2005.05169),
Sections II–IV and equations (22)–(32), treat time-dependent perturbations
of an observed coarse variable, including a four-state Markov example.
Their response reconstruction uses step protocols with changes before or
inside the observation interval, beyond constant-field evolution from the
one preparation used here. Basu, Helden and Krüger,
[*Extrapolation to Nonequilibrium from Coarse-Grained Response Theory*](https://arxiv.org/abs/1707.00932),
equations (5)–(10), derive coarse-grained second-order response for a
constant perturbation. These are response-reconstruction results, not
minima over alternative finite Markov realizations.

The additional result here is the constrained stochastic realization:
positive Markov rates, one preparation, deterministic binary readout and
one prescribed Gibbs family. These constraints force the four possible
hidden-coordinate multipliers, hence an **attained sharp lower bound**
from four calibration settings and one switched experiment. A wrong
switching prediction is unavoidable throughout the calibrated three-state
ordinary class. The same endpoint task admits a general three-state
predictor and a reversible four-state predictor.

The generic coordinate-mismatch explanation is not claimed as new. The
focused comparison does not establish exhaustive priority. The sharp
calibrated gap, a uniform finite-error radius, and statistical detection
cost are different quantities. Practical acquisition cost, robust device
realization and broad publication significance remain open. No path-law,
hardware-bit or dissipation-saving conclusion is asserted. Manuscript
drafting remains deferred.
