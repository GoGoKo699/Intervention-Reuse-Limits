# Publication scope and closest-theorem comparison

[Repository overview](../README.md) · [Source audit](PRIOR_ART.md) · [Structure-cost proof](STRUCTURE_COST.md) · [Current work order](../work_orders/CURRENT.md)

**Expanded research assessment, 22 September 2026.** The central candidate is now a distinction between passive simplicity, low-order response complexity, and full controlled prediction. General reversible targets can require a state count larger than every fixed power of the logarithm of the inverse mean error, even with binary sensitivity, a bounded internal rate band, and a fixed minimum control dwell time. Within one explicit family, exact cubic prediction needs $n+3$ states while full controlled prediction needs at least $2^n$.

A complementary theorem proves uniform finite-field approximation inside the original reversible family, preserving exact sensitivity variance and all specified passive and lower-order agreements. Its double-exponential upper bound is far above the lower bound. The general complexity law is not sharp. The earlier sharp rank-one theorem remains a resolved special case, while the information and observation theorems explain what calibration can reveal.

The response, realization, spectral approximation, and Hankel-rank mechanisms remain established. The candidate contribution is their concrete consequence for physical Markov state cost in this passive-equivalent controlled family. The comparisons below and in the source audit constrain that claim; they do not certify originality. Manuscript writing remains on hold during research development.

## 1. General prediction cost and the sharp subclass

### General actuators have a larger state cost

Fix $k,G,W,H$ with $0<W\le G^2$. The [general controlled lower bound](GENERAL_CONTROLLED_LOWER_BOUND.md) proves, for sufficiently small actual-mean tolerance $\delta$,

$$
D_*^{\mathrm{general}}(\delta)
\ge c\exp\!\left(c\sqrt{\log(1/\delta)}\right).
$$

The target uses only $g=\pm\sqrt W$, with mass $1/2$ at each sensitivity level, and all nonzero internal relaxation rates in $[k,3k]$. The lower bound applies to arbitrary finite-state Markov competitors with fixed readout and preparation. It uses only two field values, $0$ and a fixed $h_*>0$, and held intervals that are integer multiples of $1/(8k)$. It therefore does not rely on arbitrarily fast target modes or increasingly rapid control switching.

The construction embeds a binary tree in hidden function space. Its positive reversible physical generator produces a controlled Hankel matrix with $2^n$ independent directions, while the cubic kernel has only $n+1$ modes. Logarithm polynomials of fixed-duration propagators transfer that rank witness to actual mean errors without requiring derivative bounds on a competitor. This gives the exact comparison $D_{\mathrm{cubic}}=n+3$ and $2^n\le D_{\mathrm{full\ controlled}}\le2^{n+1}+1$, as well as a separate finite-error lower bound. The cubic minimum is in the established analytic-in-field Markov class; the full controlled lower bound allows broader competitors.

The [reversible general upper theorem](REVERSIBLE_GENERAL_COMPRESSION.md) returns a surrogate in the same family, with exact variance $W$ and sensitivity bound $G$, for every target and every positive tolerance. At fixed $G,H$ its sufficient state count is

$$
D(\delta)\le\exp\!\left\{\exp\!\left[C_{G,H}\log^2(16/\delta)\right]\right\}.
$$

It preserves the passive law, equilibrium curve, and linear/quadratic mean responses exactly, while controlling the actual mean uniformly over all allowed protocols and horizons. Existence of such structure-preserving compression is settled; its optimal cost is not. The earlier finite-word upper construction remains a useful precursor, but its nonreversibility and variance error are no longer limitations of the strongest existence theorem.

### The rank-one subclass has a sharp answer

The [sharp finite-field theorem](FINITE_FIELD.md) concerns a smaller target subclass. That subclass has one hidden state of stationary mass $1/2$ and sensitivity $+\sqrt W$, while all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel of mass $W$ has a realization in this subclass. This is an additional actuator-geometry restriction, not a generic statement about every centered bounded sensitivity vector.

