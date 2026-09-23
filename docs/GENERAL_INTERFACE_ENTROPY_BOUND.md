# Entropy-production comparison for a general kinetic interface

[Original-interface theorem](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) · [General kinetic prediction class](GENERAL_KINETIC_INTERFACE.md) · [State–entropy-production tradeoff](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) · [Generalized-reversal boundary](GENERALIZED_REVERSAL_PREDICTION.md)

**Research theorem, 23 September 2026.** The uniform same-state entropy-production comparison does not require exponential field rates. It holds for arbitrary control-dependent return rates bounded below and arbitrary entrance rates dominated by the hidden stationary law. A common local-balance ratio is needed to interpret the comparator as a fully reversible model at each fixed control; it is not needed for the endpoint-distance estimate itself.

Only ordinary time reversal, which fixes every state label, is used below. The distinction from generalized reversals of odd variables remains essential.

## 1. Broad hub interface and exact statement

Let $K$ be a finite hidden generator with strictly positive stationary probability law $\mu$. Its arithmetic reversibilization is

$$
L=(K+K^*)/2,\qquad K^*_{ij}=\mu_jK_{ji}/\mu_i\ (i\ne j),
\qquad K^*_{ii}=K_{ii}.
\tag{1}
$$

Add one visible hub $A$. For a deterministic control $u(t)$, use identical external rates in the two models:

$$
q_{iA}(u)=b_i(u),\qquad q_{Ai}(u)=\mu_i c_i(u).
\tag{2}
$$

Assume the allowed controls obey the uniform, dimensionful bounds

$$
b_i(u)\ge\alpha>0,\qquad 0\le c_i(u)\le\beta<\infty.
\tag{3}
$$

The rates along any selected protocol are assumed locally bounded in time so the finite-state processes are well-defined. No common upper bound on the return rates is used in the estimate. Both models start from the same distribution $p(0)$, with

$$
p_i(0)\le c_0\mu_i\quad\text{on hidden states}.
\tag{4}
$$

The initial distribution need not be stationary. Let $p_K(T),p_L(T)$ denote the full endpoint laws. Define

$$
\begin{aligned}
d_i&=\sum_{j\ne i}
\left[K_{ij}\log\frac{K_{ij}}{L_{ij}}-K_{ij}+L_{ij}\right],
&d&=\sum_i\mu_i d_i,\\
\sigma_{\rm hid}&=\sum_{i\ne j}\mu_iK_{ij}
\log\frac{\mu_iK_{ij}}{\mu_jK_{ji}}.
\end{aligned}
\tag{5}
$$

