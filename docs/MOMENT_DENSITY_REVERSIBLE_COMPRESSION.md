# Polynomial reversible compression from conductance tails and moments

[Repository overview](../README.md) · [Bounded-density sampling](BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) · [Bounded-rate finite-alphabet bounds](BOUNDED_RATE_FINITE_FIELD.md) · [General reversible compression](REVERSIBLE_GENERAL_COMPRESSION.md)

**Research theorem, 22 September 2026.** A uniform global $L^{1+\alpha}$ moment of the internal conductance density, together with a fixed spectral cap and finite actuator alphabet, suffices for polynomial-size reversible prediction of the actual controlled mean. A pointwise density bound is unnecessary. Symmetric clipping is charged directly in the driven-mean norm; concentration and one common rescaling keep the surrogate's update clock independent of the clipping threshold.

The result preserves ordinary detailed balance and the exact actuator histogram. The original spectral-band endpoints need not be retained. A matching-edge example below proves that a spectral cap alone cannot justify density clipping, even in the actual-mean norm. This is a limitation of that approximation step, not a lower bound on optimal reversible compression: the example has an exact three-state controlled realization.

Clipping, Bernstein concentration, stratified sampling, reversible weighted graphs, and regeneration are established tools. The constrained combination here is an internal derivation, not a certification of originality.

## 1. A tail-dependent theorem and a uniform moment corollary

Fix $k,\Lambda,G,H>0$ and an integer $m\ge2$. Let the supplied target belong to the original finite reversible family, with stationary hidden law $\mu$, irreducible internal generator $K$, and every nonzero eigenvalue of $-K$ at most $\Lambda k$. Let its centered actuator take exactly $m$ positive-mass values $z_a\in[-G,G]$, with masses $\rho_a=\mu(g=z_a)>0$. There is no lower bound on a microscopic mass or actuator-level mass.

Define the dimensionless symmetric conductance density and its global excess tail by

$$
q(x,y)=\begin{cases}K_{xy}/(k\mu_y),&x\ne y,\\0,&x=y,\end{cases}
\qquad
\tau(B)=\sum_{x,y}\mu_x\mu_y(q(x,y)-B)_+.
\tag{1}
$$

Put

$$
R=e^{(1+G)H},\qquad A_H=e^{2GH},\qquad C_R=1+2R^2,
$$

$$
\beta=\log\left(1+\frac1{\Lambda R}\right),\qquad
p_\Lambda=\frac{\log m}{\beta}.
\tag{2}
$$

For $0<\delta<1$, choose any $B\ge\Lambda$ such that

$$
R^3\tau(B)\le\delta/2,
\qquad b=B/\Lambda\ge1.
\tag{3}
$$

Such a threshold exists for each finite target. There is a surrogate in the original reversible family, using the same external-field rule and zero-field equilibrium preparation, with

$$
\boxed{
\sup_{T>0}\sup_{|h|\le H}\sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|\le\delta.
}
\tag{4}
$$

Protocols are deterministic and piecewise continuous. Its physical-state count satisfies

$$
\boxed{
D\le C_{m,\Lambda,G,H}\,b\delta^{-2(1+p_\Lambda)}
\log^2(2/\delta)
\bigl[\log(2/\delta)+\log(2b)\bigr].
}
\tag{5}
$$

The surrogate has a fixed binary readout and fixed stationary preparation. It is irreducible and ordinarily reversible, and preserves every actuator value and its exact mass. Thus centering, variance $W$, sensitivity bound, the passive telegraph law, equilibrium curve, reference linear mean response, and zero quadratic mean response are retained. Internal outgoing rates are at most $\Lambda k$ and internal relaxation rates are at most $2\Lambda k$. The original spectral-band endpoints are not generally preserved.

The threshold in (3) can depend on the target. Consequently (5) alone does not give a uniform polynomial over all spectrally capped targets.

**Uniform moment corollary.** Additionally fix $\alpha>0$ and $M<\infty$, and assume only the global bound

