# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        s_idx, g_idx = 0, 0
        ans = 0
        while s_idx < len(s) and g_idx < len(g):
            if s[s_idx] < g[g_idx]:
                s_idx += 1
                continue
            s_idx += 1
            g_idx += 1
            ans += 1
        return ans
