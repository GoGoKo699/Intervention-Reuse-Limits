# Exact passive compression and cubic intervention response

[Repository overview](../README.md) · [Finite-accuracy results](FINITE_ACCURACY.md) · [Prior art](PRIOR_ART.md)

**Working derivation, 22 September 2026.** The arguments below have deterministic consistency checks, not independent proof review or certified originality. This is a finite-state stochastic model, not a turbulence theorem.

## 1. Model and comparison class

There are $N=M+1$ states $A,B_1,\ldots,B_M$. The observed variable is $S(A)=-1$ and $S(B_j)=+1$. Choose a rate $k>0$, positive probability vector $\mu$, an irreducible row generator $K$ reversible under $\mu$, and a fixed vector $g$ satisfying $\sum_j\mu_jg_j=0$. Write $\langle f,v\rangle_\mu=\sum_j\mu_jf_jv_j$.

A dimensionless applied field $h$ changes the off-diagonal rates as follows:

$$
q_{AB_j}(h)=k\mu_j e^{(1+g_j)h},\qquad
q_{B_jA}(h)=k e^{(g_j-1)h},\qquad
q_{B_iB_j}(h)=K_{ij}\quad(i\ne j).
$$

Every diagonal is minus its row's outgoing sum. Column probabilities obey $\dot p=Q(h)^Tp$. The same $K$ and $g$ are retained when the field changes. All response calculations start from zero-field equilibrium.

The exact lower bound concerns **finite-state autonomous Markov surrogates with rates analytic in the field near zero**, a fixed state readout and a fixed initial distribution. The surrogate need not be reversible or a partition of the original states. Exact equality of one Taylor coefficient as a function of time is required. The bound is not a statement about stored bits, arbitrary nonlinear differential equations, memory-based models, or approximate fitting.

## 2. Detailed balance and physical interpretation

For every constant field,

$$
\pi_h(A)=\frac{e^{-h}}{2\cosh h},\qquad
\pi_h(B_j)=\frac{\mu_j e^h}{2\cosh h}.
$$

Both directed equilibrium fluxes on the $A$--$B_j$ edge equal $k\mu_j e^{g_jh}/(2\cosh h)$. Internal detailed balance follows from $K$. Consequently,

$$
\mathbb E_{\pi_h}S=\tanh h.
$$

In thermal units, state energies $E_A(h)=h$ and $E_{B_j}(h)=-h-\log\mu_j$, with transition-state shifts $W_j(h)=W_j(0)-g_jh$, produce the displayed field factors through Arrhenius rates. Fixed baseline barriers supply the prefactors. Internal transition-state energies can shift by $-h$ alongside the $B$ energies, leaving $K$ unchanged.

This specifies a thermodynamically consistent kinetic coupling; it is not a demonstrated molecular mechanism. The distinction between thermodynamic and kinetic field coupling is established response theory, not a contribution claimed here; see [Basu et al. and Diezemann](PRIOR_ART.md).

## 3. Exact passive path law

At $h=0$, the total exit rate from $A$ to the $B$ block is $k$, and the exit rate from every $B_j$ to $A$ is $k$. Thus the partition is strongly lumpable, with visible generator

$$
\overline Q=\begin{pmatrix}-k&k\\k&-k\end{pmatrix}.
$$

This is equality of **the entire visible path distribution**, for every microscopic initial law with the same visible initial law. No passive observation of $S$ identifies $K$. At equilibrium, $\mathbb E_0[S(0)S(t)]=e^{-2kt}$. A single fixed-readout state cannot reproduce this binary switching process, so the passive state count is exactly two.

An essential positive boundary: multiplying all microscopic transitions from one visible block to another by the same block-dependent factor preserves lumpability. A block-uniform potential tilt therefore does not automatically destroy a coarse model. Our example uses explicitly nonuniform kinetic sensitivities $g$; it does not assign arbitrary unspecified behavior to interventions.

## 4. Visible and hidden equations

Parameterize the law by

$$
p_A=\frac{1-m}{2},\qquad
p_{B_j}=\frac{\mu_j}{2}(1+m+v_j),\qquad
\langle v\rangle_\mu=0,
$$

