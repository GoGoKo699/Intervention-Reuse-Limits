# Four snapshot types without an equilibrium-preparation promise for rivals

The four types $0H,H0,0,H$ give an exact three-versus-four state advantage
throughout the existing independent $1\%$ kinetic box. The ordinary
comparison now permits an arbitrary preparation for each type. No common
preparation, stationary preparation, reset time, hidden-state mixing rate,
or balanced stationary readout is required of those rivals.

The added single-plateau types serve two purposes. Conditioning on a
singleton readout sector removes the rival's preparation from a simple
return-probability identity. At the stationary physical target, the two
extra pair laws are already determined by the original four moments, so
the existing positive three-state continuous-time realization fits all
four types exactly.

This note concerns faithful, noiseless initial and final readouts of the
true binary state label. It does not transfer an earlier detector model,
sampling guarantee, or full recorded-trajectory realization. The target
is still prepared at its low-field equilibrium. Removing a preparation
promise from the rival class does not assert target power under every
possible target preparation.

## 1. Shared controls and the enlarged comparison class

Use the target and independent edge-prefactor box of the
[one-percent kinetic proof](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md):

$$
 J=\log3,\qquad h_0=0,\qquad H=\log2,\qquad
 u=\tanh H=\frac35,\qquad \tau_0=\tau_H=\frac54.
 \tag{1}
$$

Each of the four undirected heat-bath edges at each field has an
independent factor in $[.99,1.01]$, multiplying both directional rates.
The four-state target therefore remains ordinarily reversible with its
unchanged Gibbs stationary laws. Every target type starts from its
balanced low-field equilibrium $\pi$.

A rival has one finite state space, a fixed deterministic readout
$S\in\{-1,+1\}$, and fixed stochastic kernels $K_0,K_H$. Its strictly
positive stationary laws obey

$$
 \pi_0K_0=\pi_0,\qquad \pi_HK_H=\pi_H,\qquad
 \pi_H(x)=\frac{\pi_0(x)e^{HS(x)}}{\sum_y\pi_0(y)e^{HS(y)}}.
 \tag{2}
$$

The ordinary class additionally requires detailed balance for each
kernel with its stated stationary law. The lower proof allows arbitrary
stochastic kernels, so also applies to continuous-time Markov
propagators with no rival rate cap. No constraint on $\pi_0S$ is imposed.

Each word $w\in\{0H,H0,0,H\}$ may start from its own arbitrary law
$\nu_w$. The two occurrences of a given field kernel are nevertheless
the same operation wherever that field appears. Field-dependent
feedback, a different kernel for each word, or an additional between-
plateau instrument would define a different task.

An initial hidden-state kick may be included if it preserves $S$ on
every state. For the null argument it need not preserve $\pi_0$:
conditioning on a singleton sector makes such a kick act trivially.
The initial record is the true sign, and the final record is the true
sign at the end of the word.

[Exact verifier](../scripts/verify_switch_preparation_free.py) ·
[Certificate report](../reports/switch_preparation_free.json).

Let $P_w$ be the target pair law and $\widehat P_w$ the rival pair law.
Measure prediction error by

$$
 \delta_{\rm pair}
 =\max_{w\in\{0H,H0,0,H\}}
    \operatorname{TV}(P_w,\widehat P_w).
 \tag{3}
$$

## 2. A singleton return identity independent of preparation

For every type and sign with positive initial probability, define

$$
 r_{w,s}=\Pr(S_{\rm final}=s\mid S_{\rm initial}=s,w),
 \qquad s\in\{-1,+1\}.
$$

Suppose sector $s$ consists of a single state $j$. Then conditioning
on the true initial sign fixes the hidden initial state to $j$ for
every preparation. Consequently

$$
 r_{0,s}=(K_0)_{jj},\quad r_{H,s}=(K_H)_{jj},\quad
 r_{0H,s}=(K_0K_H)_{jj},\quad
 r_{H0,s}=(K_HK_0)_{jj}.
 \tag{4}
$$

Every $k\ne j$ has sign $-s$. Detailed balance and (2) give

$$
 (K_0)_{jk}(K_H)_{kj}
 =\frac{\pi_0(k)\pi_H(j)}{\pi_0(j)\pi_H(k)}
    (K_H)_{jk}(K_0)_{kj}
 =\frac{1+su}{1-su}(K_H)_{jk}(K_0)_{kj}.
 \tag{5}
$$

Separate the term $k=j$ in the two matrix products. Equation (5)
proves the bounded-coefficient identity

$$
 \boxed{\mathcal R_s
 =(1-su)r_{0H,s}-(1+su)r_{H0,s}
       +2su\,r_{0,s}r_{H,s}=0.}
 \tag{6}
