# B. Two Tables

for _ in range(int(input())):
    w, h = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w1, h1 = map(int, input().split())

    # Solution is based on https://codeforces.com/contest/1555/status/B
    
    ans = 0
  
    if x2 - x1 + w1 > w and y2 - y1 + h1 > h:
        ans = -1
    
    else:
        ans = w + h
        if x2 - x1 + w1 <= w:
            ans = min(ans, min(max(0, w1-x1), max(0, x2 - (w-w1))))
        if y2 - y1 + h1 <= h:
            ans = min(ans, min(max(0, h1-y1), max(0, y2 - (h-h1))))

    print(ans)
