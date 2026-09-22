# No finite response order determines a fixed actuator's predictions

[Repository overview](../README.md) · [Model](THEORY.md) · [Finite-field theorem and its boundary](FINITE_FIELD.md) · [Visible path response](ACTIVE_PATH_RESPONSE.md)

**Research theorem, 22 September 2026.** The finite-field theorem uses a particular actuator geometry in which one scalar kernel is a complete prediction statistic. This note proves an obstruction in the general sensitivity family: an arbitrarily long response hierarchy can agree while actual driven predictions differ, even when the two models have exactly the same state labels, $k$, $\mu$, $g$, and field-dependent external transition rates. Only the reversible internal generator changes. The proof uses finite orthogonal polynomials and a positive perturbation of a refresh generator. It is an internal derivation, not an originality certification.

## 1. Statement and quantifiers

Fix

$$
k>0,\qquad \lambda>0,\qquad G>0,\qquad 0<W<G^2.
$$

For every integer $d\ge2$, there exist $d+2$-state models in the original family with the following properties.

- Within the constructed pair, the state labels, $k$, stationary weights $\mu$, and sensitivity vector $g$ are identical. They satisfy $\langle g\rangle_\mu=0$, $\langle g^2\rangle_\mu=W$, and $\|g\|_\infty=G$.
- The internal generators are irreducible, reversible under this same $\mu$, and different. All nonzero internal relaxation rates lie in $[\lambda,3\lambda/2]$, independently of $d$. Their common cubic kernel is $C(t)=We^{-\lambda t}$.
- For every bounded piecewise-continuous protocol $h(t)=\epsilon u(t)$, every finite horizon, and every time on that horizon, the mean-response coefficients through order $2d$ agree.
- Their order-$(2d+1)$ mean coefficients differ for the constant unit protocol. Their actual mean curves differ under every constant field $h\ne0$.
- More strongly, their complete visible-path response coefficients through order $2d-1$ agree for every such protocol and horizon. A no-exit statistic first separates them at order $2d$.

All preparations are the same zero-field equilibrium. Thus, for any prescribed finite mean-response order $L$, choosing $d\ge\max\{2,\lceil L/2\rceil\}$ gives a pair whose mean responses agree through $L$ but whose finite-field predictions differ.

The full tuple $(\mu,g)$ is fixed **between the two models at each chosen depth $d$**. The construction permits this tuple and the state space to change when $d$ changes; it does not claim that one fixed finite state space conceals infinitely many successive response orders. The strict interior condition $W<G^2$ is substantive for this construction. The endpoint case $W=G^2$ is not addressed here.

## 2. Fixed bounded sensitivities with any prescribed interior variance

Use two sensitivity values $-G,+G$, and $d-1$ distinct interior values. For $d=2$, the sole interior value is zero. For $d\ge3$, set

$$
a=\min\{G/2,\sqrt{W/2}\},\qquad
y_j=a\left(\frac{2j}{d-2}-1\right),\quad 0\le j\le d-2.
$$

Let $\nu$ be the uniform probability measure on these interior values, and let $v=\int x^2\,d\nu(x)$. The interior distribution is symmetric and $0\le v<W$. Define

$$
\alpha=\frac{G^2-W}{G^2-v}\in(0,1),\qquad
\mu=\alpha\nu+\frac{1-\alpha}{2}(\delta_{-G}+\delta_G).
$$

Use its $d+1$ distinct support values as the entries of $g$, and its strictly positive masses as the hidden stationary distribution. This gives exactly the required centering, variance and sensitivity bound. These support values and weights will remain unchanged throughout the generator comparison.

Let $w$ be the degree-$d$ orthonormal polynomial evaluated on these support values, with positive leading coefficient. Thus

$$
\langle w,w\rangle_\mu=1,\qquad
\langle w,g^j\rangle_\mu=0\quad(0\le j<d).
$$

There is no degeneracy: a nonzero polynomial of degree at most $d$ cannot vanish at all $d+1$ distinct support points. In particular,

$$
\gamma_d:=\langle w,g^d\rangle_\mu>0.
$$

Indeed, if the leading coefficient of $w$ is $\kappa_d>0$, then $g^d=\kappa_d^{-1}w$ plus a lower-degree polynomial, giving $\gamma_d=\kappa_d^{-1}$.

