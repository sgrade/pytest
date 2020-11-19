# A. Partition

n = int(input())
a = list(map(int, input().split()))
a = [-x if x < 0 else x for x in a]
print(sum(a))
