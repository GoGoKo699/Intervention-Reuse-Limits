# Publication scope and closest-theorem comparison

**PRL target decision, 23 September 2026.** The user selected *Physical Review Letters* as the target for the next exploration phase. The [PRL exploration record](PRL_EXPLORATION.md) sets the physical question and research priorities. The [research dossier](RESEARCH_DOSSIER.md) and [claim ledger](CLAIM_LEDGER.md) supply the quantified statements, dependencies, reproducibility and source links for eventual drafting. Manuscript drafting remains the last step; this assessment does not predict acceptance or certify priority.

The [two-switch theorem](FAMILIAR_SWITCH_STRUCTURE.md) now supplies the simplest physical example. Two interacting heat-bath conformational switches have four configurations, yet their controlled single-switch mean has an exact three-state stationary predictor. Ordinary detailed balance requires four states, for every finite positive coupling $J$ and queried field $H$, with equal attempt rates. The configurations are even under physical time reversal. Rivals retain a deterministic binary readout, balanced zero-field equilibrium preparation and the shared Gibbs tilt $\pi_h\propto\pi_0e^{hS}$; they may otherwise choose arbitrary new states and endpoint generators.

The [seven-experiment refinement](FAMILIAR_SWITCH_FINITE_MARGIN.md) now quantifies this distinction. A necessary quartic identity covers every ordinary rival with at most three states, even arbitrary reversible stochastic tick kernels with the shared tilt; no rate cap or continuous-time embedding is needed. It gives an explicit analytic occupation-error lower bound $\Delta/(2L)>0$ for all positive couplings, fields and clocks. At $J=H=\log3$ and clock two, seven words of at most four ticks and three segments certify ordinary minimum four and unrestricted minimum three whenever $\delta_P\le1/2000$. The explicit three-state construction serves arbitrary nonnegative-field protocol means, with exits below two. Binary path-law equality is not asserted, and the target's passive path already has memory.

The [exact verifier](../scripts/verify_familiar_switch_margin.py) and [certificate](../reports/familiar_switch_margin.json) are essential premises of the numerical bounds. The universal ordinary-three-state occupation error is $>1/2000$, while a fixed rational ordinary three-state model achieves $<837/10^6<1/1000$ on those same seven words. This brackets the error between 0.05 and 0.1 percentage points; the upper does not cover the eleven-word menu or arbitrary protocols. The [four-panel numerical screen](../reports/short_switch_witness_screen.json) and preceding [protocol study](FAMILIAR_SWITCH_PROTOCOLS.md) are separate feasible-fit evidence, not global optima or lower bounds. No one-percentage-point advantage or practical sample budget is established.

The next physical task is to quantify preparation, field and timing calibration errors and deviations from the shared Gibbs tilt. The [new source comparison](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) supplements the [kinetic source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md); priority and unresolved source access remain distinct from internal proof checks. No microscopic device realization, generalized-reversal separation or universal dissipation necessity is claimed.

The [matrix prediction principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) gives a simple organizing statement for a whole target class. A general stationary predictor can separate its incoming and outgoing memory profiles; ordinary detailed balance identifies the factors in matched reversed tests. For any normalized completely positive matrix $H$ of size $n$ with positive row sums, the exact state minima are $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$ under the shared interface and cap. The targets still have two-state passive paths. Both counts persist on a positive matrix-dependent accuracy interval, whose useful scale remains unknown in general. This is a controlled realization theorem, not a new matrix-rank definition or a generic HMM-order characterization.

The [kinetic-variance theorem](KINETIC_VARIANCE_COMPRESSION.md) supplies a complementary simple mechanism: heterogeneity excites hidden deviations and reads them back into the visible mean. Its exact memory equation yields uniform compression bounds. For the preceding twelve-state target, two reversible states suffice within $557/51920<0.01073$ on every two-field protocol and horizon. This makes the precision limitation concrete. The [new source comparison](SIMPLE_PREDICTION_SOURCE_AUDIT.md) attributes static rank interpretations, stochastic normalization, projection memory equations and uniform coarse-graining to established literature; the [internal review](SIMPLE_PREDICTION_INTERNAL_REVIEW.md) records the new controlled statements and their boundaries.

The [finite construction](FINITE_REVERSIBILITY_ADVANTAGE.md) now has a [stable rational observation certificate](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md): ordinary-reversible minimum twelve at mean error $\delta\le2^{-220}$, while an exact eleven-state stationary predictor suffices. The same interface, hidden cap $2k$, two fields and clock are retained; 12,766 explicit experiments use at most 66 ticks each. The [earlier minimum theorem](FINITE_PREDICTOR_MINIMALITY.md) proves unrestricted minimum eleven only on $\delta\le2^{-1360}$, using its earlier witness family. The new threshold remains far below useful measurement accuracy. No eleven-state generalized-reversible predictor is established.

A complementary [symmetry-compression theorem](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) gives a nine-state ordinary-reversible predictor with mean error at most $1/2376$ on every two-field switching protocol and horizon. Thus a substantial compression is possible at larger errors; the wide interval between this sufficient upper and the state-gap lower remains unresolved. For this earlier twelve-state example, that bounds its physical significance without estimating the optimal error. The familiar two-switch target above is the subsequent simpler comparison.

The [source supplement](FINITE_PRECISION_SOURCE_AUDIT.md) identifies direct prior examples of the exact core matrix, including Fawzi–Parrilo Eq. (55). Neither that matrix nor its positive-rank gap is a novelty claim. The candidate contribution remains the controlled Markov realization and quantitative same-interface comparison. The [new source audit](RATIONAL_OBSERVATION_SOURCE_AUDIT.md) identifies prior finite-matrix realization, divided-difference calculus, second-order response and uniform perturbation bounds. The [internal review](RATIONAL_OBSERVATION_INTERNAL_REVIEW.md) distinguishes the new quantitative connection from those ingredients. The experiment menu is now explicit and reproducible; its tiny error budget still gives no practical sample or measurement guarantee.

The [single-force interpretation](SINGLE_FORCE_CONFORMATIONAL_MODEL.md), [physical-source assessment](PHYSICAL_REALIZATION_SOURCE_AUDIT.md), [uniform perturbation bounds](PHYSICAL_INTERFACE_ROBUSTNESS.md) and [even-observation closure](PHYSICAL_REVERSAL_REALIZATION.md) fix an ordinary-parity conformational model class. They do not supply a microscopic molecular realization. Small rate errors and finite ramps have a quantitative accuracy floor; arbitrary hidden control dependence is not resolved for the state-count classification. The variance theorem separately permits field-dependent hidden generators with a common stationary law.

The earlier asymptotic comparison distinguishes ordinary detailed balance from generalized time reversal on a counted memory representation. On the same equilibrium targets, under the same hidden exit cap $3k$ and two-field fixed-clock task, unrestricted and generalized-reversible predictors have polynomial state growth, while ordinary reversible predictors have exponential growth in a positive power of inverse error:

$$
D_{\rm all}=D_{\rm inv}=\delta^{-\Theta(1)},\qquad
D_{\rm id}=\exp(\delta^{-\Theta(1)}).
$$

These equalities identify growth classes, not matching exponents or identical state counts. The target retains its original nineteen-level actuator, hidden relaxation band $[k,3k]$ and exact two-state passive visible law. Rivals may use arbitrary finite new state spaces and their own bounded kinetic barrier functions
$q_{iA}(h)=kb_i(h)$, $q_{Ai}(h)=k\mu_i e^{2h}b_i(h)$, with $b_i(0)=1$. No target alphabet or histogram is imposed. The common equilibrium bias, field-independent hidden generator, preparation and readout remain specified. Two fields $0,H$ at every fixed positive clock $a/k$ suffice.

The preceding five proof notes retain the asymptotic scope:

