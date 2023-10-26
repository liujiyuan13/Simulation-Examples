'''
Created on 2019年12月18日

@author: liqun
'''

from scipy import stats
import math

def GetE(values):
    e = 0.0
    for v in values:
        e = e + v
    e = e / len(values)
    return e

def GetS(values):
    e = GetE(values)
    s = 0.0
    for v in values:
        s = s + (v - e) * (v - e)
    s = s / (len(values) - 1)
    return math.sqrt(s)

def GetSE(values):
    s = GetS(values)
    return s / math.sqrt(len(values))

def GetH(values,alpha):
    s = GetS(values)
    print("S = %g"%(s))
    t = stats.t.ppf(1-alpha/2, len(values) - 1)
    print("T = %g"%(t))
    return t * s / math.sqrt(len(values))

def GetNR(values,alpha,e):
    s = GetS(values)
    print("S = %g"%(s))
    n = stats.norm.ppf(1-alpha/2)
    print("N = %g"%(n))
    r = n * s / e;
    return r * r

def GetTR(s,alpha,e,r):
    t = stats.t.ppf(1-alpha/2,r-1)
    tr = t * s / e;
    print("R = %g T = %g TR = %g"%(r,t,tr * tr))
    return tr * tr

def GetR(values,alpha,e,R):
    s = GetS(values)
    r = math.ceil(R)
    tr = GetTR(s,alpha,e,r)
    
    while r < tr:
        r = r + 1
        tr = GetTR(s,alpha,e,r)
    return r