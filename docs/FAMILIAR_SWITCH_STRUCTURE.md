# Two coupled conformational switches: three predictive states, four reversible states

This note gives a familiar small kinetic model in which ordinary detailed
balance has an exact predictive state cost. **Any positively coupled pair of
heat-bath conformational switches with equal attempt rates** has four physical
configurations, but its controlled single-spin mean has an exact stationary
three-state Markov predictor. The predictor respects the same equilibrium
field tilt and has a deterministic binary readout. Every ordinarily
reversible model reproducing the same two-field task needs four states.

The reason is elementary. The two field values identify a hidden coordinate
whose conditional variance is positive at **both** readout values. Detailed
balance forces that variance. A three-state model with a binary readout has
a singleton readout sector and cannot supply it.

The assertion concerns controlled means, not equality of visible path laws.
The passive visible process is not an exact two-state Markov chain. This is
a new physical target and comparison class, separate from the hub-interface
and incidence constructions in the earlier notes.

## 1. Physical model and comparison task

Set the temperature and attempt-rate units to one. Represent two conformations
of each switch by Ising variables $s_0,s_1\in\{-1,1\}$. These are
time-even configurations, not magnetic moments; ordinary detailed balance
uses identity time reversal. Use the energy and heat-bath rates

$$
 E_h(s)=-Js_0s_1-hs_0,\qquad
 q_i(s,s^{(i)})=
 \frac{\alpha_i}{1+\exp[2s_i(h\mathbf1_{i=0}+Js_{1-i})]}.
 \tag{1}
$$

Here $s^{(i)}$ flips spin $i$. The observed variable is $S=s_0$.
Every fixed-field generator is reversible for the Boltzmann distribution.
The main theorem allows any finite $J>0$, any finite $H>0$, and uses
$\alpha_0=\alpha_1=1$. A rational example used below is

$$
 J=H=\tfrac12\log2,\qquad \alpha_0=\alpha_1=1,
 \qquad h\in\{0,H\}.
 \tag{2}
$$

Prepare the zero-field equilibrium once, and compare the endpoint mean of
$S$ after every finite word of the two physical fields. The dwell time of
each letter is one prescribed clock tick $a>0$; repeated letters permit
all positive integer multiples of that tick. The theorem holds for **every**
choice of $a$. It also holds if arbitrary positive dwell times are allowed.

An admissible rival has finitely many states, a deterministic readout
$\widehat S\in\{-1,1\}$, and a strictly positive zero-field stationary
law $\widehat\pi_0$ satisfying
$\widehat\pi_0(\widehat S=\pm1)=1/2$. Its equilibrium force dependence is

$$
 \widehat\pi_h(x)=
 \frac{\widehat\pi_0(x)e^{h\widehat S(x)}}{\cosh h},
 \qquad \widehat\pi_h\widehat Q_h=0.
 \tag{3}
$$

The initial law is $\widehat\pi_0$. The two endpoint generators may
otherwise be arbitrary. The ordinary subclass additionally requires detailed
balance at each field. No hidden architecture, target state labels, stationary
mass histogram, or prescribed rate formula is imposed on a rival.
The shared Gibbs tilt is a substantive physical assumption: the control
couples only to the measured conformation, with no independent force coupling
to hidden states. Rivals with arbitrary unrelated equilibrium laws at the
two fields are not covered by this theorem.

**Exact state-count theorem.** For every $J,H>0$, equal unit attempt rates,
and the two fields $\{0,H\}$,

$$
 D_{\rm all}(0)=3,\qquad D_{\rm ord}(0)=4.
 \tag{4}
$$

The exact lower bounds require no rival rate cap. The physical target and
the general three-state predictor have total exit rates below $2$, so (4)
also holds under a common exit cap of $3$. The three-state predictor in
fact works under arbitrary nonnegative field protocols. Eleven specified
endpoint measurements, each using at most three field segments and five
clock ticks, already distinguish the exact counts. Both counts persist at
a positive, presently unquantified error tolerance on that same menu,
even when rival rates are unbounded (Section 6).

The heat-bath model is standard; the controlled compression statement is
proved below. Source comparison and attribution are recorded separately in
[the familiar-switch source audit](FAMILIAR_SWITCH_SOURCE_AUDIT.md).

## 2. The controlled means close exactly

Write $t=\tanh J$ and

$$
 A(h)=\frac{\tanh(h+J)+\tanh(h-J)}2,\qquad
 B(h)=\frac{\tanh(h+J)-\tanh(h-J)}2.
 \tag{5}
