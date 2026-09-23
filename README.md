# Intervention Reuse Limits

**When does a perfect passive model remain useful after an intervention?**

This theory-first project studies finite-state stochastic dynamics. A system can have an exact two-state description when left alone, while hidden kinetic modes become visible in its nonlinear response. The objective is to characterize what a reusable model must retain, and how that requirement changes when exact equality is replaced by a specified accuracy.

**Research target: Physical Review Letters.** The [current exploration](docs/PRL_EXPLORATION.md) asks how the time-reversal convention changes the state cost of a reusable stochastic model. On the same equilibrium target family and two-field prediction task, unrestricted and generalized-reversible predictors have polynomial state cost, while ordinary detailed balance has exponential cost under a common hidden exit budget.

The [new comparison](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) allows arbitrary bounded kinetic barrier functions and imposes no rival actuator alphabet or histogram. A [centered memory-word construction](docs/GENERALIZED_REVERSAL_PREDICTION.md) supplies the small generalized-reversible predictor. Its stationary entropy production is zero under word reversal, though it can be positive under identity reversal. **The ordinary-reversal lower is therefore not a universal thermodynamic dissipation or heat requirement.** A physical interpretation must specify how the retained variables transform under time reversal.

**Research package for eventual drafting:** start with the [research dossier](docs/RESEARCH_DOSSIER.md) for the model, quantifiers, assumptions and dependencies. The [claim ledger](docs/CLAIM_LEDGER.md) maps results to proofs, finite checks and source comparisons. [Verification](docs/VERIFICATION.md) records reproducibility. Manuscript drafting remains the final step.

## The reversal convention changes prediction state cost

The target is the original nineteen-level family with hidden relaxation band $[k,3k]$ and an exact two-state passive visible law. Rivals may create arbitrary new states and choose state-specific barrier functions in

$$
q_{iA}(h)=k b_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),\qquad b_i(0)=1.
$$

Only the two fields $0,H$ are needed, with any fixed positive control clock. The [capped theorem](docs/CAPPED_KINETIC_INTERFACE_SEPARATION.md) fixes the same hidden exit budget $3k$ in all classes and a finite interval for the queried return rates. The hidden generator is field independent; preparation is $(1/2,\mu/2)$ and readout is binary. There is no rival histogram or finite-alphabet promise.

| Predictor requirement | Worst-case total state count |
|---|---|
| Stationarity | $\delta^{-\Theta(1)}$ |
| Generalized reversal $K^*=\Theta K\Theta$, with an invariant actuator | $\delta^{-\Theta(1)}$ |
| Ordinary detailed balance $K^*=K$ | $\exp(\delta^{-\Theta(1)})$ |

The exponents are unmatched. These are the same target family, accuracy norm, two fields and common rate budget. The bounds count every retained memory state, but do not charge parameter precision, sample cost or construction time. Finite witnesses have horizons logarithmic in inverse error.

The ordinary lower uses nonnegative squared-Lagrange selectors and a positive uniformized hidden kernel. They recover exact target gates while staying positive on rivals with arbitrary endpoint barrier values. Finite clock observations control the required moments, and weighted transport repair forces many rival states. A separate target-only rank argument establishes polynomial necessity on the same two fields without a rival rate cap.

The generalized upper reverses an odd-length memory word and reads its middle symbol. The actuator is unchanged by this reversal. Stationary index-shift invariance gives exactly the same actuator-path law, hence exactly the same controlled response, as the established polynomial word predictor. This is a counted Markov realization; the reversal is not an extra supplied control. A natural mechanical implementation of its parity has not been supplied.

## Entropy-production consequences and their physical boundary

For a general hub interface, hidden-to-visible rates bounded below and entrance rates dominated by the hidden stationary law are enough for a [uniform endpoint comparison](docs/GENERAL_INTERFACE_ENTROPY_BOUND.md). With dimensionless bounds $b_i(h)\ge b_-$ and $e^{2h}b_i(h)\le c_+$, additive reversibilization preserves states and exits and gives

$$
\mathcal D_H(F,F_{\rm sym})
\le\sqrt{\frac{c_+}{b_-^2}\frac{\sigma_0^{\rm id}}k},\qquad
D_{\le\Sigma}^{\rm id}(\delta)\ge
D_{\rm id}\!\left(\delta+\sqrt{\frac{c_+}{b_-^2}\frac\Sigma k}\right).
$$

Here $\sigma_0^{\rm id}$ is stationary zero-field entropy production under identity reversal. The constant has no hidden rate, dimension or minimum-mass factor. A common local-balance ratio is additionally needed to make the full comparator reversible. The [resource theorem](docs/KINETIC_PARITY_RESOURCE_TRADEOFF.md) now gives the stronger capped frontier without histogram matching or prescribed exponential barriers.

Polynomial predictors can have finite identity-reversal entropy production and exactly zero entropy production under their generalized reversal. Thus the identity-reversal frontier remains meaningful for physically even retained configurations, but cannot be interpreted as an implementation-independent dissipation cost. It is also distinct from total entropy production during a driven protocol.

Without a common rival rate cap, the [general kinetic-interface theorem](docs/GENERAL_KINETIC_INTERFACE.md) retains polynomial unrestricted growth on two fields and the weaker ordinary lower $\exp(\exp(c[\log(1/\delta)]^{1/5}))$. The same target band is retained. Stronger uncapped growth, a small certified finite-accuracy advantage, and a separation in a recognizable physical model class remain open.

The [internal review](docs/KINETIC_PARITY_INTERNAL_REVIEW.md), [bounded verifier](scripts/verify_kinetic_parity.py), [report](reports/kinetic_parity.json) and [primary-source comparison](docs/KINETIC_PARITY_SOURCE_AUDIT.md) record distinct evidence. Word reversal, kinetic-barrier freedom and generalized balance have established antecedents; the complete controlled-prediction comparison is the claim under investigation. The historical results below retain their original scope.

## Earlier binary result: two physical fields at a fixed clock

Fix any $a>0$. The [new theorem](docs/FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) uses only held segments in $(a/k)\mathbb N$ and observations at clock endpoints. On its precisely defined rescaled binary tagged family,

$$
D_{\rm all}^{a,\{0,H\}}(\delta)\le C\delta^{-p},\qquad
D_{\rm rev}^{a,\{0,H\}}(\delta)\ge
\exp\!\left(\exp\!\left(c_a[\log(1/\delta)]^{1/12}\right)\right).
$$

