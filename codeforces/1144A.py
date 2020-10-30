# A. Diverse Strings

for _ in range(int(input())):
    s = input()
    s = ''.join(sorted(s))
    st = set(s)
    if len(s) == len(st) and ord(s[-1])-ord(s[0]) == len(s)-1:
        print('Yes')
    else:
        print('No')
