# Polynomial reversible compression from bounded conductance density

[Repository overview](../README.md) · [Bounded-rate finite-alphabet bounds](BOUNDED_RATE_FINITE_FIELD.md) · [General reversible compression](REVERSIBLE_GENERAL_COMPRESSION.md) · [Polynomial controlled lower bound](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md)

**Research theorem, 22 September 2026.** A finite actuator alphabet and a uniform bound on the internal conductance density permit a polynomial-size **reversible** predictor of the actual controlled mean. The construction samples microscopic vertices separately within each actuator level, assigns them exact stationary weights, and connects them by symmetric sampled conductances. It preserves the complete actuator histogram and ordinary detailed balance.

The conductance-density assumption is stronger than a spectral rate cap. Consequently this result does not settle polynomial reversible compression for the full bounded-spectrum binary class. It gives a positive construction in an additional structural subclass; the original spectral band need not be preserved. Stratified sampling, concentration, and reversible weighted graphs are established tools. Their application here is an internal derivation, not a certification of originality.

## 1. The theorem and its explicit state bound

Fix $k,L,G,H>0$ and an integer $m\ge2$. Consider any target in the original family with an irreducible internal generator $K$, reversible stationary law $\mu$, and centered sensitivity $g$ taking exactly $m$ positive-mass values $z_1,\ldots,z_m\in[-G,G]$. Write

$$
\rho_a=\mu(g=z_a)>0,\qquad
W=\langle g^2,1\rangle_\mu.
$$

Assume the off-diagonal conductance-density bound

$$
\boxed{\frac{K_{xy}}{\mu_y}\le Lk\qquad(x\ne y).}
\tag{1}
$$

The density $K_{xy}/\mu_y$ is symmetric in $x,y$ by reversibility. There is no lower bound on an individual microscopic mass $\mu_x$ or actuator-level mass $\rho_a$.

Use the original external rates

$$
q_{AB_x}(h)=k\mu_xe^{(1+g_x)h},\qquad
q_{B_xA}(h)=ke^{(g_x-1)h},
$$

and zero-field equilibrium preparation. Set

$$
R=e^{(1+G)H},\qquad A_H=e^{2GH},\qquad C_R=1+2R^2,
$$

$$
q_L=\frac{LR}{1+LR},\qquad
\beta=-\log q_L=\log\left(1+\frac1{LR}\right),\qquad
p_L=\frac{\log m}{\beta}.
\tag{2}
$$

For $0<\delta<1$, choose

$$
\ell=\max\left\{1,
\left\lceil\frac{\log(2C_R/\delta)}{\beta}\right\rceil-1
\right\},\qquad
\eta=\frac{\delta}{C_RA_Hm^{\ell+1}(2\ell+1)},
\tag{3}
$$

$$
V_\ell=\sum_{r=1}^{\ell+1}m^r,\qquad
n=\left\lceil256\eta^{-2}\log\left(\frac{16mV_\ell}{\eta}\right)\right\rceil.
\tag{4}
$$

There exists a surrogate in the original reversible family with at most $D=1+mn$ total physical states such that

$$
\boxed{
\sup_{T>0}\sup_{|h|\le H}\sup_{0\le t\le T}
|m_F[h](t)-m_{\widehat F}[h](t)|\le\delta.
}
\tag{5}
$$

Protocols are deterministic and piecewise continuous. The surrogate has a fixed binary readout, fixed zero-field equilibrium preparation, and the same instantaneous-field rate rule. It preserves the exact sensitivity values and their masses $(z_a,\rho_a)$, and therefore the centering, variance $W$, sensitivity bound, passive telegraph path law, equilibrium curve, reference linear mean response, and zero quadratic mean response.

Its internal generator is irreducible and ordinarily reversible. Every internal outgoing rate is at most $Lk$, and every internal relaxation rate is at most $2Lk$. Preservation of the target's original spectral-band endpoints is **not** claimed.

The explicit bound implies, with a constant depending only on the displayed fixed parameters,

$$
\boxed{
D\le C_{m,L,G,H}\,
\delta^{-2(1+p_L)}\log^3(2/\delta).
}
\tag{6}
$$

The construction knows the full target. It is a probabilistic existence proof with a quantified success event, not a procedure for learning an unknown generator from visible records. Repeated sampled vertices count as distinct physical states. If the centered actuator has only one value, it is identically zero and the ordinary two-state model is exact. Targets with at most a prescribed number of levels can be treated with their actual number of positive-mass levels.

