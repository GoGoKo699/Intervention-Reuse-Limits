# Polynomial state bounds for bounded internal rates and a finite actuator alphabet

[Repository overview](../README.md) · [General upper bound](GENERAL_FINITE_FIELD_UPPER_BOUND.md) · [Reversible upper bound](REVERSIBLE_GENERAL_COMPRESSION.md) · [Shift-register lower bound](SHIFT_REGISTER_LOWER_BOUND.md)

**Research corollary, 22 September 2026.** A finite actuator alphabet and an upper bound on internal relaxation rates give a polynomial sufficient state count for predicting the exact driven mean. The surrogate preserves the entire stationary actuator distribution, including its centering, variance and sensitivity bound. Its internal dynamics can be nonreversible. The proof combines exact uniformization, the stationary finite-order word construction, and a regenerative coupling. These are established constructions used here to obtain a quantitative prediction bound; no originality certification is claimed.

The regenerative estimate below applies directly on every horizon. It improves the exponent obtained by first truncating the experiment to a finite reset horizon and then bounding a Poisson update count on that interval.

## 1. The theorem and its explicit polynomial

Fix $k>0$, $G>0$, $H>0$, $\Lambda>0$, and an integer $m\ge2$. Consider any target in the original finite reversible family with:

- an irreducible internal generator $K$, stationary law $\mu$, and all nonzero eigenvalues of $-K$ at most $\Lambda k$;
- a centered sensitivity $g$ taking at most $m$ distinct values in $[-G,G]$;
- external rates $q_{AB_j}(h)=k\mu_j e^{(1+g_j)h}$ and $q_{B_jA}(h)=k e^{(g_j-1)h}$;
- the original zero-field equilibrium preparation.

No lower bound on the internal spectral gap is needed. Write

$$
R=e^{(1+G)H},\qquad
q=\frac{\Lambda R}{1+\Lambda R},\qquad
\beta=-\log q=\log\left(1+\frac1{\Lambda R}\right),
\qquad C_R=1+2R^2.
$$

For any integer $\ell\ge1$, there is an autonomous Markov surrogate with at most $1+m^\ell$ total states such that

$$
\boxed{
\sup_{T>0}\sup_{|h|\le H}\sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F_\ell}[h](t)|
\le C_R q^{\ell+1}.
}
\tag{1}
$$

Protocols are deterministic and piecewise continuous. The surrogate uses a fixed binary readout, a fixed zero-field stationary preparation, and the same instantaneous-field rate rule. Its stationary sensitivity distribution is **exactly** that of the target. In particular it preserves every one-time actuator moment, the variance $W=\langle g^2,1\rangle_\mu$, and the bound $|g|\le G$. It also preserves the passive telegraph path law, equilibrium mean $\tanh h$, reference linear mean response, and zero quadratic mean response. Its internal generator is irreducible and stationary but need not be reversible; its total internal outgoing rate is at most $\Lambda k$.

For $0<\varepsilon<1$, choose

$$
\ell_\varepsilon=
\max\left\{1,
\left\lceil\frac{\log(C_R/\varepsilon)}{\beta}\right\rceil-1
\right\}.
\tag{2}
$$

Then (1) is at most $\varepsilon$, with the explicit sufficient count

$$
\boxed{
D\le1+m^{\ell_\varepsilon}
\le1+\max\left\{m,
\left(\frac{C_R}{\varepsilon}\right)^{p_{m,\Lambda,G,H}}
\right\},\qquad
p_{m,\Lambda,G,H}
=\frac{\log m}{\log(1+1/(\Lambda R))}.
}
\tag{3}
$$

This is a uniform polynomial in inverse error at fixed $m,\Lambda,G,H$. Neither the count nor the error constant depends on the original number of states, stationary masses, or individual internal transition rates. The constructor knows the full target. If the actuator is identically zero, or if $H=0$, the ordinary two-state model is exact and no approximation construction is needed.

## 2. A spectral cap supplies an exact bounded update clock

Reversibility makes $-K$ a nonnegative selfadjoint operator in $L^2(\mu)$. Let $e_i$ be the indicator of hidden state $i$. Since $K\mathbf1=0$,

$$
\mu_i(-K_{ii})
=\langle e_i,-Ke_i\rangle_\mu
\le\Lambda k\|e_i-\mu_i\mathbf1\|_\mu^2
=\Lambda k\mu_i(1-\mu_i).
$$

Thus $-K_{ii}\le\Lambda k(1-\mu_i)<\Lambda k$ unless the hidden chain has only one state. Set

