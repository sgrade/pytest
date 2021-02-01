# C. Ternary XOR

for _ in range(int(input())):
    n = int(input())
    s = input()

    # Editorial - https://codeforces.com/blog/entry/75246
    s1 = s2 = ""
    for i in range(n):
        if s[i] == '1':
            s1 += '1'
            s2 += '0'
            for j in range(i + 1, n):
                s1 += '0'
                s2 += s[j]
            break
        else:
            if s[i] == '2':
                s1 += '1'
                s2 += '1'
            else:
                s1 += '0'
                s2 += '0'
    print(s1)
    print(s2)
