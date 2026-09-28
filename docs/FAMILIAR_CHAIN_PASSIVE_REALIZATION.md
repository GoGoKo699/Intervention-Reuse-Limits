# Passive endpoint pairs need one state per relaxation mode, plus one

This note supplies the passive comparison for the
[controlled-chain theorem](FAMILIAR_CHAIN_CONTROL_COST.md). The construction
is an application of standard finite inverse spectral theory, with primary
sources identified in [the source audit](FAMILIAR_CHAIN_SOURCE_AUDIT.md).
It reproduces two-time laws, without asserting agreement of observed paths.

## Statement

Suppose a stationary, balanced, deterministic binary readout of a reversible
finite continuous-time Markov chain has autocorrelation

$$
C(a)=\sum_{j=1}^{n}w_j e^{-\lambda_j a},\qquad
0<\lambda_1<\cdots<\lambda_n,\quad w_j>0,\quad\sum_jw_j=1.
$$

Then its passive endpoint-pair laws have exact minimum state count $n+1$
in both the general and ordinary-reversible Markov classes. One fixed
preparation and one fixed passive generator must serve every lag. The
reversible upper is an irreducible birth–death chain with one negative
readout state and $n$ positive readout states.

In particular, this applies to the positively coupled open heat-bath
$n$-switch chain, with arbitrary positive couplings and attempt rates.
The endpoint spin is cyclic in the tridiagonal mean system, so precisely
$n$ distinct nonzero modes occur with positive weights. The physical chain
has $2^n$ configurations. The lower and upper here concern the smaller
endpoint-pair prediction task.

## Construction from the spectral measure

Use the probability measure

$$
\mu=\frac12\delta_0+\frac12\sum_{j=1}^{n}w_j\delta_{\lambda_j}.
$$

Orthogonal polynomials for this finite measure give a symmetric Jacobi
matrix $J$ of dimension $n+1$, with positive neighboring off-diagonals,
eigenvalues $0,\lambda_1,\ldots,\lambda_n$, and spectral measure $\mu$
at its first coordinate. Conjugate by
$D=\operatorname{diag}(1,-1,1,\ldots)$ to obtain $L=DJD$, whose
neighboring off-diagonals are negative.

Its normalized zero eigenvector $v$ is strictly positive: for sufficiently
large $c$, the matrix $cI-L$ is irreducible and nonnegative, and its
Perron eigenvalue is $c$. Define

$$
Q=-\operatorname{diag}(v)^{-1}L\operatorname{diag}(v),
\qquad \rho_i=v_i^2.
$$

Then $Q$ has nonnegative off-diagonals, zero row sums, and detailed balance
under the positive law $\rho$. The zero spectral weight gives $v_0^2=1/2$.
Take $S=1-2\mathbf1_{\{0\}}$. Its stationary sign law is balanced, and

$$
P_{00}(a)=[e^{-aL}]_{00}=\frac{1+C(a)}2,
\qquad \mathbb E_\rho[S_0S_a]=-1+2P_{00}(a)=C(a).
$$

A balanced stationary binary pair table is
$\Pr(S_0=s,S_a=b)=[1+sbC(a)]/4$. Thus every endpoint pair is correct.

## Lower bound without a reversible-rival assumption

At any clock $\tau>0$, the sequence

$$
p_k=\Pr(S_0=+,S_{k\tau}=+)=\frac14
\left(1+\sum_{j=1}^{n}w_j e^{-k\lambda_j\tau}\right)
$$

has Hankel rank $n+1$. The $(n+1)$-square matrix $(p_{i+j})_{i,j=0}^n$
is a Vandermonde matrix times a strictly positive diagonal matrix times
its transpose. For any $d$-state rival it factors through the $d$-dimensional
hidden state, so $d\ge n+1$. Its $p_0$ is the observed initial marginal;
the positive lags through $2n\tau$ suffice. Arbitrary nonstationary rival
preparation is allowed if the same preparation serves every lag.

The augmented pair-data factorization in the
[three-field proof](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md) establishes the
same general lower bound on its shorter finite menu. The inverse spectral
upper here is solely a passive construction: it does not supply a common
field-dependent model. Requiring that reuse is exactly where the controlled
ordinary lower bound increases to at least $2n$.
