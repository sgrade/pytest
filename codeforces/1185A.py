# A. Ropewalkers

a, b, c, d = map(int, input().split())
lst = [a, b, c]
lst.sort()

left = max(0, d - abs(lst[0] - lst[1]))
right = max(0, d - abs(lst[1] - lst[2]))
ans = abs(left + right)
print(ans)
