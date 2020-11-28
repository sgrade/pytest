# A. Buying A House

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

n -= 1
m -= 1

i = 0
while True:
    i += 1
    if m - i >= 0:
        if a[m-i] != 0 and a[m-i] <= k:
            break
    if m + i <= n:
        if a[m+i] != 0 and a[m+i] <= k:
            break

print(i * 10)