## 3. A positive family that changes only one hidden mode

Write

$$
P_w f=w\langle w,f\rangle_\mu,\qquad
K_\theta=\lambda(\mathbf1\mu^T-I)-\theta P_w.
$$

Let $M=\max_i|w_i|$, and choose two distinct parameters in

$$
0\le\theta\le\frac{\lambda}{2M^2}.
$$

For $i\ne j$,

$$
(K_\theta)_{ij}=\mu_j(\lambda-\theta w_iw_j)
\ge\frac{\lambda\mu_j}{2}>0.
$$

Both terms annihilate the constant vector, so rows sum to zero. Moreover $\mu_i(K_\theta)_{ij}=\mu_j(K_\theta)_{ji}$. Hence every member is an irreducible reversible Markov generator with the same invariant law $\mu$.

It acts as zero on constants, as $-(\lambda+\theta)$ on $w$, and as $-\lambda$ on every centered vector orthogonal to $w$. Since $M\ge1$, all nonzero internal relaxation rates lie in the fixed band $[\lambda,3\lambda/2]$, independently of $d$. The delayed distinction does not require a growing rate range or a vanishing spectral gap. In particular, $d\ge2$ ensures $w\perp g$, so

$$
K_\theta g=-\lambda g,\qquad C_\theta(t)=We^{-\lambda t}.
$$

The full field-dependent generators differ by the same projector at every field:

$$
Q_{\theta_2}(h)-Q_{\theta_1}(h)
=-(\theta_2-\theta_1)\,a b,
$$

where

$$
a=(0,w)^T,\qquad b=(0,\mu_1w_1,\ldots,\mu_{d+1}w_{d+1}).
$$

All external rates $k\mu_j e^{(1+g_j)h}$ and $ke^{(g_j-1)h}$ remain exactly fixed. Changing an equilibrium distribution or changing how the actuator couples to a state is not part of the construction.

## 4. Why every bounded protocol has the same mean jet

The statement concerns Taylor coefficients in $\epsilon$ at each fixed finite horizon, not a uniform remainder as the horizon grows. Finite matrices and bounded $u$ make all propagators analytic in $\epsilon$ in this setting.

### Polynomial filtration

Let $\mathcal F_\ell$ be the space of state functions whose value at $A$ is arbitrary and whose hidden values form a polynomial in $g$ of degree at most $\ell$. The two-dimensional space $\mathcal F_0$ consists of block-constant functions. The zero-field generator preserves each $\mathcal F_\ell$: the refresh part preserves polynomial degree, the projector either annihilates a polynomial of degree below $d$ or adds a multiple of $w$ of degree $d$.

Write

$$
Q_\theta(h)=Q_\theta(0)+\sum_{j\ge1}h^j Q_j.
$$

All $Q_j$ with $j\ge1$ are independent of $\theta$. Their hidden action is

$$
(Q_j f)_{B_i}=\frac{k}{j!}(g_i-1)^j(f_A-f_{B_i}),
$$

so $Q_j\mathcal F_\ell\subseteq\mathcal F_{\ell+j}$. Use the inner product weighted by the common full equilibrium $\pi_0=(1/2,\mu/2)$. The adjoint hidden action is

$$
(Q_j^*f)_{B_i}=\frac{k}{j!}
\left[(g_i+1)^j f_A-(g_i-1)^j f_{B_i}\right].
$$

Thus $Q_j^*$ also raises polynomial degree by at most $j$. There is an additional cancellation for the stationary initial relative density $\mathbf1$:

$$
(Q_j^*\mathbf1)_{B_i}
=\frac{k}{j!}\left[(g_i+1)^j-(g_i-1)^j\right],
$$

which has degree at most $j-1$.

Let $p_{\theta,\epsilon}(s)$ be the forward row distribution from $\pi_0$. Its order-$n$ relative-density coefficient belongs to $\mathcal F_{n-1}$ for $1\le n\le d$. This follows by induction in the coefficient equation: the direct source $Q_n^*\mathbf1$ has degree at most $n-1$, every lower-order source $Q_j^*r_{n-j}$ has the same degree bound, and the zero-field semigroup preserves that space. Consequently,

