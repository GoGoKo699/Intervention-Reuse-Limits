# Recovering bounded rational selectors from a finite clock experiment

[Finite target](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Earlier minimum counts](FINITE_PREDICTOR_MINIMALITY.md) · [Observation bottleneck](FINITE_OBSERVATION_BOTTLENECK.md) · [Sharper Gram obstruction](FINITE_GRAM_ROBUSTNESS.md) · [Source comparison](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) · [Exact certificate report](../reports/rational_observation.json)

**Research theorem, 23 September 2026.** For the unchanged twelve-state incidence target, ordinary reversibility requires twelve states at error at most $2^{-220}$ on an explicit collection of 12,766 two-field clock experiments, each using at most 66 ticks. The existing eleven-state stationary predictor reproduces every controlled mean exactly. The new threshold improves the previous sufficient $2^{-1360}$ bound, but remains far below practical measurement accuracy.

The proof recovers bounded rational selectors through the target's ten-dimensional observable subspace. It does not expand the selectors into a high-degree generator polynomial. The selectors used on a rival are the exact nonnegative rational functions, and the conclusion covers every ordinarily reversible rival in the original comparison class, including arbitrary endpoint barriers in $[0,1]$, new states and stationary masses.

The unrestricted minimum is known to be eleven throughout the earlier interval $0\le\delta\le2^{-1360}$. At the larger threshold proved here, the statement is an unrestricted sufficient count of eleven and an ordinary-reversible minimum of twelve; no new unrestricted lower is asserted.

The basis inequality used below is an essential, bounded computer-assisted premise, established by exact rational arithmetic with explicit transcendental and rounding errors. The subsequent transfer from finite means to an arbitrary rival is analytic. The [reproducible certificate](../scripts/verify_rational_observation.py) is not a numerical fit or a test over a selected rival family.

## 1. The unchanged comparison

