# 3633. Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        def get_earliest(start1, duration1, start2, duration2):
            end1 = 10000
            for s1, d1 in zip(start1, duration1, strict=True):
                end1 = min(end1, s1 + d1)
            end2 = 10000
            for s2, d2 in zip(start2, duration2, strict=True):
                end2 = min(end2, max(end1, s2) + d2)
            return end2

        land = get_earliest(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water = get_earliest(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land, water)
