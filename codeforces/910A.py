# A. The Way to Home

n, d = map(int, input().split())
s = input()

ans = 0
i = 0
while i < n-1:
    try:
        x = s[:i+d+1].rindex('1')
        if x == i:
            raise ValueError
        i = x
        ans += 1
    except ValueError:
        ans = -1
        break

print(ans)
