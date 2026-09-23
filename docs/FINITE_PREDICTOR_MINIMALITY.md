# Exact and finite-error minimality of the eleven-state predictor

[Finite twelve-versus-eleven construction](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Capped kinetic interface](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [Finite-advantage review](FINITE_ADVANTAGE_INTERNAL_REVIEW.md) · [Direct matrix and method precedents](FINITE_PRECISION_SOURCE_AUDIT.md)

**Research theorem, 23 September 2026.** The explicit eleven-state stationary predictor for the twelve-state incidence target is minimal. A centered logarithm improves the certified error interval to $0\le\delta\le2^{-1360}$ and reduces the required two-field experiments to 520 clock ticks. The unrestricted lower requires no reversibility: a positive left/right factorization replaces the Gram factorization, and an infinity-norm clock argument replaces reversible spectral calculus.

The target, predictor, clock and rival class are unchanged. The result sharpens a sufficient eleven-state count to an exact minimum and improves the earlier $2^{-3000}$, 1200-tick certificate. The new tolerance remains very conservative; no eleven-state generalized-reversible realization is asserted.

## 1. Fixed target, comparison and statement

Retain exactly the target and classes of the [finite construction](FINITE_REVERSIBILITY_ADVANTAGE.md#1-task-and-statement). There is one visible state $A$, hidden preparation law $\mu$, readout $S=(-1,1_{\rm hid})$, a field-independent stationary hidden generator with exits at most $2k$, and external rates

$$
q_{iA}(h)=k b_i(h),\qquad q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
\qquad b_i(0)=1,\quad b_i(H)\in[0,1].
\tag{1}
$$

The fields and clock are

$$
H=\log2,\qquad a/k=\frac{\log2}{8k},\qquad
\delta_*=2^{-1360}.
\tag{2}
$$

Let $\mathcal W_{520}$ be all words in the two sampled propagators with at most 520 ticks, as in the finite theorem. Every physical state is counted. No rival label, histogram, lower stationary mass or detailed balance is required in the unrestricted class.

**Theorem.** Every admissible stationary rival with at most ten total states has

$$
\boxed{
\max_{w\in\mathcal W_{520}}
|m_T(w)-m_R(w)|>\delta_*.}
\tag{3}
$$

The existing exact eleven-state predictor attains zero error. Applying the same improved clock transfer to the earlier ordinary-reversible obstruction gives, for this one fixed target and every $0\le\delta\le\delta_*$,

$$
\boxed{D_{\rm all}(\delta)=11,\qquad D_{\rm ord}(\delta)=12.}
\tag{4}
$$

These equalities hold already when accuracy is required only on $\mathcal W_{520}$. They also hold for the full two-field clock task and any larger well-defined protocol task containing these words, since the two explicit sufficient models reproduce all controlled means exactly. This statement does not enlarge the rival interface or rate budget in (1).

## 2. Positive left and right feature words

Set $k=1$ until times are restored. Write $J=e_Ae_A^{\mathsf T}$ and $H_0=I-J$, and extend hidden operators by zero on $A$. The two full generators give

$$
B=H_0+H_0(Q_0-Q_H)H_0,\qquad
K=H_0Q_0H_0+H_0.
\tag{5}
$$

For the six target values $\beta_j=(6+j)/16$, define the same squared Lagrange selectors and positive hidden kernel:

$$
L_j(x)=\prod_{r\ne j}\frac{x-\beta_r}{\beta_j-\beta_r},\qquad
A_j=L_j(B)^2,\qquad P=H_0+K/2.
\tag{6}
$$

Use $H_0$ for every polynomial constant term. In every rival, each $A_j$ is nonnegative diagonal and $P$ is a nonnegative Markov kernel on the hidden states. Stationarity, rather than reversibility, suffices for these facts.

For $1\le i\le5$, let

$$
\begin{aligned}
R_i&=2A_0PA_i,& R_{5+i}&=A_i,\\
L_i^{\rm word}&=2A_iPA_0,& L_{5+i}^{\rm word}&=A_i.
\end{aligned}
\tag{7}
$$

The left word reverses the order of the positive factors. It is not asserted to be an adjoint on a nonreversible rival. Define the observable matrix

$$
N_{ij}=\mu L_i^{\rm word}R_j1
=2\pi_0L_i^{\rm word}R_jS.
\tag{8}
$$

It has a nonnegative factorization through the actual hidden states:

$$
N=UV,\qquad
U_{is}=(\mu L_i^{\rm word})_s\ge0,\quad
V_{sj}=(R_j1)_s\ge0.
\tag{9}
$$

Hence its nonnegative rank is at most the hidden state count $D_h$. No relationship between the two factors is imposed in a general stationary model.

On the ordinarily reversible target, the reversed left word is the stationary adjoint of its corresponding right word. Thus $N_T$ is the previously calculated Gram matrix

$$
G=\operatorname{diag}\left(
\frac1{48}\begin{pmatrix}3I_2&\mathbf1_{2\times3}\\
\mathbf1_{3\times2}&2I_3\end{pmatrix},
\operatorname{diag}(3,3,2,2,2)/24\right).
\tag{10}
$$

All its positive entries are at least $c=1/48$, and every entry is at most $M_0=1/8$.

## 3. The support requires ten positive rectangles

A positive rectangle is a set of row indices times a set of column indices containing no zero entry of the target matrix. The support of a nonnegative rank-one matrix is such a rectangle. Let $S$ be the support of the first $5\times5$ block of (10). With vertex sets
$\mathcal L=\{L_1,L_2\}$ and $\mathcal R=\{R_1,R_2,R_3\}$, its positive cells are the five diagonal cells and all cross-part cells. There are seventeen positive cells.

**Support lemma.** Exactly five positive rectangles are needed to cover $S$.

Five row stars give an upper bound. For the lower, suppose that at most four rectangles cover $S$. Some rectangle contains two diagonal cells. They must be the endpoints of an edge, say $L_1,R_1$. Such a rectangle is forced to be the complete $2\times2$ box on those two vertices: any additional row or column would meet a same-part off-diagonal zero.

There are two cases.

1. Another rectangle contains two diagonal cells on a disjoint edge, say $L_2,R_2$. These two edge boxes do not cover
$L_1R_2,R_2L_1,L_2R_1,R_1L_2$. Among the two remaining rectangles, at least one contains the diagonal cell $R_3R_3$ and cannot contain any of those four cross cells. The last rectangle cannot contain all four: their combined row and column sets include a forbidden same-part pair. This is impossible.

2. No such disjoint diagonal edge box occurs. The three uncovered diagonal cells $L_2L_2,R_2R_2,R_3R_3$ must then belong to three distinct remaining rectangles. Both directions $L_1R_2,R_2L_1$ can only be covered by the rectangle containing $R_2R_2$: the first edge box excludes $R_2$, while the other two diagonals forbid those cells. This forces that rectangle to be the rigid $L_1,R_2$ edge box. Likewise the rectangle containing $R_3R_3$ is the rigid $L_1,R_3$ box. The rectangle containing $L_2L_2$ must now contain both directions between $L_2$ and each of $R_2,R_3$, which includes a forbidden $R_2,R_3$ cell. Again this is impossible.

The lemma follows. Every rectangle meeting one of the five isolated probe diagonals in (10) cannot meet another positive block. Those five diagonals therefore require five additional rectangles. The full support-cover number is exactly ten.

In particular, the first block has nonnegative rank five and the full matrix has nonnegative rank ten. For orientation, their ordinary ranks are four and nine, respectively: the first block has null vector $(1,1,-1,-1,-1)$ and rank four. The full matrix's completely positive rank is eleven by the earlier edge/isolated-diagonal argument. The distinction between these three factorization constraints is why a linear-rank bound alone would miss the unrestricted state minimum.

## 4. A robust nine-factor obstruction

**Finite nonnegative-rank lemma.** If a nonnegative matrix $N$ has a nonnegative factorization with at most nine factors, then

$$
\boxed{\|N-G\|_{\max}>\varepsilon_0,
\qquad \varepsilon_0=1/40000.}
\tag{11}
$$

Suppose instead that the error is at most $\varepsilon_0$, and write
$N=\sum_{s=1}^{D_h}u_sv_s^{\mathsf T}$ with $D_h\le9$ and $u_s,v_s\ge0$. Every positive target cell has value at least $c$. Assign each such cell to a factor contributing at least

$$
t=\frac{c-\varepsilon_0}{9}.
$$

If two assigned cells $(i,j),(r,l)$ share one factor, then its cross-product identity gives

$$
(u_s(i)v_s(j))(u_s(r)v_s(l))
=(u_s(i)v_s(l))(u_s(r)v_s(j))\ge t^2.
\tag{12}
$$

If either cross cell is a target zero, the corresponding factor contribution is at most $\varepsilon_0$. The other cross contribution is at most the corresponding entry of $N$, hence at most $M_0+\varepsilon_0$. This would imply
$t^2\le\varepsilon_0(M_0+\varepsilon_0)$. But exact arithmetic gives

$$
81\varepsilon_0(M_0+\varepsilon_0)
=\frac{405081}{1600000000}
<\frac{6235009}{14400000000}
=(c-\varepsilon_0)^2,
\tag{13}
$$

with positive margin $16183/90000000$.

Thus any two cells assigned to one factor have both cross cells in the target support. The row set times column set of all cells assigned to that factor is therefore a positive rectangle. At most nine such rectangles would cover every positive target entry, contrary to Section 3. This proves (11). No normalization of individual factors, no lower stationary mass and no bounded feature vector are needed.

## 5. Centered clock logarithms without reversibility

The full generators at the observed fields have exit rates at most four: at zero the cap is three, and at $H$ the visible exit is $4\sum\mu_i b_i(H)\le4$, while hidden exits are at most three. This holds without detailed balance.

Let $\|\cdot\|_\infty$ be the induced maximum-row-sum norm, and set

$$
c_0=\sqrt2=e^{4a},\qquad E_h=e^{aQ_h},\qquad Z_h=I-c_0E_h.
\tag{14}
$$

Since $Q_h+4I$ is entrywise nonnegative,
$c_0E_h=\exp[a(Q_h+4I)]\ge I$ entrywise. Its row sums are $c_0$. Thus $Z_h\le0$ entrywise and

$$
\|Z_h\|_\infty=c_0-1<5/12,
\tag{15}
$$

where the strict inequality follows from $\sqrt2<17/12$.
The actual generator has the convergent centered logarithm

$$
Q_h=-\frac{\log c_0}{a}I
-\frac1a\sum_{j\ge1}\frac{Z_h^j}{j}.
\tag{16}
$$

This identity needs no spectral or detailed-balance hypothesis. Indeed, for $0\le t\le1$, the matrix
$F_h(t)=\exp[ta(Q_h+4I)]\ge I$ has row sums $c_0^t$ and
$\|I-F_h(t)\|_\infty=c_0^t-1\le c_0-1<1$.
The logarithm series and its derivative therefore converge uniformly along this path. Its derivative is
$F_h(t)^{-1}F_h'(t)=a(Q_h+4I)$, since all factors are functions of one matrix. The series vanishes at $t=0$, so its value at $t=1$ is $aQ_h+(\log c_0)I$, giving (16). There is no ambiguous logarithm branch.

Include the degree-zero constant term when replacing each generator letter by (16). At operator bookkeeping radius $2$, its absolute majorant is

$$
\frac1a\left[\log c_0+\log\frac1{1-2(c_0-1)}\right]
<\frac{\log9}{a}<32.
\tag{17}
$$

Here $c_0<3/2$ and $1-2(c_0-1)>1/6$. The final inequality is equivalent to $9<16$ because $a=(\log2)/8$.
The formal propagator-coefficient mass of $Z_h$ is $1+c_0<5/2$. At coefficient bookkeeping radius $1/3$, the corresponding majorant is also less than
$[\log(3/2)+\log6]/a=(\log9)/a<32$.

Visible projectors have infinity norm one. For a generator/projector polynomial $\mathcal P$ of generator degree $d$ and coefficient mass $J_{\mathcal P}$, retain terms in (16) with total centered-logarithm degree at most $N$, calling the result $\mathcal P^{[N]}$. The two majorants give

$$
\|\mathcal P-\mathcal P^{[N]}\|_\infty
\le J_{\mathcal P}32^d2^{-(N+1)},\qquad
\|\mathcal P^{[N]}\|_{\mathrm{coeff},1}
\le J_{\mathcal P}32^d3^N.
\tag{18}
$$

Every retained propagator word has at most $N$ ticks. These bounds hold uniformly for every stationary rival in (1), whether reversible or not. The constant term in (16) is included in the majorants and adds no tick.

## 6. Actual means recover the positive-factor matrix

The shared local-balance interface gives the fixed-field stationary law
$\pi_h=(1, e^{2h}\mu)/(1+e^{2h})$ whenever $\mu K=0$. It does not require hidden detailed balance. Thus the exact visible-row preparation recursion remains

$$
\begin{aligned}
b(E_HV)&=b(V)+(1+\coth H)[m(E_HV)-m(V)],\\
b(E_0V)&=e^{-2a}b(V)+(1-e^{-2a})m(V),\qquad b(I)=-1,
\end{aligned}
\tag{19}
$$

with $b(V)=e_A^{\mathsf T}VS$. Its rank-one insertion formula bounds discrepancies of inserted forward words of length $N$ by $(1+7N)\delta$, since $1+2(1+\coth H)=19/3<7$. The observed words are legal two-field experiments and have no more than $N$ ticks.

Combining this fact with (18), and using that $\pi_0$ is a probability law and $\|S\|_\infty=1$, gives

$$
|\pi_0\mathcal P S-\widehat\pi_0\widehat{\mathcal P}\widehat S|
\le J_{\mathcal P}32^d
\left[2\,2^{-(N+1)}+3^N(1+7N)\delta\right].
\tag{20}
$$

The factor two accounts for the target and rival truncation tails. No adjoint operation or rival spectral representation enters this estimate.

For $\mathcal P_{ij}=2L_i^{\rm word}R_j$, the unchanged coefficient calculation in the finite theorem gives

$$
d\le42,\qquad J_{\mathcal P}\le2^{289},\qquad
J_{\mathcal P}32^d\le2^{499}.
\tag{21}
$$

A reversed positive left word has the same factor coefficients as its right counterpart, regardless of reversibility. At $N=520$ and $\delta=\delta_*$,

$$
\|N_R-G\|_{\max}
\le2^{-21}+2^{-17}<2^{-16}<1/40000,
\tag{22}
$$

because $3^{520}=(3^5)^{104}<2^{832}$ and $1+7\cdot520=3641<2^{12}$. This refers to the positive-factor matrix (8); it is not interpreted as a Gram matrix of nonreversible rival features.

## 7. Minimum counts and limits

A rival with at most ten total states has at most nine hidden states. Its matrix (8) has at most nine nonnegative factors by (9), contradicting (11) and (22). This proves (3). For an ordinarily reversible rival, the same matrix is a Gram matrix of nonnegative feature vectors and has completely positive rank at most its hidden state count. The earlier robust completely positive obstruction rules out ten hidden states whenever the matrix error is at most $1/40000$. Thus (22) also excludes ordinarily reversible rivals with at most eleven total states. The exact eleven-state stationary construction and the twelve-state ordinary reversible target supply the respective matching upper counts in (4).

The result establishes unrestricted minimality and improves the original finite certificate. It also makes the matrix distinction explicit: ordinary rank nine does not give the needed hidden-state lower, nonnegative rank ten does, and completely positive rank eleven supplies the additional ordinary-reversibility cost.

The new horizon is $520a/k=65\log2/k$, compared with the earlier $150\log2/k$. The precision $2^{-1360}$ remains impractical and the witness family may be enormous. Obtaining a useful tolerance remains open. The theorem assumes the same hidden exit cap two, bounded endpoint barriers, baseline returns, field-independent hidden dynamics and preparation/readout as the finite construction. It does not supply a ten-state unrestricted predictor, an eleven-state generalized-reversible realization, or a useful experimental sample bound. The existing target is a six-label, generally uncentered model; the earlier nineteen-level asymptotic family is unchanged.

## 8. Finite ordinary entropy production at the improved tolerance

The same eleven-state predictor can be perturbed to have finite ordinary entropy production. For any $0<\delta\le\delta_*$, use the frozen construction's perturbation

$$
K_\eta=(1-\eta)K_R+\eta K_R^*,\qquad
\eta=\delta/22.
\tag{23}
$$

The prior bound gives controlled-mean error at most $11\eta=\delta/2$ on the entire field interval $|h|\le H$, uniformly over the corresponding admissible protocols, while retaining the eleven physical states and the hidden exit cap two. Its full zero-field identity-reversal entropy-production rate obeys

$$
\sigma_0(K_\eta)\le k\log(22/\delta).
\tag{24}
$$

This is a parameter substitution into the existing perturbation proof, rather than a new entropy estimate. At $\delta=\delta_*$ it supplies a finite-entropy-production eleven-state predictor within the improved certified tolerance. It does not make that predictor ordinarily reversible or establish generalized reversibility.

The matrix $48H$ already appears as $A(0,0)$ in Fawzi–Parrilo, Eq.(55), with completely positive rank six. The [source audit](FINITE_PRECISION_SOURCE_AUDIT.md) records this direct matrix precedent, its older attribution, and the established rectangle-cover lower bound for nonnegative rank. No novelty is claimed for that matrix or those general tools. The proof above records the concrete support obstruction, its robust tolerance and the nonreversible controlled-mean transfer needed for this fixed physical target. Exact finite enumeration can check the small support-cover statement and scalar inequalities; the arbitrary-rival conclusion is the analytic argument.
