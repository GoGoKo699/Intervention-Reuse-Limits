# General finite-field compression preserving reversibility and variance

[Repository overview](../README.md) · [General nonreversible upper bound](GENERAL_FINITE_FIELD_UPPER_BOUND.md) · [Canonical sharp theorem](FINITE_FIELD.md)

**Working extension, 22 September 2026.** Every target in the original reversible family has a finite-state approximation of its exact mean, uniformly over all bounded protocols and all horizons, within that same reversible family. The surrogate preserves the original sensitivity bound and sensitivity variance exactly. The state bound is independent of target size and internal rates but is very large and nonsharp. The argument establishes feasibility of structure-preserving compression; it does not extend the canonical subclass's sharp logarithmic-squared state law to general actuators.

The construction uses reversible conditional-expectation lumping, finite collections of prediction functions, and a two-point moment construction. These ingredients are combined with the reset and regularization estimates in the [general upper-bound proof](GENERAL_FINITE_FIELD_UPPER_BOUND.md). Their established mathematical ingredients are attributed in [the prior-art comparison](PRIOR_ART.md).

For the narrower class with a fixed finite sensitivity alphabet and an internal spectral cap, [the bounded-rate theorem](BOUNDED_RATE_FINITE_FIELD.md) now gives a sharper reversible count $\exp[C\delta^{-p}\log(2/\delta)]$ while retaining the entire actuator distribution and the spectral band. Its nonreversible construction is polynomial in $1/\delta$. The present theorem continues to cover arbitrary bounded sensitivities and unrestricted internal rates.

## 1. The theorem

Fix $k>0$, $H>0$, and $0<W\le G^2$. Let $\mathcal F(k,G,W)$ be the original family: an arbitrary finite irreducible reversible internal generator $K$ with stationary law $\mu$, a centered actuator $g$ with $|g_i|\le G$ and $\langle g^2,1\rangle_\mu=W$, and external rates

$$
q_{AB_j}(h)=k\mu_j e^{(1+g_j)h},\qquad
q_{B_jA}(h)=k e^{(g_j-1)h}.
$$

For every $0<\varepsilon<1$, there is a finite number $D(G,H,\varepsilon)$ such that every target $F\in\mathcal F(k,G,W)$ has a surrogate $\widehat F\in\mathcal F(k,G,W)$ with at most $D$ total states and

$$
\boxed{\sup_{T>0}\ \sup_{|h|\le H}\ \sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|\le\varepsilon.}
\tag{1}
$$

Protocols are deterministic and piecewise continuous, and both models start from their own zero-field equilibria. The constructor knows the full target. The surrogate retains reversibility at every constant field, the exact bound $G$, exact variance $W$, the passive telegraph law, equilibrium mean $\tanh h$, reference linear mean, and zero quadratic mean. This is a physical Markov-state count; no external clock or memory is supplied.

Time is rescaled by $k$ below, so $k=1$ in all construction formulas. This rescaling does not change the state count.

## 2. An explicit sufficient state bound

Put

$$
R=e^{(1+G)H},\qquad \alpha=R^{-1},\qquad
B=2(R-1),\qquad L_H=e^{2GH},
$$

and choose

$$
\eta=\min\left\{1,G,\frac{\varepsilon}{16HR^2}\right\},
\quad m=\left\lceil\frac{2G}{\eta}\right\rceil,
\quad T_*=R\log\frac{16}{\varepsilon}.
$$

Next set

$$
\Delta=\min\left\{\frac{T_*}{2},
\frac{\varepsilon^2}{128B^2e^{4BT_*}T_*}\right\},
\qquad M=\frac{T_*}{\Delta},
$$

$$
\ell=\left\lceil
\frac{M+\log[16(1+RT_*)/\varepsilon]}{\log2}
\right\rceil,
\qquad
\beta=\frac{\varepsilon}
{8L_H(1+RT_*)\ell m^{\ell+1}}.
$$

Finally define

