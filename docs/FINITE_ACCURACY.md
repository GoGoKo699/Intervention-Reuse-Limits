# Exact complexity is not fixed-accuracy complexity

[Repository overview](../README.md) · [Core derivation](THEORY.md) · [Prior art](PRIOR_ART.md)

**Working extension, 22 September 2026.** Sections 8–10 give constructive upper bounds and finite-sample response lower bounds. The broad minimax rate remains between logarithmic and squared-logarithmic state growth; a fixed upper bound on active target rates gives matching logarithmic order. Publication-level originality is not asserted.

The core example has an exact two-state passive description and an $N$-state exact cubic response requirement. This note retains nonvanishing total signal, constructs reversible approximate models independently of $N$, and proves tolerance-dependent lower bounds directly from response samples. The lower bounds allow the full analytic Markov surrogate class defined below.

## 0. The approximation task and its quantifiers

Fix $k>0$, a sensitivity bound $G<\infty$, a protocol bound $U<\infty$, and a kernel mass $0\le W\le G^2$. The target class $\mathcal F(k,G,W)$ consists of all finite models in [Theory, Section 1](THEORY.md), of arbitrary microscopic size, with $|g_j|\le G$ and $\langle g^2\rangle_\mu=W$. The internal generator is irreducible and reversible. There is no common bound on its rates, spectral gap, or topology.

Every experiment starts from the model's zero-field equilibrium. Its readout is the fixed binary state observable in the core model. For $h(t)=\epsilon u(t)$, the task is the coefficient of $\epsilon^3$ in the single-time mean, with coefficients defined by derivatives divided by factorials. Let $\mathcal U_U(T)$ contain all piecewise-continuous protocols on $[0,T]$ with $|u|\le U$. Define

$$
\mathcal E_U(F,\widehat F)=
\sup_{T>0}\ \sup_{u\in\mathcal U_U(T)}\ \sup_{0\le t\le T}
|m_{3,F}[u](t)-m_{3,\widehat F}[u](t)|.
$$

One surrogate must serve all protocols and all horizons in this norm. The constructor is supplied the exact finite spectral measure of $C$, as well as $k$. This is a known-kernel compression problem; computation and bit precision of that input are not charged as states. It is not a learning or sample-complexity problem.

For the broad comparison, $\mathcal A_D(k)$ consists of Markov models with at most $D$ states, rates analytic in the same instantaneous scalar field near zero, fixed binary state readout, and a fixed zero-field stationary preparation. Require the same complete stationary passive visible path law, the equilibrium mean $\tanh h$ near zero, the reference linear mean response for every protocol, and zero quadratic mean response. No reversibility, topology, or derivative bound is imposed on this broad surrogate class. In particular a coordinate named $g$ need not exist for a general surrogate.

The minimax question is

$$
E_D(k,G,W,U)=
\sup_{F\in\mathcal F(k,G,W)}\ \inf_{\widehat F\in\mathcal A_D(k)}
\mathcal E_U(F,\widehat F).
$$

The constructive **upper bounds** produce surrogates in the original reversible rate-rule family, with the same $k,W$ and $|\widehat g|\le G$. They also preserve the passive path law under every microscopic initial law with the same visible initial law. Their microscopic rates and topology may change. Sections 9–10 instead prove **lower bounds against all of $\mathcal A_D(k)$** by constraining finite response samples. A lower bound proved only for positive kernels, reversible surrogates, or this rate-rule family would not automatically bound $E_D$.

The norm concerns Taylor coefficients only. None of its quantifiers asserts a Taylor remainder uniform in $T$, $N$, or the field amplitude. Finite-field prediction and kernel acquisition remain separate tasks.

## 1. A bounded-coupling, nonvanishing-signal exact family

Keep the reflecting path $K$, uniform $\mu$, and $0<\rho<k/4$ from the core note. Write

$$
a_j=(-1)^{j-1},\qquad \bar a=\frac1M\sum_{j=1}^M a_j,
\qquad g_j=\frac12\left(a_j-\bar a+\mathbf1_{\{j=1\}}-\frac1M\right).
$$

For every $M\ge2$, this vector is centered and $|g_j|\le1$. The kernel mass is

$$
W=\frac14\left[1-\bar a^2+\frac{M-1}{M^2}+\frac{2(1-\bar a)}{M}\right].
$$

For even $M$, this is $(1+3/M-1/M^2)/4$; for odd $M$, it is $(1+3/M-4/M^2)/4$. Therefore $W\ge1/4$ for every $M\ge2$, while the pointwise bound on $g$ gives $W\le1$.

Let $\theta_\ell=\pi\ell/(2M)$ and let $I_\ell$ be one when $M+\ell$ is odd and zero otherwise. The path eigenvalues are unchanged, and the weights are

$$
c_\ell=\frac{1}{2M^2}
\left(\cos\theta_\ell+\frac{I_\ell}{\cos\theta_\ell}\right)^2>0,
\qquad 1\le\ell<M.
$$

