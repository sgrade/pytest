# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

# Based on the Editorial's Approach 3: Using Stack
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        mp = {}
        for el in nums2:
            while st and el > st[-1]:
                mp[st.pop()] = el
            st.append(el)
        while st:
            mp[st.pop()] = -1
        for i in range(len(nums1)):
            nums1[i] = mp[nums1[i]]
        return nums1
