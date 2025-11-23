# 1262. Greatest Sum Divisible by Three
# https://leetcode.com/problems/greatest-sum-divisible-by-three/

from math import inf
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rems = [inf] * 3
        # we keep only two nums, for which (num % 3) == 1 as we may need to combine them to get rem == 2
        nums_with_rem_one = [inf] * 2
        # we keep only two nums, for which (num % 3) == 2 as we may need to combine them to get rem == 1
        nums_with_rem_two = [inf] * 2
        sm = 0
        for num in nums:
            sm += num
            rem = num % 3
            if rem == 0:
                continue
            elif rem == 2:
                if num > nums_with_rem_two[1]:
                    continue
                nums_with_rem_two[1] = num
                nums_with_rem_two.sort()
                rems[2] = nums_with_rem_two[0]
            else:
                if num > nums_with_rem_one[1]:
                    continue
                nums_with_rem_one[1] = num
                nums_with_rem_one.sort()
                rems[1] = nums_with_rem_one[0]

        rem_to_remove = sm % 3
        if rem_to_remove == 0:
            return sm

        if rem_to_remove == 1:
            candidate_sum = inf
            if rems[1] != inf:
                candidate_sum = sm - rems[1]
            if nums_with_rem_two[0] != inf and nums_with_rem_two[1] != inf:
                second_candidate = sum(nums_with_rem_two)
                candidate_sum = max(candidate_sum, sm - second_candidate)
            if candidate_sum != inf:
                sm = candidate_sum

        elif rem_to_remove == 2:
            candidate = inf
            if rems[2] != inf:
                candidate = rems[2]
            if nums_with_rem_one[0] != inf and nums_with_rem_one[1] != inf:
                second_candidate = sum(nums_with_rem_one)
                if second_candidate < candidate:
                    candidate = second_candidate
            if candidate != inf:
                sm -= candidate

        if sm % 3 == 0:
            return sm
        return 0
