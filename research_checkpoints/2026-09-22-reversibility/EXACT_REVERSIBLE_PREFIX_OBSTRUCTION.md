# A fixed fifteen-symbol obstruction to exact reversible realization

[Checkpoint](README.md) · [Source comparison](PRIOR_ART_COMPARISON.md)

**Archival status.** This note reconstructs the internally audited argument from recovered research context. It is not asserted to be byte-identical to the inaccessible workspace document. No executable verification was run during reconstruction.

## 1. Statement and scope

For every integer $N\ge3$, there is an irreducible, ordinarily reversible Markov chain with $3N+2$ states and a deterministic observation map into five colors such that every color has stationary probability $1/5$, the generator $K=k(P-I)$ has all nonzero relaxation rates in $[k/8,k]$, and every finite ordinarily reversible chain matching the stationary observation probabilities through fifteen observed symbols has at least $N$ states of one specified color.

A rival may use entirely new states, need not be an aggregation, and need not be irreducible, lazy or rate bounded. Its observations must be deterministic state colors and its transition matrix must satisfy ordinary detailed balance with its stationary law.

Thus no bound depending only on alphabet size and prefix length can bound exact reversible realization dimension for these laws. This is an exact realization theorem. It does not give a positive-error state lower, a controlled-mean lower, or a reversible-versus-unrestricted approximation gap.

## 2. A five-color target

Addresses are modulo $N$. Set $\theta=2\pi/N$, $S(a)=-a$, and $T(a)=1-a$; both address maps are involutions.

The state set consists of three ports $(j,a)$ for $j=0,1,2$, $a\in\mathbb Z_N$, and two further states $r_+,r_-$. Their five colors are $0,1,2,+,-$. Set

$$
\pi(j,a)=\frac1{5N},\qquad
\pi(r_+)=\pi(r_-)=\frac15.
$$

Every address state has a self-loop of probability $1/2$. The following port matching edges have transition probability $1/8$ in each direction:

$$
(0,a)\longleftrightarrow(1,S(a)),\qquad
(1,a)\longleftrightarrow(2,T(a)),\qquad
(2,a)\longleftrightarrow(0,a).
$$

For each port $j$ set

$$
P((j,a),r_\pm)=\frac{1\pm\frac12\cos(\theta a)}8,\qquad
P(r_\pm,(j,a))=\frac{1\pm\frac12\cos(\theta a)}{8N},
$$

and $P(r_\pm,r_\pm)=5/8$. All other entries are zero.

Each address row sums to $1/2+1/8+1/8+1/4=1$. Since
$\sum_a\cos(\theta a)=0$, each additional-state row has outgoing mass $3/8$ besides its self-loop. Detailed balance holds edge by edge. Each address-to-$r_\pm$ probability is at least $1/16$, so the chain is irreducible.

The labels $+$ and $-$ name observation colors. They are not the binary visible readout of a separately attached physical model.

## 3. Spectral band

Every diagonal entry of $P$ is at least $1/2$, so $P=(I+R)/2$ for a reversible stochastic $R$. Thus the spectrum of $P$ lies in $[0,1]$, proving the upper relaxation cap $k$.

For a lower comparison, let $L_\star$ have only rates

$$
L_\star((j,a),r_\pm)=1/8,\qquad
L_\star(r_\pm,(j,a))=1/(8N),
$$

and diagonal entries making row sums zero. It is reversible with the same law. Its relaxation eigenvalues are $0,1/4,3/8,5/8$: address zero-mean modes have rate $1/4$, the $r_+$/$r_-$ contrast rate $3/8$, and the address/additional-state contrast rate $5/8$.

Every comparison conductance is at most twice its counterpart in $P-I$. Port matchings only add Dirichlet energy. Therefore

$$
-\langle u,(P-I)u\rangle_\pi
\ge\frac12[-\langle u,L_\star u\rangle_\pi].
$$

The gap is at least $1/8$, proving the band $[k/8,k]$ uniformly in $N$.

## 4. Inner products from stationary prefixes

Let $D_c$ be the color indicator projection. The probability of a word with $m+1$ symbols is

$$
p(c_0,\ldots,c_m)
=\pi D_{c_0}P D_{c_1}\cdots P D_{c_m}\mathbf1.
$$

Agreement of all fifteen-symbol probabilities implies agreement of every shorter prefix by marginalization.

For a word $w=(c_0,\ldots,c_m)$ let
$F_w=D_{c_0}P D_{c_1}\cdots P D_{c_m}\mathbf1$.
Reversibility makes $P$ self-adjoint in $L^2(\pi)$; the $D_c$ are also self-adjoint. Inner products of two such functions are obtained by reversing the first word and concatenating it with the second. If the initial colors agree, the central projections merge. Thus functions with at most $m$ and $\ell$ transitions have inner products determined by at most $m+\ell+1$ observed symbols; if initial colors differ the inner product is zero.

