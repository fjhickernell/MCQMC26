# MCQMC 2026 Talks and Proceedings Manuscripts

This repository contains the slides, proceedings-manuscript sources, and
supporting material for my contributions to the

[17th Annual International Conference on Monte Carlo and Quasi-Monte Carlo Methods in Scientific Computing](https://maths.ed.ac.uk/events/mcqmc-2026)

For more information, go to 

https://fjhickernell.github.io/MCQMC26/

The proceedings manuscripts will be written in LaTeX and developed in
alignment with the plenary and special-session slide decks. We are awaiting the
official conference LaTeX macros. This repository will also reference a
related MCQMC 2026 paper coauthored with Aadit Jain and others once its
authoritative link is available.

## Manuscripts

- `manuscripts/plenary` is a Git submodule connected to
  [the Plenary Overleaf project](https://www.overleaf.com/project/6ae4101e2b7c96d63cf03bd6),
  containing the draft **Where Quasi-Monte Carlo Theory and Practice Meet**
  by Fred J. Hickernell. It expands the plenary slides and abstract using
  the MCQMC 2024 macros and green Codex review comments. The supplied limit
  is 25 pages; the current draft is 19 pages including references and notes.
  Build with `latexmk -pdf mcqmc2026_plenary.tex` in that directory. Its README and source
  provenance identify the existing slide artifacts and remaining work.
  The special-session paper references this draft for the broader context.
  Fetch Overleaf changes before editing and publish the manuscript before
  its parent pointer, following the same submodule workflow below.

- `manuscripts/special-session` is a Git submodule connected to
  [the Special Session Overleaf project](https://www.overleaf.com/project/6ae39728ff70b39ca2fd98b1), containing the initial draft of
  **Component-by-Component Constructions of Kronecker and Lattice Sequences
  for Arbitrary Sample Sizes**, developed from the
  special-session slides and conference abstract, with the newer SURE 2025
  Newo scrambling material. The maximum is 16 pages; the current discussion
  draft uses the MCQMC 2024 macros from the Aadit paper, as Fred requested.
  Build with `latexmk -pdf mcqmc2026_special_session.tex`
  in that directory; see its README for source provenance and remaining work.
  Fetch Anders's Overleaf edits before local work; publish manuscript commits
  to its Overleaf `origin` before updating this repository's submodule pointer.
  MCQMC26 remains the parent project, retaining its slide, computation, and
  Academic Library connections; it is not itself an Overleaf mirror.

- `manuscripts/aadit-jain-paper` is a Git submodule connected to the separate
  Overleaf repository for the paper coauthored with Aadit Jain and others.
  Commit manuscript changes inside that directory and push its `main` branch to
  `origin` to propagate them to Overleaf. Then commit the updated submodule
  pointer in this repository.
  The active manuscript is `rqmc_kurt_ci_paper.tex`. Dated copies such as
  `rqmc_kurt_ci_paper_2026-10-18.tex` are archival snapshots; make new edits in
  the undated source and preserve the dated files unchanged.

Clone this repository together with its manuscript and library submodules using

```sh
git clone --recurse-submodules https://github.com/fjhickernell/MCQMC26.git
```

Fetching the private Overleaf submodule requires access to the Overleaf project
and an Overleaf Git authentication token. Overleaf Cloud Git access uses HTTPS;
it does not provide an SSH remote.


#### Author

Fred J. Hickernell  
Department of Applied Mathematics  
Illinois Institute of Technology
