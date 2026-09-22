# Publication scope and closest-theorem comparison

[Repository overview](../README.md) · [Source audit](PRIOR_ART.md) · [Structure-cost proof](STRUCTURE_COST.md) · [Current work order](../work_orders/CURRENT.md)

**Assessment, 22 September 2026.** Retain the project as a narrowly framed theorem about the state cost of nonlinear-response model reduction. The candidate contribution is the compatibility of optimal-order cubic approximation with reversible Markov dynamics and exact passive and low-order response agreements. It is not the discovery that hidden kinetics affect nonlinear response, a new general realization theorem, or a new root-exponential approximation mechanism.

The inspected results establish the individual ingredients but do not directly state the combined constrained-response conclusion below. That is a specific comparison result, not a certification that the conclusion is new in the entire literature. Manuscript writing remains on hold while the final contribution and significance assessment is completed.

## 1. The precise candidate theorem

Fix the target family, scalar field rule, stationary preparation, binary readout, bounded sensitivity, and coefficient norm in [Finite accuracy, Section 0](FINITE_ACCURACY.md#0-the-approximation-task-and-its-quantifiers). The intervention kernel is supplied exactly. One reduced model must work for every bounded protocol and every finite horizon.

The comparison can be strengthened beyond the original formulation. A relaxed competitor need only be a stationary-prepared analytic finite-state Markov model with a fixed real-valued readout; it need not reproduce the passive law or any lower-order response. Even in that relaxed class, the cubic-only approximation task has the same worst-case state-growth order as a reversible model that preserves all the prescribed agreements and the sensitivity bound:

| Target information, fixed positive $WU^3$ | Relaxed Markov fit to the cubic coefficient alone | Reversible fit preserving the prescribed structure |
|---|---|---|
| Unrestricted active rates | $\Theta(\log^2(WU^3/\varepsilon))$ | $\Theta(\log^2(WU^3/\varepsilon))$ |
| Active rates at most $3k$ | $\Theta(\log(WU^3/\varepsilon))$ | $\Theta(\log(WU^3/\varepsilon))$ |

The [structure-cost corollary](STRUCTURE_COST.md) proves this comparison. For unrestricted rates, the existing lower proof already applies to the relaxed class. For capped targets, filtering still cannot increase the coefficient-lift rank, so replacing the earlier witness mode count by $r=3D-1$ gives the required relaxed lower bound. The existing upper constructions retain all the structure.

Thus preservation does not increase the **asymptotic order** of the required state count in this family. This does not identify equal errors at a fixed state budget or equal leading constants. The relaxed competitor is judged only on its cubic coefficient; it may have incorrect passive behavior or lower-order mean response. The theorem does not say that arbitrary positive systems, physical constraints, or finite-amplitude predictions have no cost.

The exact two-versus-$N$ theorem remains the motivating zero-tolerance limit. The finite-accuracy statement is the main resource result: microscopic target size alone does not determine the required reusable model size.

## 2. What a model builder can use

The intended use is compression after a microscopic model or intervention kernel is known. Choose a protocol-amplitude bound and a cubic-coefficient tolerance. The construction returns a smaller reversible Markov model with a certificate valid across that protocol class, without refitting it for each waveform. It retains the complete passive binary path law, the equilibrium curve, the dynamic linear mean response, and zero quadratic mean response.

State count measures the number of latent Markov states. It does not charge parameter precision, computing the spectral measure, fitting data, or running the resulting simulator. The worst-case lower bound is a limit on model dimension, not an experimental sample count or a wall-clock runtime bound.

The rate cap supplies additional information about active hidden relaxation times relative to the visible switching time $1/k$. It is not a lower bound on the hidden spectral gap, a cap on every microscopic transition, or a bandwidth restriction on the controller. Without a cap, the hard targets have increasingly fast active modes while their slowest active rate stays at $5k/2$.

The actuator must be specified kinetically. Local detailed balance fixes rate ratios but does not uniquely fix how barriers change. Within a comparison at fixed state labels, the target models can keep $k,\mu,g$ and the displayed field rule unchanged while changing only the internal generator $K$. Their complete microscopic generators are therefore different. A surrogate may use a different internal realization, but receives the same scalar protocol $h(t)$.

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
| Gesztesy–Simon (1997), Theorem 3.5 / Appendix A.6 | A positive finite spectral measure determines a Jacobi matrix. | Our reversible kernel realization is a direct corollary, not new inverse-spectral theory. |
| Koyama (2023 v3), Theorems 2.14 and 3.14 | Positive, mass-preserving exponential approximation on a spectral interval. | Clamping and the response estimate yield our upper order. The upper approximation mechanism is already known. |
| Lacroce et al. (2024), Theorems 2 and 16; Fasino (2023), Section 2.1 | Hankel rank/singular-value obstruction and explicit Cauchy inversion. | These supply classical lower-bound tools. The target construction and response-norm estimate make them applicable here. |
| Chowdhury (2026 v1), Appendix K.1, Proposition 2 | Autonomy of entropy-selected hidden dynamics despite exact ordinary visible-law agreement. | Closest complete-passive-law conceptual comparison; trajectory selection differs from our reversible scalar-field response and state-cost question. |

Two reductions are particularly important. First, the Taylor hierarchy becomes bilinear after replacing $u$ by the constrained triple $(u,u^2,u^3)$, and becomes a linear autonomous system under a constant protocol. No new general realization theorem is needed for that step. Second, Koyama's positive quadrature plus rate clamping already gives the upper asymptotic order; the explicit dyadic proof improves transparency and constants, not the mechanism.

The passive-HMM comparison can be made exact. At any fixed sampling interval, every target has the same visible word probabilities as the two-state telegraph model. An operator formed solely from those probabilities is therefore identical for the target and the two-state model. Its approximation error is zero even when their driven cubic responses differ. To obtain the response obstruction, the field-dependent family must first be represented through its Taylor coefficients and the resulting operator error related to the response norm. The existing coefficient-lift proof performs those steps; passive HMM approximation alone does not.

A norm distinction alone is insufficient. For a scalar nonnegative impulse error, its $L_1$ norm equals the zero-frequency gain and its $H_\infty$ norm. Positive-system truncation can therefore sometimes transfer into a kernel estimate. A signed error need not have that property. The missing conclusion from the positive-reduction result is the full uniform complexity and constrained realization statement, not an assertion that its norm can never be useful.

## 5. Assessment and remaining uncertainty

The defensible scope is a model-reduction theorem in stochastic response theory: a universal family of positive relaxation kernels can be represented behind an exactly compressed passive process, and its optimal cubic approximation order is achievable while retaining reversibility, bounded sensitivity, and the prescribed passive and low-order response agreements. The lower obstruction already holds without demanding those agreements. Consequently the logarithmic exponents should not be described as a penalty caused by preserving the passive law.

The exact equal-escape condition and centered sensitivity are deliberate model choices. They isolate the question cleanly; they are not claimed to be generic properties of coarse molecular dynamics. The kinetic barrier rule is thermodynamically consistent but is extra physical specification beyond local detailed balance. The known-kernel and coefficient-error assumptions define the computational task. These limitations belong in the theorem statement and operational interpretation, rather than being repaired by adding unrelated assumptions.

The current evidence supports retaining this combined theorem for a focused publication assessment. It does not support a broad new physical law, a general result that positivity is free, or a journal-level significance claim. No experimental platform is asserted or needed to establish the present mathematical theorem.

The remaining closest-theorem question is precise: does existing stochastic realization or positive approximation theory already provide, for an arbitrary finite positive relaxation measure, a reversible bounded-sensitivity analytic Markov family with the same binary passive path law and prescribed low-order response, together with the matching broad-surrogate complexity bound in this bounded-protocol coefficient norm? A direct reduction providing all of those steps would settle the contribution assessment. A theorem addressing only unconstrained realization, only passive HMM approximation, or only kernel quadrature supplies an ingredient rather than the whole statement.

The original Frazho article remains a full-text access gap, but the inspected Petreczky theorem already makes the classical exact-realization comparison concrete. Kotsalis–Shamma's central definitions and lower-bound statement were checked through indexed primary-manuscript excerpts; the complete PDF remains unavailable. These access limits are documented rather than used as novelty arguments. The current assessment is a conditional go for a focused model-reduction contribution, with no claim of certified originality or journal suitability. Further work should test the specific combined implication above and its modeling value, rather than restart an unrestricted bibliography search or optimize constants without a scientific reason.
