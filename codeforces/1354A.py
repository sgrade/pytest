# A. Alarm Clock

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    ans = -1

    if a <= b:
        ans = b
    elif c > d:
        ans = b
        a -= b

        sleep_cycle_duration = c - d
        num_of_cycles = (a + sleep_cycle_duration - 1) // sleep_cycle_duration

        ans += num_of_cycles * c

    print(ans)