where $m=\mathbb E S$. Let $G(h)=\langle e^{hg}\rangle_\mu$. Substitution in the master equation, using reversibility to act on relative densities, gives

$$
\dot m=2kG(h)(\sinh h-m\cosh h)-ke^{-h}\langle e^{hg}v\rangle_\mu,
$$

$$
\dot v=Kv+2k(e^{hg}-G(h))(\sinh h-m\cosh h)
-ke^{-h}(e^{hg}v-\langle e^{hg}v\rangle_\mu).
$$

Vector products and exponentials are componentwise. Scalar terms in the vector equation denote constant vectors. Initially $m=0$ and $v=0$.

## 5. Arbitrary bounded weak protocols

Set $h(t)=\epsilon u(t)$ for a bounded, piecewise continuous protocol on a finite horizon, and expand

$$
m=\epsilon m_1+\epsilon^2m_2+\epsilon^3m_3+O(\epsilon^4).
$$

These coefficients are derivatives divided by factorials. In particular, $m_3$ is the third derivative divided by $3!$. Centering $g$ gives

$$
\dot m_1=2k(u-m_1),\qquad m_2=0,\qquad v_1=0,
$$

$$
\dot v_2=(K-kI)v_2+2kg\,u(u-m_1).
$$

Define the internal kinetic kernel and its mass,

$$
C(t)=\langle g,e^{Kt}g\rangle_\mu,\qquad W=C(0).
$$

Here $K$ is the internal $B$ generator, not an independent hidden process that continues autonomously through visits to $A$. The full passive-process observable equal to zero on $A$ and $g_j$ on $B_j$ has equilibrium autocorrelation $e^{-kt}C(t)/2$.

The ordinary two-state reference has rates $ke^h$ and $ke^{-h}$. Its cubic coefficient $b_3$ and the correction $\delta=m_3-b_3$ obey

$$
\dot b_3=-2kb_3+2k\left(\frac{u^3}{6}-\frac{m_1u^2}{2}\right),
$$

$$
\begin{aligned}
\dot\delta={}&-2k\delta+kWu(t)^2[u(t)-m_1(t)]\\
&-2k^2u(t)\int_0^t e^{-k(t-s)}C(t-s)
 u(s)[u(s)-m_1(s)]\,ds.
\end{aligned}
$$

All coefficients initially vanish. These equations follow by expanding the exact equations and solving the linear equation for $v_2$. They show that $k$ and $C$ determine the single-time mean through cubic order for every such protocol. They are not a closure at arbitrary finite field, nor a uniform-in-time Taylor remainder estimate.

## 6. Step response and kernel recovery

For $u=1$,

$$
m_1(t)=1-e^{-2kt},\qquad
b_3(t)=-\frac{1-e^{-2kt}}{3}+kt e^{-2kt}.
$$

The reference mean at finite field is $\tanh h[1-e^{-2k\cosh h\,t}]$. Solving the hidden coefficient equation gives

$$
\langle g,v_2(t)\rangle_\mu=2ke^{-2kt}\int_0^t e^{ks}C(s)\,ds,
$$

and hence

$$
m_3(t)=b_3(t)+e^{-2kt}\left[kWt-2k^2\int_0^t(t-s)e^{ks}C(s)\,ds\right].
$$

Differentiating twice gives the exact inverse:

$$
C(t)=-\frac{e^{-kt}}{2k^2}\frac{d^2}{dt^2}
\left[e^{2kt}(m_3(t)-b_3(t))\right].
$$

At fixed $k$, **two members of this family have identical cubic single-time responses for every bounded weak protocol if and only if their kernels agree**. Sufficiency follows from the protocol equations; necessity follows from the step inverse. This is noiseless identifiability, not stable statistical estimation. A scalar function can encode many modes.

## 7. The three-state example

Take $k=1$, $\mu=(1/2,1/2)$, $g=(1,-1)$, and

$$
K=\begin{pmatrix}-r&r\\r&-r\end{pmatrix},\qquad r>0.
$$

The kernel is $C(t)=e^{-2rt}$. Changing $r$ changes only internal kinetics, not the field rule. The passive path law, full static response, dynamic linear response, and vanishing quadratic mean response remain unchanged. Examples are

