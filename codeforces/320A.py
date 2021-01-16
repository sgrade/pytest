# A. Magic Numbers

s = input()

ans = False
i = 0
if s[i] == '1':
    ans = True
    i += 1
    try:
        while i < len(s):
            if s[i] == '1':
                i += 1
                continue
            elif s[i] == '4' and s[i - 1] == '1':
                i += 1
                continue
            elif s[i] == '4' and s[i - 2] == '1':
                i += 1
                continue
            else:
                ans = False
                break
    except IndexError:
        ans = False

print("YES" if ans else "NO")
