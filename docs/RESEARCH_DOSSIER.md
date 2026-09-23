# Research dossier for eventual manuscript preparation

[Claim ledger](CLAIM_LEDGER.md) · [Publication scope](PUBLICATION_SCOPE.md) · [Source audit](PRIOR_ART.md) · [Verification](VERIFICATION.md) · [Current work](../work_orders/CURRENT.md)

**Planning record, 23 September 2026.** This document organizes the research needed before drafting. It contains no manuscript draft or journal recommendation. The established baseline is commit `e21c454ec1a0eef8ceba8bd7e3d01defc62b53a5`, with twenty-nine mathematical verifiers. Proofs, generated checks and source comparisons have different evidentiary roles; the [ledger](CLAIM_LEDGER.md) keeps them separate. Subsequent work must retain its own status and provenance.

## 1. Recommended scientific focus and result hierarchy

The principal candidate is now the [nineteen-level uncapped reversibility theorem](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md): ordinary reversibility forces superpolynomial state cost although stationary predictors without that requirement have polynomial cost on the same target family. Both classes keep the original kinetic rule, exact histogram, preparation and readout; neither has a rival rate cap. Rivals may construct new states. The reversible lower is $\exp(\exp(c\sqrt{\log(1/\delta)}))$, while the available upper remains singly exponential in a positive power of inverse error. These rates are not matched.

The complementary [balanced binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) proves a stronger growth-class separation under a common fixed exit budget: polynomial versus singly exponential in a positive power of inverse error. The [fixed-budget nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) retains the smaller $3k$ budget and target band $[k,3k]$. Keep both distinctions visible: removing the rival cap is established for nineteen levels with arbitrary switching; the stronger fixed-cap law also holds for a balanced binary actuator and every fixed clock.

The eventual central theorem should state the shared constraints before the growth comparison. Its uncapped proof continues whole physical protocols in a bounded external coefficient family, extracts bounded positive resolvent words, repairs whole transports on the rival's states, and decodes lamps deterministically. The binary fixed-cap proof uses its separate positive-selector normalization. The source audits treat the constrained quantitative connection as the candidate contribution; the realization, analytic continuation, interpolation, transport and entropy ingredients have antecedents.

The remaining results should have explicit roles:

| Role | Results to retain | Reason for inclusion |
|---|---|---|
| Principal comparison | Uncapped nineteen-level penalty; binary fixed-budget stronger law | Separates ordinary reversibility from the freedom to invent states; makes both rate and clock assumptions explicit. |
| Essential upper and lower machinery | Bounded-control resolvent observability; whole-word repair; stationary word-chain upper; reversible prediction partition; target-only rank lower | Connects physical means to an uncapped reversible obstruction and supplies the polynomial comparison; only the fixed-budget laws have matching growth classes. |
| Complementary task comparison | Passive / all constant steps / switching; local-path version | Shows that the experiment menu itself changes state cost; the step upper has a different field-rule scope. |
| Structural controls | Fresh reversible versus aggregation; density, local-fragmentation and expander compression | Shows precisely where reversible prediction remains polynomial or a restricted architecture is costly. |
| Foundations and diagnostics | Cubic response, rank-one finite-field closure, actuator-process equivalence, path response, near-lumpability | Explains the model and operational limits; these are separate tasks and need not all become main-text theorems. |
| Rate and fixed-target supporting results | State–speed–accuracy; regularization; finite-state closure; Walsh hierarchy | Explains cap dependence and fast-rate limits; Walsh rank gives explicit fixed-target floors against all Markov rivals and an exact small-target minimum. |

This is an organizational choice, not a novelty or publication-level assessment. A concise eventual paper can center the uncapped nineteen-level comparison together with the balanced binary fixed-budget result, and place the remaining results in supporting material or separate work. Independent review remains a recommended evidence task.

## 2. Common model and notation

