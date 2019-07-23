import math

"""
f(x) = x if x>=0
     = alpha * (exp(x) - 1) if x<0
"""


def eLU(data, alpha=0):
    result = []
    for x in data:
        result.append(x if x >= 0 else alpha * (math.exp(x) - 1))
    return result
