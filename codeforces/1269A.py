# A. Equation

from math import sqrt, inf


def is_prime(n):
    if n <= 1:
        return False
    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False
    return True


n = int(input())
i = n+1
while True:
    if not is_prime(i) and not is_prime(n+i):
        print(n+i, i)
        break
    i += 1
