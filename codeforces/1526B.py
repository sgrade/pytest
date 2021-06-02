# 

for _ in range(int(input())):
    x = int(input())

    ans = False
    
    # Idea from https://codeforces.com/contest/1526/submission/117594170
    for i in range(11):
        if 111 * i <= x and (x - 111 * i) % 11 == 0:
            ans = True
    
    print("YES" if ans else "NO")
