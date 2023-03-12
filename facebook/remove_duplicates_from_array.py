l = [1, 2, 3, 4, 5, 7, 9, 9, 12, 38, 38, 45]

# Easy way is too easy
# print(set(l))


# Alternative implementation
def remove_duplicates(lst):
    hash = list()
    length = len(lst)
    for i in range(length):
        if lst[i] not in hash:
            hash.append(lst[i])
    return hash


print(remove_duplicates(l))


## An alternative
print(set(l))