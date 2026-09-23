# 1658. Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # Removing a prefix and a suffix summing to x keeps a middle subarray
        # summing to sum(nums) - x, so minimizing the removals means finding
        # the longest such subarray.
        target = sum(nums) - x
        if target < 0:
            return -1

        longest = -1
        window_sum = 0
        left = 0

        for right, num in enumerate(nums):
            window_sum += num
            # Values are positive, so shrinking from the left is enough to
            # bring an oversized window back to at most target.
            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                longest = max(longest, right - left + 1)

        return len(nums) - longest if longest >= 0 else -1
