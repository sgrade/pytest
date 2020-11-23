# A. Tom Riddle's Diary

st = set()
for _ in range(int(input())):
    s = input()
    if s in st:
        print('YES')
    else:
        st.add(s)
        print('NO')
