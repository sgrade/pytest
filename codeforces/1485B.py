# B. Replace and Keep Sorted

n, q, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print((a[l] - 1) + (k - a[r]) + 2 * ((a[r] - a[l]) - (r - l)))
