
def finding_the_largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n = n // factor

        else:
            factor +=1

    return n


print(finding_the_largest_prime_factor(600851475143))