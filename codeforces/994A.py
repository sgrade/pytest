# A. Fingerprints

from collections import OrderedDict

n, m = map(int, input().split())
x = list(input().split())
y = list(input().split())

ans = OrderedDict()
for key in y:
    if key in x:
        ans[x.index(key)] = key

print(' '.join([value for key, value in sorted(ans.items())]))
