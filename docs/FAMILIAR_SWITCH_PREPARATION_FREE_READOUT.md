# Repeated readout for the preparation-free return test

Seven initial readings and seven final readings extend the
[four-word preparation-free test](FAMILIAR_SWITCH_PREPARATION_FREE_TEST.md)
to unknown fixed detector error probabilities, including errors
correlated with the hidden kick in the same reading. With the same
nine-million-trial cap and score cutoff $.004$, the test has false
rejection below $5\%$ and power above $95\%$ under the explicit
instrument and freshness assumptions below. The acquisition cost is
**126 million raw binary readings**.

The proof compares the observed majority-labelled groups with groups
formed using the unobserved true signs. A bounded number of incorrectly
labelled records changes their fixed-size averages by a bounded amount.
This permits correlation between a readout error and its associated
hidden-state disturbance without an independence-based identification of
the observed conditional response.

This is a sampling extension for the four retained initial/final pair
laws. It does not assert that a three-state predictor reproduces the
complete fourteen-reading transcript. Manuscript drafting remains
deferred.

[Exact verifier](../scripts/verify_switch_preparation_free.py) ·
[Certificate report](../reports/switch_preparation_free.json) ·
[Four-word realization and scope](FAMILIAR_SWITCH_PREPARATION_FREE_REALIZATION.md)

## 1. The repeated-readout contract

Each trial uses one of $0,H,0H,H0$ and proceeds as follows:

1. Prepare the system and make seven consecutive initial readings.
2. Execute the selected field word.
3. Make seven consecutive final readings.

Every reading first observes the current true sign, flips its recorded
bit with the specified electronic error, and may then disturb the hidden
state. **Every hidden disturbance during either seven-reading block
preserves the true sign.** Thus each block has one fixed true sign to
which all seven electronic errors refer. This includes any hidden motion
between readings; unmodelled sign changes during the block are not
allowed by this contract. The extra measurement operations and their
duration are experimental resources.

At the initial stage the error probability is one fixed
$p_i\in[0,1/2]$; at the final stage it is one fixed
$p_f\in[0,1/2]$. Before every reading, conditional on the full past and
the current hidden state, its electronic error is a Bernoulli variable
with that stage's fixed parameter. This is the **freshness** assumption.
The error may be correlated with the hidden kick applied by that same
reading. Subsequent errors must still have the stated conditional
Bernoulli law. Unconditional error marginals alone are insufficient.

Each reading uses a fixed joint error-and-kick kernel, possibly fixed in
advance by its position within a block. Conditional on the current model
state, that same joint kernel applies for every past, word, and trial.
Its nonselective hidden channel is therefore a fixed kernel as well;
it is not selected from different stationary kernels in response to
earlier readout outcomes. Subsequent evolution uses only the
postmeasurement model state and the prescribed fixed controls. Recorded
errors do not trigger control feedback during the word. Any persistent
detector or controller variable that changes these post-instrument
transition laws must be included in the model state being counted,
rather than treated as unmodelled external memory. The null's explicitly
allowed history-dependent preparation before the next trial is unchanged.

The null retains the strictly positive stationary laws, exact common
tilt $u=3/5$, and fixed reversible kernels from the ideal theorem.
Its preparation may be arbitrary and history-dependent. Its initial
readings need not preserve equilibrium: sign preservation alone fixes
the hidden state whenever the true initial sign is a singleton.

For the target, require each initial reading's nonselective hidden
channel to preserve the low stationary law as well as the sign. A
composition of seven such channels preserves the stationary joint law
of the true initial sign and the postmeasurement hidden state. This
remains true when each error is correlated with its own kick, because
the statement concerns the nonselective channel. No equilibrium
preservation is needed for the final block, whose true sign cannot
change.

The target's conditional **true-sign pair law**, with these physical
measurement operations included, is required to be within
$B=79/10^6$ in TV of one fixed reference from the one-percent kinetic
family, for every word and preparation history. The target finite-reset,
field, and timing budget in the ideal theorem supplies this allowance
under exact protected initial channels. Its old instrument allowance
need not be spent. In particular, an arbitrary sign-changing instrument
fault cannot be imported into a repeated block under that allowance:
exact sign preservation is needed separately throughout both blocks.

For target power only, assume $p_i,p_f\le1/100$. The null permits the
whole interval $[0,1/2]$ and uses the disagreement gates below.

## 2. Acquisition, gates, and rejection

Keep the deterministic four-word cycle and fixed allocation

$$
 N=9{,}000{,}000,\qquad M=N/4=2{,}250{,}000,
 \qquad n=1{,}000{,}000.                              \tag{1}
$$

The majority of the seven initial readings labels the observed initial
sign; the majority of the seven final readings labels the observed
final sign. Retain the first $n$ observed records in each of the eight
word/initial-sign groups. If any group is incomplete at the fixed cap,
do not reject.

At each stage also count trials in which its first two readings disagree.
Reject only if **both** disagreement frequencies are at most $.03$,
all eight groups are complete, and

