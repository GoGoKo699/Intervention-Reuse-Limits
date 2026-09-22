# Hidden kinetics appear at second order in visible paths

[Repository overview](../README.md) · [Model and cubic mean response](THEORY.md) · [Publication scope](PUBLICATION_SCOPE.md)

**Research extension, 22 September 2026.** This note gives analytic results for the same model and the same zero-field stationary preparation as the cubic-mean theorem. It changes the measured observable: a resolved visible trajectory contains information that its final-time mean discards. The likelihood expansion below is on each fixed finite horizon; it is not a uniform-in-horizon finite-field approximation. These are internal derivations, not an originality certification.

## 1. What the extension establishes

For the model in [THEORY.md](THEORY.md), let $P_{\epsilon}^{C,u}$ be the law of the visible trajectory $S$ on $[0,T]$ under $h(t)=\epsilon u(t)$, starting from $\pi_0$. Let $P_{\epsilon}^{\mathrm{ref},u}$ be the visible law of the ordinary two-state model with rates $ke^{h(t)}$ and $ke^{-h(t)}$, with the same initial visible distribution. Here $u$ is bounded and piecewise continuous, and $T<\infty$ is fixed.

The results are:

1. Every bounded visible-path observable has the same response through first order in $\epsilon$ as the two-state reference.
2. The entire second-order visible-path response is determined by the scalar kernel $C(t)=\langle g,e^{Kt}g\rangle_\mu$. Conversely, one second-order no-exit curve determines $C$.
3. If $C$ has $r$ distinct positive-weight exponential modes, reproducing this second-order path response with an analytic binary-readout Markov model requires at least $r+2$ states. The reversible construction already in the repository attains this count. There is no exceptional mode at $\lambda=k$.
4. For an explicit fixed pair of three-state models, independent trials recording the initial and final visible states distinguish the models with $\Theta(\epsilon^{-4})$ samples as $\epsilon\to0$. Recording only the final visible state requires $\Theta(\epsilon^{-6})$ samples in the same fixed step experiment. Resolving the entire path cannot improve the sample exponent for this fixed task.

Thus the cubic mean is not the earliest visible intervention diagnostic. The operational hierarchy is passive law, first-order path response, second-order path response, and then the cubic single-time mean.

## 2. Exact conditional likelihood and its expansion

Fix a visible path with finitely many jumps. Decompose its time in $B$ into maximal intervals $I$. An interval touching $0$ or $T$ has an artificial endpoint there; such an endpoint is not a visible jump. Write $\mathcal J_I$ for the actual visible jumps at the endpoints of $I$. Define the signed measure

$$
a_I(dt)=\sum_{\tau\in\mathcal J_I}u(\tau)\,\delta_\tau(dt)
-k u(t)\mathbf 1_I(t)\,dt.
$$

Both an entry into $B$ and an exit from $B$ carry a positive atomic coefficient $u(\tau)$ in this definition. Values of $u$ at its deterministic discontinuities do not affect the result, since a jump occurs at any specified time with probability zero.

To obtain an exact likelihood representation, lift the two-state reference to the microscopic states using the same $K$ and $\mu$, but set $g=0$ in the field coupling. Under this lifted reference, conditional on the visible path, the hidden process on each $B$ interval is an independent stationary $K$ process. This remains true under the applied field: entries have distribution $\mu$, exits have a state-independent rate, and the field does not change $K$. An interval beginning at time zero starts from $\mu$ because the preparation is $\pi_0$.

Let $X_t$ denote this conditional hidden process during $B$ intervals, and let $G(h)=\langle e^{hg}\rangle_\mu$. The continuous-time Markov path likelihood formula gives

$$
\frac{dP_{\epsilon}^{C,u}}{dP_{\epsilon}^{\mathrm{ref},u}}(S)
=\mathbb E\!\left[\exp L_\epsilon(X,S)\mid S\right],
$$

where

$$
\begin{aligned}
L_\epsilon={}&
\epsilon\sum_{I}\sum_{\tau\in\mathcal J_I}u(\tau)g(X_\tau)\\
&-k\int_{S_t=-1}e^{\epsilon u(t)}[G(\epsilon u(t))-1]dt\\
&-k\int_{S_t=+1}e^{-\epsilon u(t)}
[e^{\epsilon u(t)g(X_t)}-1]dt.
\end{aligned}
$$

