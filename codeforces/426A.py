# A. Sereja and Mugs

n, s = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
print("YES" if sum(a[:-1]) <= s else "NO")
