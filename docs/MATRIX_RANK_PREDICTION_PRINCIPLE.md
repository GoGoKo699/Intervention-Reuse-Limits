# A matrix principle for reversible prediction

[Finite incidence example](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Exact finite minimum counts](FINITE_PREDICTOR_MINIMALITY.md) · [Bounded rational finite-error certificate](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Source comparison](SIMPLE_PREDICTION_SOURCE_AUDIT.md) · [Internal review](SIMPLE_PREDICTION_INTERNAL_REVIEW.md)

**Research theorem, 23 September 2026.** A memory state's incoming and outgoing roles can be different in a stationary predictor. Ordinary detailed balance ties them together. For the controlled models below, matched tests taken in reversed operator order expose this distinction and give an exact characterization of the minimum state counts by two familiar matrix factorizations.

Let $H$ be an $n\times n$ completely positive matrix with

$$
v=H1>0,\qquad 1^{\mathsf T}H1=1.
\tag{1}
$$

Here $v$ is a probability row when it is used in generator formulas. Write $\operatorname{rank}_+(H)$ for the least number of nonnegative rank-one terms $u_sw_s^{\mathsf T}$ summing to $H$, and $\operatorname{cprank}(H)$ for the least number of terms $c_sc_s^{\mathsf T}$ with $c_s\ge0$. The construction below defines one controlled binary-mean task from $H$, independently of which completely positive factorization is used to implement its target.

On this task, with every physical state counted,

$$
\boxed{
D_{\rm all}(0)=1+n+\operatorname{rank}_+(H),
\qquad
D_{\rm ord}(0)=1+n+\operatorname{cprank}(H).}
\tag{2}
$$

The comparison uses the same two fields, positive clock, visible/hidden preparation, readout and hidden exit cap for both classes. Rivals may introduce arbitrary new hidden states, stationary masses and endpoint barriers throughout $[0,1]$. They need not retain the target's label histogram. The sufficient models do retain that histogram.

Every reversible target in this family has its nonzero hidden decay rates in $[k,3k]$, while its passive zero-field binary path law is exactly that of a two-state chain. The larger counts in (2) concern prediction under interventions.

The exact formulas also persist on some positive, matrix-dependent error interval, as proved in Section 5. No useful size for that interval is asserted. Nonnegative rank, completely positive rank, factor normalization and the distinction between one-sided and symmetric factorizations are established ideas. The statement identifies the state counts for this specified controlled continuous-time task; no novelty claim is made for the matrix ranks themselves.

## 1. The common physical task

There is one visible state $A$, a hidden stationary law $\mu$, preparation $\pi_0=(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. The hidden generator $K$ is field-independent and has exits at most $2k$. The controlled interface is

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h).
\tag{3}
$$

Only fields $0$ and $h_*=\log2$ are needed for the lower. Their dwell times are positive multiples of $a/k$, with $a=(\log2)/8$. The task consists of every finite word on this two-field clock. Allowed rivals satisfy $\mu K=0$, $b_i(0)=1$ and $b_i(h_*)\in[0,1]$. The ordinary class additionally requires detailed balance of $K$ with respect to $\mu$. No target coordinate or factorization is supplied to a rival.

The target has one common memory label and $n$ distinct probe labels. These labels specify kinetic rates; they are not additional observed colors. The readout distinguishes only $A$ from the hidden block. A fixed choice is

$$
\beta_j=\frac38+\frac{5j}{16n},\qquad 0\le j\le n.
\tag{4}
$$

All memory states use $\beta_0$ and probe $i$ uses $\beta_i$. The curves $b_j(h)=\beta_j^{h/h_*}$ realize these values within the original exponential interface. Their sensitivities $g_j=1+\log(\beta_j)/\log2$ lie in $(-1/2,1/2)$. In particular, the sufficient models can share the same original exponential curves at every field, even though the lower needs only the two endpoint values.

At zero field, every hidden state returns to $A$ at rate $k$, and the total rate from $A$ into the hidden block is $k$. Thus the visible/hidden partition is exactly lumpable, with binary generator $k\left(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\right)$. Its initial law is $(1/2,1/2)$. This proves the two-state passive statement for the full binary-output path law, not only for its mean.

## 2. Turning a factorization into a stationary model

