# 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/

# Based on Editorial's Approach 2: Stack


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # Each stack entry is the score accumulated so far inside one open
        # parenthesis; the bottom entry is the outermost (top-level) score.
        scores = [0]

        for char in S:
            if char == "(":
                # Open a new frame with an empty score.
                scores.append(0)
            else:
                # Close the frame: "()" is worth 1, "(A)" is worth 2 * A.
                inner_score = scores.pop()
                scores[-1] += max(2 * inner_score, 1)

        return scores.pop()
