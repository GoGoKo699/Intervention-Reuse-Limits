# Reversible generator-word observability at a fixed clock

[Checkpoint](README.md) · [Dynamic-lamp application](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md)

This archival note recovers the direct finite-horizon proposition used in the main separation. The earlier workspace also contained a broader preparation-calibrated theorem for return and adjoint words; its source is listed for recovery in the checkpoint work record. That broader theorem is not needed here.

## 1. Two physical models

Consider two models with the original field rule

$$
q_{Az}(h)=k\mu_z e^{(1+g_z)h},\qquad
q_{zA}(h)=k e^{(g_z-1)h},
$$

stationary hidden generator $K$ satisfying ordinary detailed balance, preparation
$\pi_0=(1/2,\mu/2)$, and readout $S(A)=-1$, $S(z)=1$.
The models may have different state spaces and stationary laws.
Assume $|g|\le G$ and that each model has hidden relaxation cap $\Lambda k$.
Alternatively, assume directly a common hidden outgoing-rate budget $\Gamma k$ and replace $\Lambda$ below by $\Gamma$.

Set dimensionless time by $k=1$. Fix a positive clock $a$ and a finite field menu inside $[-h_0,h_0]$. Suppose actual means agree to error at most $\delta$ on all menu protocols with positive segment lengths in $a\mathbb N$, up to the horizon specified below.

For each menu field the reversible stationary law is

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h}.
$$

The ratio between its largest and smallest density relative to $\pi_0$ is $e^{2|h|}$. Transferring an operator norm from $L^2(\pi_h)$ to $L^2(\pi_0)$ therefore costs at most $\kappa=e^{h_0}$.

## 2. Constants and estimate

Put

$$
R=e^{(1+G)h_0},\quad B_{\rm sp}=2(\Lambda+R),\quad
q=1-e^{-aB_{\rm sp}},\quad \rho=(1+q)/2,\quad t=q/\rho,
$$

and

$$
Z=\frac{\kappa}{a}\log\frac1{1-\rho},\qquad
D=8/\rho,\qquad
\theta=\frac{\log(1/t)}{\log(D/t)}>0.
\tag{1}
$$

A cap bounds each internal exit rate by $\Lambda$ through the reversible Rayleigh quotient of a state indicator. Full outgoing rates are then at most $\Lambda+R$, so Gershgorin and reversibility place every full spectrum inside $[-B_{\rm sp},0]$.

Let $p$ be any noncommutative polynomial in the finitely many dimensionless physical generators. Let $d$ be its maximum degree, and $J$ the sum of absolute coefficients in a specified word expansion. Then

$$
\boxed{
|\pi_0p(Q)S-\bar\pi_0p(\bar Q)\bar S|
\le4J\max\{1,Z\}^{d}\delta^\theta.}
\tag{2}
$$

Only mean experiments up to

$$
aM,\qquad
M=\left\lfloor\frac{\log(1/\delta)}{\log(D/t)}\right\rfloor
\tag{3}
$$

are used. This is $O_a(\log(1/\delta))$ dimensionless time.

## 3. Proof

For $E_h=e^{aQ_h}$ and $U_h=I-E_h$, the reversible spectral theorem and equilibrium norm comparison imply

$$
\|U_h^j\|_{\pi_0}\le\kappa q^j.
$$

Since $q<1$, the operator logarithm converges and

$$
Q_h=-\frac1a\sum_{j\ge1}\frac{U_h^j}{j}.
\tag{4}
$$

For a word of $d$ generators, multiply these series and group by total $U$-degree. The absolute coefficient generating function, including one factor $\kappa$ for each logarithm block, evaluated at $\rho$ is $Z^d$.
If $a_j$ denotes these weighted coefficients, then

$$
\sum_{j>M}a_jq^j
\le(q/\rho)^{M+1}\sum_ja_j\rho^j
=Z^dt^{M+1}.
\tag{5}
$$

This bounds the operator tail in each model. Charging $\kappa$ once per block rather than once per power is essential: each block is a single $U_h^j$ controlled by the spectral estimate.

Every retained monomial of total degree $j$ in the $U$ matrices expands into legal propagator words with absolute coefficient sum at most $2^j$. Thus its scalar discrepancy is at most $2^j\delta$. Bounding each coefficient group by the generating function gives retained error at most

$$
Z^d\delta\sum_{j=0}^M(2/\rho)^j
\le 2Z^dD^M\delta.
\tag{6}
$$

In either model the scalar tail is no larger than its operator tail, because the constant vector and the binary readout have unit $L^2(\pi_0)$ norm. Equations (5)--(6) and the cutoff (3) give
$4Z^d\delta^\theta$ for one homogeneous word. Indeed,
$D^M\delta\le\delta^\theta$ and
$t^{M+1}\le\delta^\theta$.
Summing the word expansion proves (2), including words of degree below $d$ by replacing $Z^d$ with $\max(1,Z)^d$.
The empty-word scalar is zero in both original preparations.

Each retained experiment contains at most $M$ propagator factors $e^{aQ_h}$. Identity factors are deleted; adjacent equal fields may be merged. Hence all segment lengths are integer multiples of $a$ and all horizons obey (3). No limiting preparation or experimental adjoint is needed.

Restoring units multiplies the witnessing horizon by $1/k$.

## 4. Scope

Both-model caps enter this scalar transfer. It cannot be applied to an unbounded-rate rival without another argument. The separate rank lower in the main note expands only the target, then evaluates finite propagator expressions exactly on every rival, which is why that other lower permits unbounded rates.

The proposition concerns observable scalars $\pi_0p(Q)S$ only. It does not identify generators or arbitrary feature vectors between two different state spaces. In the main proof the required row and lamp moments already have exactly this observable form.
