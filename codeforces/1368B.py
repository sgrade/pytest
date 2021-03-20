# B. Codeforces Subsequences

k = int(input())

s = "codeforces"
cnt = [1] * 10

n = 1
while n < k:
    for i in range(10):
        n /= cnt[i]
        cnt[i] += 1
        n *= cnt[i]

        if n >= k:
            break

ans = list()
for i in range(10):
    for _ in range(cnt[i]):
        ans.append(s[i])

print(''.join(ans))

# Good explanation - https://www.youtube.com/watch?v=HQnGixJMCiI
# I found the solution myself though :)