To verify the overlap, the endpoint term contributes $\cos\theta_\ell$ to the unnormalized cosine sum. The alternating term contributes $1/\cos\theta_\ell$ when $M+\ell$ is odd and zero otherwise. Centering removes only the constant mode. This proves that all $M-1$ hidden modes remain active, with no cancellation. The exact $2$-versus-$N$ theorem therefore still holds.

This also yields a nonvanishing visible correction, not merely a nonvanishing kernel norm. Since $0\le C(s)\le W$, the step formula implies, with $\tau=kt$,

$$
m_3(t)-b_3(t)\ge W e^{-2\tau}(3\tau+2-2e^\tau).
$$

At $t=1/(4k)$ the bracket is positive, so

$$
m_3(1/(4k))-b_3(1/(4k))
\ge\frac{e^{-1/2}}4\left(\frac{11}{4}-2e^{1/4}\right)
\approx0.0275894.
$$

This is a bound on a cubic **coefficient**, not on a finite-field signal without the factor $\epsilon^3$ and a remainder. It establishes a visible total correction of size independent of $N$. It does not establish that all $N-2$ hidden modes are separately resolvable: some individual weights still become small.

## 2. The response error controlled by a kernel approximation

For fixed $k$, consider two kernels with equal mass $C(0)=\widetilde C(0)=W$. Let $m_3[u]$ and $\widetilde m_3[u]$ denote their cubic mean-response coefficients, each model started from its own zero-field equilibrium and driven by the same protocol $|u(t)|\le U$.

The common linear response obeys $|m_1|\le U$, and hence $|u(u-m_1)|\le2U^2$. Subtracting the two equations for $\delta$ in the core note and using the stable filter with decay $2k$ gives

$$
\sup_{0\le t\le T}|m_3[u](t)-\widetilde m_3[u](t)|
\le2kU^3\int_0^\infty e^{-ks}|C(s)-\widetilde C(s)|\,ds.
$$

For completeness, before integrating the outer filter the forcing is bounded by $4k^2U^3\int_0^t e^{-ks}|C(s)-\widetilde C(s)|ds$; the outer filter integrates to at most $1/(2k)$. The bound holds for every finite $T$, with the same constant. It is a uniform statement about Taylor coefficients, not a uniform finite-amplitude expansion.

## 3. Compactifying the kinetic rates

For a reversible finite-state model,

$$
C(t)=\sum_jc_j e^{-\lambda_jt},\qquad c_j>0,\quad\lambda_j>0,\quad\sum_jc_j=W.
$$

Introduce $x_j=k/(k+\lambda_j)\in(0,1)$. If a rate $\lambda_j$ is replaced by a positive rate $\widetilde\lambda_j$, the two exponentials are ordered for all nonnegative times. Therefore

$$
\int_0^\infty e^{-kt}|e^{-\lambda_jt}-e^{-\widetilde\lambda_jt}|\,dt
=\left|\frac1{k+\lambda_j}-\frac1{k+\widetilde\lambda_j}\right|
=\frac{|x_j-\widetilde x_j|}{k}.
$$

Combining this identity with the preceding response bound and the triangle inequality gives the certificate

$$
\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|
\le2U^3\sum_jc_j|x_j-\widetilde x_j|.
$$

This transport bound is sufficient, not necessary or asserted optimal.

## 4. A universal $q$-mode compression

Divide $(0,1)$ into $q$ equal intervals and move each $x_j$ to the midpoint of its interval. Aggregate all weights in the same interval. Every displacement is at most $1/(2q)$, the weights remain positive, and the mass remains exactly $W$. Thus the resulting kernel has at most $q$ active rates and satisfies

$$
\boxed{\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|\le\frac{U^3W}{q}.}
$$

The same surrogate works for every bounded piecewise continuous protocol and every finite horizon. It does not need to be refitted when the protocol changes. No lower bound on the original hidden spectral gap and no upper bound on its largest rate enter this certificate.

The midpoint rates lie between $k/(2q-1)$ and $k(2q-1)$. The construction is not required to preserve the original microscopic topology or a prescribed upper bound on all kinetic rates. Adding such restrictions would change the comparison class.

Crucially, the construction requires knowledge of the intervention kernel or its spectral measure. It is **not** a way to learn hidden kinetics from the passive binary process. Statistical identification from noisy intervention data is a separate problem.

## 5. Reversible Markov realization of the compressed kernel

Let the compressed kernel have $r\le q$ positive terms,

$$
\widetilde C(t)=\sum_{\ell=1}^r w_\ell e^{-\eta_\ell t},\qquad
\sum_\ell w_\ell=W>0.
$$

Create hidden pairs $B_{\ell,+},B_{\ell,-}$, with

