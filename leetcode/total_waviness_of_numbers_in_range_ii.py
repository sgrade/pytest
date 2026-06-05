# 3753. Total Waviness of Numbers in Range II
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

from functools import lru_cache


# Based on Editorial's Approach 1: Digit Dynamic Programming
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Sum of waviness of every number in [0, num].
        def solve(num: int) -> int:
            # Numbers below 100 have fewer than 3 digits, so waviness is 0.
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            # dfs returns (count, waviness_sum) for the suffix starting at pos,
            # given the two preceding digits prev and curr. is_limit: still
            # bounded by num's prefix; is_lead: still in leading zeros.
            @lru_cache(None)
            def dfs(pos, prev, curr, is_limit, is_lead):
                if pos == n:
                    return 1, 0

                cnt = 0
                waviness = 0
                up = int(s[pos]) if is_limit else 9
                for d in range(up + 1):
                    new_lead = is_lead and d == 0
                    new_curr = -1 if new_lead else d
                    sub_cnt, sub_sum = dfs(
                        pos + 1, curr, new_curr,
                        is_limit and d == up, new_lead,
                    )
                    # Count curr as a peak/valley once all three digits exist.
                    if not new_lead and prev >= 0 and curr >= 0:
                        if (prev < curr > d) or (prev > curr < d):
                            waviness += sub_cnt
                    cnt += sub_cnt
                    waviness += sub_sum

                return cnt, waviness

            return dfs(0, -1, -1, True, True)[1]

        return solve(num2) - solve(num1 - 1)