Take any nonnegative factorization

$$
H=UW,\qquad U\in\mathbb R_+^{n\times r},\quad
W\in\mathbb R_+^{r\times n}.
\tag{5}
$$

Remove zero factor terms. Then $s_\alpha=\sum_jW_{\alpha j}>0$, and the following definitions are valid:

$$
R_{\alpha j}=\frac{W_{\alpha j}}{s_\alpha},
\qquad
T_{i\alpha}=\frac{U_{i\alpha}s_\alpha}{v_i},
\qquad
a_\alpha=\sum_i v_iT_{i\alpha}.
\tag{6}
$$

Every coordinate of $a$ is positive. Direct multiplication, using the symmetry of $H$, gives

$$
R1=T1=1,\qquad
TR=\operatorname{diag}(v)^{-1}H=:M,
\qquad vT=a,\quad aR=v,\quad a1=1.
\tag{7}
$$

Use $r$ memory states and $n$ probe states. In units $k=1$, their hidden generator is

$$
K=
\begin{pmatrix}-I&R\\T&-I\end{pmatrix}
+
\begin{pmatrix}1a-I&0\\0&1v-I\end{pmatrix}.
\tag{8}
$$

The first term moves from memory to probe at total rate one and from probe to memory at total rate one. The second refreshes the state at rate one within its current block. Its conditional laws are $a$ for memory and $v$ for probes. This is a generator with exits at most two and stationary law

$$
\mu=(a/2,v/2).
\tag{9}
$$

Every constructed predictor therefore has the same total memory mass $1/2$ and the same probe masses $v_i/2$. It has the same full kinetic histogram under (4), regardless of the factor count $r$. The within-block refreshes and positive conditional laws make the hidden chain irreducible.

If the chosen factorization is completely positive, write $H=CC^{\mathsf T}$ and use $U=C$, $W=C^{\mathsf T}$. Then $a_\alpha=s_\alpha^2$ and

$$
a_\alpha R_{\alpha i}=v_iT_{i\alpha}.
\tag{10}
$$

These are exactly the cross-block detailed-balance equations; the refresh terms already satisfy detailed balance. Thus every completely positive factorization supplies an ordinary reversible realization.

Every such reversible realization also has nonzero hidden decay rates in $[k,3k]$. Indeed, the first term of (8) is a reversible rate-one bipartite walk, with decay rates in $[0,2]$. On the two-dimensional space of block-constant functions it has decay rates zero and two, and the refresh term vanishes. On the orthogonal complement, the refresh adds one to every decay rate. This argument also covers a disconnected support of $H$; the refresh makes the full hidden chain irreducible.

## 3. Every realization maps to the same endpoint predictor

Use the canonical factorization $H=H I_n$. Its memory-to-probe matrix is $R_*=I_n$, its probe-to-memory matrix is $T_*=M=\operatorname{diag}(v)^{-1}H$, and its memory law is $a_*=v$. A canonical memory state therefore stores the next probe endpoint.

For any normalized factorization from Section 2, define the stochastic map

$$
C=\operatorname{diag}(R,I_n),\qquad
\widetilde C=\operatorname{diag}(1,R,I_n).
\tag{11}
$$

A memory state maps to the endpoint distribution in its row of $R$; each probe and the visible state map to themselves. Equations (7) give, directly,

$$
K C=C K_*,\qquad \mu C=\mu_*,\qquad
Q_h\widetilde C=\widetilde C Q_{*,h},\qquad
\pi_0\widetilde C=\pi_{*,0},\qquad
\widetilde C S_*=S.
\tag{12}
$$

The controlled identity holds at every field because all memory states share the same barrier and every probe keeps its own barrier. Exponentiating and multiplying the identities across any switched protocol proves equality of the controlled means, at every horizon. No future control is used or presumed: endpoint selection is a fixed stochastic map compatible with every current field.

There is also equality of the entire controlled binary-output path law. If $D_-$ and $D_+$ project onto the visible and hidden readout classes, then $D_\pm\widetilde C=\widetilde C D_{*,\pm}$. Inserting these identities between propagators shows equality of every finite-dimensional binary-output distribution. All factorization realizations map to the same canonical model, so they agree with each other in both senses.

