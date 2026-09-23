# Fixed-clock reversible observation: focused source comparison

[Repository overview](../README.md) · [Fixed-clock uncapped theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Target-sensitive Gram observability](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) · [Earlier capped clock lemma](REVERSIBLE_WORD_OBSERVABILITY.md) · [Bounded-word source comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) · [Binary source comparison](BINARY_OBSERVATION_PRIOR_ART.md)

**Research date: 23 September 2026; updated after internal mathematical reviews passed.** This focused search compares reversible embedding, matrix-function stability, sampled system identification and approximate positive realization. The repository now supplies an internally reviewed [target-sensitive fixed-clock research theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md). The sources below neither establish that theorem nor certify its priority. The elementary logarithmic transfer in Section 4 is a weaker comparison route; its limitations are not an impossibility theorem for the stronger target-sensitive method. Manuscript drafting remains deferred.

## 1. The precise comparison

Fix a positive clock $a$ and a finite menu of physical fields in $[-H,H]$. The observations are the actual scalar means from the prescribed equilibrium preparation and binary readout, for every menu protocol whose segment durations belong to $a\mathbb N$. The hidden target has a fixed rate cap; reversible rivals may have arbitrarily many states, arbitrarily small stationary masses and arbitrarily fast rates. Target and rival retain the original field rule and exact actuator histogram, but need not share hidden coordinates.

Three different questions must be distinguished:

1. Recovering a reversible generator from its complete sampled transition matrix on a known state space.
2. Comparing arbitrary-duration controlled means from clock-only controlled means.
3. Transferring the particular bounded positive witnesses needed for a state-count lower bound, using the target's rate cap but no rival cap.

The embedding results answer the first question exactly. Section 4 gives an elementary, weak quantitative answer to the second. The repository's [Gram observability](FIXED_CLOCK_GRAM_OBSERVABILITY.md) and [positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) pursue the third. These questions have different data and error norms.

## 2. Inspected primary sources

