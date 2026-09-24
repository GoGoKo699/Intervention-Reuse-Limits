# Four endpoint-pair laws: three predictive states, four reversible states

This note extracts the elementary theory result from the existing
[positive realization](FAMILIAR_SWITCH_STRUCTURE.md),
[conditional-covariance identity](FAMILIAR_SWITCH_SNAPSHOT_ROBUSTNESS.md),
and [preparation-free return test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md).
It concerns ideal observables of a specified Markov state process. It
does not require a detector construction or a finite experimental sample
count, and does not establish that a physical instrument measures these
observables with any prescribed accuracy.

Detailed-balance reciprocity, the heat-bath moment equations and positive
Markov realizations are established ingredients. The statement below
combines the existing repository construction and obstruction on one
four-word prediction task; it is not a new attribution claim for those
ingredients. The [physical-assumption alignment](PHYSICAL_ASSUMPTION_ALIGNMENT.md)
and close prior-art comparison remain separate requirements.

## 1. Model, task and theorem

Let $S,Z\in\{-1,+1\}$ be two time-even configurations, with energy
in units of $k_{\rm B}T$ and unit-attempt heat-bath rates

$$
 E_h(S,Z)=-JSZ-hS,
 \qquad
 q_S(S,Z)=\frac1{1+e^{2S(h+JZ)}},\qquad
 q_Z(S,Z)=\frac1{1+e^{2JZS}}.
 \tag{1}
$$

Fix any finite $J,H>0$ and any finite $\tau_0,\tau_H>0$. At every
fixed field the four-state generator is ordinarily reversible for its
Boltzmann law. Define $K_0=e^{\tau_0Q_0}$ and
$K_H=e^{\tau_HQ_H}$. Prepare the low-field equilibrium $\pi_0$ and
record the true initial and final signs of $S$ for each chronological
word

$$
 \mathcal W=\{0,H,0H,H0\}.
 \tag{2}
$$

Only these four binary pair laws are requested. There are no
intermediate observations.

A predictive model has one finite state space, a deterministic binary
readout, fixed kernels $\widehat K_0,\widehat K_H$, and strictly
positive stationary laws satisfying

$$
 \widehat\pi_0\widehat K_0=\widehat\pi_0,\quad
 \widehat\pi_H\widehat K_H=\widehat\pi_H,\quad
 \widehat\pi_H(x)
 =\frac{\widehat\pi_0(x)e^{H\widehat S(x)}}
        {\sum_y\widehat\pi_0(y)e^{H\widehat S(y)}}.
 \tag{3}
$$

The ordinary class additionally requires detailed balance at both
fields. Each word may start from a different arbitrary predictive
preparation. No equal stationary sign masses, equilibrium preparation,
state-mass floor or mixing bound is imposed on a rival. The same active kernels and readout
must nevertheless serve all four words. A preparation operation can be
included before the true initial sign is defined at the word boundary.

Let $D_{\rm all}(\delta)$ and $D_{\rm ord}(\delta)$ be the minimum
numbers of states in these two classes whose maximum TV error over the
four complete pair laws is at most $\delta$.

**Theorem.** For every parameter choice above,

$$
 D_{\rm all}(0)=3,\qquad D_{\rm ord}(0)=4.
 \tag{4}
$$

Both upper models are genuine continuous-time Markov chains. The
ordinary lower bound holds even for arbitrary reversible stochastic
kernels, whether or not they are continuous-time propagators.
Consequently (4) also holds when both classes are restricted to
continuous-time models with the prescribed dwell times.

## 2. A singleton sector obeys a reciprocal return identity

Put $u=\tanh H$. For a word $w$ and a sign whose initial probability
is nonzero, write

$$
 r_{w,s}=\Pr(S_{\rm final}=s\mid S_{\rm initial}=s,w),
$$

and define

$$
 R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}
                  +2su\,r_{0,s}r_{H,s}.
 \tag{5}
$$

An at-most-three-state model with both visible signs has a singleton
sector, say state $j$ with sign $s$. Conditional on that sign, every
preparation starts the word at $j$. Thus its single-word returns are
the two diagonal kernel entries, and its two-word returns are the
corresponding diagonal entries of the two kernel products.

Every other state $k$ has sign $-s$. Detailed balance and (3) imply

$$
 (\widehat K_0)_{jk}(\widehat K_H)_{kj}
 =\frac{1+su}{1-su}
   (\widehat K_H)_{jk}(\widehat K_0)_{kj}.
 \tag{6}
$$

Separate the term $k=j$ in each diagonal product. Equation (6) gives
$R_s=0$. The normalization in (3) cancels, so this conclusion needs
no stationary balance condition. The arbitrary per-word
preparations also disappear after conditioning on a singleton sign.

