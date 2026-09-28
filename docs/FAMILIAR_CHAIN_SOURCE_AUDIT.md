# Open kinetic chains: physical assumptions and source comparison

Focused primary-source audit, 28 September 2026. This note supports the
[controlled-chain result](FAMILIAR_CHAIN_CONTROL_COST.md); it is not a
complete priority search or a device-feasibility claim.

For the homogeneous open heat-bath chain with $n\ge3$, equal attempt rates,
and $0<t=\tanh J\le1/\sqrt5$, the current result is

$$
D_{\rm all}=n+1,\qquad D_{\rm ord}\ge2n.
$$

The comparison concerns one preparation, one binary endpoint readout, and
one reusable model across fields. The ordinary class obeys detailed balance
and the inherited equilibrium field convention. The explicit general
model obeys that same equilibrium convention, works at every finite
nonnegative field, and has exit rates at most $13/12$ in attempted-update
units. Its $n+1$ lower bound allows rivals without the equilibrium promises.

The ordinary lower bound needs only three fields and
$2(n-1)(n+2)$ endpoint-pair settings of at most $2n-2$ ticks. It applies
more broadly to unequal positive couplings and attempt rates. A positive
finite-accuracy radius is proved for fixed parameters. Passive endpoint
pairs alone have minimum $n+1$ in both classes. For three switches at
$t=1/3$ and three distinct field tilts in $[0,1/2]$, the ordinary minimum
is exactly six. Attainability of $2n$ for general $n$ remains open.

## Which physical assumptions are established, and which are selected?

| Assumption | Standing and role in this result |
| --- | --- |
| Two-state, time-even configurations with nearest-neighbor equilibrium coupling | A conventional conformational-switch interpretation of an Ising energy. Ordinary detailed balance is appropriate for these retained variables. This does not identify a magnetic moment with a time-even coordinate or cover predictors retaining genuine reversal-odd variables. See the [community model](FAMILIAR_SWITCH_COMMUNITY_MODEL.md). |
| Continuous-time single-spin heat-bath updates | An established kinetic Ising model. Godrèche's Eq. (2.19) gives the symmetric field-dependent rate; the discussion after Eq. (2.22) permits a spatially varying field while preserving detailed balance [1]. These rates are a model assumption, not an experimentally derived universal law for every switch. |
| Equal couplings and attempt rates in the positive construction | A deliberately selected homogeneous family. The reversible lower bound does not require this equality. Exact homogeneity in a particular device is not established. |
| $0<t\le1/\sqrt5$ | A sufficient positivity condition for the explicit simplex construction. It is neither a community requirement for heat-bath dynamics nor a proved optimal coupling boundary. |
| One field coupled only to the measured sign $S$ | The energy change $-hS$ gives $\pi_m=\pi_0(1+mS)$ when the zero-field sign is balanced, with $m=\tanh h$. A fixed, readout-compatible equilibrium reduction inherits the same tilt, as derived in the [equilibrium reduction note](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md). Imposing that interface on a predictor is substantive; a different actuator coupling to hidden coordinates falls outside the comparison. |
| One common zero-field equilibrium preparation | A selected prediction task. Reusing one hidden initial law across the protocol menu is necessary for the state-count argument; independently fitting every experiment is a different task. |
| Ideal deterministic binary endpoint observation | A selected observation task. Only the initial and final signs are requested, without intermediate measurement. Detector noise, finite switching, full observed paths, and a laboratory implementation are separate questions. |

The first two rows anchor the target in familiar physics. The remaining
rows state the particular family, interface, and data task under study.
They should not be presented as properties of every physical reduction.

## Closest mathematical and physical precedents

