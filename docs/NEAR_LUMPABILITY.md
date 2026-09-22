# Passive information near exact lumpability

[Repository overview](../README.md) · [Model and response](THEORY.md) · [Finite-field control](FINITE_FIELD.md)

**Working theorem, 22 September 2026.** Exact passive compression is a useful mathematical boundary, but a physical model will generally have unequal microscopic exit rates. This note quantifies one natural departure from that boundary: small, arbitrary changes in the equilibrium conductances of the edges between the visible blocks. The passive visible path then carries information about the hidden kinetics, but that information can appear only at fourth order in the size of the conductance disorder. A driven response can remain separated at a fixed, nonzero field. These are analytic statements for the specified model; practical sample counts and a universal robustness claim for all microscopic perturbations are not asserted.

## 1. Perturbing barriers while keeping equilibrium fixed

Retain the states, stationary weights, internal generator, readout, and actuator of [the main model](THEORY.md). In addition to the centered actuator profile $g$, choose any real barrier profile $b$ satisfying

$$
\langle b,1\rangle_\mu=0,\qquad B=\|b\|_\infty>0.
$$

For $a_j=1+\delta b_j$ and $q=|\delta|B<1$, replace the external rates by

$$
q_{AB_j}(h)=k\mu_j a_j e^{(1+g_j)h},\qquad
q_{B_jA}(h)=k a_j e^{(g_j-1)h}.
$$

The internal rates remain $K$. Both directions of each external edge acquire the same factor, so detailed balance and the equilibrium law remain exactly

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(B_j)=\frac{\mu_j e^h}{2\cosh h}.
$$

This represents a change in barriers with the state energies held fixed. The profile $b$ need not equal $g$. Centering absorbs a common clock change: any positive factors $\widetilde a_j$ can be written as a common factor $\langle\widetilde a,1\rangle_\mu$ times factors of mean one, with the common factor absorbed into $k$.

At zero field the exit rate from $A$ remains $k$, whereas the exit rate from $B_j$ is $ka_j$. Unless $b$ is constant, strong lumpability is broken for every nonzero $\delta$. All observations below start in the unchanged equilibrium $\pi_0$.

## 2. The complete passive observation is a renewal process

Let $M_\delta=K-k\operatorname{diag}(a)$ be the generator of the hidden motion within $B$, killed when it jumps to $A$. A visit to $A$ lasts an independent exponential time of rate $k$. The next hidden state has distribution $\mu_j a_j$, independently of that duration and of previous visits. Consequently, successive complete $B$ sojourns are independent with density

$$
f_{\delta,K}(t)=k\langle a,e^{M_\delta t}a\rangle_\mu.
\tag{1}
$$

The initial $B$ sojourn, conditional on observing $S(0)=+1$, is a stationary residual sojourn and has density

$$
f^{\mathrm{res}}_{\delta,K}(t)
=k\langle 1,e^{M_\delta t}a\rangle_\mu.
\tag{2}
$$

At $\delta=0$, both densities are $f_0(t)=ke^{-kt}$. The mean complete $B$ sojourn is exactly $1/k$ at every admissible $\delta$. For example, with $L=-M_\delta$, the identity $\mu L=k\mu\operatorname{diag}(a)$ gives

$$
\langle a,L^{-1}1\rangle_\mu=\frac1k.
$$

Thus a complete $A$--$B$ cycle has mean duration $2/k$. The stationary rate of $A\to B$ entries is also exactly $k/2$.

Equations (1)--(2), including the final censored sojourn, describe the entire observed zero-field path law. No hidden trajectory is available to the observer.

## 3. A bound independent of state count and internal rates

Write $P^T_{\delta,K}$ for the law of the stationary visible path on $[0,T]$, and $P^T_0$ for the stationary rate-$k$ two-state telegraph law. If $q\le1/4$, then

$$
\boxed{D_{\mathrm{KL}}(P^T_{\delta,K}\|P^T_0)
\le q^4(152+241kT).}
\tag{3}
$$

The bound has no dependence on the number of hidden states, the smallest stationary weight, or the internal rates. Its constants are conservative.

### Density estimate

Put $x=kt$. Since $K$ is stationary under $\mu$, its Markov semigroup is a contraction on $L^2(\mu)$ and fixes the constant vector. Expand

