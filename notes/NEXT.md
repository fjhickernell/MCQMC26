# Immediate manuscript work

## Plenary paper

The new `manuscripts/plenary` Overleaf submodule contains **Where Quasi-Monte
Carlo Theory and Practice Meet**, by Fred J. Hickernell, developed from the
current plenary slides and submitted abstract. The project is
<https://www.overleaf.com/project/6ae4101e2b7c96d63cf03bd6> (`main` branch).
The main source is `mcqmc2026_plenary.tex`; the preview is
`build/mcqmc2026_plenary.pdf`. The original draft was published at `eb04589`.
Fred specified **25 pages** for this paper on October 29, 2026; the special-session
limit remains 16. Use the MCQMC 2024 macros and dark-green `\codex{[...]}`
comments. The initial draft compiles to 19 pages including references and
the front author agenda. Figures are byte-identical snapshots of shared
notebook artifacts, with hashes and caveats in the manuscript provenance.

Next, review the front agenda with Fred and decide the balance between a
perspective and a computational study. Reproduce a selected subset of
experiments, independently validate the importance proposal comparison,
check regularity assumptions after transformation, and complete primary
error-assessment/software citations. Existing plots do not validate coverage.
The actual UQ target is a posterior second moment of an integrated penalty;
do not copy stale notebook probability wording. Keep detailed CBC/Newo proofs
in the special-session paper. Both drafts cite the other as in preparation.
Fetch and inspect Overleaf changes before editing; publish manuscript commits
before advancing the parent pointer. The slides themselves remain unchanged.

## Special-session paper

The initial draft is `manuscripts/special-session/mcqmc2026_special_session.tex`, with sections in
that directory and a 13-page compiled preview at `build/mcqmc2026_special_session.pdf`.
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

The Overleaf manuscript is published on `main`, including the
confirmed title, infinite-precision Newo formulation, coordinate-reflection
invariance, the generator-search action, sync/Codex-note instructions, and
the companion plenary draft reference.
Anders's editor invitation was sent and was pending acceptance when
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

Routine manuscript synchronization is now implemented in SharedConfigs
`bin/sync-manuscript-submodules.py` and explicitly configured for this path in
`settings/manuscript-submodules.json`. Both `arrive` and `depart` reach it
through `sync-active.sh`. Arrival fast-forwards compatible clean Overleaf
history and records only its verified published pointer in a local parent
commit. Departure publishes clean linear manuscript `main` commits before
pushing the parent pointer. No manuscript source is auto-committed. Dirty
files, staged pointers, unexpected branches/URLs, unfinished operations,
unpublished detached work, and divergent histories are preserved and
reported; arrival also leaves unpublished manuscript commits for explicit
publication or departure. The manuscript is excluded from the generic
checkout of older parent pins. MCQMC26 remains a GitHub parent, not a
whole-repository Overleaf mirror.

The update is installed on M3 and published in SharedConfigs at `d836cc6`.
Other Macs receive it through their normal infrastructure refresh; preserve
local infrastructure edits if that refresh reports a deferred update.
Offline sync tests cover migration from the older tracked-file folder as
well as dirty/divergent work and publication failures.
Anders can leave `[Codex: Please ...]` notes in tracked manuscript sources.
Routine sync reports filenames and counts; during manuscript work and
Checkpoint, inspect and address these as coauthor feedback under `AGENTS.md`.
They are not executed by the sync scripts, and fetching a note is not
completion of the request.

### Scientific review

Review it with Anders, starting with the permutation-only Newo theorem in
Section 4 and the author agenda above the abstract
(`sections/author-questions.tex`). Keep the agenda at the front. Anders will
investigate the newer Kronecker CBC (question 2). Question 3 asks which code
produced the historical comparison figures and whether it can be rerun with
the paper's discrepancy convention. Question 4 compares methods on their first
$n$ points for varying $n$, including sizes between powers of two. Fred confirmed on October 29 that
the theoretical $\pi$ family must have infinite precision. Anders's October 28
SURE edit (`1daf4d6`) already uses infinite suffixes and absorbs the unused
output tail into a common shift on each finite prefix. The draft now follows
that formulation; question 1 concerns review of the common-tail reduction
and specification of the finite-precision implementation. Do not revert the
theory to a sample-size-dependent digit cutoff. Do not add a tree presentation.
The framework also records Fred's coordinate-reflection observation:
reflecting all points in any fixed coordinate leaves every prefix's
shift-averaged periodic-kernel discrepancy and the weighted loss unchanged.
The proof uses the symmetry of $B_2$; exact rational-node checks include all
coordinate subsets and the zero/one endpoint. This also gives componentwise
sign symmetry for the lattice and Kronecker generating vectors.
Author action 6 records the search reduction: with finite-horizon lattice
modulus $L=2^M\ge N$, retain odd representatives $1\le h_j\le L/2$;
this is $N/2$ only when $N=L$. For Kronecker generators, review the
candidate family's use of representatives $\zeta_j\in[0,1/2]$ under
$\zeta_j\sim1-\zeta_j$. Implementation verification remains open.
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
as Fred specified on October 28 (provisional). The plenary draft now provides
the broader context and is cited in the special-session introduction.

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
