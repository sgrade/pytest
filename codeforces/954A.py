# A. Diagonal Walking

n = int(input())
s = input() + 'X'   # The idea about "+ 'X'" is from https://codeforces.com/contest/954/submission/68485638

ans = 1

if n > 1:
    ans = 0
    i = 0
    while i < n:
        ans += 1
        if (s[i+1] == 'R' and s[i] == 'U') or (s[i+1] == 'U' and s[i] == 'R'):
            i += 2
        else:
            i += 1

print(ans)
