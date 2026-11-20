# Polybrutus 11D - Mathematical proof certificate

## 1. Exact labelled distances and affine dimension

Let `p1,...,p15` be the previously certified, radius-one Polybrutus D10 points of minimal affine rank 10. They are unchanged except that a zero coordinate is appended. Add `p16=e12`, orthogonal to their entire linear span. For each `i<=15`, `||p16-p_i||²=1+1-0=2`. Hence the new metric consists of 105 preserved old distances and 15 new distances, i.e. 120 distinct labelled unordered pairs.

For the complete matrix `D` of squared labelled distances, set `H=I-11^T/16` and `B=-HDH/2`. The main exact symbolic program verifies:

```
rank([p2-p1,...,p16-p1]) = 11;
rank(B) = 11;
B = (HX)(HX)^T.
```

The final identity proves PSD exactly (not numerically). The centered Gram matrix is uniquely determined by the labelled squared-distance metric. Consequently **every Euclidean realization of this exact labelled metric has minimal affine dimension 11**, even though the convenient coordinate storage consists of twelve slots subject to one constraint.

The eight normalized families `k=4d²` have counts `{4:6,7:2,8:89,9:3,10:10,12:6,13:2,16:2}`. Their total is 120 and the sum of the squared lengths is `1007/4`.

## 2. Exact characteristic-polynomial identity for a chosen oscillator graph

Choose unit masses and pairwise weights `w_ij=1/d_ij²` for a **hypothetical** scalar displacement oscillator at each vertex. The new point has equal couplings `1/2` to 15 old vertices. Therefore

```
L11 = [ L10 + (1/2) I15     -(1/2) 1 ]
      [ -(1/2) 1^T              15/2 ]
```

If `chi15(z)=det(zI-L10)` is the old monic characteristic polynomial, then

```
chi16(z) = z(z-8) chi15(z-1/2)/(z-1/2).
```

The pinned D10 calculation provides `chi15(z)=z(z-15/2)^4(z-7)^4 f6(z-4)`, where `f6(z)=chiP7(z)/z` contains the six nonzero modes of the original 7-point graph.

Substituting gives

```
chi16(z) = z(z-8)^5(z-15/2)^4 f6(z-9/2).
```

The complete directly computed 16-by-16 exact characteristic polynomial equals the above expression. Further, `f6(7/2) != 0` and `f6(3) != 0`, so the multiplicities are **exactly five** for eigenvalue `8` and **exactly four** for eigenvalue `15/2`. An independent rational metric implementation reconstructs the Laplacian and checks the multiplicities via characteristic-polynomial derivatives without importing the primary source.

## 3. Reproduction and adversarial tests

Both programs verify all 120 distances and the predecessor's 105 distances. Four deliberately invalid variations are rejected: a distance tamper, repeated point, tilted new point and point-label permutation preserving the distance multiset.

**Scope:** This is a mathematical metric and graph model. The orthogonal construction and the graph shift are established operations; neither a new fundamental physical dimension nor a new universal mathematical law is claimed. No human independent scientific peer review has been performed.
