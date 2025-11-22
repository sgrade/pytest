# 3190. Find Minimum Operations to Make All Elements Divisible by Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += min(num % 3, (num // 3 + 1) * 3 - num)
        return ans
