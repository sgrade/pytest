# 3542. Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

from typing import List


# Based on Editorial's Approach: Monotonic stack
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        ops = 0
        for num in nums:
            while st and st[-1] > num:
                st.pop()
            if num == 0:
                continue
            if not st or st[-1] < num:
                ops += 1
                st.append(num)
        return ops
