# Preparation-free information cost: source and scope audit

[Information and approximation theorem](FAMILIAR_SWITCH_PREPARATION_FREE_INFORMATION.md) · [Seven-word witness and sufficient test](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_TILT.md) · [Physical and reciprocity comparison](FAMILIAR_SWITCH_PREPARATION_FREE_UNKNOWN_SOURCE_AUDIT.md) · [Earlier five-word acquisition](FAMILIAR_SWITCH_PROFILED_ACQUISITION.md)

**Focused primary-source audit, 28 September 2026.** Adaptive change of measure, Hellinger affinity, data processing and optimization over testing alternatives are established methods. The additional inputs here are an explicit admissible physical rival, certified seven-word divergences and approximation errors, and the resulting bounds for this particular experiment.

## Certified result being compared

The chronological menu is $L,LL,H,LH,HL,LLH,HLL$. The ordinary null has fixed reused reversible kernels and a common unknown Gibbs tilt, with arbitrary word- and history-dependent preparations. Its counted states may include preparable states of zero equilibrium weight. Recorded endpoint pairs, rather than continuous trajectories, constitute the observations.

The selected rival is an actual **three-state reversible CTMC**, with positive rational transition rates, tilt $u=0.768614727605$, and word-specific preparations balanced in the visible sign. It certifies

$$
\max_w D(P_w\Vert Q_w)<3.023\times10^{-8},\qquad
\max_w\left(1-\sum_z\sqrt{P_w(z)Q_w(z)}\right)<7.557\times10^{-9}.
$$

Both error probabilities at most $0.05$ require expected acquisition exceeding **87,661,100.934495… complete pairs** under the ideal target. A deterministic cap requires at least **109,880,323 pairs**, including tests that select words adaptively and stop early. The existing **1.176-billion-pair** sufficient test is therefore within a factor **11** of the optimal deterministic cap for the matched interface. These are different statements about expectations and deterministic caps.

For the ideal population approximation problem, let $E_3$ denote the infimum maximum word-wise pair-law TV error among ordinary models with at most three states. The separate certificate gives

$$
\delta_0=\frac{3}{40006}\approx74.98875\ \mathrm{ppm}
\le E_3<86\ \mathrm{ppm},
$$

an upper-to-lower ratio below $1.15$. The attained general/ordinary state counts are **3/4 through $\delta_0$**, and **3/3 at 86 ppm**. This does not identify a globally optimal rival or the exact approximation frontier.

## Primary statistical precedents

