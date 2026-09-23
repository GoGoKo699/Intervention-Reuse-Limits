# An intrinsic state cost of reversible prediction

[Checkpoint and recovery status](../README.md) · [Bounded-rate upper bounds](BOUNDED_RATE_FINITE_FIELD.md) · [Positive transport repair](POSITIVE_TRANSPORT_REPAIR.md) · [Fixed-clock transfer](REVERSIBLE_WORD_OBSERVABILITY.md)

**Research theorem, 22 September 2026.** A fixed nineteen-level actuator family has polynomial state complexity when nonreversible predictors are allowed, but state complexity singly exponential in a positive power of inverse error when predictors must be reversible. Both predictor classes use the same internal exit-rate budget, original field rule, exact actuator histogram, preparation and readout. The lower bound applies to arbitrary newly constructed reversible state spaces. It concerns actual controlled means and survives every fixed positive control clock.

The analytic argument is supplemented by [exact finite checks](../scripts/verify_dynamic_lamp_reversibility_lower_bound.py), with [generated evidence](../reports/dynamic_lamp_reversibility_lower_bound.json) and [verification scope](VERIFICATION.md). Finite checks do not establish the asymptotic theorem by enumeration.

## 1. The comparison and its scope

Fix $H,k>0$. Section 2 constructs targets indexed by $n\ge1$, with $r=2^n$, $18r2^r+2$ total physical states, and hidden relaxation band $[k,3k]$. Their fixed sensitivity histogram is

$$
\Pr_\mu(g=0)=\frac12,\qquad
\Pr_\mu\!\left(g=\pm\frac j{100}\right)=\frac1{36},
\quad j=1,\ldots,9.
\tag{1}
$$

Thus $G=9/100$, $\mu g=0$, and $W=19/12000$.

Let $D_{\rm all}^{(3)}(\delta)$ and $D_{\rm rev}^{(3)}(\delta)$ be the worst-case minimal total predictor state counts over this target family. Both classes have one visible state $A$, a finite hidden stationary law, histogram (1), the original field rule, and internal outgoing rates at most $3k$ from every state. The second class additionally requires ordinary internal reversibility; the first permits stationary nonreversible dynamics. Preparation and readout are the original zero-field equilibrium and binary visible readout. Error means uniform absolute error of the actual mean over all bounded deterministic piecewise-continuous protocols and all observation times.

For sufficiently small $\delta$ there are fixed positive constants such that

$$
\boxed{
\begin{aligned}
c_0\delta^{-\gamma}
&\le D_{\rm all}^{(3)}(\delta)
\le C_0\delta^{-p},\\
\exp(c_1\delta^{-\alpha})
&\le D_{\rm rev}^{(3)}(\delta)
\le \exp\!\left(C_1\delta^{-p}\log\frac2\delta\right),\\
p&=\frac{\log19}{\log(1+1/(3R_H))},
\qquad R_H=e^{(1+9/100)H}.
\end{aligned}}
\tag{2}
$$

Both lower bounds already hold on thirty-nine fixed field values, with all positive segment durations integer multiples of any fixed $a/k>0$. Their witnessing horizons are $O_a(\log(1/\delta)/k)$. The upper bounds control the full protocol class. The exponents in (2) are unmatched.

The reversible lower holds for any fixed $\Lambda\ge3$ for all original-rule reversible rivals with histogram (1) and hidden relaxation cap $\Lambda k$, with constants depending on $\Lambda$. Rivals need not preserve a lower gap or the target topology. Taking $\Lambda=6$ covers every reversible rival with internal exit budget $3k$, because its real spectrum lies in $[-6k,0]$. The reversible upper models retain the narrower target band $[k,3k]$, hence also obey the common exit budget.

This construction uses nineteen actuator values and a fixed rate budget. The [binary extension](BINARY_REVERSIBILITY_LOWER_BOUND.md) proves the same growth-class separation with two actuator values at a larger fixed rate budget. The binary target band $[k,3k]$, unbounded-rate reversible rivals, and reversible rivals with arbitrary field dependence remain outside these results. There is no partition, encoder, inherited-coordinate, or target-state labeling restriction on the reversible rivals in (2).

