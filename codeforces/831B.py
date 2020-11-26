# B. Keyboard Layouts

l1 = input()
l2 = input()
s = input()
ans = list()
for i in range(len(s)):
    try:
        ind = l1.index(s[i].lower())
        is_low = s[i].islower()
        ind = l1.index(s[i].lower())
        ans.append(l2[ind]) if is_low else ans.append(l2[ind].upper())
    except ValueError:
        ans.append(s[i])

print(''.join(ans))
