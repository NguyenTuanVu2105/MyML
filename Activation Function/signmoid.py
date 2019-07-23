import math

"""
f(x) = 1 / (1 + exp(-x))
"""


def signmoid(data):
    result = []
    for x in data:
        result.append(1 / (1 + math.exp(-x)))
    return result
