# A. Anti-knapsack

for _ in range(int(input())):
    n, k = map(int, input().split())
    # Idea - https://codeforces.com/contest/1493/submission/109290286
    output = list()
    for i in range(1, n+1):
        if i != k and (i * 2 >= k or i > k):
            output.append(i)
    print(len(output))
    print(*output)
