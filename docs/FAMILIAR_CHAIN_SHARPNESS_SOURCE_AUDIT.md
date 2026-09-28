# Sharp chain state counts: construction and source comparison

Focused primary-source comparison, 28 September 2026. This supplements the
[chain source audit](FAMILIAR_CHAIN_SOURCE_AUDIT.md) without changing its
historical assessment. The new upper bound resolves attainability on an
explicit coupling range independent of chain length. Its derivation has
passed independent internal review; that is distinct from external
validation or a literature-based certification of priority. See the
[sharpness overview](FAMILIAR_CHAIN_SHARPNESS.md) and
[reversible realization proof](FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md).

## The sharpened result and its range

For every open heat-bath chain of length $n\ge3$, the construction
uses equal coupling $t=\tanh J$ and field tilt $m=\tanh h$ satisfying

$$
0<t\le\frac1{64},\qquad |m|\le\frac12.
$$

There is a reversible $2n$-state model reproducing every requested
endpoint-pair law for arbitrary finite field words and positive dwell times.
Its common initial preparation is uniform, its readout is deterministic
and binary, and its stationary laws have the prescribed Gibbs tilt.
All off-diagonal rates are strictly positive and the total exit rates are
at most $1+2t\le33/32$ in attempted-update time units.

Combining this upper bound with the existing nonnegative-control
construction and three-field lower bound gives the exact finite-task
comparison

$$
D_{\rm all}=n+1,\qquad D_{\rm ord}=2n.
$$

The general-model upper bound used in this comparison is established for
nonnegative fields. The signed-field reversible upper bound therefore does
not establish the same two minima for a task that includes negative fields.
The comparison uses the existing finite menu with three distinct
nonnegative field tilts in $[0,1/2]$. Unlike the initial norm-bound
construction, the new sufficient coupling interval permits one fixed
positive coupling for arbitrarily large $n$.

## Established ingredients

| Ingredient | Inspected primary statement | Boundary of the comparison |
| --- | --- | --- |
| Positive moment representation using $2n$ symmetric nodes | Arasaratnam and Haykin [1], Sections IV-B–D, Propositions 4.1–4.2 and the construction following them, give the third-degree spherical-radial cubature rule and its covariance transformation. | Equal-weight antipodal nodes matching low-order moments are established. The chain construction orients and transforms these nodes to make the first coordinate exactly the observed sign. It does not introduce a new cubature method or assume a Gaussian physical chain. |
| Historical attribution of that cubature rule | Santos-León, Orive, Acosta and Acosta [2], Introduction, explicitly identify the third-degree rule with Stroud and Secrest's 1963 construction and its later tabulation by Stroud. | The original 1963 article was not accessible in this check. Its historical attribution is reported through [2], not represented as an independently inspected original formula. |
| Reversible kernels from orthogonal expansions | Griffiths [3], Introduction, Eq. (1), the subsequent displayed reversible transition kernel, and Eq. (3), describe nonnegative orthogonal expansions and their Poisson embedding in continuous time. | A spectral expansion gives a Markov kernel only after entrywise positivity is proved. The chain calculation supplies a sufficient uniform bound over its chosen field interval. |
| Positive realization of a symmetric linear response | Grussler and Damm [4], Theorem 4, give a symmetric positive minimal realization of a quasi-symmetric continuous-time SISO system by Lanczos/Arnoldi. | This concerns one input-output transfer function. It does not itself retain one binary readout, common preparation and Gibbs-compatible realization over the controlled family. |
| Exact stochastic reduction and switching words | Grigoletto and Ticozzi [5], Theorems 1–2, construct HMM reductions preserving single-time or full multi-time laws; Appendix A, Theorem 4, gives a projection criterion preserving outputs under every switching word. | All-word equivalence from a suitable common invariant subspace is established methodology. These statements do not supply the present reversible $2n$-state family with its fixed Gibbs interface. |
| Exact controlled positive dynamics | Grigoletto, Viola and Ticozzi [6], Propositions 1–2 and Theorem 1, construct an observable subspace for all controls and close it to an operator algebra to obtain valid reduced Lindblad dynamics. | This is a stronger controlled precedent than single-system realization. The guarantee concerns the resulting algebra's size, not a universal $2n$ bound or the present shared Gibbs tilt. |

## What the fixed-coupling construction adds to those tools

The spectral step is standard. Let $Y$ contain the centered node
coordinates, $R=Y^{\mathsf T}D_\rho Y$ their covariance, $\Pi$ the stationary
projection and $P=YR^{-1}Y^{\mathsf T}D_\rho$ the projection onto the mean
coordinates. If the physical mean drift is $-I+K$, the proposed generator
is

$$
\widehat Q=-I+\Pi+YK^{\mathsf T}R^{-1}Y^{\mathsf T}D_\rho
 +\frac16(I-\Pi-P).
$$

Diagonalizing its self-adjoint action gives a finite orthogonal-function
expansion of the type in [3]. The dynamics on the orthogonal complement of
the constant and mean coordinates are free: here their generator
eigenvalue is $-5/6$. After positivity is established, uniformization with
rate $33/32$ gives a reversible transition kernel and its Poisson
embedding. This is an algebraic identification with established spectral
machinery, not a theorem in [3] about this controlled chain.

