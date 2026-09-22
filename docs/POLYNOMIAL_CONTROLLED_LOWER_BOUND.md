# Polynomial state cost for controlled finite-field prediction

[Repository overview](../README.md) · [Positive shift-register target](SHIFT_REGISTER_LOWER_BOUND.md) · [Polynomial upper bound](BOUNDED_RATE_FINITE_FIELD.md) · [Earlier tree construction](GENERAL_CONTROLLED_LOWER_BOUND.md)

**Research theorem, 22 September 2026.** The positive shift-register targets admit a polynomial lower bound in inverse prediction error, even when control changes must respect any fixed positive dwell time. The proof truncates a logarithm expansion by total degree across each complete left or right observable word. This keeps both the experiment coefficient cost and the witness conditioning exponential in word length. It strengthens the earlier interpolation bounds without changing the physical target.

Together with the bounded-rate finite-alphabet upper theorem, this determines the unrestricted-predictor complexity of the binary capped class as $\delta^{-\Theta(1)}$. The upper and lower exponents are not matched. No polynomial reversible upper bound or optimal exponent is established. The logarithm series and coefficient majorants are standard ingredients; the controlled prediction application below is an internal derivation, not a certification of originality.

## 1. Statement and experiment class

Fix $k>0$, $H>0$, and $0<W\le G^2$. Put $s=\sqrt W$ and

$$
h_* =\min\{H,1/[20(1+s)]\}>0.
$$

Consider the original reversible target family with actuator values $g=\pm s$, each having stationary mass $1/2$, and nonzero internal relaxation rates at most $5k/2$. Targets use the original external rates and zero-field equilibrium preparation. Their passive visible path is exactly the common two-state telegraph process.

Fix any $a>0$. The experiments needed for the lower bound use only fields $0,h_*$. Each positive-duration constant-field segment has duration an integer multiple of $a/k$, and the visible binary mean is observed at the end. Equivalently, an experiment is a finite word of propagators at those two fields, each of duration $a/k$; adjacent equal fields can be merged.

Competitors have a fixed initial distribution, a fixed real readout and at most $D$ physical Markov states. Their generator depends on the instantaneous field, so a constant field gives time-homogeneous evolution. They may have arbitrary transition rates and need not be reversible, analytic in the field, or calibrated to any passive or lower-order response data. A competitor can depend on the supplied target.

Let $D_{*,a}^{\rm bin}(\delta)$ be the worst-case minimal competing state count for this target class, when error is the supremum mean error on the specified experiment menu. There are constants $c_a,\gamma_a,\delta_a>0$, depending only on the fixed parameters, such that

$$
\boxed{
D_{*,a}^{\rm bin}(\delta)\ge c_a\delta^{-\gamma_a},
\qquad 0<\delta<\delta_a.
}
\tag{1}
$$

The lower bound already holds for targets whose internal rates all lie in $[3k/2,5k/2]$. It therefore also holds for the broader all-protocol prediction norm and for the larger menu allowing arbitrary durations at least $a/k$.

More explicitly, for every integer $n\ge1$, a target with $2^{4n+3}+1$ total states has

$$
\boxed{
\inf_{\widehat F:\,|\widehat F|<2^n}
\sup_{\text{specified experiments}}
|m_{F_n}-m_{\widehat F}|
\ge e^{-C_a(n+1)}.
}
\tag{2}
$$

The experiments witnessing (2) have total duration $O_a((n+1)/k)$. Hence the experiments proving (1) use horizons $O_a(\log(1/\delta)/k)$ while retaining the fixed minimum dwell $a/k$. Constants in this notation may also depend on $s,H$.

## 2. The target and its generator-word witness

Rescale time so that $k=1$. Import the positive construction from [SHIFT_REGISTER_LOWER_BOUND.md](SHIFT_REGISTER_LOWER_BOUND.md). With $m=4n+3$, its hidden physical states are the bit strings $x\in\{-1,+1\}^m$, with uniform law $\mu$ and $g(x)=s x_1$. Write $L$ for left shift followed by a fresh fair bit, $R=L^T$ for the reverse shift, and $\Pi=\mathbf1\mu^T$. The internal generator is

$$
K=\frac32(\Pi-I)+\frac14(L+R-2I).
\tag{3}
$$

It is irreducible and reversible, every physical off-diagonal entry is positive, and all nonzero internal relaxation rates lie in $[3/2,5/2]$. The coefficients of the refresh and shift kernels are independent of $n$.

Let $Q_0,Q_*$ be the full backward generators at fields $0,h_*$. Use the inner product weighted by $\pi_0=(1/2,\mu/2)$ and the original readout $S(A)=-1$, $S(B)=+1$. Both the initial-law functional $\pi_0$ and $S$ have norm one in this dual pairing. Define

