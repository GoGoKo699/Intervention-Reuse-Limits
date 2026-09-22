# Aggregation can require exponentially more states than a new reversible model

[Repository overview](../README.md) · [Uniform new-state upper bound](REGISTER_SCENERY_COMPRESSION.md) · [Fixed-clock transfer](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Prior-art assessment](PRIOR_ART.md)

**Research theorem, 22 September 2026.** There is a fixed six-level actuator family for which prediction by stationary-flux partition aggregation has a worst-case state cost singly exponential in a positive power of inverse error, while a newly constructed reversible model has polynomial cost. Both classes use the original exponential field rule, exact actuator histogram, fixed preparation and readout, and the same advertised internal spectral band. The aggregation lower bound concerns actual controlled means, and survives any fixed positive control clock.

The restriction is precise: an aggregate keeps $A$ separate, partitions hidden states into cells of constant actuator value, and uses the stationary intercell fluxes for its rates. The lower bound applies to **every** such partition, including partitions mixing configurations and addresses. It does not apply to arbitrary fitted rates on partition cells, or to general reversible surrogates. The distinction between aggregation and new-state realization is established; the candidate contribution here is the quantitative robust separation in this physical prediction problem.

## 1. Target family and main comparison

Fix $H,k>0$. For every $n\ge1$, put $r=2^n$. An address $a$ is a binary register indexed by $\mathbb Z_n$, and a configuration is a complete bit table $x=(x_a)_a\in\{-1,+1\}^r$. The hidden states are

$$
z=(x,a,j,\sigma),\qquad j\in\{1,2,3\},\quad \sigma\in\{-1,+1\},
\tag{1}
$$

with uniform stationary law $\mu$. The total physical count, including $A$, is $1+6r2^r$. Every table, address, port and sign coordinate is counted.

At the level of coordinate maps, let $R:i\mapsto i+1$, $J:i\mapsto-i-1$, $V=R\circ J:i\mapsto-i$, and let $X$ flip address bit $0$. The address maps

$$
U_1=J,\qquad U_2=V,\qquad U_3=X
$$

are involutions. Either cyclic rotation can be implemented by two of these involutions. Composition of backward pullback operators reverses the order of address maps; whenever an instruction word is used below, its order is chosen to give the stated pullback action.

Set $\lambda=1/8$ and define the local generator by

$$
\begin{aligned}
(Lf)(x,a,j,\sigma)={}&k\lambda[f(x,U_ja,j,\sigma)-f(x,a,j,\sigma)]\\
&+k\lambda\sum_{d\ne j}[f(x,a,d,\sigma)-f(x,a,j,\sigma)].
\end{aligned}
\tag{2}
$$

An involution fixed point contributes no jump. The local degree is at most three. The matching part has relaxation cap $2k\lambda$ and the complete three-port part has cap $3k\lambda$; hence $L$ has cap $5k/8$. Put

$$
K=L+\frac{3k}{2}(\Pi_\mu-I),\qquad
g(x,a,j,\sigma)=\sigma\gamma_jx_a,
\qquad (\gamma_1,\gamma_2,\gamma_3)=\frac1{10}(1,2,3).
\tag{3}
$$

The six actuator levels each have stationary mass $1/6$. Thus $G=3/10$, $\mu g=0$, and $W=\mu g^2=7/150$. The nonzero internal relaxation rates lie in $[3k/2,17k/8]$, and in particular in the advertised interval $[3k/2,5k/2]$. Global refresh makes all internal off-diagonal rates positive.

Attach $A$ using

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h}.
\tag{4}
$$

Use $S(A)=-1$, $S(z)=+1$, and preparation $\pi_0=(1/2,\mu/2)$. The targets are ordinarily reversible at each field, with the original equilibrium law. Their passive visible path law is exactly the rate-$k$ two-state telegraph law.

Let $D_{\rm agg}(\delta)$ be the worst-case minimal total state count over this family for the aggregation architecture defined in Section 2. Let $D_{\rm fresh}(\delta)$ instead allow new reversible states with (4), the exact six-level histogram and advertised band. Let $D_*(\delta)$ allow arbitrary finite Markov rivals with fixed preparation and fixed real readout. Error is uniform absolute error of the actual visible mean over all bounded deterministic piecewise-continuous protocols and all observation times. The combined lower and upper theorems give positive constants such that

