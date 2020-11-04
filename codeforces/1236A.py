# A. Stones

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = min(b, c // 2)
    b -= ans
    ans += min(a, b // 2)
    print(ans * 3)
