# A. Perfectly Imperfect Array

dp = set()
for i in range(1, 10001):
    dp.add(i * i)

for _ in range(int(input())):
    n = int(input())
    st = set(map(int, input().split()))
    for x in st:
        if x not in dp:
            print("YES")
            break
    else:
        print ("NO")
