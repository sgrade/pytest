# B. Kefa and Company

n, d = map(int, input().split())
lst = list()
for _ in range(n):
    m, s = map(int, input().split())
    lst.append([m, s])
lst.sort()

# Idea - https://www.youtube.com/watch?v=fkG_mF-55Rw
i, j, ans, current_ans = 0, 0, 0, 0
while j < n:
    while j < n and lst[j][0] - lst[i][0] < d:
        current_ans += lst[j][1]
        j += 1
    ans = max(ans, current_ans)
    current_ans -= lst[i][1]
    i += 1

print(ans)
