# A. Arpa and a research in Mexican wave

n, k, t = map(int, input().split())

ans = min(k, t)
if t > n:
    ans = k - (t - n)

print(ans)
