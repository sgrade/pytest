# A. Prefixes

# Editorial - https://codeforces.com/blog/entry/69954

n, s = int(input()), input()
ans = 0
output = list()
for i in range(0, n, 2):
    if s[i] == s[i + 1]:
        ans += 1
        output += 'a' if s[i] == 'b' else 'b'
    else:
        output.append(s[i])
    output.append(s[i+1])

print(ans)
print(''.join(output))
