# A. Elections

n = int(input())
a = list(map(int, input().split()))

votes_opponent = sum(a)

a.sort()
k = max(a)
while True:
    votes_awruk = sum([k - el for el in a])
    if votes_awruk > votes_opponent:
        break
    else:
        k += 1

print(k)
