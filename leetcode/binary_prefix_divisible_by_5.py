# 1018. Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        sm = 0
        for i in range(n):
            sm *= 2
            sm = (sm + nums[i]) % 5
            ans[i] = sm == 0
        return ans
