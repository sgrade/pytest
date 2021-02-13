# A. Declined Finalists

k = int(input())
r = list(map(int, input().split()))
r.sort()
print(max(0, r[-1] - 25))
