# An exact boundary for three-state prediction under signed control

[Four controlled pairs](FAMILIAR_SWITCH_MINIMAL_THEOREM.md) ·
[Positive realization](FAMILIAR_SWITCH_STRUCTURE.md) ·
[Passive pairs and three-time observations](FAMILIAR_SWITCH_THREE_TIME_BOUNDARY.md) ·
[Control and realization source comparison](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md)

The positive three-state predictor for nonnegative fields does not extend
to an arbitrary symmetric field range. For the same two-switch target,
there is an exact boundary between three and four predictive states.
This note derives that boundary from positivity of one common Markov
realization. It also gives a finite endpoint-pair menu that determines it.

The task here uses **one common initial preparation**. This is a stronger
reuse requirement than the four fixed pair laws with arbitrary per-word
preparations in the minimal theorem. No Gibbs force rule or reversibility
is assumed for the general rival: the Gibbs stationary family follows
from the data if a three-state realization exists. All observations are
ideal deterministic state observables. The statement makes no detector,
device-realization or thermodynamic-cost claim.

The proof uses standard minimal linear realization, matrix logarithms and
positivity of Markov generators. Its content is an explicit application
to this target and control interface, rather than a new general method
for positive realization.

## 1. Model, prediction tasks and exact criterion

Use the equal-attempt heat-bath model with energy in units of
$k_{\rm B}T$,

$$
 E_h(S,Z)=-JSZ-hS,
 \qquad
 q_S(S,Z)=\frac1{1+e^{2S(h+JZ)}},\qquad
 q_Z(S,Z)=\frac1{1+e^{2JZS}},
 \tag{1}
$$

where $S,Z\in\{-1,+1\}$ and $0<J,H<\infty$. Put
$t=\tanh J\in(0,1)$ and $u=\tanh H\in(0,1)$.
Every experiment starts from
$\pi_0(S,Z)=(1+tSZ)/4$ and retains the true initial and final signs
of $S$. A chronological word specifies the successive fields and their
dwell times; there are no intermediate observations.

A rival has one finite state space, a deterministic binary readout
$\widehat S$, one common initial law $\nu$, and one fixed real
continuous-time Markov generator $\widehat Q_h$ for each allowed field.
There are no initial stationarity, positive-mass, detailed-balance,
shared-force or rate-cap assumptions on the rival. Its rates may vanish.
The counted state must contain all memory affecting subsequent evolution.
The ordinary subclass additionally requires detailed balance with a
positive stationary law at each field; those laws are initially allowed
to have an arbitrary relation across fields.

Consider either of the following tasks:

1. Match all endpoint-pair laws for all finite words, with arbitrary
   positive dwell times, using the fields $\{0,+H,-H\}$ or the entire
   interval $[-H,H]$.
2. Fix any clock $\alpha>0$, use one tick per letter, and match the
   following **23 endpoint-pair laws**:

$$
 \mathcal W_{23}=
 \{H^k:1\le k\le5\}
 \ \cup\ \{H^i0H^j:0\le i,j\le2\}
 \ \cup\ \{H^i(-H)H^j:0\le i,j\le2\}.
 \tag{2}
$$

Here $H^0$ is the empty prefix or suffix; the symbol $0$ in the
middle is a genuine zero-field tick. The longest word has five ticks.
The same initial law is used for all 23 words.

**Signed-control theorem.** In either task the exact minimum number of
states in the general continuous-time Markov class is

$$
 D_{\rm all}(0)=
 \begin{cases}
 3,&3t^2u^2+(1+t^2)u\le1,\\
 4,&3t^2u^2+(1+t^2)u>1.
 \end{cases}
 \tag{3}
$$

The ordinary reversible minimum is four for every $t,u\in(0,1)$.
This conclusion does not assume a shared Gibbs force rule for a rival.

The three-state construction, when available, works simultaneously on
the whole interval $[-H,H]$. It has a positive stationary law and is
irreducible at every field, including at the equality boundary in (3).
It therefore also matches every finite subtask of the first task.

For the 23-word task, there is a parameter- and clock-dependent
$\delta_*>0$ such that both exact state minima persist for maximum
pair-law TV error $0\le\delta<\delta_*$. This is an existence
statement for a positive error margin, without a numerical constant
or a rival rate bound.

For every three-state exact realization, the data force

