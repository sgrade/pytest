# A. Devu, the Singer and Churu, the Joker

n, d = map(int, input().split())
t = list(map(int, input().split()))

ans = -1

songs = sum(t)
rest = (n - 1) * 10
if songs + rest <= d:
    ans = (d - songs) // 5

print(ans)
