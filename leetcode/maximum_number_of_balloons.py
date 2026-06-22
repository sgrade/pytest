# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have: list = [0] * 26
        for c in text:
            have[ord(c) - 97] += 1

        target = "balloon"
        need: list = [0] * 26
        for c in target:
            need[ord(c) - 97] += 1

        ans = len(text) // len(target)
        for i, cnt in enumerate(need):
            if cnt == 0:
                continue
            ans = min(ans, have[i] // cnt)
        return ans
