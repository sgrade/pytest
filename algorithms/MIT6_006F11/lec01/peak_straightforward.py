import time
import json
from os import path, getcwd

script_dir = getcwd()
input_dir = "/".join(script_dir.split('/')[:-2])
input_file = path.join(input_dir, 'input', 'set_of_ints.json')
with open(input_file, 'r') as inp_f:
    inp = json.load(inp_f)

lst = inp['set_of_ints']
# lst = [6, 7, 4, 3, 2, 1, 4, 5]

start_time = time.time()

peak = None

# Starting from the second element
n = 1

while n < len(lst)-1:
    if lst[n] > lst[n-1] and lst[n] > lst[n+1]:
        peak = lst[n]
    n += 1
    break
# Checking the last element
if not peak and lst[n] > lst[n-1]:
    peak = lst[n]

print('Peak: ', peak)

print('Execution time, sec: ', (time.time() - start_time))
