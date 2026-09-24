# One-percent kinetic uncertainty in the same two-word experiment

Independent one-percent changes of all four edge prefactors at each field
preserve a finite three-versus-four state advantage. The argument bounds
the measured witness directly and constructs a three-state model of the
two snapshot tables. It does not require the perturbed dynamics to retain
the exact heat-bath coordinate closure.

With the physical allowances specified below, the certified interval is

$$
 \boxed{0.00008\le\delta_{\rm obs}\le0.0009.}
 \tag{1}
$$

The two chronological words, initial and final binary observations, field
values, dwell times, and four physical states are unchanged. Manuscript
drafting remains deferred. This is a conditional mathematical tolerance
guarantee; it does not establish device calibration or experimental cost.
At the nominal fields and dwell times with stationary preparation and
ideal initial instrument, the interval is $0\le\delta_{\rm obs}\le.001$:
the general three-state predictor is exact throughout the kinetic box.

[Weaker-field witness](FAMILIAR_SWITCH_WEAK_FIELD_ROBUSTNESS.md) ·
[Earlier total-variation transfer](FAMILIAR_SWITCH_KINETIC_TOLERANCE.md) ·
[Three-state snapshot construction](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md) ·
[Five-million-trial score test](FAMILIAR_SWITCH_PERCENT_SCORE_TEST.md) ·
[Source audit](FAMILIAR_SWITCH_PERCENT_KINETIC_SOURCE_AUDIT.md) ·
[Internal review](FAMILIAR_SWITCH_PERCENT_KINETIC_INTERNAL_REVIEW.md) ·
[Exact verifier](../scripts/verify_switch_percent_kinetics.py) ·
[Certificate report](../reports/switch_percent_kinetics.json)

## 1. The kinetic box and stationary comparison

Use states $(S,Z)\in\{-1,1\}^2$, energy $-JSZ-hS$, and nominal values

$$
 J=\log3,\qquad h_0=0,\quad h_H=\log2,\qquad
 \tau_0=\tau_H=5/4,\quad u_0=3/5.
 \tag{2}
$$

For each of the four undirected single-coordinate flip edges $e$ and
each plateau $h$, replace the unit-attempt heat-bath rate by

$$
 \widetilde q_h(x,y)=(1+\varepsilon_{h,e})q_h(x,y),\qquad
 |\varepsilon_{h,e}|\le1/100.
 \tag{3}
$$

The same factor multiplies both directions of an edge. The eight factors
are otherwise independent, and each plateau generator is fixed. The
diagonal entries enforce zero row sums. Every model in (3) preserves its
Gibbs stationary law and detailed balance, while neighbor-dependent
factors can destroy the three-dimensional heat-bath closure. There are
no added states, transitions, feedback operations, or recorded variables.

Both words start from the common stationary low law in this section.
Write $(m,c,\ell,d)$ for the latent final means and initial--final
correlations of words $0H,H0$. Initial and final electronic readout are
independent symmetric flips, independent of the dynamics, with contrasts
$a,b\in[49/50,1]$ shared across words. The recorded moments are

$$
 (M,C,L,D)=(bm,ab c,b\ell,ab d).
 \tag{4}
$$

The ordinary rival class and its stationary promises remain those of the
weaker-field proof: arbitrary reversible kernels and graphs, deterministic
binary readout, arbitrary independent symmetric detector errors, low
stationary bias at most $10^{-4}$, tilt-parameter error at most $10^{-4}$,
and stationary tilt residual at most $10^{-5}$. Target and rival detector
probabilities need not agree. A single model supplies both words.

## 2. A direct finite certificate for the entire kinetic box

For either word expand its transition kernel in the eight deviations in
(3), retaining total degree at most two. If $P^{[2]}$ is this polynomial,
its omitted homogeneous terms satisfy

$$
 \|P-P^{[2]}\|_\infty\le
 \rho_2(A):=\frac{A^3}{6(1-A/4)},\qquad
 A=\frac{19}{2}\varepsilon,\quad \varepsilon=1/100.
 \tag{5}
$$

Here the matrix norm is the maximum absolute row sum. Each reference
generator has exit rate below $19/10$, so its perturbation has norm at
most $(19/5)\varepsilon$. Reference propagators are stochastic and
contract this norm. The degree-$k$ term of the time-ordered perturbation
expansion across total duration $5/2$ has norm at most $A^k/k!$.
Summing $k\ge3$ and bounding each successive ratio by $A/4$ proves (5).
This argument bounds the joint-word kernel; it makes no independence
assumption between successive dynamical steps.

All retained coefficients are enclosed using rational arithmetic. At
each plateau, multiply out the matrix-exponential Taylor series through
degree 96 and discard perturbation monomials of degree above two. The
coefficient norm used for this step is

$$
 \|B\|_{\rm coeff}
 =\max_i\sum_j\sum_\alpha |(B_\alpha)_{ij}|.
 \tag{6}
