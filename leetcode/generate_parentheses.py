# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        # Backtracking: build the string one character at a time, keeping
        # only prefixes that can still be completed to a valid combination.
        def backtrack(curr: str, open_count: int, close_count: int) -> None:
            # A complete combination has n pairs, i.e. 2 * n characters.
            if len(curr) == n * 2:
                ans.append(curr)
                return

            # Can add "(" while we haven't used all n opening brackets.
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)

            # Can add ")" only if it closes a previously opened bracket.
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans
