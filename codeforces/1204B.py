# B. Mislove Has Lost an Array

n, l, r = map(int, input().split())

print(n - l + (2 ** l - 1), end = ' ')
print(2 ** (r - 1) * (n - r) + (2 ** r - 1))
