# A reversible realization at fixed coupling for every chain length

[Assessment](FAMILIAR_CHAIN_SHARPNESS.md) · [Finite lower bound](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md) · [Source comparison](FAMILIAR_CHAIN_SHARPNESS_SOURCE_AUDIT.md)

An open chain of $n$ interacting heat-bath switches admits an exact
reversible predictor with **$2n$ states**, for every $n\ge3$ in one fixed
weak-coupling interval. The interval does not shrink with chain length.
This attains the existing lower bound under the same physical field and
preparation convention.

## 1. Statement and conventions

Use the homogeneous open-chain energy and attempt-time units from the
[positive realization](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md):

$$
E_h=-J\sum_{j=0}^{n-2}X_jX_{j+1}-hX_0,
\qquad t=\tanh J,\quad m=\tanh h,\quad S=X_0.
$$

For every

$$
n\ge3,\qquad 0<t\le\frac1{64},\qquad |m|\le\frac12,
\tag{1}
$$

there is a $2n$-state continuous-time Markov family with one common
preparation $\rho_0$, deterministic readout $\widehat S\in\{-1,+1\}$,
and stationary laws

$$
\rho_m=\rho_0(1+m\widehat S).
\tag{2}
$$

Every generator satisfies detailed balance, all its off-diagonal rates
are strictly positive, and every total exit rate is at most
$1+2t\le33/32$. From the common preparation it matches every physical
endpoint-pair law for every finite word of fields in (1), with arbitrary
positive dwell times. The constant $1/64$ is sufficient, not optimal.

Combining this construction with the existing
[general upper](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md) and
[finite lower bounds](FAMILIAR_CHAIN_REVERSIBLE_BOUND.md) gives

$$
D_{\rm all}=n+1,\qquad D_{\rm ord}=2n.
\tag{3}
$$

Equation (3) holds both for all nonnegative protocols with $0\le m\le1/2$
and for the finite three-field menu in the lower-bound note. Choose any
three distinct tilts in $[0,1/2]$ and any positive clock for the exact
finite-menu statement. Choose the lowest tilt to be zero to use the
same explicit positive TV radius for both state minima. That radius
depends on the instance. The reversible upper alone permits signed
fields; the general $(n+1)$-state upper has the stated nonnegative-field
scope.

## 2. Common moment coordinates

Index physical coordinates by $0,\ldots,n-1$. Write

$$
C_{ab}=t^{|a-b|},\qquad T_a=t^a,\qquad c=\frac{t}{1+t^2},
\qquad d=1-t^2.
$$

Here $C$ is the physical raw spin second-moment matrix, at every boundary
field, and the physical mean is $mT$. A Cholesky factor $C=LL^{\mathsf T}$
is

$$
L_{a0}=t^a,\qquad L_{ab}=\sqrt d\,t^{a-b}\ (1\le b\le a),
\qquad L_{ab}=0\ (b>a).
$$

Let $\phi_i=(i+1/2)\pi/n$ and define the orthogonal cosine matrix

$$
U_{i0}=\frac1{\sqrt n},\qquad
U_{ik}=\sqrt{\frac2n}\cos(k\phi_i),\quad 1\le k<n.
$$

Orthogonality follows from the finite cosine sum. Set
$V=\sqrt n\,UL^{\mathsf T}$, and let $v_i^{\mathsf T}$ be its rows.
Then

$$
(v_i)_0=1,\quad \frac1n\sum_i v_i=T,\quad
\frac1n\sum_i v_iv_i^{\mathsf T}=C,\quad
v_i^{\mathsf T}C^{-1}v_j=n\delta_{ij}.
\tag{4}
$$

Use states $a=(s,i)$, with $s=\pm1$ and $0\le i<n$. Their coordinate
vectors and probabilities are

$$
x_a=sv_i,\qquad \widehat S(a)=s,\qquad
\rho_m(a)=\frac{1+ms}{2n}.
\tag{5}
$$

Only $x_0=\widehat S$ is a physical output of this predictor. The other
coordinates are auxiliary real-valued functions, not additional measured
spins. Equations (4)–(5) give the physical conditional initial means
$\mathbb E_0[x\mid\widehat S=s]=sT$. Define centered coordinates
$y_a=x_a-mT$, the matrix $Y$ whose rows are $y_a^{\mathsf T}$, and
$W=\operatorname{diag}(\rho_m)$. Their covariance is

