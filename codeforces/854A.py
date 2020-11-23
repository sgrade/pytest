# A. Fraction

from math import floor

n = int(input())

if n % 2 == 0:
    numerator = n // 2 - 1
else:
    numerator = floor(n // 2)
denominator = n - numerator

found = False
while not found:
    for i in range(2, numerator + 1):
        if numerator % i == 0 and denominator % i == 0:
            numerator -= 1
            denominator += 1
            break
    else:
        found = True

print(numerator, denominator)