## 2. A reversible graph on stratified sampled vertices

Rescale time so that $k=1$. Define

$$
q(x,y)=\begin{cases}K_{xy}/\mu_y,&x\ne y,\\0,&x=y.\end{cases}
$$

Then $q(x,y)=q(y,x)$ and $0\le q\le L$. For every function $u$,

$$
(Ku)(x)=\sum_y\mu_yq(x,y)[u(y)-u(x)].
\tag{7}
$$

In particular every target outgoing rate is at most $L$, so

$$
P=I+K/L
\tag{8}
$$

is an exact stochastic uniformization matrix.

For each actuator level $a$, draw $n$ independent microscopic states from $\mu$ conditioned on $g=z_a$. All draws in all strata are independent. Write the resulting $mn$ sampled vertices as $X_i$, and assign a vertex in stratum $a$ weight and sensitivity

$$
\omega_i=\rho_a/n,\qquad \gamma_i=z_a.
\tag{9}
$$

Repeated samples remain distinct replicas. For distinct replica vertices $i,j$, put

$$
\overline K_{ij}=\omega_jq(X_i,X_j),
$$

and choose the diagonal for zero row sums. Symmetry of $q$ gives

$$
\omega_i\overline K_{ij}=\omega_j\overline K_{ji}.
$$

Thus $\overline K$ is reversible under $\omega$. Its outgoing rates are at most $L$, since $q\le L$ and $\sum_j\omega_j=1$. Consequently

$$
\overline P=I+\overline K/L
$$

is stochastic. When two replicas represent the same microscopic state, the density value $q(x,x)=0$ correctly gives no transition contribution between them in (7).

The sampled graph might be disconnected. For $0<\eta\le1/2$, let $\Pi_\omega$ have every row equal to $\omega$, and define

$$
P^*=(1-\eta)\overline P+\eta\Pi_\omega,
\qquad K^*=L(P^*-I).
\tag{10}
$$

Every entry of $P^*$ is positive. Hence $K^*$ is irreducible and reversible under $\omega$, with outgoing rates still at most $L$. A reversible stochastic matrix has spectrum in $[-1,1]$, so the spectrum of $-K^*$ lies in $[0,2L]$. The small reset in (10) is part of the surrogate generator; its approximation cost is included below. It should be distinguished from the common external reset used later only to analyze the coupling.

The stationary actuator histogram is exactly the target's before and after (10): each stratum has total weight $\rho_a$ for every realization of the sampling.

## 3. One-step consistency and the sampled-row bias

Let $u$ be a deterministic target function with values in $[0,1]$, and write $u^X_i=u(X_i)$. At a sampled row $i$, equations (7)--(8) give

$$
(\overline P u^X)_i-(Pu)(X_i)
=\sum_j\omega_jF_{X_i,u}(X_j)-\mathbb E_\mu F_{X_i,u},
\tag{11}
$$

where

$$
F_{x,u}(y)=\frac{q(x,y)}L[u(y)-u(x)]\in[-1,1].
$$

Condition on $X_i=x$ in stratum $a$. The $j=i$ summand in (11) is exactly zero. All remaining summands are independent. Their conditional expectation differs from $\mathbb E_\mu F_{x,u}$ by at most $\omega_i\le1/n$: precisely one draw from stratum $a$ has been removed, and its expected contribution has magnitude at most $\rho_a/n$. Also

$$
\sum_j\omega_j^2=\frac1n\sum_a\rho_a^2\le\frac1n.
$$

Weighted Hoeffding therefore yields, for $n\ge2/\eta$,

$$
\Pr\left\{|(\overline P u^X)_i-(Pu)(X_i)|>\eta\right\}
\le2e^{-n\eta^2/8}.
\tag{12}
$$

Indeed the bias is at most $\eta/2$, and each independent centered summand has range length at most $2\omega_j$. The resulting tail bound at threshold $\eta/2$ is $2\exp[-n\eta^2/8]$. The conditional bound is uniform in $x$ and can be integrated over $X_i$.

For any finite deterministic family $\mathcal U$ of such functions, a union bound over all rows and functions gives failure probability at most

$$
2mn|\mathcal U|e^{-n\eta^2/8}.
\tag{13}
$$

On the good event, adding (10) changes the value of any $[0,1]$-valued function by at most $\eta$. Therefore

