import time
import json
from os import path, getcwd

script_dir = getcwd()
input_dir = "/".join(script_dir.split('/')[:-2])
input_file = path.join(input_dir, 'input', 'set_of_ints.json')
with open(input_file, 'r') as inp_f:
    inp = json.load(inp_f)

# lst = [6, 7, 8]
# lst = [8, 7, 6]
# lst = [8, 8, 8]
# lst = [6, 7, 4, 3, 2, 1, 4, 5]
# lst = [6, 7, 8, 9K, 10, 11, 12, 13]
lst = inp['set_of_ints']

start_time = time.time()


def find_peak(lst):

    # Start in the middle
    mid = len(lst) // 2
    # print(lst)
    # print('mid:', lst[mid])

    # Base case:
    # 1) Peak is in the left side of the list (mid == 0)
    # 2) Peak is in the right side of the list (mid == len(lst) - 1)
    # 3) Peak is somewhere inside the list
    if (mid == 0 or (lst[mid] >= lst[mid-1])) and ((mid == len(lst) - 1) or (lst[mid] >= lst[mid+1])):
        # print("Peak found!", "Index:", mid, "Value:", lst[mid])
        return lst[mid]

    # If a[n/2] < a[n/2 − 1] then only look at left half
    # 1 . . . n/2 − 1 to look for peak
    elif lst[mid] <= lst[mid-1]:
        # print("Looking into left part")
        return find_peak(lst[:mid])

    # Else if a[n/2] < a[n/2 + 1] then only look at right half
    # n/2 + 1 . . . n to look for peak
    elif lst[mid] <= lst[mid+1]:
        # print("Looking into right part")
        return find_peak(lst[mid:])


peak = None
print('Peak: ', find_peak(lst))

print('Execution time, sec: ', (time.time() - start_time))


