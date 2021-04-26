# A. Three Indices

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    ans = False
    indexes = [0, 0, 0]
    
    # Editorial - https://codeforces.com/blog/entry/80054
    for j in range(1, n-1):

        if ans:
            break
        
        indexes[1] = j
        
        if p[j-1] < p[j] > p[j+1]:
            ans = True
            indexes[0] = j - 1
            indexes[2] = j + 1

    
    print("YES" if ans else "NO")
    if ans:
        print(' '.join([str(x+1) for x in indexes]))
