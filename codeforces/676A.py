# A. Nicholas and Permutation

n = int(input())
a = list(map(int, input().split()))
ma = a.index(max(a))
mi = a.index(min(a))

current_distance = max(ma, mi) - min(ma, mi)
candidate_right = (n - 1) - max(ma, mi)
candidate_left = min(ma, mi)
if candidate_right > candidate_left:
    print(n - 1 - min(ma, mi))
else:
    print(max(ma, mi))
