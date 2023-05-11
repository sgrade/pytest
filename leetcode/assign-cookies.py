# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s = sorted(s)
        g = sorted(g)
        s_idx, g_idx, ans = len(s) - 1, len(g) - 1, 0
        while s_idx >= 0 and g_idx >= 0:
            if s[s_idx] >= g[g_idx]:
                s_idx -= 1
                ans += 1
            g_idx -= 1
        return ans
