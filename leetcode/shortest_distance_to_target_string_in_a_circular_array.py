# 2515. Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/


class Solution:
    def closestTarget(
        self, words: list[str], target: str, startIndex: int
    ) -> int:
        n = len(words)
        # Min of clockwise and counter-clockwise distance to each match.
        ans = n
        for i, w in enumerate(words):
            if w == target:
                ans = min(ans, (i - startIndex) % n, (startIndex - i) % n)
        return ans if ans < n else -1
