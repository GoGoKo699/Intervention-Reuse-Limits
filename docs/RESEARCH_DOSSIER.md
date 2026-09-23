# Research dossier for eventual manuscript preparation

[PRL exploration](PRL_EXPLORATION.md) · [Claim ledger](CLAIM_LEDGER.md) · [Publication scope](PUBLICATION_SCOPE.md) · [Source audit](PRIOR_ART.md) · [Verification](VERIFICATION.md) · [Current work](../work_orders/CURRENT.md)

**Planning record, 23 September 2026.** This document organizes research before drafting. PRL remains the selected target; no manuscript is drafted here. The preceding published baseline is `c6b8194`, with thirty-five mathematical verifiers. The new finite construction, perturbation theorem and physical interpretation are indexed as R27–R30 in the [ledger](CLAIM_LEDGER.md). Two new bounded verifiers supplement analytic derivations. Full-suite and remote-CI evidence is recorded in [Verification](VERIFICATION.md); neither internal checks nor source comparisons certify external validation or novelty.

## 1. Recommended scientific focus and result hierarchy

The principal asymptotic candidate remains the [kinetic-interface and reversal comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) on the original nineteen-level targets. Their hidden relaxation band remains $[k,3k]$ and their count remains $18r2^r+2$, with $r=2^n$. With a common hidden exit cap $3k$, every fixed positive clock and the same two fields $0,H$ give

$$
D_{\rm all}(\delta)=D_{\rm gen}(\delta)=\delta^{-\Theta(1)},
\qquad D_{\rm ord}(\delta)=\exp(\delta^{-\Theta(1)}).
$$

Here $D_{\rm ord}$ requires ordinary detailed balance, while $D_{\rm gen}$ permits a stationary-law-preserving hidden involution $\theta$ with $K^*=\Theta K\Theta$ and an even actuator. The equalities specify growth classes, not matching exponents or pointwise equality of state counts. Rivals may choose arbitrary bounded state-dependent kinetic barriers with $q_{iA}=k b_i(h)$, $q_{Ai}=k\mu_i e^{2h}b_i(h)$ and $b_i(0)=1$. They need no target alphabet, histogram, moments, topology or lower gap. The equilibrium block tilt, field-independent hidden generator, preparation and readout remain shared. The [capped proof](CAPPED_KINETIC_INTERFACE_SEPARATION.md) gives a witnessing horizon $O(\log(1/\delta)/k)$ on the same two-field menu for both necessary growth classes.

Removing the rival rate cap preserves polynomial unrestricted growth on these same two fields and the weaker ordinary-reversible lower

$$
D_{\rm ord}^{\rm unc}(\delta)\ge
\exp\!\left(\exp\!\left(c_{a,H,\ell,u}[\log(1/\delta)]^{1/5}\right)\right).
$$

The [uncapped kinetic-interface theorem](GENERAL_KINETIC_INTERFACE.md) now incorporates the target-only two-field rank lower. Thus its unrestricted growth class is matched without enlarging the menu to thirty-nine fields. Its ordinary-reversible upper and lower remain unmatched. At target index $n$, the ordinary-reversible witness uses $O((n+1)^5)$ clock ticks at error $e^{-C(n+1)^5}$. No target tags or rate rescaling are introduced, and neither result charges the number or precision of mean experiments.

A second main result supplies a quantitative resource bridge for this broader kinetic class. Under $b_i(h)\ge b_{\min}>0$ and $e^{2h}b_i(h)\le c_{\max}$, [same-state reversibilization](GENERAL_INTERFACE_ENTROPY_BOUND.md) changes every controlled endpoint mean by at most $(\sqrt{c_{\max}}/b_{\min})\sqrt{\sigma_0^{\rm id}/k}$, with no hidden cap or minimum stationary mass. Consequently

$$
D_{\le\Sigma}^{\rm id}(\delta)\ge
D_{\rm ord}\!\left(\delta+\frac{\sqrt{c_{\max}}}{b_{\min}}\sqrt{\Sigma/k}\right).
$$

The [new capped frontier](KINETIC_PARITY_RESOURCE_TRADEOFF.md) uses $\exp(c\varepsilon^{-\alpha})$ without an exact rival histogram or exponential barrier rule; the common exit cap $3k$ remains an assumption of that stronger lower. The uncapped class inherits the fifth-root-log lower. The [centered-word construction](GENERALIZED_REVERSAL_PREDICTION.md) attains polynomial prediction with exactly zero stationary entropy production under its own generalized reversal. It can also have finite ordinary entropy production $O(k\log(1/\delta))$ after regularization. These are different reversal conventions. If retained configurations are physically even, identity reversal is the relevant convention; a mathematically chosen involution does not by itself establish a physical realization. No universal heat or dissipation necessity follows, and zero stationary generalized entropy production does not imply zero production during a changing protocol.

