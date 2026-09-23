# Fixed-clock Gram observability and physical resolvent words

[Fixed-clock uncapped theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Positive hidden resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) · [Primary-source comparison](FIXED_CLOCK_PRIOR_ART.md) · [Original model](THEORY.md) · [Earlier fixed-clock transfer](REVERSIBLE_WORD_OBSERVABILITY.md)

**Research lemma, 23 September 2026.** Under the original preparation, readout and field rule, mean observations at a fixed positive clock determine Gram scalars of sampled operator words quantitatively. Rank-one insertions at the visible state and stationary adjoints introduce no new preparation or measurement. A target spectral cap then permits quantitative transfer of words of physical resolvents without any rival rate cap.

The proof uses finite legal clock words throughout. It does not infer raw generator derivatives or a global rival spectral bound.

## 1. Model, clock and notation

Work in units $k=1$. Fix a clock $a>0$ and a finite field menu $\mathcal H\subset[-H,H]$. In each finite model use the original rates, preparation and readout, with a reversible hidden generator and positive hidden stationary law. Put

$$
\pi_0=(1/2,\mu/2),\qquad S=1-2e_A,\qquad
A=e_Ae_A^{\mathsf T},\qquad E_h=e^{aQ_h}.
\tag{1}
$$

Here $A$ is a diagonal rank-one projector, not an extra physical operation. A forward clock word is a product of the $E_h$. Empty words are allowed. For such a word $V$ define

$$
M(V)=\pi_0VS,\qquad b(V)=e_A^{\mathsf T}VS.
\tag{2}
$$

Assume the two models' observed means satisfy

$$
|M(V)-\widehat M(V)|\le\delta,\qquad 0<\delta\le1,
\tag{3}
$$

for all forward clock words used below. Hats have their own state space and law. A uniform all-word fixed-clock hypothesis is sufficient. Whenever a finite horizon is specified, only words up to that horizon are needed.

Let

$$
C_{\mathcal H}=1+2\max_{h\in\mathcal H\setminus\{0\}}|1+\coth h|,
\qquad J_H=2e^{2H}-1,\qquad \chi=e^H,
\tag{4}
$$

where the maximum over an empty set is zero. Constants may depend on the fixed menu; no uniformity as a nonzero menu field approaches zero is claimed.

## 2. Exact finite recovery of the visible-state row

The stationary law at field $h$ is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h}.
$$

Writing $t_h=\tanh h$, it has the exact row identity

$$
\pi_h=(1+t_h)\pi_0-t_he_A^{\mathsf T}.
\tag{5}
$$

For $h\ne0$, stationarity $\pi_hE_h=\pi_h$ gives

$$
\boxed{
b(E_hV)=b(V)+(1+\coth h)\,[M(E_hV)-M(V)].}
\tag{6}
$$

For $h=0$, the span of the visible state and the hidden equilibrium row is the exact rate-one telegraph sector, independently of the hidden generator. With $\rho=e^{-2a}$,

$$
e_A^{\mathsf T}E_0=\rho e_A^{\mathsf T}+(1-\rho)\pi_0,
\qquad
\boxed{b(E_0V)=\rho b(V)+(1-\rho)M(V).}
\tag{7}
$$

Starting from $b(I)=-1$, equations (6)–(7) recover $b(V)$ by processing successive suffixes of $V$. Every required $M$ is a legal forward word of length at most $|V|$. No long-time preparation limit, shortened clock tick or hidden preparation is used.

The same recursion applies in the rival. From (3), each nonzero-field step adds at most $2|1+\coth h|\delta$ to the discrepancy; a zero-field step adds at most $\delta$ and contracts the inherited discrepancy. Consequently

$$
|b(V)-\widehat b(V)|\le C_{\mathcal H}|V|\delta.
\tag{8}
$$

The sum of absolute coefficients in its finite mean formula, including its constant term, is at most $1+C_{\mathcal H}|V|$.

