# C. Social Distance

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = '0' * k + input()

    max_tables = 0
    i = 0
    while i < n:
        segment_len = 0
        found = s.find('1', i)
        if found != -1:
            segment_len = max(0, found - i - k)
            i = found + 1
        else:
            segment_len = len(s) - i
            i = n

        max_tables += segment_len // (k + 1)

    print(max_tables)
