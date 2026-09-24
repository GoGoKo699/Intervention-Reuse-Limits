# Passive pairs need three states; one passive triple needs four

[Four controlled pair laws](FAMILIAR_SWITCH_MINIMAL_THEOREM.md) ·
[Equilibrium reduction](FAMILIAR_SWITCH_EQUILIBRIUM_REDUCTION.md) ·
[Existing matrix principle](MATRIX_RANK_PREDICTION_PRINCIPLE.md) ·
[Control and realization source comparison](FAMILIAR_SWITCH_CONTROL_SCOPE_SOURCE_AUDIT.md)

This note makes the observation boundary of the familiar-switch result
explicit. The four-state equilibrium target has a reversible three-state
model reproducing every passive initial/final pair law. Nevertheless, one
passive three-time law requires four states even without reversibility or
an equilibrium force rule. The controlled-pair minimum of three versus four
therefore concerns a specified prediction task, rather than compression of
the entire observed process into three Markov states.

The proof uses the standard conditional independence and past/future
factorization of a hidden Markov model. Neither that principle nor the
distinction between pair and sequence prediction is claimed as new. The
contribution here is its explicit application, positive error margin and
matching passive-pair construction for this target. All observations below
are ideal deterministic state observables. No detector or nondisturbing
measurement implementation is established.

## 1. Target and three-time statement

Use the equal-attempt two-switch model with dimensionless energy

$$
 E_h(S,Z)=-JSZ-hS,
 \qquad S,Z\in\{-1,+1\},\qquad 0<J<\infty.
 \tag{1}
$$

At zero field its single-coordinate flip rates are
$[1+e^{2JSZ}]^{-1}$. Time is measured in inverse attempt-rate units.
Put $t=\tanh J\in(0,1)$. The zero-field stationary law and generator
identities are

$$
 \pi_0(S,Z)=\frac{1+tSZ}{4},\qquad
 Q_0S=-S+tZ,\qquad Q_0Z=tS-Z.
 \tag{2}
$$

Prepare $\pi_0$, hold $h=0$, and retain the joint law $P$ of

$$
 (X,M,Y)=(S_0,S_a,S_{a+b}),\qquad a,b>0.
 \tag{3}
$$

The middle observation does not disturb the process. Define

$$
 c_r=e^{-r}\cosh(tr),\qquad d_r=e^{-r}\sinh(tr),
 \qquad C(r)=c_r+t d_r,
$$

$$
 D=(1-t^2)d_a d_b>0,
 \qquad
 \delta_{\rm triple}=\frac{\sqrt{1+D/2}-1}{2}>0.
 \tag{4}
$$

An admissible rival has a finite Markov state, a fixed deterministic binary
readout and an arbitrary initial distribution. Conditional on the counted
state at the middle time, future evolution is independent of the earlier
history. Its two successive transition kernels may be different and need
not be continuous-time propagators. The lower bound assumes neither
stationarity, detailed balance, a shared Gibbs force rule, a state-mass
floor nor bounded rates. Any persistent memory affecting future evolution
must belong to the counted state; current or earlier observations cannot
silently supply additional predictive memory.

**Three-time theorem.** Every such rival with at most three states has

$$
 \operatorname{TV}(P,P_R)\ge\delta_{\rm triple}.
 \tag{5}
$$

Consequently the minimum state count for reproducing this triple within
TV error $0\le\delta<\delta_{\rm triple}$ is four, both in the general
Markov class and in the ordinary reversible class. The physical target
attains zero error. The margin in (5) is a sufficient bound, not an exact
distance to the nearest three-state model.

## 2. Each middle-sign sector needs two states

The backward and forward target means, conditional on its full middle
state, are

$$
 \mathbb E[X\mid S_a,Z_a]=c_aS_a+d_aZ_a,
 \qquad
 \mathbb E[Y\mid S_a,Z_a]=c_bS_a+d_bZ_a.
 \tag{6}
$$

The backward equality uses target stationarity and detailed balance;
the forward equality follows from (2). Given the full middle state the
past and future are independent. Since
$\mathbb E[Z_a\mid M=s]=ts$ and
$\operatorname{Var}(Z_a\mid M=s)=1-t^2$, the law of total covariance
gives, for both $s=\pm1$,

$$
 \operatorname{Cov}(X,Y\mid M=s)=d_a d_b(1-t^2)=D>0.
 \tag{7}
$$

In contrast, if a rival's middle-sign sector is a singleton, conditioning
on that sign fixes its complete middle state. Its past and future are then
independent, for every initial preparation. If a sector is absent, its
entire triple slice vanishes. An at-most-three-state rival therefore has
at least one sign whose slice has rank at most one.

More explicitly, let

$$
 A_s(i,j)=\Pr(X=i,M=s,Y=j),\qquad i,j\in\{-1,+1\}.
 \tag{8}
$$

For any rival with middle-state sector $\Omega_s$, the Markov property gives