## 2. A uniformly mixing table-and-register target

Set $k=1$ until Section 9. Addresses belong to $\{0,1\}^{\mathbb Z_n}$. A table is $x=(x_b)_b\in\{-1,+1\}^r$, and $\sigma\in\{-1,+1\}$ is a sign. There are $M=2r2^r$ triples $y=(x,b,\sigma)$.

There are nine ports: central port $0$, and ports $a_g,b_g$ for each $g\in\{J,V,X,F\}$. Every port contains every triple, with stationary mass $1/(18M)$ per state. Each port has mass $1/18$. One additional hidden hub $o$ has mass $1/2$. Including visible state $A$, the physical count is $9M+2=18r2^r+2$.

On register coordinates let $J:i\mapsto-i-1$ and $V:i\mapsto-i$, and let $X$ flip address coordinate $0$. The two reflections generate cyclic rotation. These involutions change only the address. The fourth involution is

$$
F(x,b,\sigma)=(x^{(b)},b,\sigma),
\tag{3}
$$

where $x^{(b)}$ flips exactly the table entry at address $b$.

For each gate $g$, add the undirected matching edges

$$
(y,0)\longleftrightarrow(y,a_g),\qquad
(y,a_g)\longleftrightarrow(gy,b_g),\qquad
(y,b_g)\longleftrightarrow(y,0),
\tag{4}
$$

each at rate $\lambda=1/16$ in both directions. The central degree is eight and each auxiliary degree is two. Distinct ports make these genuine jumps even when a gate fixes an address. Every nonhub hidden state $z$ jumps to $o$ at rate one, and $o$ jumps to $z$ at rate $2\mu_z$. There are no other hidden off-diagonal rates.

Every edge satisfies detailed balance. The star alone has relaxation spectrum $\{0,1,2\}$: leaf zero-mean modes have rate one and the hub/leaf contrast has rate two. The gate generator has maximum exit rate $8\lambda=1/2$, hence spectral cap at most $16\lambda=1$. Adding Dirichlet forms places the hidden relaxation band in $[1,3]$. The star makes the target connected.

Enumerate ports by $j=0,\ldots,8$, put $\gamma_j=(j+1)/100$, and define

$$
g(x,b,j,\sigma)=\gamma_j\sigma x_b,\qquad g(o)=0.
\tag{5}
$$

The exact histogram is (1), and
$W=(1/18)\sum_{j=1}^9j^2/10000=19/12000$.
Attach $A$ with the original rule

$$
q_{Az}(h)=\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=e^{(g_z-1)h}.
\tag{6}
$$

Use $\pi_0=(1/2,\mu/2)$ and $S(A)=-1$, $S(z)=+1$. The full generator is reversible at every constant field, with
$\pi_h(A)=e^{-h}/(2\cosh h)$ and
$\pi_h(z)=\mu_z e^h/(2\cosh h)$.
The passive visible path law is exactly the rate-one two-state telegraph law. Central port mass under $\pi_0$ is $1/36$.

## 3. Physical fields expose positive cross-port transports

For a sensitivity level $\gamma$, let $X_\gamma$ have only row $A$ nonzero, hidden entries $\mu_z\mathbf1_{g_z=\gamma}$, and diagonal minus that level's mass. Let $Y_\gamma$ have hidden rows of level $\gamma$, with entry $1$ in column $A$ and diagonal $-1$. Let $K_b$ be the hidden-only extension of $K$. Then

$$
Q(h)=K_b+\sum_\gamma e^{(1+\gamma)h}X_\gamma
             +\sum_\gamma e^{(\gamma-1)h}Y_\gamma.
\tag{7}
$$

The thirty-nine frequencies $0$ and $\gamma\pm1$ are distinct. Choose

$$
\bar h=\min\{H,1/[20(1+G)]\},\qquad
h_i=i\bar h/38,\quad i=0,\ldots,38.
\tag{8}
$$