| Ingredient | Inspected primary statement | What it does and does not settle here |
| --- | --- | --- |
| Kinetic Ising mean closure | Godrèche [1], Eqs. (2.19), (3.2), and the discussion following Eq. (2.22). | Standard heat-bath dynamics and zero-field linear magnetization equations. With a field only at an endpoint, closure remains elementary: the endpoint has one neighbor and every bulk site has zero local field. The $n+1$ affine mean space is not a new solvability principle. |
| Shared linear realization and rank | Petreczky, Bako and van Schuppen [2], Theorems 3–5. | Minimal switched linear realizations are characterized by reachability, observability, and generalized Hankel rank. This does not itself give stochastic positivity, deterministic binary readout, a CTMC generator, or a shared Gibbs/detailed-balance realization. |
| Positive realization through a common cone | Benvenuti and Farina [3], Theorem 2 and its invariant-cone condition; Fanizza, Lumbreras and Winter [4], Section 2, Propositions 1–2 and the classical polyhedral criterion. | Positive realizations from invariant polyhedral cones are established machinery; positivity can already cost more states than unconstrained linear dimension. The inspected results do not supply this chain's explicit dyadic simplex, positivity over all nonnegative fields, uniform exit cap, or reversible state lower bound. |
| Passive reversible realization | Leite, Saldanha and Tomei [5], Introduction and Section 2; Brüning, Chelkak and Korotyaev [6], Theorem 1.4. | Finite Jacobi reconstruction from eigenvalues and positive spectral weights is standard inverse spectral theory. The [passive birth–death construction](FAMILIAR_CHAIN_PASSIVE_REALIZATION.md) is an application of that theory, not a new inverse spectral method. It provides one passive generator, without a common field-dependent realization. |
| Ranks within deterministic observation sectors | Ohta [7], Eq. (4), Proposition 1, and Eqs. (11)–(15). | Direct sums over observation symbols and transition/observation-projector invariant spaces are established HMM realization tools. Sectorwise rank counting is therefore not new by itself. The inspected setting is an autonomous observed process, without this controlled endpoint task and shared equilibrium tilt. |
| Weighted quadratic minimization and equality | Beard and Welters [8], Lemma 6, Eqs. (19)–(20), and Corollary 11, Eq. (27). | The variational representation of a Schur complement and its concavity are established facts. Common minimizers under equality are standard quadratic geometry. The final chain proof uses a direct sum-of-squares identity, rather than requiring a separate new matrix-concavity theorem. |
| Inferring detailed balance from responses | Franco, Kepka and Velázquez [9], Theorems 1.1 and 5.5, and Section 6. | Response reciprocity and its stability under admissible rate perturbations constrain detailed balance in a specified architecture; their theorem includes a cut-vertex alternative. This does not minimize the state count over alternative hidden architectures sharing a controlled Gibbs tilt. Their perturbation notion concerns rates/architecture, whereas the chain bound tolerates errors in the finite endpoint data. |

There is also a useful local caution. Gorban [10], Theorem 1, proves
equality of the instantaneous velocity cones of general and
detailed-balanced Markov kinetics at one distribution with fixed positive
equilibrium. The reversible generator may depend on that distribution.
This supplies no one generator, or one controlled family, that matches all
the protocols here. Local replacement and reusable prediction are distinct
requirements.

## What the chain calculation adds to these ingredients

The [positive construction](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md) makes
the known cone method explicit for this physical family. It gives one
$n+1$-vertex simplex, the dyadic preparation

$$
\nu=(1/2,1/4,\ldots,1/2^n,1/2^n),
$$

one negative-readout state, and a positive generator at every finite
$h\ge0$. The conditional initial spin means agree with those of the
physical chain; the shared mean equations therefore give every requested
endpoint pair after any finite field word. The construction also verifies
the common stationary law $\nu_m=\nu(1+mS)$ and the size-independent exit
cap. Linear closure alone does not establish these positivity and reuse
properties.

The [ordinary lower bound](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md), especially
Eqs. (19)–(23), addresses a different obstruction. Reversibility turns
measured endpoint pairs into both own-field and mixed-field Gram matrices
of reconstructed response coordinates. The target Gram is affine in the
tilt: $G(m)=G(0)+mG'(0)$. For three ordered tilts and their positive
interpolation weights $w_L,w_R$, those measured identities give

$$
w_L\| (\widehat F_M-\widehat F_L)v\|_L^2
+w_R\| (\widehat F_M-\widehat F_R)v\|_R^2
=v^{\mathsf T}[G(m_M)-w_LG(m_L)-w_RG(m_R)]v=0.
$$

