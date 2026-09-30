# Physical rate representations and uniform interface robustness

[Kinetic-interface separation](CAPPED_KINETIC_INTERFACE_SEPARATION.md) · [General entropy comparison](GENERAL_INTERFACE_ENTROPY_BOUND.md) · [Reversal convention](GENERALIZED_REVERSAL_PREDICTION.md) · [Kinetic/parity source audit](KINETIC_PARITY_SOURCE_AUDIT.md)

**Research theorem and physical scope, 23 September 2026.** Small rate errors around the hub-interface models give uniformly small endpoint-response errors, even when the errors introduce control-dependent hidden dynamics or break exact local balance. The relevant constant is set by return to the visible hub. This supplies a quantitative neighborhood of the existing state-complexity results, with an explicit accuracy floor at fixed perturbation size.

Every finite ordinarily reversible target also has an exact Arrhenius representation on its state graph. That algebraic representation establishes consistency of a rate model. It does not construct a small molecular device, a spatially local energy landscape, or an efficient actuator. No manuscript is drafted here, and the earlier proof notes remain unchanged.

## 1. Exact Arrhenius representation on a finite graph

Use thermal units, so energies below are dimensionless energies or state free energies divided by the bath thermal energy. For an ordinarily reversible finite generator $`Q(h)`$, choose positive equilibrium weights $`\pi_h`$ and set

**Equation (1).**

```math
E_x(h)=-\log\pi_h(x)+c(h).
```

For an allowed undirected edge $`\{x,y\}`$ choose a symmetric attempt frequency $`\nu_{xy}=\nu_{yx}\gt 0`$ and define

**Equation (2).**

```math
W_{xy}(h)=E_x(h)-\log\frac{q_{xy}(h)}{\nu_{xy}}.
```

Detailed balance gives $`E_x-E_y=\log(q_{xy}/q_{yx})`$, hence $`W_{xy}=W_{yx}`$ and

**Equation (3).**

```math
q_{xy}(h)=\nu_{xy}\exp[E_x(h)-W_{xy}(h)].
```

Absent edges are omitted, equivalently assigned infinite barriers. If both edge rates are uniformly bounded over the control set, the attempt frequency can be chosen above both bounds, ensuring $`W_{xy}\ge\max(E_x,E_y)`$. This is a representation of rates, not a derivation of an attempt frequency or barrier from microscopic mechanics.

For the repository's equilibrium interface,

**Equation (4).**

```math
q_{iA}(h)=k b_i(h),\qquad q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
```

one convenient gauge is

**Equation (5).**

```math
E_A(h)=h,\qquad E_i(h)=-h-\log\mu_i.
```

The external barriers are explicitly

**Equation (6).**

```math
W_{Ai}(h)=-h-\log\mu_i-\log\frac{kb_i(h)}{\nu_{Ai}}.
```

For the original $`b_i(h)=e^{(g_i-1)h}`$ this is a baseline barrier minus $`g_i h`$. If the hidden $`K`$ is reversible under $`\mu`$ and independent of $`h`$, its internal barriers can be chosen as

**Equation (7).**

```math
W_{ij}(h)=-h-\log\mu_i-\log\frac{K_{ij}}{\nu_{ij}};
```

they shift together with the hidden well energies, leaving the hidden rates unchanged. Arbitrary symmetric perturbations of these barriers retain ordinary detailed balance with the same equilibrium law, although they can make hidden rates control dependent.