$$
\max_i|(P^*u^X)_i-(Pu)(X_i)|\le2\eta,
\qquad u\in\mathcal U.
\tag{14}
$$

Separately, for any deterministic target function $v\in[0,1]$, the stratified empirical average has expectation $\mathbb E_\mu v$. A second weighted Hoeffding bound gives

$$
\Pr\left\{\left|\sum_i\omega_iv(X_i)-\mathbb E_\mu v\right|>\eta\right\}
\le2e^{-2n\eta^2}.
\tag{15}
$$

These estimates do not assume a lower bound on any microscopic or stratum mass. They apply to deterministic functions of the supplied target; the functions tested below do not depend on the sampled graph.

## 4. A finite family controls the required prefix law

Let $D_a$ multiply by $\mathbf1\{g=z_a\}$. For a word $w=(a_1,\ldots,a_r)$, define the target prediction function

$$
f_\varnothing=1,\qquad
f_w=PD_{a_1}PD_{a_2}\cdots PD_{a_r}1.
\tag{16}
$$

All these functions take values in $[0,1]$. For a fixed $\ell\ge1$, apply (13) to

$$
\mathcal U=\{D_af_w:|w|\le\ell-1\},
$$

and (15) to

$$
\mathcal V=\{D_af_w:|w|\le\ell\}.
$$

Both families have at most $V_\ell=\sum_{r=1}^{\ell+1}m^r$ elements. The probability that any required estimate fails is at most

$$
2mnV_\ell e^{-n\eta^2/8}+2V_\ell e^{-2n\eta^2}.
\tag{17}
$$

The explicit sample size (4) makes this quantity strictly less than one, so a good realization exists. Here is a direct check including its logarithmic dependence on $n$. Put

$$
B=\log(16mV_\ell/\eta).
$$

For $m\ge2$, $\ell\ge1$, and $\eta\le1/2$, one has $B>1$, $n\ge2/\eta$, and $n\le512\eta^{-2}B$. Since $mV_\ell=\eta e^B/16$, the first prefactor in (17) is at most

$$
64\eta^{-1}Be^B\le e^{5B},
$$

where $\eta^{-1}\le e^B$, $B\le e^B$, and $64\le e^{2B}$. Its exponential factor is at most $e^{-32B}$. The second term is at most $e^{-511B}$. Thus the success probability is at least

$$
1-e^{-27B}-e^{-511B}>0.
\tag{18}
$$

Choose any good realization. Let $f_w^*$ be the corresponding prediction function for $P^*$ on the sampled vertices. Because the actuator labels agree exactly, stochastic contraction and induction using (14) give

$$
\max_i|f_w^*(i)-f_w(X_i)|\le2|w|\eta,
\qquad |w|\le\ell.
\tag{19}
$$

For the induction step, insert and subtract $P^*(D_af_w)^X$. One difference is bounded by the shorter-word error because $P^*$ is stochastic; the other is (14) for the deterministic target function $D_af_w$.

A stationary word $(a_0,\ldots,a_\ell)$ has target probability

$$
\mathbb E_\mu[D_{a_0}f_{(a_1,\ldots,a_\ell)}].
$$

Its sampled-model probability replaces $\mu,f$ with $\omega,f^*$. Equation (19) contributes at most $2\ell\eta$ and the empirical-average bound contributes at most $\eta$. Thus every word probability differs by at most $(2\ell+1)\eta$. The total variation distance of the stationary prefix laws through length $\ell+1$ is consequently at most

$$
\boxed{\theta=\frac12m^{\ell+1}(2\ell+1)\eta.}
\tag{20}
$$

The one-symbol law agrees exactly, not approximately, by (9).

## 5. From prefixes to uniform controlled-mean error

Use the common internal update clock of rate $L$ for the target and sampled model. The external escape rate from $A$ is the same in both models because their actuator histograms coincide, and is at most $R$. Every hidden-to-$A$ rate is at least $\alpha=1/R$.

At an entry into $B$, the hidden stationary law is tilted by $e^{h z_0}$, where $z_0$ is the first actuator symbol of the visit. The normalization is the same in both models because their one-symbol marginals agree. Therefore tilting the two prefix laws multiplies their total variation distance by at most

$$
\frac{\max_z e^{hz}}{\mathbb E_\rho e^{hz}}\le e^{2GH}=A_H.
$$

