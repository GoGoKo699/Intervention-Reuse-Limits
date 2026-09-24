# Next operating point: a weaker field, the same two protocols

**Status: exploratory numerical lead, not a new robustness or sampling
certificate.** The current certified operating point remains unchanged.
The next candidate keeps $J=\log3$ and changes only the applied field to
$H=\log2$ and each dwell time to $5/4$. Thus

$$
 t=\tanh J=\frac45,\qquad u=\tanh H=\frac35,
 \qquad \tau_0=\tau_H=\frac54.
$$

Both experiments still start from the same zero-field equilibrium and
record only the initial and final binary readouts. The chronological
words remain $0H$ and $H0$. There is no additional field, readout,
preparation, or protocol type.

## Signal comparison

Use the recorded moments $(M,C,L,D)$ and scalar

$$
 R=u(C-D)+uMD-(u-M)L
$$

from the [unknown-detector witness](FAMILIAR_SWITCH_UNCALIBRATED_READOUT.md).
The following floating-point values set both independent symmetric
bit-error probabilities to one percent, so the initial and final detector
contrasts are both $0.98$.

| Operating point | $u$ | $\tau_0$ | $\tau_H$ | Recorded $R$ |
|---|---:|---:|---:|---:|
| Current certified fixture | $4/5$ | $3/2$ | $3/2$ | $0.001715761320$ |
| Recommended next candidate | $3/5$ | $5/4$ | $5/4$ | $0.004385442026$ |
| Unequal-duration comparison | $3/5$ | $3/2$ | $1$ | $0.004733737234$ |

The recommended equal-duration candidate raises the raw signal by a
factor of approximately **2.556**. All three rows satisfy
$0<M<u$, $L>0$, $D>0$, $C<D$, and $R>0$ in this calculation.
The equal-duration candidate is preferred for simplicity; the unequal
row records a nearby comparison rather than a change to the proposed
next experiment.

For the equal-duration candidate, the latent moments, in the order
$(m,c,\ell,d)$ defined in the witness note, are

$$
 (0.22064032707197068,\ 0.48288470690620500,
   0.12599041595718366,\ 0.50147660062514465).
$$

At one-percent errors, the corresponding recorded moments are

$$
 (0.21622752053053126,\ 0.46376247251271924,
   0.12347060763803998,\ 0.48161812724038890).
$$

## The existing positive predictor still applies

Section 3, equations (G1)--(G7), of the
[structure theorem](FAMILIAR_SWITCH_STRUCTURE.md) provide a positive
three-state predictor for every $t\in(0,1)$ and nonnegative field.
For this candidate the same coordinate matrix and zero-field law are

$$
 F=\begin{pmatrix}
 1&-1&-4/5\\
 1&1&-8/5\\
 1&1&41/40
 \end{pmatrix},\qquad
 \widehat\pi_0=(1/2,3/70,16/35).
$$

The second column is the deterministic readout. At the new high field,
$A=135/481$, $B=320/481$ and

$$
 \widehat Q_H=
 \begin{pmatrix}
 -180/481&876/3367&384/3367\\
 33/37&-1987/1295&832/1295\\
 9/481&1224/16835&-1539/16835
 \end{pmatrix},\qquad
 \widehat\pi_H=(1/5,12/175,128/175).
$$

The low-field generator is the same (G3) formula with $(A,B)=(0,4/5)$.
All off-diagonal rates are positive. At either field,

$$
 \widehat Q_hF
 =F\begin{pmatrix}0&A&0\\0&-1&4/5\\0&B&-1\end{pmatrix},
 \qquad \widehat\pi_h\widehat Q_h=0.
$$

Also $\widehat\pi_0F=(1,0,0)$ and
$\widehat\pi_0\operatorname{diag}(\widehat S)F=(0,1,4/5)$,
the same initial function moments as the physical model. These identities
give both endpoint means and initial--final correlations under both
words, using the existing closure argument. They concern the specified
two joint laws, not arbitrary multitime observation laws.

## Reproduce the three numerical rows

Run this command from the repository root after installing the pinned
[requirements](../requirements.txt): NumPy 2.3.5 and SciPy 1.17.0.
It uses the frozen
[physical-generator helper](../scripts/verify_familiar_switch_margin.py),
whose SHA-256 is
`e2a3056da26a357c457eeb199bc9dd3d7c2cf5f7bcba8a3b91f1df68e97b5397`.
The helper constructs exact rational generators and checks detailed
balance and closure; the exponentials below are floating-point
diagnostics. The command writes no files and runs no optimizer.

```bash
.venv/bin/python - <<'PY'
from fractions import Fraction as F
import sys
import numpy as np
from scipy.linalg import expm

sys.path.insert(0, 'scripts')
from verify_familiar_switch_margin import physical_generator

q0, pi0, readout = physical_generator(F(4, 5), F(0))
q0, pi0, s = [np.asarray(x, dtype=float) for x in (q0, pi0, readout)]
rows = [('current', F(4, 5), 1.5, 1.5),
        ('equal next', F(3, 5), 1.25, 1.25),
        ('unequal comparison', F(3, 5), 1.5, 1.0)]
for name, u, tau0, tauH in rows:
    qH, _, _ = physical_generator(F(4, 5), u)
    e0 = expm(tau0 * q0)
    eH = expm(tauH * np.asarray(qH, dtype=float))
    y, z = e0 @ eH @ s, eH @ e0 @ s
    latent = np.array([pi0 @ y, (pi0 * s) @ y,
                       pi0 @ z, (pi0 * s) @ z])
    M, C, L, D = latent * [.98, .98**2, .98, .98**2]
    u = float(u)
    R = u * (C - D) + u * M * D - (u - M) * L
    gates = 0 < M < u and L > 0 and D > 0 and C < D and R > 0
    print(name, 'R =', format(R, '.12f'), 'gates =', bool(gates))
    print('latent:', [format(x, '.17g') for x in latent])
PY
```

This lead came from a bounded diagnostic search over 2,304 equal-duration
cases and 1,029 nearby unequal-duration cases, each using matrices of
dimension four. It is not a global optimality result. The next research
step is to certify this simple candidate's target moment intervals,
physical tolerance budget, and statistical test. No current
finite-accuracy margin, calibration guarantee, or trial count is
transferred to it, and this exploratory calculation is not a default CI
gate or a new certificate report.
