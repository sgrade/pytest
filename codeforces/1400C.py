# C. Binary String Reconstruction

for _ in range(int(input())):
    s = list(input())
    x = int(input())

    n = len(s)
    w = ['1'] * n

    for i in range(n):
        if s[i] == '0':
            if i-x >= 0:
                w[i-x] = '0'
            if i+x < n:
                w[i+x] = '0'
    
    # Editorial - https://codeforces.com/blog/entry/81942
    s_recreated = ['?'] * n
    for i in range(n):
        if (i-x >= 0 and w[i-x] == '1') or (i+x < n and w[i+x] == '1'):
            s_recreated[i] = '1'
        else:
            s_recreated[i] = '0'
    
    if s_recreated == s:
        print(''.join(w))
    else:
        print("-1")