The exponential coefficient matrix is a Vandermonde matrix in the distinct positive numbers $e^{\omega\bar h/38}$. Hence $K_b$ and every $Y_\gamma$ are fixed linear combinations of these physical generators. Coefficient bounds are independent of $n$, and the same expressions hold in each allowed rival.

On the invariant subspace of functions vanishing at $A$, set
$D_j=-Y_{\gamma_j}-Y_{-\gamma_j}$.
These are port projectors on that subspace; their full polynomial expressions are not orthogonal projectors on arbitrary full functions. For an adjacent pair of distinct ports put

$$
T_{cd}=\lambda^{-1}D_cK_bD_d.
\tag{9}
$$

On hidden functions this is a nonnegative kernel from port $c$ to port $d$, of generator degree three and fixed coefficient mass. In the target it is a permutation transport. In any allowed rival it remains positive because it is a genuine off-diagonal block of the rival's hidden generator. The hub does not occur in this block; no refresh term is subtracted.

All ports have equal stationary mass. Thus $T_{dc}$ is the conditional stationary adjoint of $T_{cd}$. A reversible rival with cap $\Lambda$ has $-K_{ii}\le\Lambda$, by the spectral bound applied to a coordinate indicator. Therefore

$$
T_{cd}\mathbf1\le C_\Lambda:=16\Lambda.
\tag{10}
$$

Put $B_j=Y_{\gamma_j}+Y_{-\gamma_j}$ and
$B_s=Y_{\gamma_0}-Y_{-\gamma_0}$.
Let $s$ be the signed central actuator bit, zero outside port $0$. The equal masses of its signed levels give

$$
B_sS=-2s,\qquad
\pi_0B_s=-s^T\operatorname{diag}(\pi_0).
\tag{11}
$$

The analogous left identity for $B_j$ has an extra term
$\mu(\text{port }j)e_A^T/2$, which vanishes on hidden-supported vectors. For a hidden word $V$ beginning and ending at port $0$,

$$
\langle s,Vs\rangle_0=18\pi_0B_sVB_sS.
\tag{12}
$$

Here $\langle\cdot,\cdot\rangle_j$ uses conditional stationary probability on port $j$. Writing $R_{cd}=T_{cd}\mathbf1_d$, the row moments are

$$
\begin{aligned}
\mathbb E_cR_{cd}&=18\pi_0B_cT_{cd}B_dS,\\
\mathbb E_cR_{cd}^2&=18\pi_0B_dT_{dc}T_{cd}B_dS.
\end{aligned}
\tag{13}
$$

These are polynomials in physical generators with the actual preparation and readout. Reversing hidden words simply reverses their cross-port edges. No additional preparation or adjoint actuator is supplied.

## 4. Direct fixed-clock transfer with finite horizons

Suppose both models have hidden cap at most $\Lambda\ge3$ and actual means differ by at most $\delta$ on the menu (8) at clock $a$. Put

$$
\begin{gathered}
B_{\rm sp}=2(\Lambda+e^{(1+G)\bar h}),\qquad
\kappa=e^{\bar h},\qquad q=1-e^{-aB_{\rm sp}},\\
\rho=(1+q)/2,\qquad t=q/\rho\in(0,1),\\
Z=\frac\kappa a\log\frac1{1-\rho},\qquad D=8/\rho,\qquad
\theta=\frac{\log(1/t)}{\log(D/t)}>0.
\end{gathered}
\tag{14}
$$

Full outgoing rates are at most $\Lambda+e^{(1+G)\bar h}$, so the full reversible spectra lie in $[-B_{\rm sp},0]$. Set $E_h=e^{aQ_h}$, $U_h=I-E_h$. Equilibrium norm equivalence costs at most $\kappa$, giving

$$
\|U_h^j\|_{\pi_0}\le\kappa q^j,\qquad
Q_h=-\frac1a\sum_{j\ge1}\frac{U_h^j}{j}.
\tag{15}
$$

Expand a word of $d$ generators and grade by total $U$-degree. Charge $\kappa$ once per logarithm block. The weighted coefficient series at $\rho$ equals $Z^d$, so the operator tail above total degree $M$ is at most $Z^dt^{M+1}$ in either model.

