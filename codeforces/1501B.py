# B. Napoleon Cake

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # Idea - https://codeforces.com/contest/1501/submission/109925625
    drenched = [0] * n
    layers_drenched = 0
    for i in range(n - 1, -1, -1):
        layers_drenched = max(layers_drenched - 1, a[i])
        if layers_drenched > 0:
            drenched[i] = 1

    print(*drenched)
