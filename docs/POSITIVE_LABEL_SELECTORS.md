# Positive selectors for a finite target alphabet from two physical fields

[Fixed-clock physical resolvents](FIXED_CLOCK_GRAM_OBSERVABILITY.md) · [Positive resolvent calculus](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md) · [Tight-band fixed-clock theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md) · [Original nineteen-level target](DYNAMIC_LAMP_REVERSIBILITY_LOWER_BOUND.md)

**Research lemma, 23 September 2026.** Two natural physical resolvents supply positive approximate selectors for every label in a fixed finite target alphabet. The selectors remain entrywise nonnegative on reversible rivals whose actuator values lie anywhere in the same bounded interval. A rival need not retain the target alphabet or histogram. The construction uses positive powers of two complementary bounded features; no hidden inverse, artificial killing or extra target states are needed.

Only the target has a generator cap. Exact selector kernels are used for positivity and entropy; signed observable expansions recover their scalar values from actual means.

## 1. Model and two positive soft features

Set the external time scale $k=1$. Fix $G,H>0$, a finite target alphabet $\Gamma\subset[-G,G]$ of at least two distinct values, and the two physical fields $0$ and $h_*=H$. The hidden generator $K$ is reversible with stationary law $\mu$, and the original external field rule, preparation and readout are retained. Rivals may have arbitrary finite state spaces, rates and stationary masses, and arbitrary sensitivities $g\in[-G,G]$. Exact centering or histogram matching is not used in this lemma.

Let

$$
b_- =e^{(-G-1)H},\qquad b_+=e^{(G-1)H},\qquad
\Delta_b=b_+-b_->0,
$$

$$
B_H=\operatorname{diag}(e^{(g-1)H}),\qquad
X=\frac{B_H-b_-I}{\Delta_b},\qquad Y=I-X.
\tag{1}
$$

These are bounded diagonal features with $0\le X,Y\le I$ in every rival, including rivals with labels outside the target alphabet. For $s>0$, define natural killed resolvents

$$
G_0(s)=(sI-K+I)^{-1},\qquad
G_H(s)=(sI-K+B_H)^{-1},\qquad
\mathcal Z_h(s)=sG_h(s).
\tag{2}
$$