$$
\begin{aligned}
r=\tfrac14:\quad m_3(t)&=-\tfrac13+(\tfrac{25}{3}+6t)e^{-2t}-8e^{-3t/2},\\
r=1:\quad m_3(t)&=-\tfrac13+\tfrac73e^{-2t}-2e^{-3t},\\
r=\tfrac12:\quad m_3(t)&=-\tfrac13+(\tfrac13+2t-t^2)e^{-2t}.
\end{aligned}
$$

The last case is a pole collision, included as a check. The remainder is generally $O(h^4)$, **not** $O(h^5)$: zero quadratic response does not imply that every even coefficient vanishes. None of these statements extends automatically to arbitrary path-dependent observables or nonequilibrium hidden initial preparations.

## 8. Exact response state-count bound

Reversibility and centering give

$$
C(t)=\sum_{j=1}^{r_*}c_j e^{-\lambda_jt},\qquad c_j>0,\quad\lambda_j>0,
$$

where the rates are distinct active eigenvalues of $-K$. Set

$$
\Phi_d(t)=\frac{e^{dt}-1-dt}{d^2},\qquad \Phi_0(t)=\frac{t^2}{2}.
$$

Then

$$
m_3=b_3+e^{-2kt}\left[kWt-2k^2\sum_jc_j\Phi_{k-\lambda_j}(t)\right].
$$

If every $\lambda_j\ne k$, the coefficient of $e^{-(k+\lambda_j)t}$ is $-2k^2c_j/(k-\lambda_j)^2$, which is nonzero. The constant term is $-1/3$. The coefficient of $e^{-2kt}$ without a time multiplier is $1/3+2k^2\sum_jc_j/(k-\lambda_j)^2>0$. Thus the Laplace transform has at least $r_*+2$ distinct pole locations: $0$, $-2k$, and the $-(k+\lambda_j)$.

**Pole-location lemma.** A $D$-state analytic autonomous Markov surrogate has Laplace mean

$$
\widehat f^T(zI-\widehat Q(h)^T)^{-1}\widehat p_0.
$$

Field derivatives are finite sums of products of unperturbed resolvents and derivatives of the generator. Products increase pole orders but cannot introduce pole locations outside the spectrum of $\widehat Q(0)$. There are at most $D$ distinct eigenvalues. The argument does not require diagonalizability or reversibility. Analytic field dependence of the preparation or readout would not create additional pole locations either.

It follows that exact reproduction of the cubic curve requires $D\ge r_*+2$. Equality on an open time interval suffices by analyticity. This is an elementary realization argument; minimal-realization theory itself is established prior art.

### Explicit all-size family

For any $N\ge3$, put $M=N-1$, use uniform $\mu$, and let $K$ be the reflecting path walk with rate $0<\rho<k/4$ on every neighboring edge. Choose $g_j=\mathbf1_{\{j=1\}}-1/M$. Then

$$
\lambda_\ell=2\rho\left[1-\cos\left(\frac{\pi\ell}{M}\right)\right],\qquad
c_\ell=\frac{2}{M^2}\cos^2\left(\frac{\pi\ell}{2M}\right),
\quad 1\le\ell<M.
$$

The normalized eigenfunctions are $\sqrt2\cos[\pi\ell(j-1/2)/M]$. Their overlaps with $g$ give the stated positive weights. All $M-1$ rates are distinct and strictly below $k$. Hence $D\ge M+1=N$, attained by the original model. Passive observation needs exactly two states, whereas exact cubic response needs $N$.

This elementary construction has $W=(M-1)/M^2$, so its total correction shrinks with size. The [finite-accuracy note](FINITE_ACCURACY.md) both removes that shrinking-signal feature and proves that a size-independent approximate surrogate nevertheless exists. The exact lower bound must not be advertised as a fixed-error lower bound.

## 9. Minimal reversible realization of a positive kernel

Every finite positive kernel with $r$ distinct rates,

$$
C(t)=\sum_{j=1}^{r}c_j e^{-\lambda_jt},\qquad
c_j>0,\quad\lambda_j>0,\quad W=\sum_jc_j>0,
$$

