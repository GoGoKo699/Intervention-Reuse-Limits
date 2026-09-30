# Whole-word repair after a positive change of measure

[Binary uncapped theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) · [Binary fixed-budget proof](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Whole-word repair](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) · [Mixed bounded observations](MIXED_KILLED_WORD_OBSERVABILITY.md)

**Research lemma, 23 September 2026.** The positive normalization used in the binary proof can be combined with whole-word repair without a global operator-norm bound. The normalization mass may depend on target width and become small. This lemma is an algebraic interface; a physical construction must still supply every scalar hypothesis with an explicit accuracy budget.

## 1. Hypotheses on one finite probability space

Let $`\mu`$ be a strictly positive probability law on a finite set. Adjoint and norm notation refer to $`L^2(\mu)`$. Let $`A`$ be entrywise nonnegative and selfadjoint, and set

**Equation (1).**

```math
u=A1,\qquad Z=\|u\|_\mu^2\gt 0,\qquad \mathcal S=\{i:u_i\gt 0\}.
```

Here $`u`$ is a vector; the changed probability below is denoted by $`\nu`$. Let $`v_b,q_b`$ be real vectors supported on $`\mathcal S`$, with $`|v_b|\le q_b`$. Let $`C_c`$ be nonnegative kernels supported on $`\mathcal S\times\mathcal S`$. For example, kernels with an outer factor $`A`$ on both sides have this support: a zero row sum of the nonnegative $`A`$ implies a zero row, and selfadjointness implies a zero column.

For $`r`$ query indices, put $`\sigma_{bc}=(-1)^{\mathbf1_{b=c}}`$. Suppose $`0\le\Delta\le1`$ and

**Equation (2).**

```math
\begin{aligned}
\|q_b-u\|_\mu^2&\le Z\Delta,
&\left|\|v_b\|_\mu^2-Z\right|&\le Z\Delta,\\
\|C_cu-u\|_\mu^2&\le Z\Delta,
&\|C_c^*u-u\|_\mu^2&\le Z\Delta,\\
\|C_cv_b\|_\mu^2&\le Z(1+\Delta),
&\sigma_{bc}\langle v_b,C_cv_b\rangle_\mu&\ge Z(1-\Delta).
\end{aligned}
```

There is no lower bound on the coordinates of $`u`$, and no bound on $`\|A\|`$, $`\|C_c\|`$, or raw row sums.

## 2. A rate-independent state-count conclusion

Define on $`\mathcal S`$

**Equation (3).**

```math
\nu_i=\frac{\mu_i u_i^2}{Z},\qquad
\widetilde v_b(i)=\frac{v_b(i)}{u_i},\qquad
\widetilde q_b(i)=\frac{q_b(i)}{u_i},\qquad
\widetilde C_c(i,j)=\frac{C_c(i,j)u_j}{u_i}.
```

The map $`f\mapsto uf/\sqrt Z`$ is an isometry from $`L^2(\nu)`$ to the supported subspace of $`L^2(\mu)`$. It intertwines kernels and stationary adjoints. Thus (2) becomes

**Equation (4).**

```math
\begin{aligned}
\|\widetilde q_b-1\|_\nu^2&\le\Delta,
&\left|\|\widetilde v_b\|_\nu^2-1\right|&\le\Delta,\\
\|\widetilde C_c1-1\|_\nu^2&\le\Delta,
&\|\widetilde C_c^*1-1\|_\nu^2&\le\Delta,\\
\|\widetilde C_c\widetilde v_b\|_\nu^2&\le1+\Delta,
&\sigma_{bc}\langle\widetilde v_b,\widetilde C_c\widetilde v_b\rangle_\nu&\ge1-\Delta.
\end{aligned}
```

Also $`|\widetilde v_b|\le\widetilde q_b`$. Clip $`\widetilde v_b`$ to $`h_b\in[-1,1]`$. With $`\varepsilon=\sqrt\Delta`$,

**Equation (5).**

```math
\|\widetilde v_b-h_b\|_\nu\le\|\widetilde q_b-1\|_\nu\le\varepsilon.
```

