# Two fields suffice, with an explicit prediction-error gap

[Repository](../README.md) · [Earlier three-field proof](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md) · [Six-state model](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md) · [Certificate](../reports/familiar_chain_accuracy.json)

The controlled chain obstruction needs only **two field values**. A direct
positive-semidefinite comparison replaces the earlier interpolation through
a third field. For three switches, sixteen initial/final pair experiments
suffice. At the established stronger-coupling point, their state minima are
**four general states versus six ordinary reversible states**, including
every pair-law total-variation tolerance at most $`10^{-6}`$.

This is a quantified model-reduction result. The tolerance is small, and
the bounds below do not yet establish a useful experimental advantage or
publication readiness. All states of each predictor are counted. Only
endpoint pairs, rather than complete visible paths, are compared.

## 1. The physical task and comparison class

Keep the open heat-bath chain, common zero-field equilibrium preparation,
and deterministic binary readout $`S=X_0`$ from the
[existing model](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md#1-physical-target-and-finite-task).
The general lower statement permits arbitrary positive chain couplings
and attempt rates. Choose two distinct finite field tilts
$`-1\lt m_L\lt m_R\lt 1`$ and one positive clock $`\tau`$.

Record the initial and final signs for

```math
\begin{aligned}
&j^q,&&j=L,R,\quad 1\le q\le2n-2,\\
&L^aR^b,\ R^aL^b,&&1\le a,b\le n-1.
\end{aligned}
```

There are $`2(n^2-1)`$ settings, each with at most two field segments and
$`2n-2`$ ticks. The use of both pulse orders is essential to this proof.

A rival has one initial law $`\rho_0`$, one deterministic sign $`\widehat S`$,
and one fixed stochastic kernel $`\widehat K_j`$ per field. Require detailed
balance with the equilibrium force convention

```math
\rho_j=\frac{\rho_0(1+m_j\widehat S)}
 {1+m_j\mathbb E_{\rho_0}\widehat S}.
```

No prescribed hidden topology, rate cap, minimum stationary mass, or
continuous-time embedding is needed for the lower bound. Initial sign
imbalance and zero initial masses are allowed. The unnormalized weights
$`\omega_j=\rho_0(1+m_j\widehat S)`$ also satisfy detailed balance and have
the same support. This is the established equilibrium reduction class;
it is a substantive restriction, not a statement about every physical
memory implementation.

## 2. An observable sign-sector inequality

Let $`f_L,f_R`$ be rows of $`n`$ real functions reconstructed as fixed linear
combinations of

```math
H_j=(1,\widehat S,\widehat K_j\widehat S,\ldots,
                \widehat K_j^{n-1}\widehat S).
```

The coefficients are fixed before examining a rival. For an outer field
$`o`$ and a reference field $`r`$, define

```math
G_o=\langle f_o,f_o\rangle_{\omega_o},\qquad
C_{or}=\langle f_o,f_r\rangle_{\omega_o},\qquad
D_r=\langle f_r,f_r\rangle_{\omega_r}.
```

Here a Gram entry is the inner product of its two component functions.
All these entries are linear functions of the registered pair laws.
In particular, reversibility gives

```math
\langle\widehat K_o^a\widehat S,
       \widehat K_r^b\widehat S\rangle_{\omega_o}
 =(\rho_0\widehat S+m_o\rho_0)
      \widehat K_o^a\widehat K_r^b\widehat S.
```

The right side is an endpoint correlation plus $`m_o`$ times an endpoint
mean. Zero powers and constant-containing entries use the same pure-word
laws and their marginals; they require no extra measurement.

For the positive sector take $`(o,r)=(R,L)`$, and for the negative sector
take $`(o,r)=(L,R)`$. With $`s=+1`$ or $`-1`$ respectively, put

```math
a_s=\frac{1-sm_o}{1-sm_r},\qquad
c_s=\frac{s(m_o-m_r)}{1-sm_r}\gt 0,\qquad
W_s=C_{or}+C_{or}^{\mathsf T}-G_o-a_sD_r.
```

The elementary identity
$`\omega_o-a_s\omega_r=c_s\rho_0(1+s\widehat S)`$ yields

```math
\boxed{\quad W_s=c_s A_s-N_s\preceq c_s A_s,\quad}
```

where

```math
\begin{aligned}
A_s&=\mathbb E_{\rho_0}
 [(1+s\widehat S)f_r^{\mathsf T}f_r],\\
N_s&=\mathbb E_{\omega_o}
 [(f_o-f_r)^{\mathsf T}(f_o-f_r)]\succeq0.
\end{aligned}
```

The matrix $`A_s`$ is supported only on states with sign $`s`$. If that sector
has fewer than $`n`$ states, $`A_s`$ has a nonzero null vector, and $`W_s`$ cannot
be positive definite. Thus **positive definiteness of both observed
matrices certifies at least $`n`$ states of each sign**.

The two sectors may use different reference functions. There is no need
to first prove that the rival's reconstructed hidden coordinates agree
between fields. This is why the third field can be removed.

## 3. Exact two-field state counts

On the physical chain, choose the reconstruction coefficients so that
both $`f_j`$ equal $`\overline F=(1,X_1,\ldots,X_{n-1})`$. Such coefficients
exist at every positive clock: the endpoint's cyclic mean space and the
invertibility of $`H_j`$ on that space were proved in the
[earlier argument](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md#2-mean-closure-and-the-affine-gram-matrix).
Then $`N_s=0`$ and

```math
W_s=c_s\mathbb E_{\pi_0}
 [\overline F^{\mathsf T}\overline F\mid S=s]\succ0.
```

Each conditional distribution has full support on the hidden spin
configurations, so its $`n`$ functions are independent. Every exact
ordinary reversible rival therefore needs at least $`2n`$ states on the
two-field menu. The existing unrestricted rank proof needs only the
pure words at one field and still forces at least $`n+1`$ general states.

The established upper constructions consequently give:

| Model and control range | General minimum | Ordinary reversible minimum |
| --- | ---: | ---: |
| Every $`n\ge3`$, equal attempts, $`0\lt t\le1/64`$, two tilts in $`[0,1/2]`$ | $`n+1`$ | $`2n`$ |
| Three switches, equal attempts, $`t=1/3`$, two tilts in $`[0,1/2]`$ | $`4`$ | $`6`$ |

These are exact endpoint-pair minima, with distinct tilts. The upper
constructions also reproduce all words in their stated field intervals.
The historical three-field proof and its certificates remain unchanged.

## 4. A certified one-part-per-million tolerance

Fix three switches with $`t=\tanh J=1/3`$, equal attempt rates, clock
$`\tau=1`$, and field tilts $`m_L=0`$, $`m_R=1/2`$. Here a tick is one
attempt-time unit. The sixteen words are

```math
L,L^2,L^3,L^4,\quad R,R^2,R^3,R^4,\quad
L^aR^b,\ R^aL^b\quad(a,b\in\{1,2\}).
```

The [exact-arithmetic verifier](../scripts/verify_familiar_chain_accuracy.py)
fixes rational reconstruction coefficients and orthogonalizes the physical
conditional coordinates as
$`(1,X_1-s/3,X_2-X_1/3)`$. Their ideal conditional Gram is
$`\mathrm{diag}(1,8/9,8/9)`$. Rounding the reconstruction coefficients
does not invalidate the sector inequality: it holds for arbitrary fixed
coefficients. The verifier encloses the resulting target matrices directly.

Write either observable witness as

```math
W_s(P)=\sum_{w,z}P_w(z)M_{s,w,z},\qquad z=(S_0,S_T).
```

Its coefficient matrices are symmetric and rational. If each law changes
by at most $`\delta`$ in total variation, then

```math
\|W_s(P)-W_s(P_*)\|_2\le\delta L_s,\qquad
L_s=\sum_w\max_{z,z'}\|M_{s,w,z}-M_{s,w,z'}\|_\infty.
```

For each word the positive and negative parts of the probability
difference have equal mass at most $`\delta`$. This proves the diameter
bound; symmetry gives $`\|M\|_2\le\|M\|_\infty`$. It covers arbitrary
per-setting errors, not only independent or symmetric detector noise.
Each rival has one common initial marginal across its word settings;
treating the word errors separately is a conservative bound.

Rational Taylor enclosures of the physical mean propagators and strict
diagonal-dominance bounds certify both matrices positive definite at
$`\delta=10^{-6}`$:

| Certificate | Target diagonal-dominance margin exceeds | TV coefficient is below |
| --- | ---: | ---: |
| Positive-sign sector | $`0.44444443`$ | $`335557`$ |
| Negative-sign sector | $`0.29629628`$ | $`253748`$ |
| General four-dimensional data matrix | $`0.88888887`$ | $`56639`$ |

The smallest margin remaining after the permitted perturbation exceeds
$`0.0425`$. A separate nonsymmetric observed-matrix calculation
rules out three general states at the same tolerance. With the inherited
exact upper constructions,

```math
\boxed{0\le\delta\le10^{-6}
\quad\Longrightarrow\quad D_{\rm all}(\delta)=4,
\qquad D_{\rm ord}(\delta)=6.}
```

This is a deterministic approximation theorem for ideal endpoint laws.
It does not supply a finite-sample test, a detector model, or an acquisition
budget. The lower covers every rival in the declared class, including
nonminimal architectures and arbitrary reversible stochastic tick kernels.

## 5. Approximation comparison

There is also a simple, admissible four-state approximation. Use a physical
two-spin heat-bath chain with the same coupling $`t=1/3`$, unit attempt rate
at the measured spin, and hidden attempt rate $`r=5/6`$. Prepare its own
zero-field equilibrium and use the same observed sign and fields. It obeys
ordinary detailed balance and precisely the shared Gibbs tilt. The rival
class does not require its hidden attempt rate to equal the target's.

The [separate upper verifier](../scripts/verify_familiar_chain_approximation.py)
certifies

```math
\max_{w\text{ in the sixteen-setting menu}}
 \mathrm{TV}(P_{3,w},P_{2,r,w})\lt \frac1{3000}.
```

This is an upper bound furnished by one explicit model, not an optimized
fit. Defining $`E_{\le5}`$ as the infimum of the maximum menu error over all
admissible reversible predictors with at most five states, we obtain

```math
\boxed{10^{-6}\le E_{\le5}\lt \frac1{3000}.}
```

The upper model actually has four states. The more than two-order-of-
magnitude gap between the endpoints remains unresolved; neither bound is
claimed sharp. In particular, the lower bound does not show that a useful
fraction of the upper error is unavoidable.

### Uniform guarantee for the same four-state model

The approximation also has a proved all-protocol bound

```math
\sup_{w:\,h\ge0}\mathrm{TV}(P_{3,w},P_{2,r,w})\lt \frac1{600},
```

including arbitrary finite nonnegative field words, dwell times and total
horizons. This stronger protocol scope has a different numerical bound.
No full-path approximation is asserted.

To prove it, write either model's conditional visible mean as $`U+sV`$
given initial sign $`s`$. Cooperative mean dynamics give $`U,V\ge0`$ under
nonnegative fields. Also $`U\le1`$, as the unconditional spin mean, and
$`V\le1`$, as half the difference of two conditional spin means. Extend
the visible input into negative time by $`U=0`$, $`V=1`$. This produces exactly
the hidden equilibrium-conditioned initial means.

Eliminating the target's two hidden mean coordinates gives the positive
kernel

```math
K(u)=\frac{t}{1+t^2}e^{-u}\cosh\left(\frac{tu}{\sqrt{1+t^2}}\right),
\qquad K_r(u)=rt e^{-ru},\qquad u\ge0.
```

Both have integral $`t`$. The visible equation has the same driving term
in both models and feedback coefficient $`0\le B_m\le t`$. For either
$`U`$ or $`V`$, let $`d=z-y`$ be the target-minus-approximation difference.
Its initial value and prehistory vanish, and

```math
\dot d=-d+B_m\{K*d+(K-K_r)*y\}.
```

Because $`0\le y\le1`$ and $`\int(K-K_r)=0`$, the second convolution has
absolute value at most $`\|K-K_r\|_1/2`$. On every finite horizon,
variation of constants gives

```math
\sup|d|\le t^2\sup|d|+\frac t2\|K-K_r\|_1.
```

For balanced initial signs, the endpoint-pair distance is exactly
$`\max(|\Delta U|,|\Delta V|)/2`$. Therefore, with normalized kernels
$`k=K/t`$ and $`k_r=K_r/t`$ at $`t=1/3`$,

```math
\mathrm{TV}(P_{3,w},P_{2,r,w})
\le\frac{t\|K-K_r\|_1}{4(1-t^2)}
=\frac{\|k-k_r\|_1}{32}.
```

For $`r=5/6`$ the densities are
$`k(u)=(9/10)e^{-u}\cosh(u/\sqrt{10})`$ and
$`k_r(u)=(5/6)e^{-5u/6}`$. Their log ratio
$`\log(27/25)-u/6+\log\cosh(u/\sqrt{10})`$ is strictly convex.
Rational series enclosures locate its only two roots within
$`[0.5530,0.5531]`$ and $`[3.3702,3.3703]`$.
The survival functions are

```math
S_k(u)=e^{-u}\left[\cosh(u/\sqrt{10})
 +\frac1{\sqrt{10}}\sinh(u/\sqrt{10})\right],\qquad
S_r(u)=e^{-5u/6}.
```

Monotonicity of these tails at the four rational bracket endpoints
certifies $`\|k-k_r\|_1\lt 0.048493102`$, yielding the uniform bound above.
No floating-point root finding or integration is needed. The finite-menu
bound instead encloses the actual small mean propagators for all sixteen
words, using the same physical approximation.

The next scientific question is whether a sharper lower bound or an
explicit five-state model can substantially narrow this error interval.
The two-field simplification is complete; practical finite-accuracy
significance remains open.

## 6. Established methods and scope

The model and equilibrium convention retain the
[existing physical sources](FAMILIAR_CHAIN_SOURCE_AUDIT.md). No new device
capability or rate restriction is introduced. Gram factorization,
rank-based dimension bounds, subtraction of a squared norm, and
minimum-eigenvalue perturbation are standard tools. The additional content
here is their observable two-field combination for this shared Gibbs
interface, plus the explicit error certificate in the physical chain.

Three inspected primary comparisons delimit that claim:

- Grussler and Damm, [Theorem 4](https://lup.lub.lu.se/search/files/3937565/3163112.pdf),
  construct a symmetric positive minimal realization for one quasi-symmetric
  continuous-time SISO system. This does not impose the shared controlled
  family, binary readout, preparation and Gibbs interface used here.
- Grigoletto, Viola and Ticozzi,
  [Proposition 2 and Theorem 1](https://arxiv.org/html/2510.25546v1), preserve
  selected observables for every control and initial state through a
  positive observable-algebra reduction. Their minimality is restricted
  to that procedure. The present preparation scope is narrower, while
  its lower bound ranges over alternative reversible architectures.
- de Vicente, [Observation 1 and Section II D](https://arxiv.org/pdf/1611.01105),
  gives rank-based classical dimension bounds for prepare-and-measure
  behavior matrices and studies a specified input-independent mixture
  noise. That noise result is distinct from the arbitrary per-setting
  total-variation perturbation bounded above.

These comparisons attribute the methods and limit the candidate novelty;
they are not an exhaustive priority determination. Independent internal
review is recorded in [Verification](VERIFICATION.md). Hardware feasibility,
full-path equivalence and a thermodynamic cost do not follow. Manuscript
drafting remains deferred.
