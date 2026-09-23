# Binary observations without a rival rate cap: the remaining gate problem

[Uncapped binary theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Rare-tag construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) · [Binary theorem with a common rate cap](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Bounded resolvent observability](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) · [Earlier rate boundary](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md)

**Research boundary, 23 September 2026.** An uncapped superpolynomial reversibility penalty is now proved for a new balanced binary target family by the [rare-tag construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) and [assembled theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md). The new family has a very large fixed rate-to-gap ratio and uses arbitrarily fast switching. This note records the operator obstructions and counterexamples that delimit the route; it is not a claim that the binary extension remains globally open.

The obstruction is not a universal positive-semidefinite property of binary observation words: the exact examples below disprove that property. These finite calculations alone neither prove the new lower bound nor construct a smaller fast reversible predictor. The new theorem uses separately established selector, observability and entropy estimates; it does not remove the rival rate cap for the earlier binary family with budget $6580k$.

## 1. What the existing palindrome obstruction actually says

For a reversible hidden generator $K$, each heat kernel $e^{tK}$ and positive resolvent $P_s=s(sI-K)^{-1}$ is selfadjoint and positive semidefinite in $L^2(\mu)$. A color word whose **entire operator sequence** is palindromic factors as $B C B^*$ with a positive-semidefinite central factor $C$. Its quadratic forms are nonnegative. A selfadjoint marker sandwich preserves that property.

This is exactly the obstruction established in Section 1 of the [earlier boundary note](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md). It excludes the literal replacement of every uniformization matrix in the old palindromic binary gates by one common heat kernel or resolvent. That old target gate needs a negative quadratic form on its lamp probe.

The condition concerns the whole sequence, including dwell times and resolvent parameters. A palindrome of colors alone need not be an operator palindrome. Nor does the obstruction cover all nonpalindromic binary words, signed combinations, or different gadgets.

Negative correlation is necessary for recovering the old exact lamp-flip gate on its old probe. It is not a universal necessary condition for every entropy proof: a quantitatively nontrivial partial flip can suffice when the other bits are preserved accurately enough. Conversely, a single negative scalar without marginal and preservation estimates is insufficient for either argument.

For example, on a uniform Boolean cube let $F_c$ flip bit $c$ and let $0<\lambda\le1/2$. The stationary Markov kernel $(1-\lambda)I+\lambda F_c$ is PSD, preserves every other bit exactly, and flips bit $c$ with probability $\lambda$. Its correlation with that bit is $1-2\lambda\ge0$. This illustrates why PSD alone does not exclude a partial-flip entropy strategy; it does not construct such a kernel from the binary observations of the target.

## 2. A minimal nonpalindromic counterexample

Take three hidden states with

$$
\mu=(1/4,1/4,1/2),\qquad
g=(-\gamma,-\gamma,+\gamma),\qquad 0<\gamma<1,
$$

and the row generator

$$
K=\begin{pmatrix}
-1&0&1\\
0&-4&4\\
1/2&2&-5/2
\end{pmatrix}.
\tag{1}
$$

This is an irreducible reversible star: the stationary fluxes on its two edges are $1/4$ and $1$. The actuator histogram is exactly balanced. It can be coupled to the original visible state with the unchanged field rule

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
\tag{2}
$$

the original preparation $(1/2,\mu/2)$ and binary visible readout. Equation (1) is written in units $k=1$. No modified physical input or extra readout is used in the algebraic example.

Let $D_0=\operatorname{diag}(1,1,0)$ and $D_1=\operatorname{diag}(0,0,1)$. At Laplace parameter one,

$$
P=(I-K)^{-1}
=\frac1{33}\begin{pmatrix}
19&4&10\\
4&13&16\\
5&8&20
\end{pmatrix}.
\tag{3}
$$

Set $v=(1,-1,0)^\mathsf T$ and

$$
W=D_0P D_0P D_1P D_0.
$$

The operator $W$ is entrywise nonnegative. Its nonzero block is

$$
W\big|_{\{1,2\}}
=\frac1{35937}\begin{pmatrix}
1270&2032\\
1240&1984
\end{pmatrix},
\qquad
\boxed{\langle v,Wv\rangle_\mu=-\frac1{7986}<0.}
\tag{4}
$$

Thus a positive binary resolvent word need not have nonnegative quadratic forms. The color word $0010$ is nonpalindromic. This is minimal among returning words using one fixed selfadjoint positive-semidefinite propagator: with at most two transitions every returning binary word is palindromic. Three states are also minimal, because with two states and both colors present the initial-color subspace is one-dimensional and every nonnegative returning word acts there by a nonnegative scalar.

The example contains no same-color edge. Its unequal exit rates within color zero already escape the larger PSD subclass proved in Section 4.

### The squared-resolvent version

The bounded-control observability lemma directly exposes words with $P_s^2$ between diagonal features. The counterexample also works for that propagator. In the same model,

$$
S=P^2=\frac1{1089}\begin{pmatrix}
427&208&454\\
208&313&568\\
227&284&578
\end{pmatrix},
$$

and exact rational multiplication gives

$$
\boxed{\langle v,D_0S D_0S D_1S D_0v\rangle_\mu
=-\frac{125989}{286992882}<0.}
\tag{5}
$$

A simultaneous rescaling of $K$ and the Laplace parameter leaves its resolvent unchanged. This observation concerns the algebraic PSD boundary; it does not establish the spectral band, scalar-observability budget, or asymptotic target family needed for the binary extension. In particular, the vector $v$ in (4)–(5) is a mathematical probe, not a newly available physical readout or a demonstrated binary-word-derived probe.

### Why this does not yet give a gate

