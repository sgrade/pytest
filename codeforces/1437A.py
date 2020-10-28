# A. Marketing Scheme

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    ans = "YES" if 2*l > r else "NO"
    print(ans)
