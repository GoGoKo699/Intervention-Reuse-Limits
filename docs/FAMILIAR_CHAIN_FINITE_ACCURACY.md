# Distant switches disappear at fixed endpoint accuracy

[Assessment](FAMILIAR_CHAIN_SHARPNESS.md) · [Exact reversible upper](FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md)

The exact state minima grow with chain length, but the influence of distant
switches on the measured endpoint decreases exponentially. This note proves
a uniform approximation bound, including arbitrary control words and
arbitrarily long observation times. It is a boundary on the interpretation
of the exact theorem, not a lower bound on approximation cost.

## Statement

Use the homogeneous equal-attempt heat-bath chain, with
$0<t=\tanh J<1$. Let $P_{n,w}$ be the joint law of the initial and final
visible signs, from zero-field equilibrium, after a finite boundary-field
word $w$. Truncate the chain to its first $\ell$ spins, with the ordinary
free terminal boundary, where $2\le\ell<n$. Use its own zero-field
equilibrium and the same fields and dwell times. Then

$$
\sup_w\operatorname{TV}(P_{n,w},P_{\ell,w})
\le\frac{t^{2\ell}}{1-t^4}.
\tag{1}
$$

The supremum includes arbitrary finite fields of either sign, arbitrary
word lengths, and arbitrary total horizons. It concerns endpoint pairs.
It does not assert approximation of complete visible paths.

## Proof

Condition on the initial visible sign $s=\pm1$. The initial spin mean at
site $j$ is $s t^j$ in either chain. At every later time the full chain's
conditional hidden means satisfy

$$
|x_j|\le t^j,\qquad j\ge1.
\tag{2}
$$

Indeed, $|x_0|\le1$ because the observed spin is binary. With
$c=t/(1+t^2)$, the hidden mean equations are cooperative, and

$$
c(t^{j-1}+t^{j+1})=t^j,\qquad
t\,t^{n-2}=t^{n-1}.
$$

Thus the box (2) is invariant under the interior and terminal equations.
This uses no bound on the boundary field and remains true across switches.

Let $d$ be the difference between the first $\ell$ means of the full chain
and the means of the truncated chain. Its initial value is zero. Write
$L_{\ell,m}$ for the truncated chain's mean drift matrix, with diagonal
$-1$, first off-diagonal
$B_m=t(1-m^2)/(1-t^2m^2)$, interior off-diagonals $c$, and terminal
off-diagonal $t$. The only discrepancy in the retained equations is

$$
\dot d=L_{\ell,m}d+e_{\ell-1}f,\qquad
f=c(x_\ell-t^2x_{\ell-2}),\qquad |f|\le2ct^\ell.
\tag{3}
$$

Every $L_{\ell,m}$ is Metzler and is bounded entrywise by $L_{\ell,0}$,
since $0\le B_m\le t$. The passive matrix is stable: its endpoint row
sums are $-1+t<0$ and its interior row sums are $-1+2c<0$.
Cooperative comparison and integration to infinite time therefore give

$$
|d_0(T)|\le2ct^\ell
\bigl[(-L_{\ell,0})^{-1}\bigr]_{0,\ell-1}.
\tag{4}
$$

The required Green-function entry is

$$
\bigl[(-L_{\ell,0})^{-1}\bigr]_{0,\ell-1}
=\frac{t^{\ell-1}}{1-t^2}.
\tag{5}
$$

For $\ell\ge3$, solve $(-L_{\ell,0})y=e_{\ell-1}$. The interior
recurrence has roots $t$ and $t^{-1}$. The left equation $y_0=t y_1$
removes the $t^j$ component; the right equation
$y_{\ell-1}-t y_{\ell-2}=1$ fixes (5). For $\ell=2$, direct inversion
of the matrix with diagonal $1$ and off-diagonals $-t$ gives the same
formula.

Equations (3)–(5) show, for either initial sign,

$$
|d_0(T)|\le\frac{2t^{2\ell}}{1-t^4}.
$$

For binary final outputs, conditional TV is half the mean difference.
The initial signs have the same balanced law, so averaging the two
conditional bounds proves (1).

## Consequences for state cost

At every coupling $t\le1/64$ covered by the new exact upper, the physical
two-spin chain has four reversible states and satisfies

$$
\sup_w\operatorname{TV}(P_{n,w},P_{2,w})
\le\frac1{64^4-1}
=\frac1{16777215}<6\times10^{-8}.
\tag{6}
$$

It retains one equilibrium preparation, the deterministic visible sign,
and the same Gibbs force interface. Thus a lower bound proportional to
$n$ cannot hold at this fixed accuracy for these endpoint observations.
For comparison, the sufficient two-spin truncation bound at $t=1/3$ is
$1/80$; it does not erase the stronger-coupling exact four-versus-six
result or determine its optimal approximation error.

More generally, fix $t\le1/64$, a desired error $\delta>0$, and
$\ell\ge3$ such that $t^{2\ell}/(1-t^4)\le\delta$. For a target of
length $n\ge3$, set $k=\min(n,\ell)$. The
[reversible realization](FAMILIAR_CHAIN_REVERSIBLE_REALIZATION.md) of
the $k$-spin chain uses $2k\le2\ell$ states. It is exact when $k=n$
and obeys (1) otherwise, for all fields $|m|\le1/2$. For nonnegative
fields, the [general positive model](FAMILIAR_CHAIN_POSITIVE_REALIZATION.md)
uses $k+1\le\ell+1$ states with the same error guarantee.

These sufficient bounds are independent of the original length $n$ and
grow at most logarithmically with $1/\delta$ for fixed $t$. They are not
matched accuracy-dependent lower bounds. More sharply, take $\ell=n-1$:
for $n\ge4$, the shortened chain has a reversible $2n-2$-state predictor;
for $n=3$, its physical four states suffice. Thus the best possible error
threshold excluding every model with fewer than $2n$ reversible states
is at most

$$
\frac{t^{2n-2}}{1-t^4}.
\tag{7}
$$

This applies even to all endpoint words, and hence to any finite menu.
The tolerance for certifying the exact $2n$ count must therefore decrease
at least exponentially with $n$ at fixed $t$ in this coupling range.
The exact $n+1$ versus $2n$
comparison remains a structural obstruction to lossless equilibrium
reduction; its physical significance at finite precision needs a separate
quantitative separation.
