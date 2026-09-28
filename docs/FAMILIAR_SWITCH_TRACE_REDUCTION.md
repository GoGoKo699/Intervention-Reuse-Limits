# Strong coupling permits uniform equilibrium reduction, even at long times

Retaining the transition flux through a rare configuration closes the
remaining strong-coupling corner. A single reversible three-state model
approximates every nonnegative-field endpoint-pair experiment with error
at most $3(1-\tanh J)/2$. The bound is uniform in the hidden/visible
rate ratio, field strength, observation time and number of switches.
Thus increasing coupling, field and waiting time together cannot retain
a fixed positive fourth-state penalty for this task.

The mechanism matters: deleting a rarely visited state also deletes a
transition route, whose loss can accumulate over long times. The trace
generator retains that route as a direct transition. The proof below
controls its error at the original observation times, without replacing
the laboratory clock by time spent in the retained states.

## 1. Task and theorem

Use the [two-spin heat-bath target](FAMILIAR_SWITCH_FAST_RELAXATION.md),
with energy $-JSZ-hS$, $J>0$, $r=\Gamma_Z/\Gamma_S>0$ and
time in units of $1/\Gamma_S$. The target starts in
$\pi_0(S,Z)=(1+tSZ)/4$, where $t=\tanh J$.
Observe only the true initial and final signs of $S$.
Controls are predetermined finite words of arbitrary finite fields
$h\ge0$ and arbitrary held durations. There is no dwell floor, switch
budget or horizon bound.

The rival class retains the [broad normalized-Gibbs comparison](FAMILIAR_SWITCH_RAPID_CONTROL.md):
at most three complete persistent states, fixed binary readout, reused
continuous-time generators, ordinary detailed balance and normalized
Gibbs-related stationary laws. Rival preparations may depend arbitrarily
on the word; no stationary-preparation promise, rate cap or mass floor
is imposed. The construction here uses one common preparation.

Set

$$
\delta=\frac{1-t}{2}\in(0,1/2),\qquad
q=\frac1{1+r(1-\delta)}.
$$

There is an explicit admissible family $\widehat Q_h$ such that

$$
\boxed{\sup_w\operatorname{TV}(P_w,\widehat P_w)
\le\min\{1,(2+q)\delta\}
\le\min\{1,\tfrac32(1-t)\}.}
\tag{1}
$$

Both laws use the same field schedule and elapsed time. The field and
rate ratio may vary with $J$ along a limiting sequence; the last bound
has no dependence on either. It concerns endpoint pairs, not full
trajectory laws, intermediate observations or feedback.

## 2. Preserve the rare transition route

Label configurations $A=(-1,-1)$, $B=(1,-1)$, $C=(1,1)$,
$D=(-1,1)$. Write

$$
a_h=\frac{1+\tanh(h-J)}2,\qquad
d_h=\frac{1-\tanh(h+J)}2,\qquad
e=r\delta,\quad f=r(1-\delta).
$$

For nonnegative fields, $a_h\ge\delta$, $0<d_h\le\delta$,
and $a_h+d_h\le1$. The visible edges have rates
$A\to B:a_h$, $B\to A:1-a_h$, $C\to D:d_h$,
$D\to C:1-d_h$; the hidden edges have rates
$A\to D=C\to B=e$ and $D\to A=B\to C=f$.

Eliminate $D$ by the standard Schur trace construction. Put
$\lambda_h=f+1-d_h$ and

$$
k_h=\frac{e(1-d_h)}{\lambda_h},\qquad
l_h=\frac{d_hf}{\lambda_h}.
$$

The retained row generator is

$$
\widehat Q_h=
\begin{pmatrix}
-a_h-k_h&a_h&k_h\\
1-a_h&-(1-a_h+f)&f\\
l_h&e&-l_h-e
\end{pmatrix},\qquad \widehat S=(-1,1,1).
\tag{2}
$$

