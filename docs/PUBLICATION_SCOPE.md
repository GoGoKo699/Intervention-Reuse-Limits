# Publication scope and closest-theorem comparison

[Repository overview](../README.md) · [Source audit](PRIOR_ART.md) · [Structure-cost proof](STRUCTURE_COST.md) · [Current work order](../work_orders/CURRENT.md)

**Expanded research assessment, 22 September 2026.** The central candidate is now a quantitative distinction between passive observation, constant-field steps, and switching. Over the same binary target class with internal rates in $[k,3k]$, these tasks need exactly two states, $\Theta(\log(1/\delta))$ states, and $\delta^{-\Theta(1)}$ states respectively. One common predictor handles all constant amplitudes and times. Switching requires polynomial cost even with any fixed positive control clock. Its lower and upper exponents are not matched.

The constant-step upper now preserves real-analytic field dependence as well as reversibility, irreducibility, stationary zero-field preparation, the exact passive path law and static mean, a uniform full-generator spectral band, and the universal linear and zero quadratic mean responses. It need not obey the target's exponential rate rule, and field derivatives are not uniformly bounded in tolerance. For switching, a uniform positive density moment now permits polynomial reversible compression inside the original field-rule family, allowing unbounded individual density values. With a spectral cap alone, the available reversible upper is singly exponential and polynomial sufficiency remains open. The broader bounded-sensitivity family still has a double-exponential reversible existence bound. The sharp rank-one theorem remains a resolved special case, and the cubic, path-information, and robustness results remain foundations and operational consequences.

The candidate contribution is the polynomial controlled-word obstruction and its realization as a positive reversible physical Markov model with an exactly simple passive law, together with quantitative transfer to actual controlled-mean errors at fixed clock resolution. The de Bruijn/Walsh representation, logarithm expansions, interpolation, Markov word approximation, and rank mechanisms are established. The comparisons below distinguish those ingredients from the combined physical prediction theorem; they do not certify originality. Manuscript writing remains on hold during research development.

## 1. Controlled state cost and the sharp subclass

### Every constant-field step can have a small common model

The [constant-step compression theorem](CONSTANT_STEP_COMPRESSION.md) and its [analytic strengthening](ANALYTIC_CONSTANT_STEP_COMPRESSION.md) apply to every original bounded-sensitivity target with internal spectral cap $\Lambda k$, without a finite-alphabet assumption. Reversibility and the equilibrium tilt express each step mean as $\tanh(h)[1-\phi_h(t)]$, where $\phi_h$ is a positive exponential mixture supported in the uniform interval $[k/R,2k(\Lambda+R)]$. Positive quadrature needs only $O(\log(1/\delta))$ modes. A two-block Jacobi realization, a commuting stationary reset, and a fixed preparation perturbation make these mixtures into one physical Markov predictor with a common state space, binary readout and stationary zero-field preparation.

For the binary band $[k,3k]$, the existing capped rank-one lower witnesses establish the matching logarithmic order for the menu of all constant amplitudes. Their witnessing amplitude can shrink with state budget; no fixed-amplitude capped lower is inferred. Combining this with the switching theorem gives:

| Common target class | Passive path | All constant steps | Switching, including any fixed clock |
|---|---|---|---|
| Centered binary sensitivity, internal band $[k,3k]$ | $2$ exactly | $\Theta(\log(1/\delta))$ | $\delta^{-\Theta(1)}$ |

The comparison uses the same broad instantaneous-field competitor class and the actual-mean norm for the two intervention tasks. The analytic step upper additionally preserves the stated structure and real-analytic field dependence, but does not impose the original field rule or a uniform bound on field derivatives or function-description complexity. It does not claim that any fitted constant-step model predicts switching accurately. The shift-register witnesses themselves have the logarithmic step upper and polynomial switching lower.

The analytic strengthening regularizes the positive spectral measure by a small fixed reference measure, ensuring nondegenerate moment matrices. Two active Jacobi blocks have analytically varying positive root masses; their stationary law at zero provides the common preparation. A commuting interpolation with stationary refresh calibrates the exact passive law at zero. The interpolation starts at second order in the field and its zeroth-order correction annihilates the preparation, so the universal linear mean and zero quadratic mean hold for every weak protocol. These changes retain the logarithmic state order and remove the earlier discontinuity. They do not provide full switching accuracy.