Use the standard zero conventions and natural logarithms. Arithmetic reversibilization preserves every hidden exit and satisfies $0\le d\le\sigma_{\rm hid}/4$, as proved in the [original-interface note](ENTROPY_PRODUCTION_REVERSIBILIZATION.md#2-arithmetic-reversibilization-and-the-local-path-cost). This identity involves only the hidden generator and is unchanged by (2).

For completeness, stationarity gives $\sum_{j\ne i}K^*_{ij}=\sum_{j\ne i}K_{ij}$. On one unordered hidden pair, write $a=\mu_iK_{ij}$ and $b=\mu_jK_{ji}$. The contributions to $d$ and $\sigma_{\rm hid}$ are respectively

$$
d_{\{i,j\}}=a\log\frac{2a}{a+b}+b\log\frac{2b}{a+b},
\qquad
\sigma_{\{i,j\}}=(a-b)\log(a/b).
$$

For $a,b>0$, set $t=(a-b)/(a+b)$. The inequality $4d_{\{i,j\}}\le\sigma_{\{i,j\}}$ is equivalent to $F(t)\ge0$, where

$$
F(t)=t\log\frac{1+t}{1-t}
-2\bigl[(1+t)\log(1+t)+(1-t)\log(1-t)\bigr].
$$

It follows from $F(0)=F'(0)=0$ and $F''(t)=4t^2/(1-t^2)^2\ge0$. Zero-flux cases follow by limits. Summing unordered pairs proves the stated factor $1/4$.

For $c,A_0\ge0$, put

$$
\Psi(c,A_0)=
\begin{cases}
A_0,&c\le A_0,\\
A_0+(c-A_0)\exp[-c/(c-A_0)],&c>A_0.
\end{cases}
\tag{6}
$$

**Theorem.** Uniformly over the allowed protocols and all horizons,

$$
\boxed{
D(p_K(T)\|p_L(T))
\le\frac d\alpha\Psi(c_0,\beta/\alpha)
\le\frac{\sigma_{\rm hid}}{4\alpha}\Psi(c_0,\beta/\alpha).}
\tag{7}
$$

For any common readout $S\in[-1,1]$,

$$
\boxed{
|\mathbb E_K S(T)-\mathbb E_L S(T)|
\le\min\left\{2,
\sqrt{\frac{\sigma_{\rm hid}}{2\alpha}
\Psi(c_0,\beta/\alpha)}\right\}.}
\tag{8}
$$

In the frequent case $c_0\le\beta/\alpha$, these simplify to

$$
D(p_K\|p_L)\le\frac{\beta d}{\alpha^2},\qquad
|\mathbb E_K S-\mathbb E_L S|
\le\sqrt{\frac{\beta\sigma_{\rm hid}}{2\alpha^2}}.
\tag{9}
$$

The state space, stationary hidden law, labels and hidden exit rates are unchanged. The comparison is independent of hidden rates, state count and minimum stationary mass. It is an endpoint statement, not a uniform comparison of complete long-time path laws.

## 2. Proof by the last common reset

The lower return bound permits the exact generator decomposition

$$
Q_u=Q_u^{\rm res}+\alpha(\Pi_A-I),
\tag{10}
$$

where every row of $\Pi_A$ equals $e_A^{\mathsf T}$. The residual hidden-to-hub rates are $b_i(u)-\alpha\ge0$. This is realized by an independent rate-$\alpha$ Poisson clock which resets the current state to $A$, including a no-op if it is already there.

Between resets, let $r_i=p_i/\mu_i$ for the residual $K$ process. Its hidden forward equation is

$$
\dot r_i=(K^*r)_i-[b_i(u)-\alpha]r_i+p_Ac_i(u).
$$

The maximum principle, $p_A\le1$ and (3) imply

$$
\max_i r_i(t)\le c+\beta t
\tag{11}
$$

when the segment starts with hidden density at most $c$. A segment after a reset has $c=0$; the initial no-reset segment has $c=c_0$.

Only the hidden edges differ between the two residual models. Their path-relative-entropy cost over a segment of length $\tau$ is therefore at most

$$
\int_0^\tau\sum_i p_i(t)d_i\,dt
\le d\left(c\tau+\frac{\beta\tau^2}{2}\right).
\tag{12}
$$

Both models have exactly the same reset-clock law. At horizon $T$, no reset occurs with probability $e^{-\alpha T}$; otherwise the age of the last reset has density $\alpha e^{-\alpha\tau}$ on $[0,T)$. Relative entropy contracts under marginalization, so averaging conditional path costs bounds the endpoint entropy. With $x=\alpha T$ and $A_0=\beta/\alpha$ this gives

$$
\begin{aligned}
D(p_K(T)\|p_L(T))
&\le d\left[\frac{\beta}{\alpha^2}
\bigl(1-(1+x)e^{-x}\bigr)+c_0Te^{-x}\right]\\
&=\frac d\alpha
\left[A_0+\bigl((c_0-A_0)x-A_0\bigr)e^{-x}\right].
\end{aligned}
\tag{13}
$$

The derivative of the bracket is $[c_0-(c_0-A_0)x]e^{-x}$. If $c_0\le A_0$, the bracket increases to $A_0$. If $c_0>A_0$, its maximum occurs at $x=c_0/(c_0-A_0)$ and equals (6). This proves (7). Pinsker's inequality and the readout range prove (8). The constant $\Psi$ is the exact maximum of the bound (13); no optimality over all possible interfaces is asserted.

## 3. When the full comparison model is reversible

The endpoint estimate required no relation between $b_i$ and $c_i$. To retain the original equilibrium meaning, impose the additional condition

$$
\frac{c_i(u)}{b_i(u)}=r(u)>0
\quad\text{for every hidden state }i.
\tag{14}
$$

Then the full model has stationary law

$$
\pi_u(A)=\frac1{1+r(u)},\qquad
\pi_u(i)=\frac{r(u)}{1+r(u)}\mu_i.
\tag{15}
$$

This law is stationary even for nonreversible $K$, because $\mu K=0$ and the external edges balance individually. Replacing $K$ by $L$ makes the whole fixed-control generator reversible under (15).

Conversely, (14) is necessary for the external edges to obey detailed balance with a stationary law whose conditional hidden distribution is $\mu$. Without it, a reversible hidden $L$ need not produce a reversible full model: the external interface itself can drive cycles. Thus (7) remains a valid comparison in that broader class, but it cannot automatically be described as a comparison with a fully equilibrium predictor.

Choose a baseline control $u_0$ and its stationary preparation (15). Write

$$
p_0=\frac{r(u_0)}{1+r(u_0)}.
$$

Then $c_0=p_0$. Since $\beta\ge r(u_0)\alpha$, one has $p_0\le\beta/\alpha$ and the simple bound (9) applies. The full stationary entropy-production rate at baseline is

$$
\sigma_0=p_0\sigma_{\rm hid},
$$

because the external edges contribute zero and the hidden stationary mass is $p_0$. Therefore

$$
\boxed{
|\mathbb E_K S-\mathbb E_L S|
\le\sqrt{\frac{\beta\sigma_0}{2\alpha^2p_0}}.}
\tag{16}
$$

The common ratio may be any positive function of a multidimensional control. The state-dependent kinetic factors may be arbitrary subject to (3). No exponential sensitivity formula is needed for this entropy comparison.

## 4. Dimensionless kinetic bounds and the passive two-state baseline

A useful physical specialization is

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),\qquad b_i(0)=1.
\tag{17}
$$