By linearity, squared norms of linear combinations of prefix functions are determined in the same way.

## 5. Exact data force positive stochastic transports

For distinct address ports define
$U_{cd}=8D_cPD_d$, as a rectangular kernel from port $c$ to port $d$. In the target it is the matching transport. The observation law has

$$
p(c,d)=\frac1{40},\qquad p(d,c,d)=\frac1{320}.
$$

In a reversible rival discard zero-stationary-mass states. They are not reached from the positive stationary support, so this leaves a closed support and does not increase the state count. Denote rival quantities by hats, and its stationary conditional law on color $c$ by $\hat\mu_c$.

For a color-$c$ state let
$R_{cd}(i)=8\sum_{j:\hat c(j)=d}\hat P(i,j)$.
Since each color has mass $1/5$,

$$
\mathbb E_{\hat\mu_c}R_{cd}=40p(c,d)=1.
$$

Reversibility gives
$\|D_c\hat P D_d1\|_{\hat\pi}^2=p(d,c,d)$, so

$$
\mathbb E_{\hat\mu_c}R_{cd}^2=320p(d,c,d)=1.
$$

The row-sum variance is zero. Every retained state has positive stationary mass, hence each row sum equals one exactly. Thus every $\hat U_{cd}$ is nonnegative and row stochastic. Equal color masses and detailed balance also make $\hat U_{dc}$ its conditional stationary adjoint.

These conclusions use at most three observed symbols.

## 6. The observable cycle and recurrence

On port $0$ put

$$
B=U_{02}U_{21}U_{10}=512D_0PD_2PD_1PD_0.
$$

The matchings send $a$ to $a$, then to $T(a)$, then to $S(T(a))=a-1$. Thus $(Bu)(a)=u(a-1)$.

Define

$$
f=16D_0PD_+\mathbf1-2D_0\mathbf1.
$$

The target formula gives $f(0,a)=\cos(\theta a)$, zero off port $0$, and for $N\ge3$,

$$
\|f\|_\pi^2=\frac1{5N}\sum_a\cos^2(\theta a)=\frac1{10}.
$$

Moreover,

$$
(B^2-2\cos\theta\,B+I)f=0,
$$

where $I$ is the identity on port-zero functions.
The feature $f$ uses at most one transition, and $B$ uses three. Thus $B^2f$ uses at most seven transitions. The squared recurrence norm is determined by at most $7+7+1=15$ symbols.

Every rival with the prescribed prefix law therefore satisfies

$$
\|\hat f\|_{\hat\pi}^2=\frac1{10},\qquad
(\hat B^2-2\cos\theta\,\hat B+I)\hat f=0.
$$

The recurrence follows from its zero squared norm and positive stationary masses. Crucially,
$\hat B=\hat U_{02}\hat U_{21}\hat U_{10}$ is stochastic on the rival's actual color-zero states. It need not itself be reversible.

## 7. A primitive root requires $N$ states

Set $\zeta=e^{2\pi i/N}$. Since $\hat f$ is real and nonzero and $\zeta$ is nonreal for $N\ge3$, the vector
$v=(\hat B-\bar\zeta I)\hat f$ is nonzero. Factoring the recurrence shows $\hat Bv=\zeta v$.

For any finite stochastic matrix $A$ and eigenvector $Av=\zeta v$ with $|\zeta|=1$, choose a state where $|v_i|$ is maximal. Equality in

$$
|\zeta v_i|=\left|\sum_jA_{ij}v_j\right|
\le\sum_jA_{ij}|v_j|\le\max_j|v_j|
$$

forces $v_j=\zeta v_i$ on every positive outgoing edge. Every successor also has maximal modulus. Follow positive edges until a state repeats. The resulting cycle has length $\ell$ at most the matrix dimension, and $\zeta^\ell=1$. Since $\zeta$ has order $N$, one has $N\mid\ell$. The dimension is therefore at least $N$.

Apply this to $\hat B$. The rival needs at least $N$ color-zero states, without any rival irreducibility assumption.

## 8. Limitations and attribution

The rival is not given address coordinates, a target partition or prescribed matching. The positive cycle is forced from its own transition matrix and deterministic color projections.

Deterministic colors are essential to the projection argument. An arbitrary stochastic-emission model is a different competitor class. Exactness is also essential: zero row variance, a zero recurrence norm and an exactly peripheral eigenvalue do not automatically survive positive error.

The peripheral-spectrum obstruction is classical Perron--Frobenius theory. See [Johnson and Paparella](https://arxiv.org/pdf/1611.06970) and [Benvenuti and Farina](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf). The candidate contribution is this particular finite-prefix reversible construction; a bounded source comparison is given in the [companion audit](PRIOR_ART_COMPARISON.md).
