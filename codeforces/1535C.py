# C. Unstable String

for _ in range(int(input())):
    s = input()
    n = len(s)

    ans = 0

    cnt = 1
    i = 0
    while i < n:

        while i < n and s[i] == '?':
            ans += cnt
            i += 1
            cnt += 1

        consequitive_q_marks = 0
        j = i
        while j < n:

            if s[j] != '?':
                # different parity
                if (i ^ j) & 1:
                    if s[i] == s[j]:
                        break
                # same parity
                else:
                    if s[i] != s[j]:
                        break
                
                consequitive_q_marks = 0

            else:
                consequitive_q_marks += 1
            
            ans += cnt
            cnt += 1
            j += 1

        i = j
        cnt = 1
        if i > 0 and s[i-1] == '?':
            cnt += consequitive_q_marks
    
    print(ans)