$$
R=Y^{\mathsf T}WY=C-m^2TT^{\mathsf T}=LDL^{\mathsf T},
\qquad D=\operatorname{diag}(1-m^2,1,\ldots,1).
\tag{6}
$$

## 3. Extend the physical mean dynamics

Write the column-vector physical mean equation as
$\dot\mu=a+(-I+K)\mu$. The nonzero entries of $K$ are

$$
K_{01}=B=\frac{t(1-m^2)}{1-t^2m^2},\qquad
K_{j,j-1}=K_{j,j+1}=c\ (1\le j\le n-2),\qquad
K_{n-1,n-2}=t.
$$

The affine vector is $a=Ae_0$, with
$A=m(1-t^2)/(1-t^2m^2)$. Physical stationarity and detailed balance imply

$$
a+(-I+K)mT=0,\qquad KR=RK^{\mathsf T}.
\tag{7}
$$

Let $\boldsymbol1$ denote the constant column on the $2n$ states and set

$$
\Pi=\boldsymbol1\rho_m,\qquad
P=YR^{-1}Y^{\mathsf T}W,\qquad P_\perp=I-\Pi-P,
\qquad \theta=\frac16.
$$

These are mutually orthogonal projections in $L^2(\rho_m)$. Define

$$
\widehat Q_m=-I+\Pi+YK^{\mathsf T}R^{-1}Y^{\mathsf T}W
                 +\theta P_\perp.
\tag{8}
$$

The complementary projection annihilates constants and all columns of
$Y$. Thus (8) has zero row sums and the required pointwise closure:

$$
\widehat Q_mY=Y(-I+K)^{\mathsf T},\qquad
\widehat Q_mX=\boldsymbol1a^{\mathsf T}+X(-I+K)^{\mathsf T},
\tag{9}
$$

where $X$ has rows $x_a^{\mathsf T}$. Equation (7) makes (8)
self-adjoint in $L^2(\rho_m)$, proving detailed balance. It remains to
prove that (8) has positive off-diagonal entries, uniformly in $n$.

## 4. A positive baseline for every pair of states

For distinct complete states $a=(s,i)$ and $b=(r,j)$, divide the rate by
$\rho_m(b)>0$:

$$
\frac{\widehat q(a,b)}{\rho_m(b)}
  =(1-\theta)-\theta\ell_{ab}+h_{ab},\qquad
\ell_{ab}=y_a^{\mathsf T}R^{-1}y_b,\quad
h_{ab}=y_a^{\mathsf T}K^{\mathsf T}R^{-1}y_b.
\tag{10}
$$

Using (4) and the rank-one covariance correction gives

$$
\ell_{ab}=sr(n\delta_{ij}-1)
               +\frac{(s-m)(r-m)}{1-m^2}.
$$

The baseline $(1-\theta)-\theta\ell_{ab}$ is therefore

| Distinct states | Baseline bracket | Lower bound for $|m|\le1/2$ |
| --- | --- | --- |
| $i\ne j$, $s=r$ | $1-\theta(1-sm)/(1+sm)$ | $1/2$ |
| $i\ne j$, $s=-r$ | $1-\theta$ | $5/6$ |
| $i=j$, $s=-r$ | $1-\theta+\theta n$ | $(n+5)/6$ |

The last row supplies a margin proportional to $n$. The cosine basis
places the only extensive perturbation in precisely that row.

## 5. The bulk drift diagonalizes; boundary corrections stay bounded

Put $\widetilde K=L^{-1}KL$ and
$H=\widetilde K^{\mathsf T}D^{-1}$. This symmetric matrix is tridiagonal:

$$
\begin{aligned}
H_{00}&=\frac{t^2}{1-t^2m^2},&
H_{01}=H_{10}&=\frac{t\sqrt{1-t^2}}{1-t^2m^2},\\
H_{11}&=-\frac{t^4}{1+t^2}
          +\frac{t^2(1-t^2)m^2}{1-t^2m^2},&
H_{n-1,n-1}&=-tc,\\
H_{j,j+1}=H_{j+1,j}&=c\quad(1\le j\le n-2).
\end{aligned}
\tag{11}
$$

All unlisted entries vanish. The first-two-coordinate block and final
diagonal are disjoint even at $n=3$. The bidiagonal inverse of $L$
verifies (11) directly for arbitrary $n$.

