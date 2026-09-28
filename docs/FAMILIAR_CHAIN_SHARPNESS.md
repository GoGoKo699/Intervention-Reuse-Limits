# The exact equilibrium state cost, and its accuracy limit

[Repository](../README.md) · [Construction](FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md) · [Accuracy bound](FAMILIAR_CHAIN_FINITE_ACCURACY.md) · [Sources](FAMILIAR_CHAIN_SHARPNESS_SOURCE_AUDIT.md)

The open-chain state-count question is now sharp on one fixed physical
parameter range. For every chain length $n\ge3$,

$$
\boxed{D_{\rm all}=n+1,\qquad D_{\rm ord}=2n.}
$$

The target is the established homogeneous heat-bath Ising chain, with
equal attempt rates and $0<\tanh J\le1/64$. A field acts on the first
switch, whose initial and final signs are recorded. All experiments reuse
one zero-field equilibrium preparation. The comparison uses nonnegative
field tilts $0\le\tanh h\le1/2$.

| Prediction task | General Markov states | Ordinary reversible states |
| --- | ---: | ---: |
| All passive endpoint pairs, exactly | $n+1$ | $n+1$ |
| Three-field finite controlled menu, exactly | $n+1$ | $2n$ |
| All controlled endpoint pairs in the stated range, exactly | $n+1$ | $2n$ |
| All endpoint pairs at TV tolerance $6\times10^{-8}$ in this weak-coupling range | At most 4 | At most 4 |

The last row is an approximation upper bound, not a statement that four
is minimal. It is essential to the interpretation of the first three.

## What is now closed

The earlier [positive construction](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md)
already supplied the $(n+1)$-state upper. The
[finite three-field proof](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md) forces
at least $n$ states of each visible sign in an ordinary reversible model.
The new [reversible construction](FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md)
attains that count for every length at fixed coupling.

The model places $n$ moment-matching nodes in each visible-sign sector.
It reproduces the physical mean dynamics and assigns simple relaxation
to the unused modes. A cosine basis diagonalizes the bulk interaction;
only bounded endpoint corrections remain. Weak coupling then guarantees
strictly positive transition rates independently of chain length.

The construction has uniform zero-field probabilities $1/(2n)$ and total
exit rates at most $33/32$ in attempt-time units. It uses the same Gibbs
stationary tilt as the physical target. The reversible upper also works
for signed tilts $|m|\le1/2$; the combined comparison above uses the
existing nonnegative-field general upper. The lower bound allows arbitrary
reversible architectures and has no rival rate cap or minimum mass.

The finite menu contains $2(n-1)(n+2)$ pair settings, each with at most
two field segments and $2n-2$ ticks at any fixed positive clock. The
existing explicit positive TV radius retains both minima when the lowest
of the three tilts is zero. Its size depends on the chosen chain and
fields. The older [three-switch example](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
keeps its stronger coupling $t=1/3$ and exact four-versus-six counts.

## What the accuracy result changes

For every homogeneous chain with $0<t<1$, truncation to its first
$\ell\ge2$ spins obeys

$$
\sup_w\operatorname{TV}(P_{n,w},P_{\ell,w})
\le\frac{t^{2\ell}}{1-t^4}.
$$

The [proof](FAMILIAR_CHAIN_FINITE_ACCURACY.md) is uniform over every
finite signed-field protocol and every horizon. Distant switches have
exponentially small conditional means, and their influence must propagate
back to the observed end. At $t\le1/64$, just two physical switches give
error at most $1/16777215<6\times10^{-8}$.

The lossless state cost therefore grows while sufficient state cost at
fixed accuracy stays bounded with length. Truncating just the last switch
also shows that any error threshold certifying all $2n$ reversible states
is at most $t^{2n-2}/(1-t^4)$: its decay with length is unavoidable.
The ratio $2n/(n+1)$ approaches
two in states; the corresponding logarithmic capacity difference stays
below one bit. Neither an extensive bit-memory saving nor a uniform
finite-precision advantage follows.

## Physical and publication assessment

The target kinetics and Gibbs force convention have published physical
antecedents, recorded in the [existing audit](FAMILIAR_CHAIN_SOURCE_AUDIT.md).
The new [comparison](FAMILIAR_CHAIN_SHARPNESS_SOURCE_AUDIT.md) credits
standard quadrature and reversible realization tools. The candidate
contribution is the complete constrained state-count comparison in this
physical family, with a finite observational obstruction and matching
construction. Internal checks do not certify priority or publication
readiness.

This closes a mathematical feasibility gap for reversible predictors.
It does not demonstrate a laboratory device implementing the smaller
circulating predictor, a finite energetic cost, or full-path equality.
Ordinary detailed balance plus the common Gibbs interface remains a
substantive class restriction justified by equilibrium model reduction.

The next scientific priority is a useful accuracy-dependent separation:
identify a nonvanishing range of tolerated endpoint error where requiring
equilibrium changes the best model, preferably with stronger interactions
or a simple precision law. The existing small-chain operating point is a
better starting point than increasing length in the very weak-coupling
family. A matched approximation theorem would clarify significance;
another exact length extension would not resolve that question.
Manuscript drafting remains last.

[Exact certificate](../reports/familiar_chain_sharpness.json) · [Verification](VERIFICATION.md)