$$
\sum_{x,y}\mu_x\mu_yq(x,y)^{1+\alpha}\le M.
\tag{6}
$$

No uniform rowwise moment assumption is needed. Since $\tau(B)\le M/B^\alpha$, choose

$$
B=\max\left\{\Lambda,
\left(\frac{2R^3M}{\delta}\right)^{1/\alpha}\right\}.
\tag{7}
$$

Then (5) gives the dimension-free polynomial

$$
\boxed{
D\le C_{m,\Lambda,G,H,\alpha,M}
\delta^{-[2(1+p_\Lambda)+1/\alpha]}\log^3(2/\delta).
}
\tag{8}
$$

The clock exponent $p_\Lambda$ depends on the fixed spectral cap, not on the clipping threshold or the density moment. The extra exponent $1/\alpha$ comes from the linear sample-size dependence on $B$. If the centered actuator has only one value, it is zero and the ordinary two-state model is exact. A bound for at most a prescribed number of levels follows by using the actual number of positive-mass levels.

## 2. Explicit parameters and success probability

For any threshold satisfying (3), set

$$
\ell=\max\left\{1,
\left\lceil\frac{\log(4C_R/\delta)}{\beta}\right\rceil-1
\right\},
\qquad
\eta=\frac{\delta}{2C_RA_Hm^{\ell+1}(3\ell+1)},
\tag{9}
$$

$$
V=\sum_{r=1}^{\ell+1}m^r,\qquad
J=\log\left(\frac{32m(V+1)b}{\eta}\right),\qquad
n=\left\lceil512b\eta^{-2}J\right\rceil.
\tag{10}
$$

Sample $n$ microscopic states independently within each actuator level according to its conditional stationary law. All draws in all strata are independent; repeated draws remain distinct physical replicas. The construction below succeeds with probability at least

$$
1-e^{-37J}-e^{-1023J}>0,
\tag{11}
$$

and each good realization gives $D=1+mn$ total states. The choices ensure $0<\eta<1/2$ and $n\ge2b/\eta$.

This is an existence construction from the supplied full target, with a finite checkable good event. It is not a claim about learning an unknown generator, polynomial runtime, or parameter precision.

## 3. Symmetric clipping costs only a stationary weighted flux

Rescale time so $k=1$ until the end. The spectral cap and reversibility imply

$$
-K_{xx}\le\Lambda(1-\mu_x)\le\Lambda,
\qquad
\sum_y\mu_yq(x,y)\le\Lambda.
\tag{12}
$$

For the first inequality, apply the quadratic-form bound for $-K$ to the indicator of $x$ after subtracting its stationary mean.

Clip the density symmetrically:

$$
q_B(x,y)=\min\{q(x,y),B\},\qquad
(K_Bu)(x)=\sum_y\mu_yq_B(x,y)[u(y)-u(x)].
\tag{13}
$$

The clipped generator has the same stationary law and reversibility. It retains the connected support, hence irreducibility. Its Dirichlet form is bounded above by that of $-K$, so its relaxation-rate cap remains $\Lambda$. Its row exit rates are also at most $\Lambda$. Therefore

$$
P_B=I+K_B/\Lambda
\tag{14}
$$

is an exact stochastic uniformization matrix.

The original driven hidden occupation law satisfies

$$
0\le p_{B,i}(t)/\mu_i\le R^2
\tag{15}
$$

for every protocol and time. Indeed, its hidden forward equation has internal dynamics preserving $\mu$, killing rate at least $1/R$, entry-source coordinate at most $R\mu_i$, and initial density $1/2$. The constant density $R^2$ is a supersolution; the finite-dimensional comparison principle gives (15).

Write $x_i=p_{B,i}/\mu_i$, $r(i,j)=(q(i,j)-B)_+$ and $\Delta K=K-K_B$. Symmetry of $r$ gives the exact forcing identity

$$
(p_B\Delta K)_j
=\mu_j\sum_i\mu_ir(i,j)(x_i-x_j).
$$

