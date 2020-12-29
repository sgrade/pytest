# B. Make Product Equal One

n = int(input())
a = list(map(int, input().split()))

ans = 0
negatives = 0
zeros = 0
for el in a:
    if el < 0:
        negatives += 1
        if el < - 1:
            ans += -1 - el
    elif el > 1:
        ans += el - 1
    elif el == 0:
        ans += 1
        zeros += 1

if negatives % 2 != 0:
    if zeros == 0:
        ans += 2

print(ans)
