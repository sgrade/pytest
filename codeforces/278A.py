# A. Circle Line

n = int(input())
d = list(map(int, input().split()))
s, t = map(int, input().split())
s -= 1
t -= 1

if s > t:
    s, t = t, s

s1 = sum(d[s:t])
s2 = sum(d[t:]) + sum(d[:s])
print(min(s1, s2))