Taking a factorization of nonnegative rank proves the unrestricted upper in (2). Taking a factorization of completely positive rank proves the ordinary upper. The canonical endpoint predictor uses $n$ memory states; a smaller nonnegative factorization can use fewer. Its role is to prove common controlled behavior, not to assert that the canonical count is always minimal.

## 4. Why arbitrary rival states cannot do better

Only this lower-bound step uses distinct probe labels and exact agreement on every clock word. Put $J=e_Ae_A^{\mathsf T}$ and $\mathsf H=I-J$, and extend hidden operators by zero on $A$. At the two queried fields,

$$
\mathcal B=\mathsf H+\mathsf H(Q_0-Q_{h_*})\mathsf H,
\qquad
K=\mathsf H Q_0\mathsf H+\mathsf H.
\tag{13}
$$

The operator $\mathcal B$ is the diagonal of endpoint barriers. Let $L_j$ be the Lagrange interpolation polynomial on the distinct values $\beta_0,\ldots,\beta_n$, and set

$$
A_j=L_j(\mathcal B)^2,\qquad P=\mathsf H+K/2.
\tag{14}
$$

Use $\mathsf H$ for every hidden polynomial constant. Each $A_j$ is nonnegative diagonal on every allowed rival, including rivals with off-grid barriers. The cap two makes $P$ a nonnegative hidden Markov kernel. On the target, the $A_j$ are the exact label projectors.

For $1\le i\le n$, introduce positive right and reversed left words

$$
\begin{aligned}
F_i&=2A_0PA_i,&F_{n+i}&=A_i,\\
G_i&=2A_iPA_0,&G_{n+i}&=A_i.
\end{aligned}
\tag{15}
$$

In a general stationary rival the left word need not be an adjoint. Nevertheless the matrix

$$
N_{ij}=\mu G_iF_j1=2\pi_0G_iF_jS
\tag{16}
$$

has a nonnegative factorization through the actual hidden states: its left factors are $(\mu G_i)_s$ and its right factors are $(F_j1)_s$. Hence $\operatorname{rank}_+(N)$ is at most the rival's hidden state count. If the rival is ordinarily reversible, every factor in (14) is selfadjoint, $G_i=F_i^*$, and $N$ is a nonnegative-feature Gram. Its completely positive rank is then at most the same hidden state count.

For a reversible target realization from Section 2, the memory value of $F_i1$ is $R_{\alpha i}$ and its probe value is zero. The last $n$ features are the probe indicators. Its matrix is therefore

$$
\boxed{
N_*=
\operatorname{diag}\left(\frac H2,\frac{\operatorname{diag}(v)}2\right).}
\tag{17}
$$

The factor $1/2$ is essential: $H$ uses the conditional memory law $a$, whereas the full hidden law assigns mass $a/2$ to memory.

