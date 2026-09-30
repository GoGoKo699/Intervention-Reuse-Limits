# Three single-source routes into the project

**Shortlist, 30 September 2026; selection pending.** Each option is one
existing work. They are alternatives, not a three-source syllabus.
The [background guide](MANUSCRIPT_BACKGROUND.md) provides the separate
manuscript citation record. The scientific scope remains frozen.

**Recommendation: Option 1 for the closest route into the physical
mechanism of the current result.** Choose Option 2 for a fuller textbook
foundation, or Option 3 for the positive-realization mathematics. None
contains the project's complete controlled state-count theorem; the
remaining bridge is part of what this repository should explain.

| Option | Best use | Main bridge still needed |
| --- | --- | --- |
| 1. Bo–Celani review | Fast hidden variables and reduced kinetic dynamics | Shared-control error guarantees and necessary state counts |
| 2. Gardiner textbook | Probability, Markov dynamics and systematic approximation | The precise prediction contract and positive-model lower bounds |
| 3. Benvenuti–Farina tutorial | Positive dimension versus ordinary linear dimension | Normalized switched CTMCs, equilibrium structure and physical lag |

## 1. Bo and Celani — recommended closest-topic anchor

Stefano Bo and Antonio Celani, **Multiple-scale stochastic processes:
decimation, averaging and beyond**, *Physics Reports* **670**, 1–59
(2017). [Author review](https://arxiv.org/pdf/1612.04999) ·
[DOI](https://doi.org/10.1016/j.physrep.2016.12.003) · key `BoCelani2017`.

Read §1, §2 through §2.2, and the two-component example §2.3.2;
use §4's opening discussion to distinguish dynamical and trajectory
observables. Despite its heading, §2 treats **continuous-time** chains
on discrete states. Its fast-block averaging, especially Eq. (29), is
the closest starting point for our hidden-switch limit. The accessible
author version's relevant passages were inspected.

This route assumes matrix algebra, ODEs, probability and asymptotic
expansions. The primary bridge to build is from sufficient averaging
constructions to our uniform shared-control guarantees and lower bounds
over all smaller models. The review is freely readable; the recommended
route does not require its diffusion or thermodynamic-functional chapters.

## 2. Gardiner — strongest book foundation

Crispin Gardiner, **Stochastic Methods: A Handbook for the Natural and
Social Sciences**, fourth edition, Springer (2009), ISBN
978-3-540-70712-7. [Publisher](https://link.springer.com/book/9783540707127)
· key `Gardiner2009`.

Read §2.3, Chapter 3, §6.3, §§8.2–8.3, then §§9.1–9.2, especially §9.2.3;
Chapter 11 supplies discrete-jump examples. This covers conditioning,
Markov evolution, reversal, elimination and corrections in one volume.
It assumes calculus, matrix algebra and differential equations, with
more diffusion notation than our finite-state proofs require.

Exact section references were verified from the
[publisher contents preview](https://content.schweitzer-online.de/static/catalog_manager/live/media_files/representation/A17908000/18138984_table_of_content_1.pdf?version=1446402180000),
distributed by a legitimate bookseller. The preface and Chapter 2 sample
were inspected; the full book was not. Full access is by library or
purchase. The remaining bridge is the shared-generator prediction task,
positive realizations and class-wide minimality arguments.

## 3. Benvenuti and Farina — focused mathematical route

Luca Benvenuti and Lorenzo Farina, **A Tutorial on the Positive Realization
Problem**, *IEEE Transactions on Automatic Control* **49**(5), 651–664
(2004). [Rutgers-hosted tutorial PDF](https://sites.math.rutgers.edu/~sussmann/papers/res-farina-tutorial-positive-realization.pdf)
· [DOI](https://doi.org/10.1109/TAC.2004.826715) · key `BenvenutiFarina2004`.

Read §II, especially Theorem 2 and Eq. (2), then the examples in §VI
and the minimality discussion in §VII; use §V for existence details.
The inspected 14-page author text explains invariant cones and why a
positive realization may need more states than an unconstrained linear
one. It assumes linear algebra and basic state-space/transfer-function
language.

Its main setting is autonomous discrete-time single-input/single-output
systems. The bridge must impose CTMC normalization, common field
generators, deterministic readout and Gibbs reversibility, then explain
the accuracy orders. This is the most direct mathematical option for
readers who already know Markov dynamics; its historical open-problem
discussion is not a current research-status guide.

## What furnishing the repository would add after selection

The chosen work should supply a recognizable starting vocabulary. A
short project bridge would then do four things:

1. Translate its probability and generator conventions into ours.
2. Explain the target preparation, endpoint-pair task and model reuse.
3. Follow the hidden lag to the positive three-state construction.
4. Explain the class-wide obstruction and the finite-pulse witness.

The bridge should point directly to the frozen proof notes. It should
not reproduce the selected source, require all three options, or add a
new theorem agenda. The existing bibliography supports scholarly
attribution independently of which single teaching anchor is chosen.