$$

Direct application of the generator gives

$$
 Q_h S=\alpha_0[A(h)\mathbf1-S+B(h)Z],\qquad
 Q_h Z=\alpha_1[tS-Z],\qquad Z=s_1.
 \tag{6}
$$

Consequently the constant and the two spin means form an invariant
three-dimensional linear space for every field protocol. For (2),

$$
 t=\frac13,\qquad (A(0),B(0))=(0,\tfrac13),\qquad
 (A(H),B(H))=(\tfrac3{10},\tfrac3{10}).
 \tag{7}
$$

The zero-field initial means are zero. At equilibrium at field $h$, they
are $\langle S\rangle_h=\tanh h$ and
$\langle Z\rangle_h=t\tanh h$.

The order is exactly three, not merely at most three. Put $u=\tanh H$
and $\kappa=\sqrt{tB(H)}\in(0,1)$. Solving the two mean equations from
zero initial means gives

$$
 m_H(\tau)=u-
 \frac{u(1+\kappa)}2e^{-(1-\kappa)\tau}
 -\frac{u(1-\kappa)}2e^{-(1+\kappa)\tau}.
 \tag{8a}
$$

For the rational example, with $\kappa=1/\sqrt{10}$, this is explicitly

$$
 m_H(\tau)=\frac13-
 \frac{1+\kappa}{6}e^{-(1-\kappa)\tau}
 -\frac{1-\kappa}{6}e^{-(1+\kappa)\tau}.
 \tag{8}
$$

All three coefficients are nonzero. At any fixed clock $a>0$, the scalar
sequence $m_H(na)$ has Hankel rank three: its three distinct exponential
bases give an invertible Vandermonde factorization. Thus no two-state Markov
model, even without detailed balance or a rate cap, can reproduce the task.

## 3. A positive three-state predictor for every coupling and positive field

Fix $t=\tanh J\in(0,1)$, and introduce positive constants

$$
 d=3t,\qquad e=\frac{1-t^2}{2t},\qquad W=d+e.
 \tag{G1}
$$

The singleton readout state has the value opposed to the applied positive
field. Choose

$$
 \widehat S=(-1,1,1)^T,\qquad
 \widehat Z=\left(-t,-2t,\frac{1+t^2}{2t}\right)^T,\qquad
 \widehat\pi_0=\left(\frac12,\frac{e}{2W},\frac{d}{2W}\right).
 \tag{G2}
$$

For every finite $h\ge0$, set $A=A(h),B=B(h)$ and
$L=(1+A-Bt)/2$. The six off-diagonal rates are

$$
\begin{aligned}
 q_{12}&=L(2t+e)/W,&q_{13}&=L(d-2t)/W,\\
 q_{21}&=(1-A+2Bt)/2,&
 q_{23}&=[d+q_{21}(2t-d)]/W,\\
 q_{31}&=(1-A-B(t+e))/2,&
 q_{32}&=[e-q_{31}(2t+e)]/W.
\end{aligned}
\tag{G3}
$$

Diagonals are minus row sums. These formulas give a genuine positive Markov
generator for the entire nonnegative field range. To verify the potentially
delicate rates, write $m=\tanh h$, so

$$
 A=\frac{m(1-t^2)}{1-t^2m^2},\qquad
 B=\frac{t(1-m^2)}{1-t^2m^2},\qquad
 q_{31}=\frac{(1-t^2)(1-m)^2}{4(1-t^2m^2)}
 \le\frac{1-t^2}{4}.
 \tag{G4}
$$

Thus $q_{31}>0$ at every finite field, and

$$
 e-q_{31}(2t+e)\ge\frac{3(1-t^2)^2}{8t}>0.
 \tag{G5}
$$

Moreover $0<q_{21}\le(1+2t^2)/2<3/2$, so
$d+q_{21}(2t-d)=t(3-q_{21})>0$. The remaining rates are immediately
positive, since $d-2t=t>0$ and $0<L<1$.
The first row has exit rate $L<1$; the second and third have rates

$$
 \frac{d+q_{21}(2t+e)}{W}<2,\qquad
 \frac{e+tq_{31}}{W}<1,
 \tag{G6}
$$

respectively. The first bound follows from
$2W-d-q_{21}(2t+e)\ge e/2>0$.

Direct multiplication gives the exact target closure

$$
 \widehat Q_h\widehat S=A\mathbf1-\widehat S+B\widehat Z,
 \qquad
 \widehat Q_h\widehat Z=t\widehat S-\widehat Z.
 \tag{G7}
$$

