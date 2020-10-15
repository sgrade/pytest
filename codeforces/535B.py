# Source - https://ideone.com/0fX8LQ

__author__ = 'Zlobober'
n = input()
ans = 1
for x in n:
    ans = 2 * ans + (1 if x == '7' else 0)
    print(x, ans)
print(ans - 1)
