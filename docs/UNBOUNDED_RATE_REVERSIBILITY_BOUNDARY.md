# The boundary at unbounded reversible rates

[Binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Scalar observability](REVERSIBLE_WORD_OBSERVABILITY.md) · [Positive transport repair](POSITIVE_TRANSPORT_REPAIR.md)

**Research boundary note, 23 September 2026.** The established exponential reversible-state lower bounds assume a fixed rival rate cap. This note proves an obstruction to one proposed way of removing that cap, and removes the cap from the algebraic repair step of the nineteen-level proof. It does **not** establish an uncapped exponential lower bound or exhibit a smaller fast reversible predictor.

## 1. A positive-semidefinite obstruction to the literal binary replacement

The binary construction uses an entrywise nonnegative reversible stochastic matrix
$P=I+K/6580$. Entrywise positivity is different from positive semidefiniteness. In particular, its accepted odd-length palindromic words need not be positive semidefinite.

Suppose instead that every occurrence of $P$ in the existing marker, gate and probe words is replaced by a selfadjoint positive-semidefinite operator $S$. Examples are $e^{tK}$, $s(sI-K)^{-1}$, and nonnegative mixtures of these operators. Let $D_c$ denote the orthogonal color projectors, and consider a palindromic color word

$$
W=D_{c_0}S D_{c_1}S\cdots S D_{c_\ell},
\qquad c_i=c_{\ell-i}.
\tag{1}
$$

If $\ell=2m$, then $W=B D_{c_m}B^*$, where
$B=D_{c_0}S\cdots D_{c_{m-1}}S$. If $\ell=2m+1$, then

$$
W=B(D_{c_m}S D_{c_m})B^*.
\tag{2}
$$

For $m=0$ take $B=I$. Both central operators are positive semidefinite, so $W\succeq0$. Consequently

$$
\widetilde T_g=\kappa^{-1}A W A\succeq0
\tag{3}
$$

for every selfadjoint $A$ and positive normalization $\kappa$. This applies in particular to the marker sandwich $A=TT^*/p_*$, with any positive, possibly scale-dependent normalization.

The original binary target requires, for its root probe $v=\sigma x_b1_{\mathcal R}$,

$$
\langle v,T_Fv\rangle_\mu=-m,
\qquad m=\mu(\mathcal R)=1/18.
\tag{4}
$$

In contrast, (3) gives $\langle z,\widetilde T_Fz\rangle_\mu\ge0$ for **every** vector $z$, including a probe obtained by the same replacement. Thus the literal replacement cannot recover the negative lamp scalar to error smaller than $m$. No choice of small semigroup time, large resolvent parameter, positive normalization or selfadjoint marker sandwich resolves this obstruction.

This is a failure of that particular replacement, not a disproof of an uncapped lower bound. Signed combinations, different observation words or a different gadget are not covered. The nineteen-level triangular cross-port cycle is not a palindromic word of the form (1), so this argument does not exclude its semigroup variants.

## 2. Whole-word repair using measured vector norms

The following lemma avoids every global bound on the raw kernel norms or row sums. All operators act on the rival's own finite probability space $(\Omega,\nu)$; $T^*$ always denotes the stationary adjoint for that space.

**Lemma.** Let $|s|\le1$, and let $Q_b,C_c$ be entrywise nonnegative kernels, indexed by $b,c\in\{1,\ldots,r\}$. Put $v_b=Q_bs$ and $\sigma_{bc}=(-1)^{\mathbf1_{b=c}}$. Suppose $0\le\Delta\le1$ and

$$
\begin{aligned}
\|Q_b1-1\|_2^2&\le\Delta, &
\big|\|v_b\|_2^2-1\big|&\le\Delta,\\
\|C_c1-1\|_2^2&\le\Delta, &
\|C_c^*1-1\|_2^2&\le\Delta,\\
\|C_cv_b\|_2^2&\le1+\Delta, &
\sigma_{bc}\langle v_b,C_cv_b\rangle&\ge1-\Delta.
\end{aligned}
\tag{5}
$$

There are stationary Markov kernels $U_c$ and functions $|h_b|\le1$ on the same state space such that

$$
\|h_b\|_2^2\ge1-4\sqrt\Delta,
\qquad
\sigma_{bc}\langle h_b,U_ch_b\rangle\ge1-8\sqrt\Delta.
\tag{6}
$$

