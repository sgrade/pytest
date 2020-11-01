# A. Even Substrings

n, s = int(input()), input()
ans = 0
for index, num in enumerate(s, start=1):
    if int(num) % 2 == 0:
        ans += index
print(ans)
