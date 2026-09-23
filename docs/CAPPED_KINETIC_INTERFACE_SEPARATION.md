# Two-field separation with a shared equilibrium interface

[Original tight-band target](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Clock preparation and Gram identities](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Whole-side logarithm truncation](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md) · [Positive finite-grid selectors](POSITIVE_LABEL_SELECTORS.md)

**Research theorem, 23 September 2026.** On the original nineteen-level target family, two physical fields suffice for polynomial unrestricted state complexity and exponential ordinary-reversible state complexity under the same hidden exit-rate budget. Rivals may choose their own kinetic barrier functions and need not retain any target actuator value, histogram or parametrization. The external interface retains a specified equilibrium bias and a common zero-field switching rate.

The target family and all physical state counts are unchanged. The proof uses exact positive squared-Lagrange selectors, a positive uniformized hidden kernel, finite clock observations, and repair on the rival's own states. The unrestricted lower uses a separate target-only rank argument on the same two-field menu.

## 1. Comparison class and theorem

Fix $k,H,a>0$. The targets are the original nineteen-level lamp models, with sensitivity alphabet
$\Gamma=\{0,\pm1/100,\ldots,\pm9/100\}$, hidden band $[k,3k]$, and original exponential external rates. At index $n$, write $r=2^n$; the target has $18r2^r+2$ total physical states. Its paired logical ports have mass $z_*=1/18$.

Put $\beta_\gamma=e^{(\gamma-1)H}$. Choose fixed numbers
$$
0\le \ell<u<\infty,\qquad
\ell\le\min_{\gamma\in\Gamma}\beta_\gamma,
\qquad u\ge\max_{\gamma\in\Gamma}\beta_\gamma.
\tag{1}
$$
A competitor has a finite hidden space, a positive probability law $\mu$, a field-independent hidden generator $K$ stationary under $\mu$, and state-specific kinetic functions $b_i(h)$. Its external rates are
$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
\tag{2}
$$
with
$$
b_i(0)=1,\qquad b_i(H)\in[\ell,u].
\tag{3}
$$
Rates at the two observed fields are nonnegative and finite. One may require strictly positive $b_i(H)$; the proof does not need a uniform positive lower bound. No common functional form, differentiability, sensitivity label or histogram is imposed. Only values at $0,H$ enter the theorem. If functions on a larger field interval are specified, their behavior away from those two points is irrelevant to this experiment class.

