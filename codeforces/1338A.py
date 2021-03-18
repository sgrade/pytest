# A. Powered Addition

i, tmp = 1, 1
x = [1]
while tmp < 1000000000:
    tmp *= 2
    x.append(x[i-1] + tmp)
    i += 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    if n > 1:
        max_diff = 0
        for i in range(1, n):
            if a[i-1] > a[i]:
                max_diff = max(max_diff, a[i-1] - a[i])
                # Idea = https: // www.youtube.com / watch?v = CTDM1A1_RKc
                a[i] = a[i-1]
        if max_diff > 0:
            ans = next(idx for idx, y in enumerate(x) if y >= max_diff) + 1

    print(ans)
