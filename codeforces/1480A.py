# A. Yet Another String Game

import string

alphabet_string = string.ascii_lowercase

for _ in range(int(input())):
    s = input()

    ans = list()
    # Idea - https://codeforces.com/contest/1480/submission/110336000
    for i in range(len(s)):
        # a
        if i % 2 == 0:
            ans.append('b' if s[i] == 'a' else 'a')
        # b
        else:
            ans.append('y' if s[i] == 'z' else 'z')

    print(''.join(ans))
