# Physical reversal, even observables and Markov closure

[Generalized word predictor](GENERALIZED_REVERSAL_PREDICTION.md) · [Three-class resource comparison](KINETIC_PARITY_RESOURCE_TRADEOFF.md) · [Physical interface robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md) · [Current research](PRL_EXPLORATION.md)

**Analytic boundary, 23 September 2026.** A reversal-even observable of an equilibrium process has a reversible stationary path law. If that observable is itself an autonomous Markov process, its generator obeys ordinary detailed balance. Thus an equilibrium realization cannot turn an even Markov configuration into an ordinarily nonreversible Markov word state merely by hiding an ordinary-equilibrium phase. Memory, physical reversal parity and the retained state count must be specified.

This note proves the relevant closure and counting statements. It does **not** supply a mechanical, molecular or energy-conserving collision realization of the centered word predictor. Its word-reversal involution is a valid mathematical generalized equilibrium; identifying it with a device's physical reversal remains an additional modeling task. The statements below are elementary consequences of stationary path reversal and Markov closure, not new general lumpability mechanisms.

## 1. Generalized equilibrium and an even observation

Let $X_t$ be a stationary finite-state continuous-time Markov chain with generator $K$, strictly positive stationary law $\mu$, and involution $\theta$. Write $(\Theta f)(i)=f(\theta i)$ and suppose

$$
\mu_{\theta i}=\mu_i,\qquad K^*=\Theta K\Theta.
\tag{1}
$$

The adjoint uses $L^2(\mu)$. Equivalently,

$$
\mu_iK_{ij}=\mu_{\theta j}K_{\theta j,\theta i}.
\tag{2}
$$

The semigroup obeys the same generalized balance identity. In particular the stationary path law on $[0,T]$ is invariant under $X_t\mapsto\theta X_{T-t}$, with the usual left/right convention at jumps.

Let $f$ take finitely many values and be reversal-even:

$$
f(\theta i)=f(i),\qquad Y_t=f(X_t).
\tag{3}
$$

**Proposition 1.** The stationary process $Y$ is time-reversal invariant. If $Y$ is a time-homogeneous continuous-time Markov chain under its stationary law, with generator $L$ and positive law $\bar\mu$, then

$$
\bar\mu_aL_{ab}=\bar\mu_bL_{ba}.
\tag{4}
$$

**Proof.** Apply $f$ to the path reversal in (1); condition (3) removes the state involution. Hence every stationary finite-dimensional law of $Y$ equals its time reverse. If $Y$ is Markov, this gives
$\bar\mu_a(e^{tL})_{ab}=\bar\mu_b(e^{tL})_{ba}$ for every $t\ge0$. Differentiate at zero to obtain (4).

