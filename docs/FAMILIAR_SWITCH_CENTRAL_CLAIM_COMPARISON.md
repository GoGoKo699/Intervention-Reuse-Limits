# What is new in the four-word state-count result?

Focused primary-source comparison, 24 September 2026. This assesses the
[minimal theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md), rather than the
detector construction or improvements to sample constants. It supplements
the earlier [source audit](FAMILIAR_SWITCH_PREPARATION_FREE_SOURCE_AUDIT.md).

**Verdict:** the defensible candidate contribution is the complete
three-versus-four realization separation for one shared controlled
prediction task. Detailed-balance reciprocity, singleton-return inference,
positive realizations, equilibrium-preserving reduction, and warnings
about misleading thermodynamic interpretations of reduced models all
have substantial precedents. The lower identity by itself is elementary.
The sources inspected below do not supply the complete separation, but
that bounded finding does not establish priority or PRL-level significance.

## The claim being compared

The target is an ordinary reversible four-state model at either held
field. The data consist of the initial/final binary pair laws for the
four words $0,H,0H,H0$. One shared positive three-state continuous-time
model reproduces those laws and retains the same deterministic readout
and stationary Gibbs tilt. Every ordinary reversible model with at most
three states fails, even when it may choose arbitrary preparations for
the different words. Thus the minimum is three in the general class and
four in the ordinary class.

The minimal theorem states this for finite positive coupling, field and
dwell times, with a parameter-dependent positive accuracy interval. The
certified one-percent kinetic neighborhood of the selected operating
point is a separate robustness result. The claim concerns the specified
pair laws, not all observed trajectories. The upper model is an actual
positive Markov generator, not only a three-dimensional mean equation.
The common field coupling is a physical interface requirement; its
inheritance under a fixed readout-compatible equilibrium reduction is
explained in the [equilibrium reduction note](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md).

## Closest inspected results