$$
\widetilde\mu_{\ell,\pm}=\frac{w_\ell}{2W},\qquad
\widetilde g_{\ell,\pm}=\pm\sqrt W.
$$

Choose $0<\beta<\min_\ell\eta_\ell$. Within pair $\ell$, let the symmetric flip rate be $(\eta_\ell-\beta)/2$. Add a global refresh generator

$$
R=\beta(\mathbf1\widetilde\mu^T-I)
$$

to the block-diagonal pair generator. Call the result $\widetilde K$. It has strictly positive cross-pair off-diagonal rates, is irreducible, and is reversible under $\widetilde\mu$: the refresh flux between two states is $\beta\widetilde\mu_i\widetilde\mu_j$, and each pair has equal stationary weights.

The antisymmetric function supported on pair $\ell$ has mean zero. Pair flipping gives decay $\eta_\ell-\beta$; refresh adds decay $\beta$, so the total is $\eta_\ell$. These functions are orthogonal across pairs, and the squared projection of $\widetilde g$ on pair $\ell$ is $w_\ell$. Consequently,

$$
\langle\widetilde g,e^{\widetilde Kt}\widetilde g\rangle_{\widetilde\mu}
=\widetilde C(t).
$$

Add the state $A$ and use exactly the **functional rate rule** of the core model, with $k,\widetilde\mu,\widetilde K,\widetilde g$. This gives a reversible analytic Markov surrogate with $2r+1\le2q+1$ states. It preserves the exact two-state passive path law, equilibrium curve $\tanh h$, dynamic linear response, and zero quadratic mean response. Its cubic response satisfies the uniform certificate above.

If the original $|g_j|\le G$, then $W\le G^2$ and the realized $|\widetilde g|=\sqrt W\le G$. When $W=0$, the ordinary two-state reference already suffices and no paired construction is needed.

The paired realization remains a simple regression baseline. [Theory, Section 9](THEORY.md) now gives a smaller $r+2$-state realization by standard Jacobi inverse spectral theory, retaining the same sensitivity bound. For noncolliding rates it attains the exact state lower bound.

## 6. Consequence for the research claim

For any fixed coefficient tolerance $\varepsilon>0$, choosing

$$
q\ge\max\left(1,\left\lceil\frac{U^3W}{\varepsilon}\right\rceil\right)
$$

produces an admissible surrogate with at most $2q+1$ states, **independent of the microscopic state count $N$**. Thus a universal fixed-accuracy lower bound growing with $N$ is ruled out for this model family and this unrestricted surrogate class, at cubic order and bounded $W,U$.

The resulting scientific distinction is not simply that the first construction had weak total signal. Exact complexity can grow without bound even with a nonvanishing response correction, while finite-accuracy complexity is controlled by tolerance and kinetic-kernel information.

The $1/q$ error rate is an elementary upper bound, not a minimax or novelty claim. Section 8 improves it under the same assumptions. Positive exponential approximation supplies the method and the root-exponential order; see [the audit](PRIOR_ART.md). A useful publication contribution still needs a distinctive operational statement beyond those standard tools.

## 7. Checks and remaining boundary

[The executable extension](../scripts/verify_finite_accuracy.py) verifies the normalized spectral weights, nonvanishing signal bound, positive reversible realization, and agreement of its master equation with the memory equations. It also tests the protocol certificate on deterministic sign-changing protocols. See [verification details](VERIFICATION.md).

Still not established: the optimal dependence on tolerance for unrestricted target rates, stable inference from finite noisy data, a finite-field remainder uniform in system size and observation horizon, or a specific fluid or molecular implementation. Sections 9–10 add response-norm lower bounds and determine the state-growth order for the separately defined rate-capped target class. No large simulation is needed. The [next work order](../work_orders/CURRENT.md) records the remaining mathematical and novelty questions.

## 8. A stronger bound by positive Gaussian quadrature

The midpoint construction is not the strongest available certificate. Applying classical positive Gaussian quadrature separately on dyadic rate intervals yields a root-exponential bound without imposing a hidden spectral gap, a maximum microscopic rate, or a smooth spectral density. The Gaussian-quadrature machinery is established approximation theory; the result below is its explicit application to the operational response norm and Markov realization used here. It is neither a novelty claim for quadrature nor an optimality claim.

**Theorem.** Let $C(t)=\sum_i c_i e^{-\lambda_i t}$ be any finite positive kernel, with $c_i>0$, $\lambda_i>0$, and total mass $W$. For every integer $n\ge1$, there is a positive kernel $\widetilde C_n$ with the same mass and at most

$$
q_n=2n(n+1)+1
$$

active rates, all strictly positive, such that

$$
\int_0^\infty e^{-kt}|C(t)-\widetilde C_n(t)|\,dt
\le \frac{4W}{k}\,16^{-n}.
$$

Consequently, for every bounded piecewise continuous protocol $|u(t)|\le U$ and every finite horizon $T$,

