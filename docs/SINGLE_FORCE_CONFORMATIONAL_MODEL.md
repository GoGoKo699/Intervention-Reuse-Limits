# A single-force interpretation of the kinetic interface

[Physical source comparison](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) · [Rate robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md) · [Reversal and Markov closure](PHYSICAL_REVERSAL_REALIZATION.md)

**Physical model statement, 23 September 2026.** One applied force can supply both the equilibrium bias and the heterogeneous kinetic response in the original interface. The construction below is exact within a stipulated Bell–Arrhenius network of conformational states. It specifies a recognizable mesoscopic model class and fixes ordinary reversal for configuration states. It does not derive a particular molecular landscape, establish a laboratory implementation, or make the engineered hard networks typical.

## 1. Configurations and one mechanical control

Let a bath have thermal energy $k_B T$, fix an extension scale $\ell>0$, and write the dimensionless force as $h=f\ell/(k_B T)$. A common additive offset in extension is immaterial. Assign the visible state $A$ and hidden conformations $i$ the extensions

$$
x_A=-\ell,\qquad x_i=+\ell.
\tag{1}
$$

The hidden conformations may differ in other coordinates and in their baseline free energies. They share the extension measured by this control. Choose zero-force free energies, in thermal units,

$$
E_A^0=0,\qquad E_i^0=-\log\mu_i,
\tag{2}
$$

where $\mu$ is a strictly positive probability law. Force couples through $-fx$, giving

$$
E_A(h)=h,\qquad E_i(h)=-\log\mu_i-h.
\tag{3}
$$

The equilibrium partition function is $2\cosh h$. Consequently the equilibrium hidden mass is $(1+\tanh h)/2$, its conditional law is $\mu$, and the mean binary readout is $\tanh h$. At zero force, use this equilibrium preparation.

For the external transition $A\leftrightarrow i$, assign a transition-state extension

$$
x_{Ai}^{\ddagger}=g_i\ell.
\tag{4}
$$

When $|g_i|<1$, it lies between the two well extensions. Distinct transition-state positions are the heterogeneous kinetic information. Let $k>0$ be the baseline escape rate and let $\nu>0$ be a common attempt frequency. Put

$$
W_{Ai}^0=-\log\mu_i+\log(\nu/k),\qquad
W_{Ai}(h)=W_{Ai}^0-g_i h.
\tag{5}
$$

The stipulated transition-state rule $q_{xy}=\nu\exp(E_x-W_{xy})$ then gives exactly

$$
\boxed{
q_{Ai}(h)=k\mu_i e^{(1+g_i)h},\qquad
q_{iA}(h)=k e^{(g_i-1)h}.}
\tag{6}
$$

Thus a single force changes both well populations and escape kinetics. Two separately operated controls are unnecessary in this rate-level model. The equal zero-force escape rates are an explicit calibration condition in (5), not a generic consequence of mechanical forcing.

## 2. Hidden exchange and ordinary reversal

Let $K$ be any hidden generator with ordinary detailed balance under $\mu$. For each present hidden edge define its symmetric conductance $c_{ij}=\mu_iK_{ij}=\mu_jK_{ji}$ and set

$$
W_{ij}^0=\log(\nu/c_{ij}),\qquad
x_{ij}^{\ddagger}=\ell,\qquad
W_{ij}(h)=W_{ij}^0-h.
\tag{7}
$$

Substitution gives $q_{ij}(h)=K_{ij}$. Hidden wells and hidden transition states move together in free energy under this force. The hidden generator therefore remains independent of control. Absent edges are omitted.

For a bounded force interval and bounded rates, one may choose $\nu$ above every directed rate on that interval. Then every barrier exceeds both adjacent well free energies. In the original band-$[k,3k]$ targets with $|g|\le G$ and $|h|\le H$, choosing $\nu>\max(3k,k e^{(1+G)H})$ suffices. Raising this arbitrary attempt frequency adjusts the represented barriers; it is not an experimentally derived microscopic frequency.

