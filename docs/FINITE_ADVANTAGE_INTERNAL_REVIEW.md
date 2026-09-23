# Internal review of the finite state advantage

[Finite theorem](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Capped clock calculus](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [Earlier exact 38-state boundary](UNCAPPED_WALSH_OBSERVABILITY.md#6-partial-cubes-state-budgets-and-an-exact-small-target)

**Independent internal audit, 23 September 2026.** The complete construction and finite-error argument in `FINITE_REVERSIBILITY_ADVANTAGE.md` pass the review recorded below. The proof supplies a new twelve-state ordinary reversible target, an exact eleven-state stationary predictor, and an explicit positive error floor against every allowed ordinary reversible model with at most eleven states. The new target is separate from the earlier lamp target whose smallest exact minimum is thirty-eight in both comparison classes.

This is a mathematical review of the stated model classes and finite constants. The tolerance is $2^{-3000}$, so the result resolves existence of a small certified state advantage; it does not yet supply useful experimental precision. The explicit eleven-state predictor is not asserted to satisfy generalized detailed balance.

## 1. Construction, stationary laws and physical count

The target has six edge memories and five vertex probes of $K_{2,3}$, plus the visible state. Its edge mass is $1/12$ and probe mass is $d_i/24$, with $d=(3,3,2,2,2)$. These laws sum to one, with one half in each hidden block.

The target incidence-edge flux is $1/24$ in both directions. Conditional refresh within each block is reversible under the same law. Its exit rate is $2$ minus the conditional self-refresh probability and is therefore at most $2$. The incidence graph is connected.

The target's rate band does not rely on numerical eigenvalues. Its rate-one incidence walk is a reversible bipartite Markov walk, with relaxation spectrum in $[0,2]$. The block-constant subspace has rates $0,2$ and receives no refresh contribution. On its orthogonal complement, block refresh adds the identity to the relaxation operator. The resulting nonzero rates lie in $[1,3]$. This verifies both the common cap and the claimed relation to the external clock.

The predictor has five memory states and five probes, plus the same visible state: eleven total. Each of its hidden block laws is $d_i/12$, with unconditional mass $d_i/24$ per state. Its exit cap is also two. Its stationary incidence flows balance at each vertex, but ordinary detailed balance fails on a cross-block one-way edge. Block refresh does not fill those missing reverse edges.

## 2. Exact intertwining and intervention equivalence

The stochastic map sends an edge memory equally to its two endpoint memories and fixes each probe. Independent row checks give

$$
C1=1,\qquad \mu_TC=\mu_R,\qquad K_TC=CK_R.
$$

For an edge row, the image of the target jump is the equal mixture of the two corresponding predictor memory-to-probe jumps. For a probe row, choosing an incident edge uniformly and then an endpoint gives probability $1/2$ of its own endpoint and $1/(2d_i)$ of each neighbor. These are precisely the predictor's rates. The conditional refreshes intertwine because their conditional laws push forward under the same map.

Every mixed row stays in the common memory kinetic label. Thus the diagonal barrier multiplications intertwine at every field. Extending the map by fixing the visible state preserves the full external rates, preparation and readout. In particular, the incoming row identity is
$\mu_TB_TC=\mu_TCB_R=\mu_RB_R$; there is no missing barrier factor or unobserved preparation. Propagator intertwining therefore proves equality of every controlled mean. This is stronger than equality at the two fields used by the lower.

All predictor memory coordinates are counted. The construction can be viewed as sampling an eventual endpoint earlier while all memory states remain kinetically indistinguishable; it does not require knowledge of later fields.

## 3. Positive rival features and the target Gram matrix

The two-field identities recover the hidden return diagonal and hidden generator through the visible projector. They require a field-independent hidden generator and unit zero-field return rates, both explicit assumptions of the comparison.

The six squared Lagrange polynomials are nonnegative diagonal operators on every rival barrier value in $[0,1]$. Only on the target are they exact label projectors. No state is assigned a target label in the lower-bound proof. The common hidden exit cap makes $P=I+K/2$ nonnegative; ordinary detailed balance makes it selfadjoint.

The five memory features are $2A_0PA_i1$ and the five probe features are $A_i1$. On a target edge the former equals $1/2$ at each incident vertex and zero elsewhere. On probes it vanishes. Thus direct summation under the stated stationary law gives

$$
G_T=\operatorname{diag}\left(
\frac1{48}\begin{pmatrix}3I_2&\mathbf1\\\mathbf1&2I_3\end{pmatrix},
\operatorname{diag}(d_i/24)\right).
$$

This normalization uses the hidden law $\mu$. The factor two in the physical scalar identity correctly converts the hidden Gram to preparation $\pi_0=(1/2,\mu/2)$.

In an ordinary reversible rival, reversing the selfadjoint hidden factors gives the actual stationary adjoint. The resulting Gram is a sum of one nonnegative rank-one atom per hidden state. A nonreversible rival need not interpret that same reversed positive word as its actual Gram; this is the distinction that permits the exact smaller predictor.

## 4. Robust atom count and exact arithmetic

The six bipartite edge entries and five isolated probe diagonals form eleven witnesses. Each is at least $c=1/48$, and every target diagonal is at most $M_0=1/8$. With at most ten nonnegative atoms, each witness must receive at least $(c-\varepsilon)/10$ from one atom.

The diagonal bounds control every atom coordinate by $\sqrt{M_0+\varepsilon}$. Therefore all coordinates in an assigned witness support are at least
$(c-\varepsilon)/(10\sqrt{M_0+\varepsilon})$. This includes a diagonal witness, whose square-root lower bound is stronger. Any two distinct witnesses have a target-zero off-diagonal pair in their combined supports: two different edges of a triangle-free graph cannot form a clique, and the probe coordinates are isolated.

Pigeonhole collision of eleven witnesses on ten atoms contradicts error at most $\varepsilon$ whenever

$$
100\varepsilon(M_0+\varepsilon)<(c-\varepsilon)^2.
$$

For $\varepsilon_0=1/40000$, the two sides are exactly

$$
\frac{5001}{16000000}
\quad\text{and}\quad
\frac{6235009}{14400000000},
$$

with positive margin $1734109/14400000000$. These comparisons were independently checked using rational arithmetic. They require neither a lower stationary mass nor a lower feature value in a rival.

## 5. Controlled-mean transfer and finite constants

The whole-side logarithm estimate applies uniformly because reversible full generators have spectral cap eight. At $H=\log2$ and $a=(\log2)/8$, the constants are exactly

$$
\rho=1/2,\quad\varrho=3/2,\quad\chi=2,\quad C_a=32,
\quad C_H=19/3<7.
$$

The barrier polynomial has coefficient mass at most ten after expanding hidden complements; each numerator factor has mass at most twelve. The Lagrange denominator minimum is $12/16^5$. Hence

$$
12^4 16^5=81\,2^{28}<2^{35},
\quad \|A_i\|_{\rm coeff}<2^{70},
\quad \deg A_i\le10.
$$

The positive kernel $P$ has mass at most five and degree one. Feature degree is at most twenty-one and mass at most $2^{144}$. The **complete** Gram polynomial, including its physical normalization, consequently has degree at most forty-two and mass at most $2^{289}$. Its transfer prefactor is at most $2^{289}32^{42}=2^{499}$.

There is no missing adjoint-metric coefficient here: the feature adjoint is obtained by reversing its selfadjoint hidden factors, each of which has the same specified generator/projector expression. There is also no factor of forty-two in the clock horizon. The logarithm expansion is truncated by total degree across the complete scalar polynomial. Visible-projector insertions are recovered by the finite preparation recursion and use no longer physical word.

At cutoff $1200$ and mean accuracy $2^{-3000}$, the exact bounds are

$$
2^{499}\,2(2/3)^{1201}<2^{-100},\qquad
2^{499}4^{1200}\,8401\,2^{-3000}<2^{-87}.
$$

Their sum is less than $1/40000$. The coefficient, tail and noise inequalities were independently checked using exact rational arithmetic, rather than floating-point rank or matrix fitting. Thus the finite observation premise contradicts the atom bound for every ordinary reversible eleven-total-state rival.

The sufficient experiment family is all two-field words through 1200 ticks, with maximal physical horizon $150\log2/k$. Its finiteness does not imply a small experiment count or sample requirement.

## 6. Secondary statements and scope corrections

The finite-entropy-production perturbation preserves the predictor's states, stationary law, kinetic labels and exit cap. The largest absolute sensitivity is $\log_2(11/8)$, so $R=11/4$. With $\eta=\delta_0/22$, the cited perturbation bound gives error at most $\delta_0/2$ for protocols with $|h(t)|\le H=\log2$, and finite full zero-field entropy production at most $k\log(22/\delta_0)$. The fixed amplitude range was made explicit during review; the exact unperturbed intertwining has the broader all-bounded-protocol equality.

The $K_{p,q}$ exact extension also passes. Conditional stationary laws, refreshes and the endpoint intertwiner preserve the same band and cap. Its positive Gram has one required atom for each of the $pq$ edges and each of the $p+q$ isolated probes. Under the stated common capped interface, exact ordinary count is $pq+p+q+1$, while an unrestricted predictor with $2(p+q)+1$ states is supplied. The alphabet grows with $p+q$, and no common positive-error tolerance for this extension is claimed.

The twelve-versus-eleven theorem is not a generalized-reversal size comparison, a practical-tolerance certificate, or an arbitrary-interface theorem. It uses the common kinetic interface, stationary preparation, field-independent hidden generator and cap two. The old 38-state lamp result is unchanged. Completely positive factorization, triangle-free support counting and Markov intertwining are established tools; this review does not certify a novelty claim.

## 7. Second independent review and handoff

A second reviewer independently read the complete final proof and returned **PASS**, with no corrections requested. That review checked the full generator/label/preparation intertwining, target cap and band, eleven-atom support argument, all controlled-mean constants through the $2^{-3000}$ certificate, the 1200-tick horizon, the finite-EPR amplitude scope, and the exact growing-alphabet $K_{p,q}$ corollary. The main coordinating review also passed.

No unresolved mathematical issue remains in the stated finite theorem after these reviews. The proof and this audit are frozen for verifier provenance. New bounded matrix checks and any complete repository gate remain separate evidence; their results should be recorded by the verifier and verification log rather than inferred from the analytic review.
