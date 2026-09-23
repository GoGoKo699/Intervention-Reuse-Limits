# Internal proof review of the tight-band and entropy-production advances

[Positive selectors](POSITIVE_LABEL_SELECTORS.md) · [Tight-band theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Uniform reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) · [State–entropy-production tradeoff](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) · [Earlier clock review](FIXED_CLOCK_INTERNAL_REVIEW.md)

**Review date: 23 September 2026. Status: mathematical PASS for the four new proof notes listed below.** A separate internal review role read the complete arguments, checked the operator identities and constants, and traced their use of the existing target, clock-Gram transfer and weighted repair. This is an internal mathematical audit, not external peer review, a novelty certification or an editorial assessment. No manuscript was drafted.

## 1. Reviewed claims and dependency boundary

| Proof note | Result reviewed | Outcome |
|---|---|---|
| `POSITIVE_LABEL_SELECTORS.md` | Positive selectors for a finite target alphabet from two physical fields; arbitrary rival labels in the same bounded interval | PASS |
| `TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md` | Original nineteen-level targets, unchanged band and states, uncapped reversible lower at every fixed clock, fifth-root logarithmic exponent | PASS |
| `ENTROPY_PRODUCTION_REVERSIBILIZATION.md` | Same-state arithmetic reversibilization with a uniform endpoint-mean estimate; finite-entropy-production perturbation upper | PASS |
| `STATE_ENTROPY_PRODUCTION_TRADEOFF.md` | Transfer of reversible state lower bounds to stationary entropy-production budgets, with distinct broad and capped classes | PASS |

The review uses the previously audited fixed-clock Gram theorem and weighted whole-word repair. It also checks the invoked original target's port masses, matching-edge rate, spectral band, unrestricted upper and whole-side rank lower. No existing historical proof is changed by these advances. Finite numerical fixtures, where supplied by the verification role, are corroborating checks; the conclusions here rest on the analytic arguments.

## 2. Positive selectors and the unchanged target

The interval condition is sufficient for the exact rival features

$$
X=\frac{B_H-b_-I}{b_+-b_-},\qquad Y=I-X
$$

to satisfy $0\le X,Y\le I$. No rival histogram, alphabet, centering, variance or port mass is used. The equilibrium law and fixed-clock preparation recursion are also independent of the sensitivity histogram. The finite target grid is used only to choose a positive polynomial that separates each target value.

The signs and normalization in the resolvent identity were checked directly from

$$
G_0-G_H=G_0(B_H-I)G_H.
$$

Its symmetrization gives the stated expressions for $F_+$ and $F_-$. Each exact feature is entrywise nonnegative, selfadjoint and contractive. The argument does not assume that either feature is positive semidefinite. Noncommutation causes no problem for

$$
T_i=F_+^{a_i}F_-^{2b_i}F_+^{a_i}:
$$

the middle even power is positive semidefinite, and the two outer factors are adjoints. All powers remain entrywise nonnegative.

The important target power estimate is relative to the normalized base $V_i=\phi_i(X)/w_i$, which has norm one on the target. If $\|T_i/w_i-V_i\|\le c_i/s$, then

$$
\|(T_i/w_i)^{m_i}-V_i^{m_i}\|
\le\frac{m_ic_i}{s}(1+c_i/s)^{m_i-1}.
$$

This verifies selector Eq. (13). Using only the universal rival norm $w_i^{-m_i}$ here would introduce an unnecessary exponential loss. With $m_i=O(n+1)$ and $s=e^{200(n+1)}$, the claimed target precision follows for all sufficiently large indices. Tiny fixed grid separation changes constants and the starting index, not the asymptotic power.

The gate frequency $t=e^{20(n+1)}$ is distinct from $s$. The identity

$$
P_t=\frac{t}{t-1}\mathcal Z_0(t-1)
$$

is exact. On the target, disjoint port projectors eliminate the identity term in $P_t^2$, and the spectral remainder gives

$$
\|8tD_cP_t^2D_d-16D_cKD_d\|\le216/t.
$$

The original matching rate is $1/16$, so the ideal block is precisely the norm-one logical transport. The new soft-selector transport error is $O(e^{-20n})$. No tag, hub change, additional state, new edge or rate rescaling is made. Target port mass remains $1/18$, total physical count remains $18r2^r+2$, and the hidden relaxation band remains $[k,3k]$.

## 3. Observation budget and entropy integration

An entropy scalar has $O(n+1)$ transports and hence $O((n+1)^2)$ soft-feature factors. Their observable expansion has natural-resolvent length $O((n+1)^2)$ and logarithmic coefficient mass $O((n+1)^3)$. The same bounds include signed endpoints, selector normalizations, gate prefactors and squared defects.

All natural Laplace parameters grow at least as $e^{20(n+1)}/2$. The physical Schur denominator is therefore at least $1/2$ uniformly over rivals, using only the external rate bound. It is model-dependent and is compared as a separate observable scalar; inverse-product Lipschitz costs are included. No common denominator is silently imposed across models.

In the clock-Gram theorem, fractional degree $M=C_M(n+1)^3$ and integer cutoff zero suffice. The target spectral filter tail absorbs the coefficient mass after choosing the fixed $C_M$ large enough. The omitted whole-clock tail is superexponentially small in $n$. The measurement amplification and witness length are consequently

$$
\exp(C(n+1)^5)\sqrt\delta,
\qquad O((n+1)^5)\text{ clock ticks}.
$$

