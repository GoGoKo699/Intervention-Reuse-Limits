# A binary reversibility penalty without a rival rate cap

[Tagged target construction](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) · [Mixed observation theorem](MIXED_KILLED_WORD_OBSERVABILITY.md) · [Weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md) · [Earlier binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) · [Source comparison](BINARY_OBSERVATION_PRIOR_ART.md)

**Research theorem, 23 September 2026.** A fixed balanced binary actuator suffices for an uncapped superpolynomial cost of ordinary reversibility. On an explicit family of uniformly mixing targets, stationary nonreversible prediction has a polynomial sufficient state count, whereas every reversible predictor needs superpolynomially many states in the worst case. The competitors may build entirely new states with arbitrarily fast internal rates. The proof preserves the original field rule, exact histogram, preparation and readout.

This is a new target family. It uses rare diagnostic states and a very large fixed rate-to-gap ratio. It does not claim the earlier binary budget $6580k$, the tight band $[k,3k]$, a fixed positive control clock, or a matched uncapped growth law.

## 1. Statement and scope

Fix $k,H>0$ and $0<\gamma<1$. Let $\mathcal F_{\rm tag}$ be the family in the [construction lemma](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md), beginning at any sufficiently large fixed integer $n_0$. Its binary labels have exactly

$$
\mu(g=-\gamma)=\mu(g=+\gamma)=\tfrac12.
\tag{1}
$$

Every target has the original rates

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
\tag{2}
$$

stationary zero-field preparation $(1/2,\mu/2)$ and readout $S=(-1,1_{\rm hid})$. Its passive visible path law is exactly the rate-$k$ telegraph law. All states are counted, including every logical table entry, tag, chain vertex and balancing state.

For the unrescaled version of the construction, take

$$
B=5\times10^8,\qquad
 a=1+10^{-6},\qquad
 g_*=\frac{(\sqrt a-1)^2}{100a}>0.
\tag{3}
$$

Target exits are at most $Bk$ and the nonzero hidden relaxation rates lie in $[g_*k,2Bk]$, independently of $n$. Multiplying hidden rates by the fixed factor $1/g_*$ instead gives band $[k,2Bk/g_*]$ and exit cap $Bk/g_*$; this rescaling changes only constants in the conclusions. Neither version has an optimized rate-to-gap ratio.

Let $D_{\rm all}^{\rm tag,unc}(\delta)$ and $D_{\rm rev}^{\rm tag,unc}(\delta)$ be worst-case minimal total predictor state counts on this same family, for uniform absolute error at most $\delta$ in actual means over every bounded deterministic protocol and every horizon. Both classes retain (1)–(2), stationary preparation and binary readout on their own finite states. Neither has a rate cap or required lower gap; the second additionally has ordinary hidden detailed balance.

For sufficiently small $\delta$, fixed positive constants satisfy

$$
\boxed{
\begin{aligned}
D_{\rm all}^{\rm tag,unc}(\delta)&\le C_0\delta^{-p_B},\\
D_{\rm rev}^{\rm tag,unc}(\delta)&\ge
\exp\!\left(\exp\!\left(c_H\sqrt{\log(1/\delta)}\right)\right),\\
p_B&=\frac{\log2}{\log(1+1/(B e^{(1+\gamma)H}))}.
\end{aligned}}
\tag{4}
$$

The reversible sufficient count remains $\exp(C_1\delta^{-p_B}\log(2/\delta))$. Upper and lower reversible growth are not matched. A matching polynomial lower for unrestricted prediction is not asserted specifically for $\mathcal F_{\rm tag}$.

The reversible lower already uses the five fields $h_j=jH/4$, $0\le j\le4$, with arbitrary positive durations and arbitrarily fast switching. There is no uniform finite switching schedule or witnessing-horizon bound over all rivals. Artificial killing in the proof is not an additional physical control.

An optional common-family growth-class corollary is stated in Section 7: explicitly adjoining the earlier binary family supplies a polynomial unrestricted lower. The main separation (4) does not need that enlargement.

## 2. Positive approximate selectors and transports

Set $k=1$ and use the unrescaled target generator. The construction has $r=2^n$ addresses and

$$
36r2^r+100Nn+3\quad\text{total physical states},\qquad N=10^6.
\tag{5}
$$

Its logical core is the nineteen-level lamp graph, now entirely binary color zero. Eighteen signed port types are distinguished by private color-one tags; a remote color-one balancing state makes the full histogram exact. The positive tag filters use only binary labels, so rivals acquire no free port coordinates.

Write $P_s=s(sI-K)^{-1}$, $F_c=P_sD_cP_s$ for the binary color projectors, and

$$
s=e^{20Nn},\qquad \tau=e^{-100n},\qquad u=10^9.
$$

For each signed type $i$, the construction specifies $T_i=O(n)$ and $\kappa_i>0$ with $\kappa_i^{-1}\le e^{14Nn}$ and defines

$$
E_i=\frac{s^2}{4\kappa_i}
F_0F_1 e^{T_i(K-uD_0)}F_1F_0.
\tag{6}
$$

