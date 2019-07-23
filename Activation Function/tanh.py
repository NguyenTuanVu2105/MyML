import math

"""
f(x) = 2 / (1 + exp(-2x)) - 1
"""


def tanh(data):
    result = []
    for x in data:
        result.append(2 / (1 + math.exp(-2 * x)) - 1)
    return result


print(tanh([1, 5, -4, 3, -2]))