For fixed $k,W,H>0$, the approximation norm measures the **actual mean** over all protocols $|h(t)|\le H$ and all horizons. The worst-case state requirement is $\Theta(\log^2(1/\delta))$, or $\Theta(\log(1/\delta))$ when active target rates are at most $3k$. Reversible surrogates retain the exact passive law and specified lower-order responses. The lower bound permits arbitrary instantaneous-field Markov predictors, with a fixed readout and preparation; they need not have analytic rates or satisfy any passive-data constraint.

For unrestricted rates, the lower order already holds for [one fixed step](FIXED_FIELD_LOWER_BOUND.md) with amplitude $h_* = \min\{H,[20(1+\sqrt W)]^{-1}\}$, independent of the state budget and tolerance. The proof uses the exact positive spectral expansion of the finite-field step mean and the rank of any competing Markov curve. It does not infer a derivative bound from a small real-field error.

The exact kernel closure is special. An explicit four-state counterexample in the finite-field note holds $k,\mu,g$, and the cubic kernel fixed while changing a higher response through $K$. This is a demonstrated boundary of the result, rather than an omitted genericity assumption.

### Cubic coefficients in the broader original family

Fix the target family, scalar field rule, stationary preparation, binary readout, bounded sensitivity, and coefficient norm in [Finite accuracy, Section 0](FINITE_ACCURACY.md#0-the-approximation-task-and-its-quantifiers). The intervention kernel is supplied exactly. One reduced model must work for every bounded protocol and every finite horizon.

The comparison can be strengthened beyond the original formulation. A relaxed competitor need only be a stationary-prepared analytic finite-state Markov model with a fixed real-valued readout; it need not reproduce the passive law or any lower-order response. Even in that relaxed class, the cubic-only approximation task has the same worst-case state-growth order as a reversible model that preserves all the prescribed agreements and the sensitivity bound:

| Target information, fixed positive $WU^3$ | Relaxed Markov fit to the cubic coefficient alone | Reversible fit preserving the prescribed structure |
|---|---|---|
| Unrestricted active rates | $\Theta(\log^2(WU^3/\varepsilon))$ | $\Theta(\log^2(WU^3/\varepsilon))$ |
| Active rates at most $3k$ | $\Theta(\log(WU^3/\varepsilon))$ | $\Theta(\log(WU^3/\varepsilon))$ |

The [structure-cost corollary](STRUCTURE_COST.md) proves this comparison. For unrestricted rates, the existing lower proof already applies to the relaxed class. For capped targets, filtering still cannot increase the coefficient-lift rank, so replacing the earlier witness mode count by $r=3D-1$ gives the required relaxed lower bound. The existing upper constructions retain all the structure.

Thus preservation does not increase the **asymptotic order** of the required state count in this family. This does not identify equal errors at a fixed state budget or equal leading constants. The relaxed competitor is judged only on its cubic coefficient; it may have incorrect passive behavior or lower-order mean response. The theorem does not say that arbitrary positive systems, physical constraints, or finite-amplitude predictions have no cost.

The exact two-versus-$N$ theorem remains the motivating zero-tolerance limit. These coefficient results support the finite-field theorem and continue to apply to a broader target family.

## 2. What a model builder can use

The intended use is compression after a microscopic model is known. Choose a field bound and an actual-mean tolerance. Both the sharp subclass construction and the general reversible construction return one Markov model with a certificate valid across that protocol class and all horizons, without refitting it for each waveform. They retain the complete passive binary path law, equilibrium curve, reference linear mean, and zero quadratic mean. The general construction also restores exact sensitivity variance, but its very large worst-case size bound is an existence result rather than a practical reduction recommendation. In the rank-one subclass, supplying the scalar kernel suffices; a general actuator can require more information.

State count measures the number of latent Markov states. It does not charge parameter precision, computing the spectral measure, fitting data, or running the resulting simulator. The worst-case lower bound is a limit on model dimension, not an experimental sample count or a wall-clock runtime bound.

For the rank-one subclass, the rate cap supplies additional information about active hidden relaxation times relative to the visible switching time $1/k$; it changes the sharp state order from squared logarithmic to logarithmic. The earlier unrestricted-rate witnesses use increasingly fast modes. The new general-family witnesses instead keep every internal relaxation rate in $[k,3k]$: their larger cost arises from controlled evolution that accesses many independent hidden directions. A relaxation-rate cap and a restriction on control switching are separate assumptions; the new lower bound already permits a fixed minimum dwell time.

The actuator must be specified kinetically. Local detailed balance fixes rate ratios but does not uniquely fix how barriers change. Within a comparison at fixed state labels, the target models can keep $k,\mu,g$ and the displayed field rule unchanged while changing only the internal generator $K$. Their complete microscopic generators are therefore different. A surrogate may use a different internal realization, but receives the same scalar protocol $h(t)$.

### What an observer can measure

The [path-response theorem](ACTIVE_PATH_RESPONSE.md) shows that all first-order visible-path responses are universal in the original family, whereas their second-order response is exactly characterized by $C$. A no-exit experiment gives a sharp $r+2$ state count without the cubic mean's resonance exception. For a specified pair, two snapshots attain $\Theta(h^{-4})$ weak-step discrimination trials, compared with $\Theta(h^{-6})$ for the final snapshot alone. This is a fixed hypothesis-testing task, not a general kernel-learning theorem. Preparation cost is excluded.

The [near-lumpability theorem](NEAR_LUMPABILITY.md) considers centered perturbations of external equilibrium conductances. Complete passive paths have relative entropy at most $q^4(152+241kT)$ from the telegraph law, uniformly over hidden dimension and internal rates. A three-state pair attains the quartic information scale and retains a finite active mean separation. It supplies a quantitative neighborhood of the ideal passive degeneracy, with explicit perturbation restrictions; it does not assert robustness to every microscopic change.

## 3. A diagnostic boundary: switching the field off versus keeping it on

The model provides an exact operational example without a molecular implementation claim. Prepare it in its stationary distribution at a constant field $h_0$, then switch the field to zero. Strong passive lumpability gives

$$
m_{\mathrm{off}}(t)=\tanh(h_0)e^{-2kt}
$$

for every internal generator $K$. In fact, the entire visible path law after switch-off is the same telegraph law with that initial mean. This statement is exact at finite $h_0$, because the post-switch dynamics use the zero-field generator.

For comparison with the perturbation-arrest relation of [Engbring et al.](PRIOR_ART.md#established-response-theory), the visible stationary-density ratio minus one is $z(S)=\tanh(h_0)S$. Both its passive autocorrelation and its switch-off mean are $\tanh^2(h_0)e^{-2kt}$. Passing that diagnostic is consistent with the genuinely Markovian zero-field visible process; it does not certify the model while the field remains on.

To see the distinction with fixed actuator parameters, take two three-state targets with $\mu=(1/2,1/2)$, $g=(\sqrt W,-\sqrt W)$, and internal flip rates $k/2$ and $3k/2$. Their kernels are $We^{-kt}$ and $We^{-3kt}$. Their passive laws, equilibrium curves, linear mean responses, quadratic mean responses, and stationary-preparation switch-off laws agree. Under the constant protocol $u=U$, however, the existing step formula gives

$$
m_{3,\lambda=3k}[U](1/k)-m_{3,\lambda=k}[U](1/k)
=\frac{WU^3}{2}(e^{-2}-e^{-4})>0.
$$

Thus even these ideal calibration records do not specify the cubic field-on response. Supplied intervention information remains necessary for the constructive compression task. The displayed difference concerns Taylor coefficients; it is not a uniform finite-amplitude error guarantee or a noise-certified inference procedure.

## 4. Theorem-by-theorem comparison

The [source audit](PRIOR_ART.md) gives bibliographic links, versions, access depth, and fuller qualifications. The table records the operative mathematical differences rather than treating a different name or error norm as a novelty argument.

| Inspected result | Resource and guarantee | Consequence for this project |
|---|---|---|
| Basu et al. (2015), Sections III.1 and IV.1; Diezemann (2012), Eqs. (4)–(5), (25) | Nonlinear response under specified kinetic perturbations; no state-budget minimax theorem. | Passive agreement with different nonlinear response is established. Cubic order and kinetic dependence are not the contribution. |
| Müller et al. (2020), Eq. (30), Sections II–IV | Coarse joint-probability derivatives reconstruct arbitrary-protocol second-order response. | Establishes coarse response reconstruction, without a sharp cost in physical Markov states. |
| Cardelli et al. (2023), Theorems 2, 5–6 | Partition reduction; pointwise lumpability or extremal values under interval-rate controls. | Pointwise lumpability explains our passive construction. Corresponding uncertain controls need not be the same actuator realization. |
| Petreczky (2011), Theorem 2.3; Benner–Goyal (2017), Theorems 3.1–3.2 and 4.5 | Exact bilinear realization by Hankel rank, or Volterra/Gramian reduction in real state coordinates. | The coefficient lift is standard. Its signed coordinates are not physical Markov states; independent lifted inputs would also change the task. |
| Becker–Hartmann (2019), Definition 3.2, Corollary 3.3, Theorems 1–2 | State-factored Volterra Hankel operators and output bounds under stated stability/input assumptions. | Establishes the factorization framework. Our constant-step argument obtains a rank obstruction without imposing those input conditions on every surrogate. |
| Kotsalis–Shamma (2015), Definitions 2.1–2.3, Theorem 4.2; indexed primary excerpts | Stationary HMM word probabilities and a lower-order Hankel-norm obstruction. | Establishes the stochastic rank mechanism. The passive word law here already has an exact two-state realization; response derivatives require an additional construction. |
| Reis–Virnik (2009), Theorems 3.1–3.2 | Stable positive LTI reduction with an $H_\infty$ error bounded by an instance-dependent balancing tail. | Preserving positivity is established; a uniform tolerance-to-state law and the passive-equivalent reversible field family remain separate requirements. |
| Balle–Panangaden–Precup (2015), Theorem 2 and Section 3 | Word-Hankel rank and forward--backward factorization for real weighted automata. | The controlled rank mechanism is established; the positive physical target and quantified mean-error conversion are additional requirements. |
| Marin–Rossi (2017), Corollary 3; Fornace–Lindsey (2025 v3), Proposition 4.1 and Theorems 3/3* | Reversible quotient generators and autonomous semigroup compression with instance-dependent error bounds. | Reversible compression itself is prior art; one uniform controlled surrogate, exact actuator variance, and a size-independent state count require separate proof. |
| Gesztesy–Simon (1997), Theorem 3.5 / Appendix A.6 | A positive finite spectral measure determines a Jacobi matrix. | Our reversible kernel realization is a direct corollary, not new inverse-spectral theory. |
| Koyama (2023 v3), Theorems 2.14 and 3.14 | Positive, mass-preserving exponential approximation on a spectral interval. | Clamping and the response estimate yield our upper order. The upper approximation mechanism is already known. |
| Lacroce et al. (2024), Theorems 2 and 16; Fasino (2023), Section 2.1 | Hankel rank/singular-value obstruction and explicit Cauchy inversion. | These supply classical lower-bound tools. The target construction and response-norm estimate make them applicable here. |
| Chowdhury (2026 v1), Appendix K.1, Proposition 2 | Autonomy of entropy-selected hidden dynamics despite exact ordinary visible-law agreement. | Closest complete-passive-law conceptual comparison; trajectory selection differs from our reversible scalar-field response and state-cost question. |

Two reductions are particularly important. First, the Taylor hierarchy becomes bilinear after replacing $u$ by the constrained triple $(u,u^2,u^3)$, and becomes a linear autonomous system under a constant protocol. No new general realization theorem is needed for that step. Second, Koyama's positive quadrature plus rate clamping already gives the upper asymptotic order; the explicit dyadic proof improves transparency and constants, not the mechanism.

The passive-HMM comparison can be made exact. At any fixed sampling interval, every target has the same visible word probabilities as the two-state telegraph model. An operator formed solely from those probabilities is therefore identical for the target and the two-state model. Its approximation error is zero even when driven predictions differ. The cubic lower bound uses a coefficient lift. The new general lower bound instead constructs a matrix from fixed-amplitude controlled means, using polynomials of finite-time propagators and bounding their coefficient sums. Both use established rank reasoning, but require a separate connection to the particular intervention task.

The binary-tree lower bound does not claim a new controlled-realization or matrix-logarithm principle. Its substantive requirements are the positive reversible physical embedding, binary bounded sensitivity, fixed internal rate band, quantitative transfer to the actual controlled-mean norm, and fixed minimum control dwell time. The general upper bound likewise uses established conditional expectation, Galerkin, and moment-matching ideas; it must be assessed for its uniform guarantee and preservation of the original model constraints.

A norm distinction alone is insufficient. For a scalar nonnegative impulse error, its $L_1$ norm equals the zero-frequency gain and its $H_\infty$ norm. Positive-system truncation can therefore sometimes transfer into a kernel estimate. A signed error need not have that property. The missing conclusion from the positive-reduction result is the full uniform complexity and constrained realization statement, not an assertion that its norm can never be useful.

## 5. Assessment and next scientific question

The research now has the following distinct conclusions.

| Question | Result | Essential limitation |
|---|---|---|
| Can general finite-field prediction retain a logarithmic or squared-logarithmic state law? | [Controlled lower bound](GENERAL_CONTROLLED_LOWER_BOUND.md): no; worst-case states exceed every fixed power of the logarithm, already for binary sensitivities and fixed internal rate band and control dwell time. | The exponent is a lower bound, not the optimal general order; its signed measurement combinations can be poorly conditioned. |
| How different can cubic and full controlled prediction be? | The same binary-tree family needs exactly $n+3$ states for cubic response and between $2^n$ and $2^{n+1}+1$ for full controlled means. | This is an exact task comparison; the separate finite-error theorem supplies the quantitative tolerance statement. |
| Can finite-field approximation preserve the original physical structure? | [Reversible general compression](REVERSIBLE_GENERAL_COMPRESSION.md): yes, including exact variance $W$, bounded sensitivity, and the prescribed passive/static/low-order agreements, with a double-exponential sufficient count. | The upper bound is far from the lower bound; no equality of optimal reversible and unrestricted state costs is proved. |
| Can any fixed response order give complete intervention information? | [Fixed-actuator hierarchy](FIXED_ACTUATOR_HIERARCHY.md): arbitrarily many mean and path response orders can agree with the actuator fixed between models. | The first separating signal may shrink; that theorem alone supplies no finite-error state lower bound. |
| What information is complete for driven visible paths? | [Actuator-process equivalence](ACTUATOR_PROCESS.md): the stationary law of $g(X_t)$, with a matrix-return closure for finite actuator rank. | No stable noisy recovery or mean-only necessity is established. |

The candidate publication story is now that passive compression, low-order response, and full controlled prediction have demonstrably different physical state costs. A sharp rank-one theorem, a larger general lower bound, and a structure-preserving general upper theorem give a substantive mathematical account of that distinction. The full general law remains open, so the project must not present these bounds as a completed minimax characterization.

The next mathematical priority is to **narrow the general-family complexity gap**, especially the upper bound, while maintaining the actual controlled-mean norm and counting every physical state. Reversibility and exact variance no longer obstruct existence; whether retaining them changes the optimal order remains unresolved. Binary sensitivity is already enough for the new lower bound, so a generic two-level closure cannot recover the rank-one complexity law.

The constructor receives a known target. The observation results concern separate specified-model tests with ideal preparation and readout. No experimental platform or large simulation is required for the current theory question. Publication originality and a journal target remain separate assessments. Manuscript writing remains on hold.
