# Why the finite observation certificate remains poorly conditioned

[Finite construction](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Sharper Gram obstruction](FINITE_GRAM_ROBUSTNESS.md) · [Research roadmap](PRL_EXPLORATION.md)

**Research boundary, 23 September 2026.** The small state advantage uses six distinct kinetic labels and exact nonnegative diagonal selectors. Within this particular polynomial-selector construction, degree ten is necessary, and the unique selectors of that degree become large at permitted off-grid rival barriers. This identifies a limitation of the present proof architecture. It is not a lower bound on attainable measurement precision, the best reversible prediction error, or all possible observation certificates.

## 1. The minimum degree of an exact positive selector

Let $\beta_0,\ldots,\beta_{m-1}$ be distinct points in the interior of an interval $[\ell,u]$. Suppose a real polynomial $p_j$ obeys

$$
p_j(x)\ge0\quad(\ell\le x\le u),\qquad
p_j(\beta_r)=\mathbf1_{r=j}.
\tag{1}
$$

Every zero at $\beta_r$ with $r\ne j$ has even multiplicity: an odd-multiplicity real root in the interior changes the sign of the polynomial. There are $m-1$ such distinct roots and $p_j$ is nonzero, so

$$
\deg p_j\ge2(m-1).
\tag{2}
$$

If equality holds, every required root has multiplicity exactly two and there are no additional factors. The normalization at $\beta_j$ fixes the coefficient. Thus the unique minimum-degree selector is

$$
p_j(x)=\prod_{r\ne j}\left(\frac{x-\beta_r}{\beta_j-\beta_r}\right)^2=L_j(x)^2.
\tag{3}
$$

The positivity requirement in (1) corresponds to arbitrary rival endpoint barriers throughout $[\ell,u]$. Requiring positivity only on the six target values would change the rival class. The argument concerns scalar polynomials in the return diagonal alone; it does not restrict functions involving other operators, approximate selectors, rational functions or direct finite-time witnesses.

## 2. The actual six-label grid

For the unchanged target, $\beta_j=(6+j)/16$ for $0\le j\le5$, all strictly inside $[0,1]$. Equations (2)–(3) give minimum degree ten. For $j=2$,

$$
\prod_{r\ne2}(\beta_2-\beta_r)=-\frac3{262144},
\qquad
[x^{10}]\,p_2(x)=\frac{68719476736}{9},
\qquad
p_2(0)=12006225.
\tag{4}
$$

Consequently the sum of absolute monomial coefficients of this selector is at least $68719476736/9$, and its supremum on the permitted rival interval is at least $12006225$. Strictly positive rival barriers do not remove the supremum, since values arbitrarily close to zero are still allowed.

These are properties of the exact degree-ten selectors, not estimates of the actual response of a fitted rival. In particular, the large values do not prove that a rival matching the target's means can reach these extremes. Nor do they supply a lower bound on the conditioning of every way to recover the desired Gram matrix. They explain why reducing a few constants in the existing coefficient-mass estimate is unlikely, by itself, to produce an experimentally useful certificate.

The [sharper matrix obstruction](FINITE_GRAM_ROBUSTNESS.md) raises the tolerated intermediate Gram error from $1/40000$ to $1/1500$. That improvement and the large observation amplification are separate quantities. A tolerance of $1/1500$ for measured means does not follow.

## 3. A bounded rational alternative, with an unresolved observation step

The same interpolation polynomials provide exact bounded selectors if normalization is allowed. Define

$$
D(x)=\sum_{r=0}^{m-1}L_r(x)^2,\qquad
R_j(x)=\frac{L_j(x)^2}{D(x)}.
\tag{5}
$$

Lagrange interpolation of the constant function gives $\sum_rL_r(x)=1$. Cauchy–Schwarz therefore implies

$$
D(x)\ge\frac1m>0\quad\text{for every real }x.
\tag{6}
$$

It follows that $0\le R_j(x)\le1$, $\sum_jR_j(x)=1$ and $R_j(\beta_r)=\mathbf1_{j=r}$. Applied to a rival's diagonal barrier matrix, these functions remain nonnegative and selfadjoint and become the same exact projectors on the target. Replacing the original selectors by $R_j(B)$ thus preserves the target Gram and the abstract positive-factorization argument.

