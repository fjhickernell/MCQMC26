# MCQMC26 repository guidance

## Project scope

This repository is the working home for Fred J. Hickernell's MCQMC 2026
materials:

- the plenary and special-session slide decks;
- LaTeX proceedings manuscripts developed from those decks;
- the computations, figures, tables, references, and supporting material shared
  by the talks and manuscripts; and
- links to closely related work, including the MCQMC 2026 paper coauthored with
  Aadit Jain and others once its authoritative link is available.

The repository is not limited to the conference website or completed talk
slides. Preserve the finished decks while developing the manuscripts from the
same scientific sources.

## Authoritative sources and structure

- `slides/Plenary_MCQMC2026.qmd` is the source for the plenary deck.
- `slides/SpecialSession_MCQMC2026.qmd` is the source for the special-session
  deck.
- Put proceedings manuscript sources under `manuscripts/`, with a separate,
  clearly named subdirectory when there is more than one manuscript.
- Write the proceedings manuscripts in LaTeX. The official conference LaTeX
  macros are still pending; do not treat a provisional class, style, or macro
  file as authoritative. Keep manuscript content sufficiently separated from
  temporary formatting support that the official macros can be adopted with
  minimal rewriting when they arrive.
- Keep reusable computations in `notebooks/`, reusable images and bibliography
  material in `assets/`, and shared presentation or publication support in the
  appropriate project configuration or script.
- Treat `conference/` as source/reference material from the conference and the
  earlier LaTeX slide workflow; do not silently replace current Quarto sources
  with those files.
- `classlib` and `qmcsoftware` are Git submodules. Do not edit or advance their
  pinned commits incidentally. When an intentional change is required, validate,
  commit, and publish the submodule first, then update the parent pointer.

## Slide-to-manuscript alignment

Each proceedings manuscript should remain recognizably aligned with its source
deck while supplying the detail that a paper requires.

- Identify the source deck in the manuscript directory's README or project
  metadata.
- Preserve the deck's principal question, terminology, notation, claims, and
  main narrative unless the manuscript explicitly documents a correction or a
  deliberate extension.
- Expand compressed slide arguments into self-contained definitions,
  derivations, evidence, qualifications, and citations. Do not merely transcribe
  slide bullets.
- Reuse a common computation or artifact when a slide and manuscript make the
  same claim. Avoid independent copies that can silently diverge.
- When results are regenerated, check every affected deck and manuscript for
  consistent numbers, captions, notation, and conclusions.
- Keep manuscript-only depth out of the finished decks unless a slide revision
  is intentional. Alignment does not require identical prose or identical
  levels of detail.
- Record substantive differences between a manuscript and its source deck,
  especially corrected results or changed conclusions.

## Scholarly integrity

- Do not invent citations, bibliographic metadata, author order, affiliations,
  theorem attributions, numerical results, or the URL for related work.
- Do not invent, reconstruct, or silently substitute for the official
  proceedings LaTeX macros while they are pending. Clearly label any temporary
  local build support as provisional.
- Use an authoritative publication, preprint, DOI, or conference page for the
  Aadit Jain coauthored-paper link. Add it only after the user supplies it or it
  has been verified.
- Preserve the authorship and acknowledgment language appropriate to each
  manuscript; do not infer that all talk contributors are manuscript authors or
  vice versa.
- Distinguish reproduced results from newly computed results and retain enough
  provenance to reproduce figures and tables.

## Editing and validation

- Follow existing terminology and macros from the decks and shared Hickernell
  Academic Library metadata unless an intentional correction is documented.
- Prefer small, reviewable source changes. Do not commit generated Quarto build
  trees or notebook caches excluded by `.gitignore`.
- After changing a deck, render the nested `slides` project and inspect the
  affected slides. The pre-render scripts refresh shared slide artifacts.
- After changing a manuscript, compile the complete LaTeX manuscript and
  inspect citations, cross-references, figures, tables, equations, and
  pagination. Check conference-template compliance after the official LaTeX
  macros become available; until then, report that validation as pending rather
  than claiming compliance.
- After changing shared computations or artifacts, run the relevant notebook or
  script and render all affected outputs.
- For changes to the root website or navigation, render the root Quarto project
  and verify its links to both decks and any published manuscript outputs.

## Handoff documentation

Keep `README.md` accurate as the public overview and entry point. When
manuscript directories are added, document their source decks, build commands,
and current status close to their sources. Add a concise project handoff file
only when ongoing manuscript work creates operational state that cannot be
reconstructed from the sources and README.