Moreover, if $\sqrt\Delta\le1/(32r)$, then $|\Omega|\ge2^{3r/4}$.

**Proof.** Write $\varepsilon=\sqrt\Delta$ and clip $v_b$ to $h_b\in[-1,1]$. Positivity gives $|v_b|\le Q_b1$, hence

$$
\|v_b-h_b\|_2\le\|Q_b1-1\|_2\le\varepsilon.
\tag{7}
$$

Since $\|h_b\|_2\le1$ and $\|v_b\|_2\le\sqrt{1+\Delta}$,

$$
1-\|h_b\|_2^2
\le\Delta+\varepsilon(\sqrt{1+\Delta}+1)
\le4\varepsilon.
\tag{8}
$$

The balanced-flux construction applied once to the **whole** kernel $C_c$ yields a stationary Markov kernel $U_c$ satisfying

$$
\sum_{i,j}\nu_i|C_c(i,j)-U_c(i,j)|\le3\varepsilon.
\tag{9}
$$

The additional measured norm $\|C_cv_b\|_2$ controls the first endpoint replacement; positivity controls the second:

$$
\begin{aligned}
|\langle v_b,C_cv_b\rangle-\langle h_b,C_ch_b\rangle|
&\le\|v_b-h_b\|_2\|C_cv_b\|_2
 +\|C_c^*h_b\|_2\|v_b-h_b\|_2\\
&\le\varepsilon\big(\sqrt{1+\Delta}+1+\varepsilon\big).
\end{aligned}
\tag{10}
$$

Here $|C_c^*h_b|\le C_c^*1$ and $\|C_c^*1\|_2\le1+\varepsilon$. Both endpoints are bounded after clipping, so (9) changes the correlation by at most $3\varepsilon$. Its total deficit is at most

$$
\Delta+\varepsilon(\sqrt{1+\Delta}+1+\varepsilon)+3\varepsilon
\le(6+\sqrt2)\varepsilon<8\varepsilon.
\tag{11}
$$

This proves (6) without using $\|C_c\|_{2\to2}$.

For completeness, round $Z_b=\operatorname{sign}(h_b)$, with sign zero chosen as $+1$. Equation (8) gives $\mathbb E|Z_b-h_b|\le4\varepsilon$. Under a stationary pair $(I,J)$ with transition $U_c$, replacing both endpoints in (6) therefore costs at most $8\varepsilon$. Thus

$$
\Pr\{Z_b(J)\ne\sigma_{bc}Z_b(I)\}\le8\varepsilon.
\tag{12}
$$

Writing $\rho$ for the joint law of all $r$ rounded bits, a union bound gives
$\operatorname{TV}(\rho,\operatorname{flip}_c\rho)\le8r\varepsilon$.
The same conditional binary-entropy argument as in the main theorem yields

$$
\log_2|\Omega|\ge H(Z)\ge r(1-8r\varepsilon).
\tag{13}
$$

The asserted state lower bound follows. No state, coordinate label or physical control has been added. The $U_c$ are proof kernels, not a physical surrogate. $\square$

## 3. Instantiation in the nineteen-level target

Use the original raw cross-port kernels

$$
T_{cd}=16D_cK_bD_d\qquad(c\ne d)
\tag{14}
$$

on the conditional stationary port spaces. These kernels remain nonnegative for every finite reversible rival, however large its rates. Detailed balance and the exact equal port masses identify the reverse edge with its conditional stationary adjoint. Set

$$
Q_b=W_b,\qquad C_c=W_cG_FW_c^*,\qquad v_b=W_bs,
\tag{15}
$$

with the words and signed central actuator $s$ from the nineteen-level theorem. In the target all the row-defect squares in (5) vanish, both vector norm squares equal one, and the signed correlation equals one. Every quantity in (5) is a polynomial scalar with the original physical preparation and readout. For example,

$$
\begin{aligned}
\|Q_b1-1\|_2^2
 &=\langle1,Q_b^*Q_b1\rangle-2\langle1,Q_b1\rangle+1,\\
\|C_cv_b\|_2^2
 &=\langle s,W_b^*C_c^*C_cW_bs\rangle.
\end{aligned}
\tag{16}
$$