$$
 \nu\widehat Q_0=0,
 \qquad \nu>0,
 \qquad
 \nu_h(x)=\nu(x)(1+\tanh(h)\widehat S(x))
          =\frac{\nu(x)e^{h\widehat S(x)}}{\cosh h},
 \quad \nu_h\widehat Q_h=0.
 \tag{4}
$$

For the finite menu this conclusion applies at its three fields.
In particular, matching the menu cannot evade the positivity obstruction
by choosing a nonstationary common preparation or an unrelated stationary
force response.

## 2. The three-dimensional target closure is a minimal realization

For $m=\tanh h$, define

$$
 A_h=\frac{m(1-t^2)}{1-t^2m^2},\qquad
 B_h=\frac{t(1-m^2)}{1-t^2m^2}.
 \tag{5}
$$

The span of $1,S,Z$ is invariant, with

$$
 Q_hS=A_h-S+B_hZ,\qquad Q_hZ=tS-Z.
 \tag{6}
$$

Writing observable coefficients as columns gives

$$
 M_h=\begin{pmatrix}0&A_h&0\\0&-1&t\\0&B_h&-1\end{pmatrix},
 \qquad r=(1,0,0),\qquad b=(0,1,0)^T.
 \tag{7}
$$

Thus a target endpoint mean for a word $w$ is
$rE_wb$, where $E_h=e^{\alpha M_h}$ for a clocked letter, and the
matrices are multiplied in chronological order. The initial sign mean
is zero.

At $h=H$, $A_H,B_H>0$. The infinitesimal column and row matrices
obey

$$
 \det[b,M_Hb,M_H^2b]=A_HB_H>0,
 \qquad
 \det\begin{pmatrix}r\\rM_H\\rM_H^2\end{pmatrix}
 =tA_H^2>0.
 \tag{8}
$$

The eigenvalues of $M_H$ are $0,-1+\sqrt{tB_H},-1-\sqrt{tB_H}$,
three distinct real numbers. For every $\alpha>0$, their exponentials
are also distinct. Polynomial interpolation therefore gives the same
row and column spans when $M_H$ is replaced by $E_H$.
In particular, both matrices

$$
 R=\begin{pmatrix}r\\rE_H\\rE_H^2\end{pmatrix},
 \qquad C=[b,E_Hb,E_H^2b]
 \tag{9}
$$

are invertible. Their product is the observable Hankel matrix
$G_{ij}=rE_H^{i+j}b$, $0\le i,j\le2$.
Its empty-word entry is the initial sign mean. Hence the data have
linear realization dimension three, excluding any one- or two-state
Markov realization.

Suppose an exact three-state rival exists for the finite menu.
Write $\widehat K_h=e^{\alpha\widehat Q_h}$ and form
$\widehat R,\widehat C$ as in (9), using $\nu,\widehat K_H,
\widehat S$. Equality of the five positive-field means and the initial
mean gives
$\widehat R\widehat C=RC$. All four factors are invertible.
Set $T=\widehat C C^{-1}$.

The three shifted tables

$$
 G_h=(rE_H^iE_hE_H^jb)_{i,j=0}^2=RE_hC,
 \qquad h=0,H,-H,
 \tag{10}
$$

are completely observed in (2): the $H$ table uses the five means
at powers one through five, and the other two use their nine-word
blocks. Consequently

$$
 \widehat K_hT=TE_h,\qquad \nu T=r,
 \qquad \widehat S=Tb.
 \tag{11}
$$

Each $E_h$ has three distinct positive real eigenvalues.
A real generator $\widehat Q_h$ commutes with its exponential
$\widehat K_h$. It must therefore preserve each one-dimensional real
eigenspace of $\widehat K_h$ and act there by a real scalar.
That scalar is uniquely $\alpha^{-1}\log\lambda$ for the corresponding
positive eigenvalue $\lambda$. Thus there is no matrix-logarithm
ambiguity, even for nonreversible rivals, and

$$
 \widehat Q_hT=TM_h.
 \tag{12}
$$

The right eigenvalue one of $\widehat K_H$ is simple. Since a
stochastic matrix preserves the constant observable, (11) and
normalization imply $Te_1=\mathbf1$. Put $\widehat Z=Te_3$.
Equations (11)--(12) give the pointwise closure (6) for the rival,
and

