# A. Maximum Square

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 1
    for i in range(len(a)):
        if i + 1 == a[i]:
            ans = i + 1
            break
        elif i + 1 > a[i]:
            ans = i
            break
    print(ans)