Suppose over the allowed controls

$$
b_i(h)\ge\underline b>0,\qquad
e^{2h}b_i(h)\le\overline c<\infty.
\tag{18}
$$

Here $\alpha=k\underline b$, $\beta=k\overline c$, $p_0=1/2$, and

$$
\boxed{
\sup_{h,T}|m_K[h,T]-m_L[h,T]|
\le\sqrt{\frac{\overline c}{\underline b^2}
\frac{\sigma_0}{k}}.}
\tag{19}
$$

If zero control belongs to the allowed set, (17) ensures $\overline c\ge1$ and $\underline b\le1$, so the condition for the simple bound is automatic. At zero control, every hidden state exits to $A$ at rate $k$ and $A$ enters the hidden block at total rate $k$; the passive visible law is exactly the two-state telegraph law, independently of $K$.

The original exponential rule is the special case $b_i(h)=e^{(g_i-1)h}$, with $\underline b=1/R$ and $\overline c=R$. Equation (19) then becomes $R^{3/2}\sqrt{\sigma_0/k}$, exactly the original-interface bound. Bounds only on a two-field menu suffice when the observation class is restricted to those two fields; an all-protocol statement requires (18) throughout its full control set.

## 5. Finite-entropy-production regularization on the same states

Suppose additionally that the hidden exit cap is $Bk$. For $0<\varepsilon<1/2$, define

$$
K_\varepsilon=(1-\varepsilon)K+\varepsilon K^*.
$$

It preserves $\mu$ and every hidden exit. As in the original-interface proof,

$$
\sigma_{\rm hid}(K_\varepsilon)
\le Bk\log\frac{1-\varepsilon}{\varepsilon}.
\tag{20}
$$

