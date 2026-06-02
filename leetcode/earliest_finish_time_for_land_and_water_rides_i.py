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
        def earliest(start1, dur1, start2, dur2):
            # Finish the first ride as early as possible, then start the
            # second no sooner than that and minimize its finish time.
            end1 = min(s + d for s, d in zip(start1, dur1, strict=True))
            return min(
                max(end1, s) + d
                for s, d in zip(start2, dur2, strict=True)
            )

        # The faster overall order is either land first or water first.
        land_first = earliest(
            landStartTime, landDuration, waterStartTime, waterDuration
        )
        water_first = earliest(
            waterStartTime, waterDuration, landStartTime, landDuration
        )
        return min(land_first, water_first)