It is irreducible and reversible for
$\rho_h=\pi_h(\cdot\mid\{A,B,C\})$. The original two edges
inherit detailed balance. On the added edge,
$\pi_h(A)e=\pi_h(D)f$ and
$\pi_h(C)d_h=\pi_h(D)(1-d_h)$ give
$\pi_h(A)k_h=\pi_h(C)l_h$.
The stationary laws obey one normalized Gibbs rule:

$$
\rho_h(i)=\frac{\rho_0(i)(1+m\widehat S(i))}
 {1+m\rho_0\widehat S},\qquad m=\tanh h,
\quad \rho_0=\frac{(1-\delta,\delta,1-\delta)}{2-\delta}.
\tag{3}
$$

Use the common preparation
$\widehat\nu=(1/2,\delta/2,(1-\delta)/2)$, obtained by
moving the target's initial $D$ mass to $A$. This preserves the initial
sign exactly. The preparation is balanced and nonstationary; the
stationary low-field readout is biased. Both are permitted by the
stated comparison class.

## 3. A common error box prevents accumulation

Condition throughout on either initial sign. Let $x_A,x_B,x_C,z$
be the target probabilities, with $z$ denoting occupancy of $D$.
Then $z'=e x_A+d_h x_C-\lambda_h z$ and initially $z\le\delta$.
At $z=\delta$,

$$
z'\le\delta\max\{r,1\}(1-\delta)
 -(r+1)(1-\delta)\delta\le0.
$$

Hence $0\le z\le\delta$ throughout every word.
Define field-independent constants

$$
L=f+1,\qquad p=f/L,\qquad q=1/L,\qquad k_0=e/L
$$

and the probability row $Y=(x_A,x_B,x_C)+z(p,0,q)$.
Let $\widehat x$ be the probability row evolving with (2) from the
conditional preparation above. For the cumulative errors

$$
U=Y_A-\widehat x_A,\qquad
V=Y_A+Y_B-\widehat x_A-\widehat x_B,
$$

direct substitution of the four-state equations gives

$$
\binom{U'}{V'}=
\begin{pmatrix}
-1-k_h&1-a_h-l_h\\
f-k_h&-r-l_h
\end{pmatrix}\binom UV+
\binom{F_A}{F_A+F_B},
\tag{4}
$$

where, writing $W=(e,0,d_h)^{\mathsf T}$,

$$
\sigma=(YW)\frac{p d_h}{\lambda_h}
        =(YW)\frac{l_h}{L},
$$

$$
F_A=-\sigma+z[p a_h+p k_0+p^2d_h],\qquad
F_A+F_B=-\sigma+z[p^2d_h-q^2e].
\tag{5}
$$

For clarity, (5) follows by first using the fixed redistribution
$\nu=(p,0,q)$: $Y'=Y(Q_{RR}+W\nu)+
z(q_{DR}-\lambda_h\nu-\nu(Q_{RR}+W\nu))$.
The difference from the trace generator is
$Q_{RR}+W\nu-\widehat Q_h
=W(-p d_h/\lambda_h,0,p d_h/\lambda_h)$.

The matrix in (4) has nonnegative off-diagonal entries:
$l_h\le d_h\le1-a_h$ and $k_h\le k_0\le e\le f$.
Its row sums are $-(a_h+k_h+l_h)$ and $-(e+k_h+l_h)$.
The forcing satisfies

$$
|F_A|\le2\delta(a_h+k_h+l_h),\qquad
|F_A+F_B|\le2\delta(e+k_h+l_h).
\tag{6}
$$

Here are elementary bounds establishing (6), including uniformity in
$r$. Since $Y$ is a probability row,
$YW\le\delta\max\{r,1\}$ and
$\max\{r,1\}/L\le1/(1-\delta)\le2$, so
$0\le\sigma\le2\delta l_h$.
Also $p^2d_h\le l_h$, $k_0\le2k_h$ and $p,q\le1$.
The positive part of $F_A$ is therefore at most
$\delta(a_h+2k_h+l_h)$ and its negative part at most
$2\delta l_h$. The positive part of $F_A+F_B$ is at most
$\delta l_h$ and its negative part at most
$2\delta l_h+\delta e$. These imply (6).