### Bounded binary targets: lower and upper bounds

Fix $k,W,H>0$, put $s=\sqrt W$, and consider the original targets with $g=\pm s$ and nonzero internal relaxation rates in $[k,3k]$. Centering fixes the stationary mass at each sensitivity level to $1/2$. Let $D_*^{\rm bin}(\delta)$ be the worst-case state count over this target class, with the actual-mean error taken over all bounded protocols and horizons. Competing Markov predictors have a fixed preparation and readout; they need not be reversible, analytic in the field, or calibrated to passive data.

The [polynomial controlled-word lower theorem](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) and [bounded-rate upper theorem](BOUNDED_RATE_FINITE_FIELD.md) give, for sufficiently small $\delta$,

$$
\boxed{c\delta^{-\gamma}
\le D_*^{\rm bin}(\delta)\le C\delta^{-p},
\qquad \gamma,p>0,}
$$

where a sufficient exponent is

$$
p=\frac{\log2}{\log(1+1/(3R_s))},\qquad R_s=e^{(1+s)H}.
$$

The lower witnesses lie in the narrower band $[3k/2,5k/2]$ and use only $0$ and one fixed $h_*>0$. Their positive reversible shift-register generator supplies exponentially many independent controlled directions. Truncating the logarithm expansion by total degree across each complete left or right word transfers this controlled matrix rank to actual-mean error with only exponential coefficient cost in word length. It uses no bound on a competitor's generator or field derivatives. The conclusion $D_*^{\rm bin}(\delta)=\delta^{-\Theta(1)}$ specifies a polynomial growth class, with fixed positive lower and upper exponents; it does not identify a matched exponent or an exact power law.

The upper construction uses exact Poisson-clock uniformization, a stationary finite-order word chain, and coupling renewed at returns to $A$. Its stationary actuator histogram is exactly the target's, so the sensitivity values, all moments, passive law, equilibrium curve, and linear/quadratic mean responses are retained. Its internal dynamics may be nonreversible. It serves every allowed protocol and horizon, rather than fitting each control sequence separately.

### The polynomial obstruction survives any fixed control clock

For any fixed $a>0$, use only fields $0,h_*$ and require every positive-duration held segment to be an integer multiple of $a/k$. If $D_{*,a}^{\rm bin}(\delta)$ denotes the corresponding worst-case state count on this smaller experiment menu, the same shift-register targets give

$$
D_{*,a}^{\rm bin}(\delta)\ge c_a\delta^{-\gamma_a},
\qquad \gamma_a>0.
$$

Witnessing experiments have total duration $O_a(\log(1/\delta)/k)$. The polynomial upper serves all protocols and horizons, so the fixed-clock task also has the growth class $\delta^{-\Theta(1)}$. Allowing arbitrary segment durations at least $a/k$ only enlarges this menu and retains the conclusion. Constants and the lower exponent can depend on the fixed clock spacing. The proof uses signed combinations of many mean experiments and may have large coefficients. It establishes a state-dimension obstruction; no statistical sample bound is proved here.

The [earlier shift-register note](SHIFT_REGISTER_LOWER_BOUND.md) retains the original physical construction and the weaker transfers $\exp(cL/\log L)$ without a timing restriction and $\exp(c_aL^{2/3})$ with fixed minimum dwell, where $L=\log(1/\delta)$. Whole-side total-degree truncation strengthens both bounds without changing that target or its controlled Gram witness.

The earlier [binary-tree construction](GENERAL_CONTROLLED_LOWER_BOUND.md) remains a useful foundation. Within that family, the exact cubic response needs $n+3$ states while full controlled prediction requires between $2^n$ and $2^{n+1}+1$. The shift register has a related exact comparison: $4n+5$ states suffice and are necessary for cubic response, while the full controlled mean needs at least $2^n$. The polynomial theorem now places this comparison at precisions $\delta_n=\tfrac12e^{-C_a(n+1)}$: exact cubic prediction costs $O(\log(1/\delta_n))$ along a sequence where full controlled prediction requires a positive power of $1/\delta_n$. The cubic minima use the analytic-in-field Markov class; the full controlled lower bounds allow broader competitors.

### Reversible predictors and the broader general family

For at most $m$ actuator values and internal relaxation rates at most $\Lambda k$, put