$$
 \nu\widehat S=\nu\widehat Z=0,
 \qquad \nu\widehat Q_0=0.
 \tag{13}
$$

This also proves closure transfer for the all-word task at its three
specified fields, because it contains (2). For any additional field,
the observed shifted table in (10) gives the same similarity.
Alternatively, arbitrary dwell times give (12) directly by mixed
derivatives of endpoint means. The finite proof avoids relying on
either an assumed stationary initialization or an arbitrary logarithm
choice.

## 3. Pair information forces positive equilibrium preparation and tilt

The single passive pair, the word $0$ in (2), supplies information
beyond means. Closure gives

$$
 e^{\alpha\widehat Q_0}\widehat S
 =e^{-\alpha}\bigl[
 \cosh(t\alpha)\widehat S+\sinh(t\alpha)\widehat Z\bigr].
 \tag{14}
$$

Matching its initial/final correlation, and using $\widehat S^2=1$,
therefore forces

$$
 \nu(\widehat S\widehat Z)=t.
 \tag{15}
$$

The common initial law is strictly positive. Otherwise its balanced
signs require exactly one state of each sign in its support, each with
mass $1/2$. Equations (13) and (15) imply
$\widehat Z=t\widehat S$ on that support. Stationarity in (13)
prevents any transition under $\widehat Q_0$ from a positive-mass state
to a zero-mass state. On the support, linearity would then give

$$
 \widehat Q_0\widehat Z
 =t\widehat Q_0\widehat S
 =-t(1-t^2)\widehat S\ne0,
$$

whereas closure gives
$\widehat Q_0\widehat Z=t\widehat S-\widehat Z=0$.
This contradiction proves $\nu>0$ without a prior state-mass floor.

For every available field, the positive probability law
$\nu_h=\nu(1+m\widehat S)$ has moments

$$
 \nu_h(1,\widehat S,\widehat Z)=(1,m,tm).
$$

Since $A_h=m(1-tB_h)$, these moments annihilate $M_h$.
The three observables are a basis on the rival's three states, so
$\nu_h\widehat Q_h=0$. This proves (4). It also gives
$\mathbb E_\nu[\widehat Z\mid\widehat S=s]=ts$.
Neither a physical interpretation nor a binary range restriction for
$\widehat Z$ follows or is needed.

## 4. Every possible three-state triangle obeys the same obstruction

A three-state binary readout has a singleton sign sector. Symmetry
under $(S,Z,h)\mapsto(-S,-Z,-h)$ lets us take that sector to be
negative. Positive $\nu$, the conditional means just derived, and
independence of $1,\widehat S,\widehat Z$ permit the parameterization

$$
 \widehat S=(-1,1,1)^T,
 \qquad \widehat Z=(-t,t-a,t+b)^T,
 \qquad
 \nu=\left(\frac12,\frac{b}{2(a+b)},\frac{a}{2(a+b)}\right),
 \quad a,b>0.
 \tag{16}
$$

This covers all orderings and allows auxiliary values outside
$[-1,1]$. Define $L_h=(1+A_h-tB_h)/2>0$.
The two closure equations uniquely fix the six off-diagonal rates:

$$
 \begin{aligned}
 q_{12}&=\frac{L_h(2t+b)}{a+b},&
 q_{13}&=\frac{L_h(a-2t)}{a+b},\\
 q_{21}&=\frac{1-A_h-B_h(t-a)}2,&
 q_{23}&=\frac{a-q_{21}(a-2t)}{a+b},\\
 q_{31}&=\frac{1-A_h-B_h(t+b)}2,&
 q_{32}&=\frac{b-q_{31}(2t+b)}{a+b}.
 \end{aligned}
 \tag{17}
$$

Nonnegative $q_{13}$ forces $a\ge2t$. At $+H$, nonnegative
$q_{31}$ forces

$$
 b\le b_*:=\frac{1-t^2}{t(1+u)}.
 \tag{18}
$$

At $-H$, nonnegative $q_{32}$ requires

$$
 f(b):=q_{31}(-H)-\frac b{2t+b}\le0.
 \tag{19}
$$

For fixed $t,u$, this function is strictly decreasing:
$f'(b)=-B_H/2-2t/(2t+b)^2<0$.
Thus (18)--(19) can hold only if $f(b_*)\le0$.
At $b=b_*$, $q_{31}(H)=0$ and $q_{31}(-H)=A_H$, so this last
condition is

