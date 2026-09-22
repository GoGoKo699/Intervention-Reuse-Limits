# Intervention Reuse Limits

**When does a perfect passive model remain useful after an intervention?**

This theory-first project studies finite-state stochastic dynamics. A system can have an exact two-state description when left alone, while hidden kinetic modes become visible in its nonlinear response. The objective is to characterize what a reusable model must retain, and how that requirement changes when exact equality is replaced by a specified accuracy.

**Research status:** the takeover audit reproduces the original checkpoint and strengthens the constructive bounds. The approximation and realization methods reduce to established mathematics; publication-level novelty remains unresolved. Manuscript writing remains on hold.

## Current results

**Exact separation.** For every $N\ge3$, a reversible $N$-state model has exactly the same complete passive binary path law, static response curve, and dynamic linear mean response as a two-state reference, but its exact cubic step response requires at least $N$ states in an analytic autonomous Markov surrogate. The separation can be maintained with bounded field coupling and a nonvanishing total cubic correction.

**Finite-accuracy reuse.** Within the constructed family, a scalar kinetic kernel determines the cubic mean response to every bounded weak-field protocol. For kernel mass $W$, protocol bound $U$, and any positive integer $n$, a positive-quadrature construction and reversible realization give a surrogate with at most $2n(n+1)+3$ states and cubic-coefficient error

$$
\sup_{t\le T}|m_3[u](t)-\widetilde m_3[u](t)|\le8U^3W\,16^{-n}
$$

for every finite horizon and every admissible protocol, independently of the original state count and hidden spectral range. Thus a tolerance $\varepsilon$ needs at most order $\log^2(1/\varepsilon)$ states at fixed $W,U$. The earlier $U^3W/q$ midpoint certificate remains available. These are sufficient bounds obtained from classical quadrature, not optimality or new-approximation-theory claims.

**Exact realization of a known kernel.** A kernel with $r$ distinct positive exponential modes has an explicit reversible realization with $r+2$ total states and sensitivity magnitude $\sqrt W$. When no hidden decay rate equals $k$, this meets the exact pole-location lower bound. The construction is a corollary of finite Jacobi inverse spectral theory.

**The distinction matters:** exact response complexity can grow without bound even at nonvanishing signal strength; that does not imply an equally large state requirement at fixed accuracy. The approximation requires intervention-relevant information that cannot be obtained from the passive binary process alone.

## Read and inspect

| Question | Document |
|---|---|
| What is the model, and where is the exact proof? | [Core theory and three-state example](docs/THEORY.md) |
| What survives at nonzero error tolerance? | [Nonvanishing signal, approximation bound, and Markov realization](docs/FINITE_ACCURACY.md) |
| What is already known, and what remains to be checked? | [Prior-art and novelty audit](docs/PRIOR_ART.md) |
| What was actually tested? | [Verification scope and provenance](docs/VERIFICATION.md) |
| What is the next research task? | [Current work order](work_orders/CURRENT.md) |

The preserved [checkpoint verifier](scripts/verify_checkpoint.py) and [finite-accuracy verifier](scripts/verify_finite_accuracy.py) remain regression baselines. New checks cover [positive quadrature](scripts/verify_quadrature.py) and [minimal reversible realization](scripts/verify_minimal_realization.py). Their generated evidence is in [reports](reports).

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
```

A failed assertion exits unsuccessfully. Fresh reports go into the ignored `.check-output` directory; the saved reports are not overwritten. Numerical roundoff can differ across platforms. Dependency installation and GitHub Actions setup require network access; the verification calculations themselves do not.

The checks use symbolic algebra, exact rational calculations, and small deterministic matrices. There are no sampled trajectories, trained models, large fluid simulations, or external datasets. The [workflow](.github/workflows/verify.yml) runs the same checks on pushes and pull requests; its live status is separate from the saved local reports.

## Scope and attribution

The observable is a single-time binary mean; the response is a Taylor coefficient about equilibrium. The exact lower bound applies to analytic finite-state autonomous Markov models. The approximate surrogate may change microscopic topology and rates. Neither result is a general control impossibility, a bit-complexity bound, a noise-robust identification theorem, or a turbulence result.

Nonlinear response revealing hidden kinetics, coarse response theory, minimal realization, and exponential-kernel approximation are established subjects. The [audit](docs/PRIOR_ART.md) now includes theorem-level comparisons and both previously inaccessible 2026 leads. A broad passive-versus-altered-dynamics story is already present in prior work; the specific combined statement here still needs a distinctive operational contribution.

Manuscript writing is on hold while the novelty and significance questions are resolved. Research contact: **Ruge Lin**, [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's existing license is unchanged. Linked third-party papers retain their own copyrights and licenses; their text and figures are not redistributed here.
