# A. A pile of stones

n = int(input())
s = input()

ans = 0
for i in s:
    if i == '+':
        ans += 1
    else:
        ans = max(0, ans - 1)

print(ans)
