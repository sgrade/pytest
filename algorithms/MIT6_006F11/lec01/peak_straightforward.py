import time
start_time = time.time()

lst = [6, 7, 4, 3, 2, 1, 4, 5]

peak = None

# Starting from the second element
n = 1

while(n < len(lst)-1):
    if lst[n] > lst[n-1] and lst[n] > lst[n+1]:
        peak = lst[n]
    n += 1
# Checking the last element
if lst[n] > lst[n-1]:
    peak = lst[n]

print('Peak: ', peak)

print('Execution time, sec: ', (time.time() - start_time))