Consequently the three reconstructed coordinate systems coincide on the
rival's initial support, including for nonminimal rivals. Conditioning
their common Gram on either observed sign gives rank $n$, requiring at
least $n$ states in each sign sector. The candidate additional content is
the observable finite protocol that forces this common representation and
the resulting $2n$ bound for the familiar chain, not the nonnegativity of
squared norms or the rank bound for a Gram matrix.

The [six-state construction](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
establishes sharpness for the specified three-switch family. Together with
the standard passive construction, this isolates the role of control:
both classes use $n+1$ states passively, while ordinary equilibrium
consistency raises the controlled requirement. The physical target itself
is reversible. The theorem does not claim to diagnose irreversible target
dynamics from its observations; it bounds the size of a reversible
predictor for them.

## Scope of the comparison

The searched and inspected sources establish close precedents for every
general tool used above. None of their inspected statements gives the
specific combined chain construction and controlled state-count theorem.
That bounded finding does not establish exhaustive literature priority.
The focused search included kinetic-chain magnetization reduction,
positive Markov realization, shared reversible realization, inverse
spectral reconstruction, and detailed-balance response inference.

The result counts complete persistent Markov states. Its proved ratio
$2n/(n+1)$ approaches two. It establishes neither an extensive bit-memory
advantage nor a Shannon-entropy or energetic saving. The exact minimum of
the ordinary class for general $n$, an optimal coupling range, useful
finite-sample error budgets, and device realization remain unresolved.
The positive robustness radius depends on the target and the conditioning
of the chosen finite data basis; it is not a uniform experimental margin.

## Primary sources

1. C. Godrèche, *Dynamics of the directed Ising chain*,
   [arXiv:1102.0141](https://arxiv.org/pdf/1102.0141), inspected version 2.
   The heat-bath model is historically due to Glauber; the explicit
   field-dependent formulas and closure used in this audit were inspected
   in Godrèche's treatment.
2. M. Petreczky, L. Bako and J. H. van Schuppen, *Realization theory of
   discrete-time linear switched systems*,
   [arXiv:1103.1343](https://arxiv.org/pdf/1103.1343), inspected version 2.
3. L. Benvenuti and L. Farina, *A Tutorial on the Positive Realization
   Problem*, IEEE Transactions on Automatic Control **49**, 651–664
   (2004), [full text](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf).
4. M. Fanizza, J. Lumbreras and A. Winter, *Quantum Theory in Finite
   Dimension Cannot Explain Every General Process with Finite Memory*,
   Communications in Mathematical Physics **405**, 50 (2024),
   [doi:10.1007/s00220-023-04913-4](https://link.springer.com/article/10.1007/s00220-023-04913-4).
5. R. S. Leite, N. C. Saldanha and C. Tomei, *Reconstruction of tridiagonal
   matrices from spectral data*,
   [arXiv:math/0508099](https://arxiv.org/pdf/math/0508099).
6. J. Brüning, D. Chelkak and E. Korotyaev, *Inverse spectral analysis for
   finite matrix-valued Jacobi operators*,
   [arXiv:math/0607809](https://arxiv.org/pdf/math/0607809).
7. Y. Ohta, *On the Realization of Hidden Markov Models and Tensor
   Decomposition*, [arXiv:2008.11487](https://arxiv.org/pdf/2008.11487),
   inspected version 1.
8. K. Beard and A. Welters, *Matrix monotonicity and concavity of the
   principal pivot transform*, Linear Algebra and its Applications
   **682**, 323–350 (2024),
   [arXiv:2302.04293](https://arxiv.org/pdf/2302.04293),
   [doi:10.1016/j.laa.2023.11.016](https://doi.org/10.1016/j.laa.2023.11.016).
9. E. Franco, B. Kepka and J. J. L. Velázquez, *Characterizing the Detailed
   Balance Property by Means of Measurements*, Archive for Rational
   Mechanics and Analysis **250**, 25 (2026),
   [doi:10.1007/s00205-026-02183-7](https://link.springer.com/article/10.1007/s00205-026-02183-7).
10. A. N. Gorban, *Local Equivalence of Reversible and General Markov
    Kinetics*, [arXiv:1205.2052](https://arxiv.org/pdf/1205.2052).