$$
 A^R_s(i,j)=\sum_{x\in\Omega_s}
 \Pr_R(X=i,\widehat X_a=x)\Pr_R(Y=j\mid\widehat X_a=x).
 \tag{9}
$$

Here $\widehat X_a$ denotes the counted rival state, not the binary sign
$X$. Thus $\operatorname{rank}_+(A^R_s)\le|\Omega_s|$, and ordinary
matrix rank gives a lower bound as well. For a binary conditional table,
its determinant is one quarter of its sign covariance. Since
$\Pr(M=s)=1/2$, (7) yields

$$
 \det A_s=\frac{D}{16}>0\qquad(s=\pm1).
 \tag{10}
$$

Both target slices have rank two, so exact matching requires at least two
states per sign and four in total. No target reversibility assumption has
been transferred to a rival in this argument.

## 3. A positive TV margin without conditioning on small rival masses

Let $\delta=\operatorname{TV}(P,P_R)$ and choose a rival sector with
slice $B$ of rank at most one. Its mass $q$ satisfies
$q\le1/2+\delta$. Let $A$ be the corresponding target slice, and
$A_r=(1-r)A+rB$, $0\le r\le1$.

For a nonnegative $2\times2$ matrix, the derivative of its determinant
has coefficients $(a_{22},-a_{21},-a_{12},a_{11})$. Extend these by zero
on the other four cells of the full triple. Their maximum minus minimum
is at most the mass of that slice: the largest diagonal entry plus the
largest off-diagonal entry is at most the sum of all four entries.
Integration along $A_r$, using the TV dual inequality for the difference
of the full probability laws, therefore gives

$$
 \begin{aligned}
 \frac{D}{16}
 &=|\det A-\det B|\\
 &\le\delta\int_0^1\operatorname{mass}(A_r)\,dr
 =\frac{\delta(1/2+q)}{2}
 \le\frac{\delta(1+\delta)}{2}.
 \end{aligned}
 \tag{11}
$$

Solving the quadratic inequality proves (5). The calculation remains
valid when the rival sector has zero probability. It imposes no
normalization or mass floor on a conditional rival table.

## 4. Every passive endpoint-pair law has a reversible three-state model

The target's stationary passive pair at any lag $r\ge0$ has probability

$$
 \Pr(S_0=i,S_r=j)=\frac{1+ijC(r)}4,
 \qquad
 C(r)=\frac{1+t}{2}e^{-(1-t)r}
       +\frac{1-t}{2}e^{-(1+t)r}.
 \tag{12}
$$

Construct a three-state birth-and-death generator with readout
$\widehat S=(-1,1,1)^T$ and positive rates

$$
 r_{12}=\frac{1-t^2}{2},\qquad
 r_{21}=\frac{1+t^2}{2},\qquad
 r_{23}=\frac{2t^2}{1+t^2},\qquad
 r_{32}=\frac{1-t^2}{1+t^2},
$$

$$
 \widehat Q=
 \begin{pmatrix}
 -r_{12}&r_{12}&0\\
 r_{21}&-r_{21}-r_{23}&r_{23}\\
 0&r_{32}&-r_{32}
 \end{pmatrix},\qquad
 \widehat\pi=
 \left(\frac12,\frac{1-t^2}{2(1+t^2)},\frac{t^2}{1+t^2}\right).
 \tag{13}
$$

All three stationary masses are positive, and the adjacent stationary
fluxes balance. Thus this connected chain is ordinarily reversible.
Introduce the auxiliary observable
$\widehat Z=(-t,-t,1/t)^T$. It is a predictor coordinate, not a physical
binary switch. Direct multiplication gives

$$
 \widehat Q\widehat S=-\widehat S+t\widehat Z,
 \qquad \widehat Q\widehat Z=t\widehat S-\widehat Z,
 \qquad
 \mathbb E_{\widehat\pi}[\widehat Z\mid\widehat S=s]=ts.
 \tag{14}
$$

The conditional endpoint means and balanced initial signs therefore
reproduce (12) at every lag, with one fixed generator and one stationary
preparation. Equivalently, its two nonzero decay rates are $1-t$ and
$1+t$ with the required weights in (12). This construction is only a
zero-field model; no controlled shared-force extension is asserted for it.

Two states cannot reproduce even the two passive endpoint-pair laws at
lags $a$ and $2a$, for any fixed $a>0$, when one common time-homogeneous
kernel is used for each interval of length $a$. Exact agreement at lag
$a$ forces a two-state model's initial law to be $(1/2,1/2)$ and its
kernel to be doubly stochastic. If the one-step correlation is $C(a)$,
the two-step correlation must then be $C(a)^2$. But the target has

$$
 C(2a)-C(a)^2=(1-t^2)d_a^2>0.
 \tag{15}
$$

Even arbitrary separate preparations for the two experiments cannot
avoid this conclusion: their exact balanced initial signs fix the law
on two deterministically read states. Thus these two pair laws already
have minimum three in both Markov and reversible classes, and (13)
matches the larger family of all passive pair laws. Allowing unrelated
kernels for different requested durations would change this task.

