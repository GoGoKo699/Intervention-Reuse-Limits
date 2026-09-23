# Full Walsh observability without a rival rate cap

[Nineteen-level target](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md) · [Target-only logarithm truncation](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md) · [Finite-state fast closure](FINITE_STATE_FAST_RATE_CLOSURE.md)

**Research theorem, 23 September 2026.** Every subset character of the nineteen-level target's lamp table is physically observable. A target-only finite-clock truncation gives an explicit positive error floor against every smaller finite Markov rival, with no rival rate, reversibility, histogram or field-rule assumption. The degree hierarchy below interpolates between the previously used single-bit rank bound and full-table observability. It is a fixed-target strengthening, not an improvement of the already established polynomial unrestricted minimax growth class.

The general ingredients are Walsh characters and rank factorization of finite controlled-word matrices. The quantitative content here is their realization by this target's physical generators, with the prescribed preparation and readout and a uniform finite-clock coefficient budget.

## 1. Statement and rival class

Fix $H,k>0$ and any sampling interval $a/k>0$. Use the nineteen-level target indexed by $n\ge1$, with $r=2^n$ lamp-table entries, hidden relaxation band $[k,3k]$, and $18r2^r+2$ physical states. Use exactly the thirty-nine fields

$$
G=\frac9{100},\qquad
h_0=\min\{H,[20(1+G)]^{-1}\},\qquad
h_i=i h_0/38\quad(0\le i\le38).
\tag{1}
$$

A competing $D$-state Markov model has one fixed initial probability vector and one fixed real readout. Its generator at a constant field is time homogeneous and depends only on that instantaneous field. Its rates may be arbitrarily large, and its dependence on field may be arbitrary. No ordinary reversibility, original kinetic rule, actuator alphabet, exact histogram, or common preparation is imposed on the rival. All rival physical states count in $D$.

Experiments use the menu (1), with every positive segment duration an integer multiple of $a/k$, and observe the mean at the complete protocol horizon. The initial mean at time zero is included. Error is the supremum absolute discrepancy over this class; the usual full bounded-protocol, all-time prediction error is at least this error.

For $1\le p\le r$, define

$$
K_{n,p}=\sum_{j=0}^p\binom rj,\qquad
m_{n,p}=9K_{n,p}+2.
\tag{2}
$$

There is a constant $C_a>0$, depending only on $H,a$, such that, for every $n,p$ and every rival with $D<m_{n,p}$,

$$
\boxed{\sup_{\rm experiments}|m_n-\widehat m|
\ge \exp[-C_a(n+1)p].}
\tag{3}
$$

The witnessing experiments have horizons $O_{H,a}((n+1)p/k)$. In particular, taking $p=r$ gives

$$
\boxed{D<9\cdot2^r+2\quad\Longrightarrow\quad
\sup|m_n-\widehat m|\ge e^{-C_a(n+1)r}.}
\tag{4}
$$

Exact agreement consequently requires at least $9\cdot2^r+2$ total states. This lower bound need not be the exact minimum for general $n$. For $n=1$, it is attained: Section 6 gives an exact thirty-eight-state original-rule reversible realization.

## 2. Signed multiplication and the full Walsh family

Rescale time so that $k=1$. Use the physical polynomials $B_j=Y_{\gamma_j}+Y_{-\gamma_j}$, $B_s=Y_{\gamma_0}-Y_{-\gamma_0}$, the port selectors $D_j=-B_j$, and the cross-port transports $T_{cd}=16D_cK_bD_d$ from the target construction. On functions vanishing at the visible state, $D_s=-B_s$ multiplies by the signed central actuator bit

$$
s(x,a,\sigma)=\sigma x_a
$$

on the central port and is zero elsewhere. No full-space diagonal or projector identity is assumed.

For every address $b$, the translation word $W_b$ uses at most $9n$ cross-port edges and acts on central functions by replacing $a$ with $a\oplus b$. Write $W_b^*$ for its reversed-edge word; on the target's hidden port spaces this is its conditional stationary adjoint and inverse. Define

$$
M_b=W_bD_sW_b^*.
\tag{5}
$$