$$
\nu=\Lambda k,\qquad P=I+\frac K\nu.
\tag{4}
$$

The matrix $P$ is stochastic, reversible and irreducible, and $P_{ii}\ge\mu_i>0$. Internal evolution is therefore exactly the chain that updates by $P$ at the times of an independent Poisson clock of rate $\nu$, allowing self-updates. There is no spectral regularization error. A spectral cap alone would not imply this uniform exit-rate estimate for an arbitrary nonreversible target; reversibility is used at this step.

## 3. A stationary word chain preserves finite symbol prefixes

Let $X_j$ be the stationary discrete chain with transition matrix $P$, and write $Z_j=g(X_j)$ for its actuator symbol. The process $Z$ takes at most $m$ values but need not itself be Markov.

The surrogate hidden states are all allowed words $w=(z_1,\ldots,z_\ell)$ with positive stationary probability

$$
\widehat\mu(w)=\Pr(Z_1=z_1,\ldots,Z_\ell=z_\ell)>0.
$$

Give them transition probabilities

$$
\mathsf P\bigl(w,(z_2,\ldots,z_\ell,z)\bigr)
=\Pr(Z_{\ell+1}=z\mid Z_1=z_1,\ldots,Z_\ell=z_\ell),
\tag{5}
$$

and sensitivity $\gamma(w)=z_\ell$. When $\ell=1$, the successor word is simply $(z)$. Stationarity of $Z$ implies $\widehat\mu\mathsf P=\widehat\mu$. Its stationary output process has exactly the same consecutive-symbol laws as $Z$ through length $\ell+1$: the state and its next output have the correct length-$\ell+1$ law, deterministic shifts identify the state with the last $\ell$ outputs, and stationarity moves this block to any chosen starting time.

The allowed-word chain is irreducible even though some symbol words may have zero probability. To see this, realize any two allowed words by positive-probability microscopic paths. Irreducibility of $P$ supplies a microscopic bridge from the end of the first path to the start of the second. Every successive length-$\ell+1$ block of the concatenated path has positive probability, and hence supplies a legal transition in (5). Zero-probability words are omitted throughout.

Use the continuous-time internal generator

$$
\widehat K=\nu(\mathsf P-I).
$$

It is stationary under $\widehat\mu$, has outgoing rates at most $\nu$, and is generally nonreversible. Its actuator histogram agrees exactly with that of the target. Attach the single state $A$ using the original external rate rule and the sensitivities $\gamma$. This uses at most $1+m^\ell$ physical states. The word is an ordinary internal state; no additional memory register is used.

Stationarity of $\widehat K$ gives the full equilibrium law

$$
\widehat\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\widehat\pi_h(w)=\frac{\widehat\mu(w)e^h}{2\cosh h}.
$$

