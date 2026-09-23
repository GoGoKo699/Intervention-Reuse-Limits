# Same-state reversibilization from a stationary entropy-production bound

[State–entropy-production tradeoff](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) · [Primary-source comparison](PRL_EXPLORATION_SOURCE_AUDIT.md) · [Tight-band fixed-clock lower](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Original model](THEORY.md) · [Bounded-rate prediction upper](BOUNDED_RATE_FINITE_FIELD.md)

**Research theorem, 23 September 2026.** In the original intervention model, a predictor with small stationary hidden entropy production has a reversible predictor on exactly the same states, with the same hidden stationary law, actuator histogram and internal exit rates. Their actual controlled means remain uniformly close over every bounded deterministic protocol and every observation horizon. No hidden rate cap or minimum stationary mass is needed for this comparison.

The reason a horizon-independent estimate is possible is specific to the original external interface: every hidden state has a uniform positive return rate to the same visible state. A shared Poisson reset erases earlier state discrepancies. The statement concerns the endpoint mean, not the relative entropy of an entire arbitrarily long observed trajectory.

Additive reversibilization and its preservation of stationary weights and exits are established tools; see [Kolchinsky, Ohga and Ito (2024), Section II](https://arxiv.org/html/2304.01714v4). The result proved here concerns uniform controlled endpoint means with constants depending only on the external interface, followed by the state–entropy-production consequence. The separate source comparison records related spectral and thermodynamic bounds without claiming exhaustive novelty certification.

## 1. Definitions and statement

Let $K$ be a finite hidden generator with a strictly positive stationary law $\mu$. Hidden irreducibility is not required. Let $|g_i|\le G<1$, $|h(t)|\le H$, $k>0$, and put

$$
R=e^{(1+G)H}\ge1.
\tag{1}
$$

Use the original external rates

$$
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{iA}(h)=k e^{(g_i-1)h},
\tag{2}
$$

preparation $\pi_0=(1/2,\mu/2)$ and readout $S(A)=-1$, $S(i)=+1$. The hidden dynamics may be nonreversible. Write $m_K[h,T]$ for its actual mean.

The stationary reversed generator and arithmetic reversibilization are

$$
K^*_{ij}=\frac{\mu_jK_{ji}}{\mu_i}\quad(i\ne j),
\qquad K^*_{ii}=K_{ii},\qquad
L=\frac{K+K^*}{2}.
\tag{3}
$$

The ordered-sum stationary hidden entropy-production rate is

$$
\sigma(K)=\sum_{i\ne j}\mu_iK_{ij}
\log\frac{\mu_iK_{ij}}{\mu_jK_{ji}}.
\tag{4}
$$

Logarithms are natural; $0\log(0/b)=0$, and a positive numerator with zero denominator gives $+\infty$. This is the ordinary stationary Markov path-reversal entropy production, with Boltzmann's constant set to one. Its units are inverse time.

**Theorem.** The generator $L$ is reversible under $\mu$ and has exactly the same exit rate as $K$ at every hidden state. It uses no extra state and preserves the full actuator histogram. With the same external rule, preparation and readout,

$$
\boxed{
\sup_{h,T}|m_K[h,T]-m_L[h,T]|
\le\min\left\{2,\sqrt{\frac{R^3\sigma(K)}{2k}}\right\}.}
\tag{5}
$$

The supremum is over bounded deterministic protocols and all $T\ge0$. A stronger intermediate statement for the endpoint state laws $p_K(T),p_L(T)$ is

$$
D\bigl(p_K(T)\,\|\,p_L(T)\bigr)
\le\frac{R^3}{k}\,d(K\|L)
\le\frac{R^3\sigma(K)}{4k},
\tag{6}
$$

where $d(K\|L)$ is the stationary hidden path-relative-entropy rate defined below. The first inequality in (6) remains finite even if (4) is infinite.

## 2. Arithmetic reversibilization and the local path cost

Stationarity $\mu K=0$ implies $K^*1=0$ and $K^*_{ii}=K_{ii}$. Thus $L$ is a generator with $L_{ii}=K_{ii}$. Its edge flux is

$$
\mu_iL_{ij}=\frac{\mu_iK_{ij}+\mu_jK_{ji}}2
=\mu_jL_{ji},
$$

so $L$ satisfies detailed balance. Every edge used by $K$ is present in $L$, even if the original edge was one-way.

For each hidden state define

$$
d_i=\sum_{j\ne i}
\left[K_{ij}\log\frac{K_{ij}}{L_{ij}}-K_{ij}+L_{ij}\right]\ge0,
\qquad d=\sum_i\mu_i d_i.
\tag{7}
$$

The nonnegativity holds term by term with the usual zero conventions. Since the two exit rates agree in each row, the linear terms also cancel row by row. The quantity $d=d(K\|L)$ is finite for every finite $K$: whenever $K_{ij}>0$, $L_{ij}\ge K_{ij}/2$.

For a finite-entropy unordered flux pair $a=\mu_iK_{ij}$, $b=\mu_jK_{ji}$, its contributions to $d$ and $\sigma$ are

$$
d_{ab}=a\log\frac{2a}{a+b}+b\log\frac{2b}{a+b},
\qquad
\sigma_{ab}=(a-b)\log(a/b).
$$

They satisfy

$$
d_{ab}\le\frac14\sigma_{ab}.
\tag{8}
$$

To prove this, set $t=|a-b|/(a+b)\in[0,1)$. After removing the positive factor $(a+b)/2$, (8) is equivalent to

$$
F(t):=t\log\frac{1+t}{1-t}
-2\bigl[(1+t)\log(1+t)+(1-t)\log(1-t)\bigr]\ge0.
$$

Here $F(0)=0$ and

$$
F'(t)=\frac{2t}{1-t^2}-\log\frac{1+t}{1-t}\ge0,
$$

because the logarithm is $\int_0^t2/(1-s^2)\,ds\le2t/(1-t^2)$. Zero pairs follow by limits. A one-way pair gives infinite $\sigma$ and a finite $d$, so the inequality is still valid. Summing proves

$$
d\le\sigma(K)/4.
\tag{9}
$$

## 3. A shared state reset and a density bound

Let $\Pi_A$ be the stochastic matrix every row of which is $e_A^{\mathsf T}$, and set

$$
\alpha=k/R.
$$

Both full generators admit the decomposition

$$
Q_h=Q_h^{\rm res}+\alpha(\Pi_A-I).
\tag{10}
$$

The residual generator is valid: it subtracts $\alpha$ from every hidden-to-$A$ rate, which is at least $k/R$. At $A$ the reset is a no-op. Realize (10) by a Poisson clock of rate $\alpha$, independent of the residual time-dependent chain, which puts the process at $A$ whenever it rings.

Between reset events, let $p_i(t)$ be the hidden-state law of the residual $K$ process and define $r_i(t)=p_i(t)/\mu_i$. Its forward equation is

$$
\dot r_i=(K^*r)_i
-\bigl(q_{iA}(h(t))-\alpha\bigr)r_i
+p_A(t)k e^{(1+g_i)h(t)}.
\tag{11}
$$

The killing term is nonnegative and the source is at most $kR$. Since $K^*$ is a Markov generator, the finite-state maximum principle gives

$$
\max_i r_i(t)\le c_0+kRt
\quad\text{if}\quad\max_i r_i(0)\le c_0.
\tag{12}
$$

For a segment starting at $A$, $c_0=0$. For a segment starting in the original preparation, $c_0=1/2$. The bound depends on neither the largest hidden rate nor the smallest stationary weight. It remains valid for time-varying bounded deterministic fields.

## 4. Conditional path entropy and the last-reset mixture

Compare two residual processes using $K$ and $L$, with the same starting law and the same field protocol. Their external rates agree. The finite-state jump-path relative-entropy formula, or direct likelihood-ratio calculation, therefore gives over a segment of length $\tau$

$$
D(\mathbb P_K^{[0,\tau]}\|\mathbb P_L^{[0,\tau]})
=\int_0^\tau\sum_i p_i(t)d_i\,dt
\le d\left(c_0\tau+\frac{kR\tau^2}{2}\right).
\tag{13}
$$

All likelihoods are well-defined because every $K$ edge is an $L$ edge. Equation (13) also bounds the endpoint-law relative entropy by data processing.

At horizon $T$, a common independent reset clock has no event with probability $e^{-\alpha T}$. Otherwise its last-event age has density $\alpha e^{-\alpha\tau}$ on $0\le\tau<T$. Conditional on that age, both endpoint laws start from $A$ at the same final-segment start time. Conditional on no reset, both start from $\pi_0$. The clock law is identical in both models, so relative entropy of the endpoint mixture is bounded by the average of these conditional endpoint costs.

Put $x=\alpha T$. Applying (13) with the two values of $c_0$ yields

$$
\begin{aligned}
D(p_K(T)\|p_L(T))
&\le d\left[\frac{kR}{2}\mathbb E\min\{E,T\}^2
+\frac{T}{2}e^{-\alpha T}\right]\\
&=d\left[\frac{kR}{\alpha^2}
\bigl(1-(1+x)e^{-x}\bigr)+\frac{T}{2}e^{-x}\right],
\end{aligned}
\tag{14}
$$

where $E$ is exponential with rate $\alpha$. The equality uses
$\mathbb E\min\{E,T\}^2=2\alpha^{-2}[1-(1+x)e^{-x}]$.

Since $kR/\alpha=R^2$ and $R\ge1$, the difference between $dR^3/k$ and the last line of (14) is

$$
\frac d\alpha e^{-x}\left[R^2+(R^2-1/2)x\right]\ge0.
\tag{15}
$$

This proves the first inequality of (6), uniformly in $T$ and the protocol. Equations (9) and Pinsker's inequality finish the proof:

$$
|m_K-m_L|\le2\|p_K-p_L\|_{\rm TV}
\le\sqrt{2D(p_K\|p_L)}
\le\sqrt{R^3\sigma(K)/(2k)}.
$$

The Poisson clock is a proof representation of the original external rates. It does not add a state or change a control protocol.

## 5. Finite entropy production for a bounded-rate predictor

A separate same-state perturbation removes infinite entropy production from a stationary predictor. Suppose $-K_{ii}\le Bk$ for all hidden states, and choose $0<\varepsilon<1/2$. Put

$$
K_\varepsilon=(1-\varepsilon)K+\varepsilon K^*.
\tag{16}
$$

This preserves $\mu$ and every exit rate. For any pair of nonzero combined fluxes, its forward/reverse ratio lies between $\varepsilon/(1-\varepsilon)$ and $(1-\varepsilon)/\varepsilon$. Hence

$$
\boxed{
\sigma(K_\varepsilon)
\le Bk\log\frac{1-\varepsilon}{\varepsilon}<\infty.}
\tag{17}
$$

Indeed the stationary activity is at most $Bk$, and each logarithm in the ordered entropy sum is bounded above by the displayed logarithm. Zero flux pairs contribute zero.

At a common hidden state, the jump-rate mismatch in a maximal coupling is

$$
\frac12\sum_{j\ne i}|(K_\varepsilon)_{ij}-K_{ij}|
\le\varepsilon Bk.
$$

The external rates agree. Use the same reset clock (10), starting the two processes in the same initial state. A last reset couples both states back to $A$. Conditional on its age, the probability of a later disagreement is at most $\varepsilon Bk$ times that age. Since $\mathbb E\min\{E,T\}\le1/\alpha$,

$$
\boxed{
\sup_{h,T}|m_{K_\varepsilon}[h,T]-m_K[h,T]|
\le2BR\varepsilon.}
\tag{18}
$$

Consequently, given a rate-$Bk$ predictor with error at most $\delta/2$, choosing

$$
\varepsilon=\min\{1/4,\delta/(4BR)\}
\tag{19}
$$

gives error at most $\delta$ with the same state count and exit cap. For sufficiently small $\delta$,

$$
\sigma(K_\varepsilon)\le Bk\log(4BR/\delta).
\tag{20}
$$

If $B=0$, the generator already has zero entropy production and no perturbation is needed. Applying (19) to the existing stationary word-chain predictor gives a polynomial sufficient state count with finite entropy production $O(Bk\log(1/\delta))$. This is a sufficient upper bound, not a matched dissipation optimum.

## 6. Resource and physical scope

At zero field the full chain has stationary law $\pi_0$. Its visible-hidden edges obey detailed balance and the hidden edges carry half their $\mu$-weighted stationary flux. Thus its full zero-field stationary entropy-production rate is

$$
\sigma_0=\sigma(K)/2,
$$

and (5) becomes

$$
\sup_{h,T}|m_K[h,T]-m_L[h,T]|
\le R^{3/2}\sqrt{\sigma_0/k}.
\tag{21}
$$

More generally, the full stationary rate at a fixed field is $e^h\sigma(K)/(2\cosh h)$. These are stationary rates, not the total entropy generated by an arbitrary time-dependent protocol.

The theorem uses ordinary reversal that leaves each state label unchanged. A thermodynamic reading therefore treats the retained states as even configurations; generalized time reversal with odd variables is a different model. Equation (4) is a Markov path-irreversibility statistic. Identifying it with a physical heat cost requires a thermodynamic realization and local detailed balance, which are not supplied by this theorem.

The controlled-mean estimate uses the fixed preparation, original external return mechanism and bounded fields. It does not give a uniform bound for full controlled path laws, arbitrary initial laws with unbounded density relative to $\mu$, or models without a uniform state-erasing return rate. Every state retained by a predictor remains counted. Arithmetic reversibilization preserves a common exit cap when one is imposed; it does not generally preserve a separately imposed lower spectral gap.
