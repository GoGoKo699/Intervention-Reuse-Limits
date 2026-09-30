# A positive realization of an open kinetic Ising chain

This note gives an exact Markov realization of endpoint-pair observations for
an entire family of open heat-bath Ising chains. An `n`-spin physical chain has
`2^n` configurations, but `n+1` Markov states suffice for every finite word of
nonnegative fields at the observed end. All fields use the same initial
preparation. The construction concerns ideal state observations and does not
establish a hardware implementation or its energetic cost.

## Statement and physical model

Let `n >= 3`, and write the physical spins as
`sigma_0,...,sigma_(n-1)`, with observed spin `S=sigma_0`. Set the thermal
energy and common attempted-update rate to one. The energy is

```math
 E_h=-J\sum_{j=0}^{n-2}\sigma_j\sigma_{j+1}-h\sigma_0,
 \qquad t=\tanh J,\quad m=\tanh h.
```

Each spin undergoes the usual continuous-time single-spin heat-bath update.
The exact generator action on the spin functions is

```math
 Q_h\sigma_0=A_m-\sigma_0+B_m\sigma_1,
 \qquad
 A_m=\frac{m(1-t^2)}{1-t^2m^2},\quad
 B_m=\frac{t(1-m^2)}{1-t^2m^2},
```

```math
 Q_h\sigma_j=\frac{t}{1+t^2}(\sigma_{j-1}+\sigma_{j+1})-\sigma_j
 \quad(1\le j\le n-2),\qquad
 Q_h\sigma_{n-1}=t\sigma_{n-2}-\sigma_{n-1}.
```

For

```math
 0\lt t\le\frac1{\sqrt5},
```

there is an explicit `(n+1)`-state continuous-time Markov model with
deterministic binary readout that reproduces every endpoint-pair law of the
physical chain, starting in its zero-field equilibrium, for every finite
piecewise-constant control word with `h >= 0`. One preparation and one
generator per field serve the entire task. The construction also has a
stationary law with the same Gibbs tilt in the observed spin.

The coupling bound is sufficient for this particular construction. It is
not asserted to be an optimal feasibility boundary.

## The simplex and preparation

Use states `ell=0,...,n`. The auxiliary coordinates are

```math
 x_j^{(\ell)}=
 \begin{cases}
 (2^{j+1}-1)t^j,&j\lt \ell,\\
 -t^j,&j\ge\ell,
 \end{cases}
 \qquad 0\le j\le n-1.
```

In particular, `x_0=-1` only at state zero, and `x_0=+1` at every other
state. Set the readout to `x_0`. The remaining coordinates are real-valued
functions on the finite state space; they are not additional physical spins.

The common initial law is

```math
 \nu_0=\frac12,\qquad
 \nu_\ell=2^{-\ell-1}\ (1\le\ell\lt n),\qquad
 \nu_n=2^{-n}.
```

The simplex is nondegenerate: consecutive vertices differ by
`2^(j+1)t^j` in coordinate `j` only. Its affine barycentric functions are

```math
 p_0(x)=\frac{1-x_0}{2},
```

```math
 p_k(x)=\frac{x_{k-1}+t^{k-1}}{2^k t^{k-1}}
       -\frac{x_k+t^k}{2^{k+1}t^k}
 \quad(1\le k\le n-1),
 \qquad
 p_n(x)=\frac{x_{n-1}+t^{n-1}}{2^n t^{n-1}}.
```

Thus `p_k(x^(ell))=delta_(k,ell)`. The functions
`1,x_0,...,x_(n-1)` form a basis of all functions on the new state space.

The initial moments satisfy

```math
 \mathbb E_\nu x_j=0,\qquad
 \mathbb E_\nu[x_0x_j]=t^j,
```

and, more strongly,

```math
 \mathbb E_\nu[x_j\mid x_0=s]=s t^j\quad(s=\pm1).
```

For `s=-1` this is the single state zero. For `s=+1`, the total
conditional probability of vertices `ell>j` is `2^(-j)`, giving
`-t^j+2^(j+1)t^j 2^(-j)=t^j`. These are precisely the corresponding
conditional spin means in the physical zero-field Gibbs chain.

## Explicit rates

Put