The lower permits arbitrary new reversible states, arbitrary finite internal rates and no rival lower gap. At target index $n$, accuracy $e^{-C_a(n+1)^{12}}$ forces at least $2^{3\cdot2^n/4}$ states; a finite collection of mean experiments with at most $C_a(n+1)^{12}$ clock ticks witnesses the bound. Constants can be very large. This is not a bound on the number of experiments, parameter precision or sample cost. A polynomial unrestricted lower is not asserted for this two-field tagged-family task.

[Fixed-clock Gram recovery](docs/FIXED_CLOCK_GRAM_OBSERVABILITY.md) controls vector-specific resolvent errors using the target cap. [Positive resolvent calculus](docs/FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) then isolates hidden killing and binary label operations. Their exact counterparts remain positive on every rival; signed clock polynomials are used only to recover scalar tests. The existing weighted repair and entropy argument applies on the rival's own states. [Internal reviews](docs/FIXED_CLOCK_INTERNAL_REVIEW.md) and a [primary-source comparison](docs/FIXED_CLOCK_PRIOR_ART.md) record the evidence and its limits.

## Two actuator values suffice without a rival rate cap

For the new tagged binary target family, the [uncapped theorem](docs/BINARY_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) proves

$$
D_{\rm all}^{\rm tag,unc}(\delta)\le C\delta^{-p},\qquad
D_{\rm rev}^{\rm tag,unc}(\delta)\ge
\exp\!\left(\exp\!\left(c_H\sqrt{\log(1/\delta)}\right)\right).
$$

These are state counts for actual controlled means at all horizons, with exactly balanced sensitivities $\pm\gamma$. No rate cap or lower gap is imposed on rivals. Targets have a uniform positive gap and fixed exit cap; the explicit construction has a very large rate-to-gap ratio. The exact uncapped reversible growth law remains unmatched. The theorem's explicit union with the earlier binary family additionally gives $D_{\rm all}=\delta^{-\Theta(1)}$; a matching unrestricted lower is not asserted for the tagged family alone.

The logical core has one actuator value. Rare private states of the other value give each hidden port a distinct decay signature. A distant balancing state keeps the histogram exact while suppressing unwanted filter paths. Positive bounded observation words then recover the ports accurately enough for entropy to force many states on any reversible rival. All tags, corridor vertices and logical coordinates are counted. The [source comparison](docs/BINARY_OBSERVATION_PRIOR_ART.md) distinguishes this controlled-mean argument from classical binary hidden-state identification and generally non-Markovian dwell-time reductions.

The lower uses arbitrarily rapid switching among five fields. It does not retain the earlier binary budget $6580k$ or the nineteen-level band $[k,3k]$, and it supplies no finite schedule or sample-complexity guarantee. The [word-obstruction audit](docs/BINARY_UNCAPPED_RESEARCH_BOUNDARY.md) explains why literal palindromic replacements fail while other positive binary words can work.

## A reversibility penalty survives arbitrarily fast hidden rates

For the same nineteen-level targets used below, the [uncapped theorem](docs/UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) proves

$$
D_{\rm all}^{\rm unc}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{\rm unc}(\delta)\ge
\exp\!\left(\exp\!\left(c_H\sqrt{\log(1/\delta)}\right)\right).
$$

These are worst-case minimal total state counts in the actual all-protocol, all-horizon mean norm. Both classes retain the original exponential field rule, exact histogram, stationary zero-field preparation and binary readout. Neither has a rival rate cap or required lower gap. Targets retain the band $[k,3k]$; the existing reversible upper remains singly exponential in a power of inverse error, so the uncapped growth class is not matched.

Rapid switching among the fixed field values first exposes a full-dimensional set of external coefficients. A single analytic continuation for an entire protocol, followed by exponential averaging of segment lengths, recovers ordered words in bounded positive resolvents. On the target, these approximate the address and bit-flip gates. On arbitrary reversible rival states, whole-word repair and entropy force the state lower. The [primary-source comparison](docs/BOUNDED_WORD_RECOVERY_PRIOR_ART.md) separates established product formulas, analytic continuation and realization tools from this combined quantitative argument.

The theorem requires arbitrarily fast switching; it supplies no uniform finite schedule or witnessing-horizon bound over all rivals. The fixed-clock results below keep their separate rate assumptions. Artificial negative coefficients appear only in the analytic proof and do not enlarge the physical control menu.

## A binary actuator already forces the reversibility penalty

The [binary theorem](docs/BINARY_REVERSIBILITY_LOWER_BOUND.md) uses only the sensitivities $\pm\gamma$, each with stationary mass $1/2$, for any fixed $0<\gamma<1$. Every target still has an exact two-state passive visible law. At the common internal exit budget $Bk$, with the explicit fixed constant $B=6580$,

