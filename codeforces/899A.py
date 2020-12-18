# A. Splitting in Teams

n = int(input())
a = list(map(int, input().split()))

ones = a.count(1)
twos = a.count(2)
ans = min(twos, ones)
if ones > twos:
    ans += (ones - twos) // 3

print(ans)
