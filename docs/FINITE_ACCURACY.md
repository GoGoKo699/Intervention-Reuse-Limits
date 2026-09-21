# Exact complexity is not fixed-accuracy complexity

[Repository overview](../README.md) · [Core derivation](THEORY.md) · [Prior art](PRIOR_ART.md)

**Working extension, 22 September 2026.** This note contains two complementary derivations. Their mathematical consistency has been checked; originality and optimality have not been established.

The core example has an exact two-state passive description and an $N$-state exact cubic response requirement. This note first keeps that separation at nonvanishing total signal, then proves a constructive response-approximation bound independent of $N$. The approximation is itself realizable by a reversible Markov model, not only a formal memory equation.

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

For fixed $k$, consider two kernels with equal mass $C(0)=\widetilde C(0)=W$. Let $m_3[u]$ and $\widetilde m_3[u]$ denote their cubic mean-response coefficients for the same zero-field preparation and protocol $|u(t)|\le U$.

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

The paired realization is an explicit construction, not a claim of minimal state count for a prescribed kernel. Positivity and realization theory require further prior-art comparison.

## 6. Consequence for the research claim

For any fixed coefficient tolerance $\varepsilon>0$, choosing

$$
q\ge\max\left(1,\left\lceil\frac{U^3W}{\varepsilon}\right\rceil\right)
$$

produces an admissible surrogate with at most $2q+1$ states, **independent of the microscopic state count $N$**. Thus a universal fixed-accuracy lower bound growing with $N$ is ruled out for this model family and this unrestricted surrogate class, at cubic order and bounded $W,U$.

The resulting scientific distinction is not simply that the first construction had weak total signal. Exact complexity can grow without bound even with a nonvanishing response correction, while finite-accuracy complexity is controlled by tolerance and kinetic-kernel information.

The $1/q$ error rate is an elementary upper bound, not a minimax or novelty claim. Positive exponential approximation has an established literature, including stronger rates under different assumptions; see [the audit](PRIOR_ART.md). A useful publication contribution must survive that comparison, specify the physically meaningful task, and address optimality or a sharper operational distinction.

## 7. Checks and remaining boundary

[The executable extension](../scripts/verify_finite_accuracy.py) verifies the normalized spectral weights, nonvanishing signal bound, positive reversible realization, and agreement of its master equation with the memory equations. It also tests the protocol certificate on deterministic sign-changing protocols. See [verification details](VERIFICATION.md).

Still not established: the optimal dependence on tolerance, stable inference from finite noisy data, a finite-field remainder uniform in system size and observation horizon, or a specific fluid or molecular implementation. No large simulation is needed for the present derivations. The [next work order](../work_orders/CURRENT.md) targets these mathematical and novelty issues rather than a simulation campaign.