The row sums of (4) are $(3302,3224)/35937$, whereas the stationary-adjoint row sums are $(2510,4016)/35937$. No common normalization makes both equal to one. The block has rank one; its negative quadratic form comes with unequal marginals. Its sign therefore supplies no near-stationary flip estimate and no entropy lower bound.

More precisely, if a strictly positive rank-one block $a b^*$ has a common positive right and adjoint eigenvector, then both $a$ and $b$ are proportional to that vector. After a positive normalization its quadratic forms are nonnegative. Repeating this particular word does not solve the marginal defect.

## 3. Unequal parameters break a color palindrome

Use the same $K,\mu,D_0,D_1$, but put

$$
P_s=s(sI-K)^{-1},\qquad
V=D_0P_1D_1P_2D_0,\qquad
z=(1,-3/5,0)^\mathsf T.
$$

Then

$$
\boxed{\langle z,Vz\rangle_\mu=-\frac1{14850}<0.}
\tag{6}
$$

The colors $010$ are palindromic; the two resolvent parameters are not reflected. Hence $V$ is not of the form $B B^*$ covered by the old argument. This example makes no assertion that an arbitrary asymmetric timing protocol gives a negative scalar. Mirrored parameters restore the PSD factorization.

## 4. A genuine all-word PSD subclass

There is a broader subclass where even asymmetric timings do not help. After stationary symmetrization, suppose

$$
K=\begin{pmatrix}-aI&B\\B^*&-bI\end{pmatrix},\qquad a,b\ge0,
\tag{7}
$$

where the blocks are the two color spaces. In the original state coordinates this means there are no same-color edges and the exit rate is constant within each color. Different constants for the two colors are allowed.

**Proposition.** Every returning binary word

$$
D_{c_0}S_1D_{c_1}\cdots S_\ell D_{c_\ell},
\qquad c_\ell=c_0,
\tag{8}
$$

is selfadjoint and positive semidefinite when each $S_j$ is a heat kernel, a positive resolvent, or a finite nonnegative mixture of those operators for the same generator (7). The parameters and mixtures may differ between positions.

**Proof.** Take a singular-value decomposition of $B$. A singular pair of value $\sigma\ge0$ spans a two-dimensional invariant space on which $K$ is

$$
K_\sigma=\begin{pmatrix}-a&\sigma\\\sigma&-b\end{pmatrix}.
$$

The two color projectors select its two coordinate lines. Since $K$ is a nonpositive selfadjoint generator, $\sigma^2\le ab$. Every entry of $e^{tK_\sigma}$ is nonnegative: one may add a sufficiently large scalar multiple of the identity to make the matrix entrywise nonnegative and expand its exponential. The same holds for a positive resolvent, either by integrating the heat kernel or by the formula

$$
s(sI-K_\sigma)^{-1}
=\frac{s}{(s+a)(s+b)-\sigma^2}
\begin{pmatrix}s+b&\sigma\\\sigma&s+a\end{pmatrix}.
$$

Nonnegative mixtures preserve this property. On the initial-color line of this mode, word (8) is multiplication by the product of the selected matrix entries of the $S_j$, hence by a nonnegative real scalar. Unmatched singular vectors lie in the kernel of $B$ or $B^*$; their color-changing words vanish and their color-preserving words are products of nonnegative scalars. The orthogonal direct sum over all modes proves the proposition. $\square$

Thus this subclass has an all-word obstruction, not merely a palindrome obstruction. The unequal color-zero exits in (1) violate (7). General reversible binary models need not satisfy (7), and the proposition gives no universal binary compression theorem.

## 5. Construction obligations and their current resolution

An uncapped lower bound requires a family of **positive binary words and derived probes**, not merely a negative scalar. The rare-tag construction and assembled theorem now meet the following obligations on their new target family. They remain useful criteria for judging other proposed binary encodings.

1. Its targets retain the original field rule, preparation, readout and exactly balanced binary histogram. Any fixed target exit budget, lower gap and spectral band asserted for the family must be proved uniformly in its size.
2. Each proof kernel is an entrywise nonnegative combination or product of bounded binary observation operators, positive in every allowed rival, including rivals with arbitrarily fast hidden rates. Any positive change of measure must use the rival's own states and account for zero coordinates.
3. The target word identities jointly control forward and adjoint marginal defects, derived-probe norms, and the addressed action on all relevant bits. Reproducing the old exact flip is one sufficient route. A partial-flip route instead needs a fixed nontrivial flip strength together with sufficiently accurate preservation of all other bits and quantitative control of the repaired kernels.
4. Approximation errors, normalization factors, word lengths and coefficient masses are tracked together as the number $r=2^n$ of addressed bits grows. In the old whole-word criterion, the relevant scalar defect must be at most a constant times $r^{-2}$. A partial-flip criterion must state its own accumulated error threshold. A fixed imperfect finite gadget is not enough without such a calculation.
5. The bounded-control observability lemma must transfer the required scalar estimates from actual mean accuracy with constants uniform in rival dimension, stationary masses and rates. A useful inverse-accuracy lower bound then follows only after this transfer cost and the target approximation error have been optimized on the same scale.

The [rare-tag construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) provides approximate signed-port selectors and transports. The [mixed killed-word lemma](MIXED_KILLED_WORD_OBSERVABILITY.md) controls their actual-mean observation cost, and [weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md) supplies the rival-state entropy step. Their quantitative combination is the [uncapped binary theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md).

The old palindromic replacement and the scalar-block subclass in Section 4 still have the stated PSD obstructions. The new theorem passes around those routes using a different target family. Uncapped bounds for the earlier $6580k$ binary family, a substantially smaller target rate-to-gap ratio, fixed positive-clock versions, and stronger or matched uncapped growth laws are not resolved by this checkpoint.