### Visible-state projector insertions

For $r\ge1$, rank one gives

$$
\begin{aligned}
&\pi_0V_0AV_1A\cdots AV_rS\\
&\quad=\frac{1-M(V_0)}2
\prod_{j=1}^{r-1}\frac{1-b(V_j)}2\ b(V_r).
\end{aligned}
\tag{9}
$$

The first and intermediate factors lie in $[0,1]$ and the last lies in $[-1,1]$. Thus the discrepancy of (9), for total forward length $d=\sum_j|V_j|$, is at most

$$
(1+C_{\mathcal H}d)\delta.
\tag{10}
$$

The same bound covers $r=0$. This bound does not grow with the number of empty blocks or consecutive projectors. It follows by telescoping the products of actual bounded factors, not by bounding an expanded product of noisy linear formulas. The complementary projector $I-A$ can be handled by expansion.

## 3. Stationary adjoints and sampled Gram scalars

Detailed balance at each fixed field implies

$$
E_h^{*\pi_0}=W_hE_hW_h^{-1},\qquad
W_h=I+(e^{-2h}-1)A.
\tag{11}
$$

Indeed $\pi_h/\pi_0$ is a positive scalar multiple of $W_h$. The four-term expansion of (11) has coefficient mass

$$
(1+|e^{-2h}-1|)(1+|e^{2h}-1|)
=2e^{2|h|}-1\le J_H.
\tag{12}
$$

The projector $A$ is its own $\pi_0$-adjoint. Let $U,V$ be words in sampled propagators and $A$, with $\ell_U,\ell_V$ propagator occurrences; projector occurrences are not counted. Then

$$
\langle US,VS\rangle_{\pi_0}
=\pi_0(I-2A)U^{*\pi_0}VS.
\tag{13}
$$

Expand the adjoints using (11). The total coefficient mass is at most $3J_H^{\ell_U}$, while each resulting inserted forward word has length $\ell_U+\ell_V$. Equations (9)–(10) give

$$
\boxed{
\begin{aligned}
&|\langle US,VS\rangle_{\pi_0}
-\langle\widehat U\widehat S,\widehat V\widehat S\rangle_{\widehat\pi_0}|\\
&\quad\le 3J_H^{\ell_U}
[1+C_{\mathcal H}(\ell_U+\ell_V)]\delta.
\end{aligned}}
\tag{14}
$$

Every mean used in this formula has at most $\ell_U+\ell_V$ clock ticks. All factors $A$ and all adjoints remain analytical insertions reconstructed from those means.

For a weighted norm at another menu field $h$, use

$$
\frac{\pi_h}{\pi_0}=(1+t_h)I-2t_hA.
\tag{15}
$$

Inserting (15) between $U^{*\pi_0}$ and $V$ multiplies the coefficient bound by at most $|1+t_h|+2|t_h|\le4$. Hence weighted Gram scalars obey four times the bound (14).

### Clock-polynomial endpoints

A clock polynomial is a finite linear combination of words in $E_h,A$, with model-independent coefficients. Its degree is the largest number of propagator occurrences in a word, and its coefficient mass is the sum of absolute coefficients. If $X,Y$ have degrees at most $d$ and masses $B_X,B_Y$, expansion gives the weighted Gram bound

$$
|\langle XS,YS\rangle_{\pi_h}
-\langle\widehat X\widehat S,\widehat Y\widehat S\rangle_{\widehat\pi_h}|
\le B_XB_Y\,\mathcal G_d\delta,
\tag{16}
$$

where one convenient choice is

$$
\mathcal G_d=12J_H^d(1+2C_{\mathcal H}d).
\tag{17}
$$

