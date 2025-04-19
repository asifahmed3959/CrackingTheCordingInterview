from itertools import combinations
from math import isqrt

# Simple prime checker
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, isqrt(n)+1, 2):
        if n % i == 0:
            return False
    return True

# Check if two primes concatenate to form primes in both orders
def is_concat_prime(p1, p2):
    return is_prime(int(f"{p1}{p2}")) and is_prime(int(f"{p2}{p1}"))

# Store checked pairs to avoid redundant checks
concat_prime_cache = {}

def valid_pair(p1, p2):
    key = (p1, p2)
    if key not in concat_prime_cache:
        concat_prime_cache[key] = is_concat_prime(p1, p2)
    return concat_prime_cache[key]

# Build up groups
def find_prime_set(size=5, limit=10000):
    primes = [2]
    for num in range(3, limit, 2):
        if is_prime(num):
            primes.append(num)

    sets = [[p] for p in primes]

    for i in range(1, size):
        new_sets = []
        for s in sets:
            for p in primes:
                if p > s[-1] and all(valid_pair(p, q) for q in s):
                    new_sets.append(s + [p])
        sets = new_sets
        if not sets:
            break

    # Find set with smallest sum
    min_set = min(sets, key=sum)
    return min_set, sum(min_set)

# Run it
prime_set, total = find_prime_set()
print("Prime Set:", prime_set)
print("Sum:", total)