## 5. Exact triple error when the three pair marginals are retained

There is a sharper statement if a rival triple reproduces each of the
target's three pair marginals, at lags $a$, $b$ and $a+b$. All one-point
means are then zero. Write its remaining third moment as
$T_R=\mathbb E_R[XMY]$. The binary Fourier expansion is

$$
 P_R(i,s,j)=\frac18\left[
 1+isC(a)+sjC(b)+ijC(a+b)+isjT_R\right].
 \tag{16}
$$

The target has $T=0$ by simultaneous spin-reversal symmetry, and

$$
 C(a+b)-C(a)C(b)=(1-t^2)d_a d_b=D.
 \tag{17}
$$

For a singleton rival sign $s$, conditional independence gives

$$
 0=\operatorname{Cov}_R(X,Y\mid M=s)=D+sT_R.
 \tag{18}
$$

Every at-most-three-state rival with these pair marginals therefore has
$|T_R|=D$. Equations (16) and $T=0$ show that its triple error is exactly

$$
 \operatorname{TV}(P,P_R)=\frac{D}{2}.
 \tag{19}
$$

The reversible chain (13) attains this value: it matches all pair laws
and has singleton sign $-1$, so $T_R=D$. Hence $D/2$ is the exact optimum
within the additional constraint of matching the three pair marginals,
in both the general and reversible classes with at most three states.
It is not asserted to be the unrestricted optimum in (5).

## 6. Three different prediction tasks

For the same four-state target with $0<J<\infty$, the exact counts are:

| Requested ideal data | General Markov minimum | Ordinary reversible minimum | Shared structure needed for the lower bound |
| --- | ---: | ---: | --- |
| Passive endpoint pairs at lags $a,2a$; also all passive lags | 3 | 3 | One zero-field kernel and its repeated use |
| Four controlled endpoint pairs $0,H,0H,H0$ | 3 | 4 | The common kernels and Gibbs force interface of the minimal theorem |
| One passive triple $(S_0,S_a,S_{a+b})$ | 4 | 4 | Markov evolution through a counted state and deterministic readout |

The middle row is the [existing controlled-pair theorem](FAMILIAR_SWITCH_MINIMAL_THEOREM.md)
for finite $H>0$ and positive dwell times. Its upper model reproduces
initial/final pairs under all nonnegative field protocols; that promise
does not include intermediate observations. The first and last rows need
no field switch, so they impose no nontrivial force-interface condition.

This comparison changes a concrete model-selection decision. A reversible
three-state model is sufficient when only the stationary passive pair
family is requested. It cannot represent even one of the target's ideal
three-time laws. Conversely, a three-state controlled pair predictor does
not by itself justify a three-state Markov reduction of the observed
trajectory. At the level of the target's observable closure, propagation
preserves $\operatorname{span}\{1,S,Z\}$, whereas conditioning on an
intermediate sign multiplies observables by
$\mathbf1_{S=s}=(1+sS)/2$ and introduces $SZ$ when applied to $Z$.
The three-dimensional endpoint closure alone supplies no closure under
this conditioning operation.

An actual readout that changes the hidden state or leaves persistent
detector memory defines a different temporal law. None of the detector
contracts for endpoint acquisition automatically supplies the ideal
middle observation used here. Non-Markov predictors with additional
history-dependent information are also outside the finite-state Markov
count. The results concern state cardinality, not a memory-bit saving or
a thermodynamic work cost.

## 7. Relation to the broader rank question

Equation (9) generalizes immediately to arbitrary finite past and future
records around a deterministic middle readout: their probability matrix
in sector $s$ factors through the states in that sector. Thus the sum of
the sector matrix ranks, or nonnegative ranks, bounds the total state
count. This is a standard hidden-state factorization, and the repository
already develops more substantial [positive versus Gram matrix bounds](MATRIX_RANK_PREDICTION_PRINCIPLE.md).
For a primary observable-operator precedent, Hsu, Kakade and Zhang,
[“A Spectral Algorithm for Learning Hidden Markov Models,” §2.1 and Lemma 1](https://arxiv.org/pdf/0811.4413),
state the conditional independence and observation-operator product rule.
Their learning theorem is not invoked here; its emission-rank assumptions
are not satisfied by a binary readout with more than two hidden states.

The analogous attempt to turn many separately prepared controlled pair
experiments into one conditional-response covariance matrix needs an
additional preparation premise. A shared stationary conditional law makes
those response covariances well defined and gives the usual rank bound
by the number of hidden states per sector minus one. Arbitrary unrelated
preparations for different words do not in general supply that common
covariance. The singleton four-word obstruction avoids this problem
because conditioning on the singleton sign fixes the state. The temporal
law in (3) instead uses one actual joint distribution, so its factorization
needs no stationary preparation assumption on a rival. These are useful
scope distinctions, not a new general realization principle.
