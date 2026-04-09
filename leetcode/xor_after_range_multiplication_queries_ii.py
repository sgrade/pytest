# 3655. XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

from functools import reduce
from operator import xor


# Based on Editorial's Approach: Square Root Decomposition + Difference Array
class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(
        self, nums: list[int], queries: list[list[int]]
    ) -> int:
        n = len(nums)
        block = int(n**0.5)

        # Batch small-step queries by step size; apply large-step directly.
        batches: list[list[tuple[int, int, int]]] = [
            [] for _ in range(block)
        ]
        for left, right, k, v in queries:
            if k < block:
                batches[k].append((left, right, v))
            else:
                for i in range(left, right + 1, k):
                    nums[i] = nums[i] * v % self.MOD

        # Process each small step with a multiplicative difference array.
        diff = [1] * (n + block)
        for k in range(1, block):
            if not batches[k]:
                continue
            diff[:] = [1] * len(diff)
            for left, right, v in batches[k]:
                diff[left] = diff[left] * v % self.MOD
                end = left + ((right - left) // k + 1) * k
                diff[end] = (
                    diff[end] * pow(v, self.MOD - 2, self.MOD) % self.MOD
                )
            # Propagate prefix products with stride k.
            for i in range(k, n):
                diff[i] = diff[i] * diff[i - k] % self.MOD
            for i in range(n):
                nums[i] = nums[i] * diff[i] % self.MOD

        return reduce(xor, nums)
