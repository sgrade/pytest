# A. Lucky Ticket

n = int(input())
num = input()

ans = "YES"
for i in num:
    if i == '4' or i == '7':
        continue
    else:
        ans = "NO"
        break

if ans == "YES":
    first = 0
    for x in num[:n//2]:
        first += int(x)

    second = 0
    for x in num[n//2:]:
        second += int(x)

    if first != second:
        ans = "NO"

print(ans)