$$
p_{\theta,\epsilon}(s)a=O(\epsilon^{d+1}).
\tag{1}
$$

For the backward transition operator $U_{\theta,\epsilon}(s,t)$, the order-$n$ coefficient of $U_{\theta,\epsilon}(s,t)S$ belongs to $\mathcal F_n$. This follows from the time-ordered expansion: the final observable $S$ lies in $\mathcal F_0$, every field insertion of order $j$ raises degree by at most $j$, and zero-field propagation preserves degree. Hence

$$
b\,U_{\theta,\epsilon}(s,t)S=O(\epsilon^d).
\tag{2}
$$

Both estimates mean that the indicated earlier Taylor coefficients vanish; their remainder constants may depend on the chosen finite horizon and bounded protocol.

### Exact difference formula

Duhamel's formula, with $\Delta\theta=\theta_2-\theta_1$, gives

$$
\begin{aligned}
m_{\theta_2,\epsilon}(t)-m_{\theta_1,\epsilon}(t)
=-\Delta\theta\int_0^t
\bigl[p_{\theta_1,\epsilon}(s)a\bigr]
\bigl[b\,U_{\theta_2,\epsilon}(s,t)S\bigr]ds.
\end{aligned}
$$

Combining (1) and (2), the difference starts no earlier than order $\epsilon^{2d+1}$. This proves equality through order $2d$ for every bounded protocol, not just for a step or for finitely many time derivatives.

The extra field order on the forward side is essential. It comes from the specified stationary preparation and the cancellation of the leading $g^j$ terms in $Q_j^*\mathbf1$; a different microscopic preparation need not have the same delay.

## 5. The next order differs, and so does every nonzero step

For a constant field $h$, write $Q_\theta(h)=M(h)+\overline K_\theta$, where $M$ contains only the external transitions. Since $\pi_0\overline K_\theta=0$ and $\overline K_\theta S=0$, the first two time derivatives of the mean are independent of $\theta$, while

$$
\left.\partial_t^3 m_\theta[h](t)\right|_{t=0}
=\pi_0M^3S+\pi_0M\overline K_\theta MS.
$$

The hidden components of $\pi_0M$ and $MS$ are respectively

$$
k\mu_j e^{hg_j}\sinh h,
\qquad -2k e^{-h}e^{hg_j}.
$$

Therefore the exact difference is

$$
\boxed{
\left.\partial_t^3(m_{\theta_2}[h]-m_{\theta_1}[h])\right|_{t=0}
=2k^2\Delta\theta\,e^{-h}\sinh h\,
\langle w,e^{hg}\rangle_\mu^2.
}
\tag{3}
$$

Orthogonality gives

$$
\langle w,e^{hg}\rangle_\mu
=\frac{\gamma_d}{d!}h^d+O(h^{d+1}).
$$

For the unit-step Taylor coefficients, (3) yields

$$
\boxed{
m_{2d+1,\theta_2}(t)-m_{2d+1,\theta_1}(t)
=\frac{k^2\Delta\theta\,\gamma_d^2}{3(d!)^2}t^3+O(t^4).
}
\tag{4}
$$

The coefficient is nonzero. Together with Section 4, this identifies the first mean-response order at which the pair differs.

In fact (3) is nonzero at every real $h\ne0$. If $x_0<\cdots<x_d$ are the sensitivity support values, the functional $f\mapsto\langle w,f(g)\rangle_\mu$ annihilates all polynomials of degree below $d$ and sends $x^d$ to $\gamma_d$. Uniqueness of that annihilating functional on $d+1$ nodes gives

$$
\langle w,e^{hg}\rangle_\mu
=\gamma_d[x_0,\ldots,x_d]e^{hx}.
$$

The divided-difference mean-value theorem writes the right side as $\gamma_d h^d e^{h\xi}/d!$ for some $\xi$ between the extreme nodes. It is nonzero whenever $h\ne0$. Thus equality of an arbitrarily long response jet does not imply equality of the actual step-response curve even for this one unchanged actuator.

## 6. Complete path information is also delayed to arbitrary order

