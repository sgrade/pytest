# B. Sale

n, m = map(int, input().split())
a = list(map(int, input().split()))

negatives = [-x for x in sorted(a) if x < 0]
print(sum(negatives[:m]))
