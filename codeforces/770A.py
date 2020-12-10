# A. New Password

from string import ascii_lowercase

n, k = map(int, input().split())
ans = ""
i = 0
while i < n:
    ans += ascii_lowercase[:min(k, n-i)]
    i += k
print(ans)
