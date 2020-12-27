# A. Chips Moving

n = int(input())
x = list(map(int, input().split()))

odd = 0
even = 0

for i in range(n):
    if x[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(min(odd, even))
