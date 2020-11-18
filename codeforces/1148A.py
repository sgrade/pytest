# A. Another One Bites The Dust

a, b, c = map(int, input().split())
x = min(a, b, c)
a -= x
b -= x
c -= x

x *= 4

y = a * 2 if a == b else min(a, b) * 2 + 1

print(x + y + c * 2)