Consequently the full signed forcing, extended by zero at $A$, has total mass zero and obeys

$$
\|p_B\Delta K\|_1
\le\sum_{i,j}\mu_i\mu_jr(i,j)|x_i-x_j|
\le R^2\tau(B).
\tag{16}
$$

The clipped full propagator contracts zero-mass signed measures in $L^1$ by $e^{-(t-s)/R}$. To see this, split off the common external reset generator $(1/R)(\mathbf1e_A^T-I)$. On zero-mass rows its rank-one term vanishes, leaving exponential decay times a stochastic residual propagator.

Duhamel's formula, using the original occupation law in the forcing and the clipped propagator afterwards, now yields

$$
\|p_F(t)-p_{F_B}(t)\|_1
\le R^2\tau(B)\int_0^t e^{-(t-s)/R}\,ds
\le R^3\tau(B).
$$

The binary readout has absolute value one, so

$$
\boxed{
\sup_{h,t}|m_F[h](t)-m_{F_B}[h](t)|
\le R^3\tau(B)\le\delta/2.
}
\tag{17}
$$

Under (6), $(q-B)_+\le q^{1+\alpha}/B^\alpha$ proves the threshold choice (7). This argument requires only a global density moment: the occupation bound weights the removed rates by $\mu$, and no rowwise tail bound is assumed. It estimates actual driven means directly.

## 4. Sample a reversible graph and control its row errors

Assign a sampled vertex $i$ in actuator stratum $a$ weight and sensitivity

$$
\omega_i=\rho_a/n,\qquad\gamma_i=z_a.
$$

For distinct replicas define

$$
\widehat K_{ij}=\omega_jq_B(X_i,X_j),
$$

and choose the diagonal for zero row sums. Symmetry of $q_B$ makes this graph reversible under $\omega$. The convention $q_B(x,x)=0$ covers both self-samples and different replicas of the same microscopic state. Every actuator stratum has exactly its prescribed total mass for every sample realization.

The sampled graph may be disconnected, and its row exits may exceed $\Lambda$. These issues will be corrected after concentration. Define the algebraic matrix $\widehat P=I+\widehat K/\Lambda$; it is not yet asserted stochastic.

For a deterministic clipped-target function $u\in[0,1]$, use

$$
F_{x,u}(y)=\frac{q_B(x,y)}\Lambda[u(y)-u(x)],
$$

and also test the normalized exit function

$$
F_{x,\mathrm{exit}}(y)=q_B(x,y)/\Lambda.
$$

Both have absolute value at most $b$, vanish at $y=x$, and satisfy, by (12),

$$
\mathbb E_\mu F_{x,u}^2\le b,
\qquad
\mathbb E_\mu F_{x,\mathrm{exit}}^2\le b.
\tag{18}
$$

Here $q_B^2/\Lambda^2\le bq_B/\Lambda$, whose stationary row average is at most $b$.

Condition on a sampled row $X_i=x$ in stratum $a$. Its own summand is zero. All other samples remain independent. Removing that one conditional draw biases the weighted empirical sum by at most $b\omega_i\le b/n$. The sum of conditional variances is at most

$$
\frac1n\sum_a\rho_a^2\mathbb E_aF^2
\le\frac1n\mathbb E_\mu F^2\le\frac bn.
\tag{19}
$$

Each centered weighted summand has absolute value at most $2b/n$. Bernstein's inequality, using centered threshold $\eta/2$ and $n\ge2b/\eta$ for the bias, gives

$$
\Pr\left\{\left|\sum_j\omega_jF(X_j)-\mathbb E_\mu F\right|>\eta\right\}
\le2e^{-n\eta^2/(12b)}.
\tag{20}
$$

Before simplification, the exponent denominator is $8b+(8/3)b\eta\le12b$ for $\eta\le1/2$. The estimate is uniform in the conditioned value $x$, so it holds unconditionally.

For a finite deterministic function family $\mathcal U$, a union bound over rows, its consistency tests, and the exit test gives failure probability at most

