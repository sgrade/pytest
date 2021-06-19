# D. Corrupted Array

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort()

    sm = sum(b)

    ans = False

    for i in range(n, n+2):
        x = b[i]
        sm -= b[i]

        for j in range(n+2):
            if i == j:
                continue
            
            y = b[j]
            if sm - b[j] == b[i]:
                ans = True
                b.remove(y)
                break
        
        if ans:
            b.remove(x)
            break
        else:
            sm += b[i]

    if ans:
        print(*b)
    else:
        print(-1)
