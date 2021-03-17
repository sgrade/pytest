# C. Woodcutters

n = int(input())
d = dict()
for i in range(n):
    x, h = map(int, input().split())
    d[i] = [x, h]

ans = 1

if n == 2:
    ans = 2
elif n > 2:
    it1 = 0
    it2 = 1
    it3 = 2

    segment_clear = True
    for i in range(n - 2):
        h = d[it2][1]

        if segment_clear and d[it2][0] - h > d[it1][0]:
            ans += 1
            segment_clear = True
        elif not segment_clear and d[it2][0] - h > d[it1][0] + d[it1][1]:
            ans += 1
            segment_clear = True
        elif d[it2][0] + h < d[it3][0]:
            ans += 1
            segment_clear = False
        else:
            segment_clear = True

        it1 += 1
        it2 += 1
        it3 += 1

    ans += 1

print(ans)
