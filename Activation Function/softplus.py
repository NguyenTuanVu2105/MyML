"""
f(x) = loge(1 + exp(x))
"""
import math


def softplus(data):
    result = []
    for x in data:
        result.append(math.log(1 + math.exp(x)))
    return result


print(softplus([1, 5, -4, 3, 2]))
