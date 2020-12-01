# A. Bear and Five Cards

t = list(map(int, input().split()))
st = set(t)

sm = sum(t)
ans = sm

if len(st) < 5:
    for x in st:
        cnt = t.count(x)
        if cnt > 1:
            candidate_ans = sm - x * min(3, cnt)
            if candidate_ans < ans:
                ans = candidate_ans

print(ans)