A product of $j$ factors $U_h=I-E_h$ expands into legal propagator words with absolute coefficient sum at most $2^j$. The retained scalar discrepancy is at most

$$
Z^d\delta\sum_{j=0}^M(2/\rho)^j
\le2Z^dD^M\delta.
$$

The scalar tails are bounded by their operator norms because $\|1\|=\|S\|=1$. Choose $M=\lfloor\log(1/\delta)/\log(D/t)\rfloor$. Every generator polynomial $p$ of maximum degree $d$ and absolute coefficient mass $J$ then satisfies

$$
\left|\pi_0p(Q)S-\bar\pi_0p(\bar Q)\bar S\right|
\le4J\max\{1,Z\}^d\delta^\theta.
\tag{16}
$$

All retained experiments have at most $M$ clock steps. Identity factors disappear and adjacent equal fields may be merged. The estimate still holds when $M<d$, in which case the retained part of a homogeneous degree-$d$ word is zero. No equilibrium calibration is needed. A separate [transfer note](REVERSIBLE_WORD_OBSERVABILITY.md) gives the same argument.

Every moment used below has degree and log coefficient mass $O(n)$, so its discrepancy is at most

$$
\Delta_n=A^{n+1}\delta^\theta
\tag{17}
$$

for one fixed $A\ge1$. Uniform prediction accuracy bounds each experiment; the number of different words does not multiply this bound.

## 5. Repair on the rival's own states

The target row moments in (13) both equal one. Thus the rival has, in both directions,

$$
\mathbb E_c(R_{cd}-1)^2\le3\Delta_n.
\tag{18}
$$

The [balanced-flux lemma](POSITIVE_TRANSPORT_REPAIR.md) says: if a nonnegative kernel $T$ and its stationary adjoint have row-sum mean-square defects at most $\varepsilon$, there are kernels $U,U^*$ on the same state sets, both stochastic, such that

$$
\sum_{i,j}\nu_i|T_{ij}-U_{ij}|\le3\sqrt\varepsilon.
\tag{19}
$$

To construct them, set $F_{ij}=\nu_iT_{ij}$, clip using row and column factors $\min(1,1/(T1)_i)$ and $\min(1,1/(T^*1)_j)$, and fill the remaining marginal deficits by their normalized outer product. Apply this once per unordered port pair, using its adjoint for the reverse direction.

A length-$L$ raw path and its repaired path differ in full path $L^1$ norm by at most

$$
3LC_\Lambda^{L-1}\sqrt\varepsilon.
\tag{20}
$$

Telescope with repaired prefixes and raw suffixes: the prefix has exactly the prescribed conditional stationary marginal, and the suffix has mass at most the appropriate power of $C_\Lambda$. This also bounds every path scalar with endpoint factors bounded by one. No states are added. These stationary couplings are proof operators, not a claimed physical surrogate.

## 6. Querying and flipping every bit with short words

For gate $g$, use the central cycle

$$
G_g=T_{0b_g}T_{b_ga_g}T_{a_g0}.
\tag{21}
$$

It acts as involution $g$ on target functions; its reversed word is $G_g^*$. Repaired rival cycles are stationary Markov kernels on the central states, with reversed words as adjoints.

Any pure XOR translation has a word $W_c$ with $n$ rotations and at most $n$ first-bit flips. Each rotation costs two reflections, hence the word uses at most $3n$ cycles or $9n$ cross-port edges. Choose backward-pullback instruction order so that

$$
(W_cf)(x,b,\sigma)=f(x,b\oplus c,\sigma).
$$

Both $W_c$ and its adjoint have this target action. Put
$f_b=W_bs$ and $F_c=W_cG_FW_c^*$. On every central target state,

$$
f_b(x,a,\sigma)=\sigma x_{a\oplus b},\qquad
\|f_b\|_0^2=1,\qquad
F_cf_b=(-1)^{\mathbf1_{b=c}}f_b.
\tag{22}
$$

