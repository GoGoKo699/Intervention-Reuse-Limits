# Intervention Reuse Limits

### How many states must a kinetic model retain when its controls change?

A fast hidden variable can often be averaged away. A small model may then
fit relaxation at each held field. This repository asks whether **the same
model still predicts correctly when those fields alternate**, and how its
required number of states changes with prediction accuracy.

For two interacting equilibrium switches, we give explicit positive
Markov models and lower bounds against every smaller admissible model.
The leading hidden lag needs a third state under rapid control. Preserving
equilibrium structure at finer accuracy needs a fourth.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## Start from one tutorial

The teaching anchor is **Stefano Bo and Antonio Celani,
[Multiple-scale stochastic processes: decimation, averaging and beyond](https://arxiv.org/pdf/1612.04999)**,
*Physics Reports* 670, 1–59 (2017).

Read §1, §2 through §2.2, and §2.3.2. Then follow the
[project narrative](REVIEW.md): averaging the fast switch, retaining its
lag, and deciding how many positive states a reused model requires.
Basic probability, matrix algebra, linear ODEs and asymptotic notation
are sufficient for this route. The review supplies the multiscale
starting point; the state-count results below are proved in this repository.

## Read the repository in three passes

| Pass | Route | What it gives you |
| --- | --- | --- |
| Overview | This page | The question, result and experimental menu |
| Understand the mechanism | **[Tutorial-to-result narrative](REVIEW.md)** | One continuous explanation from Bo–Celani to the project |
| Check the arguments | **[Documentation map](docs/README.md)** and [scientific guide](docs/SCIENTIFIC_CASE.md) | Exact assumptions, proof dependencies and evidence limits |

The [background guide](docs/MANUSCRIPT_BACKGROUND.md) supplies the primary
literature and citation map. The [tutorial selection record](docs/TUTORIAL_OPTIONS.md)
retains the alternatives considered; they are not additional prerequisites.

## The prediction task

The target has one visible sign $`S`$ and one hidden sign $`Z`$.
Its dimensionless energy is $`-JSZ-hS`$, and each held field has
reversible heat-bath dynamics. Set

```math
t=\tanh J\in(0,1),\qquad u=\tanh H\in(0,1),\qquad
r=\frac{\Gamma_Z}{\Gamma_S}.
```

The asymptotic statements keep $`t,u`$ fixed as $`r\to\infty`$.
Time is measured in units of $`1/\Gamma_S`$.
The [physical-model derivation](docs/FAMILIAR_SWITCH_COMMUNITY_MODEL.md)
connects these switches to a selected equilibrium sequential-tunneling model.

| Part of the task | Requirement |
| --- | --- |
| Target preparation | Zero-field equilibrium: $`\pi_0(s,z)=(1+tsz)/4`$ |
| Observation | True initial and final visible signs; no intermediate records or feedback |
| Controls | Predetermined holds at fields $`0,H`$; ideal changes leave the state unchanged |
| Reused model | One persistent state space, one fixed generator per field, one deterministic binary readout |
| Rival preparation | May vary with the whole word; no rate cap or equilibrium-preparation promise |
| General models | Nonnegative transition rates and normalized probabilities |
| Reversible models | Detailed balance and the stated shared normalized Gibbs relation, with unknown tilt |

A held-field fit and a separate fit for every pulse sequence do not meet
the same reuse requirement. All persistent states count, including
preparable states of zero stationary weight.

## The state-count law

For **all finite two-field words with arbitrary held durations**, let
$`E_d^{\mathrm{gen}}(r)`$ and $`E_d^{\mathrm{rev}}(r)`$ be the best
worst-case endpoint-pair total-variation errors with at most $`d`$ states
in the two classes. The central orders are

```math
\boxed{
E_2^{\mathrm{gen}}(r)=\Theta(r^{-1}),\qquad
E_3^{\mathrm{rev}}(r)=\Theta(r^{-2}).
}
```

Two reversible states attain the same first-order scale. Four reversible
states are exact, and a general positive three-state model is exact for
all sufficiently large $`r`$. At tolerance $`\epsilon(r)=r^{-p}`$,
the eventual minimum counts are therefore:

| Required precision | General model | Reversible model |
| --- | ---: | ---: |
| $`0\lt p\lt1`$ | 2 states | 2 states |
| $`1\lt p\lt2`$ | 3 states | 3 states |
| $`p\gt2`$ | 3 states | 4 states |

The crossover exponents $`p=1,2`$ depend on constants. If the low/high
clock ticks instead stay fixed and positive, two states already attain
quadratic error; only $`p=2`$ is then an order-level crossover.
Control timing is part of the theorem.

The [all-duration proof](docs/FAMILIAR_SWITCH_RAPID_CONTROL.md),
[fixed-clock proof](docs/FAMILIAR_SWITCH_QUADRATIC_PRECISION.md) and
[exact general construction](docs/FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md)
establish these statements.

## Three experiments expose the leading memory requirement

Use two held-field calibration experiments and one alternating train.
Writing $`L_a,H_a`$ for holds of duration $`a`$, choose

```math
n=\lceil r/2\rceil,\qquad A=\frac nr,\qquad
\mathcal W_r=\{L_A,\ H_A,\ (L_{1/r}H_{1/r})^n\}.
```

Every reusable two-state model with one state per visible sign obeys an
exact multiplication rule for its
conditional contrasts. The target violates that rule at order
$`r^{-1}`$. A reversible three-state model has error $`O(r^{-2})`$
on the same menu. Thus these three settings already require the third
state at intermediate accuracy.

The [finite-pulse proof](docs/FAMILIAR_SWITCH_FINITE_PULSE_WITNESS.md)
covers arbitrary rival preparations. This menu establishes no
three-state lower bound or fourth-state requirement; those belong to
the separate seven-word/all-word task.

Three settings contain a growing train: its $`2\lceil r/2\rceil`$
segments each last $`1/r`$ in dimensionless time. At fixed hidden
attempt rate $`\Gamma_Z`$, each train segment lasts $`1/\Gamma_Z`$
and its total physical duration grows as $`r/\Gamma_Z`$.

## Verification and status

The theorem is analytic. The [verification record](docs/VERIFICATION.md)
and [full sanity audit](docs/FINAL_SANITY_AUDIT.md) map the reproducibility
checks to their claims. To run the existing suite:

```bash
python -m pip install -r requirements.txt
make check
```

The physical model, endpoint task and theorem scope are frozen.
Ideal field jumps and true endpoint records are assumptions; finite-ramp,
detector, sampling, hardware-bit and heat-saving guarantees are not
established for this menu. The conclusions concern predictive states,
not a demonstrated device advantage.

For search and assisted reading, [llms.txt](llms.txt) identifies relevant
research questions, canonical proof links and the limits of the results.

[Current work](work_orders/CURRENT.md) · [Claim ledger](docs/CLAIM_LEDGER.md) ·
[Publication status](docs/PUBLICATION_SCOPE.md) · [Research history](docs/RESEARCH_HISTORY.md) · [MIT license](LICENSE)
