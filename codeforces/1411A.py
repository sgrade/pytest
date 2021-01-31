# A. In-game Chat

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip(')')
    ans = n - len(s) > len(s)
    print("Yes" if ans else "No")
