"""Booking.com interview question
http://www.glassdoor.nl/Sollicitatiegesprek/Booking-com-Sollicitatiegesprek-RVW42494178.htm
"""

import os

N = 5

PATH = "/workspaces/pytest/codeforces"
lst = os.listdir(PATH)

sizes = []

for file in lst:
    fpath = PATH + "/" + file
    if os.path.isdir(fpath):
        continue

    size = os.path.getsize(fpath)
    sizes.append([size, file])

sizes.sort(reverse=True)

output = []

for f in sizes[:N]:
    output.append(f[1])

output.sort()

for f in output:
    print(f)
