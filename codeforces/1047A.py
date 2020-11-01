# A. Little C Loves 3 I

n = int(input())
a = b = 1
c = n - 2
if c % 3 == 0:
    c -= 1
    b += 1
print(a, b, c)
