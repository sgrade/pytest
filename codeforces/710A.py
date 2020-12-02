# A. King Moves

s = input()
column = s[0]
row = s[1]

ans = 8
if column in ['a', 'h']:
    ans -= 3
if row in ['1', '8']:
    ans -= 3
if column in ['a', 'h'] and row in ['1', '8']:
    ans += 1

print(ans)
