# Short-protocol diagnostics for familiar coupled switches

[Exact three-versus-four state theorem](FAMILIAR_SWITCH_STRUCTURE.md) · [Physical source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md) · [Screen and saved-model replay](../scripts/screen_familiar_switches.py) · [Retained models and results](../reports/familiar_switch_screen.json)

**Bounded numerical screen, 23 September 2026.** The coupled-switch model has a simple exact predictive state advantage, proved separately. The finite numerical experiments below do not yet show a one-percent robust advantage. Explicit three-state ordinary reversible models approximate every tested two-spin target on its fitted pulse menu to better than $0.14\%$ in occupation probability. The largest retained error is a feasible-model diagnostic, not a lower bound against all three-state rivals.

All errors here concern $P(s_0=+1)$. An absolute error $0.01$ is one percentage point; the corresponding error in the binary mean $\langle s_0\rangle$ is $0.02$. These conventions must not be interchanged.

## 1. A small physical model and a shared experiment menu

Use two or three time-even conformational switches, with energy

$$
E_h=-J_{01}s_0s_1-J_{12}s_1s_2-hs_0,
$$

omitting the last interaction for two switches. Only $s_0$ is driven and observed. The flip rate of switch $i$ is

$$
q_i(s,s^{(i)})=\frac{\alpha_i}{1+\exp(2s_iF_i)},
$$

where $F_i$ is its local interaction field plus $h$ at switch zero. Each experiment starts from the model's own zero-field Gibbs equilibrium. The target attempt rates obey $\alpha_i\le1$, so its total exit rate is at most three. These are four- or eight-state targets, with no larger model simulated.

For each target, the fitted menu contains six constant-field steps and 27 pulses of the form

$$
H\text{ for }t_w,\qquad0\text{ for }t_d,\qquad H\text{ for }t_r.
$$

The three durations range independently over three fixed values. One comparator is fitted to the entire 33-experiment menu; it is not refitted for individual protocols. In this switch model, zero-field evolution need not be an exact two-state visible law. The pulse menu does not rely on that property of the earlier hub-interface model.

The mean equations provide a useful implementation check. For three switches,

$$
\begin{aligned}
\dot m_0&=\alpha_0[-m_0+A(h)+B(h)m_1],\\
\dot m_1&=\alpha_1[-m_1+C m_0+D m_2],\\
\dot m_2&=\alpha_2[-m_2+\tanh(J_{12})m_1],
\end{aligned}
$$

where $A,B$ are the half-sum and half-difference of $\tanh(h\pm J_{01})$, and $C,D$ are the half-sum and half-difference of $\tanh(J_{01}\pm J_{12})$. The corresponding two-spin system closes on $(1,m_0,m_1)$. The screen checks these identities against the full generators. Low-dimensional affine closure alone is not a positive Markov realization or an ordinary reversible realization.

## 2. The completed bounded searches

The searches used three fixed initializations per comparator. The three-spin fits allowed at most 120 least-squares evaluations per start. Three-state fits allowed 300, followed by one local minimax epigraph refinement of at most 150 iterations. There was no search over large networks, broad parameter sweep, or claim of global optimization. The recorded discovery runs took about 1.3 seconds for the six three-spin fixtures, 0.9 seconds for the rational two-spin fixture, and 33.3 seconds for the twelve-case two-spin scan on the working environment.

### Three-spin screen

At $H=1$, all six targets used step times $0.125,0.25,0.5,1,2,4$ and pulse durations $0.25,1,3$. A two-state comparator had independently fitted heat-bath relaxation rates at the two fields, preserving the equilibrium curve. A four-state comparator was one two-spin Ising model with a positive coupling and both attempt rates at most one. Both satisfy the shared total exit cap of three.

| $J_{01},J_{12}$ | $\alpha_0,\alpha_1,\alpha_2$ | Retained two-state error | Retained four-state error |
|---|---|---:|---:|
| $0.35,0.35$ | $1,1,1$ | $0.00676223$ | $0.000154325$ |
| $0.8,0.8$ | $1,1,1$ | $0.0203201$ | $0.00117858$ |
| $1.5,1.5$ | $1,1,1$ | $0.0273313$ | $0.00103656$ |
| $1.2,0.7$ | $1,0.25,0.75$ | $0.0434486$ | $0.000190189$ |
| $1,1.5$ | $1,0.5,0.25$ | $0.0560798$ | $0.00248723$ |
| $0.4,1.5$ | $0.5,1,0.5$ | $0.00947327$ | $0.000358868$ |

These explicit four-state approximations rule out a one-percent finite-menu separation against all four-state reversible rivals for these particular targets and menus, within the numerical precision of the replay. They do not prove all-protocol approximation.

### Two-spin screen