The conjugated lamp gate flips table entry $a\oplus c$ and restores current address $a$. Therefore

$$
(-1)^{\mathbf1_{b=c}}\langle f_b,F_cf_b\rangle_0=1.
\tag{23}
$$

The norm word $W_b^*W_b$ has at most $18n$ edges; the correlation word
$W_b^*W_cG_FW_c^*W_b$ has at most $36n+3$.
Including the endpoints in (12), the maximum physical generator degree is $108n+11$, with coefficient mass bounded by a fixed constant to the power $n+1$.

## 7. Flip invariance forces entropy on actual rival states

Evaluate and repair the rival words. Let $U_b$ be repaired $W_b$, let $C_c$ be repaired $W_cG_FW_c^*$, and put $h_b=U_bs$.
All expectations below use the rival conditional central stationary law. Since $U_b$ is Markov, $|h_b|\le1$; each $C_c$ is stationary Markov.

By (16) and (20), with $\varepsilon=3\Delta_n$,

$$
\mathbb Eh_b^2\ge1-\eta_n,\qquad
(-1)^{\mathbf1_{b=c}}\langle h_b,C_ch_b\rangle\ge1-\eta_n,
\tag{24}
$$

where a common bound is

$$
\eta_n=\Delta_n+
3(36n+3)C_\Lambda^{36n+2}\sqrt{3\Delta_n}
\le B^{n+1}\delta^\beta,\qquad \beta=\theta/2>0,
\tag{25}
$$

with $B$ fixed. This is scalar path control; no vector identification between different model spaces is assumed.

Round to $Z_b=\operatorname{sign}(h_b)$, choosing $+1$ at zero. Its $r$-bit joint law $\rho$ is defined on the rival's central stationary probability space. Then

$$
\mathbb E|Z_b-h_b|=\mathbb E(1-|h_b|)
\le1-\mathbb Eh_b^2\le\eta_n.
$$

For each $c$, couple a stationary state $I$ to its next state $J$ under $C_c$. Replacing the bounded factors in (24) by rounded bits costs at most $2\eta_n$, giving

$$
\Pr\{Z_b(J)\ne(-1)^{\mathbf1_{b=c}}Z_b(I)\}\le3\eta_n/2.
$$

A union bound over $r$ bits yields a coupling of $\rho$ and its one-bit-flipped law with failure probability at most $3r\eta_n/2$. Thus

$$
\operatorname{TV}(\rho,\operatorname{flip}_c\rho)\le3r\eta_n/2
\quad\hbox{for every }c.
\tag{26}
$$

For any bit law,
$H(Z_c\mid Z_{-c})\ge1-\operatorname{TV}(\rho,\operatorname{flip}_c\rho)$:
condition on the other bits and apply $h_2(u)\ge1-|2u-1|$. The conditional average of $|2u-1|$ is that total variation. Chain rule and conditioning give

$$
H(Z)\ge\sum_cH(Z_c\mid Z_{-c})
\ge r(1-3r\eta_n/2).
\tag{27}
$$

If the rival has $D_0$ central states, $Z$ is a deterministic function of one of those states, so $H(Z)\le\log_2D_0$. Consequently

$$
\eta_n\le\frac1{6r}
\quad\Longrightarrow\quad
D_{\rm total}\ge D_0\ge2^{3r/4}.
\tag{28}
$$

The earlier static dictionary could be replaced by a small ensemble matching its short moments. The additional lamp dynamics here force approximate invariance under every separately addressed flip, and hence large support on the new rival state space itself.

## 8. Inverse-error scale and the common rate budget

Choose a fixed $C$ sufficiently large that

$$
\delta_n=e^{-C(n+1)},\qquad
B^{n+1}\delta_n^\beta\le\frac1{6\cdot2^n}
\tag{29}
$$

for every $n\ge1$. Every reversible rival of target $n$ at $\delta\le\delta_n$ needs at least $2^{3\cdot2^n/4}$ states. Taking the largest such $n$ gives
$n\ge C^{-1}\log(1/\delta)-2$, hence

