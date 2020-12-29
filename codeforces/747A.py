# A. Display Size

from math import sqrt

n = int(input())
a = int(sqrt(n))

while a > 0:
    if n % a == 0:
        break
    else:
        a -= 1

print(a, n // a)
