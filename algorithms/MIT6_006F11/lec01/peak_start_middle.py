import time
import json
from os import path
from pathlib import Path

script_dir = Path().parent.absolute()
inp_file = path.join(script_dir, 'algorithms', 'input', 'set_of_ints.json')
with open(inp_file, 'r') as inp_f:
    inp = json.load(inp_f)

lst = inp['set_of_ints']
# lst = [6, 7, 4, 3, 2, 1, 4, 5]

start_time = time.time()

peak = None

# Search boundary for recursion. In the beginning it is the whole list.
start = 0
end = len(lst)

n = end

while n > len(lst)-1:
    # Start in the middle
    a = lst[start:end]
    n = len(a)
    n_div_2 = n//2
    # If a[n/2] < a[n/2 − 1] then only look at left half 1 . . . 
    # n/2 − − − 1 to look for peak
    if a[n_div_2] < a[n_div_2 - 1]:
        start = 0
        end = n_div_2
    # Else if a[n/2] < a[n/2 + 1] then only look at right half n/2 + 1 . . . n to look for peak
    elif a[n_div_2] < a[n_div_2 + 1]:
        start = n_div_2
        end = n
    # Else n/2 position is a peak:
    else:
        peak = a[n_div_2]
        break

print('Peak: ', peak)

print('Execution time, sec: ', (time.time() - start_time))


