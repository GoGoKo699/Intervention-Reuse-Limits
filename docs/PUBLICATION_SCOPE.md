# Publication scope and closest-theorem comparison

[Repository overview](../README.md) · [Source audit](PRIOR_ART.md) · [Structure-cost proof](STRUCTURE_COST.md) · [Current work order](../work_orders/CURRENT.md)

**Expanded research assessment, 22 September 2026.** Pursue finite-field prediction limits as the central contribution. The project now goes beyond a cubic-coefficient compression theorem: an exact two-state passive process can require a growing predictor even for one fixed nonzero intervention, with matching constructive bounds for all bounded field protocols. Separate results identify a cheaper measurement than the endpoint mean and quantify the passive information that appears when exact lumpability is broken.

The individual response, realization, dwell-time, and approximation mechanisms remain established. The more ambitious candidate is their combination into a sharp finite-field reuse theorem and a quantitative observation boundary. The source comparisons below and in the audit constrain this claim; they do not certify originality. Manuscript writing remains on hold during research development.

## 1. The finite-field theorem and its coefficient foundation

The primary result is now [the finite-field theorem](FINITE_FIELD.md). Its target subclass has one hidden state of stationary mass $1/2$ and sensitivity $+\sqrt W$, while all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel of mass $W$ has a realization in this subclass. This is an additional actuator-geometry restriction, not a generic statement about every centered bounded sensitivity vector.

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

The intended use is compression after a microscopic model or intervention kernel is known. In the finite-field subclass, choose a field bound and an actual-mean tolerance. The construction returns a smaller reversible Markov model with a certificate valid across that protocol class and all horizons, without refitting it for each waveform. It retains the complete passive binary path law, the equilibrium curve, the dynamic linear mean response, and zero quadratic mean response. For the broader original family, the existing certificate still concerns cubic coefficients.

State count measures the number of latent Markov states. It does not charge parameter precision, computing the spectral measure, fitting data, or running the resulting simulator. The worst-case lower bound is a limit on model dimension, not an experimental sample count or a wall-clock runtime bound.

The rate cap supplies additional information about active hidden relaxation times relative to the visible switching time $1/k$. It is not a lower bound on the hidden spectral gap, a cap on every microscopic transition, or a bandwidth restriction on the controller. Without a cap, the hard targets have increasingly fast active modes while their slowest active rate stays at $5k/2$.

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
| Gesztesy–Simon (1997), Theorem 3.5 / Appendix A.6 | A positive finite spectral measure determines a Jacobi matrix. | Our reversible kernel realization is a direct corollary, not new inverse-spectral theory. |
| Koyama (2023 v3), Theorems 2.14 and 3.14 | Positive, mass-preserving exponential approximation on a spectral interval. | Clamping and the response estimate yield our upper order. The upper approximation mechanism is already known. |
| Lacroce et al. (2024), Theorems 2 and 16; Fasino (2023), Section 2.1 | Hankel rank/singular-value obstruction and explicit Cauchy inversion. | These supply classical lower-bound tools. The target construction and response-norm estimate make them applicable here. |
| Chowdhury (2026 v1), Appendix K.1, Proposition 2 | Autonomy of entropy-selected hidden dynamics despite exact ordinary visible-law agreement. | Closest complete-passive-law conceptual comparison; trajectory selection differs from our reversible scalar-field response and state-cost question. |

Two reductions are particularly important. First, the Taylor hierarchy becomes bilinear after replacing $u$ by the constrained triple $(u,u^2,u^3)$, and becomes a linear autonomous system under a constant protocol. No new general realization theorem is needed for that step. Second, Koyama's positive quadrature plus rate clamping already gives the upper asymptotic order; the explicit dyadic proof improves transparency and constants, not the mechanism.

The passive-HMM comparison can be made exact. At any fixed sampling interval, every target has the same visible word probabilities as the two-state telegraph model. An operator formed solely from those probabilities is therefore identical for the target and the two-state model. Its approximation error is zero even when their driven cubic responses differ. To obtain the response obstruction, the field-dependent family must first be represented through its Taylor coefficients and the resulting operator error related to the response norm. The existing coefficient-lift proof performs those steps; passive HMM approximation alone does not.

A norm distinction alone is insufficient. For a scalar nonnegative impulse error, its $L_1$ norm equals the zero-frequency gain and its $H_\infty$ norm. Positive-system truncation can therefore sometimes transfer into a kernel estimate. A signed error need not have that property. The missing conclusion from the positive-reduction result is the full uniform complexity and constrained realization statement, not an assertion that its norm can never be useful.

## 5. Assessment and next scientific question

The project should now be developed around the finite-field prediction theorem, with the measurement and near-lumpability results explaining what the passive-versus-driven distinction means operationally. This is a stronger candidate than the earlier narrow coefficient-only compatibility statement: actual outputs are controlled uniformly, and one fixed intervention already has an optimal-order state obstruction against broad Markov predictors.

Three boundaries remain material. The finite-field upper theorem uses rank-one sensitivity geometry. The constructor receives the intervention kernel rather than learning it. The observation results quantify specified two-model tests and a specified barrier perturbation, with ideal readout and preparation. These are theorem assumptions, not established features of a particular molecular platform.

The stronger scope does not make the classical tools new. Waiting-time inference and poor identifiability near equal dwell times have longstanding precedents, while positive spectral approximation, rank-one feedback, and Hankel rank are established mechanisms. The next source comparison must address the full fixed-intervention minimax theorem, rather than merely another occurrence of one ingredient. The new audit entries record what was actually inspected and where access remains partial.

The next scientific question is whether the restrictive actuator geometry can be replaced by a broader finite-field principle, or whether a precise response-hierarchy obstruction explains why it cannot. The explicit same-kernel counterexample already rules out extending the current scalar-kernel certificate unchanged to the general family. Any further extension should state what additional intervention information is sufficient and what physical resource it costs. No additional large simulation or experimental platform is needed to investigate that question.

The recommendation is to continue this stronger research direction and keep the completed finite-field theorem as its rigorous baseline. Publication originality and a journal target remain separate assessments. Manuscript writing is on hold; the current task is to improve the scientific statement, not to inflate its framing.
