# B. Parity Alternated Deletions

n = int(input())
a = list(map(int, input().split()))

odd = list()
even = list()

for digit in a:
    if digit % 2 == 0:
        even.append(digit)
    else:
        odd.append(digit)

odd.sort(reverse=True)
even.sort(reverse=True)

min_len = min(len(odd), len(even))
max_len = max(len(odd), len(even))

ans = 0

if len(odd) == max_len:
    ans += sum(odd[min(min_len + 1, len(odd)):])
else:
    ans += sum(even[min(min_len + 1, len(even)):])

print(ans)
