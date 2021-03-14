# B. Max and Mex

for _ in range(int(input())):
    n, k = map(int, input().split())
    st = set(map(int, input().split()))

    a = 0
    if k:
        while a in st:
            a += 1
        b = max(st)

        tmp = (a + b + 1) // 2

        # Idea from - https://codeforces.com/contest/1496/submission/109640110
        # Explanation in - https://www.youtube.com/watch?v=g8bYHwPjhLM
        # a (MEX) is always the same, so b will be the same as well - no need to do anything
        if tmp != a:
            st.add(tmp)
            k = 0

    print(len(st) + k)