$$

Every model with two nonempty readout sectors and at most three states
has a singleton sector. Hence every ordinary model in that class obeys
$\mathcal R_-=0$ or $\mathcal R_+=0$, even when its preparation differs
arbitrarily between the four words. The stationary sector masses and
the initial sector probabilities need not agree with one another.

The shared Gibbs tilt and ordinary detailed balance are substantive
premises in (5). The argument does not infer them from observed return
frequencies.

## 3. The stationary target violates both identities

Write the target moments of $0H,H0$ as

$$
 m=\pi K_0K_HS,\qquad c=\pi S K_0K_HS,\qquad
 \ell=\pi K_HK_0S,\qquad d=\pi S K_HK_0S.
 \tag{7}
$$

Here a row such as $\pi S$ means componentwise multiplication by the
readout. The initial mean is zero for all four target types. Define
$G=K_0S$ and $F=K_HS$. Low-field detailed balance gives the usual
conditional covariance identity

$$
 \mathcal R_s
 =-\frac{su}{2}\operatorname{Cov}_{\pi}(G,F\mid S=s)
 =\frac{1-su}{2u}\mathcal H_s,
 \tag{8}
$$

where the existing latent snapshot witness is

$$
 \mathcal H_s
 =uc-u(1+sm)d+s(u-m)\ell.
 \tag{9}
$$

For clarity, (8) can be obtained directly with the return functions
$G_s=K_0\mathbf1_{S=s}$ and $F_s=K_H\mathbf1_{S=s}$.
Detailed balance at the two fields splits the two-word returns into
contributions from sectors $s$ and $-s$. It gives

$$
 r_{0H,s}-\frac{1+su}{1-su}r_{H0,s}
 =\left(1-\frac{1+su}{1-su}\right)
     \mathbb E_{\pi}[G_sF_s\mid S=s].
$$

Subtract the corresponding product of conditional means, multiply by
$1-su$, and use
$\operatorname{Cov}(G_s,F_s\mid S=s)
=\operatorname{Cov}(G,F\mid S=s)/4$.
This proves the first equality of (8); the second is the covariance
identity in the [snapshot proof](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md).

The preparation-free verifier reuses the exact degree-two moment
polynomials and remainder bounds of the kinetic certificate. It
substitutes those polynomials into (8)--(9), retaining every resulting
term through degree four, and bounds the weighted sum of the absolute
nonconstant coefficients on the full eight-dimensional $1\%$ box.
The moment remainders are charged separately using rational derivative
bounds. This is a polynomial enclosure of the whole box, not a sampled
parameter grid or a new moment-closure assumption.

The report gives the following outward decimal enclosures; the displayed
endpoints are rational numbers rounded outwards from its exact bounds:

| Target residual | Lower bound | Upper bound |
| --- | ---: | ---: |
| $\mathcal R_-$ | $.0090387$ | $.0107927$ |
| $\mathcal R_+$ | $-.0107334$ | $-.0090980$ |

In particular, throughout the entire kinetic box,

$$
 \boxed{\mathcal R_->\frac9{1000},\qquad
        \mathcal R_+<-\frac9{1000}.}
 \tag{10}
$$

An independent, weaker consequence of the previous kinetic report is
$\mathcal R_->.005$ and $\mathcal R_+<-.005$: use its noiseless
$\mathcal H_->.00389$ and $c-d\le-.017576$, together with
$\mathcal H_++\mathcal H_-=2u(c-d)$ and (8).
The stronger enclosure (10) is the numerical premise used below.

Thus both target residuals stay uniformly away from zero. No hidden
mixing estimate for a rival appears in this target calculation.

## 4. The existing three-state model fits all four types

Only stationarity and the tilt, not detailed balance or heat-bath
moment closure, are needed for this upper bound. Let a model have a
balanced stationary low law $\pi$ and tilted stationary high law
$\pi_H=\pi(1+uS)$. Define its four moments by (7).
Low-field stationarity first gives $m=\pi K_HS$. Put

$$
 a=\pi S K_HS,\qquad x=\pi S K_0S.
$$

High-field stationarity gives

$$
 m+ua=\pi_HK_HS=\pi_HS=u,
$$

and

$$
 \ell+ud=\pi_HK_HK_0S=\pi_HK_0S=ux.
 \tag{12}
$$

Consequently the added single-plateau moments are fixed:

| Word | Initial mean | Final mean | Initial--final correlation |
| --- | ---: | ---: | ---: |
| $0$ | $0$ | $0$ | $x=(\ell+ud)/u$ |
| $H$ | $0$ | $m$ | $a=1-m/u$ |

