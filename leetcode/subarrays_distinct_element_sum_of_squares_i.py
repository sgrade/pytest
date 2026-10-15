# 2913. Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans
