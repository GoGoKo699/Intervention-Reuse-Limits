# Reversed control sequences reveal a precision-dependent state cost

[Repository](../README.md) · [Previous certificate](FAMILIAR_CHAIN_TWO_FIELD_ACCURACY.md) · [Rank certificate](../reports/familiar_chain_cross_rank.json) · [Small models](../reports/familiar_chain_small_models.json)

Two opposite pulse orders determine a matrix for each visible sign. Its
rank lower-bounds how many hidden states a reversible predictor must place
behind that sign. This direct factorization simplifies the earlier
squared-norm witness and reduces the three-switch test to **twelve
endpoint-pair settings**.

At the same established physical operating point, exact rational
certificates now identify different minimum reversible state counts at
different precisions. The five-state construction is close to the best
possible error in its class. The relevant tolerances are still only a few
parts per million; practical significance does not follow from sharpening
their mathematical bounds.

## 1. Keep the physical model and prediction task fixed

Use the three-spin equal-attempt heat-bath chain at $`t=\tanh J=1/3`$, from
its zero-field equilibrium. The only measured coordinate is the initial
and final sign of the first spin. Set field tilts $`m_L=0`$, $`m_R=1/2`$ and
clock $`\tau=1`$. The new sufficient menu is

```math
L,L^2,R,R^2,\qquad L^aR^b,\ R^aL^b
\quad(a,b\in\{1,2\}).
```

It is a subset of the previously fixed sixteen-setting task: only the
pure words $`L^3,L^4,R^3,R^4`$ are removed. The new lower certificates use
the twelve settings; the explicit upper models are verified on all
sixteen. Consequently **every state count and error bracket stated below
holds separately for both menus**. No comparison is improved by changing
the target, clock, preparation or rival class.

All persistent Markov states are counted. A rival has one common initial
law $`\rho_0`$, one deterministic sign $`S`$, and fixed stochastic tick kernels
$`K_L,K_R`$. The ordinary reversible class retains

```math
\rho_j\propto\rho_0(1+m_jS),\qquad
\rho_j(x)K_j(x,y)=\rho_j(y)K_j(y,x).
```

Initial sign imbalance and zero initial masses are allowed in the lower
bound; no rival rate cap, topology or continuous-time embedding is
imposed. The two explicit approximations are irreducible continuous-time
models with positive equilibrium weights and exit rates below two.
They therefore also give uppers if every rival is required to be a CTMC.
These remain ideal population-law comparisons, not detector or device
claims.

## 2. Recovering sign-sector matrices without an intermediate observation

The following argument works for the established length-$`n`$ chain with
positive couplings and attempt rates, any positive clock, and any two
distinct finite tilts $`m_L\lt m_R`$. Write

```math
X=(1,S,K_LS,\ldots,K_L^{n-1}S),\qquad
Y=(1,S,K_RS,\ldots,K_R^{n-1}S).
```

Use unnormalized equilibrium weights $`\omega_j=\rho_0(1+m_jS)`$ and let

```math
C_L=X^{\mathsf T}\mathrm{diag}(\omega_L)Y,
\qquad C_R=X^{\mathsf T}\mathrm{diag}(\omega_R)Y.
```

Both matrices are observable from endpoint pairs. For example,
reversibility at the appropriate field gives

```math
\begin{aligned}
\langle K_L^aS,K_R^bS\rangle_{\omega_L}
 &=\mathbb E[S_0S_T]_{L^aR^b}
     +m_L\mathbb E[S_T]_{L^aR^b},\\
\langle K_L^aS,K_R^bS\rangle_{\omega_R}
 &=\mathbb E[S_0S_T]_{R^bL^a}
     +m_R\mathbb E[S_T]_{R^bL^a}.
\end{aligned}
```

The second matrix is obtained by transposing the matrix built from the
reverse protocol order. Zero powers and constant-containing entries use
pure-word means, correlations and the initial marginal. The pure words
through $`n-1`$ ticks and both mixed orders through $`n-1`$ ticks per segment
therefore suffice: $`2n(n-1)`$ settings in total.

For $`s=\pm1`$, eliminate the two Gibbs weights:

```math
\boxed{
A_s=\frac{(m_R-s)C_L+(s-m_L)C_R}{m_R-m_L}
 =X^{\mathsf T}\mathrm{diag}[\rho_0(1+sS)]Y.
}
```

Only states of sign $`s`$ contribute to $`A_s`$. Thus
$`\mathrm{rank}A_s\le d_s`$, where $`d_s`$ counts states of that sign.
The coefficients in this identity need not be positive. At the selected
tilts the formulas are particularly simple:

```math
A_+=2C_R-C_L,\qquad A_-=3C_L-2C_R.
```

These are generally **cross-Gram matrices, not symmetric positive
matrices**. Rank and singular-value arguments apply; positive-definite
language for arbitrary perturbed data would be inappropriate.

On the physical chain, $`X`$ and $`Y`$ are two bases of the same invariant
space $`\mathrm{span}(1,X_0,\ldots,X_{n-1})`$, as proved in the
[existing mean-space argument](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md).
Transform both bases to the physical coordinates and restrict to
$`(1,X_1,\ldots,X_{n-1})`$. The target becomes the conditional Gram given
$`S=s`$, which has rank $`n`$. Hence every exact ordinary reversible rival
needs $`d_+,d_-\ge n`$.

The unrestricted $`n+1`$ lower also uses the same smaller menu. Define the
observable matrix $`C_L`$ by its endpoint-moment formulas even for a general
Markov rival. It factors through its $`d`$ states using rows

```math
\omega_L,\quad q,\quad qK_L,\ldots,qK_L^{n-1},
\qquad q=\rho_0S+m_L\rho_0,
```

and columns $`(1,S,K_RS,\ldots,K_R^{n-1}S)`$. Constant-column identities
follow from stochasticity, without a stationary-preparation assumption
on the general rival. The physical target matrix is a cross-Gram between
two bases under a positive weight and is invertible. Therefore $`d\ge n+1`$.

Combined with the existing upper constructions, this yields exact
$`n+1`$ versus $`2n`$ on the fixed weak-coupling interval, and four versus six
at the stronger three-switch point, using $`2n(n-1)`$ settings. No common
reconstructed hidden-coordinate lift or third field is needed.

## 3. Certified changes in minimum state count

For either the twelve- or sixteen-setting menu, $`D_{\rm all}(\delta)`$
and $`D_{\rm ord}(\delta)`$ denote the minimum state counts at maximum
pair-law TV error $`\delta`$. The following are deterministic approximation
statements, not finite-sample confidence claims:

| Maximum TV error | General states | Ordinary reversible states |
| --- | ---: | ---: |
| $`0\le\delta\le2\times10^{-6}`$ | Exactly $`4`$ | Exactly $`6`$ |
| $`3.6\times10^{-6}\le\delta\le3.8\times10^{-6}`$ | Exactly $`4`$ | Exactly $`5`$ |
| $`\delta=2\times10^{-5}`$ | At most $`4`$ | Exactly $`4`$ |

The intervals between these rows and the exact transition locations are
not determined. The last row does not assert a general four-state lower
at its larger tolerance.

The [rank verifier](../scripts/verify_familiar_chain_cross_rank.py) uses
the fixed rational basis coefficients from the previous certificate.
At tolerance $`2\times10^{-6}`$, nonsymmetric row diagonal dominance
certifies both sign-sector ranks three and the general rank four. Target
dominance margins exceed $`0.88888887`$; the corresponding matrix-TV
coefficients are below $`264859`$, $`392686`$ and $`73901`$ respectively.

For the five-state interval, a rational diagonal preconditioner
$`\mathrm{diag}(1,17/16,17/16)`$ brings the nominal target to
$`\mathrm{diag}(1,289/288,289/288)`$. Exact enclosures give smallest
singular value greater than $`0.99999998`$. Each within-word outcome
coefficient difference's operator norm is bounded by checking positive definiteness of
$`b^2I-M^{\mathsf T}M`$ with rational Sylvester minors. This supplies a
spectral TV coefficient below $`258772`$ for the full positive-sector
matrix and below $`14707`$ for the negative-sector two-by-two minor.
At $`3.8\times10^{-6}`$ these matrices retain ranks at least three and two.
The general four-rank certificate also survives. Consequently every
ordinary rival has at least five states, while the explicit five-state
model below fits within $`3.6\times10^{-6}`$.

The four-state row is certified by retaining rank at least two in each
sign sector at $`2\times10^{-5}`$ and by the explicit four-state model.
Thus the fifth state is necessary at the tighter certified interval;
this conclusion does not follow merely from comparing two fitted models.

For completeness, all perturbation bounds use a fixed linear data map
$`A(P)=\sum_{w,z}P_w(z)M_{w,z}`$. Per-word TV error at most $`\delta`$ gives

```math
\|A(P)-A(P_*)\|
\le\delta\sum_w\max_{z,z'}\|M_{w,z}-M_{w,z'}\|,
```

for the chosen induced norm. The positive and negative parts of each
probability difference have equal mass at most $`\delta`$, proving the
bound. Nonsymmetric infinity-norm bounds preserve strict row diagonal
dominance; spectral-norm bounds preserve a positive smallest singular
value. Neither argument assumes symmetry of the rival's data matrix.

## 4. Two explicit reversible approximations

The parameters below are exact rational numbers. Small deterministic
least-squares/minimax calculations helped discover the fixtures; the
[production verifier](../scripts/verify_familiar_chain_small_models.py)
uses only their fixed rational values and proves the error bounds without
an optimizer or a convergence assumption.

For either model, set

```math
\rho_m(i)=\rho_0(i)(1+mS_i),\qquad
Q_m(i,j)=\frac{c_{ij}(m)}{\rho_m(i)}\quad(i\ne j),
\qquad Q_m(i,i)=-\sum_{j\ne i}Q_m(i,j).
```

