# Randomized Bayes aggregation still has exponential state cost

[Repository overview](../../README.md) · [Partition aggregation lower bound](../../docs/AGGREGATION_STATE_LOWER_BOUND.md) · [Observable aggregation rigidity](OBSERVABLE_AGGREGATION_RIGIDITY.md) · [New-state reversible upper bound](../../docs/REGISTER_SCENERY_COMPRESSION.md)

**Recovered research note, 22 September 2026.** Randomizing the encoder does not remove the exponential state requirement for stationary Bayes aggregation. On the fixed six-level target family below, every sufficiently accurate color-preserving stochastic encoder, followed by the Bayes reverse channel and the specified uniformized dynamics, needs exponentially many retained labels in a positive power of inverse prediction error. Fresh reversible models for the same targets have polynomial state cost.

The theorem concerns actual controlled means. It applies on every fixed positive control clock. Its competitor architecture is precisely $BPA$, with a fixed uniformization rate; it does not cover arbitrary fitted reversible dynamics on the encoder labels.

This text reconstructs the argument from the preserved research state and the published target construction. It is not a claim that the inaccessible working file was recovered byte for byte, or that numerical verifiers have been rerun.

## 1. The six-level target family

Fix $H,k>0$. For $n\ge1$, let $r=2^n$. An address $b$ is a binary register indexed by $\mathbb Z_n$. A configuration is a complete table
$$
x=(x_b)_b\in\{-1,+1\}^{r}.
$$
The hidden states are
$$
z=(x,b,j,\sigma),\qquad j\in\{1,2,3\},\quad \sigma\in\{-1,+1\},
$$
with uniform law $\mu$. Including the visible state $A_{\mathrm{vis}}$, the target has
$$
1+6r2^r
$$
states. Every coordinate in this expression is counted.

Let $J:i\mapsto-i-1$ and $V:i\mapsto-i$ reflect register coordinates, and let $X$ flip address bit zero. These are involutions; the two reflections generate cyclic rotation. Put
$$
U_1=J,\qquad U_2=V,\qquad U_3=X,\qquad \lambda=\frac18.
$$
Define
$$
\begin{aligned}
(Lf)(x,b,j,\sigma)
={}&k\lambda\bigl[f(x,U_jb,j,\sigma)-f(x,b,j,\sigma)\bigr]\\
&+k\lambda\sum_{d\ne j}
\bigl[f(x,b,d,\sigma)-f(x,b,j,\sigma)\bigr],
\end{aligned}
$$
and
$$
K=L+\frac{3k}{2}(\Pi_\mu-I).
$$
The matching contribution has relaxation cap $k/4$, and the three-port contribution has cap $3k/8$. Consequently the nonzero relaxation rates of $K$ lie in
$$
[3k/2,17k/8]\subset[3k/2,5k/2].
$$
The refresh makes all hidden off-diagonal rates positive.

Set
$$
g(x,b,j,\sigma)=\gamma_j\sigma x_b,\qquad
(\gamma_1,\gamma_2,\gamma_3)=\frac1{10}(1,2,3).
$$
Each of the six actuator values has mass $1/6$. Thus
$$
G=\frac3{10},\qquad \mu g=0,\qquad \mu g^2=\frac7{150}.
$$

Attach $A_{\mathrm{vis}}$ through the original field rule
$$
q_{A_{\mathrm{vis}}z}(h)=k\mu_z e^{(1+g_z)h},
\qquad
q_{zA_{\mathrm{vis}}}(h)=k e^{(g_z-1)h}.
$$
Preparation and readout are
$$
\pi_0=(1/2,\mu/2),\qquad
S(A_{\mathrm{vis}})=-1,\quad S(z)=+1.
$$
The full process is ordinarily reversible at every field, with
$$
\pi_h(A_{\mathrm{vis}})=\frac{e^{-h}}{2\cosh h},
\qquad
\pi_h(z)=\frac{\mu_z e^h}{2\cosh h}.
$$
At zero field its visible path law is exactly the rate-$k$ two-state telegraph law.

## 2. The permitted stochastic aggregation

