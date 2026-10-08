# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        stack = []
        for ch in s:
            if ch == ")":
                stack.pop()
            if stack:
                ans.append(ch)
            if ch == "(":
                stack.append(ch)
        return "".join(ans)
