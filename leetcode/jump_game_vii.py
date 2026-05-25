# 1871. Jump Game VII
# https://leetcode.com/problems/jump-game-vii/


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Sliding window over reachable flags: at index i, `window` counts
        # reachable positions in [i - maxJump, i - minJump]. Position i is
        # reachable if s[i] == '0' and that window is non-empty.
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        window = 0
        for i in range(1, n):
            if i >= minJump:
                window += reachable[i - minJump]
            if i > maxJump:
                window -= reachable[i - maxJump - 1]
            if window > 0 and s[i] == "0":
                reachable[i] = True
        return reachable[-1]
