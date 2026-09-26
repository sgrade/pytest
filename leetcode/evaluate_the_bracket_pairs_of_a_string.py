# 1807. Evaluate the Bracket Pairs of a String
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        ans = []
        # Index right after the most recent "(", or -1 when outside brackets.
        left = -1

        for i, ch in enumerate(s):
            if ch == "(":
                left = i + 1
            elif ch == ")":
                # Replace the bracketed key with its value, or "?" if unknown.
                ans.append(lookup.get(s[left:i], "?"))
                left = -1
            elif left < 0:
                # Plain character outside brackets is copied as-is.
                ans.append(ch)

        return "".join(ans)
