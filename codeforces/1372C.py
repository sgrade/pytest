# C. Omkar and Baseball

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    # Editorial - https://codeforces.com/blog/entry/79974
    non_matching_indexes = list()
    for i in range(n):
        if i+1 != a[i]:
            non_matching_indexes.append(i)

    matching_indexes_cnt = n - len(non_matching_indexes)
    
    # If matching_indexes == n, a is already sorted
    if matching_indexes_cnt != n:
        if matching_indexes_cnt == 0:
            ans = 1
        else:
            # Checking if all matching indexes are in the same prefix or suffix
            # Idea how to check is from https://codeforces.com/contest/1372/submission/88018041
            if len(non_matching_indexes) == 1 + (non_matching_indexes[-1] - non_matching_indexes[0]):
                ans = 1
            else:
                ans = 2
    
    print(ans)