| Result | Established advance | Scope |
|---|---|---|
| [Capped kinetic separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) | Polynomial unrestricted and exponential ordinary-reversible state growth on the same two-field task. | Common exit cap $3k$; arbitrary bounded endpoint kinetics with the shared local-balance ratio; no histogram matching. |
| [Generalized-reversal prediction](GENERALIZED_REVERSAL_PREDICTION.md) | A polynomial word predictor has an explicit reversal involution, an even actuator and exactly the same controlled response as the earlier word predictor. | Generalized stationary entropy production is zero; a physical device implementing that parity is not supplied. |
| [General-interface entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) | A common reset and entrance rates bounded relative to the stationary hidden law give a uniform same-state endpoint comparison. | The distance bound needs no equilibrium ratio; interpreting the comparator as fully reversible additionally requires the stated common ratio. |
| [Uncapped kinetic comparison](GENERAL_KINETIC_INTERFACE.md) | The ordinary-reversibility lower survives arbitrary hidden rates and arbitrary bounded endpoint kinetics; unrestricted polynomial necessity now uses the same two fields. | The ordinary lower has fifth-root-log growth; the original tight-band target is unchanged. |
| [Kinetic and reversal resource frontier](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | The stronger identity-reversal entropy-production frontier extends beyond exponential barriers and exact histogram matching. | It is distinct from the zero generalized entropy-production upper; no implementation-independent dissipation necessity follows. |

The parity boundary is substantive. A centered word representation obeys $K^*=\Theta K\Theta$, with a fixed counted-state involution $\Theta$, while retaining the original interface, rate cap and histogram. Its stationary path law is invariant under the corresponding generalized reversal. Thus an ordinary-reversibility penalty cannot be interpreted as a generic thermodynamic cost when arbitrary reversal parities are admitted. Whether a natural physical implementation has that parity is a separate unresolved question.

For a positive lower return envelope $b_-$ and upper entrance factor $c_+$, meaning $b_i(h)\ge b_-$ and $e^{2h}b_i(h)\le c_+$ on the allowed controls, the full zero-field **identity-reversal** entropy-production rate satisfies

$$
\mathcal D_H(F,F_{\rm sym})\le
\sqrt{\frac{c_+}{b_-^2}\frac{\sigma_0^{\rm id}}k},\qquad
D_{\le\Sigma}^{\rm id}(\delta)\ge D_{\rm id}(\varepsilon),\quad
\varepsilon=\delta+\sqrt{\frac{c_+}{b_-^2}\frac\Sigma k}.
$$

Under the common cap $3k$, the resulting lower is $\exp(c\varepsilon^{-\alpha})$ on the broad kinetic class, without exact histogram matching. A uniform polynomial state budget requires worst-case $\Sigma\ge c'k[\log(1/\delta)]^{-2/\alpha}$. Conversely, a polynomial generalized-reversible predictor can have finite identity-reversal rate $\sigma_0^{\rm id}\le(3k/2)\log(12R/\delta)$, $R=e^{(1+G)H}$ and $G=9/100$, and simultaneously zero generalized stationary entropy production. The curves are unmatched. These quantities do not identify state count with stationary Shannon entropy, or stationary entropy production with driven heat or device power.

Without a rival rate cap, the same original targets and two fields satisfy

$$
D_{\rm all}^{\mathrm{kin},(2,a)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm id}^{\mathrm{kin},(2,a)}(\delta)\ge
\exp\!\left(\exp\!\left(c_{a,H}[\log(1/\delta)]^{1/5}\right)\right),
$$

with constants also depending on the fixed interface bounds. The matching unrestricted lower now follows from the new target-only two-field rank argument; the earlier thirty-nine-field restriction is no longer needed in this shared-interface class. A target of index $n$ has capped witnesses with $O(n+1)$ ticks at error $e^{-C(n+1)}$, and uncapped ordinary-reversibility witnesses with $O((n+1)^5)$ ticks at error $e^{-C(n+1)^5}$. Neither statement gives experiment counts, sample costs or practical parameter precision. The stronger capped state and entropy frontiers are not asserted without the cap.

The [source comparison](KINETIC_PARITY_SOURCE_AUDIT.md), [bounded verifier](../scripts/verify_kinetic_parity.py), [report](../reports/kinetic_parity.json) and [verification record](VERIFICATION.md) distinguish prior ingredients, mathematical audits and finite checks. They do not constitute external peer review or priority certification. On the original endpoint interval, arbitrary kinetic curves are exactly reparameterized by effective exponential sensitivities at $0,H$; the two-field data do not identify their intervening functions. Wider fixed intervals are covered by the positive-selector proof.

Earlier comparisons retain their historical assumptions. The [original-rule tight-band theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) supplied the uncapped fixed-clock foundation. The [binary fixed-clock uncapped theorem](FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) uses a rescaled tagged target and inner exponent $1/12$. Earlier [binary](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) and [nineteen-level](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) uncapped routes give inner exponent $1/2$ with arbitrarily rapid switching. The older fixed-budget results below remain valid at their stated menus and histograms.

The next priorities are a microscopic justification of the stipulated force-controlled model, a useful finite tolerance for the now-certified small advantage, and tighter identity-reversal entropy frontiers. A practical finite-tolerance gap and a physical realization of the word involution have not been established. The stronger uncapped law, a tight-band binary construction and matching quantitative bounds remain open. Manuscript drafting remains the final step.

[Repository overview](../README.md) · [Source audit](PRIOR_ART.md) · [Structure-cost proof](STRUCTURE_COST.md) · [Current work order](../work_orders/CURRENT.md)

**Supporting fixed-budget assessment, 22 September 2026.** A second principal result is an exponential-versus-polynomial cost of ordinary reversibility with a balanced binary actuator. The [binary theorem](BINARY_REVERSIBILITY_LOWER_BOUND.md) compares predictors of one target family under the same original kinetic field rule, exact histogram $\Pr(g=\pm\gamma)=1/2$ for fixed $0<\gamma<1$, stationary zero-field preparation, binary readout, and internal outgoing-rate budget $6580k$. Stationary nonreversible predictors have polynomial worst-case state growth in $1/\delta$; reversible predictors have singly exponential growth in a positive power of $1/\delta$. The lower allows arbitrary new states, with no aggregation or inherited-coordinate restriction.

The targets and reversible upper models have internal relaxation band $[k,13160k]$. Every reversible rival within the common exit budget has spectral cap $13160k$, which suffices for the lower; no positive lower gap is imposed on rivals. Both lower bounds already hold for five fixed fields at any fixed positive control clock, with witnessing horizons logarithmic in inverse error. The upper bounds serve all bounded protocols and all horizons. Exponents are not matched. The [nineteen-level theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) retains the cleaner numerical exit budget $3k$ and target band $[k,3k]$. The binary result does not retain that numerical band or remove the competitor rate cap.

The binary proof uses short observed patterns to identify gates in the target. An arbitrary rival need not interpret those patterns as state labels: its marker polynomial can be a general positive operator. A positive change of weight and quantitative transport repair turn recovered gate relations into stationary couplings on the rival's own states. Approximate invariance under each decoded lamp flip forces high entropy and exponentially many states. Binary coding, Doob transformations, marginal repair, lamp growth, entropy, and logarithm expansions have established antecedents. The [source comparison](PRIOR_ART.md) identifies the additional quantitative bridge and does not certify originality. Manuscript writing remains on hold.

The earlier task comparison remains a complementary result: over the same bounded binary target class, passive observation, all constant-field steps, and switching need exactly two, $\Theta(\log(1/\delta))$, and $\delta^{-\Theta(1)}$ states respectively. Its common analytic reversible step model may change the kinetic field rule. Separate positive routes give polynomial reversible switching compression under density moments, small stationary-flux fragmentation, or typical fixed binary labels on logarithmic-girth expanders. A six-level family also separates stationary-flux aggregation from a fresh reversible realization. The sharp rank-one, cubic, path-information, and robustness results remain foundations and operational consequences.

## 1. Controlled state cost and the sharp subclass

### A balanced binary actuator already forces an exponential reversibility cost

Fix $k,H>0$, $0<\gamma<1$, and $B=6580$. The [binary family](BINARY_REVERSIBILITY_LOWER_BOUND.md) has exact hidden histogram $\Pr_\mu(g=\pm\gamma)=1/2$, variance $W=\gamma^2$, and target band $[k,2Bk]$. Both predictor classes have the original field rule, exact histogram, stationary zero-field preparation, binary visible readout and internal exits at most $Bk$. Their worst-case minimal total state counts over the same targets satisfy

$$
\begin{aligned}
c_0\delta^{-\zeta}&\le D_{\rm all}^{(B)}(\delta)\le C_0\delta^{-p_B},\\
\exp(c_1\delta^{-\alpha})&\le D_{\rm rev}^{(B)}(\delta)
\le\exp\!\left(C_1\delta^{-p_B}\log(2/\delta)\right),\\
p_B&=\frac{\log2}{\log(1+1/[B e^{(1+\gamma)H}])}.
\end{aligned}
$$

The constants and exponents are fixed and positive; their optimal values are not matched. Both lower bounds need only five fixed fields and held segments in $(a/k)\mathbb N$ for each fixed $a>0$, with horizons $O_a(\log(1/\delta)/k)$. The uppers are uniform over all bounded protocols and horizons.

For $r=2^n$ addresses, the counted target has $224r2^r+4$ physical states. Undirected corridors encode the four address/lamp gates, probe cycles read the queried sign, a marker identifies logical roots, and a weighted hub and ballast give a uniform gap and exactly balanced colors. Every added vertex is counted. The nonlazy target update matrix makes a fixed marker polynomial equal a root projection of mass $1/18$.

That polynomial need not be a projection on an accurate rival. If its positive selfadjoint value is $A_*$ and $u=A_*1$, restrict to $u>0$ and use probability proportional to $\mu u^2$. Diagonal conjugation preserves the relevant $L^2$ norms and turns approximate relations $T_gu\simeq u$ into small stochastic defects. Bounded query functions and a mixed-norm transport repair estimate control products without assuming a pointwise lower bound on $u$. Rounding then produces a deterministic lamp law on actual rival states with small error under every bit flip. The established entropy argument gives the exponential state lower. The unrestricted lower instead uses the separate target-only rank transfer.

The nonreversible word upper uniformizes at the actual exit budget $Bk$. The reversible prediction-partition upper retains the band $[k,2Bk]$, and its intercell exits are conditional averages of original exits, hence at most $Bk$. A spectral cap $2Bk$ alone would not justify that sharper exit bound; the flux construction does. The common budget comparison concerns ordinary detailed balance, not a generalized reversal involution.

The constant $6580$ is a sufficient gadget budget, not an optimal threshold. A binary separation retaining the earlier tight numerical band $[k,3k]$ remains open, as do an uncapped lower on this same older target family and arbitrary reversible field rules. The later tagged construction establishes binary uncapped existence with different target constants. The older nineteen-level theorem below supplies a simpler low-budget instance of the same mechanism.

### The nineteen-level construction has a smaller numerical rate budget

For the [dynamic-lamp family](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md), fix $k,H>0$ and the hidden stationary actuator histogram

$$
\Pr_\mu(g=0)=\frac12,\qquad
\Pr_\mu(g=\pm j/100)=\frac1{36},\quad j=1,\ldots,9.
$$

It has $G=9/100$ and $W=19/12000$. Both predictor classes use the original exponential field rule, one visible state $A$, a finite hidden stationary law with this histogram, stationary zero-field preparation, binary visible readout, and internal exits at most $3k$. Let their worst-case minimal total state counts over the common target family be $D_{\rm all}^{(3)}$ and $D_{\rm rev}^{(3)}$, with ordinary detailed balance additionally required in the second class. For sufficiently small $\delta$,

$$
\begin{aligned}
c_0\delta^{-\gamma}&\le D_{\rm all}^{(3)}(\delta)\le C_0\delta^{-p},\\
\exp(c_1\delta^{-\alpha})&\le D_{\rm rev}^{(3)}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log(2/\delta)\right),\\
p&=\frac{\log19}{\log(1+1/(3e^{(1+9/100)H}))}.
\end{aligned}
$$