$$
2mn(|\mathcal U|+1)e^{-n\eta^2/(12b)}.
\tag{21}
$$

On the good event,

$$
\max_i(-\widehat K_{ii})\le\Lambda(1+\eta),
\qquad
\max_i|(\widehat P u^X)_i-(P_Bu)(X_i)|\le\eta.
\tag{22}
$$

Separately, a deterministic $v\in[0,1]$ has unbiased stratified empirical average. Since $\sum_i\omega_i^2=(1/n)\sum_a\rho_a^2\le1/n$, weighted Hoeffding gives

$$
\Pr\left\{\left|\sum_i\omega_iv(X_i)-\mathbb E_\mu v\right|>\eta\right\}
\le2e^{-2n\eta^2}.
\tag{23}
$$

The factor $b$ in the sample budget is linear. Using only a bounded-range estimate in (20) would instead produce a quadratic factor and a worse moment exponent.

## 5. One common rescaling and a small reset preserve a fixed clock

On the exit-rate good event, put

$$
\widetilde K=\widehat K/(1+\eta),\qquad
\widetilde P=I+\widetilde K/\Lambda
=\frac{\widehat P+\eta I}{1+\eta}.
\tag{24}
$$

This is a stochastic reversible update matrix, with outgoing rate at most $\Lambda$. For each consistency test in (22), both $u(X_i)$ and $(P_Bu)(X_i)$ lie in $[0,1]$. The identity in (24) therefore gives

$$
\max_i|(\widetilde P u^X)_i-(P_Bu)(X_i)|\le2\eta.
$$

Let $\Pi_\omega$ have every row equal to $\omega$, and define

$$
P^*=(1-\eta)\widetilde P+\eta\Pi_\omega,
\qquad K^*=\Lambda(P^*-I).
\tag{25}
$$

Every entry of $P^*$ is positive, so $K^*$ is irreducible and ordinarily reversible. The reset changes a $[0,1]$-valued function by at most $\eta$, giving

$$
\boxed{
\max_i|(P^*u^X)_i-(P_Bu)(X_i)|\le3\eta.
}
\tag{26}
$$

Outgoing rates remain at most $\Lambda$, and the surrogate's relaxation rates are at most $2\Lambda$. The clock used in both models is exactly $\Lambda$, independent of $B$. Preservation of the original lower gap or upper spectral endpoint is not asserted.

## 6. A finite good event controls the prefix law

Define clipped-target prediction functions

$$
f_\varnothing=1,\qquad
f_w=P_BD_{a_1}\cdots P_BD_{a_r}1,
$$

where $D_a$ multiplies by the actuator-level indicator. Use the families

$$
\mathcal U=\{D_af_w:|w|\le\ell-1\},\qquad
\mathcal V=\{D_af_w:|w|\le\ell\}.
$$

Each has at most $V=\sum_{r=1}^{\ell+1}m^r$ members. All functions are deterministic functions of the supplied clipped target, not of the sampled graph.

Equations (21) and (23) bound the total failure probability by

$$
2mn(V+1)e^{-n\eta^2/(12b)}+2Ve^{-2n\eta^2}.
\tag{27}
$$

For the explicit parameters (10), $n\le1024b\eta^{-2}J$ and

$$
2mn(V+1)\le64\eta^{-1}Je^J\le e^{5J}.
$$

The last inequality uses $\eta^{-1}\le e^J$, $J\le e^J$, and $64\le e^{2J}$. Since $n\eta^2/(12b)>42J$, the first term in (27) is at most $e^{-37J}$. Also $2V\le e^J$ and $2n\eta^2\ge1024J$, so the second is at most $e^{-1023J}$. This proves (11).

For any good realization, stochastic contraction and (26) give inductively

$$
\max_i|f_w^*(i)-f_w(X_i)|\le3|w|\eta,
\qquad |w|\le\ell.
$$

A stationary word of length $\ell+1$ has at most $3\ell\eta$ prediction error and $\eta$ empirical-average error. Hence the stationary prefix total variation is at most

