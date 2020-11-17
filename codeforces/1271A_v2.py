# A. Suits
# Based on https://codeforces.com/contest/1271/submission/74211958

a, b, c, d, e, f = [int(input()) for _ in range(6)]
x = min(a, d)
y = min(b, c, d)
print(max(x * e + min(b, c, d - x) * f, y * f + min(a, d - y) * e))
