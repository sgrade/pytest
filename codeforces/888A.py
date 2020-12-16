# A. Local Extrema

n = int(input())
a = list(map(int, input().split()))

ans = 0

if n > 2:
    for ind in range(1, n-1):
        if a[ind-1] < a[ind] and a[ind+1] < a[ind]:
            ans += 1
        elif a[ind-1] > a[ind] and a[ind+1] > a[ind]:
            ans += 1

print(ans)
