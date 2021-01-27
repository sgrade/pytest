# C. Ball in Berland

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    inp1 = list(map(int, input().split()))
    inp2 = list(map(int, input().split()))

    # Editorial - https://codeforces.com/blog/entry/87188
    pairs = list()
    for i in range(k):
        pairs.append([inp1[i], inp2[i]])
    boys = [0 for i in range(a)]
    girls = [0 for i in range(b)]
    for i in range(k):
        pairs[i][0] -= 1
        pairs[i][1] -= 1
        boys[pairs[i][0]] += 1
        girls[pairs[i][1]] += 1

    ans = 0

    for boy, girl in pairs:
        ans += k - (boys[boy] + girls[girl] - 1)

    print(ans // 2)
