from math import sqrt

sum_prime = 0
start = 2

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False

    return True

two_mill = 2 * (10 ** 6)

while sum_prime < two_mill:
    if is_prime(start):
        sum_prime += start
    start += 1


print(sum_prime)
