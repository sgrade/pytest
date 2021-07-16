# A. Diplomas and Certificates

n, k = map(int, input().split())

d = n // (2 * (k+1))
s = d * k
nw = n - (d + s)

print(d, s, nw)
