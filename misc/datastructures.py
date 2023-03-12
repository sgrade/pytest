import collections

lst = [1, 24, 24, 6, 45, 43]

print("\nCounter:")
cntr = collections.Counter(lst)
print(cntr)
print(cntr[99])

print("\nDict:")
# cntrdict = {24: 2, 1: 1, 6: 1, 45: 1, 43: 1}
cntrdict = dict(cntr)
print(cntrdict)
print(cntrdict.get(99))
print(cntrdict)
print(cntrdict.get(98, 2))
print(cntrdict)
print(cntrdict.setdefault(98, 3))
print(cntrdict)
print(cntrdict.setdefault(97, 3))
print(cntrdict)
print(sorted(cntrdict))
print(sorted(cntrdict.items()))
print(sorted(cntrdict.items(), key = lambda item: item[1]))

print("\nDefault dict:")
cntrdefdict = collections.defaultdict(int, {24: 2, 1: 1, 6: 1, 45: 1, 43: 1})
print(cntrdefdict)
print(cntrdefdict[99])
print(cntrdefdict)

print("\nList comprehension:")
xlst = [key for key, value in cntr.items() if value % 2 == 0]
print(xlst)

print("\nSet:")
xset = {value for value in lst}
print(xset)

print("\nGenerator expression:")
genexpr = sum(value for value in lst)
print(genexpr)

print("\nLambda:")
a, b = 1, 2
max = lambda a, b : a if (a > b) else b
print(max(1, 2))

print("\nMap:")
xsetmapped = map(lambda x: x * x, xset)
print(next(xsetmapped))
print(list(xsetmapped))

print("\nFilter:")
xsetfiltered = filter(lambda x: x < 40, xset)
print(next(xsetfiltered))
print(list(xsetfiltered))

print("\nDeque:")
xdeq = collections.deque(xlst)
xdeq.append(100)
xdeq.extend([110, 120])
xdeq.appendleft(-1)
xdeq.extendleft([-10, -11])
print(xdeq)
xdeq.pop()
xdeq.popleft()
print(xdeq)
