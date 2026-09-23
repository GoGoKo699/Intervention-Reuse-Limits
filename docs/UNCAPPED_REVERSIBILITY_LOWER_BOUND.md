# A reversible state penalty without a rival rate cap

[Nineteen-level target](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Bounded-control observability](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) · [Whole-word repair and route obstructions](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) · [Finite-state fast-rate closure](FINITE_STATE_FAST_RATE_CLOSURE.md) · [Polynomial unrestricted upper](BOUNDED_RATE_FINITE_FIELD.md) · [Source comparison](BOUNDED_WORD_RECOVERY_PRIOR_ART.md)

**Research theorem, 23 September 2026.** The fixed nineteen-level target family has a superpolynomial reversible prediction cost even when rival internal rates are unrestricted. The proof extracts bounded positive resolvent words from actual means. It does not transfer the rival's unmodified generator moments, which can diverge under arbitrarily accurate prediction.

## 1. Statement and scope

Fix $H,k>0$. Use the nineteen-level family, original external field rule, exact actuator histogram, preparation and visible readout from the main theorem. In particular, $G=9/100$, the target hidden relaxation band is $[k,3k]$, and each of the nine paired-level ports has hidden stationary mass $1/18$. Let $D_{\rm all}^{\rm unc}(\delta)$ and $D_{\rm rev}^{\rm unc}(\delta)$ denote worst-case minimal total predictor state counts over this target family. Rivals use the prescribed original rule and histogram on their own finite hidden state spaces, with a stationary hidden law $\mu$. Neither class has an internal rate cap or a required lower gap; the second additionally has ordinary hidden reversibility.

For sufficiently small $\delta$, constants depending only on the fixed model parameters satisfy

$$
\boxed{
\begin{aligned}
c_0\delta^{-\zeta}
&\le D_{\rm all}^{\rm unc}(\delta)\le C_0\delta^{-p},\\
D_{\rm rev}^{\rm unc}(\delta)
&\ge\exp\!\left(\exp\!\left(c_1\sqrt{\log(1/\delta)}\right)\right),\\
p&=\frac{\log19}{\log(1+1/(3R_H))},\qquad
R_H=e^{(1+9/100)H}.
\end{aligned}}
\tag{1}
$$

The reversible upper from the bounded-rate theorem still applies, so
$D_{\rm rev}^{\rm unc}(\delta)\le\exp(C_1\delta^{-p}\log(2/\delta))$.
The new lower is superpolynomial in $1/\delta$, but is weaker than the fixed-cap bound $\exp(c\delta^{-\alpha})$.

The lower uses only the main theorem's thirty-nine fixed field values, with arbitrary positive segment durations. It uses arbitrarily rapid switching and does **not** establish a lower bound for each fixed positive control clock. All approximation errors concern the actual mean with the original preparation and readout. No auxiliary state, preparation or actuator is supplied to a rival.

Set $k=1$ in the proof. Restoring units rescales every physical time by $1/k$.

## 2. Physical convexification has full external dimension

Sections 2--5 give a self-contained specialization of the [bounded-control resolvent observability theorem](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md). Its general field-menu construction is applied here inside the main theorem's smaller fixed field interval.

Let $\Gamma=\{0,\pm1/100,\ldots,\pm9/100\}$. Write the full generator as

$$
Q(h)=K_b+\sum_{\gamma\in\Gamma}a_\gamma(h)X_\gamma
                   +\sum_{\gamma\in\Gamma}b_\gamma(h)Y_\gamma,
\qquad
a_\gamma(h)=e^{(1+\gamma)h},\quad
b_\gamma(h)=e^{(\gamma-1)h}.
\tag{2}
$$

The $X_\gamma,Y_\gamma$ include their outgoing diagonals, exactly as in the original physical model. The thirty-nine frequencies $0,1+\gamma,\gamma-1$ are distinct. On the main theorem's equally spaced menu $h_0,\ldots,h_{38}$, the matrix with rows $(1,a(h_j),b(h_j))$ is an invertible exponential Vandermonde matrix. Thus the thirty-nine vectors
$c(h_j)=(a(h_j),b(h_j))\in\mathbb R^{38}$ are affinely independent. Their convex hull is a full-dimensional simplex $\mathcal C$.

Every piecewise constant protocol with external coefficient vector in $\mathcal C$ is a limit of physical menu protocols obtained by rapid switching. For a fixed finite model this is the elementary matrix product formula on each segment. The same switching sequence converges for the target and any fixed finite rival, even if their rates differ greatly. Therefore a uniform actual-mean error bound $\delta$ on all physical menu protocols passes to every such convexified protocol. This step needs no convergence rate uniform over rivals.

