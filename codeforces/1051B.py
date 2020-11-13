# B. Relatively Prime Pairs

l, r = map(int, input().split())
# Editorial - https://codeforces.com/blog/entry/61969
print('YES')
for i in range(l, r+1, 2):
    print(i, i+1)
