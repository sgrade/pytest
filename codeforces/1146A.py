# A. Love "A"

s = input()

num_of_a = s.count('a')
s_half = len(s) / 2

ans = len(s) if num_of_a > s_half else num_of_a * 2 - 1
print(ans)

