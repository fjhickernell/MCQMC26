# Immediate manuscript work

## Special-session paper

The initial draft is `manuscripts/special-session/main.tex`, with sections in
that directory and a 12-page compiled preview at `build/main.pdf`.
The limit is 16 pages. Fred requested the MCQMC 2024 macros for these papers;
the draft now uses the same `svproc.cls`, `spmpsci.bst`, and Times font packages
as the Aadit paper. Do not revert to generic article formatting.
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
