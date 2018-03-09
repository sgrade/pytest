a = [5, 10, 15, 20, 25]

a_cut = [item for item in a if item == a[0] or item == a[-1]]
print(a_cut)

