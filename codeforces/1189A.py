# A. Keanu Reeves

n = int(input())
s = input()
zeros = s.count('0')
ones = n - zeros
if zeros == ones:
    print(2)
    print(s[0], s[1:])
else:
    print(1)
    print(s)
