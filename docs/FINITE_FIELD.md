# Finite-field prediction with an exactly two-state passive law

[Repository overview](../README.md) · [Core model](THEORY.md) · [Cubic minimax theorem](UNRESTRICTED_RATE_LOWER_BOUND.md)

**Working theorem, 22 September 2026.** The results here concern the actual mean at a nonzero field, not a Taylor coefficient. They give matching worst-case state-growth orders for a specified subclass of the reversible model. The upper bound serves every bounded protocol and every observation horizon. The lower bound allows arbitrary finite-state Markov competitors and uses only a constant-field step. No derivative bound on a competitor is assumed. The arguments are internal derivations, not a claim of independently certified originality.

## 1. The finite-field task

Fix $k>0$, $W>0$, and a field bound $H>0$, and put $s=\sqrt W$. In the [original rate rule](THEORY.md#1-model-and-comparison-class), restrict the targets to

$$
\mu_0=\frac12,\qquad g_0=s,\qquad g_i=-s\quad(i\ne0).
$$

Thus exactly one hidden state has positive kinetic sensitivity. The other hidden states have negative sensitivity, with total stationary mass $1/2$. The internal generator $K$ is irreducible and reversible under $\mu$, with otherwise unrestricted finite size, topology, and rates. Denote this class by $\mathcal J(k,W)$. Its members retain the exact two-state passive path law, equilibrium mean $\tanh h$, reference linear mean response, and zero quadratic mean response. The sensitivity bound is $|g_i|=s$.

Every finite positive kernel of mass $W$ has a realization in this subclass, with $r+2$ total states for $r$ active rates, by the [Jacobi construction](THEORY.md#9-minimal-reversible-realization-of-a-positive-kernel). The subclass restriction therefore does not restrict the allowed finite positive kernels. It does restrict how the field acts on a realization: a general bounded $g$ with the same kernel need not have the same finite-field behavior.

Write $m_F[h](t)$ for the exact mean, starting from zero-field equilibrium. For two models define

$$
\mathcal D_H(F,\widehat F)=
\sup_{T>0}\ \sup_{\substack{h:[0,T]\to[-H,H]\\h\ \mathrm{piecewise\ continuous}}}
\ \sup_{0\le t\le T}|m_F[h](t)-m_{\widehat F}[h](t)|.
$$

One surrogate must work for all these protocols and horizons. The constructor is supplied the exact kernel; this is compression, not inference from passive or noisy observations.

Let $\mathcal M_D(H)$ contain all Markov models with at most $D$ states, a fixed real state readout, a fixed initial probability law, and rates depending on the instantaneous field, defined on $[-H,H]$. Require that bounded piecewise-continuous protocols define a Markov evolution. A constant field must give a time-homogeneous generator. No reversibility, analyticity, rate-derivative bound, passive-law agreement, or lower-order-response agreement is required. Binary readouts and stationary preparations are allowed but not imposed. Explicit time dependence or an additional external memory is outside this class.

Define

$$
E_D^{\mathrm{field}}(k,W,H)=
\sup_{F\in\mathcal J(k,W)}\ \inf_{\widehat F\in\mathcal M_D(H)}
\mathcal D_H(F,\widehat F).
$$

The constructive surrogates below belong to $\mathcal J(k,W)$ itself. Thus requiring all of the target's reversibility, sensitivity, passive-law, and low-order-response properties does not increase the worst-case asymptotic state order.

**Theorem.** For every fixed $k,W,H>0$,

$$
D_*^{\mathrm{field}}(\delta)
:=\min\{D\ge2:E_D^{\mathrm{field}}\le\delta\}
=\Theta\!\left([\log(1/\delta)]^2\right)
\quad(\delta\downarrow0).
$$

If targets are further restricted to active internal rates $\lambda_j\le3k$, the corresponding order is $\Theta(\log(1/\delta))$. Constants may depend on $W,H$; no bound on microscopic size enters. For the unrestricted-rate class, the lower order already holds for one constant step amplitude $h_*=\min\{H,1/[20(1+\sqrt W)]\}>0$, fixed independently of $D$ and the requested tolerance. The upper bound serves all allowed protocols.

## 2. A common reset gives uniform contraction

This observation also applies to the original family with any $|g_i|\le G$. If $|h(t)|\le H$, every hidden state jumps to $A$ at rate at least

$$
a_H=k e^{-(1+G)H}.
$$

The generator can therefore be decomposed into a common reset to $A$ at rate $a_H$ plus another Markov generator. A reset from $A$ to itself has no effect. Coupling two chains with the same reset clock makes them agree after their first common reset, regardless of the size or rates of $K$. Equivalently, for every signed row vector $v$ of zero total mass, the inhomogeneous propagator satisfies

$$
\|vP_h(t,r)\|_1\le e^{-a_H(t-r)}\|v\|_1,\qquad t\ge r.
$$

This remains valid for signed forcing by variation of constants. In particular, forcing $f(t)$ of zero total mass produces a deviation bounded by $a_H^{-1}\sup_t\|f(t)\|_1$, uniformly in the horizon.

For $\mathcal J(k,W)$, use

$$
\alpha=k e^{-(1+s)H}.
$$

## 3. The kernel determines the exact finite-field mean

Let $a(t)=p_A(t)$, let $x(t)$ be the row vector of hidden-state probabilities, and put $q(t)=x_0(t)$. Define

$$
\Delta(t)=e^{s h(t)}-e^{-s h(t)},\quad
\kappa(t)=k e^{-(1+s)h(t)},\quad
I(t)=k a(t)e^{(1-s)h(t)},
$$

$$
J(t)=k\Delta(t)\left[\frac{a(t)e^{h(t)}}2-q(t)e^{-h(t)}\right],
\qquad
E(t,r)=\exp\!\left[-\int_r^t\kappa(v)\,dv\right].
$$

The exact hidden equation is

$$
\dot x=xK-\kappa x+I\mu+Je_0.
$$

Here $e_0$ is the row unit vector of the distinguished hidden state. The initial hidden law is $x(0)=\mu/2$. If $b=\sum_i x_i=1-a$, variation of constants gives

$$
b(t)=\frac{E(t,0)}2+\int_0^t E(t,r)[I(r)+J(r)]\,dr,
$$

$$
q(t)=\frac{E(t,0)}4+
\int_0^t E(t,r)\left[\frac{I(r)}2+J(r)P_{00}(t-r)\right]dr,
\qquad P_{00}(t)=(e^{Kt})_{00}.
$$

Because $g=2s(\mathbf1_{\{0\}}-1/2)$ and $\mu_0=1/2$,

$$
C(t)=\langle g,e^{Kt}g\rangle_\mu
=W[2P_{00}(t)-1].
$$

Consequently these two scalar Volterra equations, with $a=1-b$ and $m=2b-1$, determine the exact mean from $C,k,W$, and the applied protocol. Their bounded coefficients give uniqueness on each finite interval by the usual Volterra iteration or a Gronwall estimate. Equal kernels in this subclass therefore imply equal finite-field means for every allowed protocol. No expansion in the field was used.

### 3.1 Exact kernel equality also determines the visible path law

For fixed $k,W$ and any $H>0$, two members of $\mathcal J(k,W)$ have the
same kernel if and only if their entire visible path laws agree under
every deterministic piecewise-continuous protocol $|h|\le H$, starting
from zero-field equilibrium. This is an exact equivalence, not an
approximate-path error bound.

To prove sufficiency, decompose the binary path into alternating visits
to $A$ and to the hidden block. While in $A$, the exit hazard is
$k e^{h(t)}\cosh(s h(t))$, independent of $K$. At an $A$-to-hidden jump
at time $u$, the conditional hidden entry distribution is

$$
\xi_u=(1-\theta_u)\mu+\theta_u e_0,
\qquad \theta_u=\tanh(s h(u)).
$$

Its components are exactly $\mu_i e^{g_i h(u)}/\cosh(s h(u))$, so it is
a probability law also when the coefficient $\theta_u$ is negative.
An experiment starting in the hidden block has the conditional law $\mu$.
Both cases have the form $\xi=c\mu+d e_0$, with $c+d=1$.

During such a hidden visit, let $v(t)$ be the unnormalized row law of the
hidden state conditional on entry at $u$, with exit to $A$ treated as
killing. Put $\Gamma(t)=k e^{-h(t)}\Delta(t)$ and
$R(t)=P_{00}(t)=1/2+C(t)/(2W)$. Then

$$
\dot v=vK-\kappa v-\Gamma v_0e_0,\qquad v(u)=\xi.
$$

Variation of constants gives a closed scalar equation for its
distinguished component:

$$
v_0(t)=E(t,u)\left[\frac c2+dR(t-u)\right]
-\int_u^t E(t,r)\Gamma(r)v_0(r)R(t-r)\,dr.
$$

The survival probability of this visible hidden-block visit is

$$
S_B(t\mid u,\xi)=E(t,u)
-\int_u^t E(t,r)\Gamma(r)v_0(r)\,dr.
$$

Equivalently, its exit density is $\kappa(t)S_B(t\mid u,\xi)+\Gamma(t)v_0(t)$.
These quantities are determined by $C$ and the protocol. The scalar
Volterra equation has a unique solution on each finite interval. Since
return to $A$ resets the hidden visit and each subsequent entry has the
displayed law, these conditional sojourn distributions determine the
complete visible path law. The initial visible probabilities are
$1/2,1/2$ in both models.

For necessity, equality of all these path laws implies equality of the
constant-step means for every sufficiently small field. The cubic
coefficients therefore agree, and the [step-response inverse](THEORY.md#6-step-response-and-kernel-recovery)
recovers the same $C$. The stability certificate below controls mean
error; it does not bound a distance between approximate path laws.

## 4. A uniform stability certificate at every field bound

Consider two members of $\mathcal J(k,W)$ with kernels $C,\widetilde C$. Set

$$
B_H=2\sinh(sH),\qquad
\|C-\widetilde C\|_{1,\alpha}
=\int_0^\infty e^{-\alpha t}|C(t)-\widetilde C(t)|\,dt.
$$

Then

$$
\boxed{
\mathcal D_H(F,\widetilde F)
\le\frac{k^2e^{2H}B_H^2}{\alpha W}
\|C-\widetilde C\|_{1,\alpha}.
}
$$

**Proof.** Drive the second model by the same protocol, and denote its quantities by tildes. Reconstruct a row vector on the first model's hidden states by

$$
x^*(t)=\frac{E(t,0)}2\mu+
\int_0^t E(t,r)
\left[\widetilde I(r)\mu+\widetilde J(r)e_0e^{K(t-r)}\right]dr.
$$

The scalar killing factor $E$ is common to the two models. The total mass of $x^*$ equals $\widetilde b$, while its distinguished coordinate satisfies

$$
x^*_0(t)=\widetilde q(t)+e(t),\qquad
e(t)=\frac1{2W}\int_0^t E(t,r)
[C(t-r)-\widetilde C(t-r)]\widetilde J(r)\,dr.
$$

The vector $p^*=(\widetilde a,x^*)$ has mass one and the surrogate's visible mean, although it need not be nonnegative. Evaluating the first model's physical generator at $p^*$ changes its scalar source from $\widetilde J$ to $\widetilde J-k e^{-h}\Delta e$. Thus

$$
\dot p^*=p^*Q(h)+k e^{-h}\Delta e\,(e_0-e_A),\qquad p^*(0)=\pi_0.
$$

The common-reset contraction applies to the difference between the true law and this signed, mass-one reconstruction. Since $\|e_0-e_A\|_1=2$,

$$
\sup_t|m_F[h](t)-m_{\widetilde F}[h](t)|
\le\frac{2ke^H B_H}{\alpha}\sup_t|e(t)|.
$$

The second model is a genuine probability law. Its nonnegative coordinates satisfy $\widetilde a+\widetilde q\le1$, so

$$
\left|\frac{\widetilde a e^h}{2}-\widetilde q e^{-h}\right|
\le\max\{e^h/2,e^{-h}\}\le e^H,
\qquad |\widetilde J|\le kB_He^H.
$$

Also $E(t,r)\le e^{-\alpha(t-r)}$. Therefore

$$
\sup_t|e(t)|\le\frac{kB_He^H}{2W}\|C-\widetilde C\|_{1,\alpha},
$$

which proves the certificate. The bound has no small-field or small-feedback restriction. Its constants are sufficient, not optimized.

## 5. Constructive finite-field upper bounds

Apply the [positive quadrature theorem](FINITE_ACCURACY.md#8-a-stronger-bound-by-positive-gaussian-quadrature) with damping parameter $\alpha$ in place of $k$. For every $n\ge1$, it supplies a positive kernel of the same mass with at most $2n(n+1)+1$ active rates and

$$
\|C-\widetilde C_n\|_{1,\alpha}
\le\frac{4W}{\alpha}16^{-n}.
$$

The Jacobi realization belongs to $\mathcal J(k,W)$, with the original physical switching rate $k$; using $\alpha$ to construct the approximation does not change $k$. Its total state count and finite-field error satisfy

$$
\boxed{
D_n\le2n(n+1)+3,\qquad
\mathcal D_H(F,\widetilde F_n)
\le A_H16^{-n},\qquad
A_H=4e^{(4+2s)H}B_H^2.
}
$$

This is a bound on the exact finite-amplitude mean, with no residual Taylor-error floor.

For the rate-capped class $0<\lambda_j\le\Lambda=3k$, a single $n$-node Gaussian rule already gives a geometric bound. Let

$$
\rho_H=\frac{\Lambda}{2\alpha+\Lambda}<1.
$$

Expand $e^{-\lambda t}$ around $\Lambda/2$. Gaussian quadrature cancels the first $2n$ polynomial terms, and both positive measures have mass $W$. Integrating the remaining absolute Taylor series against $e^{-\alpha t}$ gives

$$
\begin{aligned}
\|C-\widetilde C_n\|_{1,\alpha}
&\le\frac{2W}{\alpha+\Lambda/2}
\sum_{j=2n}^\infty
\left(\frac{\Lambda/2}{\alpha+\Lambda/2}\right)^j\\
&=\frac{2W}{\alpha}\rho_H^{2n}.
\end{aligned}
$$

The quadrature nodes lie within the positive rate support. If it has at most $n$ atoms, retain it exactly. The resulting target-family surrogate has at most $n+2$ total states and

$$
\mathcal D_H(F,\widetilde F_n)
\le2e^{(4+2s)H}B_H^2\rho_H^{2n}.
$$

It preserves the active-rate cap as well as all the structural properties above.

## 6. A Taylor remainder uniform in size and horizon

Only targets need this estimate for the lower bound. More generally, consider any original-family model with $|g_i|\le G$, write $L=1+G$, and apply $h(t)=z u(t)$ with $|u|\le1$. Let $p_j$ be its probability-law Taylor coefficients, with derivatives divided by factorials. For the row-generator coefficients,

$$
Q(zu(t))=Q_0+\sum_{j\ge1}z^jQ_j(t),\qquad
\|Q_j(t)\|_{1\to1}\le\frac{2kL^j}{j!}.
$$

The internal generator cancels in these field derivatives. Every $Q_j$ has zero row sums. The zero-field common reset has rate $k$, so coefficient variation of constants yields

$$
\sup_t\|p_j(t)\|_1\le b_jL^j,\qquad
b_0=1,\qquad b_j=2\sum_{\ell=1}^j\frac{b_{j-\ell}}{\ell!}.
$$

In particular,

$$
b_1=2,\qquad b_2=5,\qquad b_3=\frac{37}{3},\qquad b_4=\frac{365}{12}.
$$

This coefficient estimate alone need not be used to infer convergence. Instead insert the finite Taylor polynomial $P_3=\sum_{j=0}^3z^jp_j$ into the exact master equation. Its residual is a sum of generator Taylor tails. With $x=L|z|$,

$$
\|P_3Q(zu)-\dot P_3\|_1
\le2ke^x x^4\sum_{j=0}^3\frac{b_j}{(4-j)!}
=k b_4 e^x x^4.
$$

The residual has zero mass and the exact and polynomial initial laws agree. Apply the driven common-reset contraction at rate $ke^{-x}$ to their difference. Since the readout has absolute value one,

$$
\boxed{
\sup_t|m[zu](t)-z m_1[u](t)-z^3m_3[u](t)|
\le\frac{365}{12}e^{2L|z|}(L|z|)^4.
}
$$

The constant term vanishes and $m_2=0$ by the original-family response equations. This holds on every horizon with the same bound, for every microscopic size and every reversible $K$. In particular, for the finite-field targets define

$$
R_H=\frac{365}{12}e^{2(1+s)H}(1+s)^4;
$$

then the uniform remainder is at most $R_H|z|^4$ for $|z|\le H$.

## 7. A lower bound at one fixed nonzero amplitude

Set

$$
h_*=minleft{H,rac1{20(1+s)}
ight},qquad
gamma=e^{-h_*}sinh(s h_*).
$$

For every $Dge2$, put $r=D+3$. The [fixed-field proof](FIXED_FIELD_LOWER_BOUND.md) constructs a target with $r+2=D+5$ states for which

$$
oxed{
E_D^{mathrm{field}}(k,W,H)
gerac{	anh(h_*)gamma^2}{640r^2}
exp[-2pisqrt{6(r-1)}].
}
$$

Only the response to the constant field $h_*$ is used. This amplitude is independent of $D$, target size, and requested tolerance. Together with Section 5, the lower bound proves the squared-logarithmic state order even for this single-step prediction task, with error uniform over observation times.

The mechanism is exact. A reversible equilibrium-to-field step mean is a constant minus a positive exponential sum. For a canonical target with a geometric internal spectrum, its nonzero symmetrized field generator is a diagonal matrix plus one positive rank-one matrix. The secular equation locates each hidden field eigenvalue within a distance proportional to $1/r$ of its internal diagonal value and bounds its visible weight from below. A Cauchy Gram matrix then gives a root-exponential Hankel singular-value bound. A $D$-state constant-field Markov mean has Hankel rank at most $D$, independent of its field derivatives or passive behavior. The detailed proof supplies all constants and the generator reduction.

### A second route, used for the capped bound

The uniform target remainder from Section 6 gives a simpler alternative whenever a cubic step curve has a positive exponential decomposition

$$
m_3(	au)=B(	au)-sum_{j=1}^r w_je^{-eta_j	au},qquad
B(	au)=b_0+(b_1+b_2	au)e^{-2	au},qquad w_j>0,
$$

where $	au=kt$. Suppose the positive Hankel operator of the exponential sum, on $L^2(e^{-	au}d	au)$, has least positive eigenvalue at least $sigma_r$. Uniform curve error bounds Hankel operator error by the same number because this measure has mass one.

The linear curve $m_1=1-e^{-2	au}$ lies in the same rank-three baseline span as $B$. For $r=D+4$, a competitor's constant-step curve minus $z m_1+z^3B$ consequently has Hankel rank at most $D+3=r-1$. Only the target is Taylor expanded. At step amplitude $zle H$, any uniform prediction error $delta$ must satisfy

$$
delta+R_Hz^4ge z^3sigma_r.
$$

Choosing $z_D=min{H,sigma_r/(2R_H)}$ gives

$$
deltagerac{sigma_r z_D^3}{2}.
$$

This second argument permits a shrinking witness amplitude; it makes no inference from a competitor's finite-field error to its derivatives. Section 8 uses it for the capped class. The stronger fixed-amplitude theorem above is the primary unrestricted-rate lower bound.

## 8. The capped lower bound

For $r=D+4$, replace the geometric nodes by

$$
a_j=\frac72+\frac{j-1}{r-1},\qquad
\lambda_j=k(a_j-3/2)\in[2k,3k],\qquad c_j=W/r.
$$

The same cubic decomposition applies. Its weights satisfy $w_j\ge W/(2r)$. The Gram matrix is $\mathsf C_{ij}=1/(a_i+a_j)$, whose inverse diagonal is

$$
(\mathsf C^{-1})_{ii}
=2a_i\prod_{j\ne i}\left(\frac{a_i+a_j}{a_i-a_j}\right)^2.
$$

Here $2a_i\le9$, and equally spaced nodes give

$$
\prod_{j\ne i}\frac{a_i+a_j}{|a_i-a_j|}
\le\frac{[9(r-1)]^{r-1}}{(i-1)!(r-i)!}
\le(18e)^{r-1}.
$$

The last inequality uses $\binom{r-1}{i-1}\le2^{r-1}$ and $(r-1)!\ge((r-1)/e)^{r-1}$. Therefore

$$
\operatorname{tr}\mathsf C^{-1}\le9r(18e)^{2r-2},\qquad
\lambda_{\min}^+(\mathsf K)\ge
\sigma_r^{\mathrm{cap}}
:=\frac{W}{18r^2(18e)^{2r-2}}.
$$

Apply the second route in Section 7 with $\sigma_r^{\mathrm{cap}}$ and
$z_D=\min\{H,\sigma_r^{\mathrm{cap}}/(2R_H)\}$. The resulting lower bound is exponential in $D$ up to polynomial factors. Together with the capped upper bound, it proves the logarithmic state order.

## 9. Meaning and boundaries

The passive visible process is exactly two-state, yet a single Markov predictor that must remain accurate under every field protocol in a fixed nonzero interval has a tolerance-dependent state requirement. The requirement is already present without forcing a competitor to preserve passive behavior or thermodynamic structure. Conversely, the upper construction preserves all that structure while attaining the same asymptotic order.

This strengthens the cubic-coefficient result in two concrete ways: the approximation target is an actual finite-field observable, and a competitor's arbitrary higher field derivatives cannot evade the lower bound. It remains a worst-case, known-kernel, physical-state-count theorem. It does not count bits, parameter precision, running time, or samples; it does not assert a finite-field compression theorem for every centered bounded sensitivity vector; and its norm concerns single-time means rather than an approximate full path distribution. Sharp constants, finite-sample measurement requirements, and compression of the broader sensitivity family remain separate questions.

## 10. Why the target restriction matters: the same kernel can hide higher response

Outside $\mathcal J(k,W)$, the cubic kernel need not determine the exact
finite-field mean, even when $k,\mu,g$ and the functional actuator rule are
held fixed. An explicit four-state example uses $k=1$ and three hidden states:

$$
\mu=(1/3,1/3,1/3),\qquad g=(-1,0,1),\qquad W=2/3,
$$

$$
K_\eta=
\begin{pmatrix}
-1/2-\eta/6&\eta/3&1/2-\eta/6\\
\eta/3&-2\eta/3&\eta/3\\
1/2-\eta/6&\eta/3&-1/2-\eta/6
\end{pmatrix},\qquad 0<\eta<3.
$$

These generators are irreducible and reversible under the same $\mu$.
They satisfy $K_\eta g=-g$, and therefore all have exactly the same kernel

$$
C(t)=\frac23e^{-t}.
$$

Their passive path laws, equilibrium curves, and mean-response coefficients
through cubic order agree for every bounded protocol. Nevertheless, for
any two parameters $\eta_1\ne\eta_2$ and a constant nonzero field $h$, their
exact mean curves obey

$$
\boxed{
\left.\frac{d^3}{dt^3}
\bigl(m_{\eta_2}[h](t)-m_{\eta_1}[h](t)\bigr)\right|_{t=0}
=\frac{4(\eta_2-\eta_1)}9
e^{-h}\sinh(h)\bigl(\cosh(h)-1\bigr)^2\ne0.
}
$$

Here both experiments start from the same zero-field equilibrium.
Thus the finite-field means differ despite identical cubic kernels and
identical sensitivity values at each hidden state.

**Derivation.** Write the full row generator as
$Q_\eta(h)=M(h)+\overline K_\eta$, where $M$ contains only the transitions
between $A$ and the hidden block, and $\overline K_\eta$ is $K_\eta$ extended
by zeros on $A$. Put $p_0=(1/2,1/6,1/6,1/6)$ and
$f=(-1,1,1,1)^T$. Since $p_0\overline K_\eta=0$ and
$\overline K_\eta f=0$,

$$
\left.\frac{d^3m_\eta[h]}{dt^3}\right|_{t=0}
=p_0M^3f+p_0M\overline K_\eta Mf.
$$

Let $w=(1,-2,1)^T$, and let $P_w$ be the orthogonal projector onto $w$
in the $\mu$ inner product. Then
$K_{\eta_2}-K_{\eta_1}=-(\eta_2-\eta_1)P_w$.
The hidden part of $p_0M$ is the row vector with entries
$\mu_j e^{hg_j}\sinh h$, and the hidden part of $Mf$ has entries
$-2e^{-h}e^{hg_j}$. Their product with this generator difference is

$$
2(\eta_2-\eta_1)e^{-h}\sinh h\,
\|P_we^{hg}\|_\mu^2,
\qquad
\|P_we^{hg}\|_\mu^2
=\frac29(\cosh h-1)^2,
$$

which proves the displayed identity. The first two time derivatives are
independent of $\eta$ by the same endpoint cancellations. Taking the
coefficient of $h^5$ gives, for the unit-protocol fifth Taylor coefficient,

$$
m_{5,\eta_2}(t)-m_{5,\eta_1}(t)
=\frac{\eta_2-\eta_1}{54}\,t^3+O(t^4)
\qquad(t\downarrow0).
$$

This is a boundary of the sufficient statistic: $C$ closes the cubic mean
response in the full original family, but closes the exact finite-field
mean only under the additional realization structure proved above. The
counterexample does not invalidate the finite-field theorem for
$\mathcal J(k,W)$, and makes no claim that fifth order is always the first
possible discrepancy outside that subclass.

The [fixed-actuator hierarchy](FIXED_ACTUATOR_HIERARCHY.md) extends this
obstruction to arbitrarily high response order, with a fixed internal rate
band. The [actuator-process theorem](ACTUATOR_PROCESS.md) identifies the
complete information for general controlled visible path laws. The
[reversible general upper bound](REVERSIBLE_GENERAL_COMPRESSION.md) now
establishes fixed-accuracy mean compression with exact variance and a
nonsharp state bound. The [general controlled lower bound](GENERAL_CONTROLLED_LOWER_BOUND.md)
exceeds every fixed power of the logarithm of the inverse error, even with
binary sensitivities, bounded internal rates, and fixed minimum control
dwell time. It proves a quantitative separation from the sharp subclass
theorem above.
