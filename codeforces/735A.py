# A. Ostap and Grasshopper

n, k = map(int, input().split())
s = input()

g = s.index('G')
t = s.index('T')

if abs(g - t) % k == 0:
    sign = 1 if g < t else -1
    while g != t:
        if s[g] == '#':
            break
        g += sign * k

if g == t:
    print('YES')
else:
    print('NO')