| Primary source and inspected location | Shared content and decisive difference |
| --- | --- |
| Amann, Schmiedl and Seifert, *J. Chem. Phys.* **132**, 041102 (2010), [author text](https://arxiv.org/html/1001.0528v1), Eqs. (3)–(15) | A three-state autonomous model has one visible singleton and two hidden off states. Waiting-time statistics and the return probability after starting in the singleton identify combinations of rates; Eq. (14) separates equilibrium-compatible observations from incompatible ones. Singleton conditioning and an observable obstruction to a reversible hidden model are therefore precedents. The paper does not compare one shared pair of controlled generators, construct a smaller positive model of a reversible target, or prove the present three-versus-four minimum from four endpoint tables. |
| Wu and Jia, *Phys. Rev. Lett.* **134**, 087103 (2025), [author text](https://arxiv.org/html/2406.19586v2), Eqs. (3)–(5), (12)–(14), Appendix A | For a specified autonomous network topology and coarse observation, they characterize sufficient statistics of a stationary coarse path and derive equilibrium constraints. Appendix A constructs a compatible equilibrium three-state realization when the binary three-state statistics satisfy the stated criterion. Neither equilibrium inference nor an associated existence construction is new here. Their data include dwell and jump information from an autonomous path; their conclusion does not give a shared two-control positive realization with a common tilt, alongside exclusion of every ordinary three-state rival from the four pair tables. |
| Franco, Kepka and Velázquez, *Arch. Ration. Mech. Anal.* **250**, 25 (2026), [publisher full text](https://link.springer.com/article/10.1007/s00205-026-02183-7), Definition 3.1, Propositions 3.8–3.9, Corollary 3.11, Example 3.12, Theorem 5.5 | They study reciprocal concentration responses after injection into one linear reaction system. Propositions 3.8–3.9 connect pathwise reciprocity, semigroup measurements and detailed balance. Corollary 3.11 addresses three states; Example 3.12 shows a four-state limitation, and Theorem 5.5 uses perturbation stability and network architecture. Reciprocal path algebra and a three/four distinction are explicit precedents. The present return identity combines two different controlled kernels whose stationary weights are linked by the measured sign; the complete positive-realization comparison is not their one-generator response theorem. |
| Fornace and Lindsey, *An approximation theory for Markov chain compression* (2025), [author text, version 3](https://arxiv.org/html/2506.22918v3), Section 4.1, Lemma 4.1, Corollary 4.6, Theorem 3 | Their induced reduced generator is an irreducible reversible Markov generator with an aggregated stationary law. The lifted approximation preserves nonnegativity and stochasticity, with quantitative semigroup error bounds. Equilibrium-preserving Markov compression is therefore an existing constructive subject. The analysis treats a single autonomous chain. Applying it separately at two fields does not ensure a common retained state space, deterministic readout and prescribed Gibbs tilt, or exact agreement with the four controlled pair laws at a specified state budget. It does not yield the present minimality separation. |
| Hartich and Godec, *Phys. Rev. X* **11**, 041047 (2021), [author text](https://arxiv.org/html/2011.04628v4), Section IV, Eq. (23), Figs. 3 and 6; and *Nature Communications* **15**, 8678 (2024), [Comment full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11458581/), Eqs. (1)–(4) | The PRX paper analyzes memory, kinetic hysteresis, and the failure of coarse-graining to commute with time reversal in its milestoning setting. The Comment gives an equilibrium microscopic counterexample to interpreting waiting-time irreversibility as physical dissipation. A generic warning that coarse observations can mislead thermodynamic inference is established. Their objects are coarse path statistics and their physical interpretation, not a proof that every three-state shared-control Markov fit to specified pair laws must break ordinary detailed balance while a four-state fit need not. Their milestoned paths should not be conflated with an ordinary instantaneous binary projection. |
| Falk, *Physica A* **119**, 580–590 (1983), [publisher record](https://www.sciencedirect.com/science/article/pii/0378437183901103), DOI 10.1016/0378-4371(83)90110-3 | The publisher's indexed abstract says reduced stochastic-spin models retain the exact marginal equilibrium law. This is an early equilibrium-preserving reduction precedent. Bounded title/DOI searches and direct publisher/PDF requests did not yield readable full text; the latter returned access errors. No equation-level nonoverlap conclusion about Falk is claimed. This remains an explicit audit gap. |

The first five rows were checked against primary full texts. The final
row has only abstract-level support. Absence of a result from these
specific inspected passages is not a systematic literature-wide absence
claim.

## Is the main mathematics an easy corollary?

The lower identity is a short deduction from established algebra. Write
$A=K_0$, $B=K_H$ and let $j$ be a singleton readout sector of sign $s$.
For every other state $k$, detailed balance at both fields and the tilt
give

$$
 A_{jk}B_{kj}
 =\frac{1+su}{1-su}B_{jk}A_{kj},\qquad u=\tanh H.
$$

Summing over $k\ne j$ and retaining the common diagonal contribution
produces

$$
 (1-su)(AB)_{jj}-(1+su)(BA)_{jj}
                 +2su A_{jj}B_{jj}=0.
$$

Conditioning on the singleton sign fixes the starting state, so arbitrary
preparation drops out. Having at most three states ensures a singleton
when both signs occur. These are simple observations, not a new
reciprocity principle. They make the proof useful and transparent, but
do not support a broad new-law claim.

The full result requires additional work that is not supplied by that
identity: an ordinary four-state target violates it for both signs, one
shared three-state *positive continuous-time* realization matches all
four tables and the common force, and the obstruction covers every
ordinary three-state topology and preparation. A generic linear closure
does not establish positivity. A reduction at each field separately does
not establish simultaneous realizability. An autonomous equilibrium test
does not establish a smaller realization of controlled data from an
ordinary target. The construction and lower bound on the *same task*
are consequently the strongest candidate contribution.

The inference from the inspected sources is that the complete theorem
is not a direct substitution into their stated results. Its short lower
proof nevertheless lowers the novelty value of presenting the return
identity alone. The generic parameter family and the positive upper
construction matter more to the central claim than sharpening the
sample count or the numerical tolerance.

## A defensible scientific use

This is a benchmark for fitting small kinetic models under interventions.
For these data, a three-state shared-force predictor can be exactly
accurate but cannot simultaneously retain ordinary detailed balance.
A method intended to preserve an equilibrium mechanistic interpretation
must use at least four states, accept error exceeding the certified
margin, or change a stated modeling requirement. The lower bound makes
this a mathematical obstruction rather than a failed optimization run.
It can therefore distinguish predictive compression from preservation
of equilibrium structure in a controlled model-selection problem.

This use is conditional on the shared-force interface and deterministic
readout. It is not evidence of physical dissipation in the target, which
is ordinarily reversible at each held field. It does not show that
ordinary state lumping destroys reversibility, that a raw projected
equilibrium path becomes irreversible, or that the smaller predictor is
a physical implementation. The pulse sequence itself is driven. No
hardware storage, runtime, heat-cost or asymptotic scaling advantage is
established by a three-versus-four abstract state count.

## Readiness decision

The complete controlled realization theorem is a coherent, narrow theory
result worth developing. A headline about newly detecting hidden
nonequilibrium, inventing equilibrium-preserving compression, or first
showing spurious irreversibility would overstate it. The named primary
results do not presently invalidate the combined claim, with the Falk
full-text limitation stated above.

PRL readiness remains unestablished. The unresolved issue is whether the
state-count obstruction changes an important modeling practice or
illuminates a wider class of systems enough to justify that level of
significance. More detector assumptions or smaller numerical error bars
do not resolve that question. The next decisive assessment should focus
on the full shared-control positive-realization separation and its
scientific use, not on the elementary lower identity in isolation.