Let $c_*$ be the simplex barycenter, and let

$$
\mathcal A=\{(a,b):a_\gamma=0,\ -1\le b_\gamma\le1\}.
\tag{3}
$$

Choose a fixed $0<\eta\le1/2$ sufficiently small that

$$
c_*+z(v-c_*)\in\mathcal C
\quad(v\in\mathcal A,\ z\in[-\eta,\eta]).
\tag{4}
$$

Such an $\eta$ exists because $c_*$ is an interior point and $\mathcal A$ is bounded. It depends only on the fixed field menu.

## 3. One analytic continuation for an entire protocol

Fix an arbitrary piecewise constant schedule $v(t)\in\mathcal A$ on $[0,T]$. For a complex scalar $z$ use the formal generator

$$
Q_z(t)=K_b+L\big(c_*+z(v(t)-c_*)\big),
\qquad L(a,b)=\sum_\gamma a_\gamma X_\gamma+b_\gamma Y_\gamma.
\tag{5}
$$

Only the real interval in (4) represents physical convexified protocols. Elsewhere (5) is an analytic proof expression; negative killing coefficients are not asserted to be physical rates.

In $L^2(\pi_0)$, $K_b$ is selfadjoint and nonpositive. If all external coefficients have modulus at most $C$, each block of $L(a,b)$ in the decomposition $\mathbb C\oplus L^2(\mu)$ has norm at most $C$, hence
$\|L(a,b)\|\le2C$. This bound is independent of the hidden dimension, stationary weights and internal rates.

Put

$$
\chi=\eta^{-1}+\sqrt{\eta^{-2}-1},\qquad
\rho=\chi^2,\qquad Z_*=\eta(\rho+\rho^{-1})/2.
$$

Let $C_*=\max_j |(c_*)_j|$ and set
$B_*=2[C_*+Z_*(C_*+1)]$.
On the complex Bernstein ellipse $\eta E_\rho$, all external operator norms in (5) are at most $B_*$. The bounded-perturbation expansion around the contraction generated by $K_b$ consequently gives a propagator norm at most $e^{B_*T}$, independently of the number of segments.

Let $F(z)$ be the target-minus-rival difference of the formal actual means. It is entire in $z$, satisfies $|F(z)|\le\delta$ for real $z\in[-\eta,\eta]$, and is bounded by $M_T=2e^{B_*T}$ on $\eta E_\rho$. The Chebyshev coefficients of $F(\eta x)$ obey both
$|a_j|\le2\delta$ and $|a_j|\le2M_T\rho^{-j}$. Also
$|T_j(1/\eta)|\le\chi^j$.
Splitting its convergent series at
$N=\lfloor\log(M_T/\delta)/\log\rho\rfloor$ gives

$$
|F(1)|\le C_{\rm an}e^{b_{\rm an}T}\sqrt\delta,
\qquad
C_{\rm an}=\frac{4\sqrt2\chi}{\chi-1},\quad
b_{\rm an}=B_*/2.
\tag{6}
$$

Indeed, the terms through $N$ sum to at most
$2\chi\sqrt{M_T\delta}/(\chi-1)$, and the tail has the same bound because $\rho=\chi^2$.
Crucially, (6) continues the **entire schedule using one scalar**. The exponent $1/2$ does not deteriorate with word length or segment count.

## 4. Absorbing protocols expose hidden resolvent words

For a bounded real diagonal feature $D=\operatorname{diag}(d(g))$, $|d|\le1$, the artificial coefficients $a=0$, $b_\gamma=u\,d(\gamma)$ have no entrance from $A$ and hidden operator $K-uD$. The full formal generator still has row sum zero. Starting from the original preparation, its actual-mean expression on $m$ successive segments is exactly

$$
m_{\rm art}(t_1,\ldots,t_m)+1
=\mu\prod_{i=1}^m e^{t_i(K-u_iD_i)}1.
\tag{7}
$$

The identity is algebraic and remains valid for $u_i\in[-1,1]$, including negative values. It follows because the initial hidden mass is $\mu/2$, receives no new entrance, and the readout is twice the hidden mass minus one.

Independently average each duration with density $s e^{-st_i}$, where $s>\max\{1,b_{\rm an}\}$. Define

