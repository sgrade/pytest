# 3612. Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/


class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for c in s:
            if c == "#":
                ans *= 2        # double
            elif c == "%":
                ans.reverse()   # reverse in-place
            elif c == "*":
                if ans:
                    ans.pop()   # remove last char
            else:
                ans.append(c)
        return "".join(ans)