## 3. Both target residuals are explicitly nonzero

Set

$$
 t=\tanh J,\qquad
 B=\frac{t(1-u^2)}{1-t^2u^2},\qquad
 \kappa=\sqrt{tB},
$$

$$
 d_0=e^{-\tau_0}\sinh(t\tau_0),\qquad
 \gamma=e^{-\tau_H}\frac{B}{\kappa}\sinh(\kappa\tau_H).
 \tag{7}
$$

All these quantities are positive, with $t,u,\kappa<1$. The
heat-bath equations leave the span of $1,S,Z$ invariant. In particular,
$K_0S$ has $Z$ coefficient $d_0$, and $K_HS$ has $Z$ coefficient
$\gamma$. The target low equilibrium has

$$
 \mathbb E_0[Z\mid S=s]=ts,\qquad
 \operatorname{Var}_0(Z\mid S=s)=1-t^2.
$$

The detailed-balance covariance identity gives

$$
 R_s=-\frac{su}{2}
        \operatorname{Cov}_0(K_0S,K_HS\mid S=s)
     =-s g,
 \qquad
 g:=\frac u2 d_0\gamma(1-t^2)>0.
 \tag{8}
$$

For a direct verification of its first equality, let
$G_s=K_0\mathbf1_{S=s}$ and $F_s=K_H\mathbf1_{S=s}$.
Move the first kernel in each two-word return using its detailed
balance law, and use $\pi_H\propto\pi_0(1+uS)$ in the high-field
term. Their weighted difference is
$-2su\,\mathbb E_0[G_sF_s\mid S=s]$.
Adding the last term of (5) leaves
$-2su\operatorname{Cov}_0(G_s,F_s\mid S=s)$, while
$\operatorname{Cov}(G_s,F_s\mid S=s)
=\operatorname{Cov}(K_0S,K_HS\mid S=s)/4$.

Thus neither sign can be a singleton in an ordinary exact predictor.
At least two states are needed in each readout sector, proving the
ordinary lower bound of four. The physical target attains it.

## 4. A positive three-state predictor supplies the other upper

The general construction is reproduced here to distinguish a positive
Markov realization from a merely three-dimensional linear closure.
Put

$$
 d=3t,\qquad e=\frac{1-t^2}{2t},\qquad W=d+e,
$$

$$
 \widehat S=(-1,1,1)^T,\qquad
 \widehat Z=(-t,-2t,t+e)^T,\qquad
 \widehat\pi_0=\left(\frac12,\frac{e}{2W},\frac{d}{2W}\right).
 \tag{9}
$$

For a finite field $h\ge0$, set $m_h=\tanh h$ and

$$
 A_h=\frac{m_h(1-t^2)}{1-t^2m_h^2},\qquad
 B_h=\frac{t(1-m_h^2)}{1-t^2m_h^2},\qquad
 L_h=\frac{1+A_h-B_ht}{2}.
$$

Use the off-diagonal rates

$$
 \begin{aligned}
 q_{12}&=L_h(2t+e)/W,&q_{13}&=L_h(d-2t)/W,\\
 q_{21}&=(1-A_h+2B_ht)/2,&
 q_{23}&=[d+q_{21}(2t-d)]/W,\\
 q_{31}&=(1-A_h-B_h(t+e))/2,&
 q_{32}&=[e-q_{31}(2t+e)]/W,
 \end{aligned}
 \tag{10}
$$

with diagonal entries minus row sums. These are the frozen formulas
(G1)--(G7) of the structural theorem. Its positive-rate proof uses

$$
 0<q_{21}<\frac32,\qquad
 q_{31}=\frac{(1-t^2)(1-m_h)^2}{4(1-t^2m_h^2)}>0,
$$

$$
 e-q_{31}(2t+e)\ge\frac{3(1-t^2)^2}{8t}>0,
 \qquad d+q_{21}(2t-d)=t(3-q_{21})>0.
$$

Together with $L_h>0$ and $d-2t=t>0$, these establish all six
positive rates for every finite $h\ge0$.

Direct multiplication gives the common target/predictor mean equations

$$
 Q_hS=A_h-S+B_hZ,\qquad Q_hZ=tS-Z.
 \tag{11}
$$

In the predictor these hold for the hatted coordinates. Its reference
law obeys

$$
 \widehat\pi_0\widehat S
 =\widehat\pi_0\widehat Z=0,\qquad
 \widehat\pi_0\widehat S\widehat Z=t,
 \qquad \widehat\pi_0(\widehat S=s)=\frac12.
 \tag{12}
