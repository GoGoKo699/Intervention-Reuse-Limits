# Uniform rate regularization with a logarithmic accuracy loss

[Repository overview](../README.md) · [Earlier rate regularization](GENERAL_FINITE_FIELD_UPPER_BOUND.md#3-replace-arbitrarily-fast-internal-rates-by-a-bounded-clock) · [Reversible general compression](REVERSIBLE_GENERAL_COMPRESSION.md#3-two-preliminary-approximations)

**Working refinement, 23 September 2026.** Every finite reversible hidden model in the original exponential field rule has a same-state reversible approximation, uniformly over all bounded protocols and all horizons, with internal outgoing and spectral cap $O_R(k\delta^{-1}\log(1/\delta))$. It retains the stationary law, every actuator label, the complete exact actuator histogram, zero-field preparation, and original external rule. No lower bound on stationary masses or internal spectral gap is assumed. A prescribed positive internal lower gap is not retained by the rate transformation.

The Poisson rate transformation and its pointwise semigroup estimate already appear in the earlier general finite-field upper bound. The quantitative refinement here uses bounded driven densities and the common reset to avoid its finite-horizon exponential Gronwall loss. It does not remove the fixed rival rate-cap assumption from the binary or multilevel reversibility lower bounds: that requires tracking their constants as the cap grows with inverse accuracy. This note makes no novelty claim for the classical semigroup and uniformization ingredients.

## Conventions

There is one visible state $A$ and $d$ hidden states. A row generator acts on column functions. The hidden generator $K$ is reversible under the positive probability vector $\mu$. Its external rates are

$$
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad q_{iA}(h)=k e^{(g_i-1)h},
$$

Assume $|g_i|\le G$ and $|h(t)|\le H$. Put $R=e^{(1+G)H}$ and $\alpha=k/R$. Initial preparation is $\pi_0=(1/2,\mu/2)$. The readout $s$ is $-1$ on $A$ and $+1$ on hidden states. A forward probability $p$ is represented by its density $\rho_x=p_x/\pi_0(x)$. The Hilbert space is $L^2(\pi_0)$, and the forward density generator is $Q(h)^*$, where the adjoint is in this fixed Hilbert space. In particular, the hidden internal forward density generator is $K$ itself, by reversibility. All constants below are independent of $d$, $\mu$, and the spectrum of $K$.

## A sharper all-horizon Poisson capping lemma

For $\Delta>0$ define

$$
K_\Delta=(e^{\Delta K}-I)/\Delta.
$$

It is a reversible Markov generator with the same $\mu$ and outgoing rates at most $1/\Delta$. It is irreducible when $K$ is irreducible, because $e^{\Delta K}$ then has positive entries. It leaves every actuator label and the entire actuator histogram unchanged. Its spectrum lies in $[-1/\Delta,0]$. Let $m$ and $m_\Delta$ be the two actual controlled means, with the same preparation and original external rule.

**Claim.** With

$$
B=2k(R-1),\qquad
J_R=\frac{\sqrt{2+2R^2}}{\alpha},
$$

one has

$$
\sup_{h,t}|m_\Delta[h](t)-m[h](t)|
\le \sqrt2 R B(1+BJ_R) I_\Delta,
\tag{1}
$$

where

$$
I_\Delta=\int_0^\infty e^{-ku}
\min\{1,2\Delta/u\}\,du
\le2\Delta\left[2+\log_+\frac1{2k\Delta}\right].
\tag{2}
$$

Here $\log_+(x)=\max\{0,\log x\}$. Thus the error is $O_R(k\Delta[1+\log_+(1/(k\Delta))])$. The statement covers arbitrary deterministic bounded measurable protocols for which the finite-dimensional nonautonomous evolution is defined; piecewise continuous protocols suffice.

### 1. Uniform forward-density bound

Write $\rho_A=2p_A$ and $\rho_i=2p_i/\mu_i$. Their hidden density equation is

$$
\dot\rho_i=(K\rho)_i
+k\rho_A e^{(1+g_i)h}
-k e^{(g_i-1)h}\rho_i.
$$

Since $\rho_A\le2$, the source is at most $2kR$ and the killing is at least $\alpha$. The positive-semigroup comparison principle, or the maximum principle applied to the constant supersolution, gives

$$
0\le \rho_i(t)\le e^{-\alpha t}
+2R^2(1-e^{-\alpha t})\le2R^2.
$$

The $A$ density is at most $2\le2R^2$. Since $\rho$ integrates to one,

$$
\|\rho(t)\|_2\le\sqrt2 R.
\tag{3}
$$

Exactly the same bound holds with $K_\Delta$. No lower bound on individual $\mu_i$ enters.

### 2. A decaying $L^2$ bound for zero-mass data

Let $J_A$ be the row stochastic matrix whose every row puts mass one at $A$. The residual generator

$$
Q^{\rm res}(h)=Q(h)-\alpha(J_A-I)
$$

is Markov: it reduces every hidden-to-$A$ rate by $\alpha$ and leaves the $A$-to-hidden rates and internal generator unchanged. Write $U(t,s)$ and $U_{\rm res}(t,s)$ for the corresponding forward density propagators.

For residual evolution started from density one at time $s$, the $A$ density stays $\le2$ and the hidden killing rates are nonnegative. On an interval of length $u=t-s$ the maximum principle therefore gives

$$
U_{\rm res}(t,s)1\le 2+2kRu
$$

pointwise. Positivity yields the same upper bound for the $L^\infty$ operator norm. A Markov forward density propagator has $L^1(\pi_0)$ operator norm one. Interpolation consequently gives

$$
\|U_{\rm res}(t,s)\|_{2\to2}
\le\sqrt{2+2kRu}.
$$

If $x$ has zero $\pi_0$ integral, $J_A^*x=0$, and the residual evolution preserves its zero integral. Hence

$$
U(t,s)x=e^{-\alpha u}U_{\rm res}(t,s)x,
\qquad
\|U(t,s)x\|_2
\le e^{-\alpha u}\sqrt{2+2kRu}\,\|x\|_2.
\tag{4}
$$

Jensen's inequality under the exponential probability density $\alpha e^{-\alpha u}$ gives

$$
\int_0^\infty e^{-\alpha u}\sqrt{2+2kRu}\,du
\le\alpha^{-1}\sqrt{2+2kR/\alpha}=J_R.
\tag{5}
$$

The factor growing as $\sqrt u$ is integrable against the reset exponential. This step is what replaces the finite-horizon exponential Gronwall loss.

### 3. The semigroup error has an additional $e^{-kt}$

Let $Q_0$ and $Q_{0,\Delta}$ be the full zero-field generators. In $L^2(\pi_0)$, both have the same two-dimensional visible subspace, with eigenvalues $0$ and $-2k$. On the orthogonal subspace of hidden centered functions they act as $K-kI$ and $K_\Delta-kI$. Thus, putting $T_0(u)=e^{uQ_0}$ and $T_\Delta(u)=e^{uQ_{0,\Delta}}$,

$$
\|T_\Delta(u)-T_0(u)\|_{2\to2}
\le e^{-ku}\min\{1,2\Delta/u\}.
\tag{6}
$$

The minimum bound is exactly the scalar spectral estimate already proved in the repository. The extra factor $e^{-ku}$ follows from the hidden-to-$A$ exit at zero field and remains available without an internal spectral gap. Integrating (6) gives $I_\Delta$. For $2k\Delta\le1$, split the integral at $2\Delta$ and $1/k$ to obtain the upper bound $2\Delta[1+\log(1/(2k\Delta))+e^{-1}]$, which implies (2). For $2k\Delta>1$, use $I_\Delta\le1/k\le2\Delta$.

### 4. Volterra resolvent estimate

The field perturbation $V_h=Q(h)-Q_0$ is unchanged when $K$ is replaced by $K_\Delta$ and satisfies

$$
\|V_h\|_{2\to2}=\|V_h^*\|_{2\to2}\le B.
$$

Indeed, in the $A$/hidden block decomposition every block difference has norm $\le k(R-1)$, giving the factor two. Let $\rho$ and $\rho_\Delta$ be the actual forward densities. Since both zero-field semigroups fix the initial density one, their variation-of-constants equations imply, with $w=\rho_\Delta-\rho$,

$$
w(t)=F(t)+\int_0^t T_0(t-s)V_{h(s)}^*w(s)\,ds,
$$

$$
F(t)=\int_0^t[T_\Delta(t-s)-T_0(t-s)]
V_{h(s)}^*\rho_\Delta(s)\,ds.
$$

By (3) and (6), $\sup_t\|F(t)\|_2\le\sqrt2 R B I_\Delta$. The function $F$ has zero integral, since the semigroup difference annihilates total mass. The exact Volterra resolvent identity is

$$
w(t)=F(t)+\int_0^t U(t,s)V_{h(s)}^*F(s)\,ds.
\tag{7}
$$

This follows by expanding the bounded Volterra kernel on a finite interval and rearranging the absolutely convergent iterated integrals. Equivalently, substitute the Duhamel equation for $U$ into the right side. Since $V_h1=0$, $V_h^*F$ also has zero integral. Equations (4)-(5) bound the right side of (7) by $\sqrt2 R B I_\Delta(1+BJ_R)$. Finally $\|s\|_2=1$, so the same bound applies to the mean difference. This proves (1), directly for all horizons.

### 5. An explicit sufficient cap

Set

$$
C_R=4\sqrt2 R(R-1)
\left[1+2R(R-1)\sqrt{2+2R^2}\right],\qquad A_R=\max\{1,C_R\}.
$$

Equations (1)-(2) imply an error $\le C_Ra[2+\log_+(1/(2a))]$ for $a=k\Delta$. For $0<\delta<1$, choose

$$
a=\frac{\delta}{4A_R\log(e+A_R/\delta)}.
\tag{8}
$$

Then the error is $\le\delta$, and the outgoing-rate and spectral cap are at most

$$
\boxed{\frac1\Delta=
\frac{4kA_R}{\delta}\log(e+A_R/\delta).}
\tag{9}
$$

For verification, write $x=A_R/\delta\ge1$ and $L=\log(e+x)\ge1$. Then $\log(2xL)\le2L$ because $\log x\le L$ and $\log(2L)\le L$. The bracket $2+\log(2xL)$ is $\le4L$. When $R=1$ the original and capped means agree exactly, and no bound is needed.

This rate regularization keeps exactly the same physical states and scalar labels. It does not by itself transfer a capped lower theorem with constants fixed in the rival cap: the necessary cap in (9) grows with inverse accuracy.

