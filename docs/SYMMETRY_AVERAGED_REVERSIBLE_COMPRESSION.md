# Symmetry-averaged reversible compression of the finite target

[Finite twelve-versus-eleven advantage](FINITE_REVERSIBILITY_ADVANTAGE.md) · [Bounded rational observation certificate](BOUNDED_RATIONAL_OBSERVATION_CERTIFICATE.md) · [Uniform physical robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md) · [Finite observation bottlenecks](FINITE_OBSERVATION_BOTTLENECK.md) · [Source and novelty audit](RATIONAL_OBSERVATION_SOURCE_AUDIT.md)

**Analytic upper bound, 23 September 2026.** The same twelve-state target used in the finite state-advantage theorem has a nine-total-state ordinarily reversible predictor whose controlled binary means differ by at most $1/2376$ on every protocol using fields $\{0,\log2\}$, at every horizon. Durations need not lie on the observation clock. The hidden exit cap remains $2k$. This gives an upper bound on the precision needed to exclude all smaller ordinary reversible models; it does not identify the optimal approximation error or improve the lower theorem's certified tolerance.

The construction averages two nearby probe barriers and takes an exact symmetry quotient. Its error is quadratic because the first perturbation is odd under a symmetry that preserves preparation and readout. No new controls, preparations, readouts, or uncounted predictor states are used. On the two queried fields, the predictor can retain the original exponential barrier rule. A separate all-field bound below permits arithmetic averages of barrier curves, as allowed by the broader kinetic interface class.

## 1. Target, symmetry, and the nine-state predictor

Use the target of [the finite theorem, Sections 1–2](FINITE_REVERSIBILITY_ADVANTAGE.md): six memory states indexed by edges of $K_{2,3}$ with vertex parts $\{1,2\}$ and $\{3,4,5\}$, and five probes $p_i$. Write $d=(3,3,2,2,2)$. The hidden law and generator are

$$
\mu(e)=\frac1{12},\qquad \mu(p_i)=\frac{d_i}{24},\qquad
K=K^0+k(J-I),
\tag{1}
$$

where $K^0(e,p_i)=k/2$ and $K^0(p_i,e)=k/d_i$ for incident pairs, and $J$ refreshes conditionally within each of the memory and probe blocks. The full state count is twelve, including $A$. The hidden generator is ordinarily reversible, has exits at most $2k$, and has nonzero relaxation rates in $[k,3k]$.

Set $H=\log2$, $r(h)=e^{2h}$, and

$$
\beta_j=\frac{6+j}{16},\qquad b_j(h)=\beta_j^{h/H},\qquad
q_{iA}=kb_i(h),\quad q_{Ai}=k\mu_i r(h)b_i(h).
\tag{2}
$$

All memory states have label $0$, and probe $p_i$ has label $i$. Preparation is $\pi_0=(1/2,\mu/2)$ and readout is $S=(-1,1_{\rm hid})$.

Let $\Theta$ exchange vertices $3,4$: it exchanges $p_3,p_4$, $(1,3),(1,4)$, and $(2,3),(2,4)$, and fixes the other states, including $A$. It preserves $K,\mu,\pi_0,S$. Replace only $b_3,b_4$ by

$$
\bar b_3(h)=\bar b_4(h)=\frac{b_3(h)+b_4(h)}2.
\tag{3}
$$

Call the resulting full generator $\bar Q_h$. It commutes with $\Theta$, so its orbit partition is strongly lumpable. There are four memory orbits and four probe orbits, hence **eight hidden states plus $A$**. For hidden orbits $O,O'$, the quotient is explicitly

$$
\bar\mu_O=\sum_{i\in O}\mu_i,\qquad
\bar K_{OO'}=\sum_{j\in O'}K_{ij}\quad(i\in O),\qquad
\bar b_O=\bar b_i\quad(i\in O).
\tag{4}
$$

The rate sum is independent of the representative $i$. Summing detailed balance over each orbit pair proves ordinary reversibility under $\bar\mu$. Quotient exits are no greater than the original exits, hence at most $2k$; the quotient's nonzero hidden relaxation rates are a subset of those of $K$. Its physical rates have exactly the interface form (2) with $\bar\mu,\bar b$, and its preparation and readout are the same visible/hidden conventions. Its controlled means equal those of $\bar Q$ exactly.

At the queried fields,

$$
\bar b_O(0)=1,\qquad \bar b_{\{p_3,p_4\}}(H)=\frac{19}{32}.
\tag{5}
$$

All other endpoint barriers are inherited. Thus these endpoints can equally be implemented by the exponential curve $(19/32)^{h/H}$. It agrees with (3) at $0,H$, so all two-field protocols have the same quotient predictions. It does not generally agree with (3) at intermediate fields.

