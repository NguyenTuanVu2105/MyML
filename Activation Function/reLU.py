import math

"""
f(x) = x if x>=0
     = 0 if x<0
"""


def reLU(data):
    result = []
    for x in data:
        result.append(x if x >= 0 else 0)
    return result