$$
R=e^{(1+G)H},\qquad
p_{m,\Lambda,G,H}=\frac{\log m}{\log(1+1/(\Lambda R))}.
$$

The [reversible bounded-rate construction](BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) gives

$$
D_{\rm rev}(\delta)
\le\exp\!\left[C\delta^{-p_{m,\Lambda,G,H}}\log(2/\delta)\right].
$$

It preserves the exact stationary actuator histogram and the target's spectral band, including any specified positive lower gap. It therefore preserves variance $W$, sensitivity bound $G$, and every prescribed passive/static/low-order agreement, with ordinary detailed balance. The polynomial nonreversible and singly exponential reversible upper bounds do not prove an optimal reversibility penalty. A polynomial reversible upper bound remains open.

There is now a sufficient structural condition for a polynomial reversible upper. Suppose $K_{ij}/\mu_j\le Lk$ for $i\ne j$, with fixed $L$. For a fixed alphabet of $m$ actuator values, [stratified reversible sampling](BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) gives $D_{\rm rev}(\delta)\le C\delta^{-2(1+p_L)}\log^3(2/\delta)$, where $p_L=\log m/\log(1+1/(LR))$. Sampling within each actuator level preserves its stationary mass exactly; symmetric sampled transition weights and a small reset retain positivity and ordinary reversibility. Concentration on finitely many word-prediction functions, followed by regeneration, gives the all-protocol/all-horizon mean bound. This model uses the original field rule and has internal spectral cap $2Lk$, without a claim to preserve the original gap or band. The density assumption is stronger than a spectral cap, so this theorem leaves the main cap-only question open.

The [density-moment extension](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) weakens the pointwise condition. For dimensionless $q_{ij}=K_{ij}/(k\mu_j)$ off the diagonal and $q_{ii}=0$, assume $\sum_{i,j}\mu_i\mu_j q_{ij}^{1+a}\le M$ for some fixed $a>0$. At internal cap $\Lambda k$, its sufficient count is $C\delta^{-[2(1+p_\Lambda)+1/a]}\log^3(2/\delta)$, with $p_\Lambda=\log m/\log(1+1/(\Lambda R))$. The internal surrogate cap is $2\Lambda k$, and the original field rule and actuator histogram remain exact. A uniform occupation-density bound controls the error from clipping only the stationary removed jump flux. Bernstein concentration and one global rate rescaling keep the update clock tied to $\Lambda$, preventing the growing clipping threshold from entering the exponent. The theorem also states a more general tail-dependent bound. The spectral cap alone gives no such tail control; an exactly compressible matching example rules out that shortcut.

For arbitrary bounded $g$ and unrestricted internal rates, the [general reversible upper theorem](REVERSIBLE_GENERAL_COMPRESSION.md) still supplies

$$
D(\delta)\le\exp\!\left\{\exp\!\left[C_{G,H}\log^2(16/\delta)\right]\right\},
$$

inside the original family, with exact variance and sensitivity bound. This is a broader target class than the bounded finite-alphabet class above. Existence of a structure-preserving approximation is settled, while its optimal general cost is not. The earlier nonreversible finite-word upper construction remains a precursor and source of shared estimates.

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

The intended use is compression after a microscopic model is known. Choose a field bound, an actual-mean tolerance, and the structural requirements on the predictor. A finite actuator alphabet and rate cap permit a polynomial sufficient count if nonreversible internal dynamics are allowed; a larger construction retains reversibility and the whole spectral band. Arbitrary bounded actuators and unrestricted rates have the more expensive general reversible existence bound. Each construction returns one model for the full protocol class and all horizons, retaining the complete passive binary law and the prescribed static and low-order agreements. These are worst-case guarantees rather than practical runtime recommendations. In the rank-one subclass, supplying the scalar kernel suffices; the general constructors use the full target.

State count measures the number of latent Markov states. It does not charge parameter precision, computing the spectral measure, fitting data, or running the resulting simulator. The worst-case lower bound is a limit on model dimension, not an experimental sample count or a wall-clock runtime bound.

