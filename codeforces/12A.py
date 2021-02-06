# A. Super Agent

s = ""
for _ in range(3):
    s += input()

# Idea from https://codeforces.com/contest/12/submission/69686110
print("YES" if s == s[::-1] else "NO")
