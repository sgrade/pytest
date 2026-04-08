# 3653. XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/


# Based on Editorial's Approach: Simulation
class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> int:
        # Apply each query: multiply every k-th element in [left, right] by v.
        for left, right, k, v in queries:
            for i in range(left, right + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        # XOR all resulting elements.
        res = 0
        for x in nums:
            res ^= x

        return res
