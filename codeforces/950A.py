# A. Left-handers, Right-handers and Ambidexters

l, r, a = map(int, input().split())

x = min(l, r)
l -= x
r -= x

y = min(max(l, r), a)
a -= y

print((x + y + a // 2) * 2)
