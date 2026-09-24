# A relative force tolerance without a stationary-mass floor

The four-word return identity is stable under a small multiplicative
error in the common stationary force relation. This preserves the new
freedom to prepare an ordinary rival arbitrarily, including in states
with arbitrarily small stationary mass. An unweighted TV error between
stationary laws does not provide the same guarantee.

At the nominal contrast $u=3/5$, a stationary likelihood-ratio spread
of at most $1001/1000$ permits singleton residual magnitude at most
$1/2500=.0004$. The same nine-million-trial endpoint-registration test
then has false rejection below $4\%$; its target power bound is
unchanged. The ideal four-pair state minima remain three versus four
throughout $0\le\delta_{\rm pair}\le9/10000$.

These are model-level tolerances, not calibration values established by
the return data. Manuscript drafting remains deferred.

[Endpoint registration](FAMILIAR_SWITCH_ENDPOINT_REGISTRATION.md) ·
[Four-word realization](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md) ·
[Ideal return test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md) ·
[Exact verifier](../scripts/verify_switch_endpoint_registration.py) ·
[Certificate report](../reports/switch_endpoint_registration.json)

## 1. A relative stationary-law premise

Let $P_0,P_H$ be fixed stochastic kernels, each reversible for its
strictly positive stationary law. Replace the exact Gibbs relation by

$$
 \pi_H(x)=\frac{\pi_0(x)(1+uS(x))w(x)}{Z},\qquad
 0<u<1,\quad w(x)>0,\qquad
 \frac{\max_x w(x)}{\min_x w(x)}\le L,
 \quad L\ge1.                                      \tag{1}
$$

Here $Z$ is the normalization. There is no stationary balance promise,
no lower bound on a positive stationary mass, and no common or
stationary preparation promise. The same kernels, stationary laws,
readout and weights serve all four words. Positive stationary support
is still required.

Use faithful signs immediately before and after each field word when
defining the ideal conditional return probabilities. In particular,
the initial sign refers to the state that actually enters the field
word. An earlier preparation or measurement operation can therefore be
included in the rival's arbitrary preparation. The endpoint-registration
note separately controls errors in the recorded versions of these signs.

Suppose visible sector $s$ is a singleton state $j$. Define

$$
 a=(P_0)_{jj},\quad b=(P_H)_{jj},\quad
 X=(P_0P_H)_{jj}-ab,\quad
 Y=(P_HP_0)_{jj}-ab.
$$

The cross-path sums $X,Y$ are nonnegative and at most one. The measured
return residual is

$$
 R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}
           +2su r_{0,s}r_{H,s}
     =(1-su)X-(1+su)Y.                              \tag{2}
$$

Every other state $k$ has sign $-s$. Detailed balance and (1) give

$$
 (P_0)_{jk}(P_H)_{kj}
 =\frac{1+su}{1-su}\frac{w(j)}{w(k)}
       (P_H)_{jk}(P_0)_{kj}.                         \tag{3}
$$

Put $U=(1-su)X$ and $V=(1+su)Y$. Summing the nonnegative terms in
(3) yields

$$
 L^{-1}V\le U\le LV.
$$

If either sum vanishes, both vanish. Otherwise the same inequalities
give $|U-V|\le(L-1)\min(U,V)$. Since
$U\le1-su$ and $V\le1+su$, this proves the mass-independent bound

$$
 \boxed{|R_s|\le(1-u)(L-1).}                       \tag{4}
$$

One can also use the complementary bound
$|R_s|\le(1+u)(1-L^{-1})$ and take the smaller of the two.
Only (4) is needed below. It reduces to the exact singleton identity
when $L=1$. Its proof does not divide an error tolerance by the mass
of a rarely occupied state.

Every ordinary model with at most three states and both visible signs
has a singleton. At least one of its two residuals therefore lies in
the interval specified by (4), whatever preparation was used for each
word or previous history.

## 2. Energy and field interpretation

Writing $w=e^\xi$, condition (1) is equivalent to

$$
 \max_x\xi(x)-\min_x\xi(x)\le\log L.             \tag{5}
$$

An additive constant in $\xi$ is irrelevant. If the nominal field is
$H_0=\operatorname{atanh}u$, an actual field error $\Delta H$ and an
unintended energy change $\Delta E(x)$ can be included through