On central hidden functions this is multiplication by $f_b(x,a,\sigma)=\sigma x_{a\oplus b}$, and it is zero on other hidden ports. For a subset $S$ of addresses, fix an order and put

$$
A_S=\prod_{b\in S}M_b,\qquad A_\varnothing=I.
$$

Let $A_S^{\leftarrow}$ reverse this order. This denotes a specified physical polynomial with the correct target hidden adjoint action; it is not a claim that formal reversal of the physical generators is their full-space $\pi_0$ adjoint.

The resulting central features are

$$
\chi_S(x,a,\sigma)=\prod_{b\in S}f_b(x,a,\sigma)
=\sigma^{|S|}\prod_{b\in S}x_{a\oplus b}.
\tag{6}
$$

For fixed $a,\sigma$, the coordinates $x_{a\oplus b}$ are independent fair signs. Thus, under the conditional central stationary law,

$$
\mathbb E_0\chi_S\chi_T=\mathbf1_{S=T},\qquad
\mathbb E_0\chi_S=\mathbf1_{S=\varnothing}.
\tag{7}
$$

The factor $\sigma^{|S|}$ creates no relation between the even and odd characters. In particular all $2^r$ subsets give distinct orthonormal features. This does not assert that the sign and address coordinates themselves are separately observable.

## 3. Physical left and right words give an identity matrix

The target's nine ports are identical copies of the table, address and sign coordinates. Every auxiliary port has a direct identity-matching edge to the central port. Put

$$
U_j=T_{0j},\quad V_j=T_{j0}\quad(j\ne0),\qquad
U_0=V_0=D_0.
\tag{8}
$$

On target hidden functions, $V_j$ carries a central feature to its identical copy at port $j$, and $U_j$ reverses that transport. Each $U_j$ annihilates the full constant vector. Write $\nu_j$ for conditional stationary probability on port $j$; its unconditional mass under $\pi_0$ is $1/36$.

Let $Y_{\rm sum}=\sum_\gamma Y_\gamma$, including the zero-sensitivity level, and define visible-state sides

$$
\mathcal L_A=I+Y_{\rm sum},\qquad
\mathcal R_A=-I-\tfrac12Y_{\rm sum}.
\tag{9}
$$

The original preparation and readout satisfy

$$
\pi_0\mathcal L_A=e_A^T,\qquad \mathcal R_AS=e_A.
$$

For each port $j$ and subset $S$, define

$$
\begin{aligned}
\mathcal L_{j,S}
&=-36B_0A_S^{\leftarrow}U_j
  +\mathbf1_{S=\varnothing}\mathcal L_A,\\
\mathcal R_{j,S}&=-\tfrac12V_jA_SB_0.
\end{aligned}
\tag{10}
$$

The right side produces the port-supported feature:
$\mathcal R_{j,S}S=1_j\chi_S$.
To verify the left side without overlooking its visible component, the hidden entries of $\pi_0B_0A_S^{\leftarrow}U_j$ are exactly $-\nu_j\chi_S/36$. This polynomial annihilates the full constant vector, so its visible entry is $\mathbb E_j\chi_S/36=\mathbf1_{S=\varnothing}/36$. The correction in (10) cancels that entry. Consequently

$$
\pi_0\mathcal L_{j,S}=\nu_j\chi_S
$$

as a row supported on port $j$.

The target's only zero-sensitivity hidden state is its hub $o$, with $\pi_0(o)=1/4$. Its sides

$$
\mathcal L_o=-4Y_0+\mathcal L_A,\qquad
\mathcal R_o=-\tfrac12Y_0
\tag{11}
$$

satisfy $\pi_0\mathcal L_o=e_o^T$ and $\mathcal R_oS=e_o$.

For any family $\mathcal F$ of distinct address subsets, take indices $A,o$ and $(j,S)$ with $0\le j\le8$, $S\in\mathcal F$. Equations (7)–(11) give the exact physical word matrix

$$
\boxed{\mathsf H_{uv}=\pi_0\mathcal L_u\mathcal R_vS
=\mathbf1_{u=v},\qquad
\mathsf H=I_{9|\mathcal F|+2}.}
\tag{12}
$$

