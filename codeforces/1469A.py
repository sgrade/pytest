# A. Regular Bracket Sequence

n = int(input())

for _ in range(n):
    s = input()

    ans = "NO"

    open_ind = s.index('(')
    close_ind = s.index(')')

    if open_ind < close_ind:
        if (len(s) - 2) % 2 == 0:
            ans = "YES"
    elif close_ind > 0 and open_ind < len(s)-1:
        if len(s) == 4 or (len(s) - 4) % 2 == 0:
            ans = "YES"

    print(ans)