```math
 L_m=\frac{(1-t^2)(1+m)}{2(1-t^2m^2)},\qquad
 \lambda_m=\frac{(1-m)[1-t^2(3+2m)]}{2(1-t^2m^2)},
```

```math
 a=\frac1{2(1+t^2)},\quad
 b=\frac{2t^2}{1+t^2},\quad
 c=\frac{3t^2}{2(1+t^2)},\quad
 d=\frac{1-2t^2}{2(1+t^2)}.
```

Start with all off-diagonal rates zero and add the following rates. When
two entries describe the same transition, add their contributions. This
happens at `2 -> 1`, whose total rate is `d-lambda_m+b`.

| Transition | Added rate | Index range |
|---|---:|---|
| `0 -> 1` | `L_m` | |
| `1 -> 0` | `1-L_m` | |
| `ell -> 0` | `lambda_m` | `2 <= ell <= n` |
| `ell -> 1` | `d-lambda_m` | `2 <= ell <= n` |
| `ell -> ell-1` | `b` | `2 <= ell <= n-1` |
| `ell -> ell+1` | `a` | `1 <= ell <= n-2` |
| `n-1 -> n` | `1/2` | |
| `n -> n-1` | `c` | |

Set each diagonal to minus its outgoing-rate sum. This defines `Qhat_m`.
Every listed rate is nonnegative. Indeed, for `0 <= m < 1` and `5t^2<=1`,

```math
 1-L_m=\frac{(1-m)(1+t^2+2t^2m)}{2(1-t^2m^2)}\ge0,
 \qquad \lambda_m\ge0,
```

while

```math
 d-\lambda_0=\frac{3t^4}{2(1+t^2)}\gt 0,
 \qquad
 \lambda_0-\lambda_m
 =\frac{m(1-t^2)(1-3t^2m)}{2(1-t^2m^2)}\ge0.
```

The other rates are manifestly positive. For every finite field this
generator is irreducible. The limiting `m=1` matrix is also a valid Markov
generator, although irreducibility and a strictly positive tilted
stationary law are then lost; the statement only needs finite fields.

The realization does not require faster rates as the chain grows. Its
total exit rates, in the physical attempted-update time unit, are

```math
 L_m,\quad 1-L_m+a,\quad
 \underbrace{1,\ldots,1}_{\ell=2,\ldots,n-2},\quad
 \frac{2+3t^2}{2(1+t^2)},\quad \frac12.
```

The interior list is empty when `n=3`. Since
`L_m>=L_0=(1-t^2)/2`, the second entry is at most
`(1+t^2)/2+1/[2(1+t^2)]<=61/60`; the penultimate entry is at most
`13/12`. Thus every exit rate is at most `13/12`, uniformly in chain
length and all finite nonnegative fields. In particular no unbounded-rate
or vanishing-time-scale limit is hidden in the construction.

## Exact generator intertwining

Let `F_m(x)` be the affine vector field given by the physical mean equations
above, with `sigma_j` replaced by `x_j`. Define

```math
 g_j^{(\ell)}=\frac{F_{m,j}(x^{(\ell)})}{2^{j+1}t^j}.
```

The barycentric derivative construction gives

```math
 \widehat Q_m(\ell,0)=-g_0^{(\ell)},\quad
 \widehat Q_m(\ell,k)=g_{k-1}^{(\ell)}-g_k^{(\ell)}
 \ (1\le k\lt n),\quad
 \widehat Q_m(\ell,n)=g_{n-1}^{(\ell)}.
```

Here these identities include the diagonal entries. They imply row sums
zero and `Qhat_m x_j=F_(m,j)(x)` immediately, because barycentric functions
reconstruct every affine coordinate.

For completeness, the values yielding the rate table can be evaluated
without any matrix inversion. The first-coordinate values are

```math
 g_0^{(0)}=L_m,\qquad
 g_0^{(1)}=-(1-L_m),\qquad
 g_0^{(\ell)}=-\lambda_m\ (\ell\ge2).
```

For an interior spin `1 <= j <= n-2`, the successive values are

```math
 g_j^{(\ell)}=
 \begin{cases}
 0,&\ell\lt j,\\
 a,&\ell=j,\\
 -d-b,&\ell=j+1,\\
 -d,&\ell\ge j+2.
 \end{cases}
```

