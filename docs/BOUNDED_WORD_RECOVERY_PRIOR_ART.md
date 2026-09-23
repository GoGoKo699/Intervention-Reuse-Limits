# Bounded response, actuator words and exact rank: focused source comparison

[Repository overview](../README.md) · [Actuator-process invariant](ACTUATOR_PROCESS.md) · [Rate-boundary comparison](RATE_BOUNDARY_PRIOR_ART.md)

**Research date: 23 September 2026; updated after the continuation's internal proof audits passed.** This bounded search compares the [resolvent-word observability theorem](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) and its [uncapped nineteen-level state lower bound](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) with their classical ingredients. The repository now supplies a quantitative model-specific implication from controlled single-time means to bounded hidden resolvent words. This source note does not independently prove that theorem or certify priority. The compared results concern different data and norms; their assumptions remain essential.

## 1. The precise inverse question

The original external rule is

$$
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{iA}(h)=ke^{(g_i-1)h}.
$$

The hidden generator $K$ is reversible under $\mu$, the alphabet and field interval are fixed, and each experiment starts at $\pi_0=(1/2,\mu/2)$ with the ordinary binary readout. The datum is a bound on the difference of actual means for **every** allowed protocol and horizon. The desired quantities are bounded actuator-word probabilities

$$
\mu P_{a_0}e^{Kt_1}P_{a_1}\cdots e^{Kt_m}P_{a_m}\mathbf1.
$$