$$
D\ge\exp(c\delta^{-\alpha}),\qquad \alpha=(\log2)/C>0.
\tag{30}
$$

For each fixed $\Lambda\ge3$ the proof uses only the corresponding fixed constants. Choose $\Lambda=6$ to cover every ordinary reversible rival with internal exits at most $3$, using Gershgorin and reality of the reversible spectrum. The two classes in (2) thus have the same internal rate budget.

## 9. Upper bounds and the unrestricted lower on this family

The [bounded-rate word construction](BOUNDED_RATE_FINITE_FIELD.md) with $m=19$ and target cap $3$ uses $P=I+K/3$ and internal Poisson update rate $3$. It gives a stationary, possibly nonreversible surrogate with the original field rule, exact histogram and exits at most $3$, satisfying

$$
D\le1+\max\left\{19,
\left(\frac{1+2R_H^2}{\delta}\right)^p\right\},
\qquad p=\frac{\log19}{\log(1+1/(3R_H))}.
\tag{31}
$$

Section 7 of that theorem gives a reversible prediction partition with

$$
D\le\exp\!\left(C\delta^{-p}\log(2/\delta)\right).
\tag{32}
$$

It refines exact actuator levels and uses $EKE$. Rayleigh quotients on centered cell-constant functions retain both endpoints of $[1,3]$, so its exits are at most $3$. Both uppers hold uniformly over widths, bounded protocols and horizons.

The uniform target table also gives

$$
\langle f_b,f_c\rangle_{\pi_0}=\frac1{36}\mathbf1_{b=c}.
\tag{33}
$$

The physical left and right expressions are
$L_b=\pi_0B_sW_b^*$ and $R_c=W_cB_sS$.
By (11), $L_bR_c=2\langle f_b,f_c\rangle_{\pi_0}=\mathbf1_{b=c}/18$.
Each side has generator degree $O(n)$ and coefficient mass $\exp(O(n))$.

Apply the existing [target-only whole-side fixed-clock rank transfer](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md), as also used in the [static dictionary lower](AGGREGATION_STATE_LOWER_BOUND.md). Truncate logarithm expansions on each whole side separately at total degree $M=O_a(n)$. The target operator tails are exponentially small in $M$ with prefactors exponential in $n$; choose the constant in $M$ so each resulting matrix entry changes by at most $1/(72r)$. The $r\times r$ target matrix then has smallest singular value at least $1/24$, by the operator norm bound $r$ times its maximum entry error from $I_r/18$.

The retained row and column coefficient masses are $\exp(O_a(n))$. On any $D$-state Markov rival the same finite propagator expressions factor as an $r\times D$ matrix times a $D\times r$ matrix, and hence have rank at most $D$. If $D<r$, the target-to-rival matrix operator error is at least $1/24$. Uniform actual-mean accuracy bounds it above by $r\exp(O_a(n))\delta$. Therefore some actual mean differs by at least $\exp[-C'(n+1)]$.

Only the target is expanded into logarithms in this rank argument. Rivals may have arbitrary fixed preparations and real readouts, arbitrary rate dependence and unbounded rates. Thus it applies in particular to the first class in (2), proving its polynomial minimax lower. It is logically separate from the capped reversible entropy proof.

Restoring $k$ rescales times by $1/k$ and changes no state count. Equations (30)--(33) prove (2).

## 10. Contribution and attribution

An explicitly colored hub supplies uniform mixing while keeping each gate a positive off-diagonal block of a rival generator. Ordinary reversibility supplies reverse moments. Fixed caps allow their quantitative inference from actual means. Balanced repair supplies stationary couplings on existing rival states. Independent lamp-flip relations then force a high-entropy deterministic decoding.

Lamp and Følner growth, the final entropy inequality, logarithm expansions, and positive transport constructions are established ingredients or elementary arguments. The candidate contribution is their quantitative combination into the same-budget finite-error separation (2). See the [primary-source comparison](PRIOR_ART.md). No broad originality certification, binary theorem, or unrestricted-rate reversible lower is asserted.