$$
\boxed{\sup_{0\le t\le T}|m_3[u](t)-\widetilde m_{3,n}[u](t)|
\le 8U^3W\,16^{-n}.}
$$

The same kernel and its Markov realization work for all these protocols and horizons. Section 5 gives an elementary paired realization with at most $2q_n+1=4n(n+1)+3$ states. The [Jacobi realization](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel) improves this to $q_n+2=2n(n+1)+3$ states. Both preserve the passive path law, equilibrium curve, dynamic linear response, and vanishing quadratic mean response. Both use $|\widetilde g_i|=\sqrt W$, so the original bound $|g_i|\le G$ is preserved as well.

### 8.1 One dyadic interval

Use dimensionless time $y=kt$ and rates

$$
a_i=1+\lambda_i/k>1,
\qquad F(y)=e^{-y}C(y/k)=\sum_i c_i e^{-a_i y}.
$$

Consider a positive measure $\nu$ of mass $w$ supported on a finite subset of $[A,2A]$, where $A>0$. Its contribution to $F$ is $F_\nu(y)=\int e^{-ay}\,d\nu(a)$. If the support contains at most $d$ distinct points, retain it exactly. Otherwise use the $d$-point Gaussian quadrature rule for $\nu$. Its nodes lie strictly between the smallest and largest support points, its weights are positive, and it integrates all polynomials of degree at most $2d-1$ exactly. In particular it preserves $w$.

Write $p_d$ for the monic degree-$d$ orthogonal polynomial whose roots are those nodes, and $Q_d(f)$ for the quadrature value. For fixed $y\ge0$, let $H$ be the polynomial of degree at most $2d-1$ matching $f(a)=e^{-ay}$ and its first derivative at the nodes. The Hermite-interpolation remainder gives, at every support point,

$$
0\le f(a)-H(a)
\le \frac{y^{2d}e^{-Ay}}{(2d)!}\,p_d(a)^2.
$$

Both inequalities follow from $f^{(2d)}(a)=y^{2d}e^{-ay}\ge0$ and $a\ge A$. Exactness on $H$, together with $H=f$ at the nodes, implies

$$
0\le F_\nu(y)-Q_d(e^{-ay})
\le \frac{y^{2d}e^{-Ay}}{(2d)!}\int p_d(a)^2\,d\nu(a).
$$

The quadrature contribution therefore underestimates $F_\nu$ pointwise. Integration in $y$ yields

$$
\int_0^\infty |F_\nu(y)-Q_d(e^{-ay})|\,dy
\le \frac{1}{A^{2d+1}}\int p_d(a)^2\,d\nu(a).
$$

The monic orthogonal polynomial minimizes the squared $L^2(\nu)$ norm among monic degree-$d$ polynomials. Compare it with the monic rescaled Chebyshev polynomial

$$
r_d(a)=2(A/4)^d\,T_d\!\left(\frac{2a-3A}{A}\right),
\qquad |r_d(a)|\le 2(A/4)^d\quad(A\le a\le2A).
$$

It follows that $\int p_d^2\,d\nu\le4w(A/4)^{2d}$, and hence

$$
\boxed{\int_0^\infty |F_\nu(y)-Q_d(e^{-ay})|\,dy
\le\frac{4w}{A}\,16^{-d}.}
$$

Since the difference is nonnegative, its integral is also exactly the Gaussian-quadrature error for $a\mapsto1/a$. This identity provides a direct way to check the integrated kernel certificate without a numerical time cutoff.

### 8.2 Rate intervals, degree allocation, and the tail

Fix $n\ge1$, and write $\nu=\sum_i c_i\delta_{a_i}$ for the full dimensionless spectral measure. Apply the preceding one-interval argument to its restrictions. Partition $1\le a<2^{4n}$ into the half-open intervals

$$
I_j=[2^j,2^{j+1}),\qquad 0\le j<4n.
$$

On interval $I_j$, allocate

$$
d_j=n-\lfloor j/4\rfloor\ge1
$$

Gaussian nodes, retaining the measure exactly whenever it already has at most $d_j$ distinct support points. Empty intervals need no nodes. Let $w_j$ be the mass in $I_j$. Writing $j=4s+r$ with $0\le r\le3$ gives

$$
2^{-j}16^{-d_j}=16^{-n}2^{-r}\le16^{-n}.
$$

The one-interval bound therefore makes the total error from these intervals at most $4W_{\rm core}16^{-n}$, where $W_{\rm core}=\sum_jw_j$.

For the remaining mass $W_{\rm tail}$ at $a\ge 2^{4n}$, move all of it to the single rate $a_*=2^{4n}$. This preserves mass and overestimates the tail pointwise. Its integrated error is

$$
\int_{a\ge a_*}\left(\frac1{a_*}-\frac1a\right)d\nu(a)
\le W_{\rm tail}16^{-n}.
$$

Combining the core and tail errors with the triangle inequality yields

