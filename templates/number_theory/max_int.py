import math

x = math.inf
print(x)
# Output: inf
print(min(10000000000, x))
# Output: 10000000000

from sys import maxsize

print(maxsize)
# Output: 9223372036854775807