The endpoints $1,e_A,S$ belong to this same class because $e_A=-AS$ and $1=(I-2A)S$. Thus no separate endpoint observation is needed. Words in $E_h,A$ are contractions in the supremum norm; in particular $\|XS\|_{\pi_h}\le B_X$ for every model. Finally, every $E_h$, every positive normalized physical resolvent at field $h$, and the polynomials constructed below have $L^2(\pi_0)$ operator norm at most $\chi$, by norm equivalence with $L^2(\pi_h)$. The projector $A$ is a contraction in both norms.

## 4. Contractive clock polynomials for a physical resolvent

Fix $h\in\mathcal H$ and $z>0$. The normalized physical resolvent is

$$
R_{h,z}=z(zI-Q_h)^{-1}
=\int_0^\infty ze^{-zt}e^{tQ_h}\,dt.
\tag{18}
$$

Put $\lambda=az$ and $r=e^{-\lambda}$. For $0\le s\le1$, write

$$
x^s=1-\sum_{l\ge1}c_l(s)(1-x)^l,\qquad 0\le x\le1,
\tag{19}
$$

where $c_l(s)=(-1)^{l-1}\binom{s}{l}\ge0$. For $0<s\le1$, their sum is one; for $s=0$ all coefficients vanish and $x^0$ is defined to be one also at zero. Let

$$
H_{s,M}(x)=1-\sum_{l=1}^M c_l(s)(1-x)^l,
\qquad M\ge1.
$$

For every $x\in[0,1]$,

$$
0\le x^s\le H_{s,M}(x)\le1,\qquad
0\le H_{s,M}(x)-x^s\le(1-x)^{M+1}.
\tag{20}
$$

Average using the probability density $w_\lambda(s)=\lambda e^{-\lambda s}/(1-r)$ on $[0,1]$ and set

$$
\overline H_{\lambda,M}(x)=\int_0^1w_\lambda(s)H_{s,M}(x)\,ds,
$$

$$
T_{h,z;M,J}
=(1-r)\sum_{j=0}^Jr^j E_h^j\overline H_{\lambda,M}(E_h),
\qquad J\ge0.
\tag{21}
$$

This is a clock polynomial of degree at most $J+M$. Its coefficient mass in powers of $E_h$ is at most $2^{M+1}$: the truncated binomial polynomial has mass at most $1+\sum_{l\le M}c_l(s)2^l\le2^{M+1}$, and both averages in (21) have total nonnegative weight at most one.

More importantly, (20) implies that $T_{h,z;M,J}$ is a selfadjoint positive-semidefinite contraction in $L^2(\pi_h)$ **in every model**, regardless of its rates. This does not assert that the polynomial has nonnegative matrix entries.

Splitting $t/a=j+s$ in (18) gives the exact expression obtained from (21) by replacing $J$ by infinity and $\overline H$ by the average of $E_h^s$. Spectral calculus and (20) therefore imply, for every vector $f$,

$$
\boxed{
\|(R_{h,z}-T_{h,z;M,J})f\|_{\pi_h}
\le r^{J+1}\|f\|_{\pi_h}
+\|(I-E_h)^{M+1}f\|_{\pi_h}.}
\tag{22}
$$

The tail $r^{J+1}$ comes from a geometric sum of contractions. The second term is a vector-specific high-frequency remainder; it is not replaced by a small rival operator norm.

## 5. Transfer the remainder norm from a capped target

Assume only the target satisfies

$$
\operatorname{spec}(-Q_h)\subset[0,L_*]
\quad(h\in\mathcal H),\qquad
q=1-e^{-aL_*}<1.
\tag{23}
$$

A fixed target exit bound supplies such an $L_*$ by the usual row-sum spectral bound. There is no corresponding assumption on a rival.

For a clock polynomial $P$ of degree $d_0$ and mass $B$, apply the weighted Gram estimate to $(I-E_h)^{M+1}PS$. Its degree is at most $d=d_0+M+1$ and its coefficient mass at most $2^{M+1}B$. Equation (23) then gives

