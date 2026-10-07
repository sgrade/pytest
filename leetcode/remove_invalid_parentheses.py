# 301. Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/


# Based on Editorial's Approach 1: Backtracking
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        valid_exprs = set()
        min_removed = float("inf")
        expr = []

        # For each parenthesis, try both dropping it and keeping it; letters
        # are always kept. Track open/close counts so that the prefix never
        # has more ")" than "(".
        def backtrack(
            index: int, open_count: int, close_count: int, removed: int
        ) -> None:
            nonlocal valid_exprs, min_removed

            # Already removed more than the best answer found so far.
            if removed > min_removed:
                return

            if index == len(s):
                # Only an excess of "(" can make the expression invalid here.
                if open_count == close_count:
                    # Found a better minimum: discard previous answers.
                    if removed < min_removed:
                        valid_exprs = set()
                        min_removed = removed
                    valid_exprs.add("".join(expr))
                return

            char = s[index]

            if char not in "()":
                expr.append(char)
                backtrack(index + 1, open_count, close_count, removed)
                expr.pop()
                return

            # Option 1: remove the current parenthesis.
            backtrack(index + 1, open_count, close_count, removed + 1)

            # Option 2: keep it; ")" only if it closes an open "(".
            expr.append(char)
            if char == "(":
                backtrack(index + 1, open_count + 1, close_count, removed)
            elif close_count < open_count:
                backtrack(index + 1, open_count, close_count + 1, removed)
            expr.pop()

        backtrack(0, 0, 0, 0)
        return list(valid_exprs)
