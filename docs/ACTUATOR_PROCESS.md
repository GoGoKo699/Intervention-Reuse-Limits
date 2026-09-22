# The hidden actuator process is the complete path-law invariant

[Repository overview](../README.md) · [Core model](THEORY.md) · [Finite-field theorem](FINITE_FIELD.md)

**Working theorem, 22 September 2026.** For the full original finite-state model, the exact data needed for every controlled visible path law are the stationary path law of the hidden sensitivity process. A two-time correlation suffices at cubic order, but generally not at finite field. This note identifies the complete invariant, gives an exact finite-rank closure when applicable, and records why a fixed number of sensitivity levels alone does not yield the scalar compression theorem.

## 1. The operational equivalence

Keep the original rate rule, a fixed $k>0$, stationary hidden law $\mu$, hidden generator $K$, and bounded sensitivity vector $g$. Let $X_t$ be the autonomous stationary hidden chain with generator $K$, and define

$$
Y_t=g(X_t),\qquad X_0\sim\mu.
$$

This autonomous process is an auxiliary description of hidden kinetics. It is not asserted to continue independently through visits of the physical chain to $A$. Every controlled physical experiment starts from its own zero-field equilibrium.

**Theorem.** Fix any field bound $H>0$. Two models with the same $k$ have identical visible path laws for every piecewise-continuous protocol $h:[0,T]\to[-H,H]$ and every finite $T$ if and only if their stationary processes $Y$ have identical finite-dimensional distributions.

The theorem concerns full visible path distributions. Necessity from equality of single-time controlled means alone is not established. The stationary actuator-process law is a complete invariant of the stated operational equivalence; this is not a claim that its infinitely many word probabilities are a minimal finite parameterization.

### Sufficiency: hidden excursions are killed actuator paths

Write

$$
G(a)=\mathbb E e^{aY_0}.
$$

While the physical chain is at $A$, its exit hazard is $ke^{h(t)}G(h(t))$. Conditional on exiting at time $t$, its initial hidden state has law

$$
\frac{\mu_i e^{h(t)g_i}}{G(h(t))}.
$$

An ensuing hidden excursion follows $K$ and is killed, returning to $A$, at rate $k e^{h(v)(Y_v-1)}$. Its survival and exit-time laws are therefore Feynman--Kac functionals of $Y$, with the entry tilt $e^{h(t)Y_0}/G(h(t))$. Every return to $A$ erases the preceding hidden state. The initial hidden law, conditional on $S(0)=+1$, is $\mu$; the initial probability of either visible state is $1/2$.

These holding-time and excursion laws determine the complete alternating visible path. Equality of the stationary actuator-process laws gives equality of all required tilted excursion functionals, hence all controlled visible path laws. Boundedness and the finite state space justify evaluation of these path functionals from finite-dimensional distributions, for example by bounded time-discretization limits.

### Necessity: short field pulses recover joint Laplace transforms

Conditional on $S(0)=+1$, the probability of no visible jump through time $T$ is

$$
R_h(T)=\mathbb E\exp\left[-k\int_0^T e^{h(t)(Y_t-1)}\,dt\right].
$$

It is determined by the visible path law. Choose distinct times $0\le t_1<\cdots<t_n<T$, short disjoint intervals $I_i=[t_i,t_i+\epsilon_i]$, and amplitudes $a_i\in[-H,H]$. For each subset $S\subseteq\{1,\ldots,n\}$, let $h_S$ equal $a_i$ on the intervals with $i\in S$ and zero elsewhere. Set $V_i(y)=e^{a_i(y-1)}-1$. Inclusion-exclusion gives the exact identity

$$
\sum_{S\subseteq[n]}(-1)^{n-|S|}R_{h_S}(T)
=e^{-kT}\mathbb E\prod_{i=1}^n
\left\{\exp\left[-k\int_{I_i}V_i(Y_t)\,dt\right]-1\right\}.
$$

Divide by $\epsilon_1\cdots\epsilon_n$ and let each interval shrink to its left endpoint. The bounded sensitivity and field imply a common integrable bound. Right continuity of the finite-state process then yields

$$
\lim_{\epsilon_i\downarrow0}
\frac{\sum_S(-1)^{n-|S|}R_{h_S}(T)}{\prod_i\epsilon_i}
=e^{-kT}(-k)^n\mathbb E\prod_{i=1}^n
\bigl(e^{a_i(Y_{t_i}-1)}-1\bigr).
$$

