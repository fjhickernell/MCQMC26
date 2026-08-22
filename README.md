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

- `manuscripts/aadit-jain-paper` is a Git submodule connected to the separate
  Overleaf repository for the paper coauthored with Aadit Jain and others.
  Commit manuscript changes inside that directory and push its `main` branch to
  `origin` to propagate them to Overleaf. Then commit the updated submodule
  pointer in this repository.

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
