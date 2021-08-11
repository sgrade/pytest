# A. Holidays

# Based on https://codeforces.com/contest/670/submission/18031374

n = int(input())

quotient, reminder = divmod(n, 7)

holidays_in_full_weeks = 2 * quotient

# Full week is taken into account in quotient
# The only exception is when reminder == 6 (saturday should be taken into account)
mn = holidays_in_full_weeks + (reminder == 6)

# if the week starts on holiday
mx = holidays_in_full_weeks + min(reminder, 2)

print(mn, mx)