Use the row-generator convention throughout. A target has a visible state $A$ and a finite hidden set $\mathcal B$, with positive stationary probability $\mu$ and internal generator $K$. The readout is $S(A)=-1$, $S(z)=+1$ on $\mathcal B$. For $k>0$ and a dimensionless scalar field $h$,

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},\qquad
q_{zz'}(h)=K_{zz'}\quad(z\ne z').
$$

Diagonals make row sums zero; column probabilities satisfy $\dot p=Q(h)^Tp$. The target has $\mu K=0$, $\mu_zK_{zz'}=\mu_{z'}K_{z'z}$, and centered $\sum_z\mu_zg_z=0$. Preparation is $\pi_0=(1/2,\mu/2)$. Its fixed-field equilibrium is

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
| $n,r$ | Register width and number of lamp addresses, $r=2^n$. |
| $\delta$ | Uniform error in the actual controlled mean. |
| $\varepsilon,u,m_j$ | In response calculations, $h=\varepsilon u$ and $m_j$ is the coefficient of $\varepsilon^j$, including the factorial convention; coefficient error is a separate tolerance. |
| $C(t)$ | Cubic kinetic kernel $\langle g,e^{Kt}g\rangle_\mu$; complete finite-field information only in the stated rank-one subclass. |
| $\alpha,\zeta,p,c,C$ | Positive growth exponents and constants local to each theorem. Reusing a Greek letter does not identify exponents across notes. |

Ordinary reversibility means detailed balance with a positive stationary law, without an extra reversal involution. For an original-rule predictor it is equivalent to imposing hidden detailed balance: the external edges already have the displayed equilibrium flux relation. A stationary nonreversible hidden model has the same fixed-field stationary distribution but need not satisfy detailed balance.

## 3. Error, quantifiers and counted resources

For a target $F$ and one predictor $\widehat F$, define

$$
\mathcal D_H(F,\widehat F)=
\sup_{T>0}\ \sup_{\substack{h:[0,T]\to[-H,H]\\h\text{ deterministic, piecewise continuous}}}
\ \sup_{0\le t\le T}
\left|m_F[h](t)-m_{\widehat F}[h](t)\right|.
$$

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

All hidden configurations, registers, signs, ports, corridor vertices, hubs, ballast and any retained memory states count. For example, the binary target has $224r2^r+4$ total states; the nineteen-level target has $18r2^r+2$. The large target itself is never treated as a free oracle inside the reduced model. State count does not charge parameter precision, the description complexity of rate functions, construction time, integration time or experimental samples. Constructions receive the target model; this is compression after specification, not identification from passive data.

The shorthand $\delta^{-\Theta(1)}$ means upper and lower bounds with fixed positive, potentially different exponents. Likewise $\exp(\delta^{-\Theta(1)})$ denotes a growth class; the explicit reversible upper is $\exp[C\delta^{-p}\log(2/\delta)]$. It does not assert a matched exponent or an exact power law.

## 4. Principal theorem boundaries and physical assumptions

For the uncapped nineteen-level comparison, the target band remains $[k,3k]$, the histogram is the same as in the fixed-budget table below, and rivals retain the original rule, preparation and readout. There is no rival rate cap or lower-gap requirement. For sufficiently small $\delta$,

$$
c_0\delta^{-\zeta}\le D_{\rm all}^{\rm unc}(\delta)\le C_0\delta^{-p},\qquad
\exp\!\left(\exp\!\left(c_1\sqrt{\log(1/\delta)}\right)\right)
\le D_{\rm rev}^{\rm unc}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log(2/\delta)\right).
$$

The lower uses the existing thirty-nine field amplitudes with arbitrary positive durations and arbitrarily fast switching. It does not establish a superpolynomial lower at each fixed positive control clock. The following table concerns the stronger fixed-budget comparisons, whose clock guarantees remain separate.

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
| Specified exponential field rule | Fixes how the field changes kinetic barriers; finite field samples recover a shared generator decomposition. | Local detailed balance alone does not specify this rule. Arbitrary reversible field functions form a broader, unresolved competitor class for the exponential lower. |
| Exact actuator histogram | Holds one-time actuator statistics and external equilibrium coupling fixed; supports the shared scalar identities. | No theorem here establishes tolerance to arbitrary histogram mismatch. |
| Stationary preparation and fixed binary readout | Defines the actual laboratory-style mean interface used to recover word scalars. | Extra preparations, extra readouts or feedback are not supplied. |
| Exit budget / spectral cap, when imposed | Stabilizes the fixed-clock generator recovery. The binary proof also needs $P=I+K/(6580k)$ entrywise nonnegative to preserve positive words. | The nineteen-level uncapped proof replaces raw generators by bounded resolvent words; it gives a weaker lower and uses arbitrarily fast switching. |
| Ordinary reversibility | Supplies adjoint word relations and stationary reverse transports. | The entropy lower does not follow from a rank lower alone. |
| Uniform target gap | Shows that hidden slow mixing is not needed for the obstruction. | A gap is not imposed on the lower-bound rival class. |
| Fixed finite alphabet and field bound | Keeps interpolation and word-compression constants independent of target size. | Changing these with accuracy changes the resource problem. |

For reversible $K$, a relaxation cap $\Lambda k$ bounds every exit by $\Lambda k$; an exit cap $Bk$ bounds the real relaxation spectrum by $2Bk$. These implications are not equalities. In the binary upper the sharper exit budget follows directly from the known stochastic uniformization and from stationary-flux aggregation, despite the larger spectral band. The nineteen-level entropy lower permits any fixed rival cap $\Lambda k$; taking $\Lambda=6$ includes every reversible rival with exits at most $3k$. No cap-to-exit inference of the same form is asserted for general nonreversible spectra.

The energy/barrier realization in [Theory, Section 2](THEORY.md#2-detailed-balance-and-physical-interpretation) establishes consistency with a kinetic coupling, not a demonstrated molecular mechanism. Global refresh, hubs and complete lamp tables are explicit counted constructions. Fixed-clock lower bounds still use signed combinations of actual mean experiments with potentially large coefficients; they imply no measurement-noise or sample-efficiency guarantee.

### Bounded resolvent observability without a rate cap

The [bounded-control observability lemma](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md) uses the affine span of the finite physical field menu. Modelwise rapid switching passes actual-mean accuracy to convexified protocols. One analytic parameter deforms the entire protocol, and a priori holomorphic bounds depend only on the bounded external operator, giving a fixed square-root error exponent independent of word length and hidden rates. Artificial absorbing or negative-killing coefficients are proof expressions, not added experimental controls.

Independent exponential dwell averages expose $P_s=s(sI-K)^{-1}$. Polarization and finite Chebyshev interpolation recover bounded label words of $P_s^2$ with explicit coefficient mass and tail bounds. Target cross-port resolvents approximate the exact gates; the [uncapped lower](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) controls all required scalar moments at accuracy $\delta_n=e^{-C(n+1)^2}$, then applies whole-word repair and entropy to force $2^{3\cdot2^n/4}$ rival states. Raw generator moments need not be close. No uniform bound on the Trotter switching frequency is claimed.

### Rate-dependent and qualitative supporting results

The [state–speed–accuracy theorem](STATE_SPEED_ACCURACY_TRADEOFF.md) makes the nineteen-level proof uniform over a variable reversible spectral cap $\Lambda k$, $\Lambda\ge3$. For constants $c_H,C_0>0$ independent of accuracy and cap, its worst-case state requirement satisfies

$$
\log\log\mathcal D_{\rm rev}(\delta,\Lambda)
\ge c_H\frac{\log(1/\delta)}{\log(\Lambda+2)}-C_0,
\qquad 0<\delta<1.
$$

Its explicit finite-width criterion is $\delta\le[C_H(\Lambda+2)]^{-C_*(n+1)}$, which forces at least $2^{3\cdot2^n/4}$ states on target $n$. The shared thirty-nine-field menu uses a cap-dependent clock $a_\Lambda/k=1/[2k(\Lambda+R)]$, where $R=e^{(1+9/100)h_0}$ and $h_0=\min\{H,[20(1+9/100)]^{-1}\}$. Witness horizons are $O(\log(1/\delta)/(k\Lambda))$. Full protocol accuracy includes these pulses; a fixed minimum pulse duration does not include them uniformly over caps.

This gives a necessary cap of at least $\exp[c\log(1/\delta)/\log\log(1/\delta)]-2$ for a hypothetical scheme using only polynomially many reversible states uniformly over the family. That estimate alone remains compatible with polynomial-in-$1/\delta$ caps; the separate uncapped theorem now rules out polynomial reversible state cost. The cap-dependent note also proves an explicit fixed-clock criterion whose accuracy exponent deteriorates exponentially in the cap. It is a nineteen-level extension, not a new binary tradeoff theorem. The analytic derivation received a separate internal audit; finite-verifier status is recorded in the [ledger](CLAIM_LEDGER.md).

The [unbounded-rate boundary note](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md) makes two further distinctions. First, replacing the binary construction's update matrix literally by a reversible semigroup or resolvent makes its palindromic words positive semidefinite, contradicting the negative lamp correlation required by that gadget. This excludes that replacement route only. Second, repairing entire nineteen-level flip words, while controlling extra measured Gram norms, removes rate and operator-norm assumptions from the algebraic scalar-to-entropy implication. Its largest raw physical generator degree is $162n+20$. The new uncapped theorem uses the bounded-resolvent route instead of attempting uniform recovery of those raw generator scalars. The algebraic lemma also supports the qualitative compactness consequence below.

The [uniform rate-regularization theorem](RATE_REGULARIZATION.md) provides a complementary approximation: replacing $K$ by $(e^{\Delta K}-I)/\Delta$ retains the same states, stationary law, actuator labels, histogram and original rule while achieving all-protocol, all-horizon mean error $\delta$ with internal exit and spectral cap $O_R(k\delta^{-1}\log(1/\delta))$. It need not retain the prescribed lower gap and does not compress states. Its accuracy-dependent cap is compatible with the tradeoff above; one cannot insert it into a fixed-cap theorem while retaining that theorem's constants. The exact report checks a small Poisson-capping fixture, while the analytic density/reset argument supplies the uniform guarantee.

The [finite-state fast-rate closure theorem](FINITE_STATE_FAST_RATE_CLOSURE.md) addresses a different question. For a fixed hidden-state budget $D_h$, all original-rule reversible response functions have compact closure in the same all-protocol, all-horizon metric. Fast-rate limits can have actuator mixtures on clusters, with at most $D_h$ constituent atoms, including limits of vanishing stationary masses. Exact agreement with a scalar-actuator target in either principal alphabet forces those mixtures to be pure, by an observable nonnegative variance identity.

For the nineteen-level target $n$, put $r=2^n$. Compactness, purity and the zero-defect whole-word entropy lemma then give a **strictly positive error floor at each fixed $n$ and $D_h<2^r$**, even with unbounded reversible rival rates. The same conclusion holds on the thirty-nine-field menu at any fixed positive clock, for the fixed $H>0$ throughout this dossier. In total-state notation the condition is $D-1<2^r$. The error floor's dependence on $n,D_h$ and the clock is not quantified: this is not an uncapped $\exp(c\delta^{-\alpha})$ state law. The broader polynomial rank lower already implies growing worst-case state requirements without a rate cap. This structural robustness corollary does not improve that growth class or separate reversible from unrestricted rivals: no matching smaller unrestricted realization at its unknown tolerance is established. No binary version of this qualitative entropy consequence is proved here. The compactness/purity proof is analytic; the finite report does not verify it.

The separate [Walsh observability theorem](UNCAPPED_WALSH_OBSERVABILITY.md) now gives stronger explicit fixed-target floors against all Markov rivals. With $r=2^n$, degree $1\le p\le r$ and $K_{n,p}=\sum_{j=0}^p\binom rj$, every rival of total size $D<9K_{n,p}+2$ has error at least $e^{-C_a(n+1)p}$ on the thirty-nine-field fixed-clock menu. Rivals need no reversibility, histogram, rate cap or original field rule. At full degree the threshold is $9\cdot2^r+2$; for $n=1$ an explicit reversible quotient attains the exact minimum of $38$ total states. This rank hierarchy is not a reversibility penalty and does not improve the known polynomial unrestricted minimax growth class.

## 5. Theorem dependency map

| Stage | Required result | Logical output |
|---|---|---|
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

The unrestricted rank lower and reversible entropy lower are separate branches. The former does not make the latter cap-free. The aggregation norm-loss proof and exact-prefix peripheral-spectrum proof are supporting results, not prerequisites for the intrinsic binary lower.

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

The baseline binary verifier constructs 1,795 hidden vertices sparsely, with 1,796 total physical states; its new dense algebraic fixtures have dimension at most five. The baseline full suite has maximum dense dimension 68. The nineteen-level verifier constructs the 146-state width-one model sparsely. These are bounded certificates, not enumeration of arbitrary rivals or large simulation evidence. See [Verification](VERIFICATION.md) for the complete provenance and checkpoint-specific limitations.

## 8. Novelty audit, review requirements and unresolved boundaries

The [source audit](PRIOR_ART.md) records located primary statements, versions and access depth. It already attributes kinetic nonlinear response, Hankel/word rank, positive realization, stationary finite-order approximation, quadrature, Jacobi realization, lamp/Følner growth, conditional entropy, binary input coding, Doob transforms and marginal repair. The [rate-boundary follow-up](RATE_BOUNDARY_PRIOR_ART.md) adds spectral and singular-limit comparisons and distinguishes ordinary detailed balance from alternative meanings of reversible representation. The [bounded-word follow-up](BOUNDED_WORD_RECOVERY_PRIOR_ART.md) compares analytic continuation, coefficient recovery and realization inputs for the uncapped theorem. Fast-block averaging, Walsh characters and rank reasoning are not claimed as new general mechanisms. The candidate claim is the constrained quantitative connection in the full theorem. This dossier indexes those audits without expanding their coverage claims.

A theorem-level comparison of the complete uncapped nineteen-level and binary fixed-budget statements with the closest reversible/positive realization and controlled stochastic realization results, plus an independent reading of the whole-protocol continuation, positive-word normalization, repair and clock arguments, would strengthen the evidence before making publication-priority or independently validated proof claims. Current internal proof reviews and bounded source searches do not supply an external proof audit or priority certification. These are recommended follow-up tasks, not additional user-imposed prerequisites for equipping the repository or beginning a later draft; further numerical examples cannot substitute for that kind of review.

| Open boundary | Current status | What would resolve it |
|---|---|---|
| Stronger uncapped $\exp(c\delta^{-\alpha})$ law | Open; the nineteen-level [superpolynomial uncapped lower](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) is proved | Improve the accuracy-to-word transfer or another part of the estimate. The current lower is $\exp(\exp(c\sqrt{\log(1/\delta)}))$. |
| Binary uncapped intrinsic penalty | Open | A new positive binary construction or extraction argument; the existing literal resolvent substitution is obstructed. |
| Fixed-clock uncapped superpolynomial penalty | Open | Replace the arbitrary-fast-switching convexification step with a proof respecting one positive minimum dwell time. Fixed-clock polynomial rank lowers already hold. |
| Quantify a varying cap | [Uniform nineteen-level tradeoff proved](STATE_SPEED_ACCURACY_TRADEOFF.md), with a separate internal audit | Retain cap-dependent clock requirements and the weaker fixed-clock formula; the uncapped superpolynomial result has a different proof and clock scope. |
| Binary band $[k,3k]$ / smaller budget | Open | A lower-budget binary construction or a structural obstruction. |
| Arbitrary reversible field dependence | Open for the exponential separation | Control of a broader generator family; original-rule interpolation is unavailable without replacement. |
| Match exponents or optimize constants | Open | Sharper lower/upper estimates; $6580$ is a sufficient construction constant. |
| Stability to histogram or rate-rule misspecification | Not established by the exact-constraint theorems | A separate robust comparison with explicit perturbation tolerance. |
| Arbitrary expander labeling | Open | A uniform compression theorem beyond the stated good-label event. |
| Inference, sample cost, practical construction | Outside the proved state-resource results | A separately defined data/noise/computation task. |

Keep continuation results in the ledger with their proved, conditional or open status. In particular, failure of a logarithm-transfer estimate at unbounded rates is a proof limitation, not a cap-free theorem or a counterexample. Manuscript drafting remains the final step in the user's requested order; this preparation task does not start it.

## 9. Equation, figure and bibliography inventory

The mathematical source material is present. The current repository has no standalone figure assets or machine-readable bibliography; existing comparison tables, equations and exact reports provide their source data. Do not turn asymptotic bounds with unmatched exponents into numerically calibrated curves.

| Later asset | Exact reusable content | Source and remaining production step |
|---|---|---|
| Model and task equation set | Original rates, equilibrium, $\mathcal D_H$ and worst-case state count | Sections 2–3 above and [Theory](THEORY.md); unify notation when the theorem selection is fixed. |
| Uncapped principal equation set | Polynomial stationary upper/lower versus superpolynomial reversible lower; $e^{-C(n+1)^2}$ accuracy allocation | [Uncapped theorem equations (1), (19)–(22)](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md); [observability equation (17)](BOUNDED_CONTROL_RESOLVENT_OBSERVABILITY.md). Keep the arbitrary-switching limitation beside the bound. |
| Principal theorem equation set | Binary common-budget inequalities and nineteen-level variant | [Binary equations (1)–(5)](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level equations (1)–(2)](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md). Preserve explicit constants, growth-class qualification and rival conditions. |
| Proof mechanism equation set | Physical scalar transfer, stationary repair, deterministic decoding and entropy support bound | [Binary Sections 4–7](BINARY_REVERSIBILITY_LOWER_BOUND.md); [nineteen-level Sections 3–7](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md); [whole-word boundary lemma](UNBOUNDED_RATE_REVERSIBILITY_BOUNDARY.md). Choose one proof route rather than merging hypotheses from different routes. |
| Quantitative extension equation set | Uniform cap-dependent lower, concrete target threshold, weaker fixed-clock formula | [State–speed–accuracy equations (3)–(6), (22), (26)–(30)](STATE_SPEED_ACCURACY_TRADEOFF.md). The clock belongs beside the bound. |
| Qualitative boundary equation set | Mixture-cluster rates, exact purity identity and positive error floor | [Finite-state closure equations (1)–(2), (8)–(12)](FINITE_STATE_FAST_RATE_CLOSURE.md). Label the hidden-state budget and leave the unquantified error floor explicit. |
| Physical construction schematic | Nineteen-level ports/hub or binary corridors, probes, marker and ballast | Principal construction notes and exact reports. Draw a schematic only after choosing which construction to foreground; show omitted repeated copies explicitly and keep total-state formulas visible. |
| Main comparison table | Shared constraints and polynomial versus singly exponential growth | Section 4 above and ledger P1–P5. Already tabulated; final typography is the remaining step. |
| Baseline comparison table | Passive / step / switching and aggregation / fresh realization | Section 6 above and ledger S3–S8. Keep target family and field-rule differences in the table. |
| Proof dependency diagram | Physical means to word scalars to stationary couplings to entropy; separate rank/upper branches | Section 5 above. Existing table is sufficient; a later diagram would be presentation only. |

The [main audit](PRIOR_ART.md) and [rate-boundary audit](RATE_BOUNDARY_PRIOR_ART.md) contain author/title/year records, primary links, relevant theorem locations and access limits for the central ingredients. They are sufficient to begin a selected-reference bibliography. After the eventual scope is fixed, consolidate only the cited records into a bibliography and verify exact publication metadata against the linked primary records; preserve unresolved access limits instead of filling them from memory. No new exhaustive-search claim follows from that formatting step.

The remaining nonmathematical inputs are the eventual theorem selection, author/affiliation/contribution metadata and any later formatting requirements. They do not prevent this research package from being complete for its present purpose. Figure production, final bibliography formatting and manuscript prose are deferred to the drafting stage; no new simulation is needed to support the existing theory claims.