The first identity uses real kernels. Unsigned endpoints use the physical $B_j$ identities; signed endpoints use $B_s$, as in Sections 3 and 6 of the main theorem. All intermediate vectors are hidden-supported, so the extra visible component of a left $B_j$ endpoint vanishes.

The exact word counts are

| Word or scalar | Maximum cross-port edge count |
| --- | ---: |
| $Q_b=W_b$ | $9n$ |
| $C_c=W_cG_FW_c^*$ | $18n+3$ |
| $Q_b^*Q_b$ | $18n$ |
| $C_c^*C_c$ or $C_cC_c^*$ | $36n+6$ |
| $W_b^*C_cW_b$ | $36n+3$ |
| $W_b^*C_c^*C_cW_b$ | $54n+6$ |

Every edge has physical generator degree three and the two endpoints add degree two. Thus the largest needed degree is $162n+20$, and all coefficient masses are $\exp(O_H(n))$. If each individual basic scalar differs from its target value by at most $d$, then the row-defect expressions in (16) are at most $3d$; taking $\Delta=3d$ covers all hypotheses. There is no factor for the number of addresses until the explicit union bound (12).

Consequently, agreement of these physical polynomial scalars to
$3d\le1/(1024r^2)$ already forces at least $2^{3r/4}$ central rival states, **without a rate assumption in this algebraic implication**.

For a fixed rival cap, the existing scalar transfer gives $d=A_\Lambda^{n+1}\delta^{\theta_\Lambda}$ and recovers the same growth-class lower bound. The new proof repairs whole flip words and uses extra measured Gram norms instead of multiplying a global raw-kernel bound along every edge. In the nineteen-level argument, the remaining rate-cap use is therefore localized to quantitative recovery of the polynomial scalars from actual controlled means.

That remaining issue is substantial: target-only propagator approximation suffices for a rank argument, but does not automatically give (5) for the rival's raw generator words. A fast mode of tiny stationary weight can have small propagator effects and large generator moments. The present lemma does not supply a cap-independent polynomial-scalar transfer.

## 4. A general cap-free norm estimate for flux repair

There is also a useful estimate when the additional whole-word Gram norms in (5) are unavailable. Suppose a nonnegative kernel $T$ and its adjoint have row defects at most $\varepsilon$ in $L^2$. Let $U$ be its balanced-flux repair, so its weighted entrywise $L^1$ error is at most $3\varepsilon$. Then

$$
\|T-U\|_{\infty\to2},\ \|T-U\|_{2\to1}
\le\varepsilon+\sqrt{6\varepsilon}.
\tag{17}
$$

Indeed, for $|f|\le1$, put $d=(T-U)f$ and $r=T1$. Then $\|d\|_1\le3\varepsilon$ and $|d|\le r+1\le2+|r-1|$. Hence, writing $x=\|d\|_2$,

$$
x^2\le2\|d\|_1+\langle|d|,|r-1|\rangle
\le6\varepsilon+\varepsilon x,
\tag{18}
$$

which implies the first estimate. Apply it to the consistently repaired adjoint and use duality for the second. The argument also holds between two different conditional probability spaces.

For a product of raw kernels, telescope using raw prefixes and repaired suffixes. If the adjoint raw prefixes applied to the left endpoint have measured $L^2$ norms $M_j$, while the right endpoint is bounded by one, then the scalar repair error is at most

$$
\sum_j M_j\big(\varepsilon_j+\sqrt{6\varepsilon_j}\big).
\tag{19}
$$

This replaces global operator-norm growth by measured prefix norms. Its square-root loss is weaker than Section 2 when the additional Gram data there are available.

## 5. Rare fast states prevent raw-moment transfer

The remaining observability obstacle is not merely a missing estimate: a uniform transfer bound for the raw generator moments in Section 3 is false in the uncapped class, even near a fixed target.

Set $k=1$, fix any nineteen-level target with hidden law $\mu$, and write
$R=e^{(1+G)H}$, $\alpha=1/R$. Let $\nu$ be the probability law on nineteen new states having exactly the target sensitivity histogram: mass $1/2$ at sensitivity zero and mass $1/36$ at each signed nonzero level. For $0<\epsilon<1$ and $L>0$, form the augmented rival

