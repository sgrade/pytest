# C - A x B + C

# NOT MY CODE - just testing the editorial
# https://atcoder.jp/contests/abc179/submissions/16844575

n = int(input())
ans = 0
for a in range(1, n):
    # print("a: ", a)
    # print("(n - 1) // a: ", (n - 1) // a)
    ans += (n - 1) // a
    # print(ans)
print(ans)