$$
P=s(sI-K)^{-1},\qquad
F_D(u_1,\ldots,u_m)
=\mu\prod_{i=1}^m\left[s(sI-K+u_iD_i)^{-1}\right]1.
\tag{8}
$$

Equations (6)--(7), integrated over the durations, show that target and rival values of (8) differ by at most

$$
\varepsilon_{m,s}
=C_{\rm an}\left(\frac{s}{s-b_{\rm an}}\right)^m\sqrt\delta
\quad\text{on }[-1,1]^m.
\tag{9}
$$

All duration integrals converge by the same norm bounds. They are averages of analytic continuations of actual physical experiments, not extra experimental controls.

For $\epsilon\in\{-1,+1\}^m$ polarize with

$$
G_D(z)=2^{-m}\sum_\epsilon\left(\prod_i\epsilon_i\right)
F_D(z\epsilon_1,\ldots,z\epsilon_m).
\tag{10}
$$

The sign average removes every Taylor monomial unless each variable has odd degree. Consequently

$$
[z^m]G_D(z)
=(-1/s)^m\mu(PD_1P)\cdots(PD_mP)1
=(-1/s)^m\mu D_1P^2D_2\cdots P^2D_m1.
\tag{11}
$$

The second equality uses $\mu P=\mu$ and $P1=1$. The adjoint of $P$ is itself; $P$ is a stochastic nonnegative kernel. Thus the internal propagator $P^2$ in (11) is positive and reversible on each rival's own states.

## 5. A finite coefficient extractor with explicit error

For $s\ge4$ and complex $|z|\le s/2$, the Neumann resolvent bound gives

$$
\left\|s(sI-K+z\epsilon_iD_i)^{-1}\right\|
\le(1-|z|/s)^{-1}\le2.
$$

Therefore $|G_D(z)|\le2^m$ on that disk. Let $I_M$ be interpolation at the $M+1$ Chebyshev roots, with $M\ge m$. The sample-to-coefficient functional $[z^m]I_M$ has absolute coefficient mass at most $3^{M+1}$: discrete Chebyshev coefficients have bounds $1,2,\ldots,2$ for unit-bounded samples, and the sum of absolute monomial coefficients of $T_j$ is at most $3^j$.

The Taylor polynomial through degree $M$ has the same $z^m$ coefficient as $G_D$. Its omitted tail on every interpolation node is at most
$2^{m+1}(2/s)^{M+1}$. Applying the interpolation functional to that tail in both models proves

$$
\left|[z^m](G_D-\overline G_D)\right|
\le3^{M+1}\varepsilon_{m,s}
+2^{m+2}(6/s)^{M+1}.
\tag{12}
$$

No rival spectral cap enters this estimate. The polarization average has coefficient mass one, so its $2^m$ terms introduce no additional multiplicative error.

The required endpoint features are the central port indicator and the signed central actuator $s_0$. Both are bounded functions of the prescribed sensitivity label. Intermediate features are port indicators. Thus these features belong to the fixed artificial-control set used above; there is no expansion into an exponentially growing set of physical actuator values.

## 6. Positive cross-port resolvents approximate the target gates

On every rival define, for distinct adjacent ports,

$$
T_{cd}^{(s)}=8sD_cP^2D_d.
\tag{13}
$$

They are nonnegative kernels, and the reverse edge is the conditional stationary adjoint because all port masses are exactly $1/18$. This holds without a bound on $K$ or on the norms of (13).

On the target, $\|K\|\le3$. For $x\ge0$,

$$
0\le(1+x)^{-2}-1+2x
=\frac{x^2(3+2x)}{(1+x)^2}\le3x^2.
$$

Since $D_cD_d=0$, the spectral theorem gives

$$
\|T_{cd}^{(s)}-16D_cKD_d\|\le216/s.
\tag{14}
$$

The norms here are between conditional port $L^2$ spaces; their common mass makes them identical to the corresponding global block norms. Every exact target cross-port transport has norm one. Hence a path of $L$ edges differs from its exact target permutation transport in norm by at most

$$
(1+216/s)^L-1
\le432L/s\qquad(s\ge432L).
\tag{15}
$$

Use (13) in the original words $W_b,G_F,W_cG_FW_c^*$. Put
$Q_b=W_b^{(s)}$, $C_c=W_c^{(s)}G_F^{(s)}(W_c^{(s)})^*$ and
$v_b=Q_bs_0$. The [whole-word lemma](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) needs the squared row defects of $Q_b,C_c,C_c^*$, the norm of $v_b$, the norm of $C_cv_b$, and the signed correlation $\langle v_b,C_cv_b\rangle$. Their longest basic scalar path has