All left and right sides are polynomials in the original physical generators, evaluated with the single prescribed preparation and readout. There is no extra preparation, physical adjoint experiment, or rival coordinate identification.

## 4. Degree and coefficient accounting

Let $V_H\ge1$ be the maximum row $\ell^1$ norm of the inverse exponential Vandermonde matrix for fields (1), enlarged to one, and set $P_H=64V_H^3$. Thus $K_b$ and each $Y_\gamma$ have physical-generator coefficient mass at most $V_H$, each $B_j,D_j,D_s$ has mass at most $2V_H$, and each $T_{cd}$ has mass at most $P_H$ and degree three.

Equation (5) therefore has

$$
\deg M_b\le54n+1,\qquad
\|M_b\|_{{\rm coeff},1}\le P_H^{18n+1}.
\tag{13}
$$

Suppose every $S\in\mathcal F$ has size at most $p\ge1$, and put $N=(n+1)p$. Each side in (9)–(11) satisfies

$$
\deg\mathcal L_u,\ \deg\mathcal R_u
\le(54n+1)p+4\le54N,
$$

$$
\|\mathcal L_u\|_{{\rm coeff},1},\
\|\mathcal R_u\|_{{\rm coeff},1}
\le P_H^{(18n+1)p+3}\le P_H^{18N}.
\tag{14}
$$

For the nontrivial left side, the first term of (10) has mass at most $36P_H^{(18n+1)p+2}$ and the correction at most $P_H$. Since $P_H\ge64$, their sum is bounded as in (14). The other sides are smaller. Constants in (13)–(14) depend only on the fixed field menu, never on rival rates or state count.

## 5. Target-only truncation and the finite-error rank bound

Set $R_0=e^{(1+G)h_0}$, $B_0^{\rm sp}=2(3+R_0)$, and $\kappa=e^{h_0}$. All target full generators have real spectra in $[-B_0^{\rm sp},0]$. For the fixed clock $a$, define

$$
q_a=1-e^{-aB_0^{\rm sp}},\qquad
\varrho_a=\frac{1+1/q_a}{2}>1,\qquad
K_a=\frac\kappa a\log\frac1{1-\varrho_aq_a},
$$

$$
A_a=P_H^{18}\max\{1,(\log2)/a\}^{54},\qquad
B_a=P_H^{18}\max\{1,K_a\}^{54}.
\tag{15}
$$

