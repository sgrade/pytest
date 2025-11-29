# 3512. Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k
