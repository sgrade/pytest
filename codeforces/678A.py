# A. Johny Likes Numbers

n, k = map(int, input().split())

if n % k == 0:
    print(n + k)
else:
    print(((n + k - 1) // k) * k)
