# https://docs.python.org/3/howto/sorting.html

list_to_sort = [1, 7, 38, 9, 4, 45, 9, 2, 38, 3, 12, 5]

print(sorted(list_to_sort))
# will print: [1, 2, 3, 4, 5, 7, 9, 9, 12, 38, 38, 45]


print(list_to_sort.sort())
# will print: None


list_to_sort.sort()
print(list_to_sort)
# will print: [1, 2, 3, 4, 5, 7, 9, 9, 12, 38, 38, 45]


print('\n######')
dict_to_sort = {'1': 'Hi', '7': 'Haha', '38': 'don\'t know what to say'}
srtd = sorted(dict_to_sort.items())
print(srtd)
# will print: [('1', 'Hi'), ('38', "don't know what to say"), ('7', 'Haha')]
