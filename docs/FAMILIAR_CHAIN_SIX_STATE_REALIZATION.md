# Three switches: exactly four predictive states versus six reversible states

For a familiar three-spin heat-bath chain, the state-count comparison can
be made exact. With equal couplings $\tanh J=1/3$, three boundary fields
with distinct tilts in $[0,1/2]$ give

$$
\boxed{D_{\rm all}=4,\qquad D_{\rm ord}=6.}
$$

The same twenty endpoint-pair settings certify both minima, at any fixed
positive clock, and the separation persists at a positive total-variation
tolerance. The four-state upper bound is the specialization of
[the positive chain realization](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md).
The lower bounds follow from
[the three-field reversible bound](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md).
This note supplies the matching six-state reversible upper bound.

The comparison counts every persistent Markov state. All models use one
common initial preparation and deterministic binary readout. The ordinary
class satisfies detailed balance and the equilibrium convention that the
boundary field couples only to the measured sign. No physical device or
practical measurement budget is established by this state-count theorem.

## The physical model and finite task

Take three time-even spins $(S,\sigma_1,\sigma_2)$ with thermal energy and
common attempted-update rate set to one:

$$
E_h=-J(S\sigma_1+\sigma_1\sigma_2)-hS,
\qquad \tanh J=\frac13,\qquad m=\tanh h.
$$

Use ordinary continuous-time single-spin heat-bath dynamics and start
from the zero-field equilibrium $\pi_0$. Its mean equations are

$$
\begin{aligned}
Q_m S&=A_m-S+B_m\sigma_1,\\
Q_m\sigma_1&=\frac3{10}(S+\sigma_2)-\sigma_1,\\
Q_m\sigma_2&=\frac13\sigma_1-\sigma_2,
\end{aligned}
\qquad
A_m=\frac{8m}{9-m^2},\quad
B_m=\frac{3(1-m^2)}{9-m^2}.
$$

Choose any three distinct tilts

$$
0\le m_L<m_M<m_R\le\frac12
$$

and any clock $\tau>0$. Each letter denotes one clock tick at its selected
field. Record the joint law of $(S_0,S_T)$ for

$$
\begin{aligned}
&j^q,&&j\in\{L,M,R\},\quad q=1,2,3,4,\\
&L^aM^b,\ R^aM^b,&&a,b\in\{1,2\}.
\end{aligned}
$$

There are twenty settings, each with at most four ticks and two field
segments. The common preparation matters: a rival cannot choose a
different hidden initial law for each word.

The ordinary equilibrium convention for a rival is

$$
\rho_j=\frac{\rho_0(1+m_j\widehat S)}
 {1+m_j\mathbb E_{\rho_0}\widehat S},
$$

with detailed balance at each selected field. Exact matching fixes the
initial sign probabilities to one half, making the denominator one.
The lower bound permits arbitrary reversible stochastic kernels at the
clock. The matching upper bounds are continuous-time generators, so the
minima are the same if every rival is required to be a CTMC.

## Six states and their common preparation

The six states carry the following functions:

| State | $\widehat S$ | $Z_1$ | $Z_2$ | $\rho_0$ |
|---|---:|---:|---:|---:|
| $0$ | $1$ | $-1$ | $-1/3$ | $1/6$ |
| $1$ | $1$ | $1$ | $-5/3$ | $1/12$ |
| $2$ | $1$ | $1$ | $1$ | $1/4$ |
| $3$ | $-1$ | $1$ | $1/3$ | $1/6$ |
| $4$ | $-1$ | $-1$ | $5/3$ | $1/12$ |
| $5$ | $-1$ | $-1$ | $-1$ | $1/4$ |

Only $\widehat S$ is the physical readout. The other two columns are
internal coordinate functions, so their values need not lie in
$[-1,1]$. The probabilities and transition rates are nonnegative.

The common preparation has

$$
\mathbb E_{\rho_0}\widehat S
=\mathbb E_{\rho_0}Z_1
=\mathbb E_{\rho_0}Z_2=0,
\qquad
\mathbb E_{\rho_0}[\widehat S Z_1]=\frac13,
\quad
\mathbb E_{\rho_0}[\widehat S Z_2]=\frac19.
$$

Consequently,

$$
\mathbb E_{\rho_0}[(Z_1,Z_2)\mid\widehat S=s]
 =s\left(\frac13,\frac19\right),\qquad s=\pm1,
$$

exactly as in the physical chain. The full spin-coordinate Gram also
agrees:

$$
\mathbb E_{\rho_0}
\left[
\begin{pmatrix}\widehat S\\Z_1\\Z_2\end{pmatrix}
\begin{pmatrix}\widehat S&Z_1&Z_2\end{pmatrix}
\right]
=
\begin{pmatrix}
1&1/3&1/9\\
1/3&1&1/3\\
1/9&1/3&1
\end{pmatrix}.
$$

## Reversible conductances

