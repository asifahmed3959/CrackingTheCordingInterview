def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_pal = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # avoid repeat pairs
            prod = i * j
            if prod <= max_pal:
                break  # no point continuing
            if is_palindrome(prod):
                max_pal = prod
    return max_pal

print(largest_palindrome_product())