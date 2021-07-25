# A. Even But Not Even

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input()))

    sm = sum(s)

    if sm % 2 == 0 and s[-1] % 2 != 0:
        print(*s, sep='')

    else:

        ans = False
        
        # Making the last digit odd
        idx = n
        while idx > 0 and s[idx-1] % 2 == 0:
            sm -= s[idx-1]
            idx -= 1
        
        if sm > 0 and sm % 2 == 0:
            print(*s[:idx], sep = '')
        
        else:
            i = 1
            while i < idx-1:
                if s[i] % 2 != 0:
                    print(*s[:i], sep='', end = '')
                    print(*s[i+1:idx], sep='')
                    break
                i += 1
            else:
                print(-1)
