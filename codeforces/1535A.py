# A. Fair Playoff

for _ in range(int(input())):
    s = list(map(int, input().split()))
    srted = s.copy()
    srted.sort()

    idx1 = s.index(srted[2])
    idx2 = s.index(srted[3])
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    
    print("YES" if idx1 < 2 and idx2 > 1 else "NO")
