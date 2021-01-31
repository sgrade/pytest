# All prime factors (divisors) of a number

# Algorithm used in this file
# https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

from math import sqrt


def prime_factors(n):
    output = list()
    if n == 0 or n == 1:
        return output
    while n % 2 == 0:
        output.append(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            output.append(i)
            n //= i
    if n > 2:
        output.append(n)
    return output


print(prime_factors(30))