The conclusion can be strengthened beyond the mean. Use the exact conditional likelihood representation in [ACTIVE_PATH_RESPONSE.md](ACTIVE_PATH_RESPONSE.md#2-exact-conditional-likelihood-and-its-expansion), relative to the ordinary driven two-state reference. Conditional on a visible path, each $B$ interval contains a stationary $K_\theta$ process, independently of the other intervals.

The coefficient at field order $n$ is a finite sum of time integrals and endpoint terms involving stationary hidden correlations of powers of $g$. Each factor of degree $j$ in $g$ costs at least $j$ field orders: this follows directly by expanding $e^{\epsilon ug}$, the endpoint factor $\epsilon ug$, and the likelihood exponential. The deterministic moments $G(\epsilon u)$ are the same for all $\theta$ because $\mu,g$ are fixed. Products from distinct $B$ intervals preserve the total degree bound.

Within one interval a typical hidden correlation has the form

$$
\langle 1,D_g^{j_1}e^{K_\theta t_1}
D_g^{j_2}\cdots e^{K_\theta t_{r-1}}D_g^{j_r}1\rangle_\mu,
\qquad \sum_{\ell=1}^rj_\ell\le n.
$$

Zero exponents may be omitted. Multiplication by $g^j$ raises polynomial degree by at most $j$. Moreover,

$$
e^{K_{\theta_2}t}-e^{K_{\theta_1}t}
=\left(e^{-(\lambda+\theta_2)t}-e^{-(\lambda+\theta_1)t}\right)P_w.
$$

Telescope a difference of two such correlations at a changed semigroup factor. For a nonzero term, the accumulated degree on each side of $P_w$ must be at least $d$: constants start at degree zero, and all other semigroups preserve polynomial degree. Hence every correlation of total degree less than $2d$ is identical. The same is true for every conditional-likelihood coefficient through order $2d-1$.

The finite-horizon integrability argument from the path-response note applies unchanged: $g$ is bounded, visible jump counts under the reference have exponential moments, and the expanded likelihood has a polynomial-times-exponential envelope in that count. Therefore equality holds after integration against any bounded visible-path observable. This is complete path-response agreement, not only agreement of a selected list of correlations.

To show that order $2d$ actually differs, start from $\pi_0$, condition on $S_0=+1$, and observe the first exit from $B$. Its survival is

$$
R_{h,\theta}(t)=\mu^T e^{(K_\theta-D_h)t}\mathbf1,
\qquad D_h=k e^{-h}\operatorname{diag}(e^{hg}).
$$

The first two time derivatives do not involve $\theta$. In the third derivative, the only varying term is $\mu^TD_hK_\theta D_h\mathbf1$. Thus

$$
\left.\partial_t^3(R_{h,\theta_2}-R_{h,\theta_1})\right|_{t=0}
=-k^2\Delta\theta\,e^{-2h}\langle w,e^{hg}\rangle_\mu^2.
$$

Consequently,

$$
R_{2d,\theta_2}(t)-R_{2d,\theta_1}(t)
=-\frac{k^2\Delta\theta\,\gamma_d^2}{6(d!)^2}t^3+O(t^4)\ne0.
$$

The conditioning is purely on the visible initial state and does not introduce a different hidden preparation. Multiplying by the common initial probability $1/2$ converts it into a joint path event under the original preparation.

## 7. What this obstruction establishes

Within the general sensitivity family, neither the cubic kernel nor any fixed finite number of additional mean-response orders is a universally complete prediction statistic. Even allowing all bounded visible-path measurements at any prescribed finite response order does not remove the obstruction: the construction can postpone their first distinction beyond that order as well.

This explains why a structural actuator condition can do work that a longer calibration hierarchy cannot do universally. In the finite-field theorem's distinguished subclass, the scalar kernel supplies full finite-field prediction. In the broader class here, the very same one-mode kernel can coexist with arbitrarily delayed additional response information.

The result is an exact identifiability obstruction. It does not give a finite-error minimax state lower bound, a noise-robust separation uniform in $d$, a lower bound on the number of experimental trials, or an impossibility of using finite-field calibration data. The interval of allowed projector perturbations and the first nonzero coefficient can shrink with $d$. Finite-order calibration can still support a prescribed finite-horizon accuracy when accompanied by an appropriate remainder bound; this theorem rules out exact completeness, not such approximation certificates. It also does not show failure for one fixed finite state space at every response order. Those distinctions matter when using the theorem to motivate a prediction or compression task.
