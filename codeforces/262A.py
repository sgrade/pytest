# A. Roma and Lucky Numbers

n, k = map(int, input().split())
a = list(input().split())

ans = 0
lucky = ['4', '7']
for x in a:
    count = 0
    for digit in x:
        if digit in lucky:
            count += 1
            if count > k:
                break
    if count <= k:
        ans += 1

print(ans)