The Markov assumption is substantive. It need hold only for the stationary projected process; strong lumpability, which supplies a common projected generator for every initial law, is a sufficient stronger condition. Deterministic projection of a reversible process is a standard source of reversible processes with memory; see Bacallado, [primary text](https://arxiv.org/pdf/1105.2640), Section 1. The argument here states the involution-even condition explicitly.

For a strongly lumpable partition with blocks $C_a$, the same conclusion follows directly. If

$$
L_{ab}=\sum_{j\in C_b}K_{ij}\quad(i\in C_a),
\qquad \theta C_a=C_a,
$$

then summing (2) over $i\in C_a,j\in C_b$ gives (4), with $\bar\mu_a=\sum_{i\in C_a}\mu_i$. No equal block masses or lower mass bound is needed.

## 2. Stationary flux aggregation is not automatically exact dynamics

For any even partition, define the stationary-flux generator

$$
L^{\rm flux}_{ab}
=\frac1{\bar\mu_a}\sum_{i\in C_a,j\in C_b}\mu_iK_{ij},
\qquad a\ne b,
\tag{5}
$$

and set its diagonal by zero row sums. Equation (2) makes $L^{\rm flux}$ ordinarily reversible. However, unless the projected process is Markov, (5) reproduces only its stationary instantaneous block fluxes; it need not reproduce finite-time transition probabilities, waiting times or controlled responses.

If the projection is Markov under stationarity, its generator must equal (5). In particular an exit cap $Bk$ of $K$ gives the same cap for this closure, since each aggregated exit is a stationary average of microscopic exits out of its block.

A small exact example makes the distinction concrete. On $c\in\mathbb Z_3$, take uniform $\mu$ and rates

$$
K_{c,c+1}=3/4,\qquad K_{c,c-1}=1/4,
\qquad \theta c=-c\pmod3.
\tag{6}
$$

It satisfies (1). The even partition $\{0\},\{1,2\}$ is not strongly lumpable: states $1,2$ return to block $\{0\}$ at rates $1/4,3/4$. Its flux aggregate is the ordinary-reversible two-state generator with rates $1$ and $1/2$.

The projection is not Markov even under its stationary law. A hidden visit to block $\{1,2\}$, starting on entry from $0$, initially selects states $1,2$ with probabilities $3/4,1/4$. Its initial return hazard is therefore $3/8$, whereas its stationary conditional return hazard is $1/2$. A time-homogeneous two-state Markov process cannot have these different hazards for the same current state. This is a finite Markov-memory fixture, not a physical device or a new controlled-prediction separation.

For a positive closure fixture, take the independent product of (6) with a two-state coordinate having rates $0\to1=1$, $1\to0=2$. Reversal acts only on the phase coordinate. Projection onto the second coordinate is even and strongly lumpable, and its ordinary reversible generator is exactly the given two-state generator.

## 3. When eliminating reversal-odd memory preserves the interface

Suppose a generalized-reversible hidden predictor uses the shared interface

$$
q_{iA}(h)=kb_i(h),\qquad
q_{Ai}(h)=k\mu_i e^{2h}b_i(h),
\tag{7}
$$

with $b_i(0)=1$, and every kinetic function is constant on an even partition $f$. The partition into $\theta$-orbits always has this property when $b_{\theta i}(h)=b_i(h)$.

**Proposition 2.** If $Y_t=f(X_t)$ is Markov under the stationary hidden law, the block generator (5), block law $\bar\mu$ and block kinetic functions $\bar b_a(h)$ define an ordinary-reversible predictor with exactly the same controlled visible path laws, for every deterministic protocol, using no more states. It preserves the hidden exit cap and the interface bounds.

**Proof.** Proposition 1 supplies ordinary detailed balance and Section 2 gives the exit cap. Under the stationary hidden law, the block path law is exactly that of this Markov closure. At a hidden entry, the original interface tilts the stationary law by $b_i(h)$; this factor depends only on the block. The exit hazard during a hidden visit also depends only on its block path. Equality of stationary block-path laws is therefore preserved by the entry tilt and the subsequent killing functional. The initial hidden visit uses the untilted stationary law. The visible waiting times and every hidden visit law agree, proving the claim by their alternating-visit construction.

The full state count is the number of retained blocks plus the existing visible state. This proof uses stationary Markov closure, not a claim that the microscopic partition is strongly lumpable after every arbitrary microscopic initialization.

**Consequence for the small word predictor.** At any target and tolerance where the ordinary-reversible lower exceeds the size of a generalized predictor, its $\theta$-orbit process cannot satisfy this Markov-closure hypothesis. In particular, the useful centered-word predictor cannot shed its reversal-odd word memory by stationary-flux aggregation while retaining the same controlled response. If its actuator process itself were Markov, Proposition 2 would give a closure with at most nineteen hidden actuator states in the original family, contradicting the ordinary lower at sufficiently small error.

This identifies where the advantage resides: a retained memory representation can obey generalized balance while its even actuator has a reversible but non-Markov stationary law. It does not attribute observable stationary irreversibility to the equilibrium target or actuator.

## 4. An ordinary-equilibrium phase cannot provide an exact nonreversible Markov lump

Consider a proposed larger autonomous equilibrium model $Z_t$, with stationary law $\Pi$, whose ordinary reversal fixes every full state. Let a retained word state be a deterministic function $W_t=F(Z_t)$. If $W$ is stationary Markov, Proposition 1 with identity involution forces its generator to be ordinarily reversible. Hence it cannot reproduce an ordinarily nonreversible word generator exactly.

The conclusion is independent of the number of hidden phase states. It also follows for any stationary path-reversible microscopic process whenever the projected process is a finite Markov chain. An invertible microscopic evolution alone does not imply the required stationary path symmetry.

There are several distinct ways a proposed implementation can leave these hypotheses:

- a genuine physical odd variable makes the retained word transform nontrivially under reversal;
- the projected process keeps memory and is not a finite autonomous Markov closure;
- a prepared environment or externally driven phase fails the assumed stationary equilibrium condition;
- the retained controller or phase is part of a larger counted state model or changes the permitted interface.

These are changes of assumptions, not contradictions. For approximate endpoint prediction, the existing state lower applies to the entire retained finite ordinary-reversible model only if it remains in the specified interface, preparation and budget class. It does not automatically apply to a different multi-visible-state interface, a continuous hidden state, non-Markov memory or an externally clocked implementation.

A thermal bath is already implicit in a stochastic rate model and is not counted as predictor memory merely because it supplies noise. However, any persistent phase used by the predictor must be accounted for in its retained dynamical model, or its elimination and resulting memory must be specified. Declaring that phase “uncounted” does not establish the smaller finite Markov realization that the lower bound compares.

## 5. What has and has not been realized physically

Any finite involution can be written as an even orbit label together with an orientation taking values $+,-$ on paired states and $0$ on fixed states. This re-encoding adds no states. For the centered word predictor the orbit is $\{w,\operatorname{reverse}(w)\}$ and the actuator is constant on it. This is a mathematical parity representation, not evidence that the orientation is mechanical velocity, angular momentum or a chemically realizable odd coordinate.

Generic Markov dilation is also insufficient for that conclusion. Gregoratti, “Classical dilations à la Quantum Probability of Markov evolutions in discrete time,” [primary text](https://arxiv.org/pdf/math/0702690), Section 3 and Theorem 1, constructs invertible dynamics using a finite collision alphabet and an infinite environment tape with independent inputs. That establishes an invertible realization of Markov evolution. It does not by itself establish a thermal Gibbs environment, the physical word-reversal involution, an energy-conserving collision model or finite persistent environmental memory.

An honest mechanical or collision realization of this particular predictor would still need a physical state space and reversal operation, a stationary equilibrium environment, a justified Markov reduction, and control couplings that produce the stated interface without extra retained resources. No such construction is established here. Nor is there a no-go against every realization with physical odd variables: the closure propositions apply to even observations and ordinary Markov closures, not to all generalized equilibrium systems.

The current positive physical result is therefore the exact rate-network representation and robustness theorem in [Physical interface robustness](PHYSICAL_INTERFACE_ROBUSTNESS.md), under its ordinary-configuration interpretation. The centered-word result remains a rigorous generalized-reversal boundary. A natural odd-parity implementation of that word predictor remains open.
