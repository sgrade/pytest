# 3578. Count Partitions With Max-Min Difference at Most K
# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/


from typing import cast

from sortedcontainers import SortedList


# Based on Editorial's Approach 1: Sliding Window + Dynamic Programming
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        valid_partitions = [0] * (n + 1)
        valid_partitions_for_prefix = [0] * (n + 1)

        nums_in_window = SortedList()

        valid_partitions[0], valid_partitions_for_prefix[0] = 1, 1

        left = 0
        for right in range(n):
            nums_in_window.add(nums[right])
            while cast(int, nums_in_window[-1]) - cast(int, nums_in_window[0]) > k:
                nums_in_window.remove(nums[left])
                left += 1
            valid_partitions[right + 1] = (
                valid_partitions_for_prefix[right]
                - (valid_partitions_for_prefix[left - 1] if left > 0 else 0)
            ) % MOD
            valid_partitions_for_prefix[right + 1] = (
                valid_partitions_for_prefix[right] + valid_partitions[right + 1]
            ) % MOD

        return valid_partitions[n]
