# D. Yet Another Array Problem
# https://codeforces.com/contest/2167/problem/D

from math import gcd


for _ in range(int(input())):

    n = int(input())
    st = set(map(int, input().split()))

    gcd_of_set = gcd(*st)
    lowest_coprime = 2
    while gcd(gcd_of_set, lowest_coprime) != 1:
        lowest_coprime += 1
    print(lowest_coprime)
