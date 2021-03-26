# B. Partial Replacement

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    ans = 1

    i = s.find('*')
    j = s.rfind('*')

    if i != j:
        ans = 2

        while True:
            tmp = s[i+1: i+1+k]
            x = tmp.rfind('*')
            i += x + 1
            if i < j:
                ans += 1
            else:
                break

    print(ans)