At a visible entry or exit, $X_\tau$ means the hidden state on the $B$ side. There are no likelihood factors from internal transitions because their rates are unchanged. The second line accounts for the total escape rate from $A$; the third accounts for escape from each $B_j$.

Write $L_\epsilon=\epsilon L_1+\epsilon^2L_2+O(\epsilon^3)$. Centering and stationarity imply

$$
L_1=\sum_I\int_I g(X_t)\,a_I(dt),\qquad
\mathbb E[L_1\mid S]=0,
$$

and

$$
\mathbb E[L_2\mid S]=-\frac{kW}{2}\int_0^T u(t)^2dt.
$$

Within one interval,

$$
\mathbb E[g(X_s)g(X_t)\mid S]=C(|t-s|).
$$

Different intervals have independent, centered hidden processes. Expanding the conditional exponential therefore proves

$$
\boxed{
\frac{dP_{\epsilon}^{C,u}}{dP_{\epsilon}^{\mathrm{ref},u}}(S)
=1+\epsilon^2 A_C(S,u)+O(\epsilon^3),
}
$$

with

$$
\boxed{
A_C(S,u)=\frac12\sum_I\int_I\!\int_I
C(|t-s|)\,a_I(dt)a_I(ds)
-\frac{kW}{2}\int_0^T u(t)^2dt.
}
$$

This is a relative density expansion, not an assertion that the field-on trajectory is Markov. For fixed $T$, bounded $u$ and bounded $g$, the expansion holds in $L^p(P_0)$ for every finite $p$. One direct domination argument is as follows. Conditional on a visible path with $N$ jumps, the absolute values of $L_\epsilon$ and its derivatives in a sufficiently small fixed field neighborhood are bounded by constants times $N+T$. Derivatives of its exponential are bounded by a polynomial in $N+T$ times $e^{c|\epsilon|(N+T)}$. Under $P_0$, $N$ is Poisson with mean $kT$, so these bounds are integrable to every finite power. The visible reference density relative to $P_0$ has the same type of bound. Taylor expansion and conditional expectation can consequently be interchanged. Constants can depend on $T$, $\|u\|_\infty$, $k$ and the sensitivity bound; this argument supplies no uniform bound as $T\to\infty$.

For any bounded path functional $F$, the second-order coefficient of its expectation relative to the reference is therefore

$$
[\epsilon^2]\left(\mathbb E_{P_\epsilon^{C,u}}F-
\mathbb E_{P_\epsilon^{\mathrm{ref},u}}F\right)
=\mathbb E_{P_0}[F A_C].
$$

In particular, $\mathbb E_{P_0}A_C=0$. This normalization also has a direct check. For ordered times $s<t$ in the same $B$ interval, the four expected off-diagonal signed-measure densities (entry/exit, entry/occupation, occupation/exit and occupation/occupation) are respectively $+k^2/2,-k^2/2,-k^2/2,+k^2/2$, each multiplied by $e^{-k(t-s)}u(s)u(t)$. They cancel before multiplication by $C(t-s)$. The atomic diagonal has expectation $kW\int u^2$, since the passive visible jump intensity is $k$; the factor $1/2$ cancels the deterministic compensator.

The first-order coefficient vanishes for every such $F$. For example, the common first-order likelihood score relative to $P_0$ is

$$
\sum_{\tau\in\mathcal J}[-S_{\tau-}]u(\tau)
+k\int_0^T u(t)S_tdt.
$$

The complete second-order response depends only on $C$, since $W=C(0)$.

## 3. A no-exit measurement recovers the kernel

Apply a constant field $h$ at time zero. Condition only on the observed event $S_0=+1$ and let $\tau_B$ be the first visible exit time from $B$. This conditioning does not change the microscopic preparation beyond restricting $\pi_0$ to $B$: the conditional hidden law is exactly $\mu$.

The survival function is

$$
R_h(t)=\Pr_h(\tau_B>t\mid S_0=+1)
=\mu^T\exp\!\left[\left(K-k e^{-h}\operatorname{diag}(e^{hg})\right)t\right]\mathbf1.
$$

Here $\mu^T$ is a row vector. The subtracted diagonal is the killing rate into $A$. Expanding $R_h=R_0+hR_1+h^2R_2+O(h^3)$ gives

