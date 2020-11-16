# B. Numbers Box

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list()
    negatives = 0
    for _ in range(n):
        tmp = list(map(int, input().split()))
        for el in tmp:
            lst.append(abs(el))
            if el < 0:
                negatives += 1
    lst.sort()

    # Editorial - https://codeforces.com/blog/entry/82067
    ans = sum(lst)
    if lst[0] != 0 and negatives % 2 != 0:
        ans -= lst[0] * 2

    print(ans)
