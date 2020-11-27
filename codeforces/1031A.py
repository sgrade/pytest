# A. Golden Plate

w, h, k = map(int, input().split())
ans = 0
while k > 0:
    ans += 2 * w + 2 * (h - 2)
    w -= 4
    h -= 4
    k -= 1
print(ans)
