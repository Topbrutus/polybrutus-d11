#!/usr/bin/env python3
"""Independent Polybrutus D11 certificate from rational squared-distance rules.

Does not import any parent or current symbolic generator. Reconstructs
the labelled 120-pair metric from the original seven rational (x/sqrt3,y,z)
components, the five-point simplex distances, and four orthogonal unit axes.
"""
import hashlib,json
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d11.json").read_text(encoding="utf8"))
parent=json.loads((ROOT/"prior"/"certificate_d10.json").read_text(encoding="utf8"))
base=[
 (F(0),F(0),F(1)),
 (F(1,2),F(0),F(1,2)),
 (F(-1,4),F(3,4),F(1,2)),
 (F(-1,4),F(-3,4),F(1,2)),
 (F(0),F(0),F(-1)),
 (F(1,2),F(0),F(-1,2)),
 (F(-1,2),F(0),F(-1,2))
]
def d2(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        a,b,c=(base[i][k]-base[j][k] for k in range(3))
        return 3*a*a+b*b+c*c
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

edges=list(combinations(range(16),2))
independent={(i+1,j+1):d2(i,j) for i,j in edges}
claimed={(int(e["i"]),int(e["j"])):F(e["d2"]) for e in report["labelled_squared_distances"]}
assert len(independent)==120 and independent==claimed
old={(int(e["i"]),int(e["j"])):F(e["d2"]) for e in parent["labelled_squared_distances"]}
assert len(old)==105 and all(independent[k]==v for k,v in old.items())
assert all(d2(i,15)==F(2) for i in range(15))
hist=Counter(4*d2(i,j) for i,j in edges)
assert hist==Counter({F(4):6,F(7):2,F(8):89,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(independent.values(),F(0))==F(1007,4)
assert all(v>0 for v in independent.values())
D=sp.Matrix(16,16,lambda i,j:sp.Rational(d2(i,j).numerator,d2(i,j).denominator))
H=sp.eye(16)-sp.ones(16)/16
assert (-H*D*H/2).rank()==11
D10=D[:15,:15]
H10=sp.eye(15)-sp.ones(15)/15
assert (-H10*D10*H10/2).rank()==10

L=sp.zeros(16)
for i,j in edges:
    w=1/D[i,j];L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
z=sp.Symbol("z");chi=L.charpoly(z).as_expr()
for root,mult in [(sp.Integer(8),5),(sp.Rational(15,2),4)]:
    assert all(sp.simplify(sp.diff(chi,z,k).subs(z,root))==0 for k in range(mult))
    assert sp.simplify(sp.diff(chi,z,mult).subs(z,root))!=0
assert report["affine_rank"]==report["centered_gram_rank"]==11
assert report["parent_distances_preserved"]==105 and report["new_distances"]==15
p=ROOT/"results"/"certificate_d11.json"
print("INDEPENDENT D11 PASS: 120 exact rational squared distances, 105 previous preserved, Gram rank 11")
print("INDEPENDENT SPECTRAL PASS: eigenvalue 8 x5, eigenvalue 15/2 x4")
print("CERTIFICATE_SHA256="+hashlib.sha256(p.read_bytes()).hexdigest())
