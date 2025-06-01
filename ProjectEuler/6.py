from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(target):
    count = 0
    num = 1
    while count < target:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(nth_prime(10001))
