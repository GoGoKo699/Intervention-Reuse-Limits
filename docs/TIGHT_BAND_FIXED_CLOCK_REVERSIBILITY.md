# A fixed-clock reversibility penalty on the original tight-band targets

[Positive label selectors](POSITIVE_LABEL_SELECTORS.md) · [Fixed-clock Gram transfer](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Original target](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Weighted repair](WEIGHTED_WHOLE_WORD_REPAIR.md) · [Earlier uncapped theorem](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md)

**Research theorem, 23 September 2026.** The original targets with hidden relaxation band $[k,3k]$ exhibit an uncapped superpolynomial cost of ordinary reversibility at every fixed positive control clock. Two field values suffice. Rivals may choose arbitrary sensitivities throughout the target's bounded actuator range, without preserving its nineteen-level alphabet or histogram.

The targets and their physical state counts are unchanged. Positive label filters and physical resolvent recovery replace rapid-switching interpolation. The fifth-root logarithmic exponent is a conservative sufficient bound, not a claim of optimal growth.

## 1. Common model and statement

Fix $k,H>0$, a dimensionless clock $a>0$, and $G=9/100$. The targets are exactly the nineteen-level lamp family, with
$$
\Gamma=\{0,\pm1/100,\ldots,\pm9/100\},\qquad
\operatorname{spec}(-K)\setminus\{0\}\subset[k,3k].
\tag{1}
$$
At index $n$, put $r=2^n$. There are $18r2^r+2$ total physical states. The target hidden histogram has mass $1/2$ at zero and $1/36$ at each nonzero sensitivity; every paired logical port has mass $1/18$.