$$
e^{(K-k\delta\operatorname{diag}(b))t}
$$

in its convergent Dyson series. In the complete-sojourn expression there are zero, one, or two factors of $\delta b$ from the endpoints. The first-order contribution vanishes because $\langle b,1\rangle_\mu=0$. Bounding each multiplication by $b$ by $B$ gives

$$
\left|\frac{f_{\delta,K}(t)}{ke^{-kt}}-1\right|
\le q^2e^{qx}\left(1+2x+\frac{x^2}{2}\right).
\tag{4}
$$

Indeed, the terms with no endpoint factor begin at two generator insertions and are bounded by $q^2x^2e^{qx}/2$; the two possible single-endpoint terms begin at one insertion and contribute at most $2q^2xe^{qx}$; the double-endpoint terms contribute at most $q^2e^{qx}$. The residual expression has only one endpoint factor, and therefore

$$
\left|\frac{f^{\mathrm{res}}_{\delta,K}(t)}{ke^{-kt}}-1\right|
\le q^2e^{qx}\left(x+\frac{x^2}{2}\right).
\tag{5}
$$

Since $1-2q\ge1/2$, integration of the squared relative errors yields

$$
\begin{aligned}
\chi^2(f_{\delta,K}\|f_0)
&\le q^4\int_0^\infty e^{-x/2}
 \left(1+2x+\frac{x^2}{2}\right)^2dx=482q^4,\\
\chi^2(f^{\mathrm{res}}_{\delta,K}\|f_0)
&\le q^4\int_0^\infty e^{-x/2}
 \left(x+\frac{x^2}{2}\right)^2dx=304q^4.
\end{aligned}
\tag{6}
$$

Relative entropy is bounded by the corresponding chi-squared divergence.

### Finite horizon and censoring

Augment the observed path by revealing the *complete* duration of its last, censored sojourn. This adds information and can only increase relative entropy. Generate this augmented record from its initial sign and successive full holding times, stopping immediately after generating the holding time that crosses $T$.

The decision to generate each next holding time depends only on previously generated times. Conditional on beginning a complete $B$ visit, its density is always (1). Thus the chain rule for relative entropy charges the complete-$B$ divergence once for each $A\to B$ entry before $T$. Its expected count under the perturbed stationary process is $kT/2$. An initial $B$ visit occurs with probability $1/2$ and contributes the residual divergence. The initial sign has the same distribution under both models, and every $A$ holding time has the same exponential law. Consequently,

$$
D_{\mathrm{KL}}(P^T_{\delta,K}\|P^T_0)
\le\frac12D_{\mathrm{KL}}(f^{\mathrm{res}}_{\delta,K}\|f_0)
+\frac{kT}{2}D_{\mathrm{KL}}(f_{\delta,K}\|f_0),
$$

which proves (3). The same argument can first be applied with a finite cap on the number of visits, then passed to the limit. Bounded visible jump hazards and (6) give the required integrability. Revealing the final duration is only a proof device; (3) bounds the original censored observation.

For two models with common $k,\mu,b$, Pinsker's inequality and the triangle inequality give

$$
\|P^T_{\delta,K_1}-P^T_{\delta,K_2}\|_{\mathrm{TV}}
\le\min\left\{1,q^2\sqrt{2(152+241kT)}\right\}.
\tag{7}
$$

For $n$ independent stationary records with total duration $T_{\mathrm{tot}}$, replace $152+241kT$ by $152n+241kT_{\mathrm{tot}}$. Every test based on these records has equal-prior error at least $(1-\mathrm{TV})/2$. For a fixed number of long records, constant-confidence discrimination therefore needs observation time of order at least $q^{-4}/k$ as $q\to0$. This is a bound for complete visible paths, not only for means or autocorrelations.

## 4. The hidden kernel leaks into waiting times at second order

Define the barrier correlation kernel

$$
C_b(t)=\langle b,e^{Kt}b\rangle_\mu.
$$

Keeping the second-order terms in the same expansion gives

$$
f_{\delta,K}(t)=ke^{-kt}\left[1+\delta^2R_{C_b}(t)+O(\delta^3)\right],
\tag{8}
$$

where

$$
R_C(t)=C(t)-2k\int_0^tC(s)\,ds
+k^2\int_0^t(t-s)C(s)\,ds.
\tag{9}
$$