$$

It is submultiplicative. For the time-scaled affine generator, this norm
is below $19/2$: the absolute edge-generator matrices sum entrywise to
the absolute reference-generator matrix. Thus the error in its retained
Taylor coefficients is at most

$$
 e_{96}=\frac{(19/2)^{97}}{97!\,[1-(19/2)/98]}.
 \tag{7}
$$

The coefficient norm of the exact degree-two plateau propagator is at
most $B_2=1+19/4+(19/4)^2/2$. Multiplying the two plateau polynomials
therefore adds coefficient error at most $2B_2e_{96}+e_{96}^2$.
Combining this with (5) gives a per-moment error

$$
 \rho<0.000146373.
 \tag{8}
$$

Indeed, both initial rows $\pi_0$ and $\pi_0 S$ have absolute mass one,
and the final readout has supremum norm one. All dense matrices have
dimension four. The certificate uses neither an optimization result nor
a sampled grid to cover (3).

Evaluating the coefficient polynomials over the full box and retaining
their cancellations gives the outward bounds

| Quantity | Lower bound | Upper bound |
|---|---:|---:|
| Recorded $M$ | $0.21465$ | $0.22225$ |
| Recorded $C$ | $0.46075$ | $0.48602$ |
| Recorded $L$ | $0.12167$ | $0.12783$ |
| Recorded $D$ | $0.47862$ | $0.50460$ |
| Latent $c-d$ | $-0.019608$ | $-0.017576$ |

The bound on $c-d$ comes from its difference polynomial, rather than
subtracting independent moment intervals. The detector factors give
$C-D=ab(c-d)$.

For the witness and the existing fixed score,

$$
 \begin{split}
 R&=\frac35(C-D)+\frac35MD-\left(\frac35-M\right)L,\\
 T&=\frac25M+\frac35C-\frac25L-\frac{12}{25}D-\frac2{25},
 \end{split}
 \tag{9}
$$

the certified uniform lower bounds are

$$
 \boxed{R>0.00389,\qquad T>0.00367.}
 \tag{10}
$$

Both minima over detector contrasts occur at $a=b=49/50$. To verify this
without assuming monotonicity, the latent intervals fit inside
$m\in[.219,.223]$, $c\in[.479,.487]$, $\ell\in[.124,.128]$,
$d\in[.498,.505]$. These bounds make both derivatives of

$$
 R(a,b)=b\{a u_0(c-d+bmd)-u_0\ell+bm\ell\}
 \tag{11}
$$

positive on the contrast square. They also make
$u_0c-(12/25)d>0$ and $(2/5)(m-\ell)>0$, proving the same claim for
$T(a,b)$. The verifier checks these strict rational inequalities.

At that detector corner, substitute the degree-two moment polynomials
into (9), retaining all resulting terms through degree four. Subtract
the sum of the absolute nonconstant coefficients, weighted by
$\varepsilon^{|\alpha|}$. Charge the moment remainders (8) using the
gradient bounds of (9). This yields (10). For orientation, the linear
coefficient sums of $R$ and $T$ are below $.021507$ and $.023330$;
the quadratic coefficient sums are below $.031412$ and $.042791$.
These small direct changes explain why the earlier whole-table transfer
was excessively conservative for this question.

## 3. The ordinary three-state lower

Every recorded target in (3)--(4), and every table pair within joint-table
TV $g=1/1000$ of it, lies in the local box of the weaker-field proof:

$$
 .20\le M\le.24,\quad .45\le C\le.50,\quad
 .11\le L\le.14,\quad .46\le D\le.52,\quad
 -.04\le C-D\le-.001.
 \tag{12}
$$

Each moment changes by at most $2g$; the correlated $C-D$ bound above
ensures its gate as well. Throughout the target family the absolute
gradient mass of $R$ is below $1.9$. A moment displacement bounded by
$r$ contributes quadratic remainder at most $(8/5)r^2$. Hence every
point at distance at most $g$ has

$$
 R>.00389-1.9(2g)-\frac85(2g)^2
   =.0000836>.00007.
 \tag{13}
$$

The inherited singleton-sector proof requires $R<.00007$ for every
stationary ordinary model with at most three states in (12), uniformly
over the stated stationary promises and arbitrary detector contrasts.
Equation (13) contradicts that necessary condition. Thus the stationary
ordinary-three-state error is strictly greater than $.001$ for the
entire independent one-percent kinetic box.

## 4. Why three general states still suffice

The general upper must be established again: exact heat-bath coordinate
closure cannot be assumed after (3). The local snapshot construction
uses four coefficients of the observed two-word laws. In its coordinate
basis let $y,z>0$ be the fixed nominal low-kernel coefficients, with

$$
 y=e^{-5/4}\sinh1,\qquad z=\frac9{25}y.
 \tag{14}