**Chen Jia, “A solution to the reversible embedding problem for finite Markov chains,” arXiv:1605.03502v1 (2016).** [Primary PDF](https://arxiv.org/pdf/1605.03502), [record](https://arxiv.org/abs/1605.03502). Full PDF opened; §§2–3 inspected. Under the paper's irreducibility assumption, Theorem 1 states that a stochastic matrix has at most one reversible embedding, given by the real spectral logarithm in equation (4). Lemma 3 requires positive sampled spectrum. This is an exact statement about the complete transition matrix in the same coordinates. It supplies neither a uniform inverse modulus nor identification from hidden scalar means. Ordinary logarithm-branch ambiguity is therefore not an obstruction to exact recovery of a fully observed reversible generator.

**Ellen Baake, Michael Baake and Jeremy Sumner, “Embedding of reversible Markov matrices,” arXiv:2511.22800v1 (27 November 2025).** [Primary PDF](https://arxiv.org/pdf/2511.22800), [record](https://arxiv.org/abs/2511.22800). Full preprint opened; §§2–3 inspected. Lemma 3.10 proves uniqueness of an existing real logarithm reversible under a specified strictly positive reference law, and identifies it with the principal logarithm. Fact 3.9 gives the logarithm's power series in the sampled matrix minus the identity. Theorem 3.16 characterizes the positive-spectrum reversible embedding case. The treatment does not require irreducibility. Its series is instancewise convergent; the paper supplies no uniform sampled spectral floor or hidden-mean inverse bound. It extends the scope of Jia's result without removing the conditioning issue in Section 3.

**Awad H. Al-Mohy, Nicholas J. Higham and Samuel D. Relton, “Computing the Fréchet Derivative of the Matrix Logarithm and Estimating the Condition Number,” SIAM Journal on Scientific Computing 35(4) (2013), C394–C410.** [DOI:10.1137/120885991](https://doi.org/10.1137/120885991), [author-hosted published PDF](https://eprints.maths.manchester.ac.uk/2015/01/covered/MIMS_ep2012_72.pdf). Full PDF opened; §1 and the integral derivative formula in §7.2 inspected. The paper develops derivative computation and condition estimation. In the positive self-adjoint case, that formula yields a logarithm Lipschitz constant inversely proportional to a spectral floor, as derived below. It does not turn controlled-output accuracy into matrix-norm accuracy or impose a positive Markov realization with the repository's field rule.

**Jun Ichi Fujii and Masatoshi Fujii, “On Operator Inequalities due to Ando–Kittaneh–Kosaki,” Publications of RIMS 24 (1988), 295–300.** [DOI:10.2977/PRIMS/1195175203](https://doi.org/10.2977/PRIMS/1195175203), [publisher PDF](https://ems.press/content/serial-article-files/42431?nt=1). Complete PDF opened; page 297 visually checked because text extraction omitted part of Corollary 1.1. That corollary records the classical operator-norm bounds

$$
\|A^\theta-B^\theta\|\le\|A-B\|^\theta\quad(0<\theta<1),
\qquad
\|\log(A+I)-\log(B+I)\|\le\log(1+\|A-B\|)
$$

for positive operators. Scaling gives $\log(1+\|A-B\|/\eta)$ for shifts by $\eta I$. These require no spectral floor, but compare operators on the same Hilbert space. Obtaining such a comparison from hidden scalar data is an additional problem. The paper attributes the inequalities to earlier work and studies equality cases; no priority for these tools is assigned to this repository.

**Rodrigo A. González, Max van Haren, Tom Oomen and Cristian R. Rojas, “Sampling in Parametric and Nonparametric System Identification: Aliasing, Input Conditions, and Consistency,” arXiv:2410.19629 (2024), IEEE Control Systems Letters.** [Primary PDF](https://arxiv.org/pdf/2410.19629), [record](https://arxiv.org/abs/2410.19629). Full primary preprint opened; Assumptions 3.1–3.2 and Theorems 3.1, 4.1–4.2 inspected. The setting is continuous-time linear time-invariant dynamics, multisine inputs and stationary-regime noisy measurements. Theorem 4.2 gives parametric consistency subject to the explicit identifiability condition $G_f(\theta)-G_f^0\in\ker\Phi_\zeta\Rightarrow\theta=\theta_0$. This separates input aliasing from identifiability, but assumes the required identifiability condition. It does not establish a finite-error modulus for arbitrary-size reversible Markov rivals under a fixed finite field menu.

**B. Vanluyten, J. C. Willems and B. De Moor, “Structured nonnegative matrix factorization with applications to hidden Markov realization and clustering,” Linear Algebra and its Applications 429 (2008), 1409–1424.** [DOI:10.1016/j.laa.2008.03.010](https://doi.org/10.1016/j.laa.2008.03.010), [institutional full PDF](https://ftp.esat.kuleuven.be/pub/SISTA/ida/reports/07-33.pdf). Full PDF opened; the factorization formulation and §5 inspected. Equation (16) factors the matrix of length-two output probabilities as $B^T\operatorname{diag}(\pi)AB$. A structured nonnegative approximation produces an HMM approximately matching those length-two probabilities. The section expressly restricts its realization problem to length two. It gives no all-word or all-horizon controlled-mean guarantee, continuous-time embedding guarantee, or state-count theorem in the present norm. Applying a short-block factorization to the repository's problem requires those additional guarantees.

**Daniel Hsu, Sham M. Kakade and Tong Zhang, “A Spectral Algorithm for Learning Hidden Markov Models,” arXiv:0811.4413v6 (6 July 2012).** [Primary PDF](https://arxiv.org/pdf/0811.4413), [record](https://arxiv.org/abs/0811.4413). Full PDF opened; Condition 1, §3 and Theorems 6–7 inspected. Observable representations use matrices of single-, pair- and triple-observation probabilities. Theorem 6 controls finite-sequence probability error, with sample bounds depending on hidden order and inverse singular values of the emission and pair-probability matrices. Theorem 7's conditional-prediction guarantee adds a uniform positivity condition. These are substantive finite-error results, but use sequence observations and spectral separation absent from the present hypothesis. The stated single-observation emission-rank condition fails for a binary observation of more than two hidden states; the authors explicitly discuss blocking observations as a possible relaxation. The representation need not itself be a positive Markov realization. This is a relevant observable-operator precedent, not the required clock-mean-to-positive-witness transfer.

**Limited-access leads, not theorem-level evidence.** Sattar et al., PMLR 283 (2025), on partially observed bilinear system identification, was encountered through its [publisher record](https://proceedings.mlr.press/v283/sattar25a.html); linked full-text requests failed. Bhatia–Kittaneh, “Some Inequalities for Norms of Commutators” (1997), [DOI:10.1137/S0895479895293235](https://doi.org/10.1137/S0895479895293235), was accessible at abstract level only in this pass. No uninspected identification or intertwining theorem from either source is used.

## 3. Unbounded logarithm instability and its exact limitation

The following calculations are elementary deductions, included to separate conditioning from identifiability.

Let

$$
Q_L=L\begin{pmatrix}-1&1\\1&-1\end{pmatrix},
\qquad \Pi=\tfrac12\mathbf1\mathbf1^T.
$$

Both $Q_L$ and $Q_{2L}$ are reversible under the uniform law. Since
$e^{maQ_L}=\Pi+e^{-2maL}(I-\Pi)$, for every integer $m\ge1$,

$$
\|e^{maQ_L}-e^{maQ_{2L}}\|\le e^{-2aL},
\qquad \|Q_L-Q_{2L}\|=2L.
\tag{1}
$$

Thus generator recovery cannot have a uniform vanishing modulus over all reversible rates, even when the entire sampled kernel is observed. This does not contradict exact embedding uniqueness. Both generators become fast, so (1) is **not** a counterexample with a fixed-cap target. The [rare-fast-component example](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md#5-rare-fast-states-prevent-raw-moment-transfer) instead obstructs the specified raw-moment transfer with a fixed target and small controlled-mean error; it still does not construct a compressed rival or obstruct bounded target-sensitive witnesses.

For positive self-adjoint $A$, the logarithm derivative formula in the Al-Mohy–Higham–Relton paper is

$$
L_{\log}(A,E)=\int_0^1
\bigl(I+t(A-I)\bigr)^{-1}E
\bigl(I+t(A-I)\bigr)^{-1}\,dt.
$$

If $A\ge mI$, bounding the integrand and integrating gives
$\|L_{\log}(A,E)\|\le\|E\|/m$. Integration along the segment between $A$ and $B$ therefore proves

$$
A,B\ge mI\quad\Longrightarrow\quad
\|\log A-\log B\|\le m^{-1}\|A-B\|.
\tag{2}
$$

A target bound $\|-Q\|\le R$ and an aligned operator comparison
$\|e^{aQ}-\widetilde P\|<e^{-aR}/2$, with both sampled operators self-adjoint in the same Hilbert space, would force a rival spectral floor and restore logarithm stability. The target's rate cap alone does not provide that aligned comparison from scalar means. This is the missing premise in a direct application of (2), not a conclusion that target-sensitive transfer is impossible.

## 4. Exact clock equivalence and an elementary weak modulus

The proof here is self-contained. It concerns two finite reversible physical models with the original field rule, each on its own hidden space. Use $k=1$, preparation $\pi_0=(1/2,\mu/2)$, and readout $S=(-1,1_{\rm hid})$. Then $\|1\|_{\pi_0}=\|S\|_{\pi_0}=1$. For menu fields $|h|\le H$, the reversible law is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h}.
$$

Its largest-to-smallest density ratio relative to $\pi_0$ is $e^{2|h|}$. Transferring operator norms from $L^2(\pi_h)$ to $L^2(\pi_0)$ costs at most $\kappa=e^H$, independently of dimension and rates. Write $P_h=e^{aQ(h)}$.

For $0<\theta<1$, define

$$
c_j=(-1)^{j+1}\binom\theta j>0,
\qquad
p_{N,\theta}(x)=1-\sum_{j=1}^{N}c_j(1-x)^j.
$$

The binomial series has sum $x^\theta$ on $[0,1]$. Its nonnegative tail is bounded by its value at zero. The partial binomial-sum identity, or induction in $N$, gives

$$
0\le p_{N,\theta}(x)-x^\theta
\le\sum_{j>N}c_j
=\prod_{j=1}^{N}\left(1-\frac\theta j\right)
\le(N+1)^{-\theta}.
\tag{3}
$$

The last step uses $\log(1-u)\le-u$ and $\sum_{j=1}^N j^{-1}\ge\log(N+1)$. Also $0\le p_{N,\theta}\le1$, and its monomial coefficient mass is at most

$$
1+\sum_{j=1}^{N}c_j2^j\le2^{N+1}.
\tag{4}
$$

Reversible functional calculus applies (3) to $P_h$, whose spectrum is in $(0,1]$, without a rate cap. For a specified word of $\ell$ segments, write $t_i/a=q_i+\theta_i$ with $q_i\in\mathbb N_0$ and $0\le\theta_i<1$. Replace a noninteger-duration factor by
$P_{h_i}^{q_i}p_{N,\theta_i}(P_{h_i})$ and retain exact powers when $\theta_i=0$. If $\theta_*$ is the smallest positive fractional part, telescoping costs at most $\ell\kappa^\ell(N+1)^{-\theta_*}$ in each model. Every approximating factor has norm at most $\kappa$.

Suppose the two models' clock-controlled means differ by at most $\delta$. Expanding the polynomial word gives allowed clock protocols with total absolute coefficient mass at most $2^{\ell(N+1)}$. Zero powers delete segments; adjacent equal fields can be merged. Hence

$$
\left|m(t_1,h_1;\ldots;t_\ell,h_\ell)
-\widetilde m(t_1,h_1;\ldots;t_\ell,h_\ell)\right|
\le2\ell\kappa^\ell(N+1)^{-\theta_*}
+2^{\ell(N+1)}\delta.
\tag{5}
$$

If every duration is a clock multiple, the original bound $\delta$ applies. For (5), clock protocols with at most $\ell$ segments and horizon $a\sum_i(q_i+N)$ suffice. The preparation/readout scalar for the empty protocol agrees exactly in both models.

At $\delta=0$, sending $N\to\infty$ proves that equality of all clock-controlled means implies equality for every positive-duration finite word over the same menu. The converse is immediate. This is equivalence of these **observable mean data**; it does not identify hidden coordinates or assert a common realization. No multitime observation or rival rate cap enters the proof.

For a fixed word and positive $\delta$, choosing $N$ proportional to $\log(1/\delta)/(2\ell\log2)$ gives the weaker estimate

$$
O_{\ell,H,\theta_*}\!\left((\log(1/\delta))^{-\theta_*}\right)
+O(\sqrt\delta).
\tag{6}
$$

It is not uniform over increasing segment count or durations approaching zero. Even an optimistic fixed-word substitution of (6) into the earlier continuous-time lower bound does not retain a superpolynomial lower bound in $1/\delta$. This describes the weakness of this particular approximation estimate, not an upper bound on recoverable information and not an impossibility result for fixed-clock separation.

## 5. What remains distinct in the target-sensitive argument

The classical sources supply reversible spectral calculus, exact full-kernel embedding criteria, matrix-function sensitivity and restricted positive realization procedures. None of the inspected theorems supplies, under the original actuator rule, the complete implication from a fixed finite menu of clock-controlled scalar means to the required positive witnesses uniformly over uncapped rivals.

The [Gram lemma](FIXED_CLOCK_GRAM_OBSERVABILITY.md) and [positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) use the fixed target's spectral information and positivity to control the relevant rival observables without first recovering every arbitrary-duration protocol or every raw generator moment. This addresses a narrower inverse problem than (6), with a stronger quantitative estimate for the required witnesses. The finite-error transfer budget, compatibility with positive whole-word repair, and resulting state-count exponent are established in the [main fixed-clock argument](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) and its proof dependencies; they are not consequences of the source list.

The internally reviewed theorem uses exactly the two physical fields $\{0,H\}$ at every prescribed positive clock $a/k$. It rescales the tagged family's hidden rates by a fixed positive factor chosen from the natural binary killing contrast. Consequently the target retains a fixed positive hidden gap and fixed cap, with very unfavorable constants; the gap is not normalized to $k$. Its budget is

$$
\delta\le e^{-C_a(n+1)^{12}},\qquad
\text{at most }O_a((n+1)^{12})\text{ clock ticks per required word}.
$$

The conclusion is a polynomial unrestricted upper and a reversible lower of $\exp(\exp(c_a[\log(1/\delta)]^{1/12}))$ on this rescaled tagged family. A polynomial unrestricted lower on the same family is not asserted. A finite collection of legal witness words does not itself provide an efficient experiment or a sample-complexity guarantee. Neither the exponent nor the constants are claimed optimal.

The theorem's separate [growth-class corollary](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md#6-a-five-field-common-family-growth-class-corollary) adjoins the older binary family and enlarges the menu to $\{0,H/4,H/2,3H/4,H\}$. On that union it obtains polynomial unrestricted growth together with the fixed-clock reversible lower. The changed family and five-field menu are part of that corollary; they do not strengthen the two-field main theorem's unrestricted assertion.

Search scope: both available search systems were used, with queries around continuous-time reversible hidden-model identification, fixed-interval sampling, reversible embedding, matrix-logarithm inverse stability, fractional powers, aliasing, spectral observable-operator learning and approximate positive realization. Full-text access and failed-access limits are recorded above. This is a bounded comparison of tools and hypotheses, not an exhaustive review, a priority certification or external validation of the repository's proof.