The corresponding residual coefficient is

$$
R_C^{\mathrm{res}}(t)=-k\int_0^tC(s)\,ds
+k^2\int_0^t(t-s)C(s)\,ds.
$$

The remainder in (8) is understood pointwise first; the Dyson bounds with an exponential envelope also justify the weighted integrations and entropy expansions below for sufficiently small $|\delta|$. In particular, the killing hazard lies between $k(1-q)$ and $k(1+q)$, so the densities have a positive lower exponential envelope. Combining that envelope with the Dyson remainder bounds gives an integrable envelope for the required relative-error Taylor remainders.

The map $C\mapsto R_C$ is injective. To see this, set $H_C(t)=\int_0^t(t-s)C(s)ds$. Then $R_C=(\partial_t-k)^2H_C$, with $H_C(0)=H'_C(0)=0$. A zero difference of $R_C$ therefore forces a zero difference of $H_C$ and hence of $C$.

For two fixed models, the stationary visible relative-entropy rate is

$$
\begin{aligned}
\mathcal I_\delta(K_1\|K_2)
&:=\lim_{T\to\infty}\frac1T
D_{\mathrm{KL}}(P^T_{\delta,K_1}\|P^T_{\delta,K_2})\\
&=\frac{k}{2}D_{\mathrm{KL}}(f_{\delta,K_1}\|f_{\delta,K_2})\\
&=\frac{k\delta^4}{4}\int_0^\infty ke^{-kt}
 [R_{C_{b,1}}(t)-R_{C_{b,2}}(t)]^2dt+O(\delta^5).
\end{aligned}
\tag{10}
$$

The middle equality follows from the renewal reward theorem applied to complete $A$--$B$ cycles. The initial residual and final censored interval contribute only a bounded boundary term: the holding-time hazards are bounded above and below, log density and survival ratios grow at most linearly in duration, and the stationary age and residual time have bounded moments. The factor $k/2$ is the reciprocal mean cycle duration.

For the final equality, write each density as $f_0(1+\delta^2R_i+O(\delta^3))$, expand the relative entropy, and use normalization to cancel the linear relative-error contribution. This leaves half the squared second-order difference. The exponential bounds used above justify the integrated remainder. If $C_{b,1}\ne C_{b,2}$, the displayed coefficient is strictly positive. Thus the quartic information scale in (3) is attained in this model class. It is not a state-count lower bound and is not uniform below over all distinct pairs of kernels.

When $b=g$, the kernel appearing in (9) is precisely the kernel governing the cubic intervention mean in the unperturbed model. The same hidden spectrum is completely invisible at exact passive lumpability and enters passive dwell statistics quadratically as the barriers become unequal.

## 5. An explicit pair and a finite driven signal

Take $\mu=(1/2,1/2)$, $b=g=(\sqrt W,-\sqrt W)$, and internal generators with relaxation rates $\lambda=k$ and $\lambda=3k$. Then $q=|\delta|\sqrt W$. With $x=kt$,

$$
\frac{R_{C_k}(t)-R_{C_{3k}}(t)}{W}
=4e^{-x}-\frac{16}{9}e^{-3x}+\frac23x-\frac{20}{9}.
$$

The elementary integral of its square is

$$
\int_0^\infty e^{-x}
\left(4e^{-x}-\frac{16}{9}e^{-3x}+\frac23x-\frac{20}{9}\right)^2dx
=\frac8{105}.
$$

Swapping the two hidden states changes $\delta$ to $-\delta$ without changing the passive visible law, so this law is even in $\delta$. Equation (10) becomes

$$
\boxed{\mathcal I_\delta(K_k\|K_{3k})
=\frac{2k}{105}q^4+O(q^6).}
\tag{11}
$$

For direct verification, the exact complete-$B$ density for either relaxation rate is

$$
\begin{aligned}
f_{q,\lambda}(t)=k e^{-(k+\lambda/2)t}\Bigg[
&(1+q^2)\cosh(\omega t)\\
&+\frac{(\lambda/2)(1-q^2)-2kq^2}{\omega}\sinh(\omega t)\Bigg],\\
\omega&=\sqrt{(\lambda/2)^2+(kq)^2}.
\end{aligned}
$$