Let $A=(A_{zc})$ be a row-stochastic encoder from hidden target states to finitely many retained labels $c$. Remove labels of zero stationary mass. Require exact color preservation: each retained label has a value $\widehat g_c$, and
$$
A_{zc}>0\quad\Longrightarrow\quad g_z=\widehat g_c.
$$
The encoder can overlap arbitrarily within each color. It need not preserve addresses, ports beyond their encoded actuator magnitudes, configurations, or signs separately.

Define
$$
\widehat\mu_c=\sum_z\mu_zA_{zc},
\qquad
B_{cz}=\frac{\mu_zA_{zc}}{\widehat\mu_c}.
$$
Thus $B$ is the Bayes reverse channel. On the weighted function spaces,
$$
B=A^*.
$$

Fix the uniformization rate
$$
\nu=\frac{5k}{2},
\qquad
P=I+\frac K\nu.
$$
The permitted retained dynamics are
$$
\widehat P=BPA,
\qquad
\widehat K=\nu(BPA-I).
\tag{1}
$$
Attach the visible state using the original field rule with
$\widehat\mu,\widehat g$, and retain the prescribed preparation and readout.

The uniformization convention is part of the architecture. In particular,
$$
\widehat K=BKA+\nu(BA-I),
\tag{2}
$$
which generally differs from $BKA$. The extra term vanishes for deterministic partitions but is essential for genuinely randomized encoders.