has an irreducible reversible realization with $r+1$ hidden states and
$|g_i|=\sqrt W$. Adding $A$ gives $r+2$ total states under the same functional
field rule. This is a corollary of the established finite Jacobi
inverse-spectral construction, not a claim of new realization theory;
see [the prior-art audit](PRIOR_ART.md). The proof below states the construction
explicitly so its positivity and sensitivity bound can be checked.

Define a probability measure on $r+1$ distinct points by

$$
\nu=\frac12\delta_0+\sum_{j=1}^r\frac{c_j}{2W}\delta_{-\lambda_j}.
$$

Apply Gram--Schmidt to $1,x,\ldots,x^r$ in $L^2(\nu)$, choosing positive
leading coefficients. Multiplication by $x$, in this orthonormal polynomial
basis, has a symmetric tridiagonal matrix $J$ with strictly positive
off-diagonal entries. The three-term recurrence follows because $x p_i$ is
orthogonal to $p_j$ for $j<i-1$: transferring multiplication by $x$ gives
$\langle x p_i,p_j\rangle_\nu=\langle p_i,x p_j\rangle_\nu=0$.
The adjacent coefficient is the ratio of two positive leading coefficients.

The multiplication operator has eigenvalues $0,-\lambda_1,\ldots,-\lambda_r$.
Its spectral measure at the first basis vector $e_0$, which represents the
constant polynomial $1$, is exactly $\nu$. Since $0$ is the largest
eigenvalue and $J$ has positive neighboring entries, the Perron--Frobenius
theorem applied after adding a sufficiently large scalar multiple of $I$
gives a strictly positive normalized null vector $v$. Its first component
satisfies $v_0^2=\nu(\{0\})=1/2$.

Set

$$
D=\operatorname{diag}(v),\qquad
K=D^{-1}JD,\qquad \mu_i=v_i^2,\qquad
g_i=2\sqrt W\left(\mathbf1_{\{i=0\}}-\frac12\right).
$$

The positive neighboring entries of $K$ make it irreducible; $K\mathbf1=0$
follows from $Jv=0$, and all its other off-diagonal entries are zero.
Thus $K$ is a row generator. Also
$\mu_iK_{ij}=v_iJ_{ij}v_j=\mu_jK_{ji}$, proving reversibility.
The identity $\mu_0=1/2$ gives $\langle g\rangle_\mu=0$ and
$|g_i|=\sqrt W$ for every state.

Write $P(t)=e^{Kt}$. Similarity and the prescribed spectral measure give

$$
P_{00}(t)=(e^{Jt})_{00}
=\frac12+\sum_j\frac{c_j}{2W}e^{-\lambda_jt}.
$$

Stationarity then yields

$$
\langle g,e^{Kt}g\rangle_\mu
=4W\mu_0\bigl(P_{00}(t)-\mu_0\bigr)
=\sum_jc_j e^{-\lambda_jt}.
$$

Consequently, at fixed $k$, this model reproduces the cubic mean response
for every bounded weak protocol, as well as the exact passive path law,
equilibrium curve, linear response and zero quadratic response. If the
source model has $|g|\le G$, its mass satisfies $W\le G^2$, so the
realization preserves that sensitivity bound. Repeated rates are merged
before applying the construction. The case $W=0$ uses the ordinary
two-state reference.

When all $\lambda_j\ne k$, Section 8 gives the matching lower bound
$D\ge r+2$ for **any** analytic autonomous finite-state Markov surrogate
reproducing the cubic step curve. The construction therefore attains the
exact minimum in that noncollision case. It remains valid if a rate equals
$k$, but the distinct-pole proof does not establish minimality there.
The construction puts no prescribed upper bound on microscopic rates and
does not preserve an arbitrary source topology.

[The minimal-realization verifier](../scripts/verify_minimal_realization.py)
checks this construction on small deterministic spectra, including a
collision at $\lambda=k$ and merged repeated rates. These are consistency
checks, not independent validation or a novelty certificate.

## 10. Status

The model, equations, inverse, and state-count construction are derived here and checked by [the executable verification](VERIFICATION.md). Their publication-level novelty remains under audit against response theory, controlled lumpability, and nonlinear realization theory. No experimental application, optimal controller, universal compression impossibility, or journal-level claim follows from this note.
