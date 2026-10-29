# Special-session proceedings manuscript

Working title: **Component-by-Component Constructions of Kronecker and Lattice
Sequences Which Are Good for Arbitrary Sample Sizes**.

This is the special-session paper, separate from the Aadit coauthored paper
and the future plenary paper. The maximum is **16 pages including references**
for planning purposes. The current discussion draft is 12 pages using the MCQMC 2024 template
files from the Aadit paper (`svproc.cls`, `spmpsci.bst`) and the same
Times text/math packages. Fred requested this format for both new papers
on October 28. Any additional MCQMC 2026 submission requirements still need
to be checked.
Current authors, in order: **Alexander Pride and Fred J. Hickernell**
(as specified by Fred on October 28, 2026; provisional).

## Sources and deliberate extensions

- Backbone: `../../slides/SpecialSession_MCQMC2026.qmd`.
- Original abstract: `../../conference/Hickernel_Special_Session_talk.tex`.
- Shared numerical artifacts: `../../notebooks/artifacts/figures/`; figures are
  referenced in place, not copied or regenerated for this draft.
- New material: the SURE 2025 notes by Anders Pride, especially the newer
  `Owen vs new scramble notes.tex`, with a direct digit-permutation (`pi`)
  proof. Fred specifically requested no tree presentation.
- The draft narrows the talk's broad motivation to CBC and the weighted sum
  of expected squared discrepancies (WSESD). It distinguishes arbitrary
  prefixes from arbitrary missing observations, fixes the slides' definition
  of difference multiplicities to count ordered pairs, and includes exact
  finite-horizon formulas and a concise Newo invariance argument.
- The slide's accelerated lattice CBC complexity is not asserted without an
  implementation and supporting derivation. The direct candidate search is
  specified explicitly instead.

The newer Kronecker CBC is **not yet sourced**: the new Overleaf notes contain
Newo material but no Kronecker construction, and the local QMCPy source only
provides a stored CBC vector. Section 5 has a derived generic finite-candidate
CBC and a visible request for Anders's distinct newer algorithm. Do not
conflate it with the historical `ANDERS_CBC` comparison.

## Edit and build

Edit `main.tex` and the files in `sections/`. Dark-green `\codex{[...]} ` comments mark unresolved scientific or
editorial questions, matching the Cones-paper convention. Most draft prose is black;
this is a new manuscript, not a redline of the Aadit paper.

From this directory:

```sh
latexmk -pdf main.tex
python3 scripts/check_formulas.py
```

The compiled preview is `build/main.pdf`; all build outputs are ignored.
The formula check uses only Python's standard library. It independently
compares exact dyadic difference counts, 1,240 random-Newo difference rows,
odd-multiplier carries, lattice weighted sums, and the Kronecker harmonic
formula against small direct calculations. These checks supplement the proofs;
they do not validate the historical large-horizon figures.

## Before the discussion with Anders

Read Section 4 (Newo) and the questions at the end. Priorities are:

1. Confirm the `pi` definition, common scalar scrambling before multiplication,
   every-prefix invariance, precision convention, and attribution.
2. Supply the newer Kronecker CBC's candidate family, objective, update rule,
   computational cost and available guarantees.
3. Locate and validate the implementation behind the slide figures; then
   decide which new experiments belong in the paper.
4. Review result attribution and a final outline within 16 pages.

A working final-page budget is: introduction 1.5, kernel framework 2,
lattice CBC 2, Newo 2.5, Kronecker CBC 2.5, experiments 2.5,
conclusion 0.5, references 1.5, leaving 1 page for title/format variation.
Revise this budget once the official template is available.

See `SOURCE_PROVENANCE.md` for versions, figure caveats, and source mapping.