The observation-time scaling also has a direct test using independent records of fixed duration $1/k$. Let $Z$ indicate that the initial visible state is $B$ and that no visible jump occurs during the record. Its probability is

$$
\mathbb P_{q,\lambda}(Z=1)
=\frac12\langle1,e^{M_\delta/k}1\rangle_\mu.
$$

The same Dyson expansion, now with no perturbed endpoint factor, gives

$$
\mathbb P_{q,k}(Z=1)-\mathbb P_{q,3k}(Z=1)
=\frac{e^{-1}(9e^{-1}-2-e^{-3})}{18}q^2+O(q^4).
$$

The coefficient is strictly positive, while both probabilities tend to $e^{-1}/2$. A threshold test on the empirical mean of $Z$ therefore achieves any fixed nonzero confidence advantage using $O(q^{-4})$ independent records; the variance bound for a Bernoulli mean already proves this upper bound. Equation (7) gives the matching $\Omega(q^{-4})$ lower bound even when every complete visible path is retained. Hence the fixed-duration, binary testing problem has sample complexity $\Theta(q^{-4})$. The hypotheses and disorder amplitude are specified, and each trial uses the same zero-field stationary preparation. Total observed duration is $n/k$; the cost of restoring that preparation is not included. This is not a guarantee for estimation of an arbitrary unknown generator.

The quartic passive information does not force the driven signal to vanish with $q$. At $q=0$ the cubic coefficients at time $T=1/k$ differ by

$$
c_W=\frac W2(e^{-2}-e^{-4})>0
$$

for a unit step, with the $\lambda=3k$ mean larger. The [finite-field remainder theorem](FINITE_FIELD.md) gives an explicit per-model fourth-order bound with

$$
R_H=\frac{365}{12}e^{2(1+G)H}(1+G)^4,\qquad G=\sqrt W.
$$

Consequently, for

$$
0<h\le\min\{H,c_W/(4R_H)\},
$$

the exact, unperturbed mean difference under the constant field $h$ is at least $c_Wh^3/2$ at $T=1/k$. This statement concerns finite-field means, not just their cubic derivatives.

At the same field, multiplying the basal conductances by $a$ changes the generator by at most

$$
\|Q_\delta(h)^T-Q_0(h)^T\|_1
\le2kq e^{(1+G)|h|}.
$$

Both real-field semigroups are stochastic contractions. Duhamel's formula therefore bounds the change of each mean at time $T$ by $2kTq e^{(1+G)|h|}$, and the change of the pair's mean difference by twice that amount. In particular, choosing

$$
0<q\le\min\left\{\frac14,
\frac{c_Wh^3e^{-(1+G)h}}{16}\right\}
\tag{12}
$$

ensures the perturbed models retain an exact finite-field mean separation of at least $c_Wh^3/4$ at time $1/k$, while their passive information obeys (3) and (11). The inequalities are sufficient existence bounds, not optimized experimental operating ranges.

## 6. What the robustness result does and does not say

The result gives a neighborhood of barrier inhomogeneities, with the energies and actuator specified, in which full passive observation has uniformly small information about arbitrarily complex internal kinetics. It also identifies the first informative passive statistic and the observation-time scale at which exact lumpability becomes distinguishable. The [path-response analysis](ACTIVE_PATH_RESPONSE.md) shows that the cubic endpoint mean is not the earliest informative active statistic: retaining the initial visible value as well exposes a quadratic response. Its exact constant-field identity $m_h(t)=\tanh h\,[1-\mathbb E_h(S_0S_t)]$ remains valid for the perturbed model, because detailed balance and the conditional equilibrium distributions within the two visible blocks remain unchanged. Thus the finite driven mean gap above also implies a separation of the corresponding two-snapshot correlations. No joint sampling-rate theorem in both $q$ and $h$ is inferred from that identity alone.

The perturbation model preserves equilibrium weights and changes only the external conductances. Arbitrary changes to energies, preparation, readout, or actuator are different perturbations and are not covered by (3). For nonzero disorder the passive models are generally distinguishable given long enough data; no all-horizon passive equality is claimed. The fourth-order suppression depends on the common equilibrium structure and comparison after the common clock shift is removed. No fourth-order law is asserted for every possible departure from lumpability.
