# A. Vanya and Cards

n, x = map(int, input().split())
lst = list(map(int, input().split()))

# to ceil: (a + b - 1) / b
ans = (abs(sum(lst)) + x - 1) // x
print(ans)