$$
\theta=\frac12m^{\ell+1}(3\ell+1)\eta.
\tag{28}
$$

The one-symbol marginal is exactly the target's, because the actuator masses are exact.

## 7. Regeneration, physical constraints, and the state count

The clipped target and sampled surrogate have common internal update rate $\Lambda$. Their external escape rates from $A$ coincide and are at most $R$; every hidden-to-$A$ rate is at least $1/R$. At entry into the hidden block, the prefix laws are tilted by $e^{hz_0}$ with identical normalization. This multiplies their total variation by at most $A_H$.

The [bounded-rate regenerative estimate](BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) consequently gives

$$
\sup_{h,t}|m_{F_B}[h](t)-m_{\widehat F}[h](t)|
\le C_R\left[A_H\theta+q_\Lambda^{\ell+1}\right],
\qquad q_\Lambda=\frac{\Lambda R}{1+\Lambda R}.
\tag{29}
$$

The two terms account for a prefix mismatch and exhaustion of its $\ell$ internal updates before a common external reset. Initial hidden visits have probability $1/2$, later entries have intensity at most $R$, and a rate-$1/R$ reset bounds the influence of either cause uniformly in the observation horizon. The internal reset in (25) is part of the surrogate and its cost is already in (26); the external reset used in this argument changes neither model.

The choices (9) give

$$
C_RA_H\theta=\delta/4,\qquad
C_Rq_\Lambda^{\ell+1}\le\delta/4.
$$

Thus (29) is at most $\delta/2$. Adding the clipping error (17) proves (4). Restoring $k$ multiplies all internal rates and clocks by $k$, leaving the state counts and dimensionless error estimates unchanged.

Attach sampled hidden states to $A$ with

$$
q_{Ai}(h)=k\omega_i e^{(1+\gamma_i)h},\qquad
q_{iA}(h)=ke^{(\gamma_i-1)h}.
$$

The stationary law is $\widehat\pi_h(A)=e^{-h}/(2\cosh h)$ and $\widehat\pi_h(i)=\omega_i e^h/(2\cosh h)$. Every internal and external edge satisfies ordinary detailed balance. Exact actuator masses imply the stated passive, static, and low-order agreements.

At fixed $m,\Lambda,G,H$, equations (9)--(10) give

$$
\ell=O(\log(2/\delta)),\quad
m^{\ell+1},V=O(\delta^{-p_\Lambda}),\quad
\eta^{-2}=O\!\left(\delta^{-2(1+p_\Lambda)}\log^2(2/\delta)\right),
$$

$$
J=O\!\left(\log(2/\delta)+\log(2b)\right).
$$

Substitution into $D=1+mn$ proves (5). Under (6)--(7), $b=O(\delta^{-1/\alpha})$ and $J=O(\log(2/\delta))$, proving (8).

## 8. A spectral cap alone cannot make density clipping uniformly accurate

Fix $s=\sqrt W>0$. For each integer $N_0\ge1$, take hidden states $(a,j)$, with $a\in\{-1,+1\}$, $j\in\{1,\ldots,N_0\}$, uniform law $\mu=1/(2N_0)$ and actuator $g(a,j)=as$. Let $T$ flip $a$ while retaining $j$, and let $\Pi$ be global stationary refresh. Define

$$
K_{N_0}=k(T-I)+k(\Pi-I).
\tag{30}
$$

The refresh makes every off-diagonal rate positive. The generator is reversible and its nonzero relaxation rates belong to $\{k,3k\}$. The actuator process has relaxation rate $3k$ and balanced binary values. Summing over $j$ lumps the complete controlled physical model exactly to the original three-state model with hidden flip rate $3k/2$. This family has no growing intrinsic controlled state requirement.

Its conductance density is $1+2N_0$ on a matching edge and $1$ on every other off-diagonal edge. For any clipping threshold $B\ge1$, symmetric clipping gives exactly