For the rank-one subclass, a rate cap changes the sharp state order from squared logarithmic to logarithmic. The controlled-word witnesses instead keep their internal spectrum in $[3k/2,5k/2]$ and obtain a polynomial cost from many controlled hidden directions. This obstruction survives every fixed positive control clock and needs only logarithmic observation horizons in inverse error. A spectral cap and finite clock resolution therefore do not reduce this broader controlled task to the rank-one state law. The bounded-rate upper bounds use the finite actuator alphabet as well as the spectral cap.

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
| Philippakis–Mallinar–Pandit–Belkin (2024), Sections 2.2–2.3 and Theorem 3.1 | Undirected de Bruijn walks, the Walsh deletion-and-shift representation, and tridiagonal spectral chains. | The shift-register graph and spectral mechanism are established; the controlled-word physical witness and polynomial actual-mean lower bound at fixed clock resolution are the candidate additions. |
| Bressaud–Fernandez–Galves (1999), Definition 2 and Theorem 4 | Canonical finite-order Markov approximation; stationary coupling convergence under additional continuity assumptions. | Short-block matching is classical. Our all-horizon mean estimate uses the physical reset and a bounded internal update clock, rather than assuming their continuity condition. |
| Marin–Rossi (2017), Corollary 3; Fornace–Lindsey (2025 v3), Proposition 4.1 and Theorems 3/3* | Reversible quotient generators and autonomous semigroup compression with instance-dependent error bounds. | Reversible compression itself is prior art; one uniform controlled surrogate, exact actuator variance, and a size-independent state count require separate proof. |
| Gesztesy–Simon (1997), Theorem 3.5 / Appendix A.6 | A positive finite spectral measure determines a Jacobi matrix. | Our reversible kernel realization is a direct corollary, not new inverse-spectral theory. |
| Koyama (2023 v3), Theorems 2.14 and 3.14 | Positive, mass-preserving exponential approximation on a spectral interval. | Clamping and the response estimate yield our upper order. The upper approximation mechanism is already known. |
| Lacroce et al. (2024), Theorems 2 and 16; Fasino (2023), Section 2.1 | Hankel rank/singular-value obstruction and explicit Cauchy inversion. | These supply classical lower-bound tools. The target construction and response-norm estimate make them applicable here. |
| Chowdhury (2026 v1), Appendix K.1, Proposition 2 | Autonomy of entropy-selected hidden dynamics despite exact ordinary visible-law agreement. | Closest complete-passive-law conceptual comparison; trajectory selection differs from our reversible scalar-field response and state-cost question. |

Two reductions are particularly important. First, the Taylor hierarchy becomes bilinear after replacing $u$ by the constrained triple $(u,u^2,u^3)$, and becomes a linear autonomous system under a constant protocol. No new general realization theorem is needed for that step. Second, Koyama's positive quadrature plus rate clamping already gives the upper asymptotic order; the explicit dyadic proof improves transparency and constants, not the mechanism.

The passive-HMM comparison can be made exact. At any fixed sampling interval, every target has the same visible word probabilities as the two-state telegraph model. An operator formed solely from those probabilities is therefore identical for the target and the two-state model. Its approximation error is zero even when driven predictions differ. The cubic lower bound uses a coefficient lift. The controlled-word lower bound instead constructs a matrix from actual means at fixed field amplitudes, using finite polynomial combinations of propagators and bounding their coefficient sums. Its strongest transfer truncates a logarithm expansion across each complete side of the matrix factorization. Both use established rank reasoning but require a separate connection to the intervention task.

Neither the earlier binary-tree construction nor the shift-register theorems claim a new rank, logarithm-series, interpolation, or spectral principle. The polynomial theorem must be assessed for its positive reversible physical target, binary actuator, bounded internal spectrum, controlled-word singular-value witness, and polynomial transfer to actual-mean error under every fixed control clock. The upper bounds likewise use established uniformization, canonical word approximation, conditional expectation, Galerkin projection, and moment matching. Their relevant claims are the state-count guarantees and exact model constraints retained under arbitrary bounded control; these require more than naming a classical construction.

A norm distinction alone is insufficient. For a scalar nonnegative impulse error, its $L_1$ norm equals the zero-frequency gain and its $H_\infty$ norm. Positive-system truncation can therefore sometimes transfer into a kernel estimate. A signed error need not have that property. The missing conclusion from the positive-reduction result is the full uniform complexity and constrained realization statement, not an assertion that its norm can never be useful.

## 5. Assessment and next scientific question

The current conclusions distinguish prediction tasks and predictor constraints.