The proof of [whole-word repair, Section 2](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md#2-whole-word-repair-using-measured-vector-norms) uses the query kernel only to establish this clipping estimate. Apply its balanced-flux repair separately to each entire $`\widetilde C_c`$. It produces stationary Markov kernels $`U_c`$ on the same set, with

```math
\sum_{i,j}\nu_i|\widetilde C_c(i,j)-U_c(i,j)|\le3\varepsilon.
```

The measured image norm in (4) controls one endpoint replacement; positivity and the adjoint row norm control the other. Consequently the same calculation gives

**Equation (6).**

```math
\|h_b\|_\nu^2\ge1-4\varepsilon,\qquad
\sigma_{bc}\langle h_b,U_ch_b\rangle_\nu\ge1-8\varepsilon.
```

Rounding $`Z_b=\mathrm{sign}(h_b)`$, with zero rounded to $`+1`$, gives a deterministic $`r`$-bit function of one actual state. The stationary coupling associated with $`U_c`$ fails the requested flip in coordinate $`b`$ with probability at most $`8\varepsilon`$. Hence the law $`\rho`$ of the decoded vector obeys

**Equation (7).**

```math
\mathrm{TV}(\rho,\mathrm{flip}_c\rho)\le8r\varepsilon,
\qquad
\log_2|\mathcal S|\ge H(\rho)\ge r(1-8r\varepsilon).
```

In particular,

**Equation (8).**

```math
\sqrt\Delta\le\frac1{32r}\quad\Longrightarrow\quad
|\mathcal S|\ge2^{3r/4}.
```

No states were added. The repaired kernels are proof couplings, not additional controls or a fitted physical generator.

## 3. Observable scalar bookkeeping

A useful realization is $`A=A_++A_-`$ with nonnegative selfadjoint $`A_\pm`$. Put $`v=(A_+-A_-)1`$, so $`|v|\le u`$ exactly. For a positive query word $`Q_b`$ with the appropriate outer support, set

**Equation (9).**

```math
v_b=Q_bv,\qquad q_b=Q_bu.
```

Then $`|v_b|\le q_b`$ without a pointwise ratio estimate. Every quantity in (2) is an ordinary hidden word scalar. For example,

**Equation (10).**

```math
\|C_cu-u\|_\mu^2
=\mu A C_c^*C_c A1-2\mu A C_c A1+\mu A^2 1.
```

The middle scalar is real, so its adjoint has the same value. Products, reversals and the two signed endpoint choices account for all other expressions. There is no coordinatewise multiplication of unknown rival query functions in this interface.

Suppose the target normalization is $`Z_n\gt 0`$. To infer (2) from mean measurements, control $`|Z-Z_n|`$ as well as each unnormalized scalar defect. A bound $`|Z-Z_n|\le Z_n/2`$ gives $`Z\ge Z_n/2`$. Absolute scalar error of order $`Z_n\Delta`$ is then sufficient, after adding the target's own approximation errors and the finite coefficient masses. If $`Z_n\ge e^{-C(n+1)^a}`$ and all scalar recovery costs are exponential in a polynomial of $`n`$, this normalization retains that form. A fixed positive root mass is convenient but is not required by the algebra.

## 4. Partial flips can also force exponentially many states

The negative correlation used by the existing exact-flip construction is not necessary for every entropy argument.

**Lemma.** Let $`Z`$ be a random vector in $`\{-1,+1\}^r`$. For each coordinate $`c`$, suppose a coupling $`(Z,Z^{(c)})`$ has both marginals equal to the law of $`Z`$. Define

```math
p_c=\Pr\{Z_c\ne Z_c^{(c)}\},\qquad
e_c=\Pr\{Z_{-c}\ne Z_{-c}^{(c)}\}.
```

Then

**Equation (11).**

```math
H(Z)\ge\sum_{c=1}^r H(Z_c\mid Z_{-c})
\ge\sum_{c=1}^r(p_c-e_c).
```

To prove the second inequality, fix a value $`w`$ of the other coordinates and let $`a_w,b_w`$ be the two joint probabilities of $`(Z_{-c},Z_c)=(w,\pm1)`$. Each directed coupling flow that changes $`c`$ while retaining $`w`$ is at most $`\min(a_w,b_w)`$, because the two marginals agree. Therefore the total probability of changing only $`c`$ is at most $`2\sum_w\min(a_w,b_w)`$. The binary entropy inequality $`h_2(t)\ge2\min(t,1-t)`$ bounds this by $`H(Z_c\mid Z_{-c})`$. Finally, the probability of changing only $`c`$ is at least $`p_c-e_c`$. The first inequality in (11) follows from the entropy chain rule and reduction of entropy by conditioning.

For example, on a uniformly distributed bit table, the lazy flip $`(I+F_c)/2`$ is a positive-semidefinite stationary Markov kernel. It changes bit $`c`$ with probability $`1/2`$ and leaves all other bits fixed. Equation (11) still forces at least $`2^{r/2}`$ states for any deterministic decoding with those couplings. Thus positive semidefiniteness alone does not preclude every exponential entropy lower bound. It does preclude reproducing the negative scalar of the earlier specific exact-flip gadget.

In an approximate application, controlling each unintended bit-change probability separately only gives $`e_c\le\sum_{b\ne c}\Pr\{Z_b\ne Z_b^{(c)}\}`$. The factor proportional to the number of queried bits has not been removed. A target with persistent reset noise therefore needs a separate quantitative argument; a small negative scalar or partial-flip example does not establish the binary uncapped theorem.