$$
\begin{aligned}
\|(I-\widehat E_h)^{M+1}\widehat P\widehat S\|_{\widehat\pi_h}
&\le q^{M+1}\|PS\|_{\pi_h}
+2^{M+1}B\sqrt{\mathcal G_d\delta}.
\end{aligned}
\tag{24}
$$

This follows by comparing squared norms and using $\sqrt{x+y}\le\sqrt x+\sqrt y$. It is the point where the target cap controls a rival remainder through data. It supplies no cap on the rival generator.

In particular, let $P$ be a suffix consisting of at most $L$ polynomials (21), arbitrary interspersed projectors $A$, and a clock-polynomial endpoint $Y$ of degree $d_0$ and mass $B_Y$. Each suffix factor is a contraction in its own stationary norm, and norm equivalence gives

$$
\|PS\|_{\pi_h},\ \|\widehat P\widehat S\|_{\widehat\pi_h}
\le\chi^{L+1}B_Y.
\tag{25}
$$

The suffix's coefficient mass is at most $2^{(M+1)L}B_Y$ and its clock degree at most $L(M+J)+d_0$. Substitute these bounds into (22)–(24). The polynomial coefficient mass enters only the observational error; it does not replace the norm bound (25).

## 6. Finite words: true prefixes and polynomial suffixes

Let $\mathcal W$ be a word of at most $L$ normalized physical resolvents $R_{h,z}$, with arbitrary interspersed projectors $A$. All parameters and the word are fixed identically in both models. Let $X,Y$ be clock polynomials of degrees at most $d_0$ and masses $B_X,B_Y$. Define

$$
r_* = \max_{(h,z)\text{ in }\mathcal W}e^{-az}<1.
$$

Replace each resolvent by (21), with common $M,J$. In the telescoping difference, keep the prefix as the **true** resolvent word and the suffix as the polynomial word. True prefixes have norm at most $\chi^L$ in $L^2(\pi_0)$; polynomial suffixes obey (25). Apply (22)–(24) to each replacement. The same argument in the target needs no data term. The scalar difference between the two fully polynomial words is controlled by (16), after including the endpoint adjoint and the interspersed projectors.

It follows that there is a fixed constant $C$, depending only on $H,\mathcal H$ (and harmless enlargement of fixed numeric constants), such that

$$
\boxed{
\begin{aligned}
&|\langle XS,\mathcal WYS\rangle_{\pi_0}
-\langle\widehat X\widehat S,\widehat{\mathcal W}\widehat Y\widehat S\rangle_{\widehat\pi_0}|\\
&\quad\le B_XB_Y(L+1)e^{C(L+1)}
\left(r_*^{J+1}+q^{M+1}\right)\\
&\qquad+B_XB_Y
\exp\!\left(C(L+1)(M+J+d_0+1)\right)\sqrt\delta.
\end{aligned}}
\tag{26}
$$

For an empty resolvent word the first line of the bound can be omitted. The estimate is uniform in rival state count, hidden rates and minimum stationary mass. A varying positive resolvent parameter affects the explicit geometric tail through $r_*$; it does not change the contraction or coefficient-mass bounds.

All applications of (3) in this argument use at most

$$
2\bigl[L(M+J)+d_0+M+1\bigr]
\tag{27}
$$

clock ticks. This conservative count covers the remainder Gram words and the final polynomial scalar. Thus the proof has a finite witnessing horizon at the prescribed positive clock. Negative polynomial coefficients, adjoints and $A$ insertions are analytical combinations of those legal mean experiments.

If $L,d_0$, $\log(1+B_X+B_Y)$, the required logarithmic precision and $1/\min z$ grow at most polynomially with a target index, then $M,J$ can also be chosen polynomially. Equations (26)–(27) give an observation cost exponential in a polynomial of that index. Any subsequent hidden Schur complement, rare normalization, heat approximation or entropy argument must account for its own additional factors. This lemma alone does not establish such a target construction or a new state-complexity lower bound.