$$
\int_0^\infty |F(y)-\widetilde F_n(y)|\,dy
\le (4W_{\rm core}+W_{\rm tail})16^{-n}
\le4W16^{-n}.
$$

The node count is bounded by

$$
\sum_{j=0}^{4n-1}d_j+1
=4\sum_{d=1}^n d+1
=2n(n+1)+1.
$$

The final $+1$ is unnecessary when the tail is empty. Nodes or original atoms within the first interval are strictly greater than one because every original $a_i>1$; all other nodes and the tail node exceed one automatically. Returning to physical rates $\widetilde\lambda=k(a-1)$ thus gives strictly positive rates throughout. Changing variables back to $t$ and applying Section 2 proves the theorem.

### 8.3 State count at a prescribed tolerance

For $U^3W>0$ and a cubic-coefficient tolerance $\varepsilon>0$, it is sufficient to choose

$$
n=\max\!\left\{1,\left\lceil\log_{16}\!\left(\frac{8U^3W}{\varepsilon}\right)\right\rceil\right\}.
$$

The resulting reversible Markov surrogate uses at most $2n(n+1)+3$ states with the Jacobi realization, or $4n(n+1)+3$ with the explicit paired construction. Thus the constructive state upper bound is

$$
O\!\left(\left[1+\log_+\!\left(\frac{U^3W}{\varepsilon}\right)\right]^2\right),
\qquad \log_+x=\max\{0,\log x\},
$$

independently of the original state count and spectral range. For a prescribed mode budget $q\ge5$, the explicit root-exponential certificate is obtained with

$$
n(q)=\left\lfloor\frac{\sqrt{2q-1}-1}{2}\right\rfloor,
\qquad
\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|
\le8U^3W\,16^{-n(q)}.
$$

For small budgets the earlier $U^3W/q$ bound can be better; one may choose whichever construction supplies the smaller certificate. If $W=0$, the two-state reference suffices exactly. If $U=0$, there is no response to approximate.

The proof requires the kernel's spectral measure. It supplies no inference method from passive observations, and no statistically stable reconstruction from noisy response data. It permits new rates and new microscopic topology, as does the earlier midpoint construction. Section 10 proves a logarithmic state lower bound, leaving a gap from the squared-logarithmic upper bound for this unrestricted target class. No finite-amplitude guarantee follows from the cubic-coefficient theorem alone.

### 8.4 Reduction to established approximation results

The asymptotic order also follows from Koyama's positive quadrature results identified in [the prior-art audit](PRIOR_ART.md). Here is the reduction, rather than a claim that a different norm alone supplies novelty. For $0<\delta<1$, clamp each rate into $[k\delta,k/\delta]$. Section 3's exact transport identity shows that this costs at most $W\delta$ in the normalized norm $k\int_0^\infty e^{-kt}|\Delta C(t)|dt$, while preserving mass. On that finite interval, the established mass-preserving positive quadrature theorem gives uniform-time error $O(W\delta)$ with $O(\log^2(1/\delta))$ nodes. Its uniform-time bound also controls the normalized damped norm since $k\int_0^\infty e^{-kt}dt=1$. Retain measures with fewer nodes exactly. The response inequality and reversible realization then complete the same asymptotic state upper bound. The elementary proof above makes constants and rate allocation explicit; it does not create a new approximation-theory claim.

## 9. A finite-error obstruction for every two-state surrogate

The broad comparison class in Section 0 already has a nonzero operational
lower bound at two states. This does not assume the surrogate belongs to
the original rate-rule family, and it does not bound its field derivatives.

**Theorem.** For $k>0$, $U>0$, and $0<W\le G^2$,

$$
\boxed{E_2(k,G,W,U)\ge
\frac{15}{8(e^3+6e^{1/2})}\,U^3W
\approx0.06254614958\,U^3W.}
$$

One three-state target and two samples of its constant-protocol cubic
coefficient prove the bound. The result excludes two-state approximation
below a fixed positive coefficient tolerance. It does not determine the
all-protocol minimax error, or its dependence on larger state budgets.

### 9.1 Complete characterization of the two-state comparison class

A one-state fixed-readout model cannot reproduce the binary passive path
law. A two-state model reproducing that law must have one state of each
visible sign, zero-field rates $a(0)=b(0)=k$, and stationary preparation
$(1/2,1/2)$. Here $a(h)$ is the rate from $-1$ to $+1$, and $b(h)$ is the
reverse rate. These rates remain positive in a neighborhood of zero.

The required equilibrium mean implies

$$
\frac{a(h)-b(h)}{a(h)+b(h)}=\tanh h,
\qquad
a(h)=k r(h)e^h,\quad b(h)=k r(h)e^{-h},
$$

for one positive analytic function $r$ with $r(0)=1$. Thus its exact mean
obeys