The exact positive rival kernels, not their signed observable expansions, enter repair. The central nonnegative selector $A$ gives $u_0=A1$ and $|v|\le u_0$. Outer factors ensure the required support for nonempty queries and flips; empty queries start on the same support. Target word defects are $O(ne^{-20n})$, hence below $e^{-15n}$ eventually. Absolute scalar error $e^{-100n}$ and the fixed mass $1/18$ give the stated repair parameter $\Delta\le e^{-10n}$. This is more than sufficient for $\sqrt\Delta\le1/(32\,2^n)$ and the lower count $2^{3\cdot2^n/4}$.

The two-field theorem claims a polynomial unrestricted upper only. Its separate thirty-nine-field corollary obtains a polynomial unrestricted growth class on the same target family. For that corollary the target frequencies $0,1+\gamma,\gamma-1$ are distinct, so spacing $H/38$ gives an invertible exponential Vandermonde matrix. Target-only logarithm truncation retains degree $O_a(n)$ and coefficient mass $e^{O_a(n)}$. The rival rank factorization does not require a rival alphabet, rate cap or logarithm expansion. No family union is needed for this new corollary.

## 4. Uniform reversibilization and its constants

For a stationary hidden generator, $K^*$ has the same diagonal as $K$. Thus $L=(K+K^*)/2$ preserves every exit rate and the stationary law, and is reversible. Every edge used by $K$ is present in $L$, so $d(K\|L)$ is finite even for one-way edges. Pairwise flux calculation gives

$$
d(K\|L)\le\sigma_{\rm hid}(K)/4.
$$

The factor $1/4$ was checked using the stated derivative inequality. It is consistent with the ordered-sum entropy-production convention. Zero pairs and infinite-entropy one-way pairs are covered.

The reset decomposition uses rate $\alpha=k/R$ to the existing visible state. It adds no physical state or transition beyond a decomposition of the original rates. For the residual process the hidden density obeys the $K^*$ forward equation, with nonnegative killing and source at most $kR$. Its maximum is at most $c_0+kRt$, where $c_0=0$ after a reset and $c_0=1/2$ for the original preparation. This is independent of hidden rates and minimum mass.

Conditional path relative entropy on the final reset-free segment is bounded by $d(c_0\tau+kR\tau^2/2)$. Mixing over the last-reset age, including the no-reset atom, yields

$$
D(p_K(T)\|p_L(T))\le dR^3/k.
$$

The no-reset $T e^{-\alpha T}/2$ term is included; it fits below the same uniform bound because $R\ge1$. Pinsker then gives

$$
|m_K-m_L|\le\sqrt{R^3\sigma_{\rm hid}/(2k)}
=R^{3/2}\sqrt{\sigma_0/k}.
$$

The last equality uses the full zero-field entropy-production rate $\sigma_0=\sigma_{\mathrm{hid}}/2$. At a constant field, the hidden stationary mass gives the separate factor $e^h/(2\cosh h)$. Neither formula identifies this stationary rate with total entropy produced under an arbitrary changing protocol. The theorem bounds endpoint laws and means, not full path relative entropy uniformly in horizon.

For the finite-entropy-production upper, $K_\epsilon=(1-\epsilon)K+\epsilon K^*$ preserves all exits and makes every used edge bidirectional. The ordered entropy sum is bounded by $Bk\log((1-\epsilon)/\epsilon)$. Equal exits allow a maximal jump coupling with disagreement rate at most $\epsilon Bk$. The same reset argument gives mean change at most $2BR\epsilon$. Both constants and the zero-exit case check.

## 5. Resource quantifiers and physical scope

The comparison

$$
D_{\le\Sigma}(\delta)\ge
D_{\rm rev}\bigl(\delta+R^{3/2}\sqrt{\Sigma/k}\bigr)
$$

holds for each target before the supremum is taken. It does not interchange target-dependent minimizers. Exit caps and exact histograms are preserved when imposed; a separately required lower gap would need additional justification and is not imposed here.

The broad two-field frontier uses the new uncapped fifth-root theorem. The stronger $\exp(c\varepsilon^{-\alpha})$ frontier retains the older common exit cap $3k$ and exact histogram. Inverting the latter for a polynomial uniform state budget gives the stated lower of order $k[\log(1/\delta)]^{-2/\alpha}$ on the entropy-production budget. This is a worst-case family statement, not a dissipation requirement for every target. The same-state perturbation upper gives finite full entropy production $O(k\log(1/\delta))$ at polynomial state count, without asserting that the two bounds match.

The new claims retain the original external field rule, bounded actuator range and specified preparation/readout. Entropy production uses ordinary identity reversal. The notes correctly distinguish that Markov path statistic from a proved heat cost, generalized reversal with odd variables, physical stationary Shannon entropy, experimental sample complexity or fitting time. The asymptotic bounds have large fixed constants and do not establish a practically conditioned finite instance or an external novelty judgment.

## 6. Deferred exploration

An optional scratch derivation studies approximate actuator purity from constant-field clock moments. It is not needed for any reviewed theorem and is not promoted as a repository result in this checkpoint. Direct interval-positive selectors already remove the rival histogram and finite-alphabet promises. Extending the allowed rival sensitivities beyond the interval used to normalize the positive features would require a separate argument.

No unresolved mathematical issue was found in this review. Further checking should address a concrete new claim or identified risk rather than repeat the completed audit.