All constants and exponents are positive at fixed physical parameters. Thus the growth classes are polynomial and singly exponential in a positive power of inverse error; no matching exponent is claimed. Error is uniform absolute error of the actual mean over all bounded protocols and horizons. Both lower bounds hold already on thirty-nine fixed fields, with every positive segment an integer multiple of any fixed $a/k$ and witnessing horizons $O_a(\log(1/\delta)/k)$.

For width $n$, the target has $r=2^n$ addresses and $18r2^r+2$ total physical states. Its counted coordinates are the complete independent lamp table, address, sign, nine routing ports, a hidden hub and visible $A$. Hub edges supply the band $[k,3k]$ while gate edges remain positive off-diagonal blocks. Short words query every table bit and separately flip each queried bit. The proof derives corresponding nearly stochastic adjoint transports on any accurate reversible rival, repairs their stationary fluxes on the same states, and rounds the query functions to a deterministic $r$-bit decoding. Near-invariance under each flip forces at least $2^{3r/4}$ rival states at errors $e^{-O_a(n)}$.

The reversible lower does not impose a partition, stochastic encoder, target topology or lower spectral gap. Any fixed rival cap $\Lambda k$, $\Lambda\ge3$, suffices. Taking $\Lambda=6$ covers all reversible rivals with internal exits at most $3k$. The reversible upper is a prediction partition $EKE$ retaining the target band $[k,3k]$; the nonreversible upper uses a rate-$3k$ word chain. Both therefore meet the same outgoing-rate budget. Only the reversible upper is said to retain the spectral band.

An orthogonal query Gram matrix separately gives the polynomial lower against arbitrary Markov predictors through the existing target-only rank argument. This historical proof uses the original field rule, exact histogram and fixed cap. The [new capped kinetic theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md) retains its exponential growth class with only two fields, arbitrary bounded barrier functions obeying the specified local-balance ratio, and no histogram matching. The [uncapped kinetic theorem](GENERAL_KINETIC_INTERFACE.md) removes the rival cap on this same target family, with a weaker quantitative lower. Unrelated equilibrium interfaces remain outside these state comparisons. The nineteen actuator values are fixed independently of accuracy. The binary theorem above removes that alphabet requirement at the larger budget $6580k$; it does not reduce the present $3k$ construction to two levels.

### An exponential cost of requiring a target-state partition

The [aggregation lower](AGGREGATION_STATE_LOWER_BOUND.md) and [register-scenery upper](REGISTER_SCENERY_COMPRESSION.md) concern one family with fixed sensitivities $\{\pm1/10,\pm2/10,\pm3/10\}$, each of stationary mass $1/6$. Thus $G=3/10$ and $W=7/150$ are fixed. The internal band is $[3k/2,5k/2]$. All targets have the same exact two-state passive visible path law.

A permitted partition keeps $A$ separate and refines the actuator levels. Its reduced rates are stationary transition fluxes divided by cell masses, equivalently the conditional-expectation compression $EKE$. Cells may mix arbitrary configurations, addresses and signs within a level. Every such partition is subject to the lower, including optimally chosen unequal cells. Rates fitted independently after choosing cell names fall outside this architecture.

For width $n$, a target contains every configuration of $2^n$ independent table bits, a binary address register, three routing ports and a sign coordinate. All $1+6\cdot2^n2^{2^n}$ physical states are counted. Thirteen fixed physical field values extract port transports and address involutions as bounded-degree generator polynomials. Those operators act isometrically along their port itineraries. A palindrome response therefore measures the exact accumulated loss caused by conditional-expectation projections. If every controlled mean is accurate, partition cells reconstruct most independent bits at a root address; an entropy estimate forces at least $2^{5\cdot2^n/8}$ cells at error $e^{-O_a(n)}$. Whole-side logarithm truncation transfers this statement to actual means at any fixed clock $a/k$, with horizons $O_a(n/k)$.

The fresh-state upper applies to every width and every accuracy. Short address words act by affine dihedral permutations and finitely supported bit flips. Distinct formal words coincide on a long uniform register only with exponentially small probability. This allows a reference register of width $O(\log(1/\delta))$, followed by positive selection of complete table configurations. It preserves the original field rule, exact histogram, ordinary detailed balance and advertised band. A sufficient exponent is

$$
p=\frac{\log96}{\log(1+2/[5e^{(13/10)H}])}.
$$

The queried features are orthogonal across addresses, giving an exact Gram matrix $I_{2^n}/6$. The existing fixed-clock rank transfer therefore also gives a polynomial lower against arbitrary Markov predictors. Conversely, the general prediction-partition construction supplies a singly exponential aggregation upper. The comparison consequently determines both growth classes: $D_{\rm fresh}=\delta^{-\Theta(1)}$ and $D_{\rm agg}=\exp(\delta^{-\Theta(1)})$, with unmatched exponents, on the same physical target family and actual-mean norm. It demonstrates no intrinsic penalty for ordinary reversibility. It also does not remove the arbitrary-fixed-label assumption from the separate expander problem: the table dictionary here is a counted part of the target. A binary-actuator version of this architectural theorem is not claimed. The [source audit](PRIOR_ART.md) separates the new quantitative statement from established exact aggregation counterexamples, positive-realization theory and entropy methods.

### Every constant-field step can have a small common model