$$

The coefficients fitted to the perturbed target are

$$
 x=\frac{\ell+u_0d}{u_0},\qquad
 a_1=1-\frac m{u_0},\qquad
 b_1=\frac{c-a_1x}{z},\qquad
 c_1=\frac{d-a_1x}{y}.
 \tag{15}
$$

Stationarity gives the useful identity $x=\pi_0 S\widetilde P_0 S$:
with $\pi_H=\pi_0(1+u_0S)$,

$$
 \ell+u_0d
 =\pi_0(1+u_0S)\widetilde P_H\widetilde P_0S
 =\pi_H\widetilde P_0S
 =u_0\pi_0S\widetilde P_0S.
$$

Also $m=\pi_0\widetilde P_H S$, since the first low plateau preserves
$\pi_0$. These two single-plateau expressions reduce their perturbation
remainder to (5) with $A=(19/4)\varepsilon$. Multiplying the retained
polynomials before bounding $c-a_1x$ and $d-a_1x$ preserves their
correlations. Displacement bounds include the Taylor error at both the
perturbed point and the nominal constant coefficient, and division uses
certified positive lower bounds for the exact $y,z$. Relative to the
exact nominal coefficients, the resulting certified bounds are

$$
 |\Delta x|<.002021,\quad |\Delta a_1|<.002468,\quad
 |\Delta b_1|<.007022,\quad |\Delta c_1|<.003647.
 \tag{16}
$$

They lie strictly inside the box with radii $(.003,.004,.01,.006)$
used by the [local three-state construction](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md).
That construction separately certifies positive stochastic kernels,
the stationary force law, the snapshot identities, and matrix logarithms
with positive off-diagonal entries. Thus both kernels are propagators of
genuine three-state continuous-time Markov generators for the common
dwell time $5/4$. Equation (16) supplies the physical input domain for
that certificate. The resulting predictor reproduces both nominal-field,
perturbed-rate stationary joint tables exactly, and uses the target's
detector channel. Equality of full visible trajectory laws is not claimed.

## 5. Preparation, readout, field and timing allowances

Use the existing physical allowances

$$
 \epsilon_{p,T}=\epsilon_{p,R}=\epsilon_h=\epsilon_t=
 \xi_T=\xi_R=10^{-5}.
 \tag{17}
$$

Preparation is measured from each model's stationary low law.
The initial-instrument allowance includes the correlation between its
retained initial record and the postmeasurement hidden state; it is not
merely a bound on either marginal. Electronic errors are already in (4).

For an actual target, compare with the nominal-field, nominal-time model
having the same eight edge factors. No smooth dependence of these factors
on field is assumed: the comparison reference copies the actual factor
at each of the two plateaus. The field-induced generator change
is at most $1.01\epsilon_h/2$ per unit time, and the conservative exit-rate
cap $2.02$ gives timing cost $4.04\epsilon_t$. Together with the equilibrium,
preparation, and instrument terms, the per-table displacement is at most

$$
 \begin{split}
 b_T&=\epsilon_{p,T}+\xi_T+
 \left[\frac12+1.01\left(\frac54+\epsilon_t\right)\right]
 \epsilon_h+4.04\epsilon_t\\
 &=.000078025101<.000079,\qquad
 b_R=\epsilon_{p,R}+\xi_R=.00002.
 \end{split}
 \tag{18}
$$

The stationary ordinary-three lower already allows arbitrary reversible
rival kernels, so there is no rival kinetic-error term. Its actual
error is strictly greater than

$$
 .001-b_T-b_R=.000901974899>.0009.
 \tag{19}
$$

The general three-state predictor of the nominal reference has observed
error at most $b_T<.00008$ for the actual target. Here field and timing
costs are charged in the general upper: this construction does not
invoke the former exact controlled heat-bath closure at the actual fields.
Its stationary laws obey the stated force-law promises. The actual
target, with its own Gibbs laws and fixed reversible plateau generators,
provides an exact ordinary four-state upper. Every stationary two-state
model is ordinary, so (19) excludes general models with at most two
states as well. This proves the exact state minima in (1).

The nominal predictor uses tilt parameter $u_0$. If one instead assigns
the actual common field difference to that predictor, its stationary-tilt
TV residual is at most $|u-u_0|/2\le\epsilon_h=10^{-5}$, still within
the stated force-law promise. Exact agreement with the actual perturbed
Gibbs law is not asserted for this comparison predictor.

The result permits a full independent box of rate departures at the two
plateaus; it is not a common rescaling of time. The one-percent allowance
is 500 times the earlier sufficient 20-parts-per-million example. This
comparison concerns a sufficient theoretical tolerance, not an optimized
threshold or a measured device capability. Additional microscopic states,
driven nonreversible rates, uncontrolled changes of stationary energy,
and detector errors outside the specified independent symmetric channel
model remain outside the theorem.
