# A. Be Positive

n = int(input())
a = list(map(int, input().split()))

pos = 0
neg = 0
for x in a:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1

target = (n + 2 - 1) // 2
if pos >= target:
    print(1)
elif neg >= target:
    print(-1)
else:
    print(0)
