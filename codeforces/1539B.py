# B. Love Song

from string import ascii_lowercase
from collections import Counter

alphabet = list(ascii_lowercase)
a_dict = dict()
for i in range(len(alphabet)):
    a_dict[alphabet[i]] = i + 1

n, q = map(int, input().split())
s = list(input())

dp = list()
dp.append(0)
for i in range(len(s)):
    dp.append(dp[i] + a_dict[s[i]])

for _ in range(q):
    l, r = map(int, input().split())    
    print(dp[r] - dp[l-1])