Use the target, preparation, readout, state counting and rival interface of the [finite construction](FINITE_REVERSIBILITY_ADVANTAGE.md#1-task-and-statement). In particular, the hidden generator $K$ is field-independent, stationary for a positive probability law $\mu$, and has exit rates at most $2k$. At the queried fields,

$$
q_{iA}(h)=k b_i(h),\qquad q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
\qquad b_i(0)=1,\quad b_i(H)\in[0,1].
\tag{1}
$$

The preparation is $\pi_0=(1/2,\mu/2)$, the readout is $S=(-1,1_{\rm hid})$, and ordinary reversibility means detailed balance of $K$ with respect to $\mu$. The fields and clock remain

$$
H=\log2,\qquad a/k=\frac{\log2}{8k}.
\tag{2}
$$

The target has six memory edges and five probe states, with the six endpoint barriers $\beta_j=(6+j)/16$, $0\le j\le5$. Its total state count is twelve, its hidden exit cap is two, and its nonzero hidden decay rates lie in $[k,3k]$. All of these facts are established in the unchanged construction.

Set $k=1$ for the proof, write $E_h=\exp(aQ_h)$, and use the $L^2(\pi_0)$ norm on full functions. Let $J=e_Ae_A^{\mathsf T}$ and $\mathsf H=I-J$. Hats denote a rival. Every field generator is reversible in its field stationary law

$$
\pi_h=\frac{(1,e^{2h}\mu)}{1+e^{2h}}.
\tag{3}
$$

At the two fields, the full exit cap is at most four. Therefore the spectra of $E_h$, in their reversible metrics, lie in $[1/2,1]$. In the common $\pi_0$ metric, $\|E_h\|\le2$, $\|Q_0\|\le8$, and $\|Q_H\|\le16$. These bounds hold in every ordinarily reversible rival, independently of its state count or stationary masses.

## 2. A fixed observable basis and a finite experiment menu

The target's full stochastic intertwiner from the earlier construction has a ten-dimensional column space $\mathcal O$: its hidden incidence block has rank four, its probe block has rank five, and its visible column adds one dimension. The intertwining identity implies that $\mathcal O$ is invariant under $Q_0,Q_H,E_0,E_H$ and $J$. It contains $1$ and $S$.

Use the following ten target functions, and evaluate the same words on every rival:

$$
\begin{aligned}
f_0&=1,& f_1&=S,& f_2&=E_H^4S,& f_3&=E_H^{16}S,\\
f_4&=E_0^4E_H^4S,& f_5&=E_H^8S,
& f_6&=E_H^4E_0^4E_H^4S,\\
f_7&=E_H^{32}S,& f_8&=E_0E_H^8S,
& f_9&=E_H^{16}E_0^4E_H^4S.
\end{aligned}
\tag{4}
$$

Write $U:\mathbb R^{10}\to\mathcal O$ for the column map $Uc=\sum_i c_i f_i$, and write $\widehat U$ for its rival counterpart. All these functions have absolute value at most one. Thus

$$
\|U\|\le\sqrt{10}<4.
\tag{5}
$$

The fixed target basis certificate is

$$
\boxed{U^*U\succeq2^{-52}I,\qquad \sigma_{\min}(U)\ge2^{-26}.}
\tag{6}
$$

Here $U^*U$ uses the exact target law $\pi_0$. Its numerical smallest singular value is approximately $4.85\times10^{-8}$; this diagnostic is not used in place of the rational certificate. Inequality (6), together with $\dim\mathcal O=10$, proves that (4) is a basis of the invariant space.

The exact certificate constructs the twelve-by-twelve generators from rational rates, checks their stationary laws, and verifies the ten-dimensional invariant column space by rational elimination. It then encloses the clock using 80 terms of

$$
\log2=2\sum_{j\ge0}\frac1{(2j+1)3^{2j+1}},
\qquad
0<\text{tail}_{80}\le
\frac2{161\,3^{161}(1-1/9)}.
$$

Round the lower clock bound to the nearest multiple of $2^{-192}$, retaining the logarithm tail divided by eight plus $2^{-193}$ as its time error. For each one-tick matrix, use a Taylor polynomial of order 64, evaluated by Horner's method with each entry rounded to that same mesh. The matrix argument has infinity norm below one. Thus the Taylor tail is at most $3/65!$, cumulative Horner rounding is at most $64\cdot12\cdot2^{-193}$, and the clock error contributes at most $\|Q_h\|_\infty$ times its time bound, since the exact semigroups are stochastic.

Propagate powers and word actions with outward error bounds. For a rounded product of two matrices with stochastic exact counterparts and errors $e_A,e_B$, the new infinity-norm error is at most $e_A+e_B+e_Ae_B+12\cdot2^{-193}$. For a matrix acting on a bounded exact function, the analogous bound is $e_A+e_v+e_Ae_v+2^{-193}$. Rounding these bounds outward on the $2^{-180}$ mesh gives maximum basis-vector error $2^{-174}$.

Let $\widetilde G$ be the exact rational weighted Gram of the rounded basis vectors. Its operator error from $U^*U$ is bounded by $10(2e+e^2)$, which is outwardly bounded by

$$
\|\widetilde G-U^*U\|\le\frac{1281}{2^{180}}<2^{-150}.
$$

Exact rational $LDL^{\mathsf T}$ elimination of $\widetilde G-2^{-51}I$ produces ten strictly positive pivots. Their certified lower bounds, in order, are $2^{-p}$ with

$$
p=(1,1,11,21,25,27,34,36,44,49).
$$

Consequently $U^*U\succ(2^{-51}-2^{-150})I\succ2^{-52}I$, proving (6). No floating matrix exponential or floating eigenvalue enters this certificate. The script records the exact error bounds and pivot digest so that this finite premise can be independently reproduced.

The finite measurement menu can be specified without hidden preparations or path observations. A binary string $w=h_1\cdots h_m$ denotes the actual mean $\pi_0E_{h_1}\cdots E_{h_m}S$, with $0$ denoting field zero and $1$ denoting field $H$. Let

$$
\begin{aligned}
\mathcal U=\{&\varnothing,1^4,1^{16},0^41^4,1^8,
1^40^41^4,1^{32},01^8,1^{16}0^41^4\},\\
\mathcal A={}&\{u,0u,1u:u\in\mathcal U\}.
\end{aligned}
\tag{7}
$$

After removing duplicates, $\mathcal A$ has 26 words. Define $\mathcal M$ to contain every nonempty contiguous subword of

$$
\operatorname{reverse}(u)v,\qquad u,v\in\mathcal A.
\tag{8}
$$

This definition gives a specific list of 12,766 binary words, all of length at most 66. Every member is an ordinary two-field experiment with dwell times that are positive multiples of the unchanged clock. The maximum physical horizon is $66a/k=(33\log2)/(4k)$. Empty-word means are known exactly from the preparation and need no measurement.

The certificate script enumerates this menu, and the report records its count, length distribution and exact export digest. To reproduce the certificate and export every experiment from the repository root, run

~~~sh
.venv/bin/python scripts/verify_rational_observation.py \
  --output /tmp/rational_observation.json \
  --menu-output /tmp/rational_observation_menu.json
~~~

## 3. Recovering a small Gram matrix from those means

Consider the forty functions

$$
\mathcal F=\{f_i,E_0f_i,E_Hf_i,Jf_i:0\le i\le9\}.
\tag{9}
$$

Duplicates may be retained. Each is a word with at most 33 clock letters and at most two consecutive-field-$H$ runs, possibly with $J$ factors. The constant function is represented as $1=(I-2J)S$.

Suppose every mean in $\mathcal M$ differs between target and rival by at most $\delta$. Then every entry of the Gram matrix of (9) differs by at most

$$
\boxed{\varepsilon=2^{20}\delta.}
\tag{10}
$$

Here is the complete observation accounting. In the $\pi_0$ metric,

$$
(E_H^m)^*=W E_H^mW^{-1},\qquad
W=I-\tfrac34J,\quad W^{-1}=I+3J,
\tag{11}
$$

while $E_0$ and $J$ are selfadjoint. One $H$ run therefore has adjoint coefficient mass at most $(1+3/4)(1+3)=7$. A function polynomial in (9) has coefficient mass at most three before taking adjoints. Writing its Gram entries as

$$
\langle U_aS,U_bS\rangle_{\pi_0}
=\pi_0(I-2J)U_a^*U_bS
\tag{12}
$$

gives total coefficient mass at most $3(3\cdot7^2)3=1323$. Every expanded term has at most 66 propagator letters. Erasing its $J$ factors gives one of the strings in (8).

For completeness, the shared stationary interface gives the visible-row recursion

$$
\begin{aligned}
b(E_HV)&=b(V)+(1+\coth H)[m(E_HV)-m(V)],\\
b(E_0V)&=e^{-2a}b(V)+(1-e^{-2a})m(V),\qquad b(I)=-1,
\end{aligned}
\tag{13}
$$

where $b(V)=e_A^{\mathsf T}VS$. Splitting an inserted word at its rank-one $J$ factors expresses its scalar as a product of visible-row and ordinary mean terms. Recursion (13) uses suffixes of those segments. Every required observed word is consequently a contiguous subword listed in $\mathcal M$.

The established finite insertion estimate bounds the discrepancy of a length-$L$ inserted word by $(1+7L)\delta$. At $L\le66$, this is at most $463\delta$. Multiplying by the coefficient mass gives $1323\cdot463\delta=612549\delta<2^{20}\delta$, proving (10). Only endpoint means are required; the $J$ factors are algebraic reconstructions, not additional physical interventions.

## 4. An approximate map between observable spaces

Define $V:\mathcal O\to L^2(\widehat\pi_0)$ by

$$
VU=\widehat U.
\tag{14}
$$

The map need not be positive or stochastic. It is used only for norm comparisons. Since the basis contains $1$ and $S$, it satisfies $V1=\widehat1$, $VS=\widehat S$ and $Ve_A=\widehat e_A$ exactly.

The basis Gram comparison and (6) give

$$
\|V^*V-I\|\le10\varepsilon\,2^{52}
\le2^{76}\delta=:\eta.
\tag{15}
$$

For $T\in\{E_0,E_H,J\}$, target invariance gives $TU=UC_T$. Equations (5)–(6) and $\|T\|\le2$ imply

$$
\|C_T\|\le2^{29},\qquad
b_i:=1+\|C_T(:,i)\|_1\le2^{32},\qquad
\|b\|_2\le2^{34}.
\tag{16}
$$

The target residual $Tf_i-\sum_j C_T(j,i)f_j$ is zero. Its rival squared norm is a linear combination of entries of the Gram matrix in (9), with total absolute coefficient at most $b_i^2$. Thus it is at most $\varepsilon b_i^2$. Summing these residual norms and applying $\|U^{-1}\|\le2^{26}$ yields

$$
\boxed{\|\widehat T V-VT\|\le
\sqrt\varepsilon\,\|b\|_2\,2^{26}
\le2^{70}\sqrt\delta=:e.}
\tag{17}
$$

This uses neither a lower bound on rival stationary masses nor an upper bound on rival dimension. For $\delta\le2^{-220}$, (15) gives $\|V\|\le2$.

## 5. From sampled propagators to hidden generators

The logarithm is stable on the capped positive spectrum. In the common $\pi_0$ norm, for $t\ge0$,

$$
\|(E_h+tI)^{-1}\|\le\frac2{1/2+t},
\tag{18}
$$

and the same estimate holds in a rival. The resolvent representation of the logarithm gives the exact quasi-commutator identity

$$
(\log\widehat E_h)V-V\log E_h
=\int_0^\infty
(\widehat E_h+tI)^{-1}
(\widehat E_hV-VE_h)
(E_h+tI)^{-1}\,dt.
\tag{19}
$$

The integral bound is $4\int_0^\infty(1/2+t)^{-2}dt=8$. Since $a>1/16$, (17) implies

$$
\|\widehat Q_hV-VQ_h\|\le(8/a)e<2^7e.
\tag{20}
$$

No logarithm is approximated by a signed polynomial here.

On the hidden spaces set

$$
V_0=\widehat{\mathsf H}V\mathsf H,
\qquad B=\mathsf H(Q_0-Q_H+I)\mathsf H,
\qquad K=\mathsf H(Q_0+I)\mathsf H,
\qquad P=\mathsf H+K/2.
\tag{21}
$$

The diagonal $B$ has the endpoint barriers as entries. The map $V_0$ sends the target hidden constant to the rival hidden constant exactly. Its metric defect is bounded by

$$
\|V_0^*V_0-I_{\mathcal O\cap\operatorname{ran}\mathsf H}\|
\le\eta+e^2\le2^{141}\delta=:\eta_0,
\qquad \|V_0\|\le2.
\tag{22}
$$

Indeed, projecting away the rival visible component subtracts a positive term of norm at most $\|\widehat JV-VJ\|^2\le e^2$.

If $A$ is a full operator with target and rival norms at most $L$, compression changes its intertwining residual by at most $2Le$. Apply this elementary product expansion to $A=Q_0-Q_H+I$, whose norms are at most 64, and to $A=Q_0+I$, whose norms are at most 16. Equations (17) and (20) give the sufficient bounds

$$
\boxed{
\|\widehat B V_0-V_0B\|\le2^9e,
\qquad
\|\widehat P V_0-V_0P\|\le2^8e.}
\tag{23}
$$

All operators in (21) are restricted to the hidden spaces when used in (22)–(23). In particular, $P$ is a nonnegative Markov kernel, and ordinary reversibility makes it an $L^2(\mu)$ contraction because the hidden exit cap is two.

## 6. A stable bounded rational selector

Let $L_j$ be the six ordinary Lagrange polynomials on $\beta_0,\ldots,\beta_5$, and define

$$
D(x)=\sum_{r=0}^5L_r(x)^2,
\qquad R_j(x)=\frac{L_j(x)^2}{D(x)}.
\tag{24}
$$

Since $\sum_rL_r=1$, one has $D\ge1/6$. Thus $0\le R_j\le1$, $\sum_jR_j=1$, and $R_j(\beta_r)=\mathbf1_{j=r}$. These rational functions are well-defined on the entire rival interval $[0,1]$.

Only divided differences anchored at the six target nodes are needed:

$$
\boxed{
\sup_{x\in[0,1]}
\frac{|R_j(x)-\mathbf1_{j=r}|}{|x-\beta_r|}
<512.}
\tag{25}
$$

At $x=\beta_r$, use the continuous divided-difference value. To prove (25), the barycentric weights have magnitudes proportional to $(1,5,10,10,5,1)$, whose squares sum to 252. Put $d=|x-\beta_r|$ and $\Delta=1/16$. If $d\le\Delta/2$, then for $j\ne r$,

$$
\left|\frac{L_j(x)}{L_r(x)}\right|
\le\frac{2|w_j|d}{|w_r|\Delta}.
$$

Consequently

$$
1-R_r(x)\le
\min\{1,4S_rd^2/\Delta^2\},
\qquad S_r=\sum_{j\ne r}(w_j/w_r)^2\le251.
$$

The quotient by $d$ is at most $2\sqrt{S_r}/\Delta<512$. If $d>\Delta/2$, it is at most $1/d<32$. Finally $|R_j(x)-\mathbf1_{j=r}|\le1-R_r(x)$ for every $j$, proving the bound.

The target hidden subspace has six orthogonal barrier projectors $D_r$. Functional calculus gives, exactly,

$$
R_j(\widehat B)V_0-V_0R_j(B)
=\sum_{r=0}^5
\frac{R_j(\widehat B)-R_j(\beta_r)I}
{\widehat B-\beta_r I}
(\widehat B V_0-V_0B)D_r.
\tag{26}
$$

This is a finite-spectrum divided-difference identity; it does not assume that scalar Lipschitz functions are generally operator Lipschitz. Equations (23), (25), and Cauchy–Schwarz across the six orthogonal target projectors imply

$$
\boxed{\|R_j(\widehat B)V_0-V_0R_j(B)\|
\le\sqrt6\,512\,2^9e<2^{20}e.}
\tag{27}
$$

Every selector in (24)–(27) acts on the hidden space. Its extension to the visible state is zero, even when a rival has hidden barrier zero. In particular, one must not replace that extension by the unrestricted full-matrix function $R_j(B)$ at the visible zero eigenvalue.

## 7. Positive features and the state exclusion

On target and rival hidden spaces define

$$
g_i=2R_0(B)P R_i(B)1,\qquad
g_{5+i}=R_i(B)1,\qquad 1\le i\le5.
\tag{28}
$$

These are nonnegative functions on every rival. The selectors and $P$ are contractions, so $\|g_i\|_{\pi_0}\le2$. On the target the rational selectors are the exact label projectors, hence their hidden Gram is exactly the matrix $G_*$ in the [sharper finite obstruction](FINITE_GRAM_ROBUSTNESS.md#1-matrix-and-claim).

Because $V_0$ maps the hidden constant exactly, telescoping the three factors in (28), using (23) and (27), gives

$$
\|\widehat g_i-V_0g_i\|_{\widehat\pi_0}
\le2^{23}e=:v
\quad(1\le i\le10).
\tag{29}
$$

The hidden law is twice the hidden restriction of $\pi_0$. Using $\|V_0g_i\|\le4$ and (22), every hidden Gram entry therefore satisfies

$$
\begin{aligned}
|\langle\widehat g_i,\widehat g_j\rangle_{\widehat\mu}
-\langle g_i,g_j\rangle_\mu|
&\le16v+2v^2+8\eta_0\\
&\le2^{97}\sqrt\delta+2^{188}\delta.
\end{aligned}
\tag{30}
$$

At the sufficient accuracy $\delta_{\rm rat}=2^{-220}$,

$$
\boxed{\|\widehat G-G_*\|_{\max}
\le2^{-13}+2^{-32}<1/1500.}
\tag{31}
$$

An ordinarily reversible rival with at most eleven total states has at most ten hidden states. Its ten nonnegative feature vectors in (28) give a Gram factorization with at most ten nonnegative atoms. The established $1/1500$ obstruction contradicts (31). Therefore some mean in the explicit menu $\mathcal M$ must differ by more than $2^{-220}$.

The twelve-state target is itself admissible and ordinarily reversible. Thus its ordinary-reversible minimum is exactly twelve for every $0\le\delta\le2^{-220}$, already on this finite menu. The exact eleven-state stationary predictor gives the unrestricted sufficient count on the same menu and on all larger protocol tasks covered by its intertwining identity. If finite ordinary entropy production is desired at a positive error $\delta$, the earlier reverse-mixture construction with parameter $\delta/22$ still gives an eleven-state predictor with error at most $\delta/2$ throughout $|h|\le H$.

## 8. Interpretation and remaining limitation

The new recovery argument avoids the large off-grid values of squared Lagrange polynomials. It pays instead for a small singular value of a fixed, observable target basis. Both costs reflect the difficulty of distinguishing the six closely spaced kinetic labels, but the present result is a sufficient bound, not a lower bound on the best possible observation conditioning.

The proof does not use hidden-state observations, independent preparation of hidden labels, extra fields, shorter dwell times, a rival mass floor, a restricted rival label grid or a fitted family of candidate generators. Its finite list has 12,766 protocols rather than all binary words through its maximum horizon. The precision is nevertheless impractical, and no useful sampling guarantee follows. Improving the conditioning or finding a stronger direct finite-time certificate remains an open task. Manuscript drafting remains deferred.
