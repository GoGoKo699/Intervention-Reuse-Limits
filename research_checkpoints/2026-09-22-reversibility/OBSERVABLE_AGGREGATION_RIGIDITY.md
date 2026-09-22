# Controlled means force preservation of observable generator words

[Repository overview](../../README.md) · [Stochastic aggregation application](SOFT_AGGREGATION_LOWER_BOUND.md)

**Recovered proof note, 22 September 2026.** Consider an ordinarily reversible target with the original exponential field rule, and its exact-actuator stationary-flux partition aggregate. Uniform accuracy of actual controlled means forces every bounded-length observable generator word to be close to the aggregate's function space. The exponent of the prediction error can be chosen independently of word length and state count.

The proof uses an auxiliary selfadjoint path matrix, a positive Ritz resolvent deficit, fixed-clock logarithm expansions, and a polynomial coefficient bound. The auxiliary matrix does not enlarge the physical competitor.

## 1. Statement and constants

Use dimensionless generators $Q(h)/k$, denoted simply by $Q(h)$. Assume the hidden generator is reversible and has relaxation cap $\Lambda$, with $|g|\le G$. Keep the visible state separate and partition hidden states only within actuator levels. Let $E$ be conditional expectation in $L^2(\pi_0)$. The aggregate is
$$
\widehat Q(h)=EQ(h)E\big|_{\operatorname{ran}E}.
$$
Write $e=\mathbf1_A$, so $Ee=e$.

Fix $H,a>0$. Suppose actual-mean error is at most $\delta\in(0,1)$ on every protocol from a specified field menu in $[-H,H]$, with segment lengths integer multiples of $a$, allowing an arbitrarily long initial hold at $H$.

There are explicit $C,F,\kappa>0$, independent of state count, partition, and word length, such that
$$
\boxed{\;
\|(I-E)A_L\cdots A_1e\|_{\pi_0}
\le CF^L\delta^\kappa ,
\;}
\tag{1}
$$
where each $A_i$ is a menu generator or its $L^2(\pi_0)$ adjoint.

One admissible choice is
$$
R=e^{(1+G)H},\quad
B_{\mathrm{sp}}=2(\Lambda+R),\quad
\chi=e^H,\quad B_0=\chi B_{\mathrm{sp}},
$$
$$
q=1-e^{-aB_{\mathrm{sp}}},\qquad
\rho=\frac{1+q}{2},\qquad r_0=\frac q\rho,
$$
$$
K_0=2(1+e^{2H})^2,\qquad D_0=\frac{16K_0}{\rho},
$$
$$
t_0=\min\!\left\{\frac1{64},
\frac{aB_0}{8\chi\log(1/(1-\rho))}\right\},
\qquad
\theta=\frac{\log(1/r_0)}{\log(D_0/r_0)}.
$$
Finally set
$$
C_A=\frac{3}{2\tanh H},\quad
C_3=\sqrt{\frac{4C_A+2}{1-t_0}},\quad
\zeta=1-\frac{\log6}{\log(1/t_0)},
$$
$$
C=9C_3^\zeta,\qquad
F=\frac{2B_0}{t_0},\qquad
\kappa=\frac{\theta\zeta}{2}.
\tag{2}
$$
All quantities are finite and positive; $t_0\le1/64$ ensures $\zeta>0$.

For a generator polynomial of degree at most $L$ and coefficient mass $J$, the right side of (1) becomes $CJF^L\delta^\kappa$.

## 2. From physical means to visible return scalars

Let $t=\tanh H$. The prescribed equilibrium distributions satisfy
$$
\delta_A=(1+t^{-1})\pi_0-t^{-1}\pi_H.
\tag{3}
$$
An arbitrarily long initial hold at $H$, along integer clock multiples, prepares $\pi_H$ in both models. This follows from irreducibility of the full physical generators, whose visible-to-hidden rates are positive.

For every legal propagator word $W$, (3), the identity $e=(1-S)/2$, and $\pi_0(A)=1/2$ therefore give
$$
\left|\langle e,We\rangle_{\pi_0}
-\langle\widehat e,\widehat W\widehat e\rangle_{\widehat\pi_0}\right|
\le C_A\delta.
\tag{4}
$$
This is a consequence of actual-mean accuracy, not an additional observation assumption.

Adjoints have the physical representation
$$
Q(h)^*=M_hQ(h)M_h^{-1},
\qquad
M_h=I+(e^{-2h}-1)P_A,
\tag{5}
$$
where $P_A$ is the orthogonal visible-state projector. Since $E$ commutes with $P_A$, the same identity holds after compression. Insertions of $P_A$ split an $e$-to-$e$ scalar into products of visible return probabilities. Equation (4) consequently controls the expanded scalars appearing below.

## 3. A selfadjoint path matrix and its Ritz deficit