Equations (1)–(7) are elementary finite-graph identities. The standard well/barrier rate description is discussed by Rahav, Horowitz and Jarzynski, *Physical Review Letters* **101**, 140602 (2008), [primary text](https://arxiv.org/pdf/0808.0015v2), p. 1 and Eq. (3). It does not assert that every graph and every measurable control dependence can be produced by one natural physical actuator.

## 2. Ordinary configurations and physical interpretation

When the retained variables are overdamped positions, chemical populations or conformations with no retained odd variable, the physical reversal fixes the state labels and reverses the sequence of transitions. This is the ordinary reversal used by the capped state lower and the identity-EPR frontier. A chemical master equation with molecule-number states and internal conformations treated as distinct states is a standard setting; see Schmiedl and Seifert, *Journal of Chemical Physics* **126**, 044101 (2007), [primary text](https://arxiv.org/pdf/cond-mat/0605080v2), Secs. II.A and V.

The assertion is conditional on the physical variables retained. Momentum, current-like memory or other odd variables require their actual reversal. The [centered-word construction](GENERALIZED_REVERSAL_PREDICTION.md) uses a nontrivial mathematical involution and therefore prevents a convention-independent interpretation of the ordinary lower. Renaming its word states as chemical species would not by itself make word reversal their physical time reversal.

An exact graph representation can use as many well states and edges as the original construction. The present target includes a hub connected to the hidden configurations, refresh transitions and a large address-and-table system. Equations (6)–(7) do not remove those costs, demonstrate spatial locality, or explain how one scalar laboratory control realizes all prescribed barrier changes. State free energies may encode unresolved degeneracy; calling them microscopic energies would require additional modeling.

A derivation from an overdamped metastable landscape requires further assumptions. Falasco and Esposito, *Physical Review E* **103**, 042114 (2021), [primary text](https://arxiv.org/pdf/2101.03968), Sec. II.C and Sec. IV, derive local detailed balance under specified weak-noise/metastability conditions; their time-dependent extension requires separation from intrabasin equilibration and persistence of the metastable structure. The arbitrary finite-graph rate identity does not establish those assumptions, especially under rapid control changes.

The defensible claim here is an ordinarily reversible, single-bath-compatible rate network with a specified kinetic actuator. A natural low-dimensional device realization and its control-work accounting remain separate tasks.

## 3. A uniform perturbation theorem from one reference reset

Let $`Q_t`$ and $`\widetilde Q_t`$ be finite row generators on the same state space. They may depend on an arbitrary deterministic protocol. Assume their rates are measurable and locally bounded along each protocol. Let $`P(s,t)`$ and $`\widetilde P(s,t)`$ be their propagators. Suppose only the reference admits a common rate-$`\alpha`$ reset to a fixed hub $`A`$:

**Equation (8).**

```math
Q_t=Q_t^{\rm res}+\alpha(\Pi_A-I),\qquad \alpha\gt 0,
```

where $`Q_t^{\rm res}`$ is a generator. For a hub interface, (8) follows from $`q_{iA}(t)\ge\alpha`$ for every hidden state. The reset is a no-op at $`A`$.

For the difference $`\Delta_t=\widetilde Q_t-Q_t`$, define the generator-row defect

**Equation (9).**

```math
\eta=\sup_{t,x}\frac12\sum_y|\Delta_t(x,y)|.
```

The diagonal is included. This quantity has units of inverse time. It equals

```math
\max\left\{\sum_{y\ne x}(\Delta_t(x,y))_+,\;
\sum_{y\ne x}(-\Delta_t(x,y))_+\right\}
```

in each row, and is bounded by the off-diagonal absolute row sum. It need not bound either generator's absolute rate.

Let the initial laws have total-variation distance $`d_0`$. Then

**Equation (10).**

```math
\boxed{
\|\widetilde p(T)-p(T)\|_{\rm TV}
\le e^{-\alpha T}d_0+
\frac\eta\alpha(1-e^{-\alpha T}).}
```

For readouts $`S,\widetilde S\in[-1,1]`$ with $`\|\widetilde S-S\|_\infty\le e_S`$,

**Equation (11).**

```math
|\widetilde m(T)-m(T)|
\le e_S+2e^{-\alpha T}d_0+
\frac{2\eta}\alpha(1-e^{-\alpha T}),
```

and the all-horizon bound is $`\min\{2,e_S+2\max(d_0,\eta/\alpha)\}`$. No stationarity, local balance, hidden-rate cap or field independence is required of $`\widetilde Q_t`$.

**Proof.** Coupling two reference processes with the same Poisson resets gives, for every zero-mass signed row $`v`$,

**Equation (12).**

```math
\|vP(s,t)\|_{\rm TV}\le e^{-\alpha(t-s)}\|v\|_{\rm TV}.
```

Variation of constants gives the exact identity

**Equation (13).**

```math
\widetilde p(T)-p(T)=
(\widetilde p(0)-p(0))P(0,T)
+\int_0^T\widetilde p(s)\Delta_sP(s,T)\,ds.
```

Each $`\widetilde p(s)\Delta_s`$ has total mass zero and TV norm at most $`\eta`$. Applying (12) proves (10). The readout range proves (11). All constants are uniform over protocols if (8)–(9) are uniform over their allowed controls. This is an endpoint estimate; complete path laws can separate over long observation times.

## 4. Two refinements when both models retain the reset

If $`\widetilde Q_t`$ also has the same reset component, a common-reset coupling gives the sharper bound

**Equation (14).**

```math
\|\widetilde p(T)-p(T)\|_{\rm TV}
\le d_0e^{-(\alpha+\eta)T}
+\frac\eta{\alpha+\eta}(1-e^{-(\alpha+\eta)T}).
```

At a common state, locally uniformize the two residual rows at a shared rate and maximally couple their next-state distributions, including their self-loop probabilities. Their separation hazard is at most (9). At distinct states, the shared reset reunites them at rate $`\alpha`$. For mismatch probability $`z`$, this gives $`\dot z\le\eta(1-z)-\alpha z`$. Initial maximal coupling and integration prove (14). The diagonal term in (9) is needed when the exit rates differ.

A different refinement replaces the maximum hidden defect by its stationary average. Suppose the reference hidden block $`K_t`$ is stationary under the same positive $`\mu`$ at every time, and its full interface obeys

```math
q_{iA}(t)\ge\alpha,\qquad q_{Ai}(t)\le\beta\mu_i,
\qquad p_i(0)\le c_0\mu_i.
```

The full hidden-density equation and the maximum principle give

**Equation (15).**

```math
\max_i p_i(t)/\mu_i
\le c_0e^{-\alpha t}+(\beta/\alpha)(1-e^{-\alpha t})
\le C,\qquad C=\max(c_0,\beta/\alpha).
```

Write $`d_x(t)=\frac12\sum_y|\Delta_t(x,y)|`$ and assume

```math
d_A(t)\le\eta_A,\qquad
\sum_i\mu_i d_i(t)\le\eta_\mu.
```

Use the Duhamel orientation with $`p(s)\Delta_s\widetilde P(s,T)`$, and use the perturbed model's reset for its contraction. Equation (15) then gives

**Equation (16).**

```math
\|\widetilde p(T)-p(T)\|_{\rm TV}
\le e^{-\alpha T}d_0+
\frac{\eta_A+C\eta_\mu}{\alpha}(1-e^{-\alpha T}).
```

No minimum stationary mass enters. This bound permits large row errors concentrated on sufficiently rare reference states, provided the displayed weighted defect remains small. Unlike (10), this refinement uses both the reference occupation bound and a reset in the perturbed process.

## 5. Rate and barrier tolerances with explicit constants

For the dimensionless physical interface, suppose reference hidden exits are at most $`Bk`$ and

```math
b_i(h)\ge b_{\min}\gt 0,\qquad
b_i(h)\le b_{\max},\qquad e^{2h}b_i(h)\le c_{\max}.
```

Then $`\alpha=kb_{\min}`$ and every full reference exit is at most $`kL`$, where

**Equation (17).**

```math
L=\max\{B+b_{\max},c_{\max}\}.
```

If every off-diagonal rate satisfies

**Equation (18).**

```math
|\widetilde q_{xy}(h)-q_{xy}(h)|\le\epsilon q_{xy}(h),
```

then $`\eta\le\epsilon kL`$. With common preparation and readout,

**Equation (19).**

```math
\boxed{\sup_{h,T}|\widetilde m[h,T]-m[h,T]|
\le\min\{2,2\epsilon L/b_{\min}\}.}
```

The relative bound preserves absent edges; new edges can instead be included through their absolute row-rate contributions in (9). Rates need not retain the original common ratio or field-independent hidden block. A uniform logarithmic rate error $`|\log(\widetilde q_{xy}/q_{xy})|\le\zeta`$ on the same support implies (18) with $`\epsilon=e^\zeta-1`$.

In the Arrhenius representation, bounds $`|\widetilde E_x-E_x|\le e`$, $`|\widetilde W_{xy}-W_{xy}|\le w`$ and $`|\log(\widetilde\nu_{xy}/\nu_{xy})|\le v`$ imply $`\zeta\le e+w+v`$. Symmetric perturbed barriers and attempt frequencies preserve ordinary detailed balance for the perturbed energies, but neither symmetry nor detailed balance is needed for (19). If equilibrium preparation changes with the energies, its actual initial TV error must also be included through (11); it is not silently set to zero.

The sharper same-exit special case uses $`\eta=\frac12\max_x\sum_{y\ne x}|\Delta(x,y)|`$. In particular $`K_\epsilon=(1-\epsilon)K+\epsilon K^*`$ with hidden exits at most $`Bk`$ has $`\eta\le\epsilon Bk`$, recovering the previously proved mean bound $`2\epsilon B/b_{\min}`$.

### Finite ramps at a fixed switching clock

The same argument permits errors that are large but occur only during short ramps. Suppose an ideal protocol changes only at ticks $`j\tau`$, where $`\tau=a/k\gt 0`$. Fix a deterministic rule mapping each command word to its realized ramped protocol. The realized protocol agrees with the ideal one outside intervals $`[j\tau,j\tau+w]`$ of duration $`0\le w\le\tau`$, and its generator-row error on those intervals is at most $`\eta_{\rm ramp}`$, uniformly over command words. Preparation and readout are common. The reference reset throughout the comparison still suffices, and (13) gives

**Equation (19a).**

```math
\|\widetilde p(T)-p(T)\|_{\rm TV}
\le\eta_{\rm ramp}\int_0^T e^{-\alpha(T-s)}
1_{\rm ramps}(s)\,ds.
```

Dominating by a ramp at every tick, the convolution increases during each ramp and decreases between ramps. Its successive ramp-end maxima form a geometric sum with ratio $`e^{-\alpha\tau}`$. Therefore

**Equation (19b).**

```math
\boxed{
\sup_T|\widetilde m(T)-m(T)|
\le\min\left\{2,
\frac{2\eta_{\rm ramp}}\alpha
\frac{1-e^{-\alpha w}}{1-e^{-\alpha\tau}}\right\}.}
```

This tends to zero linearly in $`w`$ at each fixed clock. The number of past switches and the horizon do not enter. Additional rate errors outside ramps can be bounded separately through the same integral. A fixed nonzero ramp width contributes an accuracy floor in the lower-bound transfer below; arbitrary-accuracy conclusions require a correspondingly controlled width.

For a fixed hidden $`K`$ and any two control values within the bounds of (17), only the external rows change. Their defect is at most $`k\max(b_{\max},c_{\max})`$. Thus a continuous ramp staying within the allowed control interval has an explicit $`\eta_{\rm ramp}`$ even if no field derivative bound is available. An instantaneous-rate approximation to a microscopic system requires its own justification; (19b) compares the two specified Markov generators. It does not give a vanishing error if the ramp duration remains a nonzero fraction of a clock tending to zero.

## 6. Transfer to nearby targets and nearby competitor classes

Fix a core competitor class $`\mathcal C`$, such as the bounded kinetic-interface ordinary-reversible class. Suppose each model in an enlarged class $`\mathcal C_\rho`$ has a core model on the same counted states, with the same prescribed readout/preparation or explicit errors in (11), whose entire controlled mean is within $`\rho_C`$. Rate neighborhoods certified by (10) are one sufficient definition. They can allow weak field dependence of hidden dynamics or weak local-balance errors, but not arbitrary uncontrolled changes.

If a perturbed target $`\widetilde F`$ has controlled-mean distance at most $`\rho_T`$ from a reference $`F`$, triangle inequalities give, target by target,

**Equation (20).**

```math
\boxed{
D_{\mathcal C_\rho}(\widetilde F,\delta)
\ge D_{\mathcal C}(F,\delta+\rho_T+\rho_C).}
```

Indeed a nearby-class predictor accurate to $`\delta`$ for $`\widetilde F`$ has a same-state core predictor accurate to the displayed sum for $`F`$. Taking the supremum over paired target families preserves this implication. A core upper accurate to $`\delta-\rho_T`$ also predicts $`\widetilde F`$ to $`\delta`$ when $`\delta\gt \rho_T`$, provided that predictor is admitted by the selected competitor class.

For the capped core class, (20) retains its $`\exp(c\varepsilon^{-\gamma})`$ ordinary-core necessity with $`\varepsilon=\delta+\rho_T+\rho_C`$ in the theorem's small-error regime. The uncapped core retains its weaker fifth-root-log lower. If the enlarged class is required to be ordinarily reversible at every field, intersect the rate neighborhood with that condition. If it permits slight balance violations, describe it as a neighborhood of ordinary-reversible models; calling every member reversible would be incorrect.

At a fixed nonzero defect size, the certified lower stops at an accuracy floor of order $`\rho_T+\rho_C`$. It does not prove asymptotic divergence as $`\delta\downarrow0`$ with those defects held fixed. If $`\rho_T+\rho_C=O(\delta)`$, the known growth classes persist with adjusted constants. Equivalently each finite target witness has an explicit nonzero tolerance neighborhood; that neighborhood can shrink with target width. This is a structural stability theorem, not a demonstration of a useful small experimental instance.

## 7. Two controls that erase the intended hidden prediction problem

Kinetic freedom matters; ordinary equilibrium consistency alone does not make a target hard. Suppose the only control changes entrance rates $`q_{Ai}(t)=a_i(t)`$ while every hidden state has the same return rate $`q_{iA}(t)=b(t)`$. Regardless of hidden transitions, the visible-block law closes exactly:

**Equation (21).**

```math
\dot p_A(t)=b(t)[1-p_A(t)]-p_A(t)\sum_i a_i(t).
```

The partition is strongly lumpable even under time-dependent control, so its complete visible law has a two-state Markov realization. A ligand-only association control with common dissociation rate has this form. It does not implement the state-dependent controlled return rates used by the separation.

Likewise, if a protocol changes only barriers while keeping one common equilibrium distribution $`\pi`$ fixed, and the system starts at $`\pi`$, then $`\pi Q_t=0`$ at every time and $`p(t)=\pi`$. Every endpoint mean is constant. This elementary endpoint statement is distinct from more general cyclic no-pumping theorems.

The present target uses both a changing equilibrium block bias and distinguishable kinetic barriers. The robustness theorem quantifies small deviations from that interface; it does not turn either of these different control architectures into a hard target. Nor does it establish a universal heat, work or dissipation lower bound.
