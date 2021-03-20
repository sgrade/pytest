# A. Winner

n = int(input())
scores = dict()
chrono = list()

for _ in range(n):
    inp = input().split()
    name = inp[0]
    score = int(inp[1])
    try:
        scores[name] += score
    except KeyError:
        scores[name] = score
    chrono.append([scores[name], name])

mx = max(scores.values())
candidate_winners = [name for name, score in scores.items() if score == mx]

ans = ""
for x in chrono:
    if x[1] in candidate_winners and x[0] >= mx:
        ans = x[1]
        break

print(ans)
