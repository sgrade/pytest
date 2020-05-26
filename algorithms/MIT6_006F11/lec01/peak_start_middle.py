import time
import json
from os import path, getcwd

script_dir = getcwd()
input_dir = "/".join(script_dir.split('/')[:-2])
input_file = path.join(input_dir, 'input', 'set_of_ints.json')
with open(input_file, 'r') as inp_f:
    inp = json.load(inp_f)

# lst = inp['set_of_ints']
lst = [6, 7, 4, 3, 2, 1, 4, 5]

start_time = time.time()

peak = None

# Search boundary for recursion. In the beginning it is the whole list.
start = 0
end = len(lst) - 1

# n = end

# Track which items have been tested for peak
# tested = dict.fromkeys(range(n))


def find_peak(start, end):

    # Start in the middle
    mid = (end - start) // 2
    print('start:', start, "end:", end, 'mid:', mid)

    # If a[n/2] < a[n/2 − 1] then only look at left half
    # 1 . . . n/2 − 1 to look for peak
    if lst[mid] < lst[mid-1]:
        return find_peak(start, mid-1)

    # Else if a[n/2] < a[n/2 + 1] then only look at right half
    # n/2 + 1 . . . n to look for peak
    elif lst[mid] < lst[mid+1]:
        return find_peak(mid+1, end)

    # Else n/2 position is a peak:
    else:
        return mid


print('Peak: ', find_peak(start, end))

print('Execution time, sec: ', (time.time() - start_time))


