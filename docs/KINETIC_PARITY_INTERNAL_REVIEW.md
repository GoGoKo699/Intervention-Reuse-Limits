# Internal review of the kinetic-interface and reversal-parity results

[Resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [Source audit](KINETIC_PARITY_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md) · [Previous internal review](PRL_EXPLORATION_INTERNAL_REVIEW.md)

**Review date: 23 September 2026. Status: mathematical PASS for the five proof notes below.** This record distinguishes internal analytic review from finite computational checks, external peer review and source comparison. It does not certify novelty or editorial suitability. No manuscript is drafted.

The review role compiling this record read the four separately authored interface, capped and resource notes in full. The generalized-reversal note, authored by this role, received complete independent reads from other internal roles, including the coordinating, route and construction reviewers. All reported mathematical reviews passed. “Independent” here describes separate checks within this investigation, not external validation.

## 1. Reviewed proof package

| Note | Claim reviewed | Outcome |
|---|---|---|
| [General kinetic interface](GENERAL_KINETIC_INTERFACE.md) | Wider fixed endpoint-rate intervals and arbitrary kinetic curves preserve the uncapped fixed-clock lower; endpoint equivalence and EPR specialization | PASS |
| [General interface entropy bound](GENERAL_INTERFACE_ENTROPY_BOUND.md) | Same-state endpoint comparison with general return/injection bounds, initial density and the stated distributed-reset hypotheses | PASS |
| [Capped kinetic separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) | Same-cap exponential ordinary-reversible lower and polynomial unrestricted growth on the same two-field clock task | PASS |
| [Generalized-reversal prediction](GENERALIZED_REVERSAL_PREDICTION.md) | Centered word predictor with exact response equivalence, even actuator, generalized balance and polynomial growth | PASS |
| [Kinetic/parity resource tradeoff](KINETIC_PARITY_RESOURCE_TRADEOFF.md) | Three-class comparison and identity-reversal EPR frontier under one shared bounded interface | PASS |

The new finite verifier checks bounded fixtures and proof budgets. Its code review and full repository gates are tracked in [Verification](VERIFICATION.md); this analytic record does not assert those gates have completed. A finite fixture cannot prove an all-model, all-width or all-horizon statement.

## 2. Positive selectors, ordinary adjoints and the capped estimate

The shared interface has \(q_{iA}=kb_i(h)\), \(q_{Ai}=k\mu_i e^{2h}b_i(h)\), and \(b_i(0)=1\). Its fixed-field stationary distribution and finite visible-start recursion are independent of the kinetic values and do not require hidden reversibility. The rank-one visible-projector insertion formula therefore applies to stationary nonreversible rivals too.

With \(k=1\), \(J\) the visible projector and \(H_0=I-J\), the identities

$$
B=H_0+H_0(Q_0-Q_H)H_0,\qquad
K=H_0Q_0H_0+H_0
$$

were checked directly from the full blocks. Field independence of the hidden generator and the zero-field normalization are essential. Squared Lagrange polynomials in the diagonal \(B\) are exactly nonnegative on every rival, and exactly target label projectors. Constant terms use the hidden identity \(H_0\), so no visible-coordinate leakage occurs.

Under the common hidden exit cap, \(P=I+K/3\) is entrywise nonnegative. Thus \(48A_cPA_d\) is positive and is the exact target transport \(16D_cKD_d\). Ordinary reversibility supplies the stationary adjoint relation for reverse transports. Positivity alone does not supply that relation; a generalized reversal is insufficient for this part of the proof.

The selector degree is at most 36 and transport degree at most 73. Consequently entropy words have degree, projector count and logarithmic coefficient mass \(O(n+1)\). All target lamp relations hold exactly and the central target mass is \(1/18\). Rival support, signed-query domination and weighted normalization satisfy the existing repair interface without imposing target coordinates or a mass floor.

The common exit bound and the endpoint kinetic upper bound give a uniform full reversible spectral cap. Total-degree logarithm truncation remains valid with interspersed \(J\), since its norm and coefficient mass are one. The stated majorants give a geometric target/rival tail and coefficient mass at most \(J_{\mathcal P}C_a^d4^M\). The factor linear in the number of propagator letters from inserted-word recovery is absorbed by the spare factor in the \(8\varrho\) cutoff. Scalar error is therefore \(e^{O(n)}\delta^\theta\) with fixed \(\theta>0\).

Choosing accuracy \(e^{-C_*(n+1)}\) supplies the weighted-repair defects and state count \(2^{3\cdot2^n/4}\). The finite witness uses the cutoff associated with that threshold, so it needs only \(O(n+1)\) ticks even when the actual accuracy is smaller. The capped lower tolerates endpoint return rates approaching zero, or zero rates; its spectral argument does not need a positive reset floor.

## 3. The two-field rank lower is target-only

The target lamp vectors have Gram matrix \(I_r/18\) after the stated factor of two. The formal adjoint polynomial \(W_b^\sharp\) equals the stationary adjoint on the target. On a nonreversible rival it is only the same forward polynomial; the proof correctly makes no adjoint claim there.

Entire left and right factors are truncated separately, only on the reversible target. Degree \(O(n+1)\) makes their retained target matrix within \(1/(72r)\) per entry of \(I_r/18\), hence its smallest singular value is at least \(1/24\). Evaluating the same finite propagator/projector polynomials on any \(D\)-state rival factors the matrix through \(D\) states. The visible-start recursion controls every inserted scalar with coefficient cost \(e^{O(n)}\).

No rival logarithm, real spectrum, rate cap or detailed balance is required in this rank branch. It does require the shared interface and preparation/readout. It yields polynomial necessity on the same two fields, so the new unrestricted and generalized-reversible growth classes need no additional thirty-nine-field menu or family union.

## 4. General reset entropy and normalization

The hidden arithmetic symmetrization preserves every exit, and the pairwise inequality \(d(K\|L)\le\sigma_{\rm hid}/4\) retains the ordered-sum convention. Its proof, including the derivative \(F''(t)=4t^2/(1-t^2)^2\), was checked.

For return lower bound \(\alpha\), injection-density upper bound \(\beta\), and initial hidden density at most \(c_0\), the residual maximum principle gives \(c_0+\beta t\). Averaging the final reset-free segment gives the bracket

$$
A_0+\bigl((c_0-A_0)x-A_0\bigr)e^{-x},
\qquad A_0=\beta/\alpha,\quad x=\alpha T.
$$

Its derivative and maximum give the stated \(\Psi(c_0,A_0)\), including \(c_0>A_0\) and \(\beta=0\). Thus the initial-law convention and the no-reset atom are both retained. The usual preparation has \(c_0=1/2\); under the bounded local-balance interface it lies in the simpler regime.

For a common equilibrium ratio, the hidden baseline mass \(p_0\) gives \(\sigma_0=p_0\sigma_{\rm hid}\). In the zero-field-normalized model \(p_0=1/2\), so the mean bound is

$$
\sqrt{\frac{c_+}{b_-^2}\frac{\sigma_0}{k}}.
$$

The distributed-reset extension was checked separately: its bracket has \(A_0=c_{\rm reset}+\beta/\alpha\). The explicitly imposed residual occupation and path-cost assumptions are necessary for the supplied argument; the note does not silently subtract differing hidden transitions and retain their old relative-entropy cost.

Same-state finite-EPR regularization preserves exits, and maximal jump coupling gives the stated \(2\epsilon Bk/\alpha\) mean cost. All factors of \(k\), hidden mass and two from the readout range were checked. These are uniform endpoint comparisons, not uniform entropy bounds for full arbitrarily long paths.

## 5. Generalized reversal and exact response equivalence

Reversibility of the target symbol process makes each word-edge stationary flux equal to its reversed, word-reversed flux. This establishes \(\widehat P^*=\Theta\widehat P\Theta\), including zero and self-edges. With odd length, the middle symbol is invariant under word reversal and retains the target histogram.

The key equality is a stationary discrete-index shift: the middle output at index \(j\) equals the endpoint output at index \(j-d\). It is not a fixed physical-time shift. Independent Poisson embedding preserves equality of complete stationary actuator-path laws. Original-rule hidden entry is a tilt by the first actuator value, and hidden survival/killing depends on the actuator path. Therefore the centered and endpoint predictors have identical controlled visible path laws for every fixed deterministic protocol.

Odd-length rounding costs at most a fixed alphabet factor in state count. The full involution fixes the visible state and gives generalized balance at every constant field. The involution is a permutation of counted states, not a supplied operation, external clock or uncounted memory. A generic forward/backward doubled predictor would only average hidden excursion laws; that unsupported shortcut is not used.

Mixing \(K\) with \(K^*\) preserves the generalized relation while making ordinary EPR finite, without new states. Thus polynomial prediction can have zero generalized stationary EPR and finite positive identity-reversal EPR. Bacallado’s established word-reversal result is attributed; the source comparison does not externally validate the new controlled-response integration.

## 6. Resource scopes and limits

The shared envelopes \(b_-\le R^{-1}\), \(b_+,c_+\ge R\) admit the unchanged targets and every invoked upper at all fields in the prescribed interval. The broader capped theorem supplies the lower even before these additional envelope restrictions, while the original-rule uppers remain members of the restricted class.

The class inclusions and minima have the correct direction. Additive symmetrization preserves every imposed constraint, so the identity-EPR budget inequality holds per target before taking the worst-case supremum. The small-error inversion and polynomial-budget consequence retain that worst-case quantifier; a hard target may depend on accuracy and resource budgets.

The ordinary lower and identity-EPR frontier concern the specified reversal convention. They do not imply a generic thermodynamic dissipation necessity when nontrivial state parities are admitted. No mechanical implementation of the centered word states, driven heat/work lower, stationary Shannon-entropy lower, experimental sample bound or fitting guarantee is supplied.

Finite asymptotic witness lengths are proved. A small certified state separation at a useful numerical tolerance has **not** been achieved by this checkpoint. The engineered address-and-table target and large fixed constants remain physical-significance limitations. No unresolved mathematical issue was found in the five reviewed notes; further review should target a new claim or a concrete remaining risk.
