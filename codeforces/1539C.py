# C. Stable Groups

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 1

if n > 1:
    a.sort()

    distances = list()
    for i in range(1, n):
        d = a[i] - a[i-1]
        if d > x:
            distances.append(d)
    
    distances.sort()
    ans = len(distances) + 1

    i = 0
    while k > 0 and i < len(distances):
        k -= distances[i] // x
        if distances[i] % x == 0:
            k += 1
        if k >= 0:
            ans -= 1
        i += 1
    
print(ans)
