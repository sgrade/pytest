# A. Suits

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# 1: (a + d) * e
# 2: (b + c + d) * f

ans = 0

if e > f:
    m = min(a, d)
    ans += m * e
    a -= m
    d -= m

elif e < f:
    m = min(b, c, d)
    ans += m * f
    b -= m
    c -= m
    d -= m

else:
    if min(a, b, c, d) == d:
        ans += d * e
        d = 0
    else:
        if a < min(b, c):
            ans += a * e
            a = 0
            d -= a
        else:
            m = min(b, c)
            ans += m * f
            b -= m
            c -= m
            d -= m

if d != 0:
    if a == 0:
        m = min(b, c, d)
        ans += m * f
        b -= m
        c -= m
        d -= m
    else:
        m = min(a, d)
        ans += m * e
        a -= m
        d -= m

print(ans)
