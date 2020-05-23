import time
start_time = time.time()

a = [6, 7, 4, 3, 2, 1, 4, 5]

peak = None

# Start in the middle
n = len(a)

while n > 
# If a[n/2] < a[n/2 − 1] then only look at left half 1 . . . n/2 − − − 1 to look for peak
if a[n/2] < a[n/2 - 1]:
    pass
# Else if a[n/2] < a[n/2 + 1] then only look at right half n/2 + 1 . . . n to look for peak
elif a[n/2] < a[n/2 + 1]:
    pass
# Else n/2 position is a peak:
else:
    pass