$$
L_{\max}=54n+6
\tag{16}
$$

edges. A row-defect square is a combination of two basic scalar moments and a known constant, with total error at most three times the common basic-moment error. Every ideal target basic scalar has its prescribed value $1$ or $-1$.

A length-$L$ conditional path scalar equals

$$
18(8s)^L\mu D_1P^2D_2\cdots P^2D_{L+1}1,
\tag{17}
$$

where endpoints may be the signed central feature. Repeated port projectors at concatenation points collapse exactly. Zero-edge constants and histogram moments are already fixed; alternatively they are covered by the same bounded-feature argument after combining coincident endpoints.

In (12) take $m=L+1$ and $M=3m$. Multiplication by the normalization in (11) and (17) gives basic-scalar target-to-rival discrepancy at most

$$
1458s(216s^2)^L\varepsilon_{m,s}
+\frac{186624}{s^3}\left(\frac{3456}{s}\right)^L.
\tag{18}
$$

The large raw operator norms in a rival are irrelevant: (18) measures only the needed scalar words, and subsequent repair uses the measured Gram norms.

## 7. Explicit accuracy budgets and entropy

Let $r=2^n$, $n\ge1$, and choose the fixed constant and resolvent scale

$$
C_H=4{,}000{,}000+2b_{\rm an},\qquad
s=C_H(L_{\max}+1)r^2.
\tag{19}
$$

For every required $L\le L_{\max}$ this ensures $s\ge432L$, $s\ge3456$ and
$\varepsilon_{L+1,s}\le eC_{\rm an}\sqrt\delta$.
The target approximation error (15) is at most $1/(9216r^2)$, since
$432/C_H\le1/9216$. The second term in (18) is also at most $1/(9216r^2)$; indeed it is bounded by $186624/s^3$ and (19) is more than sufficient for this inequality.

Write $K_H=1458eC_{\rm an}$. If

$$
\delta\le\widehat\delta_n
:=[9216r^2K_Hs(216s^2)^{L_{\max}}]^{-2},
\tag{20}
$$

the first term in (18) is at most $1/(9216r^2)$ as well. Thus each rival basic moment differs from its ideal target value by at most $1/(3072r^2)$. All hypotheses of the whole-word lemma hold with

$$
\Delta\le\frac1{1024r^2},\qquad
\sqrt\Delta\le\frac1{32r}.
\tag{21}
$$

That lemma clips the query functions and repairs each whole flip kernel on the rival's own central state space. Its entropy conclusion is

$$
D_{\rm rival}\ge D_{\rm central}\ge2^{3r/4}.
\tag{22}
$$

All constants in (19)--(20) are independent of rival dimension, minimum stationary mass and rates. Since $L_{\max}=O(n)$ and
$\log s=\log C_H+\log(54n+7)+2n\log2=O_H(n+1)$, (20) satisfies
$\log(1/\widehat\delta_n)\le C(n+1)^2$ for a fixed $C$.
Consequently (22) holds whenever
$\delta\le e^{-C(n+1)^2}$.
Taking $n=\lfloor\sqrt{\log(1/\delta)/C}\rfloor-1$ proves the reversible lower in (1), after decreasing its constant and restricting to sufficiently small $\delta$.

The unrestricted polynomial lower is the existing target-only finite-clock rank lower, which already permits unbounded rival rates. The polynomial upper is the existing stationary finite-word construction with target uniformization rate three, exact histogram and original rule. Those results and (22) establish the uncapped separation in (1).

## 8. What this result does and does not remove

The rival rate cap is absent throughout. The physical target remains the original nineteen-level family with fixed band $[k,3k]$. Cross-port selectors are actual actuator level sets on each rival, and all probability laws, repaired kernels and decoded bits live on that rival's own states.

The artificial absorbing and signed-killing protocols are analytic intermediate expressions derived from actual physical means. They are not extra controls granted to a model. The extraction uses bounded resolvent words, so the rare-fast-component obstruction to unmodified generator-moment transfer is respected.

This result does not remove the rate cap from the binary theorem, does not prove the stronger uncapped bound $\exp(c\delta^{-\alpha})$, and does not survive an imposed fixed positive control clock by the present argument. The binary palindromic-PSD obstruction remains applicable to literal resolvent substitution. Those are separate open strengthening questions.
