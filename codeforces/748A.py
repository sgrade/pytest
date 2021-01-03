# A. Santa Claus and a Place in a Class

n, m, k = map(int, input().split())

r = k // (2 * m)
if k % (2 * m) != 0:
    r += 1

d = (k - (r - 1) * 2 * m) // 2
if (k - (r - 1) * 2 * m) % 2 != 0:
    d += 1

s = "L" if k % 2 != 0 else "R"

print(r, d, s)
