# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cur_ans = 0
        for ch in s:
            if ch == "(":
                cur_ans += 1
                ans = max(ans, cur_ans)
            if ch == ")":
                cur_ans -= 1
        return ans