Thus all the mixed products on the right are determined by controlled visible path laws. Summing such products over subsets recovers

$$
\mathbb E\exp\left[\sum_i a_i(Y_{t_i}-1)\right]
=\sum_{S\subseteq[n]}\mathbb E\prod_{i\in S}
\bigl(e^{a_i(Y_{t_i}-1)}-1\bigr).
$$

This is the joint Laplace transform on a neighborhood of zero. Bounded random vectors are determined by this transform: its derivatives give all polynomial moments, and polynomials determine probability measures on a compact box. Hence the finite-dimensional laws of $Y$ agree.

This proof is a noiseless identifiability argument. Shrinking intervals and alternating sums do not supply a stable experimental reconstruction method or a sample-complexity bound.

## 2. Finite sensitivity levels give a word-kernel description

Suppose $g$ takes distinct values $\zeta_1,\ldots,\zeta_m$, and let $P_a$ project onto the hidden states with sensitivity $\zeta_a$. The complete stationary actuator law is equivalently the collection

$$
\mathcal W_{a_0,\ldots,a_n}(t_1,\ldots,t_n)
=\mu P_{a_0}e^{Kt_1}P_{a_1}\cdots e^{Kt_n}P_{a_n}\mathbf1,
\qquad t_i\ge0.
$$

Here $\mu$ is written as a row vector. These are joint probabilities of level observations along the hidden process. All word lengths are allowed. They give an exact description for every controlled visible path law by Section 1.

A fixed number $m$ of actuator levels does not make the $m\times m$ two-time matrix a complete invariant. Repeated level projections can reveal internal directions that a two-time measurement misses. The explicit binary example in Section 4 demonstrates this with $m=2$.

If $K$ is strongly lumpable with respect to the level partition, then the level process itself is an $m$-state Markov chain. Adding $A$ yields an exact $m+1$-state physical description under every field protocol: the rates to $A$ are constant within each level, the aggregate rates from $A$ are $k\mu(P_a)e^{(1+\zeta_a)h}$, and internal block rates are those of the lumped $K$. This is a sufficient structural condition, not an assertion that every finite-level process is Markov.

## 3. A finite-rank actuator gives a matrix-return closure

There is a different sufficient restriction. Suppose all but $q$ distinguished hidden states share a baseline sensitivity $g_0$. Write $S$ for those $q$ states, $\mu_S$ for their stationary masses, and

$$
P_{SS}(t)=(e^{Kt})_{S,S}.
$$

This $q\times q$ return kernel, together with $\mu_S$, the sensitivities, and $k$, determines the exact controlled visible path laws. The number $q$ counts distinguished states, not merely distinct sensitivity values.

For the exact mean, let $a=p_A$, let $x$ be the row vector of hidden probabilities, let $z=x_S$, and define

$$
\kappa(t)=k e^{(g_0-1)h(t)},\qquad
I(t)=k a(t)e^{(g_0+1)h(t)},
$$

$$
J_i(t)=k\bigl(e^{g_i h(t)}-e^{g_0h(t)}\bigr)
\bigl[a(t)\mu_i e^{h(t)}-x_i(t)e^{-h(t)}\bigr],\qquad i\in S,
$$

$$
E(t,r)=\exp\left[-\int_r^t\kappa(v)\,dv\right].
$$

The full hidden equation and its closed return equations are

$$
\dot x=xK-\kappa x+I\mu+\sum_{i\in S}J_i e_i,
$$

$$
b(t)=\frac{E(t,0)}2+\int_0^tE(t,r)[I(r)+J(r)\mathbf1]dr,
\qquad a=1-b,
$$

$$
z(t)=\frac{E(t,0)}2\mu_S+
\int_0^tE(t,r)[I(r)\mu_S+J(r)P_{SS}(t-r)]dr.
$$

They determine the mean $m=2b-1$. Uniqueness follows from bounded-coefficient Volterra iteration on each finite interval.

For a single hidden excursion, the same equations omit reinjection from $A$ and allow an initial row vector in the span of $\mu$ and the distinguished unit vectors. The actual field-tilted entrance law lies in precisely that span. Thus $P_{SS}$ determines excursion survival and exit distributions, and consequently the full visible path law. Equivalently, every nonbaseline perturbation of the killed hidden generator has rank at most $q$.