The two-spin target has equal unit attempt rates. An ordinary reversible three-state rival has one singleton readout sector; both choices of its sign were tested. Its zero-field law has sector masses $1/2,1/2$, and its field-dependent law is the shared Gibbs tilt $\pi_h\propto\pi_0e^{hS}$. At each field, three symmetric conductances are independently free subject to total exit cap three. Thus each sign has seven fitted real parameters, including the split stationary mass. The report retains the feasible generators, stationary laws, and readout explicitly.

For the rational target $J=H=\tfrac12\log2$, the retained ordinary three-state model has maximum occupation error $7.18\times10^{-5}$ on 33 experiments and $5.80\times10^{-5}$ on eight additional fixed pulses. The [exact stationary nonreversible three-state construction](FAMILIAR_SWITCH_STRUCTURE.md) also reproduces this target; floating-point replay agrees to rounding error.

The following table reports the smaller achieved error of the two retained singleton-sign fits for each of twelve further targets. None is an estimate certified to equal the best possible error.

| Coupling $J$ | Field $H=0.5$ | Field $H=1$ | Field $H=2$ |
|---:|---:|---:|---:|
| $0.5$ | $0.000288507$ | $0.000563774$ | $0.000299249$ |
| $1$ | $0.000389332$ | $0.000957314$ | $0.000787648$ |
| $1.5$ | $0.000205723$ | $0.000572672$ | $0.00131285$ |
| $2$ | $0.0000613728$ | $0.000215053$ | $0.000819650$ |

For $J<1.5$, step times were $0.1,0.2,0.5,1,2,5$, and each pulse duration was chosen from $0.2,1,5$. For $J\ge1.5$, step times were $0.2,0.5,1,3,10,30$, write/read times were $0.3,3,10$, and delays were $0.3,3,30$. The longer delays test the slower zero-field mode at stronger coupling. The menus are therefore not identical across every row.

The general exact stationary three-state construction was separately evaluated on all twelve parameter pairs. Its rates were positive, its largest observed exit was below $1.947$, and its target predictions agreed within $2\times10^{-15}$. These checks support implementation of the analytic construction; they do not establish its all-parameter theorem.

## 3. Fixed reevaluation of the largest-residual retained model

The largest error in the table occurs at $J=1.5,H=2$. Its retained ordinary model was subsequently tested without refitting:

| Experiment set | Maximum occupation error |
|---|---:|
| Original 33 fitted experiments | $0.00131285$ |
| Eight fixed additional pulses | $0.00216599$ |
| Thirty-two fixed-seed additional pulses | $0.00270645$ |
| Exact eleven-word menu below, clock one | $0.00471093$ |

The 32 additional triples use seed 73113, independently drawing each duration logarithmically between $0.05$ and $40$. This is a bounded check of one already selected model, not an adversarial or exhaustive protocol search.

The exact menu from the companion theorem uses fields $0,H$, encoded by $0,1$:

$$
1,\ 11,\ 111,\ 1111,\ 11111,\ 10,\ 101,\ 1011,\ 110,\ 1101,\ 11011.
$$

Each letter lasts one time unit. Adjacent equal letters may be merged, so each experiment has at most three constant-field segments and five clock ticks. The companion proof shows that this menu has a positive separation from every three-state ordinarily reversible rival. The gap's numerical size remains unquantified. The retained model's error $0.00471093$ is an achievable numerical upper for this target on that menu, not that positive lower bound.

## 4. Reproducibility and the unresolved practical question

The [saved report](../reports/familiar_switch_screen.json) contains every retained model definition, full generators, stationary preparations, protocol durations and endpoint probabilities. Routine replay uses no optimization:

```bash
.venv/bin/python scripts/screen_familiar_switches.py --verify-saved reports/familiar_switch_screen.json
```

The script fixes numerical library thread counts before importing NumPy and SciPy. Replay checks positivity, stationarity, the relevant detailed balance, the shared cap, affine closure where applicable, and the saved responses. Schema, counts and source/proof hashes must match exactly; floating diagnostics use absolute tolerance $2\times10^{-11}$. Environment versions are recorded as information. Regeneration with `--output` permits a byte comparison under the pinned environment. The optional `--refit` flag repeats the documented bounded local search; optimizer output is not required to be identical across platforms and is not part of routine verification.

The numerical search box does not cover arbitrarily small stationary masses, and successful local termination does not imply global optimality. The stored comparators remain valid feasible models regardless of missed minima. These are floating-point diagnostics, not interval-arithmetic certificates.

The result is therefore mixed in a precise sense: the familiar two-switch model has an exact and finite-menu state advantage by the separate theorem, while the completed screens have not produced a certified practical error margin. A useful next certificate must lower-bound the actual eleven-word error against the full reversible rival class. Another positive local fitting residual would not settle that question.