Consequently the square $|U|,|V|\le2\delta$ is invariant under
every field: at each face, the row-sum damping dominates the forcing.
Initially $U=V=-q\delta$ for the negative sign, and both are zero
for the positive sign. The square therefore contains both conditional
solutions. It is unchanged at switches because the redistribution and
error coordinates are field-independent.

The target negative-sign probability is $x_A+z=Y_A+qz$;
the rival's is $\widehat x_A$. Their conditional binary-TV error
is at most $|U|+qz\le(2+q)\delta$. Averaging over the identical
balanced initial signs gives the same bound for the complete pair law,
proving (1). No duration or switch-count factor occurs.

## 4. Any fixed positive equilibrium-specific penalty lies in the interior

For the two-field task, let $E_3^{\rm all}(t,u,r)$ have the meaning
in the [finite-rate note](FAMILIAR_SWITCH_FINITE_RATE_WINDOW.md).
For any fixed tolerance $\epsilon>0$, parameters satisfying

$$
E_3^{\rm all}(t,u,r)\ge\epsilon,
\qquad r\ge r_*(t,u)
$$

are contained in a compact subset of
$(0,1)^2\times(0,\infty)$. The second condition is the
[exact general-three-state feasibility boundary](FAMILIAR_SWITCH_ONE_SIDED_BOUNDARY.md);
without it a fourth state need not be an equilibrium-specific cost.

To see the compactness, (1) bounds $t$ away from one. The previous
field upper

$$
E_3^{\rm all}\le
\frac{t^2u(1-u)}{2(r+1)(1-t^2u^2)^2}
$$

then bounds $t$ away from zero and $u$ away from both zero and one.
The previous ceiling $E_3^{\rm all}\le1/[8r(r+1)]$ bounds $r$
above, while $r\ge r_*(t,u)\ge u/4$ bounds it below.
This is a necessary location result, not a proof of a substantial gap
inside that compact region, nor a claim that an optimum is attained.

The scientific decision is now clearer: stronger coupling, extreme
fields, increasingly separated rates and longer waiting do not provide
an asymptotic route to a fixed endpoint-prediction penalty in the
general-three-state regime. The existing exact state separation and
matched precision hierarchy remain valid. Their usefulness must be
judged as claims about reusing equilibrium models under intervention;
a practical storage, heat or device advantage remains unestablished.

## 5. Established tools and the scope of this result

The reversible Schur trace is standard. Avena, Castell, Gaudillière
and Mélot, [*Intertwining wavelets or multiresolution analysis on graphs through random forests*](https://arxiv.org/pdf/1707.04616v2),
Section 4.1, Lemma 8, prove its generator and reversibility properties;
Section 1.3 identifies the conditioned stationary measure.
Those properties alone do not compare the original and reduced processes
at the same physical times under changing fields.

Fornace and Lindsey, [*An approximation theory for Markov chain compression*](https://arxiv.org/html/2506.22918v3),
Section 4.1, Equations (52)–(53), use an induced generator with
committor-assigned stationary mass. It is generally different from the
bare trace used here; their Theorem 3 gives autonomous approximation
bounds. Grigoletto, Viola and Ticozzi,
[*Model Reduction for Controlled Quantum Markov Dynamics*](https://arxiv.org/html/2510.25546v1),
Section III, give exact reductions valid across controls.
Neither standard trace construction nor arbitrary-control reuse is
claimed as new here. The additional derivation is the explicit bound
(1), with its preparation, readout, common Gibbs law and all-word,
same-time quantifiers. This focused comparison does not settle priority.

All new conclusions are analytic. No simulation, optimizer, sampling
calculation or new numerical verifier is used. The field scope of (1)
is broader than the two-field compactness corollary; signed controls,
path observations, detector errors and microscopic validity of rapid
field changes require their own analysis.
