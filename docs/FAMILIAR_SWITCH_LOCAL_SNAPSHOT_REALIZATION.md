# Local three-state realization of the two snapshot laws

This construction adapts the general three-state predictor to changes in
the four measured moments. It does not require closure of the physical
generator on the two coordinates. The model reproduces the two initial
and final binary joint laws at their specified clock times. No equality
of complete visible trajectories or of other control words is asserted.

For every independent edge-prefactor perturbation in the $1\%$ box of
the [direct kinetic proof](FAMILIAR_SWITCH_PERCENT_KINETIC_ROBUSTNESS.md),
the construction gives a genuine three-state continuous-time Markov
model matching those two latent joint laws exactly. This statement
includes kinetic perturbations that break the original affine closure.

The four-state target has a balanced low-field stationary law, and its
high-field stationary law is the Gibbs tilt by the observed coordinate,
with $u=3/5$. Preparation, measurement, field, and timing departures are
accounted for separately in the physical error budget.

## 1. A fixed three-state coordinate system

Use the same states and reference law as the positive charge predictor:

$$
 S=(-1,1,1)^T,\qquad
 Z=(-4/5,-8/5,26/25)^T,\qquad
 \pi=(1/2,1/22,5/11).
$$

Set $t=4/5$ and $W=Z-tS=(0,-12/5,6/25)^T$. Then

$$
 \pi S=\pi W=\pi SW=0,\qquad \pi S^2=1.
$$

The vectors $\mathbf1,S,W$ are a basis. Write their matrix as $F$, so

$$
 F^{-1}=
 \begin{pmatrix}
 1/2&1/22&5/11\\
 -1/2&1/22&5/11\\
 0&-25/66&25/66
 \end{pmatrix}.
$$

The high-field stationary law is fixed as
$\pi_H=\pi(1+uS)$. It has coordinate means $(1,u,0)$.

Let $K_0^*,K_H^*$ be the inherited positive three-state heat-bath
predictor kernels at fields $0,\log2$ and dwell time $\tau=5/4$.
Their matrices in this basis have the forms

$$
 B_0^*=F^{-1}K_0^*F=
 \begin{pmatrix}1&0&0\\0&x_*&z\\0&y&w\end{pmatrix},
 \qquad
 B_H^*=F^{-1}K_H^*F=
 \begin{pmatrix}1&u(1-a_*)&-u c_*\\0&a_*&c_*\\0&b_*&d\end{pmatrix}.
 \tag{1}
$$

In particular,

$$
 y=e^{-5/4}\sinh 1>0,\qquad z=\frac9{25}y>0,
$$

$$
 x_*=e^{-5/4}(\cosh1+\tfrac45\sinh1),\qquad
 w=e^{-5/4}(\cosh1-\tfrac45\sinh1).
 \tag{2}
$$

The constants $y,z,w,d$ are held fixed throughout the construction.

## 2. An explicit fit with four parameters

For the two chronological words $0H,H0$, let the target latent moments be

$$
 (m,C,\ell,D)
 =\bigl(\mathbb E[Y],\mathbb E[IY],
        \mathbb E[Z_{\rm out}],\mathbb E[JZ_{\rm out}]\bigr).
$$

Both initial means are zero. Here $Z_{\rm out}$ names the final binary
record in the second word; it is distinct from the auxiliary coordinate
$Z$ above. Define

$$
 x=\frac{\ell+uD}{u},\qquad a=1-\frac m u,\qquad
 b=\frac{C-ax}{z},\qquad c=\frac{D-ax}{y}.
 \tag{3}
$$

Use

$$
 B_0=\begin{pmatrix}1&0&0\\0&x&z\\0&y&w\end{pmatrix},
 \qquad
 B_H=\begin{pmatrix}1&u(1-a)&-uc\\0&a&c\\0&b&d\end{pmatrix},
 \qquad K_h=FB_hF^{-1}.
 \tag{4}
$$