The law in (G2) has $\langle\widehat S\rangle_0=
\langle\widehat Z\rangle_0=0$ and
$\langle\widehat S\widehat Z\rangle_0=t$. Its Gibbs tilt (3) therefore
has means $m,tm$. Since $A=(1-tB)m$, those means are stationary for
(G7). The three functions $\mathbf1,\widehat S,\widehat Z$ are a basis,
so this proves stationarity of the full three-state law, not just two moment
conditions. The law is strictly positive and the generator irreducible.

Starting at $\widehat\pi_0$, equations (6) and (G7) have identical
solutions under every nonnegative field protocol. Only $\widehat S$ is
observed; $\widehat Z$, whose values need not lie in $[-1,1]$, is an
internal coordinate. Its scale is not an extra observed quantity or control.
The predictor is a single fixed family of generators shared by all protocols.

The target and predictor are stationary at every fixed field, but the
predictor cannot obey ordinary detailed balance at both zero and any
positive field, by Section 4. No generalized time-reversal claim is made.

### 3.1 A second, particularly simple rational realization

Use three states with

$$
 \widehat S=(1,-1,-1)^T,\qquad
 \widehat Z=(\tfrac13,\tfrac23,-\tfrac43)^T,
 \qquad
 \widehat\pi_0=(\tfrac12,\tfrac14,\tfrac14).
 \tag{9}
$$

The coordinate $\widehat Z$ is an internal linear coordinate, not a second
readout or a physical spin. Only $\widehat S$ is observed. Let

$$
 \widehat Q_0=
 \begin{pmatrix}
 -4/9&10/27&2/27\\
 11/18&-109/108&43/108\\
 5/18&29/108&-59/108
 \end{pmatrix},\qquad
 \widehat Q_H=
 \begin{pmatrix}
 -3/10&1/4&1/20\\
 3/4&-9/8&3/8\\
 9/20&1/8&-23/40
 \end{pmatrix}.
 \tag{10}
$$

They are irreducible Markov generators, with maximum exit rate $9/8$.
Their stationary laws are

$$
 \widehat\pi_0=(\tfrac12,\tfrac14,\tfrac14),\qquad
 \widehat\pi_H=(\tfrac23,\tfrac16,\tfrac16),
 \tag{11}
$$

which obey exactly (3). Direct multiplication verifies

$$
 \widehat Q_h\widehat S=A(h)\mathbf1-\widehat S+B(h)\widehat Z,
 \qquad
 \widehat Q_h\widehat Z=\tfrac13\widehat S-\widehat Z.
 \tag{12}
$$

Both internal means start at zero. Equations (6) and (12) therefore give
identical output means for every switched two-field protocol, with arbitrary
dwell times. The model is one fixed predictor shared by all protocols; its
rates are not fitted anew to each experiment.

It is not ordinarily reversible. For the first two states, the stationary
flux differences are $7/216$ at zero field and $1/24$ at $H$.
No generalized time-reversal claim is made for this model.

There is also a smooth extension over the full interval $0\le h\le H$.
With $A=A(h),B=B(h)$, define the six off-diagonal rates by

$$
\begin{aligned}
 q_{12}&=5(1-A-B/3)/12,&q_{13}&=(1-A-B/3)/12,\\
 q_{21}&=(1+A+2B/3)/2,&q_{23}&=1/2-q_{21}/6,\\
 q_{31}&=(1+A-4B/3)/2,&q_{32}&=1/2-5q_{31}/6.
\end{aligned}
\tag{13}
$$

All these rates are positive on that interval and the exit rates are below
$2$: use $0\le A\le3/10$ and $3/10\le B\le1/3$.
They satisfy (12) and have the Gibbs-tilted law (3), because that law has
$\langle\widehat S\rangle_h=\tanh h$ and
$\langle\widehat Z\rangle_h=\tfrac13\tanh h$, and
$\mathbf1,\widehat S,\widehat Z$ are a basis. Thus the exact mean upper
bound is not peculiar to two isolated rate matrices. Two fields suffice for
the lower bound.

## 4. Why every three-state ordinary rival fails

First justify transferring (6) to a putative three-state rival. The target
has a minimal three-dimensional controlled linear realization by (8a).
Any three-state model with the same scalar responses is another minimal
realization. Equality of all word responses gives an invertible map between
them: map each output vector reached by a control word to the corresponding
vector in the other model. This is well-defined because the left word rows
span the three-dimensional dual space; any relation can be tested against
all such rows. The map intertwines both clock propagators, the preparation,
and the readout.