$$
\dot{\widehat m}=2k r(h)
\bigl(\sinh h-\widehat m\cosh h\bigr).
$$

Write $r(h)=1+r_1h+\alpha h^2+O(h^3)$. Its linear coefficient is the
reference $m_1$. Its quadratic coefficient satisfies

$$
\dot{\widehat m}_2=-2k\widehat m_2+2kr_1u(u-m_1).
$$

For a unit constant protocol this gives
$\widehat m_2(t)=2kr_1t e^{-2kt}$, so the required zero quadratic
response forces $r_1=0$. Conversely $r_1=0$ makes the quadratic response
zero for every protocol. The entire remaining two-state freedom at cubic
order is the real number $\alpha$:

$$
\dot{\widehat\delta}
=-2k\widehat\delta+2k\alpha u^2(u-m_1),
\qquad \widehat\delta=\widehat m_3-b_3,
\qquad \widehat\delta(0)=0.
$$

There is no restriction on $\alpha$: for any real choice,
$r(h)=\exp(\alpha h^2)$ realizes it with positive analytic rates and all
the required passive, static, linear, and quadratic properties. Higher
derivatives of $r$ cannot affect the cubic coefficient because the factor
$\sinh h-\widehat m\cosh h$ vanishes at order zero. This characterizes
cubic response throughout $\mathcal A_2(k)$, for every bounded protocol.

### 9.2 A two-time response witness

Choose the target with two hidden states,

$$
\mu=(1/2,1/2),\qquad g=(\sqrt W,-\sqrt W),\qquad
K=\begin{pmatrix}-k/2&k/2\\k/2&-k/2\end{pmatrix}.
$$

It belongs to $\mathcal F(k,G,W)$ and has $C(t)=W e^{-kt}$. For the
constant protocol $u(t)=U$, write $\tau=kt$ and
$f(\tau)=\tau e^{-2\tau}$. The target and every admissible two-state
surrogate have corrections

$$
\delta(t)=U^3W f(\tau)(1-\tau),\qquad
\widehat\delta(t)=2\alpha U^3 f(\tau).
$$

For $0<\tau_1<\tau_2$, put $f_i=f(\tau_i)$ and $t_i=\tau_i/k$.
The statistic $f_2\widehat\delta(t_1)-f_1\widehat\delta(t_2)$ vanishes
for every two-state surrogate. For the target it equals
$U^3W f_1f_2(\tau_2-\tau_1)$. Therefore, with
$e_i=m_3(t_i)-\widehat m_3(t_i)=\delta(t_i)-\widehat\delta(t_i)$,

$$
\max\{|e_1|,|e_2|\}
\ge U^3W\frac{f_1f_2}{f_1+f_2}(\tau_2-\tau_1).
$$

This is the exact minimax error for these two samples: setting

$$
2\alpha=W\frac{f_1(1-\tau_1)+f_2(1-\tau_2)}{f_1+f_2}
$$

makes the two errors equal in magnitude and opposite in sign, and such
an $\alpha$ is admissible by Section 9.1. This two-sample exactness is not
a claim of optimality in the larger all-protocol norm.

Take $\tau_1=1/4$ and $\tau_2=3/2$. Direct substitution yields

$$
\frac{f_1f_2}{f_1+f_2}(\tau_2-\tau_1)
=\frac{15}{8(e^3+6e^{1/2})}.
$$

The finite sampling horizon is $3/(2k)$. Its two coefficient samples are included
in the supremum defining $\mathcal E_U$, so the same lower bound survives
the infimum over all two-state surrogates and the supremum over targets.
The independence from $k$ is a rescaling of the sampling times. The
witness uses values of the cubic coefficient directly, with no kernel
inversion or numerical differentiation in time. It remains a statement
about response coefficients, not a finite-field or noisy-data guarantee.

## 10. A logarithmic state lower bound in the response norm

The finite-accuracy question admits a lower bound for the full comparison class
$\mathcal A_D(k)$ in Section 0. It does not require a reversible surrogate, a
positive surrogate kernel, bounded rate derivatives, or a prescribed surrogate
topology. The proof uses a finite sampled Hankel matrix of the cubic **step
response**, so its error is directly controlled by $\mathcal E_U$; no unstable
differentiation of approximate response data is used. The underlying
finite-dimensional realization and Hankel-rank principle is established
mathematics, not a novelty claim.

**Theorem.** Suppose $k>0$, $U>0$, and $0<W\le G^2$. For every integer $D\ge2$,
put $r=3D-4$. Then

$$
\boxed{
E_D(k,G,W,U)\ \ge\
\frac{7U^3W}{3200\,r^3(36e)^{2r-2}}.
}
$$

The target witnessing this bound can be chosen with $r+2=3D-2$ total states,
$|g_i|=\sqrt W$, and all active internal relaxation rates in $[2k,3k]$.
Only a constant protocol $u=U$ and times at most