The [constant-step compression theorem](CONSTANT_STEP_COMPRESSION.md) and its [analytic strengthening](ANALYTIC_CONSTANT_STEP_COMPRESSION.md) apply to every original bounded-sensitivity target with internal spectral cap $\Lambda k$, without a finite-alphabet assumption. Reversibility and the equilibrium tilt express each step mean as $\tanh(h)[1-\phi_h(t)]$, where $\phi_h$ is a positive exponential mixture supported in the uniform interval $[k/R,2k(\Lambda+R)]$. Positive quadrature needs only $O(\log(1/\delta))$ modes. A two-block Jacobi realization, a commuting stationary reset, and a fixed preparation perturbation make these mixtures into one physical Markov predictor with a common state space, binary readout and stationary zero-field preparation.

For the binary band $[k,3k]$, the existing capped rank-one lower witnesses establish the matching logarithmic order for the menu of all constant amplitudes. Their witnessing amplitude can shrink with state budget; no fixed-amplitude capped lower is inferred. Combining this with the switching theorem gives:

| Common target class | Passive path | All constant steps | Switching, including any fixed clock |
|---|---|---|---|
| Centered binary sensitivity, internal band $[k,3k]$ | $2$ exactly | $\Theta(\log(1/\delta))$ | $\delta^{-\Theta(1)}$ |

The comparison uses the same broad instantaneous-field competitor class and the actual-mean norm for the two intervention tasks. The analytic step upper additionally preserves the stated structure and real-analytic field dependence, but does not impose the original field rule or a uniform bound on field derivatives or function-description complexity. It does not claim that any fitted constant-step model predicts switching accurately. The shift-register witnesses themselves have the logarithmic step upper and polynomial switching lower.

The analytic strengthening regularizes the positive spectral measure by a small fixed reference measure, ensuring nondegenerate moment matrices. Two active Jacobi blocks have analytically varying positive root masses; their stationary law at zero provides the common preparation. A commuting interpolation with stationary refresh calibrates the exact passive law at zero. The interpolation starts at second order in the field and its zeroth-order correction annihilates the preparation, so the universal linear mean and zero quadratic mean hold for every weak protocol. These changes retain the logarithmic state order and remove the earlier discontinuity. They do not provide full switching accuracy.

### The three costs already occur with local motion on a line

The [local-walk theorem](LOCAL_WALK_LOWER_BOUND.md) uses a finite path carrying a binary string. Its hidden state records both the string and a position, and the actuator reads the current site's label. Between stationary refreshes, the position makes symmetric nearest-neighbor jumps. Every possible string is included and counted in the physical state space. This is a finite random-scenery construction, an established model idea; the externally observed variable still records only whether the system occupies the hidden block or $A$.

At depth $n$, the hidden path has $4n+3$ positions and the target has $(4n+3)2^{4n+3}+1$ total states. Local jump rate $k/4$ and stationary refresh rate $3k/2$ keep all internal relaxation rates in $[3k/2,5k/2]$. A maximal-distance projection selects $2^n$ distinct Walsh leaves with Gram floor $48^{-(4n+2)}/[2(4n+3)]$. The existing physical endpoint identities and total-degree logarithm argument transfer this to actual means using only two fixed fields and any fixed positive control clock. Competitors with fewer than $2^n$ states incur error at least $e^{-C_a(n+1)}$.

The [sparse reversible upper](SPARSE_REVERSIBLE_COMPRESSION.md) cuts local edges at small stationary jump cost, then selects a convex combination of whole small component models. This preserves positive rates and detailed balance directly. Matching their finite actuator-prefix laws and restoring the same global refresh gives one reversible predictor for every bounded protocol and horizon. For the corresponding binary path class,

$$
c_a\delta^{-\gamma_a}\le D_*^{\rm path}(\delta)
\le D_{\rm rev}^{\rm path}(\delta)
\le C\delta^{-(1+p_{5/2})},\qquad
p_{5/2}=\frac{\log2}{\log(1+1/[(5/2)e^{(1+\sqrt W)H}])}.
$$

The upper retains the original field rule, exact actuator histogram and the band $[3k/2,5k/2]$. Both competitor classes therefore have polynomial growth; their optimal exponents need not coincide. Interior path eigenvalues also give a logarithmic constant-step lower in this same class. The analytic logarithmic step upper applies, with its existing freedom to change the field rule. Thus the full passive/step/switching comparison holds in one concrete local class.

Along the switching witnesses, the cubic kernel is an equally weighted sum of $4n+3$ path relaxation modes, giving exact cubic minimum $4n+5$. The mean-prediction lower is not a claim that an individual scenery can be learned efficiently from observations. The global refresh is part of the stated dynamics; no entirely local full generator or molecular implementation is asserted.

More generally, the component proof gives $D\le1+S(\varepsilon)m^{\ell+1}$ with error $R^3\varepsilon+C_Rq_\Lambda^{\ell+1}$ whenever local edges can be removed at directed stationary flux at most $\varepsilon k$ and leave components of size at most $S(\varepsilon)$. Fixed-dimensional nearest-neighbor lattices have sufficient count $C\delta^{-(d+p_\Lambda)}$. This handles density moments that diverge with system size. A spectral cap or bounded degree alone does not imply small-cost fragmentation; a local Poincaré gap gives an explicit obstruction to that approximation step.

### Connected local expanders with one fixed labeling

The [expander upper](EXPANDER_SCENERY_COMPRESSION.md) and [expander lower](EXPANDER_SCENERY_LOWER_BOUND.md) establish a polynomial growth class when the sparse local generator itself is connected and has a size-independent gap. Fix a degree-four logarithmic-girth expander family, with base order $N$. The hidden states are $(v,\sigma)$, the binary label $x_v$ is frozen, and the actuator is $g=s\sigma x_v$. A dynamic sign flip ensures the exact balanced histogram for every labeling. The local generator is $k(P_G-I)/4+k(J-I)/4$; adding the prescribed stationary refresh $3k(\Pi-I)/2$ gives the advertised internal band $[3k/2,5k/2]$. The full physical count is $2N+1$. A dictionary of all labelings is not part of this target.

For each base graph fixed before drawing independent labels, one event $\mathcal E_G$ has probability greater than $3/4$ and is defined simultaneously over every stationary local-prefix length. Every labeling in this same event has a polynomial reversible predictor at every accuracy. For short prefixes, high girth identifies the annealed local walk and sign-flip statistics with those on a smaller graph. Positive selection of whole colored components realizes those statistics exactly. Bounded differences controls the frozen-label error, and conditioning on refresh runs transfers it to the all-protocol, all-horizon actual-mean norm. When the requested prefix or accuracy is too demanding for a given base size, retaining the exact target still obeys the uniform polynomial budget.

The lower selects independent Walsh directions along long unique geodesics. Global spatial centering does not erase label characters; an explicit $B_n/N$ estimate controls that correction. Averaging over every terminal vertex gives an expected Gram floor without a further $1/N$ loss. Concentration selects one frozen labeling. Its lower event intersects $\mathcal E_G$, so hard targets belong to the upper's all-accuracy class. At every fixed control clock $a/k$,

$$
c_a\delta^{-\gamma_a}\le D_*^{\rm good}(\delta)
\le D_{\rm rev}^{\rm good}(\delta)\le C\delta^{-p_g}.
$$

The lower permits arbitrary instantaneous-field Markov competitors with fixed preparation and readout. The reversible upper keeps the original field rule, exact histogram and advertised band; it need not keep the target graph or its larger actual gap. On the degree-four Morgenstern family a sufficient exponent is $p_g=(\log2+8\log3)/\log(1+2/(5e^{(1+s)H}))$. This uses established graph-existence and concentration results, as recorded in the [source audit](PRIOR_ART.md).

The connected local gap forces nonvanishing stationary-flux cost for bounded-size fragmentation, and the local edge densities have every positive density moment diverging with $N$. Thus the new result handles a substantive class beyond both earlier sufficient conditions. The lower and upper exponents remain unmatched. Arbitrary deterministic labelings and the tight-band binary reversible problem remain open. The binary theorem above rules out general polynomial reversible sufficiency at a larger fixed budget. The analytic $O(\log(1/\delta))$ constant-step upper applies here, but a matching step lower in this same typical-label expander class has not been proved; the complete three-task equality above remains attached to its established target classes.

### Bounded binary targets: lower and upper bounds

