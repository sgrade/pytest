# B. WeirdSort

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = set(map(int, input().split()))
    p = [x-1 for x in p]

    # Editorial - Editorial - https://codeforces.com/blog/entry/74224
    for i in range(n):
        if i in p:
            j = i
            while j < n and j in p:
                j += 1
            a[i:j+1] = sorted(a[i:j+1])

    print("YES") if sorted(a) == a else print("NO")