$$
T_D=(2r+1)\frac{\log2}{k}=(6D-7)\frac{\log2}{k}
$$

are used in the proof. The constants are conservative; no sharp exponential
rate is asserted.

### 10.1 The coefficient hierarchy gives a finite recurrence

Consider any admissible surrogate with $d\le D$ states, column generator
$L(h)=\widehat Q(h)^T$, fixed stationary preparation $p_0$, and fixed readout
$f$. Write its step-driven probability vector as

$$
p(t;\epsilon U)=p_0+\epsilon p_1(t)+\epsilon^2p_2(t)
+\epsilon^3p_3(t)+O(\epsilon^4).
$$

Let $L_j$ denote the coefficient of $\epsilon^j$ in $L(\epsilon U)$.
Conservation of probability places each $p_j$, $j\ge1$, in the
$(d-1)$-dimensional subspace
$V=\{v:\mathbf1^Tv=0\}$. Since $L_0p_0=0$, the hierarchy through order three is

$$
\begin{aligned}
\dot p_1&=L_0p_1+L_1p_0,\\
\dot p_2&=L_0p_2+L_1p_1+L_2p_0,\\
\dot p_3&=L_0p_3+L_1p_2+L_2p_1+L_3p_0.
\end{aligned}
$$

Adjoining a constant coordinate makes this an autonomous linear system
$\dot z=\mathcal Lz$ of dimension $1+3(d-1)=3d-2$. Its diagonal blocks are
$0,A,A,A$, where $A=L_0|_V$. For

$$
\Delta=\frac{\log2}{k},\qquad B=e^{A\Delta},\qquad
\mathcal B=e^{\mathcal L\Delta},\qquad a=e^{-2k\Delta}=\frac14,
$$

the sampled cubic sequence $s_n=f^Tp_3(n\Delta)$ is an output of
$\mathcal B$, whose characteristic polynomial is

$$
\chi_{\mathcal B}(z)=(z-1)\det(zI-B)^3.
$$

The prescribed passive path law forces $a$ to be an eigenvalue of $B$.
Indeed, the passive equilibrium mean is zero and its correlation is
$e^{-2kt}$. Thus $w=\operatorname{diag}(f)p_0$ lies in $V$ and
$f^TB^nw=a^n$. Applying the characteristic polynomial of $B$ to this scalar
sequence gives $\det(aI-B)a^n=0$, and hence $\det(aI-B)=0$.
This argument does not require irreducibility or diagonalizability.

Let $\mathsf E$ be the forward shift of a scalar sequence, and define

$$
P(z)=(z-1)(z-a)^2
=z^3-\frac32z^2+\frac9{16}z-\frac1{16}.
$$

The polynomial $P$ divides $\chi_{\mathcal B}$. Cayley--Hamilton therefore
shows that the filtered sequence $y=P(\mathsf E)s$ is annihilated by the
monic polynomial $\chi_{\mathcal B}/P$, of degree $3d-5$. Every sampled
Hankel matrix $(y_{i+j})$ consequently has rank at most $3d-5\le3D-5$.
This is a polynomial-quotient argument, so repeated eigenvalues, zero
eigenvalues, and Jordan blocks cause no exception.

### 10.2 A target with a positive filtered Hankel matrix

Fix $r=3D-4\ge2$ and choose equally spaced nodes and equal kernel weights:

$$
x_j=\frac1{16}+\frac{j-1}{16(r-1)},\qquad
\lambda_j=k(-\log_2x_j-1),\qquad c_j=\frac Wr,
\qquad 1\le j\le r.
$$

All rates are distinct and belong to $[2k,3k]$. By
[Theory, Section 9](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel),
the kernel $C(t)=\sum_jc_je^{-\lambda_jt}$ has a target realization in
$\mathcal F(k,G,W)$ with $r+2$ total states and $|g|=\sqrt W$.