Their tilted prefixes can be coupled with failure probability at most $A_H\theta$. The initial hidden visit has the untilted prefix law and failure probability at most $\theta$.

For completeness, the regenerative estimate from [the bounded-rate proof, Section 7](BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) is

$$
\boxed{
\sup_{h,t}|m_F[h](t)-m_{\widehat F}[h](t)|
\le C_R\left(A_H\theta+q_L^{\ell+1}\right).
}
\tag{21}
$$

To see its two contributions, represent the external generator using a common rate-$\alpha$ Poisson reset sending every state to $A$, plus a residual Markov generator. Couple each new hidden visit's prefix and its rate-$L$ update clock. Declare a failure if the prefix coupling fails or if the visit uses more than $\ell$ updates; a common external reset removes its effect. The initial probability of a hidden visit is $1/2$, and entry intensity is at most $R$. Immediate prefix failures therefore contribute at most

$$
\left(\frac12+\frac R\alpha\right)A_H\theta
$$

to the probability of a disagreement at any observation time. If $\tau_{\ell+1}$ is the time of the $(\ell+1)$st internal update, independence of the update and reset clocks gives

$$
\mathbb E e^{-\alpha\tau_{\ell+1}}
=\left(\frac L{L+\alpha}\right)^{\ell+1}
=q_L^{\ell+1}.
$$

The same initial-visit and entry-intensity calculation bounds the exhaustion contribution by $(1/2+R/\alpha)q_L^{\ell+1}$. Multiplying total disagreement probability by two for the binary readout gives (21), since $2(1/2+R/\alpha)=1+2R^2=C_R$. Conditioning at the entry stopping times and using independent future increments justifies the entry-intensity calculation; counting potential causes after an earlier failure only overcounts the event.

This coupling bounds the visible state at each observation time uniformly over horizons. It does not bound total variation of entire histories uniformly over unbounded time. The additional small **internal** reset in (10) has already been charged through (14)--(20); the common **external** reset here changes neither model.

With the choices (3), the prefix term in (21) is exactly $\delta/2$ and the exhaustion term is at most $\delta/2$. This proves (5). Restoring $k$ gives the internal outgoing bound $Lk$ and relaxation-rate cap $2Lk$.

## 6. State count and exact physical constraints

At fixed $m,L,G,H$,

$$
\ell=O(\log(2/\delta)),\qquad
m^{\ell+1}=O(\delta^{-p_L}),\qquad
V_\ell=O(m^{\ell+1}).
$$

Hence (3) implies $\eta^{-2}=O(\delta^{-2(1+p_L)}\log^2(2/\delta))$, and the logarithm in (4) contributes one further factor $O(\log(2/\delta))$. This proves (6) for the total count $1+mn$ after attaching the visible state $A$.

The sampled hidden state $i$ has sensitivity $\gamma_i$ and stationary weight $\omega_i$. Attach it using

$$
q_{Ai}(h)=k\omega_i e^{(1+\gamma_i)h},\qquad
q_{iA}(h)=ke^{(\gamma_i-1)h}.
$$

The full stationary law is

$$
\widehat\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\widehat\pi_h(i)=\frac{\omega_i e^h}{2\cosh h}.
$$

Every internal edge and every external edge satisfies detailed balance under this law. The exact actuator histogram, passive telegraph law, equilibrium curve, reference linear mean and zero quadratic mean follow from the original centered-sensitivity construction. The observation begins from $\widehat\pi_0$, as required.

## 7. Scope of the improvement

The construction avoids a partition that resolves every microscopic conditional prediction profile. It also avoids assuming that a projected operator automatically has positive transition rates: positivity and ordinary reversibility are present in the sampled edge formula itself. Exact stratum weights retain the actuator histogram despite arbitrarily small individual stationary masses.

A spectral cap alone does not imply (1). For example, the existing uniform-law shift-register targets have a fixed spectral band but some shift-edge rates bounded below independently of register size. Dividing those rates by a stationary mass inversely proportional to the number of hidden states makes their conductance density unbounded. Thus the main question of polynomial reversible prediction under only bounded binary sensitivity and a spectral cap remains open.

No matched polynomial exponent, preservation of the original spectral band, polynomial runtime, parameter-precision bound, or statistical learning guarantee is established here. The theorem permits general finite-alphabet actuator geometry under a separate structural condition on the internal conductances. It does not assert that this subclass contains every rank-one target.
