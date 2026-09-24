# Internal review: seven-mean margin certificate

[Proof](FAMILIAR_SWITCH_FINITE_MARGIN.md) · [Source comparison](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) · [Verification](VERIFICATION.md)

**24 September 2026.** This records internal mathematical and computational review, not external validation or novelty certification. Manuscript drafting remains deferred.

## 1. Analytic result reviewed

The canonical mean order is $(H,H^2,H^3,H0,H^20,H0H,H^20H)$. The numerical diagnostic may store a different order, but labels every word explicitly. Every word starts from the same balanced zero-field preparation. Occupation error is half spin-mean error.

For a deterministic binary readout on three states, one sector is a singleton. Detailed balance and the shared Gibbs tilt determine its conditional response variance. The two possible singleton signs give two quartic polynomials $W_\sigma$. The adjugate identity $C\operatorname{adj}(RC)R=\det(RC)I$ establishes the required symmetry without an invertibility assumption. Two-state cases are covered by the stated zero-mass algebraic padding; positive splitting is an alternative interpretation. A one-state model cannot have the required balanced deterministic readout.

The target factorization $W_\sigma=-\sigma\Delta$, with $\Delta>0$, was independently derived and checked by the root reviewer and three separate analytic reviewers. The determinant factor and all-parameter coefficient Lipschitz bound $\Delta/(2L)$ were checked, including the factor of two converting occupation error into mean error. Necessity uses reversible stochastic kernels only, so neither a rate cap nor continuous-time embeddability is assumed. The exact positive three-state upper comes from the preserved structure theorem. A balanced deterministic two-state stationary rival is automatically ordinarily reversible, so the same exclusion supplies unrestricted minimum three.

## 2. Essential exact numerical certificate

The canonical [verifier](../scripts/verify_familiar_switch_margin.py) has 103 exact checks, maximum dense matrix dimension four. Its complete source was read by the root reviewer and two separate reviewers. The [report](../reports/familiar_switch_margin.json) binds both the new proof and the prior structure theorem.

At $\tanh J=\tanh H=4/5$ and clock two, degree-96 rational matrix Taylor series enclose both target propagators. Explicit norm-tail bounds, dyadic entry rounding and interval word multiplication enclose all seven means. Translating each quartic at the rational center and summing the absolute nonconstant coefficient mass bounds its variation over the whole error cube. Both constant terms exceed $1455/10^7$ in magnitude; variation is below $1436/10^7$ and $425/10^7$ for the two signs. Thus occupation error $\le1/2000$ is excluded, not merely a finite grid of rival parameters.

A separate implementation used the three-dimensional mean generator, a degree-32 exact rational Taylor enclosure and a distinct scalar-polynomial representation. It independently verified the same whole-box exclusion. This cross-check does not replace the canonical source; it checks its essential arithmetic by a different representation.

The fixed rational ordinary three-state comparator has exact positive stationary masses and symmetric stationary fluxes. Degree-128 rational exponential enclosures verify maximum seven-word occupation error below $837/10^6<1/1000$. Its maximum exit is $91862/30629<3$. It need not be optimal. Its eleven-word error is larger, so no extension of this certified upper beyond the seven-word menu is made.

Pinned Python 3.13.5 regeneration reproduced the canonical exact report byte for byte. Final hashes are recorded in [Verification](VERIFICATION.md). The analytic polynomial identity is universal; the particular $1/2000$ and $837/10^6$ numerical bounds are computer-assisted exact certificates.

## 3. Exploratory fits are separate evidence

The [new numerical diagnostic](../scripts/screen_short_switch_witnesses.py) and [report](../reports/short_switch_witness_screen.json) contain four target panels, eight fitted ordinary rivals and one rounded rational model. Both singleton signs were tested with a bounded CPU budget. Root and a separate reviewer read the complete script; independent replay passed, followed by byte-identical pinned regeneration after final proof binding. Fitting is optional and absent from the verification gate. Reports preserve the original fit environments rather than rerunning fits to change version metadata.

Direct eleven-word fitting improves on an older retained model evaluated without refitting. This invalidates treating that older model's error as the best known achievable error on the eleven-word menu, but does not invalidate its historical report. No fitted residual is used as a universal lower or a global optimum. The rounded upper's rigorous guarantee comes from the exact verifier, independently of optimizer success.

## 4. Scope and readiness

The target is a familiar time-even coupled conformational pair; equal attempt rates and the specified control interface are retained. Predictions concern endpoint means, not path laws. Passive target paths already have hidden memory. Arbitrary rates at the two fields are allowed, but arbitrary changes in hidden-state field coupling are not: the shared Gibbs tilt is substantive.

The finite margin is 0.05 percentage points, bounded above by an ordinary-three-state fit below 0.1 percentage points on the same menu. No one-percentage-point advantage, experimental sample budget, calibration tolerance, microscopic device, generalized-reversal separation or universal dissipation requirement is established. Those limits prevent treating this checkpoint alone as PRL readiness.

The [source audit](FAMILIAR_SWITCH_MARGIN_SOURCE_AUDIT.md) compares three primary full texts on finite realization, polynomial invariants and dimension witnesses. Classical ingredients are attributed and complete controlled-task assumptions are separated. Falk 1983 remains an unresolved full-text lead from the prior kinetic audit. Internal checks and bounded searches do not certify originality.

The next scientific work is quantitative preparation/field/timing robustness, separate relaxation of the shared Gibbs tilt, and measurement-cost assessment. Full regression and exact-commit publication CI are reported separately in [Verification](VERIFICATION.md).