These operators are nonnegative and selfadjoint in every reversible rival. On the target, $E_i$ approximates the signed-type coordinate projector to operator-norm error at most $e^{-2300n}$ for sufficiently large $n$.

For a paired logical port $c$, put $E_c=E_{c,+}+E_{c,-}$. For each adjacent pair in the original logical graph, put

$$
\mathsf T_{cd}=\frac{16}{\tau}E_c e^{\tau K}E_d.
\tag{7}
$$

It is nonnegative in every rival and $\mathsf T_{dc}=\mathsf T_{cd}^*$. On the target,

$$
\|\mathsf T_{cd}-16D_cKD_d\|\le C e^{-100n}.
\tag{8}
$$

The ideal right-hand block is the original permutation transport between equally weighted ports, with norm one. The resolvent frequency $s$ and gate heat duration $\tau$ are chosen separately; their separation is necessary for the normalized selector and gate errors to vanish.

## 3. A probability law on the rival's actual states

Use the central port $0$, and define

$$
A=E_{0,+}+E_{0,-},\qquad u_0=A1,\qquad
v=(E_{0,+}-E_{0,-})1,\qquad Z=\|u_0\|_\mu^2.
\tag{9}
$$

Here $u_0$ is a vector, distinct from the scalar killing strength $u$. Positivity gives $|v|\le u_0$. In the ideal target, these are the central indicator and signed central query. Its central mass is

$$
z_n=\frac1{36W_0}\ge c_*e^{-100n}.
\tag{10}
$$

Build the four logical gates from the same triangular port itineraries as in the [nineteen-level proof](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md). Let $Q_b$ implement the addressed query using at most $9n$ cross-port factors (7), and let

$$
C_c=Q_cG_FQ_c^*,\qquad
v_b=Q_bv,\qquad q_b=Q_bu_0.
\tag{11}
$$

The flip word $C_c$ uses at most $18n+3$ cross-port factors. Empty query words are identities. The nonempty words and each $C_c$ have the central $A$ as an outer factor, so they have the support required by weighted whole-word repair. Also $|v_b|\le q_b$ exactly.

In the ideal target the query functions are $\sigma x_{a\oplus b}$ on the central port. Thus their squared norms equal $z_n$, the unsigned query and flip row defects vanish, and

$$
(-1)^{\mathbf1_{b=c}}\langle v_b,C_cv_b\rangle=z_n,
\qquad \|C_cv_b\|^2=z_n.
\tag{12}
$$

The actual positive filters satisfy approximate versions. Every relevant raw product has $O(n)$ factors, each target normalized gate has norm at most $1+C e^{-100n}$, and its distance from its ideal transport is $C e^{-100n}$. Telescoping gives vector errors at most $C'(n+1)e^{-100n}$, while ideal query vectors have norm $\sqrt{z_n}$. Consequently every squared row defect divided by $z_n$ and every norm/correlation defect divided by $z_n$ is at most $e^{-40n}$ for sufficiently large $n$. For example the latter is bounded by a constant times

$$
(n+1)e^{-100n}/\sqrt{z_n}
+(n+1)^2e^{-200n}/z_n
\le C''(n+1)^2e^{-50n}.
\tag{13}
$$

This calculation includes $|Z-z_n|/z_n$. It is important to divide by the actual small root mass rather than assume a fixed mass.

## 4. A quadratic logarithmic accuracy budget

All the hypotheses of [weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md), equation (2), are finite linear combinations of stationary hidden word scalars. Norms use reversed words, which are stationary adjoints because each rival is reversible. No unknown coordinatewise product or hidden preparation is introduced.

The largest word is the squared image norm $\|C_cv_b\|^2$, with at most $54n+6$ cross-port factors and two additional endpoint selectors. Expanding paired selectors and signed endpoints gives the following conservative budgets, with $q=n+1$:

| Quantity | Upper bound |
|---|---:|
| Cross-port factors | $60q$ |
| Individual signed selectors | $122q$ |
| Smoothed label factors $F_c$ | $488q$ |
| Total fixed killed and heat duration | $250Nq^2$ |
| Absolute scalar coefficient mass, including normalizations | $e^{2000Nq^2}s^{244q}$ |

Each selector has four smoothed factors, normalization $s^2/(4\kappa_i)$ and duration at most $2Nn$. Each cross-port factor contributes $16e^{100n}$. There are at most two choices per paired or signed selector and at most four absolute coefficients in a squared-defect expansion. These facts give the last row directly; every contribution is counted after expansion.

Apply [mixed-word observability](MIXED_KILLED_WORD_OBSERVABILITY.md) with fixed killing bound $U=10^9$ and interpolation degree

$$
M=1200q.
\tag{14}
$$

For all sufficiently large $n$, $s\ge s_U$ and $s\ge B_U(488q)$. The observed noise term, after the coefficient budget above, is at most $e^{C_Hq^2}\sqrt\delta$ for a fixed $C_H$. The truncation term is at most

$$
e^{2000Nq^2}s^{244q}\,2^{488q+2}6^{1200q+1}
 s^{488q-1200q-1}
