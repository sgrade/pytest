# A. Text Volume

n = int(input())
s = list(map(str, input().split()))

max_volume = 0
for word in s:
    volume = 0
    for ch in word:
        if ch.isupper():
            volume += 1
    max_volume = max(max_volume, volume)

print(max_volume)
