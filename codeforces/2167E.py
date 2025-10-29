# E. khba Loves to Sleep!
# https://codeforces.com/contest/2167/problem/E


def count_positions_with_distance(a, x, dist):
    if dist == 0:
        return x + 1
    count = 0
    if a[0] >= dist:
        count += a[0] - dist + 1
    n = len(a)
    for i in range(0, n - 1):
        gap_start = a[i] + dist
        gap_end = a[i + 1] - dist
        if gap_start <= gap_end and gap_end <= x:
            count += gap_end - gap_start + 1
    if a[n - 1] + dist <= x:
        count += x - (a[n - 1] + dist) + 1
    return count


def get_k_positions_with_distance(a, x, dist, k):
    positions = set()
    n = len(a)
    if a[0] - dist >= 0:
        start = 0
        end = min(a[0] - dist, x)
        for pos in range(start, end + 1):
            if len(positions) >= k:
                break
            positions.add(pos)
    
    for i in range(0, n - 1):
        if len(positions) >= k:
            break
        gap_start = a[i] + dist
        gap_end = a[i + 1] - dist
        if gap_start <= gap_end and gap_start <= x:
            gap_end = min(gap_end, x)
            for pos in range(gap_start, gap_end + 1):
                if len(positions) >= k:
                    break
                positions.add(pos)
    
    if a[n - 1] + dist <= x and len(positions) < k:
        start = a[n - 1] + dist
        end = x
        for pos in range(start, end + 1):
            if len(positions) >= k:
                break
            positions.add(pos)
    return positions


for _ in range(int(input())):

    n, k, x = map(int, input().split())
    st = set(map(int, input().split()))
    a = list(st)
    a.sort()
    
    lo, hi = 0, x
    best_dist = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = count_positions_with_distance(a, x, mid)
        if cnt >= k:
            best_dist = mid
            lo = mid + 1
        else:
            hi = mid - 1
    
    ans = get_k_positions_with_distance(a, x, best_dist, k)
    print(' '.join(map(str, ans)))
