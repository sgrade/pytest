# 1762. Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/


class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        ans = []
        max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                ans.append(i)
            max_height = max(heights[i], max_height)
        ans.reverse()
        return ans