In both competitor classes, a model may use any finite hidden space, positive stationary law $\mu$, stationary hidden generator $K$, and sensitivities $g_z\in[-G,G]$. There is no prescribed number of levels and no requirement to match the target's histogram, moments, lower gap or rate cap. Both classes obey the original rule
$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
\tag{2}
$$
with preparation $(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. All physical states are counted. The reversible class additionally requires ordinary detailed balance of $K$ under $\mu$; this is the only difference between the two classes.

Use only the fields $\{0,H\}$. Every positive segment duration and observation horizon is an integer multiple of $a/k$. Let $D_{\rm all}^{(2,a)}(\delta)$ and $D_{\rm rev}^{(2,a)}(\delta)$ be worst-case minimal state counts over the original target family for uniform absolute mean error $\delta$ on this clock protocol class. For sufficiently small $\delta$,
$$
\boxed{
\begin{aligned}
D_{\rm all}^{(2,a)}(\delta)&\le C_0\delta^{-p},\\
D_{\rm rev}^{(2,a)}(\delta)&\ge
\exp\!\left(\exp\!\left(c_{a,H}[\log(1/\delta)]^{1/5}\right)\right),\\
p&=\frac{\log19}{\log(1+1/(3R_H))},\qquad R_H=e^{(1+G)H}.
\end{aligned}}
\tag{3}
$$
The reversible sufficient count remains $\exp(C_1\delta^{-p}\log(2/\delta))$. Growth exponents are not matched. At target index $n$, the lower-bound implication needs only finitely many legal two-field words, of length at most $C_{a,H}(n+1)^5$, independently of rival rates and dimension.

Section 7 supplies a polynomial unrestricted lower on the same target family using a thirty-nine-field clock menu. The main two-field theorem asserts only a polynomial sufficient count for unrestricted prediction.

The passive visible law remains exactly the rate-$k$ telegraph law. No rare tags, new target states or hidden-rate rescaling are added. Set $k=1$ in the proof; restore physical times by division by $k$.

## 2. Positive filters for the finite target grid

Let
$$
B_H=\operatorname{diag}(e^{(g-1)H}),\quad
b_-=e^{(-G-1)H},\quad b_+=e^{(G-1)H},\quad
X=\frac{B_H-b_-I}{b_+-b_-}.
\tag{4}
$$
Every allowed rival has $0\le X\le I$. In the target, $X$ has nineteen distinct fixed values $x_i\in[0,1]$, including both endpoints. This interval constraint, rather than histogram matching, supplies positivity.

Set the feature frequency $s=e^{200(n+1)}$ and define
$$
G_0(s)=(sI-K+I)^{-1},\qquad G_H(s)=(sI-K+B_H)^{-1},
$$
$$
F_+=\frac{s^2}{2}(G_0XG_H+G_HXG_0),\qquad
F_-=\frac{s^2}{2}(G_0(I-X)G_H+G_H(I-X)G_0).
\tag{5}
$$
These are entrywise nonnegative selfadjoint contractions in every reversible rival. They are not asserted to be positive semidefinite. On the target, $F_+=X+O(s^{-1})$ and $F_-=I-X+O(s^{-1})$.

For each interior $x_i$, choose fixed positive integers $a_i,b_i$ for which $\phi_i(x)=x^{2a_i}(1-x)^{2b_i}$ has its unique maximum over the finite target grid at $x_i$. Such integers exist: the real ratio $a/(a+b)=x_i$ gives a strict continuous maximum, and a sufficiently close rational ratio preserves every strict finite-grid inequality. Put
$$
T_i=F_+^{a_i}F_-^{2b_i}F_+^{a_i},\qquad
w_i=\phi_i(x_i),\qquad
\beta_i=\min\{1,\log w_i-\max_{j\ne i}\log\phi_i(x_j)\}>0.
\tag{6}
$$
Zero values contribute $-\infty$ in this maximum. At the endpoints use $T_i=F_-^2$ or $F_+^2$, $w_i=1$, and the analogous positive grid separation capped at one. Define
$$
m_i=\left\lceil\frac{120(n+1)}{\beta_i}\right\rceil,\qquad
A_i=(T_i/w_i)^{m_i}.
\tag{7}
$$
Every $A_i$ is entrywise nonnegative and selfadjoint on a rival. The base $T_i$ is also positive semidefinite because its middle factor is an even selfadjoint power, though this extra property is unnecessary for repair.

The ideal target base $\phi_i(X)/w_i$ has norm one. The selector proof gives
$$
\|A_i-D_i\|
\le e^{-120(n+1)}+\frac{Cm_i}{s}\exp(Cm_i/s)
\le e^{-110n}
\tag{8}
$$
for sufficiently large $n$, where $D_i$ is the target label projector. In a rival no projector approximation is assumed. Instead, the known norm bound $\|A_i\|\le w_i^{-m_i}=e^{O(n+1)}$ supports coefficient bookkeeping. Each selector has $O(n+1)$ factors $F_\pm$. All constants depend only on the fixed grid and $H$.

## 3. Positive transports and unchanged lamp identities

For a paired logical port $c$, let $A_c$ be the sum of its two signed selectors. Use an independent frequency $t=e^{20(n+1)}$ and set
$$
P_t=t(tI-K)^{-1}=tG_0(t-1),\qquad
\mathsf T_{cd}=8t\,A_cP_t^2A_d
\tag{9}
$$
on each adjacent pair of distinct ports. These operators are positive in every rival, with $\mathsf T_{dc}=\mathsf T_{cd}^*$.

On the target, $P_t^2=I+2K/t+O(t^{-2})$. Disjoint target port projectors and (8) therefore give
$$
\|\mathsf T_{cd}-16D_cKD_d\|
\le C/t+Ct e^{-110n}\le Ce^{-20n}.
\tag{10}
$$
The ideal block is the original norm-one permutation transport. The different feature and gate frequencies are part of the approximation budget.

Use the original triangular itineraries to form query words $Q_b$ and flip words $C_c=Q_cG_FQ_c^*$. The edge counts remain at most $9n$ for a query, $18n+3$ for a flip, and $54n+6$ for the longest squared-image scalar. No target logical operation has changed.

For the central port, define
$$
A=A_{0,+}+A_{0,-},\quad u_0=A1,\quad
v=(A_{0,+}-A_{0,-})1,\quad
v_b=Q_bv,\quad q_b=Q_bu_0,\quad Z=\|u_0\|_\mu^2.
\tag{11}
$$
Positivity gives $|v_b|\le q_b$. Nonempty central words and every flip word have $A$ as an outer factor. Empty queries act on vectors already supported on $\{u_0>0\}$.

The ideal normalization is $z_*=1/18$. Telescoping (8) and (10) through $O(n+1)$ factors gives every target defect in the [weighted repair hypotheses](WEIGHTED_WHOLE_WORD_REPAIR.md#1-hypotheses-on-one-finite-probability-space), divided by $z_*$, at most $e^{-15n}$ for sufficiently large $n$. This includes $|Z-z_*|/z_*$. The fixed positive central mass eliminates the rare-mass normalization cost of the earlier binary construction.

## 4. Finite scalar reduction using two physical fields

Write $\mathcal Z_h(z)=z(zI-K+B_h)^{-1}$, with $B_0=I$. The resolvent identity supplies
$$
\begin{aligned}
F_+&=\frac{s}{b_+-b_-}\bigl(\mathcal Z_0(s)-\mathcal Z_H(s)\bigr)\\
&\quad-\frac{b_--1}{2(b_+-b_-)}
\bigl(\mathcal Z_0(s)\mathcal Z_H(s)+\mathcal Z_H(s)\mathcal Z_0(s)\bigr),\\
F_-&=\tfrac12\bigl(\mathcal Z_0(s)\mathcal Z_H(s)+\mathcal Z_H(s)\mathcal Z_0(s)\bigr)-F_+.
\end{aligned}
\tag{12}
$$
The positive kernels are those defined in (5), not the signed summands in (12). Also $P_t=[t/(t-1)]\mathcal Z_0(t-1)$, whose scalar prefactor is at most two.

Every entropy scalar contains $O(n+1)$ selectors and hence $O((n+1)^2)$ factors $F_\pm$. Each factor expands into a fixed number of normalized-resolvent words of length at most two and coefficient mass $O_H(s)$. Selector normalizations and transport factors add total logarithmic mass $O((n+1)^2)$. Writing $q=n+1$, the expanded scalars therefore have
$$
L\le C_Lq^2,\qquad \log J_{\rm scalar}\le C_Jq^3,
\tag{13}
$$
where $L$ counts natural resolvent factors and $J_{\rm scalar}$ includes every absolute coefficient from signed endpoints and squared defects.

Let $J_A$ be the visible projector, $H_0=I-J_A$, and $Z_h(z)=z(zI-Q_h)^{-1}$. The exact Schur identity is
$$
\mathcal Z_h(z)=H_0Z_h(z)H_0-
\frac{H_0Z_h(z)J_AZ_h(z)H_0}{d_h(z)},\qquad
d_h(z)=(Z_h(z))_{AA}\ge\frac{z}{z+R_H}.
\tag{14}
$$
All parameters are $s$ or $t-1$, so $z\ge e^{20q}/2$ eventually and every denominator is at least $1/2$. Expanding $H_0=I-J_A$ changes (13) only by fixed constants.

Denominators differ between models and must be compared separately. Each $d_h$ is an observable visible-return scalar. The inequality $|d^{-1}-\widehat d^{-1}|\le4|d-\widehat d|$ and product telescoping bound the total denominator-Lipschitz mass by $e^{O(L)}$. This is absorbed in (13).

For any hidden word extended by zero at $A$, $\mu W1=2\pi_0WS$. Visible-projector insertions factorize the expanded physical scalars; the clock-Gram note's finite preparation recursion recovers the resulting visible-start expressions. No additional preparation or hidden readout is introduced.

## 5. Fifth-power clock accuracy budget

The [clock-Gram theorem](FIXED_CLOCK_GRAM_OBSERVABILITY.md) uses only a bounded sensitivity range, the original field rule and stationary preparation. Its equilibrium metric change depends on the visible/hidden partition, not the sensitivity histogram. Thus it applies to the broad competitor classes of Section 1.

For physical resolvent words of length $L=O(q^2)$, choose fractional-power filter degree
$$
M=\lceil C_Mq^3\rceil
\tag{15}
$$
and integer-time cutoff $J_{\rm cut}=0$. The omitted whole-clock tail is at most $e^{-az_{\min}}$, with $z_{\min}\ge e^{20q}/2$. This beats $e^{-Cq^3}$ for every fixed $C$ eventually. The target fast-spectral tail is $\rho_*^M$ for a fixed $0<\rho_*<1$, since the target full generators have a fixed spectral cap.

Before the expansion coefficients, the scalar transfer has deterministic error
$e^{CL}(e^{-az_{\min}}+\rho_*^M)$ and measurement error
$\exp(C(L+1)(M+1))\sqrt\delta$. Choose the fixed $C_M$ sufficiently large to beat the coefficient and denominator-Lipschitz mass in (13)–(14). Every exact entropy scalar then differs between target and rival by at most
$$
e^{C_{a,H}q^5}\sqrt\delta+e^{-c q^3}.
\tag{16}
$$
No heat-polynomial approximation, generator differentiation or control convexification is used here. The rival kernels entering repair are the exact positive kernels of Sections 2–3.

Choose a fixed $C_*$ sufficiently large and require
$$
\delta\le\delta_n=e^{-C_*(n+1)^5}.
\tag{17}
$$
Then (16) is at most $e^{-100n}$ for large $n$. Adding target defects gives $Z\ge z_*/2$ and every rival weighted-repair hypothesis with
$$
\Delta\le e^{-10n}.
\tag{18}
$$
Every observed clock word has at most $C_{a,H}q^5$ ticks: there are $O(q^2)$ resolvent blocks of polynomial degree $O(q^3)$, and Gram reversal adds only a constant multiplier. The finite preparation recursion uses no longer words. These bounds are independent of rival rates and dimension.

## 6. Entropy and unrestricted prediction

Weighted whole-word repair uses the rival's actual support $\{u_0>0\}$, with law $\nu_i=\mu_i u_0(i)^2/Z$. For sufficiently large $n$, (18) gives
$$
\sqrt\Delta\le\frac1{32\,2^n},\qquad
D\ge2^{3\cdot2^n/4}.
\tag{19}
$$
The repaired couplings and deterministic decoded bits add no physical states. Choosing the largest integer $n$ allowed by (17) yields $n=\Theta((\log(1/\delta))^{1/5})$, proving the reversible lower in (3).

For unrestricted prediction, the original nineteen-symbol stationary word chain has at most $1+19^\ell$ states and all-protocol/all-horizon error
$$
(1+2R_H^2)\left(\frac{3R_H}{1+3R_H}\right)^{\ell+1}.
\tag{20}
$$
It preserves the target's exact histogram and a finite rate cap, so it belongs to the broader comparison class here. This proves the polynomial upper. The original reversible prediction partition also remains admissible and supplies the stated sufficient count. The upper constructions work uniformly over every target index.

## 7. Matching unrestricted growth on a thirty-nine-field clock menu

Keep the same target family and broad competitor classes, and enlarge only the menu to
$$
\mathcal H_{39}=\{jH/38:0\le j\le38\}.
\tag{21}
$$
The existing [same-family target-only polynomial rank lower](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md#9-upper-bounds-and-the-unrestricted-lower-on-this-family), using the [general whole-side rank method](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md), permits arbitrary field-dependent Markov rivals, unbounded rates and arbitrary new states. Its generator basis remains available: the thirty-nine frequencies $0,1+\gamma,\gamma-1$ are distinct, making the exponential Vandermonde matrix invertible. Replacing its earlier convenient smaller spacing by $H/38$ changes only fixed constants in target spectral bounds and whole-side logarithm truncation. The retained sides still have degree $O_a(n)$ and coefficient mass $e^{O_a(n)}$, giving the same polynomial unrestricted lower.

Since $\{0,H\}\subset\mathcal H_{39}$, the new reversible lower also applies. On the **same target family**, without a union,
$$
D_{\rm all}^{(39,a)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{(39,a)}(\delta)\ge
\exp\!\left(\exp\!\left(c_{a,H}[\log(1/\delta)]^{1/5}\right)\right).
\tag{22}
$$
The additional fields are used for the unrestricted lower, not the reversibility penalty. The two-field main statement makes only a polynomial sufficient-count assertion for unrestricted prediction.

## 8. Scope and remaining quantitative questions

This theorem retains the original band $[k,3k]$, uses every fixed positive clock, removes rival rate and gap restrictions, and allows arbitrary rival actuator histograms within the bounded range. Its positive scalar calculus needs only two physical fields.

The original external field rule and bounded sensitivity range remain assumptions. The theorem does not cover arbitrary alternative field rules, unbounded sensitivities, experimental sample complexity or fitting runtime. Finite-grid discrimination and clock-observability constants can be large.

Improving the fifth-root exponent, proving the stronger fixed-clock uncapped law $\exp(c\delta^{-\alpha})$, and determining the exact reversible growth class remain open. Publication positioning and novelty assessment require the separate primary-source comparison. Manuscript drafting remains the final step.