The initial upper bound set the complementary eigenvalue to $-1$ and used
a global covariance norm estimate; its sufficient coupling decreased as
$1/n$. The new proof chooses a discrete-cosine orientation of the same
antipodal moment rule and changes the complementary eigenvalue. In that
basis, the bulk Jacobi part is diagonal and the residual is supported at
the chain boundaries. Its entrywise contribution is bounded by $16t$
independently of $n$, leaving strictly positive rates on the displayed
fixed coupling interval. Discrete-cosine diagonalization, moment cubature
and free spectral completion are not being claimed as new methods.

The same nodes and binary coordinate serve every field. Their Gibbs
weights, conditional preparation moments and common pointwise mean
equations establish endpoint-pair equivalence after arbitrary field
changes. This last inference is a standard common-subspace argument,
consistent with [5–6]; static moment matching alone would not suffice.

The controlled algebraic result [6] merits a concrete comparison. For the
present connected chain, the endpoint observable's cyclic span contains
all individual spins. Their pointwise algebra is the full algebra of
functions on the $2^n$ spin configurations: products of the factors
$(1\pm\sigma_j)/2$ give each configuration indicator. Consequently,
applying that observable-algebra closure directly does not produce the
$2n$ realization. This is our mathematical comparison with the inspected
algorithm, not a claim made in [6]. The present construction instead
represents the required preparation and observable moments on a new
finite state space. The controlled reduction in [6] guarantees the
selected observables for all initial states, whereas the present theorem
uses its specified equilibrium preparation and the two endpoint-conditioned
initial laws. The different preparation scope matters when comparing sizes.

## Contribution and unresolved scope

The new content is the matching upper bound for the established controlled
state-count obstruction, at fixed positive weak coupling and uniformly
bounded exit rates for every chain length. The combined theorem identifies
an exact cost of requiring
the predictor to obey ordinary detailed balance and the shared equilibrium
force convention. The physical target itself is reversible.

The inspected sources supply strong precedents for the construction tools;
none of their inspected statements supplies this complete controlled
comparison. In particular, this audit found no direct theorem combining
the sharp state counts, deterministic binary readout, common preparation,
shared Gibbs tilt and every finite field word at fixed positive coupling.
That bounded finding does not establish exhaustive literature priority or
publication readiness. The sufficient coupling threshold is not proved
optimal. The companion truncation result shows that a radius certifying
the exact $2n$ count must decrease at least exponentially with $n$; no
practical measurement budget is established.
No energetic saving, extensive bit-memory advantage, or device realization
is inferred from the exact state counts.

## Primary sources and access record

1. I. Arasaratnam and S. Haykin, *Cubature Kalman Filters*, IEEE
   Transactions on Automatic Control **54**, 1254–1269 (2009),
   [doi:10.1109/TAC.2009.2019800](https://doi.org/10.1109/TAC.2009.2019800).
   Sections IV-B–D inspected in the
   [author-uploaded full text](https://www.researchgate.net/publication/224471882_Cubature_Kalman_Filters).
2. J.-C. Santos-León, R. Orive, D. Acosta and L. Acosta,
   *The Cubature Kalman Filter revisited*, Automatica **127**, 109541
   (2021), [publisher introduction](https://www.sciencedirect.com/science/article/pii/S0005109821000613),
   [doi:10.1016/j.automatica.2021.109541](https://doi.org/10.1016/j.automatica.2021.109541).
   The cited historical source is A. H. Stroud and D. Secrest,
   *Approximate integration formulas for certain spherically symmetric
   regions*, Mathematics of Computation **17**, 105–135 (1963),
   [doi:10.1090/S0025-5718-1963-0161473-0](https://doi.org/10.1090/S0025-5718-1963-0161473-0);
   its full text was inaccessible in this check.
3. R. Griffiths, *Lancaster distributions and Markov chains with
   multivariate Poisson–Charlier, Meixner and Hermite–Chebycheff polynomial
   eigenfunctions*, [arXiv:1412.3931v3](https://arxiv.org/pdf/1412.3931v3).
   Introduction and Eqs. (1)–(3) inspected in full text.
4. C. Grussler and T. Damm, *A Symmetry Approach for Balanced Truncation
   of Positive Linear Systems*, 51st IEEE Conference on Decision and
   Control (2012), 4308–4313,
   [author manuscript](https://lup.lub.lu.se/search/files/3937565/3163112.pdf).
   Theorem 4 and its proof inspected in full text.
5. T. Grigoletto and F. Ticozzi, *Algebraic Reduction of Hidden Markov
   Models*, IEEE Transactions on Automatic Control **68**, 7374–7389
   (2023), [doi:10.1109/TAC.2023.3279209](https://doi.org/10.1109/TAC.2023.3279209),
   [author preprint](https://arxiv.org/pdf/2208.05968).
   Problems 1–2, Theorems 1–2, Remark 8 and Appendix A, Theorem 4,
   inspected in full text. The HMM theorems are stated for time-independent
   dynamics; the appendix explicitly treats switching linear systems.
6. T. Grigoletto, L. Viola and F. Ticozzi, *Model Reduction for Controlled
   Quantum Markov Dynamics*, [arXiv:2510.25546](https://arxiv.org/pdf/2510.25546).
   Problem 1, Propositions 1–2, Theorem 1 and the accompanying
   observable-algebra construction inspected in full text.

The companion [truncation proof](FAMILIAR_CHAIN_FINITE_ACCURACY.md) uses
standard cooperative-system comparison and an explicit tridiagonal Green
function. It gives an all-protocol endpoint-error upper bound, and shows
that the tolerance certifying the exact state count must decay with length.
The sharp lossless theorem does not establish a fixed-accuracy scaling
advantage. Neither comparison is an exhaustive novelty search.