| Question | Result | Essential limitation |
|---|---|---|
| Can all constant steps remain inexpensive while switching is hard? | [One common analytic reversible step predictor](ANALYTIC_CONSTANT_STEP_COMPRESSION.md) needs only $\Theta(\log(1/\delta))$ states in the same bounded binary class. | The original actuator rule and tolerance-independent derivative bounds are not imposed by this upper. |
| How large is the bounded binary-rate-band state requirement? | [Polynomial controlled-word lower](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) and [bounded-rate upper](BOUNDED_RATE_FINITE_FIELD.md): $c\delta^{-\gamma}\le D_*\le C\delta^{-p}$, hence $\delta^{-\Theta(1)}$. | The polynomial growth class is determined; the lower and upper exponents are not matched. |
| Does the obstruction survive a fixed control clock? | For every fixed $a>0$, two fields and segment lengths in $(a/k)\mathbb N$ retain polynomial necessity, with witnessing horizons $O_a(\log(1/\delta)/k)$. | The lower exponent depends on the clock spacing; no statistical sample bound is proved. |
| Can a bounded finite-alphabet predictor preserve reversibility and the spectral band? | Yes, with sufficient count $\exp[C\delta^{-p}\log(2/\delta)]$, retaining the exact actuator histogram. | Different upper bounds do not prove a reversibility penalty; polynomial reversible size remains open. |
| Is there a polynomial reversible sufficient condition for switching? | A [uniform positive density moment](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) gives a polynomial count inside the original field-rule family, even with unbounded density spikes. | The moment assumption is stronger than a spectral cap; only the new internal cap $2\Lambda k$ is guaranteed. |
| Can arbitrary bounded actuators be approximated inside the original physical family? | [General reversible compression](REVERSIBLE_GENERAL_COMPRESSION.md): yes, with a double-exponential sufficient count and exact $G,W$. | No finite alphabet or rate cap is assumed here; its much larger bound is not a sharp complexity law. |
| How different can cubic and full controlled prediction be? | Along the shift-register sequence, exact cubic prediction needs $O(\log(1/\delta))$ states while full controlled prediction requires a positive power of $1/\delta$. | The cubic count uses analytic-in-field competitors; the full controlled lower bound allows a broader class. |
| Can any fixed response order give complete intervention information? | [Fixed-actuator hierarchy](FIXED_ACTUATOR_HIERARCHY.md): arbitrarily many mean and path response orders can agree with the actuator fixed between models. | The separating signal may shrink; this theorem alone supplies no finite-error state lower bound. |
| What information is complete for driven visible paths? | [Actuator-process equivalence](ACTUATOR_PROCESS.md): the stationary law of $g(X_t)$, with a matrix-return closure for finite actuator rank. | No stable noisy recovery or mean-only necessity is established. |

The bounds are asymptotic at fixed physical parameters, and the upper exponent $p$ depends on the actuator alphabet, rate cap and field bound. The notation $\delta^{-\Theta(1)}$ records fixed positive lower and upper exponents, not their equality. A sharp rank-one theorem and the broader cubic results remain resolved foundations; they do not impose their logarithmic state laws on the general controlled problem.

The candidate publication story is that even a common model of every constant-field step can be much smaller than a model reusable under switching. The same bounded binary target class has passive cost two, logarithmic step cost, and polynomial switching cost, with the last obstruction surviving fixed clock resolution. The controlled-word lower and bounded-rate upper determine the polynomial growth class. The density-moment theorem gives a separate positive result for reversible switching predictors. These statements should retain their unmatched exponents and precise structural assumptions, with the classical quadrature, Jacobi, sampling, graph, logarithm-series and rank ingredients explicitly acknowledged.

The main remaining mathematical questions are the optimal bounded-binary exponent and whether the density-moment reversible upper can be extended to a spectral cap alone. The analytic constant-step construction resolves qualitative field regularity; imposing the original field rule or uniform derivative bounds would be a separate refinement. The general bounded-sensitivity upper bound can also be improved, but it concerns a broader class. The different available upper bounds do not establish an intrinsic penalty for reversibility.

The constructor receives a known target. The observation results concern separate specified-model tests with ideal preparation and readout. No experimental platform or large simulation is required for the current theory question. Publication originality and a journal target remain separate assessments. Manuscript writing remains on hold.