$$
K_{N_0,B}=k(\Pi-I)
+k\min\left\{1,\frac{B-1}{2N_0}\right\}(T-I).
\tag{31}
$$

It retains reversibility, positivity, and the band $[k,3k]$, but its actuator relaxation rate becomes

$$
\lambda_{N_0,B}=k\left[1+\min\left\{2,\frac{B-1}{N_0}\right\}\right]
\longrightarrow k
\quad(N_0\to\infty)
\tag{32}
$$

at any fixed $B$. For $B\le1+2N_0$ the removed stationary flux is

$$
\tau_{N_0}(B)=1-\frac{B-1}{2N_0}\longrightarrow1.
\tag{33}
$$

For every $\alpha>0$, its global density moment is

$$
\sum_{x,y}\mu_x\mu_yq(x,y)^{1+\alpha}
=1-\frac1{N_0}+\frac{(1+2N_0)^{1+\alpha}}{2N_0},
\tag{34}
$$

which diverges. Therefore the spectral cap supplies neither a uniform density-moment bound nor a uniformly small clipping tail.

The clipping error is also nonvanishing in the actual finite-field mean. The original three-state pair with hidden relaxation rates $k$ and $3k$ has cubic step-mean difference at time $1/k$ equal to $ch^3$, where

$$
c=\frac W2(e^{-2}-e^{-4})>0.
$$

The [uniform finite-field remainder lemma](FINITE_FIELD.md#6-a-taylor-remainder-uniform-in-size-and-horizon), with sensitivity bound $s$, bounds each fourth-and-higher-order remainder by $R_Hh^4$, where

$$
R_H=\frac{365}{12}e^{2(1+s)H}(1+s)^4.
$$

Choose one fixed amplitude

$$
0<h_0\le\min\{H,c/(4R_H)\}.
$$

Their actual step means then differ by at least $ch_0^3/2$. To compare the clipped model with the rate-$k$ model, changing a three-state hidden relaxation rate from $k$ to $\lambda$ changes the generator's maximum row-$L^1$ norm by $|\lambda-k|$. Stochastic semigroup contraction and Duhamel consequently give

$$
|m_\lambda(h_0;1/k)-m_k(h_0;1/k)|\le|\lambda-k|/k.
$$

Choose an integer

$$
N_0\ge\max\left\{1,\frac{B-1}{2},
\frac{4(B-1)}{ch_0^3}\right\}.
$$

Equations (32) and the last bound show that the original and clipped models satisfy

$$
\boxed{
|m_{K_{N_0}}(h_0;1/k)-m_{K_{N_0,B}}(h_0;1/k)|
\ge ch_0^3/4>0.
}
\tag{35}
$$

The field and positive lower bound are independent of $B,N_0$. This is a certified actual finite-field discrepancy, not an inference from a nonzero Taylor coefficient alone. No cutoff chosen only from a tolerance and the fixed spectral band can therefore make this clipping operation uniformly accurate.

The example does not obstruct a redesigned reversible surrogate: its exact three-state replacement was already identified. A cap-only construction would need to retain or reorganize the observable effect of the heavy edges, rather than discard them.

## 9. What is settled and what remains open

A global density moment provides a dimension-free polynomial reversible upper bound, with exact actuator histogram and all-protocol/all-horizon actual-mean control. The weaker tail-dependent statement gives a target-specific certificate even without a common moment bound. When a smaller fixed spectral cap is known, this argument also improves the bounded-pointwise-density sampler: that density bound enters the sampling prefactor, while the clock exponent uses $\Lambda$.

The binary question in the original tight band $[k,3k]$ remains open. The [binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) rules out general polynomial reversible sufficiency at exit budget $6580k$, with the prescribed rule and exact balanced histogram. The [nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) gives the separation at budget $3k$. The clipping obstruction here establishes a failure of one approximation step; it is not the proof of that reversibility penalty. No optimal polynomial exponent, original spectral-band preservation, stable noisy learning procedure, or physical implementation is claimed. All constructions assume the kinetic target is supplied.
