# A. Cookies

n = int(input())
a = list(map(int, input().split()))

sm = sum(a)
odd, even = 0, 0
for digit in a:
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

if sm % 2 == 0:
    print(even)
else:
    print(odd)