$$
R_0(t)=e^{-kt},\qquad R_1(t)=kt e^{-kt},
$$

and

$$
\boxed{
R_2(t)=e^{-kt}\left[
\frac{k^2t^2-k(1+W)t}{2}
+k^2\int_0^t(t-s)C(s)ds
\right].
}
$$

For completeness, the killed generator has Taylor coefficients

$$
L_0=K-kI,\qquad L_1=k(I-\operatorname{diag}g),\qquad
L_2=-\frac{k}{2}\operatorname{diag}(1-2g+g^2).
$$

The single $L_2$ insertion in the matrix exponential contributes $-k(1+W)t/2$ after factoring out $e^{-kt}$. The two $L_1$ insertions contribute

$$
k^2\int_0^t(t-s)[1+C(s)]ds,
$$

because $\mu$ is stationary, $\langle g\rangle_\mu=0$, and the two centered factors have correlation $C(s)$. These are exactly the displayed terms.

It follows that

$$
\boxed{
C(t)=\frac1{k^2}\frac{d^2}{dt^2}
\left[e^{kt}R_2(t)-\frac{k^2t^2-k(1+W)t}{2}\right].
}
$$

The mass $W$ can itself be recovered from $R_2'(0)=-k(1+W)/2$. Thus no separate knowledge of $W$ is needed for noiseless recovery. As with the cubic-mean inverse, differentiation is not a stable statistical estimator without further assumptions.

Consequently two family members have identical second-order visible-path responses for every bounded protocol and finite horizon if and only if their kernels agree. Sufficiency follows from the quadratic likelihood formula; necessity follows from this single constant-field survival curve.

This is an initial-residual survival experiment. A dwell interval beginning at a later field-on $A\to B$ jump instead starts from the field-biased entrance distribution $\mu_j e^{hg_j}/G(h)$; substituting that distribution gives a different second-order formula. The two experiments must not be conflated.

### Two snapshots also expose the quadratic response

There is an especially simple constant-field observable. Define

$$
H_h(t)=\mathbb E_h[S_0S_t],
$$

with the same $\pi_0$ preparation. For every field and time, detailed balance gives the exact identity

$$
\boxed{m_h(t)=\tanh h\,[1-H_h(t)].}
$$

To prove it, let $a_h(t)$ be the probability to be in $B$ at time $t$ starting from $A$, and let $b_h(t)$ be the probability to be in $A$ starting from the conditional law $\mu$ in $B$. Reversibility of the time-$t$ transition matrix under $\pi_h$ gives $a_h=e^{2h}b_h$. The conditional distributions within either visible block agree for $\pi_0$ and $\pi_h$. Consequently $m_h=a_h-b_h$, whereas $H_h=1-a_h-b_h$, proving the identity. This argument uses constant field and the specified stationary conditional preparations; it is not an identity for an arbitrary time-dependent protocol.

Expanding $H_h=H_0+hH_1+h^2H_2+\cdots$ gives

$$
H_0=e^{-2kt},\qquad H_1=0,\qquad
H_2=-m_3-\frac{m_1}{3}.
$$

Equivalently,

$$
H_2(t)=e^{-2kt}\left[-k(1+W)t+
2k^2\int_0^t(t-s)e^{ks}C(s)ds\right].
$$

Thus two visible snapshots already reveal the hidden kernel at second order. The identity also explains why a cubic mean can coexist with a quadratic path diagnostic: the mean carries an additional factor $\tanh h$. The survival formula above remains useful for its direct killed-generator pole argument, which has no resonance exception.

## 4. Exact state count from killed-generator poles

Suppose

$$
C(t)=\sum_{j=1}^r c_j e^{-\lambda_jt},\qquad
c_j>0,\quad \lambda_j>0,
$$

with distinct rates. The formula above becomes

$$
R_2(t)=e^{-kt}\left[
\frac{k^2t^2-k(1+W)t}{2}
+k^2\sum_{j=1}^r c_j\left(
\frac{t}{\lambda_j}-\frac{1-e^{-\lambda_jt}}{\lambda_j^2}
\right)\right].
$$

Each $e^{-(k+\lambda_j)t}$ has nonzero coefficient $k^2c_j/\lambda_j^2$. In addition, the coefficient of $t^2e^{-kt}$ is $k^2/2>0$. The Laplace transform therefore has exactly $r+1$ distinct pole locations:

$$
-k,\quad -(k+\lambda_1),\ldots,-(k+\lambda_r).
$$

Now consider any finite-state Markov surrogate with a fixed binary readout, a fixed initial distribution with positive probability on each visible value, and a generator analytic in $h$ near zero. Its preparation may in particular be its stationary zero-field law, as in the original comparison class. Let $n_B$ be the number of states assigned visible value $+1$. Conditional on starting in that block, the surrogate survival curve is

$$
\widehat R_h(t)=\widehat\eta^T
\exp[\widehat Q_{BB}(h)t]\mathbf1,
$$

where $\widehat Q_{BB}$ is the principal submatrix of the full generator: its diagonals retain rates of exits into the other block. Hidden motion in the negative-readout block cannot affect this no-exit event.

For $\widehat Q_{BB}(h)=L+hL^{(1)}+h^2L^{(2)}+\cdots$, write $\mathcal R(z)=(zI-L)^{-1}$. The Laplace transform of the second Taylor coefficient is

$$
\widehat\eta^T\left[
\mathcal R L^{(2)}\mathcal R+
\mathcal R L^{(1)}\mathcal R L^{(1)}\mathcal R
\right]\mathbf1.
$$

All its pole locations belong to the spectrum of the $n_B\times n_B$ matrix $L$. Repeated eigenvalues and Jordan blocks can raise pole orders but cannot create new pole locations. Hence matching $R_2$ forces $n_B\ge r+1$. At least one negative-readout state is also necessary, and therefore

$$
\boxed{D\ge r+2.}
$$

Matching the passive path law and the second-order joint path response supplies matching conditional survival coefficients because the common initial $B$ probability is $1/2$ and is field-independent. The argument needs neither reversibility nor the other mean-response constraints of the original surrogate class. There is no pole collision when $\lambda_j=k$.

Conversely, the [Jacobi realization](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel) represents this same $C$ using $r+1$ hidden states with $|g_i|=\sqrt W$. Adding $A$ gives $r+2$ total states. The likelihood formula then supplies the same entire second-order path response, and the existing response equations supply the same cubic mean. Thus $r+2$ is the exact minimal count for the second-order path task, within analytic binary-readout Markov surrogates.

This count is not an approximate lower bound, a bit-memory bound, or a bound on non-Markov surrogates.

## 5. A fixed statistical task: paths versus endpoints

Take two three-state targets with common $k>0$, $\mu=(1/2,1/2)$ and $g=(\sqrt W,-\sqrt W)$, where $W>0$ is fixed. The internal flip rate is $\lambda/2$, with hypotheses

$$
H_1:\lambda=k,\qquad H_3:\lambda=3k.
$$

Every independent trial starts from that model's zero-field stationary law, applies the same constant field $h=\epsilon$, and runs for $T=1/k$. Compare three measurement records:

- **Path record:** the resolved binary trajectory throughout $[0,T]$.
- **Two-snapshot record:** $(S_0,S_T)$.
- **Endpoint record:** only $S_T$.

The test is between these two specified hypotheses; parameters and the applied protocol are known. Sample complexity below is the number of independent trials needed for the sum of the two testing error probabilities to be at most a fixed number in $(0,1)$ as $\epsilon\to0$. Constants may depend on $W$ and the chosen error threshold. This is not an optimization over adaptive protocols, observation noise, observation bandwidth or unknown parameter classes. The total observed duration is $n/k$; time or physical cost for restoring the stationary preparation between trials is not counted.

### A binary statistic from two snapshots

Set $J=\mathbf1\{S_0=S_T\}$. Its probability is $(1+H_h(T))/2$. The cubic mean formulas and the exact identity above give

$$
\Pr_{H_3}(J=1)-\Pr_{H_1}(J=1)
=-\frac b2\epsilon^2+O(\epsilon^3),
\qquad b=\frac W2(e^{-2}-e^{-4})>0.
$$

At zero field, $p_0=\Pr(J=1)=(1+e^{-2})/2$ lies strictly between zero and one. Bernoulli relative entropy therefore obeys

$$
D_{\mathrm{KL}}(P_{H_3}^J\Vert P_{H_1}^J)
=\frac{b^2}{8p_0(1-p_0)}\epsilon^4+o(\epsilon^4).
$$