The [physical Schur-complement identity](FIXED_CLOCK_POSITIVE_RESOLVENT_CALCULUS.md#1-full-and-hidden-resolvents) recovers $\mathcal Z_h$ from the normalized full physical resolvent and the visible projector. It uses only the specified preparation and readout.

Set

$$
F_+(s)=\frac{s^2}{2}\bigl(G_0XG_H+G_HXG_0\bigr),\qquad
F_-(s)=\frac{s^2}{2}\bigl(G_0YG_H+G_HYG_0\bigr).
\tag{3}
$$

Every factor in each summand is entrywise nonnegative. Both $F_\pm$ are selfadjoint contractions in $L^2(\mu)$, since $\|sG_0\|,\|sG_H\|\le1$ and $\|X\|,\|Y\|\le1$. Selfadjointness and entrywise positivity do not assert positive semidefiniteness of the individual $F_\pm$.

The same resolvent identity as in the binary calculus gives their explicit observable expressions:

$$
\begin{aligned}
F_+&=\frac{s}{\Delta_b}(\mathcal Z_0-\mathcal Z_H)
-\frac{b_--1}{2\Delta_b}
(\mathcal Z_0\mathcal Z_H+\mathcal Z_H\mathcal Z_0),\\
F_-&=\tfrac12(\mathcal Z_0\mathcal Z_H+\mathcal Z_H\mathcal Z_0)-F_+.
\end{aligned}
\tag{4}
$$

Thus each soft feature is a linear combination of natural-resolvent words of length at most two, with coefficient mass at most $C(1+s)$. The coefficients depend only on $G,H,s$, not on the rival's labels, histogram, rates or dimension.

## 2. Target-only approximation to multiplication

Assume the target has $\|K\|\le\Lambda$. Since the normalized resolvents are contractions,

$$
\|sG_0-I\|\le\frac{\Lambda+1}{s},\qquad
\|sG_H-I\|\le\frac{\Lambda+b_+}{s}.
$$

Expanding each product in (3) around its diagonal feature consequently gives

$$
\|F_+-X\|,\ \|F_--Y\|
\le\frac{C_F}{s},\qquad C_F=2\Lambda+1+b_+.
\tag{5}
$$

No such approximation is assumed for a rival. The distinction matters: its exact kernels (3) are positive even if its generator is arbitrarily fast.

The target feature values are the fixed distinct numbers

$$
x_i=\frac{e^{(\gamma_i-1)H}-b_-}{\Delta_b}\in[0,1],
\qquad \gamma_i\in\Gamma.
\tag{6}
$$

Let $D_i$ denote the actual target coordinate projector for $g=\gamma_i$.

## 3. A positive polynomial with a unique target-label maximum

For an interior value $x_i\in(0,1)$, consider

$$
\ell_\theta(x)=\theta\log x+(1-\theta)\log(1-x),\qquad 0<\theta<1.
$$

At $\theta=x_i$, this function has its unique maximum on $(0,1)$ at $x_i$. Therefore it has a strict gap between $x_i$ and every other interior value in the finite target list; its value at endpoints is interpreted as $-\infty$. This strict finite set of inequalities persists for all $\theta$ sufficiently close to $x_i$. Choose positive integers $a_i,b_i$ with $a_i/(a_i+b_i)$ in that neighborhood. Then

$$
\phi_i(x)=x^{2a_i}(1-x)^{2b_i}
\tag{7}
$$

has a unique maximum among target values at $x_i$. Put $w_i=\phi_i(x_i)>0$.

If $x_i=0$, instead set $\phi_i(x)=(1-x)^2$ and $w_i=1$. If $x_i=1$, use $\phi_i(x)=x^2$ and $w_i=1$. These also have unique maxima on the finite target list.

In every case, let

$$
\rho_i=\max_{j\ne i}\frac{\phi_i(x_j)}{w_i}<1,
\qquad
\beta_i=\begin{cases}\min\{1,-\log\rho_i\},&\rho_i>0,\\1,&\rho_i=0.\end{cases}
\tag{8}
$$

All exponents, $w_i$ and $\beta_i$ are fixed constants independent of the target width and of the rival. The maximizing property is required only on the finite target list. The polynomial itself is nonnegative on the entire interval $[0,1]$.

## 4. Exact positive rival selectors and their target error

For an interior label define

$$
T_i(s)=F_+^{a_i}F_-^{2b_i}F_+^{a_i}.
\tag{9}
$$

At the endpoints use $T_i=F_-^2$ or $T_i=F_+^2$, respectively. Every $T_i$ is entrywise nonnegative, selfadjoint and positive semidefinite. For (9), the middle even power is PSD and the two outer factors are stationary adjoints; the endpoint cases are squares. Its operator norm is at most one.

Let $d_i=2a_i+2b_i$ for an interior label and $d_i=2$ at an endpoint. Telescoping products of contractions in the target gives

$$
\|T_i(s)-\phi_i(X)\|\le\frac{d_iC_F}{s}.
\tag{10}
$$

For a width parameter $n\ge1$, write $q=n+1$ and choose

$$
m_i=\left\lceil\frac{120q}{\beta_i}\right\rceil,
\qquad s=e^{200q},\qquad
A_i(s,n)=\left(\frac{T_i(s)}{w_i}\right)^{m_i}.
\tag{11}
$$

These are exact positive, selfadjoint rival kernels. They are not assumed to be coordinate projectors in a rival. Their universal norm bound is

$$
\|A_i\|\le w_i^{-m_i}\le e^{C_iq}.
\tag{12}
$$

On the target, $V_i=\phi_i(X)/w_i$ has norm one and satisfies
$\|V_i^{m_i}-D_i\|\le\rho_i^{m_i}\le e^{-120q}$. Put $c_i=d_iC_F/w_i$. Equation (10), followed by a second telescoping estimate, gives the explicit bound

$$
\boxed{
\|A_i-D_i\|
\le e^{-120q}+\frac{m_ic_i}{s}\left(1+\frac{c_i}{s}\right)^{m_i-1}.}
\tag{13}
$$

Since $m_i=O(q)$ and there are finitely many labels, (11) makes

$$
\max_i\|A_i-D_i\|\le e^{-110q}
\tag{14}
$$

for all sufficiently large $n$. The starting index may depend on the fixed alphabet, field, bound and target cap. In particular, extremely small label separation only changes fixed constants and this index.

Each $A_i$ has $O(q)$ soft-feature factors, a scalar normalization with logarithm $O(q)$, and an observable expansion in natural-resolvent words of length $O(q)$ and coefficient mass at most $e^{Cq^2}$. The latter bound follows directly from (4): $\log s=200q$ and there are $O(q)$ factors. No polynomial approximates an unbounded rival generator.

## 5. Original nineteen-level transports without extra target states

Apply the construction to the original nineteen-level target with $G=9/100$ and $\Lambda=3$. For a paired logical port $c$, let

$$
A_c=A_{+\gamma_c}+A_{-\gamma_c}.
$$

For the central signed probe use $(A_{+\gamma_0}-A_{-\gamma_0})1$. Positivity gives its absolute value at most $A_01$ in every rival. The hub's zero-sensitivity selector is available but is not used as a logical port.

Set

$$
t=e^{20q},\qquad
P_t=t(tI-K)^{-1}=\frac{t}{t-1}\mathcal Z_0(t-1),
\qquad
\mathsf T_{cd}=8t A_cP_t^2A_d
\tag{15}
$$

for distinct adjacent logical ports. Every factor is positive in every rival, $P_t$ is a reversible Markov kernel, and
$\mathsf T_{dc}=\mathsf T_{cd}^*$. The parameter $t>1$ makes (15) an exact expression in a natural zero-field resolvent.

On the target, the original cross-port approximation and (14) give

$$
\|8tD_cP_t^2D_d-16D_cKD_d\|\le216/t,
$$

$$
\left\|\mathsf T_{cd}-16D_cKD_d\right\|
\le216/t+Ct e^{-110q}
\le C'e^{-20q}.
\tag{16}
$$

The ideal transport is the existing logical permutation between paired ports. Their target masses are exactly $1/18$. No target label, mass, edge, state or rate was changed. In a rival the positive weighting uses its own vector $A_01$, as in [weighted whole-word repair](WEIGHTED_WHOLE_WORD_REPAIR.md); it need not possess port sets or port masses.

## 6. Observation budgets for the fixed-clock application

An entropy scalar contains $O(q)$ cross-port transports and endpoint selectors. Equations (11) and (15) therefore yield the following fixed-constant bounds before physical Schur expansion:

| Quantity | Bound |
|---|---:|
| Soft-feature factors | $Cq^2$ |
| Natural-resolvent word length after expansion | $Cq^2$ |
| Logarithm of total observable coefficient mass | $Cq^3$ |
| Smallest natural Laplace parameter | $t-1=e^{20q}-1$ |

The factors $t/(t-1)$ are bounded by two. The only large factors are explicit scalar normalizations; their products also lie within the coefficient bound shown.

Apply the natural-resolvent Schur formula at fields $0,H$. Since every parameter grows exponentially with $q$, the normalized visible-return denominator is at least $1/2$ for sufficiently large $n$, uniformly over all rivals with $|g|\le G$. Each natural factor adds a fixed number of physical-resolvent/projector factors; expanding the hidden projector and the denominator products changes neither the $O(q^2)$ length nor the $O(q^3)$ logarithmic coefficient and denominator-Lipschitz bounds.

The [fixed-clock Gram estimate](FIXED_CLOCK_GRAM_OBSERVABILITY.md#6-finite-words-true-prefixes-and-polynomial-suffixes) can consequently use fractional-power degree $M=C_Mq^3$ and integer-time cutoff zero. The target-filter tail is geometric in $M$. The integer tail is at most $\exp[-a(e^{20q}-1)]$, which beats the full coefficient budget for sufficiently large $n$. The measurement exponent is $O(q^2M)=O(q^5)$, and every required physical word has $O(q^5)$ clock ticks.

The full entropy allocation and state-count consequence are stated separately in the [tight-band fixed-clock theorem](TIGHT_BAND_FIXED_CLOCK_REVERSIBILITY.md). The present lemma supplies the positive selectors and all costs introduced by replacing literal label projectors.

## 7. Scope of the construction

The finite alphabet belongs to the target. A rival only needs a bounded sensitivity interval and the original rule; it need not match the target histogram or use any target label. The two-field observation construction does not identify an individual rival coordinate or claim an exact projector there.

For the original nineteen-level family, the target band remains $[k,3k]$ after restoring physical units. The positive selectors and their exact observable definitions avoid rare tags, artificial killing, hidden inverses and modifications of the target graph. This lemma does not itself assert a polynomial unrestricted lower on a two-field menu; that rank comparison has its own experiment menu in the full theorem.
