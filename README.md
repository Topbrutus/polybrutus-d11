# POLYBRUTUS 11D - Exact conservative metric and fivefold model spectral mode

## Officially published and verified

- **Official Zenodo DOI:** [10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650); [public record 24408650](https://zenodo.org/records/24408650).
- **Frozen source tag:** [`v0.1.0`](https://github.com/Topbrutus/polybrutus-d11/tree/v0.1.0) at commit `b49252a03760ea55301b15a60df3c7317f8e3160`.
- **GitHub CI:** [exact + independent D11 proof](https://github.com/Topbrutus/polybrutus-d11/actions/runs/44840058390) (`success` on frozen source commit).
- **Zenodo source files:** frozen tag ZIP, four-page mathematics PDF and certificate of all 120 squared labelled distances; file integrity verified by public API.
- **Scientific scope:** a reproducible model computation, not independently peer-reviewed and not a claim about 11 physical spacetime dimensions.


**Research author and scientific responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Status:** Exact computational mathematics, preprint, not independently peer reviewed.  
**AI disclosure:** OpenAI ChatGPT (Astra) assisted derivation, coding, verification, scientific note and publication operations. AI is not an author.

## Summary of independently verified properties (R=1)

- **16** labelled points, **120** squared pairwise distances, exact **affine rank 11**.
- Retains **105/105** labelled squared distances from immutable Polybrutus 10D source tag.
- Adds **15** squared distances of value **2**, by one unit vector orthogonal to the full old linear span.
- Normalized distance histogram `k=4d²/R²` is `{4:6,7:2,8:89,9:3,10:10,12:6,13:2,16:2}`.
- Total sum `sum(d²/R²) = 1007/4`.
- Intrinsic rank established independently by coordinate differences, centered Euclidean squared-distance Gram matrix and the exact PSD identity `B=(HX)(HX)^T`.
- Ideal complete weighted-Laplacian model `w_ij=R²/d²`: eigenvalue **8** of exact multiplicity **5**, eigenvalue **15/2** of multiplicity **4**. Two distinct programs check these modes.
- Four deliberate corruption controls confirm that labelled metric validation catches corrupt data and label swaps.

## Full verification

```sh
python -m pip install sympy==1.14.0
python src/verify_d11.py
python tests/independent_d11.py
```

The independent verifier uses rational rules and **does not import the main generator**. `prior/` contains the complete immutable D10 baseline code and exact certificate, plus previous 8D/9D sources needed to regenerate the D10 coordinates. The complete new 120-pair matrix and metadata are in `results/certificate_d11.json`.

## Documentation and archive

- `SPECIFICATION_D11.md` - exact coordinate construction.
- `PREUVE_D11.md` - algebraic proof of minimal affine rank and spectral identity.
- `PROVENANCE.md` - source chain from canonical Polybrutus.
- `publication/POLYBRUTUS_11D_NOTE.pdf` and `.md` - mathematical preprint (CC BY 4.0).
- `src/` and `tests/` - MIT-licensed exact mathematics and independent checkers.
- `SHA256SUMS.txt` - SHA-256 of Git blobs in the pinned source tag.

## Prior publications

- Canonical 7-point Polybrutus: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md
- 7D: https://doi.org/10.5281/zenodo.24407952
- 8D: https://doi.org/10.5281/zenodo.24408344
- 9D: https://doi.org/10.5281/zenodo.24408448
- 10D (the frozen parent): https://doi.org/10.5281/zenodo.24408569
- Parent GitHub tag: https://github.com/Topbrutus/polybrutus-d10/tree/v0.1.0

**Limitations:** orthogonal join methods and Laplacian shifts are established mathematics. This study does not claim a new universal theorem or an eleventh physical spacetime dimension; the oscillator model has not been built or measured.