The step formula in [Theory, Section 8](THEORY.md#8-exact-response-state-count-bound)
expresses its cubic sequence as a constant, a linear polynomial in $n$ times
$a^n$, and hidden terms

$$
-\frac{2U^3c_j}{(1-\lambda_j/k)^2}\,x_j^n.
$$

The filter $P(\mathsf E)$ removes the constant and the visible terms. The
remaining sequence is

$$
y_n=U^3\sum_{j=1}^rd_jx_j^n,\qquad
d_j=\frac{2c_j(1-x_j)(x_j-a)^2}{(1-\lambda_j/k)^2}
\ge\frac{7W}{1024r}.
$$

For the inequality, use $1-x_j\ge7/8$, $|x_j-a|\ge1/8$, and
$(1-\lambda_j/k)^2\le4$. In particular the target's $r\times r$ Hankel
matrix is positive definite:

$$
H=(y_{i+j})_{i,j=0}^{r-1}
=U^3V\operatorname{diag}(d_1,\ldots,d_r)V^T,
\qquad V_{ij}=x_j^i\quad(0\le i<r).
$$

### 10.3 An explicit smallest-eigenvalue bound

The $j$th row of $V^{-1}$ consists of the monomial coefficients of the
Lagrange polynomial

$$
\ell_j(x)=\prod_{\ell\ne j}\frac{x-x_\ell}{x_j-x_\ell}.
$$

Writing $h=1/[16(r-1)]$, the sum of the absolute values of these coefficients
is at most

$$
\frac{(9/8)^{r-1}}
{h^{r-1}(j-1)!(r-j)!}
\le
\frac{[18(r-1)]^{r-1}2^{r-1}}{(r-1)!}
\le(36e)^{r-1}.
$$

The first bound follows by multiplying the coefficient absolute sums of
the factors $x-x_\ell$; the second uses
$\binom{r-1}{j-1}\le2^{r-1}$; the last uses
$n!\ge(n/e)^n$. Consequently,

$$
\|V^{-1}\|_2\le\|V^{-1}\|_F
\le\sqrt r\,(36e)^{r-1},
$$

and therefore

$$
\lambda_{\min}(H)
\ge\frac{7U^3W}{1024\,r^2(36e)^{2r-2}}.
$$

### 10.4 Converting the rank obstruction to response error

Let $\widehat H$ be the same filtered Hankel matrix for an arbitrary
surrogate in $\mathcal A_D(k)$. Section 10.1 gives
$\operatorname{rank}\widehat H\le r-1$. A unit vector in the nullspace of
$\widehat H$ shows
$\|H-\widehat H\|_2\ge\lambda_{\min}(H)$.

If the two cubic step curves differ by at most $\varepsilon$ at all sampled
times, each filtered sample differs by at most

$$
\|P\|_{\mathrm{coeff},1}\varepsilon
=\left(1+\frac32+\frac9{16}+\frac1{16}\right)\varepsilon
=\frac{25}{8}\varepsilon.
$$

It follows that $\|H-\widehat H\|_2\le(25/8)r\varepsilon$.
Combining the two inequalities proves the theorem. The largest index
required is $2(r-1)+3=2r+1$, establishing the stated finite horizon.
Because all these samples are allowed in $\mathcal E_U$, taking the
infimum over the full surrogate class and then the supremum over targets
preserves the bound.

In particular, a uniform guarantee $E_D\le\varepsilon$ requires

$$
\log\frac{U^3W}{\varepsilon}
\le\log\frac{3200}{7}+3\log(3D-4)+(6D-10)\log(36e).
$$

For fixed $U^3W>0$, this gives a necessary state count
$\Omega(\log(U^3W/\varepsilon))$ as $\varepsilon\downarrow0$.
Together with Section 8, the current unrestricted target class therefore
has logarithmic necessary and squared-logarithmic sufficient state growth.
The gap between these orders remains open; neither bound is a minimax
optimality claim for that class.

### 10.5 An upper bound on active rates gives matching logarithmic order

An upper bound on the active target rates is enough to determine the
state-count order. Let $E_D^{\le3k}$ be the same
minimax problem with target kernels restricted to active rates
$0<\lambda_j\le3k$, retaining the full broad surrogate class
$\mathcal A_D(k)$. No positive lower bound on the hidden spectral gap is
added.

The lower-bound target above already lies in this class. For an upper
bound, all dimensionless damped rates lie in $(1,4]$. Divide them between
$(1,2)$ and $[2,4]$. Apply Section 8.1 with $d$ quadrature nodes to each
nonempty bin, retaining a bin exactly if its support has at most $d$
points. The two integrated errors sum to at most $4W16^{-d}$ in
dimensionless time. Thus the cubic response error is at most
$8U^3W16^{-d}$, and the compressed kernel has at most $2d$ modes.
The Jacobi realization uses at most $2d+2$ states, with the original mass
and sensitivity bound. Its nodes in the first bin remain strictly greater
than one because its finite target support does, so every realized
internal rate is strictly positive.

Consequently, with $r=3D-4$ and $d=\lfloor(D-2)/2\rfloor$, every $D\ge4$
satisfies

$$
\frac{7U^3W}{3200\,r^3(36e)^{2r-2}}
\le E_D^{\le3k}
\le8U^3W\,16^{-\lfloor(D-2)/2\rfloor}.
$$

The necessary and sufficient number of states therefore grows as
$\Theta(\log(U^3W/\varepsilon))$ at small tolerance in this rate-capped
target class. This matches the order, not the constants in the exponential
error rate. The upper-bound construction extends to any fixed finite
upper bound on $\lambda_j/k$ by using finitely many bins.

The rate cap is additional information about the **targets**, not a
restriction on the surrogates. It does not narrow the original problem
$E_D$ or close its logarithmic versus squared-logarithmic gap. The upper
bound uses the established positive-quadrature method already discussed
in Section 8; these derivations do not certify publication-level novelty.