$$

Consequently its tilted law
$\widehat\pi_h=\widehat\pi_0(1+m_h\widehat S)$ has means
$(\widehat S,\widehat Z)=(m_h,tm_h)$. Equation (11) annihilates
these means because $A_h=(1-tB_h)m_h$.
The three coordinates $1,\widehat S,\widehat Z$ form a basis, so
this proves stationarity of the full tilted law.

Equation (12) also gives
$\mathbb E_0[\widehat Z\mid\widehat S=s]=ts$.
Conditional on either initial sign, the target and predictor thus
start with identical coordinate means $(S,Z)=(s,ts)$.
Their shared equations propagate those means through every finite
nonnegative-field protocol. Equality of the conditional final binary
means and the initial sign probabilities proves equality of the full
initial/final pair laws, including all four words (2).

The auxiliary coordinate $\widehat Z$ is not a second measured spin
and need not lie in $[-1,1]$. This construction does not identify a
physical partition of the four target configurations. Nor does it
assert equality of joint laws with intermediate observations.

Finally, every two-state stationary stochastic kernel obeys detailed
balance: its single stationary flux equation is the detailed-balance
equation. A general two-state predictor would therefore be excluded
by the ordinary lower bound. This proves (4).

## 5. A parameter-dependent positive accuracy interval

Every target initial sign has probability $1/2$. If a rival's pair
table differs by TV at most $\delta<1/2$, each conditional return
probability differs by at most

$$
 \epsilon=\frac{\delta}{1/2-\delta}.
 \tag{13}
$$

To see this, for events $A=\{S_i=s,S_f=s\}\subseteq B=\{S_i=s\}$
let $r=P(A)/P(B)$. The function $\mathbf1_A-r\mathbf1_B$ has
oscillation one and target mean zero. Its rival mean is bounded by
$\delta$, while the rival probability of $B$ is at least $1/2-\delta$.

On $[0,1]^4$, (5) has maximum-norm Lipschitz constant $2+4u$:
the two linear terms cost $2\epsilon$, and the product term costs
at most $4u\epsilon$. Therefore an ordinary singleton cannot fit
all four tables whenever

$$
 (2+4u)\frac{\delta}{1/2-\delta}<g.
$$

Together with the exact upper models, this proves

$$
 \boxed{D_{\rm all}(\delta)=3,\qquad
 D_{\rm ord}(\delta)=4,\qquad
 0\le\delta<\frac{g}{2(2+4u+g)}.}
 \tag{14}
$$

The interval is positive for each fixed nondegenerate parameter
choice. It is not a uniform lower radius over the whole model family.
The explicit $g$ tends to zero as coupling or field vanishes, as either
pulse duration vanishes, or as either pulse becomes infinitely long
with the remaining parameters fixed. Strong-coupling and infinite-field
limits can also close this particular margin. Those limits are outside
the finite positive parameter claim or its uniform interpretation.

The independently certified one-percent kinetic neighborhood at the
selected operating point is a separate robustness result. Equation
(14) does not extend that same numerical neighborhood to every coupling,
field or pair of dwell times.

## 6. The consequence and its limits

Within the shared-force class, every exact three-state predictor must
violate ordinary detailed balance at at least one fixed field. For a
continuous-time predictor, at least one stationary edge current
$\widehat\pi_h(i)\widehat Q_h(i,j)
-\widehat\pi_h(j)\widehat Q_h(j,i)$ is therefore nonzero.
The four-state target has zero such currents at both fields.

For the explicit construction (10), the zero-field current on edge
$1\to2$ is $t^2(1-t^2)/[4(1+5t^2)]>0$. Its high-field current can
vanish at a special field; the assertion is at least one field, not both.

This is a state-count cost of retaining equilibrium reversibility in
a specified controlled prediction task. The pulse experiment itself
is driven; it is not an equilibrium trajectory throughout the word.
The smaller model's stationary currents are a property of its
predictive representation, not evidence that the target has stationary
currents or a deduction of the predictor's thermodynamic cost.

Ordinary exact state lumping of a reversible chain preserves detailed
balance. The positive three-state predictor is a different type of
realization, fitted to the specified endpoint data rather than obtained
as such a lumping. The theorem does not say that observing fewer
time-even variables destroys equilibrium reversibility of the full
observed path law. That path law is not the task being compressed.

The common force coupling, deterministic readout and ordinary reversal
remain substantive comparison premises. A physical implementation of
the circulating predictor, the role of odd hidden variables, and the
resources needed to realize its currents are not settled here. No
generalized-reversal, heat-cost, device feasibility or complete-path
equivalence statement follows from (4) or (14).
