# Polybrutus 11D: Exact Conservative Metric Completion and a Fivefold Spectral Mode

**Author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** November 20, 2026  
**Version:** 0.1.0  
**Publication type:** Mathematical computational preprint; no human peer review  
**Predecessor:** [Polybrutus 10D, DOI 10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569)  
**Tagged code:** [Topbrutus/polybrutus-d11, source v0.1.0](https://github.com/Topbrutus/polybrutus-d11/tree/v0.1.0) (when publicly released).

## Abstract

We construct a new, exact **16-point labelled Euclidean metric** with minimal affine embedding dimension **11**, preserving all **105 predecessor distances** from the earlier published Polybrutus 10D configuration without moving any original point. A single new orthogonal unit vector produces **15 additional distances**, each with squared value `2R²`. The complete resulting metric has **120 pairwise distances** in eight exact families. Two independently implemented SymPy/rational-arithmetic programs verify the labelled metric, exact rank, centered squared-distance Gram matrix and positive-semidefinite factorization.

For an expressly chosen **ideal scalar-oscillator graph** with complete pairwise couplings `w_ij=R²/d_ij²`, we derive the exact characteristic-polynomial recurrence and verify **a fivefold Laplacian eigenvalue at 8** and **a fourfold eigenvalue at 15/2**. The result is a mathematical graph-model property, **not** a measured mechanical frequency, new physical dimension, or a novel universal theorem.

## 1. Provenance: preserving canonical Polybrutus

Polybrutus began with seven analytically defined points on a radius-R sphere in three dimensions. Orthogonal completion with five vertices of a regular four-dimensional simplex created the published 7D configuration, with **12 vertices and 66 pair distances**: [DOI 10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952).

The published 8D record contains **13 vertices, 78 pairs** ([DOI 10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344)); the published 9D case **14 vertices, 91 pairs** ([DOI 10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448)). The published 10D certificate has **15 vertices, 105 labelled pairs, rank 10** ([DOI 10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569)).

This 11D study starts from the **exact, frozen GitHub source tag** of its 10D predecessor: `Topbrutus/polybrutus-d10`, tag `v0.1.0`, source commit `dc2a45522e5e6794742b8a43de6c105a475d1e89`. The relevant source code and distance certificates are included unchanged as the local `prior/` audit chain.

## 2. Construction of the sixteen-point metric

Normalize radius `R=1`. Denote the fifteen previous exact vectors by `p1,...,p15` in an 11-slot storage representation that already includes the centered-simplex single linear constraint. Define `p_i'=(p_i,0)` for each `1<=i<=15`; append the new orthogonal unit vector

```
p_16' = e_12 = (0,0,0,0,0,0,0,0,0,0,0,1).
```

Every old labelled point is unchanged, apart from appending zero. Since `p'_16` is orthogonal to every old vector and all vectors lie on the unit sphere,

```
||p'_16 - p'_i||² = ||p'_16||² + ||p'_i||² = 2,
i = 1,...,15.
```

There are exactly `105+15 = 120 = 16 choose 2` distinct unordered labelled pairs. Scaling every coordinate by `R>0` multiplies all squared distances by `R²`, leaving rank and normalized families unchanged.

For `k=4d²/R²`, the exact squared-distance histogram is:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **89** | 3 | 10 | 6 | 2 | 2 |

This sums to **120**; the complete sum of squared distances is

```
sum_{i<j} (d_ij²/R²) = 1007/4.
```

At unit radius, the centroid in the 12 storage slots is exactly

```
G = (0,0,1/32,0,0,0,0,0,1/16,1/16,1/16,1/16).
```

The five-simplex-vertex coordinate block has a single constraint. Thus **12 storage coordinates do not represent twelve intrinsic affine dimensions**.

## 3. Exact proof of affine dimension eleven

Write the 16-by-16 squared-distance matrix as `D=(d_ij²)`, the coordinate array as `X` with 16 rows, and let `H=I-11^T/16` be the centering matrix. The centered Euclidean distance Gram matrix is

```
B = -1/2 H D H.
```

Exact symbolic computation establishes simultaneously:

```
rank([p'_2-p'_1, ..., p'_16-p'_1]) = 11;
rank(B) = 11;
B = (H X)(H X)^T.
```

The final equality is an **exact positive-semidefinite factorization**, not a floating-point argument. Every Euclidean realization of this *labelled* set of 120 squared distances must share the same centered Gram matrix, whose rank is eleven. Hence its minimal affine Euclidean embedding dimension is precisely **11**. This does not imply that physical spacetime contains eleven dimensions.

The source certificate provides **all 120 labelled squared distances**; the independent rational reconstruction reproduces each entry and preserves the prior 105/105 distances exactly. Four deliberate corruption controls catch a changed distance, a repeated vertex, a nonorthogonal inserted vector, and a relabelling that leaves the unlabelled distance histogram unchanged.

## 4. Weighted graph Laplacian: an exact fivefold mode

To investigate model dynamics, define a hypothetical complete graph on the 16 points, with unit-mass scalar displacements and pairwise elastic couplings proportional to `w_ij=1/d_ij²`. The graph Laplacian `L` is not extracted from an observed apparatus; its weights are a modelling choice.

For the new vertex all fifteen couplings equal `1/2`. If `L10` denotes the old 15-vertex graph Laplacian, the new 16-vertex Laplacian obeys

```
L11 = [ L10 + (1/2) I15      -(1/2) 1 ]
      [ -(1/2) 1^T              15/2 ].
```

Writing `chi15(z)=det(zI-L10)` and `chi16(z)=det(zI-L11)`, a symmetric-mode decomposition gives

```
chi16(z) = z(z-8) chi15(z-1/2)/(z-1/2).
```

The previously published D10 certificate gives

```
chi15(z) = z(z-15/2)^4(z-7)^4 f6(z-4),
f6(z) = chiP7(z)/z,
```

where `chiP7(z)` is the characteristic polynomial of the original seven-point weighted Laplacian, and `f6` its factor of six nonzero modes. Therefore the new identity is

```
chi16(z) = z(z-8)^5(z-15/2)^4 f6(z-9/2).
```

The main verifier computes **the full exact 16-by-16 characteristic polynomial** and proves equality with the formula. It verifies `f6(7/2)!=0` and `f6(3)!=0`, ensuring the two designated eigenvalues have **exact** multiplicities: `8` occurs **five times**, and `15/2` occurs **four times**.

The second independent checker reconstructs all weights from a separately derived rational metric, computes the characteristic polynomial, and proves the multiplicities using its derivatives. This provides an independently reproducible **dimension-specific ideal graph spectrum**, not physical resonance measurements in hertz.

## 5. Reproducibility and audit

The archived GitHub release includes:

- `src/verify_d11.py` - exact coordinates, Gram, complete labelled distances, closed-form graph spectrum, four adversarial controls.
- `tests/independent_d11.py` - separately derived rational metric, parent comparison and polynomial derivative checks, importing **no generator**.
- `results/certificate_d11.json` - 120 exact labelled pair entries, the histogram, rank and model polynomial.
- `prior/` - full frozen 10D, 9D and 8D source chain, including exact predecessor certificates.
- `PREUVE_D11.md`, `SPECIFICATION_D11.md`, `PROVENANCE.md`, `SHA256SUMS.txt`, workflow for GitHub Actions.

To rerun the exact computations:

```
python -m pip install sympy==1.14.0
python src/verify_d11.py
python tests/independent_d11.py
```

The source release is frozen at the tagged commit. The Zenodo deposit also includes this PDF and a copy of the JSON certificate. Hashes and source provenance prevent a changed working tree from being silently substituted for the original research artefact.

## 6. Scientific and physical scope

This is a **particular exact completion** of a labelled Euclidean metric and an associated **chosen** oscillator network. Orthogonal extensions and uniform graph attachments are mathematical techniques with existing antecedents. A new dimension label does not in itself constitute a new physical dimension, a newly discovered universal mathematical theorem, a new Higgs state, or a new physical frequency. **No human peer review has been conducted.**

The computation is a reproducible case study; its mathematical delta from 10D is the precisely characterized fivefold eigenvalue at 8 in a controlled 16-vertex graph model. It does not establish a new physics law.

## 7. Author, credit and AI disclosure

**Research author and scientific responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher. The Polybrutus canonical geometry, research programme and publishing decisions originate with the human researcher.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted in symbolic calculations, software implementation, design of a separate rational verification program, graph-model analysis, reproducibility, source auditing and technical writing. The AI is **not listed as an author**. The work has not been independently reviewed by human specialists.

**Licensing:** research paper CC BY 4.0; source programs MIT.

**Prior sources:** [canonical Polybrutus seven-point specification](https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md); [Polybrutus 7D](https://doi.org/10.5281/zenodo.24407952); [Polybrutus 8D](https://doi.org/10.5281/zenodo.24408344); [Polybrutus 9D](https://doi.org/10.5281/zenodo.24408448); [Polybrutus 10D](https://doi.org/10.5281/zenodo.24408569); [immutable D10 source tag](https://github.com/Topbrutus/polybrutus-d10/tree/v0.1.0).