| Role | Results to retain | Reason for inclusion |
|---|---|---|
| Principal comparison | [Capped kinetic separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md); [kinetic/parity resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | Same two fields and exit cap: polynomial unrestricted/generalized-reversible growth versus exponential ordinary-reversible growth. |
| Uncapped comparison | [General kinetic interface](GENERAL_KINETIC_INTERFACE.md) | Matched polynomial unrestricted growth on the same two fields; fifth-root-log ordinary lower without a rival cap or histogram promise. |
| Reversal boundary | [Generalized-reversal prediction](GENERALIZED_REVERSAL_PREDICTION.md) | Centering a word predictor makes the actuator even and preserves its controlled response; generalized stationary entropy production is exactly zero. |
| Positive observation mechanism | [Finite-alphabet positive selectors](POSITIVE_LABEL_SELECTORS.md); [clock Gram recovery](FIXED_CLOCK_GRAM_OBSERVABILITY.md) | Exact positive rival kernels are recovered through target-sensitive scalar estimates; only the target alphabet is finite. |
| Physical resource bridge | [General interface entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md); [kinetic/parity frontier](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | Relates state, fidelity and identity-reversal path irreversibility; retains explicit interface and reversal assumptions. |
| State mechanism and upper | Weighted whole-word repair; original lamp identities; stationary word-chain upper | Converts measured scalar relations to state necessity and supplies smaller stationary predictors. |
| Historical quantitative scopes | Tagged binary fixed-clock and arbitrary-switching results; older capped comparisons | Retains binary actuation and stronger bounds under their distinct assumptions. |
| Structural controls and foundations | Passive/step/switching, local paths, fresh realization versus aggregation, rate/closure and response results | Identifies the task and architecture restrictions under which smaller reversible predictors exist. |

The [new finite example](FINITE_REVERSIBILITY_ADVANTAGE.md) supplies a distinct, fully specified 12-state equilibrium target and an exact 11-state stationary nonreversible predictor. Every at-most-11-state ordinary-reversible rival in the shared kinetic interface with hidden exit cap $2k$ has mean error greater than $2^{-3000}$. The lower uses fields $0,\log2$, clock $(\log2)/(8k)$ and at most 1200 ticks per witness. The target has six kinetic labels and is generally uncentered; it is not a member of the original nineteen-level family. Its 11-state upper is unrestricted, with no claimed generalized reversal. The underlying completely positive Gram mechanism is classical matrix theory; [source comparison](FINITE_ADVANTAGE_SOURCE_AUDIT.md) separates that mechanism from the explicit controlled realization and finite certificate.

A [single-force network](SINGLE_FORCE_CONFORMATIONAL_MODEL.md) makes the ordinary parity and kinetic actuation concrete within a stipulated conformational model. Equal well extensions, calibrated zero-force returns and internal saddle extensions remain model assumptions, not a demonstrated molecule. [Uniform robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md) permits small deviations, including weak control-dependent hidden rates and finite ramps, at an explicit accuracy floor. The [closure theorem](PHYSICAL_REVERSAL_REALIZATION.md) explains why an even equilibrium observation that is Markov must obey ordinary detailed balance.

Finite existence is now established, but a useful tolerance and sample budget remain open. The next priorities are to sharpen the small certificate or construct a stronger small example, and to test the stipulated force model against a conventional microscopic model. Arbitrary interfaces, unrestricted control-dependent hidden dynamics, matching entropy-production frontiers and the older-family binary uncapped problem remain open. Manuscript drafting remains the last step.

## 2. Common model and notation

Use the row-generator convention throughout. A target has a visible state $A$ and a finite hidden set $\mathcal B$, with positive stationary probability $\mu$ and internal generator $K$. The readout is $S(A)=-1$, $S(z)=+1$ on $\mathcal B$. The original targets retain the following rule, a subclass of the broader kinetic competitor interface below. For $k>0$ and a dimensionless scalar field $h$,

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},\qquad
q_{zz'}(h)=K_{zz'}\quad(z\ne z').
$$

Diagonals make row sums zero; column probabilities satisfy $\dot p=Q(h)^Tp$. The original centered target families have $\mu K=0$, $\mu_zK_{zz'}=\mu_{z'}K_{z'z}$, and $\sum_z\mu_zg_z=0$. The new six-label finite target keeps stationarity and detailed balance but does not impose centering. Preparation is $\pi_0=(1/2,\mu/2)$. Its fixed-field equilibrium is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h},\qquad
\mathbb E_{\pi_h}S=\tanh h.
$$

At zero field, both visible-block exit rates are $k$. Strong lumpability gives the complete rate-$k$ telegraph path law, requiring exactly two fixed-readout states. This is stronger than matching a correlation function. The [model derivation](THEORY.md) also distinguishes a nonuniform kinetic actuator from a block-uniform potential tilt, which can preserve lumpability after intervention.

| Symbol | Meaning and convention |
|---|---|
| $k$ | External transition scale; restoring it changes time units, not state counts. |
| $K,Q(h)$ | Hidden generator and full physical generator, respectively. Internal budgets concern $K$, not the full exit rate of $Q(h)$. |
| $\mu,\pi_h$ | Hidden stationary law and full fixed-field equilibrium. |
| $g,G,W$ | Sensitivity, bound $\lvert g\rvert\le G$, and variance $W=\sum_z\mu_zg_z^2$. |
| $H$ | Fixed positive field bound; allowed inputs satisfy $\lvert h(t)\rvert\le H$. |
| $m$ | Number of actuator values when used as an alphabet size; $m_F[h](t)$ denotes a mean. |
| $B,\Lambda$ | Dimensionless internal exit budget $Bk$ and reversible relaxation cap $\Lambda k$. They are different constraints. |
| $a$ | Dimensionless fixed control-clock spacing; positive held segments have lengths in $(a/k)\mathbb N$. |
| $D,N$ | Total physical predictor and target state counts, including $A$. |
| $D_{\rm all},D_{\rm gen},D_{\rm ord}$ | Worst-case counts with stationarity only, a permitted reversal involution, or ordinary detailed balance. The resource note calls the last two $D_{\rm inv},D_{\rm id}$. |
| $b_{\min},c_{\max}$ | Dimensionless return lower bound and entrance-density upper bound: $b_i(h)\ge b_{\min}$ and $e^{2h}b_i(h)\le c_{\max}$. |
| $n,r$ | Register width and number of lamp addresses, $r=2^n$. |
| $\delta$ | Uniform error in the actual controlled mean. |
| $\sigma_{\rm hid},\sigma_0,\Sigma$ | Hidden stationary entropy-production rate, full zero-field rate $\sigma_0=\sigma_{\rm hid}/2$, and its budget, under ordinary identity reversal. |
| $\varepsilon,u,m_j$ | In response calculations, $h=\varepsilon u$ and $m_j$ is the coefficient of $\varepsilon^j$, including the factorial convention; coefficient error is a separate tolerance. |
| $C(t)$ | Cubic kinetic kernel $\langle g,e^{Kt}g\rangle_\mu$; complete finite-field information only in the stated rank-one subclass. |
| $\alpha,\zeta,p,c,C$ | Positive growth exponents and constants local to each theorem. Reusing a Greek letter does not identify exponents across notes. |

Ordinary reversibility means detailed balance with a positive stationary law, with identity reversal on retained states. For both the original rule and $q_{iA}=k b_i(h)$, $q_{Ai}=k\mu_i e^{2h}b_i(h)$, it is equivalent to hidden detailed balance: the external edges already balance. A stationary nonreversible hidden model has the same fixed-field stationary distribution. Generalized reversibility instead permits an involution $\theta$ preserving $\mu$ and every $b_i(h)$, fixing $A$, and satisfying $K^*=\Theta K\Theta$. It is a different competitor requirement. Its physical interpretation requires identifying the actual time-reversal parity of the retained variables; the all-even case has $\theta=\mathrm{id}$.

## 3. Error, quantifiers and counted resources

For a target $F$ and one predictor $\widehat F$, define

$$
\mathcal D_H(F,\widehat F)=
\sup_{T>0}\ \sup_{\substack{h:[0,T]\to[-H,H]\\h\text{ deterministic, piecewise continuous}}}
\ \sup_{0\le t\le T}
\left|m_F[h](t)-m_{\widehat F}[h](t)\right|.
$$

For the new principal comparison, restrict this supremum to fields $\{0,H\}$, held segment lengths in $(a/k)\mathbb N$, and observation times at clock endpoints; denote the resulting norm $\mathcal D_{a,\{0,H\}}$. Define the corresponding worst-case state count by the same supremum/infimum below with that norm. The nonreversible upper serves all bounded protocols and horizons, hence also this restricted menu. The reversible lower already holds in the restricted norm.

Preparation occurs once at the start; changing a held field does not reprepare the state. A predictor is chosen from the known target and requested tolerance, before choosing the protocol or horizon. Constant fields generate time-homogeneous dynamics; rates depend on the current scalar field, with no additional supplied memory or clock coordinate outside the counted model. The principal theorem fixes binary readout and stationary zero-field preparation. The broader rank lower allows fixed real readouts and arbitrary fixed preparations, as specified in its proof.

For target family $\mathcal F$ and admissible architecture $\mathcal C(F)$, the state requirement is

$$
D_{\mathcal C}(\delta)=
\sup_{F\in\mathcal F}\inf\left\{
|\widehat F|:\widehat F\in\mathcal C(F),\ 
\mathcal D_H(F,\widehat F)\le\delta
\right\}.
$$

Thus an upper bound constructs a predictor for every target, while a lower bound supplies a hard target at each sufficiently small accuracy. It is not a statement that every target is hard, or that a single finite target has unbounded cost as $\delta\downarrow0$. Constants are uniform over target size at fixed stated physical parameters. The lower-bound target may depend on accuracy.

All hidden configurations, registers, signs, ports, corridor vertices, hubs, ballast and any retained memory states count. For example, the historical tagged binary target has $36r2^r+100Nn+3$ total states with the fixed constant $N=10^6$; the older binary target has $224r2^r+4$; the nineteen-level target has $18r2^r+2$. The large target itself is never treated as a free oracle inside the reduced model. State count does not charge parameter precision, the description complexity of rate functions, construction time, integration time or experimental samples. Constructions receive the target model; this is compression after specification, not identification from passive data.

The shorthand $\delta^{-\Theta(1)}$ means upper and lower bounds with fixed positive, potentially different exponents. Likewise $\exp(\delta^{-\Theta(1)})$ denotes a growth class; the explicit reversible upper is $\exp[C\delta^{-p}\log(2/\delta)]$. It does not assert a matched exponent or an exact power law.

## 4. Principal theorem boundaries and physical assumptions

The principal target is exactly the original nineteen-level lamp family, with zero-level hidden mass $1/2$ and each nonzero level $\pm j/100$ of mass $1/36$. Its target band is $[k,3k]$. In the current kinetic class, rivals retain the hub, equilibrium block tilt, one field-independent hidden generator, stationary preparation and binary readout. Their barrier functions obey $b_i(0)=1$ and a fixed bounded endpoint interval at $H$, with no target alphabet or histogram requirement. The capped theorem permits endpoint lower bound zero; the general entropy bridge requires a strictly positive return lower bound on the protocols being compared. The stronger exponential ordinary lower uses common exits at most $3k$; the fifth-root-log lower permits arbitrary rival rates.

The [capped two-field proof](CAPPED_KINETIC_INTERFACE_SEPARATION.md) recovers the diagonal endpoint barrier and hidden generator from two full generators, uses exact nonnegative squared-Lagrange selectors and the positive update $I+K/(3k)$, and transfers $O(n)$-degree words using the common cap. Its separate target-only rank proof needs no rival cap and supplies polynomial unrestricted necessity on those same two fields. The [generalized upper](GENERALIZED_REVERSAL_PREDICTION.md) uses word reversal and the middle-symbol actuator; it retains the existing all-protocol prediction guarantee and exit cap. These additions strengthen the current comparison without rewriting the earlier proof scopes below.

The [complete tight-band proof](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) has $O((n+1)^2)$ natural-resolvent factors and logarithmic coefficient mass $O((n+1)^3)$. Fractional clock degree $M=O((n+1)^3)$ with zero integer-time cutoff gives logarithmic noise amplification and witness length $O((n+1)^5)$. Exact positive operators act on the rival's own states; signed expansions recover their scalar tests. The [new internal review](PRL_EXPLORATION_INTERNAL_REVIEW.md) records the selector, integration and entropy-production checks.

The [historical binary fixed-clock theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) retains its different construction: balanced binary labels, rare tags, fixed hidden-rate scaling $\eta=(e^{(\gamma-1)H}-e^{(-\gamma-1)H})/10^9$, a positive but potentially tiny uniform gap, and a very large fixed rate-to-gap ratio. Its inner exponent is $1/12$; only its separate five-field union corollary asserts polynomial unrestricted growth. The new nineteen-level theorem does not change that binary claim or solve the binary target-band problem.

The following arbitrary-switching comparison retains its own original scaling and stronger inner exponent. For that historical binary tagged family, let $B=5\times10^8$ and $g_*=(\sqrt{1+10^{-6}}-1)^2/[100(1+10^{-6})]$. Targets have exit cap $Bk$ and relaxation band $[g_*k,2Bk]$. Rescaling hidden rates by the fixed factor $1/g_*$ gives a unit-gap convention with a correspondingly larger fixed exit cap. Rival classes have no rate cap or required lower gap. The shared original rule, preparation/readout and exact balanced binary histogram remain essential.

$$
D_{\rm all}^{\rm tag,unc}(\delta)\le C_0\delta^{-p_B},\qquad
D_{\rm rev}^{\rm tag,unc}(\delta)\ge
\exp\!\left(\exp\!\left(c_H\sqrt{\log(1/\delta)}\right)\right),\qquad
p_B=\frac{\log2}{\log(1+1/(Be^{(1+\gamma)H}))}.
$$

The positive filters use exponentially small private-tag entrance rates, a weakly biased color-zero chain, fixed artificial killing, and separated resolvent and heat scales. These are explicit proof/construction costs; no parameter-precision or experimental-efficiency conclusion is supplied. The lower uses five fixed field values with arbitrary durations and rapid switching, without a uniform finite switching schedule or witnessing horizon over all rivals. The [full theorem, Section 7](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md#7-an-explicit-common-family-growth-class-corollary) identifies the precise enlarged family on which unrestricted growth is also bounded below polynomially.

For the earlier arbitrary-switching uncapped nineteen-level comparison, the target band remains $[k,3k]$, the histogram is the same as in the fixed-budget table below, and rivals retain the original rule, preparation and readout. There is no rival rate cap or lower-gap requirement. For sufficiently small $\delta$,

$$
c_0\delta^{-\zeta}\le D_{\rm all}^{\rm unc}(\delta)\le C_0\delta^{-p},\qquad
\exp\!\left(\exp\!\left(c_1\sqrt{\log(1/\delta)}\right)\right)
\le D_{\rm rev}^{\rm unc}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log(2/\delta)\right).
$$

The lower uses the existing thirty-nine field amplitudes with arbitrary positive durations and arbitrarily fast switching. That earlier proof does not establish a superpolynomial lower at each fixed positive control clock; the new theorem above does so by a different route. The following table concerns the stronger fixed-budget comparisons, whose clock guarantees remain separate.

| Item | Binary theorem | Nineteen-level theorem |
|---|---|---|
| Hidden histogram | $\mu(g=\pm\gamma)=1/2$, fixed $0<\gamma<1$ | $\mu(g=0)=1/2$; $\mu(g=\pm j/100)=1/36$, $j=1,\ldots,9$ |
| Common internal exit budget | $6580k$ | $3k$ |
| Target and reversible-upper band | $[k,13160k]$ | $[k,3k]$ |
| Rival lower-gap requirement | None | None |
| Lower-bound field menu | Five fixed amplitudes | Thirty-nine fixed amplitudes |
| Lower clock and horizon | Every fixed $a>0$; horizon $O_a(\log(1/\delta)/k)$ | Every fixed $a>0$; horizon $O_a(\log(1/\delta)/k)$ |
| Upper menu | Every allowed bounded protocol and horizon | Every allowed bounded protocol and horizon |
| State laws | Polynomial with reversibility optional / singly exponential reversible | Polynomial with reversibility optional / singly exponential reversible |

For the binary theorem, set $R_H=e^{(1+\gamma)H}$ and $p=\log2/\log(1+1/(6580R_H))$. The upper with reversibility optional is at most $1+\max\{2,[(1+2R_H^2)/\delta]^p\}$. The nineteen-level exponent replaces $2,6580,\gamma$ by $19,3,9/100$. These are sufficient, unoptimized exponents.

| Assumption | Mathematical purpose and physical interpretation | Boundary to retain |
|---|---|---|
| Shared equilibrium interface | Current competitors may choose arbitrary bounded barriers with $q_{Ai}/q_{iA}=\mu_i e^{2h}$ and $b_i(0)=1$. Two sampled fields recover the needed operators. | Arbitrary field-dependent hidden generators, unbounded endpoint barriers and different interface geometry remain outside the state lower. Local detailed balance alone does not supply the full hypothesis set. |
| Actuator range and histogram | The original finite target grid remains fixed; no rival alphabet, histogram or moments are required by the new capped or uncapped kinetic theorems. | Historical capped theorems retain their exact-histogram assumptions. The new proof needs a fixed bounded endpoint interval; the entropy bound also needs a positive return envelope. |
| Stationary preparation and fixed binary readout | Defines the actual laboratory-style mean interface used to recover word scalars. | Extra preparations, extra readouts or feedback are not supplied. |
| Exit budget / spectral cap, when imposed | Stabilizes the fixed-clock generator recovery. The older binary proof also needs $P=I+K/(6580k)$ entrywise nonnegative to preserve positive words. | The uncapped proofs replace raw generator recovery by bounded resolvent or mixed killed-semigroup words; the new target-sensitive proof respects a fixed clock without a rival cap. |
| Ordinary reversibility | Supplies adjoint word relations and stationary reverse transports when retained states are even under reversal. | Generalized reversal with an even actuator admits the polynomial centered-word upper; ordinary EPR is not a convention-independent dissipation cost. |
| Uniform target gap | Shows that hidden slow mixing is not needed for the obstruction. | A gap is not imposed on the lower-bound rival class. |
| Fixed target alphabet and bounded sensitivity/field ranges | Keeps selector and word-compression constants independent of target size; rivals may use a continuous range. | Changing the fixed ranges with accuracy, or allowing unbounded sensitivities, changes the resource problem. |

For reversible $K$, a relaxation cap $\Lambda k$ bounds every exit by $\Lambda k$; an exit cap $Bk$ bounds the real relaxation spectrum by $2Bk$. These implications are not equalities. In the binary upper the sharper exit budget follows directly from the known stochastic uniformization and from stationary-flux aggregation, despite the larger spectral band. The nineteen-level entropy lower permits any fixed rival cap $\Lambda k$; taking $\Lambda=6$ includes every reversible rival with exits at most $3k$. No cap-to-exit inference of the same form is asserted for general nonreversible spectra.

The energy/barrier realization in [Theory, Section 2](THEORY.md#2-detailed-balance-and-physical-interpretation) establishes consistency with a kinetic coupling, not a demonstrated molecular mechanism. Global refresh, hubs and complete lamp tables are explicit counted constructions. Fixed-clock lower bounds still use signed combinations of actual mean experiments with potentially large coefficients; they imply no measurement-noise or sample-efficiency guarantee.

### Fixed-clock target-sensitive observation

The exact stationary identity $\pi_h=(1+\tanh h)\pi_0-\tanh(h)e_A^{\mathsf T}$ recovers the visible-state row from finite suffix means. Rank-one projector insertions factor into these actual scalar data; stationary adjoints then expose Gram norms. For each physical resolvent, a contractive polynomial in $e^{aQ_h}$ has an explicit remainder controlled by $(I-e^{aQ_h})^{M+1}$ on the relevant vector. Its target norm decays exponentially under the target cap; the recovered Gram norm transfers that decay to a rival without bounding its full spectrum.

A Schur complement isolates the hidden killed resolvent. Two physical fields expose complementary positive soft features across the bounded actuator interval. Positive polynomial powers select each label only on the finite target grid; exact rival kernels remain nonnegative without a rival projector or histogram assumption. These [selectors](POSITIVE_LABEL_SELECTORS.md) and zero-field resolvent transports give the new fifth-power clock budget. The older binary route additionally uses killed-heat approximation and natural killing on its rescaled tagged target; that extra construction is not needed here.

### Same-state entropy-production comparison

Arithmetic reversibilization $(K+K^*)/2$ preserves the stationary law, barrier functions and every exit rate. For dimensional rates $q_{iA}\ge\alpha$ and $q_{Ai}\le\beta\mu_i$, a common reset and bounded hidden occupation give endpoint relative entropy at most $(\sigma_{\rm hid}/(4\alpha))\Psi(c_0,\beta/\alpha)$, with the explicit sharp reset-age envelope in the [general interface note](GENERAL_INTERFACE_ENTROPY_BOUND.md). The physical baseline gives mean error $(\sqrt{c_{\max}}/b_{\min})\sqrt{\sigma_0^{\rm id}/k}$. A common local-balance ratio makes the full comparator reversible; the endpoint estimate itself needs no such ratio. The comparison is applied before the target supremum. Both new kinetic frontiers omit histogram matching, while only the stronger one imposes cap $3k$. Ordinary path entropy production remains distinct from stationary Shannon entropy, protocol heat and generalized reversal.

### Bounded resolvent observability without a rate cap

The [bounded-control observability lemma](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) uses the affine span of the finite physical field menu. Modelwise rapid switching passes actual-mean accuracy to convexified protocols. One analytic parameter deforms the entire protocol, and a priori holomorphic bounds depend only on the bounded external operator, giving a fixed square-root error exponent independent of word length and hidden rates. Artificial absorbing or negative-killing coefficients are proof expressions, not added experimental controls.

Independent exponential dwell averages expose $P_s=s(sI-K)^{-1}$. Polarization and finite Chebyshev interpolation recover bounded label words of $P_s^2$ with explicit coefficient mass and tail bounds. Target cross-port resolvents approximate the exact gates; the [uncapped lower](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) controls all required scalar moments at accuracy $\delta_n=e^{-C(n+1)^2}$, then applies whole-word repair and entropy to force $2^{3\cdot2^n/4}$ rival states. Raw generator moments need not be close. No uniform bound on the Trotter switching frequency is claimed.

The [mixed-word extension](MIXED_KILLED_WORD_OBSERVABILITY.md) also inserts fixed-strength killed and ordinary heat semigroups between smoothed label factors. The binary proof applies it to positive rare-tag selectors, whose approximate port action is established only on the target. Their counterparts remain positive on arbitrary rivals. Weighted whole-word repair handles the rival's own positive normalization, including the exponentially small target root mass. The [full binary proof](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) gives the complete $e^{-C(n+1)^2}$ allocation and separates the tagged-family and enlarged-family conclusions.

### Rate-dependent and qualitative supporting results

The [state–speed–accuracy theorem](STATE_SPEED_ACCURACY_TRADEOFF.md) makes the nineteen-level proof uniform over a variable reversible spectral cap $\Lambda k$, $\Lambda\ge3$. For constants $c_H,C_0>0$ independent of accuracy and cap, its worst-case state requirement satisfies

$$
\log\log\mathcal D_{\rm rev}(\delta,\Lambda)
\ge c_H\frac{\log(1/\delta)}{\log(\Lambda+2)}-C_0,
\qquad 0<\delta<1.
$$

Its explicit finite-width criterion is $\delta\le[C_H(\Lambda+2)]^{-C_*(n+1)}$, which forces at least $2^{3\cdot2^n/4}$ states on target $n$. The shared thirty-nine-field menu uses a cap-dependent clock $a_\Lambda/k=1/[2k(\Lambda+R)]$, where $R=e^{(1+9/100)h_0}$ and $h_0=\min\{H,[20(1+9/100)]^{-1}\}$. Witness horizons are $O(\log(1/\delta)/(k\Lambda))$. Full protocol accuracy includes these pulses; a fixed minimum pulse duration does not include them uniformly over caps.

This gives a necessary cap of at least $\exp[c\log(1/\delta)/\log\log(1/\delta)]-2$ for a hypothetical scheme using only polynomially many reversible states uniformly over the family. That estimate alone remains compatible with polynomial-in-$1/\delta$ caps; the separate uncapped theorem now rules out polynomial reversible state cost. The cap-dependent note also proves an explicit fixed-clock criterion whose accuracy exponent deteriorates exponentially in the cap. It is a nineteen-level extension, not a new binary tradeoff theorem. The analytic derivation received a separate internal audit; finite-verifier status is recorded in the [ledger](CLAIM_LEDGER.md).

The [unbounded-rate boundary note](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) makes two further distinctions. First, replacing the binary construction's update matrix literally by a reversible semigroup or resolvent makes its palindromic words positive semidefinite, contradicting the negative lamp correlation required by that gadget. This excludes that replacement route only. Second, repairing entire nineteen-level flip words, while controlling extra measured Gram norms, removes rate and operator-norm assumptions from the algebraic scalar-to-entropy implication. Its largest raw physical generator degree is $162n+20$. The nineteen-level uncapped theorem uses bounded resolvent words instead of uniformly recovering those raw generator scalars. The new binary theorem uses mixed bounded words and a different target encoding; the [binary boundary note](BINARY_UNCAPPED_RESEARCH_BOUNDARY.md) explains why a literal replacement in the older gadget still fails and why general binary words are not all PSD. The algebraic lemma also supports the qualitative compactness consequence below.

The [uniform rate-regularization theorem](RATE_REGULARIZATION.md) provides a complementary approximation: replacing $K$ by $(e^{\Delta K}-I)/\Delta$ retains the same states, stationary law, actuator labels, histogram and original rule while achieving all-protocol, all-horizon mean error $\delta$ with internal exit and spectral cap $O_R(k\delta^{-1}\log(1/\delta))$. It need not retain the prescribed lower gap and does not compress states. Its accuracy-dependent cap is compatible with the tradeoff above; one cannot insert it into a fixed-cap theorem while retaining that theorem's constants. The exact report checks a small Poisson-capping fixture, while the analytic density/reset argument supplies the uniform guarantee.

The [finite-state fast-rate closure theorem](FINITE_STATE_FAST_RATE_CLOSURE.md) addresses a different question. For a fixed hidden-state budget $D_h$, all original-rule reversible response functions have compact closure in the same all-protocol, all-horizon metric. Fast-rate limits can have actuator mixtures on clusters, with at most $D_h$ constituent atoms, including limits of vanishing stationary masses. Exact agreement with a scalar-actuator target in either principal alphabet forces those mixtures to be pure, by an observable nonnegative variance identity.

For the nineteen-level target $n$, put $r=2^n$. Compactness, purity and the zero-defect whole-word entropy lemma then give a **strictly positive error floor at each fixed $n$ and $D_h<2^r$**, even with unbounded reversible rival rates. The same conclusion holds on the thirty-nine-field menu at any fixed positive clock, for the fixed $H>0$ throughout this dossier. In total-state notation the condition is $D-1<2^r$. The error floor's dependence on $n,D_h$ and the clock is not quantified: this is not an uncapped $\exp(c\delta^{-\alpha})$ state law. The broader polynomial rank lower already implies growing worst-case state requirements without a rate cap. This structural robustness corollary does not improve that growth class or separate reversible from unrestricted rivals: no matching smaller unrestricted realization at its unknown tolerance is established. No binary version of this qualitative entropy consequence is proved here. The compactness/purity proof is analytic; the finite report does not verify it.

The separate [Walsh observability theorem](UNCAPPED_WALSH_OBSERVABILITY.md) now gives stronger explicit fixed-target floors against all Markov rivals. With $r=2^n$, degree $1\le p\le r$ and $K_{n,p}=\sum_{j=0}^p\binom rj$, every rival of total size $D<9K_{n,p}+2$ has error at least $e^{-C_a(n+1)p}$ on the thirty-nine-field fixed-clock menu. Rivals need no reversibility, histogram, rate cap or original field rule. At full degree the threshold is $9\cdot2^r+2$; for $n=1$ an explicit reversible quotient attains the exact minimum of $38$ total states. This rank hierarchy is not a reversibility penalty and does not improve the known polynomial unrestricted minimax growth class.

## 5. Theorem dependency map

| Stage | Required result | Logical output |
|---|---|---|
| Capped kinetic observation | [Capped interface theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md) | Two generators recover exact positive selectors and transports; a common cap gives linear-in-$n$ clock witnesses and exponential ordinary state necessity. |
| Same-menu unrestricted necessity | [Capped theorem, target-only rank branch](CAPPED_KINETIC_INTERFACE_SEPARATION.md#6-a-polynomial-unrestricted-lower-on-the-same-two-fields) | Polynomial unrestricted necessity uses the same two fields, including when rival rates are uncapped. |
| Generalized-reversal upper | [Centered-word construction](GENERALIZED_REVERSAL_PREDICTION.md) | Word reversal and an even middle-symbol actuator retain polynomial prediction with exactly zero stationary generalized EPR. |
| Broader entropy bridge | [General interface bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) | Lower return and upper injection envelopes control all-horizon endpoint error without hidden rate or mass factors. |
| Current resource conclusion | [Kinetic/parity resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | Combines the broader capped state law and ordinary-EPR frontier while preserving the generalized-reversal distinction. |
| Fixed-clock scalar interface | [Gram observability](FIXED_CLOCK_GRAM_OBSERVABILITY.md) | Finite sampled means recover inserted/adjoint Gram tests and target-sensitive physical resolvent words with a finite clock horizon. |
| Positive selector calculus | [Positive label selectors](POSITIVE_LABEL_SELECTORS.md) | Two fields give positive rival kernels; target-only finite-grid discrimination needs no rival histogram. |
| Principal fixed-clock conclusion | [Tight-band theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) | Accuracy $e^{-C_{a,H}(n+1)^5}$ forces $2^{3\cdot2^n/4}$ states using $O_{a,H}((n+1)^5)$ ticks, with unchanged target band. |
| Entropy-production bridge | [Same-state reversibilization](ENTROPY_PRODUCTION_REVERSIBILIZATION.md) | Controlled-mean error is at most $R^{3/2}\sqrt{\sigma_0/k}$; rates and stationary masses are unrestricted. |
| Resource consequence | [State–entropy-production frontier](STATE_ENTROPY_PRODUCTION_TRADEOFF.md) | Transfers state lower bounds with their own competitor assumptions; provides a finite-EPR polynomial upper. |
| Historical binary clock route | [Binary Schur/heat calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md); [binary theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) | Retains the separately scaled tagged target, balanced histogram and twelfth-power budget. |
| Binary uncapped observation interface | [Mixed killed-word observability](MIXED_KILLED_WORD_OBSERVABILITY.md) | Transfers binary smoothed-label, killed and heat words from actual means without a rival cap, with a quadratic logarithmic accuracy budget in the application. |
| Binary target encoding | [Rare binary tags and distant ballast](BINARY_TAGGED_UNCAPPED_CONSTRUCTION.md) | Supplies positive approximate signed-port selectors; exact balance and every counted state retain a uniform gap and fixed, very large rate-to-gap ratio. |
| Binary uncapped state bridge | [Weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md) | Handles approximate selectors and a shrinking target root mass, adding no states and requiring no global rival operator-norm bound. |
| Binary uncapped conclusion | [Full binary theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) | Combines $e^{-C(n+1)^2}$ scalar accuracy with entropy; separates the tagged-family polynomial upper from the explicit union's polynomial growth class. |
| Uncapped bounded-word interface | [Bounded-control resolvent observability](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) | Convexification, one-scalar continuation, dwell averaging and coefficient extraction control bounded label words without a rival rate cap; full arbitrary switching is used. |
| Uncapped reversible lower | [Positive cross-port resolvents and entropy](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) | Target approximation plus scalar extraction at $e^{-O(n^2)}$ accuracy gives superpolynomial reversible necessity against polynomial stationary prediction. |
| Physical interface | [Theory](THEORY.md); scalar endpoints in [binary Sections 3–4](BINARY_REVERSIBILITY_LOWER_BOUND.md) and [nineteen-level Sections 3–4](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) | Expresses positive word tests as polynomials in physical generators using the prescribed preparation/readout. |
| Quantitative observation | [Reversible word observability](REVERSIBLE_WORD_OBSERVABILITY.md) | Capped reversible propagator accuracy controls the required generator-word scalars at each fixed clock. |
| Positive state-space bridge | [Transport repair](POSITIVE_TRANSPORT_REPAIR.md); [binary Sections 5–6](BINARY_REVERSIBILITY_LOWER_BOUND.md) | Repairs stationary flux on existing rival states; binary positive weighting handles a selector that need not be a projection. |
| Uncapped algebraic boundary | [Whole-word repair and additional Gram norms](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) | Removes the nineteen-level algebraic repair cap, conditional on the specified scalar data; supplies no uncapped actual-mean-to-scalar transfer. |
| Qualitative uncapped consequence | [Finite-state closure and exact actuator purity](FINITE_STATE_FAST_RATE_CLOSURE.md), together with the zero-defect whole-word lemma | Gives a positive nineteen-level error floor for each fixed $n,D_h<2^{2^n}$, including fixed clocks, without a quantitative inverse-error law. |
| Reversible lower | [Binary Section 7](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level Sections 6–8](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) | Query/flip relations produce a deterministic high-entropy lamp law and exponential physical-state necessity. |
| Unrestricted lower | [Whole-side fixed-clock rank transfer](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md), used in the principal proofs | Target-only truncation produces a finite observation matrix factoring through any rival's $D$ states; polynomial necessity needs no rival rate cap or field-rule constraint. |
| Fixed-target rank hierarchy | [Walsh observability](UNCAPPED_WALSH_OBSERVABILITY.md) | All subset characters give an explicit degree hierarchy, positive floors for broad rivals, and the exact $38$-state minimum at $n=1$. |
| Nonreversible upper | [Bounded-rate Sections 2–5](BOUNDED_RATE_FINITE_FIELD.md) | Uniformization, stationary word matching and regeneration give one polynomial-size predictor for all horizons. |
| Reversible upper | [Bounded-rate Section 7](BOUNDED_RATE_FINITE_FIELD.md) | A prediction partition retains detailed balance, the histogram and target band, giving the singly exponential sufficient count. |
| Same-budget conclusion | [Binary Sections 8–9](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level Section 9](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) | Both comparisons concern the same target family and internal exit resource. |

The unrestricted rank lower and ordinary-reversible entropy lower are separate branches. The new target-only rank argument supplies polynomial unrestricted growth on the same nineteen-level family and two-field menu for both capped and uncapped rivals. The earlier thirty-nine-field corollary remains valid under its historical scope. The binary uncapped theorem still uses the older rank result only for its explicitly enlarged-family corollary. The aggregation norm-loss proof and exact-prefix peripheral-spectrum proof are supporting results, not prerequisites for the current kinetic-interface comparison.

## 6. Baselines that must not be conflated

| Comparison | Established state behavior | Scope difference from the principal theorem |
|---|---|---|
| Passive visible process | Exactly two states | Complete zero-field path law; no active prediction. |
| All constant steps in bounded binary class | $\Theta(\log(1/\delta))$ | One common analytic reversible predictor may change the original field rule; no switching guarantee. |
| Switching in bounded binary class $[k,3k]$ | $\delta^{-\Theta(1)}$ with unrestricted predictors | Its general reversible upper is larger; binary intrinsic separation in this tight band is open. |
| One-dimensional local paths plus refresh | Polynomial necessary and reversible sufficient switching size | Original field rule and band retained; small-cost fragmentation is extra structure. The same class has logarithmic step cost. |
| Typical fixed labels on high-girth expanders | Polynomial necessary and reversible sufficient size | One high-probability label event works at every accuracy; not every fixed labeling. |
| Six-level stationary-flux / Bayes aggregation | Exponential architecture cost versus polynomial fresh reversible realization | Encoder/flux restrictions are essential; no intrinsic reversibility penalty is inferred from this result. |
| Rank-one actuator geometry | $\Theta(\log^2(1/\delta))$, or logarithmic with capped active rates | Exact scalar-kernel closure is special; a shared cubic kernel is not generally complete finite-field information. |
| Cubic coefficient prediction | Sharp logarithmic-squared / logarithmic orders | Analytic coefficient task with its own norm and competitor class; not actual finite-field error. |
| Fifteen-symbol exact reversible prefix | Arbitrarily large exact realization dimension | Zero-error deterministic-color law; no positive-error physical-mean conclusion. |

Proofs, evidence and source comparisons for each row are indexed in the [claim ledger](CLAIM_LEDGER.md).

## 7. Reproducibility and evidence protocol

1. Record the checked commit, Python version and pinned [dependencies](../requirements.txt). The baseline reports use Python 3.13.5; dependency versions are recorded in the repository, not inferred from the current machine.
2. From the repository root install the pinned requirements in a suitable environment and run `make check`. [Makefile](../Makefile) runs repository checks and mathematical verifiers; fresh reports go to `.check-output/`.
3. Inspect the changed theorem's verifier and generated report together. Exact small fixtures validate identities and counterexamples; analytic proofs carry all-width, all-model and asymptotic claims.
4. Compare fresh and saved reports in the recorded environment. If a verifier changes, regenerate its saved report through the documented command, retain source-hash provenance, and explain the changed claim. Never hand-edit saved metrics or silently overwrite protected checkpoint evidence.
5. Record local checks separately from live CI. A local PASS, a committed report and a completed remote workflow are different facts. Record independent mathematical review separately from all three.

The baseline binary verifier constructs 1,795 hidden vertices sparsely, with 1,796 total physical states; its small dense fixtures have dimension at most five. The baseline full suite has maximum dense dimension 68. The nineteen-level verifier constructs the 146-state width-one model sparsely. The [binary uncapped verifier](../scripts/verify_binary_uncapped_observability.py) and [report](../reports/binary_uncapped_observability.json) supply exact small PSD-boundary, mixed-coefficient, normalized-selector, weighted-repair and parameter-budget fixtures. They do not construct the full rare-tag target or prove its all-width estimates by enumeration. The [fixed-clock verifier](../scripts/verify_fixed_clock_observability.py) and [saved report](../reports/fixed_clock_observability.json) check sampled-row recovery, adjoints, Schur and binary resolvent identities, contraction remainders and the polynomial budget. Their finite fixtures do not prove the universal analytic estimates.

The historical `e38dde1` checkpoint has thirty-four verifiers, including the [PRL verifier](../scripts/verify_prl_exploration.py) and [report](../reports/prl_exploration.json) with 561 bounded selector/EPR/budget checks. The preceding [thirty-fifth verifier](../scripts/verify_kinetic_parity.py) and [report](../reports/kinetic_parity.json) contain 166 bounded checks at dense dimension at most nine, with hashes of all five new proof notes. They check a small generalized-reversal word chain, its physical response equivalence, kinetic selectors and the general reset constants. The parity fixture is not itself a certified small state-count advantage. The new [finite-advantage verifier](../scripts/verify_finite_advantage.py) checks the actual twelve/eleven-state models and exact Gram/tolerance arithmetic at dense dimension at most twelve. The [physical-robustness verifier](../scripts/verify_physical_robustness.py) checks separate small force, perturbation and closure fixtures. The analytic proof notes have passed internal reviews; finite checks supplement those proofs. Full-suite, saved-report provenance and remote-CI status belong to [Verification](VERIFICATION.md), separately from mathematical review.

## 8. Novelty audit, review requirements and unresolved boundaries

The [source audit](PRIOR_ART.md) records located primary statements, versions and access depth. It already attributes kinetic nonlinear response, Hankel/word rank, positive realization, stationary finite-order approximation, quadrature, Jacobi realization, lamp/Følner growth, conditional entropy, binary input coding, Doob transforms and marginal repair. The [rate-boundary follow-up](RATE_BOUNDARY_PRIOR_ART.md) adds spectral and singular-limit comparisons and distinguishes ordinary detailed balance from alternative meanings of reversible representation. The [bounded-word follow-up](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) compares analytic continuation, coefficient recovery and realization inputs for the nineteen-level uncapped theorem. The [binary follow-up](BINARY_OBSERVATION_PRIOR_ART.md) compares binary positive observation words, killing/conditioning and the new combined construction. The [fixed-clock follow-up](FIXED_CLOCK_PRIOR_ART.md) compares reversible embedding, matrix functions and observable-operator identification with the new scalar Gram/resolvent interface. Fast-block averaging, Walsh characters and rank reasoning are not claimed as new general mechanisms. The candidate claim is the constrained quantitative connection in the full theorem. This dossier indexes those audits without expanding their coverage claims.

The [PRL source audit](PRL_EXPLORATION_SOURCE_AUDIT.md) adds targeted comparisons on equilibrium compression and prediction/dissipation. The [kinetic/parity source audit](KINETIC_PARITY_SOURCE_AUDIT.md) adds the generalized-reversal and kinetic-interface comparisons. A complete-theorem comparison of the five new results and their physical interpretation against the closest reversible/positive and controlled stochastic realization results would strengthen the evidence before publication-priority claims. Current internal proof reviews and bounded source searches do not supply an external proof audit or priority certification. These are recommended follow-up tasks, not additional user-imposed prerequisites for equipping the repository or beginning a later draft; further numerical examples cannot substitute for that kind of review.

| Open boundary | Current status | What would resolve it |
|---|---|---|
| Stronger uncapped $\exp(c\delta^{-\alpha})$ law | Open; binary and nineteen-level superpolynomial uncapped lowers are proved | Improve the accuracy-to-word transfer or another part of the estimate. Arbitrary switching gives inner exponent $1/2$; the new fixed-clock result gives $1/5$. |
| Binary uncapped intrinsic penalty | Resolved in existence by the [tagged-family theorem](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) | The older budget-$6580$ family remains a separate open strengthening; literal substitution in its gadget is still obstructed. |
| Fixed-clock uncapped superpolynomial penalty | **Resolved on the original nineteen-level band $[k,3k]$ targets**, without rival histogram restrictions | The [new two-field theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) gives inner exponent $1/5$ and finite witnesses. The historical binary theorem retains exponent $1/12$ on its scaled tagged family. |
| Quantify a varying cap | [Uniform nineteen-level tradeoff proved](STATE_SPEED_ACCURACY_TRADEOFF.md), with a separate internal audit | Retain cap-dependent clock requirements and the weaker fixed-clock formula; the uncapped superpolynomial result has a different proof and clock scope. |
| Binary band $[k,3k]$ / smaller budget | Open | A lower-budget binary construction or a structural obstruction. |
| Arbitrary reversible field dependence | **Partly resolved:** bounded kinetic barriers with fixed equilibrium block tilt and $b_i(0)=1$ permit the capped exponential separation | Arbitrary field-dependent hidden dynamics, other block tilts or hub-free interfaces need separate arguments. |
| Match exponents or optimize constants | Open | Sharper lower/upper estimates; $6580$ belongs to the older binary construction, and the tagged construction has a much larger fixed rate-to-gap ratio. |
| Rival histogram and field-rule freedom | **Resolved within the bounded kinetic-interface class** for capped and uncapped lowers, with the same two fields | Unbounded endpoint barriers and arbitrary target interfaces remain outside the proof. |
| State–fidelity–entropy-production frontier | New capped frontier omits histogram matching and the exponential barrier rule; uncapped frontier also proved | Match the ordinary-EPR bounds; generalized stationary EPR can already be exactly zero with polynomial prediction. No universal dissipation conclusion follows. |
| Physical reversal convention | Explicit generalized-reversible polynomial upper proved | Identify a natural implementation whose physical parity realizes the involution, or restrict retained configurations to physically even variables. |
| Modest certified finite witness | Open | Certify a concrete state-count advantage at useful finite tolerance; the current small algebraic fixtures establish neither that advantage nor experimental efficiency. |
| Arbitrary expander labeling | Open | A uniform compression theorem beyond the stated good-label event. |
| Inference, sample cost, practical construction | Outside the proved state-resource results | A separately defined data/noise/computation task. |

Keep continuation results in the ledger with their proved, conditional or open status. In particular, failure of a logarithm-transfer estimate at unbounded rates is a proof limitation, not a cap-free theorem or a counterexample. Manuscript drafting remains the final step in the user's requested order; this preparation task does not start it.

## 9. Equation, figure and bibliography inventory

The mathematical source material is present. The current repository has no standalone figure assets or machine-readable bibliography; existing comparison tables, equations and exact reports provide their source data. Do not turn asymptotic bounds with unmatched exponents into numerically calibrated curves.

| Later asset | Exact reusable content | Source and remaining production step |
|---|---|---|
| Model and task equation set | Original rates, equilibrium, $\mathcal D_H$ and worst-case state count | Sections 2–3 above and [Theory](THEORY.md); unify notation when the theorem selection is fixed. |
| Fixed-clock principal equation set | Same two-field task: capped polynomial unrestricted/generalized growth versus exponential ordinary growth; uncapped polynomial growth and fifth-root ordinary lower | [Capped kinetic theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md), [uncapped kinetic theorem](GENERAL_KINETIC_INTERFACE.md), [generalized upper](GENERALIZED_REVERSAL_PREDICTION.md). Keep the common cap and reversal convention beside each bound. |
| Entropy-production equation set | General interface mean bound, broad/capped ordinary-EPR frontiers, finite-EPR upper and zero generalized EPR | [General interface bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) and [kinetic/parity resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md). Keep full-zero versus hidden normalization and interface envelopes explicit. |
| Historical binary uncapped equation set | Tagged-family polynomial upper versus superpolynomial reversible lower; explicit union corollary; $e^{-C(n+1)^2}$ accuracy allocation | [Binary uncapped theorem equations (4), (17)–(23)](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md). Keep rare weights, the large fixed target rate-to-gap ratio and arbitrary-switching limitation beside the bound. |
| Historical arbitrary-switching tight-band comparison | Nineteen-level polynomial unrestricted growth versus superpolynomial reversible lower | [Nineteen-level uncapped theorem](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md); [bounded-control observability](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md). It retains the band $[k,3k]$. |
| Historical fixed-budget equation set | Binary common-budget inequalities and nineteen-level variant | [Binary equations (1)–(5)](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level equations (1)–(2)](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md). Preserve explicit constants, growth-class qualification and rival conditions. |
| Proof mechanism equation set | Physical scalar transfer, stationary repair, deterministic decoding and entropy support bound | [Binary Sections 4–7](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level Sections 3–7](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md); [whole-word boundary lemma](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md). Choose one proof route rather than merging hypotheses from different routes. |
| Quantitative extension equation set | Uniform cap-dependent lower, concrete target threshold, weaker fixed-clock formula | [State–speed–accuracy equations (3)–(6), (22), (26)–(30)](STATE_SPEED_ACCURACY_TRADEOFF.md). The clock belongs beside the bound. |
| Qualitative boundary equation set | Mixture-cluster rates, exact purity identity and positive error floor | [Finite-state closure equations (1)–(2), (8)–(12)](FINITE_STATE_FAST_RATE_CLOSURE.md). Label the hidden-state budget and leave the unquantified error floor explicit. |
| Physical construction schematic | Original nineteen-level ports, hub and logical table; positive filters are proof operations | Original construction and new selector note. Keep total state count visible; historical binary tags need not lead the presentation. |
| Main comparison table | Shared two-field task, kinetic freedom, cap and reversal convention; polynomial versus exponential growth classes | Section 4 above and ledger R22–R26. Retain R18–R21, R15–R17 and P1–P5 under their historical scopes. |
| Baseline comparison table | Passive / step / switching and aggregation / fresh realization | Section 6 above and ledger S3–S8. Keep target family and field-rule differences in the table. |
| Proof dependency diagram | Physical means to word scalars to stationary couplings to entropy; separate rank/upper branches | Section 5 above. Existing table is sufficient; a later diagram would be presentation only. |

The [main audit](PRIOR_ART.md), [rate-boundary audit](RATE_BOUNDARY_PRIOR_ART.md), [bounded-word audit](BOUNDED_WORD_RECOVERY_PRIOR_ART.md), [binary audit](BINARY_OBSERVATION_PRIOR_ART.md), [fixed-clock audit](FIXED_CLOCK_PRIOR_ART.md), [PRL audit](PRL_EXPLORATION_SOURCE_AUDIT.md), and [kinetic/parity audit](KINETIC_PARITY_SOURCE_AUDIT.md) contain author/title/year records, primary links, relevant theorem locations and access limits for the central ingredients. They are sufficient to begin a selected-reference bibliography. After the eventual scope is fixed, consolidate only the cited records into a bibliography and verify exact publication metadata against the linked primary records; preserve unresolved access limits instead of filling them from memory. No new exhaustive-search claim follows from that formatting step.

The research focus and provisional PRL target are recorded in [PRL exploration](PRL_EXPLORATION.md). Remaining nonmathematical inputs include author/affiliation/contribution metadata and eventual formatting requirements. They do not prevent this research package from being complete for its present purpose. Figure production, final bibliography formatting and manuscript prose are deferred to the drafting stage; no new simulation is needed to support the existing theory claims.