When $q=1$, the matrix kernel is scalar and the canonical subclass in the [finite-field theorem](FINITE_FIELD.md) is recovered. For larger fixed $q$, the equations give exact closure, but this note does not prove a dimension-independent constructive Markov compression theorem. Although reversible matrix-return kernels have positive-semidefinite spectral measures, generic matrix quadrature or block-Jacobi realization need not produce a generator with nonnegative off-diagonal entries. That positivity and physical-realization step requires a separate argument. A finite number of actuator levels alone does not even bound $q$.

## 4. Two levels and identical two-time kernels can still differ at finite field

Take $k=1$, four hidden states with uniform $\mu$, and

$$
g=(1,1,-1,-1)^T,\qquad W=1.
$$

Let $\mathbf1=(1,1,1,1)^T$, $w_+=(1,-1,0,0)^T$, $w_-=(0,0,1,-1)^T$, and define

$$
K_\pm=-\left(I-\frac{\mathbf1\mathbf1^T}{4}\right)
+\frac18(gw_\pm^T+w_\pm g^T).
$$

Explicitly,

$$
K_+=\begin{pmatrix}
-1/2&1/4&1/8&1/8\\
1/4&-1&3/8&3/8\\
1/8&3/8&-3/4&1/4\\
1/8&3/8&1/4&-3/4
\end{pmatrix},\qquad
K_-=\begin{pmatrix}
-3/4&1/4&3/8&1/8\\
1/4&-3/4&3/8&1/8\\
3/8&3/8&-1&1/4\\
1/8&1/8&1/4&-1/2
\end{pmatrix}.
$$

Both are irreducible symmetric Markov generators. On the span of $g,w_\pm$,

$$
K_\pm g=-g+\frac12w_\pm,\qquad
K_\pm w_\pm=-w_\pm+\frac14g.
$$

Consequently they have the same scalar kernel

$$
C(t)=\langle g,e^{K_\pm t}g\rangle_\mu
=e^{-t}\cosh\left(\frac{t}{2\sqrt2}\right).
$$

Because $Y$ is binary with balanced stationary probabilities, this fixes every two-time level probability:

$$
\Pr(Y_0=a,Y_t=b)=\frac{1+ab\,C(t)}4,
\qquad a,b\in\{-1,1\}.
$$

Nevertheless, their exact means under a constant nonzero field differ. Starting both full five-state models from the same zero-field equilibrium,

$$
\boxed{
\left.\frac{d^5}{dt^5}(m_+[h](t)-m_-[h](t))\right|_{t=0}
=\frac12e^{-2h}\sinh^4h
=\frac{(e^{2h}-1)^4}{32e^{6h}}>0.
}
$$

Their first four time derivatives agree. The displayed fifth derivative is a derivative in **time**; its small-field expansion starts at order $h^4$.

**Derivation.** Write the full generator as $Q_\pm=M+\overline K_\pm$, where $M$ contains only the $A$--hidden transitions. The common initial law is $p_0=(1/2,1/8,1/8,1/8,1/8)$ and the readout is $f=(-1,1,1,1,1)^T$. We have $p_0\overline K_\pm=0$ and $\overline K_\pm f=0$. Pure powers of $M$ preserve vectors that are constant on the two sensitivity levels. Thus all words in $p_0Q_\pm^nf$ for $n\le4$, and all but one word for $n=5$, depend on $K$ only through the common numbers $\langle g,K^jg\rangle_\mu$. The exceptional word is

$$
p_0M\overline K_\pm M\overline K_\pm Mf.
$$

The hidden part of $p_0M$ is $\mu_i e^{hg_i}\sinh h$, and the hidden part of $Mf$ is $-2e^{-h}e^{hg_i}$. The middle hidden block of $M$ is $-e^{-h}\operatorname{diag}(e^{hg})$. Since $e^{hg}=\cosh h+g\sinh h$, the difference of the exceptional words is

$$
2e^{-2h}\sinh^4h\,
\left[\langle K_+g,g K_+g\rangle_\mu
-\langle K_-g,g K_-g\rangle_\mu\right].
$$

The bracket equals $1/4$: using $K_\pm g=-g+w_\pm/2$, its two terms are $+1/8$ and $-1/8$. This proves the formula. It also locates the missing information in a word with two hidden propagations separated by an actuator multiplication, rather than in the two-time kernel.

The example does not contradict the canonical scalar theorem: here each sensitivity level contains two states, so the nonbaseline actuator perturbation has rank two, not one.
