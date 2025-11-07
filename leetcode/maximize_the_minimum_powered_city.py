# 2528. Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

from typing import List


# Based on Editorial's Approach: Binary Search + Difference Array
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff_array = [0] * (n + 1)
        for i in range(n):
            left = max(0, i - r)
            # The first city, which the power stations from i-th city do not cover
            right = min(n, i + r + 1)
            diff_array[left] += stations[i]
            diff_array[right] -= stations[i]

        def is_possible(target_power: int) -> bool:
            prefix_sum = diff_array.copy()
            power_at_city, can_add = 0, k

            for i in range(n):
                power_at_city += prefix_sum[i]
                if power_at_city < target_power:
                    additional_power = target_power - power_at_city
                    if additional_power > can_add:
                        return False
                    can_add -= additional_power
                    # We add the power station to i + r, so it covers range [i, i + 2*r]
                    # The first city outside the augmented coverage window
                    exclusive_end = min(n, i + 2 * r + 1)
                    prefix_sum[exclusive_end] -= additional_power
                    power_at_city += additional_power
            return True

        lo, hi = min(stations), sum(stations) + k
        min_power_in_city = 0
        while lo <= hi:
            target_power = (lo + hi) // 2
            if is_possible(target_power):
                min_power_in_city = target_power
                lo = target_power + 1
            else:
                hi = target_power - 1
        return min_power_in_city
