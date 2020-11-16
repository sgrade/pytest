# B. Valerii Against Everyone

for _ in range(int(input())):
    n = int(input())
    b_list = list(map(int, input().split()))
    # Editorial - https://codeforces.com/blog/entry/84589
    b_set = set(b_list)
    if len(b_list) == len(b_set):
        print("NO")
    else:
        print("YES")