$$
D_{\rm all}^{(B)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{(B)}(\delta)=\exp\!\left(\delta^{-\Theta(1)}\right).
$$

These are worst-case minimal total state counts on the same target family. Error concerns actual means under every bounded protocol and every horizon. Both predictor classes preserve the original exponential field rule, exact balanced histogram, stationary zero-field preparation and binary readout. Only the second additionally requires ordinary reversibility. The lower bounds already use five fixed field amplitudes, with all segment lengths integer multiples of any fixed positive clock and witnessing horizons logarithmic in inverse error.

Short binary color sequences identify a root set and four gates that query and independently flip the entries of a hidden bit table. In a rival, the same positive observation words can have very different supports. Normalizing their positive root vector gives a probability law on the rival's own states; a transport-repair estimate then supplies stationary couplings without adding states or requiring a minimum coordinate mass. The decoded table has large entropy, forcing exponentially many physical states. A separate rank argument gives polynomial necessity without reversibility, and a stationary word-chain construction supplies polynomial sufficiency.

The explicit targets and reversible upper models retain the internal band $[k,13160k]$, as well as the common exit budget $6580k$. The reversible lower imposes no lower gap on rivals. The band constants are conservative: this proof does not establish the binary separation with the earlier target band $[k,3k]$. An uncapped lower on this same budget-$6580k$ target family and arbitrary reversible field rules remain open; the new tagged family above establishes uncapped binary existence. The exponents are unmatched; state count does not measure numerical precision or experimental sample cost. The [source comparison](docs/PRIOR_ART.md) distinguishes the classical coding, Doob-transform, transport-rounding and entropy ingredients from their quantitative use here.

## Nineteen values give a smaller rate budget

The [dynamic-lamp theorem](docs/DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) compares predictors on one uniformly mixing target family. Each target has the exact two-state passive visible law, hidden relaxation band $[k,3k]$, and fixed sensitivity histogram

$$
\mu(g=0)=\frac12,\qquad
\mu(g=\pm j/100)=\frac1{36},\quad j=1,\ldots,9.
$$

Both predictor classes retain this histogram, the original exponential field rule, stationary zero-field preparation, binary readout, and an internal outgoing-rate budget of $3k$ at every state. Both may construct new states. Only the second class additionally requires ordinary detailed balance. Their worst-case total state counts satisfy

$$
\begin{aligned}
c_0\delta^{-\gamma}&\le D_{\rm all}^{(3)}(\delta)\le C_0\delta^{-p},\\
\exp(c_1\delta^{-\alpha})&\le D_{\rm rev}^{(3)}(\delta)
\le\exp\!\left(C_1\delta^{-p}\log\frac2\delta\right),
\qquad \alpha,\gamma,p>0.
\end{aligned}
$$

Error concerns actual controlled means under every bounded deterministic protocol and at every horizon. Both lower bounds already hold with thirty-nine fixed field values and any fixed positive control clock, with witnessing horizons logarithmic in inverse error. The reversible upper retains the target band $[k,3k]$. The reversible lower also holds under any fixed rival spectral cap, without requiring a lower gap.

The target contains a complete bit table and an address register. Short gate words query every entry and flip any one queried bit. Accurate reversible rivals expose positive transports between actuator levels. Their forward and reverse row moments allow these transports to be repaired into stationary Markov couplings on the rival's own states. The couplings force a deterministically decoded table distribution to be approximately invariant under every individual bit flip. Its entropy is proportional to the table size, requiring exponentially many rival states. A stationary word-chain construction supplies the polynomial nonreversible alternative.

This is a finite-error theorem under the stated field rule, histogram and rate budget. The binary construction above uses a larger fixed budget; the nineteen-value construction retains the sharper band. The stronger uncapped law $\exp(c\delta^{-\alpha})$ and reversible rivals with arbitrary field dependence remain open. The [source comparison](docs/PRIOR_ART.md) attributes the established lamp/Følner and entropy ingredients; the candidate contribution is their quantitative connection to arbitrary reversible prediction of physical controlled means.

Two supporting results sharpen the earlier architecture analysis. [Soft aggregation](docs/SOFT_AGGREGATION_LOWER_BOUND.md) still has exponential cost when the color-preserving encoder is stochastic and overlaps target states. Separately, [exact reversible prefix matching](docs/EXACT_REVERSIBLE_PREFIX_OBSTRUCTION.md) can require unboundedly many states with five colors and a fixed fifteen-symbol prefix. The latter is a zero-error result, distinct from the positive-error dynamic-lamp theorem.

## Merging existing states can also have an exponential cost

The [aggregation lower theorem](docs/AGGREGATION_STATE_LOWER_BOUND.md) and [register-scenery upper theorem](docs/REGISTER_SCENERY_COMPRESSION.md) compare two ways to build a reversible predictor for the same targets and the same actual controlled-mean error. Fix the six sensitivities $\{\pm1/10,\pm2/10,\pm3/10\}$, each of stationary mass $1/6$, and the internal band $[3k/2,5k/2]$.

A partition aggregate keeps $A$ separate, groups only states with the same sensitivity, and obtains its rates by summing stationary transition fluxes. In operator form this is $EKE$, where $E$ is conditional expectation onto the partition. The other architecture may construct new physical states and rates, while retaining the same reversible field-rule family, histogram and advertised band. Over one common target family,

$$
c_a\delta^{-\alpha_a}\le D_*(\delta)
\le D_{\rm fresh,rev}(\delta)\le C\delta^{-p},
\qquad
p=\frac{\log96}{\beta},\quad
\beta=\log(1+2/[5e^{(13/10)H}]).
$$

For the partition architecture,

$$
\exp(c_a\delta^{-\gamma_a})\le D_{\rm agg}(\delta)
\le\exp\!\left[C\delta^{-(\log6)/\beta}\log(2/\delta)\right].
$$

Here $D_*$ allows arbitrary finite Markov predictors. Thus fresh-state prediction has polynomial growth, and aggregation has singly exponential growth in a positive power of inverse accuracy; the exponents are unmatched. Both lower bounds survive any fixed positive control clock. The aggregation lower holds for every partition in the stated architecture. It is a cost of this form of state merging; ordinary reversibility is retained by the polynomial-size alternative. Arbitrarily fitting new rates on partition cells is outside the aggregation lower.

A target contains a binary address register, three routing ports, a sign coordinate and a complete table of independent bits. All coordinates are counted: width $n$ gives $1+6\cdot2^n2^{2^n}$ physical states. Short control words act as permutations that query any table bit. If an aggregate predicts their visible-mean tests accurately, a norm-loss identity forces its cells to retain most of the table's independent bits. An entropy bound then requires exponentially many cells. The new-state construction instead replaces a wide register's short trajectory statistics by those on a smaller register and selects complete configurations with positive weights. This gives the polynomial upper uniformly over every width and every accuracy.

The qualitative distinction between aggregation and realization is established prior work. The candidate contribution is the robust quantitative gap under these shared physical constraints; see the [source comparison](docs/PRIOR_ART.md). This six-level theorem is separate from the intrinsic reversibility results above and the binary-label expander result below. Compression for every fixed expander labeling remains a separate open question.

## Binary targets: controlled prediction has a larger state cost

For the binary target class below, the experiment menu changes the worst-case physical state requirement:

| Prediction task | State cost |
|---|---|
| Complete passive visible path law | Exactly $2$ |
| All constant amplitudes $|h|\le H$, all times, one common predictor | $\Theta(\log(1/\delta))$ |
| Switching protocols, including any fixed control clock | $\delta^{-\Theta(1)}$ |

The [analytic constant-step theorem](docs/ANALYTIC_CONSTANT_STEP_COMPRESSION.md) is an actual-mean result, not a small-field expansion. Its one common predictor retains ordinary reversibility, irreducibility, stationary zero-field preparation, the exact passive path law and equilibrium mean, a uniform full-generator spectral band, and the universal linear and zero quadratic mean responses. All rate functions are real analytic. They need not follow the target's specified exponential rate rule, and their derivatives and description complexity are not bounded uniformly in tolerance. Thus the separation does not rely on discontinuous field dependence. The [earlier construction](docs/CONSTANT_STEP_COMPRESSION.md) remains the source of the matching logarithmic lower; neither step upper supplies a switching guarantee.

**Connected sparse dynamics can mix rapidly and still require polynomial controlled memory.** The [expander lower theorem](docs/EXPANDER_SCENERY_LOWER_BOUND.md) uses one fixed binary labeling $x_v$ of a four-regular graph, with hidden states $(v,\sigma)$ and sensitivity $\sqrt W\,\sigma x_v$. The sign $\sigma\in\{-1,+1\}$ is a counted, dynamically flipping state coordinate that makes the histogram exactly balanced. Local motion and sign flips give a connected degree-five local graph with a size-independent spectral gap. The supplied global refresh retains the full internal band $[3k/2,5k/2]$. There are only $2N+1$ total physical states for an $N$-vertex base graph.

For each fixed base graph with girth at least $a_g\log N$, [the new upper](docs/EXPANDER_SCENERY_COMPRESSION.md) identifies an event of iid fair labelings with probability at least $1-\eta$, independent of the requested accuracy. Every labeling in this event has a polynomial reversible predictor for every accuracy, retaining the original field rule, exact actuator histogram and advertised band. The good event contains fixed-clock polynomial lower witnesses on a concrete expander family. Thus, over this precisely specified good-label class,

$$
c_a\delta^{-\gamma_a}\le D_*^{\rm exp}(\delta)
\le D_{\rm rev}^{\rm exp}(\delta)\le C\delta^{-p_g},\qquad
p_g=\frac{\log2+\max\{2/a_g,8\log3\}}
{\log(1+2/[5e^{(1+\sqrt W)H}])}.
$$

Short local walks see the same regular-tree geometry, allowing a small replacement graph and a weighted selection of complete labeling copies to reproduce their prefix laws. A single concentration event controls the fixed target labeling at every prefix length. This avoids cutting the original expander into small pieces: its local gap proves that such fragmentation has a nonvanishing cost. Density moments also diverge. The statement is probabilistic over labels on each graph; it is not asserted for every fixed labeling or every capped graph. Constant steps retain the general $O(\log(1/\delta))$ analytic upper; a matching logarithmic lower has not been proved specifically for this new good-label subclass.

**The separation already occurs with local motion on a line.** The [local-walk theorem](docs/LOCAL_WALK_LOWER_BOUND.md) uses a hidden position moving between neighboring sites of a finite path. Each site carries a binary label, and the actuator reads the label at the current position. A stationary refresh occasionally redraws both the position and the full label string. All label strings are part of the finite Markov state space and are counted. The observed output still records only whether the system is in the hidden block or the visible state $A$.

For the class with binary actuator, local path components, refresh rate $3k/2$, and internal spectral cap $5k/2$, let $D_*^{\rm path}$ allow arbitrary Markov predictors and let $D_{\rm rev}^{\rm path}$ require reversible predictors in the original rate-rule family. The new lower and [sparse reversible upper](docs/SPARSE_REVERSIBLE_COMPRESSION.md) give

$$
c_a\delta^{-\gamma_a}\le D_*^{\rm path}(\delta)
\le D_{\rm rev}^{\rm path}(\delta)
\le C\delta^{-(1+p_{5/2})},\qquad
p_{5/2}=\frac{\log2}{\log(1+1/[(5/2)R_s])},\quad
R_s=e^{(1+\sqrt W)H}.
$$

The reversible upper retains the exact actuator histogram and band $[3k/2,5k/2]$ for every protocol and horizon. Thus both predictor classes have polynomial growth, although their optimal exponents may differ. The same target class has logarithmic constant-step cost. Along the switching witnesses, exact cubic response needs only $4n+5$ states while full controlled prediction needs at least $2^n$ below an error exponentially small in $n$.

The upper keeps strong transitions inside small path components and selects a weighted collection of whole components that matches finite actuator-word probabilities. It works despite diverging density moments. More generally, nearest-neighbor local networks in a fixed dimension $d$, with optional stationary refresh and internal cap $\Lambda k$, have a reversible sufficient count $C\delta^{-(d+p_\Lambda)}$. The proof requires a small stationary jump cost for cutting into small components; a spectral cap alone does not provide that condition.

**The broader bounded binary class.** Consider reversible targets whose sensitivity is $g=\pm\sqrt W$ and whose nonzero internal relaxation rates lie in $[k,3k]$. Every target has the exact same two-state passive binary path law. One predictor must approximate the actual binary mean under every protocol $|h(t)|\le H$ and at every observation time, starting from zero-field equilibrium.

Let $D_*^{\rm bin}(\delta)$ be the worst-case necessary state count over this target class, allowing arbitrary instantaneous-field Markov predictors with a fixed readout and preparation. The [polynomial controlled-word lower theorem](docs/POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) and [bounded-rate upper theorem](docs/BOUNDED_RATE_FINITE_FIELD.md) give, for sufficiently small $\delta$,

$$
\boxed{c\delta^{-\gamma}
\le D_*^{\rm bin}(\delta)\le C\delta^{-p},
\qquad \gamma,p>0.}
$$

Here the constants depend only on the fixed physical parameters. A sufficient exponent is

$$
p=\frac{\log2}{\log(1+1/(3R_s))},\qquad
R_s=e^{(1+\sqrt W)H}.
$$

Thus $D_*^{\rm bin}(\delta)=\delta^{-\Theta(1)}$ describes the polynomial growth class, with fixed positive lower and upper exponents; it does not claim a matched exponent or an exact power law. The upper predictor preserves the entire stationary actuator distribution and all passive/static/low-order agreements, but its internal dynamics may be nonreversible.

**A fixed control clock is enough.** For any fixed $a>0$, the polynomial lower bound already holds using only fields $0$ and one fixed $h_*>0$, with every held segment an integer multiple of $a/k$:

$$
D_{*,a}^{\mathrm{bin}}(\delta)\ge c_a\delta^{-\gamma_a},
\qquad \gamma_a>0.
$$

The witnessing experiments have horizons $O_a(\log(1/\delta)/k)$, and target rates remain in $[3k/2,5k/2]$. Finite clock resolution therefore does not remove the polynomial obstruction. The proof uses signed combinations of actual mean measurements; no statistical sample bound is proved here. It strengthens the [earlier shift-register interpolation bounds](docs/SHIFT_REGISTER_LOWER_BOUND.md) without changing the physical target.

**Reversibility can be retained.** For any fixed finite actuator alphabet and internal rate cap, a [reversible predictor](docs/BOUNDED_RATE_FINITE_FIELD.md#7-a-reversible-surrogate-preserving-the-spectral-cap) preserves the exact actuator histogram and the entire specified spectral band, with sufficient count

$$
D_{\rm rev}(\delta)\le
\exp\!\left[C\delta^{-p}\log(2/\delta)\right].
$$

Here $p$ depends on the alphabet, rate cap and field bound; for the binary band above it is the displayed exponent. These upper bounds alone do not establish an additional optimal cost. The dynamic-lamp and binary theorems supply exponential reversible lowers under common outgoing-rate budgets. Polynomial reversible size therefore does not always suffice, even for a balanced binary actuator; the binary construction uses a larger fixed cap than the earlier band.

**A sufficient condition for polynomial reversible compression.** If, additionally, $K_{ij}/\mu_j\le Lk$ for every distinct pair of hidden states, a [stratified sampling construction](docs/BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) gives

$$
D_{\rm rev}(\delta)\le C\delta^{-2(1+p_L)}\log^3(2/\delta),
\qquad p_L=\frac{\log m}{\log(1+1/(LR))}.
$$

It uses the original field rule, preserves the exact actuator histogram and all prescribed passive/static/low-order agreements, and works under every bounded protocol at every horizon. Its internal spectrum is capped by $2Lk$; it need not preserve the original spectral band. The additional density bound controls each transition rate relative to the destination's stationary mass. A spectral cap alone does not give that bound, and the shift-register lower targets violate it uniformly as their size grows.

**Individual density spikes are allowed.** The [density-moment extension](docs/MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) replaces the pointwise bound by

$$
\sum_{i,j}\mu_i\mu_j q_{ij}^{1+a}\le M,\qquad
q_{ij}=\frac{K_{ij}}{k\mu_j}\ (i\ne j),\quad q_{ii}=0,
$$

for fixed $a>0,M<\infty$, together with the internal cap $\Lambda k$. It gives

$$
D_{\rm rev}(\delta)\le C\delta^{-[2(1+p_\Lambda)+1/a]}\log^3(2/\delta),
\qquad p_\Lambda=\frac{\log m}{\log(1+1/(\Lambda R))}.
$$

The predictor preserves the original field rule and exact actuator histogram, with internal cap $2\Lambda k$. The moment condition remains substantive. An exactly three-state-compressible matching example shows that simply clipping large density values can lose a finite driven signal under a spectral cap alone. This is a failure of that approximation method, not a reversibility penalty.

Without a common bound on actuator-alphabet size or internal rates, the [general reversible upper theorem](docs/REVERSIBLE_GENERAL_COMPRESSION.md) still gives

$$
D(\delta)\le\exp\!\left\{\exp\!\left[C_{G,H}\log^2(16/\delta)\right]\right\},
$$

preserving reversibility, the sensitivity bound, exact variance $W$, and every prescribed passive/static/low-order agreement. This much larger bound concerns the broader target class. All upper constructions assume the microscopic model is supplied; state count does not measure learning cost, parameter precision, or runtime.

The candidate contribution is the polynomial controlled-word obstruction for positive physical Markov models with an exactly simple passive law, including the fixed-clock guarantee. The de Bruijn/Walsh shift mechanism, logarithm expansions, interpolation formulas, Markov word approximation, and rank arguments are established ingredients; [the comparison](docs/PRIOR_ART.md) distinguishes them from the physical construction and error guarantees here.

## A sharp subclass and operational results

**Actual finite-field prediction.** In a specified subclass, exactly one hidden state has sensitivity $+\sqrt W$ and stationary mass $1/2$; all other hidden states have sensitivity $-\sqrt W$. Every finite positive relaxation kernel has such a reversible realization. For any fixed field bound $H>0$, one reduced Markov model must predict the actual binary mean under every protocol $|h(t)|\le H$, at every time. The sharp worst-case state orders are

| Target spectrum | States for exact-mean error at most $\delta$ |
|---|---|
| Unrestricted active rates | $\Theta(\log^2(1/\delta))$ |
| Active rates at most $3k$ | $\Theta(\log(1/\delta))$ |

The upper construction preserves reversibility, bounded sensitivity, and the entire passive law. The lower bound allows arbitrary finite-state Markov competitors, with no analytic field dependence or passive matching requirement. In the unrestricted case, a **single fixed nonzero step amplitude**, independent of tolerance and state budget, already forces the lower order. See [the finite-field theorem](docs/FINITE_FIELD.md) and [the fixed-step proof](docs/FIXED_FIELD_LOWER_BOUND.md). The guarantee has no Taylor-remainder floor. The actuator restriction is substantive: outside it, identical cubic kernels can give different higher-order responses.

**Two measurements can reveal what the mean misses.** In the broader original family, the complete passive path law and every first-order visible-path response agree with a two-state reference. The second-order path response determines the hidden kernel and can require arbitrarily many states. For a concrete pair of three-state models, retaining the initial and final visible states needs $\Theta(h^{-4})$ independent weak-step trials to distinguish them; retaining only the final state needs $\Theta(h^{-6})$. These are [specified two-hypothesis experiments](docs/ACTIVE_PATH_RESPONSE.md), with no hidden-state access or continuous monitoring required for the stronger exponent.

**Imperfect lumpability has a quantitative information cost.** Small centered changes of the external equilibrium conductances, of relative size $q$, break exact passive lumpability. Nevertheless, the full stationary passive-path relative entropy from the two-state reference is bounded by $q^4(152+241kT)$, independently of hidden dimension and internal rates. A three-state pair attains the quartic information scale while retaining a nonzero finite-field driven signal. The [robustness theorem](docs/NEAR_LUMPABILITY.md) specifies the allowed barrier perturbations and the observation/preparation costs.

## Beyond the scalar-kernel subclass

**No finite response hierarchy is universally complete, even with the actuator fixed.** For every $d\ge2$, two $d+2$-state models can share the same state labels, $k,\mu,g$, field-dependent external rates, and one-mode kernel $C(t)=We^{-\lambda t}$. Changing only reversible hidden kinetics leaves every bounded-protocol mean coefficient through order $2d$ identical, and every visible-path coefficient through order $2d-1$ identical. The next orders differ, and their actual mean curves differ under every nonzero constant field. All hidden relaxation rates stay in $[\lambda,3\lambda/2]$. The [fixed-actuator hierarchy theorem](docs/FIXED_ACTUATOR_HIERARCHY.md) holds for any fixed $0<W<G^2$; the common actuator and state space may change with $d$. This is exact incompleteness, not a noise-robust separation or a finite-error state lower bound.

**The complete path information has an exact description.** For the general family, equality of all controlled visible path laws is equivalent to equality in law of the stationary hidden sensitivity process $Y_t=g(X_t)$. Short-pulse no-exit functionals recover its joint Laplace transforms in principle. The [actuator-process theorem](docs/ACTUATOR_PROCESS.md) also gives a matrix-return closure for finitely many distinguished actuator states. Two sensitivity levels alone are insufficient for two-time closure: an explicit pair has identical two-time level kernels but different finite-field means. Necessity from mean data alone is not established.

**Reversibility and exact variance can be retained.** The [general reversible construction](docs/REVERSIBLE_GENERAL_COMPRESSION.md) partitions the target using finitely many prediction functions, averages reversible transitions, and uses at most two sensitivity replicas per cell to restore the original variance. A truncated controlled expansion improves its sufficient count to the double-exponential bound above. The [earlier finite-word construction](docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md) remains as a preliminary existence proof and source of shared estimates; its nonreversibility and variance error are no longer limitations of the best available upper theorem.

These results separate three questions: which intervention data are complete, whether fixed-accuracy compression exists, and how many physical states it optimally costs. A finite response hierarchy can fail the first question without making the second impossible.

## Cubic-response foundations

**Exact separation.** For every $N\ge3$, a reversible $N$-state model has exactly the same complete passive binary path law, static response curve, and dynamic linear mean response as a two-state reference, but its exact cubic step response requires at least $N$ states in an analytic autonomous Markov surrogate. The separation can be maintained with bounded field coupling and a nonvanishing total cubic correction.

The [earlier binary-tree construction](docs/GENERAL_CONTROLLED_LOWER_BOUND.md) further separates two intervention tasks within one family:

$$
D_{\mathrm{cubic}}=n+3,\qquad
2^n\le D_{\mathrm{full\ controlled}}\le2^{n+1}+1.
$$

The cubic minimum uses analytic-in-field Markov competitors, while the full controlled lower bound permits broader competitors. The newer shift-register construction and whole-word logarithm truncation strengthen the finite-error bound to polynomial growth in inverse error. The earlier exact task comparison remains a foundation.

**Finite-accuracy reuse.** Within the constructed family, a scalar kinetic kernel determines the cubic mean response to every bounded weak-field protocol. For kernel mass $W$, protocol bound $U$, and any positive integer $n$, a positive-quadrature construction and reversible realization give a surrogate with at most $2n(n+1)+3$ states and cubic-coefficient error

$$
\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|\le8U^3W\,16^{-n}
$$

for every finite horizon and every admissible protocol, independently of the original state count and hidden spectral range. Thus a tolerance $\varepsilon$ needs at most order $\log^2(1/\varepsilon)$ states at fixed $W,U$. The earlier $U^3W/q$ midpoint certificate remains available. Classical quadrature supplies the upper bound; the lower bound below establishes its worst-case state-growth order, without claiming sharp constants or new approximation theory.

**Exact realization of a known kernel.** A kernel with $r$ distinct positive exponential modes has an explicit reversible realization with $r+2$ total states and sensitivity magnitude $\sqrt W$. When no hidden decay rate equals $k$, this meets the exact pole-location lower bound. The construction is a corollary of finite Jacobi inverse spectral theory.

**Finite-accuracy lower bounds.** Two cubic step-response samples of a three-state target force error at least $0.062546\,WU^3$ against every admissible two-state surrogate. For arbitrary state budgets, geometrically separated hidden rates give a matching obstruction through a weighted Hankel operator of the cubic step response. The proof allows nonreversible surrogates and unrestricted field derivatives. Combined with the upper bounds:

| Target information, at fixed positive $W,U$ | Necessary states | Sufficient states |
|---|---|---|
| No common bound on active hidden rates | $\Omega(\log^2(1/\varepsilon))$ | $O(\log^2(1/\varepsilon))$ |
| Active hidden rates at most $3k$ | $\Omega(\log(1/\varepsilon))$ | $O(\log(1/\varepsilon))$ |

The second row adds information about the target; it leaves the broad surrogate class unchanged and assumes no lower bound on the hidden spectral gap. These are asymptotic coefficient-tolerance results, with conservative constants. The unrestricted lower bound already holds for targets whose slowest active rate is $5k/2$: access to increasingly fast hidden modes causes the additional worst-case cost. A finite-horizon version uses the step-response curve only up to time $O(\sqrt D/k)$ for a tested budget of $D$ states; it is not a claim about finitely many noisy measurements.

**Preserving structure at the optimal order.** The same two state-growth orders hold even for stationary analytic Markov competitors that are judged only on the cubic coefficient and may abandon passive, static, linear, and quadratic matching. Our reversible construction retains all those agreements and the sensitivity bound at that same asymptotic order. The [comparison proof](docs/STRUCTURE_COST.md) does not claim equal errors at a fixed state budget or equal leading constants.

**The distinction matters:** exact response complexity can grow without bound even at nonvanishing signal strength; that does not imply an equally large state requirement at fixed accuracy. The approximation requires intervention-relevant information that cannot be obtained from the passive binary process alone.

The [switch-off example](docs/PUBLICATION_SCOPE.md#3-a-diagnostic-boundary-switching-the-field-off-versus-keeping-it-on) gives a separate diagnostic boundary: all targets have the same relaxation after a stationary field is switched off, even at finite field strength, yet their field-on response can differ. The intended compression task starts from a supplied kinetic model; the measurement results separately ask what visible data can distinguish.

## Read and inspect

| Question | Document |
|---|---|
| Does the uncapped binary penalty survive a fixed clock? | [Two-field fixed-clock theorem](docs/FIXED_CLOCK_UNCAPPED_REVERSIBILITY_LOWER_BOUND.md) |
| How can sampled means recover positive hidden operations without a rival cap? | [Gram recovery](docs/FIXED_CLOCK_GRAM_OBSERVABILITY.md) and [resolvent calculus](docs/FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) |
| Can a binary actuator force exponentially more reversible prediction states? | [Binary reversibility theorem](docs/BINARY_REVERSIBILITY_LOWER_BOUND.md) |
| Can the separation retain a smaller internal rate budget? | [Nineteen-level dynamic-lamp theorem](docs/DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) |
| How do actual means control generator words in arbitrary capped reversible rivals? | [Direct fixed-clock word observability](docs/REVERSIBLE_WORD_OBSERVABILITY.md) |
| How are positive transports repaired without adding states? | [Balanced stationary-flux repair](docs/POSITIVE_TRANSPORT_REPAIR.md) |
| Can randomized overlapping aggregation avoid exponential state cost? | [Soft-aggregation lower](docs/SOFT_AGGREGATION_LOWER_BOUND.md) |
| Why does mean accuracy constrain features lost by aggregation? | [Observable aggregation rigidity](docs/OBSERVABLE_AGGREGATION_RIGIDITY.md) |
| Can exact fixed-length reversible prefix matching require unbounded dimension? | [Five-color, fifteen-symbol obstruction](docs/EXACT_REVERSIBLE_PREFIX_OBSTRUCTION.md) |
| Can every partition-based reduction be exponentially larger than a new reversible model? | [Aggregation architecture lower](docs/AGGREGATION_STATE_LOWER_BOUND.md) |
| How can a huge address-and-table model have a polynomial reversible predictor? | [Uniform register-scenery compression](docs/REGISTER_SCENERY_COMPRESSION.md) |
| Can connected sparse local dynamics mix rapidly while switching still costs polynomially many states? | [Fixed-label expander lower](docs/EXPANDER_SCENERY_LOWER_BOUND.md) |
| Can reversible compression work when both density moments and cheap fragmentation fail? | [High-girth scenery and simultaneous-accuracy upper](docs/EXPANDER_SCENERY_COMPRESSION.md) |
| Can local motion on a line already require polynomial controlled memory? | [Local-walk lower bound and three prediction costs](docs/LOCAL_WALK_LOWER_BOUND.md) |
| Can sparse strong transitions be retained in a polynomial reversible model? | [Whole-component compression and lattice bounds](docs/SPARSE_REVERSIBLE_COMPRESSION.md) |
| Can every constant-field step be easy while switching is hard, with analytic rates? | [Analytic common predictor and the task separation](docs/ANALYTIC_CONSTANT_STEP_COMPRESSION.md) |
| When does polynomial compression retain reversibility despite unbounded density spikes? | [Density-moment and tail theorem](docs/MOMENT_DENSITY_REVERSIBLE_COMPRESSION.md) |
| What was the first reversible sampling construction? | [Bounded transition-rate density theorem](docs/BOUNDED_DENSITY_REVERSIBLE_COMPRESSION.md) |
| How large can the state cost be with only two actuator values and bounded rates? | [Polynomial lower bound with a fixed control clock](docs/POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) |
| What upper bounds hold with a finite actuator alphabet and rate cap? | [Polynomial Markov and reversible bounds](docs/BOUNDED_RATE_FINITE_FIELD.md) |
| What is the physical lower-bound target and its original interpolation proof? | [Shift-register construction and earlier lower bounds](docs/SHIFT_REGISTER_LOWER_BOUND.md) |
| How different can exact cubic and full controlled prediction be? | [Earlier binary-tree construction](docs/GENERAL_CONTROLLED_LOWER_BOUND.md) |
| Can approximation preserve reversibility and exact variance? | [General reversible compression](docs/REVERSIBLE_GENERAL_COMPRESSION.md) |
| Where is the finite-field state order sharp? | [Uniform finite-field theorem for the rank-one subclass](docs/FINITE_FIELD.md) |
| Does one fixed intervention already require growing model size? | [Fixed nonzero step lower bound](docs/FIXED_FIELD_LOWER_BOUND.md) |
| Can arbitrarily many response orders agree with the actuator fixed? | [Fixed-actuator response hierarchy](docs/FIXED_ACTUATOR_HIERARCHY.md) |
| What replaces the scalar kernel for complete driven path laws? | [Stationary actuator process and matrix-return closure](docs/ACTUATOR_PROCESS.md) |
| What was the first general existence construction? | [Finite-word bounded-sensitivity upper bound](docs/GENERAL_FINITE_FIELD_UPPER_BOUND.md) |
| What can two visible measurements reveal? | [Path response and statistical separation](docs/ACTIVE_PATH_RESPONSE.md) |
| Does the distinction survive imperfect passive lumpability? | [Quartic passive information and robustness](docs/NEAR_LUMPABILITY.md) |
| What is the candidate contribution, and how does it compare with prior theorems? | [Publication scope and operational interpretation](docs/PUBLICATION_SCOPE.md) |
| What is the model, and where is the exact proof? | [Core theory and three-state example](docs/THEORY.md) |
| What survives at nonzero error tolerance? | [Nonvanishing signal, approximation bound, and Markov realization](docs/FINITE_ACCURACY.md) |
| Why is the squared-logarithmic state count necessary? | [Unrestricted-rate lower bound](docs/UNRESTRICTED_RATE_LOWER_BOUND.md) |
| Does preserving the physical structure increase the asymptotic state cost? | [Relaxed and structure-preserving comparison](docs/STRUCTURE_COST.md) |
| What is already known, and what remains to be checked? | [Prior-art and novelty audit](docs/PRIOR_ART.md) |
| What was actually tested? | [Verification scope and provenance](docs/VERIFICATION.md) |
| What is the next research task? | [Current work order](work_orders/CURRENT.md) |

The preserved [checkpoint verifier](scripts/verify_checkpoint.py) and [finite-accuracy verifier](scripts/verify_finite_accuracy.py) remain regression baselines. Extensions check [positive quadrature](scripts/verify_quadrature.py), [minimal reversible realization](scripts/verify_minimal_realization.py), [finite-sample response lower bounds](scripts/verify_response_lower_bounds.py), [unrestricted-rate lower bounds](scripts/verify_unrestricted_rate_lower_bound.py), [finite-field identities](scripts/verify_finite_field.py), [path information](scripts/verify_path_information.py), [the actuator hierarchy](scripts/verify_actuator_hierarchy.py), [general compression identities](scripts/verify_general_compression.py), [reversible compression](scripts/verify_reversible_compression.py), [the earlier controlled lower bound](scripts/verify_general_controlled_lower_bound.py), [the shift-register lower bounds](scripts/verify_shift_register_lower_bound.py), [bounded-rate prediction](scripts/verify_bounded_rate_prediction.py), and [the polynomial controlled lower bound](scripts/verify_polynomial_controlled_lower_bound.py). The new checks cover [constant-step compression](scripts/verify_constant_step_compression.py) and [bounded-density sampling](scripts/verify_bounded_density_sampling.py). Further checks cover [analytic field dependence](scripts/verify_analytic_constant_step.py) and [density-moment sampling](scripts/verify_moment_density_sampling.py). The local-network extension checks [whole-component compression](scripts/verify_sparse_reversible_compression.py) and [the local-walk lower bound](scripts/verify_local_walk_lower_bound.py). Further exact checks cover [expander scenery compression](scripts/verify_expander_scenery_compression.py) and [the fixed-label expander lower](scripts/verify_expander_scenery_lower_bound.py). The architecture comparison adds [aggregation checks](scripts/verify_aggregation_state_lower_bound.py) and [register-scenery compression checks](scripts/verify_register_scenery_compression.py). The reversibility extension adds [dynamic-lamp checks](scripts/verify_dynamic_lamp_reversibility_lower_bound.py), [soft-aggregation checks](scripts/verify_soft_aggregation_lower_bound.py), and [exact-prefix checks](scripts/verify_exact_reversible_prefix_obstruction.py). The binary extension adds [sparse marker and normalization checks](scripts/verify_binary_reversibility_lower_bound.py). Their generated evidence is in [reports](reports).

## Reproduce

Use Python 3.13; the saved local run used 3.13.5. Dependencies are pinned to the tested environment in [requirements.txt](requirements.txt).

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make check
```

Without Make:

```bash
python scripts/check_repository.py
mkdir -p .check-output
python scripts/verify_checkpoint.py --output .check-output/checkpoint.json
python scripts/verify_finite_accuracy.py --output .check-output/finite_accuracy.json
python scripts/verify_quadrature.py --output .check-output/quadrature.json
python scripts/verify_minimal_realization.py --output .check-output/minimal_realization.json
python scripts/verify_response_lower_bounds.py --output .check-output/response_lower_bounds.json
python scripts/verify_unrestricted_rate_lower_bound.py --output .check-output/unrestricted_rate_lower_bound.json
python scripts/verify_finite_field.py --output .check-output/finite_field.json
python scripts/verify_path_information.py --output .check-output/path_information.json
python scripts/verify_actuator_hierarchy.py --output .check-output/actuator_hierarchy.json
python scripts/verify_general_compression.py --output .check-output/general_compression.json
python scripts/verify_reversible_compression.py --output .check-output/reversible_compression.json
python scripts/verify_general_controlled_lower_bound.py --output .check-output/general_controlled_lower_bound.json
python scripts/verify_shift_register_lower_bound.py --output .check-output/shift_register_lower_bound.json
python scripts/verify_bounded_rate_prediction.py --output .check-output/bounded_rate_prediction.json
python scripts/verify_polynomial_controlled_lower_bound.py --output .check-output/polynomial_controlled_lower_bound.json
python scripts/verify_constant_step_compression.py --output .check-output/constant_step_compression.json
python scripts/verify_bounded_density_sampling.py --output .check-output/bounded_density_sampling.json
python scripts/verify_analytic_constant_step.py --output .check-output/analytic_constant_step.json
python scripts/verify_moment_density_sampling.py --output .check-output/moment_density_sampling.json
python scripts/verify_sparse_reversible_compression.py --output .check-output/sparse_reversible_compression.json
python scripts/verify_local_walk_lower_bound.py --output .check-output/local_walk_lower_bound.json
python scripts/verify_expander_scenery_compression.py --output .check-output/expander_scenery_compression.json
python scripts/verify_expander_scenery_lower_bound.py --output .check-output/expander_scenery_lower_bound.json
python scripts/verify_aggregation_state_lower_bound.py --output .check-output/aggregation_state_lower_bound.json
python scripts/verify_register_scenery_compression.py --output .check-output/register_scenery_compression.json
python scripts/verify_soft_aggregation_lower_bound.py --output .check-output/soft_aggregation_lower_bound.json
python scripts/verify_exact_reversible_prefix_obstruction.py --output .check-output/exact_reversible_prefix_obstruction.json
python scripts/verify_dynamic_lamp_reversibility_lower_bound.py --output .check-output/dynamic_lamp_reversibility_lower_bound.json
python scripts/verify_binary_reversibility_lower_bound.py --output .check-output/binary_reversibility_lower_bound.json
python scripts/verify_state_speed_boundary.py --output .check-output/state_speed_boundary.json
python scripts/verify_uncapped_observability.py --output .check-output/uncapped_observability.json
python scripts/verify_binary_uncapped_observability.py --output .check-output/binary_uncapped_observability.json
python scripts/verify_fixed_clock_observability.py --output .check-output/fixed_clock_observability.json
```

A failed assertion exits unsuccessfully. Fresh reports go into the ignored `.check-output` directory; the saved reports are not overwritten. Numerical roundoff can differ across platforms. Dependency installation and GitHub Actions setup require network access; the verification calculations themselves do not.

The checks use symbolic algebra, exact rational calculations, and small deterministic matrices. There are no sampled trajectories, trained models, large fluid simulations, or external datasets. The [workflow](.github/workflows/verify.yml) runs the same checks on pushes and pull requests; its live status is separate from the saved local reports.

## Scope and attribution

The coefficient theorems cover the original centered-sensitivity family. The sharp all-protocol finite-field state order applies to the specified rank-one subclass. In the broader bounded binary class, the constant-step task has logarithmic state cost and switching has polynomial state cost, even with any fixed control clock. The switching exponents are not matched. A uniform positive density moment or a polynomial stationary-flux fragmentation profile gives a polynomial reversible upper inside the original field-rule family. In the one-dimensional local-walk class with global refresh, polynomial growth is necessary and sufficient even with reversibility and the spectral band retained. A third sufficient route uses local tree geometry and typical binary labels on logarithmic-girth graphs; it also covers connected sparse local expanders with neither density-moment nor cheap-fragmentation control. This upper holds on one high-probability label event for every accuracy, not for all labelings. A spectral cap alone currently gives a singly exponential reversible upper on general graphs. The unrestricted general family has the larger double-exponential reversible bound. The dynamic-lamp theorem and its binary extension prove an intrinsic exponential reversible cost under the same fixed exit budget, original field rule and exact histogram. The binary construction uses a larger fixed rate/gap ratio. The new nineteen-level and tagged binary theorems remove the rival cap for a superpolynomial lower. The rescaled tagged construction also gives a two-field fixed-clock lower, with inner logarithmic exponent $1/12$ and a finite polynomial witnessing horizon. The earlier tight binary band $[k,3k]$ and the stronger uncapped law $\exp(c\delta^{-\alpha})$ remain open. The separate six-level architecture theorem proves an exponential cost for actuator-respecting stationary-flux partition aggregation, alongside a polynomial new-state reversible upper on the same family; it does not transfer that lower bound to all reversible predictors. The finite-field approximation norm measures single-time means, while exact path equivalence is a separate theorem. The statistical results concern specified hypotheses and records, not recovery of an arbitrary unknown generator. State counts do not measure bits, field-function complexity, parameter precision, runtime, or experimental sample cost. No turbulence or generic molecular implementation claim is made.

Nonlinear response, aggregated Markov inference from dwell times, minimal realization, positive model reduction, and Hankel dimension witnesses are established subjects. The [audit](docs/PRIOR_ART.md) and [publication scope](docs/PUBLICATION_SCOPE.md) distinguish those ingredients from the new combined claims. Demanding the correct passive law does not cause the approximation lower bound: it already applies to competitors without that requirement.

Manuscript writing is on hold while the novelty and significance questions are resolved. Research contact: **Ruge Lin**, [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's existing license is unchanged. Linked third-party papers retain their own copyrights and licenses; their text and figures are not redistributed here.
