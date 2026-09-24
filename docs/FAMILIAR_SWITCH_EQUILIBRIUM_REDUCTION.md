# Why an equilibrium reduction inherits the same force

The common Gibbs tilt is not an additional kinetic restriction for a
fixed coarse description that retains the measured binary variable and
its physical conjugate field. It follows directly by summing equilibrium
weights. Ordinary detailed balance is also retained by stationary-flux
aggregation, although that aggregation need not reproduce the projected
dynamics.

These are standard equilibrium and coarse-graining facts. Their role here
is to explain the physical comparison class of the four-word result.
They do not prove that every smaller abstract predictor is a physical
coarse-graining, or that a finite Markov closure exists after eliminating
states. The existing circulating three-state predictor remains a
mathematical response realization.

[Physical assumption ledger](PHYSICAL_ASSUMPTION_ALIGNMENT.md) ·
[Charge energy and rates](FAMILIAR_SWITCH_CHARGE_REALIZATION.md) ·
[Minimal four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md) ·
[Four-word state theorem](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md) ·
[Relative-force robustness](FAMILIAR_SWITCH_RELATIVE_FORCE_ROBUSTNESS.md) ·
[Markov closure and physical reversal](PHYSICAL_REVERSAL_REALIZATION.md) ·
[Stochastic Bayes aggregation](SOFT_AGGREGATION_LOWER_BOUND.md)

## 1. The physical input is the controlled energy

Let $x$ range over a finite state space, with a deterministic observable
$S(x)\in\{-1,+1\}$. At fixed temperature $T$, suppose the relevant
energy or grand energy is

$$
 E_h(x)=E_0(x)-k_{\rm B}T\,hS(x).
 \tag{1}
$$

A field-dependent additive constant could be included; it cancels from
all normalized equilibrium probabilities. Fixed state degeneracies or
field-independent statistical weights can be absorbed into $E_0$.
Writing $\beta=(k_{\rm B}T)^{-1}$, the positive equilibrium laws obey

$$
 \pi_h(x)=\frac{\pi_0(x)e^{hS(x)}}{Z(h)},\qquad
 Z(h)=\sum_x\pi_0(x)e^{hS(x)}.
 \tag{2}
$$

Equation (1), rather than detailed balance alone, specifies what the
control physically changes. In the selected charge model the controlled
occupation has $S=2n_1-1$; changing its addition energy by
$-2k_{\rm B}T\,h$ gives (1), up to an additive constant, when the
other energy parameters remain fixed. The published sequential-tunneling
model and the control qualifications are recorded in the linked charge
note and assumption ledger.

Changing barriers may alter rates without changing (2). Conversely,
uncompensated changes in spectator energies can change (2), even if the
system remains reversible at each field. The equilibrium force rule and
kinetic reversibility therefore have distinct physical premises.

## 2. Fixed partitions retain the same free-energy coupling

Let $f:X\to A$ be a field-independent partition, and suppose its retained
labels have a deterministic binary readout $s(a)$ satisfying

$$
 S(x)=s(f(x)).
 \tag{3}
$$

Thus each cell $C_a=f^{-1}(a)$ lies entirely within one readout sector.
Its unnormalized equilibrium weight and free energy are

$$
 z_a(h)=\sum_{x\in C_a}e^{-\beta E_h(x)},\qquad
 F_h(a)=-k_{\rm B}T\log z_a(h).
$$

Factor the constant sign out of this sum:

$$
 z_a(h)=e^{hs(a)}z_a(0),\qquad
 \boxed{F_h(a)=F_0(a)-k_{\rm B}T\,hs(a).}
 \tag{4}
$$

The entropic contribution from the eliminated states is already inside
$F_0(a)$. It does not generate an extra field dependence, because the
field couples to the same value of $S$ throughout the cell. Consequently
the aggregated law $q_h(a)=\sum_{x\in C_a}\pi_h(x)$ satisfies

$$
 \boxed{q_h(a)=\frac{q_0(a)e^{hs(a)}}
                        {\sum_bq_0(b)e^{hs(b)}}.}
 \tag{5}
$$

No equal cell masses, separation of timescales, or dynamical closure was
used. Any fixed refinement of the readout partition has this property.
Within a cell, the conditional equilibrium distribution is independent
of $h$:

$$
 \pi_h(x\mid C_a)=\frac{\pi_0(x)}{q_0(a)},
 \qquad x\in C_a.
\tag{6}
$$

