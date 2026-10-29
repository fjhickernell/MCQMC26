# Immediate manuscript work

## Special-session paper

The initial draft is `manuscripts/special-session/main.tex`, with sections in
that directory and a 12-page compiled preview at `build/main.pdf`.
The limit is 16 pages. Fred requested the MCQMC 2024 macros for these papers;
the draft now uses the same `svproc.cls`, `spmpsci.bst`, and Times font packages
as the Aadit paper. Do not revert to generic article formatting.
The manuscript is now an Overleaf-backed submodule at the same path:
<https://www.overleaf.com/project/6ae39728ff70b39ca2fd98b1> (`main` branch).
Keep MCQMC26 as its parent and retain the existing talk/Academic Library links.
Fetch and reconcile Anders's edits before writing; push manuscript commits
to Overleaf before publishing the parent pointer. The standalone paper has
snapshots of the two shared notebook figures under `figures/`; refresh these
only with intentional artifact updates. Do not reupload a ZIP over coauthor edits.

### Cross-machine handoff and confirmed title

Fred confirmed the shortened title on October 29, 2026:
**Component-by-Component Constructions of Kronecker and Lattice Sequences for
Arbitrary Sample Sizes**. This replaces “Sequences Which Are Good for Arbitrary
Sample Sizes.” Keep the manuscript title, Overleaf project name, and both
READMEs consistent. The running title “CBC sequences for arbitrary sample
sizes” already agrees. Preserve the finished talk's title unless its revision
is intentional. If another Mac has additional unpublished manuscript work,
reconcile it while retaining this confirmed title.

The Overleaf manuscript and confirmed title are published on `main` at
`0433585`. Anders's editor invitation was sent and was pending acceptance when
checked. This parent records the manuscript as a submodule, retaining the
existing talk and Academic Library connections. Update the parent on other
Macs before initializing the new manuscript submodule.

Before updating another Mac from the eventual parent commit, inspect its
existing `manuscripts/special-session` folder for uncommitted or unpublished
work: older checkouts have ordinary tracked files there, while the new parent
commit replaces them with a submodule at the same path. Preserve and reconcile
those edits rather than deleting the old directory to make an update succeed.
After a clean parent update, initialize this submodule, fetch its Overleaf
remote, and inspect incoming changes before editing. Do not blindly reset a
coauthor's newer commit to the parent's older pinned snapshot. Git publication
and updates are explicit; this is not instantaneous cross-machine sync.

Routine-sync boundary verified October 29: MCQMC26 is already in the shared
active repository registry. `sync-active.sh` initializes all submodules to
the parent commit's recorded pins, so the published manuscript connection
will reach other Macs without a new repository entry. Automatic promotion to
the latest Overleaf manuscript commit is not configured: the shared updater
currently promotes only `classlib`, `qmcpy`, and `assets/tests/archive`.
If routine `arrive`/`depart` should adopt Anders's latest edits, add an explicit
manuscript-submodule policy in SharedConfigs with clean-tree, fast-forward,
and unpublished-work safeguards. Do not add MCQMC26 as a whole-repository
GitHub/Overleaf mirror pair. Until that policy exists, reconcile Overleaf
changes explicitly and publish the updated parent pointer at Checkpoint.

### Scientific review

Review it with Anders, starting with the permutation-only Newo theorem in
Section 4 and the questions at the end. Do not add a tree presentation.
Unresolved work is marked with dark-green `\codex{[...]}` comments, matching
the Cones papers; retain these until the corresponding issues are resolved.

The SURE GitHub and Overleaf histories were reconciled at `f37fe96`; both
services are synchronized. SharedConfigs registers their verified pairing
with `routine_sync: true`, so future `arrive`/`depart` runs bridge both.
The precise newer Kronecker CBC remains to be supplied by Anders. The current
draft derives a generic CBC from the criterion, without attributing it to
that newer algorithm. Historical slide figures are explicitly unrevalidated.
See the manuscript README and `SOURCE_PROVENANCE.md` before adding results.
Current authors are Alexander Pride and Fred J. Hickernell, in that order,
as Fred specified on October 28 (provisional). The plenary manuscript is not started.

## Aadit coauthored paper

Continue Fred's section-by-section review of the Aadit Jain coauthored paper;
Section 1 has been revised. Next review Section 2 and its assumptions,
notation, algorithm, and coverage argument before progressing through the paper.

## Sources and editing conventions

- The Overleaf submodule is `manuscripts/aadit-jain-paper`; its active source
  is `rqmc_kurt_ci_paper.tex`.
- Fred is currently editing the same source in the separate checkout
  `~/SoftwareRepositories/Confidence Intervals Dependence on Kurtosis`.
  Reconcile the two checkouts before editing or publishing; do not overwrite
  local or remote changes. Push manuscript commits to Overleaf before updating
  this repository's submodule pointer.
- `rqmc_kurt_ci_paper_2026-10-18.tex` is the unchanged archival snapshot.
- New revisions and retained author notes use the red `\fredcodex{...}` macro.
  Existing coauthor edit wrappers were removed while preserving their text;
  their macro definitions remain available. Resolved conversations were removed,
  and unresolved author notes are explicitly labeled in red.

## Remaining review points

- Recheck the Berry–Esseen cost proof, especially monotonicity and minimizer
  existence, and supply references for the Berry–Esseen constants.
- Distinguish distributional CLTs from the moment convergence needed to conclude
  kurtosis convergence. Check the ridge-direction normalization and the
  stratification interval indexing.
- The coverage guarantee assumes a valid bound on replicate kurtosis for a
  fixed rule and sample size. The numerical value 10 is not a uniform bound;
  the manuscript now records a one-dimensional jump example exceeding it.
- Decide whether to add an unbounded numerical example and which comparisons
  merit the space. Complete the abstract, keywords, discussion, and length review.

## Validation

Build in the manuscript checkout with
`latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error rqmc_kurt_ci_paper.tex`.
The current 19-page draft compiles with citations and references resolved.
One overfull cost equation remains. Mathematical review
and official conference-template compliance remain unfinished.