$$
\boxed{
\begin{aligned}
c_0\delta^{-\gamma}&\le D_*(\delta)\le D_{\rm fresh}(\delta)\le C\delta^{-p},\\
\exp(c\delta^{-\alpha})&\le D_{\rm agg}(\delta)
\le\exp\!\left(C'\delta^{-p_6}\log\frac2\delta\right),\\
p&=\frac{\log96}{\beta},\qquad p_6=\frac{\log6}{\beta},\qquad
\beta=\log(1+2/(5R_H)),\quad R_H=e^{(1+G)H}.
\end{aligned}
}
\tag{5}
$$

for sufficiently small $\delta$. Both lower bounds already hold on thirteen fixed field values with every positive segment duration an integer multiple of any fixed $a/k$. Their witnessing horizons are $O_a(\log(1/\delta)/k)$. The upper bounds control the full protocol class. Thus unrestricted and fresh reversible prediction have polynomial growth, while this aggregation architecture has $\exp(\delta^{-\Theta(1)})$ growth. Exponents are unmatched, and (5) is not a cost of reversibility itself.

## 2. Precisely which aggregates are covered

A permitted partition keeps $A$ as one cell and refines all six sensitivity levels. Let $E$ be conditional expectation in $L^2(\pi_0)$, with range $\mathcal V$ the cell-constant functions. On hidden functions it is also conditional expectation in $L^2(\mu)$.

The aggregate's stationary weights are the cell masses and its internal generator is $EKE$ restricted to $\mathcal V$. Equivalently its intercell rates are stationary fluxes divided by the source cell mass. Attaching $A$ with (4) gives

$$
\widehat Q(h)=EQ(h)E\big|_{\mathcal V}.
\tag{6}
$$

The projection commutes with every sensitivity and port projector, preserves $A$, and fixes the readout and preparation. Dirichlet-form compression retains the upper cap and the supplied refresh retains the advertised lower endpoint. This architecture therefore preserves the physical constraints used in (5).

Cells can combine arbitrary configurations, addresses and signs whenever their sensitivities agree. No root-address measurability, equal cell sizes, or coordinatewise partition restriction is imposed. The requirement (6), rather than merely assigning new names to cells, is central to the theorem.

Set $k=1$ through Sections 3–8.

## 3. Physical fields expose the hidden operators

For a sensitivity level $\gamma$, let $X_\gamma$ have only row $A$ nonzero: its hidden entries are $\mu_z\mathbf1_{g_z=\gamma}$ and its $A$ diagonal is minus that level's mass. Let $Y_\gamma$ have entries $1$ in column $A$ and $-1$ on the diagonal at hidden rows of that level, and zeros elsewhere. Write $K_b$ for the full matrix with hidden block $K$ and all $A$ rows and columns zero. Exactly,

$$
Q(h)=K_b+\sum_\gamma e^{(1+\gamma)h}X_\gamma
              +\sum_\gamma e^{(\gamma-1)h}Y_\gamma.
\tag{7}
$$

The thirteen frequencies $0$ and $\gamma\pm1$ are distinct. Choose

$$
\bar h=\min\{H,1/[20(1+G)]\},\qquad h_i=i\bar h/12,
\quad i=0,\ldots,12.
\tag{8}
$$

The matrix with entries $e^{\omega h_i}$ is a Vandermonde matrix in the distinct numbers $e^{\omega\bar h/12}$. It is invertible. Thus $K_b$, every $X_\gamma$ and every $Y_\gamma$ are fixed real linear combinations of these thirteen physical generators. Coefficient bounds depend only on the fixed alphabet and $H$.

Put $X=\sum X_\gamma$ and $Y=\sum Y_\gamma$. For a full function $f$, $Xf$ is zero on hidden states and equals $\mu f_B-f_A$ at $A$; $Yf$ is zero at $A$ and equals $f_A-f_B$ on hidden states. Hence $YX+Y$ has hidden block $\Pi_\mu-I$ and zero $A$ blocks. The hidden-only local generator is exactly

$$
L_b=K_b-\frac32(YX+Y).
\tag{9}
$$

This identity holds on all full functions. On the invariant subspace of functions vanishing at $A$, $YX$ is $\Pi_\mu$, $-Y$ is the hidden identity, and $-Y_\gamma$ is the sensitivity projector.

Each $X_\gamma$ and $Y_\gamma$ commutes with $E$, since the partition preserves $A$, levels and stationary averaging. The same expressions in the aggregate therefore give $EL_bE$ exactly. Projectors used below are their hidden actions on the invariant $A$-zero subspace; they are not asserted to be orthogonal projectors on arbitrary full functions.

## 4. Partial isometries commute with the compression construction

Let $D_j$ select port $j$ on hidden functions. Its physical expression on the $A$-zero subspace is $-Y_{\gamma_j}-Y_{-\gamma_j}$. For $c\ne d$, define

$$
T_{cd}=\lambda^{-1}D_cLD_d,
\qquad
T_{jj}=\lambda^{-1}D_jLD_j+3D_j.
\tag{10}
$$

The first operator transports a function from port $d$ to port $c$, keeping its configuration, address and sign. The second applies $U_j$ within port $j$. Indeed $D_jLD_j=\lambda D_jU_jD_j-3\lambda D_j$, also at involution fixed points.

Every $T_{cd}$ has norm one and is an isometry on its specified input port. Its adjoint is $T_{dc}$; $T_{jj}$ is selfadjoint. These statements hold in $L^2(\pi_0)$ because all ports have equal stationary weights.

Substituting (9) and the physical expressions for $D_j$ gives generator polynomials of degree at most four and coefficient mass at most a fixed $C_T$. Since $E$ commutes with their diagonal factors, their aggregate evaluations are exactly

$$
\widehat T_{cd}=ET_{cd}E\big|_{\mathcal V}.
\tag{11}
$$

There is no assumption that $E$ commutes with a transport or address permutation. The partial-isometry argument below is what permits such arbitrary partitions.

## 5. Address features have observable palindrome norms

Every pure address translation $b\mapsto b\oplus a$ can be implemented with $n$ cyclic rotations and at most $n$ first-bit flips. To see this, perform one rotation and an optional flip in each of $n$ rounds. The final permutation is $R^n=I$; conjugating the flips through the rotations gives the independent flips at every coordinate. Choose their presence to realize $a$. Reversing the instruction order gives the desired backward pullback convention.

Each rotation costs two involutions. A gate $U_j$ can be applied while beginning and ending at port $1$ by transporting to port $j$, applying $T_{jj}$, and transporting back. Thus every pure translation has a word $W_a$ of at most $9n$ partial-isometry letters with a prescribed port itinerary. Consequently the features below obey a global identity, not only a root identity:

Define

$$
f_0(x,b,j,\sigma)=\mathbf1_{j=1}\sigma x_b,
\qquad f_a=W_af_0=\mathbf1_{j=1}\sigma x_{b\oplus a}.
\tag{12}
$$

The initial feature is cell measurable, so $Ef_0=f_0$. Every target word preserves its squared norm $\|f_0\|_{\pi_0}^2=1/6$. Independence of the complete uniform bit table additionally gives the exact Gram identity

$$
\langle f_a,f_c\rangle_{\pi_0}=\frac16\mathbf1_{a=c}.
$$

On the root set $\mathcal R=\{\text{address }0,\text{port }1\}$, including both signs,

$$
\pi_0(\mathcal R)=w=\frac1{6r},\qquad
f_a(x,0,1,\sigma)=\sigma x_a.
\tag{13}
$$

Let $Y_d=Y_{\gamma_1}-Y_{-\gamma_1}$. The physical endpoint identities are

$$
f_0=-\tfrac12Y_dS,\qquad
\pi_0Y_d=-f_0^T\operatorname{diag}(\pi_0).
$$

The $A$ component of the row identity vanishes by exact sign balance. Consequently

$$
\frac12\pi_0Y_dW_a^*W_aY_dS
=\|W_af_0\|_{\pi_0}^2=\frac16.
\tag{14}
$$

The adjoint word reverses the order and exchanges each transport with its reverse. Its aggregate evaluation gives $\|\widehat W_af_0\|^2$. Equation (14) is a scalar physical-mean generator polynomial of degree $O(n)$ and coefficient mass $e^{O(n)}$. It does not introduce a hidden-state measurement.

## 6. Norm loss forces retention of all address features

Write a word as $A_\ell\cdots A_1$, with $\ell\le9n$. Let $z_0=f_0$ and $z_i=EA_iz_{i-1}$. The aggregate vector always lies on the prescribed input port because $E$ preserves ports. Orthogonal projection and the isometry on that port give

$$
\|z_{i-1}\|^2-\|z_i\|^2
=\|(I-E)A_iz_{i-1}\|^2.
$$

The losses telescope:

$$
\sum_{i=1}^{\ell}\|(I-E)A_iz_{i-1}\|^2
=\frac16-\|z_\ell\|^2.
\tag{15}
$$

All letters are norm-one operators. Propagating the vector errors and using Cauchy–Schwarz therefore gives

$$
\|f_a-Ef_a\|^2\le\|f_a-z_\ell\|^2
\le9n\left(\frac16-\|z_\ell\|^2\right).
\tag{16}
$$

This is a bound from the actual aggregate palindrome deficit. It is not a separately imposed sufficient approximation certificate.

## 7. The root contains an independent bit cube

Suppose every address palindrome deficit is at most

$$
\varepsilon_n=\frac1{864nr}.
\tag{17}
$$

Summing (16) over the $r$ addresses yields

$$
\sum_a\|f_a-Ef_a\|^2\le\frac1{96}=\frac{wr}{16}.
\tag{18}
$$

Restrict this nonnegative loss to $\mathcal R$ and condition on the known sign $\sigma$. The real values $\sigma(Ef_a)(\text{cell})$ reconstruct the independent uniform bits $x_a$ with total mean squared error at most $r/16$. The root need not be a union of cells: conditioning gives a valid cell-index reconstruction even when cells also contain nonroot states.

Threshold each reconstruction at zero. A sign error costs at least one in squared error, so the average bit error is at most $1/16$. If $C$ is the cell index, the binary entropy bound and concavity imply

$$
H(x\mid C,\sigma,\mathcal R)\le r h_2(1/16)<3r/8.
$$

Since $H(x\mid\sigma,\mathcal R)=r$,

$$
\boxed{\log_2D\ge I(x;C\mid\sigma,\mathcal R)>5r/8,
\qquad D\ge2^{5r/8}.}
\tag{19}
$$

Using the total count including $A$ only weakens this hidden-cell lower bound. No constraint on cell sizes enters the argument.

## 8. Accuracy of actual means enforces the palindrome bound

Fix a clock $a>0$. Both target and aggregate have the same cap and original field rule. At the fields (8), their full spectra are contained in $[-5,0]$ and their reversible-norm comparisons cost at most $\kappa=e^{\bar h}$. The aggregate bounds follow from Dirichlet-form compression and its unchanged histogram. These are precisely the hypotheses used by the [whole-side logarithm transfer lemma](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md#3-a-general-lemma-for-total-degree-truncation).

For an address word take sides $P_L=\tfrac12Y_dW_a^*$ and $P_R=W_aY_d$. Each has degree at most $36n+1\le36(n+1)$ and coefficient mass at most $C_0^{n+1}$ for a fixed $C_0\ge1$. Put

$$
q_a=1-e^{-5a},\quad \varrho=\frac{1+1/q_a}{2},\quad
K_a=\frac\kappa a(\log2+5a),
$$

$$
B_a=C_0\max\{1,K_a\}^{36},\qquad
A_a=C_0\max\{1,(\log2)/a\}^{36}.
$$

Truncate each complete side logarithm series at total degree $M$. For each model the scalar palindrome truncation error is at most $3B_a^{2n+2}\varrho^{-(M+1)}$; each resulting propagator side has coefficient mass at most $J_n=4^MA_a^{n+1}$.

Choose the smallest nonnegative integer $M_n$ satisfying

$$
\varrho^{M_n+1}\ge\frac{12B_a^{2n+2}}{\varepsilon_n},
\qquad
\delta_n=\frac{\varepsilon_n}{2(4^{M_n}A_a^{n+1})^2}.
\tag{20}
$$

Then $M_n=O_{a,H}(n)$ and $\delta_n=e^{-\Theta_{a,H}(n)}$. Accuracy $\delta_n$ of the actual means bounds the difference of truncated palindromes by $\delta_nJ_n^2=\varepsilon_n/2$. The two truncation errors sum to at most the other $\varepsilon_n/2$. Every exact aggregate norm deficit is therefore at most (17), proving

$$
\boxed{D_{\rm agg,F_n}(\delta_n)\ge2^{5\cdot2^n/8}.}
\tag{21}
$$

The transfer is applied to both models, which is justified here by the specified aggregation architecture and its inherited cap. It is not an argument for an arbitrary unbounded-rate competitor. Only finitely many actual experiments are used, with fields (8), segment durations integer multiples of $a$, and horizons at most $2M_na$.

Restoring $k$ gives durations in multiples of $a/k$. There is a constant $C_a$ such that $\delta_n\ge e^{-C_a(n+1)}$. For any sufficiently small $\delta$, choose $n=\lfloor\log(1/\delta)/C_a\rfloor-1$. Then $\delta\le\delta_n$ and $2^n\ge c'\delta^{-\log2/C_a}$. Applying (21) at that target proves the aggregation lower bound in (5) for all sufficiently small accuracies, not only a subsequence.

### 8.1. A polynomial lower bound for arbitrary new-state rivals

The exact Gram identity in Section 5 gives a second lower bound with a larger competitor class. The $r\times r$ physical matrix

$$
\mathcal G_{ac}=\tfrac12\pi_0Y_dW_a^*W_cY_dS
=\tfrac16\mathbf1_{a=c}
$$

has smallest singular value $1/6$. Use the same side-polynomial degree and coefficient bounds, but truncate only the target logarithm expansions, at a degree $M'_n$ satisfying

$$
\varrho^{M'_n+1}\ge36rB_a^{2n+2}.
$$

The matrix error is at most $3rB_a^{2n+2}\varrho^{-(M'_n+1)}\le1/12$. Its truncated smallest singular value is therefore at least $1/12$. Each side has propagator coefficient mass at most $J'_n=4^{M'_n}A_a^{n+1}$.

Evaluating these same finite propagator polynomials in any $D$-state rival gives a matrix factoring through $D$ coordinates. If $D<r$, actual-mean accuracy must satisfy

$$
\delta\ge\frac1{12r(J'_n)^2}=e^{-O_{a,H}(n)}.
$$

In particular, at accuracy $1/[24r(J'_n)^2]$, strictly below the displayed obstruction threshold, every rival needs at least $r$ states. No rival generator is expanded or logarithmically transformed in this argument. Its rates can be unbounded and nonanalytic in the field; reversibility, exact passive agreement and the original field rule are unnecessary. The usual choice of $n$ proportional to $\log(1/\delta)$ gives the polynomial minimax lower in (5), on the same fixed clock and field menu.

## 9. Why new reversible states avoid the aggregation cost

At the witness accuracy $\delta_n$, the existing exact whole-component prefix selection already gives a small new-state model. A fixed configuration and sign have at most $3r$ local states. Selecting at most $6^{\ell+1}$ whole components preserves an $\ell+1$ local prefix exactly. Restoring the supplied refresh and using the original field rule gives

$$
D\le1+3r6^{\ell+1},\qquad
\text{mean error}\le(1+2R_H^2)
\left(\frac{(5/2)R_H}{1+(5/2)R_H}\right)^{\ell+1}.
\tag{22}
$$

Taking $\ell=O(\log(1/\delta_n))=O(n)$ makes this count polynomial in $1/\delta_n$. These new states are selected components with adjusted positive weights, not cells carrying the original stationary fluxes.

The [companion address-dictionary compression theorem](REGISTER_SCENERY_COMPRESSION.md) strengthens (22) to the uniform all-width upper in (5). Its additional step replaces a wide address register by width $n_0=O(\log(1/\delta))$ before selecting configurations. Short words in the two coordinate reflections and the first-bit toggle are affine-dihedral transformations. On a uniform long binary register, a nonidentical short transformation fixes the address with probability at most $2^{-(n-2)/2}$. A union bound over trajectory pairs controls all short scenery coincidences. This gives a finite reference dictionary independent of the original width, followed by the same positive component selection.

That proof supplies $D\le C\delta^{-\log96/\beta}$, with $\beta=\log(1+2/(5R_H))$, uniformly over all $n$. The full iid bit table in each original target is essential and counted. The theorem is not an arbitrary frozen-label compression claim.

For the aggregation upper in (5), apply the existing [reversible prediction partition](BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) with $m=6$ and $\Lambda=5/2$. That construction refines the actuator levels and uses exactly the stationary-flux generator $EKE$, so it belongs to the present architecture. Its count is $\exp[C'\delta^{-p_6}\log(2/\delta)]$. Moreover, the target's Dirichlet inequality $-K\succeq(3k/2)(I-\Pi_\mu)$ restricts to the cell-constant subspace, preserving the advertised lower gap as well as the cap. Together with (21), this establishes the stated exponential growth class for aggregation, with unmatched powers.

## 10. Scope, proof audits and verification

This is an architecture lower bound for every exact-actuator stationary-flux aggregate. It is stronger than failure of a particular partition-finding algorithm or of a sufficient reconstruction criterion: actual controlled-mean accuracy itself forces (18). It remains narrower than a lower bound on general reversible realizations, as demonstrated by the upper theorem on the same family.

The six fixed actuator values are intentional. No binary-alphabet reduction is claimed. The large exponent and constants are sufficient bounds, not practical state budgets. Constructors know the supplied target; learning, parameter precision and efficient computation are outside the result.

The extraction identities, invariant $A$-zero subspace, compression-compatible port operators, norm telescoping, physical endpoints, root-conditioned entropy bound and two-model fixed-clock transfer have passed independent internal proof checks. The [exact verifier](../scripts/verify_aggregation_state_lower_bound.py) and [saved report](../reports/aggregation_state_lower_bound.json) supplement those arguments; finite checks do not certify all dimensions or publication novelty. The [prior-art assessment](PRIOR_ART.md) distinguishes this quantitative claim from established model aggregation, positive realization and rate-distortion arguments.