$$
 \widehat R_->.004,\qquad \widehat R_+<-.004,            \tag{2}
$$

where each $\widehat R_s$ is formed from the observed conditional return
averages using

$$
 R_s=(1-su)r_{0H,s}-(1+su)r_{H0,s}
                         +2su\,r_{0,s}r_{H,s}.         \tag{3}
$$

All $14N=126{,}000{,}000$ raw readings are counted as acquisition cost,
including readings on trials whose observed group is already full.
The majority pairs and disagreement counts are the statistics used by
the test.

For the target implementation, the inherited reset duration of 63
attempt-time units applies after an arbitrary preceding final-block
kick. Nine million resets cost 567 million attempt-time units. The
four-word cycle has average active duration $15/8=1.875$, adding
16.875 million units, for **583.875 million nominal attempt-time units**
in total. This excludes the 126 million read operations and any barrier,
switching, controller, or additional reset-clock costs. Converting to
seconds requires an attempt frequency. These are target resource costs;
no reset-duration premise is imposed on rivals.

## 3. The disagreement gates handle large unknown errors

Sign protection and freshness give first-two disagreement probability

$$
 q(p)=2p(1-p).                                        \tag{4}
$$

This identity does not assume that either electronic error is
independent of its own subsequent kick. If a null has $p_i>.02$ or
$p_f>.02$, choose one such stage before observing the experiment.
Because $q$ increases on $[0,1/2]$, its disagreement probability exceeds
$q(.02)=.0392$. Conditional Hoeffding gives

$$
 \Pr\{\text{that stage passes its gate}\}
 \le e^{-2N(.0392-.03)^2}
 =e^{-38088/25}<.05.                                  \tag{5}
$$

There is no union over stages in this null case: rejection requires the
chosen bad stage to pass. Thus it remains to analyze nulls with both
stage error probabilities at most $.02$.

## 4. Few majority errors imply stable retained averages

For seven fresh errors at rate $p$, the majority-error probability is

$$
 b_7(p)=\sum_{k=4}^{7}\binom7k p^k(1-p)^{7-k}.
$$

For $p\le.02$, monotonicity gives

$$
 b_7(p)\le b_*:=b_7(1/50)
 =\frac{26053}{4882812500}=.0000053356544.               \tag{6}
$$

For each word and stage, let $E$ count majority errors among its $M$
trials. The conditional moment generating function of each error
indicator is bounded by $1+b_*(e^t-1)$. Iteration at $t=\log4$ gives

$$
 \Pr(E>50)\le\Pr(E\ge50)
 \le 4^{-50}(1+3b_*)^M
 \le 4^{-50}e^{3Mb_*}
 <\frac{3^{37}}{4^{50}},                              \tag{7}
$$

because $3Mb_*=36.0156672<37$ and $e<3$. There are eight such
word/stage counts. Their union failure probability is bounded by

$$
 \epsilon_E:=8\frac{3^{37}}{4^{50}}<3\times10^{-12}.    \tag{8}
$$

No independence between these counts is needed.

For a fixed word and sign, compare the first $n$ records selected by the
observed initial majority with the first $n$ records selected by the
true initial sign. If fewer than $n$ true-sign records occur before the
cap, append artificial records after the cap to fill that true group.
These records are a proof device, not an instruction to take more data.
For a null singleton they are independent Bernoulli draws with its fixed
true return probability. For a target they use the corresponding fixed
reference return probability. Only the null's chosen singleton row
needs this distributional interpretation; its other row is irrelevant
to the size proof.

Changing $E_i$ initial labels changes at most $E_i$ members of a
fixed-size ordered first-$n$ selection, including the appended records.
Pair the removed and inserted members; each replacement changes a
binary average by at most $1/n$. On the common selected records,
$E_f$ incorrect final majorities change at most $E_f$ binary values.
Therefore, whenever the observed group completes,

$$
 |\widehat r_{w,s}^{\rm observed}
        -\widehat r_{w,s}^{\rm true,padded}|
 \le\frac{E_i+E_f}{n}.                               \tag{9}
$$

This is a deterministic statement about the two labelled lists. It
allows all error events to be correlated with subsequent hidden motion
and with the outcome being estimated. On the event complementary to
(8), every difference in (9) is at most
$100/n=10^{-4}$.

On the cube $[0,1]^4$, the polynomial (3) obeys

