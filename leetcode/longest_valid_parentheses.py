# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

# Based on Editorial's Approach 3: Using Stack


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        # The stack holds indices. The bottom is always the index just before
        # the current valid substring (-1 initially).
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                continue

            # Try to match this ")" with the latest unmatched "(".
            stack.pop()
            if not stack:
                # Unmatched ")": it becomes the new base index.
                stack.append(i)
            else:
                # Valid substring spans from just after the new top to i.
                ans = max(ans, i - stack[-1])

        return ans