Set

$$
\rho_m(i)=\rho_0(i)[1+m\widehat S_i].
$$

For each unordered pair, use the symmetric conductance
$c_{ij}=c_{ji}$ below. Unlisted pairs have zero conductance.

| Pair $ij$ | Conductance $c_{ij}(m)$ |
|---|---|
| $01$ | $\dfrac{(1+m)(1+2m)}{15(3+m)}$ |
| $02$ | $\dfrac{m}{10}$ |
| $03$ | $\dfrac{(1-m)(7+4m)}{30(3+m)}$ |
| $04$ | $\dfrac{m(1-m)(1+m)}{6(3-m)(3+m)}$ |
| $05$ | $\dfrac{(1-m)(1+3m)}{10(3-m)}$ |
| $12$ | $\dfrac{(1+m)(1+2m)}{20(3+m)}$ |
| $14$ | $\dfrac{(1-m)(1+m)}{12(3+m)}$ |
| $23$ | $\dfrac{(1-m)(1+2m)}{10(3+m)}$ |
| $25$ | $\dfrac{1-m}{20}$ |
| $34$ | $\dfrac{(1-m)(2-m)}{30(3+m)}$ |
| $45$ | $\dfrac{(1-m)(1-2m)}{20(3-m)}$ |

Define

$$
\widehat Q_m(i,j)=\frac{c_{ij}(m)}{\rho_m(i)}
\quad(i\ne j),
\qquad
\widehat Q_m(i,i)=-\sum_{j\ne i}\widehat Q_m(i,j).
$$

Every displayed numerator factor is nonnegative for
$0\le m\le1/2$, and every denominator and equilibrium weight is strictly
positive. Hence these are finite Markov generators. The conductance
symmetry gives detailed balance identically:

$$
\rho_m(i)\widehat Q_m(i,j)
=\rho_m(j)\widehat Q_m(j,i).
$$

The edges $01,03,05,12,14,23,25,34$ remain strictly positive throughout
the closed interval and connect all six states. Thus every generator is
irreducible, including at both endpoints. No vanishing-time or
unbounded-rate limit is required.

## Why every controlled endpoint law agrees

Direct substitution gives the pointwise identities

$$
\begin{aligned}
\widehat Q_m\widehat S&=A_m-\widehat S+B_m Z_1,\\
\widehat Q_m Z_1&=\frac3{10}(\widehat S+Z_2)-Z_1,\\
\widehat Q_m Z_2&=\frac13 Z_1-Z_2.
\end{aligned}
$$

These are rational identities in $m$. They reproduce exactly the physical
mean equations and hold for every field in the interval. Therefore each
controlled propagator preserves
$\operatorname{span}\{1,\widehat S,Z_1,Z_2\}$ with the same action as the
physical model.

The two models have the same initial sign probabilities and the same
conditional coordinate means for each initial sign. Their conditional
means remain identical after every finite sequence of these generators,
with arbitrary positive dwell times. In particular,

$$
\Pr(\widehat S_T=b\mid\widehat S_0=s)
=\frac{1+b\,\mathbb E[\widehat S_T\mid\widehat S_0=s]}2
=\Pr(S_T=b\mid S_0=s).
$$

Thus all controlled endpoint-pair laws agree, including the twenty-setting
menu. This proof does not assert equality of intermediate-observation or
full path laws.

## Exact and finite-accuracy state counts

The positive realization gives four states for all finite nonnegative
fields at this coupling. The finite-menu rank bound rules out three
states even for unrestricted Markov rivals. The reversible bound requires
at least three states of each visible sign, and the construction above
attains six. Hence the same finite task has

$$
D_{\rm all}(0)=4,\qquad D_{\rm ord}(0)=6.
$$

Let $\delta_{\rm all}>0$ and $\delta_{\rm ord}>0$ be the explicit
bounds in
[the finite-accuracy proof](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md#5-a-positive-finite-accuracy-radius),
evaluated for these couplings, three fields, and clock. Then

$$
0\le\delta<\min\{\delta_{\rm all},\delta_{\rm ord}\}
\quad\Longrightarrow\quad
D_{\rm all}(\delta)=4,\qquad D_{\rm ord}(\delta)=6.
$$

The upper bounds are exact, so they apply at every nonnegative tolerance;
the positive radius is needed only for the lower bounds. It is a
conservative mathematical certificate, not an optimized experimental
error budget. In particular the conditioning of the field-dependent mean
bases can make it small.

## Scope and verification

This is a sharp three-spin example inside the broader chain family. It
does not establish a reversible $2n$-state construction for every chain
length, coupling, or field range. The physical eight-state chain remains
an available ordinary realization, while the six-state construction shows
that reproducing these endpoint observations does not require retaining
all physical configurations.

The conductances were discovered with a small six-state linear feasibility
calculation; the proof consists of the displayed rational identities and
factor signs, with no numerical fitting or parameter samples required.