$$
F=\frac{Q_0(Q_0+2I)}3,\qquad
b_*=e^{-h_*}\sinh(sh_*),\qquad
c_*=1-e^{-h_*}\cosh(sh_*),
$$

$$
Z_0=F^2,\qquad
Z_1=-b_*^{-1}F(Q_*-Q_0-c_*I)F.
$$

For a bit word $b=(b_1,\ldots,b_n)$, put $W_b=Z_{b_n}\cdots Z_{b_1}$. Reversal below means formal reversal of these letters. With

$$
\ell_*=2\sinh(h_*)\sinh(sh_*),\qquad
r_*=-2e^{-h_*}\sinh(sh_*),
$$

define the two noncommutative operator polynomials

$$
\mathcal L_b=\ell_*^{-1}Q_*F W_b^{\rm rev},\qquad
\mathcal R_b=r_*^{-1}W_bFQ_*.
\tag{4}
$$

The imported maximal-index projection identity gives the $2^n\times2^n$ matrix

$$
\mathsf H_{bc}=\pi_0\mathcal L_b\mathcal R_cS,
\qquad
\sigma_{\min}(\mathsf H)\ge\frac12\,48^{-(4n+2)}.
\tag{5}
$$

In the target this is a Gram matrix. Its selected Walsh leaves are distinct, and each has coefficient $48^{-(2n+1)}$; their full $L^2(\pi_0)$ squared norms include the factor $1/2$. Thus (5) is an exact projection bound, not a numerical-rank observation.

Each side polynomial in (4) has generator degree at most $5n+3$. Its sum of absolute coefficients is at most $C_*^{n+1}$ for a fixed $C_*\ge1$. For example, this follows by choosing

$$
C_*\ge\max\left\{1,|\ell_*|^{-1},|r_*|^{-1},
\frac{2+|c_*|}{b_*}\right\}.
\tag{6}
$$

Indeed $F$ has coefficient sum one, $Z_0$ has coefficient sum at most one, and $Z_1$ has coefficient sum at most $(2+|c_*|)/b_*$. This bound is independent of register length.

## 3. A general lemma for total-degree truncation

