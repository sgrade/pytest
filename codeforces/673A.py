# A. Bear and Game

n = int(input())
t = list(map(int, input().split()))

ans = 0

if t[0] <= 15:
    for i in range(n):
        ans = t[i]
        if i != n-1:
            if t[i+1] - t[i] > 15:
                break

ans = min(ans + 15, 90)

print(ans)
