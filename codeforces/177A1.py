# A1. Good Matrix Elements

n = int(input())
a = list()

for _ in range(n):
    a.append(list(map(int, input().split())))

ans = 0

if n == 1:
    ans = a[0][0]

else:
    # mid row
    ans += sum(a[(n-1) // 2])
    
    # mid column
    j = (n-1) // 2
    for i in range(n):
        ans += a[i][j]
    ans -= a[(n-1)//2][(n-1)//2]

    for i in range(0, (n-1) // 2):
        ans += a[i][i] + a[i][n-1-i]
    for i in range((n-1)//2 + 1, n):
        ans += a[i][i] + a[i][n-1-i]

print(ans)
