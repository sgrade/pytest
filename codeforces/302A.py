# A. Eugeny and Array

n, m = map(int, input().split())
a = list(map(int, input().split()))
positives = a.count(1)
negatives = a.count(-1)
mn = min(positives, negatives)

output = list()
for _ in range(m):
    l, r = map(int, input().split())
    if (r - l + 1) % 2 == 0 and (r - l + 1) / 2 <= mn:
        output.append('1')
    else:
        output.append('0')

print('\n'.join(output))