$$
 |R_s(\mathbf r)-R_s(\mathbf r')|
 \le(2+4u)\|\mathbf r-\mathbf r'\|_\infty.
$$

For the product term one can use
$|ab-a'b'|\le|a-a'|+|b-b'|$ directly, so no additional quadratic
allowance is needed here. Consequently the observed and padded true
statistics differ by at most

$$
 \Delta_R=\frac{22}{5}\,10^{-4}=.00044.                \tag{10}
$$

## 5. Concentration for the padded true statistics

The ideal theorem's stopped concentration argument applies unchanged
to true-sign selected records, followed if necessary by their artificial
completion. Retention is determined before each true final outcome.
For the oracle concentration proof, reveal the current true initial sign
to decide retention, then integrate over the current initial readout
block and field evolution when taking the conditional final-sign mean.
The current block's error transcript is revealed together with the
completed trial, not separately conditioned upon in that mean. All
previous trials, including their raw transcripts, remain in the past.
This filtration choice is legitimate because oracle retention uses the
true initial sign, not the current electronic errors; it avoids assuming
that a kick remains unbiased after conditioning on its correlated error.
Real singleton records have exactly their fixed reference mean, and
the appended records have the same mean. For a target, real records
have conditional reference displacement at most

$$
 b=\frac{B}{1/2-B}=\frac{79}{499921};                  \tag{11}
$$

the appended records have displacement zero. This construction is on an
enlarged probability space and does not condition the law on observed
or true completion.

For each sign, expansion around its reference return probabilities has
linear coefficient squared sum at most $28/5$. Its predictable linear
drift is at most $(22/5)b$ for a target and zero for the singleton null.
With $\eta=.01$, the quadratic remainder is at most $.00012$ except
with probability $4e^{-2n(\eta-b)^2}$; set $b=0$ for the null.
This follows from the same two single-word mean estimates used in the
ideal proof. The artificial records ensure that every true row used by
the proof has exactly $n$ entries, while (9) only needs observed
completion.

For a null with $p_i,p_f\le.02$, choose a singleton sign. Its true
residual is zero. Rejection, (9)--(10), and the quadratic bound require
a one-sided linear deviation with margin

$$
 h_N=.004-.00044-.00012=.00344.
$$

Therefore

$$
 \Pr_{\rm null}(\text{reject})
 \le e^{-2nh_N^2/(28/5)}+4e^{-200}+\epsilon_E
 =e^{-3698/875}+4e^{-200}+\epsilon_E<.015<.05.           \tag{12}
$$

The large-error and small-error null cases are alternatives. Combining
(5) and (12) by their maximum establishes uniform size below $5\%$ for
all $p_i,p_f\in[0,1/2]$. It does not add the two case bounds.

## 6. Target power, observed quotas, and readout gates

The entire one-percent kinetic family has reference residuals
$R_->.009$ and $R_+<-.009$. For targets $p_i,p_f\le.01$, the same
conservative error-count allowance (8) applies. After the conditional
execution drift, stability shift, and quadratic remainder, the linear
margin to either threshold is

$$
 h_T=.009-.004-\frac{22}{5}\frac{79}{499921}
                   -.00044-.00012
     =\frac{46801231}{12498025000}>0.                  \tag{13}
$$

The sum of both signed-score miss bounds and the associated remainder
failures is therefore

$$
 2e^{-2nh_T^2/(28/5)}
       +8e^{-2n(.01-79/499921)^2},\qquad
 \frac{2nh_T^2}{28/5}
 =\frac{2190355223115361}{437361760921750}>5.008.        \tag{14}
$$

It remains to pay for the observed groups and the two gates. At target
error rate $.01$,

$$
 b_T:=b_7(1/100)=\frac{1708349}{5000000000000}
                       =.0000003416698.
$$

Conditional on each preparation history, either true initial sign has
probability at least $1/2-B$. A majority error can decrease its observed
probability by at most $b_T$, so each observed-sign probability is at
least $q_T=1/2-B-b_T$. Conditional Hoeffding bounds failure of any
observed quota by

$$
 \epsilon_Q\le
 8\exp\!\left[-\frac{2(Mq_T-n)^2}{M}\right].            \tag{15}
$$

The exponent exceeds $13849$. At either target stage the disagreement
probability is at most $q(.01)=.0198$. Thus failure of either $.03$
gate is bounded by

$$
 \epsilon_G\le2e^{-2N(.03-.0198)^2}
              =2e^{-46818/25}.                        \tag{16}
$$

Adding (8), (14), (15), and (16) gives total target miss probability
below $.014<.05$. The verifier checks this comparison using exact
fractions and the reciprocal positive Taylor bound for each negative
exponential. No Gaussian approximation, independent-trial assumption,
or conditioning on a successful gate is used.

## 7. What is and is not removed

The four-word singleton identity eliminates the ordinary small rival's
hidden preparation promise. The repeated-readout extension additionally
permits same-reading correlation between electronic errors and hidden
backaction. Sign protection throughout each readout block, fresh fixed
error probabilities, one fixed pair of reversible kernels, and the
shared stationary force relation remain assumptions. The disagreement
gates check a consequence of the fresh-error model; they do not certify
that model or sign protection from data alone.

The general three-state realization concerns the four retained binary
pair laws. With imperfect target execution, comparison to its fixed
ideal reference must also pay the stated execution and majority-error
allowances. No exact three-state fit to arbitrary error/kick correlations,
the full raw transcript, or its correlations with later trials is claimed
here. The additional readings and calibration counts are declared
experimental resources, and the original two-word five-million-trial
test retains its original scope.
