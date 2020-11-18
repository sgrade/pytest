# A. Summer Camp

n = int(input())
lst = [str(x) for x in range(1, n+1)]
s = ''.join(lst)
print(s[n-1])