The matrix $\widehat P$ is stochastic and $\widehat\mu$-reversible:
$$
\widehat\mu_c\widehat P_{cd}
=
\sum_{z,z'}\mu_zA_{zc}P_{zz'}A_{z'd},
$$
which is symmetric in $c,d$.

Moreover, $P$ is positive semidefinite and, on mean-zero functions,
$$
0\preceq P\preceq \frac25 I.
$$
For a mean-zero retained function $v$, $Av$ is mean zero and
$$
0\le
\langle v,BPAv\rangle_{\widehat\mu}
=
\langle Av,PAv\rangle_\mu
\le\frac25\|Av\|_\mu^2
\le\frac25\|v\|_{\widehat\mu}^2.
$$
Hence every nonconstant relaxation rate of $\widehat K$ lies in
$$
[3k/2,5k/2].
\tag{3}
$$
The exact six-level histogram is preserved by color preservation.

## 3. An exact reversible joint lift

The useful representation of (1) is an ordinary partition aggregation of a larger reversible target.

Let
$$
\widetilde\Omega=\{(z,c):A_{zc}>0\},
\qquad
\widetilde\mu_{zc}=\mu_zA_{zc}.
$$
Define the isometry
$$
(Jf)(z,c)=f(z).
$$
Its adjoint is
$$
(J^*u)(z)=\sum_cA_{zc}u(z,c).
$$
Set
$$
\widetilde P=JPJ^*,
\qquad
\widetilde K=\nu(\widetilde P-I).
\tag{4}
$$
Equivalently,
$$
\widetilde P_{(z,c),(z',c')}=P_{zz'}A_{z'c'}.
$$
This is a stochastic reversible kernel for $\widetilde\mu$.

On $\operatorname{ran}J$, the lifted generator is the original generator:
$$
\widetilde KJ=JK.
\tag{5}
$$
On $(\operatorname{ran}J)^\perp$, it equals $-\nu I$. Thus the lift retains the advertised band $[3k/2,5k/2]$; the additional modes have relaxation rate exactly $5k/2$.

Give $(z,c)$ actuator value $g_z$, attach the same visible state by the original field rule, and use
$$
\widetilde\pi_0=(1/2,\widetilde\mu/2).
$$
Extend $J$ to the full physical space by fixing the visible coordinate. For every field,
$$
\widetilde Q(h)J=JQ(h).
\tag{6}
$$
Preparation and readout also intertwine. Therefore the lifted target has exactly the original target's controlled means for every permitted protocol.

Partition the lifted hidden states by $c$, keeping the visible state separate. Let $E$ be conditional expectation onto these cells. The stationary-flux compression of (4) is precisely $BPA$. Color preservation also gives
$$
\widehat Q(h)=E\widetilde Q(h)E
$$
on the cell-constant space.

The lift is a proof device. The quantity being lower-bounded is the number of retained labels of the original encoder, plus its visible state. No lifted coordinate is supplied to that competitor.

## 4. Observable query features

Set $k=1$ until the final statement. For each sensitivity $\gamma$, define $X_\gamma$ by its only nonzero row:
$$
(X_\gamma)_{A_{\mathrm{vis}},z}
=\mu_z\mathbf1_{g_z=\gamma},
\qquad
(X_\gamma)_{A_{\mathrm{vis}},A_{\mathrm{vis}}}
=-\mu(g=\gamma).
$$
Let $Y_\gamma$ have entries $1$ in column $A_{\mathrm{vis}}$ and $-1$ on the diagonal at hidden rows of sensitivity $\gamma$. Write $K_b$ for $K$ embedded in the full space with zero visible row and column. Then
$$
Q(h)=K_b+\sum_\gamma e^{(1+\gamma)h}X_\gamma
+\sum_\gamma e^{(\gamma-1)h}Y_\gamma.
\tag{7}
$$

The thirteen frequencies $0,\gamma+1,\gamma-1$ are distinct. Choose
$$
\bar h=\min\{H,1/[20(1+G)]\},
\qquad h_i=i\bar h/12,\quad 0\le i\le12.
$$
The interpolation matrix is a Vandermonde matrix in the distinct positive numbers
$e^{\omega\bar h/12}$. Therefore $K_b,X_\gamma,Y_\gamma$ are fixed linear combinations of these thirteen physical generators.

Writing $X=\sum_\gamma X_\gamma$ and $Y=\sum_\gamma Y_\gamma$, the full operator
$$
YX+Y
$$
has hidden block $\Pi_\mu-I$ and zero visible row and column. Consequently
$$
L_b=K_b-\frac32(YX+Y).
\tag{8}
$$

On functions vanishing at the visible state, let
$$
D_j=-Y_{\gamma_j}-Y_{-\gamma_j}.
$$
This is the port-$j$ projector. Define
$$
T_{cd}=\lambda^{-1}D_cL_bD_d\quad(c\ne d),
\qquad
T_{jj}=\lambda^{-1}D_jL_bD_j+3D_j.
\tag{9}
$$
On the specified input ports these operators respectively transport between ports and apply the involution $U_j$. They are generator polynomials of degree at most four and uniformly bounded coefficient mass.

A pure address translation $b\mapsto b\oplus a$ can be implemented using $n$ rotations and at most $n$ first-bit flips. Each rotation uses two reflections. Allowing transport to and from the appropriate port, there is a word $W_a$ of at most $9n$ operators (9), beginning and ending at port one, which gives this pullback action.

Put
$$
e=\mathbf1_{\{A_{\mathrm{vis}}\}},
\qquad
Y_d=Y_{\gamma_1}-Y_{-\gamma_1},
\qquad
f_a=W_aY_de.
$$
Then, exactly,
$$
f_a(x,b,j,\sigma)
=\mathbf1_{j=1}\sigma x_{b\oplus a}.
\tag{10}
$$
In particular, each $f_a=p_a(Q)e$, where $p_a$ has degree at most
$$
36n+1
$$
and coefficient mass at most $C_q^{\,n+1}$, for a constant $C_q$ independent of $n$ and the encoder.

The physical intertwining (6) implies
$$
Jf_a=p_a(\widetilde Q)\widetilde e.
\tag{11}
$$
There is no claim that the lifted versions of the transport operators remain partial isometries away from $\operatorname{ran}J$. The argument below uses observable aggregation rigidity instead.

## 5. Mean accuracy forces reconstruction

Fix any control clock $a>0$. Suppose the stochastic aggregate has actual-mean error at most $\delta$, uniformly over all observation times and protocols whose segment lengths are integer multiples of $a$, using the thirteen extraction fields and the additional calibration field $H$.

By (6), the same error holds between the lifted target and its partition aggregate. They satisfy the hypotheses of [observable aggregation rigidity](OBSERVABLE_AGGREGATION_RIGIDITY.md). That theorem gives constants $C_0,F,\kappa>0$, depending only on the fixed physical parameters and clock, such that
$$
\|(I-E)\widetilde Q(h_L)\cdots\widetilde Q(h_1)\widetilde e\|
\le C_0F^L\delta^\kappa.
$$
Applying this bound term by term to (11), and absorbing the fixed extraction coefficients, gives constants $C,B\ge1$ such that
$$
\boxed{\;
\|(I-E)Jf_a\|_{\widetilde\pi_0}
\le CB^{n+1}\delta^\kappa
\quad\text{for every address }a.
\;}
\tag{12}
$$

The same constants work for every target width, every number of retained labels, and every color-preserving encoder. This uniformity is what allows a state-complexity conclusion.

Set
$$
\delta_n=
\left(
\frac{1}{96rC^2B^{2n+2}}
\right)^{1/(2\kappa)}.
\tag{13}
$$
At accuracy $\delta\le\delta_n$, each squared reconstruction loss in (12) is at most $1/(96r)$.

## 6. The independent table forces exponentially many labels

In the lifted stationary probability space, consider the event
$$
\mathcal R=\{\text{address }0,\ \text{port }1\},
$$
including both signs and every encoder label. Its mass is
$$
w=\widetilde\pi_0(\mathcal R)=\frac1{6r}.
$$
Conditioned on $\mathcal R$ and $\sigma$, the table $x$ remains a uniform independent $r$-bit vector. The random label $C$ is sampled through the encoder and can depend arbitrarily on that table.

The cell-constant function $EJf_a$ is a function $\phi_a(C)$. By (10), on $\mathcal R$,
$$
Jf_a=\sigma x_a.
$$
Summing (12) at the accuracy (13), restricting the nonnegative losses to $\mathcal R$, and dividing by $w$, gives
$$
\mathbb E\!\left[
\sum_a (x_a-\sigma\phi_a(C))^2
\,\middle|\,\mathcal R
\right]
\le \frac r{16}.
\tag{14}
$$
The event $\mathcal R$ need not be measurable from the retained label.

Thresholding $\sigma\phi_a(C)$ at zero gives a bit estimator from $(C,\sigma)$. Every sign error costs at least one in squared loss, so its average bit error is at most $1/16$. The binary entropy bound and concavity imply
$$
H(x\mid C,\sigma,\mathcal R)
\le r h_2(1/16)<\frac{3r}{8}.
$$
Since $H(x\mid\sigma,\mathcal R)=r$,
$$
\log_2|\mathcal C|
\ge I(x;C\mid\sigma,\mathcal R)
>\frac{5r}{8}.
$$
Thus the total retained physical count satisfies
$$
\boxed{\quad D\ge 2^{5r/8}=2^{5\cdot2^n/8}.\quad}
\tag{15}
$$

Randomization changes the conditional law of $C$, but not this information bound. No deterministic encoder, disjoint support, equal cell size, or address-measurability assumption has entered the proof.

## 7. Consequences and scope

Equation (13) has $\log(1/\delta_n)=O(n+1)$. More explicitly, choose $C_*>0$ with
$$
\delta_n\ge e^{-C_*(n+1)}
$$
for all $n$. For sufficiently small $\delta$, take
$$
n=\left\lfloor\frac{\log(1/\delta)}{C_*}\right\rfloor-1.
$$
Then $\delta\le\delta_n$ and $2^n\ge c'\delta^{-\alpha}$, where
$\alpha=\log2/C_*>0$. Therefore
$$
D_{\mathrm{soft}}(\delta)\ge
\exp(c\delta^{-\alpha}).
\tag{16}
$$

Deterministic partitions are special cases of the present architecture. The reversible prediction-partition upper bound consequently gives
$$
D_{\mathrm{soft}}(\delta)
\le
\exp\!\left(C'\delta^{-p_6}\log\frac2\delta\right),
\qquad
p_6=\frac{\log6}{\beta},
\quad
\beta=\log\!\left(1+\frac{2}{5e^{(1+G)H}}\right).
$$
The existing register-scenery construction gives fresh reversible models with
$$
D_{\mathrm{fresh}}(\delta)
\le C''\delta^{-p},
\qquad p=\frac{\log96}{\beta},
$$
uniformly over the same family. These preserve the original field rule, exact histogram, and advertised spectral band. The existing target-only Gram argument also gives a polynomial lower bound against arbitrary Markov rivals.

Thus stochastic Bayes aggregation has exponential growth in a power of inverse error, while fresh reversible realization has polynomial growth, with unmatched exponents.

Restoring $k$, the lower bound holds for every fixed clock $a/k$. This proof uses equilibrium calibration and accuracy over all horizons; it does not assert a logarithmic witnessing horizon. The alphabet has six fixed values. The result is an architecture separation and does not itself establish a penalty for reversibility.