The following argument applies to any finite alphabet of target generators. It does not depend on their dimension or on the shift-register geometry. The matrix logarithm power series itself is classical; see [Higham, *What Is the Matrix Logarithm?* (2020)](https://nhigham.com/2020/11/17/what-is-the-matrix-logarithm/). The lemma records the operator-error and experiment-coefficient budgets when that series is truncated across a complete noncommutative polynomial.

**Lemma.** Fix a sampling interval $a>0$. Let $E_i=e^{aQ_i}$ and $X_i=I-E_i$. Suppose that, in one common operator norm,

$$
\|X_i^j\|\le\kappa q^j\quad(j\ge1),\qquad 0<q<1,
\tag{7}
$$

and that the convergent logarithm series recovers the target generators:

$$
Q_i=-\frac1a\sum_{j\ge1}\frac{X_i^j}{j}.
$$

Let $P$ be a noncommutative polynomial of total generator degree at most $d(n+1)$ and coefficient sum at most $C^{n+1}$. Introduce a single bookkeeping variable,

$$
Q_i(z)=-\frac1a\sum_{j\ge1}\frac{z^jX_i^j}{j},
\qquad
P(Q(z))=\sum_{j\ge0}z^jP_j.
\tag{8}
$$

Choose $1<\varrho<1/q$, and truncate the complete polynomial at total degree $M$:

$$
P^{[M]}=\sum_{j=0}^{M}P_j.
$$

There are constants $A,B\ge1$, depending only on $a,\kappa,q,\varrho,C,d$, such that

$$
\|P(Q)-P^{[M]}\|\le B^{n+1}\varrho^{-(M+1)},
\qquad \|P(Q)\|\le B^{n+1},
\tag{9}
$$

while $P^{[M]}$ is a polynomial in the actual propagators $E_i$, of degree at most $M$, with

$$
\boxed{\|P^{[M]}\|_{\mathrm{coeff},1}\le4^M A^{n+1}.}
\tag{10}
$$

In particular, a cutoff $M=O(n+1)$ gives exponentially small whole-polynomial error with only exponentially large propagator coefficient sum.

### Proof: target operator error

At radius $\varrho$, the absolute operator-coefficient sum of each logarithm series is at most

$$
K=\frac\kappa a\sum_{j\ge1}\frac{(\varrho q)^j}{j}
=\frac\kappa a\log\frac1{1-\varrho q}.
$$

Expand each ordered monomial of $P$ using (8). Submultiplicativity of operator norms and Cauchy convolution of nonnegative scalar majorants give

$$
\sum_{j\ge0}\varrho^j\|P_j\|
\le C^{n+1}\max\{1,K\}^{d(n+1)}.
\tag{11}
$$

Take $B=C\max\{1,K\}^d$, increasing it to one if necessary. The terms with $j>M$ have total norm at most $B^{n+1}\varrho^{-(M+1)}$. Evaluation at $z=1$ gives $P(Q)$ and its norm bound. The order of different generator factors is retained throughout; no commutativity is assumed.

### Proof: actual-propagator coefficients

Now regard each $E_i$ as a formal noncommuting letter $U_i$. The coefficient of $z^j$ in (8) is $-(I-U_i)^j/(aj)$, whose coefficient sum is at most $2^j/(aj)$. At the auxiliary radius $r=1/4$,

$$
\sum_{j\ge1}r^j
\left\|\frac{(I-U_i)^j}{aj}\right\|_{\mathrm{coeff},1}
\le\frac1a\sum_{j\ge1}\frac{(2r)^j}{j}
=\frac{\log2}{a}.
$$

The same scalar-majorant calculation yields

$$
\sum_{j\ge0}r^j\|P_j\|_{\mathrm{coeff},1}
\le C^{n+1}\max\{1,(\log2)/a\}^{d(n+1)}
=A^{n+1}.
\tag{12}
$$

For $j\le M$, removing the factor $r^j$ costs at most $r^{-M}=4^M$. This proves (10). A term of bookkeeping degree $j$ has at most $j$ propagator letters after expanding its factors $(I-U_i)^l$, so the propagator degree is at most $M$. This completes the lemma.

## 4. The logarithm hypotheses hold at any fixed dwell

For the shift-register targets, $Q_0,Q_*$ have all eigenvalues in $[-5,0]$. To see the uniform bound, $\|Q_0\|_{\pi_0}\le7/2$, while the field perturbation has norm at most $2(e^{(1+s)h_*}-1)<1/2$. Both generators are reversible under their respective equilibria, and

$$
\frac{\pi_h}{\pi_0}=\frac{e^{hS}}{\cosh h}.
$$

The condition number for changing the two weighted Hilbert norms is at most $\kappa=e^{h_*}$. For every fixed $a>0$, set

$$
E_i=e^{aQ_i},\qquad q=1-e^{-5a}\in(0,1).
$$

In the reversible norm, $I-E_i$ is selfadjoint with eigenvalues in $[0,q]$. Transferring its powers back to the common $\pi_0$ norm proves

$$
\|(I-E_i)^j\|_{\pi_0}\le e^{h_*}q^j.
\tag{13}
$$

The same spectral decomposition proves the logarithm identity in the lemma. For large $a$, the one-step norm in the common Hilbert space need not be below one; the power estimate (13) is sufficient. Thus the argument does not impose an upper bound on the fixed dwell time.

One explicit radius choice is

$$
\varrho=\frac{1+1/q}{2}>1,
\qquad
K_a=\frac\kappa a\log\frac1{1-\varrho q}
=\frac\kappa a(\log2+5a).
$$

For the side polynomials (4), use $d=5$, since $5n+3\le5(n+1)$, and take

$$
B_a=C_*\max\{1,K_a\}^5,
\qquad A_a=C_*\max\{1,(\log2)/a\}^5.
\tag{14}
$$

These constants are finite and independent of $n$.

## 5. Truncate each complete side and retain the singular value

Apply the lemma separately to every $\mathcal L_b$ and $\mathcal R_c$. Define

$$
\mathsf H^{[M]}_{bc}
=\pi_0\mathcal L_b^{[M]}\mathcal R_c^{[M]}S.
$$

This matrix need not be symmetric or a Gram matrix. Set

$$
\epsilon_n=B_a^{n+1}\varrho^{-(M+1)}.
$$

The two side errors, the original side norms from (9), and the $2^n$ matrix dimension imply

$$
\begin{aligned}
\|\mathsf H^{[M]}-\mathsf H\|
&\le2^n\left(2B_a^{n+1}\epsilon_n+\epsilon_n^2\right)\\
&\le3\,2^nB_a^{2(n+1)}\varrho^{-(M+1)}.
\end{aligned}
\tag{15}
$$

Choose an integer $M=M_n$ satisfying

$$
\varrho^{M+1}\ge
12\,2^n B_a^{2(n+1)}48^{4n+2}.
\tag{16}
$$

For example, the ceiling of the logarithm of the right-hand side divided by $\log\varrho$ suffices. This is $O_a(n+1)$. Equations (5) and (15) then give

$$
\boxed{
\sigma_{\min}(\mathsf H^{[M_n]})
\ge\frac14\,48^{-(4n+2)}.
}
\tag{17}
$$

Each truncated side has propagator coefficient sum at most

$$
J_n=4^{M_n}A_a^{n+1}=\exp[O_a(n+1)].
\tag{18}
$$

Each entry is therefore a finite signed combination of actual visible means with coefficient sum at most $J_n^2$. Its experiments use at most $2M_n$ propagator letters. Every positive segment is an integer multiple of $a$, and every horizon is at most $2M_na$.

The separate side truncations are essential to the next step. A total-degree cutoff applied to the combined row-times-column entry would not automatically preserve factorization through the competing state space.

## 6. The rank bound requires no approximation assumption on a competitor

For a $D$-state competitor, evaluate the same finite polynomials $\mathcal L_b^{[M_n]}$ and $\mathcal R_c^{[M_n]}$ on its actual propagators at fields $0,h_*$ and duration $a$. Use its fixed initial law and readout. The resulting matrix factors as rows of length $D$ times columns of length $D$:

$$
\operatorname{rank}\widehat{\mathsf H}^{[M_n]}\le D.
$$

No logarithm series is evaluated on the competitor, and no bound on its generator, spectrum or field derivatives is used. Only the finite signed experiment formulas are shared.

If the competitor's mean error on these experiments is at most $\delta$, (18) bounds the entrywise error by $J_n^2\delta$, and hence

$$
\|\mathsf H^{[M_n]}-\widehat{\mathsf H}^{[M_n]}\|
\le2^nJ_n^2\delta.
$$

When $D<2^n$, rank deficiency and (17) force

$$
\boxed{
\delta\ge
\frac{48^{-(4n+2)}}{4\,2^n J_n^2}
\ge e^{-C_a(n+1)}.
}
\tag{19}
$$

This proves (2). For sufficiently small $\delta$, take $n=\lfloor\log(1/\delta)/(2C_a)\rfloor-1\ge1$. Then $\delta<e^{-C_a(n+1)}$, so attaining error at most $\delta$ requires at least $2^n\ge\tfrac14\delta^{-(\log2)/(2C_a)}$ states. This proves (1) with strict slack in the error comparison. Restoring $k$ changes the sampling interval to $a/k$ and the total horizon to $2M_na/k$.

The improvement comes from accounting for total degree across a complete side word. Approximating each of its $O(n)$ generator factors separately to exponential accuracy allows total propagator degree $O(n^2)$. Equations (11)--(12) instead control the whole omitted tail with total degree $O(n)$.

## 7. Consequences and remaining gaps

For $R_s=e^{(1+s)H}$ and

$$
p=\frac{\log2}{\log(1+2/(5R_s))},
$$

the [bounded-rate upper theorem](BOUNDED_RATE_FINITE_FIELD.md) gives a stationary, potentially nonreversible surrogate with exact binary actuator distribution and

$$
D\le1+\max\left\{2,
\left(\frac{1+2R_s^2}{\delta}\right)^p\right\}.
$$

That theorem controls all protocols and horizons, so it applies to the smaller experiment menu here. Thus

$$
\boxed{
c_a\delta^{-\gamma_a}
\le D_{*,a}^{\rm bin}(\delta)
\le C\delta^{-p}
}
$$

for sufficiently small $\delta$. The notation $\delta^{-\Theta(1)}$ means this polynomial growth class, with fixed positive lower and upper exponents. It does not assert equality of the exponents or an exact power law. The same growth-class conclusion holds for this binary capped target class under the unrestricted all-protocol norm.

If the predictor must remain reversible and retain the spectral cap, the current sufficient bound is $\exp[C\delta^{-p}\log(2/\delta)]$. The polynomial lower applies to that smaller predictor class too, but a polynomial reversible upper remains open. For general actuator alphabets and uncapped internal spectra, the earlier general upper theorem remains the applicable broader result.

The shift-register cubic kernel has exactly $4n+3$ positive modes, all with rates different from $k$. Its exact minimal cubic-response state count is $4n+5$ in the established analytic-in-field Markov competitor class. At precision $\delta_n=\tfrac12e^{-C_a(n+1)}$, (19) shows that full controlled-mean prediction requires at least $2^n$ states even in the broader competitor class. Thus exact cubic prediction costs only $O(\log(1/\delta_n))$ states along a sequence where accurate full finite-field prediction costs a positive power of $1/\delta_n$.

All these are physical-state counts. They do not bound parameter precision, computation time or the number of signed experiments. No statistical sample bound is proved here. The constructor and lower-bound comparison both assume the kinetic target is supplied. The passive law, fixed actuator rule and stationary preparation remain the original ones throughout.
