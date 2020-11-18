# A. Vitaly and Night

n, m = map(int, input().split())
ans = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    for j in range(0, 2 * m, 2):
        if lst[j] == 1 or lst[j + 1] == 1:
            ans += 1
print(ans)