All retained variables here are conformational configurations and extension coordinates, which are even under physical time reversal. At a fixed force, equilibrium therefore requires ordinary detailed balance. A word-reversal involution exchanging artificial memory states cannot be assigned to these configurations just by renaming them. The [Markov-closure note](PHYSICAL_REVERSAL_REALIZATION.md) explains why an exactly Markov projection onto even configurations also retains ordinary detailed balance, even if eliminated microscopic variables include momenta.

This fixes the physical meaning of the ordinary-reversibility restriction for the stipulated class. It does not exclude realizations that retain genuine reversal-odd variables; the earlier generalized-reversal polynomial predictor remains a valid mathematical boundary.

## 3. Which part of the physical assumption has precedent?

The [source audit](PHYSICAL_REALIZATION_SOURCE_AUDIT.md) identifies primary papers, the inspected statements, and the limits of each comparison. Bell's force-dependent activated rates and the separation of equilibrium well energies from kinetic transition-state positions are established. Dudko, Hummer and Szabo's force-spectroscopy treatment also makes the instantaneous-rate and fixed-barrier approximations explicit; a general smooth landscape need not obey (6) exactly at finite force or rapid driving. Conformational models with a common equilibrium bias and force-independent internal exchange provide closer network-level precedents.

The mathematical construction adds specific restrictions to those ingredients:

| Stipulation | Role in the prediction task | What has not been established |
|---|---|---|
| One gateway $A$ and an ensemble of hidden conformations | A common return hub gives renewal; a return-rate lower bound gives uniform response bounds | A particular molecular species realizing every required edge |
| Equal hidden extension $+\ell$ | One equilibrium block tilt, independent of hidden conformation | Exact equality for a generic biomolecule |
| Equal zero-force hidden escape rate $k$ | Exact passive two-state visible process | Genericity or calibration cost |
| Heterogeneous external transition-state positions | Force breaks the passive lumping | Arbitrary independent positioning of many saddles in one spatial landscape |
| Hidden wells and saddles have the same extension | Force-independent hidden $K$ | Validity beyond the selected force range |
| Even retained conformations and a single equilibrium bath | Ordinary detailed balance at fixed force | Physical realization of the alternative word parity |

The complete address-and-table target still has its explicit state and edge complexity. These assignments do not make that graph spatially local or provide a compact mechanical machine. State free energies may include unresolved entropy, so (2) is not automatically a microscopic potential-energy specification.

## 4. Robustness and finite switching times

Let a reference network have hidden exit cap $Bk$, return rates at least $kb_{\min}>0$, return factors at most $b_{\max}$ and entry density factors at most $c_{\max}$. Set $L=\max(B+b_{\max},c_{\max})$. If a nearby network on the same counted states has logarithmic rate errors at most $\zeta$ on the same support, the [uniform perturbation theorem](PHYSICAL_INTERFACE_ROBUSTNESS.md) gives, with identical preparation and readout,

$$
\sup_{h,T}|\widetilde m[h,T]-m[h,T]|
\le\min\{2,2L(e^\zeta-1)/b_{\min}\}.
\tag{8}
$$

The nearby model may have weakly control-dependent hidden exchange or weakly unequal passive returns. Initial preparation errors must be added if its equilibrium weights change. Finite ramps at a fixed switching clock also have an explicit uniform error bound in that note.

These results turn each finite prediction certificate into a nonzero neighborhood of rate models. At a fixed nonzero defect or ramp width, they give an accuracy floor. They do not establish the original asymptotic growth law at arbitrarily small error while laboratory defects remain fixed, or verify the instantaneous-rate approximation from microscopic mechanics.

## 5. Research assessment

The force construction answers a specific modeling question: a single conventional mechanical control can have the required thermodynamic and kinetic effects, with ordinary parity fixed by retained configurations. This is more specific than an abstract local-balance ratio, but remains a stipulated mesoscopic network.

A credible PRL case still needs the quantitative prediction result to matter within such a model class. A small certified state advantage is directly relevant; a feasible molecular design, useful error tolerance, measurement cost and a microscopic derivation would be further achievements. Neither this interpretation nor a bibliography alone establishes those claims.
