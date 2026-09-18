# 1520. Maximum Number of Non-Overlapping Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/


# Based on Editorial's Approach 1: Greedy
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [-1] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        def interval_end(left: int) -> int:
            # Grow [left, right] until every letter inside has all of its
            # occurrences in the range. Fail if any letter starts before left.
            right = last[ord(s[left]) - ord("a")]
            i = left
            while i <= right:
                idx = ord(s[i]) - ord("a")
                if first[idx] < left:
                    return -1
                right = max(right, last[idx])
                i += 1
            return right

        # One candidate valid interval per unique letter.
        intervals = []
        for idx in range(26):
            if first[idx] == -1:
                continue
            left = first[idx]
            right = interval_end(left)
            if right != -1:
                intervals.append((right, left))

        # Take earliest-ending non-overlapping intervals (max count, then
        # shortest total length).
        intervals.sort()
        ans = []
        prev_end = -1
        for right, left in intervals:
            if left > prev_end:
                ans.append(s[left : right + 1])
                prev_end = right
        return ans