Fix $k,W,H>0$, put $s=\sqrt W$, and consider the original targets with $g=\pm s$ and nonzero internal relaxation rates in $[k,3k]$. Centering fixes the stationary mass at each sensitivity level to $1/2$. Let $D_*^{\rm bin}(\delta)$ be the worst-case state count over this target class, with the actual-mean error taken over all bounded protocols and horizons. Competing Markov predictors have a fixed preparation and readout; they need not be reversible, analytic in the field, or calibrated to passive data.

The [polynomial controlled-word lower theorem](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) and [bounded-rate upper theorem](BOUNDED_RATE_FINITE_FIELD.md) give, for sufficiently small $\delta$,

$$
\boxed{c\delta^{-\gamma}
\le D_*^{\rm bin}(\delta)\le C\delta^{-p},
\qquad \gamma,p>0,}
$$

where a sufficient exponent is

$$
p=\frac{\log2}{\log(1+1/(3R_s))},\qquad R_s=e^{(1+s)H}.
$$

The lower witnesses lie in the narrower band $[3k/2,5k/2]$ and use only $0$ and one fixed $h_*>0$. Their positive reversible shift-register generator supplies exponentially many independent controlled directions. Truncating the logarithm expansion by total degree across each complete left or right word transfers this controlled matrix rank to actual-mean error with only exponential coefficient cost in word length. It uses no bound on a competitor's generator or field derivatives. The conclusion $D_*^{\rm bin}(\delta)=\delta^{-\Theta(1)}$ specifies a polynomial growth class, with fixed positive lower and upper exponents; it does not identify a matched exponent or an exact power law.

The upper construction uses exact Poisson-clock uniformization, a stationary finite-order word chain, and coupling renewed at returns to $A$. Its stationary actuator histogram is exactly the target's, so the sensitivity values, all moments, passive law, equilibrium curve, and linear/quadratic mean responses are retained. Its internal dynamics may be nonreversible. It serves every allowed protocol and horizon, rather than fitting each control sequence separately.

### The polynomial obstruction survives any fixed control clock

For any fixed $a>0$, use only fields $0,h_*$ and require every positive-duration held segment to be an integer multiple of $a/k$. If $D_{*,a}^{\rm bin}(\delta)$ denotes the corresponding worst-case state count on this smaller experiment menu, the same shift-register targets give

$$
D_{*,a}^{\rm bin}(\delta)\ge c_a\delta^{-\gamma_a},
\qquad \gamma_a>0.
$$

Witnessing experiments have total duration $O_a(\log(1/\delta)/k)$. The polynomial upper serves all protocols and horizons, so the fixed-clock task also has the growth class $\delta^{-\Theta(1)}$. Allowing arbitrary segment durations at least $a/k$ only enlarges this menu and retains the conclusion. Constants and the lower exponent can depend on the fixed clock spacing. The proof uses signed combinations of many mean experiments and may have large coefficients. It establishes a state-dimension obstruction; no statistical sample bound is proved here.

The [earlier shift-register note](SHIFT_REGISTER_LOWER_BOUND.md) retains the original physical construction and the weaker transfers $\exp(cL/\log L)$ without a timing restriction and $\exp(c_aL^{2/3})$ with fixed minimum dwell, where $L=\log(1/\delta)$. Whole-side total-degree truncation strengthens both bounds without changing that target or its controlled Gram witness.

The earlier [binary-tree construction](GENERAL_CONTROLLED_LOWER_BOUND.md) remains a useful foundation. Within that family, the exact cubic response needs $n+3$ states while full controlled prediction requires between $2^n$ and $2^{n+1}+1$. The shift register has a related exact comparison: $4n+5$ states suffice and are necessary for cubic response, while the full controlled mean needs at least $2^n$. The polynomial theorem now places this comparison at precisions $\delta_n=\tfrac12e^{-C_a(n+1)}$: exact cubic prediction costs $O(\log(1/\delta_n))$ along a sequence where full controlled prediction requires a positive power of $1/\delta_n$. The cubic minima use the analytic-in-field Markov class; the full controlled lower bounds allow broader competitors.

### Reversible predictors and the broader general family

For at most $m$ actuator values and internal relaxation rates at most $\Lambda k$, put

$$
R=e^{(1+G)H},\qquad
p_{m,\Lambda,G,H}=\frac{\log m}{\log(1+1/(\Lambda R))}.
$$

The [reversible bounded-rate construction](BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) gives

$$
D_{\rm rev}(\delta)
\le\exp\!\left[C\delta^{-p_{m,\Lambda,G,H}}\log(2/\delta)\right].
$$

It preserves the exact stationary actuator histogram and the target's spectral band, including any specified positive lower gap. It therefore preserves variance $W$, sensitivity bound $G$, and every prescribed passive/static/low-order agreement, with ordinary detailed balance. These upper bounds alone do not establish a separation. The dynamic-lamp lower proves that a general polynomial reversible bound is impossible for nineteen levels at exit budget $3k$; the binary extension proves the same growth-class gap at budget $6580k$. The tight-band binary question and optimal exponents remain open.

There is now a sufficient structural condition for a polynomial reversible upper. Suppose $K_{ij}/\mu_j\le Lk$ for $i\ne j$, with fixed $L$. For a fixed alphabet of $m$ actuator values, [stratified reversible sampling](BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) gives $D_{\rm rev}(\delta)\le C\delta^{-2(1+p_L)}\log^3(2/\delta)$, where $p_L=\log m/\log(1+1/(LR))$. Sampling within each actuator level preserves its stationary mass exactly; symmetric sampled transition weights and a small reset retain positivity and ordinary reversibility. Concentration on finitely many word-prediction functions, followed by regeneration, gives the all-protocol/all-horizon mean bound. This model uses the original field rule and has internal spectral cap $2Lk$, without a claim to preserve the original gap or band. The density assumption is stronger than a spectral cap. This is a sufficient structural subclass; the binary theorem gives a counterexample to general polynomial sufficiency under a fixed rate budget.

The [density-moment extension](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) weakens the pointwise condition. For dimensionless $q_{ij}=K_{ij}/(k\mu_j)$ off the diagonal and $q_{ii}=0$, assume $\sum_{i,j}\mu_i\mu_j q_{ij}^{1+a}\le M$ for some fixed $a>0$. At internal cap $\Lambda k$, its sufficient count is $C\delta^{-[2(1+p_\Lambda)+1/a]}\log^3(2/\delta)$, with $p_\Lambda=\log m/\log(1+1/(\Lambda R))$. The internal surrogate cap is $2\Lambda k$, and the original field rule and actuator histogram remain exact. A uniform occupation-density bound controls the error from clipping only the stationary removed jump flux. Bernstein concentration and one global rate rescaling keep the update clock tied to $\Lambda$, preventing the growing clipping threshold from entering the exponent. The theorem also states a more general tail-dependent bound. The spectral cap alone gives no such tail control; an exactly compressible matching example rules out that shortcut.

For arbitrary bounded $g$ and unrestricted internal rates, the [general reversible upper theorem](REVERSIBLE_GENERAL_COMPRESSION.md) still supplies

$$
D(\delta)\le\exp\!\left\{\exp\!\left[C_{G,H}\log^2(16/\delta)\right]\right\},
$$

inside the original family, with exact variance and sensitivity bound. This is a broader target class than the bounded finite-alphabet class above. Existence of a structure-preserving approximation is settled, while its optimal general cost is not. The earlier nonreversible finite-word upper construction remains a precursor and source of shared estimates.

### The rank-one subclass has a sharp answer

The [sharp finite-field theorem](FINITE_FIELD.md) concerns a smaller target subclass. That subclass has one hidden state of stationary mass $1/2$ and sensitivity $+\sqrt W$, while all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel of mass $W$ has a realization in this subclass. This is an additional actuator-geometry restriction, not a generic statement about every centered bounded sensitivity vector.

For fixed $k,W,H>0$, the approximation norm measures the **actual mean** over all protocols $|h(t)|\le H$ and all horizons. The worst-case state requirement is $\Theta(\log^2(1/\delta))$, or $\Theta(\log(1/\delta))$ when active target rates are at most $3k$. Reversible surrogates retain the exact passive law and specified lower-order responses. The lower bound permits arbitrary instantaneous-field Markov predictors, with a fixed readout and preparation; they need not have analytic rates or satisfy any passive-data constraint.

For unrestricted rates, the lower order already holds for [one fixed step](FIXED_FIELD_LOWER_BOUND.md) with amplitude $h_* = \min\{H,[20(1+\sqrt W)]^{-1}\}$, independent of the state budget and tolerance. The proof uses the exact positive spectral expansion of the finite-field step mean and the rank of any competing Markov curve. It does not infer a derivative bound from a small real-field error.

