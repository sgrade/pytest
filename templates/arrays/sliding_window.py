def sliding_window_fixed(nums, k):
    """Example: Max sum subarray of size k."""
    if len(nums) < k:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(len(nums) - k):
        # Remove element going out of window, add element coming in
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def sliding_window_variable(s):
    """Example: Longest substring without repeating characters."""
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If duplicate found in current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