Both predictor classes have hidden exits at most $3k$, preparation $\pi_0=(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. Every physical state is counted. The ordinary-reversible class additionally requires detailed balance of $K$ under $\mu$; this is the only difference between the classes.

Experiments use fields $\{0,H\}$, with each positive segment duration an integer multiple of $a/k$. Define worst-case minimal sizes over the unchanged target family for uniform absolute mean error $\delta$ on these experiments. There are fixed positive constants such that, for sufficiently small $\delta$,
$$
\boxed{
\begin{aligned}
D_{\rm all}^{(2,a)}(\delta)&=\delta^{-\Theta(1)},\\
D_{\rm rev}^{(2,a)}(\delta)&\ge\exp(c\delta^{-\alpha}),\\
D_{\rm rev}^{(2,a)}(\delta)&\le
\exp\!\bigl(C\delta^{-p}\log(2/\delta)\bigr),\\
p&=\frac{\log19}{\log(1+1/(3R_H))},\qquad
R_H=e^{(1+9/100)H}.
\end{aligned}}
\tag{4}
$$
The exponents are not matched. Equivalently the reversible growth class is $\exp(\delta^{-\Theta(1)})$, with the logarithm in the sufficient bound absorbed by a slightly larger power. The witnesses at width $n$ need accuracy $e^{-C_*(n+1)}$ and at most $C'(n+1)$ clock ticks.

The target keeps its exact rate-$k$ passive telegraph law and band $[k,3k]$. Set $k=1$ for the proof.

## 2. The equilibrium interface recovers visible-state insertions

Write $J=e_Ae_A^{\mathsf T}$ and $H_0=I-J$. Local balance in (2), together with stationarity of $K$, gives
$$
\pi_h(A)=\frac1{1+e^{2h}},\qquad
\pi_h(i)=\frac{e^{2h}\mu_i}{1+e^{2h}}.
\tag{5}
$$
This identity does not require hidden reversibility. In particular, with $t_h=\tanh h$,
$\pi_h=(1+t_h)\pi_0-t_he_A^{\mathsf T}$.
For a legal clock word $V$, let $M(V)=\pi_0VS$, $b(V)=e_A^{\mathsf T}VS$, and $E_h=e^{aQ_h}$. Then
$$
\begin{aligned}
b(E_HV)&=b(V)+(1+\coth H)[M(E_HV)-M(V)],\\
b(E_0V)&=e^{-2a}b(V)+(1-e^{-2a})M(V),\qquad b(I)=-1.
\end{aligned}
\tag{6}
$$
The first equation follows from (5). The second uses $b_i(0)=1$ and the exact passive telegraph sector. Thus both are valid also for the nonreversible comparison class.

Rank-one insertions factor exactly:
$$
\pi_0V_0JV_1J\cdots JV_mS
=\frac{1-M(V_0)}2
\prod_{j=1}^{m-1}\frac{1-b(V_j)}2\ b(V_m).
\tag{7}
$$
All intermediate factors lie in $[0,1]$ and the final factor lies in $[-1,1]$. If observed means differ by at most $\delta$, the discrepancy in (7) is at most
$$
(1+C_H d)\delta,
\tag{8}
$$
where $d$ is the total number of propagator letters. The bound also covers no insertion and empty blocks. It follows from finite suffix recursion and telescoping actual bounded factors; it does not assume independently prepared visible or hidden states. No word longer than $d$ is used.

When $K$ is reversible, the full $Q_h$ is reversible under (5). Its stationary adjoint in the common $\pi_0$ metric is
$$
Q_h^{*\pi_0}=W_hQ_hW_h^{-1},\qquad
W_h=I+(e^{-2h}-1)J.
\tag{9}
$$
The same formula holds for sampled propagators. Neither (5) nor (9) depends on the kinetic barrier values.

## 3. Exact positive selectors and target-exact transports

Extend hidden operators by zero on $A$. Put $B=\operatorname{diag}(b_i(H))$ on the hidden block. The two full generators recover both this diagonal multiplication and the hidden generator exactly:
$$
\boxed{
B=H_0+H_0(Q_0-Q_H)H_0,\qquad
K=H_0Q_0H_0+H_0.}
\tag{10}
$$
Here $H_0$ is the identity of the hidden block. Field independence of $K$ and the baseline $B_0=I$ are essential to (10).

For each of the nineteen distinct target values $\beta_i$, define
$$
L_i(x)=\prod_{j\ne i}\frac{x-\beta_j}{\beta_i-\beta_j},
\qquad A_i=L_i(B)^2.
\tag{11}
$$
Polynomial evaluation uses $H_0$ as its constant term, so $A_i$ vanishes on the visible state. Every $A_i$ is a nonnegative diagonal kernel in every rival. Its norm is bounded by the fixed constant
$\max_{x\in[\ell,u]}L_i(x)^2$.
On the target it is exactly the label projector $D_i$. A rival need not use any grid point, and $A_i$ need not be a projector there.

For each paired logical port $c$, let $A_c$ be the sum of its two signed selectors. The common hidden exit cap makes
$$
P=H_0+K/3
\tag{12}
$$
a Markov kernel on the hidden states. It is entrywise nonnegative in both classes and selfadjoint in a reversible rival. For each adjacent pair of distinct logical ports, put
$$
T_{cd}=48 A_c P A_d.
\tag{13}
$$
These are nonnegative kernels; ordinary reversibility gives $T_{dc}=T_{cd}^*$. On the target,
$$
T_{cd}=48D_c(I+K/3)D_d=16D_cKD_d,
\tag{14}
$$
the exact norm-one transport of the original lamp construction. There is no target approximation or shrinking gate time.

Each selector has generator degree at most $36$ after (10), and each transport has degree at most $73$. Their generator/projector coefficient masses are fixed constants. Consequently a word of $O(n+1)$ transports has generator degree, projector count and logarithmic coefficient mass all $O(n+1)$.

Use the original query itineraries $Q_b$ and flip words $C_c=Q_cG_FQ_c^*$. A query uses at most $9n$ edges, a flip at most $18n+3$, and the longest squared-image test at most $54n+6$. With central selectors $A_{0,+},A_{0,-}$, set
$$
A=A_{0,+}+A_{0,-},\quad u=A1,\quad
v=(A_{0,+}-A_{0,-})1,\quad
v_b=Q_bv,\quad q_b=Q_bu,\quad Z=\|u\|_\mu^2.
\tag{15}
$$
Positivity gives $|v_b|\le q_b$. All nonempty central words and all flips have $A$ as outer factors. Empty queries act on vectors already supported on $\{u>0\}$. Thus the support conditions of weighted repair hold in every rival.

The target has $Z=z_*=1/18$ and satisfies every weighted-repair equality exactly, because (11) and (14) are exact. This includes query preservation, both flip row relations, image norms, and the specified signs of query-flip correlations.

## 4. Uniform capped clock transfer with projector insertions

This section applies to target and reversible rival. Their full generators at $0,H$ have exit rates at most
$$
R_*=\max\{4,3+u,e^{2H}u\}.
$$
Thus their reversible spectra lie in $[-\Lambda,0]$ with $\Lambda=2R_*$. Put
$$
\chi=e^H,\quad \rho=1-e^{-a\Lambda}\in(0,1),\quad
\varrho=\frac{1+1/\rho}{2}>1.
\tag{16}
$$
Norm equivalence with $\pi_h$ gives, in the common $\pi_0$ norm,
$$
\|(I-E_h)^j\|\le\chi\rho^j,\qquad
Q_h=-\frac1a\sum_{j\ge1}\frac{(I-E_h)^j}{j}.
\tag{17}
$$
All constants are uniform in model dimension, stationary masses and rates within the stated cap.

Let $\mathcal P$ be any noncommutative polynomial in $Q_0,Q_H,J,I$, of generator degree at most $d$ and coefficient mass $J_{\mathcal P}$. Projectors do not count toward $d$. Insert a bookkeeping factor $z^j$ in the $j$th logarithm term of (17), substitute in the complete polynomial, and retain total bookkeeping degree at most $M$. Denote the result by $\mathcal P^{[M]}$. The [whole-side majorant proof](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md#3-a-general-lemma-for-total-degree-truncation) remains valid with arbitrarily interspersed $J$, since $\|J\|=1$ and its formal coefficient mass is one.

For
$$
C_a=\max\left\{1,\frac\chi a\log\frac1{1-\varrho\rho},\frac{\log2}{a}\right\},
$$
it gives
$$
\|\mathcal P-\mathcal P^{[M]}\|\le
J_{\mathcal P} C_a^d\varrho^{-(M+1)},\qquad
\|\mathcal P^{[M]}\|_{\mathrm{coeff},1}\le
J_{\mathcal P}C_a^d4^M.
\tag{18}
$$
The retained polynomial uses legal clock words with visible projectors and at most $M$ propagator letters. Expanding hidden complements $H_0=I-J$ is done before this bound and is included in $J_{\mathcal P}$.

Combining (8) and (18), for the scalar $F(\mathcal P)=\pi_0\mathcal P S$,
$$
|F(\mathcal P)-\widehat F(\mathcal P)|
\le J_{\mathcal P}C_a^d
\left[2\varrho^{-(M+1)}+4^M(1+C_H M)\delta\right].
\tag{19}
$$
Choose $M=\lfloor\log(1/\delta)/\log(8\varrho)\rfloor$ for sufficiently small $\delta$. With
$$
\theta=\frac{\log\varrho}{\log(8\varrho)}>0,
$$
(19) implies
$$
|F(\mathcal P)-\widehat F(\mathcal P)|
\le C J_{\mathcal P}C_a^d\delta^\theta.
\tag{20}
$$
This bound reconstructs scalar values; the exact positive kernels remain (11)–(13). No logarithm or signed clock polynomial is treated as a positive rival transport.

Every hidden entropy scalar equals $2\pi_0\mathcal P S$ for a hidden-supported word, with any required adjoints obtained by reversing the selfadjoint hidden factors. Its $d$ and $\log J_{\mathcal P}$ are $O(n+1)$, including expansions of squared defects. Therefore all required scalar discrepancies are at most
$$
e^{C(n+1)}\delta^\theta.
\tag{21}
$$

## 5. Ordinary-reversible lower by weighted repair

Choose a fixed $C_*$ sufficiently large and require
$$
\delta\le e^{-C_*(n+1)}.
\tag{22}
$$
Equations (20)–(21), together with the target's exact equalities, then imply $Z\ge z_*/2$ and every weighted-repair hypothesis with $\Delta\le e^{-10(n+1)}$, after increasing the starting index if necessary. Hence
$$
\sqrt\Delta\le\frac1{32r},\qquad
D\ge2^{3r/4},\qquad r=2^n.
\tag{23}
$$
The measure change, repaired couplings and decoded bits use only actual rival states. No state is added or assigned a target coordinate.

For a finite witness statement at width $n$, use the cutoff corresponding to the right side of (22), rather than the actual smaller error; it has $M=O(n+1)$ ticks. Choosing $n$ of order $\log(1/\delta)$ proves the reversible lower in (4), with some $\alpha>0$.

## 6. A polynomial unrestricted lower on the same two fields

This is a separate rank argument. It uses a logarithm expansion only on the target. A rival needs the preparation recursion (6)–(8), but no rate cap or reversibility for this section.

Let $V=A_{0,+}-A_{0,-}$ and $W_b=Q_bV$. On the target, the vectors $f_b=W_bS$ are the addressed lamp signs supported on the central port, so
$$
2\langle f_b,f_c\rangle_{\pi_0}=\frac1{18}\mathbf1_{b=c}.
\tag{24}
$$
Express $W_b$ as a polynomial in the full generators and $J$. Form a formal forward polynomial $W_b^\sharp$ by reversing factors and replacing each generator adjoint using (9); $J^*=J$. On the target this is exactly $W_b^{*\pi_0}$. On a nonreversible rival it is simply the same specified polynomial, with no assertion that it is an adjoint. Its degree and logarithmic coefficient mass remain $O(n+1)$.

The target matrix with rows and columns
$$
\mathcal L_b=2\pi_0(I-2J)W_b^\sharp,
\qquad \mathcal R_c=W_cS
\tag{25}
$$
is $I_r/18$ by (24). Truncate the entire left polynomial and entire right polynomial separately at total logarithm degree $M=C_{\mathrm{rank}}(n+1)$, using (18) only on the target. Fixed sufficiently large $C_{\mathrm{rank}}$ makes the error in every matrix entry at most $1/(72r)$: polynomial norms grow at most exponentially in $n$, while the truncation tails decay geometrically in $M$. Thus the retained target matrix has smallest singular value at least $1/24$.

Both retained sides are finite polynomials in $E_0,E_H,J$, with degree $O(n+1)$ and coefficient mass $e^{O(n+1)}$. Evaluate exactly those polynomials on a $D$-state rival. The resulting matrix factors as an $r\times D$ row matrix times a $D\times r$ column matrix, so its rank is at most $D$. This factorization does not require its generator logarithm to converge in the target expansion.

Every matrix entry is an inserted forward-word scalar. By (8), target-to-rival mean accuracy bounds its discrepancy by $e^{C_{\mathrm{rank}}'(n+1)}\delta$. If $D<r$, the matrix discrepancy has operator norm at least $1/24$, but is at most $r$ times the maximum entry discrepancy. Consequently some legal two-field mean differs by at least $e^{-C_{\mathrm{rank}}''(n+1)}$. Inverting this relation gives a fixed positive polynomial state lower.

The arbitrary kinetic curves pose no problem: (6) follows from stationarity and the shared interface, not from a field derivative or a prescribed sensitivity. This rank proof does require that interface and the stated preparation/readout; it does not assert the same two-field result for arbitrary initial laws or unrelated field rules.

## 7. Sufficient counts and the shared comparison

The existing stationary nineteen-symbol word-chain construction retains the original exponential kinetics, so it belongs to the larger class (2)–(3). It has hidden exits at most $3$ and gives
$$
D\le1+\max\left\{19,
\left(\frac{1+2R_H^2}{\delta}\right)^p\right\}.
\tag{26}
$$
The existing reversible prediction partition also belongs to this class, retains exits at most $3$, and gives the sufficient count in (4). Both control all bounded protocols and all horizons, hence the smaller two-field clock class. Combined with Sections 5–6, these prove every line of (4) on the same target family and menu.

## 8. What the kinetic generality does and does not say

The proof retains a field-independent hidden generator, the common equilibrium bias $e^{2h}$, baseline rates $b_i(0)=1$, the preparation/readout, and an upper bound on $b_i(H)$. Its capped exponential lower additionally uses the common hidden exit cap. It removes the rival actuator alphabet, histogram and exponential parametrization.

For $\ell>0$, the two observed generators of each allowed kinetic rival coincide with those of an exponential-rule model having effective sensitivity
$g_i^*=1+\log b_i(H)/H$. Arbitrary kinetic curves are therefore not separately identified by two-field observations. The result states which finite-menu assumptions support the separation; it is not a claim to recover those curves. The proof also permits positive rates approaching zero uniformly over rivals, or zero rates, because no positive lower envelope is used.

If the hidden cap is removed, the exact uniformized kernel (12) need not be positive and the exponential proof does not apply. The positive beta-selector and physical-resolvent proof still works under (2)–(3): use $X=(B-\ell H_0)/(u-\ell)$, the same equilibrium and projector identities, and the denominator bound $z/[z+\max\{1,e^{2H}u\}]$. Its target grid may lie strictly inside the interval. Thus the previously established fifth-root-log uncapped reversible lower also holds for this wider kinetic class. Section 6 supplies its polynomial unrestricted lower on the same two fields without a rival cap.

Allowing field-dependent hidden generators generally adds $K_0-K_H$ to (10), destroying the diagonal-selector identity. Allowing unrelated equilibrium biases or state-dependent zero-field return rates removes the particular preparation recursions used here. No conclusion for those larger classes is claimed. Ordinary detailed balance is the reversible constraint in this theorem; alternate notions using an internal time-reversal involution require a separate comparison.