For a word of length $L$, use $L+1$ auxiliary clock sites and define a selfadjoint block matrix $T$ by
$$
T_{i,i-1}=\frac{A_i}{2B_0},
\qquad
T_{i-1,i}=\frac{A_i^*}{2B_0},
\quad 1\le i\le L.
$$
The full field spectrum lies in $[-B_{\mathrm{sp}},0]$, and change of reversible norm costs at most $\chi$. Thus $\|A_i\|\le B_0$, and the row/column Schur bound gives $\|T\|\le1$.

Let
$$
P=I_{\mathrm{clock}}\otimes E,\qquad b=|0\rangle\otimes e.
$$
The aggregate path matrix is exactly $PTP$ on $\operatorname{ran}P$. This is compression of a generator construction; no identity between a compressed propagator and the propagator of a compression is used.

For real $|t|\le t_0$, define
$$
\Delta(t)=
\langle b,(I-tT)^{-1}b\rangle
-
\langle b,(I-tPTP)^{-1}b\rangle.
$$
The variational identity for the positive operator $I-tT$ gives
$$
\Delta(t)\ge
(1-|t|)\,
\|(I-P)(I-tT)^{-1}b\|^2.
\tag{6}
$$

## 4. A uniform fixed-clock bound on the scalar deficit

For a physical generator put
$$
U_h=I-e^{aQ(h)}.
$$
Reversibility gives, for every $m\ge1$,
$$
\|U_h^m\|_{\pi_0}\le\chi q^m,
\qquad
Q(h)=-\frac1a\sum_{m\ge1}\frac{U_h^m}{m}.
\tag{7}
$$
The factor $\chi$ is paid once per logarithm block, not once per power inside that block.

Expand the path resolvent using (7), and mark total logarithm degree. At degree weight $\rho$, each generator block has majorant
$$
Z=\frac{\chi}{a}\log\frac1{1-\rho}.
$$
By the choice of $t_0$, the clock-path row/column majorant is at most $1/8$. Its resolvent majorant is therefore less than two, uniformly in the number of clock sites. Truncating at total degree $M$ has operator tail at most $2r_0^{M+1}$ in either model.

For completeness, the retained scalar error has the bound
$$
2C_AD_0^M\delta.
$$
Indeed a term of total degree $m$ expands into semigroup words with coefficient factor at most $2^m$. Expanding (5) contributes at most $(1+e^{2H})^{2m}$. Visible projectors split the scalar into products of return probabilities; telescoping their differences costs at most $2m+1\le3^m$ for $m\ge1$. The degree-weighted majorant absorbs the remaining coefficients, and $D_0$ dominates all these factors. The degree-zero term agrees exactly.

Taking
$$
M=\left\lfloor
\frac{\log(1/\delta)}{\log(D_0/r_0)}
\right\rfloor
$$
therefore gives, uniformly on $[-t_0,t_0]$,
$$
0\le\Delta(t)\le(4C_A+2)\delta^\theta.
\tag{8}
$$
Combining (6) and (8),
$$
\|F(t)\|\le\varepsilon:=C_3\delta^{\theta/2},
\qquad
F(t)=(I-P)(I-tT)^{-1}b.
\tag{9}
$$

## 5. Recovering a word from the resolvent

Write
$$
F(t)=\sum_{j\ge0}t^jv_j,\qquad
v_j=(I-P)T^jb.
$$
Since $\|T\|\le1$, every $\|v_j\|\le1$.

The following coefficient estimate follows from (9):
$$
\|v_L\|\le9t_0^{-L}\varepsilon^\zeta.
\tag{10}
$$
Here is an elementary proof. If $0<\varepsilon<1$, put
$$
N=\left\lfloor
\frac{\log(1/\varepsilon)}{\log(1/t_0)}
\right\rfloor .
$$
The degree-$N$ Taylor polynomial of $F(t_0x)$ has norm at most $3\varepsilon$ on $[-1,1]$, because its tail is at most
$t_0^{N+1}/(1-t_0)<2\varepsilon$.
Its vector-valued Chebyshev coefficients have norms at most $6\varepsilon$. The sum of absolute monomial coefficients of the $j$-th Chebyshev polynomial is at most $3^j$. Thus every monomial coefficient of this Taylor polynomial has norm at most
$$
9\varepsilon\,3^N
\le9\varepsilon^\zeta.
$$
This proves (10) for $L\le N$. For $L>N$, use $\|v_L\|\le1$ and $t_0^L<\varepsilon$. The case $\varepsilon\ge1$ is immediate.

The clock-$L$ component of $T^Lb$ has only one contributing path: it moves forward at every step. Hence it equals
$$
(2B_0)^{-L}A_L\cdots A_1e.
$$
Applying (10) to that component proves (1) with (2).

The exponent $\kappa$ does not deteriorate with $L$. Word length enters only through the exponential factor $F^L$. This distinction allows exponentially many query features of length $O(n)$ to be retained at accuracies $e^{-O(n)}$.

The theorem requires the specified stationary-flux compression and common physical structure. It does not compare arbitrary fitted reversible generators. The equilibrium-calibration step also means that this version assumes accuracy over all horizons.
