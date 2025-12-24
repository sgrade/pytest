# 3074. Apple Redistribution into Boxes
# https://leetcode.com/problems/apple-redistribution-into-boxes/


class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        for i, cap in enumerate(capacity):
            apples -= cap
            if apples <= 0:
                return i + 1
        return len(capacity)