The external edges balance individually under this law, while internal stationary fluxes sum to zero. The passive and first two mean-response statements follow from stationarity, the original rate rule and centered sensitivity, as in [the general upper-bound construction](GENERAL_FINITE_FIELD_UPPER_BOUND.md#4-compress-a-finite-alphabet-of-hidden-words). They do not require internal reversibility.

## 4. Coupling a visit to the hidden block

The target and surrogate have the same escape hazard from $A$,

$$
k e^{h(t)}\langle e^{h(t)g},1\rangle_\mu,
$$

which is at most $b:=kR$. At an entry time $s$ into $B$, their respective hidden laws are their stationary laws tilted by the same function $e^{h(s)z_0}$ of the first actuator symbol. Their stationary symbol-prefix laws through length $\ell+1$ agree exactly. Tilting those laws by the same first-symbol function, with the same normalization, preserves equality. Consequently the first $\ell+1$ symbols of a new hidden visit can be coupled exactly. The initial visit, conditional on $S_0=+1$, has the untilted stationary prefix and can also be coupled exactly.

Use the same independent rate-$\nu$ update clock for these coupled symbols. Until more than $\ell$ updates have occurred in a visit, the symbols agree, so all field-dependent killing rates agree. This argument applies to an arbitrary deterministic protocol, not only to a constant field.

For a bound uniform in the observation time, add a common reset representation. Every hidden-to-$A$ rate is at least

$$
\alpha=\frac kR.
$$

Each full generator can be decomposed as

$$
Q(h)=\alpha(\mathbf1 e_A^T-I)+Q^{\rm res}(h),
\tag{6}
$$

where $Q^{\rm res}(h)$ is again a Markov generator. In the residual generator, each hidden-to-$A$ rate is reduced by $\alpha$; internal dynamics and rates out of $A$ are unchanged. The reset part sends every state to $A$ at the times of a rate-$\alpha$ Poisson clock, with self-updates when already at $A$.

Couple this clock in both models, independently of the internal update clock. At every reset the models are simultaneously at $A$, and their visible paths can be coupled afresh. Until a symbol prefix is exhausted, couple their exits from $A$, internal updates and residual killings as above. Declare the coupling bad if a hidden visit reaches its $(\ell+1)$st update before it ends; retain that declaration until the next common reset. After a bad declaration, any coupling with the correct marginals suffices. A good coupling guarantees equal visible states. This clock decomposition changes no model and introduces no extra physical state.

## 5. A regenerative estimate without a horizon cutoff

Fix a protocol and an observation time $t$. Let $N_\nu(u)$ denote a Poisson count of mean $\nu u$, and put

$$
p_\ell(u)=\Pr\{N_\nu(u)>\ell\}.
$$

If the coupling is bad at $t$, the visit that first exhausted a prefix after the most recent common reset must have begun either at time zero, with both models initially in $B$, or at an $A\to B$ entry time $s$. There was no common reset between that visit's start and $t$, and the potential internal clock had more than $\ell$ updates during that interval. Counting potential updates even after a visit has ended only enlarges the event.

The initial visible states can be coupled exactly, with probability $1/2$ of starting in $B$. All target entries into $B$ have intensity at most $b$. Independent future increments of the reset and update clocks therefore give

$$
\Pr\{\text{bad at }t\}
\le\frac12 e^{-\alpha t}p_\ell(t)
+b\int_0^t e^{-\alpha(t-s)}p_\ell(t-s)\,ds.
\tag{7}
$$

Here all target entry times may be counted, including those after a previous bad declaration. This overcounts possible causes of the current bad event and is harmless. To justify the integral despite random entry times, condition on the history at each entry. The future clock increments are independent of that history. Summing the resulting deterministic function of the entry time and using the entry counting process's intensity bound $b$ yields (7). Finite expected entry count on each bounded interval justifies this conditioning and summation.

Let $\tau_{\ell+1}$ be the time of the $(\ell+1)$st event of the rate-$\nu$ clock. Its Laplace transform is

$$
\mathbb E e^{-\alpha\tau_{\ell+1}}
=\left(\frac\nu{\nu+\alpha}\right)^{\ell+1}
=q^{\ell+1}.
$$

Consequently,

$$
e^{-\alpha t}p_\ell(t)
\le\mathbb E[e^{-\alpha\tau_{\ell+1}};
\tau_{\ell+1}\le t]
\le q^{\ell+1},
$$

and Tonelli's theorem gives the exact integral

$$
\int_0^\infty e^{-\alpha u}p_\ell(u)\,du
=\mathbb E\int_{\tau_{\ell+1}}^\infty e^{-\alpha u}\,du
=\frac{q^{\ell+1}}\alpha.
\tag{8}
$$

Substituting in (7) yields

$$
\Pr\{S_F(t)\ne S_{\widehat F_\ell}(t)\}
\le\left(\frac12+\frac b\alpha\right)q^{\ell+1}.
$$

Since the readout takes values $\pm1$, the absolute mean difference is at most twice this probability. Now $b/\alpha=R^2$, which proves (1) for every $t$ and every allowed protocol. No truncation of the horizon and no union bound growing with the full experiment duration is used. This is a bound for the visible state at each observation time; it does not bound total variation between complete visible histories uniformly over unbounded horizons.

## 6. The binary bounded-rate problem

For sensitivities $g=\pm s$ with $s=\sqrt W>0$, centering forces both levels to have stationary mass $1/2$. The surrogate retains these two values and their masses exactly. In the bounds above one may use $m=2$ and the sharper actual sensitivity bound $G=s$, even if the ambient family allows a larger $G$. Thus put

$$
R_s=e^{(1+s)H},\qquad
p_{\rm bin}=\frac{\log2}{\log(1+1/(\Lambda R_s))}.
$$

Every such target with internal relaxation rates at most $\Lambda k$ has a predictor obeying

$$
\boxed{
D\le1+\max\left\{2,
\left(\frac{1+2R_s^2}{\varepsilon}\right)^{p_{\rm bin}}
\right\}.
}
\tag{9}
$$

In particular this applies to the two-level class with all nonzero internal rates in $[k,3k]$, by setting $\Lambda=3$. That class contains the targets in [the stronger shift-register lower bound](SHIFT_REGISTER_LOWER_BOUND.md). For this class, put $L_\varepsilon=\log(1/\varepsilon)$. The current bounds against unrestricted Markov predictors have the form

$$
\exp\!\left(c\frac{L_\varepsilon}{\log L_\varepsilon}\right)
\ \lesssim\ D_*\ \lesssim\ \varepsilon^{-p_{\rm bin}},
$$

for sufficiently small $\varepsilon$, with constants depending on the fixed parameters. If protocols have a fixed minimum dwell $a/k$, the separate necessary bound is $\exp(c_a L_\varepsilon^{2/3})$; the same polynomial upper still applies. The stronger unrestricted lower uses shrinking intervals. The polynomial upper is not claimed optimal, and no polynomial lower is proved. These bounds do not determine whether requiring reversible predictors changes the optimal order.

The result assumes the kinetic model is supplied. Computing the required word probabilities, numerical precision, learning from experiments, statistical noise and parameter storage are outside its state-count guarantee. The large collection of allowed words is counted in full as physical Markov states.

## 7. A reversible surrogate preserving the spectral cap

A prediction partition gives an alternative construction whose internal dynamics remain reversible and retain the original spectral cap. Its sufficient state count is larger than the polynomial bound above, but smaller than the current unrestricted-rate general-family bound. At fixed $m,\Lambda,G,H$, it gives

$$
\boxed{D_{\rm rev}(\varepsilon)
\le\exp\!\left[C_{m,\Lambda,G,H}\,
\varepsilon^{-p_{m,\Lambda,G,H}}\log\frac2\varepsilon\right],}
\tag{10}
$$

for a finite constant depending only on the displayed fixed parameters. The exponent $p_{m,\Lambda,G,H}$ is exactly the exponent in (3). Thus the bound is $\exp[O(\varepsilon^{-p}\log(1/\varepsilon))]$ as $\varepsilon\downarrow0$; a polynomial reversible upper bound is not established here.

This surrogate preserves the entire stationary actuator distribution, the original bound $|g|\le G$, every actuator moment including $W$, and the internal spectral interval $[0,\Lambda k]$. It consequently retains all passive, static, and low-order mean constraints of the target, as well as reversibility at each constant field. No moment correction or replicas are needed, since the partition refines the exact actuator levels.

### 7.1. The reversible prediction partition

Use the exact stochastic matrix $P$ from (4). Let $D_a$ indicate the microscopic states with actuator value $a$, for each value in the alphabet. For each word $w=(a_1,\ldots,a_r)$, $1\le r\le\ell$, define

$$
f_w=P D_{a_1}P D_{a_2}\cdots P D_{a_r}\mathbf1.
$$

These are next-word prediction probabilities and take values in $[0,1]$. Choose a resolution $\zeta>0$. Refine the partition into exact actuator levels by the value intervals of width at most $\zeta$ of every such function. With

$$
d_\ell=\sum_{r=1}^{\ell}m^r,\qquad
J_\zeta=1+\lceil1/\zeta\rceil,
$$

there are at most $n\le mJ_\zeta^{d_\ell}$ nonempty cells. Let $E$ be conditional expectation under $\mu$ onto these cells. Then $E$ commutes with all $D_a$, and

$$
\|f_w-Ef_w\|_\infty\le\zeta.
$$

For cells $C,D$, put $\mu_C^{\rm cell}=\mu(C)$ and define

$$
\overline P_{CD}
=\frac1{\mu(C)}\sum_{i\in C,j\in D}\mu_iP_{ij},
\qquad \overline K=\nu(\overline P-I),\quad\nu=\Lambda k.
\tag{11}
$$

The cell matrix is stochastic and reversible under $\mu^{\rm cell}$. It is irreducible because the quotient of the original connected transition graph is connected. Assign each cell its original actuator value and attach $A$ with the original rate rule.

The lifted cell generator is $EKE$ on the cell-constant subspace. For every such function $v$, reversibility and the target spectral cap give

$$
0\le-\langle v,EKEv\rangle_\mu
=-\langle v,Kv\rangle_\mu
\le\Lambda k\|v\|_\mu^2.
$$

The variational characterization of eigenvalues therefore places the spectrum of $-\overline K$ inside $[0,\Lambda k]$. This is a bound on the actual reversible generator, rather than only an outgoing-rate bound. If the target also has a positive lower bound on its nonzero relaxation rates, the same Rayleigh-quotient argument on centered cell-constant functions preserves that lower bound as well. In particular, a target spectral band $[k,3k]$ remains inside $[k,3k]$ in the reversible surrogate.

Let $\overline f_w$ denote the cell-chain prediction functions lifted to the original space. They obey the recursion

$$
\overline f_{(a,w)}=EPD_a\overline f_w,
\qquad\overline f_{\varnothing}=\mathbf1.
$$

Insert $Ef_w$ between $f_w$ and $\overline f_w$. The projection error is at most $\zeta$, and the remaining term is bounded by the suffix error because $E,P,D_a$ are sup-norm contractions. Induction yields

$$
\|f_w-\overline f_w\|_\infty\le r\zeta
\qquad(|w|=r\le\ell).
$$

A stationary word $(a_0,w)$ has probability $\langle\mathbf1,D_{a_0}f_w\rangle_\mu$. Thus the stationary symbol-prefix laws through length $\ell+1$ have total variation at most

$$
\theta=\frac12m^{\ell+1}\ell\zeta.
\tag{12}
$$

Their one-symbol marginals agree exactly. At an entry into $B$, tilting both prefix laws by $e^{h a_0}$ therefore has the same normalization, at least $e^{-GH}$, and pointwise weight at most $e^{GH}$. The total variation after the tilt is bounded by $L_H\theta$, where

$$
L_H=e^{2GH}.
$$

The initial $B$ visit uses untilted stationary prefixes and has error at most $\theta$.

### 7.2. Regeneration with approximate prefixes

Use the reset and update clocks from Sections 4--5. At each new hidden visit, maximally couple the two symbol prefixes. Declare the coupling bad immediately if that prefix coupling fails; otherwise declare it bad only if the visit reaches its $(\ell+1)$st update before ending. Retain the declaration until the next common reset, when both models return to $A$ and can be coupled afresh. Prefixes are sampled independently of the future reset and internal-update clocks.

For the initial visit the prefix-failure probability is at most $\theta$, and for every later visit it is at most $L_H\theta$. The same stopped-entry argument as in (7) gives

$$
\begin{aligned}
\Pr\{\text{bad at }t\}\le{}&
\frac12e^{-\alpha t}[\theta+p_\ell(t)]\\
&+b\int_0^t e^{-\alpha(t-s)}
[L_H\theta+p_\ell(t-s)]\,ds.
\end{aligned}
\tag{13}
$$

For a prefix-failure cause, absence of a later reset contributes the exponential factor, independently of the sampled prefix. For an exhaustion cause, the same factor and the potential Poisson update count give the second term inside each bracket. Counting every target entry, including entries after an earlier bad declaration, can only enlarge the bound. The target entry intensity remains at most $b=kR$.

Since $L_H\ge1$, equations (8) and (13), together with the binary readout, prove the all-horizon bound

$$
\boxed{
\sup_{h,t}|m_F[h](t)-m_{\overline F}[h](t)|
\le C_R\bigl(L_H\theta+q^{\ell+1}\bigr).
}
\tag{14}
$$

Indeed, the initial contribution is bounded by $\tfrac12(L_H\theta+q^{\ell+1})$ and the entry contribution by $(b/\alpha)(L_H\theta+q^{\ell+1})$; twice their sum gives $C_R=1+2R^2$. This argument provides the uniform horizon bound directly, without introducing a finite observation cutoff.

### 7.3. Explicit choices and the resulting count

For $0<\varepsilon<1$, choose

$$
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_R/\varepsilon)}{\beta}\right\rceil-1
\right\},
\qquad
\zeta=\frac{\varepsilon}
{C_RL_H\ell m^{\ell+1}},
$$

where $\beta=-\log q$ as in Section 1. Then

$$
q^{\ell+1}\le\frac{\varepsilon}{2C_R},
\qquad
L_H\theta\le\frac{\varepsilon}{2C_R}.
$$

Equation (14) is consequently at most $\varepsilon$, and an explicit sufficient total count is

$$
\boxed{D_{\rm rev}\le
1+m(1+\lceil1/\zeta\rceil)^{\sum_{r=1}^{\ell}m^r}.}
\tag{15}
$$

At fixed parameters, $\ell=O(\log(2/\varepsilon))$ and

$$
m^\ell\le\max\left\{m,
\left(\frac{2C_R}{\varepsilon}\right)^p\right\},
\qquad p=p_{m,\Lambda,G,H}.
$$

Therefore $d_\ell=O(\varepsilon^{-p})$ and $\log J_\zeta=O(\log(2/\varepsilon))$. Taking the logarithm of (15) proves (10). For the binary case, use $m=2$, $G=s$, and the same $p_{\rm bin}$ appearing in (9).

The polynomial nonreversible construction and this singly exponential reversible construction are sufficient bounds, not a proved separation between optimal predictor classes. Whether a polynomial-size reversible predictor always suffices remains open.