For the last spin,

```math
 g_{n-1}^{(\ell)}=
 \begin{cases}
 0,&\ell\lt n-1,\\
 1/2,&\ell=n-1,\\
 -1/2,&\ell=n.
 \end{cases}
```

Taking adjacent differences gives exactly the displayed transition rates,
including both boundary rows. This is an all-length algebraic proof, not
an extrapolation from a finite list of chain lengths.

## Full endpoint-pair laws and Gibbs tilt

The physical and reduced models have the same affine mean equations under
each field. Their initial conditional mean vectors agree separately for
`S_0=+1` and `S_0=-1`. Consequently they retain identical conditional mean
vectors after every finite control word. In particular,

```math
 \Pr(S_T=b\mid S_0=s)=\frac{1+b\,\mathbb E[S_T\mid S_0=s]}2
```

is identical for both models. The common initial sign probabilities are
one half, so all four probabilities in every endpoint-pair law agree.
This argument makes no claim about intermediate observations or full path
laws.

The same construction automatically has the stationary family

```math
 \nu_m(\ell)=\nu_\ell[1+m x_0^{(\ell)}].
```

It is normalized, strictly positive for finite fields, and gives
`E_(nu_m)x_j=m t^j`. These moments solve the stationary affine mean
equations, since `A_m+m(t B_m-1)=0`. Because `1,x_0,...,x_(n-1)` are a full
function basis, this proves `nu_m Qhat_m=0`. At `m=0` this also verifies
stationarity of the common preparation.

The realization is irreversible: for example `n -> 0` has positive rate
at every finite field, whereas `0 -> n` has rate zero. Its shared Gibbs
tilt therefore does not make it an equilibrium, detailed-balanced device.

## State minimality within the stated task

The construction has the smallest possible state count among arbitrary
finite Markov models reproducing all passive endpoint pairs with a single
initial preparation. At zero field the physical mean matrix is an
irreducible tridiagonal matrix with positive off-diagonal entries. It is
diagonally similar to a real symmetric Jacobi matrix, so it has `n`
distinct real eigenvalues. They are strictly negative: its row sums are
strictly negative because `t<1` and `2t/(1+t^2)<1`.

The physical generator is self-adjoint in the Gibbs inner product. Its
restriction to the spin span is therefore self-adjoint as well. The
observed endpoint spin is cyclic in this span: successive applications
of the generator expose the next spin with a nonzero coefficient. Its
equilibrium autocorrelation consequently has the form

```math
 C(\tau)=\sum_{r=1}^n w_r e^{-\gamma_r\tau},
 \qquad w_r\gt 0,\quad\gamma_r\gt 0,
```

with distinct `gamma_r`. At any fixed positive clock `tau`, the sequence

```math
 p_k=\Pr(S_0=+,S_{k\tau}=+)=\frac14\left(1+
 \sum_{r=1}^n w_r e^{-k\gamma_r\tau}\right)
```

has a nonsingular `(n+1)` by `(n+1)` Hankel matrix
`H_(ij)=p_(i+j)`, `0<=i,j<=n`: its factorization is a square Vandermonde
matrix times the positive diagonal weights times its transpose. Any
`D`-state rival with one preparation and one repeated passive transition
kernel factors this same Hankel matrix through dimension `D`. Hence
`D>=n+1`.

Only the passive pair laws at lags `tau,...,2n tau` are needed for this
lower bound; `p_0` is their common initial positive-sign marginal. The
common-preparation condition matters. Independently selected hidden
preparations at different lags are not covered by this Hankel argument.

## Scope

The model family uses standard single-spin heat-bath dynamics, equal
nearest-neighbor couplings, and equal attempted-update rates. Its bounded
coupling range is an explicit theorem hypothesis. No low-temperature,
fast-variable, continuum, or large-system limit is used. The proof is exact
for every finite chain length and every finite nonnegative field word.

This note establishes an upper bound and matching unrestricted state
minimality. The [three-field proof](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md)
also certifies that general minimum on its shorter finite menu and proves
the ordinary reversible lower bound of $`2n`$. A detailed-balance lower bound must separately specify its
preparation and force interface; its assumptions must not be inferred from
this construction alone. No quantitative detector tolerance, physical
implementation, or dissipation advantage is established here.