The exact kernel closure is special. An explicit four-state counterexample in the finite-field note holds $k,\mu,g$, and the cubic kernel fixed while changing a higher response through $K$. This is a demonstrated boundary of the result, rather than an omitted genericity assumption.

### Cubic coefficients in the broader original family

Fix the target family, scalar field rule, stationary preparation, binary readout, bounded sensitivity, and coefficient norm in [Finite accuracy, Section 0](FINITE_ACCURACY.md#0-the-approximation-task-and-its-quantifiers). The intervention kernel is supplied exactly. One reduced model must work for every bounded protocol and every finite horizon.

The comparison can be strengthened beyond the original formulation. A relaxed competitor need only be a stationary-prepared analytic finite-state Markov model with a fixed real-valued readout; it need not reproduce the passive law or any lower-order response. Even in that relaxed class, the cubic-only approximation task has the same worst-case state-growth order as a reversible model that preserves all the prescribed agreements and the sensitivity bound:

| Target information, fixed positive $WU^3$ | Relaxed Markov fit to the cubic coefficient alone | Reversible fit preserving the prescribed structure |
|---|---|---|
| Unrestricted active rates | $\Theta(\log^2(WU^3/\varepsilon))$ | $\Theta(\log^2(WU^3/\varepsilon))$ |
| Active rates at most $3k$ | $\Theta(\log(WU^3/\varepsilon))$ | $\Theta(\log(WU^3/\varepsilon))$ |

The [structure-cost corollary](STRUCTURE_COST.md) proves this comparison. For unrestricted rates, the existing lower proof already applies to the relaxed class. For capped targets, filtering still cannot increase the coefficient-lift rank, so replacing the earlier witness mode count by $r=3D-1$ gives the required relaxed lower bound. The existing upper constructions retain all the structure.

Thus preservation does not increase the **asymptotic order** of the required state count in this family. This does not identify equal errors at a fixed state budget or equal leading constants. The relaxed competitor is judged only on its cubic coefficient; it may have incorrect passive behavior or lower-order mean response. The theorem does not say that arbitrary positive systems, physical constraints, or finite-amplitude predictions have no cost.

The exact two-versus-$N$ theorem remains the motivating zero-tolerance limit. These coefficient results support the finite-field theorem and continue to apply to a broader target family.

## 2. What a model builder can use

The intended use is compression after a microscopic model is known. Choose a field bound, an actual-mean tolerance, and the structural requirements on the predictor. A finite actuator alphabet and rate cap permit a polynomial sufficient count if nonreversible internal dynamics are allowed; a larger construction retains reversibility and the whole spectral band. Arbitrary bounded actuators and unrestricted rates have the more expensive general reversible existence bound. Each construction returns one model for the full protocol class and all horizons, retaining the complete passive binary law and the prescribed static and low-order agreements. These are worst-case guarantees rather than practical runtime recommendations. In the rank-one subclass, supplying the scalar kernel suffices; the general constructors use the full target.

State count measures the number of latent Markov states. It does not charge parameter precision, computing the spectral measure, fitting data, or running the resulting simulator. The worst-case lower bound is a limit on model dimension, not an experimental sample count or a wall-clock runtime bound.

For the rank-one subclass, a rate cap changes the sharp state order from squared logarithmic to logarithmic. The controlled-word witnesses instead keep their internal spectrum in $[3k/2,5k/2]$ and obtain a polynomial cost from many controlled hidden directions. This obstruction survives every fixed positive control clock and needs only logarithmic observation horizons in inverse error. A spectral cap and finite clock resolution therefore do not reduce this broader controlled task to the rank-one state law. The bounded-rate upper bounds use the finite actuator alphabet as well as the spectral cap.

The actuator must be specified kinetically. Local detailed balance fixes rate ratios but does not uniquely fix how barriers change. Within a comparison at fixed state labels, the target models can keep $k,\mu,g$ and the displayed field rule unchanged while changing only the internal generator $K$. Their complete microscopic generators are therefore different. A surrogate may use a different internal realization, but receives the same scalar protocol $h(t)$.

### What an observer can measure

The [path-response theorem](ACTIVE_PATH_RESPONSE.md) shows that all first-order visible-path responses are universal in the original family, whereas their second-order response is exactly characterized by $C$. A no-exit experiment gives a sharp $r+2$ state count without the cubic mean's resonance exception. For a specified pair, two snapshots attain $\Theta(h^{-4})$ weak-step discrimination trials, compared with $\Theta(h^{-6})$ for the final snapshot alone. This is a fixed hypothesis-testing task, not a general kernel-learning theorem. Preparation cost is excluded.

The [near-lumpability theorem](NEAR_LUMPABILITY.md) considers centered perturbations of external equilibrium conductances. Complete passive paths have relative entropy at most $q^4(152+241kT)$ from the telegraph law, uniformly over hidden dimension and internal rates. A three-state pair attains the quartic information scale and retains a finite active mean separation. It supplies a quantitative neighborhood of the ideal passive degeneracy, with explicit perturbation restrictions; it does not assert robustness to every microscopic change.

## 3. A diagnostic boundary: switching the field off versus keeping it on

The model provides an exact operational example without a molecular implementation claim. Prepare it in its stationary distribution at a constant field $h_0$, then switch the field to zero. Strong passive lumpability gives

$$
m_{\mathrm{off}}(t)=\tanh(h_0)e^{-2kt}
$$

for every internal generator $K$. In fact, the entire visible path law after switch-off is the same telegraph law with that initial mean. This statement is exact at finite $h_0$, because the post-switch dynamics use the zero-field generator.

For comparison with the perturbation-arrest relation of [Engbring et al.](PRIOR_ART.md#established-response-theory), the visible stationary-density ratio minus one is $z(S)=\tanh(h_0)S$. Both its passive autocorrelation and its switch-off mean are $\tanh^2(h_0)e^{-2kt}$. Passing that diagnostic is consistent with the genuinely Markovian zero-field visible process; it does not certify the model while the field remains on.

To see the distinction with fixed actuator parameters, take two three-state targets with $\mu=(1/2,1/2)$, $g=(\sqrt W,-\sqrt W)$, and internal flip rates $k/2$ and $3k/2$. Their kernels are $We^{-kt}$ and $We^{-3kt}$. Their passive laws, equilibrium curves, linear mean responses, quadratic mean responses, and stationary-preparation switch-off laws agree. Under the constant protocol $u=U$, however, the existing step formula gives

$$
m_{3,\lambda=3k}[U](1/k)-m_{3,\lambda=k}[U](1/k)
=\frac{WU^3}{2}(e^{-2}-e^{-4})>0.
$$

Thus even these ideal calibration records do not specify the cubic field-on response. Supplied intervention information remains necessary for the constructive compression task. The displayed difference concerns Taylor coefficients; it is not a uniform finite-amplitude error guarantee or a noise-certified inference procedure.

## 4. Theorem-by-theorem comparison

The [source audit](PRIOR_ART.md) gives bibliographic links, versions, access depth, and fuller qualifications. The table records the operative mathematical differences rather than treating a different name or error norm as a novelty argument.

| Inspected result | Resource and guarantee | Consequence for this project |
|---|---|---|
| Erschler–Zheng (2020), Theorem 1.1, Lemma 2.3, Corollary 1.2 | Lamp/Følner growth for finite subsets carrying prescribed group actions. | Exponential lamp support is established; deriving approximate flip couplings from physical means on arbitrary rival states is a separate step. |
| Verdú–Weissman (2008), Theorem 1, Eq. (5) | The conditional-entropy sum is at most the joint entropy. | The entropy inequality is standard; the dynamic-lamp proof must first produce the deterministic decoded law and small flip defects. |
| Grussler–Damm (2012), Theorem 4 | A symmetric positive minimal realization for a quasi-symmetric single scalar transfer function. | A single-transfer realization theorem does not supply one shared model for the noncommuting actuator words; stochastic normalization and the field rule need separate verification. |
| Basu et al. (2015), Sections III.1 and IV.1; Diezemann (2012), Eqs. (4)–(5), (25) | Nonlinear response under specified kinetic perturbations; no state-budget minimax theorem. | Passive agreement with different nonlinear response is established. Cubic order and kinetic dependence are not the contribution. |
| Müller et al. (2020), Eq. (30), Sections II–IV | Coarse joint-probability derivatives reconstruct arbitrary-protocol second-order response. | Establishes coarse response reconstruction, without a sharp cost in physical Markov states. |
| Cardelli et al. (2023), Theorems 2, 5–6 | Partition reduction; pointwise lumpability or extremal values under interval-rate controls. | Pointwise lumpability explains our passive construction. Corresponding uncertain controls need not be the same actuator realization. |
| Petreczky (2011), Theorem 2.3; Benner–Goyal (2017), Theorems 3.1–3.2 and 4.5 | Exact bilinear realization by Hankel rank, or Volterra/Gramian reduction in real state coordinates. | The coefficient lift is standard. Its signed coordinates are not physical Markov states; independent lifted inputs would also change the task. |
| Becker–Hartmann (2019), Definition 3.2, Corollary 3.3, Theorems 1–2 | State-factored Volterra Hankel operators and output bounds under stated stability/input assumptions. | Establishes the factorization framework. Our constant-step argument obtains a rank obstruction without imposing those input conditions on every surrogate. |
| Kotsalis–Shamma (2015), Definitions 2.1–2.3, Theorem 4.2; indexed primary excerpts | Stationary HMM word probabilities and a lower-order Hankel-norm obstruction. | Establishes the stochastic rank mechanism. The passive word law here already has an exact two-state realization; response derivatives require an additional construction. |
| Reis–Virnik (2009), Theorems 3.1–3.2 | Stable positive LTI reduction with an $H_\infty$ error bounded by an instance-dependent balancing tail. | Preserving positivity is established; a uniform tolerance-to-state law and the passive-equivalent reversible field family remain separate requirements. |
| Balle–Panangaden–Precup (2015), Theorem 2 and Section 3 | Word-Hankel rank and forward--backward factorization for real weighted automata. | The controlled rank mechanism is established; the positive physical target and quantified mean-error conversion are additional requirements. |
| Philippakis–Mallinar–Pandit–Belkin (2024), Sections 2.2–2.3 and Theorem 3.1 | Undirected de Bruijn walks, the Walsh deletion-and-shift representation, and tridiagonal spectral chains. | The shift-register graph and spectral mechanism are established; the controlled-word physical witness and polynomial actual-mean lower bound at fixed clock resolution are the candidate additions. |
| Bressaud–Fernandez–Galves (1999), Definition 2 and Theorem 4 | Canonical finite-order Markov approximation; stationary coupling convergence under additional continuity assumptions. | Short-block matching is classical. Our all-horizon mean estimate uses the physical reset and a bounded internal update clock, rather than assuming their continuity condition. |
| Marin–Rossi (2017), Corollary 3; Fornace–Lindsey (2025 v3), Proposition 4.1 and Theorems 3/3* | Reversible quotient generators and autonomous semigroup compression with instance-dependent error bounds. | Reversible compression itself is prior art; one uniform controlled surrogate, exact actuator variance, and a size-independent state count require separate proof. |
| Gesztesy–Simon (1997), Theorem 3.5 / Appendix A.6 | A positive finite spectral measure determines a Jacobi matrix. | Our reversible kernel realization is a direct corollary, not new inverse-spectral theory. |
| Koyama (2023 v3), Theorems 2.14 and 3.14 | Positive, mass-preserving exponential approximation on a spectral interval. | Clamping and the response estimate yield our upper order. The upper approximation mechanism is already known. |
| Lacroce et al. (2024), Theorems 2 and 16; Fasino (2023), Section 2.1 | Hankel rank/singular-value obstruction and explicit Cauchy inversion. | These supply classical lower-bound tools. The target construction and response-norm estimate make them applicable here. |
| Chowdhury (2026 v1), Appendix K.1, Proposition 2 | Autonomy of entropy-selected hidden dynamics despite exact ordinary visible-law agreement. | Closest complete-passive-law conceptual comparison; trajectory selection differs from our reversible scalar-field response and state-cost question. |

Two reductions are particularly important. First, the Taylor hierarchy becomes bilinear after replacing $u$ by the constrained triple $(u,u^2,u^3)$, and becomes a linear autonomous system under a constant protocol. No new general realization theorem is needed for that step. Second, Koyama's positive quadrature plus rate clamping already gives the upper asymptotic order; the explicit dyadic proof improves transparency and constants, not the mechanism.

The passive-HMM comparison can be made exact. At any fixed sampling interval, every target has the same visible word probabilities as the two-state telegraph model. An operator formed solely from those probabilities is therefore identical for the target and the two-state model. Its approximation error is zero even when driven predictions differ. The cubic lower bound uses a coefficient lift. The controlled-word lower bound instead constructs a matrix from actual means at fixed field amplitudes, using finite polynomial combinations of propagators and bounding their coefficient sums. Its strongest transfer truncates a logarithm expansion across each complete side of the matrix factorization. Both use established rank reasoning but require a separate connection to the intervention task.

Neither the earlier binary-tree construction nor the shift-register theorems claim a new rank, logarithm-series, interpolation, or spectral principle. The polynomial theorem must be assessed for its positive reversible physical target, binary actuator, bounded internal spectrum, controlled-word singular-value witness, and polynomial transfer to actual-mean error under every fixed control clock. The upper bounds likewise use established uniformization, canonical word approximation, conditional expectation, Galerkin projection, and moment matching. Their relevant claims are the state-count guarantees and exact model constraints retained under arbitrary bounded control; these require more than naming a classical construction.

A norm distinction alone is insufficient. For a scalar nonnegative impulse error, its $L_1$ norm equals the zero-frequency gain and its $H_\infty$ norm. Positive-system truncation can therefore sometimes transfer into a kernel estimate. A signed error need not have that property. The missing conclusion from the positive-reduction result is the full uniform complexity and constrained realization statement, not an assertion that its norm can never be useful.

## 5. Assessment and next scientific question

The PRL-directed exploration now distinguishes a cost of ordinary detailed balance from a cost of generalized equilibrium. The original tight-band target gives exponential-versus-polynomial state growth under one cap, two fields and broad kinetic freedom. A polynomial predictor with an explicit reversal involution has zero generalized stationary entropy production, so the result does not establish an implementation-independent dissipation requirement. The identity-reversal resource frontier remains quantitative and now needs no exact rival histogram or exponential barrier rule. The assessment is to continue exploration while testing a natural physical interpretation and finite-tolerance relevance; manuscript drafting remains on hold.

The current conclusions distinguish prediction tasks and predictor constraints.

| Question | Result | Essential limitation |
|---|---|---|
| Is there a simple general rule behind the finite state advantage? | [The matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) gives exact minima $1+n+\operatorname{rank}_+(H)$ and $1+n+\operatorname{cprank}(H)$ for a controlled target family. | Prescribed shared hub interface/cap, individually distinct target probe labels, and no useful general finite tolerance. Static ranks and their latent-variable interpretations are established. |
| When can hidden dynamics be ignored at coarse accuracy? | [The variance theorem](KINETIC_VARIANCE_COMPRESSION.md) bounds all-protocol mean error by stationary barrier variance relative to hidden/visible damping; two states suffice at $557/51920$ for the current target. | Common hidden law and initial conditional law; mean-only approximation. Multi-block averaging additionally requires an invariant partition. |
| What precision certifies the small target's state advantage? | [Rational recovery](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) gives ordinary minimum twelve at $2^{-220}$ on 12,766 experiments of at most 66 ticks; eleven unrestricted states suffice exactly. | Unrestricted minimum eleven remains proved only at $2^{-1360}$ on the earlier task. The new precision is still impractical. |
| How well can a smaller reversible model approximate that target? | [A nine-state symmetry quotient](SYMMETRY_AVERAGED_REVERSIBLE_COMPRESSION.md) has uniform two-field mean error at most $1/2376$, with the same hidden cap. | Sufficient upper only; no nine-state minimum or optimal error. The broad intervening precision range is unresolved. |
| Does the reversal convention change prediction state cost? | [The shared-cap comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) gives polynomial unrestricted/generalized-reversible and exponential ordinary-reversible growth on the same two-field task. | Ordinary and generalized reversal are different physical conventions; a device realizing the word involution is not supplied. |
| Does the exponential ordinary-reversibility penalty need the original kinetic rule or histogram? | [The capped kinetic theorem](CAPPED_KINETIC_INTERFACE_SEPARATION.md) allows arbitrary bounded endpoint barriers and no histogram matching, at hidden exit cap $3k$. | The shared equilibrium bias, zero-field normalization, field-independent hidden dynamics, preparation and readout remain fixed. |
| Can a tight-band target retain an ordinary-reversibility penalty without a rival rate cap? | [The broader interface theorem](GENERAL_KINETIC_INTERFACE.md) has polynomial unrestricted growth and ordinary lower $\exp(\exp(c[\log(1/\delta)]^{1/5}))$ on two fields. | The uncapped lower is weaker than the capped exponential law; interface bounds and ordinary reversal remain specified. |
| Does small identity-reversal entropy production imply nearby reversible prediction? | [The general endpoint bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) gives a uniform-in-time comparison from a common reset and bounded entrance density, and the [resource theorem](KINETIC_PARITY_RESOURCE_TRADEOFF.md) gives the stronger capped frontier without histogram matching. | Full comparator reversibility needs the common equilibrium ratio. No bound on complete long-path distance or universal driven heat follows. |
| Can accurate polynomial prediction have zero generalized entropy production? | [The centered-word predictor](GENERALIZED_REVERSAL_PREDICTION.md) does, while retaining an even actuator, target histogram and cap; finite identity-reversal entropy production is also possible. | The involution is explicit mathematically; its physical parity and device realization require separate justification. |
| What does the earlier binary uncapped construction establish? | [The tagged binary family](BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) has a polynomial unrestricted upper and reversible lower $\exp(\exp(c_H\sqrt{\log(1/\delta)}))$. | New target family with rare states and large fixed rate-to-gap ratio; arbitrary switching; exact unrestricted polynomial class uses the explicit union corollary. |
| What stronger error exponent does the earlier nineteen-level uncapped route establish? | [The uncapped nineteen-level theorem](UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) gives polynomial unrestricted cost and reversible cost at least $\exp(\exp(c_H\sqrt{\log(1/\delta)}))$. | Original rule and exact histogram; arbitrarily rapid switching; this earlier route does not supply the new fixed-clock conclusion. |
| How much of a fixed target is observable at a fixed clock? | [The Walsh hierarchy](UNCAPPED_WALSH_OBSERVABILITY.md) gives explicit rank thresholds up to $9\cdot2^{2^n}+2$ states, and a 38-state exact realization at $n=1$. | A fixed-target theorem against all Markov rivals, not a stronger worst-case reversibility comparison. |
| Can reversibility itself require exponentially more states with a binary actuator? | [The binary family](BINARY_REVERSIBILITY_LOWER_BOUND.md) has polynomial nonreversible and singly exponential reversible growth under the same internal exit budget $6580k$. | The original field rule, exact balanced histogram and fixed rival rate cap remain essential to the proved scope; the smaller numerical band and optimal exponents remain open. |
| Can every state-merging model be exponentially larger than a fresh reversible realization? | [The fixed six-level family](AGGREGATION_STATE_LOWER_BOUND.md) requires $\exp(c_a\delta^{-\gamma_a})$ cells under stationary-flux aggregation but admits a uniform polynomial reversible realization. | The lower concerns partitions refining the actuator with rates fixed by fluxes; it does not constrain arbitrary newly fitted reversible models. |
| Does polynomial reversible switching cost survive connected uniformly mixing local dynamics? | [Typical fixed labels on logarithmic-girth expanders](EXPANDER_SCENERY_LOWER_BOUND.md) have polynomial necessary and reversible sufficient growth in the same all-accuracy labeling class. | The class is a high-probability labeling event; arbitrary labelings and matching exponents remain open. |
| Is there a concrete local class with polynomial reversible switching cost? | [Binary path dynamics with stationary refresh](LOCAL_WALK_LOWER_BOUND.md) have polynomial necessary and sufficient state growth, retaining the original field rule and band. | The exponents are unmatched; the binary question in the tight band $[k,3k]$ remains open. |
| Can strong sparse transitions be kept without a density-moment bound? | [Whole-component selection](SPARSE_REVERSIBLE_COMPRESSION.md) gives $C\delta^{-(d+p_\Lambda)}$ for fixed-dimensional nearest-neighbor local networks. | Small-cost fragmentation is an additional structural condition, and the full generator may include global refresh. |
| Can all constant steps remain inexpensive while switching is hard? | [One common analytic reversible step predictor](ANALYTIC_CONSTANT_STEP_COMPRESSION.md) needs only $\Theta(\log(1/\delta))$ states in the same bounded binary class. | The original actuator rule and tolerance-independent derivative bounds are not imposed by this upper. |
| How large is the bounded binary-rate-band state requirement? | [Polynomial controlled-word lower](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) and [bounded-rate upper](BOUNDED_RATE_FINITE_FIELD.md): $c\delta^{-\gamma}\le D_*\le C\delta^{-p}$, hence $\delta^{-\Theta(1)}$. | The polynomial growth class is determined; the lower and upper exponents are not matched. |
| Does the obstruction survive a fixed control clock? | For every fixed $a>0$, two fields and segment lengths in $(a/k)\mathbb N$ retain polynomial necessity, with witnessing horizons $O_a(\log(1/\delta)/k)$. | The lower exponent depends on the clock spacing; no statistical sample bound is proved. |
| Can a bounded finite-alphabet predictor preserve reversibility and the spectral band? | Yes, with sufficient count $\exp[C\delta^{-p}\log(2/\delta)]$, retaining the exact actuator histogram. | The lower matches the exponential growth class for fixed nineteen-level and binary families, at different common rate budgets. |
| Is there a polynomial reversible sufficient condition for switching? | A [uniform positive density moment](MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) gives a polynomial count inside the original field-rule family, even with unbounded density spikes. | The moment assumption is stronger than a spectral cap; only the new internal cap $2\Lambda k$ is guaranteed. |
| Can arbitrary bounded actuators be approximated inside the original physical family? | [General reversible compression](REVERSIBLE_GENERAL_COMPRESSION.md): yes, with a double-exponential sufficient count and exact $G,W$. | No finite alphabet or rate cap is assumed here; its much larger bound is not a sharp complexity law. |
| How different can cubic and full controlled prediction be? | Along the shift-register sequence, exact cubic prediction needs $O(\log(1/\delta))$ states while full controlled prediction requires a positive power of $1/\delta$. | The cubic count uses analytic-in-field competitors; the full controlled lower bound allows a broader class. |
| Can any fixed response order give complete intervention information? | [Fixed-actuator hierarchy](FIXED_ACTUATOR_HIERARCHY.md): arbitrarily many mean and path response orders can agree with the actuator fixed between models. | The separating signal may shrink; this theorem alone supplies no finite-error state lower bound. |
| What information is complete for driven visible paths? | [Actuator-process equivalence](ACTUATOR_PROCESS.md): the stationary law of $g(X_t)$, with a matrix-return closure for finite actuator rank. | No stable noisy recovery or mean-only necessity is established. |

The bounds are asymptotic at fixed physical parameters, and the upper exponent $p$ depends on the actuator alphabet, rate cap and field bound. The notation $\delta^{-\Theta(1)}$ records fixed positive lower and upper exponents, not their equality. A sharp rank-one theorem and the broader cubic results remain resolved foundations; they do not impose their logarithmic state laws on the general controlled problem.

The leading publication question is how the physical reversal assigned to a reduced representation changes the memory needed for accurate controlled prediction. The present results separate ordinary and generalized reversibility on the same target and task, while extending the ordinary state and entropy-production lower bounds beyond a prescribed exponential kinetic curve. The positive results also identify a limit: generalized equilibrium can coexist with polynomial prediction, so a generic dissipation narrative is excluded. The passive/step/switching comparison and other positive compression routes remain supporting results with their own assumptions.

The next work should sharpen the finite ordinary-versus-unrestricted certificate to a useful tolerance and test a microscopic realization of the force-controlled model. The new 12-versus-11 example resolves finite existence but does not give an eleven-state generalized-reversible predictor; the address-and-table asymptotic theorem remains separate. A target's rank threshold alone does not establish a reversible-versus-irreversible state gap. Narrowing the inverse-polylogarithmic necessary and logarithmic sufficient identity-reversal entropy budgets remains useful when identity reversal is physically appropriate. A stronger uncapped ordinary lower, a tight-band binary realization and matching frontiers remain separate open questions.

The constructor receives a known target. Observation results concern specified-model tests with the stated preparation and readout. Continue with bounded analytic work and small exact checks. PRL is the user's selected target, while complete-theorem novelty, natural physical relevance and the journal's significance threshold remain matters for further assessment. Manuscript writing remains the final step.
