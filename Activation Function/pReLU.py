import math

"""
f(x) = x if x>=0
     = alpha*x if x<0
"""


def pReLU(data, alpha=0):
    result = []
    for x in data:
        result.append(x if x >= 0 else alpha * x)
    return result