These are distinct from raw generator words, whose uniform recovery is obstructed by the [rare-fast-component example](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md#5-rare-fast-states-prevent-raw-moment-transfer). The completed route controls a specific Laplace-averaged version of bounded words, described in Section 3, rather than recovering arbitrary raw generator derivatives or asserting a uniform deterministic-time word metric. Full visible path data are stronger observations: [the actuator-process note](ACTUATOR_PROCESS.md) proves their exact equivalence with the hidden actuator law. That earlier path-law argument is not the new mean-to-resolvent proof.

## 2. Inspected primary sources

| Source and inspected location | Usable result and substantive scope |
|---|---|
| Adam Gregosiewicz, *Uniform Exponential Stability of Perturbed Semigroups: The Dyson–Phillips Formula Versus Gil’s Approach Via Commutators* (2021), [publisher full text](https://link.springer.com/article/10.1007/s00025-021-01353-1), §3, equations (3.1)–(3.4) | Restates the classical Dyson–Phillips expansion for a strongly continuous semigroup perturbed by a bounded operator, attributing it to Engel–Nagel III.1.10. The semigroup growth estimate uses its growth constants and the perturbation norm, rather than the generator norm. This supports rate-independent analytic envelopes after a uniformly bounded perturbation has been established. It is a forward evolution estimate, not recovery of kernels from noisy scalar outputs. |
| Valentin A. Zagrebnov, *Operator-norm Trotter product formula on Banach spaces*, [arXiv:2205.04807v1 PDF](https://arxiv.org/pdf/2205.04807v1), Proposition 1.7, Theorems 2.6–2.7 and Corollary 2.8 | Proposition 1.7 bounds positive-time semigroup derivatives by constants times $t^{-j}$ under holomorphy. The product-formula theorems require a holomorphic contraction generator and specified domain conditions for the second contraction generator and its adjoint. The bounded-perturbation case has an $O((\log N)^2/N)$ bound, with the displayed constants and exponential time factor. These hypotheses and constants need checking before claiming uniformity over a generator family. The examples distinguish strong from operator-norm convergence. The repository needs only convergence for each fixed pair of finite models, not this quantitative splitting theorem. |
| Lloyd N. Trefethen, *Quantifying the ill-conditioning of analytic continuation*, [arXiv:1908.11097v1 PDF](https://arxiv.org/pdf/1908.11097v1), Theorems 5.1–5.3; §6 | Without a complex-domain bound, small error on a real continuum gives no bound away from it. With a common bound, Theorem 5.2 gives a geometric Hölder exponent for continuation to a fixed point; it depends on the domain and point, not the function. Cauchy estimates connect complex-neighborhood control to coefficients. The repository uses an explicit Chebyshev estimate in this classical framework, with one parameter for the whole schedule and a rate-independent envelope. The paper does not supply the physical response-to-resolvent reduction or a sampling guarantee. |
| Mihály Petreczky, *Realization theory for linear and bilinear switched systems: A formal power series approach. Part II* (2011), [publisher full text](https://www.numdam.org/item/10.1051/cocv/2010015.pdf), Theorems 2.3, 2.5–2.6, pp. 452, 455–456 | Under arbitrary switching, minimal bilinear realization dimension equals Hankel rank; finite rank plus a generalized Fliess expansion characterizes realizability. Equation (2.21) represents coefficients by matrix words. These are exact real-coordinate realizations. The statements do not supply a noisy-output inverse modulus, nonnegative rates, detailed balance, or the original actuator rule. A target-specific Walsh/Hankel calculation uses an established rank mechanism. |
| Simon Becker and Carsten Hartmann, *Infinite-dimensional bilinear and stochastic balanced truncation with explicit error bounds* (2019), [publisher full text](https://link.springer.com/article/10.1007/s00498-019-0234-8), Theorems 1–2, Definition 3.2 and Corollary 3.3 | Gives forward bounds from trace-class Hankel error to transfer-function and output error. Theorem 2 assumes zero initial state, exponential stability, a Gramian smallness condition, and bounded controls with a restricted $L^2$ energy. It is not the reverse implication from uniform bounded-control output error to hidden word data. These stability, initialization and energy restrictions cannot be dropped when comparing with arbitrary-horizon stationary experiments. |
| Lorenzo Finesso and Peter Spreij, *Approximate realization of hidden Markov chains* (2002), [author-hosted full text](https://staff.fnwi.uva.nl/p.j.c.spreij/itw.2002.1115424.pdf), §III unnumbered static-realization theorem and rank lemma; §IV | The probability matrix of past/future strings factors through the hidden states; ordinary rank is a lower bound on hidden order, while nonnegative factorization governs the static positive realization. Approximation is formulated using informational divergence of compound sequence matrices. This gives neither recovery of those matrices from controlled means nor an all-protocol CTMC approximation with the prescribed field rule. The paper attributes the stable-polyhedral-set characterization to Heller (1965). |
| Tim Austin, Assaf Naor and Alain Valette, *The Euclidean distortion of the lamplighter group*, [author-hosted full text](https://web.math.princeton.edu/~naor/homepage%20files/LAMP-official.pdf), §2.1, pp. 3–4 | Explicitly uses lamp-subgroup Walsh characters $W_A(x)=(-1)^{|A\cap x|}$ and combines them with the permutation action of the lamplighter position. This is a concrete primary precedent for the representation ingredient. Its theorem concerns Hilbert-space distortion of a cyclic lamplighter group, not Hankel rank or controlled Markov prediction. The repository's address geometry and physical scalar access still require separate proofs. |

The Petreczky and Becker–Hartmann comparisons refine sources already present in [the earlier audit](PRIOR_ART.md); the realization framework is not a new discovery of this continuation. Positive realization is stricter than unrestricted linear realization, but a rank obstruction can be applied to a positive realization because it is also a linear one. Rank alone does not construct a smaller positive or reversible model.

## 3. What the completed model-specific theorem adds

For a fixed finite alphabet $\Gamma\subset(-1,1)$, the [observability theorem](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) uses $2|\Gamma|+1$ physical fields. Both models retain the original field rule, histogram, equilibrium preparation and readout, and have reversible hidden generators. Their hidden spaces may differ; there is no lower bound on stationary masses, common dimension bound, or upper rate bound.

In units $k=1$, set $P_s=s(sI-K)^{-1}$. Uniform actual-mean error $\delta$ gives, for the specified color words,

$$
W_s=\mu D_{c_1}P_s^2D_{c_2}\cdots P_s^2D_{c_m}1,
$$

$$
|W_s-\widehat W_s|
\le C2^m3^{M+1}s^m\sqrt\delta
 +2^{m+2}6^{M+1}s^{m-M-1},
\qquad s\ge s_0,\quad M\ge m.
$$

The finite constants $C,s_0$ are fixed by the alphabet and physical field menu. The proof derives artificial absorbing, bounded signed-killing schedules from the physical means; averages independent dwell times with exponential density; and extracts a polarized Taylor coefficient by a finite Chebyshev functional. The bounded-feature version in the [state lower proof](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) includes signed endpoints. Neither source theorem in Section 2 establishes this whole physical input-output implication.

For the nineteen-level target, positive cross-port blocks of $P_s^2$, normalized by $8s$, approximate the target's gate transports. The whole-word entropy lemma then gives

$$
\delta\le e^{-C_H(n+1)^2}
\quad\Longrightarrow\quad
D\ge2^{3\cdot2^n/4}.
$$

Consequently the uncapped reversible worst-case cost is at least
$\exp(\exp(c_H\sqrt{\log(1/\delta)}))$, whereas the unrestricted class has polynomial growth. This is an intrinsic reversible state penalty under the retained original rule and histogram. The lower is weaker than $\exp(c\delta^{-\alpha})$ and is not a fixed-positive-clock theorem. The proof uses arbitrary durations, arbitrarily rapid switching and the all-horizon mean norm; $s$ is a Laplace probe frequency, not a rival rate cap.

## 4. Which ingredients are classical, and which distinctions matter

**Convexification needs only a limit for each fixed pair of models.** For finitely many allowed fields $h_j$ and probabilities $p_j$, fast periodic switching gives

$$
\left[\prod_j e^{(Tp_j/N)Q(h_j)}\right]^N
\longrightarrow e^{T\sum_jp_jQ(h_j)}
$$

for each finite model. Consequently an error bound that already holds for every ordinary switching protocol passes to the convexified experiment by taking the limit in both fixed models. No common bound on the switching frequency needed to reach that limit is required for this implication. A finite experimental implementation or a fixed minimum dwell time is a different requirement. The convexified generator need not itself belong to the original one-label exponential field family; it is an accessible limit of experiments, not automatically an admissible replacement model.

**Bounded perturbations give a uniform analytic envelope.** The actual proof uses the hidden-only generator $K_b$, extended by zero on $A$, as its contraction generator. In each model's own equilibrium Hilbert space, the external block operator satisfies $\|V(c)\|\le2\|c\|_\infty$, independently of the hidden dimension, masses and rates. The order-$j$ Dyson term for a perturbation of norm at most $B$ is bounded by $(BT)^j/j!$. This supplies the uniform complex envelope. No comparison of full hidden operators on a common space is made.

**One global continuation parameter prevents repeated loss of the accuracy exponent.** The entire artificial schedule is continued from the interior of the physical coefficient simplex with the same scalar $z$. The explicit Chebyshev split yields $Ce^{BT/2}\sqrt\delta$, with exponent $1/2$ independent of word length and segment count. After Laplace integration, the proof uses the sign average

$$
2^{-m}\sum_{\epsilon\in\{-1,1\}^m}
\left(\prod_j\epsilon_j\right)F_s(z\epsilon_1,\ldots,z\epsilon_m).
$$

Its degree-$m$ coefficient contains one bounded insertion per segment and exactly the $P_s^2$ gaps above. This normalized average has total absolute coefficient mass one; its $2^m$ summands do not introduce another error factor at that step. Polynomial interpolation and polarization are classical tools. The model-specific content includes their physical access, uniform norm bounds, normalization and quantitative combination with positive gate words.

**Positive gaps control the time regularity of bounded hidden words.** By the spectral theorem for reversible $K$,

$$
\|Ke^{tK}\|_{L^2(\mu)\to L^2(\mu)}
\le\sup_{\lambda\ge0}\lambda e^{-t\lambda}
=\frac1{et},\qquad t>0.
$$

For a word of level projectors, each of norm at most one, changing gaps from $t_j$ to $t'_j$, all at least $a>0$, changes its scalar probability by at most $\sum_j|t_j-t'_j|/(ea)$. This is a useful elementary distinction between positive-time words and raw moments at zero. It is not needed by the completed resolvent proof and does not turn that proof into a uniform deterministic-time word-recovery theorem.

**Exact Walsh rank and positive realization remain separate questions.** The [full-Walsh theorem](UNCAPPED_WALSH_OBSERVABILITY.md) uses the classical characters and rank factorization to construct this target's physical identity word matrix. Target-only logarithm truncation makes its finite-error obstruction valid against arbitrary Markov rivals, without reversibility or a rate cap. That fixed-target rank theorem does not establish a reversibility penalty; the resolvent/entropy comparison above does. The full-Walsh result improves the explicit target-specific threshold, not the already polynomial unrestricted minimax growth class.

## 5. Remaining scope and access limits

No inspected source establishes the repository's complete combined constrained theorem. That is a bounded-search finding, not evidence of priority by itself. The elementary semigroup, approximation, realization and representation mechanisms should remain explicitly attributed. The stronger uncapped law $\exp(c\delta^{-\alpha})$, an uncapped binary analogue, and the new lower at a fixed positive control clock remain separate strengthening questions. No statistical sample bound or numerical-precision guarantee is supplied by the present argument.

**Access limits.** Full HTML versions of arXiv:1908.11097v1 and arXiv:2205.04807v1 were inspected, and both versioned PDFs linked above were successfully retrieved, on 23 September 2026. The original Trotter (1959) [publisher record](https://doi.org/10.1090/S0002-9939-1959-0108732-6) was found, but its PDF returned an access error; no original theorem numbering is asserted here. Anderson's (1999) [primary record](https://link.springer.com/article/10.1007/PL00009846) was accessible only as an abstract, so it supplies no theorem-level claim in this note. Artstein's *A variational convergence that yields chattering systems* (1989), [full text](https://www.numdam.org/article/AIHPC_1989__S6__49_0.pdf), §§6–7, concerns convergence and robustness of chattering optimization problems; it was inspected but is not used as a uniform controlled-mean inverse theorem. Searches used both search systems; some system-1 queries returned largely unrelated results, which were discarded. This is a focused comparison, not an exhaustive search or certification of originality.