These formulas define a fixed shared model: the same initial law $\pi$,
the same binary readout $S$, and the same pair of kernels are used in
both words. Row sums are one because both matrices fix $\mathbf1$.
Moreover $\pi K_0=\pi$ and $\pi_HK_H=\pi_H$: the coordinate means
$(1,0,0)$ and $(1,u,0)$ are invariant under their respective matrices.
Because the coordinate vectors form a basis, these are full stationarity
identities.

The moment identities are elementary:

$$
 \pi K_HS=u(1-a)=m,
 \qquad \pi S K_0K_HS=ax+bz=C,
$$

$$
 \pi S K_HK_0S=ax+yc=D,
 \qquad \pi K_HK_0S=u(x-D)=\ell.
 \tag{5}
$$

Here $\pi S$ denotes the row whose entries are $\pi_iS_i$.
Thus, whenever the two matrices in (4) are nonnegative, they reproduce
both full joint laws. Indeed a binary pair with zero initial mean has
probabilities $[1+j m+ij C]/4$ for the first word and
$[1+j\ell+ijD]/4$ for the second, where $i,j\in\{-1,1\}$.
Applying the same electronic readout channels preserves equality.

The fit uses four independently adjustable parameters. Freezing the
entire low-field kernel would not suffice: stationarity forces
$\ell+uD=u\pi S K_0S$, fixing one combination of target moments.
In (4), varying $x$ is exactly the rank-one update
$K_0=K_0^*+(x-x_*)S(\pi S)$.

## 3. Positivity and continuous-time embedding

All entries of the two matrices in (4) are affine functions of
$(x,a,b,c)$. Their positivity on a rectangular parameter domain therefore
reduces to finitely many affine endpoint inequalities. Positivity alone
would establish a stationary stochastic-kernel realization at the stated
clock times; it does not by itself imply continuous-time embeddability.

For the stronger continuous-time statement, let either $K_h$ have
stationary law $p$, and let its two other eigenvalues satisfy
$0<\lambda_-<\lambda_+<1$. Set $\Pi=\mathbf1p$ and

$$
 \alpha=\frac{\log\lambda_+-\log\lambda_-}
              {\lambda_+-\lambda_-}>0,\qquad
 \beta=\log\lambda_--\alpha\lambda_-.
$$

The principal logarithm is

$$
 \log K_h=\alpha K_h+\beta I-(\alpha+\beta)\Pi.
 \tag{6}
$$

This follows by evaluating both sides on the three distinct eigenspaces.
In particular, $\log K_h$ has zero row sums and stationary law $p$.
Its off-diagonal entries are nonnegative exactly when

$$
 \frac{(K_h)_{ij}}{p_j}\ge q,
 \qquad q=1+\frac\beta\alpha,
 \qquad i\ne j.
 \tag{7}
$$

Consequently, strict versions of these inequalities produce a genuine
three-state CTMC generator $Q_h=\tau^{-1}\log K_h$ with
$e^{\tau Q_h}=K_h$. The generator need not satisfy ordinary detailed
balance, as permitted in the general predictive comparison class.

The relevant eigenvalues come from the lower $2\times2$ blocks in (4).
Thus the embedding test requires only scalar square roots, logarithms,
and the six inequalities (7); no numerical matrix logarithm is needed.

### A rational domain containing the entire rate box

The direct kinetic proof bounds the fitted parameter displacements by

$$
 |x-x_*|<0.002021,\quad |a-a_*|<0.002468,\quad
 |b-b_*|<0.007022,\quad |c-c_*|<0.003647.
 \tag{8}
$$

Together with certified nominal constants, these bounds put both blocks
inside the following rational domains. The constants frozen in (1) are
allowed to range over enclosing intervals here only to simplify the
domain certificate.

| Low block | Interval | High block | Interval |
| --- | --- | --- | --- |
| $x$ | $[0.706,0.717]$ | $a$ | $[0.627,0.638]$ |
| $y$ | $[0.3366,0.3368]$ | $b$ | $[0.260,0.285]$ |
| $z$ | $[0.1211,0.1213]$ | $c$ | $[0.146,0.161]$ |
| $w$ | $[0.1726,0.1729]$ | $d$ | $[0.1959,0.1961]$ |