A binary pair law is determined by these three moments; when the
initial mean is zero its entries are
$[1+jm+ijc]/4$, with $i,j\in\{-1,+1\}$ and the appropriate final
mean and correlation for the word.

The [local snapshot realization](FAMILIAR_SWITCH_LOCAL_SNAPSHOT_REALIZATION.md)
fits exactly $(m,c,\ell,d)$ and uses precisely the parameters
$x=(\ell+ud)/u$ and $a=1-m/u$. It has the balanced law
$(1/2,1/22,5/11)$, the same Gibbs tilt, positive kernels, and positive
continuous-time generator rates throughout the certified kinetic box.
Equation (12) therefore proves that this same fixed three-state model
also fits $0$ and $H$ exactly. No new fit, fifth parameter, or extension
of its matrix-logarithm domain is required.

If a target initial kick $D$ preserves both the readout sectors and
$\pi$, then
$\pi\mathbf1_{S=s}D=\pi\mathbf1_{S=s}$ for each $s$.
Its stationary initial-label/post-kick joint law is therefore the ideal
stationary one. Such kicks leave all four target pair laws unchanged;
the predictor may use the identity kick. This equilibrium preservation
is needed for the target upper, whereas the singleton lower permits
arbitrary sector-preserving kicks.

The construction reproduces four specified initial/final pair laws.
It does not reproduce a trajectory with intermediate observations,
all raw repeated-readout records, or an arbitrary target instrument.

## 5. A finite joint-table error interval

Suppose each rival pair table is within TV $\delta<1/2$ of its target
table. The target initial probability of each sign is $1/2$, so the
rival probability is at least $1/2-\delta$. In particular both
conditional returns are defined for each type.

For completeness, conditional probabilities obey the sharp elementary
bound

$$
 |\widehat r_{w,s}-r_{w,s}|
 \le\epsilon:=\frac{\delta}{1/2-\delta}.
 \tag{13}
$$

Indeed let $B$ be the event that the initial sign is $s$, let $A$ be
the event that both signs are $s$, and put $r=P(A)/P(B)$.
The function $f=\mathbf1_A-r\mathbf1_B$ has oscillation at most one
and $Pf=0$. Hence $|\widehat Pf|\le\operatorname{TV}(P,\widehat P)$,
while $\widehat Pf=\widehat P(B)(\widehat r-r)$, proving (13).

All return probabilities lie in $[0,1]$, so
$|\widehat r_0\widehat r_H-r_0r_H|\le2\epsilon$.
The residual (6) therefore has the uniform Lipschitz bound

$$
 |\widehat{\mathcal R}_s-\mathcal R_s|
 \le(2+4u)\epsilon=\frac{22}{5}\epsilon.
 \tag{14}
$$

There is no additional quadratic term: the product bound already uses
the probability range of the actual and rival factors.

For $\delta=1/1000$, equation (13) gives $\epsilon=1/499$ and therefore

$$
 |\widehat{\mathcal R}_s-\mathcal R_s|
 \le\frac{22}{2495}<\frac9{1000}.
 \tag{15}
$$

This contradicts (10) in whichever sector is a singleton. Thus every
ordinary rival with at most three states has maximum pair-table error
strictly greater than $1/1000$, without any preparation promise.

Every two-state stationary stochastic kernel is ordinarily reversible:
its single stationarity flux equation is detailed balance. A general
rival with at most two states therefore also obeys the same lower
bound. The exact three-state construction supplies the general upper,
and the physical four-state target supplies the ordinary upper. In the
comparison class of Section 1, including its arbitrary per-word
preparations, the minima are consequently

$$
 \boxed{D_{\rm all}(\delta)=3,\qquad D_{\rm ord}(\delta)=4,
 \qquad 0\le\delta\le\frac1{1000}.}
 \tag{16}
$$

The lower bound also applies when both classes are restricted to
continuous-time generators. Both exact upper models are already
continuous-time realizations.

## 6. Scope and experimental boundary

The preparation promise has been removed from the ordinary null by
changing the data task from two pair laws to four. The target power and
exact upper here use stationary target preparation, nominal fields and
dwell times, the independent $1\%$ kinetic box, and faithful initial and
final labels. The null still requires the shared equilibrium tilt,
ordinary detailed balance, one fixed model across words, and
sector-preserving initial measurement.

Electronic sign errors can mix the singleton sector with the other
sector when conditioning on the recorded initial bit. They therefore
require a separate analysis; arbitrary unknown detector noise is not
covered by (6). Neither an earlier five-million-trial allocation nor its
thresholds are inherited from the population-law theorem. Full raw
readout transcripts and approximate instrument or force-law budgets
also need their own bounds. Manuscript drafting remains deferred.
