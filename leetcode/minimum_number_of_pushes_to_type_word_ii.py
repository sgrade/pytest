# 3016. Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        cntr = Counter(word)
        ans = 0
        keys_used = 0
        for cnt in sorted(cntr.values(), reverse=True):
            ans += (keys_used // 8 + 1) * cnt
            keys_used += 1
        return ans
