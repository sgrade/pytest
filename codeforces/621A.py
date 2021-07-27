# A. Wet Shark and Odd and Even

n = int(input())
a = list(map(int, input().split()))
a.sort()

sm = sum(a)

if sm % 2 == 0:
    print(sm)
else:
    for digit in a:
        if digit % 2 != 0:
            sm -= digit
            print(sm)
            break