The conductances are symmetric and nonnegative. Both preparations have
zero mean sign, so $`\rho_m`$ is normalized. The positive-edge graphs are
connected, giving irreducible reversible generators. Every exit rate is
less than two at the queried fields. If a model on the entire field
interval is desired, linearly interpolate the conductances between the
two tables. Positivity, detailed balance and the exit cap survive: each
exit is a ratio of affine functions with positive denominator, whose
extrema occur at endpoints. **Accuracy is certified only for the stated
menus**, not for arbitrary words or intermediate fields.

### Five states

Use readout $`(+,+,+,-,-)`$ and preparation

```math
\rho_0=(1/6,1/12,1/4,1/6,1/3).
```

This preparation is the one obtained by merging the last two negative
states in the old six-state realization. The conductances have been
adjusted; they are not simply the unmodified lumped dynamics. Multiply
each integer in the table by $`10^{-8}`$:

| Edge | $`c_{ij}(0)\times10^8`$ | $`c_{ij}(1/2)\times10^8`$ |
| --- | ---: | ---: |
| $`01`$ | 2285376 | 5909500 |
| $`02`$ | 0 | 4929465 |
| $`03`$ | 7635089 | 4211206 |
| $`04`$ | 3486189 | 5786091 |
| $`12`$ | 1700907 | 4916562 |
| $`13`$ | 0 | 0 |
| $`14`$ | 2730914 | 1803786 |
| $`23`$ | 3374977 | 2897294 |
| $`24`$ | 4981230 | 2439294 |
| $`34`$ | 1372514 | 373412 |

Its maximum error on the sixteen settings is enclosed in

```math
[3.513238204,3.513238205]\times10^{-6}
\quad\lt \quad3.6\times10^{-6}.
```

Let $`E_{\le5}`$ be the infimum of the maximum menu error over the entire
ordinary reversible class with at most five states. For either menu,

```math
\boxed{2\times10^{-6}\le E_{\le5}\lt 3.6\times10^{-6}.}
```

The upper is an explicit CTMC; the lower even allows arbitrary reversible
stochastic tick kernels. The construction is therefore within a factor
of $`1.8`$ of the best possible error in that broader class. Its exact
optimality is not established.

### Four states

Use readout $`(+,+,-,-)`$ and

```math
\rho_0=(33034911,16965089,16965089,33034911)/10^8.
```

Again multiply the conductance entries by $`10^{-8}`$:

| Edge | $`c_{ij}(0)\times10^8`$ | $`c_{ij}(1/2)\times10^8`$ |
| --- | ---: | ---: |
| $`01`$ | 8706018 | 13064817 |
| $`02`$ | 11080849 | 7178642 |
| $`03`$ | 0 | 0 |
| $`12`$ | 0 | 0 |
| $`13`$ | 11080849 | 9927582 |
| $`23`$ | 8706018 | 4354941 |

The maximum error is enclosed in
$`[1.9401171757,1.9401171758]\times10^{-5}`$, below $`1/50000`$.
This improves the earlier physical two-spin comparison on this finite
task. Its bound does not replace the older model's separate all-word
guarantee. The globally optimal four-state approximation remains unknown.

Both error certificates use positive uniformization: with exit cap two,
$`P=I+Q/2`$ is stochastic and
$`e^Q=e^{-2}\sum_{k\ge0}(2P)^k/k!`$. Rational series through degree 48 and
explicit geometric bounds on the positive tail enclose every transition
probability. The target's four-dimensional mean propagation is enclosed
independently. For balanced initial signs, pair TV is exactly
$`\max(|\Delta U|,|\Delta V|)/2`$, where $`U+sV`$ is the conditional final
mean given initial sign $`s`$.

## 5. Established tools, contribution and remaining significance

The rank machinery is established. Petreczky, Bako and van Schuppen,
[Theorems 4–5 and Remark 5](https://arxiv.org/pdf/1103.1343), relate
switched-linear realization dimension to generalized Hankel rank and
factor finite data blocks. Ohta,
[Equation (4) and Proposition 1](https://arxiv.org/pdf/2008.11487),
decomposes deterministic-output HMM spaces by observation sector. These
statements do not themselves reconstruct the present sector matrices
from two Gibbs weights and reversed endpoint-only protocols. The model
and force convention retain the [existing physical sources](FAMILIAR_CHAIN_SOURCE_AUDIT.md).

The additional construction is the observable elimination
$`A_+=2C_R-C_L`$, $`A_-=3C_L-2C_R`$. It exposes sign-sector state counts
without measuring an intermediate sign. The finite certificates and
explicit reversible models then establish a precision-dependent state
cost in the same familiar physical family. Internal review and the
focused source comparison do not constitute external validation or an
exhaustive priority determination.

The former five-state error interval is now narrow enough to identify its
scale: at this operating point, excluding every five-state predictor is
necessarily a parts-per-million question. A stronger certificate alone
cannot turn that fixed-task obstruction into a large observable error.
The twelve-setting witness and exact five-state interval are completed
mathematical results. A broadly useful physical consequence, practical
acquisition cost and publication readiness remain open. Manuscript
drafting remains deferred.
