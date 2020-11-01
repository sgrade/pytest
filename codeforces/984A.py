# A. Game

n, a = int(input()), list(map(int, input().split()))
a.sort()
print(a[(n-1)//2])
