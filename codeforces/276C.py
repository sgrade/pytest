# C. Little Girl and Maximum Sum

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

cnt = [0] * n
for _ in range(q):
    l, r = map(int, input().split())
    # Idea - https: // codeforces.com / blog / entry / 6779
    cnt[l-1] += 1
    if r < n:
        cnt[r] -= 1

st = list()
v = 0
for i in range(n):
    v += cnt[i]
    st.append(v)
st.sort(reverse=True)

sm = 0
for i in range(n):
    sm += a[i] * st[i]

print(sm)