The equilibrium log-sum free energy is standard; see Strasberg and
Esposito, *Physical Review E* **95**, 062101 (2017),
[primary text](https://arxiv.org/pdf/1703.05098), Section II C,
Eqs. (26)--(28). Their dynamical closure invokes timescale separation.
Only the equilibrium sum is used in (4)--(6); no such closure is being
inferred here.

These identities explain the interface requirement on an equilibrium
reduced model: it retains the same measured coordinate as the variable
conjugate to the applied field. For a fresh reduced model with no known
partition map, imposing this same free-energy coupling is a declared
physical modeling requirement; it is not inferred merely from a fit to
the observed pair tables.

## 3. A field-independent stochastic encoder has the same inheritance

The stationary statement is not limited to disjoint cells. Let $C(x,a)$
be a row-stochastic, field-independent encoder, with labels of zero
stationary mass removed. Require exact readout compatibility,

$$
 \sum_a C(x,a)s(a)=S(x)\quad\text{for every }x.
 \tag{7}
$$

Since both readouts are binary, an average equals $+1$ or $-1$ only
when every label of positive weight has that same sign. Thus (7) is
equivalent to

$$
 C(x,a)>0\ \Longrightarrow\ s(a)=S(x).
 \tag{8}
$$

Set $q_h=\pi_h C$. Substituting (8) into (2) proves (5) again.
Moreover the Bayes reverse channel is field independent:

$$
 B_h(a,x)=\frac{\pi_h(x)C(x,a)}{q_h(a)}
         =\frac{\pi_0(x)C(x,a)}{q_0(a)}=:B(a,x).
 \tag{9}
$$

Thus the stationary decoder cannot acquire an extra field dependence
under these exact assumptions. For a stochastic encoder, the weighted
sum $\sum_xC(x,a)e^{-\beta E_h(x)}$ has the same factorization as
(4). This is an equilibrium representation of the encoded labels; it
does not by itself supply a physical implementation or thermodynamic
cost for randomized encoding.

The conditions are consequential. If a cell mixes the two signs, its
weight has the form $A_a e^h+B_a e^{-h}$, with both coefficients
positive. Its free energy then has a nonlinear field dependence and it
does not carry one exact deterministic value of the original readout.
If instead the encoder depends on $h$, then even sector-preserving
encoding can redistribute weight among labels within a sector as the
field changes. Formula (5) no longer follows for one fixed $q_0$.
Matching only an equilibrium mean is weaker than the pointwise
readout compatibility in (7).

## 4. Reversible flux aggregation is a model, not a closure theorem

Suppose the microscopic generator $Q_h$ obeys ordinary detailed balance
for $\pi_h$. For a deterministic partition as in Section 2, define
off-diagonal coarse rates by stationary flux:

$$
 \overline Q_h(a,b)=\frac1{q_h(a)}
       \sum_{x\in C_a,\,y\in C_b}\pi_h(x)Q_h(x,y),
 \qquad a\ne b,
 \tag{10}
$$

and set diagonal entries by zero row sums. All off-diagonal rates are
nonnegative. Summing microscopic detailed balance gives

$$
 q_h(a)\overline Q_h(a,b)
 =q_h(b)\overline Q_h(b,a).
 \tag{11}
$$

Together, (5) and (11) place this reduced generator in precisely the
ordinary equilibrium/force class used by the four-word lower bound.
This holds without a universal bound on microscopic or coarse rates.

Equation (10) matches stationary instantaneous fluxes. It need not
match finite-time transitions or the responses to a sequence of fields.
One sufficient condition for exact controlled closure is strong
lumpability at each allowed field: the total rate
$\sum_{y\in C_b}Q_h(x,y)$ must be independent of the choice of
$x\in C_a$. Then $Q_hC=C\overline Q_h$, where $C$ is the
partition indicator matrix; exponentiating and multiplying these
intertwining identities gives the exact same coarse dynamics under any
sequence of the allowed fields. Without such a closure condition,
the projected process can retain history in its within-cell distribution.

This distinction is explicit in Esposito, *Physical Review E* **85**,
041125 (2012), [primary text](https://arxiv.org/pdf/1112.5410),
Section III: Eqs. (31)--(32) contain the evolving conditional microscopic
distribution, while Eqs. (34), (37), and (39) give its equilibrium
specialization and effective detailed balance under the stated closure
conditions.

There is also a useful necessary statement. A deterministic projection
of a stationary ordinarily reversible process has a time-reversal
invariant path law. If that projected process is itself an autonomous
Markov process, its two-time probabilities and hence its generator obey
ordinary detailed balance. The linked physical-reversal note gives the
proof and its generalization to reversal-even observations. An
equilibrium projection cannot become a nonreversible Markov chain merely
by discarding even hidden coordinates.

For the stochastic encoder of Section 3, if $K_h$ is a reversible
stochastic kernel, then

$$
 \overline K_h=BK_hC
 \tag{12}
$$

is a stochastic kernel, stationary and reversible for $q_h$. Indeed,

$$
 q_h(a)\overline K_h(a,b)
 =\sum_{x,y}\pi_h(x)C(x,a)K_h(x,y)C(y,b),
$$

which is symmetric in $a,b$. Again, the inherited law is (5).
Using these coarse kernels successively is a declared Markov
approximation; it does not prove equality with consecutive microscopic
operations. Inserting $CB$ between two microscopic kernels can change
their endpoint law.

In continuous time one must not simply substitute $Q_h$ for $K_h$ in
(12): $BQ_hC$ need not have nonnegative off-diagonal entries. For example,
take four equally weighted states, $Q=\mathbf1\pi-I$,
$S=(-1,-1,+1,+1)$, retained signs $s=(-1,-1,+1)$, and

$$
 C=\begin{pmatrix}
 1/2&1/2&0\\1/2&1/2&0\\0&0&1\\0&0&1
 \end{pmatrix}.
 \qquad (BQC)_{12}=-\frac14.
 \tag{13}
$$

This is an exactly readout-compatible four-to-three stochastic map of
a reversible generator, yet the naive generator compression fails.
The existing stochastic Bayes note gives a valid uniformization
construction with an additional resampling term. That declared
architecture is not an exact dynamics theorem for arbitrary encoding.

## 5. Relative force errors do not grow under the equilibrium map

Suppose a microscopic high-field law has a residual factor beyond the
ideal force:

$$
 \pi_H(x)\ \propto\ \pi_0(x)e^{HS(x)}r(x),\qquad
 0<r_{\min}\le r(x)\le r_{\max}.
 \tag{14}
$$

For the same field-independent readout-compatible encoder,

$$
 q_H(a)\ \propto\ q_0(a)e^{Hs(a)}R(a),\qquad
 R(a)=\sum_xB(a,x)r(x),
 \tag{15}
$$

where $B$ is the zero-field Bayes channel. It is a convex average, so

$$
 r_{\min}\le R(a)\le r_{\max},\qquad
 \frac{\max_aR(a)}{\min_aR(a)}
 \le\frac{r_{\max}}{r_{\min}}.
 \tag{16}
$$

No lower bound on a coarse stationary mass is needed. Thus the existing
relative-force tolerance $1001/1000$ is inherited without amplification
by such a reduction. A residual energy change
$\Delta E(x)$ gives $r(x)=e^{-\beta\Delta E(x)}$, so its likelihood
spread is controlled by $e^{\beta\operatorname{osc}(\Delta E)}$.
This is a derivation of an error propagation rule, not an assertion that
a particular apparatus meets the project's tolerance. In the perturbed
case, (9)'s exact field independence of the Bayes decoder is not generally
preserved; (15)--(16) use $B$ only as a zero-field averaging identity.

## 6. Consequence for the three-state fit

The [minimal four-word theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md)
proves the exact three-versus-four state result for every finite positive
coupling, field and pair of pulse durations in the equal-attempt
two-switch family. Its two target residuals have opposite nonzero signs,
and its accuracy interval is positive for each fixed parameter choice.
Its ordinary lower permits arbitrary preparation for each word.

At the selected operating point, the certified one-percent kinetic
neighborhood has the quantitative residual bounds
$\mathcal R_->.009$ and $\mathcal R_+<-.009$. The existing
four-word certificate excludes every ordinary model with at most three
states, fixed kernels, deterministic binary readout, positive stationary
laws and the common force rule through maximum pair-table TV tolerance
$.001$. With the inherited relative-force spread $1001/1000$, the
corresponding exclusion holds through tolerance $.0009$. These numerical
neighborhoods are not asserted uniformly over the generic theorem's
parameter family.

Consequently a three-state reduction that preserves the equilibrium
force/observation interface and ordinary detailed balance cannot
reproduce those four pair laws. This includes the partition and
stationary-Bayes constructions above, and is stronger than a failure
of any one aggregation algorithm: the lower also covers fresh ordinary
models with no prescribed relation to microscopic states.

For an exact three-state **fixed Markov** fit with the same deterministic
readout, at least one of ordinary detailed balance and the common
stationary force rule must fail. If that fit also retains the inherited
force rule, it must violate ordinary detailed balance. The existing
three-state realization does retain that rule and fits all four pair
laws, so its nonreversible circulation is essential to its membership
in the smaller predictive class. Its abstract hidden states are not
established as a passive equilibrium coarse-graining or as a realized
three-state device.

Other descriptions can leave the compared class by retaining memory
beyond a finite Markov state, using a field-dependent encoding, changing
the conjugate observable, allowing stochastic emissions instead of the
faithful binary readout, or changing the physical reversal structure.
Those are distinct model choices. This derivation does not rule out
every three-state physical device with different couplings, and it does
not assign an energy, dissipation, hardware, or full-trajectory cost to
the mathematical predictor.

The interpretation supported here is specific: equilibrium-preserving
reduction of the same controlled binary coordinate inherits the shared
force rule. Keeping that rule and ordinary equilibrium kinetics has a
larger state requirement for the selected four-word task than a general
stationary predictor. The Gibbs and coarse-graining identities are
established tools; novelty and physical implementation of the combined
state-cost result remain separate questions. Manuscript drafting remains
deferred.
