import sympy as sy
import numpy as np
from sympy.physics.quantum import TensorProduct
from fractions import Fraction
class ReturnValue(object):
    def __init__(self, x, y, z, p, m):
        self.x = x
        self.y = y
        self.z = z
        self.p = p
        self.m = m

def angular_momentum(n,m):
    if int(m)>2 | int(m)<1:
        print("Oops!  denominator must be 1 oer 2")   
        return 

    s = Fraction(int(n),int(m))
#  certainly integer and rational, respectively
    m, s2 = int(2*s+1), s*(s+1)
   
    Sz = sy.Matrix.zeros(m)
    Sp = sy.Matrix.zeros(m)
    Sm = sy.Matrix.zeros(m)

    for mm in np.arange(-s,s+0.1): # -s, -s+1, ... s
        k = int(mm + s) # 0, 1, ..., 2*s
        Sz[k,k] = mm
        if mm!=s: 
            Sp[k,k+1] = sy.sqrt(s2-mm*(mm+1))
            Sm[k+1,k] = sy.sqrt(s2-mm*(mm+1))
    Sx = (Sp+Sm)/2
    Sy = (Sp-Sm)/2/sy.I
    return ReturnValue(Sx,Sy,Sz,Sp,Sm)
