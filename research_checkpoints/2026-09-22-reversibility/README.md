# Reversibility research checkpoint — 22 September 2026

This checkpoint preserves the mathematical progress made after tested main commit
[80253e1](https://github.com/GoGoKo699/Intervention-Reuse-Limits/commit/80253e1462d618ccc435f2394aba240e858496b5).
The workspace disconnected during integration. These recovered notes are stored on a separate research branch; the last fully integrated version remains on main.

## Strongest result

The [dynamic-lamp theorem](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) gives a common family with nineteen fixed actuator values for which, as actual controlled-mean tolerance $\delta$ tends to zero,

$$
D_{\rm all}^{(3)}(\delta)=\delta^{-\Theta(1)},\qquad
D_{\rm rev}^{(3)}(\delta)=\exp(\delta^{-\Theta(1)}).
$$

The notation describes growth classes with unmatched positive exponents. More precisely, the bounds are

$$
c_0\delta^{-\gamma}\le D_{\rm all}^{(3)}(\delta)\le C_0\delta^{-p},
\qquad
\exp(c_1\delta^{-\alpha})\le D_{\rm rev}^{(3)}(\delta)
\le\exp(C_1\delta^{-p}\log(2/\delta)).
$$

Both predictor classes obey the same internal outgoing-rate budget $3k$, original exponential field rule, exact actuator histogram, stationary preparation and binary readout. They may construct entirely new states. The second class additionally requires ordinary detailed balance.

The targets have hidden relaxation band $[k,3k]$ and an exact two-state passive visible law. The reversible upper retains that band. Both lower bounds already hold on thirty-nine fixed fields at any fixed positive control clock, with logarithmic witnessing horizons. The reversible lower extends to any fixed rival spectral cap, with constants depending on it and no lower-gap requirement.

The proof passed several independent internal mathematical audits before the outage. These audits are not external validation. The newly planned three-verifier extension and complete twenty-eight-verifier run were unfinished when the workspace disconnected. Any Actions run on this archive branch uses the unchanged preceding twenty-five-verifier suite; it does not verify a newly restored dynamic-lamp program.

## Preserved mathematical arguments

| Note | Result and role |
|---|---|
| [Dynamic-lamp lower](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) | Intrinsic exponential reversible state cost under a common exit budget; polynomial unrestricted growth on the same target family. |
| [Positive transport repair](POSITIVE_TRANSPORT_REPAIR.md) | Repairs nearly stochastic positive adjoint kernels on the same state sets, with explicit path-error control. |
| [Reversible word observability](REVERSIBLE_WORD_OBSERVABILITY.md) | Direct finite-horizon transfer from fixed-clock physical means to generator-word scalars for two capped reversible models. |
| [Soft aggregation lower](SOFT_AGGREGATION_LOWER_BOUND.md) | Randomized overlapping color-preserving Bayes aggregation still has exponential cost, while fresh reversible models for those six-level targets have polynomial cost. |
| [Observable aggregation rigidity](OBSERVABLE_AGGREGATION_RIGIDITY.md) | Actual mean accuracy controls observable words lost by stationary-flux projection, with an error exponent independent of word length. |
| [Exact prefix obstruction](EXACT_REVERSIBLE_PREFIX_OBSTRUCTION.md) | Five colors and fifteen observed symbols can force unbounded exact reversible realization dimension. This is a separate zero-error statement. |
| [Primary-source comparison](PRIOR_ART_COMPARISON.md) | Attributes classical lamp/Følner, entropy, positive-realization and Bayes-aggregation ingredients; scopes the candidate new combination. |

These are reconstructed archival texts based on inspected proofs and retained research context. They are not presented as byte-for-byte copies of the inaccessible local documents. Existing published mathematical scripts, reports, license, dependencies and workflow are inherited unchanged from the parent commit.

## What to do next

First finish the verification and integration recorded in [RESUME.md](RESUME.md). Recover the local sources if the workspace reconnects, complete the dynamic-lamp exact verifier, run all twenty-eight verifiers with fresh-report comparison, and finish the scope updates before merging the research into main.

The next mathematical priority is a binary-actuator version of the intrinsic separation. The nineteen distinct levels currently identify ports and signs, keeping the extracted gate blocks positive in every rival. A binary construction needs another way to force those positive transports without assuming a rival's hidden coordinates. Merely replacing colored selectors by signed algebraic filters is insufficient.

The other major boundary is removal of the reversible rival rate cap. The current physical-mean-to-generator transfer uses that cap essentially. It does not cover arbitrarily fast reversible rivals or arbitrary reversible field rules.

Optimal exponents and statistical acquisition costs remain separate questions. The current theorem is about physical state count for a known target. No large simulation is required, and manuscript drafting remains on hold pending verification and further novelty assessment.
