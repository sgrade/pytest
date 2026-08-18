# 3471. Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

from collections import Counter


class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        # An integer is almost missing if it appears in exactly one
        # contiguous subarray of length k. Cases:
        # - n == k: one window total → every value qualifies → max(nums).
        # - k == 1: windows are single elements → values with count 1.
        # - else: only the endpoints sit in a single window, so they
        #   qualify iff they appear once in the whole array.
        n = len(nums)
        if n == k:
            return max(nums)

        count = Counter(nums)
        if k == 1:
            uniques = [num for num, freq in count.items() if freq == 1]
            return max(uniques) if uniques else -1

        candidates = []
        if count[nums[0]] == 1:
            candidates.append(nums[0])
        if count[nums[-1]] == 1:
            candidates.append(nums[-1])
        return max(candidates) if candidates else -1
