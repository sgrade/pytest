# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect_right(letters, target)
        return letters[0] if idx == len(letters) else letters[idx]
