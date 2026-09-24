# Internal review: the physical interface and unknown detector errors

[Readout theorem](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md) · [Charge realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) · [Preparation boundary](FAMILIAR_SWITCH_PREPARATION_BOUNDARY.md) · [Source audit](FAMILIAR_SWITCH_REALIZATION_SOURCE_AUDIT.md) · [Verifier](../scripts/verify_switch_physical_interface.py) · [Report](../reports/switch_physical_interface.json) · [Verification](VERIFICATION.md)

**24 September 2026.** This continuation strengthens the physical interpretation and removes the need to know two symmetric detector error probabilities. It does not establish a laboratory demonstration or publication-level novelty. Reviewers here are separate agents within the same investigation; these checks are internal, not external peer review.

## Unknown detector contrasts

The author, a separate mathematical reviewer and the coordinator checked the cleared singleton polynomial and all four contrast corners. Its bilinear dependence on the contrasts is the essential simplification. The recorded scalar $R=u(C-D)+uMD-(u-M)L$, with its sign gates, puts both singleton branches strictly on the wrong side of zero for every allowed independent symmetric detector.

Target errors may lie anywhere between zero and one percent per bit; rivals may choose any fixed error probabilities up to one half. The channel must remain symmetric, memoryless and independent of the hidden process and of the other electronic flip. The same instrument is used in both protocols. Asymmetric or persistent-memory detectors remain outside scope.

The reviewers checked the target-contrast derivatives, dependency-preserving bound for $C-D$, exact quadratic remainder and biased/approximate-force residual. These yield nominal joint-TV gap $>3/8000$, stationary robust gap $>31/100000$, and actual recorded gap $>1/5000$. The constructive general-three upper is $1/50000$, giving state minima three and four on $[2\times10^{-5},2\times10^{-4}]$ under the explicit physical budgets.

The biased ordinary counterexample confirms a real boundary: dropping stationary balance can make the raw sign test reject a reversible three-state model. Its active kernels are continuous-time embeddable, and small reversible generator perturbations make the example irreducible while retaining strict violations. This is a counterexample to weakening a premise, not a fit to the target.

## Statistical test and a correction during review

Four empirical-moment Hoeffding bounds and a union bound retain the dependence of the final bit and bit product within one trial. Independent fresh trials are required. The tested moment box includes rival preparation/disturbance displacement; the target power proof includes both that radius and target concentration error.

The first statistical formulation omitted an explicit localization condition. The nuisance bands were proved only on the coordinate box in Section 4 of the readout note. The final rejection rule therefore requires the entire confidence box to lie inside that localization box. Its affine conditions and the multiaffine witness inequalities can all be checked at sixteen moment vertices and four contrast corners. With localization included, the uniform null-validity and target-power arguments pass.

The sufficient allocation is 254 million trials per arm: 508 million paired trials and 1.016 billion binary readouts. Both error probabilities are below five percent. Exact arithmetic checks the exponential comparison and the target's total moment radius $0.0006000002<0.00062$. This conservative guarantee concerns the exact composite null with its physical allowances; it supplies no extra approximation allowance or optimality claim. Earlier calibrated-detector allocations do not transfer.

## Physical realization and unequal rates

The charge-model author, an independent algebra reviewer and the coordinator checked the four-state energy substitution, Fermi rates, formal coordinate closure, tilted stationary law and six strictly positive predictive rates. The three-state construction covers $2/3\le\Gamma_2/\Gamma_1\le2$ with common exit cap $3\Gamma_1$. Positivity extends to every ratio at least $2/3$; the upper ratio bound supplies the common cap. The ordinary lower itself is uncapped.

The conditional covariance stays positive at unequal positive attempts, so the exact state counts survive. The old quantitative observation gaps and sample allocations remain restricted to the equal-rate fixture. A positive predictive-rate margin is not a uniform observation gap.

The physical embedding requires nondegenerate single levels, incoherent sequential tunneling, no interdot particle transfer, equilibrium reservoirs at the same temperature and constant bare tunnel couplings over the relevant energies. Detailed balance alone does not imply the required closure. Spin degeneracy, metallic-junction rates and generic energy-dependent prefactors can alter it. The source audit distinguishes established models and component demonstrations from our specialization and unverified device tolerances.

The spectator-field likelihood-ratio bound and generator perturbation budget were checked separately. Residual gate cross-talk changes both the stationary force-law relation and the trajectory. A short readout plus a target rate bound does not constrain arbitrarily fast rivals.

## Preparation and instrument boundaries

Separate mathematical reviews checked both explicit counterexamples and the response-specific preparation lemma. The first is a positive-rate reversible continuous-time three-state process whose complete low-field binary trajectories hide a nonstationary preparation. The second is a two-state reversible process whose initial instrument preserves every later endpoint law while destroying the initial-record correlation.

The proper disturbance object is the joint law of the recorded initial bit and the postmeasurement hidden state. Preserving the hidden marginal alone is insufficient. Conversely, an instrument preserving each conditional equilibrium law and its visible sector can be harmless despite large hidden transitions.

Under exact balance and the at-most-three-state null, an observed relaxation lower bound and an extra unrecorded low tick before each original experiment control preparation errors in the particular response tables. This optional five-protocol experiment does not establish the instrument premise, remove exact balance, or inherit any old finite-sample allocation.

## Reproducibility and remaining work

The coordinator and an independent reviewer read the complete new verifier source, including imported rational moment intervals, polynomial identities, finite fixtures and concentration arithmetic. Final source/proof hashes, exact check count, byte-for-byte replay and the complete repository gate are recorded in [Verification](VERIFICATION.md). Existing verifiers, reports, proof snapshots, license and recovery files are preserved.

The next scientific question is whether a similarly short protocol can increase the observed witness margin enough to tolerate more realistic preparation and readout models at a useful statistical cost. Manuscript drafting remains deferred.
