# A uniform state–speed–accuracy tradeoff

[Checkpoint](../README.md) · [Nineteen-level construction](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Generator-word transfer](REVERSIBLE_WORD_OBSERVABILITY.md) · [Transport repair](POSITIVE_TRANSPORT_REPAIR.md)

**Research theorem, 23 September 2026.** This note makes the rival-cap dependence in the nineteen-level lower bound explicit. It proves a tradeoff uniform over a variable spectral cap, using control resolution proportional to the inverse cap. It also states the weaker dependence obtained when control resolution is held fixed. No uncapped reversible lower bound is claimed.

All logarithms are natural except those marked with a subscript. The constants below are deliberately conservative; their uniformity, rather than numerical size, is the point.

## 1. Models and the uniform theorem

Fix $H,k>0$. Use exactly the target family indexed by $n\ge1$ in the [nineteen-level construction](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md): its hidden relaxation band is $[k,3k]$, its number of independent table bits is $r=2^n$, and its physical state count is $18r2^r+2$. The exact sensitivity histogram is

$$
\Pr_\mu(g=0)=\frac12,\qquad
\Pr_\mu\!\left(g=\pm\frac j{100}\right)=\frac1{36},
\quad j=1,\ldots,9.
\tag{1}
$$

A rival may use an arbitrary finite state space and hidden stationary law. It must have the same histogram, the original field rule, original equilibrium preparation and binary readout, and an ordinarily reversible hidden generator whose nonnegative relaxation spectrum is contained in $[0,\Lambda k]$, where $\Lambda\ge3$. No positive rival spectral gap, common topology, partition, or inherited coordinates are required. States of zero stationary mass can be discarded.

Put

$$
G=\frac9{100},\quad h_0=\min\{H,[20(1+G)]^{-1}\},\quad
h_i=\frac{i h_0}{38}\ (0\le i\le38),\quad
R=e^{(1+G)h_0}<2,\quad \kappa=e^{h_0}.
\tag{2}
$$

There is an explicit $C_H\ge256$, defined in Section 2, and an absolute constant $C_*>0$, defined below, such that **simultaneously for every $\Lambda\ge3$ and $n\ge1$**, if

$$
0<\delta\le [C_H(\Lambda+2)]^{-C_*(n+1)},
\tag{3}
$$

then every such rival that predicts the target's actual controlled means to error at most $\delta$ has

$$
\boxed{D_{\rm total}\ge2^{3\cdot2^n/4}.}
\tag{4}
$$

It suffices to assume prediction accuracy only on the thirty-nine fields (2), with positive segment lengths integer multiples of $a_\Lambda/k$, where

$$
a_\Lambda=\frac1{2(\Lambda+R)}.
\tag{5}
$$

The required experiments have total duration at most $a_\Lambda M/k$, with

$$
\begin{gathered}
q_*=1-e^{-1},\quad \rho_*=1-\frac1{2e},\quad
t_*=q_*/\rho_*,\quad D_*=8/\rho_*,\\
\theta_* = \frac{\log(1/t_*)}{\log(D_*/t_*)}>0,\qquad
C_* = \frac{220}{\theta_*},\qquad
M=\left\lfloor\frac{\log(1/\delta)}{\log(D_*/t_*)}\right\rfloor.
\end{gathered}
\tag{6}
$$

Thus the allowed shortest pulse is of order $1/(k\Lambda)$ and the witnessing horizon is at most a universal constant times $\log(1/\delta)/(k\Lambda)$. These are resolution and horizon requirements on a sufficient finite experiment class. Full bounded-protocol accuracy, as in the original theorem, includes that class for every cap. A fixed positive control resolution does not include it uniformly as $\Lambda$ grows; Section 6 treats that different requirement.

## 2. Coefficient bounds independent of the rival cap

Set $k=1$ until units are restored. Expand the thirty-nine physical generators as

$$
Q(h)=K_b+\sum_\gamma e^{(1+\gamma)h}X_\gamma
                 +\sum_\gamma e^{(\gamma-1)h}Y_\gamma.
\tag{7}
$$

The coefficient matrix at fields (2) has columns indexed by the distinct frequencies $0$ and $\gamma\pm1$. It is an invertible exponential Vandermonde matrix. Let $V_H\ge1$ be the maximum row $\ell^1$ norm of its inverse, enlarged to one if necessary. It depends only on the fixed field menu and therefore only on $H$. In particular, the physical-generator expansions of $K_b$ and every $Y_\gamma$ have coefficient mass at most $V_H$ in both the target and every rival.

Define

$$
P_H=64V_H^3,\qquad
z_H=2\kappa\log(2e),\qquad
C_H=\max\{256,\ 4^{1/108}P_H^{1/3}z_H\}.
\tag{8}
$$