$$
\mu'=(1-\epsilon)\mu\ \oplus\ \epsilon\nu,
\qquad
K'=K\ \oplus\ L(1\nu^T-I).
\tag{20}
$$

Use the original external field rule, the original preparation associated with $\mu'$, and the binary visible readout. The hidden dynamics are reversible under $\mu'$, and the actuator histogram is unchanged exactly. The full physical chain is irreducible through $A$, although this first hidden generator has two components.

**Uniform mean estimate.** The target and rival can be coupled until the rival enters the new component. Their total exit rate from $A$ is the same at every field, because it depends only on the histogram. At a matched exit from $A$, the rival chooses the new component with probability exactly $\epsilon$; otherwise it chooses the same old hidden state as the target. Such potentially separating entries have intensity at most $\epsilon R$. The initial probability of being in the new component is $\epsilon/2$.

Both physical generators contain a common reset to $A$ at rate $\alpha$: subtracting $\alpha(J_A-I)$ leaves a Markov generator, including at $A$, where this reset is a fictitious self-transition. Use the same reset clock for both chains. It restores agreement regardless of their previous states. If the pair is marked as possibly separated after an exceptional entry and cleared at a reset, its marked probability is at most

$$
\frac\epsilon2e^{-\alpha t}
+\epsilon R\int_0^t e^{-\alpha(t-s)}\,ds
\le\epsilon R^2.
\tag{21}
$$

The bounded binary readouts can differ by at most two. Therefore

$$
\sup_{h,t}|m'[h](t)-m[h](t)|\le2\epsilon R^2,
\tag{22}
$$

uniformly over all bounded protocols and all horizons, independently of $L$.

**Unbounded raw row moment.** Each nonzero sensitivity port has conditional auxiliary mass $\epsilon$. Choose two distinct adjacent ports from a gate triangle; for this pair, the target raw kernel $T_{cd}=16D_cKD_d$ has row sum one. On the auxiliary component the corresponding row sum is $16L/18=8L/9$. Thus the rival's exact conditional row-defect square is

$$
\mathbb E_c(T_{cd}1-1)^2
=\epsilon(8L/9-1)^2.
\tag{23}
$$

At any positive allowed mean tolerance, choose $\epsilon$ small enough for (22) and then send $L$ to infinity. The physical polynomial scalar (23) becomes arbitrarily large. In particular there is no finite cap-independent modulus, tending to zero or otherwise, that bounds this required raw moment from mean accuracy alone.

If hidden irreducibility is required, add the reversible global refresh
$\eta(1(\mu')^T-I)$ to (20). It preserves $\mu'$ and every actuator label, and connects every hidden state. A further coupling marks an extra refresh, of intensity at most $\eta$, and clears it with the same reset clock. Its extra mean error is at most $2\eta/\alpha=2\eta R$. The row-defect square becomes

$$
(1-\epsilon)(8\eta/9)^2
+\epsilon\big(8(L+\eta)/9-1\big)^2.
\tag{24}
$$

For example, taking $\eta=\epsilon$ leaves mean error at most
$2\epsilon(R^2+R)$ and still permits (24) to diverge. Restoring units replaces the two refresh rates by $kL$ and $k\eta$.

This construction retains the entire target and adds nineteen hidden states. It is **not a state compression or a counterexample to an uncapped state lower bound**. It establishes that a successful extension cannot demand closeness of all the rival's unmodified raw moments. It must tolerate or remove nearly unobserved fast components, use bounded proof operators, or obtain a different kind of observable estimate.

## 6. What remains open

The polynomial state lower based on a finite matrix of physical propagator words already permits unbounded rival rates. The stronger quantitative exponential lower in inverse error remains open in that class. Neither the PSD obstruction nor a failure of one extraction scheme establishes that fast reversible rivals can compress the target.

A complete extension still needs positive proof kernels and quantitative observable scalar estimates strong enough to meet (5), with constants independent of rival rates and state count. Section 5 rules out obtaining this by an unconditional transfer to the unmodified raw cross-port moments. Alternatively, an explicit fast reversible construction would have to preserve the original field rule and exact actuator histogram, count every new state, and control the actual means over the full requested protocol and time class. Approximation after replacing a cluster by a mixture of actuator levels requires a separate argument because that cluster need not obey a single-level original rule.
