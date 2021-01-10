# A. DZY Loves Hash

p, n = map(int, input().split())

st = set()
i = 0
for _ in range(n):
    i += 1
    x = int(input())
    h = x % p
    if h in st:
        break
    else:
        st.add(h)
else:
    i = -1

print(i)
