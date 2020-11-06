# A. GukiZ and Contest

# Idea - https://codeforces.com/contest/551/submission/12629224

_ = input()
lst = list(map(int, input().split()))
ans = list()
for x in lst:
    ans.append(1 + sorted(lst)[::-1].index(x))
print(' '.join(str(x) for x in ans))
