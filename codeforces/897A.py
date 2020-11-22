# A. Scarborough Fair

n, m = map(int, input().split())
s = list(input())

for _ in range(m):
    l, r, c1, c2 = input().split()
    l = int(l)
    r = int(r)
    for x in range(l-1, r):
        if s[x] == c1:
            s[x] = c2
print(''.join(s))
