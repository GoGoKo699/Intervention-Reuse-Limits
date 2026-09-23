# Reversibility costs beyond an exponential kinetic field rule

[Tight-band fixed-clock theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Two-field capped theorem and rank lower](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [Positive selectors](POSITIVE_LABEL_SELECTORS.md) · [Fixed-clock Gram transfer](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [General endpoint entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) · [State–entropy-production comparison](STATE_ENTROPY_PRODUCTION_TRADEOFF.md)

**Interface extension, 23 September 2026.** The uncapped fixed-clock state lower does not require rivals to use an exponential kinetic function between the queried fields. It extends to state-dependent positive kinetic functions obeying a common local-balance ratio, uniform zero-field return rates and a fixed endpoint-rate interval. The original nineteen-level target and its band $[k,3k]$ remain unchanged.

On the original endpoint interval, this is an exact reparameterization of the existing two-field theorem. A wider fixed interval is also permitted by the positive-selector proof. The distinction matters: changing an unqueried kinetic curve does not enlarge the set of observed two-field behaviors.

## 1. Enlarged interface and state comparison

Fix $k,H>0$, a dimensionless clock $a>0$, and $G=9/100$. Retain the original nineteen-level lamp targets, including their original exponential field rule, stationary masses, hidden generators and total state counts. Choose fixed constants $0<\ell<u<\infty$ such that

$$
\ell\le e^{(-G-1)H}<e^{(G-1)H}\le u.
\tag{1}
$$

A rival may use any finite hidden space, positive stationary law $\mu$, field-independent stationary hidden generator $K$, and positive dimensionless functions $b_i(h)$. Its external rates are

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
\tag{2}
$$

with

$$
b_i(0)=1,\qquad \ell\le b_i(H)\le u.
\tag{3}
$$

The preparation is $(1/2,\mu/2)$ and the readout is $S=(-1,1_{\rm hid})$. All physical states count. There is no rival hidden-rate cap, lower gap, target alphabet, histogram or moment requirement. The ordinary reversible subclass imposes detailed balance of $K$ under $\mu$; this is the only difference from the unrestricted stationary class. All rivals retain one field-independent hidden generator.

For the two-field comparison, (2)–(3) are needed only at $0,H$. Positive kinetic functions at other fields can be chosen arbitrarily, subject to defining the protocols under consideration; they are not queried by this metric. In particular, neither analyticity nor a bound on field derivatives is required.

Let $D_{\rm all}^{\mathrm{kin},(2,a)}$ and $D_{\rm rev}^{\mathrm{kin},(2,a)}$ be worst-case minimal state counts over the original target family for uniform absolute mean error on protocols using $0,H$, with every positive segment and observation horizon an integer multiple of $a/k$. For sufficiently small $\delta$,

$$
\boxed{
\begin{aligned}
D_{\rm all}^{\mathrm{kin},(2,a)}(\delta)&=\delta^{-\Theta(1)},\\
D_{\rm rev}^{\mathrm{kin},(2,a)}(\delta)&\ge
\exp\!\left(\exp\!\left(c_{a,H,\ell,u}
[\log(1/\delta)]^{1/5}\right)\right),\\
p&=\frac{\log19}{\log(1+1/(3R_H))},\qquad R_H=e^{(1+G)H}.
\end{aligned}}
\tag{4}
$$

The displayed $p$ is one sufficient exponent for the unrestricted upper; it need not match the positive exponent in the lower. The original reversible sufficient count $\exp(C_1\delta^{-p}\log(2/\delta))$ also remains valid. Polynomial unrestricted necessity on these same two fields follows from the [new target-only rank argument](CAPPED_KINETIC_INTERFACE_SEPARATION.md#6-a-polynomial-unrestricted-lower-on-the-same-two-fields), which does not impose a rival rate cap or reversibility. At target index $n$, error $e^{-C_*(n+1)^5}$ forces at least $2^{3\cdot2^n/4}$ ordinary reversible states; finitely many words of at most $C(n+1)^5$ clock ticks suffice. Constants may depend on $a,H,\ell,u$, but not on rival rates or dimension.

No target states, labels or rates are changed. In particular its hidden band is $[k,3k]$ and its passive visible law is exactly the rate-$k$ telegraph law. The target's kinetic label encoding is retained; this is not a theorem that every alternative kinetic choice on a target remains hard.

## 2. Exact endpoint equivalence on the original interval

Suppose $\ell=e^{(-G-1)H}$ and $u=e^{(G-1)H}$. In any rival define

$$
g_i^{\mathrm{eff}}=1+\frac{\log b_i(H)}{H}\in[-G,G].
\tag{5}
$$

The original-rule model with these sensitivities, the same $K,\mu$, states, preparation and readout has exactly the same generators at $0,H$:

$$
e^{(g_i^{\mathrm{eff}}-1)H}=b_i(H),\qquad
\mu_i e^{(1+g_i^{\mathrm{eff}})H}
=\mu_i e^{2H}b_i(H).
\tag{6}
$$

Every two-field protocol mean is therefore identical, without approximation or state overhead. Conversely, every original-rule model belongs to the enlarged class. At this endpoint interval the two model classes have exactly the same two-field behaviors and minimal state counts. No property of $b_i(h)$ between the queried endpoints can be inferred from that observation class.

A larger interval in (1) permits endpoint rates outside the earlier actuator range. The following proof handles that genuine enlargement directly; it also identifies which interface assumptions the observation argument uses.

## 3. Gram recovery uses the equilibrium law and the zero-field normalization

Set $k=1$ for the proof. At either sampled field, put $B_h=\operatorname{diag}(b_i(h))$. The full generator is

$$
Q_h=
\begin{pmatrix}
-e^{2h}\mu B_h1 & e^{2h}\mu B_h\\
B_h1 & K-B_h
\end{pmatrix}.
\tag{7}
$$

Its stationary law is independent of the kinetic values:

$$
\pi_h(A)=\frac{1}{1+e^{2h}},\qquad
\pi_h(i)=\frac{e^{2h}\mu_i}{1+e^{2h}}.
\tag{8}
$$

The external stationary fluxes balance edge by edge, and $\mu K=0$. If $K$ is ordinarily reversible, so is $Q_h$ under $\pi_h$. Writing $A=e_Ae_A^{\mathsf T}$ and $E_h=e^{aQ_h}$, one has the unchanged identities

$$
\pi_h=(1+\tanh h)\pi_0-\tanh h\,e_A^{\mathsf T},
\qquad
E_h^{*\pi_0}=W_hE_hW_h^{-1},\quad
W_h=I+(e^{-2h}-1)A.
\tag{9}
$$

For $M(V)=\pi_0VS$ and $c(V)=e_A^{\mathsf T}VS$, stationarity at $H$ gives

$$
c(E_HV)=c(V)+(1+\coth H)[M(E_HV)-M(V)].
\tag{10}
$$

At zero, the condition $B_0=I$ makes the visible/hidden-equilibrium sector an exact rate-one telegraph chain. Hence, with $\rho=e^{-2a}$,

$$
e_A^{\mathsf T}E_0=\rho e_A^{\mathsf T}+(1-\rho)\pi_0,
\qquad
c(E_0V)=\rho c(V)+(1-\rho)M(V).
\tag{11}
$$

These are precisely the finite visible-row recursion and stationary adjoint identities used in the [clock-Gram proof](FIXED_CLOCK_GRAM_OBSERVABILITY.md). Rank-one visible-projector insertions still factorize, so all its sampled Gram formulas and contractive fractional-power resolvent approximations apply. Their target-cap assumption remains valid because the target itself is unchanged. No kinetic derivative, field interpolation, new preparation or rival spectral cap enters.

## 4. Hidden resolvents have no extra endpoint weights

Let $P=I-A$, $Z_h(z)=z(zI-Q_h)^{-1}$ and
$\mathcal Z_h(z)=z(zI-K+B_h)^{-1}$, the latter extended by zero at the visible coordinate. The generic one-visible-block inverse identity gives

$$
\mathcal Z_h(z)=PZ_h(z)P-
\frac{PZ_h(z)AZ_h(z)P}{d_h(z)},
\qquad d_h(z)=(Z_h(z))_{AA}.
\tag{12}
$$

This is the Schur complement of the $AA$ entry in the full inverse. It does not impose a special incoming-rate vector, and it introduces no unobserved factor of $B_h$ at either endpoint.

The visible no-jump contribution yields

$$
d_h(z)\ge\frac{z}{z+q_A^{\rm out}(h)},\qquad
q_A^{\rm out}(0)=1,\quad
q_A^{\rm out}(H)\le e^{2H}u.
\tag{13}
$$

Thus $d_h(z)\ge z/(z+C_A)$ for $C_A=\max\{1,e^{2H}u\}$, uniformly over all rivals. At the exponentially large frequencies used below, $d_h\ge1/2$. The model-dependent denominators are compared through their own observable visible-return scalars, with $|d^{-1}-\widehat d^{-1}|\le4|d-\widehat d|$. Products cost only $e^{O(L)}$ for a length-$L$ word, as in the frozen proof.

## 5. Positive selectors and the unchanged fifth-power budget

Set

$$
X=\frac{B_H-\ell I}{u-\ell},\qquad Y=I-X,
\qquad G_0(s)=(sI-K+I)^{-1},\quad
G_H(s)=(sI-K+B_H)^{-1}.
\tag{14}
$$

Both diagonal features lie in $[0,I]$ for every rival. The target feature values are the fixed distinct numbers

$$
x_\gamma=\frac{e^{(\gamma-1)H}-\ell}{u-\ell}.
\tag{15}
$$

They may all be interior to $[0,1]$. Define the exact positive selfadjoint contractions

$$
F_+=\frac{s^2}{2}(G_0XG_H+G_HXG_0),\qquad
F_-=\frac{s^2}{2}(G_0YG_H+G_HYG_0).
\tag{16}
$$

On the target, $\|F_+-X\|,\|F_--Y\|\le(2\Lambda+1+u)/s$ with $\Lambda=3$. The observable formulas are

$$
\begin{aligned}
F_+&=\frac{s}{u-\ell}(\mathcal Z_0-\mathcal Z_H)
-\frac{\ell-1}{2(u-\ell)}
(\mathcal Z_0\mathcal Z_H+\mathcal Z_H\mathcal Z_0),\\
F_-&=\tfrac12(\mathcal Z_0\mathcal Z_H+\mathcal Z_H\mathcal Z_0)-F_+.
\end{aligned}
\tag{17}
$$

They follow by symmetrizing $G_0-G_H=G_0(B_H-I)G_H$. The coefficients depend only on the fixed interval and $s$; their mass is $O_{\ell,u}(1+s)$. Entrywise positivity is supplied by the exact kernels (16), not by individual signed summands in (17).

The [positive-selector lemma](POSITIVE_LABEL_SELECTORS.md) applies to this finite target grid. Every interior value has a fixed positive beta polynomial $x^{2a_i}(1-x)^{2b_i}$ with a unique target-grid maximum. Endpoint squares are used only when the target list contains the corresponding endpoint. Consequently its construction with $s=e^{200(n+1)}$ gives positive selfadjoint selectors $A_i$ with target error at most $e^{-110n}$ for large $n$ and universal rival norm $e^{O(n)}$. A larger fixed interval changes the polynomial exponents, separation constants and starting index, not their dependence on $n$.

The zero-field identity $B_0=I$ leaves the transports unchanged:

$$
P_t=t(tI-K)^{-1},\qquad
\mathsf T_{cd}=8tA_cP_t^2A_d,\qquad t=e^{20(n+1)}.
\tag{18}
$$

They remain entrywise positive with reversed transports equal to stationary adjoints. Their target approximation error is $Ce^{-20n}$. Thus the original lamp identities, central mass $1/18$ and weighted-repair hypotheses remain available.

Each entropy scalar has $O(n^2)$ soft-feature factors. After (17) and the physical Schur expansion, natural/full resolvent word length is $L=O((n+1)^2)$ and logarithmic coefficient mass, including denominator sensitivity, is $O((n+1)^3)$. The clock-Gram proof with fractional filter degree $M=O((n+1)^3)$ and integer-time cutoff zero gives scalar transfer error

$$
e^{C(n+1)^5}\sqrt\delta+e^{-c(n+1)^3}.
\tag{19}
$$

All physical frequencies are at least $e^{20(n+1)}/2$, so their whole-clock tails are negligible. Only the target has the spectral cap used for the remaining filter error. At $\delta\le e^{-C_*(n+1)^5}$, the same weighted whole-word repair and entropy proof give $D\ge2^{3\cdot2^n/4}$ using at most $C(n+1)^5$ clock ticks. This proves the reversible lower in (4). Both older upper constructions remain admissible under (1)–(3).

The [new two-field rank proof](CAPPED_KINETIC_INTERFACE_SEPARATION.md#6-a-polynomial-unrestricted-lower-on-the-same-two-fields) supplies the unrestricted lower in (4). It truncates logarithm expansions only on the target, retaining finite left and right polynomials whose evaluations on a $D$-state rival form a matrix of rank at most $D$. The stationarity recursion (10)–(11) recovers its visible-projector insertions even for nonreversible rivals. The proof therefore needs neither a rival cap nor rival logarithm convergence. Arbitrary intermediate kinetic functions remain unqueried. This improves the earlier thirty-nine-field unrestricted-necessity statement to the same two-field menu used for the ordinary-reversibility lower.

## 6. Entropy-production corollary for bounded kinetic interfaces

The [general endpoint entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) applies more broadly than local balance. For actual external rates $q_{iA}=b_i^{\rm act}$ and $q_{Ai}=\mu_i c_i^{\rm act}$, it needs only a common lower return bound $b_i^{\rm act}\ge\alpha>0$, an injection bound $c_i^{\rm act}\le\beta<\infty$, and a controlled initial hidden density. No common ratio is needed for that response estimate itself. Its conclusion concerns hidden additive reversibilization; full fixed-field reversibility additionally requires an appropriate common ratio.

For the interface (2), suppose on the allowed field set

$$
b_i(h)\ge\ell_*>0,\qquad e^{2h}b_i(h)\le U_*<\infty.
\tag{20}
$$

The set includes zero, so (3) implies $\ell_*\le1\le U_*$. For the original preparation, the hidden initial density relative to $\mu$ is $1/2$. The general bound therefore applies in its simpler regime with $\alpha=k\ell_*$ and $\beta=kU_*$. If $K_{\rm sym}=(K+K^*)/2$ and $\sigma_0$ denotes the full zero-field stationary entropy-production rate under ordinary identity reversal, then

$$
\boxed{
\sup_{h(\cdot),T}|m_K[h](T)-m_{K_{\rm sym}}[h](T)|
\le \min\!\left\{2,
\frac{\sqrt{U_*}}{\ell_*}\sqrt{\frac{\sigma_0}{k}}\right\}.}
\tag{21}
$$

The supremum ranges over the allowed protocols and all horizons. Equation (8) gives detailed balance for the full symmetrized model at each fixed field, while $\sigma_0=\sigma_{\rm hid}/2$ because the zero-field hidden mass is $1/2$ and every external edge balances. These facts are why (21) is a comparison with a fully ordinary reversible predictor for the local-balance interface. The proof and the more general initial-density formula are supplied in the linked entropy note.

For two-field protocols, one may take

$$
\ell_*=\min\{1,\ell\},\qquad
U_*=\max\{1,e^{2H}u\}.
\tag{22}
$$

No bounds at unqueried fields are needed. For all fields in an interval, (20) must hold throughout that interval. Under the original exponential rule, $\ell_*=R_H^{-1}$ and $U_*=R_H$ recover the earlier constant $R_H^{3/2}$.

Additive reversibilization preserves every state, stationary mass, kinetic function and hidden exit rate. Therefore the same-state resource implication extends to this enlarged class:

$$
D_{\le\Sigma}^{\mathrm{kin},(2,a)}(\delta)
\ge D_{\rm rev}^{\mathrm{kin},(2,a)}(\varepsilon),\qquad
\varepsilon=\delta+
\frac{\sqrt{U_*}}{\ell_*}\sqrt{\Sigma/k}.
\tag{23}
$$

Combining (23) with (4) gives the fifth-root-log frontier at small $\varepsilon$, without a rival rate cap or histogram constraint. Under the additional common hidden exit cap $3k$, the [new capped kinetic theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md) supplies the stronger lower $D_{\le\Sigma}(\delta)\ge\exp(c\varepsilon^{-\alpha})$ on these same two fields and this broader kinetic class, still without histogram matching. The uncapped and capped frontiers remain distinct. The existing polynomial predictor with finite stationary entropy production also remains admissible.

## 7. Physical scope and remaining assumptions

The extension removes a prescribed exponential kinetic curve while keeping a common local-balance ratio. It retains a single field-independent hidden generator, uniform zero-field returns, the stated preparation and readout, and a fixed interval for the queried endpoint return rates. The proof identifies where each assumption enters; it does not prove those assumptions are necessary for every possible lower-bound route.

Ordinary identity reversal remains essential to the asserted competitor class. The separate [generalized-reversal construction](GENERALIZED_REVERSAL_PREDICTION.md) gives polynomial prediction with a nontrivial state involution on this target family, so the ordinary lower does not extend to that broader reversal convention. Stationary entropy production here is a path-irreversibility rate; it is not automatically driven heat or device power.

The target is still the constructed nineteen-level family. If an alternative target interface erases its distinctions, for example by giving every hidden state the same kinetic return function, the present label construction no longer applies. Neither arbitrary target interfaces nor arbitrary kinetic functions without the common local-balance relation are covered by the state lower. The entropy comparison itself has the broader, separately stated reset assumptions.
