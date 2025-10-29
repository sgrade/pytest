# B. Your Name
# https://codeforces.com/contest/2167/problem/B

from collections import Counter


for _ in range(int(input())):
    n = int(input())
    s1, s2 = input().split()
    count1 = Counter(s1)
    count2 = Counter(s2)
    if count1 == count2:
        print("YES")
    else:
        print("NO")