Every entry of $FB_hF^{-1}$ is positive throughout its domain. For
example, the smallest lower bounds among all nine entries are
$322613/16500000>0.0195$ for the low block and $191/5000=0.0382$ for
the high block. The six lower bounds on the ratios in (7) are

| Entry $ij$ | Low-field ratio lower bound | High-field ratio lower bound |
| --- | --- | --- |
| $12$ | $7753/6000$ | $592/375$ |
| $13$ | $2183/12000$ | $1367/6000$ |
| $21$ | $27271/25000$ | $961/500$ |
| $23$ | $195839/300000$ | $12349/24000$ |
| $31$ | $25271/125000$ | $191/1000$ |
| $32$ | $322613/750000$ | $2953/4800$ |

These bounds follow by taking the endpoint of each affine coefficient
in the explicit matrices (4), rather than sampling interior points.
In particular, the ratios exceed $0.181$ at low field and are at least
$0.191$ at high field.

For a positive $2\times2$ block with diagonal entries $A,D$ and
off-diagonal entries $B,C$, write
$p(r)=(r-A)(r-D)-BC$. The domain bounds give

| Block | Lower bound on $p(r_-)$ | Upper bound on $p(r_+)$ | Lower bound on $p(1)$ |
| --- | --- | --- | --- |
| Low: $r_-=0.1,r_+=0.77$ | $4909/1562500>0$ | $-126433/50000000<0$ | $9660773/50000000>0$ |
| High: $r_-=0.107,r_+=0.7$ | $343/1000000>0$ | $-11607/10000000<0$ | $612817/2500000>0$ |

Since $B,C>0$, the two roots are real and distinct. In both domains
$r_-$ is below both diagonal entries, and $1$ is above both. These
signs prove

$$
 0.1<\lambda_-<\lambda_+<1,\quad \lambda_+>0.77
 \quad\text{at low field},
$$

$$
 0.107<\lambda_-<\lambda_+<1,\quad \lambda_+>0.7
 \quad\text{at high field}.
 \tag{9}
$$

Put

$$
 \kappa(l,h)=-\frac\beta\alpha
 =\frac{l\log h-h\log l}{\log h-\log l}.
$$

It is increasing in each argument for $0<l<h<1$. For example,

$$
 \frac{\partial\kappa}{\partial l}
 =\frac{-\log h\,[h/l-1-\log(h/l)]}
         {[\log(h/l)]^2}>0;
$$

the other derivative follows by interchanging the two arguments.
Certified scalar logarithm bounds give

$$
 \kappa(0.1,0.77)>0.855,\qquad
 \kappa(0.107,0.7)>0.812.
 \tag{10}
$$

Therefore $q=1-\kappa<0.145$ at low field and $q<0.188$ at high field.
Both are strictly below all six corresponding entry-ratio lower bounds.
Equations (6)–(7) now prove that both principal logarithms have strictly
positive off-diagonal entries. Thus every fitted kernel pair in the
entire $1\%$ physical rate box admits the common prescribed dwell time
$\tau=5/4$ with valid three-state generators and the stated stationary
laws.

## 4. Scope of the construction

This is a local realization theorem for two prescribed snapshot laws.
The construction adjusts one fixed predictor to the target's actual
moment tuple, rather than requiring one universal predictor for all
possible rate errors at once. The minimization over predictive models
allows that dependence. The predictor's hidden states are abstract
predictive states; the binary output and the stationary Gibbs tilt are
the preserved physical interface.

The balanced stationary moments in (3) refer to the ideal nominal fields
with deformed edge rates. Actual preparation, field and timing errors,
and a protected-readout defect are handled by the stated total-variation
allowance, not by claiming that (3) exactly fits a biased preparation.
Nor does matching these four moments establish any extra trajectory,
multi-time measurement, or arbitrary-duration claim.