$$
 \xi(x)=\Delta H\,S(x)-\frac{\Delta E(x)}{k_{\rm B}T}.
$$

A sufficient condition is consequently

$$
 2|\Delta H|+
 \frac{\max_x\Delta E(x)-\min_x\Delta E(x)}{k_{\rm B}T}
 \le\log L.                                        \tag{6}
$$

Here $H$ is a dimensionless field. The unwanted energy change is the
residual in the high-versus-low force relation, after accounting for
the intended measured-coordinate coupling. For a charge realization,
spectator-gate cross-talk is one possible contribution. Equation (6)
is a uniform microscopic energy premise over the comparison model's
states; a small observed occupation change does not establish it.

The concrete choice below permits total residual log-weight spread
$\log(1.001)\simeq .0009995003$. This number describes the theorem's
tolerance, not a demonstrated device calibration. Field uncertainty
already included in (6) must not be charged again as a separate force
defect. A target's execution error still has its own role in the
target-power comparison to the fixed reference.

## 3. The same endpoint test with a wider ordinary null

Take

$$
 u=\frac35,\qquad L=\frac{1001}{1000},\qquad
 \rho=(1-u)(L-1)=\frac1{2500}=.0004.                \tag{7}
$$

Use the unchanged endpoint-registration acquisition and rejection rule:
nine million trials, one million retained returns per word/sign group,
and rejection only when both signed residuals exceed $.004$ in their
target directions. The endpoint-label error bound is $5\times10^{-6}$
per stage conditional on the premeasurement history. This is the
registration premise of the companion note, rather than an assumption
of independent detector flips or seven protected votes.

Its error-count comparison gives a residual displacement at most
$.00044$ except on an event bounded by

$$
 \epsilon_E=8\frac{3^{34}}{4^{50}}.
$$

The singleton oracle's polynomial expansion has a quadratic remainder
of magnitude at most $.00012$, except with probability $4e^{-200}$.
Its linear coefficient squared sum remains at most $28/5$. The only
change in the null proof is that its reference residual can have
magnitude $\rho$, rather than being zero. For whichever sign is a
singleton, rejection therefore requires a linear deviation of at least

$$
 h_N=.004-.0004-.00044-.00012=.00304.
$$

The stopped concentration proof then gives

$$
 \boxed{\Pr_{\rm null}(\mathrm{reject})
 \le e^{-2(10^6)h_N^2/(28/5)}+4e^{-200}+\epsilon_E
 =e^{-2888/875}+4e^{-200}+\epsilon_E<.04.}            \tag{8}
$$

This is uniform over arbitrary history-dependent rival preparations.
It does not condition on completed groups or small realized error
counts. Incomplete groups still cause nonrejection. The fixed-model
choice of singleton sign requires no union over signs.

The target family and all target assumptions are unchanged. It obeys
the exact force relation, which is contained in (1), and its reference
residuals satisfy $R_->.009$, $R_+<-.009$. Broadening the ordinary
null does not reduce those target residuals or change the statistic.
The companion theorem's target miss bound below $.014$, hence power
above $98.6\%$, therefore remains valid. No trial or measurement count
is increased by (7).

Equation (8) concerns the conditional endpoint-registration model.
It does not automatically extend the old disagreement-gated detector
model or an unweighted stationary-law TV allowance. Those are distinct
interfaces and would require their own error accounting.

## 4. A finite ideal-table state-count interval

The stationary one-percent kinetic target has an exact general
three-state realization of all four ideal pair laws, and has both
residual magnitudes greater than $9/1000$. Both facts are proved in
the four-word realization note. The target and its general predictor
have $w=1$, so they remain admissible under (1).

Suppose an ordinary rival with at most three states approximates all
four target pair laws to maximum TV error $\delta<1/2$. The target's
initial signs are balanced. The conditional-return error is consequently
at most

$$
 \epsilon=\frac{\delta}{1/2-\delta}.
$$

The return polynomial is $22/5$-Lipschitz on $[0,1]^4$. In the
rival's singleton sector it must therefore obey

$$
 |R_s^{\rm target}|
 \le\rho+\frac{22}{5}\frac{\delta}{1/2-\delta}.
$$

At $\delta=9/10000$ the right side satisfies