The target-only total-degree logarithm lemma in [the fixed-clock rank proof](POLYNOMIAL_CONTROLLED_LOWER_BOUND.md#3-a-general-lemma-for-total-degree-truncation) applies separately to each complete side. Truncation at total logarithm degree $M$ gives target operator error at most $B_a^N\varrho_a^{-(M+1)}$, original side norm at most $B_a^N$, and propagator coefficient mass at most

$$
J=4^M A_a^N.
\tag{16}
$$

No rival is expanded into logarithms. With $m=9|\mathcal F|+2$, choose

$$
M=\left\lceil\frac{\log(6mB_a^{2N})}{\log\varrho_a}\right\rceil.
\tag{17}
$$

Separate side truncation preserves row-times-column factorization. On the target, the resulting matrix $\mathsf H^{[M]}$ obeys

$$
\|\mathsf H^{[M]}-I_m\|
\le3mB_a^{2N}\varrho_a^{-(M+1)}\le\frac12,
\qquad \sigma_{\min}(\mathsf H^{[M]})\ge\frac12.
\tag{18}
$$

Each entry is a signed combination of actual mean experiments with total absolute coefficient mass at most $J^2$ and at most $2M$ propagator letters. Its horizon is at most $2Ma/k$.

On any $D$-state rival, evaluation of these same finite propagator polynomials factors through its $D$ state coordinates. Its matrix therefore has rank at most $D$. If $D<m$, (18) and the entrywise experimental discrepancy bound imply

$$
\boxed{\delta\ge\frac1{2mJ^2}
=\frac1{2m16^M A_a^{2N}}.}
\tag{19}
$$

This argument uses no rival spectral, rate, positivity-repair, or kinetic interpolation claim. Only the actual propagators at the specified fields and fixed durations are substituted on the rival.

For the degree-$p$ family, $|\mathcal F|=K_{n,p}\le(r+1)^p$: encode a subset in a sorted $p$-tuple padded with a dummy symbol. Hence $m\le11(r+1)^p$ and $\log m=O(N)$. One explicit uniform choice is

$$
c_M=1+\frac{\log132+2\log B_a}{\log\varrho_a},\qquad
C_a=\log44+c_M\log16+2\log A_a.
\tag{20}
$$

Then $M\le c_MN$, and (19) is at least $e^{-C_aN}$. This proves (3)–(4), with the claimed horizon. The same constants work for every subfamily of degree at most $p$.

## 6. Partial cubes, state budgets, and an exact small target

Choose any $q\le r$ addresses and use all their subsets. Then $|\mathcal F|=2^q$ and (19) yields

$$
D<9\cdot2^q+2\quad\Longrightarrow\quad
\sup|m_n-\widehat m|\ge e^{-C_a(n+1)q}.
\tag{21}
$$

For any fixed target and any integer total-state budget $1\le D<9\cdot2^r+2$, let $q_D$ be the smallest integer $q\ge1$ for which $9\cdot2^q+2>D$. Then $q_D\le r$ and $q_D\le1+\log_2D$, so

$$
\inf_{\widehat F:\,|\widehat F|\le D}\sup|m_n-\widehat m|
\ge e^{-C_a(n+1)q_D}
\ge e^{-C_a(n+1)(1+\log_2D)}.
\tag{22}
$$

The degree hierarchy is stronger when the least $p$ with $m_{n,p}>D$ is smaller than $q_D$: use that $p$ in (3). These are explicit positive distances for fixed targets; compactness of a rival family is unnecessary. They also apply to its uniform-response closure, since a fixed error lower bound persists under uniform limits.

For $n=1$, $r=2$ and the full rank in (12) is $38$. There is an exact quotient attaining it. At each port replace $(x,a,\sigma)$ by

$$
z=(z_0,z_1)=(\sigma x_a,\sigma x_{a\oplus1})\in\{-1,+1\}^2.
$$

The address-coordinate reflections $J,V$ are identities for $n=1$. The gate $X$ swaps $z_0,z_1$, and $F$ flips $z_0$. Identity port spokes and all gate edges therefore descend to the four $z$ values at each of nine ports. The hub refresh is uniform on those values, and each port-$z$ state has hidden stationary mass $1/72$. The sensitivity is the well-defined scalar $\gamma_jz_0$. Keep the hub and visible state separately.

Every field generator is strongly lumpable under this map: destinations of gate edges depend only on the quotient state, hub rates aggregate by stationary mass, and external rates retain the original field rule because sensitivity is constant on each fiber. The pushed-forward preparation and readout consequently reproduce all controlled means exactly. Detailed balance and the exact nineteen-level histogram are preserved. The quotient has $9\cdot4+2=38$ total states. Together with (12), this proves the exact minimum of thirty-eight within the broader rival class stated in Section 1.

## 7. Interpretation and limits

At full degree, the required precision is $e^{-O_a(n2^n)}$, whereas the rank threshold is $e^{\Theta(2^n)}$. This fixed-target statement does not give the capped reversible theorem's $\exp(c\delta^{-\alpha})$ minimax lower bound without a rate assumption. At degree one it recovers a polynomial unrestricted family lower, already known from the shorter single-bit witness. The contribution is the explicit hierarchy up to all table characters, including positive error floors against unbounded-rate rivals and their uniform-response limits.

The nine-port factor and two additional coordinates are target-specific normalizations, not a state-label restriction on rivals. No larger exact observable dimension is established for general $n$. The bound controls deterministic mean error and maximum witnessing horizon; it supplies no statistical sample complexity, experiment-count economy, parameter-precision bound, or computation-time bound.

The proof is analytic. Small exact checks may verify Walsh orthogonality, the visible-endpoint cancellation and the $n=1$ quotient. They cannot prove its all-width and arbitrary-rival quantifiers by finite enumeration.
