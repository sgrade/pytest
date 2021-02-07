# A. Eugeny and Array

n, m = map(int, input().split())
a = list(map(int, input().split()))
positives = a.count(1)
negatives = a.count(-1)

for _ in range(m):
    l, r = map(int, input().split())
    if (r - l + 1) % 2 == 0 and (r - l + 1) / 2 <= min(positives, negatives):
        print(1)
    else:
        print(0)
