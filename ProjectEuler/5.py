from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(n):
    return reduce(lcm, range(1, n+1))


print(smallest_multiple(20))