# A. Equality

n, k = map(int, input().split())
s = input()
st = set(s)

ans = 0

if len(st) == k:
    min_occurences = 100001
    for letter in st:
        cnt = s.count(letter)
        if cnt < min_occurences:
            min_occurences = cnt
    ans = min_occurences * k

print(ans)
