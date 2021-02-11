# B. New Colony

for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))

    pos = -1
    while k > 0:
        for i in range(n-1):
            if h[i] < h[i+1]:
                h[i] += 1
                k -= 1
                pos = i + 1
                break
        else:
            break

    print('-1' if k > 0 else pos)
