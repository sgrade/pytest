# A. Determine Line

ans = set(range(1, 101))

for _ in range(int(input())):
    # https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
    ans &= set(list(map(int, input().split()))[1:])

print(*ans)