For an ordinary rival, each clock propagator has positive spectrum and its
generator is its principal real logarithm divided by $a$. The target
restricted propagators have the same property. Applying that logarithm to
the intertwining identities transfers both generators. The constant vector
is also preserved: it is the unique unit-eigenvalue direction of the
$H$-propagator, and preparation normalization fixes its scale. Therefore
there is a real rival coordinate $Z$ for which (6) holds pointwise, with
the coefficients (5). This argument needs neither a rival rate cap nor
small-clock differentiation.

Write $\langle\cdot\rangle_h$ for the rival equilibrium expectation,
$t=\tanh J\in(0,1)$, and $u=\tanh H\in(0,1)$. Stationarity and
the fixed initial response imply

$$
 \langle Z\rangle_0=0,\qquad
 \langle Z\rangle_H=tu,\qquad
 \pi_H=\pi_0(1+uS).
 \tag{14}
$$

It follows that

$$
 \langle SZ\rangle_0=t,\qquad \langle SZ\rangle_H=t.
 \tag{15}
$$

Detailed balance at field $h$ gives
$\langle Q_hS,Z\rangle_h=\langle S,Q_hZ\rangle_h$.
The right side is $t-\langle SZ\rangle_h=0$. Substitution of (6) yields

$$
 B(h)\langle Z^2\rangle_h=t-A(h)t\tanh h.
 \tag{16}
$$

At both queried fields this forces $\langle Z^2\rangle_h=1$: at zero,
$A=0,B=t$; at $H$, (G4) gives $t(1-Au)=B$. Applying
the tilt identity once more gives $\langle SZ^2\rangle_0=0$. Since
the two readout sectors each have zero-field mass $1/2$,

$$
 \mathbb E_0[Z\mid S=\pm1]=\pm t,
 \qquad
 \mathbb E_0[Z^2\mid S=\pm1]=1,
 \qquad
 \operatorname{Var}_0(Z\mid S=\pm1)=1-t^2>0.
 \tag{17}
$$

Each sector therefore contains at least two states. Three states cannot
suffice. The physical four-state chain supplies the matching ordinary upper
bound, proving (4).

The ordinary lower-bound argument also survives unequal positive attempt
rates, since $\alpha_0,\alpha_1$ cancel from the moment identities whose
right sides vanish. Its two nonconstant eigenvalues remain distinct. The
general positive upper in Section 3 was proved for equal attempt rates;
the exact three-versus-four theorem is stated with that restriction.

## 5. Passive scope and the three-spin boundary

At zero field the stationary mean of the observed spin is zero, so that mean
alone is reproduced by a neutral two-state model. The stationary visible
**path law**, however, is not two-state Markov when the spins interact. In
the fixture, the conditional observed-spin flip hazard is $4/9$ at a
stationary time, while immediately after an observed flip it is $1/2$.
For the latter calculation, incoming equilibrium flux makes the neighboring
spin uniform; at a stationary time it instead favors alignment. The unequal
hazards expose hidden memory already in passive paths. If $J=0$, the
observed spin is autonomous and remains exactly two-state under any local
field protocol.

For three spins on an open chain with energy

$$
 E_h=-J_{01}s_0s_1-J_{12}s_1s_2-hs_0,
 \tag{18}
$$

and zero hidden local fields, all three single-spin means still close. The
endpoint equations use (5), while

$$
\begin{aligned}
 Q_hs_1&=\alpha_1(c s_0+d s_2-s_1),\\
 Q_hs_2&=\alpha_2(\tanh J_{12}\,s_1-s_2),\\
 c&=\tfrac12[\tanh(J_{01}+J_{12})+\tanh(J_{01}-J_{12})],\\
 d&=\tfrac12[\tanh(J_{01}+J_{12})-\tanh(J_{01}-J_{12})].
\end{aligned}
\tag{19}
$$

Thus its controlled mean order is at most four, despite eight physical
configurations. With nonzero ferromagnetic couplings and a nonzero endpoint
field, the tridiagonal mean system is controllable and observable from its
driven end, so that order is four. This does **not** by itself supply a
four-state positive or reversible Markov realization. The explicit two-spin
result is the simpler completed mechanism; no three-spin state-count theorem
is inferred from linear closure alone.

## 6. Eleven short experiments and a positive-error consequence

Fix any clock $a>0$. Write a word chronologically, so $H^i0H^j$ means
$i$ high-field ticks, one zero-field tick, and $j$ high-field ticks. Use
the following eleven endpoint experiments:

$$
 \mathcal W=\{H,H^2,H^3,H^4,H^5\}
 \cup
 \{H\,0,H\,0\,H,H\,0\,H^2,H^2\,0,H^2\,0\,H,H^2\,0\,H^2\}.
 \tag{20}
$$

Every word uses at most five clock ticks and three constant-field segments.
Each experiment restarts from the same zero-field equilibrium. No output
distribution beyond its endpoint mean is requested.

To see why this particular menu suffices, let $m(w)$ denote a word response
and set $m(\varnothing)=0$, which is known from the preparation. Form the
three-by-three Hankel and shifted tables

$$
 G_{ij}=m(H^{i+j}),\qquad
 (G_H)_{ij}=m(H^{i+j+1}),\qquad
 (G_0)_{ij}=m(H^i0H^j),\qquad 0\le i,j\le2.
 \tag{21}
$$

All entries of $G,G_H$ are supplied by the five constant-field experiments.
The missing $i=0$ row of $G_0$ equals $m(H^j)$ because the preparation is
stationary under a zero-field tick. The six remaining entries are precisely
the second group of experiments in (20).

The three nonzero coefficients and distinct exponential bases in (8a) make
$G$ invertible for every $a>0$. For any realization, let $\mathcal R$ have
rows $\pi_0E_H^i$ and $\mathcal C$ have columns $E_H^jS$, where
$E_h=e^{aQ_h}$. Then

$$
 G=\mathcal R\mathcal C,\qquad
 G_h=\mathcal R E_h\mathcal C.
 \tag{22}
$$

For a model with at most three states, invertibility forces exactly three
states and invertible $\mathcal R,\mathcal C$. The matrices
$G^{-1}G_h=\mathcal C^{-1}E_h\mathcal C$ determine both propagators in
the same coordinates. Preparation is the first row of $G$, and readout is
the first coordinate vector. The same construction applies on the target's
three-dimensional mean space. Thus matching the eleven means already
forces the simultaneous similarity used in Section 4, and consequently
rules out every ordinary rival with at most three states. It also rules
out every unrestricted rival with at most two states by the rank of $G$.

There is a positive error margin even without bounding rival rates. This
requires a specific compactness argument for the clock propagators, not a
claim that unbounded generators form a compact set. Suppose a sequence of
ordinary rivals with at most three states had errors on (20) tending to
zero. Pass to a subsequence with fixed state count and binary readout, and
take convergent subsequences of the probability vector $\pi_0$ and the
two stochastic matrices $E_0,E_H$. Their entries are bounded. The Gibbs
tilt, stationarity, and detailed balance pass to these limits.

The limiting stationary law has full support on three states. Indeed,
stationarity and nonnegativity forbid a transition from its positive-mass
support into a zero-mass state under either limiting propagator; the common
tilt makes the support the same at both fields. If that support had at most
two states, the limiting response Hankel matrix would have rank at most
two, contradicting the invertible target $G$.

The limiting three-state propagators match all eleven means. Equation (22)
therefore makes both simultaneously similar to the target's restricted
propagators, with their strictly positive eigenvalues. The principal matrix
logarithm is continuous at these limiting matrices. For each member of the
ordinary sequence it satisfies

$$
 Q_h=\frac1a\log E_h,
 \tag{23}
$$

because a reversible generator has real spectrum and its exponential has
positive spectrum. Consequently the generators in the sequence converge
to finite matrices. Their off-diagonal nonnegativity, zero row sums,
stationarity and detailed balance all survive. The limit would be an
admissible three-state ordinary model matching (20), which Section 4 rules
out. This contradiction proves a strictly positive infimum error
$\varepsilon(J,H,a)>0$ over the entire uncapped ordinary class with at
most three states.

Every stationary two-state Markov model is ordinarily reversible, so the
same bound excludes all unrestricted rivals with at most two states.
The exact upper realizations remain available. Both counts in (4) therefore
persist for every error tolerance strictly below $\varepsilon(J,H,a)$,
using only the specified menu (20), with no rival rate cap.

The existence of this error margin is proved, but its numerical value is
not yet certified. The theorem does not imply a practical sample count or
a uniform margin over coupling, field, or clock choices. Finding and
certifying a useful margin is the next research task; a gap found by local
fitting alone would not certify all reversible rivals.

The bounded numerical screens and reproducible protocol choices are recorded
in [the protocol assessment](FAMILIAR_SWITCH_PROTOCOLS.md). They are candidate
fits and experimental design evidence, not a numerical certification of
$\varepsilon(J,H,a)$.