At a common hidden state, the maximal-coupling disagreement rate is at most $\varepsilon Bk$. The shared reset clock repairs every disagreement, and its truncated mean age is at most $1/\alpha$. Hence

$$
\boxed{
\sup_{u,T}|m_{K_\varepsilon}-m_K|
\le\frac{2\varepsilon Bk}{\alpha}
=\frac{2B\varepsilon}{\underline b}.}
\tag{21}
$$

The last equality uses the dimensionless convention (18). No upper injection bound is needed for this coupling estimate. A predictor already accurate to $\delta/2$ can use

$$
\varepsilon=\min\left\{1/4,\frac{\delta\alpha}{4Bk}\right\}
\tag{22}
$$

to remain accurate to $\delta$ without adding states. For sufficiently small $\delta$, the hidden entropy-production upper is $Bk\log(4Bk/(\delta\alpha))$. Under the stationary baseline (15), multiply this by $p_0$ for the full baseline rate. If $B=0$, the original hidden generator already has zero entropy production and needs no regularization.

## 6. What extends to a distributed reset

The hub can be replaced by a shared, state-independent reset law, but a reset alone does not establish every required occupation bound. The following sufficient version separates the two ingredients.

Suppose both models admit an independent rate-$\alpha$ Poisson reset to the same possibly control-dependent law $\nu_t$. Assume the residual models differ only through the hidden $K$ versus $L$ block, with the same local relative-entropy cost bound $\sum_i p_i d_i$. Suppose residual segments beginning after any reset obey

$$
p_i(t)/\mu_i\le c_{\rm reset}+\beta t,
$$

and the initial segment obeys $p_i(t)/\mu_i\le c_0+\beta t$. Repeating the conditional-path argument gives

$$
D(p_K(T)\|p_L(T))
\le\frac d\alpha\,
\Psi\!\left(c_0,c_{\rm reset}+\frac\beta\alpha\right).
\tag{23}
$$

Indeed the averaged path cost is

$$
d\left[c_{\rm reset}\mathbb E\min\{E,T\}
+\frac\beta2\mathbb E\min\{E,T\}^2
+(c_0-c_{\rm reset})Te^{-\alpha T}\right],
$$

where $E$ is exponential with rate $\alpha$. This reduces to the same bracket as (13), with $A_0=c_{\rm reset}+\beta/\alpha$.

A concrete realization is a finite visible sector with reset law supported on that sector. If its common external mechanism supplies the reset component, every hidden state has residual nonnegative killing, and entrance from each visible state is bounded by $\beta\mu_i$, the maximum principle proves the required bounds with $c_{\rm reset}=0$. The reset distribution may then depend on the deterministic control. Every visible and hidden state is still counted.

For resets that also redraw hidden states, bounded density of $\nu_t$ alone is not enough: the stated residual occupation bound and path-cost comparison must also be proved. In particular, one cannot subtract reset rates from the differing hidden edges and silently retain their old path-relative-entropy cost. Full reversibility of the comparator additionally requires compatibility of the whole common interface with its proposed equilibrium law. Equation (23) is a sufficient regenerative comparison principle, not a classification of every admissible kinetic interface.

## 7. Scope of the entropy resource

The rates $\sigma_{\rm hid}$ and $\sigma_0$ are stationary path-irreversibility rates under ordinary identity reversal. They do not cover a reversal that permutes hidden states, changes the sign of an odd variable, or reverses an internal word. The [generalized-reversal construction](GENERALIZED_REVERSAL_PREDICTION.md) gives a concrete boundary: the polynomial word predictor admits generalized detailed balance after centering its even actuator, with exactly the same controlled response. A thermodynamic interpretation needs the appropriate physical reversal convention and local detailed balance. No universal heat-cost assertion follows merely from assigning a nonzero value to (5).

The broad endpoint estimate permits arbitrary injection and return functions obeying (3). The fully reversible comparison and baseline resource interpretation use the additional common-ratio condition (14). State-complexity lower bounds for a particular actuator class require their own observability proof; this note does not infer one from the entropy comparison alone.
