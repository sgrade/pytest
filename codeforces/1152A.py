# A. Neko Finds Grapes

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_even = [x for x in a if x % 2 == 0]
b_odd = [x for x in b if x % 2 != 0]

ans = min(len(a_even), len(b_odd))
ans += min(n - len(a_even), m - len(b_odd))

print(ans)