Let $J$ be the zero-diagonal Chebyshev Jacobi matrix, with
$J_{01}=J_{10}=1/\sqrt2$ and all remaining nearest-neighbor entries
$1/2$. The cosine recurrence, including $\cos(n\phi_i)=0$, gives

$$
UJU^{\mathsf T}=\operatorname{diag}(\cos\phi_i).
$$

Consequently $H=2cJ+E$, where $E$ is supported only in the first-two
block and the final diagonal. In the whitened coordinates
$z_{(s,i)}=s\sqrt n\,u_i-me_0$, where $u_i^{\mathsf T}$ is row $i$ of
$U$, we have

$$
h_{ab}=z_a^{\mathsf T}Hz_b
 =sr\,2cn\cos\phi_i\,\delta_{ij}+\epsilon_{ab}.
\tag{12}
$$

Since $|U_{ik}|\le\sqrt{2/n}$, direct expansion bounds the remainder by

$$
|\epsilon_{ab}|\le
2\sum_{k,l}|E_{kl}|
+2|m|\sqrt2\,\|He_0\|_1+m^2|H_{00}|.
\tag{13}
$$

For $0<t\le1/4$ and $|m|\le1/2$, elementary estimates give

$$
H_{00}\le t/3,\quad H_{01}\le4t/3,\quad
|H_{11}|\le t/12,\quad tc\le t/4,\quad \sqrt2c\le3t/2.
$$

For example, $1-t^2m^2\ge63/64$ and

$$
|H_{11}|\le t^4+\frac{16}{63}t^2
\le\left(\frac1{64}+\frac4{63}\right)t<\frac t{12}.
$$

Thus, counting both off-diagonal entries of $E$,

$$
\sum_{k,l}|E_{kl}|\le\frac{19t}{3},\qquad
\|He_0\|_1\le\frac{5t}{3},\qquad
|\epsilon_{ab}|\le\left(\frac{38}{3}+\frac52+\frac1{12}\right)t
=\frac{61t}{4}<16t.
\tag{14}
$$

Every constant in (14) is independent of chain length.

## 6. Strict positivity and a finite rate bound

For different node indices, the extensive term in (12) vanishes.
Equations (10)–(14) give the rate bracket at least

$$
\frac12-16t\ge\frac14>0.
$$

For equal node indices and opposite signs, it is at least

$$
\frac{n+5}{6}-2cn-16t
\ge n\left(\frac16-2t\right)+\frac56-16t>\frac14.
$$

Hence all distinct states communicate directly, and in fact
$\widehat q(a,b)\ge1/(16n)$ throughout (1). Together with zero row sums
this proves that (8) is an irreducible CTMC generator. There are no zero
stationary masses or diverging exit rates hidden in the construction.

The nonzero eigenvalues of (8) are the $n$ physical mean eigenvalues of
$-I+K$ and $-1+\theta=-5/6$, repeated $n-1$ times. Matrix $K$ is similar
to a symmetric matrix and its maximum row sum is at most $2t$. Therefore
the spectrum of $-\widehat Q_m$ lies in $[0,1+2t]$. Each exit rate is a
diagonal Rayleigh quotient of the symmetric similarity transform, so

$$
-\widehat q(a,a)\le1+2t\le\frac{33}{32}.
\tag{15}
$$

## 7. Prediction, attribution and limits

The conditional preparation means agree by (4)–(5). The exact affine
mean equations agree pointwise at every field by (9). Solving the same
linear equations across successive dwell intervals therefore gives the
same final conditional expectation of $S$ for either initial sign.
Binary final outputs and the common balanced initial sign then give all
four entries of every endpoint-pair law. No intermediate-observation or
full-path equality is used or implied.

Symmetric moment quadrature, reversible spectral expansions and free
choices on an unobserved orthogonal complement are established tools;
see the [source audit](FAMILIAR_CHAIN_SHARPNESS_SOURCE_AUDIT.md). The
specific construction turns the chain's bulk mean drift into a diagonal
term and controls its boundary corrections uniformly in length. Its role
here is to attain the independently proved physical state lower bound.

The earlier [three-switch realization](FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md)
remains stronger at its particular coupling $t=1/3$. Neither the present
weak-coupling constant nor the field interval is claimed optimal. The
general predictor's directed rates have no demonstrated finite-affinity
device realization. State counts do not establish a heat cost, an
extensive number of saved bits, or a length-independent accuracy margin.
