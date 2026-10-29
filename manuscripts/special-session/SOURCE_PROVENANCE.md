# Source and evidence record

## Manuscript backbone

The special-session slide source and conference abstract are in MCQMC26.
The draft was started from local MCQMC26 commit `c750e7c` on October 28, 2026.
No deck or computation was changed to create it.

## SURE notes and synchronization

Source repository:
`~/SoftwareRepositories/SURE-2025-periodic-kernel-discrepancy-for-lattices`.

- GitHub: <https://github.com/fjhickernell/SURE-2025-periodic-kernel-discrepancy-for-lattices>.
- Overleaf: <https://www.overleaf.com/project/684722d943d66ef7fda1a0ea>.
- Previous GitHub-only import: `43764a0`.
- Newer Overleaf snapshot: `1daf4d67d1eb6c9e977363fb9e4364e49167ac72`.
- Initial two-parent reconciliation: `f37fe96`; tracked tree exactly matches
  the newer Overleaf snapshot. Both original histories are retained.
- Verified pairing is registered in SharedConfigs `settings/overleaf-sync.json`,
  with `routine_sync: true`. `arrive`/`depart` use the shared bridge; editing
  either website is not an instantaneous background synchronization trigger.

The newer `Owen vs new scramble notes.tex` has the permutation-only proof in
its theorem `thm:same disc under Newo`, Gray-code specialization, and an
unfinished odd-multiplication derivation. The draft supplies a direct carry
calculation instead of copying that unfinished derivation. It uses a fixed
number M of digits throughout and conditions on a realized Newo map while
averaging over the uniform shift. No tree presentation is used.

The multiplicity and product-update calculations also use
`WSSD_lattice_search.tex` (author: Anders Pride; dated June 2025). A later
`WIP seq char.tex` is supporting source for the multiplicity formulas, not
an invitation to add its tree diagrams. No Kronecker construction appears
in the SURE snapshot examined.

## Shared slide figures

Both figures are reused directly, without alteration:

- `../../notebooks/artifacts/figures/special_d64_lattice_discrepancy.png`
- `../../notebooks/artifacts/figures/special_d64_kronecker_discrepancy.png`

Their generating source is `../../notebooks/MCQMC2026_UQ_Penalty_Example.ipynb`,
zero-based cells 84-104. Settings: d=64, N=2^20, sample-size weights w_n=n,
coordinate weights gamma_j=j^-2, Bernoulli polynomial B2(t)=t^2-t+1/6.
The code plots sqrt(max(ESD,0)). The finite-horizon criterion in this draft
uses the same normalization.

The baseline lattice uses `kuo.lattice-39102-1024-1048576.3600.txt`, and the
searched lattice uses `anders_lattice_vector_d64_n1048576.txt`. The notebook
calls Kronecker choices `ANDERS_CBC`, `SUZUKI`, and `RICHTMYER`.

These figures have **not** been regenerated or independently validated here.
The pinned QMCPy source lacks historical lattice-search interfaces called by
the notebook. A standalone Kronecker discrepancy routine currently calls
`gen_samples`, so its randomization convention must be checked against the
unshifted-difference formula and the actual historical code revision.
Do not infer that the figures are invalid from today's code alone; do not
use their numerical legend values as verified new manuscript results either.
The new finite-horizon checks validate the formulas, not these stored outputs.

## Literature

Initial bibliography entries follow the shared library metadata. The Cools,
Kuo and Nuyens embedded-lattice article was checked against its publisher:
<https://epubs.siam.org/doi/10.1137/06065074X>.
The 2012 weighted-compound article uses Frances Y. Kuo (correcting the shared
metadata's apparent initial typo locally, without changing the library).
Pride's notes are explicitly unpublished working material; no publication
status, coauthor list, or public preprint link is inferred for them.

## Template provenance

At Fred's request on October 28, this paper uses the MCQMC 2024 working
template already used by the Aadit paper. `svproc.cls` and `spmpsci.bst`
are byte-for-byte copies from `../aadit-jain-paper`; the class declares
version 2016/07/20 v1.3. The Aadit source identifies its template as MCQMC 2024.
The draft uses that class's layout and theorem environments, its bibliography
style, and the same `newtxtext` / `newtxmath` font packages, with no custom
margin or font-size reduction. The previous article-format preview is superseded.

## Follow-up search for the newer Kronecker construction

All seven SURE manuscript sources, including both `Old work/` files, were
reviewed for the missing method. `Old work/main.tex` contains explicit CBC
pseudocode (lines 119-145), but it is a lattice construction: radical-inverse
points, odd-integer candidates, first component 1, and the WSSD objective.
`Old work/WIP_rho_n_explanation.tex` derives the dyadic difference counts;
`Sequence characterization.tex` concerns radical-inverse orderings; the brief
overview is an unfinished stub. The remaining three sources provide lattice
multiplicities, lattice CBC updates, and the Newo result. No Kronecker CBC
algorithm was identified. Ask Anders for its write-up or code location.