## 2. Symmetry cancellation and uniform propagation

Use row laws and define $\|v\|_{\rm TV}=\tfrac12\sum_i|v_i|$ for signed rows. Put

$$
Q_h=\bar Q_h+V_h,\qquad
\Theta V_h\Theta=-V_h,\qquad
\eta=\sup_h\max_x\|(V_h)_{x\cdot}\|_{\rm TV}.
\tag{6}
$$

Here $\Theta$ also denotes its permutation matrix. For the actual law $p$, its even and odd parts satisfy

$$
p_e=\frac{p+p\Theta}2,\quad p_o=\frac{p-p\Theta}2,\qquad
p_e'=p_e\bar Q+p_oV,\quad p_o'=p_o\bar Q+p_eV.
\tag{7}
$$

The even part is a probability law; $p_o$ has zero mass and starts at zero. The reference law $\bar p$ is even. Since $S$ is even,

$$
(p-\bar p)S=(p_e-\bar p)S.
\tag{8}
$$

For context, suppose the reference propagation contracts every zero-mass row at rate $\alpha>0$. The bound $\|p_eV\|_{\rm TV}\le\eta$ gives $\|p_o\|_{\rm TV}\le\eta/\alpha$. Also

$$
\|vV\|_{\rm TV}\le 2\eta\|v\|_{\rm TV}.
\tag{9}
$$

A second variation-of-constants estimate gives $\|p_e-\bar p\|_{\rm TV}\le2\eta^2/\alpha^2$ and binary-mean error at most $4\eta^2/\alpha^2$, uniformly in the horizon. These are finite-amplitude inequalities, not a truncated response expansion. A return reset to $A$ at rate $\alpha$ is one sufficient contraction mechanism. The target permits sharper source and propagation bounds.

### Two-field occupation and odd-source bounds

For every protocol with fields $0,H$, the actual law remains in

$$
p_A\le\frac12,\qquad f_i:=p_i/\mu_i\le2.
\tag{10}
$$

Initially $p_A=1/2$ and $f_i=1/2$. The density equation is

$$
f_i'=(K^*f)_i+kb_i(rp_A-f_i),
\tag{11}
$$

where $K^*$ is the stationary time-reversed generator (here $K^*=K$). At any boundary $f_i=2$, the first term is nonpositive and $rp_A\le2$. At $p_A=1/2$, the field-zero derivative is $k(1-2p_A)=0$. At field $H$, the density bound gives

$$
p_A'=k\sum_i b_i p_i-4kp_A\sum_i\mu_i b_i
\le2k\sum_i\mu_i b_i-2k\sum_i\mu_i b_i=0.
$$

This proves the invariant box by the inward-pointing boundary criterion, also across switches. Averaging under $\Theta$ preserves it.

Write $d(h)=(b_3(h)-b_4(h))/2$. The perturbation has nonzero off-diagonal entries only on the two hub–probe edges. Since $\mu_3=\mu_4=1/12$ and $r\le4$, its maximum full-row total variation is $k|d(h)|$. On $\{0,H\}$,

$$
\eta=\frac{k}{32}.
\tag{12}
$$

For an even law, $p_eV$ is supported only at $p_3,p_4$, with opposite coefficients of magnitude

$$
k|d|\,|r\mu_3p_A-p_{e,3}|
=k|d|\mu_3|rp_A-f_{e,3}|
\le\frac{\eta}{6}.
\tag{13}
$$

Both quantities inside the last difference lie in $[0,2]$ by (10); one does not sum their upper bounds.

### Faster decay on the odd subspace

An odd row has zero coordinate at $A$ and zero total mass in each hidden block. Since $\bar b$ is even, its evolution under $\bar Q$ remains hidden, and its block refresh term is $-k$ times that row. The remaining hidden evolution is generated by the substochastic matrix $K^0-k\bar B$. All return barriers on the two fields are at least $3/8$. Therefore odd rows contract in total variation at rate

$$
\lambda=k+\frac{3k}{8}=\frac{11k}{8},\qquad
\|p_o(t)\|_{\rm TV}\le\frac{\eta}{6\lambda}.
\tag{14}
$$

This bound uses positivity and killing of the incidence walk, not a spectral norm comparison.

### Full-law contraction of the averaged generator

For a finite generator $Q$, define

$$
\gamma(Q)=\min_{x\ne y}\left[q_{xy}+q_{yx}
+\sum_{z\notin\{x,y\}}\min(q_{xz},q_{yz})\right].
\tag{15}
$$

