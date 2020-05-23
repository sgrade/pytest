def partition(lst, lo, hi):

    # i - iteration variable
    # j - position of the pivot

    i, j = lo, hi - 1
    pivot = lst[hi]
    # print('partitioning with pivot:', pivot)

    while True:
        while lst[i] < pivot and i < j:
            i += 1

        while lst[j] > pivot and i < j:
            j -= 1

        if i == j:
            # print('indexes met: i and j =', j)
            if lst[i] < pivot:
                i += 1

            lst[i], lst[hi] = lst[hi], lst[i]

            # print('returning i:', i, ', list is:', lst)
            return i

        else:
            # print('found element > pivot:', lst[i])
            # print('found element < pivot:', lst[j])
            # print('swapping', lst[i], 'and', lst[j])
            lst[i], lst[j] = lst[j], lst[i]
            # print('updated list:', lst)


def quick_sort(lst, lo, hi):
    if lo < hi:
        # print('\nStarting a cycle on', lst)
        p = partition(lst, lo, hi)
        quick_sort(lst, lo, p - 1)
        quick_sort(lst, p + 1, hi)
    return lst


# list_to_sort = [1, 7, 38, 9, 4, 45, 9, 2, 38, 3, 12, 5]
list_to_sort = [1, 2, 3, 4, 5, 7, 9, 9, 12, 38, 38, 45]
# list_to_sort = [1, 3, 2]
# list_to_sort = []
# list_to_sort = [1]
x = quick_sort(list_to_sort, 0, len(list_to_sort)-1)
print(x)