The outstanding step is quantitative recovery of the resulting rational operator words from the allowed controlled means. Boundedness of $R_j(B)$ alone supplies no such observation inequality. In particular, multiplying a measured scalar by an inverse denominator is not the same as inserting the inverse diagonal operator $D(B)^{-1}$ inside a word. No improved controlled-mean tolerance or experiment count is claimed for (5).

This alternative gives a concrete next analytic task: control the entire bounded rational word in the same two-field experiment class, or construct a certificate directly from finite-time probabilities. A change to independently addressable kinetic gates would instead change the control resource and must be evaluated as a separate model. Manuscript drafting remains deferred.

## 4. A strong physical gate retains reinjection

A physical gate that increases return to the visible state also increases entry when its equilibrium bias is held fixed. Its compressed propagator therefore need not approximate a killed propagator. The following exact toy calculation isolates this distinction.

Take a hidden probability law $\mu$, a nonempty set $C$ of hidden states with mass

$$
m=\sum_{i\in C}\mu_i>0,
$$

and set the hidden generator to $K=0$. For gate strength $\kappa>0$ and fixed equilibrium ratio $r>0$, use

$$
q_{iA}=\kappa\mathbf1_{i\in C},\qquad
q_{Ai}=r\kappa\mu_i\mathbf1_{i\in C}.
\tag{7}
$$

Other off-diagonal rates vanish and diagonal entries make row sums zero. This is a reversible star on $\{A\}\cup C$, with any hidden states outside $C$ isolated. In particular, this $K=0$ toy has no positive hidden relaxation gap and is **not** a member of the hard target family with band $[k,3k]$.

Let $J$ project onto $A$, let $\mathsf H=I-J$, and let $1_C$ be the indicator of $C$, extended by zero at $A$. Starting at any $i\in C$, the aggregate membership process on $\{A,C\}$ has rates $A\to C=r\kappa m$ and $C\to A=\kappa$. Thus its probability of being in $C$ at time $t$ obeys

$$
\dot z=r\kappa m(1-z)-\kappa z,\qquad z(0)=1.
$$

Solving gives the exact constant-$C$ mode of the compressed physical propagator:

$$
\boxed{
\mathsf H e^{tQ}\mathsf H\,1_C
=\lambda_C(t)1_C,\qquad
\lambda_C(t)=
\frac{rm+e^{-\kappa(1+rm)t}}{1+rm}.}
\tag{8}
$$

The constant outside-$C$ modes are unchanged. More explicitly, on the hidden space let $D_C$ be multiplication by $1_C$ and let

$$
(\Pi_C f)_i=\frac{\mathbf1_{i\in C}}m
\sum_{j\in C}\mu_j f_j.
$$

Then

$$
\mathsf H e^{tQ}\mathsf H
=D_{C^c}+e^{-\kappa t}(D_C-\Pi_C)+\lambda_C(t)\Pi_C.
\tag{9}
$$

The centered modes on $C$ decay at rate $\kappa$ because the return through $A$ depends only on the $\mu$-weighted mean. By contrast, a process killed on jumping to $A$ has hidden propagator $D_{C^c}+e^{-\kappa t}D_C$: it excludes every path that leaves $C$ and subsequently reenters. The outer projections in (8) exclude only an endpoint at $A$ and do not exclude those return paths.

In $L^2(\mu)$, (8) implies

$$
\left\|\mathsf H e^{tQ}\mathsf H-D_{C^c}\right\|
\ge\lambda_C(t)\ge\frac{rm}{1+rm}.
\tag{10}
$$

At $r=4$ and $m=1/2$, the limiting constant-mode survival as $\kappa t\to\infty$ is $2/3$. Increasing the gate strength at fixed $r$ therefore cannot turn this single compressed physical pulse into the complementary label projector. Repeated hidden projections or a different equilibrium bias are different operations; their availability and scalar-recovery costs require separate analysis.

This calculation excludes only that simple physical-pulse-to-killing substitution. It is neither a measurement-conditioning lower bound nor an obstruction to all finite-time observables, rational recovery methods, multi-pulse protocols or alternative positive feature constructions.
