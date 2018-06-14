# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """
        # https://www.geeksforgeeks.org/python-intersection-two-lists/
        # Method 5 simplified, modified
        # doesn't work when intersection includes several repetitions of the same figure, e.g. [2, 2]
        if len(nums1) > len(nums2):
            return [x for x in nums1 if x in set(nums2)]
            # return list(filter(lambda x: x in nums1, nums2))
        else:
            return [x for x in nums2 if x in set(nums1)]
            # return list(filter(lambda x: x in nums2, nums1))
        """

        # Your runtime beats 32.10 % of python3 submissions.
        # Runtime: 76 ms
        if len(nums1) > len(nums2):
            list1 = nums1
            list2 = nums2
        else:
            list1 = nums2
            list2 = nums1

        list_to_return = []
        for item in list2:
            if item in list1:
                list_to_return.append(item)
                list1.remove(item)

        return list_to_return


sol = Solution()

inp1 = [1, 2, 2, 1]
inp2 = [2, 2]
print(sol.intersect(inp1, inp2))    # Expected [2, 2]

inp1 = [1]
inp2 = [1, 1]
print(sol.intersect(inp1, inp2))    # Expected [1]

inp1 = [3, 1, 2]
inp2 = [1, 1]
print(sol.intersect(inp1, inp2))    # Expected [1]

inp1 = [1, 2, 2, 1]
inp2 = [2, 2]
print(sol.intersect(inp1, inp2))    # Expected [2, 2]

inp1 = [1, 2, 2, 2, 1]
inp2 = [2, 2]
print(sol.intersect(inp1, inp2))    # Expected [2, 2]