Here coefficient mass means the sum of absolute coefficients in the specified noncommutative word expansion; cancellation can only improve the bounds. The signed endpoint $B_s$, port endpoints $B_j$, and hidden-supported port selectors $D_j$ in the original construction all have coefficient mass at most $2V_H$ and degree one. Each positive cross-port transport

$$
T_{cd}=16D_cK_bD_d
\tag{9}
$$

has coefficient mass at most $P_H$ and degree three. The selector interpretation is used only on functions vanishing at the visible state; no full-space projector identity is assumed.

Every scalar used in row repair, norms, or lamp correlations is $18\pi_0BVB'S$, with $L$ cross-port factors in $V$ and endpoints of the preceding type. Its coefficient mass and degree obey

$$
J\le72V_H^2P_H^L\le P_H^{L+2},\qquad d\le3L+2.
\tag{10}
$$

The row moments use $L=1,2$. A translated-bit norm uses at most $18n$ cross-port edges, and a conjugated lamp correlation at most $36n+3$. Consequently every required scalar obeys

$$
J\le P_H^{36n+5},\qquad d\le108n+11.
\tag{11}
$$

All quantities in (8)–(11) are independent of $\Lambda$, the rival state count, and $n$, except for their displayed powers. The equal masses of the signed sensitivity bins in (1) are used to identify the nine conditional port measures and the signed endpoint identities. They cannot be replaced by arbitrary actuator histograms in this argument.

## 3. An exact criterion for any cap and any clock

For now fix arbitrary $a>0$ and $\Lambda\ge3$. Define

$$
\begin{gathered}
B=2(\Lambda+R),\quad q=1-e^{-aB},\quad
\rho=(1+q)/2,\quad t=q/\rho,\quad D_a=8/\rho,\\
Z=\frac\kappa a\log\frac1{1-\rho},\quad
U=\max\{1,Z\},\quad
\theta=\frac{\log(1/t)}{\log(D_a/t)},\quad
M_a=\left\lfloor\frac{\log(1/\delta)}{\log(D_a/t)}\right\rfloor.
\end{gathered}
\tag{12}
$$

The common hidden cap bounds every internal outgoing rate by $\Lambda$. Each full constant-field generator is reversible with spectrum in $[-B,0]$. The [finite-clock logarithm proposition](REVERSIBLE_WORD_OBSERVABILITY.md), applied with (11), gives a common scalar discrepancy bound

$$
\Delta_n=4P_H^{36n+5}U^{108n+11}\delta^\theta.
\tag{13}
$$

This requires mean accuracy only up to horizon $aM_a$, on the fixed menu and clock $a$. Its proof uses finitely many propagator words of at most $M_a$ steps. The number of distinct norm and lamp words creates no extra error multiplier: the same uniform experimental error applies separately to every word.

The raw rival transports (9) are nonnegative and satisfy $T_{cd}1\le16\Lambda$. Reversibility and the equal port masses make reverse transports the conditional stationary adjoints. The two row moments are within $\Delta_n$ of their target value one, so

$$
\mathbb E(R_{cd}-1)^2\le3\Delta_n.
\tag{14}
$$

Repair every unordered pair once, using the repaired adjoint in the reverse direction. The [balanced-flux repair](POSITIVE_TRANSPORT_REPAIR.md) adds no states. Its raw-versus-repaired path estimate, at maximum length $36n+3$, gives the common norm and signed lamp-correlation defect

$$
\eta_n=\Delta_n+
3\sqrt3(36n+3)(16\Lambda)^{36n+2}\sqrt{\Delta_n}.
\tag{15}
$$

Equations (13)–(15) are an explicit sufficient criterion, with no suppressed cap dependence:

$$
\boxed{\eta_n\le\frac1{6\cdot2^n}\quad\Longrightarrow\quad
D_{\rm total}\ge2^{3\cdot2^n/4}.}
\tag{16}
$$

For completeness, repaired translated bits $h_b$ satisfy $|h_b|\le1$ and $\mathbb Eh_b^2\ge1-\eta_n$. Rounding to $Z_b=\operatorname{sign}(h_b)$ costs at most $\eta_n$ in mean absolute error. Each repaired lamp kernel couples the joint $r$-bit law to its one-bit flip with failure probability at most $3r\eta_n/2$. Conditional binary entropy therefore gives

$$
\log_2D_{\rm total}\ge H(Z)\ge r(1-3r\eta_n/2).
\tag{17}
$$

This proves (16) on the rival's own state space. It does not identify vectors or coordinates between models.

## 4. Uniformity under an adaptive clock

Choose (5). Then $a_\Lambda B=1$, so every quantity $q,\rho,t,D_a,\theta$ in (12) equals its starred constant in (6), and

$$
Z=z_H(\Lambda+R)\le z_H(\Lambda+2).
\tag{18}
$$