Exact agreement of all two-field clock means forces agreement of every scalar in (16). The needed recovery is already proved in the [nonreversible capped clock calculus](FINITE_PREDICTOR_MINIMALITY.md#5-centered-clock-logarithms-without-reversibility). Its only inputs are the shared full exit cap four, the fixed clock, and the stationary visible-row recursion. For each fixed generator/projector polynomial, substitute the convergent centered logarithm of the propagators and let the total cutoff tend to infinity. At zero mean discrepancy the coefficient-amplification term vanishes and both truncation tails tend to zero. This recovers (13)–(16) on arbitrary stationary rivals without requiring detailed balance or a target label palette.

Finally, both nonnegative rank and completely positive rank add across a nonnegative block-diagonal matrix. A nonnegative factor cannot meet two positive diagonal blocks without creating a positive off-block entry, so every factor is assigned to one block. The second block in (17) has $n$ positive diagonal entries and needs exactly $n$ factors of either kind. Thus

$$
\operatorname{rank}_+(N_*)=\operatorname{rank}_+(H)+n,\qquad
\operatorname{cprank}(N_*)=\operatorname{cprank}(H)+n.
\tag{18}
$$

Adding the visible state proves the two lower bounds in (2), including against arbitrary new rival states. The sufficient constructions in Sections 2–3 attain them.

Since the sufficient models also preserve the controlled binary path law, the same exact minimum counts hold if exact mean agreement is replaced by exact binary-output path-law agreement on the same protocol class. This follows from a mean lower and a path-law upper; no extra observable is used in the proof of (2).

## 5. The counts persist at some positive accuracy

For each fixed matrix $H$, there exist a finite set $\mathcal W_H$ of legal two-field clock experiments and a number $\delta_H>0$ such that both formulas in (2) remain true for every $0\le\delta\le\delta_H$, already when accuracy is required only on $\mathcal W_H$.

To see this, matrices of nonnegative rank at most a fixed integer $r$ form a closed set. In a convergent sequence of such matrices, normalize each nonzero left factor to have coordinate sum one. The corresponding right factor is bounded by the column sums of the matrix, so a subsequence of all factors converges. Zero terms may be padded with zero right factors. Likewise, matrices of completely positive rank at most $r$ form a closed set: in $N=\sum_{\alpha=1}^r c_\alpha c_\alpha^{\mathsf T}$, every $\|c_\alpha\|_2^2$ is bounded by $\operatorname{tr}N$. These arguments use only finitely many factors.

By (18), $N_*$ has positive entrywise distance from the nonnegative-rank class with one fewer factor than $\operatorname{rank}_+(H)+n$, and from the completely-positive-rank class with one fewer factor than $\operatorname{cprank}(H)+n$. Choose an entrywise tolerance $\epsilon_H>0$ smaller than both distances. This compactness argument is about finite matrix factors, not about the parameter space of physical rivals.

There are only finitely many scalar polynomials in (16). The uniform capped clock recovery bounds each target-to-rival scalar discrepancy by

$$
C_H\left[2^{-(L+1)}+3^L(1+7L)\delta\right]
$$

for a finite matrix-dependent constant $C_H$, simultaneously over every allowed rival. First choose the clock cutoff $L$ so that the tail is below $\epsilon_H/2$. Then choose $\delta_H>0$ so that the second term is below $\epsilon_H/2$. All clock words of length at most $L$ give one finite admissible choice for $\mathcal W_H$. A smaller rival would contradict one of the two factor-rank distances. The exact sufficient constructions give the matching upper counts.

This proves a positive accuracy interval without optimizing or claiming its size. In particular, it does not turn the exact matrix-rank identity into a practical experimental-precision claim.

## 6. Meaning and limits

The principle makes the storage distinction precise. A general predictor may assign one nonnegative profile to how a memory state is entered and another to where it leads next. In the matched tests (15)–(16), the left word reverses the right word's operator order. Detailed balance makes it the actual stationary adjoint, so the tested matrix permits general nonnegative terms $u_sw_s^{\mathsf T}$ in the first case and symmetric terms $c_sc_s^{\mathsf T}$ in the second. A generic discrete-time one-step HMM output matrix need not be a Gram matrix merely because its hidden transition matrix satisfies detailed balance. The reversed positive words are essential to identify this particular matrix $H$ and its state-count constraint; the statement does not deny the half-time Gram factorization of an ordinary reversible continuous-time semigroup.

For the established incidence example, take

$$
H=\frac1{24}
\begin{pmatrix}
3I_2&\mathbf1_{2\times3}\\
\mathbf1_{3\times2}&2I_3
\end{pmatrix}.
\tag{19}
$$

Its nonnegative rank is five and its completely positive rank is six, as proved in the earlier support arguments. Equation (2) then gives eleven unrestricted states and twelve ordinary reversible states. This is a specialization of the principle, not a new numerical state-gap claim. Likewise, the earlier complete-bipartite edge-versus-endpoint family is recovered by its incidence factorization; its known exact counts are not presented as new here.

The main formula concerns exact realization and retains individually distinguishable probe labels. Its label count grows with $n$. The positive-error corollary is an existence result: it supplies no alphabet-independent bound, useful finite tolerance, efficient experiment list or measurement-cost estimate. The theorem does not identify ordinary reversibility with generalized time reversal or infer device-independent thermodynamic dissipation. The explicit finite-accuracy certificates for the existing small example remain separate results.

The combined [verifier](../scripts/verify_simple_prediction_principles.py) and [report](../reports/simple_prediction_principles.json) check bounded exact examples of factor normalization, stationary generators, the canonical intertwiner and the feature matrix. The universal rank characterization and positive-error existence statement are the analytic arguments above; examples do not replace them.