$$
 \frac{u(1-t^2)}{1-t^2u^2}
 \le\frac{1-t^2}{1+t^2+2t^2u}.
 \tag{20}
$$

Cancelling positive factors and rearranging gives exactly
$3t^2u^2+(1+t^2)u\le1$.
This lower bound includes vanishing rates, either singleton sign,
arbitrary auxiliary coordinates and initially zero-mass states.
It does not restrict the rival to a previously chosen triangle.

## 5. A matching construction on the entire symmetric interval

Assume the inequality in (3). Choose $a=2t$, $b=b_*$ and put

$$
 c=\frac b{2t+b}=\frac{1-t^2}{1+t^2+2t^2u},
 \qquad \rho=1-c=\frac{2t}{2t+b}.
 \tag{21}
$$

Use
$\widehat S=(-1,1,1)^T$,
$\widehat Z=(-t,-t,t+b)^T$ and
$\nu=(1/2,c/2,\rho/2)$.
For $m=\tanh h\in[-u,u]$, define

$$
 L(m)=\frac{(1-t^2)(1+m)}{2(1-t^2m^2)},
 \qquad
 k(m)=\frac{(1-t^2)(1-m)(u-m)}
 {2(1+u)(1-t^2m^2)},
 \tag{22}
$$

and take

$$
 \widehat Q(m)=
 \begin{pmatrix}
 -L&L&0\\
 1-L&-(1-L+\rho)&\rho\\
 k&c-k&-c
 \end{pmatrix}.
 \tag{23}
$$

Here $0<L<1$ and $0<c,\rho<1$. Also $k\ge0$ on the interval,
and its maximum is $k(-u)=A_H$.
For completeness, (17) shows
$k(-m)-k(m)=A(m)\ge0$ for $m\ge0$.
On $[-u,0]$, both $A'(m)>0$ and $B'(m)\ge0$, so
$k'(m)=-(A'(m)+(t+b)B'(m))/2<0$.
Consequently (20) is exactly the condition $k(m)\le c$ for all
$m\in[-u,u]$. Every off-diagonal entry in (23) is nonnegative.

The chain is irreducible throughout: $1\to2$, $2\to1$ and
$2\to3$ have positive rates, and state 3 has total exit rate $c>0$
to states 1 and 2. This remains true when $k(-u)=c$ at equality,
or when $k(u)=0$. All stationary masses in (4) are positive.
The convenient construction has $q_{13}=0$; strictly positive rates
are not needed for a continuous-time Markov realization.
If the criterion is strict, $b$ can be decreased slightly below
$b_*$ and then $a$ increased slightly above $2t$ in (17) to make
all six rates strictly positive, uniformly over the compact interval.
At equality, (18)--(19) force $b=b_*$, so the two endpoint zeros
$q_{31}(H)=q_{32}(-H)=0$ cannot both be removed.

Substitution into (17) verifies the common closure and (4).
Conditional on the initial sign $s$, both target and predictor have
initial moments $(S,Z)=(s,ts)$. The closure then gives the same
conditional final sign mean for every controlled word. Binary final
signs are determined by their means, and initial signs have equal
mass. Hence all requested endpoint-pair laws agree exactly.
This proves the upper bound of three; the original four-state target
supplies the upper bound in the other case. No equality of joint
three-time or longer visible path laws is claimed.

## 6. Why the finite obstructions have positive TV margins

Fix $t,u,\alpha$ with $3t^2u^2+(1+t^2)u>1$.
Suppose a sequence of at-most-three-state rivals approached all 23
pair laws arbitrarily well. The nonzero target Hankel determinant
forces every sufficiently accurate rival to have exactly three states.
There are finitely many readout assignments; pass to a fixed one.
Probability laws $\nu$ and stochastic matrices
$\widehat K_0,\widehat K_H,\widehat K_{-H}$ lie in compact sets,
so a subsequence converges.

Endpoint-pair probabilities are polynomial functions of these entries.
The limit therefore reproduces the finite menu exactly. The same
invertible Hankel and shifted-table argument proves that its three
limit kernels are simultaneously similar to $E_0,E_H,E_{-H}$.
Their spectra are distinct and positive.

