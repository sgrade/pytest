# A. Phone Numbers

n = int(input())
s = input()

cnt = s.count('8')
ans = min(cnt, n // 11)

print(ans)
