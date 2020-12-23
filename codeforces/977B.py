# B. Two-gram

n = int(input())
s = input()

two_grams = set()

for i in range(1, n):
    two_grams.add(s[i-1:i+1])

prev_count = 0
ans = ''
for tg in two_grams:
    cnt = 0
    for i in range(1, n):
        if s[i-1:i+1] == tg:
            cnt += 1
    if cnt > prev_count:
        ans = tg
        prev_count = cnt

print(ans)