Set $N=n+1$ and $Y=C_H(\Lambda+2)$. Since $Z>1$, equations (8), (11), and (13) give

$$
\Delta_n\le
\bigl[4P_H^{36}z_H^{108}(\Lambda+2)^{108}\bigr]^N
\delta^{\theta_*}
\le Y^{108N}\delta^{\theta_*}.
\tag{19}
$$

Also $16\Lambda\le Y$, and $3\sqrt3(36n+3)\le256^N\le Y^N$ for $n\ge1$. Thus the repair term in (15) is at most

$$
Y^{N+36n+2+54N}\delta^{\theta_*/2}
\le Y^{91N}\delta^{\theta_*/2}.
$$

Because $0<\delta<1$ and $Y\ge2$, no assumption $\Delta_n\le1$ is needed to conclude

$$
\eta_n\le Y^{109N}\delta^{\theta_*/2}.
\tag{20}
$$

Under (3) with $C_*=220/\theta_*$, this is at most $Y^{-N}$. Since $Y\ge256$ and $n\ge1$, $Y^{-N}\le1/(6\cdot2^n)$. Equation (16) proves the theorem. This is a simultaneous estimate over all caps, so substituting an accuracy-dependent cap into (3) is legitimate. Substitution into the original fixed-cap theorem without this calculation would not be justified.

## 5. Minimax form, speed requirements, and crossover

Let $\mathcal D_{\rm rev}(\delta,\Lambda)$ be the supremum over this target family of the minimum total state count among the stated capped reversible rivals with uniform error at most $\delta$ over all bounded deterministic protocols and all times. The target itself is admissible for each $n$; the known uniform reversible upper bound makes this supremum finite. Every rival has at least twenty total states because all nineteen hidden sensitivity bins have positive mass and there is one visible state.

With $Y=C_H(\Lambda+2)$, set

$$
x=\frac{\log(1/\delta)}{C_*\log Y}.
$$

If $x\ge2$, choose $n=\lfloor x\rfloor-1\ge1$. Then $n+1\le x$ and $n\ge x-2$, so (3) applies and gives

$$
\mathcal D_{\rm rev}(\delta,\Lambda)
\ge\exp\!\left[\frac{3\log2}{16}\exp\!\left(
\frac{\log2}{C_*}\frac{\log(1/\delta)}{\log Y}\right)\right].
\tag{21}
$$

If $x<2$, the right side of (21) is smaller than $2^{3/4}$, so the twenty-state histogram requirement proves (21) directly. This handles the $n\ge1$ crossover; it does not extrapolate the family to nonexistent negative-width targets.

In particular, define

$$
c_H=\frac{\log2}{C_*[1+\log C_H/\log5]},\qquad
C_0=\log\frac{16}{3\log2}.
$$

Since $\Lambda\ge3$, $\log Y\le[1+\log C_H/\log5]\log(\Lambda+2)$. Hence for every $0<\delta<1$ and $\Lambda\ge3$,

$$
\boxed{\log\log\mathcal D_{\rm rev}(\delta,\Lambda)
\ge c_H\frac{\log(1/\delta)}{\log(\Lambda+2)}-C_0.}
\tag{22}
$$

The constants here do not depend on $\delta$ or $\Lambda$. The target width selected in the proof generally depends on both. The assertion is a worst-case family statement, not a necessity for every target or for one fixed finite target as $\delta\downarrow0$.

A direct inverse form avoids any minimax selection convention. Given an integer state budget $D\ge2$, put

$$
n_D=\left\lfloor\log_2\!\left(\frac43\log_2D\right)\right\rfloor+1.
\tag{23}
$$

Then $n_D\ge1$ and $2^{3\cdot2^{n_D}/4}>D$. For this specific target, every rival with at most $D$ states, cap $\Lambda$, and error at most $\delta$ must satisfy

$$
\log[C_H(\Lambda+2)]>
\frac{\log(1/\delta)}{C_*(n_D+1)},\qquad
\Lambda+2>C_H^{-1}\exp\!\left[
\frac{\log(1/\delta)}{C_*(n_D+1)}\right].
\tag{24}
$$

For budgets below twenty the histogram already prevents a rival; (24) remains a valid vacuous implication. For larger budgets it gives a concrete hard target depending on $D$ alone.

Writing $L_\delta=\log(1/\delta)$ illustrates the consequences:

| Rival cap regime | Consequence of the uniform bound |
| --- | --- |
| $\Lambda$ bounded by a fixed constant | The known $\mathcal D_{\rm rev}\ge\exp(c\delta^{-\alpha})$ form, with positive fixed $c,\alpha$. |
| $\Lambda\le C L_\delta^s$, fixed $C,s>0$ | $\mathcal D_{\rm rev}\ge\exp\!\{\exp[cL_\delta/\log L_\delta]\}$ for sufficiently small $\delta$, after changing the positive constant. |
| $\Lambda\le C\delta^{-s}$, fixed $C,s>0$ | The ratio in (22) can stay bounded. This cap upper bound alone yields no diverging state lower bound from the present estimate. |
| A scheme covers every target with $D\le C\delta^{-p}$, fixed $C,p>0$ | Its allowed cap must obey $\Lambda+2\ge\exp[cL_\delta/\log L_\delta]$ for sufficiently small $\delta$. |

The last row follows either by rearranging (22), using $\log\log D\le\log L_\delta+O(1)$, or from (24). Constants in this table may depend on its fixed parameters and $H$. A rate-capping approximation whose cap is polynomial in $1/\delta$ is therefore compatible with this tradeoff and does not settle the unrestricted-rate reversible state cost.

## 6. Keeping the experimental clock fixed

For fixed $a>0$, retain the quantities (12) and define

$$
Y_a=\max\{256,16\Lambda,4^{1/108}P_H^{1/3}\max(1,Z)\}.
\tag{25}
$$

Exactly the estimates in Section 4, now with $Y_a$ and $\theta$, give

$$
\eta_n\le Y_a^{109(n+1)}\delta^{\theta/2},\qquad
\boxed{\delta\le Y_a^{-(220/\theta)(n+1)}
\quad\Longrightarrow\quad D_{\rm total}\ge2^{3\cdot2^n/4}.}
\tag{26}
$$

The experiments still have shortest allowed pulse $a/k$ and horizon at most $aM_a/k$. This is an explicit variable-cap statement at fixed resolution, but its accuracy exponent deteriorates with the cap.

Indeed, with $u=2a(\Lambda+R)$ and $\varepsilon=e^{-u}$,

$$
Z=\frac\kappa a(u+\log2),\qquad
\theta=\frac{\log[(1-\varepsilon/2)/(1-\varepsilon)]}
{\log[8/(1-\varepsilon)]}.
\tag{27}
$$

For $u\ge1$ the following bounds are absolute:

$$
\frac{e^{-u}}{2\log[8/(1-e^{-1})]}
\le\theta\le
\frac{e^{-u}}{2(1-e^{-1})\log8}.
\tag{28}
$$

They follow from $v/(1+v)\le\log(1+v)\le v$ with $v=\varepsilon/[2(1-\varepsilon)]$. For fixed $H,a$, $\log Y_a=\Theta_{H,a}(\log(\Lambda+2))$ as $\Lambda\to\infty$, while $\theta=\Theta(e^{-2a(\Lambda+R)})$. Thus the logarithm of the sufficient inverse error in (26) grows as

$$
\Theta_{H,a}\!\left((n+1)e^{2a\Lambda}\log(\Lambda+2)\right).
\tag{29}
$$

Define $\mathcal D_{\rm rev}^{(a)}(\delta,\Lambda)$ by the same supremum over targets and minimum over rivals as in Section 5, but require error at most $\delta$ only on menu (2), for protocols whose positive segment durations are integer multiples of $a/k$, at every complete protocol horizon. The same two-case argument as in Section 5 yields

$$
\log\log\mathcal D_{\rm rev}^{(a)}(\delta,\Lambda)
\ge\frac{\theta\log2}{220\log Y_a}\log(1/\delta)-C_0.
\tag{30}
$$

For this lower bound, accuracy up to the finite horizon $aM_a/k$ already suffices. Equations (26)–(30) do not assert that this deterioration is optimal. They record what the present logarithm method proves. In particular, the adaptive-clock result (22) is not a theorem with one fixed minimum pulse duration for all $\Lambda$.

## 7. Exit-rate budgets and limits of the result

An internal outgoing-rate budget $\Gamma k$ gives spectral cap $2\Gamma k$ for a reversible hidden generator. Therefore, for $\Gamma\ge3$, all statements apply to that budget by setting $\Lambda=2\Gamma$. The target's own internal rates and relaxation band remain fixed throughout. In physical units the clock is $1/[2k(2\Gamma+R)]$ in the adaptive version. Conversely, the spectral-cap hypothesis itself already bounds each hidden exit by $\Lambda k$; neither direction assumes a rival lower gap.

The result permits an accuracy-dependent cap only through the explicit, uniform formulas above. It gives no lower bound uniform over all finite rival rates without a cap, no binary version of the new quantitative tradeoff, and no lower bound for arbitrary field-dependent rival rules. The exact nineteen-level histogram, ordinary hidden reversibility, original preparation and readout, and original field rule remain hypotheses.

The proof is analytic. Finite computations can check the coefficient exponents, cutoff arithmetic and threshold implications; they cannot establish the universal quantifiers by enumerating finitely many models.