\le e^{-Nq^2}.
\tag{15}
$$

Indeed $\log s=20Nn\ge10Nq$, so the negative power of $s$ beats $2000Nq^2$ by a fixed multiple of $Nq^2$; all remaining powers of two and six are only exponential in $q$.

Thus every required scalar has error at most

$$
e^{C_H(n+1)^2}\sqrt\delta+e^{-N(n+1)^2}.
\tag{16}
$$

Taking a sufficiently large fixed $C_*$ and

$$
\delta\le\delta_n:=e^{-C_*(n+1)^2}
\tag{17}
$$

makes (16) at most $e^{-400n}$, after increasing $n_0$ if necessary. Since $z_n\ge c_*e^{-100n}$, division by the root mass preserves an exponentially small error. Combining (13), (16) and the bound $Z\ge z_n/2$ shows that the rival satisfies every hypothesis of weighted repair with

$$
\Delta\le e^{-30n}.
\tag{18}
$$

The constants and starting index depend only on the fixed target construction and physical parameters, never on a rival's state count, rate cap or smallest stationary mass.

## 5. Repair, entropy and inversion

On the rival's own support $\mathcal S=\{u_0>0\}$ define

$$
\nu_i=\frac{\mu_i u_0(i)^2}{Z}.
\tag{19}
$$

The [weighted repair lemma](WEIGHTED_WHOLE_WORD_REPAIR.md) constructs stationary proof couplings and deterministic decoded bits on these same states. Equations (17)–(18) give, for sufficiently large $n$,

$$
\sqrt\Delta\le\frac1{32\,2^n},\qquad
\log_2|\mathcal S|\ge\frac34\,2^n.
\tag{20}
$$

Therefore target $n$ requires at least $2^{3\cdot2^n/4}$ reversible states at every tolerance below $\delta_n$. At a given small $\delta$, choose the largest integer $n\ge n_0$ satisfying $C_*(n+1)^2\le\log(1/\delta)$. Then $n=\Theta(\sqrt{\log(1/\delta)})$. Decreasing a fixed positive constant if necessary gives the reversible lower in (4).

The normalization and repair add no physical states. The large target's logical register and bit table are all counted in (5); an arbitrary rival is not assumed to carry those coordinates before the deterministic decoding is constructed.

## 6. Polynomial prediction without reversibility

Uniformize each target at its common exit bound $B$. The [stationary word-chain upper](BOUNDED_RATE_FINITE_FIELD.md) over two actuator symbols preserves the exact histogram, original field rule and stationary preparation, with all-protocol/all-horizon error bounded by

$$
(1+2R_H^2)\left(\frac{BR_H}{1+BR_H}\right)^{\ell+1},
\qquad R_H=e^{(1+\gamma)H}.
\tag{21}
$$

It has at most $1+2^\ell$ states, giving the polynomial upper in (4). It has a fixed rate budget, so it is admissible in the larger uncapped class. The prediction-partition reversible upper from the same note remains available and preserves the target's gap and cap. These upper constructions apply to every target index, not just the lower-bound witness sequence.

## 7. An explicit common-family growth-class corollary

Let

$$
\mathcal F_* = \mathcal F_{\rm tag}\ \cup\ \mathcal F_{\rm old,bin},
\tag{22}
$$

where $\mathcal F_{\rm old,bin}$ is the earlier fixed-budget binary target family with the same $k,H,\gamma$, histogram, preparation and readout. Both subsets have exits at most $Bk$ and gap at least $g_*k$. The old family's target-only rank lower permits arbitrary field-dependent Markov rivals with unbounded rates, as stated in [its Section 9](BINARY_REVERSIBILITY_LOWER_BOUND.md#9-a-polynomial-lower-for-unrestricted-prediction). Hence it supplies a polynomial unrestricted lower on this explicitly enlarged family. The common word-chain upper and the new tagged lower give

$$
D_{\rm all}^{*,\rm unc}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{*,\rm unc}(\delta)\ge
\exp\!\left(\exp\!\left(c_H\sqrt{\log(1/\delta)}\right)\right).
\tag{23}
$$

The union in (22) is part of this corollary, not an implicit change of the family in (4). The superpolynomial penalty already follows from (4) on the tagged family alone.

## 8. Scope and evidence

The result concerns ordinary reversibility of hidden kinetics and actual controlled means under the specified original rule. It does not compare arbitrary reversible field rules, approximate actuator histograms, learned models, experimental sample counts, parameter precision or runtime. Small tag weights and exponentially separated probe scales are explicit parts of the proof. The rate-to-gap constants and accuracy thresholds are conservative and can be extremely large or small.

The new binary target resolves existence of an uncapped binary superpolynomial penalty. It leaves open the same uncapped claim on the older budget-$6580$ family, a small target rate-to-gap ratio, a fixed-clock uncapped superpolynomial lower, and the stronger uncapped law $\exp(c\delta^{-\alpha})$. The bounds do not identify the exact uncapped reversible growth class. Manuscript drafting remains the final step.
