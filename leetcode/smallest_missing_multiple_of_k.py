# 3718. Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k/

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st = set(nums)
        temp = k
        while temp <= 100:
            if temp not in st:
                break
            temp += k
        return temp
