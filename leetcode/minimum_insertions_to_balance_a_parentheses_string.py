# 1541. Minimum Insertions to Balance a Parentheses String
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


class Solution:
    def minInsertions(self, s: str) -> int:
        # Every '(' requires two ')'. Track how many ')' are still owed.
        insertions = 0
        pending_closings = 0

        for char in s:
            if char == "(":
                # An odd debt means the previous '(' got only one ')'.
                # Insert one ')' to complete it before opening a new one.
                if pending_closings % 2 == 1:
                    insertions += 1
                    pending_closings -= 1
                pending_closings += 2
            else:
                pending_closings -= 1
                # No '(' to match: insert one, which itself owes one more ')'.
                if pending_closings < 0:
                    insertions += 1
                    pending_closings += 2

        # Remaining debt must be paid with inserted ')'.
        return insertions + pending_closings
