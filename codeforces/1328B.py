# B. K-th Beautiful String

for _ in range(int(input())):
    n, k = map(int, input().split())

    # Check cpp version for the explanation

    row = 1
    left_b_index = n - 2
    cycle = 2
    while row < k:
        row += cycle
        left_b_index -= 1
        cycle += 1

    right_b_index = n - 1
    cycle -= 1
    if k > 1:
        last_row_of_current_cycle = (1 + cycle) * cycle // 2
        right_b_index = left_b_index + 1 + (last_row_of_current_cycle - k)

    ans = ['a' for i in range(n)]
    ans[left_b_index] = 'b'
    ans[right_b_index] = 'b'

    print(''.join(ans))
