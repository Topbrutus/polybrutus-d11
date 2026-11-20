# Polybrutus D11 - 16 vertices, 120 exact squared distances

**Frozen predecessor:** `Topbrutus/polybrutus-d10@v0.1.0`, commit `dc2a45522e5e6794742b8a43de6c105a475d1e89`, Zenodo DOI `10.5281/zenodo.24408569`.

## Exact coordinate rule

At unit radius `R=1`, the prior D10 exact coordinates `p1,...,p15` occupy eleven storage coordinates, including one linear relation in the five-simplex storage block. Define `p'_i=(p_i,0)`, for `i=1,...,15`. Define the new sixteenth vertex `p'_16=e_12=(0,...,0,1)` in the 12th storage coordinate.

All existing labels and positions are preserved. The new unit vector is orthogonal to every old vertex, so `d²(p'_i,p'_16)=2`. For an arbitrary radius `R>0` multiply all point coordinates by `R`; then new `d²=2R²`.

### Exact results

- N=16, labelled pairs L=120; 105 old distances preserved, 15 new ones.
- Minimal Euclidean affine dimension=11, not the 12 storage coordinates.
- Sum of `d²/R²=1007/4`.
- Histogram for `k=4d²/R²`:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Count | 6 | 2 | 89 | 3 | 10 | 6 | 2 | 2 |

- At R=1 the exact centroid in storage coordinates is `(0,0,1/32,0,0,0,0,0,1/16,1/16,1/16,1/16)`.

### Ideal graph-model spectrum

Using equal-mass, complete graph coupling `w_ij=1/d_ij²`, the 16-by-16 weighted Laplacian is

```
L11 = [ L10 + (1/2) I15      -(1/2) 1 ]
      [ -(1/2) 1^T              15/2 ]
```

The exact polynomial `chi16(z) = z(z-8)^5(z-15/2)^4 f6(z-9/2)` with `f6(z)=chiP7(z)/z` gives five modes at `8`, four at `15/2`. This is a chosen mathematical graph model, not a physical measurement.