For all sufficiently late members of the subsequence, each kernel
also has three distinct positive real eigenvalues. Indeed, each small
disjoint neighborhood of a limit eigenvalue contains exactly one
eigenvalue; reality of the matrix prevents that eigenvalue from being
nonreal. The commutation argument from Section 2 then identifies each
rival generator with $\alpha^{-1}$ times its kernel's principal
logarithm. Matrix logarithms are continuous near the limit kernels.
The generators therefore converge to finite real generators with
nonnegative off-diagonals and zero row sums.

The limiting model is an exact three-state continuous-time realization
of the menu, contradicting (18)--(20). Thus the infimum maximum TV
error is positive. This argument derives the local bound on rival
rates from proximity to the observed kernels; it assumes no global
rate cap and no initial state-mass floor. It does not provide a
uniform margin as the clock, coupling, field range or distance from
the equality boundary varies.

The same argument gives a positive distance from at-most-three-state
ordinary models for every $t,u\in(0,1)$. For each field also take a
convergent subsequence of their detailed-balance stationary laws.
The limit generator has a simple zero eigenvalue, so its only
normalized stationary law is the positive law (4).
Detailed balance passes to the limit because both probabilities and
generator entries converge. This would give an exact ordinary
three-state realization, which Section 7 excludes.
Finally, continuity of the nonzero Hankel determinant separates the
menu from all at-most-two-state models. Combining these positive
distances proves the persistence of both state minima stated in
Section 1, including when the general minimum is three.

## 7. Interpretation and limits

The critical field range is

$$
 u_c(t)=\frac{\sqrt{(1+t^2)^2+12t^2}-(1+t^2)}{6t^2}.
 \tag{24}
$$

At the previously selected point $t=4/5$, $u=3/5$, the left side
of (3) is $1.6752>1$. Allowing both field signs at that point raises
the exact general predictive minimum to four. In contrast, a
sufficiently small symmetric field interval retains a three-state
model. The one-sided construction is therefore a substantive scope
condition, but the presence of any negative field is not by itself
an obstruction.

The minimal linear realization of the endpoint means remains
three-dimensional on both sides of the boundary. The extra required
Markov state is a consequence of nonnegative transition rates under
the shared signed controls; it does not come from an extra visible
linear relaxation mode. This distinguishes linear closure from a
positive Markov realization on the requested interface.

Whenever a three-state signed realization exists, it cannot be
ordinarily reversible at all fields. Its inferred stationary tilt
and the four words $0,H,0H,H0$ in (2) would otherwise violate the
nonzero singleton return residual of the
[minimal theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md).
Thus the ordinary reversible minimum for these tasks is always four,
while the general minimum changes at (3). Currents of a smaller
predictor are representational properties; they are not currents of
the reversible fixed-field target and do not establish a physical
cost of computation.

The result does not apply to unrelated preparations chosen separately
for the 23 words, to arbitrary discrete-time kernels without
continuous-time generators, to noisy or state-dependent readout, or
to uncounted memory. None of those alternatives has been ruled out
by this proof. The distinction from the original four-word theorem
is the additional shared preparation and control information, not
a stronger claim about physical coarse-graining.

The limits $J=0$ or $H=0$ are excluded from the rank-three controlled
argument. At $H=0$ the separate passive-pair construction applies;
at $J=0$ the observed switch itself is a two-state Markov process.
There is no uniform separation claim in these degenerate limits.

## Appendix. Arbitrary positive attempt-rate ratio

Equal attempt rates are not required for the signed-control boundary.
Let the physical visible and hidden attempt rates be
$\Gamma_S,\Gamma_Z>0$, normalize time by $\Gamma_S$, and in this
appendix write $r=\Gamma_Z/\Gamma_S>0$ for their scalar ratio.
The stationary target laws remain unchanged. This is the same
unequal-attempt model as the
[charge-state realization](FAMILIAR_SWITCH_CHARGE_REALIZATION.md).
The earlier one-sided construction there and the exact signed-control
criterion below are different statements; no restriction to its
previously constructed rate interval is needed here.

**Unequal-rate extension.** For every $t,u\in(0,1)$ and $r>0$, both
tasks in Section 1 have exact general minimum

$$
 D_{\rm all}(0)=
 \begin{cases}
 3,&(r+2)t^2u^2+(1+t^2)u\le r,\\
 4,&(r+2)t^2u^2+(1+t^2)u>r.
 \end{cases}
 \tag{A1}
$$