$$
d=\sum_{r=1}^{\ell}m^r,\qquad
J=1+\lceil1/\beta\rceil.
$$

A sufficient total state count is

$$
\boxed{D\le1+2mJ^d.}
\tag{2}
$$

The factor two is the maximum number of moment-matching replicas per partition cell. Most of the growth comes from quantizing many prediction functions. The purpose of (2) is a uniform existence bound; it is not proposed as a practical construction size or an optimal rate.

## 3. Two preliminary approximations

Partition $[-G,G]$ into at most $m$ bins of width at most $\eta$. Replace $g$ by its $\mu$-conditional mean $z$ within each nonempty bin. This gives

$$
|z|\le G,\qquad \langle z,1\rangle_\mu=0,
\qquad\|g-z\|_\infty\le\eta.
$$

The [uniform reset perturbation estimate](GENERAL_FINITE_FIELD_UPPER_BOUND.md#2-quantize-the-actuator-without-changing-its-mean-or-bound) bounds the resulting mean error, for all protocols and horizons, by $2HR^2\eta$.

Set $P=e^{\Delta K}$ and $K_\Delta=(P-I)/\Delta$. This preserves reversibility and $\mu$, and represents internal motion as updates by $P$ at independent Poisson times of rate $1/\Delta$. The [integrated semigroup estimate](GENERAL_FINITE_FIELD_UPPER_BOUND.md#3-replace-arbitrarily-fast-internal-rates-by-a-bounded-clock) gives

$$
\|e^{Kt}-e^{K_\Delta t}\|_{2,\mu}
\le\min\{1,2\Delta/t\}.
$$

Combined with the bounded field-dependent perturbation and Gronwall's inequality, this makes the mean error from replacing $K$ by $K_\Delta$ at most $\varepsilon/4$ on every horizon at most $T_*$, uniformly over the allowed protocols. The choice of $\Delta$ above is precisely a sufficient value from that estimate.

After this step, the remaining task is to approximate finite symbol sequences of the stationary discrete chain $P$ by a **reversible** chain. A canonical finite-order word chain need not be reversible; the next section uses a partition of the original states instead.

## 4. A reversible partition using prediction functions

Let $\mathcal Z$ be the alphabet of nonempty quantization bins, with $|\mathcal Z|\le m$. For each symbol $a$, write $D_a$ for the diagonal indicator of that bin. For a nonempty word $w=(a_1,\ldots,a_r)$ define

$$
f_w=P D_{a_1}P D_{a_2}\cdots P D_{a_r}1.
\tag{3}
$$

This is the conditional probability of seeing the next $r$ symbols equal to $w$, given the present microscopic state. Every value lies in $[0,1]$.

Refine the initial actuator-bin partition by recording, for every word of length $1\le r\le\ell$, the interval of width at most $\beta$ containing $f_w(i)$. There are at most $d$ functions and at most $J$ recorded values for each, so the refined partition has at most

$$
n\le mJ^d
$$

nonempty cells. Let $E$ be conditional expectation under $\mu$ onto functions constant on these cells. Then

$$
\|f_w-Ef_w\|_\infty\le\beta,
\tag{4}
$$

and $E$ commutes with every $D_a$ because each cell remains inside one actuator bin.

For cells $C,D$, define their masses $\nu_C=\mu(C)$ and the stochastic matrix

$$
\overline P_{CD}
=\frac1{\nu_C}\sum_{i\in C,j\in D}\mu_iP_{ij}.
\tag{5}
$$

The lifted operator of this cell chain is $EPE$ on cell-constant functions. Its stationary law is $\nu$, and reversibility follows directly from $\mu_iP_{ij}=\mu_jP_{ji}$. All entries are positive because the original finite irreducible generator has strictly positive $e^{\Delta K}$.

Let $\overline f_w$ be the next-word prediction functions of the cell chain, lifted back to the original state space. They satisfy

$$
\overline f_{(a,w)}=EPD_a\overline f_w,
\qquad \overline f_{\varnothing}=1.
$$

Using (4), the contraction of $E,P,D_a$ in sup norm, and induction gives

$$
\|f_w-\overline f_w\|_\infty\le r\beta
\qquad (|w|=r\le\ell).
\tag{6}
$$

Indeed, insert $Ef_w$ between the two functions; the projection error costs $\beta$, and the remaining error is bounded by the prediction error of the suffix.

An original stationary symbol word of length $r+1$ has probability $\langle1,D_{a_0}f_w\rangle_\mu$, with $|w|=r$. The cell-chain probability replaces $f_w$ by $\overline f_w$, while the initial symbol marginal agrees exactly. Thus their stationary symbol-block laws through length $\ell+1$ have total variation at most

$$
\theta=\frac12m^{\ell+1}\ell\beta.
\tag{7}
$$

This coarse bound sums the absolute errors of all words. It is sufficient for the existence theorem; no claim that the factor $m^{\ell+1}$ is necessary is made.

## 5. Tilted entries and the finite-horizon path comparison

Attach $A$ to the cell chain with internal generator $(\overline P-I)/\Delta$, cell stationary law $\nu$, and sensitivity equal to the original bin value $z_C$. This is a reversible member of the model family, except that its sensitivity variance is the quantized variance rather than necessarily $W$.

The stationary one-symbol marginal is exactly unchanged. Hence the exit hazard from $A$ is identical to that in the regularized quantized target and is bounded by $R$. At an entry into $B$, both initial symbol-block laws are tilted by $e^{h z_0}$ on their first symbol. Their normalization is exactly the same because their one-symbol marginals coincide. For $|h|\le H$, the tilted block laws consequently have total variation at most

$$
\frac{e^{GH}}{e^{-GH}}\theta=L_H\theta.
\tag{8}
$$

An initial $B$ visit starts from the untilted stationary law and satisfies the same bound, since $L_H\ge1$.

Couple these two prefixes by a maximal coupling, and use the same independent Poisson internal-update clock. If the prefixes agree, their visible killing rates agree until the $(\ell+1)$st update. Couple those exits as well. Each visit has at most $T_*$ available time, so its failure probability is at most

$$
L_H\theta+p_\ell,
\qquad p_\ell=\Pr\{\operatorname{Pois}(T_*/\Delta)>\ell\}.
$$

The expected number of hidden-block visits beginning before $T_*$ is at most $1+RT_*$. A union bound over the successive visits gives a full visible-path total variation bound $(1+RT_*)(L_H\theta+p_\ell)$ on that finite horizon. The symbol tilt changes the prefix comparison, but it does not change the independent Poisson count bound.

The parameter choices ensure

$$
L_H\theta\le\frac{\varepsilon}{16(1+RT_*)},
\qquad
p_\ell\le e^{T_*/\Delta}2^{-\ell}
\le\frac{\varepsilon}{16(1+RT_*)}.
$$

Therefore the difference of the binary means is at most

$$
2(1+RT_*)(L_H\theta+p_\ell)\le\frac\varepsilon4
\tag{9}
$$

for all protocols on horizons at most $T_*$. This is an approximate symbol-prefix coupling, unlike the exact prefix match in the nonreversible word-chain construction.

## 6. Restore the original variance with two replicas per cell

The refined cell $C$ lies inside an actuator bin $[a,b]$ of width at most $\eta$. Using the original, unquantized $g$ within that cell, compute its conditional mean $m_C$ and conditional variance $v_C$.

If $v_C=0$, use a single sensitivity value $\gamma_C=m_C$. Otherwise $m_C>a$, and

$$
v_C\le(m_C-a)(b-m_C)
$$

because the original sensitivity lies in $[a,b]$. Set

$$
\gamma_{C,1}=a,\qquad
\gamma_{C,2}=m_C+\frac{v_C}{m_C-a}\le b,
$$

with weights

$$
w_{C,1}=\frac{v_C}{(m_C-a)^2+v_C},\qquad
w_{C,2}=\frac{(m_C-a)^2}{(m_C-a)^2+v_C}.
\tag{10}
$$

These are positive probabilities. Their mean and variance are exactly $m_C$ and $v_C$, and both nodes lie in the original bin. Thus at most two replicas per cell suffice.

Give replica $(C,i)$ stationary mass $\widehat\mu_{C,i}=\nu_Cw_{C,i}$ and discrete transition probabilities

$$
P^{\mathrm{rep}}_{(C,i),(D,j)}
=\overline P_{CD}w_{D,j}.
\tag{11}
$$

Detailed balance holds because

$$
\widehat\mu_{C,i}P^{\mathrm{rep}}_{(C,i),(D,j)}
=\nu_C\overline P_{CD}w_{C,i}w_{D,j}
$$

is symmetric under exchanging the replicas. The continuous-time generator $(P^{\mathrm{rep}}-I)/\Delta$ is irreducible and reversible. Its cell projection has exactly the cell generator $(\overline P-I)/\Delta$.

Initially give every replica in cell $C$ the bin sensitivity $z_C$. Strong lumpability then makes its entire visible behavior identical to the cell model at every field and protocol. Now change each replica's sensitivity to $\gamma_{C,i}$ from (10). Both sensitivities lie in the same original bin, so their difference is at most $\eta$. The uniform reset perturbation estimate charges at most another $2HR^2\eta$ in mean error.

The final sensitivity has

$$
|\gamma_{C,i}|\le G,\qquad
\sum_{C,i}\widehat\mu_{C,i}\gamma_{C,i}
=\sum_C\nu_Cm_C=0,
$$

and

$$
\sum_{C,i}\widehat\mu_{C,i}\gamma_{C,i}^2
=\sum_C\nu_C(m_C^2+v_C)=W.
\tag{12}
$$

The final surrogate therefore belongs to the original reversible family with the exact target parameters $k,G,W$. No approximate moment equality is used in this membership claim.

## 7. Error budget and unrestricted horizons

On a horizon of length at most $T_*$, the successive errors are:

| Approximation | Uniform mean-error bound |
|---|---:|
| Quantize the target actuator, then restore the original moments on replicas | $4HR^2\eta\le\varepsilon/4$ |
| Regularize the internal rates | $\varepsilon/4$ |
| Reversible partition and finite-prefix comparison | $\varepsilon/4$ |

For a longer horizon, compare the original target and final surrogate after restarting each at its own zero-field equilibrium $T_*$ before the observation time. Every model has common reset rate at least $\alpha$. Each restart changes the final mean by at most $2e^{-\alpha T_*}$, and the two restart errors total

$$
4e^{-\alpha T_*}=\frac\varepsilon4.
$$

Apply the finite-horizon comparison to the final protocol segment and add the four error contributions. This proves (1). The same reset estimate works although the target and surrogate have different hidden state spaces, since each restart is compared within its own model before the two restarted means are compared.

As elsewhere in the repository, this does not bound total variation between complete visible histories uniformly over unbounded horizons. Those histories can accumulate evidence even when their instantaneous means remain close.

## 8. Interpretation and limitations

This result removes reversibility and exact variance preservation as possible obstructions to the *existence* of a uniform finite-state mean approximation for the general bounded-sensitivity family. Its large bound does not establish that those structural requirements are inexpensive in the optimal state count. A sharp general-family complexity law remains open.

The result also differs from exact state lumpability: the original target need not be lumpable under the prediction partition, and the final replica chain is a constructed surrogate. Only the finite-error field-on mean guarantee is approximate; membership in the original reversible model family and the passive/static/low-order constraints are exact. The full target is supplied, and computational cost, parameter precision, identification from data, and optimal experimental protocols are outside the theorem.

## 9. A smaller bound from controlled prediction functions

The long symbol prefixes in Sections 4--5 can be replaced by prediction functions for the bounded field perturbation. This improves the sufficient count to

$$
\boxed{D(G,H,\varepsilon)\le
\exp\!\left\{\exp\!\left[C_{G,H}\log^2\frac{16}{\varepsilon}\right]\right\},}
\tag{13}
$$

for a finite constant $C_{G,H}$ depending only on the fixed positive $G,H$. The conclusion, including reversibility, exact variance, and all-protocol/all-horizon mean error, is unchanged. This remains a very large, nonsharp upper bound. Its proof uses a truncated Dyson expansion and a conditional-expectation Galerkin estimate, not a new physical closure assumption.

### 9.1. A projection estimate for arbitrary controls

Keep the actuator quantization and rate regularization in Section 3, and write $T=T_*$. On the regularized full state space, including $A$, let

$$
Q(h)=Q_0+V_h,\qquad S_0(t)=e^{Q_0t}.
$$

Here $Q_0$ is the zero-field generator with internal generator $K_\Delta$. In the sup norm on state functions,

$$
\|Q_0\|_\infty\le M_0:=2(1+\Delta^{-1}),\qquad
\|S_0(t)\|_\infty\le1,
$$

$$
\|V_h\|_\infty\le B=2(R-1),\qquad
\|V_h-V_{h'}\|_\infty\le L_V|h-h'|,
\quad L_V:=2(1+G)R.
\tag{14}
$$

The first bound follows from the outgoing rates, which are at most $1+\Delta^{-1}$. The others follow directly from the external transition rates and the mean-value theorem. In particular, all constants are independent of the original internal rates and number of states.

Let $E$ be conditional expectation under the full equilibrium $\pi_0$, for a partition that leaves $A$ alone and refines the quantized actuator bins in $B$. It is a sup-norm contraction. It commutes with every $V_h$: hidden multiplication coefficients are constant on each cell, and the weighted sums into and out of $A$ are unchanged by conditional expectation. The operator $E Q(h)E$, restricted to cell-constant functions, is the generator of the reversible cell model; its internal generator is the stationary cell average of $K_\Delta$.

For a protocol on $[s,t]$, let $U_h(s,t)$ be the full backward transition operator and put

$$
f(s)=U_h(s,t)S,
$$

where $S$ is the binary visible readout. Suppose the partition has the uniform prediction property

$$
\|(I-E)U_h(s,t)S\|_\infty\le\sigma
\quad\text{whenever }0\le t-s\le T,
\tag{15}
$$

for every allowed protocol. Write $\bar f(s)$ for the lifted cell-model prediction with the same terminal readout. The backward equations give

$$
-\partial_s(Ef-\bar f)
=E Q(h(s))E(Ef-\bar f)+E Q_0(I-E)f,
\qquad (Ef-\bar f)(t)=0.
$$

The $V_h$ term in the forcing vanishes because $E$ commutes with $V_h$. The cell propagator is stochastic, so variation of constants yields

$$
\|Ef(s)-\bar f(s)\|_\infty\le M_0T\sigma.
\tag{16}
$$

Since $\pi_0E=\pi_0$, (16) also bounds the mean difference from the specified stationary preparations. This estimate uses the actual cell generator; it does not assume that averaging a generator commutes with exponentiation.

### 9.2. A finite collection that controls every backward prediction

The following explicit choices construct a partition satisfying (15). Set

$$
\sigma=\frac{\varepsilon}{4M_0T},\qquad
z=BT,\qquad
p=\left\lceil\frac{2z+\log(8/\sigma)}{\log2}\right\rceil,
\qquad a=\frac{\sigma e^{-z}}8.
\tag{17}
$$

All these quantities are positive, and $p\ge1$. Put $W_h=V_h/B$, so $\|W_h\|_\infty\le1$. Choose grids of $[0,T]$ and $[-H,H]$ with mesh sizes at most

$$
\delta_t=\frac{a}{2(p+1)M_0},\qquad
\delta_h=\frac{aB}{2pL_V},
$$

and cardinalities at most

$$
N_t=1+\left\lceil\frac{T}{\delta_t}\right\rceil,
\qquad
N_h=1+\left\lceil\frac{2H}{\delta_h}\right\rceil.
$$

For every $1\le n\le p$, record all state functions of the form

$$
S_0(\tau_0)W_{b_1}S_0(\tau_1)\cdots
W_{b_n}S_0(\tau_n)S,
\tag{18}
$$

where each $\tau_i$ and $b_i$ belongs to its grid. No restriction on the sum of the grid times is needed. All functions have values in $[-1,1]$. There are at most

$$
N_f=\sum_{n=1}^p N_t^{n+1}N_h^n
\tag{19}
$$

such functions. Refine the actuator-bin partition by their value intervals of width at most $a$. This makes the projection error of every recorded function at most $a$. With

$$
J_a=1+\lceil2/a\rceil,
$$

the number of nonempty hidden cells is at most $mJ_a^{N_f}$.

To verify (15), first consider the continuous-parameter version of any word (18), with $n\le p$. The semigroup estimate

$$
\|S_0(t)-S_0(t')\|_\infty\le M_0|t-t'|
$$

and (14), followed by telescoping a product of contractions, show that replacing its parameters by grid points changes the word by at most

$$
(n+1)M_0\delta_t+n(L_V/B)\delta_h\le a.
$$

Because both $E$ and $I$ have norm one, its projection error is therefore at most $3a$.

Expand $U_h(s,t)S$ in a Dyson series in $V_h$ around $S_0$. Its order-$n$ integrand is $B^n$ times a word (18) with continuous time gaps and fields. The ordered integration simplex has volume $(t-s)^n/n!$, so the sum of the integrand norm bounds through order $p$ is at most $e^z$. The order-zero term is $S_0(t-s)S=e^{-2(t-s)}S$ and is already cell-constant. The tail has norm at most

$$
\sum_{n>p}\frac{z^n}{n!}\le2^{-p}e^{2z}\le\frac\sigma8.
$$

Since $\|I-E\|_\infty\le2$, the complete projection error is at most

$$
3ae^z+2\frac\sigma8
=\frac{5\sigma}{8}\le\sigma.
$$

This proves (15) uniformly over every bounded piecewise-continuous protocol. No bound on its switching frequency or time derivative is used. Equations (16)--(17) now give a cell-model mean error at most $\varepsilon/4$ on horizons at most $T$.

### 9.3. State count and restoration of the model constraints

The new partition still refines the original actuator bins. Its reversible generator can be written $(\bar P-I)/\Delta$ with $\bar P$ the cell average of $P$. Consequently the two-replica construction in Section 6 applies without change. It restores the exact original variance and centering, preserves $|g|\le G$, and adds at most $2HR^2\eta$ mean error. The error budget and reset argument of Section 7 then prove (1), with the alternative explicit count

$$
\boxed{D\le1+2mJ_a^{N_f}.}
\tag{20}
$$

For completeness, let $L_\varepsilon=\log(16/\varepsilon)$ and hold $G,H>0$ fixed. The earlier choices give

$$
T=O_{G,H}(L_\varepsilon),\qquad
\log(\Delta^{-1})=O_{G,H}(L_\varepsilon).
$$

Equations (17)--(19) imply

$$
p=O_{G,H}(L_\varepsilon),\qquad
\log(a^{-1})+\log N_t+\log N_h=O_{G,H}(L_\varepsilon),
\qquad
\log N_f=O_{G,H}(L_\varepsilon^2).
$$

Finally $m=O_{G,H}(\varepsilon^{-1})$ and $\log J_a=O_{G,H}(L_\varepsilon)$, so (20) yields (13), after enlarging a constant depending only on $G,H$. This reduces the sufficient count by controlling a bounded number of field insertions instead of a long internal-update history. It does not close the remaining gap to general-family lower bounds.