Thresholding the empirical mean of $J$ gives an $O(\epsilon^{-4})$-trial test by Hoeffding's inequality. Continuous monitoring is unnecessary for this upper bound.

The no-exit statistic $Z=\mathbf1\{S_0=+1\text{ and no visible exit occurs before }1/k\}$ is another valid path diagnostic. The survival formula gives

$$
\Pr_{H_3}(Z=1)-\Pr_{H_1}(Z=1)
=\frac{We^{-1}}{18}(2+e^{-3}-9e^{-1})\epsilon^2+O(\epsilon^3).
$$

This coefficient is negative because $C_{H_3}(s)<C_{H_1}(s)$ for $s>0$ and the survival integral has positive weight. It independently supplies the same sample exponent, but requires resolving whether an exit occurred.

### No fixed-path test can improve the exponent

For these two full path laws, both relative to the common reference law, the likelihood formula gives

$$
D_{\mathrm{KL}}(P_\epsilon^{H_3}\Vert P_\epsilon^{H_1})
=\frac{\epsilon^4}{2}\,
\mathbb E_{P_0}\left[(A_{C_{H_3}}-A_{C_{H_1}})^2\right]
+o(\epsilon^4).
$$

The finite-horizon domination argument in Section 2 justifies expanding the logarithm as well as the density: both positive likelihood ratios have lower bounds of the form $e^{-c|\epsilon|(N+T)}$. The coefficient is finite and positive. Positivity also follows without evaluating it: the nonzero second-order probability difference of $J$ would be impossible if the two $A$ coefficients agreed $P_0$-almost surely.

For $n$ independent trials, relative entropy is additive. Pinsker's inequality implies that a fixed nontrivial testing advantage requires $n=\Omega(\epsilon^{-4})$. Together with the explicit two-snapshot test,

$$
\boxed{n_{\mathrm{path}}=n_{\mathrm{two\ snapshots}}=\Theta(\epsilon^{-4}).}
$$

The same sample exponent holds if only $J$ is retained from the two snapshots, or only $Z$ is retained from a resolved path.

### Endpoint-only measurements lose two powers

The [cubic mean formulas](THEORY.md#6-step-response-and-kernel-recovery) give, for this same experiment,

$$
\mathbb E_{H_3}S_T-\mathbb E_{H_1}S_T
=b\epsilon^3+O(\epsilon^4),\qquad
b=\frac W2(e^{-2}-e^{-4})>0.
$$

The endpoint is binary with zero-field probabilities $1/2$, so its relative entropy is

$$
D_{\mathrm{KL}}(P_{H_3}^{S_T}\Vert P_{H_1}^{S_T})
=\frac{b^2}{2}\epsilon^6+o(\epsilon^6).
$$

The same product-relative-entropy lower bound and empirical-mean upper bound yield

$$
\boxed{n_{\mathrm{endpoint}}=\Theta(\epsilon^{-6}).}
$$

At exactly zero field the two hypotheses have identical complete visible path laws, so no number of passive trials distinguishes them. At nonzero weak field, the trajectory contains a quadratic diagnostic even though the mean difference is cubic. The gain already follows from retaining the initial visible value alongside the endpoint; it does not require access to a hidden state. An experiment that retains $(S_0,S_T)$ is not an endpoint-only measurement in the stated comparison.

## 6. Scope of the stronger operational statement

The controlled observable remains the same binary $S$, the actuator remains the specified analytic field coupling, and preparation remains $\pi_0$. The added information can come from correlating two visible snapshots or from recording whether a visible exit occurred.

This extension sharpens the interpretation of the repository's mean-response results. It does not transfer their uniform-all-horizon approximation norm to full path laws. On increasingly long records, distinct trajectory laws can accumulate statistical evidence; a uniform path-law approximation problem is therefore a different problem requiring its own resource definition.

The second-order likelihood calculation uses established Markov change-of-measure and nonlinear-response methods. The candidate contribution is the exact combination here: passive and first-order full-path equivalence, complete second-order characterization by the hidden kernel, a sharp physical state count, and a concrete statistical separation from endpoint-only measurements. Its relation to the closest coarse-grained response theorems still requires explicit source comparison before an originality claim.