The two rows of $I+dt\,Q$ have total-variation distance at most $1-dt\,\gamma(Q)$ for small positive $dt$. Decomposing a zero-mass row into its positive and negative parts, then taking products and a limit, proves $\|v e^{tQ}\|_{\rm TV}\le e^{-\gamma(Q)t}\|v\|_{\rm TV}$. This also proves contraction for switched propagators using the minimum coefficient of the allowed generators.

The following table gives the exact minimum in each class of unordered row pairs for $\bar Q/k$. It follows directly from (1)–(3); the accompanying verifier evaluates every one of the 66 pairs at each field using rational arithmetic.

| Pair class | Number | At $0$ | At $H$ |
|---|---:|---:|---:|
| $A$, memory | 6 | $41/24$ | $37/24$ |
| $A$, probe | 5 | $5/3$ | $57/32$ |
| Two memories | 15 | $2$ | $11/8$ |
| Incident memory–probe | 12 | $7/3$ | $41/24$ |
| Nonincident memory–probe | 18 | $7/4$ | $9/8$ |
| Two probes | 10 | $2$ | $23/16$ |

Hence the full averaged propagation contracts zero-mass rows at

$$
\gamma=\frac{9k}{8}.
\tag{16}
$$

## 3. Uniform two-field error bound

Apply variation of constants to the even-error equation in (7), using (9), (14), and (16). For every horizon $T$ and every two-field protocol,

$$
\|p_e(T)-\bar p(T)\|_{\rm TV}
\le\int_0^T e^{-\gamma(T-t)}2\eta\|p_o(t)\|_{\rm TV}\,dt
\le\frac{\eta^2}{3\gamma\lambda}.
\tag{17}
$$

A binary readout has mean difference at most twice total variation. Substituting $\eta=k/32$, $\gamma=9k/8$, and $\lambda=11k/8$ gives

$$
\boxed{
\sup_{T\ge0}\sup_{h(\cdot)\in\{0,H\}}
|m_T(h)-m_{\rm quotient}(h)|
\le\frac{2\eta^2}{3\gamma\lambda}
=\frac1{2376}<0.000421.
}
\tag{18}
$$

Piecewise-constant protocols follow directly; bounded measurable two-valued protocols follow by approximation of the finite-dimensional time-dependent evolution. The estimate includes every word on the original clock and arbitrarily long words. The nine-state predictor is fixed once, not refitted for individual protocols.

## 4. A broader all-field upper with averaged barrier curves

Retain the arithmetic curves (3) and allow every field $|h|\le H$. The stronger box (10) is not asserted: instead $f_i\le4$ follows from (11), since $rp_A\le4$. Equation (13) then becomes $\|p_eV\|_{\rm TV}\le\eta/3$.

For $u=h/H\in[-1,0]$, the difference $\beta_3^u-\beta_4^u$ is largest at $u=-1$, giving half-difference $4/45$. For $0\le u\le1$, the mean value theorem gives

$$
\frac{|\beta_4^u-\beta_3^u|}{2}
\le\frac{\beta_4-\beta_3}{2\beta_3}
=\frac1{18}<\frac4{45}.
$$

Thus $\eta=4k/45$ suffices on the whole interval. Every return barrier is at least $3/8$, giving a common reset contraction $\alpha=3k/8$ and the same odd contraction $\lambda=11k/8$. Repeating (17) yields

$$
\boxed{
\sup_{T\ge0}\sup_{|h(\cdot)|\le H}
|m_T(h)-m_{\rm quotient}(h)|
\le\frac{4\eta^2}{3\alpha\lambda}
=\frac{4096}{200475}<0.02044.
}
\tag{19}
$$

This is an upper for the broader kinetic class: the averaged curve (3) is generally not one exponential sensitivity over the entire interval. The exponential endpoint implementation from Section 1 supports (18), not the all-field claim (19).

## 5. Interpretation and verification boundary

Equations (18)–(19) certify sufficient approximation tolerances for one explicit nine-state ordinary reversible predictor. They do not give a lower bound on its own error, prove that nine states are necessary, or locate the best error achievable with eleven states. In particular, the small positive lower tolerance in the finite advantage theorem and this upper tolerance leave a wide unresolved interval. The cancellation mechanism shows why a first-order rate-perturbation bound can substantially overestimate the distinguishability of this target.

The companion [verifier](../scripts/verify_symmetric_compression.py) and [report](../reports/symmetric_compression.json) check the exact target and quotient generators, ordinary detailed balance, caps, symmetry and intertwining identities, the complete rational contraction table, source constants, and bounded switched-propagator diagnostics. Numerical trajectories are checks of implementation, not a substitute for the all-protocol estimates above. No optimization over rival models or large-state simulation is performed.
