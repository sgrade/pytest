# A. Petr and a calendar

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())
m -= 1

columns = 1
months[m] -= 8 - d


columns += months[m] // 7
months[m] -= 7 * (columns - 1)

if months[m] > 0:
    columns += 1

print(columns)