$$
 \frac1{2500}+\frac{22}{5}\frac9{4991}
 =\frac1{2500}+\frac{198}{24955}<\frac9{1000},       \tag{9}
$$

which is a contradiction. This excludes every ordinary competitor
with at most three states throughout the specified TV interval,
without a preparation promise or stationary-mass floor.

Every two-state stationary stochastic kernel is reversible for its
stationary law, so the same exclusion also rules out general two-state
competitors. The exact general three-state predictor and physical
ordinary four-state target give the upper bounds. In the comparison
class (1),

$$
 \boxed{D_{\rm all}(\delta)=3,\qquad
 D_{\rm ord}(\delta)=4,\qquad
 0\le\delta\le\frac9{10000}.}                       \tag{10}
$$

These minima concern four ideal binary pair laws and the stated
stationary target family. The endpoint-registration test has its own
execution and label-error bounds. Equation (10) is not an exact
realization claim for a meter's complete raw current trace or for all
intertrial correlations.

## 5. Why stationary TV alone does not suffice

Let $0<\varepsilon<1/2$ and use three states $a,b,c$ with

$$
 S=(+1,-1,-1),\qquad
 \pi_0=\pi_H=(\varepsilon,\varepsilon,1-2\varepsilon),
 \qquad
 P_0=P_H=P=
 \begin{pmatrix}
 3/4&1/4&0\\
 1/4&3/4&0\\
 0&0&1
 \end{pmatrix}.                                    \tag{11}
$$

The stationary law is strictly positive. Both kernels are reversible
for it. This is a finite-time continuous-time propagator: $P=e^C$,
where the only nonzero off-diagonal rates of $C$ are
$C_{ab}=C_{ba}=(\log2)/2$. The kernel is reducible, which is
permitted in the comparison class; no zero stationary weights are
being introduced.

The nominal tilted law at $u=3/5$ is

$$
 \pi_*=
 \left(\frac{4\varepsilon}{1+3\varepsilon},
       \frac{\varepsilon}{1+3\varepsilon},
       \frac{1-2\varepsilon}{1+3\varepsilon}\right).
$$

Its TV difference from the actual high law is

$$
 \operatorname{TV}(\pi_H,\pi_*)
 =\frac{3\varepsilon(1-\varepsilon)}{1+3\varepsilon}
 \longrightarrow0.                                \tag{12}
$$

Prepare every word with law $(1/2,1/2,0)$. Conditional on the initial
sign, the prepared state is respectively $a$ or $b$. The single-word
return probabilities are $3/4$ and the two-word return probabilities
are $5/8$, for either sign. All four pair laws are independent of
$\varepsilon$. Nevertheless

$$
 R_+=-\frac3{40},\qquad R_-=\frac3{40}.              \tag{13}
$$

Thus arbitrarily small unweighted stationary-law TV error can coexist
with an order-one violation of both nominal return identities in an
ordinary three-state model. It cannot supply a uniform residual bound
that tends to zero when no stationary-mass floor or preparation
restriction is imposed. This example is not a fit to the selected
target tables; it isolates the force-law premise.

The failure also occurs for irreducible continuous-time models. Let
$\Pi_\varepsilon$ have every row equal to
$\pi_\varepsilon=(\varepsilon,\varepsilon,1-2\varepsilon)$, and
use at both fields the generator

$$
 Q_\varepsilon=C+\varepsilon(\Pi_\varepsilon-I).
$$

Every off-diagonal rate is positive. Both summands are reversible for
$\pi_\varepsilon$, and $C\Pi_\varepsilon=\Pi_\varepsilon C=0$.
The common unit-time propagator is consequently

$$
 e^{Q_\varepsilon}
 =e^{-\varepsilon}P+(1-e^{-\varepsilon})\Pi_\varepsilon
 \longrightarrow P.
$$

The stationary force error is still exactly (12). With the same
preparation, continuity of the return polynomials gives
$R_+\to-3/40$ and $R_-\to3/40$. Thus the obstruction is not
caused by nonembeddability or reducibility. No quantitative threshold
for this optional irreducible family is needed for the counterexample.

The force error lies in a pair of states whose total stationary mass
vanishes, while arbitrary preparation continues to use that pair on
every trial. The likelihood-ratio condition (1) controls this error
uniformly on those states. Unweighted stationary TV does not.
