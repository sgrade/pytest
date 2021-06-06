# C. Sum of Cubes

# Editorial - https://codeforces.com/blog/entry/87874
mx = 1000000000001

dp = set()
for i in range(1, 10001):
    dp.add(i * i * i)

for _ in range(int(input())):
    x = int(input())

    ans = False
    for i in range(1, 10001):
        if x - i * i * i in dp:
            ans = True
            break
    
    print("YES" if ans else "NO")