The ordinary reversible minimum is four throughout. For the same
23-pair menu at any fixed positive clock, both minima persist at some
positive TV accuracy. The common-preparation and ideal-readout scope
is exactly as in the main theorem.

The closed equations and coefficient matrix now are

$$
 Q_hS=A_h-S+B_hZ,\qquad Q_hZ=r(tS-Z),\qquad
 M_h^{(r)}=
 \begin{pmatrix}0&A_h&0\\0&-1&rt\\0&B_h&-r\end{pmatrix}.
 \tag{A2}
$$

The column determinant in (8) becomes $rA_HB_H$ and the row
determinant becomes $rtA_H^2$, both strictly positive. The nonzero
eigenvalues are

$$
 -\frac{1+r}{2}\pm\frac{\Omega_h}{2},\qquad
 \Omega_h=\sqrt{(1-r)^2+4rtB_h}.
 \tag{A3}
$$

They are distinct and strictly negative, because $tB_h<1$.
Thus sampled row and column spans, the three shifted tables and
the unique real logarithm argument work without an exceptional
positive rate ratio.

For a dwell $a>0$, the coefficient of $Z$ in $e^{aQ_h}S$ is

$$
 \gamma_h(a)=
 e^{-(1+r)a/2}\frac{2B_h}{\Omega_h}
                 \sinh(\Omega_h a/2)>0.
 \tag{A4}
$$

In particular the passive pair still determines
$\nu(\widehat S\widehat Z)=t$. The inferred zero first moments
still imply $\nu\widehat Q_0=0$. On any hypothetical two-state
support with $\widehat Z=t\widehat S$, closure now gives
$\widehat Q_0\widehat Z=r(t\widehat S-\widehat Z)=0$, contradicting
$t\widehat Q_0\widehat S=-t(1-t^2)\widehat S\ne0$ just as before.
Positive preparation and the stationary tilt (4) therefore follow
unchanged.

In the exhaustive triangle parameterization (16), four of the rates
in (17) stay the same. Only the two within-positive-sector rates change:

$$
 q_{23}=\frac{ra-q_{21}(a-2t)}{a+b},\qquad
 q_{32}=\frac{rb-q_{31}(2t+b)}{a+b}.
 \tag{A5}
$$

Necessity still gives $a\ge2t$ and $b\le b_*$ from (18).
At the negative endpoint, it gives
$q_{31}(-H)\le rb/(2t+b)$.
The difference of these two sides is strictly decreasing in $b$,
with derivative $-B_H/2-2rt/(2t+b)^2<0$.
Its value at the largest allowed $b=b_*$ yields $A_H\le rc$,
where $c$ is (21). This is precisely (A1).

For sufficiency, keep $a=2t$, $b=b_*$, the observables, preparation,
$L$ and $k$ from Section 5. Replace (23) by

$$
 \widehat Q^{(r)}(m)=
 \begin{pmatrix}
 -L&L&0\\
 1-L&-(1-L+r\rho)&r\rho\\
 k&rc-k&-rc
 \end{pmatrix}.
 \tag{A6}
$$

The bound $0\le k(m)\le A_H\le rc$ proves positivity on the whole
symmetric interval. The chain remains irreducible, including at
equality, since $L,1-L,r\rho,rc$ are positive.
The stationary family and conditional initial moments are unchanged,
and (A2) proves exact endpoint-pair matching. Strict inequality again
permits all six off-diagonal rates to be made positive by the small
triangle perturbation in Section 5.

Ordinary three-state matching is still impossible: the same
singleton return identity applies to the inferred Gibbs family, while
the target covariance is
$\gamma_0(a)\gamma_H(a)(1-t^2)>0$.
This is the unequal-rate covariance argument already recorded in the
charge-state note. Finally, distinct positive sampled spectra and
the positive inferred laws give the same compactness and
logarithm-continuity proof of positive finite-menu TV margins.

Equivalently, at fixed coupling and signed field range a three-state
model exists exactly when

$$
 r\ge\frac{u(1+t^2+2t^2u)}{1-t^2u^2}.
 \tag{A7}
$$

At $t=4/5,u=3/5$ this threshold is $r=903/481$. Thus the extra
state required at equal attempt rates is not universal across all
relative switch timescales. The linear endpoint-mean dimension remains
three throughout; the threshold concerns the positivity of a shared
Markov realization.
