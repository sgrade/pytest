# A. Duff and Meat

n = int(input())

ans = 0
current_min = 100
for i in range(n):
    ai, pi = map(int, input().split())
    if pi < current_min:
        current_min = pi
    ans += current_min * ai

print(ans)
