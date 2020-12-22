# B. Move and Turn

n = int(input())

ans = 4

if n % 2 != 0:
    ans = 4
    scaler = 1
    for i in range(3, n+1, 2):
        ans += 4 * (i - scaler)
        scaler += 1

else:
    scaler = 1
    for i in range(2, n+1, 2):
        scaler += 1
    ans = scaler * scaler

print(ans)
