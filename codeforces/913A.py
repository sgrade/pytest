# A. Modular Exponentiation

n = int(input())
m = int(input())

# Editorial - https://codeforces.com/blog/entry/56992

print(m if n >= 27 else m % (2 ** n))