| Primary source and inspected location | Established content and relevance |
| --- | --- |
| **E. Kaufmann, O. Cappé and A. Garivier**, “On the Complexity of Best-Arm Identification in Multi-Armed Bandit Models,” *JMLR* **17**(1), 1–42 (2016). [Published paper](https://www.jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf). Sampling convention, printed pp. 1–2; Lemma 1, p. 7; Appendix A.1, Lemma 19 and Eq. (18), p. 25. | Expected arm counts weighted by arm KL divergences bound the binary relative entropy of a stopped decision. The premises include mutually absolutely continuous fixed arm laws and an almost-surely finite stopping time. This is the direct precedent for the expected-count lower. |
| **A. Garivier and E. Kaufmann**, “Optimal Best Arm Identification with Fixed Confidence,” *PMLR* **49**, 998–1027 (2016). [Proceedings page](https://proceedings.mlr.press/v49/garivier16a.html); [paper](https://proceedings.mlr.press/v49/garivier16a.pdf). Section 2.1, Theorem 1, Eqs. (1)–(2) and proof, PDF pp. 3–4. | The information rate maximizes over allocations and minimizes over alternatives. The theorem concerns best-arm identification in one-parameter exponential families. It supplies a precise allocation-versus-alternative precedent, not an automatically optimal algorithm for this physical composite null. |
| **T. van Erven and P. Harremoës**, “Rényi Divergence and Kullback–Leibler Divergence,” *IEEE Transactions on Information Theory* **60**(7), 3797–3820 (2014). [DOI](https://doi.org/10.1109/TIT.2014.2320500); [inspected author paper](https://arxiv.org/pdf/1206.2459). Eq. (1), PDF p. 1; Eq. (5), p. 2; Theorem 1, p. 4; Example 2/Eq. (13), p. 5; Theorem 9/Eq. (22), p. 8. | Order-$1/2$ Rényi divergence is minus twice log affinity. Data processing reduces divergence and increases affinity, including processing by a common randomized channel. These properties underlie the fixed-cap decision bound. |

The [earlier calibration audit](FAMILIAR_SWITCH_CALIBRATION_SOURCE_AUDIT.md), Section 2, already attributes the KL method. Reusing it for a different physical rival does not introduce a new statistical inequality.

## Why one fixed rival constrains the broad null

Uniform false-rejection control includes this particular CTMC with fresh fixed-per-word preparations and ideal registration. Choosing that admissible special case for a lower bound imposes no independence or equilibrium-preparation promise on the entire null. All four pair outcomes enter the KL and affinity calculations. Conditioning on a chosen initial sign does not provide free observations.

Word selection occurs before the current initial observation, using completed past pairs and model-independent randomization. The same selection rule applies under both hypotheses. For rejection event $E$ and admissible complete-pair stopping time $T$, the standard likelihood argument gives

$$
\sum_w\mathbb E_P[N_w(T)]D(P_w\Vert Q_w)
\ge\operatorname{kl}(P(E),Q(E))\ge0.9\log19.
$$

State almost-sure termination under both selected laws. Infinite target expectation already satisfies the lower; otherwise the positive finite pair tables provide bounded log increments. Expected counts need not be integers.

## The adaptive affinity step

Write $A_w=\sum_z\sqrt{P_w(z)Q_w(z)}$ and $a=\min_w A_w$. At any common history $h$, let $g(w\mid h)$ be the policy's next-word distribution. The affinity of the conditional next word and pair is

$$
\sum_{w,z}\sqrt{g(w\mid h)P_w(z)\,g(w\mid h)Q_w(z)}
=\sum_wg(w\mid h)A_w\ge a.
$$

Multiplication by the nonnegative prefix weight $\sqrt{P(h)Q(h)}$ and summation over histories yield transcript affinity $\rho_t\ge a\rho_{t-1}$, hence $\rho_N\ge a^N$. Early stopping at a deterministic cap $N$ is handled by common dummy observations after stopping; their affinity is one. This is an adaptive **inequality**, not an exact product along a randomly selected arm sequence.

Data processing to the binary decision gives

$$
\rho_N\le\sqrt{P(E)Q(E)}+\sqrt{(1-P(E))(1-Q(E))}
\le\sqrt{0.19}.
$$

For $0<a<1$, therefore $N\ge\log(0.19)/(2\log a)$. The certificate needs lower bounds on arm affinities, equivalently upper bounds on their deficits. The proof does not permit substituting an expected random count for $N$. The numerical improvement over KL is task-specific, not a universal factor.

## Boundaries of the conclusion

The sufficient test allows target-only conditional 5 ppm true-boundary pair-law error and conditional 1 ppm registration error at each endpoint. Its experiment includes the ideal target and rival used for the lower. Comparing deterministic caps is valid for the same seven-word menu, pre-initial-sign selection and complete-pair observations. Initial-sign-dependent word selection, interrupted pairs or trajectory monitoring require another information calculation.

The local inverse appendix establishes completeness of $F=0$ near a specified regular interior CTMC point. It does not globally characterize realizable data, prove global minimization, or identify every hardest rival.

These bounds substantially constrain the fixed task's acquisition cost. They do not establish laboratory feasibility or price preparation, calibration and switching time. Further scientific improvement calls for a stronger physical signal or a different measurement design; minor changes to count constants would leave the central acquisition burden in place.
